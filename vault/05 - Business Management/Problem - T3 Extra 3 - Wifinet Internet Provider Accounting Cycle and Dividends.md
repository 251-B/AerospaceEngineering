---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Additional_EXERCISES.pdf, Exercise 3, p. 4"
dificultad: high
tags:
  - exam-problem
  - solved
  - balance-sheet
  - income-statement
  - dividends
  - wifinet
---

# ✏️ Problem: T3 Additional Exercise 3 — WIFINET S.L., statements 2017 and dividend options

## 📄 Statement

Wifinet S.L. was incorporated on 1/01/2016 with a registered capital of 6,003 m.u., to provide wireless Internet on the Alicante coast.

**Fiscal year 2016.** It took a bank loan of 2,000 m.u. at 5% annual interest (payable at the end of each year), the principal being repayable in 2019. It invested 5,371 m.u. in technical equipment with a life of 20 years; at the end of 2016 it recorded an accumulated depreciation of 26 m.u. for those assets. It also invested 206 m.u. in licence fees by 31/12/2016, to use certain technologies for 5 years. It spent 636 m.u. on financial shares of other companies. Most of 2016 was devoted to building the network and business started only in the last two months. At the end of 2016 the balance sheet reflected a **loss of 340 m.u.** and **cash in hand and bank of 1,476 m.u.**

In 2017 the results were positive, but the company decided not to distribute dividends and to retain all its profits to reduce the loss of the previous year.

**Fiscal year 2017.**
- Internet and VOIP: 5,000 customers on average, with an average revenue of 0.032 m.u./month per client in subscription fees. Additionally, 46 m.u. of on-line sales of other products. At the end of 2017 customers owed 164 m.u.
- Stocks were exhausted at the end of 2016. Purchases of materials to be installed in customers' homes: 680 m.u., of which 560 m.u. paid immediately and the rest deferred to the following year. The 2017 sales consumed half of the purchased goods.
- Staff costs: 559 m.u., paid in full in 2017. Supplies and outside services: 312 m.u., paid.
- Other administrative expenses: 300 m.u., 60% of them deferred to the following year.
- Corporation tax: 30%, payable in the first quarter of 2018.

**Required:** (1) the income statement for 2017; (2) the balance sheet at 31/12/2017; (3) which balance-sheet items change, and by how much, if a dividend of 20% of net profit is paid at 24:00 on 31/12/2017; (4) the same if the dividend of 20% is decided before the end of 2017 and paid on 30/06/2018.

## Phase 1 — Setup: data, timeline and hypotheses

**Period:** calendar year 2017. **Closing:** 31/12/2017. The 2016 data serve only to build the **opening balance** of 2017.

**Hypotheses:**
1. The licences were bought at the very end of 2016, so they start to be amortised in 2017 (no 2016 amortisation is given).
2. The equipment was depreciated only 26 m.u. in 2016 (part of the year); in 2017 it is used the whole year.
3. Interest is paid at the end of each year, so no interest payable remains; the loan is due in 2019, more than one year after 31/12/2017: **long-term** [Slide 16].
4. The financial shares are a long-term investment (non-current asset) [Slide 15]; they produce no revenue in the data.

## Phase 2 — Frames: opening balance and classification of every operation

### Opening balance at 31/12/2016 (rebuilt from the data)

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Technical equipment ($5{,}371 - 26$) | 5,345 | Capital | 6,003 |
| Licences | 206 | Loss of 2016 | (340) |
| Financial shares | 636 | **Equity** | **5,663** |
| Cash | 1,476 | Bank loan (due 2019) | 2,000 |
| **Total** | **7,663** | **Total** | **7,663** |

It balances ($7{,}663 = 5{,}663 + 2{,}000$), which confirms that no other 2016 item is missing.

### Operations of 2017

| Operation | Income statement 2017 | Cash 2017 | Open at 31/12/2017 |
| :--- | :--- | :--- | :--- |
| Subscriptions + on-line sales | Revenue 1,966 | +1,802 | Receivables 164 |
| Purchases of materials (680) | COGS 340 | −560 | Inventory 340; suppliers 120 |
| Staff | 559 | −559 | — |
| Supplies and outside services | 312 | −312 | — |
| Administrative expenses | 300 | −120 | Other creditors 180 |
| Equipment depreciation | 268.55 | 0 | Accumulated depreciation 294.55 |
| Licence amortisation | 41.20 | 0 | Licences 164.80 |
| Interest | 100 | −100 | — |
| Tax | 13.575 | 0 | Taxes payable 13.575 |

## Phase 3 — Derivation

### Step 1. Revenues and receivables

$$\text{Subscriptions} = 5{,}000 \text{ clients} \times 0.032 \tfrac{\text{m.u.}}{\text{client} \cdot \text{month}} \times 12 \text{ months} = 1{,}920 \text{ m.u.}$$

$$\text{Revenues} = 1{,}920 + 46 = 1{,}966 \text{ m.u.}, \qquad \text{Collected} = 1{,}966 - 164 = 1{,}802 \text{ m.u.}$$

### Step 2. Purchases, consumption and inventory

Opening stock 0 ("stocks were exhausted at the end of 2016"); purchases 680; half consumed:

$$\text{COGS} = 0 + 680 - 340 = 340 \text{ m.u.}, \qquad \text{Ending inventory} = 340 \text{ m.u.}$$

Payment: 560 paid; $680 - 560 = 120$ owed to suppliers.

### Step 3. Operating expenses

- Staff 559 and supplies and outside services 312, all paid.
- Administrative expenses 300: 60% deferred, $0.60 \times 300 = 180$ owed; $300 - 180 = 120$ paid.

### Step 4. Depreciation and amortisation

$$D_{\text{equipment}} = \frac{5{,}371}{20} = 268.55 \text{ m.u.}, \qquad A_{\text{licences}} = \frac{206}{5} = 41.20 \text{ m.u.}$$

Accumulated depreciation of the equipment: $26 + 268.55 = 294.55$; net value $5{,}371 - 294.55 = 5{,}076.45$. Licences: $206 - 41.20 = 164.80$.

### Step 5. Interest

$$I = 2{,}000 \times 0.05 = 100 \text{ m.u.} \quad \text{(paid at the end of 2017)}$$

### Step 6. Income statement 2017 (requirement 1)

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Revenues | $1{,}920 + 46$ | 1,966.000 |
| − Cost of goods sold (materials consumed) | | 340.000 |
| **= Gross profit** | | **1,626.000** |
| − Staff | | 559.000 |
| − Supplies and outside services | | 312.000 |
| − Administrative expenses | | 300.000 |
| − Depreciation and amortisation | $268.55 + 41.20$ | 309.750 |
| **= Income from operations** | $1{,}626 - 1{,}480.75$ | **145.250** |
| − Interest expense | | 100.000 |
| **= Income before taxes** | $145.25 - 100$ | **45.250** |
| − Income taxes (30%) | $0.30 \times 45.25$ | 13.575 |
| **= Net income** | $45.25 - 13.575$ | **31.675** |

### Step 7. Cash at 31/12/2017

$$\text{Cash} = 1{,}476 + 1{,}802 - 560 - 559 - 312 - 120 - 100 = 1{,}627 \text{ m.u.}$$

### Step 8. Balance sheet at 31/12/2017 (requirement 2)

All the profit is retained, so it stays in equity and reduces the accumulated loss: $-340 + 31.675 = -308.325$.

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Technical equipment | 5,371.000 | Capital | 6,003.000 |
| − Accumulated depreciation | (294.550) | Loss of 2016 | (340.000) |
| Licences (net) | 164.800 | Net income 2017 | 31.675 |
| Financial shares | 636.000 | **Equity** | **5,694.675** |
| **Non-current assets** | **5,877.250** | Bank loan (due 2019) | 2,000.000 |
| Inventory | 340.000 | **Long-term liabilities** | **2,000.000** |
| Accounts receivable | 164.000 | Suppliers | 120.000 |
| Cash | 1,627.000 | Other creditors (administration) | 180.000 |
| **Current assets** | **2,131.000** | Taxes payable (Q1 2018) | 13.575 |
| | | **Current liabilities** | **313.575** |
| **Total assets** | **8,008.250** | **Total liabilities and equity** | **8,008.250** |

### Step 9. Dividend paid at 24:00 on 31/12/2017 (requirement 3)

$$\text{Dividend} = 0.20 \times 31.675 = 6.335 \text{ m.u.}$$

Paying it at 24:00 means cash leaves the company and the profit kept in equity falls by the same amount:

| Item | Before | Change | After |
| :--- | ---: | ---: | ---: |
| Cash | 1,627.000 | −6.335 | 1,620.665 |
| Equity (net income retained) | 5,694.675 | −6.335 | 5,688.340 |
| Total assets = total liabilities and equity | 8,008.250 | −6.335 | 8,001.915 |

### Step 10. Dividend decided in 2017, paid on 30/06/2018 (requirement 4)

The dividend is already owed to the shareholders at 31/12/2017 but no cash has left: equity falls and a **current liability** (dividends payable, due within the year) appears.

| Item | Before | Change | After |
| :--- | ---: | ---: | ---: |
| Equity | 5,694.675 | −6.335 | 5,688.340 |
| Dividends payable (current liability) | 0 | +6.335 | 6.335 |
| Current liabilities | 313.575 | +6.335 | 319.910 |
| Cash and total assets | unchanged | 0 | 8,008.250 |

## Phase 4 — Interpretation and checks

- **Balance:** $5{,}877.25 + 2{,}131 = 8{,}008.25 = 5{,}694.675 + 2{,}000 + 313.575$; requirement 3: $8{,}001.915 = 5{,}688.340 + 2{,}313.575$; requirement 4: $8{,}008.25 = 5{,}688.34 + 2{,}000 + 319.91$.
- **Requirement 3 vs 4:** both reduce equity by the same 6.335; the difference is only on the other side: in 3 an **asset** (cash) falls, in 4 a **liability** rises. A dividend is never an expense, so net income is 31.675 in all three cases.
- **Why the company chose not to pay:** after 2017 the equity is still below the capital (accumulated loss $-308.325$); retaining the profit is self-financing [Slide 23] that rebuilds the equity.
- **Exam traps:** (1) the 2016 data are only the opening balance; (2) inventory is half of the purchases; (3) the licences bought at the end of 2016 are amortised from 2017; (4) the loan due in 2019 is long-term.

## Check against the official key

> [!info] Official solution, `T3_Additional_SOLUTIONS.pdf`, pp. 16-18
> Requirements 1 and 2 coincide with the key: revenues 1,966; cost of goods sold 340; operating expenses 1,511; EBITDA 455; depreciation and amortisation 309.75; EBIT 145.25; interest 100; income before taxes 45.25; tax 13.575; net income 31.675; cash 1,627; total assets 8,008.25; equity 5,694.675. The key rounds to one decimal (309.8; 145.3; 45.3; 13.6; 31.7), which only shifts the last digit.
>
> The key does not answer requirements 3 and 4 (20 % dividend): it only shows "Dividends (@0%)", so Steps 9 and 10 above are not covered by it.

> [!warning] Erratum in the official solution
> The key gives total liabilities of 2,325.935, but its own items add to $120 + 180 + 13.575 + 2{,}000 = 2{,}313.575$ (2,313.6 rounded), which together with equity of 5,694.7 gives the total of 8,008.3 that it does show. The accumulated depreciation mentions "2009"; the 26 m.u. belong to 2016.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
