"""Small UI workflow checks with synthetic files and a harmless local command."""

import os
from pathlib import Path

import pytest
from PySide6.QtCore import QProcess, Qt
from PySide6.QtGui import QCursor, QGuiApplication, QPalette
from PySide6.QtWidgets import QMessageBox

from ue5_ubt_config_wizard.command_dialog import CommandDialog
from ue5_ubt_config_wizard.profile import NAMESPACE, ProfileDocument
from ue5_ubt_config_wizard.theme import apply_theme
from ue5_ubt_config_wizard.ui import CatalogDialog, MainWindow, ValueDialog


def test_ui_stages_then_applies_with_backup(qtbot, tmp_path: Path, monkeypatch) -> None:
    source = tmp_path / "BuildConfiguration.xml"
    original = (
        f'<Configuration xmlns="{NAMESPACE}"><BuildConfiguration>'
        "<bUseUnityBuild>true</bUseUnityBuild>"
        "</BuildConfiguration></Configuration>"
    ).encode()
    source.write_bytes(original)
    window = MainWindow()
    qtbot.addWidget(window)
    assert window.load_profile(source)
    assert window.table.rowCount() == 1
    assert not window._dirty()

    record = window._catalog[("BuildConfiguration", "bUseUnityBuild")]
    monkeypatch.setattr(ValueDialog, "exec", lambda _self: ValueDialog.DialogCode.Accepted)
    monkeypatch.setattr(ValueDialog, "value", lambda _self: "false")
    window._edit_record(record, "true")
    assert window._dirty()
    assert source.read_bytes() == original
    monkeypatch.setattr(window, "_confirm_write", lambda *_args, **_kwargs: True)
    assert window.apply_changes()
    assert ProfileDocument.open(source).entries()[0].value == "false"
    assert any(path.read_bytes() == original for path in tmp_path.glob("*.bak"))
    window.close()


def test_ui_new_profile(qtbot, tmp_path: Path, monkeypatch) -> None:
    window = MainWindow()
    qtbot.addWidget(window)
    window.new_profile()
    assert window.document is not None
    assert window._dirty()
    target = tmp_path / "BuildConfiguration.xml"
    monkeypatch.setattr(
        "ue5_ubt_config_wizard.ui.QFileDialog.getSaveFileName",
        lambda *_args, **_kwargs: (str(target), ""),
    )
    monkeypatch.setattr(window, "_confirm_write", lambda *_args, **_kwargs: True)
    assert window.apply_changes()
    assert target.is_file()
    assert not window._dirty()
    window.close()


def test_catalog_shows_and_allows_all_documented_settings(qtbot) -> None:
    window = MainWindow()
    qtbot.addWidget(window)
    assert window.pages.currentIndex() == 0
    window.new_profile()
    assert window.pages.currentIndex() == 1
    dialog = CatalogDialog(window._records, window)
    qtbot.addWidget(dialog)
    assert dialog.list.count() == len(window._records)
    unreviewed = next(item for item in window._records if item.kind == "unknown")
    matches = dialog.list.findItems(unreviewed.name, Qt.MatchFlag.MatchExactly)
    selected = next(
        item for item in matches if item.data(Qt.ItemDataRole.UserRole).kind == "unknown"
    )
    dialog.list.setCurrentItem(selected)
    assert dialog.add_button.isEnabled()
    dialog._accept()
    assert dialog.selected == unreviewed
    dialog.close()
    # Close without displaying the unsaved-change prompt.
    window.document = None
    window._new = False
    window.close()


def test_unreviewed_setting_can_be_staged_as_raw_text(qtbot, monkeypatch) -> None:
    window = MainWindow()
    qtbot.addWidget(window)
    window.new_profile()
    record = next(item for item in window._records if item.kind == "unknown")
    monkeypatch.setattr(ValueDialog, "exec", lambda _self: ValueDialog.DialogCode.Accepted)
    monkeypatch.setattr(ValueDialog, "value", lambda _self: "raw-value")
    window._edit_record(record, None)
    assert any(
        (entry.category, entry.name, entry.value) == (record.category, record.name, "raw-value")
        for entry in window.document.entries()
    )
    window.document = None
    window._new = False
    window.close()


def test_discard_new_profile_returns_to_welcome(qtbot, monkeypatch) -> None:
    window = MainWindow()
    qtbot.addWidget(window)
    window.new_profile()
    monkeypatch.setattr(
        QMessageBox, "question", lambda *_args, **_kwargs: QMessageBox.StandardButton.Discard
    )
    window.revert_edits()
    assert window.document is None
    assert window.pages.currentIndex() == 0
    window.close()


def test_initial_window_fits_active_screen(qtbot) -> None:
    window = MainWindow()
    qtbot.addWidget(window)
    screen = QGuiApplication.screenAt(QCursor.pos()) or QGuiApplication.primaryScreen()
    assert screen.availableGeometry().contains(window.geometry())
    window.close()


def test_command_field_is_editable_without_a_preset(qtbot) -> None:
    dialog = CommandDialog(None, None, None)
    qtbot.addWidget(dialog)
    assert not dialog.command.isReadOnly()
    assert not dialog.run_button.isEnabled()
    dialog.command.setText("echo ready")
    assert dialog.run_button.isEnabled()
    dialog.close()


@pytest.mark.skipif(
    os.environ.get("CODEX_SANDBOX_TEST") == "1",
    reason="The local sandbox blocks Qt's Windows process pipes; CI runs this test normally.",
)
def test_ui_explicit_command(qtbot, tmp_path: Path) -> None:
    dialog = CommandDialog(None, None, None)
    qtbot.addWidget(dialog)
    assert dialog.process.state() == QProcess.ProcessState.NotRunning
    assert not dialog.command.isReadOnly()
    dialog.command.setText("echo wizard-smoke")
    dialog.directory.setText(str(tmp_path))
    dialog.run()
    qtbot.waitUntil(
        lambda: dialog.process.state() == QProcess.ProcessState.NotRunning, timeout=10_000
    )
    assert "wizard-smoke" in dialog.log.toPlainText()
    assert "exit code 0" in dialog.log.toPlainText()
    dialog.close()


def test_light_and_night_palettes_keep_selection_legible(qapp) -> None:
    try:
        for dark in (False, True):
            apply_theme(qapp, dark)
            palette = qapp.palette()
            assert palette.color(QPalette.ColorRole.HighlightedText).name() == "#ffffff"
            assert (
                palette.color(QPalette.ColorRole.Highlight).name()
                != palette.color(QPalette.ColorRole.Base).name()
            )
            assert "QMenuBar::item:selected" in qapp.styleSheet()
            assert "QTableWidget::item:selected" in qapp.styleSheet()
    finally:
        apply_theme(qapp, False)
