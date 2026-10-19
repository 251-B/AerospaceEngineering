---
materia: "Aerospace Materials I"
tema: "Topic 5: Mechanical Properties"
origen: "Problems T5_MechanicalProperties.pdf, Problem 11"
dificultad: easy
badge: "Hooke's law · Poisson's ratio"
tags:
  - official-problem
  - solved
  - hooke-law
  - poisson-ratio
  - elastic-deformation
---

# ✏️ Problem: T5-11 — Elastic Deformation of a 15 mm Steel Cylinder under 50 kN

## 📄 Official Statement
> 11. A cylindrical steel sample with a diameter of 15 mm and a length of 250 mm experiences elastic deformation when a load of 50 kN is applied. Considering that for this steel E = 207 GPa and ν = 0.27, determine the elongation in the direction of the force applied and the change in diameter of the sample.
>
> *(Solution: $\Delta l = 0.342$ mm, $\Delta\phi = -0.0055$ mm)*

---

## 📊 1. Phase 1: Hypotheses and Parameters

### Hypotheses
1. **Elastic deformation.** The statement says that the load produces only elastic deformation, so Hooke's law holds, $\sigma = E\varepsilon$ [Session 11 Slide 13].
2. **Uniaxial, uniform stress** along the axis of the cylinder: $\sigma = F/A_0$ and $\varepsilon = \Delta l/l_0$ [Session 11 Slide 9].
3. **Isotropic material.** With a uniaxial stress, the transverse strain is $\varepsilon_{lat} = -\nu\,\varepsilon_{ax}$, equal in the two transverse directions [Session 11 Slide 19].
4. The cross-section is circular and uniform, so that the diameter changes in the same proportion in every direction of the section.

### Data
| Quantity | Symbol | Value | In SI |
| :--- | :--- | ---: | ---: |
| Load | $F$ | 50 000 N | 50 000 N |
| Diameter | $d_0$ | 15.0 mm | $15.0\times10^{-3}$ m |
| Length | $l_0$ | 250 mm | $250\times10^{-3}$ m |
| Young's modulus | $E$ | 207 GPa | 207 000 N/mm² |
| Poisson's ratio | $\nu$ | 0.27 | |

**Unknowns:** the elongation $\Delta l$ in the direction of the force and the change of the diameter $\Delta d$.

---

## 🧠 2. Phase 2: Frames and Strategy

One direction for the load (the axis) and the two equal transverse directions of the cylinder; no change of basis.

![[attachments/T5/t5-axial-bar.svg]]

**Strategy.** The elongation follows from the stress and the modulus, and the contraction of the diameter follows from the same strain through Poisson's ratio [Session 11 Slide 19]:

$$\sigma = \frac{F}{A_0} \qquad \varepsilon_{ax} = \frac{\sigma}{E} \qquad \Delta l = \varepsilon_{ax}\,l_0 \qquad \varepsilon_{lat} = -\nu\,\varepsilon_{ax} \qquad \Delta d = \varepsilon_{lat}\,d_0$$

The minus sign says that the diameter decreases when the sample is stretched.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Cross-section
$$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi\,(15.0\ \text{mm})^2}{4}$$

The square is $15.0^2 = 225.00$, then $\pi\times225.00 = 706.86$ and dividing by 4:

$$A_0 = 176.71\ \text{mm}^2$$

### 2. Stress and axial strain
$$\sigma = \frac{F}{A_0} = \frac{50\,000\ \text{N}}{176.71\ \text{mm}^2} = 282.94\ \text{MPa}$$

$$\varepsilon_{ax} = \frac{\sigma}{E} = \frac{282.94\ \text{N/mm}^2}{207000\ \text{N/mm}^2} = 1.3669\times 10^{-3}$$

### 3. Elongation in the direction of the force
$$\Delta l = \varepsilon_{ax}\,l_0 = 1.3669\times 10^{-3}\times250\ \text{mm} = \mathbf{0.342\ mm}$$

### 4. Change of the diameter
The transverse strain is

$$\varepsilon_{lat} = -\nu\,\varepsilon_{ax} = -0.27\times1.3669\times 10^{-3} = -3.6905\times 10^{-4}$$

and the change of the diameter is

$$\Delta d = \varepsilon_{lat}\,d_0 = -3.6905\times 10^{-4}\times15.0\ \text{mm} = \mathbf{-0.00554\ mm}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** (N/mm²)/(N/mm²) has no units for the strains, and strain × mm gives mm for $\Delta l$ and $\Delta d$.
- **Elastic range.** $\varepsilon_{ax} = 0.1367$ %, a small strain of the order of those of the elastic deformation of a metal, consistent with the statement.
- **Volume.** The relative change of volume is $\Delta V/V \approx \varepsilon_{ax} + 2\varepsilon_{lat} = \varepsilon_{ax}(1 - 2\nu) = 6.288\times 10^{-4}$, positive: a stretched elastic body increases its volume since $\nu < 0.5$ (a perfectly incompressible material, $\nu = 0.5$, would give zero) [Session 11 Slide 19].
- **Sign.** $\Delta l > 0$ and $\Delta d < 0$: the sample gets longer and thinner.

### Interpretation
The sample elongates by 0.342 mm, about a third of a millimetre in 250 mm, and the diameter shrinks by only 5.54 micrometres. The contraction is a fraction $\nu = 0.27$ of the relative elongation, which is why it is so small and why it is difficult to measure directly.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $\Delta l$ | 0.342 mm | 0.342 mm | agrees |
| $\Delta d$ | −0.0055 mm | -0.0055 mm | agrees |

## 🔗 Related Links
* [[Topic 5 - Mechanical Properties]]
* [[Concept - Poisson's Ratio and the Shear Modulus]]
* [[Concept - Hooke's Law, Young's Modulus and Non-Linear Elasticity]]
