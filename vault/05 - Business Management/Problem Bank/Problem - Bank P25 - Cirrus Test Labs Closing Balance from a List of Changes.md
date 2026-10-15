---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P25
title: "Cirrus Test Labs: the closing balance sheet from a list of changes"
category: extra_practice_problem
archetype: year-on-year-cash
unit: 3
difficulty: 2
points: 4.0
time_minutes: 40
official: false
origen: "Practice item written for the problem bank (not an official exercise); the three-section cash-flow statement is an extension of Topic 3_Financial Management (I).pdf"
tags:
  - problem-bank
  - extra-practice
  - balance-sheet
  - cash-flow
  - depreciation
  - self-financing
---

# 🧩 Bank P25 — Cirrus Test Labs: the closing balance sheet from a list of changes

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key. The cash-flow statement in three sections is an **extension**.

## Statement

**Cirrus Test Labs S.L.** runs vibration and climatic tests for space equipment. Its balance sheet at 31/12/2024 was (m.u.): equipment at cost 300,000 with accumulated depreciation 90,000; consumables 20,000; accounts receivable 45,000; cash 35,000; contributed capital 200,000; retained earnings 40,000; long-term loan 40,000; accounts payable 30,000.

Its income statement for 2025 shows: test revenue 400,000; consumables used 80,000; staff 210,000; other operating expenses 30,000; depreciation 30,000; interest 2,000; tax rate 25% (payable in 2026).

During 2025 the following also happened:
1. A new shaker table was bought for 60,000: 40,000 paid in 2025, 20,000 to be paid in March 2026.
2. An old climatic chamber, bought for 50,000 and fully depreciated, was scrapped; nothing was received for it.
3. Accounts receivable rose by 15,000; the stock of consumables fell by 4,000; accounts payable rose by 6,000.
4. 10,000 of the long-term loan were repaid.
5. A dividend of 40% of the net income of 2025 was paid in cash on 31 December.
6. A capital increase of 30,000 was subscribed and paid in cash.

## Setup

**Roll-forward of fixed assets:** closing cost = opening cost + purchases − retirements; closing accumulated depreciation = opening + depreciation of the year − depreciation of the retired assets. A fully depreciated asset that is scrapped leaves both lines by the same amount, so no gain or loss arises.

**Extension:** indirect cash-flow statement (see Bank P23).

## (a) Compute the net income and roll forward the equipment and its accumulated depreciation [1.0 pts]

### Hint

The scrapped chamber is removed from the cost **and** from the accumulated depreciation.

### Checkpoint

- Net income 36,000 m.u.
- Equipment at cost 310,000; accumulated depreciation 70,000; net 240,000 m.u.

### Solution

#### Step 1. Net income

$$\text{Income from operations} = 400{,}000 - 80{,}000 - 210{,}000 - 30{,}000 - 30{,}000 = 50{,}000 \text{ m.u.}$$

$$\text{IBT} = 50{,}000 - 2{,}000 = 48{,}000, \qquad \text{Tax} = 0.25 \times 48{,}000 = 12{,}000, \qquad \text{NI} = 36{,}000 \text{ m.u.}$$

#### Step 2. Equipment

| Line | Cost | Accumulated depreciation |
| :--- | ---: | ---: |
| Opening, 31/12/2024 | 300,000 | 90,000 |
| + Shaker table | 60,000 | — |
| + Depreciation of 2025 | — | 30,000 |
| − Scrapped chamber | −50,000 | −50,000 |
| **Closing, 31/12/2025** | **310,000** | **70,000** |

$$\text{Net equipment} = 310{,}000 - 70{,}000 = 240{,}000 \text{ m.u.}$$

## (b) Prepare the balance sheet at 31/12/2025, finding the cash as the balancing item [1.25 pts]

### Hint

Apply each change to its line. The unpaid 20,000 for the shaker table and the tax of 2025 are new current liabilities.

### Checkpoint

- Dividend 14,400; retained earnings 61,600; equity 291,600 m.u.
- Current liabilities 68,000; total 389,600 m.u.; cash 73,600 m.u.

### Solution

#### Step 1. Equity

$$\text{Dividend} = 0.40 \times 36{,}000 = 14{,}400, \qquad \text{RE} = 40{,}000 + 36{,}000 - 14{,}400 = 61{,}600$$

$$E = (200{,}000 + 30{,}000) + 61{,}600 = 291{,}600 \text{ m.u.}$$

#### Step 2. Liabilities and cash

$$L = (40{,}000 - 10{,}000) + (30{,}000 + 6{,}000) + 20{,}000 + 12{,}000 = 30{,}000 + 68{,}000 = 98{,}000 \text{ m.u.}$$

$$\text{TA} = 291{,}600 + 98{,}000 = 389{,}600, \qquad \text{Cash} = 389{,}600 - 240{,}000 - 16{,}000 - 60{,}000 = 73{,}600 \text{ m.u.}$$

#### Step 3. Balance sheet

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Equipment | 310,000 | Contributed capital | 230,000 |
| − Accumulated depreciation | (70,000) | Retained earnings | 61,600 |
| **Non-current assets** | **240,000** | **Equity** | **291,600** |
| Consumables ($20{,}000 - 4{,}000$) | 16,000 | Long-term loan | 30,000 |
| | | **Long-term liabilities** | **30,000** |
| Accounts receivable ($45{,}000 + 15{,}000$) | 60,000 | Accounts payable | 36,000 |
| Cash | 73,600 | Supplier of the shaker table | 20,000 |
| | | Income taxes payable | 12,000 |
| **Current assets** | **149,600** | **Current liabilities** | **68,000** |
| **Total assets** | **389,600** | **Total liabilities and equity** | **389,600** |

## (c) Prepare the cash-flow statement of 2025 and check it against the change in cash [1.25 pts]

### Hint

Only the 40,000 actually paid for the shaker table are an investing outflow; the 20,000 owed will be an outflow of 2026.

### Checkpoint

- CFO 73,000; CFI −40,000; CFF +5,600 m.u.
- Δcash = 38,600 = 73,600 − 35,000 ✓

### Solution

| Section | Computation | m.u. |
| :--- | :--- | ---: |
| Net income | | 36,000 |
| + Depreciation | | 30,000 |
| − Increase in receivables | | −15,000 |
| + Decrease in consumables | | +4,000 |
| + Increase in payables | | +6,000 |
| + Increase in taxes payable | $12{,}000 - 0$ | +12,000 |
| **= CFO** | | **73,000** |
| − Shaker table paid in 2025 | | −40,000 |
| **= CFI** | | **−40,000** |
| − Loan repayment | | −10,000 |
| − Dividend | | −14,400 |
| + Capital increase | | +30,000 |
| **= CFF** | | **+5,600** |
| **Change in cash** | $73{,}000 - 40{,}000 + 5{,}600$ | **38,600** |

$\Delta\text{Cash} = 73{,}600 - 35{,}000 = 38{,}600$ m.u. ✓

## (d) Compute the pay-out and self-financing ratios and explain how the investment of 2025 was financed [0.5 pts]

### Hint

Compare the investing outflow with the cash generated by operations and by each financing source.

### Checkpoint

- Pay-out 40%; self-financing 60% [Slide 23].
- The 40,000 paid were covered by the operations (73,000); the capital increase (30,000) more than covered the dividend and the repayment (24,400).

### Solution

$$\text{Pay-out} = \frac{14{,}400}{36{,}000} = 40\%, \qquad \text{Self-financing} = \frac{21{,}600}{36{,}000} = 60\%$$

The operations generated 73,000 m.u. of cash, enough to pay the 40,000 of the new shaker table on their own; the rest of the investment is supplier credit (20,000). The capital increase (30,000) more than covered the dividend and the loan repayment (24,400), so cash grew by 38,600 m.u.

## Interpretation

- **Scrapping a fully depreciated asset** changes neither profit nor cash; it only cleans up the cost and the accumulated depreciation.
- **Supplier of fixed assets:** a debt for an investment is a liability, not an account payable for operations; its payment will appear in investing flows of 2026.
- **Dimensional check:** all changes in m.u.; ratios dimensionless.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
