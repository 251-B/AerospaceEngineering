---
materia: Engineering Mechanics
tema: "Units 2 and 5: dynamics in a translating non-inertial frame"
bank_id: P05
title: "Flight pendulum on an accelerating support: inertia forces, equilibrium and a change of regime"
category: midterm_problem
archetype: relative-motion
level: standard
unit: 5
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p05.py"
tags:
  - problem-bank
  - midterm-1
  - translating-frame
  - inertia-forces
  - energy
  - equilibrium
---

# Bank P05 — Flight pendulum on an accelerating support

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §3.2 (velocity and acceleration in a moving frame), §4.9 (dynamics of relative motion), §4.5 (mechanical energy) and §4.7 (simple pendulum). Every number was checked with SymPy.

## Statement

A flight-test pendulum hangs from a rail fixed to the ceiling of an aircraft cabin. The support $A$ slides along the rail with a **constant acceleration** $\mathbf a_A=a_0\,\mathbf i$ with respect to the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ ($x$ horizontal, forward; $y$ vertical, upward; uniform gravity $-g\,\mathbf j$), starting from rest at $t=0$. The bob $P$ of mass $m$ is joined to $A$ by a massless, inextensible string of length $\ell$ that stays taut. The angle $\theta$ is measured from the downward vertical, positive towards $+x$. At $t=0$ the bob hangs at rest with respect to the cabin ($\theta=0$, $\dot\theta=0$).

![[attachments/EM-M1/p05-flight-pendulum.svg]]

Use the reference frame $S_1=\{A;\mathbf i,\mathbf j,\mathbf k\}$ that translates with $A$ (its axes stay parallel to those of $S_0$), and, only to project vectors, the unit vectors $\mathbf e_r=\sin\theta\,\mathbf i-\cos\theta\,\mathbf j$ and $\mathbf e_\theta=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j$.

## Setup

- Data: $m$, $\ell$, $g$, $a_0>0$. In the numerical parts (f) and (g): $a_0=g/\sqrt3$.
- Hypotheses: point particle, planar motion, string always taut (checked in (g)), no friction, $S_0$ inertial.
- $S_1$ is a **translating** frame: $\boldsymbol\omega_{10}=\mathbf 0$, so the only inertia force is $-m\,\mathbf a_A$ (no Coriolis, no centrifugal force).

## (a) Degrees of freedom and frames [1.0 pts]

How many effective degrees of freedom has $P$? State the angular velocity of $S_1$ with respect to $S_0$ and the kind of inertia force that appears in $S_1$.

### Hint

The string removes one of the two planar degrees of freedom. $A$'s motion is prescribed, not unknown.

### Checkpoint

- 1 degree of freedom, coordinate $\theta(t)$.
- $\boldsymbol\omega_{10}=\mathbf 0$; only the translational inertia force $-m a_0\mathbf i$.

### Solution

#### Step 1. Count

A free particle in the plane has 2 degrees of freedom. The string gives the holonomic constraint $|\mathbf r_{AP}|=\ell$, which removes one: $\theta$ describes the configuration. The motion of $A$ is given ($\mathbf a_A=a_0\mathbf i$), so it adds no unknown: the constraint is **rheonomic** in $S_0$ and scleronomic in $S_1$.

#### Step 2. The frame

$S_1$ keeps its axes parallel to those of $S_0$, so $\boldsymbol\omega_{10}=\mathbf 0$. In the relative-motion law $\mathbf F+\mathbf F_{in}=m\mathbf a_{rel}$ (Notes §4.9) the Coriolis term $-2m\boldsymbol\omega\times\mathbf v_{rel}$ and the centrifugal term vanish, and only $\mathbf F_{in}=-m\mathbf a_A$ remains.

## (b) Kinematics of $P$ [1.5 pts]

Write the position, velocity and acceleration of $P$ **relative to $S_1$**, and the absolute velocity and acceleration of $P$ in $S_0$, in the basis $\{\mathbf e_r,\mathbf e_\theta\}$.

### Hint

Differentiate $\mathbf r_{rel}=\ell\mathbf e_r$ with $\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta$ and $\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r$. For the absolute motion add the motion of $A$.

### Checkpoint

- $\mathbf a_{rel}=\ell\ddot\theta\,\mathbf e_\theta-\ell\dot\theta^2\mathbf e_r$.
- $\mathbf a_P=a_0\mathbf i+\mathbf a_{rel}$ with $\mathbf i=\sin\theta\,\mathbf e_r+\cos\theta\,\mathbf e_\theta$.

### Solution

#### Change of basis

The projection basis $\{\mathbf e_r,\mathbf e_\theta\}$ is related to $\{\mathbf i,\mathbf j\}$ (planar, $\mathbf k$ common) by

$$\begin{pmatrix}\mathbf e_r\cr\mathbf e_\theta\end{pmatrix}=R\begin{pmatrix}\mathbf i\cr\mathbf j\end{pmatrix},\qquad R=\begin{pmatrix}\sin\theta&-\cos\theta\cr\cos\theta&\sin\theta\end{pmatrix}$$

$$\det R=\sin^2\theta+\cos^2\theta=1,\qquad RR^T=\begin{pmatrix}\sin^2\theta+\cos^2\theta&0\cr0&\cos^2\theta+\sin^2\theta\end{pmatrix}=I$$

so $R$ is orthonormal and right-handed ($\mathbf e_r\times\mathbf e_\theta=\mathbf k$). The inverse is $R^T$: $\mathbf i=\sin\theta\,\mathbf e_r+\cos\theta\,\mathbf e_\theta$, used below.

#### Step 1. Derivatives of the unit vectors

From $\mathbf e_r=\sin\theta\,\mathbf i-\cos\theta\,\mathbf j$ and the chain rule $\frac{d}{dt}f(\theta(t))=\frac{df}{d\theta}\dot\theta$:

$$\dot{\mathbf e}_r=\dot\theta\,(\cos\theta\,\mathbf i+\sin\theta\,\mathbf j)=\dot\theta\,\mathbf e_\theta,\qquad \dot{\mathbf e}_\theta=\dot\theta\,(-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j)=-\dot\theta\,\mathbf e_r$$

#### Step 2. Relative motion

$$\mathbf r_{rel}=\ell\,\mathbf e_r,\qquad \mathbf v_{rel}=\ell\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_{rel}=\ell\ddot\theta\,\mathbf e_\theta+\ell\dot\theta\,\dot{\mathbf e}_\theta=\ell\ddot\theta\,\mathbf e_\theta-\ell\dot\theta^2\,\mathbf e_r$$

($\ell$ is constant, so the string produces no radial relative velocity.)

#### Step 3. Absolute motion

The support starts from rest with constant acceleration: $\mathbf v_A=a_0t\,\mathbf i$, $\mathbf r_A=\tfrac12a_0t^2\,\mathbf i$. Since $S_1$ does not rotate, $\mathbf v_P=\mathbf v_A+\mathbf v_{rel}$ and $\mathbf a_P=\mathbf a_A+\mathbf a_{rel}$:

$$\mathbf v_P=a_0t\,\mathbf i+\ell\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_P=a_0\,\mathbf i+\ell\ddot\theta\,\mathbf e_\theta-\ell\dot\theta^2\,\mathbf e_r$$

Projecting $\mathbf i=\sin\theta\,\mathbf e_r+\cos\theta\,\mathbf e_\theta$ (the dot products $\mathbf i\cdot\mathbf e_r=\sin\theta$, $\mathbf i\cdot\mathbf e_\theta=\cos\theta$):

$$\mathbf a_P=\big(a_0\sin\theta-\ell\dot\theta^2\big)\mathbf e_r+\big(a_0\cos\theta+\ell\ddot\theta\big)\mathbf e_\theta$$

## (c) Forces on $P$ in $S_1$ [1.5 pts]

Write every force acting on $P$ in $S_1$ in the basis $\{\mathbf e_r,\mathbf e_\theta\}$, including the inertia force. Which of them can do work in $S_1$?

### Hint

$\mathbf j\cdot\mathbf e_r=-\cos\theta$ and $\mathbf j\cdot\mathbf e_\theta=\sin\theta$. The tension acts along the string.

### Checkpoint

- $\mathbf W=mg(\cos\theta\,\mathbf e_r-\sin\theta\,\mathbf e_\theta)$, $\ \mathbf T=-T\mathbf e_r$, $\ \mathbf F_{in}=-ma_0(\sin\theta\,\mathbf e_r+\cos\theta\,\mathbf e_\theta)$.
- $\mathbf T$ does no work (it is orthogonal to $\mathbf v_{rel}$); $\mathbf W$ and $\mathbf F_{in}$ are conservative.

### Solution

#### Step 1. Weight

$\mathbf W=-mg\,\mathbf j$ with $\mathbf W\cdot\mathbf e_r=-mg(\mathbf j\cdot\mathbf e_r)=mg\cos\theta$ and $\mathbf W\cdot\mathbf e_\theta=-mg\sin\theta$:

$$\mathbf W=mg\cos\theta\,\mathbf e_r-mg\sin\theta\,\mathbf e_\theta$$

#### Step 2. Tension and inertia force

The string is massless and taut, so its force on $P$ points to $A$: $\mathbf T=-T\,\mathbf e_r$ with $T\ge0$ unknown. The inertia force of the translating frame is

$$\mathbf F_{in}=-m\,\mathbf a_A=-ma_0\,\mathbf i=-ma_0\sin\theta\,\mathbf e_r-ma_0\cos\theta\,\mathbf e_\theta$$

#### Step 3. Work in $S_1$

The power of a force is $\mathbf F\cdot\mathbf v_{rel}$ with $\mathbf v_{rel}=\ell\dot\theta\,\mathbf e_\theta$: only the $\mathbf e_\theta$ components work. $\mathbf T\cdot\mathbf v_{rel}=0$. $\mathbf W$ and $\mathbf F_{in}$ are uniform forces, hence conservative, with potentials $V_g=-mg\ell\cos\theta$ and $V_{in}=ma_0\ell\sin\theta$ (check: $-\partial V/\partial\theta/\ell$ gives their $\mathbf e_\theta$ components).

## (d) Equation of motion and tension [2.0 pts]

Obtain the equation $\ddot\theta=f(\theta)$ that does not contain $T$, and the expression of $T$ as a function of $\theta$ and $\dot\theta$.

### Hint

Project $m\mathbf a_{rel}=\mathbf W+\mathbf T+\mathbf F_{in}$ on $\mathbf e_\theta$ (no $T$) and on $\mathbf e_r$ (gives $T$).

### Checkpoint

- $\ell\ddot\theta=-g\sin\theta-a_0\cos\theta$.
- $T=m\big(\ell\dot\theta^2+g\cos\theta-a_0\sin\theta\big)$.

### Solution

#### Step 1. Newton in $S_1$

$$m\big(\ell\ddot\theta\,\mathbf e_\theta-\ell\dot\theta^2\mathbf e_r\big)=\mathbf W+\mathbf T+\mathbf F_{in}$$

#### Step 2. Tangential projection

$$m\ell\ddot\theta=-mg\sin\theta-ma_0\cos\theta\ \Longrightarrow\ \ell\ddot\theta=-g\sin\theta-a_0\cos\theta$$

This equation has one unknown, $\theta(t)$, because the tension is orthogonal to $\mathbf e_\theta$.

#### Step 3. Radial projection

$$-m\ell\dot\theta^2=mg\cos\theta-T-ma_0\sin\theta\ \Longrightarrow\ T=m\big(\ell\dot\theta^2+g\cos\theta-a_0\sin\theta\big)$$

#### Step 4. Cross-check with the absolute frame

Newton in $S_0$ along $\mathbf e_r$: $m\,\mathbf a_P\cdot\mathbf e_r=m(a_0\sin\theta-\ell\dot\theta^2)=\mathbf W\cdot\mathbf e_r-T=mg\cos\theta-T$, which gives the same $T$.

## (e) Equilibrium and small oscillations [1.0 pts]

Find the equilibrium angle $\theta_e$ and the frequency of the small oscillations about it, as functions of $a_0$, $g$, $\ell$. What does the pendulum indicate?

### Hint

Write $-g\sin\theta-a_0\cos\theta=-g_{eff}\sin(\theta-\theta_e)$ with $g_{eff}=\sqrt{g^2+a_0^2}$.

### Checkpoint

- $\theta_e=-\arctan(a_0/g)$ (the bob lags behind), $g_{eff}=\sqrt{g^2+a_0^2}$.
- $\omega^2=g_{eff}/\ell$, stable equilibrium.

### Solution

#### Step 1. Equilibrium

Setting $\ddot\theta=0$: $g\sin\theta+a_0\cos\theta=0\Rightarrow\tan\theta_e=-a_0/g$. Two solutions differ by $\pi$; the stable one hangs below $A$: $\theta_e=-\arctan(a_0/g)$.

#### Step 2. Rewrite the equation

With $\cos\alpha=g/g_{eff}$, $\sin\alpha=a_0/g_{eff}$ ($\alpha=\arctan(a_0/g)$) and the identity $\sin(\theta+\alpha)=\sin\theta\cos\alpha+\cos\theta\sin\alpha$:

$$\ell\ddot\theta=-g_{eff}\big(\sin\theta\cos\alpha+\cos\theta\sin\alpha\big)=-g_{eff}\sin(\theta+\alpha)$$

so $\theta_e=-\alpha$. Define $\varphi=\theta-\theta_e=\theta+\alpha$: $\ \ell\ddot\varphi=-g_{eff}\sin\varphi$, an ordinary pendulum in a gravity $g_{eff}$.

#### Step 3. Linearisation

For $|\varphi|\ll1$, $\sin\varphi\approx\varphi$ and $\ddot\varphi+\dfrac{g_{eff}}{\ell}\varphi=0$:

$$\omega=\sqrt{\frac{g_{eff}}{\ell}}=\frac{\sqrt[4]{g^2+a_0^2}}{\sqrt\ell},\qquad \tau=2\pi\sqrt{\frac{\ell}{g_{eff}}}$$

The pendulum aligns with the **apparent gravity** $\mathbf g-\mathbf a_A$ (the specific force) and oscillates faster than at rest.

## (f) First integral and the swing from $\theta=0$ [1.5 pts]

Write a first integral of the motion in $S_1$. For $a_0=g/\sqrt3$, with the initial conditions of the statement, find the extreme angles of the swing and $\ell\dot\theta^2$ when the bob passes $\theta_e$.

### Hint

The mechanical energy in $S_1$ includes the potential of $\mathbf F_{in}$. Use $\varphi$: the energy is symmetric about $\varphi=0$.

### Checkpoint

- $\tfrac12\ell^2\dot\theta^2-g\ell\cos\theta+a_0\ell\sin\theta=$ const, i.e. $\tfrac12\ell^2\dot\theta^2-g_{eff}\ell\cos\varphi=$ const.
- $\theta_e=-30^\circ$, extremes $\theta=0$ and $\theta=-60^\circ$; $\ell\dot\theta^2(\theta_e)=2g_{eff}(1-\cos30^\circ)=(4/\sqrt3-2)\,g\approx0.309\,g$.

### Solution

#### Step 1. Energy in $S_1$

In $S_1$ the work is done by $\mathbf W$ and $\mathbf F_{in}$ (conservative, part (c)); $\mathbf T$ does none. Hence $E=T_{kin}+V_g+V_{in}$ is constant:

$$\frac{E}{m}=\tfrac12\ell^2\dot\theta^2-g\ell\cos\theta+a_0\ell\sin\theta$$

Check: $\dfrac{d}{dt}\dfrac Em=\ell\dot\theta\big(\ell\ddot\theta+g\sin\theta+a_0\cos\theta\big)=0$ by part (d). With $-g\cos\theta+a_0\sin\theta=-g_{eff}\cos(\theta+\alpha)$:

$$\frac{E}{m}=\tfrac12\ell^2\dot\theta^2-g_{eff}\,\ell\cos\varphi$$

#### Step 2. Numbers

For $a_0=g/\sqrt3$: $\tan\alpha=1/\sqrt3$, so $\alpha=30^\circ$, $\theta_e=-30^\circ$ and $g_{eff}=g\sqrt{1+1/3}=2g/\sqrt3$. At $t=0$: $\theta=0\Rightarrow\varphi_0=30^\circ$, $\dot\theta=0$.

#### Step 3. Extremes and speed

Equating $E$ at $\varphi_0$ and at a generic $\varphi$:

$$\ell^2\dot\theta^2=2g_{eff}\,\ell\,\big(\cos\varphi-\cos30^\circ\big)$$

It vanishes at $\varphi=\pm30^\circ$, i.e. $\theta=0$ and $\theta=-60^\circ$. At $\varphi=0$ the factor is $\cos0-\cos30^\circ=1-\cos30^\circ$:

$$\ell\dot\theta^2\Big|_{\theta_e}=2g_{eff}\,(1-\cos30^\circ)=\frac{4g}{\sqrt3}\Big(1-\frac{\sqrt3}{2}\Big)=\Big(\frac4{\sqrt3}-2\Big)g\approx0.309\,g$$

## (g) Tension and a change of regime [1.5 pts]

For $a_0=g/\sqrt3$: (i) compute $T$ at $\theta_e$ and show that the string never goes slack. (ii) At the instant the bob passes $\theta_e$ for the first time (moving backwards, $\dot\theta<0$) the support stops accelerating ($a_0\to0$, $A$ keeps its velocity). Find the maximum angle of the following motion and the tension when the bob passes the vertical.

### Hint

(i) Substitute $\dot\theta^2$ of (f) into $T$ of (d). (ii) The frame $S_1$ becomes inertial: use $\theta$, $\dot\theta$ at the switch as new initial conditions and energy with $g$ only.

### Checkpoint

- $T(\varphi)=mg_{eff}(3\cos\varphi-2\cos30^\circ)$; $T(\theta_e)=mg(2\sqrt3-2)\approx1.46\,mg$; $T_{min}=mg$ at the turning points.
- Phase 2: $\cos\theta_{max}=1-\sqrt3/6$, $\theta_{max}\approx44.66^\circ$ (the swing is $\pm44.66^\circ$ about the vertical; the first turning point is **behind** the vertical, at $-44.66^\circ$); $T(0)=mg(1+1/\sqrt3)\approx1.58\,mg$.

### Solution

#### Step 1. Tension along the swing

From (d), $T=m(\ell\dot\theta^2+g\cos\theta-a_0\sin\theta)$ and $g\cos\theta-a_0\sin\theta=g_{eff}\cos\varphi$. With $\ell\dot\theta^2=2g_{eff}(\cos\varphi-\cos30^\circ)$ of (f):

$$T(\varphi)=mg_{eff}\big(3\cos\varphi-2\cos30^\circ\big)$$

At $\varphi=0$: $T=m\frac{2g}{\sqrt3}(3-\sqrt3)=mg(2\sqrt3-2)\approx1.464\,mg$. $T$ decreases with $|\varphi|$; its minimum is at $\varphi=\pm30^\circ$: $T=mg_{eff}\cos30^\circ=mg>0$. The string is taut during the whole swing.

#### Step 2. Initial conditions of phase 2

At the switch: $\theta_1=-30^\circ$, $\ell\dot\theta_1^2=(4/\sqrt3-2)g$. Afterwards $\ell\ddot\theta=-g\sin\theta$ (ordinary pendulum), with the energy per unit mass $\tfrac12\ell^2\dot\theta^2-g\ell\cos\theta=$ const. The bob has kinetic energy at $\theta_1$, which is **not** the equilibrium of the new motion.

#### Step 3. Maximum angle

Setting $\dot\theta=0$ at $\theta_m$:

$$-g\ell\cos\theta_m=\tfrac12\ell^2\dot\theta_1^2-g\ell\cos30^\circ\ \Longrightarrow\ \cos\theta_m=\frac{\sqrt3}{2}-\frac12\Big(\frac4{\sqrt3}-2\Big)=1-\frac{1}{2\sqrt3}=1-\frac{\sqrt3}{6}$$

so $\theta_m=\arccos(0.7113)=44.66^\circ$: the bob, which was at $-30^\circ$ moving backwards, first reaches $-44.66^\circ$ (beyond the old equilibrium), then swings through the vertical to $+44.66^\circ$: the new motion is symmetric, $\theta\in[-44.66^\circ,+44.66^\circ]$, about the vertical.

#### Step 4. Tension at the vertical

The energy $\tfrac12\ell^2\dot\theta^2-g\ell\cos\theta$ is the same at $\theta_1=-30^\circ$ and at $\theta=0$, so $\ell\dot\theta^2(0)=\ell\dot\theta_1^2+2g(\cos0-\cos30^\circ)$ with $\cos0-\cos30^\circ=1-\sqrt3/2$:

$$\ell\dot\theta^2(0)=\Big(\frac4{\sqrt3}-2\Big)g+2g\Big(1-\frac{\sqrt3}2\Big)=\Big(\frac4{\sqrt3}-\sqrt3\Big)g=\frac{g}{\sqrt3}$$

and with $a_0=0$: $T(0)=m\big(\ell\dot\theta^2+g\big)=mg\big(1+\tfrac1{\sqrt3}\big)\approx1.577\,mg$.

## Interpretation

- **Dimensional check:** $a_0$, $g$ and $\ell\dot\theta^2$ are accelerations (m s$^{-2}$); $\omega^2=g_{eff}/\ell$ is s$^{-2}$; $T$ is $m\times$ acceleration = N.
- **Limits:** $a_0\to0$ gives $\theta_e=0$, $g_{eff}=g$ and the ordinary pendulum; $a_0\gg g$ gives $\theta_e\to-90^\circ$ (the string lies horizontal, behind the support) and $\omega^2\approx a_0/\ell$.
- **Common mistakes in the exam:** (1) writing the inertia force with the wrong sign (it is $-m\mathbf a_A$, opposite to the support's acceleration); (2) forgetting that $\mathbf T$ is orthogonal to $\mathbf v_{rel}$ and adding its work; (3) taking the old equilibrium as the centre of the new motion after the support stops: the bob keeps its speed and swings **past** the vertical; (4) using $g$ instead of $g_{eff}$ in the period.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
