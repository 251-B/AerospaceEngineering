---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 7"
dificultad: medium
badge: "MgO rock salt · densities"
tags:
  - official-problem
  - solved
  - rock-salt
  - density
  - packing-factor
  - linear-density
  - planar-density
---

# ✏️ Problem: T8-07 — MgO (Rock Salt): Cell Volume, Packing Factor, Linear, Planar and Volumetric Densities

## 📄 Official Statement
> 7- Considering that MgO crystallizes in a NaCl-type structure, determine:
> DATA: r(Mg²⁺) = 0,078 nm; r(O²⁻) = 0,132 nm; M(MgO) = 40 g/mol; $N_A$ = 6,023·10²³ átomos/mol
> a) The volume of the unit cell
> b) The packing factor
> c) The linear density (in ions/nm) in the [111] direction
> d) The planar density (in ions/nm²) in the (111) plane
> e) The volumetric density (in g/cm³)
>
> *(Solution: a) V = 0.074 nm³; b) f = 0.63; c) ρ[111] = 2.75 ions/nm; d) ρ(111) = 13.1 ions/nm²; e) ρv = 3.59 g/cm³)*

The sheet prints the volume of the key as "V = 0.074nm", with the unit nm; a volume is in nm³. It writes Avogadro's number with decimal commas and in Spanish, "6,023·10²³ átomos/mol".

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Structure.** O²⁻ on the FCC lattice points, Mg²⁺ in all the octahedral sites (edge midpoints and body centre); 4 Mg²⁺ and 4 O²⁻ per cell [Session 16 Slide 8]. The ratio $r_{Mg}/r_O = 0.078/0.132 = 0.591$ is in the octahedral range 0.414-0.732 [Session 16 Slide 6].
2. **Contact** of cation and anion along the edge: $a = 2(r_{Mg} + r_O)$.
3. $\rho = 4M_{MgO}/(V N_A)$ with the $N_A = 6.023\times10^{23}$ mol⁻¹ of the sheet.

### Data
| Quantity | Value |
| :--- | ---: |
| $r_{Mg}$, $r_O$ | 0.078, 0.132 nm |
| $M_{MgO}$ | 40 g/mol |
| $N_A$ | $6.023\times10^{23}$ mol⁻¹ |

**Unknowns:** $V$, $f$, $\rho_L[111]$, $\rho_P(111)$, $\rho_v$.

---

## 🧠 2. Model and Strategy

Edge from the contact; packing factor with 4 + 4 ions; count the ions on the body diagonal and in the (111) triangle; density with four formula units.

---

## 🔢 3. Step-by-Step Derivation

### 1. Volume of the cell
$$a = 2(r_{Mg} + r_O) = 2\times(0.078 + 0.132)\ \text{nm} = 0.420\ \text{nm}$$

$$V = a^3 = (0.420\ \text{nm})^3 = \mathbf{0.0741\ nm^3}$$

### 2. Packing factor
$$V_{Mg} = \tfrac43\pi(0.078\ \text{nm})^3 = 1.9878\times10^{-3}\ \text{nm}^3 \qquad V_O = \tfrac43\pi(0.132\ \text{nm})^3 = 9.6341\times10^{-3}\ \text{nm}^3$$

$$f = \frac{4(V_{Mg} + V_O)}{V} = \frac{4\times(1.9878 + 9.6341)\times10^{-3}\ \text{nm}^3}{0.074088\ \text{nm}^3} = \frac{0.046488\ \text{nm}^3}{0.074088\ \text{nm}^3} = \mathbf{0.627}$$

### 3. Linear density along [111]
Body diagonal, length $a\sqrt3 = 0.420\times1.7321 = 0.72746$ nm. On it: O²⁻ at the two corners ($2\times\frac12 = 1$) and Mg²⁺ at the body centre (1). Two ions:

$$\rho_L[111] = \frac{2\ \text{ions}}{0.72746\ \text{nm}} = \mathbf{2.75\ ions/nm}$$

### 4. Planar density in (111)
Triangle $(1,0,0)$, $(0,1,0)$, $(0,0,1)$, of area $\frac{\sqrt3}{2}a^2 = 0.8660\times(0.420\ \text{nm})^2 = 0.15277$ nm². It holds only O²⁻: three corners ($3\times\frac16$) and three face centres ($3\times\frac12$), 2 ions. The Mg²⁺ ions at the edge midpoints, such as $(\frac12,0,0)$, have $x+y+z = \frac12$, and the body centre $\frac32$: they lie in the parallel planes between the oxygen layers.

$$\rho_P(111) = \frac{2\ \text{ions}}{0.15277\ \text{nm}^2} = \mathbf{13.1\ ions/nm^2}$$

### 5. Volumetric density
$$m_{cell} = \frac{4M_{MgO}}{N_A} = \frac{4\times40\ \text{g/mol}}{6.023\times10^{23}\ \text{mol}^{-1}} = 2.6565\times10^{-22}\ \text{g}$$

$$\rho_v = \frac{2.6565\times10^{-22}\ \text{g}}{0.074088\times10^{-21}\ \text{cm}^3} = \mathbf{3.59\ g/cm^3}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **No anion overlap.** O-O along the face diagonal: $a\sqrt2/2 = 0.297$ nm $> 2r_O = 0.264$ nm, so the Mg-O contact sets the edge.
- **Units.** nm³; dimensionless $f$; ions/nm, ions/nm²; g/cm³ with $1\ \text{nm}^3 = 10^{-21}$ cm³.
- **Physical value.** 3.59 g/cm³ is the known density of periclase, MgO (about 3.58 g/cm³, extension).

### Interpretation
Rock salt is two interpenetrating FCC lattices, one of each ion, shifted by half an edge. Along the body diagonal the ions alternate O-Mg-O-Mg at steps of $a\sqrt3/2$, and the (111) planes are alternately all-oxygen and all-magnesium layers, which is why a (111) plane of the cell contains a single kind of ion.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $V$ | 0.074 (printed in nm) | 0.0741 nm³ | agrees; the unit of the key should read nm³ |
| $f$ | 0.63 | 0.627 | agrees |
| $\rho_L[111]$ | 2.75 ions/nm | 2.75 ions/nm | agrees |
| $\rho_P(111)$ | 13.1 ions/nm² | 13.1 ions/nm² | agrees |
| $\rho_v$ | 3.59 g/cm³ | 3.59 g/cm³ | agrees |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Problem - T8-05 Rock Salt Structure AB from Two Planes|Problem T8-05]]
