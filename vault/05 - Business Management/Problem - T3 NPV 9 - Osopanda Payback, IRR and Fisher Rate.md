---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 9, p. 2; solution in 3_II_NPV_NPV IRR_solutions.pdf, p. 6"
dificultad: hard
tags:
  - problem
  - solved
  - payback
  - irr
  - npv
---

# ✏️ Problem: Problem 9 — OSOPANDA, S.L.: payback, IRR and the Fisher rate

## 📄 Statement

Company OSOPANDA, S.L. is considering an investment, for which it has two offers. The first offer (Project A) has an initial payment of €16,653 and generates cash flows of €6,500 and €13,000 during the first and second years (two-year period), respectively. The second offer (Project B) means a much higher initial payment, €71,428. It will end in a year, and it is expected to generate a positive cash flow of €76,428 by the end of that year. Answer the following questions and account for your answers:

a) Which project would the company choose if it uses the payback period model?

b) Analyze both alternatives in terms of internal rate of return (IRR).

## Data and model

| Project | $I_0$ (€) | $CF_1$ (€) | $CF_2$ (€) |
| :--- | ---: | ---: | ---: |
| A | 16,653 | 6,500 | 13,000 |
| B | 71,428 | 76,428 | — |

Payback with flows spread evenly over each year (30-day months). IRR: the rate that makes $NPV = 0$. The **Fisher rate** is the discount rate at which both projects have the same NPV.

## Solution

### Step 1. Part (a): payback

A recovers 6,500 in year 1; the remaining $16{,}653 - 6{,}500 = 10{,}153$ € come from the 13,000 of year 2 after $10{,}153/13{,}000 = 0.781$ years $= 9.37$ months: **1 year, 9 months and 11 days** (0.37 × 30 days), recovered during the 12th day.

B recovers 71,428 out of 76,428 after $71{,}428/76{,}428 = 0.9346$ years $= 11.21$ months: **11 months and 6 days** (0.21 × 30), recovered during the 7th day.

B has the shorter payback, so the payback model chooses **B**.

### Step 2. Part (b): IRR of B

$$0 = -71{,}428 + \frac{76{,}428}{1 + r_B} \quad\Rightarrow\quad 1 + r_B = \frac{76{,}428}{71{,}428} = 1.0700 \quad\Rightarrow\quad r_B = 7.00\%$$

### Step 3. Part (b): IRR of A

$$0 = -16{,}653 + \frac{6{,}500}{1 + r_A} + \frac{13{,}000}{(1 + r_A)^2}$$

With $x = 1 + r_A$ and multiplying by $x^2$: $16{,}653\,x^2 - 6{,}500\,x - 13{,}000 = 0$, so

$$x = \frac{6{,}500 + \sqrt{6{,}500^2 + 4 \times 16{,}653 \times 13{,}000}}{2 \times 16{,}653} = \frac{6{,}500 + \sqrt{908{,}206{,}000}}{33{,}306} = \frac{6{,}500 + 30{,}136.46}{33{,}306} = 1.1000$$

$r_A = 10.00\%$ (the negative root has no economic meaning). By IRR, **A** is better (10% > 7%).

### Step 4. Fisher rate and the decision by the cost of capital

The two criteria disagree because the projects differ in size and duration. Setting $NPV_A(i) = NPV_B(i)$,

$$-16{,}653 + \frac{6{,}500}{1 + i} + \frac{13{,}000}{(1 + i)^2} = -71{,}428 + \frac{76{,}428}{1 + i}$$

whose root between 0 and 10% is $i \approx 5.08\%$. At $i = 0$, $NPV_A = 2{,}847$ € and $NPV_B = 5{,}000$ € (B better); at $i = 8\%$, $NPV_A = 510.92$ € and $NPV_B = -661.33$ € (A better). So:

- cost of capital below about 5.08%: choose **B** (higher NPV);
- between 5.08% and 10%: choose **A**;
- above 10%: neither project has a positive NPV.

## Checks and official key

- **Check of $r_A$:** $6{,}500/1.1 + 13{,}000/1.21 = 5{,}909.09 + 10{,}743.80 = 16{,}652.89 \approx 16{,}653$. ✓
- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, p. 6): payback A "1 year, 9 months and days (12...)" and B "11 months and 7 days", B preferred; IRR(A) ≈ 10%, IRR(B) ≈ 7%; Fisher rate ≈ 5% (0.0507); B below 5%, A between 5% and 10%, neither above 10%. Same results; the key counts the day in which the outlay is recovered (12th and 7th), which is why it gives one day more than the completed days above.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
