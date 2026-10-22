---
materia: Advanced Maths
tema: "Unit 4: nonlinear planar systems, competing species"
bank_id: P08
title: "Two competing species with a competition parameter b: equilibria, Jacobians, the threshold b = 4/3 between coexistence and competitive exclusion"
category: midterm_2_problem
archetype: nonlinear-systems-stability
level: conceptual
unit: 4
difficulty: 3
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2020_G45_SOL and MATHS_SECONDPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p08.py"
tags:
  - problem-bank
  - midterm-2
  - competing-species
  - linearisation
  - nullclines
  - parameter-dependence
  - competitive-exclusion
---

# Bank P08 — Competing species with a competition parameter

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_SECONDPARTIAL_2020_G45_SOL and MATHS_SECONDPARTIAL_2025_G47_SOL. Method: Robinson Sec. 32.4 (stationary points, linearisation, Hartman-Grobman theorem, "join the dots"), Sec. 33.1 (competing species, weak competition and coexistence) and Ch. 31 (classification of linear systems). Every result was checked with SymPy (scripts/am_bank/p08.py).

## Statement

Two species share a habitat. Their populations $x(t)\ge0$, $y(t)\ge0$ (in thousands of individuals, time in years) obey

$$x'=x(6-2x-y),\qquad y'=y(4-y-bx),$$

where $b>0$ is a constant.

(a) Interpret each term of the model. Find all the equilibria as functions of $b$ and the values of $b$ for which there is an equilibrium with both species present ($x>0$, $y>0$).

(b) Compute the Jacobian matrix and classify every equilibrium in the closed first quadrant as $b$ varies. Identify the threshold value of $b$ that separates coexistence from competitive exclusion.

(c) Take $b=1$. Draw (describe) the nullclines, the eigen-directions at each equilibrium and the phase portrait in the first quadrant. What happens in the long run to a population with $x(0)>0$, $y(0)>0$?

(d) Take $b=2$. Answer the same questions. Which species survives?

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns $x(t)$, $y(t)$; independent variable $t\ge0$; the right-hand side is polynomial, hence $C^1$, so solutions exist and are unique (Picard). Autonomous, **nonlinear** (quadratic terms), planar.
- The axes are invariant: $x=0\Rightarrow x'=0$, $y=0\Rightarrow y'=0$. By uniqueness no orbit crosses them, so the closed first quadrant is invariant (populations stay non-negative).
- Parameter: $b>0$, the harm done to $y$ by each unit of $x$.

| Coefficient | Meaning |
| :--- | :--- |
| $6$, $4$ | intrinsic growth rates of $x$, $y$ (year$^{-1}$) |
| $-2x^2$, $-y^2$ | intraspecific competition; carrying capacities $K_x=3$, $K_y=4$ |
| $-xy$ in $x'$ | harm to $x$ from encounters with $y$ |
| $-bxy$ in $y'$ | harm to $y$ from encounters with $x$ |

#### Phase 2. Canonical formulation

$\mathbf x'=\mathbf F(\mathbf x)$ with $\mathbf F(x,y)=\big(x(6-2x-y),\ y(4-y-bx)\big)^T$. Near an equilibrium $\mathbf x_0$, $\mathbf u=\mathbf x-\mathbf x_0$ obeys $\mathbf u'\approx D\mathbf F(\mathbf x_0)\,\mathbf u$; when the equilibrium is hyperbolic (no eigenvalue with zero real part) the Hartman-Grobman theorem (Robinson Sec. 32.4.3) says the nonlinear portrait near it is the linear one.

## (a) Interpretation, equilibria and existence of coexistence [1.0 pts]

### Hint

Each equation vanishes on two lines; intersect one line of each.

### Checkpoint

- Equilibria: $(0,0)$, $(3,0)$, $(0,4)$ and, for $b\neq2$, $\left(\dfrac{2}{2-b},\ \dfrac{8-6b}{2-b}\right)$.
- The coexistence point lies in $x>0$, $y>0$ if and only if $0<b<\tfrac43$; at $b=\tfrac43$ it merges with $(3,0)$.

### Solution

#### Step 1. Interpretation

Each species grows logistically when alone ($y=0$: $x'=2x(3-x)$, capacity 3; $x=0$: $y'=y(4-y)$, capacity 4). The cross terms $-xy$ and $-bxy$ are both negative: each species reduces the growth of the other, so the model is one of **competition** (Robinson Sec. 33.1). The larger $b$, the stronger the pressure of $x$ on $y$.

#### Step 2. Equilibria

$x'=0$ when $x=0$ or $2x+y=6$; $y'=0$ when $y=0$ or $y+bx=4$. The four combinations:

- $x=0$, $y=0$: $(0,0)$.
- $x=0$, $y+bx=4$: $(0,4)$.
- $2x+y=6$, $y=0$: $(3,0)$.
- $2x+y=6$ and $bx+y=4$: subtracting, $(2-b)x=2$, so for $b\neq2$

$$x^*=\frac{2}{2-b},\qquad y^*=6-2x^*=\frac{6(2-b)-4}{2-b}=\frac{8-6b}{2-b}.$$

#### Step 3. Positivity

$x^*>0\iff b<2$. Then $2-b>0$ and $y^*>0\iff8-6b>0\iff b<\tfrac43$. So the coexistence point is in the open quadrant exactly for $0<b<\tfrac43$. At $b=\tfrac43$: $x^*=\frac{2}{2/3}=3$, $y^*=0$, it coincides with $(3,0)$. For $\tfrac43<b<2$ it lies in $y<0$ (no biological meaning); for $b=2$ the two lines are parallel and there is none.

## (b) Jacobian and classification as b varies [2.0 pts]

### Hint

At $(3,0)$ and $(0,4)$ the Jacobian is triangular. At the coexistence point use $6-2x^*-y^*=0$ and $4-y^*-bx^*=0$ to simplify the diagonal.

### Checkpoint

- $D\mathbf F=\begin{pmatrix}6-4x-y&-x\\-by&4-2y-bx\end{pmatrix}$.
- $(0,0)$: $\operatorname{diag}(6,4)$, unstable node for all $b$.
- $(0,4)$: $\begin{pmatrix}2&0\\-4b&-4\end{pmatrix}$, eigenvalues $2,-4$: saddle for all $b$.
- $(3,0)$: $\begin{pmatrix}-6&-3\\0&4-3b\end{pmatrix}$: saddle for $b<\tfrac43$, stable node for $b>\tfrac43$, non-hyperbolic at $b=\tfrac43$.
- Coexistence ($0<b<\tfrac43$): $\begin{pmatrix}-2x^*&-x^*\\-by^*&-y^*\end{pmatrix}$, $\operatorname{tr}=-6$, $\det=\dfrac{2(8-6b)}{2-b}>0$, discriminant $>0$: stable node.
- Threshold $b_c=\tfrac43$.

### Solution

#### Step 1. Jacobian

$\dfrac{\partial}{\partial x}\big[6x-2x^2-xy\big]=6-4x-y$, $\dfrac{\partial}{\partial y}\big[6x-2x^2-xy\big]=-x$, $\dfrac{\partial}{\partial x}\big[4y-y^2-bxy\big]=-by$, $\dfrac{\partial}{\partial y}\big[4y-y^2-bxy\big]=4-2y-bx$.

#### Step 2. Origin

$D\mathbf F(0,0)=\begin{pmatrix}6&0\\0&4\end{pmatrix}$: two positive eigenvalues, **unstable node**, eigenvectors along the axes. Orbits leave tangent to the slow direction, the $y$ axis ($4<6$).

#### Step 3. The point (0, 4)

$D\mathbf F(0,4)=\begin{pmatrix}6-4&0\\-4b&4-8\end{pmatrix}=\begin{pmatrix}2&0\\-4b&-4\end{pmatrix}$. Lower triangular: eigenvalues $2$ and $-4$, a **saddle** for every $b$. Eigenvector of $-4$: $(0,1)$, the $y$ axis is the stable manifold. Eigenvector of $2$: $(D\mathbf F-2I)\mathbf v=\mathbf 0$ gives row 2 $-4bv_1-6v_2=0$, so $\mathbf v=(3,-2b)^T$: the unstable manifold enters the quadrant towards the lower right. Meaning: a few individuals of $x$ introduced into the $y$-only state grow (their per capita rate there is $6-4=2>0$).

#### Step 4. The point (3, 0)

$D\mathbf F(3,0)=\begin{pmatrix}6-12&-3\\0&4-3b\end{pmatrix}=\begin{pmatrix}-6&-3\\0&4-3b\end{pmatrix}$. Upper triangular: eigenvalues $-6$ (along the $x$ axis) and $4-3b$, which is the per capita growth rate of a few $y$ individuals in the $x$-only state.

- $b<\tfrac43$: $4-3b>0$, **saddle** ($y$ can invade).
- $b>\tfrac43$: $4-3b<0$, **stable node** ($y$ cannot invade).
- $b=\tfrac43$: one zero eigenvalue, non-hyperbolic: the linearisation decides nothing there (Robinson Sec. 32.4.3). This is where the coexistence point crosses $(3,0)$.

#### Step 5. Coexistence point

At $(x^*,y^*)$: $6-4x^*-y^*=(6-2x^*-y^*)-2x^*=-2x^*$ and $4-2y^*-bx^*=(4-y^*-bx^*)-y^*=-y^*$, so

$$D\mathbf F(x^*,y^*)=\begin{pmatrix}-2x^*&-x^*\\-by^*&-y^*\end{pmatrix}.$$

- $\operatorname{tr}=-(2x^*+y^*)=-6$ (because $2x^*+y^*=6$ on the nullcline).
- $\det=2x^*y^*-bx^*y^*=(2-b)x^*y^*=(2-b)\dfrac{2}{2-b}\dfrac{8-6b}{2-b}=\dfrac{2(8-6b)}{2-b}$, positive for $0<b<\tfrac43$.
- Discriminant: $\operatorname{tr}^2-4\det=(-2x^*-y^*)^2-4(2x^*y^*-bx^*y^*)=(2x^*-y^*)^2+4bx^*y^*>0$.

Real eigenvalues, both negative ($\operatorname{tr}<0$, $\det>0$): **stable node** for every $0<b<\tfrac43$. (The off-diagonal entries have the same sign, which always forbids a focus in a competition model.)

#### Step 6. Summary and threshold

| $b$ | $(0,0)$ | $(0,4)$ | $(3,0)$ | coexistence |
| :--- | :--- | :--- | :--- | :--- |
| $0<b<\tfrac43$ | unstable node | saddle | saddle | stable node in the quadrant |
| $b=\tfrac43$ | unstable node | saddle | non-hyperbolic | merged with $(3,0)$ |
| $b>\tfrac43$ | unstable node | saddle | stable node | outside the quadrant or none |

The threshold is $b_c=\tfrac43$, the value at which $y$ stops being able to invade the $x$-only state: $4-3b_c=0$, i.e. $b_c=r_y/K_x$ (growth rate of $y$ over the carrying capacity of $x$).

## (c) Phase portrait and long-time behaviour for b = 1 [1.0 pts]

### Hint

Nullclines in the quadrant: $2x+y=6$ and $x+y=4$. Check the field on the two triangles between them.

### Checkpoint

- Coexistence point $(2,2)$; $D\mathbf F=\begin{pmatrix}-4&-2\\-2&-2\end{pmatrix}$, $\lambda=-3\pm\sqrt5\approx-0.764,\ -5.236$.
- Slow eigenvector $(2,\,-1-\sqrt5)$, fast eigenvector $(2,\,\sqrt5-1)$.
- Saddles: $(3,0)$ with unstable direction $(3,-7)$ (eigenvalue 1); $(0,4)$ with unstable direction $(3,-2)$ (eigenvalue 2).
- Every orbit with $x(0)>0$, $y(0)>0$ tends to $(2,2)$: **coexistence**.

### Solution

#### Step 1. Eigen-data at (2, 2)

$x^*=\frac{2}{1}=2$, $y^*=\frac{2}{1}=2$. $D\mathbf F=\begin{pmatrix}-4&-2\\-2&-2\end{pmatrix}$, $p(\lambda)=(-4-\lambda)(-2-\lambda)-4=\lambda^2+6\lambda+4$, $\lambda=-3\pm\sqrt5$. Row 1 of $(D\mathbf F-\lambda I)\mathbf v=\mathbf 0$: $(-4-\lambda)v_1-2v_2=0$, $v_2=-\tfrac{4+\lambda}{2}v_1$. For $\lambda_s=-3+\sqrt5$: $v_2=-\frac{1+\sqrt5}{2}v_1$, $\mathbf v_s=(2,-1-\sqrt5)$; for $\lambda_f=-3-\sqrt5$: $v_2=\frac{\sqrt5-1}{2}v_1$, $\mathbf v_f=(2,\sqrt5-1)$. Orbits reach $(2,2)$ tangent to $\mathbf v_s$ (slope $-\frac{1+\sqrt5}{2}\approx-1.62$), except the two on the fast line.

#### Step 2. Saddles

At $(3,0)$, $b=1$: $\begin{pmatrix}-6&-3\\0&1\end{pmatrix}$; for $\lambda=1$, row 1: $-7v_1-3v_2=0$, $\mathbf v=(3,-7)$. Its branch pointing into the quadrant, along $(-3,7)$, leaves $(3,0)$ upwards to the left and runs to $(2,2)$. At $(0,4)$: $\begin{pmatrix}2&0\\-4&-4\end{pmatrix}$, unstable direction $(3,-2)$: its branch in the quadrant leaves $(0,4)$ to the lower right and runs to $(2,2)$. The axes are the stable manifolds of the two saddles.

#### Step 3. Nullclines and regions

$L_x$: $2x+y=6$ (where $x'=0$, vertical arrows), from $(0,6)$ to $(3,0)$. $L_y$: $x+y=4$ (where $y'=0$, horizontal arrows), from $(0,4)$ to $(4,0)$. They cross at $(2,2)$.

- Above both lines: $x'<0$, $y'<0$ (towards the lower left).
- Below both lines: $x'>0$, $y'>0$ (towards the upper right).
- Between them for $x<2$ (e.g. $(1,3.5)$): $x'>0$, $y'<0$.
- Between them for $x>2$ (e.g. $(3,0.5)$): $x'<0$, $y'>0$.

#### Step 4. Trapping regions and the long run

Take the triangle $R=\{x+y>4,\ 2x+y<6,\ x<2\}$. On its side on $L_x$, $x'=0$ and $y'=y(4-x-y)=y(x-2)<0$ (there $y=6-2x$, so $4-x-y=x-2$): the field points down, into $R$. On its side on $L_y$, $y'=0$ and $x'=x(6-2x-y)=x(2-x)>0$: the field points right, into $R$. So $R$ is positively invariant; inside it $x$ increases and $y$ decreases, both bounded, so they converge, and the limit must be an equilibrium: $(2,2)$. The other triangle is treated the same way. An orbit starting above or below both lines moves monotonically (lower left or upper right) until it either enters one of the triangles or converges directly to $(2,2)$. Hence every orbit with $x(0)>0$, $y(0)>0$ tends to $(2,2)$: the two species **coexist** at 2000 individuals each.

## (d) Phase portrait and long-time behaviour for b = 2 [1.0 pts]

### Hint

The two non-trivial nullclines are now parallel.

### Checkpoint

- Equilibria $(0,0)$, $(3,0)$, $(0,4)$ only; nullclines $2x+y=6$ and $2x+y=4$, parallel.
- $(3,0)$: $\begin{pmatrix}-6&-3\\0&-2\end{pmatrix}$, stable node, slow eigenvector $(3,-4)$.
- $(0,4)$: $\begin{pmatrix}2&0\\-8&-4\end{pmatrix}$, saddle, unstable eigenvector $(3,-4)$.
- Every orbit with $x(0)>0$ tends to $(3,0)$: $y$ dies out, **competitive exclusion**.

### Solution

#### Step 1. Equilibria and linearisation

$2x+y=6$ and $2x+y=4$ never meet, so only $(0,0)$, $(3,0)$, $(0,4)$ remain. At $(3,0)$, $4-3b=-2$: eigenvalues $-6$ and $-2$, a **stable node**; for $\lambda=-2$, row 1 of $(D\mathbf F+2I)\mathbf v=\mathbf 0$ is $-4v_1-3v_2=0$, so $\mathbf v=(3,-4)$, the slow direction to which orbits are tangent on arrival. At $(0,4)$, $\begin{pmatrix}2&0\\-8&-4\end{pmatrix}$: a saddle, stable manifold the $y$ axis, unstable direction from row 2 $-8v_1-6v_2=0$, $\mathbf v=(3,-4)$.

#### Step 2. Regions

- $2x+y>6$: $x'<0$ and $y'<0$ (since also $2x+y>4$).
- $4<2x+y<6$: $x'>0$, $y'<0$ (e.g. $(1.5,2)$: $x'=1.5\cdot1>0$, $y'=2\cdot(-1)<0$).
- $2x+y<4$: $x'>0$, $y'>0$.

On $2x+y=6$ the field is vertical and points down, on $2x+y=4$ it is horizontal and points right: both point into the strip, which is positively invariant. In the strip $x$ increases and $y$ decreases, both bounded, so the orbit converges to an equilibrium in the closure of the strip with $x>0$: $(3,0)$. Orbits outside the strip move monotonically into it or straight to $(3,0)$.

#### Step 3. Long run

Every orbit with $x(0)>0$ (and any $y(0)\ge0$) tends to $(3,0)$: species $y$ becomes extinct and $x$ reaches its carrying capacity. Only the orbits on the $y$ axis ($x(0)=0$) go to $(0,4)$. The unstable branch of the saddle $(0,4)$ runs to $(3,0)$, leaving along $(3,-4)$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $b\to0^+$: $x^*\to1$, $y^*\to4$; $y$ no longer feels $x$, and $x$ settles at $6-2x-4=0$. $b\to\tfrac43^-$: $(x^*,y^*)\to(3,0)$ and $\det D\mathbf F\to0$, the exchange of stability with $(3,0)$ (a transcritical bifurcation, **extension**: a bifurcation where two equilibria cross and swap their stability). For every $b>\tfrac43$ the outcome is that of (d).
- **Checks:** $\mathbf F=\mathbf 0$ at each equilibrium; triangular Jacobians read directly; $\operatorname{tr}D\mathbf F(x^*,y^*)=-6$ for every $b$; at $b=1$, $\lambda_s+\lambda_f=-6$ and $\lambda_s\lambda_f=9-5=4=\det$. Units: each bracket has units of year$^{-1}$ when the coefficients carry year$^{-1}$ and (thousand individuals)$^{-1}$ year$^{-1}$.
- **Common mistakes in the exam:** (1) keeping the coexistence point for $\tfrac43<b<2$ although $y^*<0$; (2) using the full Jacobian formula at $(x^*,y^*)$ without the simplification $6-2x^*-y^*=0$, which hides that $\operatorname{tr}=-6$; (3) concluding stability at $b=\tfrac43$ from the linearisation (zero eigenvalue); (4) predicting the long-time outcome from local stability alone, without the nullcline and trapping-region argument.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
