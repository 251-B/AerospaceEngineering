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

Generates the theory pages listed in `tools/topic_pages.json` from their vault notes. Seven pages are configured: three for Aerospace Materials I, three for Business Management and the Fluid Mechanics Topic 4 page (`"flavor": "fluids"`, which builds the body in the style of the Fluid Mechanics pages from the head of a sibling page). Each page keeps its own head, header and footer. The PDF deep links from [[Tool - source_links]] are applied before the file is written. The vault note is edited, never the page.

## Mechanics flavor

Entries with `"flavor": "mechanics"` (Engineering Mechanics) take the head, header, CSS and footer of a sibling hand-written theory page (`template`) and build the body from the note: central idea (first blockquote), `## N. Title` sections (the `h2` carries `id="sec-N"`, `###` headings get ids), a topic outline, previous/practice/next links. Accepted blocks: paragraphs, lists, tables (in a scrolling `.table-wrapper`), `> [!info]`, `> [!note]`, `> [!tip]`, `> [!warning]` callouts, `> [!info] Extension` (title starting with "Extension": dashed accent box), `> [!example] Title` (example card), figures (the attachments embed of an SVG) from the figure module (`tools/figures/em_theory.py`) and the callout `> [!derivation] Title` rendered by `tools/derivation.py` (a figure may sit inside a box). A box with a syntax error, or any calculation in prose or a display formula outside a box (`no-inline-calc`, `derivation.gate`), fails the build and `--check` with one message per finding. The page links `assets/css/derivation-box.css` and keeps `responsive.css` as the last stylesheet. Entry keys: `flavor`, `template`, `note`, `figures` (optional), `html_title`, `category`, `title`, `subtitle`, `source` (optional, citations in it are linked), `nav` (`[href, label, "prev" | "center" | "next"]`).

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
