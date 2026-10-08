---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - dipolo
  - polares
  - linea-fluida
  - aceleracion
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K9.pdf"
---

# Problem K9: Oscillating Polar Flow (Planar Dipole)

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Derivada Material y Aceleracion del Fluido|acceleration]], [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity and potential]], [[Concepto - Flujo Convectivo y Funcion de Corriente|stream function]], [[Concepto - Descripcion Euleriana vs Lagrangiana y Lineas de Flujo|fluid lines]].

## Statement

For the planar velocity field

$$ v_r = -A\sin(\Omega t)\,\frac{\sin\theta}{r^2}, \qquad v_\theta = A\sin(\Omega t)\,\frac{\cos\theta}{r^2}, $$

where $A$ and $\Omega$ are known constants,

1. Determine the vorticity.
2. Compute the expansion rate.
3. Comment on the existence of velocity potential and stream function and, if they do exist, compute them.
4. Find the acceleration for points along the line $\theta = 0$.
5. Obtain the trajectories and streamlines.
6. Determine the fluid line that at $t = 0$ is given by $\theta = 0$ and $0 < r < \infty$.

Source: K9.pdf (page 1). Notes.pdf, Chapter 2: curl and divergence in orthogonal coordinates Eqs. (2.5)-(2.6); potential Eq. (2.34); acceleration Eqs. (2.25)-(2.26); stream function Eqs. (2.40)-(2.45); trajectories Eq. (2.12); fluid lines Eqs. (2.16)-(2.17); stream lines Eq. (2.21).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar, unsteady flow in the plane $(r,\theta)$, for $r > 0$; the origin is singular and excluded. Write $\sigma(t) \equiv \sin\Omega t$; the velocity is the product of the time function $\sigma$ and a steady spatial field. Both components decay as $r^{-2}$.
- Degrees of freedom: $(r,\theta)$ and time.
- Units: $v = A/r^2$ has units m/s, so $A$ has units m$^3$/s.
- Hypothesis used in part 6: $A > 0$, $\Omega > 0$, and the time interval is such that the particle does not reach the singular point (discussed in Phase 4).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A$ | dipole strength (per unit depth) | m$^3$/s |
| $\Omega$ | angular frequency | s$^{-1}$ |
| $(r_0,\theta_0)$ | initial position of a particle | m, rad |
| $\lambda$ | material label, $r_0 = \lambda$ on the line $\theta_0 = 0$ | m |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame with the singular point at the origin; polar coordinates $(r,\theta)$, scale factors $(1,r)$, $x = r\cos\theta$, $y = r\sin\theta$, $\mathbf{e}_z = \mathbf{e}_r\wedge\mathbf{e}_\theta$.
- Operators (Eqs. 2.3, 2.5, 2.6): $\nabla\varphi = \partial_r\varphi\,\mathbf{e}_r + r^{-1}\partial_\theta\varphi\,\mathbf{e}_\theta$, $\nabla\cdot\mathbf{v} = r^{-1}\left[\partial_r(rv_r) + \partial_\theta v_\theta\right]$, $\omega_z = r^{-1}\left[\partial_r(rv_\theta) - \partial_\theta v_r\right]$.
- Stream function in polar coordinates. In Cartesian variables $v_x = \partial_y\psi$, $v_y = -\partial_x\psi$ (Eq. 2.41). Projecting on the polar basis, $v_r = v_x\cos\theta + v_y\sin\theta = \cos\theta\,\partial_y\psi - \sin\theta\,\partial_x\psi = r^{-1}\partial_\theta\psi$ and $v_\theta = -v_x\sin\theta + v_y\cos\theta = -\left(\sin\theta\,\partial_y\psi + \cos\theta\,\partial_x\psi\right) = -\partial_r\psi$, using $\partial_\theta = -r\sin\theta\,\partial_x + r\cos\theta\,\partial_y$ and $\partial_r = \cos\theta\,\partial_x + \sin\theta\,\partial_y$. Hence $v_r = r^{-1}\partial_\theta\psi$, $v_\theta = -\partial_r\psi$.
- For the acceleration, the coordinate-free form of Eq. (2.26) is used, since the Cartesian component form of Eq. (2.27) does not hold in polar coordinates.
- Material variables: initial position $(r_0,\theta_0)$ at $t = 0$.

## Phase 3: Step-by-Step Derivation

### 3.1 Vorticity

Why this tool: $\omega_z = r^{-1}\left[\partial_r(rv_\theta) - \partial_\theta v_r\right]$ is twice the angular velocity of the fluid element (Eq. 2.52).
$$ r\,v_\theta = \frac{A\sigma\cos\theta}{r} \Rightarrow \frac{\partial(rv_\theta)}{\partial r} = -\frac{A\sigma\cos\theta}{r^2}, \qquad \frac{\partial v_r}{\partial\theta} = -\frac{A\sigma\cos\theta}{r^2}, $$
$$ \omega_z = \frac{1}{r}\left[-\frac{A\sigma\cos\theta}{r^2} + \frac{A\sigma\cos\theta}{r^2}\right] = \boxed{\,0.\,} $$

### 3.2 Expansion rate

Why this tool: $\nabla\cdot\mathbf{v}$ is the rate of volume change per unit volume (Eqs. 2.62-2.63).
$$ r\,v_r = -\frac{A\sigma\sin\theta}{r} \Rightarrow \frac{\partial(rv_r)}{\partial r} = \frac{A\sigma\sin\theta}{r^2}, \qquad \frac{\partial v_\theta}{\partial\theta} = -\frac{A\sigma\sin\theta}{r^2}, $$
$$ \nabla\cdot\mathbf{v} = \frac{1}{r}\left[\frac{A\sigma\sin\theta}{r^2} - \frac{A\sigma\sin\theta}{r^2}\right] = \boxed{\,0.\,} $$

### 3.3 Existence of potential and stream function

Because $\nabla\wedge\mathbf{v} = 0$ (3.1) in the region $r > 0$, a velocity potential exists (Eq. 2.34): $\mathbf{v} = \nabla\varphi$. Because the planar flow is also solenoidal (3.2), a stream function exists (Eq. 2.41). Both are single-valued here: the circulation around the origin is $\oint v_\theta\,r\,d\theta = A\sigma\int_0^{2\pi}\cos\theta\,d\theta/r = 0$ and the flux through a circle $\oint v_r\,r\,d\theta = -A\sigma\int_0^{2\pi}\sin\theta\,d\theta/r = 0$.

Potential. From $v_r = \partial_r\varphi = -A\sigma\sin\theta/r^2$, integrate in $r$ (primitive of $r^{-2}$ is $-r^{-1}$): $\varphi = A\sigma\sin\theta/r + f(\theta,t)$. Then
$$ v_\theta = \frac{1}{r}\frac{\partial\varphi}{\partial\theta} = \frac{A\sigma\cos\theta}{r^2} + \frac{1}{r}\frac{\partial f}{\partial\theta} = \frac{A\sigma\cos\theta}{r^2} \;\Longrightarrow\; \frac{\partial f}{\partial\theta} = 0, $$
$$ \boxed{\,\varphi = \frac{A\sin(\Omega t)\sin\theta}{r} + \varphi_0(t) = A\sin(\Omega t)\,\frac{y}{x^2+y^2} + \varphi_0(t).\,} $$
Stream function. From $r\,v_r = \partial_\theta\psi = -A\sigma\sin\theta/r$, integrate in $\theta$: $\psi = A\sigma\cos\theta/r + g(r,t)$. Then
$$ v_\theta = -\frac{\partial\psi}{\partial r} = \frac{A\sigma\cos\theta}{r^2} - \frac{\partial g}{\partial r} = \frac{A\sigma\cos\theta}{r^2} \;\Longrightarrow\; \frac{\partial g}{\partial r} = 0, $$
$$ \boxed{\,\psi = \frac{A\sin(\Omega t)\cos\theta}{r} + \psi_0(t) = A\sin(\Omega t)\,\frac{x}{x^2+y^2} + \psi_0(t).\,} $$
This is the field of a planar dipole aligned with $y$ whose strength oscillates as $\sin\Omega t$.

### 3.4 Acceleration along $\theta = 0$

Why this tool: $\mathbf{a} = D\mathbf{v}/Dt$ (Eq. 2.25). Since $\nabla\wedge\mathbf{v} = 0$, Eq. (2.26) reduces to $\mathbf{a} = \partial_t\mathbf{v} + \nabla(\lvert\mathbf{v}\rvert^2/2)$ in any coordinate system.

$\lvert\mathbf{v}\rvert^2 = v_r^2 + v_\theta^2 = A^2\sigma^2\left(\sin^2\theta + \cos^2\theta\right)/r^4 = A^2\sigma^2/r^4$, so
$$ \frac{\lvert\mathbf{v}\rvert^2}{2} = \frac{A^2\sigma^2}{2r^4}, \qquad \frac{\partial}{\partial r}\left(\frac{\lvert\mathbf{v}\rvert^2}{2}\right) = -\frac{2A^2\sigma^2}{r^5}, \qquad \frac{1}{r}\frac{\partial}{\partial\theta}\left(\frac{\lvert\mathbf{v}\rvert^2}{2}\right) = 0. $$
Local term, with $\partial_t\sigma = \Omega\cos\Omega t$: $\partial_tv_r = -A\Omega\cos(\Omega t)\sin\theta/r^2$ and $\partial_tv_\theta = A\Omega\cos(\Omega t)\cos\theta/r^2$. Therefore, for any $\theta$,
$$ a_r = -\frac{A\Omega\cos(\Omega t)\sin\theta}{r^2} - \frac{2A^2\sin^2(\Omega t)}{r^5}, \qquad a_\theta = \frac{A\Omega\cos(\Omega t)\cos\theta}{r^2}. $$
On the line $\theta = 0$ ($\sin\theta = 0$, $\cos\theta = 1$):
$$ \boxed{\,a_r = -\frac{2A^2\sin^2(\Omega t)}{r^5},\qquad a_\theta = \frac{A\Omega\cos(\Omega t)}{r^2}.\,} $$

### 3.5 Trajectories and streamlines

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12) and streamlines the tangency condition (Eq. 2.21).

Streamlines at a frozen instant ($\sigma \neq 0$): $dr/v_r = r\,d\theta/v_\theta$ gives
$$ \frac{dr}{r\,d\theta} = \frac{v_r}{v_\theta} = -\frac{\sin\theta}{\cos\theta} \;\Longrightarrow\; \frac{dr}{r} = -\tan\theta\,d\theta \;\Longrightarrow\; \ln\frac{r}{r_0} = \ln\left\lvert\frac{\cos\theta}{\cos\theta_0}\right\rvert, \qquad \boxed{\,r = r_0\frac{\cos\theta}{\cos\theta_0} = C\cos\theta,\,} $$
because $\int-\tan\theta\,d\theta = \ln\lvert\cos\theta\rvert$. In Cartesian variables $x^2 + y^2 = Cx$: circles of diameter $C$ centred at $(C/2, 0)$, tangent to the $y$-axis at the origin. This is the dipole pattern, independent of $t$.

Trajectories: the system $dr/dt = v_r$, $r\,d\theta/dt = v_\theta$ contains the same ratio, so dividing the equations removes $t$ and $\sigma(t)$ and gives the same relation; therefore the path lines are the same circles, $r = r_0\cos\theta/\cos\theta_0$.

Time law. Insert $r^3 = r_0^3\cos^3\theta/\cos^3\theta_0$ in $d\theta/dt = v_\theta/r = A\sigma\cos\theta/r^3$:
$$ \frac{d\theta}{dt} = \frac{A\cos^3\theta_0}{r_0^3}\,\frac{\sin\Omega t}{\cos^2\theta} \;\Longrightarrow\; \cos^2\theta\,d\theta = \frac{A\cos^3\theta_0}{r_0^3}\sin\Omega t\,dt. $$
Integrate with Barrow's rule between $(\theta_0, 0)$ and $(\theta, t)$. For the left side use $\cos^2\theta' = (1 + \cos 2\theta')/2$, whose primitive is $\theta'/2 + \sin 2\theta'/4$; for the right side $\int_0^t\sin\Omega t'\,dt' = (1 - \cos\Omega t)/\Omega$:
$$ \frac{\theta - \theta_0}{2} + \frac{\sin 2\theta - \sin 2\theta_0}{4} = \frac{A\cos^3\theta_0}{r_0^3\Omega}\left(1 - \cos\Omega t\right), $$
$$ \boxed{\,\theta - \theta_0 + \frac{\sin 2\theta - \sin 2\theta_0}{2} = \frac{2A\cos^3\theta_0}{r_0^3\,\Omega}\left(1 - \cos\Omega t\right),\qquad r = r_0\frac{\cos\theta}{\cos\theta_0}.\,} $$
The right-hand side vanishes at $\Omega t = 2n\pi$, so the particle oscillates with the period $2\pi/\Omega$ and returns to its initial position at the end of each period.

### 3.6 Fluid line initially at $\theta = 0$, $0 < r < \infty$

Why this tool: the fluid line is the image of the initial curve under the trajectories (Eq. 2.17), with the material label eliminated afterwards. Label the particles by $\lambda = r_0$, with $\theta_0 = 0$ (so $\cos\theta_0 = 1$, $\sin 2\theta_0 = 0$).

From 3.5, the path and the time law reduce to
$$ \frac{r}{\cos\theta} = \lambda, \qquad \theta + \frac{\sin 2\theta}{2} = \frac{2A}{\lambda^3\Omega}\left(1 - \cos\Omega t\right). $$
Eliminate $\lambda$ (change of variable from label to current position) with $\lambda = r/\cos\theta$, $\lambda^{-3} = \cos^3\theta/r^3$:
$$ \theta + \frac{\sin 2\theta}{2} = \frac{2A\cos^3\theta}{r^3\,\Omega}\left(1 - \cos\Omega t\right) \;\Longrightarrow\; \boxed{\,\frac{r^3}{2\cos^3\theta}\left(\theta + \frac{\sin 2\theta}{2}\right) = \frac{A}{\Omega}\left[1 - \cos(\Omega t)\right].\,} $$
At $t = 0$ the right-hand side is $0$ and the equation gives $\theta = 0$ (the initial line), as it must.

> [!warning] Reading of the official handwritten solution
> In K9.pdf (part 6) the boxed final equation reads, as legible in the scan, $\frac{r^3}{2\cos^3\theta}\left(\theta + \frac{\sin 2\theta}{2}\right) = \frac{A}{\Omega}\left[1 + \cos(\Omega t)\right]$, whereas the line immediately above it in the same solution has $\frac{A}{\Omega}\left[1 - \cos(\Omega t)\right] = \frac{\lambda^3}{2}\left(\theta + \frac{\sin 2\theta}{2}\right)$. With $1 + \cos\Omega t$ the right-hand side would be $2A/\Omega$ at $t = 0$ and the initial line $\theta = 0$ would not be recovered; the correct sign is $1 - \cos\Omega t$, as derived above. Numerical test with $A = 0.7$ m$^3$/s, $\Omega = 1.6$ s$^{-1}$, $\lambda = 1.2$ m, $t = 1.4$ s: integrating the particle ODE gives $r^3(\theta + \sin 2\theta/2)/(2\cos^3\theta) = 0.708908$, equal to $(A/\Omega)(1 - \cos\Omega t) = 0.708908$, while the "plus" form would give $0.166092$.

## Phase 4: Interpretation, Limits and Dimensional Check

- The field is the oscillating field of a planar dipole: irrotational and incompressible, with circular streamlines through the singular point; the particles slosh back and forth along the circles ($\theta$ varies with $1 - \cos\Omega t \ge 0$, so for $A > 0$ the particle first moves towards larger $\theta$ and then returns).
- Existence of the fluid line: since $\theta + \tfrac12\sin 2\theta \le \pi/2$ for $\theta \le \pi/2$, particles of the line with $\dfrac{2A}{\lambda^3\Omega}\cdot 2 \ge \dfrac{\pi}{2}$, i.e. $\lambda^3 \le \dfrac{8A}{\pi\Omega}$, reach $\theta = \pi/2$ and $r = 0$ (the singular point) within a cycle. The formula holds for the particles that stay at $\lvert\theta\rvert < \pi/2$ ($\lambda > (8A/\pi\Omega)^{1/3}$, which is $1.0367$ m for $A = 0.7$ m$^3$/s and $\Omega = 1.6$ s$^{-1}$).
- Consistency: parts 1-2 imply 3 (potential and stream function exist); $\psi = $ const reproduces the streamlines $\cos\theta/r = $ const of 3.5; the acceleration of 3.4 is the field value at $\theta = 0$ (the acceleration of the particle that is there at time $t$).
- Dimensions (SI): $[v] = [A/r^2] = \text{m/s}$; $[\varphi] = [\psi] = [A/r] = \text{m}^2/\text{s}$; $[A\Omega/r^2] = (\text{m}^3\text{/s})(\text{s}^{-1})/\text{m}^2 = \text{m/s}^2$ and $[A^2/r^5] = (\text{m}^6/\text{s}^2)/\text{m}^5 = \text{m/s}^2$; $A/(r_0^3\Omega)$ is dimensionless; the fluid-line equation has units m$^3$ on both sides.
- Numerical cross-check: symbolic differentiation returns $\omega_z = 0$, $\nabla\cdot\mathbf{v} = 0$, $\nabla\varphi = \mathbf{v}$ and the polar stream-function relations exactly, and the full material derivative in polar components gives $a_r = -2A^2\sigma^2/r^5$, $a_\theta = A\Omega\cos\Omega t/r^2$ at $\theta = 0$. For the time law of 3.5, with $A = 0.7$ m$^3$/s, $\Omega = 1.6$ s$^{-1}$, $r_0 = 1.5$ m, $\theta_0 = 0.4$ rad, $t = 0.8$ s, the ODE integration gives $0.144498$ for the left side and the formula $0.144498$ for the right side.
