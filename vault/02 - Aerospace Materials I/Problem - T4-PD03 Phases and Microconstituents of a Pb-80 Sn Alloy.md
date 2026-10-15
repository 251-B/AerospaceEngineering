---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - hypereutectic
  - pb-sn
---

# ✏️ Problem: T4-PD03 — Phases and Microconstituents of a Pb-80 wt% Sn Alloy

## 📄 Official Statement
> **3. Using the Pb-Sn phase diagram for an alloy composition of Pb-80%Sn, indicate at the temperatures of $T_1 = 250$ ºC, $T_2 = 183 + \Delta T$ ºC, $T_3 = 183 - \Delta T$ ºC, $T_4 = 100$ ºC: a) The phases present, chemical composition of the phases and mass fraction. b) The micro constituents, chemical composition and mass fractions. Note the agreement that exists between the data obtained in (a) and (b).**
>
> *(Solutions; the phase symbols print as empty boxes in the PDF and are restored from context: a) $T_1$: $C_L = 80\%$ Sn, $w_L = 1$; $T_2$: $C_L = 61.9\%$ Sn, $C_\beta = 97.5\%$ Sn, $w_L = 0.49$; $T_3$: $C_\alpha = 19.2\%$ Sn, $C_\beta = 97.5\%$ Sn, $w_\alpha = 0.22$; $T_4$: $C_\alpha = 5\%$ Sn, $C_\beta = 100\%$ Sn, $w_\alpha = 0.21$; b) $C_{\beta'} = 97.5\%$ Sn, $C_E = 61.9\%$ Sn, $w_E = 0.49$, $w_{\beta'} = 0.51$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling**, Pb-Sn diagram of the problem sheet (p. 1): eutectic at 61.9 wt% Sn and 183 °C; at 183 °C, α of 19.2 and β of 97.5 wt% Sn.
2. Values at 250 °C and 100 °C are **readings of the figure**: at 250 °C the alloy is above the liquidus on the Sn side (which goes from 183 °C at 61.9 wt% Sn to 232 °C at 100 wt% Sn); at 100 °C the solvus lines give α of about 5 and β of about 100 wt% Sn.
3. $C_0 = 80$ wt% Sn lies between 61.9 and 97.5: a **hypereutectic** alloy, so the primary phase is β [Session 7 Slide 31].

### Data
| Temperature | Region | Phase compositions (wt% Sn) |
| :--- | :--- | :--- |
| $T_1 = 250$ °C | L | $C_L = 80$ |
| $T_2 = 183 + \Delta T$ | β + L | $C_L = 61.9$, $C_\beta = 97.5$ |
| $T_3 = 183 - \Delta T$ | α + β | $C_\alpha = 19.2$, $C_\beta = 97.5$ |
| $T_4 = 100$ °C | α + β | $C_\alpha = 5$, $C_\beta = 100$ |

---

## 🧠 2. Phase 2: Frames and Change of Basis

The frame is the Pb-Sn diagram (wt% Sn, °C). At each temperature the work is on one horizontal tie line, so it is one-dimensional; no change of basis is needed.

**Method.** (a) Tie line for the compositions, lever rule for the fractions [Session 7 Slides 15-16]. (b) Below the eutectic temperature, the lever rule on the short tie line (β to eutectic liquid) gives the microconstituents, and the long tie line (α to β) gives the phases [Session 7 Slide 32]; comparing both answers part (b)'s "agreement".

![[attachments/T4/pd-p3.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Phases
**$T_1 = 250$ °C.** Above the liquidus: one phase, liquid with the composition of the alloy. $C_L = 80$ wt% Sn, $W_L = 1$.

**$T_2 = 183 + \Delta T$.** Region β + L; tie line from $C_L = 61.9$ to $C_\beta = 97.5$ (length $97.5 - 61.9 = 35.6$):

$$W_\beta = \frac{C_0 - C_L}{C_\beta - C_L} = \frac{80 - 61.9}{97.5 - 61.9} = \frac{18.1}{35.6} = 0.508 \qquad W_L = \frac{C_\beta - C_0}{C_\beta - C_L} = \frac{97.5 - 80}{35.6} = \frac{17.5}{35.6} = 0.492$$

**$T_3 = 183 - \Delta T$.** Region α + β; tie line from 19.2 to 97.5 (length 78.3):

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{97.5 - 80}{97.5 - 19.2} = \frac{17.5}{78.3} = 0.224 \qquad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{80 - 19.2}{78.3} = \frac{60.8}{78.3} = 0.776$$

**$T_4 = 100$ °C.** Region α + β; tie line from 5 to 100 (length 95):

$$W_\alpha = \frac{100 - 80}{100 - 5} = \frac{20}{95} = 0.211 \qquad W_\beta = \frac{80 - 5}{95} = \frac{75}{95} = 0.789$$

### b) Microconstituents
At $T_1$ and $T_2$ the microconstituents are the phases themselves (liquid; primary β + liquid).

At $T_3$ there are two microconstituents: **primary β** (97.5 wt% Sn), formed in the β + L region, and **eutectic** (overall 61.9 wt% Sn), formed from the liquid present at $T_2$. With $P = C_0 - C_e$ and $Q = C_\beta - C_0$ on the short tie line:

$$W_{\beta'} = \frac{C_0 - C_e}{C_\beta - C_e} = \frac{80 - 61.9}{97.5 - 61.9} = 0.508 = W_\beta(T_2) \qquad W_E = \frac{C_\beta - C_0}{C_\beta - C_e} = \frac{17.5}{35.6} = 0.492 = W_L(T_2)$$

**Phases inside the eutectic:**

$$W_{\beta,E} = W_\beta(T_3) - W_{\beta'} = 0.776 - 0.508 = 0.268 \qquad W_{\alpha,E} = W_\alpha(T_3) = 0.224$$

(all the α is in the eutectic, since the primary phase is β).

![[attachments/T4/pd-micro-p3.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Agreement between (a) and (b)
- $W_{\beta,E} + W_{\alpha,E} = 0.268 + 0.224 = 0.492 = W_E$: the phases of the eutectic add up to the eutectic.
- Inside the eutectic, α is $0.224 / 0.492 = 0.455$, the same as the eutectic product of the sheet diagram, $(97.5 - 61.9)/(97.5 - 19.2) = 35.6/78.3 = 0.455$.
- Mass balance at $T_3$: $0.224 \times 19.2 + 0.776 \times 97.5 = 4.30 + 75.66 = 80.0$ wt% Sn.
- **Limiting cases** (fractions dimensionless, compositions in wt% Sn): at $C_0 = 61.9$ the alloy would be all eutectic ($W_{\beta'} = 0$) and at $C_0 = 97.5$ all primary β ($W_{\beta'} = 1$); 80 wt% Sn lies about halfway along the short tie line, hence about half of each.

### Interpretation
Below 183 °C the alloy is about half primary β and half eutectic. On further cooling to 100 °C the solvus lines move outwards (α purer in Pb, β practically pure Sn) and the amounts of the phases change slightly (α from 0.224 to 0.211) by solid-state precipitation, while the microconstituents keep their shape.

## ✅ Check against the official solution
All the values agree with the key ($w_L = 0.49$, $w_\alpha = 0.22$, $w_\alpha = 0.21$; $w_E = 0.49$, $w_{\beta'} = 0.51$).

> [!warning] Erratum in the worked solution
> Solution problems Phase diagrams I.pdf, p. 7, writes "T2; phases α and L"; the phases at $T_2$ are **β and L** (the alloy is hypereutectic). On the same page the $T_3$ formula is printed with the denominator $97.5 - 61.9$, but the value 0.22 corresponds to $97.5 - 19.2 = 78.3$: $17.5 / 35.6$ would give 0.49, while $17.5 / 78.3 = 0.22$. The numbers of the page are right; the labels and that denominator are not.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Concept - Tie Line and Lever Rule]]
* [[Problem - T4-PD04 Phases and Microconstituents of a Pb-30 Sn Alloy]]
