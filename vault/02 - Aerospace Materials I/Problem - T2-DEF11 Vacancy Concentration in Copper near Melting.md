---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 11"
dificultad: medium
tags:
  - official-problem
  - solved
  - copper
  - fcc
  - vacancies-concentration
  - arrhenius
  - high-temperature
---

# ✏️ Problem: T2-DEF11 — Vacancy Concentration in Copper near the Melting Point

## 📄 Official Statement
> **11. Calculate the number of vacancies per $\text{cm}^3$ expected in copper at $1080^\circ\text{C}$ (just below the melting temperature). The energy for vacancy formation is $20000\text{ cal/mol}$.**  
> *(Solution: $4.98 \times 10^{19}\text{ vacancies/cm}^3$)*  
> **Data:** Copper has an FCC crystal structure and a lattice parameter of $3.6151\text{ \AA}$; $R = 1.987\text{ cal/(mol}\cdot\text{K)}$.

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Material: Pure copper ($\text{Cu}$, FCC lattice with $n = 4\text{ átomos/celda}$).
* Lattice parameter: $a = 3.6151\text{ \AA} = 3.6151 \times 10^{-8}\text{ cm}$.
* Temperature: $T = 1080^\circ\text{C} = 1080 + 273.15 = 1353.15\text{ K}$ (melting point of pure copper: $T_m = 1084.6^\circ\text{C}$).
* Vacancy formation energy: $\Delta H_v = 20000\text{ cal/mol}$.
* Universal gas constant: $R = 1.987\text{ cal/(mol}\cdot\text{K)}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

1. **Total Number of Lattice Sites per Unit Volume ($N$):**
   In an FCC cubic unit cell of volume $V_C = a^3$ there are $4$ equivalent lattice points [Session 4 Slide 15]:
   $$N = \frac{n}{V_C} = \frac{4}{a^3} \quad [\text{sitios/cm}^3]$$
2. **Boltzmann Thermodynamic Equation for Vacancies [Session 4 Slide 15]:**
   $$n_v = N \cdot \exp\left(-\frac{\Delta H_v}{R \cdot T}\right)$$
   where $n_v$ is the number of vacancies in thermal equilibrium per cubic centimetre.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Number of Lattice Positions ($N$):
* Volume of the cubic unit cell:
  $$V_C = a^3 = (3.6151 \times 10^{-8}\text{ cm})^3 = 4.72457 \times 10^{-23}\text{ cm}^3$$
* Total concentration of lattice nodes:
  $$N = \frac{4}{4.72457 \times 10^{-23}\text{ cm}^3} = \mathbf{8.46638 \times 10^{22}\text{ sitios/cm}^3}$$

---

### 2. Boltzmann Factor ($\exp(-\Delta H_v / RT)$):
* Thermal denominator:
  $$R \cdot T = (1.987\text{ cal/mol}\cdot\text{K}) \times (1353.15\text{ K}) = 2688.71\text{ cal/mol}$$
* Dimensionless exponent:
  $$-\frac{\Delta H_v}{R \cdot T} = -\frac{20000\text{ cal/mol}}{2688.71\text{ cal/mol}} = -7.43851$$
* Vacancy fraction in thermal equilibrium:
  $$\frac{n_v}{N} = \exp(-7.43851) = \mathbf{5.88166 \times 10^{-4}}$$
  *(Note that $\approx 0.059\%$, perfectly consistent with the order of magnitude of $10^{-4}$ near melting [Slide 15]).*

---

### 3. Vacancies per Cubic Centimetre ($n_v$):
$$n_v = N \times \left(\frac{n_v}{N}\right) = (8.46638 \times 10^{22}\text{ cm}^{-3}) \times (5.88166 \times 10^{-4})$$
$$n_v = 4.9796 \times 10^{19} \approx \mathbf{4.98 \times 10^{19}\text{ vacancies / cm}^3}$$

---

## 🎯 4. Phase 4: Units and Limits

* **Macroscopic Magnitude:** Although the percentage fraction seems small ($0.059\%$), a single cubic centimetre of copper heated to $1080^\circ\text{C}$ holds the enormous quantity of almost **$50$ quintillion vacancies** ($4.98 \times 10^{19}\text{ vacantes}$).
* **Role in Diffusion and Creep:** This colossal vacancy density allows copper atoms to jump continuously into adjacent empty positions at frequencies of the order of $10^{10}\text{ jumps/s}$, which explains why at temperatures above $0.5\, T_m$ metals undergo thermal creep deformation and dislocations can climb (*dislocation climb*), bypassing obstacles.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
