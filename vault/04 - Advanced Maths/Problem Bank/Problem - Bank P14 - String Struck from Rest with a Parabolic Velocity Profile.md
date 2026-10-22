---
materia: Advanced Maths
tema: "Unit 6: wave equation for a string with fixed ends"
bank_id: P14
title: "Vibrating string with fixed ends started from the rest position with a parabolic initial velocity: modes, coefficients from the velocity, d'Alembert check at the midpoint, energy of each mode and periodicity"
category: midterm_2_problem
archetype: pde-separation-heat-wave
level: standard
unit: 6
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2019_MT3_SOL, MATHS_SECONDPARTIAL_2025_G46_SOL; not an official exercise. Verified with scripts/am_bank/p14.py"
tags:
  - problem-bank
  - midterm-2
  - wave-equation
  - separation-of-variables
  - dalembert-solution
  - normal-modes
  - energy
---

# Bank P14 — String struck from rest with a parabolic velocity profile

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the second midterm papers (MATHS_SECONDPARTIAL_2019_MT3_SOL, MATHS_SECONDPARTIAL_2025_G46_SOL). Method: Haberman, *Elementary Applied PDEs* (unit 5 text, `BookPDE's.pdf`), Sec. 4.2 (derivation of the string equation, $c^2=T_0/\rho_0$), Sec. 4.4 (vibrating string with fixed ends: separation of variables, normal modes, period) and Sec. 3.3 (sine series). The d'Alembert formula and the energy of the string are used as checks. Every result was checked with SymPy (scripts/am_bank/p14.py).

## Statement

A string of length $L$, linear density $\rho$ and tension $T_0$ is fixed at $x=0$ and $x=L$. Its small transverse displacement $u(x,t)$ satisfies
$$u_{tt}=c^2u_{xx},\qquad 0<x<L,\ t>0,\qquad c^2=\frac{T_0}{\rho}.$$
At $t=0$ the string lies along its rest position and is struck by a wide hammer that gives it the velocity profile
$$u(x,0)=0,\qquad u_t(x,0)=g(x)=\frac{4V}{L^2}\,x(L-x),$$
where $V>0$ is the speed given to the midpoint.

(a) Separate variables, discuss the sign of the separation constant and find the normal modes compatible with the fixed ends and with $u(x,0)=0$.

(b) Obtain $u(x,t)$ as a series, with the coefficients in closed form.

(c) For $0\le t\le L/(2c)$ use d'Alembert's formula to obtain the displacement of the midpoint, $u(L/2,t)$, in closed form. Check it against the series at $t=L/(2c)$ and deduce $\sum_{n\ \mathrm{odd}}n^{-4}$.

(d) The energy of the string is $E(t)=\displaystyle\int_0^L\Big(\frac{\rho}{2}u_t^2+\frac{T_0}{2}u_x^2\Big)dx$. Compute the energy carried by each mode, check that their sum is the energy given by the hammer, and give the fraction carried by the fundamental. Show that the motion is periodic in time and describe the string at $t=L/(2c)$ and $t=L/c$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $u(x,t)$ on $0\le x\le L$, $t\ge0$; small transverse vibrations, uniform string, no damping, no gravity.
- Operator: linear, second order, hyperbolic, homogeneous, with homogeneous Dirichlet conditions $u(0,t)=u(L,t)=0$.
- Data: $L$ [m], $c$ [m/s], $V$ [m/s], $\rho$ [kg/m], $T_0=\rho c^2$ [N]. Two initial conditions are needed (second order in $t$): zero displacement, non-zero velocity.

#### Phase 2. Canonical formulation

$$u_{tt}=c^2u_{xx},\quad u(0,t)=u(L,t)=0,\quad u(x,0)=0,\quad u_t(x,0)=g(x)$$
Eigenvalue problem in $x$: $X''+\lambda X=0$, $X(0)=X(L)=0$. In $t$: $T''+\lambda c^2T=0$, with $T(0)=0$ from the zero initial displacement.

## (a) Separation and normal modes [1.25 pts]

### Hint

Put $u=X(x)T(t)$ and divide by $c^2XT$. The case analysis for $X$ is the same as for a rod with both ends at zero temperature.

### Checkpoint

- $\dfrac{T''}{c^2T}=\dfrac{X''}{X}=-\lambda$.
- $\lambda\le0$: only $X\equiv0$. $\lambda_n=\Big(\dfrac{n\pi}{L}\Big)^2$, $X_n=\sin\dfrac{n\pi x}{L}$.
- With $u(x,0)=0$: $T_n=\sin\omega_nt$, $\omega_n=\dfrac{n\pi c}{L}$.

### Solution

#### Step 1. Separation

$XT''=c^2X''T$, so $\dfrac{T''}{c^2T}=\dfrac{X''}{X}=-\lambda$ (each side depends on one variable only). Fixed ends: $X(0)T(t)=0$ for all $t$, so $X(0)=0$, and $X(L)=0$.

#### Step 2. Case lambda < 0

$\lambda=-\mu^2$: $X=a\cosh\mu x+b\sinh\mu x$; $X(0)=a=0$, $X(L)=b\sinh\mu L=0\Rightarrow b=0$.

#### Step 3. Case lambda = 0

$X=a+bx$; $X(0)=a=0$, $X(L)=bL=0\Rightarrow b=0$.

#### Step 4. Case lambda > 0

$\lambda=\mu^2$: $X=a\cos\mu x+b\sin\mu x$; $X(0)=a=0$; $b\sin\mu L=0$ with $b\ne0$ gives $\mu=n\pi/L$. Then $T''+\omega_n^2T=0$ with $\omega_n=c\sqrt{\lambda_n}=\dfrac{n\pi c}{L}$, so $T=\alpha\cos\omega_nt+\beta\sin\omega_nt$. The condition $u(x,0)=X(x)T(0)=0$ gives $\alpha=0$. The normal modes are
$$u_n(x,t)=\sin\frac{n\pi x}{L}\,\sin\frac{n\pi ct}{L},\qquad n=1,2,\dots$$

## (b) Series solution with coefficients from the velocity [1.5 pts]

### Hint

Differentiate the series with respect to $t$ and set $t=0$: $\omega_nB_n$ are the sine coefficients of $g$. The integral $\int_0^Lx(L-x)\sin(n\pi x/L)\,dx$ needs two integrations by parts.

### Checkpoint

- $\displaystyle\frac2L\int_0^L g(x)\sin\frac{n\pi x}{L}\,dx=\frac{32V}{\pi^3n^3}$ for odd $n$, $0$ for even $n$.
- $\omega_nB_n=\dfrac{32V}{\pi^3n^3}$, so $B_n=\dfrac{32VL}{c\pi^4n^4}$ for odd $n$.
- $\displaystyle u(x,t)=\frac{32VL}{c\pi^4}\sum_{n\ \mathrm{odd}}\frac{1}{n^4}\sin\frac{n\pi x}{L}\sin\frac{n\pi ct}{L}$.

### Solution

#### Step 1. Superposition and the velocity condition

$u=\sum_{n\ge1}B_n\sin\dfrac{n\pi x}{L}\sin\omega_nt$ satisfies the equation, the fixed ends and $u(x,0)=0$. Differentiating in $t$ (chain rule: $\frac{d}{dt}\sin\omega_nt=\omega_n\cos\omega_nt$):
$$u_t(x,0)=\sum_{n\ge1}\omega_nB_n\sin\frac{n\pi x}{L}=g(x)\ \Rightarrow\ \omega_nB_n=\frac2L\int_0^Lg(x)\sin\frac{n\pi x}{L}\,dx$$

#### Step 2. The integral

Let $k=n\pi/L$. First parts, $u=Lx-x^2$, $dv=\sin kx\,dx$, $du=(L-2x)dx$, $v=-\cos kx/k$:
$$\int_0^L(Lx-x^2)\sin kx\,dx=\Big[-\frac{(Lx-x^2)\cos kx}{k}\Big]_0^L+\frac1k\int_0^L(L-2x)\cos kx\,dx=\frac1k\int_0^L(L-2x)\cos kx\,dx$$
Second parts, $u=L-2x$, $dv=\cos kx\,dx$, $du=-2dx$, $v=\sin kx/k$:
$$\int_0^L(L-2x)\cos kx\,dx=\Big[\frac{(L-2x)\sin kx}{k}\Big]_0^L+\frac2k\int_0^L\sin kx\,dx=0+\frac2k\Big[-\frac{\cos kx}{k}\Big]_0^L=\frac{2(1-(-1)^n)}{k^2}$$
So $\displaystyle\int_0^Lx(L-x)\sin kx\,dx=\frac{2(1-(-1)^n)}{k^3}=\frac{2L^3(1-(-1)^n)}{\pi^3n^3}$.

#### Step 3. Coefficients

$$\omega_nB_n=\frac2L\cdot\frac{4V}{L^2}\cdot\frac{2L^3(1-(-1)^n)}{\pi^3n^3}=\frac{16V(1-(-1)^n)}{\pi^3n^3}$$
which is $\dfrac{32V}{\pi^3n^3}$ for odd $n$ and $0$ for even $n$ (the even modes have a node at the midpoint and are not excited by a velocity profile symmetric about it). Dividing by $\omega_n=n\pi c/L$:
$$B_n=\frac{32VL}{c\pi^4n^4}\ (n\ \text{odd}),\qquad u(x,t)=\frac{32VL}{c\pi^4}\sum_{n=1,3,5,\dots}\frac{1}{n^4}\sin\frac{n\pi x}{L}\sin\frac{n\pi ct}{L}$$

## (c) d'Alembert check at the midpoint [1.25 pts]

### Hint

With zero initial displacement, $u(x,t)=\dfrac1{2c}\displaystyle\int_{x-ct}^{x+ct}G(s)\,ds$, with $G$ the odd $2L$-periodic extension of $g$. For $ct\le L/2$ the interval around $L/2$ stays inside $[0,L]$, where $G=g$. Substitute $s=L/2+\sigma$.

### Checkpoint

- $u(L/2,t)=Vt-\dfrac{4Vc^2t^3}{3L^2}$ for $0\le t\le\dfrac{L}{2c}$.
- At $t=L/(2c)$: $u=\dfrac{VL}{3c}$, and the series gives $\dfrac{32VL}{c\pi^4}\sum_{n\ \mathrm{odd}}n^{-4}$.
- $\displaystyle\sum_{n\ \mathrm{odd}}\frac1{n^4}=\frac{\pi^4}{96}$.

### Solution

#### Step 1. d'Alembert's formula

The general solution of $u_{tt}=c^2u_{xx}$ is $F(x-ct)+H(x+ct)$; with $u(x,0)=0$ and $u_t(x,0)=G(x)$ it becomes $u(x,t)=\dfrac{1}{2c}\displaystyle\int_{x-ct}^{x+ct}G(s)\,ds$ (extension: the course solves the string by separation of variables; d'Alembert's form is used here only as an independent check).

#### Step 2. The integral at the midpoint

With $s=L/2+\sigma$, $ds=d\sigma$, the limits $s=L/2\mp ct$ become $\sigma=\mp ct$, and $s(L-s)=\Big(\dfrac L2+\sigma\Big)\Big(\dfrac L2-\sigma\Big)=\dfrac{L^2}{4}-\sigma^2$, so $g=V-\dfrac{4V\sigma^2}{L^2}$:
$$u\Big(\frac L2,t\Big)=\frac1{2c}\int_{-ct}^{ct}\Big(V-\frac{4V\sigma^2}{L^2}\Big)d\sigma=\frac1{2c}\Big[V\sigma-\frac{4V\sigma^3}{3L^2}\Big]_{-ct}^{ct}=\frac{1}{2c}\Big(2Vct-\frac{8Vc^3t^3}{3L^2}\Big)$$
$$u\Big(\frac L2,t\Big)=Vt-\frac{4Vc^2t^3}{3L^2},\qquad 0\le t\le\frac{L}{2c}$$
For small $t$, $u\approx Vt$: the midpoint starts with speed $V$, as imposed.

#### Step 3. Comparison with the series

At $t=L/(2c)$: d'Alembert gives $\dfrac{VL}{2c}-\dfrac{4Vc^2}{3L^2}\cdot\dfrac{L^3}{8c^3}=\dfrac{VL}{2c}-\dfrac{VL}{6c}=\dfrac{VL}{3c}$. In the series, $\sin\dfrac{n\pi}{2}\sin\dfrac{n\pi}{2}=\big((-1)^{(n-1)/2}\big)^2=1$ for odd $n$:
$$\frac{VL}{3c}=\frac{32VL}{c\pi^4}\sum_{n\ \mathrm{odd}}\frac1{n^4}\ \Rightarrow\ \sum_{n\ \mathrm{odd}}\frac1{n^4}=\frac{\pi^4}{96}$$

## (d) Energy of the modes and periodicity [1.0 pts]

### Hint

For one mode, $\int_0^L\sin^2=\int_0^L\cos^2=L/2$ and $c^2k_n^2=\omega_n^2$. Cross terms between different modes integrate to zero by orthogonality. For the total, $E(0)=\frac\rho2\int_0^Lg^2dx$.

### Checkpoint

- $E_n=\dfrac{\rho L}{4}\omega_n^2B_n^2=\dfrac{256\,\rho LV^2}{\pi^6n^6}$ ($n$ odd), constant in time.
- $E(0)=\dfrac{4\rho LV^2}{15}$, and $\sum_{n\ \mathrm{odd}}E_n=\dfrac{256\rho LV^2}{\pi^6}\cdot\dfrac{\pi^6}{960}=\dfrac{4\rho LV^2}{15}$.
- Fraction in the fundamental: $\dfrac{960}{\pi^6}\approx0.99856$.
- Period $\dfrac{2L}{c}$; at $t=L/(2c)$ the string is momentarily at rest with maximum displacement; at $t=L/c$ it crosses the rest position with velocity $-g(x)$, and $u(x,t+L/c)=-u(x,t)$.

### Solution

#### Step 1. Energy of one mode

For $u_n=B_n\sin k_nx\,\sin\omega_nt$ ($k_n=n\pi/L$): $\partial_tu_n=B_n\omega_n\sin k_nx\cos\omega_nt$, $\partial_xu_n=B_nk_n\cos k_nx\sin\omega_nt$. With $\int_0^L\sin^2k_nx\,dx=\int_0^L\cos^2k_nx\,dx=L/2$ and $T_0=\rho c^2$:
$$E_n=\frac\rho2B_n^2\omega_n^2\frac L2\cos^2\omega_nt+\frac{\rho c^2}{2}B_n^2k_n^2\frac L2\sin^2\omega_nt=\frac{\rho L}{4}\omega_n^2B_n^2$$
since $c^2k_n^2=\omega_n^2$. With $\omega_nB_n=32V/(\pi^3n^3)$: $E_n=\dfrac{\rho L}{4}\cdot\dfrac{1024V^2}{\pi^6n^6}=\dfrac{256\rho LV^2}{\pi^6n^6}$.

#### Step 2. Total energy

$E$ is conserved (the ends do no work), so $E=E(0)=\dfrac\rho2\displaystyle\int_0^L\frac{16V^2}{L^4}x^2(L-x)^2dx$. Expanding $x^2(L-x)^2=L^2x^2-2Lx^3+x^4$ and integrating: $\Big[\dfrac{L^2x^3}{3}-\dfrac{Lx^4}{2}+\dfrac{x^5}{5}\Big]_0^L=L^5\Big(\dfrac13-\dfrac12+\dfrac15\Big)=\dfrac{L^5}{30}$. Hence $E=\dfrac{8\rho V^2}{L^4}\cdot\dfrac{L^5}{30}=\dfrac{4\rho LV^2}{15}$. The modes are orthogonal, so $E=\sum E_n$, and with $\sum_{n\ \mathrm{odd}}n^{-6}=\pi^6/960$ the sum indeed gives $\dfrac{256}{960}\rho LV^2=\dfrac{4}{15}\rho LV^2$.

#### Step 3. Fraction in the fundamental

$\dfrac{E_1}{E}=\dfrac{256/\pi^6}{4/15}=\dfrac{960}{\pi^6}\approx0.99856$: a smooth, symmetric strike puts $99.86\%$ of the energy in the fundamental; the string sounds an almost pure tone of frequency $c/(2L)$.

#### Step 4. Periodicity

$\omega_n=n\omega_1$, so every term has period $2\pi/\omega_1=2L/c$ and $u(x,t+2L/c)=u(x,t)$. Only odd $n$ appear, and $\sin(\omega_nt+n\pi)=-\sin\omega_nt$ for odd $n$, hence $u(x,t+L/c)=-u(x,t)$. At $t=L/c$: $u=0$ and $u_t=\sum\omega_nB_n\sin k_nx\cos n\pi=-g(x)$: the string crosses its rest position with the velocity reversed. At $t=L/(2c)$: $\cos(n\pi/2)=0$ for odd $n$, so $u_t=0$: the string is momentarily at rest at its maximum displacement (midpoint $VL/(3c)$).

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $c\to\infty$ (very stiff string): $u\to0$, the displacement amplitude $VL/(3c)$ vanishes. Small $t$: $u\approx tg(x)$, consistent with the initial velocity. The coefficients decay as $n^{-4}$, faster than for a plucked string ($n^{-2}$), because the displacement is the time integral of a smooth velocity profile.
- **Checks:** dimensions: $B_n=\dfrac{32VL}{c\pi^4n^4}$ is $\dfrac{(\text{m/s})\,\text{m}}{\text{m/s}}=$ m; $E=\rho LV^2$ is (kg/m)(m)(m$^2$/s$^2$) $=$ J. Two independent routes (series and d'Alembert) give the same midpoint displacement $VL/(3c)$.
- **Common mistakes in the exam:** (1) keeping $\cos\omega_nt$ terms although the initial displacement is zero; (2) setting $B_n$ equal to the sine coefficients of $g$, forgetting the factor $1/\omega_n$ from differentiating in $t$; (3) using $g$ itself instead of its odd periodic extension in d'Alembert's formula when $ct>L/2$; (4) giving the period as $L/c$: that is only the half-period after which $u$ changes sign.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
