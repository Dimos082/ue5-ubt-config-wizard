"""Fetch Epic documentation for a manual catalog review; never rewrite the catalog.

This deliberately extracts *candidates*, not verified XML addresses. A page can
mention code properties which are not XML-configurable in the selected engine.
Compare the report with a matching engine schema/source before editing records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from lxml import html

from ue5_ubt_config_wizard.catalog_data import DOCUMENTED_SETTINGS

SOURCE = (
    "https://dev.epicgames.com/documentation/unreal-engine/build-configuration-for-unreal-engine"
)
MAX_BYTES = 4 * 1024 * 1024
PROPERTY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s+(.+)", re.DOTALL)


def extract_candidates(page: bytes) -> tuple[str, dict[str, str]]:
    """Return the reported page version and property-like paragraphs for review."""
    document = html.fromstring(page)
    title = " ".join(document.xpath("//title/text()"))
    version = re.search(r"Unreal Engine\s+(\d+\.\d+)", title)
    candidates = {}
    for paragraph in document.xpath("//article//p"):
        match = PROPERTY.match(" ".join(paragraph.text_content().split()))
        if match:
            candidates[match.group(1)] = match.group(2)
    return version.group(1) if version else "unreported", candidates


def fetch_page(cache: Path, *, offline: bool) -> bytes:
    if offline:
        return cache.read_bytes()
    request = Request(SOURCE, headers={"User-Agent": "ue5-ubt-config-wizard-catalog-review/0.1"})
    with urlopen(request, timeout=20) as response:
        if "text/html" not in response.headers.get("Content-Type", ""):
            raise ValueError("Epic returned a non-HTML response")
        page = response.read(MAX_BYTES + 1)
    if len(page) > MAX_BYTES:
        raise ValueError("Documentation page exceeded the size limit")
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(page)
    return page


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="reuse the last cached page")
    parser.add_argument("--cache", type=Path, default=Path("catalog-cache/epic-build.html"))
    parser.add_argument("--output", type=Path, default=Path("catalog-cache/review.json"))
    args = parser.parse_args()
    try:
        page = fetch_page(args.cache, offline=args.offline)
        version, candidates = extract_candidates(page)
        if len(candidates) < 20:
            raise ValueError("The page layout did not yield a credible property inventory")
        known = {name for _, name in DOCUMENTED_SETTINGS}
        report = {
            "source": SOURCE,
            "reported_version": version,
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "page_sha256": hashlib.sha256(page).hexdigest(),
            "candidate_count": len(candidates),
            "bundled_distinct_name_count": len(known),
            "new_name_candidates": sorted(set(candidates) - known),
            "missing_from_page": sorted(known - set(candidates)),
            "review_required": (
                "Names and page explanations are evidence leads only. Verify category, "
                "XML type, behavior and exact engine version before changing the catalog."
            ),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Review report: {args.output} ({len(candidates)} candidates, UE {version})")
        return 0
    except (OSError, URLError, ValueError) as error:
        parser.exit(1, f"Documentation scan failed: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
