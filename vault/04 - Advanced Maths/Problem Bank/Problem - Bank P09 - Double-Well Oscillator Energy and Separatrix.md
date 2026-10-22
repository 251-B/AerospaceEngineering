---
materia: Advanced Maths
tema: "Unit 4: nonlinear systems, conservative second-order equations"
bank_id: P09
title: "Conservative double-well oscillator x'' = 4x - x^3: linearisation, first integral, true centres, the figure-eight separatrix and the orbit types by energy"
category: midterm_2_problem
archetype: nonlinear-systems-stability
level: standard
unit: 4
difficulty: 2
points: 5.0
time_minutes: 45
official: false
origen: "Problem written for the bank in the style of MATHS_SECONDPARTIAL_2020_G46_SOL and MATHS_SECONDPARTIAL_2025_G46_SOL; not an official exercise. Verified with scripts/am_bank/p09.py"
tags:
  - problem-bank
  - midterm-2
  - conservative-systems
  - first-integral
  - separatrix
  - homoclinic-orbit
  - nonlinear-centre
---

# Bank P09 — Double-well oscillator, energy and separatrix

> [!info] Practice item, not an official exercise
> Written for the bank in the style of MATHS_SECONDPARTIAL_2020_G46_SOL and MATHS_SECONDPARTIAL_2025_G46_SOL. Method: Robinson Sec. 34.1 (one-dimensional conservative systems, energy and potential), Sec. 32.4 (stationary points, linearisation, Hartman-Grobman) and Ch. 35 (the pendulum as a model of level-set analysis). Every result was checked with SymPy (scripts/am_bank/p09.py).

## Statement

A particle of unit mass moves on a line under the force $4x-x^3$:

$$x''=4x-x^3.$$

(a) Write the equation as a first-order system for $(x,y)$ with $y=x'$, and find the potential $V(x)$ with $x''=-V'(x)$ and $V(0)=0$. Find the equilibria and classify them by linearisation. Which conclusions can be transferred to the nonlinear system?

(b) Prove, by differentiating along solutions, that $E(x,y)=\tfrac12y^2+V(x)$ is constant on every orbit. Use it to show that the equilibria that are linear centres are true (nonlinear) centres, and give the sense of rotation around them.

(c) Find the explicit equation of the separatrix, the level set of $E$ through the saddle, and its extent in $x$ and $y$. Verify that $x(t)=2\sqrt2\,\operatorname{sech}(2t)$ solves the equation with $x(0)=2\sqrt2$, $x'(0)=0$, and explain why this solution never reaches the saddle in finite time.

(d) Determine the ranges of $E$ for which the orbits are: equilibria, closed orbits inside one well, the separatrix, closed orbits around all three equilibria. Give the turning points as functions of $E$ and describe the phase portrait.

## Setup

#### Phase 1. Hypotheses and setup

- Unknown $x(t)$, $t\in\mathbb R$. Second-order, autonomous, **nonlinear** (cubic term), no damping. The right-hand side is $C^1$, so solutions exist and are unique (Picard).
- The force does not depend on $x'$: the system is conservative (Robinson Sec. 34.1), and the energy will organise the whole portrait.
- Symmetries: the force is odd, so $V$ is even and the portrait is symmetric under $x\mapsto-x$; replacing $(y,t)$ by $(-y,-t)$ leaves the equation unchanged, so the portrait is symmetric under $y\mapsto-y$ with arrows reversed.

#### Phase 2. Canonical formulation

$$x'=y,\qquad y'=4x-x^3=-V'(x),\qquad V(x)=\frac{x^4}{4}-2x^2.$$

## (a) System, potential, equilibria and linearisation [1.5 pts]

### Hint

$V(x)=-\int_0^x(4s-s^3)\,ds$. The Jacobian of $(y,-V'(x))$ is $\begin{pmatrix}0&1\\-V''(x)&0\end{pmatrix}$.

### Checkpoint

- $V=\dfrac{x^4}{4}-2x^2$, $V(0)=0$, $V(\pm2)=-4$.
- Equilibria $(0,0)$, $(2,0)$, $(-2,0)$.
- $(0,0)$: $\begin{pmatrix}0&1\\4&0\end{pmatrix}$, $\lambda=\pm2$, eigenvectors $(1,2)$ (unstable), $(1,-2)$ (stable): saddle, also for the nonlinear system.
- $(\pm2,0)$: $\begin{pmatrix}0&1\\-8&0\end{pmatrix}$, $\lambda=\pm2\sqrt2\,i$: linear centres, non-hyperbolic, linearisation inconclusive.

### Solution

#### Step 1. Potential

$$V(x)=-\int_0^x(4s-s^3)\,ds=-\Big[2s^2-\frac{s^4}{4}\Big]_0^x=-\Big(2x^2-\frac{x^4}{4}\Big)+0=\frac{x^4}{4}-2x^2,$$

using Barrow's rule. Check: $V'(x)=x^3-4x=-(4x-x^3)$. It is a double well: $V$ has a local maximum $V(0)=0$ and two minima $V(\pm2)=4-8=-4$.

#### Step 2. Equilibria

$y=0$ and $4x-x^3=x(2-x)(2+x)=0$: $(0,0)$, $(2,0)$, $(-2,0)$, the critical points of $V$.

#### Step 3. Linearisation

$D\mathbf F=\begin{pmatrix}0&1\\4-3x^2&0\end{pmatrix}$, with $V''(x)=3x^2-4$.

- At $(0,0)$: $\begin{pmatrix}0&1\\4&0\end{pmatrix}$, $\det(D\mathbf F-\lambda I)=\lambda^2-4$, $\lambda=\pm2$. For $\lambda=2$, row 1: $-2v_1+v_2=0$, $\mathbf v=(1,2)$; for $\lambda=-2$: $2v_1+v_2=0$, $\mathbf v=(1,-2)$. Real eigenvalues of opposite sign: a **saddle**.
- At $(\pm2,0)$: $4-12=-8$, $\begin{pmatrix}0&1\\-8&0\end{pmatrix}$, $\lambda^2+8=0$, $\lambda=\pm2\sqrt2\,i$: a **linear centre**, with small-oscillation period $2\pi/(2\sqrt2)=\pi/\sqrt2$.

#### Step 4. What transfers

The saddle is hyperbolic, so by the Hartman-Grobman theorem (Robinson Sec. 32.4.3) the nonlinear system has a saddle at the origin with stable and unstable curves tangent to $(1,-2)$ and $(1,2)$. The centres are not hyperbolic (zero real part): a small nonlinear term could turn them into weak foci, so the linearisation alone decides nothing. Part (b) settles it.

## (b) First integral and true centres [1.5 pts]

### Hint

Chain rule: $\frac{d}{dt}E(x(t),y(t))=E_x\,x'+E_y\,y'$. Look at $E$ near $(2,0)$ as a function of two variables.

### Checkpoint

- $\dfrac{dE}{dt}=V'(x)\,y+y\,(-V'(x))=0$.
- $E$ has a strict local minimum $-4$ at $(\pm2,0)$ (Hessian $\operatorname{diag}(8,1)$): level sets $E=c$, $-4<c<0$, are closed curves around each minimum, so the orbits are periodic: **true centres**.
- Rotation clockwise (at $(2,1)$: $x'=1>0$).

### Solution

#### Step 1. Conservation

Along a solution, by the chain rule,

$$\frac{d}{dt}E(x(t),y(t))=\frac{\partial E}{\partial x}x'+\frac{\partial E}{\partial y}y'=V'(x)\,y+y\,\big(-V'(x)\big)=0.$$

Explicitly: $(x^3-4x)y+y(4x-x^3)=0$. So $E$ is a first integral and every orbit lies on one level set $\tfrac12y^2+\tfrac{x^4}{4}-2x^2=E_0$.

#### Step 2. Shape of E near the centres

$E_x=V'(x)$, $E_y=y$ vanish at $(2,0)$, and the Hessian there is $\begin{pmatrix}V''(2)&0\\0&1\end{pmatrix}=\begin{pmatrix}8&0\\0&1\end{pmatrix}$, positive definite: $E$ has a strict local minimum $E(2,0)=-4$. Near it, $E\approx-4+4(x-2)^2+\tfrac12y^2$, so for $c$ slightly above $-4$ the level set $E=c$ is a small closed oval around $(2,0)$.

#### Step 3. Orbits on those level sets are periodic

More precisely, for $-4<c<0$ the right-well part of $\{E=c\}$ is $y=\pm\sqrt{2(c-V(x))}$ for $x\in[x_-,x_+]$, the interval where $V\le c$ (found in (d)): one closed curve, symmetric in $y$, meeting $y=0$ only at the turning points. It contains no equilibrium ($V'(x_\pm)\neq0$), so the speed never vanishes on it and the solution goes round it in a finite time and repeats: every nearby orbit is closed. The equilibria $(\pm2,0)$ are therefore **true centres** of the nonlinear system (Robinson Sec. 34.1), by symmetry also $(-2,0)$.

#### Step 4. Sense of rotation

At $(2,1)$, above the centre, $(x',y')=(1,\ 4\cdot2-8)=(1,0)$: the motion is to the right on top, so the orbits are travelled **clockwise**, as for every conservative system written with $y=x'$ ($x$ increases where $y>0$).

## (c) Separatrix and the homoclinic solution [1.0 pts]

### Hint

The saddle has $E=V(0)=0$. For the verification use $\frac{d}{dt}\operatorname{sech}u=-\operatorname{sech}u\tanh u\,\frac{du}{dt}$ and $\tanh^2=1-\operatorname{sech}^2$.

### Checkpoint

- Separatrix $E=0$: $y^2=\dfrac{x^2(8-x^2)}{2}$, i.e. $y=\pm x\sqrt{\dfrac{8-x^2}{2}}$, for $\lvert x\rvert\le2\sqrt2$: a figure eight through the origin.
- Tangents at the origin $y=\pm2x$ (the saddle eigenvectors); maximum $\lvert y\rvert=2\sqrt2$ at $x=\pm2$.
- $x(t)=2\sqrt2\operatorname{sech}2t$: $x''=8\sqrt2\operatorname{sech}2t-16\sqrt2\operatorname{sech}^32t=4x-x^3$; $x\to0$ only as $t\to\pm\infty$.

### Solution

#### Step 1. Level set through the saddle

$E(0,0)=0$. Then $\tfrac12y^2+\tfrac{x^4}{4}-2x^2=0$ gives

$$y^2=4x^2-\frac{x^4}{2}=\frac{x^2(8-x^2)}{2},\qquad y=\pm x\sqrt{\frac{8-x^2}{2}}.$$

Real only for $x^2\le8$, i.e. $\lvert x\rvert\le2\sqrt2$, where $V(\pm2\sqrt2)=\frac{64}{4}-16=0$. Near $x=0$, $y\approx\pm x\sqrt4=\pm2x$: the separatrix leaves the origin along the eigenvectors $(1,\pm2)$ found in (a). It is a figure eight: one loop in $x>0$ around $(2,0)$, its mirror image in $x<0$.

#### Step 2. Height of the loops

$g(x)=\frac{x^2(8-x^2)}{2}=4x^2-\frac{x^4}{2}$, $g'(x)=8x-2x^3=2x(4-x^2)=0$ at $x=\pm2$, with $g(2)=16-8=8$. So $\lvert y\rvert\le2\sqrt2$, reached above and below the centres.

#### Step 3. Verification of the homoclinic solution

Let $x=2\sqrt2\operatorname{sech}u$ with $u=2t$, $\frac{du}{dt}=2$. By the chain rule

$$x'=2\sqrt2\,(-\operatorname{sech}u\tanh u)\cdot2=-4\sqrt2\operatorname{sech}u\tanh u.$$

Product rule, with $\frac{d}{dt}\tanh u=2\operatorname{sech}^2u$:

$$x''=-4\sqrt2\big[(-2\operatorname{sech}u\tanh u)\tanh u+\operatorname{sech}u\,(2\operatorname{sech}^2u)\big]=8\sqrt2\operatorname{sech}u\tanh^2u-8\sqrt2\operatorname{sech}^3u.$$

With $\tanh^2u=1-\operatorname{sech}^2u$: $x''=8\sqrt2\operatorname{sech}u-16\sqrt2\operatorname{sech}^3u$. On the other side, $4x-x^3=8\sqrt2\operatorname{sech}u-(2\sqrt2)^3\operatorname{sech}^3u=8\sqrt2\operatorname{sech}u-16\sqrt2\operatorname{sech}^3u$. They agree. Initial data: $\operatorname{sech}0=1$, $\tanh0=0$, so $x(0)=2\sqrt2$ and $x'(0)=0$; $E=0+V(2\sqrt2)=0$, the solution is on the separatrix.

#### Step 4. Infinite time

$\operatorname{sech}2t>0$ for every real $t$ and $\operatorname{sech}2t\to0$ only as $t\to\pm\infty$: the solution leaves the origin at $t=-\infty$ along $(1,2)$, reaches the turning point $x=2\sqrt2$ at $t=0$ and returns to the origin at $t=+\infty$ along $(1,-2)$. It is a **homoclinic orbit**. It cannot reach $(0,0)$ in finite time, because $(0,0)$ is itself a solution and uniqueness forbids two solutions to meet. Its speed is largest when $\operatorname{sech}^2u=\tfrac12$, with $\lvert x'\rvert=4\sqrt2\cdot\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}=2\sqrt2$, as in Step 2.

## (d) Energy ranges, turning points and portrait [1.0 pts]

### Hint

Turning points satisfy $V(x)=E$, a quadratic equation in $X=x^2$.

### Checkpoint

- $E<-4$: no orbit; $E=-4$: the centres $(\pm2,0)$.
- $-4<E<0$: two closed orbits, one per well, between $x^2=4-2\sqrt{4+E}$ and $x^2=4+2\sqrt{4+E}$ (e.g. $E=-3$: $\sqrt2\le\lvert x\rvert\le\sqrt6$).
- $E=0$: the saddle and the two homoclinic loops.
- $E>0$: one closed orbit around all three equilibria, turning points $x=\pm\sqrt{4+2\sqrt{4+E}}$, crossing $x=0$ with $y=\pm\sqrt{2E}$ (e.g. $E=5$: $x=\pm\sqrt{10}$, $y=\pm\sqrt{10}$).

### Solution

#### Step 1. Admissible energies

$E=\tfrac12y^2+V(x)\ge V(x)\ge-4$. So $E<-4$ gives an empty level set, and $E=-4$ forces $y=0$, $V(x)=-4$: the two centres.

#### Step 2. Turning points

At a turning point $y=0$ and $V(x)=E$: $\frac{x^4}{4}-2x^2-E=0$, i.e. $X^2-8X-4E=0$ with $X=x^2$. The quadratic formula gives

$$X=\frac{8\pm\sqrt{64+16E}}{2}=4\pm2\sqrt{4+E}.$$

- For $-4<E<0$: $0<2\sqrt{4+E}<4$, so both roots are positive and $x^2\in[\,4-2\sqrt{4+E},\ 4+2\sqrt{4+E}\,]$ gives two disjoint intervals of $x$, one in each well: two closed orbits (one around each centre).
- For $E>0$: $4-2\sqrt{4+E}<0$ is rejected; the only turning points are $x=\pm\sqrt{4+2\sqrt{4+E}}$, and the level set is one closed curve surrounding all three equilibria, crossing $x=0$ where $\tfrac12y^2=E$.

#### Step 3. Portrait

Inside each loop of the figure eight there is a family of nested clockwise ovals around $(\pm2,0)$, shrinking to the centre as $E\to-4^+$ and growing to the loop as $E\to0^-$ (their period tends to infinity there). Outside the figure eight there are large clockwise closed curves, peanut-shaped (pinched at $x=0$) for $E$ slightly above $0$, and close to the quartic curves $\tfrac12y^2+\tfrac{x^4}{4}=E$ for large $E$. Every orbit except the equilibria and the separatrix is periodic; there are no attractors, as expected without damping.

## Interpretation

#### Phase 4. Asymptotic and physical checks

- **Limits:** $E\to-4^+$: small ellipses $4(x-2)^2+\tfrac12y^2=E+4$, period $\to\pi/\sqrt2$ (the linear value). $E\to0$: the period grows without bound (the orbit lingers near the saddle). $E\to\infty$: $V\approx x^4/4$ dominates and the amplitude grows like $(4E)^{1/4}$.
- **Checks:** $dE/dt=0$ identically; the separatrix leaves the origin with slopes $\pm2$, matching the saddle eigenvectors; the homoclinic solution has $E=0$ and maximum speed $2\sqrt2$, matching the height of the loop. Dimensions, if $x$ is in metres and $t$ in seconds: the coefficients 4 and 1 carry s$^{-2}$ and m$^{-2}$s$^{-2}$, and $E$ is an energy per unit mass, m$^2$s$^{-2}$.
- **Common mistakes in the exam:** (1) stating that the linear centres are centres of the nonlinear system "by Hartman-Grobman": that theorem does not apply to non-hyperbolic points, the first integral is needed; (2) a sign error in $V$ (taking $V'=4x-x^3$), which turns minima into maxima and swaps saddles and centres; (3) forgetting the root $X=4-2\sqrt{4+E}$ and describing one orbit instead of two for $-4<E<0$; (4) drawing the separatrix as crossing itself transversally at angles other than those of the eigenvectors $(1,\pm2)$.

**Back to:** [[Problem Set - Advanced Maths Problem Bank]]
