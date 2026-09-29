"""Suggest a local Unreal build command and stop only a process we started.

The preset is a suggestion, not a dry run or proof that a particular XML profile
was consumed. Users can inspect the executable, arguments and directory first.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import psutil

from .discovery import engine_directory


def _dotnet_for(engine: Path) -> str | None:
    third_party = engine_directory(engine) / "Binaries" / "ThirdParty" / "DotNet"
    executable = "dotnet.exe" if sys.platform == "win32" else "dotnet"
    if third_party.is_dir():
        # UBT installations can bundle different SDK directory names. Searching
        # only this known engine directory avoids a machine-wide executable scan.
        for found in sorted(third_party.glob(f"**/{executable}"), reverse=True):
            if found.is_file():
                return str(found)
    return shutil.which("dotnet")


def default_command(
    engine: Path | None, project: Path | None
) -> tuple[str, list[str], Path] | None:
    """Construct a direct UBT invocation when all required files are available.

    Passing UBT.dll to dotnet avoids the Windows batch-file quoting trap noted
    in Python's subprocess documentation: https://docs.python.org/3/library/subprocess.html
    """
    if engine is None or project is None:
        return None
    engine = Path(engine).expanduser().absolute()
    project = Path(project).expanduser().absolute()
    if not project.is_file() or project.suffix.lower() != ".uproject":
        return None
    ubt = (
        engine_directory(engine) / "Binaries" / "DotNET" / "UnrealBuildTool" / "UnrealBuildTool.dll"
    )
    if not ubt.is_file():
        return None
    dotnet = _dotnet_for(engine)
    if dotnet is None:
        return None
    if sys.platform == "win32":
        platform = "Win64"
    elif sys.platform == "darwin":
        platform = "Mac"
    elif sys.platform.startswith("linux"):
        platform = "Linux"
    else:
        return None
    target = f"{project.stem}Editor"
    return dotnet, [str(ubt), target, platform, "Development", f"-Project={project}"], engine


def terminate_process_tree(pid: int, timeout: float = 3.0) -> None:
    """Terminate a supervised process and its current descendants.

    The caller must pass the PID of the command it started, never a process name.
    psutil handles child enumeration on Windows, macOS and Linux.
    https://psutil.readthedocs.io/en/latest/#psutil.Process.children
    """
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return
    for process in children + [parent]:
        try:
            process.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    _gone, alive = psutil.wait_procs(children + [parent], timeout=timeout)
    for process in alive:
        try:
            process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
