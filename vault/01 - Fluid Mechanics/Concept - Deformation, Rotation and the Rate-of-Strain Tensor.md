---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - strain-tensor
  - vorticity
  - helmholtz
dificultad: high
prerrequisitos: []
---

# 🔬 Concept: Kinematics of Deformation, Rotation and the Rate-of-Strain Tensor

> **Key idea in one sentence:** The local relative motion of a fluid element with respect to its surroundings decomposes exactly (Helmholtz theorem) into a rigid-body rotation at angular velocity $\frac{1}{2}\vec{\omega}$ described by the antisymmetric tensor $\bar{\bar{T}}_r$, and a pure deformation described by the symmetric tensor $\bar{\bar{T}}_d$, whose trace measures the volumetric dilatation rate ($\nabla \cdot \vec{v}$) and whose off-diagonal terms represent the rate of angular distortion (shear).

---

## 🎯 1. Relative Motion Near a Point (Notes.pdf, Eq. 2.46)

The internal viscous force exerted between neighbouring fluid particles depends exclusively on how fast the fluid deforms.

Consider an infinitesimal fluid line element $d\vec{x}$ whose ends occupy the positions $\vec{x}$ and $\vec{x} + d\vec{x}$ at time $t$. The velocities of both ends differ by a differential amount $d\vec{v}$, expressible to first order through the velocity gradient tensor $\nabla\vec{v}$:

$$ d\vec{v} = d\vec{x} \cdot \nabla\vec{v} \qquad \text{[Eq. 2.46]} $$

After an infinitesimal time $dt$, the ends occupy $\vec{x} + \vec{v} dt$ and $\vec{x} + d\vec{x} + (\vec{v} + d\vec{v}) dt$. The elemental vector evolves according to:
$$ d\vec{x} \longrightarrow d\vec{x} + d\vec{v} \, dt = d\vec{x} + (d\vec{x} \cdot \nabla\vec{v}) \, dt $$
Therefore, besides a global translation $\vec{v} dt$, the element undergoes a spatial distortion governed by $\nabla\vec{v}$.

---

## 📐 2. Helmholtz / Cauchy Decomposition (Notes.pdf, Eqs. 2.47–2.52)

Every second-order tensor can be uniquely decomposed into the sum of a symmetric tensor and an antisymmetric tensor:

$$ \mathbf{\nabla\vec{v} = \underbrace{\frac{1}{2}(\nabla\vec{v} + \nabla\vec{v}^T)}_{\bar{\bar{T}}_d \text{ (symmetric)}} + \underbrace{\frac{1}{2}(\nabla\vec{v} - \nabla\vec{v}^T)}_{\bar{\bar{T}}_r \text{ (antisymmetric)}}} \qquad \text{[Eq. 2.47]} $$

The relative velocity differential decomposes correspondingly into:
$$ d\vec{v} = d\vec{x} \cdot \bar{\bar{T}}_d + d\vec{x} \cdot \bar{\bar{T}}_r = d\vec{v}_d + d\vec{v}_r \qquad \text{[Eq. 2.51]} $$

### A. Rotation-Rate Tensor ($\bar{\bar{T}}_r$) and Rigid-Body Rotation
In Cartesian coordinates, the antisymmetric tensor $\bar{\bar{T}}_r$ is given by:

$$ \bar{\bar{T}}_r = \frac{1}{2} \begin{bmatrix} 0 & \frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2} & \frac{\partial v_3}{\partial x_1} - \frac{\partial v_1}{\partial x_3} \\ -\left(\frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2}\right) & 0 & \frac{\partial v_3}{\partial x_2} - \frac{\partial v_2}{\partial x_3} \\ -\left(\frac{\partial v_3}{\partial x_1} - \frac{\partial v_1}{\partial x_3}\right) & -\left(\frac{\partial v_3}{\partial x_2} - \frac{\partial v_2}{\partial x_3}\right) & 0 \end{bmatrix} \qquad \text{[Eq. 2.49]} $$

Introducing the components of the vorticity vector $\vec{\omega} = \nabla \wedge \vec{v} = (\omega_1, \omega_2, \omega_3)$:
$$ \mathbf{\bar{\bar{T}}_r = \frac{1}{2} \begin{bmatrix} 0 & \omega_3 & -\omega_2 \\ -\omega_3 & 0 & \omega_1 \\ \omega_2 & -\omega_1 & 0 \end{bmatrix}} \qquad \text{[Eq. 2.50]} $$

Acting on the differential element $d\vec{x}$:
$$ d\vec{v}_r = d\vec{x} \cdot \bar{\bar{T}}_r = \frac{1}{2}(\nabla \wedge \vec{v}) \wedge d\vec{x} = \mathbf{\frac{1}{2} \vec{\omega} \wedge d\vec{x}} \qquad \text{[Eq. 2.52]} $$

> [!NOTE] Physical Interpretation of the Rotation
> The contribution $d\vec{v}_r$ represents a **pure rigid-body rotation** of the element $d\vec{x}$ with instantaneous angular velocity:
> $$ \vec{\Omega}_{\text{fluid}} = \frac{1}{2} \vec{\omega} = \frac{1}{2} (\nabla \wedge \vec{v}) $$
> If the deformation tensor $\bar{\bar{T}}_d$ were zero, the element would undergo no distortion at all: its motion would be limited to pure translation and rotation as an undeformable solid.

### B. Rate-of-Strain Tensor ($\bar{\bar{T}}_d$)
The symmetric tensor $\bar{\bar{T}}_d$ (*rate-of-strain tensor*) governs the actual geometric distortion of the fluid:

$$ \mathbf{\bar{\bar{T}}_d = \begin{bmatrix} \frac{\partial v_1}{\partial x_1} & \frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right) & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_1} + \frac{\partial v_1}{\partial x_3}\right) \\ \frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right) & \frac{\partial v_2}{\partial x_2} & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_2} + \frac{\partial v_2}{\partial x_3}\right) \\ \frac{1}{2}\left(\frac{\partial v_3}{\partial x_1} + \frac{\partial v_1}{\partial x_3}\right) & \frac{1}{2}\left(\frac{\partial v_3}{\partial x_2} + \frac{\partial v_2}{\partial x_3}\right) & \frac{\partial v_3}{\partial x_3} \end{bmatrix}} \qquad \text{[Eq. 2.48]} $$

Writing the line element as $d\vec{x} = \vec{n} ds$ (with $|\vec{n}| = 1$ and length $ds$):
$$ d\vec{v}_d = \bar{\bar{T}}_d \cdot \vec{n} \, ds \qquad \text{[Eq. 2.53]} $$
In general, $d\vec{v}_d$ is not aligned with $\vec{n}$, which indicates that the element simultaneously experiences two effects:
1. **Unit extension rate in the direction $\vec{n}$:** Longitudinal projection onto $\vec{n}$:
   $$ \dot{\epsilon}_n = \vec{n} \cdot \bar{\bar{T}}_d \cdot \vec{n} $$
2. **Angular deformation rate (shear):** Component orthogonal to $\vec{n}$:
   $$ \vec{\gamma}_n = \left[ \bar{\bar{T}}_d \cdot \vec{n} - (\vec{n} \cdot \bar{\bar{T}}_d \cdot \vec{n})\vec{n} \right] ds $$

---

## 🌟 3. Principal Directions of Deformation (Notes.pdf, Eqs. 2.54–2.55)

There exist three privileged orthogonal directions in space along which the deformation reduces to a **pure extension or compression, with no shear whatsoever** ($d\vec{v}_d \parallel \vec{n}$).

These principal directions $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ and their corresponding principal strain rates $(\lambda_1, \lambda_2, \lambda_3)$ are obtained by solving the eigenvalue problem:

$$ \bar{\bar{T}}_d \cdot \vec{n} = \lambda \vec{n} \qquad \text{[Eq. 2.54]} $$

Imposing the existence of non-trivial solutions leads to the **characteristic equation**:

$$ |\bar{\bar{T}}_d - \lambda \bar{\bar{I}}| = 0 \qquad \text{[Eq. 2.55]} $$

Since $\bar{\bar{T}}_d$ is a real symmetric tensor, the spectral theorem guarantees that:
1. The three roots $\lambda_1, \lambda_2, \lambda_3$ are **strictly real**.
2. The three directing eigenvectors $(\vec{n}_1, \vec{n}_2, \vec{n}_3)$ are **mutually perpendicular**.
3. In the principal reference frame, the tensor takes diagonal form: $\bar{\bar{T}}_d = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$.

---

## 📦 4. Deformation of Square and Cubic Elements (Notes.pdf, Eqs. 2.56–2.63)

### A. Two-Dimensional Square Element (Side $dl$)
Analysing the time evolution of the horizontal side $dl(1, 0)$ and the vertical side $dl(0, 1)$:
* **Diagonal elements:** $(\bar{\bar{T}}_d)_{11} = \frac{\partial v_1}{\partial x_1}$ and $(\bar{\bar{T}}_d)_{22} = \frac{\partial v_2}{\partial x_2}$ represent the relative elongation rate per unit length along each axis.
* **Off-diagonal elements of $\bar{\bar{T}}_d$:** $\frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} + \frac{\partial v_1}{\partial x_2}\right)$ represents half of the rate at which the original right angle between the two sides decreases (shear angular deformation rate).
* **Elements of $\bar{\bar{T}}_r$:** $\frac{1}{2}\left(\frac{\partial v_2}{\partial x_1} - \frac{\partial v_1}{\partial x_2}\right) = \frac{1}{2}\omega_3$ represents the mean angular velocity of rotation of the element in its own plane.

### B. Three-Dimensional Cubic Element: Volumetric Dilatation Rate
Consider a differential cubic element of initial volume $V_0 = dl^3$. After a time $dt$, each of the three edges is distorted according to $dl \vec{e}_i + dl (\vec{e}_i \cdot \nabla\vec{v}) dt$. The final volume is determined by the scalar triple product (determinant of the transformation):

$$ V_f = dl^3 \begin{vmatrix} 1 + \frac{\partial v_1}{\partial x_1} dt & \frac{\partial v_2}{\partial x_1} dt & \frac{\partial v_3}{\partial x_1} dt \\ \frac{\partial v_1}{\partial x_2} dt & 1 + \frac{\partial v_2}{\partial x_2} dt & \frac{\partial v_3}{\partial x_2} dt \\ \frac{\partial v_1}{\partial x_3} dt & \frac{\partial v_2}{\partial x_3} dt & 1 + \frac{\partial v_3}{\partial x_3} dt \end{vmatrix} \qquad \text{[Eq. 2.62]} $$

Expanding the determinant and neglecting higher-order terms $\mathcal{O}(dt^2, dt^3)$:

$$ V_f \simeq dl^3 \left[ 1 + \left( \frac{\partial v_1}{\partial x_1} + \frac{\partial v_2}{\partial x_2} + \frac{\partial v_3}{\partial x_3} \right) dt \right] $$

Dividing by the initial volume and the time increment, the **unit volumetric dilatation rate** is identically the divergence of the velocity and coincides with the trace of the rate-of-strain tensor:

$$ \mathbf{\frac{1}{V}\frac{dV}{dt} = \nabla \cdot \vec{v} = \text{tr}(\nabla\vec{v}) = \text{tr}(\bar{\bar{T}}_d) = \lambda_1 + \lambda_2 + \lambda_3} $$

### C. Incompressibility Condition
For a perfect liquid (strictly constant density $\rho = \rho_0$), the particle volume cannot change:

$$ \mathbf{\nabla \cdot \vec{v} = 0 \iff \frac{\partial v_1}{\partial x_1} + \frac{\partial v_2}{\partial x_2} + \frac{\partial v_3}{\partial x_3} = 0} \qquad \text{[Eq. 2.63]} $$

Physically, this implies that the extension rates $(\partial_1 v_1, \partial_2 v_2, \partial_3 v_3)$ **cannot all have the same sign**: a positive extension in one direction must necessarily be compensated by contractions in the remaining directions to preserve volume.

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Vorticity, Circulation and Velocity Potential|Concept: Vorticity and Circulation]]
* [[01 - Fluid Mechanics/Concept - Convective Flux and Stream Function|Concept: Convective Flux and Divergence]]
