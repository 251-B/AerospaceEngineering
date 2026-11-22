---
materia: Business Management
tema: "Topic 4: The Production Function"
origen: "BEP  OL Statements.pdf, Exercise 2, p. 1; solution in BEP  OL Statements  Solutions.pdf, pp. 3-4"
dificultad: easy
tags:
  - problem
  - solved
  - break-even
  - operating-leverage
---

# ✏️ Problem: Exercise 2 — Break-even point from a known loss, and leverage at full capacity

## 📄 Statement

A company has a unit margin of €5.

a) Assuming that the manufacturing of 500 physical units produces a loss of €500, calculate the break-even point.

b) Represent graphically the situation of this company assuming that the maximum capacity of the plant is 900 physical units. What is the maximum profit that can be obtained?

c) Calculate the degree of operating leverage of this company for a production and sales volume of 900 physical units and interpret this result.

## Data and model

| Symbol | Meaning | Value |
| :--- | :--- | ---: |
| $m$ | unit margin | 5 €/unit |
| $B(500)$ | profit at 500 units | −500 € |
| $Q_{max}$ | maximum capacity | 900 units |

The profit is $B = Q\,m - FC$ [Slide 39], the break-even point $Q^* = FC/m$ [Slide 37] and the operating leverage $OL = Q\,m/(Q\,m - FC)$ [Slide 40]. Production equals sales, so $Q$ is both.

## Solution

### Step 1. Part (a): fixed costs and break-even point

The fixed costs are the only unknown in the profit at 500 units:

$$\begin{aligned} B(500) &= 500\,m - FC \\ -500 &= 500 \times 5 - FC = 2{,}500 - FC \\ FC &= 2{,}500 + 500 = 3{,}000 \ \text{€} \end{aligned}$$

Then

$$Q^* = \frac{FC}{m} = \frac{3{,}000}{5} = 600 \ \text{units}$$

### Step 2. Part (b): graph and maximum profit

The profit line is $B(Q) = 5\,Q - 3{,}000$, valid between 0 and the capacity of 900 units. It starts at $-3{,}000$ € (only the fixed costs) and crosses zero at 600 units. The line grows with $Q$, so the maximum profit is at the capacity limit:

$$B_{max} = B(900) = 900 \times 5 - 3{,}000 = 4{,}500 - 3{,}000 = 1{,}500 \ \text{€}$$

![[attachments/BM-T4/p2-profit.svg]]

### Step 3. Part (c): operating leverage at 900 units

$$OL_{900} = \frac{Q\,m}{Q\,m - FC} = \frac{900 \times 5}{900 \times 5 - 3{,}000} = \frac{4{,}500}{1{,}500} = 3$$

**Interpretation:** a 1% change in sales changes the profit by 3% [Slide 40]. The company is at full capacity and cannot sell more, so only a fall in sales is possible: each 1% fall below 900 units cuts the profit by 3%.

## Checks and official key

- **Check with the BEP form** [Slide 42]: $OL = Q/(Q - Q^*) = 900/(900 - 600) = 3$, the same value.
- **Check of (a):** $B(600) = 600 \times 5 - 3{,}000 = 0$.
- **Units:** $FC$ in €, $Q^*$ in units, OL dimensionless.
- **Check against the official key** (BEP  OL Statements  Solutions.pdf, pp. 3-4): $FC = 3{,}000$ €, $q^* = 600$ units, maximum profit 1,500 € and $AO = 3$, with the same reading for a decrease in sales. Same results.

---

**Back to:** [[Problem Set - T4 Break-Even Point and Operating Leverage]]
