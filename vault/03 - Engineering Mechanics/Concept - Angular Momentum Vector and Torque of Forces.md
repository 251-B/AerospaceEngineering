---
subject: Mechanics Applied to Aerospace Engineering
topic: 4 - Angular Momentum and Central Forces
concept: Angular Momentum Vector and Torque of Forces
tags:
  - concept
  - angular-momentum
  - torque
  - cross-product
  - action-reaction
---

# Concept: Angular Momentum Vector and Torque of Forces

## 1. Physical Definition of Angular Momentum
In linear mechanics, the primary dynamic vector is linear momentum $\mathbf{p}_0 = m\mathbf{v}_0^P$. In rotational mechanics about a reference point $A$, the fundamental quantity is the moment of linear momentum, termed the **angular momentum vector** (Slide 3 & Notes Eq. 4.48):

$$ \mathbf{H}_{A0}^P = \mathbf{AP} \times \mathbf{p}_0^P = \left(\mathbf{r}_0^P - \mathbf{r}_0^A\right) \times m^P \mathbf{v}_0^P $$

### Key Properties:
* **Vector Nature:** $\mathbf{H}_{A0}^P$ is an axial vector perpendicular to both the position vector relative to $A$ ($\mathbf{AP}$) and the velocity vector $\mathbf{v}_0^P$:
  $$ \mathbf{H}_{A0}^P \cdot \mathbf{AP} = 0, \qquad \mathbf{H}_{A0}^P \cdot \mathbf{v}_0^P = 0 $$
* **Base Point Dependence:** Changing the reference center from $A$ to $B$:
  $$ \mathbf{H}_{B0}^P = \mathbf{H}_{A0}^P + \mathbf{BA} \times m^P \mathbf{v}_0^P $$
* **SI Units:** $\text{kg}\cdot\text{m}^2/\text{s} = \text{J}\cdot\text{s}$ (Dimensions: $[M][L]^2[T]^{-1}$).

---

## 2. Torque (Moment of a Force)
The moment of an applied force $\mathbf{F}$ acting on particle $P$ about reference point $A$ is the **torque** $\mathbf{M}_A$ (Slide 3 & Notes Eq. 4.51):

$$ \mathbf{M}_A = \mathbf{AP} \times \mathbf{F} = \left(\mathbf{r}_0^P - \mathbf{r}_0^A\right) \times \mathbf{F} $$

* **SI Units:** $\text{N}\cdot\text{m}$ (Dimensions: $[M][L]^2[T]^{-2}$).
* **Line of Action Invariance:** Moving the force vector along its line of action leaves $\mathbf{M}_A$ invariant because $\mathbf{AP}_\parallel \times \mathbf{F} = \mathbf{0}$.

---

## 3. Action-Reaction Symmetry for Torques
For two interacting particles $P$ and $Q$ exerting mutual collinear forces $\mathbf{F}^P = -\mathbf{F}^Q \parallel \mathbf{PQ}$:
$$ \mathbf{M}_A^P + \mathbf{M}_A^Q = \mathbf{AP} \times \mathbf{F}^P + \mathbf{AQ} \times (-\mathbf{F}^P) = (\mathbf{AP} - \mathbf{AQ}) \times \mathbf{F}^P = \mathbf{QP} \times \mathbf{F}^P \equiv \mathbf{0} $$
Internal torques in an isolated material system always sum to zero:
$$ \sum \mathbf{M}_A^{\text{internal}} \equiv \mathbf{0} $$
