---
materia: "Aerospace Materials I"
tema: "Topic 4: Phase Diagrams and Solidification"
origen: "Problems T4_PhaseDiagrams I.pdf, Problem 8"
dificultad: hard
tags:
  - official-problem
  - solved
  - lever-rule
  - eutectic
  - phase-diagram-construction
  - microconstituents
---

# ✏️ Problem: T4-PD08 — Drawing a Eutectic Diagram and the 40 % B Alloy

## 📄 Official Statement
> **8. Two metals (A and B) have partial solubility among each other. Metal A, with a melting point at 700 °C, can dissolve 5% of B at 0 °C, and its maximum solubility occurs at 400 °C, being 25% B. On the other hand, B metal melts at 600 °C, can dissolve 10% of A at 0 °C and its maximum solubility occurs at 400 °C, being 20% A. At 400 °C there is an eutectic reaction when the B content is 65%. a. Draw and identify the parts of the phase diagram in equilibrium (suppose straight lines). b. For an alloy 40% B, determine the phases composition and their relative proportions at 450 °C, 400 °C + ΔT and 400 °C − ΔT. c. For an alloy 40% B, draw its microstructure indicating the microconstituents and the mass fraction of each one. Additionally, indicate the mass fraction of each of the phases present in such microconstituents.**
>
> *(Solution: b) 450 °C: $C_L$ = 55%B; $C_\alpha$ = 20%B; $X_\alpha = 0.43$; $X_L = 0.57$; 400 °C + ΔT: $C_L$ = 65%B; $C_\alpha$ = 25%B; $X_\alpha = 0.62$; $X_L = 0.38$; 400 °C − ΔT: $C_\beta$ = 80%B; $C_\alpha$ = 25%B; $X_\alpha = 0.73$; $X_\beta = 0.27$. c) Eutectic microconstituent and proeutectic α; $X_{\alpha p} = 0.62$; $X_E = 0.38$; Phases in the eutectic microconstituent: $X(\alpha_E) = 0.11$; $X(\beta_E) = 0.27$.)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Hypotheses
1. **Binary eutectic system** with partial solid solubility: α (rich in A) and β (rich in B) [Session 7 Slide 26].
2. **Straight lines** between the given points, as the statement asks.
3. Compositions in % B (mass); "20 % A" in β means 80 % B, and "10 % A" means 90 % B.

### Points of the diagram
| Point | Composition (% B) | Temperature (°C) | Meaning |
| :--- | ---: | ---: | :--- |
| Melting point of A | 0 | 700 | top of α solidus and of the A-side liquidus |
| Melting point of B | 100 | 600 | top of β solidus and of the B-side liquidus |
| Eutectic point E | 65 | 400 | lowest point of the liquid |
| Max. solubility of B in α | 25 | 400 | end of the eutectic line, α side |
| Max. solubility of A in β | 80 | 400 | end of the eutectic line, β side |
| α solvus at 0 °C | 5 | 0 | |
| β solvus at 0 °C | 90 | 0 | |

---

## 🧠 2. Phase 2: Frames and Change of Basis

Frame: composition (% B) on the horizontal axis and temperature (°C) on the vertical one. Each boundary is a straight segment, so a composition on it at a temperature $T$ comes from linear interpolation between its two end points; the tie lines are horizontal. No change of basis is needed.

**Lines of the diagram (part a):**
- liquidus: $(0, 700) \to (65, 400)$ and $(100, 600) \to (65, 400)$;
- solidus: $(0, 700) \to (25, 400)$ for α and $(100, 600) \to (80, 400)$ for β;
- eutectic line: $(25, 400) \to (80, 400)$;
- solvus: $(25, 400) \to (5, 0)$ for α and $(80, 400) \to (90, 0)$ for β.

Regions: L above the liquidus; α + L and β + L between liquidus and solidus; α and β next to the axes, bounded by solidus and solvus; α + β below the eutectic line, between the solvus lines.

![[attachments/T4/pd-p8.svg]]

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### b) Phases of the 40 % B alloy
**450 °C.** The alloy is between the A-side liquidus and the α solidus: **α + L**. On a straight segment from $(0, 700)$ to $(C_1, 400)$ the composition at $T$ is $C = C_1 \dfrac{700 - T}{700 - 400}$:

$$C_L = 65 \times \frac{700 - 450}{300} = 65 \times \frac{250}{300} = 54.17\ \%\text{B} \qquad C_\alpha = 25 \times \frac{250}{300} = 20.83\ \%\text{B}$$

$$W_L = \frac{C_0 - C_\alpha}{C_L - C_\alpha} = \frac{40 - 20.83}{54.17 - 20.83} = \frac{19.17}{33.33} = 0.575 \qquad W_\alpha = \frac{C_L - C_0}{C_L - C_\alpha} = \frac{54.17 - 40}{33.33} = \frac{14.17}{33.33} = 0.425$$

**400 °C + ΔT.** Still α + L, with the ends of the tie line at the eutectic temperature: $C_\alpha = 25$, $C_L = 65$ % B (length 40):

$$W_L = \frac{40 - 25}{65 - 25} = \frac{15}{40} = 0.375 \qquad W_\alpha = \frac{65 - 40}{40} = \frac{25}{40} = 0.625$$

**400 °C − ΔT.** α + β; $C_\alpha = 25$, $C_\beta = 80$ % B (length 55):

$$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{80 - 40}{80 - 25} = \frac{40}{55} = 0.727 \qquad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{40 - 25}{55} = \frac{15}{55} = 0.273$$

### c) Microconstituents at 400 °C − ΔT
$25 < 40 < 65$: hypoeutectic, so the microconstituents are **proeutectic α** (25 % B) and **eutectic** (65 % B overall). The α present just above 400 °C is the proeutectic α, and the liquid becomes eutectic [Session 7 Slide 32]:

$$W_{\alpha p} = \frac{C_e - C_0}{C_e - C_\alpha} = \frac{65 - 40}{65 - 25} = 0.625 \qquad W_E = \frac{C_0 - C_\alpha}{C_e - C_\alpha} = \frac{40 - 25}{40} = 0.375$$

**Phases inside the eutectic:**

$$W_{\alpha,E} = W_\alpha - W_{\alpha p} = 0.7273 - 0.6250 = 0.1023 \qquad W_{\beta,E} = W_\beta = 0.273$$

The same numbers from the make-up of the eutectic, which is $(80 - 65)/(80 - 25) = 15/55 = 0.273$ α and $40/55 = 0.727$ β: $W_{\alpha,E} = 0.375 \times 0.273 = 0.102$ and $W_{\beta,E} = 0.375 \times 0.727 = 0.273$.

![[attachments/T4/pd-micro-p8.svg]]

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- Mass balance at 450 °C: $0.425 \times 20.83 + 0.575 \times 54.17 = 8.85 + 31.15 = 40.0$ % B.
- Mass balance at 400 °C − ΔT: $0.727 \times 25 + 0.273 \times 80 = 18.18 + 21.82 = 40.0$ % B.
- $W_{\alpha,E} + W_{\beta,E} = 0.102 + 0.273 = 0.375 = W_E$, and $W_{\alpha p} + W_{\alpha,E} = 0.625 + 0.102 = 0.727 = W_\alpha$.

### Interpretation
On cooling from the liquid, α starts to form at the liquidus ($700 - 300 \times 40/65 = 515$ °C for this alloy), grows to 62.5 % at the eutectic temperature, and the remaining 37.5 % of liquid, of 65 % B, becomes eutectic at 400 °C. Most of the eutectic is β (0.273 of the alloy), which is all the β of the alloy.

## ✅ Check against the official solution
At 400 °C ± ΔT the results agree with the key (0.62/0.38 are 0.625/0.375; 0.73/0.27). The key writes "$C_\alpha$ = 25%Cu" at 400 °C + ΔT, a typo for 25 % B.

> [!warning] Discrepancy with the official solution
> **450 °C.** The key reads $C_L = 55$ and $C_\alpha = 20$ % B from its drawing and gives $X_L = 0.57$, $X_\alpha = 0.43$. With the straight lines that the statement requires, linear interpolation gives $C_L = 54.17$ and $C_\alpha = 20.83$ % B, hence $W_L = 0.575$ and $W_\alpha = 0.425$. The difference comes from reading the drawing; the interpolated values are kept.
>
> **α in the eutectic.** The key gives $X(\alpha_E) = 0.11$, which is $0.73 - 0.62$ with rounded values. Exactly, $0.7273 - 0.6250 = 0.1023$, confirmed by $0.375 \times 15/55 = 0.102$; the key's 0.11 is a rounding effect.

---

## 🔗 Related Links
* [[Topic 4 - Phase Diagrams and Solidification]] (Master note for Topic 4)
* [[Concept - Binary Eutectic Systems and Microconstituents]]
* [[Concept - Tie Line and Lever Rule]]
