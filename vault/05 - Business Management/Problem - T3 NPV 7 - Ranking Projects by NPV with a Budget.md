---
materia: Business Management
tema: "Topic 3: Financial Management - Investment Selection"
origen: "3_II_NPV IRR.pdf, Problem 7, p. 2; solution in 3_II_NPV_NPV IRR_solutions.pdf, pp. 4-5"
dificultad: medium
tags:
  - problem
  - solved
  - npv
---

# ✏️ Problem: Problem 7 — Ranking projects by NPV with a budget

## 📄 Statement

You want to rank, in order of preference, according to the criterion of NPV, the investment projects with initial payments and cash flows generated in the different years of their duration, listed in the table below:

| Project | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Initial outlay |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 2,000 | 2,000 | 3,500 | 3,500 | 3,500 | 10,000 |
| B | 2,000 | 2,000 | 4,000 | 4,000 | 4,000 | 11,000 |
| C | 3,000 | 3,000 | 4,000 | 4,000 | 4,000 | 12,000 |
| D | 2,000 | 2,000 | 15,000 | — | — | 13,000 |
| E | 2,000 | 3,000 | 5,000 | 5,000 | 5,000 | 14,000 |
| F | 4,000 | 4,000 | 4,500 | 4,500 | 4,500 | 15,000 |

The required profitability is the same for all projects (10 percent). Which projects should be undertaken by an individual who has 40,000 euros to invest if they cannot be repeated?

## Data and model

Net cash flows in euros, discount rate 10% with the factors $0.909091$, $0.826446$, $0.751315$, $0.683013$, $0.620921$ for years 1 to 5. $NPV = -I_0 + \sum CF_t/1.1^t$.

## Solution

### Step 1. NPV of project A

$$NPV_A = -10{,}000 + 2{,}000\,(0.909091 + 0.826446) + 3{,}500\,(0.751315 + 0.683013 + 0.620921) = -10{,}000 + 3{,}471.07 + 7{,}193.37 = 664.45 \ \text{€}$$

### Step 2. All the projects

| Project | Outlay | Present value of the flows | NPV | Rank |
| :--- | ---: | ---: | ---: | ---: |
| A | 10,000 | 10,664.45 | 664.45 | 5 |
| B | 11,000 | 11,692.07 | 692.07 | 4 |
| C | 12,000 | 13,427.61 | 1,427.61 | 2 |
| D | 13,000 | 14,740.80 | 1,740.80 | 1 |
| E | 14,000 | 14,573.77 | 573.77 | 6 |
| F | 15,000 | 16,190.77 | 1,190.77 | 3 |

All six have a positive NPV.

### Step 3. Choice with 40,000 €

Taking the projects in order of NPV: D (13,000), then C (12,000, total 25,000), then F (15,000, total 40,000). The budget is used exactly, so the individual undertakes **D, C and F**, with a total NPV of $1{,}740.80 + 1{,}427.61 + 1{,}190.77 = 4{,}359.18$ €.

## Checks and official key

- **Check of the budget choice:** no four projects fit in 40,000 € (the four cheapest cost 46,000 €), and every other set of three that fits gives less: D + C + B (36,000 €) 3,860.48 €, D + C + E (39,000 €) 3,742.18 €, D + F + A (38,000 €) 3,596.02 €.
- **Check against the official key** (3_II_NPV_NPV IRR_solutions.pdf, pp. 4-5): NPVs 664.45, 692.07, 1,427.61, 1,740.8, 573.77 and 1,190.77 with the same ranking, and D, C and F selected. Same results.

---

**Back to:** [[Problem Set - T3 Investment Selection NPV and IRR]]
