---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 10"
dificultad: media
id: "e10"
pill: "Quadratic damping and Lyapunov stability"
tags:
  - problema-resuelto
  - advanced-maths
  - phase-plane
  - pendulum
  - lyapunov
  - lasalle
---

# Problem 5.10: Quadratically Damped Pendulum and Lyapunov Stability

> Official exercise 10 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Consider the equation for a pendulum with a quadratic damping term $\dot x = y$, $\dot y = -\sin x - ky|y|$. Show that if $E = \tfrac12 y^2 - \cos x$, then $\dfrac{dE}{dt} = -ky^2|y|$, and hence that, while the point $(0,0)$ is a center for the linearized equation, it behaves like a stable spiral for the nonlinear equation. Sketch the phase diagram for the latter.

## Equation of Motion and Energy Dissipation

By the chain rule,

$$\dot E = \frac{\partial E}{\partial x}\dot x + \frac{\partial E}{\partial y}\dot y = \sin x\;y + y\bigl(-\sin x - ky|y|\bigr) = -ky^2|y| = -k|y|^3 \le 0 .$$

Here $y^2|y| = |y|^3$, so $\dot E = 0$ exactly when $y = 0$. Source: `Notes03-05-Nov_v2.pdf`, Lyapunov functions; Robinson, Sec. 34.

## Stationary Points and Linearisation

Equilibria: $y = 0$, $\sin x = 0$, so $(m\pi, 0)$, as in [[Problem - Ch5-P9 Damped Simple Pendulum Energy Dissipation and Regimes]].

> [!info] Differentiability of $y|y|$
> $y|y| = y^2$ for $y\ge0$ and $-y^2$ for $y<0$, so $\frac{d}{dy}(y|y|) = 2y$ for $y>0$ and $-2y$ for $y<0$, i.e. $2|y|$. This is continuous and equals $0$ at $y=0$ (one-sided limits agree), so $y|y|$ is $C^1$ and the Jacobian exists.

$$J = \begin{pmatrix} 0 & 1 \\ -\cos x & -2k|y| \end{pmatrix}.$$

At $(0,0)$: $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, $\lambda = \pm i$: a **centre of the linearised equation** (non-hyperbolic, so the linearisation does not decide the nonlinear behaviour). At $(\pi, 0)$: $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\lambda=\pm1$, a saddle, as in the undamped and linearly damped pendulum.

### Asymptotic stability of $(0,0)$

$E$ is positive definite near the origin up to the constant: $E + 1 = \tfrac12y^2 + (1-\cos x) \ge 0$, vanishing only at $(0,0)$ in the pocket $\{E<1\}$, and $\dot E = -k|y|^3 \le 0$, so $(0,0)$ is Lyapunov stable. If $\dot E = 0$ along a whole trajectory, then $y\equiv0$, so $\dot y = 0$ and $\sin x = 0$, which in the pocket means $x=0$. By LaSalle, every trajectory starting in $\{E<1\}$ (bounded and invariant, since $\dot E\le0$) tends to $(0,0)$: it is **asymptotically stable**.

### Spiral behaviour and its rate

Since $\dot x = y$, orbits turn clockwise (they move right in the upper half plane, left in the lower). They cannot be stopped on $y=0$ (there $\dot y=-\sin x\ne0$ for $x\ne0$), so they cross the $x$-axis infinitely many times while $E$ decreases monotonically: an inward spiral.

> [!warning] Not an exponential spiral
> The decay is algebraic, not exponential. Near the origin take $x\approx A\cos t$, $y\approx-A\sin t$ with $E+1\approx A^2/2$. Averaging $\dot E=-k|y|^3$ over one period with $\langle|\sin t|^3\rangle=\frac1{2\pi}\int_0^{2\pi}|\sin t|^3dt=\frac1{2\pi}\cdot\frac83=\frac4{3\pi}$ gives $A\dot A=-\frac{4k}{3\pi}A^3$, so $\dot A=-\frac{4k}{3\pi}A^2$ and $A(t)=\dfrac{A_0}{1+\frac{4k}{3\pi}A_0t}\sim\dfrac1t$. A linearly damped stable spiral decays like $e^{-kt/2}$; the quadratic drag is too weak at small $|y|$ for that (hence the linearisation sees a centre).

## Phase Portrait and Physical Interpretation

Orbits from the pocket around $(0,0)$ spiral clockwise inward, closer together at large $|y|$ (strong drag) and almost circular near the origin (weak drag). Orbits with large energy rotate over the top, lose energy at each turn and are eventually captured in one of the wells $(2m\pi,0)$; the stable manifolds of the saddles $((2m+1)\pi,0)$ separate the basins.

![[attachments/AM-PS/ch5-e10.svg]]
*Phase diagram of $\dot x=y$, $\dot y=-\sin x-ky|y|$: inward clockwise spirals around $(2m\pi,0)$, saddles at $((2m+1)\pi,0)$.*

> [!result] Summary
> $\dot E=-ky^2|y|\le0$; the linearisation at $(0,0)$ has eigenvalues $\pm i$ (centre) but the nonlinear equation is asymptotically stable (Lyapunov + LaSalle), a stable spiral winding clockwise with amplitude decaying like $1/t$. Dimensional check: $x=\theta$ is dimensionless and $[y]=[\dot\theta]=\mathrm{T^{-1}}$, so $[k]=1$ (dimensionless) gives $[ky|y|]=\mathrm{T^{-2}}=[\dot y]$ in nondimensional pendulum units.
