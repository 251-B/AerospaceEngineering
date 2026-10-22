---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_maths_bank.py"
---

# Tool - build_maths_bank

## Purpose

Builds the Advanced Maths problem bank from its vault notes: the 22 exam-style problems `Problem - Bank Pnn - ...` in `vault/04 - Advanced Maths/Problem Bank/`, indexed by [[Problem Set - Advanced Maths Problem Bank]]. P01 to P07 train the first partial (5 points), P08 to P14 the second partial (5 points) and P15 to P22 the final (2.5 points). Each note carries its metadata in the frontmatter (`bank_id`, `title`, `category`, `archetype`, `level`, `unit`, `difficulty`, `points`, `time_minutes`, `tags`, `origen`) and its content in `## Statement`, `## Setup`, `## (a) ... [x pts]` (with `### Hint`, `### Checkpoint`, `### Solution`) and `## Interpretation`. Each result was checked with SymPy in `scripts/am_bank/pnn.py`.

It reuses the note parser of `tools/build_mechanics_bank.py` and writes:

- `subjects/advanced-maths/data/problems.json` and `problems.js` (`window.AE_AM_BANK` plus the three blueprints `AE_AM_BLUEPRINT`, `AE_AM_BLUEPRINT_MT2`, `AE_AM_BLUEPRINT_FINAL`).
- The generated blocks of `subjects/advanced-maths/extra-problems/` (`index.html`, `midterm-1-problems.html`, `midterm-2-problems.html`, `final-problems.html`).

The exam structures live in `subjects/advanced-maths/data/exam-blueprint.json` (Midterm 1: one ODE problem plus one linear-system problem, the latter required by `must_archetypes`), `exam-blueprint-midterm-2.json` and `exam-blueprint-final.json`. The simulator (`assets/js/exam-simulator.js`) picks one with `?exam=midterm-1|midterm-2|final`.

## Command

`python tools/build_maths_bank.py [--check] [--lint]`

## Checks

Subquestion points add up to the item's points; categories and points agree; every subquestion has hint, checkpoint and solution; `$$` balanced; no emojis; the index note lists every item; every blueprint has enough items per part and its archetypes exist. `--check` exits 1 if a generated file is stale.

## When to run

After editing a bank note or a blueprint. The note is edited, never the JSON or the generated blocks.
