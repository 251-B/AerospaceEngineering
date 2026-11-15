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

## Lecture citations

`[Lecture N, Slide M]` (also `[Lecture N, Slides M-K]`, linked to M) becomes a link to page M of the deck of lecture N. The decks per subject are the `lectures` key of `tools/source_links.json` (Engineering Mechanics, Lectures 1 to 10, ids `em-s1` to `em-s10`); other subjects are unaffected. `Problems.pdf, p. N` is linked on pages whose `cite` rules name a `problems` PDF. Both work inside the `derivation-source` span of a derivation box. Where a deck has a `slide_map` (Lecture 1) the printed slide number is mapped to the PDF page.

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
