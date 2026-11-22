---
materia: Business Management
tema: "Topic 4: The Production Function"
origen: "BEP  OL Statements.pdf, Exercise 5, pp. 1-2; solution in BEP  OL Statements  Solutions.pdf, p. 6"
dificultad: medium
tags:
  - problem
  - solved
  - break-even
  - operating-leverage
  - margin-of-safety
---

# ✏️ Problem: Exercise 5 — Cost structure from two observations

## 📄 Statement

A visit to a company has provided the following information:

- If the company produced and sold 300 physical units, it would make a profit of €56.
- If the company produced and sold 160 physical units, it would make zero profit.
- The company forecasts sales of 500 physical units.

Calculate the company's fixed costs, the forecast profit, its safety margin and the degree of operating leverage.

## Data and model

| Observation | Volume $Q$ (units) | Profit $B$ (€) |
| :--- | ---: | ---: |
| 1 | 300 | 56 |
| 2 (break-even point) | 160 | 0 |
| Forecast | 500 | ? |

The profit is linear in the volume, $B = Q\,m - FC$ [Slide 39]; the margin of safety is $Q - Q^*$ in units, $(Q - Q^*)\,m$ in monetary units and $(Q - Q^*)/Q^*$ in percentage [Slide 43]; the leverage is $OL = Q\,m/(Q\,m - FC)$ [Slide 40].

## Solution

### Step 1. Unit margin

Subtracting the two observations removes the fixed costs:

$$\begin{aligned} B(300) - B(160) &= (300\,m - FC) - (160\,m - FC) = (300 - 160)\,m \\ 56 - 0 &= 140\,m \\ m &= \frac{56}{140} = 0.4 \ \text{€/unit} \end{aligned}$$

### Step 2. Fixed costs

At the break-even point the profit is zero:

$$0 = 160 \times 0.4 - FC \quad\Rightarrow\quad FC = 64 \ \text{€}$$

### Step 3. Forecast profit (500 units)

$$B(500) = 500 \times 0.4 - 64 = 200 - 64 = 136 \ \text{€}$$

### Step 4. Margin of safety

$$MS = Q - Q^* = 500 - 160 = 340 \ \text{units}$$

In monetary units, $MS = 340 \times 0.4 = 136$ €, and as a percentage of the break-even volume, $MS = 340/160 = 2.125$, that is 212.5%.

### Step 5. Operating leverage

$$OL_{500} = \frac{500 \times 0.4}{500 \times 0.4 - 64} = \frac{200}{136} = 1.47$$

A 1% change in sales changes the profit by 1.47%.

## Checks and official key

- **Check with observation 1:** $300 \times 0.4 - 64 = 120 - 64 = 56$ €. ✓
- **Check with the BEP form** [Slide 42]: $OL = 500/(500 - 160) = 1.47$. ✓
- **Note:** above the break-even point the margin of safety in m.u. equals the profit (136 €), since $(Q - Q^*)\,m = Q\,m - FC$.
- **Check against the official key** (BEP  OL Statements  Solutions.pdf, p. 6): $m = 0.4$ €/unit, $FC = 64$ €, forecast profit 136 €, $MS = 340$ units, $AO = 1.47$. Same results; the key gives the margin of safety in units only.

---

**Back to:** [[Problem Set - T4 Break-Even Point and Operating Leverage]]
