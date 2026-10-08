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
  $$\rho_{(hkl)} = \frac{N_{\text{átomos contenidos en la cara o sección}}}{A_{(hkl)}}$$
* **Linear Density ($\rho_{[uvw]}$):**
  $$\rho_{[uvw]} = \frac{N_{\text{átomos cortados diametralmente}}}{L_{[uvw]}}$$
* **Volumetric Density ($\rho_v$):**
  $$\rho_v = \frac{n}{V_C} = \frac{2}{a^3}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Planar Density on the $(100)$ Plane:
* **Plane geometry:** Outer face of the cube, of dimensions $a \times a$.
* **Area:** $A_{(100)} = a^2$.
* **Atoms contained:** Only the 4 atoms located at the vertices of the square (the central atom of the BCC cell is at $z = a/2$, so it does not belong to the plane $z=0$ or $x=0$).
  $$N_{\text{átomos}} = 4 \times \frac{1}{4} = 1\text{ átomo}$$
* **Planar density:**
  $$\rho_{(100)} = \frac{1}{a^2} = \mathbf{\frac{1}{a^2}}$$

### 2. Planar Density on the $(110)$ Plane:
* **Plane geometry:** Diagonal rectangle crossing the cube through two opposite edges.
* **Dimensions:** Base $= a\sqrt{2}$ (face diagonal), Height $= a$.
* **Area:**
  $$A_{(110)} = a\sqrt{2} \times a = a^2\sqrt{2}$$
* **Atoms contained:**
  * 4 vertices of the rectangle, each contributing $\frac{1}{4}$: $4 \times \frac{1}{4} = 1\text{ átomo}$.
  * 1 atom at the geometric centre of the cell (the $(110)$ plane passes exactly through the centre of the cube): it contributes a whole $1\text{ átomo}$.
  * Total atoms: $N_{\text{átomos}} = 1 + 1 = 2\text{ átomos}$.
* **Planar density:**
  $$\rho_{(110)} = \frac{2}{a^2\sqrt{2}} = \frac{2\sqrt{2}}{2a^2} = \mathbf{\frac{\sqrt{2}}{a^2}}$$

### 3. Planar Density on the $(111)$ Plane:
* **Geometry and spacing:**
  In the BCC lattice, the parallel $(111)$ planes have an interplanar spacing $d_{111} = \frac{a}{\sqrt{1^2+1^2+1^2}} = \frac{a}{\sqrt{3}}$.
  However, because the central atom sits exactly at the midpoint of the cube diagonal along $[111]$, the real $(111)$ planes alternate at an effective distance $d_{\text{eff}} = \frac{a}{2\sqrt{3}}$ (corresponding to the reflected family $\{222\}$).
* **Direct calculation by cell or density relation:**
  Using the fundamental conservation relation between densities [Session 4 Slide 9]:
  $$\rho_v = \frac{\rho_{(hkl)}}{d_{\text{eff}}} \implies \rho_{(111)} = \rho_v \cdot d_{\text{eff}} = \left(\frac{2}{a^3}\right) \cdot \left(\frac{a}{2\sqrt{3}}\right) = \mathbf{\frac{1}{a^2\sqrt{3}}}$$
* **Direct check by geometric area:**
  The plane that cuts the vertices $(a, 0, 0)$, $(0, a, 0)$, $(0, 0, a)$ forms an equilateral triangle of side $L = a\sqrt{2}$ and area $A = \frac{\sqrt{3}}{4}(a\sqrt{2})^2 = \frac{\sqrt{3}}{2}a^2$.
  The plane does not contain the central atom (it lies at $(a/2, a/2, a/2)$, whose distance to the origin is $\frac{a\sqrt{3}}{2}$, while the plane is at $\frac{a}{\sqrt{3}}$).
  Therefore, the plane contains only the 3 vertices: $N_{\text{átomos}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ átomo}$.
  $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

### 4. Linear Density in the $[100]$ Direction:
* **Edge segment length:** $L_{[100]} = a$.
* **Atoms cut:** It cuts the two vertex atoms at their ends:
  $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
* **Linear density:**
  $$\rho_{[100]} = \frac{1}{a} = \mathbf{\frac{1}{a}}$$

### 5. Volumetric Density ($\rho_v$):
* It contains $n = 2$ atoms in a cell volume $V_C = a^3$:
  $$\rho_v = \mathbf{\frac{2}{a^3}}$$

---

## 🎯 4. Phase 4: Units and Limits

Comparing the planar densities obtained in the BCC lattice:
* $\rho_{(110)} = \frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$
* $\rho_{(100)} = \frac{1}{a^2} = \frac{1.000}{a^2}$
* $\rho_{(111)} = \frac{1}{a^2\sqrt{3}} \approx \frac{0.577}{a^2}$

$$\rho_{(110)} > \rho_{(100)} > \rho_{(111)}$$

The $(110)$ plane is the plane of **highest atomic density of the BCC structure**, rigorously confirming why the $\{110\}$ family is the preferred slip plane for dislocations in BCC metals such as ferritic iron ($\alpha\text{-Fe}$), molybdenum, tantalum and tungsten [Session 4 Slide 36].

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
