---
materia: Engineering Mechanics
tema: "Unit 1: intrinsic kinematics of a 3D trajectory in cylindrical coordinates"
bank_id: C01
title: "Intrinsic acceleration on a parabolic helix: constant angular rate is not constant speed"
category: conceptual_question
archetype: kinematics
level: conceptual
unit: 1
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013 to 2018); not an official exercise. Verified with scripts/mechanics/c01.py"
tags:
  - problem-bank
  - midterm-1
  - intrinsic-frame
  - cylindrical-coordinates
  - curvature
---

# Bank C01 — Intrinsic acceleration on a parabolic helix

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §2.4 and §2.5 (intrinsic basis, tangential and normal acceleration) and §2.6 (cylindrical coordinates). Every number was checked with SymPy.

## Statement

A point particle $P$ moves with respect to the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ along the curve given in cylindrical coordinates $(R,\varphi,z)$, with basis $\{\mathbf e_R,\mathbf e_\varphi,\mathbf e_z\}$, by

$$R=a,\qquad z=\frac{a}{2}\,\varphi^2,\qquad \varphi\ge0,$$

with $a>0$ a constant length: a helix wound on the cylinder $R=a$ whose pitch grows with $\varphi$. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

## (a) Constant angular rate [1.0 pts]

The particle moves with the time law $\varphi=\omega t$, $\omega>0$ constant. Statement: "Since $\dot\varphi$ is constant, the tangential acceleration of $P$ is zero, and at the point $\varphi=1$ the acceleration of $P$ is purely normal."

### Hint

The tangential acceleration is the rate of change of the speed $|\mathbf v|$, not of $\dot\varphi$. Compute $|\mathbf v|$ as a function of $\varphi$.

### Checkpoint

- FALSE.
- $\mathbf v=a\omega\,\mathbf e_\varphi+a\omega\varphi\,\mathbf e_z$, $\ |\mathbf v|=a\omega\sqrt{1+\varphi^2}$ grows with time; $\ \mathbf a=a\omega^2(-\mathbf e_R+\mathbf e_z)$.
- $a_t=a\omega^2\varphi/\sqrt{1+\varphi^2}$: at $\varphi=1$, $a_t=a\omega^2/\sqrt2\neq0$ and $a_n=\sqrt{3/2}\,a\omega^2$.

### Solution

#### Step 1. Velocity in cylindrical coordinates

With $\mathbf r=R\,\mathbf e_R+z\,\mathbf e_z$, $\dot{\mathbf e}_R=\dot\varphi\,\mathbf e_\varphi$ and $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_R$ (Notes §2.6), the velocity is $\mathbf v=\dot R\,\mathbf e_R+R\dot\varphi\,\mathbf e_\varphi+\dot z\,\mathbf e_z$. Here $\dot R=0$, $\dot\varphi=\omega$ and, by the chain rule, $\dot z=\frac{dz}{d\varphi}\dot\varphi=a\varphi\,\omega$:

$$\mathbf v=a\omega\,\mathbf e_\varphi+a\omega\varphi\,\mathbf e_z,\qquad |\mathbf v|=a\omega\sqrt{1+\varphi^2}$$

The speed is not constant, so the statement already fails: a constant angular rate does not mean a constant speed when the curve climbs faster and faster.

#### Step 2. Acceleration

$\mathbf a=(\ddot R-R\dot\varphi^2)\,\mathbf e_R+(R\ddot\varphi+2\dot R\dot\varphi)\,\mathbf e_\varphi+\ddot z\,\mathbf e_z$, with $\ddot\varphi=0$ and $\ddot z=\frac{d}{dt}(a\omega\varphi)=a\omega\dot\varphi=a\omega^2$:

$$\mathbf a=-a\omega^2\,\mathbf e_R+a\omega^2\,\mathbf e_z,\qquad |\mathbf a|^2=2a^2\omega^4$$

#### Step 3. Tangential and normal components

The tangential acceleration is $a_t=\frac{d|\mathbf v|}{dt}$ (Notes §2.5). With the chain rule $\frac{d}{dt}\sqrt{1+\varphi^2}=\frac{\varphi\,\dot\varphi}{\sqrt{1+\varphi^2}}$:

$$a_t=a\omega\,\frac{\varphi\,\omega}{\sqrt{1+\varphi^2}}=\frac{a\omega^2\varphi}{\sqrt{1+\varphi^2}}$$

The same result follows from $a_t=\mathbf a\cdot\mathbf v/|\mathbf v|=a^2\omega^3\varphi/(a\omega\sqrt{1+\varphi^2})$. At $\varphi=1$:

$$a_t=\frac{a\omega^2}{\sqrt2}\neq0,\qquad a_n=\sqrt{|\mathbf a|^2-a_t^2}=a\omega^2\sqrt{2-\tfrac12}=\sqrt{\tfrac32}\,a\omega^2$$

The acceleration has a tangential part, so the statement is FALSE. For later use: at $\varphi=1$, $\mathbf e_t=(\mathbf e_\varphi+\mathbf e_z)/\sqrt2$, $a_t\mathbf e_t=\tfrac12a\omega^2(\mathbf e_\varphi+\mathbf e_z)$ and

$$\mathbf a_n=\mathbf a-a_t\mathbf e_t=a\omega^2\big(-\mathbf e_R-\tfrac12\mathbf e_\varphi+\tfrac12\mathbf e_z\big),\qquad \mathbf e_n=\frac{-2\,\mathbf e_R-\mathbf e_\varphi+\mathbf e_z}{\sqrt6}$$

## (b) Constant speed [1.0 pts]

The same curve is now traversed at a constant speed $v_0$. Statement: "At the point $\varphi=1$ the acceleration of $P$ is perpendicular to its velocity, has magnitude $\sqrt6\,v_0^2/(4a)$ and points along the same unit vector $\mathbf e_n$ as the normal acceleration of part (a)."

### Hint

With constant speed only the normal term $\dot s^2/\rho$ remains. The curvature and the principal normal are properties of the curve, not of the time law: compute $\kappa=1/\rho$ from $|\mathbf a_n|/|\mathbf v|^2$ of part (a), or from $|\mathbf r'\times\mathbf r''|/|\mathbf r'|^3$.

### Checkpoint

- TRUE.
- $\mathbf a=\dot v\,\mathbf e_t+\dfrac{v^2}{\rho}\,\mathbf e_n$ with $\dot v=0$: $\mathbf a\perp\mathbf v$.
- $\kappa(\varphi)=\dfrac{\sqrt{2+\varphi^2}}{a(1+\varphi^2)^{3/2}}$, $\ \kappa(1)=\dfrac{\sqrt6}{4a}$, $\ |\mathbf a|=\kappa v_0^2=\dfrac{\sqrt6\,v_0^2}{4a}$; $\mathbf e_n$ depends only on the curve.

### Solution

#### Step 1. Intrinsic acceleration

In the intrinsic basis (Notes §2.5), $\mathbf a=\ddot s\,\mathbf e_t+\dfrac{\dot s^2}{\rho}\,\mathbf e_n$. With $\dot s=v_0$ constant, $\ddot s=0$, so $\mathbf a=\dfrac{v_0^2}{\rho}\,\mathbf e_n$, which is perpendicular to $\mathbf v=v_0\,\mathbf e_t$. It is not zero: the trajectory is curved.

#### Step 2. Curvature at $\varphi=1$

The curvature depends only on the geometry. From part (a) at $\varphi=1$, $\kappa=\dfrac{a_n}{|\mathbf v|^2}=\dfrac{\sqrt{3/2}\,a\omega^2}{2a^2\omega^2}=\dfrac{\sqrt6}{4a}$. Independent check with the parameter $\varphi$: $\mathbf r'=a(-\sin\varphi,\cos\varphi,\varphi)$ and $\mathbf r''=a(-\cos\varphi,-\sin\varphi,1)$ in $\{\mathbf i,\mathbf j,\mathbf k\}$, so

$$\mathbf r'\times\mathbf r''=a^2\big(\cos\varphi+\varphi\sin\varphi,\ \sin\varphi-\varphi\cos\varphi,\ 1\big),\qquad |\mathbf r'\times\mathbf r''|=a^2\sqrt{2+\varphi^2},\qquad |\mathbf r'|=a\sqrt{1+\varphi^2}$$

$$\kappa=\frac{|\mathbf r'\times\mathbf r''|}{|\mathbf r'|^3}=\frac{\sqrt{2+\varphi^2}}{a\,(1+\varphi^2)^{3/2}},\qquad \kappa(1)=\frac{\sqrt3}{a\,2^{3/2}}=\frac{\sqrt6}{4a}$$

#### Step 3. Magnitude and direction

$$|\mathbf a|=\kappa\,v_0^2=\frac{\sqrt6\,v_0^2}{4a}$$

The principal normal is $\mathbf e_n=\dfrac{d\mathbf e_t/ds}{|d\mathbf e_t/ds|}$, a function of the point of the curve only (Notes §2.4), so it is the same vector $(-2\,\mathbf e_R-\mathbf e_\varphi+\mathbf e_z)/\sqrt6$ found in (a). The three claims hold: TRUE.

## Interpretation

- **Dimensional check:** $a\omega^2$ is m s$^{-2}$; $\kappa$ is m$^{-1}$ and $\kappa v_0^2$ is m s$^{-2}$.
- **Limits:** at $\varphi=0$ the tangent is horizontal, but $\kappa(0)=\sqrt2/a$ is larger than the $1/a$ of the circle $R=a$ because the curve also bends upwards ($d^2z/d\varphi^2=a\neq0$); for $\varphi\to\infty$, $\kappa\approx1/(a\varphi^2)\to0$: the turns become almost vertical lines.
- **Common mistakes in the exam:** (1) confusing a constant angular rate $\dot\varphi$ with a constant speed; (2) saying "constant speed implies zero acceleration"; (3) believing that $\mathbf e_t$, $\mathbf e_n$ or $\rho$ depend on how fast the curve is traversed.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
