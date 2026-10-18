---
materia: Engineering Mechanics
tema: "Unit 3: rheonomic constraints, strings and the work of a moving constraint"
bank_id: P11
title: "Pendulum whose string is hauled through a ring: a rheonomic constraint, angular momentum and the work of the hauling force"
category: midterm_problem
archetype: constraints
level: trap
unit: 3
difficulty: 3
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2011 to 2019); not an official exercise. Verified with scripts/mechanics/p11.py"
tags:
  - problem-bank
  - midterm-1
  - rheonomic-constraint
  - string
  - angular-momentum
  - work-energy
  - variable-length-pendulum
---

# Bank P11 — Pendulum hauled through a ring

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §2.6.2 (polar coordinates), §2.7 (degrees of freedom and constraints), §4.3 (equations of motion), §4.4 (power and work) and §4.8 (angular momentum and torque). Part (f) is an **extension** beyond the course. Every equation and number was checked with SymPy and a numerical integration.

## Statement

A bob $P$ of mass $m$ hangs from a light inextensible string that passes through a small, smooth ring $O$ fixed to the ceiling. The other end of the string leaves the ring and is hauled in so that the length between $O$ and $P$ is

$$\ell(t)=\ell_0-u\,t,\qquad u>0\ \text{constant}$$

The motion is planar, in the vertical plane of the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ ($x$ horizontal, $y$ vertical upward, uniform gravity $-g\,\mathbf j$, $\mathbf k=\mathbf i\times\mathbf j$ out of the page). The angle $\theta$ is measured from the downward vertical, positive towards $+x$, and the string stays taut. Use the unit vectors $\mathbf e_r=\sin\theta\,\mathbf i-\cos\theta\,\mathbf j$ (from $O$ to $P$) and $\mathbf e_\theta=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j$.

![[attachments/EM-M1/p11-hauled-pendulum.svg]]

## Setup

- Data: $m$, $g$, $\ell_0$, $u$. Numerical parts: (d) and (e) $m=0.5$ kg, $\ell_0=2$ m, $u=0.5$ m s$^{-1}$, $g=0$, initial transverse speed $\ell_0\dot\theta_0=1$ m s$^{-1}$; (f) $\ell_0=1$ m, $u=0.01$ m s$^{-1}$, $g=9.81$ m s$^{-2}$, $\theta(0)=0.05$ rad, $\dot\theta(0)=0$.
- Hypotheses: point particle, massless inextensible string, smooth ring (the tension $T$ is the same on both sides), no air drag, $S_0$ inertial, $\ell>0$.

## (a) Degrees of freedom and the constraint [1.0 pts]

How many degrees of freedom has $P$? Classify the constraint imposed by the string.

### Hint

Write the constraint as an equation $f(\mathbf r,t)=0$. Does $t$ appear explicitly? Can the string push?

### Checkpoint

- $|\overrightarrow{OP}|-\ell_0+ut=0$: holonomic, **rheonomic** (depends on $t$), and unilateral ($T\ge0$).
- $2-1=1$ degree of freedom, coordinate $\theta(t)$; $\ell(t)$ is a given function, not an unknown.

### Solution

#### Step 1. Count

In the vertical plane a free particle has 2 degrees of freedom. The taut string between $O$ and $P$ imposes

$$f(\mathbf r,t)=|\mathbf r|-(\ell_0-ut)=0$$

one equation, so 1 degree of freedom remains: $\theta$. The length is **prescribed** by whoever pulls the string, so it is not a second coordinate (Notes §2.7).

#### Step 2. Classification

The constraint involves only positions and time: it is holonomic. Time appears explicitly, so it is **rheonomic**: the constraint moves, and its reaction (the tension) can do work on $P$, unlike the fixed string of the ordinary pendulum. A string can only pull, so the constraint is unilateral and holds while $T\ge0$.

## (b) Kinematics in polar coordinates [1.5 pts]

Write the position, velocity and acceleration of $P$ in $\{\mathbf e_r,\mathbf e_\theta\}$, first for a general length $\ell(t)$ and then for $\ell=\ell_0-ut$.

### Hint

$\dot{\mathbf e}_r=\dot\theta\,\mathbf e_\theta$ and $\dot{\mathbf e}_\theta=-\dot\theta\,\mathbf e_r$. Now $\ell$ is not constant: use the product rule.

### Checkpoint

- $\mathbf v=\dot\ell\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta$, $\ \mathbf a=(\ddot\ell-\ell\dot\theta^2)\,\mathbf e_r+(\ell\ddot\theta+2\dot\ell\dot\theta)\,\mathbf e_\theta$.
- With $\dot\ell=-u$, $\ddot\ell=0$: $\mathbf v=-u\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta$, $\ \mathbf a=-\ell\dot\theta^2\,\mathbf e_r+(\ell\ddot\theta-2u\dot\theta)\,\mathbf e_\theta$.

### Solution

#### Step 1. Change of basis and unit vectors

The working basis $\{\mathbf e_r,\mathbf e_\theta,\mathbf k\}$ turns with $P$; its relation to the inertial basis is

$$\begin{pmatrix}\mathbf e_r\\ \mathbf e_\theta\\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\\ \mathbf j\\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\sin\theta&-\cos\theta&0\\ \cos\theta&\sin\theta&0\\ 0&0&1\end{pmatrix}$$

Checks: rows 1 and 2 have length $\sin^2\theta+\cos^2\theta=1$ and $\sin\theta\cos\theta-\cos\theta\sin\theta=0$, row 3 is $\mathbf k$, so $[R][R]^T=I$; $\det[R]=\sin\theta\cdot\sin\theta-(-\cos\theta)\cos\theta=+1$, so the basis is right-handed ($\mathbf e_r\times\mathbf e_\theta=\mathbf k$). By the chain rule, $\dot{\mathbf e}_r=\dfrac{d\mathbf e_r}{d\theta}\dot\theta=(\cos\theta\,\mathbf i+\sin\theta\,\mathbf j)\dot\theta=\dot\theta\,\mathbf e_\theta$ and $\dot{\mathbf e}_\theta=(-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j)\dot\theta=-\dot\theta\,\mathbf e_r$.

#### Step 2. Position and velocity

$\mathbf r=\ell\,\mathbf e_r$. Product rule:

$$\mathbf v=\dot\ell\,\mathbf e_r+\ell\,\dot{\mathbf e}_r=\dot\ell\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta$$

#### Step 3. Acceleration

Differentiating each product:

$$\mathbf a=\ddot\ell\,\mathbf e_r+\dot\ell\dot\theta\,\mathbf e_\theta+\big(\dot\ell\dot\theta+\ell\ddot\theta\big)\mathbf e_\theta+\ell\dot\theta\,\dot{\mathbf e}_\theta=\big(\ddot\ell-\ell\dot\theta^2\big)\mathbf e_r+\big(\ell\ddot\theta+2\dot\ell\dot\theta\big)\mathbf e_\theta$$

#### Step 4. Prescribed length

$\ell=\ell_0-ut$ gives $\dot\ell=-u$, $\ddot\ell=0$:

$$\mathbf v=-u\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta,\qquad \mathbf a=-\ell\dot\theta^2\,\mathbf e_r+\big(\ell\ddot\theta-2u\dot\theta\big)\mathbf e_\theta$$

## (c) Forces and equations of motion [2.0 pts]

Write the forces on $P$ and obtain the equation of motion free of the tension and the tension itself.

### Hint

Project Newton's law on $\mathbf e_\theta$ (no $T$) and on $\mathbf e_r$.

### Checkpoint

- $\mathbf W=mg(\cos\theta\,\mathbf e_r-\sin\theta\,\mathbf e_\theta)$, $\ \mathbf T=-T\,\mathbf e_r$.
- $\ell\ddot\theta+2\dot\ell\dot\theta+g\sin\theta=0$, i.e. $(\ell_0-ut)\ddot\theta-2u\dot\theta+g\sin\theta=0$.
- $T=m\big(g\cos\theta+\ell\dot\theta^2-\ddot\ell\big)=m\big(g\cos\theta+\ell\dot\theta^2\big)$.

### Solution

#### Step 1. Forces

Weight: $\mathbf W=-mg\,\mathbf j$ with $\mathbf j\cdot\mathbf e_r=-\cos\theta$ and $\mathbf j\cdot\mathbf e_\theta=\sin\theta$, so $\mathbf W=mg\cos\theta\,\mathbf e_r-mg\sin\theta\,\mathbf e_\theta$. Tension: the string pulls $P$ towards the ring, $\mathbf T=-T\,\mathbf e_r$, $T\ge0$.

#### Step 2. Transverse projection

$$m\big(\ell\ddot\theta+2\dot\ell\dot\theta\big)=-mg\sin\theta\ \Longrightarrow\ \ell\ddot\theta+2\dot\ell\dot\theta+g\sin\theta=0$$

With $\dot\ell=-u$: $(\ell_0-ut)\ddot\theta-2u\dot\theta+g\sin\theta=0$. The term $-2u\dot\theta$ has the form of a **negative damping**: hauling the string in feeds the swing.

#### Step 3. Radial projection

$$m\big(\ddot\ell-\ell\dot\theta^2\big)=mg\cos\theta-T\ \Longrightarrow\ T=m\big(g\cos\theta+\ell\dot\theta^2-\ddot\ell\big)=m\big(g\cos\theta+\ell\dot\theta^2\big)$$

because $\ddot\ell=0$: a constant hauling speed adds no radial inertia term. The equation of Step 2 is also what a Lagrange equation (extension, not in the course notes) with $L=\tfrac12m(\dot\ell^2+\ell^2\dot\theta^2)+mg\ell\cos\theta$ gives.

## (d) Angular momentum about $O$ and the gravity-free case [1.5 pts]

Compute $\mathbf H_O$ and $d\mathbf H_O/dt$. Is it conserved? Then remove gravity (a tether in orbit reeled in at constant speed, $g=0$): find $T(\ell)$ and, for the data of the Setup, $\dot\theta$, the speed and $T$ when $\ell=0.5$ m.

### Hint

Which forces have a moment about $O$? With $g=0$, $\ell^2\dot\theta$ is constant; call it $h$.

### Checkpoint

- $\mathbf H_O=m\ell^2\dot\theta\,\mathbf k$; $\ \dfrac{d\mathbf H_O}{dt}=\mathbf r\times\mathbf W=-mg\ell\sin\theta\,\mathbf k$: **not** conserved.
- $g=0$: $\ell^2\dot\theta=h$, $T=m\ell\dot\theta^2=mh^2/\ell^3$, which grows without bound as $\ell\to0$.
- Data: $h=2$ m$^2$ s$^{-1}$; at $\ell=0.5$ m ($t=3$ s): $\dot\theta=8$ rad s$^{-1}$, $\ell\dot\theta=4$ m s$^{-1}$, $|\mathbf v|=4.031$ m s$^{-1}$, $T=16$ N (it was $0.25$ N at $\ell_0$).

### Solution

#### Step 1. Angular momentum

$\mathbf H_O=\mathbf r\times m\mathbf v=\ell\,\mathbf e_r\times m\big(\dot\ell\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta\big)=m\ell^2\dot\theta\,(\mathbf e_r\times\mathbf e_\theta)$, and $\mathbf e_r\times\mathbf e_\theta=\mathbf k$ (it is the cross product of $\mathbf i$ and $\mathbf j$ rotated by $\theta-90^\circ$):

$$\mathbf H_O=m\ell^2\dot\theta\,\mathbf k$$

#### Step 2. Its rate (Notes §4.8)

The tension passes through $O$, so its moment is zero; the weight gives $\mathbf r\times\mathbf W=\ell\,\mathbf e_r\times(-mg\sin\theta\,\mathbf e_\theta)=-mg\ell\sin\theta\,\mathbf k$. Product rule:

$$\frac{d}{dt}\big(m\ell^2\dot\theta\big)=m\big(2\ell\dot\ell\dot\theta+\ell^2\ddot\theta\big)=m\ell\big(\ell\ddot\theta+2\dot\ell\dot\theta\big)=-mg\ell\sin\theta$$

which is the equation of (c) multiplied by $m\ell$. With gravity $\mathbf H_O$ is not conserved.

#### Step 3. Gravity-free case

With $g=0$ the right-hand side vanishes: $\ell^2\dot\theta=h$ constant. In the tension, $\dot\theta=h/\ell^2$:

$$T=m\ell\dot\theta^2=m\ell\frac{h^2}{\ell^4}=\frac{mh^2}{\ell^3}$$

The transverse speed $\ell\dot\theta=h/\ell$ grows as the string shortens, and the tension grows like $\ell^{-3}$: whoever reels the tether in must pull harder and harder.

#### Step 4. Numbers

$h=\ell_0\cdot(\ell_0\dot\theta_0)=2\cdot1=2$ m$^2$ s$^{-1}$. $\ell=0.5$ m is reached at $t=(2-0.5)/0.5=3$ s. Then $\dot\theta=2/0.25=8$ rad s$^{-1}$, $\ell\dot\theta=4$ m s$^{-1}$, $|\mathbf v|=\sqrt{u^2+(\ell\dot\theta)^2}=\sqrt{0.25+16}=4.031$ m s$^{-1}$ and $T=0.5\cdot4/0.125=16$ N, compared with $T=0.5\cdot4/8=0.25$ N at the start.

## (e) Who supplies the kinetic energy? [2.0 pts]

Show that $\dfrac{d}{dt}\big(E_{kin}+V\big)=T\,u$ and explain why this is the power of the hauling force. For $g=0$ and the data of (d), compute the work done by the hauling force between $\ell_0=2$ m and $\ell=0.5$ m and check it against the change in kinetic energy.

### Hint

The power of the tension on $P$ is $\mathbf T\cdot\mathbf v$. To integrate $T\,u\,dt$, change the variable to $\ell$ with $d\ell=-u\,dt$.

### Checkpoint

- $\mathbf T\cdot\mathbf v=-T\,\dot\ell=T\,u>0$: the tension does positive work although it is "a constraint force".
- $W_{haul}=\dfrac{mh^2}{2}\Big(\dfrac1{\ell^2}-\dfrac1{\ell_0^2}\Big)=3.75$ J $=\Delta E_{kin}$.

### Solution

#### Step 1. Power of the tension

$\mathbf T\cdot\mathbf v=-T\,\mathbf e_r\cdot\big(\dot\ell\,\mathbf e_r+\ell\dot\theta\,\mathbf e_\theta\big)=-T\dot\ell=Tu$. On a fixed string ($\dot\ell=0$) the tension is orthogonal to the velocity and does no work; here the constraint moves and it does.

#### Step 2. Energy balance (Notes §4.4)

The work-energy theorem gives $\dfrac{dE_{kin}}{dt}=\mathbf W\cdot\mathbf v+\mathbf T\cdot\mathbf v$, and the weight derives from $V=mgy_P=-mg\ell\cos\theta$, so $\mathbf W\cdot\mathbf v=-dV/dt$. Hence

$$\frac{d}{dt}\Big(\tfrac12m\big(\dot\ell^2+\ell^2\dot\theta^2\big)-mg\ell\cos\theta\Big)=Tu$$

The string is massless and the ring smooth, so the tension has the same value $T$ at the free end, which moves with speed $u$ along the pull: the hauler's power is $Tu$. The mechanical energy of $P$ is **not** a first integral. Integrating the balance from $0$ to $t$ (Barrow's rule) gives instead

$$E_{kin}(t)+V(t)-W_{haul}(t)=E_{kin}(0)+V(0),\qquad W_{haul}(t)=\int_0^tT\,u\,dt'$$

that is, the energy of $P$ grows by exactly the work done by the hauler. This is an energy balance, not a first integral in the strict sense: $W_{haul}(t)$ depends on the whole history $T(t')$, not on the state $(\theta,\dot\theta,t)$ alone.

#### Step 3. Work for $g=0$

With $T=mh^2/\ell^3$, change the variable to $\ell'=\ell_0-ut'$: $d\ell'=-u\,dt'$, so $dt'=-d\ell'/u$, and the limits become $t'=0\mapsto\ell'=\ell_0$, $t'=t\mapsto\ell'=\ell$:

$$W_{haul}=\int_0^{t}Tu\,dt'=\int_{\ell_0}^{\ell}\frac{mh^2}{\ell'^3}\,u\,\Big(-\frac{d\ell'}{u}\Big)=\int_{\ell}^{\ell_0}\frac{mh^2}{\ell'^3}\,d\ell'$$

An antiderivative of $mh^2\ell'^{-3}$ is $F(\ell')=-\dfrac{mh^2}{2\ell'^2}$ (check: $F'=-\tfrac{mh^2}{2}(-2)\ell'^{-3}=mh^2\ell'^{-3}$). Barrow's rule:

$$W_{haul}=F(\ell_0)-F(\ell)=-\frac{mh^2}{2\ell_0^2}-\Big(-\frac{mh^2}{2\ell^2}\Big)=\frac{mh^2}{2}\Big(\frac1{\ell^2}-\frac1{\ell_0^2}\Big)$$

With the data: $\tfrac{0.5\cdot4}{2}\big(4-0.25\big)=3.75$ J.

#### Step 4. Check

$E_{kin}=\tfrac12m\big(u^2+h^2/\ell^2\big)$: from $\tfrac12\cdot0.5\,(0.25+1)$ to $\tfrac12\cdot0.5\,(0.25+16)$, a change of $\tfrac12\cdot0.5\cdot15=3.75$ J. The radial part $u^2$ is the same at both ends, so all the work goes into the transverse motion.

## (f) Extension: the amplitude of small swings while hauling [2.0 pts]

> [!note] Extension
> This part goes beyond the course (adiabatic invariants and Bessel functions are not in the Notes). It is included because the result is a classic trap: neither the energy nor the angular momentum is conserved, so neither gives the amplitude.

For small angles, rewrite the equation of (c) with $\ell$ as the independent variable. Show that, when the hauling is slow ($u\ll\sqrt{g\ell}$), the angular amplitude grows like $\ell^{-3/4}$, and check it with the data of the Setup between $\ell_0=1$ m and $\ell=0.25$ m. Grading: the 2.0 points are for the change of variable (chain rule) and the reduced equation in $\ell$; the solution with Bessel functions and the $\ell^{-3/4}$ law are an extension, shown for completeness and not expected in the exam.

### Hint

$\dot\theta=\theta'\dot\ell=-u\,\theta'$ (prime: $d/d\ell$). Only the change of variable and the reduced ODE are graded; the rest is an extension. For the extension: the equation $x\,y''+2y'+y=0$ has the solution $y=x^{-1/2}J_1(2\sqrt x)$.

### Checkpoint

- Graded: $\dot\theta=-u\,\theta'$, $\ddot\theta=u^2\theta''$ (chain rule) and the reduced equation below. Everything after it (Bessel solution, $\ell^{-3/4}$ law, numbers) is an extension, not expected in the exam.
- $\ell\,\theta''+2\theta'+\dfrac{g}{u^2}\,\theta=0$, i.e. $\dfrac1\ell\dfrac{d}{d\ell}\big(\ell^2\theta'\big)+\dfrac{g}{u^2}\theta=0$.
- $\theta=\ell^{-1/2}\big[A\,J_1(z)+B\,Y_1(z)\big]$, $z=2\sqrt{g\ell}/u$; for $z\gg1$, $J_1,Y_1\sim\sqrt{2/(\pi z)}$ times a cosine, so the amplitude is $\propto\ell^{-1/2}\ell^{-1/4}=\ell^{-3/4}$.
- From $1$ m to $0.25$ m: $\theta_a=0.05\cdot4^{3/4}=0.1414$ rad; a numerical integration of the full equation agrees within $0.2\,\%$.

### Solution

#### Step 1. Change of variable

For $\theta(t)=\Theta(\ell(t))$, the chain rule gives $\dot\theta=\Theta'\dot\ell=-u\Theta'$ and $\ddot\theta=\dfrac{d}{dt}(-u\Theta')=-u\Theta''\dot\ell=u^2\Theta''$. With $\sin\theta\approx\theta$ the equation of (c) becomes

$$\ell u^2\Theta''+2(-u)(-u\Theta')+g\Theta=0\ \Longrightarrow\ \ell\,\Theta''+2\Theta'+\frac{g}{u^2}\Theta=0$$

and since $\dfrac{d}{d\ell}\big(\ell^2\Theta'\big)=\ell^2\Theta''+2\ell\Theta'$, it is $\dfrac1\ell\big(\ell^2\Theta'\big)'+\dfrac{g}{u^2}\Theta=0$.

#### Step 2. Exact solution

With $x=g\ell/u^2$ the equation is $x\,y''+2y'+y=0$, whose solutions are $x^{-1/2}J_1(2\sqrt x)$ and $x^{-1/2}Y_1(2\sqrt x)$ (Bessel functions of order 1). So

$$\theta=\ell^{-1/2}\Big[A\,J_1\Big(\frac{2\sqrt{g\ell}}{u}\Big)+B\,Y_1\Big(\frac{2\sqrt{g\ell}}{u}\Big)\Big]$$

#### Step 3. Slow hauling

For large argument $J_1(z)\approx\sqrt{2/(\pi z)}\cos(z-3\pi/4)$ (and $Y_1$ with a sine). With $z\propto\ell^{1/2}$ the envelope is $\ell^{-1/2}z^{-1/2}\propto\ell^{-3/4}$:

$$\theta_a\propto\ell^{-3/4}$$

The condition $z\gg1$ is $u\ll\sqrt{g\ell}$: the length changes little during one swing. The same law follows from the adiabatic invariant $E_{osc}/\omega$ with $E_{osc}\approx\tfrac12mg\ell\theta_a^2$ and $\omega=\sqrt{g/\ell}$: $\ell^{3/2}\theta_a^2$ stays constant.

#### Step 4. Numbers

At $\ell=0.25$ m, $z=2\sqrt{9.81\cdot0.25}/0.01=313\gg1$ and $u/\sqrt{g\ell}=0.0064$. The law predicts $\theta_a=0.05\,(0.25)^{-3/4}=0.05\cdot2.828=0.1414$ rad: the swing angle almost triples, while the horizontal excursion $\ell\theta_a\propto\ell^{1/4}$ shrinks by the factor $0.707$. A Runge-Kutta integration of $(\ell_0-ut)\ddot\theta-2u\dot\theta+g\sin\theta=0$ gives $0.1401$ rad at the last turning point ($\ell=0.253$ m), where the law gives $0.1400$ rad.

## Interpretation

- **Dimensional check:** every term of $\ell\ddot\theta+2\dot\ell\dot\theta+g\sin\theta$ is m s$^{-2}$; $[mh^2/\ell^3]=\text{kg}\,\text{m}^4\text{s}^{-2}/\text{m}^3=$ N; $[Tu]=$ W; $g\ell/u^2$ is dimensionless.
- **Limits:** $u=0$ gives the simple pendulum with $T=m(g\cos\theta+\ell\dot\theta^2)$ and energy conservation; $u<0$ (paying the string out) turns $-2u\dot\theta$ into a true damping and the amplitude decreases like $\ell^{-3/4}$.
- **Common mistakes in the exam:** (1) forgetting the Coriolis-like term $2\dot\ell\dot\theta$ when $\ell$ varies; (2) claiming that the tension does no work because "it is a constraint force" (it does, because the constraint is rheonomic); (3) writing energy conservation for $P$; (4) using $\ell^2\dot\theta=$ const with gravity (the weight has a moment about $O$); (5) believing that $T$ stays bounded in the gravity-free case.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
