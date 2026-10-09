---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 23-27; Problems T3_Diffusion.pdf, Problems 2, 3, 5"
tags:
  - theory
  - fundamental-concept
  - arrhenius
  - activation-energy
  - diffusivity
  - crystal-structure
  - grain-boundary-diffusion
dificultad: medium
prerrequisitos:
  - "[[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]"
---

# 🌡️ Concept: The Arrhenius Equation and Factors Influencing Diffusivity

> **Principle of Thermal Activation:** The diffusivity $D$ is not a universal constant but a transport property that depends strongly on temperature and on the crystallochemical characteristics of the solute-solvent pair [Slide 23]. As temperature rises, the mean kinetic energy of the atoms and the probability that they overcome the jump energy barrier increase exponentially, drastically accelerating the diffusion process [Slide 26].

---

## 📈 1. The Arrhenius Equation for Diffusivity

The thermal dependence of the diffusion coefficient ($D$) follows, with great experimental rigor, the phenomenological law of Svante Arrhenius [Slide 26]:

$$D = D_0 \exp\left(-\frac{E_D}{RT}\right)$$

### Physical Meaning of the Variables:
* $D$: Diffusion coefficient or diffusivity at absolute temperature $T$ ($\text{m}^2/\text{s}$ or $\text{cm}^2/\text{s}$).
* $D_0$: **Pre-exponential frequency factor** ($\text{m}^2/\text{s}$ or $\text{cm}^2/\text{s}$), independent of temperature, determined by the atomic vibration frequency in the lattice ($\nu_0 \sim 10^{13}\text{ s}^{-1}$), the migration entropy factor and the geometric jump distance [Slide 26].
* $E_D$ (or $E_a$): **Diffusion activation energy** ($\text{J/mol}$ or $\text{cal/mol}$), representing the minimum energy needed for one mole of atoms to execute the jump into a vacancy or interstitial site [Slide 26].
* $R$: Universal ideal gas constant ($8.314\text{ J/mol}\cdot\text{K} = 1.987\text{ cal/mol}\cdot\text{K}$).
* $T$: Absolute temperature in Kelvin ($\text{K} = ^\circ\text{C} + 273.15$).

---

## 📉 2. Arrhenius Linearization and the Two-Temperature Formulation

Taking the natural logarithm of both sides of the equation [Slide 26]:

$$\ln D = \ln D_0 - \left(\frac{E_D}{R}\right) \frac{1}{T}$$

This expression has the structure of a straight line $y = y_0 + m x$:
* Ordinate axis ($y$): $\ln D$.
* Abscissa axis ($x$): $\frac{1}{T}$ ($\text{K}^{-1}$).
* Intercept ($y_0$): $\ln D_0$.
* Slope of the line ($m$): $-\frac{E_D}{R} < 0$.

### Two-Temperature Equation:
When the diffusion coefficients $D_1$ and $D_2$ are known at two different temperatures $T_1$ and $T_2$, the activation energy $E_D$ is obtained directly by subtracting the two equations, without needing to know the factor $D_0$ in advance [Problems 2, 3]:

$$\ln\left(\frac{D_2}{D_1}\right) = -\frac{E_D}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{E_D}{R} \left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

Solving for $E_D$:
$$E_D = \frac{R \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}}$$

---

## 🧩 3. Physical and Crystalline Factors That Modulate Diffusivity

The rate and magnitude of $D$ in solids depend on five fundamental factors identified in the experimental literature [Slides 23-27]:

### A) Diffusion Mechanism and Solute Size (Interstitial vs Vacancy) [Slide 24]
* Small atoms ($\text{C}, \text{H}, \text{N}, \text{O}$) diffuse by interstitial jumps with activation energies notably lower than those of lattice atoms.
* **Quantitative example in austenite (FCC $\gamma\text{-Fe}$ at $1000^\circ\text{C}$):**
  $$D(\text{C in } \gamma\text{-Fe}) = 3 \times 10^{-11}\text{ m}^2/\text{s} \quad \text{vs} \quad D(\text{Fe in } \gamma\text{-Fe}) = 2 \times 10^{-16}\text{ m}^2/\text{s}$$
  *Interstitial diffusion of carbon is five orders of magnitude faster ($10^5$) than the self-diffusion of iron.*

### B) Crystal Structure Type of the Matrix (Solvent) [Slide 24]
* **More open** crystal lattices have lower atomic packing factors (APF) and larger free interatomic distances, offering less resistance to atomic jumps.
* The body-centered cubic lattice ($\text{BCC}$, $\text{APF} = 0.68$) is more open than the close-packed face-centered cubic lattice ($\text{FCC}$, $\text{APF} = 0.74$).
* **Comparison of carbon diffusion at $500^\circ\text{C}$ [Slides 23-24]:**
  $$D(\text{C in Fe-}\alpha, \text{BCC}) = 10^{-12}\text{ m}^2/\text{s} \gg D(\text{C in Fe-}\gamma, \text{FCC}) = 5 \times 10^{-15}\text{ m}^2/\text{s}$$
  *Carbon diffuses about 200 times faster in BCC ferrite than in FCC austenite at the same temperature.*

### C) Crystal Defects and Short-Circuit Diffusion [Slide 25]
Regions where the atomic ordering is interrupted contain more free volume and lower bond density, facilitating mass transport:

$$D_{\text{surface}} > D_{\text{grain boundary}} > D_{\text{volume (lattice)}}$$

* **Surface diffusion:** Surface atoms have a lower coordination number and unsaturated bonds; the activation barrier is minimal.
* **Grain boundary diffusion:** A region of lattice mismatch of $2\text{--}5$ atomic diameters. It acts as a high-diffusivity channel.
  * *Example in Silver at $500^\circ\text{C}$ [Slide 23]:* $D(\text{Ag in grain boundary}) = 10^{-11}\text{ m}^2/\text{s}$, whereas $D(\text{Ag in single-crystal lattice}) = 10^{-17}\text{ m}^2/\text{s}$ ($\mathbf{10^6\text{ times higher}}$).
* **Lattice/volume diffusion:** It is the slowest because it requires displacing the perfect three-dimensional crystal lattice.

### D) Solute Concentration [Slide 25]
As the concentration of dissolved solute atoms increases, distortions are generated in the surrounding lattice and solute-solute interactions or local changes in the Gibbs free enthalpy may occur, altering the effective diffusivity $D$.

### E) Temperature and Melting Temperature ($T_m$) [Slides 8-9, 26-27]
* The higher the absolute temperature $T$, the greater the thermal energy and the exponential diffusivity.
* Materials with a higher melting point ($T_m$) have stiffer and stronger atomic bonds (high $E_{\text{bond}}$), which increases their activation energy $E_D$ and decreases their diffusivity at comparable homologous temperatures [Slide 9].

---

## 📊 4. Official UC3M Reference Diffusivity Table

Experimental values compiled in [Session 5 Slide 23]:

| Solute | Solvent (Matrix) | Matrix Structure | $D$ at $500^\circ\text{C}$ ($\text{m}^2/\text{s}$) | $D$ at $1000^\circ\text{C}$ ($\text{m}^2/\text{s}$) |
| :--- | :--- | :---: | :---: | :---: |
| **Carbon** | Iron ($\gamma$) | FCC | $5 \times 10^{-15} \ ^*$ | $3 \times 10^{-11}$ |
| **Carbon** | Iron ($\alpha$) | BCC | $10^{-12}$ | $2 \times 10^{-9} \ ^*$ |
| **Iron** | Iron ($\gamma$) | FCC | $2 \times 10^{-23} \ ^*$ | $2 \times 10^{-16}$ |
| **Iron** | Iron ($\alpha$) | BCC | $10^{-20}$ | $3 \times 10^{-14} \ ^*$ |
| **Nickel** | Iron ($\gamma$) | FCC | $10^{-23}$ | $2 \times 10^{-16} \ ^*$ |
| **Manganese**| Iron ($\gamma$) | FCC | $3 \times 10^{-24} \ ^*$ | $10^{-16}$ |
| **Zinc** | Copper | FCC | $4 \times 10^{-18}$ | $5 \times 10^{-13}$ |
| **Copper** | Aluminum | FCC | $4 \times 10^{-14}$ | — |
| **Copper** | Copper | FCC | $10^{-18}$ | $2 \times 10^{-13}$ |
| **Silver** | Silver (volume) | FCC | $10^{-17}$ | — |
| **Silver** | Silver (grain boundary)| — | $10^{-11}$ | — |
| **Carbon** | Titanium | HCP | $3 \times 10^{-16}$ | $2 \times 10^{-11} \ ^*$ |

*\*Metastable phases extrapolated to that temperature.*

---

## ⚖️ 5. Comparative Summary of Kinetic Factors [Slide 27]

| Diffusion is **FASTER** in: | Diffusion is **SLOWER** in: |
| :--- | :--- |
| • Open crystal structures (BCC) | • Close-packed structures (FCC, ideal HCP) |
| • Lower-density materials | • High-density materials |
| • Materials with a large number of defects (fine grain, dislocations) | • Perfect single-crystal materials (defect-free) |
| • Neutral diffusing species | • Ionically charged diffusing species |
| • Materials with a low melting point ($T_m$) | • Refractory materials with high $T_m$ |
| • High temperatures | • Low temperatures |
| • Small atomic species ($\text{C}, \text{H}, \text{N}$) | • Bulky, heavy atomic species |

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC of Topic 3)
* [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Problem - T3-02 Diffusion of Aluminium in Single-Crystal Silicon]]
* [[Problem - T3-03 Activation Energy and Diffusivity of Carbon in Steel]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
