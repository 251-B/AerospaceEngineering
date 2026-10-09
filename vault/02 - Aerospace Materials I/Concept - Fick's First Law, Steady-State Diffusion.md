---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 15-17, 35; Problems T3_Diffusion.pdf, Problem 6"
tags:
  - theory
  - fundamental-concept
  - ficks-laws
  - steady-state
  - diffusion-flux
  - membrane-purification
dificultad: medium
prerrequisitos:
  - "[[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]"
---

# 📏 Concept: Fick's First Law — Steady-State Diffusion

> **Main Postulate:** Under **steady-state** conditions, the concentration profile does not change with time ($\partial C / \partial t = 0$), so the **diffusional flux** $J$ is strictly constant over time ($\partial J / \partial t = 0$) [Slides 15-16].  
> The net flux of matter is directly proportional to the spatial concentration gradient and moves in the direction opposite to that gradient [Slide 16].

---

## 🌊 1. Definition of the Diffusional Flux ($J$)

The diffusional flux or flux density ($J$) quantifies the rate at which atoms or mass cross a plane of unit area perpendicular to the diffusion direction per unit time [Slide 15]:

$$J = \frac{M}{A \cdot t} = \frac{\text{moles (or mass) diffusing}}{\text{area} \times \text{time}}$$

### Units in SI and in Engineering:
* In molar units: $\left[\frac{\text{mol}}{\text{m}^2\cdot\text{s}}\right]$ or $\left[\frac{\text{mol}}{\text{cm}^2\cdot\text{s}}\right]$
* In mass units: $\left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right]$
* In atomic units: $\left[\frac{\text{atoms}}{\text{m}^2\cdot\text{s}}\right]$ or $\left[\frac{\text{atoms}}{\text{cm}^2\cdot\text{s}}\right]$

---

## ⚖️ 2. Mathematical Formulation of Fick's First Law

For a one-dimensional system along the $x$ axis, Adolf Fick (1855) formulated the fundamental constitutive relation [Slide 16]:

$$J = -D \frac{\partial C}{\partial x}$$

Under purely steady-state conditions through a flat wall or membrane of thickness $\Delta x = x_2 - x_1$, the concentration gradient is constant and linear [Slides 16-17]:

$$J = -D \frac{\Delta C}{\Delta x} = -D \left(\frac{C_2 - C_1}{x_2 - x_1}\right) = D \left(\frac{C_{\text{high}} - C_{\text{low}}}{\Delta x}\right)$$

### Physical Meaning of the Variables:
* $J$: Diffusional flux ($\text{kg}/\text{m}^2\cdot\text{s}$ or $\text{mol}/\text{m}^2\cdot\text{s}$).
* $D$: **Diffusivity** or diffusion coefficient of the solute in the matrix ($\text{m}^2/\text{s}$ or $\text{cm}^2/\text{s}$).
* $\frac{\Delta C}{\Delta x}$: **Concentration gradient** ($\text{kg}/\text{m}^4$ or $\text{mol}/\text{m}^4$).
* **Negative Sign:** Indicates that the net mass transport occurs spontaneously from regions of high concentration to regions of low concentration (in the direction of decreasing gradient, "downhill" in chemical potential) [Slide 16].

---

## 🔬 3. Linear Concentration Profile Across Membranes

When two media with constant chemical concentrations $C_{\text{ext}}$ and $C_{\text{int}}$ ($C_{\text{ext}} > C_{\text{int}}$) are maintained on both sides of a flat membrane or metal plate of thickness $\Delta x$, the system reaches a stable steady state [Slide 17]:

$$\frac{\partial C}{\partial t} = 0 \iff \frac{\partial J}{\partial x} = 0 \implies \frac{d^2 C}{dx^2} = 0$$

Integrating twice with respect to $x$:
$$C(x) = C_{\text{ext}} - \left(\frac{C_{\text{ext}} - C_{\text{int}}}{\Delta x}\right) x$$

The spatial concentration profile is strictly a **decreasing straight line**, and the flux $J$ remains invariant across any transverse plane along the thickness of the membrane [Slide 17].

---

## 🚀 4. Aerospace Application: $\text{H}_2$ Purification with a Palladium ($\text{Pd}$) Membrane

A fundamental industrial and aerospace application of Fick's first law is the purification of hydrogen gas for space fuel cells and high-purity chemical reactors [Slide 35]:

* Diatomic hydrogen gas ($\text{H}_2$) is adsorbed on the high-pressure face of a pure Palladium ($\text{Pd}$) sheet, dissociates into $\text{H}$ atoms and diffuses interstitially through the FCC lattice of $\text{Pd}$ toward the low-pressure face, where it recombines into ultrapure $\text{H}_2$ gas.
* If the membrane area is $A$ and the required mass purification rate is $\dot{m} = M/t$:
  $$J = \frac{\dot{m}}{A}$$
* Equating with Fick's First Law:
  $$\frac{\dot{m}}{A} = D \frac{C_{\text{high}} - C_{\text{low}}}{\Delta x} \implies \Delta x = \frac{D \cdot A \cdot (C_{\text{high}} - C_{\text{low}})}{\dot{m}}$$

*(See the detailed numerical solution in [[Problem - T3-06 Hydrogen Purification with a Palladium Membrane]]).*

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC of Topic 3)
* [[Concept - Diffusion Mechanisms, Vacancies and Interstitials]]
* [[Concept - Fick's Second Law, Non-Steady-State Diffusion and the Error Function]]
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Problem - T3-04 Ionic Transport of Nickel through an MgO Plate]]
* [[Problem - T3-06 Hydrogen Purification with a Palladium Membrane]]
