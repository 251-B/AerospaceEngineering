---
materia: Business Management
tema: "Topic 5: Marketing and Sales Management"
origen: "Elasticity exercises STATEMENTS.pdf, Exercise 2, p. 1; solution in PED Exercises SOL.pdf, p. 2"
dificultad: medium
tags:
  - problem
  - solved
  - elasticity
---

# ✏️ Problem: Exercise 2 — Quantity sold after a price rise

## 📄 Statement

The price elasticity of demand of a certain good is 2 and we are currently selling 100 units at a price of 20 €. How many units will be sold at a price of 21 €? Show your answer with the respective calculations.

## Data and model

| Symbol | Meaning | Value |
| :--- | :--- | ---: |
| $\lvert E_d \rvert$ | price elasticity (absolute value) | 2 |
| $Q_1$, $P_1$ | current quantity and price | 100 units, 20 € |
| $P_2$ | new price | 21 € |
| $x$ | units sold at 21 € | unknown |

Price elasticity $E_d = (\%\Delta Q)/(\%\Delta P)$, negative by the law of demand (topic 5.2.2.pdf, p. 2). Two ways of taking the percentages give two estimates.

## Solution

### Step 1. Estimate with the initial values as base (Slide 17)

$$\%\Delta P = \frac{21 - 20}{20} = 5\% \qquad \%\Delta Q = E_d \cdot \%\Delta P = -2 \times 5\% = -10\%$$

$$x = 100 \times (1 - 0.10) = 90 \ \text{units}$$

### Step 2. Exact value with the midpoint of the change

Taking the elasticity at the midpoint of the change from $P = 20$ to $P = 21$ and from $Q = 100$ to $Q = x$:

$$\frac{(x - 100) \big/ \frac{x + 100}{2}}{(21 - 20) \big/ \frac{21 + 20}{2}} = -2$$

The price part is $1/20.5$, so

$$\begin{aligned} \frac{2\,(x - 100)}{x + 100} \cdot 20.5 &= -2 \\ \frac{41\,(x - 100)}{x + 100} &= -2 \\ 41x - 4{,}100 &= -2x - 200 \\ 43x &= 3{,}900 \\ x &= \frac{3{,}900}{43} = 90.70 \ \text{units} \end{aligned}$$

At 21 € about **90.7 units** are sold (90 units in the simpler estimate).

## Checks and official key

- **Check of the midpoint value:** $\Delta Q/\bar Q = (90.70 - 100)/95.35 = -0.0975$ and $\Delta P/\bar P = 1/20.5 = 0.0488$; the ratio is $-2.00$. ✓
- **Meaning:** demand is elastic ($\lvert E_d \rvert = 2 > 1$), so the 5% price rise lowers sales by about 10% and revenue falls from $20 \times 100 = 2{,}000$ € to $21 \times 90.70 = 1{,}904.7$ €.
- **Check against the official key** (PED Exercises SOL.pdf, p. 2): about 90 units in rough numbers, and $x = 3{,}900/43 = 90.697$ units with the midpoint formula. Same result; $3{,}900/43 = 90.6977$, which the key truncates to 90.697 and is rounded here to 90.70.

---

**Back to:** [[Problem Set - T5 Price Elasticity of Demand]]
