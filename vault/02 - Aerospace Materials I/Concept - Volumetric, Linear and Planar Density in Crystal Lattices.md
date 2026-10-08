---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 7-9"
tags:
  - theory
  - fundamental-concept
  - volumetric-density
  - linear-density
  - planar-density
  - crystal-calculations
dificultad: medium
prerrequisitos:
  - "[[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes]]"
---

# ⚖️ Concept: Volumetric, Linear and Planar Density in Crystal Lattices

> **Overall Definition:** Mechanical properties, elastic anisotropy, resistance to dislocation creep and corrosion rates depend strongly on the **atomic packing density** evaluated in 3 dimensions (volume), 2 dimensions (crystallographic planes) and 1 dimension (crystallographic directions) [Slides 7-9].

---

## 🧊 1. Volumetric Density ($\rho$ or $\rho_v$)

The theoretical volumetric density is the total mass contained within the unit cell divided by the volume of that cell [Slide 15, Session 4]:

$$\rho_v = \frac{m_{\text{cell}}}{V_C} = \frac{n \cdot M}{V_C \cdot N_A}$$

where:
* $n$: number of equivalent atoms per unit cell ($n_{\text{BCC}} = 2$, $n_{\text{FCC}} = 4$, $n_{\text{HCP}} = 6$).
* $M$: molar atomic mass of the element ($\text{g/mol}$).
* $V_C$: unit cell volume ($V_{\text{cubic}} = a^3$; $V_{\text{orthorhombic}} = a \cdot b \cdot c$; $V_{\text{HCP}} = \frac{3\sqrt{3}}{2}a^2 c$).
* $N_A$: Avogadro's number ($6.022 \times 10^{23}\text{ atoms/mol}$).

### Canonical Example: Pure Copper ($\text{Cu}$, FCC) [Session 4 Slide 7]
* Data: $M = 63.546\text{ g/mol}$, $R = 1.28\text{ \AA} = 1.28 \times 10^{-8}\text{ cm}$, $n = 4$.
* FCC lattice parameter: $a = 2\sqrt{2} R = 2\sqrt{2}(1.28 \times 10^{-8}) = 3.62 \times 10^{-8}\text{ cm}$.
* Cell volume: $V_C = a^3 = (3.6204 \times 10^{-8}\text{ cm})^3 = 4.745 \times 10^{-23}\text{ cm}^3$.
* Theoretical density:
  $$\rho_v = \frac{4 \times 63.546}{4.745 \times 10^{-23} \times 6.022 \times 10^{23}} = \frac{254.18}{28.58} = \mathbf{8.90\text{ g/cm}^3}$$
  *(The slide, with $M = 63.5$ and $N_A = 6.023 \times 10^{23}$, obtains $8.89\text{ g/cm}^3$; it quotes $8.94\text{ g/cm}^3$ from the bibliography. The $0.5\%$ gap comes from the rounded $R = 1.28\text{ \AA}$: with $a = 3.615\text{ \AA}$ the same formula gives $8.935\text{ g/cm}^3$).*

---

## 📏 2. Linear Density ($\rho_l$)

The linear density represents the number of atomic diameters centered on a crystallographic direction vector or segment $[u\, v\, w]$ divided by the geometric length of that vector [Slide 7]:

$$\rho_l = \frac{N_{\text{atoms centered on the line}}}{L_{[u\, v\, w]}}$$

* If a line passes through an atom at its exact center within the cell segment, it counts as $1$ whole atom.
* If it cuts atoms at both ends of the edge or diagonal, each end contributes $\frac{1}{2}$ atom $\implies 2 \times \frac{1}{2} = 1$ atom.

### Examples in Cubic Lattices:
1. **FCC along the $[100]$ direction [Slide 7]:**
   * $L_{[100]} = a = 2\sqrt{2}R$.
   * It intersects 2 corners: $2 \times \frac{1}{2} = 1\text{ atom}$.
   * For Cu ($R = 1.28\text{ \AA}$):
     $$\rho_l [100] = \frac{1\text{ at}}{2\sqrt{2}(1.28 \times 10^{-8}\text{ cm})} = 2.76 \times 10^7\text{ at/cm} = 2.76 \times 10^9\text{ at/m}$$
2. **FCC along the $[110]$ direction (Direction of Maximum Packing):**
   * $L_{[110]} = a\sqrt{2} = 4R$.
   * It intersects 2 corners ($2 \times 1/2$) + 1 whole face center = $2\text{ atoms}$.
   * Linear density:
     $$\rho_l [110] = \frac{2\text{ at}}{4R} = \frac{1}{2R} = \frac{\sqrt{2}}{a} = \frac{1}{2(1.28 \times 10^{-8})} = 3.91 \times 10^7\text{ at/cm}$$
3. **BCC along the $[111]$ direction (Direction of Maximum Packing):**
   * $L_{[111]} = a\sqrt{3} = 4R$.
   * It intersects 2 corners ($2 \times 1/2$) + 1 central atom = $2\text{ atoms}$.
     $$\rho_l [111] = \frac{2}{a\sqrt{3}} = \frac{1}{2R}$$

---

## 🗺️ 3. Planar Density ($\rho_p$)

The planar density quantifies the number of atoms whose geometric centers are contained in the crystallographic plane $(h\, k\, l)$, divided by the two-dimensional area bounded by the unit cell in that plane [Slide 8]:

$$\rho_p = \frac{N_{\text{atoms contained in the plane}}}{A_{(h\, k\, l)}}$$

* A fraction of an atom counts according to the angle that the plane boundary subtends at that atom:
  * Vertex of a square / rectangle ($90^\circ$): contributes $\frac{90^\circ}{360^\circ} = \frac{1}{4}$.
  * Vertex of an equilateral triangle in the $(111)$ plane ($60^\circ$): contributes $\frac{60^\circ}{360^\circ} = \frac{1}{6}$.
  * Atom on an edge shared between two cells: contributes $\frac{180^\circ}{360^\circ} = \frac{1}{2}$.
  * Atom entirely within the interior of the plane: contributes $1$.

### Examples in Cubic Lattices:
1. **FCC in the $(100)$ plane [Slide 8]:**
   * Area: $A_{(100)} = a^2$.
   * Atoms contained: 4 corners $\times \frac{1}{4} + 1\text{ face center} = 1 + 1 = 2\text{ atoms}$.
   * Analytical expression: $\rho_p (100) = \frac{2}{a^2}$.
   * For Cu: $\rho_p (100) = \frac{2}{(3.62 \times 10^{-8}\text{ cm})^2} = 1.52 \times 10^{15}\text{ at/cm}^2$.
2. **FCC in the $(110)$ plane:**
   * Rectangle dimensions: base $a\sqrt{2}$, height $a \implies A_{(110)} = \sqrt{2}a^2$.
   * Atoms contained: 4 corners $\times \frac{1}{4} + 2\text{ centers on face edges} \times \frac{1}{2} = 1 + 1 = 2\text{ atoms}$.
   * Analytical expression: $\rho_p (110) = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$.
3. **FCC in the $(111)$ plane (Close-Packed Slip Plane):**
   * The $(111)$ plane cuts the face diagonals forming an equilateral triangle of side $L = a\sqrt{2}$.
   * Area: $A_{(111)} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$.
   * Atoms contained: 3 corners $\times \frac{1}{6} + 3\text{ centers on the sides} \times \frac{1}{2} = \frac{1}{2} + \frac{3}{2} = 2\text{ atoms}$.
   * Analytical expression:
     $$\rho_p (111) = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \frac{4}{a^2\sqrt{3}}$$
4. **BCC in the $(110)$ plane (Densest Plane of BCC):**
   * Dimensions: base $a\sqrt{2}$, height $a \implies A_{(110)} = \sqrt{2}a^2$.
   * Atoms: 4 corners $\times \frac{1}{4} + 1\text{ whole central atom} = 2\text{ atoms}$.
   * Analytical expression:
     $$\rho_p (110) = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$

---

## 💡 4. Fundamental Relation between Densities and Interplanar Spacing

The volumetric density $\rho_v$ of atoms is related to the planar density $\rho_p$ of a family of planes $(hkl)$ by the spacing $d_p$ between **consecutive planes that contain atoms**:

$$\rho_v = \frac{\rho_p(hkl)}{d_p}$$

$d_p$ equals the crystallographic $d_{hkl} = a/\sqrt{h^2+k^2+l^2}$ only when every plane of the family is populated (BCC $(110)$: $\rho_p = \sqrt{2}/a^2$, $d_p = a/\sqrt{2}$, $\rho_v = 2/a^3$; FCC $(111)$: $\rho_p = 4/(\sqrt{3}a^2)$, $d_p = a/\sqrt{3}$, $\rho_v = 4/a^3$). When a mid-plane is also populated, $d_p = d_{hkl}/2$: BCC $(100)$ has $\rho_p = 1/a^2$ (corner atoms) plus a second set of atoms in the plane at $a/2$, so $d_p = a/2$ and $\rho_v = (1/a^2)/(a/2) = 2/a^3$ (using $d_{100} = a$ would give the wrong $1/a^3$); likewise FCC $(100)$: $\rho_p = 2/a^2$, $d_p = a/2$, $\rho_v = 4/a^3$.

With this relation, the most densely packed planes (largest $\rho_p$) are simultaneously those with the **largest spacing $d_p$ between atomic planes**, which explains why they are the preferred planes for dislocation slip (lowest Peierls-Nabarro lattice resistance).

---
*Bidirectional Links:*
* [[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes|⬅️ Previous: Miller Notation]]
* [[Concept - X-Ray Diffraction and Bragg's Law|Next: X-Ray Diffraction and Bragg's Law ➡️]]
