---
materia: Advanced Maths
tema: "Unit 4: linear systems with a repeated eigenvalue and constant forcing"
bank_id: P07
title: "Non-homogeneous planar system with a defective matrix: Jordan form, equilibrium shift, IVP and the improper node"
category: midterm_1_problem
archetype: linear-systems-phase-portrait
level: standard
unit: 4
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the format of MATHS_FIRSTPARTIAL_2019_MT2 (problem 1: a planar system with the repeated eigenvalue -2; its matrix has the same trace and determinant as this one, and this item adds a constant forcing, the equilibrium shift and the Jordan-form solution) and of the systems problems of MATHS_FIRSTPARTIAL_2020_G46_SOL; not an official exercise. Verified with scripts/am_bank/p07.py"
tags:
  - problem-bank
  - midterm-1
  - repeated-eigenvalue
  - generalised-eigenvector
  - jordan-form
  - non-homogeneous-system
  - improper-node
---

# Bank P07 — Forced system with a repeated eigenvalue and an improper node

> [!info] Practice item, not an official exercise
> Written for the bank in the format of MATHS_FIRSTPARTIAL_2019_MT2 (problem 1: a planar system with the repeated eigenvalue -2; its matrix has the same trace and determinant as this one, and this item adds a constant forcing, the equilibrium shift and the Jordan-form solution) and of the systems problems of MATHS_FIRSTPARTIAL_2020_G46_SOL. Method: Robinson Ch. 30 (repeated eigenvalue, $\mathbf x=c_1e^{\lambda t}\mathbf v+c_2e^{\lambda t}(t\mathbf v+\mathbf w)$), Ch. 31 (Jordan form and classification), undetermined coefficients for constant forcing, and [[Concept - Planar Systems with a Repeated Eigenvalue]]. Every result was checked with SymPy (scripts/am_bank/p07.py).

## Statement

Consider the system

$$x'=-x+y,\qquad y'=-x-3y+4.$$

(a) Write it as $\mathbf x'=A\mathbf x+\mathbf f$. Show that $A$ has a repeated eigenvalue with only one independent eigenvector $\mathbf v$. Find a generalised eigenvector $\mathbf w$ with $(A-\lambda I)\mathbf w=\mathbf v$, build $P=[\mathbf v\mid\mathbf w]$, compute $P^{-1}$ and check that $P^{-1}AP$ is the Jordan form.

(b) Find a particular solution by undetermined coefficients (a constant vector) and the general solution.

(c) Solve the initial value problem $x(0)=3$, $y(0)=0$ and check your answer.

(d) Classify the equilibrium and describe the phase portrait: invariant line, direction of tangency as $t\to\pm\infty$, sense of turning (test vector), nullclines, and the behaviour of the orbit of (c).

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns $x(t)$, $y(t)$, $t\in\mathbb R$. First-order, linear, constant coefficients, **non-homogeneous** with a constant forcing; solutions exist for all $t$ and are unique given $\mathbf x(0)$.
- Structure of the general solution (superposition): $\mathbf x=\mathbf x_p+\mathbf x_h$, with $\mathbf x_h$ the general solution of $\mathbf x'=A\mathbf x$.
- Since $\mathbf f$ is constant and $0$ will not be an eigenvalue ($\det A\neq0$), a constant $\mathbf x_p$ exists: it is the equilibrium, and $\mathbf u=\mathbf x-\mathbf x_p$ obeys the homogeneous system.

#### Phase 2. Canonical formulation

$$\mathbf x'=A\mathbf x+\mathbf f,\qquad A=\begin{pmatrix}-1&1\\-1&-3\end{pmatrix},\qquad \mathbf f=\begin{pmatrix}0\\4\end{pmatrix}.$$

Target frame: $\mathbf u=P\mathbf z$ with $P=[\mathbf v\mid\mathbf w]$, which turns $\mathbf u'=A\mathbf u$ into $\mathbf z'=J\mathbf z$, $J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$.

## (a) Repeated eigenvalue, generalised eigenvector and Jordan form [1.5 pts]

### Hint

Expand $\det(A-\lambda I)$; the matrix $N=A-\lambda I$ has rank 1. Solve $N\mathbf w=\mathbf v$ row by row.

### Checkpoint

- $p(\lambda)=\lambda^2+4\lambda+4=(\lambda+2)^2$, $\lambda=-2$ (double); $N=A+2I=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$, rank 1, $N^2=0$.
- $\mathbf v=(1,-1)^T$, $\mathbf w=(1,0)^T$.
- $P=\begin{pmatrix}1&1\\-1&0\end{pmatrix}$, $\det P=1$, $P^{-1}=\begin{pmatrix}0&-1\\1&1\end{pmatrix}$, $P^{-1}AP=\begin{pmatrix}-2&1\\0&-2\end{pmatrix}$.

### Solution

#### Step 1. Characteristic polynomial

$$\det(A-\lambda I)=(-1-\lambda)(-3-\lambda)-(1)(-1)=\lambda^2+4\lambda+3+1=\lambda^2+4\lambda+4=(\lambda+2)^2$$

so $\lambda=-2$ is a double root ($\operatorname{tr}A=-4=2\lambda$, $\det A=4=\lambda^2$).

#### Step 2. Eigenvectors

$N=A+2I=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$. Row 1: $v_1+v_2=0$; row 2: $-v_1-v_2=0$, the same equation. The rank of $N$ is 1, so the eigenspace is one-dimensional, spanned by $\mathbf v=(1,-1)^T$: $A$ is not diagonalisable. Also $N^2=\begin{pmatrix}1-1&1-1\\-1+1&-1+1\end{pmatrix}=0$, as the Cayley-Hamilton theorem predicts.

#### Step 3. Generalised eigenvector

$N\mathbf w=\mathbf v$: row 1 $w_1+w_2=1$, row 2 $-w_1-w_2=-1$ (the same). Any solution works; take $w_2=0$, $w_1=1$: $\mathbf w=(1,0)^T$. It is not a multiple of $\mathbf v$, as required.

#### Step 4. Change of basis and Jordan form

$P=[\mathbf v\mid\mathbf w]=\begin{pmatrix}1&1\\-1&0\end{pmatrix}$, $\det P=1\cdot0-1\cdot(-1)=1$, $P^{-1}=\frac11\begin{pmatrix}0&-1\\1&1\end{pmatrix}$.

$A\mathbf v=-2\mathbf v=(-2,2)^T$ and $A\mathbf w=(-1,-1)^T=\mathbf v-2\mathbf w$, so $AP=\begin{pmatrix}-2&-1\\2&-1\end{pmatrix}$. Then

$$\begin{aligned}(P^{-1}AP)_{11}&=0(-2)+(-1)(2)=-2, & (P^{-1}AP)_{12}&=0(-1)+(-1)(-1)=1,\\ (P^{-1}AP)_{21}&=1(-2)+1(2)=0, & (P^{-1}AP)_{22}&=1(-1)+1(-1)=-2.\end{aligned}$$

$$P^{-1}AP=\begin{pmatrix}-2&1\\0&-2\end{pmatrix}=J.$$

## (b) Particular solution and general solution [1.5 pts]

### Hint

Try $\mathbf x_p=\mathbf c$ constant: then $\mathbf 0=A\mathbf c+\mathbf f$. Solve $\mathbf z'=J\mathbf z$ from the bottom row up.

### Checkpoint

- $\mathbf x_p=\mathbf x^*=(1,1)^T$.
- $\mathbf x(t)=\begin{pmatrix}1\\1\end{pmatrix}+c_1e^{-2t}\begin{pmatrix}1\\-1\end{pmatrix}+c_2e^{-2t}\left[t\begin{pmatrix}1\\-1\end{pmatrix}+\begin{pmatrix}1\\0\end{pmatrix}\right]$.
- In components: $x=1+(c_1+c_2+c_2t)e^{-2t}$, $y=1-(c_1+c_2t)e^{-2t}$.

### Solution

#### Step 1. Undetermined constant vector

With $\mathbf x_p=(p,q)^T$ constant, $\mathbf x_p'=\mathbf 0$ and the system gives $A\mathbf x_p=-\mathbf f$:

$$-p+q=0,\qquad -p-3q+4=0.$$

The first gives $q=p$; substituting, $-4p+4=0$, so $p=q=1$. The solution is unique because $\det A=4\neq0$. So $\mathbf x^*=(1,1)^T$ is the only equilibrium.

#### Step 2. Homogeneous part in the Jordan frame

Let $\mathbf u=\mathbf x-\mathbf x^*$; then $\mathbf u'=\mathbf x'=A\mathbf x+\mathbf f=A\mathbf u+(A\mathbf x^*+\mathbf f)=A\mathbf u$. With $\mathbf u=P\mathbf z$ ($P$ constant): $\mathbf z'=P^{-1}AP\,\mathbf z=J\mathbf z$, i.e.

$$z_1'=-2z_1+z_2,\qquad z_2'=-2z_2.$$

The second equation gives $z_2=c_2e^{-2t}$. The first becomes $z_1'+2z_1=c_2e^{-2t}$; multiply by the integrating factor $e^{2t}$: $(e^{2t}z_1)'=e^{2t}z_1'+2e^{2t}z_1=c_2$ (product rule). Integrating, $e^{2t}z_1=c_1+c_2t$, so $z_1=(c_1+c_2t)e^{-2t}$.

#### Step 3. Back to the original frame

$\mathbf u=P\mathbf z=z_1\mathbf v+z_2\mathbf w=c_1e^{-2t}\mathbf v+c_2e^{-2t}(t\mathbf v+\mathbf w)$, the formula of Robinson Ch. 30. Adding $\mathbf x^*$:

$$\mathbf x(t)=\begin{pmatrix}1+(c_1+c_2+c_2t)e^{-2t}\\ 1-(c_1+c_2t)e^{-2t}\end{pmatrix}.$$

The fundamental matrix $\Phi=\big[e^{-2t}\mathbf v\mid e^{-2t}(t\mathbf v+\mathbf w)\big]$ has $\det\Phi=e^{-4t}\det[\mathbf v\mid t\mathbf v+\mathbf w]=e^{-4t}\det[\mathbf v\mid\mathbf w]=e^{-4t}\neq0$, in agreement with Abel's formula for systems (**extension**) $W(t)=W(0)e^{(\operatorname{tr}A)t}$.

## (c) Initial value problem x(0) = 3, y(0) = 0 [1.0 pts]

### Hint

Impose $t=0$ in the components of (b); then substitute back into both equations.

### Checkpoint

- $c_1=1$, $c_2=1$.
- $x(t)=1+(2+t)e^{-2t}$, $y(t)=1-(1+t)e^{-2t}$.
- $x'=-(3+2t)e^{-2t}$, $y'=(1+2t)e^{-2t}$.

### Solution

#### Step 1. Constants

$x(0)=1+c_1+c_2=3$ and $y(0)=1-c_1=0$. Hence $c_1=1$ and $c_2=2-c_1=1$:

$$x(t)=1+(2+t)e^{-2t},\qquad y(t)=1-(1+t)e^{-2t}.$$

#### Step 2. Check

By the product rule, $x'=e^{-2t}-2(2+t)e^{-2t}=-(3+2t)e^{-2t}$ and $y'=-e^{-2t}+2(1+t)e^{-2t}=(1+2t)e^{-2t}$. Right-hand sides:

$$-x+y=-1-(2+t)e^{-2t}+1-(1+t)e^{-2t}=-(3+2t)e^{-2t},$$

$$-x-3y+4=-1-(2+t)e^{-2t}-3+3(1+t)e^{-2t}+4=(1+2t)e^{-2t}.$$

Both equations hold, and $x(0)=3$, $y(0)=0$.

## (d) Classification and phase portrait [1.0 pts]

### Hint

Work with $\mathbf u=\mathbf x-\mathbf x^*$. For the sense of turning compute $u_1u_2'-u_2u_1'$, or $A\mathbf w$ at the point $\mathbf x^*+\mathbf w$.

### Checkpoint

- $(1,1)$ is a **stable improper node**: $\operatorname{tr}A=-4<0$, $\det A=4>0$, $(\operatorname{tr}A)^2-4\det A=0$, one eigen-direction.
- Invariant line $x+y=2$ (through $(1,1)$ along $\mathbf v=(1,-1)$); all other orbits are tangent to it at $(1,1)$ and parallel to it as $t\to-\infty$.
- $u_1u_2'-u_2u_1'=-(u_1+u_2)^2\le0$: orbits turn **clockwise**; test vector $A\mathbf w=(-1,-1)^T$ at $(2,1)$.
- Nullclines: $x'=0$ on $y=x$; $y'=0$ on $x+3y=4$. The orbit of (c) stays in $x+y>2$; for $t\ge0$ $x$ decreases to 1 and $y$ increases to 1.

### Solution

#### Step 1. Type

A double negative eigenvalue with a one-dimensional eigenspace gives a stable improper node (Robinson Ch. 31): it lies on the parabola $(\operatorname{tr})^2=4\det$ of the trace-determinant plane, at the border between the nodes and the foci.

#### Step 2. Eigen-direction and tangency

The line $\mathbf x^*+s\mathbf v$, i.e. $x+y=2$, is invariant ($c_2=0$: $\mathbf u=c_1e^{-2t}\mathbf v$ moves straight to $(1,1)$). For $c_2\neq0$, $\mathbf u=e^{-2t}\big[(c_1+c_2t)\mathbf v+c_2\mathbf w\big]$ and the term $c_2t\mathbf v$ dominates as $t\to\pm\infty$: the direction of $\mathbf u$ tends to $\pm\mathbf v$ at both ends. So every orbit enters $(1,1)$ tangent to the line $x+y=2$, and far away (as $t\to-\infty$) it is again parallel to that line, on the other side: each orbit turns half a revolution.

#### Step 3. Sense of turning

With $\mathbf u'=A\mathbf u$: $u_1'=-u_1+u_2$, $u_2'=-u_1-3u_2$, so

$$u_1u_2'-u_2u_1'=u_1(-u_1-3u_2)-u_2(-u_1+u_2)=-u_1^2-2u_1u_2-u_2^2=-(u_1+u_2)^2\le0,$$

zero only on the invariant line. The polar angle around $(1,1)$ never increases: orbits turn **clockwise**. Test vector: at $(2,1)$, $\mathbf u=\mathbf w=(1,0)$, and $\mathbf u'=A\mathbf w=(-1,-1)^T$ points down, crossing the horizontal through $(1,1)$ downwards on its right: clockwise.

#### Step 4. Nullclines

$x'=0$ on the line $y=x$ (vertical slopes there); $y'=0$ on $x+3y=4$ (horizontal slopes). Both pass through $(1,1)$ and split the plane into four sectors where $(x',y')$ keeps its signs; e.g. at $(3,0)$: $x'=-3<0$, $y'=1>0$.

#### Step 5. The orbit of (c)

$u_1+u_2=(2+t)e^{-2t}-(1+t)e^{-2t}=e^{-2t}>0$: the orbit never meets the invariant line and stays in the half-plane $x+y>2$ (uniqueness forbids crossing an invariant line). For $t\ge0$, $x'=-(3+2t)e^{-2t}<0$ and $y'=(1+2t)e^{-2t}>0$: it moves monotonically from $(3,0)$ to $(1,1)$, with $u_2/u_1=-(1+t)/(2+t)\to-1$, i.e. arriving from the lower right tangent to $x+y=2$. Backwards in time it crosses $y=1$ at $t=-1$ and $x=1$ at $t=-2$, and escapes to infinity parallel to $(-1,1)$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $t\to+\infty$: $\mathbf x\to(1,1)$ like $te^{-2t}$, slower than a pure $e^{-2t}$ because of the secular factor $t$. $t\to-\infty$: $\lvert\mathbf x\rvert\to\infty$. If $\mathbf f=\mathbf 0$ the portrait is the same, centred at the origin.
- **Checks:** $P^{-1}AP=J$ with $\det P=1$; $A\mathbf x^*+\mathbf f=\mathbf 0$; the IVP solution satisfies both equations and the initial data; $\det\Phi=e^{-4t}$ matches Abel's formula for systems (extension).
- **Common mistakes in the exam:** (1) writing $\mathbf x_h=c_1e^{-2t}\mathbf v+c_2te^{-2t}\mathbf v$, which forgets $\mathbf w$ and is not a fundamental set; (2) solving $(A-\lambda I)\mathbf w=\mathbf v$ with the wrong sign of $\lambda$ (using $A-2I$); (3) trying a particular solution $\mathbf c\,t$ or $\mathbf c\,e^{-2t}$ for a constant forcing: a constant vector suffices since $\det A\neq0$; (4) drawing a star node (all straight lines), or claiming orbits cross the eigenline.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
