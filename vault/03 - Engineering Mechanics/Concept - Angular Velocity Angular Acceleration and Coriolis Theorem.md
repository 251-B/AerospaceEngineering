---
subject: Mechanics Applied to Aerospace Engineering
topic: 5 - Relative Motion
concept: Angular Velocity, Angular Acceleration and Coriolis Theorem
tags:
  - concept
  - topic-5
  - angular-velocity
  - coriolis-theorem
---

# Concept: Angular Velocity, Angular Acceleration and the Coriolis Theorem

Part of [[Topic 5 - Relative Motion]] (Sections 5–8).

## 1. Angular velocity and acceleration
$\boldsymbol{\omega}_{10}$ points along the instantaneous axis of rotation of $\mathcal{B}_1$ relative to $\mathcal{B}_0$ (right-hand rule) and its magnitude is the angular rate (Slide 14). It is unrelated to the motion of the origin. The basis vectors of $S_1$ change, seen from $S_0$, as $\left.d\mathbf{i}_1/dt\right|_0 = \boldsymbol{\omega}_{10}\times\mathbf{i}_1$ (Notes Eqs. 3.3–3.5). The angular acceleration is $\boldsymbol{\alpha}_{10} = \left.d\boldsymbol{\omega}_{10}/dt\right|_0$; its component along $\boldsymbol{\omega}_{10}$ changes the rate, its perpendicular component changes the axis (Slide 15).

## 2. Coriolis theorem (Notes Eq. 3.8, Slide 17)
$$ \left.\frac{d\mathbf{b}}{dt}\right|_0 = \left.\frac{d\mathbf{b}}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\mathbf{b} $$
Proof: write $\mathbf{b} = b_{x1}\mathbf{i}_1 + b_{y1}\mathbf{j}_1 + b_{z1}\mathbf{k}_1$, apply the product rule in $S_0$; the derivatives of the components give $d\mathbf{b}/dt|_1$, the derivatives of the basis vectors give $\boldsymbol{\omega}_{10}\times\mathbf{b}$. Translation of $S_1$ does not change the result. Applied to $\boldsymbol{\omega}_{10}$ itself: $\boldsymbol{\alpha}_{10}$ is the same in $S_0$ and $S_1$ (Notes Eq. 3.9).

## 3. Composition (Notes Eqs. 3.13–3.15, Slide 19)
$$ \boldsymbol{\omega}_{20} = \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10}, \qquad \boldsymbol{\alpha}_{20} = \boldsymbol{\alpha}_{21} + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21} + \boldsymbol{\alpha}_{10}, \qquad \boldsymbol{\omega}_{01} = -\boldsymbol{\omega}_{10} $$
For Euler angles, each simple rotation contributes its angle rate times its axis: $\boldsymbol{\omega}_{30} = \dot\varphi\,\mathbf{k}_2 + \dot\theta\,\mathbf{i}_1 + \dot\psi\,\mathbf{k}_0$ for 3-1-3 (Slides 20–21).

> [!warning] Same basis before adding
> A vector can be defined in one frame, differentiated in another and expressed in a third basis (Slide 17). Before adding vectors in components, express all of them in the same basis.
