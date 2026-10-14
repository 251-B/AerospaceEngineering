---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 2"
dificultad: easy
tags:
  - official-problem
  - solved
  - fe-c-system
  - eutectoid
  - pearlite
---

# ✏️ Problem: T4-FC02 — Phases and Microconstituents of a Eutectoid Steel

## 📄 Official Statement
> **2.- For a steel of $C_0$ = 0.76%C, at the following temperatures: $T_1$ = (1147+ΔT)ºC; $T_2$ = (1147−ΔT)ºC; $T_3$ = 900ºC; $T_4$ = (727+ΔT)ºC; $T_5$ = (727−ΔT)ºC. a) Indicate the phases present, their chemical composition and their mass fraction. b) Indicate the micro constituents, their chemical composition and their mass fraction at $T_5$.**
>
> *(Solution: a) $T_1$, $T_2$, $T_3$ and $T_4$: $C_\gamma$ = 0.76% C, $w_\gamma$ = 1; $T_5$: $C_\alpha$ = 0.022% C, $C_{Fe_3C}$ = 6.7% C, $w_\alpha$ = 0.89, $w_{Fe_3C'}$ = 0.11; b) pearlite $w_{\alpha,E}$ = 0.89, $w_{Fe_3C,E}$ = 0.11)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium cooling on the Fe-Fe₃C diagram: α 0.022, eutectoid 0.76 % C at 727 °C, Fe₃C 6.67 % C [Session 9 Slide 4].
2. $C_0 = 0.76$ % C is the **eutectoid composition** [Session 9 Slide 12]: the alloy is austenite down to 727 °C (it touches the eutectoid point only there).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C), one tie line per temperature; no change of basis. The eutectoid reaction $\gamma\,(0.76) \rightarrow \alpha\,(0.022) + \text{Fe}_3\text{C}\,(6.67)$ turns all the austenite into pearlite at once [Session 9 Slide 10].

![[attachments/T4/fc-p2.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1$ to $T_4$:** austenite, $C_\gamma = 0.76$ % C, $W_\gamma = 1$.

**$T_5$** (length $6.67 - 0.022 = 6.648$):
$$W_\alpha = \frac{6.67 - 0.76}{6.648} = \frac{5.91}{6.648} = 0.889 \qquad W_{\text{Fe}_3\text{C}} = \frac{0.76 - 0.022}{6.648} = \frac{0.738}{6.648} = 0.111$$

### b) Microconstituents at $T_5$
One microconstituent, **pearlite**, 100 %, with overall composition 0.76 % C; inside it, eutectoid ferrite 0.889 and eutectoid cementite 0.111.

![[attachments/T4/fc-micro-p2.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Mass balance: $0.889 \times 0.022 + 0.111 \times 6.67 = 0.020 + 0.740 = 0.76$ % C ✓.
- This is the make-up of every pearlite, the same as Worked example 15 of the theory (Session 9 Slide 13: 89 % and 11 %).

## ✅ Check against the official solution
Agrees with the key (0.89 and 0.11). The key calls the cementite of part (a) "$w_{Fe_3C'}$" (with a prime, the symbol of proeutectoid cementite); in a eutectoid steel there is no proeutectoid cementite, all of it is in the pearlite, as part (b) of the key says.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
