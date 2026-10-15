---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P18
title: "Corvid Drone Works: reconstructing equity from the pay-out and a rights issue"
category: extra_practice_problem
archetype: reverse-engineering-ratios
unit: 3
difficulty: 2
points: 4.0
time_minutes: 35
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 17, 23-26 and 36"
tags:
  - problem-bank
  - extra-practice
  - equity
  - self-financing
  - rights-issue
  - leverage
---

# 🧩 Bank P18 — Corvid Drone Works: reconstructing equity from the pay-out and a rights issue

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Corvid Drone Works S.A. makes inspection drones for wind farms and airports. The equity section of its balance sheet is known only at 31/12/2024: contributed capital 150,000 m.u. (shares of nominal value 10 m.u.) and retained earnings 40,000 m.u. For 2025 the following is known (m.u.):

- the pay-out ratio of 2025 was 35%, and the dividend was paid in cash in 2025;
- retained earnings increased by 26,000 during 2025;
- during 2025 the company issued new shares at their nominal value (no premium), fully paid in cash;
- at 31/12/2025 total liabilities were 200,000 (long-term loan 120,000; accounts payable 67,000; taxes payable 13,000) and the debt-to-equity ratio was 0.8;
- assets at 31/12/2025: non-current assets 300,000; inventory 60,000; accounts receivable 55,000; cash $X$.

## Setup

Retained earnings change only by the undistributed profit [Slides 17, 23]:

$$\Delta\,\text{Retained earnings} = \text{Net income} - \text{Dividends} = (1 - \text{pay-out}) \times \text{Net income}$$

Contributed capital changes only through rights issues (capital increases) [Slides 25-26]. The debt-to-equity ratio [Slide 36] fixes the total equity at year end.

**Extension (not defined in the course decks).** $\text{ROE} = \text{Net income}/E$; current ratio $= \text{CA}/\text{CL}$.

## (a) Find the net income and the dividend of 2025 [1.0 pts]

### Hint

The 26,000 m.u. retained are the self-financing share of the profit, that is $1 - 0.35 = 65\%$ of it.

### Checkpoint

- Net income 40,000 m.u.; dividend 14,000 m.u.
- Self-financing ratio 65%.

### Solution

$$0.65 \times \text{NI} = 26{,}000 \;\Rightarrow\; \text{NI} = \frac{26{,}000}{0.65} = 40{,}000 \text{ m.u.}$$

$$\text{Dividend} = 0.35 \times 40{,}000 = 14{,}000 \text{ m.u.}, \qquad \text{check: } 40{,}000 - 14{,}000 = 26{,}000 \;✓$$

## (b) Find equity at 31/12/2025, the contributed capital and the number of new shares issued [1.25 pts]

### Hint

$L/E = 0.8$ with $L = 200{,}000$ gives $E$. Subtract the retained earnings at the close of 2025 to obtain the capital.

### Checkpoint

- $E = 250{,}000$; retained earnings 66,000; capital 184,000 m.u.
- Rights issue 34,000 m.u. = 3,400 new shares.

### Solution

$$E = \frac{L}{0.8} = \frac{200{,}000}{0.8} = 250{,}000 \text{ m.u.}$$

$$\text{Retained earnings}_{2025} = 40{,}000 + 26{,}000 = 66{,}000, \qquad \text{Capital}_{2025} = 250{,}000 - 66{,}000 = 184{,}000 \text{ m.u.}$$

$$\text{Rights issue} = 184{,}000 - 150{,}000 = 34{,}000 \text{ m.u.}, \qquad \text{New shares} = \frac{34{,}000}{10} = 3{,}400$$

## (c) Find the cash $X$ and present the balance sheet at 31/12/2025 [1.0 pts]

### Hint

Total assets equal $E + L$. Cash is the only missing asset.

### Checkpoint

- Total 450,000 m.u.; $X = 35{,}000$ m.u.
- Current ratio 1.88 (extension).

### Solution

$$\text{TA} = 250{,}000 + 200{,}000 = 450{,}000, \qquad X = 450{,}000 - 300{,}000 - 60{,}000 - 55{,}000 = 35{,}000 \text{ m.u.}$$

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| **Non-current assets** | **300,000** | Contributed capital | 184,000 |
| Inventory | 60,000 | Retained earnings | 66,000 |
| Accounts receivable | 55,000 | **Equity** | **250,000** |
| Cash | 35,000 | Long-term loan | 120,000 |
| | | **Long-term liabilities** | **120,000** |
| | | Accounts payable | 67,000 |
| | | Taxes payable | 13,000 |
| **Current assets** | **150,000** | **Current liabilities** | **80,000** |
| **Total assets** | **450,000** | **Total liabilities and equity** | **450,000** |

$$\text{Current ratio} = \frac{150{,}000}{67{,}000 + 13{,}000} = \frac{150{,}000}{80{,}000} = 1.88$$

## (d) Compute the ROE of 2025 and compare the two ways in which equity grew [0.75 pts]

### Hint

Equity grew by internal equity (self-financing) and by external equity (the rights issue). Compare their sizes and their features in the course.

### Checkpoint

- Equity grew from 190,000 to 250,000 (+60,000): 26,000 self-financing + 34,000 rights issue.
- ROE = 16% (extension).

### Solution

$$\text{ROE} = \frac{40{,}000}{250{,}000} = 16\%$$

| Source | Amount (m.u.) | Feature in the course |
| :--- | ---: | :--- |
| Self-financing (retained earnings) | 26,000 | Internal; generated by the activity; no new owners [Slides 23-24] |
| Rights issue | 34,000 | External equity; never repaid; new shareholders share future dividends [Slides 25-26] |

More than half of the growth of equity came from new shareholders. That allowed the company to reach a leverage of 0.8 without borrowing more, but it also spreads future dividends over 3,400 more shares.

## Interpretation

- **Dimensional check:** shares = m.u. / (m.u. per share); ratios dimensionless.
- **Two equations, two unknowns:** the pay-out fixes the profit split; the leverage fixes the size of equity. The rights issue is the residual.
- **Typical mistake:** dividing the 26,000 by the pay-out (35%) instead of by the self-financing ratio (65%).

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
