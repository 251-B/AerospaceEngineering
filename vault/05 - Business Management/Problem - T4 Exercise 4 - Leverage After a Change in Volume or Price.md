---
materia: Business Management
tema: "Topic 4: The Production Function"
origen: "BEP  OL Statements.pdf, Exercise 4, p. 1; solution in BEP  OL Statements  Solutions.pdf, p. 5"
dificultad: easy
tags:
  - problem
  - solved
  - break-even
  - operating-leverage
---

# ✏️ Problem: Exercise 4 — Leverage after a change in volume or in price

## 📄 Statement

Given the following information: selling price €10; variable cost per unit €3; fixed costs €1,000.

a) How many units must be sold to start making a profit?

b) What would the profit be if the company sold 200 units?

c) What is the degree of operating leverage for 200 units sold?

d) Will the degree of operating leverage vary if there is a 50 unit increase in sales?

e) Will the degree of operating leverage vary if there is a 10% rise in price (for 200 units)?

## Data and model

| Symbol | Meaning | Value |
| :--- | :--- | ---: |
| $P$ | selling price | 10 €/unit |
| $VC$ | variable cost per unit | 3 €/unit |
| $FC$ | fixed costs | 1,000 € |
| $m$ | unit margin, $P - VC$ | 7 €/unit |

Break-even point $Q^* = FC/m$ [Slide 37], profit $B = Q\,m - FC$ and operating leverage $OL = Q\,m/(Q\,m - FC)$ [Slides 39-40].

## Solution

### Step 1. Part (a): break-even point

$$Q^* = \frac{FC}{P - VC} = \frac{1{,}000}{10 - 3} = \frac{1{,}000}{7} = 142.86 \ \text{units}$$

Units are whole, so at 142 units the profit is still negative ($142 \times 7 - 1{,}000 = -6$ €) and at 143 it becomes positive ($143 \times 7 - 1{,}000 = 1$ €): the company starts making a profit from **143 units**.

### Step 2. Part (b): profit at 200 units

$$B = (10 - 3) \times 200 - 1{,}000 = 1{,}400 - 1{,}000 = 400 \ \text{€}$$

### Step 3. Part (c): leverage at 200 units

$$OL_{200} = \frac{200 \times 7}{200 \times 7 - 1{,}000} = \frac{1{,}400}{400} = 3.5$$

A 1% change in sales changes the profit by 3.5%.

### Step 4. Part (d): 50 more units (250 units)

$$OL_{250} = \frac{250 \times 7}{250 \times 7 - 1{,}000} = \frac{1{,}750}{750} = 2.33$$

Yes, it varies: it falls from 3.5 to 2.33, because the volume has moved away from the break-even point [Slide 42].

### Step 5. Part (e): 10% higher price (200 units)

The new price is $10 \times 1.10 = 11$ €/unit, so $m = 11 - 3 = 8$ €/unit and

$$OL = \frac{200 \times 8}{200 \times 8 - 1{,}000} = \frac{1{,}600}{600} = 2.67$$

Yes, it varies: it falls from 3.5 to 2.67. The higher margin lowers the break-even point to $1{,}000/8 = 125$ units, so 200 units are now farther from it.

## Checks and official key

- **Check with the BEP form** [Slide 42]: (c) $200/(200 - 142.86) = 3.5$; (d) $250/(250 - 142.86) = 2.33$; (e) $200/(200 - 125) = 2.67$.
- **Units:** $Q^*$ in units, profit in €, OL dimensionless.
- **Check against the official key** (BEP  OL Statements  Solutions.pdf, p. 5): $q^* \approx 143$ units, profit 400 €, $AO = 3.5$, $2.33$ and $2.66$ (2.67 rounded up here), with the same explanation (the volume moves away from the break-even point; the price changes the break-even point). Same results.

---

**Back to:** [[Problem Set - T4 Break-Even Point and Operating Leverage]]
