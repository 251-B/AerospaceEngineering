---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Simple pendulum phase portrait"
tags:
  - problema-resuelto
  - advanced-maths
  - phase-plane
  - pendulum
  - energy-conservation
---

# Problem 5.8: Simple Pendulum, Energy Conservation and Phase Portrait

> Official exercise 8 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Method and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Consider the equation for a simple pendulum of unit frequency $\omega = 1$ that was derived and studied in Chapter 3, $\dfrac{d^2\theta}{dt^2} = -\sin\theta$. Convert this single second order equation into a first order system and sketch the phase portrait. Discuss the physical behavior of the system taking into account that the total energy is conserved.

## Equation of Motion and Energy Dissipation

With $y = \dot\theta$:

$$\dot\theta = y, \qquad \dot y = -\sin\theta .$$

The pendulum is a particle in the potential $V(\theta) = -\cos\theta$ (since $V' = \sin\theta$), so $E(\theta, y) = \tfrac12 y^2 - \cos\theta$. Along solutions, by the chain rule,

$$\dot E = y\,\dot y + \sin\theta\,\dot\theta = y(-\sin\theta) + \sin\theta\,y = 0 .$$

> [!info] Consequence
> $E$ is constant on trajectories (no dissipation, so no attractors and no spirals): each orbit lies on a level curve $\tfrac12 y^2 - \cos\theta = E$, i.e. $y = \pm\sqrt{2(E + \cos\theta)}$, defined where $E + \cos\theta \ge 0$. The portrait is $2\pi$-periodic in $\theta$ (the angle $\theta$ and $\theta + 2\pi$ are the same physical state).

Source: `Notes03-05-Nov_v2.pdf`, conserved quantities of Hamiltonian systems; Robinson, Sec. 34.

## Stationary Points and Linearisation

Equilibria: $y = 0$ and $\sin\theta = 0$, so $(k\pi, 0)$, $k\in\mathbb Z$. The Jacobian of $(y, -\sin\theta)$ is $J = \begin{pmatrix} 0 & 1 \\ -\cos\theta & 0 \end{pmatrix}$.

### (i) $(2k\pi, 0)$: pendulum hanging down

$\cos(2k\pi) = 1$, so $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, $\lambda^2 + 1 = 0$, $\lambda = \pm i$: a linear centre. It is non-hyperbolic, so linearisation alone cannot decide. The conserved $E$ decides it: $E = \tfrac12 y^2 - \cos\theta$ has a strict local minimum $E = -1$ at $(2k\pi, 0)$ (Hessian $\operatorname{diag}(\cos\theta, 1) = I$, positive definite), so the level curves $E < 1$ near it are closed curves. Therefore $(2k\pi, 0)$ is a **nonlinear centre**.

### (ii) $((2k+1)\pi, 0)$: pendulum inverted

$\cos((2k+1)\pi) = -1$, so $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\lambda^2 - 1 = 0$, $\lambda = \pm1$ with eigenvectors $(1, 1)^T$ (unstable) and $(1,-1)^T$ (stable): a **saddle**.

## Phase Portrait and Physical Interpretation

The saddle sits at $E = -\cos\pi = 1$. Its level set $E = 1$ gives $\tfrac12y^2 = 1 + \cos\theta = 2\cos^2(\theta/2)$ (half-angle identity), so

$$E = 1 \iff y = \pm 2\cos\frac{\theta}{2} .$$

This is the **separatrix**: the curves joining adjacent saddles (heteroclinic orbits).

| Energy | Orbit shape | Motion |
| :--- | :--- | :--- |
| $E = -1$ | the point $(2k\pi, 0)$ | pendulum at rest, hanging |
| $-1 < E < 1$ | closed curves around the centre | **libration**: oscillation between turning points $\pm\theta_{\max}$, $\cos\theta_{\max} = -E$ |
| $E = 1$ | separatrix $y = \pm2\cos(\theta/2)$ | the pendulum approaches the upright position as $t\to\infty$ (infinite period) |
| $E > 1$ | curves with $y \ne 0$ for all $\theta$ | **rotation**: the pendulum goes round the pivot, $y$ keeps its sign, $|y|$ minimal at the top |

![[attachments/AM-PS/ch5-e8.svg]]
*Phase portrait of $\ddot\theta = -\sin\theta$: centres at $\theta = 2k\pi$, saddles at $(2k+1)\pi$, separatrix $y = \pm2\cos(\theta/2)$ bounding the librations.*

> [!result] Summary
> $\dot E = 0$; centres at $(2k\pi, 0)$ (nonlinear, confirmed by closed level curves for $E<1$); saddles at $((2k+1)\pi, 0)$; separatrix $E=1\iff y=\pm2\cos(\theta/2)$; libration for $-1<E<1$ and rotation for $E>1$. Dimensional check: with $\omega=1$, $[\sin\theta]=1$ and $[\ddot\theta]=\mathrm{T^{-2}}$, consistent with $\omega^2=1\ \mathrm{T^{-2}}$.
