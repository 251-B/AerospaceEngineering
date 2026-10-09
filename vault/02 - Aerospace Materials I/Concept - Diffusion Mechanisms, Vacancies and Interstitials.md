---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 2-13"
tags:
  - theory
  - fundamental-concept
  - diffusion
  - vacancies
  - interstitials
  - activation-energy
  - hume-rothery
dificultad: medium
prerrequisitos:
  - "[[Concept - Point Defects, Thermal Vacancies, Schottky and Frenkel]]"
  - "[[Concept - Tetrahedral and Octahedral Interstitial Sites]]"
---

# ⚛️ Concept: Atomic Diffusion Mechanisms — Vacancies and Interstitials

> **Fundamental Definition:** **Diffusion** in the solid state is the phenomenon of mass transport through the thermally activated motion of atoms, ions or molecules through the crystal lattice [Slide 2].  
> **Driving Force:** The chemical potential gradient or **composition gradient** ($\nabla C$). Net diffusion occurs spontaneously in the direction that homogenizes the concentration, maximizing the entropy of the system [Slide 2].

---

## 🔬 1. Necessary Conditions for Diffusion in Solids

For an atom to execute a diffusional jump from its equilibrium position to an adjacent one, two physical conditions must be satisfied simultaneously [Slides 4-5]:

1. **Adjacent Vacant Site (*Empty Site*):** There must be an unoccupied lattice site (a vacancy or a free interstitial site) immediately adjacent to the migrating species.
2. **Sufficient Thermal Energy ($E_{\text{thermal}} \ge E_a$):** The atom must possess the **activation energy** ($E_a$) needed to temporarily distort the bonds of the neighboring atoms and overcome the saddle-point potential barrier between equilibrium positions [Slides 4, 6].

$$\uparrow T \implies \uparrow \text{Thermal vibration amplitude} \implies \uparrow \text{Jump probability} \implies \uparrow \text{Diffusion}$$

The macroscopically observed diffusivity obeys an Arrhenius-type dependence [Slide 5]:
$$D = D_0 \exp\left(-\frac{E_a}{RT}\right)$$

---

## 🔘 2. Vacancy (or Substitutional) Diffusion

In substitutional alloys and in pure metals, the atoms of the crystal lattice have comparable atomic sizes. The only geometrically possible mechanism consists of the exchange of position between an atom and a neighboring **vacancy** [Slides 6-7].

### 2.1 Self-Diffusion vs Interdiffusion
* **Self-diffusion:** Occurs in pure metals when identical atoms exchange sites with vacancies [Slide 7]. It does not produce a net change in the macroscopic chemical composition, but it is demonstrated experimentally using isotopic radioactive tracers (e.g. $^{60}\text{Co}$ or $^{64}\text{Cu}$).
* **Interdiffusion (or chemical diffusion):** Occurs in substitutional solid solutions or diffusion couples (e.g. the copper-nickel diffusion couple, $\text{Cu}-\text{Ni}$) [Slides 10-12].
  * Both metals strictly satisfy the **Hume-Rothery rules** [Slide 12]:
    1. Same crystal structure: both are FCC ($\text{Cu}$ and $\text{Ni}$).
    2. Minimal atomic radius difference: $R_{\text{Cu}} = 128\text{ pm}$, $R_{\text{Ni}} = 124\text{ pm}$ ($\Delta R \approx 3.1\% \ll 15\%$).
    3. Nearly identical electronegativity: $\chi_{\text{Cu}} \approx 1.90$, $\chi_{\text{Ni}} \approx 1.91$.
    4. Same usual valence ($+2$).
  * The net flow of atoms produces a gradual, continuous Cu-Ni solid solution (the two metals are completely miscible, so no intermetallic compound forms in this couple). Interdiffusion in general can form alloys or intermetallics in other couples [Slide 10], and it is the key basis of **diffusion bonding** [Slides 10, 33]. *(Erratum: an earlier version attributed intermetallic compounds to the Cu-Ni couple.)*

### 2.2 Thermodynamics of the Self-Diffusion Activation Energy
For a vacancy jump to occur, the vacancy must first be created in the lattice and then the neighboring atom must migrate into it. Therefore, the total self-diffusion activation energy is the sum of two terms [Slide 8]:

$$E_{\text{self}} = E_v + E_m = \Delta H_v + \Delta H_m$$

* $\Delta H_v$: Energy needed to **form** one mole of thermal vacancies in the crystal.
* $\Delta H_m$: Energy needed to **move** the atom through the lattice constriction into the vacancy.

### 2.3 Direct Correlation between $E_a$ and the Melting Temperature ($T_m$)
Since both the formation and the motion of vacancies involve breaking interatomic bonds, there is a nearly linear correlation between the cohesive bond energy, the melting temperature $T_m$ and the diffusion activation energy [Slides 8-9]:

$$\uparrow T_{\text{melting}} \implies \uparrow E_{\text{bond}} \implies \uparrow E_a$$

| Metal | $T_m$ ($^\circ\text{C}$) | Crystal Structure | $E_a$ ($\text{kJ/mol}$) | $E_a$ ($\text{kcal/mol}$) |
| :--- | :---: | :---: | :---: | :---: |
| **Zinc ($\text{Zn}$)** | 419 | HCP | 91.6 | 21.9 |
| **Aluminum ($\text{Al}$)** | 660 | FCC | 165.0 | 39.5 |
| **Copper ($\text{Cu}$)** | 1083 | FCC | 196.0 | 46.9 |
| **Nickel ($\text{Ni}$)** | 1452 | FCC | 293.0 | 70.1 |
| **Alpha iron ($\alpha\text{-Fe}$)** | 1530 | BCC | 240.0 | 57.5 |
| **Molybdenum ($\text{Mo}$)** | 2600 | BCC | 460.0 | 110.0 |

*Data taken directly from Session 5 Slide 9.*

---

## ⚡ 3. Interstitial Diffusion

Interstitial diffusion describes the migration of atomic solutes of small relative size with respect to the host metallic matrix (typically $\text{C}$, $\text{H}$, $\text{N}$, $\text{O}$, $\text{B}$) by jumping directly from one interstitial position to an adjacent one [Slide 13].

### Distinctive Characteristics:
1. **Conservation of the Host Lattice:** Interstitial atoms move **without permanently displacing** any matrix atom [Slide 13].
2. **Abundance of Free Sites:** In any metallic crystal lattice, the vast majority of interstitial sites (octahedral and tetrahedral) are empty. The geometric probability of finding an adjacent free site is practically 1, unlike the substitutional mechanism where the vacancy concentration is minuscule ($n_v/N \sim 10^{-4}$ at high temperature).
3. **Lower Energy Barrier ($E_i \ll E_v$):** No energy is required to form a vacancy ($\Delta H_v = 0$). Only the local elastic strain energy is needed for the small solute to slip between the matrix atoms [Slide 13].
4. **Extraordinarily Faster Kinetics:** The interstitial diffusivity is much higher than the vacancy diffusivity at the same temperature [Slides 13, 24]; the slide's own example (below) gives about 5 orders of magnitude ($1.5\times10^5$). *(Erratum: an earlier version quoted a general range of 4 to 8 orders of magnitude, which is not stated in the slides.)*

### Critical Comparison in Steels at $1000^\circ\text{C}$ ($\gamma\text{-Fe}$ FCC) [Slide 24]:
* Interstitial carbon in austenite:
  $$D_{\text{C in } \gamma\text{-Fe}} (1000^\circ\text{C}) = 3 \times 10^{-11}\text{ m}^2/\text{s}$$
* Self-diffusion of iron by vacancies in austenite:
  $$D_{\text{Fe in } \gamma\text{-Fe}} (1000^\circ\text{C}) = 2 \times 10^{-16}\text{ m}^2/\text{s}$$
* **Acceleration Factor:**
  $$\frac{D_{\text{interstitial}}}{D_{\text{vacancy}}} = \frac{3 \times 10^{-11}}{2 \times 10^{-16}} = 1.5 \times 10^5 \quad (\mathbf{150\,000\text{ times faster}})$$

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC of Topic 3)
* [[Concept - Fick's First Law, Steady-State Diffusion]]
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Concept - Carburizing and Industrial Applications of Diffusion]]
