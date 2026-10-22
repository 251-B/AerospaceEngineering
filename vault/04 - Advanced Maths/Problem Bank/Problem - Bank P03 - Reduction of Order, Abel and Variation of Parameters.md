---
materia: Advanced Maths
tema: "Unit 3: second-order linear ODEs with variable coefficients"
bank_id: P03
title: "A variable-coefficient equation with the solution x: reduction of order to x e^x, Abel's identity against the direct Wronskian, variation of parameters for the forcing x^4 and an IVP"
category: midterm_1_problem
archetype: ode-second-order-reduction
level: standard
unit: 3
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL, MATHS_FIRSTPARTIAL_2024_SOL; not an official exercise. Verified with scripts/am_bank/p03.py"
tags:
  - problem-bank
  - midterm-1
  - reduction-of-order
  - wronskian
  - abel-identity
  - variation-of-parameters
---

# Bank P03 — Reduction of order, Abel and variation of parameters

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL and MATHS_FIRSTPARTIAL_2024_SOL. Method: Topic 3 (general theory and the Wronskian, Robinson Ch. 11; Abel's identity, Notes, p. 5 and [[Concept - Abel's Identity and Properties of the Wronskian]]; reduction of order, Robinson Ch. 17 and Notes, p. 7; variation of constants, Robinson Ch. 18, Eq. 18.8 and Notes, p. 8). Every result was checked with SymPy (scripts/am_bank/p03.py).

## Statement

Consider, for $x>0$, the equation

$$x^2y''-x(x+2)\,y'+(x+2)\,y=g_0(x).$$

The homogeneous equation ($g_0=0$) has a solution that is a polynomial of degree one. In parts (c) and (d) the right-hand side is $g_0(x)=x^4$, and the initial data of (d) are

$$y(1)=\frac12,\qquad y'(1)=-\frac12.$$

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $y(x)$, independent variable $x$ on the interval $(0,\infty)$.
- Operator: second order, **linear**, with **variable** coefficients; homogeneous in (a) and (b), inhomogeneous in (c) and (d).
- The leading coefficient $x^2$ vanishes at $x=0$: $x=0$ is a singular point, so all statements are made on $x>0$, where the coefficients of the standard form are continuous and the existence and uniqueness theorem holds (Topic 3, [[Concept - Existence and Uniqueness Theorem for Second-Order ODEs]]).

#### Phase 2. Canonical formulation

Dividing by $x^2\neq0$, with $\frac{x+2}{x^2}=\frac1x+\frac2{x^2}$, the standard form $y''+p(x)y'+q(x)y=g(x)$ is

$$y''-\Big(1+\frac2x\Big)y'+\Big(\frac1x+\frac2{x^2}\Big)y=\frac{g_0(x)}{x^2},\qquad p(x)=-\Big(1+\frac2x\Big),\quad g(x)=x^2\ \text{for}\ g_0=x^4.$$

## (a) First solution and reduction of order [1.5 pts]

Find the polynomial solution $y_1$ of degree one and, with $y=v\,y_1$, a second solution $y_2$ linearly independent of $y_1$.

### Hint

Try $y=\alpha x+\beta$. For $y=v\,x$, the terms in $v$ without derivatives must cancel; then $w=v'$ satisfies a first-order equation.

### Checkpoint

- $y_1=x$.
- $y=v\,x$ gives $x^3(v''-v')=0$, so $v'=Ce^x$ and $y_2=x\,e^x$.
- General homogeneous solution $y_h=c_1x+c_2\,x\,e^x$.

### Solution

#### Step 1. Polynomial solution

With $y=\alpha x+\beta$: $y'=\alpha$, $y''=0$, and

$$-x(x+2)\alpha+(x+2)(\alpha x+\beta)=(x+2)\big(-\alpha x+\alpha x+\beta\big)=\beta\,(x+2).$$

This vanishes for all $x$ only if $\beta=0$. So $y_1=x$ (taking $\alpha=1$).

#### Step 2. Substitution y = v x

By the product rule, $y=vx$ gives $y'=v'x+v$ and $y''=v''x+v'+v'=v''x+2v'$. Substituting:

$$x^2\big(xv''+2v'\big)-x(x+2)\big(xv'+v\big)+(x+2)\,xv.$$

Expanding term by term: $x^3v''+2x^2v'-(x^3+2x^2)v'-(x^2+2x)v+(x^2+2x)v=x^3v''-x^3v'$. The terms in $v$ cancel because $y_1$ solves the equation, as they must. Hence

$$x^3\big(v''-v'\big)=0\iff v''=v'\qquad(x>0).$$

#### Step 3. First-order equation for w = v'

$w'=w$ is separable: $\frac{dw}{w}=dx$, $\ln\lvert w\rvert=x+C_1$, $w=Ce^x$. Integrating once more, $v=\int Ce^x\,dx=Ce^x+D$. Then $y=vx=C\,x\,e^x+D\,x$. The part $Dx$ is the old solution; the new one is

$$y_2=x\,e^x.$$

Check: $y_2'=(1+x)e^x$, $y_2''=(2+x)e^x$; $x^2(2+x)-x(x+2)(1+x)+(x+2)x=x(x+2)\big[x-(1+x)+1\big]=0$, times $e^x$.

## (b) Wronskian by Abel's identity and directly [1.0 pts]

Compute the Wronskian of $\{y_1,y_2\}$ from Abel's identity and from the determinant, and conclude that they form a fundamental set on $x>0$.

### Hint

Abel: $W'=-p\,W$, so $W=C\exp\!\big(-\int p\,dx\big)$, with $p$ read from the standard form.

### Checkpoint

- Abel: $W=C\,x^2e^x$.
- Determinant: $W=x(1+x)e^x-x\,e^x=x^2e^x$, so $C=1$.
- $W\neq0$ on $(0,\infty)$: fundamental set; $W(0)=0$ only at the singular point.

### Solution

#### Step 1. Abel's identity

With $p=-(1+\frac2x)$, $W'=-pW=\big(1+\frac2x\big)W$. Separating, $\frac{dW}{W}=\big(1+\frac2x\big)dx$, and with the antiderivative $x+2\ln x$ ($x>0$):

$$\ln\lvert W\rvert=x+2\ln x+C_1\ \Longrightarrow\ W(x)=C\,x^2e^x.$$

#### Step 2. Direct determinant

$$W=\det\begin{pmatrix}y_1&y_2\\y_1'&y_2'\end{pmatrix}=\det\begin{pmatrix}x&x\,e^x\\1&(1+x)e^x\end{pmatrix}=x(1+x)e^x-x\,e^x\cdot1=x^2e^x.$$

The two results agree with $C=1$.

#### Step 3. Conclusion

$x^2e^x>0$ for $x>0$, so $y_1$, $y_2$ are linearly independent there and $y_h=c_1x+c_2xe^x$ is the general solution of the homogeneous equation (Robinson Ch. 11). The dichotomy "either $W\equiv0$ or $W$ never vanishes" applies on intervals where $p$ is continuous; $W(0)=0$ happens at the singular point $x=0$ and is no contradiction.

## (c) Variation of parameters for the forcing x^4 [1.5 pts]

With $g_0(x)=x^4$, find a particular solution by variation of parameters and write the general solution.

### Hint

First divide by $x^2$: the formula uses $g=x^2$, not $x^4$. One of the integrals needs integration by parts.

### Checkpoint

- $\displaystyle\int\frac{y_2\,g}{W}dx=\int x\,dx=\frac{x^2}2$, $\ \displaystyle\int\frac{y_1\,g}{W}dx=\int x\,e^{-x}dx=-(x+1)e^{-x}$.
- $y_p=-\dfrac{x^3}2-x^2$ (after dropping the multiple $-x$ of $y_1$).
- $y=c_1x+c_2xe^x-\dfrac{x^3}2-x^2$.

### Solution

#### Step 1. Formula

For $y''+py'+qy=g$ with fundamental set $\{y_1,y_2\}$ (Robinson Eq. 18.8, Notes, p. 8):

$$y_p=-y_1\int\frac{y_2\,g}{W}\,dx+y_2\int\frac{y_1\,g}{W}\,dx,\qquad g=\frac{x^4}{x^2}=x^2.$$

#### Step 2. The two integrands

$$\frac{y_2\,g}{W}=\frac{x\,e^x\cdot x^2}{x^2e^x}=x,\qquad \frac{y_1\,g}{W}=\frac{x\cdot x^2}{x^2e^x}=x\,e^{-x}.$$

#### Step 3. The integrals

$\int x\,dx=\frac{x^2}2$. For the second, integrate by parts with $u=x$, $dv=e^{-x}dx$, so $du=dx$, $v=-e^{-x}$:

$$\int x\,e^{-x}dx=-x\,e^{-x}-\int(-e^{-x})\,dx=-x\,e^{-x}-e^{-x}=-(x+1)e^{-x}.$$

(Integration constants are omitted: they only add multiples of $y_1$ and $y_2$.)

#### Step 4. Particular and general solution

$$y_p=-x\cdot\frac{x^2}2+x\,e^x\cdot\big(-(x+1)e^{-x}\big)=-\frac{x^3}2-x^2-x.$$

The term $-x$ is a multiple of $y_1$ and can be absorbed: $y_p=-\dfrac{x^3}2-x^2$. Check, with $y_p'=-\frac32x^2-2x$, $y_p''=-3x-2$:

$$x^2(-3x-2)-x(x+2)\Big(-\frac32x^2-2x\Big)+(x+2)\Big(-\frac{x^3}2-x^2\Big)$$

$$=\big(-3x^3-2x^2\big)+\Big(\frac32x^4+5x^3+4x^2\Big)+\Big(-\frac12x^4-2x^3-2x^2\Big)=x^4.\ \checkmark$$

The general solution is $y=c_1x+c_2\,x\,e^x-\dfrac{x^3}2-x^2$.

## (d) Initial value problem [1.0 pts]

Solve the IVP with $y(1)=\frac12$, $y'(1)=-\frac12$ and give the largest interval on which the solution is guaranteed to exist and be unique.

### Hint

$y'=c_1+c_2(1+x)e^x-\frac32x^2-2x$. Subtract the two conditions to isolate $c_2$.

### Checkpoint

- $c_1+e\,c_2=2$ and $c_1+2e\,c_2=3$, so $c_2=e^{-1}$, $c_1=1$.
- $y(x)=x+x\,e^{x-1}-\dfrac{x^3}2-x^2$ on $(0,\infty)$.

### Solution

#### Step 1. Conditions

$y(1)=c_1+c_2e-\frac12-1=\frac12\Rightarrow c_1+e\,c_2=2$. $\ y'(1)=c_1+2e\,c_2-\frac32-2=-\frac12\Rightarrow c_1+2e\,c_2=3$.

#### Step 2. Constants

Subtracting the first equation from the second: $e\,c_2=1$, $c_2=e^{-1}$; then $c_1=2-1=1$. The system is uniquely solvable because its matrix is $\begin{pmatrix}y_1(1)&y_2(1)\\y_1'(1)&y_2'(1)\end{pmatrix}=\begin{pmatrix}1&e\\1&2e\end{pmatrix}$, whose determinant $2e-e=e$ is exactly $W(1)\neq0$.

$$y(x)=x+x\,e^{x-1}-\frac{x^3}2-x^2.$$

#### Step 3. Interval

$p$, $q$ and $g$ of the standard form are continuous on $(0,\infty)$, which contains $x_0=1$; the existence and uniqueness theorem gives a unique solution on the whole of $(0,\infty)$. Nothing is guaranteed at or across $x=0$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** as $x\to\infty$ the term $x\,e^{x-1}$ dominates and $y\to+\infty$; as $x\to0^+$, $y\to0$ and $y'(0^+)=1+e^{-1}$ (finite, though the theorem does not cover $x=0$).
- **Checks:** $y_1$, $y_2$ and $y_p$ were substituted back; Abel's $W$ and the determinant agree; $y(1)=1+1-\frac12-1=\frac12$ and $y'(1)=1+2-\frac32-2=-\frac12$.
- **Common mistakes in the exam:** (1) applying variation of parameters to $x^4$ without dividing by the leading coefficient $x^2$; (2) taking $p=-(x+2)$ instead of $-(x+2)/x$ in Abel's identity; (3) a sign slip in $\int xe^{-x}dx$; (4) keeping $-x$ in $y_p$ and still reporting $c_1=1$: with $y_p=-\frac{x^3}2-x^2-x$ the IVP gives $c_1=2$, and the solution $y(x)$ is the same.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
