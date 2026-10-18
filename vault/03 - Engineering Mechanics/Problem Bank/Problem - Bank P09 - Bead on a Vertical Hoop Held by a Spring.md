---
materia: Engineering Mechanics
tema: "Units 2 and 3: motion on a smooth curve, potential energy, equilibria and their stability"
bank_id: P09
title: "Bead on a vertical hoop held by a spring: reaction, equilibria and a pitchfork bifurcation"
category: midterm_problem
archetype: oscillations
level: trap
unit: 2
difficulty: 3
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers; not an official exercise. Verified with scripts/mechanics/p09.py"
tags:
  - problem-bank
  - midterm-1
  - equilibrium
  - stability
  - bifurcation
  - smooth-curve
  - energy
---

# Bank P09 — Bead on a vertical hoop held by a spring

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §6.5 (motion along a smooth curve, reaction), §4.4 to §4.5 (potential energy, conservation of energy), §4.6 (equilibrium and stability) and §4.7 (linearisation about an equilibrium). Every equation and number was checked with SymPy (Lagrange equation as an independent route).

## Statement

A smooth circular hoop of radius $a$ and centre $C$ is fixed in a vertical plane. A bead $P$ of mass $m$ is threaded on it (it can neither leave the hoop nor the plane). A linear spring of stiffness $k$ and natural length $l_0$ joins $P$ to the fixed point $A$, which lies on the vertical through $C$ at the height $d=2a$ above $C$. The natural length is $l_0=d-a=a$, so the spring is unstretched when the bead is at the top $T$ of the hoop. Gravity $-g\,\mathbf j$ acts. The position of the bead is given by the angle $\theta$ between $\mathbf{CT}$ (upward vertical) and $\mathbf{CP}$, positive clockwise in the figure (towards $+x$).

![[attachments/EM-M1/p09-hoop-spring-bead.svg]]

Use the inertial frame $S_0=\{C;\mathbf i,\mathbf j\}$ ($\mathbf i$ horizontal, $\mathbf j$ upward) and the unit vectors $\mathbf e_r=\sin\theta\,\mathbf i+\cos\theta\,\mathbf j$ (along $\mathbf{CP}$) and $\mathbf e_\theta=\cos\theta\,\mathbf i-\sin\theta\,\mathbf j$ (tangent to the hoop, towards increasing $\theta$). The results are expressed with the dimensionless stiffness

$$\kappa=\frac{ka}{mg}$$

## Setup

- Data: $m$, $a$, $k$, $g$; $d=2a$, $l_0=a$. Numerical values in (e) and (f): $a=0.40$ m, $g=9.81$ m/s$^2$.
- Hypotheses: point particle; smooth, rigid, fixed hoop (bilateral constraint); massless linear spring that can be stretched or compressed; $S_0$ inertial.
- Spring length: $l=|\mathbf{AP}|$ with $\mathbf{AP}=a\,\mathbf e_r-d\,\mathbf j$.

## (a) Degrees of freedom, geometry and potential energy [1.5 pts]

How many degrees of freedom has the bead? Find the spring length $l(\theta)$ and the total potential energy $V(\theta)$; check that the applied forces are conservative.

### Hint

Use the cosine rule in the triangle $ACP$, or compute $|\mathbf{AP}|^2$ with $\mathbf j\cdot\mathbf e_r=\cos\theta$. Take the gravitational potential zero at the height of $C$.

### Checkpoint

- 1 degree of freedom, $\theta$ (the hoop removes 2 of the 3 spatial coordinates).
- $l^2=a^2+d^2-2ad\cos\theta=a^2(5-4\cos\theta)$; $\ l(0)=a=l_0$, $\ l(\pi)=3a$.
- $V(\theta)=mga\cos\theta+\tfrac12k\big(l(\theta)-l_0\big)^2$, i.e. $\dfrac{V}{mga}=\cos\theta+\dfrac{\kappa}{2}\Big(\sqrt{5-4\cos\theta}-1\Big)^2$.

### Solution

#### Step 1. Degrees of freedom

A free particle has 3 coordinates. The hoop is a curve: two holonomic, scleronomic constraints (the plane and the circle $|\mathbf{CP}|=a$), so 1 degree of freedom remains, described by $\theta$ (Notes §2.7).

#### Step 2. Spring length

$$l^2=\mathbf{AP}\cdot\mathbf{AP}=(a\,\mathbf e_r-d\,\mathbf j)\cdot(a\,\mathbf e_r-d\,\mathbf j)=a^2-2ad\,(\mathbf e_r\cdot\mathbf j)+d^2=a^2+d^2-2ad\cos\theta$$

With $d=2a$: $l=a\sqrt{5-4\cos\theta}$, from $l(0)=a$ at the top to $l(\pi)=3a$ at the bottom.

#### Step 3. Potentials

Weight: uniform, $V_g=mg\,y_P=mga\cos\theta$. Spring: $V_s=\tfrac12k(l-l_0)^2$, a function of the position only (Notes §4.4). Both are conservative, the reaction of the smooth fixed hoop does no work (part (b)), so

$$V(\theta)=mga\cos\theta+\tfrac12k\big(l(\theta)-l_0\big)^2,\qquad \frac{V}{mga}=\cos\theta+\frac{\kappa}{2}\Big(\sqrt{5-4\cos\theta}-1\Big)^2$$

## (b) Equation of motion and reaction of the hoop [2.0 pts]

Write the kinematics of $P$ in $\{\mathbf e_r,\mathbf e_\theta\}$, the forces, the equation of motion free of the reaction, and the reaction $\mathbf N$ as a function of $\theta$ and $\dot\theta$. Check the equation of motion against $V(\theta)$.

### Hint

$\dot{\mathbf e}_r=\dot\theta\,\mathbf e_\theta$, $\dot{\mathbf e}_\theta=-\dot\theta\,\mathbf e_r$. The spring force on $P$ is $-k(l-l_0)\,\mathbf{AP}/l$. $\mathbf{AP}\cdot\mathbf e_r=a-d\cos\theta$ and $\mathbf{AP}\cdot\mathbf e_\theta=d\sin\theta$.

### Checkpoint

- $\mathbf a_P=a\ddot\theta\,\mathbf e_\theta-a\dot\theta^2\,\mathbf e_r$; $\ \mathbf N=N\,\mathbf e_r$ (smooth hoop, planar forces).
- $ma\ddot\theta=\sin\theta\Big[mg-kd\Big(1-\dfrac{l_0}{l}\Big)\Big]$, equal to $-V'(\theta)/a$.
- $N=mg\cos\theta+k\Big(1-\dfrac{l_0}{l}\Big)(a-d\cos\theta)-ma\dot\theta^2$ (positive: outwards).

### Solution

#### Step 1. Change of basis

The pair $\{\mathbf e_r,\mathbf e_\theta\}$ turns with $\theta$. Since $\theta$ grows clockwise (from $\mathbf j$ towards $\mathbf i$), the right-handed order in the plane is $\{\mathbf e_\theta,\mathbf e_r\}$: with $\mathbf k=\mathbf i\times\mathbf j$, $\mathbf e_\theta\times\mathbf e_r=(\cos\theta\cos\theta+\sin\theta\sin\theta)\,\mathbf k=\mathbf k$ (the order $\{\mathbf e_r,\mathbf e_\theta\}$ has determinant $-1$). Then

$$\begin{pmatrix}\mathbf e_\theta\ \mathbf e_r\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\theta&-\sin\theta\ \sin\theta&\cos\theta\end{pmatrix}$$

with $[R][R]^T=\begin{pmatrix}\cos^2\theta+\sin^2\theta&\cos\theta\sin\theta-\sin\theta\cos\theta\ \sin\theta\cos\theta-\cos\theta\sin\theta&\sin^2\theta+\cos^2\theta\end{pmatrix}=I$ and $\det[R]=\cos^2\theta+\sin^2\theta=+1$.

#### Step 2. Kinematics

$\mathbf r_{CP}=a\,\mathbf e_r$. By the chain rule, $\dot{\mathbf e}_r=\dot\theta(\cos\theta\,\mathbf i-\sin\theta\,\mathbf j)=\dot\theta\,\mathbf e_\theta$ and $\dot{\mathbf e}_\theta=\dot\theta(-\sin\theta\,\mathbf i-\cos\theta\,\mathbf j)=-\dot\theta\,\mathbf e_r$. With $a$ constant:

$$\mathbf v_P=a\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_P=a\ddot\theta\,\mathbf e_\theta+a\dot\theta\,\dot{\mathbf e}_\theta=a\ddot\theta\,\mathbf e_\theta-a\dot\theta^2\,\mathbf e_r$$

#### Step 3. Forces

- Weight: $\mathbf W=-mg\,\mathbf j=-mg\cos\theta\,\mathbf e_r+mg\sin\theta\,\mathbf e_\theta$ (using $\mathbf j\cdot\mathbf e_r=\cos\theta$, $\mathbf j\cdot\mathbf e_\theta=-\sin\theta$).
- Spring: $\mathbf F_s=-k\,\dfrac{l-l_0}{l}\,\mathbf{AP}=-k\Big(1-\dfrac{l_0}{l}\Big)\big[(a-d\cos\theta)\,\mathbf e_r+d\sin\theta\,\mathbf e_\theta\big]$, since $\mathbf{AP}\cdot\mathbf e_r=a-d\cos\theta$ and $\mathbf{AP}\cdot\mathbf e_\theta=-d\,(\mathbf j\cdot\mathbf e_\theta)=d\sin\theta$.
- Reaction: the hoop is smooth, so $\mathbf N$ is orthogonal to the tangent $\mathbf e_\theta$ (Notes §6.5); its component normal to the plane balances nothing (all other forces are in the plane), so $\mathbf N=N\,\mathbf e_r$.

#### Step 4. Equation of motion (tangential projection)

$$ma\ddot\theta=mg\sin\theta-k\Big(1-\frac{l_0}{l}\Big)d\sin\theta=\sin\theta\Big[mg-kd\Big(1-\frac{l_0}{l}\Big)\Big]$$

$N$ does not appear: this is the reaction-free equation.

#### Step 5. Reaction (radial projection)

$$-ma\dot\theta^2=-mg\cos\theta-k\Big(1-\frac{l_0}{l}\Big)(a-d\cos\theta)+N$$

$$N=mg\cos\theta+k\Big(1-\frac{l_0}{l}\Big)(a-d\cos\theta)-ma\dot\theta^2$$

#### Step 6. Check with $V$

By the chain rule, $\dfrac{dV}{d\theta}=-mga\sin\theta+k(l-l_0)\dfrac{dl}{d\theta}$ and, differentiating $l^2=a^2+d^2-2ad\cos\theta$ implicitly, $2l\,l'=2ad\sin\theta$, so $l'=ad\sin\theta/l$. Hence

$$V'(\theta)=\sin\theta\Big[-mga+kad\Big(1-\frac{l_0}{l}\Big)\Big]=-a\cdot ma\ddot\theta$$

which is the energy form $ma^2\ddot\theta=-V'(\theta)$ of Step 4 (the Lagrange equation, an extension beyond the course notes, gives the same).

## (c) Equilibrium positions [2.0 pts]

Find all the equilibrium positions as functions of $\kappa$. Show that besides $\theta=0$ and $\theta=\pi$ there is a symmetric pair $\theta=\pm\theta^*$ only above a critical value $\kappa_c$, and give $\cos\theta^*(\kappa)$.

### Hint

$V'(\theta)=\sin\theta\cdot G(\theta)$: either $\sin\theta=0$ or $G=0$. The second condition fixes $l$; then use $l^2=a^2(5-4\cos\theta)$ and the range $a<l<3a$.

### Checkpoint

- $\theta=0$ (top) and $\theta=\pi$ (bottom) for every $\kappa$.
- $G=0\iff 1-\dfrac{a}{l}=\dfrac{1}{2\kappa}\iff l^*=\dfrac{2\kappa a}{2\kappa-1}$; $\ \cos\theta^*=\dfrac14\Big(5-\dfrac{4\kappa^2}{(2\kappa-1)^2}\Big)$.
- The pair exists only for $\kappa>\kappa_c=\tfrac34$ ($\theta^*\to\pi$ as $\kappa\to\tfrac34^+$, $\theta^*\to0$ as $\kappa\to\infty$).

### Solution

#### Step 1. Factorisation

From (b), with $d=2a$, $l_0=a$ and $k=\kappa mg/a$:

$$\frac{V'(\theta)}{mga}=\sin\theta\Big[-1+2\kappa\Big(1-\frac{a}{l}\Big)\Big]$$

Equilibria are the zeros of $V'$ (Notes §4.6).

#### Step 2. $\sin\theta=0$

$\theta=0$ and $\theta=\pi$ are equilibria for every $\kappa$: by symmetry, the spring force and the weight are both along the vertical there, so they have no tangential component.

#### Step 3. The symmetric pair

$-1+2\kappa(1-a/l)=0\Rightarrow 1-a/l=1/(2\kappa)\Rightarrow l^*=\dfrac{a}{1-1/(2\kappa)}=\dfrac{2\kappa a}{2\kappa-1}$, which requires $\kappa>\tfrac12$ for $l^*>0$. Substituting into $l^2=a^2(5-4\cos\theta)$:

$$\cos\theta^*=\frac14\Big(5-\frac{l^{*2}}{a^2}\Big)=\frac14\Big(5-\frac{4\kappa^2}{(2\kappa-1)^2}\Big)$$

#### Step 4. Existence condition

A point of the hoop has $a\le l\le3a$; a new equilibrium needs $a<l^*<3a$. $l^*>a$ holds for every $\kappa>\tfrac12$. $l^*<3a\iff2\kappa<3(2\kappa-1)\iff\kappa>\tfrac34$. So the pair $\pm\theta^*$ exists only for $\kappa>\kappa_c=\tfrac34$; at $\kappa=\tfrac34$, $\cos\theta^*=\tfrac14(5-9)=-1$: the pair is born **at the bottom**. As $\kappa\to\infty$, $l^*\to a$ and $\theta^*\to0$.

## (d) Stability and the bifurcation [1.5 pts]

Classify the stability of each equilibrium in the two regimes $\kappa<\tfrac34$ and $\kappa>\tfrac34$. Describe what happens at $\kappa=\tfrac34$. Is "the bottom of the hoop is always stable" true?

### Hint

$V''(\theta)=\cos\theta\,G+\sin\theta\,G'$. At $\theta^*$, $G=0$. At $\kappa=\tfrac34$ the second derivative vanishes at the bottom: look at the fourth one.

### Checkpoint

- Top: $V''(0)=-mga<0$, always unstable.
- Bottom: $V''(\pi)=mga\big(1-\tfrac43\kappa\big)$: stable for $\kappa<\tfrac34$, **unstable** for $\kappa>\tfrac34$.
- Pair: $V''(\theta^*)=\dfrac{ka^2d^2l_0\sin^2\theta^*}{l^{*3}}>0$: stable whenever it exists. Supercritical pitchfork at $\kappa=\tfrac34$ ($V''''(\pi)=\tfrac13mga>0$ there).

### Solution

#### Step 1. Second derivative

From $V'=\sin\theta\,G(\theta)$ with $G=-mga+kad(1-l_0/l)$, the product rule gives $V''=\cos\theta\,G+\sin\theta\,G'$, and by the chain rule $G'=kad\,\dfrac{l_0}{l^2}\,l'=kad\,\dfrac{l_0}{l^2}\,\dfrac{ad\sin\theta}{l}$.

#### Step 2. Top and bottom

At $\theta=0$: $l=l_0$, so $G(0)=-mga$ and $V''(0)=-mga<0$: unstable for every $\kappa$ (the spring is slack there and cannot hold the bead up).

At $\theta=\pi$: $l=3a$, $G(\pi)=-mga+k\,a\,2a\,\tfrac23=-mga+\tfrac43ka^2$ and $V''(\pi)=\cos\pi\,G(\pi)=mga-\tfrac43ka^2=mga\big(1-\tfrac43\kappa\big)$.

#### Step 3. The pair

At $\theta^*$, $G=0$, so $V''(\theta^*)=\sin\theta^*G'(\theta^*)=\dfrac{ka^2d^2l_0\sin^2\theta^*}{l^{*3}}>0$: a minimum, stable.

#### Step 4. The two regimes (the trap)

- $\kappa<\tfrac34$ (soft spring): two equilibria; top unstable, **bottom stable**.
- $\kappa>\tfrac34$ (stiff spring): four equilibria; top unstable, **bottom unstable**, $\pm\theta^*$ stable. The stretched spring pulls the bead up harder than gravity pulls it down, and the bead settles on one side.

The bottom is not always stable. At $\kappa=\tfrac34$, $V''(\pi)=0$ and $V'''(\pi)=0$ (symmetry), and $V''''(\pi)=\tfrac13mga>0$: the bottom is still a (flat) minimum. As $\kappa$ crosses $\tfrac34$ the minimum at the bottom splits into two minima that move away symmetrically: a **supercritical pitchfork bifurcation** (see the energy curves of the figure).

## (e) Small oscillations [1.5 pts]

Compute the angular frequency of small oscillations (i) about the bottom for $\kappa=\tfrac12$ and (ii) about $\theta^*$ for $\kappa=1$ (give $\theta^*$). Numerical values for $a=0.40$ m.

### Hint

Linearise $ma^2\ddot\theta=-V'(\theta)$ about the equilibrium: $\omega^2=V''(\theta_e)/(ma^2)$ (Notes §4.6 and §4.7).

### Checkpoint

- (i) $\omega^2=\dfrac{g}{3a}$, $\ \omega=2.859$ rad/s.
- (ii) $l^*=2a$, $\cos\theta^*=\tfrac14$, $\theta^*=75.52^\circ$; $\ \omega^2=\dfrac{15}{32}\dfrac ga$, $\ \omega=3.391$ rad/s.

### Solution

#### Step 1. Linearisation

With $\theta=\theta_e+\eta$, $V'(\theta)=V'(\theta_e)+V''(\theta_e)\eta+O(\eta^2)$ and $V'(\theta_e)=0$, so $ma^2\ddot\eta+V''(\theta_e)\eta=0$ and $\omega^2=V''(\theta_e)/(ma^2)$ when $V''(\theta_e)>0$.

#### Step 2. Bottom, $\kappa=\tfrac12$

$V''(\pi)=mga(1-\tfrac43\cdot\tfrac12)=\tfrac13mga$, so $\omega^2=\dfrac{g}{3a}=\dfrac{9.81}{1.2}=8.175$ s$^{-2}$ and $\omega=2.859$ rad/s.

#### Step 3. Side equilibrium, $\kappa=1$

$l^*=2a/(2-1)=2a$, $\cos\theta^*=\tfrac14(5-4)=\tfrac14$, $\theta^*=\arccos\tfrac14=75.52^\circ$, $\sin^2\theta^*=\tfrac{15}{16}$. With $k=mg/a$, $d=2a$, $l_0=a$:

$$V''(\theta^*)=\frac{k\,a^2\,(4a^2)\,a\cdot\tfrac{15}{16}}{8a^3}=\frac{15}{32}ka^2=\frac{15}{32}mga,\qquad \omega^2=\frac{15}{32}\frac ga$$

Numerically $\omega^2=\tfrac{15}{32}\times\tfrac{9.81}{0.40}=11.50$ s$^{-2}$, $\omega=3.391$ rad/s.

## (f) Energy integral and the bead at the bottom [1.5 pts]

Write the energy first integral. For $\kappa=\tfrac12$ the bead leaves the top with a vanishingly small speed. Find its speed at the bottom and the reaction of the hoop there. Would a bead released exactly at rest at the top move?

### Hint

$\tfrac12ma^2\dot\theta^2+V(\theta)=$ const (the reaction does no work). Use $N$ from (b) with $\theta=\pi$.

### Checkpoint

- $\tfrac12ma^2\dot\theta^2+mga\cos\theta+\tfrac12k(l-l_0)^2=E$; $\ V(\pi)-V(0)=2mga(\kappa-1)$.
- $\kappa=\tfrac12$: $v_{bottom}^2=4ga(1-\kappa)=2ga$, $v=2.801$ m/s (against $4ga$ without spring).
- $N(\pi)=-2mg$: the hoop pushes the bead **towards** $C$, i.e. upwards with $2mg$. At rest exactly at the top the bead stays (equilibrium); it needs a disturbance.

### Solution

#### Step 1. First integral

The reaction is normal to $\mathbf v_P=a\dot\theta\,\mathbf e_\theta$, so its power $\mathbf N\cdot\mathbf v_P=0$ (Notes §6.4 to §6.5); the other forces derive from $V$. Hence (Notes §4.5)

$$\tfrac12ma^2\dot\theta^2+mga\cos\theta+\tfrac12k\big(l(\theta)-l_0\big)^2=E$$

Check: $\dfrac{dE}{dt}=\dot\theta\big(ma^2\ddot\theta+V'(\theta)\big)=0$ by (b).

#### Step 2. Top versus bottom

$V(0)=mga+0$ and $V(\pi)=-mga+\tfrac12k(3a-a)^2=-mga+2ka^2$, so $V(\pi)-V(0)=2ka^2-2mga=2mga(\kappa-1)$.

#### Step 3. Speed at the bottom

$\theta=0$ is an equilibrium: released **exactly** at rest there, the bead stays. With an infinitesimal push, $E=V(0)$. For $\kappa=\tfrac12<\tfrac34$ the only equilibria are $0$ and $\pi$, so $V$ decreases monotonically on $(0,\pi)$ and the bead reaches the bottom with

$$\tfrac12mv^2=V(0)-V(\pi)=2mga(1-\kappa)\ \Longrightarrow\ v^2=4ga(1-\kappa)=2ga,\qquad v=\sqrt{2\times9.81\times0.40}=2.801\ \text{m/s}$$

With no spring ($\kappa=0$) it would be $v^2=4ga$: the spring stores part of the energy.

#### Step 4. Reaction at the bottom

At $\theta=\pi$: $l=3a$, $1-l_0/l=\tfrac23$, $a-d\cos\pi=3a$, $a\dot\theta^2=v^2/a=2g$ and $k=mg/(2a)$:

$$N=mg\cos\pi+\frac{mg}{2a}\cdot\frac23\cdot3a-m\cdot2g=-mg+mg-2mg=-2mg$$

$N<0$ means the reaction points along $-\mathbf e_r$, towards $C$; at the bottom $-\mathbf e_r=\mathbf j$, so the hoop pushes the bead **up** with $2mg$. Check on the vertical: $N_{up}-mg+T_{spring}=mv^2/a$ with $T_{spring}=k(3a-a)=mg$ gives $N_{up}=2mg-mg+mg=2mg$.

## Interpretation

- **Dimensional check:** $\kappa=ka/(mg)$ is (N/m)(m)/N = 1; $V$ and $mga$ in J; $\omega^2=g/a$ in s$^{-2}$; $N$ in N; $v^2=ga$ in m$^2$ s$^{-2}$.
- **Limits:** $\kappa\to0$ recovers the bead on a hoop under gravity alone (top unstable, bottom stable, $\omega^2=g/a$ at the bottom: our $V''(\pi)$ gives $mga$). $\kappa\to\infty$: the spring dominates and the stable positions approach the top, where the spring is unstretched. For $\kappa=1$, $V(\pi)=V(0)$: a bead leaving the top with a vanishing speed approaches the (now unstable) bottom only asymptotically, never reaching it in finite time.
- **Common mistakes in the exam:** (1) assuming the bottom is always the stable position; (2) missing the side equilibria by cancelling $\sin\theta$ without keeping the second factor; (3) using $l-l_0$ with the wrong natural length (the spring is unstretched at the **top**, not at the bottom); (4) forgetting that the reaction of a bead on a hoop can point either way (bilateral constraint), and assuming $N\ge0$; (5) "releasing from rest at the top" without noticing that it is an equilibrium.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
