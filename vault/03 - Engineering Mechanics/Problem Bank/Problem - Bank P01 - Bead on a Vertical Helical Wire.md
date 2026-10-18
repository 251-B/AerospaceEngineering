---
materia: Engineering Mechanics
tema: "Units 1 to 3: intrinsic kinematics and motion on a smooth curve"
bank_id: P01
title: "Bead on a vertical helical wire: Frenet triad, constant angular acceleration and the reaction"
category: midterm_problem
archetype: kinematics
level: standard
unit: 1
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p01.py"
tags:
  - problem-bank
  - midterm-1
  - frenet-serret
  - cylindrical-coordinates
  - smooth-curve
  - reaction-forces
  - energy
---

# Bank P01 — Bead on a vertical helical wire

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §2.4 and §2.5 (intrinsic basis and intrinsic acceleration), §2.6.2 (cylindrical coordinates), §2.7 (degrees of freedom), §6.5 (motion along a smooth curve) and §4.5 (mechanical energy). Every number was checked with SymPy.

## Statement

A rigid wire has the shape of a circular helix of radius $R$ wound around the vertical axis $Oz$ of the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ ($z$ upward, uniform gravity $-g\,\mathbf k$). In cylindrical coordinates $(\rho,\varphi,z)$, with $\varphi$ measured from the $x$ axis and counter-clockwise seen from above, the wire is

$$\rho=R,\qquad z=b\,\varphi\qquad(b>0)$$

so it rises a height $2\pi b$ (the pitch) per turn. A bead $P$ of mass $m$ slides **without friction** along the wire. At $t=0$ it is released from rest at $\varphi=\varphi_0$.

![[attachments/EM-M1/p01-helix-bead.svg]]

Use the cylindrical basis $\{\mathbf e_\rho,\mathbf e_\varphi,\mathbf k\}$ with $\mathbf e_\rho=\cos\varphi\,\mathbf i+\sin\varphi\,\mathbf j$, $\mathbf e_\varphi=-\sin\varphi\,\mathbf i+\cos\varphi\,\mathbf j$, and the intrinsic (Frenet) triad $\{\mathbf t,\mathbf n,\mathbf b\}$ of the helix, with $\mathbf t$ oriented towards increasing $\varphi$. Write $h=\sqrt{R^2+b^2}$.

## Setup

- Data: $m$, $R$, $b$, $g$, $\varphi_0$. In the numerical part (f): $R=0.30$ m, $b=0.40$ m (so $h=0.50$ m), $g=9.81$ m s$^{-2}$.
- Hypotheses: point particle, rigid fixed wire, no friction (the reaction has no component along $\mathbf t$), $S_0$ inertial.
- The bead is threaded on the wire, so the constraint is **bilateral**: the reaction may point either way in the normal plane.
- Notation: the scalar $b$ is the pitch parameter of the helix ($z=b\varphi$); the bold $\mathbf b$ is the binormal unit vector. They are unrelated.

## (a) Degrees of freedom and kinematics [1.5 pts]

How many degrees of freedom has $P$? Classify the constraints. Write the position, velocity and acceleration of $P$ in the cylindrical basis as functions of $\varphi$, $\dot\varphi$, $\ddot\varphi$.

### Hint

A free particle has 3 degrees of freedom; each curve equation removes one. Differentiate $z=b\varphi$ with the chain rule.

### Checkpoint

- 1 degree of freedom, coordinate $\varphi$; two holonomic, scleronomic, bilateral constraints $\rho-R=0$, $z-b\varphi=0$.
- $\mathbf v=R\dot\varphi\,\mathbf e_\varphi+b\dot\varphi\,\mathbf k$, $\ |\mathbf v|=h\,|\dot\varphi|$.
- $\mathbf a=-R\dot\varphi^2\,\mathbf e_\rho+R\ddot\varphi\,\mathbf e_\varphi+b\ddot\varphi\,\mathbf k$.

### Solution

#### Step 1. Count

The configuration of a free particle needs 3 coordinates $(\rho,\varphi,z)$. The wire imposes $f_1=\rho-R=0$ and $f_2=z-b\varphi=0$: two independent holonomic equations (positions only), with no explicit time (scleronomic), and two-sided (bilateral). Hence $3-2=1$ degree of freedom (Notes §2.7), and $\varphi$ is a convenient coordinate: $\rho$ and $z$ follow from it.

#### Step 2. Change of basis

The cylindrical basis turns with $\varphi$; its relation to the inertial basis is

$$\begin{pmatrix}\mathbf e_\rho\ \mathbf e_\varphi\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\varphi&\sin\varphi&0\ -\sin\varphi&\cos\varphi&0\ 0&0&1\end{pmatrix}$$

Checks: rows 1 and 2 have length $\cos^2\varphi+\sin^2\varphi=1$ and $-\cos\varphi\sin\varphi+\sin\varphi\cos\varphi=0$, row 3 is $\mathbf k$, so $[R][R]^T=I$; $\det[R]=\cos^2\varphi+\sin^2\varphi=+1$ (right-handed, $\mathbf e_\rho\times\mathbf e_\varphi=\mathbf k$). Differentiating the rows with the chain rule, $\dfrac{d\mathbf e_\rho}{d\varphi}=\mathbf e_\varphi$ and $\dfrac{d\mathbf e_\varphi}{d\varphi}=-\mathbf e_\rho$.

#### Step 3. Position and velocity

$\mathbf r=\rho\,\mathbf e_\rho+z\,\mathbf k=R\,\mathbf e_\rho+b\varphi\,\mathbf k$. The cylindrical velocity (Notes §2.6.2) is $\mathbf v=\dot\rho\,\mathbf e_\rho+\rho\dot\varphi\,\mathbf e_\varphi+\dot z\,\mathbf k$. Here $\dot\rho=0$ and, by the chain rule, $\dot z=\dfrac{dz}{d\varphi}\dot\varphi=b\dot\varphi$:

$$\mathbf v=R\dot\varphi\,\mathbf e_\varphi+b\dot\varphi\,\mathbf k,\qquad |\mathbf v|=\sqrt{R^2\dot\varphi^2+b^2\dot\varphi^2}=h\,|\dot\varphi|$$

#### Step 4. Acceleration

The cylindrical acceleration is $\mathbf a=(\ddot\rho-\rho\dot\varphi^2)\mathbf e_\rho+(\rho\ddot\varphi+2\dot\rho\dot\varphi)\mathbf e_\varphi+\ddot z\,\mathbf k$. With $\rho=R$, $\dot\rho=\ddot\rho=0$ and $\ddot z=\dfrac{d}{dt}(b\dot\varphi)=b\ddot\varphi$:

$$\mathbf a=-R\dot\varphi^2\,\mathbf e_\rho+R\ddot\varphi\,\mathbf e_\varphi+b\ddot\varphi\,\mathbf k$$

Check by direct differentiation of $\mathbf v$ with $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_\rho$: $\dot{\mathbf v}=R\ddot\varphi\,\mathbf e_\varphi+R\dot\varphi(-\dot\varphi\,\mathbf e_\rho)+b\ddot\varphi\,\mathbf k$, the same result.

## (b) Intrinsic triad, curvature and torsion [2.0 pts]

Obtain the unit vectors $\mathbf t$, $\mathbf n$, $\mathbf b$ of the helix in the cylindrical basis, its curvature $\kappa$ and torsion $\tau$, and the intrinsic components of the acceleration of $P$.

### Hint

Use the arc length $s=h\,(\varphi-\varphi_0)$, so $\dfrac{d}{ds}=\dfrac1h\dfrac{d}{d\varphi}$. Frenet: $\dfrac{d\mathbf t}{ds}=\kappa\,\mathbf n$, $\dfrac{d\mathbf b}{ds}=-\tau\,\mathbf n$.

### Checkpoint

- $\mathbf t=\dfrac{R\,\mathbf e_\varphi+b\,\mathbf k}{h}$, $\ \mathbf n=-\mathbf e_\rho$ (horizontal, towards the axis), $\ \mathbf b=\dfrac{-b\,\mathbf e_\varphi+R\,\mathbf k}{h}$.
- $\kappa=\dfrac{R}{R^2+b^2}$, $\ \tau=\dfrac{b}{R^2+b^2}$.
- $\mathbf a=h\ddot\varphi\,\mathbf t+R\dot\varphi^2\,\mathbf n$, no binormal component.

### Solution

#### Step 1. Arc length and tangent

$ds=|\mathbf v|\,dt=h\,d\varphi$ (taking $s$ increasing with $\varphi$), so $s=h(\varphi-\varphi_0)$ and $\dot s=h\dot\varphi$. The unit tangent (Notes §2.4) is

$$\mathbf t=\frac{d\mathbf r}{ds}=\frac{d\mathbf r}{d\varphi}\frac{d\varphi}{ds}=\frac1h\big(R\,\mathbf e_\varphi+b\,\mathbf k\big)$$

using $\dfrac{d\mathbf e_\rho}{d\varphi}=\mathbf e_\varphi$.

#### Step 2. Curvature and normal

With $\dfrac{d\mathbf e_\varphi}{d\varphi}=-\mathbf e_\rho$ and $\mathbf k$ constant:

$$\frac{d\mathbf t}{ds}=\frac1h\frac{d\mathbf t}{d\varphi}=\frac1h\cdot\frac{R}{h}\big(-\mathbf e_\rho\big)=\frac{R}{h^2}\,(-\mathbf e_\rho)$$

The modulus is the curvature and the unit vector the principal normal: $\kappa=R/h^2=R/(R^2+b^2)$, $\mathbf n=-\mathbf e_\rho$. The normal is **horizontal** and points to the axis, although the helix is inclined.

#### Step 3. Binormal and torsion

$\mathbf b=\mathbf t\times\mathbf n=\dfrac1h(R\,\mathbf e_\varphi+b\,\mathbf k)\times(-\mathbf e_\rho)$. With $\mathbf e_\varphi\times\mathbf e_\rho=-\mathbf k$ and $\mathbf k\times\mathbf e_\rho=\mathbf e_\varphi$:

$$\mathbf b=\frac1h\big(R\,\mathbf k-b\,\mathbf e_\varphi\big)$$

Then $\dfrac{d\mathbf b}{ds}=\dfrac1h\cdot\dfrac{-b}{h}\dfrac{d\mathbf e_\varphi}{d\varphi}=\dfrac{b}{h^2}\,\mathbf e_\rho=-\dfrac{b}{h^2}\,\mathbf n$, so $\tau=b/h^2=b/(R^2+b^2)$. In matrix form the triad is $(\mathbf t,\mathbf n,\mathbf b)^T=[Q]\,(\mathbf e_\rho,\mathbf e_\varphi,\mathbf k)^T$ with rows $(0,\ R/h,\ b/h)$, $(-1,\ 0,\ 0)$, $(0,\ -b/h,\ R/h)$: the rows are unit and mutually orthogonal ($R^2/h^2+b^2/h^2=1$, $-bR/h^2+bR/h^2=0$), so $[Q][Q]^T=I$, and expanding along the second row $\det[Q]=-(-1)\big(\tfrac Rh\tfrac Rh+\tfrac bh\tfrac bh\big)=+1$: $\{\mathbf t,\mathbf n,\mathbf b\}$ is right-handed. The third Frenet formula $\dfrac{d\mathbf n}{ds}=-\kappa\,\mathbf t+\tau\,\mathbf b$ checks: $\dfrac1h\dfrac{d(-\mathbf e_\rho)}{d\varphi}=-\dfrac{\mathbf e_\varphi}{h}$ and $-\dfrac{R}{h^3}(R\mathbf e_\varphi+b\mathbf k)+\dfrac{b}{h^3}(R\mathbf k-b\mathbf e_\varphi)=-\dfrac{R^2+b^2}{h^3}\mathbf e_\varphi=-\dfrac{\mathbf e_\varphi}{h}$.

#### Step 4. Intrinsic acceleration

The intrinsic acceleration (Notes §2.5) is $\mathbf a=\ddot s\,\mathbf t+\kappa\dot s^2\,\mathbf n$. With $\dot s=h\dot\varphi$, $\ddot s=h\ddot\varphi$ and $\kappa\dot s^2=\dfrac{R}{h^2}h^2\dot\varphi^2$:

$$\mathbf a=h\ddot\varphi\,\mathbf t+R\dot\varphi^2\,\mathbf n$$

Cross-check with (a): $\mathbf a\cdot\mathbf t=\dfrac1h(R\cdot R\ddot\varphi+b\cdot b\ddot\varphi)=h\ddot\varphi$, $\ \mathbf a\cdot\mathbf n=R\dot\varphi^2$, $\ \mathbf a\cdot\mathbf b=\dfrac1h(-bR\ddot\varphi+Rb\ddot\varphi)=0$.

## (c) Forces on the bead [1.0 pts]

Write the weight and the reaction of the wire in the intrinsic basis. How many unknowns does the problem have?

### Hint

Project $\mathbf k$ on $\mathbf t$, $\mathbf n$, $\mathbf b$. A smooth curve can only push in its normal plane.

### Checkpoint

- $\mathbf k=\dfrac{b}{h}\mathbf t+\dfrac{R}{h}\mathbf b$, so $\mathbf W=-mg\dfrac bh\,\mathbf t-mg\dfrac Rh\,\mathbf b$.
- $\mathbf N=N_n\,\mathbf n+N_b\,\mathbf b$; unknowns $\varphi(t)$, $N_n$, $N_b$.

### Solution

#### Step 1. Weight

$\mathbf k\cdot\mathbf t=b/h$, $\ \mathbf k\cdot\mathbf n=-\mathbf k\cdot\mathbf e_\rho=0$, $\ \mathbf k\cdot\mathbf b=R/h$. Hence

$$\mathbf W=-mg\,\mathbf k=-\frac{mgb}{h}\,\mathbf t-\frac{mgR}{h}\,\mathbf b$$

The weight has no component along $\mathbf n$, because $\mathbf n$ is horizontal.

#### Step 2. Reaction

The wire is smooth: its reaction is orthogonal to the tangent, i.e. it lies in the normal plane spanned by $\mathbf n$ and $\mathbf b$ (Notes §6.5):

$$\mathbf N=N_n\,\mathbf n+N_b\,\mathbf b$$

The three scalar equations of Newton's law will determine the three unknowns $\varphi(t)$, $N_n$, $N_b$.

## (d) Equation of motion and reaction [2.0 pts]

Obtain the equation of motion free of reactions and integrate it. Obtain $N_n$ and $N_b$ as functions of $\dot\varphi$. Does the bead move like a pendulum?

### Hint

Project $m\mathbf a=\mathbf W+\mathbf N$ on $\mathbf t$, $\mathbf n$, $\mathbf b$. Look at the right-hand side of the tangential equation before integrating.

### Checkpoint

- $\ddot\varphi=-\dfrac{gb}{R^2+b^2}$: **constant**. $\ \varphi(t)=\varphi_0-\dfrac{gb}{2h^2}t^2$.
- $N_n=mR\dot\varphi^2$, $\ N_b=\dfrac{mgR}{h}$ (constant).

### Solution

#### Step 1. Projections

With $\mathbf a$ of (b) and the forces of (c):

$$\mathbf t:\ mh\ddot\varphi=-\frac{mgb}{h},\qquad \mathbf n:\ mR\dot\varphi^2=N_n,\qquad \mathbf b:\ 0=-\frac{mgR}{h}+N_b$$

#### Step 2. Equation of motion

The tangential equation contains no reaction:

$$\ddot\varphi=-\frac{gb}{h^2}=-\frac{gb}{R^2+b^2}$$

The right-hand side does not depend on $\varphi$: there is **no restoring term** and no equilibrium. The tangential acceleration is $\ddot s=h\ddot\varphi=-g\,\dfrac bh=-g\sin\alpha$, with $\alpha$ the constant inclination of the helix ($\sin\alpha=b/h$): the bead moves exactly as on an inclined plane wound around a cylinder. It is not a pendulum.

#### Step 3. Integration

Integrating once between $0$ and $t$ (Barrow's rule, $\dot\varphi(0)=0$): $\dot\varphi(t)-\dot\varphi(0)=\displaystyle\int_0^t\ddot\varphi\,dt'=-\frac{gb}{h^2}\,[t']_0^t$, so $\dot\varphi=-\dfrac{gb}{h^2}t$. Integrating again with $\varphi(0)=\varphi_0$:

$$\varphi(t)=\varphi_0+\int_0^t\Big(-\frac{gb}{h^2}t'\Big)dt'=\varphi_0-\frac{gb}{h^2}\Big[\frac{t'^2}{2}\Big]_0^t=\varphi_0-\frac{gb}{2h^2}\,t^2$$

The bead descends ($\varphi$ and $z=b\varphi$ decrease).

#### Step 4. Reactions

$$N_n=mR\dot\varphi^2,\qquad N_b=\frac{mgR}{h}$$

$N_b$ supports the part of the weight normal to the wire and is constant; $N_n$ (pointing to the axis) supplies the centripetal force of the horizontal circular motion and grows with the speed.

## (e) First integral [1.5 pts]

Show that the mechanical energy is conserved and use it to write $\dot\varphi^2$ and $N_n$ as functions of $\varphi$.

### Hint

Compute the power of $\mathbf N$. Or multiply the equation of motion by $\dot\varphi$.

### Checkpoint

- $E=\tfrac12mh^2\dot\varphi^2+mgb\varphi=mgb\varphi_0$.
- $\dot\varphi^2=\dfrac{2gb(\varphi_0-\varphi)}{h^2}$, $\ N_n=\dfrac{2mgRb(\varphi_0-\varphi)}{h^2}=2mg\,\kappa\,\Delta z$ with $\Delta z=b(\varphi_0-\varphi)$.

### Solution

#### Step 1. Power of the forces

$\mathbf v=h\dot\varphi\,\mathbf t$ and $\mathbf N\cdot\mathbf t=0$, so $\mathbf N\cdot\mathbf v=0$: the reaction of a fixed smooth curve does no work (Notes §6.4). The weight is conservative with $V=mgz=mgb\varphi$. Hence (Notes §4.5)

$$E=\tfrac12m|\mathbf v|^2+mgz=\tfrac12mh^2\dot\varphi^2+mgb\varphi=\text{const}$$

#### Step 2. Same result from the equation of motion

Multiply $h^2\ddot\varphi=-gb$ by $\dot\varphi$: $h^2\dot\varphi\ddot\varphi=\dfrac{d}{dt}\Big(\tfrac12h^2\dot\varphi^2\Big)$ (chain rule) and $-gb\dot\varphi=\dfrac{d}{dt}(-gb\varphi)$. Integrating from $0$ to $t$ with Barrow's rule: $\tfrac12h^2\dot\varphi^2-0=-gb(\varphi-\varphi_0)$.

#### Step 3. Speed and reaction along the wire

$$\dot\varphi^2=\frac{2gb(\varphi_0-\varphi)}{h^2},\qquad N_n=mR\dot\varphi^2=\frac{2mgRb(\varphi_0-\varphi)}{h^2}$$

With $\kappa=R/h^2$ and the height fallen $\Delta z=b(\varphi_0-\varphi)$: $N_n=2mg\kappa\,\Delta z$, i.e. $N_n=m\kappa v^2$ with $v^2=2g\Delta z$.

## (f) One full turn: time, speed and reaction [2.0 pts]

Find the time $t_1$ the bead needs to complete one turn and its speed then. For $R=0.30$ m, $b=0.40$ m, $g=9.81$ m s$^{-2}$ give $\kappa$, $\tau$, $\ddot\varphi$, $t_1$, the speed and the reaction (in units of $mg$) at $t_1$. Is the acceleration vector of the bead constant?

### Hint

One turn is $\varphi_0-\varphi=2\pi$; use the law $\varphi(t)$ of (d) and the energy of (e).

### Checkpoint

- $t_1=2h\sqrt{\dfrac{\pi}{gb}}$, $\ v_1=\sqrt{4\pi gb}=\sqrt{2g\,(2\pi b)}$ (independent of $R$).
- $\kappa=1.2$ m$^{-1}$, $\tau=1.6$ m$^{-1}$, $\ddot\varphi=-15.70$ rad s$^{-2}$, $\ddot s=-7.848$ m s$^{-2}$, $t_1=0.8948$ s, $v_1=7.022$ m/s, $|\dot\varphi_1|=14.04$ rad/s.
- $N_n=1.92\pi\,mg\approx6.032\,mg$, $N_b=0.6\,mg$, $|\mathbf N|\approx6.062\,mg$. The acceleration is not constant: its normal part $R\dot\varphi^2$ grows.

### Solution

#### Step 1. Time for one turn

From $\varphi(t_1)=\varphi_0-2\pi$: $\dfrac{gb}{2h^2}t_1^2=2\pi\Rightarrow t_1=\sqrt{\dfrac{4\pi h^2}{gb}}=2h\sqrt{\dfrac{\pi}{gb}}$.

#### Step 2. Speed after one turn

From (e) with $\varphi_0-\varphi=2\pi$: $\dot\varphi_1^2=\dfrac{4\pi gb}{h^2}$ and $v_1=h|\dot\varphi_1|=\sqrt{4\pi gb}$. Equivalently $v_1=h|\dot\varphi(t_1)|=h\dfrac{gb}{h^2}t_1=\dfrac{gb}{h}\cdot2h\sqrt{\dfrac{\pi}{gb}}=\sqrt{4\pi gb}$. Since the fall per turn is $2\pi b$, $v_1=\sqrt{2g\cdot2\pi b}$: the speed depends only on the height fallen, not on $R$.

#### Step 3. Numbers

$h=\sqrt{0.09+0.16}=0.5$ m; $\kappa=0.3/0.25=1.2$ m$^{-1}$; $\tau=0.4/0.25=1.6$ m$^{-1}$; $\ddot\varphi=-9.81\cdot0.4/0.25=-15.696$ rad s$^{-2}$, $\ddot s=h\ddot\varphi=-7.848$ m s$^{-2}$ ($\sin\alpha=0.8$, $\alpha=53.13^\circ$).

$$t_1=2(0.5)\sqrt{\frac{\pi}{9.81\cdot0.4}}=0.8948\ \text{s},\qquad v_1=\sqrt{4\pi\cdot9.81\cdot0.4}=7.022\ \text{m/s},\qquad |\dot\varphi_1|=\frac{v_1}{h}=14.04\ \text{rad/s}$$

#### Step 4. Reaction after one turn

$$\frac{N_n}{mg}=\frac{R\dot\varphi_1^2}{g}=\frac{4\pi Rb}{h^2}=4\pi\cdot\frac{0.12}{0.25}=1.92\pi\approx6.032,\qquad \frac{N_b}{mg}=\frac Rh=0.6$$

$|\mathbf N|=mg\sqrt{6.032^2+0.6^2}\approx6.062\,mg$. The tangential acceleration is constant, but $\mathbf a=h\ddot\varphi\,\mathbf t+R\dot\varphi^2\,\mathbf n$ has a growing normal part and a direction that turns with the triad: the acceleration vector is not constant.

## Interpretation

- **Dimensional check:** $\kappa$ and $\tau$ are m/m$^2$ = m$^{-1}$; $gb/h^2$ is (m s$^{-2}$)(m)/m$^2$ = s$^{-2}$, an angular acceleration; $t_1=2h\sqrt{\pi/(gb)}$ has m/$\sqrt{\text{m}^2\,\text{s}^{-2}}$ = s; $N=mR\dot\varphi^2$ is kg m s$^{-2}$ = N.
- **Limits:** $b\to0$ (horizontal ring): $\ddot\varphi\to0$, the bead stays at rest and $N_b\to mg$ carries the whole weight. $R\to0$ (vertical straight wire): $\ddot z=b\ddot\varphi=-g\,b^2/h^2\to-g$ (free fall), $\kappa\to0$ and the reaction vanishes. $\kappa$ is largest for $b\to0$ and $\tau$ is largest for $b=R$.
- **Common mistakes in the exam:** (1) expecting a pendulum-type equation: on a helix the gravity component along the wire is the same everywhere, so $\ddot\varphi$ is constant; (2) taking $\mathbf n$ along the "radius of the coil" tilted with the helix: it is exactly $-\mathbf e_\rho$, horizontal; (3) forgetting $N_b$, which exists even at rest; (4) concluding that the acceleration is constant because $\ddot\varphi$ is: the normal acceleration $R\dot\varphi^2$ grows linearly with the height fallen.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
