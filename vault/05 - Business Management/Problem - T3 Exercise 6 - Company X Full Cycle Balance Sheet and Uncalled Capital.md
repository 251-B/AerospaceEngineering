---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Financial Statements_EXERCISES.pdf, Exercise 6, p. 3"
dificultad: medium
tags:
  - problem
  - solved
  - balance-sheet
  - income-statement
---

# ✏️ Problem: Exercise 6 — Company X, first-year balance sheet and partly paid capital

## 📄 Statement

Company X was incorporated on 1/01/2017 with a subscription of shares worth 100 m.u., fully paid in cash. On 1/01/2017 it bought, with cash: a) an area (land) for 20 m.u.; b) equipment with a life of 10 years (straight-line depreciation) and a purchase price of 20 m.u.; c) raw materials for 20 m.u.

The company hires an employee for a total annual cost (salaries, Social Security, etc.) of 10 m.u. per year. This employee processes half of the raw material and sells it for a total of 50 m.u. Sales are the same every day of the year. The average collection period is 3 months.

The single tax rate on the profits of the company is 30% (paid on 31/12/2017). The company follows a strict self-financing strategy.

1. Prepare the balance sheet at 31/12/2017, justifying and explaining the intermediate calculations.
2. Explain how the accounting statements would change if, instead of 100%, the shareholders had paid only 90% of the 100 m.u. subscribed.

## Phase 1 — Setup: data and hypotheses

**Period:** calendar year 2017. **Closing:** 31/12/2017.

**Hypotheses:**
1. The employee's cost is paid during the year.
2. Land has no useful life given and is not depreciated; the equipment has no residual value given (zero).
3. **Strict self-financing** [Slide 23]: the whole net income is retained (pay-out 0%).
4. The tax is paid on 31/12, so no tax liability remains.

## Phase 2 — Frames: classification of every operation

| Operation | Income statement 2017 | Cash 2017 | Open at 31/12/2017 |
| :--- | :--- | :--- | :--- |
| Capital | — | +100 | Share capital 100 |
| Land | — | −20 | Land 20 |
| Equipment | Depreciation 2 | −20 | Equipment $20 - 2$ |
| Raw materials | COGS 10 (half consumed) | −20 | Inventory 10 |
| Employee | Personnel 10 | −10 | — |
| Sales | Revenue 50 | +37.5 | Receivables 12.5 |
| Tax | 8.4 | −8.4 | — |

## Phase 3 — Derivation (requirement 1)

### Step 1. Depreciation and cost of goods sold

$$D = \frac{20 - 0}{10} = 2 \text{ m.u.}, \qquad \text{COGS} = \frac{20}{2} = 10 \text{ m.u.}, \qquad \text{Inventory} = 20 - 10 = 10 \text{ m.u.}$$

### Step 2. Receivables from the collection period

Sales are spread evenly over the year and customers pay 3 months after buying. At 31/12 the sales of the last 3 months are still unpaid:

$$\text{Receivables} = 50 \times \frac{3}{12} = 12.5 \text{ m.u.}, \qquad \text{Collected} = 50 - 12.5 = 37.5 \text{ m.u.}$$

### Step 3. Income statement 2017

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | | 50.0 |
| − Cost of goods sold | Step 1 | 10.0 |
| **= Gross profit** | | **40.0** |
| − Personnel | | 10.0 |
| − Depreciation | Step 1 | 2.0 |
| **= Income from operations = income before taxes** | no interest | **28.0** |
| − Income taxes (30%) | $0.30 \times 28$ | 8.4 |
| **= Net income** | $28 - 8.4$ | **19.6** |

All 19.6 is retained (strict self-financing).

### Step 4. Cash at 31/12/2017

$$\text{Cash} = 100 - 20 - 20 - 20 + 37.5 - 10 - 8.4 = 59.1 \text{ m.u.}$$

### Step 5. Balance sheet at 31/12/2017

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Land | 20.0 | Share capital | 100.0 |
| Equipment ($20 - 2$) | 18.0 | Retained earnings (net income 2017) | 19.6 |
| **Non-current assets** | **38.0** | **Equity** | **119.6** |
| Inventory (raw materials) | 10.0 | **Liabilities** | **0** |
| Accounts receivable | 12.5 | | |
| Cash | 59.1 | | |
| **Current assets** | **81.6** | | |
| **Total assets** | **119.6** | **Total liabilities and equity** | **119.6** |

## Phase 3b — Derivation (requirement 2: only 90% paid)

### Step 6. What changes

The shareholders **subscribed** 100 m.u. but **paid in** only $0.90 \times 100 = 90$ m.u. The remaining 10 m.u. is capital not yet paid (uncalled capital): the shareholders still owe it to the company.

- **Income statement:** **no change**. Revenues and expenses do not depend on how the capital was paid; there is no interest involved. Net income stays 19.6.
- **Cash:** 10 m.u. less: $59.1 - 10 = 49.1$ m.u. All the purchases (60) can still be paid in cash, since the company receives 90.
- **Equity:** the contributed capital is what the stockholders actually provided [Slide 13, Slide 17], so the subscribed capital is shown minus the unpaid part: $100 - 10 = 90$.

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| **Non-current assets** | **38.0** | Subscribed capital | 100.0 |
| Inventory | 10.0 | − Uncalled capital (unpaid by shareholders) | (10.0) |
| Accounts receivable | 12.5 | Retained earnings | 19.6 |
| Cash | 49.1 | **Equity** | **109.6** |
| **Current assets** | **71.6** | **Liabilities** | **0** |
| **Total assets** | **109.6** | **Total liabilities and equity** | **109.6** |

Both totals fall by exactly the 10 m.u. not paid.

## Phase 4 — Interpretation and checks

- **Balance:** $38 + 81.6 = 119.6 = 100 + 19.6$ (requirement 1); $38 + 71.6 = 109.6 = 90 + 19.6$ (requirement 2).
- **Equity bridge:** equity = capital paid + net income retained: $100 + 19.6$ and $90 + 19.6$.
- **Profit vs cash:** after the purchases of 1/01, the cash generated during the year is $37.5 - 10 - 8.4 = 19.1$, while the profit is 19.6. Reconciliation: $19.6 + 2 + 10 - 12.5 = 19.1$, that is, profit + depreciation (expense, never a payment) + materials consumed (expense whose payment was made on 1/01 with the purchase) − sales not collected yet.
- **Presentation note:** some textbooks show the 10 m.u. owed by shareholders as an asset instead of deducting it from capital; then both totals stay at 119.6. The deduction used here is the one consistent with "contributed capital" in [Slide 17]. Both readings give the same net equity provided (109.6) and leave the income statement unchanged.

## Check against the official key

> [!info] Official solution, `T3_Financial Statements_SOLUTIONS.pdf`, pp. 7-8
> Requirement 1 coincides with the key: sales 50; cost of goods sold 10; personnel 10; depreciation 2; EBIT 28; tax 8.4; net income 19.6; cash 59.1; receivables 12.5; inventory 10; land 20; equipment 18; total assets 119.6. The key does not solve requirement 2 (90 % paid in), so that part of the solution is not covered by it.

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
