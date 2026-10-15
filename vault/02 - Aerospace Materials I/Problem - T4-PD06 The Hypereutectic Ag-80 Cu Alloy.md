---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 6"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - hypereutectic
  - ag-cu
---

# ✏️ Problem: T4-PD06 — The Hypereutectic Ag-80 wt% Cu Alloy

## 📄 Official Statement
> **6. Using the Cu-Ag phase diagram, for an alloy with composition $C_0$ = 80% Cu, for temperatures $T_1 = 900$ °C; $T_2 = (780 + \Delta T)$ °C; $T_3 = (780 - \Delta T)$ °C, determine: a. Present phases, chemical composition of phases and mass fraction. b. Microconstituents, chemical composition and mass fraction at $T_3$.**
>
> *(Solution: a) $T_1$: $C_L$ = 58%Cu; $C_\beta$ = 93%Cu; $X_L = 0.37$; $X_\beta = 0.63$; $T_2$: $C_L$ = 28.1%Cu; $C_\beta$ = 92%Cu; $X_L = 0.19$; $X_\beta = 0.81$; $T_3$: $C_\alpha$ = 8.8%Cu; $C_\beta$ = 92%Cu; $X_\alpha = 0.14$; $X_\beta = 0.86$. b) eutectic microconstituent ($X_E = 0.19$) and proeutectic β ($X_{\beta p} = 0.81$))*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling**, Ag-Cu diagram of the problem sheet (p. 2): eutectic 28.1 wt% Cu at 779.1 °C ≈ 780 °C; α = (Ag) of 8.8 and β = (Cu) of 92 wt% Cu at that temperature.
2. **Reading of the figure at 900 °C:** the tie line meets the Cu-side liquidus at 58 wt% Cu and the (Cu) solidus at 93 wt% Cu (the readings of the official solution).
3. $28.1 < C_0 = 80 < 92$: a **hypereutectic** alloy, primary phase β [Session 7 Slide 31].

### Data
| Temperature | Region | Phase compositions (wt% Cu) |
| :--- | :--- | :--- |
| $T_1 = 900$ °C | L + β | $C_L = 58$, $C_\beta = 93$ |
| $T_2 = 780 + \Delta T$ | L + β | $C_L = 28.1$, $C_\beta = 92$ |
| $T_3 = 780 - \Delta T$ | α + β | $C_\alpha = 8.8$, $C_\beta = 92$ |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Ag-Cu diagram (wt% Cu, °C), one tie line per temperature; no change of basis. Lever rule for phases [Session 7 Slide 16]; short tie line (eutectic liquid to β) for the microconstituents [Session 7 Slide 32].

![[attachments/T4/pd-p6.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1 = 900$ °C** (tie line length $93 - 58 = 35$):

$$W_L = \frac{C_\beta - C_0}{C_\beta - C_L} = \frac{93 - 80}{93 - 58} = \frac{13}{35} = 0.371 \qquad W_\beta = \frac{C_0 - C_L}{C_\beta - C_L} = \frac{80 - 58}{35} = \frac{22}{35} = 0.629$$

**$T_2 = 780 + \Delta T$** (length $92 - 28.1 = 63.9$):

$$W_L = \frac{92 - 80}{92 - 28.1} = \frac{12}{63.9} = 0.188 \qquad W_\beta = \frac{80 - 28.1}{63.9} = \frac{51.9}{63.9} = 0.812$$

**$T_3 = 780 - \Delta T$** (length $92 - 8.8 = 83.2$):

$$W_\alpha = \frac{92 - 80}{92 - 8.8} = \frac{12}{83.2} = 0.144 \qquad W_\beta = \frac{80 - 8.8}{83.2} = \frac{71.2}{83.2} = 0.856$$

### b) Microconstituents at $T_3$
**Proeutectic (primary) β** of 92 wt% Cu, and **eutectic** of 28.1 wt% Cu overall:

$$W_{\beta p} = \frac{C_0 - C_e}{C_\beta - C_e} = \frac{80 - 28.1}{92 - 28.1} = \frac{51.9}{63.9} = 0.812 \qquad W_E = \frac{C_\beta - C_0}{C_\beta - C_e} = \frac{12}{63.9} = 0.188$$

**Phases inside the eutectic:**

$$W_{\beta,E} = W_\beta(T_3) - W_{\beta p} = 0.856 - 0.812 = 0.044 \qquad W_{\alpha,E} = W_\alpha(T_3) = 0.144$$

![[attachments/T4/pd-micro-p6.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- $W_{\alpha,E} + W_{\beta,E} = 0.144 + 0.044 = 0.188 = W_E$.
- Inside the eutectic α is $0.1442 / 0.1878 = 0.768$, the make-up of the eutectic alloy of Problem 5.
- Mass balance at $T_3$: $0.1442 \times 8.8 + 0.8558 \times 92 = 1.27 + 78.73 = 80.0$ wt% Cu.
- **Limiting cases** (fractions dimensionless, compositions in wt% Cu): at $C_0 = 28.1$ the alloy would be all eutectic and at $C_0 = 92$ all primary β; 80 wt% Cu lies close to the β end, hence 0.81 of primary β.

### Interpretation
Between 900 °C and the eutectic temperature the amount of primary (Cu) grows from 63 % to 81 %, and the liquid becomes poorer in Cu, from 58 to 28.1 wt%. The final structure is mostly primary (Cu) crystals with about 19 % eutectic between them.

## ✅ Check against the official solution
All values agree with the key. The worked page (Solution problems Phase diagrams I.pdf, pp. 11-12) adds a fourth temperature, $T_4 = 500$ °C, that is not in the statement of the sheet, and writes $\chi_{Cu,E} = 0.86 - 0.81 = 0.04$ (exactly $0.856 - 0.812 = 0.044$).

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Problem - T4-PD05 The Eutectic Ag-28.1 Cu Alloy]]
* [[Problem - T4-PD07 The Hypoeutectic Ag-10 Cu Alloy]]
