---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - estela
  - resistencia
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL1.pdf"
---

# Problem CL1: Airfoil Wake: Streamline Displacement and Drag

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The experimental tests of an airfoil in a wind tunnel indicate that the velocity profile upstream remains uniform, whereas behind the airfoil there exists a wake region with significant velocity deficit whose thickness increases downstream, resulting in the flow field sketched in the figure of CL1.pdf. For the airfoil tested, the velocity measurements at a given downstream section reveal that the velocity in the wake varies linearly from the value $u = U/2$ at the centerline to reach the value $u = U$ at the edge of the wake, located at $y = y_0$. To analyze the problem, consider a control volume limited laterally by the streamlines that extend from $x \to -\infty$, $y = \pm y_{-\infty}$ ($y_{-\infty} < y_0$) to $x = x_0$, $y = \pm y_0$ and internally by the surface of the airfoil. Assuming that the air behaves as an incompressible fluid with density $\rho$ and that viscous stresses are negligible both in the wake and along the bounding streamlines, obtain the value of $y_{-\infty}$ as a function of $y_0$, as well as the value of the drag on the airfoil as a function of $\rho$, $y_0$ and $U$. In the analysis, assume that on the outer boundary of the control volume the pressure differences from the ambient value $p_\infty$ are negligible, and so is the effect of gravity on the air flow.

Source: CL1.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36, force of the fluid on a body Eq. 3.32.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, planar (everything per unit span), incompressible ($\rho$ constant); neglect $\bar{g}$.
- Viscous stresses negligible in the wake and on the bounding streamlines; $p - p_\infty \simeq 0$ on the whole outer boundary of the control volume (given). On the airfoil surface pressure and viscous stresses are **not** neglected: they make the drag.
- Wake profile at $x = x_0$ (symmetric about $y = 0$): $v_x = \tfrac{U}{2}\left(1 + \tfrac{|y|}{y_0}\right)$ for $|y| \le y_0$, and $v_x = U$ outside.
- Data: $[\rho,\ U,\ y_0]$. Unknowns: $[y_{-\infty},\ D]$, with $D$ the drag per unit span.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | uniform upstream velocity | m/s |
| $y_0$ | half-width of the wake at $x = x_0$ | m |
| $y_{-\infty}$ | half-width of the stream tube far upstream | m |
| $\rho$ | air density | kg/m$^3$ |
| $D$ | drag per unit span | N/m |

Dimensional check of the unknown: $[\rho U^2 y_0] = (\text{kg/m}^3)(\text{m}^2/\text{s}^2)\,\text{m} = \text{N/m}$, a force per unit length, as required for a planar problem.

## Phase 2: Frames, Control Volume and Surfaces

- Inertial frame fixed to the airfoil and the tunnel; basis $(\bar{e}_x, \bar{e}_y, \bar{e}_z)$ with $\bar{e}_x$ along the stream. The control volume is fixed: $\bar{v}_c = 0$.
- Surfaces of $\Sigma_c$ (outward normal $\bar{n}$): $\Sigma_1$, far upstream, $|y| < y_{-\infty}$, $\bar{n} = -\bar{e}_x$; $\Sigma_2$, the section $x = x_0$, $|y| < y_0$, $\bar{n} = +\bar{e}_x$; $\Sigma_l$, the two bounding streamlines ($\bar{v}\cdot\bar{n} = 0$); $\Sigma_w$, the airfoil surface ($\bar{n}$ pointing into the airfoil).
- Change of variable for the wake integrals: $s = 1 + y/y_0$, $dy = y_0\,ds$; $y \in [0, y_0]$ maps to $s \in [1, 2]$.

Force of the air on the airfoil (Notes Eq. 3.32), written on the wetted surface with the normal $\bar{n}$ of the control volume:

$$ \boxed{\,\bar{F} = \int_{\Sigma_w}(p - p_\infty)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,} $$

Hence the $\Sigma_w$ terms of the momentum balance add up to $-\bar{F}$.

## Phase 3: Balances, Surface by Surface

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_1$ | $\rho\,U\,(-1)\,2y_{-\infty} = -2\rho U y_{-\infty}$ |
| $\Sigma_2$ | $2\rho\int_0^{y_0}\tfrac{U}{2}\left(1 + \tfrac{y}{y_0}\right)dy = \tfrac{3}{2}\rho U y_0$ |
| $\Sigma_l$ | $0$ (streamlines, $\bar{v}\cdot\bar{n} = 0$) |
| $\Sigma_w$ | $0$ (impermeable wall) |

$$ -2\rho U y_{-\infty} + \frac{3}{2}\rho U y_0 = 0 \;\Longrightarrow\; \boxed{\,y_{-\infty} = \frac{3}{4}\,y_0\,} \tag{1} $$

The $\Sigma_2$ entry in detail: the antiderivative of $1 + y/y_0$ is $y + y^2/(2y_0)$, and by Barrow's rule between $y = 0$ and $y = y_0$, $\rho U\left[y + \frac{y^2}{2y_0}\right]_0^{y_0} = \rho U\left(y_0 + \frac{y_0}{2}\right) = \frac{3}{2}\rho U y_0$ (the factor 2 of the table counts both halves of the wake).

**Linear momentum (Notes Eq. 3.36, with $p_a = p_\infty$)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_\infty)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_\infty)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_1$ | $\rho U\,(-U)\,2y_{-\infty}\,\bar{e}_x = -2\rho U^2y_{-\infty}\,\bar{e}_x$ | $0$ ($p \simeq p_\infty$) | $0$ (uniform flow) |
| $\Sigma_2$ | $2\rho\int_0^{y_0}v_x^2\,dy\;\bar{e}_x = \tfrac{7}{6}\rho U^2 y_0\,\bar{e}_x$ | $0$ ($p \simeq p_\infty$) | $0$ (given) |
| $\Sigma_l$ | $0$ ($\bar{v}\cdot\bar{n} = 0$) | $0$ ($p \simeq p_\infty$) | $0$ (given) |
| **$\Sigma_w$** (boxed) | $0$ (impermeable) | $-\int_{\Sigma_w}(p - p_\infty)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: the force of the airfoil on the air, $-\bar{F}$. The $\Sigma_1$ entry uses (1): $-2\rho U^2y_{-\infty} = -\tfrac{3}{2}\rho U^2 y_0$.

$$ -\frac{3}{2}\rho U^2y_0\,\bar{e}_x + \frac{7}{6}\rho U^2y_0\,\bar{e}_x = -\bar{F} \;\Longrightarrow\; \boxed{\,\bar{F} = D\,\bar{e}_x,\qquad D = \frac{1}{3}\,\rho\,U^2\,y_0\,} \tag{2} $$

The $\Sigma_2$ momentum entry in detail, with $s = 1 + y/y_0$, $dy = y_0\,ds$ and Barrow's rule between $s = 1$ and $s = 2$: $2\rho\frac{U^2}{4}\int_0^{y_0}\left(1 + \frac{y}{y_0}\right)^2dy = \frac{\rho U^2y_0}{2}\int_1^2 s^2\,ds = \frac{\rho U^2y_0}{2}\left[\frac{s^3}{3}\right]_1^2 = \frac{\rho U^2y_0}{2}\cdot\frac{8 - 1}{3} = \frac{7}{6}\rho U^2y_0$. The sum of the flux column is $\left(-\frac{9}{6} + \frac{7}{6}\right)\rho U^2y_0 = -\frac{1}{3}\rho U^2 y_0$.

For a wake symmetric about $y = 0$ (a symmetric airfoil at zero incidence, as the symmetric profile implies) the $y$ component of the momentum flux through $\Sigma_2$ cancels between the two halves, so $F_y = 0$: no lift.

## Phase 4: Interpretation, Limits and Dimensional Check

- The wake carries less mass flux ($\tfrac{3}{2}\rho U y_0$) than the undisturbed stream through the same width ($2\rho U y_0$): the bounding streamlines are pushed outwards, from $y_{-\infty} = \tfrac{3}{4}y_0$ to $y_0$. The momentum deficit left in the wake is the drag.
- Limit $y_0 \to 0$: no wake, $y_{-\infty} \to 0$ and $D \to 0$ (d'Alembert's paradox for a frictionless attached flow).
- Dimensions (SI): $[y_{-\infty}] = \text{m}$; $[D] = [\rho U^2 y_0] = \text{N/m}$.
- Numerical cross-check (midpoint quadrature of the defining integrals with $2\times10^5$ cells, $U = 1$ m/s, $\rho = 1.2$ kg/m$^3$, $y_0 = 0.35$ m): $y_{-\infty}/y_0 = 0.75000$ and $D = 0.140000$ N/m $= \rho U^2y_0/3$.
- Agreement with the official solution: CL1.pdf obtains $y_{-\infty} = \tfrac{3}{4}y_0$ and $\bar{F}_{\text{airfoil}} = \tfrac{1}{3}\rho U^2 y_0\,\bar{e}_x$.

> [!info] Extension (beyond the official solution)
> With the momentum thickness $\theta = \int_{-y_0}^{y_0}\frac{v_x}{U}\left(1 - \frac{v_x}{U}\right)dy = 2y_0\int_0^1\frac{1 - \sigma^2}{4}\,d\sigma = \frac{y_0}{3}$ ($\sigma = y/y_0$), the result reads $D = \rho U^2\theta$, the classical momentum-deficit formula for the drag from a wake survey.
