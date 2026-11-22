---
materia: Business Management
tema: "Unit 3: investment selection"
bank_id: M01
title: "Aldebaran Space Systems: IRR ranking against NPV at the cost of capital"
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

# Bank M01 — Aldebaran Space Systems: IRR ranking against NPV at the cost of capital

> [!info] Practice item, not an official exercise
> Written for the bank in the style of Exercises 5 (SunTech Energy) and 6 (GreenWave Solutions) of the examples PDF. The company and its figures are invented. The twist: the project with the higher IRR is not the one with the higher NPV at the company's cost of capital, and the project with the highest IRR of all is the worst at that rate. Method: Examples PDF, Exercises 5 and 6; 3_II_NPV IRR.pdf, Exercises 8 and 9; Topic 3, Slide 37.

## Statement

Aldebaran Space Systems, a manufacturer of small satellites, is evaluating two investment projects:

- Investment A: an automated integration line for satellite buses, requiring an initial outlay of 500,000 € and expected to generate net cash flows of 300,000 € in year 1 and 300,000 € in year 2.
- Investment B: a test stand for reusable rocket engines with an unknown initial outlay, expected to generate net cash flows of 200,000 € in year 1 and 700,000 € in year 2.

The company is financed 40% with equity, whose cost is estimated at 9%, and 60% with liabilities, whose average cost is 4%. It uses the NPV criterion with its weighted average cost of capital as the yearly discount rate. The projects are mutually exclusive (only one can be accepted).

a) Determine the discount rate of the company and the maximum initial outlay of project B for it to be interesting (NPV ≥ 0). (0.5 points)

b) The initial outlay of project B is finally fixed at 750,000 €. Which investment is preferable under the IRR criterion? Does the NPV at the company's discount rate give the same ranking, and which project does the company undertake? (0.75 points)

c) A third project C is presented, a ground-station network for a satellite data-download service (a new line of business), requiring an initial investment of 200,000 € and generating 100,000 € in year 1 and 150,000 € in year 2. Draw a schematic graph of the NPV of the three projects as a function of the discount rate and compute Fisher's rates of the pairs A–B, A–C and B–C. (0.75 points)

d) Reason which project would be chosen depending on the discount rate, state from which discount rate no project should be selected, and say which project the company chooses at its own discount rate. (0.5 points)

## Setup

#### Data

| Project | Initial outlay $A$ (€) | $Q_1$ (€) | $Q_2$ (€) |
| :--- | ---: | ---: | ---: |
| A | 500,000 | 300,000 | 300,000 |
| B | unknown in (a); 750,000 from (b) on | 200,000 | 700,000 |
| C | 200,000 | 100,000 | 150,000 |

| Financial structure | Share | Cost |
| :--- | ---: | ---: |
| Equity $E$ | 40% | $K_{EQ}$ = 9% |
| Liabilities $L$ | 60% | $K_L$ = 4% |

#### Model

- **Cost of capital** (Topic 3, Slide 37): the capital cost is the weighted average of the costs of the financial resources, $K_{WACC} = K_{EQ}\,\frac{E}{E+L} + K_L\,\frac{L}{E+L}$. The key of 3_II_NPV IRR.pdf, Exercise 8 uses it as the cut-off rate of the IRR.
- **Net present value** (Examples PDF, Exercise 5): with outlay $A$, flows $Q_t$ and discount rate $k$,
$$NPV = -A + \frac{Q_1}{1+k} + \frac{Q_2}{(1+k)^2}$$
A project is interesting when $NPV \geq 0$; of mutually exclusive projects, the one with the largest positive NPV is chosen.
- **Internal rate of return**: the rate $r$ at which $NPV = 0$ (3_II_NPV_NPV IRR_solutions.pdf, Exercise 4). For a two-year project, with $x = 1 + r$ and multiplying by $x^2 > 0$, $NPV = 0$ becomes the quadratic $A\,x^2 - Q_1\,x - Q_2 = 0$, solved with $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Only the root with $x > 0$ has economic meaning.
- **Fisher's rate** of a pair: the rate at which both NPVs are equal (3_II_NPV_NPV IRR_solutions.pdf, Exercise 9). Multiplying $NPV_P = NPV_Q$ by $x^2$ gives $-A_P x^2 + Q_{1P} x + Q_{2P} = -A_Q x^2 + Q_{1Q} x + Q_{2Q}$, again a quadratic in $x$ (Examples PDF, Exercise 5 (c)).
- Hypotheses: flows at the end of each year, a constant yearly discount rate, no taxes and no residual value.

## (a) Discount rate and maximum outlay of project B [0.5 pts]

### Hint

First turn the financial structure into one rate with the weighted average of Slide 37. Then write the NPV of B with the outlay as the unknown $X$ and require $NPV_B \geq 0$.

### Checkpoint

- $K_{WACC}$ = 6.00%.
- Present value of the flows of B at 6%: 811,676.75 €.
- B is interesting for an outlay $X \leq$ 811,676.75 €.

### Solution

#### Discount rate from the financial structure

The weights are the shares of equity and liabilities in the financial structure, $E/(E+L) = 0.40$ and $L/(E+L) = 0.60$ (Topic 3, Slide 37):

$$K_{WACC} = 0.40 \times 9\% + 0.60 \times 4\% = 3.60\% + 2.40\% = 6.00\%$$

So $k = 0.06$ and the discount factors are $1 + k = 1.06$ and $(1 + k)^2 = 1.06 \times 1.06 = 1.1236$.

#### NPV of B with an unknown outlay

Writing every term of the NPV of B with outlay $X$:

$$NPV_B = -X + \frac{200{,}000}{1.06} + \frac{700{,}000}{1.1236} = -X + 188{,}679.245 + 622{,}997.508 = -X + 811{,}676.75$$

#### Condition NPV ≥ 0

$$-X + 811{,}676.75 \geq 0 \quad\Longleftrightarrow\quad X \leq 811{,}676.75\ \text{€}$$

Project B is interesting as long as its initial outlay does not exceed **811,676.75 €**, the present value of its flows at 6%. Units: each term is a sum of money in € divided by a dimensionless factor $(1.06)^t$, so the NPV is in €.

## (b) IRR ranking of A and B, and the NPV at the cost of capital [0.75 pts]

### Hint

Set each NPV equal to zero, put $x = 1 + r$, multiply by $x^2$ and solve the quadratic; keep the positive root. Then compute both NPVs at 6% and compare the two rankings.

### Checkpoint

- IRR(A) = 13.07%; IRR(B) = 10.86%; both above 6%, and A ranks first by IRR.
- $NPV_A(6\%)$ = 50,017.80 €; $NPV_B(6\%)$ = 61,676.75 €; B ranks first by NPV.
- The company uses NPV, so it undertakes B (the conflict is explained by Fisher's rate A–B in (c)).

### Solution

#### IRR of A

$$-500{,}000 + \frac{300{,}000}{x} + \frac{300{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 500{,}000\,x^2 - 300{,}000\,x - 300{,}000 = 0$$

Dividing by 100,000: $5x^2 - 3x - 3 = 0$, with $a = 5$, $b = -3$, $c = -3$:

$$x = \frac{3 \pm \sqrt{(-3)^2 - 4 \cdot 5 \cdot (-3)}}{2 \cdot 5} = \frac{3 \pm \sqrt{9 + 60}}{10} = \frac{3 \pm \sqrt{69}}{10} = \frac{3 \pm 8.30662}{10}$$

The roots are $x = 1.130662$ and $x = -0.530662$; the negative one has no economic meaning. Hence $r_A = 1.130662 - 1 = 0.1307$, **IRR(A) = 13.07%**.

#### IRR of B

$$-750{,}000 + \frac{200{,}000}{x} + \frac{700{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 750{,}000\,x^2 - 200{,}000\,x - 700{,}000 = 0$$

Dividing by 50,000: $15x^2 - 4x - 14 = 0$, with $a = 15$, $b = -4$, $c = -14$:

$$x = \frac{4 \pm \sqrt{(-4)^2 - 4 \cdot 15 \cdot (-14)}}{2 \cdot 15} = \frac{4 \pm \sqrt{16 + 840}}{30} = \frac{4 \pm \sqrt{856}}{30} = \frac{4 \pm 29.25748}{30}$$

The positive root is $x = 1.108583$ (the other, $-0.841916$, is rejected), so **IRR(B) = 10.86%**.

#### Ranking by IRR

Both IRRs exceed the 6% cost of capital, so each project is acceptable on its own (IRR > k, 3_II_NPV IRR.pdf, Exercise 8). Under the IRR criterion **A is preferable**, because $13.07\% > 10.86\%$.

#### NPVs at the company's discount rate

$$NPV_A(6\%) = -500{,}000 + \frac{300{,}000}{1.06} + \frac{300{,}000}{1.1236} = -500{,}000 + 283{,}018.868 + 266{,}998.932 = 50{,}017.80\ \text{€}$$

$$NPV_B(6\%) = -750{,}000 + 188{,}679.245 + 622{,}997.508 = 61{,}676.75\ \text{€}$$

(the two discounted terms of B are those of part (a); equivalently $811{,}676.75 - 750{,}000$).

#### The two rankings disagree

At 6% the NPV ranks **B first** ($61{,}676.75 > 50{,}017.80$), the opposite of the IRR ranking. The company has adopted the NPV criterion and the projects are mutually exclusive, so it **undertakes B**. The IRR compares the projects at their own break-even rates, not at the company's 6%; B receives most of its money in year 2, so its NPV is high when the rate is low and falls fast when the rate rises. Part (c) shows that the two NPV profiles cross at Fisher's rate A–B of 8.06%, above the 6% of the company.

## (c) NPV profiles and Fisher's rates of the three pairs [0.75 pts]

### Hint

For each project, mark the NPV at 0% (the plain sum of flows minus the outlay) on the vertical axis and the IRR on the horizontal axis. For each pair, equate the two NPVs, multiply by $x^2$ and solve the quadratic in $x = 1 + r$.

### Checkpoint

- IRR(C) = 15.14%; $NPV$ at 0%: A 100,000 €, B 150,000 €, C 50,000 €.
- Fisher's rates: A–B 8.06%; A–C 11.51%; B–C 9.50%.

### Solution

#### IRR of C

$$-200{,}000 + \frac{100{,}000}{x} + \frac{150{,}000}{x^2} = 0 \quad\xrightarrow{\ \times x^2\ }\quad 200{,}000\,x^2 - 100{,}000\,x - 150{,}000 = 0$$

Dividing by 50,000: $4x^2 - 2x - 3 = 0$, so

$$x = \frac{2 \pm \sqrt{(-2)^2 - 4 \cdot 4 \cdot (-3)}}{2 \cdot 4} = \frac{2 \pm \sqrt{4 + 48}}{8} = \frac{2 \pm \sqrt{52}}{8} = \frac{2 \pm 7.21110}{8}$$

The positive root is $x = 1.151388$ (the other, $-0.651388$, is rejected): **IRR(C) = 15.14%**.

#### Points of the profiles

At $r = 0$ every discount factor is 1, so the NPV is the sum of the flows minus the outlay:

$$NPV_A(0) = -500{,}000 + 300{,}000 + 300{,}000 = 100{,}000\ \text{€}$$

$$NPV_B(0) = -750{,}000 + 200{,}000 + 700{,}000 = 150{,}000\ \text{€}$$

$$NPV_C(0) = -200{,}000 + 100{,}000 + 150{,}000 = 50{,}000\ \text{€}$$

At 6%, $NPV_C = -200{,}000 + \frac{100{,}000}{1.06} + \frac{150{,}000}{1.1236} = -200{,}000 + 94{,}339.623 + 133{,}499.466 = 27{,}839.09$ €.

| Project | NPV at 0% (€) | NPV at 6% (€) | IRR |
| :--- | ---: | ---: | ---: |
| A | 100,000.00 | 50,017.80 | 13.07% |
| B | 150,000.00 | 61,676.75 | 10.86% |
| C | 50,000.00 | 27,839.09 | 15.14% |

Each profile starts at its NPV at 0%, decreases as the rate rises (every flow is divided by a larger $(1+r)^t$), cuts the horizontal axis at its IRR and tends to minus the outlay for very large rates. B starts highest but falls fastest (its large flow is in year 2), and C starts lowest but reaches zero last.

![[attachments/BM-MT2/m01-npv-profile.svg]]

#### Fisher's rate A–B

$$-500{,}000\,x^2 + 300{,}000\,x + 300{,}000 = -750{,}000\,x^2 + 200{,}000\,x + 700{,}000$$

Moving every term to the left: $250{,}000\,x^2 + 100{,}000\,x - 400{,}000 = 0$; dividing by 50,000, $5x^2 + 2x - 8 = 0$:

$$x = \frac{-2 \pm \sqrt{2^2 - 4 \cdot 5 \cdot (-8)}}{2 \cdot 5} = \frac{-2 \pm \sqrt{4 + 160}}{10} = \frac{-2 \pm \sqrt{164}}{10} = \frac{-2 \pm 12.80625}{10}$$

The positive root is $x = 1.080625$ (the other, $-1.480625$, is rejected): **FR(A–B) = 8.06%**.

#### Fisher's rate A–C

$$-500{,}000\,x^2 + 300{,}000\,x + 300{,}000 = -200{,}000\,x^2 + 100{,}000\,x + 150{,}000$$

Moving every term to the right: $300{,}000\,x^2 - 200{,}000\,x - 150{,}000 = 0$; dividing by 50,000, $6x^2 - 4x - 3 = 0$:

$$x = \frac{4 \pm \sqrt{(-4)^2 - 4 \cdot 6 \cdot (-3)}}{2 \cdot 6} = \frac{4 \pm \sqrt{16 + 72}}{12} = \frac{4 \pm \sqrt{88}}{12} = \frac{4 \pm 9.38083}{12}$$

The positive root is $x = 1.115069$ (the other, $-0.448403$, is rejected): **FR(A–C) = 11.51%**.

#### Fisher's rate B–C

$$-750{,}000\,x^2 + 200{,}000\,x + 700{,}000 = -200{,}000\,x^2 + 100{,}000\,x + 150{,}000$$

Moving every term to the right: $550{,}000\,x^2 - 100{,}000\,x - 550{,}000 = 0$; dividing by 50,000, $11x^2 - 2x - 11 = 0$:

$$x = \frac{2 \pm \sqrt{(-2)^2 - 4 \cdot 11 \cdot (-11)}}{2 \cdot 11} = \frac{2 \pm \sqrt{4 + 484}}{22} = \frac{2 \pm \sqrt{488}}{22} = \frac{2 \pm 22.09072}{22}$$

The positive root is $x = 1.095033$ (the other, $-0.913215$, is rejected): **FR(B–C) = 9.50%**.

#### Who is above whom on each side of each crossing

Each pair crosses only once for $r > 0$, so the project with the larger NPV at 0% stays ahead until the crossing:

- A–B: B is ahead below 8.06% (150,000 > 100,000 at 0%), A above it.
- A–C: A is ahead below 11.51% (100,000 > 50,000 at 0%), C above it.
- B–C: B is ahead below 9.50% (150,000 > 50,000 at 0%), C above it.

## (d) Decision intervals and the rate above which no project is chosen [0.5 pts]

### Hint

Follow the highest of the three profiles from left to right: it changes only at a Fisher's rate where the two leading profiles cross, and the choice ends at the largest IRR.

### Checkpoint

- $0 \leq r < 8.06\%$: B; $8.06\% < r < 11.51\%$: A; $11.51\% < r < 15.14\%$: C; $r > 15.14\%$: no project.
- At the company's 6%: project B.
- The B–C crossing at 9.50% happens while A is ahead of both, so it changes nothing.

### Solution

#### The upper envelope of the three profiles

- From 0% to 8.06%, B is above A (A–B) and above C (B–C holds up to 9.50%): **B**.
- At 8.06% A overtakes B. Between 8.06% and 11.51%, A is above B (A–B) and above C (A–C): **A**. The B–C crossing at 9.50% lies inside this interval, below A, so it does not change the decision.
- At 11.51% C overtakes A, and C is already above B (since 9.50%). Between 11.51% and 15.14%, C has the largest NPV and it is positive: **C**.
- Above 15.14%, the largest IRR, every NPV is negative: **no project** should be selected.

Check at one rate inside each interval: at 4%, $NPV_A$ = 65,828.40 €, $NPV_B$ = 89,497.04 €, $NPV_C$ = 34,837.28 € (B); at 10%, 20,661.16 €, 10,330.58 € and 14,876.03 € (A); at 14%, −6,001.85 €, −35,934.13 € and 3,139.43 € (C); at 16%, −18,430.44 €, −57,372.18 € and −2,318.67 € (none).

#### Decision of the company

$$0\% \leq r < 8.06\% \Rightarrow B, \qquad 8.06\% < r < 11.51\% \Rightarrow A, \qquad 11.51\% < r < 15.14\% \Rightarrow C, \qquad r > 15.14\% \Rightarrow \text{no project}$$

At exactly a Fisher's rate the two leading projects are indifferent. At its own discount rate of 6%, Aldebaran chooses **project B**. The trap is twofold: A beats B by IRR, and C has the highest IRR of the three, yet at 6% C has the lowest NPV (27,839.09 €). The IRR ranking only tells which project survives longest as the rate rises; at a given cost of capital the decision follows the NPV.

## Interpretation

The three profiles differ in how their money is spread over time. B concentrates 700,000 € in year 2, so a rising rate hits it hardest: it leads at low rates and is the first to drop out. C is small and returns most of its outlay in year 1, so its profile is flat and it is the last to become negative. Limiting cases: at $r = 0$ the NPV is the plain sum of flows minus the outlay, and as $r \to \infty$ every discounted flow tends to 0, so the NPV tends to minus the outlay. Dimensions: every NPV is a sum of amounts in € divided by dimensionless factors, so it is in €; the IRR and Fisher's rates are dimensionless rates per year. A common exam mistake is to stop at "A has the higher IRR, so A is chosen" without comparing the NPVs at the company's own rate, which here lies below Fisher's rate A–B.

## Verification

- (a) K_WACC (%) | 100*(0.40*0.09+0.60*0.04) | 6.00
- (a) PV of B's flows at 6% | 200000/1.06+700000/1.06**2 | 811676.75
- (b) IRR of A (%) | 100*((3+sqrt(69))/10-1) | 13.07
- (b) IRR of B (%) | 100*((4+sqrt(856))/30-1) | 10.86
- (b) NPV of A at 6% | -500000+300000/1.06+300000/1.06**2 | 50017.80
- (b) NPV of B at 6% | -750000+200000/1.06+700000/1.06**2 | 61676.75
- (c) IRR of C (%) | 100*((2+sqrt(52))/8-1) | 15.14
- (c) NPV of A at 0% | -500000+300000+300000 | 100000
- (c) NPV of B at 0% | -750000+200000+700000 | 150000
- (c) NPV of C at 0% | -200000+100000+150000 | 50000
- (c) NPV of C at 6% | -200000+100000/1.06+150000/1.06**2 | 27839.09
- (c) Fisher A-B (%) | 100*((-2+sqrt(164))/10-1) | 8.06
- (c) Fisher A-C (%) | 100*((4+sqrt(88))/12-1) | 11.51
- (c) Fisher B-C (%) | 100*((2+sqrt(488))/22-1) | 9.50
- (d) NPV of A at 4% | -500000+300000/1.04+300000/1.04**2 | 65828.40
- (d) NPV of B at 4% | -750000+200000/1.04+700000/1.04**2 | 89497.04
- (d) NPV of C at 4% | -200000+100000/1.04+150000/1.04**2 | 34837.28
- (d) NPV of A at 10% | -500000+300000/1.10+300000/1.10**2 | 20661.16
- (d) NPV of B at 10% | -750000+200000/1.10+700000/1.10**2 | 10330.58
- (d) NPV of C at 10% | -200000+100000/1.10+150000/1.10**2 | 14876.03
- (d) NPV of A at 14% | -500000+300000/1.14+300000/1.14**2 | -6001.85
- (d) NPV of B at 14% | -750000+200000/1.14+700000/1.14**2 | -35934.13
- (d) NPV of C at 14% | -200000+100000/1.14+150000/1.14**2 | 3139.43
- (d) NPV of A at 16% | -500000+300000/1.16+300000/1.16**2 | -18430.44
- (d) NPV of B at 16% | -750000+200000/1.16+700000/1.16**2 | -57372.18
- (d) NPV of C at 16% | -200000+100000/1.16+150000/1.16**2 | -2318.67

---

**Back to:** [[Problem Set - Business Management Problem Bank]]
