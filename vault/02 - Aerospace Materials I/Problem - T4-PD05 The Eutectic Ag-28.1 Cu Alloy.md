---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 5"
dificultad: easy
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - ag-cu
---

# ✏️ Problem: T4-PD05 — The Eutectic Ag-28.1 wt% Cu Alloy

## 📄 Official Statement
> **5. Given an alloy Ag-28.1%Cu, indicate for the given temperatures, $T_1 = 900$ °C; $T_2 = (780 + \Delta T)$ °C; $T_3 = (780 - \Delta T)$ °C: a. Present phases, chemical composition of phases and mass fraction. b. Microconstituents, chemical composition and mass fraction at $T_3$.**
>
> *(Solution: a) $T_1$: Liquid (28.1%Cu); $T_2$: Liquid (28.1%Cu); $T_3$: $\alpha$($C_\alpha$ = 8.8%Cu) + $\beta$($C_\beta$ = 92%Cu); $x_\alpha = 0.77$; $x_\beta = 0.23$. b) Eutectic microconstituent (28.1%Cu); $C_{\alpha E}$ = 8.8%Cu; $C_{\beta E}$ = 92%Cu)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling** with the Ag-Cu diagram of the problem sheet (p. 2): eutectic at 28.1 wt% Cu and 779.1 °C (the statement rounds it to 780 °C); at that temperature (Ag) = α contains 8.8 wt% Cu and (Cu) = β contains 92 wt% Cu. Melting points: 961.93 °C (Ag) and 1084.87 °C (Cu).
2. $C_0 = 28.1$ wt% Cu is exactly the **eutectic composition** [Session 7 Slides 26-27].

### Data
| Quantity | Value |
| :--- | ---: |
| $C_0$ | 28.1 wt% Cu |
| $C_\alpha$, $C_e$, $C_\beta$ at the eutectic temperature | 8.8, 28.1, 92 wt% Cu |
| Eutectic temperature | 779.1 °C ≈ 780 °C |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ag-Cu diagram (wt% Cu, °C), one horizontal tie line per temperature; no change of basis is needed.

**Why no lever rule above 780 °C.** The eutectic liquid meets both liquidus lines at their lowest point, so it never enters a two-phase L + solid region: it stays liquid down to the eutectic temperature and then transforms at once, $L \rightarrow \alpha + \beta$ [Session 7 Slide 27].

![[attachments/T4/pd-p5.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1 = 900$ °C.** Above the liquidus: liquid, $C_L = 28.1$ wt% Cu, $W_L = 1$.

**$T_2 = 780 + \Delta T$.** Still above the eutectic point: liquid, $C_L = 28.1$ wt% Cu, $W_L = 1$.

**$T_3 = 780 - \Delta T$.** α + β; tie line from 8.8 to 92 (length $92 - 8.8 = 83.2$):

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{92 - 28.1}{92 - 8.8} = \frac{63.9}{83.2} = 0.768 \qquad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{28.1 - 8.8}{83.2} = \frac{19.3}{83.2} = 0.232$$

### b) Microconstituents at $T_3$
All the liquid of $T_2$ became eutectic: **one microconstituent, the eutectic**, $W_E = 1$, with overall composition 28.1 wt% Cu. Inside it: α (8.8 wt% Cu) with mass fraction 0.768 and β (92 wt% Cu) with mass fraction 0.232.

![[attachments/T4/pd-micro-p5.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- $W_\alpha + W_\beta = 0.768 + 0.232 = 1$.
- Mass balance: $0.768 \times 8.8 + 0.232 \times 92 = 6.76 + 21.34 = 28.1$ wt% Cu $= C_0$.
- Phase rule at the eutectic point (1 atm): $F = 2 - 3 + 1 = 0$, so the transformation happens at one temperature, with a plateau in the cooling curve, like a pure metal [Session 7 Slide 27].
- **Limiting case** (fractions dimensionless, compositions in wt% Cu): the alloy sits exactly at the eutectic composition, so the primary fraction $(C_0 - C_e)/(C_\beta - C_e)$ (or its hypoeutectic twin) is 0: the end case of both formulas, an alloy that is all eutectic.

### Interpretation
The eutectic alloy has the lowest melting point of the system (779 °C, well below 961.93 °C for Ag and 1084.87 °C for Cu) and solidifies at a single temperature into a fine layered mixture of a Ag-rich and a Cu-rich solid.

## ✅ Check against the official solution
Agrees with the key: $x_\alpha = 0.77$, $x_\beta = 0.23$; 100 % eutectic. The official solutions PDF has no worked page for this problem.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Problem - T4-PD06 The Hypereutectic Ag-80 Cu Alloy]]
* [[Problem - T4-PD07 The Hypoeutectic Ag-10 Cu Alloy]]
