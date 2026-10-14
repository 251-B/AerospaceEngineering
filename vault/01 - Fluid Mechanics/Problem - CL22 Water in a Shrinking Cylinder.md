---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - volumen-de-control-movil
  - energia-cinetica
  - no-estacionario
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL22.pdf"
---

# Problem CL22: Water in a Shrinking Cylinder: Level, Velocity, Force and Power

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

Figure (a) of CL22.pdf shows a cylinder of radius $a_0$ closed at the bottom that contains a volume $\pi a_0^2h_0$ of water. The water is in contact with the stagnant atmosphere at a pressure $p_a$. At time $t = 0$ the cylinder radius $a(t)$ starts decreasing and the level of water rises, as shown in figure (b) for a generic instant of time $t$. If $a(t)$ is known,

- Define clearly a control volume and use the mass conservation principle to determine the level of water $h(t)$ and the velocity of the free surface $\dot{h}(t)$ for a generic instant of time $t$.
- Using control volume $V_2$, as shown in the figure (b), use the continuity equation to obtain the $z$-component of the velocity $v_z(z,t)$ in the liquid at an arbitrary level $z$, as sketched in figure b.
- Using the previous results, and specifying the control volume used in the analysis, determine separately the force exerted by both the liquid and the atmosphere on the cylinder. Calculate the net force exerted by both fluids on the cylinder.
- Using the kinetic energy equation, and neglecting $v_r^2$ in the kinetic energy, obtain the mechanical power exerted on the solid walls by both the liquid and the atmosphere. Determine the net power exerted by both fluids on the liquid.

Note: Neglect viscous dissipation within the liquid, viscous stresses at the free surface and take the pressure in the air as a constant $p_a$.

![[attachments/FM-T3/cl22-statement.svg]]
*Statement figure (redrawn from CL22.pdf, p. 1): (a) at $t = 0$, radius $a_0$ and level $h_0$; (b) at $t > 0$, radius $a(t)$, level $h(t)$ and the fixed control volume $V_2$ up to the level $z$*

Source: CL22.pdf (pages 1-3, exam of 28-10-2018, with handwritten solution). Notes.pdf, Chapter 3: Reynolds transport theorem for a moving control volume Eqs. 3.7-3.8, integral mass balance Eq. 3.10, integral momentum balance Eq. 3.35, energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Unsteady flow of an incompressible liquid (water, $\rho$ constant) with gravity $\bar{g} = -g\bar{e}_z$ (here gravity is kept); viscous dissipation and stresses at the free surface neglected; air at constant $p_a$.
- The radius $a(t)$ is a known function with $a(0) = a_0$, $\dot{a} < 0$; the bottom is fixed at $z = 0$; the free surface stays flat at $z = h(t)$.
- The axial velocity is assumed uniform over each horizontal section, $v_z(z,t)$, and the kinetic energy of the radial motion ($v_r^2$) is neglected (statement).
- Data: $[a(t),\ a_0,\ h_0,\ \rho,\ g,\ p_a]$. Unknowns: $[h,\ \dot{h},\ v_z,\ F_{L\to W},\ F_{A\to W},\ \dot{W}_{L\to W},\ \dot{W}_{A\to W}]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a(t)$, $a_0$ | cylinder radius, initial radius | m |
| $h(t)$, $h_0$ | water level, initial level | m |
| $v_z(z,t)$ | axial velocity of the water | m/s |
| $F$ | axial force on the cylinder | N |
| $\dot{W}$ | mechanical power on the walls | W |

## Phase 2: Frames, Control Volumes and Surfaces

- Inertial frame fixed to the bottom; cylindrical coordinates $(r, \theta, z)$, $\bar{e}_z$ upwards.
- Control volume 1 (the water itself, a material volume): $\Sigma_s$ (free surface, $\bar{v} = \bar{v}_c = \dot{h}\bar{e}_z$, $\bar{n} = \bar{e}_z$), $\Sigma_L$ (lateral wall, $\bar{v} = \bar{v}_c = \dot{a}\bar{e}_r$, $\bar{n} = \bar{e}_r$) and $\Sigma_b$ (bottom, $\bar{v} = \bar{v}_c = 0$, $\bar{n} = -\bar{e}_z$). Everywhere $\bar{v} = \bar{v}_c$, so no flux crosses $\Sigma_c$.
- Control volume $V_2$: from the bottom to a fixed level $z$: $\Sigma_b$, $\Sigma_{L2}$ (lateral wall, moving with $\dot{a}\bar{e}_r$) and $\Sigma_z$ (fixed horizontal section, $\bar{v}_c = 0$, $\bar{n} = \bar{e}_z$).
- Axial forces on the cylinder: $F_{L\to W}$ (liquid on $\Sigma_L$, $\Sigma_b$) and $F_{A\to W}$ (atmosphere on the outer surface: radial on the lateral wall, $+p_a\pi a^2$ on the outer face of the bottom; the air inside above the water also pushes only radially).

![[attachments/FM-T3/cl22-cv.svg]]
*Control volumes of the solution: (1) the water, with $\Sigma_s$, $\Sigma_L$, $\Sigma_b$ and their outward normals, used for mass, momentum and kinetic energy; (2) $V_2$, with the fixed section $\Sigma_z$, the moving wall $\Sigma_{L2}$ and $\Sigma_b$, used for $v_z(z,t)$ (after the official solution, CL22.pdf, p. 2)*

## Phase 3: Balances, Surface by Surface

**1. Mass on control volume 1 (Notes Eq. 3.10)**

$$ \frac{d}{dt}\int_{V_c(t)}\rho\,dV + \int_{\Sigma_c(t)}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_s$ | $0$ ($\bar{v} = \bar{v}_c = \dot{h}\bar{e}_z$) |
| $\Sigma_L$ | $0$ ($\bar{v} = \bar{v}_c = \dot{a}\bar{e}_r$) |
| $\Sigma_b$ | $0$ ($\bar{v} = \bar{v}_c = 0$) |

Therefore $\frac{d}{dt}\left[\rho\pi a^2h\right] = 0$ and $\rho\pi a^2(t)h(t) = \rho\pi a_0^2h_0$. Differentiating $h = a_0^2h_0a^{-2}$ with the chain rule, $\frac{dh}{dt} = a_0^2h_0\,(-2)a^{-3}\dot{a}$:

$$ \boxed{\,h(t) = \frac{a_0^2}{a^2(t)}\,h_0\,}\ \ \text{(1)}\qquad \boxed{\,\dot{h} = -\frac{2a_0^2h_0\,\dot{a}}{a^3} = -2h\,\frac{\dot{a}}{a}\,}\ \ \text{(2)} $$

**2. Mass on V₂ (Notes Eq. 3.10)**

$$ \frac{d}{dt}\int_{V_2(t)}\rho\,dV + \int_{\Sigma_2(t)}\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_z$ | $\rho\,v_z\,\pi a^2$ ($\bar{v}_c = 0$) |
| $\Sigma_{L2}$ | $0$ ($\bar{v} = \bar{v}_c$) |
| $\Sigma_b$ | $0$ |

Volume term: $\frac{d}{dt}(\rho\pi a^2z) = \rho\pi z\frac{d(a^2)}{dt} = 2\rho\pi za\dot{a}$ ($z$ fixed).

$$ 2\rho\pi za\dot{a} + \rho v_z\pi a^2 = 0 \;\Longrightarrow\; \boxed{\,v_z(z,t) = -\frac{1}{a^2}\frac{d(a^2)}{dt}\,z = -\frac{2\dot{a}(t)}{a(t)}\,z\,} \tag{3} $$

Check: at $z = h$, $v_z = -2\dot{a}h/a = \dot{h}$, the velocity of the free surface (2). It is also consistent with the differential continuity equation: with $v_r = \dot{a}r/a$ (so that $v_r = \dot{a}$ at the wall), $\frac{1}{r}\frac{\partial(rv_r)}{\partial r} + \frac{\partial v_z}{\partial z} = \frac{2\dot{a}}{a} - \frac{2\dot{a}}{a} = 0$ (extension).

**3. Momentum, z component, on control volume 1 (Notes Eq. 3.35)**

$$ \frac{d}{dt}\int_{V_c}\rho v_z\,dV + \underbrace{\cancel{\int_{\Sigma_c}\rho v_z\,[(\bar{v} - \bar{v}_c)\cdot\bar{n}]\,d\sigma}}_{0} = -\int_{\Sigma_c}p\,n_z\,d\sigma + \int_{\Sigma_c}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma - \int_{V_c}\rho g\,dV $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $-\int p\,n_z\,d\sigma$ | $\int(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$ |
| :--- | :--- | :--- |
| $\Sigma_s$ | $-p_a\pi a^2$ | $0$ (neglected) |
| **$\Sigma_L$** (boxed) | $-\int_{\Sigma_L}p\,n_z\,d\sigma$ | $\int_{\Sigma_L}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$ |
| **$\Sigma_b$** (boxed) | $-\int_{\Sigma_b}p\,n_z\,d\sigma$ | $\int_{\Sigma_b}(\bar{\bar{\tau}}'\cdot\bar{n})_z\,d\sigma$ |

Boxed $\Sigma_L$, $\Sigma_b$ terms: the force of the walls on the liquid, $-F_{L\to W}$. Volume terms: $\int_{V_c}\rho v_z\,dV = \int_0^h\rho\left(-\frac{2\dot{a}}{a}z\right)\pi a^2\,dz = -2\rho\pi a\dot{a}\left[\frac{z^2}{2}\right]_0^h = -\rho\pi a\dot{a}h^2$, and the weight $\rho g\pi a_0^2h_0$.

$$ \frac{d}{dt}\left(-\rho\pi a\dot{a}h^2\right) = -F_{L\to W} - p_a\pi a^2 - \rho g\pi a_0^2h_0 \tag{4} $$

Product rule: $\frac{d}{dt}(a\dot{a}h^2) = \dot{a}^2h^2 + a\ddot{a}h^2 + 2a\dot{a}h\dot{h}$, and with (2), $2a\dot{a}h\dot{h} = 2a\dot{a}h\left(-2h\frac{\dot{a}}{a}\right) = -4\dot{a}^2h^2$, so $\frac{d}{dt}(a\dot{a}h^2) = h^2\left(a\ddot{a} - 3\dot{a}^2\right)$ with $h^2 = \frac{a_0^4h_0^2}{a^4}$ from (1). From (4):

$$ \boxed{\,F_{L\to W} = \rho\pi\,\frac{a_0^4h_0^2}{a^4}\left(a\ddot{a} - 3\dot{a}^2\right) - p_a\pi a^2 - \rho g\pi a_0^2h_0\,} \tag{5} $$

$$ \boxed{\,F_{A\to W} = p_a\pi a^2\,} $$

$$ \boxed{\,F = F_{L\to W} + F_{A\to W} = \rho\pi a_0^2\left[\frac{a_0^2h_0^2}{a^4}\left(a\ddot{a} - 3\dot{a}^2\right) - gh_0\right]\,} \tag{6} $$

**4. Kinetic energy on control volume 1**

$$ \frac{d}{dt}\int_{V_c}\rho\frac{v_z^2}{2}\,dV + \underbrace{\cancel{\int_{\Sigma_c}\rho\frac{v^2}{2}(\bar{v} - \bar{v}_c)\cdot\bar{n}\,d\sigma}}_{0} = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV + \underbrace{\cancel{\int_{V_c}p\,\nabla\cdot\bar{v}\,dV}}_{0\ (\text{incompressible})} - \underbrace{\cancel{\int_{V_c}\Phi_v\,dV}}_{\text{neglect}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |
| :--- | :--- | :--- |
| $\Sigma_s$ | $-p_a\dot{h}\,\pi a^2$ | $0$ (neglected) |
| **$\Sigma_L$** (boxed) | $-\int_{\Sigma_L}p\,\dot{a}\,d\sigma$ | $\int_{\Sigma_L}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ |
| $\Sigma_b$ | $0$ ($\bar{v} = 0$) | $0$ ($\bar{v} = 0$) |

Boxed $\Sigma_L$ terms: the power of the walls on the liquid, $-\dot{W}_{L\to W}$. Volume terms: $\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV = -\rho g\int_0^hv_z\pi a^2\,dz = \rho g\pi a\dot{a}h^2$ and $\int_{V_c}\rho\frac{v_z^2}{2}dV = \frac{\rho\pi a^2}{2}\frac{4\dot{a}^2}{a^2}\left[\frac{z^3}{3}\right]_0^h = \frac{2}{3}\rho\pi\dot{a}^2h^3$.

$$ \frac{d}{dt}\left(\frac{2}{3}\rho\pi\dot{a}^2h^3\right) = -\dot{W}_{L\to W} - p_a\pi a^2\dot{h} + \rho g\pi a\dot{a}h^2 \tag{7} $$

Chain and product rule with (2): $\frac{d}{dt}(\dot{a}^2h^3) = 2\dot{a}\ddot{a}h^3 + 3\dot{a}^2h^2\dot{h} = 2\dot{a}\ddot{a}h^3 - 6\dot{a}^3\frac{h^3}{a} = 2h^3\dot{a}\left(\ddot{a} - 3\frac{\dot{a}^2}{a}\right)$, with $h^3 = \frac{a_0^6h_0^3}{a^6}$; and $-p_a\pi a^2\dot{h} = 2p_a\pi\frac{a_0^2}{a}h_0\dot{a}$. From (7):

$$ \boxed{\,\dot{W}_{L\to W} = -\frac{4}{3}\rho\pi\left(\frac{a_0}{a}\right)^6h_0^3\,\dot{a}\left(\ddot{a} - \frac{3\dot{a}^2}{a}\right) + 2p_a\pi\frac{a_0^2}{a}h_0\,\dot{a} + \rho g\pi a\dot{a}h^2\,} \tag{8} $$

Atmosphere on the walls: only the outer lateral surface below the water level moves against an unbalanced $p_a$ (above the level, the air acts on both faces), and the bottom does not move: $\dot{W}_{A\to W} = -\int p_a\,\bar{v}\cdot\bar{n}_{out}\,d\sigma = -p_a\dot{a}\,2\pi ah$:

$$ \boxed{\,\dot{W}_{A\to W} = -2p_a\pi\frac{a_0^2}{a}h_0\,\dot{a}\,} $$

$$ \boxed{\,\dot{W} = \dot{W}_{L\to W} + \dot{W}_{A\to W} = -\frac{4}{3}\rho\pi\left(\frac{a_0}{a}\right)^6h_0^3\,\dot{a}\left(\ddot{a} - \frac{3\dot{a}^2}{a}\right) + \rho g\pi a\dot{a}h^2\,} \tag{9} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- At rest ($\dot{a} = \ddot{a} = 0$): $F_{L\to W} = -p_a\pi a^2 - \rho g\pi a_0^2h_0$ (the water and the air above it push the bottom down with $p_a$ and the weight), the atmosphere pushes the bottom up with $p_a\pi a^2$, and the net force is the weight. The ambient pressure cancels in the net force (6) and in the net power (9).
- The term $\rho\pi\frac{a_0^4h_0^2}{a^4}(a\ddot{a} - 3\dot{a}^2)$ is minus the rate of change of the momentum of the water: the walls must accelerate the rising column.
- The statement asks finally for 'the net power exerted by both fluids on the liquid'; from the context (and the official solution) the intended quantity is the net power of both fluids on the walls, (9).
- Dimensions (SI): $[\rho a_0^4h_0^2\dot{a}^2/a^4] = \text{N}$; $[\rho(a_0/a)^6h_0^3\dot{a}\ddot{a}] = \text{W}$; $[p_aa_0^2h_0\dot{a}/a] = \text{W}$.
- Numerical cross-check (hypothetical data): $a(t) = a_0(1 - 0.15t + 0.04t^2)$, $a_0 = 0.1$ m, $h_0 = 0.3$ m, $\rho = 1000$ kg/m$^3$ at $t = 0.7$ s: differentiating numerically the momentum and the kinetic energy of the water (quadrature of the integrals of 3 and 4) reproduces $F_{L\to W} = -2755.01$ N and $\dot{W}_{L\to W} = -199.696$ W from (5) and (8) to 12 digits; the net values are $F = -92.27$ N and $\dot{W} = -3.399$ W.
- Agreement with the official solution: CL22.pdf obtains (1) to (9).
