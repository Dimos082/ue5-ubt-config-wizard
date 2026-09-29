"""The maintenance parser reports leads without creating catalog assertions."""

from tools.documentation_scan import extract_candidates


def test_extract_candidates_from_synthetic_epic_layout():
    page = b"""<html><head><title>Example | Unreal Engine 5.8 Documentation</title></head>
    <body><article>
      <p>MaxParallelActions : Number of actions allowed.</p>
      <p>Other discussion without a property marker.</p>
      <p><strong>bUseUnityBuild</strong> : Combine translation units.</p>
    </article></body></html>"""
    version, candidates = extract_candidates(page)
    assert version == "5.8"
    assert candidates == {
        "MaxParallelActions": "Number of actions allowed.",
        "bUseUnityBuild": "Combine translation units.",
    }
