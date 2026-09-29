# Testing

## Local application checks

Use Python 3.12 or 3.13 in a virtual environment. Windows commands (use `.venv/bin/python` on macOS/Linux):

```powershell
.\.venv\Scripts\python.exe -m pip install -c requirements-dev.lock -e ".[dev]"
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m build
```

The constraints file pins direct dependencies and Qt's split distributions. It is not a complete transitive lock with hashes. Review resolved dependencies per OS when refreshing it.

Tests use synthetic profiles and temporary directories. They exercise parsing, namespaces, staged values, unknown content, backup/save failures, stale-file conflicts, discovery and harmless command processes. GUI tests use pytest-qt. Headless runs set `QT_QPA_PLATFORM=offscreen`; a successful offscreen startup is not a full desktop usability check.

## GitHub Actions

`ci.yml` runs on every branch push and pull request, plus manual dispatch and release reuse. Its matrix is Windows, Ubuntu and macOS × Python 3.12/3.13. A stable `CI / required` aggregate rejects failed, cancelled or unexpectedly skipped mandatory jobs. No path filters or concurrency cancellation silently omit advertised checks.

Normal CI validates the event revision. Local commits not pushed to GitHub cannot trigger Actions. Intermediate commits in a multi-commit push are not individually tested. Strict historical-commit testing is not implemented; push separately and run checks before each commit when individual revision evidence is required.

GitHub-hosted jobs never need Epic credentials or an engine download. A green application workflow does not certify Unreal compatibility. Workflow files are generated locally and start only when the owner uploads them to an Actions-enabled repository.

## Owner-run engine integration

No automatic real-engine suite is included in this initial delivery. The `engine` marker is excluded by normal pytest defaults. Future engine tests must require an additional explicit opt-in and avoid engine access during module import/collection.

Before an integration check, record the engine identity, project, selected profile and exact command. Use a disposable profile/project and retain an independent original backup. Verify XML structure against the matching local schema where available, then run the chosen build script manually or through the app. Inspect the engine's logs for evidence of profile consumption; a successful build alone is insufficient.

Record the actual command, exit status, settings tested and limitations in the compatibility record. Restore any approved test changes and verify the restored bytes. Do not claim this procedure ran until the owner performs it.

