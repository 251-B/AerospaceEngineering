---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 4"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - cast-iron
  - ledeburite
---

# ✏️ Problem: T4-FC04 — Phases and Microconstituents of a Eutectic Cast Iron

## 📄 Official Statement
> **4.- For an alloy Fe-4.3% of C, at the following temperatures: $T_1$ = 1147 + ΔT ºC; $T_2$ = 1147 − ΔT ºC; $T_3$ = 900 ºC; $T_4$ = 727 + ΔT ºC; $T_5$ = 727 − ΔT ºC. a) Indicate the phases present, their chemical composition and their mass fractions. b) Indicate the micro constituents, their chemical composition and their mass fractions.**
>
> *(Solutions; the phase symbols print as empty boxes in the PDF and are restored from context: a) $T_1$: $C_L$ = 4.3% C, $w_L$ = 1; $T_2$: $C_{Fe_3C}$ = 6.7% C, $C_\gamma$ = 2.14% C, $w_\gamma$ = 0.53; $T_3$: $C_\gamma$ = 1.3% C, $C_{Fe_3C}$ = 6.7% C, $w_\gamma$ = 0.44; $T_4$: $C_\gamma$ = 0.76% C, $C_{Fe_3C}$ = 6.7% C, $w_\gamma$ = 0.40; $T_5$: $C_\alpha$ = 0.022% C, $C_{Fe_3C}$ = 6.7% C, $w_\alpha$ = 0.36; b) At $T_2$: $w_{Fe_3C,E}$ 0.47, $w_{\gamma,E}$ 0.53)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium cooling, Fe-Fe₃C diagram [Session 9 Slide 4]; $C_0 = 4.3$ % C is the **eutectic composition**: the alloy is liquid down to 1147 °C and then becomes 100 % **ledeburite**, $L \rightarrow \gamma\,(2.14) + \text{Fe}_3\text{C}\,(6.67)$ [Session 9 Slide 10].
2. **Reading of the figure:** $A_{cm}$ at 900 °C ≈ 1.3 % C (as in Problem FC03).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C); one tie line per temperature. Below 1147 °C the alloy stays in γ + Fe₃C, and the γ of the ledeburite loses carbon along $A_{cm}$ (more cementite precipitates), until at 727 °C it becomes pearlite ("transformed ledeburite", Session 9 Slide 11).

![[attachments/T4/fc-p4.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1$:** liquid, 4.3 % C, $W_L = 1$.

**$T_2$** (γ 2.14 / Fe₃C 6.67; length 4.53):
$$W_\gamma = \frac{6.67 - 4.3}{4.53} = \frac{2.37}{4.53} = 0.523 \qquad W_{\text{Fe}_3\text{C}} = \frac{4.3 - 2.14}{4.53} = \frac{2.16}{4.53} = 0.477$$

**$T_3$** (γ 1.3 / Fe₃C 6.67; length 5.37):
$$W_\gamma = \frac{6.67 - 4.3}{5.37} = \frac{2.37}{5.37} = 0.441 \qquad W_{\text{Fe}_3\text{C}} = 1 - W_\gamma = 1 - 0.441 = 0.559$$

**$T_4$** (γ 0.76 / Fe₃C 6.67; length 5.91):
$$W_\gamma = \frac{6.67 - 4.3}{6.67 - 0.76} = \frac{2.37}{5.91} = 0.401 \qquad W_{\text{Fe}_3\text{C}} = 1 - 0.401 = 0.599$$

**$T_5$** (α 0.022 / Fe₃C 6.67; length 6.648):
$$W_\alpha = \frac{6.67 - 4.3}{6.67 - 0.022} = \frac{2.37}{6.648} = 0.356 \qquad W_{\text{Fe}_3\text{C}} = 1 - 0.356 = 0.644$$

### b) Microconstituents
- $T_1$: liquid.
- $T_2$: 100 % **ledeburite** (4.3 % C overall), made of $W_{\gamma,E} = 0.523$ and $W_{\text{Fe}_3\text{C},E} = 0.477$ (Worked example 14 of the theory).
- $T_3$, $T_4$: ledeburite whose austenite has rejected cementite: γ + Fe₃C in the amounts of part (a).
- $T_5$: **transformed ledeburite**: the 0.401 of austenite at $T_4$ has become pearlite, inside a cementite matrix (0.599).

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Mass balance at $T_2$: $0.523 \times 2.14 + 0.477 \times 6.67 = 1.12 + 3.18 = 4.30$ % C ✓.
- The amount of cementite only grows on cooling (0.477 → 0.559 → 0.599 → 0.644), because the solubility of C in the iron phase only falls.
- **Limiting case** (fractions dimensionless, compositions in wt% C): at exactly 4.30 % C the primary fraction is 0 on both sides of the eutectic: the alloy is all ledeburite at $T_2$.

## ✅ Check against the official solution
Agrees with the key at $T_3$, $T_4$ and $T_5$.

> [!warning] Discrepancy with the official solution
> At $T_2$ the key gives $w_\gamma = 0.53$. With 6.67 % C for cementite (the value of the slides), $w_\gamma = 2.37/4.53 = 0.523$ (0.52); the key's 0.53 follows from 6.7 % C, $2.4/4.56 = 0.526$. The same gap appears in part (b): the ledeburite is $W_{\gamma,E} = 0.523$ and $W_{\text{Fe}_3\text{C},E} = 0.477$ (0.52/0.48), against the key's 0.53/0.47. The difference is only the rounding of the cementite composition (the sheet's diagram ends at 6.7 % C); 0.523 and 0.477 are kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
