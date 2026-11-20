---
materia: Business Management
tema: "Unit 3: investment selection (NPV, IRR, payback, Fisher's rate, cost of capital)"
bank_id: B01
title: "NPV, IRR, payback and the cost of capital"
category: mt2_mcq_block
unit: 3
concepts:
  - u3-npv-calculation
  - u3-max-outlay-from-irr
  - u3-wacc-calculation
  - u3-payback-calculation
  - u3-fisher-rate-definition
  - u3-irr-below-cost-of-capital
  - u3-irr-npv-relation
  - u3-payback-limits
  - u3-ranking-conflict
  - u3-cost-of-equity
difficulty: 2
origen: "Questions written for the bank as a practice format of the portal (the examples PDF has no multiple-choice part); not official exercises. Content from 3_II_NPV IRR.pdf and its solutions (Exercises 3 to 9), Exercises 5 and 6 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf and Topic 3, Slide 37."
tags:
  - problem-bank
  - midterm-2
  - multiple-choice
  - unit-3
---

# Bank B01 — NPV, IRR, payback and the cost of capital

> [!info] Practice item, not an official exercise
> Ten multiple-choice questions written for the bank (four options, one right answer; +0.25 right, −0.08 wrong, 0 blank). The multiple-choice part is a practice format of the portal. Sources: 3_II_NPV IRR.pdf and 3_II_NPV_NPV IRR_solutions.pdf, Exercises 3 to 9; Examples PDF, Exercises 5 and 6; Topic 3, Slide 37.

## B01.1 NPV of a two-year project

- id: B01-Q1
- concept_id: u3-npv-calculation
- format: numeric
- asks: calculation
- calc: -120000+70000/1.05+80000/1.05**2

A project requires an initial outlay of 120,000 € and generates net cash flows of 70,000 € in year 1 and 80,000 € in year 2. With a yearly discount rate of 5%, its NPV is:

a) 30,000.00 €
b) 16,054.42 €
c) 19,229.02 €
d) 139,229.02 €

### Answer

c

### Explanation

Each flow is discounted to year 0 with its own exponent: $NPV = -120{,}000 + 70{,}000/1.05 + 80{,}000/1.05^2 = -120{,}000 + 66{,}666.67 + 72{,}562.36 = 19{,}229.02$ €.

- a) This is the undiscounted sum $70{,}000 + 80{,}000 - 120{,}000$, the NPV at 0%; the flows were not discounted.
- b) Both flows were divided by $1.05^2$: the year 1 flow was discounted twice instead of once.
- d) The present value of the inflows is right, but the initial outlay of 120,000 € was not subtracted.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a); Examples PDF, Exercise 5 (a).

## B01.2 Largest outlay compatible with a given IRR

- id: B01-Q2
- concept_id: u3-max-outlay-from-irr
- format: numeric
- asks: calculation
- calc: 25000*(1/1.06+1/1.06**2+1/1.06**3)

A project is expected to generate 25,000 € at the end of each of the next three years, and its estimated IRR is 6%. The maximum amount that can be invested in it at year 0 is:

a) 66,825.30 €
b) 75,000.00 €
c) 70,754.72 €
d) 62,971.45 €

### Answer

a

### Explanation

At the IRR the NPV is zero, so the outlay equals the present value of the flows at 6%: $I_0 = 25{,}000/1.06 + 25{,}000/1.06^2 + 25{,}000/1.06^3 = 23{,}584.91 + 22{,}249.91 + 20{,}990.48 = 66{,}825.30$ €.

- b) This is $3 \times 25{,}000$: the flows were added without discounting them at the IRR.
- c) The whole 75,000 € was discounted one year, as if every flow arrived at the end of year 1.
- d) The whole 75,000 € was discounted three years, as if every flow arrived at the end of year 3.

### Source

3_II_NPV IRR.pdf, Exercise 4 and its key (same method with four flows of 30,000 € at 8%).

## B01.3 Weighted average cost of capital

- id: B01-Q3
- concept_id: u3-wacc-calculation
- format: numeric
- asks: calculation
- calc: 100*(0.35*0.12+0.65*0.05)

A company is financed 35% with equity, whose cost is estimated at 12%, and 65% with liabilities, whose average cost is 5%. Its capital cost $K_{WACC}$ is:

a) 8.50%
b) 9.55%
c) 17.00%
d) 7.45%

### Answer

d

### Explanation

$K_{WACC} = K_{EQ}\,E/(E+L) + K_L\,L/(E+L) = 0.35 \times 12\% + 0.65 \times 5\% = 4.20\% + 3.25\% = 7.45\%$.

- a) This is the simple average $(12\% + 5\%)/2$; the costs were not weighted by the financial structure.
- b) The weights were swapped: $0.65 \times 12\% + 0.35 \times 5\%$ gives the equity cost the weight of the liabilities.
- c) The two costs were added, $12\% + 5\%$, which is not an average of any kind.

### Source

Topic 3, Slide 37; 3_II_NPV_NPV IRR_solutions.pdf, Exercise 8.

## B01.4 Payback with uneven flows

- id: B01-Q4
- concept_id: u3-payback-calculation
- format: numeric
- asks: calculation
- calc: 2+(90000-30000-40000)/50000

A project requires 90,000 € and generates 30,000 €, 40,000 € and 50,000 € in years 1, 2 and 3. Assuming that each flow arrives evenly during its year, its payback period is:

a) 2.25 years
b) 2.40 years
c) 2.67 years
d) 3.00 years

### Answer

b

### Explanation

After two years $30{,}000 + 40{,}000 = 70{,}000$ € are recovered; the remaining $90{,}000 - 70{,}000 = 20{,}000$ € come from the 50,000 € of year 3 after $20{,}000/50{,}000 = 0.40$ years, so the payback is 2.40 years.

- a) The outlay was divided by the average flow, $90{,}000/40{,}000$; the payback follows the cumulative flows year by year, not their average.
- c) The missing 20,000 € were divided by the year 1 flow (30,000 €) instead of the flow of year 3, the year in which the recovery happens.
- d) The recovery was rounded up to the end of year 3, ignoring that the flows arrive evenly during the year.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (b) and Exercise 9 (a) (fraction of the year in which the outlay is recovered).

## B01.5 What Fisher's rate is

- id: B01-Q5
- concept_id: u3-fisher-rate-definition
- format: identify
- asks: definition

Fisher's rate of two investment projects is:

a) The discount rate at which the NPV of each project is zero
b) The weighted average of the costs of equity and liabilities of the company
c) The discount rate at which both projects have the same NPV
d) The discount rate at which each project recovers its initial outlay

### Answer

c

### Explanation

The key of Exercise 9 obtains Fisher's rate from $NPV_A = NPV_B$; it is the rate at which the NPV profiles of the two projects cross, so the preferred project changes there.

- a) The rate that makes the NPV of one project zero is its IRR, a property of a single project, not of a pair.
- b) This is the capital cost $K_{WACC}$ of Slide 37, a property of the company's financing, not of two projects.
- d) The time in which a project recovers its outlay is the payback period, which is measured in years, not a discount rate.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b); Examples PDF, Exercise 5 (c).

## B01.6 Both IRRs below the cost of capital

- id: B01-Q6
- concept_id: u3-irr-below-cost-of-capital
- format: what-happens
- asks: application

Two mutually exclusive projects have IRRs of 9.2% (project A) and 8.4% (project B). The company's cost of capital is 9.5%. Under the IRR criterion, the company should:

a) Undertake A, because it has the higher IRR
b) Undertake both, because both IRRs are positive
c) Undertake B, because its outlay is recovered with a lower rate
d) Reject both, because both IRRs are below the cost of capital

### Answer

d

### Explanation

A project is accepted only when its IRR exceeds the cost of capital; here $9.2\% < 9.5\%$ and $8.4\% < 9.5\%$, so both NPVs at 9.5% are negative and neither project is undertaken, whatever their ranking.

- a) Ranking A above B is correct, but ranking alone does not make A acceptable: its IRR is still below the 9.5% cut-off rate.
- b) A positive IRR is not the acceptance condition; the IRR must exceed the cost of capital, and the projects are mutually exclusive anyway.
- c) A lower IRR makes a project less attractive, not more: this inverts the meaning of the IRR.

### Source

Examples PDF, Exercise 6 (b); 3_II_NPV IRR.pdf, Exercise 8.

## B01.7 Effect of a higher discount rate

- id: B01-Q7
- concept_id: u3-irr-npv-relation
- format: cause-effect
- asks: effect

A project made of an initial outlay followed by positive flows has an IRR of 12% and has been valued at 6%. If the discount rate is raised to 9%, its NPV:

a) Decreases, but remains positive
b) Increases, because the project earns more than 9%
c) Becomes negative, because the rate has risen
d) Does not change, because the IRR does not depend on the rate

### Answer

a

### Explanation

The NPV of such a project falls as the rate rises, so it is lower at 9% than at 6%; since 9% is still below the 12% IRR, at which the NPV is zero, it remains positive. The key of Exercise 6 reasons the same way for rates of 7% and 9% with an IRR of 10%.

- b) A higher rate divides every future flow by a larger factor $(1+k)^t$, so the NPV cannot increase.
- c) The NPV becomes negative only when the rate exceeds the IRR (12%), not as soon as it rises.
- d) The IRR itself does not change, but the NPV is evaluated at the discount rate and does change with it.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 6 (b).

## B01.8 A false statement about payback

- id: B01-Q8
- concept_id: u3-payback-limits
- format: false-statement
- asks: comparison

Which one of the following statements about the payback period is FALSE:

a) It is the time it takes to recover the initial investment from the project's cash flows
b) Of two projects, the one with the shorter payback always has the higher NPV
c) It does not take into account the cash flows received after the outlay is recovered
d) A project accepted under a maximum payback of three years may have a negative NPV

### Answer

b

### Explanation

Payback and NPV can rank projects differently. In Exercise 9 of the sheet project B has the shorter payback (about 11 months against 1 year and 9 months), yet above Fisher's rate of about 5% project A has the higher NPV.

- a) True: this is the definition used in the key of Exercise 5 (b), so it is not the false statement asked for.
- c) True: payback stops counting when the outlay is recovered, which is why it ignores later flows; not the false one.
- d) True: in Exercise 5 project A has a payback of one year and an NPV of −90.91 € at 10%, so this statement is not false.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercises 5 and 9.

## B01.9 IRR ranking against NPV at the cost of capital

- id: B01-Q9
- concept_id: u3-ranking-conflict
- format: identify
- asks: application

Two mutually exclusive projects: A has an IRR of 14% and B an IRR of 11%; B has the larger NPV at 0%, and their Fisher's rate is 7%. The company uses the NPV criterion with a cost of capital of 5%. It should choose:

a) A, because it has the higher IRR
b) Neither, because the IRRs disagree with the NPV at 0%
c) Both, because both IRRs exceed 5%
d) B, because below the Fisher's rate B has the higher NPV

### Answer

d

### Explanation

The two NPV profiles cross only at Fisher's rate (7%). At 0% B has the larger NPV, so B stays above A for every rate below 7%; at 5% the NPV criterion chooses B, even though A has the higher IRR.

- a) The IRR ranking holds only above Fisher's rate; at 5% it disagrees with the NPV ranking, and the company decides by NPV.
- b) A disagreement between rankings does not make the projects unacceptable: both IRRs exceed 5%, so both NPVs are positive.
- c) The projects are mutually exclusive, so only one of them can be undertaken even if both are acceptable.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b); Examples PDF, Exercise 5 (c).

## B01.10 The cost of each financial resource

- id: B01-Q10
- concept_id: u3-cost-of-equity
- format: complete-sentence
- asks: definition

In the capital cost of the company, equity has ... cost and liabilities have ... cost:

a) an implicit (opportunity) ... an explicit
b) no ... an explicit
c) an explicit ... an implicit (opportunity)
d) an explicit ... no

### Answer

a

### Explanation

Slide 37 states that every financial resource has a cost: equity has an implicit (opportunity) cost and liabilities an explicit cost (the interest), and both enter the weighted average $K_{WACC}$.

- b) Equity is not free: the owners give up other uses of their funds, which is its opportunity cost.
- c) The two kinds of cost were swapped: interest on liabilities is the explicit one.
- d) Liabilities do carry a cost (their interest), and equity's cost is not explicit but implicit.

### Source

Topic 3, Slide 37.

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
