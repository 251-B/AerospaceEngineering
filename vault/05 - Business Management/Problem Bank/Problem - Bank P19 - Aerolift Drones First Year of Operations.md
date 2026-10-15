---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P19
title: "Aerolift Drones: the first year told as a story"
category: extra_practice_problem
archetype: narrative-case
unit: 3
difficulty: 2
points: 4.0
time_minutes: 45
official: false
origen: "Practice item written for the problem bank (not an official exercise), in the style of T3_Additional_EXERCISES.pdf, Exercises 1 and 2"
tags:
  - problem-bank
  - extra-practice
  - income-statement
  - balance-sheet
  - cash
  - depreciation
---

# 🧩 Bank P19 — Aerolift Drones: the first year told as a story

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Two aerospace engineers founded **Aerolift Drones S.L.** on 1 January 2025 to assemble cargo drones for mountain rescue teams. Their consultant summarises the first year as follows (m.u.).

The partners contributed 120,000 in cash on 1 January, and the same day a bank lent the company 100,000 at 6% per year for five years: on each 31 December the company repays 20,000 and pays the interest on the balance outstanding at the start of that year. On 1 March they bought the assembly line for 90,000; they paid 60,000 on delivery and agreed to pay the remaining 30,000 on 1 March 2026. The line will last six years, after which it can be sold for 18,000, and it is depreciated linearly.

During the year they bought 1,000 drone kits at 150 each, the same number every month, paying the suppliers 90 days after each purchase. They sold 900 drones at 400 each, also evenly over the twelve months; the rescue teams pay 60 days after each sale. The 100 kits not yet assembled were still in the warehouse on 31 December.

Salaries cost 8,000 per month, paid in the same month; Social Security adds 2,500 per month, paid in the following month. The workshop rent is 2,000 per month, paid monthly. The corporate tax is 25% of the profit and will be paid in 2026. No dividends are distributed.

## Setup

**Timeline.** Every flow is spread evenly over the months, so "paid 90 days later" means that the purchases of October, November and December are unpaid at 31/12; "collected 60 days later" leaves November and December sales uncollected.

| Data | Value |
| :--- | :--- |
| Kits | 1,000 at 150 = 150,000 (12,500 per month), paid at 90 days |
| Sales | 900 at 400 = 360,000 (30,000 per month), collected at 60 days |
| Assembly line | 90,000 on 1/3; 60,000 paid, 30,000 due 1/3/2026; 6 years; residual 18,000 |
| Loan | 100,000 at 6%; 20,000 repaid each 31/12 |
| Staff | 8,000/month salaries (paid same month) + 2,500/month Social Security (paid next month) |

**Accrual principle.** Revenues are recorded when the sale is made and expenses when the goods and services are received, whether paid or not [Slide 8]. Cash only records what was actually collected or paid.

## (a) Prepare the income statement for 2025 [1.25 pts]

### Hint

Only the 900 kits used in the drones sold are an expense of 2025; the other 100 are inventory. The assembly line worked for 10 months.

### Checkpoint

- Cost of goods sold 135,000; depreciation 10,000 m.u.
- Income from operations 65,000; interest 6,000 m.u.
- Net income 44,250 m.u.

### Solution

#### Step 1. Cost of goods sold and depreciation

$$\text{COGS} = 900 \times 150 = 135{,}000 \text{ m.u.} \quad (= 150{,}000 - 15{,}000 \text{ closing inventory})$$

$$D = \frac{90{,}000 - 18{,}000}{6} \times \frac{10}{12} = 12{,}000 \times \frac{10}{12} = 10{,}000 \text{ m.u.}$$

#### Step 2. Interest

$$I_{2025} = 0.06 \times 100{,}000 = 6{,}000 \text{ m.u.}$$

#### Step 3. Income statement

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | $900 \times 400$ | 360,000 |
| − Cost of goods sold | Step 1 | 135,000 |
| **= Gross profit** | $360{,}000 - 135{,}000$ | **225,000** |
| − Salaries and Social Security | $12 \times (8{,}000 + 2{,}500)$ | 126,000 |
| − Rent | $12 \times 2{,}000$ | 24,000 |
| − Depreciation | Step 1 | 10,000 |
| **= Income from operations** | $225{,}000 - (126{,}000 + 24{,}000 + 10{,}000) = 225{,}000 - 160{,}000$ | **65,000** |
| − Interest expense | Step 2 | 6,000 |
| **= Income before taxes** | $65{,}000 - 6{,}000$ | **59,000** |
| − Income taxes (25%) | $0.25 \times 59{,}000$ | 14,750 |
| **= Net income** | $59{,}000 - 14{,}750$ | **44,250** |

## (b) Compute the cash balance at 31/12/2025 [1.0 pts]

### Hint

Use the course's cash account: initial cash + collections − payments. List what is still unpaid or uncollected at 31/12 first; everything else moved cash.

### Checkpoint

- Collections from customers 300,000; payments to suppliers 112,500 m.u.
- Social Security paid 27,500 (11 months) m.u.
- Cash at 31/12/2025: 174,000 m.u.

### Solution

#### Step 1. What is still open at 31/12

- Customers: November and December sales, $2 \times 30{,}000 = 60{,}000$ uncollected → collected $360{,}000 - 60{,}000 = 300{,}000$.
- Suppliers of kits: October to December, $3 \times 12{,}500 = 37{,}500$ unpaid → paid $150{,}000 - 37{,}500 = 112{,}500$.
- Social Security of December, 2,500 unpaid → paid $11 \times 2{,}500 = 27{,}500$.
- Assembly line: 30,000 unpaid → paid 60,000.

#### Step 2. Cash account (initial cash + inflows − outflows)

| Inflows | m.u. | Outflows | m.u. |
| :--- | ---: | :--- | ---: |
| Capital | 120,000 | Assembly line | 60,000 |
| Bank loan | 100,000 | Suppliers of kits | 112,500 |
| Collections from customers | 300,000 | Salaries | 96,000 |
| | | Social Security | 27,500 |
| | | Rent | 24,000 |
| | | Interest | 6,000 |
| | | Loan repayment | 20,000 |
| **Total** | **520,000** | **Total** | **346,000** |

$$\text{Cash}_{31/12} = 0 + 520{,}000 - 346{,}000 = 174{,}000 \text{ m.u.}$$

## (c) Prepare the balance sheet at 31/12/2025 [1.25 pts]

### Hint

Every amount "still open" in part (b) is either a receivable or a payable. Split the loan: the instalment of 31/12/2026 is current.

### Checkpoint

- Non-current assets 80,000; current assets 249,000 m.u.
- Equity 164,250; current liabilities 104,750 m.u.
- Total 329,000 m.u.

### Solution

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Assembly line | 90,000 | Contributed capital | 120,000 |
| − Accumulated depreciation | (10,000) | Retained earnings (profit of 2025) | 44,250 |
| **Non-current assets** | **80,000** | **Equity** | **164,250** |
| Inventory (100 kits × 150) | 15,000 | Bank loan due after 2026 | 60,000 |
| Accounts receivable | 60,000 | **Long-term liabilities** | **60,000** |
| Cash | 174,000 | Bank loan due 31/12/2026 | 20,000 |
| | | Supplier of the assembly line | 30,000 |
| | | Suppliers of kits | 37,500 |
| | | Social Security payable | 2,500 |
| | | Income taxes payable | 14,750 |
| **Current assets** | **249,000** | **Current liabilities** | **104,750** |
| **Total assets** | **329,000** | **Total liabilities and equity** | **329,000** |

## (d) Give a short diagnosis of the financial health of Aerolift [0.5 pts]

### Hint

Compute the working capital (extension) and the debt-to-equity ratio, then ask whether the cash balance is well used.

### Checkpoint

- Working capital 144,250 m.u. (extension); $L/E = 164{,}750/164{,}250 = 1.00$.
- Idle cash of 174,000 m.u. while paying 6% on the loan.

### Solution

$$\text{Working capital} = 249{,}000 - 104{,}750 = 144{,}250 \text{ m.u.}, \qquad \frac{L}{E} = \frac{60{,}000 + 104{,}750}{164{,}250} = 1.00$$

The first year is profitable (net margin $44{,}250/360{,}000 = 12.3\%$) and liquid: the current assets more than double the current liabilities. Leverage is balanced (one m.u. of debt per m.u. of equity). The weak point is the large idle cash balance: 174,000 m.u. earn nothing while the loan costs 6%. The company could repay debt early or invest in a second assembly line.

## Interpretation

- **Profit vs cash:** net income 44,250 m.u., but cash grew by 174,000 m.u. because it also received the capital and the loan, and because part of its expenses (kits, tax, Social Security) is still unpaid.
- **Dimensional check:** units × m.u./unit = m.u.; m.u./year × months/12 = m.u.
- **Typical mistakes:** expensing all 1,000 kits, depreciating 12 months, and forgetting that the residual value is not depreciated.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
