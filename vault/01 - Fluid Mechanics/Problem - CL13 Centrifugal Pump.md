---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - bomba
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL13.pdf"
id: "cl13"
pill: "CL13: Centrifugal Pump"
tags_html:
  - "Turbomachine"
  - "Angular momentum"
  - "Euler torque"
  - "Pump power"
---

# Problem CL13: Centrifugal Pump: Exit Velocity, Axial Force, Torque and Power

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The figure of CL13.pdf shows a sketch of a centrifugal pump. Water enters the pump with uniform axial velocity $V_o$ and pressure $p_o$ through a circular pipe of diameter $D_o$. The internal geometry of the pump includes rotating blades that redirect the flow, so that the water leaves the pump with zero axial velocity through a lateral exit of width $h$ and diameter $D$. At the exit section, the pressure is $p_s \ne p_a$ and the velocity vector, of magnitude $V_s$, forms an angle $\alpha$ with the lateral surface, as indicated in the figure, i.e., the corresponding normal and tangential velocity components are $V_s\sin\alpha$ and $V_s\cos\alpha$, respectively. Assuming that the effect of gravity is negligible and that the water temperature at the exit is equal to that found at the entrance (handwritten addition: and that the pump walls are insulated), determine the values of the:

- Radial velocity component at the exit section $V_s\sin\alpha$.
- Axial force exerted on the pump.
- Torque exerted on the pump.
- Power of the pump, assumed to be ideal (i.e., work per unit time exerted on the water stream by the rotating parts).

Note: besides the water density $\rho$ and the ambient pressure $p_a$, the following quantities can be assumed to be known in solving the problem: $D$, $D_o$, $h$, $\alpha$, $V_o$, $p_o$, and $p_s$.

![[attachments/FM-T3/cl13-statement.png]]
*Statement figure (CL13.pdf, p. 1, cropped): inlet $D_o$ ($V_o$, $p_o$), lateral exit of width $h$ and diameter $D$, exit velocity $V_s$ at the angle $\alpha$ with the lateral surface; the surface names are handwritten on the official sheet*

Source: CL13.pdf (page 1, exam of Jan 10, 2012). Notes.pdf, Chapter 3: integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady (on average), incompressible water; neglect $\bar{g}$; equal temperature at entrance and exit ($e_s = e_o$); insulated walls; uniform properties at both sections.
- The outer casing is surrounded by air at $p_a$ (gauge pressure $p - p_a$ in the force).
- Data: $[\rho,\ p_a,\ D,\ D_o,\ h,\ \alpha,\ V_o,\ p_o,\ p_s]$. Unknowns: $[V_s\sin\alpha,\ F_x,\ \bar{M},\ \dot{W}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $D_o$, $V_o$, $p_o$ | inlet diameter, velocity, pressure | m, m/s, Pa |
| $D$, $h$ | exit diameter and width | m |
| $V_s$, $\alpha$, $p_s$ | exit velocity, angle, pressure | m/s, rad, Pa |
| $\dot{W}$ | power given to the water by the blades | W |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the casing; $\bar{e}_x$ along the axis (inlet flow direction); cylindrical basis $(\bar{e}_r, \bar{e}_\theta)$ around $\bar{e}_x$ with $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_x$; origin on the axis in the exit plane. Over a full turn, $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$.
- Surfaces: $\Sigma_o$ (inlet disc, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (lateral exit cylinder, radius $D/2$, width $h$, $\bar{n} = \bar{e}_r$, $\bar{v} = V_s\sin\alpha\,\bar{e}_r + V_s\cos\alpha\,\bar{e}_\theta$), $\Sigma_w$ (fixed casing) and $\Sigma_b$ (rotating blades).

![[attachments/FM-T3/cl13-cv.svg]]
*Control volume of the solution: $\Sigma_o$ (inlet disc, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (lateral exit cylinder of radius $D/2$ and width $h$, $\bar{n} = \bar{e}_r$), the fixed casing $\Sigma_w$ and the rotating blades $\Sigma_b$ (schematic); on the right, the exit velocity $V_s$ at the angle $\alpha$ with the lateral surface: normal component $V_s\sin\alpha$, tangential $V_s\cos\alpha$*

$$ \boxed{\,\bar{F} = \int_{\Sigma_w,\Sigma_b}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\bar{M} = \int_{\Sigma_w,\Sigma_b}\bar{x}\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.10)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_o$ | $-\rho V_o\frac{\pi D_o^2}{4}$ |
| $\Sigma_s$ | $+\rho V_s\sin\alpha\,\pi Dh$ |
| $\Sigma_w,\ \Sigma_b$ | $0$ |

$$ \boxed{\,V_s\sin\alpha = \frac{D_o^2}{4Dh}\,V_o\,},\qquad \dot{m} = \rho V_o\frac{\pi D_o^2}{4} \tag{1} $$

**Linear momentum, axial component (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho v_x\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_a)\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_o$ | $-\rho V_o^2\frac{\pi D_o^2}{4}$ | $+(p_o - p_a)\frac{\pi D_o^2}{4}$ | $0$ |
| $\Sigma_s$ | $0$ ($v_x = 0$) | $0$ ($n_x = 0$) | $0$ |
| **$\Sigma_w,\ \Sigma_b$** (boxed) | $0$ | $-\int(p - p_a)\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |

Boxed terms: $-F_x$. The radial and azimuthal components vanish because $\int\bar{e}_r\,d\theta = \int\bar{e}_\theta\,d\theta = 0$.

$$ \boxed{\,\bar{F} = \frac{\pi D_o^2}{4}\left[\rho V_o^2 + (p_o - p_a)\right]\bar{e}_x\,} \tag{2} $$

**Angular momentum about the axis (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,\bar{x}\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,(\bar{x}\wedge\bar{v})[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}\bar{x}\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{x}\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{x}\wedge\bar{v})_x\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $\text{pressure and viscous moments}$ |
| :--- | :--- | :--- |
| $\Sigma_o$ | $0$ ($\bar{v} \parallel \bar{e}_x$, no swirl) | $0$ |
| $\Sigma_s$ | $\rho V_s\sin\alpha\,\pi Dh\,\frac{D}{2}V_s\cos\alpha = \dot{m}\,\frac{D}{2}\,V_s\cos\alpha$ | $0$ ($\bar{x}\wedge\bar{e}_r$ has no $x$ component) |
| **$\Sigma_w,\ \Sigma_b$** (boxed) | $0$ | $-\bar{M}\cdot\bar{e}_x$ |

On $\Sigma_s$, $\bar{x} = \frac{D}{2}\bar{e}_r + x\bar{e}_x$, and the $x$ component of $\bar{x}\wedge\bar{v}$ is $\frac{D}{2}V_s\cos\alpha$ (from $\bar{e}_r\wedge\bar{e}_\theta = \bar{e}_x$). The mass flux in front of it is (1).

$$ \boxed{\,\bar{M} = -\rho V_o\frac{\pi D_o^2}{4}\,V_s\cos\alpha\,\frac{D}{2}\,\bar{e}_x\,} \tag{3} $$

**Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_o$ | $-\dot{m}\left(e_o + \tfrac{V_o^2}{2}\right)$ | $+p_oV_o\frac{\pi D_o^2}{4}$ | $0$ | $0$ |
| $\Sigma_s$ | $+\dot{m}\left(e_s + \tfrac{V_s^2}{2}\right)$ | $-p_sV_s\sin\alpha\,\pi Dh$ | $0$ | $0$ |
| **$\Sigma_b$** (boxed) | $0$ | $-\int_{\Sigma_b}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_b}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $0$ |
| $\Sigma_w$ | $0$ | $0$ | $0$ | $0$ (insulated) |

Boxed $\Sigma_b$ terms: the power $\dot{W}$ of the blades. With $e_s = e_o$ and (1):

$$ \boxed{\,\dot{W} = \rho V_o\frac{\pi D_o^2}{4}\left[\left(\frac{p_s}{\rho} + \frac{V_s^2}{2}\right) - \left(\frac{p_o}{\rho} + \frac{V_o^2}{2}\right)\right]\,} \tag{4} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- (3) is the reaction to the angular momentum given to the water: the blades give the water the swirl $V_s\cos\alpha$ at radius $D/2$, and the water acts on the pump with the opposite torque (Euler's turbomachinery relation; the motor must supply it).
- (4): the ideal power raises the total pressure $p + \tfrac{1}{2}\rho V^2$ of the water flow rate $\dot{m}/\rho$.
- Dimensions (SI): $[\dot{m}\,D\,V_s] = \text{N}\cdot\text{m}$; $[\dot{m}\,p/\rho] = \text{W}$; $[D_o^2V_o/(Dh)] = \text{m/s}$.
- Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $D = 0.3$ m, $D_o = 0.1$ m, $h = 0.02$ m, $\alpha = 30^\circ$, $V_o = 3$ m/s, $p_o = 1.2\times10^5$ Pa, $p_s = 2.5\times10^5$ Pa, $p_a = 101325$ Pa give $V_s\sin\alpha = 1.25$ m/s ($V_s = 2.5$ m/s), $F_x = 217.36$ N, $|\bar{M}| = 7.652$ N$\cdot$m, $\dot{W} = 3030.7$ W.
- Agreement with the official solution: CL13.pdf obtains (1) to (4).
