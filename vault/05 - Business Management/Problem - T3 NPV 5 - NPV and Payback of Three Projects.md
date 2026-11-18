---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 5, pp. 1-2; solution in 3_II_NPV_NPV IRR_solutions.pdf, p. 3"
dificultad: medium
tags:
  - problem
  - solved
  - npv
  - payback
---

# ✏️ Problem: Problem 5 — NPV and payback of three projects

## 📄 Statement

Consider these projects (cash flows in euros) and answer the questions:

| Project | C0 | C1 | C2 | C3 | C4 | C5 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | −1,000 | +1,000 | 0 | 0 | 0 | 0 |
| B | −2,000 | +1,000 | +1,000 | +4,000 | +1,000 | +1,000 |
| C | −3,000 | +1,000 | +1,000 | 0 | +1,000 | +1,000 |

a) If the interest rate is 10%, which projects have a positive NPV? b) Calculate the payback period for each project. c) Which project(s) would be accepted by a company that uses the payback period model if the maximum period is three years?

## Data and model

$NPV = \sum_{t=0}^{5} C_t/(1.10)^t$ with the discount factors $1.1^{-1} = 0.909091$, $1.1^{-2} = 0.826446$, $1.1^{-3} = 0.751315$, $1.1^{-4} = 0.683013$, $1.1^{-5} = 0.620921$. Payback: the time the cumulative flows take to recover the outlay.

## Solution

### Step 1. Part (a): NPV at 10%

$$NPV_A = -1{,}000 + 1{,}000 \times 0.909091 = -90.91 \ \text{€}$$

$$\begin{aligned} NPV_B &= -2{,}000 + 909.09 + 826.45 + 4{,}000 \times 0.751315 + 683.01 + 620.92 \\ &= -2{,}000 + 909.09 + 826.45 + 3{,}005.26 + 683.01 + 620.92 = 4{,}044.73 \ \text{€} \end{aligned}$$

$$NPV_C = -3{,}000 + 909.09 + 826.45 + 0 + 683.01 + 620.92 = 39.47 \ \text{€}$$

**B and C** have a positive NPV; A does not.

### Step 2. Part (b): payback

| Year | A cumulative | B cumulative | C cumulative |
| :--- | ---: | ---: | ---: |
| 1 | 1,000 | 1,000 | 1,000 |
| 2 | 1,000 | 2,000 | 2,000 |
| 3 | 1,000 | 6,000 | 2,000 |
| 4 | 1,000 | 7,000 | 3,000 |

A recovers its 1,000 in **1 year**, B its 2,000 in **2 years** and C its 3,000 in **4 years**.

### Step 3. Part (c): maximum payback of three years

A and B are accepted, C is rejected. The payback model accepts A although its NPV is negative and rejects C although its NPV is positive, because it ignores the time value of money and the flows after the cut-off. Between the two accepted projects, the NPV favours B.

## Checks and official key

- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, p. 3): $NPV_A = -90.91$, $NPV_B = 4{,}044.7$, $NPV_C = 39.47$; payback 1, 2 and 4 years; A and B accepted, and B chosen by NPV. Same results.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
