---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 1, p. 1; solution in 3_II_NPV_NPV IRR_solutions.pdf, p. 1"
dificultad: easy
tags:
  - problem
  - solved
  - capitalization
---

# ✏️ Problem: Problem 1 — Capitalization of a deferred debt

## 📄 Statement

One person, Mr. Smith, is able to invest his available liquid capital at a 5 percent rate per year. Currently, another person, Mr. Martinez, must pay Mr. Smith the amount of USD 1,000, but he is going through a period of scarce liquidity and asks him to wait. How much money will Mr. Smith require if it is delayed a year? What if it is a two-year delay? What if it were three years of deferment?

## Data and model

| Symbol | Meaning | Value |
| :--- | :--- | ---: |
| $C_0$ | debt today | 1,000 |
| $i$ | rate at which Mr. Smith can invest | 5% per year |
| $n$ | years of delay | 1, 2, 3 |

Mr. Smith must receive the amount that, invested at 5%, equals having the 1,000 today: the future (capitalized) value with compound interest,

$$C_n = C_0\,(1 + i)^n$$

This is the capitalization rule used in the key; the course decks on disk do not state it.

## Solution

### Step 1. One, two and three years

$$\begin{aligned} C_1 &= 1{,}000 \times 1.05 = 1{,}050 \\ C_2 &= 1{,}000 \times 1.05^2 = 1{,}000 \times 1.1025 = 1{,}102.50 \\ C_3 &= 1{,}000 \times 1.05^3 = 1{,}000 \times 1.157625 = 1{,}157.63 \end{aligned}$$

Each year the interest is earned on the previous year's balance, so the yearly increase grows: 50, then 52.50, then 55.13.

## Checks and official key

- **Check:** $C_3 = C_2 \times 1.05 = 1{,}102.50 \times 1.05 = 1{,}157.63$. ✓
- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, p. 1): 1,050, 1,102.5 and 1,157.62. Same results ($1{,}157.625$ is truncated to 1,157.62 in the key and rounded to 1,157.63 here).

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
