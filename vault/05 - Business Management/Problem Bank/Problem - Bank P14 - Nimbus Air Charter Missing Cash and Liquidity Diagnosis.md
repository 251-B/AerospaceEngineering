---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P14
title: "Nimbus Air Charter: the missing cash figure and a liquidity diagnosis"
category: extra_practice_problem
archetype: unordered-items
unit: 3
difficulty: 3
points: 4.0
time_minutes: 45
official: false
origen: "Practice item written for the problem bank (not an official exercise), in the style of Topic 3_Financial Management (I).pdf, Slides 19, 31, 35 and 36"
tags:
  - problem-bank
  - extra-practice
  - balance-sheet
  - working-capital
  - leverage
  - short-term-financing
---

# 🧩 Bank P14 — Nimbus Air Charter: the missing cash figure and a liquidity diagnosis

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

Nimbus Air Charter S.A. operates three turboprops for executive flights. A file corruption deleted the cash balance at 31/12/2025; everything else survived (m.u.). The tax rate is 30% (payable in 2026). On 31/12/2025 the board declared a dividend of 50% of the net income, to be paid in January 2026.

| Item | m.u. |
| :--- | ---: |
| Charter revenue of 2025 | 520,000 |
| Fuel | 160,000 |
| Crew salaries and Social Security | 140,000 |
| Maintenance | 45,000 |
| Airport and navigation fees | 38,000 |
| Depreciation of aircraft | 72,000 |
| Amortization of flight-planning software | 6,000 |
| Interest on the long-term loan | 21,000 |
| Interest on the bank credit line | 3,000 |
| Aircraft at cost | 900,000 |
| Accumulated depreciation of aircraft | 300,000 |
| Software at cost | 30,000 |
| Accumulated amortization of software | 10,000 |
| Fuel and spare parts in stock | 12,000 |
| Accounts receivable | 25,000 |
| Long-term loan (total outstanding; 70,000 repayable in 2026) | 350,000 |
| Bank credit line: limit 100,000, drawn at 31/12 | 60,000 |
| Accounts payable to fuel suppliers | 48,000 |
| Flights paid in advance by customers, to be flown in 2026 | 30,000 |
| Contributed capital | 250,000 |
| Retained earnings at 1/1/2025 | 8,000 |

## Setup

The balance sheet must satisfy $\text{Assets} = \text{Liabilities} + \text{Equity}$ [Slide 12], so a single missing figure can always be recovered as the balancing item once everything else is placed. The bank credit line is short-term bank financing: the bank makes a maximum available and interest is paid only on the amount drawn [Slides 31, 35].

**Extension (not defined in the course decks).** Working capital $= \text{CA} - \text{CL}$; current ratio $= \text{CA}/\text{CL}$.

## (a) Prepare the income statement for 2025 [1.0 pts]

### Hint

Nimbus sells a service, so there is no cost of goods sold line: all its operating costs go to operating expenses. Both interests are non-operating items.

### Checkpoint

- Operating expenses 461,000; income from operations 59,000 m.u.
- Income before taxes 35,000; taxes 10,500; net income 24,500 m.u.

### Solution

| Line | Computation | m.u. |
| :--- | :--- | ---: |
| Charter revenue | | 520,000 |
| − Fuel, crew, maintenance, fees | $160{,}000 + 140{,}000 + 45{,}000 + 38{,}000$ | 383,000 |
| − Depreciation and amortization | $72{,}000 + 6{,}000$ | 78,000 |
| **= Income from operations** | $520{,}000 - (383{,}000 + 78{,}000) = 520{,}000 - 461{,}000$ | **59,000** |
| − Interest expense | $21{,}000 + 3{,}000$ | 24,000 |
| **= Income before taxes** | $59{,}000 - 24{,}000$ | **35,000** |
| − Income taxes (30%) | $0.30 \times 35{,}000$ | 10,500 |
| **= Net income** | $35{,}000 - 10{,}500$ | **24,500** |

## (b) Recover the cash balance at 31/12/2025 and present the balance sheet [1.5 pts]

### Hint

First close the right-hand side completely (equity after the dividend, long-term and current liabilities). Then subtract every known asset from that total.

### Checkpoint

- Dividend payable 12,250; equity 270,250 m.u.
- Current liabilities 230,750; long-term liabilities 280,000 m.u.
- Total 781,000 m.u.; cash = 124,000 m.u.

### Solution

#### Step 1. Equity [Slide 23]

$$\text{Dividend} = 0.50 \times 24{,}500 = 12{,}250, \qquad \text{Retained earnings}_{31/12} = 8{,}000 + 24{,}500 - 12{,}250 = 20{,}250$$

$$E = 250{,}000 + 20{,}250 = 270{,}250 \text{ m.u.}$$

#### Step 2. Liabilities by maturity [Slide 16]

$$\text{Long-term loan, part after 2026} = 350{,}000 - 70{,}000 = 280{,}000 \text{ m.u.}$$

$$\text{CL} = 70{,}000 + 60{,}000 + 48{,}000 + 30{,}000 + 10{,}500 + 12{,}250 = 230{,}750 \text{ m.u.}$$

$$\text{Total liabilities and equity} = 270{,}250 + 280{,}000 + 230{,}750 = 781{,}000 \text{ m.u.}$$

#### Step 3. Cash as the balancing item

$$\text{Known assets} = (900{,}000 - 300{,}000) + (30{,}000 - 10{,}000) + 12{,}000 + 25{,}000 = 657{,}000$$

$$\text{Cash} = 781{,}000 - 657{,}000 = 124{,}000 \text{ m.u.}$$

#### Step 4. Balance sheet

| Assets | m.u. | Liabilities and equity | m.u. |
| :--- | ---: | :--- | ---: |
| Aircraft (900,000 − 300,000) | 600,000 | Contributed capital | 250,000 |
| Software (30,000 − 10,000) | 20,000 | Retained earnings | 20,250 |
| **Non-current assets** | **620,000** | **Equity** | **270,250** |
| Fuel and spare parts | 12,000 | Long-term loan (after 2026) | 280,000 |
| Accounts receivable | 25,000 | **Long-term liabilities** | **280,000** |
| Cash | 124,000 | Loan instalment due in 2026 | 70,000 |
| | | Bank credit line drawn | 60,000 |
| | | Accounts payable | 48,000 |
| | | Flights paid in advance | 30,000 |
| | | Income taxes payable | 10,500 |
| | | Dividend payable | 12,250 |
| **Current assets** | **161,000** | **Current liabilities** | **230,750** |
| **Total assets** | **781,000** | **Total liabilities and equity** | **781,000** |

## (c) Compute the working capital, the current ratio and the debt-to-equity ratio [0.75 pts]

### Hint

A negative working capital means that part of the long-lived assets is financed with debts due within the year.

### Checkpoint

- Working capital −69,750 m.u.; current ratio 0.70 (extension).
- Debt-to-equity 1.89; equity 34.6% of the financing.

### Solution

$$\text{Working capital} = 161{,}000 - 230{,}750 = -69{,}750 \text{ m.u.}, \qquad \text{Current ratio} = \frac{161{,}000}{230{,}750} = 0.70$$

$$\frac{L}{E} = \frac{280{,}000 + 230{,}750}{270{,}250} = \frac{510{,}750}{270{,}250} = 1.89, \qquad \%\,\text{Equity} = \frac{270{,}250}{781{,}000} = 34.6\%$$

## (d) Diagnose the financial position and propose two measures from the course's financing sources [0.75 pts]

### Hint

Look at which side of the balance sheet the problem lies on (maturity of debts, not profitability), then pick instruments from the map of financing sources [Slides 21-22, 35].

### Checkpoint

- Profitable but illiquid: debts due within a year exceed current assets.
- Measures: lengthen the debt (long-term loan or leasing instead of the credit line), retain profits (no dividend), or bring in equity; factoring of receivables helps only marginally (25,000).

### Solution

Nimbus is **profitable** (net income 24,500 m.u.) but its **short-term liquidity is weak**: the current liabilities exceed the current assets by 69,750 m.u., and the leverage (1.89) is high, which increases the risk for shareholders [Slide 36]. Part of the aircraft fleet is effectively financed with short-term money (the credit line and the debts due in 2026).

Measures consistent with the course:
1. **Replace the credit line with long-term financing** (a long-term loan, or leasing for the next aircraft [Slides 31, 33]), so that long-lived assets are financed with long-lived resources.
2. **Increase self-financing** by cancelling or reducing the dividend: the 12,250 m.u. would stay in the company with no explicit cost [Slides 23-24].
3. **A capital increase** (rights issue) would reduce leverage directly [Slide 26]. Factoring the receivables [Slide 35] brings cash forward but only 25,000 m.u. are available, so it cannot solve the gap alone.

## Interpretation

- **Dimensional check:** all in m.u.; ratios dimensionless.
- **Profit is not liquidity:** a firm can earn a profit and still struggle to pay its short-term debts; the balance sheet shows maturities, the income statement does not.
- **Why the advance from customers is a liability:** Nimbus owes flights, not money, but it is an obligation to be settled within the year [Slide 13].

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
