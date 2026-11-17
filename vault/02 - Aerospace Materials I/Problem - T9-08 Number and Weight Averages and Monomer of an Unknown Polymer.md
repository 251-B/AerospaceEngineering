---
materia: "Aerospace Materials I"
tema: "Topic 9: Polymers"
origen: "Problems T9_Polymers.pdf, Problem 8"
dificultad: medium
badge: "Mn and Mw · monomer identification · nylon 6,6"
tags:
  - official-problem
  - solved
  - molecular-weight
  - degree-of-polymerization
  - nylon
---

# ✏️ Problem: T9-08 — Number and Weight Averages and Monomer of an Unknown Polymer

## 📄 Official Statement
> 8. A polymer sample with unknown molecular weight has been analyzed and the following results were obtained.
> a) Calculate the number-average and weight-average molecular weight.
> b) If the number average degree of polymerization is 211, calculate the molecular weight of the monomeric unit.
> c) Which of these polymers correspond to: PE, PVC, PTFE, PP, PS, PMMA, Nylon 66, PC.
> d) What is the weight-average degree of polymerization?
>
> ![[attachments/T9/t9-p8-number-weight-fraction-table.png]]
>
> *(Solution: a) Mn = 47720, Mw = 53720; b) M0 = 226.2; c) Nylon 66; d) Xw = 238)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Mean of each range.** Each range is represented by its midpoint $M_i$ [Session 19 Slides 14-15].
2. **Averages.** $M_n = \sum x_i M_i$, $M_w = \sum w_i M_i$ [Session 19 Slide 13], and $X_n = M_n/M_0$ [Session 19 Slide 12].
3. **Weight-average degree of polymerization.** By analogy with $X_n$, $X_w = M_w/M_0$ (this definition is an extension; the slides define only $X_n$).
4. **Repeat units of the candidates.** From Session 19 Slide 50 and Session 20 Slides 8-9: PE $\mathrm{C_2H_4}$, PVC $\mathrm{C_2H_3Cl}$, PTFE $\mathrm{C_2F_4}$, PP $\mathrm{C_3H_6}$, PS $\mathrm{C_8H_8}$, PMMA $\mathrm{C_5H_8O_2}$, nylon 6,6 $\mathrm{-[NH{-}(CH_2)_6{-}NH{-}CO{-}(CH_2)_4{-}CO]-}$ = $\mathrm{C_{12}H_{22}N_2O_2}$, and polycarbonate $\mathrm{-[O{-}CO{-}O{-}C_6H_4{-}C(CH_3)_2{-}C_6H_4]-}$ = $\mathrm{C_{16}H_{14}O_3}$. Atomic masses C = 12, H = 1, N = 14, O = 16, F = 19, Cl = 35.5 g/mol (the sheet gives none for this problem; standard values).

### Data
| Range (g/mol) | Midpoint $M_i$ (g/mol) | $x_i$ | $w_i$ |
| :--- | ---: | ---: | ---: |
| 8 000 – 20 000 | 14 000 | 0.05 | 0.02 |
| 20 000 – 32 000 | 26 000 | 0.15 | 0.08 |
| 32 000 – 44 000 | 38 000 | 0.21 | 0.17 |
| 44 000 – 56 000 | 50 000 | 0.28 | 0.29 |
| 56 000 – 68 000 | 62 000 | 0.18 | 0.23 |
| 68 000 – 80 000 | 74 000 | 0.10 | 0.16 |
| 80 000 – 92 000 | 86 000 | 0.03 | 0.05 |

$\sum x_i = 1.00$ and $\sum w_i = 1.00$. Also $X_n = 211$.

**Unknowns:** (a) $M_n$ and $M_w$; (b) $M_0$; (c) the polymer; (d) $X_w$.

---

## 🧠 2. Model and Strategy

[Session 19 Slides 12-13]:

$$M_n = \sum x_i M_i \qquad M_w = \sum w_i M_i \qquad M_0 = \frac{M_n}{X_n}$$

**Strategy.**
1. Compute the two weighted sums.
2. Divide $M_n$ by $X_n$ to get the molecular weight of the repeat unit.
3. Compute $M_0$ of every candidate and pick the one that matches.
4. Divide $M_w$ by $M_0$.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Number-average and weight-average molecular weights [Session 19 Slide 13]
| $M_i$ (g/mol) | $x_i M_i$ (g/mol) | $w_i M_i$ (g/mol) |
| ---: | ---: | ---: |
| 14 000 | 700 | 280 |
| 26 000 | 3 900 | 2 080 |
| 38 000 | 7 980 | 6 460 |
| 50 000 | 14 000 | 14 500 |
| 62 000 | 11 160 | 14 260 |
| 74 000 | 7 400 | 11 840 |
| 86 000 | 2 580 | 4 300 |

$$M_n = 700 + 3900 + 7980 + 14000 + 11160 + 7400 + 2580 = \mathbf{47\,720\ g/mol}$$

$$M_w = 280 + 2080 + 6460 + 14500 + 14260 + 11840 + 4300 = \mathbf{53\,720\ g/mol}$$

### 2. b) Molecular weight of the monomeric unit [Session 19 Slide 12]
$$M_0 = \frac{M_n}{X_n} = \frac{47\,720\ \text{g/mol}}{211} = \mathbf{226.2\ g/mol}$$

### 3. c) Identification of the polymer
| Polymer | Repeat unit | $M_0$ (g/mol) |
| :--- | :--- | ---: |
| PE | $\mathrm{C_2H_4}$: $2(12) + 4(1)$ | 28 |
| PVC | $\mathrm{C_2H_3Cl}$: $2(12) + 3(1) + 35.5$ | 62.5 |
| PTFE | $\mathrm{C_2F_4}$: $2(12) + 4(19)$ | 100 |
| PP | $\mathrm{C_3H_6}$: $3(12) + 6(1)$ | 42 |
| PS | $\mathrm{C_8H_8}$: $8(12) + 8(1)$ | 104 |
| PMMA | $\mathrm{C_5H_8O_2}$: $5(12) + 8(1) + 2(16)$ | 100 |
| Nylon 6,6 | $\mathrm{C_{12}H_{22}N_2O_2}$: $12(12) + 22(1) + 2(14) + 2(16)$ | 226 |
| PC | $\mathrm{C_{16}H_{14}O_3}$: $16(12) + 14(1) + 3(16)$ | 254 |

For nylon 6,6 the count is: carbon $6 + 1 + 4 + 1 = 12$ (the two $(\mathrm{CH_2})$ blocks and the two C=O); hydrogen $1 + 12 + 1 + 8 = 22$ (the two N-H and the ten $\mathrm{CH_2}$); 2 N; 2 O. Only nylon 6,6 has $M_0$ close to 226.2 g/mol.

**Answer: nylon 6,6.**

### 4. d) Weight-average degree of polymerization
$$X_w = \frac{M_w}{M_0} = \frac{53\,720\ \text{g/mol}}{226.16\ \text{g/mol}} = 237.5 \approx \mathbf{238}$$

(with the rounded $M_0 = 226$ g/mol of nylon 6,6, $X_w = 237.7$, also 238).

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $x_i$ and $w_i$ are dimensionless, so $M_n$ and $M_w$ are in g/mol; $X_n$ and $X_w$ are pure numbers.
- **$M_w \ge M_n$.** $53\,720 > 47\,720$ g/mol; the index of polydispersion is $I = 53\,720/47\,720 = 1.126$, a narrow distribution.
- **Consistency of the two columns (extension).** The weight fraction of a range follows from its number fraction as $w_i = x_i M_i/M_n$: for 44 000 – 56 000 g/mol, $0.28\times50\,000/47\,720 = 0.293$, against 0.29 in the table. Computed in the same way from the $x_i$, $M_w = \sum x_i M_i^2/\sum x_i M_i = 53\,978$ g/mol, 0.5 % above the 53 720 g/mol of the $w_i$ column, so the two columns describe the same sample within the rounding of the table.
- **Second candidate.** The closest other candidate, polycarbonate (254 g/mol), would need $X_n = 47\,720/254 = 188$, not 211.

### Interpretation
The sample is a nylon 6,6 with about 211 repeat units per chain on a number basis and 238 on a weight basis; the weight average is larger because the long chains carry more of the mass. Nylon 6,6 is the polyamide used for fibres (Session 19 Slide 50) and an engineering thermoplastic with a melting point of 250 – 266 °C (Session 20 Slide 9), the result of its polar amide groups that form hydrogen bonds between chains (Session 19 Slide 26).

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $M_n$ | 47 720 | 47 720 g/mol | agrees |
| a) $M_w$ | 53 720 | 53 720 g/mol | agrees |
| b) $M_0$ | 226.2 | 226.16 g/mol | agrees |
| c) Polymer | Nylon 66 | nylon 6,6 | agrees |
| d) $X_w$ | 238 | 237.5 | agrees after rounding |

## 🔗 Related Links
* [[Topic 9 - Polymers]]
* [[Problem - T9-07 Weight Average Polydispersity and Repeat Unit of a Polyalkene|Problem T9-07]]
