---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - momento-angular
  - gas
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL12.pdf"
---

# Problem CL12: Gas Discharging through an Inverted U-Pipe: Outlet State, Force and Moment

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The gas circulating along the pipe of cross section $A$ depicted in the figure of CL12.pdf discharges to the atmosphere, where the pressure is $p_a$. Measurements at a given upstream location give $V_u$, $p_u$, and $T_u$ for the velocity, pressure and temperature, all uniform across the section. In the analysis that follows, it is assumed that the pipe is thermally insulated and that buoyancy forces have a negligible effect on the gas motion. The gas properties are defined by its gas constant $R_g$ together with the ratio of specific heats $\gamma = c_p/c_v$.

- Obtain the values of the gas temperature and velocity at the outlet section $T_o$ and $V_o$ in terms of $V_u$, $p_u$, $T_u$, $p_a$, $R_g$ and $\gamma$.
- Compute the two components of the force $F_x$ and $F_y$ acting on the stretch of pipe considered.
- Calculate the momentum on the pipe with respect to the origin of the coordinate system indicated in the figure.

Source: CL12.pdf (page 1, exam of Dec 16, 2011). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady compressible flow of a perfect gas ($p = \rho R_gT$, $h = c_pT = \frac{\gamma}{\gamma-1}R_gT$); neglect $\bar{g}$; pipe insulated and at rest (no heat, no work); uniform properties at both sections.
- Geometry (figure): inverted U of constant section $A$; the gas goes up the left leg ($\bar{v} = V_u\bar{e}_y$ at the measuring section) and down the right leg, discharging as a free jet ($p = p_a$, $\bar{v} = -V_o\bar{e}_y$) at a horizontal distance $L$ from the left leg; the origin $O$ is on the axis of the left leg.
- Data: $[V_u,\ p_u,\ T_u,\ p_a,\ R_g,\ \gamma,\ A,\ L]$. Unknowns: $[T_o,\ V_o,\ F_x,\ F_y,\ \bar{M}]$. The 'momentum on the pipe' of the statement is the moment of the forces on the pipe about $O$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $V_u$, $p_u$, $T_u$ | upstream state | m/s, Pa, K |
| $V_o$, $T_o$ | outlet velocity and temperature | m/s, K |
| $A$, $L$ | pipe section, distance between legs | m$^2$, m |
| $\bar{F}$, $\bar{M}$ | force and moment on the pipe | N, N$\cdot$m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the pipe; $\bar{e}_x$ horizontal (from the left leg to the right leg), $\bar{e}_y$ vertical upwards, $\bar{e}_z = \bar{e}_x\wedge\bar{e}_y$ towards the reader. Fixed control volume.
- Surfaces: $\Sigma_u$ (measuring section, $\bar{n} = -\bar{e}_y$), $\Sigma_o$ (outlet, $\bar{n} = -\bar{e}_y$), $\Sigma_w$ (inner wall). Positions: $\bar{x} = y\bar{e}_y + \bar{\eta}$ on $\Sigma_u$ and $\bar{x} = L\bar{e}_x + y\bar{e}_y + \bar{\eta}$ on $\Sigma_o$, with $\int\bar{\eta}\,d\sigma = 0$.

$$ \boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\,\bar{M} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_u$ | $-\rho_uV_uA$, with $\rho_u = \frac{p_u}{R_gT_u}$ |
| $\Sigma_o$ | $+\rho_oV_oA$, with $\rho_o = \frac{p_a}{R_gT_o}$ |
| $\Sigma_w$ | $0$ |

$$ \rho_uV_uA = \rho_oV_oA \;\Longrightarrow\; \boxed{\,\frac{p_uV_u}{T_u} = \frac{p_aV_o}{T_o}\,} \tag{1} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_u$ | $-\dot{m}\left(e_u + \tfrac{V_u^2}{2}\right)$ | $+p_uV_uA$ | $0$ | $0$ |
| $\Sigma_o$ | $+\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$ | $-p_aV_oA$ | $0$ | $0$ |
| $\Sigma_w$ | $0$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) | $0$ (insulated) |

$$ \boxed{\,\frac{\gamma}{\gamma - 1}R_gT_u + \frac{1}{2}V_u^2 = \frac{\gamma}{\gamma - 1}R_gT_o + \frac{1}{2}V_o^2\,} \tag{2} $$

Solving (1) and (2): with $C \equiv \frac{p_uV_u}{p_aT_u}$, (1) gives $V_o = C\,T_o$; substituting into (2), $\frac{C^2}{2}T_o^2 + \frac{\gamma R_g}{\gamma - 1}T_o - H = 0$ with $H = \frac{\gamma R_g}{\gamma - 1}T_u + \frac{V_u^2}{2}$, whose positive root is

$$ \boxed{\,T_o = \frac{-\frac{\gamma R_g}{\gamma - 1} + \sqrt{\left(\frac{\gamma R_g}{\gamma - 1}\right)^2 + 2C^2H}}{C^2},\qquad V_o = C\,T_o\,} \tag{3} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_u$ | $\rho_uV_u\bar{e}_y(-V_u)A = -\rho_uV_u^2A\,\bar{e}_y$ | $-(p_u - p_a)(-\bar{e}_y)A = (p_u - p_a)A\,\bar{e}_y$ | $0$ |
| $\Sigma_o$ | $\rho_o(-V_o\bar{e}_y)(V_o)A = -\rho_uV_uA\,V_o\,\bar{e}_y$ | $0$ (free jet) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F}$. The $\Sigma_o$ entry uses (1).

$$ -\rho_uV_uA\,(V_u + V_o)\,\bar{e}_y = (p_u - p_a)A\,\bar{e}_y - \bar{F} \;\Longrightarrow\; \boxed{\,F_x = 0,\qquad F_y = \rho_uV_uA\,(V_u + V_o) + (p_u - p_a)A\,} \tag{4} $$

**Angular momentum about O (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_u$ | $0$ ($y\bar{e}_y\wedge\bar{e}_y = 0$, $\int\bar{\eta}\,d\sigma = 0$) | $0$ (same reason) | $0$ |
| $\Sigma_o$ | $\rho_oV_oA\,(L\bar{e}_x\wedge(-V_o\bar{e}_y)) = -\rho_uV_uA\,LV_o\,\bar{e}_z$ | $0$ (free jet) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{M}$.

$$ -\rho_uV_uA\,LV_o\,\bar{e}_z = -\bar{M} \;\Longrightarrow\; \boxed{\,\bar{M} = \rho_uV_uA\,L\,V_o\,\bar{e}_z = \frac{p_u}{R_gT_u}V_uA\,L\,V_o\,\bar{e}_z\,} \tag{5} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- Adiabatic, workless flow keeps the stagnation enthalpy (2); the pressure drop to $p_a$ lowers the density, so the gas accelerates ($V_o > V_u$) and cools slightly ($T_o < T_u$).
- Both legs push the pipe upwards: the gas turning down in the right leg and the gauge pressure at the measuring section. The moment comes only from the outlet jet, offset by $L$ from $O$.
- Incompressible-like limit ($p_u \to p_a$, small $V$): $T_o \to T_u$, $V_o \to V_u$, $F_y \to 2\rho_uV_u^2A$.
- Dimensions (SI): $[\rho_uV_u^2A] = \text{N}$; $[\rho_uV_uALV_o] = \text{N}\cdot\text{m}$; $[R_gT] = [V^2] = \text{m}^2/\text{s}^2$.
- Numerical illustration (hypothetical data, air): $V_u = 50$ m/s, $p_u = 1.5\times10^5$ Pa, $T_u = 400$ K, $p_a = 101325$ Pa, $R_g = 287$ J/(kg K), $\gamma = 1.4$, $A = 0.01$ m$^2$, $L = 1$ m give $T_o = 398.537$ K, $V_o = 73.749$ m/s, $F_y = 567.6$ N, $M_z = 48.181$ N$\cdot$m (residuals of (1), (2) below $10^{-8}$).
- Agreement with the official solution: CL12.pdf obtains (1), (2), (4) and (5); it does not solve (1)-(2) explicitly.
