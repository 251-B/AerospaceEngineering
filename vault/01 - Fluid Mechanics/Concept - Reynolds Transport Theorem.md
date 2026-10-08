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

## Step-by-Step Derivation of the Reynolds Transport Theorem (Notes.pdf, Eqs. 3.2-3.8)

This section expands every step that the compact derivation above skips. Throughout, $\phi(\vec{x},t)$ is the volumetric density of the extensive property (in the notation $B=\int\rho b\,dV$ used elsewhere, $\phi=\rho b$). It is assumed twice continuously differentiable in space and time, and the surfaces $\Sigma_f(t)$ and $\Sigma_c(t)$ are smooth and closed, with $\vec{n}$ the outward unit normal. Equation numbers are those of Notes.pdf, Chapter 3.

### Step 1: Split the difference quotient (Eqs. 3.2 and 3.3)

The material volume at $t+dt$ is the volume at $t$ plus the thin shell $\delta V=V_f(t+dt)-V_f(t)$ swept by its boundary. The shell is counted algebraically: where the boundary moves inward it removes volume. Add and subtract $\int_{V_f(t)}\phi(\vec{x},t+dt)\,dV$ in the numerator of the limit definition (Eq. 3.2):

$$ \int_{V_f(t+dt)}\phi(\vec{x},t+dt)\,dV-\int_{V_f(t)}\phi(\vec{x},t)\,dV=\int_{V_f(t)}\big[\phi(\vec{x},t+dt)-\phi(\vec{x},t)\big]dV+\int_{\delta V}\phi(\vec{x},t+dt)\,dV $$

*Eq. 3.2 rewritten as Eq. 3.3 (before the limit)*

The first integral has a fixed domain $V_f(t)$ and measures how the field changes at fixed points. The second integral contains the field only over the thin shell and measures how much the domain grows.

### Step 2: The unsteadiness term (Eq. 3.4)

Taylor-expand the integrand at a fixed point $\vec{x}$:

$$ \phi(\vec{x},t+dt)-\phi(\vec{x},t)=\frac{\partial\phi}{\partial t}\,dt+O(dt^{2}) $$

Because $\phi$ is $C^2$ and $V_f(t)$ is bounded, the remainder is uniformly $O(dt^2)$ over the domain, so it can be integrated. Dividing by $dt$ and letting $dt\to0$ (the domain $V_f(t)$ does not depend on $dt$):

$$ \lim_{dt\to0}\frac{1}{dt}\int_{V_f(t)}\big[\phi(\vec{x},t+dt)-\phi(\vec{x},t)\big]dV=\int_{V_f(t)}\frac{\partial\phi}{\partial t}\,dV $$

*Eq. 3.4*

### Step 3: The swept-volume term (Eq. 3.5)

A point $\vec{x}_s$ of the material surface moves in the time $dt$ to $\vec{x}_s+\vec{v}\,dt+O(dt^2)$. Its displacement along the outward normal is $(\vec{v}\cdot\vec{n})\,dt$. The tangential part only slides the point along the surface and adds no volume. The shell above a surface element $d\sigma$ is therefore a prism of base $d\sigma$ and height $(\vec{v}\cdot\vec{n})\,dt$ (an oblique prism has the same volume as a right prism of equal base and height). Where $\vec{v}\cdot\vec{n}\lt0$ the height is negative and the shell removes volume, which is the algebraic counting adopted in Step 1:

$$ d(\delta V)=(\vec{v}\cdot\vec{n})\,dt\,d\sigma+O(dt^{2}) $$

Since $\phi(\vec{x},t+dt)=\phi(\vec{x},t)+O(dt)$, the integrand can be evaluated at time $t$ at the cost of an $O(dt^2)$ error:

$$ \int_{\delta V}\phi(\vec{x},t+dt)\,dV=dt\int_{\Sigma_f(t)}\phi(\vec{x},t)\,\vec{v}\cdot\vec{n}\,d\sigma+O(dt^{2}) $$

Dividing by $dt$ and taking the limit gives the convective flux through the moving boundary:

$$ \lim_{dt\to0}\frac{1}{dt}\int_{\delta V}\phi(\vec{x},t+dt)\,dV=\int_{\Sigma_f(t)}\phi\,\vec{v}\cdot\vec{n}\,d\sigma $$

*Eq. 3.5*

### Step 4: Add both contributions (Eq. 3.6)

The limit of the sum is the sum of the limits, so Eqs. 3.4 and 3.5 give Eq. 3.6:

$$ \frac{d}{dt}\int_{V_f(t)}\phi\,dV=\int_{V_f(t)}\frac{\partial\phi}{\partial t}\,dV+\int_{\Sigma_f(t)}\phi\,\vec{v}\cdot\vec{n}\,d\sigma $$

*Eq. 3.6*

### Step 5: Arbitrary moving control volume (Eq. 3.7)

A control volume $V_c(t)$ is a geometric region whose boundary points move with a prescribed velocity $\vec{v}_c(\vec{x},t)$, not necessarily equal to the fluid velocity. Steps 1 to 4 used the velocity of the boundary only to compute the displacement $(\vec{v}\cdot\vec{n})\,dt$ of the surface. Repeating them with the boundary velocity $\vec{v}_c$ in place of $\vec{v}$ gives

$$ \frac{d}{dt}\int_{V_c(t)}\phi\,dV=\int_{V_c(t)}\frac{\partial\phi}{\partial t}\,dV+\int_{\Sigma_c(t)}\phi\,\vec{v}_c\cdot\vec{n}\,d\sigma $$

*Eq. 3.7*

### Step 6: Subtraction at the instant of coincidence (Eq. 3.8)

Choose $V_c(t)$ so that at the instant $t$ it occupies exactly the same region as $V_f(t)$, hence $\Sigma_c(t)=\Sigma_f(t)$ and the normal $\vec{n}$ is the same. (At later times the two volumes differ, which is why only the instantaneous values of the derivatives are compared.) The integrals of $\partial\phi/\partial t$ in Eqs. 3.6 and 3.7 are then identical. Subtracting Eq. 3.7 from Eq. 3.6:

$$ \frac{d}{dt}\int_{V_f}\phi\,dV-\frac{d}{dt}\int_{V_c}\phi\,dV=\int_{\Sigma_c}\phi\,\vec{v}\cdot\vec{n}\,d\sigma-\int_{\Sigma_c}\phi\,\vec{v}_c\cdot\vec{n}\,d\sigma $$

Combining the two surface integrals gives Eq. 3.8:

$$ \frac{d}{dt}\int_{V_f(t)}\phi\,dV=\frac{d}{dt}\int_{V_c(t)}\phi\,dV+\int_{\Sigma_c(t)}\phi\,(\vec{v}-\vec{v}_c)\cdot\vec{n}\,d\sigma $$

*Eq. 3.8*

### Step 7: Checks (extension, not in the Notes)

**One-dimensional check with the Leibniz rule.** Take a one-dimensional "volume" $a(t)\le x\le b(t)$. The outward normals are $n=+1$ at $x=b$ and $n=-1$ at $x=a$, and the boundary velocities are $\dot b$ and $\dot a$. Eq. 3.7 gives $\int_a^b\partial\phi/\partial t\,dx+\phi(b,t)\dot b-\phi(a,t)\dot a$. Differentiating $F(t)=\int_{a(t)}^{b(t)}\phi(x,t)\,dx$ directly with the chain rule for $F(t,a,b)$ and Barrow's rule $\partial F/\partial b=\phi(b,t)$, $\partial F/\partial a=-\phi(a,t)$:

$$ \frac{dF}{dt}=\frac{\partial F}{\partial t}+\frac{\partial F}{\partial b}\dot b+\frac{\partial F}{\partial a}\dot a=\int_a^b\frac{\partial\phi}{\partial t}\,dx+\phi(b,t)\,\dot b-\phi(a,t)\,\dot a $$

Both results coincide, which confirms the sign convention of the flux term.

**Dimensional check.** If $[\phi]$ denotes the units of the density, then $[d\Phi/dt]=[\phi]\,\mathrm{m^3/s}$, the unsteady term has units $[\phi]\,\mathrm{m^3/s}$, and the flux term has units $[\phi]\cdot(\mathrm{m/s})\cdot\mathrm{m^2}=[\phi]\,\mathrm{m^3/s}$.

**Limiting case.** If $\vec{v}_c=\vec{v}$ at the boundary, the relative velocity vanishes and Eq. 3.8 reduces to the identity $d\Phi_f/dt=d\Phi_c/dt$, as expected for a volume that moves with the fluid.

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
