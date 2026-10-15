---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 7"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - cast-iron
  - ledeburite
---

# ✏️ Problem: T4-FC07 — Hypereutectic Cast Iron from its Cementite Fraction

## 📄 Official Statement
> **7.- Consider an alloy of Fe-C, with content of C > 4.3%C at (727−ΔT)ºC. In these conditions, $\chi_{Fe_3C}$ = 0.73. Indicate the mass fraction of the phases at (1147+ΔT)ºC and (1147−ΔT)ºC.**
>
> *(Solution: T1: $w_L$ = 0.75, $w_{Fe_3C}$ = 0.25; T2: $w_\gamma$ = 0.39, $w_{Fe_3C}$ = 0.61, $w_{(Fe_3C)p}$ = 0.25, $w_E$ = 0.75, $w_{\gamma E}$ = 0.39, $w_{(Fe_3C)E}$ = 0.36)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium, Fe-Fe₃C diagram [Session 9 Slide 4].
2. $C_0 > 4.3$: a **hypereutectic cast iron**; the primary phase is cementite, which forms in L + Fe₃C above 1147 °C.
3. Unknown first: $C_0$ from the cementite fraction just below 727 °C.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C). Tie lines: 727 − ΔT (α 0.022 / Fe₃C 6.67), 1147 + ΔT (L 4.30 / Fe₃C 6.67), 1147 − ΔT (γ 2.14 / Fe₃C 6.67). Lever rule each time [Session 7 Slides 16, 32].

![[attachments/T4/fc-p7.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Composition
$$C_0 = C_\alpha + W_{\text{Fe}_3\text{C}}\,(C_{\text{Fe}_3\text{C}} - C_\alpha) = 0.022 + 0.73 \times 6.648 = 0.022 + 4.853 = 4.875\ \%\,\text{C}$$

### 2. $T_1$ = 1147 + ΔT (length $6.67 - 4.30 = 2.37$)
$$W_L = \frac{6.67 - 4.875}{2.37} = \frac{1.795}{2.37} = 0.757 \qquad W_{\text{Fe}_3\text{C}} = \frac{4.875 - 4.30}{2.37} = \frac{0.575}{2.37} = 0.243$$

### 3. $T_2$ = 1147 − ΔT (length $6.67 - 2.14 = 4.53$)
$$W_\gamma = \frac{6.67 - 4.875}{4.53} = \frac{1.795}{4.53} = 0.396 \qquad W_{\text{Fe}_3\text{C}} = \frac{4.875 - 2.14}{4.53} = \frac{2.735}{4.53} = 0.604$$

**Microconstituents at $T_2$:** primary cementite = 0.243; ledeburite = 0.757, made of γ 0.396 and Fe₃C $0.604 - 0.243 = 0.361$.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Ledeburite make-up: $0.396/0.757 = 0.523$ γ ✓ (Worked example 14).
- Mass balance at $T_1$: $0.757 \times 4.30 + 0.243 \times 6.67 = 3.26 + 1.62 = 4.875$ % C ✓.
- **Limiting cases** (fractions dimensionless, compositions in wt% C): at $C_0 = 4.30$ the primary Fe₃C would be 0 and at $C_0 = 6.67$ the alloy would be all Fe₃C; 4.875 % C lies near the eutectic end, hence 0.243 of primary Fe₃C.

## ✅ Check against the official solution
Agrees with the key in the eutectic Fe₃C, 0.361 (key 0.36). The key does not give $C_0$; it is 4.875 % C (4.90 % with 6.7 % C for cementite: $0.022 + 0.73 \times 6.678 = 4.897$).

> [!warning] Discrepancy with the official solution
> Four values differ from the key by 0.01: 0.757/0.243 (key 0.75/0.25) and 0.396/0.604 (key 0.39/0.61). The key works with $C_0$ rounded to 4.9 % and 6.7 % C for cementite: $(6.7 - 4.9)/2.4 = 0.75$, $(4.9 - 4.3)/2.4 = 0.25$, $(6.7 - 4.9)/4.56 = 0.395 \to 0.39$ and $0.605 \to 0.61$. With the slides' 6.67 % C and the unrounded $C_0$ the values above follow; they are kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Problem - T4-FC06 Hypoeutectic Cast Iron from its Ferrite Fraction]]
