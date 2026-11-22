---
materia: "Advanced Maths"
tema: "Tema 5: Coupled Nonlinear Systems and the Phase Plane"
origen: "probls_ch5_2627.pdf - Exercise 8"
dificultad: media
id: "e8"
pill: "Simple Pendulum • Separatrix • Librations & Rotations"
tags:
  - problema-resuelto
  - sistemas-no-lineales
  - retrato-de-fase
---

# Problem 5.8: Simple Undamped Pendulum

> Official exercise 8 of the sheet `probls_ch5_2627.pdf` (UC3M, Advanced Mathematics 2026/27). Part of [[Problem Set - Chapter 5]]. Theory and notation: [[Topic 5 - Coupled Nonlinear Systems and the Phase Plane]].

## Statement

Consider the equation for a simple pendulum of unit frequency $\omega = 1$ that was derived and studied in Chapter 3, $\frac{d^2\theta}{dt^2} = -\sin\theta$. Convert this single second order equation into a first order system and sketch the phase portrait. Discuss the physical behavior of the system taking into account that the total energy is conserved.

## Setting up the system

First, we convert the second-order pendulum ODE into an autonomous first-order system using the angular position $\theta$ and angular velocity $v = \dot\theta$ (matching the notation of `Notes03-05-Nov_v2.pdf`, pp. 10–12), and we verify explicitly that the total mechanical energy $E$ is conserved.

Defining $v = \frac{d\theta}{dt} = \dot\theta$, we have $\dot v = \frac{d^2\theta}{dt^2} = -\sin\theta$, so the equivalent coupled first-order system is

$$ \dot\theta = f(\theta, v) = v, \qquad \dot v = g(\theta, v) = -\sin\theta. $$

Since the right-hand side is $2\pi$-periodic in $\theta$, the entire phase portrait is $2\pi$-periodic along the $\theta$-axis.

In dimensionless units ($\omega^2 = g/L = 1$, $m = 1$, $L = 1$), the kinetic energy is $T = \frac{1}{2}v^2$ and the gravitational potential energy (measured from the horizontal level of the pivot) is $V(\theta) = -\cos\theta$, so the total mechanical energy is

$$ E(\theta, v) = \frac{1}{2}v^2 - \cos\theta. $$

Differentiating $E(\theta(t), v(t))$ along any trajectory by the chain rule:

$$ \frac{dE}{dt} = \frac{\partial E}{\partial\theta}\dot\theta + \frac{\partial E}{\partial v}\dot v = (\sin\theta)\cdot v + v\cdot(-\sin\theta) = v\sin\theta - v\sin\theta = 0. $$

Therefore $E(\theta(t), v(t)) = E_0 = \text{const}$ along every solution: every trajectory lies on a level curve $\frac{1}{2}v^2 - \cos\theta = E_0$.

## Step 1: Critical points

Next, we locate all equilibrium points by setting $\dot\theta = 0$ and $\dot v = 0$ simultaneously.

$$ \begin{cases} \dot\theta = v = 0, \\ \dot v = -\sin\theta = 0 \implies \theta = m\pi, \quad m \in \mathbb{Z}. \end{cases} $$

There is an infinite periodic array of critical points along the $\theta$-axis:

$$ (\theta^*, v^*) = (m\pi,\, 0), \qquad m \in \mathbb{Z}. $$

Physically, the even points $(2n\pi, 0)$ represent the pendulum hanging straight **downward** at rest, while the odd points $((2n+1)\pi, 0)$ represent the pendulum balanced straight **upward** at rest.

## Step 2: Linearization

We compute the Jacobian matrix $J(\theta, v)$ by taking all four partial derivatives of $f(\theta, v) = v$ and $g(\theta, v) = -\sin\theta$.

$$ \frac{\partial f}{\partial\theta} = 0, \qquad \frac{\partial f}{\partial v} = 1, \qquad \frac{\partial g}{\partial\theta} = -\cos\theta, \qquad \frac{\partial g}{\partial v} = 0. $$

Thus

$$ J(\theta, v) = \begin{pmatrix} 0 & 1 \\ -\cos\theta & 0 \end{pmatrix}. $$

At $(m\pi, 0)$ we have $\cos(m\pi) = (-1)^m$, so the Jacobian alternates between two matrices depending on the parity of $m$:

$$ J(2n\pi,\, 0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad J\bigl((2n+1)\pi,\, 0\bigr) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}. $$

## Step 3: Local study

We now classify the two families of equilibria via their eigenvalues, eigenvectors, and energy contours.

### Even equilibria: $(2n\pi, 0)$ (hanging downward)

Characteristic polynomial of $J(2n\pi, 0) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$:

$$ \det\bigl(J(2n\pi, 0) - \lambda I\bigr) = \det\begin{pmatrix} -\lambda & 1 \\ -1 & -\lambda \end{pmatrix} = \lambda^2 + 1 = 0 \implies \lambda_\pm = \pm i. $$

The linearized system predicts a **centre** (purely imaginary eigenvalues, non-hyperbolic, so Hartman–Grobman alone is inconclusive). To confirm that $(2n\pi, 0)$ is a true **nonlinear centre**, note that the conserved energy $E(\theta, v) = \frac{1}{2}v^2 - \cos\theta$ attains a strict local minimum $E(2n\pi, 0) = -1$ at each even equilibrium (since $V(2n\pi) = -1$ and $V''(2n\pi) = \cos(2n\pi) = 1 > 0$). Hence for $-1 < E < 1$ the level curves $E(\theta, v) = \text{const}$ are nested closed loops surrounding $(2n\pi, 0)$, proving that every $(2n\pi, 0)$ is a **nonlinear centre** (Lyapunov stable).

### Odd equilibria: $((2n+1)\pi, 0)$ (balanced upright)

Characteristic polynomial of $J((2n+1)\pi, 0) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$:

$$ \det\Bigl(J\bigl((2n+1)\pi, 0\bigr) - \lambda I\Bigr) = \det\begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = (\lambda - 1)(\lambda + 1) = 0 \implies \lambda_1 = 1, \quad \lambda_2 = -1. $$

Row-by-row eigenvectors:
- For $\lambda_1 = 1$: $(J - I)\mathbf v_1 = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} v_\theta \\ v_v \end{pmatrix} = \mathbf 0 \implies -v_\theta + v_v = 0 \implies \mathbf v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ (unstable direction, slope $+1$).
- For $\lambda_2 = -1$: $(J + I)\mathbf v_2 = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} v_\theta \\ v_v \end{pmatrix} = \mathbf 0 \implies v_\theta + v_v = 0 \implies \mathbf v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ (stable direction, slope $-1$).

Since $\lambda_1 = 1 > 0 > -1 = \lambda_2$, every odd equilibrium $((2n+1)\pi, 0)$ is a hyperbolic **saddle** (unstable).

## Step 4: Global picture

We solve the energy conservation equation $\frac{1}{2}v^2 - \cos\theta = E$ for $v$ to classify all global trajectories and their physical meaning.

Solving for $v$:

$$ v = \pm\sqrt{2(E + \cos\theta)}. $$

Since $\dot\theta = v$, trajectories move to the right in the upper half-plane ($v > 0$) and to the left in the lower half-plane ($v < 0$). Because $\cos\theta \in [-1, 1]$, real motion requires $E \ge -1$, and the global phase portrait splits into three distinct physical regimes separated by the saddle energy $E((2n+1)\pi, 0) = 0 - (-1) = 1$:

1. **Librations (oscillations), $-1 < E < 1$:** Here $E + \cos\theta \ge 0$ only on bounded intervals $|\theta - 2n\pi| \le \theta_{\max}$ where $\cos\theta_{\max} = -E$. Each energy level gives a closed, clockwise periodic orbit around $(2n\pi, 0)$: the pendulum swings back and forth between $-\theta_{\max}$ and $+\theta_{\max}$ without ever reaching the top. Near $(2n\pi, 0)$ ($E \approx -1$), $\cos\theta \approx 1 - \frac{1}{2}\theta^2$, so the orbits are nearly circles $v^2 + (\theta - 2n\pi)^2 \approx 2(E + 1)$.
2. **Heteroclinic separatrix, $E = 1$:** Substituting $E = 1$ and using the half-angle identity $1 + \cos\theta = 2\cos^2(\theta/2)$:

$$ v = \pm\sqrt{2(1 + \cos\theta)} = \pm\sqrt{4\cos^2(\theta/2)} = \pm 2\cos\left(\frac{\theta}{2}\right) \quad \text{(with sign alternating across each odd } m\pi\text{)}. $$

These curves are **heteroclinic orbits** connecting adjacent saddles $((2n-1)\pi, 0)$ and $((2n+1)\pi, 0)$, entering and leaving each saddle with slopes $\pm 1$. Physically, the pendulum has the exact energy needed to swing up and approach the upright position asymptotically as $t \to +\infty$ (taking infinite time to reach it, since an equilibrium cannot be reached in finite time by uniqueness of solutions).
3. **Rotations (whirling motion), $E > 1$:** Here $E + \cos\theta \ge E - 1 > 0$ for all $\theta \in \mathbb{R}$, so $v$ never vanishes. The phase curves are wavy, unbounded $2\pi$-periodic graphs running purely to the right ($v > 0$, continuous rotation in one direction) or purely to the left ($v < 0$, continuous rotation in the opposite direction). The speed $|v|$ is largest at the bottom ($\theta = 2n\pi$, $|v| = \sqrt{2(E + 1)}$) and smallest at the top ($\theta = (2n+1)\pi$, $|v| = \sqrt{2(E - 1)}$).

![[attachments/AM-PS/ch5-e8-pendulum.svg]]
*Phase portrait of the simple undamped pendulum $\dot\theta = v$, $\dot v = -\sin\theta$ (Exercise 5.8). Centres at $(2n\pi, 0)$, saddles at $((2n+1)\pi, 0)$ with slopes $\pm 1$, heteroclinic separatrix $E = 1$ ($v = \pm 2\cos(\theta/2)$) separating librations ($-1 < E < 1$) from continuous rotations ($E > 1$).*

## Answers and checks

We verify the physical dimensions and the small-angle approximation.

- **Dimensional check (SI units):** Restoring the natural frequency $\omega = \sqrt{g/L}$ ($\mathrm{s}^{-1}$, since $[g/L] = (\mathrm{m\,s^{-2}})/\mathrm{m} = \mathrm{s}^{-2}$), the equation is $\ddot\theta = -\omega^2\sin\theta$. The angle $\theta$ is dimensionless ($\mathrm{rad}$), so $[\dot\theta] = \mathrm{s}^{-1}$ and $[\ddot\theta] = \mathrm{s}^{-2} = [\omega^2\sin\theta]$. The specific energy $E = \frac{1}{2}\dot\theta^2 - \omega^2\cos\theta$ has units of $\mathrm{s}^{-2}$ in both terms (multiplying by $mL^2$ gives joules, $\mathrm{J}$).
- **Small-angle check:** For $|\theta| \ll 1$, $\sin\theta \approx \theta$ gives $\ddot\theta = -\theta$, whose circular phase curves $\theta^2 + v^2 = r^2$ and angular frequency $\omega = 1$ match the linearization at $(0, 0)$ ($\lambda = \pm i$).

> [!result] Key results
> - **First-order system & conserved energy:** $\dot\theta = v$, $\dot v = -\sin\theta$; $E(\theta, v) = \frac{1}{2}v^2 - \cos\theta$, with $\dot E = 0$.
> - **Equilibria $(m\pi, 0)$, $m \in \mathbb{Z}$:**
>   - Even $m = 2n$: nonlinear **centres** ($\lambda = \pm i$, strict local minima $E = -1$, hanging downward).
>   - Odd $m = 2n+1$: hyperbolic **saddles** ($\lambda = \pm 1$, $\mathbf v_\pm = (1, \pm 1)^T$, $E = 1$, balanced upright).
> - **Global regimes:** $-1 < E < 1$ periodic **librations**; $E = 1$ heteroclinic **separatrix** $v = \pm 2\cos(\theta/2)$ (asymptotic approach to upright rest); $E > 1$ continuous **rotations** ($v > 0$ or $v < 0$).
