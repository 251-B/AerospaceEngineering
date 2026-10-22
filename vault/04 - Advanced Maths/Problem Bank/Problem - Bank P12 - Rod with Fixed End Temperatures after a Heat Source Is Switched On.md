---
materia: Advanced Maths
tema: "Unit 6: heat equation with non-homogeneous boundary data"
bank_id: P12
title: "Heat equation with a constant source and fixed, different end temperatures: steady state, separation of variables for the deviation, series solution and the time constant of the slowest mode"
category: midterm_2_problem
archetype: pde-separation-heat-wave
level: standard
unit: 6
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2020_G45_SOL, MATHS_SECONDPARTIAL_2025_G46_SOL; not an official exercise. Verified with scripts/am_bank/p12.py"
tags:
  - problem-bank
  - midterm-2
  - heat-equation
  - separation-of-variables
  - steady-state
  - nonhomogeneous-boundary-conditions
  - fourier-sine-series
---

# Bank P12 — Rod with fixed end temperatures after a heat source is switched on

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the second midterm papers (MATHS_SECONDPARTIAL_2020_G45_SOL, MATHS_SECONDPARTIAL_2025_G46_SOL). Method: Haberman, *Elementary Applied PDEs* (unit 5 text, `BookPDE's.pdf`), Sec. 1.4 (equilibrium temperature distribution), Sec. 2.3 (heat equation with zero temperatures at the ends: separation of variables, the three signs of the separation constant), Sec. 3.3 (Fourier sine series) and Sec. 7.2 (heat flow with sources and non-homogeneous boundary conditions). Every result was checked with SymPy (scripts/am_bank/p12.py).

## Statement

A thin laterally insulated rod occupies $0\le x\le L$. Its ends are held at the constant temperatures $u(0,t)=T_A$ and $u(L,t)=T_B$. For $t<0$ the rod has been left long enough to reach the equilibrium with no internal heat source. At $t=0$ an electric current is switched on that heats the rod uniformly, so that for $t>0$ the temperature $u(x,t)$ satisfies
$$u_t=k\,u_{xx}+Q,\qquad 0<x<L,\ t>0,$$
with constant diffusivity $k>0$ and constant source $Q>0$ (in K/s).

(a) Write the initial temperature $u(x,0)$. Find the steady state $u_s(x)$ of the problem for $t>0$ and the steady temperature at the midpoint.

(b) Write the problem satisfied by $v=u-u_s$. Separate variables in it, $v=X(x)T(t)$, and discuss the three cases of the sign of the separation constant to find all eigenvalues and eigenfunctions.

(c) Obtain $u(x,t)$ as a series with all coefficients in closed form.

(d) Find $\lim_{t\to\infty}u$, the time constant $\tau_1$ of the slowest mode, and, keeping only that mode, the time $t_{99}$ after which the midpoint has completed $99\%$ of its final rise. Numbers: $L=0.5$ m, $k=1.0\times10^{-4}$ m$^2$/s, $Q=0.02$ K/s, $T_A=20$ °C, $T_B=40$ °C.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $u(x,t)$, independent variables $x\in[0,L]$, $t\ge0$. One-dimensional conduction, constant properties, uniform volumetric source.
- Operator: linear, second order, parabolic; **non-homogeneous** twice: the source $Q$ in the equation and the Dirichlet data $T_A,T_B$ (non-zero). Separation of variables needs homogeneous boundary conditions, so the inhomogeneities are removed first with the steady state.
- Data: $L$ [m], $k$ [m$^2$/s], $Q$ [K/s], $T_A,T_B$ [°C or K].

#### Phase 2. Canonical formulation

$$u_t=k u_{xx}+Q,\quad u(0,t)=T_A,\quad u(L,t)=T_B,\quad u(x,0)=u_0(x)$$
Split $u(x,t)=u_s(x)+v(x,t)$, where $u_s$ absorbs the source and the boundary data and $v$ solves a homogeneous problem with homogeneous Dirichlet conditions (Haberman Sec. 7.2).

## (a) Initial temperature and steady state [1.0 pts]

### Hint

For $t<0$ there is no source: the equilibrium solves $u''=0$. For $t>0$, the steady state solves $k u_s''+Q=0$ with the same end values.

### Checkpoint

- $u_0(x)=T_A+(T_B-T_A)\dfrac{x}{L}$.
- $u_s(x)=T_A+(T_B-T_A)\dfrac{x}{L}+\dfrac{Q}{2k}\,x(L-x)$.
- $u_s(L/2)=\dfrac{T_A+T_B}{2}+\dfrac{QL^2}{8k}$; with the numbers $30+6.25=36.25$ °C.

### Solution

#### Step 1. Initial profile

Before the source is switched on the rod is in equilibrium, $u_t=0$, so $k u''=0$ and $u=\alpha+\beta x$. The end values give $\alpha=T_A$, $\alpha+\beta L=T_B$, hence $u_0(x)=T_A+(T_B-T_A)x/L$ (Haberman Sec. 1.4).

#### Step 2. Steady state with the source

$u_s''=-\dfrac{Q}{k}$. Integrating once: $u_s'=-\dfrac{Q}{k}x+C_1$; again: $u_s=-\dfrac{Q}{2k}x^2+C_1x+C_2$.

#### Step 3. Constants

$u_s(0)=C_2=T_A$. $u_s(L)=-\dfrac{QL^2}{2k}+C_1L+T_A=T_B$, so $C_1=\dfrac{T_B-T_A}{L}+\dfrac{QL}{2k}$. Substituting and grouping $\dfrac{Q}{2k}(Lx-x^2)$:
$$u_s(x)=T_A+(T_B-T_A)\frac xL+\frac{Q}{2k}\,x(L-x)$$
Check: $k u_s''=k\cdot\dfrac{Q}{2k}\cdot(-2)=-Q$, and $x(L-x)$ vanishes at both ends.

#### Step 4. Midpoint

$u_s(L/2)=T_A+\dfrac{T_B-T_A}{2}+\dfrac{Q}{2k}\cdot\dfrac{L}{2}\cdot\dfrac{L}{2}=\dfrac{T_A+T_B}{2}+\dfrac{QL^2}{8k}$. Numbers: $\dfrac{0.02\cdot0.25}{8\cdot10^{-4}}=6.25$ K, so $u_s(L/2)=36.25$ °C.

## (b) Problem for v and separation of variables [1.5 pts]

### Hint

Subtract the equations for $u$ and $u_s$. With $v=XT$, divide by $kXT$ and call the common constant $-\lambda$.

### Checkpoint

- $v_t=kv_{xx}$, $v(0,t)=v(L,t)=0$, $v(x,0)=u_0-u_s=-\dfrac{Q}{2k}x(L-x)$.
- $\lambda<0$ and $\lambda=0$: only $X\equiv0$.
- $\lambda_n=\Big(\dfrac{n\pi}{L}\Big)^2$, $X_n=\sin\dfrac{n\pi x}{L}$, $T_n=e^{-k n^2\pi^2t/L^2}$, $n=1,2,\dots$

### Solution

#### Step 1. Homogeneous problem

$v_t=u_t-0=k u_{xx}+Q-(k u_s''+Q)=k(u-u_s)_{xx}=k v_{xx}$. At the ends $v(0,t)=T_A-T_A=0$ and $v(L,t)=T_B-T_B=0$. Initially $v(x,0)=u_0-u_s=-\dfrac{Q}{2k}x(L-x)$: the linear parts cancel.

#### Step 2. Separation

$v=X(x)T(t)$ gives $XT'=kX''T$, and dividing by $kXT$:
$$\frac{T'}{kT}=\frac{X''}{X}=-\lambda$$
The left side depends only on $t$ and the middle only on $x$, so both equal a constant. Hence $T'=-\lambda kT$ and $X''+\lambda X=0$, $X(0)=X(L)=0$ (the conditions on $v$ with $T\not\equiv0$).

#### Step 3. Case lambda < 0

Write $\lambda=-\mu^2$, $\mu>0$: $X=a\cosh\mu x+b\sinh\mu x$. $X(0)=a=0$; $X(L)=b\sinh\mu L=0$ with $\sinh\mu L>0$, so $b=0$. Only the trivial solution.

#### Step 4. Case lambda = 0

$X''=0$, $X=a+bx$. $X(0)=a=0$, $X(L)=bL=0\Rightarrow b=0$. Trivial.

#### Step 5. Case lambda > 0

$\lambda=\mu^2$: $X=a\cos\mu x+b\sin\mu x$. $X(0)=a=0$; $X(L)=b\sin\mu L=0$ with $b\ne0$ requires $\mu L=n\pi$. Hence
$$\lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\qquad X_n(x)=\sin\frac{n\pi x}{L},\qquad n=1,2,3,\dots$$
and $T'=-k\lambda_nT$ integrates to $T_n(t)=e^{-k\lambda_n t}$.

## (c) Series solution [1.5 pts]

### Hint

By superposition $v=\sum c_n X_nT_n$; the $c_n$ are the sine coefficients of $v(x,0)$. Integrate $x(L-x)\sin(n\pi x/L)$ by parts twice.

### Checkpoint

- $\displaystyle\frac2L\int_0^L x(L-x)\sin\frac{n\pi x}{L}\,dx=\frac{4L^2}{n^3\pi^3}\big(1-(-1)^n\big)$: $\dfrac{8L^2}{n^3\pi^3}$ for odd $n$, $0$ for even $n$.
- $c_n=-\dfrac{4QL^2}{k\pi^3n^3}$ for odd $n$, $c_n=0$ for even $n$.
- $\displaystyle u(x,t)=T_A+(T_B-T_A)\frac xL+\frac{Q}{2k}x(L-x)-\frac{4QL^2}{k\pi^3}\sum_{n\ \mathrm{odd}}\frac{1}{n^3}\sin\frac{n\pi x}{L}\,e^{-kn^2\pi^2t/L^2}$.

### Solution

#### Step 1. Superposition

Each product $X_nT_n$ satisfies $v_t=kv_{xx}$ and the zero end conditions, and so does any convergent combination:
$$v(x,t)=\sum_{n=1}^{\infty}c_n\sin\frac{n\pi x}{L}\,e^{-kn^2\pi^2t/L^2}$$
At $t=0$: $\displaystyle -\frac{Q}{2k}x(L-x)=\sum c_n\sin\frac{n\pi x}{L}$, so by orthogonality $c_n=\dfrac2L\displaystyle\int_0^L\Big(-\frac{Q}{2k}\Big)x(L-x)\sin\frac{n\pi x}{L}\,dx$.

#### Step 2. The integral

Write $\omega=n\pi/L$. With $u=x(L-x)=Lx-x^2$, $dv=\sin\omega x\,dx$ ($du=(L-2x)\,dx$, $v=-\cos\omega x/\omega$):
$$\int_0^L(Lx-x^2)\sin\omega x\,dx=\Big[-\frac{(Lx-x^2)\cos\omega x}{\omega}\Big]_0^L+\frac1\omega\int_0^L(L-2x)\cos\omega x\,dx$$
The bracket is $0$ because $Lx-x^2$ vanishes at $x=0$ and $x=L$. Next, $u=L-2x$, $dv=\cos\omega x\,dx$ ($du=-2\,dx$, $v=\sin\omega x/\omega$):
$$\int_0^L(L-2x)\cos\omega x\,dx=\Big[\frac{(L-2x)\sin\omega x}{\omega}\Big]_0^L+\frac2\omega\int_0^L\sin\omega x\,dx=0+\frac2\omega\Big[-\frac{\cos\omega x}{\omega}\Big]_0^L=\frac{2}{\omega^2}\big(1-\cos n\pi\big)$$
since $\sin\omega L=\sin n\pi=0$. Hence $\displaystyle\int_0^L x(L-x)\sin\omega x\,dx=\frac{2(1-(-1)^n)}{\omega^3}=\frac{2L^3(1-(-1)^n)}{n^3\pi^3}$ and
$$\frac2L\int_0^Lx(L-x)\sin\frac{n\pi x}{L}\,dx=\frac{4L^2(1-(-1)^n)}{n^3\pi^3}$$

#### Step 3. Coefficients and solution

Multiplying by $-\dfrac{Q}{2k}$: $c_n=-\dfrac{2QL^2(1-(-1)^n)}{k\pi^3n^3}$, which is $-\dfrac{4QL^2}{k\pi^3n^3}$ for odd $n$ and $0$ for even $n$. Adding $u_s$:
$$u(x,t)=T_A+(T_B-T_A)\frac xL+\frac{Q}{2k}x(L-x)-\frac{4QL^2}{k\pi^3}\sum_{n=1,3,5,\dots}\frac{1}{n^3}\sin\frac{n\pi x}{L}\,e^{-kn^2\pi^2t/L^2}$$
The coefficients decay as $1/n^3$ (the odd extension of $x(L-x)$ is continuous with a continuous derivative), so the series converges fast even at $t=0$.

## (d) Long-time limit, time constant and the 99 % time [1.0 pts]

### Hint

Each exponential has rate $k n^2\pi^2/L^2$; the smallest rate ($n=1$) dominates at long times. Evaluate the series at $x=L/2$, where $\sin(n\pi/2)=(-1)^{(n-1)/2}$ for odd $n$.

### Checkpoint

- $u(x,t)\to u_s(x)$ as $t\to\infty$.
- $\tau_1=\dfrac{L^2}{k\pi^2}=253.3$ s; the $n=3$ mode decays $9$ times faster.
- Midpoint: $\dfrac{u_s(L/2)-u(L/2,t)}{QL^2/(8k)}\approx\dfrac{32}{\pi^3}e^{-t/\tau_1}$, so $t_{99}=\tau_1\ln\dfrac{3200}{\pi^3}=4.637\,\tau_1\approx1174.5$ s (about 19.6 min).

### Solution

#### Step 1. Limit

Every term carries $e^{-kn^2\pi^2t/L^2}\to0$ and $\sum 1/n^3$ converges, so $v\to0$ and $u\to u_s$: the rod forgets its initial state.

#### Step 2. Slowest mode

The $n=1$ term decays as $e^{-t/\tau_1}$ with $\tau_1=\dfrac{1}{k\lambda_1}=\dfrac{L^2}{k\pi^2}=\dfrac{0.25}{10^{-4}\cdot9.8696}=253.3$ s. The next non-zero mode, $n=3$, has $\tau_3=\tau_1/9$.

#### Step 3. Midpoint rise

The total rise of the midpoint is $u_s(L/2)-u_0(L/2)=\dfrac{QL^2}{8k}=6.25$ K. At $x=L/2$ the deficit is
$$u_s\Big(\frac L2\Big)-u\Big(\frac L2,t\Big)=\frac{4QL^2}{k\pi^3}\sum_{m=0}^{\infty}\frac{(-1)^m}{(2m+1)^3}e^{-(2m+1)^2t/\tau_1}$$
At $t=0$ the sum is $\pi^3/32$ (bank item P11), giving $\dfrac{4QL^2}{k\pi^3}\cdot\dfrac{\pi^3}{32}=\dfrac{QL^2}{8k}$, as it must. Keeping $m=0$, the fraction still missing is $\dfrac{32}{\pi^3}e^{-t/\tau_1}$.

#### Step 4. The 99 % time

$\dfrac{32}{\pi^3}e^{-t_{99}/\tau_1}=0.01\Rightarrow t_{99}=\tau_1\ln\dfrac{3200}{\pi^3}=\tau_1\ln(103.2)=4.637\,\tau_1\approx1174.5$ s. At that time the $m=1$ term is smaller than the $m=0$ term by the factor $\tfrac1{27}e^{-8\cdot4.637}<10^{-17}$: the one-mode answer is exact for practical purposes.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $Q\to0$ gives $u_s=u_0$ and $v\equiv0$: nothing happens, as expected. $t\to\infty$: $u\to u_s$, a parabola above the straight line between $T_A$ and $T_B$; with these numbers its maximum is interior, at $x^*=\dfrac L2+\dfrac{k(T_B-T_A)}{QL}=0.25+0.2=0.45$ m, since $u_s'(x^*)=0$.
- **Checks:** dimensions: $\dfrac{Q}{k}x^2$ is $\dfrac{\text{K s}^{-1}}{\text{m}^2\text{s}^{-1}}\text{m}^2=$ K; $\tau_1=L^2/k$ is s. Each mode satisfies $v_t=kv_{xx}$ and vanishes at both ends; the series at $t=0$ reproduces $u_0$ (checked numerically in the script).
- **Common mistakes in the exam:** (1) separating variables directly in $u$, whose boundary conditions are not homogeneous; (2) taking $v(x,0)=u_0$ instead of $u_0-u_s$; (3) skipping the cases $\lambda\le0$; (4) giving the time constant as $L^2/k$ (forgetting $\pi^2$) or using the decay rate of $v^2$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
