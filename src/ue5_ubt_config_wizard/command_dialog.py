"""Optional local build check, kept outside the everyday editing screen."""

from __future__ import annotations

import locale
import os
import shlex
import subprocess
from pathlib import Path
from threading import Thread

from PySide6.QtCore import QProcess, QTimer
from PySide6.QtWidgets import (
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
)

from .runner import default_command, terminate_process_tree


class CommandDialog(QDialog):
    """Runs a command only after the user clicks Run; owns only that process."""

    def __init__(
        self, engine: Path | None, project: Path | None, profile: Path | None, parent=None
    ):
        super().__init__(parent)
        self.setWindowTitle("Build check")
        self.resize(780, 540)
        self.setMinimumSize(620, 400)
        self.profile = profile
        self.preset = default_command(engine, project)
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self._read_output)
        self.process.readyReadStandardError.connect(self._read_output)
        self.process.finished.connect(self._finished)
        self.process.errorOccurred.connect(self._error)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(14)
        heading = QLabel("Run a local build check")
        heading.setObjectName("dialogTitle")
        layout.addWidget(heading)
        note = QLabel(
            "This runs on your computer. A successful command does not prove which XML profile or settings UnrealBuildTool used."
        )
        note.setObjectName("muted")
        note.setWordWrap(True)
        layout.addWidget(note)

        form = QFormLayout()
        self.command = QLineEdit()
        self.command.setPlaceholderText("Enter a command to run")
        self.command.textChanged.connect(self._update_run_button)
        form.addRow("Command", self.command)
        self.directory = QLineEdit(str(engine or Path.cwd()))
        form.addRow("Working folder", self.directory)
        layout.addLayout(form)

        row = QHBoxLayout()
        self.run_button = QPushButton("Run command")
        self.run_button.setObjectName("primary")
        self.run_button.clicked.connect(self.run)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setEnabled(False)
        row.addWidget(self.run_button)
        row.addWidget(self.stop_button)
        row.addStretch()
        layout.addLayout(row)
        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("Command output will appear here.")
        layout.addWidget(self.log, 1)
        self.suggested_command = ""
        if self.preset:
            program, arguments, directory = self.preset
            self.suggested_command = (
                subprocess.list2cmdline([program, *arguments])
                if os.name == "nt"
                else shlex.join([program, *arguments])
            )
            self.command.setText(self.suggested_command)
            self.directory.setText(str(directory))
        self._update_run_button()

    def _update_run_button(self, *_):
        self.run_button.setEnabled(bool(self.command.text().strip()))

    def run(self):
        if self.process.state() != QProcess.ProcessState.NotRunning:
            return
        directory = Path(self.directory.text()).expanduser()
        if not directory.is_dir():
            QMessageBox.warning(self, "Folder not found", "Choose an existing working folder.")
            return
        command = self.command.text().strip()
        if not command:
            return
        if self.preset and command == self.suggested_command:
            program, arguments, _ = self.preset
            if os.name == "nt":
                self.process.setNativeArguments("")
        else:
            if os.name == "nt":
                program = os.environ.get("COMSPEC", r"C:\Windows\System32\cmd.exe")
                arguments = []
                self.process.setNativeArguments(f'/d /s /c "{command}"')
            else:
                program, arguments = "/bin/sh", ["-c", command]
        self.log.setPlainText(
            f"Command: {self.command.text()}\nProfile: {self.profile or 'none'} (consumption unverified)\n\n"
        )
        self.process.setWorkingDirectory(str(directory))
        self.process.setProgram(str(program))
        self.process.setArguments([str(item) for item in arguments])
        self.process.start()
        self.run_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def _read_output(self):
        data = bytes(self.process.readAllStandardOutput()) + bytes(
            self.process.readAllStandardError()
        )
        self.log.insertPlainText(data.decode(locale.getpreferredencoding(False), errors="replace"))

    def _finished(self, code: int, _status):
        self._read_output()
        self.log.appendPlainText(f"\nFinished with exit code {code}.")
        self._update_run_button()
        self.stop_button.setEnabled(False)

    def _error(self, error):
        self.log.appendPlainText(f"\nProcess error: {self.process.errorString()}")
        if error == QProcess.ProcessError.FailedToStart:
            self.run_button.setEnabled(True)
            self.stop_button.setEnabled(False)

    def stop(self):
        if self.process.state() == QProcess.ProcessState.NotRunning:
            return
        Thread(
            target=terminate_process_tree, args=(int(self.process.processId()),), daemon=True
        ).start()
        QTimer.singleShot(4000, self._kill_if_running)

    def _kill_if_running(self):
        if self.process.state() != QProcess.ProcessState.NotRunning:
            self.process.kill()

    def closeEvent(self, event):
        if self.process.state() != QProcess.ProcessState.NotRunning:
            QMessageBox.information(self, "Command running", "Stop the command before closing.")
            event.ignore()
        else:
            event.accept()
