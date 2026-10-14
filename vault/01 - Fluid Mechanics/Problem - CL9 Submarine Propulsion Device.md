---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - propulsion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL9.pdf"
---

# Problem CL9: Submarine Propulsion Device: Thrust from the Propeller Power

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The submarine propulsion device schematically represented in the figure of CL9.pdf consists of a nozzle, with inlet and outlet cross-section area $A_e$ and $A_s$, and a propeller (printed as 'fan', corrected by hand to 'propeller') located inside, which imparts a rate of work per unit time (power) $\dot{W}$ to the circulating water stream, whose density and viscosity are $\rho$ and $\mu$, respectively. To determine the thrust $T$ produced when the submarine is at rest and at sufficient depth for gravity to have a negligible effect, please follow these steps:

- By application of the continuity equation determine a relationship between the uniform velocities $U_e$ and $U_s$ at the inlet and outlet sections.
- Use the momentum conservation equation to obtain an expression for the thrust (axial force) that the fluid exerts on the propulsion device as a function of the flow conditions at the inlet and outlet. Assume that the pressure surrounding the device is equal to the ambient pressure $p_\infty$.
- Assuming that the flow upstream from the entrance is steady and inviscid, use Bernoulli's equation along a given streamline to find a relationship between the flow conditions in the stagnant atmosphere (1) and at the entrance $e$.
- Use the energy equation to relate the work per unit time $\dot{W}$ with the different fluid variables appearing in the problem. Assume that the variation of internal energy between the inlet and outlet sections is negligible ($e_e = e_s$) and that all of the device walls, including those of the fan, are thermally insulated.
- Combine the above equations to show that the thrust can be expressed in the form $T/(\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}) = f(A_e/A_s)$, obtaining the function $f$.

Source: CL9.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.

## Phase 1: Hypotheses, Data and Unknowns

- Steady (on average), incompressible water; gravity negligible at depth (it is absorbed in the reduced pressure $p + \rho gz$, as the official solution notes); uniform properties at $e$ and $s$.
- Viscous stresses negligible on the sections ($\rho UD/\mu \gg 1$); the exit jet discharges at the ambient pressure, $p_s = p_\infty$; walls and propeller insulated; $e_e = e_s$.
- Data: $[\rho,\ A_e,\ A_s,\ \dot{W},\ p_\infty]$. Unknowns: $[U_e,\ U_s,\ p_e,\ T]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_e$, $A_s$ | inlet and outlet areas | m$^2$ |
| $U_e$, $U_s$ | inlet and outlet velocities | m/s |
| $p_e$, $p_\infty$ | inlet and ambient pressures | Pa |
| $\dot{W}$ | power given by the propeller to the water | W |
| $T$ | thrust | N |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the submarine (at rest), $\bar{e}_x$ along the axis in the direction of the exit jet. The thrust pushes the device towards $-\bar{e}_x$: $\bar{F} = -T\bar{e}_x$ is the force of the water (inside and outside, at $p_\infty$) on the device.
- Surfaces: $\Sigma_e$ (inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (outlet, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (nozzle walls, fixed) and $\Sigma_p$ (propeller, moving).

$$ \boxed{\,\bar{F} = -T\,\bar{e}_x = \int_{\Sigma_w,\Sigma_p}\left[(p - p_\infty)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**(1) Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_e$ | $-\rho U_eA_e$ |
| $\Sigma_s$ | $+\rho U_sA_s$ |
| $\Sigma_w,\ \Sigma_p$ | $0$ |

$$ \boxed{\,U_eA_e = U_sA_s\,} \tag{1} $$

**(2) Linear momentum (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_\infty)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_\infty)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_e$ | $-\rho U_e^2A_e\,\bar{e}_x$ | $(p_e - p_\infty)A_e\,\bar{e}_x$ | $0$ |
| $\Sigma_s$ | $+\rho U_s^2A_s\,\bar{e}_x$ | $0$ ($p_s = p_\infty$) | $0$ |
| **$\Sigma_w,\ \Sigma_p$** (boxed) | $0$ | $-\int(p - p_\infty)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F} = T\bar{e}_x$. With (1), $\rho U_s^2A_s - \rho U_e^2A_e = \rho U_eA_e(U_s - U_e)$.

$$ \rho U_eA_e(U_s - U_e) = (p_e - p_\infty)A_e + T \;\Longrightarrow\; \boxed{\,T = \rho U_eA_e\,(U_s - U_e) - (p_e - p_\infty)A_e\,} \tag{2} $$

### (3) Bernoulli upstream of the inlet

Steady inviscid flow from the stagnant water far ahead (1), where $v = 0$ and $p = p_\infty$, to the inlet $e$ (Notes Eq. 4.17 with the reduced pressure):

$$ p_\infty = p_e + \tfrac{1}{2}\rho U_e^2 \;\Longrightarrow\; \boxed{\,p_e - p_\infty = -\tfrac{1}{2}\rho U_e^2\,} \tag{3} $$

**(4) Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_e$ | $-\rho U_eA_e\left(e_e + \tfrac{U_e^2}{2}\right)$ | $+p_eU_eA_e$ | $0$ | $0$ |
| $\Sigma_s$ | $+\rho U_sA_s\left(e_s + \tfrac{U_s^2}{2}\right)$ | $-p_\infty U_sA_s$ | $0$ | $0$ |
| **$\Sigma_p$** (boxed) | $0$ | $-\int_{\Sigma_p}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_p}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $0$ (insulated) |
| $\Sigma_w$ | $0$ | $0$ | $0$ | $0$ (insulated) |

Boxed $\Sigma_p$ terms: the propeller power $\dot{W}$. With $e_e = e_s$, $\rho U_eA_e = \rho U_sA_s = \dot{m}$ and (3):

$$ \dot{W} = \dot{m}\left[\frac{p_\infty - p_e}{\rho} + \frac{U_s^2 - U_e^2}{2}\right] = \dot{m}\left[\frac{U_e^2}{2} + \frac{U_s^2 - U_e^2}{2}\right] \;\Longrightarrow\; \boxed{\,\dot{W} = \tfrac{1}{2}\rho A_sU_s^3,\qquad U_s = \left(\frac{2\dot{W}}{\rho A_s}\right)^{1/3}\,} \tag{4} $$

### (5) Thrust in similarity form

Substituting (3) into (2) and using (1), $U_eA_e = U_sA_s$ and $U_e = U_sA_s/A_e$:

$$ T = \rho U_eA_e(U_s - U_e) + \tfrac{1}{2}\rho U_e^2A_e = \rho U_eA_e\left(U_s - \frac{U_e}{2}\right) = \rho A_sU_s\left(U_s - \frac{U_s}{2}\frac{A_s}{A_e}\right) = \rho A_sU_s^2\left(1 - \frac{1}{2}\frac{A_s}{A_e}\right). $$

With (4), $\rho A_sU_s^2 = \rho A_s\left(\frac{2\dot{W}}{\rho A_s}\right)^{2/3} = 2^{2/3}\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}$, so

$$ \boxed{\,\frac{T}{\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}} = f\!\left(\frac{A_e}{A_s}\right) = 2^{2/3}\left(1 - \frac{1}{2\,A_e/A_s}\right)\,} \tag{5} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- $f$ grows with $A_e/A_s$: a large intake (slow inflow, small suction depression at the inlet) gives the most thrust for a given power, tending to $f \to 2^{2/3} \approx 1.587$ as $A_e/A_s \to \infty$. For $A_e = A_s$, $f = 2^{2/3}/2 \approx 0.794$.
- Thrust grows only as $\dot{W}^{2/3}$: doubling the power gives $2^{2/3} \approx 1.59$ times the thrust, because the extra power goes into a faster jet whose kinetic energy is wasted.
- Dimensions (SI): $[\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}] = (\text{kg/m}^3)^{1/3}(\text{kg m}^2/\text{s}^3)^{2/3}(\text{m}^2)^{1/3} = \text{kg}\cdot\text{m/s}^2 = \text{N}$, so $f$ is dimensionless.
- Numerical check (hypothetical data): $\rho = 1000$ kg/m$^3$, $A_s = 0.05$ m$^2$, $A_e = 0.1$ m$^2$, $\dot{W} = 50$ kW give $U_s = 12.599$ m/s, $U_e = 6.2996$ m/s, $T = 5952.8$ N, and $T/(\rho^{1/3}\dot{W}^{2/3}A_s^{1/3}) = 1.1906 = f(2)$; the energy balance (4) gives back $\dot{W} = 50$ kW.
- Agreement with the official solution: CL9.pdf obtains (1) to (5), $f = 2^{2/3}\left(1 - \tfrac{1}{2}A_s/A_e\right)$.
