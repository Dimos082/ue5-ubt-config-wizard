"""Behavioral checks for safe profile editing; no Unreal installation is used."""

from pathlib import Path

import pytest

from ue5_ubt_config_wizard.profile import NAMESPACE, ProfileDocument, ProfileError

SAMPLE = f"""<?xml version="1.0" encoding="UTF-8"?>
<Configuration xmlns="{NAMESPACE}">
  <!-- keep this note -->
  <BuildConfiguration>
    <bUseUnityBuild>true</bUseUnityBuild>
    <UnknownSetting>stay</UnknownSetting>
  </BuildConfiguration>
</Configuration>
""".encode()


def test_load_noop_does_not_rewrite_bytes(tmp_path: Path) -> None:
    source = tmp_path / "BuildConfiguration.xml"
    source.write_bytes(SAMPLE)
    document = ProfileDocument.open(source)
    assert document.entries()[0].value == "true"
    assert document.render() == SAMPLE
    assert document.save(source) is None
    assert source.read_bytes() == SAMPLE
    assert not list(tmp_path.glob("*.bak"))


def test_edit_preview_backup_and_preserve_unrelated_xml(tmp_path: Path) -> None:
    source = tmp_path / "BuildConfiguration.xml"
    source.write_bytes(SAMPLE)
    document = ProfileDocument.open(source)
    document.set("BuildConfiguration", "bUseUnityBuild", "false")
    document.set("BuildConfiguration", "MaxParallelActions", "0")
    assert b"<MaxParallelActions>0</MaxParallelActions>" in document.render()
    backup = document.save(source)
    assert backup is not None
    assert backup.read_bytes() == SAMPLE
    assert b"<!-- keep this note -->" in source.read_bytes()
    assert b"<UnknownSetting>stay</UnknownSetting>" in source.read_bytes()
    assert {entry.name: entry.value for entry in ProfileDocument.open(source).entries()}[
        "bUseUnityBuild"
    ] == "false"


def test_external_change_blocks_overwrite(tmp_path: Path) -> None:
    source = tmp_path / "BuildConfiguration.xml"
    source.write_bytes(SAMPLE)
    document = ProfileDocument.open(source)
    document.set("BuildConfiguration", "bUseUnityBuild", "false")
    source.write_bytes(SAMPLE.replace(b"stay", b"changed"))
    with pytest.raises(ProfileError, match="changed on disk"):
        document.save(source)
    assert b"changed" in source.read_bytes()
    assert document.dirty


def test_new_profile_uses_namespace_and_never_overwrites_racing_target(tmp_path: Path) -> None:
    document = ProfileDocument.new()
    document.set("BuildConfiguration", "bUseUnityBuild", "true")
    document.set("BuildConfiguration", "MaxParallelActions", "0")
    document.set("WindowsPlatform", "CompilerVersion", "Latest")
    target = tmp_path / "nested" / "BuildConfiguration.xml"
    assert document.save(target) is None
    assert target.is_file()
    saved = target.read_text(encoding="utf-8")
    assert "\n  <BuildConfiguration>\n    <bUseUnityBuild>true</bUseUnityBuild>" in saved
    assert "\n    <MaxParallelActions>0</MaxParallelActions>\n  </BuildConfiguration>" in saved
    assert "\n  <WindowsPlatform>\n    <CompilerVersion>Latest</CompilerVersion>" in saved
    assert ProfileDocument.open(target).entries()[0].value == "true"

    other = ProfileDocument.new()
    other.set("BuildConfiguration", "bUseUnityBuild", "false")
    with pytest.raises(ProfileError, match="exists"):
        other.save(target)
    assert ProfileDocument.open(target).entries()[0].value == "true"


def test_save_as_existing_requires_opt_in_and_backups_destination(tmp_path: Path) -> None:
    source = tmp_path / "one.xml"
    target = tmp_path / "two.xml"
    source.write_bytes(SAMPLE)
    target.write_bytes(SAMPLE.replace(b"stay", b"destination"))
    document = ProfileDocument.open(source)
    document.set("BuildConfiguration", "bUseUnityBuild", "false")
    with pytest.raises(ProfileError, match="exists"):
        document.save(target)
    original_target = target.read_bytes()
    backup = document.save(target, allow_overwrite=True)
    assert backup is not None and backup.read_bytes() == original_target
    assert source.read_bytes() == SAMPLE
    assert b"false" in target.read_bytes()


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"<Configuration/>",
        b"<Configuration>",
        f'<!DOCTYPE Configuration [<!ENTITY x "boom">]><Configuration xmlns="{NAMESPACE}"/>'.encode(),
    ],
)
def test_invalid_input_is_rejected(tmp_path: Path, content: bytes) -> None:
    source = tmp_path / "bad.xml"
    source.write_bytes(content)
    with pytest.raises(ProfileError):
        ProfileDocument.open(source)


def test_prefixed_namespace_and_unknown_node_survive_edit(tmp_path: Path) -> None:
    source = tmp_path / "prefixed.xml"
    source.write_text(
        f'<ub:Configuration xmlns:ub="{NAMESPACE}" xmlns:x="urn:other">'
        "<ub:BuildConfiguration><ub:bUseUnityBuild>true</ub:bUseUnityBuild>"
        "<x:Custom>hello</x:Custom></ub:BuildConfiguration></ub:Configuration>",
        encoding="utf-8",
    )
    document = ProfileDocument.open(source)
    document.set("BuildConfiguration", "bUseUnityBuild", "false")
    document.save(source)
    saved = source.read_text(encoding="utf-8")
    assert "<x:Custom>hello</x:Custom>" in saved
    assert "false" in saved
    assert "\n  <ub:BuildConfiguration>\n    <ub:bUseUnityBuild>" in saved


def test_duplicate_scalar_setting_cannot_be_edited(tmp_path: Path) -> None:
    source = tmp_path / "duplicate.xml"
    source.write_text(
        f'<Configuration xmlns="{NAMESPACE}"><BuildConfiguration>'
        "<bUseUnityBuild>true</bUseUnityBuild>"
        "<bUseUnityBuild>false</bUseUnityBuild>"
        "</BuildConfiguration></Configuration>",
        encoding="utf-8",
    )
    document = ProfileDocument.open(source)
    with pytest.raises(ProfileError, match="Duplicate"):
        document.set("BuildConfiguration", "bUseUnityBuild", "false")
    assert not document.dirty


def test_remove_setting_also_removes_its_adjacent_comment(tmp_path: Path) -> None:
    source = tmp_path / "comments.xml"
    source.write_text(
        f'<Configuration xmlns="{NAMESPACE}"><BuildConfiguration>\n'
        "<!-- Forces local virtualization mode -->\n"
        "<bAllowUBAExecutor>true</bAllowUBAExecutor>\n"
        "<!-- Keep the comment for the next setting -->\n"
        "<bUseUnityBuild>false</bUseUnityBuild>"
        "</BuildConfiguration></Configuration>",
        encoding="utf-8",
    )
    document = ProfileDocument.open(source)
    document.remove("BuildConfiguration", "bAllowUBAExecutor")
    document.save(source)
    saved = source.read_bytes()
    assert b"Forces local virtualization mode" not in saved
    assert b"Keep the comment for the next setting" in saved
    assert b"bAllowUBAExecutor" not in saved


def test_remove_setting_keeps_separated_section_comment(tmp_path: Path) -> None:
    source = tmp_path / "comments.xml"
    source.write_text(
        f'<Configuration xmlns="{NAMESPACE}"><BuildConfiguration>\n'
        "<!-- General build notes -->\n\n"
        "<bUseUnityBuild>true</bUseUnityBuild>"
        "</BuildConfiguration></Configuration>",
        encoding="utf-8",
    )
    document = ProfileDocument.open(source)
    document.remove("BuildConfiguration", "bUseUnityBuild")
    assert b"General build notes" in document.render()
