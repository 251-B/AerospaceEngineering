---
materia: "Aerospace Materials I"
tema: "Topic 3: Diffusion in Solids and Mass Transport"
fuentes: "Session 5 T3  Difussion_2025.pdf, Slides 18-21; Problems T3_Diffusion.pdf, Table and Problems 1, 5"
tags:
  - theory
  - fundamental-concept
  - ficks-laws
  - non-steady-state
  - error-function
  - erf
  - carburization
  - semi-infinite-solid
dificultad: high
prerrequisitos:
  - "[[Concept - Fick's First Law, Steady-State Diffusion]]"
---

# 📉 Concept: Fick's Second Law — Non-Steady-State Diffusion and the Error Function

> **Physical Principle:** In the vast majority of engineering processes and heat treatments (such as surface carburizing of gears and dopant diffusion in semiconductors), the conditions are **non-steady-state or transient**: the solute concentration at any point of the solid varies continuously with time ($\partial C / \partial t \neq 0$) and the diffusional flux depends on both position and time ($J = J(x, t)$) [Slides 18-19].

---

## 📐 1. Derivation and Fundamental Differential Equation

Consider a differential volume element of cross-section $A$ and length $\Delta x$. The rate of solute accumulation in the elementary volume is given by the mass-conservation balance:

$$\text{Accumulation} = \text{Input} - \text{Output}$$
$$A \cdot \Delta x \cdot \frac{\partial C_x}{\partial t} = A \cdot J(x) - A \cdot J(x + \Delta x)$$

Dividing by the volume $A \cdot \Delta x$ and taking the limit as $\Delta x \to 0$:
$$\frac{\partial C_x}{\partial t} = -\frac{\partial J}{\partial x}$$

Substituting the diffusional flux given by Fick's First Law ($J = -D \frac{\partial C_x}{\partial x}$):
$$\frac{\partial C_x}{\partial t} = \frac{\partial}{\partial x}\left( D \frac{\partial C_x}{\partial x} \right) \quad \text{[Slide 18]}$$

### Canonical Hypothesis: $D \neq f(C)$
When the diffusion coefficient $D$ is independent of the local solute concentration (valid for dilute solid solutions where there is no mutual interaction between diffusing atoms), the diffusivity $D$ comes out of the spatial derivative, leading to the **canonical Fick's Second Law** [Slide 19]:

$$\frac{\partial C_x}{\partial t} = D \frac{\partial^2 C_x}{\partial x^2}$$

* $\frac{\partial C_x}{\partial t}$: Rate of change of the composition with time at a depth $x$.
* $D$: Diffusivity of the solute in the matrix ($\text{m}^2/\text{s}$).
* $\frac{\partial^2 C_x}{\partial x^2}$: Curvature, or rate of change of the concentration gradient.

---

## 🏛️ 2. Analytical Solution for a Semi-Infinite Solid

In surface carburizing processes and thermochemical treatments, the solute penetration depth ($\sim 1\text{ mm}$) is negligible compared with the thickness of the part (gear, shaft or sheet), so the geometry is modeled with extraordinary accuracy as a **semi-infinite solid** ($0 \le x < \infty$) [Slide 20].

### Official Initial and Boundary Conditions [Slides 20-21]:
1. **Initial condition ($t = 0$):** The solid has a homogeneous initial solute concentration $C_0$ throughout its depth:
   $$C(x, 0) = C_0 \quad \text{for } 0 \le x \le \infty$$
2. **Surface boundary condition ($t > 0$):** The surface ($x = 0$) is instantaneously brought into contact with a solute-rich gaseous atmosphere, fixing a constant surface concentration $C_s$:
   $$C(0, t) = C_s \quad \text{for } t > 0$$
3. **Boundary condition at infinity ($t > 0$):** In the deep core of the solid, the concentration remains unchanged:
   $$C(\infty, t) = C_0 \quad \text{for } t > 0$$

### Solution in Terms of the Gaussian Error Function ($\text{erf}$):
Through the similarity transformation $z = \frac{x}{2\sqrt{Dt}}$, the partial differential equation reduces to an ordinary differential equation whose exact solution is [Slides 20-21]:

$$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

Or equivalently:
$$\frac{C_s - C_x}{C_s - C_0} = \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erf}(z)$$

where:
* $C_x$: Solute concentration at a distance $x$ from the surface after a time $t$.
* $C_s$: Surface solute concentration imposed by the surrounding medium ($x = 0$).
* $C_0$: Uniform initial solute concentration in the material.
* $x$: Perpendicular distance from the surface into the interior of the solid ($\text{m}$).
* $t$: Elapsed diffusion time ($\text{s}$).
* $z = \frac{x}{2\sqrt{Dt}}$: Dimensionless similarity variable.

---

## 📊 3. The Gaussian Error Function ($\text{erf}$) and Its Properties

The Gaussian error function is formally defined as the normalized integral of a Gaussian bell curve [Slide 20]:

$$\text{erf}(z) \equiv \frac{2}{\sqrt{\pi}} \int_0^z e^{-\xi^2} d\xi$$

### Essential Mathematical Properties:
1. $\text{erf}(0) = 0 \implies \frac{C_x - C_0}{C_s - C_0} = 1 \implies C_x(0, t) = C_s$ (consistency at the surface).
2. $\text{erf}(\infty) = 1 \implies \frac{C_x - C_0}{C_s - C_0} = 0 \implies C_x(\infty, t) = C_0$ (consistency at infinity).
3. Odd (antisymmetric) symmetry: $\text{erf}(-z) = -\text{erf}(z)$.
4. Complementary error function: $\text{erfc}(z) \equiv 1 - \text{erf}(z)$.

---

## 📋 4. Official Table of $\text{erf}(z)$ Values and Linear Interpolation

The complete **official UC3M table** is transcribed below [Session 5 Slide 21; Problems T3_Diffusion.pdf]:

| $z$ | $\text{erf}(z)$ | $z$ | $\text{erf}(z)$ |
| :---: | :---: | :---: | :---: |
| **0.00** | 0.0000 | **0.70** | 0.6778 |
| **0.01** | 0.0113 | **0.75** | 0.7112 |
| **0.02** | 0.0226 | **0.80** | 0.7421 |
| **0.03** | 0.0338 | **0.85** | 0.7707 |
| **0.04** | 0.0451 | **0.90** | 0.7969 |
| **0.05** | 0.0564 | **0.95** | 0.8209 |
| **0.10** | 0.1125 | **1.00** | 0.8427 |
| **0.15** | 0.1680 | **1.10** | 0.8802 |
| **0.20** | 0.2227 | **1.20** | 0.9103 |
| **0.25** | 0.2763 | **1.30** | 0.9340 |
| **0.30** | 0.3286 | **1.40** | 0.9523 |
| **0.35** | 0.3794 | **1.50** | 0.9661 |
| **0.40** | 0.4284 | **1.60** | 0.9763 |
| **0.45** | 0.4755 | **1.70** | 0.9838 |
| **0.50** | 0.5205 | **1.80** | 0.9891 |
| **0.55** | 0.5633 | **1.90** | 0.9928 |
| **0.60** | 0.6039 | **2.00** | 0.9953 |
| **0.65** | 0.6420 | | |

### Exact Linear Interpolation Algorithm:
Given a target value of the error function $\text{erf}(z)$ lying between two adjacent tabulated values $\text{erf}(z_1)$ and $\text{erf}(z_2)$ (with $z_1 \le z \le z_2$):

$$\frac{z - z_1}{z_2 - z_1} = \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)}$$

Solving for the dimensionless argument $z$:
$$z = z_1 + \left[ \frac{\text{erf}(z) - \text{erf}(z_1)}{\text{erf}(z_2) - \text{erf}(z_1)} \right] (z_2 - z_1)$$

From $z$, the required treatment time or the penetration depth is obtained immediately through:
$$z = \frac{x}{2\sqrt{Dt}} \implies t = \frac{x^2}{4 z^2 D} \quad \text{or} \quad x = 2 z \sqrt{Dt}$$

---

## 🔗 Related Links
* [[Topic 3 - Diffusion in Solids and Mass Transport]] (Master MOC of Topic 3)
* [[Concept - Fick's First Law, Steady-State Diffusion]]
* [[Concept - The Arrhenius Equation and Factors Influencing Diffusivity]]
* [[Concept - Carburizing and Industrial Applications of Diffusion]]
* [[Problem - T3-01 Carburisation of a 1018 Steel Gear]]
* [[Problem - T3-05 Carburising Temperature of 1010 Steel in 8 Hours]]
