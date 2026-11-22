---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 6, p. 2; solution in 3_II_NPV_NPV IRR_solutions.pdf, pp. 3-4"
dificultad: medium
tags:
  - problem
  - solved
  - npv
  - irr
---

# ✏️ Problem: Problem 6 — NPV from a known IRR

## 📄 Statement

Assuming an interest rate of 7%, consider a three-year investment period generating a positive cash flow of €10,000 per year with an internal rate of return of 10%. Calculate the NPV of this investment.

## Data and model

$CF_1 = CF_2 = CF_3 = 10{,}000$ €, IRR 10%, discount rate $k = 7\%$. The outlay $I_0$ is not given: it follows from the IRR, the rate at which the NPV is zero. Then the NPV is computed at 7%.

## Solution

### Step 1. Outlay from the IRR

$$0 = -I_0 + \frac{10{,}000}{1.1} + \frac{10{,}000}{1.1^2} + \frac{10{,}000}{1.1^3} = -I_0 + 9{,}090.91 + 8{,}264.46 + 7{,}513.15$$

$$I_0 = 24{,}868.52 \ \text{€}$$

### Step 2. NPV at 7%

$$NPV = -24{,}868.52 + \frac{10{,}000}{1.07} + \frac{10{,}000}{1.1449} + \frac{10{,}000}{1.225043} = -24{,}868.52 + 9{,}345.79 + 8{,}734.39 + 8{,}162.98 = 1{,}374.64 \ \text{€}$$

The NPV is positive because the discount rate (7%) is below the IRR (10%).

## Checks and official key

- **Check:** at $k = $ IRR the NPV would be zero; a lower rate gives a positive NPV, as found.
- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, pp. 3-4): $I_0 = 24{,}868$ € and $NPV = 1{,}375$ €. Same results. The key also adds a part (b), not in the statement: at $k = 9\%$ the NPV is smaller but still positive, since $9\% < 10\%$; its value is $1{,}374.64 - 930.21 = 444.43$ €.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
