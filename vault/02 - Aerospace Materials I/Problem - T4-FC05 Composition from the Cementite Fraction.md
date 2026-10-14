---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 5"
dificultad: easy
tags:
  - official-problem
  - solved
  - fe-c-system
  - lever-rule
  - cast-iron
---

# ✏️ Problem: T4-FC05 — Composition from the Cementite Fraction

## 📄 Official Statement
> **5.- Calculate the composition of a Fe-C alloy whose composition is within the range in %C of (2.11 < $C_0$ < 4.3). Consider temperature is (727−ΔT)ºC and the mass fraction $\chi_{Fe_3C}$ is 0.38.**
>
> *(Solution: $C_0$ = 2.56%C)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium; just below 727 °C every Fe-C alloy is α (0.022 % C) + Fe₃C (6.67 % C) [Session 9 Slides 4, 9].
2. The range given (2.11-4.3 % C) is that of hypoeutectic cast irons (the diagram of the slides puts the steel limit at 2.14 %).
3. Unknown: $C_0$; one equation (lever rule for Fe₃C).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the tie line at 727 − ΔT, from 0.022 to 6.67 % C; one-dimensional, no change of basis. The lever rule is solved for the alloy composition instead of the fraction [Session 7 Slide 16].

![[attachments/T4/fc-p5.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

$$W_{\text{Fe}_3\text{C}} = \frac{C_0 - C_\alpha}{C_{\text{Fe}_3\text{C}} - C_\alpha} \;\Rightarrow\; C_0 = C_\alpha + W_{\text{Fe}_3\text{C}}\,(C_{\text{Fe}_3\text{C}} - C_\alpha)$$
$$C_0 = 0.022 + 0.38 \times (6.67 - 0.022) = 0.022 + 0.38 \times 6.648 = 0.022 + 2.526 = 2.55\ \%\,\text{C}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Check: $(2.548 - 0.022)/6.648 = 0.380$ ✓; and $2.11 < 2.55 < 4.3$, inside the given range ✓.
- Units: percentages of C on both sides; $W$ dimensionless.
- The alloy is a hypoeutectic cast iron: it would contain primary austenite and ledeburite just below 1147 °C.

## ✅ Check against the official solution

> [!warning] Discrepancy with the official solution
> The key gives $C_0 = 2.56$ % C, which follows from 6.7 % C for cementite: $0.022 + 0.38 \times 6.678 = 2.56$. With the 6.67 % C of the slides the result is 2.55 % C; the difference is only that rounding.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Tie Line and Lever Rule]]
* [[Problem - T4-FC10 Fe-Cementite Questions and Pearlite Limits]]
