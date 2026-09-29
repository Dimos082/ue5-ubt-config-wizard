"""Install a built wheel in a clean venv and check startup outside the checkout."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
import venv
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=Path("dist"))
    args = parser.parse_args()
    wheels = list(args.dist.resolve().glob("ue5_ubt_config_wizard-*.whl"))
    if len(wheels) != 1:
        parser.error(f"Expected exactly one application wheel, found {len(wheels)}")
    root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="ubt-wizard-install-") as directory:
        work = Path(directory)
        environment = work / "venv"
        # pip --python can bootstrap an otherwise clean venv. This also avoids
        # relying on activation scripts or the caller's site-packages.
        venv.EnvBuilder(with_pip=False).create(environment)
        python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "--python",
                str(environment),
                "install",
                "-c",
                str(root / "requirements-dev.lock"),
                str(wheels[0]),
            ],
            check=True,
            cwd=work,
            timeout=600,
        )
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        env["QT_QPA_PLATFORM"] = "offscreen"
        # Import must resolve from this fresh environment; no source path injection.
        check = (
            "import ue5_ubt_config_wizard as p; "
            "assert 'site-packages' in str(p.__file__), p.__file__; "
            "from ue5_ubt_config_wizard.catalog_data import DOCUMENTED_SETTINGS; "
            "assert len(DOCUMENTED_SETTINGS) > 0, "
            "'catalog missing'; print(p.__version__)"
        )
        subprocess.run([str(python), "-c", check], check=True, cwd=work, env=env, timeout=60)
        subprocess.run(
            [str(python), "-m", "ue5_ubt_config_wizard", "--smoke-test"],
            check=True,
            cwd=work,
            env=env,
            timeout=60,
        )
    print("Clean wheel import, bundled catalog, and offscreen startup passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
