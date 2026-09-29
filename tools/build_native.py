"""Build, smoke-test and archive an unsigned PyInstaller onedir application."""

from __future__ import annotations

import importlib.metadata as metadata
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "ue5-ubt-config-wizard"


def collect_notices(target: Path) -> None:
    """Retain installed runtime metadata and available dependency license texts."""
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
        shutil.copy2(ROOT / name, target / name)
    names = ("PySide6", "PySide6_Addons", "PySide6_Essentials", "shiboken6", "lxml", "psutil")
    for name in names:
        distribution = metadata.distribution(name)
        destination = target / "dependency-notices" / name
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "METADATA.txt").write_text(
            distribution.read_text("METADATA") or "", encoding="utf-8"
        )
        for item in distribution.files or ():
            lowered = str(item).lower()
            if not any(word in lowered for word in ("license", "copying", "copyright", "notice")):
                continue
            source = Path(distribution.locate_file(item))
            if not source.is_file():
                continue
            # Flatten with a hash-free unique sequence: contents and original locator retained.
            number = len(list(destination.iterdir()))
            shutil.copy2(source, destination / f"{number:04d}-{source.name}")
            with (destination / "SOURCE_PATHS.txt").open("a", encoding="utf-8") as stream:
                stream.write(f"{number:04d}-{source.name}: {item}\n")


def main() -> int:
    version = metadata.version(NAME)
    build_env = os.environ.copy()
    if os.name == "nt":
        # PyInstaller searches PATH for imported DLLs. A developer's unrelated
        # tools can supply an incompatible DLL with the same name as a Windows
        # system DLL, so keep the build's DLL search path predictable.
        windows = Path(os.environ.get("SystemRoot", r"C:\Windows"))
        build_env["PATH"] = os.pathsep.join(
            (str(Path(sys.executable).parent), str(windows / "System32"), str(windows))
        )
    build_directory = ROOT / "build" / "native"
    build_directory.mkdir(parents=True, exist_ok=True)
    launcher = build_directory / "launcher.py"
    launcher.write_text(
        "from ue5_ubt_config_wizard.__main__ import main\n"
        "if __name__ == '__main__':\n"
        "    raise SystemExit(main())\n",
        encoding="utf-8",
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--noconfirm",
            "--clean",
            "--onedir",
            *(["--windowed"] if os.name == "nt" else []),
            *(["--icon", str(ROOT / "packaging/app_icon.ico")] if os.name == "nt" else []),
            "--name",
            NAME,
            "--distpath",
            str(ROOT / "dist" / "native"),
            "--workpath",
            str(build_directory / "work"),
            "--specpath",
            str(build_directory),
            "--collect-data",
            "ue5_ubt_config_wizard",
            "--recursive-copy-metadata",
            "PySide6",
            "--copy-metadata",
            "lxml",
            "--copy-metadata",
            "psutil",
            str(launcher),
        ],
        check=True,
        cwd=ROOT,
        env=build_env,
        timeout=900,
    )
    bundle = ROOT / "dist" / "native" / NAME
    executable = bundle / (NAME + ".exe" if os.name == "nt" else NAME)
    if not executable.is_file():
        raise RuntimeError(f"Expected native executable is missing: {executable}")
    collect_notices(bundle)
    env = build_env.copy()
    env.pop("PYTHONPATH", None)
    env["QT_QPA_PLATFORM"] = "offscreen"
    with tempfile.TemporaryDirectory(prefix="ubt-wizard-native-") as directory:
        subprocess.run(
            [str(executable), "--smoke-test"], cwd=directory, env=env, check=True, timeout=90
        )
    output = ROOT / "release-assets"
    output.mkdir(exist_ok=True)
    label = f"{NAME}-{version}-{platform.system().lower()}-{platform.machine().lower()}"
    if os.name == "nt":
        archive = shutil.make_archive(str(output / label), "zip", bundle.parent, bundle.name)
    else:
        # tar preserves executable permission bits; ZIP extraction may not.
        archive = shutil.make_archive(str(output / label), "gztar", bundle.parent, bundle.name)
    print(f"Unsigned portable onedir archive: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
