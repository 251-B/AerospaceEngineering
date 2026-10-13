---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
origen: "T3_Financial Statements_EXERCISES.pdf, Exercise 5, p. 2"
dificultad: medium
tags:
  - problem
  - solved
  - income-statement
  - dividends
---

# ✏️ Problem: Exercise 5 — Income statement 2017 with discounts, payroll, depreciation, taxes and dividends

## 📄 Statement

Prepare the income statement of a company with the following information for 2017:
- Gross sales during the year reached 2,002 million €. The company's trade policy gives a 3% discount to its Type A customers, those whose annual purchases from the company exceed 120 million €. Type A customers account for 40% of sales. Assume total sales = gross sales − discount.
- Purchases of raw materials amounted to 962 million €.
- The workforce consists of 7,800 employees. The average salary is 30,000 € per year, and the average spending on Social Security is 30% of the salary.
- Payments for other operating expenses amounted to 457 million €.
- In recent years the company has invested a total of 1,200 million € in fixed assets with an average lifespan of 10 years (linear depreciation, no residual value).
- The company obtained an international loan of 225 million € in 2015, at 6% interest along the whole year; the whole principal will be repaid in 2020.
- The corporate tax rate is 30%. The company has agreed to a dividend of 50%.
- Assume no change in stocks of raw materials or finished products during the year.

## Phase 1 — Setup: units and hypotheses

All amounts are expressed in **millions of euros (M€)**. Salaries are given per employee in €, so they must be converted: $1 \text{ M€} = 10^6$ €.

**Hypotheses:**
1. "No change in stocks" means initial inventory = final inventory, so $\text{COGS} = \text{Purchases}$.
2. The 120 M€ threshold only defines who is a Type A customer; the statement already says these customers make 40% of the sales, so the discount applies to that 40%.
3. The loan principal is not an expense: only its interest enters the income statement [Slide 11].
4. The dividend of 50% is applied to the **net income** [Slide 23].

## Phase 2 — Frames: line of each item

| Item | Line |
| :--- | :--- |
| Gross sales − discount | Sales revenue (net) |
| Raw materials (no stock change) | Cost of goods sold |
| Salaries + Social Security | Operating expense |
| Other operating expenses | Operating expense |
| Depreciation of fixed assets | Operating expense [Slide 10] |
| Interest on the loan | Non-operating item [Slide 11] |
| Tax 30% | Income taxes |
| Dividend 50% | Distribution of net income (not an expense) |

## Phase 3 — Derivation

### Step 1. Net sales

$$\text{Type A sales} = 0.40 \times 2{,}002 = 800.8 \text{ M€}, \qquad \text{Discount} = 0.03 \times 800.8 = 24.024 \text{ M€}$$

$$\text{Net sales} = 2{,}002 - 24.024 = 1{,}977.976 \text{ M€}$$

### Step 2. Personnel expense

$$\text{Salaries} = 7{,}800 \times 30{,}000 = 234{,}000{,}000 \text{ €} = 234 \text{ M€}$$

$$\text{Social Security} = 0.30 \times 234 = 70.2 \text{ M€}, \qquad \text{Personnel} = 234 + 70.2 = 304.2 \text{ M€}$$

### Step 3. Depreciation and interest

$$D = \frac{1{,}200 - 0}{10} = 120 \text{ M€/year}, \qquad I = 225 \times 0.06 = 13.5 \text{ M€}$$

### Step 4. Income statement 2017

| Line | Computation | M€ |
| :--- | :--- | ---: |
| Net sales | Step 1 | 1,977.976 |
| − Cost of goods sold (raw materials) | | 962.000 |
| **= Gross profit** | $1{,}977.976 - 962$ | **1,015.976** |
| − Personnel | Step 2 | 304.200 |
| − Other operating expenses | | 457.000 |
| − Depreciation | Step 3 | 120.000 |
| **= Income from operations** | $1{,}015.976 - 881.2$ | **134.776** |
| − Interest expense | Step 3 | 13.500 |
| **= Income before taxes** | $134.776 - 13.5$ | **121.276** |
| − Income taxes (30%) | $0.30 \times 121.276$ | 36.383 |
| **= Net income** | $121.276 - 36.3828$ | **84.893** |

### Step 5. Distribution of the net income [Slide 23]

$$\text{Dividends} = 0.50 \times 84.8932 = 42.447 \text{ M€}, \qquad \text{Retained earnings} = 84.8932 - 42.4466 = 42.447 \text{ M€}$$

Pay-out 50%, self-financing 50%.

## Phase 4 — Interpretation and checks

- **Applying the discount to all the sales** would deduct $0.03 \times 2{,}002 = 60.06$ M€ instead of 24.024: the 40% restriction matters.
- **The loan repayment in 2020** does not appear in 2017: repaying principal is a payment that is never an expense.
- **Exact values:** income taxes 36.3828 M€ and net income 84.8932 M€ (shown rounded to three decimals in the table).
- **Dividends** come after taxes and are not an expense: the income statement ends at the net income, and the 50/50 split is shown separately.

## Check against the official key

> [!info] Official solution, `T3_Financial Statements_SOLUTIONS.pdf`, p. 6
> Every line coincides with the key: discount 24.024; net sales 1,977.976; cost of goods sold 962; personnel 304.2; other operating expenses 457; depreciation 120; EBIT 134.776; interest 13.5; income before taxes 121.276; tax 36.3828; net income 84.8932; dividends 42.4466 and retained earnings 42.4466 (all in M€).

---

**Back to:** [[Business Management MOC]]

**Related notes:** [[Concept - Method to Build the Income Statement and Balance Sheet]] · [[Topic 3 - Financial Management I - Financial Statements]]
