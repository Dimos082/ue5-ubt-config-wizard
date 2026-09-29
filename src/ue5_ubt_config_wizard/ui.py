"""A small, local desktop editor for one UBT XML profile at a time.

The screen exposes the everyday path. Catalog browsing and build checks live in
separate dialogs; XML, backup and conflict rules stay in GUI-independent modules.
"""

from __future__ import annotations

import copy
import difflib
import html
import sys
from importlib.resources import files
from pathlib import Path

from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QAction, QCursor, QGuiApplication, QIcon, QKeySequence, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from .catalog import catalog_report, schema_path, validate_document
from .command_dialog import CommandDialog
from .discovery import candidate_profiles, engine_version
from .profile import ProfileDocument, ProfileError
from .theme import LIGHT_STYLE, apply_theme

STYLE = LIGHT_STYLE  # Kept for source compatibility; main() applies the selected theme.


def _button(label: str, action, style: str = "") -> QPushButton:
    button = QPushButton(label)
    if style:
        button.setObjectName(style)
    button.clicked.connect(action)
    return button


def _xml_text(data: bytes) -> str:
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        return data.decode("utf-16", errors="replace")
    return data.decode("utf-8-sig", errors="replace")


def _details(record) -> str:
    if record is None:
        return (
            "<h3>Select a setting</h3><p>Choose a row to see its meaning and source. "
            "Settings without verified metadata are preserved.</p>"
        )
    source = html.escape(record.source, quote=True)
    link = QApplication.instance().palette().color(QPalette.ColorRole.Link).name()
    return (
        f"<h3>{html.escape(record.name)}</h3>"
        f"<p>{html.escape(record.description)}</p>"
        f"<p><b>Category:</b> {html.escape(record.category)}<br>"
        f"<b>Value type:</b> {html.escape(record.kind)}<br>"
        f"<b>Evidence:</b> {html.escape(record.status)}<br>"
        f"<b>Documented version:</b> {html.escape(record.evidence_version)}</p>"
        f'<p><a href="{source}" style="color:{link}">Read the source ↗</a></p>'
    )


class ValueDialog(QDialog):
    """Ask for one known scalar value; absence never becomes false implicitly."""

    def __init__(self, record, current: str | None, parent=None):
        super().__init__(parent)
        self.record = record
        self.setWindowTitle("Edit setting" if current is not None else "Add setting")
        self.setMinimumWidth(450)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(12)
        title = QLabel(record.name)
        title.setObjectName("dialogTitle")
        layout.addWidget(title)
        note = QLabel(record.description)
        note.setWordWrap(True)
        layout.addWidget(note)
        layout.addWidget(QLabel("Value"))
        if record.kind in ("bool", "boolean"):
            self.editor = QComboBox()
            self.editor.addItems(["true", "false"])
            self.editor.setCurrentText(current if current is not None else "true")
        elif record.kind == "enum" and record.choices:
            self.editor = QComboBox()
            self.editor.addItems(list(record.choices))
            if current and self.editor.findText(current) < 0:
                self.editor.addItem(current)
            if current:
                self.editor.setCurrentText(current)
        else:
            self.editor = QLineEdit(current or "")
        layout.addWidget(self.editor)
        evidence_text = f"{record.kind} · {record.status}"
        if record.kind in ("unknown", "list"):
            evidence_text += (
                "\nValue format is unverified. This writes raw text; check the source and "
                "your engine before using it. A local schema can reject invalid XML."
            )
        evidence = QLabel(evidence_text)
        evidence.setObjectName("muted")
        evidence.setWordWrap(True)
        layout.addWidget(evidence)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._accept_value)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def value(self) -> str:
        return (
            self.editor.currentText() if isinstance(self.editor, QComboBox) else self.editor.text()
        )

    def _accept_value(self):
        try:
            if self.record.kind in ("int", "integer"):
                int(self.value())
            elif self.record.kind == "float":
                float(self.value())
        except ValueError:
            QMessageBox.warning(self, "Invalid value", f"Enter a valid {self.record.kind} value.")
            return
        self.accept()


class CatalogDialog(QDialog):
    """Keep the large, partly unverified catalog out of the main editor."""

    def __init__(self, records, parent=None):
        super().__init__(parent)
        self.records = records
        self.selected = None
        self.setWindowTitle("Add a setting")
        self.resize(760, 590)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(12)
        title = QLabel("Add a setting")
        title.setObjectName("dialogTitle")
        layout.addWidget(title)
        reviewed = sum(item.kind not in ("unknown", "list") for item in records)
        note = QLabel(
            f"All {len(records)} documented candidates are shown. "
            f"{len(records) - reviewed} have unverified value formats; review their source before saving."
        )
        note.setObjectName("muted")
        note.setWordWrap(True)
        layout.addWidget(note)
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search settings")
        self.search.textChanged.connect(self._filter)
        layout.addWidget(self.search)
        row = QHBoxLayout()
        self.list = QListWidget()
        self.list.currentItemChanged.connect(self._selected)
        self.list.itemDoubleClicked.connect(self._accept)
        row.addWidget(self.list, 1)
        self.details = QTextBrowser()
        self.details.setOpenExternalLinks(True)
        self.details.setHtml(_details(None))
        row.addWidget(self.details, 1)
        layout.addLayout(row, 1)
        buttons = QHBoxLayout()
        buttons.addStretch()
        buttons.addWidget(_button("Cancel", self.reject))
        self.add_button = _button("Add setting", self._accept, "primary")
        buttons.addWidget(self.add_button)
        layout.addLayout(buttons)
        self._filter()

    def _filter(self):
        query = self.search.text().casefold().strip()
        self.list.clear()
        for record in self.records:
            if (
                query
                and query not in f"{record.category} {record.name} {record.description}".casefold()
            ):
                continue
            item = QListWidgetItem(record.name)
            item.setData(Qt.ItemDataRole.UserRole, record)
            item.setToolTip(record.category)
            self.list.addItem(item)
        if self.list.count():
            self.list.setCurrentRow(0)
        else:
            self._selected(None)

    def _selected(self, item, _previous=None):
        record = item.data(Qt.ItemDataRole.UserRole) if item else None
        self.details.setHtml(_details(record))
        self.add_button.setEnabled(record is not None)

    def _accept(self, *_):
        item = self.list.currentItem()
        record = item.data(Qt.ItemDataRole.UserRole) if item else None
        if record:
            self.selected = record
            self.accept()


class MainWindow(QMainWindow):
    """One selected file, one visible list, one Save action."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("UE5 UBT Configuration Wizard")
        self._settings = QSettings("UE5 UBT Configuration Wizard", "UE5 UBT Configuration Wizard")
        self.dark_mode = self._settings.value("night_mode", False, type=bool)
        apply_theme(QApplication.instance(), self.dark_mode)
        self.engine: Path | None = None
        self.project: Path | None = None
        self.profile_path: Path | None = None
        self.document: ProfileDocument | None = None
        self._baseline = b""
        self._disk = b""
        self._new = False
        self._recent: list[Path] = []
        self._records = []
        self._catalog = {}
        self._build_ui()
        self._build_menu()
        self._reload_catalog()
        self.refresh_profiles()
        self._refresh()
        self._fit_screen()

    def _fit_screen(self):
        """Center on the monitor under the pointer and stay inside its work area."""
        screen = QGuiApplication.screenAt(QCursor.pos()) or QGuiApplication.primaryScreen()
        if screen is None:
            self.resize(900, 650)
            return
        area = screen.availableGeometry()
        width = min(1060, max(1, int(area.width() * 0.90)))
        height = min(740, max(1, int(area.height() * 0.85)))
        self.setMinimumSize(min(720, width), min(500, height))
        self.setGeometry(
            area.x() + (area.width() - width) // 2,
            area.y() + (area.height() - height) // 2,
            width,
            height,
        )

    def _build_ui(self):
        root = QWidget()
        outer = QVBoxLayout(root)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        top = QFrame()
        top.setObjectName("topbar")
        top_row = QHBoxLayout(top)
        top_row.setContentsMargins(24, 15, 24, 15)
        brand = QVBoxLayout()
        name = QLabel("UBT Configuration Wizard")
        name.setObjectName("brand")
        hint = QLabel("One XML profile at a time")
        hint.setObjectName("brandHint")
        brand.addWidget(name)
        brand.addWidget(hint)
        top_row.addLayout(brand)
        top_row.addStretch()
        top_row.addWidget(_button("Open XML…", self.browse_profile, "topButton"))
        top_row.addWidget(_button("New profile", self.new_profile, "topButton"))
        outer.addWidget(top)

        self.pages = QStackedWidget()
        outer.addWidget(self.pages, 1)
        welcome = QWidget()
        welcome_layout = QVBoxLayout(welcome)
        welcome_layout.setContentsMargins(90, 70, 90, 60)
        welcome_layout.setSpacing(14)
        welcome_layout.addStretch()
        hero = QLabel("Start with a BuildConfiguration.xml")
        hero.setObjectName("hero")
        hero.setWordWrap(True)
        welcome_layout.addWidget(hero)
        subtitle = QLabel(
            "Open an existing profile, or create a new one. Your file is never changed until you review and save."
        )
        subtitle.setObjectName("muted")
        subtitle.setWordWrap(True)
        welcome_layout.addWidget(subtitle)
        row = QHBoxLayout()
        row.addWidget(_button("Open XML file…", self.browse_profile, "primary"))
        row.addWidget(_button("Create new profile", self.new_profile))
        row.addStretch()
        welcome_layout.addLayout(row)
        recent = QLabel("Suggested locations")
        recent.setObjectName("section")
        welcome_layout.addWidget(recent)
        self.candidates = QListWidget()
        self.candidates.setMaximumHeight(180)
        self.candidates.itemDoubleClicked.connect(self.open_selected)
        welcome_layout.addWidget(self.candidates)
        self.candidate_hint = QLabel()
        self.candidate_hint.setObjectName("muted")
        self.candidate_hint.setWordWrap(True)
        welcome_layout.addWidget(self.candidate_hint)
        welcome_layout.addStretch()
        self.pages.addWidget(welcome)

        editor = QWidget()
        edit_layout = QVBoxLayout(editor)
        edit_layout.setContentsMargins(24, 22, 24, 0)
        edit_layout.setSpacing(16)
        file_card = QFrame()
        file_card.setObjectName("surface")
        file_row = QHBoxLayout(file_card)
        file_row.setContentsMargins(18, 14, 18, 14)
        file_labels = QVBoxLayout()
        self.profile_label = QLabel()
        self.profile_label.setObjectName("section")
        self.path_label = QLabel()
        self.path_label.setObjectName("path")
        self.path_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.path_label.setWordWrap(True)
        self.context_label = QLabel()
        self.context_label.setObjectName("muted")
        file_labels.addWidget(self.profile_label)
        file_labels.addWidget(self.path_label)
        file_labels.addWidget(self.context_label)
        file_row.addLayout(file_labels, 1)
        self.build_button = _button("Build check…", self.open_command)
        file_row.addWidget(self.build_button)
        edit_layout.addWidget(file_card)

        heading_row = QHBoxLayout()
        heading = QLabel("Settings in this file")
        heading.setObjectName("section")
        heading_row.addWidget(heading)
        heading_row.addStretch()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Find in this file")
        self.search.setMaximumWidth(260)
        self.search.textChanged.connect(self._refresh_table)
        heading_row.addWidget(self.search)
        heading_row.addWidget(_button("+ Add setting", self.add_setting, "primary"))
        edit_layout.addLayout(heading_row)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Setting", "Value", "Category"])
        self.table.verticalHeader().hide()
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.itemSelectionChanged.connect(self._selected_entry)
        self.table.itemDoubleClicked.connect(self.edit_setting)
        splitter.addWidget(self.table)
        side = QFrame()
        side.setObjectName("surface")
        side_layout = QVBoxLayout(side)
        side_layout.setContentsMargins(16, 14, 16, 14)
        self.details = QTextBrowser()
        self.details.setOpenExternalLinks(True)
        self.details.setFrameShape(QFrame.Shape.NoFrame)
        side_layout.addWidget(self.details, 1)
        row = QHBoxLayout()
        self.edit_button = _button("Edit value", self.edit_setting)
        self.remove_button = _button("Remove", self.remove_setting)
        row.addWidget(self.edit_button)
        row.addWidget(self.remove_button)
        side_layout.addLayout(row)
        splitter.addWidget(side)
        splitter.setSizes([650, 340])
        edit_layout.addWidget(splitter, 1)

        savebar = QFrame()
        savebar.setObjectName("savebar")
        save_row = QHBoxLayout(savebar)
        save_row.setContentsMargins(0, 14, 0, 14)
        self.state_label = QLabel()
        self.state_label.setObjectName("muted")
        save_row.addWidget(self.state_label, 1)
        self.review_button = _button("Review changes", self.preview_changes)
        self.discard_button = _button("Discard edits", self.revert_edits)
        self.apply_button = _button("Save changes", self.apply_changes, "primary")
        save_row.addWidget(self.review_button)
        save_row.addWidget(self.discard_button)
        save_row.addWidget(self.apply_button)
        edit_layout.addWidget(savebar)
        self.pages.addWidget(editor)
        self.setCentralWidget(root)

    def _build_menu(self):
        file_menu = self.menuBar().addMenu("File")
        for label, shortcut, action in (
            ("Open XML…", QKeySequence.StandardKey.Open, self.browse_profile),
            ("New profile", QKeySequence.StandardKey.New, self.new_profile),
            ("Save changes", QKeySequence.StandardKey.Save, self.apply_changes),
            ("Save a copy…", QKeySequence.StandardKey.SaveAs, self.save_as),
        ):
            item = QAction(label, self)
            item.setShortcut(shortcut)
            item.triggered.connect(action)
            file_menu.addAction(item)
            if label == "Save changes":
                self._save_action = item
            elif label == "Save a copy…":
                self._copy_action = item
        file_menu.addSeparator()
        self._backup_action = file_menu.addAction("Back up original…", self.backup_profile)
        self._restore_action = file_menu.addAction("Restore backup…", self.restore_backup)
        view = self.menuBar().addMenu("View")
        self._theme_action = view.addAction("Night mode")
        self._theme_action.setCheckable(True)
        self._theme_action.setChecked(self.dark_mode)
        self._theme_action.toggled.connect(self._change_theme)
        tools = self.menuBar().addMenu("Tools")
        tools.addAction("Select UE5 engine…", self.browse_engine)
        tools.addAction("Select Unreal project…", self.browse_project)
        tools.addAction("Refresh suggested locations", self.refresh_profiles)
        tools.addSeparator()
        tools.addAction("Run build check…", self.open_command)

    def _change_theme(self, dark: bool):
        self.dark_mode = dark
        self._settings.setValue("night_mode", dark)
        apply_theme(QApplication.instance(), dark)
        if self.document:
            self._selected_entry()

    def _dirty(self) -> bool:
        return self.document is not None and (self._new or self.document.render() != self._baseline)

    def _can_switch(self) -> bool:
        if not self._dirty():
            return True
        answer = QMessageBox.question(
            self,
            "Unsaved changes",
            "Discard your unsaved changes?",
            QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel,
        )
        return answer == QMessageBox.StandardButton.Discard

    def _error(self, title: str, error):
        QMessageBox.warning(self, title, str(error))

    def refresh_profiles(self):
        self.candidates.clear()
        try:
            paths = dict.fromkeys([*self._recent, *candidate_profiles(self.engine, self.project)])
            existing = [path for path in paths if path.is_file()]
        except (OSError, ValueError) as error:
            self._error("Could not find profiles", error)
            existing = []
        for path in existing:
            item = QListWidgetItem(str(path))
            item.setData(Qt.ItemDataRole.UserRole, path)
            self.candidates.addItem(item)
        self.candidate_hint.setText(
            "Double-click a suggested profile, or browse to another XML file."
            if existing
            else "No profile was found in the usual locations. Choose Open XML file or create a new profile."
        )

    def open_selected(self, item):
        if item and self._can_switch():
            self.load_profile(item.data(Qt.ItemDataRole.UserRole))

    def browse_profile(self):
        if not self._can_switch():
            return
        chosen, _ = QFileDialog.getOpenFileName(
            self,
            "Open BuildConfiguration.xml",
            str(self.profile_path.parent if self.profile_path else Path.home()),
            "XML files (*.xml);;All files (*)",
        )
        if chosen:
            self.load_profile(Path(chosen))

    def load_profile(self, path: Path) -> bool:
        try:
            document = ProfileDocument.open(path)
            disk = Path(path).read_bytes()
        except (ProfileError, OSError, ValueError) as error:
            self._error("Could not open XML", error)
            return False
        self.document = document
        self.profile_path = Path(path).resolve()
        self._disk = disk
        self._baseline = document.render()
        self._new = False
        self._recent = [self.profile_path, *[p for p in self._recent if p != self.profile_path]][
            :10
        ]
        self._refresh()
        self.refresh_profiles()
        self.statusBar().showMessage("Profile opened. Changes stay staged until you save.")
        return True

    def new_profile(self):
        if not self._can_switch():
            return
        self.document = ProfileDocument.new()
        self.profile_path = None
        self._disk = b""
        self._baseline = self.document.render()
        self._new = True
        self._refresh()

    def browse_engine(self):
        if not self._can_switch():
            return
        chosen = QFileDialog.getExistingDirectory(self, "Select UE5 installation", str(Path.home()))
        if chosen:
            self.engine = Path(chosen)
            self._reload_catalog()
            self.refresh_profiles()
            self._refresh()
            version = engine_version(self.engine)
            self.statusBar().showMessage(
                f"Engine {version or 'version unknown'} selected. Exact XML support remains unverified."
            )

    def browse_project(self):
        if not self._can_switch():
            return
        chosen, _ = QFileDialog.getOpenFileName(
            self, "Select .uproject", str(Path.home()), "Unreal projects (*.uproject)"
        )
        if chosen:
            self.project = Path(chosen)
            self.refresh_profiles()

    def _reload_catalog(self):
        report = catalog_report(self.engine)
        self._records = list(report["settings"])
        self._catalog = {(item.category, item.name): item for item in self._records}

    def _refresh(self):
        self.pages.setCurrentIndex(1 if self.document else 0)
        self._save_action.setEnabled(self._dirty())
        self._copy_action.setEnabled(self.document is not None)
        self._backup_action.setEnabled(self.profile_path is not None)
        self._restore_action.setEnabled(self.profile_path is not None)
        if not self.document:
            return
        self.profile_label.setText(self.profile_path.name if self.profile_path else "New profile")
        self.path_label.setText(
            str(self.profile_path)
            if self.profile_path
            else "Choose where to save this XML profile."
        )
        self.context_label.setText(
            f"UE {engine_version(self.engine) or 'version unknown'} selected · XML support unverified"
            if self.engine
            else ""
        )
        self.context_label.setVisible(self.engine is not None)
        self.state_label.setText(
            "Unsaved changes · A backup is made before replacing an existing file."
            if self._dirty()
            else f"{len(self.document.entries())} setting(s) in this file · No unsaved changes"
        )
        self.apply_button.setEnabled(self._dirty())
        self.discard_button.setEnabled(self._dirty())
        self.review_button.setEnabled(self._dirty())
        self._refresh_table()

    def _refresh_table(self):
        self.table.setRowCount(0)
        if self.document:
            query = self.search.text().casefold().strip()
            for entry in self.document.entries():
                if query and query not in f"{entry.category} {entry.name} {entry.value}".casefold():
                    continue
                row = self.table.rowCount()
                self.table.insertRow(row)
                for column, text in enumerate((entry.name, entry.value, entry.category)):
                    self.table.setItem(row, column, QTableWidgetItem(text))
        if self.table.rowCount():
            self.table.selectRow(0)
        else:
            self.details.setHtml(_details(None))
            self.edit_button.setEnabled(False)
            self.remove_button.setEnabled(False)

    def _selected_key(self) -> tuple[str, str] | None:
        row = self.table.currentRow()
        if row < 0 or self.table.item(row, 0) is None:
            return None
        return self.table.item(row, 2).text(), self.table.item(row, 0).text()

    def _selected_entry(self):
        key = self._selected_key()
        record = self._catalog.get(key) if key else None
        self.details.setHtml(
            _details(record)
            if record
            else "<h3>Unreviewed setting</h3><p>This XML value is preserved. Its meaning and type are not verified.</p>"
        )
        self.edit_button.setEnabled(record is not None)
        self.remove_button.setEnabled(key is not None)

    def add_setting(self):
        if not self.document:
            return
        dialog = CatalogDialog(self._records, self)
        if dialog.exec() == QDialog.DialogCode.Accepted and dialog.selected:
            record = dialog.selected
            current = next(
                (
                    item.value
                    for item in self.document.entries()
                    if (item.category, item.name) == (record.category, record.name)
                ),
                None,
            )
            self._edit_record(record, current)

    def edit_setting(self, *_):
        key = self._selected_key()
        if not key or not self.document:
            return
        record = self._catalog.get(key)
        if record:
            row = self.table.currentRow()
            self._edit_record(record, self.table.item(row, 1).text())

    def _edit_record(self, record, current):
        dialog = ValueDialog(record, current, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                self.document.set(record.category, record.name, dialog.value())
                self._refresh()
            except (ProfileError, ValueError) as error:
                self._error("Could not change setting", error)

    def remove_setting(self):
        key = self._selected_key()
        if key and self.document:
            try:
                self.document.remove(*key)
                self._refresh()
                self.statusBar().showMessage(
                    "Setting removed from staged XML; a default may then apply."
                )
            except ProfileError as error:
                self._error("Could not remove setting", error)

    def revert_edits(self):
        if not self._can_switch():
            return
        if self.profile_path:
            self.load_profile(self.profile_path)
        elif self.document:
            self.document = None
            self._new = False
            self._baseline = b""
            self._disk = b""
            self._refresh()

    def _diff(self, rendered: bytes | None = None) -> str:
        if not self.document:
            return ""
        before = _xml_text(self._disk).splitlines(keepends=True)
        after = _xml_text(rendered or self.document.render()).splitlines(keepends=True)
        return "".join(difflib.unified_diff(before, after, fromfile="On disk", tofile="To save"))

    def preview_changes(self):
        if not self.document:
            return
        dialog = QDialog(self)
        dialog.setWindowTitle("Review changes")
        dialog.resize(800, 520)
        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("These are the serialized XML changes that will be saved."))
        preview = QPlainTextEdit(self._diff() or "No serialized changes.")
        preview.setReadOnly(True)
        layout.addWidget(preview)
        layout.addWidget(_button("Close", dialog.accept))
        dialog.exec()

    def _confirm_write(self, target: Path, rendered: bytes, title="Save changes") -> bool:
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.resize(820, 550)
        layout = QVBoxLayout(dialog)
        heading = QLabel(title)
        heading.setObjectName("dialogTitle")
        layout.addWidget(heading)
        path = QLabel(f"Destination: {target}")
        path.setWordWrap(True)
        layout.addWidget(path)
        note = QLabel(
            "The existing file will be backed up before replacement. Review the complete serialized diff."
            if target.exists()
            else "A new XML file will be created at this path."
        )
        note.setObjectName("muted")
        note.setWordWrap(True)
        layout.addWidget(note)
        preview = QPlainTextEdit(self._diff(rendered) or "No serialized changes.")
        preview.setReadOnly(True)
        layout.addWidget(preview, 1)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        return dialog.exec() == QDialog.DialogCode.Accepted

    def apply_changes(self) -> bool:
        if not self.document:
            return False
        if not self._dirty():
            self.statusBar().showMessage("Nothing changed; the file was not written.")
            return True
        target = self.profile_path
        if target is None:
            chosen, _ = QFileDialog.getSaveFileName(
                self,
                "Save new profile",
                str(Path.home() / "BuildConfiguration.xml"),
                "XML files (*.xml)",
            )
            if not chosen:
                return False
            target = Path(chosen)
        if schema_path(self.engine):
            errors = validate_document(self.document.render(), self.engine)
            if errors:
                self._error("Schema validation failed", "\n".join(errors[:10]))
                return False
        overwrite = self.profile_path is None and target.exists()
        if not self._confirm_write(target, self.document.render()):
            return False
        try:
            backup = self.document.save(target, allow_overwrite=overwrite)
            self.profile_path = target.resolve()
            self._disk = target.read_bytes()
            self._baseline = self.document.render()
            self._new = False
            self._refresh()
            self.statusBar().showMessage(
                f"Saved {target}" + (f" · Backup: {backup}" if backup else "")
            )
            return True
        except (ProfileError, OSError, ValueError) as error:
            self._error("Changes were not saved", error)
            return False

    def save_as(self):
        if not self.document:
            return
        suggestion = (
            self.profile_path.with_name("BuildConfiguration-copy.xml")
            if self.profile_path
            else Path.home() / "BuildConfiguration.xml"
        )
        chosen, _ = QFileDialog.getSaveFileName(
            self, "Save a copy", str(suggestion), "XML files (*.xml)"
        )
        if not chosen:
            return
        target = Path(chosen)
        if self.profile_path and target.resolve() == self.profile_path:
            self.apply_changes()
            return
        if not self._confirm_write(target, self.document.render(), "Save a copy"):
            return
        try:
            copy.deepcopy(self.document).save(target, allow_overwrite=target.exists())
            self.statusBar().showMessage(
                f"Copy saved to {target}. Editing remains on the original."
            )
        except (ProfileError, OSError, ValueError) as error:
            self._error("Could not save copy", error)

    def backup_profile(self):
        if self.document and self.profile_path:
            try:
                backup = self.document.backup()
                QMessageBox.information(
                    self, "Backup created", f"On-disk profile copied to:\n{backup}"
                )
            except (ProfileError, OSError) as error:
                self._error("Backup failed", error)

    def restore_backup(self):
        if not self.document or not self.profile_path or not self._can_switch():
            return
        chosen, _ = QFileDialog.getOpenFileName(
            self, "Choose a backup", str(self.profile_path.parent), "Backups (*.bak);;All files (*)"
        )
        if not chosen:
            return
        try:
            restored = ProfileDocument.open(chosen)
            if not self._confirm_write(self.profile_path, restored.render(), "Restore backup"):
                return
            backup = restored.save(self.profile_path, allow_overwrite=True)
            self.load_profile(self.profile_path)
            self.statusBar().showMessage(f"Restored backup. Prior file saved at {backup}.")
        except (ProfileError, OSError, ValueError) as error:
            self._error("Could not restore backup", error)

    def open_command(self):
        if self._dirty():
            answer = QMessageBox.question(
                self,
                "Unsaved changes",
                "Run against the current on-disk file? Unsaved edits will not be used.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Cancel,
            )
            if answer != QMessageBox.StandardButton.Yes:
                return
        CommandDialog(self.engine, self.project, self.profile_path, self).exec()

    def closeEvent(self, event):
        event.accept() if self._can_switch() else event.ignore()


def main() -> int:
    application = QApplication.instance() or QApplication(sys.argv)
    application.setApplicationName("UE5 UBT Configuration Wizard")
    application.setWindowIcon(QIcon(str(files("ue5_ubt_config_wizard") / "assets/app_icon.png")))
    application.setStyle("Fusion")
    application.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    return application.exec()
