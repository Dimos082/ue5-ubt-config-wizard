"""Report catalog coverage without modifying the engine, profile, or catalog.

The bundled documentation inventory is UE 5.8 evidence. A selected engine's
local XSD adds structural evidence when present, but this report never claims
that the schema matches the installed UBT binary or proves runtime behavior.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ue5_ubt_config_wizard.catalog import catalog_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", type=Path, help="Unreal Engine installation root")
    parser.add_argument("--output", type=Path, help="write this read-only report as JSON")
    args = parser.parse_args()
    result = catalog_report(args.engine)
    report = {key: value for key, value in result.items() if key != "settings"}
    report["unreviewed_examples"] = [
        f"{item.category}/{item.name}"
        for item in result["settings"]
        if not item.has_reviewed_description
    ][:20]
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Catalog audit saved to {args.output}")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
