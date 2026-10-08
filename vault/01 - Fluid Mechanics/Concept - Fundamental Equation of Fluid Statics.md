---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Statics"
tags:
  - theory
  - statics
  - pressure
  - isa-atmosphere
dificultad: medium
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concept - Continuum Hypothesis and Thermophysical Properties|Continuum]]"
---

# 📖 Fundamental Equation of Fluid Statics

> **Rest condition:** In a fluid at rest ($\vec{v} = 0$), there are no velocity gradients $\implies \tau_{ij} = 0$. Therefore, **there are no shear stresses**; the state of stress is purely normal and isotropic (scalar pressure $p$).

---

## 🔍 1. Rigorous Derivation of the Differential Equation

Consider a differential cubic fluid element with edges $dx, dy, dz$ at rest under a gravitational body field $\vec{g} = (0, 0, -g)$:

### 1.1 Surface Pressure Forces
On the faces perpendicular to the $z$ axis:
* Lower face ($z$): $+ p \cdot dx dy \cdot \vec{k}$
* Upper face ($z + dz$): $-\left(p + \frac{\partial p}{\partial z} dz\right) \cdot dx dy \cdot \vec{k}$
* Net surface force in $z$:
  $$ dF_{s,z} = -\frac{\partial p}{\partial z} dx dy dz $$

Generalising to the three vector directions:
$$ d\vec{F}_s = -\nabla p \cdot dV $$

### 1.2 Volumetric Body Forces
$$ d\vec{F}_m = \rho \vec{g} \cdot dV $$

### 1.3 Static Equilibrium Condition ($\sum \vec{F} = 0$)
$$ -\nabla p \cdot dV + \rho \vec{g} \cdot dV = 0 $$

Dividing by the volume $dV$:
$$ \mathbf{\nabla p = \rho \vec{g}} $$

In Cartesian components with the $z$ axis vertical pointing upwards:
$$ \frac{\partial p}{\partial x} = 0, \quad \frac{\partial p}{\partial y} = 0, \quad \mathbf{\frac{dp}{dz} = -\rho g} $$

---

## 📐 2. Immediate Physical Consequences

1. **Isobaric Surfaces ($p = \text{const}$):**
   $$ dp = \nabla p \cdot d\vec{r} = \rho \vec{g} \cdot d\vec{r} = 0 \implies \vec{g} \cdot d\vec{r} = 0 $$
   *Surfaces of equal pressure are always perpendicular to the local gravity vector $\vec{g}$ (that is, horizontal in a uniform gravitational field).*
2. **Pascal's Principle:**
   Any pressure increment applied at a point of an incompressible fluid at rest is transmitted undiminished to all points of the fluid.

---

## 🚀 3. Integration for Incompressible Fluids ($\rho = \text{const}$)

$$ \int_{p_1}^{p_2} dp = -\rho g \int_{z_1}^{z_2} dz \implies p_2 - p_1 = -\rho g (z_2 - z_1) $$

Defining the depth $h = z_1 - z_2$ measured from the free surface at atmospheric pressure $p_{\text{atm}}$:
$$ \mathbf{p(h) = p_{\text{atm}} + \rho g h} $$

* **Gauge (relative) pressure:** $p_{\text{rel}} = p - p_{\text{atm}} = \rho g h$.
* **Absolute pressure:** $p_{\text{abs}} = p_{\text{atm}} + p_{\text{rel}}$.

---

## ✈️ 4. International Standard Atmosphere (ISA) — Tropospheric Model

In the atmosphere, air is an ideal gas ($p = \rho R T$), so the density varies with altitude:
$$ \frac{dp}{dz} = -\rho g = -\frac{p}{RT} g \implies \frac{dp}{p} = -\frac{g}{R T(z)} dz $$

In the **Troposphere** (from $z = 0$ to $11\,000\text{ m}$), the temperature decreases linearly with a thermal gradient (lapse rate) $\alpha = 6.5\times 10^{-3}\text{ K/m}$:
$$ T(z) = T_0 - \alpha z \quad (T_0 = 288.15\text{ K}) $$

### Integration:
$$ \ln\left(\frac{p}{p_0}\right) = -\frac{g}{R} \int_0^z \frac{dz}{T_0 - \alpha z} = \frac{g}{\alpha R} \ln\left(1 - \frac{\alpha z}{T_0}\right) $$

$$ \mathbf{p(z) = p_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R}}} $$

With the standard values:
* $ \frac{g}{\alpha R} = \frac{9.80665}{0.0065 \times 287.05} \approx 5.25588 $
* For the density:
  $$ \rho(z) = \rho_0 \left(1 - \frac{\alpha z}{T_0}\right)^{\frac{g}{\alpha R} - 1} = \rho_0 \left(1 - \frac{\alpha z}{T_0}\right)^{4.256} $$

---

## ⚠️ 5. Rigid-Body Acceleration Cases (Apparent Gravity)
If a fluid tank moves with a constant linear acceleration $\vec{a}$, the fluid does not deform after an initial transient:
$$ \nabla p = \rho (\vec{g} - \vec{a}) = \rho \vec{g}_{\text{effective}} $$
The isobars tilt by an angle $\theta$ with respect to the horizontal:
$$ \tan\theta = \frac{a_x}{g + a_z} $$

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Concept - Manometry and Pressure Measurement|Next: Manometry and Pressure Calculation]]
* [[01 - Fluid Mechanics/Concept - Forces on Submerged Surfaces and Center of Pressure|Hydrostatic Forces]]
