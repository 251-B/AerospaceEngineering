---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P23
title: "Pegasus Aerostructures: a plant expansion seen through two balance sheets"
category: extra_practice_problem
archetype: year-on-year-cash
unit: 3
difficulty: 3
points: 4.0
time_minutes: 45
official: false
origen: "Practice item written for the problem bank (not an official exercise); the three-section cash-flow statement is an extension of Topic 3_Financial Management (I).pdf"
tags:
  - problem-bank
  - extra-practice
  - cash-flow
  - working-capital
  - roa
  - roe
  - leverage
---

# 🧩 Bank P23 — Pegasus Aerostructures: a plant expansion seen through two balance sheets

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key. The cash-flow statement in three sections is an **extension**: the course works with the cash account (initial cash + inflows − outflows).

## Statement

In January 2025 **Pegasus Aerostructures S.A.**, a maker of wing ribs, doubled its plant capacity with a 300,000 m.u. investment financed by a new long-term bank loan of 300,000 m.u. drawn on 1/1/2025. Its statements are (m.u.):

| Balance sheet at 31/12 | 2024 | 2025 |
| :--- | ---: | ---: |
| Plant at cost | 500,000 | 800,000 |
| − Accumulated depreciation | (150,000) | (220,000) |
| Inventory | 60,000 | 90,000 |
| Accounts receivable | 70,000 | 110,000 |
| Cash | 50,000 | 73,000 |
| Contributed capital | 300,000 | 300,000 |
| Retained earnings | 80,000 | 110,000 |
| Long-term bank loans | 50,000 | 330,000 |
| Accounts payable | 70,000 | 95,000 |
| Taxes payable | 30,000 | 18,000 |

| Income statement | 2024 | 2025 |
| :--- | ---: | ---: |
| Sales revenue | 820,000 | 900,000 |
| Income from operations | 109,000 | 90,000 |
| Depreciation included above | 50,000 | 70,000 |
| Interest expense | 9,000 | 18,000 |
| Tax rate | 30% | 25% |
| Net income | 70,000 | 54,000 |

In 2025 the old loan was partly repaid, and dividends were paid in cash. No plant was sold.

## Setup

**Extension: cash-flow statement, indirect method.** The change in cash of the year splits into three flows:

$$\Delta\text{Cash} = \underbrace{\text{CFO}}_{\text{operations}} + \underbrace{\text{CFI}}_{\text{investing}} + \underbrace{\text{CFF}}_{\text{financing}}$$

$$\text{CFO} = \text{Net income} + \text{Depreciation} - \Delta\text{Inventory} - \Delta\text{Receivables} + \Delta\text{Payables} + \Delta\text{Taxes payable}$$

Depreciation is added back because it is an expense that did not use cash. An increase in an operating asset absorbs cash; an increase in an operating liability provides it.

**Extension:** working capital $= \text{CA} - \text{CL}$; $\text{ROA} = \text{Income from operations}/\text{TA}$; $\text{ROE} = \text{Net income}/E$ (year-end figures). The debt-to-equity ratio is course material [Slide 36].

## (a) Compute the totals of both balance sheets and the working capital of each year [0.75 pts]

### Hint

All the liabilities in this company except the bank loans are current.

### Checkpoint

- Total assets 530,000 (2024) and 853,000 (2025) m.u.
- Working capital 80,000 → 160,000 m.u. (+80,000).

### Solution

| Block | 2024 | 2025 |
| :--- | ---: | ---: |
| Non-current assets (net plant) | 350,000 | 580,000 |
| Current assets | 180,000 | 273,000 |
| **Total assets** | **530,000** | **853,000** |
| Equity | 380,000 | 410,000 |
| Long-term liabilities | 50,000 | 330,000 |
| Current liabilities | 100,000 | 113,000 |
| **Total liabilities and equity** | **530,000** | **853,000** |

$$\text{WC}_{2024} = 180{,}000 - 100{,}000 = 80{,}000, \qquad \text{WC}_{2025} = 273{,}000 - 113{,}000 = 160{,}000 \text{ m.u.}$$

## (b) Prepare the cash-flow statement of 2025 in three sections [1.5 pts]

### Hint

Find first the two flows the statement does not give: the repayment of the old loan (from the change in total bank loans) and the dividend (from the change in retained earnings).

### Checkpoint

- CFO = 67,000 m.u.
- CFI = −300,000 m.u.
- Repayment 20,000; dividend 24,000; CFF = +256,000 m.u.

### Solution

#### Step 1. Hidden flows

$$\text{Loans: } 50{,}000 + 300{,}000 - \text{Repayment} = 330{,}000 \;\Rightarrow\; \text{Repayment} = 20{,}000 \text{ m.u.}$$

$$\text{Retained earnings: } 80{,}000 + 54{,}000 - \text{Dividend} = 110{,}000 \;\Rightarrow\; \text{Dividend} = 24{,}000 \text{ m.u.}$$

$$\text{Plant: } 800{,}000 - 500{,}000 = 300{,}000 \text{ invested;} \quad 220{,}000 - 150{,}000 = 70{,}000 = \text{depreciation} \;✓$$

#### Step 2. Cash-flow statement 2025 (extension)

| Section | Computation | m.u. |
| :--- | :--- | ---: |
| Net income | | 54,000 |
| + Depreciation | | 70,000 |
| − Increase in inventory | $90{,}000 - 60{,}000$ | −30,000 |
| − Increase in receivables | $110{,}000 - 70{,}000$ | −40,000 |
| + Increase in payables | $95{,}000 - 70{,}000$ | +25,000 |
| − Decrease in taxes payable | $18{,}000 - 30{,}000$ | −12,000 |
| **= Cash flow from operations (CFO)** | | **67,000** |
| − Investment in plant | | −300,000 |
| **= Cash flow from investing (CFI)** | | **−300,000** |
| + New bank loan | | +300,000 |
| − Repayment of the old loan | Step 1 | −20,000 |
| − Dividends paid | Step 1 | −24,000 |
| **= Cash flow from financing (CFF)** | | **+256,000** |

## (c) Check the result against the balance sheets [0.5 pts]

### Hint

The three flows must add up to the change in the cash line.

### Checkpoint

- $67{,}000 - 300{,}000 + 256{,}000 = 23{,}000 = 73{,}000 - 50{,}000$ ✓.

### Solution

$$\text{CFO} + \text{CFI} + \text{CFF} = 67{,}000 - 300{,}000 + 256{,}000 = 23{,}000 \text{ m.u.}$$

$$\Delta\text{Cash} = 73{,}000 - 50{,}000 = 23{,}000 \text{ m.u.} \;✓$$

## (d) Compute ROA, ROE and debt-to-equity for both years and assess the impact of the expansion [1.25 pts]

### Hint

The expansion doubled the asset base in January, but its returns take time to appear. Compare also how the financial structure changed.

### Checkpoint

- ROA 20.6% → 10.6%; ROE 18.4% → 13.2% (extension).
- $L/E$ 0.39 → 1.08.

### Solution

| Ratio | 2024 | 2025 |
| :--- | ---: | ---: |
| ROA $= \text{Income from operations}/\text{TA}$ | $109{,}000/530{,}000 = 20.6\%$ | $90{,}000/853{,}000 = 10.6\%$ |
| ROE $= \text{NI}/E$ | $70{,}000/380{,}000 = 18.4\%$ | $54{,}000/410{,}000 = 13.2\%$ |
| $L/E$ [Slide 36] | $150{,}000/380{,}000 = 0.39$ | $443{,}000/410{,}000 = 1.08$ |

In its first year the expansion has **not yet paid off**: sales grew by only 9.8% while the assets grew by 61%, so the return on assets fell sharply and the higher depreciation (+40%), the doubled interest and the lower tax rate only partly offsetting them pushed the net income down. The financial structure moved from low to balanced leverage, which raises the risk for shareholders [Slide 36]. The operations still generate cash (CFO 67,000) and working capital doubled, so the company is not in liquidity trouble; the question for 2026 is whether sales will fill the new capacity.

## Interpretation

- **Why CFO ≠ net income:** depreciation (+70,000) and the growth of inventory and receivables (−70,000) cancel exactly; the higher payables (+25,000) and the lower tax payable (−12,000) leave CFO 13,000 above the net income.
- **Investment financed long-term:** CFI ≈ −CFF, so the plant was paid with long-term money, not with the cash from operations.
- **Dimensional check:** every flow and change in m.u.; ratios dimensionless.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
