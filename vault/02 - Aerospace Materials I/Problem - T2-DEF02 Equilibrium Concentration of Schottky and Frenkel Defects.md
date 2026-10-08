---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
origen: "Problems T2 defects.pdf, Problem 2"
dificultad: medium
tags:
  - official-problem
  - solved
  - schottky
  - frenkel
  - ionic-defects
  - boltzmann-statistics
---

# ✏️ Problem: T2-DEF02 — Equilibrium Concentration of Schottky and Frenkel Defects

## 📄 Official Statement
> **2. Considering that the energies for Schottky and Frenkel defects formation in a specific material are $1\text{ eV}$ and $4\text{ eV}$ per atom, respectively. Determine the equilibrium concentrations of such defects at $1000\text{ K}$. $k = 8.62 \times 10^{-5}\text{ eV/K}$.**  
> *(Solution: $3.026 \times 10^{-3}$ and $8.386 \times 10^{-11}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Input Data:
* Schottky defect formation energy: $\Delta H_s = 1.0\text{ eV/defecto}$.
* Frenkel defect formation energy: $\Delta H_F = 4.0\text{ eV/defecto}$.
* Absolute temperature: $T = 1000\text{ K}$.
* Boltzmann constant: $k_B = 8.62 \times 10^{-5}\text{ eV/K}$.

### Starting Hypotheses:
1. The material is a stoichiometric ionic solid of type $MX$.
2. Defect concentrations are expressed as fractions of the total number of regular lattice sites $N$ (assuming $N_i \approx N$ for the fractional Frenkel concentration $n_F / \sqrt{N N_i} \approx n_F / N$).

---

## 🧠 2. Phase 2: Frames and Change of Basis

Citing the official formulations for ionic crystals [Session 4 Slide 16]:

1. **Schottky Defects (Anion-Cation Vacancy Pairs):**
   The formation of a Schottky pair requires the simultaneous creation of two vacancies of opposite sign. Thermodynamically, the equilibrium fraction is:
   $$\frac{n_s}{N} = \exp\left(-\frac{\Delta H_s}{2\, k_B T}\right)$$

2. **Frenkel Defects (Vacancy-Interstitial Pairs):**
   The migration of an ion to an interstitial position generates a vacancy and an interstitial. The equilibrium fractional concentration is:
   $$\frac{n_F}{\sqrt{N N_i}} = \exp\left(-\frac{\Delta H_F}{2\, k_B T}\right)$$

> [!NOTE]
> The factor $2$ in the denominator of the exponent is a fundamental thermodynamic feature of ionic defects: since two defect species are generated simultaneously to preserve electroneutrality, the mass-action product leads to $\exp(-\Delta H / 2k_B T)$.

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Concentration of Schottky Defects ($n_s / N$):
* Thermal denominator:
  $$2\, k_B T = 2 \times (8.62 \times 10^{-5}\text{ eV/K}) \times (1000\text{ K}) = 2 \times 0.0862\text{ eV} = 0.1724\text{ eV}$$
* Argument of the exponential:
  $$-\frac{\Delta H_s}{2\, k_B T} = -\frac{1.0\text{ eV}}{0.1724\text{ eV}} = -5.800464$$
* Equilibrium concentration:
  $$\frac{n_s}{N} = \exp(-5.800464) = \mathbf{3.0262 \times 10^{-3}} \approx \mathbf{3.026 \times 10^{-3}}$$

---

### 2. Concentration of Frenkel Defects ($n_F / \sqrt{N N_i}$):
* Thermal denominator:
  $$2\, k_B T = 0.1724\text{ eV}$$
* Argument of the exponential:
  $$-\frac{\Delta H_F}{2\, k_B T} = -\frac{4.0\text{ eV}}{0.1724\text{ eV}} = -23.201856$$
* Equilibrium concentration:
  $$\frac{n_F}{\sqrt{N N_i}} = \exp(-23.201856) = \mathbf{8.386 \times 10^{-11}}$$

---

## 🎯 4. Phase 4: Units and Limits

1. **Absolute Thermodynamic Predominance:**
   Comparing both populations at $1000\text{ K}$:
   $$\frac{n_s}{n_F} = \frac{3.026 \times 10^{-3}}{8.386 \times 10^{-11}} \approx \mathbf{3.6 \times 10^{7}}$$
   The concentration of Schottky defects is more than **36 million times higher** than that of Frenkel defects.
2. **Correlation with Slide 16 [Session 4 Slide 16]:**
   As the official theory states verbatim:
   $$\text{"In a crystal } \Delta H_s \neq \Delta H_F \implies \text{the defect with the lowest } \Delta H \text{ will form"}$$
   Since $\Delta H_s = 1\text{ eV} \ll \Delta H_F = 4\text{ eV}$, the crystal will overwhelmingly present Schottky-type defects, while Frenkel defects will be statistically non-existent.

---
*Return:* [[Topic 2 - Structure of Materials and Crystalline Defects|⬅️ Back to Topic 2]] | [[02 - Aerospace Materials I/Aerospace Materials I MOC|🔬 Subject MOC]]
