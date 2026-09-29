"""Catalog behavior uses synthetic schemas, never a user's engine installation."""

import json

import pytest

from ue5_ubt_config_wizard.catalog import (
    NAMESPACE,
    SchemaInventoryError,
    catalog_report,
    schema_inventory,
    settings,
    validate_document,
)


def write_schema(tmp_path, properties, extra=""):
    path = tmp_path / "BuildConfiguration.Schema.xsd"
    path.write_text(
        f'<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" '
        f'xmlns:u="{NAMESPACE}" targetNamespace="{NAMESPACE}" elementFormDefault="qualified">'
        f'{extra}<xs:element name="Configuration"><xs:complexType><xs:all>'
        f'<xs:element name="BuildConfiguration"><xs:complexType><xs:all>{properties}'
        "</xs:all></xs:complexType></xs:element></xs:all></xs:complexType></xs:element></xs:schema>",
        encoding="utf-8",
    )
    return path


def engine_with_schema(tmp_path, properties):
    engine = tmp_path / "UE_5_Test"
    schema_dir = engine / "Engine/Saved/UnrealBuildTool"
    schema_dir.mkdir(parents=True)
    build_dir = engine / "Engine/Build"
    build_dir.mkdir()
    (build_dir / "Build.version").write_text(
        json.dumps({"MajorVersion": 5, "MinorVersion": 8, "PatchVersion": 1}),
        encoding="utf-8",
    )
    write_schema(schema_dir, properties)
    return engine


def test_documentation_inventory_is_large_sourced_and_honest():
    report = catalog_report()
    records = report["settings"]
    assert report["documented_count"] == 551
    assert len({(item.category, item.name) for item in records}) == len(records)
    assert len({item.category for item in records}) == 34
    assert all(item.source.startswith("https://dev.epicgames.com/") for item in records)
    assert report["editable_scalar_count"] == 20
    assert report["description_gap_count"] == 412
    explained = next(
        item
        for item in records
        if (item.category, item.name) == ("BuildConfiguration", "bUseAdaptiveUnityBuild")
    )
    assert "incremental compile" in explained.description
    assert explained.has_reviewed_description
    assert explained.kind == "unknown"
    assert all(item.status != "verified" for item in records)


def test_draft_errors_are_not_reintroduced():
    by_key = {(item.category, item.name): item for item in settings()}
    assert ("BuildConfiguration", "bArtifactRead") in by_key
    assert ("BuildConfiguration", "bArtifactWrites") in by_key
    assert ("BuildConfiguration", "bEnableAddressSanitizer") in by_key
    assert not any(key[0] in {"IODataSource", "SourceCodeControl"} for key in by_key)
    assert by_key[("WindowsPlatform", "WindowsSdkVersion")].kind == "string"
    assert "zero" in by_key[("BuildConfiguration", "MaxParallelActions")].description


def test_schema_provides_types_instead_of_name_guessing(tmp_path):
    path = write_schema(
        tmp_path,
        '<xs:element name="bActuallyText" type="xs:string"/>'
        '<xs:element name="Toggle" type="xs:boolean"/>'
        '<xs:element name="Counter" type="xs:int"/>',
    )
    records = {item.name: item for item in schema_inventory(path)}
    assert records["bActuallyText"].kind == "string"
    assert records["Toggle"].kind == "bool"
    assert records["Counter"].xml_type == "int"
    assert len(records["Counter"].schema_sha256) == 64
    assert records["Counter"].schema_source == str(path.resolve())


def test_schema_enumerations_and_collections(tmp_path):
    path = write_schema(
        tmp_path,
        '<xs:element name="Mode"><xs:simpleType><xs:restriction base="xs:string">'
        '<xs:enumeration value="Latest"/><xs:enumeration value="Preview"/>'
        "</xs:restriction></xs:simpleType></xs:element>"
        '<xs:element name="Values"><xs:complexType><xs:sequence>'
        '<xs:element name="Item" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>'
        "</xs:sequence></xs:complexType></xs:element>",
    )
    records = {item.name: item for item in schema_inventory(path)}
    assert records["Mode"].kind == "enum"
    assert records["Mode"].choices == ("Latest", "Preview")
    assert records["Values"].kind == "list"
    assert records["Values"].item_kind == "string"


def test_named_types_and_unimplemented_facets_remain_explicit(tmp_path):
    path = write_schema(
        tmp_path,
        '<xs:element name="Alias" type="u:TextAlias"/>'
        '<xs:element name="Limited" type="u:Limited"/>',
        '<xs:simpleType name="TextAlias"><xs:restriction base="u:TextBase"/></xs:simpleType>'
        '<xs:simpleType name="TextBase"><xs:restriction base="xs:string"/></xs:simpleType>'
        '<xs:simpleType name="Limited"><xs:restriction base="xs:int">'
        '<xs:minInclusive value="7"/></xs:restriction></xs:simpleType>',
    )
    records = {item.name: item for item in schema_inventory(path)}
    assert records["Alias"].kind == "string"
    assert records["Limited"].kind == "unknown"


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
def test_schema_rejects_dtd_even_with_utf16(tmp_path, encoding):
    path = tmp_path / "danger.xsd"
    text = (
        '<?xml version="1.0" encoding="' + encoding + '"?>'
        '<!DOCTYPE schema [<!ENTITY stolen SYSTEM "file:///must-not-read">]>'
        f'<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="{NAMESPACE}"/>'
    )
    path.write_bytes(text.encode(encoding))
    with pytest.raises(SchemaInventoryError, match="DTD"):
        schema_inventory(path)


def test_schema_refuses_network_imports_and_wrong_namespace(tmp_path):
    path = write_schema(
        tmp_path, "", '<xs:include schemaLocation="https://example.invalid/evil.xsd"/>'
    )
    with pytest.raises(SchemaInventoryError, match="composed"):
        schema_inventory(path)
    path.write_text('<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>', encoding="utf-8")
    with pytest.raises(SchemaInventoryError, match="namespace"):
        schema_inventory(path)


def test_overlay_retains_missing_documented_candidates_read_only(tmp_path):
    engine = engine_with_schema(
        tmp_path,
        '<xs:element name="bUseUnityBuild" type="xs:boolean"/>'
        '<xs:element name="CustomForkSetting" type="xs:string"/>',
    )
    report = catalog_report(engine)
    by_key = {(item.category, item.name): item for item in report["settings"]}
    assert report["engine_version"] == "5.8.1"
    assert report["local_schema_count"] == 2
    assert len(report["settings"]) == 552
    assert by_key[("BuildConfiguration", "bUseUnityBuild")].kind == "bool"
    assert by_key[("BuildConfiguration", "bUseUnityBuild")].has_reviewed_description
    assert by_key[("BuildConfiguration", "CustomForkSetting")].kind == "string"
    assert not by_key[("BuildConfiguration", "CustomForkSetting")].has_reviewed_description
    assert by_key[("BuildConfiguration", "bAllowUBAExecutor")].kind == "unknown"
    assert "independently" in " ".join(report["warnings"])


def test_engine_version_mismatch_is_not_silently_accepted(tmp_path):
    engine = tmp_path / "Engine"
    (engine / "Build").mkdir(parents=True)
    (engine / "Build/Build.version").write_text(
        '{"MajorVersion":5,"MinorVersion":4,"PatchVersion":0}', encoding="utf-8"
    )
    report = catalog_report(engine)
    assert report["editable_scalar_count"] == 0
    assert any("5.4.0" in warning for warning in report["warnings"])


def test_broken_schema_reports_failure_without_claiming_local_coverage(tmp_path):
    engine = engine_with_schema(tmp_path, '<xs:element name="Count" type="xs:int"/>')
    path = engine / "Engine/Saved/UnrealBuildTool/BuildConfiguration.Schema.xsd"
    path.write_text("<broken", encoding="utf-8")
    report = catalog_report(engine)
    assert report["local_schema_count"] == 0
    assert report["schema_sha256"] is None
    assert any("Malformed schema" in warning for warning in report["warnings"])


def test_schema_size_limit(tmp_path):
    path = tmp_path / "large.xsd"
    path.write_bytes(b" " * (8 * 1024 * 1024 + 1))
    with pytest.raises(SchemaInventoryError, match="limit"):
        schema_inventory(path)


def test_document_validation_checks_actual_xsd_constraints(tmp_path):
    engine = engine_with_schema(tmp_path, '<xs:element name="Count" type="xs:unsignedByte"/>')

    def document(value):
        return (
            f'<Configuration xmlns="{NAMESPACE}"><BuildConfiguration>'
            f"<Count>{value}</Count></BuildConfiguration></Configuration>"
        ).encode()

    assert validate_document(document(255), engine) == []
    assert validate_document(document(256), engine)
    assert validate_document(document(-1), engine)
    assert validate_document(document(12), None)
    assert "DTD" in validate_document(b"<!DOCTYPE Configuration><Configuration/>", engine)[0]
