---
subject: Mechanics Applied to Aerospace Engineering
topic: 5 - Relative Motion
concept: Attitude of a Reference Frame and Euler Angles
tags:
  - concept
  - topic-5
  - attitude
  - rotation-matrix
  - euler-angles
---

# Concept: Attitude of a Reference Frame and Euler Angles

Part of [[Topic 5 - Relative Motion]] (Sections 3–4). Builds on [[Concept - Vector Bases Rotation Matrices and Poisson Theorem]].

## 1. Attitude
The attitude of $S_1$ with respect to $S_0$ is the orientation of its basis $\mathcal{B}_1$; the origin plays no role (Slide 5). It is given by the change-of-basis relations $\mathbf{i}_1 = \ell_{x1,x0}\mathbf{i}_0 + \ell_{x1,y0}\mathbf{j}_0 + \ell_{x1,z0}\mathbf{k}_0$, etc. (Notes Eq. 1.8), or by the matrix
$$ [{}_0R_1] = \begin{bmatrix} \ell_{x1,x0} & \ell_{y1,x0} & \ell_{z1,x0} \\ \ell_{x1,y0} & \ell_{y1,y0} & \ell_{z1,y0} \\ \ell_{x1,z0} & \ell_{y1,z0} & \ell_{z1,z0} \end{bmatrix}, \qquad [\mathbf{b}]_0 = [{}_0R_1][\mathbf{b}]_1 $$
whose columns are $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ written in $\mathcal{B}_0$ and whose rows are $\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0$ written in $\mathcal{B}_1$ (Slide 6).

## 2. Properties
* Orthogonal: $[{}_0R_1]^{-1} = [{}_0R_1]^T$; right-handed bases give $\det[{}_0R_1] = 1$ (Notes Eqs. 1.14–1.15).
* Eigenvalues $1, e^{\pm i\beta}$: the eigenvector of $\lambda = 1$ is the axis of the single equivalent rotation and $\beta$ is its angle (Slide 6, Notes Sec. 1.5.1).
* Composition: $[{}_0R_2] = [{}_0R_1][{}_1R_2]$, not commutative (Notes Eq. 1.16, Slide 7).

## 3. Simple rotations and Euler angles
A simple rotation has its axis along a basis vector (Slide 8, Notes Eqs. 1.18–1.20). Any attitude is the composition of three simple rotations about axes that are not repeated consecutively (Slide 9):
* **3-1-3 (standard)**: precession $\psi$ about $\mathbf{k}_0$, nutation $\theta$ about $\mathbf{i}_1$, spin $\varphi$ about $\mathbf{k}_2$.
* **3-2-1 (flight mechanics)**: yaw $\psi$ about $\mathbf{k}_b$, pitch $\theta$ about $\mathbf{j}_1$, roll $\varphi$ about $\mathbf{i}_2$ (Slides 10–13).

> [!tip] Avoiding sign errors
> Draw each simple rotation looking down from its stationary axis (Notes Sec. 1.5.2), write the new vectors in the old ones, and put them as columns.
