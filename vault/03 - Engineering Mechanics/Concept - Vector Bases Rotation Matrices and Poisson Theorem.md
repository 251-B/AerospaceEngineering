---
subject: Mechanics Applied to Aerospace Engineering
topic: 1 - Fundamentals and Particle Kinematics
tags:
  - theory
  - key-concept
  - rotation-matrices
  - change-of-basis
  - time-derivative
difficulty: medium
prerequisites:
  - "Linear Algebra (Orthogonal matrices)"
  - "Vector Calculus"
---

# 📖 Concept: Vector Bases, Rotation Matrices, and Poisson's Theorem

> **Key Takeaway in One Sentence:** Any transformation between orthonormal right-handed bases in $\mathbb{R}^3$ is equivalent to a pure rotation represented by an orthogonal matrix $[{}_0 R_1]$ ($\det = 1, R^{-1} = R^T$), and time differentiation in a rotating reference frame introduces the convective transport term $\boldsymbol{\omega} \times \mathbf{A}$.

---

## 🎯 1. Physical Principle and Intuition

In aerospace dynamics, vectors are routinely expressed across multiple reference frames:
* An Earth-fixed or inertial navigation frame.
* A body-fixed aircraft frame (nose, right wing, belly).
* A wind / aerodynamic frame aligned with the incoming free-stream velocity vector.

Transforming vector components between these frames without changing the physical vector requires **change-of-basis matrices $[{}_0 R_1]$**, which are mathematically identical to **pure spatial rotations**.

---

## 📐 2. Mathematical Formulation

### 2.1 Change-of-Basis Matrix $[{}_0 R_1]$
Given bases $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ and $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$:
$$ \begin{bmatrix} A_{x0} \\ A_{y0} \\ A_{z0} \end{bmatrix}_0 = [{}_0 R_1] \begin{bmatrix} A_{x1} \\ A_{y1} \\ A_{z1} \end{bmatrix}_1 $$
where the columns of $[{}_0 R_1]$ are the components of the unit vectors of $\mathcal{B}_1$ projected onto $\mathcal{B}_0$:
$$ [{}_0 R_1] = \begin{bmatrix} \mathbf{i}_1 \cdot \mathbf{i}_0 & \mathbf{j}_1 \cdot \mathbf{i}_0 & \mathbf{k}_1 \cdot \mathbf{i}_0 \\ \mathbf{i}_1 \cdot \mathbf{j}_0 & \mathbf{j}_1 \cdot \mathbf{j}_0 & \mathbf{k}_1 \cdot \mathbf{j}_0 \\ \mathbf{i}_1 \cdot \mathbf{k}_0 & \mathbf{j}_1 \cdot \mathbf{k}_0 & \mathbf{k}_1 \cdot \mathbf{k}_0 \end{bmatrix} $$

### 2.2 Properties of $[{}_0 R_1]$
1. **Orthogonality:** $[{}_1 R_0] = [{}_0 R_1]^{-1} = [{}_0 R_1]^T$.
2. **Determinant Unity:** $\det([{}_0 R_1]) = +1$.
3. **Euler's Rotation Theorem:** Every proper rotation has at least one invariant axis corresponding to eigenvalue $\lambda = 1$.
4. **Finite Rotation Composition:**
   $$ [R] = [R_n]\cdots[R_1] \implies [R_i][R_j] \neq [R_j][R_i] \quad (\text{non-commutative}) $$

### 2.3 Elementary Rotations About Coordinate Axes
$$ R_x(\theta_x) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta_x & -\sin\theta_x \\ 0 & \sin\theta_x & \cos\theta_x \end{bmatrix}, \quad R_y(\theta_y) = \begin{bmatrix} \cos\theta_y & 0 & \sin\theta_y \\ 0 & 1 & 0 \\ -\sin\theta_y & 0 & \cos\theta_y \end{bmatrix}, \quad R_z(\theta_z) = \begin{bmatrix} \cos\theta_z & -\sin\theta_z & 0 \\ \sin\theta_z & \cos\theta_z & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

---

## 🔍 3. Infinitesimal Rotations and Poisson's Theorem

### 3.1 Infinitesimal Rotations Commute
For differential rotations $d\theta_x, d\theta_y, d\theta_z \ll 1$:
$$ [R] \approx [U] + [\Omega]\,dt, \quad [\Omega] = \begin{bmatrix} 0 & -\dot{\theta}_z & \dot{\theta}_y \\ \dot{\theta}_z & 0 & -\dot{\theta}_x \\ -\dot{\theta}_y & \dot{\theta}_x & 0 \end{bmatrix} \implies [\Omega]\mathbf{A} \equiv \boldsymbol{\omega} \times \mathbf{A} $$

### 3.2 Poisson's Theorem (Kinematic Transport Formula)
The time derivative of the unit vectors of a moving frame $\mathcal{B}_1$ rotating at $\boldsymbol{\omega}_{10}$ relative to inertial frame $S_0$ is:
$$ \left.\frac{d\mathbf{i}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10} \times \mathbf{i}_1, \quad \left.\frac{d\mathbf{j}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10} \times \mathbf{j}_1, \quad \left.\frac{d\mathbf{k}_1}{dt}\right|_0 = \boldsymbol{\omega}_{10} \times \mathbf{k}_1 $$
For any arbitrary vector $\mathbf{A}(t)$:
$$ \left.\frac{d\mathbf{A}}{dt}\right|_0 = \left.\frac{d\mathbf{A}}{dt}\right|_1 + \boldsymbol{\omega}_{10} \times \mathbf{A} $$

---

## ⚠️ 4. Common Exam Pitfalls
> [!WARNING] Exam Precautions
> 1. Omitting the reference frame label: Writing $\dot{\mathbf{A}}$ is ambiguous when multiple frames are present. Always write $\left.\frac{d\mathbf{A}}{dt}\right|_0$ or $\left.\frac{d\mathbf{A}}{dt}\right|_1$.
> 2. Sign error in $R_y(\theta)$: Notice the $-\sin\theta$ term is at entry $(3,1)$ due to the right-hand cross product in the $z-x$ plane ($\mathbf{k} \times \mathbf{i} = \mathbf{j}$).

---

## 🔗 Related Concepts
* `[[Topic 1 - Fundamentals and Particle Kinematics|Topic 1: Fundamentals and Particle Kinematics]]`
* `[[Concept - Intrinsic Frenet-Serret Frame and Intrinsic Acceleration|Concept: Intrinsic Frenet-Serret Frame]]`
