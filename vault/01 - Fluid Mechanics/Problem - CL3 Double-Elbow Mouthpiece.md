---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - momento-angular
  - tobera
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL3.pdf"
id: "cl3"
pill: "CL3: Mouthpiece"
tags_html:
  - "Control volume"
  - "Linear momentum"
  - "Angular momentum"
  - "Gauge pressure"
---

# Problem CL3: Double-Elbow Mouthpiece: Exit Velocity, Force and Moment

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The double-elbow mouth piece of exit cross section $A_o$ shown in the figure of CL3.pdf is to be installed at the end of a circular pipe of cross section $A_p$ to redirect the outflow of water into the open atmosphere. Once the mouth piece is installed, the uniform values $U_p$ and $p_p$ are measured for the flow velocity and the pressure at the end of the pipe (i.e., just at the entrance of the mouth piece). Find the value of the uniform velocity at the exit section, $U_o$, as well as the force exerted on the mouth piece and its corresponding moment with respect to the entrance section. (Handwritten addition: neglect the effect of gravity.)

![[attachments/FM-T3/cl3-statement.svg]]
*Statement figure (redrawn from CL3.pdf, p. 1): pipe of section $A_p$ ($U_p$, $p_p$ at the end of the pipe), mouth piece with two elbows dropping a height $H$ to the exit section $A_o$ ($U_o$, open atmosphere $p_a$); $F$ and $M$ act at the entrance section*

Source: CL3.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eqs. 3.37-3.38, force and moment on a body Eqs. 3.32-3.33.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible (water); neglect $\bar{g}$ (handwritten addition); uniform properties at inlet and outlet; viscous stresses negligible on both sections.
- Free jet at the exit: $p = p_a$ over $\Sigma_o$. The thin wall of the mouth piece has the atmosphere $p_a$ on its outer face; the force asked for is the net force of the water inside plus the atmosphere outside, as in the official solution. Ignoring the atmosphere would add $p_a(A_p - A_o)\,\bar{e}_x$.
- Geometry (figure): S-shaped piece; the exit axis is a vertical distance $H$ below the entrance axis; both the entrance and the exit flows are along $+\bar{e}_x$.
- Data: $[\rho,\ A_p,\ A_o,\ U_p,\ p_p,\ p_a,\ H]$. Unknowns: $[U_o,\ \bar{F}_{MP},\ \bar{M}_{MP}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_p$, $A_o$ | entrance and exit areas | m$^2$ |
| $U_p$, $p_p$ | velocity and pressure at the entrance | m/s, Pa |
| $U_o$ | exit velocity | m/s |
| $H$ | vertical offset between the axes | m |
| $\bar{F}_{MP}$, $\bar{M}_{MP}$ | force and moment on the mouth piece | N, N$\cdot$m |

## Phase 2: Frames, Control Volume and Surfaces

- Inertial frame fixed to the pipe: $\bar{e}_x$ along the pipe axis (flow direction), $\bar{e}_y$ vertical upwards, $\bar{e}_z = \bar{e}_x\wedge\bar{e}_y$ towards the reader. Origin $O$ at the centre of the entrance section (moments about $O$).
- Centre of the exit section: $\bar{x}_o = X\bar{e}_x - H\bar{e}_y$ relative to $O$ ($X$ drops out). Position within a circular section relative to its centre: $\bar{\eta}$, with $\int\bar{\eta}\,d\sigma = 0$.
- Control volume: the water inside the mouth piece, fixed ($\bar{v}_c = 0$). Surfaces: $\Sigma_p$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (exit, $\bar{n} = +\bar{e}_x$), $\Sigma_w$ (inner wall).

![[attachments/FM-T3/cl3-cv.svg]]
*Control volume of the solution: $\Sigma_p$ (entrance, $\bar{n} = -\bar{e}_x$), $\Sigma_o$ (exit, $\bar{n} = +\bar{e}_x$) and the inner wall $\Sigma_w$; origin $O$ at the centre of the entrance section, exit centre at $\bar{x}_o = X\bar{e}_x - H\bar{e}_y$ (moments about $O$)*

Force and moment of the water and the atmosphere on the mouth piece, with $\bar{n}$ the outward normal of the control volume:

$$ \boxed{\,\bar{F}_{MP} = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,} $$

$$ \boxed{\,\bar{M}_{MP} = \int_{\Sigma_w}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_p$ | $\rho\,U_p\bar{e}_x\cdot(-\bar{e}_x)\,A_p = -\rho U_pA_p$ |
| $\Sigma_o$ | $\rho\,U_o\bar{e}_x\cdot\bar{e}_x\,A_o = +\rho U_oA_o$ |
| $\Sigma_w$ | $0$ (wall) |

$$ \rho U_pA_p = \rho U_oA_o \;\Longrightarrow\; \boxed{\,U_o = \frac{A_p}{A_o}\,U_p\,},\qquad \dot{m} \equiv \rho U_pA_p = \rho U_oA_o \tag{1} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_p$ | $\rho U_p\bar{e}_x\,(-U_p)\,A_p = -\dot{m}\,U_p\bar{e}_x$ | $-(p_p - p_a)(-\bar{e}_x)A_p = (p_p - p_a)A_p\bar{e}_x$ | $0$ (uniform) |
| $\Sigma_o$ | $\rho U_o\bar{e}_x\,(U_o)\,A_o = \dot{m}\,U_o\bar{e}_x$ | $0$ (free jet, $p = p_a$) | $0$ (uniform) |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F}_{MP}$.

$$ \dot{m}\,(U_o - U_p)\,\bar{e}_x = (p_p - p_a)A_p\,\bar{e}_x - \bar{F}_{MP} \;\Longrightarrow\; \boxed{\,\bar{F}_{MP} = \left[(p_p - p_a)A_p + \rho U_p\,(U_p - U_o)\,A_p\right]\bar{e}_x\,} \tag{2} $$

No entry of the table has a component along $\bar{e}_y$ or $\bar{e}_z$, so $F_{MP,y} = F_{MP,z} = 0$.

**Angular momentum about O (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\,\bar{x}\wedge\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_p$ | $-\rho U_p^2\left(\int\bar{\eta}\,d\sigma\right)\wedge\bar{e}_x = 0$ | $(p_p - p_a)\left(\int\bar{\eta}\,d\sigma\right)\wedge\bar{e}_x = 0$ | $0$ |
| $\Sigma_o$ | $\rho U_o^2A_o\,(\bar{x}_o\wedge\bar{e}_x) = \rho U_o^2HA_o\,\bar{e}_z$ | $0$ ($p = p_a$) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{M}_{MP}$. In the $\Sigma_o$ entry, $\bar{x} = \bar{x}_o + \bar{\eta}$ and $\bar{x}_o\wedge\bar{e}_x = (X\bar{e}_x - H\bar{e}_y)\wedge\bar{e}_x = -H\,\bar{e}_y\wedge\bar{e}_x = +H\,\bar{e}_z$.

$$ \rho U_o^2HA_o\,\bar{e}_z = -\bar{M}_{MP} \;\Longrightarrow\; \boxed{\,\bar{M}_{MP} = -\rho U_o^2HA_o\,\bar{e}_z = -\rho\,\frac{A_p^2}{A_o}\,U_p^2\,H\,\bar{e}_z\,} \tag{3} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- $A_o < A_p$ gives $U_o > U_p$: the piece accelerates the water, and the wall supplies the momentum change.
- The moment exists only because the exit axis is offset by $H$: for $H \to 0$, $\bar{M}_{MP} \to 0$. With the exit below the entrance, the moment is clockwise as seen in the figure ($\bar{e}_z$ towards the reader).
- Limit $A_o \to A_p$: $U_o = U_p$ and $\bar{F}_{MP} \to (p_p - p_a)A_p\bar{e}_x$, the pure pressure force.
- Dimensions (SI): $[\rho U_pA_p(U_p - U_o)] = \text{N}$; $[\rho U_o^2HA_o] = \text{N}\cdot\text{m}$.
- Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $A_p = 0.02$ m$^2$, $A_o = 0.008$ m$^2$, $U_p = 3$ m/s, $p_p = 2.5\times10^5$ Pa, $p_a = 101325$ Pa, $H = 1.5$ m give $U_o = 7.5$ m/s, $F_{MP,x} = 2703.5$ N and $M_{MP,z} = -675$ N$\cdot$m.
- Agreement with the official solution: CL3.pdf obtains (1), (2) and (3).

> [!info] Extension (beyond the official solution)
> If the flow inside were lossless (not stated), Bernoulli's equation $p_p - p_a = \tfrac{1}{2}\rho(U_o^2 - U_p^2)$ would give $F_{MP,x} = \tfrac{1}{2}\rho A_p(U_o - U_p)^2 \ge 0$. With losses, the measured $p_p$ must be used, as in (2).
