---
materia: Business Management
tema: "Topic 4: The Production Function"
origen: "BEP  OL Statements.pdf, Exercise 3, p. 1; solution in BEP  OL Statements  Solutions.pdf, pp. 4-5"
dificultad: medium
tags:
  - problem
  - solved
  - break-even
  - operating-leverage
---

# ✏️ Problem: Exercise 3 — Choosing between two production processes

## 📄 Statement

A company manager who wants to market a new product has to choose between two alternative production processes A and B. In both cases the selling price of the product is €20.

| | Process A | Process B |
| :--- | ---: | ---: |
| Fixed costs | 40,000 | 20,000 |
| Unit variable costs | 13 | 15 |

a) Assuming that the expected level of production and sales is 10,000 physical units, decide the most convenient process according to the break-even analysis and the graphic representation.

b) If process B resulted in a higher quality product with a selling price of €25, how would this affect the choice of the most convenient process?

c) If the rise in price of the product obtained with process B (€25) caused a drop in sales from 10,000 to 6,000 physical units, which production process would the company choose?

## Data and model

| Magnitude | Process A | Process B |
| :--- | ---: | ---: |
| Price $P$ (€/unit) | 20 | 20 |
| Fixed costs $FC$ (€) | 40,000 | 20,000 |
| Variable cost $VC$ (€/unit) | 13 | 15 |
| Unit margin $m = P - VC$ (€/unit) | 7 | 5 |

Profit $B = Q\,m - FC$, break-even point $Q^* = FC/m$ [Slide 37] and operating leverage $OL = Q\,m/(Q\,m - FC)$ [Slide 40], the index of operating risk [Slide 41].

## Solution

### Step 1. Part (a): profit, break-even point and leverage at 10,000 units

$$\begin{aligned} B_A &= (20 - 13) \times 10{,}000 - 40{,}000 = 70{,}000 - 40{,}000 = 30{,}000 \ \text{€} \\ B_B &= (20 - 15) \times 10{,}000 - 20{,}000 = 50{,}000 - 20{,}000 = 30{,}000 \ \text{€} \end{aligned}$$

Both processes give the same profit. The break-even points are

$$Q^*_A = \frac{40{,}000}{7} = 5{,}714.3 \ \text{units} \qquad Q^*_B = \frac{20{,}000}{5} = 4{,}000 \ \text{units}$$

and the operating leverages at 10,000 units

$$OL_A = \frac{70{,}000}{30{,}000} = 2.33 \qquad OL_B = \frac{50{,}000}{30{,}000} = 1.67$$

With the same profit, process **B** is chosen: its break-even point is lower, so 10,000 units are farther from it, and its leverage (operating risk) is lower. A fall in sales would hurt A's profit more.

The two profit lines cross where $7\,Q - 40{,}000 = 5\,Q - 20{,}000$, that is $2\,Q = 20{,}000$ and $Q = 10{,}000$ units: below that volume B gives more profit, above it A does. The expected volume is exactly the crossing point.

![[attachments/BM-T4/p3-profit.svg]]

### Step 2. Part (b): process B sold at €25

The new unit margin of B is $m_B = 25 - 15 = 10$ €/unit, twice the old one. At 10,000 units:

$$B_B = 10 \times 10{,}000 - 20{,}000 = 80{,}000 \ \text{€} \qquad Q^*_B = \frac{20{,}000}{10} = 2{,}000 \ \text{units} \qquad OL_B = \frac{100{,}000}{80{,}000} = 1.25$$

Process A is unchanged (30,000 €, $OL_A = 2.33$). B now gives more profit with less operating risk: **B** is chosen with even more reason.

### Step 3. Part (c): B at €25 but only 6,000 units sold

$$B_B = (25 - 15) \times 6{,}000 - 20{,}000 = 60{,}000 - 20{,}000 = 40{,}000 \ \text{€}$$

Process A, which keeps the price of 20 € and the 10,000 units, still gives 30,000 €. Since $40{,}000 > 30{,}000$, the company still chooses **B**. Its leverage is $OL_B = 60{,}000/40{,}000 = 1.5$, also below A's 2.33.

## Checks and official key

- **Check of the crossing:** at 10,000 units both lines give 30,000 €, as found in (a).
- **Units:** profits in €, break-even points in units, OL dimensionless.
- **Check against the official key** (BEP  OL Statements  Solutions.pdf, pp. 4-5): profits 30,000 € for both processes, $AO_A = 2.33$, $AO_B = 1.66$ (1.67 rounded up here), B chosen in (a), (b) and (c), with 40,000 € > 30,000 € in (c). Same results.

> [!warning] Discrepancy with the official solution
> Two sentences of the key do not match its own numbers. In (a) it says that "A has a lower break-even point than B"; in fact $Q^*_A = 40{,}000/7 = 5{,}714$ units is **higher** than $Q^*_B = 4{,}000$ units, which is why B carries less risk, as the key itself concludes. In (b) it says the price rise increases "the unit margin by 5%"; the margin goes up by 5 € (from 5 to 10 €/unit, a 100% increase). The choices of the key are not affected.

---

**Back to:** [[Problem Set - T4 Break-Even Point and Operating Leverage]]
