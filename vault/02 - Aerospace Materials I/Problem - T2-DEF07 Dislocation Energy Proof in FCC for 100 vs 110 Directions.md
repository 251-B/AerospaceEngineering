---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 7"
dificultad: medium
tags:
  - official-problem
  - solved
  - dislocation-energy
  - frank-rule
  - burgers-vector
  - fcc
  - slip-systems
---

# ✏️ Problem: T2-DEF07 — Proof of Dislocation Energy in FCC: [100] vs [110] Directions

## 📄 Official Statement
> **7. For a metal with FCC structure, $E_1$ and $E_2$ are the energies necessary to generate dislocations in the directions $[100]$ and $[110]$, respectively. Demonstrate that $E_1 / E_2 = 2$.**  
> *(Solution: theory)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Lattice Model:
* Structure: Face-Centred Cubic (FCC), with lattice parameter $a$.
* Relation to the atomic radius: $a\sqrt{2} = 4R \implies a = 2\sqrt{2}R$.

### Definition of Energies:
* $E_1$: Elastic energy per unit length to generate a dislocation with Burgers vector along the $[100]$ direction.
* $E_2$: Elastic energy per unit length to generate a dislocation with Burgers vector along the $[110]$ direction.

| Quantity | Symbol | SI unit |
| :--- | :---: | :--- |
| Lattice parameter | $a$ | m |
| Atomic radius | $R$ | m |
| Burgers vector magnitude | $b = \lvert\vec{b}\rvert$ | m |
| Dislocation energy per unit length | $E$ | J/m |
| Proportionality constant ($E = k\,b^2$) | $k$ | $\text{J/m}^3 = \text{Pa}$ (of the order of the shear modulus) |

Hypotheses: both dislocations are in the same FCC crystal, so $k$ (which depends only on the elastic constants of the material and on the dislocation character, taken to be the same) is the same for both and cancels in the ratio; atoms are hard spheres touching along the face diagonal $\langle 110 \rangle$ [Session 4 Slide 36].

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the mechanics of dislocations [Session 4 Slides 29, 36]:
1. **Elastic energy of a dislocation** (the course states it as "E used to move a dislocation $\propto |b|^2$" [Session 4 Slide 36]; in the literature this is the basis of Frank's criterion, an extension name not used on the slides):
   The elastic strain energy stored in the elastic distortion field surrounding a dislocation is directly proportional to the **square of the magnitude of its Burgers vector**:
   $$E \propto |\vec{b}|^2$$
2. **Determination of the Minimum Translation Vectors:**
   For a dislocation to be kinematically stable in the crystal lattice, its Burgers vector must connect two equivalent lattice atomic positions:
   * In the $[100]$ direction, the minimum translation joining two FCC lattice nodes (two adjacent vertices) is the full edge:
     $$\vec{b}_1 = a[1\, 0\, 0]$$
   * In the $[110]$ direction, owing to the presence of the face-centred atom, the shortest lattice translation goes from a vertex to the face centre:
     $$\vec{b}_2 = \frac{a}{2}[1\, 1\, 0]$$

---

## 🔢 3. Phase 3: Step-by-Step Analytical Proof

### 1. Geometry of the FCC cell
In FCC the atoms touch along the face diagonal, which holds $4R$ (a corner atom contributes $R$, the face-centre atom $2R$, the opposite corner atom $R$). By Pythagoras on a face of side $a$:
$$a^2 + a^2 = (4R)^2 \;\Longrightarrow\; 2a^2 = 16R^2 \;\Longrightarrow\; a^2 = 8R^2 \;\Longrightarrow\; a = 2\sqrt{2}\,R$$

### 2. Burgers vector along $[100]$
The shortest lattice translation along $[100]$ joins two neighbouring corners, $\vec{b}_1 = a[1\,0\,0] = (a, 0, 0)$ (the point $(\tfrac12, 0, 0)$ is an octahedral interstice, not a lattice site). Its squared magnitude:
$$|\vec{b}_1|^2 = a^2 + 0^2 + 0^2 = a^2 = (2\sqrt{2}R)^2 = 4 \cdot 2 \cdot R^2 = 8R^2 \;\Longrightarrow\; b_1 = 2\sqrt{2}\,R$$
This is the value on the slide, obtained there as $b^2 + b^2 = (4R)^2 \Rightarrow b = 2\sqrt{2}\,R$ [Session 4 Slide 36].

### 3. Burgers vector along $[110]$
Along $[110]$ the face-centre atom sits halfway along the diagonal, so the shortest translation is $\vec{b}_2 = \tfrac{a}{2}[1\,1\,0] = (\tfrac{a}{2}, \tfrac{a}{2}, 0)$:
$$|\vec{b}_2|^2 = \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + 0^2 = \frac{a^2}{4} + \frac{a^2}{4} = \frac{2a^2}{4} = \frac{a^2}{2} = \frac{8R^2}{2} = 4R^2 \;\Longrightarrow\; b_2 = 2R$$
This is one atomic diameter, the value on the slide ($b = 2R$) [Session 4 Slide 36].

### 4. Energies and their ratio
With $E = k\,b^2$ and the same $k$ for both dislocations:
$$E_1 = k\,|\vec{b}_1|^2 = k\,a^2 = 8kR^2, \qquad E_2 = k\,|\vec{b}_2|^2 = k\,\frac{a^2}{2} = 4kR^2$$
$$\frac{E_1}{E_2} = \frac{k\,a^2}{k\,a^2/2} = a^2 \cdot \frac{2}{a^2} = 2 \qquad\text{and, in terms of } R:\qquad \frac{E_1}{E_2} = \frac{8kR^2}{4kR^2} = 2$$
$$\boxed{\dfrac{E_1}{E_2} = 2} \quad \blacksquare$$
The two routes (through $a$ and through $R$) agree, and the result is the one requested by the statement.

---

## 🎯 4. Phase 4: Units and Limits, with Metallurgical Consequences

1. **Dimensional check:** $[k\,b^2] = \text{Pa}\cdot\text{m}^2 = \frac{\text{N}}{\text{m}^2}\cdot\text{m}^2 = \text{N} = \frac{\text{J}}{\text{m}}$, an energy per unit length of dislocation line, as expected. The ratio $E_1/E_2 = \frac{\text{J/m}}{\text{J/m}}$ is dimensionless, and so is $b_1/b_2 = \frac{2\sqrt{2}R}{2R} = \sqrt{2}$; squaring it gives back $(\sqrt{2})^2 = 2$.
2. **Independence of the material:** $a$ (or $R$) and $k$ cancel, so the ratio $2$ holds for every FCC metal (Al, Cu, Ni, ...), whatever its lattice parameter or shear modulus.
3. **Physical meaning:** the $[110]$ dislocation stores half the energy of the $[100]$ one because its Burgers vector is the shortest lattice translation, along the close-packed direction. This is why slip in FCC takes place along $\langle 110 \rangle$: dislocation movement is parallel to the direction of maximum packing [Session 4 Slide 36].
4. **Extension (not in the course material):** a $[100]$ dislocation can be written as the sum of two close-packed ones, $a[1\,0\,0] = \tfrac{a}{2}[1\,1\,0] + \tfrac{a}{2}[1\,\bar{1}\,0]$ (check: $\tfrac{a}{2}(1+1,\ 1-1,\ 0+0) = (a, 0, 0)$). The energies are $|a[100]|^2 = a^2$ before and $\tfrac{a^2}{2} + \tfrac{a^2}{2} = a^2$ after, so with $E \propto b^2$ alone this split is energy-neutral: the argument of the problem is the comparison of the two shortest translations, not a decomposition.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
