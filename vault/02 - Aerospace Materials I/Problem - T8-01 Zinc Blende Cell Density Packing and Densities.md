---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 1"
dificultad: medium
badge: "Zinc blende · density and packing"
tags:
  - official-problem
  - solved
  - zinc-blende
  - density
  - packing-factor
  - linear-density
  - planar-density
---

# ✏️ Problem: T8-01 — Zinc Blende (ZnS): Cell Volume, Density, Packing Factor, Linear and Planar Densities

## 📄 Official Statement
> 1.- For the following Zinc Blende structure (ZnS) calculate:
> a) The volume of the unit cell and volumetric density expressed in g/cm³.
> b) The packing factor.
> c) The linear density (ions/mm) in the direction [111].
> d) The planar density (ions/mm²) in the plane (111).
>
> Data: r(Zn²⁺) = 0.060 nm; r(S²⁻) = 0.174 nm, M(Zn) = 63.54, M(S) = 32.06.
>
> *(Solution: a) V = 1.57x10⁻²² cm³, ρv = 4.04 g/cm³; b) f = 0.585; c) ρ[111] = 2.13x10⁶ ions/mm; d) ρ(111) = 7.92x10¹² ions/mm²)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Structure.** S²⁻ on the FCC lattice points, Zn²⁺ in half of the tetrahedral sites; 4 Zn²⁺ and 4 S²⁻ per cubic cell [Session 16 Slide 9]. The radius ratio $0.060/0.174 = 0.345$ is in the tetrahedral range 0.225-0.414 [Session 16 Slide 6].
2. **Hard spheres in contact.** The cation touches the anions of its tetrahedron. A tetrahedral site lies at $(\frac14,\frac14,\frac14)$, a quarter of the body diagonal from the corner, so the contact is along the body diagonal: $a\sqrt3/4 = r_{Zn} + r_S$ (extension of Slide 9, the geometry of the cell).
3. **Density of a cell** (from [[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]): $\rho = nM/(V N_A)$, with $N_A = 6.022\times10^{23}$ mol⁻¹ (not printed on this item of the sheet).
4. **Counting.** A direction counts the ions whose centres lie on it, a plane the ions whose centres lie in it, with the fractions that belong to the segment or area of the cell.

### Data
| Quantity | Symbol | Value |
| :--- | :--- | ---: |
| Radius of Zn²⁺ | $r_{Zn}$ | 0.060 nm |
| Radius of S²⁻ | $r_S$ | 0.174 nm |
| Atomic masses | $M_{Zn},\ M_S$ | 63.54, 32.06 g/mol |
| Formula units per cell | $n$ | 4 |

**Unknowns:** $V$ and $\rho$; $f$; $\rho_L[111]$; $\rho_P(111)$.

---

## 🧠 2. Model and Strategy

The edge $a$ comes from the contact along the body diagonal; every other quantity is a count of ions divided by a volume, a length or an area of the cell.

**Strategy.**
1. Lattice parameter from $a\sqrt3/4 = r_{Zn} + r_S$, then $V = a^3$.
2. Density $\rho = 4(M_{Zn} + M_S)/(V N_A)$.
3. Packing factor $f = 4(V_{Zn} + V_S)/V$.
4. Count the ions on the body diagonal and in the (111) triangle.

---

## 🔢 3. Step-by-Step Derivation

### 1. Lattice parameter and volume
$$a = \frac{4(r_{Zn} + r_S)}{\sqrt3} = \frac{4\times(0.060 + 0.174)\ \text{nm}}{1.7321} = \frac{0.936\ \text{nm}}{1.7321} = 0.54040\ \text{nm}$$

$$V = a^3 = (0.54040\ \text{nm})^3 = 0.15781\ \text{nm}^3 = 0.15781\times10^{-21}\ \text{cm}^3 = \mathbf{1.578\times10^{-22}\ cm^3}$$

using $1\ \text{nm} = 10^{-7}$ cm, so $1\ \text{nm}^3 = 10^{-21}$ cm³.

### 2. Volumetric density
Mass of the four formula units of the cell:

$$m_{cell} = \frac{4(M_{Zn} + M_S)}{N_A} = \frac{4\times(63.54 + 32.06)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{382.40\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 6.3500\times10^{-22}\ \text{g}$$

$$\rho_v = \frac{m_{cell}}{V} = \frac{6.3500\times10^{-22}\ \text{g}}{1.5781\times10^{-22}\ \text{cm}^3} = \mathbf{4.02\ g/cm^3}$$

### 3. Packing factor
Volume of each ion, $V_{ion} = \frac43\pi r^3$:

$$V_{Zn} = \tfrac43\pi(0.060\ \text{nm})^3 = 9.048\times10^{-4}\ \text{nm}^3 \qquad V_S = \tfrac43\pi(0.174\ \text{nm})^3 = 2.2067\times10^{-2}\ \text{nm}^3$$

$$f = \frac{4(V_{Zn} + V_S)}{V} = \frac{4\times(9.048\times10^{-4} + 2.2067\times10^{-2})\ \text{nm}^3}{0.15781\ \text{nm}^3} = \frac{0.091887\ \text{nm}^3}{0.15781\ \text{nm}^3} = \mathbf{0.582}$$

### 4. Linear density along [111]
The body diagonal runs from $(0,0,0)$ to $(1,1,1)$, length $a\sqrt3 = 0.936$ nm. On it lie S²⁻ at both corners (each shared with the next diagonal, $2\times\frac12 = 1$) and Zn²⁺ at $(\frac14,\frac14,\frac14)$ (1); the site $(\frac34,\frac34,\frac34)$ belongs to the empty half of the tetrahedral sites. So 2 ions per diagonal:

$$\rho_L[111] = \frac{2\ \text{ions}}{0.936\ \text{nm}} = 2.137\ \text{ions/nm} = 2.137\times10^{6}\ \text{ions/mm} \approx \mathbf{2.14\times10^{6}\ ions/mm}$$

with $1\ \text{mm} = 10^{6}$ nm.

### 5. Planar density in (111)
The (111) plane cuts the cell in the equilateral triangle with vertices $(1,0,0)$, $(0,1,0)$, $(0,0,1)$, of side $a\sqrt2$ and area

$$A = \frac{\sqrt3}{4}(a\sqrt2)^2 = \frac{\sqrt3}{2}a^2 = 0.8660\times0.29203\ \text{nm}^2 = 0.25291\ \text{nm}^2$$

The S²⁻ ions in it are the three corners, each contributing $\frac16$ of its area (the 60° angle of the triangle), and the three face centres on its sides, each $\frac12$: $3\times\frac16 + 3\times\frac12 = 2$. No Zn²⁺ lies in it (their positions have $x+y+z = \frac34$ or $\frac74$, not 1).

$$\rho_P(111) = \frac{2\ \text{ions}}{0.25291\ \text{nm}^2} = 7.908\ \text{ions/nm}^2 = \mathbf{7.91\times10^{12}\ ions/mm^2}$$

with $1\ \text{mm}^2 = 10^{12}$ nm².

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** $\rho = [\text{g/mol}]/([\text{mol}^{-1}][\text{cm}^3]) = \text{g/cm}^3$; $f$ = nm³/nm³, dimensionless; ions per length and per area.
- **Anions do not overlap.** The nearest S²⁻ ions are half a face diagonal apart, $a\sqrt2/2 = 0.382$ nm, more than $2r_S = 0.348$ nm, so the cation-anion contact is the one that sets $a$.
- **Packing.** $f = 0.58$ is below the 0.74 of an FCC metal: the tetrahedral cation is small and fills little of the space between the anions, as expected for an open, covalent-like structure.
- **Density.** 4.02 g/cm³ is close to the measured density of sphalerite (about 4.1 g/cm³, extension).

### Interpretation
The body diagonal is the close-contact direction of zinc blende, so it alternates S-Zn-gap-S; the (111) plane holds only the anions, the close-packed layer of the FCC sulfur lattice, with the cations between layers. That layering is why the (111) planar density equals that of an FCC packing of S²⁻ ions alone.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $V$ | $1.57\times10^{-22}$ cm³ | $1.578\times10^{-22}$ cm³ | agrees |
| $\rho_v$ | 4.04 g/cm³ | 4.02 g/cm³ | the key divides by the rounded $V = 1.57\times10^{-22}$ cm³ (382.40/(6.022e23 × 1.57e-22) = 4.04) |
| $f$ | 0.585 | 0.582 | same rounding: 0.091887/0.157 = 0.585 |
| $\rho_L[111]$ | $2.13\times10^{6}$ ions/mm | $2.14\times10^{6}$ ions/mm | agrees (2.137) |
| $\rho_P(111)$ | $7.92\times10^{12}$ ions/mm² | $7.91\times10^{12}$ ions/mm² | agrees |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2: crystal structures]]
