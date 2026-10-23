---
materia: Advanced Maths
tema: "Unit 3: constant-coefficient equations, undetermined coefficients and resonance"
bank_id: P04
title: "Inverse problem: rebuild y'' + a y' + b y = f from one homogeneous solution and one particular solution, then the resonant forcing e^{-x} sin 2x, an IVP and which forcings need the modified guess"
category: midterm_1_problem
archetype: ode-second-order-undetermined-params
level: trap
unit: 3
difficulty: 3
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the format and topics of MATHS_FIRSTPARTIAL_2021_G45_SOL (problem 2) and MATHS_FIRSTPARTIAL_2020_G47_SOL (problem 2); the inverse formulation (reconstructing the equation) is original to the bank; not an official exercise. Verified with scripts/am_bank/p04.py"
tags:
  - problem-bank
  - midterm-1
  - undetermined-coefficients
  - characteristic-equation
  - resonance
  - inverse-problem
  - damped-oscillator
---

# Bank P04 — Reconstructing an equation from its solutions and resonant forcing

> [!info] Practice item, not an official exercise
> Written for the bank in the format and topics of MATHS_FIRSTPARTIAL_2021_G45_SOL (problem 2) and MATHS_FIRSTPARTIAL_2020_G47_SOL (problem 2); the inverse formulation is original to the bank. Method: Topic 3 (characteristic equation and complex roots, Robinson Ch. 12 and [[Concept - Homogeneous Equations with Constant Coefficients and the Characteristic Equation]]; undetermined coefficients, Robinson 14.5 and 14.6; the modified guess for a root of the characteristic polynomial, Robinson 14.5; the oscillator resonance of Robinson Ch. 15 is the special case $\ddot x+\omega^2x=a\cos\alpha t$; steady-state amplitude as in [[Problem - Ch3-II-P4 Damped Forced Oscillator Amplitude and Phase of the Steady State]]). Every result was checked with SymPy (scripts/am_bank/p04.py).

## Statement

The real constants $a$, $b$ of the equation

$$y''+a\,y'+b\,y=f(x)$$

are unknown. Two facts are known about it:

- the function $y=e^{-x}\cos2x$ solves the homogeneous equation ($f=0$);
- when the right-hand side is $f(x)=k\,x$, for a certain constant $k$, the polynomial $y=5x-2$ is a solution.

Afterwards the equation is driven by $f(x)=8\,e^{-x}\sin2x$, with initial data $y(0)=1$, $y'(0)=-3$. Finally, consider forcings of the form $f(x)=e^{\alpha x}\cos\omega x$ or $e^{\alpha x}\sin\omega x$ with real $\alpha$ and $\omega\ge0$, and in particular the purely oscillatory forcing $f(x)=\cos\omega x$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns: first the parameters $a$, $b$, $k$ (inverse problem), then the function $y(x)$, $x\in\mathbb R$.
- Operator: second order, linear, constant coefficients, $L[y]=y''+ay'+by$. Coefficients and forcings are continuous on $\mathbb R$, so every IVP has a unique solution on all of $\mathbb R$.
- Superposition: $y=y_h+y_p$, with $y_h$ from the characteristic equation $r^2+ar+b=0$ and $y_p$ from undetermined coefficients.

#### Phase 2. Canonical formulation

The equation is already in standard form. Writing $y=e^{-x}u$ (an exponential shift, **extension**: not in the course, it only organises the computation of (b)) turns $L$ into an operator on $u$ that will expose the resonance.

## (a) Reconstruction of the equation [1.5 pts]

Find $a$, $b$ and $k$, and write the general solution of the homogeneous equation.

### Hint

Substitute $e^{-x}\cos2x$ and use that $\cos2x$ and $\sin2x$ are linearly independent. Alternatively: real coefficients force the conjugate root as well.

### Checkpoint

- $a=2$, $b=5$; characteristic roots $r=-1\pm2i$.
- $k=25$; $y_p=5x-2$ is recovered by the guess $Ax+B$.
- $y_h=e^{-x}\big(c_1\cos2x+c_2\sin2x\big)$.

### Solution

#### Step 1. Derivatives of the given solution

Product and chain rule on $y=e^{-x}\cos2x$:

$$y'=-e^{-x}\cos2x-2e^{-x}\sin2x=e^{-x}\big(-\cos2x-2\sin2x\big),$$

$$y''=-e^{-x}\big(-\cos2x-2\sin2x\big)+e^{-x}\big(2\sin2x-4\cos2x\big)=e^{-x}\big(-3\cos2x+4\sin2x\big).$$

#### Step 2. Conditions on a and b

$$L[y]=e^{-x}\Big[\big(-3-a+b\big)\cos2x+\big(4-2a\big)\sin2x\Big]=0\quad\forall x.$$

$e^{-x}\neq0$ and $\cos2x$, $\sin2x$ are linearly independent, so both brackets vanish: $4-2a=0\Rightarrow a=2$, and $-3-2+b=0\Rightarrow b=5$.

Cross-check: $e^{-x}\cos2x=\operatorname{Re}e^{(-1+2i)x}$ requires the root $r=-1+2i$; real coefficients give also $-1-2i$, so $r^2+ar+b=(r+1-2i)(r+1+2i)=(r+1)^2+4=r^2+2r+5$.

#### Step 3. The constant k

$y=5x-2$: $y'=5$, $y''=0$, so $L[y]=0+2\cdot5+5(5x-2)=25x$. Hence $k=25$. Undetermined coefficients give the same: with $y_p=Ax+B$, $L[y_p]=2A+5Ax+5B=25x$, so $5A=25$, $A=5$, and $2A+5B=0$, $B=-2$. The second fact is consistent with $a=2$, $b=5$ (it imposes $5a=2b$ through the constant term, which they satisfy).

#### Step 4. Homogeneous solution

$r^2+2r+5=0$: $r=\dfrac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$ (Robinson Ch. 12), so

$$y_h=e^{-x}\big(c_1\cos2x+c_2\sin2x\big).$$

## (b) Resonant forcing and the modified guess [1.5 pts]

For $f(x)=8\,e^{-x}\sin2x$ explain why the usual guess fails and find a particular solution.

### Hint

$-1+2i$ is a root of the characteristic polynomial. With $y=e^{-x}u$ the operator becomes $u''+4u$.

### Checkpoint

- $e^{-x}(A\cos2x+B\sin2x)$ is a homogeneous solution: $L$ annihilates it.
- Modified guess $y_p=x\,e^{-x}(A\cos2x+B\sin2x)$; $L[y_p]=e^{-x}\big(4B\cos2x-4A\sin2x\big)$.
- $A=-2$, $B=0$: $y_p=-2x\,e^{-x}\cos2x$.

### Solution

#### Step 1. Why the usual guess fails

The forcing is $\operatorname{Im}\big(8e^{(-1+2i)x}\big)$ and $-1+2i$ is a simple root of $r^2+2r+5$. The guess $e^{-x}(A\cos2x+B\sin2x)$ lies in $y_h$, so $L$ of it is $0$ for every $A$, $B$, never $8e^{-x}\sin2x$. The rule (Robinson 14.5) multiplies the guess by $x$ (once, because the root is simple).

#### Step 2. Exponential shift

Let $y=e^{-x}u$. By the product rule, $y'=e^{-x}(u'-u)$ and $y''=-e^{-x}(u'-u)+e^{-x}(u''-u')=e^{-x}(u''-2u'+u)$. Then

$$L[y]=e^{-x}\Big[(u''-2u'+u)+2(u'-u)+5u\Big]=e^{-x}\big(u''+4u\big).$$

So $L[y]=8e^{-x}\sin2x$ becomes $u''+4u=8\sin2x$: an undamped oscillator forced exactly at its natural frequency $2$.

#### Step 3. Coefficients

With $u=x(A\cos2x+B\sin2x)$:

$$u'=(A\cos2x+B\sin2x)+x(-2A\sin2x+2B\cos2x),$$

$$u''=2(-2A\sin2x+2B\cos2x)+x(-4A\cos2x-4B\sin2x).$$

The terms with $x$ cancel against $4u$: $x(-4A\cos2x-4B\sin2x)+4x(A\cos2x+B\sin2x)=0$, so $u''+4u=4B\cos2x-4A\sin2x$. Matching with $8\sin2x$: $4B=0$ and $-4A=8$, so $A=-2$, $B=0$:

$$y_p=-2x\,e^{-x}\cos2x.$$

## (c) Initial value problem [1.0 pts]

Solve the IVP with $f(x)=8e^{-x}\sin2x$, $y(0)=1$, $y'(0)=-3$, and describe its behaviour as $x\to\infty$.

### Hint

At $x=0$ the derivative of $-2xe^{-x}\cos2x$ is $-2$.

### Checkpoint

- $y'(0)=-c_1+2c_2-2$; $c_1=1$, $c_2=0$.
- $y(x)=(1-2x)\,e^{-x}\cos2x\to0$ as $x\to\infty$.

### Solution

#### Step 1. General solution and its derivative

$y=e^{-x}(c_1\cos2x+c_2\sin2x)-2xe^{-x}\cos2x$. Differentiating with the product rule and evaluating at $x=0$ ($\cos0=1$, $\sin0=0$):

$$\frac{d}{dx}\Big[e^{-x}(c_1\cos2x+c_2\sin2x)\Big]_{x=0}=-c_1+2c_2,\qquad \frac{d}{dx}\Big[-2xe^{-x}\cos2x\Big]_{x=0}=-2e^{0}\cos0=-2.$$

#### Step 2. Constants

$y(0)=c_1=1$; $y'(0)=-c_1+2c_2-2=-3\Rightarrow2c_2=0$, $c_2=0$:

$$y(x)=(1-2x)\,e^{-x}\cos2x.$$

#### Step 3. Long-time behaviour

$\lvert y\rvert\le\lvert1-2x\rvert e^{-x}\to0$, because $e^{-x}$ beats any polynomial. Here "resonance" does not mean unbounded growth: the factor $x$ only slows the decay, since the damping ($a=2>0$) sets the envelope $e^{-x}$.

## (d) Which forcings need the modified guess [1.0 pts]

For $f=e^{\alpha x}\cos\omega x$ or $e^{\alpha x}\sin\omega x$, when is the modified guess needed? For $f=\cos\omega x$, find the amplitude of the particular solution as a function of $\omega$ and the frequency that maximises it.

### Hint

The guess must be modified exactly when $\alpha+i\omega$ is a root of $r^2+2r+5$. For $\cos\omega x$ use $y_p=A\cos\omega x+B\sin\omega x$ and $y_p''=-\omega^2y_p$.

### Checkpoint

- Modified guess only for $\alpha=-1$, $\omega=2$. Never for $\cos\omega x$ ($\alpha=0$), for polynomials or for real exponentials.
- $A=\dfrac{5-\omega^2}{D}$, $B=\dfrac{2\omega}{D}$, $D=(5-\omega^2)^2+4\omega^2=(\omega^2-3)^2+16$; amplitude $R(\omega)=\dfrac1{\sqrt D}$.
- Maximum at $\omega=\sqrt3$, with $R_{\max}=\dfrac14$.

### Solution

#### Step 1. The rule

The guess $e^{\alpha x}(A\cos\omega x+B\sin\omega x)$ fails only when it solves the homogeneous equation, i.e. when $\alpha+i\omega\in\{-1+2i,-1-2i\}$: $\alpha=-1$ and $\omega=2$. For a polynomial or $e^{\alpha x}$ ($\omega=0$) the guess would need a real root, and there is none. For $\cos\omega x$ ($\alpha=0$) the real part $0$ never equals $-1$: **no frequency** of a purely oscillatory forcing needs the modified guess.

#### Step 2. Coefficients for cos(omega x)

$y_p'=-A\omega\sin\omega x+B\omega\cos\omega x$, $y_p''=-\omega^2y_p$. Then

$$L[y_p]=\big[(5-\omega^2)A+2\omega B\big]\cos\omega x+\big[(5-\omega^2)B-2\omega A\big]\sin\omega x=\cos\omega x.$$

From the second bracket $B=\frac{2\omega}{5-\omega^2}A$ (for $\omega^2\neq5$); substituting into the first, $A\,\frac{(5-\omega^2)^2+4\omega^2}{5-\omega^2}=1$. Hence $A=\frac{5-\omega^2}{D}$, $B=\frac{2\omega}{D}$ with $D=(5-\omega^2)^2+4\omega^2$ (the same formulas hold at $\omega^2=5$, solving directly).

#### Step 3. Amplitude and its maximum

$R=\sqrt{A^2+B^2}=\dfrac{\sqrt{(5-\omega^2)^2+4\omega^2}}{D}=\dfrac1{\sqrt D}$. Expanding, $D=\omega^4-10\omega^2+25+4\omega^2=\omega^4-6\omega^2+25=(\omega^2-3)^2+16\ge16$. $D$ is smallest, and $R$ largest, at $\omega^2=3$:

$$\omega=\sqrt3,\qquad R_{\max}=\frac1{\sqrt{16}}=\frac14.$$

This "practical resonance" is a finite peak, not a failure of the guess: it is the damped counterpart of the undamped resonance, and it sits below the frequency $2$ of the free oscillation.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** as $x\to\infty$ every solution of the homogeneous equation decays like $e^{-x}$, so the long-time response to $\cos\omega x$ is $y_p$ alone; $R(0)=\frac15$ (static response $1/b$) and $R(\omega)\sim\omega^{-2}$ as $\omega\to\infty$.
- **Checks:** $L[e^{-x}\cos2x]=0$, $L[5x-2]=25x$, $L[-2xe^{-x}\cos2x]=8e^{-x}\sin2x$ and the IVP were verified by substitution. With zero damping and forcing at the natural frequency (for example $y''+4y=8\sin2x$) the factor $x$ would grow without bound (true resonance); here $a=2$ gives the envelope $e^{-x}$, so $xe^{-x}\to0$.
- **Common mistakes in the exam:** (1) deducing only $b$ from the homogeneous solution and forgetting that the $\sin2x$ coefficient fixes $a$; (2) trying $e^{-x}(A\cos2x+B\sin2x)$ for the resonant forcing and getting $0=8$; (3) calling $\omega=2$ or $\omega=\sqrt3$ resonant for $\cos\omega x$: the guess never needs modifying there; (4) losing the term $-2$ from $\frac{d}{dx}(-2xe^{-x}\cos2x)$ at $x=0$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
