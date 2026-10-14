---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 8"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - hypoeutectoid
  - alloying-elements
---

# ✏️ Problem: T4-FC08 — Annealed 0.55 % C Steel Bar and the Effect of Nickel

## 📄 Official Statement
> **8.- Examine closely the phase diagram Fe-C and answer the following questions. a) If there is a 5 kg annealed bar of an alloy with 0.55 % C, what is the quantity (mass expressed in kg) of pre-eutectoid ferrite, eutectoid ferrite and cementite that is contained at 726 ºC? b) List the phases and microconstituents in this steel, their composition and their percentage at 600 ºC. c) How are the carbon content and temperature at the eutectoid point modified in the diagram if Ni is added? How does this addition modify the steel's microstructure?**
>
> *(Solutions: a) $\alpha'$ = 1.43 kg; pearlite = 3.6 kg; $\alpha_{total}$ = 4.6 kg; $\alpha_{eutectoid}$ = 3.17 kg; Fe₃C = 0.4 kg; b) $x_{\alpha pre}$ = 0.26; $x_{eutectoid}$ = 0.72; $w_{\alpha total}$ = 0.92; $w_{Fe_3C}$ = 0.08; c) possible decrease in amount of primary ferrite)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. **Annealed** means slowly cooled: equilibrium structure, Fe-Fe₃C diagram [Session 9 Slide 4].
2. $C_0 = 0.55 < 0.76$: hypoeutectoid; at 726 °C (just below 727 °C) the structure is proeutectoid ferrite + pearlite [Session 9 Slide 14].
3. At 600 °C the ferrite solvus gives slightly less than 0.022 % C; the difference does not change the result to two decimals, so 0.022 % C is used (a reading of the figure).
4. Data: $m$ = 5 kg.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram; tie lines just above 727 °C (α 0.022 / γ 0.76, for the proeutectoid ferrite) and below it (α 0.022 / Fe₃C 6.67, for the phases). Masses are fractions times 5 kg.

![[attachments/T4/fc-p8.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) At 726 °C
$$W_{\alpha'} = \frac{0.76 - 0.55}{0.76 - 0.022} = \frac{0.21}{0.738} = 0.285 \;\Rightarrow\; m_{\alpha'} = 0.285 \times 5 = 1.42\ \text{kg}$$
$$W_{\text{pearlite}} = 1 - 0.285 = 0.715 \;\Rightarrow\; m_{\text{pearlite}} = 3.58\ \text{kg}$$
$$W_{\alpha,\text{total}} = \frac{6.67 - 0.55}{6.648} = \frac{6.12}{6.648} = 0.921 \;\Rightarrow\; m_{\alpha,\text{total}} = 4.60\ \text{kg}$$
$$m_{\alpha,E} = 4.60 - 1.42 = 3.18\ \text{kg} \qquad m_{\text{Fe}_3\text{C}} = (1 - 0.921) \times 5 = 0.079 \times 5 = 0.40\ \text{kg}$$

### b) At 600 °C
- **Phases:** α (≈ 0.022 % C) 92 % and Fe₃C (6.67 % C) 8 %.
- **Microconstituents:** proeutectoid ferrite 28.5 % and pearlite (0.76 % C overall) 71.5 %. The microconstituents formed at 727 °C do not change on further slow cooling.

### c) Effect of nickel
Ni is a **γ-stabilising element**: it displaces the eutectoid point to **lower temperature and lower %C** [Session 9 Slides 22-23]. With a lower eutectoid composition, the same 0.55 % C steel lies closer to the eutectoid point, so the short tie line gives **less proeutectoid ferrite and more pearlite**.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- Mass check: $1.42 + 3.58 = 5.00$ kg; $4.60 + 0.40 = 5.00$ kg; pearlite $3.18 + 0.40 = 3.58$ kg ✓.
- Carbon: $0.40\ \text{kg} \times 6.67\,\% + 4.60\ \text{kg} \times 0.022\,\% = 0.0267 + 0.0010 = 0.0277$ kg C $= 0.55\,\%$ of 5 kg ✓.

## ✅ Check against the official solution
Part (a) agrees with the key (1.43, 3.6, 4.6, 3.17 and 0.4 kg, within rounding); (c) agrees.

> [!warning] Discrepancy with the official solution
> For part (b) the key gives $x_{\alpha pre} = 0.26$ and $x_{eutectoid} = 0.72$, which do not add up to 1 and do not match its own part (a) ($1.43/5 = 0.286$, $3.6/5 = 0.72$). The lever rule gives 0.285 proeutectoid ferrite and 0.715 pearlite, the same at 726 and at 600 °C; these values are kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Problem - T4-FC01 Phases and Microconstituents of a 0.5 C Steel]]
