---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P13
title: "Helix Rotor Components: depreciation and cost of goods sold from raw data"
category: extra_practice_problem
archetype: unordered-items
unit: 3
difficulty: 2
points: 4.0
time_minutes: 40
official: false
origen: "Practice item written for the problem bank (not an official exercise), in the style of T3_Financial Statements_EXERCISES.pdf, Exercises 1 and 4"
tags:
  - problem-bank
  - extra-practice
  - depreciation
  - inventory
  - income-statement
  - balance-sheet
---

# 🧩 Bank P13 — Helix Rotor Components: depreciation and cost of goods sold from raw data

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Helix Rotor Components S.A. machines titanium hubs for helicopter rotors. Its list of balances at 31/12/2025 is incomplete: the depreciation and the cost of goods sold were never computed. You have the following data (m.u.); the tax rate is 25%.

**Fixed assets**
- Land, bought on 1/1/2020: 50,000 (not depreciated).
- Building, bought on 1/1/2020 for 200,000; useful life 40 years; no residual value; linear depreciation.
- CNC machinery, bought on 1/4/2024 for 60,000; useful life 5 years; residual value 10% of cost; linear depreciation.

**Inventory of titanium bars:** 18,000 on 1/1/2025; purchases during 2025: 110,000; physical count on 31/12/2025: 24,000.

**Other items of 2025:** sales 210,000; salaries 52,000; utilities 7,000; insurance 3,000. The bank loan of 80,000 carries 5% interest per year (paid on 31/12/2025); 16,000 of it is repayable in 2026 and the rest later.

**Other balances at 31/12/2025:** accounts receivable 19,000; accounts payable 14,000; contributed capital 200,000; retained earnings at 1/1/2025: 12,000; cash 18,840.

**Distribution:** 40% of the net income is paid as a dividend in cash on 31/12/2025, before the balance is drawn; the tax is paid in 2026.

## Setup

| Asset | Cost | Residual | Life | Depreciable base |
| :--- | ---: | ---: | :--- | ---: |
| Building | 200,000 | 0 | 40 years | 200,000 |
| Machinery | 60,000 | 6,000 | 5 years | 54,000 |
| Land | 50,000 | — | not depreciated | — |

Linear depreciation spreads the depreciable base evenly over the useful life, in proportion to the months of use in each year. The cost of goods sold of a trading or manufacturing firm is the inventory consumed: opening inventory plus purchases minus closing inventory.

## (a) Compute the depreciation of 2025 and the accumulated depreciation at 31/12/2025 of the building and the machinery [1.0 pts]

### Hint

The machinery was used for only 9 months in 2024. The residual value is not depreciated. Accumulated depreciation sums every year since purchase.

### Checkpoint

- Building: 5,000 per year; accumulated 30,000 m.u. (6 years).
- Machinery: 10,800 per year; accumulated 8,100 + 10,800 = 18,900 m.u.
- Depreciation expense of 2025: 15,800 m.u.

### Solution

#### Step 1. Building

$$D_{\text{building}} = \frac{200{,}000 - 0}{40} = 5{,}000 \text{ m.u./year}$$

From 1/1/2020 to 31/12/2025 there are 6 full years: accumulated depreciation $= 6 \times 5{,}000 = 30{,}000$ m.u.

#### Step 2. Machinery

$$D_{\text{machinery}} = \frac{60{,}000 - 0.10 \times 60{,}000}{5} = \frac{54{,}000}{5} = 10{,}800 \text{ m.u./year}$$

In 2024 it was used from 1/4 to 31/12, that is 9 months:

$$D_{2024} = 10{,}800 \times \frac{9}{12} = 8{,}100 \text{ m.u.}, \qquad D_{2025} = 10{,}800 \text{ m.u.}$$

$$\text{Accumulated depreciation}_{31/12/2025} = 8{,}100 + 10{,}800 = 18{,}900 \text{ m.u.}$$

#### Step 3. Expense of the year

$$D_{2025} = 5{,}000 + 10{,}800 = 15{,}800 \text{ m.u.}$$

## (b) Compute the cost of goods sold and prepare the income statement for 2025 [1.25 pts]

### Hint

What was available to sell in 2025 is the opening inventory plus the purchases; what was not sold is still on the shelf at 31/12.

### Checkpoint

- Cost of goods sold 104,000 m.u.; gross profit 106,000 m.u.
- Income from operations 28,200; income before taxes 24,200 m.u.
- Net income 18,150 m.u.

### Solution

#### Step 1. Cost of goods sold

$$\text{COGS} = 18{,}000 + 110{,}000 - 24{,}000 = 104{,}000 \text{ m.u.}$$

#### Step 2. Interest

$$I = 0.05 \times 80{,}000 = 4{,}000 \text{ m.u.}$$

#### Step 3. Income statement

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | | 210,000 |
| − Cost of goods sold | Step 1 | 104,000 |
| **= Gross profit** | $210{,}000 - 104{,}000$ | **106,000** |
| − Salaries | | 52,000 |
| − Utilities and insurance | $7{,}000 + 3{,}000$ | 10,000 |
| − Depreciation | Part (a) | 15,800 |
| **= Income from operations** | $106{,}000 - (52{,}000 + 10{,}000 + 15{,}800) = 106{,}000 - 77{,}800$ | **28,200** |
| − Interest expense | Step 2 | 4,000 |
| **= Income before taxes** | $28{,}200 - 4{,}000$ | **24,200** |
| − Income taxes (25%) | $0.25 \times 24{,}200$ | 6,050 |
| **= Net income** | $24{,}200 - 6{,}050$ | **18,150** |

## (c) Prepare the balance sheet at 31/12/2025 [1.25 pts]

### Hint

The dividend is already paid in cash, so it is no longer a liability; only 60% of the net income reaches retained earnings. Split the loan by maturity.

### Checkpoint

- Dividend 7,260; retained earnings at 31/12 = 22,890 m.u.
- Non-current assets 261,100; current assets 61,840 m.u.
- Total 322,940 m.u. on both sides.

### Solution

#### Step 1. Retained earnings [Slide 23]

$$\text{Dividend} = 0.40 \times 18{,}150 = 7{,}260, \qquad \text{Retained earnings}_{31/12} = 12{,}000 + 18{,}150 - 7{,}260 = 22{,}890 \text{ m.u.}$$

#### Step 2. Balance sheet

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Land | 50,000 | Contributed capital | 200,000 |
| Building (200,000 − 30,000) | 170,000 | Retained earnings | 22,890 |
| Machinery (60,000 − 18,900) | 41,100 | **Equity** | **222,890** |
| **Non-current assets** | **261,100** | Bank loan due after 2026 | 64,000 |
| Inventory | 24,000 | **Long-term liabilities** | **64,000** |
| Accounts receivable | 19,000 | Bank loan due in 2026 | 16,000 |
| Cash | 18,840 | Accounts payable | 14,000 |
| | | Income taxes payable | 6,050 |
| **Current assets** | **61,840** | **Current liabilities** | **36,050** |
| **Total assets** | **322,940** | **Total liabilities and equity** | **322,940** |

## (d) Compute the working capital and the debt-to-equity ratio and comment [0.5 pts]

### Hint

Working capital is an extension of the course: current assets minus current liabilities.

### Checkpoint

- Working capital 25,790 m.u. (extension).
- Debt-to-equity $100{,}050 / 222{,}890 = 0.45$.

### Solution

$$\text{Working capital} = 61{,}840 - 36{,}050 = 25{,}790 \text{ m.u.}, \qquad \frac{L}{E} = \frac{64{,}000 + 36{,}050}{222{,}890} = \frac{100{,}050}{222{,}890} = 0.45$$

The company finances itself mostly with equity (69% of the total) and keeps a positive working capital, so it is both liquid and solvent. Low leverage means low risk for shareholders, but also that the profitability of equity is not amplified by debt [Slide 36].

## Interpretation

- **Dimensional check:** depreciation in m.u./year times years (or months/12) gives m.u.
- **Sensitivity:** forgetting the residual value would raise the machinery's yearly depreciation to 12,000 m.u. and lower the net income by $0.75 \times 1{,}200 = 900$ m.u.
- **Land is never depreciated:** it has no limited useful life.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
