#!/usr/bin/env python3
"""Splice sections 7 and 8 of subjects/advanced-maths/teoria/topic-4.html.

The text lives in tools/am_phase/sections_7_8.html (tokens {{fig:NAME}}), the
phase portraits in tools/figures/am_phase.py.  The block between the markers
AM-PHASE:START and AM-PHASE:END of the page is generated: edit the template or
the figure module, never the block.  Figures used elsewhere on the page (section 6)
sit between <!-- AM-FIG:NAME --> and <!-- /AM-FIG --> and are refilled from the
same module.  `--check` fails if the page is stale.

    python tools/am_phase_build.py            # rewrite the block
    python tools/am_phase_build.py --check    # exit 1 if the page differs

Run order after a change: am_phase_build.py, then source_links.py (which adds the
PDF deep links to the citations in the block), then build_pdfs.py.  `--check`
ignores the deep links that source_links.py adds.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "figures"))
import am_phase  # noqa: E402

PAGE = ROOT / "subjects" / "advanced-maths" / "teoria" / "topic-4.html"
TEMPLATE = ROOT / "tools" / "am_phase" / "sections_7_8.html"
START, END = "<!-- AM-PHASE:START -->", "<!-- AM-PHASE:END -->"
OLD7 = "    <!-- ===================================================== 7 -->"
OLD9 = "    <!-- ===================================================== 9 -->"


def render():
    text = TEMPLATE.read_text(encoding="utf-8")
    figs = am_phase.FIGURES

    def sub(m):
        return "      " + figs[m.group(1)]

    out = re.sub(r"[ \t]*\{\{fig:(\w+)\}\}", sub, text)
    if "{{" in out:
        raise SystemExit("unresolved figure token in template")
    return out.rstrip("\n") + "\n"


def splice(page, block):
    if START in page:
        a, b = page.index(START), page.index(END)
        return page[:a] + START + "\n" + block + "    " + page[b:]
    a, b = page.index(OLD7), page.index(OLD9)
    return page[:a] + "    " + START + "\n" + block + "    " + END + "\n\n" + page[b:]


FIG_BLOCK = re.compile(r"<!-- AM-FIG:(\w+) -->.*?<!-- /AM-FIG -->", re.S)


def fill_figures(page):
    """Single figures used outside sections 7-8 (section 6): <!-- AM-FIG:name --> ... <!-- /AM-FIG -->."""
    figs = am_phase.FIGURES

    def sub(m):
        return f"<!-- AM-FIG:{m.group(1)} -->{figs[m.group(1)]}<!-- /AM-FIG -->"

    return FIG_BLOCK.sub(sub, page)


SRC_LINK = re.compile(r'<a class="src-cite" data-srclink[^>]*>(.*?)</a>', re.S)


def _plain(html):
    """The page without the deep links added by tools/source_links.py."""
    return SRC_LINK.sub(lambda m: m.group(1), html)


def main():
    page = PAGE.read_text(encoding="utf-8")
    new = fill_figures(splice(page, render()))
    if "--check" in sys.argv:
        if _plain(new) != _plain(page):
            print("topic-4.html is stale: run python tools/am_phase_build.py")
            return 1
        print("topic-4.html sections 7-8 are up to date")
        return 0
    PAGE.write_text(new, encoding="utf-8", newline="\n")
    print("wrote", PAGE.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
