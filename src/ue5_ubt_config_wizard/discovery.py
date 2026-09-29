"""Find likely UBT XML locations without scanning the whole computer.

Candidate locations come from Epic's Build Configuration reference. Their order
is for display only; it does not claim UnrealBuildTool precedence.
https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configuration-for-unreal-engine
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

PROFILE_NAME = "BuildConfiguration.xml"


def engine_directory(selected: Path) -> Path:
    """Accept an installation root or its Engine subdirectory."""
    selected = Path(selected).expanduser()
    child = selected / "Engine"
    return child if child.is_dir() else selected


def _documents_dir(home: Path) -> Path:
    """Respect a redirected Windows Documents folder when Windows supplies one."""
    if sys.platform == "win32":
        try:
            import winreg

            key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                value, _ = winreg.QueryValueEx(key, "Personal")
            return Path(os.path.expandvars(value)).expanduser()
        except (ImportError, OSError, ValueError):
            pass
    return home / "Documents"


def candidate_profiles(engine: Path | None = None, project: Path | None = None) -> list[Path]:
    """Return documented candidate paths, including paths that do not yet exist."""
    home = Path.home()
    user_config = Path("Unreal Engine") / "UnrealBuildTool" / PROFILE_NAME
    paths: list[Path] = []
    if sys.platform == "win32":
        if engine is not None:
            paths.append(engine_directory(engine) / "Saved" / "UnrealBuildTool" / PROFILE_NAME)
        appdata = Path(os.environ.get("APPDATA", str(home / "AppData" / "Roaming")))
        paths.extend([appdata / user_config, _documents_dir(home) / user_config])
    else:
        paths.append(home / ".config" / user_config)
        if sys.platform.startswith("linux"):
            paths.append(_documents_dir(home) / user_config)
    if project is not None:
        project_path = Path(project).expanduser()
        directory = (
            project_path.parent if project_path.suffix.lower() == ".uproject" else project_path
        )
        paths.append(directory / "Saved" / "UnrealBuildTool" / PROFILE_NAME)

    # Dict preserves discovery order and removes a duplicate on unusual layouts.
    return list(dict.fromkeys(path.absolute() for path in paths))


def engine_version(engine: Path) -> str | None:
    """Read an installed engine's actual version descriptor, if present."""
    root = Path(engine).expanduser()
    for candidate in (
        root / "Engine" / "Build" / "Build.version",
        root / "Build" / "Build.version",
    ):
        try:
            data = json.loads(candidate.read_text(encoding="utf-8-sig"))
            major = int(data["MajorVersion"])
            minor = int(data["MinorVersion"])
            patch = int(data["PatchVersion"])
            if major < 0 or minor < 0 or patch < 0:
                return None
            return f"{major}.{minor}.{patch}"
        except (OSError, ValueError, TypeError, KeyError):
            continue
    return None
