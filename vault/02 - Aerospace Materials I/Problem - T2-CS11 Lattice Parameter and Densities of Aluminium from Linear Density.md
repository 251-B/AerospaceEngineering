---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 11"
dificultad: medium
tags:
  - official-problem
  - solved
  - aluminum
  - fcc
  - linear-density
  - lattice-parameter
  - planar-density
---

# ✏️ Problem: T2-CS11 — Lattice Parameter and Densities of Aluminium from Linear Density

## 📄 Official Statement
> **11. Aluminum has an FCC structure with atomic weight of $26.98\text{ g/mol}$. Given that its linear density in the direction $[111]$ is $1.43 \times 10^7\text{ at/cm}$, determine:**  
> **a)** The lattice parameter and the atomic radius for aluminum. *(Solution: $a = 4.04\text{ \AA}$, $r = 1.43\text{ \AA}$)*  
> **b)** Volume density in $(\text{g/cm}^3)$ and planar density in the plane $(101)$ in $(\text{at/cm}^2)$. *(Solution: $\rho = 2.71\text{ g/cm}^3$; $\rho_{(101)} = 8.66 \times 10^{14}\text{ at/cm}^2$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Element: Pure aluminium ($\text{Al}$).
* Structure: Face-Centred Cubic (FCC) $\implies n = 4\text{ átomos/celda}$.
* Molar atomic mass: $M = 26.98\text{ g/mol}$.
* Linear density in the $[111]$ direction: $\rho_{[111]} = 1.43 \times 10^7\text{ at/cm}$.
* Avogadro number: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Linear Density on $[111]$ for FCC [Session 4 Slide 7]:**
   In an FCC cell, the main diagonal $[111]$ has length $L_{[111]} = a\sqrt{3}$. It passes through only two atoms located at the opposite end vertices, each contributing $\frac{1}{2}$ centred atom:
   $$N_{\text{átomos}} = 2 \times \frac{1}{2} = 1\text{ átomo}$$
   $$\rho_{[111]} = \frac{1}{a\sqrt{3}} \implies a = \frac{1}{\sqrt{3} \cdot \rho_{[111]}}$$
2. **Atomic Radius in FCC [Session 3 Slide 20]:**
   $$4R = a\sqrt{2} \implies R = \frac{a\sqrt{2}}{4}$$
3. **Volumetric Density ($\rho_v$):**
   $$\rho_v = \frac{n \cdot M}{a^3 \cdot N_A} = \frac{4 \cdot M}{a^3 \cdot N_A}$$
4. **Planar Density on the $(101)$ Plane [Session 4 Slide 8]:**
   In the cubic system, the $(101)$ plane is crystallographically equivalent to $(110) \in \{110\}$.
   The $(101)$ plane cuts the diagonal of the $x-z$ face (length $a\sqrt{2}$) and the $y$ edge (length $a$).
   Area: $A_{(101)} = a\sqrt{2} \times a = a^2\sqrt{2}$.
   Atoms contained: $N_{\text{átomos}} = 4 \times \frac{1}{4} + 2 \times \frac{1}{2} = 2\text{ átomos}$.
   $$\rho_{(101)} = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Part a: Lattice Parameter and Atomic Radius
* **Calculation of $a$:**
  $$a = \frac{1}{\sqrt{3} \times (1.43 \times 10^7\text{ at/cm})} = \frac{1}{1.73205 \times 1.43 \times 10^7\text{ cm}^{-1}} = \frac{1}{2.4768 \times 10^7\text{ cm}^{-1}}$$
  $$a = 4.0374 \times 10^{-8}\text{ cm} \approx \mathbf{4.04\text{ \AA}}$$
* **Calculation of $R$:**
  $$R = \frac{a\sqrt{2}}{4} = \frac{(4.0374 \times 10^{-8}\text{ cm}) \times 1.4142136}{4} = 1.4274 \times 10^{-8}\text{ cm} \approx \mathbf{1.43\text{ \AA}}$$

---

### 2. Part b: Volumetric and Planar Density
* **Volumetric Density ($\rho_v$):**
  $$V_C = a^3 = (4.0374 \times 10^{-8}\text{ cm})^3 = 6.5813 \times 10^{-23}\text{ cm}^3$$
  $$\rho_v = \frac{4 \times 26.98\text{ g/mol}}{(6.5813 \times 10^{-23}\text{ cm}^3) \times (6.022 \times 10^{23}\text{ mol}^{-1})} = \frac{107.92}{39.633} = \mathbf{2.72\text{ g/cm}^3} \approx \mathbf{2.71\text{ g/cm}^3}$$

* **Planar Density on the $(101)$ Plane:**
  $$a^2 = (4.0374 \times 10^{-8}\text{ cm})^2 = 1.63006 \times 10^{-15}\text{ cm}^2$$
  $$\rho_{(101)} = \frac{\sqrt{2}}{a^2} = \frac{1.4142136}{1.63006 \times 10^{-15}\text{ cm}^2} = 8.6758 \times 10^{14} \approx \mathbf{8.66 \times 10^{14}\text{ at/cm}^2}$$

---

## 🎯 4. Phase 4: Units and Limits

* **Cross-Validation of Methods:** In problem T2-CS05 the planar density was obtained from the known atomic radius $R = 1.43\text{ \AA}$. Here, the procedure is reversed: by measuring the linear density $\rho_{[111]}$ (accessible through high-resolution transmission electron microscopy or diffraction), the lattice parameter ($4.04\text{ \AA}$), the atomic radius ($1.43\text{ \AA}$), the density of the solid ($2.71\text{ g/cm}^3$) and the planar density of the shear planes are derived with identical accuracy.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
