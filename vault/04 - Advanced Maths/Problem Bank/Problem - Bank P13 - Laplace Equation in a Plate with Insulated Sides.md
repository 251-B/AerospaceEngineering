---
materia: Advanced Maths
tema: "Unit 6: Laplace's equation in a rectangle"
bank_id: P13
title: "Laplace's equation in a rectangle with Neumann conditions on the vertical sides and Dirichlet data given by finite cosine sums: the zero mode, cosh and sinh modes, flux balance and uniqueness"
category: midterm_2_problem
archetype: pde-separation-laplace
level: standard
unit: 6
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2020_G47_SOL, MATHS_SECONDPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p13.py"
tags:
  - problem-bank
  - midterm-2
  - laplace-equation
  - separation-of-variables
  - neumann-conditions
  - zero-eigenvalue
  - uniqueness
---

# Bank P13 — Laplace equation in a plate with insulated sides

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the second midterm papers (MATHS_SECONDPARTIAL_2020_G47_SOL, MATHS_SECONDPARTIAL_2025_G47_SOL). Method: Haberman, *Elementary Applied PDEs* (unit 5 text, `BookPDE's.pdf`), Sec. 2.4 (eigenvalue problem with insulated ends, the zero eigenvalue), Sec. 2.5 (Laplace's equation in a rectangle, qualitative properties: maximum principle, well-posedness, solvability condition) and Sec. 3.3 (cosine series). Every result was checked with SymPy (scripts/am_bank/p13.py).

## Statement

The steady temperature $u(x,y)$ of the plate $0<x<\pi$, $0<y<1$ satisfies Laplace's equation
$$u_{xx}+u_{yy}=0 .$$
The vertical sides are insulated and the horizontal sides are held at prescribed temperatures:
$$u_x(0,y)=u_x(\pi,y)=0,\qquad u(x,0)=2+\cos 2x,\qquad u(x,1)=4+3\cos x .$$

(a) Separate variables, $u=X(x)Y(y)$, and solve the eigenvalue problem for $X$, discussing the three signs of the separation constant.

(b) Solve the equations for $Y$, paying special attention to the zero eigenvalue, and write the general solution that satisfies the conditions on the insulated sides.

(c) Impose the conditions on $y=0$ and $y=1$ and obtain $u(x,y)$ in closed form. Give $u$ at the centre $(\pi/2,\ 1/2)$.

(d) Compute $\displaystyle\Phi(y)=\int_0^{\pi}u_y(x,y)\,dx$ and explain why it does not depend on $y$. Is the solution unique? Would it be unique, and would it exist for any data, if the horizontal sides were also insulated?

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $u(x,y)$ on the rectangle $R=(0,\pi)\times(0,1)$; steady two-dimensional conduction, no sources.
- Operator: Laplacian, linear, second order, elliptic, homogeneous equation. The conditions are homogeneous (Neumann) in $x$ and non-homogeneous (Dirichlet) in $y$, so the eigenvalue problem is posed in $x$.
- Data: the bottom and top temperatures are **finite cosine sums**, i.e. already combinations of the eigenfunctions found in (a); no integral is needed for the coefficients.

#### Phase 2. Canonical formulation

$$\Delta u=0\ \text{in }R,\qquad \frac{\partial u}{\partial x}=0\ \text{on }x=0,\pi,\qquad u=f(x)\ \text{on }y=0,\qquad u=g(x)\ \text{on }y=1$$
with $f(x)=2+\cos2x$ and $g(x)=4+3\cos x$. Sturm-Liouville problem in $x$: $X''+\lambda X=0$, $X'(0)=X'(\pi)=0$.

## (a) Separation and the eigenvalue problem in x [1.5 pts]

### Hint

Divide $X''Y+XY''=0$ by $XY$. Translate $u_x=0$ on the sides into conditions on $X'$. Do not forget to test $\lambda=0$.

### Checkpoint

- $\dfrac{X''}{X}=-\dfrac{Y''}{Y}=-\lambda$; $X''+\lambda X=0$, $X'(0)=X'(\pi)=0$; $Y''-\lambda Y=0$.
- $\lambda<0$: only $X\equiv0$.
- $\lambda_0=0$ is an eigenvalue with $X_0=1$.
- $\lambda_n=n^2$, $X_n=\cos nx$, $n=1,2,\dots$

### Solution

#### Step 1. Separation

$u=X(x)Y(y)$ gives $X''Y+XY''=0$. Dividing by $XY$: $\dfrac{X''}{X}=-\dfrac{Y''}{Y}$. The left side depends only on $x$, the right only on $y$; both equal a constant $-\lambda$:
$$X''+\lambda X=0,\qquad Y''-\lambda Y=0$$
The side conditions $u_x(0,y)=X'(0)Y(y)=0$ for all $y$ and $Y\not\equiv0$ give $X'(0)=0$; likewise $X'(\pi)=0$.

#### Step 2. Case lambda < 0

$\lambda=-m^2$, $m>0$: $X=a\cosh mx+b\sinh mx$, $X'=m(a\sinh mx+b\cosh mx)$. $X'(0)=mb=0\Rightarrow b=0$. $X'(\pi)=ma\sinh m\pi=0$ with $\sinh m\pi>0\Rightarrow a=0$. Trivial.

#### Step 3. Case lambda = 0

$X''=0$, $X=a+bx$, $X'=b$. Both conditions give $b=0$, and $a$ is free: $X_0=1$ is an eigenfunction. With Neumann conditions the zero eigenvalue **does** occur (Haberman Sec. 2.4).

#### Step 4. Case lambda > 0

$\lambda=m^2$: $X=a\cos mx+b\sin mx$, $X'=m(-a\sin mx+b\cos mx)$. $X'(0)=mb=0\Rightarrow b=0$. $X'(\pi)=-ma\sin m\pi=0$ with $a\ne0$ requires $m=n\in\{1,2,\dots\}$. So $\lambda_n=n^2$, $X_n=\cos nx$.

## (b) The y equations and the general solution [1.0 pts]

### Hint

For $\lambda=0$ the $Y$ equation is $Y''=0$. For $\lambda=n^2>0$ the solutions are exponentials; write them with $\cosh$ and $\sinh$.

### Checkpoint

- $Y_0=A_0+B_0y$ (linear in $y$).
- $Y_n=A_n\cosh ny+B_n\sinh ny$.
- $\displaystyle u(x,y)=A_0+B_0y+\sum_{n=1}^{\infty}\cos nx\,\big(A_n\cosh ny+B_n\sinh ny\big)$.

### Solution

#### Step 1. Zero mode

$\lambda=0$: $Y''=0$, integrate twice: $Y'=B_0$, $Y=A_0+B_0y$. The product $X_0Y_0=A_0+B_0y$ is the part of the temperature that varies linearly between the plates.

#### Step 2. Modes n >= 1

$Y''-n^2Y=0$ has characteristic equation $r^2-n^2=0$, $r=\pm n$, so $Y=\alpha e^{ny}+\beta e^{-ny}$. With $\cosh ny=\tfrac12(e^{ny}+e^{-ny})$ and $\sinh ny=\tfrac12(e^{ny}-e^{-ny})$ this is $Y_n=A_n\cosh ny+B_n\sinh ny$ ($A_n=\alpha+\beta$, $B_n=\alpha-\beta$). The $\cosh/\sinh$ form is preferred because $\sinh 0=0$ and $\cosh0=1$ make the condition at $y=0$ immediate.

#### Step 3. Superposition

Every product satisfies Laplace's equation and the side conditions, and so does the sum:
$$u(x,y)=A_0+B_0y+\sum_{n=1}^{\infty}\cos nx\,\big(A_n\cosh ny+B_n\sinh ny\big)$$

## (c) Coefficients from the data and the closed form [1.5 pts]

### Hint

At $y=0$ only the $A$'s survive. Compare coefficients of $1$, $\cos x$, $\cos 2x$, ... (the cosines are orthogonal on $(0,\pi)$, so the expansion of a finite cosine sum is that sum itself). Then use $\cosh2\,\sinh2y$-type identities to simplify.

### Checkpoint

- $A_0=2$, $B_0=2$; $A_1=0$, $B_1=\dfrac{3}{\sinh1}$; $A_2=1$, $B_2=-\coth 2$; all other coefficients $0$.
- $\displaystyle u(x,y)=2+2y+\frac{3\sinh y}{\sinh1}\cos x+\frac{\sinh\big(2(1-y)\big)}{\sinh2}\cos2x$.
- $u(\pi/2,1/2)=3-\dfrac{1}{2\cosh1}\approx2.675973$.

### Solution

#### Step 1. Bottom side

$u(x,0)=A_0+\sum_n A_n\cos nx=2+\cos2x$. By orthogonality of $\{1,\cos nx\}$ on $(0,\pi)$ the coefficients are unique: $A_0=2$, $A_2=1$, $A_n=0$ for $n\ne2$. (Directly: $\frac1\pi\int_0^\pi(2+\cos2x)dx=2$ and $\frac2\pi\int_0^\pi(2+\cos2x)\cos nx\,dx=\delta_{n2}$.)

#### Step 2. Top side

$u(x,1)=A_0+B_0+\sum_n(A_n\cosh n+B_n\sinh n)\cos nx=4+3\cos x$:
- constant: $2+B_0=4\Rightarrow B_0=2$;
- $n=1$: $0\cdot\cosh1+B_1\sinh1=3\Rightarrow B_1=\dfrac{3}{\sinh1}$;
- $n=2$: $1\cdot\cosh2+B_2\sinh2=0\Rightarrow B_2=-\dfrac{\cosh2}{\sinh2}=-\coth2$;
- $n\ge3$: $B_n\sinh n=0\Rightarrow B_n=0$.

#### Step 3. Simplify the n = 2 mode

$$\cosh2y-\frac{\cosh2}{\sinh2}\sinh2y=\frac{\sinh2\cosh2y-\cosh2\sinh2y}{\sinh2}=\frac{\sinh(2-2y)}{\sinh2}$$
by $\sinh(a-b)=\sinh a\cosh b-\cosh a\sinh b$. It equals $1$ at $y=0$ and $0$ at $y=1$, as required. Therefore
$$u(x,y)=2+2y+\frac{3\sinh y}{\sinh1}\cos x+\frac{\sinh\big(2(1-y)\big)}{\sinh2}\cos2x$$

#### Step 4. Check

$u_{xx}=-\dfrac{3\sinh y}{\sinh1}\cos x-\dfrac{4\sinh(2-2y)}{\sinh2}\cos2x$ and $u_{yy}=\dfrac{3\sinh y}{\sinh1}\cos x+\dfrac{(-2)^2\sinh(2-2y)}{\sinh2}\cos2x$ (chain rule: $\frac{d}{dy}\sinh(2-2y)=-2\cosh(2-2y)$), so $u_{xx}+u_{yy}=0$. $u_x$ contains $\sin x$ and $\sin2x$, both zero at $x=0,\pi$.

#### Step 5. Centre

$\cos(\pi/2)=0$, $\cos\pi=-1$: $u(\pi/2,1/2)=2+1-\dfrac{\sinh1}{\sinh2}$. With $\sinh2=2\sinh1\cosh1$:
$$u\Big(\frac\pi2,\frac12\Big)=3-\frac{1}{2\cosh1}\approx3-0.324027=2.675973$$

## (d) Flux balance and uniqueness [1.0 pts]

### Hint

Integrate term by term in $x$: $\int_0^\pi\cos nx\,dx=0$ for $n\ge1$. For uniqueness, take the difference $w$ of two solutions and look at $\iint_R\lvert\nabla w\rvert^2$.

### Checkpoint

- $\Phi(y)=2\pi$ for every $y$: only the zero mode carries net flux.
- Constant because, integrating $u_{xx}+u_{yy}=0$ over $(0,\pi)$, $\Phi'(y)=-[u_x]_0^\pi=0$: what enters through one plate leaves through the other (insulated sides).
- Unique: with Dirichlet data on two sides, $w\equiv0$. With all four sides insulated, solutions exist only if the net flux data are compatible, and are unique only up to an additive constant.

### Solution

#### Step 1. The integral

$u_y=2+\dfrac{3\cosh y}{\sinh1}\cos x-\dfrac{2\cosh(2-2y)}{\sinh2}\cos2x$. Since $\int_0^\pi\cos x\,dx=[\sin x]_0^\pi=0$ and $\int_0^\pi\cos2x\,dx=\big[\tfrac12\sin2x\big]_0^\pi=0$:
$$\Phi(y)=\int_0^\pi 2\,dx=2\pi$$

#### Step 2. Why it is constant

$\Phi'(y)=\displaystyle\int_0^\pi u_{yy}\,dx=-\int_0^\pi u_{xx}\,dx=-\big[u_x\big]_{x=0}^{x=\pi}=-(0-0)=0$. Physically the heat flux $-K\,u_y$ through any horizontal line is the same: there are no sources inside and the sides are insulated. The temperature rises linearly on average, from mean $2$ at the bottom to mean $4$ at the top, so $B_0=2$ is exactly the mean gradient.

#### Step 3. Uniqueness (Dirichlet on two sides)

Let $u_1,u_2$ be two solutions and $w=u_1-u_2$: $\Delta w=0$, $w_x=0$ on $x=0,\pi$, $w=0$ on $y=0,1$. Green's first identity (extension: $\iint_R\big(w\Delta w+\lvert\nabla w\rvert^2\big)dA=\oint_{\partial R}w\,\dfrac{\partial w}{\partial n}\,ds$) gives $\iint_R\lvert\nabla w\rvert^2dA=0$, because on each side either $w=0$ or $\partial w/\partial n=0$. Hence $\nabla w=0$, $w$ is constant, and $w=0$ on $y=0$ makes it zero. The solution is unique. Consistently, the maximum principle (Haberman Sec. 2.5) bounds $u$ between the extreme boundary values: $1=u(\pi/2,0)\le u\le u(0,1)=7$ (the maximum principle on this mixed problem is checked on a grid in the script).

#### Step 4. All sides insulated

If $u_y$ were prescribed on $y=0$ and $y=1$ as well, the zero mode would only fix $B_0$ (twice) and leave $A_0$ free: solutions would differ by constants. Moreover, by Step 2 the prescribed fluxes would have to satisfy $\int_0^\pi u_y(x,0)\,dx=\int_0^\pi u_y(x,1)\,dx$ (solvability condition, Haberman Sec. 2.5): no net heat may enter a steady insulated plate. Data violating it give no solution at all.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** the $\cos2x$ mode imposed at the bottom decays upward like $\sinh(2(1-y))/\sinh2\approx e^{-2y}$; higher modes $\cos nx$ would decay like $e^{-ny}$, so fine detail of boundary data is felt only near the side where it is imposed. The zero mode does not decay: it is the only part of the data felt across the whole plate.
- **Checks:** $u(x,0)=2+0+0+\cos2x$ and $u(x,1)=4+3\cos x+0$; $u_x(0,y)=u_x(\pi,y)=0$; the centre value $2.676$ lies between the boundary extremes $1$ and $7$.
- **Common mistakes in the exam:** (1) discarding $\lambda=0$ as "trivial", which loses the linear part $2+2y$ and makes the constant data impossible to match; (2) using $\sin nx$ eigenfunctions (those belong to Dirichlet sides); (3) writing $Y_n=A_ne^{ny}+B_ne^{-ny}$ and then solving a $2\times2$ system with large numbers instead of using $\sinh(n(1-y))$; (4) claiming uniqueness only up to a constant, which is true only when every side is insulated.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
