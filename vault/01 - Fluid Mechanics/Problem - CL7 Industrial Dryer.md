---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - secador
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL7.pdf"
---

# Problem CL7: Industrial Dryer: Velocities, Force, Power and Torque

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The axisymmetric industrial dryer of the figure in CL7.pdf is designed to provide a steady hot jet of radius $R$, mass flux $G$, and temperature $T_s$. Air enters the dryer from the ambient, at temperature and pressure $T_a$ and $p_a$, through a radial inlet of surface $A$. Inside the dryer there exists an electric resistance that releases an amount of heat $Q$ per unit time, as well as a fan of power $W$ (work per unit time). Because of the presence of the fan, the air velocity at the exit has both azimuthal and axial components, $v_\theta$ and $v_z$, such that $v_\theta/v_z = \tan(\beta)$. In the analysis, assume that the fan and the inner walls of the dryer are thermally insulated, that the air behaves as an ideal gas with constant $R_g$ and specific heat at constant pressure $c_p$, that gravity has a negligible effect on the fluid motion, and that the flow properties are uniform at the inlet and outlet sections. For given values of $G$, $T_s$, $T_a$, $p_a$, $A$, $R$, $R_g$, $c_p$ and $\tan(\beta)$, determine:

- The velocity at the entrance section $v_r$ as well as the two velocity components at the exit $v_\theta$ and $v_z$.
- The force acting on the dryer, indicating clearly its magnitude and direction.
- The total power required to run the dryer $Q + W$.
- The torque acting on the dryer.

Source: CL7.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady (on average) axisymmetric flow; ideal gas $p = \rho R_gT$, so $h = e + p/\rho = c_pT$; neglect $\bar{g}$; uniform properties at inlet and outlet.
- Inlet: air taken from the ambient, with $p = p_a$, $T = T_a$, $\rho_a = p_a/(R_gT_a)$ and radial velocity $v_r$ pointing inwards (as in the official solution). Exit: free jet, $p = p_a$, $T = T_s$, $\rho_s = p_a/(R_gT_s)$, velocity $v_z\bar{e}_z + v_\theta\bar{e}_\theta$ uniform over the disc of radius $R$.
- $G$ is the mass flow rate of the jet (kg/s), as used in the official solution ($G = \rho_av_rA$). Fan and inner walls insulated; the resistance releases $\dot{Q}$; the fan delivers the power $\dot{W}$ to the air.
- Data: $[G,\ T_s,\ T_a,\ p_a,\ A,\ R,\ R_g,\ c_p,\ \tan\beta]$. Unknowns: $[v_r,\ v_z,\ v_\theta,\ \bar{F},\ \dot{Q} + \dot{W},\ \bar{M}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $G$ | mass flow rate | kg/s |
| $A$, $R$ | inlet area, jet radius | m$^2$, m |
| $v_r$, $v_z$, $v_\theta$ | inlet and exit velocities | m/s |
| $R_g$, $c_p$ | gas constant, specific heat | J/(kg$\cdot$K) |
| $\bar{F}$, $\bar{M}$ | force and torque on the dryer | N, N$\cdot$m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the dryer; cylindrical basis $(\bar{e}_r, \bar{e}_\theta, \bar{e}_z)$ with $\bar{e}_z$ along the axis in the jet direction; origin on the axis. By axisymmetry $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$ over a full turn.
- Surfaces: $\Sigma_1$ (radial inlet, area $A$, $\bar{n} = \bar{e}_r$, $\bar{v} = -v_r\bar{e}_r$), $\Sigma_2$ (exit disc, $\bar{n} = \bar{e}_z$), $\Sigma_w$ (fixed casing and resistance, $\bar{v} = 0$) and $\Sigma_m$ (fan blades, $\bar{v} = \bar{v}_c$).

Force and torque of the air (inside, and ambient outside) on the dryer, and the heat and work exchanged:

$$ \boxed{\,\bar{F} = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\,\bar{M} = \int_{\Sigma_w,\Sigma_m}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $\rho_a(-v_r)A = -\rho_av_rA$ |
| $\Sigma_2$ | $\rho_sv_z\pi R^2$ |
| $\Sigma_w,\ \Sigma_m$ | $0$ |

$$ G = \frac{p_a}{R_gT_a}\,v_rA = \frac{p_a}{R_gT_s}\,v_z\pi R^2 \;\Longrightarrow\; \boxed{\,v_r = \frac{GR_gT_a}{p_aA},\qquad v_z = \frac{GR_gT_s}{p_a\pi R^2},\qquad v_\theta = v_z\tan\beta\,} \tag{1} $$

**Linear momentum (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $\rho_av_r^2\int_{\Sigma_1}\bar{e}_r\,d\sigma = 0$ (axisymmetric) | $0$ ($p = p_a$) | $0$ |
| $\Sigma_2$ | $\rho_sv_z\int_{\Sigma_2}(v_z\bar{e}_z + v_\theta\bar{e}_\theta)\,d\sigma = \rho_sv_z^2\pi R^2\,\bar{e}_z$ | $0$ (free jet) | $0$ |
| **$\Sigma_w,\ \Sigma_m$** (boxed) | $0$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F}$. On $\Sigma_2$, $\int_{\Sigma_2}\bar{e}_\theta\,d\sigma = 0$, so the swirl gives no force.

$$ \rho_sv_z^2\pi R^2\,\bar{e}_z = -\bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = -\frac{p_a}{R_gT_s}\,v_z^2\,\pi R^2\,\bar{e}_z = -G\,v_z\,\bar{e}_z\,} \tag{2} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-G\left(e_a + \tfrac{v_r^2}{2}\right)$ | $+p_av_rA$ | $0$ | $0$ |
| $\Sigma_2$ | $+G\left(e_s + \tfrac{v_\theta^2 + v_z^2}{2}\right)$ | $-p_av_z\pi R^2$ | $0$ | $0$ |
| **$\Sigma_m$** (boxed) | $0$ | $-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $0$ (insulated) |
| **$\Sigma_w$** (boxed) | $0$ | $0$ | $0$ | $-\int_{\Sigma_w}\bar{q}\cdot\bar{n}\,d\sigma$ |

Boxed terms: the work on $\Sigma_m$ is the fan power $\dot{W}$; the heat through $\Sigma_w$ (only the resistance, the walls are insulated) is $\dot{Q}$. With $p_av_rA = G\,p_a/\rho_a$ and $p_av_z\pi R^2 = G\,p_a/\rho_s$, $e + p/\rho = c_pT$:

$$ \boxed{\,\dot{Q} + \dot{W} = G\left[\left(c_pT_s + \frac{v_\theta^2 + v_z^2}{2}\right) - \left(c_pT_a + \frac{v_r^2}{2}\right)\right]\,} \tag{3} $$

**Angular momentum about the origin, z component (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})_z\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $\text{pressure and viscous moments}$ |
| :--- | :--- | :--- |
| $\Sigma_1$ | $0$ ($\bar{x}\wedge(-v_r\bar{e}_r) = -zv_r\,\bar{e}_\theta$, no $z$ component) | $0$ |
| $\Sigma_2$ | $\int_0^R\rho_sv_z\,(rv_\theta)\,2\pi r\,dr = \rho_sv_zv_\theta\,\frac{2\pi R^3}{3}$ | $0$ |
| **$\Sigma_w,\ \Sigma_m$** (boxed) | $0$ | $-\bar{M}\cdot\bar{e}_z$ |

On $\Sigma_2$, $\bar{x} = r\bar{e}_r + z_2\bar{e}_z$ and $\bar{x}\wedge(v_z\bar{e}_z + v_\theta\bar{e}_\theta) = -rv_z\bar{e}_\theta + rv_\theta\bar{e}_z - z_2v_\theta\bar{e}_r$; only $rv_\theta\bar{e}_z$ survives the integral. The antiderivative of $r^2$ is $r^3/3$, and Barrow's rule between $0$ and $R$ gives $R^3/3$.

$$ \boxed{\,\bar{M} = -\rho_sv_zv_\theta\,\frac{2\pi R^3}{3}\,\bar{e}_z = -\frac{2}{3}\,R\,G\,v_\theta\,\bar{e}_z\,} \tag{4} $$

> [!warning] Erratum in the official solution (slip in the boxed result)
> CL7.pdf writes the momentum balance as $\frac{p_a}{R_gT_s}v_z^2\pi R^2\bar{e}_z = -\bar{F}$ but boxes $\bar{F} = -\frac{p_a}{R_gT_s}v_z^2\bar{e}_z$, without the area $\pi R^2$. That expression has units of pressure, not force; the correct result is (2).

## Phase 4: Interpretation, Limits and Dimensional Check

- The radial inflow gives no net momentum (axisymmetry), so the force is the reaction to the jet: magnitude $Gv_z$, direction $-\bar{e}_z$ (opposite to the jet).
- The swirl gives no force but gives a torque: the fan sets the air rotating, and the air reacts on the dryer with $\bar{M}$ opposite to the swirl. For $\beta = 0$, $v_\theta = 0$ and $\bar{M} = 0$.
- (3): the electric and mechanical power go into heating the air from $T_a$ to $T_s$ and into its kinetic energy.
- Dimensions (SI): $[Gv_z] = \text{N}$; $[RGv_\theta] = \text{m}\cdot(\text{kg/s})(\text{m/s}) = \text{N}\cdot\text{m}$; $[Gc_pT] = \text{W}$.
- Numerical illustration (hypothetical data): $G = 0.5$ kg/s, $T_s = 350$ K, $T_a = 293$ K, $p_a = 101325$ Pa, $A = 0.05$ m$^2$, $R = 0.05$ m, $R_g = 287$ J/(kg K), $c_p = 1005$ J/(kg K), $\tan\beta = 0.5$ give $v_r = 8.2991$ m/s, $v_z = 63.112$ m/s, $v_\theta = 31.556$ m/s, $|\bar{F}| = 31.556$ N, $\dot{Q} + \dot{W} = 29870$ W and $|\bar{M}| = 0.52594$ N$\cdot$m (a midpoint quadrature of the torque integral gives the same value).
