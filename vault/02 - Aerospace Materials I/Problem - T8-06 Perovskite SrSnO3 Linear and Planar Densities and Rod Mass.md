---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 6"
dificultad: hard
badge: "Perovskite SrSnO₃ · rod mass"
tags:
  - official-problem
  - solved
  - perovskite
  - linear-density
  - planar-density
  - density
---

# ✏️ Problem: T8-06 — Perovskite SrSnO₃: Linear and Planar Densities and the Mass of a Rod

## 📄 Official Statement
> 6.-The compound SrSnO₃ has a perovskite structure, with Sn⁴⁺ occupying the octahedral interstitial position at the center of the cube. DATA: Atomic masses: O = 16, Sr = 87.6, Sn = 118.7; Ionic radii: O⁻² = 0,146 nm, Sn⁺⁴ = 0,071nm, Sr⁺² = 0,113nm. Calculate:
> a) The linear density in ions/nm along the [101] direction
> b) The surface density in ions/nm² in the (101) plane
> c) The mass of a cylindrical rod with a 5 mm radius and a 10 mm length
>
> *(Solution: a) ρ [101] = 3.86 ions/nm; b) ρ(101) = 15.87 ions/nm²; c) m = 6.76 g)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Structure.** Sr²⁺ at the corners, O²⁻ at the face centres, Sn⁴⁺ at the body centre (the octahedral site); 1 Sr, 3 O and 1 Sn per cell [Session 16 Slide 12].
2. **Hard spheres.** The edge $a$ is set by the pair of ions that touch. Two contacts are possible: Sn⁴⁺ with its six O²⁻ along the edge direction, $a = 2(r_{Sn} + r_O)$, and Sr²⁺ with O²⁻ along the face diagonal, $a\sqrt2 = 2(r_{Sr} + r_O)$, the "FCC packing of A and O" of Slide 12. The real edge is the **larger** of the two: with the smaller one the other pair of spheres would overlap.
3. $\rho = \sum M/(V N_A)$ with $N_A = 6.022\times10^{23}$ mol⁻¹ ([[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]); the rod is a solid cylinder, $V = \pi R^2 L$, with no porosity.

### Data
| Quantity | Value |
| :--- | ---: |
| $r_O$, $r_{Sn}$, $r_{Sr}$ | 0.146, 0.071, 0.113 nm |
| $M_O$, $M_{Sr}$, $M_{Sn}$ | 16, 87.6, 118.7 g/mol |
| Rod | $R = 5$ mm, $L = 10$ mm |

**Unknowns:** $\rho_L[101]$, $\rho_P(101)$, $m$.

---

## 🧠 2. Model and Strategy

1. Compute both contact edges and keep the one that leaves no overlap.
2. Count the ions on the face diagonal [101] and in the plane (101).
3. Density of the cell, then the mass of the rod.

---

## 🔢 3. Step-by-Step Derivation

### 1. Lattice parameter
Sn-O contact along the edge:

$$a_1 = 2(r_{Sn} + r_O) = 2\times(0.071 + 0.146)\ \text{nm} = 0.434\ \text{nm}$$

Sr-O contact along the face diagonal:

$$a_2 = \frac{2(r_{Sr} + r_O)}{\sqrt2} = \frac{2\times(0.113 + 0.146)\ \text{nm}}{1.4142} = \frac{0.518\ \text{nm}}{1.4142} = 0.36628\ \text{nm}$$

With $a_2$ the Sn⁴⁺ ion would be $a_2/2 = 0.183$ nm from its oxygens, less than $r_{Sn} + r_O = 0.217$ nm: the spheres would overlap by 0.034 nm. With $a_1$ the Sr-O distance is $a_1\sqrt2/2 = 0.307$ nm, more than $r_{Sr} + r_O = 0.259$ nm: no overlap. The cell is fixed by the Sn-O contact:

$$a = 0.434\ \text{nm}$$

### 2. Linear density along [101]
The direction [101] is the diagonal of the face $y = 0$, from $(0,0,0)$ to $(1,0,1)$, of length $a\sqrt2 = 0.434\times1.4142 = 0.61377$ nm. On it: Sr²⁺ at both corners ($2\times\frac12 = 1$) and O²⁻ at the centre of the face, $(\frac12,0,\frac12)$ (1). Two ions:

$$\rho_L[101] = \frac{2\ \text{ions}}{0.61377\ \text{nm}} = \mathbf{3.26\ ions/nm}$$

### 3. Planar density in (101)
The plane (101) of the cell, $x + z = 1$, is the rectangle with corners $(1,0,0)$, $(0,0,1)$, $(1,1,0)$, $(0,1,1)$: one side is the face diagonal $a\sqrt2$, the other the edge $a$, so its area is

$$A = a\cdot a\sqrt2 = \sqrt2\,a^2 = 1.4142\times(0.434\ \text{nm})^2 = 0.26638\ \text{nm}^2$$

Ions in it: Sr²⁺ at the four corners ($4\times\frac14 = 1$); O²⁻ at $(\frac12,0,\frac12)$ and $(\frac12,1,\frac12)$, the midpoints of the two long sides ($2\times\frac12 = 1$); Sn⁴⁺ at $(\frac12,\frac12,\frac12)$, the centre (1). The other face centres have $x + z = \frac12$ or $\frac32$ and lie outside. Three ions:

$$\rho_P(101) = \frac{3\ \text{ions}}{0.26638\ \text{nm}^2} = \mathbf{11.26\ ions/nm^2}$$

### 4. Mass of the rod
Density of the cell:

$$V_{cell} = a^3 = (0.434\ \text{nm})^3 = 0.081747\ \text{nm}^3 = 8.1747\times10^{-23}\ \text{cm}^3$$

$$m_{cell} = \frac{M_{Sr} + M_{Sn} + 3M_O}{N_A} = \frac{(87.6 + 118.7 + 3\times16)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{254.3\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 4.2228\times10^{-22}\ \text{g}$$

$$\rho = \frac{4.2228\times10^{-22}\ \text{g}}{8.1747\times10^{-23}\ \text{cm}^3} = 5.166\ \text{g/cm}^3$$

Volume of the rod, with $R = 0.5$ cm and $L = 1.0$ cm:

$$V_{rod} = \pi R^2 L = \pi\times(0.5\ \text{cm})^2\times1.0\ \text{cm} = 0.78540\ \text{cm}^3$$

$$m = \rho V_{rod} = 5.166\ \text{g/cm}^3\times0.78540\ \text{cm}^3 = \mathbf{4.06\ g}$$

### 5. The edge of the key
The key corresponds to the second edge, $a_2 = 0.36628$ nm (Sr-O contact):

$$\rho_L[101] = \frac{2}{0.518\ \text{nm}} = 3.86\ \text{ions/nm} \qquad \rho_P(101) = \frac{3}{\sqrt2\,(0.36628)^2\ \text{nm}^2} = 15.81\ \text{ions/nm}^2$$

$$\rho = \frac{4.2228\times10^{-22}\ \text{g}}{0.049141\times10^{-21}\ \text{cm}^3} = 8.593\ \text{g/cm}^3 \qquad m = 8.593\times0.78540 = 6.75\ \text{g}$$

> [!warning] Discrepancy with the official solution
> The key (3.86 ions/nm, 15.87 ions/nm², 6.76 g) takes the edge from the Sr-O contact along the face diagonal, $a = 0.366$ nm, the rule used in Problem 2 for CaTiO₃. With the radii of this problem that cell is too small for the Sn⁴⁺ ion: the body-centre site leaves $a/2 - r_O = 0.183 - 0.146 = 0.037$ nm for a cation of radius 0.071 nm, so Sn-O would overlap by 0.034 nm. In CaTiO₃ the two contacts happened to give the same edge (0.3366 and 0.336 nm, Problem T8-02), which is why the rule worked there. The hard-sphere cell that respects every radius is $a = 2(r_{Sn} + r_O) = 0.434$ nm, and it gives 3.26 ions/nm, 11.26 ions/nm² and 4.06 g. The computed values are kept; the key's values are reproduced in step 5 for comparison. (The key's 15.87 is also slightly above the 15.81 of its own edge, a rounding of $a$.)

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** ions/nm, ions/nm²; $[\rho V] = (\text{g/cm}^3)(\text{cm}^3) = \text{g}$; 5 mm = 0.5 cm, 10 mm = 1.0 cm.
- **Radius ratio.** $r_{Sn}/r_O = 0.071/0.146 = 0.486$, inside the octahedral range 0.414-0.732 of Slide 6: the cation is larger than the minimum for its hole, so it touches its anions and pushes them apart, which is exactly the Sn-O contact used here.
- **Charge.** $+2 + 4 - 3\times2 = 0$.
- **Order of magnitude.** The measured edge of SrSnO₃ is about 0.403 nm (extension), between the two hard-sphere edges; real ions are not hard spheres, and these radii are not those of a single consistent table.

### Interpretation
In a perovskite the B cation sits in the octahedron of oxygens and the A cation in the twelve-fold hole between octahedra. Which contact sets the cell depends on the sizes (the tolerance of the perovskite structure, an extension): here the B-O contact dominates, the A cation rattles in a hole a little too large for it, and the cell is larger and lighter than the key assumes.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| $\rho_L[101]$ | 3.86 ions/nm | 3.26 ions/nm | key uses $a = 0.366$ nm (Sr-O contact), which overlaps Sn-O; see the warning |
| $\rho_P(101)$ | 15.87 ions/nm² | 11.26 ions/nm² | same cause (15.81 with the key's edge) |
| $m$ | 6.76 g | 4.06 g | same cause (6.75 g with the key's edge) |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Problem - T8-02 Perovskite CaTiO3 Cell Packing and Densities|Problem T8-02]]
