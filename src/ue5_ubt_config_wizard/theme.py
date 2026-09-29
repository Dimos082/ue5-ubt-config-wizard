"""Explicit light and night palettes keep Qt readable under either OS theme."""

from __future__ import annotations

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

LIGHT_STYLE = """
QWidget { font-family: 'Segoe UI', 'Helvetica Neue', sans-serif; font-size: 13px; color: #233044; }
QMainWindow, QDialog { background: #f6f7f9; }
QFrame#topbar { background: #172436; }
QLabel#brand { color: #ffffff; font-size: 18px; font-weight: 700; }
QLabel#brandHint { color: #c6d3e3; font-size: 12px; }
QLabel#hero { font-size: 28px; font-weight: 700; color: #172436; }
QLabel#section { font-size: 16px; font-weight: 700; color: #172436; }
QLabel#dialogTitle { font-size: 20px; font-weight: 700; color: #172436; }
QLabel#muted { color: #586b82; }
QLabel#path { color: #465c76; font-size: 12px; }
QFrame#surface { background: #ffffff; border: 1px solid #d8e0e8; border-radius: 12px; }
QFrame#savebar { background: #ffffff; border-top: 1px solid #d8e0e8; }
QPushButton { padding: 8px 14px; color: #172436; background: #ffffff;
              border: 1px solid #b8c5d4; border-radius: 7px; font-weight: 600; }
QPushButton:hover { border-color: #536f91; background: #eaf0f8; }
QPushButton:disabled { color: #77889e; background: #edf1f5; border-color: #d8e0e8; }
QPushButton#primary { background: #225bc5; color: #ffffff; border-color: #225bc5; }
QPushButton#primary:hover { background: #174aa9; }
QPushButton#primary:disabled { background: #a9bfe8; border-color: #a9bfe8; }
QPushButton#topButton { background: #263b56; color: #ffffff; border-color: #506781; }
QPushButton#topButton:hover { background: #355273; }
QLineEdit, QComboBox { color: #172436; padding: 8px; background: #ffffff;
                      border: 1px solid #b8c5d4; border-radius: 7px; }
QLineEdit:focus, QComboBox:focus { border-color: #225bc5; }
QTableWidget, QListWidget, QTextBrowser, QPlainTextEdit { color: #172436;
    background: #ffffff; alternate-background-color: #f7f9fc;
    border: 1px solid #d8e0e8; border-radius: 8px; }
QTableWidget::item, QListWidget::item { padding: 7px; }
QTableWidget::item:selected, QListWidget::item:selected { background: #225bc5; color: #ffffff; }
QHeaderView::section { background: #edf1f6; border: none; border-bottom: 1px solid #d8e0e8;
                       padding: 10px; color: #394f69; font-weight: 600; }
QMenuBar { background: #edf1f6; color: #172436; }
QMenuBar::item:selected { background: #d8e5fb; color: #172436; }
QMenu { background: #ffffff; color: #172436; border: 1px solid #b8c5d4; }
QMenu::item:selected { background: #225bc5; color: #ffffff; }
QMenu::item:disabled { color: #77889e; }
QStatusBar { background: #edf1f6; color: #394f69; }
"""

DARK_STYLE = """
QWidget { font-family: 'Segoe UI', 'Helvetica Neue', sans-serif; font-size: 13px; color: #e8eef8; }
QMainWindow, QDialog { background: #141c28; }
QFrame#topbar { background: #0d1520; }
QLabel#brand { color: #ffffff; font-size: 18px; font-weight: 700; }
QLabel#brandHint { color: #acbed2; font-size: 12px; }
QLabel#hero { font-size: 28px; font-weight: 700; color: #f1f5fb; }
QLabel#section { font-size: 16px; font-weight: 700; color: #f1f5fb; }
QLabel#dialogTitle { font-size: 20px; font-weight: 700; color: #f1f5fb; }
QLabel#muted { color: #b2c2d6; }
QLabel#path { color: #b2c2d6; font-size: 12px; }
QFrame#surface { background: #202c3c; border: 1px solid #3a4a5e; border-radius: 12px; }
QFrame#savebar { background: #202c3c; border-top: 1px solid #3a4a5e; }
QPushButton { padding: 8px 14px; color: #f1f5fb; background: #26364a;
              border: 1px solid #60748f; border-radius: 7px; font-weight: 600; }
QPushButton:hover { border-color: #99b9e8; background: #344862; }
QPushButton:disabled { color: #a0afc1; background: #273443; border-color: #425266; }
QPushButton#primary { background: #356bd7; color: #ffffff; border-color: #6897ef; }
QPushButton#primary:hover { background: #477ce7; }
QPushButton#primary:disabled { background: #405b87; border-color: #536d98; }
QPushButton#topButton { background: #263b56; color: #ffffff; border-color: #60748f; }
QPushButton#topButton:hover { background: #355273; }
QLineEdit, QComboBox { color: #f1f5fb; padding: 8px; background: #202c3c;
                      border: 1px solid #60748f; border-radius: 7px; }
QLineEdit:focus, QComboBox:focus { border-color: #8db5ff; }
QTableWidget, QListWidget, QTextBrowser, QPlainTextEdit { color: #f1f5fb;
    background: #202c3c; alternate-background-color: #263449;
    border: 1px solid #3a4a5e; border-radius: 8px; }
QTableWidget::item, QListWidget::item { padding: 7px; }
QTableWidget::item:selected, QListWidget::item:selected { background: #527de0; color: #ffffff; }
QHeaderView::section { background: #2a384b; border: none; border-bottom: 1px solid #3a4a5e;
                       padding: 10px; color: #d7e4f5; font-weight: 600; }
QMenuBar { background: #1b2737; color: #f1f5fb; }
QMenuBar::item:selected { background: #36506f; color: #ffffff; }
QMenu { background: #202c3c; color: #f1f5fb; border: 1px solid #60748f; }
QMenu::item:selected { background: #527de0; color: #ffffff; }
QMenu::item:disabled { color: #a0afc1; }
QStatusBar { background: #1b2737; color: #d7e4f5; }
"""


def apply_theme(application: QApplication, dark: bool) -> None:
    """Set both palette and stylesheet so native menu/selection colors agree."""
    colors = (
        {
            "window": "#141c28",
            "base": "#202c3c",
            "text": "#f1f5fb",
            "alternate": "#263449",
            "button": "#26364a",
            "highlight": "#527de0",
            "link": "#8fc8ff",
            "placeholder": "#b2c2d6",
        }
        if dark
        else {
            "window": "#f6f7f9",
            "base": "#ffffff",
            "text": "#172436",
            "alternate": "#f7f9fc",
            "button": "#ffffff",
            "highlight": "#225bc5",
            "link": "#1658bd",
            "placeholder": "#586b82",
        }
    )
    palette = QPalette()
    for role, key in (
        (QPalette.ColorRole.Window, "window"),
        (QPalette.ColorRole.Base, "base"),
        (QPalette.ColorRole.AlternateBase, "alternate"),
        (QPalette.ColorRole.Button, "button"),
        (QPalette.ColorRole.Text, "text"),
        (QPalette.ColorRole.WindowText, "text"),
        (QPalette.ColorRole.ButtonText, "text"),
        (QPalette.ColorRole.HighlightedText, "text"),
        (QPalette.ColorRole.Link, "link"),
        (QPalette.ColorRole.PlaceholderText, "placeholder"),
    ):
        palette.setColor(role, QColor(colors[key]))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(colors["highlight"]))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    application.setPalette(palette)
    application.setStyleSheet(DARK_STYLE if dark else LIGHT_STYLE)
