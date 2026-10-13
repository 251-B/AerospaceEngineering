---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_pdfs.py"
---

# Tool - build_pdfs

## Purpose

Prints every theory and problem page to A4 PDF for the "Download PDF" and "Open as PDF" buttons. The whole page goes to `assets/pdf/<slug>/<area>/<page>.pdf`. Each problem card goes to `assets/pdf/<slug>/<area>/<page>/<card id>.pdf`. It uses headless Edge or Chrome, found through [[Tool - render_check]], and the print layout in `assets/css/print.css`.

## Command

`python tools/build_pdfs.py [--check] [--only TEXT] [--force] [--katex DIR] [--jobs N] [--root DIR]`

## Read and write behaviour

- `--check`: read-only and needs no browser. Exits 1 if a PDF is missing, stale or orphaned.
- Without `--check`: prints the stale or new PDFs with the browser, deletes orphan PDFs, and rewrites `assets/pdf/manifest.json`. Orphan removal is not limited by `--only`. Exits 2 if no browser is found and 1 if a print fails.
- Each hash covers the page plus `assets/css/print.css` and `assets/js/pdf-export.js`.
- `--katex DIR` loads KaTeX from a local folder through a temporary copy of the pages. The page sources are not changed, but the PDFs and the manifest are still written to the repository.

## When to run

- After editing any theory or problem page, `assets/css/print.css` or `assets/js/pdf-export.js`.
- Gate: `--check` must pass. `assets/pdf/` is never edited by hand. Where the CDN is blocked, print with `--katex` (see [[Rules - AGENTS.md]]).

## Related

[[Repository MOC]] · [[Tool - build_topic_pages]] · [[Tool - build_problem_pages]] · [[Tool - source_links]] · [[Tool - Test suite]]
