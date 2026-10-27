#!/usr/bin/env python3
"""
pull_source.py — extract, highlight, and open pages from a source code PDF.

Usage:
    python pull_source.py <SOURCE_KEY> <START_PAGE> <END_PAGE> [--highlight "text"]... [--out NAME]

<SOURCE_KEY> must match an entry in sources.json (repo root). Page numbers are
the PDF's own physical page numbers (what you'd type into a reader's "go to
page" box), 1-indexed, matching the page numbers cited in the vault notes.

Examples:
    python pull_source.py IS456 45 46
    python pull_source.py NBC2026 2774 2776 --highlight "Table 1" --highlight "travel distance"

Output: a highlighted copy is written to _pulled/<SOURCE_KEY>_p<start>-<end>.pdf
(gitignored — never commit these) and opened with the OS default PDF handler.
The output path is always printed, so it can be referenced/opened manually
too (e.g. via the Browser pane in Claude Code Desktop).
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    print("ERROR: pymupdf is not installed. Run: pip install pymupdf", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = REPO_ROOT / "sources.json"
OUT_DIR = REPO_ROOT / "_pulled"


def load_sources() -> dict:
    if not SOURCES_FILE.exists():
        print(
            f"ERROR: {SOURCES_FILE} not found.\n"
            f"Copy sources.template.json to sources.json and fill in the path(s) "
            f"to your own copies of the code PDFs. See README.md.",
            file=sys.stderr,
        )
        sys.exit(1)
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_path(source_key: str, sources: dict) -> Path:
    if source_key not in sources:
        known = ", ".join(sorted(sources.keys())) or "(none configured)"
        print(
            f"ERROR: '{source_key}' is not in sources.json.\n"
            f"Configured keys: {known}\n"
            f"Add an entry for '{source_key}' pointing at your PDF, or check CODES-COVERED.md "
            f"for the exact key names this project expects.",
            file=sys.stderr,
        )
        sys.exit(1)
    p = Path(sources[source_key])
    if not p.exists():
        print(f"ERROR: sources.json points '{source_key}' at {p}, but that file doesn't exist.", file=sys.stderr)
        sys.exit(1)
    return p


def open_file(path: Path):
    """Best-effort open with the OS default handler. Never fatal if it fails."""
    try:
        if sys.platform.startswith("win"):
            os.startfile(str(path))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])
    except Exception as e:
        print(f"(couldn't auto-open the file: {e} — open it manually from the path above)", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description="Extract, highlight, and open pages from a source code PDF.")
    ap.add_argument("source_key", help="Key from sources.json, e.g. IS456, NBC2026")
    ap.add_argument("start_page", type=int, help="First page to pull (1-indexed, PDF physical page number)")
    ap.add_argument("end_page", type=int, help="Last page to pull (inclusive)")
    ap.add_argument("--highlight", action="append", default=[], help="Exact text to highlight (repeatable)")
    ap.add_argument("--out", default=None, help="Output filename (default: auto-generated)")
    args = ap.parse_args()

    if args.end_page < args.start_page:
        print("ERROR: end_page must be >= start_page.", file=sys.stderr)
        sys.exit(1)

    sources = load_sources()
    src_path = resolve_path(args.source_key, sources)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_name = args.out or f"{args.source_key}_p{args.start_page}-{args.end_page}.pdf"
    out_path = OUT_DIR / out_name

    src = pymupdf.open(str(src_path))
    n_pages = len(src)
    if args.start_page < 1 or args.end_page > n_pages:
        print(f"ERROR: {src_path.name} has {n_pages} pages; requested {args.start_page}-{args.end_page}.", file=sys.stderr)
        sys.exit(1)

    out = pymupdf.open()
    out.insert_pdf(src, from_page=args.start_page - 1, to_page=args.end_page - 1)

    hit_count = 0
    for term in args.highlight:
        for pg in out:
            rects = pg.search_for(term)
            for r in rects:
                pg.add_highlight_annot(r)
                hit_count += 1

    out.save(str(out_path))
    out.close()
    src.close()

    print(f"PULLED: {src_path.name}, pages {args.start_page}-{args.end_page} -> {out_path}")
    if args.highlight:
        print(f"Highlighted {hit_count} match(es) for: {', '.join(args.highlight)}")
        if hit_count == 0:
            print("WARNING: no highlight matches found - the search text may not match the page's exact wording.", file=sys.stderr)

    open_file(out_path)


if __name__ == "__main__":
    main()
