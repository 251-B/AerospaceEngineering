---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Damped pendulum regimes"
tags:
  - problema-resuelto
  - advanced-maths
  - phase-plane
  - pendulum
  - damping
  - lasalle
---

# Problem 5.9: Damped Simple Pendulum, Energy Dissipation and Regimes

> Official exercise 9 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The first order system $\dot x = y$, $\dot y = -\sin x - ky$ describes a more realistic situation in which the simple pendulum considered in the previous exercise is subject to a damping force with constant $k > 0$. Sketch the phase portrait and discuss the physical behavior of the system taking into account that the total energy is not conserved.

## Equation of Motion and Energy Dissipation

With $E = \tfrac12 y^2 - \cos x$ (the energy of [[Problem - Ch5-P8 Simple Pendulum Energy Conservation and Phase Portrait]]), the chain rule gives

$$\frac{dE}{dt} = y\,\dot y + \sin x\,\dot x = y(-\sin x - ky) + y\sin x = -ky^2 \le 0 .$$

> [!info] LaSalle argument
> $\dot E = 0$ only on $y = 0$. There $\dot y = -\sin x$, so a trajectory can remain on $y=0$ only if $\sin x = 0$, i.e. at an equilibrium. Hence the largest invariant subset of $\{\dot E = 0\}$ consists of the equilibria. The set $\{E < 1\}$ is a union of bounded lens-shaped pockets, $y^2 < 2(1+\cos x)$ (it forces $|x - 2m\pi| < \pi$), each containing one point $(2m\pi, 0)$. Since $E$ decreases, a trajectory that enters a pocket never leaves it, so it converges to the equilibrium inside it.

Source: `Notes03-05-Nov_v2.pdf`, damped systems and Lyapunov functions; Robinson, Sec. 34.

## Stationary Points and Linearisation

Equilibria: $y=0$, $\sin x=0$, so $(m\pi, 0)$. The Jacobian is $J = \begin{pmatrix} 0 & 1 \\ -\cos x & -k \end{pmatrix}$.

### (i) $(2m\pi, 0)$: hanging position

$J = \begin{pmatrix} 0 & 1 \\ -1 & -k \end{pmatrix}$, $\lambda^2 + k\lambda + 1 = 0$, so $\lambda = \dfrac{-k \pm \sqrt{k^2 - 4}}{2}$ (trace $-k<0$, determinant $1>0$, so always stable).

| Damping | $k^2-4$ | Eigenvalues | Type |
| :--- | :--- | :--- | :--- |
| underdamped, $0<k<2$ | $<0$ | complex, $\operatorname{Re}\lambda=-k/2<0$ | **stable spiral** |
| critically damped, $k=2$ | $=0$ | $\lambda=-1$ double | **stable improper node** |
| overdamped, $k>2$ | $>0$ | two real negatives, $\frac{-k\pm\sqrt{k^2-4}}{2}$ | **stable node** |

At $k=2$: $J + I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \ne 0$, so there is only one eigenvector $(1,-1)^T$ (not a star node): an improper node. For $k>2$ the product of the roots is $1$, so both are negative and distinct.

### (ii) $((2m+1)\pi, 0)$: inverted position

$J = \begin{pmatrix} 0 & 1 \\ 1 & -k \end{pmatrix}$, $\lambda^2 + k\lambda - 1 = 0$, so $\lambda = \dfrac{-k \pm \sqrt{k^2+4}}{2}$. The determinant is $-1 < 0$ for every $k>0$, so one root is positive and one negative: **saddles for all $k>0$**.

## Phase Portrait and Physical Interpretation

Damping removes energy, so the closed orbits of the undamped pendulum become inward spirals (small $k$) or monotone curves (large $k$) ending at a hanging equilibrium $(2m\pi,0)$. The stable manifolds of the saddles $((2m+1)\pi,0)$ separate which well $(2m\pi,0)$ a trajectory finally falls into: a pendulum released with high energy rotates several times, losing energy each turn, and then settles. Only the inverted position, an unstable equilibrium reached along the stable manifold, is a non-hanging final state.

![[attachments/AM-PS/ch5-e9-under.svg]]
*Underdamped pendulum, $0<k<2$ (e.g. $k=0.5$): trajectories spiral into $(2m\pi,0)$; the saddles' stable manifolds are the basin boundaries.*

![[attachments/AM-PS/ch5-e9-over.svg]]
*Overdamped pendulum, $k>2$ (e.g. $k=3$): no oscillation, trajectories approach $(2m\pi,0)$ monotonically along the slow eigendirection.*

> [!result] Summary
> $\dot E = -ky^2\le0$. $(2m\pi,0)$: stable spiral ($0<k<2$), stable improper node ($k=2$), stable node ($k>2$). $((2m+1)\pi,0)$: saddle for all $k>0$. The limit $k\to0$ recovers the centres of the undamped case. Dimensional check: $[k]=\mathrm{T^{-1}}$, so $[ky]=\mathrm{T^{-2}}=[\sin x\cdot\omega^2]$ with $\omega=1$.
