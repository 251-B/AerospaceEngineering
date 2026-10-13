---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/sources_manifest.py"
---

# Tool - sources_manifest

## Purpose

Regenerates `assets/data/sources.js`, the manifest of official PDFs that the portal reads (`window.AE_SOURCES = {...}`). It scans `sources/cuatrimestre-1/` by subject, unit and category (`teoria`, `slides`, `problemas`, `examenes`, `schedule`). Folders whose names start with `laborator` or `extracted` are excluded, so laboratory material never reaches the web.

## Command

`python tools/sources_manifest.py [--root DIR] [--check]`

## Read and write behaviour

It reads `sources/cuatrimestre-1/`. Without `--check`, it writes `assets/data/sources.js` and prints the PDF count. With `--check`, it is read-only and exits 1 if the file is stale. The output is generated, so it is never edited by hand.

## When to run

- After adding, moving or removing PDFs under `sources/`.
- Gate: run with `--check`.
- The exam and sources index pages do not read this file. [[Tool - build_sources_pages]] calls the same scan directly.

## Related

[[Repository MOC]] · [[Tool - build_sources_pages]] · [[Tool - Test suite]] · [[Rules - AGENTS.md]]
