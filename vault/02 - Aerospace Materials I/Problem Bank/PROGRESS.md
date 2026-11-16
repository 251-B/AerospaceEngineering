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

## Pending

- Problems P01-P20 (four per type; specification in the analysis note, section 6). None written yet: the build runs with `--allow-partial` until they exist, and the simulator draws only the test.
- Audit of a 10 % sample of the questions and of every problem (`problem-step-mentor`), then the ultrareview.
- Full test suite with the browser harnesses on a machine where headless Chrome can reach the network.

**Back to:** [[Problem Set - Aerospace Materials I Problem Bank]]
