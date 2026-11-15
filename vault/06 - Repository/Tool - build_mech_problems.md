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

Generates the Engineering Mechanics official problem pages (`subjects/engineering-mechanics/problemas/topic-1.html` to `topic-5.html`, the 51 particle problems, and `topic-6.html` to `topic-8.html`, the 42 rigid body problems `rb-01` to `rb-42`) from the notes `Problem Set - Topic N ...` (verbatim statements) and `Solution Set - Topic N ...` (worked solutions) in `vault/03 - Engineering Mechanics/`. What the notes do not hold (card title, badge, source note, structure version of each solution) lives in `tools/mech_problems.json`.

A solution with `"structure": 3` in the JSON follows the lecturer's order: `### Reference Frames, Bases and Coordinates`, `### Change of Basis and Position Vector` (with its deduction figures from `tools/figures/em_solutions.py`, embedded with an Obsidian embed of `attachments/EM-SOL/<name>.svg`), `### Kinematics`, `### Forces and Equations of Motion` (optional) and `### Answers and Checks`, which must contain "Check against the official key". `"structure": 2` is the legacy `### Phase 1..4` layout, accepted only until a topic is migrated. The page never shows the word "Phase": the sections carry their own headings and no badge.

## Structure 4 and topics 6-8 (rigid body)

`"structure": 4` requires six `###` sections in this order: `Reference Frames, Bases and Degrees of Freedom`, `Change of Basis, Position Vectors and Constraint Kinematics`, `Center of Mass and Inertia Tensor`, `Linear Momentum, Angular Momentum and Kinetic Energy`, `Free-Body Diagram and Equations of Motion`, `Answers and Checks` (with "Check against the official key" or "Limiting cases"). A section may be one sentence saying it does not apply. The rigid body problems are keyed `rb-NN` in `tools/mech_problems.json` (`topic` 6-8, `title`, `badge`, `source_note`, `structure`, `group` A-G); the notes use `## Problem RB-NN: title` (statement notes `## 📌 Problem RB-NN: title`), the card id is `rb-NN` and the visible number `RB NN`. Statements may carry several figures (`T6-RB04-figure.png`, `T8-RB20-figure-b.png`). Pages 6-8 group the cards under `<h2 id="group-a">` ... `group-g` headings (titles in `GROUPS` of the tool), keeping the order of the Problem Set note inside a group. A topic whose notes do not exist yet is skipped with a notice; when its notes exist and its page does not, the page is created from the head, header, banner and footer of `topic-5.html`. `EXPECTED` counts: 6, 10, 12, 3, 20, 8, 8, 26.

## Derivation boxes, the gate and the simulator

- A `> [!derivation] Title` callout (see `tools/derivation.py`) is rendered as a derivation box; a figure embed inside it is numbered like the others. Parse errors are errors of the problem.
- Gate `no-inline-calc`: for structure 3 and 4 the rendered solution goes through `derivation.gate` (no equals sign, `\dot`, `\times`, `\frac`, `\int` in prose; no `$$` outside a box). Statements are never gated. `"boxed": false` in the JSON switches the gate off for a legacy structure-3 solution (all 20 Topic 5 problems today); it is not allowed with structure 4. Each run prints how many problems are structure 2, `"boxed": false` and fully boxed.
- `> [!example] Interactive simulator` followed by `> sim: {"archetype": ..., "params": ..., "defaults": ..., "readouts": [...]}` renders `<div class="m3-sim" data-archetype data-config>` with a no-JavaScript fallback; one per problem, archetype from the eight of `mechanics-3d-sim.js`. A page with a simulator links `mechanics-3d-sim.css` and `.js`; every page links `derivation-box.css`; all go before `responsive.css`, which stays the last stylesheet.
- `"badges": [...]` in the JSON adds badges next to `badge` (In-Class Sessions, Oscillations lectures).

## Command

`python tools/build_mech_problems.py [--check]`

## Read and write behaviour

It reads the notes and the JSON and rewrites only the cards of each page (from the first `<!-- Problem` comment to `<div class="article-nav">`), keeping the head, header, banner and navigation. PDF deep links are not applied here, so the comparison strips them first. `--check` is read-only and exits 1 if a page is stale or a note is invalid (missing problem, missing figure caption, wrong structure, inline calculation outside a box, emoji in a card).

## When to run

- After editing a Problem Set or Solution Set note of Engineering Mechanics. The note is edited, never the page.
- Order: this tool, then `python tools/source_links.py`, then `python tools/build_pdfs.py`.

## Related

[[Repository MOC]] · [[Tool - build_problem_pages]] · [[Tool - build_topic_pages]] · [[Tool - source_links]] · [[Tool - build_pdfs]] · [[Tool - Test suite]]
