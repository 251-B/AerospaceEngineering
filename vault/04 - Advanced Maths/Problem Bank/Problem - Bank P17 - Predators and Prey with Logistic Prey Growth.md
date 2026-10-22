---
materia: Advanced Maths
tema: "Unit 4: nonlinear systems, linearisation and stability"
bank_id: P17
title: "Predators and prey with logistic prey growth: equilibria, Jacobians, the focus-node threshold of the coexistence point and the long-time outcome"
category: final_problem
archetype: nonlinear-systems-stability
level: standard
unit: 4
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2013_EXTRA, MATHS_FINALEXAM_2016_ORD_A and MATHS_FINALEXAM_2022_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p17.py"
tags:
  - problem-bank
  - final-exam
  - predator-prey
  - linearisation
  - jacobian
  - stable-focus
  - stable-node
---

# Bank P17 — Predators and prey with logistic prey growth

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2013_EXTRA, MATHS_FINALEXAM_2016_ORD_A and MATHS_FINALEXAM_2022_ORD_SOL. Method: Robinson Ch. 32 (Sec. 32.4, stationary points, linearisation, Hartman-Grobman theorem, stability type, joining the dots) and Ch. 33 (Sec. 33.2-33.3, predator-prey models); classification of linear systems from Robinson Ch. 28-31 and Notes, p. 9-10. Every result was checked with SymPy (scripts/am_bank/p17.py).

## Statement

After scaling, the densities $x(t)\ge 0$ of a prey and $y(t)\ge 0$ of its predator obey

$$
\dot x=x(1-x)-xy,\qquad \dot y=y\,(x-a),
$$

where the parameter $a$, with $0<a<1$, is the death rate of the predator measured against its rate of conversion of prey. Without predators the prey grows logistically with carrying capacity $1$.

(a) Find all the equilibria in the closed first quadrant and the Jacobian matrix of the system. Classify the two equilibria that lie on the axes and give their eigen-directions.

(b) Show that the coexistence equilibrium is asymptotically stable for every $a\in(0,1)$, and find the value $a^*$ that separates a stable focus from a stable node. Describe the phase portrait near this point for $a=\tfrac12$ (eigenvalues, sense of rotation) and for $a=\tfrac{9}{11}$ (eigenvalues, eigenvectors, the change of basis $P$ with $P^{-1}JP$, and the slow direction).

(c) Describe the global phase portrait in the open quadrant (nullclines and the direction of the flow) and state the ecological long-time outcome. Hint for the global part: study $V(x,y)=x-a-a\ln\dfrac{x}{a}+y-b-b\ln\dfrac{y}{b}$ with $b=1-a$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns $x(t)$, $y(t)$, independent variable $t\ge 0$; state space the closed quadrant $x\ge0$, $y\ge0$ (densities).
- Autonomous, nonlinear (quadratic) planar system $\dot{\mathbf x}=\mathbf f(\mathbf x)$ with $\mathbf f$ polynomial, hence $\mathbf f$ and $D\mathbf f$ are continuous: the existence and uniqueness theorem for systems (Robinson Thm 25.2) gives one solution through each point, and orbits cannot cross.
- The axes are invariant: if $x=0$ then $\dot x=0$; if $y=0$ then $\dot y=0$. Hence the open quadrant is invariant and densities never become negative.

| Symbol | Meaning | Range |
| :--- | :--- | :--- |
| $x$ | prey density (scaled by the carrying capacity) | $x\ge0$ |
| $y$ | predator density (scaled) | $y\ge0$ |
| $a$ | predator death rate / conversion rate | $0<a<1$ |
| $b=1-a$ | predator density at coexistence | $0<b<1$ |

#### Phase 2. Canonical formulation

$$
\dot{\mathbf x}=\mathbf f(\mathbf x),\qquad \mathbf f(x,y)=\begin{pmatrix}x-x^2-xy\\ xy-ay\end{pmatrix}.
$$

Near an equilibrium $\mathbf x^*$, with $\boldsymbol\xi=\mathbf x-\mathbf x^*$, the linearised system is $\dot{\boldsymbol\xi}=J(\mathbf x^*)\,\boldsymbol\xi$ (Robinson Sec. 32.4.2). When no eigenvalue of $J(\mathbf x^*)$ has zero real part, the Hartman-Grobman theorem (Robinson Sec. 32.4.3) says the nonlinear portrait near $\mathbf x^*$ is the linear one, slightly deformed.

## (a) Equilibria, Jacobian and the boundary equilibria [0.8 pts]

### Hint

Factor each component: $\dot x=x(1-x-y)$, $\dot y=y(x-a)$. Each factor gives a nullcline.

### Checkpoint

- Equilibria: $O=(0,0)$, $E_1=(1,0)$, $E^*=(a,\,1-a)$.
- $J(x,y)=\begin{pmatrix}1-2x-y&-x\\ y&x-a\end{pmatrix}$.
- $O$: eigenvalues $1$ (along $(1,0)$) and $-a$ (along $(0,1)$), saddle.
- $E_1$: eigenvalues $-1$ (along $(1,0)$) and $1-a>0$ (along $(1,a-2)$), saddle.

### Solution

#### Step 1. Equilibria

$\dot x=0\iff x=0$ or $y=1-x$; $\dot y=0\iff y=0$ or $x=a$. Combine one condition from each equation:

- $x=0$ and $y=0$: $O=(0,0)$.
- $x=0$ and $x=a$: impossible, since $a>0$.
- $y=1-x$ and $y=0$: $x=1$, so $E_1=(1,0)$.
- $y=1-x$ and $x=a$: $E^*=(a,1-a)$, inside the open quadrant because $0<a<1$.

#### Step 2. Jacobian

Differentiate each component with respect to each variable:

$$
\frac{\partial}{\partial x}(x-x^2-xy)=1-2x-y,\quad \frac{\partial}{\partial y}(x-x^2-xy)=-x,\quad \frac{\partial}{\partial x}(xy-ay)=y,\quad \frac{\partial}{\partial y}(xy-ay)=x-a,
$$

$$
J(x,y)=\begin{pmatrix}1-2x-y&-x\\ y&x-a\end{pmatrix}.
$$

#### Step 3. The origin

$$
J(0,0)=\begin{pmatrix}1&0\\0&-a\end{pmatrix}.
$$

The matrix is diagonal, so the eigenvalues are $\lambda_1=1$ with $\mathbf v_1=(1,0)$ and $\lambda_2=-a<0$ with $\mathbf v_2=(0,1)$ (Robinson Example 27.2). Opposite signs: a **saddle** (Robinson Sec. 28.3), hyperbolic, so the nonlinear point is a saddle too. The $x$-axis is its unstable direction (prey alone grow), the $y$-axis its stable direction (predators alone die out as $y=y_0e^{-at}$, which is exact because the $y$-axis is invariant).

#### Step 4. The prey-only equilibrium

$$
J(1,0)=\begin{pmatrix}1-2-0&-1\\0&1-a\end{pmatrix}=\begin{pmatrix}-1&-1\\0&1-a\end{pmatrix}.
$$

It is upper triangular, so its eigenvalues are the diagonal entries (Robinson Example 27.3): $\lambda_1=-1$ and $\lambda_2=1-a>0$. Eigenvectors from $(J-\lambda I)\mathbf v=\mathbf 0$:

- $\lambda_1=-1$: $\begin{pmatrix}0&-1\\0&2-a\end{pmatrix}\mathbf v=\mathbf 0$. Row 1 gives $-v_2=0$, so $\mathbf v_1=(1,0)$.
- $\lambda_2=1-a$: $\begin{pmatrix}-(2-a)&-1\\0&0\end{pmatrix}\mathbf v=\mathbf 0$. Row 1 gives $-(2-a)v_1-v_2=0$, so $v_2=(a-2)v_1$ and $\mathbf v_2=(1,a-2)$.

Opposite signs: $E_1$ is a **saddle**. Its unstable direction $\pm(1,a-2)$ enters the open quadrant along $(-1,\,2-a)$, up and to the left: a small number of predators introduced into a prey population at capacity grows.

## (b) Stability of the coexistence point and the focus-node threshold [1.0 pts]

### Hint

Write $J(E^*)$, then $\operatorname{tr}J$, $\det J$ and the discriminant $(\operatorname{tr}J)^2-4\det J$ as functions of $a$. In the trace-determinant plane the boundary between foci and nodes is the parabola $\operatorname{tr}^2=4\det$.

### Checkpoint

- $J(E^*)=\begin{pmatrix}-a&-a\\1-a&0\end{pmatrix}$, $\operatorname{tr}=-a<0$, $\det=a(1-a)>0$: asymptotically stable for all $a\in(0,1)$.
- Discriminant $a(5a-4)$: stable focus for $0<a<\tfrac45$, stable degenerate node at $a^*=\tfrac45$, stable node for $\tfrac45<a<1$.
- $a=\tfrac12$: $\lambda=-\tfrac14\pm\tfrac{\sqrt3}{4}i$, counter-clockwise spiral.
- $a=\tfrac9{11}$: $\lambda_1=-\tfrac3{11}$, $\mathbf v_1=(3,-2)$ (slow), $\lambda_2=-\tfrac6{11}$, $\mathbf v_2=(3,-1)$ (fast); $P^{-1}JP=\operatorname{diag}(-\tfrac3{11},-\tfrac6{11})$.

### Solution

#### Step 1. Jacobian at the coexistence point

Substitute $x=a$, $y=1-a$ in $J$: $1-2a-(1-a)=-a$, $-x=-a$, $y=1-a$, $x-a=0$:

$$
J^*=J(a,1-a)=\begin{pmatrix}-a&-a\\1-a&0\end{pmatrix}.
$$

#### Step 2. Characteristic polynomial

$$
\det(J^*-\lambda I)=\begin{vmatrix}-a-\lambda&-a\\1-a&-\lambda\end{vmatrix}=(-a-\lambda)(-\lambda)-(-a)(1-a)=\lambda^2+a\lambda+a(1-a).
$$

So $\operatorname{tr}J^*=-a$, $\det J^*=a(1-a)$ and

$$
\lambda=\frac{-a\pm\sqrt{a^2-4a(1-a)}}{2}=\frac{-a\pm\sqrt{a(5a-4)}}{2}.
$$

#### Step 3. Stability for every $a\in(0,1)$

$\det J^*=a(1-a)>0$ excludes a saddle, and $\operatorname{tr}J^*=-a<0$ gives both eigenvalues negative real part: if they are real, their product is positive and their sum negative, so both are negative; if they are complex, the real part is $-a/2<0$. Every eigenvalue has nonzero real part, so the point is hyperbolic and by Hartman-Grobman (Robinson Sec. 32.4.3) $E^*$ is **asymptotically stable** in the nonlinear system.

#### Step 4. The threshold

The type depends on the sign of $\Delta(a)=a(5a-4)$ (Robinson Ch. 31, summary of phase portraits):

- $0<a<\tfrac45$: $\Delta<0$, complex pair with real part $-a/2$: **stable focus** (spiral).
- $a=\tfrac45$: $\Delta=0$, double eigenvalue $\lambda=-\tfrac25$; $J^*-\lambda I=\begin{pmatrix}-\frac25&-\frac45\\ \frac15&\frac25\end{pmatrix}\neq0$, so there is a single eigen-direction, $\mathbf v=(2,-1)$ from row 1: **stable degenerate (improper) node** (Robinson Ch. 30). The eigenvalue is still negative, so the point stays hyperbolic and asymptotically stable; only the fine shape (node or slow spiral) may be changed by the nonlinear terms in this borderline case.
- $\tfrac45<a<1$: $\Delta>0$, two distinct negative eigenvalues: **stable node**.

So $a^*=\tfrac45$: predators that die fast (large $a$) let the system settle without oscillating.

#### Step 5. Focus case $a=\tfrac12$

$\lambda^2+\tfrac12\lambda+\tfrac14=0$, so $\lambda=\dfrac{-\frac12\pm\sqrt{\frac14-1}}{2}=-\dfrac14\pm\dfrac{\sqrt3}{4}i$. Real part $-\tfrac14$ (decay rate), imaginary part $\tfrac{\sqrt3}4$ (angular frequency; period of the linear oscillation $2\pi/(\sqrt3/4)=8\pi/\sqrt3$).

Sense of rotation from a test vector (Robinson Ch. 29): at $\boldsymbol\xi=(1,0)$ (more prey than at equilibrium), $\dot{\boldsymbol\xi}=J^*\boldsymbol\xi=(-\tfrac12,\ \tfrac12)$. The second component is positive: the orbit turns from the positive $\xi_1$ axis towards the positive $\xi_2$ axis, i.e. **counter-clockwise** in the $(x,y)$ plane. Ecologically: an excess of prey makes the predators grow, the predators then eat the prey down, and so on, with oscillations of decreasing amplitude.

#### Step 6. Node case $a=\tfrac9{11}$

$$
J^*=\begin{pmatrix}-\frac9{11}&-\frac9{11}\\ \frac2{11}&0\end{pmatrix},\qquad \lambda^2+\frac9{11}\lambda+\frac9{11}\cdot\frac2{11}=0,\qquad \lambda=\frac{-\frac9{11}\pm\sqrt{\frac{81}{121}-\frac{72}{121}}}{2}=\frac{-\frac9{11}\pm\frac3{11}}{2}.
$$

So $\lambda_1=-\tfrac3{11}$ and $\lambda_2=-\tfrac6{11}$ (check: sum $-\tfrac9{11}=\operatorname{tr}$, product $\tfrac{18}{121}=\det$). Eigenvectors from the first row of $(J^*-\lambda I)\mathbf v=\mathbf 0$ (the second row is proportional because $\det(J^*-\lambda I)=0$):

- $\lambda_1=-\tfrac3{11}$: $\left(-\tfrac9{11}+\tfrac3{11}\right)v_1-\tfrac9{11}v_2=0\Rightarrow -6v_1-9v_2=0\Rightarrow \mathbf v_1=(3,-2)$. Second row check: $\tfrac2{11}\cdot3+\tfrac3{11}\cdot(-2)=0$.
- $\lambda_2=-\tfrac6{11}$: $\left(-\tfrac9{11}+\tfrac6{11}\right)v_1-\tfrac9{11}v_2=0\Rightarrow -3v_1-9v_2=0\Rightarrow \mathbf v_2=(3,-1)$. Second row check: $\tfrac2{11}\cdot3+\tfrac6{11}\cdot(-1)=0$.

Change of basis (Robinson Sec. 28.2): $P=[\mathbf v_1\mid\mathbf v_2]=\begin{pmatrix}3&3\\-2&-1\end{pmatrix}$, $\det P=3(-1)-3(-2)=3$, and

$$
P^{-1}=\frac13\begin{pmatrix}-1&-3\\2&3\end{pmatrix}.
$$

$J^*P=[\lambda_1\mathbf v_1\mid\lambda_2\mathbf v_2]=\begin{pmatrix}-\frac9{11}&-\frac{18}{11}\\ \frac6{11}&\frac6{11}\end{pmatrix}$, and entry by entry

$$
\begin{aligned}
(P^{-1}J^*P)_{11}&=\tfrac13\left[(-1)(-\tfrac9{11})+(-3)\tfrac6{11}\right]=\tfrac13\cdot\left(-\tfrac9{11}\right)=-\tfrac3{11},\\
(P^{-1}J^*P)_{12}&=\tfrac13\left[(-1)(-\tfrac{18}{11})+(-3)\tfrac6{11}\right]=0,\\
(P^{-1}J^*P)_{21}&=\tfrac13\left[2(-\tfrac9{11})+3\cdot\tfrac6{11}\right]=0,\\
(P^{-1}J^*P)_{22}&=\tfrac13\left[2(-\tfrac{18}{11})+3\cdot\tfrac6{11}\right]=-\tfrac6{11}.
\end{aligned}
$$

So $P^{-1}J^*P=\operatorname{diag}(-\tfrac3{11},-\tfrac6{11})$. In $\mathbf z=P^{-1}\boldsymbol\xi$ coordinates $z_1=c_1e^{-3t/11}$, $z_2=c_2e^{-6t/11}$, and eliminating $t$, $z_2=K z_1^2$: parabola-like orbits. All orbits enter $E^*$ tangent to the **slow** eigenvector $\mathbf v_1=(3,-2)$ (smaller $\lvert\lambda\rvert$), and far from $E^*$ they run parallel to the fast one $\mathbf v_2=(3,-1)$ (Robinson Sec. 28.3-28.4).

## (c) Global portrait and long-time outcome [0.7 pts]

### Hint

Compute $\dot V=V_x\dot x+V_y\dot y$ by the chain rule and simplify. Then use the nullclines to see that orbits cannot stay on the line $x=a$ away from $E^*$.

### Checkpoint

- Nullclines: $\dot x=0$ on $x=0$ and on $x+y=1$; $\dot y=0$ on $y=0$ and on $x=a$.
- $\dot V=-(x-a)^2\le0$ (extension: Lyapunov function).
- Every orbit with $x(0)>0$, $y(0)>0$ tends to $E^*=(a,1-a)$: prey and predators coexist; with $a=\tfrac12$ through damped oscillations, with $a=\tfrac9{11}$ without them.

### Solution

#### Step 1. Nullclines and direction field

In the open quadrant, $\dot x>0$ below the line $x+y=1$ and $\dot x<0$ above it; $\dot y>0$ to the right of $x=a$ and $\dot y<0$ to the left. The two lines cross at $E^*$ and cut the quadrant into four regions; the flow goes right-and-up (below the line, right of $x=a$), left-and-up (above, right), left-and-down (above, left) and right-and-down (below, left). Going round these four regions in that order is a counter-clockwise turn about $E^*$, consistent with (b). The axes are invariant: on the $x$ axis orbits run to $E_1$, on the $y$ axis to $O$.

#### Step 2. The function $V$ (extension)

A **Lyapunov function** (extension: not in the course; a $C^1$ function with a strict minimum at the equilibrium that does not increase along orbits) proves global statements that linearisation cannot. Here $V$ is defined in the open quadrant. Its derivatives are

$$
V_x=1-\frac{a}{x}=\frac{x-a}{x},\qquad V_y=1-\frac{b}{y}=\frac{y-b}{y}.
$$

By the chain rule, $\dfrac{d}{dt}V(x(t),y(t))=V_x\dot x+V_y\dot y$:

$$
\dot V=\frac{x-a}{x}\,x(1-x-y)+\frac{y-b}{y}\,y(x-a)=(x-a)\big[(1-x-y)+(y-b)\big]=(x-a)(1-b-x).
$$

With $1-b=a$: $\dot V=(x-a)(a-x)=-(x-a)^2\le0$.

Also $V\ge0$ with equality only at $E^*$: the function $g(s)=s-c-c\ln(s/c)$ has $g'(s)=1-c/s$, negative for $s<c$ and positive for $s>c$, so its minimum is $g(c)=0$; $V$ is the sum of $g(x)$ with $c=a$ and $g(y)$ with $c=b$. $V\to\infty$ at the axes and at infinity, so every level set $V=\text{const}$ is a closed curve around $E^*$ and orbits stay bounded.

#### Step 3. Long-time outcome

$V$ decreases strictly except where $x=a$. On the line $x=a$ away from $E^*$, $\dot x=a(1-a-y)\neq0$, so the orbit leaves the line at once: no orbit other than $E^*$ stays where $\dot V=0$. Hence (LaSalle's invariance principle, extension) $V(x(t),y(t))\to0$ and every orbit starting in the open quadrant tends to $E^*$. The linearisation of (b) gives the final approach: spirals for $a<\tfrac45$, tangent to the slow eigenvector for $a>\tfrac45$.

**Ecological outcome:** neither species dies out; prey and predator settle to $x=a$, $y=1-a$. The prey density at coexistence equals the predator's death parameter; a less efficient predator (larger $a$) leaves more prey and fewer predators, and for $a\ge1$ (outside the data) $E^*$ leaves the quadrant and the predator goes extinct.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $a\to0^+$: $E^*\to(0,1)$, trace $\to0$, weakly damped oscillations (close to a centre). $a\to1^-$: $E^*\to E_1=(1,0)$ and the eigenvalue $1-a$ of $E_1$ tends to $0$: the two equilibria merge (transcritical bifurcation, extension). For all $a\in(0,1)$, $t\to\infty$ gives $(x,y)\to(a,1-a)$.
- **Checks:** $\mathbf f(a,1-a)=\big(a(1-a-(1-a)),\,(1-a)(a-a)\big)=\mathbf 0$; $\operatorname{tr}$ and $\det$ match sums and products of the eigenvalues in both cases; $P^{-1}J^*P$ is diagonal; numerical integration from $(0.2,0.2)$ ends at $E^*$ for $a=\tfrac12$ and $a=\tfrac9{11}$ (script). The model is dimensionless, so no units appear.
- **Common mistakes in the exam:** (1) writing the classical Lotka-Volterra centre: the logistic term $-x^2$ adds $-a$ to the trace and makes $E^*$ a sink; (2) concluding "stable" from $\det>0$ alone, without the sign of the trace; (3) taking the fast eigenvector as the direction of approach of a node: orbits arrive tangent to the slow one, $(3,-2)$; (4) using the linearisation to claim global convergence: Hartman-Grobman is only local, the global statement needs $V$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
