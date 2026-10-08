---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 13"
dificultad: high
tags:
  - official-problem
  - solved
  - orthorhombic
  - face-centered-orthorhombic
  - packing-factor
  - bragg-spacing
  - crystal-weight
---

# ✏️ Problem: T2-CS13 — Characterisation of an Orthorhombic Metal: (220) Plane and [101] Direction

## 📄 Official Statement
> **13. In the figure, the dimensions of the $(220)$ plane and the $[101]$ direction of a hypothetical metal with a radius of $1.98\text{ \AA}$ and atomic weight of $180.95\text{ g/mol}$ are shown.**  
> * Plane $(220)$: Width $= 3.9\text{ \AA}$, Height $= 7.0\text{ \AA}$.  
> * Direction $[101] = 8.6\text{ \AA}$ (exhibiting 3 atoms in contact along the diagonal, so length $= 4R$).  
> 
> **a)** Draw the unit cell, deduce which crystal system it belongs to, and identify the name of this crystal structure.  
> **b)** Determine the packing factor.  
> **c)** Calculate the density on the $(110)$ and $(100)$ planes in $\text{atoms/cm}^2$.  
> **d)** Calculate the interplanar distances $d_{(111)}$ and $d_{(110)}$ in $\text{\AA}$.  
> **e)** Calculate the weight of a single crystal with a volume of $1\text{ cm}^3$.  
> *(Solution: a) Face centred Orthorhombic; b) $0.62$; c) $\rho_{(110)} = 3.66 \times 10^{14}\text{ atoms/cm}^2$, $\rho_{(100)} = 4.76 \times 10^{14}\text{ atoms/cm}^2$; d) $d_{(111)} = 3.37\text{ \AA}$, $d_{(110)} = 3.84\text{ \AA}$; e) $5.72\text{ g}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Atomic radius: $R = 1.98\text{ \AA} = 1.98 \times 10^{-8}\text{ cm}$.
* Molar atomic weight: $M = 180.95\text{ g/mol}$ (Tantalum, $\text{Ta}$).
* Height of the $(220)$ plane: $c = 7.0\text{ \AA}$.
* Width of the $(220)$ plane: in an orthogonal crystal, the $(220)$ plane cuts at $a/2$ and $b/2$, so its width is half the base diagonal:
  $$\frac{\sqrt{a^2 + b^2}}{2} = 3.9\text{ \AA} \implies \sqrt{a^2 + b^2} = 7.8\text{ \AA}$$
* Length of the $[101]$ direction:
  $$L_{[101]} = \sqrt{a^2 + c^2} = 8.6\text{ \AA} \approx 4R = 4(1.98) = 7.92\text{ \AA}$$
* Avogadro constant: $N_A = 6.022 \times 10^{23}\text{ mol}^{-1}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Deduction of the Lattice Parameters ($a, b, c$):**
   * We know $c = 7.0\text{ \AA}$.
   * From the diagonal $[101]$: $a^2 + c^2 = 8.6^2 \implies a^2 = 8.6^2 - 7.0^2 = 73.96 - 49.00 = 24.96\text{ \AA}^2 \implies a \approx 5.0\text{ \AA}$.
   * From the base diagonal: $a^2 + b^2 = 7.8^2 = 60.84 \implies b^2 = 60.84 - 24.96 = 35.88\text{ \AA}^2 \implies b \approx 6.0\text{ \AA}$.
   * Since $a \neq b \neq c$ ($a \approx 5.0\text{ \AA}, b \approx 6.0\text{ \AA}, c = 7.0\text{ \AA}$) and the angles are $90^\circ$, the system is **Orthorhombic** [Session 3 Slide 12].
   * The atomic contacts along the face diagonals reveal a **Face-Centred ($F$)** lattice with $n = 4$ equivalent atoms.
2. **Atomic Packing Factor (APF):**
   $$\text{APF} = \frac{n \cdot \left(\frac{4}{3}\pi R^3\right)}{a \cdot b \cdot c}$$
3. **Planar Densities:**
   $$\rho_{(110)} = \frac{2}{\sqrt{a^2 + b^2} \cdot c}, \quad \rho_{(100)} = \frac{2}{b \cdot c}$$
4. **Interplanar Spacings in an Orthorhombic Lattice [Session 3 Slide 53]:**
   $$d_{hkl} = \frac{1}{\sqrt{\frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}}}$$
5. **Mass of a Single Crystal of $V = 1\text{ cm}^3$:**
   $$\rho = \frac{n \cdot M}{V_C \cdot N_A}, \quad m = \rho \cdot V$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Parameters and Lattice Type
* $c = 7.0\text{ \AA}$.
* $a = \sqrt{8.6^2 - 7.0^2} = \sqrt{73.96 - 49.00} = \sqrt{24.96} = 4.996\text{ \AA} \approx \mathbf{5.0\text{ \AA}}$.
* $b = \sqrt{7.8^2 - 24.96} = \sqrt{60.84 - 24.96} = \sqrt{35.88} = 5.990\text{ \AA} \approx \mathbf{6.0\text{ \AA}}$.
* Since $a \neq b \neq c$ and the axes are orthogonal, the crystal system is **Orthorhombic**.
* Having atoms at all face centres, it is the **Face-Centred Orthorhombic Lattice (Face-Centered Orthorhombic)** with $n = 4$.

---

### 2. Part b: Packing Factor (APF)
* Unit cell volume:
  $$V_C = a \cdot b \cdot c = 4.996 \times 5.990 \times 7.0 = 209.48\text{ \AA}^3$$
* Volume of the 4 atoms ($R = 1.98\text{ \AA}$):
  $$V_{\text{átomos}} = 4 \times \left(\frac{4}{3}\pi R^3\right) = \frac{16}{3}\pi (1.98)^3 = \frac{16}{3}\pi (7.7624) = 130.06\text{ \AA}^3$$
* Packing factor:
  $$\text{APF} = \frac{130.06}{209.48} = \mathbf{0.6209} \approx \mathbf{0.62}$$

---

### 3. Part c: Planar Densities
* **$(110)$ Plane:**
  * Dimensions: base $\sqrt{a^2 + b^2} = 7.8\text{ \AA} = 7.8 \times 10^{-8}\text{ cm}$; height $c = 7.0\text{ \AA} = 7.0 \times 10^{-8}\text{ cm}$.
  * Area: $A_{(110)} = 7.8 \times 7.0 = 54.6\text{ \AA}^2 = 5.46 \times 10^{-15}\text{ cm}^2$.
  * Atoms contained: $N_{\text{átomos}} = 2$.
  $$\rho_{(110)} = \frac{2\text{ at}}{5.46 \times 10^{-15}\text{ cm}^2} = 3.663 \times 10^{14} \approx \mathbf{3.66 \times 10^{14}\text{ atoms/cm}^2}$$

* **$(100)$ Plane:**
  * Dimensions: base $b = 5.990\text{ \AA} = 5.990 \times 10^{-8}\text{ cm}$; height $c = 7.0\text{ \AA} = 7.0 \times 10^{-8}\text{ cm}$.
  * Area: $A_{(100)} = 5.990 \times 7.0 = 41.93\text{ \AA}^2 = 4.193 \times 10^{-15}\text{ cm}^2$.
  * Atoms contained: $N_{\text{átomos}} = 2$.
  $$\rho_{(100)} = \frac{2\text{ at}}{4.193 \times 10^{-15}\text{ cm}^2} = 4.770 \times 10^{14} \approx \mathbf{4.77 \times 10^{14}\text{ atoms/cm}^2}$$

---

### 4. Part d: Interplanar Distances
* **Spacing $d_{(111)}$:**
  $$\frac{1}{d_{(111)}^2} = \frac{1^2}{a^2} + \frac{1^2}{b^2} + \frac{1^2}{c^2} = \frac{1}{24.96} + \frac{1}{35.88} + \frac{1}{49.00}$$
  $$\frac{1}{d_{(111)}^2} = 0.040064 + 0.027871 + 0.020408 = 0.088343\text{ \AA}^{-2}$$
  $$d_{(111)} = \frac{1}{\sqrt{0.088343}} = \frac{1}{0.297225} = \mathbf{3.364\text{ \AA}} \approx \mathbf{3.36\text{ \AA}}$$

* **Spacing $d_{(110)}$:**
  $$\frac{1}{d_{(110)}^2} = \frac{1^2}{a^2} + \frac{1^2}{b^2} + 0 = \frac{1}{24.96} + \frac{1}{35.88} = 0.040064 + 0.027871 = 0.067935\text{ \AA}^{-2}$$
  $$d_{(110)} = \frac{1}{\sqrt{0.067935}} = \frac{1}{0.26064} = \mathbf{3.837\text{ \AA}} \approx \mathbf{3.84\text{ \AA}}$$

---

### 5. Part e: Mass of the $1\text{ cm}^3$ Single Crystal
* **Cell volume:** $V_C = 209.48\text{ \AA}^3 = 2.0948 \times 10^{-22}\text{ cm}^3$.
* **Theoretical density:**
  $$\rho = \frac{4 \times 180.95\text{ g/mol}}{(2.0948 \times 10^{-22}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})} = \frac{723.8}{126.15} = \mathbf{5.738\text{ g/cm}^3} \approx \mathbf{5.74\text{ g/cm}^3}$$
* For a macroscopic volume $V = 1.0\text{ cm}^3$:
  $$m = \rho \cdot V = 5.74\text{ g/cm}^3 \times 1.0\text{ cm}^3 = \mathbf{5.74\text{ g}}$$

> [!warning] Discrepancy with the official solution
> The official key ($\rho_{(100)} = 4.76\times10^{14}$, $d_{(111)} = 3.37\text{ \AA}$, $m = 5.72\text{ g}$) is reproduced only if the cell is first rounded to $a = 5.0$, $b = 6.0$, $c = 7.0\text{ \AA}$ ($V = 210\text{ \AA}^3$: $\rho = 5.723\text{ g/cm}^3$, $d_{(111)} = 3.367\text{ \AA}$). Without that rounding, the cell obtained from the figure data ($a = 4.996$, $b = 5.990$, $c = 7.0\text{ \AA}$) gives $\rho_{(100)} = 4.77\times10^{14}\text{ atoms/cm}^2$, $d_{(111)} = 3.36\text{ \AA}$ and $m = 5.74\text{ g}$ ($0.3$-$0.4\%$ differences, within the two-significant-figure precision of the figure). The unrounded values are reported.

---

## 🎯 4. Phase 4: Units and Limits

* The results agree with the official solution except for rounding differences (see the discrepancy note): $\text{APF} = 0.62$ reflects the lower packing typical of an anisotropic orthorhombic cell relative to the FCC limit ($0.74$), and the planar densities confirm that the most densely packed plane $(100)$ has a smaller area and a higher atomic concentration than $(110)$.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
