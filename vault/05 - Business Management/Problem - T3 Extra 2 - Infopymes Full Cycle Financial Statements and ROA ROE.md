---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Additional_EXERCISES.pdf, Exercise 2, p. 3"
dificultad: high
tags:
  - exam-problem
  - solved
  - balance-sheet
  - income-statement
  - infopymes
---

# ✏️ Problem: T3 Additional Exercise 2 — INFOPYMES, statements 2016-2017 and ROA/ROE

## 📄 Statement

Three entrepreneurs established INFOPYMES on 1/01/2016 to provide on-line information services for small and medium enterprises, start-ups and potential entrepreneurs.

- The computer equipment, worth 100,000 €, was acquired on 1/01/2016 and will be paid to suppliers after three months, on 1/04/2016. Useful life 5 years (until 31/12/2020), linear depreciation, no residual value.
- On-line consultations brought revenues of 300,000 € in 2016.
- Rented premises: 1,000 €/month from 1/01/2016. Salaries and Social Security of the permanent employees: 5,000 €/month. Electricity, phone, etc.: 500 €/month.
- Variable wages of the additional staff for the on-line consultations: 174,000 € in 2016.
- The partners contributed an initial capital of 100,000 €. A bank granted a loan of 100,000 € at 10% yearly interest for 5 years (1/01/2016 to 31/12/2020). Each 31 December the company returns 20,000 € and pays the interest (10%) on the loan value at the beginning of each year.
- Results are declared at 23:59 on 31 December (after all payments and receipts, including interest, wages, Social Security, etc.), and the corporation tax of 30% on the profits is paid immediately. Dividends of 40% of the profits after taxes are distributed, and the final balance is drawn at 24:00.

**Required:** (1) the income statement for 2016; (2) assuming the tax has been paid and the dividends distributed, the balance sheet at 24:00 on 31/12/2016; (3) the balance sheet at 24:00 on 31/12/2017, assuming no new investments in 2017 and that the retained earnings and the cash balance at the end of 2017 remained unchanged with respect to 2016; (4) the ROA and ROE ratios in 2017.

## Phase 1 — Setup: data, timeline and hypotheses

| Item | Value |
| :--- | :--- |
| Capital | 100,000 € (1/01/2016) |
| Loan | 100,000 € at 10%; 20,000 € returned each 31/12; interest on the balance at the start of each year |
| Equipment | 100,000 €, bought 1/01/2016, paid 1/04/2016, 5 years, no residual value |
| Revenues 2016 | 300,000 € |
| Fixed monthly costs | Rent 1,000; permanent staff 5,000; utilities 500 (€/month) |
| Variable wages 2016 | 174,000 € |
| Tax | 30% of profits, paid at 23:59 on 31/12 |
| Dividends | 40% of profit after taxes, paid at 23:59 on 31/12 |

**Hypotheses:**
1. The statement says the results are declared "after having made all payments and receipts", so the 300,000 € of revenues are **collected** and all 2016 costs are **paid** within 2016.
2. The balance is drawn at 24:00, **after** paying tax, interest, the 20,000 € instalment and dividends: none of them remains as a liability.
3. For 2017 the statement gives no operating data; we assume the **same revenues and operating costs as in 2016**, which is the only reading that lets requirement 4 be computed. With retained earnings unchanged, the whole 2017 profit must have been paid out as dividends (shown in Phase 3).

## Phase 2 — Frames: classification of every operation (2016)

| Operation | Income statement 2016 | Cash 2016 | Open at 24:00 on 31/12/2016 |
| :--- | :--- | :--- | :--- |
| Capital | — | +100,000 | Capital 100,000 |
| Loan | — | +100,000 | Loan 80,000 (after the instalment) |
| Equipment | Depreciation 20,000 | −100,000 (on 1/04) | Equipment 100,000 − 20,000 |
| Revenues | 300,000 | +300,000 | — |
| Rent, staff, utilities, variable wages | 252,000 | −252,000 | — |
| Interest | 10,000 | −10,000 | — |
| Instalment | — | −20,000 | (reduces the loan) |
| Tax | 5,400 | −5,400 | — |
| Dividends | — (distribution) | −5,040 | Retained earnings 7,560 |

The equipment is bought on credit on 1/01 and paid on 1/04: between those dates it is a debt to the supplier, but at 31/12 that debt no longer exists.

## Phase 3 — Derivation

### Step 1. Depreciation and interest 2016

$$D = \frac{100{,}000 - 0}{5} \times \frac{12}{12} = 20{,}000 \text{ €/year}$$

$$I_{2016} = 100{,}000 \times 0.10 = 10{,}000 \text{ €} \quad \text{(loan value at the beginning of 2016)}$$

### Step 2. Income statement 2016 (requirement 1)

| Line | Computation | € |
| :--- | :--- | ---: |
| Revenues (on-line consultations) | | 300,000 |
| − Rent | $12 \times 1{,}000$ | 12,000 |
| − Permanent staff and Social Security | $12 \times 5{,}000$ | 60,000 |
| − Electricity, phone, etc. | $12 \times 500$ | 6,000 |
| − Variable wages | | 174,000 |
| − Depreciation | Step 1 | 20,000 |
| **= Income from operations** | $300{,}000 - 272{,}000$ | **28,000** |
| − Interest expense | Step 1 | 10,000 |
| **= Income before taxes** | $28{,}000 - 10{,}000$ | **18,000** |
| − Income taxes (30%) | $0.30 \times 18{,}000$ | 5,400 |
| **= Net income** | $18{,}000 - 5{,}400$ | **12,600** |

Distribution [Slide 23]: dividends $= 0.40 \times 12{,}600 = 5{,}040$ €; retained earnings (self-financing) $= 12{,}600 - 5{,}040 = 7{,}560$ €.

### Step 3. Cash at 24:00 on 31/12/2016

| Inflows | € | Outflows | € |
| :--- | ---: | :--- | ---: |
| Capital | 100,000 | Equipment (1/04) | 100,000 |
| Loan | 100,000 | Rent + staff + utilities | 78,000 |
| Revenues collected | 300,000 | Variable wages | 174,000 |
| | | Interest | 10,000 |
| | | Loan instalment | 20,000 |
| | | Tax | 5,400 |
| | | Dividends | 5,040 |
| **Total** | **500,000** | **Total** | **392,440** |

$$\text{Cash}_{2016} = 500{,}000 - 392{,}440 = 107{,}560 \text{ €}$$

### Step 4. Balance sheet at 24:00 on 31/12/2016 (requirement 2)

The loan after the first instalment is $100{,}000 - 20{,}000 = 80{,}000$ €. The instalment due on 31/12/2017 (20,000 €) is within one year, so it is a **current liability**; the other 60,000 € are long-term [Slide 16].

| Assets | € | Liabilities and equity | € |
| :--- | ---: | :--- | ---: |
| Equipment | 100,000 | Capital | 100,000 |
| − Accumulated depreciation | (20,000) | Retained earnings | 7,560 |
| **Non-current assets** | **80,000** | **Equity** | **107,560** |
| Cash | 107,560 | Long-term bank loan | 60,000 |
| **Current assets** | **107,560** | Short-term bank loan (due 31/12/2017) | 20,000 |
| **Total assets** | **187,560** | **Total liabilities and equity** | **187,560** |

### Step 5. Balance sheet at 24:00 on 31/12/2017 (requirement 3)

Item by item:
- **Equipment:** no new investment; two years of depreciation, $2 \times 20{,}000 = 40{,}000$; net value $100{,}000 - 40{,}000 = 60{,}000$ €.
- **Loan:** second instalment paid, $80{,}000 - 20{,}000 = 60{,}000$ €: 20,000 € current (due 31/12/2018) and 40,000 € long-term.
- **Cash and retained earnings:** unchanged by statement: 107,560 € and 7,560 €.
- **Capital:** unchanged, 100,000 €.

| Assets | € | Liabilities and equity | € |
| :--- | ---: | :--- | ---: |
| Equipment | 100,000 | Capital | 100,000 |
| − Accumulated depreciation | (40,000) | Retained earnings | 7,560 |
| **Non-current assets** | **60,000** | **Equity** | **107,560** |
| Cash | 107,560 | Long-term bank loan | 40,000 |
| **Current assets** | **107,560** | Short-term bank loan (due 31/12/2018) | 20,000 |
| **Total assets** | **167,560** | **Total liabilities and equity** | **167,560** |

**Is the statement consistent?** With the 2016 operations repeated (hypothesis 3), 2017 gives:

$$I_{2017} = 80{,}000 \times 0.10 = 8{,}000, \quad \text{IBT} = 28{,}000 - 8{,}000 = 20{,}000, \quad T = 0.30 \times 20{,}000 = 6{,}000, \quad \text{NI} = 14{,}000$$

Retained earnings unchanged means dividends $= 14{,}000$ € (a 100% pay-out). Cash then moves by $+300{,}000 - 252{,}000 - 8{,}000 - 20{,}000 - 6{,}000 - 14{,}000 = 0$, so the cash is indeed unchanged: the two conditions of the statement are compatible.

### Step 6. ROA and ROE in 2017 (requirement 4)

> [!warning] Definitions not in the Topic 3 slides
> The Topic 3 deck in `sources/` does not define ROA and ROE, but the problem asks for them. The standard definitions used here are $\text{ROA} = \dfrac{\text{Income from operations}}{\text{Total assets}}$ (the return of the economic structure) and $\text{ROE} = \dfrac{\text{Net income}}{\text{Equity}}$ (the return to the owners). Check them against your class notes: if your lecturer defines ROA with net income instead, the value is $14{,}000 / 167{,}560 = 8.36\%$.

$$\text{ROA}_{2017} = \frac{28{,}000}{167{,}560} = 0.1671 = 16.71\%$$

$$\text{ROE}_{2017} = \frac{14{,}000}{107{,}560} = 0.1302 = 13.02\%$$

## Phase 4 — Interpretation and checks

- **Balances:** $80{,}000 + 107{,}560 = 187{,}560 = 107{,}560 + 60{,}000 + 20{,}000$ (2016) and $60{,}000 + 107{,}560 = 167{,}560 = 107{,}560 + 40{,}000 + 20{,}000$ (2017).
- **What changes between the two years:** both sides shrink by 20,000 €: the asset loses 20,000 € of value through depreciation, and the loan falls by the 20,000 € instalment, which in cash terms was financed by the cash generated (depreciation is an expense that is not a payment).
- **Leverage** [Slide 36]: $L/E = 80{,}000/107{,}560 = 0.74$ in 2016 and $60{,}000/107{,}560 = 0.56$ in 2017; the company becomes less indebted each year.
- **ROE < ROA here:** the return to the owners is lower than the return of the assets because interest and taxes are deducted from the numerator; the equity base being smaller than total assets is not enough to compensate.
- **Exam traps:** (1) the loan instalment is a payment, never an expense; (2) at 24:00 no tax or dividend liability remains; (3) the current part of the loan (next instalment) must be separated from the long-term part.
- No official numerical solution is included in `sources/`.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
