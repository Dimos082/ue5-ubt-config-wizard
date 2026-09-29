"""Read, edit and save one UnrealBuildTool XML profile.

The editor changes only direct scalar children of a configuration category. Other
XML remains in the tree, so settings this version does not understand survive a
save. The persistence code deliberately does not modify the original in place.

XML root and namespace: https://dev.epicgames.com/documentation/en-us/unreal-engine/
horde-unreal-build-accelerator-and-remote-compilation-tutorial-for-unreal-engine
"""

from __future__ import annotations

import hashlib
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from lxml import etree

NAMESPACE = "https://www.unrealengine.com/BuildConfiguration"
ROOT_TAG = f"{{{NAMESPACE}}}Configuration"
MAX_XML_BYTES = 8 * 1024 * 1024
XML_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*\Z")


class ProfileError(Exception):
    """A profile cannot be read, edited or saved safely."""


@dataclass(frozen=True)
class Entry:
    category: str
    name: str
    value: str


def _parse(data: bytes) -> etree._Element:
    if not data:
        raise ProfileError("The XML file is empty.")
    if len(data) > MAX_XML_BYTES:
        raise ProfileError(f"XML exceeds the {MAX_XML_BYTES // (1024 * 1024)} MiB limit.")

    # No DTD loading, external entities, network, or recovery of malformed XML.
    # Parser controls: https://lxml.de/parsing.html
    parser = etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        recover=False,
        remove_comments=False,
        remove_pis=False,
        remove_blank_text=False,
        huge_tree=False,
    )
    try:
        root = etree.fromstring(data, parser=parser)
    except (etree.XMLSyntaxError, ValueError) as exc:
        raise ProfileError(f"Invalid XML: {exc}") from exc

    if root.getroottree().docinfo.doctype:
        raise ProfileError("DTD declarations are not supported in profiles.")
    if root.tag != ROOT_TAG:
        raise ProfileError("Expected <Configuration> in the Unreal BuildConfiguration namespace.")
    return root


def _local_name(tag: str) -> str:
    return etree.QName(tag).localname


def _qualified(name: str) -> str:
    if not XML_NAME.fullmatch(name):
        raise ProfileError(f"Invalid XML setting name: {name!r}")
    return f"{{{NAMESPACE}}}{name}"


def _file_identity(path: Path) -> tuple[int, int, int]:
    info = path.stat()
    return info.st_dev, info.st_ino, info.st_mtime_ns


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ProfileDocument:
    """An in-memory editable copy plus a snapshot of the loaded file."""

    def __init__(
        self,
        root: etree._Element,
        original: bytes | None,
        path: Path | None,
        identity: tuple[int, int, int] | None,
    ) -> None:
        self.root = root
        self.original = original
        self.path = path
        self._identity = identity
        self._dirty = False
        self._had_declaration = bool(original and original.lstrip().startswith(b"<?xml"))
        self._encoding = root.getroottree().docinfo.encoding or "UTF-8"

    @classmethod
    def open(cls, path: Path | str) -> ProfileDocument:
        path = Path(path).expanduser().absolute()
        if path.is_symlink():
            raise ProfileError("Symbolic-link profiles are read-only in this version.")
        try:
            data = path.read_bytes()
            identity = _file_identity(path)
        except OSError as exc:
            raise ProfileError(f"Cannot read {path}: {exc}") from exc
        return cls(_parse(data), data, path, identity)

    @classmethod
    def new(cls) -> ProfileDocument:
        root = etree.Element(ROOT_TAG, nsmap={None: NAMESPACE})
        return cls(root, None, None, None)

    @property
    def dirty(self) -> bool:
        return self._dirty

    def entries(self) -> list[Entry]:
        """Return visible scalar settings; unsupported nested nodes stay intact."""
        result: list[Entry] = []
        for category in self.root:
            if not isinstance(category.tag, str) or etree.QName(category).namespace != NAMESPACE:
                continue
            for setting in category:
                if (
                    isinstance(setting.tag, str)
                    and etree.QName(setting).namespace == NAMESPACE
                    and not len(setting)
                ):
                    result.append(
                        Entry(
                            _local_name(category.tag), _local_name(setting.tag), setting.text or ""
                        )
                    )
        return result

    def _categories(self, category: str) -> list[etree._Element]:
        tag = _qualified(category)
        return [item for item in self.root if item.tag == tag]

    def _setting(self, category: str, name: str) -> tuple[etree._Element, etree._Element] | None:
        found: list[tuple[etree._Element, etree._Element]] = []
        for parent in self._categories(category):
            found.extend((parent, item) for item in parent if item.tag == _qualified(name))
        if len(found) > 1:
            raise ProfileError(f"Duplicate XML setting {category}/{name}; edit the file manually.")
        return found[0] if found else None

    def set(self, category: str, name: str, value: str) -> None:
        if not isinstance(value, str):
            raise ProfileError("Setting values must be text after type validation.")
        current = self._setting(category, name)
        if current is None:
            categories = self._categories(category)
            if len(categories) > 1:
                raise ProfileError(f"Duplicate {category} categories need manual review.")
            parent = (
                categories[0] if categories else etree.SubElement(self.root, _qualified(category))
            )
            setting = etree.SubElement(parent, _qualified(name))
            setting.text = value
            self._dirty = True
        elif (current[1].text or "") != value:
            if len(current[1]):
                raise ProfileError("Nested XML settings cannot be edited as plain text.")
            current[1].text = value
            self._dirty = True

    def remove(self, category: str, name: str) -> None:
        current = self._setting(category, name)
        if current is not None:
            parent, setting = current
            # A comment immediately before a setting documents that setting.
            # Keep comments elsewhere, including category-level notes.
            previous = setting.getprevious()
            gap = (previous.tail or "") if previous is not None else ""
            if isinstance(previous, etree._Comment) and not gap.strip() and gap.count("\n") <= 1:
                parent.remove(previous)
            parent.remove(setting)
            # Retain the category and all unrelated nodes and comments.
            self._dirty = True

    def render(self) -> bytes:
        if not self._dirty and self.original is not None:
            return self.original

        # UBT profiles contain elements and comments, not mixed prose. Reindent
        # edited trees so both new profiles and additions to compact XML remain
        # readable. Leave mixed-content extensions alone: their whitespace may
        # be significant to another tool.
        def has_mixed_content(element: etree._Element) -> bool:
            for node in element.iter():
                if not isinstance(node.tag, str):
                    continue
                if len(node) and node.text and node.text.strip():
                    return True
                if any(child.tail and child.tail.strip() for child in node):
                    return True
            return False

        if not has_mixed_content(self.root):
            etree.indent(self.root, space="  ")
        return etree.tostring(
            self.root.getroottree(),
            encoding=self._encoding,
            xml_declaration=self._had_declaration or self.original is None,
            pretty_print=False,
        )

    @staticmethod
    def _write_backup(path: Path, original: bytes) -> Path:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = path.with_name(f"{path.name}.{stamp}.{uuid4().hex[:8]}.bak")
        try:
            with backup.open("xb") as stream:
                stream.write(original)
                stream.flush()
                os.fsync(stream.fileno())
            if backup.read_bytes() != original:
                raise ProfileError("Backup verification failed.")
        except (OSError, ProfileError) as exc:
            backup.unlink(missing_ok=True)
            raise ProfileError(f"Could not make a verified backup: {exc}") from exc
        return backup

    def backup(self) -> Path:
        if self.path is None:
            raise ProfileError("Save the new profile before backing it up.")
        if self.path.is_symlink():
            raise ProfileError("Symbolic-link profiles are read-only in this version.")
        try:
            original = self.path.read_bytes()
        except OSError as exc:
            raise ProfileError(f"Cannot read the current profile: {exc}") from exc
        return self._write_backup(self.path, original)

    def save(self, target: Path | str, *, allow_overwrite: bool = False) -> Path | None:
        """Save staged XML, returning the backup path when one was needed.

        Existing targets get an exact backup first. A new target is installed by
        exclusive hard link so an unrelated file created while we save is never
        overwritten. Existing targets use same-directory atomic replacement.
        """
        target = Path(target).expanduser().absolute()
        if target.is_symlink():
            raise ProfileError("Symbolic-link destinations are not supported.")
        same_target = self.path is not None and target == self.path
        if target.exists() and not same_target and not allow_overwrite:
            raise ProfileError("The destination exists. Confirm overwrite in Save As first.")

        try:
            target.parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise ProfileError(f"Cannot create the destination directory: {exc}") from exc

        try:
            existed = target.exists()
            disk_bytes = target.read_bytes() if existed else None
            disk_identity = _file_identity(target) if existed else None
        except OSError as exc:
            raise ProfileError(f"Cannot inspect the destination: {exc}") from exc

        if same_target:
            if disk_bytes is None:
                raise ProfileError("The profile disappeared; reload or use Save As.")
            if self.original is None or _digest(disk_bytes) != _digest(self.original):
                raise ProfileError("The profile changed on disk; reload or use Save As.")
            if disk_identity != self._identity:
                raise ProfileError("The profile was replaced externally; reload it first.")
        if not self._dirty and same_target:
            return None

        output = self.render()
        _parse(output)  # Do not write malformed output even if the in-memory tree changed.
        temp_path: Path | None = None
        backup: Path | None = None
        replaced = False
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix=f".{target.name}.", suffix=".tmp", dir=target.parent, delete=False
            ) as stream:
                temp_path = Path(stream.name)
                stream.write(output)
                stream.flush()
                os.fsync(stream.fileno())
            _parse(temp_path.read_bytes())

            if existed:
                if target.is_symlink() or not target.exists():
                    raise ProfileError(
                        "The destination changed while saving; no overwrite occurred."
                    )
                if _file_identity(target) != disk_identity or target.read_bytes() != disk_bytes:
                    raise ProfileError("The destination changed while saving; reload it first.")
                backup = self._write_backup(target, disk_bytes)
                # Best-effort second check narrows the overwrite race.
                if _file_identity(target) != disk_identity or target.read_bytes() != disk_bytes:
                    raise ProfileError(
                        "The destination changed after backup; no overwrite occurred."
                    )
                os.chmod(temp_path, stat.S_IMODE(target.stat().st_mode))
                os.replace(temp_path, target)
            else:
                # `replace` would silently clobber a file created during Save As.
                os.link(temp_path, target)
                temp_path.unlink()
            replaced = True
        except (OSError, ProfileError) as exc:
            if replaced:
                raise ProfileError(
                    f"The file was replaced, but finishing the save failed: {exc}. "
                    f"Inspect {target} and the backup."
                ) from exc
            raise ProfileError(f"Save cancelled; original unchanged: {exc}") from exc
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)

        # The disk operation is committed. If refresh fails, the backup is still
        # available and the error names the exact file to inspect.
        try:
            self.path = target
            self.original = output
            self._identity = _file_identity(target)
            self._dirty = False
        except OSError as exc:
            raise ProfileError(
                f"Saved {target}, but could not refresh its file identity: {exc}. "
                f"Inspect the file and backup {backup}."
            ) from exc
        return backup
