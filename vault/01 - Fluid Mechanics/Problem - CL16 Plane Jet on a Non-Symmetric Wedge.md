---
materia: Fluid Mechanics
tema: "Topic 3: Conservation Laws"
tags:
  - problema-examen
  - leyes-de-conservacion
  - momento-angular
  - energia
  - chorro
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-03-conservation-laws/problemas/CL16.pdf"
---

# Problem CL16: Plane Jet Split by a Non-Symmetric Wedge: Force, Moment and Heat

> Official UC3M conservation-laws problem collection (Introduction to Fluid Mechanics). Part of [[Topic 3 - Conservation Laws]]. Related: [[Concept - Integral Conservation of Mass, Momentum and Energy|integral balances]], [[Concept - Reynolds Transport Theorem|Reynolds transport theorem]], [[Formula Sheet - Topic 3 Conservation Laws|formula sheet]].
> Method: each balance is written in full with the vanishing terms crossed out and the reason underneath; each surface integral is then evaluated surface by surface (the vertical line drawn under each integral in class), and the wall terms are grouped (boxed) as the force on the body.

## Statement

A plane liquid jet of constant density $\rho$, thickness $h$ and uniform velocity $v$, impinges on a non-symmetric wedge of geometry and dimensions shown in the figure of CL16.pdf. The wedge splits the jet into two layers of unequal flux, such that a portion $\alpha$ of the volume flux is deflected an angle $\theta$, and the rest of the fluid is deflected an angle $2\theta$. The flow is steady; viscous and gravitational forces are negligible; the known data are $(\rho, c, v, h, \alpha, \theta, L, p_a, T_0, T_1, T_2)$.

- Noting that the conditions for the use of Bernoulli's theorem are met, determine the (uniform) velocity of the fluid on each deflected layer.
- Determine the thickness $h_1$ and $h_2$ of each layer.
- Determine the force $\bar{F}$ (per unit length in the $z$-direction) that the liquid jet and the ambient air exert on the wedge.
- Determine the moment $\bar{M}_0$ due to the force $\bar{F}$ about the corner $\bar{x}_0$ of the wedge. Find the value of the fraction $\alpha$ that would produce a null moment, $\bar{M}_0 = 0$.
- Knowing the uniform temperature $T_0$ of the incoming jet, the uniform temperatures $T_1$ and $T_2$ of the two liquid layers when they lose contact with the wedge, and the constant specific heat $c$ of the liquid, determine the heat $q$ transferred per unit surface from the liquid to the wedge. Assume that the heat flux is uniform on the wedge surface and that there is no heat transfer by conduction between the liquid and the ambient air.

![[attachments/FM-T3/cl16-statement.svg]]
*Statement figure (redrawn from CL16.pdf, p. 1): plane jet ($h$, $Q$, $v$, $T_0$) on the wedge with corner $\bar{x}_0$; the layer $\alpha Q$ ($T_1$) leaves at $\theta$ and $(1 - \alpha)Q$ ($T_2$) at $2\theta$; faces of horizontal extent $L$; heat flux $q$ into the wedge; ambient $p_a$*

Source: CL16.pdf (pages 1-2, exam of Jan 14, 2013, with handwritten results). Notes.pdf: Bernoulli's equation Eq. 4.17, integral mass balance Eq. 3.11, integral momentum balance Eq. 3.36, integral angular momentum balance Eq. 3.38, integral total energy balance Eq. 3.46.

## Phase 1: Hypotheses, Data and Unknowns

- Steady, planar (per unit length in $z$), incompressible, frictionless; neglect $\bar{g}$; free jets at $p_a$ (straight parallel streamlines in the layers away from the corner, so $p = p_a$ inside them).
- Geometry (figure): the incoming jet is centred on the $x$ axis, which passes through the corner $\bar{x}_0$; layer 1 leaves along $\bar{t}_1 = \cos\theta\,\bar{e}_x + \sin\theta\,\bar{e}_y$ on the upper face, layer 2 along $\bar{t}_2 = \cos2\theta\,\bar{e}_x - \sin2\theta\,\bar{e}_y$ on the lower face. The faces have horizontal length $L$, i.e. lengths $L/\cos\theta$ and $L/\cos2\theta$.
- Heat: uniform flux $q$ from the liquid to the wedge on both faces; no conduction to the air; $e = cT$.
- Data: $[\rho,\ c,\ v,\ h,\ \alpha,\ \theta,\ L,\ p_a,\ T_0,\ T_1,\ T_2]$. Unknowns: $[v_1,\ v_2,\ h_1,\ h_2,\ \bar{F},\ \bar{M}_0,\ q]$.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $v$, $h$ | jet velocity and thickness | m/s, m |
| $\alpha$, $\theta$ | flux fraction and deflection angle | 1, rad |
| $h_1$, $h_2$ | layer thicknesses | m |
| $\bar{F}$, $\bar{M}_0$ | force and moment per unit length | N/m, N$\cdot$m/m |
| $q$ | heat flux to the wedge | W/m$^2$ |

## Phase 2: Frames, Control Volume and Surfaces

- Frame fixed to the wedge; origin at the corner $\bar{x}_0$; $\bar{e}_z$ towards the reader.
- Surfaces: $\Sigma_0$ (incoming jet section, $\bar{n} = -\bar{e}_x$), $\Sigma_1$, $\Sigma_2$ (layer sections normal to $\bar{t}_1$, $\bar{t}_2$, $\bar{n} = \bar{t}_1, \bar{t}_2$), $\Sigma_a$ (free surfaces, $p = p_a$) and $\Sigma_w$ (wetted faces). On layer $k$, $\bar{x} - \bar{x}_0 = s\,\bar{t}_k + \eta\,\bar{m}_k$, with $\bar{m}_1 = -\sin\theta\,\bar{e}_x + \cos\theta\,\bar{e}_y$, $\bar{m}_2 = -\sin2\theta\,\bar{e}_x - \cos2\theta\,\bar{e}_y$ the unit normals pointing away from the wedge and $0 \le \eta \le h_k$.

![[attachments/FM-T3/cl16-cv.svg]]
*Control volume of the solution: $\Sigma_0$ (incoming jet, $\bar{n} = -\bar{e}_x$), $\Sigma_1$ and $\Sigma_2$ (sections across the layers, $\bar{n} = \bar{t}_1$, $\bar{t}_2$), the free surfaces $\Sigma_a$ at $p_a$ and the wetted faces $\Sigma_w$; $\bar{m}_1$, $\bar{m}_2$ are the unit normals pointing away from the wedge, and moments are taken about the corner $\bar{x}_0$*

$$ \boxed{\,\bar{F} = \int_{\Sigma_w}\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{\bar{M}_0 = \int_{\Sigma_w}(\bar{x} - \bar{x}_0)\wedge\left[(p - p_a)\,\bar{n} - \bar{\bar{\tau}}'\cdot\bar{n}\right]d\sigma\,} $$

$$ \boxed{q = -\frac{1}{L/\cos\theta + L/\cos2\theta}\int_{\Sigma_w}\bar{q}\cdot\bar{n}_{\text{in}}\,d\sigma\,} $$

## Phase 3: Bernoulli and Balances, Surface by Surface

### 1. Velocities

Bernoulli (Notes Eq. 4.17, $U = 0$) along a free streamline from the incoming jet to each layer, with $p = p_a$ at both ends: $p_a + \tfrac{1}{2}\rho v^2 = p_a + \tfrac{1}{2}\rho v_k^2$, so

$$ \boxed{\,v_1 = v_2 = v\,} \tag{1} $$

**2. Mass (Notes Eq. 3.11): thicknesses**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\,(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}\,d\sigma = 0 $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- |
| $\Sigma_0$ | $-\rho vh = -\rho Q$ |
| $\Sigma_1$ | $+\rho vh_1 = \rho\alpha Q$ |
| $\Sigma_2$ | $+\rho vh_2 = \rho(1 - \alpha)Q$ |
| $\Sigma_a,\ \Sigma_w$ | $0$ |

$$ \boxed{\,h_1 = \alpha h,\qquad h_2 = (1 - \alpha)h\,} \tag{2} $$

**3. Linear momentum (Notes Eq. 3.36)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\,dV}}_{\text{neglect } \bar{g}} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int(p - p_a)\,\bar{n}\,d\sigma$ | $\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- |
| $\Sigma_0$ | $-\rho v^2h\,\bar{e}_x$ | $0$ | $0$ |
| $\Sigma_1$ | $\rho v^2\alpha h\,(\cos\theta\,\bar{e}_x + \sin\theta\,\bar{e}_y)$ | $0$ | $0$ |
| $\Sigma_2$ | $\rho v^2(1 - \alpha)h\,(\cos2\theta\,\bar{e}_x - \sin2\theta\,\bar{e}_y)$ | $0$ | $0$ |
| $\Sigma_a$ | $0$ | $0$ ($p = p_a$) | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\int_{\Sigma_w}(p - p_a)\,\bar{n}\,d\sigma$ | $\int_{\Sigma_w}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma$ |

Boxed $\Sigma_w$ terms: $-\bar{F}$.

$$ \boxed{\,\bar{F} = \rho v^2h\left\{\left[1 - \alpha\cos\theta - (1 - \alpha)\cos2\theta\right]\bar{e}_x - \left[\alpha\sin\theta - (1 - \alpha)\sin2\theta\right]\bar{e}_y\right\}\,} \tag{3} $$

**4. Angular momentum about x̄₀ (Notes Eq. 3.38)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\,(\bar{x} - \bar{x}_0)\wedge\bar{v}\,dV}}_{0} + \int_{\Sigma_c}\rho\,[(\bar{x} - \bar{x}_0)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma = -\int_{\Sigma_c}(\bar{x} - \bar{x}_0)\wedge(p - p_a)\bar{n}\,d\sigma + \int_{\Sigma_c}(\bar{x} - \bar{x}_0)\wedge(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\,[(\bar{x} - \bar{x}_0)\wedge\bar{v}](\bar{v}\cdot\bar{n})\,d\sigma$ | $\text{pressure and viscous moments}$ |
| :--- | :--- | :--- |
| $\Sigma_0$ | $\int_{-h/2}^{h/2}\rho v\,(-yv)(-1)\,dy\;\bar{e}_z = 0$ (odd in $y$) | $0$ |
| $\Sigma_1$ | $\int_0^{h_1}\rho v^2\,\eta\,(\bar{m}_1\wedge\bar{t}_1)\,d\eta = -\rho v^2\frac{h_1^2}{2}\,\bar{e}_z$ | $0$ |
| $\Sigma_2$ | $\int_0^{h_2}\rho v^2\,\eta\,(\bar{m}_2\wedge\bar{t}_2)\,d\eta = +\rho v^2\frac{h_2^2}{2}\,\bar{e}_z$ | $0$ |
| **$\Sigma_w$** (boxed) | $0$ | $-\bar{M}_0$ |

Here $\bar{m}_1\wedge\bar{t}_1 = (-\sin^2\theta - \cos^2\theta)\,\bar{e}_z = -\bar{e}_z$ and $\bar{m}_2\wedge\bar{t}_2 = (\sin^22\theta + \cos^22\theta)\,\bar{e}_z = +\bar{e}_z$; the part $s\,\bar{t}_k\wedge\bar{t}_k$ vanishes. The antiderivative of $\eta$ is $\eta^2/2$; Barrow's rule between $0$ and $h_k$ gives $h_k^2/2$. With (2): $-\frac{\rho v^2h^2}{2}\left[\alpha^2 - (1 - \alpha)^2\right] = -\frac{\rho v^2h^2}{2}(2\alpha - 1)$.

$$ -\frac{\rho v^2h^2}{2}(2\alpha - 1)\,\bar{e}_z = -\bar{M}_0 \;\Longrightarrow\; \boxed{\,\bar{M}_0 = \rho v^2\,\frac{h^2}{2}\,(2\alpha - 1)\,\bar{e}_z,\qquad \bar{M}_0 = 0 \iff \alpha = \frac{1}{2}\,} \tag{4} $$

**5. Total energy (Notes Eq. 3.46)**

$$ \underbrace{\cancel{\frac{d}{dt}\int_{V_c}\rho\left(e + \tfrac{v^2}{2}\right)dV}}_{0\ (\text{steady})} + \int_{\Sigma_c}\rho\left(e + \frac{v^2}{2}\right)[(\bar{v} - \underbrace{\cancel{\bar{v}_c}}_{0})\cdot\bar{n}]\,d\sigma = -\int_{\Sigma_c}p\,\bar{v}\cdot\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma + \underbrace{\cancel{\int_{V_c}\rho\bar{g}\cdot\bar{v}\,dV}}_{\text{neglect } \bar{g}} - \int_{\Sigma_c}\bar{q}\cdot\bar{n}\,d\sigma + \underbrace{\cancel{\int_{V_c}Q_R\,dV}}_{0} $$

Each surface integral, surface by surface (the vertical line drawn under each integral in class):

| Surface | $\int\rho\left(e + \tfrac{v^2}{2}\right)(\bar{v}\cdot\bar{n})\,d\sigma$ | $-\int p\,\bar{v}\cdot\bar{n}\,d\sigma$ | $\int\bar{v}\cdot(\bar{\bar{\tau}}'\cdot\bar{n})\,d\sigma$ | $-\int\bar{q}\cdot\bar{n}\,d\sigma$ |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma_0$ | $-\rho vh\left(cT_0 + \tfrac{v^2}{2}\right)$ | $+p_avh$ | $0$ | $0$ |
| $\Sigma_1$ | $+\rho v\alpha h\left(cT_1 + \tfrac{v^2}{2}\right)$ | $-p_av\alpha h$ | $0$ | $0$ |
| $\Sigma_2$ | $+\rho v(1 - \alpha)h\left(cT_2 + \tfrac{v^2}{2}\right)$ | $-p_av(1 - \alpha)h$ | $0$ | $0$ |
| $\Sigma_a$ | $0$ | $0$ | $0$ | $0$ (no conduction to the air) |
| **$\Sigma_w$** (boxed) | $0$ | $0$ ($\bar{v} = 0$) | $0$ | $-q\left(\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}\right)$ |

Boxed $\Sigma_w$ term: the heat leaves the liquid towards the wedge. The kinetic-energy and pressure-work terms cancel because $\alpha + (1 - \alpha) = 1$.

$$ \rho vhc\left[\alpha T_1 + (1 - \alpha)T_2 - T_0\right] = -q\left(\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}\right) \;\Longrightarrow\; \boxed{\,q = \frac{\rho cvh}{\frac{L}{\cos\theta} + \frac{L}{\cos2\theta}}\left[T_0 - \alpha T_1 - (1 - \alpha)T_2\right]\,} \tag{5} $$

## Phase 4: Interpretation, Limits and Dimensional Check

- Symmetric-split check: with $\alpha = 1/2$ the two layers carry equal flux and their moments about the corner cancel, (4). The force (3) is still not symmetric because the deflections $\theta$ and $2\theta$ differ.
- Limit $\theta \to 0$: no deflection, $\bar{F} \to 0$ in (3) (both brackets vanish).
- (5): $q > 0$ (liquid heats the wedge) when the liquid leaves colder than it arrived on average.
- Dimensions (SI, per unit length): $[\rho v^2h] = \text{N/m}$; $[\rho v^2h^2] = \text{N}\cdot\text{m}/\text{m}$; $[\rho cvh\,\Delta T/L] = \text{W/m}^2$.
- Numerical cross-check of (4) (hypothetical data): $\rho = 1000$ kg/m$^3$, $v = 10$ m/s, $h = 0.02$ m, $\alpha = 0.3$, $\theta = 25^\circ$: midpoint quadrature of the two layer integrals gives an angular-momentum flux of $8.000$ N$\cdot$m/m, equal to $-\rho v^2h^2(2\alpha - 1)/2 = 8$, i.e. $M_{0,z} = -8$ N$\cdot$m/m.
- Agreement with the official solution: CL16.pdf obtains (1) to (5).
