---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - turborreactor
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL5.pdf"
id: "cl5"
pill: "CL5: Turbojet"
tags_html:
  - "Moving boundaries"
  - "Mass, momentum, energy"
  - "Heat and work"
  - "Thrust"
---

# Problem CL5: Turbojet on a Testbench: Exit State

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The entrance and exit sections of the turboreactor sketched in the figure of CL5.pdf have areas $A_1$ and $A_2$. Besides the outer fixed frame, the machine has mobile parts in its interior that extract an amount of work $W$ per unit time from the fluid stream. The combined effects of chemical reaction in the combustion chamber and heat transfer through the walls give a heat transfer per unit time $Q$ to the fluid stream. The axial force on the turboreactor measured on the testbench is $\bar{F} = -F\,\bar{e}_x$. For given values of $W$, $Q$ and $F$ and assuming that at the entrance and exit sections the flow properties are uniform, obtain the values of the density $\rho_2$, pressure $p_2$ and velocity $v_2$ in terms of their values $p_1$, $\rho_1$ and $v_1$ at the entrance. (Handwritten addition: no gravity.)

![[attachments/FM-T3/cl5-statement.svg]]
*Statement figure (redrawn from CL5.pdf, p. 1): entrance $A_1$ ($v_1$, $p_1$, $\rho_1$), exit $A_2$ ($v_2$, $p_2$, $\rho_2$), rotor and heat sources $Q_r$, $Q_c$; the dashed control volume and its surfaces $\Sigma_1$ to $\Sigma_4$ belong to the official figure*

Source: CL5.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.

## Phase 1: Hypotheses, Data and Unknowns

- Compressible flow; neglect gravity; uniform properties at inlet and outlet; steady on average (the rotating parts make the flow periodic inside, but there is no net accumulation).
- Perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$, as in the class solution. Fuel mass flow neglected (not given), so the same mass flow crosses both sections.
- $\dot{W}$: work per unit time extracted from the fluid by the mobile parts; $\dot{Q}$: heat per unit time transferred to the fluid; $\bar{F} = -F\bar{e}_x$: force on the device measured on the testbench (fluid inside plus ambient air outside, at $p_a$).
- Data: $[\rho_1,\ p_1,\ \bar{v}_1 = v_1\bar{e}_x,\ A_1,\ A_2,\ p_a,\ F,\ \dot{W},\ \dot{Q},\ \gamma]$. Unknowns: $[\rho_2,\ p_2,\ \bar{v}_2 = v_2\bar{e}_x]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_1$, $A_2$ | entrance and exit areas | m$^2$ |
| $p_1$, $\rho_1$, $v_1$ | entrance state | Pa, kg/m$^3$, m/s |
| $p_2$, $\rho_2$, $v_2$ | exit state | Pa, kg/m$^3$, m/s |
| $F$ | thrust measured on the bench | N |
| $\dot{W}$, $\dot{Q}$ | power extracted and heat added | W |
| $\dot{m} = \rho_1v_1A_1$ | mass flow | kg/s |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the testbench; $\bar{e}_x$ along the engine axis in the flow direction.
- Surfaces: $\Sigma_1$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (exit, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (fixed walls, $\bar{v} = \bar{v}_c = 0$) and $\Sigma_m$ (surface of the mobile parts, moving with them: $\bar{v} = \bar{v}_c \ne 0$). On $\Sigma_w$ and $\Sigma_m$, $(\bar{v} - \bar{v}_c)\cdot\bar{n} = 0$.
- $\bar{n}$ is the outward normal of the control volume; $\bar{n}_{\text{in}} = -\bar{n}$ points into the fluid.

![[attachments/FM-T3/cl5-cv.svg]]
*Control volume of the solution (as in the class notes): $\Sigma_1$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (exit, $\bar{n} = +\bar{e}_x$), the fixed walls $\Sigma_w$ and the surface $\Sigma_m$ of the mobile parts. The official figure calls them $\Sigma_1$, $\Sigma_2$, $\Sigma_3$ and $\Sigma_4$*

Definitions written on the surfaces, as in class:

$$ \boxed{\,\bar{F} = \int_{\Sigma_m,\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_m,\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma = -F\,\bar{e}_x\,} $$

$$ \boxed{\,\dot{Q} = \int_{\Sigma_w,\Sigma_m}\bar{q}\cdot\bar{n}_{\text{in}}\,d\sigma + \int_{V_c}Q_R\,dV\,} $$

$$ \boxed{\,\dot{W} = -\int_{\Sigma_m}p\,\bar{n}_{\text{in}}\cdot\bar{v}\,d\sigma + \int_{\Sigma_m}(\bar{\bar{\tau}}'\cdot\bar{n}_{\text{in}})\cdot\bar{v}\,d\sigma\,} $$

Only $\Sigma_m$ enters $\dot{W}$: $\Sigma_w$ is a fixed surface and does no work. $\dot{W}$ is the power of the gas on the moving solid, so the power done on the gas there is $-\dot{W}$.

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.10)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{on average})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $-\rho_1v_1A_1$ |
| $\Sigma_2$ | $+\rho_2v_2A_2$ |
| $\Sigma_m$ | $0$ ($\bar{v} = \bar{v}_c$) |
| $\Sigma_w$ | $0$ |

$$ \boxed{\,\rho_1v_1A_1 = \rho_2v_2A_2 = \dot{m}\,} \tag{1} $$

**Linear momentum (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $\rho_1v_1\bar{e}_x(-v_1)A_1 = -\dot{m}v_1\bar{e}_x$ | $(p_1 - p_a)A_1\bar{e}_x$ | $0$ |
| $\Sigma_2$ | $\rho_2v_2\bar{e}_x(v_2)A_2 = \dot{m}v_2\bar{e}_x$ | $-(p_2 - p_a)A_2\bar{e}_x$ | $0$ |
| **$\Sigma_m,\ \Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_m,\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_m,\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_m$, $\Sigma_w$ terms: $-\bar{F} = F\bar{e}_x$ (uniform velocity vectors give no viscous stress on $\Sigma_1$, $\Sigma_2$).

$$ \boxed{\,\dot{m}\,(v_2 - v_1) = (p_1 - p_a)A_1 - (p_2 - p_a)A_2 + F\,} \tag{2} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \int_{V_c}Q_R\,dV $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-\dot{m}\left(e_1 + \tfrac{v_1^2}{2}\right)$ | $+p_1v_1A_1$ | $0$ | $0$ ($\nabla T = 0$) |
| $\Sigma_2$ | $+\dot{m}\left(e_2 + \tfrac{v_2^2}{2}\right)$ | $-p_2v_2A_2$ | $0$ | $0$ ($\nabla T = 0$) |
| **$\Sigma_m$** (boxed) | $0$ | $-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_m}(\bar{\bar{\tau}}'\cdot\bar{n})\cdot\bar{v}\,d\sigma$ | $-\int_{\Sigma_m}\bar{q}\cdot\bar{n}\,d\sigma$ |
| **$\Sigma_w$** (boxed) | $0$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) | $-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed terms: the pressure and viscous work on $\Sigma_m$ add up to $-\dot{W}$; the conduction through $\Sigma_m$, $\Sigma_w$ plus the volume term $\int_{V_c}Q_R\,dV$ add up to $\dot{Q}$. Moving the pressure work on $\Sigma_1$, $\Sigma_2$ to the left gives $h = e + p/\rho$; with (1) and $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:

$$ \boxed{\,\dot{m}\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_2}{\rho_2} + \frac{v_2^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2}\right)\right] = -\dot{W} + \dot{Q}\,} \tag{3} $$

(1), (2) and (3) determine $\rho_2$, $p_2$ and $v_2$.

## Phase 4: Interpretation, Limits and Dimensional Check

- (2) is the thrust balance: thrust = change of momentum flux + pressure imbalance on the sections. For $p_1 = p_2 = p_a$, $F = \dot{m}(v_2 - v_1)$.
- (3): the stagnation enthalpy of the stream rises by the heat added and falls by the work extracted, per unit mass flow.
- Dimensions (SI): $[\dot{m}(v_2 - v_1)] = \text{N}$; $[(\dot{Q} - \dot{W})/\dot{m}] = \text{J/kg} = \text{m}^2/\text{s}^2 = [h] = [v^2]$.
- Numerical illustration (hypothetical data): $A_1 = 0.5$ m$^2$, $A_2 = 0.3$ m$^2$, $v_1 = 150$ m/s, $p_1 = 0.9\times10^5$ Pa, $\rho_1 = 1.1$ kg/m$^3$ ($M_1 = 0.443$), $p_a = 10^5$ Pa, $F = 30$ kN, $\dot{W} = 2$ MW, $\dot{Q} = 30$ MW, $\gamma = 1.4$: $\dot{m} = 82.5$ kg/s and the two roots of the extension below, $v_2 = 355.515$ m/s, $p_2 = 126817$ Pa, $\rho_2 = 0.77353$ kg/m$^3$ ($M_2 = 0.742$), and $v_2 = 597.263$ m/s, $p_2 = 60336$ Pa, $\rho_2 = 0.46043$ kg/m$^3$ ($M_2 = 1.39$); residuals of (1) to (3) below $10^{-6}$ in SI units.
- Agreement with the official and class solutions: the same equations (1), (2), (3) (CL5.pdf writes (2) as $F = \rho_1v_1A_1(v_2 - v_1) - (p_1 - p_a)A_1 + (p_2 - p_a)A_2$).

> [!info] Extension (beyond the official solution): explicit solution
> With $K = p_aA_2 + F + (p_1 - p_a)A_1 + \dot{m}v_1$, (2) gives $p_2A_2 = K - \dot{m}v_2$ and, with (1), $p_2/\rho_2 = (K - \dot{m}v_2)v_2/\dot{m}$. Substituting into (3) and using $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$: $(\gamma + 1)v_2^2 - 2\gamma\frac{K}{\dot{m}}v_2 + 2(\gamma - 1)H_0 = 0$, with $H_0 = \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_1^2}{2} + \frac{\dot{Q} - \dot{W}}{\dot{m}}$. The two roots are a subsonic and a supersonic exit state; for a subsonic entrance with heat addition the physical one is the subsonic (smaller) root, since reaching the other would require passing through sonic conditions inside the engine, which this overall balance cannot describe. For $F = 0$, $\dot{Q} = \dot{W} = 0$ and $A_1 = A_2$ one root is $v_2 = v_1$ and the product of the roots is $2(\gamma - 1)H_0/(\gamma + 1)$, the Prandtl relation of a normal shock.
