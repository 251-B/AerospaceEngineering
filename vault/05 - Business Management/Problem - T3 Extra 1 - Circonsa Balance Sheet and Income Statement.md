---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Additional_EXERCISES.pdf, Exercise 1, pp. 1-2"
dificultad: high
tags:
  - exam-problem
  - solved
  - balance-sheet
  - income-statement
  - circonsa
---

# ✏️ Problem: T3 Additional Exercise 1 — CIRCONSA, statements at 30 June 2015

## 📄 Statement

The financial director of CIRCONSA is working on its financial statements (balance sheet and income statement) as of 30 June 2015. It has the balance of the company as of 31 December 2014 and the following operations that took place from 1 January 2015 to 30 June 2015. The company sells a certain product.

- **i.** During the semester the company sold 1,200 units at 20 m.u./unit (every month the same amount, 200 u.). Customers pay 30 days after the sale. A very important customer (30% of the sales), who bought an equal amount each month, was given a 10% discount on its purchases.
- **ii.** During the semester 1,000 units were purchased (40% in the first quarter and 60% in the second) at 12 m.u./u. Suppliers are paid at 90 days.
- **iii.** At 31/12/2014 there is a stock of 200 units valued at 12 m.u./u.
- **iv.** During the first quarter of 2015 the taxes and the outstanding supplier balances of the previous year were paid.
- **v.** During the first quarter of 2015 the customer debt outstanding from the previous year was collected, except 300 m.u. from a customer who requested to defer payment until July 2016.
- **vi.** Personnel expenses were 350 m.u./month (plus 150 for Social Security) and general expenses 300 m.u./month. Personnel and Social Security are paid in the month in which they occur; overheads two months after.
- **vii.** On 1/04/2015 a renting contract (3 years) for computer equipment was signed with a specialised company, 400 m.u. per month, with payment at 120 days (payment at the end of each month).
- **viii.** On 1/04/2015 a patent was bought for 2,400 m.u., to be paid on 1/07/2015. It is amortised in 4 years.
- **ix.** On 1/02/2015 a credit of 2,000 m.u. was obtained, to be returned a year later with 12% annual interest; interest and principal are paid on 1/02/2016.
- **x.** At 31/12/2014 the company had only one machine, bought on 1/07/2014, amortised linearly with a residual value of 20%.
- **xi.** On 1/02/2015 a capital increase (fully paid, no issue premium) of 10,000 m.u. was made. The same day a new machine costing 12,000 m.u. was bought: 8,000 paid in cash and the remainder on 1/07/2015. It is amortised in 4 years with zero residual value.
- **xii.** Assume a 20% corporate tax, recorded in the balance at 30/06/2015 as "taxes to pay".

**Balance sheet at 31/12/2014 (m.u.):** current assets 5,400 (cash 1,200; accounts receivable 1,800; inventory 2,400); non-current assets 450 (machinery 500; accumulated depreciation 50); current liabilities 800 (unpaid taxes 350; suppliers 450); owners' equity 5,050 (retained earnings 850; paid-in capital 4,200); total 5,850.

**Question:** calculate the balance sheet and the profit and loss account of CIRCONSA at 30 June 2015.

## Phase 1 — Setup: data, timeline and hypotheses

**Period:** 1/01/2015 to 30/06/2015, **6 months**. **Closing instant:** 30/06/2015. Every monthly figure is multiplied by the months it applies inside this window.

| Date | Event |
| :--- | :--- |
| Jan-Mar | Sales 200 u./month; purchases 400 u. (Q1); payment of 2014 taxes and suppliers; collection of 2014 receivables except 300 |
| 1/02 | Credit 2,000 received; capital increase 10,000; machine 2 bought (8,000 paid) |
| 1/04 | Renting starts (400/month); patent bought (2,400, payable 1/07) |
| Apr-Jun | Sales 200 u./month; purchases 600 u. (Q2) |
| 30/06 | **Closing** |
| 1/07 | Payment of patent and of the 4,000 left on machine 2 (after the closing) |

**Hypotheses** (all read from the statement):
1. Sales are uniform (200 u./month) and collected 30 days later, so at 30/06 only **June's sales** are uncollected.
2. Q1 purchases are paid 90 days later, inside the semester; **Q2 purchases** are still unpaid at 30/06.
3. Overheads are paid two months later: January-April are paid, **May and June** are unpaid.
4. The renting is paid at 120 days: none of the April-June instalments has been paid at 30/06.
5. Simple interest, prorated by months. Tax: 20% of income before taxes, left unpaid.
6. Machine 1: its useful life is not given; it is deduced from the opening balance (Phase 3, Step 5).

## Phase 2 — Frames: classification of every operation

The three questions of the method (income statement? cash? open balance item at 30/06?) applied to each operation:

| Op. | Income statement (6 months) | Cash in (+) / out (−) | Open at 30/06 |
| :--- | :--- | :--- | :--- |
| i. Sales | Net sales 23,280 | +19,400 (Jan-May) | Receivables 3,880 (June) |
| ii-iii. Purchases and stock | COGS 14,400 | −4,800 (Q1) | Inventory 0; suppliers 7,200 (Q2) |
| iv. 2014 taxes and suppliers | — | −350 − 450 | — |
| v. 2014 receivables | — | +1,500 | Long-term receivable 300 |
| vi. Personnel + SS | 3,000 | −3,000 | — |
| vi. Overheads | 1,800 | −1,200 (Jan-Apr) | Overheads payable 600 |
| vii. Renting | 1,200 | 0 | Renting payable 1,200 |
| viii. Patent | Amortisation 150 | 0 | Patent 2,400 − 150; patent payable 2,400 |
| ix. Credit | Interest 100 | +2,000 | Credit 2,000; interest payable 100 |
| x. Machine 1 | Depreciation 50 | 0 | Machine 500 − 100 |
| xi. Capital increase | — | +10,000 | Capital +10,000 |
| xi. Machine 2 | Depreciation 1,250 | −8,000 | Machine 12,000 − 1,250; debt 4,000 |
| xii. Tax | 266 | 0 | Taxes payable 266 |

Each figure is derived in Phase 3.

## Phase 3 — Derivation

### Step 1. Sales and receivables (op. i)

Gross sales per month: $200 \times 20 = 4{,}000$ m.u. The important customer buys 30% of them, so its discount per month is

$$0.30 \times 4{,}000 \times 0.10 = 120 \text{ m.u./month}$$

Net sales per month: $4{,}000 - 120 = 3{,}880$ m.u. Over the semester:

$$\text{Net sales} = 6 \times 3{,}880 = 23{,}280 \text{ m.u.} \quad (= 24{,}000 - 720)$$

Collections at 30 days: the sales of January to May are collected by 30/06 ($5 \times 3{,}880 = 19{,}400$); June's sales are still owed: **receivables 3,880**.

### Step 2. Purchases, stock and cost of goods sold (ops. ii, iii)

Units: initial stock 200 + purchases 1,000 = 1,200 available; 1,200 sold, so the ending stock is 0 units. All units cost 12 m.u., so

$$\text{COGS} = \text{Initial inventory} + \text{Purchases} - \text{Ending inventory} = 2{,}400 + 12{,}000 - 0 = 14{,}400 \text{ m.u.}$$

Purchases: Q1 $= 0.40 \times 1{,}000 \times 12 = 4{,}800$, paid at 90 days (inside the semester); Q2 $= 0.60 \times 1{,}000 \times 12 = 7{,}200$, **unpaid at 30/06**.

### Step 3. Items from 2014 (ops. iv, v)

Paid in Q1: taxes 350 and suppliers 450 (cash −800; both liabilities disappear). Collected in Q1: $1{,}800 - 300 = 1{,}500$. The remaining 300 is due in July 2016, more than one year after 30/06/2015, so it becomes a **non-current receivable** [Slide 15].

None of these affects the income statement: they settle revenues and expenses of 2014.

### Step 4. Personnel, overheads and renting (ops. vi, vii)

- Personnel + Social Security: $6 \times (350 + 150) = 3{,}000$, all paid.
- Overheads: $6 \times 300 = 1{,}800$ of expense; paid two months later, so January-April are paid ($4 \times 300 = 1{,}200$) and May-June are owed: **600 payable**.
- Renting: April, May, June, $3 \times 400 = 1{,}200$ of expense; paid at 120 days, nothing paid by 30/06: **1,200 payable**.

### Step 5. Fixed assets: depreciation and amortisation (ops. viii, x, xi)

**Machine 1.** Cost 500, residual value $0.20 \times 500 = 100$, depreciable base $500 - 100 = 400$. The opening accumulated depreciation is 50 for the 6 months from 1/07/2014 to 31/12/2014, so the annual depreciation is $50 \times \frac{12}{6} = 100$ and the useful life is $\frac{400}{100} = 4$ years. For the semester:

$$D_1 = \frac{500 - 100}{4} \times \frac{6}{12} = 50 \text{ m.u.}, \qquad \text{accumulated} = 50 + 50 = 100$$

**Machine 2.** Bought 1/02, used 5 months (February-June), zero residual value:

$$D_2 = \frac{12{,}000 - 0}{4} \times \frac{5}{12} = 1{,}250 \text{ m.u.}$$

**Patent.** Bought 1/04, used 3 months:

$$A = \frac{2{,}400}{4} \times \frac{3}{12} = 150 \text{ m.u.}$$

Total depreciation and amortisation: $50 + 1{,}250 + 150 = 1{,}450$ m.u. None of it is a payment.

Payments: machine 2, 8,000 paid in cash; the other 4,000 and the whole patent (2,400) are due on 1/07/2015, one day after the closing, so they are **current liabilities** at 30/06.

### Step 6. Credit and interest (op. ix)

Received 1/02 (cash +2,000), returned on 1/02/2016, within one year of 30/06/2015: **current liability**. Interest from 1/02 to 30/06 (5 months), paid only in 2016:

$$I = 2{,}000 \times 0.12 \times \frac{5}{12} = 100 \text{ m.u.} \quad \text{(expense and interest payable)}$$

### Step 7. Income statement for the semester

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Net sales | $24{,}000 - 720$ | 23,280 |
| − Cost of goods sold | Step 2 | 14,400 |
| **= Gross profit** | $23{,}280 - 14{,}400$ | **8,880** |
| − Personnel and Social Security | | 3,000 |
| − Overheads | | 1,800 |
| − Renting | | 1,200 |
| − Depreciation and amortisation | $50 + 1{,}250 + 150$ | 1,450 |
| **= Income from operations** | $8{,}880 - 7{,}450$ | **1,430** |
| − Interest expense | Step 6 | 100 |
| **= Income before taxes** | $1{,}430 - 100$ | **1,330** |
| − Income taxes (20%) | $0.20 \times 1{,}330$ | 266 |
| **= Net income** | $1{,}330 - 266$ | **1,064** |

### Step 8. Cash at 30/06/2015

| Inflows | m.u. | Outflows | m.u. |
| :--- | ---: | :--- | ---: |
| Opening cash | 1,200 | 2014 taxes | 350 |
| 2014 receivables collected | 1,500 | 2014 suppliers | 450 |
| Sales Jan-May collected | 19,400 | Q1 purchases | 4,800 |
| Credit | 2,000 | Personnel + SS | 3,000 |
| Capital increase | 10,000 | Overheads Jan-Apr | 1,200 |
| | | Machine 2 (cash part) | 8,000 |
| **Total** | **34,100** | **Total** | **17,800** |

$$\text{Cash}_{30/06} = 34{,}100 - 17{,}800 = 16{,}300 \text{ m.u.}$$

### Step 9. Balance sheet at 30/06/2015

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Machinery (cost $500 + 12{,}000$) | 12,500 | Paid-in capital ($4{,}200 + 10{,}000$) | 14,200 |
| − Accumulated depreciation ($100 + 1{,}250$) | (1,350) | Retained earnings (2014) | 850 |
| Patent ($2{,}400 - 150$) | 2,250 | Net income of the semester | 1,064 |
| Long-term receivable (due July 2016) | 300 | **Equity** | **16,114** |
| **Non-current assets** | **13,700** | Credit (due 1/02/2016) | 2,000 |
| Inventory | 0 | Interest payable | 100 |
| Accounts receivable (June) | 3,880 | Suppliers (Q2 purchases) | 7,200 |
| Cash | 16,300 | Debt for machine 2 (due 1/07) | 4,000 |
| **Current assets** | **20,180** | Debt for patent (due 1/07) | 2,400 |
| | | Overheads payable | 600 |
| | | Renting payable | 1,200 |
| | | Taxes payable | 266 |
| | | **Current liabilities** | **17,766** |
| **Total assets** | **33,880** | **Total liabilities and equity** | **33,880** |

There are no long-term liabilities: every debt is due before 30/06/2016.

## Phase 4 — Interpretation and checks

- **Balance:** $13{,}700 + 20{,}180 = 33{,}880 = 16{,}114 + 17{,}766$.
- **Equity bridge:** equity grows from 5,050 to 16,114, that is $+11{,}064 = 10{,}000$ (capital increase) $+ 1{,}064$ (net income).
- **Profit is not cash:** the semester earns 1,064 but cash grows by $16{,}300 - 1{,}200 = 15{,}100$, mostly because of the capital increase (10,000), the credit (2,000) and the many expenses still unpaid (suppliers, renting, overheads, interest, taxes). In the opposite direction, 8,000 of cash went into a machine whose expense this semester is only 1,250.
- **Limiting case:** if June's sales had been collected, cash would be 3,880 higher and receivables zero, but net income would not change: revenue is recognised when the sale is made [Slide 8].
- **Exam traps:** (1) the 1/07 debts are liabilities at 30/06, not payments; (2) the 300 deferred to July 2016 is non-current; (3) machine 2 is depreciated 5 months and the patent 3 months, not 6; (4) the life of machine 1 must be deduced from the opening balance.

## Check against the official key

> [!info] Official solution, `T3_Additional_SOLUTIONS.pdf`, pp. 6-8
> The income statement and the cash account coincide with the key: net sales 23,280; cost of goods sold 14,400; personnel 3,000; general expenses 1,800; renting 1,200; EBITDA 2,880; depreciation and amortisation 1,450; EBIT 1,430; interest 100; income before taxes 1,330; tax 266; net income 1,064; collections 34,100; cash 16,300; total 33,880. The key writes the depreciation of machine 1 as $(500 - 100)/8$, that is, 8 half-years, the same 4-year life deduced above.

> [!warning] Discrepancy with the official solution (the 300 deferred to July 2016)
> The key shows accounts receivable of 4,180, which includes the 300 due in July 2016, so it counts them as a current asset (current assets 20,480; non-current assets 13,400). Here they are a non-current receivable, because they fall due more than one year after 30/06/2015 (Slide 15), so receivables are 3,880 + 300 (current assets 20,180; non-current assets 13,700). Total assets, liabilities and equity are the same in both.

> [!warning] Erratum in the official solution
> The key's payments column adds to 16,800, but its items add to $450 + 3{,}000 + 1{,}200 + 4{,}800 + 350 + 8{,}000 = 17{,}800$, which gives the cash of 16,300 that it does show. The capital increase in the equity block reads 1,000 instead of 10,000 (only 10,000 gives equity of 16,114), and the labels of the interest payable (100) and the tax payable (266) are swapped.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
