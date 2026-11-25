---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 6"
dificultad: media
id: "e6"
pill: "Damped motion in three potential wells"
tags:
  - problema-resuelto
  - advanced-maths
  - phase-plane
  - damping
  - lasalle
---

# Problem 5.6: Damped Motion in Three Potential Wells

> Official exercise 6 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Write down the equation of motion for a particle of unit mass moving in each of the potentials in Exercise 4 above, when there is an additional damping force $-\dot x$ (in part (i) take $\omega = 1$). Writing down a coupled system of equations for $x$ and $y = \dot x$, sketch the phase portrait for each case.

## Equation of Motion and Energy Dissipation

For a unit mass in a potential $V(x)$ with the extra force $-\dot x$, Newton's second law gives

$$\ddot x = -V'(x) - \dot x .$$

Setting $y = \dot x$ gives $\dot y = \ddot x$, so the coupled first order system is

$$\dot x = y, \qquad \dot y = -V'(x) - y .$$

The total energy is $E(x,y) = \tfrac12 y^2 + V(x)$. Its derivative along a trajectory follows from the chain rule, $\dot E = \frac{\partial E}{\partial x}\dot x + \frac{\partial E}{\partial y}\dot y$:

$$\dot E = V'(x)\,y + y\,\bigl(-V'(x) - y\bigr) = -y^2 \le 0 .$$

> [!info] Dissipation and the LaSalle argument
> $\dot E = -y^2$ vanishes only on the line $y = 0$. On that line the second equation gives $\dot y = -V'(x)$, so a trajectory can stay on $y=0$ only where $V'(x) = 0$, i.e. at an equilibrium. By LaSalle's invariance principle, every bounded trajectory therefore tends to an equilibrium. No periodic orbit exists, since one would need $\dot E \equiv 0$ along a closed curve, which forces $y \equiv 0$. Energy is lost, so the closed level curves of the conservative Exercise 4 open into spirals.

The Jacobian of the system at an equilibrium $(x^*, 0)$ with $V'(x^*) = 0$ is

$$J = \begin{pmatrix} 0 & 1 \\ -V''(x^*) & -1 \end{pmatrix}, \qquad \operatorname{tr} J = -1, \quad \det J = V''(x^*),$$

with characteristic equation $\lambda^2 + \lambda + V''(x^*) = 0$ and roots $\lambda = \dfrac{-1 \pm \sqrt{1 - 4V''(x^*)}}{2}$.
Source: `Notes03-05-Nov_v2.pdf`, linearisation about an equilibrium; Robinson, Sec. 34.

## Stationary Points and Linearisation

### (i) $V(x) = \tfrac12 x^2$ (with $\omega = 1$)

Here $V'(x) = x$ and $V''(x) = 1$, so $\ddot x = -x - \dot x$ and

$$\dot x = y, \qquad \dot y = -x - y .$$

The only equilibrium is $(0,0)$. With $V''(0) = 1$,

$$J = \begin{pmatrix} 0 & 1 \\ -1 & -1 \end{pmatrix}, \qquad \lambda^2 + \lambda + 1 = 0 \;\Rightarrow\; \lambda = \frac{-1 \pm \sqrt{1-4}}{2} = -\frac12 \pm i\frac{\sqrt3}{2}.$$

Complex roots with negative real part: $(0,0)$ is a **stable spiral**, and the system is linear, so the picture is global.

![[attachments/AM-PS/ch5-e6-i.svg]]
*Phase portrait of $\ddot x = -x - \dot x$: trajectories spiral clockwise into the origin.*

### (ii) $V(x) = \tfrac12 x^4 - x^2$

Here $V'(x) = 2x^3 - 2x = 2x(x-1)(x+1)$ and $V''(x) = 6x^2 - 2$. The system is

$$\dot x = y, \qquad \dot y = -2x^3 + 2x - y .$$

Equilibria: $y = 0$ and $2x(x^2-1) = 0$, so $(0,0)$ and $(\pm1, 0)$.

- **At $(0,0)$:** $V''(0) = -2$, so $J = \begin{pmatrix} 0 & 1 \\ 2 & -1 \end{pmatrix}$ and $\lambda^2 + \lambda - 2 = 0$, giving $\lambda = \dfrac{-1 \pm \sqrt{1+8}}{2} = \dfrac{-1\pm3}{2} = 1,\,-2$. Real roots of opposite sign: a **saddle**. The eigenvector of $\lambda = 1$ solves $-\lambda v_1 + v_2 = 0$, so $v = (1, 1)^T$ (unstable direction); for $\lambda=-2$, $v = (1,-2)^T$ (stable direction).
- **At $(\pm 1, 0)$:** $V''(\pm1) = 6 - 2 = 4$, so $J = \begin{pmatrix} 0 & 1 \\ -4 & -1 \end{pmatrix}$ and $\lambda^2 + \lambda + 4 = 0$, giving $\lambda = \dfrac{-1 \pm \sqrt{1-16}}{2} = -\frac12 \pm i\frac{\sqrt{15}}{2}$. Both are **stable spirals**.

![[attachments/AM-PS/ch5-e6-ii.svg]]
*Double-well case with damping: a saddle at the origin between two stable spirals. The stable manifold of the saddle separates the basins of $(1,0)$ and $(-1,0)$.*

### (iii) $V(x) = \tfrac12 x^6 - \tfrac54 x^4 + 2x^2$ (as printed on the sheet)

Here $V'(x) = 3x^5 - 5x^3 + 4x = x\,(3x^4 - 5x^2 + 4)$ and $V''(x) = 15x^4 - 15x^2 + 4$. Setting $u = x^2$, the factor $3u^2 - 5u + 4$ has discriminant $25 - 48 = -23 < 0$, so it has no real root: the only equilibrium is $(0,0)$. With $V''(0) = 4$,

$$J = \begin{pmatrix} 0 & 1 \\ -4 & -1 \end{pmatrix}, \qquad \lambda = -\frac12 \pm i\frac{\sqrt{15}}{2},$$

a **stable spiral**. Since $V$ has a single global minimum and $V\to\infty$ as $|x|\to\infty$, LaSalle gives that every trajectory spirals into the origin.

![[attachments/AM-PS/ch5-e6-iii-sheet.svg]]
*Phase portrait for the potential as printed on the sheet: one stable spiral at the origin.*

> [!warning] Possible misprint in the official sheet (vs Robinson Ex. 34.1(iii))
> Robinson's exercise uses $V(x) = \tfrac16 x^6 - \tfrac54 x^4 + 2x^2$ (Robinson, Ex. 34.1(iii)); the sheet prints $\tfrac12 x^6$. With the coefficient $\tfrac16$ the potential has several wells, which matches the "three wells" wording of Exercise 4. We solve the printed version above and the Robinson version here; the sheet's answer is the computed one.
>
> $V'(x) = x^5 - 5x^3 + 4x = x(x^4 - 5x^2 + 4) = x(x^2-1)(x^2-4)$, so the equilibria are $x = 0, \pm1, \pm2$, and $V''(x) = 5x^4 - 15x^2 + 4$.
>
> | Equilibrium | $V''$ | $\lambda^2 + \lambda + V'' = 0$ | Type |
> | :--- | :--- | :--- | :--- |
> | $(0,0)$ | $4$ | $\lambda = -\frac12 \pm i\frac{\sqrt{15}}{2}$ | stable spiral |
> | $(\pm1,0)$ | $5 - 15 + 4 = -6$ | $\lambda = \frac{-1\pm5}{2} = 2,\,-3$ | saddle |
> | $(\pm2,0)$ | $80 - 60 + 4 = 24$ | $\lambda = -\frac12 \pm i\frac{\sqrt{95}}{2}$ | stable spiral |

![[attachments/AM-PS/ch5-e6-iii-robinson.svg]]
*Robinson's potential: three wells (stable spirals at $0$ and $\pm2$) separated by saddles at $\pm1$.*

## Phase Portrait and Physical Interpretation

In every case $\dot E = -y^2 \le 0$: the particle loses mechanical energy to friction, so it ends at rest at a local minimum of $V$ (a stable spiral or, for a stronger damping, node). Local maxima of $V$ (the saddles) are reached only along their stable manifolds, which act as separatrices between the basins of attraction of different wells. The spiralling comes from $\operatorname{Im}\lambda \ne 0$, i.e. $1 - 4V'' < 0$ (underdamped oscillation about the minimum); the motion is clockwise since $\dot x = y$.

> [!result] Summary
> | Case | Equilibria | Classification |
> | :--- | :--- | :--- |
> | (i) $\tfrac12x^2$ | $(0,0)$ | stable spiral, $\lambda=-\frac12\pm i\frac{\sqrt3}{2}$ |
> | (ii) $\tfrac12x^4-x^2$ | $(0,0)$; $(\pm1,0)$ | saddle ($\lambda=1,-2$); stable spirals ($-\frac12\pm i\frac{\sqrt{15}}{2}$) |
> | (iii) sheet | $(0,0)$ | stable spiral |
> | (iii) Robinson | $0,\pm1,\pm2$ | spirals at $0,\pm2$; saddles at $\pm1$ |
>
> Dimensional check (unit mass, unit damping rate $c/m = 1\,\mathrm{T^{-1}}$): $[E] = [y^2] = \mathrm{L^2 T^{-2}}$ (energy per unit mass) and $[\dot E] = [(c/m)y^2] = \mathrm{L^2 T^{-3}}$ in the nondimensional units of the sheet, consistent with $\dot E = -y^2$.
