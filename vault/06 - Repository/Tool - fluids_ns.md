---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/fluids_ns/build.py"
---

# Tool - fluids_ns

## Purpose

Generates the Fluid Mechanics Topic 4 problem page (`subjects/fluid-mechanics/problemas/topic-4-navier-stokes.html`) from the seventeen vault notes `Problem - NS1` to `Problem - NS17`, and keeps in step the places that list the problems: the source links, the subject MOC, `tools/nav.json`, the problems index card and the portal counters. The statement of each note is transcribed word for word from the official sheet; the figure of each statement is a cropped PNG of the sheet or a redrawn SVG (`tools/figures/fluids_t4.py`). The vault note is edited, never the page.

## Command

`python tools/fluids_ns/build.py [--check]`

## Inputs

- The notes `vault/01 - Fluid Mechanics/Problem - NS*.md`, read back with the reader of `tools/fluids_cl/notes.py` (prefix `NS`, figure folder `FM-T4`).
- The figures: PNG crops in `vault/attachments/FM-T4/` registered in `RASTER`, and the SVG figures of `tools/figures/fluids_t4.py`.
- The page templates of `tools/fluids_cl/` and the helpers of `tools/fluids_cl/build.py`.

## Read and write behaviour

Without `--check`, the tool rewrites the notes in their canonical layout, the page, the SVG figures and the lists named above. With `--check`, it regenerates in a scratch copy and exits 1 if a file differs. The PNG crops are inputs and are never regenerated.

## When to run

After editing a problem note or the figure module. Then run [[Tool - build_nav]], [[Tool - source_links]] and [[Tool - build_pdfs]], and the gates of [[Rules - AGENTS.md]].

## Related

[[Repository MOC]] · [[Tool - build_topic_pages]] · [[Tool - audit_portal]] · [[Tool - Test suite]]
