---
materia: Fluid Mechanics
tema: "Tema 2: Flow Kinematics"
tags:
  - problema-examen
  - cinematica
  - cizalladura
  - potencial
  - funcion-de-corriente
  - elemento-fluido
dificultad: media
fuente: "sources/cuatrimestre-1/01-fluid-mechanics/unit-02-flow-kinematics/problemas/K10.pdf"
---

# Problem K10: Planar Flow with Exponentially Varying Shear (Quiz, 30 September 2013)

> Official UC3M kinematics problem collection (Introduction to Fluid Mechanics, quiz of 30 September 2013). Part of [[Tema 2 - Flow Kinematics]]. Related concepts: [[Concepto - Vorticidad, Circulacion y Potencial de Velocidades|vorticity and potential]], [[Concepto - Flujo Convectivo y Funcion de Corriente|stream function]], [[Concepto - Deformacion, Rotacion y Tensor de Velocidad de Deformacion|rate-of-strain tensor]].

## Statement

Given the steady planar motion described by the velocity components

$$ v_x = A e^{\Omega t}\,y \qquad\text{and}\qquad v_y = B e^{\Omega t}\,x, $$

where $A$, $B$, and $\Omega$ are constants.

1. Determine the value of the volume dilation rate $\nabla\cdot\vec{v}$.
2. Obtain the value of $B$ for which the resulting flow is irrotational. Adopt this particular value in what follows.
3. Calculate the stream line that intersects the point $(x, y) = (x_0, y_0)$ at a given instant of time $t$. Sketch the resulting stream lines.
4. Compute the trajectory of a fluid particle located initially at $(x, y) = (x_0, y_0)$.
5. If they exist, calculate the velocity potential $\varphi$ and the stream function $\psi$.
6. Determine the rate-of-strain tensor $\bar{\bar{T}}_d$.
7. Describe the deformation of a fluid element of square shape whose sides of length $dl$ are initially oriented parallel to the axes.

Source: K10.pdf (page 1). Notes.pdf, Chapter 2: expansion rate Eqs. (2.62)-(2.63); vorticity Eq. (2.52); stream lines Eq. (2.21); trajectories Eq. (2.12); potential Eq. (2.34); stream function Eqs. (2.40)-(2.45); velocity gradient and rate-of-strain tensor Eqs. (2.46)-(2.48); square element Eqs. (2.56)-(2.61).

## Phase 1: Hypotheses, Degrees of Freedom and Data

- Planar flow with a velocity that is linear in the coordinates and multiplied by the common time factor $e^{\Omega t}$. Two spatial degrees of freedom and an explicit time dependence.
- Although the statement calls the motion "steady", the velocity depends explicitly on $t$ whenever $\Omega \neq 0$; the flow is unsteady in general (and part 3 asks for the streamline "at a given instant of time $t$"). The steady case is recovered for $\Omega = 0$. The general case $\Omega \neq 0$ is solved below, with $A \neq 0$.
- The constants $A$, $B$ and $\Omega$ have units s$^{-1}$ (so that $v = Ae^{\Omega t}y$ is a velocity).

| Symbol | Meaning | SI unit |
| :--- | :--- | :--- |
| $A$, $B$ | shear constants | s$^{-1}$ |
| $\Omega$ | rate of the exponential time dependence | s$^{-1}$ |
| $(x_0, y_0)$ | position at the reference (initial) instant | m |
| $\tau(t) = (A/\Omega)\left(e^{\Omega t} - 1\right)$ | dimensionless time variable defined in 3.4 | 1 |

## Phase 2: Coordinates, Frames and Changes of Variable

- Inertial frame, Cartesian basis $(\mathbf{e}_x,\mathbf{e}_y)$, origin at the stagnation point $\mathbf{v} = 0$. Gradient convention $(\nabla\mathbf{v})_{ij} = \partial v_j/\partial x_i$.
- Change of time variable for part 4: $\tau(t) = \dfrac{A}{\Omega}\left(e^{\Omega t} - 1\right)$, with $d\tau = A e^{\Omega t}dt$ and $\tau(0) = 0$. In terms of $\tau$ the unsteady trajectory system becomes autonomous with constant coefficients.
- Change of basis for the sum and difference coordinates $u = x + y$, $w = x - y$ (a rotation by $45^\circ$ and a scaling by $\sqrt2$) used to decouple the trajectory equations; this is the same basis that diagonalises $\bar{\bar{T}}_d$ in part 6.

## Phase 3: Step-by-Step Derivation

### 3.1 Volume dilation rate

Why this tool: $\nabla\cdot\mathbf{v}$ is the rate at which a material volume changes per unit volume (Eqs. 2.62-2.63).
$$ \nabla\cdot\mathbf{v} = \frac{\partial}{\partial x}\left(Ae^{\Omega t}y\right) + \frac{\partial}{\partial y}\left(Be^{\Omega t}x\right) = 0 + 0 = \boxed{\,0\,} $$
for any values of $A$, $B$ and $\Omega$: the flow is incompressible.

### 3.2 Condition for irrotational flow

Why this tool: the flow is irrotational when $\boldsymbol{\omega} = \nabla\wedge\mathbf{v} = 0$ (text after Eq. 2.33).
$$ \omega_z = \frac{\partial v_y}{\partial x} - \frac{\partial v_x}{\partial y} = Be^{\Omega t} - Ae^{\Omega t} = (B - A)e^{\Omega t}. $$
Since $e^{\Omega t} > 0$, $\omega_z = 0$ for all $t$ if and only if
$$ \boxed{\,B = A.\,} $$
From now on $\mathbf{v} = Ae^{\Omega t}(y, x)$.

### 3.3 Streamlines at a given instant

Why this tool: streamlines are tangent to the velocity at a frozen instant (Eq. 2.21); $t$ is a parameter.
$$ \frac{dx}{v_x} = \frac{dy}{v_y} \;\Longrightarrow\; \frac{dx}{Ae^{\Omega t}y} = \frac{dy}{Ae^{\Omega t}x} \;\Longrightarrow\; \frac{dx}{y} = \frac{dy}{x} \;\Longrightarrow\; x\,dx = y\,dy, $$
where the common non-zero factor $Ae^{\Omega t}$ cancels. Integrate between $(x_0,y_0)$ and $(x,y)$ (Barrow's rule):
$$ \left[\frac{x'^2}{2}\right]_{x_0}^{x} = \left[\frac{y'^2}{2}\right]_{y_0}^{y} \;\Longrightarrow\; \boxed{\,y^2 - x^2 = y_0^2 - x_0^2.\,} $$
These are rectangular hyperbolae with asymptotes $y = \pm x$; the shape does not depend on $t$ (only the speed does). For $y_0^2 > x_0^2$ the branches open towards $\pm y$, for $y_0^2 < x_0^2$ towards $\pm x$, and $y_0^2 = x_0^2$ gives the straight lines $y = \pm x$. Sketch (in words), for $Ae^{\Omega t} > 0$: $v_x$ has the sign of $y$ and $v_y$ the sign of $x$, so in the first and third quadrants the flow moves away from the origin along the diagonal $y = x$, and in the second and fourth quadrants towards the origin along $y = -x$. The origin is a stagnation point; it is a saddle, with $y = -x$ the incoming and $y = x$ the outgoing direction. For $Ae^{\Omega t} < 0$ all arrows reverse.

### 3.4 Trajectory of the particle starting at $(x_0, y_0)$

Why this tool: trajectories solve $d\mathbf{x}/dt = \mathbf{v}(\mathbf{x},t)$ with $\mathbf{x}(0) = (x_0, y_0)$ (Eq. 2.12). Because $\mathbf{v}$ is a separable product of a function of time and a function of position, the change of time variable $\tau$ of Phase 2 makes the system autonomous. With $d\tau = Ae^{\Omega t}dt$:
$$ \frac{dx}{d\tau} = y, \qquad \frac{dy}{d\tau} = x. $$
Sum and difference: $u = x + y$ and $w = x - y$ satisfy
$$ \frac{du}{d\tau} = y + x = u, \qquad \frac{dw}{d\tau} = y - x = -w. $$
Integrate with Barrow's rule between $\tau = 0$ and $\tau$: $\ln(u/u_0) = \tau$ and $\ln(w/w_0) = -\tau$, i.e. $u = (x_0 + y_0)e^{\tau}$ and $w = (x_0 - y_0)e^{-\tau}$. Return to $x = (u + w)/2$, $y = (u - w)/2$:
$$ \boxed{\,x = x_0\cosh\tau + y_0\sinh\tau,\qquad y = y_0\cosh\tau + x_0\sinh\tau,\qquad \tau = \frac{A}{\Omega}\left(e^{\Omega t} - 1\right).\,} $$
Path lines: eliminate $\tau$ using $\cosh^2\tau - \sinh^2\tau = 1$:
$$ y^2 - x^2 = (y_0^2 - x_0^2)\left(\cosh^2\tau - \sinh^2\tau\right) = y_0^2 - x_0^2, $$
the same hyperbolae as the streamlines. (The path lines coincide with the streamlines because the direction of $\mathbf{v}$ does not depend on time.)

Logarithmic form (equivalent, as in the handwritten solution). Along the path $y = \pm\sqrt{x^2 + y_0^2 - x_0^2}$, so $dx/dt = \pm Ae^{\Omega t}\sqrt{x^2 + C}$ with $C = y_0^2 - x_0^2$. Since $\dfrac{d}{dx}\ln\left(x + \sqrt{x^2 + C}\right) = \dfrac{1}{\sqrt{x^2 + C}}$, Barrow's rule gives, for $y_0 > 0$ (upper sign),
$$ \ln\frac{x + \sqrt{x^2 + y_0^2 - x_0^2}}{x_0 + y_0} = \frac{A}{\Omega}\left(e^{\Omega t} - 1\right), $$
which is $\ln[(x + y)/(x_0 + y_0)] = \tau$ obtained from $u = u_0e^{\tau}$. For $y_0 < 0$ the lower branch of the square root applies.

### 3.5 Velocity potential and stream function

Why this tool: the flow is irrotational (3.2) so a potential exists (Eq. 2.34); it is planar and solenoidal (3.1) so a stream function exists (Eq. 2.41).

Potential: $\partial_x\varphi = v_x = Ae^{\Omega t}y$ gives $\varphi = Ae^{\Omega t}xy + f(y,t)$; $\partial_y\varphi = Ae^{\Omega t}x + f' = v_y = Ae^{\Omega t}x$ gives $f' = 0$:
$$ \boxed{\,\varphi = Ae^{\Omega t}\,xy + \varphi_0(t).\,} $$
Stream function: $\partial_y\psi = v_x = Ae^{\Omega t}y$ gives $\psi = \tfrac12Ae^{\Omega t}y^2 + g(x,t)$; $-\partial_x\psi = -g' = v_y = Ae^{\Omega t}x$ gives $g = -\tfrac12Ae^{\Omega t}x^2$:
$$ \boxed{\,\psi = \frac{A e^{\Omega t}}{2}\left(y^2 - x^2\right) + \psi_0(t).\,} $$
Check: $\partial_y\psi = Ae^{\Omega t}y = v_x$ and $-\partial_x\psi = Ae^{\Omega t}x = v_y$. The level curves $\psi = $ const are the hyperbolae of 3.3 (Eq. 2.42), and are orthogonal to the level curves of $\varphi$ ($xy = $ const).

> [!warning] Reading of the official handwritten solution
> K10.pdf (part 5) gives $\psi = Ae^{\Omega t}(y^2 - x^2) + \psi_0$, without the factor $1/2$. That expression would give $\partial_y\psi = 2Ae^{\Omega t}y$, twice the velocity component $v_x$. The relations written just above that line, $\partial_y\psi = Ae^{\Omega t}y$ and $\partial_x\psi = -Ae^{\Omega t}x$, are correct, and integrating them produces the factor $1/2$. The correct result is $\psi = \tfrac12Ae^{\Omega t}(y^2 - x^2) + \psi_0$. The statement also calls the motion "steady", although the velocity depends on $t$ through $e^{\Omega t}$ (see Phase 1). The velocity potential $\varphi = Ae^{\Omega t}xy + \varphi_0$ in the handwritten solution is correct.

### 3.6 Rate-of-strain tensor

Why this tool: $\bar{\bar{T}}_d = \tfrac12\left[\nabla\mathbf{v} + (\nabla\mathbf{v})^T\right]$ (Eq. 2.47) gives the pure strain of the material elements.
$$ \nabla\mathbf{v} = \begin{pmatrix}\partial_xv_x & \partial_xv_y\\ \partial_yv_x & \partial_yv_y\end{pmatrix} = Ae^{\Omega t}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \qquad \boxed{\,\bar{\bar{T}}_d = Ae^{\Omega t}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} = \nabla\mathbf{v}.\,} $$
It is symmetric, so $\bar{\bar{T}}_r = \tfrac12\left[\nabla\mathbf{v} - (\nabla\mathbf{v})^T\right] = 0$, consistent with $\omega_z = 0$. Its eigenvalues follow from $\lambda^2 - (Ae^{\Omega t})^2 = 0$: $\lambda = \pm Ae^{\Omega t}$, with principal directions $(1,1)/\sqrt2$ (extension, for $Ae^{\Omega t} > 0$) and $(1,-1)/\sqrt2$ (compression); these are the outgoing and incoming diagonals found in 3.3. The trace is zero ($\nabla\cdot\mathbf{v} = 0$).

### 3.7 Deformation of a square fluid element

Why this tool: a material segment evolves as $d\mathbf{l}(t+dt) = d\mathbf{l} + (d\mathbf{l}\cdot\nabla\mathbf{v})\,dt$ (Eqs. 2.46 and 2.56-2.57). With the sides along the axes:
$$ dl\,(1,0) \;\to\; dl\,(1,0) + dl\,(1,0)\,Ae^{\Omega t}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}dt = dl\,\left(1,\ Ae^{\Omega t}dt\right), $$
$$ dl\,(0,1) \;\to\; dl\,(0,1) + dl\,(0,1)\,Ae^{\Omega t}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}dt = dl\,\left(Ae^{\Omega t}dt,\ 1\right). $$
The horizontal side tilts upward by the angle $Ae^{\Omega t}dt$ and the vertical side tilts towards $+x$ by the same angle, so the two sides rotate towards each other, and their (initially right) angle decreases by $2Ae^{\Omega t}dt$. There is no net rotation ($\bar{\bar{T}}_r = 0$): the square deforms into a rhombus-like parallelogram by pure shear strain, with strain rate $\dot\gamma = \partial_xv_y + \partial_yv_x = 2Ae^{\Omega t}$ (the rate at which the angle between the sides decreases, Notes after Eq. 2.61). The area changes only at second order ($dl^2\left[1 - (Ae^{\Omega t}dt)^2\right]$), as required by $\nabla\cdot\mathbf{v} = 0$. Equivalently, the diagonal along $y = x$ is stretched at the rate $Ae^{\Omega t}$ and the diagonal along $y = -x$ is compressed at the same rate.

## Phase 4: Interpretation, Limits and Dimensional Check

- Physical picture: it is the stagnation-point flow of K7 rotated by $45^\circ$ (principal axes along the diagonals, no rotation), with a strain rate $Ae^{\Omega t}$ that grows or decays exponentially in time.
- Steady limit $\Omega \to 0$: $\tau \to At$, and the trajectories become $x = x_0\cosh At + y_0\sinh At$, $y = y_0\cosh At + x_0\sinh At$, the standard stagnation-point trajectories. For $\Omega < 0$ the time variable saturates at $\tau_\infty = A/\lvert\Omega\rvert$, so particles approach finite limit positions (the strain rate dies out) instead of escaping.
- Particles on the incoming diagonal $y_0 = -x_0$ satisfy $u = 0$ for all $t$ and $w = w_0e^{-\tau}$: they move towards the origin as $\tau$ grows, but reach it only as $\tau \to \infty$ (for $\Omega > 0$, $A > 0$, as $t \to \infty$).
- Consistency: $\bar{\bar{T}}_d$ symmetric traceless, $\omega_z = 0$, $\nabla\cdot\mathbf{v} = 0$; $\psi = $ const reproduces the streamlines of 3.3 and the paths of 3.4.
- Dimensions (SI): $[Ae^{\Omega t}y] = \text{s}^{-1}\text{m} = \text{m/s}$; $[\tau] = [A/\Omega] = 1$; $[\varphi] = [Axy] = \text{m}^2/\text{s}$; $[\psi] = [Ay^2] = \text{m}^2/\text{s}$; $[\bar{\bar{T}}_d] = [A] = \text{s}^{-1}$; $[\dot\gamma] = \text{s}^{-1}$.
- Numerical cross-check: RK4 integration of the particle ODE with $A = B = 0.8$ s$^{-1}$, $\Omega = 0.9$ s$^{-1}$, $(x_0,y_0) = (0.5, 1.2)$ m up to $t = 1.7$ s gives $(21.17827, 21.20635)$ m, equal to the $\cosh$/$\sinh$ formulas ($\tau = 3.216157$), with $y^2 - x^2 = 1.19$ m$^2$ equal to $y_0^2 - x_0^2$, and $\ln[(x+y)/(x_0+y_0)] = 3.216157 = \tau$.
