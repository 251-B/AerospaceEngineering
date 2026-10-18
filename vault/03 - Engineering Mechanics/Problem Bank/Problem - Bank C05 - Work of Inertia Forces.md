---
materia: Engineering Mechanics
tema: "Unit 5: inertia forces in rotating and accelerating frames, work and trajectories"
bank_id: C05
title: "Work of inertia forces: the Coriolis force on a rotating rod and a free particle in an accelerating frame"
category: conceptual_question
archetype: relative-motion
level: conceptual
unit: 5
difficulty: 1
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013 and 2014); not an official exercise. Verified with scripts/mechanics/c05.py"
tags:
  - problem-bank
  - midterm-1
  - inertia-forces
  - coriolis
  - relative-motion
---

# Bank C05 — Work of inertia forces

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §3.2 (velocity and acceleration in a moving frame) and §4.9 (dynamics of relative motion, inertia forces). Every number was checked with SymPy.

## Statement

$S_0$ is an inertial frame. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

## (a) Bead on a rotating rod [1.0 pts]

A straight, smooth rod lies in a horizontal plane and rotates about a fixed vertical axis through its end $O$ with constant angular velocity $\boldsymbol\Omega=\Omega\,\mathbf k$ ($\mathbf k$ upward). A bead of mass $m$ slides on the rod; $r$ is its distance to $O$, and $S_1=\{O;\mathbf e_r,\mathbf e_\varphi,\mathbf k\}$ is the frame of the rod ($\mathbf e_r$ along the rod). The bead is released at rest relative to the rod at $r=r_0$. Statement: "In $S_1$ the Coriolis force does work on the bead, and this work is what makes the relative kinetic energy of the bead grow as it slides outwards."

### Hint

Compute the power $\mathbf F\cdot\mathbf v_{rel}$ of each inertia force with $\mathbf v_{rel}=\dot r\,\mathbf e_r$.

### Checkpoint

- FALSE.
- Coriolis force $-2m\boldsymbol\Omega\times\mathbf v_{rel}=-2m\Omega\dot r\,\mathbf e_\varphi\perp\mathbf v_{rel}$: zero power, always.
- The work comes from the centrifugal force $m\Omega^2r\,\mathbf e_r$: $\tfrac12m\dot r^2=\tfrac12m\Omega^2(r^2-r_0^2)$, $r=r_0\cosh\Omega t$.
- The rod reaction $N\mathbf e_\varphi+mg\,\mathbf k$, $N=2m\Omega\dot r$: its horizontal part balances the Coriolis force in $S_1$ and its vertical part the weight; in $S_0$ it does work at the rate $2m\Omega^2r\dot r$.

### Solution

#### Step 1. Forces in $S_1$

$S_1$ rotates with constant $\boldsymbol\Omega$ about the fixed point $O$, so (Notes §4.9) $m\mathbf a_{rel}=\mathbf F+\mathbf F_{cf}+\mathbf F_{cor}$ with the centrifugal force $\mathbf F_{cf}=-m\boldsymbol\Omega\times(\boldsymbol\Omega\times r\,\mathbf e_r)=m\Omega^2r\,\mathbf e_r$ and the Coriolis force

$$\mathbf F_{cor}=-2m\,\boldsymbol\Omega\times\mathbf v_{rel}=-2m\,\Omega\,\mathbf k\times\dot r\,\mathbf e_r=-2m\Omega\dot r\,\mathbf e_\varphi$$

(no Euler term since $\dot{\boldsymbol\Omega}=\mathbf 0$). The real forces are the weight and the rod reaction, both orthogonal to $\mathbf e_r$ on a smooth rod.

#### Step 2. Powers

With $\mathbf v_{rel}=\dot r\,\mathbf e_r$: $\ \mathbf F_{cor}\cdot\mathbf v_{rel}=-2m\Omega\dot r^2\,(\mathbf e_\varphi\cdot\mathbf e_r)=0$. This holds for any motion, because $\boldsymbol\Omega\times\mathbf v_{rel}$ is perpendicular to $\mathbf v_{rel}$: **the Coriolis force never works in the moving frame.** Only the centrifugal force works, with power $m\Omega^2r\dot r$.

#### Step 3. Relative kinetic energy

Along $\mathbf e_r$: $m\ddot r=m\Omega^2r$, whose solution with $r(0)=r_0$, $\dot r(0)=0$ is $r=r_0\cosh\Omega t$. Work-energy theorem in $S_1$, with the work of the centrifugal force from $r_0$ to $r$ given by Barrow's rule:

$$\tfrac12m\dot r^2-0=\int_{r_0}^{r}m\Omega^2s\,ds=\Big[\tfrac12m\Omega^2s^2\Big]_{r_0}^{r}=\tfrac12m\Omega^2\big(r^2-r_0^2\big)$$

The growth comes from the centrifugal force; the Coriolis force only presses the bead against the rod, where the reaction $N\mathbf e_\varphi+N_z\mathbf k$ balances it: along $\mathbf e_\varphi$, $N=2m\Omega\dot r$ against the Coriolis force, and along $\mathbf k$, $N_z=mg$ against the weight $-mg\,\mathbf k$ (both components are orthogonal to the smooth rod). The statement is FALSE.

#### Step 4. Seen from $S_0$

In $S_0$ there are no inertia forces; the energy is supplied by the rod reaction $N\mathbf e_\varphi+mg\,\mathbf k$, whose power with the absolute velocity $\mathbf v=\dot r\,\mathbf e_r+\Omega r\,\mathbf e_\varphi$ is $N\Omega r=2m\Omega^2r\dot r$ (the vertical part $mg\,\mathbf k$ is orthogonal to $\mathbf v$), exactly $\frac{d}{dt}\big[\tfrac12m(\dot r^2+\Omega^2r^2)\big]$ with $\ddot r=\Omega^2r$.

## (b) Free particle in an accelerating frame [1.0 pts]

The frame $S_1$ translates without rotating, with constant acceleration $\mathbf a_{O_1}=a_0\,\mathbf e$ ($a_0>0$, $\mathbf e$ a fixed unit vector) with respect to $S_0$. A particle subject to no real force (no gravity) is observed from $S_1$. Statement: "The only inertia force in $S_1$ is $-m a_0\,\mathbf e$, and the relative trajectory of the particle is a straight line only when its initial relative velocity is zero or parallel to $\mathbf e$; otherwise it is a parabola."

### Hint

$\boldsymbol\omega_{10}=\mathbf 0$ removes Coriolis, centrifugal and Euler terms. The relative motion is that of a projectile in a uniform field $-a_0\,\mathbf e$.

### Checkpoint

- TRUE.
- $\mathbf F_{in}=-m\,\mathbf a_{O_1}=-ma_0\,\mathbf e$; $\ \mathbf r_{rel}=\mathbf r_0+\mathbf v_0t-\tfrac12a_0t^2\,\mathbf e$.
- $\mathbf v_{rel}\times\mathbf a_{rel}=-a_0\,\mathbf v_0\times\mathbf e$ (constant): the path is straight if and only if $\mathbf v_0\times\mathbf e=\mathbf 0$.
- Example $\mathbf v_0=U\mathbf j$, $\mathbf e=\mathbf i$: $x-x_0=-\dfrac{a_0}{2U^2}(y-y_0)^2$.

### Solution

#### Step 1. Inertia forces

For a frame in pure translation, $\mathbf a_{abs}=\mathbf a_{O_1}+\mathbf a_{rel}$ (Notes §3.2 with $\boldsymbol\omega=\mathbf 0$), so $m\mathbf a_{rel}=\mathbf F-m\mathbf a_{O_1}$: the only inertia force is $-ma_0\,\mathbf e$, uniform and constant. With $\mathbf F=\mathbf 0$: $\mathbf a_{rel}=-a_0\,\mathbf e$.

#### Step 2. Relative motion

Integrating twice with Barrow's rule from $0$ to $t$: $\mathbf v_{rel}=\mathbf v_0-a_0t\,\mathbf e$ and $\mathbf r_{rel}=\mathbf r_0+\mathbf v_0t-\tfrac12a_0t^2\,\mathbf e$. The path is straight exactly when $\mathbf v_{rel}$ keeps its direction, i.e. when $\mathbf v_{rel}\times\mathbf a_{rel}=\mathbf 0$ (zero curvature, Notes §2.5):

$$\mathbf v_{rel}\times\mathbf a_{rel}=(\mathbf v_0-a_0t\,\mathbf e)\times(-a_0\,\mathbf e)=-a_0\,\mathbf v_0\times\mathbf e$$

which vanishes if and only if $\mathbf v_0=\mathbf 0$ or $\mathbf v_0\parallel\mathbf e$.

#### Step 3. The parabola

With $\mathbf e=\mathbf i$ and $\mathbf v_0=U\mathbf j$: $x=x_0-\tfrac12a_0t^2$, $y=y_0+Ut$. Eliminating $t=(y-y_0)/U$ gives $x-x_0=-\dfrac{a_0}{2U^2}(y-y_0)^2$, a parabola. Both claims hold: TRUE. (In $S_0$ the same particle moves in a straight line at constant velocity.)

## Interpretation

- **Dimensional check:** $m\Omega\dot r$ and $ma_0$ are N; $m\Omega^2r^2$ is J; $a_0y^2/U^2$ is m.
- **Limits:** $\Omega\to0$ in (a) gives $r\equiv r_0$ (no driving force). $a_0\to0$ in (b) makes $S_1$ inertial and every free trajectory straight.
- **Common mistakes in the exam:** (1) attributing work to the Coriolis force (it is always normal to $\mathbf v_{rel}$); (2) adding centrifugal or Coriolis forces in a frame that only translates; (3) "a free particle moves in a straight line" in a non-inertial frame.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
