---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - stress-tensor
  - cauchy-principle
  - body-forces
dificultad: high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]"
---

# 🔬 Concept: Cauchy Stress Tensor and Body Forces

> **Key idea in one sentence:** The mechanical interaction in a fluid is divided into long-range body forces acting on the volume ($\vec{f}_m$) and short-range contact forces acting on the surface; according to Cauchy's Principle, the surface traction vector $\vec{f}_n$ on any orientation $\vec{n}$ is uniquely determined by the projection of a symmetric second-order tensor $\bar{\bar{\tau}}$ ($\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$), whose spatial divergence $\nabla\cdot\bar{\bar{\tau}}$ represents the resultant surface force per unit volume.

---

## 🌌 1. Physical Classification of Forces: Long Range vs Short Range

In macroscopic fluid mechanics, the forces acting on a fluid particle or element are classified according to their intermolecular range of action:

### A. Body or Volumetric Forces ($\vec{f}_m$) — Long Range
Their macroscopic range is infinitely greater than the mean intermolecular distance $d$. They act directly on each mass element $dm = \rho dV$:

$$ d\vec{F}_m = \rho \vec{f}_m(\vec{x}, t) \, dV \qquad \text{[Eq. 3.12]} $$

where $\vec{f}_m$ is the force per unit mass. In the most general case of a **non-inertial reference frame** with translational acceleration $\vec{a}_0(t)$ and instantaneous angular velocity $\vec{\Omega}(t)$, the net body force incorporates the acceleration of gravity and the four fictitious inertial forces:

$$ \mathbf{\vec{f}_m(\vec{x}, t) = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v}} \qquad \text{[Eq. 3.13]} $$

* $\vec{g}$: terrestrial gravity.
* $-\vec{a}_0$: translational inertia of the reference frame.
* $-\frac{d\vec{\Omega}}{dt}\wedge\vec{x}$: azimuthal or Euler inertial force.
* $-\vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x})$: apparent centrifugal force.
* $-2\vec{\Omega}\wedge\vec{v}$: Coriolis force (orthogonal to the relative velocity).

#### Potential of Conservative Body Forces
When the entrainment acceleration $\vec{a}_0$ and the rotation $\vec{\Omega}$ are constant, the gravity, linear translation and centrifugal forces are strictly conservative and derive from a single scalar potential $U(\vec{x})$:

$$ \vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla U \qquad \text{[Eq. 3.14]} $$
$$ U(\vec{x}) = -\vec{g}\cdot\vec{x} + \vec{a}_0\cdot\vec{x} - \frac{1}{2}| \vec{\Omega}\wedge\vec{x} |^2 $$

### B. Surface Forces — Short Range
Their radius of influence is of molecular order ($d \sim 10^{-9}\text{ m}$). They are exerted exclusively through the contact area between adjacent fluid particles or between the fluid and a solid wall.
Given a differential surface element $d\sigma$ with outward-pointing unit normal vector $\vec{n}$, the surface force exerted on the fluid is given by:

$$ d\vec{F}_s = \vec{f}_n(\vec{n}, \vec{x}, t) \, d\sigma \qquad \text{[Eq. 3.15]} $$

where $\vec{f}_n$ is the **traction vector** or surface stress (force per unit area, units of $\text{N/m}^2$ or $\text{Pa}$). By the principle of action and reaction, $\vec{f}_{-n} = -\vec{f}_n$.

---

## 🔺 2. The Cauchy Tetrahedron and Derivation of the Stress Tensor (Notes.pdf, Eqs. 3.16–3.19)

The traction vector $\vec{f}_n$ depends a priori on the position $\vec{x}$, the time $t$ and the angular orientation of the unit vector $\vec{n} = (n_1, n_2, n_3)$. Cauchy showed that this directional dependence is strictly linear.

Consider an infinitesimal fluid element in the shape of a tetrahedron with three orthogonal faces parallel to the Cartesian coordinate planes, of areas $dA_1, dA_2, dA_3$ with outward normals $-\vec{e}_1, -\vec{e}_2, -\vec{e}_3$, and a fourth inclined or oblique face of area $dA$ with arbitrary outward unit normal $\vec{n} = n_1\vec{e}_1 + n_2\vec{e}_2 + n_3\vec{e}_3$.

By elementary geometric projection of the tetrahedron:
$$ dA_1 = n_1 dA, \quad dA_2 = n_2 dA, \quad dA_3 = n_3 dA $$
The volume of the tetrahedron is of order $dV \sim \frac{1}{6} h dA$, where $h$ is the height perpendicular to the oblique face.

Applying Newton's 2nd Law to the fluid tetrahedron:
$$ \rho dV \frac{D\vec{v}}{Dt} = \vec{f}_n dA + \vec{f}_{-e_1} dA_1 + \vec{f}_{-e_2} dA_2 + \vec{f}_{-e_3} dA_3 + \rho \vec{f}_m dV $$
Using $\vec{f}_{-e_i} = -\vec{f}_{e_i} \equiv -\vec{f}_i$:
$$ \vec{f}_n dA - \vec{f}_1 dA_1 - \vec{f}_2 dA_2 - \vec{f}_3 dA_3 = \rho dV \left(\frac{D\vec{v}}{Dt} - \vec{f}_m\right) \qquad \text{[Eq. 3.16]} $$

Taking the limit as the size of the tetrahedron tends to zero ($h \to 0$):
* Surface forces scale with the area of the faces: $\sim \mathcal{O}(dA) \sim \mathcal{O}(h^2)$.
* Inertial and volumetric forces scale with the volume: $\sim \mathcal{O}(dV) \sim \mathcal{O}(h^3)$.

Therefore, upon dividing by $dA$ and taking the limit $h \to 0$, the right-hand side vanishes rigorously:
$$ \vec{f}_n = n_1 \vec{f}_1 + n_2 \vec{f}_2 + n_3 \vec{f}_3 \qquad \text{[Eq. 3.17]} $$

Defining the Cartesian components of the traction vector on the face perpendicular to $\vec{e}_i$ as:
$$ \vec{f}_i = \tau_{i1}\vec{e}_1 + \tau_{i2}\vec{e}_2 + \tau_{i3}\vec{e}_3 = \sum_{j=1}^3 \tau_{ij}\vec{e}_j $$
where $\tau_{ij}$ represents the force per unit area in the direction $\vec{e}_j$ acting on a face whose outward normal points in the direction $\vec{e}_i$.
Grouping in matrix and tensor notation:

$$ \mathbf{\vec{f}_n = \vec{n} \cdot \bar{\bar{\tau}} = \bar{\bar{\tau}} \cdot \vec{n}} \qquad \text{[Eq. 3.17, 3.19]} $$

where the matrix of the **Cauchy Stress Tensor** $\bar{\bar{\tau}}$ is given by:

$$ \bar{\bar{\tau}} = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{21} & \tau_{22} & \tau_{23} \\ \tau_{31} & \tau_{32} & \tau_{33} \end{bmatrix} \qquad \text{[Eq. 3.18]} $$

* **Normal stresses ($\tau_{11}, \tau_{22}, \tau_{33}$):** Stresses perpendicular to the surface (tension or compression).
* **Tangential or shear stresses ($\tau_{ij}$ with $i \neq j$):** Grazing stresses or viscous friction parallel to the face.

---

## ⚖️ 3. Symmetry of the Stress Tensor ($\tau_{ij} = \tau_{ji}$) (Notes.pdf, Eq. 3.19)

Consider a differential cubic fluid element with edges $dx_1, dx_2, dx_3$ centred at $\vec{x}$. Let us evaluate the angular momentum balance about the axis through the center of the cube parallel to $\vec{e}_3$:

$$ I_3 \frac{d\omega_3}{dt} = \sum M_{3, \text{ext}} $$
* The moment of inertia of the cube is $I_3 = \frac{1}{12} \rho (dx_1 dx_2 dx_3)(dx_1^2 + dx_2^2) \sim \mathcal{O}(dx^5)$.
* The moments of the body forces scale with the volume and the arm: $\sim \mathcal{O}(dx^4)$.
* The tangential forces on the lateral faces generate moments with arms $\frac{dx_1}{2}$ and $\frac{dx_2}{2}$:
  * Forces $\tau_{12}(dx_2 dx_3)$ on the $\pm x_1$ faces generate a counterclockwise couple: $\tau_{12}(dx_2 dx_3) dx_1$.
  * Forces $\tau_{21}(dx_1 dx_3)$ on the $\pm x_2$ faces generate a clockwise couple: $-\tau_{21}(dx_1 dx_3) dx_2$.

The moment balance gives:
$$ (\tau_{12} - \tau_{21}) dx_1 dx_2 dx_3 = \mathcal{O}(dx^4) + \mathcal{O}(dx^5) $$
Dividing by the differential volume $dV = dx_1 dx_2 dx_3$ and letting the size tend to zero ($dx \to 0$):

$$ \mathbf{\tau_{12} = \tau_{21}, \quad \tau_{13} = \tau_{31}, \quad \tau_{23} = \tau_{32} \implies \bar{\bar{\tau}} = \bar{\bar{\tau}}^T} \qquad \text{[Eq. 3.19]} $$

The Cauchy stress tensor is **strictly symmetric** in the absence of distributed internal volumetric couples (Boltzmann hypothesis / non-micropolar continuum).

---

## 🧭 4. Principal Stress Directions (Notes.pdf, Eqs. 3.20–3.21)

At any point of the fluid there exist particular orientations $\vec{n}$ for which the resulting surface traction is strictly normal to the face, with the tangential friction stresses vanishing completely ($\vec{f}_n \parallel \vec{n}$):

$$ \bar{\bar{\tau}} \cdot \vec{n} = \lambda \vec{n} \qquad \text{[Eq. 3.20]} $$

The eigenvalue condition requires the characteristic determinant to vanish:

$$ \mathbf{|\bar{\bar{\tau}} - \lambda \bar{\bar{I}}| = 0} \qquad \text{[Eq. 3.21]} $$

Since $\bar{\bar{\tau}}$ is a real symmetric ($3 \times 3$) matrix, the spectral theorem guarantees:
1. There exist three real roots $\lambda_1, \lambda_2, \lambda_3$ called **principal stresses**.
2. The corresponding associated unit directions $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ are **mutually orthogonal**.
3. In the coordinate system of the principal axes, the tensor is diagonalised: $\bar{\bar{\tau}} = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$.

---

## 📦 5. Surface Resultant and Divergence of the Tensor (Notes.pdf, Eqs. 3.22–3.25)

The total surface force exerted on the boundary $\Sigma$ of a fluid volume is given by:

$$ \vec{F}_s = \int_\Sigma \vec{f}_n \, d\sigma = \int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma \qquad \text{[Eq. 3.22]} $$

Applying the general divergence theorem (Gauss's theorem) for second-order tensors:

$$ \mathbf{\int_\Sigma \bar{\bar{\tau}} \cdot \vec{n} \, d\sigma = \int_V (\nabla \cdot \bar{\bar{\tau}}) \, dV} \qquad \text{[Eq. 3.23]} $$

where in Cartesian components, the divergence of the tensor is the vector:
$$ (\nabla \cdot \bar{\bar{\tau}})_i = \sum_{j=1}^3 \frac{\partial \tau_{ji}}{\partial x_j} = \frac{\partial \tau_{1i}}{\partial x_1} + \frac{\partial \tau_{2i}}{\partial x_2} + \frac{\partial \tau_{3i}}{\partial x_3} $$

Evaluating the momentum balance on a differential element $dV$:
$$ \rho dV \frac{D\vec{v}}{Dt} = (\nabla \cdot \bar{\bar{\tau}}) dV + \rho \vec{f}_m dV \qquad \text{[Eq. 3.24]} $$
Dividing by the volume $dV$, the **Cauchy momentum differential equation** is obtained:

$$ \mathbf{\rho \frac{D\vec{v}}{Dt} = \nabla \cdot \bar{\bar{\tau}} + \rho \vec{f}_m} \qquad \text{[Eq. 3.25]} $$

This differential equation governs the dynamic motion of any deformable continuum. To close it mathematically in fluids, it is essential to express $\bar{\bar{\tau}}$ in terms of the kinematic and thermodynamic variables ($\vec{v}, p, T$), which leads to the **Navier-Poisson constitutive equation**.
