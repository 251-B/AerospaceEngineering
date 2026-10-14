---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 7"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - hypoeutectic
  - ag-cu
---

# ✏️ Problem: T4-PD07 — The Hypoeutectic Ag-10 wt% Cu Alloy

## 📄 Official Statement
> **7. Using the Cu-Ag phase diagram, for an alloy with composition $C_0$ = 10% Cu, for the temperatures $T_1 = 900$ °C, $T_2 = (780 + \Delta T)$ °C, $T_3 = (780 - \Delta T)$ °C, determine: a. Present phases, chemical composition of phases and mass fraction. b. Microconstituents, chemical composition and mass fraction at $T_3$.**
>
> *(Solution: a) $T_1$: Liquid (10%Cu); $T_2$: $C_L$ = 28.1%Cu; $C_\alpha$ = 8.8%Cu; $X_\alpha = 0.94$; $X_L = 0.06$; $T_3$: $C_\alpha$ = 8.8%Cu; $C_\beta$ = 92%Cu; $X_\alpha = 0.98$; $X_\beta = 0.02$. b) eutectic microconstituent ($X_E = 0.06$) and proeutectic α ($X_{\alpha p} = 0.94$))*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling**, Ag-Cu diagram of the problem sheet (p. 2): eutectic 28.1 wt% Cu at 779.1 °C ≈ 780 °C; α = (Ag) of 8.8 and β = (Cu) of 92 wt% Cu.
2. **Reading of the figure at 900 °C:** the Ag-side liquidus falls from 961.93 °C (0 % Cu) to 779.1 °C (28.1 % Cu), and at 10 wt% Cu it is just below 900 °C, so at 900 °C the alloy is still liquid (as the official solution states).
3. $8.8 < C_0 = 10 < 28.1$: a **hypoeutectic** alloy, very close to the α limit; the primary phase is α [Session 7 Slide 30].

### Data
| Temperature | Region | Phase compositions (wt% Cu) |
| :--- | :--- | :--- |
| $T_1 = 900$ °C | L | $C_L = 10$ |
| $T_2 = 780 + \Delta T$ | α + L | $C_\alpha = 8.8$, $C_L = 28.1$ |
| $T_3 = 780 - \Delta T$ | α + β | $C_\alpha = 8.8$, $C_\beta = 92$ |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ag-Cu diagram (wt% Cu, °C), one tie line per temperature; no change of basis. Lever rule for the phases [Session 7 Slide 16] and for the microconstituents (short tie line from α to the eutectic liquid) [Session 7 Slide 32].

![[attachments/T4/pd-p7.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1 = 900$ °C.** Liquid, $C_L = 10$ wt% Cu, $W_L = 1$.

**$T_2 = 780 + \Delta T$** (tie line length $28.1 - 8.8 = 19.3$):

$$W_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} = \frac{28.1 - 10}{28.1 - 8.8} = \frac{18.1}{19.3} = 0.938 \qquad W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha} = \frac{10 - 8.8}{19.3} = \frac{1.2}{19.3} = 0.062$$

**$T_3 = 780 - \Delta T$** (length $92 - 8.8 = 83.2$):

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{92 - 10}{92 - 8.8} = \frac{82}{83.2} = 0.986 \qquad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{10 - 8.8}{83.2} = \frac{1.2}{83.2} = 0.014$$

### b) Microconstituents at $T_3$
**Proeutectic (primary) α** of 8.8 wt% Cu and **eutectic** of 28.1 wt% Cu overall:

$$W_{\alpha p} = \frac{C_e - C_0}{C_e - C_\alpha} = \frac{18.1}{19.3} = 0.938 \qquad W_E = \frac{C_0 - C_\alpha}{C_e - C_\alpha} = \frac{1.2}{19.3} = 0.062$$

**Phases inside the eutectic:**

$$W_{\alpha,E} = W_\alpha(T_3) - W_{\alpha p} = 0.986 - 0.938 = 0.048 \qquad W_{\beta,E} = W_\beta(T_3) = 0.014$$

![[attachments/T4/pd-micro-p7.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- $W_{\alpha,E} + W_{\beta,E} = 0.048 + 0.014 = 0.062 = W_E$; inside the eutectic α is $0.048/0.062 = 0.77$, as in Problem 5.
- Mass balance at $T_3$: $0.9856 \times 8.8 + 0.0144 \times 92 = 8.67 + 1.33 = 10.0$ wt% Cu.

### Interpretation
The alloy is only 1.2 wt% Cu beyond the solubility limit of α, so almost all of it is primary (Ag) and just 6 % is eutectic, found as thin films between the α grains. An alloy below 8.8 wt% Cu would form no eutectic at all.

## ✅ Check against the official solution
At $T_1$, $T_2$ and in part (b) the results agree with the key.

> [!warning] Discrepancy with the official solution
> At $T_3$ the key gives $X_\alpha = 0.98$ and $X_\beta = 0.02$. With the data of the problem, $W_\alpha = 82/83.2 = 0.9856$ and $W_\beta = 1.2/83.2 = 0.0144$, which round to 0.99 and 0.01. The computed values are kept; the key's 0.98 and 0.02 are not reproduced by any rounding of the data.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Problem - T4-PD05 The Eutectic Ag-28.1 Cu Alloy]]
* [[Problem - T4-PD06 The Hypereutectic Ag-80 Cu Alloy]]
