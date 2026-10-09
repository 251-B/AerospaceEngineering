---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
origen: "Problems T3_Diffusion.pdf, Problem 6; Session 5 Slide 35"
dificultad: medium
tags:
  - official-problem
  - solved
  - ficks-first-law
  - steady-state
  - palladium-membrane
  - hydrogen-purification
  - mass-flux
---

# ✏️ Problem: T3-06 — Hydrogen Purification with a Palladium Membrane

## 📄 Official Statement
> **6.- Determine the thickness of a plate of $\text{Pd}$ with transversal area of $0.2\text{ m}^2$ so that it can purify $1.73 \times 10^{-3}\text{ kg/h}$ of hydrogen, if the hydrogen concentration at the side of high pressure of the plate is $1.5\text{ kg/m}^3$ and at the side of low pressure is $0.3\text{ kg/m}^3$. The diffusion coefficient of hydrogen in $\text{Pd}$ is $1 \times 10^{-8}\text{ m}^2/\text{s}$.**  
> *(Solution: $5\text{ mm}$)*

---

## 📊 1. Phase 1: Hypotheses and Degrees of Freedom

### Physical Hypotheses:
1. **Pure Steady-State Regime:** Since the partial pressures of gaseous hydrogen on both sides of the palladium ($\text{Pd}$) membrane are kept constant and invariant in time, constant concentrations are established on both faces, giving rise to a steady state in which the diffusive flux $J$ is uniform and constant at any section of the thickness: $\partial C / \partial t = 0$ and $\partial J / \partial t = 0$ [Session 5 Slides 16, 35].
2. **Linear Concentration Gradient:** Since the diffusion coefficient of hydrogen in palladium is independent of solute concentration in this pressure range ($D \neq f(C)$), the concentration profile $C(x)$ across the flat membrane is rigorously a straight line [Slide 17]:
   $$\frac{dC}{dx} = \frac{\Delta C}{\Delta x} = \text{constante}$$
3. **Perpendicular One-Dimensional Flow:** Edge effects at the perimeter of the plate are neglected, assuming a purely one-dimensional macroscopic diffusive flow perpendicular to the cross-sectional area $A$.

### Input Parameters:
* Cross-sectional area of the palladium membrane: $A = 0.2\text{ m}^2$
* Purified mass rate (mass flow rate): $\dot{m} = \frac{M}{t} = 1.73 \times 10^{-3}\text{ kg/h}$ (in the official slide $1.733 \times 10^{-3}\text{ kg/h}$)
* Concentration at the high-pressure face ($x = 0$): $C_{\text{alta}} = C_1 = 1.5\text{ kg/m}^3$
* Concentration at the low-pressure face ($x = \Delta x$): $C_{\text{baja}} = C_2 = 0.3\text{ kg/m}^3$
* Diffusion coefficient of $\text{H}$ in $\text{Pd}$: $D = 1 \times 10^{-8}\text{ m}^2/\text{s}$

---

## 🧠 2. Phase 2: Frames and Change of Basis

The transport rate of hydrogen atoms through the membrane is quantified by the **diffusive flux density** ($J$), formally defined as the mass that diffuses per unit area and per unit time [Session 5 Slide 15]:

$$J = \frac{\text{masa difusora}}{\text{área} \times \text{tiempo}} = \frac{\dot{m}}{A} \quad \left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right]$$

On the other hand, **Fick's First Law** in steady state for a membrane of thickness $\Delta x$ states [Session 5 Slides 16, 35]:

$$J = -D \frac{\Delta C}{\Delta x} = -D \left(\frac{C_2 - C_1}{\Delta x}\right) = D \left(\frac{C_{\text{alta}} - C_{\text{baja}}}{\Delta x}\right)$$

### Solution Strategy:
1. Convert the hourly purification rate $\dot{m}$ to SI units ($\text{kg/s}$).
2. Compute the diffusive flux density $J = \frac{\dot{m}}{A}$.
3. Evaluate the concentration jump $\Delta C = C_{\text{alta}} - C_{\text{baja}}$.
4. Equate both expressions for the flux and solve for the membrane thickness $\Delta x$:
   $$J = D \frac{\Delta C}{\Delta x} \implies \Delta x = \frac{D \cdot \Delta C}{J} = \frac{D \cdot (C_{\text{alta}} - C_{\text{baja}})}{J}$$
5. Express the final result in millimetres ($\text{mm}$).

---

## 🔢 3. Phase 3: Step-by-Step Derivation

### 1. Diffusive Flux Density ($J$):
* Hourly mass flow rate per unit area:
  $$\frac{\dot{m}}{A} = \frac{1.73 \times 10^{-3}\text{ kg/h}}{0.2\text{ m}^2} = 8.65 \times 10^{-3}\text{ kg/m}^2\cdot\text{h}$$
* Conversion to seconds ($1\text{ h} = 3600\text{ s}$):
  $$J = \frac{8.65 \times 10^{-3}\text{ kg/m}^2\cdot\text{h}}{3600\text{ s/h}} \approx \mathbf{2.4028 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}}$$
  *(The worked solution stored in the text layer of Session 5 Slide 35 gives $J = 8.65 \times 10^{-3}\text{ kg/m}^2\cdot\text{h} = 2.4 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}$; the answer box on the rendered slide appears empty).*

---

### 2. Concentration Gradient:
$$\Delta C = C_{\text{alta}} - C_{\text{baja}} = 1.5\text{ kg/m}^3 - 0.3\text{ kg/m}^3 = \mathbf{1.2\text{ kg/m}^3}$$

---

### 3. Solving for the Thickness ($\Delta x$):
Starting from:
$$J = D \frac{\Delta C}{\Delta x}$$

We solve for the thickness $\Delta x$:
$$\Delta x = \frac{D \cdot \Delta C}{J}$$

Substituting the numerical values:
$$\Delta x = \frac{(1.0 \times 10^{-8}\text{ m}^2/\text{s}) \times (1.2\text{ kg/m}^3)}{2.4028 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}}$$
$$\Delta x = \frac{1.2 \times 10^{-8}}{2.4028 \times 10^{-6}}\text{ m} \approx \mathbf{4.994 \times 10^{-3}\text{ m}} \approx \mathbf{5.0 \times 10^{-3}\text{ m}}$$

*(Using the rounded $J = 2.4 \times 10^{-6}\text{ kg/m}^2\cdot\text{s}$ of Slide 35: $\Delta x = \frac{1.2 \times 10^{-8}}{2.4 \times 10^{-6}} = 5.0 \times 10^{-3}\text{ m}$, consistent with the unrounded $4.994 \times 10^{-3}\text{ m}$).*

### Expression in Millimetres:
$$\Delta x = 5.0 \times 10^{-3}\text{ m} \times 1000\text{ mm/m} = \mathbf{5\text{ mm}}$$

---

## 🔍 4. Phase 4: Units and Limits, with Physical and Dimensional Verification

### Dimensional Analysis:
$$[\Delta x] = \frac{[D] \cdot [\Delta C]}{[J]} = \frac{(\text{m}^2/\text{s}) \cdot (\text{kg/m}^3)}{\text{kg}/(\text{m}^2\cdot\text{s})} = \frac{\text{kg}/(\text{m}\cdot\text{s})}{\text{kg}/(\text{m}^2\cdot\text{s})} = \text{m} \quad \checkmark$$

### Physical-Aerospace Interpretation:
1. **Thickness-flux relation:** At fixed concentrations $J \propto 1/\Delta x$ [Slide 16], so **$5\text{ mm}$** is the thickness at which steady-state permeation equals the required purified flow [Slide 35].
2. **Interstitial Kinetics of Hydrogen:** The diffusivity of hydrogen in palladium ($D = 10^{-8}\text{ m}^2/\text{s}$) is exceptionally high compared with other metallic solutes (typically $10^{-12}\text{--}10^{-16}\text{ m}^2/\text{s}$), because the hydrogen atom is the smallest chemical element in the universe and slips through the octahedral and tetrahedral holes of the FCC lattice of $\text{Pd}$ with an extremely low activation energy [Slides 13, 23].
3. **Application:** Slide 35 presents this calculation as the example of $\text{H}_2$ purification through a $\text{Pd}$ layer; no further application is claimed here.

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC for Topic 3)
* [[Concept - Fick's First Law, Steady-State Diffusion]]
* [[Concept - Carburizing and Industrial Applications of Diffusion]]
* [[Problem - T3-04 Ionic Transport of Nickel through an MgO Plate]]
