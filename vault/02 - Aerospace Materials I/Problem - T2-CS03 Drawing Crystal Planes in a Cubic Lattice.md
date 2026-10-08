---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 3"
dificultad: medium
tags:
  - official-problem
  - solved
  - miller-indices
  - crystal-planes
  - cubic-lattice
  - origin-translation
---

# ✏️ Problem: T2-CS03 — Drawing Crystal Planes in a Cubic Lattice

## 📄 Official Statement
> **3. Draw the crystalline planes in a cubic lattice that present the following Miller indices:**  
> **a)** $(1\, 0\, \bar{1})$  
> **b)** $(1\, \bar{2}\, 1)$  
> **c)** $(\bar{2}\, 1\, 3)$  
> **d)** $(1\, \bar{3}\, 3)$  
> **e)** $(1\, \bar{2}\, \bar{2})$  
> **f)** $(\bar{3}\, \bar{1}\, 2)$  
> **g)** $(1\, 2\, \bar{3})$  
> **h)** $(\bar{1}\, \bar{4}\, 3)$  
> **i)** $(\bar{3}\, \bar{1}\, \bar{3})$  
> **j)** $(3\, \bar{1}\, 3)$

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Geometric Context:
Ten families of crystallographic planes are analysed in a cubic lattice with orthogonal edges of length $a$.

### Origin Selection Criterion [Session 3 Slide 43]:
* If all indices $h, k, l$ are positive, the natural origin is placed at the lower left rear vertex $(0, 0, 0)$.
* If any index is negative (overbar notation $\bar{u}$), the origin must be translated by $+1$ unit along the corresponding axis so that the intercept falls inside the standard unit cell:
  * $\bar{h} \implies$ translate origin to $x = 1$.
  * $\bar{k} \implies$ translate origin to $y = 1$.
  * $\bar{l} \implies$ translate origin to $z = 1$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

According to Miller's systematic inverse procedure [Session 3 Slides 41-45]:
1. Take the **reciprocals of the Miller indices** to find the relative axial intercepts:
   $$x_{\text{int}} = \frac{1}{h}, \quad y_{\text{int}} = \frac{1}{k}, \quad z_{\text{int}} = \frac{1}{l}$$
   (with the rule $1/0 = \infty$, indicating parallelism to the axis).
2. Determine the required origin translation from the sign of the intercepts.
3. Mark the cut points on the unit cell edges relative to the chosen origin and join them with straight lines to form the polygon of the planar section.

---

## 🔢 3. Phase 3: Step-by-Step Derivation of the 10 Planes

| Part | Plane $(h\,k\,l)$ | Reciprocals $(1/h, 1/k, 1/l)$ | Recommended Origin | Cut Points on Edges $(x, y, z)$ | Plane Geometry |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **a** | $(1\, 0\, \bar{1})$ | $(1,\, \infty,\, -1)$ | $(0, 0, 1)$ | $(1, 0, 1)$, parallel to the $y$ axis, $(0, 0, 0)$ | Diagonal rectangle joining opposite edges |
| **b** | $(1\, \bar{2}\, 1)$ | $(1,\, -1/2,\, 1)$ | $(0, 1, 0)$ | $(1, 1, 0)$, $(0, 1/2, 0)$, $(0, 1, 1)$ | Triangle cutting the $y$ axis at mid-height |
| **c** | $(\bar{2}\, 1\, 3)$ | $(-1/2,\, 1,\, 1/3)$ | $(1, 0, 0)$ | $(1/2, 0, 0)$, $(1, 1, 0)$, $(1, 0, 1/3)$ | Scalene triangle with fractional cuts |
| **d** | $(1\, \bar{3}\, 3)$ | $(1,\, -1/3,\, 1/3)$ | $(0, 1, 0)$ | $(1, 1, 0)$, $(0, 2/3, 0)$, $(0, 1, 1/3)$ | Oblique triangle |
| **e** | $(1\, \bar{2}\, \bar{2})$ | $(1,\, -1/2,\, -1/2)$ | $(0, 1, 1)$ | $(1, 1, 1)$, $(0, 1/2, 1)$, $(0, 1, 1/2)$ | Isosceles triangle with respect to the negative $y, z$ axes |
| **f** | $(\bar{3}\, \bar{1}\, 2)$ | $(-1/3,\, -1,\, 1/2)$ | $(1, 1, 0)$ | $(2/3, 1, 0)$, $(1, 0, 0)$, $(1, 1, 1/2)$ | Oblique triangle in the $(+x, +y)$ quadrant |
| **g** | $(1\, 2\, \bar{3})$ | $(1,\, 1/2,\, -1/3)$ | $(0, 0, 1)$ | $(1, 0, 1)$, $(0, 1/2, 1)$, $(0, 0, 2/3)$ | Oblique triangle with cuts at $a$, $a/2$, $-a/3$ |
| **h** | $(\bar{1}\, \bar{4}\, 3)$ | $(-1,\, -1/4,\, 1/3)$ | $(1, 1, 0)$ | $(0, 1, 0)$, $(1, 3/4, 0)$, $(1, 1, 1/3)$ | Triangle strongly inclined about the $y$ axis |
| **i** | $(\bar{3}\, \bar{1}\, \bar{3})$ | $(-1/3,\, -1,\, -1/3)$ | $(1, 1, 1)$ | $(2/3, 1, 1)$, $(1, 0, 1)$, $(1, 1, 2/3)$ | Triangle symmetric with respect to the $x$ and $z$ axes |
| **j** | $(3\, \bar{1}\, 3)$ | $(1/3,\, -1,\, 1/3)$ | $(0, 1, 0)$ | $(1/3, 1, 0)$, $(0, 0, 0)$, $(0, 1, 1/3)$ | Triangle symmetric in $x$ and $z$ cutting at $y=0$ |

---

## 🎯 4. Phase 4: Units and Limits

1. **Symmetry Invariance:** The planes $(\bar{3}\bar{1}2)$, $(12\bar{3})$, $(\bar{3}\bar{1}\bar{3})$ and $(3\bar{1}3)$ all belong to the same crystallographic family of planes $\{321\}$ or $\{331\}$ in the cubic lattice. Although their geometric orientation differs because of the choice of axes, they all have the **same interplanar spacing $d_{hkl}$** and the **same planar atomic density $\rho_p$**.
2. **Orthogonality Property:** In all cases, the normal direction vector of the drawn plane is proportional to the index vector $[h\, k\, l]$, rigorously satisfying crystallographic perpendicularity in cubic lattices [Session 3 Slide 52].

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
