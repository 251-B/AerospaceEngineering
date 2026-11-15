---
subject: "Repository"
tags:
  - repository
  - tool
  - generator
source: "tools/build_materials_bank.py"
---

# Tool - build_materials_bank

## Purpose

Builds the Aerospace Materials I Midterm 2 bank (Assessment Test II, Units 4 to 7) from the notes of `vault/02 - Aerospace Materials I/Problem Bank/`, indexed by [[Problem Set - Aerospace Materials I Problem Bank]] and specified by [[Rules - Midterm 2 Exam Style Analysis]].

Two kinds of notes:

- `Quiz - Bank Bnn - Unit N <theme>.md`: one **block of ten test questions** (one note per block, not per question: 520 single notes would not be maintainable). Frontmatter: `bank_id`, `title`, `category: mt2_test_block`, `unit`, `concepts`, `difficulty`, `tags`, `origen`. Each question is a `## Qnn.k <short title>` section with a metadata list (`- id: Bnn-Qk`, `- concept_id: uN-...`, `- format: ...`, `- asks: ...`, and for numbers `- calc: <expression>` or `- check: <condition>`), the statement, the options `a)` to `d)`, `### Answer` (one letter), `### Explanation` (why the answer is right, then one bullet `- x) ...` per wrong option naming the mistake behind it) and `### Source` (slide or page).
- `Problem - Bank Pnn - <title>.md`: one Part II problem of 5 points in the format of `tools/build_mechanics_bank.py` (`## Statement`, `## Setup`, `## (a) ... [x pts]` with `### Hint`, `### Checkpoint`, `### Solution`, `## Interpretation`), `category: mt2_problem`, plus `## Verification` with one bullet `- <label> | <expression> | <stated value>` per recomputed result.

It writes `subjects/aerospace-materials-1/data/problems.json` and `problems.js` (`window.AE_MAT_BANK`, and `window.AE_MAT_BLUEPRINT_MT2` read from `data/exam-blueprint-midterm-2.json`), the figures of `tools/figures/materials_mt2.py` (one module per unit in `tools/figures/mat_mt2/`, vault copies in `vault/attachments/MAT-MT2/`) and the generated blocks of `subjects/aerospace-materials-1/extra-problems/` (`index.html`, `midterm-2-test.html`, `midterm-2-problems.html`).

## Command

`python tools/build_materials_bank.py [--check] [--lint] [--allow-partial]`

`python tools/materials_bank/verify_mt2.py` recomputes every `calc`, `check` and Verification line. `python tools/materials_bank/preview_figures.py OUT_DIR [name ...]` renders PNG previews of the figures.

## Checks

Ten questions per block with ids `Bnn-Q1` to `Bnn-Q10`; four different options and exactly one answer; every wrong option explained; a source per question; a numeric question's right option matches its `calc` and no wrong option does; the four options carry the same unit; at most four questions per `concept_id`, and those differ in format or in what they ask; the right letter spread over a to d (20 to 30 % each) and never four times in a row in a block; text similarity between every pair of questions below 0.80, with the pairs above 0.65 listed for review; unit quotas (150, 170, 100, 100); at least four problems per type; subquestion points add up; every solution has step titles; `$` and `$$` balanced; no emojis, no "Phase N" labels, no `\euro`; every figure exists; the index lists every note; the blueprint adds up. `--allow-partial` skips the quotas while the bank is being written. `--check` exits 1 if a generated file is stale.

## When to run

After editing a bank note, a figure module or the blueprint. The note is edited, never the JSON or the generated blocks. Then `build_nav`, `build_pdfs` and the tests.
