#!/usr/bin/env python3
"""Generate subjects/<slug>/sources/index.html: one "Official material" page per subject.

The pages are static (no JavaScript needed to list files), built from the same scan as
assets/data/sources.js, so every link points at a PDF that exists in sources/cuatrimestre-1/.
Laboratory material is never listed (sources_manifest excludes it).

    python tools/build_sources_pages.py          # (re)write the pages
    python tools/build_sources_pages.py --check  # exit 1 if any page is stale
"""
from __future__ import annotations

import argparse
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sources_manifest import build_manifest  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent

SUBJECTS = {
    "fluid-mechanics": ("Fluid Mechanics", "--accent-fluid"),
    "aerospace-materials-1": ("Aerospace Materials I", "--accent-materials"),
    "engineering-mechanics": ("Engineering Mechanics", "--accent-mechanics"),
    "advanced-maths": ("Advanced Mathematics", "--accent-maths"),
    "business-management": ("Business Management", "--accent-business"),
}
KIND_LABEL = {
    "teoria": "Theory", "slides": "Slides", "problemas": "Problem sheets",
    "examenes": "Exams", "schedule": "Schedule", "other": "Other",
}
KIND_ORDER = ("teoria", "slides", "problemas", "examenes", "schedule", "other")

CSS = """
    body { margin: 0; background: var(--bg-primary); color: var(--text-primary); font-family: var(--font-body); line-height: 1.6; }
    .wrap { max-width: 920px; margin: 0 auto; padding: 24px 16px 64px; }
    .top { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 24px; }
    .back { color: var(--accent); text-decoration: none; font-family: var(--font-sans); font-size: 0.95rem; }
    .back:hover { text-decoration: underline; }
    .theme-toggle { font-family: var(--font-sans); background: var(--bg-glass); color: var(--text-primary); border: 1px solid var(--border-card); border-radius: var(--radius-sm); padding: 6px 12px; cursor: pointer; }
    h1 { font-family: var(--font-display); font-weight: 400; font-size: 2.2rem; margin: 0 0 4px; }
    .lead { color: var(--text-secondary); margin: 0 0 28px; }
    h2 { font-family: var(--font-sans); font-size: 1.05rem; margin: 28px 0 8px; padding-bottom: 6px; border-bottom: 2px solid var(--accent); }
    h3 { font-family: var(--font-sans); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-muted); margin: 14px 0 4px; }
    ul { list-style: none; margin: 0; padding: 0; }
    li { padding: 6px 0; border-bottom: 1px solid var(--border-subtle); display: flex; justify-content: space-between; gap: 12px; }
    li a { color: var(--text-primary); text-decoration: none; word-break: break-word; }
    li a:hover { color: var(--accent); text-decoration: underline; }
    .size { color: var(--text-muted); font-family: var(--font-mono); font-size: 0.8rem; white-space: nowrap; }
    .note { margin-top: 36px; padding: 12px 16px; background: var(--bg-glass); border: 1px solid var(--border-card); border-radius: var(--radius-md); color: var(--text-secondary); font-size: 0.92rem; }
"""


def _size(n: int) -> str:
    return f"{n / 1024 / 1024:.1f} MB" if n >= 1024 * 1024 else f"{max(1, round(n / 1024))} KB"


def _group(title: str, bucket: dict) -> str:
    kinds = [k for k in KIND_ORDER if bucket.get(k)]
    if not kinds:
        return ""
    out = [f"<h2>{html.escape(title)}</h2>"]
    for kind in kinds:
        out.append(f"<h3>{KIND_LABEL[kind]}</h3>\n<ul>")
        for item in bucket[kind]:
            href = "../../../" + item["href"]
            out.append(f'<li><a href="{html.escape(href, quote=True)}">{html.escape(item["name"])}</a>'
                       f'<span class="size">{_size(item["bytes"])}</span></li>')
        out.append("</ul>")
    return "\n".join(out)


def render_page(slug: str, data: dict) -> tuple[str, int]:
    name, accent = SUBJECTS[slug]
    sections, count = [], 0
    general = data.get("general", {})
    count += sum(len(v) for v in general.values())
    sections.append(_group("Course-wide material", general))
    for unit in data["units"]:
        count += sum(len(unit[k]) for k in ("teoria", "slides", "problemas", "other") if k in unit)
        sections.append(_group(f"Unit {unit['number']}: {unit['title']}", unit))
    body = "\n".join(s for s in sections if s)
    page = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(name)} - Official Material</title>
  <meta name="description" content="Original course PDFs for {html.escape(name)} (UC3M).">
  <script src="../../../assets/js/theme.js"></script>
  <link rel="stylesheet" href="../../../assets/css/tokens.css">
  <style>
    :root {{ --accent: var({accent}); }}{CSS}  </style>
</head>
<body>
  <div class="wrap">
    <div class="top">
      <a class="back" href="../../../index.html">&larr; Study Portal</a>
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">Theme</button>
    </div>
    <h1>{html.escape(name)}: Official material</h1>
    <p class="lead">{count} original PDFs from the course (theory, slides and problem sheets), grouped by unit.</p>
{body}
    <p class="note">These are the course documents as published by the lecturers at Universidad Carlos III de Madrid. They are linked here for personal study; the notes and solutions elsewhere in this portal are written independently from them.</p>
  </div>
</body>
</html>
"""
    return page, count


def build(root: pathlib.Path = REPO) -> dict[pathlib.Path, str]:
    manifest = build_manifest(root)
    pages = {}
    for slug in SUBJECTS:
        if slug in manifest["subjects"]:
            pages[pathlib.Path(root, "subjects", slug, "sources", "index.html")] = render_page(slug, manifest["subjects"][slug])[0]
    return pages


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    stale = 0
    for path, content in build().items():
        current = path.read_bytes().decode("utf-8") if path.exists() else None
        if current is None or current.replace("\r\n", "\n") != content:  # git may check files out with CRLF
            stale += 1
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode("utf-8"))
                print("wrote", path.relative_to(REPO).as_posix())
            else:
                print("stale", path.relative_to(REPO).as_posix())
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
