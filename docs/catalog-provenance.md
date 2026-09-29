# Catalog provenance

The bundled catalog is a documentation-backed starting point. It is not an exhaustive or certified inventory for all UE5 versions.

Every catalog entry should retain namespace/category/XML name, a proven value codec, concise original description, source links, source/version scope and evidence status. Unknown defaults, ranges or dependencies must stay unknown. Source comments sit next to records, and the GUI exposes the links.

Primary explanation source: [Epic's Build Configuration reference](https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine), labeled UE 5.8 when the bundled inventory was compiled. Structural acceptance and completeness need the exact engine's XML configuration annotations/schema, including any XML category/name aliases. Do not promote TargetRules, ModuleRules, INI values, CVars or arbitrary command-line switches merely because they look related.

Catalog maintenance is a deliberate developer operation. Run `python tools/documentation_scan.py` to fetch the official Build Configuration page with a timeout and size limit. Its ignored `catalog-cache/review.json` compares page property names against the bundled inventory and records the page version and SHA-256. Use `--offline` to review the cached page without network access. It emits candidates only: verify XML category, type and meaning against the exact engine before changing catalog code. `python tools/catalog_audit.py --engine PATH` reports local-schema coverage. Startup does not scrape the Internet, and network failures do not create replacement facts.

Public tests use synthetic evidence and XML. Engine source and local schemas remain outside the repository. Record true engine verification in [supported engines](supported-engines.md), including unresolved inventory entries and unsupported value shapes.
