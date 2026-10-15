---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - cilindros
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL21.pdf"
id: "cl21"
pill: "CL21: Hot Cylinders"
tags_html:
  - "Periodicity"
  - "Drag"
  - "Heat release"
  - "Perfect gas"
---

# Problem CL21: Array of Hot Cylinders in a Gas Stream: Density, Force and Heat

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A linear array of parallel hot cylinders of radius $R$, whose centers are separated a distance $3R$, is placed perpendicular to a gas stream with velocity $U_1$, density $\rho_1$, and pressure $p_1$, as indicated in the figure of CL21.pdf. Sufficiently far downstream the gas properties recover uniform values, including a velocity $U_2$ and a pressure $p_2$. Assume that the effect of gravity is negligible. In terms of the quantities indicated in the figure, determine:

- The value of the density downstream from the array of cylinders.
- The force acting on each cylinder (per unit length).
- The heat transferred from each cylinder to the gas stream per unit time (per unit length). Express the result with use made of the ratio of specific heats $\gamma$.

NOTE: Explain clearly the simplifications and assumptions employed in the derivation.

![[attachments/FM-T3/cl21-statement.svg]]
*Statement figure (redrawn from CL21.pdf, p. 1): array of cylinders of radius $R$, centres $3R$ apart, in a stream $U_1$, $\rho_1$, $p_1$; far downstream $U_2$, $p_2$*

Source: CL21.pdf (page 1, retake of Jun 13, 2014). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, planar (per unit length of cylinder); neglect $\bar{g}$; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; uniform states far upstream (1) and far downstream (2), where viscous stresses and conduction vanish.
- Infinite array: the flow is periodic in $y$ with period $3R$ and symmetric about each cylinder axis, so the downstream velocity stays along $\bar{e}_x$ (no lift).
- Cylinders at rest (no work); they release heat to the gas.
- Data: $[\rho_1,\ U_1,\ p_1,\ U_2,\ p_2,\ R,\ \gamma]$. Unknowns: $[\rho_2,\ \bar{F},\ \dot{Q}]$ per unit length.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U_1$, $\rho_1$, $p_1$ | upstream state | m/s, kg/m$^3$, Pa |
| $U_2$, $\rho_2$, $p_2$ | downstream state | m/s, kg/m$^3$, Pa |
| $R$ | cylinder radius (spacing $3R$) | m |
| $\bar{F}$, $\dot{Q}$ | force and heat per unit length | N/m, W/m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the array; $\bar{e}_x$ along the stream. Fixed control volume of height $3R$ around one cylinder (as in the official figure).
- Surfaces: $\Sigma_1$ (far upstream, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (far downstream, $\bar{n} = +\bar{e}_x$), $\Sigma_{top}$ and $\Sigma_{bot}$ (lines midway between cylinders, $\bar{n} = \pm\bar{e}_y$) and $\Sigma_{cyl}$ (cylinder surface). By periodicity every flux through $\Sigma_{top}$ equals minus the one through $\Sigma_{bot}$: they cancel each other out.

![[attachments/FM-T3/cl21-cv.svg]]
*Control volume of the solution: $\Sigma_1$ and $\Sigma_2$ far upstream and downstream, $\Sigma_{top}$ and $\Sigma_{bot}$ midway between cylinders ($3R$ apart; their fluxes cancel by periodicity) and the cylinder surface $\Sigma_{cyl}$, with the outward normals*

$$ \boxed{\,\bar{F} = \int_{\Sigma_{cyl}}\left[p\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\,\dot{Q} = -\int_{\Sigma_{cyl}}\bar{q}\cdot\bar{n}\,d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**1. Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $-\rho_1U_1\,3R$ |
| $\Sigma_2$ | $+\rho_2U_2\,3R$ |
| $\Sigma_{top} + \Sigma_{bot}$ | $0$ (cancel each other out) |
| $\Sigma_{cyl}$ | $0$ |

$$ \boxed{\,\rho_2 = \frac{U_1}{U_2}\,\rho_1\,} \tag{1} $$

**2. Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-\rho_1U_1^2\,3R\,\bar{e}_x$ | $+p_1\,3R\,\bar{e}_x$ | $0$ |
| $\Sigma_2$ | $+\rho_2U_2^2\,3R\,\bar{e}_x$ | $-p_2\,3R\,\bar{e}_x$ | $0$ |
| $\Sigma_{top} + \Sigma_{bot}$ | $0$ | $0$ | $0$ (cancel each other out) |
| **$\Sigma_{cyl}$** (boxed) | $0$ | $-\int_{\Sigma_{cyl}}p\,\bar{n}\,d\sigma$ | $\int_{\Sigma_{cyl}}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F}$. With (1), $\rho_2U_2^2 = \rho_1U_1U_2$.

$$ \boxed{\,\frac{\bar{F}}{3R} = \left[p_1 - p_2 + \rho_1U_1^2\left(1 - \frac{U_2}{U_1}\right)\right]\bar{e}_x\,} \tag{2} $$

**3. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-\rho_1U_1\,3R\left(e_1 + \tfrac{U_1^2}{2}\right)$ | $+p_1U_1\,3R$ | $0$ | $0$ |
| $\Sigma_2$ | $+\rho_2U_2\,3R\left(e_2 + \tfrac{U_2^2}{2}\right)$ | $-p_2U_2\,3R$ | $0$ | $0$ |
| $\Sigma_{top} + \Sigma_{bot}$ | $0$ | $0$ | $0$ | $0$ (cancel each other out) |
| **$\Sigma_{cyl}$** (boxed) | $0$ | $0$ ($\bar{v} = 0$) | $0$ | $-\int_{\Sigma_{cyl}}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed term: $\dot{Q}$. With $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$ and $\frac{p_2}{\rho_2} = \frac{p_2U_2}{\rho_1U_1}$ from (1):

$$ \boxed{\,\dot{Q} = \rho_1U_1\,3R\left[\frac{\gamma}{\gamma - 1}\left(\frac{p_2U_2}{\rho_1U_1} - \frac{p_1}{\rho_1}\right) + \frac{1}{2}\left(U_2^2 - U_1^2\right)\right]\,} \tag{3} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- Heating expands the gas: $\rho_2 < \rho_1$ requires $U_2 > U_1$ (1). The drag (2) combines the pressure drop across the array with the momentum change.
- Without heat ($\dot{Q} = 0$) and without drag, (1) to (3) are satisfied by state 2 = state 1.
- Dimensions (SI, per unit length): $[(p + \rho U^2)R] = \text{N/m}$; $[\rho UR\,p/\rho] = \text{W/m}$.
- Numerical illustration (hypothetical data): $\rho_1 = 1.2$ kg/m$^3$, $U_1 = 30$ m/s, $p_1 = 101325$ Pa, $U_2 = 31$ m/s, $p_2 = 101000$ Pa, $R = 0.01$ m, $\gamma = 1.4$ give $\rho_2 = 1.1613$ kg/m$^3$, $F/L = 8.67$ N/m and $\dot{Q}/L = 9614.2$ W/m.
- Agreement with the official solution: CL21.pdf obtains (1), (2) and (3) (the handwritten correction in (3) replaces $1/\rho_2$ by $U_2/(\rho_1U_1)$, as here).
