---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 9"
dificultad: medium
badge: "Design for a modulus · volume to mass"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - composite-design
  - weight-fraction
---

# ✏️ Problem: T10-09 — Mass of Carbon Fibres for a Carbon-Polyimide Composite

## 📄 Official Statement
> 9. We want to produce 5 kg of a continuous unidirectional fiber-reinforced composite of HS (High Strength) carbon in a polyimide matrix that has a modulus of elasticity of at least 172×10³ MPa parallel to the fibers. How many kilograms of fibers are required?
>
> Data: E_carbon fiber = 276×10³ MPa; E_PI = 2070 MPa; ρ_carbon fiber = 1.75 g/cm³; ρ_PI = 1.39 g/cm³.
>
> *(Solution: 3.37 Kg)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Isostrain** parallel to the continuous fibres: $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22, Eq. 1].
2. **Minimum fibre content.** $E_{1C}$ grows with $V_f$, so the least fibre that meets the requirement is the one that gives exactly $E_{1C} = 172\times10^3$ MPa.
3. **Mass fraction** $w_f = V_f\rho_f/\rho_c$ with $\rho_c = V_f\rho_f + V_m\rho_m$ [Session 22 Slide 27]; no porosity.

### Data
| Quantity | Value |
| :--- | ---: |
| $E_f$ (HS carbon) | $276\times10^3$ MPa |
| $E_m$ (polyimide) | 2070 MPa |
| $\rho_f$, $\rho_m$ | 1.75, 1.39 g/cm³ |
| $E_{1C,min}$ | $172\times10^3$ MPa |
| $m_c$ | 5 kg |

**Unknown:** $m_f$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 27]:

$$V_f = \frac{E_{1C} - E_m}{E_f - E_m} \qquad w_f = \frac{V_f\rho_f}{V_f\rho_f + V_m\rho_m} \qquad m_f = w_f\,m_c$$

**Strategy.** Invert the isostrain rule for $V_f$; convert the volume fraction into a mass fraction with the densities; multiply by the 5 kg of composite.

---

## 🔢 3. Step-by-Step Derivation

### 1. Volume fraction of fibre [Session 22 Slide 22]
Writing $V_m = 1 - V_f$ and solving the isostrain rule for $V_f$:

$$E_{1C} = E_m + V_f(E_f - E_m) \ \Rightarrow\ V_f = \frac{172\,000 - 2\,070}{276\,000 - 2\,070} = \frac{169\,930\ \text{MPa}}{273\,930\ \text{MPa}} = 0.6203$$

### 2. Mass fraction of fibre [Session 22 Slide 27]
Masses of fibre and matrix in 1 cm³ of composite:

$$V_f\rho_f = 0.6203 \times 1.75 = 1.0856\ \text{g} \qquad V_m\rho_m = 0.3797 \times 1.39 = 0.5278\ \text{g} \qquad \rho_c = 1.6134\ \text{g/cm}^3$$

$$w_f = \frac{1.0856}{1.6134} = 0.6729$$

### 3. Mass of fibres

$$m_f = 0.6729 \times 5\ \text{kg} = \mathbf{3.36\ kg}$$

and $5 - 3.36 = 1.64$ kg of polyimide.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $V_f$ is MPa/MPa and $w_f$ is (g/cm³)/(g/cm³), both dimensionless, so $m_f$ is in kg.
- **Back-substitution.** $0.6203 \times 276\,000 + 0.3797 \times 2\,070 = 171\,203 + 786 = 171\,989 \approx 172\,000$ MPa.
- **Weight against volume.** The fibre is the denser phase, so $w_f = 0.673 > V_f = 0.620$.
- **Feasibility.** $V_f = 62$ % is slightly above the 50 to 60 % of typical fibre composites [Session 22 Slide 22]: the requirement asks for a well-packed unidirectional composite.

### Interpretation
Because the matrix contributes less than 1 % of the modulus, the requirement is essentially $V_f \approx E_{1C}/E_f = 172/276 = 0.623$. A stiffer (HM) fibre would meet the same target with less fibre and a lighter part.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $m_f$ | 3.37 kg | 3.364 kg | agrees within 0.2 % (the key rounds $\rho_c$ to 1.61 g/cm³) |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-11 Lighter Replacements for a Titanium Part|Problem T10-11]]
