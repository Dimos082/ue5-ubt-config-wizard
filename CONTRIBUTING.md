# Contributing

Create a focused branch, install the development dependencies from the documented constraints file, and run Ruff plus pytest before proposing a change. See [testing](docs/testing.md) for commands.

Tests must exercise application behavior using temporary directories and synthetic XML. Never commit a real profile, backup, log, engine source/schema cache or credential. Keep fixtures in `tests/fixtures`; ignored personal files belong in `local-data`.

Catalog changes need a source URL or local source locator, matching engine/version scope, claim-level provenance and a stated uncertainty where evidence is incomplete. A new name from a search result is a candidate, not verified XML support. Add regression coverage for parsing, value semantics and serialization.

Preserve comments and unknown content. Do not run commands on profile load, UI selection, catalog refresh or test collection. Tests marked `engine` must remain excluded by default and require explicit owner opt-in.

The maintainer chooses versions and releases. Do not create version-bump commits from workflows. Review [architecture](docs/architecture.md) and [release policy](docs/releasing.md).

