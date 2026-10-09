---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 6"
dificultad: medium
tags:
  - official-problem
  - solved
  - iron-bcc
  - nickel-fcc
  - linear-density
  - planar-density
  - slip-systems
---

# ✏️ Problem: T2-CS06 — Linear and Planar Densities in the [111] Direction and (111) Plane of Fe (BCC) and Ni (FCC)

## 📄 Official Statement
> **6. Calculate the linear density in the $[111]$ direction and the planar density in the $(111)$ plane for:**  
> **a)** Iron BCC *(Solution: $\rho_{[111]} = 2/(\sqrt{3}a)$, $\rho_{(111)} = 1/(a^2\sqrt{3})$)*  
> **b)** Nickel FCC *(Solution: $\rho_{[111]} = 1/(a\sqrt{3})$, $\rho_{(111)} = 4/(a^2\sqrt{3})$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Structural Models:
1. **Ferritic Iron ($\alpha\text{-Fe}$):** Body-Centred Cubic (BCC) lattice, parameter $a_{\text{Fe}}$, $n = 2$ atoms/cell.
2. **Nickel ($\text{Ni}$):** Face-Centred Cubic (FCC) lattice, parameter $a_{\text{Ni}}$, $n = 4$ atoms/cell.

### Comparison Parameters:
* Direction evaluated: $[111]$ (main cube diagonal, length $L_{[111]} = a\sqrt{3}$).
* Plane evaluated: $(111)$ (plane that intersects the axes at $x=a, y=a, z=a$, bounding an equilateral triangle of edges $a\sqrt{2}$).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the lattice packing theory [Session 4 Slides 7-9]:
* **Linear Density:**
  $$\rho_{[111]} = \frac{N_{\text{átomos centrados en la diagonal}}}{a\sqrt{3}}$$
* **Planar Density:**
  $$\rho_{(111)} = \frac{N_{\text{átomos contenidos en el triángulo}}}{A_{\text{triángulo}}}$$
  where the triangle on the cell has edge $L = a\sqrt{2}$ and area:
  $$A_{\text{triángulo}} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### Part a: BCC Iron ($\alpha\text{-Fe}$)

1. **Linear Density on $[111]$:**
   * In BCC, atoms are in contact along the main diagonal $[111]$.
   * The diagonal passes through the two opposite vertices and goes through the central body atom.
   * Atoms cut: $2 \times \frac{1}{2} (\text{vértices}) + 1 (\text{centro}) = 2\text{ átomos}$.
   * Segment length: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \frac{2}{a\sqrt{3}} = \mathbf{\frac{2}{\sqrt{3}a}}$$

2. **Planar Density on $(111)$:**
   * The $(111)$ plane contains only the 3 vertices $(a,0,0), (0,a,0), (0,0,a)$. Each vertex contributes an angle of $60^\circ$ inside the equilateral triangle ($\frac{60^\circ}{360^\circ} = \frac{1}{6}$):
     $$N_{\text{átomos}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ átomo}$$
   * The central atom $(a/2, a/2, a/2)$ is **not contained in the $(111)$ plane**, but lies at a perpendicular distance $d = \frac{a}{2\sqrt{3}}$ behind it.
   * Area of the triangle: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

---

### Part b: FCC Nickel ($\text{Ni}$)

1. **Linear Density on $[111]$:**
   * In FCC, atoms do not touch along $[111]$; the cube diagonal is empty at its centre.
   * The diagonal cuts only the two atoms at the opposite vertices through their centres:
     $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
   * Length: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \mathbf{\frac{1}{a\sqrt{3}}}$$

2. **Planar Density on $(111)$:**
   * In FCC, the $(111)$ plane is the plane of maximum packing (close-packed plane).
   * It contains the 3 vertices of the triangle (each contributes $\frac{1}{6}$) plus the 3 face centres located at the midpoints of the triangle sides (each contributes $\frac{1}{2}$ since it belongs to two adjacent cells):
     $$N_{\text{átomos}} = 3 \times \left(\frac{1}{6}\right) + 3 \times \left(\frac{1}{2}\right) = \frac{1}{2} + \frac{3}{2} = 2\text{ átomos}$$
   * Area of the triangle: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{4}{a^2\sqrt{3}}}$$

---

## 🎯 4. Phase 4: Units and Limits, with Mechanical Consequences

| Crystallographic Parameter | BCC Iron ($\alpha\text{-Fe}$) | FCC Nickel ($\text{Ni}$) | Physical Conclusion |
| :--- | :--- | :--- | :--- |
| **Linear density $\rho_{[111]}$** | $\mathbf{\frac{2}{\sqrt{3}a}}$ (Maximum packing) | $\frac{1}{\sqrt{3}a}$ | $[111]$ is the slip direction in BCC |
| **Planar density $\rho_{(111)}$** | $\frac{1}{\sqrt{3}a^2}$ | $\mathbf{\frac{4}{\sqrt{3}a^2}}$ (Maximum packing) | $(111)$ is the slip plane in FCC |

* In **BCC Iron**, $[111]$ is the densest close-packed direction (the Burgers vector is $\vec{b} = \frac{a}{2}\langle 111 \rangle$), but its $(111)$ plane is very sparse ($\frac{1}{a^2\sqrt{3}}$), which explains why slip in BCC occurs on the $\{110\}$ planes, whose density is $\frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$.
* In **FCC Nickel**, the $(111)$ plane has a planar density four times higher ($\frac{4}{a^2\sqrt{3}} \approx \frac{2.309}{a^2}$), making it the canonical close-packed plane of the nickel-based superalloys used in single-crystal turbine blades.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
