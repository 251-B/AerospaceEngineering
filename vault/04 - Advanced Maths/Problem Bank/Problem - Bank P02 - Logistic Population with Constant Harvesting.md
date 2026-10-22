---
materia: Advanced Maths
tema: "Unit 2: autonomous first-order ODEs, phase lines and separable equations"
bank_id: P02
title: "Logistic population with constant harvesting: equilibria against the harvest rate, the critical rate 1/4, extinction times by partial fractions and by an arctangent"
category: midterm_1_problem
archetype: ode-first-order-qualitative
level: conceptual
unit: 2
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of MATHS_FIRSTPARTIAL_2019_MT1_SOL, MATHS_FIRSTPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p02.py"
tags:
  - problem-bank
  - midterm-1
  - logistic-equation
  - phase-line
  - stability
  - partial-fractions
  - separable-equations
---

# Bank P02 — Logistic population with constant harvesting

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FIRSTPARTIAL_2019_MT1_SOL and MATHS_FIRSTPARTIAL_2025_G47_SOL. Method: Topic 2 (autonomous equations, equilibria and their stability through $f'(p^*)$, Notes, p. 3; separable equations, Robinson Ch. 8) and the logistic model of [[Concept - Logistic Equation and Carrying Capacity]]. Every result was checked with SymPy (scripts/am_bank/p02.py).

## Statement

A fish population $P(t)$ grows logistically with intrinsic rate $r>0$ and carrying capacity $K>0$ and is fished at a constant rate $H\ge0$ (individuals per unit time), independent of the size of the stock:

$$\frac{dP}{dt}=rP\Big(1-\frac PK\Big)-H.$$

With $p=P/K$, $\tau=rt$ and $h=H/(rK)$ the model becomes, writing again $t$ for $\tau$ and $'$ for $d/dt$,

$$p'=p(1-p)-h,\qquad h\ge0.$$

The model is used only while $p\ge0$; if $p$ reaches $0$ the population is extinct (collapse). Part (c) uses $h=2/9$ and part (d) uses $h=1/2$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $p(t)\ge0$ (fraction of the carrying capacity), independent variable $t$ (dimensionless time, unit $1/r$); parameter $h\ge0$ (dimensionless harvest).
- Operator: first order, **nonlinear** (quadratic in $p$), **autonomous** ($f$ does not depend on $t$). $f(p)=p(1-p)-h$ is a polynomial, so $f$ and $f'$ are continuous and Picard's theorem gives a unique local solution for every $p(0)$; distinct solutions never cross, and equilibria split the line into invariant intervals.
- Separable: $\dfrac{dp}{f(p)}=dt$ wherever $f(p)\neq0$.

#### Phase 2. Canonical formulation

$$p'=f(p),\qquad f(p)=-\big(p^2-p+h\big)=-\Big[\Big(p-\frac12\Big)^2+h-\frac14\Big].$$

The completed square already shows that the sign of $h-\tfrac14$ decides everything.

## (a) Equilibria and the critical harvesting rate [1.0 pts]

Find the equilibria as functions of $h$, the critical rate $h_c$ and its meaning.

### Hint

Solve $p^2-p+h=0$. The growth term $p(1-p)$ has a maximum.

### Checkpoint

- $p_\pm=\dfrac{1\pm\sqrt{1-4h}}{2}$ for $h<\tfrac14$; one equilibrium $p=\tfrac12$ for $h=\tfrac14$; none for $h>\tfrac14$.
- $h_c=\tfrac14$, i.e. $H_c=\dfrac{rK}{4}$, the maximum natural growth rate (reached at $P=K/2$).

### Solution

#### Step 1. Equilibria

$f(p)=0\iff p^2-p+h=0$, with discriminant $1-4h$:

$$p_\pm=\frac{1\pm\sqrt{1-4h}}{2}\quad(h<\tfrac14),\qquad p=\tfrac12\quad(h=\tfrac14),\qquad \text{none}\quad(h>\tfrac14).$$

For $0\le h<\tfrac14$: $0\le p_-<\tfrac12<p_+\le1$, with $p_-=0$, $p_+=1$ when $h=0$ (the logistic equation). As $h$ grows the two equilibria approach each other, merge at $\tfrac12$ for $h=\tfrac14$ and disappear.

#### Step 2. Critical rate and meaning

$h_c=\tfrac14$. The natural growth $g(p)=p(1-p)$ has $g'(p)=1-2p=0$ at $p=\tfrac12$, with $g(\tfrac12)=\tfrac14$, its maximum. In original variables $h=H/(rK)$, so

$$H_c=\frac{rK}{4},$$

the largest growth the stock can produce, reached at $P=K/2$. Any constant catch above it exceeds what the population can regenerate at any size (the "maximum sustainable yield"). The merging and disappearance of two equilibria as a parameter crosses a value is called a saddle-node bifurcation (extension: a name beyond the course; the course only needs the phase lines of (b)).

## (b) Phase lines in the three regimes [1.5 pts]

Describe the phase line and classify the equilibria for $h<h_c$, $h=h_c$, $h>h_c$, and say which initial populations survive.

### Hint

$f$ is a downward parabola: positive between its roots, negative outside. Use $f'(p^*)$ when it is not zero.

### Checkpoint

- $h<\tfrac14$: $p_-$ unstable ($f'(p_-)=\sqrt{1-4h}>0$), $p_+$ asymptotically stable ($f'(p_+)=-\sqrt{1-4h}<0$). Survival iff $p(0)\ge p_-$ (with $p(0)=p_-$ the equilibrium itself).
- $h=\tfrac14$: $p=\tfrac12$ semi-stable ($f=-(p-\tfrac12)^2\le0$): attracts from above, repels below. Survival iff $p(0)\ge\tfrac12$.
- $h>\tfrac14$: $f\le\tfrac14-h<0$ everywhere, every solution decreases and collapses in finite time.

### Solution

#### Step 1. Case $0\le h<\tfrac14$

$f(p)=-(p-p_-)(p-p_+)$: $f<0$ for $p<p_-$, $f>0$ on $(p_-,p_+)$, $f<0$ for $p>p_+$. Phase line (arrows of $p'$):

$$0\ \ \longleftarrow\ \ p_-\ \ \longrightarrow\ \ p_+\ \ \longleftarrow$$

With $f'(p)=1-2p$ (Notes, p. 3, linear stability test):

$$f'(p_\pm)=1-\big(1\pm\sqrt{1-4h}\big)=\mp\sqrt{1-4h},$$

so $f'(p_-)>0$: **unstable**; $f'(p_+)<0$: **asymptotically stable**. Populations with $p(0)>p_-$ tend to $p_+$; those with $p(0)<p_-$ decrease and reach $0$ ($p_-$ is a survival threshold). For $h=0$, $p_-=0$ and nothing collapses.

#### Step 2. Case $h=\tfrac14$

$f(p)=-(p-\tfrac12)^2\le0$, with $f'(\tfrac12)=0$: the linear test is inconclusive and the sign of $f$ decides. $p'<0$ on both sides:

$$\longleftarrow\ \ \tfrac12\ \ \longleftarrow$$

From above, $p$ decreases to $\tfrac12$ (attracting side); from below, $p$ moves away towards $0$ (repelling side). The equilibrium is **semi-stable**: it is not stable, since an arbitrarily small loss pushes the stock into collapse.

#### Step 3. Case $h>\tfrac14$

$f(p)=-(p-\tfrac12)^2-(h-\tfrac14)\le-(h-\tfrac14)<0$ for every $p$. There is no equilibrium and every solution decreases at a rate at least $h-\tfrac14$, so from any $p(0)$ it reaches $0$ before the time $p(0)/(h-\tfrac14)$: collapse in finite time for every initial stock.

## (c) Explicit solutions for h = 2/9 [1.5 pts]

Solve with $p(0)=1/2$ and with $p(0)=1/4$; in the second case find the time of collapse.

### Hint

$p^2-p+\tfrac29=(p-\tfrac13)(p-\tfrac23)$. Decompose $\dfrac1{(p-\frac13)(p-\frac23)}$ into partial fractions.

### Checkpoint

- Equilibria $p_-=\tfrac13$ (unstable), $p_+=\tfrac23$ (stable). General solution $\dfrac{p-\frac23}{p-\frac13}=K\,e^{-t/3}$, $p=\dfrac{2-Ke^{-t/3}}{3(1-Ke^{-t/3})}$.
- $p(0)=\tfrac12$: $K=-1$, $p(t)=\dfrac{2+e^{-t/3}}{3(1+e^{-t/3})}\to\tfrac23$.
- $p(0)=\tfrac14$: $K=5$, $p(t)=\dfrac{2e^{t/3}-5}{3(e^{t/3}-5)}$, collapse at $T_0=3\ln\tfrac52\approx2.749$.

### Solution

#### Step 1. Factorisation and partial fractions

With $h=\tfrac29$: $\sqrt{1-\tfrac89}=\tfrac13$, $p_\pm=\tfrac{1\pm1/3}{2}$, i.e. $p_-=\tfrac13$, $p_+=\tfrac23$, and $f(p)=-(p-\tfrac13)(p-\tfrac23)$. Write

$$\frac{1}{(p-\frac13)(p-\frac23)}=\frac{A}{p-\frac13}+\frac{B}{p-\frac23}\iff1=A\Big(p-\frac23\Big)+B\Big(p-\frac13\Big).$$

At $p=\tfrac13$: $1=-\tfrac13A$, $A=-3$. At $p=\tfrac23$: $1=\tfrac13B$, $B=3$.

#### Step 2. Separation and integration

For $p\neq\tfrac13,\tfrac23$: $\dfrac{dp}{(p-\frac13)(p-\frac23)}=-dt$. With the antiderivatives $\int\frac{dp}{p-c}=\ln\lvert p-c\rvert$:

$$3\ln\Big\lvert p-\frac23\Big\rvert-3\ln\Big\lvert p-\frac13\Big\rvert=-t+C\ \Longrightarrow\ \ln\left\lvert\frac{p-\frac23}{p-\frac13}\right\rvert=-\frac t3+\frac C3.$$

Exponentiating and absorbing the sign into the constant: $\dfrac{p-\frac23}{p-\frac13}=K\,e^{-t/3}$, with $K=\dfrac{p(0)-\frac23}{p(0)-\frac13}$ from $t=0$.

#### Step 3. Solving for p

Write $E=Ke^{-t/3}$: $p-\tfrac23=E\,p-\tfrac E3$, so $p(1-E)=\tfrac23-\tfrac E3$ and

$$p(t)=\frac{2-K\,e^{-t/3}}{3\big(1-K\,e^{-t/3}\big)}.$$

#### Step 4. The two initial data

- $p(0)=\tfrac12$: $K=\dfrac{-1/6}{1/6}=-1$, $\ p(t)=\dfrac{2+e^{-t/3}}{3(1+e^{-t/3})}$. Check $p(0)=\tfrac36=\tfrac12$. As $t\to\infty$, $e^{-t/3}\to0$ and $p\to\tfrac23=p_+$: the stock recovers to the stable equilibrium, as the phase line predicts.
- $p(0)=\tfrac14$ (below the threshold $p_-=\tfrac13$): $K=\dfrac{\frac14-\frac23}{\frac14-\frac13}=\dfrac{-5/12}{-1/12}=5$. Multiplying numerator and denominator by $e^{t/3}$:

$$p(t)=\frac{2e^{t/3}-5}{3\big(e^{t/3}-5\big)}.$$

Check $p(0)=\tfrac{-3}{-12}=\tfrac14$. $p=0$ when $2e^{t/3}=5$:

$$T_0=3\ln\frac52\approx2.749.$$

The formula has a pole at $t=3\ln5\approx4.83>T_0$, but the model has already stopped: the population is extinct at $T_0$. In original time, $t_{\text{real}}=T_0/r$.

## (d) Collapse time for h = 1/2 [1.0 pts]

Take $h=1/2$ and $p(0)=1$. Find the collapse time $T$ and $p(t)$ on $[0,T]$.

### Hint

$p^2-p+\tfrac12=(p-\tfrac12)^2+\tfrac14$. Substitute $s=2p-1$, $ds=2\,dp$.

### Checkpoint

- $\displaystyle T=\int_0^1\frac{dp}{(p-\frac12)^2+\frac14}=\big[2\arctan(2p-1)\big]_0^1=\pi$.
- $p(t)=\dfrac12+\dfrac12\tan\Big(\dfrac\pi4-\dfrac t2\Big)$, $0\le t\le\pi$.
- For a general start $p(0)\in[0,1]$: $T=2\arctan(2p(0)-1)+\dfrac\pi2$.

### Solution

#### Step 1. Antiderivative

$p'=-\big[(p-\tfrac12)^2+\tfrac14\big]<0$. With $s=2p-1$, $ds=2\,dp$ and $(p-\tfrac12)^2+\tfrac14=\tfrac{s^2+1}{4}$:

$$\int\frac{dp}{(p-\frac12)^2+\frac14}=\int\frac{ds/2}{(s^2+1)/4}=2\int\frac{ds}{1+s^2}=2\arctan s=2\arctan(2p-1).$$

#### Step 2. Time to collapse

Separating, $dt=-\dfrac{dp}{(p-\frac12)^2+\frac14}$. As $t$ runs from $0$ to $T$, $p$ runs from $1$ down to $0$, so by Barrow's rule

$$T=\int_1^0\frac{-dp}{(p-\frac12)^2+\frac14}=\Big[2\arctan(2p-1)\Big]_0^1=2\arctan1-2\arctan(-1)=2\cdot\frac\pi4+2\cdot\frac\pi4=\pi.$$

The same computation from a general $p(0)$ gives $T=2\arctan(2p(0)-1)-2\arctan(-1)=2\arctan(2p(0)-1)+\tfrac\pi2$; for example $p(0)=\tfrac12$ gives $\tfrac\pi2$.

#### Step 3. The solution

Integrating from $0$ to $t$: $2\arctan(2p-1)-2\arctan(1)=-t$, so $\arctan(2p-1)=\tfrac\pi4-\tfrac t2$ and

$$p(t)=\frac12+\frac12\tan\Big(\frac\pi4-\frac t2\Big),\qquad0\le t\le\pi.$$

Check: $p(0)=\tfrac12+\tfrac12\tan\tfrac\pi4=1$; $p(\pi)=\tfrac12+\tfrac12\tan(-\tfrac\pi4)=0$. By the chain rule $p'=\tfrac12\sec^2(\tfrac\pi4-\tfrac t2)\cdot(-\tfrac12)=-\tfrac14(1+\tan^2)$, and $-\big[(p-\tfrac12)^2+\tfrac14\big]=-\tfrac14\tan^2-\tfrac14$: the same. In original time the collapse happens at $t_{\text{real}}=\pi/r$.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $h=0$ recovers the logistic equation ($p_-=0$, $p_+=1$). For $h>\tfrac14$ and $p(0)=1$, with $\omega=\sqrt{h-\frac14}$ the same arctangent integral gives $T=\frac2\omega\arctan\frac1{2\omega}$ ($=\pi$ for $\omega=\tfrac12$): $T\to\infty$ as $h\to\tfrac14^+$ (the stock lingers near $p=\tfrac12$, where $p'$ is almost zero) and $T\to0$ as $h\to\infty$.
- **Checks:** every explicit solution was substituted back into the equation and satisfies its initial value; the solutions agree with the phase lines of (b) (monotone, no crossing of equilibria). Dimensions: $h=H/(rK)$ is (individuals/time)/((1/time)(individuals)), dimensionless; real times are the dimensionless ones divided by $r$.
- **Common mistakes in the exam:** (1) applying the linear test $f'(p^*)$ at $h=\tfrac14$, where it gives $0$, and concluding "stable"; (2) forgetting that below $p_-$ the population collapses even for small harvesting; (3) reading the pole of the formula of (c) as the time of extinction instead of the first zero of $p$; (4) losing the factor $2$ from $ds=2\,dp$ in the arctangent integral.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
