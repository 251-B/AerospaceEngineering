---
materia: Business Management
tema: "Unit 3: investment selection (NPV against IRR, Fisher's rate, exclusive and independent projects, cost of capital)"
bank_id: F07
title: "Ranking conflicts, Fisher's rate and the cut-off rate"
category: mt2_tf_block
unit: 3
concepts:
  - u3-fisher-rate-graph
  - u3-no-project-rate
  - u3-decision-intervals
  - u3-budget-ranking
  - u3-conflict-cause
  - u3-independent-projects
  - u3-wacc-weights-effect
  - u3-wacc-cutoff-rate
  - u3-fisher-rate-zero
  - u3-irr-two-year-quadratic
difficulty: 2
origen: "Statements written for the bank in the style of Exercise 4 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not official exercises. Content from 3_II_NPV IRR.pdf and its solutions (Exercises 7, 8 and 9), Exercises 5 and 6 of the examples PDF and Topic 3, Slide 37."
tags:
  - problem-bank
  - midterm-2
  - true-false
  - unit-3
---

# Bank F07 — Ranking conflicts, Fisher's rate and the cut-off rate

> [!info] Practice item, not an official exercise
> Ten True/False statements written for the bank in the style of Exercise 4 of the examples PDF (+0.15 right, −0.15 wrong, 0 blank; the reasoning is required). Sources: 3_II_NPV IRR.pdf and 3_II_NPV_NPV IRR_solutions.pdf, Exercises 7, 8 and 9; Examples PDF, Exercises 5 and 6; Topic 3, Slide 37. The Topic 3 deck has no investment-selection slides, so the criteria are those used in the problem sheet and its key.

## F07.1 Reading Fisher's rate on the graph

- id: F07-S1
- concept_id: u3-fisher-rate-graph

On a graph of the NPV against the discount rate, the Fisher's rate of two projects is read as the horizontal coordinate of the point where their two profiles cross.

### Answer

T

### Reasoning

Where the profiles cross, both projects have the same NPV, which is the condition $NPV_A = NPV_B$ that defines Fisher's rate; the horizontal axis carries the discount rate, so the crossing point gives the rate.

### Source

Examples PDF, Exercise 5 (c); 3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b).

## F07.2 The rate above which nothing is chosen

- id: F07-S2
- concept_id: u3-no-project-rate

When several mutually exclusive projects are compared, the discount rate above which no project is chosen is the lowest of their IRRs.

### Answer

F

### Reasoning

Above the lowest IRR the other projects can still have a positive NPV. No project is chosen only when every NPV is negative, that is above the highest IRR: 18.02% (project C) in Exercise 5 of the examples and 12.87% (project C) in Exercise 6.

### Source

Examples PDF, Exercises 5 (c) and 6 (c), conclusions.

## F07.3 Which project lies below the crossing

- id: F07-S3
- concept_id: u3-decision-intervals

When the NPV profiles of two projects cross once at a positive Fisher's rate, the project with the higher IRR is preferred at every discount rate below that Fisher's rate.

### Answer

F

### Reasoning

It is the other way round: the higher-IRR project is preferred above the Fisher's rate (as long as its NPV is positive), and below it the project with the larger NPV at 0% leads. In Exercise 5 of the examples, A is preferred to C below 4.77% even though C has the higher IRR (18.02% against 11.65%).

### Source

Examples PDF, Exercise 5 (c), pair A–C.

## F07.4 Ranking under a budget

- id: F07-S4
- concept_id: u3-budget-ranking

When a budget limits a set of independent projects that cannot be repeated, the key of the problem sheet undertakes them in decreasing order of NPV until the budget is used up.

### Answer

T

### Reasoning

In Exercise 7 every project has a positive NPV at 10%, and with 40,000 € the key takes D, C and F (the three largest NPVs, outlays $13{,}000 + 12{,}000 + 15{,}000 = 40{,}000$ €).

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 7.

## F07.5 What makes the rankings disagree

- id: F07-S5
- concept_id: u3-conflict-cause

The NPV and IRR rankings of two projects can only disagree when the projects require different initial outlays.

### Answer

F

### Reasoning

The timing of the flows alone can make the profiles cross. With the same outlay of 100,000 €, a project paying 120,000 € in year 1 has an IRR of 20% and an NPV of 20,000 € at 0%, while one paying 135,000 € in year 2 has an IRR of about 16.2% and an NPV of 35,000 € at 0%; below their Fisher's rate of 12.5% the NPV ranks the second first and the IRR the first.

### Source

Examples PDF, Exercise 5 (c) (profiles that cross); 3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b). The figures of the reasoning are an example worked for the bank.

## F07.6 Independent projects

- id: F07-S6
- concept_id: u3-independent-projects

If two projects are independent and both have a positive NPV at the cost of capital, the company should undertake only the one with the higher NPV.

### Answer

F

### Reasoning

Choosing only one is the rule for mutually exclusive projects ("only one can be accepted"). Independent projects are each accepted when their NPV is positive, as in Exercise 7, where every project with a positive NPV is undertaken while the budget allows.

### Source

Examples PDF, Exercise 5 (statement: mutually exclusive projects); 3_II_NPV_NPV IRR_solutions.pdf, Exercise 7.

## F07.7 Cheaper liabilities in the mix

- id: F07-S7
- concept_id: u3-wacc-weights-effect

If a company replaces part of its equity with liabilities whose cost is lower than that of equity, and both costs stay unchanged, its capital cost falls.

### Answer

T

### Reasoning

$K_{WACC} = K_{EQ}\,E/(E+L) + K_L\,L/(E+L)$ is a weighted average; moving weight from the dearer resource to the cheaper one, with the two costs fixed, lowers the average.

### Source

Topic 3, Slide 37.

## F07.8 Comparing the yield with the cost of debt

- id: F07-S8
- concept_id: u3-wacc-cutoff-rate

A company is financed 30% with equity at a cost of 15% and 70% with liabilities at an average cost of 8%. It should accept a project with a yield of 8.5%, because the yield exceeds the cost of the liabilities that finance most of it.

### Answer

F

### Reasoning

The cut-off rate is the weighted cost of all the funds, $K = 0.30 \times 15\% + 0.70 \times 8\% = 10.1\%$, not the cost of the debt alone. Since $8.5\% < 10.1\%$ the project is rejected; a project yielding 18.5% would be accepted.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 8; Topic 3, Slide 37.

## F07.9 A pair whose only crossing is at zero

- id: F07-S9
- concept_id: u3-fisher-rate-zero

For two two-year projects whose only Fisher's rate is 0%, one of the two projects is preferred to the other at every positive discount rate.

### Answer

T

### Reasoning

The two profiles meet only at $r = 0$, so for $r > 0$ one stays above the other. In Exercise 6 of the examples, A and B cross at 0% and B is never preferred for $r > 0$.

### Source

Examples PDF, Exercise 6 (c), pair A–B and conclusion; Exercise 5 (c), pair A–B.

## F07.10 The quadratic of a two-year IRR

- id: F07-S10
- concept_id: u3-irr-two-year-quadratic

For a project with an outlay $A$ and flows $Q_1$ and $Q_2$ in years 1 and 2, the IRR is found by writing $x = 1 + r$ and taking the positive root of $A x^2 - Q_1 x - Q_2 = 0$.

### Answer

T

### Reasoning

Setting $-A + Q_1/x + Q_2/x^2 = 0$ and multiplying by $-x^2$ gives $A x^2 - Q_1 x - Q_2 = 0$; the product of its roots is $-Q_2/A < 0$, so exactly one root is positive and the IRR is that root minus 1.

### Source

Examples PDF, Exercise 5 (b) ($500{,}000x^2 - 200{,}000x - 400{,}000 = 0$) and Exercise 6 (b).

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
