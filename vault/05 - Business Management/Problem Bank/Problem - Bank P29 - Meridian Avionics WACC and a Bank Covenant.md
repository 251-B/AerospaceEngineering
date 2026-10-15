---
materia: Business Management
tema: "Topic 3: Financial Management (I) - Financial Statements"
bank_id: P29
title: "Meridian Avionics: choosing a capital structure with the WACC and a bank covenant"
category: extra_practice_problem
archetype: financing-leverage
unit: 3
difficulty: 2
points: 4.0
time_minutes: 35
official: false
origen: "Practice item written for the problem bank (not an official exercise), using Topic 3_Financial Management (I).pdf, Slides 5, 36 and 37"
tags:
  - problem-bank
  - extra-practice
  - wacc
  - capital-structure
  - value-creation
  - leverage
---

# 🧩 Bank P29 — Meridian Avionics: choosing a capital structure with the WACC and a bank covenant

> [!info] Practice item
> Written for the problem bank in the style of the course exercises. It is not an official exercise and has no official key.

## Statement

**Meridian Avionics S.A.** needs 5,000,000 m.u. to finance its assets. Its banks and its investors have quoted the following costs for three possible structures:

| Structure | Equity share | Liabilities share | Cost of equity $K_{EQ}$ | Cost of liabilities $K_L$ |
| :--- | ---: | ---: | ---: | ---: |
| S1 | 80% | 20% | 10.0% | 5.0% |
| S2 | 60% | 40% | 11.0% | 5.5% |
| S3 | 40% | 60% | 12.0% | 6.0% |

The main bank imposes a **covenant**: the debt-to-equity ratio must not exceed 1.0. The assets are expected to earn a return of 9.5% per year.

## Setup

The capital cost of the company is the weighted average of the costs of its financial resources [Slide 37]:

$$K_{WACC} = K_{EQ}\,\frac{E}{E+L} + K_L\,\frac{L}{E+L}$$

The company creates value when the return on its assets is above the cost of the funds that finance them (profitability > cost) [Slide 5]. Both costs rise with leverage, because lenders and owners demand more when the risk is higher [Slide 36].

## (a) Compute the amounts of equity and liabilities and the debt-to-equity ratio of each structure [0.75 pts]

### Hint

$L/E = \%L / \%E$.

### Checkpoint

- S1: $E$ 4,000,000, $L$ 1,000,000, $L/E$ 0.25.
- S2: $E$ 3,000,000, $L$ 2,000,000, $L/E$ 0.67.
- S3: $E$ 2,000,000, $L$ 3,000,000, $L/E$ 1.50.

### Solution

| Structure | $E$ (m.u.) | $L$ (m.u.) | $L/E$ |
| :--- | ---: | ---: | ---: |
| S1 | $0.80 \times 5{,}000{,}000 = 4{,}000{,}000$ | 1,000,000 | 0.25 |
| S2 | 3,000,000 | 2,000,000 | 0.67 |
| S3 | 2,000,000 | 3,000,000 | 1.50 |

## (b) Compute the WACC of each structure and its annual cost in m.u. [1.25 pts]

### Hint

Multiply each cost by its weight and add. The annual cost is the WACC times the 5,000,000 m.u.

### Checkpoint

- WACC: S1 9.0%, S2 8.8%, S3 8.4%.
- Annual cost: 450,000 / 440,000 / 420,000 m.u.

### Solution

$$K_{S1} = 0.10 \times 0.80 + 0.05 \times 0.20 = 0.080 + 0.010 = 9.0\%$$

$$K_{S2} = 0.11 \times 0.60 + 0.055 \times 0.40 = 0.066 + 0.022 = 8.8\%$$

$$K_{S3} = 0.12 \times 0.40 + 0.06 \times 0.60 = 0.048 + 0.036 = 8.4\%$$

| Structure | WACC | Annual cost of capital (m.u.) |
| :--- | ---: | ---: |
| S1 | 9.0% | $0.090 \times 5{,}000{,}000 = 450{,}000$ |
| S2 | 8.8% | 440,000 |
| S3 | 8.4% | 420,000 |

## (c) Choose the structure, taking the covenant into account [0.75 pts]

### Hint

First discard any structure that breaks the covenant; then compare the WACC of the rest.

### Checkpoint

- S3 has the lowest WACC (8.4%) but breaks the covenant ($1.50 > 1.0$): not allowed.
- Among the allowed structures, S2 has the lowest WACC (8.8% < 9.0%): chosen.

### Solution

S3 would be the cheapest structure (8.4%), but its debt-to-equity ratio of 1.50 exceeds the limit of 1.0 imposed by the bank, so it is not available: the covenant is what decides the choice. Between the two structures that respect it, **S2** gives the lowest capital cost (8.8% against 9.0%), saving 10,000 m.u. per year. Moving from S1 to S2 lowers the WACC because more of the cheaper source (debt) is used while its cost rises only slightly; the covenant caps how far Meridian can go down that path.

## (d) Check whether the assets create value under each structure, and by how much per year [1.25 pts]

### Hint

Compare the expected return of 9.5% with each WACC; the yearly surplus is the difference times 5,000,000. What does the covenant cost the company?

### Checkpoint

- S1: +0.5% → +25,000 m.u.; S2: +0.7% → +35,000 m.u.; S3: +1.1% → +55,000 m.u. (not allowed).
- Cost of the covenant: 55,000 − 35,000 = 20,000 m.u. per year.

### Solution

| Structure | Return − WACC | Value created per year (m.u.) |
| :--- | ---: | ---: |
| S1 | $9.5\% - 9.0\% = +0.5\%$ | $0.005 \times 5{,}000{,}000 = +25{,}000$ |
| S2 | $9.5\% - 8.8\% = +0.7\%$ | +35,000 |
| S3 (not allowed) | $9.5\% - 8.4\% = +1.1\%$ | +55,000 |

Under every structure the assets earn more than the funds cost (profitability > cost), so the company **creates value** [Slide 5]. The chosen structure S2 creates 35,000 m.u. per year. S3 would create 55,000 m.u., so the covenant costs Meridian about 20,000 m.u. per year; that is the price of the protection the bank demands against a highly leveraged borrower [Slide 36]. If the expected return fell below 8.8%, the same assets financed with S2 would destroy value: the financing decision can turn a good investment into a bad one.

## Interpretation

- **Dimensional check:** weights and costs dimensionless; cost of capital in m.u./year.
- **Extension:** in practice interest reduces the taxes paid, so the cost of debt is often taken after tax, $K_L(1 - t)$; the course formula uses $K_L$ as given.
- **Key idea:** the optimum is not "as little debt as possible" nor "as much as possible", but the structure with the lowest weighted cost that the lenders accept.

---

**Back to:** [[Problem Set - Business Management Problem Bank]] · [[Business Management MOC]]
