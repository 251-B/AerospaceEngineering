---
title: "Formula Sheet - Topic 5: Relative Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
ground_truth: "slides/05_-_Relative_motion.pdf & teoria/Notes.pdf (Secs. 1.5, 1.7, Ch. 3, Sec. 4.9)"
tier: "Formula Cheat Sheet"
language: "English"
tags:
  - formula-sheet
  - topic-5
  - relative-motion
  - coriolis-theorem
---

# 📑 Formula Sheet: Topic 5 — Relative Motion

Theory: [[Topic 5 - Relative Motion]]. Notation: $S_0 = \{O; \mathcal{B}_0\}$ fixed (inertial), $S_1 = \{A; \mathcal{B}_1\}$ moving; subscript = observer, superscript = point.

## 1. Attitude (change of basis)

| Result | Formula | Source |
| :--- | :--- | :--- |
| Change of basis | $[\mathbf{b}]_0 = [{}_0R_1]\,[\mathbf{b}]_1$, columns of $[{}_0R_1]$ = $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$ | Notes Eqs. 1.12–1.13, Slide 5 |
| Orthogonality | $[{}_1R_0] = [{}_0R_1]^{-1} = [{}_0R_1]^T$, $\det[{}_0R_1] = 1$ | Notes Eqs. 1.14–1.15, Slide 6 |
| Eigenvalues | $\lambda = 1, e^{i\beta}, e^{-i\beta}$: axis = eigenvector of $\lambda = 1$, angle $\beta$ | Slide 6 |
| Composition | $[{}_0R_2] = [{}_0R_1]\,[{}_1R_2]$ (not commutative) | Notes Eq. 1.16, Slide 7 |
| Simple rotation about $z$ | $[{}_0R_1(z,\theta_z)] = \begin{bmatrix} \cos\theta_z & -\sin\theta_z & 0 \\ \sin\theta_z & \cos\theta_z & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | Notes Eq. 1.20, Slide 8 |
| Simple rotation about $x$ | $[{}_0R_1(x,\theta_x)] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta_x & -\sin\theta_x \\ 0 & \sin\theta_x & \cos\theta_x \end{bmatrix}$ | Notes Eq. 1.18, Slide 8 |
| Simple rotation about $y$ | $[{}_0R_1(y,\theta_y)] = \begin{bmatrix} \cos\theta_y & 0 & \sin\theta_y \\ 0 & 1 & 0 \\ -\sin\theta_y & 0 & \cos\theta_y \end{bmatrix}$ | Notes Eq. 1.19, Slide 8 |
| Euler angles 3-1-3 | $[{}_0R_3] = [{}_0R_1(z,\psi)]\,[{}_1R_2(x,\theta)]\,[{}_2R_3(z,\varphi)]$ (precession, nutation, spin) | Slide 9 |
| Euler angles 3-2-1 | yaw $\psi$ about $\mathbf{k}$, pitch $\theta$ about $\mathbf{j}_1$, roll $\varphi$ about $\mathbf{i}_2$ | Slides 9–13 |

## 2. Angular motion and Coriolis theorem

| Result | Formula | Source |
| :--- | :--- | :--- |
| Basis vectors | $\left.\frac{d\mathbf{i}_1}{dt}\right\|_0 = \boldsymbol{\omega}_{10}\times\mathbf{i}_1$ (same for $\mathbf{j}_1, \mathbf{k}_1$) | Notes Eqs. 3.3–3.5, Slide 14 |
| Constant vector in $S_1$ | $\left.\frac{d\mathbf{c}}{dt}\right\|_0 = \boldsymbol{\omega}_{10}\times\mathbf{c}$ | Slide 14 |
| Angular acceleration | $\boldsymbol{\alpha}_{10} = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right\|_0 = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right\|_1$ | Notes Eq. 3.9, Slide 15 |
| **Coriolis theorem** | $\left.\frac{d\mathbf{b}}{dt}\right\|_0 = \left.\frac{d\mathbf{b}}{dt}\right\|_1 + \boldsymbol{\omega}_{10}\times\mathbf{b}$ | Notes Eq. 3.8, Slide 17 |
| Composition | $\boldsymbol{\omega}_{20} = \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10}$, $\boldsymbol{\alpha}_{20} = \boldsymbol{\alpha}_{21} + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{21} + \boldsymbol{\alpha}_{10}$ | Notes Eqs. 3.14–3.15, Slide 19 |
| Inverse | $\boldsymbol{\omega}_{01} = -\boldsymbol{\omega}_{10}$, $\boldsymbol{\alpha}_{01} = -\boldsymbol{\alpha}_{10}$ | Notes Eq. 3.13, Slide 19 |
| Simple rotation | $\boldsymbol{\omega}_{10} = \dot\psi\,\mathbf{k}_0$ for a rotation $\psi(t)$ about $\mathbf{k}_0$ | Slide 16 |
| 3-1-3 angular velocity | $\boldsymbol{\omega}_{30} = \dot\varphi\,\mathbf{k}_2 + \dot\theta\,\mathbf{i}_1 + \dot\psi\,\mathbf{k}_0$ | Slides 20–21 |
| 3-1-3 in $\mathcal{B}_3$ | $(\dot\theta\cos\varphi + \dot\psi\sin\varphi\sin\theta)\mathbf{i}_3 + (-\dot\theta\sin\varphi + \dot\psi\cos\varphi\sin\theta)\mathbf{j}_3 + (\dot\varphi + \dot\psi\cos\theta)\mathbf{k}_3$ | Slide 21 |
| 3-2-1 in body axes | $(\dot\varphi - \dot\psi\sin\theta)\mathbf{i}_r + (\dot\theta\cos\varphi + \dot\psi\cos\theta\sin\varphi)\mathbf{j}_r + (\dot\psi\cos\theta\cos\varphi - \dot\theta\sin\varphi)\mathbf{k}_r$ | Slide 21 exercise |

## 3. Relative kinematics

| Result | Formula | Source |
| :--- | :--- | :--- |
| Position | $\mathbf{r}_0^P = \mathbf{r}_0^A + \mathbf{r}_1^P$ | Notes Eq. 3.16, Slide 23 |
| Velocity | $\mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P$ | Notes Eq. 3.26, Slide 24 |
| Acceleration | $\mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ | Notes Eq. 3.27, Slide 25 |
| Pure translation | $\mathbf{v}_0^P = \mathbf{v}_0^A + \mathbf{v}_1^P$, $\mathbf{a}_0^P = \mathbf{a}_0^A + \mathbf{a}_1^P$ | Notes Eqs. 3.28–3.29 |
| Centripetal term | $\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) = -\omega_{10}^2\,\mathbf{r}_\perp$ | Slide 30 |

## 4. Relative dynamics

| Result | Formula | Units | Source |
| :--- | :--- | :---: | :--- |
| Newton in $S_1$ | $m^P\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ | N | Notes Eq. 4.63, Slide 27 |
| Inertia force | $\mathbf{F}_i = -m^P\mathbf{a}_0^A - m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P - m^P\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) - 2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ | N | Notes Eq. 4.62, Slide 28 |
| Origin acceleration | $\mathbf{F}_A = -m^P\mathbf{a}_0^A$, $V_1 = m^P\mathbf{a}_0^A\cdot\mathbf{r}_1^P$ if $\mathbf{a}_0^A$ const | N, J | Slide 29 |
| Euler force | $\mathbf{F}_E = -m^P\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$, no potential ($\nabla\times\mathbf{F}_E \neq \mathbf{0}$) | N | Slide 31 |
| Centrifugal force | $\mathbf{F}_C = m^P\omega_{10}^2\,\mathbf{r}_\perp$, $V_1 = -\tfrac12 m^P\omega_{10}^2 r_\perp^2$ if $\boldsymbol{\omega}_{10}$ const | N, J | Slide 30 |
| Coriolis force | $\mathbf{F}_{COR} = -2m^P\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$, $\mathbf{F}_{COR}\cdot\mathbf{v}_1^P = 0$ (no work) | N | Slide 31 |
| Energy in $S_1$ | $E_1^P = \tfrac12 m^P\vert\mathbf{v}_1^P\vert^2 + V - \tfrac12 m^P\omega_{10}^2 r_\perp^2$ conserved if $\mathbf{a}_0^A = \mathbf{0}$, $\boldsymbol{\omega}_{10}$ const, conservative actual forces, constraints fixed in $S_1$ | J | Slide 29 |

## 5. Dimensional checks
* $[\boldsymbol{\omega}_{10}] = \text{s}^{-1}$, $[\boldsymbol{\alpha}_{10}] = \text{s}^{-2}$.
* $[\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P] = \text{s}^{-1}\cdot\text{m} = \text{m/s}$; $[\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P] = [\omega^2 r] = [\omega v] = \text{m/s}^2$.
* $[m\,\omega^2 r_\perp^2] = \text{kg}\,\text{m}^2/\text{s}^2 = \text{J}$.
