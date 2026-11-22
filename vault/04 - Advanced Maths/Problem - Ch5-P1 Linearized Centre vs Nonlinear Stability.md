---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 1"
dificultad: media
id: "e1"
pill: "Linearized Centre • Polar Form • Hartman-Grobman Limit"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.1: Linearized Centre vs Nonlinear Stability

> Official exercise 1 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The linearized system may not give a qualitatively correct picture when the linearized equation produces a center, as this example demonstrates. First show that the origin is a center for the linearized version of the system

$$
\dot x = -y + \lambda x(x^2 + y^2), \qquad \dot y = x + \lambda y(x^2 + y^2).
$$

Write down the equation satisfied by $r$, where $r^2 = x^2 + y^2$, and show that the stability of the origin depends actually on the sign of $\lambda$. Draw the phase portrait for $\lambda < 0$.

## Setting up the system

We begin by writing the autonomous planar system in standard component form $\dot x = f(x,y)$, $\dot y = g(x,y)$ and noting the role of the real parameter $\lambda$.

$$
f(x,y) = -y + \lambda x(x^2 + y^2), \qquad g(x,y) = x + \lambda y(x^2 + y^2), \qquad \lambda \in \mathbb{R}.
$$

Both $f$ and $g$ are polynomials in $(x,y)$, hence $C^\infty(\mathbb{R}^2)$, so global existence and uniqueness of local trajectories hold everywhere. Because the symbol $\lambda$ already denotes the real system parameter, we write $\mu_\pm$ for the eigenvalues of the Jacobian matrix to avoid any notation clash.

## Step 1: Critical points

We find all stationary points $(x^*, y^*) \in \mathbb{R}^2$ by setting $f(x,y) = 0$ and $g(x,y) = 0$ simultaneously.

$$
-y + \lambda x(x^2 + y^2) = 0, \qquad x + \lambda y(x^2 + y^2) = 0.
$$

To eliminate the cubic term $\lambda(x^2 + y^2)$ without dividing by a possibly zero quantity, multiply the first equation by $y$ and the second equation by $x$:

$$
-y^2 + \lambda xy(x^2 + y^2) = 0, \qquad x^2 + \lambda xy(x^2 + y^2) = 0.
$$

Subtracting the first equation from the second gives

$$
x^2 + y^2 = 0.
$$

Since $x$ and $y$ are real numbers, $x^2 \ge 0$ and $y^2 \ge 0$, so $x^2 + y^2 = 0$ forces $x = 0$ and $y = 0$. Checking directly, $f(0,0) = 0$ and $g(0,0) = 0$. Thus the origin

$$
(x^*, y^*) = (0, 0)
$$

is the **unique real critical point** of the system for every $\lambda \in \mathbb{R}$.

## Step 2: Linearization

We compute the Jacobian matrix $J(x,y)$ by differentiating $f(x,y)$ and $g(x,y)$ with respect to $x$ and $y$ using the product rule, and then evaluate it at $(0,0)$.

Expanding $f(x,y) = -y + \lambda x^3 + \lambda xy^2$ and $g(x,y) = x + \lambda x^2 y + \lambda y^3$:

$$
\frac{\partial f}{\partial x} = 3\lambda x^2 + \lambda y^2 = \lambda(3x^2 + y^2), \qquad \frac{\partial f}{\partial y} = -1 + 2\lambda xy,
$$

$$
\frac{\partial g}{\partial x} = 1 + 2\lambda xy, \qquad \frac{\partial g}{\partial y} = \lambda x^2 + 3\lambda y^2 = \lambda(x^2 + 3y^2).
$$

Hence the general Jacobian matrix is

$$
J(x,y) = \begin{pmatrix} \lambda(3x^2 + y^2) & -1 + 2\lambda xy \\ 1 + 2\lambda xy & \lambda(x^2 + 3y^2) \end{pmatrix}.
$$

Evaluating at $(x^*, y^*) = (0, 0)$ yields

$$
J(0,0) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
$$

which is completely independent of $\lambda$. The linearized system about the origin is therefore $\dot u = -v$, $\dot v = u$, where $(u,v) = (x,y)$.

## Step 3: Local study

We determine the eigenvalues and eigenvectors of $J(0,0)$ to classify the linearized equilibrium and check whether the Hartman–Grobman (Poincaré) linearization theorem applies.

Form the characteristic polynomial $\det(J(0,0) - \mu I) = 0$:

$$
\det\begin{pmatrix} -\mu & -1 \\ 1 & -\mu \end{pmatrix} = (-\mu)(-\mu) - (-1)(1) = \mu^2 + 1 = 0 \;\Longrightarrow\; \mu_\pm = \pm i.
$$

To find the complex eigenvector $\vec\eta_+$ associated with $\mu_+ = i$, solve $(J(0,0) - iI)\vec\eta_+ = \vec 0$ row by row:

$$
\begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix}\begin{pmatrix} \eta_1 \\ \eta_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.
$$

- Row 2 gives $\eta_1 - i\eta_2 = 0 \implies \eta_1 = i\eta_2$.
- Row 1 gives $-i(i\eta_2) - \eta_2 = \eta_2 - \eta_2 = 0$ (consistent).

Choosing $\eta_2 = 1$ yields

$$
\vec\eta_+ = \begin{pmatrix} i \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} + i\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \vec\eta_- = \begin{pmatrix} -i \\ 1 \end{pmatrix}.
$$

Because the eigenvalues $\mu_\pm = \pm i$ are purely imaginary ($\operatorname{Re}(\mu_\pm) = 0$, $\operatorname{Im}(\mu_\pm) = \pm 1 \neq 0$), the origin is a **centre** for the linearized system, with circular trajectories rotating counter-clockwise (at $(1,0)$, $\dot x = 0$ and $\dot y = 1 > 0$).

However, $(0,0)$ is **non-hyperbolic** ($\operatorname{Re}(\mu_\pm) = 0$). Consequently, the Hartman–Grobman / Poincaré linearization theorem does **not** apply: the cubic nonlinearities $\lambda x(x^2+y^2)$ and $\lambda y(x^2+y^2)$ can destroy the closed orbits of the linear centre and turn the origin into either an asymptotically stable spiral or an unstable spiral.

## Step 4: Global picture

We transform the full nonlinear system into polar coordinates $(r, \theta)$ to obtain exact equations for the radial distance and rotation angle across the entire plane.

### Radial equation for $r$

From $r^2 = x^2 + y^2$, differentiate both sides with respect to $t$ using the chain rule:

$$
\frac{d}{dt}(r^2) = 2r\dot r = 2x\dot x + 2y\dot y.
$$

Substitute $\dot x = -y + \lambda x(x^2+y^2)$ and $\dot y = x + \lambda y(x^2+y^2)$:

$$
\begin{aligned}
2r\dot r &= 2x\bigl(-y + \lambda x(x^2 + y^2)\bigr) + 2y\bigl(x + \lambda y(x^2 + y^2)\bigr) \\
&= -2xy + 2\lambda x^2(x^2 + y^2) + 2xy + 2\lambda y^2(x^2 + y^2) \\
&= 2\lambda(x^2 + y^2)(x^2 + y^2) \\
&= 2\lambda r^4.
\end{aligned}
$$

For $r > 0$, dividing both sides by $2r$ yields the exact radial ODE:

$$
\dot r = \lambda r^3.
$$

(This also holds at $r = 0$, since the origin is a stationary point with $\dot r = 0$.)

### Angular equation for $\theta$

Differentiating $\tan\theta = y/x$ with respect to $t$ gives $\sec^2\theta\,\dot\theta = (x\dot y - y\dot x)/x^2$. Multiplying by $\cos^2\theta = x^2/r^2$ yields

$$
\dot\theta = \frac{x\dot y - y\dot x}{r^2}.
$$

Compute the numerator explicitly:

$$
\begin{aligned}
x\dot y - y\dot x &= x\bigl(x + \lambda y(x^2 + y^2)\bigr) - y\bigl(-y + \lambda x(x^2 + y^2)\bigr) \\
&= x^2 + \lambda xy(x^2 + y^2) + y^2 - \lambda xy(x^2 + y^2) \\
&= x^2 + y^2 = r^2.
\end{aligned}
$$

Therefore, for every $r > 0$,

$$
\dot\theta = \frac{r^2}{r^2} = 1 > 0.
$$

Every non-trivial trajectory rotates **counter-clockwise** at constant unit angular speed $\theta(t) = \theta_0 + t$.

### Stability dependence on the sign of $\lambda$

Separating variables in $\dot r = \lambda r^3$ for $r_0 = r(0) > 0$:

$$
\frac{dr}{r^3} = \lambda\,dt \;\Longrightarrow\; \int_{r_0}^{r(t)} r^{-3}\,dr = \int_0^t \lambda\,ds \;\Longrightarrow\; \left[-\frac{1}{2r^2}\right]_{r_0}^{r(t)} = \lambda t.
$$

Simplifying gives

$$
\frac{1}{r(t)^2} = \frac{1}{r_0^2} - 2\lambda t \;\Longrightarrow\; r(t) = \frac{1}{\sqrt{r_0^{-2} - 2\lambda t}}.
$$

Three distinct qualitative regimes emerge according to the sign of $\lambda$:

1. **$\lambda < 0$ (asymptotically stable spiral):** Since $\dot r = \lambda r^3 < 0$ for all $r > 0$, the radius decreases strictly monotonically. Here $-2\lambda > 0$, so $r_0^{-2} - 2\lambda t > 0$ for all $t \ge 0$, and $r(t) \to 0$ as $t \to +\infty$ (with slow algebraic decay $r(t) \sim (-2\lambda t)^{-1/2}$ rather than exponential decay). Combined with $\dot\theta = 1 > 0$, all trajectories spiral counter-clockwise into the origin.
2. **$\lambda = 0$ (true nonlinear centre):** Here $\dot r = 0$, so $r(t) = r_0$ is constant and trajectories are exact concentric circles $x^2 + y^2 = r_0^2$ traversed counter-clockwise with period $2\pi$. The origin is Lyapunov stable, but not asymptotically stable.
3. **$\lambda > 0$ (unstable spiral with finite-time blow-up):** Since $\dot r = \lambda r^3 > 0$ for all $r > 0$, every trajectory spirals counter-clockwise outward. Moreover, $r_0^{-2} - 2\lambda t$ reaches zero at $t_* = \frac{1}{2\lambda r_0^2} < \infty$, so $r(t) \to +\infty$ in finite time.

![[attachments/AM-PS/ch5-e1-spiral.svg]]
*Phase portrait of $\dot x = -y + \lambda x(x^2+y^2)$, $\dot y = x + \lambda y(x^2+y^2)$ for $\lambda < 0$ (drawn with $\lambda = -1$). Every non-trivial trajectory spirals counter-clockwise ($\dot\theta = 1 > 0$) into the asymptotically stable origin as $r(t) = (r_0^{-2} - 2\lambda t)^{-1/2} \to 0$.*

## Answers and checks

- **Check against Robinson (Ex. 32.1):** The radial equation $\dot r = \lambda r^3$ and the trichotomy ($\lambda < 0$ stable spiral, $\lambda = 0$ centre, $\lambda > 0$ unstable spiral) match Robinson, *An Introduction to Ordinary Differential Equations*, Exercise 32.1.
- **Limiting case $\lambda \to 0$:** Setting $\lambda = 0$ in the exact radial formula $r(t) = (r_0^{-2} - 2\lambda t)^{-1/2}$ recovers $r(t) = r_0$, matching the circular orbits of the linearized centre.
- **Dimensional / scaling consistency:** Taking $x, y$ to have length dimension $[L]$ and $t$ to have time dimension $[T]$, the linear terms $\dot x \sim -y$ require unit frequency $[T^{-1}]$, while $\lambda x^3$ has dimension $[\lambda][L]^3 = [L][T]^{-1} \implies [\lambda] = [L]^{-2}[T]^{-1}$. Then $\dot r = \lambda r^3$ has dimension $[L]^{-2}[T]^{-1}\cdot [L]^3 = [L][T]^{-1}$, and $r_0^{-2} - 2\lambda t$ has homogeneous dimension $[L]^{-2}$.

> [!result] Key results
> - **Linearization at $(0,0)$:** $J(0,0) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ with eigenvalues $\mu_\pm = \pm i$ (linearized centre; Hartman–Grobman does not apply).
> - **Exact polar form:** $\dot r = \lambda r^3$, $\dot\theta = 1$, with radial solution $r(t) = \bigl(r_0^{-2} - 2\lambda t\bigr)^{-1/2}$.
> - **Nonlinear stability of $(0,0)$:** asymptotically stable spiral for $\lambda < 0$; true centre for $\lambda = 0$; unstable spiral (finite-time blow-up at $t_* = 1/(2\lambda r_0^2)$) for $\lambda > 0$.
