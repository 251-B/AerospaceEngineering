---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P17
title: "Lumen Optics Space: both statements from the financial structure and the ROA"
category: extra_practice_problem
archetype: reverse-engineering-ratios
unit: 3
difficulty: 3
points: 4.0
time_minutes: 40
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 9-11 and 36"
tags:
  - problem-bank
  - extra-practice
  - financial-structure
  - roa
  - roe
  - leverage
---

# 🧩 Bank P17 — Lumen Optics Space: both statements from the financial structure and the ROA

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Lumen Optics Space S.A. polishes mirrors for Earth-observation satellites. Its investor presentation for 2025 gives only the following information (m.u.):

- total assets at 31/12/2025: 800,000;
- equity finances 60% of the assets;
- of the liabilities, 120,000 are interest-free (suppliers and taxes payable); the rest is a bank loan at 6% per year;
- ROA (income from operations / total assets): 9%;
- operating margin (income from operations / sales): 12%;
- the cost of goods sold is 55% of sales;
- tax rate: 30%.

## Setup

The structure ratios of [Slide 36] fix the right-hand side of the balance sheet; the bank loan then fixes the interest. The ROA gives the income from operations, and from there the income statement can be completed both downward (to net income) and upward (to sales).

**Extension (not defined in the course decks).** $\text{ROA} = \text{Income from operations}/\text{TA}$; $\text{ROE} = \text{Net income}/E$; operating margin $= \text{Income from operations}/\text{Sales}$.

## (a) Find equity, liabilities, the bank loan and its interest [1.0 pts]

### Hint

$\%\,\text{Equity} = E/(E+L)$ and $E + L = \text{TA}$ [Slides 18, 36].

### Checkpoint

- $E = 480{,}000$; $L = 320{,}000$; bank loan 200,000 m.u.
- Interest 12,000 m.u.; $L/E = 0.67$.

### Solution

$$E = 0.60 \times 800{,}000 = 480{,}000 \text{ m.u.}, \qquad L = 800{,}000 - 480{,}000 = 320{,}000 \text{ m.u.}$$

$$\text{Bank loan} = 320{,}000 - 120{,}000 = 200{,}000 \text{ m.u.}, \qquad I = 0.06 \times 200{,}000 = 12{,}000 \text{ m.u.}$$

$$\frac{L}{E} = \frac{320{,}000}{480{,}000} = 0.67$$

## (b) Complete the income statement from the income from operations down to the net income [1.25 pts]

### Hint

Invert the ROA to get the income from operations, then subtract the interest and the tax.

### Checkpoint

- Income from operations 72,000; income before taxes 60,000 m.u.
- Taxes 18,000; net income 42,000 m.u.

### Solution

$$\text{Income from operations} = 0.09 \times 800{,}000 = 72{,}000 \text{ m.u.}$$

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| **Income from operations** | $0.09 \times 800{,}000$ | **72,000** |
| − Interest expense | Part (a) | 12,000 |
| **= Income before taxes** | $72{,}000 - 12{,}000$ | **60,000** |
| − Income taxes (30%) | $0.30 \times 60{,}000$ | 18,000 |
| **= Net income** | $60{,}000 - 18{,}000$ | **42,000** |

## (c) Compute the ROE and compare it with the ROA [0.75 pts]

### Hint

Compare the return on the assets with the cost of the bank loan: when the assets earn more than the debt costs, the surplus goes to the owners.

### Checkpoint

- ROE = 8.75% (extension).
- ROE < ROA here, although the assets earn more (9%) than the debt costs (6%): taxes reduce the owners' return.

### Solution

$$\text{ROE} = \frac{42{,}000}{480{,}000} = 8.75\%$$

The ROA (9%) is measured **before** interest and taxes, while the ROE (8.75%) is measured **after** both. The assets earn 9% and the bank loan costs only 6%, so debt raises the owners' return before taxes:

$$\frac{\text{Income before taxes}}{E} = \frac{60{,}000}{480{,}000} = 12.5\% > 9\%$$

The 30% tax then brings it down to $0.70 \times 12.5\% = 8.75\%$. Leverage helps the owners here; it is the tax, not the debt, that pushes the ROE below the ROA [Slide 36; the after-tax comparison is an extension].

## (d) Find the sales, the cost of goods sold, the gross profit and the operating expenses [1.0 pts]

### Hint

Invert the operating margin to obtain the sales. The operating expenses are the gap between gross profit and income from operations.

### Checkpoint

- Sales 600,000; cost of goods sold 330,000; gross profit 270,000 m.u.
- Operating expenses 198,000 m.u.

### Solution

$$S = \frac{72{,}000}{0.12} = 600{,}000 \text{ m.u.}, \qquad \text{COGS} = 0.55 \times 600{,}000 = 330{,}000 \text{ m.u.}$$

$$\text{Gross profit} = 600{,}000 - 330{,}000 = 270{,}000, \qquad \text{Operating expenses} = 270{,}000 - 72{,}000 = 198{,}000 \text{ m.u.}$$

| Line | m.u. |
| :--- | ---: |
| Sales revenue | 600,000 |
| − Cost of goods sold | 330,000 |
| **= Gross profit** | **270,000** |
| − Operating expenses | 198,000 |
| **= Income from operations** | **72,000** |
| − Interest expense | 12,000 |
| **= Income before taxes** | **60,000** |
| − Income taxes | 18,000 |
| **= Net income** | **42,000** |

## Interpretation

- **Dimensional check:** every ratio dimensionless; amounts in m.u.
- **Order of reasoning:** structure → interest → bottom of the income statement; ROA and margin → top of the income statement. Each published ratio is one equation.
- **Net margin:** $42{,}000 / 600{,}000 = 7\%$ of sales reaches the owners.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
