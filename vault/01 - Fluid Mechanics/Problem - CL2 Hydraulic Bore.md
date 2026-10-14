---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - resalto
  - bore
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL2.pdf"
---

# Problem CL2: Bore over a Stagnant Water Layer

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].

## Statement

The bore sketched in the figure of CL2.pdf moves under the action of gravity with constant velocity $U$ over an initially stagnant water layer of thickness $h_0$, leaving behind a layer of thickness $h_1$ moving with velocity $U_1$. Assuming that in the air both viscous stresses and pressure variations with respect to the ambient value $p_a$ are negligible, and so are viscous stresses on the bottom wall, find the values of $U_1$ and $h_1$ as a function of $U$, $h_0$ and $g$. As a preliminary computation, obtain the pressure distributions both upstream and downstream from the bore, verifying that they can be expressed in the form $p = p_a + \rho g(h_0 - z)$ and $p = p_a + \rho g(h_1 - z)$, respectively, where $z$ represents the vertical distance to the bottom wall.

Source: CL2.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36.

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar flow (quantities per unit width normal to the figure) of an incompressible liquid of density $\rho$, under gravity $\mathbf{g} = -g\,\mathbf{e}_z$. The bore advances towards $-\mathbf{e}_x$ (the $x$ axis points to the right in the figure) with constant velocity $U$ over the stagnant layer of thickness $h_0$; behind it the layer has thickness $h_1$ and uniform velocity $-U_1\mathbf{e}_x$.
- Far from the front, in each region, the velocity is horizontal and uniform and the free surface is horizontal at pressure $p_a$. Viscous stresses are negligible (given); the ratio of viscous to inertial forces is of order $\mu/(\rho U h) \ll 1$ for a water layer.
- The two unknowns are $h_1/h_0$ and $U_1/U$; the data are $U$, $h_0$, $g$ and $\rho$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | velocity of the bore (relative to the stagnant layer) | m/s |
| $U_1$ | velocity of the water behind the bore | m/s |
| $h_0$, $h_1$ | layer thickness ahead of and behind the bore | m |
| $p_a$ | ambient pressure acting on the free surface | Pa |
| $g$ | gravitational acceleration | m/s$^2$ |
| $F = U^2/(g h_0)$ | Froude number of the bore (dimensionless) | 1 |

Dimensional check: $[U^2/(g h_0)] = (\text{m}^2/\text{s}^2)/\big((\text{m}/\text{s}^2)\,\text{m}\big) = 1$.

## Phase 2: Coordinates, Frames and Changes of Variable

- Laboratory frame $L$: Cartesian basis $(\mathbf{e}_x, \mathbf{e}_z)$ with $z$ measured from the bottom wall. The flow is unsteady in $L$ because the front moves.
- Frame of the bore $B$: it moves with the velocity $-U\,\mathbf{e}_x$ relative to $L$. Since this velocity is constant, $B$ is inertial and no inertial forces appear in the balances. Velocities in $B$ are $\mathbf{v}_B = \mathbf{v}_L + U\,\mathbf{e}_x$: the liquid ahead has $\mathbf{v}_B = U\,\mathbf{e}_x$ and the liquid behind has $\mathbf{v}_B = (U - U_1)\,\mathbf{e}_x$. In $B$ the front is stationary, so the flow is steady.
- Control volume fixed in $B$ (so $\mathbf{v}_c = 0$; Eqs. 3.11 and 3.36): $\Sigma_0$ (vertical section ahead of the front, $\mathbf{n} = -\mathbf{e}_x$, area $h_0$ per unit width), $\Sigma_1$ (vertical section behind, $\mathbf{n} = +\mathbf{e}_x$, area $h_1$), $\Sigma_b$ (bottom wall, $\mathbf{n} = -\mathbf{e}_z$) and $\Sigma_s$ (free surface, material and steady in $B$). On $\Sigma_b$ and $\Sigma_s$, $\mathbf{v}\cdot\mathbf{n} = 0$.

## Phase 3: Step-by-Step Derivation

### 3.1 Preliminary result: hydrostatic pressure upstream and downstream

Why this tool: in the uniform regions the velocity is horizontal, so the $z$ component of the integral momentum balance (Notes Eq. 3.36) has no momentum flux and reduces to a force balance. Take a fixed control volume formed by the liquid column of width $\Delta x$ (per unit width) between a height $z$ and the free surface $z = h_0$ (upstream region). Its faces are: the bottom face at height $z$ ($\mathbf{n} = -\mathbf{e}_z$), the free surface ($\mathbf{n} = +\mathbf{e}_z$, $p = p_a$) and two vertical faces ($\mathbf{n} = \mp\mathbf{e}_x$).

The $z$ component of $\rho\,\mathbf{v}\,(\mathbf{v}\cdot\mathbf{n})$ vanishes on every face because $v_z = 0$. The pressure force has $z$ component $+p(z)\Delta x$ on the bottom face and $-p_a\Delta x$ on the free surface; the pressure on the vertical faces points along $\pm\mathbf{e}_x$ and viscous stresses are negligible. The weight of the column is $-\rho g\,(h_0 - z)\,\Delta x$. Hence

$$ 0 = p(z)\,\Delta x - p_a\,\Delta x - \rho g\,(h_0 - z)\,\Delta x \;\Longrightarrow\; \boxed{\,p = p_a + \rho g\,(h_0 - z)\,}\quad\text{(upstream)}. $$

The same argument with the surface at $z = h_1$ gives $p = p_a + \rho g\,(h_1 - z)$ downstream.

### 3.2 Mass balance in the frame of the bore

Why this tool: steady flow and fixed control volume in $B$, so $\int_{\Sigma_c}\rho\,\mathbf{v}\cdot\mathbf{n}\,d\sigma = 0$ (Notes Eq. 3.11). Only $\Sigma_0$ and $\Sigma_1$ are crossed by the flow:

$$ -\rho\,U\,h_0 + \rho\,(U - U_1)\,h_1 = 0 \;\Longrightarrow\; U\,h_0 = (U - U_1)\,h_1. \tag{c1} $$

### 3.3 Momentum balance in the frame of the bore

Why this tool: the unknown $h_1$ appears through the pressure forces, which only the momentum balance (Notes Eq. 3.36) contains. Since $\int_{\Sigma_c}p_a\,\mathbf{n}\,d\sigma = 0$, replace $p$ by $p - p_a$. The $x$ component of the left-hand side is

$$ \int_{\Sigma_c}\rho\,v_x\,(\mathbf{v}\cdot\mathbf{n})\,d\sigma = \rho U\,(-U h_0) + \rho\,(U - U_1)\,(U - U_1)\,h_1 = -\rho U^2 h_0 + \rho\,(U - U_1)^2\,h_1. $$

Right-hand side: on $\Sigma_s$, $p - p_a = 0$; on $\Sigma_b$ the normal is $-\mathbf{e}_z$, with no $x$ component; the viscous stresses are negligible (hypothesis); gravity has no $x$ component. The pressure on $\Sigma_0$ and $\Sigma_1$ is the hydrostatic distribution of 3.1, with $\mathbf{n} = -\mathbf{e}_x$ and $+\mathbf{e}_x$ respectively. The antiderivative of $\rho g\,(h - z)$ is $\rho g\,(hz - z^2/2)$ and Barrow's rule between $z = 0$ and $z = h$ gives $\rho g\,(h^2 - h^2/2) = \rho g h^2/2$:

$$ -\int_{\Sigma_0}(p - p_a)\,\mathbf{n}\,d\sigma \cdot \mathbf{e}_x = +\int_0^{h_0}\rho g\,(h_0 - z)\,dz = \frac{\rho g h_0^2}{2}, \qquad -\int_{\Sigma_1}(p - p_a)\,\mathbf{n}\,d\sigma \cdot \mathbf{e}_x = -\int_0^{h_1}\rho g\,(h_1 - z)\,dz = -\frac{\rho g h_1^2}{2}. $$

$$ -\rho U^2 h_0 + \rho\,(U - U_1)^2\,h_1 = \frac{\rho g}{2}\left(h_0^2 - h_1^2\right). \tag{c2} $$

### 3.4 Solution for $h_1/h_0$ and $U_1/U$

From (c1), $U - U_1 = U h_0/h_1$, so $(U - U_1)^2\,h_1 = U^2 h_0^2/h_1$. Substituting into (c2) and dividing by $\rho$:

$$ U^2 h_0\left(\frac{h_0}{h_1} - 1\right) = \frac{g}{2}\,(h_0 - h_1)(h_0 + h_1) \;\Longrightarrow\; U^2 h_0\,\frac{h_0 - h_1}{h_1} = \frac{g}{2}\,(h_0 - h_1)(h_0 + h_1). $$

For a genuine bore $h_1 \ne h_0$ (the case $h_1 = h_0$ is the undisturbed layer), so the factor $h_0 - h_1$ can be cancelled. With $r \equiv h_1/h_0$ and $F = U^2/(g h_0)$, dividing by $g h_0^2$ gives $F/r = (1 + r)/2$, that is

$$ r^2 + r - 2F = 0 \;\Longrightarrow\; \boxed{\,\frac{h_1}{h_0} = \frac{1}{2}\left(\sqrt{1 + 8F} - 1\right)\,}\qquad (\text{the negative root is rejected since } h_1 > 0). $$

The velocity behind follows from (c1): $U_1/U = 1 - h_0/h_1 = 1 - 1/r = (r - 1)/r$. With $s \equiv \sqrt{1 + 8F}$, $r = (s - 1)/2$ and

$$ \boxed{\,\frac{U_1}{U} = 1 - \frac{2}{s - 1} = \frac{\sqrt{1 + 8F} - 3}{\sqrt{1 + 8F} - 1}\,},\qquad F = \frac{U^2}{g h_0}. $$

> [!warning] Erratum in the official solution (reading of the handwriting)
> CL2.pdf gives $h_1/h_0 = \tfrac{1}{2}(\sqrt{1+8F} - 1)$, which agrees with the result above. For the velocity it gives, as legible in the scan, $U_1/U = \tfrac{3}{2}\left(\tfrac{1}{3}\sqrt{1+8F} - 1\right) = (\sqrt{1+8F} - 3)/2 = r - 1$. This contradicts the official continuity equation $U h_0 = (U - U_1)h_1$, which requires $U_1/U = (r-1)/r$; the two expressions coincide only for $r = 1$. The check that proves it: $(U - U_1)h_1 = U h_0 > 0$ forces $U_1 < U$, whereas $r - 1 > 1$ for $F > 3$ (for $F = 4$, $r - 1 = 1.3723$ against the correct $U_1/U = 0.5785$, and the mass residual of (c1) with the scan formula is $U h_0 - (U - U_1)h_1 \ne 0$). The computed value is kept.

## Phase 4: Interpretation, Limits and Dimensional Check

- The bore exists only for $F > 1$: $r > 1 \iff s > 3 \iff F > 1$. $F$ is the Froude number of the front relative to the shallow-water wave speed $\sqrt{g h_0}$; a front slower than $\sqrt{g h_0}$ cannot raise the level.
- Weak bore, $F = 1 + \epsilon$: $r \approx 1 + \tfrac{2}{3}\epsilon$ and $U_1/U \approx \tfrac{2}{3}\epsilon \to 0$; the front degenerates into an infinitesimal gravity wave travelling at $\sqrt{g h_0}$.
- Strong bore, $F \gg 1$: $r \approx \sqrt{2F}$, so $h_1 \approx h_0\sqrt{2}\,U/\sqrt{g h_0}$ and $U_1 \to U$: the liquid behind moves almost with the bore.
- Dimensions (SI): both sides of (c2) are forces per unit width, $[\rho U^2 h_0] = [\rho g h^2] = \text{N/m}$; $F$, $r$ and $U_1/U$ are dimensionless.
- Numerical cross-check: $F = 4$, $h_0 = 0.5$ m, $g = 9.81$ m/s$^2$ give $U = 4.4294$ m/s, $h_1/h_0 = 2.3723$ ($h_1 = 1.1861$ m), $U_1/U = 0.57846$ ($U_1 = 2.5623$ m/s); the residuals of (c1) and (c2) are below $10^{-14}$ in SI units.

> [!info] Extension (beyond the official solution)
> Mechanical energy is not conserved across the bore: Bernoulli's equation between both sections would give a different relation. The head lost is the classical hydraulic-jump value $\Delta H = (h_1 - h_0)^3/(4h_0h_1)$, always positive for $h_1 > h_0$.
