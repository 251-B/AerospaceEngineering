---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/source_links.py"
---

# Tool - source_links

## Purpose

Adds deep links from the study pages to the official PDFs in `sources/`. It inserts three kinds of link: an "Official material" strip in the page header (panel), an "Original statement" link in each problem card (card), and inline citations such as "[Slide 14]" or "Eq. 2.26" (cite). Every inserted element carries `data-srclink`, so a re-run removes and rebuilds only its own links.

## Command

`python tools/source_links.py [--check] [--refresh-anchors] [-v]`

## Inputs and outputs

- Reads `tools/source_links.json` (35 configured pages and the PDF registry) and `tools/source_anchors.json` (resolved equation and section labels).
- Without `--check`, rewrites each configured page under `subjects/` whose links are out of date.
- `--refresh-anchors` re-reads labels from the PDFs with `pdftotext` (poppler), rewrites `tools/source_anchors.json`, and updates the pages in the same run.
- Applying the links needs no external tool. Only `--refresh-anchors` needs `pdftotext`.
- `-v` lists citations that could not be resolved.

## Exit codes

Exit 1 when a configured PDF is missing, when a page is stale under `--check`, or when a problem card has no PDF page configured.

## When to run

- After editing a configured page or a problem card. New pages or cards are added to `tools/source_links.json` first.
- Citations inside `$...$` are never linked, so citations stay outside math.
- Gate: run with `--check`.

## Related

[[Repository MOC]] · [[Tool - build_topic_pages]] · [[Tool - build_problem_pages]] · [[Tool - audit_portal]] · [[Agent - source-researcher]]
