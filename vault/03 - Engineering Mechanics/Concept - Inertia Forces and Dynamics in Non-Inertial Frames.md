---
subject: Mechanics Applied to Aerospace Engineering
topic: 5 - Relative Motion
concept: Inertia Forces and Dynamics in Non-Inertial Frames
tags:
  - concept
  - topic-5
  - inertia-forces
  - non-inertial-frames
---

# Concept: Inertia Forces and Dynamics in Non-Inertial Frames

Part of [[Topic 5 - Relative Motion]] (Sections 11–13). Builds on [[Concept - Newton Laws and Equations of Motion]].

## 1. Newton's law in a non-inertial frame (Notes Eqs. 4.59–4.63, Slide 27)
Substituting Notes Eq. 3.27 into $m^P\mathbf{a}_0^P = \mathbf{F}$ and keeping $m^P\mathbf{a}_1^P$ on the left:
$$ m^P\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i, \qquad \mathbf{F}_i = -m^P\mathbf{a}_0^A - m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P - m^P\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) - 2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$
The four terms are the force due to the acceleration of the origin $\mathbf{F}_A$, Euler's force $\mathbf{F}_E$, the centrifugal force $\mathbf{F}_C$ and the Coriolis force $\mathbf{F}_{COR}$ (Slide 28).

## 2. Properties (Slides 28–31)
* All are proportional to the mass; the first three are locally indistinguishable from gravity.
* $\mathbf{F}_A$ has potential $V_1 = m^P\mathbf{a}_0^A\cdot\mathbf{r}_1^P$ if $\mathbf{a}_0^A$ is constant.
* $\mathbf{F}_C = m^P\omega_{10}^2\mathbf{r}_\perp$ (outward from the axis) has potential $V_1 = -\tfrac12 m^P\omega_{10}^2 r_\perp^2$ if $\boldsymbol{\omega}_{10}$ is constant.
* $\mathbf{F}_E$ has no potential ($\nabla\times\mathbf{F}_E \neq \mathbf{0}$).
* $\mathbf{F}_{COR}\perp\mathbf{v}_1^P$: it never does work; it deflects eastward launches upward and westward launches downward at the equator (Slide 31).

## 3. Energy in $S_1$ (Slide 29)
$T_1^P$, $E_1^P$ and $\mathbf{H}_{A1}^P$ can always be defined in $S_1$. $E_1^P$ is conserved under the same conditions as in an inertial frame, now counting the inertia forces: typically a frame with fixed origin rotating at constant $\boldsymbol{\omega}_{10}$, conservative actual forces and constraints fixed in $S_1$.

> [!info] Two equivalent routes
> Either write $m\mathbf{a}_0^P = \mathbf{F}$ in $S_0$ with Eq. 3.27, or $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ in $S_1$. Choose the simplest option for each problem (Slide 28).
