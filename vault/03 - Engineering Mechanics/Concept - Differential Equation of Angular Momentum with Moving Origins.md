---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Differential Equation of Angular Momentum with Moving Origins
tags:
  - concept
  - angular-momentum
  - moving-origins
  - differential-equations
  - newton-second-law
---

# Concept: Differential Equation of Angular Momentum with Moving Origins

## 1. General Derivation for an Arbitrary Origin $A$
Taking the time derivative of $\mathbf{H}_{A0}^P = (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \mathbf{v}_0^P$ in the inertial reference frame $S_0$ (Slide 4 & Notes Eq. 4.49–4.52):

$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \frac{d}{dt}\left[ (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \mathbf{v}_0^P \right]_0 $$
Applying the product rule:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = (\mathbf{v}_0^P - \mathbf{v}_0^A) \times m^P \mathbf{v}_0^P + (\mathbf{r}_0^P - \mathbf{r}_0^A) \times m^P \mathbf{a}_0^P $$

Using Newton's Second Law $m^P \mathbf{a}_0^P = \mathbf{F}$ and the identity $\mathbf{v}_0^P \times \mathbf{v}_0^P = \mathbf{0}$:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A - \mathbf{v}_0^A \times m^P \mathbf{v}_0^P $$

---

## 2. Canonical Reductions

### Case 1: Fixed Reference Point ($\mathbf{v}_0^A = \mathbf{0}$)
When origin $A$ is stationary in the inertial frame $S_0$:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$
This is the fundamental rotational analogue to Newton's Second Law ($\dot{\mathbf{p}}_0 = \mathbf{F}$).

### Case 2: Origin Moving Parallel to Particle ($\mathbf{v}_0^A \parallel \mathbf{v}_0^P$)
When $\mathbf{v}_0^A \times \mathbf{v}_0^P = \mathbf{0}$, the transport cross product vanishes identically:
$$ \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{M}_A $$

### Case 3: Origin Moving with Constant Velocity ($\mathbf{a}_0^A = \mathbf{0}$)
In an auxiliary non-rotating frame $S_A$ centered at $A$:
$$ \frac{d\mathbf{H}_{AA}}{dt}\Bigg|_A = \mathbf{M}_A $$
where $\mathbf{H}_{AA} = \mathbf{AP} \times m\mathbf{v}_A^P$ is the relative angular momentum.

---

## 3. Conservation Criterion
When the resultant external torque about a fixed point $A$ vanishes:
$$ \mathbf{M}_A = \mathbf{0} \implies \frac{d\mathbf{H}_{A0}^P}{dt}\Bigg|_0 = \mathbf{0} \implies \mathbf{H}_{A0}^P = \text{constant vector} $$
This yields three independent scalar first integrals of motion.
