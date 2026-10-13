#!/usr/bin/env python3
"""Build the Business Management Topic 3 problem pages in subjects/ from their vault notes.

Two pages are generated, each from several notes in vault/05 - Business Management/:

    subjects/business-management/problemas/topic-3-financial-statements.html
        Problem - T3 Exercise 1..6 (T3_Financial Statements_EXERCISES.pdf)
    subjects/business-management/problemas/topic-3-extra-exam-problems.html
        Problem - T3 Extra 1..4 (T3_Additional_EXERCISES.pdf), preceded by the full text of
        "Concept - Method to Build the Income Statement and Balance Sheet"

Per note: the first "## " section is the statement (box `.statement-box`), every later "## " section
becomes a phase block (`.phase-title`), "### " headings become step titles, and Obsidian callouts
(> [!info] / > [!warning]) become callouts. The page keeps its own <head>, header and footer; only the
part between the article header and the topic navigation is rewritten. The PDF deep links of
tools/source_links.py are NOT applied here (run that tool afterwards), so `--check` compares the page
with its links stripped.

Usage:
    python tools/build_problem_pages.py            # rewrite both pages
    python tools/build_problem_pages.py --check    # exit 1 if a page no longer matches its notes
"""
import argparse
import html
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import build_topic_pages as bt  # noqa: E402
import source_links as sl  # noqa: E402

VAULT = REPO / "vault" / "05 - Business Management"
METHOD_NOTE = "Concept - Method to Build the Income Statement and Balance Sheet"
EXTRA_PAGE = "subjects/business-management/problemas/topic-3-extra-exam-problems.html"
STD_PAGE = "subjects/business-management/problemas/topic-3-financial-statements.html"

PAGES = {
    STD_PAGE: (False, [
        ("Problem - T3 Exercise 1 - Accrual vs Cash Basis and Linear Depreciation", "exercise-1", "Exercise 1"),
        ("Problem - T3 Exercise 2 - JUGA SA Opening Balance Sheet", "exercise-2", "Exercise 2"),
        ("Problem - T3 Exercise 3 - Libbys Company Balance Sheet Classification", "exercise-3", "Exercise 3"),
        ("Problem - T3 Exercise 4 - Hawkins Partners Income Statement and Inventories", "exercise-4", "Exercise 4"),
        ("Problem - T3 Exercise 5 - Corporate Income Statement, Taxes and Dividends", "exercise-5", "Exercise 5"),
        ("Problem - T3 Exercise 6 - Company X Full Cycle Balance Sheet and Uncalled Capital", "exercise-6", "Exercise 6"),
    ]),
    EXTRA_PAGE: (True, [
        ("Problem - T3 Extra 1 - Circonsa Balance Sheet and Income Statement", "problem-1", "Additional Exercise 1 · Exam type"),
        ("Problem - T3 Extra 2 - Infopymes Full Cycle Financial Statements and ROA ROE", "problem-2", "Additional Exercise 2 · Exam type"),
        ("Problem - T3 Extra 3 - Wifinet Internet Provider Accounting Cycle and Dividends", "problem-3", "Additional Exercise 3 · Exam type"),
        ("Problem - T3 Extra 4 - Cemed Mediterranean Pottery Manufacturing and Supplier Discount", "problem-4", "Additional Exercise 4 · Exam type"),
    ]),
}

CSS = """
    /* Phase blocks rendered from the vault notes */
    .phase-block { margin: 28px 0 8px; }
    .phase-block h4.step-title { font-size: 1.05rem; color: var(--text-heading); margin: 22px 0 10px; font-family: var(--font-serif, Georgia, serif) !important; font-weight: 700 !important; }
    .phase-block .table-container, .method-box .table-container { overflow-x: auto; margin: 16px 0; }
    .phase-block td, .phase-block th, .method-box td, .method-box th { vertical-align: top; }
    .math-block { overflow-x: auto; margin: 16px 0; }
    .callout { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-left: 4px solid var(--accent); border-radius: 8px; padding: 14px 18px; margin: 18px 0; }
    .callout-title { font-weight: 700; color: var(--text-heading); margin-bottom: 6px; }
    .callout-warning { border-left-color: #f59e0b; }
    .method-box { border: 1px solid var(--border-subtle); border-radius: 12px; padding: 8px 24px 16px; margin: 8px 0 40px; background: var(--bg-surface); }
    .method-box h3 { margin-top: 22px; }
  </style>"""


def read_note(name):
    return bt.strip_frontmatter((VAULT / f"{name}.md").read_text(encoding="utf-8"))


def sections(md):
    """(title, markdown) for every '## ' section of the note body (up to the closing 'Back to' line)."""
    body = md[md.index("\n## "):md.index("**Back to:**")]
    out = []
    for s in re.split(r"\n## ", body)[1:]:
        title, _, rest = s.partition("\n")
        out.append((title.strip(), rest))
    return out


def render(md):
    """Markdown (no '## ' headings) to HTML; '### ' becomes a step title."""
    out, chunk = [], []
    for line in md.split("\n"):
        m = re.match(r"### (.*)", line)
        if m:
            out.append(bt.blocks(chunk))
            chunk = []
            out.append(f'<h4 class="step-title">{bt.inline(m.group(1))}</h4>')
        elif line.strip() == "---":
            continue
        else:
            chunk.append(line)
    out.append(bt.blocks(chunk))
    return "\n".join(x for x in out if x)


def card(note, card_id, tag):
    md = read_note(note)
    title = re.search(r"^# ✏️ Problem: (.*)$", md, re.M).group(1)
    parts = sections(md)
    statement = render(parts[0][1])
    phases = "\n".join(
        f'        <div class="phase-block">\n          <h3 class="phase-title">{bt.inline(t)}</h3>\n{render(b)}\n        </div>'
        for t, b in parts[1:])
    return f'''      <section class="problem-box" id="{card_id}">
        <span class="problem-tag">{html.escape(tag)}</span>
        <h2 class="problem-title">{bt.inline(title)}</h2>
        <div class="statement-box">
{statement}
        </div>
{phases}
      </section>
'''


def method_section(full):
    md = read_note(METHOD_NOTE)
    idea = re.search(r"^> (.*)$", md, re.M).group(1)
    if not full:
        return f'''      <section class="method-box" id="method">
        <h2>Method used in every solution</h2>
        <div class="callout"><p>{bt.inline(idea)}</p></div>
        <p>The full step-by-step method (classification table, depreciation and interest rules, cash account and balance-sheet layout) is at the top of the <a href="topic-3-extra-exam-problems.html#method">exam-type problems page</a>. Each solution below follows the same four phases: setup, frames (period and classification of every operation), derivation, interpretation.</p>
      </section>
'''
    inner = "\n".join(f"        <h3>{bt.inline(t)}</h3>\n{render(b)}" for t, b in sections(md))
    return f'''      <section class="method-box" id="method">
        <h2>Method: building the income statement and the balance sheet</h2>
        <div class="callout"><p>{bt.inline(idea)}</p></div>
{inner}
      </section>
'''


def build_page(rel):
    """The page as it must be (without PDF deep links), starting from its current head and footer."""
    full, cards = PAGES[rel]
    text = sl.strip_links((REPO / rel).read_text(encoding="utf-8"))
    if "phase-block {" not in text:
        text = text.replace("  </style>", CSS, 1)
    start = text.index('<header class="article-header">')
    start = text.index("      </header>\n", start) + len("      </header>\n")
    end = text.index('      <footer class="topic-nav">')
    middle = "\n" + method_section(full) + "\n" + "\n".join(card(*c) for c in cards) + "\n"
    return text[:start] + middle + text[end:]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if a page no longer matches its vault notes")
    args = ap.parse_args(argv)
    stale = []
    for rel in PAGES:
        path = REPO / rel
        want = build_page(rel)
        have = sl.strip_links(path.read_text(encoding="utf-8"))
        if have == want:
            continue
        stale.append(rel)
        if not args.check:
            path.write_text(want, encoding="utf-8", newline="\n")
            print(f"build_problem_pages: wrote {rel}")
    if args.check:
        for rel in stale:
            print(f"build_problem_pages: stale {rel} (run python tools/build_problem_pages.py)", file=sys.stderr)
        return 1 if stale else 0
    print(f"build_problem_pages: {len(PAGES)} page(s) checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
