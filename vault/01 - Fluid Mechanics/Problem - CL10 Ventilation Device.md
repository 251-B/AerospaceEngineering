---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - ventilador
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL10.pdf"
---

# Problem CL10: Ventilation Device: Velocities, Force and Fan Power

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The ventilation device shown in the figure of CL10.pdf takes air out of a room at pressure $p_a$ through a circular nozzle of diameter $D_e$. The air is discharged to the open atmosphere, also at pressure $p_a$, through a pipe of diameter $D_s < D_e$. To force the air motion the device includes a fan, which exerts a rate of work per unit time $\dot{W}$ on the air stream. To simplify the solution you may assume that the air density $\rho$ and viscosity $\mu$ are constant and that gravity has a negligible effect.

- Using the continuity equation, obtain a relationship between the values of the velocity at the entrance and exit sections $U_e$ and $U_s$, assumed to be uniform.
- Make use of Bernoulli's equation upstream from the entrance section (i.e., along a stream line between (0) and (e)) to obtain an equation for the pressure and velocity at the entrance section $p_e$ and $U_e$.
- Determine the two components of the force $F_x$ and $F_y$ acting on the device. Include in the computation the contribution of the stagnant surrounding air.
- Use the energy equation to compute the value of $U_s$ as a function of the power $\dot{W}$. Assume that the air temperature has the same values at the entrance and exit sections and that the device is thermally insulated.
- Obtain the numerical values of $U_s$, $U_e$, $p_e$, $F_x$ and $F_y$ for $D_e = 2$ m, $D_s = 0.1$ m, $\rho = 1.2$ kg/m$^3$, $\mu = 1.8\times10^{-5}$ kg/(m$\cdot$s), $\dot{W} = 1000$ W, $p_a = 101300$ Pa. Note: the following quantities are known: $D_e$, $D_s$, $\rho$, $\mu$, $\dot{W}$, $p_a$.

Source: CL10.pdf (page 1). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.35, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, constant $\rho$ and $\mu$; neglect $\bar{g}$; uniform properties at $e$ and $s$; same temperature at $e$ and $s$ ($e_e = e_s$); device insulated.
- The air in the room far from the inlet is at rest at $p_a$ (point 0); the exit is a free jet at $p_a$; the outer surface of the device is surrounded by stagnant air at $p_a$ (included through the gauge pressure).
- Geometry (figure): the inlet faces downwards, air enters along $+\bar{e}_y$; the exit pipe points along $+\bar{e}_x$.
- Data: $[D_e,\ D_s,\ \rho,\ \mu,\ \dot{W},\ p_a]$. Unknowns: $[U_e,\ U_s,\ p_e,\ F_x,\ F_y]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $D_e$, $D_s$ | inlet and exit diameters | m |
| $U_e$, $U_s$ | inlet and exit velocities | m/s |
| $p_e$, $p_a$ | inlet and ambient pressures | Pa |
| $\dot{W}$ | fan power given to the air | W |
| $F_x$, $F_y$ | force on the device | N |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the device: $\bar{e}_x$ horizontal (exit direction), $\bar{e}_y$ vertical upwards (inlet flow direction).
- Surfaces: $\Sigma_e$ (inlet, $\bar{n} = -\bar{e}_y$, $\bar{v} = U_e\bar{e}_y$), $\Sigma_s$ (exit, $\bar{n} = +\bar{e}_x$, $\bar{v} = U_s\bar{e}_x$), $\Sigma_w$ (fixed walls) and $\Sigma_m$ (fan).

$$ \boxed{\,\bar{F} = F_x\bar{e}_x + F_y\bar{e}_y = \int_{\Sigma_w,\Sigma_m}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**(1) Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_e$ | $-\rho U_e\frac{\pi D_e^2}{4}$ |
| $\Sigma_s$ | $+\rho U_s\frac{\pi D_s^2}{4}$ |
| $\Sigma_w,\ \Sigma_m$ | $0$ |

$$ \boxed{\,U_e\,D_e^2 = U_s\,D_s^2\,} \tag{1} $$

### (2) Bernoulli from the room (0) to the inlet (e)

$$ p_a + 0 = p_e + \tfrac{1}{2}\rho U_e^2 \;\Longrightarrow\; \boxed{\,p_e = p_a - \tfrac{1}{2}\rho U_e^2\,} \tag{2} $$

**(3) Linear momentum (Notes Eq. 3.35)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_e$ | $\rho U_e\bar{e}_y(-U_e)\frac{\pi D_e^2}{4} = -\rho U_e^2\frac{\pi D_e^2}{4}\bar{e}_y$ | $-(p_e - p_a)(-\bar{e}_y)\frac{\pi D_e^2}{4} = (p_e - p_a)\frac{\pi D_e^2}{4}\bar{e}_y$ | $0$ |
| $\Sigma_s$ | $+\rho U_s^2\frac{\pi D_s^2}{4}\bar{e}_x$ | $0$ (free jet) | $0$ |
| **$\Sigma_w,\ \Sigma_m$** (boxed) | $0$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F}$.

$$ \boxed{\,F_x = -\rho U_s^2\frac{\pi D_s^2}{4},\qquad F_y = \rho U_e^2\frac{\pi D_e^2}{4} + (p_e - p_a)\frac{\pi D_e^2}{4} = \rho U_e^2\frac{\pi D_e^2}{8}\,} \tag{3} $$

The last form of $F_y$ uses (2): $(p_e - p_a) = -\tfrac{1}{2}\rho U_e^2$.

**(4) Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_e$ | $-\dot{m}\left(e_e + \tfrac{U_e^2}{2}\right)$ | $+p_eU_e\frac{\pi D_e^2}{4}$ | $0$ | $0$ |
| $\Sigma_s$ | $+\dot{m}\left(e_s + \tfrac{U_s^2}{2}\right)$ | $-p_aU_s\frac{\pi D_s^2}{4}$ | $0$ | $0$ |
| **$\Sigma_m$** (boxed) | $0$ | $-\int_{\Sigma_m}p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int_{\Sigma_m}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $0$ |
| $\Sigma_w$ | $0$ | $0$ | $0$ | $0$ (insulated) |

Boxed $\Sigma_m$ terms: the fan power $\dot{W}$. With $e_e = e_s$, $\dot{m} = \rho U_s\pi D_s^2/4$ and (2), $\frac{p_a - p_e}{\rho} = \frac{U_e^2}{2}$:

$$ \dot{W} = \dot{m}\left[\frac{p_a - p_e}{\rho} + \frac{U_s^2 - U_e^2}{2}\right] = \dot{m}\,\frac{U_s^2}{2} \;\Longrightarrow\; \boxed{\,\dot{W} = \rho\,\frac{\pi D_s^2}{8}\,U_s^3,\qquad U_s = \left(\frac{8\dot{W}}{\rho\pi D_s^2}\right)^{1/3}\,} \tag{4} $$

### (5) Numerical values

| Quantity | Expression | Value |
| :--- | :--- | :--- |
| $U_s$ | $\left(8\dot{W}/(\rho\pi D_s^2)\right)^{1/3}$ | $59.647$ m/s |
| $U_e$ | $U_s\,(D_s/D_e)^2$ | $0.14912$ m/s |
| $p_e$ | $p_a - \tfrac{1}{2}\rho U_e^2$ | $101299.987$ Pa ($p_a - p_e = 0.0133$ Pa) |
| $F_x$ | $-\rho U_s^2\pi D_s^2/4$ | $-33.531$ N |
| $F_y$ | $\rho U_e^2\pi D_e^2/8$ | $0.04191$ N |

## Phase 4: Interpretation, Limits and Dimensional Check

- The large intake makes the inlet velocity tiny ($U_e \approx 0.15$ m/s), so the suction depression $p_a - p_e$ and $F_y$ are negligible; the force is the reaction to the exit jet, $F_x < 0$ (opposite to the jet).
- The Reynolds numbers, $\rho U_sD_s/\mu \approx 4\times10^5$ and $\rho U_eD_e/\mu \approx 2\times10^4$, are large, which supports neglecting viscous stresses on the sections and using Bernoulli upstream of the inlet (this is where $\mu$ enters).
- Dimensions (SI): $[\rho D_s^2U_s^3] = (\text{kg/m}^3)\,\text{m}^2(\text{m/s})^3 = \text{W}$; $[\rho U^2D^2] = \text{N}$.
- Agreement with the official solution: CL10.pdf obtains (1) to (4), with $F_x = -\rho U_s^2\pi D_s^2/4$, $F_y = \rho U_e^2\pi D_e^2/4 + (p_e - p_a)\pi D_e^2/4$ and $\dot{W} = \rho\pi D_s^2U_s^3/8$; it does not write out the numbers of part 5.
