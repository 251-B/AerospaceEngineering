---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 6"
dificultad: low
tags:
  - official-problem
  - solved
  - burgers-vector
  - bcc
  - fcc
  - slip-direction
  - dislocations
---

# ✏️ Problem: T2-DEF06 — Magnitude of the Burgers Vector in α-Fe (BCC) and Al (FCC)

## 📄 Official Statement
> **6. Calculate the Burgers vector magnitude for $\alpha\text{-Fe}$ (BCC) and $\text{Al}$ (FCC).**  
> *(Solution: $\alpha\text{-Fe}: \frac{\sqrt{3}a}{2}$; $\text{Al}: \frac{a}{\sqrt{2}}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Lattice Models:
1. **Ferritic Iron ($\alpha\text{-Fe}$):** Body-Centred Cubic (BCC) lattice, lattice parameter $a$.
2. **Pure Aluminium ($\text{Al}$):** Face-Centred Cubic (FCC) lattice, lattice parameter $a$.

### Fundamental Hypothesis:
* In any metallic crystal lattice, stable dislocations are **unit (or perfect) dislocations** whose Burgers vector $\vec{b}$ connects two identical, equivalent lattice positions along the **crystallographic direction of maximum packing** in order to minimise the elastic energy of the dislocation ($E \propto |\vec{b}|^2$) [Session 4 Slide 35].

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the theory of dislocations and slip systems [Session 4 Slides 28, 34-36]:
* **In the BCC lattice:**
  * The direction of maximum atomic packing is the main cube diagonal $\langle 111 \rangle$.
  * The smallest lattice translation connecting two lattice nodes is the one going from a vertex $(0,0,0)$ to the body centre $(1/2, 1/2, 1/2)$:
    $$\vec{b}_{\text{BCC}} = \frac{a}{2}[1\, 1\, 1]$$
* **In the FCC lattice:**
  * The direction of maximum packing is the face diagonal $\langle 110 \rangle$.
  * The smallest lattice translation joining two identical lattice positions goes from a vertex $(0,0,0)$ to the face centre $(1/2, 1/2, 0)$:
    $$\vec{b}_{\text{FCC}} = \frac{a}{2}[1\, 1\, 0]$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Magnitude in $\alpha\text{-Fe}$ (BCC):
* Burgers vector in Cartesian components:
  $$\vec{b} = \left(\frac{a}{2}, \frac{a}{2}, \frac{a}{2}\right)$$
* Magnitude (Euclidean norm):
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2} = \sqrt{3 \left(\frac{a^2}{4}\right)}$$
  $$|\vec{b}|_{\alpha\text{-Fe}} = \mathbf{\frac{a\sqrt{3}}{2}} = \mathbf{\frac{\sqrt{3}a}{2}}$$
  *(Note that since in BCC $a\sqrt{3} = 4R$, the magnitude is exactly $|\vec{b}| = 2R$, which corresponds to the atomic diameter in contact).*

---

### 2. Magnitude in $\text{Al}$ (FCC):
* Burgers vector in Cartesian components:
  $$\vec{b} = \left(\frac{a}{2}, \frac{a}{2}, 0\right)$$
* Magnitude (Euclidean norm):
  $$|\vec{b}| = \sqrt{\left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2 + 0^2} = \sqrt{\frac{a^2}{4} + \frac{a^2}{4}} = \sqrt{\frac{2a^2}{4}} = \frac{a\sqrt{2}}{2}$$
  Rationalising by dividing numerator and denominator by $\sqrt{2}$:
  $$|\vec{b}|_{\text{Al}} = \mathbf{\frac{a}{\sqrt{2}}}$$
  *(Note that in FCC $a\sqrt{2} = 4R$, so $|\vec{b}| = \frac{4R}{2} = 2R$, which also coincides exactly with the atomic diameter in contact).*

---

## 🎯 4. Phase 4: Units and Limits

* **Universality of the Atomic Diameter:** In both metallic crystal structures, the magnitude of the Burgers vector of the elementary perfect dislocation is identical to the atomic diameter:
  $$|\vec{b}| = 2R$$
* This shows mathematically why plastic slip occurs step by step along the dense atomic rows: each time the dislocation line sweeps a plane, it displaces the upper block of the crystal by one elementary atomic distance $|\vec{b}| = 2R$ relative to the lower one.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
