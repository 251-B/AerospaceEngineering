---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - empuje
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL17.pdf"
---

# Problem CL17: Airplane with an Engine without Moving Parts: Exit State, Thrust, Torque and Canard

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

An experimental airplane is powered by an engine without moving parts that delivers a heat $\dot{Q}$ per unit time. The entrance and exit sections of the engine are, respectively, below and above the airplane's center of gravity (CoG), which is placed at the origin of the coordinate system shown in the figure of CL17.pdf. Both sections are rectangular with the same spanwise length $b$ (along the $z$-direction), and heights $a_i$ and $a_o$, as indicated in the figure. The flow at the engine's inlet has velocity $V_i$, pressure $p_i$ and density $\rho_i$, while the outlet jet discharges at pressure $p_o$. The flow is steady; gravitational forces are negligible; the conditions at the engine's inlet and outlet sections are uniform; the air behaves as a perfect gas of constant $R_g$ and specific heat ratio $\gamma$; the known data are $(a_i, V_i, \rho_i, p_i, a_o, p_o, p_a, \dot{Q})$.

- Applying the mass and energy conservation equations to an appropriately defined control volume, obtain the pair of equations that determine the jet exhaust velocity, $V_o$, and the corresponding density, $\rho_o$. In the remainder of the problem, assume that $V_o$ and $\rho_o$ are already known.
- Use the momentum equation to obtain the thrust provided by the engine, $\bar{T}$.
- Use the angular momentum equation to obtain the net torque $\bar{M}$ acting on the airplane with respect to its CoG. Assume that the surrounding air is at uniform pressure $p_a$, except at the engine's inlet and outlet.
- To compensate the torque obtained in the previous question, the engineers decide that the main wing's CoG coincides with that of the full airplane, so that it doesn't contribute to the torque, and to place a control surface (canard) at a distance $L$ from the CoG (see figure). Knowing that this control surface provides a lift force $F$, determine the distance $L$.

Source: CL17.pdf (page 1, exam of June 27, 2013; statement only, no official solution in the source). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady; neglect $\bar{g}$; uniform properties at the inlet and outlet; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; no moving parts (no shaft work); the heat $\dot{Q}$ is the only energy input.
- Surrounding air at $p_a$ everywhere except at the two sections; viscous stresses negligible on the sections.
- Geometry (reading of the figure): the inlet section spans $-a_i < y < 0$ and the outlet section $0 < y < a_o$, both normal to $\bar{e}_x$, with the flow along $+\bar{e}_x$ (from the nose side to the tail). The nose points towards $-\bar{e}_x$; the canard is at $x = -L$.
- Data: $[a_i,\ V_i,\ \rho_i,\ p_i,\ a_o,\ p_o,\ p_a,\ \dot{Q},\ b,\ \gamma,\ F]$. Unknowns: $[V_o,\ \rho_o,\ \bar{T},\ \bar{M},\ L]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a_i$, $a_o$, $b$ | section heights and span | m |
| $V_i$, $\rho_i$, $p_i$ | inlet state | m/s, kg/m$^3$, Pa |
| $V_o$, $\rho_o$, $p_o$ | outlet state | m/s, kg/m$^3$, Pa |
| $\dot{Q}$ | heat added per unit time | W |
| $\bar{T}$, $\bar{M}$ | thrust and torque on the airplane | N, N$\cdot$m |

> [!info] No official solution
> CL17.pdf contains only the statement. The solution below is derived independently and checked numerically; there is no official key to compare with.

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the airplane (steady flight or test bench), origin at the CoG, $\bar{e}_x$ towards the tail, $\bar{e}_y$ upwards, $\bar{e}_z$ towards the reader. Fixed control volume: the air inside the engine.
- Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$, area $a_ib$), $\Sigma_o$ (outlet, $\bar{n} = +\bar{e}_x$, area $a_ob$), $\Sigma_w$ (engine walls, at rest).

$$ \boxed{\,\bar{T} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\,\bar{M} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**1. Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_i$ | $-\rho_iV_ia_ib$ |
| $\Sigma_o$ | $+\rho_oV_oa_ob$ |
| $\Sigma_w$ | $0$ |

$$ \boxed{\,\rho_iV_ia_i = \rho_oV_oa_o\,},\qquad \dot{m} = \rho_iV_ia_ib \tag{1} $$

**1. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \int_{V_c}Q_R\,dV $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $-\dot{m}\left(e_i + \tfrac{V_i^2}{2}\right)$ | $+p_iV_ia_ib$ | $0$ | $0$ |
| $\Sigma_o$ | $+\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$ | $-p_oV_oa_ob$ | $0$ | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $0$ ($\bar{v} = 0$) | $0$ | $-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed term plus the volume heat release: $\dot{Q}$.

$$ \boxed{\,\dot{m}\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_o}{\rho_o} + \frac{V_o^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_i}{\rho_i} + \frac{V_i^2}{2}\right)\right] = \dot{Q}\,} \tag{2} $$

(1) and (2) are the pair of equations for $V_o$ and $\rho_o$. Explicitly (extension): with (1), $\frac{p_o}{\rho_o} = \frac{p_oV_oa_ob}{\dot{m}}$, and (2) becomes $\frac{V_o^2}{2} + BV_o - H = 0$ with $B = \frac{\gamma}{\gamma-1}\frac{p_oa_ob}{\dot{m}}$ and $H = \frac{\gamma}{\gamma-1}\frac{p_i}{\rho_i} + \frac{V_i^2}{2} + \frac{\dot{Q}}{\dot{m}}$, whose positive root is $V_o = -B + \sqrt{B^2 + 2H}$.

**2. Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $-\dot{m}V_i\,\bar{e}_x$ | $+(p_i - p_a)a_ib\,\bar{e}_x$ | $0$ |
| $\Sigma_o$ | $+\dot{m}V_o\,\bar{e}_x$ | $-(p_o - p_a)a_ob\,\bar{e}_x$ | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{T}$.

$$ \boxed{\,\bar{T} = -\left[\dot{m}\,(V_o - V_i) + (p_o - p_a)a_ob - (p_i - p_a)a_ib\right]\bar{e}_x\,} \tag{3} $$

**3. Angular momentum about the CoG, z component (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})_z(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int\left[\bar{x}\wedge(p - p_a)\bar{n}\right]_z d\sigma$ | $\text{viscous}$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $\int_{-a_i}^0\rho_i(-yV_i)(-V_i)\,b\,dy = -\rho_iV_i^2\frac{a_i^2}{2}b$ | $-\int_{-a_i}^0(p_i - p_a)\,y\,b\,dy = +(p_i - p_a)\frac{a_i^2}{2}b$ | $0$ |
| $\Sigma_o$ | $\int_0^{a_o}\rho_o(-yV_o)(V_o)\,b\,dy = -\rho_oV_o^2\frac{a_o^2}{2}b$ | $-\int_0^{a_o}(p_o - p_a)(-y)\,b\,dy = +(p_o - p_a)\frac{a_o^2}{2}b$ | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}\left[\bar{x}\wedge(p - p_a)\bar{n}\right]_z d\sigma$ | $\int_{\Sigma_w}\left[\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\right]_z d\sigma$ |

Boxed terms: $-M_z$. On a section normal to $\bar{e}_x$, $(\bar{x}\wedge\bar{v})_z = xv_y - yv_x = -yV$ and $(\bar{x}\wedge\bar{n})_z = -yn_x$. Antiderivative of $y$: $y^2/2$; Barrow's rule gives $\left[\frac{y^2}{2}\right]_{-a_i}^0 = -\frac{a_i^2}{2}$ and $\left[\frac{y^2}{2}\right]_0^{a_o} = \frac{a_o^2}{2}$.

$$ \boxed{\,\bar{M} = \frac{b}{2}\left[\left(\rho_iV_i^2 + p_i - p_a\right)a_i^2 + \left(\rho_oV_o^2 + p_o - p_a\right)a_o^2\right]\bar{e}_z\,} \tag{4} $$

### 4. Canard position

The lift $F\bar{e}_y$ of the canard, applied at $x = -L$, has moment $(-L\bar{e}_x)\wedge(F\bar{e}_y) = -LF\,\bar{e}_z$ about the CoG. The wing gives no moment (its CoG is the airplane's). Trim requires $\bar{M} - LF\bar{e}_z = 0$:

$$ \boxed{\,L = \frac{M_z}{F} = \frac{b}{2F}\left[\left(\rho_iV_i^2 + p_i - p_a\right)a_i^2 + \left(\rho_oV_o^2 + p_o - p_a\right)a_o^2\right]\,} \tag{5} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- The airflow enters below the CoG and leaves above it, so both the intake (pushed backwards) and the exhaust reaction (pushed forwards) create a positive $M_z$, which pitches the nose down (the nose is at $-x$). The canard ahead of the CoG with an upward lift balances it, which is why $L > 0$.
- Heating raises the stagnation enthalpy (2): the gas leaves faster ($V_o > V_i$), giving the thrust (3) along $-\bar{e}_x$ (forwards).
- Dimensions (SI): $[\dot{m}V] = \text{N}$; $[(\rho V^2 + p)a^2b] = \text{N}\cdot\text{m}$; $[M_z/F] = \text{m}$.
- Numerical illustration (hypothetical data): $a_i = 0.3$ m, $a_o = 0.25$ m, $b = 1$ m, $V_i = 150$ m/s, $\rho_i = 1$ kg/m$^3$, $p_i = 0.9\times10^5$ Pa, $p_o = p_a = 10^5$ Pa, $\dot{Q} = 20$ MW, $\gamma = 1.4$, $F = 5$ kN give $V_o = 362.56$ m/s, $\rho_o = 0.49647$ kg/m$^3$, $|\bar{T}| = 12565$ N, $M_z = 2601.9$ N$\cdot$m, $L = 0.5204$ m (energy residual below $10^{-7}$).
