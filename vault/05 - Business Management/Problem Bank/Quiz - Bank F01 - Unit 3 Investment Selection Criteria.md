---
materia: Business Management
tema: "Unit 3: investment selection (NPV, IRR, payback, Fisher's rate, cost of capital)"
bank_id: F01
title: "Investment selection criteria and the cost of capital"
category: mt2_tf_block
unit: 3
concepts:
  - u3-npv-definition
  - u3-irr-definition
  - u3-irr-below-cost-of-capital
  - u3-irr-npv-relation
  - u3-payback-limits
  - u3-fisher-rate-definition
  - u3-wacc-definition
  - u3-cost-of-equity
  - u3-npv-rate-sensitivity
  - u3-fisher-rate-zero
difficulty: 2
origen: "Statements written for the bank in the style of Exercise 4 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not official exercises. Content from 3_II_NPV IRR.pdf and its solutions (Exercises 3 to 9), Exercises 5 and 6 of the examples PDF and Topic 3, Slide 37."
tags:
  - problem-bank
  - midterm-2
  - true-false
  - unit-3
---

# Bank F01 — Investment selection criteria and the cost of capital

> [!info] Practice item, not an official exercise
> Ten True/False statements written for the bank in the style of Exercise 4 of the examples PDF (+0.15 right, −0.15 wrong, 0 blank; the reasoning is required). Sources: 3_II_NPV IRR.pdf and 3_II_NPV_NPV IRR_solutions.pdf, Exercises 3 to 9; Examples PDF, Exercises 5 and 6; Topic 3, Slide 37. The Topic 3 deck has no investment-selection slides, so the criteria are those used in the problem sheet and its key.

## F01.1 What the NPV adds up

- id: F01-S1
- concept_id: u3-npv-definition

The NPV of a project is the sum of its net cash flows minus the initial outlay, with every flow counted at its nominal value whatever the year in which it arrives.

### Answer

F

### Reasoning

That sum is only the NPV at a discount rate of 0%. The NPV discounts each flow to year 0, $NPV = -A + \sum_t Q_t/(1+k)^t$, so a flow received later is worth less today.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a); Examples PDF, Exercise 5 (a).

## F01.2 The rate that cancels the NPV

- id: F01-S2
- concept_id: u3-irr-definition

The internal rate of return of a project is the discount rate at which its NPV is equal to zero.

### Answer

T

### Reasoning

This is the definition used in the key: the IRR is the rate that makes the NPV equal to 0, which is why a known IRR lets one solve for the initial outlay.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercises 4 and 6.

## F01.3 Ranking two projects below the cost of capital

- id: F01-S3
- concept_id: u3-irr-below-cost-of-capital

Two mutually exclusive projects have IRRs of 9% and 7%, and the cost of capital is 9.5%. Under the IRR criterion the company should undertake the project with the 9% IRR, because it ranks first.

### Answer

F

### Reasoning

Ranking is not enough: a project is accepted only if its IRR exceeds the cost of capital. Both IRRs are below 9.5%, so both NPVs at 9.5% are negative and neither project is accepted.

### Source

Examples PDF, Exercise 6 (b); 3_II_NPV IRR.pdf, Exercise 8.

## F01.4 IRR above the discount rate

- id: F01-S4
- concept_id: u3-irr-npv-relation

A project with conventional cash flows (an outlay followed by positive flows) has an IRR of 10%. If it is valued at a discount rate of 7%, its NPV is positive.

### Answer

T

### Reasoning

The NPV of such a project falls as the rate rises and is zero at the IRR. At 7%, below the 10% IRR, it is therefore positive (IRR > k).

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 6.

## F01.5 Flows after the recovery

- id: F01-S5
- concept_id: u3-payback-limits

The payback period takes into account every cash flow of the project, including those received after the initial outlay has been recovered.

### Answer

F

### Reasoning

The payback is the time it takes to recover the initial investment, so it stops counting at that moment and ignores every later flow. Two projects with the same payback can differ greatly in what they return afterwards.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercises 3 and 5 (b).

## F01.6 Fisher's rate of one project

- id: F01-S6
- concept_id: u3-fisher-rate-definition

Fisher's rate of a project is the discount rate at which the NPV of that project becomes zero.

### Answer

F

### Reasoning

That is the IRR. Fisher's rate belongs to a pair of projects: it is the discount rate at which the two NPVs are equal, and it marks where the preferred project changes.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b); Examples PDF, Exercise 5 (c).

## F01.7 The weighted average cost of capital

- id: F01-S7
- concept_id: u3-wacc-definition

The capital cost of a company is the average of the cost of its equity and the cost of its liabilities, each weighted by its share in the financial structure.

### Answer

T

### Reasoning

Topic 3 defines $K_{WACC} = K_{EQ}\,E/(E+L) + K_L\,L/(E+L)$; the key of Exercise 8 uses this weighted cost as the cut-off rate for the IRR.

### Source

Topic 3, Slide 37; 3_II_NPV_NPV IRR_solutions.pdf, Exercise 8.

## F01.8 Is equity free

- id: F01-S8
- concept_id: u3-cost-of-equity

Equity has no cost for the company, because the company does not pay interest on the funds contributed by its owners.

### Answer

F

### Reasoning

Every financial resource has a cost: liabilities have an explicit cost and equity an implicit (opportunity) cost, which enters the weighted average cost of capital.

### Source

Topic 3, Slide 37; 3_II_NPV IRR.pdf, Exercise 8 (cost of equity 15%).

## F01.9 Raising the discount rate

- id: F01-S9
- concept_id: u3-npv-rate-sensitivity

For a project made of an initial outlay followed by positive cash flows, a higher discount rate gives a lower NPV.

### Answer

T

### Reasoning

Each positive flow is divided by $(1+k)^t$, which grows with $k$, while the outlay at year 0 is not discounted; the NPV therefore decreases as the rate rises.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 6 (b); Examples PDF, Exercise 5 (c), table of NPVs at 0% and 8%.

## F01.10 Equal NPVs at a zero rate

- id: F01-S10
- concept_id: u3-fisher-rate-zero

If two projects have the same NPV at a discount rate of 0% (the same sum of net cash flows minus the outlay), then 0% is a Fisher's rate of that pair.

### Answer

T

### Reasoning

Fisher's rate is the rate at which both NPVs are equal; at 0% both NPVs equal their undiscounted sums, which are the same, so $r = 0\%$ solves the equation.

### Source

Examples PDF, Exercise 5 (c), pair A–B ($x = 1$, FR = 0%), and Exercise 6 (c).

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
