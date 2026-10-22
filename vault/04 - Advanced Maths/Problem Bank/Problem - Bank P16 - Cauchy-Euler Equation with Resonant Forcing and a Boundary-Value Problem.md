---
materia: Advanced Maths
tema: "Unit 3: Cauchy-Euler equations and boundary-value problems"
bank_id: P16
title: "x^2 y'' - x y' + 2y = x sin(ln x): reduction to constant coefficients by x = e^z, a resonant particular solution x ln x cos(ln x), and a boundary-value problem on [1, b] whose existence and uniqueness depend on b"
category: final_problem
archetype: ode-second-order-undetermined-params
level: trap
unit: 3
difficulty: 3
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2020_ORD, MATHS_FINALEXAM_2021_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p16.py"
tags:
  - problem-bank
  - final-exam
  - cauchy-euler-equation
  - undetermined-coefficients
  - resonance
  - boundary-value-problem
---

# Bank P16 — Cauchy-Euler equation with resonant forcing and a boundary-value problem

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the final exams (MATHS_FINALEXAM_2020_ORD, MATHS_FINALEXAM_2021_ORD_SOL). Method: Euler equation reduced by $x=e^z$ and the educated guess for the particular solution (Notes.pdf, pp. 5-6), undetermined coefficients with trigonometric forcing and the general rule for resonance (Robinson Sec. 14.4 and 14.5), and the eigenvalue reasoning of two-point boundary-value problems (Haberman Sec. 2.3, unit 5 text). Every result was checked with SymPy (scripts/am_bank/p16.py).

## Statement

Consider, for $x\ge1$,
$$x^2y''-x\,y'+2y=x\sin(\ln x).$$

(a) With the change of variable $x=e^z$, $Y(z)=y(e^z)$, write the chain rule for $y'$ and $y''$ explicitly and obtain a constant-coefficient equation for $Y$. Find the general solution of the homogeneous equation in terms of $x$.

(b) Find a particular solution. Explain why the natural guess $x\big(A\cos\ln x+B\sin\ln x\big)$ fails.

(c) Consider the boundary-value problem formed by the equation and $y(1)=0$, $y(b)=0$, with $b>1$.
- For which $b$ does it have exactly one solution? Write it, and simplify it for $b=e^{\pi/2}$.
- Show that for $b=e^{n\pi}$ ($n=1,2,\dots$) it has no solution.
- For $b=e^{\pi}$, replace $y(b)=0$ by $y(e^{\pi})=\beta$. For which $\beta$ are there solutions, and how many?

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $y(x)$ on $[1,b]$; $x>0$ so $\ln x$ is defined and the leading coefficient $x^2$ does not vanish.
- Operator: linear, second order, variable coefficients of Cauchy-Euler type ($x^k y^{(k)}$), non-homogeneous with forcing $x\sin(\ln x)$.
- Two conditions at **different** points: a boundary-value problem, for which Picard's theorem gives no existence or uniqueness guarantee.

#### Phase 2. Canonical formulation

Standard form: $y''-\dfrac1x\,y'+\dfrac{2}{x^2}\,y=\dfrac{\sin(\ln x)}{x}$. After $x=e^z$ the problem becomes a constant-coefficient equation on $0\le z\le\ln b$ with $Y(0)=0$, $Y(\ln b)=0$.

## (a) Change of variable and homogeneous solution [0.75 pts]

### Hint

$z=\ln x$, so $\dfrac{dz}{dx}=\dfrac1x$. Differentiate $y'=\dfrac1xY'(z)$ again with the product rule and the chain rule.

### Checkpoint

- $y'=\dfrac1x\dfrac{dY}{dz}$, $\ y''=\dfrac1{x^2}\Big(\dfrac{d^2Y}{dz^2}-\dfrac{dY}{dz}\Big)$.
- $Y''-2Y'+2Y=e^z\sin z$; characteristic roots $r=1\pm i$.
- $y_h=x\big(C_1\cos(\ln x)+C_2\sin(\ln x)\big)$.

### Solution

#### Step 1. First derivative

$y(x)=Y(z(x))$ with $z=\ln x$. Chain rule: $y'=\dfrac{dY}{dz}\dfrac{dz}{dx}=\dfrac1x\,Y'(z)$.

#### Step 2. Second derivative

Product rule on $\dfrac1x\cdot Y'(z(x))$, and chain rule on the second factor, $\dfrac{d}{dx}Y'(z)=Y''(z)\dfrac1x$:
$$y''=-\frac1{x^2}Y'+\frac1x\cdot\frac1xY''=\frac{1}{x^2}\big(Y''-Y'\big)$$

#### Step 3. Transformed equation

$x^2y''=Y''-Y'$, $\ xy'=Y'$, $\ x=e^z$, $\ \sin(\ln x)=\sin z$:
$$Y''-Y'-Y'+2Y=e^z\sin z\ \Longrightarrow\ Y''-2Y'+2Y=e^z\sin z$$

#### Step 4. Homogeneous solution

Characteristic polynomial $r^2-2r+2=0$, $r=\dfrac{2\pm\sqrt{4-8}}{2}=1\pm i$. So $Y_h=e^z(C_1\cos z+C_2\sin z)$ and, back with $e^z=x$, $z=\ln x$:
$$y_h=x\big(C_1\cos(\ln x)+C_2\sin(\ln x)\big)$$

## (b) Resonant particular solution [0.75 pts]

### Hint

$e^z\sin z$ is built from $e^{(1+i)z}$, and $1+i$ is a root of the characteristic polynomial. Multiply the guess by $z$. The substitution $Y=e^zw$ shortens the algebra.

### Checkpoint

- The guess $e^z(A\cos z+B\sin z)$ is a homogeneous solution: substituting gives $0=e^z\sin z$, impossible.
- Corrected guess $Y_p=ze^z(A\cos z+B\sin z)$; $A=-\tfrac12$, $B=0$.
- $y_p=-\tfrac12\,x\ln x\cos(\ln x)$; general solution $y=x\big(C_1\cos\ln x+C_2\sin\ln x\big)-\tfrac12x\ln x\cos\ln x$.

### Solution

#### Step 1. Why the natural guess fails

$\alpha+i\beta=1+i$ is a simple root of $r^2-2r+2$; $e^z\cos z$ and $e^z\sin z$ solve the homogeneous equation, so any $e^z(A\cos z+B\sin z)$ is mapped to $0$ and cannot produce $e^z\sin z$. The general rule (Robinson Sec. 14.5; Notes.pdf, the second case of the guess) multiplies the guess by $z$ once (simple root).

#### Step 2. Shift by e^z

Write $Y=e^zw(z)$. Product rule: $Y'=e^z(w'+w)$, $Y''=e^z(w''+2w'+w)$. Then
$$Y''-2Y'+2Y=e^z\big[w''+2w'+w-2w'-2w+2w\big]=e^z\big(w''+w\big)$$
so the equation becomes $w''+w=\sin z$, and the guess is $w=z(A\cos z+B\sin z)$.

#### Step 3. Coefficients

$w'=A\cos z+B\sin z+z(-A\sin z+B\cos z)$ and
$$w''=2(-A\sin z+B\cos z)-z(A\cos z+B\sin z)$$
Hence $w''+w=-2A\sin z+2B\cos z=\sin z$: $-2A=1$, $2B=0$, so $A=-\tfrac12$, $B=0$.

#### Step 4. Back to x

$Y_p=-\tfrac12ze^z\cos z$, and with $z=\ln x$, $e^z=x$:
$$y_p=-\frac12\,x\ln x\,\cos(\ln x)$$
the $x^r\ln x$ structure typical of resonance in Euler equations (here $r=1\pm i$). General solution:
$$y=x\big(C_1\cos(\ln x)+C_2\sin(\ln x)\big)-\frac12x\ln x\cos(\ln x)$$

## (c) Boundary-value problem on [1, b] [1.0 pts]

### Hint

$\ln1=0$ fixes $C_1$. The second condition is one linear equation for $C_2$ whose coefficient is $b\sin(\ln b)$: discuss whether it vanishes.

### Checkpoint

- $y(1)=0\Rightarrow C_1=0$. $y(b)=0\Rightarrow C_2\sin(\ln b)=\tfrac12\ln b\cos(\ln b)$.
- Unique solution iff $b\ne e^{n\pi}$: $\ y=\dfrac x2\Big(\ln b\cot(\ln b)\sin(\ln x)-\ln x\cos(\ln x)\Big)$. For $b=e^{\pi/2}$: $y=y_p=-\tfrac12x\ln x\cos(\ln x)$.
- $b=e^{n\pi}$: the condition reads $0=(-1)^{n+1}\dfrac{n\pi}{2}e^{n\pi}\neq0$: no solution.
- $y(e^\pi)=\beta$: solvable iff $\beta=\dfrac{\pi e^{\pi}}{2}\approx36.35$, and then there are infinitely many solutions $y=y_p+C_2x\sin(\ln x)$.

### Solution

#### Step 1. Condition at x = 1

$\ln1=0$, $\cos0=1$, $\sin0=0$: $y(1)=C_1$. So $C_1=0$ and $y=C_2x\sin(\ln x)-\tfrac12x\ln x\cos(\ln x)$.

#### Step 2. Condition at x = b

$y(b)=b\Big(C_2\sin(\ln b)-\tfrac12\ln b\cos(\ln b)\Big)=0$, and $b>0$, so
$$C_2\sin(\ln b)=\tfrac12\ln b\cos(\ln b)$$

#### Step 3. Unique case

If $\sin(\ln b)\neq0$, i.e. $b\neq e^{n\pi}$, then $C_2=\tfrac12\ln b\cot(\ln b)$ and
$$y=\frac x2\Big(\ln b\,\cot(\ln b)\sin(\ln x)-\ln x\cos(\ln x)\Big)$$
For $b=e^{\pi/2}$: $\cot(\pi/2)=0$, so $C_2=0$ and the solution is $y_p$ itself, which already vanishes at $x=1$ and at $x=e^{\pi/2}$ (where $\cos(\ln x)=0$).

#### Step 4. b = e^{n pi}: no solution

$\sin(n\pi)=0$ and $\cos(n\pi)=(-1)^n$, so Step 2 reads $0=\tfrac12\,n\pi(-1)^n$, impossible. Equivalently $y(e^{n\pi})=(-1)^{n+1}\tfrac{n\pi}{2}e^{n\pi}$ whatever $C_2$ is. The reason: $x\sin(\ln x)$ is a non-trivial solution of the **homogeneous** boundary-value problem (in $z$, $\sin z$ vanishes at $z=0$ and $z=n\pi$, exactly as the eigenfunctions of Haberman Sec. 2.3), and the forcing is not orthogonal to it. Fredholm alternative (extension): the non-homogeneous problem is solvable if and only if the forcing, written for the self-adjoint form of the operator, is orthogonal to every solution of the homogeneous problem. Dividing the equation by $x^3$ gives the self-adjoint form $\Big(\dfrac{y'}{x}\Big)'+\dfrac{2}{x^3}y=\dfrac{\sin(\ln x)}{x^2}$, and with $z=\ln x$, $dz=dx/x$:
$$\int_1^{e^{n\pi}}\frac{\sin(\ln x)}{x^2}\,x\sin(\ln x)\,dx=\int_0^{n\pi}\sin^2z\,dz=\Big[\frac z2-\frac{\sin2z}{4}\Big]_0^{n\pi}=\frac{n\pi}{2}\neq0$$

#### Step 5. Changed data at b = e^pi

With $y(e^\pi)=\beta$: $e^\pi\big(C_2\cdot0-\tfrac12\pi(-1)\big)=\beta$, i.e. $\beta=\dfrac{\pi e^\pi}{2}\approx36.35$. If $\beta$ has this value, $C_2$ is free: infinitely many solutions $y=y_p+C_2x\sin(\ln x)$. For any other $\beta$, none.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $b\to e^{n\pi}$ from either side: $\cot(\ln b)\to\pm\infty$, so the unique solution blows up, the signature of an approaching eigenvalue. $b\to1^+$: $\ln b\cot(\ln b)\to1$ and $y\to\tfrac x2\big(\sin(\ln x)-\ln x\cos(\ln x)\big)$ restricted to a shrinking interval, which tends to $0$.
- **Checks:** $y_p$ substituted back in the original variable: the script verifies $x^2y_p''-xy_p'+2y_p=x\sin(\ln x)$; the boundary values $y(1)=0$, $y(b)=0$ hold identically in $b$; the solution of Step 3 is the case $b=e$ with $C_2=\tfrac12\cot1\approx0.32105$.
- **Common mistakes in the exam:** (1) writing $y''=\dfrac1{x^2}Y''$, forgetting the $-Y'$ term produced by the product rule; (2) using the non-resonant guess and getting the contradiction $0=e^z\sin z$ without multiplying by $z$; (3) concluding "unique by Picard" for a boundary-value problem; (4) assuming that a boundary-value problem with a zero-determinant system always has infinitely many solutions: it has none unless the data satisfy the solvability condition.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
