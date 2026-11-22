---
materia: Business Management
tema: "Unit 3: investment selection (three-year NPV, two-year IRR, Fisher's rate, WACC, decision intervals)"
bank_id: B06
title: "Two-year IRR, Fisher's rate and decision intervals"
category: mt2_mcq_block
unit: 3
concepts:
  - u3-npv-three-year
  - u3-irr-two-year-quadratic
  - u3-fisher-rate-calculation
  - u3-wacc-from-balance-sheet
  - u3-max-outlay-npv
  - u3-timing-of-flows
  - u3-payback-negative-flow
  - u3-exclusive-vs-independent
  - u3-no-project-rate
  - u3-conflict-cause
difficulty: 2
origen: "Questions written for the bank as a practice format of the portal (the examples PDF has no multiple-choice part); not official exercises. Content from 3_II_NPV IRR.pdf and its solutions (Exercises 2, 3, 5, 7, 8 and 9), Exercises 5 and 6 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf and Topic 3, Slide 37."
tags:
  - problem-bank
  - midterm-2
  - multiple-choice
  - unit-3
---

# Bank B06 — Two-year IRR, Fisher's rate and decision intervals

> [!info] Practice item, not an official exercise
> Ten multiple-choice questions written for the bank (four options, one right answer; +0.25 right, −0.08 wrong, 0 blank). The multiple-choice part is a practice format of the portal. Sources: 3_II_NPV IRR.pdf and 3_II_NPV_NPV IRR_solutions.pdf, Exercises 2, 3, 5, 7, 8 and 9; Examples PDF, Exercises 5 and 6; Topic 3, Slide 37.

## B06.1 NPV of a three-year project

- id: B06-Q1
- concept_id: u3-npv-three-year
- format: numeric
- asks: calculation
- calc: -50000+20000/1.06+25000/1.06**2+15000/1.06**3

An avionics test bench costs 50,000 € today and will bring in 20,000 € at the end of year 1, 25,000 € at the end of year 2 and a final 15,000 € at the end of year 3, after which it is scrapped with no further flows. Valued at 6% a year, the bench is worth today, net of its cost:

a) 10,000.00 €
b) 3,712.12 €
c) 6,603.77 €
d) 4,467.78 €

### Answer

b

### Explanation

Each flow is discounted with the exponent of its own year: $NPV = -50{,}000 + 20{,}000/1.06 + 25{,}000/1.06^2 + 15{,}000/1.06^3 = -50{,}000 + 18{,}867.92 + 22{,}249.91 + 12{,}594.29 = 3{,}712.12$ €.

- a) This is $20{,}000 + 25{,}000 + 15{,}000 - 50{,}000$, the NPV at 0%: none of the flows was discounted.
- c) The whole 60,000 € was discounted one year, as if every flow arrived at the end of year 1.
- d) The year 3 flow was divided by $1.06^2$ instead of $1.06^3$, so it was discounted one year too few.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a); Examples PDF, Exercise 5 (a).

## B06.2 IRR of a two-year project

- id: B06-Q2
- concept_id: u3-irr-two-year-quadratic
- format: numeric
- asks: calculation
- calc: 100*((150000+sqrt(150000**2+4*400000*330000))/(2*400000)-1)

A project requires 400,000 € and generates 150,000 € in year 1 and 330,000 € in year 2. Its IRR is:

a) 20.00%
b) 10.00%
c) 9.54%
d) 11.49%

### Answer

d

### Explanation

With $x = 1 + r$, $-400{,}000 + 150{,}000/x + 330{,}000/x^2 = 0$ becomes $400{,}000x^2 - 150{,}000x - 330{,}000 = 0$, so $x = \left(150{,}000 + \sqrt{150{,}000^2 + 4 \times 400{,}000 \times 330{,}000}\right)/800{,}000 = (150{,}000 + 741{,}956.87)/800{,}000 = 1.1149$ and the IRR is 11.49%.

- a) This is $(480{,}000 - 400{,}000)/400{,}000$, the undiscounted gain over the outlay; it ignores that the flows arrive over two years.
- b) The 20% gain was spread evenly over the two years, a simple average that does not cancel the NPV.
- c) Both flows were treated as if they arrived in year 2, $x^2 = 480{,}000/400{,}000$, which discounts the year 1 flow one year too many.

### Source

Examples PDF, Exercise 5 (b) and Exercise 6 (b) (quadratic in $x = 1 + r$).

## B06.3 Fisher's rate of two two-year projects

- id: B06-Q3
- concept_id: u3-fisher-rate-calculation
- format: numeric
- asks: calculation
- calc: 100*((-50000+sqrt(50000**2+4*100000*160000))/(2*100000)-1)

Project A requires 300,000 € and generates 100,000 € and 260,000 € in years 1 and 2; project B requires 200,000 € and generates 150,000 € and 100,000 €. Their Fisher's rate is:

a) 3.94%
b) 11.24%
c) 53.94%
d) 17.54%

### Answer

a

### Explanation

Equating the NPVs with $x = 1 + r$: $-300{,}000 + 100{,}000/x + 260{,}000/x^2 = -200{,}000 + 150{,}000/x + 100{,}000/x^2$. Multiplying by $x^2$ and grouping gives $100{,}000x^2 + 50{,}000x - 160{,}000 = 0$, so $x = \left(-50{,}000 + \sqrt{50{,}000^2 + 4 \times 100{,}000 \times 160{,}000}\right)/200{,}000 = (-50{,}000 + 257{,}875.94)/200{,}000 = 1.0394$, a Fisher's rate of 3.94% (both NPVs are then 36,882.86 €).

- b) This is the IRR of project A ($300{,}000x^2 - 100{,}000x - 260{,}000 = 0$), where its own NPV is zero, not the rate where the two NPVs are equal.
- c) The sign of the $x$ term was lost when grouping, $100{,}000x^2 - 50{,}000x - 160{,}000 = 0$, which gives $x = 1.5394$.
- d) This is the IRR of project B ($200{,}000x^2 - 150{,}000x - 100{,}000 = 0$), a property of one project, not of the pair.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b); Examples PDF, Exercise 5 (c), pairs A–C and B–C.

## B06.4 Capital cost from the balance sheet

- id: B06-Q4
- concept_id: u3-wacc-from-balance-sheet
- format: numeric
- asks: calculation
- calc: 100*((6+4.8)/18*0.14+7.2/18*0.06)

A company is financed with capital of 6,000,000 €, reserves of 4,800,000 € and debt of 7,200,000 €. The cost of its equity is estimated at 14% and the average cost of its debt at 6%. Its capital cost $K_{WACC}$ is:

a) 8.67%
b) 10.00%
c) 10.80%
d) 9.20%

### Answer

c

### Explanation

Equity is capital plus reserves, $6{,}000{,}000 + 4{,}800{,}000 = 10{,}800{,}000$ €, that is $10.8/18 = 60\%$ of the 18,000,000 € of funds, and debt is 40%. Then $K_{WACC} = 0.60 \times 14\% + 0.40 \times 6\% = 8.40\% + 2.40\% = 10.80\%$.

- a) The reserves were left out of equity, so equity weighed $6/18$ and debt $12/18$; reserves are retained profit and belong to equity.
- b) This is the simple average $(14\% + 6\%)/2$; the costs were not weighted by the financial structure.
- d) The weights were swapped, $0.40 \times 14\% + 0.60 \times 6\%$, giving equity the weight of the debt.

### Source

Topic 3, Slide 37; 3_II_NPV_NPV IRR_solutions.pdf, Exercise 2 (equity = capital + reserves) and Exercise 8.

## B06.5 The largest outlay worth paying

- id: B06-Q5
- concept_id: u3-max-outlay-npv
- format: identify
- asks: definition

A company discounts at a rate $k$ and is offered a project with known flows over a few years and an outlay still to be negotiated. The maximum outlay for which the project is interesting (NPV ≥ 0) is:

a) The present value of its future cash flows discounted at $k$
b) The sum of its future cash flows, without discounting
c) The present value of its future cash flows discounted at its IRR
d) Its year 1 cash flow divided by $k$, as if that flow were a perpetuity

### Answer

a

### Explanation

Writing the outlay as an unknown $X$, $NPV = -X + \sum_t Q_t/(1+k)^t \geq 0$ holds while $X$ does not exceed the present value of the flows at $k$; this is how the key of the examples finds $X \leq 706{,}447.19$ for project B at 8%.

- b) The undiscounted sum is the limit only at a rate of 0%; at any positive $k$ it overstates what the project is worth today.
- c) The IRR depends on the outlay that is still unknown, so it cannot fix it; and the decision is taken at the company's rate $k$, not at the IRR.
- d) The flows last a finite number of years; dividing one flow by $k$ values an endless stream that the project does not provide.

### Source

Examples PDF, Exercise 5 (a) and Exercise 6 (a).

## B06.6 Same outlay, same total, different timing

- id: B06-Q6
- concept_id: u3-timing-of-flows
- format: cause-effect
- asks: comparison

Projects A and B both require 100,000 €. A generates 90,000 €, 40,000 € and 20,000 € in years 1 to 3; B generates 20,000 €, 40,000 € and 90,000 €. At a discount rate of 8%:

a) Both have the same NPV, because their undiscounted flows add up to the same total
b) A has the higher NPV, because its largest flow is discounted over fewer years
c) B has the higher NPV, because its largest flow arrives at the end
d) They cannot be compared by NPV, only by the payback period

### Answer

b

### Explanation

The factor $(1+k)^t$ grows with the year, so a large flow received early loses less value. At 8%, $NPV_A = 33{,}503.53$ € and $NPV_B = 24{,}256.97$ €: A is ahead although both totals are 150,000 €.

- a) The totals are equal only before discounting; at 8% each flow is divided by a different factor, so the NPVs differ.
- c) Receiving the largest flow later lowers its present value, it does not raise it: this inverts the effect of discounting.
- d) The NPV compares any two projects at a given rate; the payback ignores discounting and is the weaker tool here.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 5 (a); Examples PDF, Exercise 5 (c).

## B06.7 Payback with a negative year 1

- id: B06-Q7
- concept_id: u3-payback-negative-flow
- format: what-happens
- asks: application

A project requires 1,200 and generates −200, 300, 500, 200, 400 and 400 in years 1 to 6. Under the payback criterion:

a) It cannot be assessed, because one of its flows after year 0 is negative
b) The negative flow is ignored and the outlay is recovered in year 4
c) The negative flow is added to the outlay and the outlay is never recovered
d) Its cumulative flows must first offset the year 1 deficit, and the outlay is recovered at the end of year 5

### Answer

d

### Explanation

The cumulative flows are −200, 100, 600, 800 and 1,200, so the 1,200 is recovered exactly at the end of year 5, the payback of project X in the key of Exercise 3.

- a) A negative flow does not stop the method; it only delays the recovery, and the key computes a payback of 5 years.
- b) Dropping the −200 gives cumulative flows 300, 800, 1,000, 1,400 and a recovery during year 4, which overstates how fast the money comes back.
- c) Adding the −200 to the outlay is correct (1,400 to recover), but the later flows add up to 1,800, so the recovery still happens, at the end of year 5.

### Source

3_II_NPV IRR.pdf, Exercise 3, and its key (Payback X = 5 years).

## B06.8 Independent or mutually exclusive

- id: B06-Q8
- concept_id: u3-exclusive-vs-independent
- format: identify
- asks: comparison

Three projects have IRRs of 14% (A), 11% (B) and 9% (C), and the cost of capital is 10%. The NPV profiles of A and B cross at a Fisher's rate of 12%, with B having the larger NPV at 0%. Which projects does the company undertake if they are independent, and which if they are mutually exclusive?

a) Independent: A only; mutually exclusive: A
b) Independent: A, B and C; mutually exclusive: A
c) Independent: A and B; mutually exclusive: B
d) Independent: A and B; mutually exclusive: A

### Answer

c

### Explanation

Independent projects are accepted whenever their IRR exceeds 10% (positive NPV): A and B, not C. If only one can be accepted, the choice is the higher NPV at 10%; since 10% is below the Fisher's rate of 12% and B leads at 0%, B's profile is still above A's at 10%, so B is chosen.

- a) B also has an IRR above the 10% cost of capital, so as an independent project it is accepted too.
- b) C has an IRR of 9%, below 10%, so its NPV is negative and it is rejected even if independent.
- d) Choosing A follows the IRR ranking, which holds only above the 12% Fisher's rate; at 10% B has the higher NPV.

### Source

Examples PDF, Exercises 5 and 6 (mutually exclusive projects, Fisher's rates); 3_II_NPV_NPV IRR_solutions.pdf, Exercises 7 and 8.

## B06.9 Decision intervals of two projects

- id: B06-Q9
- concept_id: u3-no-project-rate
- format: identify
- asks: application

Two mutually exclusive projects: P has an IRR of 9% and Q an IRR of 13%; P has the larger NPV at 0%, and their Fisher's rate is 4%. For which discount rates does the company choose Q, and above which rate does it choose no project?

a) Q for rates between 4% and 13%; no project above 13%
b) Q for rates below 4%; no project above 9%
c) Q for rates between 9% and 13%; no project above 13%
d) Q for rates between 4% and 9%; no project above 9%

### Answer

a

### Explanation

P leads below the 4% crossing, Q leads above it; Q keeps a positive NPV up to its IRR of 13%, while P's NPV is already negative above 9%. Above 13% both NPVs are negative, so no project is chosen, as in the conclusions of Exercises 5 and 6 of the examples.

- b) Below 4% the project with the larger NPV at 0% leads, which is P, not Q; and Q still has a positive NPV between 9% and 13%.
- c) Q is already above P from the 4% crossing; it does not wait until P's NPV becomes negative at 9%.
- d) Above 9% only P becomes unacceptable; Q stays positive up to its own IRR of 13%, so it is still chosen there.

### Source

Examples PDF, Exercise 5 (c) and Exercise 6 (c), conclusions.

## B06.10 Why the two criteria disagree

- id: B06-Q10
- concept_id: u3-conflict-cause
- format: cause-effect
- asks: cause

At the company's rate of 5%, project A (IRR 15%) has a lower NPV than project B (IRR 11%), although both are acceptable. The reason is that:

a) One of the IRRs must be wrong, because NPV and IRR always rank projects alike
b) The discount rate lies below the Fisher's rate of the pair, where B's profile is still above A's
c) A's IRR exceeds the discount rate by more, so A's NPV must be negative
d) The NPV ignores the flows received after the outlay is recovered

### Answer

b

### Explanation

The IRR ranking describes the profiles where they cut the horizontal axis; the NPV ranking at 5% describes them at 5%. If the profiles cross at a Fisher's rate above 5%, B is above A to the left of the crossing and A above B to the right, so the two criteria disagree at 5%, as in Exercise 9 of the sheet below its Fisher's rate of about 5%.

- a) The rankings can legitimately differ: they agree only on the side of the Fisher's rate where the higher-IRR project leads.
- c) An IRR above the discount rate means a positive NPV, not a negative one; both projects are acceptable at 5%.
- d) Ignoring the flows after the recovery is the limitation of the payback, not of the NPV, which counts every flow.

### Source

3_II_NPV_NPV IRR_solutions.pdf, Exercise 9 (b); Examples PDF, Exercise 5 (c).

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
