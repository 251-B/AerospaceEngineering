---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Additional_EXERCISES.pdf, Exercise 4, pp. 5-6"
dificultad: high
tags:
  - exam-problem
  - solved
  - balance-sheet
  - income-statement
  - trade-credit
  - cemed
---

# ✏️ Problem: T3 Additional Exercise 4 — CEMED, statements 2016 and supplier discount

## 📄 Statement

CERÁMICAS DEL MEDITERRÁNEO (CEMED) manufactures and distributes ceramic tiles for construction in Valencia.

- CEMED was created on 1/01/2016 by three partners, each contributing 7 m.u., fully in cash.
- On 1/02/2016 it bought a piece of land worth 10 m.u., paying 50% in cash and leaving 50% to be paid one year later. On the same date it bought the factory building, paying 6 m.u. in cash and financing this amount with a mortgage at 5% annual interest for ten years. The factory is amortised over 20 years, linearly, with zero residual value. Each 31 December the company returns 10% of the mortgage principal plus the interest accrued in the year.
- On 1/04/2016 it obtained an additional bank loan of 5 m.u. at 6% annual interest, returning 20% of the principal each semester for the next 2½ years (first repayment on 1/10/2016, second on 1/04/2017, and so on). Interest is paid semiannually, calculated on the amount actually due in that semester, the day after the end of the semester.
- With this loan, on the same date, it bought machinery for 3 m.u. with 60 days payment delay; useful life 10 years, straight-line, zero residual value.
- On 1/07/2016 it acquired 150 tons of raw material at 0.03 m.u./ton. Half of it was used in producing the products sold. 60% of the total cost is paid to the supplier at 90 days; the other 40% remains unpaid at the end of the year.
- Sales revenue: 50 m.u., of which only 70% had been collected at 31/12/2016.
- Personnel plus Social Security: 0.8 m.u., paid in full in 2016.
- Corporation tax: 30%, settled by calendar year and paid on 15/01/2017.
- The company keeps 40% of annual net profits as reserves; the dividends are paid on 31/12/2016.

**Required:** (1) the income statement and the balance sheet at 24:00 on 31/12/2016, explaining the intermediate calculations; (2) the changes in the income statement and the balance sheet if the company had negotiated a 5% discount on the total price of the raw materials in exchange for paying in cash the 60% agreed at 90 days. In which case is the profit higher, and why?

## Phase 1 — Setup: data, timeline and hypotheses

| Date | Event | Cash |
| :--- | :--- | ---: |
| 1/01 | Capital $3 \times 7 = 21$ | +21 |
| 1/02 | Land 10: 50% paid, 50% due 1/02/2017 | −5 |
| 1/02 | Building 6, financed by a mortgage of 6 | +6 −6 |
| 1/04 | Bank loan 5 at 6% | +5 |
| 1/04 | Machinery 3 bought, paid 60 days later (31/05) | −3 (on 31/05) |
| 1/07 | Raw material $150 \times 0.03 = 4.5$ | — |
| 29/09 | 60% of the raw material paid (90 days) | −2.7 |
| 1/10 | Loan: first instalment (20% of 5) and interest of the first semester | −1 −0.15 |
| 31/12 | Mortgage: 10% of principal and interest of the year | −0.6 −0.275 |
| 31/12 | Dividends (60% of net income) | −19.3053 |
| 15/01/2017 | Tax paid (after the closing) | — |

**Hypotheses:**
1. The building is used from 1/02 (11 months) and the machinery from 1/04 (9 months). Land is not depreciated.
2. The mortgage interest of 2016 runs from 1/02 to 31/12 (11 months) on the 6 m.u. outstanding.
3. Loan semesters: 1/04-30/09 (principal 5) and 1/10-31/03 (principal 4). The interest of the second semester is paid on 1/04/2017, so the part from 1/10 to 31/12 is an **accrued, unpaid** expense of 2016.
4. Results to four decimals; exact fractions were used and the last digit is rounded.

## Phase 2 — Frames: classification of every operation

| Operation | Income statement 2016 | Cash 2016 | Open at 31/12/2016 |
| :--- | :--- | :--- | :--- |
| Capital | — | +21 | Capital 21 |
| Land | — | −5 | Land 10; land payable 5 (current) |
| Building / mortgage | Depreciation 0.275; interest 0.275 | +6 −6 −0.6 −0.275 | Building $6 - 0.275$; mortgage 5.4 (0.6 current, 4.8 long-term) |
| Bank loan | Interest $0.15 + 0.06$ | +5 −1 −0.15 | Loan 4 (2 current, 2 long-term); interest payable 0.06 |
| Machinery | Depreciation 0.225 | −3 | Machinery $3 - 0.225$ |
| Raw material | COGS 2.25 | −2.7 | Inventory 2.25; suppliers 1.8 |
| Sales | Revenue 50 | +35 | Receivables 15 |
| Personnel + SS | 0.8 | −0.8 | — |
| Tax | 13.7895 | 0 | Taxes payable 13.7895 |
| Dividends | — (distribution) | −19.3053 | Reserves 12.8702 |

## Phase 3 — Derivation (requirement 1)

### Step 1. Depreciation

$$D_{\text{building}} = \frac{6 - 0}{20} \times \frac{11}{12} = 0.3 \times 0.9167 = 0.2750 \text{ m.u.}$$

$$D_{\text{machinery}} = \frac{3 - 0}{10} \times \frac{9}{12} = 0.3 \times 0.75 = 0.2250 \text{ m.u.}$$

Total depreciation: $0.275 + 0.225 = 0.5$ m.u.

### Step 2. Mortgage

Interest of 2016 (1/02 to 31/12, principal 6):

$$I_{\text{mortgage}} = 6 \times 0.05 \times \frac{11}{12} = 0.2750 \text{ m.u.} \quad \text{(paid on 31/12)}$$

Principal returned on 31/12: $0.10 \times 6 = 0.6$; outstanding $6 - 0.6 = 5.4$. The next 0.6, due 31/12/2017, is current; the remaining $5.4 - 0.6 = 4.8$ is long-term.

### Step 3. Bank loan

Each instalment is $0.20 \times 5 = 1$ m.u. (five instalments: 1/10/2016, 1/04/2017, 1/10/2017, 1/04/2018, 1/10/2018).

- First semester (1/04-30/09, principal 5): $I_1 = 5 \times 0.06 \times \frac{6}{12} = 0.15$, paid on 1/10/2016 together with the first instalment.
- Second semester (1/10/2016-31/03/2017, principal 4): the 2016 part is October-December, $I_2 = 4 \times 0.06 \times \frac{3}{12} = 0.06$, **accrued but unpaid** (it will be paid on 1/04/2017).

Interest of the loan in 2016: $0.15 + 0.06 = 0.21$. Principal outstanding at 31/12: $5 - 1 = 4$, of which the instalments of 1/04/2017 and 1/10/2017 (2) are current and those of 2018 (2) are long-term.

### Step 4. Raw material, cost of goods sold and suppliers

$$\text{Purchase} = 150 \times 0.03 = 4.5 \text{ m.u.}, \qquad \text{COGS} = \frac{4.5}{2} = 2.25, \qquad \text{Inventory} = 2.25$$

Paid at 90 days: $0.60 \times 4.5 = 2.7$; unpaid: $0.40 \times 4.5 = 1.8$ (suppliers, current).

### Step 5. Sales

Collected $0.70 \times 50 = 35$; receivables $50 - 35 = 15$.

### Step 6. Income statement 2016

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | | 50.0000 |
| − Cost of goods sold | Step 4 | 2.2500 |
| **= Gross profit** | | **47.7500** |
| − Personnel and Social Security | | 0.8000 |
| − Depreciation | Step 1 | 0.5000 |
| **= Income from operations** | $47.75 - 1.3$ | **46.4500** |
| − Interest (mortgage 0.275; loan 0.21) | Steps 2-3 | 0.4850 |
| **= Income before taxes** | $46.45 - 0.485$ | **45.9650** |
| − Income taxes (30%) | $0.30 \times 45.965$ | 13.7895 |
| **= Net income** | $45.965 - 13.7895$ | **32.1755** |

Distribution: reserves $= 0.40 \times 32.1755 = 12.8702$; dividends $= 0.60 \times 32.1755 = 19.3053$, paid on 31/12.

### Step 7. Cash at 24:00 on 31/12/2016

| Inflows | m.u. | Outflows | m.u. |
| :--- | ---: | :--- | ---: |
| Capital | 21.0000 | Land (50%) | 5.0000 |
| Mortgage | 6.0000 | Building | 6.0000 |
| Bank loan | 5.0000 | Machinery | 3.0000 |
| Sales collected | 35.0000 | Raw material (60%) | 2.7000 |
| | | Personnel | 0.8000 |
| | | Mortgage principal + interest | 0.8750 |
| | | Loan instalment + interest | 1.1500 |
| | | Dividends | 19.3053 |
| **Total** | **67.0000** | **Total** | **38.8303** |

$$\text{Cash} = 67 - 38.8303 = 28.1697 \text{ m.u.}$$

### Step 8. Balance sheet at 24:00 on 31/12/2016

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Land | 10.0000 | Capital | 21.0000 |
| Building ($6 - 0.275$) | 5.7250 | Reserves (40% of net income) | 12.8702 |
| Machinery ($3 - 0.225$) | 2.7750 | **Equity** | **33.8702** |
| **Non-current assets** | **18.5000** | Mortgage, long-term part | 4.8000 |
| Inventory (raw material) | 2.2500 | Bank loan, long-term part | 2.0000 |
| Accounts receivable | 15.0000 | **Long-term liabilities** | **6.8000** |
| Cash | 28.1697 | Land payable (1/02/2017) | 5.0000 |
| **Current assets** | **45.4197** | Mortgage, current part | 0.6000 |
| | | Bank loan, current part | 2.0000 |
| | | Interest payable | 0.0600 |
| | | Suppliers | 1.8000 |
| | | Taxes payable (15/01/2017) | 13.7895 |
| | | **Current liabilities** | **23.2495** |
| **Total assets** | **63.9197** | **Total liabilities and equity** | **63.9197** |

## Phase 3b — Derivation (requirement 2: 5% discount, 60% paid in cash)

### Step 9. New purchase price and payments

$$\text{Price} = 4.5 \times (1 - 0.05) = 4.275 \text{ m.u.}$$

- Paid in cash on 1/07: $0.60 \times 4.275 = 2.565$ (instead of 2.7 at 90 days).
- Unpaid at 31/12: $0.40 \times 4.275 = 1.71$ (instead of 1.8).
- Consumed (half): $\text{COGS} = 4.275 / 2 = 2.1375$; inventory 2.1375 (both instead of 2.25).

### Step 10. New income statement

Only the cost of goods sold changes before taxes: $\Delta\text{COGS} = 2.1375 - 2.25 = -0.1125$.

| Line | Requirement 1 | Requirement 2 | Change |
| :--- | ---: | ---: | ---: |
| Cost of goods sold | 2.2500 | 2.1375 | −0.1125 |
| Income before taxes | 45.9650 | 46.0775 | +0.1125 |
| Income taxes (30%) | 13.7895 | 13.8233 | +0.0338 |
| **Net income** | **32.1755** | **32.2543** | **+0.0788** |
| Dividends (60%) | 19.3053 | 19.3526 | +0.0473 |
| Reserves (40%) | 12.8702 | 12.9017 | +0.0315 |

The net change is the after-tax saving: $0.1125 \times (1 - 0.30) = 0.07875$.

### Step 11. New balance sheet items

| Item | Change | Reason |
| :--- | ---: | :--- |
| Inventory | −0.1125 | Half of the material is still in stock, valued at the lower price |
| Cash | +0.0878 | Pays 2.565 instead of 2.7 (+0.135) but pays 0.0473 more dividends |
| Suppliers | −0.0900 | 40% of a lower price (1.71 instead of 1.8) |
| Taxes payable | +0.0338 | Higher profit |
| Reserves | +0.0315 | 40% of the higher net income |
| **Total assets** | **−0.0248** | $-0.1125 + 0.08775$ |
| **Total liabilities and equity** | **−0.0248** | $-0.09 + 0.03375 + 0.0315$ |

New totals: $63.9197 - 0.0248 = 63.8950$ on both sides (cash 28.2575).

## Phase 4 — Interpretation and checks

- **Balance:** $18.5 + 45.4197 = 63.9197 = 33.8702 + 6.8 + 23.2495$; requirement 2: both sides fall by 0.02475.
- **In which case is the profit higher?** With the **discount**. The discount lowers the cost of the material; the price paid for it is giving up 90 days of **trade credit** [Slide 35], and trade credit has no explicit interest in this problem, so losing it costs nothing in the income statement: it only advances a payment that in both cases falls inside 2016.
- **Why only half of the saving reaches the profit:** only half of the material was consumed. The other half of the saving is in the lower value of the inventory and will reach the income statement when that stock is used.
- **Debt structure** [Slide 36]: liabilities $6.8 + 23.2495 = 30.0495$, equity 33.8702, so $L/E = 0.89$.
- **Exam traps:** (1) the mortgage finances the building: cash +6 and −6 on the same day; (2) the loan interest of October-December is accrued but unpaid; (3) the current part of each loan is what is due before 31/12/2017; (4) the land is not depreciated; (5) taxes are payable on 15/01/2017, so they are a liability, while dividends were paid.
- No official numerical solution is included in `sources/`.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
