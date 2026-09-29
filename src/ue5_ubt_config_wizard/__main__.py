"""Launch the desktop editor or run a harmless packaged-app smoke check."""

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Edit UnrealBuildTool BuildConfiguration.xml locally"
    )
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="construct and close the GUI without opening files",
    )
    args = parser.parse_args()
    from .ui import main as run_gui

    if args.smoke_test:
        from importlib.resources import files

        from PySide6.QtGui import QIcon
        from PySide6.QtWidgets import QApplication

        from .catalog import settings
        from .ui import STYLE, MainWindow

        application = QApplication.instance() or QApplication([])
        application.setWindowIcon(
            QIcon(str(files("ue5_ubt_config_wizard") / "assets/app_icon.png"))
        )
        application.setStyle("Fusion")
        application.setStyleSheet(STYLE)
        window = MainWindow()
        assert settings(), "bundled catalog is empty"
        window.close()
        print("GUI and bundled catalog smoke test passed.")
        return 0
    return run_gui()


if __name__ == "__main__":
    raise SystemExit(main())
