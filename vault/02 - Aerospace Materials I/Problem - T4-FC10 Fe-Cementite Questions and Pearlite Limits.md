---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams II.pdf, Problem 10"
dificultad: medium
tags:
  - official-problem
  - solved
  - fe-c-system
  - pearlite
  - invariant-reactions
---

# ✏️ Problem: T4-FC10 — Fe-Cementite Questions and Pearlite Limits

## 📄 Official Statement
> **10.- Using the Fe-cementite phase diagram, indicate: a) What real alloy or alloys comply the following conditions $W_\alpha$ = 0.267 at 727 − ΔT ºC? b) What is the maximum and minimum content (mass fraction W) of pearlite in a steel? Explain why. c) Indicate the invariant points that appear in the diagram and explain which microconstituents are formed during cooling. d) For the alloys with 1.5% C and 3% C, indicate the microconstituents and if the mass fraction of them changes on cooling in the range between 1148 ºC and 727 + ΔT ºC.**
>
> *(Solutions: a) $C_0$ = 4.9% C; b) Max: 100% for $C_0$ = 0.76%C; min: 0% for $C_0$ < 0.022%C; d) 1.5% C; $T_1$: $w_\gamma$ = 1, $T_2$: $w_{Fe_3C}$ 0.12, $w_\gamma$ = 0.88; 3% C; $T_1$: $w_\gamma$ = 0.6, $w_L$ = 0.4, $T_2$: $w_{\gamma total}$ = 0.62, $w_{Fe_3C\,Total}$ = 0.38, $w_{Fe_3C\,secondary}$ = 0.20)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

1. Equilibrium, Fe-Fe₃C diagram [Session 9 Slides 4, 10].
2. Below 727 °C every alloy is α (0.022) + Fe₃C (6.67); one ferrite fraction gives one composition.
3. "Steel" = up to 2.14 % C [Session 9 Slide 4].

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Fe-Fe₃C diagram (wt% C, °C). The lever rule on the α-Fe₃C tie line (a), the short tie line through the eutectoid point (b), the invariant lines (c) and the tie lines at 1148 °C (the statement's temperature, just above the eutectic: 1147 + ΔT) and 727 + ΔT (d) [Session 7 Slides 16, 32].

![[attachments/T4/fc-p10.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Alloy with $W_\alpha$ = 0.267
$$W_\alpha = \frac{C_{\text{Fe}_3\text{C}} - C_0}{C_{\text{Fe}_3\text{C}} - C_\alpha} \;\Rightarrow\; C_0 = C_{\text{Fe}_3\text{C}} - W_\alpha\,(C_{\text{Fe}_3\text{C}} - C_\alpha)$$
$$C_0 = 6.67 - 0.267 \times (6.67 - 0.022) = 6.67 - 0.267 \times 6.648 = 6.67 - 1.775 = 4.895 \approx 4.9\ \%\,\text{C}$$
Only **one** alloy: a hypereutectic cast iron.

### b) Pearlite in steels
Pearlite is the austenite of 0.76 % C present just above 727 °C.
- **Maximum, 100 %**, for the eutectoid steel, $C_0$ = 0.76 % C: all of it is austenite of eutectoid composition.
- **Minimum, 0 %**, for $C_0 \le 0.022$ % C: the alloy never crosses the eutectoid line inside the α + γ field (it stays α).
- Between them, hypoeutectoid: $W_{\text{pearlite}} = (C_0 - 0.022)/(0.76 - 0.022)$; hypereutectoid: $W_{\text{pearlite}} = (6.67 - C_0)/(6.67 - 0.76)$, which at the steel limit (2.14 % C) is $4.53/5.91 = 0.77$.

### c) Invariant points and their products on cooling [Session 9 Slide 10]
- **Peritectic, 1493 °C:** $\delta\,(0.09) + L\,(0.53) \rightarrow \gamma\,(0.16)$: austenite.
- **Eutectic, 1147 °C:** $L\,(4.3) \rightarrow \gamma\,(2.14) + \text{Fe}_3\text{C}$: ledeburite (cast irons).
- **Eutectoid, 727 °C:** $\gamma\,(0.76) \rightarrow \alpha\,(0.022) + \text{Fe}_3\text{C}$: pearlite (steels, and the austenite of cast irons).

### d) 1.5 % C and 3 % C between 1148 °C and 727 + ΔT
**1.5 % C** (hypereutectoid steel). At 1148 °C: austenite only, $W_\gamma = 1$. At 727 + ΔT (γ 0.76 / Fe₃C 6.67):
$$W_\gamma = \frac{6.67 - 1.5}{5.91} = 0.875 \qquad W_{\text{Fe}_3\text{C}} = \frac{1.5 - 0.76}{5.91} = 0.125$$
The microconstituents **change**: proeutectoid cementite appears at $A_{cm}$ and grows to 0.125.

**3 % C** (hypoeutectic cast iron). At 1148 °C (γ 2.14 / L 4.30): $W_\gamma = 1.30/2.16 = 0.602$, $W_L = 0.398$. At 727 + ΔT (γ 0.76 / Fe₃C 6.67):
$$W_{\gamma,\text{total}} = \frac{6.67 - 3.0}{5.91} = \frac{3.67}{5.91} = 0.621 \qquad W_{\text{Fe}_3\text{C},\text{total}} = \frac{3.0 - 0.76}{5.91} = \frac{2.24}{5.91} = 0.379$$
The microconstituents (primary austenite and ledeburite) **change** too: the austenite loses carbon and secondary cementite precipitates. The ledeburite brought $0.190$ of cementite at 1146 °C (Problem FC09), so the secondary cementite is $0.379 - 0.190 = 0.189$.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

- (a): $(6.67 - 4.895)/6.648 = 0.267$ ✓.
- (d): 1.5 %: $0.875 \times 0.76 + 0.125 \times 6.67 = 0.665 + 0.834 = 1.50$ % C ✓; 3 %: $0.621 \times 0.76 + 0.379 \times 6.67 = 0.47 + 2.53 = 3.0$ % C ✓.
- **Limiting cases** (fractions dimensionless, compositions in wt% C): the pearlite fraction of a hypereutectoid steel, $(6.67 - C_0)/(6.67 - 0.76)$, is 1 at the eutectoid composition and falls to 0 at 6.67 % C; at 1.5 % C it is 0.875.

## ✅ Check against the official solution
(a), (b) and the 3 % C phases agree with the key (4.9 %; 100 % and 0 %; 0.6/0.4; 0.62/0.38). The key does not answer part (c).

> [!warning] Discrepancy with the official solution
> For 1.5 % C the key gives 0.12/0.88 against 0.125/0.875 here (0.13/0.87 when rounded, as in the key of Problem 3 for the same alloy). The key's value follows from 6.7 % C for cementite: $(1.5 - 0.76)/(6.7 - 0.76) = 0.74/5.94 = 0.1246 \to 0.12$. With the slides' 6.67 % C it is $0.74/5.91 = 0.125$, which is kept.

> [!warning] Discrepancy with the official solution
> The key gives 0.20 of secondary cementite for the 3 % C alloy. With the values of the diagram, $0.379 - 0.190 = 0.189$ (0.19); the key's 0.20 is not reproduced by any rounding of these data. The computed value is kept.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - The Fe-Fe3C Diagram and Steel Microstructures]]
* [[Problem - T4-FC09 A 3 C Cast Iron from 1146 to 800 C]]
