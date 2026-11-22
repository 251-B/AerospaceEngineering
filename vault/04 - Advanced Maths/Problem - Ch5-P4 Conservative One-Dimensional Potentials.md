---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 4"
dificultad: media
id: "e4"
pill: "Conservative Systems • Energy Curves • Double Well"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.4: Conservative One-Dimensional Potentials

> Official exercise 4 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

For the following choices of potential functions $V(x)$, write down the total energy for a particle of unit mass, and assuming that this is conserved write down a coupled system of equations for $x$ and $y = \dot x$. Sketch the phase portrait and interpret the dynamics in each case.

(i) $V(x) = \frac{1}{2}\omega^2 x^2$,

(ii) $V(x) = \frac{1}{2}x^4 - x^2$,

(iii) $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$.

## Setting up the system

We derive the coupled first-order system from conservation of mechanical energy for a particle of unit mass ($m = 1$) moving in a one-dimensional potential $V(x)$, and then write out the explicit energy and equations for each of the three potentials.

The total mechanical energy is the sum of kinetic energy $\frac{1}{2}\dot x^2$ and potential energy $V(x)$:

$$
E(x, \dot x) = \frac{1}{2}\dot x^2 + V(x).
$$

Assuming $E$ is conserved along every trajectory ($\dot E = 0$), differentiate with respect to $t$ using the chain rule:

$$
\frac{dE}{dt} = \frac{1}{2}(2\dot x\ddot x) + V'(x)\dot x = \dot x\bigl(\ddot x + V'(x)\bigr) = 0.
$$

For any non-stationary motion ($\dot x \not\equiv 0$), this forces Newton's equation $\ddot x = -V'(x)$ (which also holds at equilibria where $\dot x = 0$ and $V'(x) = 0$). Introducing the velocity variable $y = \dot x$ converts this second-order ODE into the planar conservative system

$$
\dot x = y, \qquad \dot y = -V'(x),
$$

whose trajectories lie on the constant-energy level curves $\frac{1}{2}y^2 + V(x) = E$, i.e. $y = \pm\sqrt{2\bigl(E - V(x)\bigr)}$. Every phase portrait is therefore symmetric about the $x$-axis, with motion to the right in the upper half-plane ($y > 0 \implies \dot x > 0$) and to the left in the lower half-plane ($y < 0 \implies \dot x < 0$).

### (i) Harmonic potential $V(x) = \frac{1}{2}\omega^2 x^2$ ($\omega > 0$)

Here $V'(x) = \omega^2 x$, so the conserved energy and coupled system are

$$
E(x,y) = \frac{1}{2}y^2 + \frac{1}{2}\omega^2 x^2, \qquad \dot x = y, \qquad \dot y = -\omega^2 x.
$$

### (ii) Double-well potential $V(x) = \frac{1}{2}x^4 - x^2$

Here $V'(x) = 2x^3 - 2x = 2x(x^2 - 1)$, so the conserved energy and coupled system are

$$
E(x,y) = \frac{1}{2}y^2 + \frac{1}{2}x^4 - x^2, \qquad \dot x = y, \qquad \dot y = -2x^3 + 2x = -2x(x^2 - 1).
$$

### (iii) Sextic potential $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$

Here $V'(x) = 3x^5 - 5x^3 + 4x = x(3x^4 - 5x^2 + 4)$, so the conserved energy and coupled system are

$$
E(x,y) = \frac{1}{2}y^2 + \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2, \qquad \dot x = y, \qquad \dot y = -3x^5 + 5x^3 - 4x = -x(3x^4 - 5x^2 + 4).
$$

## Step 1: Critical points

We find all stationary points $(x^*, y^*) \in \mathbb{R}^2$ by setting $\dot x = y = 0$ and $\dot y = -V'(x) = 0$. All critical points therefore lie on the $x$-axis at the stationary points of the potential $V(x)$.

### (i) Harmonic potential

Setting $y = 0$ and $-\omega^2 x = 0$ (with $\omega \neq 0$) gives a single stationary point:

$$
(x^*, y^*) = (0, 0).
$$

### (ii) Double-well potential

Setting $y = 0$ and $-2x(x^2 - 1) = -2x(x - 1)(x + 1) = 0$ gives three stationary points:

$$
(0, 0), \qquad (1, 0), \qquad (-1, 0).
$$

### (iii) Sextic potential

Setting $y = 0$ and $-x(3x^4 - 5x^2 + 4) = 0$ gives either $x = 0$ or $3x^4 - 5x^2 + 4 = 0$. Letting $u = x^2 \ge 0$, the quadratic equation $3u^2 - 5u + 4 = 0$ has discriminant

$$
\Delta = (-5)^2 - 4(3)(4) = 25 - 48 = -23 < 0.
$$

Hence $3x^4 - 5x^2 + 4 > 0$ has no real roots, and the system has **only one real critical point**:

$$
(x^*, y^*) = (0, 0).
$$

> [!warning] Sheet erratum vs Robinson Ex. 34.1 (iii)
> The official sheet `probls_ch5_2627.pdf` prints $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$, which has a single real equilibrium at $(0,0)$ because $3x^4 - 5x^2 + 4$ has negative discriminant $\Delta = -23$. In Robinson (*An Introduction to Ordinary Differential Equations*, Ex. 34.1(iii), p. 350), the leading coefficient is $\frac{1}{6}$ rather than $\frac{1}{2}$: $V(x) = \frac{1}{6}x^6 - \frac{5}{4}x^4 + 2x^2$, for which $V'(x) = x(x^4 - 5x^2 + 4) = x(x^2 - 1)(x^2 - 4)$ yields **five** critical points at $x = 0, \pm 1, \pm 2$ (a triple-well potential with centres at $0, \pm 2$ and saddles at $\pm 1$). Below we solve the exact potential printed on the UC3M sheet.

## Step 2: Linearization

We compute the Jacobian matrix $J(x,y)$ for any conservative system $\dot x = y$, $\dot y = -V'(x)$ and evaluate it at every critical point.

Since $f(x,y) = y$ and $g(x,y) = -V'(x)$:

$$
\frac{\partial f}{\partial x} = 0, \qquad \frac{\partial f}{\partial y} = 1, \qquad \frac{\partial g}{\partial x} = -V''(x), \qquad \frac{\partial g}{\partial y} = 0,
$$

so

$$
J(x,y) = \begin{pmatrix} 0 & 1 \\ -V''(x) & 0 \end{pmatrix}.
$$

### (i) Harmonic potential

Here $V''(x) = \omega^2$, so at $(0,0)$:

$$
J(0,0) = \begin{pmatrix} 0 & 1 \\ -\omega^2 & 0 \end{pmatrix}.
$$

### (ii) Double-well potential

Here $V''(x) = 6x^2 - 2$. Evaluating at $(0,0)$ and $(\pm 1, 0)$ (following `Notes03-05-Nov_v2.pdf`, pp. 15–16):

$$
J(0,0) = \begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}, \qquad J(\pm 1, 0) = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}.
$$

### (iii) Sextic potential

Here $V''(x) = 15x^4 - 15x^2 + 4$. Evaluating at $(0,0)$ gives $V''(0) = 4$:

$$
J(0,0) = \begin{pmatrix} 0 & 1 \\ -4 & 0 \end{pmatrix}.
$$

## Step 3: Local study

We compute the eigenvalues and eigenvectors of $J(x^*, 0)$ row by row at each stationary point. Note that for a conservative system, a linearized centre at a strict local minimum of $V(x)$ is automatically a **true nonlinear centre**, because $E(x,y) = \frac{1}{2}y^2 + V(x)$ has a strict local minimum there and its level sets form closed loops around $(x^*, 0)$.

### (i) Harmonic potential

Characteristic equation at $(0,0)$:

$$
\det\begin{pmatrix} -\lambda & 1 \\ -\omega^2 & -\lambda \end{pmatrix} = \lambda^2 + \omega^2 = 0 \;\Longrightarrow\; \lambda_\pm = \pm i\omega.
$$

For $\lambda_+ = i\omega$, solve $(J(0,0) - i\omega I)\vec\eta_+ = \vec 0$:

$$
\begin{pmatrix} -i\omega & 1 \\ -\omega^2 & -i\omega \end{pmatrix}\begin{pmatrix} \eta_1 \\ \eta_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.
$$

Row 1 gives $-i\omega\eta_1 + \eta_2 = 0 \implies \eta_2 = i\omega\eta_1$ (Row 2 gives $-\omega^2\eta_1 - i\omega(i\omega\eta_1) = 0$, consistent). Choosing $\eta_1 = 1$ gives $\vec\eta_+ = \begin{pmatrix} 1 \\ i\omega \end{pmatrix}$. Since the system is already linear, $(0,0)$ is an exact **centre**.

### (ii) Double-well potential

- **At $(0,0)$:** Characteristic equation:
  $$
  \det\begin{pmatrix} -\lambda & 1 \\ 2 & -\lambda \end{pmatrix} = \lambda^2 - 2 = 0 \;\Longrightarrow\; \lambda_\pm = \pm\sqrt{2}.
  $$
  Solving $(J(0,0) - \lambda_\pm I)\vec v_\pm = \vec 0$:
  $$
  \begin{pmatrix} \mp\sqrt{2} & 1 \\ 2 & \mp\sqrt{2} \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.
  $$
  Row 1 gives $\mp\sqrt{2}v_1 + v_2 = 0 \implies v_2 = \pm\sqrt{2}v_1$ (Row 2 gives $2v_1 \mp \sqrt{2}(\pm\sqrt{2}v_1) = 0$, consistent). Choosing $v_1 = \pm\sqrt{2}$ yields $\vec v_\pm = \begin{pmatrix} \pm\sqrt{2} \\ 2 \end{pmatrix}$. Because $\lambda_+ > 0 > \lambda_-$, $(0,0)$ is a **saddle point**.

- **At $(\pm 1, 0)$:** Characteristic equation:
  $$
  \det\begin{pmatrix} -\lambda & 1 \\ -4 & -\lambda \end{pmatrix} = \lambda^2 + 4 = 0 \;\Longrightarrow\; \lambda_\pm = \pm 2i.
  $$
  Solving $(J(\pm 1, 0) - (\pm 2i)I)\vec\eta_\pm = \vec 0$:
  $$
  \begin{pmatrix} \mp 2i & 1 \\ -4 & \mp 2i \end{pmatrix}\begin{pmatrix} \eta_1 \\ \eta_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.
  $$
  Row 1 gives $\mp 2i\eta_1 + \eta_2 = 0 \implies \eta_2 = \pm 2i\eta_1$ (Row 2 consistent). Choosing $\eta_1 = \pm i$ gives $\eta_2 = -2$, so
  $$
  \vec\eta_\pm = \begin{pmatrix} \pm i \\ -2 \end{pmatrix} = \begin{pmatrix} 0 \\ -2 \end{pmatrix} \pm i\begin{pmatrix} 1 \\ 0 \end{pmatrix}.
  $$
  Both $(\pm 1, 0)$ are **linearized centres**; because $V(\pm 1) = -\frac{1}{2}$ are strict local minima of $V(x)$ ($V''(\pm 1) = 4 > 0$), the closed energy contours confirm that both are **true nonlinear centres**.

### (iii) Sextic potential

Characteristic equation at $(0,0)$:

$$
\det\begin{pmatrix} -\lambda & 1 \\ -4 & -\lambda \end{pmatrix} = \lambda^2 + 4 = 0 \;\Longrightarrow\; \lambda_\pm = \pm 2i.
$$

As in part (ii), the complex eigenvectors are $\vec\eta_\pm = \begin{pmatrix} \pm i \\ -2 \end{pmatrix}$. Because $V'(x) = x(3x^4 - 5x^2 + 4)$ has the same sign as $x$ everywhere on $\mathbb{R}$, $V(x)$ has a **strict global minimum** at $x = 0$ with $V(0) = 0$. Therefore $(0,0)$ is a **true nonlinear centre**.

## Step 4: Global picture

We trace the constant-energy curves $y = \pm\sqrt{2(E - V(x))}$ across all energy levels $E$ and interpret the physical motion of the particle.

### (i) Simple harmonic oscillations

For every $E > 0$, the level curve $\frac{1}{2}y^2 + \frac{1}{2}\omega^2 x^2 = E$ is the ellipse

$$
\frac{x^2}{2E/\omega^2} + \frac{y^2}{2E} = 1,
$$

traversed **clockwise** (since $\dot x = y > 0$ in the upper half-plane). Physically, the particle executes periodic simple harmonic oscillations about $x = 0$ with amplitude $A = \sqrt{2E}/\omega$ and constant period $T = 2\pi/\omega$ independent of energy.

![[attachments/AM-PS/ch5-e4-i.svg]]
*Phase portrait of the harmonic potential $V(x) = \frac{1}{2}\omega^2 x^2$ (drawn with $\omega = 1$): concentric clockwise ellipses around the centre $(0,0)$.*

### (ii) Double-well dynamics and homoclinic separatrix

The potential $V(x) = \frac{1}{2}x^4 - x^2$ has two symmetric minima at $x = \pm 1$ with depth $V(\pm 1) = -\frac{1}{2}$, separated by a central barrier of height $V(0) = 0$:

- **$E = -\frac{1}{2}$:** The particle sits at rest at the bottom of either potential well, $(-1, 0)$ or $(1, 0)$.
- **$-\frac{1}{2} < E < 0$ (low-energy trapped oscillations):** The particle lacks enough energy to cross the central barrier at $x = 0$; trajectories form two disjoint families of closed clockwise orbits oscillating inside either the left well ($x < 0$) or the right well ($x > 0$).
- **$E = 0$ (figure-eight separatrix):** The level curve $\frac{1}{2}y^2 + \frac{1}{2}x^4 - x^2 = 0$ simplifies to $y = \pm x\sqrt{2 - x^2}$, forming two homoclinic loops that leave and return to the saddle $(0,0)$ in infinite time, with turning points at $x = \pm\sqrt{2}$.
- **$E > 0$ (high-energy oscillations):** The particle overcomes the central barrier and executes large periodic clockwise oscillations enclosing both wells and the saddle.

![[attachments/AM-PS/ch5-e4-ii.svg]]
*Phase portrait of the double-well potential $V(x) = \frac{1}{2}x^4 - x^2$: two nonlinear centres at $(\pm 1, 0)$, a saddle at $(0,0)$, the $E = 0$ figure-eight homoclinic separatrix, and high-energy orbits for $E > 0$.*

### (iii) Single-well anharmonic oscillations

Because $V'(x) = x(3x^4 - 5x^2 + 4)$ vanishes only at $x = 0$ and $V(x) \to +\infty$ as $|x| \to \infty$, the potential $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$ is a single symmetric well (with slight flattening near the inflection region where $V''(x) = 15x^4 - 15x^2 + 4$ dips to its minimum value $4 - 15/4 = 1/4 > 0$ at $x^2 = 1/2$, so $V$ is in fact strictly convex everywhere!). Consequently, every energy level $E > 0$ produces a single closed clockwise periodic orbit enclosing $(0,0)$: **every non-stationary trajectory is a bounded, periodic anharmonic oscillation about the origin**.

![[attachments/AM-PS/ch5-e4-iii.svg]]
*Phase portrait of the sheet potential $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$: globally nested clockwise periodic orbits around the unique nonlinear centre $(0,0)$.*

## Answers and checks

- **Check against the lecturer's solution (`Notes03-05-Nov_v2.pdf`, pp. 15–17):** Part (ii) matches the class notes verbatim: $\dot x = y$, $\dot y = -2x^3 + 2x$, saddle $(0,0)$ with $\lambda_\pm = \pm\sqrt{2}$ and $\vec v_\pm = (\pm\sqrt{2}, 2)^T$, centres $(\pm 1, 0)$ with $\lambda_\pm = \pm 2i$ and $\vec\eta_\pm = (\pm i, -2)^T$, figure-eight separatrix at $E = 0$, and low-/high-energy regimes.
- **Check against Robinson (Ex. 34.1):** Parts (i) and (ii) agree identically with Robinson, Ex. 34.1; the sheet erratum in part (iii) ($\frac{1}{2}x^6$ vs Robinson's $\frac{1}{6}x^6$) is documented in the warning callout above.
- **Dimensional consistency:** For a particle of unit mass ($m = 1\;\text{kg}$), $[x] = \text{m}$, $[y] = [\dot x] = \text{m}\,\text{s}^{-1}$, $[E] = [V] = \text{m}^2\,\text{s}^{-2}$ (energy per unit mass), $[V'(x)] = \text{m}\,\text{s}^{-2} = [\dot y]$, and $[V''(x)] = \text{s}^{-2}$, so $\lambda_\pm = \pm\sqrt{-V''(x^*)}$ has dimension $\text{s}^{-1}$.

> [!result] Key results
> - **Conservative system:** $E = \frac{1}{2}y^2 + V(x)$ conserved $\implies \dot x = y$, $\dot y = -V'(x)$.
> - **(i) $V(x) = \frac{1}{2}\omega^2 x^2$:** $\dot x = y, \dot y = -\omega^2 x$; unique centre $(0,0)$ ($\lambda_\pm = \pm i\omega$); concentric clockwise ellipses $y^2 + \omega^2 x^2 = 2E$.
> - **(ii) $V(x) = \frac{1}{2}x^4 - x^2$:** $\dot x = y, \dot y = -2x(x^2-1)$; saddle $(0,0)$ ($\lambda_\pm = \pm\sqrt{2}$) and nonlinear centres $(\pm 1, 0)$ ($\lambda_\pm = \pm 2i$); figure-eight separatrix at $E = 0$ separating trapped well oscillations ($-\frac{1}{2} < E < 0$) from global oscillations ($E > 0$).
> - **(iii) $V(x) = \frac{1}{2}x^6 - \frac{5}{4}x^4 + 2x^2$:** $\dot x = y, \dot y = -x(3x^4 - 5x^2 + 4)$; unique real critical point $(0,0)$ ($\lambda_\pm = \pm 2i$, global nonlinear centre) since $\Delta = -23 < 0$; all trajectories with $E > 0$ are bounded clockwise periodic oscillations.
