---
materia: Engineering Mechanics
tema: "Units 2, 3 and 5: a moving constraint, reactions between two bodies and first integrals of a system"
bank_id: P16
title: "Particle on a free wedge: a moving constraint, the reaction, momentum and energy, and the limit of a massless wedge"
category: midterm_problem
archetype: constraints
level: standard
unit: 3
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p16.py"
tags:
  - problem-bank
  - midterm-1
  - moving-constraint
  - reaction-forces
  - translating-frame
  - linear-momentum
  - energy
---

# Bank P16 — Particle on a free wedge

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §6.4 and §6.5 (constraint forces, their power, dynamical decoupling), §3.2 and §4.9 (motion relative to a translating frame), §4.5 (mechanical energy) and the linear momentum theorem for a system of particles. Every number was checked with SymPy.

## Statement

A wedge of mass $M$ rests on a smooth horizontal table. Its upper face is a smooth plane inclined at the angle $\alpha$ ($0<\alpha<\pi/2$) to the horizontal, descending towards $-x$; the top edge is $A$ and the corner of the wedge under $A$ is $B$. A particle $P$ of mass $m$ is placed on the incline. The inertial frame is $S_0=\{O;\mathbf i,\mathbf j\}$ ($x$ horizontal, $y$ vertical upwards, gravity $-g\,\mathbf j$). The wedge translates without rotating (it does not tip), and its position is the abscissa $X$ of $B$. The position of $P$ on the incline is the distance $s=|AP|$ measured from $A$ **down the slope**, along the unit vector $\mathbf u=-\cos\alpha\,\mathbf i-\sin\alpha\,\mathbf j$; $\mathbf n=-\sin\alpha\,\mathbf i+\cos\alpha\,\mathbf j$ is the unit normal of the incline pointing out of the wedge. Both bodies are released from rest at $t=0$ with $s=0$.

![[attachments/EM-M1/p16-free-wedge.svg]]

## Setup

- Data: $m$, $M$, $\alpha$, $g$. Numerical parts: $\alpha=30^\circ$, $M=2m$, and the particle has slid a distance $L$ along the incline.
- Hypotheses: point particle, rigid wedge translating on the table, all contacts smooth (no friction), $S_0$ inertial; the contact of $P$ with the incline is unilateral ($N\ge0$, checked in (d)).
- Frames: $S_0$ and the frame $S_1=\{A;\mathbf n,\mathbf u\}$ attached to the wedge, ordered so that it is right-handed: $\mathbf n\times\mathbf u=\big[(-\sin\alpha)(-\sin\alpha)-\cos\alpha\,(-\cos\alpha)\big]\mathbf k=\mathbf k$ (the order $\{\mathbf u,\mathbf n\}$ would give $\mathbf u\times\mathbf n=-\mathbf k$, a left-handed basis). $S_1$ **translates** with acceleration $\ddot X\,\mathbf i$ and does not rotate.
- Basis change: $\mathbf i=-\sin\alpha\,\mathbf n-\cos\alpha\,\mathbf u$, $\ \mathbf j=\cos\alpha\,\mathbf n-\sin\alpha\,\mathbf u$ (from $\mathbf i\cdot\mathbf n=-\sin\alpha$, $\mathbf i\cdot\mathbf u=-\cos\alpha$, $\mathbf j\cdot\mathbf n=\cos\alpha$, $\mathbf j\cdot\mathbf u=-\sin\alpha$).

In matrix form:

$$\begin{pmatrix}\mathbf i\\ \mathbf j\end{pmatrix}=[R]\begin{pmatrix}\mathbf n\\ \mathbf u\end{pmatrix},\qquad [R]=\begin{pmatrix}-\sin\alpha & -\cos\alpha\\ \cos\alpha & -\sin\alpha\end{pmatrix}$$

with $[R][R]^T=\begin{pmatrix}\sin^2\alpha+\cos^2\alpha & -\sin\alpha\cos\alpha+\cos\alpha\sin\alpha\\ -\sin\alpha\cos\alpha+\cos\alpha\sin\alpha & \cos^2\alpha+\sin^2\alpha\end{pmatrix}=I$ and $\det[R]=\sin^2\alpha+\cos^2\alpha=+1$.

## (a) Degrees of freedom and constraints [1.0 pts]

How many degrees of freedom has the system particle + wedge? Classify the constraint that keeps $P$ on the incline, as seen in $S_0$ and in $S_1$.

### Hint

The motion of the wedge is **not** prescribed: it is an unknown of the problem.

### Checkpoint

- 2 degrees of freedom, $(X,s)$.
- $P$ on the incline: holonomic, unilateral, smooth; scleronomic as a relation between the coordinates $(X,s)$ of the system (no explicit $t$); it would be rheonomic for $P$ alone only if $X(t)$ were a prescribed function of time, which it is not here.

### Solution

#### Step 1. Count

The wedge is a rigid body in the plane (3 coordinates); the table fixes its height and, since it does not tip, its orientation: 1 coordinate $X$ remains. The particle has 2 coordinates in the plane; staying on the incline removes one, leaving $s$. In total **2 degrees of freedom**, $(X,s)$. Unlike a fixed incline, $X(t)$ is an unknown: the motion of the support depends on the motion of the particle.

#### Step 2. Classification

The condition "$P$ on the incline" reads $\overrightarrow{AP}\cdot\mathbf n=0$, i.e. $-(x_P-X)\sin\alpha+(y_P-h)\cos\alpha=0$ with $\overrightarrow{OA}=X\,\mathbf i+h\,\mathbf j$, a relation between the positions of $P$ and of the wedge: it is **holonomic** and, written in the system coordinates $(X,s)$ (or $(X,x_P,y_P)$), it contains no explicit time, so it is **scleronomic**. It would be rheonomic for $P$ alone only if the motion $X(t)$ of the wedge were prescribed from outside; here $X$ is an unknown, so the time enters only through the coordinates. In $S_1$ the plane is fixed. It is **unilateral**: $P$ can leave the plane upwards, so it holds only while $N\ge0$. Smooth: the reaction is $\mathbf N=N\,\mathbf n$, with no component along $\mathbf u$ (Notes §6.4).

## (b) Kinematics of $P$ [1.5 pts]

Write the position, velocity and acceleration of $P$ relative to $S_1$ and in $S_0$, in the basis $\{\mathbf n,\mathbf u\}$.

### Hint

$S_1$ does not rotate, so $\mathbf v_P=\mathbf v_A+\mathbf v_{rel}$ and $\mathbf a_P=\mathbf a_A+\mathbf a_{rel}$ with $\mathbf a_A=\ddot X\,\mathbf i$.

### Checkpoint

- $\mathbf r_{rel}=s\,\mathbf u$, $\ \mathbf v_{rel}=\dot s\,\mathbf u$, $\ \mathbf a_{rel}=\ddot s\,\mathbf u$.
- $\mathbf a_P=\ddot X\,\mathbf i+\ddot s\,\mathbf u=(\ddot s-\ddot X\cos\alpha)\,\mathbf u-\ddot X\sin\alpha\,\mathbf n$.

### Solution

#### Step 1. Relative motion

$\mathbf u$ is fixed in $S_1$, so $\mathbf r_{rel}=\overrightarrow{AP}=s\,\mathbf u$, $\ \mathbf v_{rel}=\dot s\,\mathbf u$, $\ \mathbf a_{rel}=\ddot s\,\mathbf u$. The relative velocity is tangent to the incline.

#### Step 2. Absolute motion

$\overrightarrow{OA}=X\,\mathbf i+h\,\mathbf j$ with the height $h$ of the wedge constant, so $\mathbf v_A=\dot X\,\mathbf i$, $\mathbf a_A=\ddot X\,\mathbf i$. Since $\boldsymbol\omega_{10}=\mathbf 0$ (Notes §3.2):

$$\mathbf v_P=\dot X\,\mathbf i+\dot s\,\mathbf u,\qquad \mathbf a_P=\ddot X\,\mathbf i+\ddot s\,\mathbf u$$

Substituting $\mathbf i=-\cos\alpha\,\mathbf u-\sin\alpha\,\mathbf n$:

$$\mathbf a_P=(\ddot s-\ddot X\cos\alpha)\,\mathbf u-\ddot X\sin\alpha\,\mathbf n$$

and in Cartesian components $\mathbf v_P=(\dot X-\dot s\cos\alpha)\,\mathbf i-\dot s\sin\alpha\,\mathbf j$.

## (c) Equations of motion and the reaction [2.5 pts]

Write the forces on $P$ in $S_1$, including the inertia force, and on the wedge. Obtain $\ddot X$, $\ddot s$ and $N$, and the reaction of the table on the wedge.

### Hint

Project $m\mathbf a_{rel}=\mathbf W+\mathbf N+\mathbf F_{in}$ on $\mathbf u$ (no $N$) and on $\mathbf n$. The wedge receives $-\mathbf N$ (action and reaction); its horizontal equation closes the system.

### Checkpoint

- $\ddot s=g\sin\alpha+\ddot X\cos\alpha$, $\ N=m(g\cos\alpha-\ddot X\sin\alpha)$, $\ M\ddot X=N\sin\alpha$.
- $\ddot X=\dfrac{m\,g\sin\alpha\cos\alpha}{M+m\sin^2\alpha}$, $\ \ddot s=\dfrac{(M+m)\,g\sin\alpha}{M+m\sin^2\alpha}$, $\ N=\dfrac{M\,m\,g\cos\alpha}{M+m\sin^2\alpha}$.
- Table reaction $R=Mg+N\cos\alpha$.

### Solution

#### Step 1. Forces on $P$ in $S_1$

Weight $\mathbf W=-mg\,\mathbf j=mg\sin\alpha\,\mathbf u-mg\cos\alpha\,\mathbf n$; reaction $\mathbf N=N\,\mathbf n$; inertia force of the translating frame (Notes §4.9) $\mathbf F_{in}=-m\,\mathbf a_A=-m\ddot X\,\mathbf i=m\ddot X\cos\alpha\,\mathbf u+m\ddot X\sin\alpha\,\mathbf n$. There is no Coriolis or centrifugal force ($\boldsymbol\omega_{10}=\mathbf 0$).

#### Step 2. Projections for $P$

$m\,\ddot s\,\mathbf u=\mathbf W+\mathbf N+\mathbf F_{in}$:

$$\mathbf u:\quad m\ddot s=mg\sin\alpha+m\ddot X\cos\alpha\ \Longrightarrow\ \ddot s=g\sin\alpha+\ddot X\cos\alpha$$

$$\mathbf n:\quad 0=-mg\cos\alpha+N+m\ddot X\sin\alpha\ \Longrightarrow\ N=m\big(g\cos\alpha-\ddot X\sin\alpha\big)$$

The $\mathbf u$ equation is free of the reaction (dynamical decoupling, Notes §6.5), but it still contains the unknown $\ddot X$.

#### Step 3. The wedge

Forces on the wedge: its weight $-Mg\,\mathbf j$, the table reaction $R\,\mathbf j$ (smooth table, vertical) and $-\mathbf N=-N\mathbf n=N\sin\alpha\,\mathbf i-N\cos\alpha\,\mathbf j$. Newton for the translating wedge, $M\ddot X\,\mathbf i=-Mg\,\mathbf j+R\,\mathbf j-N\mathbf n$:

$$\mathbf i:\quad M\ddot X=N\sin\alpha,\qquad \mathbf j:\quad 0=R-Mg-N\cos\alpha$$

#### Step 4. Solve

Substituting $N$ of Step 2 in the wedge equation: $M\ddot X=m\sin\alpha\,(g\cos\alpha-\ddot X\sin\alpha)$, so $\ddot X\,(M+m\sin^2\alpha)=m\,g\sin\alpha\cos\alpha$:

$$\ddot X=\frac{m\,g\sin\alpha\cos\alpha}{M+m\sin^2\alpha}$$

Then, with $\sin^2\alpha+\cos^2\alpha=1$:

$$\ddot s=g\sin\alpha+\frac{m\,g\sin\alpha\cos^2\alpha}{M+m\sin^2\alpha}=\frac{g\sin\alpha\,(M+m\sin^2\alpha+m\cos^2\alpha)}{M+m\sin^2\alpha}=\frac{(M+m)\,g\sin\alpha}{M+m\sin^2\alpha}$$

$$N=mg\cos\alpha-\frac{m^2g\sin^2\alpha\cos\alpha}{M+m\sin^2\alpha}=\frac{M\,m\,g\cos\alpha}{M+m\sin^2\alpha}$$

and $R=Mg+N\cos\alpha$. All three accelerations are **constant**. Check with the system: the vertical external forces are $R-(M+m)g=N\cos\alpha-mg$, which equals $m\,\mathbf a_P\cdot\mathbf j=-m\ddot s\sin\alpha$ (the wedge has no vertical acceleration). An independent check with the Lagrange equations in $(X,s)$ gives the same $\ddot X$ and $\ddot s$.

#### Step 5. Numbers ($\alpha=30^\circ$, $M=2m$)

$M+m\sin^2\alpha=2m+m/4=\tfrac94m$: $\ \ddot X=\dfrac{mg\cdot\frac12\cdot\frac{\sqrt3}2}{\frac94m}=\dfrac{\sqrt3}{9}g=0.1925\,g$, $\ \ddot s=\dfrac{3m\,g\cdot\frac12}{\frac94m}=\dfrac23g$, $\ N=\dfrac{2m\cdot m\,g\frac{\sqrt3}2}{\frac94m}=\dfrac{4\sqrt3}{9}mg=0.7698\,mg$ (smaller than $mg\cos30^\circ=0.866\,mg$ on a fixed wedge).

## (d) Limits, the sign of $N$ and the massless wedge [1.5 pts]

Check that $N>0$ for every $M>0$. Study the limits $M\to\infty$ and $M\to0$. In the second one a student says: "the particle slides down a plane, so it accelerates along the incline with $g\sin\alpha$ times some factor and presses on it". Discuss.

### Hint

Compute the absolute acceleration $\mathbf a_P=\ddot X\,\mathbf i+\ddot s\,\mathbf u$ in the limit $M\to0$.

### Checkpoint

- $N>0$ for $M>0$ and $0<\alpha<\pi/2$: the particle never leaves the incline; $R>Mg>0$.
- $M\to\infty$: $\ddot X\to0$, $\ddot s\to g\sin\alpha$, $N\to mg\cos\alpha$ (fixed incline).
- $M\to0$: $N\to0$, $\ddot X\to g\cot\alpha$, $\ddot s\to g/\sin\alpha$ and $\mathbf a_P\to-g\,\mathbf j$: **free fall**; the massless wedge is pushed away just fast enough to stay in contact without force.
- The factor $\ddot s/(g\sin\alpha)=(M+m)/(M+m\sin^2\alpha)\ge1$ grows to $1/\sin^2\alpha$ as $M\to0$; the student's error is "presses on the wedge", since $N\to0$.

### Solution

#### Step 1. Sign of the reaction

$N=\dfrac{Mmg\cos\alpha}{M+m\sin^2\alpha}$: numerator and denominator are positive for $M>0$ and $0<\alpha<\pi/2$, so $N>0$ throughout the motion (the accelerations are constant, so $N$ is too). The unilateral constraint is never violated, and $R=Mg+N\cos\alpha>Mg>0$: the wedge stays on the table.

#### Step 2. Heavy wedge

Dividing numerator and denominator by $M$ and letting $M\to\infty$ ($m/M\to0$): $\ddot X\to0$, $\ddot s\to g\sin\alpha$, $N\to mg\cos\alpha$, the results of a fixed incline.

#### Step 3. Massless wedge (the trap)

Setting $M=0$: $N\to0$, $\ddot X\to\dfrac{mg\sin\alpha\cos\alpha}{m\sin^2\alpha}=g\cot\alpha$, $\ddot s\to\dfrac{mg\sin\alpha}{m\sin^2\alpha}=\dfrac{g}{\sin\alpha}$. The absolute acceleration is

$$\mathbf a_P=g\cot\alpha\,\mathbf i+\frac{g}{\sin\alpha}\big(-\cos\alpha\,\mathbf i-\sin\alpha\,\mathbf j\big)=-g\,\mathbf j$$

The particle **falls freely**; the incline exerts no force on it. A massless wedge cannot push back ($M\ddot X=N\sin\alpha$ with $M=0$ forces $N=0$), so it flies away horizontally with $g\cot\alpha$, exactly the motion that keeps the surface under the falling particle. The first half of the student's statement is harmless: $\ddot s=g\sin\alpha\cdot\dfrac{M+m}{M+m\sin^2\alpha}$ is indeed $g\sin\alpha$ times a factor, and this factor is $\ge1$ for every $M$ (because $M+m\ge M+m\sin^2\alpha$), growing from $1$ ($M\to\infty$) to $1/\sin^2\alpha$ ($M\to0$), which gives $\ddot s\to g/\sin\alpha$. The error is the second half, "the particle presses on the wedge": $N\to0$, the incline exerts no force and the particle is in free fall, merely accompanied by the surface.

## (e) First integrals and the speeds after sliding a distance $L$ [2.0 pts]

Show that the horizontal linear momentum of the system and its mechanical energy are conserved, explaining why the reaction $\mathbf N$ does no net work although it works on each body. For $\alpha=30^\circ$, $M=2m$, find $\dot s$, $\dot X$ and $|\mathbf v_P|$ when $P$ has slid a distance $L$, and the work of $\mathbf N$ on $P$ and on the wedge.

### Hint

The external forces on the system (weights, table reaction) are vertical. The power of $\mathbf N$ on $P$ plus that of $-\mathbf N$ on the wedge is $\mathbf N\cdot(\mathbf v_P-\mathbf v_A)=\mathbf N\cdot\mathbf v_{rel}$.

### Checkpoint

- $p_x=M\dot X+m(\dot X-\dot s\cos\alpha)=0\Rightarrow\dot X=\dfrac{m\cos\alpha}{M+m}\,\dot s$; $\ \tfrac12M\dot X^2+\tfrac12m|\mathbf v_P|^2-mgs\sin\alpha=0$.
- $\alpha=30^\circ$, $M=2m$: $E_{kin}=\tfrac38m\dot s^2$, $\dot s^2=\tfrac43gL$ ($\dot s=1.1547\sqrt{gL}$), $\dot X=\tfrac13\sqrt{gL}$, $|\mathbf v_P|=\tfrac{\sqrt7}{3}\sqrt{gL}=0.8819\sqrt{gL}$.
- Work of $\mathbf N$ on $P$: $-\tfrac19mgL$; on the wedge: $+\tfrac19mgL$; total 0.

### Solution

#### Step 1. Horizontal momentum

The external forces on the system $\{P,\text{wedge}\}$ are $-mg\,\mathbf j$, $-Mg\,\mathbf j$ and $R\,\mathbf j$: no horizontal component. $\mathbf N$ is internal (action-reaction pair). The linear momentum theorem gives $\frac{d}{dt}p_x=0$, with $p_x=M\dot X+m\,\mathbf v_P\cdot\mathbf i=M\dot X+m(\dot X-\dot s\cos\alpha)$. From rest, $p_x=0$:

$$\dot X=\frac{m\cos\alpha}{M+m}\,\dot s$$

Consequently the centre of mass has $\ddot x_G=0$ and moves only vertically.

#### Step 2. Energy

Powers: the weights are conservative; $R\,\mathbf j\cdot\dot X\,\mathbf i=0$; the pair $\mathbf N$, $-\mathbf N$ has total power

$$\mathbf N\cdot\mathbf v_P+(-\mathbf N)\cdot\mathbf v_A=\mathbf N\cdot(\mathbf v_P-\mathbf v_A)=N\,\mathbf n\cdot\dot s\,\mathbf u=0$$

because the relative velocity is tangent to the smooth incline (Notes §6.4). So the mechanical energy of the system is constant (Notes §4.5). With the zero of potential energy at $s=0$, the height of $P$ changes by $-s\sin\alpha$:

$$\tfrac12M\dot X^2+\tfrac12m\big[(\dot X-\dot s\cos\alpha)^2+\dot s^2\sin^2\alpha\big]-mg\,s\sin\alpha=0$$

#### Step 3. Kinetic energy for $\alpha=30^\circ$, $M=2m$

$\dot X=\frac{m\cdot\frac{\sqrt3}2}{3m}\,\dot s=\frac{\sqrt3}{6}\,\dot s$. For $P$: $\dot X-\dot s\cos\alpha=\big(\tfrac{\sqrt3}{6}-\tfrac{3\sqrt3}{6}\big)\dot s=-\tfrac{\sqrt3}{3}\dot s$, whose square is $\tfrac13\dot s^2$, and $\dot s^2\sin^2\alpha=\tfrac14\dot s^2$, so $|\mathbf v_P|^2=\tfrac7{12}\dot s^2$ and $\tfrac12m|\mathbf v_P|^2=\tfrac7{24}m\dot s^2$. For the wedge: $\dot X^2=\tfrac3{36}\dot s^2=\tfrac1{12}\dot s^2$ and $\tfrac12(2m)\tfrac1{12}\dot s^2=\tfrac2{24}m\dot s^2$. Total:

$$E_{kin}=\frac{2+7}{24}\,m\dot s^2=\frac38\,m\dot s^2$$

#### Step 4. Speeds after sliding $L$

With $s=L$ and $mgL\sin30^\circ=\tfrac12mgL$:

$$\tfrac38m\dot s^2=\tfrac12mgL\ \Longrightarrow\ \dot s^2=\tfrac43gL,\quad \dot s=1.1547\sqrt{gL},\quad \dot X=\tfrac{\sqrt3}{6}\cdot\tfrac2{\sqrt3}\sqrt{gL}=\tfrac13\sqrt{gL}$$

$$|\mathbf v_P|^2=\tfrac7{12}\cdot\tfrac43gL=\tfrac79gL,\qquad |\mathbf v_P|=\tfrac{\sqrt7}{3}\sqrt{gL}=0.8819\sqrt{gL}$$

Check with (c): constant $\ddot s=\tfrac23g$ from rest gives $\dot s^2=2\ddot sL=\tfrac43gL$. The time to slide $L$ is $\sqrt{2L/\ddot s}=\sqrt{3L/g}$ and the wedge has moved $\Delta X=\tfrac{\sqrt3}{6}L=0.2887\,L$ towards $+x$.

#### Step 5. Work of the reaction on each body

Kinetic energy theorem for $P$ alone: $\tfrac12m|\mathbf v_P|^2=W_{weight}+W_{N\to P}$ with $W_{weight}=\tfrac12mgL$: $W_{N\to P}=\tfrac7{18}mgL-\tfrac9{18}mgL=-\tfrac19mgL$. For the wedge: $W_{-N\to wedge}=\tfrac12(2m)\dot X^2=\tfrac19mgL$. The reaction **does** work on each body (the incline moves), but the two works cancel: energy is transferred from $P$ to the wedge.

## (f) The absolute path of $P$ [1.5 pts]

Show that $P$ moves along a straight line in $S_0$ and find the angle $\beta$ of this line with the horizontal. Compare it with $\alpha$ for $\alpha=30^\circ$, $M=2m$.

### Hint

Both bodies start from rest with constant accelerations, so $\mathbf v_P(t)=\mathbf a_P\,t$.

### Checkpoint

- $\tan\beta=\dfrac{\ddot s\sin\alpha}{\ddot s\cos\alpha-\ddot X}=\Big(1+\dfrac mM\Big)\tan\alpha$.
- $\alpha=30^\circ$, $M=2m$: $\tan\beta=\tfrac{\sqrt3}{2}$, $\beta=40.89^\circ>\alpha$.

### Solution

#### Step 1. A straight path

$\mathbf a_P=\ddot X\,\mathbf i+\ddot s\,\mathbf u$ is a constant vector (part (c)). Integrating twice from rest (Barrow): $\mathbf v_P=\mathbf a_P\,t$ and $\mathbf r_P-\mathbf r_P(0)=\tfrac12\mathbf a_P\,t^2$, so $P$ moves along the fixed straight line through its initial position with direction $\mathbf a_P$.

#### Step 2. Its slope

In Cartesian components $\mathbf a_P=(\ddot X-\ddot s\cos\alpha)\,\mathbf i-\ddot s\sin\alpha\,\mathbf j$; the line descends towards $-x$ with

$$\tan\beta=\frac{\ddot s\sin\alpha}{\ddot s\cos\alpha-\ddot X}=\frac{\sin\alpha}{\cos\alpha-\dfrac{\ddot X}{\ddot s}}$$

From (c), $\dfrac{\ddot X}{\ddot s}=\dfrac{m\cos\alpha}{M+m}$ (the same ratio as $\dot X/\dot s$ in (e)), so $\cos\alpha-\dfrac{m\cos\alpha}{M+m}=\dfrac{M\cos\alpha}{M+m}$ and

$$\tan\beta=\frac{(M+m)\sin\alpha}{M\cos\alpha}=\Big(1+\frac mM\Big)\tan\alpha$$

#### Step 3. Numbers

$\tan\beta=\tfrac32\cdot\tfrac1{\sqrt3}=\tfrac{\sqrt3}2=0.8660$, $\beta=40.89^\circ$. The particle descends **more steeply** than the incline, because the incline recedes under it. Check with (e): $|v_{Py}|/|v_{Px}|=\sqrt{gL/3}\big/\tfrac23\sqrt{gL}=\tfrac{\sqrt3}2$.

## Interpretation

- **Dimensional check:** $\ddot X$ and $\ddot s$ are $g$ times a ratio of masses times trigonometric factors (m s$^{-2}$); $N=Mmg\cos\alpha/(M+m\sin^2\alpha)$ is kg$\cdot$m s$^{-2}$ = N; $\dot s^2=\tfrac43gL$ is m$^2$s$^{-2}$; the works are $mgL$ times numbers (J).
- **Limiting cases:** $M\to\infty$ recovers the fixed incline ($\beta\to\alpha$); $M\to0$ gives free fall ($\beta\to90^\circ$, $\tan\beta\to\infty$); $\alpha\to0$ gives $\ddot X=\ddot s=0$, $N=mg$ (nothing moves); $\alpha\to\pi/2$ gives $N\to0$, $\ddot X\to0$, $\ddot s\to g$ (the particle falls along the vertical face).
- **Common mistakes in the exam:** (1) using $N=mg\cos\alpha$ as on a fixed incline; (2) forgetting the inertia force $-m\ddot X\,\mathbf i$ in $S_1$, or giving it the wrong sign; (3) writing energy conservation for $P$ alone (the reaction works on $P$: $-\tfrac19mgL$ here); (4) assuming the particle's absolute path is parallel to the incline.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
