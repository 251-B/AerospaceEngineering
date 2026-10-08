---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - dipolo
  - potencial
  - polares
  - aceleracion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K5.pdf"
---

# Problem K5: Oscillating Planar Dipole

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Derivada Material y Aceleracion del Fluido|material derivative and acceleration]], [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity, circulation and potential]], [[Concepto - Coordenadas Curvilineas y Operadores Diferenciales|polar coordinates]].

## Statement

For the planar fluid motion deriving from the velocity potential

$$ \varphi = M\cos(\Omega t)\,\frac{\cos\theta}{r}, $$

obtain:

1. Radial and azimuthal velocity components.
2. Expansion rate $\nabla\cdot\vec{v}$.
3. Vorticity.
4. Acceleration of the fluid particle initially located at $r = 1$ and $\theta = \pi/2$.
5. Initial value of the circulation around a circle of radius $R = 1/2$ centered at $(r = 1, \theta = \pi/2)$.
6. Streamlines.
7. Trajectories and particle paths.

Source: K5.pdf (page 1). Notes.pdf, Chapter 2: gradient, divergence and curl in orthogonal coordinates Eqs. (2.3), (2.5), (2.6); potential Eq. (2.34); material derivative and acceleration Eqs. (2.23)-(2.27); circulation and Stokes theorem Eqs. (2.29)-(2.33); trajectories Eq. (2.12); stream lines Eq. (2.21).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar, unsteady, potential flow $\mathbf{v} = \nabla\varphi$ in the plane $(r,\theta)$, for $r > 0$. The potential is that of a dipole whose strength $M\cos\Omega t$ oscillates in time.
- Degrees of freedom: two spatial coordinates $(r,\theta)$ plus time; the only time scale is $\Omega^{-1}$.
- Dimensions of the constants follow from $\varphi$ (a velocity times a length, m$^2$/s): $M\cos\Omega t/r$ has the units of $\varphi$, so $M$ has units m$^3$/s.
- The origin is a singular point and is excluded.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $M$ | dipole strength (per unit depth) | m$^3$/s |
| $\Omega$ | angular frequency | s$^{-1}$ |
| $r$, $\theta$ | polar coordinates (the data $r=1$, $R=1/2$ are lengths in m) | m, rad |
| $\varphi$ | velocity potential | m$^2$/s |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame at rest with the dipole; polar coordinates $(r,\theta)$ with scale factors $(1, r)$, $x = r\cos\theta$, $y = r\sin\theta$, and $\mathbf{e}_z = \mathbf{e}_r\wedge\mathbf{e}_\theta$.
- Gradient: $\nabla\varphi = \partial_r\varphi\,\mathbf{e}_r + r^{-1}\partial_\theta\varphi\,\mathbf{e}_\theta$; divergence: $\nabla\cdot\mathbf{v} = r^{-1}\left[\partial_r(rv_r) + \partial_\theta v_\theta\right]$; vorticity: $\omega_z = r^{-1}\left[\partial_r(rv_\theta) - \partial_\theta v_r\right]$ (Eqs. 2.3, 2.5, 2.6).
- Acceleration in curvilinear coordinates: the component form $a_i = Dv_i/Dt$ of Eq. (2.27) holds only in Cartesian coordinates. The coordinate-free form of Eq. (2.26), $\mathbf{a} = \partial_t\mathbf{v} + \nabla\!\left(\lvert\mathbf{v}\rvert^2/2\right) - \mathbf{v}\wedge\left(\nabla\wedge\mathbf{v}\right)$, is used instead.
- For part 7 the material coordinates are the initial position $(r_0,\theta_0)$ at $t = 0$.

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity components

Why this tool: since the motion derives from a potential, $\mathbf{v} = \nabla\varphi$ (Eq. 2.34), with the polar gradient above. Write $c(t) \equiv \cos\Omega t$.
$$ v_r = \frac{\partial\varphi}{\partial r} = M c\cos\theta\,\frac{\partial}{\partial r}\left(\frac{1}{r}\right) = \boxed{\,-\frac{Mc\cos\theta}{r^2},\,} \qquad v_\theta = \frac{1}{r}\frac{\partial\varphi}{\partial\theta} = \frac{1}{r}\cdot\frac{Mc}{r}\left(-\sin\theta\right) = \boxed{\,-\frac{Mc\sin\theta}{r^2}.\,} $$

### 3.2 Expansion rate

Why this tool: $\nabla\cdot\mathbf{v}$ is the rate of volume change per unit volume (Eqs. 2.62-2.63).
$$ r\,v_r = -\frac{Mc\cos\theta}{r} \;\Rightarrow\; \frac{\partial(rv_r)}{\partial r} = \frac{Mc\cos\theta}{r^2}, \qquad \frac{\partial v_\theta}{\partial\theta} = -\frac{Mc\cos\theta}{r^2}, $$
$$ \nabla\cdot\mathbf{v} = \frac{1}{r}\left[\frac{Mc\cos\theta}{r^2} - \frac{Mc\cos\theta}{r^2}\right] = \boxed{\,0.\,} $$
The flow is incompressible for all $t$ (consistent with $\nabla^2\varphi = 0$).

### 3.3 Vorticity

Why this tool: $\omega_z = r^{-1}\left[\partial_r(rv_\theta) - \partial_\theta v_r\right]$ is twice the angular velocity of the fluid element (Eq. 2.52).
$$ r\,v_\theta = -\frac{Mc\sin\theta}{r} \;\Rightarrow\; \frac{\partial(rv_\theta)}{\partial r} = \frac{Mc\sin\theta}{r^2}, \qquad \frac{\partial v_r}{\partial\theta} = \frac{Mc\sin\theta}{r^2}, $$
$$ \omega_z = \frac{1}{r}\left[\frac{Mc\sin\theta}{r^2} - \frac{Mc\sin\theta}{r^2}\right] = \boxed{\,0.\,} $$
The motion is irrotational, as it must be for $\mathbf{v} = \nabla\varphi$ ($\nabla\wedge\nabla\varphi \equiv 0$).

### 3.4 Acceleration of the particle initially at $r = 1$, $\theta = \pi/2$

Why this tool: the acceleration is the material derivative of the velocity (Eq. 2.25). Because $\boldsymbol{\omega} = 0$, Eq. (2.26) reduces to $\mathbf{a} = \partial_t\mathbf{v} + \nabla(\lvert\mathbf{v}\rvert^2/2)$, which is valid in polar coordinates.

Local term, using $\partial_t c = -\Omega\sin\Omega t$:
$$ \frac{\partial v_r}{\partial t} = \frac{M\Omega\sin\Omega t\cos\theta}{r^2}, \qquad \frac{\partial v_\theta}{\partial t} = \frac{M\Omega\sin\Omega t\sin\theta}{r^2}. $$
Convective term: $\lvert\mathbf{v}\rvert^2 = v_r^2 + v_\theta^2 = \dfrac{M^2c^2\left(\cos^2\theta + \sin^2\theta\right)}{r^4} = \dfrac{M^2c^2}{r^4}$, hence
$$ \frac{\lvert\mathbf{v}\rvert^2}{2} = \frac{M^2c^2}{2r^4}, \qquad \frac{\partial}{\partial r}\left(\frac{\lvert\mathbf{v}\rvert^2}{2}\right) = -\frac{2M^2c^2}{r^5}, \qquad \frac{1}{r}\frac{\partial}{\partial\theta}\left(\frac{\lvert\mathbf{v}\rvert^2}{2}\right) = 0. $$
Field acceleration:
$$ a_r = \frac{M\Omega\sin\Omega t\cos\theta}{r^2} - \frac{2M^2\cos^2\Omega t}{r^5}, \qquad a_\theta = \frac{M\Omega\sin\Omega t\sin\theta}{r^2}. $$
Evaluate at $r = 1$, $\theta = \pi/2$ ($\cos\theta = 0$, $\sin\theta = 1$):
$$ \boxed{\,\mathbf{a}(1,\tfrac{\pi}{2},t) = -2M^2\cos^2(\Omega t)\,\mathbf{e}_r + M\Omega\sin(\Omega t)\,\mathbf{e}_\theta.\,} $$
This is the acceleration of whichever particle occupies the point $(1,\pi/2)$ at time $t$. For the particle that is at that point at the initial instant, set $t = 0$: $\mathbf{a} = -2M^2\mathbf{e}_r$ (the local term vanishes because $\sin 0 = 0$). For $t > 0$ that particle has moved away from the point, so its acceleration is the field value at its new position (part 7).

### 3.5 Initial circulation around the circle of radius $1/2$ centred at $(r = 1, \theta = \pi/2)$

Why this tool: $\Gamma = \oint\mathbf{v}\cdot d\mathbf{l}$ (Eq. 2.29) equals the flux of the vorticity through any surface bounded by the curve that lies in the fluid (Eq. 2.32). The centre is at Cartesian $(0, 1)$ and the circle has radius $1/2$, so every point of the disc is at a distance of at least $1/2$ from the origin: the disc lies entirely inside the domain, where $\omega_z = 0$.
$$ \Gamma = \iint_S\omega_z\,d\sigma = \iint_S 0\,d\sigma = \boxed{\,0\,} $$
at $t = 0$ and, since $\omega_z = 0$ for all $t$, at every instant. In fact $\varphi$ is single-valued, so $\oint\nabla\varphi\cdot d\mathbf{l} = \varphi(\text{end}) - \varphi(\text{start}) = 0$ for every closed curve, including those that enclose the origin.

### 3.6 Streamlines

Why this tool: streamlines are tangent to $\mathbf{v}$ at a frozen instant (Eq. 2.21): $dr/v_r = r\,d\theta/v_\theta$. At an instant with $\cos\Omega t \neq 0$ the common factor $-Mc/r^2$ cancels:
$$ \frac{dr}{\cos\theta} = \frac{r\,d\theta}{\sin\theta} \;\Longrightarrow\; \frac{dr}{r} = \frac{\cos\theta}{\sin\theta}\,d\theta \;\Longrightarrow\; \ln\frac{r}{r_0} = \ln\left\lvert\frac{\sin\theta}{\sin\theta_0}\right\rvert, $$
$$ \boxed{\,r = \frac{r_0}{\sin\theta_0}\sin\theta = C\sin\theta.\,} $$
In Cartesian variables $r^2 = Cr\sin\theta$ gives $x^2 + y^2 = Cy$: circles of diameter $C$ centred at $(0, C/2)$ and tangent to the $x$-axis at the origin. The shape does not depend on $t$. (At the isolated instants with $\cos\Omega t = 0$ the whole velocity field vanishes.) Equivalent form: the stream function $\psi = -Mc\sin\theta/r$ (with $v_r = r^{-1}\partial_\theta\psi$, $v_\theta = -\partial_r\psi$) has the level curves $\sin\theta/r = $ const.

### 3.7 Trajectories and particle paths

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12), here
$$ \frac{dr}{dt} = -\frac{Mc\cos\theta}{r^2}, \qquad r\frac{d\theta}{dt} = -\frac{Mc\sin\theta}{r^2}, \qquad r(0) = r_0,\ \theta(0) = \theta_0. $$
Dividing the first equation by the second eliminates both $t$ and the factor $c(t)$:
$$ \frac{dr}{r\,d\theta} = \frac{\cos\theta}{\sin\theta} \;\Longrightarrow\; \boxed{\,r = r_0\frac{\sin\theta}{\sin\theta_0}\,} $$
which is the path line. It coincides with the streamlines of 3.6 because the direction of $\mathbf{v}$ does not depend on time (only its magnitude does).

Time law. Substitute the path into the second equation, $r^3 = r_0^3\sin^3\theta/\sin^3\theta_0$:
$$ \frac{d\theta}{dt} = -\frac{Mc\sin\theta}{r^3} = -\frac{M\sin^3\theta_0}{r_0^3}\,\frac{\cos\Omega t}{\sin^2\theta} \;\Longrightarrow\; \sin^2\theta\,d\theta = -\frac{M\sin^3\theta_0}{r_0^3}\cos\Omega t\,dt. $$
Integrate with Barrow's rule between $(\theta_0, 0)$ and $(\theta, t)$. For the left side use $\sin^2\theta' = (1 - \cos 2\theta')/2$, whose primitive is $\theta'/2 - \sin 2\theta'/4$; for the right side, $\int_0^t\cos\Omega t'\,dt' = \sin(\Omega t)/\Omega$:
$$ \boxed{\,\frac{\theta - \theta_0}{2} - \frac{\sin 2\theta - \sin 2\theta_0}{4} = -\frac{M\sin^3\theta_0}{r_0^3\,\Omega}\sin\Omega t.\,} $$
Together with $r = r_0\sin\theta/\sin\theta_0$ this defines $\mathbf{x}(t)$ implicitly. The right-hand side vanishes whenever $\sin\Omega t = 0$, so the particle returns to its starting point every half period $\pi/\Omega$: it oscillates back and forth along its circular path. (Particles on the axis $\theta_0 = 0$ or $\pi$ stay on it, with $r^3 = r_0^3 \mp 3(M/\Omega)\sin\Omega t$.)

## Phase 4: Interpretation, Limits and Dimensional Check

- The flow is the oscillating field of a point dipole: incompressible, irrotational, with streamlines that are circles through the singular point and a velocity that decays as $r^{-2}$.
- Steady limit $\Omega \to 0$ (with $c \to 1$): the local term vanishes and the acceleration is purely convective, $a_r = -2M^2/r^5$ and $a_\theta = 0$, equal to $\nabla(\lvert\mathbf{v}\rvert^2/2)$; the particle then drifts monotonically along the circle.
- Consistency of the answers: part 5 ($\Gamma = 0$) follows from part 3 ($\omega_z = 0$); part 7 reproduces part 6 geometrically.
- Dimensions (SI): $[v] = [M/r^2] = (\text{m}^3/\text{s})/\text{m}^2 = \text{m/s}$; $[a] = [M^2/r^5] = (\text{m}^6/\text{s}^2)/\text{m}^5 = \text{m/s}^2$ and $[M\Omega/r^2] = (\text{m}^3/\text{s})(1/\text{s})/\text{m}^2 = \text{m/s}^2$; the combination $M/(r_0^3\Omega)$ in 3.7 is $(\text{m}^3/\text{s})/(\text{m}^3/\text{s}) = 1$, dimensionless as required for an angle.
- Numerical cross-check: symbolic differentiation of $\varphi$ gives $\nabla\cdot\mathbf{v} = 0$, $\omega_z = 0$ and, from the full material derivative in polar components (including the $-v_\theta^2/r$ and $v_rv_\theta/r$ terms), the same $a_r$, $a_\theta$ as above, in particular $\mathbf{a}(1,\pi/2,t) = -2M^2\cos^2\Omega t\,\mathbf{e}_r + M\Omega\sin\Omega t\,\mathbf{e}_\theta$. RK4 integration of the particle ODE with $M = 0.8$ m$^3$/s, $\Omega = 1.7$ s$^{-1}$, $r_0 = 1$ m, $\theta_0 = 0.45\pi$ up to $t = 1.3$ s gives $r = 0.846496$ m, equal to $r_0\sin\theta/\sin\theta_0$ at the integrated angle, and the two sides of the boxed time law, $-0.363902$ and $-0.363902$.

> [!note] Reading of the official handwritten solution
> K5.pdf evaluates the acceleration at the field point $(1,\pi/2)$ for general $t$, obtaining the vector given in 3.4; the value for the particle that is there at $t=0$ is its $t=0$ value. The handwritten trajectory law agrees with the boxed relation in 3.7 and notes that streamlines and path lines coincide. No numerical discrepancy was found.
