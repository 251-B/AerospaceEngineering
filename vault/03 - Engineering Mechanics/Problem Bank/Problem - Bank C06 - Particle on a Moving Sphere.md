---
materia: Engineering Mechanics
tema: "Unit 3: degrees of freedom, classification of constraints and work of the reaction"
bank_id: C06
title: "Particle on a moving sphere: degrees of freedom, constraint type and the work of a smooth reaction"
category: conceptual_question
archetype: constraints
level: conceptual
unit: 3
difficulty: 1
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013 to 2016); not an official exercise. Verified with scripts/mechanics/c06.py"
tags:
  - problem-bank
  - midterm-1
  - constraints
  - degrees-of-freedom
  - reaction-forces
---

# Bank C06 — Particle on a moving sphere

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §2.7 (degrees of freedom and constraints), §6.1 to §6.4 (curves, surfaces, motion on a smooth surface) and §4.4 (power of a force). Every number was checked with SymPy.

## Statement

A rigid sphere of radius $R$ has its centre $C$ on the vertical axis $Oz$ of the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ ($\mathbf k$ upward, gravity $-g\,\mathbf k$). A motor moves the sphere without rotating it so that $\mathbf r_C=h(t)\,\mathbf k$ with the prescribed law $h(t)=H+b\sin\Omega t$ ($H$, $b$, $\Omega$ constants). A point particle $P$ of mass $m$ rests on the **outer** surface of the sphere, which is smooth, and can leave it. Use spherical coordinates about $C$: polar angle $\theta$ from the upward vertical and azimuth $\varphi$ about $Oz$, with the basis $\{\mathbf u_r,\mathbf e_\theta,\mathbf e_\varphi\}$, so that $\mathbf r_P=h\,\mathbf k+R\,\mathbf u_r$ while $P$ is in contact. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

![[attachments/EM-M1/c06-moving-sphere.svg]]

## (a) Degrees of freedom [1.0 pts]

Statement: "While $P$ is in contact with the sphere it has a single degree of freedom, because two conditions are imposed on it: it must lie on the sphere, and the sphere moves with the law $h(t)$."

### Hint

Count coordinates minus independent constraint equations **on $P$**. Is $h(t)=H+b\sin\Omega t$ an equation that restricts the position of $P$, or a known function inside the one constraint equation?

### Checkpoint

- FALSE.
- One constraint on $P$: $f(\mathbf r,t)=|\mathbf r-h(t)\mathbf k|-R=0$. The law $h(t)$ is data, not a second constraint.
- $3-1=2$ degrees of freedom while in contact, coordinates $(\theta,\varphi)$; 3 after $P$ leaves the sphere.

### Solution

#### Step 1. Coordinates and constraint equations

A free particle has 3 degrees of freedom (Notes §2.7). Contact with the sphere imposes one scalar equation on the position of $P$:

$$f(\mathbf r,t)=\sqrt{x^2+y^2+\big(z-h(t)\big)^2}-R=0$$

The motion of the sphere, $h(t)$, is a known function of time: it enters this equation but does not add another equation linking $x,y,z$. It removes no further degree of freedom.

#### Step 2. Count

$3-1=2$ degrees of freedom; $\theta$ and $\varphi$ fix the position at each instant through $\mathbf r_P=h(t)\,\mathbf k+R\,\mathbf u_r(\theta,\varphi)$. The Lagrangian in $(\theta,\varphi)$ gives two equations of motion, each with its own second derivative (their mass matrix has determinant $m^2R^4\sin^2\theta\neq0$ off the poles), which confirms two independent coordinates. The statement is FALSE.

## (b) Classification and work of the reaction [1.0 pts]

Statement: "The constraint is holonomic, rheonomic and unilateral, and although the sphere is smooth its normal reaction does work on $P$ in $S_0$."

### Hint

Write the power of $\mathbf N=N\,\mathbf u_r$ with the **absolute** velocity $\mathbf v_P=\dot h\,\mathbf k+\mathbf v_{rel}$, where $\mathbf v_{rel}$ is tangent to the sphere.

### Checkpoint

- TRUE.
- Holonomic: $f$ depends on position and time only; rheonomic: $\partial f/\partial t$ not identically zero; unilateral: $f\ge0$ (outer surface, $N\ge0$, $P$ may leave).
- $\mathbf v_P=\dot h\,\mathbf k+R\big(\dot\theta\,\mathbf e_\theta+\sin\theta\,\dot\varphi\,\mathbf e_\varphi\big)$, $\ \mathbf N\cdot\mathbf v_P=N\dot h\cos\theta=Nb\Omega\cos\Omega t\cos\theta\neq0$ in general.
- In the frame translating with $C$ the reaction does no work ($\mathbf u_r\cdot\mathbf v_{rel}=0$).

### Solution

#### Step 1. Classification (Notes §2.7)

The constraint $f(\mathbf r,t)=0$ involves positions and time but no velocities: **holonomic**. It depends explicitly on $t$ through $h(t)$, $\partial f/\partial t=-(z-h)\dot h/|\mathbf r-h\mathbf k|$, which is not identically zero (it vanishes only where $z=h$ or at the instants with $\dot h=0$): **rheonomic**. $P$ lies on the outside and can lose contact: the true condition is $f\ge0$ with $N\ge0$, an inequality: **unilateral**.

#### Step 2. Velocity of $P$

Differentiating $\mathbf r_P=h\,\mathbf k+R\,\mathbf u_r$ with $\dot{\mathbf u}_r=\dot\theta\,\mathbf e_\theta+\sin\theta\,\dot\varphi\,\mathbf e_\varphi$ (chain rule on $\mathbf u_r(\theta(t),\varphi(t))$):

$$\mathbf v_P=\dot h\,\mathbf k+R\big(\dot\theta\,\mathbf e_\theta+\sin\theta\,\dot\varphi\,\mathbf e_\varphi\big),\qquad \dot h=b\Omega\cos\Omega t$$

#### Step 3. Power of the reaction

Smooth means the reaction is normal to the surface: $\mathbf N=N\,\mathbf u_r$. With $\mathbf u_r\cdot\mathbf e_\theta=\mathbf u_r\cdot\mathbf e_\varphi=0$ and $\mathbf u_r\cdot\mathbf k=\cos\theta$:

$$\dot W_N=\mathbf N\cdot\mathbf v_P=N\dot h\cos\theta=Nb\Omega\cos(\Omega t)\cos\theta$$

At $t=0$ with $P$ at the top ($\theta=0$) it equals $Nb\Omega\neq0$. A smooth reaction does no work only against a **fixed** surface (Notes §6.4); here the surface pushes $P$ as it moves. In the frame translating with $C$ the velocity of $P$ is $\mathbf v_{rel}$, tangent to the sphere, and there $\mathbf N\cdot\mathbf v_{rel}=0$. All the claims hold: TRUE.

## Interpretation

- **Dimensional check:** $N\dot h$ is N m s$^{-1}$ = W; $f$ is a length.
- **Limits:** $b\to0$ (fixed sphere) gives a scleronomic constraint and $\dot W_N=0$: mechanical energy is then conserved. If $P$ were a bead threaded on a fixed meridian, a second constraint would leave 1 degree of freedom.
- **Common mistakes in the exam:** (1) counting a prescribed motion as an extra constraint; (2) "smooth implies no work" for a moving surface; (3) calling the constraint bilateral when the particle is only resting on the outside.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
