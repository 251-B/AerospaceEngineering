---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - material-derivative
  - acceleration
dificultad: medium
prerrequisitos: []
---

# ⚡ Concept: Material Derivative and Acceleration Field

> **Key idea in one sentence:** The material derivative describes the time rate of change of any intensive property (scalar or vector) experienced by a fluid particle as it moves, decomposing into a local temporal contribution (unsteadiness) and a spatial convective contribution (displacement through spatial gradients).

---

## 🎯 1. Physical Foundation and Step-by-Step Derivation

Consider a fluid particle located at position $\vec{x}$ at time $t$, where a scalar intensive property takes the value $\phi(\vec{x}, t)$ (for example, temperature $T$, pressure $p$ or density $\rho$).

An infinitesimal interval $dt$ later, the particle has moved by a vector $d\vec{x} = \vec{v} dt$ and occupies the position $\vec{x} + d\vec{x}$ at time $t + dt$. The new value of the property is $\phi(\vec{x} + d\vec{x}, t + dt)$.

Carrying out a first-order Taylor series expansion about $(\vec{x}, t)$:

$$ d\phi = \phi(\vec{x} + d\vec{x}, t + dt) - \phi(\vec{x}, t) = \frac{\partial \phi}{\partial t} dt + d\vec{x} \cdot \nabla\phi + \mathcal{O}(dt^2) \qquad \text{[Eq. 2.22]} $$

Dividing by the time increment $dt$ and identifying the particle velocity as $\vec{v} = \frac{d\vec{x}}{dt}$:

$$ \frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + \vec{v} \cdot \nabla\phi \qquad \text{[Eq. 2.23]} $$

### Material Derivative Operator (Notes.pdf, Eq. 2.24)
$$ \mathbf{\frac{D()}{Dt} = \underbrace{\frac{\partial()}{\partial t}}_{\text{Local variation}} + \underbrace{\vec{v} \cdot \nabla()}_{\text{Convective variation}}} $$

* **Local term ($\partial/\partial t$):** Measures how fast the property changes at a fixed point in space due to the intrinsic unsteadiness of the flow. It vanishes in steady flows.
* **Convective term ($\vec{v} \cdot \nabla$):** Measures the variation experienced by the particle as it travels from one region to another where the spatial field has a non-zero gradient. It can be very large even in purely steady flows (for example, the heating of air crossing a converging nozzle).

---

## 🏎️ 2. Acceleration of a Fluid Particle (Notes.pdf, Eqs. 2.25–2.27)

Applying the material operator to the velocity vector $\vec{v}(\vec{x}, t)$, the physical acceleration of the fluid particle is:

$$ \vec{a} = \frac{D\vec{v}}{Dt} = \frac{\partial \vec{v}}{\partial t} + \vec{v} \cdot (\nabla\vec{v}) \qquad \text{[Eq. 2.25]} $$

where $\nabla\vec{v}$ is the second-order velocity gradient tensor.

### A. Universal Intrinsic Expression (Independent of the Coordinate System)
Using the vector calculus identity for the scalar product $\vec{v} \cdot (\nabla\vec{v}) = \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v})$, the acceleration is written invariantly as:

$$ \mathbf{\vec{a} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v})} \qquad \text{[Eq. 2.26]} $$

* $\frac{\partial\vec{v}}{\partial t}$: Local acceleration.
* $\nabla(|\vec{v}|^2/2)$: Gradient of the specific kinetic energy.
* $-\vec{v} \wedge (\nabla \wedge \vec{v}) = -\vec{v} \wedge \vec{\omega}$: Lamb acceleration term (cross product with the vorticity $\vec{\omega}$). In irrotational flows ($\vec{\omega} = 0$), this term vanishes identically.

### B. Components in Cartesian Coordinates
In rectangular Cartesian coordinates $(x, y, z)$, $(\nabla\vec{v})_{ij} = \frac{\partial v_j}{\partial x_i}$, and the acceleration reduces to the material derivative of each velocity component:

$$ a_i = \frac{D v_i}{Dt} = \frac{\partial v_i}{\partial t} + \sum_j v_j \frac{\partial v_i}{\partial x_j} = \frac{\partial v_i}{\partial t} + v_x \frac{\partial v_i}{\partial x} + v_y \frac{\partial v_i}{\partial y} + v_z \frac{\partial v_i}{\partial z} \qquad \text{[Eq. 2.27]} $$

> [!WARNING] Crucial Warning for Curvilinear Coordinates
> The scalar equation $a_i = \frac{\partial v_i}{\partial t} + \vec{v} \cdot \nabla v_i$ **is ONLY valid in Cartesian coordinates**.  
> In cylindrical or spherical coordinates, the curvature of the coordinate lines generates centripetal and Coriolis accelerations associated with the spatial derivative of the local basis vectors:
> * In cylindrical coordinates $(r, \theta, z)$:
>   $$ a_r = \frac{\partial v_r}{\partial t} + v_r \frac{\partial v_r}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_r}{\partial \theta} + v_z \frac{\partial v_r}{\partial z} - \mathbf{\frac{v_\theta^2}{r}} $$
>   $$ a_\theta = \frac{\partial v_\theta}{\partial t} + v_r \frac{\partial v_\theta}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_\theta}{\partial \theta} + v_z \frac{\partial v_\theta}{\partial z} + \mathbf{\frac{v_r v_\theta}{r}} $$
>   $$ a_z = \frac{\partial v_z}{\partial t} + v_r \frac{\partial v_z}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_z}{\partial \theta} + v_z \frac{\partial v_z}{\partial z} $$
> The term $-v_\theta^2/r$ is the centripetal acceleration and $+v_r v_\theta/r$ is the azimuthal convective contribution.

---

## 🔄 3. Acceleration in Non-Inertial Reference Frames (Notes.pdf, Eq. 2.28)

When the flow is analysed from a moving reference frame with linear acceleration of its origin $\vec{a}_0(t)$ and rotation angular velocity $\vec{\Omega}(t)$ (for example, turbojet blades or atmospheric and oceanic flows on the rotating Earth):

$$ \mathbf{\vec{a} = \vec{a}_{\text{rel}} + \vec{a}_s} $$

where the apparent inertial acceleration of the system $\vec{a}_s$ is given by:

$$ \vec{a}_s = \vec{a}_0 + \frac{d\vec{\Omega}}{dt} \wedge \vec{x} + \vec{\Omega} \wedge (\vec{\Omega} \wedge \vec{x}) + 2\vec{\Omega} \wedge \vec{v}_{\text{rel}} \qquad \text{[Eq. 2.28]} $$

1. $\vec{a}_0$: Translational acceleration of the origin.
2. $\frac{d\vec{\Omega}}{dt} \wedge \vec{x}$: Angular acceleration of the frame.
3. $\vec{\Omega} \wedge (\vec{\Omega} \wedge \vec{x})$: Apparent centrifugal acceleration (directed perpendicular to the rotation axis, outwards).
4. $2\vec{\Omega} \wedge \vec{v}_{\text{rel}}$: Coriolis acceleration (perpendicular to the relative velocity and to the rotation axis).

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Vorticity, Circulation and Velocity Potential|Concept: Vorticity and Circulation]]
