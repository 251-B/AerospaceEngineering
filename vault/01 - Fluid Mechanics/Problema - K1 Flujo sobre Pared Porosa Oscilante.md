---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - pared-porosa
  - stokes
dificultad: alta
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K1.pdf"
---

# Problem K1: Flow over an Oscillating Porous Wall with Transverse Blowing

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|Eulerian vs Lagrangian description and flow lines]], [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity, circulation and potential]], [[Concepto - Flujo Convectivo y Funcion de Corriente|convective flux and stream function]].

## Statement

A fluid is blown with velocity $V$ through a horizontal porous wall that is oscillating in its plane with velocity $U \cos(\Omega t)$. The resulting fluid velocity for $0 < y < \infty$ is given by (approximately)

$$ v_x = U e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right), \qquad v_y = V, $$

where the characteristic thickness $\delta = (2\nu/\Omega)^{1/2}$ depends on the kinematic viscosity of the fluid $\nu$.

1. Determine the trajectory and path of a fluid particle initially located at $x = 0$ and $y = 0$.
2. Obtain the streamline that intersects the point $x = 0$ and $y = 0$.
3. Compute the vorticity $\nabla \wedge \vec{v}$. If $\nabla \wedge \vec{v} = 0$, obtain also the velocity potential.
4. Calculate the rate of expansion $\nabla \cdot \vec{v}$. If $\nabla \cdot \vec{v} = 0$, obtain also the stream function.
5. Equation of the fluid line formed by the fluid particles initially located along the vertical axis $x = 0$.
6. Determine the volume flux crossing the plane $x = 0$ as a function of time $Q(t)$ along with its average value $Q_a = \int_t^{t+2\pi/\Omega} Q\,dt$.
7. Obtain the volume flux leaving the sphere of radius $R$ centered at $x = 0$ and $y = 2R$.
8. Compute the circulation around a square of side $L$ whose base lies parallel to the wall at a distance $y = L/2$. Redo the computation making use of Stokes theorem.

Source: K1.pdf (page 1). Notes.pdf, Chapter 2: trajectories and path lines Eqs. (2.10)-(2.15), fluid lines Eqs. (2.16)-(2.17), stream lines Eq. (2.21), circulation and Stokes theorem Eqs. (2.29)-(2.33), potential Eq. (2.34), convective flux Eqs. (2.35)-(2.38), stream function Eqs. (2.40)-(2.45).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- The motion is planar: the velocity has components $(v_x, v_y)$ that depend only on $y$ and $t$. The only spatial degree of freedom of the field is $y$; the flow is unsteady with the single time scale $\Omega^{-1}$.
- The field is given as an approximation to a viscous (Stokes-layer) solution; here it is treated as a prescribed kinematic field and no dynamics are used.
- The fluid occupies $0 < y < \infty$. At the wall, $v_x(y=0) = U\cos\Omega t$ equals the wall velocity and $v_y = V$ is the blowing velocity.
- We assume $V \neq 0$ (transverse blowing) and $\Omega > 0$, so that $\delta$ is real and positive.
- Fluxes and the circulation are computed per unit length in the direction $z$ normal to the plane of the motion.

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $U$ | amplitude of the wall velocity | m/s |
| $V$ | blowing velocity (uniform, along $y$) | m/s |
| $\Omega$ | angular frequency of the wall oscillation | s$^{-1}$ |
| $\nu$ | kinematic viscosity | m$^2$/s |
| $\delta = (2\nu/\Omega)^{1/2}$ | thickness of the oscillatory layer | m |
| $L$, $R$ | side of the square and radius of the sphere | m |
| $Q(t)$ | volume flux per unit depth through $x=0$ | m$^2$/s |
| $\Gamma$ | circulation | m$^2$/s |

Dimensional check of $\delta$: $[\nu/\Omega] = (\text{m}^2/\text{s})/(1/\text{s}) = \text{m}^2$, so $\delta$ is a length.

## Phase 2: Coordinates, Frames and Changes of Variable

- Frame of observation: inertial laboratory frame, Cartesian basis $(\mathbf{e}_x, \mathbf{e}_y, \mathbf{e}_z)$, with $x$ along the wall, $y$ normal to it and $\mathbf{e}_z = \mathbf{e}_x \wedge \mathbf{e}_y$. The wall oscillates in this frame; the velocity field given in the statement is the laboratory-frame field.
- Eulerian variables: $(x, y, t)$. Lagrangian label of a particle: its position $(x_0, y_0)$ at $t = 0$.
- Phase variable used throughout: $\Theta(y,t) \equiv \Omega t - y/\delta$, so that $v_x = U e^{-y/\delta}\cos\Theta$.
- Change of variable along a particle: since $v_y = V$ is constant, $y(t) = y_0 + Vt$, hence $t = (y - y_0)/V$. This trades time for $y$ when the path line is required.
- Abbreviations: $b \equiv \Omega - V/\delta$ and $D \equiv (V/\delta)^2 + b^2$ (so $D > 0$ because $V \neq 0$).

> [!info] Why a lemma is needed
> Parts 1, 2, 5 and 6 require primitives of an exponential times a cosine. Instead of quoting a table, the primitive is proved once. For constants $a$, $\beta$, $c$ with $a^2 + \beta^2 \neq 0$,
> $$ \int e^{as}\cos(\beta s + c)\,ds = \frac{e^{as}}{a^2 + \beta^2}\left[a\cos(\beta s+c) + \beta\sin(\beta s+c)\right] + C. \tag{L} $$
> Proof by differentiation: $\dfrac{d}{ds}\left\{e^{as}\left[a\cos(\beta s+c) + \beta\sin(\beta s+c)\right]\right\} = e^{as}\left[a^2\cos + a\beta\sin - a\beta\sin + \beta^2\cos\right] = (a^2+\beta^2)\,e^{as}\cos(\beta s+c)$.

## Phase 3: Step-by-Step Derivation

### 3.1 Trajectory and path line of the particle starting at the origin

Why this tool: a trajectory is the solution of $d\mathbf{x}/dt = \mathbf{v}(\mathbf{x},t)$ with $\mathbf{x}(0) = \mathbf{x}_0$ (Notes Eq. 2.12); the path line is the curve in space obtained by eliminating $t$ (Eq. 2.15). The system is triangular: $v_y$ does not depend on $x$, so $y(t)$ is found first.

Vertical motion:
$$ \frac{dy}{dt} = V \;\Longrightarrow\; \int_0^{y} dy' = \int_0^{t} V\,dt' \;\Longrightarrow\; y(t) = Vt. $$

Along this particle, $e^{-y/\delta} = e^{-Vt/\delta}$ and $\Theta = \Omega t - Vt/\delta = bt$. Therefore
$$ \frac{dx}{dt} = U e^{-Vt/\delta}\cos(bt). $$
Apply (L) with $s = t'$, $a = -V/\delta$, $\beta = b$, $c = 0$, and Barrow's rule between the limits $t' = 0$ and $t' = t$:
$$ x(t) = U\left[\frac{e^{-Vt'/\delta}}{D}\left(-\frac{V}{\delta}\cos bt' + b\sin bt'\right)\right]_{t'=0}^{t'=t}. $$
Upper limit: $\dfrac{e^{-Vt/\delta}}{D}\left(-\dfrac{V}{\delta}\cos bt + b\sin bt\right)$. Lower limit: $\dfrac{1}{D}\left(-\dfrac{V}{\delta}\cdot 1 + b\cdot 0\right) = -\dfrac{V}{\delta D}$. Subtracting,
$$ \boxed{\,x(t) = \frac{U}{D}\left[e^{-Vt/\delta}\left(-\frac{V}{\delta}\cos bt + b\sin bt\right) + \frac{V}{\delta}\right],\qquad y(t) = Vt.\,} $$
Path line: substitute $t = y/V$, so that $bt = (\Omega/V - 1/\delta)\,y$:
$$ x(y) = \frac{U}{D}\left[e^{-y/\delta}\left(-\frac{V}{\delta}\cos\!\left[\left(\frac{\Omega}{V} - \frac{1}{\delta}\right)y\right] + b\sin\!\left[\left(\frac{\Omega}{V} - \frac{1}{\delta}\right)y\right]\right) + \frac{V}{\delta}\right]. $$
The trajectory carries the time law; the path line is a damped oscillation of the horizontal displacement versus height.

### 3.2 Streamline through the origin

Why this tool: a streamline is tangent to $\mathbf{v}$ at a frozen instant (Notes Eq. 2.21), so $t$ is a parameter and not an integration variable. With $t$ frozen:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \;\Longrightarrow\; \frac{dx}{dy} = \frac{U}{V}e^{-y/\delta}\cos\left(\Omega t - \frac{y}{\delta}\right). $$
Apply (L) with $s = y'$, $a = -1/\delta$, $\beta = -1/\delta$, $c = \Omega t$; here $a^2 + \beta^2 = 2/\delta^2$:
$$ \int e^{-y'/\delta}\cos\Theta\,dy' = \frac{e^{-y'/\delta}}{2/\delta^2}\left[-\frac{1}{\delta}\cos\Theta - \frac{1}{\delta}\sin\Theta\right] = -\frac{\delta}{2}e^{-y'/\delta}\left(\cos\Theta + \sin\Theta\right), \qquad \Theta = \Omega t - \frac{y'}{\delta}. $$
Barrow's rule between $y' = 0$ (where $x = 0$ and $\Theta = \Omega t$) and $y' = y$:
$$ \boxed{\,x(y,t) = \frac{U\delta}{2V}\left[\cos\Omega t + \sin\Omega t - e^{-y/\delta}\left(\cos\Theta + \sin\Theta\right)\right],\quad \Theta = \Omega t - \frac{y}{\delta}.\,} $$
Check by differentiation, using $\partial\Theta/\partial y = -1/\delta$: $\partial_y(\cos\Theta + \sin\Theta) = (\sin\Theta - \cos\Theta)/\delta$, so $\partial_y\left[e^{-y/\delta}(\cos\Theta+\sin\Theta)\right] = -\tfrac{1}{\delta}e^{-y/\delta}\left[(\cos\Theta+\sin\Theta) + (\cos\Theta - \sin\Theta)\right] = -\tfrac{2}{\delta}e^{-y/\delta}\cos\Theta$, hence $dx/dy = (U/V)e^{-y/\delta}\cos\Theta$ as required.

### 3.3 Vorticity and velocity potential

Why this tool: vorticity $\boldsymbol{\omega} = \nabla\wedge\mathbf{v}$ measures twice the local angular velocity (Notes Eq. 2.52); a velocity potential $\mathbf{v} = \nabla\varphi$ (Eq. 2.34) exists only when $\boldsymbol{\omega} \equiv 0$ in a simply connected domain.
$$ \omega_z = \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} = 0 - \frac{\partial v_x}{\partial y}. $$
Chain rule, using $\partial_y e^{-y/\delta} = -e^{-y/\delta}/\delta$ and $\partial_y\cos\Theta = -\sin\Theta\,\partial_y\Theta = \sin\Theta/\delta$:
$$ \frac{\partial v_x}{\partial y} = U e^{-y/\delta}\left[-\frac{1}{\delta}\cos\Theta + \frac{1}{\delta}\sin\Theta\right] \;\Longrightarrow\; \boxed{\,\omega_z = \frac{U}{\delta}e^{-y/\delta}\left(\cos\Theta - \sin\Theta\right)\neq 0.\,} $$
For example, at $y = 0$ and $t = 0$: $\omega_z = U/\delta \neq 0$. The flow is rotational, so no velocity potential exists.

### 3.4 Rate of expansion and stream function

Why this tool: $\nabla\cdot\mathbf{v}$ is the rate of change of volume per unit volume (Notes Eqs. 2.62-2.63). If it vanishes, a planar field admits a stream function with $v_x = \partial_y\psi$, $v_y = -\partial_x\psi$ (Eq. 2.41), whose level lines are stream lines (Eq. 2.42).
$$ \nabla\cdot\mathbf{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} = 0 + 0 = 0. $$
Integrate $v_y = -\partial_x\psi = V$ with respect to $x$: $\psi = -Vx + f(y,t)$. Then $\partial_y\psi = f'(y,t) = v_x$, and by the primitive of 3.2,
$$ f(y,t) = U\int e^{-y/\delta}\cos\Theta\,dy = -\frac{U\delta}{2}e^{-y/\delta}\left(\cos\Theta + \sin\Theta\right) + \psi_0(t), $$
$$ \boxed{\,\psi(x,y,t) = -Vx - \frac{U\delta}{2}e^{-y/\delta}\left(\cos\Theta + \sin\Theta\right) + \psi_0(t).\,} $$
Check: $-\partial_x\psi = V$ and $\partial_y\psi = U e^{-y/\delta}\cos\Theta = v_x$. Consistency with 3.2: along the curve of 3.2, $\psi - \psi_0 = -Vx(y,t) - \tfrac{U\delta}{2}e^{-y/\delta}(\cos\Theta+\sin\Theta) = -\tfrac{U\delta}{2}(\cos\Omega t + \sin\Omega t)$, independent of $y$, so that curve is a level set $\psi = $ const.

### 3.5 Fluid line initially on the axis $x = 0$

Why this tool: a fluid line is made of particles, so it is obtained by writing the trajectories (Eq. 2.17) of all particles of the initial curve $\mathbf{x}_l(\lambda) = (0, \lambda)$ and then eliminating the label $\lambda$.

Particle $\lambda$: $y = \lambda + Vt'$ and $\Theta = \Omega t' - (\lambda + Vt')/\delta = bt' - \lambda/\delta$, so
$$ \frac{dx}{dt'} = U e^{-\lambda/\delta}e^{-Vt'/\delta}\cos\left(bt' - \frac{\lambda}{\delta}\right). $$
Lemma (L) with $a = -V/\delta$, $\beta = b$, $c = -\lambda/\delta$ and Barrow's rule between $t' = 0$ and $t' = t$:
$$ x(\lambda,t) = \frac{U e^{-\lambda/\delta}}{D}\left\{e^{-Vt/\delta}\left[-\frac{V}{\delta}\cos\left(bt - \frac{\lambda}{\delta}\right) + b\sin\left(bt - \frac{\lambda}{\delta}\right)\right] - \left[-\frac{V}{\delta}\cos\frac{\lambda}{\delta} - b\sin\frac{\lambda}{\delta}\right]\right\}, $$
where the lower limit used that cosine is even and sine is odd. Now eliminate $\lambda = y - Vt$ (the change of variable from label to current height). Then $e^{-\lambda/\delta}e^{-Vt/\delta} = e^{-y/\delta}$, $e^{-\lambda/\delta} = e^{-(y-Vt)/\delta}$ and $bt - \lambda/\delta = \Omega t - y/\delta = \Theta$:
$$ \boxed{\,x(y,t) = -\frac{U e^{-y/\delta}}{D}\left[\frac{V}{\delta}\cos\Theta - b\sin\Theta\right] + \frac{U e^{-(y-Vt)/\delta}}{D}\left[\frac{V}{\delta}\cos\frac{y - Vt}{\delta} + b\sin\frac{y - Vt}{\delta}\right]\,} $$
with $\Theta = \Omega t - y/\delta$, $b = \Omega - V/\delta$, $D = (V/\delta)^2 + b^2$, valid for $y \ge Vt$ (the particles with $\lambda \ge 0$). At $t = 0$ it reduces to $x = 0$.

### 3.6 Volume flux through the plane $x = 0$

Why this tool: the volume flux through a fixed surface is $\int\mathbf{v}\cdot\mathbf{n}\,d\sigma$ (Eq. 2.36). The plane $x = 0$ has normal $\mathbf{e}_x$, so only $v_x$ crosses it; per unit depth, $d\sigma = dy$.
$$ Q(t) = \int_0^\infty v_x(0,y,t)\,dy = U\left[-\frac{\delta}{2}e^{-y/\delta}\left(\cos\Theta + \sin\Theta\right)\right]_{y=0}^{y=\infty}. $$
At the upper limit the exponential vanishes; at $y = 0$, $\Theta = \Omega t$:
$$ \boxed{\,Q(t) = \frac{U\delta}{2}\left(\cos\Omega t + \sin\Omega t\right) = \frac{U\delta}{\sqrt{2}}\cos\left(\Omega t - \frac{\pi}{4}\right).\,} $$
Integral over one period, as written in the statement, with the primitive $\int(\cos\Omega t' + \sin\Omega t')\,dt' = (\sin\Omega t' - \cos\Omega t')/\Omega$ and Barrow's rule:
$$ \int_t^{t+2\pi/\Omega}Q\,dt' = \frac{U\delta}{2\Omega}\left[\sin\Omega t' - \cos\Omega t'\right]_{t}^{t+2\pi/\Omega} = \frac{U\delta}{2\Omega}\left[(\sin\Omega t - \cos\Omega t) - (\sin\Omega t - \cos\Omega t)\right] = 0, $$
because $\Omega(t + 2\pi/\Omega) = \Omega t + 2\pi$. The time average (that integral divided by the period $2\pi/\Omega$) is also $0$: there is no net volume transported through $x = 0$ over a cycle.

### 3.7 Flux leaving the sphere of radius $R$ centred at $(0, 2R)$

Why this tool: for a closed surface the flux is turned into a volume integral by Gauss' formula (Eq. 2.37). The sphere (a body in the planar flow extended uniformly in $z$) has lowest point at $y = 2R - R = R > 0$, so it lies entirely inside the fluid domain $y > 0$ and the field is smooth in it.
$$ \oint_\Sigma\mathbf{v}\cdot\mathbf{n}\,d\sigma = \int_{V_\Sigma}\nabla\cdot\mathbf{v}\,dV = \int_{V_\Sigma}0\,dV = 0. $$
Independent check by symmetry: $v_x$ depends on $y$ only, so it is even under $x \to -x$ while $n_x$ is odd, and $\oint v_x n_x\,d\sigma = 0$; the uniform $V\mathbf{e}_y$ gives $V\oint n_y\,d\sigma = 0$ for any closed surface. Result: $\boxed{\,0\,}$.

### 3.8 Circulation around the square

Why this tool: the circulation is $\Gamma = \oint\mathbf{v}\cdot d\mathbf{l}$ (Eq. 2.29); by Stokes (Eq. 2.32) it equals the flux of $\omega_z$ through the enclosed area provided the area lies inside the fluid. The square has vertices $(x_1, L/2)$, $(x_1+L, L/2)$, $(x_1+L, 3L/2)$, $(x_1, 3L/2)$ and is traversed counter-clockwise (normal $+\mathbf{e}_z$).

Line integral, side by side:

- bottom ($y = L/2$, $dx > 0$): $\int_{x_1}^{x_1+L}v_x\,dx = L\,v_x(L/2)$;
- right side ($x = x_1 + L$, $dy > 0$): $\int_{L/2}^{3L/2}V\,dy = VL$;
- top ($y = 3L/2$, $dx < 0$): $-L\,v_x(3L/2)$;
- left side ($dy < 0$): $-VL$.

The vertical contributions cancel, hence
$$ \boxed{\,\Gamma = UL\left[e^{-L/2\delta}\cos\left(\Omega t - \frac{L}{2\delta}\right) - e^{-3L/2\delta}\cos\left(\Omega t - \frac{3L}{2\delta}\right)\right].\,} $$
Stokes theorem:
$$ \Gamma = \int_{x_1}^{x_1+L}\int_{L/2}^{3L/2}\omega_z\,dy\,dx = L\int_{L/2}^{3L/2}\left(-\frac{\partial v_x}{\partial y}\right)dy = -L\left[v_x\right]_{y=L/2}^{y=3L/2} = L\left[v_x\!\left(\tfrac{L}{2}\right) - v_x\!\left(\tfrac{3L}{2}\right)\right], $$
which is the same expression.

## Phase 4: Interpretation, Limits and Dimensional Check

- Wall limit: at $y = 0$, $v_x = U\cos\Omega t$ (the wall velocity) and the oscillation decays as $e^{-y/\delta}$, with a phase lag $y/\delta$. For $y \gg \delta$ the fluid has no motion in $x$ and only the uniform blowing $V$ remains.
- Limit $V \to 0$ in 3.1: $D \to \Omega^2$, $b \to \Omega$ and $x(t) \to (U/\Omega)\sin\Omega t$, the displacement of the wall itself, as expected for a particle that stays on the wall.
- Limit $V \to 0$ in 3.2: $x \propto 1/V \to \infty$, i.e. the streamlines become parallel to the wall, consistent with $v_y \to 0$.
- The flow is incompressible and rotational; it has a stream function but no potential, as found in 3.3 and 3.4. The zero net flux in 3.7 and the zero cycle integral in 3.6 follow from this solenoidal, periodic character.
- Dimensions (SI): $[x(t)] = [U/D]\,[V/\delta] = (\text{m/s})(\text{s}^2)(\text{s}^{-1}) = \text{m}$. $[\omega_z] = [U/\delta] = \text{s}^{-1}$. $[\psi] = [Vx] = [U\delta] = \text{m}^2/\text{s}$. $[Q] = [U\delta] = \text{m}^2/\text{s}$ per unit depth. $[\Gamma] = [UL] = \text{m}^2/\text{s}$.
- Numerical cross-check (quadrature of the defining integral against the closed form), with $U = 1.3$ m/s, $V = 0.7$ m/s, $\delta = 0.9$ m, $\Omega = 2.1$ s$^{-1}$, $t = 1.7$ s: path $x(t) = 0.653175$ m (both); streamline at $y = 0.8$ m, $x = -0.952255$ m (both); fluid line at $y = 0.8$ m, $x = 0.420088$ m, and at $y = 2.5$ m, $x = 0.194357$ m (both); $Q = -0.775155$ m$^2$/s (both); for $L = 0.6$ m, $\Gamma = -0.315037$ m$^2$/s from the line integral, from the closed form and from the Stokes integral.

> [!warning] Reading of the official handwritten solution
> In K1.pdf the first bracket of part 5 is written $\tfrac{V}{\delta}\cos[\cdot] - (\Omega - \tfrac{V}{\delta})\sin[\cdot]$ and, as legible in the scan, the argument of that sine shows $y$ where $t$ is meant. The expression above is the result of the explicit Barrow derivation. The statement of part 6 defines $Q_a$ as the bare integral over one period (no factor $\Omega/2\pi$); the handwritten answer is $0$, which agrees with the integral computed above, and the mean value is also $0$.
