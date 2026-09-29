# Compatibility record

## Initial delivery

| Layer | Status |
|---|---|
| Python | Declared support: CPython 3.12 and 3.13 |
| Application OS | Windows, macOS and Linux targets; consult CI for each tested revision |
| Catalog descriptions | Bundled documentation-backed metadata with source links |
| Exact UE installation/schema acceptance | Not certified in this source delivery |
| Complete setting inventory for all UE5 versions | Not claimed |
| Native OS/CPU artifacts | Available only when the release workflow successfully builds that named target |
| Code signing/notarization | Not configured |

Documentation version scope is evidence about the documented page, not proof of acceptance by every patch release or custom engine branch. Unknown versions must stay unverified. A passing application CI run is not an Unreal Engine build test.

## Add a verified engine record

Record engine major/minor/patch/changelist, installed/source-build layout, config-reader/schema identity, host OS/toolchain, test command and date. Compare the full XML-configurable inventory against catalog entries. Record unknown descriptions, unsupported list codecs, aliases and exclusions. Keep private engine source/schema data out of Git.

Use [the owner-run integration procedure](testing.md#owner-run-engine-integration) and add results here only after they have actually run. Never mark a nearby engine version verified by inference.

