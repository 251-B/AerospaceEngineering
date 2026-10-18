---
materia: Engineering Mechanics
tema: "Units 2, 4 and 5: relative motion in a uniformly rotating frame, linearised gravity (Clohessy-Wiltshire)"
bank_id: P15
title: "Relative orbital motion near a target on a circular orbit: Clohessy-Wiltshire equations, drift and a counter-intuitive rendezvous"
category: midterm_problem
archetype: relative-motion
level: trap
unit: 5
difficulty: 3
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p15.py"
tags:
  - problem-bank
  - midterm-1
  - rotating-frame
  - coriolis
  - linearisation
  - orbital-mechanics
  - rendezvous
---

# Bank P15 — Relative orbital motion near a circular target

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §3.2 (velocity and acceleration in a moving frame), §4.9 (dynamics of relative motion, inertia forces) and §8.3 (circular orbits under the gravity of a point mass). The linearised equations obtained here are known as the Clohessy-Wiltshire (or Hill) equations: their use for rendezvous is an **extension** of the course, but every step uses only the course's tools. Every number was checked with SymPy, and the numerical case also with a nonlinear two-body integration.

## Statement

A target $T$ moves on a circular orbit of radius $R_T$ around the Earth, whose centre $O$ is the origin of the inertial frame $S_0$ and whose gravitational parameter is $\mu$ (the Earth's gravity on a mass $m$ at $\mathbf r$ is $-m\mu\,\mathbf r/|\mathbf r|^3$). The target's angular velocity is constant, $n\,\mathbf k$, with the **mean motion** $n=\sqrt{\mu/R_T^3}$ ($\mathbf k$ normal to the orbital plane). A chaser $P$ of mass $m$, subject only to the Earth's gravity, moves in the same plane close to $T$.

Use the frame $S_1=\{T;\mathbf e_x,\mathbf e_y,\mathbf k\}$ attached to the target: $\mathbf e_x$ radial, pointing away from $O$; $\mathbf e_y=\mathbf k\times\mathbf e_x$ along the target's velocity (along-track); $S_1$ rotates with $\boldsymbol\omega_{10}=n\,\mathbf k$. The relative position of the chaser is $\boldsymbol\rho=x\,\mathbf e_x+y\,\mathbf e_y$ with $|\boldsymbol\rho|\ll R_T$. Initial conditions at $t=0$: $x_0$, $y_0$, $\dot x_0$, $\dot y_0$ (relative to $S_1$).

![[attachments/EM-M1/p15-cw-relative-orbit.svg]]

## Setup

- Data: $\mu$, $R_T$, $n=\sqrt{\mu/R_T^3}$, the initial conditions. Numerical part (f): $\mu=3.986\times10^{14}$ m$^3$/s$^2$, $R_T=6778$ km (low Earth orbit), chaser 1 km behind the target ($x_0=0$, $y_0=-1000$ m).
- Hypotheses: point masses, planar motion in the orbital plane, $S_0$ inertial, no drag, no other bodies; the target's orbit is not affected by the chaser; terms of order $|\boldsymbol\rho|^2/R_T^2$ are neglected in the gravity difference.
- The frame $S_1$ has a uniformly rotating basis ($\dot{\boldsymbol\omega}_{10}=\mathbf 0$) and an accelerated origin ($\mathbf a_T=-n^2R_T\,\mathbf e_x$).

## (a) Degrees of freedom, frame and relative kinematics [1.5 pts]

How many degrees of freedom has $P$ in this planar problem? Write the absolute acceleration of $P$ in the basis of $S_1$ as the sum of the acceleration of $T$, the relative acceleration, the Coriolis and the centripetal terms, and list the inertia forces that act on $P$ in $S_1$.

### Hint

$\mathbf a_P=\mathbf a_T+\mathbf a_{rel}+2\boldsymbol\omega\times\mathbf v_{rel}+\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)+\dot{\boldsymbol\omega}\times\boldsymbol\rho$, with $\mathbf k\times\mathbf e_x=\mathbf e_y$ and $\mathbf k\times\mathbf e_y=-\mathbf e_x$.

### Checkpoint

- 2 degrees of freedom, $(x,y)$; $\boldsymbol\omega_{10}=n\mathbf k$ constant, $\mathbf a_T=-n^2R_T\,\mathbf e_x$.
- $\mathbf a_P=\big(-n^2R_T+\ddot x-2n\dot y-n^2x\big)\mathbf e_x+\big(\ddot y+2n\dot x-n^2y\big)\mathbf e_y$.
- Inertia forces in $S_1$: $-m\mathbf a_T=mn^2R_T\,\mathbf e_x$, centrifugal $mn^2\boldsymbol\rho$, Coriolis $-2mn\mathbf k\times\mathbf v_{rel}$; no Euler force.

### Solution

#### Step 1. Count

$P$ is free in the orbital plane: 2 degrees of freedom, the coordinates $(x,y)$ in $S_1$. There are no constraints and no reactions; the only force is gravity.

#### Step 2. Motion of the frame

$T$ moves on a circle of radius $R_T$ with constant angular velocity $n\mathbf k$, so its acceleration is purely centripetal: $\mathbf a_T=-n^2R_T\,\mathbf e_x$. The basis of $S_1$ turns with $\boldsymbol\omega_{10}=n\mathbf k$, and $\dot{\boldsymbol\omega}_{10}=\mathbf 0$.

Change of basis: take the inertial basis $\{\mathbf i,\mathbf j,\mathbf k\}$ of $S_0$ with $\mathbf i$ along $\overrightarrow{OT}$ at $t=0$. Then $\mathbf e_x=\cos nt\,\mathbf i+\sin nt\,\mathbf j$, $\mathbf e_y=\mathbf k\times\mathbf e_x=-\sin nt\,\mathbf i+\cos nt\,\mathbf j$, and

$$\begin{pmatrix}\mathbf e_x\\ \mathbf e_y\\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\\ \mathbf j\\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos nt&\sin nt&0\\ -\sin nt&\cos nt&0\\ 0&0&1\end{pmatrix}$$

The rows have length $\cos^2nt+\sin^2nt=1$, rows 1 and 2 are orthogonal ($-\cos nt\sin nt+\sin nt\cos nt=0$) and row 3 is $\mathbf k$, so $[R][R]^T=I$; $\det[R]=\cos^2nt+\sin^2nt=+1$. Differentiating, $\dot{\mathbf e}_x=n\,\mathbf e_y=n\mathbf k\times\mathbf e_x$ and $\dot{\mathbf e}_y=-n\,\mathbf e_x=n\mathbf k\times\mathbf e_y$ (Poisson), which confirms $\boldsymbol\omega_{10}=n\,\mathbf k$.

#### Step 3. Relative kinematics

In $S_1$: $\mathbf v_{rel}=\dot x\,\mathbf e_x+\dot y\,\mathbf e_y$, $\mathbf a_{rel}=\ddot x\,\mathbf e_x+\ddot y\,\mathbf e_y$. With $\mathbf k\times\mathbf e_x=\mathbf e_y$, $\mathbf k\times\mathbf e_y=-\mathbf e_x$:

$$2\boldsymbol\omega\times\mathbf v_{rel}=2n\big(\dot x\,\mathbf e_y-\dot y\,\mathbf e_x\big),\qquad \boldsymbol\omega\times\boldsymbol\rho=n\big(x\,\mathbf e_y-y\,\mathbf e_x\big),\qquad \boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)=-n^2\big(x\,\mathbf e_x+y\,\mathbf e_y\big)$$

The composition of accelerations (Notes §3.2), with the Euler term zero, gives

$$\mathbf a_P=\big(-n^2R_T+\ddot x-2n\dot y-n^2x\big)\,\mathbf e_x+\big(\ddot y+2n\dot x-n^2y\big)\,\mathbf e_y$$

#### Step 4. Inertia forces

Written as $m\mathbf a_{rel}=\mathbf F+\mathbf F_{in}$ (Notes §4.9), the inertia force is $\mathbf F_{in}=-m\mathbf a_T-2m\boldsymbol\omega\times\mathbf v_{rel}-m\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol\rho)$: the dragging force of the origin $mn^2R_T\,\mathbf e_x$, the centrifugal force $mn^2\boldsymbol\rho$ (about $T$) and the Coriolis force $-2mn\,\mathbf k\times\mathbf v_{rel}$. The Coriolis force is perpendicular to $\mathbf v_{rel}$ and does no work in $S_1$.

## (b) Linearised gravity and the equations of motion [2.0 pts]

Expand the gravity on $P$ to first order in $|\boldsymbol\rho|/R_T$ and obtain the two equations of relative motion. Explain why the terms in $R_T$ disappear.

### Hint

$|\mathbf r_P|^{-3}=\big[(R_T+x)^2+y^2\big]^{-3/2}=R_T^{-3}\big(1+2x/R_T+\dots\big)^{-3/2}$ and $(1+u)^{-3/2}\approx1-\tfrac32u$.

### Checkpoint

- $-\mu\,\mathbf r_P/|\mathbf r_P|^3\approx-n^2R_T\,\mathbf e_x+n^2\big(2x\,\mathbf e_x-y\,\mathbf e_y\big)$ (using $\mu=n^2R_T^3$).
- $\ddot x-2n\dot y-3n^2x=0$, $\qquad\ddot y+2n\dot x=0$.

### Solution

#### Step 1. The exact gravity

$\mathbf r_P=\overrightarrow{OT}+\boldsymbol\rho=(R_T+x)\,\mathbf e_x+y\,\mathbf e_y$ and $|\mathbf r_P|^2=R_T^2\big(1+\tfrac{2x}{R_T}+\tfrac{x^2+y^2}{R_T^2}\big)$.

#### Step 2. First-order expansion

Keeping only first-order terms, $u=2x/R_T$ and $(1+u)^{-3/2}=1-\tfrac32u+O(u^2)$:

$$\frac1{|\mathbf r_P|^3}\approx\frac1{R_T^3}\Big(1-\frac{3x}{R_T}\Big)$$

$$-\frac{\mu\,\mathbf r_P}{|\mathbf r_P|^3}\approx-\frac{\mu}{R_T^3}\Big(1-\frac{3x}{R_T}\Big)\big[(R_T+x)\,\mathbf e_x+y\,\mathbf e_y\big]\approx-\frac{\mu}{R_T^2}\,\mathbf e_x+\frac{\mu}{R_T^3}\big(2x\,\mathbf e_x-y\,\mathbf e_y\big)$$

(the product $x\cdot3x/R_T$ and $y\cdot3x/R_T$ are second order and dropped). The circular orbit of $T$ gives $n^2R_T=\mu/R_T^2$ (Notes §8.3), i.e. $\mu/R_T^3=n^2$.

#### Step 3. Newton in $S_0$, projected on the basis of $S_1$

$m\mathbf a_P=-m\mu\mathbf r_P/|\mathbf r_P|^3$ with $\mathbf a_P$ of (a):

$$\mathbf e_x:\quad -n^2R_T+\ddot x-2n\dot y-n^2x=-n^2R_T+2n^2x$$

$$\mathbf e_y:\quad \ddot y+2n\dot x-n^2y=-n^2y$$

The terms $-n^2R_T$ cancel: the gravity at $T$ is exactly what keeps $T$ (and $S_1$) on its orbit, so only the **difference** of gravity between $P$ and $T$ (the tidal term) drives the relative motion. Likewise the centrifugal term $-n^2y$ cancels the along-track gravity component. Hence

$$\ddot x-2n\dot y-3n^2x=0,\qquad \ddot y+2n\dot x=0$$

## (c) Closed-form solution [2.0 pts]

Solve the equations of (b) for the initial conditions $x_0,y_0,\dot x_0,\dot y_0$.

### Hint

The second equation is an exact derivative: $\frac{d}{dt}(\dot y+2nx)=0$. Substitute in the first to obtain a harmonic oscillator with a constant forcing; then integrate $\dot y$ with Barrow's rule.

### Checkpoint

- First integral $\dot y+2nx=C\equiv\dot y_0+2nx_0$; then $\ddot x+n^2x=2nC$.
- $x(t)=4x_0+\dfrac{2\dot y_0}{n}-\Big(3x_0+\dfrac{2\dot y_0}{n}\Big)\cos nt+\dfrac{\dot x_0}{n}\sin nt$.
- $y(t)=y_0-(6nx_0+3\dot y_0)\,t+\Big(6x_0+\dfrac{4\dot y_0}{n}\Big)\sin nt+\dfrac{2\dot x_0}{n}(\cos nt-1)$.

### Solution

#### Step 1. First integral

$\ddot y+2n\dot x=\frac{d}{dt}\big(\dot y+2nx\big)=0$. Integrating from $0$ to $t$ (Barrow): $\big[\dot y+2nx\big]_0^t=0$, so

$$\dot y+2nx=C,\qquad C=\dot y_0+2nx_0$$

#### Step 2. Radial equation

Substitute $\dot y=C-2nx$ in the radial equation: $\ddot x-2n(C-2nx)-3n^2x=0$, i.e.

$$\ddot x+n^2x=2nC$$

A particular solution is the constant $x_p=2C/n$; the homogeneous solution is $A\cos nt+B\sin nt$. The initial conditions give $x(0)=2C/n+A=x_0$ and $\dot x(0)=nB=\dot x_0$:

$$A=x_0-\frac{2C}{n}=-3x_0-\frac{2\dot y_0}{n},\qquad B=\frac{\dot x_0}{n}$$

$$x(t)=4x_0+\frac{2\dot y_0}{n}-\Big(3x_0+\frac{2\dot y_0}{n}\Big)\cos nt+\frac{\dot x_0}{n}\sin nt$$

#### Step 3. Along-track position

From Step 1, $\dot y=C-2nx=-3C-2nA\cos nt-2nB\sin nt$. Integrating from $0$ to $t$ with the antiderivatives $\int\cos n\tau\,d\tau=\frac{\sin n\tau}{n}$ and $\int\sin n\tau\,d\tau=-\frac{\cos n\tau}{n}$ (chain rule: $\frac{d}{d\tau}\sin n\tau=n\cos n\tau$) and Barrow's rule:

$$y(t)-y_0=-3Ct-2nA\Big[\frac{\sin n\tau}{n}\Big]_0^t-2nB\Big[-\frac{\cos n\tau}{n}\Big]_0^t=-3Ct-2A\sin nt+2B(\cos nt-1)$$

With $C$, $A$, $B$:

$$y(t)=y_0-(6nx_0+3\dot y_0)\,t+\Big(6x_0+\frac{4\dot y_0}{n}\Big)\sin nt+\frac{2\dot x_0}{n}(\cos nt-1)$$

Check: $x(0)=x_0$, $y(0)=y_0$, $\dot x(0)=\dot x_0$, $\dot y(0)=-6nx_0-3\dot y_0+6nx_0+4\dot y_0=\dot y_0$.

## (d) Secular drift: the trap of the lower orbit [1.5 pts]

Find the along-track drift per orbit and the condition for no drift. A chaser is placed 1 km **below** the target on its **own circular orbit** (radius $R_T-1$ km): does it keep its position below $T$? Compare with a chaser released 1 km below $T$ at rest in $S_1$.

### Hint

Only the term proportional to $t$ grows. For the circular orbit of radius $R_T+x_0$, $\dot y_0=(R_T+x_0)(n'-n)$ with $n'=\sqrt{\mu/(R_T+x_0)^3}$; expand to first order.

### Checkpoint

- $\Delta y_{orbit}=-\dfrac{2\pi}{n}\,(6nx_0+3\dot y_0)=-12\pi x_0-\dfrac{6\pi\dot y_0}{n}$; no drift iff $\dot y_0=-2nx_0$ (i.e. $C=0$).
- Own circular orbit: $\dot y_0\approx-\tfrac32nx_0$, $x\equiv x_0$, $\Delta y_{orbit}=-3\pi x_0=+9.42$ km per orbit for $x_0=-1$ km: it **moves ahead** of $T$.
- At rest in $S_1$ ($\dot y_0=0$): $\Delta y_{orbit}=-12\pi x_0=+37.70$ km per orbit.

### Solution

#### Step 1. Drift per orbit

The periodic terms of $y(t)$ repeat after one orbital period $2\pi/n$, and $x(2\pi/n)=x_0$; only the secular term changes:

$$\Delta y_{orbit}=y\Big(\frac{2\pi}n\Big)-y_0=-(6nx_0+3\dot y_0)\,\frac{2\pi}{n}=-12\pi x_0-\frac{6\pi\,\dot y_0}{n}$$

It vanishes iff $6nx_0+3\dot y_0=0$:

$$\dot y_0=-2n\,x_0\quad(C=0)$$

#### Step 2. Chaser on its own circular orbit

The circular orbit of radius $R_T+x_0$ has angular rate $n'=\sqrt{\mu/(R_T+x_0)^3}=n\,(1+x_0/R_T)^{-3/2}\approx n\big(1-\tfrac{3x_0}{2R_T}\big)$. Its velocity in $S_1$ is the absolute velocity minus the transport velocity $n\mathbf k\times\mathbf r$: $\dot y_0=(R_T+x_0)(n'-n)\approx R_T\cdot n\cdot\big(-\tfrac{3x_0}{2R_T}\big)=-\tfrac32nx_0$ (first order). Then $C=\tfrac12nx_0$, $A=-3x_0+3x_0=0$, so $x(t)=x_0$ for all $t$ and

$$y(t)=y_0-\tfrac32n\,x_0\,t,\qquad \Delta y_{orbit}=-3\pi x_0$$

For $x_0=-1000$ m: $\Delta y_{orbit}=+3000\pi=+9425$ m per orbit. **The trap:** "same circular motion, so it stays below" is wrong. The lower orbit has a shorter period (Kepler), so the chaser moves ahead of the target at $\tfrac32n|x_0|$. The no-drift value $-2nx_0$ is **not** the circular-orbit value $-\tfrac32nx_0$: the drift-free relative motion is the ellipse of (e), not a fixed point.

#### Step 3. Chaser at rest in $S_1$

With $\dot y_0=0$ (and $\dot x_0=0$): $\Delta y_{orbit}=-12\pi x_0=+12\,000\pi$ m $=+37.70$ km per orbit, while $x$ oscillates between $x_0$ and $7x_0$ ($x(t)=4x_0-3x_0\cos nt$, i.e. down to 7 km below $T$): a point "at rest" below the target is moving slower than the local circular speed and falls into an eccentric orbit.

## (e) Bounded relative orbit [1.5 pts]

For $\dot y_0=-2nx_0$, show that the relative trajectory is an ellipse centred on the along-track axis, with the along-track semi-axis twice the radial one. Find its centre, its period and its sense of motion.

### Hint

Write $x=A_e\cos(nt-\delta)$ with $A_e\cos\delta=x_0$, $A_e\sin\delta=\dot x_0/n$.

### Checkpoint

- $x=x_0\cos nt+\dfrac{\dot x_0}{n}\sin nt$, $\ y=y_c-2x_0\sin nt+\dfrac{2\dot x_0}{n}\cos nt$, $\ y_c=y_0-\dfrac{2\dot x_0}{n}$.
- $\dfrac{x^2}{A_e^2}+\dfrac{(y-y_c)^2}{4A_e^2}=1$, $A_e=\sqrt{x_0^2+\dot x_0^2/n^2}$; period $2\pi/n$; run in the sense of $-\mathbf k$ (opposite to the orbital motion).

### Solution

#### Step 1. Substitution

With $\dot y_0=-2nx_0$: $4x_0+2\dot y_0/n=0$, $3x_0+2\dot y_0/n=-x_0$, $6nx_0+3\dot y_0=0$ and $6x_0+4\dot y_0/n=-2x_0$. Then (c) gives

$$x=x_0\cos nt+\frac{\dot x_0}{n}\sin nt,\qquad y=y_0-\frac{2\dot x_0}{n}-2x_0\sin nt+\frac{2\dot x_0}{n}\cos nt$$

#### Step 2. The ellipse

With $A_e\cos\delta=x_0$, $A_e\sin\delta=\dot x_0/n$ and the addition formulas, $x=A_e\cos(nt-\delta)$ and $y-y_c=-2\big(x_0\sin nt-\tfrac{\dot x_0}{n}\cos nt\big)=-2A_e\sin(nt-\delta)$. Using $\cos^2+\sin^2=1$:

$$\frac{x^2}{A_e^2}+\frac{(y-y_c)^2}{4A_e^2}=1$$

an ellipse centred at $(0,y_c)$, with semi-axes $A_e$ (radial) and $2A_e$ (along-track), run once per orbital period $2\pi/n$.

#### Step 3. Sense of motion

The $\mathbf k$-component of $\big(x\,\mathbf e_x+(y-y_c)\,\mathbf e_y\big)\times\big(\dot x\,\mathbf e_x+\dot y\,\mathbf e_y\big)$ is $x\dot y-(y-y_c)\dot x=A_e\cos\theta\,(-2A_en\cos\theta)-(-2A_e\sin\theta)(-A_en\sin\theta)=-2nA_e^2<0$ (with $\theta=nt-\delta$): the ellipse is run in the sense of $-\mathbf k$. Above the target ($x>0$) the chaser moves backwards ($\dot y<0$), below it moves forwards: higher means slower.

## (f) A low Earth orbit case: two manoeuvres [1.5 pts]

Data: $\mu=3.986\times10^{14}$ m$^3$/s$^2$, $R_T=6778$ km; the chaser is 1 km behind the target, $x_0=0$, $y_0=-1000$ m, at rest in $S_1$, and receives an impulse at $t=0$. (i) The impulse is radial, $\dot x_0=+0.5$ m/s. Describe the motion and give the position after half an orbit and after one orbit. (ii) Which **along-track** impulse $\dot y_0$ (with $\dot x_0=0$) brings the chaser onto the target after exactly one orbit? Which way does it point, how far does the chaser go from the orbit, and with what relative velocity does it arrive?

### Hint

(i) Check the no-drift condition. (ii) With $x_0=\dot x_0=0$, $y(2\pi/n)=y_0-3\dot y_0\cdot2\pi/n$.

### Checkpoint

- $n=1.1314\times10^{-3}$ rad/s, period $2\pi/n=5553$ s $=92.6$ min.
- (i) $C=0$: bounded ellipse with $A_e=\dot x_0/n=441.9$ m, centre $y_c=-1884$ m; at half orbit $(x,y)=(0,-2768$ m$)$; after one orbit back at $(0,-1000$ m$)$: no gain.
- (ii) $\dot y_0=\dfrac{y_0\,n}{6\pi}=\dfrac{y_0}{3\cdot2\pi/n}=-0.0600$ m/s (**backwards**); $x$ reaches $4\dot y_0/n=-212.2$ m at half orbit; arrival with $\mathbf v_{rel}=\dot y_0\,\mathbf e_y$, so a braking impulse of $+0.0600$ m/s is needed. A nonlinear two-body integration misses the target by about 3 m (2.8 m).

### Solution

#### Step 1. Mean motion

$$n=\sqrt{\frac{3.986\times10^{14}}{(6.778\times10^6)^3}}=1.1314\times10^{-3}\ \text{s}^{-1},\qquad \frac{2\pi}{n}=5553\ \text{s}=92.6\ \text{min}$$

#### Step 2. Radial impulse

$x_0=0$, $\dot y_0=0$: $C=\dot y_0+2nx_0=0$, so the motion is the bounded ellipse of (e), with $A_e=\dot x_0/n=0.5/1.1314\times10^{-3}=441.9$ m:

$$x=441.9\,\sin nt\ \text{m},\qquad y=-1000+883.9\,(\cos nt-1)\ \text{m}$$

At half an orbit ($nt=\pi$): $x=0$, $y=-1000-4\cdot441.9=-2768$ m (the chaser rose and fell behind); centre of the ellipse $y_c=y_0-2\dot x_0/n=-1884$ m. After one orbit it is back at $(0,-1000)$ m: a radial impulse alone gains nothing.

#### Step 3. Along-track impulse for a one-orbit rendezvous

With $x_0=\dot x_0=0$, (c) gives $x=\frac{2\dot y_0}{n}(1-\cos nt)$ and $y=y_0-3\dot y_0t+\frac{4\dot y_0}{n}\sin nt$. At $t=2\pi/n$, $\sin2\pi=0$, $\cos2\pi=1$: $x=0$ and

$$0=y_0-3\dot y_0\,\frac{2\pi}{n}\ \Longrightarrow\ \dot y_0=\frac{y_0\,n}{6\pi}=\frac{-1000}{3\cdot5553}=-0.0600\ \text{m/s}$$

**The trap:** to catch a target 1 km **ahead**, the chaser must thrust **backwards**. The backward impulse lowers its orbit ($x$ reaches $\frac{4\dot y_0}{n}=-212.2$ m at half orbit), and the lower orbit is faster, so it gains $3|\dot y_0|\cdot2\pi/n=1000$ m in one period. A forward impulse would raise the chaser and make it fall behind.

#### Step 4. Arrival

At $t=2\pi/n$: $\dot x=2\dot y_0\sin nt=0$ and $\dot y=-3\dot y_0+4\dot y_0\cos nt=\dot y_0$. The chaser arrives at $T$ with $\mathbf v_{rel}=-0.0600\,\mathbf e_y$ m/s, so a second impulse of $+0.0600$ m/s along $\mathbf e_y$ stops it at the target (total $0.120$ m/s). A numerical integration of the full nonlinear two-body equations from the same initial state misses the target by about 3 m (2.8 m) after one orbit, consistent with neglecting terms of order $|\boldsymbol\rho|^2/R_T$.

## Interpretation

- **Dimensional check:** $n$ is s$^{-1}$ ($\mu/R^3$ is m$^3$s$^{-2}$/m$^3$); every term of $\ddot x-2n\dot y-3n^2x$ is m s$^{-2}$; $\dot y_0/n$ is m, so $x(t)$ and $y(t)$ are m; $\Delta y_{orbit}=-12\pi x_0-6\pi\dot y_0/n$ is m.
- **Limiting cases:** $\boldsymbol\rho=\mathbf 0$ with zero relative velocity stays at the origin (the target itself). $n\to0$ (no gravity, non-rotating frame): expanding $\cos nt\approx1-\tfrac12n^2t^2$ and $\sin nt\approx nt-\tfrac16n^3t^3$ in (c) gives $x\to x_0+\dot x_0t$, $y\to y_0+\dot y_0t$, uniform straight motion, as it must.
- **Physical meaning of $C$:** $C=\dot y+2nx$ is constant; it measures the difference of orbital period between chaser and target (to first order the chaser's semi-major axis differs from $R_T$ by $2C/n$). Equal periods ($C=0$) means no drift; that is why the radial impulse of (f)(i) gives a closed loop.
- **Common mistakes in the exam:** (1) forgetting the acceleration of the origin $\mathbf a_T$ or the centrifugal term, which leaves an $R_T$ term that does not cancel; (2) expanding $|\mathbf r_P|^{-3}$ with the wrong exponent ($1-2x/R_T$ instead of $1-3x/R_T$); (3) assuming that a chaser below the target on its own circular orbit, or at rest in $S_1$, keeps its relative position; (4) thrusting towards the target to catch it.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
