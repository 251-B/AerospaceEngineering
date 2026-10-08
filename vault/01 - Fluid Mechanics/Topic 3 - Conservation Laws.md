---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws (Integral Form)"
fuentes:
  - "Notes.pdf (Sánchez & Rodríguez-Rodríguez, UC3M), Chapter 3, pp. 25-36"
tags:
  - moc-topic
  - fluid-mechanics
  - conservation-laws
  - reynolds-transport
  - second-year
dificultad: high
---

# 🌊 Topic 3: Conservation Laws (Integral Form)

> **Topic objective:** Establish the fundamental macroscopic balances of continuum mechanics applied to fluids. The Reynolds Transport Theorem (RTT) is derived, connecting the time derivative of an extensive quantity in a material or fluid volume $V_f(t)$ with its evolution in an arbitrary moving control volume $V_c(t)$ or a fixed one $V_0$. From the physical principles of mass conservation, momentum balance (Newton's 2nd Law), angular momentum and the 1st Law of Thermodynamics (total energy), the global integral equations governing fluid systems and submerged bodies in aerospace engineering are formulated (rocket thrust, turbine engines, aerodynamic forces and thermal balances).

---

## 📑 Table of Contents of Chapter 3

1. [[01 - Fluid Mechanics/Concept - Reynolds Transport Theorem|1. Introduction and the Reynolds Transport Theorem (RTT)]]
   * Extensive and intensive quantities: $\phi = \rho, \rho\vec{v}, \rho(e + v^2/2)$.
   * Rigorous mathematical derivation by passage to the limit $\Delta t \to 0$: splitting into an unsteadiness term and a convective flux through the boundary.
   * Formulation for a material fluid volume $V_f(t)$ and extension to an arbitrary moving control volume $V_c(t)$ with boundary velocity $\vec{v}_c(\vec{x},t)$.
   * Canonical case of the control volume fixed in space ($V_0, \vec{v}_c = 0$).

2. [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|2. Integral Mass Conservation (Continuity)]]
   * Conservation principle for a fluid volume $V_f(t)$: $\frac{d}{dt}\int_{V_f}\rho dV = 0$.
   * Integral equation for a moving control volume $V_c(t)$ and a fixed one $V_0$.
   * Limiting cases: steady flow and incompressible fluid ($\rho = \text{const}$). Mass flow rate balance $\sum \dot{m}_{\text{in}} = \sum \dot{m}_{\text{out}}$.

3. [[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|3. Body (Mass) and Surface Forces]]
   * Classification by range of action: long range (body forces $\rho\vec{f}_m dV$, gravity, non-inertial systems with entrainment acceleration $\vec{a}_0$, angular $\dot{\vec{\Omega}}\wedge\vec{x}$, centrifugal and Coriolis) vs short range (surface forces of molecular origin).
   * Potential of conservative body forces: $\vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla U$.
   * Traction vector or surface stress: $\vec{f}_n(\vec{n}, \vec{x}, t)$.

4. [[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|4. The Cauchy Stress Tensor]]
   * Cauchy's postulate and the infinitesimal tetrahedron: proof of the linear dependence $\vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}$.
   * Symmetry of the stress tensor ($\tau_{ij} = \tau_{ji}$) from the angular momentum balance on an infinitesimal cubic element ($dx\to 0$).
   * Principal stress directions and real eigenvalues: $|\bar{\bar{\tau}} - \lambda\bar{\bar{I}}| = 0$.
   * Resultant of surface forces on a finite volume and application of Gauss's theorem: $\int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} d\sigma = \int_V \nabla\cdot\bar{\bar{\tau}} dV$.
   * Balance on a fluid element and preliminary differential momentum equation: $\rho \frac{D\vec{v}}{Dt} = \nabla\cdot\bar{\bar{\tau}} + \rho\vec{f}_m$.

5. [[01 - Fluid Mechanics/Concept - Navier-Poisson Constitutive Equation|5. Navier-Poisson Constitutive Equation (Newtonian Fluids)]]
   * Fluid at rest or in rigid translation/rotation: hydrostatic state $\bar{\bar{\tau}} = -p\bar{\bar{I}}$.
   * General decomposition: $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$, where $\bar{\bar{\tau}}'$ is the viscous stress tensor.
   * Isotropic Newtonian fluid hypothesis: linear constitutive relation $\tau'_{ij} = \alpha_{ijkl} \gamma_{kl}$.
   * Coefficients of dynamic viscosity $\mu$ and second viscosity $\lambda$: $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \lambda(\nabla\cdot\vec{v})\bar{\bar{I}}$.
   * Bulk viscosity $\mu_B = \lambda + \frac{2}{3}\mu$ and the Stokes hypothesis ($\mu_B \approx 0 \implies \lambda = -2/3\mu$).
   * Thermal behaviour of viscosity: gases ($\mu \propto T^{1/2}$) vs liquids ($\mu$ decreases markedly with $T$).

6. [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|6. Forces and Moments on Submerged Bodies]]
   * Net aerodynamic/hydrodynamic force $\vec{F}$ on a submerged body with wetted surface $\Sigma$: split into a normal pressure integral and a tangential friction integral.
   * Net aerodynamic/hydrodynamic moment $\vec{M}_{x_0}$ about a reference point $\vec{x}_0$.
   * Lift ($L$), drag ($D$) and pitching moment ($M$).

7. [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|7. Integral Momentum Equation]]
   * Newton's 2nd Law for a fluid volume $V_f(t)$: $\frac{d}{dt}\int_{V_f}\rho\vec{v}dV = \vec{F}_{\text{ext}}$.
   * General equation for an arbitrary moving control volume $V_c(t)$ and a fixed one $V_0$.
   * Rigorous term-by-term physical interpretation: local accumulation rate, net outgoing convective flux, surface pressure forces, tangential viscous stresses and volumetric body forces.
   * Canonical aerospace applications: computation of the propulsive thrust of rockets and turbojets, force on blades and jet deflection.

8. [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|8. Integral Angular Momentum Equation]]
   * Conservation of angular momentum for $V_f(t)$ and $V_c(t)$ about a point $\vec{x}_0$.
   * Euler equation for turbomachinery: specific power and torque transmitted in aircraft rotors, compressors and turbines.

9. [[01 - Fluid Mechanics/Concept - Fourier's Law and Heat Conduction|9. Heat Transfer by Conduction and Fourier's Law]]
   * Heat flux per unit area $q_n(\vec{n}, \vec{x}, t)$.
   * Thermal Cauchy tetrahedron and derivation of the heat flux density vector $\vec{q}$: $q_n = \vec{q}\cdot\vec{n}$.
   * Conductive heat loss in a closed volume: $\int_\Sigma \vec{q}\cdot\vec{n}d\sigma = \int_V \nabla\cdot\vec{q} dV$.
   * Fourier's Law: $\vec{q} = -k\nabla T$.
   * Thermal conductivity $k(T)$, thermal diffusivity $\alpha = k/(\rho c_p)$, and Prandtl number $\mathrm{Pr} = \nu/\alpha$.
   * Orders of magnitude in air ($\mathrm{Pr}\approx 0.72$), water ($\mathrm{Pr}\sim 2-8$), liquid metals ($\mathrm{Pr}\ll 1$) and aerospace lubricating oils ($\mathrm{Pr}\gg 1$).

10. [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|10. Integral Total Energy Conservation Equation]]
    * 1st Law of Thermodynamics for a material volume $V_f(t)$: rate of change of total energy (kinetic + internal).
    * Power of external forces: work of normal pressure, work of viscous stresses and work of body forces.
    * Heat transferred: thermal conduction at the boundary ($\vec{q}\cdot\vec{n}$) and internal volumetric heat sources ($Q_c$: combustion chemical reactions, $Q_r$: thermal radiation).
    * General integral equation for a moving control volume $V_c(t)$ and simplification for fixed control volumes in aeronautical engineering.

11. [[01 - Fluid Mechanics/Formula Sheet - Topic 3 Conservation Laws|11. Complete Formula Sheet of Equations (3.1 to 3.46)]]
    * Complete table of equations with cross-references, operating hypotheses and detailed physical meaning.

---

## 📚 Fundamental Equations of the Chapter (Notes.pdf, Eqs. 3.1–3.46)

### 1. Reynolds Transport Theorem (RTT)
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.6]} $$
$$ \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.7]} $$
$$ \frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.8]} $$

### 2. Mass Conservation (Continuity Equation)
$$ \frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0 \qquad \text{[Eq. 3.10]} $$
$$ \int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \, \vec{v}\cdot\vec{n} \, d\sigma = 0 \qquad \text{[Eq. 3.11]} $$

### 3. Body Forces, Cauchy Stress and Constitutive Equation
$$ \vec{f}_m = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v} \qquad \text{[Eq. 3.13]} $$
$$ \vec{f}_n = \bar{\bar{\tau}}\cdot\vec{n}, \quad \tau_{ij} = \tau_{ji}, \quad |\bar{\bar{\tau}} - \lambda\bar{\bar{I}}| = 0 \qquad \text{[Eqs. 3.17, 3.19, 3.21]} $$
$$ \bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}' = -p\bar{\bar{I}} + 2\mu\bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\bar{\bar{I}} \qquad \text{[Eqs. 3.28, 3.31]} $$

### 4. Forces on Submerged Bodies
$$ \vec{F} = -\int_\Sigma p\vec{n} \, d\sigma + \int_\Sigma \bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma \qquad \text{[Eq. 3.32]} $$
$$ \vec{M} = -\int_\Sigma (\vec{x} - \vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_\Sigma (\vec{x} - \vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma \qquad \text{[Eq. 3.33]} $$

### 5. Conservation of Momentum and Angular Momentum
$$ \frac{d}{dt}\left[\int_{V_c(t)} \rho\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = -\int_{\Sigma_c(t)} p\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m \, dV \qquad \text{[Eq. 3.35]} $$
$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_c(t)} \rho(\vec{x}-\vec{x}_0)\wedge\vec{v} \, dV\right] + \int_{\Sigma_c(t)} \rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = \\
-\int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(p\vec{n}) \, d\sigma + \int_{\Sigma_c(t)} (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n}) \, d\sigma + \int_{V_c(t)} \rho(\vec{x}-\vec{x}_0)\wedge\vec{f}_m \, dV
\end{aligned} \qquad \text{[Eq. 3.38]} $$

### 6. Fourier's Law and Total Energy Conservation
$$ \vec{q} = -k\nabla T, \quad q_n = \vec{q}\cdot\vec{n}, \quad \mathrm{Pr} = \frac{\nu}{\alpha} = \frac{\mu c_p}{k} \qquad \text{[Eqs. 3.41, 3.44]} $$
$$ \begin{aligned}
\frac{d}{dt}\left[\int_{V_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right) dV\right] + \int_{\Sigma_c(t)} \rho\left(e + \frac{|\vec{v}|^2}{2}\right)[(\vec{v}-\vec{v}_c)\cdot\vec{n}] \, d\sigma = \\
-\int_{\Sigma_c(t)} p\vec{v}\cdot\vec{n} \, d\sigma + \int_{\Sigma_c(t)} \vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n} \, d\sigma + \int_{V_c(t)} \rho\vec{f}_m\cdot\vec{v} \, dV - \int_{\Sigma_c(t)} \vec{q}\cdot\vec{n} \, d\sigma + \int_{V_c(t)} (Q_c + Q_r) \, dV
\end{aligned} \qquad \text{[Eq. 3.46]} $$

---

## Derivation Chain of the Chapter (where each step is proved)

Every integral law of this chapter follows from one kinematic identity and one physical principle. The full step-by-step derivations, with the equation numbers of Notes.pdf and with every extension marked as such, are in the concept notes:

1. Reynolds Transport Theorem, Eqs. 3.2 to 3.8 (limit definition, Taylor expansion, swept shell, subtraction of the two volumes): [[01 - Fluid Mechanics/Concept - Reynolds Transport Theorem|Concept: Reynolds Transport Theorem]].
2. Mass: Eq. 3.9 plus Eq. 3.8 gives Eq. 3.10, the fixed-volume case gives Eq. 3.11, and Gauss' theorem with the arbitrary-volume argument gives the differential form (Notes, Eqs. 4.4 to 4.7): [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|Concept: Integral Conservation of Mass, Momentum and Energy]].
3. Momentum: Newton's law with the stress tensor (Eq. 3.34), then Eq. 3.8 gives Eq. 3.35 and Eq. 3.36, and the local form follows from Eq. 4.9 and continuity. Same note.
4. Angular momentum: Eq. 3.37, its consistency with the symmetry of the stress tensor, Eq. 3.38 and the Euler turbomachinery equation. Same note.
5. Energy: origin of each power and heat term (Eq. 3.45), Eq. 3.46, flow work, enthalpy and the engineering energy equation. Same note.
6. Stress tensor: Cauchy tetrahedron (Eqs. 3.16 to 3.19), symmetry, principal stresses, Gauss' theorem and Eq. 3.25, and the wall shear stress: [[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|Concept: Cauchy Stress Tensor and Body Forces]]. The Navier-Poisson relation (Eqs. 3.29 to 3.31) is derived in [[01 - Fluid Mechanics/Concept - Navier-Poisson Constitutive Equation|Concept: Navier-Poisson Constitutive Equation]].

The logical order is: Eq. 3.8 (kinematics) combined with the laws of mass, momentum, angular momentum and energy gives Eqs. 3.10, 3.35, 3.38 and 3.46; the stress tensor of item 6 supplies the surface forces that appear in the last three.

---

## 🔗 Linked Concept Notes
- [[01 - Fluid Mechanics/Concept - Reynolds Transport Theorem|Concept: Reynolds Transport Theorem (RTT)]]
- [[01 - Fluid Mechanics/Concept - Stress Tensor and Cauchy Principle|Concept: Cauchy Stress Tensor and Body Forces]]
- [[01 - Fluid Mechanics/Concept - Navier-Poisson Constitutive Equation|Concept: Navier-Poisson Constitutive Equation]]
- [[01 - Fluid Mechanics/Concept - Fourier's Law and Heat Conduction|Concept: Fourier's Law, Conduction and Prandtl Number]]
- [[01 - Fluid Mechanics/Concept - Integral Conservation of Mass, Momentum and Energy|Concept: Integral Conservation of Mass, Momentum and Energy]]
- [[01 - Fluid Mechanics/Formula Sheet - Topic 3 Conservation Laws|Master Formula Sheet: Conservation Laws (Eqs. 3.1 to 3.46)]]
