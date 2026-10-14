---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - vtol
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL11.pdf"
---

# Problem CL11: VTOL Propulsion Device in Hover: Nozzle Angle and Flow State

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The propulsion device of a VTOL (vertical take-off and landing) aircraft includes a horizontal intake of cross section $A_i$ and a thrust vectoring nozzle of variable angle $\alpha$ and exit cross section $A_e$. When the aircraft is hovering (suspended at a fixed point), the engine must provide a force $\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y$, such that the lift $F_y$ equals the weight of the aircraft ($Mg$), while the thrust $F_x$ is identically zero. The work per unit time on the air stream through the mobile blades is $W$ and the amount of heat added per unit time is $Q$ (including heat losses through the walls). For the analysis of the problem, one may introduce the following assumptions regarding the air motion:

- The effect of gravity is entirely negligible.
- Flow properties at the entrance and exit sections are uniform.
- The air around the engine casing is at rest with uniform pressure $p_a$.
- Upstream from the inlet the flow is inviscid and with constant density, such that $\rho_i = \rho_a$ and one may use Bernoulli's equation along any streamline to relate the ambient pressure $p_a$ with that found at the entrance $p_i$.

With the above simplifications, write the equations that determine the values of $U_i$, $U_e$, $p_i$, $\rho_e$ and $\alpha$ in terms of the known quantities ($p_a$, $Mg$, $\rho_a$, $A_i$, $A_e$, $\gamma$, $W$, and $Q$).

![[attachments/FM-T3/cl11-statement.svg]]
*Statement figure (redrawn from CL11.pdf, p. 1): intake $A_i$ ($p_i$, $U_i$, $\rho_a$), heat $Q$ and blades $W$ inside the duct, nozzle of exit section $A_e$ at the angle $\alpha$ from the vertical ($U_e$, $\rho_e$, $p_a$); axes $x$, $y$ at the centre of the rotating joint*

Source: CL11.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.

## Phase 1: Hypotheses, Data and Unknowns

- Steady (on average); neglect $\bar{g}$; uniform properties at $i$ and $e$; perfect gas, $h = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$; ambient air at rest at $p_a$ around the casing.
- Inlet: $\rho_i = \rho_a$ (constant density upstream) and Bernoulli from the still air to the inlet. Exit: free jet at $p_a$, density $\rho_e$.
- Geometry (figure): air enters along $-\bar{e}_x$ through the horizontal intake; the jet leaves downwards and backwards, $\bar{v}_e = -U_e(\sin\alpha\,\bar{e}_x + \cos\alpha\,\bar{e}_y)$, with $\alpha$ measured from the vertical.
- Hover: $F_x = 0$, $F_y = Mg$. Data: $[p_a,\ \rho_a,\ Mg,\ A_i,\ A_e,\ \gamma,\ \dot{W},\ \dot{Q}]$. Unknowns: $[U_i,\ U_e,\ p_i,\ \rho_e,\ \alpha]$: five equations are needed.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A_i$, $A_e$ | intake and exit areas | m$^2$ |
| $U_i$, $U_e$ | intake and exit velocities | m/s |
| $p_i$, $\rho_e$ | intake pressure, exit density | Pa, kg/m$^3$ |
| $\alpha$ | nozzle angle from the vertical | rad |
| $\dot{W}$, $\dot{Q}$ | power and heat given to the air | W |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the hovering aircraft (inertial while hovering); $\bar{e}_x$ horizontal, $\bar{e}_y$ vertical upwards.
- Surfaces: $\Sigma_i$ (intake, $\bar{n} = +\bar{e}_x$, $\bar{v} = -U_i\bar{e}_x$), $\Sigma_e$ (exit, $\bar{n} = \bar{v}_e/U_e$), $\Sigma_w$ (fixed walls) and $\Sigma_m$ (mobile blades).

![[attachments/FM-T3/cl11-cv.svg]]
*Control volume of the solution: $\Sigma_i$ (intake, $\bar{n} = +\bar{e}_x$, $\bar{v} = -U_i\bar{e}_x$), $\Sigma_e$ (exit, $\bar{n} = \bar{v}_e/U_e$), the fixed walls $\Sigma_w$ and the mobile blades $\Sigma_m$ (dashed around them)*

$$ \boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,}\qquad(\text{force of the air on the engine}) $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.10)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_i$ | $\rho_a(-U_i)A_i$ |
| $\Sigma_e$ | $+\rho_eU_eA_e$ |
| $\Sigma_w,\ \Sigma_m$ | $0$ |

$$ \boxed{\,\rho_aU_iA_i = \rho_eU_eA_e = \dot{m}\,} \tag{1} $$

Entrance region (Notes Eq. 4.17, from the still ambient air to the inlet):

$$ \boxed{\,p_a = p_i + \tfrac{1}{2}\rho_aU_i^2\,} \tag{2} $$

**Linear momentum (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $\rho_a(-U_i\bar{e}_x)(-U_i)A_i = \rho_aU_i^2A_i\,\bar{e}_x$ | $-(p_i - p_a)A_i\,\bar{e}_x$ | $0$ |
| $\Sigma_e$ | $-\rho_eU_e^2A_e(\sin\alpha\,\bar{e}_x + \cos\alpha\,\bar{e}_y)$ | $0$ (free jet) | $0$ |
| **$\Sigma_w,\ \Sigma_m$** (boxed) | $0$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F} = -F_x\bar{e}_x - F_y\bar{e}_y$. $x$ component with $F_x = 0$, (2) and (1): $\rho_aU_i^2A_i - \rho_eU_e^2A_e\sin\alpha = \tfrac{1}{2}\rho_aU_i^2A_i$, i.e. $\tfrac{1}{2}\rho_aU_i^2A_i = \rho_aU_iA_i\,U_e\sin\alpha$. $y$ component with $F_y = Mg$: $-\rho_eU_e^2A_e\cos\alpha = -Mg$.

$$ \boxed{\,U_i = 2\,U_e\sin\alpha\,}\ \ \text{(3)}\qquad \boxed{\,Mg = \rho_eU_e^2A_e\cos\alpha = \rho_aU_i^2A_i\,\frac{\cos\alpha}{2\sin\alpha}\,}\ \ \text{(4)} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \int_{V_c}Q_R\,dV $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_i$ | $-\dot{m}\left(e_i + \tfrac{U_i^2}{2}\right)$ | $+p_iU_iA_i$ | $0$ | $0$ |
| $\Sigma_e$ | $+\dot{m}\left(e_e + \tfrac{U_e^2}{2}\right)$ | $-p_aU_eA_e$ | $0$ | $0$ |
| **$\Sigma_m$** (boxed) | $0$ | $-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int_{\Sigma_m}\bar{q}\cdot\bar{n}\,d\sigma$ |
| **$\Sigma_w$** (boxed) | $0$ | $0$ | $0$ | $-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed terms: the work on $\Sigma_m$ is $\dot{W}$; the heat through the walls plus the volume term $\int_{V_c}Q_R\,dV$ is $\dot{Q}$ (net, including the losses). With $h = e + p/\rho = \frac{\gamma}{\gamma-1}\frac{p}{\rho}$:

$$ \boxed{\,\rho_aU_iA_i\left[\left(\frac{\gamma}{\gamma - 1}\frac{p_a}{\rho_e} + \frac{U_e^2}{2}\right) - \left(\frac{\gamma}{\gamma - 1}\frac{p_i}{\rho_a} + \frac{U_i^2}{2}\right)\right] = \dot{W} + \dot{Q}\,} \tag{5} $$

(1) to (5) are five equations for $U_i$, $U_e$, $p_i$, $\rho_e$ and $\alpha$, which answers the question.

## Phase 4: Interpretation, Limits and Dimensional Check

- (3) says that the backward component of the jet momentum must cancel the intake momentum plus the suction force at the intake: because the intake is at a lower pressure than ambient (2), only half of $\rho_aU_i^2A_i$ has to be balanced.
- (4): the lift is the vertical momentum flux of the jet. For $\alpha \to 0$ (vertical jet), (3) would require $U_i \to 0$: the intake momentum could not be balanced, so a hovering engine with a horizontal intake needs $\alpha > 0$.
- Dimensions (SI): $[\rho_eU_e^2A_e] = \text{N} = [Mg]$; $[\dot{m}\,\gamma p/((\gamma-1)\rho)] = \text{W}$.
- Numerical illustration (hypothetical data, solved by Newton's method on the two equations left after eliminating $U_i$, $p_i$, $\rho_e$): $\rho_a = 1.2$ kg/m$^3$, $p_a = 101325$ Pa, $A_i = 2.5$ m$^2$, $A_e = 1.2$ m$^2$, $Mg = 80$ kN, $\dot{W} + \dot{Q} = 6$ MW, $\gamma = 1.4$ give $U_e = 212.22$ m/s, $\alpha = 71.85^\circ$, $U_i = 403.32$ m/s, $p_i = 3727.19$ Pa, $\rho_e = 4.7511$ kg/m$^3$ (residuals below $10^{-6}$).
- Agreement with the official solution: CL11.pdf obtains (1) to (5).
