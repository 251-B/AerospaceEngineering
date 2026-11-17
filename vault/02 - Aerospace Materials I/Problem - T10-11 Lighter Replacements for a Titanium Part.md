---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 11"
dificultad: medium
badge: "Equal stiffness · mass of the part · specific modulus"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - isostrain
  - specific-modulus
  - weight-saving
---

# ✏️ Problem: T10-11 — Lighter Replacements for a Titanium Part

## 📄 Official Statement
> 11. A titanium alloy with a modulus of elasticity of 110x10³ MPa is used to make a 450 kg part for a manned space vehicle. Determine the weight of a part having the same modulus of elasticity parallel to the fibers, if the part is made of:
> a) Aluminium reinforced with boron fibers.
> b) Polyester (with a modulus of 4500 MPa) reinforced with high modulus carbon fibers.
> c) Compare the specific modulus for all three materials.
>
> Data: ρ_Ti = 4.507 g/cm³; E_Al = 70 GPa; ρ_Al = 2.699 g/cm³; E_Boron = 380 GPa; ρ_Boron = 2.36 g/cm³; E_carbon fiber = 530x10³ MPa; ρ_carbon fiber = 1.9 g/cm³; ρ_polyester = 1.28 g/cm³.
>
> *(Solution: a) 265 kg b) 140.3 kg c) Ti Ti:24406 kN m/kg ; B-Al: 41431 kN m/kg ; C-PE: 78314 kN m/kg)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Same part, same volume.** The new part has the shape and size of the titanium part, so its volume is $V = m_{Ti}/\rho_{Ti}$ and its mass is $m = \rho_c V$.
2. **Same modulus parallel to the fibres.** Isostrain, $E_{1C} = V_f E_f + (1 - V_f)E_m = 110$ GPa [Session 22 Slide 22, Eq. 1]; the least fibre that reaches it is used.
3. **Density** by the rule of mixtures, $\rho_c = V_f\rho_f + V_m\rho_m$ [Session 22 Slide 27].
4. **Specific modulus** $E/\rho$ [Session 21 Slide 43], in N m/kg (= m²/s²).

### Data
| Material | $E$ (GPa) | $\rho$ (g/cm³) |
| :--- | ---: | ---: |
| Titanium alloy | 110 | 4.507 |
| Aluminium (matrix a) | 70 | 2.699 |
| Boron fibre | 380 | 2.36 |
| Polyester (matrix b) | 4.5 | 1.28 |
| HM carbon fibre | 530 | 1.9 |

$m_{Ti} = 450$ kg.

**Unknowns:** (a) $m_{B\text{-}Al}$; (b) $m_{C\text{-}PE}$; (c) $E/\rho$ of the three materials.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 27]:

$$V = \frac{m_{Ti}}{\rho_{Ti}} \qquad V_f = \frac{E_{Ti} - E_m}{E_f - E_m} \qquad \rho_c = V_f\rho_f + V_m\rho_m \qquad m = \rho_c V$$

**Strategy.** Volume of the part; for each composite, the fibre fraction that matches 110 GPa, its density and the mass of the part; finally the three specific moduli.

---

## 🔢 3. Step-by-Step Derivation

### 1. Volume of the part
With $\rho_{Ti} = 4.507\ \text{g/cm}^3 = 4507\ \text{kg/m}^3$:

$$V = \frac{450\ \text{kg}}{4507\ \text{kg/m}^3} = 0.099845\ \text{m}^3$$

### 2. a) Boron-aluminium [Session 22 Slides 22, 27]

$$V_f = \frac{110 - 70}{380 - 70} = \frac{40\ \text{GPa}}{310\ \text{GPa}} = 0.1290 \qquad \rho_c = 0.1290 \times 2.36 + 0.8710 \times 2.699 = 0.3045 + 2.3508 = 2.6553\ \text{g/cm}^3$$

$$m = 2655.3\ \text{kg/m}^3 \times 0.099845\ \text{m}^3 = \mathbf{265.1\ kg}$$

### 3. b) Carbon-polyester [Session 22 Slides 22, 27]

$$V_f = \frac{110 - 4.5}{530 - 4.5} = \frac{105.5\ \text{GPa}}{525.5\ \text{GPa}} = 0.2008 \qquad \rho_c = 0.2008 \times 1.9 + 0.7992 \times 1.28 = 0.3814 + 1.0230 = 1.4045\ \text{g/cm}^3$$

$$m = 1404.5\ \text{kg/m}^3 \times 0.099845\ \text{m}^3 = \mathbf{140.2\ kg}$$

### 4. c) Specific modulus [Session 21 Slide 43]
All three materials have $E = 110\times10^9$ Pa:

$$\left(\frac{E}{\rho}\right)_{Ti} = \frac{110\times10^9\ \text{N/m}^2}{4507\ \text{kg/m}^3} = 24.41\times10^6\ \text{N m/kg} = \mathbf{24\,406\ kN\,m/kg}$$

$$\left(\frac{E}{\rho}\right)_{B\text{-}Al} = \frac{110\times10^9}{2655.3} = \mathbf{41\,427\ kN\,m/kg} \qquad \left(\frac{E}{\rho}\right)_{C\text{-}PE} = \frac{110\times10^9}{1404.5} = \mathbf{78\,321\ kN\,m/kg}$$

| Material | $\rho$ (g/cm³) | Mass of the part (kg) | $E/\rho$ (kN m/kg) | Relative to Ti |
| :--- | ---: | ---: | ---: | ---: |
| Titanium alloy | 4.507 | 450 | 24 406 | 1.00 |
| Boron-aluminium | 2.655 | 265.1 | 41 427 | 1.70 |
| Carbon-polyester | 1.404 | 140.2 | 78 321 | 3.21 |

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** kg/(kg/m³) = m³; (kg/m³) × m³ = kg; (N/m²)/(kg/m³) = N m/kg.
- **Mass ratio.** At equal volume and modulus, $m/m_{Ti} = \rho_c/\rho_{Ti} = (E/\rho)_{Ti}/(E/\rho)_c$: $265.1/450 = 0.589 = 24\,406/41\,427$.
- **Fractions.** Both $V_f$ are well below 1 (0.13 and 0.20), so both composites are possible; the carbon fibre needs only 20 % because it is 4.8 times stiffer than the titanium.
- **Limit.** If the fibre modulus fell to 110 GPa, $V_f \to 1$ and the part would be made of fibre only.

### Interpretation
For a part designed for stiffness, the mass is inversely proportional to the specific modulus. The carbon-polyester part weighs less than a third of the titanium one (saving 310 kg), and the boron-aluminium part 59 %. This is the argument of the slides for composites in aerospace: high specific modulus and specific strength [Session 21 Slides 16, 43].

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $m_{B\text{-}Al}$ | 265 kg | 265.1 kg | agrees |
| b) $m_{C\text{-}PE}$ | 140.3 kg | 140.2 kg | agrees |
| c) $E/\rho$ | Ti 24406; B-Al 41431; C-PE 78314 kN m/kg | 24 406; 41 427; 78 321 kN m/kg | agrees within rounding of the densities |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-08 Boron-Aluminium Composite Density and Longitudinal and Transverse Moduli|Problem T10-08]]
* [[Problem - T10-07 Carbon-Epoxy Composite against the Aluminium Alloy 2024|Problem T10-07]]
