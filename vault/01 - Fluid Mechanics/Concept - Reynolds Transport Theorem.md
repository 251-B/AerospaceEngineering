---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - reynolds-transport
  - control-volume
  - euler-lagrange
dificultad: high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Topic 2 - Flow Kinematics|Topic 2: Flow Kinematics]]"
---

# 🔬 Concept: Reynolds Transport Theorem (RTT)

> **Key idea in one sentence:** The Reynolds Transport Theorem is the fundamental kinematic bridge between the Lagrangian perspective (physical laws applied to a closed material or fluid volume $V_f(t)$) and the Eulerian perspective (balances in an arbitrary open control volume $V_c(t)$ or a fixed one $V_0$), splitting the global time variation into a local internal accumulation rate and a net convective flux through the control surface.

---

## 🎯 1. Extensive and Intensive Quantities (Notes.pdf, Eq. 3.1)

In classical mechanics, the fundamental conservation laws (mass, Newton's second law, angular momentum, first law of thermodynamics) are postulated for **closed material systems** (a fixed fluid mass $M$ invariably composed of the same fluid particles occupying a deformable volume $V_f(t)$ bounded by a fluid surface $\Sigma_f(t)$).

Let $\Phi(t)$ be a global extensive property of the fluid system (such as the total mass, the linear momentum or the total energy). This quantity can be expressed as the volume integral of an intensive quantity per unit volume $\phi(\vec{x}, t)$:

$$ \Phi(t) = \int_{V_f(t)} \phi(\vec{x}, t) \, dV \qquad \text{[Eq. 3.1]} $$

where the volumetric density $\phi$ takes the canonical values:
* **Mass:** $\phi = \rho$
* **Linear momentum:** $\phi = \rho \vec{v}$
* **Angular momentum about $\vec{x}_0$:** $\phi = \rho [(\vec{x} - \vec{x}_0) \wedge \vec{v}]$
* **Total energy:** $\phi = \rho \left(e + \frac{|\vec{v}|^2}{2}\right)$

Since both the integrand $\phi(\vec{x}, t)$ and the integration domain $V_f(t)$ vary continuously with time, the ordinary time derivative $\frac{d\Phi}{dt}$ cannot be evaluated by directly introducing the partial derivative inside the integral.

---

## 📐 2. Rigorous Mathematical Derivation by Passage to the Limit (Notes.pdf, Eqs. 3.2–3.6)

By the formal definition of the ordinary time derivative:

$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi(\vec{x}, t) \, dV\right] = \lim_{\Delta t \to 0} \frac{1}{\Delta t} \left[ \int_{V_f(t + \Delta t)} \phi(\vec{x}, t + \Delta t) \, dV - \int_{V_f(t)} \phi(\vec{x}, t) \, dV \right] \qquad \text{[Eq. 3.2]} $$

Decomposing the domain at time $t + \Delta t$ into the common region $V_f(t)$ and the incremental region swept by the boundary $V_f(t + \Delta t) - V_f(t)$, the limit splits exactly into two summands:

$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \left[ \int_{V_f(t)} \left[\phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t)\right] dV + \int_{V_f(t + \Delta t) - V_f(t)} \phi(\vec{x}, t + \Delta t) \, dV \right] \qquad \text{[Eq. 3.3]} $$

### Term 1: Local Unsteadiness
In the first summand, the domain $V_f(t)$ is independent of $\Delta t$. Expanding in a Taylor series:
$$ \phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t) = \frac{\partial \phi}{\partial t} \Delta t + \mathcal{O}(\Delta t^2) $$
Dividing by $\Delta t$ and taking the limit $\Delta t \to 0$:
$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \int_{V_f(t)} \left[\phi(\vec{x}, t + \Delta t) - \phi(\vec{x}, t)\right] dV = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV \qquad \text{[Eq. 3.4]} $$

### Term 2: Convective Flux through the Moving Boundary
In the second summand, during the differential interval $\Delta t$, each surface element $d\sigma$ of $\Sigma_f(t)$ with outward normal vector $\vec{n}$ moves at the fluid velocity $\vec{v}(\vec{x}, t)$. The swept volume element is an oblique cylinder of base $d\sigma$ and height $(\vec{v} \Delta t)\cdot\vec{n}$:
$$ dV = (\vec{v} \Delta t) \cdot \vec{n} \, d\sigma $$
Substituting into the integral and integrating over the whole closed surface $\Sigma_f(t)$:
$$ \lim_{\Delta t \to 0} \frac{1}{\Delta t} \int_{V_f(t + \Delta t) - V_f(t)} \phi(\vec{x}, t + \Delta t) \, dV = \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.5]} $$

### Reynolds Equation for a Fluid Volume $V_f(t)$
Adding both contributions yields the classical form of the Reynolds Transport Theorem:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_f(t)} \phi(\vec{x}, t) \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma} \qquad \text{[Eq. 3.6]} $$

> [!NOTE] Physical Duality: Unsteadiness vs Motion
> * **First term ($\int_{V_f} \frac{\partial \phi}{\partial t} dV$):** Intrinsic rate of variation of the property inside the instantaneous volume due to the unsteady character of the flow (*flow unsteadiness*).
> * **Second term ($\int_{\Sigma_f} \phi \vec{v}\cdot\vec{n} d\sigma$):** Net rate of gain or loss produced by the deformation and convective translation of the boundary in space (*fluid motion*).

---

## 🔄 3. Extension to an Arbitrary Moving Control Volume $V_c(t)$ (Notes.pdf, Eqs. 3.7–3.8)

In aerospace engineering practice (for example, the interior of a rocket combustion chamber or the nozzle of a turbofan), it is not convenient to follow a material fluid volume that deforms and stretches indefinitely downstream. It is convenient to define an arbitrary geometric region in space: a **control volume** $V_c(t)$ bounded by a control surface $\Sigma_c(t)$, whose boundary moves at an arbitrary prescribed velocity $\vec{v}_c(\vec{x}, t)$.

Applying the same kinematic passage-to-the-limit argument to the geometric volume $V_c(t)$:

$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi(\vec{x}, t) \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.7]} $$

Let us now choose, at the generic instant $t$, a control volume $V_c(t)$ whose surface coincides instantaneously and exactly with the material fluid volume $V_f(t)$ ($\Sigma_c(t) \equiv \Sigma_f(t)$ and $V_c(t) \equiv V_f(t)$). The volume integrals of $\partial\phi/\partial t$ in (3.6) and (3.7) are identical. Directly subtracting both expressions:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma} \qquad \text{[Eq. 3.8]} $$

> [!IMPORTANT] Universal Reynolds Transport Theorem
> Equation 3.8 is the fundamental mathematical tool of the whole integral analysis of fluids. It establishes that the rate of change of any physical property contained in the material system $V_f(t)$ is equal to:
> 1. The time rate of variation of that quantity stored in the control volume $V_c(t)$.
> 2. Plus the net outgoing convective flux of that quantity through the control surface $\Sigma_c(t)$, transported by the **relative velocity of the fluid with respect to the control boundary** $(\vec{v} - \vec{v}_c)$.

---

## ⚙️ 4. Special Cases of Practical Interest

### A. Control Volume Fixed in Space ($V_0, \vec{v}_c = 0$)
If the control volume neither deforms nor moves ($\vec{v}_c \equiv 0$ and $V_c(t) \equiv V_0$ with fixed surface $\Sigma_0$):
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_0} \phi \, dV\right] + \int_{\Sigma_0} \phi \, \vec{v}\cdot\vec{n} \, d\sigma = \int_{V_0} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_0} \phi \, \vec{v}\cdot\vec{n} \, d\sigma $$

### B. Volume That Moves with the Fluid ($\vec{v}_c = \vec{v}$)
If the boundary of the control volume moves locally with the fluid itself ($\vec{v}_c = \vec{v}$), the relative velocity is zero $(\vec{v} - \vec{v}_c = 0)$, trivially recovering the derivative of the fluid volume:
$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] $$

### C. Local Differential Form via Gauss's Theorem
Applying the divergence theorem to the surface flux in (3.6) for a material volume:
$$ \int_{\Sigma_f(t)} \phi \vec{v}\cdot\vec{n} d\sigma = \int_{V_f(t)} \nabla \cdot (\phi\vec{v}) \, dV $$
Substituting into (3.6):
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \left[ \frac{\partial \phi}{\partial t} + \nabla \cdot (\phi\vec{v}) \right] dV $$
Recalling the identity $\nabla \cdot (\phi\vec{v}) = \vec{v}\cdot\nabla\phi + \phi\nabla\cdot\vec{v}$ and the material derivative $\frac{D\phi}{Dt} = \frac{\partial\phi}{\partial t} + \vec{v}\cdot\nabla\phi$:
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \left[ \frac{D\phi}{Dt} + \phi(\nabla \cdot \vec{v}) \right] dV $$
Taking the limit of an elementary particle of volume $dV$, with $\phi = \rho$:
$$ \frac{d}{dt}(\rho dV) = \left[\frac{D\rho}{Dt} + \rho(\nabla \cdot \vec{v})\right] dV = 0 $$
which transparently demonstrates the exact equivalence between the macroscopic mass conservation and the differential continuity equation $\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec{v}) = 0$.

---

## 🚀 5. Applications in Aerospace Engineering

1. **Rocket Thrust and Propulsive Nozzles:** Choice of control volumes that cut the nozzle exit section orthogonally ($\vec{v}_c = 0$ or $\vec{v}_c = \vec{v}_{\text{rocket}}$), making it possible to compute the thrust force directly by integrating the momentum flux $(\rho\vec{v})(\vec{v}-\vec{v}_c)\cdot\vec{n} d\sigma$ without having to solve the complete internal turbulent field.
2. **Propagation of Moving Shock Waves:** Selection of a control volume that travels attached to the shock discontinuity at constant velocity $\vec{v}_c = \vec{D}_{\text{shock}}$, transforming an unsteady transient problem into a steady one-dimensional algebraic balance (Rankine-Hugoniot relations).
3. **Pistons and Moving Blades in Turbomachinery:** Modelling of cavities of axial compressors and centrifugal pumps where the walls move periodically at angular velocity $\vec{v}_c = \vec{\Omega}\wedge\vec{x}$.
