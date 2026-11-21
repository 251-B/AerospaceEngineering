---
materia: Business Management
tema: "Unit 3: investment selection"
bank_id: M06
title: "Corvus Flight Simulators: payback against NPV under a budget limit"
category: mt2_problem
archetype: npv-irr-fisher
level: standard
unit: 3
difficulty: 2
points: 2.5
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Exercises 5 and 6 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not an official exercise. Payback with 30-day months as in 3_II_NPV IRR.pdf, Exercises 3, 5 and 9; selection of independent projects with a budget as in Exercise 7 of the same sheet; IRR and Fisher's rate as in Exercise 9."
tags:
  - problem-bank
  - midterm-2
  - npv-irr-fisher
  - payback
  - budget
  - fisher-rate
---

# Bank M06 — Corvus Flight Simulators: payback against NPV under a budget limit

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercises 5 (SunTech Energy) and 6 (GreenWave Solutions) of the examples PDF. The company and its figures are invented. The twist: four independent projects compete for a limited budget; the ranking by payback and the ranking by NPV disagree, a project that passes the payback rule destroys value, and a cut in the budget turns the choice into one among mutually exclusive projects. Method: Examples PDF, Exercises 5 and 6; 3_II_NPV IRR.pdf, Exercises 3, 5, 7 and 9.

## Statement

Corvus Flight Simulators builds full-flight simulators for airline training centres. For next year its board has received four proposals, which are independent of each other, cannot be split and cannot be repeated. Each one lasts two years:

- Project A, a motion-platform retrofit kit, costs 400,000 € today and brings in 380,000 € at the end of the first year and 100,000 € at the end of the second.
- Project B, a new simulator for a wide-body aircraft type, costs 600,000 €; it returns only 90,000 € in year 1, while the certification is completed, and 680,000 € in year 2.
- Project C, a visual-system upgrade for the existing fleet, costs 300,000 € and returns 60,000 € in year 1 and 300,000 € in year 2.
- Project D, a refurbished-simulator resale deal, costs 200,000 € and returns 180,000 € in year 1 and 30,000 € in year 2.

The shareholders require a yearly return of 8% on every project. Until now the board has accepted any project that recovers its outlay in at most 1 year and 9 months, and it has 900,000 € available to invest.

a) Compute the payback period of the four projects (in years, months and days, with 30-day months and the flows spread evenly over each year), rank them, and say which ones the board's payback rule accepts. (0.5 points)

b) Compute the NPV of the four projects at 8% and rank them. Which projects create value? Comment on the projects for which the payback rule and the NPV give opposite answers. (0.5 points)

c) The board proposes to use the 900,000 € by taking the projects in order of shortest payback while they still fit in the budget. Which projects would it undertake, and what total NPV would it obtain? Which set of projects maximises the total NPV within the budget? (0.5 points)

d) Compute the IRR of the four projects and compare the IRR ranking of A, B and C with their NPV ranking at 8%. Draw a schematic graph of the NPV of A, B and C as a function of the discount rate. (0.5 points)

e) The budget is finally cut to 600,000 €, so only one of A, B and C can be undertaken. Compute Fisher's rates of the pairs A–B, A–C and B–C, state which project would be chosen depending on the discount rate and from which rate none would be chosen, and give the choice at 8%. (0.5 points)

## Setup

#### Data

| Project | Initial outlay $A$ (€) | $Q_1$ (€) | $Q_2$ (€) |
| :--- | ---: | ---: | ---: |
| A | 400,000 | 380,000 | 100,000 |
| B | 600,000 | 90,000 | 680,000 |
| C | 300,000 | 60,000 | 300,000 |
| D | 200,000 | 180,000 | 30,000 |

Required return $k$ = 8% a year; budget 900,000 € (600,000 € in part (e)); payback cut-off 1 year and 9 months.

#### Model

- **Payback** (3_II_NPV IRR.pdf, Exercises 3 and 9): the time the cumulative flows take to equal the outlay. When the outlay is recovered during year 2, the payback is $1 + (A - Q_1)/Q_2$ years; the fraction of a year times 12 gives the months, and the fraction of a month times 30 gives the days. The shorter, the better; it ignores the time value of money and every flow after the recovery.
- **Net present value** (Examples PDF, Exercise 5): with outlay $A$, flows $Q_t$ and discount rate $k$,
$$NPV = -A + \frac{Q_1}{1+k} + \frac{Q_2}{(1+k)^2}$$
A project creates value when $NPV > 0$. With a budget and independent, indivisible projects, the set chosen is the one with the largest total NPV that fits in the budget (3_II_NPV IRR.pdf, Exercise 7).
- **Internal rate of return**: the rate $r$ at which $NPV = 0$ (3_II_NPV_NPV IRR_solutions.pdf, Exercise 4). With $x = 1 + r$ and multiplying by $x^2 > 0$, $NPV = 0$ becomes $A\,x^2 - Q_1\,x - Q_2 = 0$, solved with $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$; only the root with $x > 0$ has economic meaning.
- **Fisher's rate** of a pair: the rate at which both NPVs are equal (3_II_NPV_NPV IRR_solutions.pdf, Exercise 9). Multiplying $NPV_P = NPV_Q$ by $x^2$ gives a quadratic in $x$ (Examples PDF, Exercise 5 (c)).
- Hypotheses: flows at the end of each year for the NPV and spread evenly over the year for the payback, a constant yearly rate, no taxes and no residual value.

## (a) Payback periods and the board's rule [0.5 pts]

### Hint

Each project recovers part of its outlay in year 1; divide what is still missing by the flow of year 2 to get the fraction of the second year.

### Checkpoint

- A: 1.2 years = 1 year, 2 months and 12 days; D: 1.6667 years = 1 year and 8 months; B: 1.75 years = 1 year and 9 months; C: 1.8 years = 1 year, 9 months and 18 days.
- Ranking: A, D, B, C. The rule (at most 1 year and 9 months) accepts A, D and B and rejects C.

### Solution

#### Amount still missing after year 1

No project recovers its outlay in year 1, so each one finishes the recovery during year 2:

| Project | Outlay (€) | Recovered in year 1 (€) | Missing (€) | $Q_2$ (€) | Fraction of year 2 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| A | 400,000 | 380,000 | 20,000 | 100,000 | 20,000 / 100,000 = 0.2 |
| B | 600,000 | 90,000 | 510,000 | 680,000 | 510,000 / 680,000 = 0.75 |
| C | 300,000 | 60,000 | 240,000 | 300,000 | 240,000 / 300,000 = 0.8 |
| D | 200,000 | 180,000 | 20,000 | 30,000 | 20,000 / 30,000 = 0.6667 |

#### Years, months and days

- A: 0.2 years × 12 = 2.4 months, and 0.4 months × 30 = 12 days: **1 year, 2 months and 12 days**.
- D: 0.6667 years × 12 = 8 months exactly: **1 year and 8 months**.
- B: 0.75 years × 12 = 9 months exactly: **1 year and 9 months**.
- C: 0.8 years × 12 = 9.6 months, and 0.6 months × 30 = 18 days: **1 year, 9 months and 18 days**.

#### Ranking and the cut-off

By payback the order is **A, D, B, C**. The board's rule accepts the projects that recover their outlay in at most 1 year and 9 months: **A, D and B** (B exactly at the limit); **C is rejected**.

## (b) NPV at 8% and the conflict with payback [0.5 pts]

### Hint

The discount factors are $1.08$ and $1.08^2 = 1.1664$. Write both discounted flows of each project before adding them.

### Checkpoint

- $NPV_A$ = 37,585.73 €; $NPV_B$ = 66,323.73 €; $NPV_C$ = 12,757.20 €; $NPV_D$ = −7,613.17 €.
- Ranking by NPV: B, A, C, D. A, B and C create value; D destroys value although it passes the payback rule; C creates value although the rule rejects it.

### Solution

#### NPV of each project

$$NPV_A = -400{,}000 + \frac{380{,}000}{1.08} + \frac{100{,}000}{1.1664} = -400{,}000 + 351{,}851.852 + 85{,}733.882 = 37{,}585.73\ \text{€}$$

$$NPV_B = -600{,}000 + \frac{90{,}000}{1.08} + \frac{680{,}000}{1.1664} = -600{,}000 + 83{,}333.333 + 582{,}990.398 = 66{,}323.73\ \text{€}$$

$$NPV_C = -300{,}000 + \frac{60{,}000}{1.08} + \frac{300{,}000}{1.1664} = -300{,}000 + 55{,}555.556 + 257{,}201.646 = 12{,}757.20\ \text{€}$$

$$NPV_D = -200{,}000 + \frac{180{,}000}{1.08} + \frac{30{,}000}{1.1664} = -200{,}000 + 166{,}666.667 + 25{,}720.165 = -7{,}613.17\ \text{€}$$

Units: each term is an amount in € divided by a dimensionless factor $(1.08)^t$, so every NPV is in €.

#### Ranking and the two conflicts

By NPV the order is **B, A, C, D**: A, B and C create value, D does not.

- **D** is second by payback and passes the rule, yet its NPV is negative. Its flows add up to 210,000 €, only 10,000 € more than the outlay, and that margin does not cover the 8% the shareholders require over two years. Payback only checks that the money comes back quickly, not that it comes back with its cost.
- **C** is rejected by the rule because it recovers its outlay 18 days too late, yet its NPV is positive: payback ignores that the 300,000 € of year 2 more than pay for the wait.
- **B**, last but one by payback, has the largest NPV: its large flow arrives late, which payback penalises and the NPV only discounts.

## (c) Filling the budget: payback order against NPV [0.5 pts]

### Hint

Go down the payback ranking of (a) and skip a project that no longer fits. Then list every combination that costs at most 900,000 € and add the NPVs of (b).

### Checkpoint

- Payback order: A (400,000 €), D (600,000 € in total), B does not fit (1,200,000 €), C (900,000 €): A + C + D, total NPV 42,729.76 €.
- Best set within 900,000 €: B + C, total NPV 79,080.93 €, 36,351.17 € more.

### Solution

#### The board's proposal

Taking the projects in the order of (a): A uses 400,000 €; D brings the total to 600,000 €; B would bring it to 1,200,000 €, above the budget, so it is skipped; C brings the total to exactly 900,000 €. The board would undertake **A, C and D**, with a total NPV of

$$37{,}585.73 + 12{,}757.20 - 7{,}613.17 = 42{,}729.76\ \text{€}$$

#### Every combination that fits

| Set | Outlay (€) | Total NPV at 8% (€) |
| :--- | ---: | ---: |
| B + C | 900,000 | 66,323.73 + 12,757.20 = 79,080.93 |
| B + D | 800,000 | 66,323.73 − 7,613.17 = 58,710.56 |
| A + C | 700,000 | 37,585.73 + 12,757.20 = 50,342.93 |
| A + C + D | 900,000 | 42,729.76 |
| A + D | 600,000 | 37,585.73 − 7,613.17 = 29,972.56 |
| C + D | 500,000 | 12,757.20 − 7,613.17 = 5,144.03 |

A + B costs 1,000,000 € and any set of three with B costs at least 1,100,000 €, so none of them fits. No single project beats B + C either, since the best one, B, has 66,323.73 €.

#### The set that maximises the NPV

The company should undertake **B and C**, with a total NPV of **79,080.93 €**, which uses the whole budget. The same set comes out of the NPV ranking of (b): B first, A skipped because A + B does not fit, then C. The payback order loses $79{,}080.93 - 42{,}729.76 = 36{,}351.17$ €, because it spends 200,000 € on D, which destroys value, and leaves out B, the project that creates the most.

## (d) IRR of the projects and the NPV profiles [0.5 pts]

### Hint

For each project write $A\,x^2 - Q_1\,x - Q_2 = 0$ with $x = 1 + r$, divide by a common factor and keep the positive root.

### Checkpoint

- IRR(A) = 16.47%; IRR(B) = 14.22%; IRR(C) = 10.50%; IRR(D) = 4.37%.
- IRR ranking A, B, C against NPV ranking at 8% B, A, C: A and B swap places. D is the only IRR below 8%, consistent with its negative NPV.
- NPV at 0%: A 80,000 €, B 170,000 €, C 60,000 €.

### Solution

#### IRR of A

$$400{,}000\,x^2 - 380{,}000\,x - 100{,}000 = 0 \quad\xrightarrow{\ \div 20{,}000\ }\quad 20x^2 - 19x - 5 = 0$$

$$x = \frac{19 \pm \sqrt{(-19)^2 - 4 \cdot 20 \cdot (-5)}}{2 \cdot 20} = \frac{19 \pm \sqrt{361 + 400}}{40} = \frac{19 \pm \sqrt{761}}{40} = \frac{19 \pm 27.58623}{40}$$

The positive root is $x = 1.164656$ (the other, $-0.214656$, is rejected): **IRR(A) = 16.47%**.

#### IRR of B

$$600{,}000\,x^2 - 90{,}000\,x - 680{,}000 = 0 \quad\xrightarrow{\ \div 10{,}000\ }\quad 60x^2 - 9x - 68 = 0$$

$$x = \frac{9 \pm \sqrt{(-9)^2 - 4 \cdot 60 \cdot (-68)}}{2 \cdot 60} = \frac{9 \pm \sqrt{81 + 16{,}320}}{120} = \frac{9 \pm \sqrt{16{,}401}}{120} = \frac{9 \pm 128.06639}{120}$$

The positive root is $x = 1.142220$ (the other, $-0.992220$, is rejected): **IRR(B) = 14.22%**.

#### IRR of C

$$300{,}000\,x^2 - 60{,}000\,x - 300{,}000 = 0 \quad\xrightarrow{\ \div 60{,}000\ }\quad 5x^2 - x - 5 = 0$$

$$x = \frac{1 \pm \sqrt{(-1)^2 - 4 \cdot 5 \cdot (-5)}}{2 \cdot 5} = \frac{1 \pm \sqrt{1 + 100}}{10} = \frac{1 \pm \sqrt{101}}{10} = \frac{1 \pm 10.04988}{10}$$

The positive root is $x = 1.104988$ (the other, $-0.904988$, is rejected): **IRR(C) = 10.50%**.

#### IRR of D

$$200{,}000\,x^2 - 180{,}000\,x - 30{,}000 = 0 \quad\xrightarrow{\ \div 10{,}000\ }\quad 20x^2 - 18x - 3 = 0$$

$$x = \frac{18 \pm \sqrt{(-18)^2 - 4 \cdot 20 \cdot (-3)}}{2 \cdot 20} = \frac{18 \pm \sqrt{324 + 240}}{40} = \frac{18 \pm \sqrt{564}}{40} = \frac{18 \pm 23.74868}{40}$$

The positive root is $x = 1.043717$ (the other, $-0.143717$, is rejected): **IRR(D) = 4.37%**, below the 8% required, which agrees with $NPV_D < 0$ in (b).

#### The two rankings

By IRR the order of the value-creating projects is **A, B, C** ($16.47\% > 14.22\% > 10.50\%$); by NPV at 8% it is **B, A, C**. A and B swap places because B is larger and receives most of its money in year 2: at a low rate its NPV is the higher one, but it falls faster as the rate rises. All three IRRs exceed 8%, so for independent projects with enough money both criteria accept A, B and C.

#### Points of the profiles

At $r = 0$ the NPV is the sum of the flows minus the outlay:

$$NPV_A(0) = -400{,}000 + 380{,}000 + 100{,}000 = 80{,}000\ \text{€}$$

$$NPV_B(0) = -600{,}000 + 90{,}000 + 680{,}000 = 170{,}000\ \text{€}$$

$$NPV_C(0) = -300{,}000 + 60{,}000 + 300{,}000 = 60{,}000\ \text{€}$$

| Project | NPV at 0% (€) | NPV at 8% (€) | IRR |
| :--- | ---: | ---: | ---: |
| A | 80,000.00 | 37,585.73 | 16.47% |
| B | 170,000.00 | 66,323.73 | 14.22% |
| C | 60,000.00 | 12,757.20 | 10.50% |

Each profile starts at its NPV at 0%, decreases as the rate rises, cuts the horizontal axis at its IRR and tends to minus the outlay for very large rates. B starts far above the others and falls steeply; A starts lower but is flatter, because 380,000 € of its flows arrive in year 1. D is left out of the graph: it is rejected at 8%.

![[attachments/BM-MT2/m06-npv-profile.svg]]

## (e) One project only: Fisher's rates and decision intervals [0.5 pts]

### Hint

Equate the NPVs of each pair, multiply by $x^2$ and solve. A root outside the range of rates where the projects have a positive NPV does not change the decision; check which project is ahead at $r = 0$.

### Checkpoint

- FR(A–B) = 12.58%; A–C: no crossing between 0% and the IRRs (the roots give −14.83% and 134.83%), A is always above C; FR(B–C) = 17.66%, where both NPVs are already negative.
- $0 \leq r < 12.58\%$: B; $12.58\% < r < 16.47\%$: A; $r > 16.47\%$: no project. C is never chosen.
- At 8%: project B.

### Solution

#### Fisher's rate A–B

$$-400{,}000\,x^2 + 380{,}000\,x + 100{,}000 = -600{,}000\,x^2 + 90{,}000\,x + 680{,}000$$

Moving every term to the left: $200{,}000\,x^2 + 290{,}000\,x - 580{,}000 = 0$; dividing by 10,000, $20x^2 + 29x - 58 = 0$:

$$x = \frac{-29 \pm \sqrt{29^2 - 4 \cdot 20 \cdot (-58)}}{2 \cdot 20} = \frac{-29 \pm \sqrt{841 + 4{,}640}}{40} = \frac{-29 \pm \sqrt{5{,}481}}{40} = \frac{-29 \pm 74.03378}{40}$$

The positive root is $x = 1.125844$ (the other, $-2.575844$, is rejected): **FR(A–B) = 12.58%**. B is ahead below it (170,000 > 80,000 at 0%), A above it.

#### Fisher's rate A–C

$$-400{,}000\,x^2 + 380{,}000\,x + 100{,}000 = -300{,}000\,x^2 + 60{,}000\,x + 300{,}000$$

Moving every term to the left: $-100{,}000\,x^2 + 320{,}000\,x - 200{,}000 = 0$; dividing by $-20{,}000$, $5x^2 - 16x + 10 = 0$:

$$x = \frac{16 \pm \sqrt{(-16)^2 - 4 \cdot 5 \cdot 10}}{2 \cdot 5} = \frac{16 \pm \sqrt{256 - 200}}{10} = \frac{16 \pm \sqrt{56}}{10} = \frac{16 \pm 7.48331}{10}$$

The roots are $x = 2.348331$ and $x = 0.851669$, that is $r = 134.83\%$ and $r = -14.83\%$. Neither lies between 0% and the IRRs of A and C, so the two profiles do not cross where they matter: A is ahead at 0% (80,000 > 60,000) and **stays above C at every relevant rate**; Fisher's rate A–C does not exist in that range.

#### Fisher's rate B–C

$$-600{,}000\,x^2 + 90{,}000\,x + 680{,}000 = -300{,}000\,x^2 + 60{,}000\,x + 300{,}000$$

Moving every term to the right: $300{,}000\,x^2 - 30{,}000\,x - 380{,}000 = 0$; dividing by 10,000, $30x^2 - 3x - 38 = 0$:

$$x = \frac{3 \pm \sqrt{(-3)^2 - 4 \cdot 30 \cdot (-38)}}{2 \cdot 30} = \frac{3 \pm \sqrt{9 + 4{,}560}}{60} = \frac{3 \pm \sqrt{4{,}569}}{60} = \frac{3 \pm 67.59438}{60}$$

The positive root is $x = 1.176573$ (the other, $-1.076573$, is rejected): **FR(B–C) = 17.66%**. This crossing lies above both IRR(B) = 14.22% and IRR(C) = 10.50%, where both NPVs are negative, so it never affects a decision.

#### Decision intervals

- From 0% to 12.58%, B is above A (A–B) and above C (B–C holds up to 17.66%): **B**.
- From 12.58% to 16.47%, A is above B and, as shown, above C; its NPV is positive up to its IRR: **A**.
- Above 16.47%, the largest IRR, every NPV is negative: **no project**.

$$0\% \leq r < 12.58\% \Rightarrow B, \qquad 12.58\% < r < 16.47\% \Rightarrow A, \qquad r > 16.47\% \Rightarrow \text{no project}$$

C is never chosen: it is beaten by A at every rate. Check at one rate inside each interval: at 10%, $NPV_A$ = 28,099.17 €, $NPV_B$ = 43,801.65 €, $NPV_C$ = 2,479.34 € (B); at 14%, 10,280.09 €, 2,185.29 € and −16,528.16 € (A); at 18%, −6,147.66 €, −35,363.40 € and −33,697.21 € (none).

#### Choice at 8%

At the shareholders' 8%, below FR(A–B), Corvus undertakes **project B** with the 600,000 € budget, the same project that led the NPV ranking in (b).

## Interpretation

Payback measures liquidity, not value: it ranked first A and D, the projects that return their money in year 1, and it would have spent more than a fifth of the budget on D, whose small margin does not cover the cost of the funds. The NPV ranks by the value created at the required return, and with a budget the right choice is the combination with the largest total NPV, not the first projects of a list. Limiting cases: at $r = 0$ each NPV is the plain sum of flows minus the outlay, and as $r \to \infty$ it tends to minus the outlay; a project with a later flow profile, like B, moves the most between these two limits. Dimensions: NPVs in €, IRR and Fisher's rates as dimensionless rates per year, payback in years. A common mistake is to report Fisher's rate B–C as a switching point: it lies where neither project is worth undertaking.

## Verification

- (a) Payback A (years) | 1+(400000-380000)/100000 | 1.2
- (a) Payback A, days of the third month | ((1+(400000-380000)/100000-1)*12-2)*30 | 12
- (a) Payback B (years) | 1+(600000-90000)/680000 | 1.75
- (a) Payback C (years) | 1+(300000-60000)/300000 | 1.8
- (a) Payback C, days of the tenth month | ((1+(300000-60000)/300000-1)*12-9)*30 | 18
- (a) Payback D (years) | 1+(200000-180000)/30000 | 1.6667
- (a) Payback D (months after year 1) | (200000-180000)/30000*12 | 8
- (b) NPV of A at 8% | -400000+380000/1.08+100000/1.08**2 | 37585.73
- (b) NPV of B at 8% | -600000+90000/1.08+680000/1.08**2 | 66323.73
- (b) NPV of C at 8% | -300000+60000/1.08+300000/1.08**2 | 12757.20
- (b) NPV of D at 8% | -200000+180000/1.08+30000/1.08**2 | -7613.17
- (c) Total NPV of A + C + D | (-400000+380000/1.08+100000/1.08**2)+(-300000+60000/1.08+300000/1.08**2)+(-200000+180000/1.08+30000/1.08**2) | 42729.76
- (c) Total NPV of B + C | (-600000+90000/1.08+680000/1.08**2)+(-300000+60000/1.08+300000/1.08**2) | 79080.93
- (c) Total NPV of B + D | (-600000+90000/1.08+680000/1.08**2)+(-200000+180000/1.08+30000/1.08**2) | 58710.56
- (c) Total NPV of A + C | (-400000+380000/1.08+100000/1.08**2)+(-300000+60000/1.08+300000/1.08**2) | 50342.93
- (c) Total NPV of A + D | (-400000+380000/1.08+100000/1.08**2)+(-200000+180000/1.08+30000/1.08**2) | 29972.56
- (c) Total NPV of C + D | (-300000+60000/1.08+300000/1.08**2)+(-200000+180000/1.08+30000/1.08**2) | 5144.03
- (c) NPV lost by the payback order | (-600000+90000/1.08+680000/1.08**2)+(-300000+60000/1.08+300000/1.08**2)-((-400000+380000/1.08+100000/1.08**2)+(-300000+60000/1.08+300000/1.08**2)+(-200000+180000/1.08+30000/1.08**2)) | 36351.17
- (d) IRR of A (%) | 100*((19+sqrt(761))/40-1) | 16.47
- (d) IRR of B (%) | 100*((9+sqrt(16401))/120-1) | 14.22
- (d) IRR of C (%) | 100*((1+sqrt(101))/10-1) | 10.50
- (d) IRR of D (%) | 100*((18+sqrt(564))/40-1) | 4.37
- (d) NPV of A at 0% | -400000+380000+100000 | 80000
- (d) NPV of B at 0% | -600000+90000+680000 | 170000
- (d) NPV of C at 0% | -300000+60000+300000 | 60000
- (e) Fisher A-B (%) | 100*((-29+sqrt(5481))/40-1) | 12.58
- (e) A-C larger root as a rate (%) | 100*((16+sqrt(56))/10-1) | 134.83
- (e) A-C smaller root as a rate (%) | 100*((16-sqrt(56))/10-1) | -14.83
- (e) Fisher B-C (%) | 100*((3+sqrt(4569))/60-1) | 17.66
- (e) NPV of A at 10% | -400000+380000/1.10+100000/1.10**2 | 28099.17
- (e) NPV of B at 10% | -600000+90000/1.10+680000/1.10**2 | 43801.65
- (e) NPV of C at 10% | -300000+60000/1.10+300000/1.10**2 | 2479.34
- (e) NPV of A at 14% | -400000+380000/1.14+100000/1.14**2 | 10280.09
- (e) NPV of B at 14% | -600000+90000/1.14+680000/1.14**2 | 2185.29
- (e) NPV of C at 14% | -300000+60000/1.14+300000/1.14**2 | -16528.16
- (e) NPV of A at 18% | -400000+380000/1.18+100000/1.18**2 | -6147.66
- (e) NPV of B at 18% | -600000+90000/1.18+680000/1.18**2 | -35363.40
- (e) NPV of C at 18% | -300000+60000/1.18+300000/1.18**2 | -33697.21

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
