# Business plan presentation: worked example (AeroVanguard, Group B)

Final 7-minute presentation of the Business Plan of **AeroVanguard Autonomous Systems, S.L.** (Introduction to Engineering Management, BSc Aerospace Engineering, UC3M, 2026-27), kept as a model for future presentations. Team names are replaced by roles (CEO, CTO, Head of AI, COO, CMO, CFO).

## Files

| File | What it is |
| :--- | :--- |
| `build_deck.py` | Single source of truth: slide text, speaker script, source lines, Q&A and chart data. Generates everything else. |
| `AeroVanguard_Canva_Base.pptx` | 12 presented slides plus 4 backup slides, 16:9, speaker notes included. Imports into Canva (Create → Import file) with every element editable. |
| `AeroVanguard_Presentation_Guide.md` | Timing per speaker, Canva layout of each slide, the spoken script, delivery notes and the Q&A cheat sheet. |
| `figures/chart_*.png` | Charts drawn by the generator at their placed size (Calibri, 14 pt ticks). |

Rebuild with `python build_deck.py` (needs `python-pptx` and `matplotlib`).

## Method that worked

1. **Every figure from the plan and the model only.** The brief given to the AI contained one wrong number (Year 5 cash 13.75 M€ instead of 6.81 M€); checking the Excel caught it.
2. **One generator for slides, notes and guide**, so the script, the slides and the Q&A cannot disagree. Timings are computed from the spoken script (numbers written as they are said), at 140 words a minute plus slide and speaker changes, with a 125 wpm check for nervous speakers.
3. **Course rubric first.** Each block of the course guide appears on a presented slide (PESTEL and Porter, full VRIO with weaknesses, corporate and competitive strategy, operations with competitive priorities, segmentation and the 4P with life cycle, legal form, HR with payroll, break-even, structure and ratios, NPV, IRR and payback); detailed tables go to backup slides.
4. **Design rules:** one-line action titles, one navy conclusion band per slide, body text 14 pt or more, a source line and the group tag on every slide, orange only on navy.
5. **Several independent, demanding reviews per round**, each with its own rubric (professor and course guide, forensic numbers audit, slide design, oral delivery and Q&A, investor pitch), and every finding checked against the plan before it was applied.

| Review | Round 1 | Final round |
| :--- | :---: | :---: |
| Professor rubric (originality, content, format) | 8.9 | 10 (overall quality 9.2) |
| Forensic numbers audit | 8.5 | 9.3 to 9.5 |
| Oral delivery and Q&A | 6.8 | 8.9 |
| Slide design | 6.6 | 8.5 to 8.8 |
| Investor pitch | 6.0 | 6.5 (capped: no traction may be invented in a course plan) |
