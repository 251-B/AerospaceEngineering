---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_topic_pages.py"
---

# Tool - build_topic_pages

## Purpose

Generates the theory pages listed in `tools/topic_pages.json` from their vault notes. Six pages are configured: three for Aerospace Materials I and three for Business Management. Each page keeps its own head, header and footer. The PDF deep links from [[Tool - source_links]] are applied before the file is written. The vault note is edited, never the page.

## Command

`python tools/build_topic_pages.py [PAGE ...] [--check]`

## Inputs

- `tools/topic_pages.json`: the page list. Each entry names its vault note and its figure module.
- The vault note of each page, with its frontmatter removed.
- The figure modules in `tools/figures/` (`bm_t1` to `bm_t3`, `materials_t1` to `materials_t3`), with the shared helpers `tools/figures/svgkit.py` and `tools/figures/bm_common.py`.
- `tools/source_links.json` and `tools/source_anchors.json`.

## Read and write behaviour

Without `--check`, the tool writes each configured page under `subjects/` and each figure SVG into `vault/attachments/`. With `--check`, it writes nothing and exits 1 if a page or a figure is stale.

## When to run

- After editing a vault note listed in `tools/topic_pages.json`, or a figure module. Run it without `--check` to regenerate, then run `--check` in the gate.
- For Business Management pages, the order is build_topic_pages, then [[Tool - build_problem_pages]], then [[Tool - source_links]], then [[Tool - build_pdfs]] (see [[Rules - AGENTS.md]]).

## Related

[[Repository MOC]] · [[Agent - aerospace-pedagogue]] · [[Tool - audit_portal]] · [[Tool - Test suite]]
