---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 1"
dificultad: medium
tags:
  - official-problem
  - solved
  - miller-indices
  - linear-density
  - planar-density
  - volumetric-density
  - fcc
---

# ✏️ Problem: T2-CS01 — Miller Indices and Densities in FCC

## 📄 Official Statement
> **1. Find the Miller indices corresponding to the planes in the figures:**  
> **Figure I, Figure II, Figure III.**  
> **For an FCC structure, with lattice parameter $a$, calculate the linear density along direction $[110]$, the planar density on the plane drawn on figure I and the volumetric density.**  
> *(Solution: I $(\bar{1}1\bar{1})$; II $(\bar{2}31)$; III $(\bar{1}\bar{1}1)$; $\rho_l = \sqrt{2}/a$; $\rho_s = 4/(a^2\sqrt{3})$; $\rho_v = 4/a^3$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Context:
Three crystallographic planes drawn inside cubic cells of edge $a$ are analysed. Afterwards, a Face-Centred Cubic (FCC) lattice of lattice parameter $a$ is evaluated.

### Input Data:
* **Figure I:** The plane passes through the upper right vertex, intersecting the axes at: $x = -a$, $y = a$, $z = -a$ (taking a suitable origin).
* **Figure II:** The plane cuts the axes at $x = -a/2$, $y = a/3$, $z = a$.
* **Figure III:** The plane cuts the axes at $x = -a$, $y = -a$, $z = a$.
* **FCC structure:** Lattice parameter $a$, number of atoms per cell $n = 4$, atomic radius $R = a\sqrt{2}/4$.

### Starting Hypotheses:
1. The cubic lattice is orthonormal ($a=b=c$, $\alpha=\beta=\gamma=90^\circ$).
2. For planes with negative indices, the coordinate origin is conveniently translated to an adjacent vertex of the unit cell [Session 3 Slide 43].
3. Atoms are modelled as rigid spheres in contact along the face diagonals $\langle 110 \rangle$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Before calculating, we identify the governing principles of the official syllabus:
* **Determination of Miller Indices $(h\, k\, l)$ [Session 3 Slides 41-45]:**
  1. Identify the fractional intercept coordinates $(p, q, r)$ with the axes $x, y, z$.
  2. Compute the reciprocals $(1/p, 1/q, 1/r)$.
  3. Reduce to the smallest set of integers by multiplying by the LCM.
* **Linear Density ($\rho_l$) [Session 4 Slide 7]:**
  $$\rho_l = \frac{N_{\text{átomos centrados sobre el segmento}}}{L_{[uvw]}}$$
* **Planar Density ($\rho_s$ or $\rho_p$) [Session 4 Slide 8]:**
  $$\rho_s = \frac{N_{\text{átomos contenidos en el plano}}}{A_{(hkl)}}$$
* **Volumetric Density ($\rho_v$) [Session 4 Slide 7]:**
  $$\rho_v = \frac{n}{V_C} = \frac{n}{a^3}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Miller Indices of the Planes:
* **Figure I:**
  * Translating the origin to the corner $(1, 0, 1)$, the plane intersects the axes at:
    $$x = -1, \quad y = +1, \quad z = -1$$
  * Reciprocals of the intercepts:
    $$\frac{1}{-1} = -1, \quad \frac{1}{+1} = 1, \quad \frac{1}{-1} = -1$$
  * Miller notation:
    $$\mathbf{(\bar{1}1\bar{1})}$$
    *(Note that it belongs to the close-packed family of planes $\{111\}$).*

* **Figure II:**
  * Reading the marks on the axes of Figure II:
    * $x$ axis: intercept at $-a/2 \implies p = -1/2$ (with origin translated to $x=1$).
    * $y$ axis: intercept at $+a/3 \implies q = +1/3$.
    * $z$ axis: intercept at $+a \implies r = +1$.
  * Reciprocals:
    $$\frac{1}{-1/2} = -2, \quad \frac{1}{1/3} = 3, \quad \frac{1}{1} = 1$$
  * Miller notation:
    $$\mathbf{(\bar{2}31)}$$

* **Figure III:**
  * Translating the origin to $(1, 1, 0)$:
    * $x$ axis: intercept at $-1 \implies p = -1$.
    * $y$ axis: intercept at $-1 \implies q = -1$.
    * $z$ axis: intercept at $+1 \implies r = +1$.
  * Reciprocals:
    $$\frac{1}{-1} = -1, \quad \frac{1}{-1} = -1, \quad \frac{1}{1} = 1$$
  * Miller notation:
    $$\mathbf{(\bar{1}\bar{1}1)}$$

---

### 2. Calculations for the FCC Lattice:
* **Linear density along $[110]$:**
  * The direction $[110]$ is the diagonal of the bottom face of the cube.
  * Segment length: $L_{[110]} = a\sqrt{2}$.
  * Number of atoms cut diametrally:
    $$N_{\text{átomos}} = 2 \times \left(\frac{1}{2}\right)_{\text{vértices}} + 1_{\text{centro cara}} = 1 + 1 = 2\text{ átomos}$$
  * Linear density:
    $$\rho_l = \frac{2}{a\sqrt{2}} = \frac{2\sqrt{2}}{2a} = \mathbf{\frac{\sqrt{2}}{a}}$$

* **Planar density on the plane of Figure I $(\bar{1}1\bar{1}) \in \{111\}$:**
  * The $\{111\}$ plane intersects three face diagonals of length $L = a\sqrt{2}$, forming an equilateral triangle.
  * Area of the triangle:
    $$A = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4} (a\sqrt{2})^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$$
  * Atoms contained inside the triangle of the plane:
    $$N_{\text{átomos}} = 3 \times \left(\frac{1}{6}\right)_{\text{vértices}} + 3 \times \left(\frac{1}{2}\right)_{\text{aristas}} = \frac{1}{2} + \frac{3}{2} = 2\text{ átomos}$$
  * Planar density:
    $$\rho_s = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{4}{a^2\sqrt{3}}}$$

* **Volumetric density ($\rho_v$):**
  * The FCC cell has $n = 4$ equivalent atoms in a volume $V_C = a^3$:
    $$\rho_v = \mathbf{\frac{4}{a^3}}$$

---

## 🎯 4. Phase 4: Units and Limits

1. **Dimensionality:**
   * $[\rho_l] = \text{length}^{-1} \implies \frac{\sqrt{2}}{a}$ has dimensions of $\text{atoms/m}$.
   * $[\rho_s] = \text{length}^{-2} \implies \frac{4}{a^2\sqrt{3}}$ has dimensions of $\text{atoms/m}^2$.
   * $[\rho_v] = \text{length}^{-3} \implies \frac{4}{a^3}$ has dimensions of $\text{atoms/m}^3$.
2. **Packing consistency:**
   The $[110]$ direction is the line of maximum linear density in FCC ($\rho_l = 1/(2R)$), and the $\{111\}$ plane is the plane of maximum planar density ($\text{APF}_{\text{planar}} = \pi/(2\sqrt{3}) \approx 90.7\%$), which shows why $\{111\}\langle 110 \rangle$ is the canonical slip system of FCC metals.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
