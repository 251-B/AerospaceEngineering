---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 4"
dificultad: medium
tags:
  - official-problem
  - solved
  - planar-density
  - linear-density
  - volumetric-density
  - bcc
---

# ✏️ Problem: T2-CS04 — Planar and Linear Densities in the BCC Lattice

## 📄 Official Statement
> **4. For a BCC structure, determine the surface (planar) density for the planes $(100)$, $(110)$ and $(111)$; the linear density in the direction $[100]$, and the volume density.**  
> *(Solution: $\rho_{(100)} = 1/a^2$, $\rho_{(110)} = \sqrt{2}/a^2$, $\rho_{(111)} = 1/(a^2\sqrt{3})$, $\rho_{[100]} = 1/a$, $\rho_v = 2/a^3$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Context:
A Body-Centred Cubic (BCC) lattice with lattice parameter $a$ is studied.

### BCC Lattice Data:
* Atoms per unit cell: $n = 2$ (8 at vertices $\times 1/8$ + 1 central).
* Volume of the cubic cell: $V_C = a^3$.
* Atomic radius: $R = \frac{a\sqrt{3}}{4}$ (contact along the cube diagonal $\langle 111 \rangle$).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Applying the formal definitions of the course [Session 4 Slides 7-9]:
* **Planar Density ($\rho_{(hkl)}$):**
  $$\rho_{(hkl)} = \frac{N_{\text{atoms contained in the face or section}}}{A_{(hkl)}}$$
* **Linear Density ($\rho_{[uvw]}$):**
  $$\rho_{[uvw]} = \frac{N_{\text{atoms cut diametrically}}}{L_{[uvw]}}$$
* **Volumetric Density ($\rho_v$):**
  $$\rho_v = \frac{n}{V_C} = \frac{2}{a^3}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Planar Density on the $(100)$ Plane:
* **Plane geometry:** Outer face of the cube, of dimensions $a \times a$.
* **Area:** $A_{(100)} = a^2$.
* **Atoms contained:** Only the 4 atoms located at the vertices of the square (the central atom of the BCC cell is at $z = a/2$, so it does not belong to the plane $z=0$ or $x=0$).
  $$N_{\text{atoms}} = 4 \times \frac{1}{4} = 1\text{ atom}$$
* **Planar density:**
  $$\rho_{(100)} = \frac{1}{a^2} = \mathbf{\frac{1}{a^2}}$$

### 2. Planar Density on the $(110)$ Plane:
* **Plane geometry:** Diagonal rectangle crossing the cube through two opposite edges.
* **Dimensions:** Base $= a\sqrt{2}$ (face diagonal), Height $= a$.
* **Area:**
  $$A_{(110)} = a\sqrt{2} \times a = a^2\sqrt{2}$$
* **Atoms contained:**
  * 4 vertices of the rectangle, each contributing $\frac{1}{4}$: $4 \times \frac{1}{4} = 1\text{ atom}$.
  * 1 atom at the geometric centre of the cell (the $(110)$ plane passes exactly through the centre of the cube): it contributes a whole $1\text{ atom}$.
  * Total atoms: $N_{\text{atoms}} = 1 + 1 = 2\text{ atoms}$.
* **Planar density:**
  $$\rho_{(110)} = \frac{2}{a^2\sqrt{2}} = \frac{2\sqrt{2}}{2a^2} = \mathbf{\frac{\sqrt{2}}{a^2}}$$

### 3. Planar Density on the $(111)$ Plane:
* **Geometry and spacing:**
  In the BCC lattice, the parallel $(111)$ planes have an interplanar spacing $d_{111} = \frac{a}{\sqrt{1^2+1^2+1^2}} = \frac{a}{\sqrt{3}}$.
  However, because the central atom sits exactly at the midpoint of the cube diagonal along $[111]$, the real $(111)$ planes alternate at an effective distance $d_{\text{eff}} = \frac{a}{2\sqrt{3}}$ (corresponding to the reflected family $\{222\}$).
* **Direct calculation by cell or density relation:**
  Using the relation $\rho_{(hkl)} = \rho_v \cdot d$ between the volume density and the spacing $d$ of consecutive atomic layers (extension: the slides only define $\rho_{(hkl)}$ as atoms over area [Session 4 Slide 9]; the direct count below is the course method):
  $$\rho_v = \frac{\rho_{(hkl)}}{d_{\text{eff}}} \implies \rho_{(111)} = \rho_v \cdot d_{\text{eff}} = \left(\frac{2}{a^3}\right) \cdot \left(\frac{a}{2\sqrt{3}}\right) = \mathbf{\frac{1}{a^2\sqrt{3}}}$$
* **Direct check by geometric area:**
  The plane that cuts the vertices $(a, 0, 0)$, $(0, a, 0)$, $(0, 0, a)$ forms an equilateral triangle of side $L = a\sqrt{2}$ and area $A = \frac{\sqrt{3}}{4}(a\sqrt{2})^2 = \frac{\sqrt{3}}{2}a^2$.
  The plane does not contain the central atom (it lies at $(a/2, a/2, a/2)$, whose distance to the origin is $\frac{a\sqrt{3}}{2}$, while the plane is at $\frac{a}{\sqrt{3}}$).
  Therefore, the plane contains only the 3 vertices: $N_{\text{atoms}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ atom}$.
  $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

### 4. Linear Density in the $[100]$ Direction:
* **Edge segment length:** $L_{[100]} = a$.
* **Atoms cut:** It cuts the two vertex atoms at their ends:
  $$N_{\text{atoms}} = 2 \times \frac{1}{2} = 1\text{ atom}$$
* **Linear density:**
  $$\rho_{[100]} = \frac{1}{a} = \mathbf{\frac{1}{a}}$$

### 5. Volumetric Density ($\rho_v$):
* It contains $n = 2$ atoms in a cell volume $V_C = a^3$:
  $$\rho_v = \mathbf{\frac{2}{a^3}}$$

---

## 🎯 4. Phase 4: Interpretation and Verification

### 1. Ranking of the planes
Comparing the planar densities obtained in the BCC lattice:
* $\rho_{(110)} = \frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$
* $\rho_{(100)} = \frac{1}{a^2} = \frac{1.000}{a^2}$
* $\rho_{(111)} = \frac{1}{a^2\sqrt{3}} = \frac{\sqrt{3}}{3a^2} \approx \frac{0.577}{a^2}$

$$\rho_{(110)} > \rho_{(100)} > \rho_{(111)}$$

The $(110)$ plane is the densest plane of the BCC structure, which is why $\{110\}$ is the slip plane of BCC metals, with slip direction $\langle 111 \rangle$ [Session 4 Slide 37].

### 2. Cross-check with the volume density (extension)
Every plane of atoms carries $\rho_{(hkl)}$ atoms per unit area and consecutive atomic layers are a distance $d$ apart, so a slab of area $A$ and thickness $d$ holds $\rho_{(hkl)} A$ atoms in a volume $A d$: $\rho_v = \rho_{(hkl)}/d$. With $\rho_v = 2/a^3$:

| Plane | Atomic layers (coordinates in units of $a$) | $d$ | $\rho_v \cdot d$ | Direct count |
| :---: | :--- | :---: | :---: | :---: |
| $(100)$ | corners at $x = 0, 1$; body centre at $x = \tfrac12$ | $\frac{a}{2}$ | $\frac{2}{a^3}\cdot\frac{a}{2} = \frac{1}{a^2}$ | $\frac{1}{a^2}$ ✓ |
| $(110)$ | $x + y = 0, 1, 2$ (the body centre has $x + y = \tfrac12 + \tfrac12 = 1$) | $\frac{a}{\sqrt{2}}$ | $\frac{2}{a^3}\cdot\frac{a}{\sqrt{2}} = \frac{\sqrt{2}}{a^2}$ | $\frac{\sqrt{2}}{a^2}$ ✓ |
| $(111)$ | $x + y + z = 0, 1, \tfrac32, 2, 3$ | $\frac{a}{2\sqrt{3}}$ | $\frac{2}{a^3}\cdot\frac{a}{2\sqrt{3}} = \frac{1}{a^2\sqrt{3}}$ | $\frac{1}{a^2\sqrt{3}}$ ✓ |

For $(111)$ the layers $x+y+z = 1$ and $\tfrac32$ are $\frac{(3/2 - 1)\,a}{\sqrt{1^2+1^2+1^2}} = \frac{a}{2\sqrt{3}}$ apart (distance between parallel planes $x+y+z = c_1$ and $c_2$ is $|c_2 - c_1|\,a/\sqrt{3}$).

### 3. Linear density and contact
Along $[100]$ the atoms do not touch: their centres are $a$ apart, while their diameter is $2R = \frac{a\sqrt{3}}{2} \approx 0.866\,a$ (contact is along $\langle 111 \rangle$ [Session 4 Slide 5]). Hence $\rho_{[100]} = 1/a$ is lower than the close-packed limit $1/(2R) = \frac{2}{a\sqrt{3}} \approx \frac{1.155}{a}$ that is reached along $[111]$.

### 4. Dimensional check
$[\rho_{(hkl)}] = \frac{\text{atoms}}{\text{m}^2}$, $[\rho_{[100]}] = \frac{\text{atoms}}{\text{m}}$ and $[\rho_v] = \frac{\text{atoms}}{\text{m}^3}$, consistent with $a$ in m; in the cross-check, $[\rho_v \cdot d] = \text{m}^{-3}\cdot\text{m} = \text{m}^{-2}$ ✓.

### 5. Comparison with the official answer
All five results agree with the official solution: $\rho_{(100)} = 1/a^2$, $\rho_{(110)} = \sqrt{2}/a^2$, $\rho_{(111)} = 1/(a^2\sqrt{3})$, $\rho_{[100]} = 1/a$, $\rho_v = 2/a^3$.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
