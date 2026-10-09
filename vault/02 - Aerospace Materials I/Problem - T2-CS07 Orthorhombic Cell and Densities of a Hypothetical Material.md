---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 7"
dificultad: high
tags:
  - official-problem
  - solved
  - orthorhombic
  - face-centered-orthorhombic
  - planar-density
  - silver
---

# ✏️ Problem: T2-CS07 — Orthorhombic Cell and Densities of a Hypothetical Material

## 📄 Official Statement
> **7. The figure below shows the crystallographic directions of a hypothetical material with orthogonal structure.**  
> **$[010] = 5\text{ \AA}$, $[110] = 6.4\text{ \AA}$, $[101] = 7.21\text{ \AA}$**  
> *(The figure illustrates that atoms are in contact along $[110]$ and $[101]$, containing 2 atoms in the segment, while $[010]$ contains 1 atom).*  
> **a)** Draw the unit cell. To which crystalline lattice does it belong?  
> **b)** Calculate the atomic weight given that the density is $5.97\text{ g/cm}^3$.  
> **c)** Calculate the planar density in $\text{atoms/mm}^2$ in the planes $(100)$ and $(110)$, and compare them with each other.  
> *(Solution: a) face centered orthorhombic lattice; b) $M = 107.87\text{ g/mol}$; c) $\rho_{(100)} = 6.66 \times 10^{12}\text{ at/mm}^2$; $\rho_{(110)} = 5.2 \times 10^{12}\text{ at/mm}^2$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Orthogonal structure: $\alpha = \beta = \gamma = 90^\circ$.
* Given lengths:
  * $L_{[010]} = b = 5\text{ \AA} = 5.0 \times 10^{-8}\text{ cm}$.
  * $L_{[110]} = \sqrt{a^2 + b^2} = 6.4\text{ \AA}$.
  * $L_{[101]} = \sqrt{a^2 + c^2} = 7.21\text{ \AA}$.
* Volumetric density: $\rho = 5.97\text{ g/cm}^3$.
* Avogadro number: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Determination of the Lattice Parameters ($a, b, c$):**
   Using the orthogonal metric $L_{[uvw]} = \sqrt{(ua)^2 + (vb)^2 + (wc)^2}$, $a$ and $c$ are solved for successively.
2. **Identification of the Bravais Lattice [Session 3 Slides 9, 12]:**
   If the face diagonals $[110]$ and $[101]$ are directions of continuous atomic contact with atoms at their midpoints, the cell has atoms centred on all faces $\implies$ **Face-Centred Orthorhombic Lattice ($F$)** with $n = 4$ equivalent atoms.
3. **Molar Atomic Mass:**
   $$M = \frac{\rho \cdot (a \cdot b \cdot c) \cdot N_A}{n}$$
4. **Planar Densities:**
   $$\rho_{(100)} = \frac{N_{\text{átomos}(100)}}{b \cdot c}, \quad \rho_{(110)} = \frac{N_{\text{átomos}(110)}}{\sqrt{a^2 + b^2} \cdot c}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Deduction of Parameters and Lattice Type
* From $L_{[110]}$ and $b = 5.0\text{ \AA}$:
  $$a^2 + b^2 = 6.4^2 \implies a^2 + 5.0^2 = 40.96 \implies a^2 = 40.96 - 25 = 15.96\text{ \AA}^2$$
  $$a = \sqrt{15.96} \approx 3.995\text{ \AA} \approx \mathbf{4.0\text{ \AA}}$$
* From $L_{[101]}$ and $a^2 = 15.96$:
  $$a^2 + c^2 = 7.21^2 \implies 15.96 + c^2 = 51.984 \implies c^2 = 51.984 - 15.96 = 36.024\text{ \AA}^2$$
  $$c = \sqrt{36.024} \approx \mathbf{6.0\text{ \AA}}$$
* Since $a \neq b \neq c$ ($a \approx 4.0\text{ \AA}$, $b = 5.0\text{ \AA}$, $c = 6.0\text{ \AA}$) and all three angles are $90^\circ$, the system is **Orthorhombic**.
* Since there are atoms at the centres of all the faces through which the close-packed directions pass, it belongs to the **face-centred orthorhombic lattice (Face-Centered Orthorhombic, $F$)** with $n = 4$ atoms/cell.

---

### 2. Part b: Atomic Weight ($M$)
* **Unit cell volume:**
  $$V_C = a \cdot b \cdot c = (3.995 \times 10^{-8}\text{ cm}) \times (5.0 \times 10^{-8}\text{ cm}) \times (6.0 \times 10^{-8}\text{ cm}) = 1.1985 \times 10^{-22}\text{ cm}^3$$
* **Molar atomic mass:**
  $$M = \frac{\rho \cdot V_C \cdot N_A}{n} = \frac{(5.97\text{ g/cm}^3) \times (1.1985 \times 10^{-22}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})}{4}$$
  $$M = \frac{7.155 \times 10^{-22} \times 6.022 \times 10^{23}}{4} = \frac{430.87}{4} = \mathbf{107.72\text{ g/mol}} \approx \mathbf{107.87\text{ g/mol}}$$
  *(It corresponds to Silver, $\text{Ag}$, with $M_{\text{tabulada}} = 107.868\text{ g/mol}$).*

---

### 3. Part c: Planar Densities

1. **$(100)$ Plane:**
   * It is the face bounded by the edges $b$ and $c$.
   * Dimensions: $b = 5.0\text{ \AA} = 5.0 \times 10^{-7}\text{ mm}$; $c = 6.0\text{ \AA} = 6.0 \times 10^{-7}\text{ mm}$.
   * Area: $A_{(100)} = b \cdot c = 30.0\text{ \AA}^2 = 3.0 \times 10^{-13}\text{ mm}^2$.
   * Atoms contained in the centred face: 4 vertices $\times \frac{1}{4} + 1\text{ centro de cara} = 2\text{ átomos}$.
   $$\rho_{(100)} = \frac{2\text{ at}}{3.0 \times 10^{-13}\text{ mm}^2} = \mathbf{6.66 \times 10^{12}\text{ at/mm}^2}$$

2. **$(110)$ Plane:**
   * Diagonal rectangular plane of base $L_{[110]} = 6.4\text{ \AA} = 6.4 \times 10^{-7}\text{ mm}$ and height $c = 6.0\text{ \AA} = 6.0 \times 10^{-7}\text{ mm}$.
   * Area: $A_{(110)} = 6.4 \times 6.0 = 38.4\text{ \AA}^2 = 3.84 \times 10^{-13}\text{ mm}^2$.
   * Atoms contained: 4 vertices $\times \frac{1}{4} + 2\text{ centros en aristas de base} \times \frac{1}{2} = 1 + 1 = 2\text{ átomos}$.
   $$\rho_{(110)} = \frac{2\text{ at}}{3.84 \times 10^{-13}\text{ mm}^2} = \mathbf{5.21 \times 10^{12}\text{ at/mm}^2}$$

3. **Comparison:**
   $$\rho_{(100)} = 6.66 \times 10^{12}\text{ at/mm}^2 > \rho_{(110)} = 5.21 \times 10^{12}\text{ at/mm}^2$$
   The $(100)$ plane has a **$28\%$ higher atomic density** than the $(110)$ plane.

---

## 🎯 4. Phase 4: Units and Limits

* **Anisotropic Geometry:** Unlike the cubic system, where $\{100\}$ has a lower density than $\{110\}$, in this orthorhombic crystal with $a < b < c$ the $(100)$ plane has a small area ($bc = 30\text{ \AA}^2$) containing 2 atoms, making it denser than the larger-area $(110)$ plane ($38.4\text{ \AA}^2$), which demonstrates the strong anisotropy of orthorhombic lattices.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
