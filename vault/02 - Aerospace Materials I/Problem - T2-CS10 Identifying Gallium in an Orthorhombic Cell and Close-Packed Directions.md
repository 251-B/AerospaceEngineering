---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 10"
dificultad: high
tags:
  - official-problem
  - solved
  - gallium
  - base-centered-orthorhombic
  - close-packed-directions
  - close-packed-planes
---

# ✏️ Problem: T2-CS10 — Identification of Gallium in an Orthorhombic Cell and Close-Packed Directions

## 📄 Official Statement
> **10. Three distinct crystallographic planes in the unit cell of a hypothetic metal are shown below. The circles represent atoms.**  
> * **Plane $(110)$:** Rectangle with dimensions $4.88\text{ \AA}$ (diagonal) and $3.32\text{ \AA}$ (vertical edge). Atoms at the 4 corners and 2 in the center of the base edges.
> * **Plane $(101)$:** Rectangle with dimensions $4.64\text{ \AA}$ and $3.65\text{ \AA}$. Atoms only at the 4 corners.
> * **Plane $(020)$:** Rectangle with dimensions $3.24\text{ \AA}$ and $3.32\text{ \AA}$. Atoms at the 4 corners.
> 
> **a)** To which crystalline structure does this unit cell belong?  
> **b)** Given that the density of this metal is $5.9\text{ g/cm}^3$, determine the atomic mass. Which specific metal is it referred to?  
> **c)** Identify the directions and planes of maximum packing.  
> *(Solution: a) Base centered orthorhombic lattice; b) $M = 69.76\text{ g/mol}$, Gallium; c) $[110], [\bar{1}10], [\bar{1}\bar{1}0], [1\bar{1}0], (001)$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Dimensions read from the planes:
  * From the $(020)$ plane: edge $a = 3.24\text{ \AA}$, edge $c = 3.32\text{ \AA}$.
  * From the $(110)$ plane: vertical edge $c = 3.32\text{ \AA}$, base diagonal $\sqrt{a^2 + b^2} = 4.88\text{ \AA}$.
  * From the $(101)$ plane: diagonal $\sqrt{a^2 + c^2} = \sqrt{3.24^2 + 3.32^2} = \sqrt{10.50 + 11.02} = \sqrt{21.52} \approx 4.64\text{ \AA}$, and edge $b = 3.65\text{ \AA}$.
* Volumetric density: $\rho = 5.9\text{ g/cm}^3$.
* Avogadro number: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Lattice Parameters ($a, b, c$):**
   * $a = 3.24\text{ \AA}$
   * $b = 3.65\text{ \AA}$ (check: $\sqrt{3.24^2 + 3.65^2} = \sqrt{10.50 + 13.32} = \sqrt{23.82} = 4.881\text{ \AA}$, in agreement with the $4.88\text{ \AA}$ read from the figure).
   * $c = 3.32\text{ \AA}$
   * Since $a \neq b \neq c$ and the planes form angles of $90^\circ$, the system is **Orthorhombic** [Session 3 Slide 12].
2. **Cell Centring Type (Bravais) [Session 3 Slide 9, 12]:**
   The $(110)$ plane contains atoms at the centre of the lower and upper base edges, which reveals that the basal face $(001)$ has a centred atom. By contrast, the $(101)$ and $(020)$ planes contain no atoms centred on their faces. Therefore, only the two $(001)$ bases are centred $\implies$ **Base-Centred Orthorhombic Lattice (Base-Centered Orthorhombic, $C$)**.
3. **Number of Atoms per Cell:**
   $$n = 8 \times \left(\frac{1}{8}\right)_{\text{vértices}} + 2 \times \left(\frac{1}{2}\right)_{\text{bases}} = 1 + 1 = 2\text{ átomos/celda}$$
4. **Molar Atomic Mass:**
   $$M = \frac{\rho \cdot (a \cdot b \cdot c) \cdot N_A}{n}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Identification of the Crystal Lattice
* Edges: $a = 3.24\text{ \AA}$, $b = 3.65\text{ \AA}$, $c = 3.32\text{ \AA}$ ($a \neq b \neq c$).
* Angles: $\alpha = \beta = \gamma = 90^\circ$.
* Atom arrangement: Atoms at the 8 vertices and at the barycentres of the two opposite basal faces $z=0$ and $z=c$.
* Structure: **Base-centred orthorhombic lattice (Base-centered Orthorhombic)**.

---

### 2. Part b: Atomic Mass and Identification
* **Unit cell volume:**
  $$V_C = a \cdot b \cdot c = (3.24 \times 10^{-8}\text{ cm}) \times (3.65 \times 10^{-8}\text{ cm}) \times (3.32 \times 10^{-8}\text{ cm}) = 3.9262 \times 10^{-23}\text{ cm}^3$$
* **Atomic mass ($M$):**
  $$M = \frac{\rho \cdot V_C \cdot N_A}{n} = \frac{(5.9\text{ g/cm}^3) \times (3.9262 \times 10^{-23}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})}{2}$$
  $$M = \frac{2.3165 \times 10^{-22} \times 6.022 \times 10^{23}}{2} = \frac{139.50}{2} = \mathbf{69.75\text{ g/mol}}$$

> [!warning] Discrepancy with the official solution
> The official key gives $69.76\text{ g/mol}$. With the $N_A = 6.022\times10^{23}\text{ mol}^{-1}$ used throughout this page the result is $69.75\text{ g/mol}$; the key's value follows from $N_A = 6.023\times10^{23}$ (the value supplied in Problem 5 of the same sheet), $0.015\%$ higher. The difference is a constant-rounding effect and no data were altered. Both identify gallium ($69.72\text{ g/mol}$).
* **Identification of the Metal:**
  The chemical element with a molar mass of $\approx 69.7\text{ g/mol}$ and density $\approx 5.9\text{ g/cm}^3$ is **Gallium ($\text{Ga}$)**.

---

### 3. Part c: Directions and Planes of Maximum Packing
* **Plane of Maximum Packing:**
  * In the base-centred orthorhombic cell, the basal face $(001)$ contains the centred atom and the 4 vertex atoms over an area $a \cdot b = 3.24 \times 3.65 = 11.83\text{ \AA}^2$.
  * Planar density of $(001)$: $\rho_{(001)} = \frac{2}{11.83 \times 10^{-16}\text{ cm}^2} = 1.69 \times 10^{15}\text{ at/cm}^2$.
  * Therefore, the most densely packed plane is **$(001)$** (the basal plane).
* **Directions of Maximum Packing:**
  * In the $(001)$ plane, the vertex atoms and the central atom are aligned along the diagonals of the basal face:
    $$\mathbf{[110], \quad [\bar{1}10], \quad [\bar{1}\bar{1}0], \quad [1\bar{1}0]}$$
  * Along these 4 coplanar diagonal directions, the atoms are in continuous mutual contact.

---

## 🎯 4. Phase 4: Units and Limits

* **Physics of Gallium:** Pure gallium is an extremely singular element in aerospace materials science and optoelectronics ($\text{GaAs}, \text{GaN}$). It has an extremely low melting temperature ($T_m = 29.76^\circ\text{C}$), melting with the heat of a human hand, and crystallises at room temperature in a slightly distorted orthorhombic lattice in which the atoms form almost molecular $\text{Ga}_2$ dimers oriented along the dense directions of the $(001)$ plane.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
