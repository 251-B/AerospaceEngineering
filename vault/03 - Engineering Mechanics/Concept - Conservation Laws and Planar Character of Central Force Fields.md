---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Conservation Laws and Planar Character of Central Force Fields
tags:
  - concept
  - central-forces
  - angular-momentum-conservation
  - planar-motion
  - polar-coordinates
---

# Concept: Conservation Laws and Planar Character of Central Force Fields

## 1. Central Force Definition
A force $\mathbf{F}$ is a **central force** with respect to a fixed origin $O$ if its line of action passes through $O$ at all times (Slide 7 & Notes 4.8.1):

$$ \mathbf{F} = F(r)\,\mathbf{e}_r = F(r)\,\frac{\mathbf{r}}{r} $$

---

## 2. Invariance of Angular Momentum & Proof of Planar Motion
Taking torques about the center of attraction $O$:
$$ \mathbf{M}_O = \mathbf{r} \times \mathbf{F} = \mathbf{r} \times \left(F(r)\frac{\mathbf{r}}{r}\right) = \frac{F(r)}{r}(\mathbf{r} \times \mathbf{r}) \equiv \mathbf{0} $$

By the angular momentum theorem about fixed point $O$:
$$ \frac{d\mathbf{H}_{O0}^P}{dt}\Bigg|_0 = \mathbf{0} \implies \mathbf{H}_{O0}^P = \mathbf{r} \times m\mathbf{v}_0^P = \mathbf{H} = \text{constant vector} $$

### Proof of Planar Trajectory:
By vector properties of the cross product:
$$ \mathbf{r}(t) \cdot \mathbf{H} = \mathbf{r} \cdot (\mathbf{r} \times m\mathbf{v}) \equiv 0 $$
$$ \mathbf{v}(t) \cdot \mathbf{H} = \mathbf{v} \cdot (\mathbf{r} \times m\mathbf{v}) \equiv 0 $$
Because $\mathbf{H}$ is a non-zero constant vector fixed in space, both position $\mathbf{r}(t)$ and velocity $\mathbf{v}(t)$ lie permanently in the invariant plane through $O$ orthogonal to $\mathbf{H}$.

---

## 3. Five Core Properties of Central Force Motion
1. **Vector First Integral:** $\mathbf{H}_{O0}^P = \text{const}$ (3 scalar conservation laws).
2. **Strictly 2D Motion:** Confined to the plane $z = 0$ perpendicular to $\mathbf{H}$.
3. **Polar Coordinates:** Trajectory described by $(r, \theta)$ in the plane.
4. **Inverse Speed-Radius Scaling:** Specific angular momentum $h = r^2\dot{\theta} = \text{const} \implies \dot{\theta} = h/r^2$. Angular rate increases as radius decreases.
5. **Origin Inaccessibility ($r \to 0$ Barrier):** For the Newtonian attraction (and any central force weaker than $1/r^3$) a particle with $h \ne 0$ cannot reach the center $O$, because the centrifugal kinetic barrier $\frac{m h^2}{2r^2} \to +\infty$ as $r \to 0$ (Notes Sec. 4.8.1, property 5). This is not general: for $F \propto 1/r^3$ with $h^2 < \mu$ and for $F \propto 1/r^4$ (Problem 42) the attraction wins and the particle reaches $r = 0$.
