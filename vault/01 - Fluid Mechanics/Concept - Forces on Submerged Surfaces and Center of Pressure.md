---
materia: Fluid Mechanics
tema: "Topic 1: Fluid Statics"
tags:
  - theory
  - statics
  - center-of-pressure
  - gates
dificultad: high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concept - Fundamental Equation of Fluid Statics|Fundamental Equation of Statics]]"
---

# 📖 Forces on Submerged Surfaces and the Center of Pressure

> **Key principle:** The total hydrostatic force on a plane surface equals the pressure evaluated at the **Center of Gravity (CG)** multiplied by the area. However, its resultant point of application, the **Center of Pressure (CP)**, is **always below** the CG because hydrostatic pressure grows with depth.

---

## 📐 1. Inclined Plane Surfaces

Consider a plane gate of area $A$ submerged in a liquid of density $\rho$, inclined at an angle $\theta$ with respect to the free surface.
* We define the $y$ axis contained in the plane of the gate with origin $y = 0$ at the intersection of the plane with the free surface.
* The vertical depth of any point is $h = y \cdot \sin\theta$.

### 1.1 Magnitude of the Resultant Force ($F_R$)
The gauge pressure at a depth $h$ is $p = \rho g h = \rho g y \sin\theta$:
$$ F_R = \int_A p \, dA = \rho g \sin\theta \int_A y \, dA $$

By definition of the center of gravity (first moment of area $\int_A y \, dA = y_{CG} \cdot A$):
$$ \mathbf{F_R = \rho g \sin\theta \, y_{CG} \cdot A = p_{CG} \cdot A} $$

*The net force is the product of the hydrostatic pressure at the centroid and the total wetted area.*

---

## 🎯 2. Location of the Center of Pressure ($x_{CP}, y_{CP}$)

Applying the principle of moments (the moment of the resultant force must equal the integral of the moments of the elementary pressures):

### 2.1 Coordinate $y_{CP}$ (Along the Inclination)
$$ F_R \cdot y_{CP} = \int_A y \cdot (p \, dA) = \rho g \sin\theta \int_A y^2 \, dA $$
Recalling that $\int_A y^2 \, dA = I_{xx}$ is the second moment of area about the axis of the free surface ($y=0$).

By the **Parallel-Axis (Steiner) Theorem**:
$$ I_{xx} = I_{xx,CG} + A \cdot y_{CG}^2 $$

Substituting $F_R = \rho g \sin\theta \, y_{CG} A$:
$$ (\rho g \sin\theta \, y_{CG} A) \cdot y_{CP} = \rho g \sin\theta \left( I_{xx,CG} + A \, y_{CG}^2 \right) $$

Dividing by $\rho g \sin\theta \, y_{CG} A$:
$$ \mathbf{y_{CP} = y_{CG} + \frac{I_{xx,CG}}{y_{CG} \cdot A}} $$

*Since $I_{xx,CG} > 0$, it always holds strictly that $\mathbf{y_{CP} > y_{CG}}$ (the center of pressure is deeper than the centroid).*

### 2.2 Lateral Coordinate $x_{CP}$
$$ \mathbf{x_{CP} = x_{CG} + \frac{I_{xy,CG}}{y_{CG} \cdot A}} $$
*(If the gate has at least one axis of symmetry perpendicular to $x$, the centroidal product of inertia vanishes: $I_{xy,CG} = 0 \implies x_{CP} = x_{CG}$)*.

---

## 📊 3. Classical Centroidal Moments of Inertia

| Geometry | Area ($A$) | $y_{CG}$ from the base | $I_{xx,CG}$ (horizontal neutral axis) |
| :--- | :--- | :--- | :--- |
| **Rectangle** ($b \times h$) | $b \cdot h$ | $h/2$ | $\frac{b \cdot h^3}{12}$ |
| **Circle** (radius $R$) | $\pi R^2$ | $R$ | $\frac{\pi R^4}{4}$ |
| **Triangle** (base $b$, height $h$) | $\frac{b \cdot h}{2}$ | $h/3$ | $\frac{b \cdot h^3}{36}$ |

---

## 🌊 4. Submerged Curved Surfaces

For curved surfaces (cylindrical, spherical, parabolic dams), direct computation of the vector integral $\int p \, d\vec{A}$ is tedious. The **Component Decomposition Method** is used:

### Horizontal Component ($F_H$):
It equals the hydrostatic force on the **vertical projection ($A_v$)** of the curved surface:
$$ \mathbf{F_H = p_{CG,v} \cdot A_v} $$
Its line of action passes through the center of pressure of that plane projected area.

### Vertical Component ($F_V$):
It equals the **weight of the volume of liquid (real or imaginary)** contained between the curved surface and the free surface of the liquid:
$$ \mathbf{F_V = \rho g \cdot V_{\text{fluid}}} $$
Its line of action passes exactly through the **center of gravity of the liquid volume considered**.

### Resultant and Direction:
$$ F_R = \sqrt{F_H^2 + F_V^2}, \quad \tan\alpha = \frac{F_V}{F_H} $$

---

## 🔗 Practice and Exercises
* [[01 - Fluid Mechanics/Problem - Inclined Submerged Gate with Opening Moment|Worked Problem: Hinged Gate]]
* [[01 - Fluid Mechanics/Concept - Archimedes' Principle and Stability of Floating Bodies|Next: Archimedes' Principle and Floating Bodies]]
