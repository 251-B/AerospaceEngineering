---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - convective-flux
  - stream-function
dificultad: medium
prerrequisitos: []
---

# 🌊 Concept: Convective Flux and the Stream Function ($\psi$)

> **Key idea in one sentence:** The convective flux quantifies the net transport of mass, momentum and energy crossing a surface due to the fluid velocity; for incompressible plane flows ($\nabla \cdot \vec{v} = 0$), the stream function $\psi(x, y)$ reduces the two-dimensional vector field to a scalar whose level curves are exactly the streamlines and whose jumps $\Delta\psi$ measure the circulating volumetric flow rate.

---

## 📦 1. Convective Flux through Surfaces (Notes.pdf, Eqs. 2.35–2.39)

Mass, momentum and energy travel carried by the fluid particles in their motion. To formalise this transport rate in a unified way:

We define $\phi(\vec{x}, t)$ as a generic fluid quantity expressed **per unit volume**. The total amount of that quantity contained in a volume $V$ is $\int_V \phi \, dV$.

### Derivation of the Flux through a Fixed Surface $\Sigma_0$
Consider a fixed oriented surface $\Sigma_0$ with unit normal vector $\vec{n}$. In an infinitesimal interval $dt$, the volume of fluid crossing a differential area element $d\sigma$ is the volume of the parallelepiped with base $d\sigma$ and oblique edge $\vec{v} dt$:

$$ dV_c = (\vec{v} \cdot \vec{n}) \, d\sigma \, dt $$

The amount of the quantity $\phi$ transported through $d\sigma$ during $dt$ is $\phi (\vec{v} \cdot \vec{n}) \, d\sigma \, dt$. Dividing by $dt$ and integrating over the whole surface $\Sigma_0$, the **net convective flux** is defined:

$$ \mathbf{\Phi_{\text{conv}} = \int_{\Sigma_0} \phi \, \vec{v} \cdot \vec{n} \, d\sigma} \qquad \text{[Eq. 2.35]} $$

| Extensive Quantity | Volumetric Density ($\phi$) | Convective Flux Vector / Tensor ($\phi\vec{v}$) | Total Flux through $\Sigma_0$ |
| :--- | :--- | :--- | :--- |
| **Volume** | $\phi = 1$ | $\vec{v}$ (volume flow rate vector) | $Q = \int_{\Sigma_0} \vec{v} \cdot \vec{n} \, d\sigma$ (Volumetric flow rate, Eq. 2.36) |
| **Mass** | $\phi = \rho$ | $\rho\vec{v}$ (mass flux vector) | $\dot{m} = \int_{\Sigma_0} \rho \, \vec{v} \cdot \vec{n} \, d\sigma$ (Mass flow rate) |
| **Momentum** | $\phi = \rho\vec{v}$ | $\rho\vec{v}\vec{v}$ (momentum flux tensor) | $\int_{\Sigma_0} \rho\vec{v} (\vec{v} \cdot \vec{n}) \, d\sigma$ |
| **Total Energy** | $\phi = \rho\left(e + \frac{|\vec{v}|^2}{2}\right)$ | $\rho\left(e + \frac{|\vec{v}|^2}{2}\right)\vec{v}$ (energy flux vector) | $\dot{E} = \int_{\Sigma_0} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) \vec{v} \cdot \vec{n} \, d\sigma$ |

### Gauss's Theorem and the Divergence of the Velocity
If $\Sigma_0$ is a closed surface enclosing a fixed control volume $V_0$:

$$ \oint_{\Sigma_0} \phi \, \vec{v} \cdot \vec{n} \, d\sigma = \int_{V_0} \nabla \cdot (\phi\vec{v}) \, dV \qquad \text{[Eq. 2.37]} $$

In the limit of an infinitesimal differential volume, $\nabla \cdot (\phi\vec{v})$ represents the net rate of loss of the quantity per unit volume due to the outgoing flux.  
In particular, for $\phi = 1$, $\nabla \cdot \vec{v}$ physically represents the **unit volumetric dilatation rate** (net volume leaving the unit volume per unit time). Therefore, for an incompressible fluid or perfect liquid:

$$ \mathbf{\nabla \cdot \vec{v} = 0} \qquad \text{[Eq. 2.38]} $$

### Convective Flux through Moving Surfaces
If the control surface $\Sigma_c(t)$ moves with a velocity $\vec{v}_c(\vec{x}_c, t)$, the net transport depends on the **relative velocity** $(\vec{v} - \vec{v}_c)$ of the fluid particles with respect to the control boundary:

$$ \Phi_{\text{conv}} = \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c) \cdot \vec{n} \, d\sigma \qquad \text{[Eq. 2.39]} $$

---

## 🎯 2. The Stream Function ($\psi$) for Plane Flows (Notes.pdf, Eqs. 2.40–2.45)

For two-dimensional plane flows in the Cartesian $x-y$ plane, the solenoidality condition $\nabla \cdot \vec{v} = 0$ takes the form:

$$ \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = 0 \qquad \text{[Eq. 2.40]} $$

This exact differential relation guarantees the existence of a scalar field $\psi(x, y, t)$, called the **stream function**, defined through the cross derivatives:

$$ \mathbf{v_x = \frac{\partial \psi}{\partial y}}, \qquad \mathbf{v_y = -\frac{\partial \psi}{\partial x}} \qquad \text{[Eq. 2.41]} $$

Substituting directly into the divergence:
$$ \frac{\partial}{\partial x}\left(\frac{\partial \psi}{\partial y}\right) + \frac{\partial}{\partial y}\left(-\frac{\partial \psi}{\partial x}\right) = \frac{\partial^2 \psi}{\partial x \partial y} - \frac{\partial^2 \psi}{\partial y \partial x} \equiv 0 $$
Volume conservation is thus **automatically satisfied** for any function $\psi$.

---

## 📐 3. Fundamental Kinematic Properties of $\psi$

### 1. The Level Curves $\psi(x, y) = \text{constant}$ are Streamlines
Along a level curve where $\psi = \text{const}$, its total differential is identically zero:

$$ d\psi = \frac{\partial \psi}{\partial x} dx + \frac{\partial \psi}{\partial y} dy = -v_y dx + v_x dy = 0 \qquad \text{[Eq. 2.42]} $$

Rearranging the terms algebraically:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \qquad \text{[Eq. 2.43]} $$
which coincides exactly with the differential equation of the streamlines in the two-dimensional plane.

### 2. The Jump $\Delta\psi = \psi_2 - \psi_1$ Represents the Circulating Volumetric Flow Rate
Consider two streamlines characterised by the constant values $\psi_1$ and $\psi_2$, and draw an arbitrary curve joining point 1 on $\psi_1$ with point 2 on $\psi_2$. The increment of the stream function between both points is:

$$ \psi_2 - \psi_1 = \int_1^2 d\psi = \int_1^2 \left( -v_y dx + v_x dy \right) \qquad \text{[Eq. 2.44]} $$

Noting that along the oriented differential curve $(dx, dy)$ the unit normal vector satisfies $\vec{n} dl = (dy, -dx)$, it follows that $-v_y dx + v_x dy = \vec{v} \cdot \vec{n} dl$. Consequently:

$$ \mathbf{\psi_2 - \psi_1 = \int_1^2 \vec{v} \cdot \vec{n} \, dl = Q'} \qquad \text{[Eq. 2.45]} $$

where $Q'$ is the **volumetric flow rate circulating between the two stream surfaces per unit length perpendicular to the plane of motion** $[m^2/s]$.

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Eulerian vs Lagrangian Description and Flow Lines|Concept: Streamlines]]
* [[01 - Fluid Mechanics/Concept - Vorticity, Circulation and Velocity Potential|Concept: Velocity Potential]]
