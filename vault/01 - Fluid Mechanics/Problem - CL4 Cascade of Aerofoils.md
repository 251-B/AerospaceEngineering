---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - cascada
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL4.pdf"
---

# Problem CL4: Cascade of Aerofoils: Downstream State

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].

## Statement

A planar uniform stream of air with pressure $p_1$, density $\rho_1$ and velocity $\mathbf{v}_1 = v_{1x}\mathbf{e}_x$ flows past an array of aerofoils with vertical separation $L$, exerting on each one a force (per unit length) given by $\mathbf{F} = F_x\mathbf{e}_x + F_y\mathbf{e}_y$. Assuming that the aerofoils are thermally insulated and neglecting the effect of gravity, write the equations that determine the values of the pressure $p_2$, density $\rho_2$ and velocity $\mathbf{v}_2 = v_{2x}\mathbf{e}_x + v_{2y}\mathbf{e}_y$ for the uniform stream found sufficiently far downstream.

Source: CL4.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Steady planar flow of air through an infinite array of identical aerofoils, equally spaced by $L$ in the $y$ direction; the flow is periodic with period $L$. Far upstream (section 1) and far downstream (section 2) the flow is uniform.
- No gravity; the aerofoils are thermally insulated (adiabatic); viscous stresses and heat conduction are negligible in the uniform sections 1 and 2.
- Perfect gas with specific heat ratio $\gamma$: the specific enthalpy is $h = e + p/\rho = \dfrac{\gamma}{\gamma - 1}\dfrac{p}{\rho}$. This is the assumption used in the official solution; the statement does not give $\gamma$.
- $\mathbf{F}$ is the force that the air exerts on each aerofoil, per unit length normal to the figure, so $[F_x/L]$ is a pressure. There are four unknowns, $p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$, and therefore four equations are needed: mass, two components of momentum and energy.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $p_1$, $\rho_1$, $v_{1x}$ | upstream state (data) | Pa, kg/m$^3$, m/s |
| $p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$ | downstream state (unknowns) | Pa, kg/m$^3$, m/s |
| $L$ | vertical separation (pitch) of the aerofoils | m |
| $F_x$, $F_y$ | force on each aerofoil per unit length | N/m |
| $\gamma$ | ratio of specific heats | 1 |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame fixed to the array, Cartesian basis $(\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z)$, $\mathbf{e}_x$ along the incoming stream and $\mathbf{e}_y$ along the array.
- Fixed control volume (one period): $\Sigma_1$ (section far upstream, height $L$, $\mathbf{n} = -\mathbf{e}_x$), $\Sigma_2$ (section far downstream, height $L$, $\mathbf{n} = +\mathbf{e}_x$), the two stream surfaces $\Sigma_3$ (top) and $\Sigma_4$ (bottom), and the surface of the aerofoil $\Sigma_5$. $\mathbf{v}_c = 0$, so Eqs. 3.11, 3.36 and 3.46 apply with $\mathbf{v}_c = 0$.
- Periodicity: $\Sigma_4$ is $\Sigma_3$ translated by $-L\,\mathbf{e}_y$, and the outward normals are opposite at corresponding points ($\mathbf{n}_4 = -\mathbf{n}_3$). Therefore the integral over $\Sigma_3 \cup \Sigma_4$ of any periodic field times the normal vanishes: pressure force, viscous force, heat flux and work of viscous stresses.
- On the stream surfaces $\mathbf{v}\cdot\mathbf{n} = 0$ and on the aerofoil $\mathbf{v} = 0$ (no slip) with $\mathbf{q}\cdot\mathbf{n} = 0$ (insulated). The force of the aerofoil on the fluid is $-\mathbf{F}$ per unit length.

## Phase 3: Step-by-Step Derivation

### 3.1 Mass

Why this tool: Notes Eq. 3.11 with $\partial/\partial t = 0$. Only $\Sigma_1$ and $\Sigma_2$ are crossed by the flow, each of height $L$ per unit length:

$$ -\rho_1 v_{1x}L + \rho_2 v_{2x}L = 0 \;\Longrightarrow\; \boxed{\,\rho_1\,v_{1x} = \rho_2\,v_{2x}\,}. \tag{E1} $$

Denote by $\dot m' \equiv \rho_1 v_{1x}L$ the mass flow per unit length through one period.

### 3.2 Linear momentum, components $x$ and $y$

Why this tool: the force $\mathbf{F}$ on the aerofoil enters only through the momentum balance (Notes Eq. 3.36). Left-hand side, using (E1) and $v_{1y} = 0$:

$$ \int_{\Sigma_c}\rho\,\mathbf{v}\,(\mathbf{v}\cdot\mathbf{n})\,d\sigma = \left(-\rho_1 v_{1x}^2 L + \rho_2 v_{2x}^2 L\right)\mathbf{e}_x + \rho_2 v_{2y}v_{2x}L\,\mathbf{e}_y = \dot m'\left[(v_{2x} - v_{1x})\,\mathbf{e}_x + v_{2y}\,\mathbf{e}_y\right]. $$

Right-hand side: on $\Sigma_1$, $-p_1(-\mathbf{e}_x)L = p_1L\,\mathbf{e}_x$; on $\Sigma_2$, $-p_2L\,\mathbf{e}_x$; the contributions of $\Sigma_3$ and $\Sigma_4$ cancel by periodicity; viscous stresses are negligible on $\Sigma_1$ and $\Sigma_2$; on $\Sigma_5$ the force on the fluid is $-\mathbf{F}$. Component by component:

$$ \dot m'\,(v_{2x} - v_{1x}) = (p_1 - p_2)\,L - F_x \;\Longrightarrow\; \boxed{\,\frac{F_x}{L} = p_1 - p_2 + \rho_1 v_{1x}\,(v_{1x} - v_{2x})\,} \tag{E2} $$

$$ \dot m'\,v_{2y} = -F_y \;\Longrightarrow\; \boxed{\,\frac{F_y}{L} = -\rho_1\,v_{1x}\,v_{2y}\,} \tag{E3} $$

### 3.3 Total energy

Why this tool: $p_2$ and $\rho_2$ are linked by the thermal state of the gas, which only the energy balance (Notes Eq. 3.46) provides. Steady, no gravity, no volumetric heat: the convective flux of $e + v^2/2$ plus the pressure work $p\,\mathbf{v}\cdot\mathbf{n}$ combine into the flux of $\rho\left(h + v^2/2\right)$.

On $\Sigma_3$ and $\Sigma_4$: $\mathbf{v}\cdot\mathbf{n} = 0$, and conduction and viscous work cancel by periodicity. On $\Sigma_5$: $\mathbf{v} = 0$ (no work) and $\mathbf{q}\cdot\mathbf{n} = 0$. On $\Sigma_1$ and $\Sigma_2$: viscous work and conduction are negligible. What remains is

$$ \int_{\Sigma_1 + \Sigma_2}\rho\left(h + \frac{v^2}{2}\right)(\mathbf{v}\cdot\mathbf{n})\,d\sigma = 0 \;\Longrightarrow\; \dot m'\left[\left(h_2 + \frac{v_{2x}^2 + v_{2y}^2}{2}\right) - \left(h_1 + \frac{v_{1x}^2}{2}\right)\right] = 0, $$

$$ \boxed{\,\frac{\gamma}{\gamma - 1}\,\frac{p_2}{\rho_2} + \frac{v_{2x}^2 + v_{2y}^2}{2} = \frac{\gamma}{\gamma - 1}\,\frac{p_1}{\rho_1} + \frac{v_{1x}^2}{2}\,} \tag{E4} $$

Equations (E1) to (E4) are four equations for the four unknowns $p_2$, $\rho_2$, $v_{2x}$ and $v_{2y}$, which answers the question of the statement.

## Phase 4: Interpretation, Limits and Dimensional Check

- Equation (E3) says that the transverse force on an aerofoil (lift) equals minus the rate of change of $y$ momentum of the stream: the flow is deflected by $v_{2y}$ in the direction opposite to the force on the body. Equation (E2) splits the streamwise force into a pressure drop across the array and a momentum change.
- Trivial limit $\mathbf{F} = 0$: (E1) to (E4) are satisfied by $\rho_2 = \rho_1$, $p_2 = p_1$, $\mathbf{v}_2 = \mathbf{v}_1$ (no body, no change).
- Incompressible limit ($\rho_2 = \rho_1$): (E1) gives $v_{2x} = v_{1x}$ and (E2) reduces to $p_1 - p_2 = F_x/L$.
- Dimensions (SI): $[F_x/L] = (\text{N/m})/\text{m} = \text{Pa}$ and $[\rho_1 v_{1x}^2] = \text{Pa}$; $[\rho_1 v_{1x}\,v_{2y}\,L] = (\text{kg/m}^3)(\text{m/s})(\text{m/s})\,\text{m} = \text{N/m}$; $[\gamma p/((\gamma-1)\rho)] = \text{m}^2/\text{s}^2 = [v^2]$.

> [!info] Extension (beyond the official solution): closed solution of the four equations
> With $m \equiv \rho_1 v_{1x}$, (E1) gives $\rho_2 = m/v_{2x}$, (E3) gives $v_{2y} = -F_y/(mL)$ and (E2) gives $p_2 = P - m\,v_{2x}$ with $P \equiv p_1 + m\,v_{1x} - F_x/L$. Substituting into (E4), with $E \equiv \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_{1x}^2}{2}$, and using that the coefficient of $v_{2x}^2$ is $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$, one obtains the quadratic $(\gamma + 1)\,v_{2x}^2 - 2\gamma\,\frac{P}{m}\,v_{2x} + 2(\gamma - 1)\left(E - \frac{v_{2y}^2}{2}\right) = 0$. For $\mathbf{F} = 0$ one root is $v_{2x} = v_{1x}$; the root continuous with it is the physical one (the other is the supersonic-subsonic conjugate state, as in a normal shock). Numerical check: $p_1 = 101325$ Pa, $\rho_1 = 1.2$ kg/m$^3$, $v_{1x} = 100$ m/s, $L = 0.2$ m, $F_x = 30$ N/m, $F_y = -80$ N/m, $\gamma = 1.4$ give $v_{2x} = 100.16$ m/s, $v_{2y} = 3.3333$ m/s, $\rho_2 = 1.19808$ kg/m$^3$, $p_2 = 101155.8$ Pa, with residuals of (E1) to (E4) below $10^{-9}$ in SI units; the other root gives $p_2 = -6843.3$ Pa $< 0$ and is discarded.
