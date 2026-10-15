---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P16
title: "Stratos Ground Systems: rebuilding the income statement from margins"
category: extra_practice_problem
archetype: reverse-engineering-ratios
unit: 3
difficulty: 3
points: 4.0
time_minutes: 40
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 9-11"
tags:
  - problem-bank
  - extra-practice
  - income-statement
  - ratios
  - roa
  - roe
---

# 🧩 Bank P16 — Stratos Ground Systems: rebuilding the income statement from margins

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Stratos Ground Systems S.L. builds antenna stations for satellite operators. In its 2025 annual report only percentages and a few amounts are published (m.u.):

- gross margin: gross profit is 40% of sales;
- operating expenses (salaries, rent, depreciation, etc.): 150,000;
- the only debt that bears interest is a bank loan of 200,000 at 5% per year;
- corporate income tax: 25% of the income before taxes;
- net margin: net income is 6% of sales;
- ROE: 10%; ROA: 8% (both on year-end figures, see Setup);
- inventory: 40,000 at 1/1/2025 and 55,000 at 31/12/2025.

## Setup

Write every line of the extended income statement [Slides 9-11] as a function of the unknown sales $S$. The net margin then gives one equation in $S$.

**Extension (not defined in the course decks).** Net margin $= \text{Net income}/\text{Sales}$; $\text{ROA} = \text{Income from operations}/\text{Total assets}$; $\text{ROE} = \text{Net income}/\text{Equity}$. These are the definitions used in the solved Infopymes problem of the portal. Total assets and equity are taken at year end (31/12/2025).

## (a) Find the sales of 2025 [1.5 pts]

### Hint

Gross profit $= 0.40\,S$; income from operations $= 0.40\,S - 150{,}000$; subtract the interest, apply the 25% tax, and set the result equal to $0.06\,S$.

### Checkpoint

- Interest 10,000 m.u.
- Equation $0.75\,(0.40\,S - 160{,}000) = 0.06\,S$.
- Sales $S = 500{,}000$ m.u.

### Solution

#### Step 1. Interest

$$I = 0.05 \times 200{,}000 = 10{,}000 \text{ m.u.}$$

#### Step 2. Lines as functions of $S$

$$\text{Gross profit} = 0.40\,S, \qquad \text{Income from operations} = 0.40\,S - 150{,}000$$

$$\text{Income before taxes} = 0.40\,S - 150{,}000 - 10{,}000 = 0.40\,S - 160{,}000$$

$$\text{Net income} = (1 - 0.25)(0.40\,S - 160{,}000) = 0.75\,(0.40\,S - 160{,}000)$$

#### Step 3. Net margin equation

$$0.75\,(0.40\,S - 160{,}000) = 0.06\,S$$

$$0.30\,S - 120{,}000 = 0.06\,S \;\Rightarrow\; 0.24\,S = 120{,}000 \;\Rightarrow\; S = \frac{120{,}000}{0.24} = 500{,}000 \text{ m.u.}$$

## (b) Present the complete income statement [0.75 pts]

### Hint

Substitute $S = 500{,}000$ into each line of Step 2 and verify the net margin.

### Checkpoint

- Cost of goods sold 300,000; income from operations 50,000 m.u.
- Net income 30,000 m.u. ($= 6\%$ of 500,000 ✓).

### Solution

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Sales revenue | Part (a) | 500,000 |
| − Cost of goods sold | $0.60 \times 500{,}000$ | 300,000 |
| **= Gross profit** | $0.40 \times 500{,}000$ | **200,000** |
| − Operating expenses | given | 150,000 |
| **= Income from operations** | $200{,}000 - 150{,}000$ | **50,000** |
| − Interest expense | $0.05 \times 200{,}000$ | 10,000 |
| **= Income before taxes** | $50{,}000 - 10{,}000$ | **40,000** |
| − Income taxes (25%) | $0.25 \times 40{,}000$ | 10,000 |
| **= Net income** | $40{,}000 - 10{,}000$ | **30,000** |

Check: $30{,}000 / 500{,}000 = 6\%$ ✓.

## (c) Use ROA and ROE to find total assets, equity, liabilities and the debt-to-equity ratio [1.0 pts]

### Hint

Each ratio has one known numerator from part (b): invert it to obtain its denominator.

### Checkpoint

- Total assets 625,000; equity 300,000; liabilities 325,000 m.u.
- $L/E = 1.08$; equity 48% of the financing.

### Solution

$$\text{TA} = \frac{\text{Income from operations}}{\text{ROA}} = \frac{50{,}000}{0.08} = 625{,}000 \text{ m.u.}, \qquad E = \frac{\text{Net income}}{\text{ROE}} = \frac{30{,}000}{0.10} = 300{,}000 \text{ m.u.}$$

$$L = \text{TA} - E = 625{,}000 - 300{,}000 = 325{,}000 \text{ m.u.}, \qquad \frac{L}{E} = \frac{325{,}000}{300{,}000} = 1.08, \qquad \%\,E = \frac{300{,}000}{625{,}000} = 48\%$$

Of the 325,000 m.u. of liabilities, only 200,000 bear interest; the other 125,000 are interest-free debts such as suppliers and taxes payable.

## (d) Compute the purchases of goods in 2025 [0.75 pts]

### Hint

Turn the relation $\text{COGS} = \text{Opening inventory} + \text{Purchases} - \text{Closing inventory}$ around.

### Checkpoint

- Purchases 315,000 m.u.: more than the cost of goods sold because the inventory grew by 15,000.

### Solution

$$\text{Purchases} = \text{COGS} + \text{Closing inventory} - \text{Opening inventory} = 300{,}000 + 55{,}000 - 40{,}000 = 315{,}000 \text{ m.u.}$$

## Interpretation

- **Dimensional check:** margins and returns are dimensionless; dividing m.u. by a dimensionless ratio returns m.u.
- **ROE above ROA here:** $10\% > 8\%$ because the debt finances part of the assets; the owners earn on the whole asset base while contributing only 48% of the money (financial leverage, [Slide 36]; the quantitative relation is an extension).
- **Typical mistake:** applying the tax rate to the income from operations instead of the income before taxes.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
