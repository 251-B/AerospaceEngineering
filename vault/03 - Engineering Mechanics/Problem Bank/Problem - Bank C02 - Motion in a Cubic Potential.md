---
materia: Engineering Mechanics
tema: "Unit 2: one-dimensional motion from the energy diagram"
bank_id: C02
title: "Motion in a cubic potential: a separatrix that is never crossed and an asymmetric well"
category: conceptual_question
archetype: dynamics
level: conceptual
unit: 2
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2015, 2016 and 2018); not an official exercise. Verified with scripts/mechanics/c02.py"
tags:
  - problem-bank
  - midterm-1
  - potential-energy
  - energy-diagram
  - equilibrium
---

# Bank C02 — Motion in a cubic potential

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §4.4 and §4.5 (potential energy, conservation of mechanical energy, energy diagrams) and §4.6 (equilibrium and stability). Every number was checked with SymPy.

## Statement

A point particle $P$ of mass $m$ moves along the $x$ axis of an inertial frame under the single conservative force derived from the potential energy

$$V(x)=V_0\left[\Big(\frac{x}{b}\Big)^3-3\,\frac{x}{b}\right],$$

with $V_0>0$ (an energy) and $b>0$ (a length) constants. The figure shows $V(x)$ and two energy levels. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

![[attachments/EM-M1/c02-cubic-potential.svg]]

## (a) Released at $x=2b$ [1.0 pts]

Statement: "If $P$ is released from rest at $x=2b$, it moves to the left, reaches the top of the barrier at $x=-b$ after a finite time and then escapes towards $x\to-\infty$."

### Hint

Compare $V(2b)$ with $V(-b)$. Near a maximum of $V$, write $E-V$ to second order and look at the time integral $t=\int dx/|\dot x|$.

### Checkpoint

- FALSE.
- $V(2b)=2V_0=V(-b)$: the energy equals the top of the barrier. $F(2b)=-9V_0/b<0$, so $P$ does start to the left.
- $E-V=V_0(u+1)^2(2-u)$ with $u=x/b$: $|\dot x|\propto|x+b|$ near $x=-b$ and the time $t=b\sqrt{m/(6V_0)}\,\ln\dfrac{\sqrt3+w}{\sqrt3-w}$, $w=\sqrt{2-x/b}$, diverges as $x\to-b$: $P$ approaches the barrier top asymptotically and never crosses it.

### Solution

#### Step 1. Energy and direction of the motion

Write $u=x/b$, so $V=V_0(u^3-3u)$. By the chain rule $\frac{dV}{dx}=\frac{dV}{du}\frac{du}{dx}=\frac{3V_0}{b}(u^2-1)$: the equilibria are $x=\pm b$, with $V(-b)=2V_0$ (maximum, $V''<0$) and $V(b)=-2V_0$ (minimum). Released from rest at $x=2b$, the energy is $E=V(2b)=V_0(8-6)=2V_0$ and the initial force is $F=-\frac{dV}{dx}\big|_{2b}=-\frac{3V_0}{b}(4-1)=-\frac{9V_0}{b}<0$: $P$ moves to the left.

#### Step 2. The kinetic energy factorises

Energy conservation (Notes §4.5) gives $\tfrac12m\dot x^2=E-V$, and

$$E-V=V_0\big(2-u^3+3u\big)=V_0\,(u+1)^2\,(2-u)$$

(check: $(u+1)^2(2-u)=(u^2+2u+1)(2-u)=-u^3+3u+2$). For $-1<u<2$ it is positive, and it vanishes at $u=-1$ with a **double** root.

#### Step 3. Time to approach $x=-b$

On the way to the left $\dot x=-\sqrt{2V_0/m}\,(u+1)\sqrt{2-u}$, so $dt=\dfrac{-b\,du}{\sqrt{2V_0/m}\,(u+1)\sqrt{2-u}}$. Substitute $w=\sqrt{2-u}$: $u=2-w^2$, $du=-2w\,dw$, $u+1=3-w^2$, with $w=0$ at the start ($u=2$) and $w\to\sqrt3$ at the barrier ($u\to-1$):

$$t(w)=\frac{2b}{\sqrt{2V_0/m}}\int_0^{w}\frac{dw'}{3-w'^2}$$

With the antiderivative $\int\frac{dw}{3-w^2}=\frac{1}{2\sqrt3}\ln\frac{\sqrt3+w}{\sqrt3-w}$ and Barrow's rule (the lower limit gives $\ln1=0$):

$$t(w)=b\sqrt{\frac{m}{6V_0}}\;\ln\frac{\sqrt3+w}{\sqrt3-w}\ \xrightarrow[\ w\to\sqrt3\ ]{}\ \infty$$

For instance, $P$ passes $x=0$ ($w=\sqrt2$) at $t=b\sqrt{m/(6V_0)}\,\ln\big(5+2\sqrt6\big)\approx0.936\,b\sqrt{m/V_0}$, but it needs an infinite time to reach $x=-b$. The particle tends to the unstable equilibrium and never escapes: the statement is FALSE.

## (b) Released at $x=0$ [1.0 pts]

Statement: "If $P$ is released from rest at $x=0$, it oscillates about the stable equilibrium $x=b$ between $x=0$ and $x=2b$, symmetrically about $x=b$."

### Hint

The turning points are the roots of $V(x)=E$, not the mirror image of the starting point about the minimum. The well is not a parabola.

### Checkpoint

- FALSE.
- $E=V(0)=0$; $V=V_0u(u-\sqrt3)(u+\sqrt3)$: turning points $x=0$ and $x=\sqrt3\,b\approx1.732\,b$ (not $2b$, where $V=2V_0>E$).
- $x=b$ is stable ($V''>0$), small-oscillation frequency $\omega^2=6V_0/(mb^2)$; the motion is periodic but the distances to the turning points are $b$ and $0.732\,b$.

### Solution

#### Step 1. Energy and initial force

$E=V(0)=0$. The initial force is $F=-\frac{dV}{dx}\big|_0=-\frac{3V_0}{b}(0-1)=\frac{3V_0}{b}>0$: $P$ moves to the right, into the well of the minimum $x=b$.

#### Step 2. Turning points

They solve $V(x)=E=0$: $V_0(u^3-3u)=V_0\,u\,(u-\sqrt3)(u+\sqrt3)=0$, so $u\in\{-\sqrt3,0,\sqrt3\}$. Between $u=0$ and $u=\sqrt3$ we have $V<0=E$ and the kinetic energy is positive; the motion is confined to $0\le x\le\sqrt3\,b$. At both ends $dV/dx\neq0$ ($-3V_0/b$ at $x=0$, $+6V_0/b$ at $x=\sqrt3\,b$), so they are simple turning points reached in a finite time, and the motion is a periodic oscillation (Notes §4.5).

#### Step 3. Not symmetric, not up to $2b$

$x=2b$ is never reached, since $V(2b)=2V_0>E$. The interval $[0,\sqrt3\,b]$ extends $b$ to the left of the minimum and only $(\sqrt3-1)\,b\approx0.732\,b$ to its right: the cubic well is steeper on the right. Symmetry about the minimum holds only for a parabolic well, i.e. for small oscillations, whose frequency follows from $V''(b)=\frac{1}{b^2}\frac{d^2V}{du^2}\big|_{u=1}=\frac{6V_0}{b^2}$: $\omega^2=\dfrac{6V_0}{mb^2}$ (Notes §4.6). The statement is FALSE.

## Interpretation

- **Dimensional check:** $V_0/b$ is a force (N); $b\sqrt{m/V_0}$ is $\text{m}\sqrt{\text{kg}/\text{J}}=\text{s}$; $\omega^2=6V_0/(mb^2)$ is s$^{-2}$.
- **Limits:** with $E$ slightly below $2V_0$, $P$ would turn back just before $x=-b$ after a long but finite time; slightly above, it would cross the barrier and run to $x\to-\infty$ ($V\to-\infty$, unbounded speed). $E=2V_0$ is the separatrix between both behaviours.
- **Common mistakes in the exam:** (1) assuming that "enough energy to reach the top" means crossing it; (2) placing the turning points symmetrically about the minimum; (3) forgetting to check the sign of the initial force to know where the particle goes.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
