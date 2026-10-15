---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - hypereutectoid
  - lever-rule
---

# ✏️ Problem: T4-FC03 — Phases and Microconstituents of a 1.5 % C Steel

## 📄 Official Statement
> **3.- For an alloy Fe-1.5%C, at the following temperatures: $T_1$ = (1147+ΔT)ºC; $T_2$ = (1147−ΔT)ºC; $T_3$ = 900ºC; $T_4$ = (727+ΔT)ºC; $T_5$ = (727−ΔT)ºC. a) Indicate the phases present, their chemical composition and their mass fraction. b) Indicate the micro constituents, their chemical composition and their mass fraction at $T_5$.**
>
> *(Solution: a) $T_1$ and $T_2$: $C_\gamma$ = 1.5% C, $w_\gamma$ = 1; $T_3$: $C_{Fe_3C}$ = 6.7% C, $C_\gamma$ = 1.3% C, $w_\gamma$ = 0.96, $w_{Fe_3C}$ = 0.04; $T_4$: $C_\gamma$ = 0.76% C, $C_{Fe_3C}$ = 6.7% C, $w_\gamma$ = 0.87, $w_{Fe_3C}$ = 0.13; $T_5$: $C_\alpha$ = 0.022% C, $C_{Fe_3C}$ = 6.7% C, $w_\alpha$ = 0.78, $w_{Fe_3C}$ = 0.22; b) Pearlite $w_{Fe_3C'}$ = 0.13, $w_{pearlite}$ = 0.87, $w_{\alpha E}$ = 0.78, $w_{Fe_3C,E}$ = 0.09)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium cooling, Fe-Fe₃C diagram [Session 9 Slide 4].
2. $0.76 < C_0 = 1.5 < 2.14$: a **hypereutectoid steel**; at 1147 ± ΔT it is single-phase austenite (1.5 < 2.14).
3. **Reading of the figure:** at 900 °C the $A_{cm}$ line is at about 1.3 % C (the key's value; a straight line from (0.76, 727) to (2.14, 1147) would give 1.33).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C); one tie line per temperature. Below $A_{cm}$ proeutectoid cementite precipitates from the austenite [Session 9 Slide 19]; at 727 °C the remaining austenite (0.76 % C) becomes pearlite.

![[attachments/T4/fc-p3.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1$, $T_2$:** γ, 1.5 % C, $W_\gamma = 1$.

**$T_3$ = 900 °C** (γ 1.3 / Fe₃C 6.67; length 5.37):
$$W_\gamma = \frac{6.67 - 1.5}{6.67 - 1.3} = \frac{5.17}{5.37} = 0.963 \qquad W_{\text{Fe}_3\text{C}} = \frac{1.5 - 1.3}{5.37} = \frac{0.2}{5.37} = 0.037$$

**$T_4$** (γ 0.76 / Fe₃C 6.67; length 5.91):
$$W_\gamma = \frac{6.67 - 1.5}{5.91} = \frac{5.17}{5.91} = 0.875 \qquad W_{\text{Fe}_3\text{C}} = \frac{1.5 - 0.76}{5.91} = \frac{0.74}{5.91} = 0.125$$

**$T_5$** (α 0.022 / Fe₃C 6.67; length 6.648):
$$W_\alpha = \frac{6.67 - 1.5}{6.648} = \frac{5.17}{6.648} = 0.778 \qquad W_{\text{Fe}_3\text{C}} = \frac{1.5 - 0.022}{6.648} = \frac{1.478}{6.648} = 0.222$$

### b) Microconstituents at $T_5$
Proeutectoid cementite = the cementite at $T_4$, $W_{\text{Fe}_3\text{C}'} = 0.125$; pearlite = the austenite at $T_4$, $W_{\text{pearlite}} = 0.875$. Inside the pearlite: $W_{\alpha,E} = 0.778$ (all the ferrite) and $W_{\text{Fe}_3\text{C},E} = 0.222 - 0.125 = 0.097$.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- $0.778 + 0.097 = 0.875 = W_{\text{pearlite}}$; and $0.875 \times 0.889 = 0.778$ ✓.
- Mass balance at $T_5$: $0.778 \times 0.022 + 0.222 \times 6.67 = 0.017 + 1.481 = 1.50$ % C ✓.
- The proeutectoid cementite grows from 0.037 at 900 °C to 0.125 at 727 °C as the austenite loses carbon along $A_{cm}$.
- **Limiting cases** (fractions dimensionless, compositions in wt% C): at $C_0 = 0.76$ the proeutectoid Fe₃C would be 0 and at $C_0 = 6.67$ the alloy would be all Fe₃C; 1.5 % C lies near the eutectoid end, hence only 0.125 of proeutectoid cementite.

## ✅ Check against the official solution
Agrees with the key, except for the last figure.

> [!warning] Discrepancy with the official solution
> The key gives $w_{Fe_3C,E} = 0.09$. Exactly, $0.222 - 0.125 = 0.097$ (≈ 0.10), confirmed by $0.875 \times 0.111 = 0.097$; the key subtracts the rounded values, $0.22 - 0.13 = 0.09$. The computed value is kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
