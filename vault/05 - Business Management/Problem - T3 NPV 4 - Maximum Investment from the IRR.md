---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 4, p. 1; solution in 3_II_NPV_NPV IRR_solutions.pdf, pp. 2-3"
dificultad: easy
tags:
  - problem
  - solved
  - irr
  - npv
---

# ✏️ Problem: Problem 4 — Maximum investment from the IRR

## 📄 Statement

What is the maximum amount we should invest in a project at time 0 if the estimated annual cash inflow is €30,000 over a period of 4 years starting from year 1? Assume that the estimated internal rate of return is 8%.

## Data and model

Cash inflows $CF_1 = \dots = CF_4 = 30{,}000$ €; IRR 8%. The **net present value** of a project with outlay $I_0$ is

$$NPV = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1 + k)^t}$$

and the **internal rate of return** is the rate that makes $NPV = 0$. The maximum outlay is the one that leaves the NPV at zero when discounted at 8%: any higher outlay would give a return below 8%.

## Solution

### Step 1. NPV equal to zero at 8%

$$0 = -I_0 + \frac{30{,}000}{1.08} + \frac{30{,}000}{1.08^2} + \frac{30{,}000}{1.08^3} + \frac{30{,}000}{1.08^4}$$

### Step 2. Each discounted flow

$$\frac{30{,}000}{1.08} = 27{,}777.78 \qquad \frac{30{,}000}{1.1664} = 25{,}720.16 \qquad \frac{30{,}000}{1.259712} = 23{,}814.96 \qquad \frac{30{,}000}{1.36048896} = 22{,}050.90$$

### Step 3. Maximum outlay

$$I_0 = 27{,}777.78 + 25{,}720.16 + 23{,}814.96 + 22{,}050.90 = 99{,}363.81 \ \text{€}$$

## Checks and official key

- **Check with the annuity factor:** $30{,}000 \times \dfrac{1 - 1.08^{-4}}{0.08} = 30{,}000 \times 3.312127 = 99{,}363.81$ €. ✓
- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, pp. 2-3): $I_0 = 99{,}363.81$ €. Same result.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
