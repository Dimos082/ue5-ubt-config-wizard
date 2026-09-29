"""Discovery and command construction operate only on synthetic paths."""

import json
from pathlib import Path

from ue5_ubt_config_wizard import discovery, runner


def test_engine_version_reads_descriptor(tmp_path: Path) -> None:
    descriptor = tmp_path / "Engine" / "Build" / "Build.version"
    descriptor.parent.mkdir(parents=True)
    descriptor.write_text(
        json.dumps({"MajorVersion": 5, "MinorVersion": 7, "PatchVersion": 2}), encoding="utf-8"
    )
    assert discovery.engine_version(tmp_path) == "5.7.2"


def test_candidate_profiles_include_project_and_user_config(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(discovery.Path, "home", lambda: tmp_path)
    monkeypatch.setattr(discovery.sys, "platform", "linux")
    project = tmp_path / "Demo" / "Demo.uproject"
    result = discovery.candidate_profiles(None, project)
    assert (
        tmp_path / ".config" / "Unreal Engine" / "UnrealBuildTool" / "BuildConfiguration.xml"
        in result
    )
    assert tmp_path / "Demo" / "Saved" / "UnrealBuildTool" / "BuildConfiguration.xml" in result


def test_preset_requires_real_engine_files(tmp_path: Path, monkeypatch) -> None:
    assert runner.default_command(None, None) is None
    ubt = tmp_path / "Engine" / "Binaries" / "DotNET" / "UnrealBuildTool" / "UnrealBuildTool.dll"
    ubt.parent.mkdir(parents=True)
    ubt.write_bytes(b"fake")
    project = tmp_path / "Game Project" / "Game.uproject"
    project.parent.mkdir()
    project.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(runner, "_dotnet_for", lambda _: "dotnet")
    command = runner.default_command(tmp_path, project)
    assert command is not None
    program, args, cwd = command
    assert program == "dotnet"
    assert args[-1] == f"-Project={project}"
    assert args[1] == "GameEditor"
    assert cwd == tmp_path
    assert runner.default_command(tmp_path / "Engine", project) is not None
    assert (
        tmp_path / "Engine" / "Saved" / "UnrealBuildTool" / "BuildConfiguration.xml"
        in discovery.candidate_profiles(tmp_path / "Engine")
    )
