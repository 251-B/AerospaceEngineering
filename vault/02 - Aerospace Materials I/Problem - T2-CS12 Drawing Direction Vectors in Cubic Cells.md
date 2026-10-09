---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 12"
dificultad: medium
tags:
  - official-problem
  - solved
  - crystallographic-directions
  - cubic-lattice
  - miller-indices
  - vector-drawing
---

# ✏️ Problem: T2-CS12 — Drawing Direction Vectors in Cubic Cells

## 📄 Official Statement
> **12. Draw direction vectors in unit cells for the following cubic directions:**  
> **a)** $[1\, 1\, 2]$  
> **b)** $[\bar{3}\, 3\, 1]$  
> **c)** $[2\, 1\, 2]$  
> **d)** $[\bar{1}\, 0\, 1]$  
> **e)** $[3\, 2\, 1]$  
> **f)** $[1\, 2\, 2]$  
> **g)** $[\bar{1}\, 2\, 3]$  
> **h)** $[0\, \bar{2}\, 1]$  
> **i)** $[2\, \bar{3}\, 3]$  
> **j)** $[1\, 2\, \bar{1}]$  
> **k)** $[2\, 2\, 3]$  
> **l)** $[\bar{1}\, 0\, 3]$

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Geometric Context:
Twelve crystallographic vectors are drawn inside a standard cubic unit cell of normalised dimensions $1 \times 1 \times 1$.

### Normalisation and Origin Translation Rules [Session 3 Slides 37-40]:
1. The components of the direction vector must be reduced by dividing by the component of largest absolute value ($u_{\text{max}}$) so that the vector fits strictly inside the volume of a single unit cell:
   $$\vec{r} = \left(\frac{u}{u_{\text{max}}}, \frac{v}{u_{\text{max}}}, \frac{w}{u_{\text{max}}}\right)$$
2. If any component is negative (overbar $\bar{u}$), the **origin of the vector must be translated** to the position $+1$ along that axis so that the vector points towards the interior of the cell.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the systematic procedure [Session 3 Slide 38]:
1. Identify whether there are negative indices and fix the local origin:
   * $\bar{u} \implies$ origin at $x = 1$.
   * $\bar{v} \implies$ origin at $y = 1$.
   * $\bar{w} \implies$ origin at $z = 1$.
2. Draw the vector from the origin $(x_0, y_0, z_0)$ to the end point $(x_0 + \Delta x, y_0 + \Delta y, z_0 + \Delta z)$.
3. Join both points with an oriented arrow.

---

## 🔢 3. Phase 3: Step-by-Step Derivation of the 12 Directions

| Letter | Direction $[u\,v\,w]$ | Normalisation $(\Delta x, \Delta y, \Delta z)$ | Local Origin $(x_0, y_0, z_0)$ | Vector End Point $(x_f, y_f, z_f)$ | Geometric Description of the Vector |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **a** | $[1\, 1\, 2]$ | $(1/2,\, 1/2,\, 1)$ | $(0, 0, 0)$ | $(1/2, 1/2, 1)$ | From the origin to the centre of the top face $z=1$ |
| **b** | $[\bar{3}\, 3\, 1]$ | $(-1,\, 1,\, 1/3)$ | $(1, 0, 0)$ | $(0, 1, 1/3)$ | From the vertex $(1,0,0)$ to the left face at $z=1/3$ |
| **c** | $[2\, 1\, 2]$ | $(1,\, 1/2,\, 1)$ | $(0, 0, 0)$ | $(1, 1/2, 1)$ | From the origin to the midpoint of the upper right edge |
| **d** | $[\bar{1}\, 0\, 1]$ | $(-1,\, 0,\, 1)$ | $(1, 0, 0)$ | $(0, 0, 1)$ | Face diagonal in the $x-z$ plane, from $(1,0,0)$ to $(0,0,1)$ |
| **e** | $[3\, 2\, 1]$ | $(1,\, 2/3,\, 1/3)$ | $(0, 0, 0)$ | $(1, 2/3, 1/3)$ | Crosses the interior of the cell towards the right face $x=1$ |
| **f** | $[1\, 2\, 2]$ | $(1/2,\, 1,\, 1)$ | $(0, 0, 0)$ | $(1/2, 1, 1)$ | Towards the upper front edge |
| **g** | $[\bar{1}\, 2\, 3]$ | $(-1/3,\, 2/3,\, 1)$ | $(1, 0, 0)$ | $(2/3, 2/3, 1)$ | Rises towards the top face, leaving from $x=1$ |
| **h** | $[0\, \bar{2}\, 1]$ | $(0,\, -1,\, 1/2)$ | $(0, 1, 0)$ | $(0, 0, 1/2)$ | Parallel to the $y-z$ plane, from $(0,1,0)$ to the $z$ edge at mid-height |
| **i** | $[2\, \bar{3}\, 3]$ | $(2/3,\, -1,\, 1)$ | $(0, 1, 0)$ | $(2/3, 0, 1)$ | From $(0,1,0)$ towards the top face $z=1$ |
| **j** | $[1\, 2\, \bar{1}]$ | $(1/2,\, 1,\, -1/2)$ | $(0, 0, 1)$ | $(1/2, 1, 1/2)$ | From the top face $(0,0,1)$ downwards onto the face $y=1$ |
| **k** | $[2\, 2\, 3]$ | $(2/3,\, 2/3,\, 1)$ | $(0, 0, 0)$ | $(2/3, 2/3, 1)$ | Vector symmetric in $x$ and $y$ towards the top face $z=1$ |
| **l** | $[\bar{1}\, 0\, 3]$ | $(-1/3,\, 0,\, 1)$ | $(1, 0, 0)$ | $(2/3, 0, 1)$ | Contained in the $x-z$ plane, from $(1,0,0)$ to $(2/3, 0, 1)$ |

---

## 🎯 4. Phase 4: Units and Limits

1. **Parallelism:** If we multiply a vector by a positive scalar constant, the direction does not change: $[1\, 1\, 2]$ and $[2\, 2\, 4]$ represent exactly the **same crystallographic direction**.
2. **Equivalence of $\langle u\, v\, w \rangle$ Families:** Directions such as $[1\, 2\, 2]$ and $[2\, 1\, 2]$ are symmetric members of the $\langle 221 \rangle$ family in the cubic lattice, which implies that they have identical translational repeat length and the same physical properties of conductivity or elastic modulus.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
