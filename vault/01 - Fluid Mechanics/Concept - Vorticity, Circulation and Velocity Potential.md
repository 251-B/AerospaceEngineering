---
materia: Fluid Mechanics
tema: "Topic 2: Flow Kinematics"
tags:
  - theory
  - key-concept
  - vorticity
  - circulation
  - velocity-potential
dificultad: medium
prerrequisitos: []
---

# 🌪️ Concept: Vorticity, Circulation and Velocity Potential

> **Key idea in one sentence:** Vorticity quantifies the local microscopic rotation of fluid particles, while circulation measures the macroscopic motion along a closed circuit; when the flow is irrotational ($\vec{\omega} \equiv 0$), the vector velocity field derives from a scalar potential $\phi$ ($\vec{v} = \nabla\phi$).

---

## 🎯 1. Circulation ($\Gamma$) along a Curve (Notes.pdf, Eqs. 2.29–2.31)

The **circulation** $\Gamma$ of the velocity field along an oriented curve $L$ is defined as the line integral:

$$ \Gamma = \int_L \vec{v} \cdot d\vec{l} \qquad \text{[Eq. 2.29]} $$

where $d\vec{l}$ is the differential displacement vector along the curve. Physically, the circulation represents an accumulated measure of the net motion or transport of the fluid projected onto the tangential direction of the curve.

If the curve is parametrised by $\vec{x} = \vec{x}_l(\lambda)$ with $\lambda_1 \le \lambda \le \lambda_2$:
$$ d\vec{l} = \frac{d\vec{x}_l}{d\lambda} d\lambda \implies \Gamma = \int_{\lambda_1}^{\lambda_2} \vec{v}(\vec{x}_l(\lambda), t) \cdot \frac{d\vec{x}_l}{d\lambda} d\lambda \qquad \text{[Eq. 2.31]} $$

---

## 🌀 2. The Vorticity Vector ($\vec{\omega}$) and Stokes' Theorem (Notes.pdf, Eqs. 2.32–2.33)

Consider a simple closed curve $L$ bounding an oriented surface $\Sigma$ fully immersed in the continuous fluid. Applying **Stokes' theorem**:

$$ \mathbf{\Gamma = \oint_L \vec{v} \cdot d\vec{l} = \int_\Sigma (\nabla \wedge \vec{v}) \cdot \vec{n} \, d\sigma} \qquad \text{[Eq. 2.32]} $$

where $\vec{n}$ is the unit vector normal to the surface $\Sigma$, oriented according to the right-hand rule with respect to the direction of traversal of the curve $L$.

### Definition of Vorticity
The **vorticity** vector $\vec{\omega}$ is defined as the curl of the velocity field:

$$ \mathbf{\vec{\omega} = \nabla \wedge \vec{v}} $$

### Local Physical Meaning
If we shrink the curve $L$ to the contour of an infinitesimal differential surface element $d\sigma$ with normal $\vec{n}$:
$$ \oint_L \vec{v} \cdot d\vec{l} = (\nabla \wedge \vec{v}) \cdot \vec{n} \, d\sigma = \vec{\omega} \cdot \vec{n} \, d\sigma \qquad \text{[Eq. 2.33]} $$

Therefore, $(\nabla \wedge \vec{v}) \cdot \vec{n} = \omega_n$ is the **circulation per unit surface area oriented along $\vec{n}$**.  
At a given point, the circulation reaches its maximum value when the plane containing the curve is perpendicular to the vorticity vector $\vec{\omega}$. As will be shown when decomposing the velocity gradient tensor, the angular velocity of rotation of the fluid particle as a rigid solid is exactly half the vorticity:
$$ \vec{\Omega}_{\text{fluid}} = \frac{1}{2} \vec{\omega} = \frac{1}{2}(\nabla \wedge \vec{v}) $$

---

## 🌊 3. Irrotational Flow and the Velocity Potential Function ($\phi$) (Notes.pdf, Eq. 2.34)

A flow is called **irrotational** when the vorticity is identically zero at all points of the fluid domain:

$$ \vec{\omega} = \nabla \wedge \vec{v} = 0 \quad \forall \vec{x} $$

From vector calculus it follows that every irrotational vector field admits the existence of a scalar function $\phi(\vec{x}, t)$, called the **velocity potential**, such that:

$$ \mathbf{\vec{v} = \nabla\phi} \qquad \text{[Eq. 2.34]} $$

* In Cartesian coordinates: $v_x = \frac{\partial\phi}{\partial x}, \quad v_y = \frac{\partial\phi}{\partial y}, \quad v_z = \frac{\partial\phi}{\partial z}$.
* In cylindrical coordinates: $v_r = \frac{\partial\phi}{\partial r}, \quad v_\theta = \frac{1}{r}\frac{\partial\phi}{\partial \theta}, \quad v_z = \frac{\partial\phi}{\partial z}$.
* In spherical coordinates: $v_r = \frac{\partial\phi}{\partial r}, \quad v_\theta = \frac{1}{r}\frac{\partial\phi}{\partial \theta}, \quad v_\phi = \frac{1}{r\sin\theta}\frac{\partial\phi}{\partial \phi}$.

### Fundamental Analytical Advantage
The velocity potential replaces the determination of a vector field with three unknowns $(v_1, v_2, v_3)$ by the solution of a single scalar field $\phi(\vec{x}, t)$. If the fluid is also incompressible ($\nabla \cdot \vec{v} = 0$), the potential satisfies the **Laplace equation**:
$$ \nabla \cdot (\nabla\phi) = \nabla^2\phi = 0 $$

---

## 🛩️ 4. Topological Connectivity of the Domain and Aerodynamic Lift

> [!IMPORTANT] Simply Connected vs Multiply Connected Domains (Notes.pdf, p. 16)
> * If the circulation around **any** closed curve is zero, the flow is necessarily irrotational.
> * **However, the converse does not always hold:** even though $\nabla \wedge \vec{v} = 0$ at every point where there is fluid, the circulation $\oint_L \vec{v}\cdot d\vec{l}$ around a closed curve can be **non-zero**.
>
> This occurs when the fluid domain is **multiply connected** (for example, the external flow around an airfoil or cylinder). The curve $L$ surrounding the obstacle cannot be continuously contracted to a point without leaving the fluid domain (that is, without crossing the solid). Since the surface $\Sigma$ spanning $L$ is not entirely contained in the fluid, Stokes' theorem cannot be applied to the whole interior.
>
> In aerodynamics, this phenomenon is the physical basis of lift: the non-zero circulation $\Gamma \neq 0$ around the airfoil generates a lift force perpendicular to the free stream, proportional to $\Gamma$ (**Kutta-Joukowski Theorem**):
> $$ L' = \rho_\infty V_\infty \Gamma $$

---

## 🔗 Related Concepts
* [[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]
* [[01 - Fluid Mechanics/Concept - Convective Flux and Stream Function|Concept: Stream Function]]
* [[01 - Fluid Mechanics/Concept - Deformation, Rotation and the Rate-of-Strain Tensor|Concept: Strain and Rotation Tensor]]
