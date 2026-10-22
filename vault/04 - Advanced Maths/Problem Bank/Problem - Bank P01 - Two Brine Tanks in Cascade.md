---
materia: Advanced Maths
tema: "Unit 1: modelling with first-order linear ODEs"
bank_id: P01
title: "Two brine tanks in cascade: separation for the first tank, integrating factor for the second, the equal-rate case and the peak of salt"
category: midterm_1_problem
archetype: ode-first-order-modeling
level: standard
unit: 1
difficulty: 2
points: 5.0
time_minutes: 30
official: false
origen: "Problem written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL, MATHS_FIRSTPARTIAL_2025_G47_SOL; not an official exercise. Verified with scripts/am_bank/p01.py"
tags:
  - problem-bank
  - midterm-1
  - mixing-tanks
  - separable-equations
  - integrating-factor
  - modelling
  - dimensional-analysis
---

# Bank P01 — Two brine tanks in cascade

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FIRSTPARTIAL_2020_G45_SOL and MATHS_FIRSTPARTIAL_2025_G47_SOL. Method: Topic 1 (modelling by a balance law, the mixing tank of Ch1-P6), Topic 2 (separable equations, Robinson Ch. 8; the integrating factor, Robinson Ch. 9 and Notes, p. 3). Every result was checked with SymPy (scripts/am_bank/p01.py).

## Statement

Two well-stirred tanks are connected in series. Tank A holds $V_A=100$ L of brine containing $20$ kg of dissolved salt; tank B holds $V_B$ litres of fresh water. At $t=0$ three pumps are switched on, all with the same flow rate $r=10$ L/min: fresh water enters A, the mixture of A flows into B, and the mixture of B is drained to the outside. Time is measured in minutes. Let $x(t)$ and $y(t)$ be the masses of salt (kg) in A and in B, and write $k_A=r/V_A$, $k_B=r/V_B$ for the rate constants. Part (c) uses $V_B=100$ L and part (d) uses $V_B=50$ L.

## Setup

#### Phase 1. Hypotheses and setup

- Unknowns $x(t)$, $y(t)$ (kg), independent variable $t\ge0$ (min).
- Hypotheses: perfect mixing (the concentration of the outflow of each tank is its mean concentration), equal inflow and outflow, so the volumes stay constant; salt is conserved (no reaction, no precipitation).
- Operator: two first-order, linear equations with constant coefficients. The equation for $x$ is homogeneous and decoupled; the equation for $y$ is inhomogeneous, forced by $x$ (a triangular, one-way coupling).

| Quantity | Symbol | Value | Unit |
| :--- | :--- | :--- | :--- |
| Flow rate | $r$ | $10$ | L/min |
| Volume of A | $V_A$ | $100$ | L |
| Volume of B | $V_B$ | $100$ in (c), $50$ in (d) | L |
| Initial salt in A | $x_0$ | $20$ | kg |
| Initial salt in B | $y(0)$ | $0$ | kg |
| Rate constants | $k_A=r/V_A$, $k_B=r/V_B$ | $0.1$; $0.1$ or $0.2$ | min$^{-1}$ |

#### Phase 2. Canonical formulation

The balance law (rate of change = rate in $-$ rate out) for each tank, in the linear standard form $y'+p(t)\,y=q(t)$ of Topic 2:

$$x'+k_A\,x=0,\qquad y'+k_B\,y=k_A\,x(t),\qquad x(0)=x_0,\quad y(0)=0.$$

## (a) Model and dimensions [1.0 pts]

Write the initial value problem satisfied by $x$ and $y$ and check its dimensions.

### Hint

The salt leaves a tank at (flow rate) $\times$ (concentration $=$ mass/volume). What leaves A enters B.

### Checkpoint

- $x'=-\dfrac{r}{V_A}x$, $\ y'=\dfrac{r}{V_A}x-\dfrac{r}{V_B}y$, $\ x(0)=20$ kg, $y(0)=0$.
- $k_A=k_B=0.1$ min$^{-1}$ in (c); $k_A=0.1$, $k_B=0.2$ min$^{-1}$ in (d).
- Every term has units kg/min.

### Solution

#### Step 1. Tank A

Fresh water carries no salt, so the rate in is $0$. The outflow carries $r$ L/min at concentration $x/V_A$ kg/L:

$$\frac{dx}{dt}=0-r\,\frac{x}{V_A}=-k_A\,x,\qquad k_A=\frac{r}{V_A}.$$

#### Step 2. Tank B

Its inflow is the outflow of A, with concentration $x/V_A$; its outflow has concentration $y/V_B$:

$$\frac{dy}{dt}=r\,\frac{x}{V_A}-r\,\frac{y}{V_B}=k_A\,x-k_B\,y,\qquad k_B=\frac{r}{V_B}.$$

The initial data are $x(0)=x_0=20$ kg and $y(0)=0$ (fresh water).

#### Step 3. Dimensions

$[r]=$ L min$^{-1}$, $[V]=$ L, so $[k_A]=[k_B]=$ min$^{-1}$. Then $[k_Ax]=$ min$^{-1}\cdot$kg $=$ kg/min $=[dx/dt]$, and the same for every term of the second equation: both equations are dimensionally homogeneous. The exponents that will appear, $k_At$ and $k_Bt$, are dimensionless.

Numerically $k_A=10/100=0.1$ min$^{-1}$; $k_B=10/100=0.1$ min$^{-1}$ for $V_B=100$ L and $k_B=10/50=0.2$ min$^{-1}$ for $V_B=50$ L.

## (b) Solution for different rate constants [1.5 pts]

Solve for $x(t)$ by separation of variables and, for $k_A\neq k_B$, solve for $y(t)$ with an integrating factor.

### Hint

For $y$ the integrating factor is $\mu(t)=e^{k_Bt}$; integrate $(\mu y)'$ from $0$ to $t$ with Barrow's rule.

### Checkpoint

- $x(t)=x_0\,e^{-k_At}$.
- $y(t)=\dfrac{k_A\,x_0}{k_B-k_A}\big(e^{-k_At}-e^{-k_Bt}\big)$, $k_A\neq k_B$.

### Solution

#### Step 1. Tank A by separation

$x\equiv0$ is not the solution ($x_0\neq0$). For $x>0$, separate: $\dfrac{dx}{x}=-k_A\,dt$. Integrate from $0$ to $t$:

$$\int_{x_0}^{x(t)}\frac{d\xi}{\xi}=\big[\ln\xi\big]_{x_0}^{x(t)}=\ln\frac{x(t)}{x_0},\qquad \int_0^t(-k_A)\,ds=-k_A\,t.$$

Hence $\ln(x/x_0)=-k_At$ and

$$x(t)=x_0\,e^{-k_At}.$$

#### Step 2. Integrating factor for B

Substitute $x(t)$: $y'+k_By=k_Ax_0e^{-k_At}$. With $p=k_B$ the integrating factor (Notes, p. 3) is $\mu(t)=e^{\int_0^tk_B\,ds}=e^{k_Bt}$, with $\mu'=k_B\mu$. By the product rule, $(\mu y)'=\mu y'+\mu'y=e^{k_Bt}(y'+k_By)$, so

$$\frac{d}{dt}\big(e^{k_Bt}y\big)=k_Ax_0\,e^{(k_B-k_A)t}.$$

#### Step 3. Integration

For $k_B\neq k_A$ an antiderivative of $e^{(k_B-k_A)s}$ is $\dfrac{e^{(k_B-k_A)s}}{k_B-k_A}$. Integrating from $0$ to $t$ and using $y(0)=0$ (Barrow's rule on both sides):

$$e^{k_Bt}y(t)-e^{0}\,y(0)=k_Ax_0\left[\frac{e^{(k_B-k_A)s}}{k_B-k_A}\right]_0^t=\frac{k_Ax_0}{k_B-k_A}\Big(e^{(k_B-k_A)t}-1\Big).$$

Multiplying by $e^{-k_Bt}$:

$$y(t)=\frac{k_A\,x_0}{k_B-k_A}\Big(e^{-k_At}-e^{-k_Bt}\Big).$$

#### Step 4. Check

$y(0)=\frac{k_Ax_0}{k_B-k_A}(1-1)=0$. Differentiating, $y'=\frac{k_Ax_0}{k_B-k_A}(-k_Ae^{-k_At}+k_Be^{-k_Bt})$ and $k_Ax-k_By=\frac{k_Ax_0}{k_B-k_A}\big[(k_B-k_A)e^{-k_At}-k_Be^{-k_At}+k_Be^{-k_Bt}\big]$, which is the same expression. The quotient $\frac{e^{-k_At}-e^{-k_Bt}}{k_B-k_A}$ does not change when $k_A$ and $k_B$ are exchanged (numerator and denominator both change sign), and it is positive for $t>0$: $y(t)>0$ whichever tank is faster.

## (c) Equal volumes: the resonant case [1.5 pts]

Take $V_B=100$ L. Solve the equation for $y$ directly, show that the result is the limit of (b) as $k_B\to k_A$, and find the time and value of the largest amount of salt in B.

### Hint

With $k_A=k_B=k$ the right-hand side of $(e^{kt}y)'$ is a constant. For the limit, the quotient $\frac{e^{-k_At}-e^{-k_Bt}}{k_B-k_A}$ is a $0/0$ form in $k_B$.

### Checkpoint

- $y(t)=k\,x_0\,t\,e^{-kt}=2\,t\,e^{-t/10}$ kg.
- Maximum at $t^*=1/k=10$ min, $y_{\max}=x_0/e=20/e\approx7.358$ kg (concentration $0.0736$ kg/L).

### Solution

#### Step 1. Direct solution

With $k_A=k_B=k=0.1$ min$^{-1}$, Step 2 of (b) gives $\frac{d}{dt}(e^{kt}y)=kx_0e^{0}=kx_0$. Integrating from $0$ to $t$: $e^{kt}y(t)-y(0)=kx_0\,[s]_0^t=kx_0\,t$, so

$$y(t)=k\,x_0\,t\,e^{-kt}=0.1\cdot20\,t\,e^{-t/10}=2\,t\,e^{-t/10}\ \text{kg}.$$

The forcing $k x_0e^{-kt}$ decays at exactly the rate of the free response $e^{-kt}$ of tank B: the exponential guess fails and a factor $t$ appears, the first-order analogue of resonance.

#### Step 2. Limit of the general formula

Fix $k_A=k$. In $y=kx_0\,\dfrac{e^{-kt}-e^{-k_Bt}}{k_B-k}$ numerator and denominator vanish at $k_B=k$. By L'Hôpital's rule in the variable $k_B$, with $\frac{\partial}{\partial k_B}e^{-k_Bt}=-t\,e^{-k_Bt}$ (chain rule):

$$\lim_{k_B\to k}\frac{e^{-kt}-e^{-k_Bt}}{k_B-k}=\lim_{k_B\to k}\frac{t\,e^{-k_Bt}}{1}=t\,e^{-kt},$$

so $y\to kx_0\,t\,e^{-kt}$, the result of Step 1. The two cases join continuously.

#### Step 3. Maximum

By the product rule, $y'(t)=kx_0\big(e^{-kt}+t(-k)e^{-kt}\big)=kx_0\,e^{-kt}(1-kt)$. It is positive for $t<1/k$ and negative for $t>1/k$, so $y$ has its maximum at $t^*=1/k=10$ min:

$$y_{\max}=kx_0\cdot\frac1k\,e^{-1}=\frac{x_0}{e}=\frac{20}{e}\approx7.358\ \text{kg},$$

a concentration of $7.358/100\approx0.0736$ kg/L. At that moment tank A holds $x(10)=20e^{-1}$ kg as well.

## (d) Smaller second tank, peak and long-time behaviour [1.0 pts]

Take $V_B=50$ L. Find the time and value of the largest amount of salt in B, compare the concentrations of both tanks then, give the limit $t\to\infty$ and the total salt that leaves the system.

### Hint

Write $u=e^{-t/10}$, so $e^{-t/5}=u^2$. The condition $y'=0$ is $k_Ax=k_By$.

### Checkpoint

- $y(t)=20\big(e^{-t/10}-e^{-t/5}\big)$ kg.
- $t^*=10\ln2\approx6.93$ min, $y_{\max}=5$ kg; at $t^*$ both concentrations equal $0.1$ kg/L.
- $x,y\to0$; total outflow of salt $\int_0^\infty k_By\,dt=20$ kg.

### Solution

#### Step 1. The formula

$k_A=0.1$, $k_B=0.2$ min$^{-1}$, so $\frac{k_Ax_0}{k_B-k_A}=\frac{0.1\cdot20}{0.1}=20$ kg and $y(t)=20\big(e^{-t/10}-e^{-t/5}\big)$.

#### Step 2. Maximum

$y'(t)=20\big(-\tfrac1{10}e^{-t/10}+\tfrac15e^{-t/5}\big)$. With $u=e^{-t/10}\in(0,1]$: $y'=20\big(-\tfrac{u}{10}+\tfrac{u^2}{5}\big)=\tfrac{20u}{10}(2u-1)$, which vanishes for $u=\tfrac12$, is positive for $u>\tfrac12$ (early times) and negative after. Hence $e^{-t^*/10}=\tfrac12$, $t^*=10\ln2\approx6.93$ min, and

$$y_{\max}=20\Big(\frac12-\frac14\Big)=5\ \text{kg}.$$

This agrees with the general time $t^*=\dfrac{\ln(k_B/k_A)}{k_B-k_A}=\dfrac{\ln2}{0.1}$.

#### Step 3. Concentrations at the peak

$x(t^*)=20\cdot\tfrac12=10$ kg, so A has $10/100=0.1$ kg/L and B has $5/50=0.1$ kg/L. This is general: $y'=0$ means $k_Ax=k_By$, i.e. $\frac{x}{V_A}=\frac{y}{V_B}$. Tank B stops gaining salt exactly when its concentration equals that of the brine coming in.

#### Step 4. Long time and total outflow

Both exponentials tend to $0$, so $x(t)\to0$ and $y(t)\to0$: all salt is washed out. The salt drained from B per minute is $k_By$; with the antiderivatives $-10e^{-t/10}$ and $-5e^{-t/5}$ and Barrow's rule on $[0,T]$, $T\to\infty$:

$$\int_0^\infty0.2\cdot20\big(e^{-t/10}-e^{-t/5}\big)dt=4\Big[-10e^{-t/10}+5e^{-t/5}\Big]_0^\infty=4\big(0-(-10+5)\big)=20\ \text{kg},$$

the whole initial mass $x_0$, as conservation of salt requires.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $t\to0^+$: $y\approx k_Ax_0\,t$ (B starts filling at the rate A loses salt, $k_Ax_0=2$ kg/min). $t\to\infty$: $y\sim\frac{k_Ax_0}{k_B-k_A}e^{-k_At}$ when $k_A<k_B$, so the slower tank sets the decay. $V_B\to0$ ($k_B\to\infty$): $y\to0$, B becomes a pipe.
- **Checks:** both formulas satisfy the ODEs and $y(0)=0$ by substitution; the equal-rate case is the limit of the general one; $\int_0^\infty k_By\,dt=x_0$. Dimensions: $k\,x_0\,t$ is (min$^{-1}$)(kg)(min) $=$ kg, $t^*=1/k$ and $\ln(k_B/k_A)/(k_B-k_A)$ are in minutes.
- **Common mistakes in the exam:** (1) using the volume of B in the inflow term of B (the inflow concentration is $x/V_A$); (2) applying the formula of (b) with $k_A=k_B$, which divides by zero, instead of noticing the factor $t$; (3) dropping the lower limit in the integrating-factor integral, which leaves $y(0)\neq0$; (4) reporting the maximum time without checking the sign of $y'$, or confusing the maximum of mass with the maximum of concentration.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
