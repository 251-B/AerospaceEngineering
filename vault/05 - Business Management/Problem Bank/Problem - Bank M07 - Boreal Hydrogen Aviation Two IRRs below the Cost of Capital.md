---
materia: Business Management
tema: "Unit 3: investment selection"
bank_id: M07
title: "Boreal Hydrogen Aviation: two IRRs below the cost of capital and a third project"
category: mt2_problem
archetype: npv-irr-fisher
level: trap
unit: 3
difficulty: 3
points: 2.5
time_minutes: 25
official: false
origen: "Problem written for the bank in the style of Exercises 5 and 6 of BUSINESS_SECONDPARTIAL_2026_EXAMPLES_SOL.pdf; not an official exercise. Discount rate from the weighted cost of capital of Topic 3, Slide 37, as in 3_II_NPV IRR.pdf, Exercise 8; decision by Fisher's rate as in Exercise 9 of the same sheet."
tags:
  - problem-bank
  - midterm-2
  - npv-irr-fisher
  - fisher-rate
  - cost-of-capital
---

# Bank M07 — Boreal Hydrogen Aviation: two IRRs below the cost of capital and a third project

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercise 6 (GreenWave Solutions) of the examples PDF, whose trap is reused: the IRR ranks A above B, but both IRRs are below the cost of capital, so neither is accepted. The company and its figures are invented. Here the cost of capital must first be built from the amounts of the financial structure, the unknown of the first part is a cash flow instead of an outlay, and the project with the second-best IRR is never chosen at any rate. Method: Examples PDF, Exercises 5 and 6; 3_II_NPV IRR.pdf, Exercises 8 and 9; Topic 3, Slide 37.

## Statement

Boreal Hydrogen Aviation develops hydrogen fuel-cell powertrains for regional aircraft. Its balance sheet shows 3,000,000 € of equity, for which the shareholders demand 13% a year, and 2,000,000 € of liabilities, whose average cost is 6.5% a year. The company discounts every project at its weighted average cost of capital and treats the following projects as mutually exclusive (only one can be accepted):

- Project A: a hydrogen refuelling truck for airports. It needs 600,000 € today and returns 400,000 € after one year and 280,000 € after two.
- Project B: a fuel-cell test bench. It needs 800,000 € today and returns 300,000 € after one year; the flow of the second year depends on a testing contract that is still being negotiated.

a) Compute the discount rate of the company. What is the minimum cash flow of project B in year 2 for B to be interesting (NPV ≥ 0)? (0.5 points)

b) The contract is finally signed and fixes the year-2 flow of B at 610,000 €. Rank A and B under the IRR criterion and say whether either of them should be undertaken. Confirm your answer with the NPVs at the company's discount rate. (0.6 points)

c) A third project C is then presented: a retrofit kit for ground-power units, needing 400,000 € and returning 360,000 € in year 1 and 110,000 € in year 2. Compute its IRR, draw a schematic graph of the NPV of the three projects as a function of the discount rate and compute Fisher's rates of the pairs A–B, A–C and B–C. (0.8 points)

d) State which project would be chosen depending on the discount rate and from which rate no project should be selected. Which project does Boreal choose at its own discount rate? Is there any discount rate at which A, the project with the higher IRR of the first two, would be the one chosen? (0.6 points)

## Setup

#### Data

| Project | Initial outlay $A$ (€) | $Q_1$ (€) | $Q_2$ (€) |
| :--- | ---: | ---: | ---: |
| A | 600,000 | 400,000 | 280,000 |
| B | 800,000 | 300,000 | unknown in (a); 610,000 from (b) on |
| C | 400,000 | 360,000 | 110,000 |

| Financial structure | Amount (€) | Cost |
| :--- | ---: | ---: |
| Equity $E$ | 3,000,000 | $K_{EQ}$ = 13% |
| Liabilities $L$ | 2,000,000 | $K_L$ = 6.5% |

#### Model

- **Cost of capital** (Topic 3, Slide 37): $K_{WACC} = K_{EQ}\,\frac{E}{E+L} + K_L\,\frac{L}{E+L}$, the cut-off rate of the IRR in 3_II_NPV IRR.pdf, Exercise 8. The weights are the shares of each source in the total financing, computed from the amounts.
- **Net present value** (Examples PDF, Exercise 6): with outlay $A$, flows $Q_t$ and discount rate $k$,
$$NPV = -A + \frac{Q_1}{1+k} + \frac{Q_2}{(1+k)^2}$$
A project is interesting when $NPV \geq 0$; of mutually exclusive projects, the one with the largest positive NPV is chosen.
- **Internal rate of return**: the rate $r$ at which $NPV = 0$ (3_II_NPV_NPV IRR_solutions.pdf, Exercise 4). With $x = 1 + r$ and multiplying by $x^2 > 0$: $A\,x^2 - Q_1\,x - Q_2 = 0$, solved with $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$; only $x > 0$ has economic meaning. A project is acceptable on its own when its IRR exceeds the cost of capital.
- **Fisher's rate** of a pair: the rate at which both NPVs are equal (3_II_NPV_NPV IRR_solutions.pdf, Exercise 9), again a quadratic in $x$ after multiplying by $x^2$ (Examples PDF, Exercise 6 (c)).
- Hypotheses: flows at the end of each year, a constant yearly rate, no taxes and no residual value.

## (a) Discount rate and minimum year-2 flow of B [0.5 pts]

### Hint

Turn the amounts of equity and liabilities into shares of the total 5,000,000 € before weighting the costs. Then write the NPV of B with the year-2 flow as the unknown $Y$.

### Checkpoint

- Weights 0.60 and 0.40; $K_{WACC}$ = 10.40% (not the simple average 9.75%).
- Discounted year-1 flow of B: 271,739.13 €.
- B is interesting for $Y \geq$ 643,852.80 €.

### Solution

#### Discount rate from the financial structure

Total financing: $E + L = 3{,}000{,}000 + 2{,}000{,}000 = 5{,}000{,}000$ €, so the weights are $E/(E+L) = 3{,}000{,}000 / 5{,}000{,}000 = 0.60$ and $L/(E+L) = 2{,}000{,}000 / 5{,}000{,}000 = 0.40$ (Topic 3, Slide 37):

$$K_{WACC} = 0.60 \times 13\% + 0.40 \times 6.5\% = 7.80\% + 2.60\% = 10.40\%$$

The plain average $(13\% + 6.5\%)/2 = 9.75\%$ would be wrong: equity finances 60% of the company, so its cost weighs more. With $k = 0.104$ the discount factors are $1.104$ and $1.104^2 = 1.218816$.

#### NPV of B with an unknown year-2 flow

$$NPV_B = -800{,}000 + \frac{300{,}000}{1.104} + \frac{Y}{1.218816} = -800{,}000 + 271{,}739.130 + \frac{Y}{1.218816} = -528{,}260.870 + \frac{Y}{1.218816}$$

#### Condition NPV ≥ 0

$$\frac{Y}{1.218816} \geq 528{,}260.870 \quad\Longleftrightarrow\quad Y \geq 528{,}260.870 \times 1.218816 = 643{,}852.80\ \text{€}$$

B is interesting only if its year-2 flow reaches **643,852.80 €**: the part of the outlay not covered by the discounted first flow, carried forward two years at 10.40%. Units: € multiplied by a dimensionless factor, so the result is in €.

## (b) IRR ranking of A and B, and why neither is accepted [0.6 pts]

### Hint

Solve the quadratic in $x = 1 + r$ for each project. Before ranking, compare each IRR with the 10.40% of (a).

### Checkpoint

- IRR(A) = 9.35%; IRR(B) = 8.06%: A ranks above B, but both are below 10.40%.
- $NPV_A(10.40\%)$ = −7,950.01 €; $NPV_B(10.40\%)$ = −27,775.15 €: neither project is undertaken.

### Solution

#### IRR of A

$$-600{,}000 + \frac{400{,}000}{x} + \frac{280{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 600{,}000\,x^2 - 400{,}000\,x - 280{,}000 = 0$$

Dividing by 40,000: $15x^2 - 10x - 7 = 0$, with $a = 15$, $b = -10$, $c = -7$:

$$x = \frac{10 \pm \sqrt{(-10)^2 - 4 \cdot 15 \cdot (-7)}}{2 \cdot 15} = \frac{10 \pm \sqrt{100 + 420}}{30} = \frac{10 \pm \sqrt{520}}{30} = \frac{10 \pm 22.80351}{30}$$

The positive root is $x = 1.093450$ (the other, $-0.426784$, is rejected): **IRR(A) = 9.35%**.

#### IRR of B

$$-800{,}000 + \frac{300{,}000}{x} + \frac{610{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 800{,}000\,x^2 - 300{,}000\,x - 610{,}000 = 0$$

Dividing by 10,000: $80x^2 - 30x - 61 = 0$, with $a = 80$, $b = -30$, $c = -61$:

$$x = \frac{30 \pm \sqrt{(-30)^2 - 4 \cdot 80 \cdot (-61)}}{2 \cdot 80} = \frac{30 \pm \sqrt{900 + 19{,}520}}{160} = \frac{30 \pm \sqrt{20{,}420}}{160} = \frac{30 \pm 142.89857}{160}$$

The positive root is $x = 1.080616$ (the other, $-0.705616$, is rejected): **IRR(B) = 8.06%**.

#### The ranking does not decide anything

| Project | IRR | Cost of capital | Acceptable? |
| :--- | ---: | ---: | :--- |
| A | 9.35% | 10.40% | No (IRR < k) |
| B | 8.06% | 10.40% | No (IRR < k) |

A ranks above B ($9.35\% > 8.06\%$), but a ranking only matters among acceptable projects. Both projects return less than the 10.40% their funds cost, so **neither A nor B should be undertaken** (3_II_NPV IRR.pdf, Exercise 8). For B this was already known from (a): 610,000 € is below the minimum of 643,852.80 €.

#### Confirmation with the NPVs at 10.40%

$$NPV_A = -600{,}000 + \frac{400{,}000}{1.104} + \frac{280{,}000}{1.218816} = -600{,}000 + 362{,}318.841 + 229{,}731.149 = -7{,}950.01\ \text{€}$$

$$NPV_B = -800{,}000 + \frac{300{,}000}{1.104} + \frac{610{,}000}{1.218816} = -800{,}000 + 271{,}739.130 + 500{,}485.717 = -27{,}775.15\ \text{€}$$

Both NPVs are negative, consistent with IRR < k: an NPV profile is positive only to the left of its IRR.

## (c) IRR of C, NPV profiles and Fisher's rates [0.8 pts]

### Hint

For the graph, mark the NPV at 0% of each project and its IRR. For each pair, equate the two NPVs, multiply by $x^2$, collect the terms on one side and solve.

### Checkpoint

- IRR(C) = 14.10%; NPV at 0%: A 80,000 €, B 110,000 €, C 70,000 €; $NPV_C(10.40\%)$ = 16,338.48 €.
- Fisher's rates: A–C 2.74%; B–C 4.55%; A–B 5.86%. All three lie below the cost of capital.

### Solution

#### IRR of C

$$-400{,}000 + \frac{360{,}000}{x} + \frac{110{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 400{,}000\,x^2 - 360{,}000\,x - 110{,}000 = 0$$

Dividing by 10,000: $40x^2 - 36x - 11 = 0$:

$$x = \frac{36 \pm \sqrt{(-36)^2 - 4 \cdot 40 \cdot (-11)}}{2 \cdot 40} = \frac{36 \pm \sqrt{1{,}296 + 1{,}760}}{80} = \frac{36 \pm \sqrt{3{,}056}}{80} = \frac{36 \pm 55.28110}{80}$$

The positive root is $x = 1.141014$ (the other, $-0.241014$, is rejected): **IRR(C) = 14.10%**, above the 10.40% cost of capital.

#### Points of the profiles

$$NPV_A(0) = -600{,}000 + 400{,}000 + 280{,}000 = 80{,}000\ \text{€}$$

$$NPV_B(0) = -800{,}000 + 300{,}000 + 610{,}000 = 110{,}000\ \text{€}$$

$$NPV_C(0) = -400{,}000 + 360{,}000 + 110{,}000 = 70{,}000\ \text{€}$$

$$NPV_C(10.40\%) = -400{,}000 + \frac{360{,}000}{1.104} + \frac{110{,}000}{1.218816} = -400{,}000 + 326{,}086.957 + 90{,}251.523 = 16{,}338.48\ \text{€}$$

| Project | NPV at 0% (€) | NPV at 10.40% (€) | IRR |
| :--- | ---: | ---: | ---: |
| A | 80,000.00 | −7,950.01 | 9.35% |
| B | 110,000.00 | −27,775.15 | 8.06% |
| C | 70,000.00 | 16,338.48 | 14.10% |

Each profile decreases from its NPV at 0%, cuts the horizontal axis at its IRR and tends to minus the outlay for very large rates. B starts highest and falls fastest (610,000 € arrive in year 2); C starts lowest but is the flattest (360,000 € of its 470,000 € arrive in year 1), so it is the last to reach zero.

![[attachments/BM-MT2/m07-npv-profile.svg]]

#### Fisher's rate A–B

$$-600{,}000\,x^2 + 400{,}000\,x + 280{,}000 = -800{,}000\,x^2 + 300{,}000\,x + 610{,}000$$

Moving every term to the left: $200{,}000\,x^2 + 100{,}000\,x - 330{,}000 = 0$; dividing by 10,000, $20x^2 + 10x - 33 = 0$:

$$x = \frac{-10 \pm \sqrt{10^2 - 4 \cdot 20 \cdot (-33)}}{2 \cdot 20} = \frac{-10 \pm \sqrt{100 + 2{,}640}}{40} = \frac{-10 \pm \sqrt{2{,}740}}{40} = \frac{-10 \pm 52.34501}{40}$$

The positive root is $x = 1.058625$ (the other, $-1.558625$, is rejected): **FR(A–B) = 5.86%**. B is ahead below it (110,000 > 80,000 at 0%), A above it.

#### Fisher's rate A–C

$$-600{,}000\,x^2 + 400{,}000\,x + 280{,}000 = -400{,}000\,x^2 + 360{,}000\,x + 110{,}000$$

Moving every term to the right: $200{,}000\,x^2 - 40{,}000\,x - 170{,}000 = 0$; dividing by 10,000, $20x^2 - 4x - 17 = 0$:

$$x = \frac{4 \pm \sqrt{(-4)^2 - 4 \cdot 20 \cdot (-17)}}{2 \cdot 20} = \frac{4 \pm \sqrt{16 + 1{,}360}}{40} = \frac{4 \pm \sqrt{1{,}376}}{40} = \frac{4 \pm 37.09447}{40}$$

The positive root is $x = 1.027362$ (the other, $-0.827362$, is rejected): **FR(A–C) = 2.74%**. A is ahead below it (80,000 > 70,000 at 0%), C above it.

#### Fisher's rate B–C

$$-800{,}000\,x^2 + 300{,}000\,x + 610{,}000 = -400{,}000\,x^2 + 360{,}000\,x + 110{,}000$$

Moving every term to the right: $400{,}000\,x^2 + 60{,}000\,x - 500{,}000 = 0$; dividing by 20,000, $20x^2 + 3x - 25 = 0$:

$$x = \frac{-3 \pm \sqrt{3^2 - 4 \cdot 20 \cdot (-25)}}{2 \cdot 20} = \frac{-3 \pm \sqrt{9 + 2{,}000}}{40} = \frac{-3 \pm \sqrt{2{,}009}}{40} = \frac{-3 \pm 44.82187}{40}$$

The positive root is $x = 1.045547$ (the other, $-1.195547$, is rejected): **FR(B–C) = 4.55%**. B is ahead below it (110,000 > 70,000 at 0%), C above it.

## (d) Decision intervals and the choice at 10.40% [0.6 pts]

### Hint

Order the three Fisher's rates and follow the highest profile from 0% upwards. A crossing between two projects that are both below the leader changes nothing.

### Checkpoint

- $0 \leq r < 4.55\%$: B; $4.55\% < r < 14.10\%$: C; $r > 14.10\%$: no project.
- At 10.40%: project C, NPV 16,338.48 €.
- A is never chosen: at 2.74% and at 5.86% it only changes places with a project that is not the leader.

### Solution

#### The upper envelope of the three profiles

The crossings in increasing order are A–C at 2.74%, B–C at 4.55% and A–B at 5.86%.

- From 0% to 4.55%, B is above C (B–C) and above A (A–B holds up to 5.86%): **B**. The A–C crossing at 2.74% happens below B, so it changes nothing.
- At 4.55% C overtakes B. From then on C is above B, and it has been above A since 2.74%. So from 4.55% to its IRR of 14.10%, C has the largest NPV and it is positive: **C**. The A–B crossing at 5.86% happens below C and changes nothing either.
- Above 14.10%, the largest IRR, every NPV is negative: **no project**.

$$0\% \leq r < 4.55\% \Rightarrow B, \qquad 4.55\% < r < 14.10\% \Rightarrow C, \qquad r > 14.10\% \Rightarrow \text{no project}$$

At exactly 4.55% B and C are indifferent. Check at one rate inside each interval: at 2%, $NPV_A$ = 61,284.12 €, $NPV_B$ = 80,430.60 €, $NPV_C$ = 58,669.74 € (B); at 8%, 10,425.24 €, 754.46 € and 27,640.60 € (C); at 15%, −40,453.69 €, −77,882.80 € and −3,780.72 € (none).

#### Decision of the company

At 10.40% only C has a positive NPV: Boreal undertakes **project C**, with $NPV_C$ = 16,338.48 €.

#### Is A ever the best?

No. A would be acceptable on its own for any cost of capital below its IRR of 9.35%, but it is never the project with the highest NPV: below 4.55% B beats it, and from 2.74% on C beats it. The IRR ranking "A before B" of (b) therefore says nothing about the decision: it compares two projects that are both rejected at 10.40% and that, at any lower rate, are both beaten by another project or by each other.

## Interpretation

The trap of the GreenWave exercise appears twice. First, a higher IRR is not a reason to invest: A beats B by IRR, yet both lose money at the 10.40% the company pays for its funds. Second, the project that the company finally chooses, C, is the one with the lowest NPV at 0%: it wins because most of its money comes back in year 1, so its profile falls slowly. All three Fisher's rates lie below the cost of capital, which is why, at the company's own rate, the IRR and the NPV rank the projects in the same order. Limiting cases: at $r = 0$ the NPV is the plain sum of flows minus the outlay; as $r \to \infty$ it tends to minus the outlay. Dimensions: NPVs in €, the cost of capital, the IRRs and Fisher's rates are dimensionless rates per year. Using the simple average 9.75% instead of the weighted 10.40% would not change the decision here, since both rates lie between IRR(A) = 9.35% and IRR(C) = 14.10%, but it is a mark lost in part (a).

## Verification

- (a) Weight of equity | 3000000/(3000000+2000000) | 0.60
- (a) K_WACC (%) | 100*(0.60*0.13+0.40*0.065) | 10.40
- (a) Simple average (%) | 100*(0.13+0.065)/2 | 9.75
- (a) Discount factor of year 2 | 1.104**2 | 1.218816
- (a) Discounted year-1 flow of B | 300000/1.104 | 271739.13
- (a) Minimum year-2 flow of B | (800000-300000/1.104)*1.104**2 | 643852.80
- (b) IRR of A (%) | 100*((10+sqrt(520))/30-1) | 9.35
- (b) IRR of B (%) | 100*((30+sqrt(20420))/160-1) | 8.06
- (b) NPV of A at 10.40% | -600000+400000/1.104+280000/1.104**2 | -7950.01
- (b) NPV of B at 10.40% | -800000+300000/1.104+610000/1.104**2 | -27775.15
- (c) IRR of C (%) | 100*((36+sqrt(3056))/80-1) | 14.10
- (c) NPV of A at 0% | -600000+400000+280000 | 80000
- (c) NPV of B at 0% | -800000+300000+610000 | 110000
- (c) NPV of C at 0% | -400000+360000+110000 | 70000
- (c) NPV of C at 10.40% | -400000+360000/1.104+110000/1.104**2 | 16338.48
- (c) Fisher A-B (%) | 100*((-10+sqrt(2740))/40-1) | 5.86
- (c) Fisher A-C (%) | 100*((4+sqrt(1376))/40-1) | 2.74
- (c) Fisher B-C (%) | 100*((-3+sqrt(2009))/40-1) | 4.55
- (d) NPV of A at 2% | -600000+400000/1.02+280000/1.02**2 | 61284.12
- (d) NPV of B at 2% | -800000+300000/1.02+610000/1.02**2 | 80430.60
- (d) NPV of C at 2% | -400000+360000/1.02+110000/1.02**2 | 58669.74
- (d) NPV of A at 8% | -600000+400000/1.08+280000/1.08**2 | 10425.24
- (d) NPV of B at 8% | -800000+300000/1.08+610000/1.08**2 | 754.46
- (d) NPV of C at 8% | -400000+360000/1.08+110000/1.08**2 | 27640.60
- (d) NPV of A at 15% | -600000+400000/1.15+280000/1.15**2 | -40453.69
- (d) NPV of B at 15% | -800000+300000/1.15+610000/1.15**2 | -77882.80
- (d) NPV of C at 15% | -400000+360000/1.15+110000/1.15**2 | -3780.72

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
