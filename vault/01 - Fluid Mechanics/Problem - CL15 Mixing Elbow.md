---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - mezcla
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL15.pdf"
id: "cl15"
pill: "CL15: Mixing Elbow"
tags_html:
  - "Two inlets"
  - "Mixing"
  - "Energy"
  - "Angular momentum"
---

# Problem CL15: Mixing Elbow: Exit Velocity and Temperature, Force and Torque

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

Consider the mixing elbow shown schematically in the figure of CL15.pdf. Cold water flows through the main pipe and mixes with warmer water that enters through a smaller inlet located at the elbow. The liquid properties can be considered independent of the temperature and gravity effects can be neglected. All pipe walls are adiabatic. The known pipe dimensions, fluid properties and boundary conditions are given in the figure (as read from it: density $\rho$, viscosity $\mu$, conductivity $k$, specific heat $c$; main inlet $v_1$, $p_1$, $T_1$, diameter $D_1$; secondary inlet $v_2$, $p_2$, $T_2$, diameter $D_2$; exit at $p_a$). Assume that the two streams mix completely and that the velocity and temperature are uniform at the exit section.

- Find the velocity $v_s$ and temperature $T_s$ of the mixed stream emerging from the pipe at ambient pressure.
- Obtain the net force $\bar{F}$ exerted on the mixing elbow by the water flowing inside and the ambient air.
- Obtain the torque $\bar{M}_1$ about the point $\bar{x}_1$ located at the center of the larger inlet.
- Compute the above results numerically, given the following data: $v_1 = 0.4$ m/s; $v_2 = 1.2$ m/s; $\rho = 1000$ kg/m$^3$; $T_1 = 20^\circ$C; $T_2 = 40^\circ$C; $\mu = 8\times10^{-4}$ Pa s; $p_1 - p_a = 50$ Pa; $p_2 - p_a = 200$ Pa; $k = 0.677$ W/(m s) [sic: the dimensions of a conductivity are W/(m K)]; $D_1 = 10$ cm; $D_2 = 2.5$ cm; $c = 4216$ J/(kg K); $L_1 = 20$ cm; $L_2 = 7$ cm.

![[attachments/FM-T3/cl15-statement.svg]]
*Statement figure (redrawn from CL15.pdf, p. 1): main inlet ($D_1$, $v_1$, $p_1$, $T_1$, centre $\bar{x}_1$), bend and exit pipe of length $L_1$ discharging at $p_a$; secondary inlet ($D_2$, $v_2$, $p_2$, $T_2$) at the elbow, $L_2$ below the main axis; the thin lines are the axes of the official figure*

Source: CL15.pdf (pages 1-2, exam of Dec 18, 2012, with solution). Notes.pdf, Chapter 3: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible liquid with constant properties, $e = e_0 + cT$; neglect $\bar{g}$; adiabatic walls; uniform properties at the three sections; complete mixing.
- Geometry (figure): main inlet along $+\bar{e}_x$ (section $A_1 = \pi D_1^2/4$), secondary inlet along $+\bar{e}_y$ ($A_2 = \pi D_2^2/4$), exit along $+\bar{e}_y$ (section $A_1$) at $p_a$. The secondary inlet and the exit share the same vertical axis, at a horizontal distance $L_1 + D_1 + D_1/2 = L_1 + \tfrac{3}{2}D_1$ from $\bar{x}_1$ (bend of inner radius $D_1$; reading of the figure, as in the official solution).
- Data: as listed. Unknowns: $[v_s,\ T_s,\ \bar{F},\ \bar{M}_1]$. $\mu$, $k$ and $L_2$ are not needed.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $v_1$, $v_2$, $v_s$ | inlet and exit velocities | m/s |
| $T_1$, $T_2$, $T_s$ | temperatures | K (the data are given in $^\circ$C) |
| $p_1 - p_a$, $p_2 - p_a$ | inlet gauge pressures | Pa |
| $D_1$, $D_2$, $L_1$ | diameters and length | m |
| $\bar{F}$, $\bar{M}_1$ | force and torque on the elbow | N, N$\cdot$m |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the elbow: $\bar{e}_x$ horizontal (main inlet flow), $\bar{e}_y$ vertical upwards, $\bar{e}_z$ towards the reader; moments about $\bar{x}_1$.
- Surfaces (fixed CV, as in the official solution): $\Sigma_1$ (main inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (secondary inlet, $\bar{n} = -\bar{e}_y$), $\Sigma_{out}$ (exit, $\bar{n} = +\bar{e}_y$), $\Sigma_{wall}$.

![[attachments/FM-T3/cl15-cv.svg]]
*Control volume of the solution: $\Sigma_1$ (main inlet, $\bar{n} = -\bar{e}_x$), $\Sigma_2$ (secondary inlet, $\bar{n} = -\bar{e}_y$), $\Sigma_{out}$ (exit, $\bar{n} = +\bar{e}_y$) and $\Sigma_{wall}$; moments about $\bar{x}_1$*

$$ \boxed{\,\bar{F} = -\int_{\Sigma_{wall}}\left[-(p - p_a)\,\bar{n} + \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\bar{M}_1 = -\int_{\Sigma_{wall}}(\bar{x} - \bar{x}_1)\wedge\left[-(p - p_a)\,\bar{n} + \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $-\rho v_1A_1$ |
| $\Sigma_2$ | $-\rho v_2A_2$ |
| $\Sigma_{out}$ | $+\rho v_sA_1$ |
| $\Sigma_{wall}$ | $0$ |

$$ v_1A_1 + v_2A_2 = v_sA_1 \;\Longrightarrow\; \boxed{\,v_s = v_1 + v_2\left(\frac{D_2}{D_1}\right)^2\,} \tag{1} $$

**Total energy (Notes Eq. 3.46; $Q_R \equiv Q_c + Q_r$ is the volumetric heat release)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-\rho\left(e_1 + \tfrac{v_1^2}{2}\right)v_1A_1$ | $+p_1v_1A_1$ | $0$ | $0$ |
| $\Sigma_2$ | $-\rho\left(e_2 + \tfrac{v_2^2}{2}\right)v_2A_2$ | $+p_2v_2A_2$ | $0$ | $0$ |
| $\Sigma_{out}$ | $+\rho\left(e_s + \tfrac{v_s^2}{2}\right)v_sA_1$ | $-p_av_sA_1$ | $0$ | $0$ |
| $\Sigma_{wall}$ | $0$ | $0$ | $0$ | $0$ (adiabatic) |

With $e = e_0 + cT$, dividing by $\rho c\,v_sA_1$ ($e_0$ cancels by (1)) and writing $p_a$ as $p_a(v_1A_1 + v_2A_2)/(v_sA_1)$:

$$ \boxed{\,T_s = \left(T_1 + \frac{p_1 - p_a}{\rho c} + \frac{v_1^2}{2c}\right)\frac{v_1}{v_s} + \left(T_2 + \frac{p_2 - p_a}{\rho c} + \frac{v_2^2}{2c}\right)\frac{v_2A_2}{v_sA_1} - \frac{v_s^2}{2c}\,} \tag{2} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $-\rho v_1^2A_1\,\bar{e}_x$ | $(p_1 - p_a)A_1\,\bar{e}_x$ | $0$ |
| $\Sigma_2$ | $-\rho v_2^2A_2\,\bar{e}_y$ | $(p_2 - p_a)A_2\,\bar{e}_y$ | $0$ |
| $\Sigma_{out}$ | $+\rho v_s^2A_1\,\bar{e}_y$ | $0$ ($p = p_a$) | $0$ |
| **$\Sigma_{wall}$** (boxed) | $0$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F}$.

$$ \boxed{\,\bar{F} = \left(\rho v_1^2 + p_1 - p_a\right)A_1\,\bar{e}_x + \left[\left(\rho v_2^2 + p_2 - p_a\right)A_2 - \rho v_s^2A_1\right]\bar{e}_y\,} \tag{3} $$

**Angular momentum about x̄₁ (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,(\bar{x} - \bar{x}_1)\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,[(\bar{x} - \bar{x}_1)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,[(\bar{x} - \bar{x}_1)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $0$ (centred at $\bar{x}_1$) | $0$ | $0$ |
| $\Sigma_2$ | $-\rho v_2^2A_2\,d\,\bar{e}_z$ | $(p_2 - p_a)A_2\,d\,\bar{e}_z$ | $0$ |
| $\Sigma_{out}$ | $+\rho v_s^2A_1\,d\,\bar{e}_z$ | $0$ | $0$ |
| **$\Sigma_{wall}$** (boxed) | $0$ | $-\int(\bar{x} - \bar{x}_1)\wedge(p - p_a)\bar{n}\,d\sigma$ | $\int(\bar{x} - \bar{x}_1)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |

Boxed terms: $-\bar{M}_1$. With $d = L_1 + \tfrac{3}{2}D_1$ the horizontal distance to the common vertical axis, $(\bar{x} - \bar{x}_1)\wedge\bar{e}_y = d\,\bar{e}_x\wedge\bar{e}_y = d\,\bar{e}_z$ for the centres of $\Sigma_2$ and $\Sigma_{out}$ (the vertical offsets are parallel to $\bar{e}_y$ and drop out).

$$ \boxed{\,\bar{M}_1 = \left[\left(\rho v_2^2 + p_2 - p_a\right)A_2 - \rho v_s^2A_1\right]\left(L_1 + \frac{3}{2}D_1\right)\bar{e}_z\,} \tag{4} $$

### Numerical values (part 4)

| Quantity | Value |
| :--- | :--- |
| $v_s$ | $0.475$ m/s |
| $T_s$ | $23.16\ ^\circ$C |
| $\bar{F}$ | $1.65\,\bar{e}_x -0.967\,\bar{e}_y$ N |
| $\bar{M}_1$ | $-0.338\,\bar{e}_z$ N$\cdot$m |

## Phase 4: Interpretation, Limits and Dimensional Check

- (2) is a mass-weighted average of the inlet temperatures, corrected by the tiny flow-work and kinetic-energy terms ($\Delta p/(\rho c) \sim 10^{-5}$ K here): $T_s \approx (v_1A_1T_1 + v_2A_2T_2)/(v_sA_1)$.
- $F_y < 0$: the exit momentum flux exceeds the momentum and gauge pressure brought in by the small inlet, so the elbow is pulled downwards; $\bar{M}_1$ follows from the same vertical imbalance acting at the arm $d$.
- Dimensions (SI): $[(p - p_a)/(\rho c)] = \text{K}$, $[v^2/c] = \text{K}$; $[\rho v^2A] = \text{N}$; $[\rho v^2Ad] = \text{N}\cdot\text{m}$.
- Agreement with the official solution: CL15.pdf obtains (1) to (4) and $v_s = 0.475$ m/s, $T_s = 23^\circ$C, $\bar{F} = 1.65\,\bar{e}_x - 0.967\,\bar{e}_y$ N, $\bar{M}_1 = -0.338\,\bar{e}_z$ N$\cdot$m, the same values.
