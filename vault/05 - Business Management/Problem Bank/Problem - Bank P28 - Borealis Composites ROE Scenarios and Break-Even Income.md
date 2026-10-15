---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P28
title: "Borealis Composites: ROE in three scenarios and the break-even income from operations"
category: extra_practice_problem
archetype: financing-leverage
unit: 3
difficulty: 3
points: 4.0
time_minutes: 45
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slide 36; ROE and the break-even analysis are extensions"
tags:
  - problem-bank
  - extra-practice
  - financial-leverage
  - risk
  - roe
  - scenarios
---

# 🧩 Bank P28 — Borealis Composites: ROE in three scenarios and the break-even income from operations

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key. ROE and the break-even analysis are **extensions** of the course.

## Statement

The founders of **Borealis Composites S.A.**, a supplier of thermoplastic brackets for aircraft cabins, need 1,000,000 m.u. to start. They hesitate between two financial structures:

- **Plan X:** 1,000,000 m.u. of equity, no debt.
- **Plan Y:** 400,000 m.u. of equity and a bank loan of 600,000 m.u. at 8% per year.

The tax rate is 30%; a year with a loss pays no tax. The income from operations of the first year depends on the market:

| Scenario | Income from operations (m.u.) |
| :--- | ---: |
| Downturn | 40,000 |
| Base | 100,000 |
| Boom | 180,000 |

## Setup

The assets (1,000,000 m.u.) and the income from operations are the same under both plans; only the interest and the equity base change. $\text{ROE} = \text{NI}/E$ and $\text{ROA} = \text{Income from operations}/\text{TA}$ (extensions).

Interest under Plan Y: $I = 0.08 \times 600{,}000 = 48{,}000$ m.u. per year, in every scenario.

## (a) Compute the net income and the ROE of each plan in each scenario [1.5 pts]

### Hint

Under Plan Y, check first whether the income from operations covers the 48,000 of interest. If it does not, there is a loss and no tax.

### Checkpoint

- Plan X ROE: 2.8% / 7.0% / 12.6%.
- Plan Y ROE: −2.0% / 9.1% / 23.1%.

### Solution

#### Step 1. Plan X (no debt)

$$\text{NI} = (1 - 0.30) \times \text{Income from operations}, \qquad \text{ROE} = \frac{\text{NI}}{1{,}000{,}000}$$

| Scenario | IBT | Tax | NI | ROE |
| :--- | ---: | ---: | ---: | ---: |
| Downturn | 40,000 | 12,000 | 28,000 | 2.8% |
| Base | 100,000 | 30,000 | 70,000 | 7.0% |
| Boom | 180,000 | 54,000 | 126,000 | 12.6% |

#### Step 2. Plan Y (debt of 600,000 at 8%)

$$\text{IBT} = \text{Income from operations} - 48{,}000, \qquad \text{ROE} = \frac{\text{NI}}{400{,}000}$$

| Scenario | IBT | Tax | NI | ROE |
| :--- | ---: | ---: | ---: | ---: |
| Downturn | $40{,}000 - 48{,}000 = -8{,}000$ | 0 | −8,000 | −2.0% |
| Base | $100{,}000 - 48{,}000 = 52{,}000$ | 15,600 | 36,400 | 9.1% |
| Boom | $180{,}000 - 48{,}000 = 132{,}000$ | 39,600 | 92,400 | 23.1% |

## (b) Find the income from operations at which both plans give the same ROE, and relate it to the ROA and the interest rate [1.0 pts]

### Hint

Set $\text{ROE}_X = \text{ROE}_Y$ with the income from operations as the unknown $B$, assuming the result is positive so both plans pay tax.

### Checkpoint

- $B = 80{,}000$ m.u.; ROE = 5.6% in both plans.
- At that point ROA = 8% = interest rate.

### Solution

$$\frac{0.70\,B}{1{,}000{,}000} = \frac{0.70\,(B - 48{,}000)}{400{,}000}$$

Dividing both sides by 0.70 and cross-multiplying:

$$400{,}000\,B = 1{,}000{,}000\,(B - 48{,}000) \;\Rightarrow\; 600{,}000\,B = 48{,}000{,}000{,}000 \;\Rightarrow\; B = 80{,}000 \text{ m.u.}$$

$$\text{ROE}_X = \text{ROE}_Y = \frac{0.70 \times 80{,}000}{1{,}000{,}000} = 5.6\%, \qquad \text{ROA} = \frac{80{,}000}{1{,}000{,}000} = 8\% = i$$

Above 80,000 m.u. (ROA > 8%) debt raises the ROE; below it, debt lowers it.

## (c) Compute the debt-to-equity ratio and % equity of each plan and the spread of ROE across scenarios; relate them to risk [0.75 pts]

### Hint

The spread (boom minus downturn) is a simple measure of how much the owners' return varies.

### Checkpoint

- X: $L/E = 0$, 100% equity, spread 9.8 points.
- Y: $L/E = 1.5$, 40% equity, spread 25.1 points.

### Solution

| Plan | $L/E$ | % Equity | ROE spread |
| :--- | ---: | ---: | ---: |
| X | 0 | 100% | $12.6\% - 2.8\% = 9.8$ points |
| Y | $600{,}000/400{,}000 = 1.5$ | 40% | $23.1\% - (-2.0\%) = 25.1$ points |

The same business risk (income from operations from 40,000 to 180,000) becomes a much larger risk for the owners under Plan Y: debt amplifies the ROE both upward and downward. This is what the course means by "higher leverage ratios tend to indicate higher risk for shareholders" [Slide 36].

## (d) Which plan would you recommend if the base scenario is the most likely but a downturn is possible? [0.75 pts]

### Hint

Compare the expected return with what happens in the bad case, including the obligation to pay interest whatever the result.

### Checkpoint

- Base: Y beats X (9.1% vs 7.0%) because the base ROA (10%) exceeds 8%.
- Downturn: Y makes a loss and still owes 48,000 of interest; X stays profitable.
- A reasoned answer either way; a start-up usually favours less debt.

### Solution

In the most likely scenario, Plan Y gives the owners 9.1% instead of 7.0% while requiring them to invest only 400,000 m.u. But Plan Y commits the company to 48,000 m.u. of interest every year: in a downturn it makes a loss, consumes cash and depends on the bank's patience. For a **start-up** with no track record, whose income is uncertain, Plan X (or an intermediate structure) is the prudent choice; Plan Y suits owners who are confident that the ROA will stay well above 8% and who can bear a bad year.

## Interpretation

- **Rule of thumb (extension):** debt helps the owners exactly when $\text{ROA} > i$; the break-even of part (b) is where $\text{ROA} = i$.
- **Dimensional check:** m.u. on both sides of the break-even equation; ROE dimensionless.
- **Limitation:** the losses of the downturn could be offset against future profits (as in the WIFINET exercise), which would soften the bad case slightly; it is ignored here.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
