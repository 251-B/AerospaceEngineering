---
subject: Mechanics Applied to Aerospace Engineering
topic: 2 - Point Particle Dynamics
concept: Conservative Forces and Potential Energy
tags:
  - concept
  - conservative-forces
  - potential-energy
  - curl-condition
---

# Concept: Conservative Forces and Potential Energy

## 1. Physical Definition
A force field $\mathbf{F}(\mathbf{r})$ is **conservative** if the work done on a particle moving between two points $A$ and $B$ depends solely on the initial and final endpoints, and is strictly independent of the path $\Gamma$ followed:
$$ \int_{\Gamma_1} \mathbf{F} \cdot d\mathbf{r} = \int_{\Gamma_2} \mathbf{F} \cdot d\mathbf{r} \iff \oint_{\mathcal{C}} \mathbf{F} \cdot d\mathbf{r} = 0 \quad \text{for any closed contour } \mathcal{C} $$

---

## 2. Potential Energy Function $V_0(\mathbf{r})$
For a conservative force, choosing an arbitrary reference point $\mathbf{r}_*$:
$$ V_0(\mathbf{r}) = -\int_{\mathbf{r}_*}^{\mathbf{r}} \mathbf{F} \cdot d\mathbf{r}' $$
The force field is the negative gradient of its scalar potential energy:
$$ \mathbf{F} = -\nabla V_0 $$
In component form:
$$ F_x = -\frac{\partial V_0}{\partial x}, \quad F_y = -\frac{\partial V_0}{\partial y}, \quad F_z = -\frac{\partial V_0}{\partial z} $$
Work becomes the negative change in potential energy:
$$ W_{12} = -(V_0(\mathbf{r}_2) - V_0(\mathbf{r}_1)) = -\Delta V_0 $$

---

## 3. Necessary and Sufficient Curl Condition
In a simply connected spatial domain, a continuously differentiable force field is conservative if and only if its curl vanishes identically:
$$ \nabla \times \mathbf{F} = \mathbf{0} \iff \begin{cases}
\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} = 0 \\
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} = 0 \\
\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} = 0
\end{cases} $$

### Cylindrical Coordinates Test:
* $\mathbf{F} = aR\,\mathbf{e}_R \implies \nabla \times \mathbf{F} = \mathbf{0} \implies V_0(R) = -\frac{1}{2}aR^2$ (Conservative).
* $\mathbf{F} = bR^2\,\mathbf{e}_\theta \implies (\nabla \times \mathbf{F})_z = 3bR \neq 0$ (Non-conservative).
