# Owner-operated releases

The owner updates the single version in `src/ue5_ubt_config_wizard/__init__.py`, adds a matching changelog entry, runs checks and pushes the source commit. There are no keyword-based version bumps or workflow-created tags.

After routine CI succeeds, create and push one annotated tag:

```powershell
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

Choose a fresh version for later releases. The workflow accepts tags shaped `vMAJOR.MINOR.PATCH`; it verifies an annotated tag, package/changelog agreement and ancestry on the repository's default branch. It checks out and tests the tagged revision before building.

The release calls the same Windows/Ubuntu/macOS × Python3.12/3.13 test workflow, then produces a Python wheel/source archive and OS/architecture-specific PyInstaller **portable onedir archives**. These are extracted directories containing the executable and its libraries, not installers. Keep the entire directory together. macOS/Linux use tar.gz to preserve executable permission bits; Windows uses ZIP.

Each native build runs on its target OS, checks startup outside the checkout, and collects available dependency notices. Assets are unsigned and macOS builds are unnotarized. CI runner labels and CPU architecture are recorded in the filenames; no universal binary is claimed. Source and native support are distinct.

The final job creates SHA-256 checksums and a draft GitHub Release only after checks/builds pass. An existing release with that tag makes creation fail; a rerun does not overwrite its assets. For a failed partial draft, review it and remove that draft manually before retrying, or choose a new version.

Review release notes, required artifacts, test results, engine compatibility limits and dependency notices before selecting **Publish release**. The draft is marked prerelease initially. Change that status only when its actual readiness supports it. GitHub does not require a personal access token stored in repository secrets for this workflow; its final job uses the scoped GITHUB_TOKEN.

The supplied Apache-2.0 project license is proposed. Confirm it before public distribution. Qt and other dependency obligations remain separate. Review the collected license texts and component requirements before distributing binaries.

Useful references: [GitHub release management](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), [GitHub CLI draft/tag options](https://cli.github.com/manual/gh_release_create), [PyInstaller distribution modes](https://pyinstaller.org/en/stable/operating-mode.html).

