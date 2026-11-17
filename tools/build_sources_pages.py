#!/usr/bin/env python3
"""Generate the PDF library and the solved-exams placeholder of each subject from the scan behind
assets/data/sources.js:

    subjects/<slug>/sources/index.html   "PDFs": every official PDF of the subject on one page:
                                         theory, slides, problem sheets and schedule grouped by unit,
                                         then the past exams grouped by exam (first, second, third
                                         partial, final, other universities), newest year first.
                                         A search box and filters (type, unit; for exams, exam and
                                         year) are added by assets/js/pdf-library.js; without
                                         JavaScript the page lists everything.
    subjects/<slug>/exams/index.html     "Solved exams": a "Coming soon" placeholder that points at
                                         the exam PDFs of the library. It will hold the solved exams.

Both pages carry the subject's tab strip and header icon, copied from its teoria/index.html, and
are styled by assets/css/pdf-library.css. Every link points at a PDF that exists in
sources/cuatrimestre-1/. Laboratory material is never listed (sources_manifest excludes it). Exam
files are classified from their names, SUBJECT_KIND_YEAR[_DETAILS].pdf
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
import unicodedata
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
KIND_ONE = {"teoria": "Theory", "slides": "Slides", "problemas": "Problem sheet", "schedule": "Schedule", "other": "Other"}
KIND_ORDER = ("teoria", "slides", "problemas", "schedule", "other")

# Same families as the root index.html.
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=JetBrains+Mono:ital,wght@0,400;0,500;'
         '0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600;'
         '1,6..72,700&display=swap" rel="stylesheet">')


def _size(n: int) -> str:
    return f"{n / 1024 / 1024:.1f} MB" if n >= 1024 * 1024 else f"{max(1, round(n / 1024))} KB"


def _files(n: int) -> str:
    return f"{n} file" if n == 1 else f"{n} files"


def _fold(text: str) -> str:
    """Lower case without accents: what the search box of pdf-library.js matches against."""
    text = unicodedata.normalize("NFD", text.lower())
    return " ".join("".join(c for c in text if not unicodedata.combining(c)).split())


def _item(item: dict, name: str, meta: str, attrs: dict, search: str) -> str:
    href = "../../../" + item["href"]
    data = "".join(f' data-{k}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    return (f'<li class="lib-item"{data} data-name="{html.escape(_fold(search), quote=True)}">'
            f'<a href="{html.escape(href, quote=True)}"><span class="lib-name">{html.escape(name)}</span>'
            f'<span class="lib-meta">{html.escape(meta)}</span>'
            f'<span class="lib-size">{_size(item["bytes"])}</span></a></li>')


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


# --------------------------------------------------------------------------- the PDF library
def material_count(data: dict) -> int:
    general = data.get("general", {})
    return sum(len(general.get(k, [])) for k in KIND_ORDER) + \
        sum(len(unit.get(k, [])) for unit in data["units"] for k in KIND_ORDER)


def _material_group(title: str, unit_id: str, bucket: dict) -> str:
    rows = [_item(item, unquote(item["name"]), KIND_ONE[kind], {"kind": kind, "unit": unit_id},
                  f'{unquote(item["name"])} {KIND_LABEL[kind]} {title}')
            for kind in KIND_ORDER for item in bucket.get(kind, [])]
    if not rows:
        return ""
    return (f'    <section class="lib-group">\n      <h2>{html.escape(title)}<span class="count">{_files(len(rows))}</span></h2>\n'
            '      <ul class="lib-list">\n        ' + "\n        ".join(rows) + "\n      </ul>\n    </section>")


def _exam_group(kind: str, group: list[dict]) -> str:
    group = sorted(group, key=lambda e: (-(e["year"] or 0), e["year_label"], e["sort"]))
    rows = [_item(e["item"], f'{e["year_label"]} · {e["label"]}', EXAM_TITLE[kind],
                  {"kind": "exam", "exam": kind, "year": e["year_label"]},
                  f'{e["year_label"]} {e["label"]} {EXAM_TITLE[kind]} exam {unquote(e["item"]["name"])}')
            for e in group]
    return (f'    <section class="lib-group" id="{kind}">\n      <h2>Exams · {EXAM_SECTION[kind]}'
            f'<span class="count">{_files(len(rows))}</span></h2>\n'
            '      <ul class="lib-list">\n        ' + "\n        ".join(rows) + "\n      </ul>\n    </section>")


def _chip(name: str, value: str, label: str, n: int | None = None, pressed: bool = False) -> str:
    count = f'<span class="n">{n}</span>' if n is not None else ""
    return (f'<button type="button" class="lib-chip" data-filter="{name}" data-value="{value}" '
            f'aria-pressed="{"true" if pressed else "false"}">{html.escape(label)}{count}</button>')


def _tools(data: dict, exams: list[dict], total: int) -> str:
    general = data.get("general", {})
    per_kind = {k: len(general.get(k, [])) + sum(len(u.get(k, [])) for u in data["units"]) for k in KIND_ORDER}
    kinds = [_chip("kind", "all", "All", total, True)]
    kinds += [_chip("kind", k, KIND_LABEL[k], per_kind[k]) for k in KIND_ORDER if per_kind[k]]
    if exams:
        kinds.append(_chip("kind", "exam", "Exams", len(exams)))
    units = ['<option value="all">All units</option>']
    if any(general.get(k) for k in KIND_ORDER):
        units.append('<option value="general">Course-wide material</option>')
    units += [f'<option value="{u["number"]}">Unit {u["number"]}: {html.escape(u["title"])}</option>'
              for u in data["units"] if any(u.get(k) for k in KIND_ORDER)]
    out = ['    <section class="lib-tools" id="libTools" aria-label="Search and filters" hidden>',
           '      <label class="lib-search"><input type="search" id="libSearch" placeholder="Search by file name, unit or year" '
           'aria-label="Search the PDFs" autocomplete="off"></label>',
           '      <div class="lib-row" role="group" aria-label="Type"><span class="lib-label">Type</span>' + "".join(kinds) + "</div>",
           '      <div class="lib-row" data-only="material"><label class="lib-label" for="libUnit">Unit</label>'
           '<select class="lib-select" id="libUnit" data-filter="unit">' + "".join(units) + "</select></div>"]
    if exams:
        present = [k for k in EXAM_ORDER if any(e["kind"] == k for e in exams)]
        parts = [_chip("exam", "all", "All", None, True)] + [_chip("exam", k, EXAM_TITLE[k]) for k in present]
        years = sorted({(e["year"] or 0, e["year_label"]) for e in exams}, key=lambda y: (-y[0], y[1]))
        opts = '<option value="all">All years</option>' + "".join(
            f'<option value="{html.escape(label, quote=True)}">{html.escape(label)}</option>' for _, label in years)
        out += ['      <div class="lib-row" data-only="exam" role="group" aria-label="Exam" hidden><span class="lib-label">Exam</span>'
                + "".join(parts) + "</div>",
                '      <div class="lib-row" data-only="exam" hidden><label class="lib-label" for="libYear">Year</label>'
                f'<select class="lib-select" id="libYear" data-filter="year">{opts}</select></div>']
    out += [f'      <div class="lib-status"><p class="lib-count" id="libCount" aria-live="polite">{total} files</p>'
            '<button type="button" class="lib-reset" id="libReset" hidden>Clear filters</button></div>',
            "    </section>"]
    return "\n".join(out)


def render_library(slug: str, data: dict, exams: list[dict], root: pathlib.Path = REPO) -> str:
    name, accent = SUBJECTS[slug]
    total = material_count(data) + len(exams)
    sections = [_material_group("Course-wide material", "general", data.get("general", {}))]
    for unit in data["units"]:
        sections.append(_material_group(f"Unit {unit['number']} · {unit['title']}", str(unit["number"]), unit))
    for kind in EXAM_ORDER:
        group = [e for e in exams if e["kind"] == kind]
        if group:
            sections.append(_exam_group(kind, group))
    body = "\n".join([_tools(data, exams, total)] + [s for s in sections if s] +
                     ['    <p class="lib-empty" id="libEmpty" hidden>No file matches these filters.</p>',
                      '    <p class="lib-note">These are the course documents and exams as published by the lecturers at '
                      "Universidad Carlos III de Madrid. They are linked here for personal study; the notes and solutions "
                      "elsewhere in this portal are written independently from them.</p>"])
    return _page(root, slug, "sources", f"{name} — PDFs", f"{name} - PDFs",
                 f"Official course PDFs for {name} (UC3M): theory, slides, problem sheets and past exams.", body, accent,
                 script=True)


def render_exams(slug: str, exams: list[dict], root: pathlib.Path = REPO) -> str:
    """The "Solved exams" placeholder. The exam PDFs themselves are listed in the PDF library."""
    name, accent = SUBJECTS[slug]
    if exams:
        text = (f"Past exams of {name} solved step by step will be published here. "
                f"Until then, the {len(exams)} exam papers and official solutions are in the PDF library.")
        link = '<a class="soon-link" href="../sources/index.html?type=exam">Open the exam PDFs</a>'
    else:
        text = (f"Past exams of {name} solved step by step will be published here. "
                "The course material is in the PDF library.")
        link = '<a class="soon-link" href="../sources/index.html">Open the PDF library</a>'
    body = ('    <section class="soon-card">\n      <p class="soon-badge">Coming soon</p>\n      <h2>Solved exams</h2>\n'
            f"      <p>{html.escape(text)}</p>\n      {link}\n    </section>")
    return _page(root, slug, "exams", f"{name} — Solved exams", f"{name} - Solved exams",
                 f"Solved past exams of {name} (UC3M): coming soon.", body, accent)


_TABS = re.compile(r'<nav class="subject-tabs"[^>]*>.*?</nav>', re.S)
_ICON = re.compile(r'<(?:div|span) class="(?:icon|page-header-icon)"[^>]*>\s*(<svg\b.*?</svg>)', re.S)
_FALLBACK_TABS = ('<nav class="subject-tabs" aria-label="{name} sections">\n'
                  '      <a class="subject-tab" href="../teoria/index.html">Theory</a>\n'
                  '      <a class="subject-tab" href="../problemas/index.html">Problems</a>\n'
                  '      <span class="subject-tab" aria-disabled="true">Extra problems <span class="subject-tab__soon">Soon</span></span>\n'
                  '      <span class="subject-tab" aria-disabled="true">Exam simulator <span class="subject-tab__soon">Soon</span></span>\n'
                  '      <a class="subject-tab" href="../sources/index.html">PDFs</a>\n'
                  "    </nav>")


def _chrome(root: pathlib.Path, slug: str, area: str) -> tuple[str, str]:
    """The tab strip and the header icon of the subject, copied from its theory index so the two
    generated pages match the hand-written ones. The PDFs tab is marked current on the library."""
    index = pathlib.Path(root, "subjects", slug, "teoria", "index.html")
    text = index.read_text(encoding="utf-8") if index.is_file() else ""
    tabs = _TABS.search(text)
    tabs = tabs.group(0) if tabs else _FALLBACK_TABS.format(name=html.escape(SUBJECTS[slug][0]))
    tabs = tabs.replace(' aria-current="page"', "")
    if area == "sources":
        tabs = tabs.replace('href="../sources/index.html"', 'href="../sources/index.html" aria-current="page"')
    icon = _ICON.search(text)
    return tabs, (icon.group(1) if icon else "")


_LIB_SEAL = (
    '<svg class="lib-seal" viewBox="96 96 832 832" width="20" height="20" aria-hidden="true" focusable="false">'
    '<path class="sideris-stroke" d="M 398.51,379.43 A 355,160 -14 0 1 652.50,634.24" fill="none" stroke-width="11" stroke-linecap="round" stroke-opacity="0.92"/>'
    '<path class="sideris-stroke" d="M 624.34,644.98 A 355,160 -14 0 1 370.40,390.21" fill="none" stroke-width="11" stroke-linecap="round" stroke-opacity="0.92"/>'
    '<polyline class="sideris-stroke" points="652,286 512,212 368,290 392,430 512,512 632,594 652,736 510,812 368,738" fill="none" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle class="sideris-fill" cx="652" cy="286" r="17"/><circle class="sideris-fill" cx="512" cy="212" r="20"/>'
    '<circle class="sideris-fill" cx="368" cy="290" r="16"/><circle class="sideris-fill" cx="392" cy="430" r="19"/>'
    '<circle class="sideris-fill" cx="632" cy="594" r="18"/><circle class="sideris-fill" cx="652" cy="736" r="20"/>'
    '<circle class="sideris-fill" cx="510" cy="812" r="18"/><circle class="sideris-fill" cx="368" cy="738" r="19"/>'
    '<path class="sideris-fill" d="M 512,464 Q 518.7,505.3 560,512 Q 518.7,518.7 512,560 Q 505.3,518.7 464,512 Q 505.3,505.3 512,464 Z"/>'
    '</svg>'
)


def _page(root, slug, area, h1, title, description, body, accent, script=False) -> str:
    tabs, icon = _chrome(root, slug, area)
    icon = f'\n      <div class="icon" aria-hidden="true">{icon}</div>' if icon else ""
    tail = '\n  <script defer src="../../../assets/js/pdf-library.js"></script>' if script else ""
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark" data-celestial-subject="{slug}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  {FONTS}
  <script src="../../../assets/js/theme.js"></script>
  <link rel="stylesheet" href="../../../assets/css/tokens.css">
  <link rel="stylesheet" href="../../../assets/css/study-surface.css">
  <link rel="stylesheet" href="../../../assets/css/subject-tabs.css">
  <link rel="stylesheet" href="../../../assets/css/pdf-library.css">
  <style>
    :root {{ --accent: var({accent}); --accent-soft: color-mix(in srgb, var({accent}) 12%, transparent); }}
  </style>
  <link rel="stylesheet" href="../../../assets/css/subject-index.css">
</head>
<body class="pdf-library">
  <header class="site-header">
    <div class="container header-inner">
      <div class="header-left">
        <a class="back-link" href="../../../index.html"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg><span>Main Portal</span></a>
      </div>
      <div class="header-right"><button class="theme-toggle" id="themeToggle" aria-label="Toggle theme"></button></div>
    </div>
  </header>

  <main class="container">
    {tabs}

    <header class="page-header">{icon}
      <h1>{html.escape(h1)}</h1>
    </header>

{body}
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">{_LIB_SEAL}<span>Aerospace Engineering Study Portal — Universidad Carlos III de Madrid</span></div>
  </footer>{tail}
</body>
</html>
"""


# --------------------------------------------------------------------------- driver
def counts(root: pathlib.Path = REPO) -> dict[str, tuple[int, int]]:
    """(files in the PDF library, of which exam files) per subject. The first number is the one the
    PDFs badge of the landing page must show: course material plus exams, each file once."""
    manifest = build_manifest(root)
    out = {}
    for slug, d in manifest["subjects"].items():
        exams = len(exam_entries(root, d))
        out[slug] = (material_count(d) + exams, exams)
    return out


def build(root: pathlib.Path = REPO) -> dict[pathlib.Path, str]:
    manifest = build_manifest(root)
    pages = {}
    for slug in SUBJECTS:
        if slug not in manifest["subjects"]:
            continue
        data = manifest["subjects"][slug]
        exams = exam_entries(root, data)
        pages[pathlib.Path(root, "subjects", slug, "sources", "index.html")] = render_library(slug, data, exams, root)
        pages[pathlib.Path(root, "subjects", slug, "exams", "index.html")] = render_exams(slug, exams, root)
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
