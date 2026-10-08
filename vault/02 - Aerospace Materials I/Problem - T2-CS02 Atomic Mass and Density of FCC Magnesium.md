---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2_CrystStruct.pdf, Problem 2"
dificultad: low
tags:
  - official-problem
  - solved
  - atomic-mass
  - density
  - fcc
  - magnesium
---

# ✏️ Problem: T2-CS02 — Atomic Mass and Density of FCC Magnesium

## 📄 Official Statement
> **2. Determine the atomic mass of a metal element with FCC structure, density of $1.74\text{ g/cm}^3$ and lattice constant of $4.527\text{ \AA}$. Find the element with these characteristics.**  
> *(Solution: $M = 24.3\text{ g/mol}$; $\text{Mg}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Crystal structure: Face-Centred Cubic (FCC) $\implies n = 4\text{ átomos/celda}$.
* Lattice parameter: $a = 4.527\text{ \AA} = 4.527 \times 10^{-8}\text{ cm} = 0.4527\text{ nm}$.
* Macroscopic volumetric density: $\rho = 1.74\text{ g/cm}^3 = 1740\text{ kg/m}^3$.
* Avogadro constant: $N_A = 6.022 \times 10^{23}\text{ átomos/mol}$.

### Starting Hypotheses:
1. The metal is a pure single crystal free of vacancies or defects that would significantly alter the apparent density.
2. The cubic unit cell satisfies $V_C = a^3$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the theoretical foundations of the course [Session 4 Slide 7, 15]:
* The theoretical volumetric density of a crystalline solid is defined by the ratio of the cell mass to its volume:
  $$\rho = \frac{m_{\text{celda}}}{V_C} = \frac{n \cdot M}{a^3 \cdot N_A}$$
* Solving algebraically for the molar atomic mass $M$:
  $$M = \frac{\rho \cdot a^3 \cdot N_A}{n}$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

1. **Unit cell volume ($V_C$):**
   $$a = 4.527 \times 10^{-8}\text{ cm}$$
   $$V_C = a^3 = (4.527 \times 10^{-8}\text{ cm})^3 = 9.2775 \times 10^{-23}\text{ cm}^3$$

2. **Molar mass ($M$):**
   $$M = \frac{(1.74\text{ g/cm}^3) \times (9.2775 \times 10^{-23}\text{ cm}^3) \times (6.02214 \times 10^{23}\text{ mol}^{-1})}{4}$$
   $$M = \frac{1.6143 \times 10^{-22} \times 6.02214 \times 10^{23}}{4} = \frac{97.215}{4} = \mathbf{24.304\text{ g/mol}}$$

3. **Identification in the Periodic Table:**
   Checking the standard atomic weights of the elements:
   * Sodium ($\text{Na}$): $22.99\text{ g/mol}$
   * **Magnesium ($\text{Mg}$):** $24.305\text{ g/mol}$ (our $24.304\text{ g/mol}$ agrees to $0.004\%$; the official key rounds to $24.3$).
   * Aluminium ($\text{Al}$): $26.98\text{ g/mol}$

   Therefore, the element with these physical characteristics and atomic mass is **Magnesium ($\text{Mg}$)**.

---

## 🎯 4. Phase 4: Units and Limits

* **Crystallographic Analysis:** At ambient temperature and pressure, pure magnesium usually crystallises in the **HCP** structure ($c/a \approx 1.624$) with density $1.738\text{ g/cm}^3$. However, in thin films, epitaxial metastable states or as a theoretical polymorphic phase, it can adopt the FCC cubic configuration while keeping the same bulk atomic density.
* **Dimensional Consistency:**
  $$[M] = \frac{[\text{g/cm}^3] \cdot [\text{cm}^3] \cdot [\text{mol}^{-1}]}{[\text{adimensional}]} = \text{g/mol} \quad \checkmark$$

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
