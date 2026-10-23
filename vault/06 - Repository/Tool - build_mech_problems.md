---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_mech_problems.py"
---

# Tool - build_mech_problems

## Purpose

Generates the five Engineering Mechanics official problem pages (`subjects/engineering-mechanics/problemas/topic-1.html` to `topic-5.html`, 51 problems in all) from the notes `Problem Set - Topic N ...` (verbatim statements) and `Solution Set - Topic N ...` (worked solutions) in `vault/03 - Engineering Mechanics/`. What the notes do not hold (card title, badge, source note, structure version of each solution) lives in `tools/mech_problems.json`.

A solution with `"structure": 3` in the JSON follows the lecturer's order: `### Reference Frames, Bases and Coordinates`, `### Change of Basis and Position Vector` (with its deduction figures from `tools/figures/em_solutions.py`, embedded with an Obsidian embed of `attachments/EM-SOL/<name>.svg`), `### Kinematics`, `### Forces and Equations of Motion` (optional) and `### Answers and Checks`, which must contain "Check against the official key". `"structure": 2` is the legacy `### Phase 1..4` layout, accepted only until a topic is migrated. The page never shows the word "Phase": the sections carry their own headings and no badge.

## Command

`python tools/build_mech_problems.py [--check]`

## Read and write behaviour

It reads the notes and the JSON and rewrites only the cards of each page (from the first `<!-- Problem` comment to `<div class="article-nav">`), keeping the head, header, banner and navigation. PDF deep links are not applied here, so the comparison strips them first. `--check` is read-only and exits 1 if a page is stale or a note is invalid (missing problem, missing figure caption, wrong structure for a structure-2 solution, emoji in a card).

## When to run

- After editing a Problem Set or Solution Set note of Engineering Mechanics. The note is edited, never the page.
- Order: this tool, then `python tools/source_links.py`, then `python tools/build_pdfs.py`.

## Related

[[Repository MOC]] · [[Tool - build_problem_pages]] · [[Tool - build_topic_pages]] · [[Tool - source_links]] · [[Tool - build_pdfs]] · [[Tool - Test suite]]
