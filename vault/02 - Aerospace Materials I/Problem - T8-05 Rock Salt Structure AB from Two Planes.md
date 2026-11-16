---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 5"
dificultad: medium
badge: "Two planes · rock salt AB"
tags:
  - official-problem
  - solved
  - rock-salt
  - stoichiometry
  - density
  - packing-factor
---

# ✏️ Problem: T8-05 — Rock Salt AB Ceramic from Two Planes: Structure, Stoichiometry, Density and Packing Factor

## 📄 Official Statement
> 5.- In the figure, two crystallographic planes are represented. They correspond to a cubic unit cell of a ceramic material with the following formula AB. If the diagonal of the cube is 0.824 nm, determine.
> a) The structure type and its description.
> b) The stoichiometry of the compound.
> c) The density expressed in g/cm³.
> d) The packing factor.
>
> Data: M(A) = 40 g/mol, M(B) = 16 g/mol, r(A) = 0.106 nm.
>
> ![[attachments/T8/t8-p2-planes-020-100.png]]
>
> *(Solution: a) NaCl type; b) AB; c) 3.45 g/cm³; d) 0.54)*

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Reading of the figure.** Plane (100): B ions (large open circles) at the corners and at the centre; A ions (small black) at the middles of the four edges. Plane (020), the plane parallel to (010) at half the edge ($y = a/2$): A at the corners and at the centre, B at the middles of the edges. The labels A (small black) and B (large open) are printed above the (020) plane.
2. **Diagonal of the cube.** The diagonal of a cube is its body diagonal, $a\sqrt3$ (a face diagonal would be called so). Hence $a = 0.824/\sqrt3$ nm.
3. **Contact.** The radius of B is not given; in the rock salt structure cation and anion touch along the edge, $a = 2(r_A + r_B)$, which gives it [Session 16 Slide 8].
4. $\rho = nM/(V N_A)$ with $N_A = 6.022\times10^{23}$ mol⁻¹ ([[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]).

### Data
| Quantity | Value |
| :--- | ---: |
| Body diagonal | 0.824 nm |
| $M_A$, $M_B$ | 40, 16 g/mol |
| $r_A$ | 0.106 nm |

**Unknowns:** structure; formula; $\rho$; $f$.

---

## 🧠 2. Model and Strategy

1. Positions from the two planes; count; compare with Slide 8 of Session 16.
2. Edge from the body diagonal, then $\rho$.
3. $r_B$ from the edge contact, then $f$.

---

## 🔢 3. Step-by-Step Derivation

### 1. Positions and structure type
- **B in (100)** at the corners and the face centre: B occupies the corners and face centres of the cell, an **FCC** lattice.
- **A in (100)** at the edge midpoints, $(0,\frac12,0)$ and the like, and **A in (020)** at the corners of that mid-plane, $(0,\frac12,0)$, $(1,\frac12,0)$, ..., which are again edge midpoints, and at its centre, $(\frac12,\frac12,\frac12)$, the body centre. The edge midpoints and the body centre are the **octahedral sites** of the FCC cell, and A fills all of them.
- **B in (020)** at the middles of the edges of the mid-plane, $(\frac12,\frac12,0)$ and $(0,\frac12,\frac12)$ and the like: face centres, consistent with the FCC lattice of B.

An FCC lattice of one ion with the other in all the octahedral sites is the **rock salt (NaCl) type** [Session 16 Slide 8]. With the masses the compound is CaO (Ca 40, O 16), one of the oxides that Slide 8 lists, with A = Ca²⁺ and B = O²⁻.

### 2. Stoichiometry
$$n_B = 8\times\tfrac18 + 6\times\tfrac12 = 4 \qquad n_A = 12\times\tfrac14 + 1 = 4 \qquad\Rightarrow\qquad \mathbf{AB}$$

### 3. Density
$$a = \frac{0.824\ \text{nm}}{\sqrt3} = \frac{0.824\ \text{nm}}{1.7321} = 0.47574\ \text{nm}$$

$$V = a^3 = (0.47574\ \text{nm})^3 = 0.10767\ \text{nm}^3 = 1.0767\times10^{-22}\ \text{cm}^3$$

$$m_{cell} = \frac{4(M_A + M_B)}{N_A} = \frac{4\times(40 + 16)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{224\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 3.7197\times10^{-22}\ \text{g}$$

$$\rho = \frac{3.7197\times10^{-22}\ \text{g}}{1.0767\times10^{-22}\ \text{cm}^3} = \mathbf{3.45\ g/cm^3}$$

### 4. Radius of B and packing factor
From the contact along the edge:

$$r_B = \frac{a}{2} - r_A = \frac{0.47574\ \text{nm}}{2} - 0.106\ \text{nm} = 0.23787 - 0.106 = 0.13187\ \text{nm}$$

$$V_A = \tfrac43\pi(0.106\ \text{nm})^3 = 4.9889\times10^{-3}\ \text{nm}^3 \qquad V_B = \tfrac43\pi(0.13187\ \text{nm})^3 = 9.6056\times10^{-3}\ \text{nm}^3$$

$$f = \frac{4(V_A + V_B)}{V} = \frac{4\times(4.9889 + 9.6056)\times10^{-3}\ \text{nm}^3}{0.10767\ \text{nm}^3} = \frac{0.058378\ \text{nm}^3}{0.10767\ \text{nm}^3} = \mathbf{0.542}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Reading of the diagonal.** With the face diagonal instead, $a = 0.824/\sqrt2 = 0.583$ nm and the density would be 1.88 g/cm³, half of the key and far below any oxide of calcium; the body diagonal is the consistent reading.
- **Radius ratio.** $r_A/r_B = 0.106/0.132 = 0.80$, which lies in the range 0.732-1.0 of Slide 6 (coordination 8), not in the octahedral range. The figure, the formula AB and the key all say NaCl type, so the structure is taken from the figure; the radius-ratio rule is a guide, not a law (extension, the same happens for real CaO, which is rock salt).
- **No anion overlap.** B-B along the face diagonal: $a\sqrt2/2 = 0.336$ nm $> 2r_B = 0.264$ nm.
- **Units** as in the previous problems.

### Interpretation
The same two planes describe the cell completely: (100) shows the face of the cell, (020) the mid-plane, and together they place an ion of each kind at every point of a simple cubic grid of step $a/2$, alternating A and B, which is the rock salt structure seen from the side. The derived $r_B = 0.132$ nm is the radius of O²⁻ used in the other problems of the sheet.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Structure | NaCl type | NaCl (rock salt), B FCC, A in all octahedral sites | agrees |
| Stoichiometry | AB | AB | agrees |
| Density | 3.45 g/cm³ | 3.45 g/cm³ | agrees, with $a = 0.824/\sqrt3$ nm (body diagonal) |
| Packing factor | 0.54 | 0.542 | agrees |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
* [[Problem - T8-07 MgO Rock Salt Cell Packing and Densities|Problem T8-07]]
