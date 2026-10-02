"""Copy the dairy heat-stress dashboard into the site as a public, preliminary release.

The canonical file in the dairy project is left untouched. The public copy gets a
"preliminary results" banner, a noindex tag, and no grant title.
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPO_ROOT.parent / "projects" / "dairy" / "outputs" / "dashboard" / "us_dairy_climate_dashboard.html"
DEST = REPO_ROOT / "dashboards" / "dairy-heat-stress" / "index.html"
PROJECT_URL = "/projects/climate-stress-dairy/"

HEAD_EXTRA = """  <meta name="robots" content="noindex">
  <style>
    .release-banner{display:flex;flex-wrap:wrap;align-items:center;gap:4px 14px;padding:9px 28px;background:rgba(247,201,72,.1);border-bottom:1px solid rgba(247,201,72,.35);color:var(--text);font-size:.86rem;line-height:1.45}
    .release-banner strong{color:var(--gold);font-size:.74rem;letter-spacing:.07em;text-transform:uppercase}
    .release-banner a{margin-left:auto;color:var(--gold);font-weight:600;text-decoration:none;white-space:nowrap}
    .release-banner a:hover{text-decoration:underline}
    @media (max-width:640px){.release-banner{padding:9px 16px}.release-banner a{margin-left:0}}
  </style>
</head>"""

BANNER = """<body>
  <div class="release-banner" role="note">
    <strong>Preliminary results</strong>
    <span>Snapshot {snapshot}. Estimates may change before the paper is published, so please check with the author before citing.</span>
    <a href="{project_url}">About this project &rarr;</a>
  </div>"""


def replace_once(html: str, pattern: str, repl: str, what: str) -> str:
    new, n = re.subn(pattern, lambda _: repl, html)
    if n != 1:
        sys.exit(f"error: expected exactly one match for {what}, found {n}. The dashboard markup changed; update this script.")
    return new


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="built dashboard HTML")
    args = parser.parse_args()

    if not args.source.is_file():
        sys.exit(f"error: dashboard not found at {args.source}")
    html = args.source.read_text(encoding="utf-8")

    m = re.search(r'"snapshot_label":"([^"]+)"', html)
    if not m:
        sys.exit("error: snapshot_label not found in dashboard metadata.")
    snapshot = m.group(1)

    html = replace_once(html, r" under the grant <em>[^<]+</em>", "", "grant title")
    html = replace_once(html, r"Offline dashboard of", "Interactive dashboard of", "meta description")
    html = replace_once(html, r"<span>offline review edition</span>", "<span>preliminary web edition</span>", "edition label")
    html = replace_once(html, r"</head>", HEAD_EXTRA, "</head>")
    html = replace_once(html, r"<body>", BANNER.format(snapshot=snapshot, project_url=PROJECT_URL), "<body>")

    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(html, encoding="utf-8", newline="\n")
    print(f"Published snapshot {snapshot} -> {DEST.relative_to(REPO_ROOT)} ({DEST.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
