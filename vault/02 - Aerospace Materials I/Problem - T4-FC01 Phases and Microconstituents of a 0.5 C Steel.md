---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 1"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - hypoeutectoid
  - lever-rule
---

# ✏️ Problem: T4-FC01 — Phases and Microconstituents of a 0.5 % C Steel

## 📄 Official Statement
> **1.- For a Fe-C alloy with $C_0$ = 0.5%C, at the following temperatures: $T_1$ = (1147+ΔT)ºC; $T_2$ = (1147−ΔT)ºC; $T_3$ = 900ºC; $T_4$ = (727+ΔT)ºC; $T_5$ = (727−ΔT)ºC. a) Indicate the phases present, their chemical composition and their mass fraction. b) Indicate the micro constituents, their chemical composition and their mass fraction at $T_5$.**
>
> *(Solutions: a) $T_1$, $T_2$, and $T_3$: $C_\gamma$ = 0.5% C, $w_\gamma$ = 1; $T_4$: $C_\alpha$ = 0.022% C, $C_\gamma$ = 0.76% C, $w_\alpha$ = 0.35; $T_5$: $C_\alpha$ = 0.022% C, $C_{Fe_3C}$ = 6.7% C, $w_\alpha$ = 0.93; b) $w_{\alpha'}$ = 0.35, $w_{\alpha,E}$ = 0.58, $w_{Fe_3C}$ = 0.07)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. **Equilibrium cooling** on the metastable Fe-Fe₃C diagram of the sheet (the diagram of Session 9 Slide 4): $C_\alpha$ = 0.022 % C, eutectoid 0.76 % C at 727 °C, cementite 6.67 % C.
2. $C_0 = 0.5 < 0.76$: a **hypoeutectoid steel** [Session 9 Slide 14]; its solidus is far above 1147 °C, so at $T_1$, $T_2$ and $T_3$ it is fully austenitic.
3. The microconstituents below 727 °C are proeutectoid ferrite and pearlite [Session 9 Slide 14].

| Temperature | Region | Phase compositions (% C) |
| :--- | :--- | :--- |
| $T_1$, $T_2$, $T_3$ | γ | 0.5 |
| $T_4$ = 727 + ΔT | α + γ | α 0.022, γ 0.76 |
| $T_5$ = 727 − ΔT | α + Fe₃C | α 0.022, Fe₃C 6.67 |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C); each temperature is one horizontal tie line, so no change of basis is needed. Phases from the lever rule [Session 7 Slide 16]; microconstituents from the short tie line α-eutectoid (0.022-0.76), exactly as in the 0.3 % C example of the slides [Session 9 Slide 18].

![[attachments/T4/fc-p1.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1$, $T_2$, $T_3$:** austenite only, $C_\gamma = 0.5$ % C, $W_\gamma = 1$.

**$T_4$** (length $0.76 - 0.022 = 0.738$):
$$W_\alpha = \frac{C_\gamma - C_0}{C_\gamma - C_\alpha} = \frac{0.76 - 0.5}{0.738} = \frac{0.26}{0.738} = 0.352 \qquad W_\gamma = \frac{0.5 - 0.022}{0.738} = \frac{0.478}{0.738} = 0.648$$

**$T_5$** (length $6.67 - 0.022 = 6.648$):
$$W_\alpha = \frac{6.67 - 0.5}{6.648} = \frac{6.17}{6.648} = 0.928 \qquad W_{\text{Fe}_3\text{C}} = \frac{0.5 - 0.022}{6.648} = \frac{0.478}{6.648} = 0.072$$

### b) Microconstituents at $T_5$
The ferrite present at $T_4$ is the proeutectoid ferrite, and the austenite present at $T_4$ (0.76 % C) becomes pearlite:
$$W_{\alpha'} = 0.352 \qquad W_{\text{pearlite}} = 0.648$$
Inside the pearlite: eutectoid ferrite $W_{\alpha,E} = W_\alpha - W_{\alpha'} = 0.928 - 0.352 = 0.576$ and cementite $W_{\text{Fe}_3\text{C}} = 0.072$.

![[attachments/T4/fc-micro-p1.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- $0.576 + 0.072 = 0.648 = W_{\text{pearlite}}$, and $0.648 \times 0.889 = 0.576$ (pearlite is 88.9 % ferrite, Session 9 Slide 13) ✓.
- Mass balance at $T_5$: $0.928 \times 0.022 + 0.072 \times 6.67 = 0.020 + 0.480 = 0.50$ % C ✓.
- Limits: at $C_0 = 0.022$ there is no pearlite; at $C_0 = 0.76$ there is no proeutectoid ferrite.

## ✅ Check against the official solution
All values agree with the key (0.35; 0.93; 0.35, 0.58, 0.07). The key writes $C_{Fe_3C}$ = 6.7 % C; the 6.67 % C of the slides gives the same rounded results.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Concept - Tie Line and Lever Rule]]
