---
materia: Aerospace Materials I
tema: "Midterm 2 bank: progress log"
tipo: progress
estado: in-progress
tags:
  - problem-bank
  - midterm-2
---

# Midterm 2 bank: progress

Working log of the build of the Midterm 2 bank, kept so that the work can be resumed. Specification: [[Rules - Midterm 2 Exam Style Analysis]].

## Done

- Analysis of the paper and quota table ([[Rules - Midterm 2 Exam Style Analysis]]).
- `tools/build_materials_bank.py`, `tools/materials_bank/verify_mt2.py`, `update_index.py`, `preview_figures.py`, figure package `tools/figures/mat_mt2/`.
- `assets/js/exam-simulator.js`: multiple-choice parts and block practice; `assets/css/mcq.css`.
- Blueprint, Extra problems pages, simulator page, tab strips, nav, landing chips, updates entry, docs, tests.
- **Test bank: 62 blocks, 620 questions** (Unit 4 B01-B15, Unit 5 B16-B32, Unit 6 B33-B42 and B53-B57, Unit 7 B43-B52 and B58-B62), all recomputed by `verify_mt2.py`.
- Units 6 and 7 audit: 24 questions rewritten for answer-form tells; 100 new questions (B53-B62); see section 8 of the rules note.
- Simulator practice scopes: real paper, focus on Units 6 and 7, and one unit only (`modes` of the blueprint).

- **Part II complete (2026-27 structure): 20 problems.** P01-P12 the long phase-diagram problem (3 points: binary diagrams with compounds, eutectic systems, Fe-Fe3C steels), P13-P20 the short Unit 5 problem (2 points: tensile test, bar under load). Every result recomputed by `verify_mt2.py`; all 20 audited by `problem-step-mentor` (21 defects found and fixed: P11 lamella colours, P12 hardness claim, P18 E/rho, P19 reloading marked extension, lever-rule and true-strain derivations, readings).

## Pending

- Confirm the points of the two problems (3 + 2 is an assumption from the finals) and the duration (75 min assumed); update `exam-blueprint-midterm-2.json`.
- Browser test harnesses (`mcq_simulator_harness.html`, `test_surface`) and `render_check.py` on a machine where headless Chrome works; here the pages were checked with Playwright (no KaTeX or console errors).

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
