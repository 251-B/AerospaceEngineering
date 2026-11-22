---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 1"
dificultad: easy
badge: "Weight fraction · density · isostrain modulus"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - volume-fraction
  - weight-fraction
  - isostrain
---

# ✏️ Problem: T10-01 — Weight Fractions, Density and Modulus of a Carbon-Epoxy Composite

## 📄 Official Statement
> 1. A composite material has an epoxy matrix reinforced with 68% in volume of unidirectional carbon fiber. The density of carbon fiber is 1.79 g/cm³ and of the epoxy resin is 1.20 g/cm³.
> a) What's the percentage in weight of the carbon fibers and the epoxy resin?
> b) What's the average density of the composite?
> c) If the average density of the composite is 1.65 g/cm³, what's the percentage in volume of the carbon fibers inside the material?
> d) Which of the two materials has a higher Elastic modulus? Calculate its value.
>
> Data: E_FC = 400 GPa and E_epoxy = 3 GPa. Assume isostrain conditions.
>
> *(Solution: a) 76%; b) 1.6 g/cm³; c) 76%; d) 304.7 GPa)*

"The two materials" of part d) are the two composites of the statement: the one with 68 vol% fibres (parts a and b) and the one whose density is 1.65 g/cm³ (part c).

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Two phases, no porosity.** The composite is fibre plus matrix only, so $V_f + V_m = 1$.
2. **Rule of mixtures.** A property of the composite is the volume-weighted sum of the properties of its phases, $P_{CM} = \sum_i f_i p_i$ with $\sum_i f_i = 1$ [Session 22 Slide 27]; for the density, $\rho_c = V_f\rho_f + V_m\rho_m$.
3. **Mass of a phase.** By the definition of density, the mass of each phase in a volume $V_c$ of composite is $m_i = \rho_i V_i = \rho_i f_i V_c$, so the weight fraction is $w_f = V_f\rho_f/\rho_c$.
4. **Isostrain.** Load along the continuous, aligned fibres with a perfect bond: $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22, Eq. 1].

### Data
| Quantity | Value |
| :--- | ---: |
| $V_f$ (parts a, b) | 0.68 |
| $\rho_f$ (carbon fibre) | 1.79 g/cm³ |
| $\rho_m$ (epoxy) | 1.20 g/cm³ |
| $\rho_c$ (part c) | 1.65 g/cm³ |
| $E_f$, $E_m$ | 400 GPa, 3 GPa |

**Unknowns:** (a) $w_f$, $w_m$; (b) $\rho_c$; (c) $V_f$ when $\rho_c = 1.65$ g/cm³; (d) which composite is stiffer and its $E_{1C}$.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 27]:

$$\rho_c = V_f\rho_f + (1 - V_f)\rho_m \qquad w_f = \frac{V_f\rho_f}{\rho_c} \qquad E_{1C} = V_f E_f + (1 - V_f)E_m$$

**Strategy.**
1. Work with $1\ \text{cm}^3$ of composite: the mass of each phase is $\rho_i V_i$; their sum is $\rho_c$ (part b) and their ratio gives the weight fractions (part a).
2. Invert the density rule of mixtures for $V_f$ (part c).
3. Apply the isostrain rule to both composites and compare (part d).

---

## 🔢 3. Step-by-Step Derivation

### 1. a) and b) Masses in 1 cm³ of composite [Session 22 Slide 27]
In $1\ \text{cm}^3$ there are $0.68\ \text{cm}^3$ of fibre and $0.32\ \text{cm}^3$ of epoxy:

$$m_f = 0.68\ \text{cm}^3 \times 1.79\ \text{g/cm}^3 = 1.2172\ \text{g} \qquad m_m = 0.32\ \text{cm}^3 \times 1.20\ \text{g/cm}^3 = 0.3840\ \text{g}$$

Their sum is the mass of $1\ \text{cm}^3$ of composite, which is the density of part b):

$$\rho_c = 1.2172\ \text{g} + 0.3840\ \text{g} = 1.6012\ \text{g in } 1\ \text{cm}^3 \ \Rightarrow\ \mathbf{\rho_c = 1.60\ g/cm^3}$$

Weight fractions:

$$w_f = \frac{1.2172\ \text{g}}{1.6012\ \text{g}} = 0.760 \ \Rightarrow\ \mathbf{76.0\ \%\ \text{carbon fibre}} \qquad w_m = \frac{0.3840\ \text{g}}{1.6012\ \text{g}} = 0.240 \ \Rightarrow\ \mathbf{24.0\ \%\ \text{epoxy}}$$

### 2. c) Volume fraction from the density [Session 22 Slide 27]
Writing $V_m = 1 - V_f$ in the density rule and solving for $V_f$:

$$\rho_c = V_f\rho_f + (1 - V_f)\rho_m = \rho_m + V_f(\rho_f - \rho_m) \ \Rightarrow\ V_f = \frac{\rho_c - \rho_m}{\rho_f - \rho_m}$$

$$V_f = \frac{1.65 - 1.20}{1.79 - 1.20} = \frac{0.45\ \text{g/cm}^3}{0.59\ \text{g/cm}^3} = 0.763 \ \Rightarrow\ \mathbf{76.3\ vol\%\ \text{carbon fibre}}$$

### 3. d) Isostrain modulus of the two composites [Session 22 Slide 22]
Composite of parts a) and b), $V_f = 0.68$:

$$E_{1C} = 0.68 \times 400\ \text{GPa} + 0.32 \times 3\ \text{GPa} = 272.0 + 0.96 = 272.96\ \text{GPa}$$

Composite of part c), $V_f = 0.7627$:

$$E_{1C} = 0.7627 \times 400\ \text{GPa} + 0.2373 \times 3\ \text{GPa} = 305.08 + 0.71 = 305.8\ \text{GPa}$$

**Answer:** the composite of part c), with more fibre, is the stiffer one: $\mathbf{E_{1C} \approx 306\ GPa}$ (against 273 GPa for the 68 vol% composite).

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $V_f$ and $w_f$ are dimensionless; $\rho_c$ is a volume-weighted sum of densities, in g/cm³; $E_{1C}$ is a sum of moduli, in GPa.
- **Bounds.** $1.20 < 1.60 < 1.79$ g/cm³ and $3 < 273 < 400$ GPa: each mixture value lies between those of its phases.
- **Weight against volume.** The fibre is the denser phase, so its weight fraction (76.0 %) is larger than its volume fraction (68 %).
- **Back-substitution.** $0.7627 \times 1.79 + 0.2373 \times 1.20 = 1.650$ g/cm³, the density given in c).
- **Limit.** For $V_f \to 1$ the modulus tends to $E_f = 400$ GPa; with $E_f \gg E_m$ the matrix adds less than 1 GPa, which is why $E_{1C} \approx V_f E_f$ [Session 22 Slide 22].

### Interpretation
Because the modulus along the fibres is almost proportional to $V_f$, the composite of part c), with 8 more volume percent of fibre, is 12 % stiffer and only 3 % denser. This is the reason aerospace laminates are made with as high a fibre fraction as processing allows.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $w_f$ | 76% | 76.0 % fibre, 24.0 % epoxy | agrees |
| b) $\rho_c$ | 1.6 g/cm³ | 1.601 g/cm³ | agrees |
| c) $V_f$ | 76% | 76.3 vol% | agrees |
| d) $E$ | 304.7 GPa | 305.8 GPa (composite of part c) | agrees within rounding: the key uses $V_f = 0.76$, and $0.76 \times 400 + 0.24 \times 3 = 304.7$ GPa |

The key value 304.7 GPa is the modulus of the composite of part c) with $V_f$ rounded to 0.76, not the modulus of the 68 vol% composite (273.0 GPa); this is consistent with reading part d) as a comparison of the two composites of the statement.

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-07 Carbon-Epoxy Composite against the Aluminium Alloy 2024|Problem T10-07]]
