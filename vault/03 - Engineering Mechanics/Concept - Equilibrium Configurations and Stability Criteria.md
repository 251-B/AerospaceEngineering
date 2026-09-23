---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: Equilibrium Configurations and Stability Criteria
tags:
  - concept
  - equilibrium
  - stability
  - potential-wells
  - lyapunov
---

# Concept: Equilibrium Configurations and Stability Criteria

## 1. Definition of Equilibrium Configuration
A position $\mathbf{r}_*$ is an **equilibrium configuration** if a particle released at $\mathbf{r}_*$ with zero velocity remains permanently at rest:
$$ \mathbf{a}_0^P = \mathbf{0} \iff \sum \mathbf{F}(\mathbf{r}_*) = \mathbf{0} $$
For a conservative system, equilibrium points correspond to the critical points of the potential function:
$$ \nabla V_0(\mathbf{r}_*) = \mathbf{0} \quad \left( \text{in 1D: } \left.\frac{dV_0}{dx}\right|_{x_*} = 0 \right) $$

---

## 2. Lyapunov Stability Definition
An equilibrium configuration $\mathbf{r}_*$ is **stable** if for any arbitrarily small tolerance $\varepsilon_r, \varepsilon_v > 0$, there exist bounds $\delta_r, \delta_v > 0$ such that initial perturbations $\|\mathbf{r}(0) - \mathbf{r}_*\| < \delta_r$ and $\|\mathbf{v}(0)\| < \delta_v$ ensure that:
$$ \|\mathbf{r}(t) - \mathbf{r}_*\| < \varepsilon_r \quad \text{and} \quad \|\mathbf{v}(t)\| < \varepsilon_v \quad \forall t \ge 0 $$
Otherwise, the equilibrium configuration is **unstable**.

---

## 3. Second-Derivative Curvature Criterion in 1D
Expanding the potential $V_0(x)$ in a Taylor series about $x_*$:
$$ F(x) = -\frac{dV_0}{dx} \approx -\left.\frac{d^2V_0}{dx^2}\right|_{x_*}(x - x_*) $$

* **Stable Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} > 0$):**
  * Local minimum of $V_0(x)$ (bottom of a potential well).
  * Linearized restoring force $F \approx -k(x - x_*)$ producing oscillations about $x_*$.
* **Unstable Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} < 0$):**
  * Local maximum of $V_0(x)$ (crest of a potential hill).
  * Linearized repulsive force $F \approx +k(x - x_*)$ driving the particle away from $x_*$.
* **Neutral Equilibrium ($\frac{d^2V_0}{dx^2}\big|_{x_*} = 0$):**
  * Inflection point or flat plateau; requires evaluating higher-order derivatives.
