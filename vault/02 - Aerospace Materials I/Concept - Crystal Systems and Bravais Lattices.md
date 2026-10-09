---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 7-14"
tags:
  - theory
  - fundamental-concept
  - crystallography
  - bravais-lattices
  - crystal-systems
dificultad: low
prerrequisitos:
  - "Topic 1: Bonding in Solids"
---

# 🔷 Concept: Crystal Systems and the 14 Bravais Lattices

> **Central Definition:** A **crystal system** is a geometric classification of three-dimensional space based on the length relations of its three cell base vectors ($a, b, c$) and the three interaxial angles ($\alpha, \beta, \gamma$). By combining the **7 crystal systems** with the **4 unit cell types** (Primitive $P$, Body-centered $I$, Face-centered $F$ and Base-centered $C$), the French physicist **Auguste Bravais (1848)** showed that there exist exactly **14 independent three-dimensional periodic lattices** capable of filling space without discontinuities or overlaps [Slide 8].

---

## 📐 1. Unit Cell Lattice Parameters

Any three-dimensional unit cell is formally defined by a common origin and three primary translation vectors $\vec{a}, \vec{b}, \vec{c}$ [Slide 7]:
* **Axial lengths:** $a = |\vec{a}|$, $b = |\vec{b}|$, $c = |\vec{c}|$.
* **Interaxial angles:**
  * $\alpha$: angle subtended between $\vec{b}$ and $\vec{c}$.
  * $\beta$: angle subtended between $\vec{a}$ and $\vec{c}$.
  * $\gamma$: angle subtended between $\vec{a}$ and $\vec{b}$.

$$\text{Unit Cell} \iff \{a, b, c;\, \alpha, \beta, \gamma\}$$

---

## 🏛️ 2. The 7 Crystal Systems

The 7 crystal systems represent the highest possible metric symmetry classes in $\mathbb{R}^3$ [Slides 11-13]:

| Crystal System | Edge Relations | Angle Relations | Characteristic Symmetry |
| :--- | :--- | :--- | :--- |
| **Cubic** | $a = b = c$ | $\alpha = \beta = \gamma = 90^\circ$ | 4 threefold rotation axes $\langle 111 \rangle$ |
| **Tetragonal** | $a = b \neq c$ | $\alpha = \beta = \gamma = 90^\circ$ | 1 fourfold rotation axis $[001]$ |
| **Orthorhombic** | $a \neq b \neq c$ | $\alpha = \beta = \gamma = 90^\circ$ | 3 perpendicular twofold axes |
| **Rhombohedral (Trigonal)** | $a = b = c$ | $\alpha = \beta = \gamma \neq 90^\circ < 120^\circ$ | 1 threefold rotation axis |
| **Hexagonal** | $a = b \neq c$ | $\alpha = \beta = 90^\circ,\, \gamma = 120^\circ$ | 1 sixfold rotation axis $[0001]$ |
| **Monoclinic** | $a \neq b \neq c$ | $\alpha = \gamma = 90^\circ \neq \beta$ | 1 twofold rotation axis |
| **Triclinic** | $a \neq b \neq c$ | $\alpha \neq \beta \neq \gamma \neq 90^\circ$ | Inversion center only ($C_i$) |

---

## 📦 3. The 4 Types of Unit Cell Centering

To locate the atomic motifs within the lattice volume, Bravais categorized four standard arrangements [Slide 9]:

1. **Primitive ($P$ / Simple):**
   * Lattice points located exclusively at the 8 corners of the cell.
   * Effective contribution: $8 \times \frac{1}{8} = 1\text{ net lattice point}$.
2. **Body-Centered ($I$ - *Innenzentrierte*):**
   * Lattice points at the corners plus 1 point at the geometric center of the cell volume.
   * Effective contribution: $8 \times \frac{1}{8} + 1 = 2\text{ net points}$.
3. **Face-Centered ($F$ - *Flächenzentrierte*):**
   * Lattice points at the 8 corners plus 1 point at the centroid of each of the 6 faces.
   * Effective contribution: $8 \times \frac{1}{8} + 6 \times \frac{1}{2} = 4\text{ net points}$.
4. **Base-Centered ($C$ - Base-Centered):**
   * Lattice points at the 8 corners plus 1 point at the center of two opposite, parallel faces (usually the $(001)$ plane).
   * Effective contribution: $8 \times \frac{1}{8} + 2 \times \frac{1}{2} = 2\text{ net points}$.

---

## 🗺️ 4. Rigorous Distribution of the 14 Bravais Lattices

Not all $7 \times 4 = 28$ combinations are independent; many reduce by change-of-basis operations to primitive cells of higher symmetry. The **14 unique lattices** are [Slides 11-13]:

```
7 Crystal Systems
 ├── 1. Cubic (3 lattices):          P (Simple), I (BCC), F (FCC)
 ├── 2. Tetragonal (2 lattices):     P (Simple), I (Body-centered)
 ├── 3. Orthorhombic (4 lattices):   P (Simple), C (Base-centered), I (Body-centered), F (Face-centered)
 ├── 4. Rhombohedral (1 lattice):    P (Simple)
 ├── 5. Hexagonal (1 lattice):       P (Simple)
 ├── 6. Monoclinic (2 lattices):     P (Simple), C (Base-centered)
 └── 7. Triclinic (1 lattice):       P (Simple)
 Total = 3 + 2 + 4 + 1 + 1 + 2 + 1 = 14 Bravais Lattices
```

### Why does the orthorhombic system have all 4 variants ($P, C, I, F$)?
Because its three edges are mutually unequal ($a \neq b \neq c$), adding points on the faces or in the body never introduces an additional symmetry that would allow the cell to collapse into a smaller tetragonal or cubic one. Hence, the orthorhombic is the **only crystal system that exhibits all 4 Bravais lattice modes** [Slide 12].

---

## 🚀 Aerospace Relevance

* **Titanium Alloys ($\text{Ti}$):** It undergoes a polymorphic transition between the $\alpha$ phase (Hexagonal close-packed) and the high-temperature $\beta$ phase (Body-centered cubic), key for the forging of compressor disks and blades.
* **Refractories and Zirconia ($\text{ZrO}_2$):** Its structure goes from monoclinic at room temperature to tetragonal and cubic at high temperature; stabilizing the tetragonal phase with yttria ($\text{Y}_2\text{O}_3$, YSZ) makes it possible to manufacture thermal barrier coatings (TBC) in aeronautical turbines.

---
*Bidirectional Links:*
* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]]
* [[Concept - FCC, BCC and HCP Metallic Structures and Packing Factor|Next: FCC, BCC, HCP Metallic Structures and APF ➡️]]
