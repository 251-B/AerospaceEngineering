---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 8"
dificultad: easy
badge: "Yield strength · Hooke's law"
tags:
  - official-problem
  - solved
  - yield-strength
  - hooke-law
  - elastic-limit
---

# ✏️ Problem: T5-08 — Elastic Limits of a Brass Sample: Stress, Load and Length without Plastic Deformation

## 📄 Official Statement
> 8. For a particular kind of brass, plastic deformation begins at 345 MPa, and its elastic modulus is 103 GPa.
> >
> > - a. What is the value of the yield stress?
> > - b. What is the maximum stress that can be applied to a sample of this brass with a cross-section 130 mm² without plastic deformation taking place? And the maximum load?
> > - c. If the initial length of the sample is 76 mm, what is the maximum length that it can reach without plastic deformation?
>
> *(Solution: a. $\sigma_y = 345$ MPa; b. $\sigma_{max} = 345$ MPa, $F_{max} = 44850$ N; c. $l = 76.25$ mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Yield strength.** "Plastic deformation begins at 345 MPa" means that 345 MPa is the yield strength of the brass: below it the deformation is only elastic, above it part of it is permanent [Session 11 Slide 28].
2. **Linear elastic below the yield strength**, $\sigma = E\varepsilon$ [Session 11 Slide 13], with the given modulus.
3. **Uniaxial, uniform stress**: $\sigma = F/A_0$ and $\varepsilon = \Delta l/l_0$ [Session 11 Slide 9]. The maximum values without plastic deformation are those that correspond to the stress $\sigma_y$.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Stress at which plastic deformation begins | $\sigma_y$ | 345 MPa | $345\times10^{6}$ Pa |
| Young's modulus | $E$ | 103 GPa | 103 000 N/mm² |
| Cross-section (item b) | $A_0$ | 130 mm² | $130\times10^{-6}$ m² |
| Initial length (item c) | $l_0$ | 76 mm | $76\times10^{-3}$ m |

**Unknowns:** $\sigma_y$ (a), the maximum stress and load (b), the maximum length (c).

---

## 🧠 2. Phase 2: Frames and Strategy

One direction (the axis of the sample), no change of basis.

**Strategy.** The three items are the same limit seen from three sides. The largest stress that does not cause plastic deformation is the yield strength (a, b). The largest load is that stress times the area, $F = \sigma_y A_0$ (b). The largest length is the initial length plus the elongation at the yield strength, and that elongation comes from Hooke's law, $\varepsilon_y = \sigma_y/E$ and $\Delta l = \varepsilon_y\,l_0$ (c).

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### a) Yield stress
By the hypothesis, plastic deformation begins when $\sigma = 345$ MPa, so

$$\sigma_y = \mathbf{345\ MPa}$$

### b) Maximum stress and maximum load
Without plastic deformation the stress cannot be larger than the yield strength, so

$$\sigma_{max} = \sigma_y = \mathbf{345\ MPa}$$

The load that produces that stress in a section of 130 mm² follows from $\sigma = F/A_0$:

$$F_{max} = \sigma_{max}\,A_0 = 345\ \frac{\text{N}}{\text{mm}^2}\times130\ \text{mm}^2 = 44\,850\ \text{N} = \mathbf{44.85\ kN}$$

### c) Maximum length without plastic deformation
The strain at the yield strength comes from Hooke's law:

$$\varepsilon_y = \frac{\sigma_y}{E} = \frac{345\ \text{N/mm}^2}{103000\ \text{N/mm}^2} = 3.3495\times 10^{-3}$$

The elongation of a sample of 76 mm is

$$\Delta l = \varepsilon_y\,l_0 = 3.3495\times 10^{-3}\times76\ \text{mm} = 0.2546\ \text{mm}$$

and the maximum length that it can reach without plastic deformation is

$$l = l_0 + \Delta l = 76 + 0.2546 = \mathbf{76.255\ mm}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** (N/mm²)·mm² = N for the load; (N/mm²)/(N/mm²) has no units for the strain; strain × mm = mm for the elongation.
- **Order of magnitude.** $\varepsilon_y = 0.335$ %, a few tenths of a percent, the order of magnitude of the elastic strain of a metal.
- **Limit.** If the load were zero, $l = l_0 = 76$ mm. At the yield load, the sample is only 0.25 mm longer, that is, 0.33 % of its length.

### Interpretation
Up to $44.85$ kN the sample returns to 76 mm when unloaded. Beyond that load part of the elongation is permanent. The brass elongates very little (a quarter of a millimetre) before it yields: the yield strength is a stress limit, but it translates into a small strain because $E$ is large.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a. $\sigma_y$ | 345 MPa | 345 MPa | agrees |
| b. $\sigma_{max}$, $F_{max}$ | 345 MPa, 44 850 N | 345 MPa, 44\,850 N | agrees |
| c. $l$ | 76.25 mm | 76.25 mm | agrees |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Yield Strength and the 0.2 Percent Offset]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
