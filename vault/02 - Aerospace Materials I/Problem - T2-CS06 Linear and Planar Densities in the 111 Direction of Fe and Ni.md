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
  $$\rho_{[111]} = \frac{N_{\text{atoms centred on the diagonal}}}{a\sqrt{3}}$$
* **Planar Density:**
  $$\rho_{(111)} = \frac{N_{\text{atoms contained in the triangle}}}{A_{\text{triangle}}}$$
  where the triangle on the cell has edge $L = a\sqrt{2}$ and area:
  $$A_{\text{triangle}} = \frac{\sqrt{3}}{4} L^2 = \frac{\sqrt{3}}{4}(2a^2) = \frac{\sqrt{3}}{2}a^2$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### Part a: BCC Iron ($\alpha\text{-Fe}$)

1. **Linear Density on $[111]$:**
   * In BCC, atoms are in contact along the main diagonal $[111]$.
   * The diagonal passes through the two opposite vertices and goes through the central body atom.
   * Atoms cut: $2 \times \frac{1}{2} (\text{vertices}) + 1 (\text{centre}) = 2\text{ atoms}$.
   * Segment length: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \frac{2}{a\sqrt{3}} = \mathbf{\frac{2}{\sqrt{3}a}}$$

2. **Planar Density on $(111)$:**
   * The $(111)$ plane contains only the 3 vertices $(a,0,0), (0,a,0), (0,0,a)$. Each vertex contributes an angle of $60^\circ$ inside the equilateral triangle ($\frac{60^\circ}{360^\circ} = \frac{1}{6}$):
     $$N_{\text{atoms}} = 3 \times \frac{1}{6} = \frac{1}{2}\text{ atom}$$
   * The central atom $(a/2, a/2, a/2)$ is **not contained in the $(111)$ plane**, but lies at a perpendicular distance $d = \frac{a}{2\sqrt{3}}$ behind it.
   * Area of the triangle: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{1/2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{1}{a^2\sqrt{3}}}$$

---

### Part b: FCC Nickel ($\text{Ni}$)

1. **Linear Density on $[111]$:**
   * In FCC, atoms do not touch along $[111]$; the cube diagonal is empty at its centre.
   * The diagonal cuts only the two atoms at the opposite vertices through their centres:
     $$N_{\text{atoms}} = 2 \times \frac{1}{2} = 1\text{ atom}$$
   * Length: $L = a\sqrt{3}$.
   $$\rho_{[111]} = \mathbf{\frac{1}{a\sqrt{3}}}$$

2. **Planar Density on $(111)$:**
   * In FCC, the $(111)$ plane is the plane of maximum packing (close-packed plane).
   * It contains the 3 vertices of the triangle (each contributes $\frac{1}{6}$) plus the 3 face centres located at the midpoints of the triangle sides (each contributes $\frac{1}{2}$ since it belongs to two adjacent cells):
     $$N_{\text{atoms}} = 3 \times \left(\frac{1}{6}\right) + 3 \times \left(\frac{1}{2}\right) = \frac{1}{2} + \frac{3}{2} = 2\text{ atoms}$$
   * Area of the triangle: $A = \frac{\sqrt{3}}{2}a^2$.
   $$\rho_{(111)} = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \mathbf{\frac{4}{a^2\sqrt{3}}}$$

---

## 🎯 4. Phase 4: Interpretation and Verification

### 1. Summary and mechanical consequences
| Quantity | BCC iron ($\alpha\text{-Fe}$) | FCC nickel ($\text{Ni}$) | Physical conclusion |
| :--- | :--- | :--- | :--- |
| **Linear density $\rho_{[111]}$** | $\frac{2}{a\sqrt{3}} \approx \frac{1.155}{a}$ (atoms in contact) | $\frac{1}{a\sqrt{3}} \approx \frac{0.577}{a}$ | $\langle 111 \rangle$ is the slip direction of BCC |
| **Planar density $\rho_{(111)}$** | $\frac{1}{a^2\sqrt{3}} \approx \frac{0.577}{a^2}$ | $\frac{4}{a^2\sqrt{3}} \approx \frac{2.309}{a^2}$ (close-packed) | $\{111\}$ is the slip plane of FCC |

* The coefficients are compared for the same symbol $a$; iron and nickel have different lattice parameters, which the statement does not give, so the absolute densities of the two metals cannot be ranked from these formulas alone.
* In **BCC iron** the atoms touch along the cube diagonal ($4R = a\sqrt{3}$ [Session 4 Slide 5]), so $[111]$ is the close-packed direction, but its $(111)$ plane is sparse. The densest BCC plane is $(110)$, with $\rho_{(110)} = \sqrt{2}/a^2 \approx 1.414/a^2$ (Problem 4), and BCC slips on $\{110\}\langle 111 \rangle$ [Session 4 Slide 37].
* In **FCC nickel** the $(111)$ plane is the close-packed plane, four times denser (for equal $a$) than the BCC $(111)$ plane, while the FCC close-packed direction is $\langle 110 \rangle$, not $\langle 111 \rangle$: FCC slips on $\{111\}\langle 110 \rangle$ [Session 4 Slide 37].

### 2. Checks
* **Contact in BCC:** the close-packed linear density must be one atom per diameter, $\frac{1}{2R}$. With $2R = \frac{a\sqrt{3}}{2}$: $\frac{1}{2R} = \frac{2}{a\sqrt{3}}$ ✓, equal to $\rho_{[111]}^{\text{BCC}}$.
* **Lattice repeat in FCC:** the point $(t, t, t)$ on the diagonal is an FCC site only for integer $t$ (corners); face centres have one coordinate different from the other two. The repeat distance is therefore the whole diagonal $a\sqrt{3}$, so $\rho_{[111]}^{\text{FCC}} = 1/(a\sqrt{3})$ ✓.
* **Volume-density cross-check (extension):** $\rho_{(111)} = \rho_v \cdot d$, with $d$ the spacing of consecutive atomic $(111)$ layers. FCC: $\rho_v = 4/a^3$, layers $x + y + z = 0, 1, 2, 3$, $d = a/\sqrt{3}$, so $\rho_v d = \frac{4}{a^3}\cdot\frac{a}{\sqrt{3}} = \frac{4}{a^2\sqrt{3}}$ ✓. BCC: $\rho_v = 2/a^3$, layers $x+y+z = 0, 1, \tfrac32, 2, 3$, $d = \frac{a}{2\sqrt{3}}$, so $\rho_v d = \frac{2}{a^3}\cdot\frac{a}{2\sqrt{3}} = \frac{1}{a^2\sqrt{3}}$ ✓.
* **Dimensions:** $[\rho_{[111]}] = \text{atoms}/\text{m}$ and $[\rho_{(111)}] = \text{atoms}/\text{m}^2$ for $a$ in m ✓.

### 3. Comparison with the official answer
All four results agree with the official solution: BCC $\rho_{[111]} = 2/(\sqrt{3}\,a)$, $\rho_{(111)} = 1/(a^2\sqrt{3})$; FCC $\rho_{[111]} = 1/(a\sqrt{3})$, $\rho_{(111)} = 4/(a^2\sqrt{3})$.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
