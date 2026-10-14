---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 4"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - hypoeutectic
  - pb-sn
---

# ✏️ Problem: T4-PD04 — Phases and Microconstituents of a Pb-30 wt% Sn Alloy

## 📄 Official Statement
> **4. Using the Pb-Sn phase diagram for an alloy composition of Pb-30%Sn, indicate at the temperatures of $T_1 = 250$ ºC, $T_2 = 183 + \Delta T$ ºC, $T_3 = 183 - \Delta T$ ºC, $T_4 = 100$ ºC: a) The phases present, chemical composition of the phases and mass fraction. b) The micro constituents, chemical composition and mass fractions. Note the agreement that exists between the data obtained in (a) and (b).**
>
> *(Solutions: a) $T_1$: $C_L = 36\%$ Sn, $C_\alpha = 12\%$ Sn, $w_L = 0.75$; $T_2$: $C_L = 61.9\%$ Sn, $C_\alpha = 19.2\%$ Sn, $w_L = 0.25$; $T_3$: $C_\alpha = 19.2\%$ Sn, $C_\beta = 97.5\%$ Sn, $w_\alpha = 0.86$; $T_4$: $C_\alpha = 5\%$ Sn, $C_\beta = 100\%$ Sn, $w_\alpha = 0.74$; b) $T_3$: $C_{\alpha'} = 19.2\%$ Sn, $C_E = 61.9\%$ Sn, $w_E = 0.25$, $w_{\alpha'} = 0.75$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling**, Pb-Sn diagram of the problem sheet (p. 1): eutectic at 61.9 wt% Sn and 183 °C; α of 19.2 and β of 97.5 wt% Sn at 183 °C.
2. **Readings of the figure:** at 250 °C the tie line meets the α solidus at 12 wt% Sn and the liquidus at 36 wt% Sn; at 100 °C the solvus lines give α of 5 and β of 100 wt% Sn (the same readings as the official solution).
3. $19.2 < C_0 = 30 < 61.9$: a **hypoeutectic** alloy, so the primary phase is α [Session 7 Slide 30]. This is the same kind of alloy as the hypoeutectic example of the slides.

### Data
| Temperature | Region | Phase compositions (wt% Sn) |
| :--- | :--- | :--- |
| $T_1 = 250$ °C | α + L | $C_\alpha = 12$, $C_L = 36$ |
| $T_2 = 183 + \Delta T$ | α + L | $C_\alpha = 19.2$, $C_L = 61.9$ |
| $T_3 = 183 - \Delta T$ | α + β | $C_\alpha = 19.2$, $C_\beta = 97.5$ |
| $T_4 = 100$ °C | α + β | $C_\alpha = 5$, $C_\beta = 100$ |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: the Pb-Sn diagram (wt% Sn, °C); one horizontal tie line per temperature, so no change of basis is needed.

**Method.** Tie line and lever rule at each temperature [Session 7 Slides 15-16]; below 183 °C, the short tie line (α to eutectic liquid) gives the microconstituents and the long one (α to β) the phases [Session 7 Slide 32].

![[attachments/T4/pd-p4.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1 = 250$ °C.** α + L; tie line from 12 to 36 (length 24):

$$W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha} = \frac{30 - 12}{36 - 12} = \frac{18}{24} = 0.750 \qquad W_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} = \frac{36 - 30}{24} = \frac{6}{24} = 0.250$$

**$T_2 = 183 + \Delta T$.** α + L; tie line from 19.2 to 61.9 (length 42.7):

$$W_L = \frac{30 - 19.2}{61.9 - 19.2} = \frac{10.8}{42.7} = 0.253 \qquad W_\alpha = \frac{61.9 - 30}{42.7} = \frac{31.9}{42.7} = 0.747$$

**$T_3 = 183 - \Delta T$.** α + β; tie line from 19.2 to 97.5 (length 78.3):

$$W_\alpha = \frac{97.5 - 30}{97.5 - 19.2} = \frac{67.5}{78.3} = 0.862 \qquad W_\beta = \frac{30 - 19.2}{78.3} = \frac{10.8}{78.3} = 0.138$$

**$T_4 = 100$ °C.** α + β; tie line from 5 to 100 (length 95):

$$W_\alpha = \frac{100 - 30}{100 - 5} = \frac{70}{95} = 0.737 \qquad W_\beta = \frac{30 - 5}{95} = \frac{25}{95} = 0.263$$

### b) Microconstituents
At $T_1$ and $T_2$ they coincide with the phases (α + liquid). At $T_3$: **primary α** (19.2 wt% Sn) and **eutectic** (61.9 wt% Sn overall):

$$W_{\alpha'} = \frac{C_e - C_0}{C_e - C_\alpha} = \frac{61.9 - 30}{61.9 - 19.2} = 0.747 = W_\alpha(T_2) \qquad W_E = \frac{C_0 - C_\alpha}{C_e - C_\alpha} = \frac{30 - 19.2}{42.7} = 0.253 = W_L(T_2)$$

**Phases inside the eutectic:**

$$W_{\alpha,E} = W_\alpha(T_3) - W_{\alpha'} = 0.862 - 0.747 = 0.115 \qquad W_{\beta,E} = W_\beta(T_3) = 0.138$$

![[attachments/T4/pd-micro-p4.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Agreement between (a) and (b)
- $W_{\alpha,E} + W_{\beta,E} = 0.115 + 0.138 = 0.253 = W_E$.
- Inside the eutectic, α is $0.115 / 0.253 = 0.455$, the eutectic product of the sheet diagram ($35.6/78.3 = 0.455$), the same as in Problem 3: the eutectic has the same make-up whatever the alloy.
- Mass balance at $T_3$: $0.862 \times 19.2 + 0.138 \times 97.5 = 16.55 + 13.45 = 30.0$ wt% Sn.

### Interpretation
The alloy is three quarters primary α in one quarter of eutectic, the structure of the hypoeutectic micrograph of Slide 30. From 250 °C to 183 °C the amount of α grows from 25 % to 75 % while the liquid gets richer in Sn, from 36 to 61.9 wt%.

## ✅ Check against the official solution
The values agree with the key ($w_L = 0.75$, $0.25$; $w_\alpha = 0.86$, $0.74$; $w_E = 0.25$, $w_{\alpha'} = 0.75$). The α inside the eutectic is $0.862 - 0.747 = 0.115$; the worked page writes 0.11 because it subtracts the rounded values $0.86 - 0.75$.

> [!warning] Erratum in the worked solution
> Solution problems Phase diagrams I.pdf, p. 10, gives for $T_4$ the numbers of Problem 3: $\chi_\alpha = (100 - 80)/(100 - 5) = 0.21$ and $\chi_{\beta,\text{total}} = 0.79$. For this alloy ($C_0 = 30$) the correct values are $W_\alpha = 70/95 = 0.74$ and $W_\beta = 0.26$, as the key of the statement says. The $T_1$ formula on p. 9 is also printed with the wrong labels ($C_o - C_\beta$ over $C_E - C_\alpha$), while its numbers, $(30 - 12)/(36 - 12) = 0.75$, are right.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Concept - Tie Line and Lever Rule]]
* [[Problem - T4-PD03 Phases and Microconstituents of a Pb-80 Sn Alloy]]
