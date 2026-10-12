#!/usr/bin/env python3
"""Generate the two PDF pages of each subject from the scan behind assets/data/sources.js:

    subjects/<slug>/sources/index.html   "Theory & exercise PDFs": theory, slides, problem sheets
                                         and schedule, grouped by unit (no exams)
    subjects/<slug>/exams/index.html     "Exams": past partials and finals, grouped by exam
                                         (first, second, third partial, final) and sorted by
                                         year, newest first (only for subjects with exams)

The pages are static (no JavaScript needed to list files), so every link points at a PDF that
exists in sources/cuatrimestre-1/. Laboratory material is never listed (sources_manifest
excludes it). Exam files are classified from their names, SUBJECT_KIND_YEAR[_DETAILS].pdf
(e.g. FLUIDS_FINALEXAM_2014_ORD_SOL_P1.pdf); byte-identical copies are listed once.

    python tools/build_sources_pages.py          # (re)write the pages
    python tools/build_sources_pages.py --check  # exit 1 if any page is stale
"""
from __future__ import annotations

import argparse
import hashlib
import html
import pathlib
import re
import sys
from urllib.parse import unquote

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
    "schedule": "Schedule", "other": "Other",
}
KIND_ORDER = ("teoria", "slides", "problemas", "schedule", "other")

# Same families as the root index.html.
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=JetBrains+Mono:ital,wght@0,400;0,500;'
         '0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600;'
         '1,6..72,700&display=swap" rel="stylesheet">')

CSS = """
    body { margin: 0; background: var(--bg-primary); color: var(--text-primary); font-family: var(--font-body); font-size: 1.06rem; line-height: 1.6; }
    .wrap { max-width: 920px; margin: 0 auto; padding: 24px 16px 64px; }
    .top { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 20px; }
    .back { color: var(--accent); text-decoration: none; font-family: var(--font-mono); font-size: 0.85rem; letter-spacing: 0.02em; }
    .back:hover { text-decoration: underline; }
    .top-actions { display: flex; align-items: center; gap: 10px; }
    .theme-toggle { font-family: var(--font-mono); font-size: 0.8rem; background: var(--bg-glass); color: var(--text-primary); border: 1px solid var(--border-card); border-radius: var(--radius-sm); padding: 6px 12px; cursor: pointer; }
    .tabs { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 22px; }
    .tabs a, .tabs span { font-family: var(--font-mono); font-size: 0.78rem; letter-spacing: 0.06em; text-transform: uppercase; text-decoration: none; padding: 6px 14px; border-radius: 999px; border: 1px solid var(--border-card); color: var(--text-secondary); }
    .tabs a:hover { border-color: var(--accent); color: var(--accent); }
    .tabs [aria-current="page"] { border-color: var(--accent); color: var(--accent); background: color-mix(in srgb, var(--accent) 12%, transparent); font-weight: 600; }
    h1 { font-family: var(--font-display); font-weight: 400; font-size: clamp(1.8rem, 5vw, 2.4rem); line-height: 1.15; margin: 0 0 6px; }
    .lead { color: var(--text-secondary); margin: 0 0 24px; }
    h2 { font-family: var(--font-display); font-weight: 400; font-size: 1.45rem; letter-spacing: 0.01em; margin: 34px 0 10px; padding-bottom: 6px; border-bottom: 2px solid var(--accent); }
    h3 { font-family: var(--font-mono); font-weight: 600; font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin: 16px 0 4px; }
    ul { list-style: none; margin: 0; padding: 0; }
    li { padding: 6px 0; border-bottom: 1px solid var(--border-subtle); display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }
    li a { color: var(--text-primary); text-decoration: none; word-break: break-word; }
    li a:hover { color: var(--accent); text-decoration: underline; }
    .size { color: var(--text-muted); font-family: var(--font-mono); font-size: 0.75rem; white-space: nowrap; }
    .jump { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 8px; }
    .jump a { font-family: var(--font-mono); font-size: 0.78rem; color: var(--accent); text-decoration: none; padding: 4px 10px; border-radius: 999px; border: 1px solid color-mix(in srgb, var(--accent) 40%, transparent); }
    .jump a:hover { background: color-mix(in srgb, var(--accent) 10%, transparent); }
    .count { font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted); margin-left: 8px; letter-spacing: 0.04em; }
    .year { display: grid; grid-template-columns: 5.2rem 1fr; gap: 4px 16px; padding: 10px 0; border-bottom: 1px solid var(--border-subtle); }
    .year-label { font-family: var(--font-display); font-size: 1.3rem; line-height: 1.5; color: var(--accent); }
    .year ul li { border-bottom: 0; padding: 2px 0; }
    .year ul li a .tag { font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); letter-spacing: 0.04em; margin-left: 6px; }
    .note { margin-top: 36px; padding: 12px 16px; background: var(--bg-glass); border: 1px solid var(--border-card); border-radius: var(--radius-md); color: var(--text-secondary); font-size: 0.95rem; }
    @media (max-width: 520px) {
      .year { grid-template-columns: 1fr; }
      .year-label { font-size: 1.15rem; }
    }
"""


def _size(n: int) -> str:
    return f"{n / 1024 / 1024:.1f} MB" if n >= 1024 * 1024 else f"{max(1, round(n / 1024))} KB"


def _link(item: dict, label_html: str) -> str:
    href = "../../../" + item["href"]
    return (f'<li><a href="{html.escape(href, quote=True)}">{label_html}</a>'
            f'<span class="size">{_size(item["bytes"])}</span></li>')


# --------------------------------------------------------------------------- exam classification
EXAM_KINDS = {
    "FIRSTPARTIAL": ("first", "First partial"),
    "SECONDPARTIAL": ("second", "Second partial"),
    "THIRDPARTIAL": ("third", "Third partial"),
    "FINALEXAM": ("final", "Final exam"),
    # Exams of the same subject from other universities or degrees, listed apart from UC3M's:
    # SUBJECT_OTHERUNI_YEAR_INSTITUTION[_DETAILS].pdf, e.g. FLUIDS_OTHERUNI_2025_SEVILLA_EXTRA_P2.pdf
    "OTHERUNI": ("other", "Other universities and degrees"),
}
EXAM_ORDER = ("first", "second", "third", "final", "other")
EXAM_TITLE = {v[0]: v[1] for v in EXAM_KINDS.values()}
EXAM_SECTION = {k: (t if k == "other" else t + "s") for k, t in EXAM_TITLE.items()}

_CALLS = {"ORD": (1, "Ordinary call"), "EXTRA": (2, "Extraordinary call"), "RETAKE": (3, "Retake"),
          "PRACTICE": (4, "Practice exam"), "QUIZ": (5, "Quiz")}
_FLAGS = {"HANDWRITTEN": "handwritten", "HIGHLIGHTED": "highlighted"}


def classify_exam(name: str) -> dict | None:
    """Kind, year and a readable label for an exam file name, or None if it is not an exam."""
    stem = re.sub(r"\.pdf$", "", unquote(name), flags=re.I)
    legacy = re.match(r"(?:1st\s*Partial|First\s*Partial)\s*(.*)$", stem, re.I)
    if legacy:                                                  # e.g. 1stPartial2022, 1stPartialTipoTestsVariados
        rest = legacy.group(1)
        year = re.search(r"(20\d\d)", rest)
        extra = "Assorted test questions" if re.search(r"test", rest, re.I) else ""
        return {"kind": "first", "year": int(year.group(1)) if year else None, "year_label": year.group(1) if year else "Undated",
                "label": "Exam" + (f" · {extra}" if extra else ""), "sort": (0, extra, False, 0, stem)}
    parts = stem.split("_")
    if len(parts) < 3 or parts[1] not in EXAM_KINDS:
        return None
    kind = EXAM_KINDS[parts[1]][0]
    tokens = parts[2:]
    year, year_label, compilation = None, "Undated", False
    if tokens and tokens[0] == "COMPILATION":
        compilation, tokens = True, tokens[1:]
    if tokens and re.fullmatch(r"\d{4}(-\d{4})?", tokens[0]):
        year_label = tokens[0].replace("-", "–")
        year = int(tokens[0][-4:])
        tokens = tokens[1:]
    elif tokens and tokens[0] == "UNDATED":
        tokens = tokens[1:]
    call_rank, bits, doc, flags, problem, rest = 0, [], "Exam", [], 0, []
    if compilation:
        bits.append("Compilation")
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t in _CALLS:
            call_rank = _CALLS[t][0]; bits.append(_CALLS[t][1])
        elif re.fullmatch(r"[ABC]", t):
            bits.append(f"Model {t}")
        elif re.fullmatch(r"G\d+", t):
            bits.append(f"Group {t[1:]}")
        elif re.fullmatch(r"MT\d", t):
            bits.append(f"Midterm {t[2:]}")
        elif re.fullmatch(r"V\d", t):
            bits.append(f"Version {t[1:]}")
        elif t == "SOL":
            doc = "Solutions"
        elif re.fullmatch(r"P\d", t):
            problem = int(t[1:])
        elif t == "PROBLEMS":
            bits.append("Problems part")
        elif t == "EXERCISE":
            bits.append("Exercise")
        elif t in _FLAGS:
            flags.append(_FLAGS[t])
        else:
            rest.append(t.capitalize())
        i += 1
    bits += [r for r in rest if r]
    label = doc + (f", problem {problem}" if problem else "") + (f" ({', '.join(flags)})" if flags else "")
    if bits:
        label = " · ".join(bits) + " · " + label
    return {"kind": kind, "year": year, "year_label": year_label, "label": label,
            "sort": (call_rank, " ".join(bits), doc != "Exam", problem, stem)}


_STANDARD = re.compile(r"^[A-Z]+_(?:FIRSTPARTIAL|SECONDPARTIAL|THIRDPARTIAL|FINALEXAM|OTHERUNI)_")


def _digest(root: pathlib.Path, item: dict) -> str:
    try:
        return hashlib.sha1((root / unquote(item["href"])).read_bytes()).hexdigest()
    except OSError:
        return item["href"]


def exam_entries(root: pathlib.Path, data: dict) -> list[dict]:
    """Every exam file of a subject, classified, with byte-identical copies listed once."""
    items = list(data.get("general", {}).get("examenes", []))
    for unit in data["units"]:
        items += unit.get("examenes", [])
    seen = {}
    for item in sorted(items, key=lambda x: x["name"]):
        info = classify_exam(item["name"]) or {"kind": "final", "year": None, "year_label": "Undated",
                                               "label": unquote(item["name"]), "sort": (9, "", False, 0, item["name"])}
        key = _digest(root, item)
        standard = bool(_STANDARD.match(item["name"]))
        if key in seen:                                   # a byte-identical copy: list it once
            keep, other = (seen[key], dict(item=item, standard=standard, **info))
            if standard and not keep["standard"]:
                keep, other = other, keep                 # prefer the standard name
            if keep["year"] is None and other["year"] is not None:
                keep.update(year=other["year"], year_label=other["year_label"])   # and a known year
            seen[key] = keep
            continue
        seen[key] = {"item": item, "standard": standard, **info}
    return list(seen.values())


def render_exams(slug: str, entries: list[dict]) -> str:
    name, accent = SUBJECTS[slug]
    sections, jumps = [], []
    for kind in EXAM_ORDER:
        group = [e for e in entries if e["kind"] == kind]
        if not group:
            continue
        years = sorted({(e["year"] or 0, e["year_label"]) for e in group}, key=lambda y: (-y[0], y[1]))
        rows = []
        for y, ylabel in years:
            files = sorted((e for e in group if (e["year"] or 0) == y and e["year_label"] == ylabel), key=lambda e: e["sort"])
            lis = "\n".join(_link(e["item"], html.escape(e["label"])) for e in files)
            rows.append(f'<div class="year"><div class="year-label">{html.escape(ylabel)}</div>\n<ul>\n{lis}\n</ul></div>')
        title = EXAM_SECTION[kind]
        sections.append(f'<h2 id="{kind}">{title}<span class="count">{len(group)} files</span></h2>\n' + "\n".join(rows))
        jumps.append(f'<a href="#{kind}">{EXAM_SECTION[kind]}</a>')
    body = '<nav class="jump" aria-label="Exams">' + "".join(jumps) + "</nav>\n" + "\n".join(sections)
    lead = (f"{len(entries)} past exams and solutions, grouped by exam and sorted by year, newest first. "
            "Ordinary and extraordinary calls are listed together under each year.")
    return _page(slug, "exams", f"{name}: Exams", f"{name} - Exams",
                 f"Past partial and final exams of {name} (UC3M), sorted by year.", lead, body,
                 "These are the exams as published by the lecturers at Universidad Carlos III de Madrid. "
                 "They are linked here for personal study.", accent, has_exams=True)


# --------------------------------------------------------------------------- theory & exercises
def _group(title: str, bucket: dict) -> str:
    kinds = [k for k in KIND_ORDER if bucket.get(k)]
    if not kinds:
        return ""
    out = [f"<h2>{html.escape(title)}</h2>"]
    for kind in kinds:
        out.append(f"<h3>{KIND_LABEL[kind]}</h3>\n<ul>")
        for item in bucket[kind]:
            out.append(_link(item, html.escape(item["name"])))
        out.append("</ul>")
    return "\n".join(out)


def material_count(data: dict) -> int:
    general = data.get("general", {})
    return sum(len(general.get(k, [])) for k in KIND_ORDER) + \
        sum(len(unit.get(k, [])) for unit in data["units"] for k in KIND_ORDER)


def render_material(slug: str, data: dict, has_exams: bool) -> str:
    name, accent = SUBJECTS[slug]
    sections = [_group("Course-wide material", data.get("general", {}))]
    for unit in data["units"]:
        sections.append(_group(f"Unit {unit['number']}: {unit['title']}", unit))
    body = "\n".join(s for s in sections if s)
    count = material_count(data)
    lead = f"{count} original PDFs from the course (theory, slides and problem sheets), grouped by unit."
    return _page(slug, "sources", f"{name}: Theory &amp; Exercise PDFs", f"{name} - Theory & Exercise PDFs",
                 f"Original course PDFs for {name} (UC3M): theory, slides and problem sheets.", lead, body,
                 "These are the course documents as published by the lecturers at Universidad Carlos III de Madrid. "
                 "They are linked here for personal study; the notes and solutions elsewhere in this portal are "
                 "written independently from them.", accent, has_exams)


def _page(slug, current, h1, title, description, lead, body, note, accent, has_exams) -> str:
    tabs = []
    for key, label, href in (("sources", "Theory &amp; Exercise PDFs", "../sources/index.html"),
                             ("exams", "Exams", "../exams/index.html")):
        if key == "exams" and not has_exams:
            continue
        if key == current:
            tabs.append(f'<span aria-current="page">{label}</span>')
        else:
            tabs.append(f'<a href="{href}">{label}</a>')
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  {FONTS}
  <script src="../../../assets/js/theme.js"></script>
  <link rel="stylesheet" href="../../../assets/css/tokens.css">
  <link rel="stylesheet" href="../../../assets/css/study-surface.css">
  <style>
    :root {{ --accent: var({accent}); }}{CSS}  </style>
</head>
<body>
  <div class="wrap">
    <div class="top">
      <a class="back" href="../../../index.html">&larr; Study Portal</a>
      <div class="top-actions"><button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">Theme</button></div>
    </div>
    <nav class="tabs" aria-label="PDF pages">{"".join(tabs)}</nav>
    <h1>{h1}</h1>
    <p class="lead">{html.escape(lead)}</p>
{body}
    <p class="note">{html.escape(note)}</p>
  </div>
</body>
</html>
"""


# --------------------------------------------------------------------------- driver
def counts(root: pathlib.Path = REPO) -> dict[str, tuple[int, int]]:
    """(theory & exercise PDFs, exam files) per subject, as the index badges must show them."""
    manifest = build_manifest(root)
    return {slug: (material_count(d), len(exam_entries(root, d))) for slug, d in manifest["subjects"].items()}


def build(root: pathlib.Path = REPO) -> dict[pathlib.Path, str]:
    manifest = build_manifest(root)
    pages = {}
    for slug in SUBJECTS:
        if slug not in manifest["subjects"]:
            continue
        data = manifest["subjects"][slug]
        exams = exam_entries(root, data)
        pages[pathlib.Path(root, "subjects", slug, "sources", "index.html")] = render_material(slug, data, bool(exams))
        if exams:
            pages[pathlib.Path(root, "subjects", slug, "exams", "index.html")] = render_exams(slug, exams)
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
