---
materia: "Aerospace Materials I"
tema: "Topic 8: Ceramic Materials"
origen: "Problems T8_CeramicMaterials.pdf, Problem 4"
dificultad: medium
badge: "Two planes · fluorite AB₂"
tags:
  - official-problem
  - solved
  - fluorite
  - stoichiometry
  - density
  - packing-factor
---

# ✏️ Problem: T8-04 — Fluorite-Type AxBy Ceramic from Two Planes: Structure, Stoichiometry, Density and Packing Factor

## 📄 Official Statement
> 4.- In the figure, two crystallographic planes are represented. They correspond to a cubic unit cell of a ceramic material with the following formula AxBy. Determine.
> a) The structure type and its description
> b) The stoichiometry of the compound
> c) The density expressed in g/cm³
> d) The packing factor
>
> Data: M(A) = 238 g/mol, M(B) = 16 g/mol, r(A) = 0.105 nm, r(B) = 0.132 nm.
>
> ![[attachments/T8/t8-p2-planes-100-110.png]]
>
> *(Solution: a) Fluorite type structure, CaF₂. FCC close packing of A ions. The B atoms occupy all the tetrahedral sites; b) AB₂; c) 10.95 g/cm³; d) f = 0.589)*

On the sheet each key is printed after its own item; they are collected here in one line.

---

## 📊 1. Hypotheses and Parameters

### Hypotheses
1. **Reading of the figure.** (100) plane: a square of edge 0.547 nm with A ions (open circles) at the corners and at the centre (the diagonal line joins a corner, the centre and the opposite corner). (110) plane: a rectangle $a\sqrt2$ wide and $a$ high, with A at the four corners and at the middle of the two long edges, and four B ions (black) inside, at a quarter and three quarters of the width and of the height. The cell is cubic (statement), $a = 0.547$ nm.
2. **Counting** of [[Topic 2 - Structure of Materials and Crystalline Defects|Topic 2]]; $\rho = nM/(V N_A)$ with $N_A = 6.022\times10^{23}$ mol⁻¹.

### Data
| Quantity | Value |
| :--- | ---: |
| Edge | $a = 0.547$ nm |
| $M_A$, $M_B$ | 238, 16 g/mol |
| $r_A$, $r_B$ | 0.105, 0.132 nm |

**Unknowns:** structure; formula; $\rho$; $f$.

---

## 🧠 2. Model and Strategy

1. Turn the points of the two planes into positions in the cell.
2. Count the ions and compare with the structures of Slides 10-11 of Session 16.
3. Density and packing factor with the counted ions.

---

## 🔢 3. Step-by-Step Derivation

### 1. Positions
- **A in (100):** corners and the centre of the face, $(0,\frac12,\frac12)$. Since the cell is cubic the same holds for every face: A sits at the corners and at all the face centres, the **FCC** lattice points.
- **B in (110):** the diagonal plane contains the points $(t, t, z)$. Its width is the face diagonal, so a point at a quarter of the width has $t = \frac14$, and at three quarters $t = \frac34$. The four B ions are therefore at $(\frac14,\frac14,\frac14)$, $(\frac14,\frac14,\frac34)$, $(\frac34,\frac34,\frac14)$ and $(\frac34,\frac34,\frac34)$: these are tetrahedral sites of the FCC cell. The (110) plane shows four of them; the other plane through the cell, (1̄10), shows the other four, and the sheet labels the figure (110)/(1̄10). B therefore fills **all eight** tetrahedral sites.
- **A in (110):** the corners and $(\frac12,\frac12,0)$, $(\frac12,\frac12,1)$, the face centres of the bottom and top faces, consistent with the FCC lattice.

### 2. Structure type and stoichiometry
$$n_A = 8\times\tfrac18 + 6\times\tfrac12 = 4 \qquad n_B = 8\times1 = 8 \qquad \Rightarrow\qquad \mathbf{AB_2}$$

An FCC lattice of the cation with the anion in all the tetrahedral sites, 4 A and 8 B per cell, is the **fluorite (CaF₂) type** [Session 16 Slide 10]. With the masses, the compound is UO₂ (U 238, O 16), which Slide 10 lists among the fluorite oxides. The radius ratio agrees: $r_A/r_B = 0.105/0.132 = 0.795$, in the range 0.732-1.0 of coordination 8 for the cation [Session 16 Slide 6], and each B has 4 A neighbours.

### 3. Density
$$V = a^3 = (0.547\ \text{nm})^3 = 0.16367\ \text{nm}^3 = 1.6367\times10^{-22}\ \text{cm}^3$$

$$m_{cell} = \frac{4(M_A + 2M_B)}{N_A} = \frac{4\times(238 + 2\times16)\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = \frac{1080\ \text{g/mol}}{6.022\times10^{23}\ \text{mol}^{-1}} = 1.7934\times10^{-21}\ \text{g}$$

$$\rho = \frac{1.7934\times10^{-21}\ \text{g}}{1.6367\times10^{-22}\ \text{cm}^3} = \mathbf{10.96\ g/cm^3}$$

### 4. Packing factor
$$V_A = \tfrac43\pi(0.105\ \text{nm})^3 = 4.849\times10^{-3}\ \text{nm}^3 \qquad V_B = \tfrac43\pi(0.132\ \text{nm})^3 = 9.634\times10^{-3}\ \text{nm}^3$$

$$f = \frac{4V_A + 8V_B}{V} = \frac{(4\times4.849\times10^{-3} + 8\times9.634\times10^{-3})\ \text{nm}^3}{0.16367\ \text{nm}^3} = \frac{0.096469\ \text{nm}^3}{0.16367\ \text{nm}^3} = \mathbf{0.589}$$

---

## 🔍 4. Units and Limits, with Physical and Dimensional Verification

### Checks
- **Contact.** A tetrahedral site is $a\sqrt3/4 = 0.547\times1.7321/4 = 0.2369$ nm from its corner ion, and $r_A + r_B = 0.237$ nm: the A-B pairs touch, so the edge of the figure is consistent with the radii.
- **No overlap of like ions.** B-B along the edge: $a/2 = 0.2735$ nm $> 2r_B = 0.264$ nm; A-A along the face diagonal: $a\sqrt2/2 = 0.387$ nm $> 2r_A = 0.210$ nm.
- **Charge** with A⁴⁺ and B²⁻ (U⁴⁺, O²⁻): $4\times4 - 8\times2 = 0$.
- **Units** as in the previous problems; $f$ dimensionless.

### Interpretation
The heavy uranium ions make the density high (UO₂ is the nuclear fuel), while the packing factor is moderate: the anions are the large ions here, and the eight of them fill the tetrahedral holes of a cation lattice that is far from close-packed by itself.

## ✅ Check against the official solution
| Item | Official | Computed | Comment |
| :--- | :--- | :--- | :--- |
| Structure | fluorite, FCC A, B in all tetrahedral sites | same | agrees |
| Stoichiometry | AB₂ | AB₂ | agrees |
| Density | 10.95 g/cm³ | 10.96 g/cm³ | agrees within rounding (10.958) |
| Packing factor | 0.589 | 0.589 | agrees |

## 🔗 Related Links
* [[Topic 8 - Ceramic Materials]]
