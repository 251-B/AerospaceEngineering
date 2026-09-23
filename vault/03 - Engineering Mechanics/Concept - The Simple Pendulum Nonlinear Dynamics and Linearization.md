---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: The Simple Pendulum — Nonlinear Dynamics and Linearization
tags:
  - concept
  - simple-pendulum
  - harmonic-oscillator
  - nonlinear-dynamics
  - linearization
---

# Concept: The Simple Pendulum — Nonlinear Dynamics and Linearization

## 1. Physical Model and Constraints
A point particle of mass $m$ is suspended by an inextensible massless rod of length $\ell$ from a fixed pivot $O$.
* **Coordinate:** Angle $\theta(t)$ measured from the vertical downward equilibrium.
* **Polar Basis:** $\{\mathbf{e}_R, \mathbf{e}_\theta\}$ with $R = \ell = \text{const}$.
* **Acceleration:** $\mathbf{a}_0^P = -\ell\dot{\theta}^2\mathbf{e}_R + \ell\ddot{\theta}\mathbf{e}_\theta$.

---

## 2. Dynamic Force Balance
* **Weight:** $\mathbf{W} = mg\cos\theta\,\mathbf{e}_R - mg\sin\theta\,\mathbf{e}_\theta$.
* **Tension:** $\mathbf{T} = -T\,\mathbf{e}_R$.
* **Newton's Second Law ($m\mathbf{a} = \mathbf{W} + \mathbf{T}$):**
  * Radial: $-m\ell\dot{\theta}^2 = mg\cos\theta - T \implies T = m(g\cos\theta + \ell\dot{\theta}^2)$.
  * Azimuthal: $m\ell\ddot{\theta} = -mg\sin\theta \implies \ddot{\theta} + \frac{g}{\ell}\sin\theta = 0$.

---

## 3. Conservation of Mechanical Energy
$$ T_0 = \frac{1}{2}m\ell^2\dot{\theta}^2, \quad V_0(\theta) = mg\ell(1 - \cos\theta) $$
$$ E_0 = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell(1 - \cos\theta) = \text{constant} $$
The first integral of motion gives angular velocity:
$$ \dot{\theta} = \pm\sqrt{\frac{2}{m\ell^2}[E_0 - mg\ell(1 - \cos\theta)]} $$

---

## 4. Equilibrium and Linearization
* **Stable Equilibrium:** $\theta_* = 0$ ($V_0''(0) = mg\ell > 0$).
* **Unstable Equilibrium:** $\theta_* = \pm\pi$ ($V_0''(\pm\pi) = -mg\ell < 0$).
* **Small Angle Linearization ($\theta \ll 1 \implies \sin\theta \approx \theta$):**
  $$ \ddot{\theta} + \frac{g}{\ell}\theta = 0 \iff \ddot{\theta} + \omega_0^2\theta = 0 $$
  Harmonic oscillation with natural frequency and period:
  $$ \omega_0 = \sqrt{\frac{g}{\ell}} \quad [\text{rad/s}], \quad T_0 = 2\pi\sqrt{\frac{\ell}{g}} \quad [\text{s}] $$
