---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 9"
dificultad: media
id: "e9"
pill: "Damped Pendulum • Energy Dissipation • Bifurcation at k = 2"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.9: Damped Pendulum

> Official exercise 9 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

The first order system

$$ \dot x = y, \qquad \dot y = -\sin x - ky $$

describes a more realistic situation in which the simple pendulum considered in the previous exercise is subject to a damping force with constant $k > 0$. Sketch the phase portrait and discuss the physical behavior of the system taking into account that the total energy is not conserved.

## Setting up the system

First, we relate the variables $(x, y)$ to the physical pendulum coordinates and compute the time derivative of the mechanical energy $E(x, y)$ to quantify energy dissipation.

Here $x = \theta$ is the angular displacement and $y = \dot\theta = v$ is the angular velocity (matching `Notes03-05-Nov_v2.pdf`, pp. 12–14). The system is

$$ \dot x = f(x, y) = y, \qquad \dot y = g(x, y) = -\sin x - ky, \qquad k > 0, $$

which is $2\pi$-periodic in $x$. Taking the undamped mechanical energy $E(x, y) = \frac{1}{2}y^2 - \cos x$ and differentiating along any solution by the chain rule:

$$ \frac{dE}{dt} = \frac{\partial E}{\partial x}\dot x + \frac{\partial E}{\partial y}\dot y = (\sin x)\cdot y + y\cdot(-\sin x - ky) = y\sin x - y\sin x - ky^2 = -ky^2 \le 0. $$

Because $k > 0$, $\dot E \le 0$ everywhere, and $\dot E = 0$ if and only if $y = 0$. On the $x$-axis ($y = 0$), $\dot y = -\sin x$, which is non-zero except at the equilibria $x = m\pi$. Therefore no non-equilibrium trajectory can remain on $y = 0$, so $E(t)$ decreases **strictly** along every non-equilibrium orbit: neither closed librations nor perpetual rotations can exist.

## Step 1: Critical points

Next, we find all equilibria by setting $\dot x = 0$ and $\dot y = 0$ simultaneously.

$$ \begin{cases} \dot x = y = 0, \\ \dot y = -\sin x - k\cdot 0 = -\sin x = 0 \implies x = m\pi, \quad m \in \mathbb{Z}. \end{cases} $$

Damping leaves the equilibrium positions unchanged: $(m\pi, 0)$ for $m \in \mathbb{Z}$ (even $m = 2n$ hanging downward; odd $m = 2n+1$ balanced upright).

## Step 2: Linearization

We compute the Jacobian matrix $J(x, y)$ explicitly and evaluate it at the even and odd equilibria.

$$ \frac{\partial f}{\partial x} = 0, \qquad \frac{\partial f}{\partial y} = 1, \qquad \frac{\partial g}{\partial x} = -\cos x, \qquad \frac{\partial g}{\partial y} = -k, $$

so

$$ J(x, y) = \begin{pmatrix} 0 & 1 \\ -\cos x & -k \end{pmatrix}. $$

Evaluating at $x = m\pi$ where $\cos(m\pi) = (-1)^m$:

$$ J(2n\pi,\, 0) = \begin{pmatrix} 0 & 1 \\ -1 & -k \end{pmatrix}, \qquad J\bigl((2n+1)\pi,\, 0\bigr) = \begin{pmatrix} 0 & 1 \\ 1 & -k \end{pmatrix}. $$

## Step 3: Local study

We now find the eigenvalues and eigenvectors of both matrices and identify the bifurcation in local type at $k = 2$.

### Even equilibria: $(2n\pi, 0)$ (hanging downward)

Characteristic polynomial of $J(2n\pi, 0) = \begin{pmatrix} 0 & 1 \\ -1 & -k \end{pmatrix}$:

$$ \det\bigl(J(2n\pi, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -1 & -k - \lambda \end{pmatrix} = (-\lambda)(-k - \lambda) - (-1) = \lambda^2 + k\lambda + 1 = 0. $$

Applying the quadratic formula:

$$ \lambda_\pm = \frac{-k \pm \sqrt{k^2 - 4}}{2}. $$

Every root has strictly negative real part for all $k > 0$, so every $(2n\pi, 0)$ is **hyperbolic and asymptotically stable**, with a qualitative transition (bifurcation) at the critical damping value $k = 2$:

- **Underdamped ($0 < k < 2$):** $k^2 - 4 < 0$, giving a complex conjugate pair with negative real part:

$$ \lambda_\pm = \frac{-k \pm i\sqrt{4 - k^2}}{2}. $$

Each $(2n\pi, 0)$ is a **stable spiral** (clockwise, since $\dot x = y > 0$ for $y > 0$). For instance, in the lecturer's example $k = \sqrt{2}$ (`Notes03-05-Nov_v2.pdf`, p. 13), $\lambda_\pm = \frac{-\sqrt{2} \pm i\sqrt{2}}{2}$. Physically, the pendulum oscillates back and forth around the bottom with exponentially decaying amplitude.

- **Critically damped ($k = 2$):** $k^2 - 4 = 0$, giving a repeated negative eigenvalue $\lambda = -1$ (algebraic multiplicity $2$). Checking the eigenspace:

$$ (J + I)\mathbf v = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies v_x + v_y = 0 \implies \mathbf v = \begin{pmatrix} 1 \\ -1 \end{pmatrix}. $$

There is only a one-dimensional eigenspace (geometric multiplicity $1$), so each $(2n\pi, 0)$ is a **stable improper node** (degenerate node) with unique tangent slope $-1$.

- **Overdamped ($k > 2$):** $k^2 - 4 > 0$ and $\sqrt{k^2 - 4} < k$, giving two distinct negative real eigenvalues $\lambda_- < \lambda_+ < 0$ with eigenvectors

$$ (J - \lambda_\pm I)\mathbf v_\pm = \begin{pmatrix} -\lambda_\pm & 1 \\ -1 & -k - \lambda_\pm \end{pmatrix}\begin{pmatrix} v_x \\ v_y \end{pmatrix} = \mathbf 0 \implies \mathbf v_\pm = \begin{pmatrix} 1 \\ \lambda_\pm \end{pmatrix}. $$

Each $(2n\pi, 0)$ is a **stable node**: the pendulum returns to the bottom without oscillating, approaching tangent to the slower eigendirection $\mathbf v_+ = (1, \lambda_+)^T$.

### Odd equilibria: $((2n+1)\pi, 0)$ (balanced upright)

Characteristic polynomial of $J((2n+1)\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & -k \end{pmatrix}$:

$$ \det\Bigl(J\bigl((2n+1)\pi, 0\bigr) - \lambda I\Bigr) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -k - \lambda \end{pmatrix} = \lambda^2 + k\lambda - 1 = 0, $$

$$ \lambda_\pm = \frac{-k \pm \sqrt{k^2 + 4}}{2}. $$

Because $\sqrt{k^2 + 4} > \sqrt{k^2} = k > 0$, we have $\lambda_+ > 0$ and $\lambda_- < 0$ for **every** $k > 0$ (with $|\lambda_-| > \lambda_+$, since $\lambda_+ + \lambda_- = -k < 0$). Row-by-row eigenvectors from $(J - \lambda_\pm I)\mathbf v_\pm = \mathbf 0$:

$$ -\lambda_\pm v_x + v_y = 0 \implies \mathbf v_+ = \begin{pmatrix} 1 \\ \lambda_+ \end{pmatrix} \quad (\text{unstable, slope } \lambda_+ > 0), \qquad \mathbf v_- = \begin{pmatrix} 1 \\ \lambda_- \end{pmatrix} \quad (\text{stable, slope } \lambda_- < 0). $$

Hence every odd equilibrium $((2n+1)\pi, 0)$ is a hyperbolic **saddle** for all $k > 0$.

## Step 4: Global picture

Combining the local classification with the strict energy decay $\dot E = -ky^2 \le 0$ determines the global dynamics completely:

- **Breaking of the heteroclinic separatrix:** In the undamped pendulum ($k = 0$), a trajectory leaving $((2n-1)\pi, 0)$ along its unstable manifold had $E = 1$ and arrived at the next saddle $((2n+1)\pi, 0)$. With $k > 0$, energy decreases strictly along the unstable manifold, so it drops below $E = 1$ and cannot reach the next hilltop; instead, it falls into the basin of $(2n\pi, 0)$ (for small $k$, spiralling into $(2n\pi, 0)$).
- **Basins of attraction as diagonal strips:** The two branches of the stable manifold of each saddle $((2n+1)\pi, 0)$ extend backward in time toward $|y| \to \infty$ without intersecting any other trajectory, forming parallel curved boundaries that partition the entire $(x, y)$-plane into an infinite sequence of $2\pi$-shifted **basins of attraction**, one for each downward equilibrium $(2n\pi, 0)$.
- **Physical interpretation of large initial velocities:** A pendulum launched with large angular speed ($E \gg 1$) initially rotates over the top several times, losing energy $\Delta E = -k\int y^2\,dt$ on every revolution. Eventually $E$ drops below $1$, the pendulum can no longer pass the upright position, and it gets trapped in one of the basins, settling asymptotically to $(2n\pi, 0)$ (where $n$ is the integer number of full revolutions completed before stopping). Only a measure-zero set of initial conditions — those lying exactly on the stable manifold of a saddle $((2n+1)\pi, 0)$ — comes to rest balanced upright as $t \to +\infty$.

![[attachments/AM-PS/ch5-e9-damped-pendulum.svg]]
*Phase portrait of the linearly damped pendulum $\dot x = y$, $\dot y = -\sin x - ky$ in the underdamped regime $0 < k < 2$ (Exercise 5.9). Stable spirals at $(2n\pi, 0)$, saddles at $((2n+1)\pi, 0)$, and saddle stable manifolds partitioning the phase plane into basins of attraction.*

## Answers and checks

We check the undamped limit, the lecturer's numerical case, and dimensional consistency.

- **Undamped limit ($k \to 0^+$):** As $k \to 0^+$, $\dot E = -ky^2 \to 0$, $\lambda_\pm(2n\pi, 0) = \frac{-k \pm i\sqrt{4-k^2}}{2} \to \pm i$, and $\lambda_\pm((2n+1)\pi, 0) = \frac{-k \pm \sqrt{k^2+4}}{2} \to \pm 1$, recovering Exercise 5.8 smoothly.
- **Cross-check with class notes (`Notes03-05-Nov_v2.pdf`, pp. 12–14):** For $k = \sqrt{2} < 2$, the even equilibria have $\lambda_\pm = \frac{-\sqrt{2} \pm i\sqrt{2}}{2}$ (stable spirals) and the odd equilibria have $\lambda_\pm = \frac{-\sqrt{2} \pm \sqrt{6}}{2}$ (saddles), matching the notes identically.
- **Dimensional check (SI units):** Restoring $\omega^2 = g/L$ ($\mathrm{s}^{-2}$) and damping rate $\gamma$ ($\mathrm{s}^{-1}$), the equation is $\ddot\theta = -\omega^2\sin\theta - \gamma\dot\theta$. Every term has units of $\mathrm{s}^{-2}$ ($[\gamma\dot\theta] = \mathrm{s}^{-1}\cdot\mathrm{s}^{-1} = \mathrm{s}^{-2}$). The dimensionless damping ratio is $k = \gamma/\omega$, so the critical damping condition $k = 2$ corresponds to $\gamma = 2\omega$.

> [!result] Key results
> - **Energy dissipation:** $E(x, y) = \frac{1}{2}y^2 - \cos x \implies \dot E = -ky^2 \le 0$ (strictly decreasing off equilibria; no periodic orbits).
> - **Even equilibria $(2n\pi, 0)$ ($\lambda^2 + k\lambda + 1 = 0$, $\lambda_\pm = \frac{-k \pm \sqrt{k^2 - 4}}{2}$):**
>   - $0 < k < 2$: **stable spiral** (underdamped);
>   - $k = 2$: **stable improper node** ($\lambda = -1$, single eigenvector $(1, -1)^T$, critically damped);
>   - $k > 2$: **stable node** (overdamped).
> - **Odd equilibria $((2n+1)\pi, 0)$ ($\lambda^2 + k\lambda - 1 = 0$, $\lambda_\pm = \frac{-k \pm \sqrt{k^2 + 4}}{2}$):** hyperbolic **saddles** for all $k > 0$.
> - **Global dynamics:** Every rotating trajectory loses energy until captured by a basin of attraction of some $(2n\pi, 0)$; the stable manifolds of the saddles partition the phase plane into these basins.
