---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 36-52"
tags:
  - theory
  - fundamental-concept
  - miller-indices
  - miller-bravais
  - crystal-directions
  - crystal-planes
dificultad: medium
prerrequisitos:
  - "[[Concept - Crystal Systems and Bravais Lattices]]"
---

# 🧭 Concept: Miller Notation for Cubic and Hexagonal Directions and Planes

> **Methodological Basis:** **Miller notation** is the universal crystallographic standard for unambiguously identifying translation vectors (directions) and periodic families of planes within a crystal lattice. It allows the lattice symmetry to be correlated with anisotropic physical phenomena such as X-ray wave propagation, plastic deformation by slip and epitaxial growth [Slide 36].

---

## ➡️ 1. Cubic Crystallographic Directions $[u\, v\, w]$

A crystallographic direction is defined as a vector drawn from the coordinate origin to a generic point of the cell [Slides 37-40].

### Systematic Determination Procedure:
1. **Choice of Axis System and Origin:** A right-handed coordinate system is placed at a corner of the unit cell. If any component of the direction projects toward negative values, **the origin is translated** along the corresponding axis by one cell length (+1).
2. **Vector Coordinates:** The coordinates of the tip (Head) minus those of the origin (Tail) are subtracted:
   $$\Delta x = x_2 - x_1, \quad \Delta y = y_2 - y_1, \quad \Delta z = z_2 - z_1$$
3. **Reduction to Minimum Integers:** Divide or multiply by the least common denominator to obtain the smallest possible integers:
   $$u, v, w \in \mathbb{Z}$$
4. **Notation:** They are enclosed in **square brackets** without commas: $[u\, v\, w]$. Negative numbers are denoted with an overbar: $\bar{u} \equiv -u$.
5. **Families of Crystallographically Equivalent Directions:** They are enclosed in **angle brackets**: $\langle u\, v\, w \rangle$. For example, in the cubic system, the 6 edge directions are:
   $$\langle 100 \rangle = \{[100], [\bar{1}00], [010], [0\bar{1}0], [001], [00\bar{1}]\}$$

---

## 📐 2. Miller Crystallographic Planes $(h\, k\, l)$

A crystallographic plane represents an infinite family of parallel, equidistant planes [Slides 41-49].

### Systematic Determination Procedure:
1. **Origin and Intercept Rule:** The plane under analysis **cannot pass through the origin**. If it does, the coordinate origin is translated to an adjacent neighboring corner.
2. **Determination of Intercepts:** The fractional coordinates at which the plane cuts the crystallographic axes are identified:
   $$\text{Intercepts} = (p\, a,\, q\, b,\, r\, c) \implies (p, q, r)$$
   If a plane is parallel to a crystallographic axis, its intercept is taken at **infinity** ($\infty$).
3. **Calculation of the Reciprocals:** The inverses of the intercepts are taken:
   $$h' = \frac{1}{p}, \quad k' = \frac{1}{q}, \quad l' = \frac{1}{r}$$
   (with the convention $\frac{1}{\infty} = 0$).
4. **Reduction to Minimum Integers:** Fractions are eliminated by multiplying by the least common multiple (LCM).
5. **Notation:** They are enclosed in **round parentheses**: $(h\, k\, l)$. Negative indices carry an overbar: $(\bar{h}\, k\, l)$.
6. **Families of Equivalent Planes:** They are enclosed in **braces**: $\{h\, k\, l\}$. For example, in a cubic lattice:
   $$\{100\} = \{(100), (\bar{1}00), (010), (0\bar{1}0), (001), (00\bar{1})\}$$
   $$\{111\} = \{(111), (\bar{1}11), (1\bar{1}1), (11\bar{1}), (\bar{1}\bar{1}1), (\bar{1}1\bar{1}), (1\bar{1}\bar{1}), (\bar{1}\bar{1}\bar{1})\}$$

### Perpendicularity Property Exclusive to Cubic Lattices:
> In the cubic system (and only in it, owing to its isotropic orthonormal metric $a=b=c$), the direction $[h\, k\, l]$ is **rigorously orthogonal** to the plane $(h\, k\, l)$:
> $$[h\, k\, l] \perp (h\, k\, l) \quad (\text{in cubic crystals})$$

---

## ⬡ 3. Four-Index Miller-Bravais Notation for the Hexagonal System

The hexagonal cell has sixfold rotational symmetry ($60^\circ$) in the basal plane that is not transparently reflected with 3 orthogonal axes. To preserve the symmetry equivalence in the indices, the **4-axis** system is used [Slides 50-52]:
* Three coplanar axes in the basal plane: $\vec{a}_1, \vec{a}_2, \vec{a}_3$, spaced $120^\circ$ apart ($\vec{a}_1 + \vec{a}_2 + \vec{a}_3 = 0$).
* One perpendicular vertical axis: $\vec{c} = [0001]$.

### Miller-Bravais Planes $(h\, k\, i\, l)$:
The indices correspond to the reciprocals of the intercepts with $\vec{a}_1, \vec{a}_2, \vec{a}_3$ and $\vec{c}$. The coplanar geometry imposes the **strict closure condition**:
$$i = -(h + k)$$
* *Example:* The plane that cuts $a_1$ at 1, $a_2$ at $\infty$ and $c$ at $\infty$:
  Intercepts: $(1, \infty, -1, \infty) \implies \text{Reciprocals}: (1, 0, -1, 0) \implies (10\bar{1}0)$. Check: $i = -(1 + 0) = -1$.
* The close-packed basal plane of HCP is: $(0001)$ (or the $\{0001\}$ plane).

### Miller-Bravais Directions $[u\, v\, t\, w]$:
To transform a conventional three-dimensional direction $[u'\, v'\, w']$ to the 4-axis notation $[u\, v\, t\, w]$ [Slide 51]:
$$u = \frac{1}{3}(2u' - v'), \quad v = \frac{1}{3}(2v' - u'), \quad t = -(u + v) = -\frac{1}{3}(u' + v'), \quad w = w'$$
* *Key examples in HCP:*
  * $[100] \to [2\bar{1}\bar{1}0]$ (direction of maximum packing in the basal plane).
  * $[110] \to [11\bar{2}0]$.
  * $[001] \to [0001]$ (optic / axial axis).

---

## 📊 4. Summary of Crystallographic Notation Conventions

| Crystallographic Entity | Cubic Notation (3 indices) | Hexagonal Notation (4 indices) |
| :--- | :--- | :--- |
| **Point in space** | $x, y, z$ | $x, y, z$ |
| **Specific direction** | $[u\, v\, w]$ | $[u\, v\, t\, w]$ with $t = -(u+v)$ |
| **Family of directions** | $\langle u\, v\, w \rangle$ | $\langle u\, v\, t\, w \rangle$ |
| **Specific plane** | $(h\, k\, l)$ | $(h\, k\, i\, l)$ with $i = -(h+k)$ |
| **Family of planes** | $\{h\, k\, l\}$ | $\{h\, k\, i\, l\}$ |

---
*Bidirectional Links:*
* [[Concept - Tetrahedral and Octahedral Interstitial Sites|⬅️ Previous: Interstitial Sites]]
* [[Concept - Volumetric, Linear and Planar Density in Crystal Lattices|Next: Volumetric, Linear and Planar Density ➡️]]
