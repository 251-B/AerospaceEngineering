---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_problem_pages.py"
---

# Tool - build_problem_pages

## Purpose

Generates the two Business Management Topic 3 problem pages in `subjects/business-management/problemas/` from notes in `vault/05 - Business Management/`. The financial statements page holds Exercises 1 to 6. The extra exam problems page holds Problems 1 to 4 and is preceded by the method note. In each note, the first section becomes the statement box and later sections become phase blocks. The tool adds its shared CSS block to the page head when that block is missing.

## Command

`python tools/build_problem_pages.py [--check]`

## Read and write behaviour

It reads the vault notes and the current pages, keeping their existing head and footer. Without `--check`, it rewrites a page only when the generated version differs. With `--check`, it is read-only and exits 1 if a page no longer matches its notes. PDF deep links are not applied here, so the comparison strips them first. It reuses helper functions from [[Tool - build_topic_pages]] and [[Tool - source_links]].

## When to run

- After editing a Business Management Topic 3 problem note. The note is edited, never the page.
- Order: after build_topic_pages and before source_links and build_pdfs (see [[Rules - AGENTS.md]]).

## Related

[[Repository MOC]] · [[Agent - problem-step-mentor]] · [[Tool - build_topic_pages]] · [[Tool - build_pdfs]] · [[Tool - Test suite]]
