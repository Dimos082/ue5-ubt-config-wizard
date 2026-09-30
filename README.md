# UE5 UBT Configuration Wizard

**Understand, edit, and undo Unreal Engine C++ build-setting changes without hand-editing XML.**

Adjusting an Unreal C++ build often means finding `BuildConfiguration.xml`, looking up unfamiliar settings, and editing the file by hand. When you are investigating build resource usage, trying a different executor, or changing unity-build behavior, you also need to keep track of what changed and how to restore the previous configuration.

UE5 UBT Configuration Wizard brings that work into one desktop interface. Open a profile, inspect its settings, read available explanations with links to the source, and add or remove values. Review the XML diff before saving; the app backs up an existing file before replacing it. You can then run a local build command and inspect its output.

Built for **UE5 C++ developers, plugin authors, and build engineers** working with UnrealBuildTool XML profiles. Available for Windows, macOS, and Linux.

[Download the app](https://github.com/Dimos082/ue5-ubt-config-wizard/releases) · [Usage guide](docs/usage.md) · [Report a problem](https://github.com/Dimos082/ue5-ubt-config-wizard/issues)

![A loaded XML profile with its settings and editing controls](docs/screenshot.png)

## When is it useful?

| What you want to investigate | How the wizard helps |
| --- | --- |
| The build runs too many actions at once | Find and edit concurrency settings such as `MaxParallelActions`, then test the change on your machine. |
| You need to inspect UBA or another build executor's configuration | See the flags present in the profile, read their explanations, and review exactly what you changed. |
| You want to compare unity-build behavior while developing C++ code | Edit settings such as `bUseUnityBuild`, save a separate profile copy, and restore the previous file when needed. |

These are investigation workflows, not automatic tuning presets. The best values depend on your engine, project, hardware, and toolchain. Setting semantics are documented in [Epic's Build Configuration reference](https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine).

## Try it

Download a portable archive from [Releases](https://github.com/Dimos082/ue5-ubt-config-wizard/releases):

| Your computer | Archive name contains |
| --- | --- |
| Windows, Intel or AMD 64-bit | `windows-amd64.zip` |
| Linux x64, built on Ubuntu | `linux-x86_64.tar.gz` |
| macOS, Apple Silicon | `darwin-arm64.tar.gz` |

Extract the **whole folder**, then launch `ue5-ubt-config-wizard.exe` on Windows or `ue5-ubt-config-wizard` on macOS/Linux. Keep the executable and its supporting files together. Portable builds include their Python runtime; a separate Python installation is not required. Builds are unsigned, and the macOS build is not notarized.

1. Open a suggested XML file, browse to another, or create a new profile.
2. Select a setting to read its description and source. Double-click to edit, or use **+ Add setting** to search the catalog.
3. Choose **Review changes**, then **Save changes**. An existing destination gets a backup before replacement.
4. Optionally use **Tools → Run build check** to run a command against the saved configuration and inspect its output.

Use **File** to save a copy, back up, or restore a profile. **View → Night mode** switches to the [dark theme](docs/night-mode.png).

## Scope and compatibility

The app edits one `BuildConfiguration.xml` at a time. It helps you make and review configuration changes; it does not automatically diagnose build failures, benchmark improvements, or choose optimal settings.

It does not edit `Build.cs`, `Target.cs`, or INI files, and it does not provide a game-packaging workflow. Unreal's Development, DebugGame, and Shipping configurations are separate concepts; see [Epic's build configurations guide](https://dev.epicgames.com/documentation/unreal-engine/build-configurations-reference-for-unreal-engine).

The bundled catalog has **551 documented category/name candidates**, **139 reviewed explanations**, and **20 reviewed scalar value types**, based on Epic's UE 5.8 documentation. Candidates with unverified types remain clearly marked and accept raw text. Unknown or nested XML content is retained; the editor changes direct scalar settings.

An available local engine schema can check XML structure. It does not establish all setting behavior, and a successful build command does not prove which profile UBT loaded. Consult the build log and the documentation for your exact engine version. [Compatibility details](docs/supported-engines.md) · [Catalog sources and review process](docs/catalog-provenance.md).

Profile editing works offline. A build command you choose to run may use network services or other local tools.

## Run from source

With Python **3.12 or 3.13**, run these commands from a clone or extracted source directory.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -c requirements-dev.lock .
.\.venv\Scripts\python.exe -m ue5_ubt_config_wizard
```

macOS/Linux, using Python 3.12 or 3.13:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -c requirements-dev.lock .
.venv/bin/python -m ue5_ubt_config_wizard
```

## Help improve it

The most useful contributions are **engine-version compatibility reports**, corrections to setting descriptions with source links, and reproducible bugs. Open an [issue](https://github.com/Dimos082/ue5-ubt-config-wizard/issues) with your engine version, OS, affected setting, and expected versus observed behavior. Remove private paths, server addresses, and credentials from shared profiles or logs.

See [CONTRIBUTING.md](CONTRIBUTING.md). If the tool helps your workflow, a star helps other developers discover it.

The [CI workflow](https://github.com/Dimos082/ue5-ubt-config-wizard/actions/workflows/ci.yml) runs application tests on Windows, macOS, and Linux with Python 3.12/3.13. These checks are separate from testing against a real Unreal Engine installation.

```bash
python -m pip install -c requirements-dev.lock -e ".[dev]"
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

[Maintainer release guide](docs/releasing.md) · [Manual GitHub setup](docs/manual-github-setup.md)

[Apache-2.0 license](LICENSE). Bundled dependencies have their own licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
