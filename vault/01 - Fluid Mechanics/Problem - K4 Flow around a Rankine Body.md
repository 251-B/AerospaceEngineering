---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - potencial
  - semicuerpo-rankine
  - punto-de-remanso
  - funcion-de-corriente
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K4.pdf"
---

# Problem K4: Source in a Uniform Stream (Rankine Half-Body)

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Topic 2 - Flow Kinematics]]. Related concepts: [[Concept - Vorticity, Circulation and Velocity Potential|velocity potential]], [[Concept - Convective Flux and Stream Function|stream function]], [[Concept - Curvilinear Coordinates and Differential Operators|polar coordinates]].

## Statement

Consider the fluid flow that derives from the potential

$$ \varphi = \frac{Q}{2\pi}\ln r + U_\infty r\cos\theta, $$

corresponding to the superposition of a uniform stream of velocity $U_\infty$ and a source of volumetric flux $Q$.

1. Determine the velocity components in cartesian and cylindrical coordinates.
2. Obtain the stream lines.
3. Compute the trajectories and paths.
4. Calculate the stagnation points, sketching the stream lines that reach them.
5. Consider the flow near the stagnation points, determining in particular the trajectories and the stream lines.

Source: K4.pdf (page 1). Notes.pdf, Chapter 2: potential Eq. (2.34), gradient in orthogonal coordinates Eq. (2.3), stagnation points Eq. (2.11), trajectories Eqs. (2.12)-(2.15), stream lines Eq. (2.21), stream function Eqs. (2.40)-(2.45), velocity gradient Eq. (2.46).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar flow in the plane $(r,\theta)$ (or $(x,y)$), steady, derived from a potential: $\mathbf{v} = \nabla\varphi$. The flow is irrotational and, since $\nabla^2\varphi = 0$ for $r > 0$, incompressible.
- The point $r = 0$ is the source and is excluded from the domain. Because the problem is two-dimensional, $Q$ is the volume flux per unit length normal to the plane.
- Degrees of freedom: two coordinates $(r,\theta)$; steady flow, so no time dependence enters the field.
- $\theta$ is multivalued around the origin; where a stream function is used, the range $0 < \theta < 2\pi$ is adopted (cut along the positive $x$-axis).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $Q$ | source strength (volume flux per unit depth) | m$^2$/s |
| $U_\infty$ | velocity of the uniform stream, along $+x$ | m/s |
| $\varphi$ | velocity potential | m$^2$/s |
| $\psi$ | stream function | m$^2$/s |
| $r_s = Q/(2\pi U_\infty)$ | distance source-stagnation point (derived in 3.4) | m |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame at rest with the source. Cartesian basis $(\mathbf{e}_x,\mathbf{e}_y)$ and polar basis $(\mathbf{e}_r,\mathbf{e}_\theta)$ with $x = r\cos\theta$, $y = r\sin\theta$.
- Change of basis (rotation by $\theta$): $\mathbf{e}_r = \cos\theta\,\mathbf{e}_x + \sin\theta\,\mathbf{e}_y$, $\mathbf{e}_\theta = -\sin\theta\,\mathbf{e}_x + \cos\theta\,\mathbf{e}_y$, so that
$$ \begin{pmatrix}v_x\\ v_y\end{pmatrix} = \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}\begin{pmatrix}v_r\\ v_\theta\end{pmatrix}. $$
This matrix has determinant $\cos^2\theta + \sin^2\theta = 1$ and its inverse is its transpose.
- Gradient in polar coordinates (scale factors $h_r = 1$, $h_\theta = r$, Eq. 2.3): $\nabla\varphi = \partial_r\varphi\,\mathbf{e}_r + r^{-1}\partial_\theta\varphi\,\mathbf{e}_\theta$.
- For part 5, local non-dimensional coordinates around the stagnation point and a non-dimensional time are introduced.

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity components

Why this tool: for a potential flow $\mathbf{v} = \nabla\varphi$ (Eq. 2.34); in polar coordinates the gradient has the scale factors above.
$$ v_r = \frac{\partial\varphi}{\partial r} = \frac{Q}{2\pi r} + U_\infty\cos\theta, \qquad v_\theta = \frac{1}{r}\frac{\partial\varphi}{\partial\theta} = -U_\infty\sin\theta. $$
Cartesian components by the rotation of Phase 2:
$$ v_x = v_r\cos\theta - v_\theta\sin\theta = \frac{Q\cos\theta}{2\pi r} + U_\infty\left(\cos^2\theta + \sin^2\theta\right) = \boxed{\,\frac{Q}{2\pi}\frac{x}{x^2+y^2} + U_\infty,\,} $$
$$ v_y = v_r\sin\theta + v_\theta\cos\theta = \frac{Q\sin\theta}{2\pi r} + U_\infty\left(\sin\theta\cos\theta - \sin\theta\cos\theta\right) = \boxed{\,\frac{Q}{2\pi}\frac{y}{x^2+y^2}.\,} $$
Flux check: on any circle of radius $r$ around the source, $\oint v_r\,r\,d\theta = \int_0^{2\pi}\left(\tfrac{Q}{2\pi} + U_\infty r\cos\theta\right)d\theta = Q + U_\infty r\left[\sin\theta\right]_0^{2\pi} = Q$, so $Q$ is indeed the source flux.

### 3.2 Streamlines

Why this tool: the flow is planar and incompressible, $\nabla\cdot\mathbf{v} = r^{-1}\partial_r(rv_r) + r^{-1}\partial_\theta v_\theta = r^{-1}\left(U_\infty\cos\theta\right) - r^{-1}U_\infty\cos\theta = 0$, so the stream lines are the level curves of a stream function (Eq. 2.42). They are obtained directly from the tangency condition (Eq. 2.21) in polar coordinates, $dr/v_r = r\,d\theta/v_\theta$:
$$ v_\theta\,dr - r\,v_r\,d\theta = 0 \;\Longleftrightarrow\; U_\infty\sin\theta\,dr + \left(\frac{Q}{2\pi} + U_\infty r\cos\theta\right)d\theta = 0. $$
This is an exact differential, because
$$ d\left[\frac{Q\theta}{2\pi} + U_\infty r\sin\theta\right] = \frac{Q}{2\pi}d\theta + U_\infty\sin\theta\,dr + U_\infty r\cos\theta\,d\theta. $$
Hence, with $\psi \equiv \dfrac{Q\theta}{2\pi} + U_\infty r\sin\theta$,
$$ \boxed{\,\psi = \frac{Q\theta}{2\pi} + U_\infty r\sin\theta = \text{const},\quad\text{i.e.}\quad \frac{Q\theta}{2\pi} + U_\infty r\sin\theta = \frac{Q\theta_0}{2\pi} + U_\infty r_0\sin\theta_0.\,} $$
Check in Cartesian variables: $\psi = \tfrac{Q}{2\pi}\theta + U_\infty y$ gives $\partial_y\psi = \tfrac{Q}{2\pi}\tfrac{x}{x^2+y^2} + U_\infty = v_x$ and $-\partial_x\psi = \tfrac{Q}{2\pi}\tfrac{y}{x^2+y^2} = v_y$, using $\partial_x\theta = -y/(x^2+y^2)$ and $\partial_y\theta = x/(x^2+y^2)$; this is the sign convention of Eq. (2.41).

### 3.3 Trajectories and paths

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12). In polar coordinates the system is
$$ \frac{dr}{dt} = \frac{Q}{2\pi r} + U_\infty\cos\theta, \qquad r\frac{d\theta}{dt} = -U_\infty\sin\theta, \qquad r(0) = r_i,\ \theta(0) = \theta_i. $$
Because the field is steady, the path lines coincide with the streamlines of 3.2, so the path is
$$ r(\theta) = \frac{\dfrac{Q}{2\pi}(\theta_i - \theta) + U_\infty r_i\sin\theta_i}{U_\infty\sin\theta}. $$
The time law follows from the second equation, $dt = -r\,d\theta/(U_\infty\sin\theta)$, by substituting $r(\theta)$ and defining $r_s \equiv Q/(2\pi U_\infty)$:
$$ t = -\frac{1}{U_\infty}\int_{\theta_i}^{\theta}\left[r_s(\theta_i - \theta') + r_i\sin\theta_i\right]\frac{d\theta'}{\sin^2\theta'}. $$
Two primitives are needed. First, $\int\csc^2\theta'\,d\theta' = -\cot\theta'$. Second, $F(\theta') \equiv -(\theta_i - \theta')\cot\theta' - \ln\lvert\sin\theta'\rvert$ satisfies $F'(\theta') = \cot\theta' + (\theta_i - \theta')\csc^2\theta' - \cot\theta' = (\theta_i - \theta')\csc^2\theta'$. Barrow's rule between $\theta_i$ and $\theta$ (where $F(\theta_i) = -\ln\lvert\sin\theta_i\rvert$ because the first term vanishes):
$$ \int_{\theta_i}^{\theta}(\theta_i-\theta')\csc^2\theta'\,d\theta' = -(\theta_i - \theta)\cot\theta - \ln\left\lvert\frac{\sin\theta}{\sin\theta_i}\right\rvert, \qquad \int_{\theta_i}^{\theta}\csc^2\theta'\,d\theta' = \cot\theta_i - \cot\theta. $$
Therefore
$$ \boxed{\,t = \frac{1}{U_\infty}\left\{r_s\left[(\theta_i - \theta)\cot\theta + \ln\left\lvert\frac{\sin\theta}{\sin\theta_i}\right\rvert\right] + r_i\sin\theta_i\left(\cot\theta - \cot\theta_i\right)\right\},\,} $$
valid while the particle stays in the same half-plane ($\sin\theta$ keeps its sign). For $0 < \theta < \pi$, $d\theta/dt < 0$: particles drift towards $\theta \to 0$, i.e. downstream. The axes $\theta = 0, \pi$ are invariant lines, with $dr/dt = Q/(2\pi r) \pm U_\infty$.

### 3.4 Stagnation points and the streamlines reaching them

Why this tool: a stagnation point is a point where the velocity vanishes (Eq. 2.11), so $v_r = v_\theta = 0$ simultaneously.

$v_\theta = -U_\infty\sin\theta = 0$ gives $\theta = 0$ or $\theta = \pi$. Then $v_r = 0$ requires $\dfrac{Q}{2\pi r} = -U_\infty\cos\theta$. For $\theta = 0$ the right side is negative, impossible for $r > 0$. For $\theta = \pi$,
$$ \boxed{\,\theta = \pi,\quad r = r_s = \frac{Q}{2\pi U_\infty}\quad\Longleftrightarrow\quad (x,y) = (-r_s, 0),\,} $$
the only stagnation point, upstream of the source.

Streamlines through it: $\psi_s = \dfrac{Q\pi}{2\pi} + U_\infty r_s\sin\pi = \dfrac{Q}{2}$. The streamline $\psi = Q/2$ consists of two branches:

- the incoming axis $\theta = \pi$, $r > r_s$ (where $\sin\pi = 0$ and $\psi = Q/2$);
- the curve $\dfrac{Q\theta}{2\pi} + U_\infty r\sin\theta = \dfrac{Q}{2}$, that is
$$ \boxed{\,r = \frac{Q}{2\pi U_\infty}\,\frac{\pi - \theta}{\sin\theta} = r_s\,\frac{\pi - \theta}{\sin\theta},\quad 0 < \theta < 2\pi,\,} $$
which at $\theta \to \pi$ gives $r \to r_s$ (the limit of $(\pi-\theta)/\sin\theta$ is $1$) and, for $\theta \to 0^+$ or $2\pi^-$, $r\sin\theta \to \pm\pi r_s = \pm Q/(2U_\infty)$. The closed-nose body so defined is the Rankine half-body: it has total half-width $Q/(2U_\infty)$ on each side far downstream, hence full width $Q/U_\infty$, consistent with the source flux $Q$ being carried within the width $Q/U_\infty$ of the uniform stream. Fluid emitted by the source stays inside this body, and the incoming stream passes outside.

Sketch (in words): the uniform stream comes from $x \to -\infty$, splits at the stagnation point $S = (-r_s, 0)$, and the dividing streamline leaves $S$ perpendicular to the axis, bending downstream to the two asymptotes $y = \pm Q/(2U_\infty)$.

### 3.5 Flow near the stagnation point

Why this tool: near a stagnation point the velocity is small, and a first-order Taylor expansion of the field captures the local kinematics (compare Eq. 2.46). Local non-dimensional variables, with $\lvert\xi\rvert,\lvert\eta\rvert \ll 1$ and the time scale $r_s/U_\infty$:
$$ \xi = \frac{x + r_s}{r_s},\qquad \eta = \frac{y}{r_s},\qquad \tau = \frac{U_\infty t}{r_s}. $$
Use $Q = 2\pi r_sU_\infty$ and $x = r_s(\xi - 1)$ in the Cartesian components of 3.1:
$$ \frac{v_x}{U_\infty} = 1 + \frac{\xi - 1}{(\xi-1)^2 + \eta^2}, \qquad \frac{v_y}{U_\infty} = \frac{\eta}{(\xi-1)^2+\eta^2}. $$
To first order, $\left[(1-\xi)^2 + \eta^2\right]^{-1} = 1 + 2\xi + \mathcal{O}(2)$, so $(\xi - 1)(1 + 2\xi) = -1 - \xi + \mathcal{O}(2)$ and
$$ V_\xi \equiv \frac{v_x}{U_\infty} \simeq -\xi, \qquad V_\eta \equiv \frac{v_y}{U_\infty} \simeq \eta. $$
Streamlines: $\dfrac{d\xi}{-\xi} = \dfrac{d\eta}{\eta} \Rightarrow \ln\lvert\xi\rvert + \ln\lvert\eta\rvert = $ const, that is
$$ \boxed{\,\xi\eta = \xi_0\eta_0\ \ (\text{hyperbolae}).\,} $$
Trajectories: $\dfrac{d\xi}{d\tau} = -\xi$ and $\dfrac{d\eta}{d\tau} = \eta$, with Barrow's rule, $\ln(\xi/\xi_0) = -\tau$ and $\ln(\eta/\eta_0) = \tau$:
$$ \boxed{\,\xi = \xi_0e^{-\tau},\qquad \eta = \eta_0e^{\tau}.\,} $$
The product $\xi\eta$ is constant along each trajectory, so paths and streamlines coincide. The axis $\eta = 0$ is the incoming streamline (approached only as $\tau \to \infty$) and $\xi = 0$ is the outgoing streamline along which the body contour leaves the point; the velocity gradient there has eigenvalues $-U_\infty/r_s$ (compression along $x$) and $+U_\infty/r_s$ (extension along $y$), a saddle.

> [!warning] Reading of the official handwritten solution
> In K4.pdf (part 5), as legible in the scan, the local variable is defined as $\xi = (x - r_0)/r_0$ with $r_0 = Q/(2\pi U_\infty)$. The stagnation point found in part 4 of the same solution is at $\theta = \pi$, i.e. $x = -r_0$, so the local variable must be $\xi = (x + r_0)/r_0$ (written $r_s$ here); otherwise $\xi$ would not be small at the stagnation point. With the corrected definition the handwritten results $V_\xi = -\xi$, $V_\eta = \eta$, $\xi\eta = \xi_0\eta_0$, $\xi = \xi_0e^{-\tau}$, $\eta = \eta_0e^{\tau}$ are recovered. The handwritten solution also reuses $r_0$ both for the initial radius of a particle (part 3) and for the stagnation distance; here $r_i$ and $r_s$ are used.

## Phase 4: Interpretation, Limits and Dimensional Check

- Far field: $r \to \infty$ gives $\mathbf{v} \to U_\infty\mathbf{e}_x$; near the source $v_r \to Q/(2\pi r)$, a purely radial outflow.
- Limits: $Q \to 0$ gives $r_s \to 0$ and the uniform stream, with streamlines $y = $ const (3.2 reduces to $r\sin\theta = $ const); $U_\infty \to 0$ gives $r_s \to \infty$, the pure source with radial streamlines $\theta = $ const.
- Mass balance of the half-body: width at infinity $Q/U_\infty$ times speed $U_\infty$ equals $Q$; this is the asymptotic result $r\sin\theta \to Q/2U_\infty$ of 3.4.
- Consistency: at the nose of the body the streamline direction is perpendicular to the axis (the contour is tangent to the outgoing axis $\xi = 0$ of 3.5), as sketched in the official figure.
- Dimensions (SI): $[Q/2\pi r] = (\text{m}^2/\text{s})/\text{m} = \text{m/s}$; $[r_s] = [Q/U_\infty] = \text{m}$; $[\psi] = [Q] = [U_\infty r] = \text{m}^2/\text{s}$; $[r_s/U_\infty] = \text{s}$, the time scale of 3.5 and of 3.3.
- Numerical cross-check with $Q = 1.7$ m$^2$/s, $U_\infty = 0.9$ m/s ($r_s = 0.30061$ m), start $r_i = 1.2$ m, $\theta_i = 2.0$ rad: RK4 integration of the particle ODE up to $t = 1.5$ s, then the boxed $t(\theta)$ evaluated at the final angle returns $1.5000000000000147$ s, and $\psi$ is conserved ($1.5231680274841803$ initially, $1.5231680274841746$ finally). Asymptote: $r\sin\theta$ at $\theta = 10^{-6}$ rad is $0.944444$ m versus $Q/2U_\infty = 0.944444$ m. Linearisation at $\xi = \eta = 10^{-3}$: $v_x/U_\infty = -0.00100000$, $v_y/U_\infty = +0.00100200$.
