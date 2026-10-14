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

## Statement

The experimental tests of an airfoil in a wind tunnel indicate that the velocity profile upstream remains uniform, whereas behind the airfoil there exists a wake region with significant velocity deficit whose thickness increases downstream, resulting in the flow field sketched in the figure of CL1.pdf. For the airfoil tested, the velocity measurements at a given downstream section reveal that the velocity in the wake varies linearly from the value $u = U/2$ at the centerline to reach the value $u = U$ at the edge of the wake, located at $y = y_0$. To analyze the problem, consider a control volume limited laterally by the streamlines that extend from $x \to -\infty$, $y = \pm y_{-\infty}$ ($y_{-\infty} < y_0$) to $x = x_0$, $y = \pm y_0$ and internally by the surface of the airfoil. Assuming that the air behaves as an incompressible fluid with density $\rho$ and that viscous stresses are negligible both in the wake and along the bounding streamlines, obtain the value of $y_{-\infty}$ as a function of $y_0$, as well as the value of the drag on the airfoil as a function of $\rho$, $y_0$ and $U$. In the analysis, assume that on the outer boundary of the control volume the pressure differences from the ambient value $p_\infty$ are negligible, and so is the effect of gravity on the air flow.

Source: CL1.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36, force of the fluid on a body Eq. 3.32.

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Steady flow ($\partial/\partial t = 0$), planar (everything is computed per unit span in the direction $z$ normal to the figure), incompressible (constant $\rho$), no gravity.
- Viscous stresses are negligible in the wake and on the bounding streamlines (given); pressure differences $p - p_\infty$ are negligible on the whole outer boundary of the control volume (given). Pressure and viscous stresses on the airfoil surface are **not** neglected: they are the drag.
- Wake profile at the section $x = x_0$, symmetric about $y = 0$: $v_x = \tfrac{U}{2}\left(1 + \tfrac{|y|}{y_0}\right)$ for $|y| \le y_0$ and $v_x = U$ for $|y| > y_0$. The only unknowns are the scalar $y_{-\infty}$ and the drag $D$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | uniform upstream velocity | m/s |
| $y_0$ | half-width of the wake at $x = x_0$ | m |
| $y_{-\infty}$ | half-width of the stream tube far upstream | m |
| $\rho$ | air density | kg/m$^3$ |
| $D$ | drag per unit span | N/m |

Dimensional check of the unknown: $[\rho U^2 y_0] = (\text{kg/m}^3)(\text{m}^2/\text{s}^2)\,\text{m} = \text{kg/s}^2 = \text{N/m}$, a force per unit length, as required for a planar problem.

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame fixed to the airfoil and the wind tunnel, Cartesian basis $(\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z)$ with $\mathbf{e}_x$ along the incoming stream and $\mathbf{e}_z = \mathbf{e}_x \wedge \mathbf{e}_y$. The control volume is fixed in this frame, so $\mathbf{v}_c = 0$ in the universal balances (Eqs. 3.10, 3.35 reduce to Eqs. 3.11, 3.36).
- Boundary of the control volume: $\Sigma_u$ (section far upstream, $|y| < y_{-\infty}$, $\mathbf{n} = -\mathbf{e}_x$), $\Sigma_d$ (section $x = x_0$, $|y| < y_0$, $\mathbf{n} = +\mathbf{e}_x$), $\Sigma_l$ (the two bounding streamlines), and $\Sigma_w$ (airfoil surface, with $\mathbf{n}$ pointing out of the fluid, i.e. into the airfoil).
- The force of the fluid on the airfoil is $\mathbf{F} = \int_{\Sigma_w}(-p\,\mathbf{n}_w + \bar{\bar{\tau}}'\cdot\mathbf{n}_w)\,d\sigma$ with $\mathbf{n}_w = -\mathbf{n}$ pointing out of the airfoil (Eq. 3.32). The force of the airfoil on the fluid is therefore $-\mathbf{F}$.
- Change of variable used in the integral of the wake: $s = 1 + y/y_0$, $ds = dy/y_0$, so that $y \in [0, y_0]$ maps to $s \in [1, 2]$.

## Phase 3: Step-by-Step Derivation

### 3.1 Mass balance: the width $y_{-\infty}$ of the incoming stream tube

Why this tool: the control volume is fixed and the flow is steady, so the integral continuity equation (Notes Eq. 3.11) reduces to $\int_{\Sigma_c}\rho\,\mathbf{v}\cdot\mathbf{n}\,d\sigma = 0$. It is the only relation that links the unknown $y_{-\infty}$ to the measured profile.

On $\Sigma_l$ (streamlines) and on $\Sigma_w$ (impermeable wall) $\mathbf{v}\cdot\mathbf{n} = 0$, so only $\Sigma_u$ and $\Sigma_d$ contribute. On $\Sigma_u$, $\mathbf{v}\cdot\mathbf{n} = -U$ over a width $2y_{-\infty}$:

$$ \int_{\Sigma_u}\rho\,\mathbf{v}\cdot\mathbf{n}\,d\sigma = -\rho U\,(2y_{-\infty}). $$

On $\Sigma_d$, $\mathbf{v}\cdot\mathbf{n} = v_x$ and, by symmetry, the integral is twice the integral over $0 \le y \le y_0$. The antiderivative of $1 + y/y_0$ is $y + y^2/(2y_0)$, and Barrow's rule between $y = 0$ and $y = y_0$ gives:

$$ \int_{\Sigma_d}\rho\,\mathbf{v}\cdot\mathbf{n}\,d\sigma = 2\rho\int_0^{y_0}\frac{U}{2}\left(1 + \frac{y}{y_0}\right)dy = \rho U\left[y + \frac{y^2}{2y_0}\right]_{0}^{y_0} = \rho U\left(y_0 + \frac{y_0}{2}\right) = \frac{3}{2}\rho U y_0. $$

Adding both contributions and setting the sum to zero:

$$ -2\rho U y_{-\infty} + \frac{3}{2}\rho U y_0 = 0 \;\Longrightarrow\; \boxed{\,y_{-\infty} = \frac{3}{4}\,y_0.\,} $$

### 3.2 Linear momentum balance: the drag

Why this tool: the force of the fluid on a body is not accessible from the (unknown) pressure and shear on its surface, but it appears in the integral momentum balance (Notes Eq. 3.36, steady, fixed control volume, no gravity) as the only unknown surface term:

$$ \int_{\Sigma_c}\rho\,\mathbf{v}\,(\mathbf{v}\cdot\mathbf{n})\,d\sigma = \int_{\Sigma_c}\left(-p\,\mathbf{n} + \bar{\bar{\tau}}'\cdot\mathbf{n}\right)d\sigma. $$

Because $\Sigma_c$ is a closed surface, $\int_{\Sigma_c}p_\infty\mathbf{n}\,d\sigma = 0$, and $p$ may be replaced by $p - p_\infty$ on the right-hand side. On $\Sigma_u$, $\Sigma_d$ and $\Sigma_l$ the difference $p - p_\infty$ and the viscous stresses are negligible (hypothesis), so the only surviving term is the one on $\Sigma_w$, which equals the force of the airfoil on the fluid, $-\mathbf{F}$. The $x$ component gives the drag $D = F_x$:

$$ D = -\int_{\Sigma_u + \Sigma_d + \Sigma_l}\rho\,v_x\,(\mathbf{v}\cdot\mathbf{n})\,d\sigma. $$

On $\Sigma_l$, $\mathbf{v}\cdot\mathbf{n} = 0$. On $\Sigma_u$, $v_x = U$ and $\mathbf{v}\cdot\mathbf{n} = -U$, hence with 3.1:

$$ \int_{\Sigma_u}\rho\,v_x(\mathbf{v}\cdot\mathbf{n})\,d\sigma = -\rho U^2\,(2y_{-\infty}) = -\frac{3}{2}\rho U^2 y_0. $$

On $\Sigma_d$, with the substitution $s = 1 + y/y_0$, $dy = y_0\,ds$, and Barrow's rule between $s = 1$ and $s = 2$:

$$ \int_{\Sigma_d}\rho\,v_x^2\,d\sigma = 2\rho\,\frac{U^2}{4}\int_0^{y_0}\left(1 + \frac{y}{y_0}\right)^2dy = \frac{\rho U^2}{2}\,y_0\int_1^2 s^2\,ds = \frac{\rho U^2 y_0}{2}\left[\frac{s^3}{3}\right]_1^2 = \frac{\rho U^2 y_0}{2}\cdot\frac{8 - 1}{3} = \frac{7}{6}\rho U^2 y_0. $$

Therefore:

$$ D = -\left(-\frac{3}{2} + \frac{7}{6}\right)\rho U^2 y_0 = -\left(-\frac{9}{6} + \frac{7}{6}\right)\rho U^2 y_0 \;\Longrightarrow\; \boxed{\,D = \frac{1}{3}\,\rho\,U^2\,y_0\,}\quad\text{per unit span, in the direction } +\mathbf{e}_x. $$

For a wake symmetric about $y = 0$ (a symmetric airfoil at zero angle of attack, which the statement implies by giving a symmetric profile) the $y$ component of the same balance gives $F_y = 0$: there is no lift.

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: the wake carries less mass flux ($\tfrac{3}{2}\rho U y_0$) than the undisturbed stream would through the same width ($2\rho U y_0$); the missing flux is the volume displaced sideways by the wake, which is why the bounding streamlines are at $y_{-\infty} = \tfrac{3}{4}y_0 < y_0$ far upstream. The momentum deficit left in the wake is the drag.
- Limit $y_0 \to 0$: no wake, $y_{-\infty} \to 0$ and $D \to 0$, consistent with d'Alembert's paradox for a frictionless attached flow.
- Dimensions (SI): $[y_{-\infty}] = [y_0] = \text{m}$; $[D] = [\rho U^2 y_0] = \text{N/m}$.
- Numerical cross-check (midpoint quadrature with $2\times10^5$ cells of the defining integrals, $U = 1$ m/s, $\rho = 1.2$ kg/m$^3$, $y_0 = 0.35$ m): $y_{-\infty}/y_0 = 0.75000$ and $D = 0.140000$ N/m, equal to $\rho U^2 y_0/3 = 0.14$ N/m.
- Agreement with the official solution: CL1.pdf obtains $y_{-\infty} = \tfrac{3}{4}y_0$ and $\mathbf{F}_{\text{airfoil}} = \tfrac{1}{3}\rho U^2 y_0\,\mathbf{e}_x$, the same results.

> [!info] Extension (beyond the official solution)
> With the momentum thickness $\theta = \int_{-y_0}^{y_0}\frac{v_x}{U}\left(1 - \frac{v_x}{U}\right)dy = 2y_0\int_0^1\frac{1 - \sigma^2}{4}\,d\sigma = \frac{y_0}{3}$ (substituting $\sigma = y/y_0$), the result reads $D = \rho U^2\theta$: the classical momentum-deficit formula for the drag from a wake survey.
