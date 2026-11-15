---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_sources_pages.py"
---

# Tool - build_sources_pages

## Purpose

Generates two pages per subject from the scan of `sources/cuatrimestre-1/`. The first is `subjects/<slug>/sources/index.html`, the PDF library ("PDFs"): theory, slides, problem sheets and schedules grouped by unit, followed by the exams by partial or final, newest year first, with a search box and filters (type, unit, exam, year) added by `assets/js/pdf-library.js`. The second is `subjects/<slug>/exams/index.html`, a "Coming soon" placeholder for the solved exams that links to the exam PDFs of the library. Exam files are classified from their names, `SUBJECT_KIND_YEAR[_DETAILS].pdf`, where KIND is `FIRSTPARTIAL`, `SECONDPARTIAL`, `THIRDPARTIAL`, `FINALEXAM` or `OTHERUNI`. Byte-identical copies are listed once.

## Command

`python tools/build_sources_pages.py [--check]`

## Read and write behaviour

It reads `sources/cuatrimestre-1/` through `build_manifest` in `tools/sources_manifest.py`, not through `assets/data/sources.js`. Without `--check`, it writes the pages and creates their folders. With `--check`, it is read-only and exits 1 if any page is stale. Its `counts()` function is also used by [[Tool - audit_portal]].

## When to run

- After adding, renaming or removing a PDF under `sources/`.
- Gate: run with `--check`. These pages are never edited by hand (see [[Rules - AGENTS.md]]).

## Related

[[Repository MOC]] · [[Tool - sources_manifest]] · [[Tool - audit_portal]] · [[Tool - Test suite]]
