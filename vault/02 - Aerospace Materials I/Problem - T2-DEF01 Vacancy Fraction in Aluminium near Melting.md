---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 1"
dificultad: medium
tags:
  - official-problem
  - solved
  - thermal-vacancies
  - aluminum
  - point-defects
  - arrhenius
---

# ✏️ Problem: T2-DEF01 — Vacancy Fraction in Aluminium near the Melting Point

## 📄 Official Statement
> **1. The fraction of vacancies in an aluminum lattice is $2.29 \times 10^{-5}$ at $400^\circ\text{C}$. Calculate the fraction of vacancies at $660^\circ\text{C}$ (just before the melting point). $R = 8.31\text{ J/(mol}\cdot\text{K)}$.**  
> *(Solution: $4.53 \times 10^{-4}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Material: Pure aluminium ($\text{Al}$, FCC lattice).
* Temperature 1: $T_1 = 400^\circ\text{C} = 400 + 273.15 = 673.15\text{ K}$.
* Vacancy fraction at $T_1$:
  $$\left(\frac{n_v}{N}\right)_1 = 2.29 \times 10^{-5}$$
* Temperature 2: $T_2 = 660^\circ\text{C} = 660 + 273.15 = 933.15\text{ K}$ (temperature just below the melting of aluminium, $T_m \approx 660.3^\circ\text{C}$).
* Universal gas constant: $R = 8.31\text{ J/(mol}\cdot\text{K)}$.

---

## 🧠 2. Phase 2: Frames and Change of Basis

The thermodynamic equilibrium concentration of vacancies in a metallic lattice follows the Boltzmann distribution [Session 4 Slide 15]:

$$\frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{RT}\right)$$

where $\Delta H_v$ is the enthalpy of formation of one mole of vacancies in the lattice.

### Solution Strategy:
1. With the data at $T_1$, determine the vacancy formation enthalpy $\Delta H_v$:
   $$\ln\left(\frac{n_v}{N}\right)_1 = -\frac{\Delta H_v}{R \cdot T_1} \implies \Delta H_v = -R \cdot T_1 \cdot \ln\left(\frac{n_v}{N}\right)_1$$
2. With $\Delta H_v$ constant (independent of temperature in this range), compute the new fraction at $T_2$:
   $$\left(\frac{n_v}{N}\right)_2 = \exp\left(-\frac{\Delta H_v}{R \cdot T_2}\right)$$
   Or, combining into a single two-point relation:
   $$\ln\left( \frac{(n_v/N)_2}{(n_v/N)_1} \right) = -\frac{\Delta H_v}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Formation Enthalpy ($\Delta H_v$):
* Natural logarithm of the initial fraction:
  $$\ln(2.29 \times 10^{-5}) = -10.68437$$
* Solving for $\Delta H_v$:
  $$\Delta H_v = -(8.31\text{ J/mol}\cdot\text{K}) \times (673.15\text{ K}) \times (-10.68437)$$
  $$\Delta H_v = 5593.8765 \times 10.68437 = 59767.1\text{ J/mol} \approx \mathbf{59.77\text{ kJ/mol}}$$
  *(In atomic units: $E_v = \frac{59767.1}{6.022 \times 10^{23} \times 1.602 \times 10^{-19}} \approx 0.62\text{ eV/átomo}$, consistent with the literature for aluminium).*

---

### 2. Vacancy Fraction at $660^\circ\text{C}$ ($T_2 = 933.15\text{ K}$):
* Boltzmann exponent at $T_2$:
  $$\frac{\Delta H_v}{R \cdot T_2} = \frac{59767.1\text{ J/mol}}{(8.31\text{ J/mol}\cdot\text{K}) \times (933.15\text{ K})} = \frac{59767.1}{7754.4765} = 7.70743$$
* Equilibrium vacancy fraction:
  $$\left(\frac{n_v}{N}\right)_2 = \exp(-7.70743) = \mathbf{4.49 \times 10^{-4}}$$
  Check with $T = 273 + t$ (i.e. $T_1 = 673\text{ K}$, $T_2 = 933\text{ K}$): $\Delta H_v = 8.31 \times 673 \times 10.68437 = 59754\text{ J/mol}$ and $(n_v/N)_2 = \exp(-59754/(8.31 \times 933)) = \exp(-7.7069) = 4.50 \times 10^{-4}$.

> [!warning] Discrepancy with the official solution
> The official key gives $4.53\times10^{-4}$. Recomputing from the given data ($2.29\times10^{-5}$ at $400^\circ\text{C}$, $R = 8.31\text{ J/(mol K)}$) gives $\exp(-7.7074) = 4.49\times10^{-4}$ with $T = 273.15 + t$, and $\exp(-7.7069) = 4.50\times10^{-4}$ with $T = 273 + t$ ($\Delta H_v = 59.75\text{ kJ/mol}$). The key's $4.53\times10^{-4}$ ($\approx 0.8\%$ higher) is not reproduced by either convention; no value was adjusted.

---

## 🎯 4. Phase 4: Units and Limits

* **Exponential Thermal Increase:** Going from $400^\circ\text{C}$ to $660^\circ\text{C}$ ($\Delta T = 260^\circ\text{C}$), the vacancy concentration is multiplied by a factor of:
  $$\frac{4.49 \times 10^{-4}}{2.29 \times 10^{-5}} \approx \mathbf{19.6\text{ veces}}$$
* **Physical Limit of Real Crystals:** The fraction reached near melting ($4.49 \times 10^{-4} \approx 1\text{ vacante por cada } 2200\text{ átomos}$) satisfies the general rule quoted in the official slide [Session 4 Slide 15]:
  $$\frac{n_v}{N} \sim 10^{-4}\text{ máximo}$$
  This high density of thermal vacancies near the melting point is responsible for the drastic increase in the rate of atomic diffusion in homogenisation and aeronautical sintering processes.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
