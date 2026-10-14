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
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A planar uniform stream of air with pressure $p_1$, density $\rho_1$ and velocity $\bar{v}_1 = v_{1x}\bar{e}_x$ flows past an array of aerofoils with vertical separation $L$, exerting on each one a force (per unit length) given by $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$. Assuming that the aerofoils are thermally insulated and neglecting the effect of gravity, write the equations that determine the values of the pressure $p_2$, density $\rho_2$ and velocity $\bar{v}_2 = v_{2x}\bar{e}_x + v_{2y}\bar{e}_y$ for the uniform stream found sufficiently far downstream.

![[attachments/FM-T3/cl4-statement.png]]
*Statement figure (CL4.pdf, p. 1, cropped): cascade of aerofoils $L$ apart; the dashed control volume ($\Sigma_1$ to $\Sigma_5$) and the handwritten notes belong to the official sheet*

Source: CL4.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46, force on a body Eq. 3.32.

## Phase 1: Hypotheses, Data and Unknowns

- Steady planar flow through an infinite array of identical aerofoils (pitch $L$), so the flow is periodic in $y$; uniform far upstream (1) and far downstream (2).
- Neglect $\bar{g}$; aerofoils thermally insulated; compressible fluid. Viscous stresses and heat conduction negligible in the uniform sections.
- Perfect gas: $h = e + \frac{p}{\rho} = c_pT = \frac{c_p}{R_g}\frac{p}{\rho} = \frac{\gamma}{\gamma - 1}\frac{p}{\rho}$ (with $p = \rho R_gT$ and $\gamma = c_p/c_v$), as in the class solution.
- Data: $[p_1,\ \rho_1,\ v_{1x},\ L,\ F_x,\ F_y,\ \gamma]$. Unknowns: $[p_2,\ \rho_2,\ v_{2x},\ v_{2y}]$: four equations are needed.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $p_1$, $\rho_1$, $v_{1x}$ | upstream state | Pa, kg/m$^3$, m/s |
| $p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$ | downstream state | Pa, kg/m$^3$, m/s |
| $L$ | pitch of the array | m |
| $F_x$, $F_y$ | force on each aerofoil per unit length | N/m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the array; $\bar{e}_x$ along the incoming stream, $\bar{e}_y$ along the array. Fixed control volume, $\bar{v}_c = 0$, one period high.
- Surfaces: $\Sigma_1$ (far upstream, height $L$, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (far downstream, height $L$, $\bar{n} = +\bar{e}_x$), $\Sigma_{l1}$ and $\Sigma_{l2}$ (upper and lower stream surfaces, $\bar{v}\cdot\bar{n} = 0$), $\Sigma_w$ (aerofoil surface, $\bar{v} = 0$, insulated).
- Periodicity: $\Sigma_{l2}$ is $\Sigma_{l1}$ shifted by $-L\bar{e}_y$ with opposite normals, so the integrals of any periodic quantity over $\Sigma_{l1}$ and $\Sigma_{l2}$ cancel each other out.

![[attachments/FM-T3/cl4-cv.svg]]
*Control volume of the solution (as in the class notes): $\Sigma_1$ and $\Sigma_2$ (sections of height $L$), the stream surfaces $\Sigma_{l1}$ and $\Sigma_{l2}$ ($\Sigma_{l2}$ is $\Sigma_{l1}$ shifted by $-L\bar{e}_y$, so their fluxes cancel) and the aerofoil surface $\Sigma_w$. The official figure calls them $\Sigma_1$, $\Sigma_2$, $\Sigma_3$, $\Sigma_4$ and $\Sigma_5$*

Force on each aerofoil (per unit length), with $\bar{n}$ the outward normal of the control volume:

$$ \boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w}p\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $\rho_1(-v_{1x})\,L$ |
| $\Sigma_2$ | $\rho_2\,v_{2x}\,L$ |
| $\Sigma_{l1},\ \Sigma_{l2}$ | $0$ (stream surfaces) |
| $\Sigma_w$ | $0$ (wall) |

$$ \boxed{\,\rho_1v_{1x} = \rho_2v_{2x}\,} \tag{1} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $\rho_1v_{1x}\bar{e}_x(-v_{1x})L$ | $+p_1L\,\bar{e}_x$ | $0$ |
| $\Sigma_2$ | $\rho_2(v_{2x}\bar{e}_x + v_{2y}\bar{e}_y)\,v_{2x}L$ | $-p_2L\,\bar{e}_x$ | $0$ |
| $\Sigma_{l1} + \Sigma_{l2}$ | $0$ | $0$ (cancel each other out) | $0$ (cancel each other out) |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}p\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F} = -F_x\bar{e}_x - F_y\bar{e}_y$. With (1), $\rho_2v_{2x}L = \rho_1v_{1x}L$ in the $\Sigma_2$ flux.

$$ \boxed{\,F_x = \rho_1v_{1x}L\,(v_{1x} - v_{2x}) + (p_1 - p_2)\,L\,}\ \ \text{(2)}\qquad \boxed{\,F_y = -\rho_1v_{1x}L\,v_{2y}\,}\ \ \text{(3)} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}(Q_c + Q_r)\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $\rho_1\left(e_1 + \tfrac{v_{1x}^2}{2}\right)(-v_{1x})L$ | $+p_1v_{1x}L$ | $0$ | $0$ |
| $\Sigma_2$ | $\rho_2\left(e_2 + \tfrac{v_{2x}^2 + v_{2y}^2}{2}\right)v_{2x}L$ | $-p_2v_{2x}L$ | $0$ | $0$ |
| $\Sigma_{l1} + \Sigma_{l2}$ | $0$ | $0$ | $0$ (cancel each other out) | $0$ (cancel each other out) |
| $\Sigma_w$ | $0$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) | $0$ (insulated) |

Moving the pressure work to the left turns $e$ into $h = e + p/\rho$; dividing by $\rho_1v_{1x}L = \rho_2v_{2x}L$ and using $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:

$$ \boxed{\,\frac{\gamma}{\gamma - 1}\left(\frac{p_2}{\rho_2} - \frac{p_1}{\rho_1}\right) + \frac{v_{2x}^2 + v_{2y}^2}{2} - \frac{v_{1x}^2}{2} = 0\,} \tag{4} $$

(1) to (4) are four equations for the four unknowns $p_2$, $\rho_2$, $v_{2x}$, $v_{2y}$, which answers the question.

## Phase 4: Interpretation, Limits and Dimensional Check

- (3): the transverse force on an aerofoil equals minus the $y$ momentum given to the stream; the flow is deflected opposite to the force. (2) splits the streamwise force into a pressure drop and a momentum change.
- $\bar{F} = 0$: (1) to (4) are satisfied by state 2 = state 1. Incompressible limit ($\rho_2 = \rho_1$): $v_{2x} = v_{1x}$ and $p_1 - p_2 = F_x/L$.
- Dimensions (SI): $[F_x/L] = \text{Pa} = [\rho_1v_{1x}^2]$; $[\rho_1v_{1x}Lv_{2y}] = \text{N/m}$; $[\gamma p/((\gamma-1)\rho)] = \text{m}^2/\text{s}^2 = [v^2]$.
- Agreement with the official solution and the class solution: the same four equations (1) to (4).

> [!info] Extension (beyond the official solution): closed solution
> With $m = \rho_1v_{1x}$: $\rho_2 = m/v_{2x}$, $v_{2y} = -F_y/(mL)$ and $p_2 = P - m\,v_{2x}$ with $P = p_1 + mv_{1x} - F_x/L$. Substituting into (4), with $E = \frac{\gamma}{\gamma-1}\frac{p_1}{\rho_1} + \frac{v_{1x}^2}{2}$ and the coefficient $\frac{1}{2} - \frac{\gamma}{\gamma-1} = -\frac{\gamma+1}{2(\gamma-1)}$ of $v_{2x}^2$: $(\gamma + 1)v_{2x}^2 - 2\gamma\frac{P}{m}v_{2x} + 2(\gamma - 1)\left(E - \frac{v_{2y}^2}{2}\right) = 0$. For $\bar{F} = 0$ one root is $v_{2x} = v_{1x}$; the root continuous with it is the physical one. Check: $p_1 = 101325$ Pa, $\rho_1 = 1.2$ kg/m$^3$, $v_{1x} = 100$ m/s, $L = 0.2$ m, $F_x = 30$ N/m, $F_y = -80$ N/m, $\gamma = 1.4$ give $v_{2x} = 100.16$ m/s, $v_{2y} = 3.3333$ m/s, $\rho_2 = 1.19808$ kg/m$^3$, $p_2 = 101155.8$ Pa, residuals of (1) to (4) below $10^{-9}$; the other root gives $p_2 = -6843.3$ Pa $< 0$ and is discarded.
