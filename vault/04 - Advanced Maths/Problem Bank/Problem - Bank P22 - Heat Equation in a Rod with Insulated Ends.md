---
materia: Advanced Maths
tema: "Unit 6: heat equation, separation of variables with Neumann conditions"
bank_id: P22
title: "Heat equation in a rod with insulated ends: conservation of the total heat, the zero eigenvalue, a cosine-power initial profile and the time for the midpoint to settle"
category: final_problem
archetype: pde-separation-heat-wave
level: standard
unit: 6
difficulty: 2
points: 2.5
time_minutes: 50
official: false
origen: "Problem written for the bank in the style of MATHS_FINALEXAM_2013_ORD, MATHS_FINALEXAM_2020_ORD and MATHS_FINALEXAM_2021_ORD_SOL; not an official exercise. Verified with scripts/am_bank/p22.py"
tags:
  - problem-bank
  - final-exam
  - heat-equation
  - neumann-conditions
  - zero-eigenvalue
  - conservation-of-energy
  - separation-of-variables
---

# Bank P22 — Heat equation in a rod with insulated ends

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_FINALEXAM_2013_ORD, MATHS_FINALEXAM_2020_ORD and MATHS_FINALEXAM_2021_ORD_SOL. Method: Haberman, Elementary Applied PDEs (BookPDE's.pdf, unit 5-6 theory), Sec. 1.2-1.4 (heat equation, insulated boundaries, total thermal energy and equilibrium), Sec. 2.3 (separation of variables, the three cases of the separation constant) and Sec. 2.4 (worked example: heat conduction in a rod with insulated ends). Every result was checked with SymPy (scripts/am_bank/p22.py).

## Statement

A homogeneous metal rod of length $L=0.5$ m, with lateral surface and both ends thermally insulated, has thermal diffusivity $k=1.0\times10^{-4}$ m$^2$/s. Its temperature $u(x,t)$ (in $^\circ$C) obeys

$$
u_t=k\,u_{xx},\quad 0<x<L,\ t>0,\qquad u_x(0,t)=u_x(L,t)=0,\qquad u(x,0)=20+40\cos^4\Big(\frac{\pi x}{2L}\Big).
$$

(a) Without solving the equation, prove that the total heat $H(t)=\displaystyle\int_0^Lu(x,t)\,dx$ (proportional to the thermal energy, with constant $c\rho A$) does not change in time. Deduce the uniform temperature $u_\infty$ the rod tends to, assuming it tends to a uniform temperature.

(b) Solve the problem by separation of variables. Discuss the three signs of the separation constant, including the zero eigenvalue, and write the initial profile as a finite cosine combination using a power-reduction identity.

(c) Confirm $u_\infty$ from the solution. Find the time constant of the slowest decaying mode and the time $t_{10}$ after which the deviation of the midpoint temperature $u(L/2,t)$ from $u_\infty$ has fallen to one tenth of its initial value. Give the temperatures of both ends at $t_{10}$.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $u(x,t)$ ($^\circ$C), independent variables $x\in[0,L]$ (m) and $t\ge0$ (s); $u$ is $C^2$ in $x$ and $C^1$ in $t$ for $t>0$.
- Linear, homogeneous, second-order parabolic PDE with constant coefficient $k>0$; homogeneous Neumann (insulated) conditions at both ends (Haberman Sec. 1.3); nonhomogeneous initial condition, smooth and compatible with the end conditions ($f'(0)=f'(L)=0$).
- No heat sources and no flux through the boundary.

| Symbol | Value | Unit |
| :--- | :--- | :--- |
| $L$ | $0.5$ | m |
| $k$ | $1.0\times10^{-4}$ | m$^2$/s |
| $f(x)=u(x,0)$ | $20+40\cos^4\frac{\pi x}{2L}$ | $^\circ$C |
| $f(0)$, $f(L/2)$, $f(L)$ | $60$, $30$, $20$ | $^\circ$C |

#### Phase 2. Canonical formulation

Product solutions $u=X(x)T(t)$ lead to the Sturm-Liouville problem $X''+\lambda X=0$, $X'(0)=X'(L)=0$ ($p=\sigma=1$, $q=0$) and to $T'=-\lambda kT$. The initial profile is rewritten as

$$
f(x)=A_0+\sum_{n\ge1}A_n\cos\frac{n\pi x}{L}.
$$

## (a) Conservation of the total heat and the final temperature [0.6 pts]

### Hint

Differentiate $H(t)$ under the integral sign, replace $u_t$ by $ku_{xx}$ and apply Barrow's rule to $u_{xx}=\frac{\partial}{\partial x}u_x$.

### Checkpoint

- $H'(t)=k\big[u_x(L,t)-u_x(0,t)\big]=0$, so $H(t)=H(0)$.
- $H(0)=\int_0^Lf\,dx=35L$, so $u_\infty=\dfrac1L\int_0^Lf\,dx=35\ ^\circ$C.

### Solution

#### Step 1. Derivative of the total heat

The limits $0$ and $L$ do not depend on $t$ and $u_t$ is continuous, so we may differentiate under the integral (Haberman Sec. 1.2):

$$
H'(t)=\frac{d}{dt}\int_0^Lu(x,t)\,dx=\int_0^Lu_t(x,t)\,dx=k\int_0^Lu_{xx}(x,t)\,dx .
$$

An antiderivative of $u_{xx}$ with respect to $x$ is $u_x$, so by Barrow's rule

$$
H'(t)=k\big[u_x(x,t)\big]_{x=0}^{x=L}=k\big(u_x(L,t)-u_x(0,t)\big)=k(0-0)=0 .
$$

Hence $H(t)=H(0)$ for all $t$: insulated ends let no heat in or out (Haberman Sec. 1.4).

#### Step 2. Initial total heat

With $\cos^4\theta=\frac{3+4\cos2\theta+\cos4\theta}{8}$ (proved in (b), Step 4) and $\theta=\frac{\pi x}{2L}$, $f=35+20\cos\frac{\pi x}{L}+5\cos\frac{2\pi x}{L}$. For $n\ge1$, with $s=\frac{n\pi x}{L}$, $ds=\frac{n\pi}{L}dx$:

$$
\int_0^L\cos\frac{n\pi x}L\,dx=\frac{L}{n\pi}\Big[\sin s\Big]_0^{n\pi}=\frac{L}{n\pi}\big(\sin n\pi-\sin0\big)=0 .
$$

So $H(0)=\int_0^L35\,dx=35L$.

#### Step 3. Final temperature

If $u\to u_\infty$ (a constant) as $t\to\infty$, then $H\to u_\infty L$; but $H=35L$ for all $t$, so

$$
u_\infty=\frac1L\int_0^Lf(x)\,dx=35\ ^\circ\text{C},
$$

the mean of the initial temperature, not the mean $40\ ^\circ$C of the end values $60$ and $20$.

## (b) Separation of variables and the solution [1.3 pts]

### Hint

Substitute $u=XT$, divide by $kXT$. For the Neumann problem the case $\lambda=0$ gives a nontrivial eigenfunction. Write $\cos^4\theta=(\cos^2\theta)^2$ with $\cos^2\theta=\frac{1+\cos2\theta}2$, twice.

### Checkpoint

- $\lambda<0$: trivial; $\lambda_0=0$: $X_0=1$; $\lambda_n=\big(\frac{n\pi}L\big)^2$: $X_n=\cos\frac{n\pi x}L$, $T_n=e^{-k(n\pi/L)^2t}$.
- $f(x)=35+20\cos\dfrac{\pi x}{L}+5\cos\dfrac{2\pi x}{L}$.
- $u(x,t)=35+20\,e^{-k\pi^2t/L^2}\cos\dfrac{\pi x}L+5\,e^{-4k\pi^2t/L^2}\cos\dfrac{2\pi x}L$.

### Solution

#### Step 1. Separation

With $u=X(x)T(t)$: $XT'=kX''T$; dividing by $kXT$,

$$
\frac{T'}{kT}=\frac{X''}{X}=-\lambda .
$$

The end conditions give $X'(0)T(t)=0$ and $X'(L)T(t)=0$, so $X'(0)=X'(L)=0$ for a nontrivial $T$.

#### Step 2. The three cases for $X''+\lambda X=0$

- $\lambda=-\mu^2<0$: $X=A\cosh\mu x+B\sinh\mu x$, $X'=\mu(A\sinh\mu x+B\cosh\mu x)$. $X'(0)=\mu B=0\Rightarrow B=0$. $X'(L)=\mu A\sinh\mu L=0$ with $\sinh\mu L>0$, so $A=0$: trivial.
- $\lambda=0$: $X=A+Bx$, $X'=B$; $X'(0)=B=0$ and $X'(L)=0$ holds for any $A$. Eigenvalue $\lambda_0=0$ with $X_0=1$: the constant temperature is an equilibrium of the insulated rod (Haberman Sec. 2.4).
- $\lambda=\mu^2>0$: $X=A\cos\mu x+B\sin\mu x$, $X'=\mu(-A\sin\mu x+B\cos\mu x)$. $X'(0)=\mu B=0\Rightarrow B=0$. $X'(L)=-\mu A\sin\mu L=0$ with $A\neq0$, so $\sin\mu L=0$, $\mu=\frac{n\pi}{L}$: $\lambda_n=\big(\frac{n\pi}L\big)^2$, $X_n=\cos\frac{n\pi x}L$, $n=1,2,\dots$

#### Step 3. Time factors

$T'=-\lambda_nkT$ is separable: for $T\neq0$, $\frac{dT}{T}=-\lambda_nk\,dt$, integrate from $0$ to $t$ with Barrow's rule, $\ln\lvert T(t)\rvert-\ln\lvert T(0)\rvert=-\lambda_nkt$, so $T_n(t)=T_n(0)e^{-\lambda_nkt}$. For $n=0$, $T_0$ is constant. By superposition (Haberman Sec. 2.2):

$$
u(x,t)=A_0+\sum_{n=1}^\infty A_n\,e^{-k(n\pi/L)^2t}\cos\frac{n\pi x}{L}.
$$

#### Step 4. Initial profile as a finite cosine sum

With $\cos^2\theta=\frac{1+\cos2\theta}{2}$ applied twice:

$$
\cos^4\theta=\Big(\frac{1+\cos2\theta}2\Big)^2=\frac{1+2\cos2\theta+\cos^22\theta}{4}=\frac14\Big(1+2\cos2\theta+\frac{1+\cos4\theta}2\Big)=\frac{3+4\cos2\theta+\cos4\theta}{8}.
$$

With $\theta=\frac{\pi x}{2L}$: $2\theta=\frac{\pi x}L$, $4\theta=\frac{2\pi x}L$, and

$$
f(x)=20+40\cdot\frac{3+4\cos\frac{\pi x}L+\cos\frac{2\pi x}L}{8}=20+15+20\cos\frac{\pi x}{L}+5\cos\frac{2\pi x}{L}.
$$

Check: $f(0)=35+20+5=60$, $f(L/2)=35+0-5=30$, $f(L)=35-20+5=20$, as in the data table.

#### Step 5. Coefficients and solution

$f$ is already a combination of eigenfunctions, so matching $u(x,0)=f$ term by term (orthogonality of $\cos\frac{n\pi x}L$ on $[0,L]$, Haberman Sec. 2.4: $A_0=\frac1L\int_0^Lf$, $A_n=\frac2L\int_0^Lf\cos\frac{n\pi x}L$) gives $A_0=35$, $A_1=20$, $A_2=5$ and $A_n=0$ for $n\ge3$:

$$
u(x,t)=35+20\,e^{-k\pi^2t/L^2}\cos\frac{\pi x}L+5\,e^{-4k\pi^2t/L^2}\cos\frac{2\pi x}L .
$$

Verification: $u_t=-\frac{20k\pi^2}{L^2}e^{-k\pi^2t/L^2}\cos\frac{\pi x}L-\frac{20k\pi^2}{L^2}e^{-4k\pi^2t/L^2}\cos\frac{2\pi x}L$ and, by the chain rule, $ku_{xx}=k\Big[-20\frac{\pi^2}{L^2}e^{-k\pi^2t/L^2}\cos\frac{\pi x}L-5\frac{4\pi^2}{L^2}e^{-4k\pi^2t/L^2}\cos\frac{2\pi x}L\Big]$, the same expression. $u_x$ contains only $\sin\frac{\pi x}L$ and $\sin\frac{2\pi x}L$, which vanish at $x=0$ and $x=L$.

## (c) Final state and settling times [0.6 pts]

### Hint

At $x=L/2$ the first mode vanishes, because $\cos\frac\pi2=0$. Only the second mode is left there.

### Checkpoint

- $u\to35\ ^\circ$C; slowest time constant $\tau_1=\dfrac{L^2}{k\pi^2}\approx253.3$ s ($\tau_2=\tau_1/4\approx63.3$ s).
- $u(L/2,t)=35-5e^{-4k\pi^2t/L^2}$; $t_{10}=\dfrac{L^2\ln10}{4\pi^2k}\approx145.8$ s.
- At $t_{10}$: $u(0)=35+20\cdot10^{-1/4}+0.5\approx46.75\ ^\circ$C, $u(L)\approx24.25\ ^\circ$C.

### Solution

#### Step 1. Long-time limit

Both exponents are negative, so as $t\to\infty$ the two modes vanish and $u\to A_0=35\ ^\circ$C, the value predicted in (a) from conservation alone. The zero eigenvalue is the reason: its mode does not decay, and its amplitude is the mean of $f$.

#### Step 2. Time constants

Mode $n$ decays as $e^{-t/\tau_n}$ with $\tau_n=\dfrac{L^2}{k n^2\pi^2}$. The slowest is $n=1$:

$$
\tau_1=\frac{(0.5)^2}{(1.0\times10^{-4})\pi^2}=\frac{0.25}{9.870\times10^{-4}}\approx253.3\ \text{s},\qquad \tau_2=\frac{\tau_1}4\approx63.3\ \text{s}.
$$

#### Step 3. Midpoint

At $x=L/2$: $\cos\frac\pi2=0$ and $\cos\pi=-1$, so $u(L/2,t)=35-5e^{-4k\pi^2t/L^2}$. The midpoint starts at $30\ ^\circ$C and warms monotonically to $35\ ^\circ$C; its deviation $5e^{-4k\pi^2t/L^2}$ is governed by the faster mode only. One tenth of the initial deviation:

$$
e^{-4k\pi^2t_{10}/L^2}=\frac1{10}\iff\frac{4k\pi^2t_{10}}{L^2}=\ln10\iff t_{10}=\frac{L^2\ln10}{4\pi^2k}=\frac{0.25\cdot2.3026}{4\pi^2\cdot10^{-4}}\approx145.8\ \text{s}.
$$

#### Step 4. Ends at $t_{10}$

$t_{10}/\tau_1=\frac{\ln10}{4}$, so $e^{-t_{10}/\tau_1}=10^{-1/4}\approx0.5623$, and the second mode equals $5\cdot\frac1{10}=0.5$. At $x=0$ (both cosines $=1$): $u=35+20(0.5623)+0.5\approx46.75\ ^\circ$C. At $x=L$ ($\cos\pi=-1$, $\cos2\pi=1$): $u=35-11.25+0.5\approx24.25\ ^\circ$C. The ends are still far from equilibrium when the midpoint has almost settled: the midpoint is a node of the slow mode.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $t\to0^+$ reproduces $f$ (Step 4 of (b)); $t\to\infty$ gives the mean $35\ ^\circ$C; for $t\gg\tau_2$, $u-35\approx20e^{-t/\tau_1}\cos\frac{\pi x}{L}$, a single half cosine with the hot end at $x=0$. Doubling $L$ multiplies all times by $4$ (diffusive scaling $t\sim L^2/k$).
- **Checks:** dimensions: $k\pi^2t/L^2$ has (m$^2$/s)(s)/m$^2$, dimensionless; $\tau_1=L^2/(k\pi^2)$ is in s. $H(t)=35L$ for all $t$ computed directly from the solution (script). The PDE, both Neumann conditions and the initial condition hold (script); the coefficients also follow from the integrals $\frac1L\int f$ and $\frac2L\int f\cos\frac{n\pi x}L$ with the original $\cos^4$ form.
- **Common mistakes in the exam:** (1) forgetting the $\lambda=0$ eigenvalue and its constant mode, which gives a rod that cools to $0\ ^\circ$C although no heat can leave; (2) using sines $\sin\frac{n\pi x}L$ (the Dirichlet eigenfunctions); (3) taking the final temperature as the average of the end values, $40\ ^\circ$C, instead of the spatial mean $35\ ^\circ$C; (4) computing $t_{10}$ with the slow rate $k\pi^2/L^2$ at the midpoint, where that mode is absent ($t$ would come out four times too large, $583$ s).

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
