---
materia: Advanced Maths
tema: "Unit 4: linear systems with complex eigenvalues"
bank_id: P06
title: "Inverse problem: rebuild the matrix of a spiral sink from one real solution, solve an IVP and measure the decay per turn"
category: midterm_1_problem
archetype: linear-systems-phase-portrait
level: trap
unit: 4
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL and MATHS_FIRSTPARTIAL_2021_G45_SOL; not an official exercise. Verified with scripts/am_bank/p06.py"
tags:
  - problem-bank
  - midterm-1
  - complex-eigenvalues
  - inverse-problem
  - stable-focus
  - phase-portrait
  - change-of-basis
---

# Bank P06 — Rebuilding a spiral system from one real solution

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL and MATHS_FIRSTPARTIAL_2021_G45_SOL. Method: Robinson Ch. 29 (complex eigenvalues, real solutions $e^{\rho t}(\cos\omega t\,\mathbf u-\sin\omega t\,\mathbf w)$, canonical form $J=\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}$), Ch. 31 (classification) and [[Concept - Planar Systems with Complex Eigenvalues]]. Every result was checked with SymPy (scripts/am_bank/p06.py).

## Statement

The real $2\times2$ matrix $A$ of the linear system $\mathbf x'=A\mathbf x$, $\mathbf x=(x,y)^T$, is unknown. The only information available is that the system has the real solution

$$\mathbf x_1(t)=e^{-t}\begin{pmatrix}\cos 2t-\sin 2t\\ \cos 2t-2\sin 2t\end{pmatrix}.$$

(a) Reconstruct $A$. Show that its eigenvalues are $-1\pm 2i$, find a complex eigenvector, and check that $P^{-1}AP$ is the real canonical form, with $P$ the matrix whose columns are the real and imaginary parts of that eigenvector.

(b) Find a second real solution, prove that the two solutions form a fundamental set, write the real general solution and solve the initial value problem $\mathbf x(0)=(1,0)^T$.

(c) Classify the origin. Do the trajectories spiral in or out? Is the rotation clockwise or counter-clockwise? Justify with a test vector.

(d) Let $V(x,y)=5x^2-6xy+2y^2$. Show that $V(\mathbf x)=\lvert P^{-1}\mathbf x\rvert^2$ and that $\frac{d}{dt}V(\mathbf x(t))=-2V(\mathbf x(t))$ along every solution. For the solution of (b), find the time needed for $\sqrt V$ to halve, and the first time $t>0$ at which the solution is back on the positive $x$ axis, with the ratio of its distances to the origin there and at $t=0$. Is the Euclidean distance $\lvert\mathbf x(t)\rvert$ decreasing for every solution?

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns: the four real entries of $A$; then the solutions $\mathbf x(t)\in\mathbb R^2$, $t\in\mathbb R$.
- Operator: first-order, linear, homogeneous, constant coefficients, planar. Solutions exist for all $t$ and are unique for given $\mathbf x(0)$ (existence and uniqueness for linear systems).
- Datum: one solution $\mathbf x_1$. Since $\mathbf x_1'(t)=A\mathbf x_1(t)$ for every $t$, evaluating at two instants where $\mathbf x_1$ takes independent values gives $A$ on a basis, hence $A$.
- Course convention (Robinson Ch. 29): if $\lambda=\rho+i\omega$ ($\omega>0$) has eigenvector $\boldsymbol\eta=\mathbf u+i\mathbf w$, the real solutions are $e^{\rho t}(\cos\omega t\,\mathbf u-\sin\omega t\,\mathbf w)$ and $e^{\rho t}(\sin\omega t\,\mathbf u+\cos\omega t\,\mathbf w)$.

| Quantity | Value |
| :--- | :--- |
| $\mathbf x_1(0)$ | $(1,1)^T$ |
| $\mathbf x_1(\pi/4)$ | $e^{-\pi/4}(-1,-2)^T$ |
| Initial condition (b) | $\mathbf x(0)=(1,0)^T$ |

#### Phase 2. Canonical formulation

Matrix form $\mathbf x'=A\mathbf x$. The target canonical form ("frame" of the problem) is $\mathbf z'=J\mathbf z$ with $\mathbf x=P\mathbf z$, $P=[\mathbf u\mid\mathbf w]$ and $J=\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}$, so that $A=PJP^{-1}$.

## (a) Reconstruct A, its eigenvalues and eigenvector, and check the canonical form [1.5 pts]

### Hint

Differentiate $\mathbf x_1$ with the product rule and impose $\mathbf x_1'=A\mathbf x_1$ at $t=0$ and $t=\pi/4$. Then compare $\mathbf x_1$ with $e^{\rho t}(\cos\omega t\,\mathbf u-\sin\omega t\,\mathbf w)$.

### Checkpoint

- $A=\begin{pmatrix}-7&4\\-10&5\end{pmatrix}$, $\operatorname{tr}A=-2$, $\det A=5$, $p(\lambda)=\lambda^2+2\lambda+5$, $\lambda=-1\pm2i$.
- $\boldsymbol\eta=(1+i,\ 1+2i)^T$, $\mathbf u=(1,1)^T$, $\mathbf w=(1,2)^T$.
- $P=\begin{pmatrix}1&1\\1&2\end{pmatrix}$, $\det P=1$, $P^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$, $P^{-1}AP=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix}$.

### Solution

#### Step 1. Derivative of the given solution

Write $c=\cos2t$, $s=\sin2t$. By the chain rule $\frac{d}{dt}\cos2t=-2\sin2t$, $\frac{d}{dt}\sin2t=2\cos2t$, and by the product rule $\frac{d}{dt}\big(e^{-t}g(t)\big)=-e^{-t}g(t)+e^{-t}g'(t)$:

$$\mathbf x_1'(t)=-e^{-t}\begin{pmatrix}c-s\\c-2s\end{pmatrix}+e^{-t}\begin{pmatrix}-2s-2c\\-2s-4c\end{pmatrix}=e^{-t}\begin{pmatrix}-3c-s\\-5c\end{pmatrix}$$

#### Step 2. Two instants give A on a basis

At $t=0$ ($c=1$, $s=0$): $\mathbf x_1(0)=(1,1)^T$, $\mathbf x_1'(0)=(-3,-5)^T$. At $t=\pi/4$ ($c=0$, $s=1$): $\mathbf x_1(\pi/4)=e^{-\pi/4}(-1,-2)^T$, $\mathbf x_1'(\pi/4)=e^{-\pi/4}(-1,0)^T$. Dividing the second relation by $-e^{-\pi/4}$:

$$A\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}-3\\-5\end{pmatrix},\qquad A\begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}$$

With $P=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ this reads $AP=\begin{pmatrix}-3&1\\-5&0\end{pmatrix}$. $\det P=1\cdot2-1\cdot1=1\neq0$, and $P^{-1}=\frac{1}{1}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$, so $A=(AP)P^{-1}$ entry by entry:

$$\begin{aligned}A_{11}&=(-3)(2)+(1)(-1)=-7, & A_{12}&=(-3)(-1)+(1)(1)=4,\\ A_{21}&=(-5)(2)+(0)(-1)=-10, & A_{22}&=(-5)(-1)+(0)(1)=5.\end{aligned}$$

$$A=\begin{pmatrix}-7&4\\-10&5\end{pmatrix}$$

#### Step 3. Eigenvalues

$$p(\lambda)=\det(A-\lambda I)=(-7-\lambda)(5-\lambda)-(4)(-10)=\lambda^2+2\lambda-35+40=\lambda^2+2\lambda+5$$

$\lambda=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$, so $\rho=-1$, $\omega=2$. Check: $\operatorname{tr}A=-2=2\rho$, $\det A=-35+40=5=\rho^2+\omega^2$.

#### Step 4. Eigenvector from $(A-\lambda I)\boldsymbol\eta=\mathbf 0$

For $\lambda=-1+2i$, row 1: $(-7-(-1+2i))\eta_1+4\eta_2=0$, i.e. $(-6-2i)\eta_1+4\eta_2=0$, so $\eta_2=\frac{3+i}{2}\eta_1$. Taking $\eta_1=1+i$: $\eta_2=\frac{(3+i)(1+i)}{2}=\frac{3+3i+i-1}{2}=1+2i$. Row 2 as a check: $-10(1+i)+(5-(-1+2i))(1+2i)=-10-10i+(6-2i)(1+2i)=-10-10i+6+12i-2i+4=0$. Hence

$$\boldsymbol\eta=\begin{pmatrix}1+i\\1+2i\end{pmatrix}=\underbrace{\begin{pmatrix}1\\1\end{pmatrix}}_{\mathbf u}+i\underbrace{\begin{pmatrix}1\\2\end{pmatrix}}_{\mathbf w}$$

and indeed $\mathbf x_1=e^{-t}(\cos2t\,\mathbf u-\sin2t\,\mathbf w)$: the given curve is the real part of $e^{\lambda t}\boldsymbol\eta$.

#### Step 5. Frame check $P^{-1}AP=J$

$P=[\mathbf u\mid\mathbf w]$ is the matrix of Step 2. With $AP=\begin{pmatrix}-3&1\\-5&0\end{pmatrix}$:

$$\begin{aligned}(P^{-1}AP)_{11}&=2(-3)+(-1)(-5)=-1, & (P^{-1}AP)_{12}&=2(1)+(-1)(0)=2,\\ (P^{-1}AP)_{21}&=(-1)(-3)+1(-5)=-2, & (P^{-1}AP)_{22}&=(-1)(1)+1(0)=-1.\end{aligned}$$

$$P^{-1}AP=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix}=\begin{pmatrix}\rho&\omega\\-\omega&\rho\end{pmatrix}=J$$

## (b) Second real solution, fundamental set, general solution and IVP [1.5 pts]

### Hint

Take the imaginary part of $e^{\lambda t}\boldsymbol\eta$. The Wronskian at $t=0$ is $\det[\mathbf u\mid\mathbf w]$.

### Checkpoint

- $\mathbf x_2(t)=e^{-t}\begin{pmatrix}\sin2t+\cos2t\\ \sin2t+2\cos2t\end{pmatrix}$, $W(0)=1\neq0$.
- $\mathbf x(t)=c_1\mathbf x_1(t)+c_2\mathbf x_2(t)$; IVP: $c_1=2$, $c_2=-1$.
- $\mathbf x(t)=e^{-t}\begin{pmatrix}\cos2t-3\sin2t\\-5\sin2t\end{pmatrix}$.

### Solution

#### Step 1. Complex solution split into real and imaginary parts

With Euler's formula $e^{(-1+2i)t}=e^{-t}(\cos2t+i\sin2t)$:

$$e^{\lambda t}\boldsymbol\eta=e^{-t}(\cos2t+i\sin2t)(\mathbf u+i\mathbf w)=e^{-t}\big[(\cos2t\,\mathbf u-\sin2t\,\mathbf w)+i(\sin2t\,\mathbf u+\cos2t\,\mathbf w)\big]$$

Since $A$ is real, real and imaginary parts are real solutions (Robinson Ch. 29). The real part is $\mathbf x_1$; the imaginary part is

$$\mathbf x_2(t)=e^{-t}(\sin2t\,\mathbf u+\cos2t\,\mathbf w)=e^{-t}\begin{pmatrix}\sin2t+\cos2t\\ \sin2t+2\cos2t\end{pmatrix}$$

#### Step 2. Fundamental set

$\mathbf x_1(0)=\mathbf u$, $\mathbf x_2(0)=\mathbf w$, so the Wronskian at $t=0$ is $W(0)=\det\begin{pmatrix}1&1\\1&2\end{pmatrix}=2-1=1\neq0$. By Abel's formula $W(t)=W(0)e^{(\operatorname{tr}A)t}=e^{-2t}\neq0$ for all $t$: the solutions are independent and the general real solution is

$$\mathbf x(t)=c_1e^{-t}\begin{pmatrix}\cos2t-\sin2t\\ \cos2t-2\sin2t\end{pmatrix}+c_2e^{-t}\begin{pmatrix}\sin2t+\cos2t\\ \sin2t+2\cos2t\end{pmatrix},\qquad c_1,c_2\in\mathbb R$$

#### Step 3. Initial condition

At $t=0$: $c_1\mathbf u+c_2\mathbf w=(1,0)^T$, i.e. $c_1+c_2=1$ and $c_1+2c_2=0$. Subtracting, $c_2=-1$, then $c_1=2$:

$$\mathbf x(t)=e^{-t}\begin{pmatrix}2(\cos2t-\sin2t)-(\sin2t+\cos2t)\\ 2(\cos2t-2\sin2t)-(\sin2t+2\cos2t)\end{pmatrix}=e^{-t}\begin{pmatrix}\cos2t-3\sin2t\\-5\sin2t\end{pmatrix}$$

#### Step 4. Check by substitution

$\mathbf x(0)=(1,0)^T$. With $c=\cos2t$, $s=\sin2t$, the product rule gives $\mathbf x'=e^{-t}\big(-(c-3s)+(-2s-6c),\ 5s-10c\big)^T=e^{-t}(-7c+s,\ -10c+5s)^T$, and $A\mathbf x=e^{-t}\big(-7(c-3s)+4(-5s),\ -10(c-3s)+5(-5s)\big)^T=e^{-t}(-7c+s,\ -10c+5s)^T$. They agree.

## (c) Classification, spiralling and sense of rotation [1.0 pts]

### Hint

Sign of $\rho$; then compute $A\mathbf x$ at a point of the positive $x$ axis, or the sign of $xy'-yx'$.

### Checkpoint

- $\rho=-1<0$, $\omega=2\neq0$: **stable focus** (spiral sink); $\operatorname{tr}A=-2<0$, $\det A=5>0$, $(\operatorname{tr}A)^2-4\det A=-16<0$.
- $A(1,0)^T=(-7,-10)^T$: **clockwise** rotation.
- $xy'-yx'=-2(5x^2-6xy+2y^2)<0$ off the origin.

### Solution

#### Step 1. Type

The eigenvalues are complex with negative real part, so every solution is $e^{-t}$ times a bounded $\pi$-periodic vector: it tends to $\mathbf 0$ while winding around it. The origin is a stable focus (Robinson Ch. 31; trace-determinant plane: $\operatorname{tr}<0$, $\det>0$, discriminant $<0$).

#### Step 2. Test vector

At $(1,0)$, on the positive $x$ axis, $\mathbf x'=A(1,0)^T=(-7,-10)^T$: the $y$ component is negative, so the solution crosses the positive $x$ axis downwards. That is a **clockwise** rotation.

#### Step 3. Global confirmation

With $\theta$ the polar angle, $\theta'=\dfrac{xy'-yx'}{x^2+y^2}$. Here

$$xy'-yx'=x(-10x+5y)-y(-7x+4y)=-10x^2+12xy-4y^2=-2(5x^2-6xy+2y^2).$$

The quadratic form $5x^2-6xy+2y^2$ has matrix $\begin{pmatrix}5&-3\\-3&2\end{pmatrix}$ with $5>0$ and determinant $10-9=1>0$: it is positive definite. So $\theta'<0$ at every point except the origin: the rotation is clockwise everywhere. In the canonical plane $J$ with $\omega=2>0$ rotates clockwise ($z_2'=-2z_1<0$ at $(1,0)$), and $\det P=1>0$ preserves orientation, which is consistent.

#### Step 4. Portrait in words

Trajectories are spirals that wind clockwise into the origin, one full turn every $T=2\pi/\omega=\pi$ time units. They are not circles: they are images under $P$ of logarithmic spirals of the $\mathbf z$ plane, so they are flattened along the directions fixed by $\mathbf u=(1,1)$ and $\mathbf w=(1,2)$.

## (d) Decay of the canonical radius, return to the axis, Euclidean distance [1.0 pts]

### Hint

$\mathbf z=P^{-1}\mathbf x$ obeys $\mathbf z'=J\mathbf z$. For $\frac{dV}{dt}$ use the chain rule $\frac{d}{dt}V(x(t),y(t))=V_xx'+V_yy'$.

### Checkpoint

- $V=\lvert P^{-1}\mathbf x\rvert^2=5x^2-6xy+2y^2$, $\frac{dV}{dt}=-2V$, $V(t)=V(0)e^{-2t}$; for the IVP $V(t)=5e^{-2t}$.
- $\sqrt V$ halves in $t_{1/2}=\ln2\approx0.693$.
- Back on the positive $x$ axis at $t=\pi$ (negative axis at $t=\pi/2$); $\mathbf x(\pi)=e^{-\pi}(1,0)^T$, ratio $e^{-\pi}\approx0.0432$.
- No: $\frac{d}{dt}\lvert\mathbf x\rvert^2=2(-7x^2-6xy+5y^2)$ is positive at $(0,1)$.

### Solution

#### Step 1. V is the canonical radius squared

$P^{-1}\mathbf x=\begin{pmatrix}2x-y\\-x+y\end{pmatrix}$, so $\lvert P^{-1}\mathbf x\rvert^2=(4x^2-4xy+y^2)+(x^2-2xy+y^2)=5x^2-6xy+2y^2=V$.

#### Step 2. Derivative along solutions

$V_x=10x-6y$, $V_y=-6x+4y$, $x'=-7x+4y$, $y'=-10x+5y$. By the chain rule

$$\begin{aligned}\frac{dV}{dt}&=(10x-6y)(-7x+4y)+(-6x+4y)(-10x+5y)\\&=(-70x^2+82xy-24y^2)+(60x^2-70xy+20y^2)=-10x^2+12xy-4y^2=-2V.\end{aligned}$$

(Equivalently $\frac{d}{dt}\lvert\mathbf z\rvert^2=2\mathbf z^TJ\mathbf z=2\rho\lvert\mathbf z\rvert^2$, because the skew part of $J$ gives $\mathbf z^T\begin{pmatrix}0&\omega\\-\omega&0\end{pmatrix}\mathbf z=0$.)

#### Step 3. Integration

For $V\neq0$ separate variables: $\displaystyle\int_{V(0)}^{V(t)}\frac{dV}{V}=\int_0^t(-2)\,d\tau$, so by Barrow's rule $[\ln V]_{V(0)}^{V(t)}=[-2\tau]_0^t$, i.e. $\ln V(t)-\ln V(0)=-2t$ and $V(t)=V(0)e^{-2t}$. For the IVP $V(0)=5\cdot1^2-0+0=5$, so $V(t)=5e^{-2t}$ and $\sqrt{V(t)}=\sqrt5\,e^{-t}$. Halving: $e^{-t_{1/2}}=\tfrac12$, so $t_{1/2}=\ln2\approx0.693$.

#### Step 4. Return to the positive x axis

$y(t)=-5e^{-t}\sin2t=0$ for $t=k\pi/2$. At $t=\pi/2$: $x=e^{-\pi/2}\cos\pi=-e^{-\pi/2}<0$ (negative axis). At $t=\pi$: $x=e^{-\pi}\cos2\pi=e^{-\pi}>0$. So the first return is $t=\pi$, with $\mathbf x(\pi)=e^{-\pi}(1,0)^T$ and ratio $\lvert\mathbf x(\pi)\rvert/\lvert\mathbf x(0)\rvert=e^{-\pi}\approx0.0432$. This holds for every solution: the trigonometric factors have period $T=\pi$, so $\mathbf x(t+\pi)=e^{-\pi}\mathbf x(t)$.

#### Step 5. The Euclidean distance

$\frac{d}{dt}\lvert\mathbf x\rvert^2=2\mathbf x^TA\mathbf x=2(-7x^2+4xy-10xy+5y^2)=2(-7x^2-6xy+5y^2)$. At $(0,1)$ it equals $10>0$: a solution through $(0,1)$ moves away from the origin at that instant. The Euclidean distance decays on average (by $e^{-\pi}$ per turn) but not monotonically; the quantity that decays monotonically, and exactly like $e^{-t}$, is $\sqrt V=\lvert P^{-1}\mathbf x\rvert$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $t\to+\infty$: $\mathbf x\to\mathbf 0$ like $e^{-t}$; $t\to-\infty$: the spirals grow without bound. If $\rho$ were $0$ the trajectories would be the closed ellipses $V=\text{const}$ (a centre); here they cut those ellipses inwards.
- **Checks:** $A\mathbf x_1=\mathbf x_1'$ for all $t$; $\operatorname{tr}A=2\rho$, $\det A=\rho^2+\omega^2$; $P^{-1}AP=J$; the IVP solution satisfies the system and $\mathbf x(0)=(1,0)^T$; Abel: $W(t)=e^{-2t}$.
- **Common mistakes in the exam:** (1) reading $\mathbf w$ with the wrong sign: the course writes the real part as $\cos\omega t\,\mathbf u-\sin\omega t\,\mathbf w$, so $\mathbf w=+(1,2)$; (2) deciding the sense of rotation from $\omega>0$ alone: it must be checked with a test vector (it is clockwise here, and it would flip if $\det P<0$); (3) claiming that the Euclidean distance halves after $\ln2$: only the canonical radius $\lvert P^{-1}\mathbf x\rvert$ does; (4) taking the return time to the same half-axis as $\pi/\omega$ instead of $2\pi/\omega$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
