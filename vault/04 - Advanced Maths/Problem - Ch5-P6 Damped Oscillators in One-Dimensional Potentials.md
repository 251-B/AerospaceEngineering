---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Damped Oscillators • Basins of Attraction"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.6: Damped Oscillators in One-Dimensional Potentials

> Official exercise 6 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Write down the equation of motion for a particle of unit mass moving in each of the potentials in Exercise 4 above, when there is an additional damping force $-\dot x$ (in part (i) take $\omega = 1$). Writing down a coupled system of equations for $x$ and $y = \dot x$, sketch the phase portrait for each case.

## Setting up the system

First, we write Newton's second law with both the conservative force $-V'(x)$ and the linear damping force $-\dot x$, convert it to a first-order system, and compute the rate of change of the mechanical energy $E$.

For a particle of unit mass ($m = 1$) in a potential $V(x)$ subject to a linear damping force $-\dot x$, Newton's second law gives

$$ \ddot x = -V'(x) - \dot x. $$

Setting $y = \dot x$ produces the coupled first-order system

$$ \dot x = f(x, y) = y, \qquad \dot y = g(x, y) = -V'(x) - y. $$

The mechanical energy of the undamped system is $E(x, y) = \frac{1}{2}y^2 + V(x)$. Differentiating $E(x(t), y(t))$ along any solution by the chain rule:

$$ \frac{dE}{dt} = \frac{\partial E}{\partial x}\dot x + \frac{\partial E}{\partial y}\dot y = V'(x)\cdot y + y\cdot\bigl(-V'(x) - y\bigr) = V'(x)y - V'(x)y - y^2 = -y^2 \le 0. $$

Thus $E$ is non-increasing along every trajectory, and $\dot E = 0$ only on the $x$-axis ($y = 0$). Whenever $y = 0$ and $V'(x) \neq 0$, we have $\dot y = -V'(x) \neq 0$, so trajectories cross the $x$-axis vertically without remaining on it. Consequently, $E(t)$ decreases strictly along every non-equilibrium orbit: **no closed orbits (periodic solutions) can exist** in any of the three cases.

Writing out the explicit system for each potential of Exercise 5.4:

- **Part (i):** $V(x) = \frac{1}{2}x^2$ (taking $\omega = 1$), $V'(x) = x$, $V''(x) = 1$:

$$ \dot x = y, \qquad \dot y = -x - y. $$

- **Part (ii):** $V(x) = \frac{1}{2}x^4 - x^2$, $V'(x) = 2x^3 - 2x = 2x(x^2 - 1)$, $V''(x) = 6x^2 - 2$:

$$ \dot x = y, \qquad \dot y = -2x^3 + 2x - y. $$

- **Part (iii):** $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$ (the potential printed on the official sheet), $V'(x) = 3x^5 - 5x^3 + 4x = x(3x^4 - 5x^2 + 4)$, $V''(x) = 15x^4 - 15x^2 + 4$:

$$ \dot x = y, \qquad \dot y = -3x^5 + 5x^3 - 4x - y. $$

## Step 1: Critical points

Next, we find all equilibria by setting $\dot x = 0$ and $\dot y = 0$ simultaneously.

Setting $\dot x = y = 0$ and substituting into $\dot y = -V'(x) - y = 0$ gives $V'(x) = 0$. Damping does not shift the positions of the critical points:

- **Part (i):** $x = 0 \implies$ unique equilibrium $(0, 0)$.
- **Part (ii):** $2x(x^2 - 1) = 0 \implies$ three equilibria: $(-1, 0)$, $(0, 0)$, and $(1, 0)$.
- **Part (iii):** $x(3x^4 - 5x^2 + 4) = 0$. Setting $u = x^2 \ge 0$, the quadratic $3u^2 - 5u + 4 = 0$ has discriminant $\Delta = (-5)^2 - 4(3)(4) = 25 - 48 = -23 < 0$, so it has no real roots. Thus the unique equilibrium is $(0, 0)$.

*(Note: in Robinson's textbook, Exercise 34.1(iii) uses $V(x) = \frac{1}{6}x^6 - \frac{5}{4}x^4 + 2x^2$, whose derivative $x(x^2 - 1)(x^2 - 4)$ gives five equilibria at $x \in \{0, \pm 1, \pm 2\}$. Here we solve the official sheet potential $\frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$ and comment on Robinson's triple-well variant at the end.)*

## Step 2: Linearization

We compute the Jacobian matrix $J(x, y)$ in general and evaluate it at every equilibrium $(x^*, 0)$.

Differentiating $f(x, y) = y$ and $g(x, y) = -V'(x) - y$:

$$ \frac{\partial f}{\partial x} = 0, \qquad \frac{\partial f}{\partial y} = 1, \qquad \frac{\partial g}{\partial x} = -V''(x), \qquad \frac{\partial g}{\partial y} = -1. $$

Hence at any critical point $(x^*, 0)$,

$$ J(x^*, 0) = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -1 \end{pmatrix}. $$

Its characteristic polynomial is

$$ \det\bigl(J(x^*, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -V''(x^*) & -1 - \lambda \end{pmatrix} = (-\lambda)(-1 - \lambda) - (-V''(x^*)) = \lambda^2 + \lambda + V''(x^*) = 0, $$

with roots

$$ \lambda_\pm = \frac{-1 \pm \sqrt{1 - 4V''(x^*)}}{2}. $$

## Step 3: Local study

We now evaluate $\lambda_\pm$ (and eigenvectors where real) at every critical point of parts (i), (ii), and (iii).

### Part (i): $V(x) = \frac{1}{2}x^2$ at $(0, 0)$

Here $V''(0) = 1$, so $J(0, 0) = \begin{pmatrix} 0 & 1 \\ -1 & -1 \end{pmatrix}$ and

$$ \lambda^2 + \lambda + 1 = 0 \implies \lambda_\pm = \frac{-1 \pm \sqrt{1 - 4}}{2} = \frac{-1 \pm i\sqrt{3}}{2}. $$

Since $\operatorname{Re}\lambda_\pm = -\frac{1}{2} < 0$ and $\operatorname{Im}\lambda_\pm \neq 0$, $(0, 0)$ is a **stable spiral** (underdamped linear harmonic oscillator). At $(0, 1)$, $\dot x = 1 > 0$, so trajectories wind **clockwise** into the origin.

### Part (ii): $V(x) = \frac{1}{2}x^4 - x^2$

- **At $(0, 0)$:** $V''(0) = -2$, so $J(0, 0) = \begin{pmatrix} 0 & 1 \\ 2 & -1 \end{pmatrix}$. Characteristic equation:

$$ \lambda^2 + \lambda - 2 = (\lambda - 1)(\lambda + 2) = 0 \implies \lambda_1 = 1, \quad \lambda_2 = -2. $$

Row-by-row eigenvectors:
- For $\lambda_1 = 1$: $(J - I)\mathbf v_1 = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies -v_x + v_y = 0 \implies \mathbf v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ (unstable manifold, slope $+1$).
- For $\lambda_2 = -2$: $(J + 2I)\mathbf v_2 = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies 2v_x + v_y = 0 \implies \mathbf v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$ (stable manifold, slope $-2$).

Since $\lambda_1 = 1 > 0 > -2 = \lambda_2$, $(0, 0)$ is a hyperbolic **saddle**.

- **At $(-1, 0)$ and $(1, 0)$:** $V''(\pm 1) = 6(\pm 1)^2 - 2 = 4$, so $J(\pm 1, 0) = \begin{pmatrix} 0 & 1 \\ -4 & -1 \end{pmatrix}$. Characteristic equation:

$$ \lambda^2 + \lambda + 4 = 0 \implies \lambda_\pm = \frac{-1 \pm \sqrt{1 - 16}}{2} = \frac{-1 \pm i\sqrt{15}}{2}. $$

Since $\operatorname{Re}\lambda_\pm = -\frac{1}{2} < 0$, both $(-1, 0)$ and $(1, 0)$ are hyperbolic **stable spirals** (clockwise, since $\dot x = y > 0$ above the $x$-axis).

### Part (iii): $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$ at $(0, 0)$

Here $V''(0) = 4$, so $J(0, 0) = \begin{pmatrix} 0 & 1 \\ -4 & -1 \end{pmatrix}$ and

$$ \lambda^2 + \lambda + 4 = 0 \implies \lambda_\pm = \frac{-1 \pm \sqrt{1 - 16}}{2} = \frac{-1 \pm i\sqrt{15}}{2}. $$

Thus $(0, 0)$ is a hyperbolic **stable spiral** (clockwise).

## Step 4: Global picture

Using the energy dissipation $\dot E = -y^2 \le 0$ and the fact that $V(x) \to +\infty$ as $|x| \to \infty$ in all three cases, every trajectory remains bounded and must approach an equilibrium point as $t \to +\infty$.

- **Part (i):** Every trajectory spirals clockwise into the unique equilibrium $(0, 0)$, which is globally asymptotically stable.

![[attachments/AM-PS/ch5-e6-i.svg]]
*Phase portrait of the damped harmonic oscillator $\dot x = y$, $\dot y = -x - y$ (Exercise 5.6(i)). All trajectories spiral clockwise into the globally attracting stable spiral at $(0, 0)$.*

- **Part (ii):** The two branches of the **stable manifold** of the saddle $(0, 0)$ (entering $(0, 0)$ tangent to $\mathbf v_2 = (1, -2)^T$) wind backward in time out to infinity as a double spiral. They act as a **separatrix** dividing the entire phase plane into two **basins of attraction**:
  - Initial conditions in the left basin spiral into the stable spiral $(-1, 0)$;
  - Initial conditions in the right basin spiral into the stable spiral $(1, 0)$;
  - Only initial conditions lying precisely on the one-dimensional stable manifold of $(0, 0)$ converge to the hilltop equilibrium $(0, 0)$.
  - The two branches of the unstable manifold of $(0, 0)$ (leaving tangent to $\mathbf v_1 = (1, 1)^T$) fall into the right well $(1, 0)$ and the left well $(-1, 0)$, respectively.

![[attachments/AM-PS/ch5-e6-ii.svg]]
*Phase portrait of the damped double-well oscillator $\dot x = y$, $\dot y = -2x^3 + 2x - y$ (Exercise 5.6(ii)). The stable manifold of the saddle $(0, 0)$ (slope $-2$) separates the basins of attraction of the two stable spirals at $(-1, 0)$ and $(1, 0)$.*

- **Part (iii):** Because $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2 \ge 0$ has $(0, 0)$ as its unique critical point and $E(x, y) \to +\infty$ as $x^2 + y^2 \to \infty$, $(0, 0)$ is a **global attractor**: every trajectory in the phase plane spirals clockwise into $(0, 0)$, slowed slightly near the inflection regions where $V'(x)$ is small. *(In Robinson's $\frac{1}{6}x^6$ triple-well variant, the centres at $0, \pm 2$ become three stable spirals and the saddles at $\pm 1$ carry stable manifolds that partition the plane into three basins of attraction.)*

![[attachments/AM-PS/ch5-e6-iii.svg]]
*Phase portrait of the damped sextic oscillator $\dot x = y$, $\dot y = -3x^5 + 5x^3 - 4x - y$ (Exercise 5.6(iii)). All trajectories spiral clockwise into the unique global attractor $(0, 0)$.*

## Answers and checks

We verify the physical units and the zero-damping limit.

- **Dimensional check (SI units):** Restoring mass $m$ ($\mathrm{kg}$) and linear damping coefficient $c$ ($\mathrm{N\cdot s\,m^{-1}} = \mathrm{kg\,s^{-1}}$), the equation reads $m\ddot x = -V'(x) - c\dot x$. Each term has units of force ($\mathrm{N} = \mathrm{kg\,m\,s^{-2}}$), and the energy dissipation rate $\dot E = -c\dot x^2$ has units of power ($\mathrm{W} = \mathrm{J\,s^{-1}} = \mathrm{kg\,m^2\,s^{-3}}$). Setting $m = 1$ and $c = 1$ recovers $\dot E = -y^2$.
- **Consistency check with Exercise 5.4:** Removing the damping term ($-y \to 0$) sets $\operatorname{tr} J = 0$, turning every stable spiral ($\lambda_\pm = \frac{-1 \pm i\sqrt{4V''-1}}{2}$) back into a centre ($\lambda_\pm = \pm i\sqrt{V''}$) and restoring the symmetric saddle slopes $\pm\sqrt{2}$ at $(0, 0)$ in part (ii).

> [!result] Key results
> - **General damped system & energy law:** $\dot x = y$, $\dot y = -V'(x) - y$, with $\dot E = -y^2 \le 0$ (no periodic orbits).
> - **Part (i) ($V = \frac{1}{2}x^2$):** $(0, 0)$ is a globally attracting stable spiral, $\lambda_\pm = \frac{-1 \pm i\sqrt{3}}{2}$.
> - **Part (ii) ($V = \frac{1}{2}x^4 - x^2$):** $(0, 0)$ is a saddle ($\lambda_1 = 1$, $\mathbf v_1 = (1, 1)^T$; $\lambda_2 = -2$, $\mathbf v_2 = (1, -2)^T$); $(\pm 1, 0)$ are stable spirals ($\lambda_\pm = \frac{-1 \pm i\sqrt{15}}{2}$). The stable manifold of $(0, 0)$ separates the two basins of attraction.
> - **Part (iii) ($V = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$):** $(0, 0)$ is the unique equilibrium and a globally attracting stable spiral, $\lambda_\pm = \frac{-1 \pm i\sqrt{15}}{2}$.
