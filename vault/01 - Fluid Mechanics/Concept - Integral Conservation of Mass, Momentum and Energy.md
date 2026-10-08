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

## 🌀 4. Integral Angular Momentum Equation (Notes.pdf, Eqs. 3.37–3.38)

The balance of the moment of momentum about a fixed point $\vec{x}_0$ for a moving control volume $V_c(t)$ is given by:

$$ \begin{aligned}
\mathbf{\frac{d}{dt}\left[\int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}] \, dV\right] + \int_{\Sigma_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma =} \\
\mathbf{-\int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma + \int_{V_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{f}_m] \, dV}
\end{aligned} \qquad \text{[Eq. 3.38]} $$

### Application to Aerospace Turbomachinery: Euler Equation
In the rotor of an axial compressor or gas turbine rotating at constant angular velocity $\vec{\Omega}$, the torque exerted by the fluid on the rotor in steady regime is:
$$ T_{\text{shaft}} = \dot{m} (r_2 v_{\theta 2} - r_1 v_{\theta 1}) $$
Multiplying by $\Omega$, the mechanical power exchanged per unit mass flow rate is the **Euler turbomachinery formula**:
$$ w_{\text{Euler}} = u_2 v_{\theta 2} - u_1 v_{\theta 1} $$
where $u = \Omega r$ is the blade entrainment (blade-speed) velocity and $v_\theta$ is the tangential component of the fluid velocity.

---

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
