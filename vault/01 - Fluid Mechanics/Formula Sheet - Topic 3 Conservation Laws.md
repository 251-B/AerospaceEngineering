---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - formula-sheet
  - quick-reference
  - key-equations
  - conservation-laws
  - reynolds
dificultad: medium
---

# 📋 Master Formula Sheet: Topic 3 — Conservation Laws (Integral Form)

> **Official Reference:** *Notes.pdf* (Antonio L. Sánchez and Javier Rodríguez-Rodríguez, UC3M), Chapter 3: *Conservation Laws*, Pages 25–36.

---

## 📑 Complete Table of Fundamental Equations (Eqs. 3.1 to 3.46)

| Eq. | Mathematical Expression | Physical Meaning and Name | Hypothesis / Scope |
| :---: | :--- | :--- | :--- |
| **3.1** | $\Phi(t) = \int_{V_f(t)} \phi(\vec{x},t) dV$<br>$\phi = \rho, \, \rho\vec{v}, \, \rho\left(e + \frac{\|\vec{v}\|^2}{2}\right)$ | Definition of an extensive quantity from its intensive volumetric density $\phi$. | Closed material fluid system $V_f(t)$. |
| **3.2** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi dV\right] = \lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V_f(t+\Delta t)}\phi(t+\Delta t)dV - \int_{V_f(t)}\phi(t)dV\right]$ | Formal definition of the ordinary time derivative of the material fluid volume. | General. |
| **3.3** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V_f(t)}[\phi(t+\Delta t)-\phi(t)]dV + \int_{V_f(t+\Delta t)-V_f(t)}\phi(t+\Delta t)dV\right]$ | Splitting of the limit into an internal term and the incremental region swept by the boundary. | General. |
| **3.4** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\int_{V_f(t)}[\phi(t+\Delta t)-\phi(t)]dV = \int_{V_f(t)}\frac{\partial\phi}{\partial t}dV$ | Limit of the internal term: contribution of local unsteadiness (*unsteadiness*). | First-order Taylor. |
| **3.5** | $\lim_{\Delta t\to 0}\frac{1}{\Delta t}\int_{V_f(t+\Delta t)-V_f(t)}\phi(t+\Delta t)dV = \int_{\Sigma_f(t)}\phi \vec{v}\cdot\vec{n}d\sigma$ | Limit of the swept volume: net convective flux through the boundary surface $\Sigma_f(t)$. | Differential kinematics: $dV = (\vec{v}\Delta t)\cdot\vec{n}d\sigma$. |
| **3.6** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \int_{V_f(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_f(t)} \phi \, \vec{v}\cdot\vec{n} \, d\sigma$ | **Reynolds Transport Theorem (RTT)** for a material fluid volume $V_f(t)$. | Volume following the fluid particles. |
| **3.7** | $\frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] = \int_{V_c(t)} \frac{\partial \phi}{\partial t} \, dV + \int_{\Sigma_c(t)} \phi \, \vec{v}_c\cdot\vec{n} \, d\sigma$ | RTT applied to an arbitrary moving control volume $V_c(t)$ with boundary velocity $\vec{v}_c$. | Arbitrary moving geometry. |
| **3.8** | $\frac{d}{dt}\left[\int_{V_f(t)} \phi \, dV\right] = \frac{d}{dt}\left[\int_{V_c(t)} \phi \, dV\right] + \int_{\Sigma_c(t)} \phi \, (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma$ | **Universal RTT:** Connection between the material derivative and the moving control volume with relative velocity $(\vec{v} - \vec{v}_c)$. | Fundamental in integral analysis. |
| **3.9** | $\frac{d}{dt}\left[\int_{V_f(t)} \rho \, dV\right] = 0$ | Conservation of mass in a closed material volume. | Non-relativistic classical mechanics. |
| **3.10** | $\frac{d}{dt}\left[\int_{V_c(t)} \rho \, dV\right] + \int_{\Sigma_c(t)} \rho (\vec{v} - \vec{v}_c)\cdot\vec{n} \, d\sigma = 0$ | **Integral Mass Conservation (Continuity)** for an arbitrary moving control volume $V_c(t)$. | Applicable to any moving volume. |
| **3.11** | $\int_{V_0} \frac{\partial \rho}{\partial t} \, dV + \int_{\Sigma_0} \rho \vec{v}\cdot\vec{n} \, d\sigma = 0$ | Mass conservation for a control volume fixed in space ($V_0, \vec{v}_c = 0$). | Undeformable, stationary volume. |
| **3.12** | $d\vec{F}_m = \rho \vec{f}_m(\vec{x},t) \, dV$ | Volumetric (body) force acting on an elementary fluid particle. | Long-range forces. |
| **3.13** | $\vec{f}_m = \vec{g} - \vec{a}_0 - \frac{d\vec{\Omega}}{dt}\wedge\vec{x} - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) - 2\vec{\Omega}\wedge\vec{v}$ | Net body force in a non-inertial reference frame (gravity + 4 inertial forces). | Accelerated and rotating reference frame. |
| **3.14** | $\vec{g} - \vec{a}_0 - \vec{\Omega}\wedge(\vec{\Omega}\wedge\vec{x}) = -\nabla\left[-\vec{g}\cdot\vec{x} + \vec{a}_0\cdot\vec{x} - \frac{1}{2}\|\vec{\Omega}\wedge\vec{x}\|^2\right] = -\nabla U$ | Conservative character of gravity, uniform translation and centrifugal force deriving from the potential $U$. | Steady $\vec{a}_0$ and $\vec{\Omega}$. |
| **3.15** | $d\vec{F}_s = \vec{f}_n(\vec{n}, \vec{x}, t) \, d\sigma$ | Surface contact force (traction vector or stress $\vec{f}_n$) on an element $d\sigma$. | Short range (intermolecular origin). |
| **3.16** | $dA \vec{f}_n - dA_1 \vec{f}_1 - dA_2 \vec{f}_2 - dA_3 \vec{f}_3 = 0$ | Dynamic force equilibrium on the differential Cauchy tetrahedron in the limit $h \to 0$. | Order of magnitude: area $\gg$ volume. |
| **3.17** | $\vec{f}_n = n_1 \vec{f}_1 + n_2 \vec{f}_2 + n_3 \vec{f}_3 = \vec{n}\cdot\bar{\bar{\tau}} = \bar{\bar{\tau}}\cdot\vec{n}$ | **Cauchy's Postulate:** Linear dependence between the traction vector $\vec{f}_n$ and the tensor $\bar{\bar{\tau}}$. | Classical continuum. |
| **3.18** | $\bar{\bar{\tau}} = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{21} & \tau_{22} & \tau_{23} \\ \tau_{31} & \tau_{32} & \tau_{33}\end{bmatrix}$ | Component matrix of the Cauchy Stress Tensor. | Orthogonal Cartesian system. |
| **3.19** | $\vec{f}_n = \begin{bmatrix} \tau_{11} & \tau_{12} & \tau_{13} \\ \tau_{12} & \tau_{22} & \tau_{23} \\ \tau_{13} & \tau_{23} & \tau_{33}\end{bmatrix}\cdot\vec{n}, \quad \tau_{ij} = \tau_{ji}$ | **Symmetry of the stress tensor:** Proven by angular momentum balance on a cubic element ($dx\to 0$). | Absence of volumetric micro-couples. |
| **3.20** | $\bar{\bar{\tau}}\cdot\vec{n} = \lambda \vec{n}$ | Eigenvalue equation for the principal directions and stresses (zero shear stress). | General for any state of stress. |
| **3.21** | $|\bar{\bar{\tau}} - \lambda \bar{\bar{I}}| = 0$ | Secular or characteristic equation with 3 real, mutually orthogonal roots $(\lambda_1, \lambda_2, \lambda_3)$. | Guaranteed by the symmetry of $\bar{\bar{\tau}}$. |
| **3.22** | $\vec{F}_s = \int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} \, d\sigma$ | Global resultant of surface forces on a material surface $\Sigma$. | General. |
| **3.23** | $\int_\Sigma \bar{\bar{\tau}}\cdot\vec{n} \, d\sigma = \int_V (\nabla\cdot\bar{\bar{\tau}}) \, dV$ | Application of Gauss's Theorem: the divergence of the tensor $\nabla\cdot\bar{\bar{\tau}}$ is the surface force per unit volume. | Closed surface enclosing volume $V$. |
| **3.24** | $\rho dV \frac{D\vec{v}}{Dt} = (\nabla\cdot\bar{\bar{\tau}})dV + \rho\vec{f}_m dV$ | Newton's 2nd Law applied to a differential fluid element $dV$. | Infinitesimal fluid element. |
| **3.25** | $\rho \frac{D\vec{v}}{Dt} = \nabla\cdot\bar{\bar{\tau}} + \rho\vec{f}_m$ | **Cauchy differential equation for momentum**. | Valid for any continuum. |
| **3.26** | $\vec{f}_n = -p\vec{n}$ | Purely normal traction in a fluid at rest or in rigid-body motion. | Fluid at rest or without deformation ($\bar{\bar{T}}_d=0$). |
| **3.27** | $\bar{\bar{\tau}} = -p \bar{\bar{I}}$ | Hydrostatic stress tensor (isotropic, independent of orientation). | Static state or without shear. |
| **3.28** | $\bar{\bar{\tau}} = -p\bar{\bar{I}} + \bar{\bar{\tau}}'$ | Decomposition of the stress tensor into spherical thermodynamic pressure and the deviatoric viscous tensor $\bar{\bar{\tau}}'$. | General for any moving fluid. |
| **3.29** | $\tau'_{ij} = \alpha_{ijkl} \gamma_{kl}$ | Newtonian fluid hypothesis: linear constitutive relation between viscous stresses and strain rates. | Newtonian fluid. |
| **3.30** | $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \lambda(\nabla\cdot\vec{v})\bar{\bar{I}}$ | Navier-Poisson constitutive equation in terms of dynamic viscosity $\mu$ and second viscosity $\lambda$. | Isotropic Newtonian fluid. |
| **3.31** | $\bar{\bar{\tau}}' = 2\mu\bar{\bar{T}}_d + \left(\mu_B - \frac{2}{3}\mu\right)(\nabla\cdot\vec{v})\bar{\bar{I}}$ | **Canonical Navier-Poisson equation** in terms of the bulk viscosity $\mu_B = \lambda + \frac{2}{3}\mu$. | Stokes hypothesis: $\mu_B \approx 0 \implies \lambda = -\frac{2}{3}\mu$. |
| **3.32** | $\vec{F} = -\int_\Sigma p\vec{n}d\sigma + \int_\Sigma \bar{\bar{\tau}}'\cdot\vec{n}d\sigma$ | **Resultant aerodynamic force on a submerged body**: decomposed into pressure and viscous friction. | $\vec{n}$ pointing out of the body into the fluid. |
| **3.33** | $\vec{M}_{\vec{x}_0} = -\int_\Sigma (\vec{x}-\vec{x}_0)\wedge(p\vec{n})d\sigma + \int_\Sigma (\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n})d\sigma$ | **Resultant moment on a submerged body** about a reduction center $\vec{x}_0$. | Wetted surface $\Sigma$. |
| **4.2** (3.34 with 3.28) | $\frac{d}{dt}\left[\int_{V_f(t)}\rho\vec{v}dV\right] = -\int_{\Sigma_f(t)} p\vec{n}d\sigma + \int_{\Sigma_f(t)}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_f(t)}\rho\vec{f}_m dV$ | Newton's 2nd Law for a closed material fluid volume $V_f(t)$. | Fixed fluid mass. |
| **3.35** | $\frac{d}{dt}\left[\int_{V_c(t)}\rho\vec{v}dV\right] + \int_{\Sigma_c(t)}\rho\vec{v}[(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = -\int_{\Sigma_c(t)} p\vec{n}d\sigma + \int_{\Sigma_c(t)}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_c(t)}\rho\vec{f}_m dV$ | **Integral Momentum Conservation** for an arbitrary moving control volume $V_c(t)$. | Fundamental for thrust and aerodynamic forces. |
| **3.36** | $\int_{V_0}\frac{\partial(\rho\vec{v})}{\partial t}dV + \int_{\Sigma_0}\rho\vec{v}(\vec{v}\cdot\vec{n})d\sigma = -\int_{\Sigma_0} p\vec{n}d\sigma + \int_{\Sigma_0}\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_0}\rho\vec{f}_m dV$ | Momentum conservation for a control volume fixed in space ($V_0, \vec{v}_c = 0$). | Bearings, fixed nozzles, wind tunnels. |
| **3.37** | $\frac{d}{dt}\left[\int_{V_f(t)}\rho(\vec{x}-\vec{x}_0)\wedge\vec{v}dV\right] = -\int_{\Sigma_f}(\vec{x}-\vec{x}_0)\wedge(p\vec{n})d\sigma + \int_{\Sigma_f}(\vec{x}-\vec{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\vec{n})d\sigma + \int_{V_f}\rho(\vec{x}-\vec{x}_0)\wedge\vec{f}_m dV$ | Conservation of angular momentum for a material volume $V_f(t)$. | Material system of particles. |
| **3.38** | $\frac{d}{dt}\left[\int_{V_c}\rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}]dV\right] + \int_{\Sigma_c}\rho[(\vec{x}-\vec{x}_0)\wedge\vec{v}][(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = \sum \vec{M}_{\vec{x}_0, \text{ext}}$ | **Integral Angular Momentum Conservation** for a moving control volume $V_c(t)$. | Basis of the Euler equation in turbomachinery. |
| **3.39** | $d\dot{Q}_{\text{cond}} = q_n(\vec{n}, \vec{x}, t) \, d\sigma$ | Thermal power conducted through the differential element $d\sigma$ in direction $\vec{n}$. | Molecular conduction. |
| **3.40** | $q_n dA = q_1 dA_1 + q_2 dA_2 + q_3 dA_3$ | Balance of heat fluxes on the infinitesimal tetrahedron in the limit $h \to 0$. | Conduction in local equilibrium. |
| **3.41** | $q_n = \vec{q}\cdot\vec{n}$ | Thermal Cauchy relation: the scalar flux $q_n$ is the projection of the heat flux density vector $\vec{q}$. | Thermal continuum. |
| **3.42** | $\dot{Q}_{\text{cond}} = \int_\Sigma \vec{q}\cdot\vec{n} \, d\sigma$ | Total heat conducted through a finite surface $\Sigma$. | General. |
| **3.43** | $\int_\Sigma \vec{q}\cdot\vec{n}d\sigma = \int_V (\nabla\cdot\vec{q})dV$ | Gauss's Theorem: $\nabla\cdot\vec{q}$ represents the rate of conductive heat loss per unit volume. | Closed volume $V$. |
| **3.44** | $\vec{q} = -k\nabla T$ | **Fourier's Law of heat conduction**: linearity and inversion with the temperature gradient. | Isotropic continuum. |
| **3.45** | $\frac{d}{dt}\left[\int_{V_f(t)}\rho(e+\frac{\|\vec{v}\|^2}{2})dV\right] = -\int_{\Sigma_f}p\vec{v}\cdot\vec{n}d\sigma + \int_{\Sigma_f}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_f}\rho\vec{f}_m\cdot\vec{v}dV - \int_{\Sigma_f}\vec{q}\cdot\vec{n}d\sigma + \int_{V_f}(Q_c+Q_r)dV$ | **First Law of Thermodynamics** for a material volume $V_f(t)$ (total energy balance). | Closed material system. |
| **3.46** | $\frac{d}{dt}\left[\int_{V_c}\rho(e+\frac{\|\vec{v}\|^2}{2})dV\right] + \int_{\Sigma_c}\rho(e+\frac{\|\vec{v}\|^2}{2})[(\vec{v}-\vec{v}_c)\cdot\vec{n}]d\sigma = -\int_{\Sigma_c}p\vec{v}\cdot\vec{n}d\sigma + \int_{\Sigma_c}\vec{v}\cdot\bar{\bar{\tau}}'\cdot\vec{n}d\sigma + \int_{V_c}\rho\vec{f}_m\cdot\vec{v}dV - \int_{\Sigma_c}\vec{q}\cdot\vec{n}d\sigma + \int_{V_c}(Q_c+Q_r)dV$ | **Integral Total Energy Conservation** for an arbitrary moving control volume $V_c(t)$. | Master form of the energy balance. |
