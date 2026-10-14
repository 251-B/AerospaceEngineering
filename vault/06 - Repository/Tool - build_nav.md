---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_nav.py"
---

# Tool - build_nav

## Purpose

Regenerates `assets/data/nav.js`, the tree that the side menu reads (`window.AE_NAV = {...}`). The short labels are written by hand in `tools/nav.json`; the script checks them against the pages in `subjects/<slug>/teoria/` and `problemas/` and adds the index page of each area, `sources/index.html` and `exams/index.html` when they exist. `assets/js/sidebar.js` builds the drawer from the result, so no page carries the tree. Laboratory material is never listed.

## Command

`python tools/build_nav.py [--root DIR] [--check]`

## Read and write behaviour

It reads `tools/nav.json` and lists the pages on disk. Without `--check`, it writes `assets/data/nav.js` and prints the page count. With `--check`, it is read-only and exits 1 if the file is stale, or if `nav.json` lists a page that does not exist, omits a page that does, or omits a subject folder. The output is generated, so it is never edited by hand.

## When to run

- After adding, renaming or removing a theory or problem page: add or change its entry in `tools/nav.json` first.
- Gate: run with `--check`.
- Adding a page changes only `nav.js`, not the other pages, so no PDF is reprinted for it.

## Related

[[Repository MOC]] · [[Tool - sources_manifest]] · [[Tool - Test suite]] · [[Rules - AGENTS.md]]
