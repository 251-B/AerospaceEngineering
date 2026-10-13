---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Financial Statements_EXERCISES.pdf, Exercise 1, p. 1"
dificultad: easy
tags:
  - problem
  - solved
  - accrual
  - depreciation
---

# ✏️ Problem: Exercise 1 — Revenues vs collections, expenses vs payments, and depreciation

## 📄 Statement

A company started activity on 1 January of the present year. At 31 March it has the following goods, acquired on 31 December of the previous year:
- factory building 1,000 m.u., duration 25 years;
- office building 1,500 m.u., duration 50 years;
- machinery 300 m.u., duration 10 years;
- transport equipment 100 m.u., duration 5 years.

Information for the first quarter:
- personnel salaries of the quarter 450 m.u., of which 75 m.u. are pending to be paid after 31/3;
- materials purchased and used in production 700 m.u., of which 125 m.u. are pending to be paid after 31/3;
- energy consumption estimated at 230 m.u., nothing paid to date;
- sales invoiced to customers 1,930 m.u., of which 315 m.u. had not been collected at 31/3; the rest was collected in due time. In manufacturing all the units sold, all the purchased materials were consumed.

Ignore corporation taxes.

a) At 31/3, find the income, expenses, collections (cash inflows), payments (cash outflows), investments and depreciation of the quarter (linear depreciation along the lifetime of the goods).

b) How does the answer change if only half of the purchased materials had been consumed in manufacturing the units sold?

## Phase 1 — Setup: data and hypotheses

**Period:** first quarter (1/01 to 31/03), $\frac{3}{12} = \frac{1}{4}$ of a year. The fixed assets were bought on 31/12 of the previous year, so they are used during the **whole** quarter.

The exercise trains the distinction of [Slide 8]: a **revenue** is recorded when the sale is made, whether or not it is collected; an **expense** when the good or service is received or consumed, whether or not it is paid. Collections and payments are the cash side of the same operations.

## Phase 2 — Frames: classification of every operation

| Operation | Revenue / expense of Q1 | Collection / payment in Q1 | Pending at 31/3 |
| :--- | :--- | :--- | :--- |
| Sales | Revenue 1,930 | Collection $1{,}930 - 315 = 1{,}615$ | Receivable 315 |
| Salaries | Expense 450 | Payment $450 - 75 = 375$ | Salaries payable 75 |
| Materials (all consumed) | Expense 700 | Payment $700 - 125 = 575$ | Supplier payable 125 |
| Energy | Expense 230 | Payment 0 | Energy payable 230 |
| Fixed assets | Depreciation 30 | 0 | Net value $2{,}900 - 30$ |

## Phase 3 — Derivation

### Step 1. Depreciation of the quarter

For each asset, with no residual value given:

$$D_{\text{quarter}} = \frac{\text{Cost}}{\text{Years of life}} \times \frac{3}{12}$$

| Asset | Annual depreciation | Quarter |
| :--- | :--- | ---: |
| Factory building | $1{,}000 / 25 = 40$ | $40 / 4 = 10.0$ |
| Office building | $1{,}500 / 50 = 30$ | $30 / 4 = 7.5$ |
| Machinery | $300 / 10 = 30$ | $30 / 4 = 7.5$ |
| Transport equipment | $100 / 5 = 20$ | $20 / 4 = 5.0$ |
| **Total** | **120** | **30.0** |

### Step 2. Part (a)

- **Income (revenues):** the sales invoiced, **1,930 m.u.**
- **Expenses:** $450 + 700 + 230 + 30 = $ **1,410 m.u.** (so the profit of the quarter is $1{,}930 - 1{,}410 = 520$ m.u.).
- **Collections:** $1{,}930 - 315 = $ **1,615 m.u.**
- **Payments:** $(450 - 75) + (700 - 125) + 0 = 375 + 575 = $ **950 m.u.** Depreciation is not a payment.
- **Investments of the quarter:** **0 m.u.** The fixed assets (total $1{,}000 + 1{,}500 + 300 + 100 = 2{,}900$ m.u.) were acquired on 31/12 of the previous year, before the quarter began. If the question is read as "the investment the company works with", the answer is that 2,900 m.u.; state the reading you use in the exam.
- **Depreciation:** **30 m.u.**

### Step 3. Part (b): only half of the materials consumed

Only the material **consumed** is an expense [Slide 8, Slide 10]: $700 / 2 = 350$ m.u. The other 350 m.u. stay in the warehouse as **inventory**, a current asset [Slide 14].

| Magnitude | (a) | (b) | Change |
| :--- | ---: | ---: | ---: |
| Income | 1,930 | 1,930 | 0 |
| Expenses | 1,410 | $450 + 350 + 230 + 30 = 1{,}060$ | −350 |
| Profit | 520 | 870 | +350 |
| Collections | 1,615 | 1,615 | 0 |
| Payments | 950 | 950 | 0 |
| Inventory at 31/3 | 0 | 350 | +350 |
| Depreciation | 30 | 30 | 0 |

Payments do not change: the company **paid** for what it **bought** (575 of the 700), regardless of how much it **used**.

## Phase 4 — Interpretation and checks

- **Profit is not cash:** in (a) the profit is 520 while the net cash generated is $1{,}615 - 950 = 665$. The difference, $665 - 520 = 145$, is explained item by item: $+30$ (depreciation, an expense without payment) $+75 + 125 + 230$ (expenses not yet paid) $- 315$ (revenue not yet collected) $= 145$.
- **Part (b)** raises the profit by 350 without any extra cash: unconsumed material is an asset, not an expense.
- **Check of depreciation:** the annual total 120 times $\frac{1}{4}$ gives 30.

## Check against the official key

> [!info] Official solution, `T3_Financial Statements_SOLUTIONS.pdf`, pp. 1-2
> Part (a) coincides with the key: income 1,930; collections 1,615; payments 950; expenses 1,410; depreciation 30; investments 0. In part (b) the key also states that revenue, collections and payments do not change and that the unused material appears as inventory.

> [!warning] Erratum in the official solution (part b)
> The key gives total expenses of 1,124 for part (b), but its own items add to $450 + 350 + 230 + 30 = 1{,}060$. That is the value obtained above, and the only one consistent with a profit that rises by exactly the 350 of material that was not consumed.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
