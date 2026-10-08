---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 8"
dificultad: medium
tags:
  - official-problem
  - solved
  - edge-dislocation
  - fcc
  - burgers-vector
  - copper
---

# ✏️ Problem: T2-DEF08 — Determination of the Burgers Vector of an Edge Dislocation in FCC

## 📄 Official Statement
> **8. A metallic crystal with FCC structure and lattice parameter $3.6 \times 10^{-10}\text{ m}$ contains an edge dislocation in the plane $(110)$. Determine the magnitude and the direction of the Burgers vector.**  
> *(Solution: $b = 2.553 \times 10^{-10}\text{ m}$, $[110]$ or $[1\bar{1}0]$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Structure: Face-Centred Cubic (FCC) (typical of Copper, $a \approx 3.61\text{ \AA}$).
* Lattice parameter: $a = 3.6 \times 10^{-10}\text{ m} = 3.6\text{ \AA}$.
* Slip plane where the dislocation resides: $(110)$.
* Type of linear imperfection: **Edge Dislocation (Taylor)**.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Kinematic Condition of the Edge Dislocation [Session 4 Slide 29, 34]:**
   In an edge dislocation:
   * The Burgers vector $\vec{b}$ must be **contained in the slip plane** of the defect:
     $$\vec{b} \cdot \vec{n}_{\text{plano}} = 0$$
   * $\vec{b}$ is **perpendicular to the dislocation line**: $\vec{b} \perp \vec{t}$.
   * $\vec{b}$ is **parallel to the direction of the slip motion**: $\vec{b} \parallel \vec{v}_{\text{slip}}$.
2. **Slip Direction in FCC:**
   The crystallographic directions of minimum Burgers vector in FCC are those of the $\langle 110 \rangle$ family.
   For a direction $[u\, v\, w] \in \langle 110 \rangle$ to lie within the $(110)$ plane, it must satisfy the orthogonality condition with the plane normal $\vec{n} = (1, 1, 0)$:
   $$1 \cdot u + 1 \cdot v + 0 \cdot w = 0 \implies u + v = 0 \implies v = -u$$
   The only non-trivial dense direction that satisfies this is $[1\, \bar{1}\, 0]$ (or $[\bar{1}\, 1\, 0]$, equivalent by sign inversion to the $\langle 110 \rangle$ family, denoted simply as $[110]$ in the official solution).
3. **Magnitude of the Burgers Vector in FCC [Session 4 Slide 35]:**
   $$|\vec{b}| = \frac{a}{\sqrt{2}} = \frac{a\sqrt{2}}{2}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Determination of the Direction of $\vec{b}$:
* The slip plane is $(110)$, whose normal vector is:
  $$\vec{n} = [1, 1, 0]$$
* We look for a direction of the maximum-packing family $\langle 110 \rangle$ contained in the plane. We evaluate:
  * If $\vec{b} \parallel [1, -1, 0]$:
    $$\vec{n} \cdot \vec{b} = (1)(1) + (1)(-1) + (0)(0) = 1 - 1 = 0 \quad \checkmark$$
* Therefore, the crystallographic direction of the Burgers vector is:
  $$\mathbf{[1\bar{1}0]} \quad (\text{perteneciente a la familia } \mathbf{\langle 110 \rangle})$$

---

### 2. Magnitude of $\vec{b}$:
* The minimum lattice translation vector in this direction is:
  $$\vec{b} = \frac{a}{2}[1\, \bar{1}\, 0]$$
* Magnitude:
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(-\frac{a}{2}\right)^2 + 0^2} = \sqrt{\frac{a^2}{4} + \frac{a^2}{4}} = \frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$$
* Substituting $a = 3.6 \times 10^{-10}\text{ m}$:
  $$|\vec{b}| = \frac{3.6 \times 10^{-10}\text{ m}}{\sqrt{2}} = \frac{3.6 \times 10^{-10}\text{ m}}{1.4142136}$$
  $$|\vec{b}| = \mathbf{2.5456 \times 10^{-10}\text{ m}}$$

> [!warning] Discrepancy with the official solution
> The official key gives $B = 2.553\times10^{-10}\text{ m}$, which corresponds to $a = 3.61\times10^{-10}\text{ m}$ (the lattice parameter of copper). The statement gives $a = 3.6\times10^{-10}\text{ m}$, for which $|\vec{b}| = a/\sqrt{2} = 2.5456\times10^{-10}\text{ m}$ ($0.3\%$ lower). The given value is used; $a$ was not changed to match the key.

---

## 🎯 4. Phase 4: Units and Limits

* **Geometry of Plastic Deformation:** The edge dislocation in this copper crystal represents an extra half-plane that terminates along a line normal to the $(110)$ plane. When the crystal is subjected to shear stresses on the $(110)$ plane, the dislocation advances parallel to its Burgers vector $[\bar{1}10]$, producing a discrete atomic translation of $2.546\text{ \AA}$ with the given data (equal to the hard-sphere atomic diameter, $b = a/\sqrt{2} = 2R$ in FCC).

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
