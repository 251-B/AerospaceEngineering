---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 3"
dificultad: medium
badge: "Two planes · orthorhombic perovskite"
tags:
  - official-problem
  - solved
  - perovskite
  - crystal-system
  - stoichiometry
  - density
---

# ✏️ Problem: T8-03 — Crystal System, Stoichiometry, Density and Structure of an AxByCz Ceramic from Two Planes

## 📄 Official Statement
> 3.- In the figure, two crystallographic planes are represented. They correspond to a unit cell of a ceramic material with the following formula AxByCz. Determine:
> a) The crystalline system they belong to
> b) The stoichiometry and density (g/cm³)
> c) The structure type and the description of the structure in terms of the closed packing sequence.
>
> Data: M(A) = 40 g/mol, M(B) = 48 g/mol, M(C) = 16 g/mol.
>
> ![[attachments/T8/t8-p1-planes-110-100.png]]
>
> *(Solution: a) orthorhombic symmetry; b) ABC₃; ρ = 3.96 g/cm³, c) Perovskite-type structure)*

The sheet prints "AxByCz.." with a double full stop.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Reading of the figure.** In the (100) plane: A ions (large, dotted) at the four corners and one C ion (open circle) at the centre; edges 0.387 nm (horizontal) and 0.383 nm (vertical). In the (110) plane: A at the four corners, C at the middle of the two long edges, one small B ion at the centre; edges 0.546 nm (horizontal) and 0.383 nm (vertical). The identification of the circles is read from the labels of the figure.
2. **Axes.** The (100) plane is the face $x = 0$, spanned by $b$ and $c$, so $b = 0.387$ nm and $c = 0.383$ nm. The (110) plane is the diagonal plane, spanned by the face diagonal $\sqrt{a^2 + b^2}$ of the base and by $c$; its vertical edge is again $c = 0.383$ nm, the same as in (100), which confirms the reading.
3. **Counting.** Corner $\frac18$, face $\frac12$, interior 1 (the rules of [[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]); $\rho = \sum M/(V N_A)$ with $N_A = 6.022\times10^{23}$ mol⁻¹.

### Data
| Quantity | Value |
| :--- | ---: |
| (100) plane | $b = 0.387$ nm, $c = 0.383$ nm |
| (110) plane | $\sqrt{a^2 + b^2} = 0.546$ nm, $c = 0.383$ nm |
| $M_A$, $M_B$, $M_C$ | 40, 48, 16 g/mol |

**Unknowns:** crystal system; formula and $\rho$; structure type and stacking.

---

## 🧠 2. Model and Strategy

1. Solve the face diagonal for $a$ and compare the three edges.
2. Place every ion of the two planes in the cell and count.
3. Compare the arrangement with the perovskite of Slide 12 of Session 16.

---

## 🔢 3. Step-by-Step Derivation

### 1. Crystal system
From the diagonal of the base, by Pythagoras in the right triangle with legs $a$ and $b$ and hypotenuse 0.546 nm:

$$a = \sqrt{0.546^2 - b^2} = \sqrt{(0.546\ \text{nm})^2 - (0.387\ \text{nm})^2} = \sqrt{0.298116 - 0.149769}\ \text{nm} = \sqrt{0.148347}\ \text{nm} = 0.3852\ \text{nm}$$

The three edges $a = 0.385$ nm, $b = 0.387$ nm and $c = 0.383$ nm are all different, and the planes drawn are rectangles, so the axes are at right angles: three unequal edges at 90° is the **orthorhombic** system. A cube with $a = b = 0.387$ nm would need a diagonal $0.387\sqrt2 = 0.547$ nm; the printed 0.546 nm and the two different vertical and horizontal edges of (100) rule that out.

### 2. Positions and stoichiometry
- **A**: at the corners of both planes, hence at the 8 corners of the cell: $8\times\frac18 = 1$.
- **C**: at the centre of the face (100), and at the middle of the long edges of (110). Those points of the diagonal plane are $(\frac12,\frac12,0)$ and $(\frac12,\frac12,1)$, the centres of the bottom and top faces. So C occupies the centres of all six faces: $6\times\frac12 = 3$.
- **B**: at the centre of (110), the point $(\frac12,\frac12,\frac12)$, the body centre: 1.

$$\text{A}_1\text{B}_1\text{C}_3 = \mathbf{ABC_3}$$

### 3. Density
$$V = abc = 0.3852\ \text{nm}\times0.387\ \text{nm}\times0.383\ \text{nm} = 0.05709\ \text{nm}^3 = 5.709\times10^{-23}\ \text{cm}^3$$

$$m_{cell} = \frac{M_A + M_B + 3M_C}{N_A} = \frac{(40 + 48 + 3\times16)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{136\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 2.2584\times10^{-22}\ \text{g}$$

$$\rho = \frac{2.2584\times10^{-22}\ \text{g}}{5.709\times10^{-23}\ \text{cm}^3} = \mathbf{3.96\ g/cm^3}$$

### 4. Structure type and close-packing description
The arrangement is that of the perovskite of Slide 12: A at the corners, C at the face centres, B at the body centre [Session 16 Slide 12]. The masses match CaTiO₃ (Ca 40, Ti 48, O 16), with A = Ca²⁺, B = Ti⁴⁺ and C = O²⁻.

- **Close packing:** the A and C ions together (corners plus face centres) form a cubic close packing, the FCC arrangement, here slightly distorted into an orthorhombic cell. Along the body diagonal [111] the close-packed layers, each of composition AC₃, follow the sequence **ABCABC...** of the FCC packing.
- **Interstitial:** B fills **¼ of the octahedral sites** of that packing, the one at the body centre, surrounded by six C ions (C.I. 6); A has C.I. 12.

**Perovskite-type structure, ABC₃**, with an orthorhombic distortion of the ideal cube.

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Units.** nm³ to cm³ with $10^{-21}$; g/mol over mol⁻¹ gives g.
- **Charge balance** with A²⁺, B⁴⁺, C²⁻: $+2 + 4 - 3\times2 = 0$.
- **Limit of the cubic cell.** As $a, b, c \to 0.387$ nm the cell becomes the cubic perovskite and the density changes only slightly (to 3.90 g/cm³ for $a = b = c = 0.387$ nm, extension), so the distortion is small: the edges differ by about 1 %.

### Interpretation
Two planes are enough to fix a cell when they show all the ions: the face (100) gives two edges and the face centres, the diagonal plane (110) gives the third edge and the body centre. The distortion of real perovskites from the cube is common (CaTiO₃ itself is orthorhombic, extension), and it is what the three slightly different edges of the figure express.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Crystal system | orthorhombic | orthorhombic ($a = 0.385$, $b = 0.387$, $c = 0.383$ nm) | agrees |
| Stoichiometry | ABC₃ | ABC₃ | agrees |
| Density | 3.96 g/cm³ | 3.96 g/cm³ | agrees |
| Structure | perovskite-type | perovskite: AC₃ close packing ABCABC, B in ¼ of the octahedral sites | agrees; the stacking description is not printed in the key |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Problem - T8-02 Perovskite CaTiO3 Cell Packing and Densities|Problem T8-02]]
