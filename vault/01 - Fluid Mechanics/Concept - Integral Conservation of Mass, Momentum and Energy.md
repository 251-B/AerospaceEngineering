---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - theory
  - key-concept
  - integral-conservation
  - mass-momentum-energy
  - aerospace-thrust
dificultad: very high
prerrequisitos:
  - "[[01 - Fluid Mechanics/Concept - Reynolds Transport Theorem|Concept: Reynolds Transport Theorem]]"
  - "[[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|Concept: Cauchy Stress Tensor]]"
  - "[[01 - Fluid Mechanics/Concept - Navier-Poisson Constitutive Equation|Concept: Navier-Poisson Equation]]"
  - "[[01 - Fluid Mechanics/Concept - Fourier's Law and Heat Conduction|Concept: Fourier's Law and Heat Conduction]]"
---

# 🔬 Concept: Integral Conservation of Mass, Momentum and Energy

> **Key idea in one sentence:** The conservation laws of classical mechanics applied to an arbitrary control volume $V_c(t)$ allow exact global balances (lift and drag forces, thrust of aeronautical propulsors, torques in turbomachinery and thermal powers) to be computed by integrating only the fluxes and stresses on the control boundaries, without having to solve the detailed kinematics at every interior point of the domain.

---

## 💧 1. Integral Mass Conservation Equation (Notes.pdf, Eqs. 3.9–3.11)

### Physical Principle
The mass of a closed material system (fluid volume $V_f(t)$) is constant in time in non-relativistic mechanics:

$$ \frac{d}{dt} M = \frac{d}{dt} \left[ \int_{V_f(t)} \rho \, dV \right] = 0 \qquad \text{[Eq. 3.9]} $$

### For an Arbitrary Moving Control Volume $V_c(t)$
Applying the Reynolds Transport Theorem (Eq. 3.8) with $\phi = \rho$:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0} \qquad \text{[Eq. 3.10]} $$

* **Term 1:** Time rate of accumulation or depletion of mass inside the geometric cavity $V_c(t)$.
* **Term 2:** Net mass flux crossing the control surface $\Sigma_c(t)$, driven by the relative velocity of the fluid $(\vec{v} - \vec{v}_c)$.

### For a Control Volume Fixed in Space ($V_0, \vec{v}_c = 0$)
$$ \mathbf{\int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \, \vec{v}\cdot\vec{n} \, d\sigma = 0} \qquad \text{[Eq. 3.11]} $$

* **Steady flow:** $\frac{\partial\rho}{\partial t} = 0 \implies \int_{\Sigma_0} \rho \vec{v}\cdot\vec{n} d\sigma = 0 \implies \sum \dot{m}_{\text{out}} = \sum \dot{m}_{\text{in}}$.
* **Incompressible fluid ($\rho = \text{const}$):** $\int_{\Sigma_0} \vec{v}\cdot\vec{n} d\sigma = 0 \implies \sum Q_{\text{out}} = \sum Q_{\text{in}}$ (conservation of volumetric flow rate).

---

## Mass Conservation: Complete Derivation Chain (Notes.pdf, Eqs. 3.9-3.11 and 4.4-4.7)

### Step 1: Mass balance for an arbitrary moving control volume (Eq. 3.10)

The principle (Eq. 3.9) states that the mass of a fluid volume does not change, $dM/dt=0$ with $M=\int_{V_f(t)}\rho\,dV$. Choose $\phi=\rho$ in the Reynolds Transport Theorem (Eq. 3.8) and replace the left-hand side by zero:

$$ 0=\frac{d}{dt}\int_{V_f(t)}\rho\,dV=\frac{d}{dt}\int_{V_c(t)}\rho\,dV+\int_{\Sigma_c(t)}\rho\,(\vec{v}-\vec{v}_c)\cdot\vec{n}\,d\sigma $$

Moving the flux term to the other side shows the physical meaning: the rate of change of the mass stored in the control volume equals minus the net mass flux out through its boundary, that is, the mass flux entering.

$$ \frac{d}{dt}\int_{V_c(t)}\rho\,dV=-\int_{\Sigma_c(t)}\rho\,(\vec{v}-\vec{v}_c)\cdot\vec{n}\,d\sigma $$

*Eq. 3.10, rearranged*

### Step 2: Fixed control volume (Eq. 3.11)

For a fixed volume $V_0$ with surface $\Sigma_0$ we have $\vec{v}_c=\vec{0}$ and the domain does not depend on $t$. The limits of integration are therefore constants, no boundary term appears, and the time derivative passes inside the integral (compare Eq. 3.7 with $\vec{v}_c=\vec{0}$):

$$ \frac{d}{dt}\int_{V_0}\rho\,dV=\int_{V_0}\frac{\partial\rho}{\partial t}\,dV $$

Substituting into Eq. 3.10 with $\vec{v}_c=\vec{0}$ gives

$$ \int_{V_0}\frac{\partial\rho}{\partial t}\,dV+\int_{\Sigma_0}\rho\,\vec{v}\cdot\vec{n}\,d\sigma=0 $$

*Eq. 3.11*

### Step 3: Mass flow rate and sign convention

With $\vec{n}$ outward, the algebraic mass flow rate through a part $A$ of the control surface is

$$ \dot m_A=\int_A\rho\,(\vec{v}-\vec{v}_c)\cdot\vec{n}\,d\sigma $$

It is positive at outlets, negative at inlets and zero on impermeable walls, where no fluid crosses the surface and $(\vec{v}-\vec{v}_c)\cdot\vec{n}=0$. Eq. 3.10 then reads $dM_c/dt=-\sum_A\dot m_A$. For a steady flow in a fixed volume the left-hand side vanishes and $\sum\dot m_{\text{out}}=\sum\dot m_{\text{in}}$ (magnitudes). On a port of area $A_k$ with uniform $\rho_k$ and uniform velocity $v_k$ normal to the port, $|\dot m_k|=\rho_kv_kA_k$.

### Step 4: Differential form (Eqs. 4.4-4.7 of Notes.pdf, Chapter 4)

The following steps belong to Chapter 4 of the Notes and are reproduced here to close the logical chain between the integral and the local statement. Apply Eq. 3.6 with $\phi=\rho$ to Eq. 3.9:

$$ \int_{V_f(t)}\frac{\partial\rho}{\partial t}\,dV+\int_{\Sigma_f(t)}\rho\,\vec{v}\cdot\vec{n}\,d\sigma=0 $$

Gauss' theorem (Eq. 2.9), $\int_\Sigma\vec{A}\cdot\vec{n}\,d\sigma=\int_V\nabla\cdot\vec{A}\,dV$ with $\vec{A}=\rho\vec{v}$, turns the surface integral into a volume integral over the same domain:

$$ \int_{V_f(t)}\left[\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec{v})\right]dV=0 $$

*Eq. 4.4*

**Arbitrary-volume argument.** Let $g(\vec{x},t)=\partial\rho/\partial t+\nabla\cdot(\rho\vec{v})$, a continuous function. Eq. 4.4 holds for every fluid volume. Suppose $g(\vec{x}^{*},t)\neq0$ at some point, say $g(\vec{x}^{*},t)\gt0$. By continuity $g\gt0$ in a ball $B_\varepsilon(\vec{x}^{*})$. The fluid volume that occupies this ball at time $t$ then gives $\int_{B_\varepsilon}g\,dV\gt0$, which contradicts Eq. 4.4. The case $g\lt0$ is identical. Hence $g\equiv0$ at every point:

$$ \frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec{v})=0 $$

*Eq. 4.5*

Expand the divergence, $\nabla\cdot(\rho\vec{v})=\vec{v}\cdot\nabla\rho+\rho\,\nabla\cdot\vec{v}$, and use the material derivative $D\rho/Dt=\partial\rho/\partial t+\vec{v}\cdot\nabla\rho$:

$$ \frac{1}{\rho}\frac{D\rho}{Dt}=-\nabla\cdot\vec{v} $$

*Eq. 4.6*

For a constant-density fluid $D\rho/Dt=0$, so $\nabla\cdot\vec{v}=0$ (Eq. 4.7). For a steady flow of a gas, $\partial\rho/\partial t=0$ and Eq. 4.5 gives $\nabla\cdot(\rho\vec{v})=0$ (Eq. 4.8).

### Step 5: Control volume bounded by a moving free surface (extension)

**Extension, not in the Notes.** For a tank, the free surface $z=h(t)$ is part of $\Sigma_c$ and moves with $\vec{v}_c=\dot h\,\vec{e}_z$. It is a material surface (no fluid crosses it), so the kinematic condition $\vec{v}\cdot\vec{n}=\vec{v}_c\cdot\vec{n}$ holds. Therefore $(\vec{v}-\vec{v}_c)\cdot\vec{n}=0$ on it and it contributes no flux to Eq. 3.10. Only the inlet and the outlet contribute. With constant density and a tank of constant horizontal area $A_T$, the stored mass is $\rho A_Th(t)$ and Eq. 3.10 gives

$$ \rho A_T\frac{dh}{dt}=\rho Q_{\text{in}}-\rho Q_{\text{out}}\;\Longrightarrow\;A_T\frac{dh}{dt}=Q_{\text{in}}-Q_{\text{out}} $$

The discharge law $Q_{\text{out}}=A_e\sqrt{2gh}$ (Torricelli) is an input of the problem. It follows from Bernoulli's equation for steady inviscid flow, which is not derived in Topic 3 of the Notes, so it is taken here as an assumption.

## ✈️ 2. Forces and Moments on Submerged Bodies (Notes.pdf, Eqs. 3.32–3.33)

When a solid body (such as an airfoil, a fuselage or a turbine blade) is immersed in a fluid stream, the aerodynamic force and moment that the fluid exerts on the wetted solid wall $\Sigma$ come exclusively from the normal pressure stresses and the tangential viscous friction stresses.

Defining the unit normal vector $\vec{n}$ pointing **into the fluid** (leaving the solid):

### Resultant Force $\vec{F}$ (Lift + Drag)
$$ \mathbf{\vec{F} = -\int_\Sigma p \vec{n} \, d\sigma + \int_\Sigma \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma} \qquad \text{[Eq. 3.32]} $$

* $-\int_\Sigma p \vec{n} d\sigma$: **Pressure force**. The minus sign arises because a positive pressure compresses the surface in the direction opposite to the outward normal $\vec{n}$. It gives rise to aerodynamic lift ($L$) and form (pressure) drag ($D_p$).
* $\int_\Sigma \bar{\bar{\tau}}' \cdot \vec{n} d\sigma$: **Viscous friction force** (*skin-friction drag*). It gives rise to the parasitic drag due to tangential friction in the boundary layer.

### Resultant Moment $\vec{M}_{\vec{x}_0}$ about a Point $\vec{x}_0$
$$ \mathbf{\vec{M}_{\vec{x}_0} = -\int_\Sigma (\vec{x} - \vec{x}_0) \wedge (p\vec{n}) \, d\sigma + \int_\Sigma (\vec{x} - \vec{x}_0) \wedge (\bar{\bar{\tau}}' \cdot \vec{n}) \, d\sigma} \qquad \text{[Eq. 3.33]} $$

It determines the pitching, rolling and yawing moments of the space or aeronautical vehicle.

---

## 🎯 3. Integral Momentum Conservation Equation (Notes.pdf, Eqs. 3.34–3.36)

### For a Material Fluid Volume $V_f(t)$
Applying Newton's 2nd Law ($\frac{d}{dt}\vec{P} = \sum \vec{F}_{\text{ext}}$) and substituting the Cauchy tensor $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$:

$$ \frac{d}{dt}\left[\int_{V_f(t)} \rho\vec{v} \, dV\right] = -\int_{\Sigma_f(t)} p\vec{n} \, d\sigma + \int_{\Sigma_f(t)} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_f(t)} \rho\vec{f}_m \, dV \qquad \text{[Eq. 3.34]} $$

### For an Arbitrary Moving Control Volume $V_c(t)$
Applying the RTT (Eq. 3.8) with $\phi = \rho\vec{v}$:

$$ \mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = -\int_{\Sigma_c(t)} p\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m \, dV} \qquad \text{[Eq. 3.35]} $$

### For a Control Volume Fixed in Space ($V_0, \vec{v}_c = 0$)
$$ \mathbf{\int_{V_0} \frac{\partial(\rho\vec{v})}{\partial t} \, dV + \int_{\Sigma_0} \rho\vec{v}(\vec{v}\cdot\vec{n}) \, d\sigma = -\int_{\Sigma_0} p\vec{n} \, d\sigma + \int_{\Sigma_0} \bar{\bar{\tau}}' \cdot \vec{n} \, d\sigma + \int_{V_0} \rho\vec{f}_m \, dV} \qquad \text{[Eq. 3.36]} $$

### Exhaustive Physical Breakdown of the Five Terms
1. **$\frac{d}{dt}\int_{V_c} \rho\vec{v} dV$ (Inertia / Local Accumulation):** Rate at which the total momentum contained inside the control volume changes. It vanishes rigorously in steady regime.
2. **$\int_{\Sigma_c} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] d\sigma$ (Net Outgoing Convective Flux):** Net rate at which momentum leaves the volume through the inlet and outlet sections, driven by the mass crossing with relative velocity $(\vec{v}-\vec{v}_c)\cdot\vec{n}$.
3. **$-\int_{\Sigma_c} p\vec{n} d\sigma$ (Net Pressure Force):** Distributed thrust of the thermodynamic pressures on the control boundary. On sections open to the atmosphere, gauge pressures $(p - p_a)$ may be used.
4. **$\int_{\Sigma_c} \bar{\bar{\tau}}' \cdot \vec{n} d\sigma$ (Net Viscous Force):** Tangential friction on wetted solid walls or shear stresses on shear planes. Frequently negligible at distant inlet/outlet sections.
5. **$\int_{V_c} \rho\vec{f}_m dV$ (Total Body Force):** Total weight of the fluid in the volume ($+\int \rho\vec{g} dV$) and inertial forces if the system is non-inertial.

---

## Linear Momentum: Complete Derivation Chain (Notes.pdf, Eqs. 3.34-3.36 and 4.9-4.10)

### Step 1: Newton's second law for a fluid volume (Eq. 3.34)

The surface force on a fluid volume is the integral of the stress vector $\vec{f}_n=\bar{\bar{\tau}}\cdot\vec{n}$ (Eqs. 3.19 and 3.22) and the volume force is $\rho\vec{f}_m\,dV$ (Eq. 3.12). Newton's second law gives Eq. 3.34 in terms of the full stress tensor:

$$ \frac{d}{dt}\int_{V_f(t)}\rho\vec{v}\,dV=\int_{\Sigma_f(t)}\bar{\bar{\tau}}\cdot\vec{n}\,d\sigma+\int_{V_f(t)}\rho\vec{f}_m\,dV $$

*Eq. 3.34*

Insert the decomposition $\bar{\bar{\tau}}=-p\bar{\bar{I}}+\bar{\bar{\tau}}'$ (Eq. 3.28). Because $(p\bar{\bar{I}})\cdot\vec{n}=p\vec{n}$,

$$ \int_{\Sigma}\bar{\bar{\tau}}\cdot\vec{n}\,d\sigma=-\int_{\Sigma}p\,\vec{n}\,d\sigma+\int_{\Sigma}\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma $$

so the right-hand side splits into a pressure force, a viscous force and a body force. This is the form of the right-hand side of Eq. 3.35 (and of Eq. 4.2).

### Step 2: Transfer to a moving control volume (Eq. 3.35)

Eq. 3.8 holds for each Cartesian component of the vector density $\vec{\phi}=\rho\vec{v}$:

$$ \frac{d}{dt}\int_{V_f(t)}\rho\vec{v}\,dV=\frac{d}{dt}\int_{V_c(t)}\rho\vec{v}\,dV+\int_{\Sigma_c(t)}\rho\vec{v}\,\big[(\vec{v}-\vec{v}_c)\cdot\vec{n}\big]\,d\sigma $$

At the instant considered $V_c=V_f$ and $\Sigma_c=\Sigma_f$, so the force integrals of Step 1 can be evaluated on $\Sigma_c$ and $V_c$. Equating the right-hand side of Step 1 to the right-hand side above and moving the convective flux to the other side gives Eq. 3.35:

$$ \frac{d}{dt}\int_{V_c(t)}\rho\vec{v}\,dV+\int_{\Sigma_c(t)}\rho\vec{v}\,\big[(\vec{v}-\vec{v}_c)\cdot\vec{n}\big]\,d\sigma=-\int_{\Sigma_c(t)}p\,\vec{n}\,d\sigma+\int_{\Sigma_c(t)}\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_c(t)}\rho\vec{f}_m\,dV $$

*Eq. 3.35*

### Step 3: Fixed control volume (Eq. 3.36)

For a fixed volume $\vec{v}_c=\vec{0}$, the domain is constant and $d/dt$ passes inside the integral (see the mass section). The convective term becomes $\rho\vec{v}(\vec{v}\cdot\vec{n})$:

$$ \int_{V_0}\frac{\partial(\rho\vec{v})}{\partial t}\,dV+\int_{\Sigma_0}\rho\vec{v}\,(\vec{v}\cdot\vec{n})\,d\sigma=-\int_{\Sigma_0}p\,\vec{n}\,d\sigma+\int_{\Sigma_0}\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_0}\rho\vec{f}_m\,dV $$

*Eq. 3.36*

### Step 4: Reduction to uniform ports (extension)

**Extension, not in the Notes.** On a port $A_k$ of a fixed control volume where $\rho_k$ and $\vec{v}_k$ are uniform and $\vec{v}_k$ is normal to the port, the momentum flux integral is evaluated without approximation:

$$ \int_{A_k}\rho\vec{v}\,(\vec{v}\cdot\vec{n})\,d\sigma=\rho_k\vec{v}_k\,(\vec{v}_k\cdot\vec{n})\,A_k=\dot m_k\,\vec{v}_k,\qquad \dot m_k=\rho_k(\vec{v}_k\cdot\vec{n})A_k $$

where $\dot m_k$ is negative at inlets (algebraic convention of the mass section). On impermeable walls $\vec{v}\cdot\vec{n}=0$ and the flux vanishes. For steady flow Eq. 3.36 becomes

$$ \sum_k\dot m_k\vec{v}_k=\sum_{\text{out}}|\dot m|\,\vec{v}-\sum_{\text{in}}|\dot m|\,\vec{v}=-\int_{\Sigma_0}p\,\vec{n}\,d\sigma+\int_{\Sigma_0}\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_0}\rho\vec{f}_m\,dV $$

This is the "outgoing minus incoming momentum flux equals the sum of forces" statement used in the five-stage algorithm. If the velocity profile at a port is not uniform, the true flux $\int\rho v^2\,dA$ exceeds $\dot m\,\bar v$ and a momentum-flux correction coefficient is needed.

### Step 5: Differential momentum equation (Eq. 4.9) and consistency with Eq. 3.25

Apply Eq. 3.6 to Eq. 3.34 with $\phi=\rho v_i$, and use Gauss' theorem for every surface integral: $\int_\Sigma p\,n_i\,d\sigma=\int_V\partial p/\partial x_i\,dV$, $\int_\Sigma\rho v_iv_jn_j\,d\sigma=\int_V\partial(\rho v_iv_j)/\partial x_j\,dV$ and $\int_\Sigma\tau'_{ij}n_j\,d\sigma=\int_V\partial\tau'_{ij}/\partial x_j\,dV$. The volume is arbitrary, so the arbitrary-volume argument of the mass section gives

$$ \frac{\partial(\rho\vec{v})}{\partial t}+\nabla\cdot(\rho\vec{v}\vec{v})=-\nabla p+\nabla\cdot\bar{\bar{\tau}}'+\rho\vec{f}_m $$

*Eq. 4.9*

Expand component $i$ of the left-hand side with the product rule:

$$ \frac{\partial(\rho v_i)}{\partial t}+\frac{\partial(\rho v_iv_j)}{\partial x_j}=v_i\left[\frac{\partial\rho}{\partial t}+\frac{\partial(\rho v_j)}{\partial x_j}\right]+\rho\left[\frac{\partial v_i}{\partial t}+v_j\frac{\partial v_i}{\partial x_j}\right]=0+\rho\frac{Dv_i}{Dt} $$

The first bracket vanishes by the continuity equation (Eq. 4.5). Hence $\rho\,D\vec{v}/Dt=-\nabla p+\nabla\cdot\bar{\bar{\tau}}'+\rho\vec{f}_m$ (Eq. 4.10), which is Eq. 3.25 with $\nabla\cdot(-p\bar{\bar{I}})=-\nabla p$. The integral law (Eq. 3.35) and Cauchy's local law (Eq. 3.25) are therefore the same statement.


## Wake Momentum Integral: Every Step of the Drag Formula

This section expands the derivation of the wake-deficit drag integral of the airfoil example (profile $v(y)=v_\infty[1-\delta(y)]$, $\delta(y)=\Delta(1-|y|/b)$ for $|y|\le b$, and $v=v_\infty$ outside). It is an application of Eq. 3.36 and Eq. 3.11 (extension, not in the Notes). Per unit span, steady incompressible flow.

### Step 1: Control volume and momentum equation

Take the fixed rectangle $-L\le x\le L$, $-H\le y\le H$ with $H\gt b$, from which the airfoil is excluded, so the airfoil surface is part of the boundary. There $\vec{v}\cdot\vec{n}=0$ (no flux through a solid wall) and the fluid receives the force $-D\,\vec{e}_x$, where $D$ is the drag of the fluid on the airfoil. Pressure equals $p_\infty$ on the outer boundary, whose net force vanishes (the gauge-pressure argument of the text), and viscous stresses and body forces on the outer boundary are neglected. The $x$ component of Eq. 3.36 for steady flow gives

$$ -D=\int_{\Sigma_0}\rho\,v_x\,(\vec{v}\cdot\vec{n})\,d\sigma $$

### Step 2: Mass flux through each side

Inlet $x=-L$: $\vec{n}=-\vec{e}_x$, $v_x=v_\infty$. Outlet $x=L$: $\vec{n}=+\vec{e}_x$, $v_x=v(y)$ and the wake occupies $|y|\le b$. Top and bottom $y=\pm H$: fluid leaves through them with total mass flow $\dot m_{\text{lat}}$ and with axial velocity $v_x\approx v_\infty$ (outside the wake the streamlines are only slightly displaced; this is the assumption of the example). Eq. 3.11 in steady state states that the outflow equals the inflow:

$$ \underbrace{\rho v_\infty\,2H}_{\text{in}}=\underbrace{\rho v_\infty(2H-2b)+\rho\int_{-b}^{b}v\,dy}_{\text{outlet}}+\dot m_{\text{lat}}\;\Longrightarrow\;\dot m_{\text{lat}}=\rho\int_{-b}^{b}\big(v_\infty-v\big)\,dy $$

The outlet mass flow has been split into the uniform part outside the wake, of total width $2H-2b$, and the wake itself. This is the lateral leakage that a rigid rectangular control volume must include.

### Step 3: Momentum flux through each side

The three contributions to the right-hand side of the momentum equation are

$$ \text{inlet: }-\rho v_\infty^{2}\,2H,\qquad \text{outlet: }\rho v_\infty^{2}(2H-2b)+\rho\int_{-b}^{b}v^{2}\,dy,\qquad \text{lateral: }\dot m_{\text{lat}}\,v_\infty $$

Adding them and substituting $\dot m_{\text{lat}}$ from Step 2:

$$ -D=-2H\rho v_\infty^{2}+(2H-2b)\rho v_\infty^{2}+\rho\int_{-b}^{b}v^{2}\,dy+\rho v_\infty\int_{-b}^{b}(v_\infty-v)\,dy $$

The terms in $H$ cancel. Using $\int_{-b}^{b}v_\infty^{2}\,dy=2b\,v_\infty^{2}$ to cancel the remaining constant $-2b\rho v_\infty^{2}$:

$$ -D=\rho\int_{-b}^{b}\big(v^{2}-v_\infty v\big)\,dy\;\Longrightarrow\;D=\rho\int_{-b}^{b}v\,(v_\infty-v)\,dy $$

### Step 4: Evaluation of the integral with explicit limits

Since $v=v_\infty(1-\delta)$ and $v_\infty-v=v_\infty\delta$, the integrand is $v_\infty^{2}(1-\delta)\delta$. It is even in $y$, so

$$ D=2\rho v_\infty^{2}\int_{0}^{b}\big(\delta-\delta^{2}\big)\,dy,\qquad \delta(y)=\Delta\Big(1-\frac{y}{b}\Big) $$

Substitute $\xi=1-y/b$, so that $\delta=\Delta\xi$ and $dy=-b\,d\xi$. The limits are $y=0\Rightarrow\xi=1$ and $y=b\Rightarrow\xi=0$. Applying Barrow's rule after reversing the limits:

$$ \int_{0}^{b}\delta\,dy=\int_{\xi=1}^{\xi=0}\Delta\xi\,(-b\,d\xi)=\Delta b\int_{0}^{1}\xi\,d\xi=\Delta b\left[\frac{\xi^{2}}{2}\right]_{0}^{1}=\frac{\Delta b}{2} $$

$$ \int_{0}^{b}\delta^{2}\,dy=\Delta^{2}b\int_{0}^{1}\xi^{2}\,d\xi=\Delta^{2}b\left[\frac{\xi^{3}}{3}\right]_{0}^{1}=\frac{\Delta^{2}b}{3} $$

Therefore

$$ D=2\rho v_\infty^{2}\left(\frac{\Delta b}{2}-\frac{\Delta^{2}b}{3}\right)=\rho v_\infty^{2}\,b\,\Delta\left(1-\frac{2}{3}\Delta\right) $$

**Checks.** Dimensions: $[\rho v_\infty^{2}b]=\mathrm{kg\,m^{-3}\,m^{2}s^{-2}\,m}=\mathrm{N/m}$, a force per unit span, as required. Limit $\Delta\to0$ gives $D\to0$ (no wake, no drag). Limit $\Delta\to1$ gives $D\to\rho v_\infty^{2}b/3$, finite and positive.

## 🌀 4. Integral Angular Momentum Equation (Notes.pdf, Eqs. 3.37–3.38)

The balance of the moment of momentum about a fixed point $\vec{x}_0$ for a moving control volume $V_c(t)$ is given by:

$$ \begin{aligned}
\mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}] \, dV\right] + \int_{\Sigma_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma =} \\
\mathbf{-\int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma + \int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{f}_m] \, dV}
\end{aligned} \qquad \text{[Eq. 3.38]} $$

### Application to Aerospace Turbomachinery: Euler Equation
In the rotor of an axial compressor or gas turbine rotating at constant angular velocity $\vec{\Omega}$, the torque exerted by the rotor on the fluid in steady regime (the torque of the fluid on the rotor is its negative) is:
$$ T_{\text{shaft}} = \dot{m} (r_2 v_{\theta 2} - r_1 v_{\theta 1}) $$
Multiplying by $\Omega$, the mechanical power exchanged per unit mass flow rate is the **Euler turbomachinery formula**:
$$ w_{\text{Euler}} = u_2 v_{\theta 2} - u_1 v_{\theta 1} $$
where $u = \Omega r$ is the blade entrainment (blade-speed) velocity and $v_\theta$ is the tangential component of the fluid velocity.

---

## Angular Momentum: Complete Derivation Chain (Notes.pdf, Eqs. 3.37-3.38)

### Step 1: Angular momentum of a fluid volume (Eq. 3.37)

Let $\vec{r}=\vec{x}-\vec{x}_0$, with $\vec{x}_0$ a fixed point of an inertial frame. A fluid particle of mass $\rho\,dV$ has angular momentum $\vec{r}\wedge\rho\vec{v}\,dV$ about $\vec{x}_0$ (Notes, p. 33), so the angular momentum of the fluid volume is $\int_{V_f}\rho\,\vec{r}\wedge\vec{v}\,dV$. Newton's second law for angular momentum states that its rate of change equals the moment of the external forces about $\vec{x}_0$. The moment of the surface force $\bar{\bar{\tau}}\cdot\vec{n}\,d\sigma$ on each element of the boundary and the moment of the body force $\rho\vec{f}_m\,dV$ on each particle give Eq. 3.37:

$$ \frac{d}{dt}\int_{V_f(t)}\rho\,\vec{r}\wedge\vec{v}\,dV=\int_{\Sigma_f(t)}\vec{r}\wedge(\bar{\bar{\tau}}\cdot\vec{n})\,d\sigma+\int_{V_f(t)}\rho\,\vec{r}\wedge\vec{f}_m\,dV $$

*Eq. 3.37*

### Step 2: Consistency with the local momentum equation (extension)

**Extension, not in the Notes.** For a fluid particle the mass $\rho\,dV$ is constant and $D\vec{r}/Dt=\vec{v}$ because $\vec{x}_0$ is fixed. The product rule gives

$$ \frac{D}{Dt}\big[\vec{r}\wedge\rho\vec{v}\,dV\big]=\big[\vec{v}\wedge\vec{v}+\vec{r}\wedge\frac{D\vec{v}}{Dt}\big]\rho\,dV=\vec{r}\wedge\rho\frac{D\vec{v}}{Dt}\,dV $$

since $\vec{v}\wedge\vec{v}=\vec{0}$. Insert Cauchy's equation (Eq. 3.25), $\rho D\vec{v}/Dt=\nabla\cdot\bar{\bar{\tau}}+\rho\vec{f}_m$, and integrate over the volume:

$$ \frac{d}{dt}\int_{V_f}\rho\,\vec{r}\wedge\vec{v}\,dV=\int_{V_f}\vec{r}\wedge(\nabla\cdot\bar{\bar{\tau}})\,dV+\int_{V_f}\rho\,\vec{r}\wedge\vec{f}_m\,dV $$

It remains to show that the first integral on the right equals the surface integral of Eq. 3.37. With the permutation symbol $\epsilon_{kij}$, component $k$ of the integrand is $\epsilon_{kij}r_i\,\partial\tau_{lj}/\partial x_l$. The product rule and $\partial r_i/\partial x_l=\delta_{il}$ give

$$ \epsilon_{kij}\,r_i\frac{\partial\tau_{lj}}{\partial x_l}=\frac{\partial}{\partial x_l}\big(\epsilon_{kij}r_i\tau_{lj}\big)-\epsilon_{kij}\,\tau_{ij} $$

The last term vanishes because $\epsilon_{kij}$ is antisymmetric in $(i,j)$ and $\tau_{ij}$ is symmetric (Eq. 3.19). Gauss' theorem on the first term, together with $\tau_{lj}n_l=\tau_{jl}n_l=(\bar{\bar{\tau}}\cdot\vec{n})_j$, gives

$$ \int_{V}\vec{r}\wedge(\nabla\cdot\bar{\bar{\tau}})\,dV=\int_{\Sigma}\vec{r}\wedge(\bar{\bar{\tau}}\cdot\vec{n})\,d\sigma $$

which proves that Eq. 3.37 follows from Newton's law for linear momentum. The symmetry of the stress tensor is exactly the condition that makes both statements agree.

### Step 3: Transfer to a moving control volume (Eq. 3.38)

Apply Eq. 3.8 with the density $\vec{\phi}=\rho\,\vec{r}\wedge\vec{v}$, evaluate the right-hand side of Eq. 3.37 on $\Sigma_c$, $V_c$ (coincident with $\Sigma_f$, $V_f$ at the instant considered) and split the stress with Eq. 3.28. Since $\vec{r}\wedge\big((-p\bar{\bar{I}})\cdot\vec{n}\big)=-\vec{r}\wedge(p\vec{n})$:

$$ \frac{d}{dt}\int_{V_c}\rho\,\vec{r}\wedge\vec{v}\,dV+\int_{\Sigma_c}\rho\,(\vec{r}\wedge\vec{v})\big[(\vec{v}-\vec{v}_c)\cdot\vec{n}\big]\,d\sigma=-\int_{\Sigma_c}\vec{r}\wedge(p\vec{n})\,d\sigma+\int_{\Sigma_c}\vec{r}\wedge(\bar{\bar{\tau}}'\cdot\vec{n})\,d\sigma+\int_{V_c}\rho\,\vec{r}\wedge\vec{f}_m\,dV $$

*Eq. 3.38*

Because $\vec{x}_0$ is fixed, $\vec{r}$ is not differentiated in the control-volume term; the point $\vec{x}_0$ may be placed anywhere, and the choice is a matter of convenience.

### Step 4: Uniform ports and the pivot rule (extension)

**Extension, not in the Notes.** If a port $A_k$ is small compared with its distance to $\vec{x}_0$, then $\vec{r}\approx\vec{r}_k$ is constant over the port. With uniform $\rho_k$, $\vec{v}_k$ normal to the port and a fixed volume,

$$ \int_{A_k}\rho\,(\vec{r}\wedge\vec{v})(\vec{v}\cdot\vec{n})\,d\sigma\approx\vec{r}_k\wedge\Big[\int_{A_k}\rho\vec{v}(\vec{v}\cdot\vec{n})\,d\sigma\Big]=\dot m_k\,\vec{r}_k\wedge\vec{v}_k $$

For steady flow the equation reduces to $\sum_k\dot m_k\,\vec{r}_k\wedge\vec{v}_k=\sum\vec{M}_{\vec{x}_0}$, with $\dot m_k$ negative at inlets. An unknown reaction force $\vec{R}$ applied at the point $\vec{x}_R$ contributes the moment $(\vec{x}_R-\vec{x}_0)\wedge\vec{R}$, which is zero if $\vec{x}_0=\vec{x}_R$ (or if $\vec{x}_0$ lies on the line of action of $\vec{R}$). This is the pivot rule.

### Step 5: Euler turbomachinery equation (every step)

**Extension, not in the Notes.** Take a fixed annular control volume around the rotor axis $z$, with an inlet cylinder $r=r_1$ (normal $-\vec{e}_r$) and an outlet cylinder $r=r_2$ (normal $+\vec{e}_r$), with $\vec{x}_0$ on the axis. The flow is periodic and is treated as steady and axisymmetric on average, with $\rho$, $v_r$, $v_\theta$ uniform on each cylinder. The end walls are impermeable. The $z$ component of the angular momentum per unit mass follows from $\vec{r}=r\vec{e}_r+z\vec{e}_z$ and $\vec{v}=v_r\vec{e}_r+v_\theta\vec{e}_\theta+v_z\vec{e}_z$:

$$ (\vec{r}\wedge\vec{v})_z=r\,v_\theta $$

Convective flux in the $z$ component of Eq. 3.38. On the outlet $\vec{v}\cdot\vec{n}=+v_r$ and on the inlet $\vec{v}\cdot\vec{n}=-v_r$. The mass flow through each cylinder is the same, $\dot m=\int\rho v_r\,d\sigma$, by Eq. 3.11 in steady flow:

$$ \int_{\Sigma_0}\rho\,(r v_\theta)(\vec{v}\cdot\vec{n})\,d\sigma=r_2v_{\theta2}\,\dot m-r_1v_{\theta1}\,\dot m=\dot m\,(r_2v_{\theta2}-r_1v_{\theta1}) $$

Moments on the right-hand side. A pressure force on a cylinder of constant $r$ is $\mp p\,\vec{e}_r\,d\sigma$, and $(r\vec{e}_r+z\vec{e}_z)\wedge\vec{e}_r=z\,\vec{e}_z\wedge\vec{e}_r=z\,\vec{e}_\theta$, which has no $z$ component. On the end walls the force is along $\pm\vec{e}_z$ and $r\vec{e}_r\wedge\vec{e}_z=-r\vec{e}_\theta$, again with no $z$ component. Viscous stresses on the ports and the moment of the body force about the axis are neglected. The only remaining moment is the moment $M_z$ exerted by the blades (solid surfaces inside the volume) on the fluid:

$$ M_z=\dot m\,(r_2v_{\theta2}-r_1v_{\theta1}) $$

Here $M_z$ is the torque exerted by the rotor on the fluid. The torque exerted by the fluid on the rotor is $-M_z$ (Newton's third law). Each blade point moves with velocity $\Omega r\,\vec{e}_\theta$, so the power transmitted to the fluid is $\Omega M_z$ and the work per unit mass is

$$ w_{\text{Euler}}=\frac{\Omega M_z}{\dot m}=u_2v_{\theta2}-u_1v_{\theta1},\qquad u=\Omega r $$

Dimensional check: $[\dot m\,r\,v_\theta]=\mathrm{kg\,s^{-1}\,m\,m\,s^{-1}}=\mathrm{N\,m}$ and $[u\,v_\theta]=\mathrm{m^2/s^2}=\mathrm{J/kg}$.

## ⚡ 5. Integral Total Energy Conservation Equation (Notes.pdf, Eqs. 3.45–3.46)

### For a Material Fluid Volume $V_f(t)$
The total energy per unit mass of a fluid particle is the sum of its microscopic internal energy $e$ and its macroscopic kinetic energy $\frac{1}{2}|\vec{v}|^2$. According to the First Law of Thermodynamics:
$$ \frac{d}{dt} E_{\text{total}} = \dot{W}_{\text{ext}} + \dot{Q}_{\text{ext}} $$

$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_f(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] = & -\int_{\Sigma_f(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_f(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_f(t)} \rho\vec{f}_m\cdot\vec{v} \, dV \\
& -\int_{\Sigma_f(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_f(t)} (Q_c + Q_r) \, dV
\end{aligned} \qquad \text{[Eq. 3.45]} $$

### For an Arbitrary Moving Control Volume $V_c(t)$
Applying the Reynolds Transport Theorem (Eq. 3.8):

$$ \begin{aligned}
\mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] + \int_{\Sigma_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right)[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma =} \\
\mathbf{-\int_{\Sigma_c(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m\cdot\vec{v} \, dV} \\
\mathbf{-\int_{\Sigma_c(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_c(t)} (Q_c + Q_r) \, dV}
\end{aligned} \qquad \text{[Eq. 3.46]} $$

### Term-by-Term Physical Breakdown
1. **Unsteady Accumulation:** Variation of the kinetic and internal energy stored in $V_c(t)$.
2. **Net Outgoing Convection:** Convective transport of enthalpy and kinetic energy crossing the surface with relative velocity $(\vec{v}-\vec{v}_c)$.
3. **Pressure Work ($-\int_{\Sigma_c} p\vec{v}\cdot\vec{n} d\sigma$):** Mechanical flow work exerted by the external pressure on the fluid as it enters or leaves the volume. Grouped with the convected internal energy $e$, it yields the **specific enthalpy** $h = e + p/\rho$ and the **total stagnation enthalpy** $h_0 = h + \frac{|\vec{v}|^2}{2}$.
4. **Work of Viscous Stresses ($\int_{\Sigma_c} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} d\sigma$):** Power transmitted by friction on moving boundaries (e.g. turbine blades) and viscous dissipation.
5. **Power of Body Forces ($\int_{V_c} \rho\vec{f}_m\cdot\vec{v} dV$):** Work done by gravity or centrifugal forces along the trajectories of the fluid particles.
6. **Heat Conduction at the Boundary ($-\int_{\Sigma_c} \vec{q}\cdot\vec{n} d\sigma$):** Molecular heat conducted through the wall according to Fourier's Law (active cooling of regenerative nozzles or thermal shock).
7. **Volumetric Sources ($Q_c, Q_r$):**
   * $Q_c$: Heat released by exothermic combustion chemical reactions per unit volume and time (burning of kerosene / $\text{LOX}-\text{LH}_2$ in thrust chambers).
   * $Q_r = -\nabla\cdot\vec{q}_r$: Volumetric heating or cooling by thermal radiation of incandescent gases.

## Total Energy: Complete Derivation Chain (Notes.pdf, Eqs. 3.39-3.46)

### Step 1: Origin of each term of the First Law (Eq. 3.45)

The total energy of a fluid volume is $\int_{V_f}\rho(e+|\vec{v}|^2/2)\,dV$. Its rate of change equals the power of the forces plus the heat added (First Law). Each contribution is built from an elementary power on a surface element $d\sigma$ or a volume element $dV$.

* **Surface forces.** The stress vector $(\bar{\bar{\tau}}\cdot\vec{n})\,d\sigma$ acts on material that moves with velocity $\vec{v}$, so its power is $\vec{v}\cdot\bar{\bar{\tau}}\cdot\vec{n}\,d\sigma$. With $\bar{\bar{\tau}}=-p\bar{\bar{I}}+\bar{\bar{\tau}}'$ and $\vec{v}\cdot(p\bar{\bar{I}})\cdot\vec{n}=p\,\vec{v}\cdot\vec{n}$, the total is $-\int p\,\vec{v}\cdot\vec{n}\,d\sigma+\int\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma$.
* **Body force.** The force $\rho\vec{f}_m\,dV$ has power $\rho\vec{f}_m\cdot\vec{v}\,dV$.
* **Heat conduction.** By Eqs. 3.41 and 3.43, $\vec{q}\cdot\vec{n}\,d\sigma$ is the conductive heat leaving through $d\sigma$ (its divergence is the heat loss per unit volume), so the heat added is $-\int\vec{q}\cdot\vec{n}\,d\sigma$.
* **Volumetric sources.** Chemical reaction and radiation add $\int(Q_c+Q_r)\,dV$.

Summing these contributions gives Eq. 3.45:

$$ \frac{d}{dt}\int_{V_f}\rho\Big(e+\frac{|\vec{v}|^2}{2}\Big)dV=-\int_{\Sigma_f}p\,\vec{v}\cdot\vec{n}\,d\sigma+\int_{\Sigma_f}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_f}\rho\vec{f}_m\cdot\vec{v}\,dV-\int_{\Sigma_f}\vec{q}\cdot\vec{n}\,d\sigma+\int_{V_f}(Q_c+Q_r)\,dV $$

*Eq. 3.45*

### Step 2: Transfer to a moving control volume (Eq. 3.46)

Apply Eq. 3.8 with $\phi=\rho(e+|\vec{v}|^2/2)$ to the left-hand side of Eq. 3.45 and evaluate the right-hand side on $\Sigma_c$ and $V_c$, which coincide with $\Sigma_f$ and $V_f$ at the instant considered. Moving the convective flux to the left gives

$$ \frac{d}{dt}\int_{V_c}\rho\Big(e+\frac{|\vec{v}|^2}{2}\Big)dV+\int_{\Sigma_c}\rho\Big(e+\frac{|\vec{v}|^2}{2}\Big)\big[(\vec{v}-\vec{v}_c)\cdot\vec{n}\big]d\sigma=-\int_{\Sigma_c}p\,\vec{v}\cdot\vec{n}\,d\sigma+\int_{\Sigma_c}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_c}\rho\vec{f}_m\cdot\vec{v}\,dV-\int_{\Sigma_c}\vec{q}\cdot\vec{n}\,d\sigma+\int_{V_c}(Q_c+Q_r)\,dV $$

*Eq. 3.46*

### Step 3: Flow work and specific enthalpy (extension)

**Extension, not in the Notes.** For a fixed control volume ($\vec{v}_c=\vec{0}$), move the pressure work to the left-hand side and write $p\,\vec{v}\cdot\vec{n}=(p/\rho)\,\rho\,\vec{v}\cdot\vec{n}$:

$$ \int_{\Sigma_0}\Big[\rho\Big(e+\frac{|\vec{v}|^2}{2}\Big)+p\Big]\vec{v}\cdot\vec{n}\,d\sigma=\int_{\Sigma_0}\rho\Big(e+\frac{p}{\rho}+\frac{|\vec{v}|^2}{2}\Big)\vec{v}\cdot\vec{n}\,d\sigma=\int_{\Sigma_0}\rho\Big(h+\frac{|\vec{v}|^2}{2}\Big)\vec{v}\cdot\vec{n}\,d\sigma $$

with $h=e+p/\rho$. The balance for a fixed volume becomes

$$ \int_{V_0}\frac{\partial}{\partial t}\Big[\rho\Big(e+\frac{|\vec{v}|^2}{2}\Big)\Big]dV+\int_{\Sigma_0}\rho\Big(h+\frac{|\vec{v}|^2}{2}\Big)\vec{v}\cdot\vec{n}\,d\sigma=\int_{\Sigma_0}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}\,d\sigma+\int_{V_0}\rho\vec{f}_m\cdot\vec{v}\,dV-\int_{\Sigma_0}\vec{q}\cdot\vec{n}\,d\sigma+\int_{V_0}(Q_c+Q_r)\,dV $$

For a moving boundary, $p\,\vec{v}\cdot\vec{n}=p\,(\vec{v}-\vec{v}_c)\cdot\vec{n}+p\,\vec{v}_c\cdot\vec{n}$. The first part joins the enthalpy flux in the same way and the second part is the work of the pressure on the moving boundary, which stays on the right-hand side.

### Step 4: Gravity and the total enthalpy $h_0$ (extension)

**Extension, not in the Notes.** For gravity with $z$ pointing upward, $\vec{f}_m=-\nabla(gz)$ (Eq. 3.14 with $U=gz$). In a steady flow, the continuity equation $\nabla\cdot(\rho\vec{v})=0$ (Eq. 4.5) lets the body-force power be written as a divergence:

$$ \rho\vec{f}_m\cdot\vec{v}=-\rho\vec{v}\cdot\nabla(gz)=-\nabla\cdot(\rho\,gz\,\vec{v})+gz\,\nabla\cdot(\rho\vec{v})=-\nabla\cdot(\rho\,gz\,\vec{v}) $$

Gauss' theorem converts the volume integral into $-\int_{\Sigma_0}\rho\,gz\,\vec{v}\cdot\vec{n}\,d\sigma$. Moving it to the left-hand side adds $gz$ inside the convective flux:

$$ \int_{\Sigma_0}\rho\,h_0\,\vec{v}\cdot\vec{n}\,d\sigma,\qquad h_0=h+\frac{|\vec{v}|^2}{2}+gz $$

### Step 5: Steady engineering energy equation (extension)

**Extension, not in the Notes.** For a steady flow in a fixed control volume, split the boundary into ports, stationary solid walls and moving blades.

* On stationary walls the no-slip condition gives $\vec{v}=\vec{0}$, so the pressure and viscous work vanish; the heat conducted through the walls defines $\dot Q=-\int_{\text{walls}}\vec{q}\cdot\vec{n}\,d\sigma+\int(Q_c+Q_r)\,dV$.
* On the moving blades of a machine, the (time-averaged) power of pressure and viscous forces on the fluid is defined as $\dot W_{\text{shaft}}$.
* At the ports, viscous work and conduction are negligible against convection (high Reynolds and Peclet numbers) and $h_0$, $\rho$, $\vec{v}$ are taken uniform, so $\int_{A_k}\rho h_0\,\vec{v}\cdot\vec{n}\,d\sigma=\dot m_k h_{0,k}$.

The balance of Step 4 then gives the form used in the engineering applications:

$$ \sum_{\text{out}}|\dot m|\,h_0-\sum_{\text{in}}|\dot m|\,h_0=\dot Q+\dot W_{\text{shaft}} $$

Dimensional check: each term has units $\mathrm{kg\,s^{-1}\cdot J\,kg^{-1}}=\mathrm{W}$.
