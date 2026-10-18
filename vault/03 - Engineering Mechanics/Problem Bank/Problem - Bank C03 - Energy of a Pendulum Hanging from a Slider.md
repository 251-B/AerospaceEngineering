---
materia: Engineering Mechanics
tema: "Unit 2: work of internal forces and of a moving support, energy of a particle and of a system"
bank_id: C03
title: "Energy of a pendulum hanging from a slider: one particle, the system, and a driven support"
category: conceptual_question
archetype: dynamics
level: conceptual
unit: 2
difficulty: 2
points: 2.0
time_minutes: 15
official: false
origen: "Question written for the bank in the style of the true/false questions of the final exams (MECHANICS_FINALEXAM_2013 to 2016); not an official exercise. Verified with scripts/mechanics/c03.py"
tags:
  - problem-bank
  - midterm-1
  - work-and-power
  - mechanical-energy
  - moving-support
---

# Bank C03 — Energy of a pendulum hanging from a slider

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the true/false questions of the final exams. Method: Notes §4.4 and §4.5 (power, work, potential energy and conservation of mechanical energy) and §4.9 (dynamics in a translating frame). Every number was checked with SymPy.

## Statement

A slider $A$ of mass $M$ moves along a smooth, fixed horizontal rail (the $x$ axis direction of the inertial frame $S_0=\{O;\mathbf i,\mathbf j\}$, $y$ upward, gravity $-g\,\mathbf j$); its abscissa is $x_A$. A bob $P$ of mass $m$ hangs from $A$ on a massless, inextensible string of length $\ell$ that stays taut. The angle $\theta$ is measured from the downward vertical, positive towards $+x$, and $\mathbf e_r=\sin\theta\,\mathbf i-\cos\theta\,\mathbf j$ (from $A$ to $P$), $\mathbf e_\theta=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j$. The motion is planar. Decide whether each statement is TRUE or FALSE and justify the answer. A verdict without a justification scores nothing.

![[attachments/EM-M1/c03-slider-pendulum.svg]]

## (a) Free slider [1.0 pts]

The slider moves freely on the rail. Statement: "The mechanical energy of the bob alone, $E_P=\tfrac12m|\mathbf v_P|^2+mg\,y_P$, is **not** conserved, but the mechanical energy of the system slider plus bob, $E=\tfrac12M\dot x_A^2+E_P$, is conserved."

### Hint

Compute the power of the tension on $P$ with the **absolute** velocity $\mathbf v_P=\dot x_A\,\mathbf i+\ell\dot\theta\,\mathbf e_\theta$. Then add the power of the reaction of the string on $A$.

### Checkpoint

- TRUE.
- Tension on $P$: $-T\mathbf e_r$, power $-T\mathbf e_r\cdot\mathbf v_P=-T\dot x_A\sin\theta\neq0$ in general, so $\dot E_P=-T\dot x_A\sin\theta$.
- Tension on $A$: $+T\mathbf e_r$, power $+T\dot x_A\sin\theta$; the pair has total power $T\mathbf e_r\cdot(\mathbf v_A-\mathbf v_P)=0$ (inextensible string); rail reaction and $M\mathbf g$ are vertical, orthogonal to $\dot x_A\mathbf i$: $\dot E=0$.
- Example: released from rest at $\theta_0$, at $\theta=0$ the slider has $\tfrac12M\dot x_A^2=\dfrac{m^2g\ell(1-\cos\theta_0)}{M+m}$, energy that $P$ has lost.

### Solution

#### Step 1. Power of the tension on the bob

The string pulls $P$ towards $A$: $\mathbf T_P=-T\,\mathbf e_r$, $T\ge0$. The absolute velocity of $P$ is $\mathbf v_P=\dot x_A\,\mathbf i+\ell\dot\theta\,\mathbf e_\theta$ (derivative of $\mathbf r_P=x_A\mathbf i+\ell\mathbf e_r$ with $\dot{\mathbf e}_r=\dot\theta\,\mathbf e_\theta$). With $\mathbf e_r\cdot\mathbf i=\sin\theta$ and $\mathbf e_r\cdot\mathbf e_\theta=0$:

$$\dot W_{T,P}=\mathbf T_P\cdot\mathbf v_P=-T\dot x_A\sin\theta$$

The tension is orthogonal to the velocity of $P$ **relative to $A$**, but not to its absolute velocity. By the work-energy theorem with the weight as the only conservative force on $P$ (Notes §4.5), $\dot E_P=-T\dot x_A\sin\theta$, which is not zero whenever the slider moves with the string inclined: $E_P$ is not conserved.

#### Step 2. The system

On $A$ act $M\mathbf g$ and the rail reaction (both vertical, power zero against $\dot x_A\mathbf i$: smooth rail) and the string force $\mathbf T_A=+T\,\mathbf e_r$, of power $T\dot x_A\sin\theta$. Hence $\frac{d}{dt}\big(\tfrac12M\dot x_A^2\big)=T\dot x_A\sin\theta$ and

$$\dot E=T\dot x_A\sin\theta-T\dot x_A\sin\theta=T\,\mathbf e_r\cdot(\mathbf v_A-\mathbf v_P)=-T\ell\dot\theta\,\mathbf e_r\cdot\mathbf e_\theta=0$$

The internal pair of an inextensible string does no net work (Notes §4.4), so $E$ is conserved. The statement is TRUE.

#### Step 3. How much energy moves from $P$ to $A$

The horizontal external force is zero, so $p_x=(M+m)\dot x_A+m\ell\dot\theta\cos\theta$ is conserved, equal to $0$ for a release from rest at $\theta_0$. At $\theta=0$: $\dot x_A=-\dfrac{m\ell\dot\theta}{M+m}$. At $\theta=0$, $\mathbf e_\theta=\mathbf i$, so $\mathbf v_P=(\dot x_A+\ell\dot\theta)\,\mathbf i$ with $\dot x_A+\ell\dot\theta=\dfrac{M\ell\dot\theta}{M+m}$, and $y_P=-\ell\cos\theta$. Energy conservation between the release ($\theta_0$, at rest) and $\theta=0$:

$$\frac12M\frac{m^2\ell^2\dot\theta^2}{(M+m)^2}+\frac12m\frac{M^2\ell^2\dot\theta^2}{(M+m)^2}-mg\ell=-mg\ell\cos\theta_0$$

The two kinetic terms add up to $\dfrac{Mm(m+M)\ell^2\dot\theta^2}{2(M+m)^2}=\dfrac{Mm\,\ell^2\dot\theta^2}{2(M+m)}$, so $\dfrac{Mm\,\ell^2\dot\theta^2}{2(M+m)}=mg\ell(1-\cos\theta_0)$, which gives $\ell\dot\theta^2=\dfrac{2g(1-\cos\theta_0)(M+m)}{M}$ and

$$\tfrac12M\dot x_A^2=\frac{M}{2}\,\frac{m^2\ell^2\dot\theta^2}{(M+m)^2}=\frac{m^2g\ell\,(1-\cos\theta_0)}{M+m}>0$$

which is exactly what $E_P$ has lost.

## (b) Driven slider [1.0 pts]

A motor now imposes $x_A(t)=b\sin(\Omega t)$. Let $S_1$ be the frame that translates with $A$. Statement: "In $S_1$ the tension does no work on $P$ and the weight is conservative; therefore $E_{rel}=\tfrac12m\ell^2\dot\theta^2-mg\ell\cos\theta$ is a first integral of the motion of the bob."

### Hint

In $S_1$ there is a third force on $P$, the inertia force $-m\ddot x_A\,\mathbf i$. Is it conservative when $\ddot x_A$ depends on time?

### Checkpoint

- FALSE.
- In $S_1$: $\mathbf v_{rel}=\ell\dot\theta\,\mathbf e_\theta$, $-T\mathbf e_r\cdot\mathbf v_{rel}=0$ (this part is true).
- Equation: $\ell\ddot\theta=-g\sin\theta-\ddot x_A\cos\theta$; $\dot E_{rel}=-m\ddot x_A\,\ell\dot\theta\cos\theta=mb\Omega^2\ell\sin(\Omega t)\,\dot\theta\cos\theta\neq0$.
- The inertia force depends explicitly on $t$: even $E_{rel}+m\ddot x_A\ell\sin\theta$ changes, at the rate $m\,\dfrac{d^3x_A}{dt^3}\,\ell\sin\theta$.

### Solution

#### Step 1. Forces and work in $S_1$

$S_1$ translates with acceleration $\ddot x_A\mathbf i$, so (Notes §4.9) the forces on $P$ in $S_1$ are $m\mathbf g$, $-T\mathbf e_r$ and the inertia force $\mathbf F_{in}=-m\ddot x_A\,\mathbf i$ (no Coriolis or centrifugal terms: $\boldsymbol\omega_{10}=\mathbf 0$). With $\mathbf v_{rel}=\ell\dot\theta\,\mathbf e_\theta$ the tension does no work, and the weight has the potential $-mg\ell\cos\theta$. The power of the inertia force is

$$\mathbf F_{in}\cdot\mathbf v_{rel}=-m\ddot x_A\,\ell\dot\theta\,(\mathbf i\cdot\mathbf e_\theta)=-m\ddot x_A\,\ell\dot\theta\cos\theta$$

#### Step 2. Rate of change of $E_{rel}$

Projecting $m\mathbf a_{rel}=m\mathbf g-T\mathbf e_r+\mathbf F_{in}$ on $\mathbf e_\theta$: $m\ell\ddot\theta=-mg\sin\theta-m\ddot x_A\cos\theta$. Differentiating $E_{rel}$ with the chain rule, $\frac{d}{dt}\cos\theta=-\sin\theta\,\dot\theta$:

$$\dot E_{rel}=m\ell\dot\theta\,\big(\ell\ddot\theta+g\sin\theta\big)=-m\ddot x_A\,\ell\dot\theta\cos\theta$$

With $\ddot x_A=-b\Omega^2\sin(\Omega t)$: $\dot E_{rel}=mb\Omega^2\ell\,\sin(\Omega t)\,\dot\theta\cos\theta$. For example at $\Omega t=\pi/2$ with $\theta=0$ and $\dot\theta\neq0$ it equals $mb\Omega^2\ell\dot\theta\neq0$. $E_{rel}$ is not a first integral: the statement is FALSE.

#### Step 3. Why no other energy works either

For a constant $\ddot x_A=a_0$ (as in a uniformly accelerating support) the inertia force would be uniform and conservative, with potential $ma_0\ell\sin\theta$. Here, if we try $E^*=E_{rel}+m\ddot x_A(t)\,\ell\sin\theta$, the explicit time dependence leaves

$$\dot E^*=m\,\frac{d^3x_A}{dt^3}\,\ell\sin\theta=-mb\Omega^3\cos(\Omega t)\,\ell\sin\theta\neq0$$

The motor keeps pumping energy in and out of the bob.

## Interpretation

- **Dimensional check:** $T\dot x_A$ is N m s$^{-1}$ = W; $mb\Omega^2\ell\dot\theta$ is kg m s$^{-2}$ m s$^{-1}$ = W; $m^2g\ell/(M+m)$ is J.
- **Limits:** $M\to\infty$ makes the slider a fixed support ($\dot x_A\to0$): the energy transfer $m^2g\ell(1-\cos\theta_0)/(M+m)\to0$ and $E_P$ is conserved. $b\to0$ in (b) gives the ordinary pendulum and $\dot E_{rel}\to0$.
- **Common mistakes in the exam:** (1) "the tension is perpendicular to the velocity, so it does no work": true only for the velocity relative to the point the string is tied to; (2) forgetting the inertia force when writing the energy in a non-inertial frame; (3) treating a time-dependent inertia force as conservative.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
