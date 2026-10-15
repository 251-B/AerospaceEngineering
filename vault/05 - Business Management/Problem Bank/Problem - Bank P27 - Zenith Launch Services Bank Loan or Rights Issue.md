---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P27
title: "Zenith Launch Services: financing a new pad with a bank loan or a rights issue"
category: extra_practice_problem
archetype: financing-leverage
unit: 3
difficulty: 2
points: 4.0
time_minutes: 40
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 20, 25-26, 31 and 36; the leverage formula is an extension"
tags:
  - problem-bank
  - extra-practice
  - financial-leverage
  - roa
  - roe
  - financing-decisions
---

# 🧩 Bank P27 — Zenith Launch Services: financing a new pad with a bank loan or a rights issue

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key. ROA, ROE and the leverage formula are **extensions** of the course.

## Statement

**Zenith Launch Services S.A.** integrates small satellites into rockets. It has total assets of 3,000,000 m.u., financed entirely with equity (300,000 shares of nominal value 10 m.u.), and no debt. Its income from operations is 600,000 m.u. per year.

It wants to build a second integration pad costing 2,000,000 m.u., which would add 300,000 m.u. per year to the income from operations. Two financing options are on the table:

- **Option A:** a long-term bank loan of 2,000,000 m.u. at 7% per year.
- **Option B:** a rights issue of 200,000 new shares at 10 m.u. each (no premium).

The tax rate is 25%. Assume the year-end balance sheet equals the opening one plus the new financing (no repayment in the year).

## Setup

| Item | Option A (debt) | Option B (equity) |
| :--- | ---: | ---: |
| Total assets | 5,000,000 | 5,000,000 |
| Equity $E$ | 3,000,000 | 5,000,000 |
| Liabilities $L$ | 2,000,000 | 0 |
| Shares | 300,000 | 500,000 |
| Income from operations | 900,000 | 900,000 |

The investment decision (what to invest in) is the same in both options; only the **financing decision** changes [Slides 3, 20]. Debt has an explicit cost, the interest; equity has an implicit, opportunity cost [Slide 37].

**Extensions.** $\text{ROA} = \text{Income from operations}/\text{TA}$; $\text{ROE} = \text{NI}/E$; earnings per share $= \text{NI}/\text{number of shares}$. With $i$ the interest rate and $t$ the tax rate:

$$\text{ROE} = \left[\text{ROA} + (\text{ROA} - i)\,\frac{L}{E}\right](1 - t)$$

## (a) Prepare the income statement of the first year under each option [1.25 pts]

### Hint

The income from operations is the same in both options: the financing choice only changes the lines below it.

### Checkpoint

- A: interest 140,000; income before taxes 760,000; net income 570,000 m.u.
- B: interest 0; income before taxes 900,000; net income 675,000 m.u.

### Solution

| Line | Option A | Option B |
| :--- | ---: | ---: |
| **Income from operations** | **900,000** | **900,000** |
| − Interest ($0.07 \times 2{,}000{,}000$ in A) | 140,000 | 0 |
| **= Income before taxes** | **760,000** | **900,000** |
| − Income taxes (25%) | 190,000 | 225,000 |
| **= Net income** | **570,000** | **675,000** |

Option B gives a larger net income in m.u., but it is shared among more owners' money: the next part compares the returns.

## (b) Compute ROA, ROE, debt-to-equity, % equity and earnings per share for each option [1.0 pts]

### Hint

The ROA does not depend on the financing; ROE and earnings per share do.

### Checkpoint

- ROA 18% in both options.
- ROE: A 19.0%, B 13.5%; $L/E$: A 0.67, B 0.
- Earnings per share: A 1.90, B 1.35 m.u.

### Solution

| Ratio | Option A | Option B |
| :--- | ---: | ---: |
| ROA | $900{,}000/5{,}000{,}000 = 18\%$ | $18\%$ |
| ROE | $570{,}000/3{,}000{,}000 = 19.0\%$ | $675{,}000/5{,}000{,}000 = 13.5\%$ |
| $L/E$ [Slide 36] | $2{,}000{,}000/3{,}000{,}000 = 0.67$ | $0$ |
| % Equity [Slide 36] | $3{,}000{,}000/5{,}000{,}000 = 60\%$ | $100\%$ |
| Earnings per share | $570{,}000/300{,}000 = 1.90$ | $675{,}000/500{,}000 = 1.35$ |

## (c) Verify the ROE of each option with the leverage formula and explain the leverage effect [1.0 pts]

### Hint

Substitute ROA = 0.18, $i = 0.07$, $t = 0.25$ and each option's $L/E$.

### Checkpoint

- A: $[0.18 + 0.11 \times 0.667] \times 0.75 = 0.19$ ✓
- B: $0.18 \times 0.75 = 0.135$ ✓
- Debt raises the ROE because ROA (18%) > cost of debt (7%).

### Solution

**Option A:**

$$\text{ROE}_A = \left[0.18 + (0.18 - 0.07) \times \frac{2{,}000{,}000}{3{,}000{,}000}\right](1 - 0.25) = \left[0.18 + 0.11 \times 0.667\right] \times 0.75 = 0.2533 \times 0.75 = 0.19$$

**Option B** ($L/E = 0$):

$$\text{ROE}_B = 0.18 \times 0.75 = 0.135$$

Both agree with part (b). Each m.u. borrowed earns 18% in the company and costs only 7%; the difference of 11 points goes to the shareholders, multiplied by the leverage $L/E$. That is the positive **financial leverage effect**: as long as $\text{ROA} > i$, debt raises the return on equity.

## (d) Recommend an option, taking risk into account [0.75 pts]

### Hint

Higher leverage tends to indicate higher risk for shareholders [Slide 36]. What would happen to Option A if the ROA fell below 7%?

### Checkpoint

- A maximises ROE and earnings per share, and keeps control with the current shareholders.
- A adds a fixed charge of 140,000 m.u. per year: if ROA < 7%, leverage turns against the owners.
- B is safer but dilutes the owners and lowers ROE.

### Solution

With the expected figures, **Option A** is better for the current shareholders: ROE rises from the 15% of today ($0.20 \times 0.75$) to 19%, earnings per share from 1.50 to 1.90, and no new shareholders enter. Its cost is risk: the company commits to 140,000 m.u. of interest every year and to repaying the principal [Slide 31]. If launch demand fell and the ROA dropped below 7%, debt would reduce the ROE instead of raising it.

**Option B** never has to be repaid and adds no fixed charge [Slide 25], but it lowers the ROE to 13.5% and spreads the profit over 500,000 shares. A firm with stable demand and moderate leverage after the loan ($L/E = 0.67$) can reasonably choose A; if demand is very uncertain, B (or a mix of both) protects the company.

## Interpretation

- **Before the project:** ROA $= 600{,}000/3{,}000{,}000 = 20\%$; the project's own return is $300{,}000/2{,}000{,}000 = 15\%$, still well above the 7% cost of debt.
- **Dimensional check:** ratios dimensionless; earnings per share in m.u./share.
- **Key idea:** the investment creates the ROA; the financing decision decides how that return is shared between lenders, the State (taxes) and owners.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
