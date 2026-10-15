---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P15
title: "Vector Avionics: closing the gaps of a balance sheet with three ratios"
category: extra_practice_problem
archetype: reverse-engineering-ratios
unit: 3
difficulty: 2
points: 4.0
time_minutes: 35
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 18, 23 and 36"
tags:
  - problem-bank
  - extra-practice
  - balance-sheet
  - ratios
  - working-capital
  - leverage
---

# 🧩 Bank P15 — Vector Avionics: closing the gaps of a balance sheet with three ratios

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Vector Avionics S.A. designs flight-control computers. A bank analyst received its balance sheet at 31/12/2025 with four figures blanked out ($X$, $W$, $Y$, $Z$), together with three ratios computed by the company's auditor (m.u.).

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Equipment (net) | 280,000 | Contributed capital | 200,000 |
| Patents (net) | 40,000 | Retained earnings | $Z$ |
| Inventory | 70,000 | Long-term bank loan | $Y$ |
| Accounts receivable | 65,000 | Accounts payable | 80,000 |
| Cash | $X$ | Short-term bank loan | $W$ |

Ratios at 31/12/2025:
- working capital $= 60{,}000$ m.u.;
- current ratio $= 1.5$;
- debt-to-equity ratio $L/E = 1.0$.

In 2025 the net income was 30,000 m.u. and the company paid 40% of it as dividends.

## Setup

The unknowns sit in different blocks of the balance sheet, so each ratio unlocks one block:
- working capital and current ratio involve only current assets (CA) and current liabilities (CL);
- the balance-sheet identity [Slide 18] gives total assets, hence total liabilities plus equity;
- the debt-to-equity ratio [Slide 36] splits that total between $L$ and $E$.

**Extension (not defined in the course decks).** Working capital $= \text{CA} - \text{CL}$; current ratio $= \text{CA}/\text{CL}$; $\text{ROE} = \text{Net income}/\text{Equity}$.

## (a) Find the current assets, the current liabilities, the cash $X$ and the short-term loan $W$ [1.25 pts]

### Hint

You have two equations in CA and CL: $\text{CA} - \text{CL} = 60{,}000$ and $\text{CA} = 1.5\,\text{CL}$. Substitute the second into the first.

### Checkpoint

- CL = 120,000 m.u.; CA = 180,000 m.u.
- $X = 45{,}000$ m.u.; $W = 40{,}000$ m.u.

### Solution

#### Step 1. Solve the two liquidity equations

Substituting $\text{CA} = 1.5\,\text{CL}$ into $\text{CA} - \text{CL} = 60{,}000$:

$$1.5\,\text{CL} - \text{CL} = 0.5\,\text{CL} = 60{,}000 \;\Rightarrow\; \text{CL} = \frac{60{,}000}{0.5} = 120{,}000 \text{ m.u.}$$

$$\text{CA} = 1.5 \times 120{,}000 = 180{,}000 \text{ m.u.}$$

#### Step 2. The unknown items

$$X = \text{CA} - \text{Inventory} - \text{Receivables} = 180{,}000 - 70{,}000 - 65{,}000 = 45{,}000 \text{ m.u.}$$

$$W = \text{CL} - \text{Accounts payable} = 120{,}000 - 80{,}000 = 40{,}000 \text{ m.u.}$$

## (b) Find total assets, equity, total liabilities, the long-term loan $Y$ and retained earnings $Z$ [1.25 pts]

### Hint

Total assets follow from the asset side, now complete. With $L/E = 1$, liabilities and equity are equal halves of the total.

### Checkpoint

- Total assets 500,000 m.u.
- $E = L = 250{,}000$ m.u.
- $Y = 130{,}000$ m.u.; $Z = 50{,}000$ m.u.

### Solution

#### Step 1. Total assets

$$\text{Non-current assets} = 280{,}000 + 40{,}000 = 320{,}000, \qquad \text{TA} = 320{,}000 + 180{,}000 = 500{,}000 \text{ m.u.}$$

#### Step 2. Split by the debt-to-equity ratio

$$L + E = 500{,}000, \qquad \frac{L}{E} = 1 \;\Rightarrow\; L = E \;\Rightarrow\; 2E = 500{,}000 \;\Rightarrow\; E = L = 250{,}000 \text{ m.u.}$$

#### Step 3. The two unknown items

$$Y = L - \text{CL} = 250{,}000 - 120{,}000 = 130{,}000 \text{ m.u.}$$

$$Z = E - \text{Contributed capital} = 250{,}000 - 200{,}000 = 50{,}000 \text{ m.u.}$$

## (c) Present the complete balance sheet [0.75 pts]

### Hint

Order the items by the course layout: non-current before current assets; equity, then long-term, then current liabilities [Slide 18].

### Checkpoint

- 500,000 m.u. on both sides; equity 50%.

### Solution

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Equipment (net) | 280,000 | Contributed capital | 200,000 |
| Patents (net) | 40,000 | Retained earnings | 50,000 |
| **Non-current assets** | **320,000** | **Equity** | **250,000** |
| Inventory | 70,000 | Long-term bank loan | 130,000 |
| Accounts receivable | 65,000 | **Long-term liabilities** | **130,000** |
| Cash | 45,000 | Accounts payable | 80,000 |
| | | Short-term bank loan | 40,000 |
| **Current assets** | **180,000** | **Current liabilities** | **120,000** |
| **Total assets** | **500,000** | **Total liabilities and equity** | **500,000** |

## (d) Find the retained earnings at 1/1/2025 and the ROE of 2025 [0.75 pts]

### Hint

Retained earnings grow each year by the part of the net income that is not distributed [Slide 23].

### Checkpoint

- Retained in 2025: 18,000 m.u.; retained earnings at 1/1/2025: 32,000 m.u.
- ROE = 12% (extension).

### Solution

$$\text{Retained in 2025} = (1 - 0.40) \times 30{,}000 = 18{,}000 \text{ m.u.}$$

$$Z_{1/1/2025} = Z_{31/12/2025} - 18{,}000 = 50{,}000 - 18{,}000 = 32{,}000 \text{ m.u.}$$

$$\text{ROE} = \frac{30{,}000}{250{,}000} = 12\% \quad \text{(extension, on year-end equity)}$$

## Interpretation

- **Consistency check:** $\text{CA}/\text{CL} = 180{,}000/120{,}000 = 1.5$ and $\text{CA} - \text{CL} = 60{,}000$ ✓; $L/E = 250{,}000/250{,}000 = 1$ ✓.
- **Why three ratios are enough:** each ratio is one equation; together with the balance identity they determine four unknowns because two of them (CA, CL) are intermediate totals.
- **Reading the result:** a leverage of 1 means each m.u. of owners' money is matched by one m.u. of debt; the bank analyst will check that the current assets comfortably cover the current debts (they do, 1.5 times).

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
