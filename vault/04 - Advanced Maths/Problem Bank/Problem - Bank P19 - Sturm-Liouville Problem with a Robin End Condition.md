---
materia: Advanced Maths
tema: "Unit 5: Sturm-Liouville eigenvalue problems"
bank_id: P19
title: "Sturm-Liouville problem with a Dirichlet end and a Robin end: positivity, the transcendental eigenvalue equation, large eigenvalues, orthogonality and norms"
category: final_problem
archetype: sturm-liouville-eigenproblems
level: standard
unit: 5
difficulty: 3
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2014_EXTRA, MATHS_FINALEXAM_2018_ORD_SOL and MATHS_FINALEXAM_2021_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p19.py"
tags:
  - problem-bank
  - final-exam
  - sturm-liouville
  - robin-condition
  - transcendental-equation
  - orthogonality
  - asymptotic-eigenvalues
---

# Bank P19 — Sturm-Liouville problem with a Robin end condition

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2014_EXTRA, MATHS_FINALEXAM_2018_ORD_SOL and MATHS_FINALEXAM_2021_ORD_SOL. Method: Haberman, Elementary Applied PDEs (BookPDE's.pdf, unit 5 theory), Sec. 2.3 (the three cases of the separation constant), Sec. 5.3 and 5.5 (Sturm-Liouville problems, Green's formula and orthogonality), Sec. 5.6 (Rayleigh quotient), Sec. 5.8 (boundary conditions of the third kind) and Sec. 5.9 (large eigenvalues). Every result was checked with SymPy and mpmath (scripts/am_bank/p19.py).

## Statement

A rod $0\le x\le1$ has its end $x=0$ kept at zero temperature, while its end $x=1$ exchanges heat with surroundings at zero temperature by Newton's law, with a dimensionless transfer coefficient $h>0$. Separating variables in the heat equation leads to the eigenvalue problem

$$
X''(x)+\lambda X(x)=0,\quad 0<x<1,\qquad X(0)=0,\qquad X'(1)+h\,X(1)=0 .
$$

(a) Prove that the problem has no eigenvalue $\lambda\le0$. For $\lambda=\mu^2>0$ ($\mu>0$) find the eigenfunctions and show that $\mu$ must satisfy $\tan\mu=-\mu/h$.

(b) Show graphically that there are infinitely many eigenvalues $0<\lambda_1<\lambda_2<\dots$, locate $\mu_n$ in an interval of length $\pi/2$, and obtain the asymptotic behaviour of $\mu_n$ and $\lambda_n$ for large $n$. For $h=1$, give $\lambda_1$ and $\lambda_2$ to four significant figures and compare with the asymptotic formula.

(c) Prove, by integrating by parts (Green's identity), that eigenfunctions of different eigenvalues are orthogonal on $[0,1]$. Show that $\displaystyle\int_0^1\sin^2(\mu_nx)\,dx=\frac{\mu_n^2+h^2+h}{2(\mu_n^2+h^2)}$ and write the formula for the coefficients of the expansion $f(x)=\sum_n c_n\sin(\mu_nx)$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns: the eigenvalue $\lambda\in\mathbb R$ and the eigenfunction $X(x)\not\equiv0$ on $[0,1]$, of class $C^2$.
- Linear, homogeneous, second-order ODE with constant coefficients; homogeneous boundary conditions: Dirichlet at $x=0$, Robin (third kind) at $x=1$ with $h>0$.
- Data: $h>0$ (general); $h=1$ in the numerical questions.

#### Phase 2. Canonical formulation

Sturm-Liouville form (Haberman Sec. 5.3): $\dfrac{d}{dx}\Big(p\dfrac{dX}{dx}\Big)+qX+\lambda\sigma X=0$ with $p=1$, $q=0$, $\sigma=1$, and boundary conditions $\beta_1X(0)+\beta_2X'(0)=0$ with $(\beta_1,\beta_2)=(1,0)$, $\beta_3X(1)+\beta_4X'(1)=0$ with $(\beta_3,\beta_4)=(h,1)$. It is a regular Sturm-Liouville problem ($p,\sigma>0$ on $[0,1]$), so it has real eigenvalues, one eigenfunction per eigenvalue, and orthogonal eigenfunctions with weight $\sigma=1$.

## (a) No eigenvalues $\lambda\le0$ and the eigenvalue equation [0.8 pts]

### Hint

Treat $\lambda=-\mu^2<0$, $\lambda=0$ and $\lambda=\mu^2>0$ separately; in each case impose $X(0)=0$ first. Remember $\cosh\mu>0$ and $\sinh\mu>0$ for $\mu>0$.

### Checkpoint

- $\lambda<0$: $\mu\cosh\mu+h\sinh\mu>0$ forces $X\equiv0$. $\lambda=0$: $(1+h)A=0$ forces $X\equiv0$.
- $\lambda=\mu^2>0$: $X_n=\sin(\mu_nx)$ with $\mu\cos\mu+h\sin\mu=0$, i.e. $\tan\mu=-\mu/h$.

### Solution

#### Step 1. Case $\lambda=-\mu^2<0$, $\mu>0$

Characteristic equation $r^2-\mu^2=0$, $r=\pm\mu$, so $X=A\cosh(\mu x)+B\sinh(\mu x)$. $X(0)=A=0$. Then $X'=B\mu\cosh(\mu x)$ and

$$
X'(1)+hX(1)=B\big(\mu\cosh\mu+h\sinh\mu\big)=0 .
$$

For $\mu>0$ and $h>0$ both terms in the bracket are positive, so $B=0$ and $X\equiv0$: no negative eigenvalues.

#### Step 2. Case $\lambda=0$

$X''=0$, so integrating twice $X=Ax+B$. $X(0)=B=0$; $X'(1)+hX(1)=A+hA=(1+h)A=0$ with $1+h>0$, so $A=0$: $\lambda=0$ is not an eigenvalue.

#### Step 3. Cross-check with the Rayleigh quotient

Multiplying $X''=-\lambda X$ by $X$ and integrating by parts, $\int_0^1XX''dx=[XX']_0^1-\int_0^1(X')^2dx$, so (Haberman Sec. 5.6)

$$
\lambda=\frac{-[XX']_0^1+\int_0^1(X')^2dx}{\int_0^1X^2dx}=\frac{h\,X(1)^2+\int_0^1(X')^2dx}{\int_0^1X^2dx},
$$

using $X(0)=0$ and $X'(1)=-hX(1)$. The numerator is $\ge0$, and it is $0$ only if $X'\equiv0$ and $X(1)=0$, i.e. $X\equiv0$. Hence $\lambda>0$, in agreement with Steps 1-2.

#### Step 4. Case $\lambda=\mu^2>0$

$r^2+\mu^2=0$, $r=\pm i\mu$, so $X=A\cos(\mu x)+B\sin(\mu x)$. $X(0)=A=0$, $X=B\sin(\mu x)$, $X'=B\mu\cos(\mu x)$:

$$
X'(1)+hX(1)=B\big(\mu\cos\mu+h\sin\mu\big)=0 .
$$

A nontrivial solution needs $B\neq0$, so $\mu\cos\mu+h\sin\mu=0$. If $\cos\mu=0$ this would give $h\sin\mu=\pm h=0$, impossible; so we may divide by $h\cos\mu$:

$$
\tan\mu=-\frac{\mu}{h},\qquad X_n(x)=\sin(\mu_nx),\qquad \lambda_n=\mu_n^2 .
$$

## (b) Infinitely many eigenvalues and their asymptotic behaviour [0.8 pts]

### Hint

Plot $y=\tan\mu$ and the straight line $y=-\mu/h$ for $\mu>0$. For large $n$ set $\mu_n=(n-\tfrac12)\pi+\varepsilon_n$ and use $\tan\big((n-\tfrac12)\pi+\varepsilon\big)=-\cot\varepsilon$.

### Checkpoint

- One root on each branch: $(n-\tfrac12)\pi<\mu_n<n\pi$, $n=1,2,\dots$
- $\mu_n=(n-\tfrac12)\pi+\dfrac{h}{(n-\frac12)\pi}+O(n^{-3})$, $\ \lambda_n=(n-\tfrac12)^2\pi^2+2h+O(n^{-2})$.
- $h=1$: $\mu_1=2.029$, $\lambda_1=4.116$; $\mu_2=4.913$, $\lambda_2=24.14$ (asymptotic: $\mu_1\approx2.207$, $\mu_2\approx4.925$).

### Solution

#### Step 1. Graphical argument

For $\mu>0$ the line $y=-\mu/h$ is negative and decreasing. The function $\tan\mu$ has branches on $\big((n-\tfrac12)\pi,(n+\tfrac12)\pi\big)$, on each of which it increases continuously from $-\infty$ to $+\infty$; on the first piece $(0,\pi/2)$ it is positive, so there is no root there. On the branch $n\ge1$, $\tan\mu<0$ exactly on $\big((n-\tfrac12)\pi,n\pi\big)$, and the difference $\tan\mu+\mu/h$ goes from $-\infty$ to $n\pi/h>0$ there, increasing strictly (its derivative is $\sec^2\mu+1/h>0$). By the intermediate value theorem it vanishes **exactly once**:

$$
\Big(n-\frac12\Big)\pi<\mu_n<n\pi,\qquad n=1,2,3,\dots
$$

There are infinitely many branches, hence infinitely many eigenvalues $\lambda_n=\mu_n^2$, increasing to $+\infty$ (Haberman Sec. 5.3, property 2). Negative roots $-\mu_n$ give the same eigenfunctions up to sign and are not new.

#### Step 2. Large $n$

Write $p_n=(n-\tfrac12)\pi$ and $\mu_n=p_n+\varepsilon_n$ with $0<\varepsilon_n<\pi/2$. Since $\cos p_n=0$ and $\sin p_n=\pm1$, the addition formulas give $\tan(p_n+\varepsilon)=\dfrac{\sin(p_n+\varepsilon)}{\cos(p_n+\varepsilon)}=\dfrac{\sin p_n\cos\varepsilon}{-\sin p_n\sin\varepsilon}=-\cot\varepsilon$. The eigenvalue equation becomes

$$
-\cot\varepsilon_n=-\frac{p_n+\varepsilon_n}{h}\iff\tan\varepsilon_n=\frac{h}{p_n+\varepsilon_n}.
$$

The right-hand side tends to $0$, so $\varepsilon_n\to0$ and $\tan\varepsilon_n=\varepsilon_n+O(\varepsilon_n^3)$: $\varepsilon_n=\dfrac h{p_n}+O(p_n^{-3})$. Squaring,

$$
\lambda_n=\mu_n^2=p_n^2+2p_n\varepsilon_n+\varepsilon_n^2=\Big(n-\frac12\Big)^2\pi^2+2h+O(n^{-2}).
$$

Geometrically: the line becomes steeper relative to the branches, and the roots crowd towards the left asymptotes $(n-\tfrac12)\pi$ (Haberman Sec. 5.9). The leading term $(n-\frac12)^2\pi^2$ is the eigenvalue of the problem with $X(0)=0$, $X'(1)=0$: for large $n$ the eigenfunctions oscillate so fast that the Robin end looks like an insulated end.

#### Step 3. Numbers for $h=1$

Solving $\mu\cos\mu+\sin\mu=0$ numerically (Newton's method or bisection) inside $(\pi/2,\pi)$ and $(3\pi/2,2\pi)$:

| $n$ | interval | $\mu_n$ | $\lambda_n$ | asymptotic $\mu_n$ | asymptotic $\lambda_n$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | $(1.571,\,3.142)$ | $2.029$ | $4.116$ | $\frac\pi2+\frac2\pi=2.207$ | $\frac{\pi^2}4+2=4.467$ |
| 2 | $(4.712,\,6.283)$ | $4.913$ | $24.14$ | $\frac{3\pi}2+\frac2{3\pi}=4.925$ | $\frac{9\pi^2}4+2=24.21$ |

The error of the asymptotic formula drops from about $9\%$ to $0.3\%$ between $n=1$ and $n=2$ for $\lambda_n$.

## (c) Orthogonality and norms [0.9 pts]

### Hint

Compute $\int_0^1\big(X_mX_n''-X_nX_m''\big)dx$ in two ways: with the ODE, and by parts. For the norm use $\sin^2s=\frac{1-\cos2s}2$ and then the eigenvalue equation to remove $\cos\mu_n$.

### Checkpoint

- $\int_0^1(X_mX_n''-X_nX_m'')dx=\big[X_mX_n'-X_nX_m'\big]_0^1=0$, hence $(\lambda_m-\lambda_n)\int_0^1X_mX_n\,dx=0$.
- $\int_0^1\sin^2(\mu_nx)dx=\dfrac12-\dfrac{\sin2\mu_n}{4\mu_n}=\dfrac{\mu_n^2+h^2+h}{2(\mu_n^2+h^2)}$; for $h=1$, $n=1$: $0.5977$.
- $c_n=\dfrac{2(\mu_n^2+h^2)}{\mu_n^2+h^2+h}\displaystyle\int_0^1f(x)\sin(\mu_nx)\,dx$.

### Solution

#### Step 1. Green's identity

For $C^2$ functions $u,v$, the product rule gives $\dfrac{d}{dx}(uv'-vu')=u'v'+uv''-v'u'-vu''=uv''-vu''$. Integrating over $[0,1]$ with Barrow's rule (Haberman Sec. 5.5, Green's formula with $p=1$):

$$
\int_0^1(uv''-vu'')\,dx=\big[uv'-vu'\big]_0^1=\big(u(1)v'(1)-v(1)u'(1)\big)-\big(u(0)v'(0)-v(0)u'(0)\big).
$$

#### Step 2. The boundary terms vanish

Take $u=X_m$, $v=X_n$ with $m\neq n$. At $x=0$: $X_m(0)=X_n(0)=0$, so the bracket is $0$. At $x=1$: $X_m'(1)=-hX_m(1)$ and $X_n'(1)=-hX_n(1)$, so

$$
X_m(1)X_n'(1)-X_n(1)X_m'(1)=X_m(1)\big(-hX_n(1)\big)-X_n(1)\big(-hX_m(1)\big)=0 .
$$

#### Step 3. Orthogonality

With the ODE, $X_n''=-\lambda_nX_n$ and $X_m''=-\lambda_mX_m$:

$$
\int_0^1(X_mX_n''-X_nX_m'')\,dx=(\lambda_m-\lambda_n)\int_0^1X_mX_n\,dx=0 .
$$

Since $\lambda_m\neq\lambda_n$ (the $\mu_n$ lie in disjoint intervals), $\displaystyle\int_0^1\sin(\mu_mx)\sin(\mu_nx)\,dx=0$. Note that the $\mu_n$ are not multiples of a common number, so this is not the elementary orthogonality of $\sin(n\pi x)$: it holds because of the boundary condition. (Direct check in the script: the integral $\frac{n\sin m\cos n-m\cos m\sin n}{m^2-n^2}$ vanishes after substituting $\cos\mu=-h\sin\mu/\mu$.)

#### Step 4. Norm

With $\sin^2s=\frac12(1-\cos2s)$ and the substitution $s=2\mu_nx$, $ds=2\mu_n\,dx$ for the cosine:

$$
\int_0^1\sin^2(\mu_nx)\,dx=\Big[\frac x2-\frac{\sin(2\mu_nx)}{4\mu_n}\Big]_0^1=\frac12-\frac{\sin2\mu_n}{4\mu_n}=\frac12-\frac{\sin\mu_n\cos\mu_n}{2\mu_n}.
$$

From the eigenvalue equation $\cos\mu_n=-\dfrac{h\sin\mu_n}{\mu_n}$, so $-\dfrac{\sin\mu_n\cos\mu_n}{2\mu_n}=\dfrac{h\sin^2\mu_n}{2\mu_n^2}$. Squaring the same equation, $\mu_n^2\cos^2\mu_n=h^2\sin^2\mu_n$, i.e. $\mu_n^2(1-\sin^2\mu_n)=h^2\sin^2\mu_n$, so $\sin^2\mu_n=\dfrac{\mu_n^2}{\mu_n^2+h^2}$. Therefore

$$
\int_0^1\sin^2(\mu_nx)\,dx=\frac12+\frac{h}{2(\mu_n^2+h^2)}=\frac{\mu_n^2+h^2+h}{2(\mu_n^2+h^2)}.
$$

For $h=1$, $n=1$: $\dfrac{4.1159+1+1}{2(4.1159+1)}=0.5977$. The norm is slightly above $\tfrac12$ and tends to $\tfrac12$ as $n\to\infty$.

#### Step 5. Expansion coefficients

If $f(x)=\sum_{n\ge1}c_n\sin(\mu_nx)$, multiply by $\sin(\mu_mx)$, integrate over $[0,1]$ and use Step 3 (only $n=m$ survives; Haberman Sec. 5.3):

$$
c_m=\frac{\int_0^1f(x)\sin(\mu_mx)\,dx}{\int_0^1\sin^2(\mu_mx)\,dx}=\frac{2(\mu_m^2+h^2)}{\mu_m^2+h^2+h}\int_0^1f(x)\sin(\mu_mx)\,dx .
$$

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $h\to0^+$ (insulated end): $\tan\mu=0^-$ pushes $\mu_n\to(n-\frac12)\pi$, the eigenvalues of $X(0)=0$, $X'(1)=0$, and the norm $\to\frac12$. $h\to\infty$ (end held at zero): the line becomes horizontal, $\tan\mu\to0^-$ from the left of $n\pi$, so $\mu_n\to n\pi$, the Dirichlet eigenvalues $n^2\pi^2$, and the norm $\to\frac12$. For every $h>0$, $\lambda_n$ lies between these two Dirichlet-Neumann bounds.
- **Checks:** $\sin(\mu_nx)$ satisfies the ODE and both boundary conditions (script); the numerical roots lie in the predicted intervals; $\int_0^1\sin(\mu_1x)\sin(\mu_2x)dx=0$ numerically to 20 digits; the norm formula agrees with direct quadrature. In the heat problem the mode $n$ decays as $e^{-k\lambda_nt}$, so $\lambda_1=4.116$ (for $h=1$) sets the slowest decay rate.
- **Common mistakes in the exam:** (1) dropping the case $\lambda<0$ or $\lambda=0$ without proof, or "proving" it with the wrong sign of $h$; (2) writing $\mu_n=n\pi$ or $(n-\tfrac12)\pi$, as for Dirichlet or Neumann ends; (3) placing the roots in $(n\pi,(n+\tfrac12)\pi)$, where $\tan\mu>0$; (4) using $\int_0^1\sin^2=\tfrac12$ for the norm, which is false here because $\sin2\mu_n\neq0$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
