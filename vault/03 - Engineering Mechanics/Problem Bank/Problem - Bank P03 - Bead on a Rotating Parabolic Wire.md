---
materia: Engineering Mechanics
tema: "Units 3 and 5: smooth curve in a rotating frame, inertia forces and relative equilibrium"
bank_id: P03
title: "Bead on a parabolic wire spinning about its axis: Coriolis side force, Jacobi integral and the critical rate"
category: midterm_problem
archetype: relative-motion
level: trap
unit: 5
difficulty: 3
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p03.py"
tags:
  - problem-bank
  - midterm-1
  - rotating-frame
  - inertia-forces
  - coriolis
  - relative-equilibrium
  - stability
---

# Bank P03 — Bead on a rotating parabolic wire

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §1.5 (change of basis), §3.1 and §3.2 (derivative, velocity and acceleration in a moving frame), §4.9 (dynamics of relative motion), §6.5 (motion along a smooth curve) and §4.6 (equilibrium and stability). Every number was checked with SymPy.

## Statement

A smooth rigid wire lies in a vertical plane and has the shape of the parabola $y=x^2/(2p)$ ($p>0$), with its vertex at $O$ and its axis along the upward vertical. The wire is driven by a motor so that it spins about that vertical axis with **constant** angular rate $\Omega>0$. A bead $P$ of mass $m$ is threaded on the wire.

Let $S_0=\{O;\mathbf i_0,\mathbf j_0,\mathbf k_0\}$ be inertial ($\mathbf j_0$ vertical upward, gravity $-g\,\mathbf j_0$) and $S_1=\{O;\mathbf i_1,\mathbf j_1,\mathbf k_1\}$ be attached to the wire, with $\mathbf j_1=\mathbf j_0$, the wire in the plane $x_1y_1$ and $\boldsymbol\omega_{10}=\Omega\,\mathbf j_0$. At $t=0$ both frames coincide, so $\mathbf i_1$ has turned the angle $\theta=\Omega t$ about $\mathbf j_0$. The position of $P$ on the wire is given by its abscissa $x$ along $\mathbf i_1$ (positive or negative).

![[attachments/EM-M1/p03-parabolic-wire.svg]]

## Setup

- Data: $m$, $p$, $g$, $\Omega$. In part (g): $\Omega^2=2g/p$ and the bead is released **at rest relative to the wire** at $x_0=p/2$.
- Hypotheses: point particle, no friction, bead threaded on the wire (bilateral constraint), $S_0$ inertial.
- Write $q=\sqrt{1+x^2/p^2}$.

## (a) Degrees of freedom and frames [1.0 pts]

Count the degrees of freedom and classify the constraints in $S_0$ and in $S_1$. Write the change-of-basis matrix $[{}_0R_1]$, check it, and give $\boldsymbol\omega_{10}$ and $\boldsymbol\alpha_{10}$.

### Hint

A rotation of angle $\theta$ about $\mathbf j_0$ sends $\mathbf i_0$ to $\cos\theta\,\mathbf i_0-\sin\theta\,\mathbf k_0$.

### Checkpoint

- 1 degree of freedom, coordinate $x$. Two holonomic constraints, scleronomic in $S_1$ ($z_1=0$, $y_1=x_1^2/(2p)$), rheonomic in $S_0$.
- $[{}_0R_1]=\begin{pmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{pmatrix}$, $\det=1$, $RR^T=I$; $\boldsymbol\omega_{10}=\Omega\,\mathbf j_0$, $\boldsymbol\alpha_{10}=\mathbf 0$.

### Solution

#### Step 1. Count

In $S_1$ the wire is fixed: $z_1=0$ and $y_1-x_1^2/(2p)=0$ are two holonomic equations without time, so $3-2=1$ degree of freedom, coordinate $x$ (Notes §2.7). Seen from $S_0$ the same curve moves, so the constraints contain $t$ through $\theta=\Omega t$: rheonomic. This is why we work in $S_1$.

#### Step 2. Change of basis

The columns of $[{}_0R_1]$ are the components of $\mathbf i_1,\mathbf j_1,\mathbf k_1$ in $\mathcal B_0$ (Notes §1.5): $\mathbf i_1=\cos\theta\,\mathbf i_0-\sin\theta\,\mathbf k_0$, $\mathbf j_1=\mathbf j_0$, $\mathbf k_1=\sin\theta\,\mathbf i_0+\cos\theta\,\mathbf k_0$:

$$[{}_0R_1]=\begin{pmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{pmatrix},\qquad\det[{}_0R_1]=\cos^2\theta+\sin^2\theta=1,\qquad [{}_0R_1][{}_0R_1]^T=I$$

#### Step 3. Angular velocity

$\dot{\mathbf i}_1=\dot\theta(-\sin\theta\,\mathbf i_0-\cos\theta\,\mathbf k_0)=-\Omega\,\mathbf k_1$ and $\boldsymbol\omega\times\mathbf i_1=\Omega\,\mathbf j_1\times\mathbf i_1=-\Omega\,\mathbf k_1$ (Poisson, Notes §1.7), so $\boldsymbol\omega_{10}=\dot\theta\,\mathbf j_0=\Omega\,\mathbf j_0$, and $\boldsymbol\alpha_{10}=\dot{\boldsymbol\omega}_{10}=\mathbf 0$ because $\Omega$ is constant.

## (b) Relative and absolute kinematics [1.5 pts]

Write $\mathbf r$, $\mathbf v_{rel}$, $\mathbf a_{rel}$ in $\mathcal B_1$, and the absolute acceleration of $P$ with the Coriolis theorem.

### Hint

$y=x^2/(2p)$ gives $\dot y=x\dot x/p$ and $\ddot y=(x\ddot x+\dot x^2)/p$.

### Checkpoint

- $\mathbf v_{rel}=\dot x\Big(\mathbf i_1+\dfrac xp\mathbf j_1\Big)$, $\ \mathbf a_{rel}=\ddot x\Big(\mathbf i_1+\dfrac xp\mathbf j_1\Big)+\dfrac{\dot x^2}{p}\mathbf j_1$.
- $\mathbf a_{tr}=-\Omega^2x\,\mathbf i_1$, $\ \mathbf a_{cor}=-2\Omega\dot x\,\mathbf k_1$, $\ \mathbf a=\mathbf a_{rel}+\mathbf a_{tr}+\mathbf a_{cor}$.

### Solution

#### Step 1. Relative motion

$\mathbf r=x\,\mathbf i_1+\dfrac{x^2}{2p}\mathbf j_1$. Differentiating in $S_1$ (where $\mathbf i_1,\mathbf j_1$ are constant), with the chain rule $\dfrac{d}{dt}\dfrac{x^2}{2p}=\dfrac{x\dot x}{p}$ and the product rule $\dfrac{d}{dt}\dfrac{x\dot x}{p}=\dfrac{\dot x^2+x\ddot x}{p}$:

$$\mathbf v_{rel}=\dot x\,\mathbf i_1+\frac{x\dot x}{p}\mathbf j_1,\qquad \mathbf a_{rel}=\ddot x\,\mathbf i_1+\frac{x\ddot x+\dot x^2}{p}\mathbf j_1$$

#### Step 2. Transport and Coriolis terms

$O$ is fixed and $\boldsymbol\alpha_{10}=\mathbf 0$, so (Notes §3.2) $\mathbf a=\mathbf a_{rel}+\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)+2\boldsymbol\omega\times\mathbf v_{rel}$. With $\mathbf j_1\times\mathbf i_1=-\mathbf k_1$ and $\mathbf j_1\times\mathbf j_1=\mathbf 0$:

$$\boldsymbol\omega\times\mathbf r=-\Omega x\,\mathbf k_1,\qquad \boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)=\Omega\,\mathbf j_1\times(-\Omega x\,\mathbf k_1)=-\Omega^2x\,\mathbf i_1,\qquad 2\boldsymbol\omega\times\mathbf v_{rel}=-2\Omega\dot x\,\mathbf k_1$$

$$\mathbf a=\big(\ddot x-\Omega^2x\big)\mathbf i_1+\frac{x\ddot x+\dot x^2}{p}\mathbf j_1-2\Omega\dot x\,\mathbf k_1$$

## (c) Forces and inertia forces [1.5 pts]

Write the applied forces, the reaction of the wire and the inertia forces of $S_1$ in $\mathcal B_1$. Which of them do work in $S_1$?

### Hint

The reaction of a smooth wire is orthogonal to its tangent $\mathbf i_1+(x/p)\mathbf j_1$; one direction of the normal plane lies in the plane of the wire and the other is $\mathbf k_1$.

### Checkpoint

- $\mathbf W=-mg\,\mathbf j_1$; $\ \mathbf N=N_n\mathbf n+N_z\mathbf k_1$ with $\mathbf n=\dfrac{-(x/p)\mathbf i_1+\mathbf j_1}{q}$.
- $\mathbf F_{cf}=m\Omega^2x\,\mathbf i_1$ (potential $-\tfrac12m\Omega^2x^2$), $\ \mathbf F_{cor}=2m\Omega\dot x\,\mathbf k_1$ (no work in $S_1$).

### Solution

#### Step 1. Applied force and reaction

$\mathbf W=-mg\,\mathbf j_1$. The tangent of the wire is along $\boldsymbol\tau=\mathbf i_1+\dfrac xp\mathbf j_1$; the normal plane is spanned by the in-plane normal $\mathbf n=\dfrac1q\Big(-\dfrac xp\mathbf i_1+\mathbf j_1\Big)$ and by $\mathbf k_1$. A smooth wire gives (Notes §6.5) $\mathbf N=N_n\,\mathbf n+N_z\,\mathbf k_1$, two unknowns.

#### Step 2. Inertia forces

In $S_1$ Newton's law reads $m\mathbf a_{rel}=\mathbf W+\mathbf N+\mathbf F_{cf}+\mathbf F_{cor}$ (Notes §4.9), with

$$\mathbf F_{cf}=-m\,\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)=m\Omega^2x\,\mathbf i_1,\qquad \mathbf F_{cor}=-2m\,\boldsymbol\omega\times\mathbf v_{rel}=2m\Omega\dot x\,\mathbf k_1$$

There is no Euler term ($\boldsymbol\alpha=\mathbf 0$) and no translational term ($O$ fixed).

#### Step 3. Work in $S_1$

$\mathbf N\cdot\mathbf v_{rel}=0$ and $\mathbf F_{cor}\cdot\mathbf v_{rel}=0$ (both orthogonal to the tangent). $\mathbf W$ has potential $mgy=\dfrac{mgx^2}{2p}$ and $\mathbf F_{cf}$ has potential $V_{cf}=-\tfrac12m\Omega^2x^2$ (check: $-\dfrac{dV_{cf}}{dx}=m\Omega^2x$).

## (d) Equation of motion and reactions [2.0 pts]

Obtain the equation of motion free of reactions and the two components of the reaction.

### Hint

Project on the tangent $\boldsymbol\tau$ (no reaction), on $\mathbf k_1$ and on $q\,\mathbf n$.

### Checkpoint

- $\Big(1+\dfrac{x^2}{p^2}\Big)\ddot x+\dfrac{x}{p^2}\dot x^2=x\Big(\Omega^2-\dfrac gp\Big)$.
- $N_z=-2m\Omega\dot x$; $\ N_n=\dfrac mq\Big(\dfrac{\dot x^2}{p}+\dfrac{\Omega^2x^2}{p}+g\Big)>0$.

### Solution

#### Step 1. Tangential projection

Dot $m\mathbf a_{rel}=\mathbf W+\mathbf N+\mathbf F_{cf}+\mathbf F_{cor}$ with $\boldsymbol\tau=\mathbf i_1+\dfrac xp\mathbf j_1$. Left: $m\Big[\ddot x+\dfrac xp\cdot\dfrac{x\ddot x+\dot x^2}{p}\Big]$. Right: $\mathbf W\cdot\boldsymbol\tau=-\dfrac{mgx}{p}$, $\mathbf F_{cf}\cdot\boldsymbol\tau=m\Omega^2x$, and $\mathbf N\cdot\boldsymbol\tau=\mathbf F_{cor}\cdot\boldsymbol\tau=0$:

$$\Big(1+\frac{x^2}{p^2}\Big)\ddot x+\frac{x}{p^2}\dot x^2=x\Big(\Omega^2-\frac gp\Big)$$

#### Step 2. Out-of-plane projection

$\mathbf a_{rel}\cdot\mathbf k_1=0$, so $0=N_z+2m\Omega\dot x$:

$$N_z=-2m\Omega\dot x$$

The wire must cancel the Coriolis force. Seen from $S_0$: a bead moving outwards must gain the azimuthal speed $\Omega x$ of the wire; the drag direction of the rotation at $P$ is $\boldsymbol\omega\times\mathbf r=-\Omega x\,\mathbf k_1$, and for $x>0$, $\dot x>0$ the wire indeed pushes along $-\mathbf k_1$.

#### Step 3. In-plane normal projection

Dot with $q\,\mathbf n=-\dfrac xp\mathbf i_1+\mathbf j_1$. Left: $m\Big[-\dfrac xp\ddot x+\dfrac{x\ddot x+\dot x^2}{p}\Big]=\dfrac{m\dot x^2}{p}$. Right: $-mg$ (weight) $-\dfrac{m\Omega^2x^2}{p}$ (centrifugal) $+qN_n$:

$$N_n=\frac mq\Big(\frac{\dot x^2}{p}+\frac{\Omega^2x^2}{p}+g\Big)$$

a sum of positive terms: the wire always pushes the bead towards the concave side.

#### Step 4. Cross-check in $S_0$

As an extension (Lagrange equations are not in the course notes), the Lagrange equation of $L=\tfrac12m|\mathbf v|^2-mgy$ with the absolute velocity $\mathbf v=\mathbf v_{rel}-\Omega x\,\mathbf k_1$, $|\mathbf v|^2=q^2\dot x^2+\Omega^2x^2$, gives the same equation (checked with SymPy).

## (e) Jacobi first integral [1.0 pts]

Obtain a first integral of the motion. Is it the mechanical energy of the bead in $S_0$?

### Hint

Multiply the equation of motion by $\dot x$ and recognise exact derivatives.

### Checkpoint

- $J=\tfrac12\Big(1+\dfrac{x^2}{p^2}\Big)\dot x^2+\tfrac12\Big(\dfrac gp-\Omega^2\Big)x^2=$ const (per unit mass).
- It is the energy **in $S_1$** including the centrifugal potential; the energy in $S_0$ is not conserved (the motor works through $N_z$).

### Solution

#### Step 1. Exact derivatives

By the product and chain rules, $\dfrac{d}{dt}\Big[\tfrac12\Big(1+\dfrac{x^2}{p^2}\Big)\dot x^2\Big]=\Big(1+\dfrac{x^2}{p^2}\Big)\dot x\ddot x+\dfrac{x\dot x}{p^2}\dot x^2=\dot x\Big[\Big(1+\dfrac{x^2}{p^2}\Big)\ddot x+\dfrac{x}{p^2}\dot x^2\Big]$, and $\dot x\cdot x\Big(\Omega^2-\dfrac gp\Big)=\dfrac{d}{dt}\Big[\tfrac12\Big(\Omega^2-\dfrac gp\Big)x^2\Big]$. Integrating from $0$ to $t$ (Barrow's rule):

$$J=\frac12\Big(1+\frac{x^2}{p^2}\Big)\dot x^2+\frac12\Big(\frac gp-\Omega^2\Big)x^2=J(0)$$

#### Step 2. Meaning

$\tfrac12|\mathbf v_{rel}|^2=\tfrac12q^2\dot x^2$ and the potentials of (c): $J=\tfrac12|\mathbf v_{rel}|^2+gy-\tfrac12\Omega^2x^2$. In $S_1$ only $\mathbf W$ and $\mathbf F_{cf}$ work, so this "relative energy" is conserved. In $S_0$, $\mathbf N\cdot\mathbf v=N_z\mathbf k_1\cdot(-\Omega x\,\mathbf k_1)=2m\Omega^2x\dot x\neq0$: the motor feeds energy to the bead.

## (f) Relative equilibrium and the critical rate [1.5 pts]

Find the positions of relative equilibrium and their stability for $\Omega^2<g/p$, $\Omega^2=g/p$ and $\Omega^2>g/p$. Give the frequency of small oscillations when it exists. What happens at the critical rate?

### Hint

Effective potential $V_{eff}=\tfrac12m(g/p-\Omega^2)x^2$. At the critical rate look at $J$, not at the linearisation.

### Checkpoint

- $x=0$ is an equilibrium for every $\Omega$: stable for $\Omega^2<g/p$ ($\omega^2=g/p-\Omega^2$), unstable for $\Omega^2>g/p$.
- $\Omega^2=g/p$: **every** point of the wire is an equilibrium (neutral), and a bead with relative speed slides at constant speed along the wire: $q^2\dot x^2=$ const.

### Solution

#### Step 1. Equilibria

$\dot x=\ddot x=0$ in (d) gives $x(\Omega^2-g/p)=0$. If $\Omega^2\neq g/p$ only $x=0$ (the vertex). $V_{eff}''(0)=m(g/p-\Omega^2)$ (Notes §4.6): a minimum (stable) for $\Omega^2<g/p$, a maximum (unstable) for $\Omega^2>g/p$.

#### Step 2. Small oscillations

Linearising (d) about $x=0$ ($q\to1$, the $x\dot x^2$ term is of third order): $\ddot x+\Big(\dfrac gp-\Omega^2\Big)x=0$, so $\omega=\sqrt{g/p-\Omega^2}$ for $\Omega^2<g/p$.

#### Step 3. The critical rate (the trap)

For $\Omega^2=g/p$ the linearised equation is $\ddot x=0$, which does not decide anything by itself. The full equation becomes $q^2\ddot x+\dfrac{x}{p^2}\dot x^2=0$, so $\ddot x=0$ whenever $\dot x=0$, **at any $x$**: every point is a relative equilibrium. $J$ reduces to $\tfrac12q^2\dot x^2=|\mathbf v_{rel}|^2/2=$ const: the bead slides with constant relative speed and never comes back (neutral, not stable). Geometric reason: at relative rest the resultant of gravity and centrifugal force must be normal to the wire, i.e. $dy/dx=\Omega^2x/g$; the parabola has $dy/dx=x/p$, which matches at every $x$ exactly when $\Omega^2=g/p$ (it is the shape of the free surface of a liquid spinning at that rate).

## (g) Release at $\Omega^2=2g/p$: escape and side force [1.5 pts]

For $\Omega^2=2g/p$ and release from relative rest at $x_0=p/2$: show that the bead moves outwards, give $\dot x^2(x)$ and $N_z(x)$, their values at $x=p$ and their limits for $x\to\infty$.

### Hint

Use $J(x_0,0)=J(x,\dot x)$. The sign of $\ddot x(x_0)$ decides the direction.

### Checkpoint

- $\ddot x(x_0)=\dfrac{(g/p)\,x_0}{1+x_0^2/p^2}>0$; $\ \dot x^2=\dfrac gp\,\dfrac{x^2-x_0^2}{1+x^2/p^2}$.
- $N_z=-\dfrac{2\sqrt2\,mg}{p}\sqrt{\dfrac{x^2-x_0^2}{1+x^2/p^2}}$; at $x=p$: $\dot x^2=\tfrac38gp$, $N_z=-\sqrt3\,mg\approx-1.732\,mg$, $N_n=\dfrac{27}{8\sqrt2}mg\approx2.386\,mg$.
- $x\to\infty$: $\dot x^2\to gp$ and $|N_z|\to2\sqrt2\,mg\approx2.83\,mg$.

### Solution

#### Step 1. Direction

With $\dot x=0$ in (d): $q_0^2\ddot x=x_0\Big(\dfrac{2g}{p}-\dfrac gp\Big)=\dfrac{g x_0}{p}>0$. The bead starts outwards (the vertex is unstable, part (f)).

#### Step 2. Speed

$J(x,\dot x)=J(x_0,0)$ with $g/p-\Omega^2=-g/p$:

$$\frac12\Big(1+\frac{x^2}{p^2}\Big)\dot x^2-\frac{g}{2p}x^2=-\frac{g}{2p}x_0^2\ \Longrightarrow\ \dot x^2=\frac gp\,\frac{x^2-x_0^2}{1+x^2/p^2}$$

$\dot x^2\ge0$ only for $|x|\ge x_0$: the bead never returns towards the vertex, and $x$ grows monotonically. Consistency: $\dfrac{d(\dot x^2)}{dx}=2\ddot x$ reproduces (d) (checked with SymPy).

#### Step 3. Side force

$N_z=-2m\Omega\dot x$ with $\Omega=\sqrt{2g/p}$ and $\dot x>0$:

$$N_z=-2m\sqrt{\frac{2g}{p}}\sqrt{\frac gp\,\frac{x^2-x_0^2}{1+x^2/p^2}}=-\frac{2\sqrt2\,mg}{p}\sqrt{\frac{x^2-x_0^2}{1+x^2/p^2}}$$

#### Step 4. Values

At $x=p$ ($x_0=p/2$): $\dot x^2=\dfrac gp\cdot\dfrac{p^2-p^2/4}{2}=\dfrac38gp$, and $N_z=-2m\sqrt{\dfrac{2g}{p}}\sqrt{\dfrac{3gp}{8}}=-2mg\sqrt{\dfrac34}=-\sqrt3\,mg$. The in-plane reaction there: $\dfrac{\dot x^2}{p}+\dfrac{\Omega^2x^2}{p}+g=\dfrac38g+2g+g=\dfrac{27}{8}g$ and $q=\sqrt2$, so $N_n=\dfrac{27}{8\sqrt2}mg\approx2.386\,mg$. The relative speed is then $|\mathbf v_{rel}|^2=q^2\dot x^2=\tfrac34gp$.

#### Step 5. Limits

For $x\to\infty$, $\dfrac{x^2-x_0^2}{1+x^2/p^2}\to p^2$, so $\dot x^2\to gp$ and $|N_z|\to2\sqrt2\,mg$. The abscissa grows at a bounded rate, while the speed along the wire $q|\dot x|$ grows without bound because the wire becomes steep.

## Interpretation

- **Dimensional check:** $g/p$ and $\Omega^2$ are s$^{-2}$; in (d) every term is m s$^{-2}$ ($x\dot x^2/p^2$ is m (m/s)$^2$/m$^2$); $N_z=2m\Omega\dot x$ is kg s$^{-1}$ m s$^{-1}$ = N; $\dot x^2\to gp$ is m$^2$ s$^{-2}$.
- **Limits:** $\Omega=0$: a bead in a fixed parabolic bowl, $\omega=\sqrt{g/p}$ about the vertex and $N_z=0$; $p\to\infty$ (straight horizontal wire): always $\Omega^2>g/p$, and $x(t)$ grows as $\cosh\Omega t$, the classic rotating rod.
- **Common mistakes in the exam:** (1) forgetting $N_z$ (the reaction of a wire has two components; the Coriolis force needs one of them); (2) writing the Jacobi integral as the absolute energy (the motor does work in $S_0$); (3) at $\Omega^2=g/p$, concluding "stable" or "unstable" from $\ddot x=0$: every point is an equilibrium and a moving bead keeps a constant relative speed; (4) dropping the $(x/p^2)\dot x^2$ term, which comes from differentiating the constraint $y=x^2/(2p)$ twice.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
