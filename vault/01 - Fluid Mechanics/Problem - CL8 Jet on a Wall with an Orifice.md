---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-lineal
  - chorro
  - bernoulli
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL8.pdf"
---

# Problem CL8: Jet Impinging on a Wall with an Orifice

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A circular water jet of diameter $D_j$ and velocity $V_j$ impinges perpendicularly to a wall, where there exists an orifice centered at the jet axis, as shown in the figure of CL8.pdf, so that part of the water flows through the orifice and part is deflected to flow next to the wall. Assuming that the flow velocity is sufficiently large for the effects of viscosity and gravity to be negligible:

- Determine the values of the velocities $V_s$ and $V_r$ for the secondary jet that emerges from the orifice and for the radial wall jet.
- Obtain the thickness $h(r)$ of the radial wall jet.
- Compute the force that the jet exerts on the wall as a function of $\rho$, $V_j$, $D_j$ and $D_s$.

Source: CL8.pdf (page 1). Notes.pdf: Bernoulli's equation Eq. 4.17 (Chapter 4), integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, incompressible, frictionless (viscosity negligible); neglect $\bar{g}$ (buoyancy-free).
- Free jets surrounded by the ambient air at $p_a$. In each jet away from the wall the streamlines are straight and parallel (aligned), so the pressure does not vary across them: $p = p_a$ inside the incoming jet, the secondary jet and the wall jet (official solution).
- Data: $[\rho,\ V_j,\ D_j,\ D_s]$. Unknowns: $[V_s,\ V_r,\ h(r),\ \bar{F}_w]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $V_j$, $D_j$ | velocity and diameter of the jet | m/s, m |
| $V_s$, $D_s$ | secondary jet velocity, orifice diameter | m/s, m |
| $V_r$, $h(r)$ | wall-jet velocity and thickness | m/s, m |
| $\bar{F}_w$ | force of the jet on the wall | N |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the wall; $\bar{e}_x$ along the jet axis (towards the wall); cylindrical coordinate $r$ on the wall, with $\int\bar{e}_r\,d\theta = 0$.
- Fixed control volume around the water: $\Sigma_j$ (section of the incoming jet, $\bar{n} = -\bar{e}_x$), $\Sigma_s$ (section of the secondary jet beyond the orifice, $\bar{n} = +\bar{e}_x$), $\Sigma_r$ (cylinder of radius $r$ across the wall jet, $\bar{n} = \bar{e}_r$, height $h$), $\Sigma_a$ (free surfaces, $p = p_a$, $\bar{v}\cdot\bar{n} = 0$) and $\Sigma_w$ (wetted wall).

Force of the water (and of the ambient air on the dry side) on the wall:

$$ \boxed{\,\bar{F}_w = \int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma - \int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma\,} $$

## Phase 3: Bernoulli and Balances, Surface by Surface

### 3.1 Velocities: Bernoulli along a streamline

Why this tool: for steady, frictionless, incompressible flow without mass forces, $p + \tfrac{1}{2}\rho|\bar{v}|^2$ is constant along a streamline (Notes Eq. 4.17 with $U = 0$, as used in the official solution). Take a streamline from the incoming jet to the wall jet, and another one to the secondary jet; at both ends $p = p_a$:

$$ p_a + \tfrac{1}{2}\rho V_j^2 = p_a + \tfrac{1}{2}\rho V_r^2 \;\Longrightarrow\; \boxed{\,V_r = V_j\,},\qquad p_a + \tfrac{1}{2}\rho V_j^2 = p_a + \tfrac{1}{2}\rho V_s^2 \;\Longrightarrow\; \boxed{\,V_s = V_j\,} \tag{1} $$

**Mass (Notes Eq. 3.11)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_j$ | $-\rho V_j\frac{\pi D_j^2}{4}$ |
| $\Sigma_s$ | $+\rho V_s\frac{\pi D_s^2}{4}$ |
| $\Sigma_r$ | $+\rho V_r\,2\pi r\,h$ |
| $\Sigma_a,\ \Sigma_w$ | $0$ |

With (1), $V_s = V_r = V_j$ and the velocity cancels.

$$ -\frac{\pi D_j^2}{4} + \frac{\pi D_s^2}{4} + 2\pi rh = 0 \;\Longrightarrow\; \boxed{\,h(r) = \frac{D_j^2 - D_s^2}{8\,r}\,} \tag{2} $$

**Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_j$ | $\rho V_j\bar{e}_x(-V_j)\frac{\pi D_j^2}{4} = -\rho V_j^2\frac{\pi D_j^2}{4}\bar{e}_x$ | $0$ ($p = p_a$) | $0$ |
| $\Sigma_s$ | $+\rho V_s^2\frac{\pi D_s^2}{4}\bar{e}_x$ | $0$ ($p = p_a$) | $0$ |
| $\Sigma_r$ | $\rho V_r^2h\,r\int_0^{2\pi}\bar{e}_r\,d\theta = 0$ | $0$ ($p = p_a$) | $0$ |
| $\Sigma_a$ | $0$ | $0$ ($p = p_a$) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F}_w$. With (1), $V_s = V_j$.

$$ \left(\rho V_j^2\frac{\pi D_s^2}{4} - \rho V_j^2\frac{\pi D_j^2}{4}\right)\bar{e}_x = -\bar{F}_w \;\Longrightarrow\; \boxed{\,\bar{F}_w = \rho V_j^2\,\frac{\pi}{4}\left(D_j^2 - D_s^2\right)\bar{e}_x\,} \tag{3} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- Only the part of the jet stopped by the wall (the annulus between $D_s$ and $D_j$) pushes on it; the secondary jet keeps its momentum. For $D_s \to 0$, $\bar{F}_w \to \rho V_j^2\pi D_j^2/4$, the force of a jet on a flat plate; for $D_s \to D_j$ the jet passes through and $\bar{F}_w \to 0$, $h \to 0$.
- $h \propto 1/r$: the wall jet thins as it spreads, keeping the flow rate $2\pi rhV_j$ constant.
- Dimensions (SI): $[h] = \text{m}^2/\text{m} = \text{m}$; $[\rho V_j^2D^2] = \text{N}$.
- Numerical illustration (hypothetical data): $\rho = 1000$ kg/m$^3$, $V_j = 10$ m/s, $D_j = 0.05$ m, $D_s = 0.02$ m give $|\bar{F}_w| = 164.93$ N and $h(0.1\ \text{m}) = 2.625$ mm.
- Agreement with the official solution: CL8.pdf obtains (1), (2) and (3).
