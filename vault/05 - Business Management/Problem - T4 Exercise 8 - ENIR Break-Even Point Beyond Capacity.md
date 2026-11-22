---
materia: Business Management
tema: "Topic 4: The Production Function"
origen: "BEP  OL Statements.pdf, Exercise 8, p. 2; solution in BEP  OL Statements  Solutions.pdf, p. 7"
dificultad: medium
tags:
  - problem
  - solved
  - break-even
  - capacity
---

# ✏️ Problem: Exercise 8 — ENIR, S.A.: a break-even point beyond capacity

## 📄 Statement

Company ENIR, S.A., a black cigarette manufacturer, has not obtained profits during year 2008. It was established two years before and its maximum production capacity amounts to 11 million packs per year. Analyzing its management, we know that in 2008, the company produced 10 million packs, with financial costs relative to its external financing of €300,000, fixed costs of commercialization and administration of €1,000,000 and other fixed costs of €1,700,000. The selling price was €1.3 per pack, which was established by the Government, as this is an industry regulated by the State.

For the following year 2009 and, maintaining the same facilities, the company expects an increase of 15% in its fixed costs, as well as a decrease of 1% in the variable cost per unit. Calculate:

a) The break-even point for year 2009.

b) Considering these plans, is it possible that the company obtains profits? Account for your answer.

## Data and model

| Magnitude | 2008 | 2009 |
| :--- | ---: | ---: |
| Capacity (packs) | 11,000,000 | 11,000,000 |
| Volume $Q$ (packs) | 10,000,000 | ? |
| Price $P$ (€/pack) | 1.3 | 1.3 |
| Fixed costs $FC$ (€) | 3,000,000 | +15% |
| Variable cost $VC$ (€/pack) | unknown | −1% |

**Reading of the statement (the same as the official key):** "has not obtained profits" is read as a profit of exactly zero in 2008, so 10 million packs was the break-even point of 2008; and the financial costs of 300,000 € are counted among the fixed costs:

$$FC_{2008} = 300{,}000 + 1{,}000{,}000 + 1{,}700{,}000 = 3{,}000{,}000 \ \text{€}$$

Break-even condition: profit $= Q\,(P - VC) - FC = 0$ [Slides 36-37].

## Solution

### Step 1. Variable cost per pack in 2008

$$\begin{aligned} 10{,}000{,}000 \times 1.3 - 3{,}000{,}000 - 10{,}000{,}000 \times VC &= 0 \\ 13{,}000{,}000 - 3{,}000{,}000 &= 10{,}000{,}000 \times VC \\ VC_{2008} &= \frac{10{,}000{,}000}{10{,}000{,}000} = 1.0 \ \text{€/pack} \end{aligned}$$

### Step 2. Cost structure of 2009

$$FC_{2009} = 3{,}000{,}000 \times 1.15 = 3{,}450{,}000 \ \text{€} \qquad VC_{2009} = 1.0 \times 0.99 = 0.99 \ \text{€/pack}$$

so the unit margin is $m_{2009} = 1.3 - 0.99 = 0.31$ €/pack.

### Step 3. Part (a): break-even point of 2009

$$Q^*_{2009} = \frac{FC}{m} = \frac{3{,}450{,}000}{0.31} = 11{,}129{,}032 \ \text{packs}$$

### Step 4. Part (b): can the company make a profit?

No. The break-even point (11,129,032 packs) is above the maximum capacity of the facilities (11,000,000 packs), and the price is fixed by the Government. Even working at full capacity the company loses money:

$$B(11{,}000{,}000) = 11{,}000{,}000 \times 0.31 - 3{,}450{,}000 = 3{,}410{,}000 - 3{,}450{,}000 = -40{,}000 \ \text{€}$$

## Checks and official key

- **Check of Step 1:** $10{,}000{,}000 \times (1.3 - 1.0) - 3{,}000{,}000 = 0$. ✓
- **Units:** €/(€/pack) = packs.
- **Check against the official key** (BEP  OL Statements  Solutions.pdf, p. 7): $FC = 3{,}000{,}000$ €, $VC = 1.0$ €/unit, $FC_{2009} = 3{,}450{,}000$ €, $VC_{2009} = 0.99$ €, break-even point 11,129,032 units, and no profit possible because the maximum volume is 11,000,000. Same results; the key calls the packs "bottles" in its last sentence.

---

**Back to:** [[Problem Set - T4 Break-Even Point and Operating Leverage]]
