---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - codo
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL6.pdf"
id: "cl6"
pill: "CL6: Elbow"
tags_html:
  - "Elbow"
  - "Linear momentum"
  - "Energy"
  - "Heat through the walls"
---

# Problem CL6: Elbow Discharging a Vertical Jet: Velocity, Force and Heat

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A liquid of density $\rho$ and specific heat $c$ flows through the elbow-shaped pipe shown in CL6.pdf, discharging to the atmosphere as a vertical jet through an outlet section of surface area $A_o$, different from the value $A_i$ at the inlet. Gravity is assumed to have a negligible effect on the fluid motion. Besides, uniform flow properties are assumed at the inlet and outlet sections, where readings from a thermometer give different values $T_i$ and $T_o$ for the temperature. The velocity at the outlet section is measured to be $v_o$ and a manometer is used to determine the value $p_i$ for the pressure at the inlet section. In terms of all of these quantities, determine:

- The value of the velocity at the inlet $v_i$.
- The two components of the force $(F_x, F_z)$ exerted on the pipe.
- The amount of heat $Q$ transferred per unit time to the liquid by heat conduction through the pipe walls.

![[attachments/FM-T3/cl6-statement.svg]]
*Statement figure (redrawn from CL6.pdf, p. 1): inlet section $A_i$ with $v_i$, $p_i$, $T_i$; outlet $A_o$ discharging a vertical jet $v_o$, $T_o$ into $p_a$; force components $F_x$, $F_z$ on the pipe and heat $Q$ through its walls*

Source: CL6.pdf (page 1), also solved in class (class notes, CL6). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; uniform properties at inlet and outlet (no viscous stresses or conduction across them).
- Free jet: $p = p_a$ over the outlet section. The outer face of the pipe is in contact with the ambient air at $p_a$, so the force on the pipe is computed with gauge pressure $p - p_a$.
- Geometry (figure): the liquid enters horizontally along $+\bar{e}_x$ and leaves as a vertical jet along $-\bar{e}_z$ ($\bar{e}_z$ upwards).
- Data: $[\rho,\ c,\ A_i,\ A_o,\ v_o,\ p_i,\ p_a,\ T_i,\ T_o]$. Unknowns: $[v_i,\ F_x,\ F_z,\ \dot{Q}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_i$, $A_o$ | inlet and outlet areas | m$^2$ |
| $v_i$, $v_o$ | inlet and outlet velocities | m/s |
| $p_i$, $p_a$ | inlet and ambient pressures | Pa |
| $T_i$, $T_o$ | inlet and outlet temperatures | K |
| $c$ | specific heat of the liquid | J/(kg$\cdot$K) |
| $\dot{Q}$ | heat per unit time into the liquid | W |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the pipe, $\bar{e}_x$ horizontal (inlet flow direction), $\bar{e}_z$ vertical upwards. Fixed control volume: the liquid inside the pipe, $\bar{v}_c = 0$.
- Surfaces: $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$, $\bar{v} = v_i\bar{e}_x$), $\Sigma_o$ (outlet, $\bar{n} = -\bar{e}_z$, $\bar{v} = -v_o\bar{e}_z$), $\Sigma_w$ (pipe wall, $\bar{v} = 0$).

![[attachments/FM-T3/cl6-cv.svg]]
*Control volume of the solution (as in the class notes): the liquid inside the pipe, with $\Sigma_i$ (inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (outlet, $\bar{n} = -\bar{e}_z$) and the wall $\Sigma_w$, where the force and the heat are collected*

Force of the liquid and the ambient air on the pipe, and heat through the walls, written on $\Sigma_w$:

$$ \boxed{\,\bar{F} = F_x\bar{e}_x + F_z\bar{e}_z = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,} $$

$$ \boxed{\,\dot{Q} = -\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_i$ | $\rho\,v_i\bar{e}_x\cdot(-\bar{e}_x)A_i = -\rho v_iA_i$ |
| $\Sigma_o$ | $\rho\,(-v_o\bar{e}_z)\cdot(-\bar{e}_z)A_o = +\rho v_oA_o$ |
| $\Sigma_w$ | $0$ |

$$ \boxed{\,v_i = \frac{A_o}{A_i}\,v_o\,},\qquad \dot{m} = \rho v_iA_i = \rho v_oA_o \tag{1} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $\rho v_i\bar{e}_x\,(-v_i)A_i = -\rho v_i^2A_i\,\bar{e}_x$ | $-(p_i - p_a)(-\bar{e}_x)A_i = (p_i - p_a)A_i\,\bar{e}_x$ | $0$ |
| $\Sigma_o$ | $\rho(-v_o\bar{e}_z)\,(v_o)A_o = -\rho v_o^2A_o\,\bar{e}_z$ | $0$ (free jet) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F}$.

$$ -\rho v_i^2A_i\,\bar{e}_x - \rho v_o^2A_o\,\bar{e}_z = (p_i - p_a)A_i\,\bar{e}_x - \bar{F} \;\Longrightarrow\; \boxed{\,F_x = \left[\rho v_i^2 + (p_i - p_a)\right]A_i,\qquad F_z = \rho v_o^2A_o\,} \tag{2} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $-\dot{m}\left(cT_i + \tfrac{v_i^2}{2}\right)$ | $+p_iv_iA_i$ | $0$ | $0$ (uniform $T$) |
| $\Sigma_o$ | $+\dot{m}\left(cT_o + \tfrac{v_o^2}{2}\right)$ | $-p_av_oA_o$ | $0$ | $0$ (uniform $T$) |
| **$\Sigma_w$** (boxed) | $0$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) | $-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ term: $\dot{Q}$. Using (1), $p_iv_iA_i - p_av_oA_o = (p_i - p_a)\,v_oA_o$.

$$ \dot{m}\left[c(T_o - T_i) + \frac{v_o^2 - v_i^2}{2}\right] = (p_i - p_a)\,v_oA_o + \dot{Q} \;\Longrightarrow\; \boxed{\,\dot{Q} = \rho v_oA_o\left[c(T_o - T_i) + \frac{v_o^2 - v_i^2}{2}\right] + (p_a - p_i)\,v_oA_o\,} \tag{3} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- $F_x > 0$: the pipe is pushed along the incoming flow by the momentum flux and the gauge pressure at the inlet. $F_z > 0$: the jet leaves downwards, so the pipe is pushed upwards.
- (3) splits the heat into the rise of internal energy, the change of kinetic energy and the flow work. If no heat were exchanged and there were no losses, (3) with $\dot{Q} = 0$ and $T_o = T_i$ would reduce to Bernoulli's equation $p_i + \tfrac{1}{2}\rho v_i^2 = p_a + \tfrac{1}{2}\rho v_o^2$.
- Dimensions (SI): $[\rho v_i^2A_i] = [(p_i - p_a)A_i] = \text{N}$; $[\rho v_oA_o\,c\,\Delta T] = (\text{kg/s})(\text{J/(kg K)})\,\text{K} = \text{W}$; $[(p_a - p_i)v_oA_o] = \text{Pa}\cdot\text{m}^3/\text{s} = \text{W}$.
- Numerical illustration (hypothetical data): water, $c = 4186$ J/(kg K), $A_i = 0.01$ m$^2$, $A_o = 0.004$ m$^2$, $v_o = 6$ m/s, $p_i = 1.6\times10^5$ Pa, $p_a = 101325$ Pa, $T_o - T_i = 0.5$ K give $v_i = 2.4$ m/s, $F_x = 644.35$ N, $F_z = 144$ N and $\dot{Q} = 49187$ W.
- Agreement with the official and class solutions: (1), (2) and (3) are the results of CL6.pdf (which labels the vertical axis $y$: $F_y = \rho v_o^2A_o$) and of the class notes.
