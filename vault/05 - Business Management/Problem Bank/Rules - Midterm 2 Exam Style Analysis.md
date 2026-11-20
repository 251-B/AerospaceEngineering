---
materia: Business Management
tema: "Midterm 2 (Topics 3 Part II to 7): exam style and rules of the bank"
tipo: rules
origen: "sources/cuatrimestre-1/05-business-management/examenes/BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf (Exam exercises, examples with solutions, Exercises 1 to 6); structure of the simulated exam agreed with the student on 2026-11-20"
tags:
  - problem-bank
  - midterm-2
  - rules
---

# Rules - Midterm 2 Exam Style Analysis

This note is the specification of the Business Management Midterm 2 bank: what the course's example exam shows, how the simulated exam is built, and the exact format of every bank note. `tools/bm_mt2/bank.py` (called by `python tools/build_problem_bank.py`) enforces it.

## 1. What the official examples show

`BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf` ("Exam exercises – examples with solutions") holds eight example exercises with their solutions. Exercises 7 and 8 (financial statements with pending operations, ECOBIKE and SOLARBIKE) belong to Topic 3 Part I and are **out of the scope of Midterm 2**. The six in scope:

| Ex. | Content | Points | Archetype of the bank |
| :--- | :--- | :--- | :--- |
| 1 | Pegasus S.A.: break-even list price with a 5% commercial discount, volume for a target profit, operating leverage at two volumes and its meaning, price rise with a price elasticity of demand of 1.4 | 2.5 | `bep-ol-elasticity` |
| 2 | TechNova Solutions: parts of strategic marketing (customer orientation, positioning, segmentation/targeting), product attribute strategy (brand, design, quality, service; communication is not a product attribute), distribution strategy (direct, short zero-level channel, B2B, exclusive intensity) | 2.5 | `marketing-case` |
| 3 | Agile methodology: one task per managerial function (planning, organizing, leading, controlling), the eight steps of the decision-making process, four KPIs, the hardest structure (machine bureaucracy) and the easiest (adhocracy) | 2.0 | `management-case` |
| 4 | Twenty True/False statements, +0.15 right, −0.15 wrong, 0 blank; "no answer will be accepted as correct without the reasoning" | 3.0 | True/False part |
| 5 | SunTech Energy: maximum outlay of B for NPV ≥ 0, IRR ranking, a third project C, NPV profiles, Fisher's rates A–B, A–C, B–C, decision intervals and the rate above which no project is chosen | 2.0 | `npv-irr-fisher` |
| 6 | GreenWave Solutions: same structure, with the trap where IRR(A) > IRR(B) but both are below the 10% cost of capital, so neither is accepted | 2.0 | `npv-irr-fisher` |

The PDF has no multiple-choice part and no Topic 7 exercise. The multiple-choice part and the `innovation-case` archetype are practice formats added for the portal (agreed with the student) and are labelled as such.

## 2. The simulated exam (data/exam-blueprint-midterm-2.json)

| Part | Items | Rule | Points |
| :--- | :--- | :--- | :--- |
| I. True / False | 20 statements, 4 per unit (3, 4, 5, 6, 7) | +0.15 right, −0.15 wrong, 0 blank, never below 0; a short written reason for each answer | 3.0 |
| II. Multiple choice | 8 questions (2 of Units 3, 4, 5; 1 of Units 6, 7) | +0.25 right, −0.08 wrong, 0 blank, never below 0 | 2.0 |
| III. Problems and cases | 2 items of different archetypes | graded per part with the key results | 2 × 2.5 = 5.0 |
| **Total** | 90 min (options 60 / 90 / 120) | | **10.0** |

The −0.15 of a wrong statement and the 3 points of Part I are those of Exercise 4. The +0.25 / −0.08 rule of Part II and the 2.5 points of every bank problem are choices of the portal: the official example problems are worth 2 to 2.5 points.

Practice modes: Full Midterm 2 exam; True/False practice and Multiple-choice practice (units chosen with checkboxes, 5 / 10 / 15 / 20 / all questions spread evenly over the chosen units, timed or corrected as you answer); Problems and cases practice (archetypes chosen with checkboxes).

## 3. Units and concept ids

| unit | Content | Main sources |
| :--- | :--- | :--- |
| 3 | Topic 3 Part II, investment selection: NPV, IRR, payback, Fisher's rate, cost of capital (WACC) as the discount rate | `Topic 3_Financial Management (I).pdf`; `3_II_NPV IRR.pdf` and `3_II_NPV_NPV IRR_solutions.pdf`; notes `Problem - T3 NPV 1..9`; Exercises 5-6 of the examples PDF |
| 4 | Topic 4, the production function: costs, break-even point, operating leverage, productivity, production processes | `Topic 4_ The Production Function.pdf`; `BEP  OL Statements  Solutions.pdf`; notes `Problem - T4 Exercise 1..8` |
| 5 | Topic 5, marketing and sales: strategic vs operational marketing, segmentation, targeting, positioning, the marketing mix, product attributes and ranges, price and price elasticity of demand, distribution, communication | `Topic 5_ Marketing _ Sales Management (I+II).pdf`, `topic 5.2.2.pdf`; `PED Exercises SOL.pdf` |
| 6 | Topic 6, the management function: decisions, decision-making process, management levels, skills, roles, planning, organizing, structures and configurations, HR, controlling | `Topic 6_ The Management Function.pdf` |
| 7 | Topic 7, entrepreneurship and innovation: sources of innovation, creativity, R&D, collaborative networks, technology trajectories, the four pairs of innovation types, the S-curve, discontinuous technologies, diffusion, dominant design | `Topic 7_Entrepreneurship  Innovation.pdf` |

A `concept_id` is `u<unit>-<kebab-case>` (`u4-operating-leverage-meaning`). Anything the course PDFs do not define (KPIs as a term, for example) is marked **extension** with its definition. Cite the official material outside `$...$`, as `Topic 6, Slide 6`, `3_II_NPV IRR.pdf, Exercise 9`, `Examples PDF, Exercise 4`.

## 4. True/False blocks: `Quiz - Bank Fnn - Unit N <theme>.md`

One note per block of **ten** statements on one unit. Frontmatter:

```yaml
---
materia: Business Management
tema: "Unit 4: operating leverage and economic risk"
bank_id: F02
title: "Costs, break-even point and operating leverage"
category: mt2_tf_block
unit: 4
concepts:
  - u4-operating-leverage-meaning
  - ...
difficulty: 2
origen: "Statements written for the bank in the style of Exercise 4 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not official exercises. Content from Topic 4, Slides ..."
tags:
  - problem-bank
  - midterm-2
  - true-false
  - unit-4
---
```

Then `# Bank F02 — <title>`, the callout `> [!info] Practice item, not an official exercise` with one line on the sources, and ten sections:

```markdown
## F02.1 Fixed costs and operating leverage

- id: F02-S1
- concept_id: u4-operating-leverage-meaning

A firm whose costs are mostly variable has a higher economic risk, because its operating profit varies more when sales change.

### Answer

F

### Reasoning

Mostly variable costs mean a low operating leverage: the operating profit changes little when sales change, so the economic risk is lower, not higher.

### Source

Topic 4, Slide 20; Examples PDF, Exercise 4, statement 2.
```

Rules: numbering F02.1 to F02.10 and ids F02-S1 to F02-S10 in order; `### Answer` is `T` or `F`; the reasoning (one to three sentences) is the justification a student must write in the exam: for a false statement it names the error and gives the right version. Each block has between 4 and 6 true statements and never the same answer four times in a row; over the whole bank the true statements are 45% to 55%. A statement tests one idea, is unambiguous under the course's own definitions, and its trap is a real confusion of the course (strategic vs operational marketing, width vs depth of a range, recruitment vs selection, tactical vs operational decisions, fixed vs variable costs and leverage, payback vs NPV, radical vs incremental, architectural vs component, ...). Do not copy the six example statements of Exercise 4 word for word. At most three statements per `concept_id` in the bank, and no two statements with nearly the same wording.

## 5. Multiple-choice blocks: `Quiz - Bank Bnn - Unit N <theme>.md`

Same format as the Aerospace Materials I blocks (`Tool - build_materials_bank`): category `mt2_mcq_block`; ten sections `## B02.k <title>` with `- id: B02-Qk`, `- concept_id`, `- format` (one of `true-statement`, `false-statement`, `complete-sentence`, `cause-effect`, `what-happens`, `numeric`, `identify`, `ordering`), `- asks` (one of `definition`, `cause`, `effect`, `calculation`, `comparison`, `classification`, `application`), a numeric question also `- calc: <python expression>` that gives the number of the right option (the four options start with a number and carry the same unit); the statement; options `a)` to `d)`; `### Answer` (one letter); `### Explanation` (why the answer is right, then one bullet `- x) ...` per wrong option naming the mistake behind it, at least 25 characters each); `### Source`. Four different options; the right letter never four times in a row in a block and spread over a-d in the bank; at most four questions per `concept_id`, and those differ in format or in what they ask. Money is written `€` inside `\text{}` in maths or as plain text, never `\euro`.

## 6. Problems and cases: `Problem - Bank Mnn - <title>.md`

Format of `tools/build_mechanics_bank.py` (`Problem - Bank Pnn` of Materials). Frontmatter:

```yaml
---
materia: Business Management
tema: "Unit 3: investment selection"
bank_id: M01
title: "..."
category: mt2_problem
archetype: npv-irr-fisher
level: standard          # standard | trap | conceptual
unit: 3
difficulty: 2
points: 2.5
time_minutes: 22
official: false
origen: "Problem written for the bank in the style of Exercises 5 and 6 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not an official exercise."
tags:
  - problem-bank
  - midterm-2
  - npv-irr-fisher
---
```

| archetype | unit | Model |
| :--- | :--- | :--- |
| `npv-irr-fisher` | 3 | Exercises 5-6 |
| `bep-ol-elasticity` | 4 | Exercise 1 (Topic 4 with the price elasticity of Topic 5) |
| `marketing-case` | 5 | Exercise 2 |
| `management-case` | 6 | Exercise 3 |
| `innovation-case` | 7 | Topic 7 (no official example) |

Body: `# Bank M01 — <title>`, the callout `> [!info] Practice item, not an official exercise`, `## Statement`, optional `## Setup` (data and model, with the formulas of the course and their citation), then `## (a) <prompt> [0.5 pts]` ... with `### Hint`, `### Checkpoint` (key figures for problems, the points the answer must contain for cases) and `### Solution` made of `#### <step title>` steps; the subquestion points add up to exactly 2.5. Optional `## Interpretation`. Numeric problems end with `## Verification`, one line per result: `- <label> | <python expression> | <stated value>` (the expression recomputes the value printed in the solution; names `sqrt`, `log`, `exp`, `min`, `max`, `abs`, `round` are available).

- Calculations follow the course with no skipped step: NPV $= -A + \sum_t Q_t/(1+k)^t$; for two-year projects the IRR and every Fisher rate come from a quadratic in $x = 1 + r$, solved with its formula; the decision intervals are stated, and the rate above which every NPV is negative. An `npv-irr-fisher` problem embeds its NPV profile, the file `<id lowercase>-npv-profile.svg` of `attachments/BM-MT2` (drawn by `tools/figures/bm_mt2.py` from the cash flows of the statement) in the solution of the graph part.
- Break-even: $Q^* = CF/(p - c_v)$, operating leverage $OL = Q(p-c_v)/(Q(p-c_v) - CF)$ and its meaning, $\Delta Q/Q = -\varepsilon\,\Delta p/p$ as in Exercise 1.
- Cases: a statement of one to three paragraphs about an aerospace or technology company, with the facts the answer must find in it; the solution quotes the facts of the statement and names the concept of the course each one illustrates, and says what does not belong (as Exercise 2 says that communication is not a product attribute).

No emojis, no "Phase N" labels, balanced `$` and `$$`, academic English.
