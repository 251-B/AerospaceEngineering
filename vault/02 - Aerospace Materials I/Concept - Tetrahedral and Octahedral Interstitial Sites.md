---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 3 T2 Structure of Materials I_2025.pdf, Slides 29-35; Session 4 T2 Structure of Materials II_2025.pdf, Slide 9-10"
tags:
  - theory
  - fundamental-concept
  - interstitials
  - tetrahedral-sites
  - octahedral-sites
  - solid-solutions
dificultad: medium
prerrequisitos:
  - "[[Concept - FCC, BCC and HCP Metallic Structures and Packing Factor]]"
---

# 🔘 Concept: Tetrahedral and Octahedral Interstitial Sites

> **Fundamental Principle:** In any metallic crystal lattice, the rigid atoms leave three-dimensional empty spaces called **interstitial sites or voids** [Slide 29]. These voids are the physical positions that can host solute atoms of small atomic radius ($\text{H}, \text{C}, \text{N}, \text{B}$) in interstitial solid solutions (e.g., carbon in steels or titanium) and they determine the solubility of impurities, the local elastic strain and atomic diffusion.

---

## 📐 1. Types of Interstitial Sites

Depending on the number of host-lattice atoms that surround and touch the void, the following are distinguished [Slide 29]:

1. **Tetrahedral Site:**
   * **Coordination:** Surrounded by **4 atoms** located at the vertices of a regular tetrahedron.
   * **Multiplicity rule in close-packed structures (FCC, HCP):**
     $$N_{\text{tetrahedral}} = 2n$$
     where $n$ is the number of net atoms of the unit cell.

2. **Octahedral Site:**
   * **Coordination:** Surrounded by **6 atoms** located at the vertices of a regular (or distorted) octahedron.
   * **Multiplicity rule in close-packed structures (FCC, HCP):**
     $$N_{\text{octahedral}} = n$$

### 1.1 Why $2n$ Tetrahedral and $n$ Octahedral Sites in Close-Packed Structures (added)
Take one close-packed layer A of $N$ spheres. Its triangular depressions number $2N$ (each sphere is bordered by 6 depressions, each shared by 3 spheres: $6N/3 = 2N$), and they are of two types, $N$ of type B and $N$ of type C. Place the next layer on the $N$ B-type depressions.
* Each sphere of the new layer rests on 3 spheres of layer A and touches all of them: 4 mutually touching spheres enclose a **tetrahedral** void. That gives $N$ tetrahedral voids per interlayer gap. The same argument applies at the other side of every layer, so each sphere is the apex of $2$ tetrahedra, $2N$ in total.
* The $N$ C-type depressions of layer A stay uncovered; directly above each one the new layer presents a triangle of 3 spheres rotated by $180^\circ$. Two opposed triangles of 3 spheres enclose an **octahedral** void: $N$ octahedral voids per interlayer gap, that is $N$ per $N$ spheres.

Hence $N_{\text{tet}} = 2n$ and $N_{\text{oct}} = n$ for FCC and HCP. BCC is not close-packed, so the rule does not apply there (Section 3).

---

## 🟦 2. Interstitial Sites in the FCC Structure ($n=4$)

In the FCC lattice there are $2 \times 4 = 8$ tetrahedral sites and $1 \times 4 = 4$ octahedral sites [Slide 30]:

### Octahedral Sites in FCC ($N_{\text{oct}} = 4$):
* **Spatial locations:**
  * 1 at the **geometric center** of the unit cell: $\left(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right) \implies 1 \times 1 = 1$.
  * 12 at the **center of the 12 edges**: each edge is shared by 4 adjacent cells $\implies 12 \times \frac{1}{4} = 3$.
  * **Total:** $1 + 3 = 4\text{ octahedral sites/cell}$.
* **Radius of the octahedral site ($r_{\text{oct}}$) [Session 4 Slide 9]:**
  Along the cube edge, two lattice atoms of radius $r$ and one interstitial atom of radius $r_{\text{oct}}$ fill the edge $a$:
  $$2r + 2r_{\text{oct}} = a \implies r_{\text{oct}} = \frac{a - 2r}{2}$$
  Knowing that in FCC $a = 2\sqrt{2} r$:
  $$r_{\text{oct}} = \frac{2\sqrt{2}r - 2r}{2} = (\sqrt{2} - 1)r \approx \mathbf{0.414\, r}$$

### Tetrahedral Sites in FCC ($N_{\text{tet}} = 8$):
* **Spatial locations:**
  * They are located within each of the 8 subcubes of edge $a/2$. Each site is at the center of a subcube (coordinates $\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)$, etc.) at a distance $\frac{a\sqrt{3}}{4}$ from the **4 atoms** that surround it: one corner atom and the 3 face-centre atoms adjacent to that corner (for the site $\left(\frac14,\frac14,\frac14\right)$: the atoms at $(0,0,0)$, $\left(\frac12,\frac12,0\right)$, $\left(\frac12,0,\frac12\right)$ and $\left(0,\frac12,\frac12\right)$). The other 4 corners of the subcube are octahedral sites or empty positions, not atoms, so the earlier wording \"each of the 8 main vertices\" was wrong (erratum). The slide value $r_t = [\sqrt{3/2}-1]\,r$ (Session 4 Slide 10) follows only from 4 contacts at distance $a\sqrt3/4$.
  * Being entirely inside the cell: $8 \times 1 = 8\text{ tetrahedral sites/cell}$.
* **Radius of the tetrahedral site ($r_{\text{tet}}$) [Session 4 Slide 9]:**
  The distance from the subcube vertex to its center is $\frac{\sqrt{3}}{2}\left(\frac{a}{2}\right) = \frac{a\sqrt{3}}{4}$. Along that half-diagonal:
  $$r + r_{\text{tet}} = \frac{a\sqrt{3}}{4} = \frac{(2\sqrt{2}r)\sqrt{3}}{4} = \frac{\sqrt{6}}{2}r = \sqrt{\frac{3}{2}}r$$
  $$r_{\text{tet}} = \left(\sqrt{\frac{3}{2}} - 1\right)r \approx \mathbf{0.225\, r}$$

---

## 🟥 3. Interstitial Sites in the BCC Structure ($n=2$)

The BCC lattice is **not close-packed** ($\text{APF} = 0.68$). Although it has more free volume ($32\%$), its voids are significantly **smaller and anisotropic** [Slide 32]:

### Octahedral Sites in BCC ($N_{\text{oct}} = 6$):
* **Spatial locations:**
  * Centers of the 6 faces: $6 \times \frac{1}{2} = 3$.
  * Centers of the 12 edges: $12 \times \frac{1}{4} = 3$.
  * **Total:** $3 + 3 = 6\text{ octahedral sites/cell}$.
* **Radius of the octahedral site ($r_{\text{oct}}$) [Session 4 Slide 9]:**
  The octahedral site in BCC is flattened (irregular octahedron): it is very tightly squeezed between the two atoms along the $[100]$ direction at distance $a$:
  $$2r + 2r_{\text{oct}} = a = \frac{4r}{\sqrt{3}} \implies r_{\text{oct}} = \left(\frac{2}{\sqrt{3}} - 1\right)r \approx \mathbf{0.155\, r}$$

### Tetrahedral Sites in BCC ($N_{\text{tet}} = 12$):
* **Spatial locations:**
  * Located on the 6 faces of the cube, at positions of the type $\left(\frac{1}{2}, \frac{1}{4}, 0\right)$. Each of the 6 faces contains 4 equivalent positions shared by 2 cells:
    $$6_{\text{faces}} \times 4 \times \frac{1}{2} = 12\text{ tetrahedral sites/cell}$$
* **Radius of the tetrahedral site ($r_{\text{tet}}$) [Session 4 Slide 9]:**
  $$r_{\text{tet}} = \left(\sqrt{\frac{5}{3}} - 1\right)r \approx \mathbf{0.291\, r}$$

### 3.1 Derivation of the BCC Void Radii (added)
Put the lattice atoms at the corners $(0,0,0)$ and the body centre $\left(\frac12,\frac12,\frac12\right)$, with contact along the body diagonal, $a = 4r/\sqrt3$.
* **Tetrahedral site** at $\left(\frac12,\frac14,0\right)$ on a cube face. Its 4 nearest atoms are the corners $(0,0,0)$ and $(1,0,0)$ and the body centres $\left(\frac12,\frac12,\pm\frac12\right)$, all at the same distance $a\sqrt{\frac{1}{16}+\frac14} = \frac{\sqrt5}{4}a$ (for the corner $(0,0,0)$: $\sqrt{(\frac12)^2+(\frac14)^2+0^2}$; for the body centre $\left(\frac12,\frac12,\frac12\right)$: $\sqrt{0+(\frac14)^2+(\frac12)^2}$). Then
  $$r + r_{\text{tet}} = \frac{\sqrt5}{4}\cdot\frac{4r}{\sqrt3} = \sqrt{\frac53}\,r \;\Rightarrow\; r_{\text{tet}} = \left(\sqrt{\tfrac53}-1\right)r = 0.291\,r$$
* **Octahedral site** at $\left(\frac12,\frac12,0\right)$ (face centre). Its 2 nearest atoms are the body centres of the two cells sharing that face, at distance $a/2$ each:
  $$r + r_{\text{oct}} = \frac a2 = \frac{2r}{\sqrt3} \;\Rightarrow\; r_{\text{oct}} = \left(\frac{2}{\sqrt3}-1\right)r = 0.155\,r$$
  (This equals the form $2r + 2r_{\text{oct}} = a$ used in Section 3, because the two body-centre atoms and the void lie on a line of length $a$.)

> [!IMPORTANT]
> **The Void Paradox in BCC vs FCC:**
> Although the BCC structure has lower volumetric packing ($\text{APF} = 0.68$ vs $0.74$), the BCC octahedral site ($0.155\, r$) is **much smaller** than the FCC one ($0.414\, r$). Moreover, in BCC the tetrahedral site ($0.291\, r$) is larger than the octahedral one ($0.155\, r$). Therefore, when Carbon ($r_C \approx 0.071\text{ nm}$) dissolves in $\alpha\text{-Fe}$ (BCC, $r_{\text{Fe}} \approx 0.124\text{ nm}$), it must force a severe asymmetric tetragonal distortion, limiting its maximum solubility to only **0.022 wt% C at 727 ºC**, whereas in $\gamma\text{-Fe}$ (FCC) it enters the wide octahedral sites with a solubility of up to **2.14 wt% C**.

---

## 🟩 4. Interstitial Sites in the HCP Structure ($n=6$)

* **Octahedral Sites:** $N_{\text{oct}} = n = 6$. Relative radius: $r_{\text{oct}} \approx 0.414\, r$ [Slide 34, Session 4 Slide 9].
* **Tetrahedral Sites:** $N_{\text{tet}} = 2n = 12$. Relative radius: $r_{\text{tet}} \approx 0.225\, r$.

---

## 📊 5. Summary Table of Interstitial Sites

| Structure | $n$ | $V_{\text{voids}}/V_C$ | Octahedral Sites ($N_{\text{oct}}$) | $r_{\text{oct}}/r$ | Tetrahedral Sites ($N_{\text{tet}}$) | $r_{\text{tet}}/r$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FCC** | 4 | $0.26$ | **4** (center and edges) | **0.414** | **8** (interior, at $a\sqrt{3}/4$) | **0.225** |
| **BCC** | 2 | $0.32$ | **6** (faces and edges) | **0.155** | **12** (4 on each face) | **0.291** |
| **HCP** | 6 | $0.26$ | **6** | **0.414** | **12** | **0.225** |

Per atom ($N/n$): FCC $2$ tetrahedral and $1$ octahedral; HCP $2$ tetrahedral and $1$ octahedral; BCC $6$ tetrahedral and $3$ octahedral (BCC has $12$ and $6$ sites per cell with $n = 2$, so the compact-structure rule $N_{\text{tet}} = 2n$, $N_{\text{oct}} = n$ does not apply to BCC).

---
*Bidirectional Links:*
* [[Concept - FCC, BCC and HCP Metallic Structures and Packing Factor|⬅️ Previous: FCC, BCC, HCP Metallic Structures]]
* [[Concept - Miller Notation for Cubic and Hexagonal Directions and Planes|Next: Miller Notation for Directions and Planes ➡️]]
