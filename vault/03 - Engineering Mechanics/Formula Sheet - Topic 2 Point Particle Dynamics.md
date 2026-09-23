---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
type: formula-sheet
tags:
  - formulas
  - point-particle
  - dynamics
  - summary
---

# 📑 Formula Sheet — Topic 2: Point Particle Dynamics

## 1. Linear Momentum and Newton's Second Law
$$ \mathbf{p}_0 = m_P\,\mathbf{v}_0^P, \quad \mathbf{F} = \left.\frac{d\mathbf{p}_0}{dt}\right|_0 = m_P\,\mathbf{a}_0^P $$
$$ \text{In Cartesian components:} \quad m_P\ddot{x} = F_x, \quad m_P\ddot{y} = F_y, \quad m_P\ddot{z} = F_z $$

## 2. Momentum Conservation (Isolated Systems)
$$ \sum_{i=1}^N \mathbf{F}_i^{\text{ext}} = \mathbf{0} \implies \mathbf{p}_{\text{tot}} = \sum_{i=1}^N m_i\,\mathbf{v}_0^{P_i} = \text{constant} $$

## 3. Kinetic Energy, Power, and Work
$$ T_0 = \frac{1}{2}m_P\,v_0^2, \quad P = \mathbf{F} \cdot \mathbf{v}_0^P = F_t\,v_0 $$
$$ \frac{dT_0}{dt} = P = \mathbf{F} \cdot \mathbf{v}_0^P \iff W_{12} = \int_{t_1}^{t_2} P\,dt = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F}\cdot d\mathbf{r} = \Delta T_0 = T_{0,2} - T_{0,1} $$

## 4. Conservative Forces and Potential Energy
$$ \oint_{\mathcal{C}} \mathbf{F} \cdot d\mathbf{r} = 0 \iff \nabla \times \mathbf{F} = \mathbf{0} $$
$$ \mathbf{F} = -\nabla V_0, \quad W_{12} = -\Delta V_0 = -(V_0(\mathbf{r}_2) - V_0(\mathbf{r}_1)) $$
* **Uniform Gravity:** $V_0(z) = m_P g z + C$
* **Linear Spring:** $V_0(r) = \frac{1}{2}k r^2$
* **Inverse-Square Gravity:** $V_0(r) = -\frac{G M m_P}{r}$

## 5. Mechanical Energy Conservation
$$ E_0 = T_0 + V_0 = \frac{1}{2}m_P\,v_0^2 + V_0(\mathbf{r}) $$
$$ \frac{dE_0}{dt} = \mathbf{F}_N \cdot \mathbf{v}_0^P \implies \text{If } \mathbf{F}_N = \mathbf{0} \text{ or } \mathbf{F}_N \perp \mathbf{v}_0^P \implies E_0 = \text{constant} $$

## 6. Qualitative 1D Motion Analysis
$$ v(x) = \sqrt{\frac{2(E_0 - V_0(x))}{m_P}} $$
* **Allowed Region:** $E_0 \ge V_0(x)$
* **Forbidden Region:** $E_0 < V_0(x)$
* **Turning Points:** $E_0 = V_0(x) \iff v = 0$

## 7. Equilibrium and Stability
* **Equilibrium:** $\left.\frac{dV_0}{dx}\right|_{x_*} = 0 \iff F(x_*) = 0$
* **Stable (Minimum):** $\left.\frac{d^2V_0}{dx^2}\right|_{x_*} > 0$
* **Unstable (Maximum):** $\left.\frac{d^2V_0}{dx^2}\right|_{x_*} < 0$

## 8. Simple Pendulum Summary
* **Equation of Motion:** $\ddot{\theta} + \frac{g}{\ell}\sin\theta = 0$
* **Rod Tension:** $T(\theta, \dot{\theta}) = m(g\cos\theta + \ell\dot{\theta}^2)$
* **Mechanical Energy:** $E_0 = \frac{1}{2}m\ell^2\dot{\theta}^2 + mg\ell(1 - \cos\theta) = \text{const}$
* **Linearized Harmonic Motion ($\theta \ll 1$):**
  $$ \ddot{\theta} + \omega_0^2\theta = 0, \quad \omega_0 = \sqrt{\frac{g}{\ell}}, \quad T_0 = 2\pi\sqrt{\frac{\ell}{g}} $$
