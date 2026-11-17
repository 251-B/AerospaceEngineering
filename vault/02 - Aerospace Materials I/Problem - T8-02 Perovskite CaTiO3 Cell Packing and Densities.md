---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 2"
dificultad: medium
badge: "Perovskite CaTiO₃ · densities"
tags:
  - official-problem
  - solved
  - perovskite
  - density
  - packing-factor
  - linear-density
  - planar-density
---

# ✏️ Problem: T8-02 — Perovskite (CaTiO₃): Cell Volume, Packing Factor, Linear, Planar and Volumetric Densities

## 📄 Official Statement
> 2- The Perovskite structure (CaTiO₃) can be described as an FCC packing of Ca²⁺ and O²⁻ ions on which Ti⁴⁺ occupies ¼ of the octahedral sites. Calculate:
> a) The volume of the unit cell.
> b) The packing factor.
> c) The linear density (ions/nm) in the direction [111].
> d) The planar density (ions/nm²) in the plane (111).
> e) The volumetric density expressed in g/cm³.
>
> Data: r(Ca²⁺) = 0.106 nm; r(O²⁻) = 0.132 nm; r(Ti⁴⁺) = 0.036 nm; M(Ca) = 40.08; M(O) = 16.00; M(Ti) = 47.90.
>
> *(Solution: a) V = 0.038 nm³; b) f = 0.897; c) ρ[111] = 3.44 ions/nm; d) ρ(111) = 20.4 ions/nm²; e) ρv = 5.95 g/cm³)*

The sheet prints "O² ions⁻" for O²⁻ ions.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Structure.** Ca²⁺ at the corners and O²⁻ at the face centres form together an FCC packing; Ti⁴⁺ sits in the octahedral site at the body centre, the only one of the four octahedral sites surrounded by six O²⁻. Per cell: 1 Ca²⁺, 3 O²⁻, 1 Ti⁴⁺ [Session 16 Slide 12].
2. **Contact.** In a close packing the spheres touch along the face diagonal, here a Ca²⁺ at a corner and the O²⁻ at the centre of the face: $a\sqrt2 = 2(r_{Ca} + r_O)$ [Session 16 Slide 12, FCC packing of Ca²⁺ and O²⁻].
3. **Density:** $\rho = \sum M/(V N_A)$, $N_A = 6.022\times10^{23}$ mol⁻¹ ([[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]).

### Data
| Quantity | Value |
| :--- | ---: |
| $r_{Ca}$, $r_O$, $r_{Ti}$ | 0.106, 0.132, 0.036 nm |
| $M_{Ca}$, $M_O$, $M_{Ti}$ | 40.08, 16.00, 47.90 g/mol |

**Unknowns:** $V$, $f$, $\rho_L[111]$, $\rho_P(111)$, $\rho_v$.

---

## 🧠 2. Model and Strategy

1. Edge from the Ca-O contact along the face diagonal; check that Ti⁴⁺ fits its octahedral hole.
2. Packing factor with the five ions of the cell.
3. Count the ions on the body diagonal and in the (111) triangle.
4. Density with one formula unit per cell.

---

## 🔢 3. Step-by-Step Derivation

### 1. Lattice parameter and volume
$$a = \frac{2(r_{Ca} + r_O)}{\sqrt2} = \frac{2\times(0.106 + 0.132)\ \text{nm}}{1.4142} = \frac{0.476\ \text{nm}}{1.4142} = 0.33658\ \text{nm}$$

$$V = a^3 = (0.33658\ \text{nm})^3 = \mathbf{0.0381\ nm^3}$$

Fit of Ti⁴⁺: along the edge direction the body-centre site is $a/2$ from the O²⁻ of each face centre, $a/2 = 0.16829$ nm, against $r_{Ti} + r_O = 0.036 + 0.132 = 0.168$ nm. The cation just touches the six oxygens, so the cell is consistent.

### 2. Packing factor
$$V_{Ca} = \tfrac43\pi(0.106)^3 = 4.9889\times10^{-3}\ \text{nm}^3 \qquad V_O = \tfrac43\pi(0.132)^3 = 9.6341\times10^{-3}\ \text{nm}^3 \qquad V_{Ti} = \tfrac43\pi(0.036)^3 = 1.954\times10^{-4}\ \text{nm}^3$$

$$f = \frac{V_{Ca} + 3V_O + V_{Ti}}{V} = \frac{(4.9889\times10^{-3} + 3\times9.6341\times10^{-3} + 1.954\times10^{-4})\ \text{nm}^3}{0.038131\ \text{nm}^3} = \frac{0.034087\ \text{nm}^3}{0.038131\ \text{nm}^3} = \mathbf{0.894}$$

### 3. Linear density along [111]
Body diagonal, length $a\sqrt3 = 0.33658\times1.7321 = 0.58298$ nm. On it: Ca²⁺ at both corners ($2\times\frac12 = 1$) and Ti⁴⁺ at the body centre (1). The O²⁻ ions sit at face centres, off the diagonal.

$$\rho_L[111] = \frac{2\ \text{ions}}{0.58298\ \text{nm}} = \mathbf{3.43\ ions/nm}$$

### 4. Planar density in (111)
Triangle $(1,0,0)$, $(0,1,0)$, $(0,0,1)$, of area $\frac{\sqrt3}{2}a^2 = 0.8660\times0.11329\ \text{nm}^2 = 0.098110$ nm². In it: Ca²⁺ at the three vertices ($3\times\frac16 = \frac12$) and O²⁻ at the three face centres on its sides, $(\frac12,\frac12,0)$ and the like ($3\times\frac12 = \frac32$). Ti⁴⁺ at $(\frac12,\frac12,\frac12)$ has $x+y+z = \frac32$ and lies outside. Total 2 ions:

$$\rho_P(111) = \frac{2\ \text{ions}}{0.098110\ \text{nm}^2} = \mathbf{20.4\ ions/nm^2}$$

### 5. Volumetric density
$$m_{cell} = \frac{M_{Ca} + M_{Ti} + 3M_O}{N_A} = \frac{(40.08 + 47.90 + 3\times16.00)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{135.98\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 2.2581\times10^{-22}\ \text{g}$$

$$\rho_v = \frac{2.2581\times10^{-22}\ \text{g}}{0.038131\times10^{-21}\ \text{cm}^3} = \mathbf{5.92\ g/cm^3}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** nm³ for $V$; $f$ dimensionless; ions/nm and ions/nm²; g/cm³ with $1\ \text{nm}^3 = 10^{-21}$ cm³.
- **Charge balance.** $+2 + 4 + 3\times(-2) = 0$ per cell.
- **Packing.** $f = 0.894$ is above the 0.74 of an FCC metal. It can be, because the Ti⁴⁺ ion fills an octahedral hole of the close packing of Ca²⁺ and O²⁻, which a metal leaves empty. The sum is a hard-sphere estimate: the Ca²⁺ ion is smaller than O²⁻, so the "close packing" of the two is itself an approximation.
- **Two contacts at once.** Both the Ca-O contact ($a = 0.3366$ nm) and the Ti-O contact ($a = 2\times0.168 = 0.336$ nm) give nearly the same edge, so the data describe an ideal perovskite.

### Interpretation
The large Ca²⁺ and the O²⁻ ions build the frame together, and the small, highly charged Ti⁴⁺ sits in the octahedron of oxygens at the centre; the same corner-sharing TiO₆ octahedra are those of Slide 12. The (111) planes hold Ca and O (composition CaO₃ per layer when extended), and the Ti⁴⁺ ions lie between them.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $V$ | 0.038 nm³ | 0.0381 nm³ | agrees |
| $f$ | 0.897 | 0.894 | the key divides by the rounded $V = 0.038$ nm³ (0.034087/0.038 = 0.897) |
| $\rho_L[111]$ | 3.44 ions/nm | 3.43 ions/nm | agrees within rounding (3.431) |
| $\rho_P(111)$ | 20.4 ions/nm² | 20.4 ions/nm² | agrees |
| $\rho_v$ | 5.95 g/cm³ | 5.92 g/cm³ | 0.5 % apart; with the rounded $V = 0.038$ nm³ the density is 5.94 g/cm³, so the key rounds an intermediate value |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Problem - T8-06 Perovskite SrSnO3 Linear and Planar Densities and Rod Mass|Problem T8-06]]
