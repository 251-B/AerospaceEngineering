---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 2"
dificultad: medium
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - pb-sn
  - microconstituents
---

# ✏️ Problem: T4-PD02 — Primary and Total β in a Pb-Sn Alloy

## 📄 Official Statement
> **2. From 2.8 kg of a Sn-Pb alloy, is it possible to have 2.21 kg of primary β and 2.53 kg of β total at (183 − ΔT) °C? Justify your answer.**
>
> *(Solution: Yes, for an alloy with composition $C_0 = 90\%$ B)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Equilibrium cooling** with the Pb-Sn diagram of the problem sheet (Problems T4_PhaseDiagrams I.pdf, p. 1): eutectic at $C_e = 61.9$ wt% Sn and 183 °C; at 183 °C the α limit is $C_\alpha = 19.2$ wt% Sn and the β limit $C_\beta = 97.5$ wt% Sn.
2. **Primary β** exists only in a **hypereutectic** alloy ($61.9 < C_0 < 97.5$ wt% Sn): it is the β that forms in the β + L region before the eutectic reaction [Session 7 Slide 31].
3. Just below the eutectic temperature the primary β keeps the amount it had just above it, and the liquid present just above becomes the eutectic [Session 7 Slide 32].
4. "% B" in the key means wt% Sn (B is the Sn-rich side of the diagram).

### Data
| Quantity | Value |
| :--- | ---: |
| Mass of alloy $m$ | 2.8 kg |
| Mass of primary β $m_{\beta'}$ | 2.21 kg |
| Mass of total β $m_\beta$ (at 183 − ΔT) | 2.53 kg |
| $C_\alpha$, $C_e$, $C_\beta$ at 183 °C | 19.2, 61.9, 97.5 wt% Sn |

**Unknown:** the composition $C_0$. There is one unknown and two conditions, so the question is whether **both** masses can be met by the same $C_0$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

The frame is the Pb-Sn diagram, composition in wt% Sn and temperature in °C; the work is on the horizontal tie lines just above and just below 183 °C, so it is one-dimensional and no change of basis is needed.

**Strategy.** The primary β fixes $C_0$ through the lever rule on the short tie line between the eutectic liquid and β (microconstituents). The total β is then **predicted** with the lever rule on the long tie line between α and β (phases), and compared with 2.53 kg. If they agree, the answer is yes.

![[attachments/T4/pd-p2.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Mass fraction of primary β

$$W_{\beta'} = \frac{m_{\beta'}}{m} = \frac{2.21\ \text{kg}}{2.8\ \text{kg}} = 0.7893$$

### 2. Composition of the alloy
Just above 183 °C the alloy is β (97.5 wt% Sn) plus liquid of eutectic composition (61.9 wt% Sn). The lever rule gives the β fraction, which is the primary β [Session 7 Slide 32]:

$$W_{\beta'} = \frac{C_0 - C_e}{C_\beta - C_e} = \frac{C_0 - 61.9}{97.5 - 61.9} = \frac{C_0 - 61.9}{35.6}$$

Solving for $C_0$:

$$C_0 = 61.9 + 0.7893 \times 35.6 = 61.9 + 28.10 = 90.0\ \text{wt\% Sn}$$

$61.9 < 90.0 < 97.5$: the alloy is hypereutectic, as primary β requires.

### 3. Total β predicted for this alloy
Just below 183 °C the phases are α (19.2 wt% Sn) and β (97.5 wt% Sn):

$$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{90.0 - 19.2}{97.5 - 19.2} = \frac{70.8}{78.3} = 0.9042$$

$$m_\beta = W_\beta\, m = 0.9042 \times 2.8\ \text{kg} = 2.532\ \text{kg} \approx 2.53\ \text{kg}$$

### 4. Answer
Both conditions are met by the same alloy: **yes**, it is possible, with a Pb-90 wt% Sn alloy.

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Eutectic part:** mass of eutectic $= 2.8 - 2.21 = 0.59$ kg; β inside it $= 2.53 - 2.21 = 0.32$ kg, a fraction $0.32 / 0.59 = 0.54$. The eutectic of the sheet diagram has $W_{\beta,e} = (61.9 - 19.2)/(97.5 - 19.2) = 42.7/78.3 = 0.545$ of β, and $0.545 \times 0.59 = 0.32$ kg: consistent.
- **Units:** masses in kg, fractions dimensionless, compositions in wt% Sn.

### Interpretation
The two masses are not independent: once the primary β fixes the composition, the total β is fixed too. A different total β (say 2.40 kg) would have been impossible for any alloy.

## ✅ Check against the official solution
The official key ("Yes, for an alloy with composition $C_0 = 90\%$") agrees. The worked page (Solution problems Phase diagrams I.pdf, p. 6) finds $C_0 = 90\%$ from the primary β only; the check of the total β (2.53 kg) above completes the justification. The page writes the fraction as "079"; it is 0.79.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Tie Line and Lever Rule]]
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Problem - T4-PD03 Phases and Microconstituents of a Pb-80 Sn Alloy]]
