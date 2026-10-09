---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 16-28"
tags:
  - theory
  - fundamental-concept
  - fcc
  - bcc
  - hcp
  - packing-factor
  - coordination-number
dificultad: medium
prerrequisitos:
  - "[[Concept - Crystal Systems and Bravais Lattices]]"
---

# 📦 Concept: FCC, BCC and HCP Metallic Structures and the Packing Factor

> **Physical Principle:** In metals, because metallic bonding is essentially **non-directional**, atoms (rigid spheres of radius $R$) tend to arrange themselves so as to minimize the Gibbs free energy and maximize the spatial packing density. The three predominant structural metallic lattices are **BCC (Body-Centered Cubic)**, **FCC (Face-Centered Cubic)** and **HCP (Hexagonal Close-Packed)** [Slides 16-17].

---

## 🧮 1. Definition of the Atomic Packing Factor (APF)

The **Atomic Packing Factor (APF)** measures the volume fraction occupied by rigid atomic matter within the unit cell [Slide 16]:

$$\text{APF} = \frac{V_{\text{atoms}}}{V_{\text{cell}}} = \frac{n \cdot V_{\text{sphere}}}{V_C} = \frac{n \cdot \left(\frac{4}{3}\pi R^3\right)}{V_C}$$

where:
* $n$: number of equivalent or net atoms contained in the unit cell.
* $R$: effective atomic radius.
* $V_C$: total geometric volume of the unit cell.
* $\text{NC}$ (Coordination Number): number of nearest atomic neighbors in direct contact with each atom.

### 1.1 Reference Case: Simple Cubic (added)
For the simple cubic (SC) cell the atoms touch along the cube edge, so $a = 2R$, there is $n = 8 \times \tfrac18 = 1$ atom per cell and the coordination number is $6$:

$$\text{APF}_{\text{SC}} = \frac{1\cdot\frac43\pi R^3}{(2R)^3} = \frac{4\pi R^3/3}{8R^3} = \frac{\pi}{6} \approx 0.5236$$

SC is rare in metals (only polonium) because it leaves $48\%$ of the volume empty. Ordering the four cases by APF, $0.52 < 0.68 < 0.74 = 0.74$, shows why metals prefer BCC, FCC or HCP. A Python check of all four expressions gives $0.5236$, $0.6802$, $0.7405$ and $0.7405$.

---

## 🟥 2. Body-Centered Cubic (BCC) Structure

### Geometry and Lattice Parameter [Slide 18]
* **Atomic contact:** Atoms touch along the main diagonal of the cube $[111]$.
* **Geometric relation:**
  $$\text{Cube diagonal} = \sqrt{a^2 + a^2 + a^2} = a\sqrt{3} = 4R \implies a = \frac{4R}{\sqrt{3}}$$
* **Number of net atoms ($n$):**
  $$n = 8 \times \left(\frac{1}{8}\right)_{\text{corners}} + 1_{\text{center}} = 2\text{ atoms/cell}$$
* **Coordination number:** $\text{NC} = 8$ (the central atom touches the 8 corner atoms).
* **APF calculation [Slide 19]:**
  $$V_C = a^3 = \left(\frac{4R}{\sqrt{3}}\right)^3 = \frac{64 R^3}{3\sqrt{3}}$$
  $$\text{APF}_{\text{BCC}} = \frac{2 \cdot \frac{4}{3}\pi R^3}{\frac{64 R^3}{3\sqrt{3}}} = \frac{\frac{8}{3}\pi R^3}{\frac{64}{3\sqrt{3}} R^3} = \frac{\pi\sqrt{3}}{8} \approx 0.6802 \implies \mathbf{68\%}$$
* **Relative volume of interstices:** $V_{\text{voids}} / V_C = 1 - 0.68 = 0.32$ ($32\%$ free space).
* **Representative metals:** $\alpha\text{-Fe}$ (ferrite at $T < 912^\circ\text{C}$), $\text{Cr}, \text{Mo}, \text{W}, \text{Ta}, \text{V}, \text{Nb}$.

---

## 🟦 3. Face-Centered Cubic (FCC) Structure

### Geometry and Lattice Parameter [Slide 20]
* **Atomic contact:** Atoms are in direct contact along the face diagonals $\langle 110 \rangle$.
* **Geometric relation:**
  $$\text{Face diagonal} = \sqrt{a^2 + a^2} = a\sqrt{2} = 4R \implies a = \frac{4R}{\sqrt{2}} = 2\sqrt{2} R$$
* **Number of net atoms ($n$):**
  $$n = 8 \times \left(\frac{1}{8}\right)_{\text{corners}} + 6 \times \left(\frac{1}{2}\right)_{\text{faces}} = 1 + 3 = 4\text{ atoms/cell}$$
* **Coordination number:** $\text{NC} = 12$ (each atom at a face center touches 4 corner atoms and 8 adjacent face centers).
* **APF calculation [Slide 21]:**
  $$V_C = a^3 = (2\sqrt{2}R)^3 = 16\sqrt{2} R^3$$
  $$\text{APF}_{\text{FCC}} = \frac{4 \cdot \frac{4}{3}\pi R^3}{16\sqrt{2} R^3} = \frac{\frac{16}{3}\pi R^3}{16\sqrt{2} R^3} = \frac{\pi}{3\sqrt{2}} = \frac{\pi\sqrt{2}}{6} \approx 0.7405 \implies \mathbf{74\%}$$
* **Relative volume of interstices:** $V_{\text{voids}} / V_C = 1 - 0.74 = 0.26$ ($26\%$ free space).
* **Representative metals:** $\text{Al}, \text{Cu}, \text{Ni}, \text{Au}, \text{Ag}, \text{Pt}, \gamma\text{-Fe}$ (austenite).

---

## 🟩 4. Hexagonal Close-Packed (HCP) Structure

### Geometry and Ideal Axial Ratio $c/a$ [Slides 22-25]
The hexagonal close-packed cell consists of two hexagonal basal planes of parameter $a$ and an intermediate plane with 3 atoms located at mid-height ($c/2$).
* **Contact in the base:** $a = 2R$.
* **Number of net atoms ($n$):**
  $$n = 12 \times \left(\frac{1}{6}\right)_{\text{corners}} + 2 \times \left(\frac{1}{2}\right)_{\text{base centers}} + 3_{\text{mid-plane}} = 2 + 1 + 3 = 6\text{ atoms/cell}$$
* **Rigorous derivation of the ideal ratio $c/a$ [Slide 24]:**
  Consider the regular tetrahedron formed by the three atoms of the intermediate plane and the central atom of the basal plane. The tetrahedron edge is $a$, and its height is $c/2$.
  The distance from a vertex of the base of the equilateral triangle of side $a$ to its centroid is $r_b = \frac{a}{\sqrt{3}}$.
  Applying the Pythagorean theorem:
  $$\left(\frac{c}{2}\right)^2 + r_b^2 = a^2 \implies \frac{c^2}{4} + \frac{a^2}{3} = a^2 \implies \frac{c^2}{4} = \frac{2}{3}a^2$$
  $$\left(\frac{c}{a}\right)^2 = \frac{8}{3} \implies \frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$$
* **Volume of the Hexagonal Cell ($V_C$):**
  The base is composed of 6 equilateral triangles of side $a$:
  $$A_{\text{base}} = 6 \times \left(\frac{\sqrt{3}}{4}a^2\right) = \frac{3\sqrt{3}}{2} a^2$$
  $$V_C = A_{\text{base}} \cdot c = \frac{3\sqrt{3}}{2} a^2 c = \frac{3\sqrt{3}}{2} a^3 \sqrt{\frac{8}{3}} = 3\sqrt{2} a^3$$
  Substituting $a = 2R$:
  $$V_C = 3\sqrt{2} (2R)^3 = 24\sqrt{2} R^3$$
* **APF calculation [Slide 25]:**
  $$\text{APF}_{\text{HCP}} = \frac{6 \cdot \frac{4}{3}\pi R^3}{24\sqrt{2} R^3} = \frac{8\pi R^3}{24\sqrt{2} R^3} = \frac{\pi}{3\sqrt{2}} = \frac{\pi\sqrt{2}}{6} \approx 0.7405 \implies \mathbf{74\%}$$
* **APF as a function of $c/a$ (added check):**
  With $a = 2R$ the cell volume is $V_C = \frac{3\sqrt3}{2}a^2c = 6\sqrt3\,R^2c$, so
  $$\text{APF}_{\text{HCP}} = \frac{6\cdot\frac43\pi R^3}{6\sqrt3\,R^2c} = \frac{4\pi}{3\sqrt3}\,\frac{R}{c} = \frac{2\pi}{3\sqrt3\,(c/a)}$$
  For the ideal $c/a = \sqrt{8/3} = 1.6330$ this gives $\frac{2\pi}{3\sqrt3\sqrt{8/3}} = \frac{2\pi}{3\sqrt8} = \frac{\pi}{3\sqrt2} = 0.7405$, as above. If $a = 2R$ were kept for a larger $c/a$ (for example $1.856$ for zinc), the same formula would give a lower APF ($0.65$), which is why only the ideal ratio reaches the Kepler limit.
* **Coordination number:** $\text{NC} = 12$ (6 in the basal plane itself, 3 in the plane below, 3 in the plane above).
* **Representative metals:** $\alpha\text{-Ti}, \text{Mg}, \text{Zn}, \text{Be}, \text{Cd}, \text{Zr}$.

---

## 🔄 5. Stacking Sequence Comparison: HCP ($ABAB\dots$) vs FCC ($ABCABC\dots$)

Both FCC and HCP reach the theoretical maximum density limit for congruent rigid spheres in 3D ($\text{APF} = 0.7405$, Kepler's theorem). The only difference lies in the periodic stacking sequence of the close-packed planes [Slides 26-28]:

```
Plane A: Initial close-packed hexagonal layer.
Plane B: Sits in the triangular valleys formed by layer A.
Plane C: Sits in the second, alternate group of triangular voids that do NOT coincide vertically with A.

HCP sequence: A - B - A - B - A - B ...  (2-layer period, hexagonal symmetry)
FCC sequence: A - B - C - A - B - C ...  (3-layer period along [111], cubic symmetry)
```

| Property | BCC | FCC | HCP |
| :--- | :--- | :--- | :--- |
| **Relation $a(R)$** | $a = 4R/\sqrt{3}$ | $a = 2\sqrt{2}R$ | $a = 2R,\, c = 1.633 a$ |
| **Atoms/cell ($n$)** | 2 | 4 | 6 |
| **Coord. Number ($\text{NC}$)** | 8 | 12 | 12 |
| **APF** | **0.68** | **0.74** | **0.74** |
| **Close-packed planes** | $\{110\}$ (dense, not close-packed) | $\{111\}$ (4 families) | $(0001)$ (1 basal plane) |
| **Close-packed directions** | $\langle 111 \rangle$ (4 directions) | $\langle 110 \rangle$ (6 directions) | $\langle 11\bar{2}0 \rangle$ (3 directions) |
| **Macroscopic ductility** | Moderate (high at $T \uparrow$) | **Very High (at any $T$)** | Low at room temperature |

---
*Bidirectional Links:*
* [[Concept - Crystal Systems and Bravais Lattices|⬅️ Previous: Crystal Systems and Bravais Lattices]]
* [[Concept - Tetrahedral and Octahedral Interstitial Sites|Next: Tetrahedral and Octahedral Interstitial Sites ➡️]]
