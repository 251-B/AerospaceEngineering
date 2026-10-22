---
materia: Advanced Maths
tema: "Unit 3: reduction of order for variable-coefficient equations"
bank_id: P15
title: "x y'' - (x+2) y' + 2y = 0 with the known solution e^x: a polynomial second solution by reduction of order, the forced equation with x^3 e^x, and initial-value problems at the singular point x = 0"
category: final_problem
archetype: ode-second-order-reduction
level: standard
unit: 3
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2020_ORD, MATHS_FINALEXAM_2022_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p15.py"
tags:
  - problem-bank
  - final-exam
  - reduction-of-order
  - variable-coefficients
  - wronskian
  - singular-point
---

# Bank P15 — Reduction of order with an exponential solution and a singular point

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final exams (MATHS_FINALEXAM_2020_ORD, MATHS_FINALEXAM_2022_ORD_SOL). Method: reduction of order (Notes.pdf, p. 7; Robinson Ch. 17), the Wronskian (Robinson Sec. 11.3-11.4) and Abel's formula, first-order linear equations with an integrating factor (Robinson Ch. 9), and Picard's theorem (Robinson Sec. 6.2). Every result was checked with SymPy (scripts/am_bank/p15.py).

## Statement

Consider, for $x>0$, the equation
$$x\,y''-(x+2)\,y'+2y=0 .$$

(a) Check that $y_1(x)=e^x$ is a solution. Using $y=v(x)\,e^x$, find a second solution $y_2$, linearly independent of $y_1$, and compute the Wronskian $W(y_1,y_2)$.

(b) Find the general solution of
$$x\,y''-(x+2)\,y'+2y=x^3e^x,\qquad x>0,$$
again with the substitution $y=v\,e^x$.

(c) The solutions of (b) extend smoothly to $x=0$. Show that all of them satisfy $y'(0)=y(0)$. What does this say about the initial-value problems $y(0)=1,\ y'(0)=0$ and $y(0)=1,\ y'(0)=1$? Why does this not contradict Picard's theorem?

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $y(x)$, independent variable $x$, domain $x>0$ (the leading coefficient $x$ vanishes at $x=0$).
- Operator: linear, second order, variable coefficients; (a) homogeneous, (b) non-homogeneous with $g=x^3e^x$.
- One solution is known, so the order can be reduced: $v'$ satisfies a first-order linear equation.

#### Phase 2. Canonical formulation

Dividing by $x$ gives the standard form $y''+p(x)y'+q(x)y=f(x)$ with
$$p(x)=-\frac{x+2}{x}=-1-\frac2x,\qquad q(x)=\frac2x,\qquad f(x)=x^2e^x .$$
$p$, $q$, $f$ are continuous on $x>0$, so every initial-value problem posed at $x_0>0$ has a unique solution there; at $x_0=0$ the hypotheses fail.

## (a) Second solution by reduction of order and the Wronskian [1.0 pts]

### Hint

With $y=ve^x$, the terms in $v$ cancel because $e^x$ solves the equation; what is left is a first-order separable equation for $w=v'$.

### Checkpoint

- $x v''+(x-2)v'=0$, so $w=v'=x^2e^{-x}$.
- $v=-(x^2+2x+2)e^{-x}$, hence $y_2=x^2+2x+2$ (a polynomial).
- $W(e^x,\ x^2+2x+2)=-x^2e^x\neq0$ for $x>0$.

### Solution

#### Step 1. Check of y1

$y_1=y_1'=y_1''=e^x$: $xe^x-(x+2)e^x+2e^x=(x-x-2+2)e^x=0$.

#### Step 2. Substitution

$y=ve^x$, product rule: $y'=e^x(v'+v)$, $y''=e^x(v''+2v'+v)$. Substituting:
$$xe^x(v''+2v'+v)-(x+2)e^x(v'+v)+2ve^x=e^x\big[xv''+(2x-x-2)v'+(x-x-2+2)v\big]=e^x\big[xv''+(x-2)v'\big]$$
So the homogeneous equation becomes $xv''+(x-2)v'=0$.

#### Step 3. First-order equation for w = v'

$xw'=-(x-2)w$, separable: $\dfrac{dw}{w}=\Big(-1+\dfrac2x\Big)dx$. Integrating, $\ln\lvert w\rvert=-x+2\ln x+c$, so $w=Kx^2e^{-x}$; take $K=1$.

#### Step 4. Integrate w

By parts twice ($u=x^2$, $dv=e^{-x}dx$, $du=2x\,dx$, $v=-e^{-x}$; then $u=x$, $du=dx$):
$$\int x^2e^{-x}dx=-x^2e^{-x}+2\int xe^{-x}dx=-x^2e^{-x}+2\Big(-xe^{-x}+\int e^{-x}dx\Big)=-(x^2+2x+2)e^{-x}$$
Then $y=ve^x=-(x^2+2x+2)$. Dropping the constant factor $-1$: $y_2=x^2+2x+2$. Check: $y_2'=2x+2$, $y_2''=2$: $2x-(x+2)(2x+2)+2(x^2+2x+2)=2x-(2x^2+6x+4)+2x^2+4x+4=0$.

#### Step 5. Wronskian

$$W=\begin{vmatrix}e^x&x^2+2x+2\\e^x&2x+2\end{vmatrix}=e^x(2x+2)-e^x(x^2+2x+2)=-x^2e^x$$
It never vanishes on $x>0$, so $\{y_1,y_2\}$ is a fundamental set. Abel's formula agrees: $W=C\exp\Big(-\int p\,dx\Big)=C\exp\Big(x+2\ln x\Big)=Cx^2e^x$, with $C=-1$.

## (b) General solution of the forced equation [1.0 pts]

### Hint

The same substitution gives $xv''+(x-2)v'=x^3$. Solve the first-order linear equation for $w=v'$ with the integrating factor $\mu=\exp\int(1-2/x)\,dx$.

### Checkpoint

- $w'+\Big(1-\dfrac2x\Big)w=x^2$, $\mu=\dfrac{e^x}{x^2}$, $(\mu w)'=e^x$.
- $w=x^2+Cx^2e^{-x}$, $v=\dfrac{x^3}{3}-C(x^2+2x+2)e^{-x}+D$.
- $y=C_1e^x+C_2(x^2+2x+2)+\dfrac{x^3e^x}{3}$.

### Solution

#### Step 1. Reduced equation

From Step 2 of (a), $L[ve^x]=e^x\big[xv''+(x-2)v'\big]=x^3e^x$, so $xv''+(x-2)v'=x^3$. With $w=v'$ and dividing by $x$:
$$w'+\Big(1-\frac2x\Big)w=x^2$$

#### Step 2. Integrating factor

$\mu=\exp\displaystyle\int\Big(1-\frac2x\Big)dx=\exp(x-2\ln x)=\frac{e^x}{x^2}$. Check: $\mu'=\dfrac{e^x}{x^2}-\dfrac{2e^x}{x^3}=\mu\Big(1-\dfrac2x\Big)$. Then $(\mu w)'=\mu w'+\mu'w=\mu\big[w'+(1-2/x)w\big]=\dfrac{e^x}{x^2}x^2=e^x$.

#### Step 3. Integrate twice

$\mu w=e^x+C$, so $w=x^2+Cx^2e^{-x}$. Integrating, with the antiderivative of (a) Step 4:
$$v=\frac{x^3}{3}-C(x^2+2x+2)e^{-x}+D$$
and $y=ve^x$:
$$y=De^x-C(x^2+2x+2)+\frac{x^3e^x}{3}=C_1e^x+C_2(x^2+2x+2)+\frac{x^3e^x}{3}$$

#### Step 4. Check of the particular solution

$y_p=\tfrac13x^3e^x$: $y_p'=\big(x^2+\tfrac13x^3\big)e^x$, $y_p''=\big(2x+2x^2+\tfrac13x^3\big)e^x$. Then
$$xy_p''-(x+2)y_p'+2y_p=e^x\Big[2x^2+2x^3+\tfrac13x^4-\big(x^3+\tfrac13x^4+2x^2+\tfrac23x^3\big)+\tfrac23x^3\Big]=x^3e^x$$
Variation of constants with $f=x^2e^x$ and $W=-x^2e^x$ gives $y_p-2e^x$, the same up to a homogeneous solution.

## (c) Initial conditions at the singular point x = 0 [0.5 pts]

### Hint

Evaluate the general solution and its derivative at $x=0$, or set $x=0$ directly in the equation.

### Checkpoint

- $y(0)=C_1+2C_2=y'(0)$ for every solution.
- $y(0)=1,\ y'(0)=0$: no solution. $y(0)=y'(0)=1$: infinitely many ($C_1=1-2C_2$, $C_2$ free).
- No contradiction: $p=-1-2/x$ and $q=2/x$ are not continuous at $x=0$ (equivalently $W(0)=0$).

### Solution

#### Step 1. Values at x = 0

$y=C_1e^x+C_2(x^2+2x+2)+\tfrac13x^3e^x$ gives $y(0)=C_1+2C_2$. $y'=C_1e^x+C_2(2x+2)+\big(x^2+\tfrac13x^3\big)e^x$ gives $y'(0)=C_1+2C_2$. So $y'(0)=y(0)$ always. Directly: at $x=0$ the equation reads $0\cdot y''(0)-2y'(0)+2y(0)=0$.

#### Step 2. The two initial-value problems

$y(0)=1$, $y'(0)=0$ violates $y'(0)=y(0)$: **no solution**. $y(0)=y'(0)=1$ only gives $C_1+2C_2=1$: a one-parameter family, **no uniqueness**.

#### Step 3. Picard

Picard's theorem needs the standard form $y''=f(x)-p(x)y'-q(x)y$ with coefficients continuous near $x_0$. At $x_0=0$, $p$ and $q$ blow up, so the theorem does not apply. Consistently, $W=-x^2e^x$ vanishes at $x=0$: the matrix $\begin{pmatrix}y_1(0)&y_2(0)\\y_1'(0)&y_2'(0)\end{pmatrix}=\begin{pmatrix}1&2\\1&2\end{pmatrix}$ is singular, so the constants cannot be fitted to arbitrary data.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** as $x\to\infty$ the forced response $\tfrac13x^3e^x$ dominates both $e^x$ and the polynomial. As $x\to0^+$ every solution is smooth, but only data on the line $y'(0)=y(0)$ are reachable.
- **Checks:** $y_1$, $y_2$, $y_p$ substituted back (Steps (a)4 and (b)4); Abel's formula reproduces the Wronskian; $W\neq0$ on $x>0$.
- **Common mistakes in the exam:** (1) forgetting to divide by $x$ before reading $p(x)$ for Abel's formula or variation of constants (with $f=x^2e^x$, not $x^3e^x$); (2) sign slips in $\int x^2e^{-x}dx$; (3) presenting $y_2=-(x^2+2x+2)e^{-x}$, i.e. $v$ instead of $y=ve^x$; (4) claiming uniqueness at $x_0=0$ by quoting Picard without checking continuity of $p$ and $q$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
