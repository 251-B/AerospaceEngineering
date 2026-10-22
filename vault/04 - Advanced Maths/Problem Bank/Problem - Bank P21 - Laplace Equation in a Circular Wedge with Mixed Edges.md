---
materia: Advanced Maths
tema: "Unit 6: Laplace's equation, separation of variables in polar coordinates"
bank_id: P21
title: "Laplace's equation in a circular wedge with one edge held at zero and the other insulated: angular eigenfunctions, bounded radial powers and a datum that is a hidden finite sum"
category: final_problem
archetype: pde-separation-laplace
level: standard
unit: 6
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2014_ORD_B, MATHS_FINALEXAM_2019_ORD_SOL and MATHS_FINALEXAM_2022_EXTRA; not an official exercise. Verified with scripts/am_bank/p21.py"
tags:
  - problem-bank
  - final-exam
  - laplace-equation
  - polar-coordinates
  - mixed-boundary-conditions
  - euler-equation
  - separation-of-variables
---

# Bank P21 — Laplace's equation in a circular wedge with mixed edges

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2014_ORD_B, MATHS_FINALEXAM_2019_ORD_SOL and MATHS_FINALEXAM_2022_EXTRA. Method: Haberman, Elementary Applied PDEs (BookPDE's.pdf, unit 5-6 theory), Sec. 2.3 (separation of variables and the three cases of the separation constant), Sec. 2.4 (insulated boundaries), Sec. 2.5 (Laplace's equation inside a circular disk, the equidimensional radial equation and the boundedness condition at $r=0$) and Sec. 5.3 (orthogonality of Sturm-Liouville eigenfunctions). Every result was checked with SymPy (scripts/am_bank/p21.py).

## Statement

A thin plate has the shape of the circular sector $D=\{(r,\theta):\ 0<r<a,\ 0<\theta<\alpha\}$, with $0<\alpha\le2\pi$. Its faces are insulated, so its steady temperature $u(r,\theta)$ solves

$$
\Delta u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}=0\quad\text{in }D,
$$

$$
u(r,0)=0,\qquad u_\theta(r,\alpha)=0\quad(0<r<a),\qquad \lvert u(r,\theta)\rvert\ \text{bounded as } r\to0^+,\qquad u(a,\theta)=f(\theta)\quad(0<\theta<\alpha).
$$

The straight edge $\theta=0$ is held at temperature $0$, the straight edge $\theta=\alpha$ is insulated, and the arc $r=a$ has a prescribed temperature.

(a) Separate variables, $u=R(r)\Theta(\theta)$, and solve the angular eigenvalue problem, discussing the three possible signs of the separation constant. Show that the eigenfunctions are $\Theta_n=\sin\big(\nu_n\theta\big)$ with $\nu_n=\dfrac{(2n-1)\pi}{2\alpha}$, $n=1,2,\dots$

(b) Solve the radial equation, justify which solutions are admissible, and write the general bounded solution together with the formula for its coefficients in terms of $f$.

(c) Let $\alpha=\pi/2$ (a quarter disc) and $f(\theta)=\sin^3\theta$. Find $u(r,\theta)$ in closed form, check all the conditions, write it in Cartesian coordinates $x=r\cos\theta$, $y=r\sin\theta$, and give $u$ at $(r,\theta)=(a/2,\pi/2)$ and at $(a/2,\pi/6)$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $u(r,\theta)$, independent variables $r\in(0,a)$, $\theta\in(0,\alpha)$; $u\in C^2(D)$, continuous up to the boundary except possibly at corners.
- Linear, homogeneous, second-order elliptic PDE (Laplace). Homogeneous conditions on the two straight edges (Dirichlet at $\theta=0$, Neumann at $\theta=\alpha$) and a boundedness condition at the vertex $r=0$; the only nonhomogeneous condition is on the arc $r=a$. This is the structure that allows separation of variables with eigenfunctions in $\theta$.
- Data: $a>0$ (radius), $\alpha$ (opening angle), $f$ (arc datum). In (c): $\alpha=\pi/2$, $f=\sin^3\theta$; $u$ is a dimensionless temperature.

#### Phase 2. Canonical formulation

Multiplying the PDE by $r^2$: $r^2u_{rr}+ru_r+u_{\theta\theta}=0$. With $u=R(r)\Theta(\theta)$:

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}=\lambda\quad(\text{constant}),
$$

$$
\Theta''+\lambda\Theta=0,\ \ \Theta(0)=0,\ \ \Theta'(\alpha)=0;\qquad r^2R''+rR'-\lambda R=0,\ \ \lvert R(0^+)\rvert<\infty .
$$

The angular problem is a regular Sturm-Liouville problem with $p=\sigma=1$, $q=0$ (Haberman Sec. 5.3).

## (a) Separation and the angular eigenvalue problem [1.0 pts]

### Hint

Insert $u=R\Theta$ in $r^2u_{rr}+ru_r+u_{\theta\theta}=0$ and divide by $R\Theta$. Impose $\Theta(0)=0$ first, then $\Theta'(\alpha)=0$.

### Checkpoint

- $\lambda<0$ and $\lambda=0$: only $\Theta\equiv0$.
- $\lambda=\nu^2>0$: $\Theta=\sin\nu\theta$ with $\cos\nu\alpha=0$, so $\nu_n=\dfrac{(2n-1)\pi}{2\alpha}$, $\lambda_n=\nu_n^2$.
- $\displaystyle\int_0^\alpha\sin\nu_m\theta\,\sin\nu_n\theta\,d\theta=\frac\alpha2\delta_{mn}$.

### Solution

#### Step 1. Separation

$u_{rr}=R''\Theta$, $u_r=R'\Theta$, $u_{\theta\theta}=R\Theta''$. Then $r^2R''\Theta+rR'\Theta+R\Theta''=0$; dividing by $R\Theta$ (where it is not zero),

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}.
$$

The left side depends only on $r$ and the right only on $\theta$, so both equal a constant $\lambda$. The edge conditions become $R(r)\Theta(0)=0$ and $R(r)\Theta'(\alpha)=0$ for all $r$; for a nontrivial $R$, $\Theta(0)=0$ and $\Theta'(\alpha)=0$.

#### Step 2. Case $\lambda=-\mu^2<0$

$\Theta=A\cosh\mu\theta+B\sinh\mu\theta$. $\Theta(0)=A=0$. $\Theta'(\alpha)=B\mu\cosh\mu\alpha=0$; since $\mu>0$ and $\cosh\mu\alpha\ge1$, $B=0$. Trivial.

#### Step 3. Case $\lambda=0$

$\Theta''=0$, $\Theta=A\theta+B$. $\Theta(0)=B=0$, $\Theta'(\alpha)=A=0$. Trivial: unlike the full disc, the constant is not allowed (it would violate $u=0$ on $\theta=0$).

#### Step 4. Case $\lambda=\nu^2>0$

$\Theta=A\cos\nu\theta+B\sin\nu\theta$. $\Theta(0)=A=0$. $\Theta'(\alpha)=B\nu\cos\nu\alpha=0$ with $B\neq0$, $\nu>0$, so $\cos\nu\alpha=0$:

$$
\nu\alpha=\frac{(2n-1)\pi}{2}\ \Longrightarrow\ \nu_n=\frac{(2n-1)\pi}{2\alpha},\qquad \Theta_n(\theta)=\sin\Big(\frac{(2n-1)\pi\theta}{2\alpha}\Big),\qquad n=1,2,\dots
$$

Each $\Theta_n$ vanishes at $\theta=0$ and has zero slope at $\theta=\alpha$: a quarter wave, three quarter waves, and so on across the opening.

#### Step 5. Orthogonality and norm

For $m\neq n$ the eigenvalues differ, so $\int_0^\alpha\Theta_m\Theta_n\,d\theta=0$ (Haberman Sec. 5.3; the boundary terms $[\Theta_m\Theta_n'-\Theta_n\Theta_m']_0^\alpha$ vanish because $\Theta(0)=0$ and $\Theta'(\alpha)=0$). For $m=n$, with $\sin^2s=\frac12(1-\cos2s)$:

$$
\int_0^\alpha\sin^2\nu_n\theta\,d\theta=\Big[\frac\theta2-\frac{\sin2\nu_n\theta}{4\nu_n}\Big]_0^\alpha=\frac\alpha2-\frac{\sin\big((2n-1)\pi\big)}{4\nu_n}=\frac\alpha2 .
$$

## (b) Radial equation and the general bounded solution [0.6 pts]

### Hint

$r^2R''+rR'-\nu^2R=0$ is an equidimensional (Euler) equation: try $R=r^p$.

### Checkpoint

- $R=r^p$ gives $p^2-\nu_n^2=0$, $R=c_1r^{\nu_n}+c_2r^{-\nu_n}$; boundedness forces $c_2=0$.
- $u(r,\theta)=\displaystyle\sum_{n=1}^\infty A_n\Big(\frac ra\Big)^{\nu_n}\sin\nu_n\theta$, $\ A_n=\frac2\alpha\int_0^\alpha f(\theta)\sin\nu_n\theta\,d\theta$.

### Solution

#### Step 1. Euler equation

With $R=r^p$: $R'=pr^{p-1}$, $R''=p(p-1)r^{p-2}$, so $r^2R''+rR'-\nu^2R=\big[p(p-1)+p-\nu^2\big]r^p=(p^2-\nu^2)r^p$. Hence $p=\pm\nu_n$ and, since $\nu_n\neq0$, the two roots are distinct (Haberman Sec. 2.5):

$$
R_n(r)=c_1r^{\nu_n}+c_2r^{-\nu_n}.
$$

#### Step 2. Boundedness at the vertex

$\nu_n>0$, so $r^{-\nu_n}\to\infty$ as $r\to0^+$ while $r^{\nu_n}\to0$. The condition $\lvert u\rvert<\infty$ at $r=0$ forces $c_2=0$. (The $\lambda=0$ branch $c_1+c_2\ln r$ does not appear, because $\lambda=0$ is not an eigenvalue.)

#### Step 3. Superposition and coefficients

By linearity (Haberman Sec. 2.2), the sum of the product solutions is a solution of the PDE that satisfies the homogeneous conditions. Writing the constants as $A_n/a^{\nu_n}$ for convenience:

$$
u(r,\theta)=\sum_{n=1}^\infty A_n\Big(\frac ra\Big)^{\nu_n}\sin\nu_n\theta .
$$

At $r=a$: $f(\theta)=\sum_nA_n\sin\nu_n\theta$. Multiplying by $\sin\nu_m\theta$, integrating over $(0,\alpha)$ and using (a), Step 5:

$$
A_m=\frac{\int_0^\alpha f(\theta)\sin\nu_m\theta\,d\theta}{\alpha/2}=\frac2\alpha\int_0^\alpha f(\theta)\sin\nu_m\theta\,d\theta .
$$

## (c) Quarter disc with $f=\sin^3\theta$ [0.9 pts]

### Hint

With $\alpha=\pi/2$ the eigenfunctions are $\sin\theta,\sin3\theta,\sin5\theta,\dots$ Expand $\sin3\theta$ with the addition formulas: the datum is a finite combination of eigenfunctions, so no integral is needed.

### Checkpoint

- $\nu_n=2n-1$; $\sin^3\theta=\tfrac34\sin\theta-\tfrac14\sin3\theta$; $A_1=\tfrac34$, $A_2=-\tfrac14$, $A_n=0$ for $n\ge3$.
- $u(r,\theta)=\dfrac34\,\dfrac ra\sin\theta-\dfrac14\Big(\dfrac ra\Big)^3\sin3\theta$; Cartesian: $u=\dfrac{3y}{4a}-\dfrac{3x^2y-y^3}{4a^3}$.
- $u(a/2,\pi/2)=\dfrac{13}{32}$, $\ u(a/2,\pi/6)=\dfrac5{32}$.

### Solution

#### Step 1. Eigenvalues for the quarter disc

$\nu_n=\dfrac{(2n-1)\pi}{2\cdot\pi/2}=2n-1$: eigenfunctions $\sin\theta$, $\sin3\theta$, $\sin5\theta,\dots$, and radial factors $r$, $r^3$, $r^5,\dots$

#### Step 2. The datum as a finite sum

$\sin3\theta=\sin(2\theta+\theta)=\sin2\theta\cos\theta+\cos2\theta\sin\theta=2\sin\theta\cos^2\theta+(1-2\sin^2\theta)\sin\theta$. With $\cos^2\theta=1-\sin^2\theta$: $\sin3\theta=2\sin\theta-2\sin^3\theta+\sin\theta-2\sin^3\theta=3\sin\theta-4\sin^3\theta$. Solving for the cube:

$$
\sin^3\theta=\frac34\sin\theta-\frac14\sin3\theta .
$$

Both terms are eigenfunctions, so by uniqueness of the coefficients (orthogonality) $A_1=\tfrac34$, $A_2=-\tfrac14$ and $A_n=0$ for $n\ge3$. Cross-check of $A_1$ with the formula of (b): $A_1=\frac4\pi\int_0^{\pi/2}\sin^3\theta\sin\theta\,d\theta=\frac4\pi\cdot\frac{3\pi}{16}=\frac34$, using $\int_0^{\pi/2}\sin^4\theta\,d\theta=\frac{3\pi}{16}$ (from $\sin^4=\frac38-\frac12\cos2\theta+\frac18\cos4\theta$).

#### Step 3. Solution

$$
u(r,\theta)=\frac34\,\frac ra\,\sin\theta-\frac14\Big(\frac ra\Big)^3\sin3\theta .
$$

Checks: $u(r,0)=0$ because $\sin0=0$; $u_\theta=\frac34\frac ra\cos\theta-\frac34\big(\frac ra\big)^3\cos3\theta$ vanishes at $\theta=\pi/2$ because $\cos\frac\pi2=\cos\frac{3\pi}2=0$; $u$ is bounded (a polynomial in $r$); $u(a,\theta)=\frac34\sin\theta-\frac14\sin3\theta=\sin^3\theta$. Each term $r^\nu\sin\nu\theta$ is harmonic by Step 1 of (b).

#### Step 4. Cartesian form

$r\sin\theta=y$, and $r^3\sin3\theta=r^3(3\sin\theta\cos^2\theta-\sin^3\theta)=3(r\cos\theta)^2(r\sin\theta)-(r\sin\theta)^3=3x^2y-y^3$ (using $\sin3\theta=3\sin\theta-4\sin^3\theta=3\sin\theta\cos^2\theta-\sin^3\theta$). Therefore

$$
u(x,y)=\frac{3y}{4a}-\frac{3x^2y-y^3}{4a^3}.
$$

Direct check: $u_{xx}=-\dfrac{6y}{4a^3}$, $u_{yy}=\dfrac{6y}{4a^3}$, so $\Delta u=0$. On the insulated edge $x=0$ ($\theta=\pi/2$), $u_x=-\dfrac{6xy}{4a^3}=0$: the normal derivative vanishes, as required. On $y=0$ ($\theta=0$), $u=0$.

#### Step 5. Values

- $(r,\theta)=(a/2,\pi/2)$: $\sin\frac\pi2=1$, $\sin\frac{3\pi}2=-1$, so $u=\frac34\cdot\frac12+\frac14\cdot\frac18=\frac38+\frac1{32}=\frac{13}{32}\approx0.406$.
- $(r,\theta)=(a/2,\pi/6)$: $\sin\frac\pi6=\frac12$, $\sin\frac\pi2=1$, so $u=\frac34\cdot\frac12\cdot\frac12-\frac14\cdot\frac18=\frac3{16}-\frac1{32}=\frac5{32}\approx0.156$.

Both lie between the minimum $0$ and the maximum $1$ of the boundary values, as the maximum principle for Laplace's equation requires (Haberman Sec. 2.5).

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $r\to0$: $u\approx\frac34\frac ra\sin\theta\to0$, the vertex takes the temperature of the cold edge; the leading mode $r^{\nu_1}$ dominates near the vertex. For a general opening, $\nu_1=\pi/(2\alpha)<1$ when $\alpha>\pi/2$: $u$ stays bounded but $\lvert\nabla u\rvert\sim r^{\nu_1-1}\to\infty$ at the vertex (a corner singularity caused by the mixed conditions; with $u=0$ on both edges it would only appear for $\alpha>\pi$). The quarter disc, $\nu_1=1$, is exactly the borderline case with a finite gradient. Along the insulated edge, $u(r,\pi/2)=\frac34s+\frac14s^3$ with $s=r/a$ increases monotonically from $0$ to $1$.
- **Checks:** the PDE, the two edge conditions, boundedness and the arc datum are satisfied (script, in polar and Cartesian form); the coefficient formula of (b) reproduces $A_1=\frac34$, $A_2=-\frac14$ and $A_n=0$ for $n=3,4,5$; the norm $\int_0^{\pi/2}\sin^23\theta\,d\theta=\frac\pi4=\frac\alpha2$. Dimensionless problem: $(r/a)^\nu$ is a pure number for any $a$.
- **Common mistakes in the exam:** (1) using the full-disc eigenfunctions $\cos n\theta,\sin n\theta$ or the half-disc ones $\sin n\theta$ ($\nu=n$): the insulated edge requires odd quarter-wave multiples; (2) keeping $r^{-\nu}$ or a $\ln r$ term, which blow up at the vertex; (3) computing the coefficients by integrals over $(0,\pi)$ or with norm $\pi/2$ instead of $\alpha/2=\pi/4$; (4) not recognising $\sin^3\theta$ as a finite sum and writing an infinite series with wrong integrals.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
