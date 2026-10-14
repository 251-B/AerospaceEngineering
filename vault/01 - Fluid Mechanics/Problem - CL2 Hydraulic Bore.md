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
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

The bore sketched in the figure of CL2.pdf moves under the action of gravity with constant velocity $U$ over an initially stagnant water layer of thickness $h_0$, leaving behind a layer of thickness $h_1$ moving with velocity $U_1$. Assuming that in the air both viscous stresses and pressure variations with respect to the ambient value $p_a$ are negligible, and so are viscous stresses on the bottom wall, find the values of $U_1$ and $h_1$ as a function of $U$, $h_0$ and $g$. As a preliminary computation, obtain the pressure distributions both upstream and downstream from the bore, verifying that they can be expressed in the form $p = p_a + \rho g(h_0 - z)$ and $p = p_a + \rho g(h_1 - z)$, respectively, where $z$ represents the vertical distance to the bottom wall.

Source: CL2.pdf (page 1). Notes.pdf, Chapter 3: integral mass balance Eqs. 3.10-3.11, integral momentum balance Eqs. 3.35-3.36.

## Phase 1: Hypotheses, Data and Unknowns

- Planar flow (per unit width) of an incompressible liquid of density $\rho$, with gravity $\bar{g} = -g\,\bar{e}_z$ (here gravity is **not** neglected: it drives the bore).
- The bore advances towards $-\bar{e}_x$ with constant velocity $U$ over the stagnant layer $h_0$; behind it the layer $h_1$ moves with $-U_1\bar{e}_x$. Far from the front the velocity is uniform and horizontal and the free surface is flat at $p = p_a$.
- Viscous stresses negligible in the water sections and on the bottom wall (given); $\mu/(\rho U h) \ll 1$.
- Data: $[U,\ h_0,\ g,\ \rho]$. Unknowns: $[h_1,\ U_1]$ and the pressure distributions.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | velocity of the bore | m/s |
| $U_1$ | velocity of the water behind the bore | m/s |
| $h_0$, $h_1$ | layer thickness ahead of and behind the bore | m |
| $F = U^2/(gh_0)$ | Froude number of the bore | 1 |

## Phase 2: Frames, Control Volume and Surfaces

- Laboratory frame $L$, with $z$ measured from the bottom: unsteady flow, because the front moves.
- Frame of the bore $B$, moving with $-U\bar{e}_x$ relative to $L$. It is inertial (constant velocity), so the balances keep their form, and the flow is steady in it. Velocities: $\bar{v}_B = \bar{v}_L + U\bar{e}_x$, so the water ahead has $U\bar{e}_x$ and the water behind $(U - U_1)\bar{e}_x$.
- Control volume fixed in $B$ ($\bar{v}_c = 0$). Surfaces: $\Sigma_0$, vertical section ahead ($\bar{n} = -\bar{e}_x$, height $h_0$); $\Sigma_1$, vertical section behind ($\bar{n} = +\bar{e}_x$, height $h_1$); $\Sigma_b$, bottom wall ($\bar{n} = -\bar{e}_z$); $\Sigma_s$, free surface (steady material surface in $B$, $p = p_a$).

## Phase 3: Balances, Surface by Surface

### 3.1 Preliminary: hydrostatic pressure in the uniform regions

Control volume: a column of width $\Delta x$ in the uniform region ahead, from height $z$ up to the free surface $z = h_0$. Surfaces: $\Sigma_{\text{bot}}$ (at height $z$, $\bar{n} = -\bar{e}_z$), $\Sigma_{\text{top}}$ (free surface, $\bar{n} = +\bar{e}_z$) and two vertical faces $\Sigma_{\text{side}}$ ($\bar{n} = \mp\bar{e}_x$). Only the $z$ component is needed.

**Momentum, z component, on the column (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho v_z\,dV}}_{0} + \int_{\Sigma_c}\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}p\,n_z\,d\sigma + \underbrace{\cancel{\int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma}}_{\text{negligible}} - \int_{V_c}\rho g\,dV $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho v_z\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,n_z\,d\sigma$ |
| :--- | :--- | :--- |
| $\Sigma_{\text{bot}}$ | $0$ ($v_z = 0$) | $+p(z)\,\Delta x$ |
| $\Sigma_{\text{top}}$ | $0$ ($v_z = 0$) | $-p_a\,\Delta x$ |
| $\Sigma_{\text{side}}$ | $0$ ($v_z = 0$) | $0$ ($n_z = 0$) |

Volume term: $-\int_{V_c}\rho g\,dV = -\rho g\,(h_0 - z)\,\Delta x$ (weight of the column).

$$ 0 = p(z)\,\Delta x - p_a\,\Delta x - \rho g\,(h_0 - z)\,\Delta x \;\Longrightarrow\; \boxed{\,p = p_a + \rho g\,(h_0 - z)\,} \tag{1} $$

The same column taken behind the bore gives $p = p_a + \rho g\,(h_1 - z)$ (1').

### 3.2 Mass and momentum in the frame of the bore

**Mass (Notes Eq. 3.11), frame B**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_0$ | $\rho\,U\,(-1)\,h_0 = -\rho U h_0$ |
| $\Sigma_1$ | $\rho\,(U - U_1)\,h_1$ |
| $\Sigma_b$ | $0$ (wall) |
| $\Sigma_s$ | $0$ (material surface) |

$$ \boxed{\,U\,h_0 = (U - U_1)\,h_1\,} \tag{2} $$

In the momentum balance $p$ may be replaced by $p - p_a$ because $\int_{\Sigma_c}p_a\bar{n}\,d\sigma = 0$ on a closed surface. The $x$ component is taken (gravity has no $x$ component). On $\Sigma_0$ and $\Sigma_1$ the pressure is (1) and (1'); the antiderivative of $\rho g(h - z)$ is $\rho g(hz - z^2/2)$, and Barrow's rule between $z = 0$ and $z = h$ gives $\rho g h^2/2$.

**Momentum, x component (Notes Eq. 3.36), frame B**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho v_x\,dV}}_{0\ (\text{steady in } B)} + \int_{\Sigma_c}\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,n_x\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho g_x\,dV}}_{g_x = 0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho v_x\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,n_x\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_x\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_0$ | $\rho U\,(-U)\,h_0 = -\rho U^2h_0$ | $+\int_0^{h_0}\rho g(h_0 - z)\,dz = \frac{\rho g h_0^2}{2}$ | $0$ |
| $\Sigma_1$ | $\rho\,(U - U_1)^2\,h_1$ | $-\int_0^{h_1}\rho g(h_1 - z)\,dz = -\frac{\rho g h_1^2}{2}$ | $0$ |
| $\Sigma_b$ | $0$ | $0$ ($n_x = 0$) | $0$ (given) |
| $\Sigma_s$ | $0$ | $0$ ($p = p_a$) | $0$ (air) |

$$ \boxed{\,-\rho U^2 h_0 + \rho\,(U - U_1)^2\,h_1 = \frac{\rho g}{2}\left(h_0^2 - h_1^2\right)\,} \tag{3} $$

### 3.3 Solution for $h_1/h_0$ and $U_1/U$

From (2), $U - U_1 = Uh_0/h_1$, so $(U - U_1)^2h_1 = U^2h_0^2/h_1$. Substituting into (3) and dividing by $\rho$:

$$ U^2h_0\left(\frac{h_0}{h_1} - 1\right) = \frac{g}{2}(h_0 - h_1)(h_0 + h_1) \;\Longrightarrow\; U^2h_0\,\frac{h_0 - h_1}{h_1} = \frac{g}{2}(h_0 - h_1)(h_0 + h_1). $$

For a bore $h_1 \ne h_0$, so $h_0 - h_1$ cancels. With $r = h_1/h_0$ and $F = U^2/(gh_0)$, dividing by $gh_0^2$ gives $F/r = (1 + r)/2$:

$$ r^2 + r - 2F = 0 \;\Longrightarrow\; \boxed{\,\frac{h_1}{h_0} = \frac{1}{2}\left(\sqrt{1 + 8F} - 1\right)\,} \tag{4} $$

(the negative root is rejected, $h_1 > 0$). From (2), $U_1/U = 1 - h_0/h_1 = (r - 1)/r$; with $s = \sqrt{1 + 8F}$, $r = (s - 1)/2$ and

$$ \boxed{\,\frac{U_1}{U} = 1 - \frac{2}{s - 1} = \frac{\sqrt{1 + 8F} - 3}{\sqrt{1 + 8F} - 1}\,},\qquad F = \frac{U^2}{gh_0}. \tag{5} $$

> [!warning] Erratum in the official solution (reading of the handwriting)
> CL2.pdf gives $h_1/h_0 = \tfrac{1}{2}(\sqrt{1+8F} - 1)$, as in (4). For the velocity it gives, as legible in the scan, $U_1/U = \tfrac{3}{2}\left(\tfrac{1}{3}\sqrt{1+8F} - 1\right) = (\sqrt{1+8F} - 3)/2 = r - 1$. This contradicts its own continuity equation (2), which requires $U_1/U = (r - 1)/r$; the two coincide only for $r = 1$. Check: (2) gives $(U - U_1)h_1 = Uh_0 > 0$, hence $U_1 < U$, whereas $r - 1 > 1$ for $F > 3$ (for $F = 4$, $r - 1 = 1.3723$ against $U_1/U = 0.5785$ from (5)). The computed value is kept.

## Phase 4: Interpretation, Limits and Dimensional Check

- A bore exists only for $F > 1$: $r > 1 \iff s > 3 \iff F > 1$. $F$ compares the speed of the front with the shallow-water wave speed $\sqrt{gh_0}$.
- Weak bore, $F = 1 + \epsilon$: $r \approx 1 + \tfrac{2}{3}\epsilon$ and $U_1/U \approx \tfrac{2}{3}\epsilon \to 0$ (an infinitesimal gravity wave travelling at $\sqrt{gh_0}$).
- Strong bore, $F \gg 1$: $r \approx \sqrt{2F}$ and $U_1 \to U$.
- Dimensions (SI): both sides of (3) are forces per unit width, $[\rho U^2h_0] = [\rho gh^2] = \text{N/m}$; $F$, $r$ and $U_1/U$ are dimensionless.
- Numerical cross-check: $F = 4$, $h_0 = 0.5$ m, $g = 9.81$ m/s$^2$ give $U = 4.4294$ m/s, $h_1/h_0 = 2.3723$ ($h_1 = 1.1861$ m), $U_1/U = 0.57846$ ($U_1 = 2.5623$ m/s); the residuals of (2) and (3) are below $10^{-14}$ in SI units.

> [!info] Extension (beyond the official solution)
> Mechanical energy is not conserved across the bore, so Bernoulli's equation cannot be used between both sections. The head lost is the classical hydraulic-jump value $\Delta H = (h_1 - h_0)^3/(4h_0h_1)$, positive for $h_1 > h_0$.
