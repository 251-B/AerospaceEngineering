---
materia: "Aerospace Materials I"
tema: "Topic 2: Structure of Materials and Crystalline Defects"
fuentes: "Session 4 T2 Structure of Materials II_2025.pdf, Slides 12-18"
tags:
  - theory
  - fundamental-concept
  - point-defects
  - vacancies
  - schottky
  - frenkel
  - defect-thermodynamics
dificultad: high
prerrequisitos:
  - "[[Concept - X-Ray Diffraction and Bragg's Law]]"
---

# 🔘 Concept: Point Defects, Thermal Vacancies, Schottky and Frenkel

> **Thermodynamic Principle:** A perfect, defect-free crystal can only exist at absolute zero ($T = 0\text{ K}$). At any temperature $T > 0\text{ K}$, the spontaneous introduction of zero-dimensional defects (**point defects**) raises the enthalpy of the crystal ($\Delta H > 0$), but produces an extraordinary increase in the **configurational entropy** ($\Delta S_{\text{conf}} > 0$). Therefore, the Gibbs free energy change $\Delta G = \Delta H - T\Delta S$ reaches a stable minimum at a finite equilibrium defect concentration [Slides 11, 15].

---

## 🌡️ 1. Thermodynamics of Vacancy Formation in Metals

A **vacancy** is the absence of an atom or ion at a regular lattice site [Slide 15].

### Derivation of the Equilibrium Concentration ($n_v/N$):
Consider a metallic crystal with $N$ lattice sites and $n_v$ vacancies. The number of indistinguishable microscopic ways of distributing $n_v$ vacancies over $N$ sites is given by the combinatorics:
$$W = \frac{N!}{(N - n_v)! \, n_v!}$$

The configurational entropy according to the Boltzmann equation is:
$$S = k_B \ln W = k_B \left[ \ln N! - \ln(N - n_v)! - \ln n_v! \right]$$

Applying Stirling's approximation ($\ln x! \approx x\ln x - x$):
$$S \approx k_B \left[ N\ln N - (N - n_v)\ln(N - n_v) - n_v \ln n_v \right]$$

The change in Gibbs free energy to form $n_v$ vacancies with formation enthalpy $\Delta H_v$ per mole is:
$$\Delta G(n_v) = n_v \Delta H_v - T \Delta S$$

At thermodynamic equilibrium at constant temperature $T$, the free energy is minimized:
$$\left( \frac{\partial \Delta G}{\partial n_v} \right)_T = \Delta H_v - k_B T \ln\left( \frac{N - n_v}{n_v} \right) = 0$$

Since $n_v \ll N$ ($n_v/N \sim 10^{-4}$ near the melting point [Slide 15]):
$$\ln\left(\frac{N}{n_v}\right) = \frac{\Delta H_v}{k_B T} \implies \frac{n_v}{N} = \exp\left(-\frac{\Delta H_v}{k_B T}\right) = \exp\left(-\frac{\Delta H_v}{RT}\right)$$

### Explicit Differentiation Step (added)
Using $\frac{d}{dn}\left[x\ln x\right] = \ln x + 1$ with the chain rule on $(N - n_v)$:

$$\frac{\partial}{\partial n_v}\Big[-(N-n_v)\ln(N-n_v) - n_v\ln n_v\Big] = \big[\ln(N-n_v) + 1\big] - \big[\ln n_v + 1\big] = \ln\frac{N-n_v}{n_v}$$

so $\partial S/\partial n_v = k_B\ln\frac{N-n_v}{n_v}$ and $\partial\Delta G/\partial n_v = E_v - k_BT\ln\frac{N-n_v}{n_v} = 0$, where $E_v$ is the formation energy **per vacancy**. For $n_v \ll N$, $\ln\frac{N-n_v}{n_v}\approx\ln\frac{N}{n_v}$ and

$$\frac{n_v}{N} = \exp\left(-\frac{E_v}{k_BT}\right) = \exp\left(-\frac{\Delta H_v}{RT}\right), \qquad \Delta H_v = N_A E_v \ \text{(per mole)}, \quad R = N_Ak_B$$

Use $E_v$ with $k_B$ (J or eV per vacancy) or $\Delta H_v$ with $R$ (J/mol) and never mix the two. If the vibrational formation entropy $\Delta S_v$ of each vacancy is kept (slide: $\Delta G = \Delta H - T\Delta S$), the result acquires the prefactor $e^{\Delta S_v/k_B}$ (extension). Numerical illustration (Python): $E_v = 1.0\ \text{eV}$ gives $n_v/N = 9.1\times10^{-6}$ at $1000\ \text{K}$ and $1.6\times10^{-17}$ at $300\ \text{K}$, so vacancies are quenched-in only if the metal is cooled fast.

### Equation Parameters:
* $n_v$: equilibrium number of vacancies per unit volume ($\text{vacancies/cm}^3$).
* $N$: number density of lattice sites ($\text{sites/cm}^3$):
  $$N = \frac{\rho \cdot N_A}{M} = \frac{n_{\text{atoms per cell}}}{V_C}$$
* $\Delta H_v$: molar enthalpy or energy of formation of a vacancy ($\text{J/mol}$ or $\text{cal/mol}$, or $E_v$ in $\text{eV/atom}$).
* $R = 8.314\text{ J/mol}\cdot\text{K} = 1.987\text{ cal/mol}\cdot\text{K}$ (or Boltzmann constant $k_B = 8.62 \times 10^{-5}\text{ eV/K}$).
* Maximum vacancy fraction: In most metals near the melting temperature $T_m$, the fraction reaches $n_v/N \approx 10^{-4}\text{--}10^{-3}$ [Slide 15].

---

## ⚡ 2. Point Defects in Ionic Crystals (Schottky and Frenkel)

In ionic ceramics, any defect must strictly preserve the **macroscopic electroneutrality** of the crystal [Slide 16].

### a) Schottky Defect (Cation-Anion Vacancy Pair) [Slide 16]
* **Mechanism:** A cation and an anion simultaneously leave their regular lattice sites and migrate to the outer surface of the crystal.
* A **stoichiometric vacancy pair** is created ($1\text{ cation vacancy} + 1\text{ anion vacancy}$ in an $MX$ compound).
* The bulk density of the crystal **decreases**.
* **Equilibrium concentration:**
  $$n_s = N \exp\left(-\frac{\Delta H_s}{2RT}\right)$$
  *(The factor 2 in the denominator reflects that the formation of each defect involves the simultaneous creation of two independent vacancies).*

### b) Frenkel Defect (Vacancy-Interstitial Pair) [Slide 16]
* **Mechanism:** An ion (usually the cation, having the smaller atomic radius) jumps from its normal lattice site into a nearby interstitial void.
* An associated pair is formed: **1 cation vacancy + 1 interstitial cation**.
* The macroscopic bulk density **remains practically constant**.
* **Equilibrium concentration:**
  $$n_F = \sqrt{N N_i} \exp\left(-\frac{\Delta H_F}{2RT}\right)$$
  where $N$ is the number of regular sites and $N_i$ is the number of available interstitial sites.

---

## 📊 3. Official Defect Formation Enthalpies (Smart and Moore)

In any real ionic crystal, $\Delta H_s \neq \Delta H_F$. **The predominant defect is always the one with the lowest formation enthalpy $\Delta H$** [Slides 16-17]:

| Compound | Dominant Defect Type | Formation Enthalpy ($\Delta H$) | Concentration at $300\text{ K}$ | Concentration at $1000\text{ K}$ |
| :--- | :--- | :--- | :--- | :--- |
| **$\text{NaCl}$** | **Schottky** | $3.69 \times 10^{-19}\text{ J}$ ($2.30\text{ eV}$) | $n_s = 2.64 \times 10^{4}\text{ vac/mol}$ | $n_s = 9.38 \times 10^{17}\text{ vac/mol}$ |
| **$\text{MgO}$** | **Schottky** | $10.57 \times 10^{-19}\text{ J}$ ($6.60\text{ eV}$) | $n_s = 2.12 \times 10^{-32}\text{ vac/mol}$ | $n_s = 1.39 \times 10^{7}\text{ vac/mol}$ |
| **$\text{CaO}$** | **Schottky** | $\approx 9.8 \times 10^{-19}\text{ J}$ | Negligible | Low |
| **$\text{LiF}$** | **Schottky** | $\approx 4.3 \times 10^{-19}\text{ J}$ | Very low | Moderate |
| **$\text{AgCl}$** | **Frenkel (cationic)** | $\approx 2.56 \times 10^{-19}\text{ J}$ ($1.60\text{ eV}$) | Appreciable | High |

> [!NOTE]
> Because the ion charge in $\text{MgO}$ ($\text{Mg}^{2+}, \text{O}^{2-}$) is twice that in $\text{NaCl}$ ($\text{Na}^{+}, \text{Cl}^{-}$), the Coulomb electrostatic attraction is about 4 times larger. Therefore, the Schottky formation enthalpy in $\text{MgO}$ ($10.57 \times 10^{-19}\text{ J}$) is almost three times that in $\text{NaCl}$, making it extraordinarily more difficult to generate thermal vacancies in $\text{MgO}$ [Slide 17].

---
*Bidirectional Links:*
* [[Concept - X-Ray Diffraction and Bragg's Law|⬅️ Previous: X-Ray Diffraction]]
* [[Concept - Substitutional and Interstitial Solid Solutions, Hume-Rothery Rules|Next: Solid Solutions and Hume-Rothery ➡️]]
