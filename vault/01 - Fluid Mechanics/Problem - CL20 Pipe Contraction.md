---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - energia
  - contraccion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL20.pdf"
---

# Problem CL20: Pipe Contraction Discharging to the Atmosphere: Velocity, Force and Heating

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A liquid of density $\rho$ and specific heat $c$ flows steadily along a circular pipe of diameter $D$, discharging to the atmosphere, at pressure $p_a$, through a coaxial contraction that ends with a circular orifice of diameter $d$. Upstream from the contraction, the velocity, pressure, and temperature have known uniform values $v_u$, $p_u$, and $T_u$. As a function of these data ($\rho$, $c$, $D$, $d$, $p_a$, $v_u$, $p_u$, $T_u$), obtain explicit expressions for:

- The value of the discharge velocity $v_d$.
- The force acting on the contraction $F$, neglecting in the calculation the effect of gravity.
- The temperature increment $T_d - T_u$. Assume in the calculation that the contraction wall is adiabatic.

Simplify these last two results by further assuming that the effect of viscosity is entirely negligible, so that for this incompressible steady flow Bernoulli's equation can be used to relate the variation of the fluid properties along a given stream line.

Source: CL20.pdf (page 1, final of Jan 21, 2014). Notes.pdf: integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral total energy balance Eq. 3.46, Bernoulli's equation Eq. 4.17.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible liquid, $e = cT$; neglect $\bar{g}$; uniform properties at the upstream section $u$ and at the orifice $d$; adiabatic contraction; free jet at $p_a$.
- Data: $[\rho,\ c,\ D,\ d,\ p_a,\ v_u,\ p_u,\ T_u]$. Unknowns: $[v_d,\ \bar{F},\ T_d - T_u]$, first in general and then in the inviscid (Bernoulli) limit.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $D$, $d$ | pipe and orifice diameters | m |
| $v_u$, $p_u$, $T_u$ | upstream state | m/s, Pa, K |
| $v_d$, $T_d$ | discharge velocity and temperature | m/s, K |
| $\bar{F}$ | force on the contraction | N |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the contraction, $\bar{e}_x$ along the axis. Fixed control volume: the liquid inside the contraction.
- Surfaces: $\Sigma_u$ (upstream section, $\bar{n} = -\bar{e}_x$, area $\pi D^2/4$), $\Sigma_d$ (orifice, $\bar{n} = +\bar{e}_x$, area $\pi d^2/4$), $\Sigma_w$ (contraction wall, outer face at $p_a$).

$$ \boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

## Phase 3: Balances, Surface by Surface

**1. Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_u$ | $-\rho v_u\frac{\pi D^2}{4}$ |
| $\Sigma_d$ | $+\rho v_d\frac{\pi d^2}{4}$ |
| $\Sigma_w$ | $0$ |

$$ \boxed{\,v_d = \left(\frac{D}{d}\right)^2v_u\,} \tag{1} $$

**2. Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_u$ | $-\rho v_u^2\frac{\pi D^2}{4}\bar{e}_x$ | $(p_u - p_a)\frac{\pi D^2}{4}\bar{e}_x$ | $0$ |
| $\Sigma_d$ | $+\rho v_d^2\frac{\pi d^2}{4}\bar{e}_x = \rho v_uv_d\frac{\pi D^2}{4}\bar{e}_x$ | $0$ (free jet) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed terms: $-\bar{F}$. The $\Sigma_d$ flux uses (1).

$$ \rho\frac{\pi D^2}{4}v_u(v_d - v_u)\,\bar{e}_x = (p_u - p_a)\frac{\pi D^2}{4}\bar{e}_x - \bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = \frac{\pi D^2}{4}\left\{p_u - p_a - \rho v_u^2\left[\left(\frac{D}{d}\right)^2 - 1\right]\right\}\bar{e}_x\,} \tag{2} $$

**3. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_u$ | $-\dot{m}\left(cT_u + \tfrac{v_u^2}{2}\right)$ | $+p_uv_u\frac{\pi D^2}{4}$ | $0$ | $0$ |
| $\Sigma_d$ | $+\dot{m}\left(cT_d + \tfrac{v_d^2}{2}\right)$ | $-p_av_d\frac{\pi d^2}{4}$ | $0$ | $0$ |
| $\Sigma_w$ | $0$ | $0$ | $0$ | $0$ (adiabatic) |

With $\dot{m} = \rho v_u\pi D^2/4 = \rho v_d\pi d^2/4$, dividing by $\dot{m}c$:

$$ \boxed{\,T_d - T_u = \frac{1}{c}\left[\left(\frac{p_u}{\rho} + \frac{v_u^2}{2}\right) - \left(\frac{p_a}{\rho} + \frac{v_d^2}{2}\right)\right]\,} \tag{3} $$

### 4. Inviscid limit (Bernoulli)

Without viscosity, Bernoulli (Notes Eq. 4.17) along a streamline from $u$ to $d$ gives $\frac{p_u}{\rho} + \frac{v_u^2}{2} = \frac{p_a}{\rho} + \frac{v_d^2}{2}$, i.e. $p_u - p_a = \tfrac{1}{2}\rho v_u^2\left[\left(\frac{D}{d}\right)^4 - 1\right]$. Substituting into (2), with $\left(\frac{D}{d}\right)^4 - 2\left(\frac{D}{d}\right)^2 + 1 = \left[\left(\frac{D}{d}\right)^2 - 1\right]^2$, and into (3):

$$ \boxed{\,\bar{F} = \frac{\pi D^2}{8}\,\rho v_u^2\left[\left(\frac{D}{d}\right)^2 - 1\right]^2\bar{e}_x,\qquad T_d - T_u = 0\,} \tag{4} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- (3): the temperature rise measures the loss of mechanical energy (total pressure) by viscous dissipation; without viscosity it is zero, (4).
- In the inviscid limit $\bar{F}$ points downstream and is always positive: the contraction is pulled along the flow. For $d \to D$, $\bar{F} \to 0$.
- Dimensions (SI): $[\rho v^2D^2] = \text{N}$; $[(p/\rho + v^2/2)/c] = \text{K}$.
- Numerical illustration (hypothetical data): water, $D = 0.1$ m, $d = 0.04$ m, $v_u = 1$ m/s, $p_u = 1.21\times10^5$ Pa, $p_a = 101325$ Pa: $v_d = 6.25$ m/s, $F = 113.29$ N and $T_d - T_u = 0.154$ mK (some loss); the inviscid value is $F = 108.24$ N (it needs $p_u - p_a = 19031$ Pa).
- Agreement with the official solution: CL20.pdf obtains (1) to (4).
