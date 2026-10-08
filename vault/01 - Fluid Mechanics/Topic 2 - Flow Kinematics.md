---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 2, pp. 9-24"
  - "slides_Chapters1-2.pdf, Slides 2.0 to 2.24 and Figures 3.8 to 3.16"
tags:
  - moc-topic
  - fluid-mechanics
  - kinematics
  - second-year
dificultad: high
---

# 🌊 Topic 2: Flow Kinematics

> **Topic objective:** Describe the geometry and kinematics of fluid motion without regard to the forces that originate it. It introduces orthogonal coordinate systems and their differential operators, the fundamental distinction between Lagrangian and Eulerian descriptions, the characteristic lines of the flow (pathlines, streamlines, streaklines), the material derivative, the acceleration field, the concepts of vorticity, circulation and velocity potential, the convective flux, the two-dimensional stream function ($\psi$), and the decomposition of the relative motion into translation, rigid rotation ($\bar{\bar{T}}_r$) and pure deformation ($\bar{\bar{T}}_d$).

---

## 📑 Table of Contents of Chapter 2

1. [[01 - Fluid Mechanics/Concept - Curvilinear Coordinates and Differential Operators|1. Orthogonal Curvilinear Coordinates and Differential Operators]]
   * Cartesian, cylindrical and spherical: scale factors $(h_1, h_2, h_3)$ and differential elements $d\vec{x}$.
   * Tensor algebra: dyadic product $\vec{a}\vec{b}$, contraction $\bar{\bar{A}}:\bar{\bar{B}}$, tensor product and vector-tensor cross product $\vec{a}\wedge\bar{\bar{A}}$.
   * General formulas for the gradient $\nabla\Phi$, Laplacian $\nabla^2\Phi$, divergence $\nabla\cdot\vec{a}$, curl $\nabla\wedge\vec{a}$, vector gradient $(\nabla\vec{a})_{ij}$ and tensor divergence $(\nabla\cdot\bar{\bar{A}})_i$.
   * General Gauss theorem: $\int_\Sigma (\vec{n}\circ\phi)d\sigma = \int_V (\nabla\circ\phi)dV$.

2. [[01 - Fluid Mechanics/Concept - Eulerian vs Lagrangian Description and Flow Lines|2. Eulerian and Lagrangian Descriptions and Characteristic Lines]]
   * Lagrangian approach: trajectories $\vec{x} = \vec{x}_T(\vec{x}_0, t)$, velocity and acceleration by direct differentiation.
   * Eulerian approach: continuous vector field $\vec{v}(\vec{x}, t)$.
   * Preliminary concepts: uniform flow ($\vec{v}=\vec{v}(t)$), steady flow ($\vec{v}=\vec{v}(\vec{x})$), observer relativity and stagnation points ($\vec{v}=0$).
   * Pathlines: integration of $d\vec{x}/dt = \vec{v}(\vec{x}, t)$ and elimination of $t$.
   * Fluid lines, fluid surfaces ($Df/Dt = 0$) and fluid volumes (mass conservation).
   * Streamlines: tangent to the instantaneous velocity vector ($dx/v_x = dy/v_y = dz/v_z$).
   * Stream surfaces and stream tubes. Condition for the coincidence of pathlines and streamlines in steady flows.

3. [[01 - Fluid Mechanics/Concept - Material Derivative and Fluid Acceleration|3. Material Derivative and Acceleration Field]]
   * Mathematical derivation of the material operator $D\phi/Dt = \partial\phi/\partial t + \vec{v}\cdot\nabla\phi$ (local term + convective term).
   * Acceleration of a fluid particle: $\vec{a} = D\vec{v}/Dt = \partial\vec{v}/\partial t + \vec{v}\cdot(\nabla\vec{v})$.
   * Universal intrinsic expression: $\vec{a} = \partial\vec{v}/\partial t + \nabla(|\vec{v}|^2/2) - \vec{v}\wedge(\nabla\wedge\vec{v})$.
   * Components in Cartesian vs curvilinear systems.
   * Acceleration in non-inertial reference frames: translation $\vec{a}_0$, angular acceleration $\dot{\vec{\Omega}}\wedge\vec{x}$, centrifugal $\vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x})$ and Coriolis $2\vec{\Omega}\wedge\vec{v}$.

4. [[01 - Fluid Mechanics/Concept - Vorticity, Circulation and Velocity Potential|4. Vorticity, Circulation and Velocity Potential]]
   * Circulation along a curve: $\Gamma = \int_L \vec{v}\cdot d\vec{l}$.
   * Stokes' theorem and definition of vorticity: $\vec{\omega} = \nabla\wedge\vec{v}$. Physical meaning as circulation per unit area.
   * Irrotational flow ($\vec{\omega} \equiv 0$) and velocity potential: $\vec{v} = \nabla\phi$.
   * Simply connected vs multiply connected domains: non-zero circulation around airfoils and lift generation (Kutta-Joukowski).

5. [[01 - Fluid Mechanics/Concept - Convective Flux and Stream Function|5. Convective Flux and Stream Function ($\psi$)]]
   * Convective transport of extensive quantities per unit volume $\phi$: mass ($\rho\vec{v}$), momentum ($\rho\vec{v}\vec{v}$), energy ($\rho(e+v^2/2)\vec{v}$) and volumetric flow rate $Q = \int_\Sigma \vec{v}\cdot\vec{n}d\sigma$.
   * Divergence of the velocity $\nabla\cdot\vec{v}$ as the volumetric dilatation rate. Incompressibility: $\nabla\cdot\vec{v} = 0$.
   * Fluxes through moving surfaces with relative velocity $(\vec{v} - \vec{v}_c)$.
   * Plane stream function $\psi(x, y)$: $v_x = \partial\psi/\partial y$, $v_y = -\partial\psi/\partial x$. Proof that the isolines $\psi = \text{const}$ are streamlines and that the jump $\Delta\psi = \psi_2 - \psi_1$ equals the flow rate per unit depth.

6. [[01 - Fluid Mechanics/Concept - Deformation, Rotation and the Rate-of-Strain Tensor|6. Kinematics of Deformation: Strain and Rotation Tensors]]
   * Relative motion between two nearby points: $d\vec{v} = d\vec{x}\cdot\nabla\vec{v}$.
   * Helmholtz decomposition: $\nabla\vec{v} = \bar{\bar{T}}_d + \bar{\bar{T}}_r$.
   * Rotation-rate tensor $\bar{\bar{T}}_r$: antisymmetric, linked to the vorticity $d\vec{v}_r = \frac{1}{2}\vec{\omega}\wedge d\vec{x}$.
   * Rate-of-strain tensor $\bar{\bar{T}}_d$: symmetric, diagonal elements (linear extension rates) and off-diagonal elements (half of the angular deformation rate or shear).
   * Principal directions of deformation: eigenvalue problem $\bar{\bar{T}}_d\cdot\vec{n} = \lambda\vec{n}$.
   * Deformation of square and cubic elements: analytical proof of $\frac{1}{V}\frac{dV}{dt} = \nabla\cdot\vec{v} = \text{tr}(\bar{\bar{T}}_d)$.

---

## 📚 Fundamental Equations of the Chapter (Notes.pdf)

$$ \vec{x} = \vec{x}_T(\vec{x}_0, t) \qquad \text{[Eq. 2.10: Trajectory]} $$
$$ \frac{h_1 dx_1}{v_1} = \frac{h_2 dx_2}{v_2} = \frac{h_3 dx_3}{v_3} \qquad \text{[Eq. 2.21: Streamlines]} $$
$$ \frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + \vec{v} \cdot \nabla \phi \qquad \text{[Eq. 2.24: Material Derivative]} $$
$$ \vec{a} = \frac{\partial \vec{v}}{\partial t} + \nabla\left(\frac{|\vec{v}|^2}{2}\right) - \vec{v} \wedge (\nabla \wedge \vec{v}) \qquad \text{[Eq. 2.26: Intrinsic Acceleration]} $$
$$ \Gamma = \oint_L \vec{v} \cdot d\vec{l} = \int_\Sigma (\nabla \wedge \vec{v}) \cdot \vec{n} d\sigma \qquad \text{[Eq. 2.32: Stokes and Vorticity]} $$
$$ v_x = \frac{\partial \psi}{\partial y}, \quad v_y = -\frac{\partial \psi}{\partial x}, \quad Q' = \psi_2 - \psi_1 \qquad \text{[Eqs. 2.41, 2.45: Stream Function]} $$
$$ \nabla \vec{v} = \bar{\bar{T}}_d + \bar{\bar{T}}_r, \quad d\vec{v}_r = \frac{1}{2}\vec{\omega}\wedge d\vec{x}, \quad \nabla \cdot \vec{v} = \text{tr}(\bar{\bar{T}}_d) = \frac{1}{V}\frac{dV}{dt} \qquad \text{[Eqs. 2.47, 2.52, 2.62]} $$

---

## ✏️ Solved Kinematics Problems (Official Exam Sheet)

All the problems of the official kinematics collection developed step by step:
1. [[01 - Fluid Mechanics/Problem - K1 Flow over an Oscillating Porous Wall|Problem K1: Flow over an Oscillating Porous Wall with Suction/Blowing]]
2. [[01 - Fluid Mechanics/Problem - K2 Plane Couette Flow|Problem K2: Plane Couette Flow and Deformation / Rotation Analysis]]
3. [[01 - Fluid Mechanics/Problem - K3 Three-Dimensional Source at the Origin|Problem K3: Point Three-Dimensional Source at the Origin]]
4. [[01 - Fluid Mechanics/Problem - K4 Flow around a Rankine Body|Problem K4: Flow around a Rankine Half-Body]]
5. [[01 - Fluid Mechanics/Problem - K5 Oscillating Plane Dipole|Problem K5: Pulsating / Oscillating Plane Dipole]]
6. [[01 - Fluid Mechanics/Problem - K6 Three-Dimensional Burgers Vortex|Problem K6: Three-Dimensional Burgers Vortex with Axial Stretching]]
7. [[01 - Fluid Mechanics/Problem - K7 Hyperbolic Stagnation Flow|Problem K7: Plane Hyperbolic Stagnation Flow]]
8. [[01 - Fluid Mechanics/Problem - K8 Pulsating Three-Dimensional Potential|Problem K8: Pulsating Three-Dimensional Flow and Spherical Deformation]]
9. [[01 - Fluid Mechanics/Problem - K9 Oscillating Polar Flow|Problem K9: Oscillating Polar Flow and Deformation of a Fluid Line]]
10. [[01 - Fluid Mechanics/Problem - K10 Plane Flow with Exponential Shear|Problem K10: Plane Flow with Exponential Shear and Pure Deformation]]
