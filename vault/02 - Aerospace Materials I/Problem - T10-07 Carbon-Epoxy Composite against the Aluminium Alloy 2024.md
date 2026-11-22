---
materia: "Aerospace Materials I"
tema: "Topic 10: Composite Materials"
origen: "Problems T10_CompositeMaterials.pdf, Problem 7"
dificultad: easy
badge: "Density · weight fraction · weight saving against Al 2024"
tags:
  - official-problem
  - solved
  - rule-of-mixtures
  - weight-saving
  - isostrain
  - aluminium-replacement
---

# ✏️ Problem: T10-07 — Carbon-Epoxy Composite against the Aluminium Alloy 2024

## 📄 Official Statement
> 7. A composite material is composed of an epoxy matrix and 68% in volume of unidirectional continuous carbon fibers. Calculate:
> a) The average density of the composite material.
> b) The weight percentage of the carbon fibers and the epoxy resin in the composite.
> If the composite material is substituted by an Aluminium alloy AL2024, calculate:
> c) The young's modulus of the composite material and the percentage change of the young's modulus with respect to the aluminium alloy. Assume isostrain conditions
> d) The weight change for a cylindrical bar of material with 1 cm² cross-sectional area and 1 m in length.
>
> | Material | Density (g/cm³) | E (GPa) |
> | :--- | ---: | ---: |
> | Epoxy resin | 1.2 | 3.0 |
> | Carbon fiber | 1.79 | 220 |
> | Al2024 | 2.28 | 73.4 |
>
> *(Solution: a) 1.601 g/cm³; b) 76% fiber-24% resin; c) 105.1%; d) 67.9 g lighter, -29.8%)*

The sentence "If the composite material is substituted by an Aluminium alloy" is read, as the key does, as a comparison: the composite replaces the aluminium alloy, and the changes are those of the composite with respect to Al 2024.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Rule of mixtures** for the density, $\rho_c = V_f\rho_f + V_m\rho_m$ [Session 22 Slide 27], and the mass of a phase $m_i = \rho_i V_i$ (definition of density).
2. **Isostrain** modulus along the fibres, $E_{1C} = V_f E_f + (1 - V_f)E_m$ [Session 22 Slide 22].
3. **Same bar.** Composite and alloy bars have the same volume, $V = 1\ \text{cm}^2 \times 100\ \text{cm} = 100\ \text{cm}^3$, so their masses differ only through the density.
4. The density of Al 2024 is used as printed on the sheet (2.28 g/cm³).

### Data
| Quantity | Value |
| :--- | ---: |
| $V_f$, $V_m$ | 0.68, 0.32 |
| $\rho_f$, $\rho_m$ | 1.79, 1.2 g/cm³ |
| $E_f$, $E_m$ | 220, 3.0 GPa |
| $\rho_{Al}$, $E_{Al}$ | 2.28 g/cm³, 73.4 GPa |

**Unknowns:** (a) $\rho_c$; (b) $w_f$, $w_m$; (c) $E_{1C}$ and its change against Al 2024; (d) the mass change of the bar.

---

## 🧠 2. Model and Strategy

[Session 22 Slides 22, 27]:

$$\rho_c = V_f\rho_f + V_m\rho_m \qquad w_f = \frac{V_f\rho_f}{\rho_c} \qquad E_{1C} = V_f E_f + V_m E_m \qquad \Delta = \frac{X_c - X_{Al}}{X_{Al}}$$

**Strategy.** Density and weight fractions from the masses in 1 cm³; modulus by isostrain; relative changes with respect to the alloy; masses of the two bars from their common volume.

---

## 🔢 3. Step-by-Step Derivation

### 1. a) Density [Session 22 Slide 27]

$$\rho_c = 0.68 \times 1.79 + 0.32 \times 1.2 = 1.2172 + 0.3840 = \mathbf{1.601\ g/cm^3}$$

### 2. b) Weight fractions
The two terms of the density are the masses of fibre and epoxy in 1 cm³:

$$w_f = \frac{1.2172}{1.6012} = 0.760 \ \Rightarrow\ \mathbf{76\ \%\ fibre} \qquad w_m = \frac{0.3840}{1.6012} = 0.240 \ \Rightarrow\ \mathbf{24\ \%\ resin}$$

### 3. c) Modulus and change with respect to Al 2024 [Session 22 Slide 22]

$$E_{1C} = 0.68 \times 220\ \text{GPa} + 0.32 \times 3.0\ \text{GPa} = 149.6 + 0.96 = \mathbf{150.6\ GPa}$$

$$\Delta E = \frac{150.56 - 73.4}{73.4} = \frac{77.16}{73.4} = 1.051 \ \Rightarrow\ \mathbf{+105.1\ \%}$$

The composite is about twice as stiff as the alloy along the fibres.

### 4. d) Mass change of the bar
Volume $V = 1\ \text{cm}^2 \times 100\ \text{cm} = 100\ \text{cm}^3$:

$$m_c = 1.6012\ \text{g/cm}^3 \times 100\ \text{cm}^3 = 160.12\ \text{g} \qquad m_{Al} = 2.28\ \text{g/cm}^3 \times 100\ \text{cm}^3 = 228.0\ \text{g}$$

$$\Delta m = 160.12 - 228.0 = \mathbf{-67.9\ g} \qquad \frac{\Delta m}{m_{Al}} = \frac{-67.88}{228.0} = \mathbf{-29.8\ \%}$$

The composite bar is 67.9 g lighter.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** g/cm³ × cm³ = g; percentages are ratios of equal units.
- **Bounds.** $1.2 < 1.601 < 1.79$ g/cm³; $3 < 150.6 < 220$ GPa.
- **Specific modulus.** Composite $150.56/1.601 = 94.0$ GPa cm³/g against the alloy $73.4/2.28 = 32.2$ GPa cm³/g: 2.9 times higher along the fibres.
- **Same composite as T10-01.** Parts a) and b) repeat [[Problem - T10-01 Weight Fractions Density and Modulus of a Carbon-Epoxy Composite|T10-01]] (same fractions and densities), and give the same values.

### Interpretation
Replacing the alloy by the unidirectional composite doubles the stiffness and saves about 30 % of the mass (with the printed density of the alloy). The gain holds only along the fibres: across them the modulus falls towards the matrix value (isostress, [Session 22 Slide 24]), which is why real parts are laminated in several orientations [Session 21 Slide 37].

> [!note] Density of Al 2024 on the sheet
> The sheet prints 2.28 g/cm³ for Al 2024, and the key uses it. Handbook values for aluminium alloys of the 2xxx series are close to 2.78 g/cm³ (extension, not on the slides); with that value the saving would be $160.12 - 278.0 = -117.9$ g, that is $-42.4\ \%$. The solution above keeps the printed datum.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| a) $\rho_c$ | 1.601 g/cm³ | 1.601 g/cm³ | agrees |
| b) $w_f$, $w_m$ | 76% fiber-24% resin | 76.0 %, 24.0 % | agrees |
| c) $\Delta E$ | 105.1% | +105.1 % ($E_{1C} = 150.6$ GPa) | agrees |
| d) $\Delta m$ | 67.9 g lighter, -29.8% | $-67.9$ g, $-29.8$ % | agrees |

## 🔗 Related Links
* [[Topic 10 - Composite Materials|Topic 10: Composite Materials]]
* [[Problem - T10-01 Weight Fractions Density and Modulus of a Carbon-Epoxy Composite|Problem T10-01]]
* [[Problem - T10-11 Lighter Replacements for a Titanium Part|Problem T10-11]]
