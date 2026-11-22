---
materia: Business Management
tema: "Unit 3: investment selection (cash-flow profiles, timing of flows, payback, capitalization)"
bank_id: F06
title: "Cash-flow profiles, timing of flows and payback"
category: mt2_tf_block
unit: 3
concepts:
  - u3-payback-negative-flow
  - u3-timing-of-flows
  - u3-npv-profile-intercepts
  - u3-npv-profile-large-rate
  - u3-profile-slope-irr
  - u3-payback-uneven-flows
  - u3-payback-no-discounting
  - u3-accept-reject-npv-sign
  - u3-capitalization-compound
  - u3-constant-financial-structure
difficulty: 2
origen: "Statements written for the bank in the style of Exercise 4 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not official exercises. Content from 3_II_NPV IRR.pdf and its solutions (Exercises 1, 2, 3, 5 and 9) and Exercises 5 and 6 of the examples PDF."
tags:
  - problem-bank
  - midterm-2
  - true-false
  - unit-3
---

# Bank F06 — Cash-flow profiles, timing of flows and payback

> [!info] Practice item, not an official exercise
> Ten True/False statements written for the bank in the style of Exercise 4 of the examples PDF (+0.15 right, −0.15 wrong, 0 blank; the reasoning is required). Sources: 3_II_NPV IRR.pdf and 3_II_NPV_NPV IRR_solutions.pdf, Exercises 1, 2, 3, 5 and 9; Examples PDF, Exercises 5 and 6. The Topic 3 deck has no investment-selection slides, so the criteria are those used in the problem sheet and its key.

## F06.1 A negative flow after the outlay

- id: F06-S1
- concept_id: u3-payback-negative-flow

The payback criterion cannot be applied to a project whose net cash flow in year 1 is negative.

### Answer

F

### Reasoning

The payback still follows the cumulative flows: the negative flow only delays the recovery. Project X of Exercise 3 (outlay 1,200, flows −200, 300, 500, 200, 400, 400) accumulates −200, 100, 600, 800 and 1,200, so its payback is 5 years, and the key even prefers it.

### Source

3_II_NPV IRR.pdf, Exercise 3, and its key (Payback X = 5 years).

## F06.2 Same total, different timing

- id: F06-S2
- concept_id: u3-timing-of-flows

Two projects require the same outlay and their flows add up to the same total, but one of them receives most of its money in year 1 and the other in year 3. At any positive discount rate, the project that receives its money earlier has the higher NPV.

### Answer

T

### Reasoning

Each flow is divided by $(1+k)^t$, and this factor grows with $t$ when $k > 0$; moving money to an earlier year reduces the discount applied to it, so the present value of the same total is larger.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a) (each flow discounted with its own exponent); Examples PDF, Exercise 5 (a).

## F06.3 Where the profile meets the axes

- id: F06-S3
- concept_id: u3-npv-profile-intercepts

On a graph of the NPV against the discount rate, the profile of a project meets the vertical axis at its undiscounted net sum and the horizontal axis at its IRR.

### Answer

T

### Reasoning

At $r = 0$ every discount factor is 1, so the NPV is the sum of the flows minus the outlay; the profile reaches zero at the rate that cancels the NPV, which is the IRR. These are the two columns, NPV at 0% and IRR, that the key tabulates before drawing the graph.

### Source

Examples PDF, Exercise 5 (c) and Exercise 6 (c), tables of NPV at 0% and IRR.

## F06.4 Very large discount rates

- id: F06-S4
- concept_id: u3-npv-profile-large-rate

As the discount rate grows without limit, the NPV of a project made of an outlay followed by positive flows tends to zero.

### Answer

F

### Reasoning

The discounted flows $Q_t/(1+k)^t$ tend to zero, but the outlay at year 0 is not discounted, so the NPV tends to minus the initial outlay, $-A$, not to zero.

### Source

Examples PDF, Exercise 5 (c) (schematic graph of the NPV profiles); 3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a).

## F06.5 The steeper profile and the IRR

- id: F06-S5
- concept_id: u3-profile-slope-irr

Two projects have the same NPV at a discount rate of 0%. The one whose NPV profile falls faster as the rate rises has the lower IRR.

### Answer

T

### Reasoning

Both profiles start from the same point on the vertical axis, so the one that falls faster cuts the horizontal axis first, at a lower rate. In Exercise 5 of the examples, A and B both have an NPV of 100,000 at 0%; B falls faster (6,447.19 against 28,120.71 at 8%) and its IRR is lower (8.62% against 11.65%).

### Source

Examples PDF, Exercise 5 (b) and (c).

## F06.6 Payback with uneven flows

- id: F06-S6
- concept_id: u3-payback-uneven-flows

A project requires 100,000 € and generates 20,000 €, 50,000 € and 60,000 € in years 1, 2 and 3. If each flow arrives evenly during its year, its payback period is 2.5 years.

### Answer

T

### Reasoning

After two years $20{,}000 + 50{,}000 = 70{,}000$ € are recovered; the remaining 30,000 € come from the 60,000 € of year 3 in $30{,}000/60{,}000 = 0.5$ years, so the payback is 2.5 years.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (a) (fraction of the year in which the outlay is recovered).

## F06.7 Does payback discount

- id: F06-S7
- concept_id: u3-payback-no-discounting

Because the payback period adds up the flows year by year until the outlay is recovered, it already takes the time value of money into account.

### Answer

F

### Reasoning

The payback adds the flows at their nominal value, with no discount factor; it only counts how long the recovery takes. The time value of money enters through the NPV, which divides each flow by $(1+k)^t$.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercises 3 and 5 (b) (payback from undiscounted flows) against Exercise 5 (a) (NPV).

## F06.8 Slightly negative NPV

- id: F06-S8
- concept_id: u3-accept-reject-npv-sign

A project has an NPV of 100,000 at 0% and an NPV of −826.45 at the company's discount rate of 10%. It should be accepted, because its NPV is large at 0% and only slightly negative at 10%.

### Answer

F

### Reasoning

The decision is taken with the NPV at the company's own rate: a negative NPV at 10%, however small, means the project does not cover the cost of its funds (its IRR, 9.91%, is below 10%), so it is rejected. This is project A of Exercise 6 of the examples.

### Source

Examples PDF, Exercise 6 (b).

## F06.9 Deferring a debt for two years

- id: F06-S9
- concept_id: u3-capitalization-compound

A creditor who can invest at 5% a year is asked to defer a debt of 1,000 € for two years. The amount he should require at the end of year 2 is 1,100 €.

### Answer

F

### Reasoning

Capitalization is compound: $C_n = C_0(1+i)^n$, so $C_2 = 1{,}000 \times 1.05^2 = 1{,}102.50$ €. The figure 1,100 € adds the interest of the first year twice and forgets the interest earned on the interest.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 1.

## F06.10 New debt with a constant financial structure

- id: F06-S10
- concept_id: u3-constant-financial-structure

A company with capital of 6,000,000, reserves of 4,800,000 and debt of 7,200,000 retains 1,200,000 of profit in year 1. To keep its financial structure unchanged, it can take on 800,000 of new debt.

### Answer

T

### Reasoning

Equity is $6{,}000{,}000 + 4{,}800{,}000 = 10{,}800{,}000$, 60% of the total of 18,000,000. After retaining profit equity is 12,000,000, so the total must be $12{,}000{,}000/0.6 = 20{,}000{,}000$ and the debt $0.4 \times 20{,}000{,}000 = 8{,}000{,}000$: the new debt is $8{,}000{,}000 - 7{,}200{,}000 = 800{,}000$.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 2.

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
