---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P26
title: "Sirius Flight Academy: from accrual figures to collections, payments and cash"
category: extra_practice_problem
archetype: year-on-year-cash
unit: 3
difficulty: 3
points: 4.0
time_minutes: 45
official: false
origen: "Practice item written for the problem bank (not an official exercise); the cash account follows T3_Additional_SOLUTIONS.pdf, the indirect reconciliation is an extension"
tags:
  - problem-bank
  - extra-practice
  - cash
  - accrual-vs-cash
  - unearned-revenue
  - cash-flow
---

# 🧩 Bank P26 — Sirius Flight Academy: from accrual figures to collections, payments and cash

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key. The reconciliation of net income with operating cash (indirect method) is an **extension**.

## Statement

**Sirius Flight Academy S.L.** trains commercial pilots. Students may pay before their course starts (prepaid courses) or after finishing a module. Its income statement for 2025 is (m.u.): tuition revenue 500,000; fuel and maintenance 140,000; instructors' salaries 220,000; hangar rent 36,000; depreciation of aircraft and simulators 60,000; interest 8,000; corporate tax 30%.

Selected balances at 31/12 (m.u.):

| Item | 2024 | 2025 |
| :--- | ---: | ---: |
| Cash | 60,000 | ? |
| Tuition pending from students | 40,000 | 55,000 |
| Courses prepaid by students, not yet taught | 30,000 | 40,000 |
| Owed to fuel and maintenance suppliers | 18,000 | 12,000 |
| Salaries payable | 10,000 | 10,000 |
| Taxes payable | 9,000 | 10,800 |

During 2025 Sirius also bought a new flight simulator for 120,000 in cash, received a long-term bank loan of 80,000, and paid dividends of 12,000. Rent and interest were paid in the year in which they were incurred.

## Setup

**Accrual vs cash** [Slide 8]: revenue is recorded when the course is taught, and the collection may happen before (prepaid course, a liability) or after (tuition pending, an asset). For each flow:

$$\text{Collections} = \text{Revenue} - \Delta\,\text{Tuition pending} + \Delta\,\text{Prepaid courses}$$

$$\text{Payments to suppliers} = \text{Expense} - \Delta\,\text{Amount owed to suppliers}$$

**Course cash account** (T3_Additional_SOLUTIONS.pdf): $\text{Cash at end} = \text{Initial cash} + \text{Cash inflows} - \text{Cash outflows}$.

## (a) Compute the net income and the cash collected from students in 2025 [0.75 pts]

### Hint

Tuition pending grew: part of the revenue was not collected. Prepaid courses grew: students paid for courses not yet taught.

### Checkpoint

- Net income 25,200 m.u. (tax 10,800).
- Collections 495,000 m.u.

### Solution

$$\text{Income from operations} = 500{,}000 - 140{,}000 - 220{,}000 - 36{,}000 - 60{,}000 = 44{,}000$$

$$\text{IBT} = 44{,}000 - 8{,}000 = 36{,}000, \qquad \text{Tax} = 0.30 \times 36{,}000 = 10{,}800, \qquad \text{NI} = 25{,}200 \text{ m.u.}$$

$$\text{Collections} = 500{,}000 - (55{,}000 - 40{,}000) + (40{,}000 - 30{,}000) = 500{,}000 - 15{,}000 + 10{,}000 = 495{,}000 \text{ m.u.}$$

## (b) Compute every operating payment of 2025 [1.0 pts]

### Hint

Apply the same correction to every expense: expense minus the increase in what is still owed. The corporate tax works the same way. Depreciation is not a payment.

### Checkpoint

- Suppliers 146,000; salaries 220,000; rent 36,000; interest 8,000; tax 9,000 m.u.
- Total operating payments 419,000 m.u.

### Solution

| Payment | Computation | m.u. |
| :--- | :--- | ---: |
| Fuel and maintenance suppliers | $140{,}000 - (12{,}000 - 18{,}000)$ | 146,000 |
| Salaries | $220{,}000 - (10{,}000 - 10{,}000)$ | 220,000 |
| Hangar rent | | 36,000 |
| Interest | | 8,000 |
| Corporate tax (tax of 2024) | $10{,}800 - (10{,}800 - 9{,}000)$ | 9,000 |
| **Total operating payments** | | **419,000** |

The amount owed to suppliers fell, so Sirius paid more than the expense of the year: it also settled part of what it owed from 2024.

## (c) Prepare the cash account of 2025 and find the cash at 31/12/2025 [1.0 pts]

### Hint

Add the non-operating flows: the simulator, the loan and the dividend.

### Checkpoint

- Inflows 575,000; outflows 551,000 m.u.
- Cash at 31/12/2025: 84,000 m.u.

### Solution

| Inflows | m.u. | Outflows | m.u. |
| :--- | ---: | :--- | ---: |
| Collections from students | 495,000 | Operating payments | 419,000 |
| Long-term bank loan | 80,000 | Flight simulator | 120,000 |
| | | Dividends | 12,000 |
| **Total** | **575,000** | **Total** | **551,000** |

$$\text{Cash}_{31/12/2025} = 60{,}000 + 575{,}000 - 551{,}000 = 84{,}000 \text{ m.u.}$$

## (d) Reconcile the net income with the operating cash flow and explain the difference [1.25 pts]

### Hint

Start from the net income and correct it for each item that is in the income statement but did not move cash in the same amount.

### Checkpoint

- Operating cash flow (direct): $495{,}000 - 419{,}000 = 76{,}000$ m.u.
- Indirect: $25{,}200 + 60{,}000 - 15{,}000 + 10{,}000 - 6{,}000 + 0 + 1{,}800 = 76{,}000$ ✓

### Solution

#### Step 1. Direct method

$$\text{CFO} = \text{Collections} - \text{Operating payments} = 495{,}000 - 419{,}000 = 76{,}000 \text{ m.u.}$$

#### Step 2. Indirect method (extension)

| Item | m.u. |
| :--- | ---: |
| Net income | 25,200 |
| + Depreciation (expense without payment) | 60,000 |
| − Increase in tuition pending | −15,000 |
| + Increase in prepaid courses | +10,000 |
| − Decrease in amounts owed to suppliers | −6,000 |
| ± Change in salaries payable | 0 |
| + Increase in taxes payable | +1,800 |
| **= CFO** | **76,000** |

#### Step 3. Why net income and cash differ

Profit measures what Sirius **earned** in 2025; cash measures what it **received and paid**. The largest gap is depreciation (60,000), an expense that consumes no cash in the year. Students who still owe tuition reduce cash; students who prepay increase it; settling old supplier debts reduces it. Both methods give the same 76,000 m.u. because they describe the same transactions from two sides.

## Interpretation

- **Full cash check:** $\text{CFO} + \text{CFI} + \text{CFF} = 76{,}000 - 120{,}000 + (80{,}000 - 12{,}000) = 24{,}000 = 84{,}000 - 60{,}000$ ✓.
- **Prepaid courses are liabilities:** the academy owes the training, which is why an increase brings cash in without being revenue yet [Slide 13].
- **Dimensional check:** every term in m.u.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
