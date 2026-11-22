---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 10"
dificultad: media
id: "e10"
pill: "Quadratic Drag • Nonlinear Spiral • Lyapunov Energy"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.10: Pendulum with Quadratic Damping

> Official exercise 10 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Consider the equation for a pendulum with a quadratic damping term

$$ \dot x = y, \qquad \dot y = -\sin x - ky|y|. $$

Show that if $E = \frac{1}{2}y^2 - \cos x$, then

$$ \frac{dE}{dt} = -ky^2|y|, $$

and hence that, while the point $(0, 0)$ is a center for the linearized equation, it behaves like a stable spiral for the nonlinear equation. Sketch the phase diagram for the latter.

## Setting up the system

First, we examine the quadratic aerodynamic drag term $-ky|y|$ ($k > 0$) and derive the exact energy dissipation rate $\frac{dE}{dt}$ term by term using the chain rule.

The autonomous first-order system is

$$ \dot x = f(x, y) = y, \qquad \dot y = g(x, y) = -\sin x - ky|y|, \qquad k > 0. $$

Note that $y|y|$ always has the same sign as $y$ (since $|y| \ge 0$), so $-ky|y|$ always opposes the angular velocity $y$, modelling turbulent aerodynamic drag proportional to the square of the speed.

For the mechanical energy $E(x, y) = \frac{1}{2}y^2 - \cos x$, we compute the partial derivatives explicitly:

$$ \frac{\partial E}{\partial x} = \sin x, \qquad \frac{\partial E}{\partial y} = y. $$

Differentiating $E(x(t), y(t))$ along any trajectory by the chain rule:

$$ \frac{dE}{dt} = \frac{\partial E}{\partial x}\dot x + \frac{\partial E}{\partial y}\dot y = (\sin x)\cdot y + y\cdot\bigl(-\sin x - ky|y|\bigr). $$

Expanding the product and cancelling the opposite terms $y\sin x$ and $-y\sin x$:

$$ \frac{dE}{dt} = y\sin x - y\sin x - ky^2|y| = -ky^2|y| \le 0. $$

This proves the required energy dissipation identity.

## Step 1: Critical points

Next, we find all equilibrium points by setting $\dot x = 0$ and $\dot y = 0$ simultaneously.

$$ \begin{cases} \dot x = y = 0, \\ \dot y = -\sin x - k\cdot 0\cdot |0| = -\sin x = 0 \implies x = m\pi, \quad m \in \mathbb{Z}. \end{cases} $$

As in Exercises 5.8 and 5.9, the equilibria are $(m\pi, 0)$ for $m \in \mathbb{Z}$ (even $m = 2n$ hanging downward; odd $m = 2n+1$ balanced upright).

## Step 2: Linearization

To compute the Jacobian matrix $J(x, y)$ rigorously, we first differentiate the non-polynomial function $\phi(y) = y|y|$ explicitly on all three domains ($y > 0$, $y < 0$, and $y = 0$).

Writing $\phi(y) = y|y|$ piecewise:

- For $y > 0$: $\phi(y) = y^2$, so $\phi'(y) = 2y = 2|y|$.
- For $y < 0$: $\phi(y) = -y^2$, so $\phi'(y) = -2y = 2|y|$.
- At $y = 0$: from the definition of the derivative,

$$ \phi'(0) = \lim_{h \to 0}\frac{\phi(h) - \phi(0)}{h} = \lim_{h \to 0}\frac{h|h| - 0}{h} = \lim_{h \to 0}|h| = 0 = 2|0|. $$

Therefore $\phi(y) = y|y|$ is continuously differentiable ($C^1$) everywhere on $\mathbb{R}$, with $\frac{d}{dy}(y|y|) = 2|y|$ for all $y \in \mathbb{R}$.

Computing all four partial derivatives of $f(x, y) = y$ and $g(x, y) = -\sin x - ky|y|$:

$$ \frac{\partial f}{\partial x} = 0, \qquad \frac{\partial f}{\partial y} = 1, \qquad \frac{\partial g}{\partial x} = -\cos x, \qquad \frac{\partial g}{\partial y} = -2k|y|. $$

Thus the Jacobian matrix at any point $(x, y)$ is

$$ J(x, y) = \begin{pmatrix} 0 & 1 \\ -\cos x & -2k|y| \end{pmatrix}. $$

At every equilibrium $(m\pi, 0)$, we have $y = 0$ so $-2k|0| = 0$: the quadratic damping vanishes completely from the linearization! Hence

$$ J(2n\pi,\, 0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad J\bigl((2n+1)\pi,\, 0\bigr) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}. $$

## Step 3: Local study

We now classify the linearized equilibria and then use the Lyapunov/energy function $E(x, y)$ to resolve the non-hyperbolic even equilibria.

### Odd equilibria: $((2n+1)\pi, 0)$ (balanced upright)

For $J((2n+1)\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, expanding the characteristic determinant gives

$$ \det\Bigl(J\bigl((2n+1)\pi, 0\bigr) - \lambda I\Bigr) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = (-\lambda)(-\lambda) - 1\cdot 1 = \lambda^2 - 1 = 0 \implies \lambda_1 = 1,\ \lambda_2 = -1. $$

Solving $(J - \lambda I)\mathbf v = \mathbf 0$ row by row: for $\lambda_1 = 1$, Row 1 gives $-v_x + v_y = 0 \implies \mathbf v_1 = (1, 1)^T$; for $\lambda_2 = -1$, Row 1 gives $v_x + v_y = 0 \implies \mathbf v_2 = (1, -1)^T$. Because $\lambda_1 > 0 > \lambda_2$, every odd equilibrium is **hyperbolic**, so the Hartman–Grobman theorem guarantees that each $((2n+1)\pi, 0)$ is a **saddle** in the nonlinear system, with local stable and unstable manifolds tangent to slopes $-1$ and $+1$.

### Even equilibria: $(2n\pi, 0)$ (in particular $(0, 0)$)

For $J(0, 0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the characteristic polynomial is

$$ \det\bigl(J(0, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -1 & -\lambda \end{pmatrix} = \lambda^2 + 1 = 0 \implies \lambda_\pm = \pm i. $$

Hence $(0, 0)$ is a **centre for the linearized system** $\dot x = y, \dot y = -x$. Because $\operatorname{Re}\lambda_\pm = 0$, $(0, 0)$ is **non-hyperbolic**: the Hartman–Grobman theorem does **not** apply, and nonlinear terms decide the true stability.

We now prove using $E(x, y) = \frac{1}{2}y^2 - \cos x$ (equivalently, the positive-definite Lyapunov function $V_L(x, y) = E(x, y) + 1 = \frac{1}{2}y^2 + (1 - \cos x)$) that $(0, 0)$ behaves like a **nonlinear stable spiral**:

1. **Strict local minimum:** On the open neighbourhood $|x| < \pi$, $V_L(0, 0) = 0$ and $V_L(x, y) = \frac{1}{2}y^2 + (1 - \cos x) > 0$ for all $(x, y) \neq (0, 0)$. Its level sets $E(x, y) = c$ ($-1 < c < 1$) are nested closed ovals surrounding $(0, 0)$.
2. **Strict energy decay along orbits:** Along any solution, $\dot V_L = \dot E = -ky^2|y| \le 0$, with $\dot E = 0$ if and only if $y = 0$. On the segment $y = 0$ with $0 < |x| < \pi$, the system gives $\dot y = -\sin x \neq 0$, so trajectories cross the $x$-axis vertically and can never remain on $y = 0$ except at $(0, 0)$. Therefore $E(t)$ decreases **strictly** along every non-equilibrium trajectory inside the well $-1 < E < 1$.
3. **Inward winding (nonlinear spiral):** Whenever $y \neq 0$, the trajectory crosses the closed $E$-contours strictly from outside to inside. Meanwhile, the vector field winds **clockwise** around $(0, 0)$ ($\dot x = y > 0$ for $y > 0$, $\dot x < 0$ for $y < 0$, $\dot y < 0$ for $x \in (0, \pi)$ and $y = 0$, $\dot y > 0$ for $x \in (-\pi, 0)$ and $y = 0$). By LaSalle's invariance principle, every trajectory starting with $E < 1$ and $|x| < \pi$ winds clockwise infinitely many times while approaching $E = -1$, i.e. $(x(t), y(t)) \to (0, 0)$ as $t \to +\infty$.

By $2\pi$-periodicity, every even equilibrium $(2n\pi, 0)$ is an asymptotically stable **nonlinear spiral** (also called a weak focus).

## Step 4: Global picture

Globally, the phase portrait shares the same topological structure as the underdamped linearly damped pendulum of Exercise 5.9, with two notable quantitative differences driven by the quadratic drag law $-ky|y|$:

- **Strong braking at high speeds:** For $|y| \gg 1$, $\bigl|y|y|\bigr| = y^2 \gg |y|$, so rotating trajectories lose energy much more rapidly than under linear damping and quickly drop below the saddle energy $E = 1$.
- **Very slow decay near $(2n\pi, 0)$:** As a trajectory approaches $(2n\pi, 0)$, $|y| \to 0$ and the drag force $ky^2$ becomes negligibly small compared to the linear restoring force $-x$. Consequently, the spiral turns become tightly packed near $(2n\pi, 0)$, with amplitude decaying **algebraically** ($O(1/t)$) rather than exponentially ($O(e^{-kt/2})$).
- **Basins of attraction:** Just as in Exercise 5.9, the stable manifolds of the saddles $((2n+1)\pi, 0)$ (now entering each saddle with exact slopes $\pm 1$, since $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ at $y = 0$) partition the entire phase plane into $2\pi$-periodic basins of attraction, one for each nonlinear stable spiral $(2n\pi, 0)$.

![[attachments/AM-PS/ch5-e10-quad-pendulum.svg]]
*Phase portrait of the pendulum with quadratic damping $\dot x = y$, $\dot y = -\sin x - ky|y|$ (Exercise 5.10). Nonlinear stable spirals at $(2n\pi, 0)$ (linear centres turned asymptotically stable by $\dot E = -ky^2|y| \le 0$), saddles at $((2n+1)\pi, 0)$ with tangent slopes $\pm 1$, and saddle stable manifolds separating the basins of attraction.*

## Answers and checks

We verify the undamped limit and dimensional consistency.

- **Undamped limit ($k \to 0^+$):** Setting $k = 0$ gives $\dot E = 0$, turning the tightly wound nonlinear spirals at $(2n\pi, 0)$ back into the true closed centres of Exercise 5.8 while leaving the saddle Jacobians at $((2n+1)\pi, 0)$ unchanged.
- **Dimensional check (SI units):** Restoring $\omega^2 = g/L$ ($\mathrm{s}^{-2}$) and the dimensionless quadratic drag constant $c_q$, the equation reads $\ddot\theta = -\omega^2\sin\theta - c_q\dot\theta|\dot\theta|$. Here $[\dot\theta|\dot\theta|] = (\mathrm{s}^{-1})^2 = \mathrm{s}^{-2} = [\ddot\theta]$, so $c_q$ (and therefore $k$ in $\omega = 1$ units) is **dimensionless** (proportional to $\frac{\rho_{\text{air}} C_D A L}{2m}$). The specific energy rate $\dot E = -c_q\dot\theta^2|\dot\theta|$ has units of $\mathrm{s}^{-3} = [E]/\mathrm{s}$.

> [!result] Key results
> - **Energy dissipation:** For $E(x, y) = \frac{1}{2}y^2 - \cos x$, $\dfrac{dE}{dt} = (\sin x)y + y(-\sin x - ky|y|) = -ky^2|y| \le 0$.
> - **Linearization:** Since $\frac{d}{dy}(y|y|) = 2|y|$, $J(x, y) = \begin{pmatrix} 0 & 1 \\ -\cos x & -2k|y| \end{pmatrix}$. At $(2n\pi, 0)$, $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ ($\lambda = \pm i$, **linear centre** — non-hyperbolic). At $((2n+1)\pi, 0)$, $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ ($\lambda = \pm 1$, $\mathbf v_\pm = (1, \pm 1)^T$, **saddles**).
> - **Nonlinear behaviour at $(0, 0)$:** $E(x, y)$ has a strict local minimum $E = -1$ at $(0, 0)$ and $\dot E = -ky^2|y| \le 0$ vanishes only on $y = 0$, where $\dot y = -\sin x \neq 0$ for $0 < |x| < \pi$. Hence $E$ decreases strictly along every non-equilibrium orbit, forcing trajectories to spiral clockwise into $(0, 0)$ (**nonlinear stable spiral** with algebraic decay as $y \to 0$).
