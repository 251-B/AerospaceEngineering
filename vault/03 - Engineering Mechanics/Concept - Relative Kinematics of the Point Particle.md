---
subject: Mechanics Applied to Aerospace Engineering
topic: 5 - Relative Motion
concept: Relative Kinematics of the Point Particle
tags:
  - concept
  - topic-5
  - relative-kinematics
---

# Concept: Relative Kinematics of the Point Particle

Part of [[Topic 5 - Relative Motion]] (Sections 9–10).

## 1. Data of the moving frame (Slide 22)
$S_1 = \{A; \mathcal{B}_1\}$ is fully described by $\mathbf{r}_0^A(t)$ and its attitude $[{}_0R_1](t)$; from them come $\mathbf{v}_0^A, \mathbf{a}_0^A, \boldsymbol{\omega}_{10}, \boldsymbol{\alpha}_{10}$. If they are known a priori, they are not unknowns of the problem.

## 2. Composition formulas (Notes Eqs. 3.16, 3.26, 3.27; Slides 23–26)
$$ \mathbf{r}_0^P = \mathbf{r}_0^A + \mathbf{r}_1^P $$
$$ \mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P $$
$$ \mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
Each is obtained by differentiating the previous one in $S_0$ and applying the Coriolis theorem to every vector naturally described in $S_1$. The last three terms of $\mathbf{a}_0^P$ are the Euler, centripetal and Coriolis accelerations.

## 3. Remarks (Notes p. 39)
* The centripetal term equals $-\omega_{10}^2\mathbf{r}_\perp$: magnitude $r_\perp\omega_{10}^2$, pointing to the rotation axis through $A$.
* The factor 2 of the Coriolis term collects two equal contributions; it vanishes if $\mathbf{v}_1^P = \mathbf{0}$ or $\mathbf{v}_1^P\parallel\boldsymbol{\omega}_{10}$.
* Pure translation ($\boldsymbol{\omega}_{10} = \mathbf{0}$): $\mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P$, $\mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P$ (Notes Eqs. 3.28–3.29).
