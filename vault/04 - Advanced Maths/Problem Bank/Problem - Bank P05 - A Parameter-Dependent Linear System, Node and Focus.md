---
materia: Advanced Maths
tema: "Unit 4: planar linear systems and phase portraits"
bank_id: P05
title: "The system x' = A(a) x with A = (-4, a; 1, 0): type of the origin for every a, the stable node a = -3 with P, P^{-1}, P^{-1}AP, and the stable focus a = -8 in real form with its sense of rotation"
category: midterm_1_problem
archetype: linear-systems-phase-portrait
level: standard
unit: 4
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G47_SOL, MATHS_FIRSTPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p05.py"
tags:
  - problem-bank
  - midterm-1
  - phase-portrait
  - eigenvalues
  - change-of-basis
  - trace-determinant
  - complex-eigenvalues
---

# Bank P05 — A parameter-dependent linear system, node and focus

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G47_SOL and MATHS_FIRSTPARTIAL_2025_G47_SOL. Method: Topic 4 (eigenvalues and the characteristic polynomial, Robinson Ch. 27; distinct real eigenvalues and the change of coordinates $\mathbf z=P^{-1}\mathbf x$, Robinson Ch. 28 and Notes, p. 9; complex eigenvalues, Robinson Ch. 29 and [[Concept - Planar Systems with Complex Eigenvalues]]; repeated eigenvalue, Robinson Ch. 30 and [[Concept - Planar Systems with a Repeated Eigenvalue]]; trace-determinant classification, Robinson Ch. 31). Every result was checked with SymPy (scripts/am_bank/p05.py).

## Statement

For a real parameter $a$ consider the planar system

$$\dot{\mathbf x}=A(a)\,\mathbf x,\qquad A(a)=\begin{pmatrix}-4&a\\1&0\end{pmatrix},\qquad \mathbf x=\begin{pmatrix}x_1\\x_2\end{pmatrix}.$$

The type of the origin changes with $a$. Afterwards two values are studied in detail: $a=-3$, with initial condition $\mathbf x(0)=(1,1)^T$, and $a=-8$, with initial condition $\mathbf x(0)=(0,1)^T$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $\mathbf x(t)\in\mathbb R^2$, $t\in\mathbb R$; parameter $a\in\mathbb R$.
- Operator: first-order, linear, homogeneous, constant coefficients: solutions exist for all $t$, are unique, and $\mathbf x\equiv\mathbf0$ is always an equilibrium. It is the only one when $\det A\neq0$.
- The type of $\mathbf 0$ is read from $\tau=\operatorname{tr}A$, $\delta=\det A$ and $\Delta=\tau^2-4\delta$ (Robinson Ch. 31).

#### Phase 2. Canonical formulation

$\tau=-4+0=-4$ for every $a$, $\ \delta=(-4)(0)-a\cdot1=-a$, $\ \Delta=16+4a$. With an invertible matrix $P$ of (generalised) eigenvectors, $\mathbf x=P\mathbf z$ turns the system into $\dot{\mathbf z}=(P^{-1}AP)\,\mathbf z$ with $P^{-1}AP$ diagonal, a Jordan block, or the rotation-dilation block $\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}$.

## (a) Classification for all a [1.5 pts]

Classify the origin for every real $a$ (table with trace, determinant and discriminant) and describe the borderline cases.

### Hint

$\det(A-\lambda I)=\lambda^2-\tau\lambda+\delta$. The trace never changes: which types are impossible?

### Checkpoint

- $\lambda^2+4\lambda-a=0$, $\lambda=-2\pm\sqrt{4+a}$.
- $a>0$ saddle; $a=0$ line of equilibria $x_1=0$; $-4<a<0$ stable node; $a=-4$ degenerate (improper) stable node, single eigenvector $(-2,1)^T$; $a<-4$ stable focus, anticlockwise.
- Never a centre and never unstable apart from the saddle.

### Solution

#### Step 1. Characteristic polynomial

$$\det(A-\lambda I)=\det\begin{pmatrix}-4-\lambda&a\\1&-\lambda\end{pmatrix}=(-4-\lambda)(-\lambda)-a=\lambda^2+4\lambda-a,$$

$$\lambda_\pm=\frac{-4\pm\sqrt{16+4a}}{2}=-2\pm\sqrt{4+a}.$$

#### Step 2. Table

| Range of $a$ | $\tau$ | $\delta=-a$ | $\Delta=16+4a$ | Eigenvalues | Origin |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $a>0$ | $-4$ | $<0$ | $>16$ | real, opposite signs | saddle (unstable) |
| $a=0$ | $-4$ | $0$ | $16$ | $0$ and $-4$ | line of equilibria $x_1=0$ |
| $-4<a<0$ | $-4$ | $>0$ | $0<\Delta<16$ | real, both negative | stable node |
| $a=-4$ | $-4$ | $4$ | $0$ | $-2$ double | degenerate stable node |
| $a<-4$ | $-4$ | $>4$ | $<0$ | $-2\pm i\sqrt{-4-a}$ | stable focus |

For $-4<a<0$: $0<\sqrt{4+a}<2$, so both $-2\pm\sqrt{4+a}$ are negative. For $a>0$: $\sqrt{4+a}>2$, so $\lambda_+>0>\lambda_-$.

#### Step 3. Borderline values

- $a=0$: $A\mathbf x=\mathbf0$ means $-4x_1=0$ and $x_1=0$, so every point of the $x_2$-axis is an equilibrium (eigenvalue $0$, eigenvector $(0,1)^T$). For $\lambda=-4$, $(A+4I)\mathbf v=\mathbf0$ has rows $(0,0)$ and $(1,4)$: $v_1+4v_2=0$, $\mathbf v=(-4,1)^T$. Every other orbit is a half-line parallel to $(-4,1)^T$ that ends on the $x_2$-axis as $t\to\infty$.
- $a=-4$: $A+2I=\begin{pmatrix}-2&-4\\1&2\end{pmatrix}\neq0$; its second row gives $v_1+2v_2=0$, a single eigenvector line through $(-2,1)^T$. The origin is a degenerate (improper) stable node: all orbits approach it tangent to that line.
- $a<-4$: $\rho=-2$, $\omega=\sqrt{-4-a}$. Sense of rotation from the test vector $(1,0)^T$: $A(1,0)^T=(-4,1)^T$, whose second component is positive on the positive $x_1$-axis, so orbits turn **anticlockwise** (equivalently $a_{12}=a<0$).

Since $\tau=-4\neq0$ there is never a centre, and since $\tau<0$ there is never an unstable node or focus: the only unstable case is the saddle.

## (b) The stable node a = -3 [1.5 pts]

For $a=-3$ find eigenvalues and eigenvectors, build $P$, $P^{-1}$, check $P^{-1}AP$, write the general solution, solve with $\mathbf x(0)=(1,1)^T$ and describe the phase portrait.

### Hint

$\lambda=-2\pm1$. Solve $(A-\lambda I)\mathbf v=\mathbf0$ row by row; the slow direction is the eigenvector of the eigenvalue of smaller modulus.

### Checkpoint

- $\lambda_1=-1$, $\mathbf v_1=(1,-1)^T$; $\lambda_2=-3$, $\mathbf v_2=(3,-1)^T$.
- $P=\begin{pmatrix}1&3\\-1&-1\end{pmatrix}$, $\det P=2$, $P^{-1}=\frac12\begin{pmatrix}-1&-3\\1&1\end{pmatrix}$, $P^{-1}AP=\operatorname{diag}(-1,-3)$.
- $\mathbf x(t)=\big(-2e^{-t}+3e^{-3t},\ 2e^{-t}-e^{-3t}\big)^T$; stable node, tangent to $\mathbf v_1$ at the origin.

### Solution

#### Step 1. Eigenvectors

$A=\begin{pmatrix}-4&-3\\1&0\end{pmatrix}$, $\lambda^2+4\lambda+3=(\lambda+1)(\lambda+3)$.

- $\lambda_1=-1$: $A+I=\begin{pmatrix}-3&-3\\1&1\end{pmatrix}$. Row 1: $-3v_1-3v_2=0$; row 2: $v_1+v_2=0$ (the same line). $\mathbf v_1=(1,-1)^T$.
- $\lambda_2=-3$: $A+3I=\begin{pmatrix}-1&-3\\1&3\end{pmatrix}$. Row 1: $-v_1-3v_2=0$; row 2: $v_1+3v_2=0$. $\mathbf v_2=(3,-1)^T$.

#### Step 2. Change of basis

$$P=\begin{pmatrix}1&3\\-1&-1\end{pmatrix},\qquad \det P=(1)(-1)-(3)(-1)=2,\qquad P^{-1}=\frac12\begin{pmatrix}-1&-3\\1&1\end{pmatrix}.$$

Column by column, $AP=[A\mathbf v_1\mid A\mathbf v_2]$ with $A\mathbf v_1=(-4+3,\ 1)^T=(-1,1)^T=-\mathbf v_1$ and $A\mathbf v_2=(-12+3,\ 3)^T=(-9,3)^T=-3\mathbf v_2$:

$$AP=\begin{pmatrix}-1&-9\\1&3\end{pmatrix},\qquad P^{-1}AP=\frac12\begin{pmatrix}(-1)(-1)+(-3)(1)&(-1)(-9)+(-3)(3)\\(1)(-1)+(1)(1)&(1)(-9)+(1)(3)\end{pmatrix}=\frac12\begin{pmatrix}-2&0\\0&-6\end{pmatrix}=\begin{pmatrix}-1&0\\0&-3\end{pmatrix}.$$

#### Step 3. Solution

In $\mathbf z=P^{-1}\mathbf x$: $\dot z_1=-z_1$, $\dot z_2=-3z_2$, so $z_1=c_1e^{-t}$, $z_2=c_2e^{-3t}$ (each separable: $\frac{dz_i}{z_i}=\lambda_i\,dt$). Back with $\mathbf x=P\mathbf z$:

$$\mathbf x(t)=c_1e^{-t}\begin{pmatrix}1\\-1\end{pmatrix}+c_2e^{-3t}\begin{pmatrix}3\\-1\end{pmatrix}.$$

For $\mathbf x(0)=(1,1)^T$: $(c_1,c_2)^T=P^{-1}(1,1)^T=\frac12(-1-3,\ 1+1)^T=(-2,1)^T$, so

$$\mathbf x(t)=\begin{pmatrix}-2e^{-t}+3e^{-3t}\\2e^{-t}-e^{-3t}\end{pmatrix},\qquad \mathbf x(0)=\begin{pmatrix}1\\1\end{pmatrix}.$$

#### Step 4. Phase portrait in words

Both eigenvalues are negative: **stable node**. The eigenlines through $(1,-1)^T$ and $(3,-1)^T$ are invariant, with arrows towards the origin. In the $\mathbf z$-plane the orbits are $z_2=K\lvert z_1\rvert^{3}$ (exponent $\lambda_2/\lambda_1=3$), tangent to the $z_1$-axis at the origin. Back in $\mathbf x$: every orbit not on the fast line enters the origin tangent to the **slow** eigenvector $\mathbf v_1=(1,-1)^T$ ($\lvert\lambda_1\rvert=1$), and far from the origin ($t\to-\infty$) it is parallel to the fast one $\mathbf v_2=(3,-1)^T$. The orbit of the IVP behaves like $-2e^{-t}\mathbf v_1=e^{-t}(-2,2)^T$ for large $t$: it enters from the second quadrant along $x_2=-x_1$. Nullclines: $\dot x_1=0$ on $x_2=-\frac43x_1$, $\dot x_2=0$ on $x_1=0$ (there the motion is horizontal, $\dot x_1=-3x_2$).

## (c) The stable focus a = -8 [2.0 pts]

For $a=-8$ find the complex eigenvalues and an eigenvector $\mathbf v=\mathbf u+i\mathbf w$, build $Q=[\mathbf u\mid\mathbf w]$, $Q^{-1}$ and check $Q^{-1}AQ$; write the real general solution, solve with $\mathbf x(0)=(0,1)^T$ and find the sense of rotation.

### Hint

Use the second row of $(A-\lambda I)\mathbf v=\mathbf0$: it gives $v_1=\lambda v_2$. The canonical block is $\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}$.

### Checkpoint

- $\lambda=-2\pm2i$ ($\rho=-2$, $\omega=2$); $\mathbf v=(-2+2i,\ 1)^T$, $\mathbf u=(-2,1)^T$, $\mathbf w=(2,0)^T$.
- $Q=\begin{pmatrix}-2&2\\1&0\end{pmatrix}$, $\det Q=-2$, $Q^{-1}=\begin{pmatrix}0&1\\\frac12&1\end{pmatrix}$, $Q^{-1}AQ=\begin{pmatrix}-2&2\\-2&-2\end{pmatrix}$.
- $\mathbf x(t)=e^{-2t}\big(-4\sin2t,\ \cos2t+\sin2t\big)^T$; stable focus, anticlockwise in $\mathbf x$ (clockwise in $\mathbf z$), radius factor $e^{-2\pi}$ per turn.

### Solution

#### Step 1. Eigenvalues and eigenvector

$\lambda^2+4\lambda+8=0$: $\lambda=\frac{-4\pm\sqrt{16-32}}{2}=-2\pm2i$. For $\lambda=-2+2i$:

$$A-\lambda I=\begin{pmatrix}-2-2i&-8\\1&2-2i\end{pmatrix}.$$

Row 2: $v_1+(2-2i)v_2=0$; with $v_2=1$, $v_1=-2+2i$. Row 1 checks: $(-2-2i)(-2+2i)-8=(4-4i+4i-4i^2)-8=8-8=0$. So $\mathbf v=(-2+2i,1)^T=\mathbf u+i\mathbf w$ with $\mathbf u=(-2,1)^T$, $\mathbf w=(2,0)^T$.

#### Step 2. Action of A on u and w

$A\mathbf u=(8-8,\ -2)^T=(0,-2)^T=\rho\mathbf u-\omega\mathbf w=(4,-2)^T-(4,0)^T$. $\ A\mathbf w=(-8,\ 2)^T=\omega\mathbf u+\rho\mathbf w=(-4,2)^T+(-4,0)^T$. Both agree with Robinson Eq. 29.3.

#### Step 3. Change of basis

$$Q=\begin{pmatrix}-2&2\\1&0\end{pmatrix},\qquad \det Q=(-2)(0)-(2)(1)=-2,\qquad Q^{-1}=\frac1{-2}\begin{pmatrix}0&-2\\-1&-2\end{pmatrix}=\begin{pmatrix}0&1\\\frac12&1\end{pmatrix}.$$

$AQ=[A\mathbf u\mid A\mathbf w]=\begin{pmatrix}0&-8\\-2&2\end{pmatrix}$ and

$$Q^{-1}AQ=\begin{pmatrix}0\cdot0+1\cdot(-2)&0\cdot(-8)+1\cdot2\\\frac12\cdot0+1\cdot(-2)&\frac12\cdot(-8)+1\cdot2\end{pmatrix}=\begin{pmatrix}-2&2\\-2&-2\end{pmatrix}=\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}.$$

#### Step 4. Real general solution and the IVP

In $\mathbf z$: $\dot z_1=-2z_1+2z_2$, $\dot z_2=-2z_1-2z_2$; in polar form $\dot r=-2r$, $\dot\theta=-2$, so $r=r_0e^{-2t}$, $\theta=\theta_0-2t$ (Barrow: $[e^{2s}r(s)]_0^t=0$). Back in $\mathbf x$:

$$\mathbf x(t)=e^{-2t}\Big[(a_1\cos2t+b_1\sin2t)\,\mathbf u+(b_1\cos2t-a_1\sin2t)\,\mathbf w\Big],\qquad (a_1,b_1)^T=Q^{-1}\mathbf x(0).$$

For $\mathbf x(0)=(0,1)^T$: $(a_1,b_1)^T=(0\cdot0+1\cdot1,\ \frac12\cdot0+1\cdot1)^T=(1,1)^T$. Then

$$\mathbf x(t)=e^{-2t}\Big[(\cos2t+\sin2t)\begin{pmatrix}-2\\1\end{pmatrix}+(\cos2t-\sin2t)\begin{pmatrix}2\\0\end{pmatrix}\Big]=e^{-2t}\begin{pmatrix}-4\sin2t\\\cos2t+\sin2t\end{pmatrix}.$$

Check: $\mathbf x(0)=(0,1)^T$. By the product rule $\dot x_1=e^{-2t}(8\sin2t-8\cos2t)$, and $-4x_1-8x_2=e^{-2t}\big(16\sin2t-8\cos2t-8\sin2t\big)=e^{-2t}(8\sin2t-8\cos2t)$; $\dot x_2=e^{-2t}\big(-2\cos2t-2\sin2t-2\sin2t+2\cos2t\big)=-4e^{-2t}\sin2t=x_1$.

#### Step 5. Rotation and portrait

At $(1,0)^T$, $\dot{\mathbf x}=A(1,0)^T=(-4,1)^T$: the velocity on the positive $x_1$-axis points upward, so orbits turn **anticlockwise** in the $\mathbf x$-plane. In the $\mathbf z$-plane they turn clockwise ($\dot\theta=-2$); the sense flips because $\det Q=-2<0$. The origin is a **stable focus**: spirals shrinking by the factor $e^{2\pi\rho/\omega}=e^{-2\pi}\approx0.0019$ each turn (one turn every $\pi$ time units). The IVP orbit starts at $(0,1)^T$, moves into the half-plane $x_1<0$ and crosses the $x_2$-axis again at $t=\pi/2$, at $(0,-e^{-\pi})^T$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** for every $a<0$ all solutions tend to $\mathbf0$ as $t\to\infty$ (asymptotic stability); for $a=0$ they tend to points of the $x_2$-axis; for $a>0$ only the orbits on the stable eigenline reach the origin. As $a\to-4^\pm$ the node's two eigenlines merge (from $a>-4$) or the spiral's rotation rate $\omega=\sqrt{-4-a}$ goes to $0$ (from $a<-4$): the degenerate node is the common boundary.
- **Checks:** $P^{-1}AP$ and $Q^{-1}AQ$ were multiplied out; both IVP solutions satisfy the system and the initial data; $\operatorname{tr}(P^{-1}AP)=-4=\tau$ and $\det(P^{-1}AP)=3=\delta$ for $a=-3$, and the same for $a=-8$ ($-4$ and $8$).
- **Common mistakes in the exam:** (1) calling $a=0$ a node: the origin is not isolated; (2) ordering $Q=[\mathbf w\mid\mathbf u]$ and then expecting $\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}$ (that order gives the transpose); (3) reading the sense of rotation from the $\mathbf z$-plane, which is always clockwise, instead of from a test vector in $\mathbf x$; (4) making the node's orbits tangent to the fast eigenvector at the origin.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
