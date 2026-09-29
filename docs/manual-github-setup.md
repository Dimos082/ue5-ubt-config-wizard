# Create and populate your GitHub repository

These commands are for the owner to execute. The generation agent does not create repositories, commit, push, tag, activate workflows or publish releases.

The intended remote is [Dimos082/ue5-ubt-config-wizard](https://github.com/Dimos082/ue5-ubt-config-wizard). Create it on GitHub as an **empty** repository without a README, license or gitignore, because those files are in this source tree. If it already contains work, stop and reconcile that history; do not force-push this folder over it.

## 1. Review and test locally

Open PowerShell in the generated project directory. Python 3.12 or 3.13 is required. This example uses 3.13:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -c requirements-dev.lock -e ".[dev]"
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m build
.\.venv\Scripts\python.exe tools/smoke_install.py
```

Use `py -3.12` when that is the installed version. On macOS/Linux use `python3.13 -m venv .venv` (or 3.12) and `.venv/bin/python` for the remaining Python commands.

Review the proposed license, README, catalog gaps, .gitignore and generated workflow files. Do not stage actual engine files, real XML profiles, backups, logs or credentials.

## 2. Initialize and commit

If this folder is not already a Git repository:

```powershell
git init -b main
```

If Git reports a missing identity, configure it **for this repository** using your own verified name/email:

```powershell
git config user.name "Your Name"
git config user.email "YOUR_VERIFIED_EMAIL_OR_GITHUB_NOREPLY_ADDRESS"
```

Review and commit the intended files:

```powershell
git status --short
git add .
git diff --cached --stat
git diff --cached
git commit -m "Initial UE5 UBT configuration wizard"
```

If anything sensitive was staged, unstage it and correct the ignore rules before committing.

## 3. Authenticate and push

Use Git Credential Manager's normal browser authentication or GitHub CLI `gh auth login`. Do not paste a token into a command or remote URL.

For the empty repository created in GitHub's browser UI:

```powershell
git remote add origin https://github.com/Dimos082/ue5-ubt-config-wizard.git
git remote -v
git push -u origin main
```

If `origin` already exists, inspect it before deciding whether to update it. Do not blindly add a duplicate remote.

**Alternative remote creation with GitHub CLI:** only when you have not created the remote in the browser, run `gh repo create Dimos082/ue5-ubt-config-wizard --private --source=. --remote=origin`, then `git push -u origin main`. Choose `--public` instead of `--private` if public visibility is your intent. Do not execute both creation paths.

## 4. Actions setup and validation

1. Open the repository's **Actions** tab after the initial push.
2. If Actions is disabled, enable it under **Settings → Actions → General**. Permit the official actions used by the workflows.
3. Inspect the **CI** run. Six matrix jobs cover three operating systems and two Python versions. All required jobs must succeed.
4. Under **Settings → Rules → Rulesets** (or branch protection where available), protect main and require the stable `CI / required` check after GitHub has observed its first run.
5. Keep normal workflow token permissions read-only. The release's final job requests `contents: write`; organization policy must permit that job when you want draft releases. No Epic credentials or custom token secret is needed.

A workflow does not need a manual 'upload' button: GitHub discovers files under `.github/workflows` after you push them. Push and PR checks activate then. Tag pushes activate release builds; the owner still publishes the resulting draft.

## 5. Subsequent changes

```powershell
git status --short
git diff
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
git add .
git diff --cached
git commit -m "Describe the change"
git push
```

Use focused staging instead of `git add .` when unrelated edits exist. Inspect the resulting Actions run before releasing.

For versions, tags, artifacts and publication, follow [releasing.md](releasing.md). Never force-push to make a failed release work.

References: [GitHub command-line import guide](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github), [GitHub Actions permissions](https://docs.github.com/en/actions/reference/security/secure-use).

