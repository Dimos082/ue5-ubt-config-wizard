"""Offline documented settings and a conservative, local XSD inventory reader.

XSD establishes XML shapes, not runtime defaults, availability, or semantics.
Nothing in this module downloads sources, runs Unreal, or writes a profile.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from pathlib import Path

from lxml import etree

from .catalog_data import DOCUMENTED_SETTINGS, DOCUMENTED_VERSION, RETRIEVED, SOURCE
from .catalog_explanations import EXPLANATIONS

NAMESPACE = "https://www.unrealengine.com/BuildConfiguration"
XSD = "http://www.w3.org/2001/XMLSchema"
XS = {"xs": XSD}
MAX_SCHEMA_BYTES = 8 * 1024 * 1024


@dataclass(frozen=True)
class Setting:
    category: str
    name: str
    description: str
    kind: str = "unknown"
    source: str = SOURCE
    status: str = "documented; type and meaning need review"
    xml_type: str = ""
    choices: tuple[str, ...] = ()
    evidence_version: str = DOCUMENTED_VERSION
    schema_source: str = ""
    item_kind: str = ""
    has_reviewed_description: bool = False
    schema_sha256: str = ""


# Concise original descriptions of commonly requested settings. The linked
# reference supports these specific descriptions, not all runtime defaults.
# Source: https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine
_COMMON = {
    ("BuildConfiguration", "bAllowUBAExecutor"): ("bool", "Permit the UBA executor."),
    ("BuildConfiguration", "bAllowUBALocalExecutor"): (
        "bool",
        "Permit local-only UBA; this does not disable remote UBA.",
    ),
    ("BuildConfiguration", "MaxParallelActions"): (
        "int",
        "Concurrent action limit; zero requests automatic selection.",
    ),
    ("BuildConfiguration", "bUseUnityBuild"): (
        "bool",
        "Combine translation units for compilation.",
    ),
    ("BuildConfiguration", "bAdaptiveUnityDisablesOptimizations"): (
        "bool",
        "Disable optimization within the adaptive non-unity working set.",
    ),
    ("BuildConfiguration", "bUseUBTMakefiles"): (
        "bool",
        "Cache target information between builds.",
    ),
    ("BuildConfiguration", "bPrintDebugInfo"): ("bool", "Print UBT diagnostic information."),
    ("BuildConfiguration", "bCompactOutput"): (
        "bool",
        "Request compact executor output when supported.",
    ),
    ("BuildConfiguration", "bAllowFASTBuild"): ("bool", "Permit FASTBuild when available."),
    ("BuildConfiguration", "bAllowXGE"): ("bool", "Permit XGE when available."),
    ("BuildConfiguration", "bArtifactRead"): ("bool", "Allow artifact reads."),
    ("BuildConfiguration", "bArtifactWrites"): ("bool", "Allow artifact writes."),
    ("BuildConfiguration", "bEnableAddressSanitizer"): (
        "bool",
        "Request ASan; check platform and toolchain support.",
    ),
    ("UnrealBuildAccelerator", "bLaunchVisualizer"): (
        "bool",
        "Open UBA's build-progress visualizer.",
    ),
    ("UnrealBuildAccelerator", "bForceBuildAllRemote"): (
        "bool",
        "Force remotely eligible actions remote; unavailable agents can stall builds.",
    ),
    ("UnrealBuildAccelerator", "CacheDesiredConnectionCount"): (
        "int",
        "Desired cache TCP connection count.",
    ),
    ("WindowsPlatform", "CompilerVersion"): (
        "string",
        "Compiler version selector; documented selectors include Latest and Preview.",
    ),
    ("WindowsPlatform", "WindowsSdkVersion"): (
        "string",
        "Windows SDK version selector; Latest is also supported.",
    ),
    ("SourceFileWorkingSet", "GitPath"): ("string", "Git executable location."),
    ("SourceFileWorkingSet", "RepositoryPath"): (
        "string",
        "Working-set repository path; relative paths use the engine root.",
    ),
}


def _documented() -> dict[tuple[str, str], Setting]:
    records = {}
    for category, name in DOCUMENTED_SETTINGS:
        common = _COMMON.get((category, name))
        explanation = EXPLANATIONS.get((category, name))
        records[(category, name)] = Setting(
            category=category,
            name=name,
            description=(
                common[1]
                if common
                else explanation
                or "Epic lists this XML setting. Its meaning, accepted values and defaults "
                "have not been reviewed for this catalog. Open the source before using it."
            ),
            kind=common[0] if common else "unknown",
            status=(
                "documented; installation not verified"
                if common
                else (
                    "documented explanation; value type unverified"
                    if explanation
                    else "documented; type and meaning need review"
                )
            ),
            has_reviewed_description=common is not None or explanation is not None,
        )
    return records


def _engine_directory(engine: str | Path) -> Path:
    selected = Path(engine).expanduser().resolve()
    # Accept either the installation root or its Engine directory.
    return selected / "Engine" if (selected / "Engine").is_dir() else selected


def _engine_version(directory: Path) -> str:
    try:
        descriptor = directory / "Build" / "Build.version"
        if descriptor.stat().st_size > 64 * 1024:
            return "unknown"
        data = json.loads(descriptor.read_text(encoding="utf-8-sig"))
        parts = [data[key] for key in ("MajorVersion", "MinorVersion", "PatchVersion")]
        if any(type(value) is not int or value < 0 for value in parts):
            return "unknown"
        return ".".join(str(value) for value in parts)
    except (OSError, ValueError, KeyError, TypeError):
        return "unknown"


def schema_path(engine: str | Path | None) -> Path | None:
    """Return an existing candidate, without promising it matches the engine build.

    Historical location evidence:
    https://forums.unrealengine.com/t/buildconfiguration-xml-invalid-child-error/452777/2
    The path is only probed; no engine execution or schema generation occurs.
    """
    if engine is None:
        return None
    candidate = _engine_directory(engine) / "Saved/UnrealBuildTool/BuildConfiguration.Schema.xsd"
    return candidate if candidate.is_file() else None


class SchemaInventoryError(ValueError):
    """The local schema cannot be safely inventoried with this reader."""


def _read_schema(path: Path) -> tuple[etree._Element, str]:
    with path.open("rb") as stream:
        raw = stream.read(MAX_SCHEMA_BYTES + 1)
    if len(raw) > MAX_SCHEMA_BYTES:
        raise SchemaInventoryError("Schema exceeds the 8 MiB inventory limit.")
    # Explicit parser security options: https://lxml.de/parsing.html
    parser = etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        recover=False,
        huge_tree=False,
    )
    try:
        root = etree.fromstring(raw, parser)
    except etree.XMLSyntaxError as exc:
        raise SchemaInventoryError(f"Malformed schema: {exc}") from exc
    if root.getroottree().docinfo.doctype:
        raise SchemaInventoryError("DTD declarations are not allowed in schemas.")
    if root.tag != f"{{{XSD}}}schema" or root.get("targetNamespace") != NAMESPACE:
        raise SchemaInventoryError("Schema is not for the UBT Configuration namespace.")
    if any(root.find(f"xs:{tag}", XS) is not None for tag in ("include", "import", "redefine")):
        raise SchemaInventoryError("External or composed schemas require explicit review.")
    try:
        etree.XMLSchema(root)
    except etree.XMLSchemaParseError as exc:
        raise SchemaInventoryError(f"Invalid schema: {exc}") from exc
    return root, hashlib.sha256(raw).hexdigest()


def _local_name(value: str) -> str:
    return value.rsplit(":", 1)[-1]


def schema_inventory(path: str | Path) -> list[Setting]:
    """Inventory the supported UBT schema shape without executing engine code.

    Unknown complex types remain visible and read-only. A schema found beside an
    engine is local evidence, not independently verified engine provenance.
    """
    path = Path(path).resolve()
    root, digest = _read_schema(path)
    complex_types = {item.get("name"): item for item in root.findall("xs:complexType", XS)}
    simple_types = {item.get("name"): item for item in root.findall("xs:simpleType", XS)}
    elements = {item.get("name"): item for item in root.findall("xs:element", XS)}
    groups = {item.get("name"): item for item in root.findall("xs:group", XS)}

    def dereference(node):
        if node.get("ref"):
            referred = elements.get(_local_name(node.get("ref")))
            if referred is None:
                raise SchemaInventoryError("Unresolved element reference.")
            return referred
        return node

    def complex_type(node):
        inline = node.find("xs:complexType", XS)
        return (
            inline if inline is not None else complex_types.get(_local_name(node.get("type", "")))
        )

    def children(node, visited=frozenset()):
        found = []
        for child in node:
            if child.tag == f"{{{XSD}}}element":
                found.append(dereference(child))
            elif child.tag in {f"{{{XSD}}}{tag}" for tag in ("all", "sequence", "choice")}:
                found.extend(children(child, visited))
            elif child.tag == f"{{{XSD}}}group":
                name = _local_name(child.get("ref", ""))
                if name in visited or name not in groups:
                    raise SchemaInventoryError("Unsupported or recursive schema group.")
                found.extend(children(groups[name], visited | {name}))
            elif child.tag not in {f"{{{XSD}}}annotation", f"{{{XSD}}}attribute"}:
                raise SchemaInventoryError("Unsupported schema container; inventory is incomplete.")
        return found

    def value_type(node, visited=frozenset()):
        type_name = _local_name(node.get("type", ""))
        simple = node.find("xs:simpleType", XS)
        if simple is None:
            simple = simple_types.get(type_name)
        if simple is not None:
            if type_name and type_name in visited:
                return "unknown", type_name, ()
            restriction = simple.find("xs:restriction", XS)
            if restriction is None:
                return "unknown", type_name, ()
            choices = tuple(item.get("value") for item in restriction.findall("xs:enumeration", XS))
            if choices:
                return "enum", type_name or restriction.get("base", ""), choices
            type_name = _local_name(restriction.get("base", ""))
            # Restriction facets require the full schema for validation; never
            # advertise an unconstrained scalar editor for them.
            if any(item.tag != f"{{{XSD}}}annotation" for item in restriction):
                return "unknown", type_name, ()
            if type_name in simple_types:
                proxy = etree.Element(f"{{{XSD}}}element", type=type_name)
                return value_type(proxy, visited | {_local_name(node.get("type", ""))})
        kinds = {
            "boolean": "bool",
            "byte": "int",
            "short": "int",
            "int": "int",
            "long": "int",
            "integer": "int",
            "unsignedByte": "int",
            "unsignedShort": "int",
            "unsignedInt": "int",
            "unsignedLong": "int",
            "positiveInteger": "int",
            "nonNegativeInteger": "int",
            "negativeInteger": "int",
            "nonPositiveInteger": "int",
            "float": "float",
            "double": "float",
            "decimal": "float",
            "string": "string",
            "normalizedString": "string",
            "token": "string",
        }
        return kinds.get(type_name, "unknown"), type_name, ()

    configuration = elements.get("Configuration")
    if configuration is None:
        raise SchemaInventoryError("Schema has no Configuration element.")
    container = complex_type(configuration)
    if container is None:
        raise SchemaInventoryError("Configuration has no supported complex type.")
    records = []
    seen = set()
    for category in children(container):
        category_name = category.get("name", "")
        category_type = complex_type(category)
        if not category_name or category_type is None:
            raise SchemaInventoryError("Unsupported category shape; inventory is incomplete.")
        for node in children(category_type):
            name = node.get("name", "")
            identity = (category_name, name)
            if not name or identity in seen:
                raise SchemaInventoryError("Duplicate or unnamed XML setting in schema.")
            seen.add(identity)
            kind, xml_type, choices = value_type(node)
            item_kind = ""
            nested = complex_type(node)
            if nested is not None:
                try:
                    items = children(nested)
                except SchemaInventoryError:
                    items = []
                kind = "unknown"
                if len(items) == 1 and items[0].get("name") == "Item":
                    kind = "list"
                    item_kind, xml_type, choices = value_type(items[0])
            records.append(
                Setting(
                    category_name,
                    name,
                    "Found in a local XML schema. Meaning, defaults and runtime applicability "
                    "still require source review.",
                    kind=kind,
                    source=path.as_uri(),
                    status="local schema; semantics unverified",
                    xml_type=xml_type,
                    choices=choices,
                    evidence_version="local schema",
                    schema_source=str(path),
                    item_kind=item_kind,
                    schema_sha256=digest,
                )
            )
    if not records:
        raise SchemaInventoryError("Schema inventory contains no XML settings.")
    return records


def catalog_report(engine: str | Path | None = None) -> dict:
    """Return settings plus explicit coverage and local-schema provenance limits."""
    records = _documented()
    warnings = []
    path = None
    local = []
    version = "not selected"
    if engine is None:
        warnings.append("No engine selected; bundled documentation is not installation-verified.")
    if engine is not None:
        version = _engine_version(_engine_directory(engine))
        path = schema_path(engine)
        if path is not None:
            try:
                local = schema_inventory(path)
            except (OSError, SchemaInventoryError) as exc:
                warnings.append(str(exc))
        if not local:
            warnings.append("No usable local schema; installation compatibility is unverified.")
        if not version.startswith(f"{DOCUMENTED_VERSION}."):
            warnings.append(
                f"Bundled documentation is UE {DOCUMENTED_VERSION}; selected version is {version}."
            )
    if local:
        # Retain every documentation candidate, but do not allow adding entries
        # absent from this local schema. They may belong to another release.
        records = {
            key: replace(value, kind="unknown", status="not present in selected local schema")
            for key, value in records.items()
        }
        for record in local:
            key = (record.category, record.name)
            documented = records.get(key)
            if documented:
                record = replace(
                    record,
                    description=documented.description,
                    source=documented.source,
                    evidence_version=f"local schema; description from UE {DOCUMENTED_VERSION}",
                    has_reviewed_description=documented.has_reviewed_description,
                    status="local schema; runtime compatibility unverified",
                )
            records[key] = record
        warnings.append(
            "A colocated schema's correspondence to the engine binary is not independently verified."
        )
    elif engine is not None and not version.startswith(f"{DOCUMENTED_VERSION}."):
        records = {
            key: replace(
                value, kind="unknown", status="documentation version differs; verify before editing"
            )
            for key, value in records.items()
        }
    result = sorted(
        records.values(), key=lambda item: (item.category.casefold(), item.name.casefold())
    )
    return {
        "settings": result,
        "documented_version": DOCUMENTED_VERSION,
        "retrieved": RETRIEVED,
        "engine_version": version,
        "documented_count": len(DOCUMENTED_SETTINGS),
        "local_schema_count": len(local),
        "schema_path": str(path) if path else None,
        "schema_sha256": local[0].schema_sha256 if local else None,
        "editable_scalar_count": sum(
            item.kind in {"bool", "int", "float", "enum", "string"} for item in result
        ),
        "description_gap_count": sum(not item.has_reviewed_description for item in result),
        "codec_gap_count": sum(item.kind in {"unknown", "list"} for item in result),
        "warnings": warnings,
    }


def settings(engine: str | Path | None = None) -> list[Setting]:
    """Return documented candidates, enriched by a safe local schema when present."""
    return catalog_report(engine)["settings"]


def validate_document(xml_bytes: bytes, engine: str | Path | None) -> list[str]:
    """Return local XSD errors, or an explicit lack-of-verification diagnostic.

    An empty result only means this document satisfies this local schema. It is
    not proof that the schema matches the selected engine binary or that UBT
    consumed the profile. Imports, DTDs and external entities are never loaded.
    """
    path = schema_path(engine)
    if path is None:
        return ["No local UBT schema is available; schema validation is unverified."]
    if len(xml_bytes) > MAX_SCHEMA_BYTES:
        return ["XML exceeds the 8 MiB schema-validation limit."]
    try:
        schema_root, _ = _read_schema(path)
        parser = etree.XMLParser(
            resolve_entities=False,
            load_dtd=False,
            no_network=True,
            recover=False,
            huge_tree=False,
        )
        document = etree.fromstring(xml_bytes, parser)
        if document.getroottree().docinfo.doctype:
            return ["DTD declarations are not allowed in configuration XML."]
        schema = etree.XMLSchema(schema_root)
        if schema.validate(document):
            return []
        return [f"Line {item.line}: {item.message}" for item in schema.error_log]
    except (OSError, SchemaInventoryError, etree.XMLSyntaxError) as exc:
        return [str(exc)]
