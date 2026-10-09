---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - estancamiento
  - potencial
  - funcion-de-corriente
  - elemento-fluido
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K7.pdf"
---

# Problem K7: Hyperbolic Stagnation-Point Flow

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics). Part of [[Topic 2 - Flow Kinematics]]. Related concepts: [[Concept - Vorticity, Circulation and Velocity Potential|vorticity and potential]], [[Concept - Convective Flux and Stream Function|stream function]], [[Concept - Deformation, Rotation and the Rate-of-Strain Tensor|rate-of-strain tensor]], [[Concept - Material Derivative and Fluid Acceleration|acceleration]].

## Statement

Consider the planar motion of velocity components $v_x = ax$ and $v_y = by$, where $a$ and $b$ are known constants.

1. If the flow is irrotational compute the associated velocity potential.
2. Compute the value of $b$ for which the flow corresponds to that of an incompressible fluid (use that value in the solution of the following questions).
3. Obtain the stream lines and represent the result schematically.
4. Determine the trajectory and the path of a fluid particle initially located at $x_o = 0$ and $y_o = 1$. How long does it take to reach the origin?
5. Calculate the acceleration of fluid particles located along the axis $y = 0$.
6. Find the stream function for the flow.
7. Compute the rate-of-strain tensor.
8. Investigate the evolution of a fluid element whose initial shape is that of a square of sides $dl$,

Source: K7.pdf (page 1). The statement of part 8 is cut off in the scan after "sides $dl$,"; the handwritten solution takes the sides parallel to the coordinate axes, which is assumed here. Notes.pdf, Chapter 2: potential Eq. (2.34), incompressibility Eq. (2.38), stream lines Eq. (2.21), acceleration Eqs. (2.25)-(2.27), stream function Eqs. (2.40)-(2.42), rate-of-strain tensor Eqs. (2.47)-(2.48), square element Eqs. (2.56)-(2.61).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Steady, planar, linear velocity field $\mathbf{v} = (ax, by)$ on the whole plane. Two spatial degrees of freedom; no time dependence.
- $a$ and $b$ are constants with units s$^{-1}$. For the sketches and for part 4 we take $a > 0$ (a particle on the $y$-axis moves towards the origin once $b = -a$); for $a < 0$ every velocity reverses.
- The only stagnation point of the field is the origin (where $\mathbf{v} = 0$, Eq. 2.11).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $a$, $b$ | strain rates along $x$ and $y$ | s$^{-1}$ |
| $(x_o, y_o) = (0, 1)$ | initial position of the particle of part 4 | m |
| $dl$ | side of the fluid element | m |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame, Cartesian basis $(\mathbf{e}_x,\mathbf{e}_y)$, origin at the stagnation point. The velocity gradient convention is $(\nabla\mathbf{v})_{ij} = \partial v_j/\partial x_i$.
- Cartesian acceleration: $a_i = \partial_t v_i + v_j\,\partial_j v_i$ (Eq. 2.27, valid in Cartesian coordinates).
- No change of coordinates is required; the principal axes of strain coincide with the coordinate axes (part 7), so the change-of-basis matrix is the identity.

## Phase 3: Step-by-Step Derivation

### 3.1 Velocity potential for the irrotational case

Why this tool: a velocity potential exists when $\nabla\wedge\mathbf{v} = 0$ (Eq. 2.34).
$$ \omega_z = \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} = \frac{\partial(by)}{\partial x} - \frac{\partial(ax)}{\partial y} = 0 - 0 = 0 $$
for any $a$ and $b$, so the field is irrotational and $\mathbf{v} = \nabla\varphi$. Integrate $\partial_x\varphi = ax$: $\varphi = ax^2/2 + f(y)$. Then $\partial_y\varphi = f'(y) = by$ gives $f = by^2/2 + \varphi_0$:
$$ \boxed{\,\varphi = \frac{a x^2 + b y^2}{2} + \varphi_0.\,} $$

### 3.2 Incompressibility

Why this tool: $\nabla\cdot\mathbf{v} = 0$ (Eq. 2.38) is the condition for a liquid element to keep its volume.
$$ \nabla\cdot\mathbf{v} = \frac{\partial(ax)}{\partial x} + \frac{\partial(by)}{\partial y} = a + b = 0 \;\Longrightarrow\; \boxed{\,b = -a.\,} $$
From here on $\mathbf{v} = (ax, -ay)$ and $\varphi = a(x^2 - y^2)/2$ (up to a constant).

### 3.3 Streamlines

Why this tool: the field is steady, so the tangency condition (Eq. 2.21) gives fixed curves:
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \;\Longrightarrow\; \frac{dx}{ax} = \frac{dy}{-ay} \;\Longrightarrow\; \frac{dx}{x} = -\frac{dy}{y}. $$
Integrate between $(x_0, y_0)$ and $(x, y)$ (for $x_0y_0 \neq 0$): $\ln\lvert x/x_0\rvert = -\ln\lvert y/y_0\rvert$, so $\ln\lvert xy/(x_0y_0)\rvert = 0$:
$$ \boxed{\,xy = x_0y_0 = \text{const}.\,} $$
These are rectangular hyperbolae with the coordinate axes as asymptotes. The axes themselves are also streamlines ($x_0y_0 = 0$): the $y$-axis ($x = 0$), along which $v_y = -ay$ points towards the origin for $a > 0$, and the $x$-axis ($y = 0$), along which $v_x = ax$ points away from it. Schematic (in words): fluid approaches the origin along the $y$-axis, turns, and leaves along the $x$-axis; in each quadrant the streamlines are hyperbolae that follow the incoming axis and then the outgoing axis. This is the flow near a stagnation point on a wall (with the wall along the $x$-axis, in the half-plane $y > 0$).

### 3.4 Trajectory and path of the particle starting at $(0, 1)$

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}$ (Eq. 2.12).
$$ \frac{dx}{dt} = ax,\quad x(0) = 0 \;\Longrightarrow\; x(t) = 0; \qquad \frac{dy}{dt} = -ay,\quad y(0) = 1\ \text{m}. $$
Separate variables and apply Barrow's rule:
$$ \int_{1}^{y}\frac{dy'}{y'} = -a\int_0^t dt' \;\Longrightarrow\; \ln y = -at \;\Longrightarrow\; \boxed{\,x(t) = 0,\quad y(t) = e^{-at}\ \text{(m)}.\,} $$
Path line: the segment of the $y$-axis $x = 0$, $0 < y \le 1$ m.

Time to reach the origin. $y = 0$ would require $e^{-at} = 0$, which only happens as $t \to \infty$. The particle approaches the stagnation point exponentially but never reaches it in finite time: it takes the time $t_\varepsilon = a^{-1}\ln(1\,\text{m}/\varepsilon)$ to come within a distance $\varepsilon$ of the origin, and $t_\varepsilon \to \infty$ as $\varepsilon \to 0$. (A solution of the ODE cannot reach in finite time an equilibrium point of a Lipschitz field.)

### 3.5 Acceleration along $y = 0$

Why this tool: the acceleration is the material derivative of the velocity (Eq. 2.25); in Cartesian coordinates $a_i = \partial_t v_i + v_j\partial_jv_i$ (Eq. 2.27). The flow is steady, so only the convective part remains.
$$ a_x = v_x\frac{\partial v_x}{\partial x} + v_y\frac{\partial v_x}{\partial y} = (ax)(a) + (-ay)(0) = a^2x, \qquad a_y = v_x\frac{\partial v_y}{\partial x} + v_y\frac{\partial v_y}{\partial y} = (ax)(0) + (-ay)(-a) = a^2y. $$
On the axis $y = 0$:
$$ \boxed{\,\mathbf{a} = a^2x\,\mathbf{e}_x.\,} $$
It is directed along $+x$ for $x > 0$ and along $-x$ for $x < 0$, i.e. away from the origin, so the particles on the axis accelerate as they move outwards. Since the flow is irrotational, $\mathbf{a} = \nabla(\lvert\mathbf{v}\rvert^2/2) = a^2(x, y)$ (Eq. 2.26), which agrees.

### 3.6 Stream function

Why this tool: the flow is planar and incompressible ($b = -a$), so $v_x = \partial_y\psi$ and $v_y = -\partial_x\psi$ (Eq. 2.41).
$$ \frac{\partial\psi}{\partial y} = ax \;\Rightarrow\; \psi = axy + f(x); \qquad -\frac{\partial\psi}{\partial x} = -ay - f'(x) = v_y = -ay \;\Rightarrow\; f' = 0. $$
$$ \boxed{\,\psi = axy + \psi_0.\,} $$
The level curves $\psi = $ const are the hyperbolae $xy = $ const of 3.3 (Eq. 2.42), and $\psi - \psi_0$ vanishes on both axes.

### 3.7 Rate-of-strain tensor

Why this tool: $\bar{\bar{T}}_d = \tfrac12\left[\nabla\mathbf{v} + (\nabla\mathbf{v})^T\right]$ (Eq. 2.47) collects the stretching and shearing of material elements.
$$ \nabla\mathbf{v} = \begin{pmatrix}\partial_x v_x & \partial_x v_y\\ \partial_y v_x & \partial_y v_y\end{pmatrix} = \begin{pmatrix}a & 0\\ 0 & -a\end{pmatrix}, \qquad \boxed{\,\bar{\bar{T}}_d = \begin{pmatrix}a & 0\\ 0 & -a\end{pmatrix} = \nabla\mathbf{v},\,} $$
$$ \bar{\bar{T}}_r = \tfrac12\left[\nabla\mathbf{v} - (\nabla\mathbf{v})^T\right] = 0 \quad(\text{consistent with }\omega_z = 0). $$
$\bar{\bar{T}}_d$ is already diagonal: the principal directions are the coordinate axes, with principal strain rates $+a$ (along $x$, extension) and $-a$ (along $y$, compression); their sum is $\nabla\cdot\mathbf{v} = 0$.

### 3.8 Evolution of a square fluid element

Why this tool: a material segment evolves as $d\mathbf{l}(t+dt) = d\mathbf{l} + (d\mathbf{l}\cdot\nabla\mathbf{v})\,dt$ (Eqs. 2.46 and 2.56-2.57). With the sides along the axes:
$$ d\mathbf{l}_1 = dl\,(1,0) \;\to\; dl\,(1,0) + dl\,(1,0)\begin{pmatrix}a & 0\\ 0 & -a\end{pmatrix}dt = dl\,(1 + a\,dt,\ 0), $$
$$ d\mathbf{l}_2 = dl\,(0,1) \;\to\; dl\,(0,1) + dl\,(0,1)\begin{pmatrix}a & 0\\ 0 & -a\end{pmatrix}dt = dl\,(0,\ 1 - a\,dt). $$
The square becomes a rectangle: it is stretched along $x$ and compressed along $y$ at the rate $a$, with no rotation ($\bar{\bar{T}}_r = 0$) and no shear (off-diagonal terms zero, the right angle is preserved). Its area is $dl^2(1 + a\,dt)(1 - a\,dt) = dl^2(1 - a^2dt^2) \simeq dl^2$ to first order, as required by $\nabla\cdot\mathbf{v} = 0$. For a finite time the same linear flow gives sides $dl\,e^{at}$ and $dl\,e^{-at}$ (from $dl_x/dt = a\,dl_x$, $dl_y/dt = -a\,dl_y$), whose product is exactly $dl^2$.

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: the origin is a saddle-type stagnation point (a stagnation-point flow). The flow compresses material along $y$ and stretches it along $x$, with $T_{d,xx} + T_{d,yy} = 0$; there is no rotation anywhere.
- Consistency of results: the streamlines $xy = $ const (3.3) are the level curves of $\psi$ (3.6); the velocity is the gradient of $\varphi$ (3.1) and perpendicular to its level curves $x^2 - y^2 = $ const, which are the orthogonal family of hyperbolae; $\bar{\bar{T}}_r = 0$ (3.7) agrees with $\omega_z = 0$ (3.1).
- Limits: $a \to 0$ gives a fluid at rest (all quantities vanish, the particle of 3.4 stays at $y = 1$ m); $t \to \infty$ gives $y \to 0$.
- Dimensions (SI): $[a] = \text{s}^{-1}$; $[\varphi] = [ax^2] = \text{m}^2/\text{s}$; $[\psi] = [axy] = \text{m}^2/\text{s}$; $[\mathbf{a}] = [a^2x] = \text{s}^{-2}\cdot\text{m} = \text{m/s}^2$; $[\bar{\bar{T}}_d] = \text{s}^{-1}$; $[at]$ is dimensionless.
- Numerical cross-check: the acceleration of 3.5 was recomputed symbolically from $\mathbf{a} = (\mathbf{v}\cdot\nabla)\mathbf{v}$, and $\partial_y\psi$, $-\partial_x\psi$ return the velocity components.

> [!note] Reading of the official handwritten solution
> K7.pdf obtains $b = -a$, $xy = x_0y_0$, $x = 0$, $y = e^{-at}$ with "$y \to 0$ when $t \to \infty$" (so the origin is not reached in finite time), $\mathbf{a} = a^2x\,\mathbf{e}_x$ on $y = 0$, $\psi = axy + \psi_0$, $\bar{\bar{T}}_d = \mathrm{diag}(a, -a)$ and the element $dl\,(1 + a\,dt, 0)$, $dl\,(0, 1 - a\,dt)$. All agree with the results above; no discrepancy was found.
