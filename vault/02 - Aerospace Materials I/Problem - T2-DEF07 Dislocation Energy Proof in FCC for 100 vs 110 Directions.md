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

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing Frank's theory and the mechanics of dislocations [Session 4 Slide 29, 35]:
1. **Frank's Rule for the Elastic Energy of a Dislocation:**
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

### 1. Computation of $|\vec{b}_1|^2$ for the $[100]$ Direction:
* Vector: $\vec{b}_1 = (a, 0, 0)$.
* Squared magnitude:
  $$|\vec{b}_1|^2 = a^2 + 0^2 + 0^2 = a^2$$
* Expressed in terms of the atomic radius ($a = 2\sqrt{2}R$):
  $$|\vec{b}_1|^2 = (2\sqrt{2}R)^2 = 8R^2$$
* Therefore, the associated elastic energy is:
  $$E_1 = k \cdot |\vec{b}_1|^2 = k \cdot a^2 = k \cdot (8R^2)$$
  where $k$ is an elastic constant depending on the shear modulus $G$ and Poisson's ratio $\nu$.

---

### 2. Computation of $|\vec{b}_2|^2$ for the $[110]$ Direction:
* Vector: $\vec{b}_2 = \left(\frac{a}{2}, \frac{a}{2}, 0\right)$.
* Squared magnitude:
  $$|\vec{b}_2|^2 = \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + 0^2 = \frac{a^2}{4} + \frac{a^2}{4} = \frac{2a^2}{4} = \frac{a^2}{2}$$
* Expressed in terms of the atomic radius ($a = 2\sqrt{2}R$):
  $$|\vec{b}_2|^2 = \frac{8R^2}{2} = 4R^2$$
* Therefore, the associated elastic energy is:
  $$E_2 = k \cdot |\vec{b}_2|^2 = k \cdot \frac{a^2}{2} = k \cdot (4R^2)$$

---

### 3. Energy Ratio ($E_1 / E_2$):
Taking the quotient of both elastic energies:
$$\frac{E_1}{E_2} = \frac{k \cdot |\vec{b}_1|^2}{k \cdot |\vec{b}_2|^2} = \frac{a^2}{a^2 / 2} = \frac{8R^2}{4R^2} = \mathbf{2}$$

$$\mathbf{\frac{E_1}{E_2} = 2} \quad \blacksquare \text{ Q.E.D.}$$

---

## 🎯 4. Phase 4: Units and Limits, with Metallurgical Consequences

* **Spontaneous Decomposition Criterion:** Suppose a dislocation with $\vec{b}_1 = a[100]$ were artificially created. Since:
  $$a[100] = \frac{a}{2}[110] + \frac{a}{2}[1\bar{1}0]$$
  The energy of the two dissociation products would be:
  $$E_{\text{productos}} \propto \left|\frac{a}{2}[110]\right|^2 + \left|\frac{a}{2}[1\bar{1}0]\right|^2 = \frac{a^2}{2} + \frac{a^2}{2} = a^2$$
  Since the vector $\vec{b}_2 = \frac{a}{2}\langle 110 \rangle$ is individually half as energetic ($E_2 = E_1 / 2$), the energy required to move or thermally activate slip along $[110]$ is half that along $[100]$.
* This constitutes the definitive analytical proof of slide 35 [Session 4 Slide 35] of why plastic slip in FCC metals is restricted exclusively to the $\langle 110 \rangle$ directions.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
