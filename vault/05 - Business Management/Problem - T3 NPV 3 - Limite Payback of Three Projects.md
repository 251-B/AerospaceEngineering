---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 3, p. 1; solution in 3_II_NPV_NPV IRR_solutions.pdf, p. 2"
dificultad: easy
tags:
  - problem
  - solved
  - payback
---

# ✏️ Problem: Problem 3 — Límite, S.A.: payback of three projects

## 📄 Statement

Límite S.A. has 1,200 millions to invest in this period. Applying the criterion of recovery or payback, indicate which investment project is preferred and why.

| Project | Initial outlay | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| X | 1,200 | −200 | 300 | 500 | 200 | 400 | 400 |
| Y | 1,200 | 200 | 200 | 200 | 200 | 200 | 200 |
| Z | 1,000 | 125 | 125 | 250 | 250 | 250 | 250 |

## Data and model

Cash flows in millions, one per year. The **payback** (recovery) period is the time the cumulative cash flows take to equal the initial outlay; the shorter, the better. Within a year the flow is taken as uniform.

## Solution

### Step 1. Cumulative cash flows

| Year | X | Y | Z |
| :--- | ---: | ---: | ---: |
| 1 | −200 | 200 | 125 |
| 2 | 100 | 400 | 250 |
| 3 | 600 | 600 | 500 |
| 4 | 800 | 800 | 750 |
| 5 | **1,200** | 1,000 | **1,000** |
| 6 | 1,600 | **1,200** | 1,250 |

### Step 2. Payback periods

- X recovers its 1,200 exactly at the end of year 5: **5 years**.
- Y recovers its 1,200 at the end of year 6: **6 years**.
- Z recovers its 1,000 exactly at the end of year 5: **5 years**.

### Step 3. Choice

Y is the worst. X and Z tie at 5 years, so the payback criterion alone does not separate them. Two remarks help: Z needs 200 million less, which stays available to the company, and X has a negative flow in the first year that must be financed. Beyond year 5, X returns 400 in year 6 against 250 for Z; payback ignores those flows.

## Checks and official key

- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, p. 2): payback X = 5 years and Y = 6 years agree; the key prefers X "even if it generates negative cash flow in the first year".

> [!warning] Discrepancy with the official solution
> The key gives Z a payback of **5 years and 10 months**. With the outlay of the statement (1,000) the cumulative flow reaches 1,000 exactly at the end of year 5 (table above), so the payback is 5 years. The key's figure is what an outlay of 1,200 would give: $5 + (1{,}200 - 1{,}000)/250 = 5.8$ years, about 5 years and 10 months. With the stated data X and Z tie, and the key's preference for X is not supported by payback alone.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
