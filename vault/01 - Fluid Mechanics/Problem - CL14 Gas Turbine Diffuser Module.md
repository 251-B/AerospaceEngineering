---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - difusor
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL14.pdf"
id: "cl14"
pill: "CL14: Diffuser Module"
tags_html:
  - "Stator"
  - "Swirl removal"
  - "Angular momentum"
  - "Perfect gas"
---

# Problem CL14: Gas-Turbine Diffuser Module: Exit State, Force and Torque

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The diffuser module at the exit of a gas turbine consists of a **fixed** aerofoil cascade (stator), of inner and outer radii $R_i$ and $R_o$, respectively, together with a conical diffuser, as depicted in the figure of CL14.pdf. The gas enters the module with velocity field $\bar{v}_1 = u_1\bar{e}_z + u_\theta\bar{e}_\theta$, having both axial and azimuthal components, pressure $p_1$ and density $\rho_1$, and leaves the module with a purely axial velocity field $\bar{v}_2 = u_2\bar{e}_z$, pressure $p_2$ and density $\rho_2$. For the analysis of the problem, one may introduce the following assumptions:

- The effect of gravity is entirely negligible.
- Flow properties at the entrance and exit sections are uniform.
- The air around the casing is at rest with uniform pressure $p_a$.
- The working gas behaves as a perfect gas (gas constant $R_g$, specific heat ratio $\gamma$).
- All the inner walls are adiabatic.

With the above simplifications, write the equations that determine the values of $\rho_2$ and $u_2$, as well as the net force, $F$, and torque, $M$, acting on the diffuser module, in terms of the known quantities ($p_a$, $p_1$, $\rho_1$, $p_2$, $u_1$, $u_\theta$, $R_i$, $R_o$, $\gamma$ and $R_g$).

![[attachments/FM-T3/cl14-statement.svg]]
*Statement figure (redrawn from CL14.pdf, p. 1): front view of the inlet ($u_1$, $u_\theta$, $p_1$, $\rho_1$) and axial section of the module: fixed stator between $R_i$ and $R_o$, conical diffuser, purely axial exit $u_2$, $p_2$, $\rho_2$*

Source: CL14.pdf (pages 1-4, quiz of Nov 5, 2012, with typed solution). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, axisymmetric; neglect $\bar{g}$; uniform properties at both sections; perfect gas, $h = c_pT = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; adiabatic walls; the module is fixed (no work).
- Inlet: annulus $R_i < r < R_o$ (area $A_1 = \pi(R_o^2 - R_i^2)$). Exit: full disc $r < R_o$ (area $A_2 = \pi R_o^2$).
- The ambient air at $p_a$ touches only the outer cylindrical casing, whose normal is radial: by axisymmetry it gives no axial force and no axial torque ($\bar{F}_{ext} = 0$, $\bar{M}_{ext} = 0$). Absolute pressures are therefore used, as in the official solution (the gauge form would wrongly add $p_a\pi R_i^2$ on the hub face, which is not in contact with the ambient air).
- Data: $[p_a,\ p_1,\ \rho_1,\ p_2,\ u_1,\ u_\theta,\ R_i,\ R_o,\ \gamma,\ R_g]$. Unknowns: $[\rho_2,\ u_2,\ F,\ M]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $u_1$, $u_\theta$ | axial and azimuthal inlet velocity | m/s |
| $p_1$, $\rho_1$; $p_2$, $\rho_2$ | inlet and exit states | Pa, kg/m$^3$ |
| $u_2$ | exit axial velocity | m/s |
| $R_i$, $R_o$ | inner and outer radii | m |
| $F$, $M$ | axial force and torque on the module | N, N$\cdot$m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the module; right-handed cylindrical basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$, $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_z$, with $\bar{e}_z$ along the flow; origin on the axis.
- Surfaces (as in the official solution): $\Sigma_{in}$ (inlet annulus, $\bar{n} = -\bar{e}_z$), $\Sigma_{out}$ (exit disc, $\bar{n} = +\bar{e}_z$), $\Sigma_w$ (inner wall of the casing and outer wall of the cone) and $\Sigma_a$ (surfaces around the stator aerofoils). All are fixed.

![[attachments/FM-T3/cl14-cv.svg]]
*Control volume of the solution (axial section): $\Sigma_{in}$ (inlet annulus, $\bar{n} = -\bar{e}_z$), $\Sigma_{out}$ (exit disc, $\bar{n} = +\bar{e}_z$), $\Sigma_w$ (inner wall of the casing and outer wall of the cone) and $\Sigma_a$ (around the stator aerofoils); all are fixed*

$$ \boxed{\,F\,\bar{e}_z = \int_{\Sigma_w,\Sigma_a}\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma + \underbrace{\bar{F}_{ext}}_{0}\,} $$

$$ \boxed{M\,\bar{e}_z = \int_{\Sigma_w,\Sigma_a}\bar{x}\wedge\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma + \underbrace{\bar{M}_{ext}}_{0}\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_{in}$ | $-\rho_1u_1\pi(R_o^2 - R_i^2)$ |
| $\Sigma_{out}$ | $+\rho_2u_2\pi R_o^2$ |
| $\Sigma_w,\ \Sigma_a$ | $0$ |

$$ \boxed{\,\rho_1u_1\pi(R_o^2 - R_i^2) = \rho_2u_2\pi R_o^2 = G\,} \tag{1} $$

**Linear momentum, axial component (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,n_z\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_{in}$ | $-\rho_1u_1^2\pi(R_o^2 - R_i^2)$ | $+p_1\pi(R_o^2 - R_i^2)$ | $0$ (uniform) |
| $\Sigma_{out}$ | $+\rho_2u_2^2\pi R_o^2$ | $-p_2\pi R_o^2$ | $0$ (uniform) |
| **$\Sigma_w,\ \Sigma_a$** (boxed) | $0$ | $-\int p\,n_z\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$ |

Boxed terms: the force of the walls on the gas, $-F$ (with $\bar{F}_{ext} = 0$). The swirl gives no axial momentum flux.

$$ \boxed{\,F = \pi(R_o^2 - R_i^2)\left(p_1 + \rho_1u_1^2\right) - \pi R_o^2\left(p_2 + \rho_2u_2^2\right)\,} \tag{2} $$

**Angular momentum, axial component (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge p\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})_z\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $\text{pressure and viscous moments}$ |
| :--- | :--- | :--- |
| $\Sigma_{in}$ | $\int_{R_i}^{R_o}\rho_1\,(ru_\theta)(-u_1)\,2\pi r\,dr = -\frac{2\pi}{3}\rho_1u_1u_\theta(R_o^3 - R_i^3)$ | $0$ ($\bar{x}\wedge\bar{e}_z$ has no $z$ component) |
| $\Sigma_{out}$ | $0$ (no swirl) | $0$ |
| **$\Sigma_w,\ \Sigma_a$** (boxed) | $0$ | $-M$ |

On $\Sigma_{in}$, $\bar{x} = r\bar{e}_r + z\bar{e}_z$ and the $z$ component of $\bar{x}\wedge(u_1\bar{e}_z + u_\theta\bar{e}_\theta)$ is $ru_\theta$ (from $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_z$). The antiderivative of $r^2$ is $r^3/3$; Barrow's rule between $R_i$ and $R_o$ gives $(R_o^3 - R_i^3)/3$.

$$ \boxed{\,M = \frac{2\pi}{3}\,\rho_1u_1u_\theta\left(R_o^3 - R_i^3\right)\,} \tag{3} $$

**Total energy (Notes Eq. 3.46; $Q_R \equiv Q_c + Q_r$ is the volumetric heat release)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_{in}$ | $-G\left(e_1 + \tfrac{u_1^2 + u_\theta^2}{2}\right)$ | $+p_1u_1\pi(R_o^2 - R_i^2)$ | $0$ | $0$ |
| $\Sigma_{out}$ | $+G\left(e_2 + \tfrac{u_2^2}{2}\right)$ | $-p_2u_2\pi R_o^2$ | $0$ | $0$ |
| $\Sigma_w,\ \Sigma_a$ | $0$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) | $0$ (adiabatic) |

Using $G = \rho_1u_1\pi(R_o^2 - R_i^2) = \rho_2u_2\pi R_o^2$ from (1), the pressure-work terms are $p_1u_1\pi(R_o^2 - R_i^2) = G\,p_1/\rho_1$ and $p_2u_2\pi R_o^2 = G\,p_2/\rho_2$. Moving them to the left and dividing by $G$, each side contains $e + p/\rho = c_pT = \frac{\gamma}{\gamma - 1}\frac{p}{\rho}$ (perfect gas):

$$ \boxed{\,\frac{\gamma}{\gamma - 1}\frac{p_1}{\rho_1} + \frac{u_1^2 + u_\theta^2}{2} = \frac{\gamma}{\gamma - 1}\frac{p_2}{\rho_2} + \frac{u_2^2}{2}\,} \tag{4} $$

(1) and (4) give $\rho_2$ and $u_2$; then (2) gives $F$ and (3) gives $M$ directly; $T_2 = p_2/(\rho_2R_g)$ from the equation of state.

> [!warning] Discrepancy with the official solution (sign of the torque)
> CL14.pdf uses $\bar{x}\wedge\bar{e}_\theta = -r\bar{e}_z$ and obtains $M = -\frac{2\pi}{3}\rho_1u_1u_\theta(R_e^3 - R_i^3)$ (it calls the outer radius $R_e$). With the right-handed basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$ one has $\bar{e}_r\wedge\bar{e}_\theta = +\bar{e}_z$, so $\bar{x}\wedge\bar{e}_\theta = +r\bar{e}_z$ and the sign is the one in (3). The magnitude is the same; physically, the torque of the gas on the stator has the sense of the incoming swirl, since the stator removes it. The computed sign is kept.

## Phase 4: Interpretation, Limits and Dimensional Check

- (4): the stagnation enthalpy is conserved; the kinetic energy of the swirl, $u_\theta^2/2$, is recovered as enthalpy (pressure and temperature) downstream.
- For $u_\theta = 0$ there is nothing to remove and $M = 0$. $M$ is the torque that the mounting of the stator must withstand.
- Dimensions (SI): $[(p + \rho u^2)R^2] = \text{N}$; $[\rho u_1u_\theta R^3] = \text{N}\cdot\text{m}$.
- Numerical illustration (hypothetical data, extension): $p_1 = 1.2\times10^5$ Pa, $\rho_1 = 1.1$ kg/m$^3$, $u_1 = 150$ m/s, $u_\theta = 80$ m/s, $p_2 = 1.3\times10^5$ Pa, $R_i = 0.2$ m, $R_o = 0.5$ m, $\gamma = 1.4$: eliminating $\rho_2 = G/(\pi R_o^2u_2)$ in (4) gives a quadratic in $u_2$ with positive root $u_2 = 118.57$ m/s, $\rho_2 = 1.1689$ kg/m$^3$; then $F = -19512$ N (the module is pushed upstream by the pressure rise) and $M = 3234.6$ N$\cdot$m.
