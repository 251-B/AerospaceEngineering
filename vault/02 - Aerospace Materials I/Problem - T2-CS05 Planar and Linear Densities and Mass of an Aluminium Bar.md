---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 5"
dificultad: medium
tags:
  - official-problem
  - solved
  - aluminum
  - fcc
  - planar-density
  - linear-density
  - bar-mass
---

# ✏️ Problem: T2-CS05 — Planar and Linear Densities and Mass of an Aluminium Bar

## 📄 Official Statement
> **5. Given that aluminum has an FCC structure, the atomic radius $1.43\text{ \AA}$ and the atomic weight $26.98\text{ g/mol}$, calculate:**  
> **a)** Planar density, in $\text{at/cm}^2$, for the $(110)$ plane. *(Solution: $\rho_{(110)} = 8.7 \times 10^{14}\text{ at/cm}^2$)*  
> **b)** Linear density, in $\text{at/cm}$, for the $[110]$ direction. *(Solution: $\rho_{[110]} = 3.5 \times 10^7\text{ at/cm}$)*  
> **c)** Weight of a bar of $20\text{ mm}$ in diameter and $1\text{ m}$ long. *(Solution: $m = 855\text{ g}$)*  
> **Data:** $1\text{ m} = 10^{10}\text{ \AA}$; $N_A = 6.023 \times 10^{23}\text{ mol}^{-1}$.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Structure: Face-Centred Cubic (FCC) $\implies n = 4\text{ átomos/celda}$.
* Atomic radius: $R = 1.43\text{ \AA} = 1.43 \times 10^{-8}\text{ cm} = 0.143\text{ nm}$.
* Molar atomic weight: $M = 26.98\text{ g/mol}$.
* Aluminium bar dimensions:
  * Diameter: $D = 20\text{ mm} = 2.0\text{ cm}$.
  * Length: $L = 1\text{ m} = 100\text{ cm}$.
* Avogadro constant: $N_A = 6.023 \times 10^{23}\text{ mol}^{-1}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Lattice Parameter in FCC [Session 3 Slide 20]:**
   The atoms touch along the face diagonal:
   $$4R = a\sqrt{2} \implies a = 2\sqrt{2}R$$
2. **Planar Density on the $(110)$ Plane [Session 4 Slide 8]:**
   The $(110)$ plane is a rectangle of base $a\sqrt{2}$ and height $a$. It contains 2 net atoms:
   $$\rho_{(110)} = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$
3. **Linear Density in the $[110]$ Direction [Session 4 Slide 7]:**
   The $[110]$ direction is the face diagonal, with length $L_{[110]} = a\sqrt{2} = 4R$. It contains 2 net atoms:
   $$\rho_{[110]} = \frac{2}{4R} = \frac{1}{2R}$$
4. **Mass of the Cylindrical Bar:**
   From the theoretical volumetric density:
   $$\rho_v = \frac{n \cdot M}{a^3 \cdot N_A}$$
   The volume of the cylindrical bar is:
   $$V = \pi \left(\frac{D}{2}\right)^2 L$$
   The total mass is $m = \rho_v \cdot V$.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Lattice Parameter ($a$):
$$a = 2\sqrt{2} R = 2 \times \sqrt{2} \times (1.43 \times 10^{-8}\text{ cm}) = 4.04465 \times 10^{-8}\text{ cm} = 4.045\text{ \AA}$$

### 2. Part a: Planar Density on $(110)$:
$$A_{(110)} = \sqrt{2} a^2 = \sqrt{2} \times (4.04465 \times 10^{-8}\text{ cm})^2 = \sqrt{2} \times 1.6359 \times 10^{-15}\text{ cm}^2 = 2.3135 \times 10^{-15}\text{ cm}^2$$
The plane contains $N_{\text{átomos}} = 4 \times \frac{1}{4} + 2 \times \frac{1}{2} = 2\text{ átomos}$:
$$\rho_{(110)} = \frac{2\text{ at}}{2.3135 \times 10^{-15}\text{ cm}^2} = 8.645 \times 10^{14} \approx \mathbf{8.6 \times 10^{14}\text{ at/cm}^2}$$

> [!warning] Discrepancy with the official solution
> The official key gives $8.7\times10^{14}\text{ at/cm}^2$; the given radius ($R = 1.43\text{ \AA}$) yields $8.645\times10^{14}\text{ at/cm}^2$, i.e. $8.6\times10^{14}$ to two significant figures. The official figure is reproduced only if $a$ is first rounded to $4.04\text{ \AA}$ ($8.66\times10^{14}$); that rounding is not applied here.

### 3. Part b: Linear Density on $[110]$:
Since $[110]$ is the close-packed direction ($L = 4R$):
$$\rho_{[110]} = \frac{1}{2R} = \frac{1}{2 \times (1.43 \times 10^{-8}\text{ cm})} = \frac{1}{2.86 \times 10^{-8}\text{ cm}} = 3.4965 \times 10^7 \approx \mathbf{3.5 \times 10^7\text{ at/cm}}$$

### 4. Part c: Mass of the Bar:
* **Unit cell volume:**
  $$V_C = a^3 = (4.04465 \times 10^{-8}\text{ cm})^3 = 6.6167 \times 10^{-23}\text{ cm}^3$$
* **Volumetric density of aluminium:**
  $$\rho_v = \frac{4 \times 26.98\text{ g/mol}}{(6.6167 \times 10^{-23}\text{ cm}^3) \times (6.023 \times 10^{23}\text{ mol}^{-1})} = \frac{107.92}{39.853} = 2.708\text{ g/cm}^3$$
* **Macroscopic volume of the bar:**
  $$V = \pi \left(\frac{2.0\text{ cm}}{2}\right)^2 \times (100\text{ cm}) = 100\pi \approx 314.159\text{ cm}^3$$
* **Total calculated mass:**
  $$m = \rho_v \cdot V = (2.708\text{ g/cm}^3) \times (314.159\text{ cm}^3) = \mathbf{850.7\text{ g}} \approx \mathbf{851\text{ g}}$$

> [!warning] Discrepancy with the official solution
> The official key gives $m = 855\text{ g}$. The given data ($R = 1.43\text{ \AA}$, $M = 26.98\text{ g/mol}$, $N_A = 6.023\times10^{23}\text{ mol}^{-1}$) give $\rho = 2.708\text{ g/cm}^3$ and $m = 850.7\text{ g}$ ($\approx 851\text{ g}$, $0.5\%$ below the key). $855\text{ g}$ would require $\rho \approx 2.72\text{ g/cm}^3$, which is inconsistent with the computed $2.708\text{ g/cm}^3$ and is not used.

---

## 🎯 4. Phase 4: Units and Limits

* **Consistency with Aeronautical Aluminium:** The calculated theoretical density of $2.708\text{ g/cm}^3$ reproduces the reference value for light aerospace aluminium alloys (such as the 2024-T3 and 7075-T6 series, with $\rho \approx 2.7\text{--}2.8\text{ g/cm}^3$), whose low specific weight is the backbone of pressurised fuselage and wing-skin airframe structures.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
