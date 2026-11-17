---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 8"
dificultad: medium
badge: "Masses to volume fractions · isostrain and isostress"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - isostress
  - metal-matrix-composite
---

# ✏️ Problem: T10-08 — Boron-Aluminium Composite: Density and Longitudinal and Transverse Moduli

## 📄 Official Statement
> 8. Five kilograms of continuous boron fibers are introduced in a unidirectional orientation into 8 kg of an aluminum matrix. Calculate
> a) The density of the composite.
> b) The modulus of elasticity parallel to the fibers.
> c) The modulus of elasticity perpendicular to the fibers.
>
> Data: E_Al = 70 GPa; ρ_Al = 2.7 g/cm³; E_Boron = 380 GPa; ρ_Boron = 2.3 g/cm³.
>
> *(Solution: a) 2.530 g/cm³; b) 201.1×10³ MPa; c) 106.4×10³ MPa)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Volumes from masses.** $V_i = m_i/\rho_i$; the composite has no porosity, so its volume is the sum of the two.
2. **Parallel to the fibres: isostrain**, $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22, Eq. 1].
3. **Perpendicular to the fibres: isostress**, the same stress in both phases and strains that add, $1/E_{2C} = V_f/E_f + V_m/E_m$ [Session 22 Slide 24, Eq. 2]. The boron fibre is taken as isotropic, so its transverse modulus $E'_f$ equals 380 GPa.

### Data
| Constituent | Mass (kg) | $\rho$ (g/cm³) | $E$ (GPa) |
| :--- | ---: | ---: | ---: |
| Boron fibre (f) | 5 | 2.3 | 380 |
| Aluminium (m) | 8 | 2.7 | 70 |

**Unknowns:** $\rho_c$, $E_{1C}$, $E_{2C}$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 24, 27]:

$$\rho_c = \frac{m_f + m_m}{V_f + V_m} \qquad E_{1C} = V_f E_f + V_m E_m \qquad \frac{1}{E_{2C}} = \frac{V_f}{E_f} + \frac{V_m}{E_m}$$

**Strategy.** Volumes of the two phases → volume fractions → density; then the upper (isostrain) and lower (isostress) rules.

---

## 🔢 3. Step-by-Step Derivation

### 1. Volumes and volume fractions
With 5 kg = 5000 g and 8 kg = 8000 g:

$$V_B = \frac{5000\ \text{g}}{2.3\ \text{g/cm}^3} = 2173.9\ \text{cm}^3 \qquad V_{Al} = \frac{8000\ \text{g}}{2.7\ \text{g/cm}^3} = 2963.0\ \text{cm}^3 \qquad V_c = 5136.9\ \text{cm}^3$$

$$V_f = \frac{2173.9}{5136.9} = 0.4232 \qquad V_m = \frac{2963.0}{5136.9} = 0.5768$$

### 2. a) Density [Session 22 Slide 27]

$$\rho_c = \frac{13\,000\ \text{g}}{5136.9\ \text{cm}^3} = \mathbf{2.531\ g/cm^3}$$

The rule of mixtures gives the same: $0.4232 \times 2.3 + 0.5768 \times 2.7 = 0.9734 + 1.5574 = 2.531$ g/cm³.

### 3. b) Modulus parallel to the fibres [Session 22 Slide 22]

$$E_{1C} = 0.4232 \times 380\ \text{GPa} + 0.5768 \times 70\ \text{GPa} = 160.82 + 40.38 = \mathbf{201.2\ GPa} = 201.2\times10^3\ \text{MPa}$$

### 4. c) Modulus perpendicular to the fibres [Session 22 Slide 24]

$$\frac{1}{E_{2C}} = \frac{0.4232}{380\ \text{GPa}} + \frac{0.5768}{70\ \text{GPa}} = 0.0011137 + 0.0082400 = 0.0093537\ \text{GPa}^{-1}$$

$$E_{2C} = \frac{1}{0.0093537\ \text{GPa}^{-1}} = \mathbf{106.9\ GPa} = 106.9\times10^3\ \text{MPa}$$

The closed form of the slide gives the same: $E_{2C} = E_f E_m/(V_f E_m + V_m E_f) = (380 \times 70)/(0.4232 \times 70 + 0.5768 \times 380) = 26\,600/248.81 = 106.9$ GPa.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** g/cm³ from g over cm³; in the isostress rule each term is dimensionless over GPa, so $1/E_{2C}$ is in GPa⁻¹.
- **Bounds.** $E_m = 70 < E_{2C} = 106.9 < E_{1C} = 201.2 < E_f = 380$ GPa: the isostress value is the lower bound and the isostrain value the upper bound [Session 22 Slides 25, 28].
- **Density.** Boron is lighter than aluminium here, so adding fibre lowers the density (2.531 < 2.7 g/cm³) while it nearly triples the stiffness along the fibres.

### Interpretation
Across the fibres the compliant aluminium layers deform the most and control the response, so $E_{2C}$ is only half of $E_{1C}$. The anisotropy is milder than in polymer composites ($E_f/E_m = 5.4$ here against about 100 for carbon-epoxy), because the metal matrix is itself stiff: one of the reasons boron-aluminium is used in structural MMC parts such as the DC-10 aft pylon skin [Session 23 Slide 47].

> [!warning] Discrepancy with the official solution
> The key gives $106.4\times10^3$ MPa for part c). With the volume fraction of part a), $V_f = 0.4232$, the isostress rule gives $106.9\times10^3$ MPa (the bracket is written out above). The key value corresponds to $V_f = (1/70 - 1/106.4)/(1/70 - 1/380) = 0.419$, which does not follow from the data (5 kg of boron at 2.3 g/cm³ in 8 kg of aluminium at 2.7 g/cm³), so the computed $106.9\times10^3$ MPa is kept. The difference is 0.5 %.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $\rho_c$ | 2.530 g/cm³ | 2.531 g/cm³ | agrees |
| b) $E_{1C}$ | 201.1×10³ MPa | 201.2×10³ MPa | agrees |
| c) $E_{2C}$ | 106.4×10³ MPa | 106.9×10³ MPa | differs by 0.5 % (see the warning) |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-11 Lighter Replacements for a Titanium Part|Problem T10-11]]
