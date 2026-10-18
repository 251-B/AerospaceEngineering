---
materia: Engineering Mechanics
tema: "Units 3 and 4: motion on a smooth surface, axial angular momentum and orbits"
bank_id: P02
title: "Particle on a smooth paraboloid of revolution: axial angular momentum, circular orbits and radial oscillations"
category: midterm_problem
archetype: central-force
level: trap
unit: 4
difficulty: 3
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p02.py"
tags:
  - problem-bank
  - midterm-1
  - smooth-surface
  - angular-momentum
  - circular-orbit
  - small-oscillations
  - reaction-forces
---

# Bank P02 — Particle on a smooth paraboloid of revolution

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §2.6.2 (cylindrical coordinates), §6.3 and §6.4 (normal vector and motion on a smooth surface), §4.8 (angular momentum and torque), §4.5 (mechanical energy) and §4.6 (equilibrium and linearisation). Every number was checked with SymPy.

## Statement

A particle $P$ of mass $m$ moves on the **inner** face of a smooth, fixed paraboloid of revolution whose axis $Oz$ is vertical (upward; uniform gravity $-g\,\mathbf k$). In cylindrical coordinates $(r,\varphi,z)$ of the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ the surface is

$$z=\frac{r^2}{2c}\qquad(c>0)$$

with $O$ at its vertex. The particle rests on the surface from above (the contact can only push $P$ away from the surface, towards the inside of the bowl). The azimuth $\varphi$ is measured from the $x$ axis, counter-clockwise seen from above.

![[attachments/EM-M1/p02-paraboloid.svg]]

Use the cylindrical basis $\{\mathbf e_r,\mathbf e_\varphi,\mathbf k\}$, and write $q=\sqrt{1+r^2/c^2}$ and $\Omega_0=\sqrt{g/c}$.

## Setup

- Data: $m$, $c$, $g$. In part (f): initial radius $r_0=c/2$, $\dot r(0)=0$, initial velocity horizontal and tangent to the parallel with speed $v_0=2r_0\Omega_0=c\,\Omega_0$; for numbers, $c=1$ m and $g=9.81$ m s$^{-2}$.
- Hypotheses: point particle, no friction, $S_0$ inertial. The contact is **unilateral**: the model is valid while the normal reaction is non-negative (checked in (f)).

## (a) Degrees of freedom and kinematics [1.5 pts]

How many degrees of freedom has $P$ while it stays on the surface? Write its velocity and acceleration in the cylindrical basis using the constraint.

### Hint

Differentiate $z=r^2/(2c)$ twice with the chain and product rules.

### Checkpoint

- 2 degrees of freedom, coordinates $(r,\varphi)$; one holonomic, scleronomic, unilateral constraint.
- $\dot z=r\dot r/c$, $\ \ddot z=(\dot r^2+r\ddot r)/c$.
- $\mathbf a=(\ddot r-r\dot\varphi^2)\mathbf e_r+(2\dot r\dot\varphi+r\ddot\varphi)\mathbf e_\varphi+\dfrac{\dot r^2+r\ddot r}{c}\mathbf k$.

### Solution

#### Step 1. Count

A free particle needs $(r,\varphi,z)$. The surface $f=z-r^2/(2c)=0$ is one holonomic equation without explicit time: $3-1=2$ degrees of freedom (Notes §2.7), with generalized coordinates $r$ and $\varphi$. The constraint is unilateral, because the particle is only pressed against the surface.

#### Step 2. Derivatives of $z$

By the chain rule, $\dot z=\dfrac{dz}{dr}\dot r=\dfrac{r\dot r}{c}$. By the product rule, $\ddot z=\dfrac1c\dfrac{d}{dt}(r\dot r)=\dfrac{\dot r\,\dot r+r\ddot r}{c}=\dfrac{\dot r^2+r\ddot r}{c}$.

#### Step 3. Change of basis

The cylindrical basis turns with $\varphi$; its relation to the inertial basis is

$$\begin{pmatrix}\mathbf e_r\ \mathbf e_\varphi\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\varphi&\sin\varphi&0\ -\sin\varphi&\cos\varphi&0\ 0&0&1\end{pmatrix}$$

Checks: rows 1 and 2 have length $\cos^2\varphi+\sin^2\varphi=1$ and $-\cos\varphi\sin\varphi+\sin\varphi\cos\varphi=0$, row 3 is $\mathbf k$, so $[R][R]^T=I$; $\det[R]=\cos^2\varphi+\sin^2\varphi=+1$ (right-handed, $\mathbf e_r\times\mathbf e_\varphi=\mathbf k$). By the chain rule, $\dot{\mathbf e}_r=\dot\varphi\,\mathbf e_\varphi$ and $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_r$.

#### Step 4. Velocity and acceleration

In cylindrical coordinates (Notes §2.6.2), $\mathbf v=\dot r\,\mathbf e_r+r\dot\varphi\,\mathbf e_\varphi+\dot z\,\mathbf k$ and $\mathbf a=(\ddot r-r\dot\varphi^2)\mathbf e_r+(r\ddot\varphi+2\dot r\dot\varphi)\mathbf e_\varphi+\ddot z\,\mathbf k$. With Step 2:

$$\mathbf v=\dot r\,\mathbf e_r+r\dot\varphi\,\mathbf e_\varphi+\frac{r\dot r}{c}\,\mathbf k,\qquad |\mathbf v|^2=q^2\dot r^2+r^2\dot\varphi^2$$

$$\mathbf a=(\ddot r-r\dot\varphi^2)\,\mathbf e_r+(2\dot r\dot\varphi+r\ddot\varphi)\,\mathbf e_\varphi+\frac{\dot r^2+r\ddot r}{c}\,\mathbf k$$

## (b) Forces [1.0 pts]

Obtain the unit normal of the surface and write the forces on $P$.

### Hint

The normal of $f(r,z)=0$ is along $\nabla f$; in cylindrical coordinates $\nabla f=\dfrac{\partial f}{\partial r}\mathbf e_r+\dfrac{\partial f}{\partial z}\mathbf k$ here.

### Checkpoint

- $\mathbf n=\dfrac{-(r/c)\,\mathbf e_r+\mathbf k}{q}$ (towards the inside of the bowl).
- $\mathbf W=-mg\,\mathbf k$, $\ \mathbf N=N\mathbf n$ with $N\ge0$ for contact.

### Solution

#### Step 1. Normal vector

$\nabla f=\dfrac{\partial f}{\partial r}\mathbf e_r+\dfrac1r\dfrac{\partial f}{\partial\varphi}\mathbf e_\varphi+\dfrac{\partial f}{\partial z}\mathbf k=-\dfrac rc\,\mathbf e_r+\mathbf k$, of modulus $\sqrt{1+r^2/c^2}=q$ (Notes §6.3). Its $\mathbf k$ component is positive, so it points into the bowl, the side on which the particle lies:

$$\mathbf n=\frac{1}{q}\Big(-\frac rc\,\mathbf e_r+\mathbf k\Big)$$

Check: $\mathbf n\cdot\mathbf v=\dfrac1q\Big(-\dfrac{r\dot r}{c}+\dfrac{r\dot r}{c}\Big)=0$.

#### Step 2. Forces

The weight $\mathbf W=-mg\,\mathbf k$ and the smooth normal reaction $\mathbf N=N\,\mathbf n$ (Notes §6.4). Contact requires $N\ge0$. Note that $\mathbf N$ lies in the meridian plane (it has no $\mathbf e_\varphi$ component) but does **not** pass through $O$ in general.

## (c) Equations of motion and first integrals [2.0 pts]

Project Newton's law, show that the component $H=r^2\dot\varphi$ of the specific angular momentum along the axis is conserved, write the energy and obtain one equation for $r(t)$ free of $N$. Give $N$ as a function of the state.

### Hint

The $\mathbf e_\varphi$ equation is $\frac{m}{r}\frac{d}{dt}(r^2\dot\varphi)=0$. Eliminate $N$ between the $\mathbf e_r$ and $\mathbf k$ equations. Is the angular momentum about $O$ conserved?

### Checkpoint

- $H=r^2\dot\varphi=$ const (the moment about the axis of $\mathbf W$ and $\mathbf N$ is zero; $\mathbf H_O$ itself is not conserved).
- $\Big(1+\dfrac{r^2}{c^2}\Big)\ddot r+\dfrac{r\dot r^2}{c^2}-\dfrac{H^2}{r^3}+\dfrac{gr}{c}=0$.
- $\dfrac Em=\tfrac12\Big[\Big(1+\dfrac{r^2}{c^2}\Big)\dot r^2+\dfrac{H^2}{r^2}\Big]+\dfrac{gr^2}{2c}$; $\ N=mq\Big(\dfrac{\dot r^2+r\ddot r}{c}+g\Big)$.

### Solution

#### Step 1. Projections

With $\mathbf a$ of (a), $\mathbf N\cdot\mathbf e_r=-Nr/(cq)$, $\mathbf N\cdot\mathbf k=N/q$:

$$\mathbf e_r:\ m(\ddot r-r\dot\varphi^2)=-\frac{N r}{c\,q}\qquad\mathbf e_\varphi:\ m(2\dot r\dot\varphi+r\ddot\varphi)=0\qquad\mathbf k:\ m\frac{\dot r^2+r\ddot r}{c}=\frac Nq-mg$$

#### Step 2. Axial angular momentum

By the product rule, $\dfrac{d}{dt}(r^2\dot\varphi)=2r\dot r\dot\varphi+r^2\ddot\varphi=r(2\dot r\dot\varphi+r\ddot\varphi)$, so the $\mathbf e_\varphi$ equation is $\dfrac mr\dfrac{d}{dt}(r^2\dot\varphi)=0$: $H=r^2\dot\varphi$ is constant. Physical reason (Notes §4.8): $\mathbf k\cdot(\mathbf r\times\mathbf F)$ is the moment about the $z$ axis; $\mathbf W$ is parallel to the axis and $\mathbf N$ lies in the meridian plane, which contains the axis, so both have zero moment about it. The full vector $\mathbf H_O$ is **not** conserved ($\mathbf r\times\mathbf N\neq\mathbf 0$ in general): only its axial component is.

#### Step 3. Equation for $r$

From $\mathbf k$: $\dfrac Nq=m\Big(\dfrac{\dot r^2+r\ddot r}{c}+g\Big)$. Substituting in $\mathbf e_r$ (which contains $\dfrac{r}{c}\cdot\dfrac Nq$) and using $\dot\varphi=H/r^2$:

$$\ddot r-\frac{H^2}{r^3}=-\frac rc\Big(\frac{\dot r^2+r\ddot r}{c}+g\Big)\ \Longrightarrow\ \Big(1+\frac{r^2}{c^2}\Big)\ddot r+\frac{r\dot r^2}{c^2}-\frac{H^2}{r^3}+\frac{gr}{c}=0$$

#### Step 4. Energy

$\mathbf N\cdot\mathbf v=0$ (fixed smooth surface) and $\mathbf W$ derives from $V=mgz=mgr^2/(2c)$, so $E=\tfrac12m|\mathbf v|^2+V$ is constant (Notes §4.5). With $|\mathbf v|^2$ of (a) and $r\dot\varphi=H/r$:

$$\frac Em=\frac12\Big[\Big(1+\frac{r^2}{c^2}\Big)\dot r^2+\frac{H^2}{r^2}\Big]+\frac{gr^2}{2c}$$

Check: $\dfrac{d}{dt}\dfrac Em=\dot r\Big[\Big(1+\dfrac{r^2}{c^2}\Big)\ddot r+\dfrac{r\dot r^2}{c^2}-\dfrac{H^2}{r^3}+\dfrac{gr}{c}\Big]=0$ by Step 3 (the term $\dfrac{r\dot r^3}{c^2}$ comes from the chain rule on $\dfrac{r^2}{c^2}\dot r^2$).

#### Step 5. Reaction

$N=mq\Big(\dfrac{\dot r^2+r\ddot r}{c}+g\Big)$, with $\ddot r$ from Step 3.

## (d) Horizontal circular orbits [1.5 pts]

Find the angular rate of a horizontal circular motion at radius $r_0$, its speed and the normal reaction. Discuss the dependence on $r_0$.

### Hint

Set $\dot r=\ddot r=0$ in the equation for $r$.

### Checkpoint

- $\dot\varphi^2=g/c$: $\Omega_0=\sqrt{g/c}$, **the same for every $r_0$**; period $2\pi\sqrt{c/g}$; speed $r_0\Omega_0$.
- $N=mg\sqrt{1+r_0^2/c^2}$.

### Solution

#### Step 1. Rate

With $\dot r=\ddot r=0$ and $H=r_0^2\dot\varphi$: $\dfrac{H^2}{r_0^3}=r_0\dot\varphi^2=\dfrac{gr_0}{c}$, hence

$$\dot\varphi^2=\frac gc\quad\Longrightarrow\quad\Omega_0=\sqrt{\frac gc},\qquad T=2\pi\sqrt{\frac cg},\qquad v=r_0\Omega_0$$

All horizontal circles are described in the same time, whatever their radius (isochronous orbits). This is the trap of the item: on a cone or on a sphere the rate depends on the radius; on the paraboloid the slope $dz/dr=r/c$ grows exactly in proportion to the centripetal acceleration $r\Omega^2$ needed.

#### Step 2. Reaction

$N=mq_0(0+g)=mg\sqrt{1+r_0^2/c^2}$. Its vertical component $N/q_0=mg$ carries the weight; its horizontal component $Nr_0/(cq_0)=mgr_0/c=mr_0\Omega_0^2$ is the centripetal force.

## (e) Small radial oscillations about a circular orbit [2.0 pts]

Perturb the circular orbit of radius $r_0$ keeping $H=r_0^2\Omega_0$. Obtain the frequency $\omega_r$ of the small radial oscillations and the ratio $\omega_r/\Omega_0$. For which $r_0$ is the perturbed orbit closed after one revolution? What happens for $r_0\to0$ and $r_0=c$?

### Hint

Write the equation of (c) as $\ddot r=G(r,\dot r)$ and linearise about $(r_0,0)$: the $\dot r^2$ term is of second order.

### Checkpoint

- $\omega_r^2=\dfrac{4g}{c\,(1+r_0^2/c^2)}=\dfrac{4gc}{c^2+r_0^2}$, $\quad\dfrac{\omega_r}{\Omega_0}=\dfrac{2c}{\sqrt{c^2+r_0^2}}$.
- Ratio 1 for $r_0=\sqrt3\,c$ (closed after one revolution); $2$ for $r_0\to0$; $\sqrt2$ for $r_0=c$ (not closed).

### Solution

#### Step 1. Linearisation

$G(r,\dot r)=\dfrac{F(r)-r\dot r^2/c^2}{1+r^2/c^2}$ with $F(r)=\dfrac{H^2}{r^3}-\dfrac{gr}{c}$, and $F(r_0)=0$ by (d). Put $r=r_0+\varepsilon$ with $\varepsilon$, $\dot\varepsilon$ small. $\partial G/\partial\dot r=-2r\dot r/(c^2q^2)$ vanishes at $\dot r=0$. Since $F(r_0)=0$, $\dfrac{\partial G}{\partial r}\Big|_{r_0}=\dfrac{F'(r_0)}{1+r_0^2/c^2}$ (the derivative of the denominator multiplies $F(r_0)=0$). With $F'(r)=-\dfrac{3H^2}{r^4}-\dfrac gc$ and $H^2=r_0^4\,g/c$:

$$F'(r_0)=-\frac{3g}{c}-\frac gc=-\frac{4g}{c}\qquad\Longrightarrow\qquad\ddot\varepsilon+\frac{4g}{c\,(1+r_0^2/c^2)}\,\varepsilon=0$$

#### Step 2. Frequency and ratio

$$\omega_r^2=\frac{4gc}{c^2+r_0^2},\qquad\frac{\omega_r}{\Omega_0}=\sqrt{\frac{4c^2}{c^2+r_0^2}}=\frac{2c}{\sqrt{c^2+r_0^2}}$$

The orbit is stable (positive $\omega_r^2$) for every $r_0$. The trap: the radial frequency is **not** $\Omega_0$, and the factor $1+r_0^2/c^2$ (the inertia of the vertical motion that comes with $\dot r$) cannot be dropped.

#### Step 3. Special radii

- $r_0\to0$: ratio $2$: two radial oscillations per revolution, a centred ellipse, as for an isotropic harmonic bowl ($z\approx r^2/(2c)$ is then the potential of a linear spring of stiffness $mg/c$).
- $r_0=c$: ratio $\sqrt2$, irrational: the perturbed orbit precesses and never closes.
- $r_0=\sqrt3\,c$: ratio $2c/\sqrt{4c^2}=1$: one radial oscillation per revolution, a closed orbit.

## (f) Turning points and contact [2.0 pts]

The particle starts at $r_0$ with $\dot r=0$ and a horizontal velocity $v_0$ tangent to the parallel. Find the turning radii. Then take $r_0=c/2$, $v_0=2r_0\Omega_0$: give the turning radii, $\ddot r$ and $N$ at both, and decide whether the particle ever leaves the surface.

### Hint

$H=r_0v_0$ and $E/m=\tfrac12v_0^2+gr_0^2/(2c)$. At a turning point $\dot r=0$; use $u=r^2$. For the contact, replace $\ddot r$ and $\dot r^2$ in $N$ by their expressions in $r$.

### Checkpoint

- $(u-r_0^2)\Big(\dfrac{gu}{c}-v_0^2\Big)=0$: turning radii $r_0$ and $r^*=v_0\sqrt{c/g}=v_0/\Omega_0$.
- Case: $r^*=c$; $\ddot r(c/2)=\tfrac65g$ (outwards), $\ddot r(c)=-\tfrac38g$; $N(c/2)=\tfrac{4}{\sqrt5}mg\approx1.789\,mg$, $N(c)=\tfrac{5\sqrt2}{8}mg\approx0.884\,mg$.
- On every motion $N=\dfrac{m\,(2Ec^2/m+H^2+gc^3)}{(c^2+r^2)^{3/2}}>0$: contact is never lost. Here $N=\dfrac{5mgc^3}{2(c^2+r^2)^{3/2}}$.

### Solution

#### Step 1. Constants

$\mathbf v(0)=v_0\mathbf e_\varphi$, so $H=r_0\cdot r_0\dot\varphi(0)=r_0v_0$ and $E/m=\tfrac12v_0^2+\dfrac{gr_0^2}{2c}$.

#### Step 2. Turning radii

At $\dot r=0$ the energy of (c) gives $\dfrac{H^2}{r^2}+\dfrac{gr^2}{c}=v_0^2+\dfrac{gr_0^2}{c}$. Multiply by $u=r^2$:

$$\frac gc u^2-\Big(v_0^2+\frac{gr_0^2}{c}\Big)u+r_0^2v_0^2=0\ \Longleftrightarrow\ (u-r_0^2)\Big(\frac{gu}{c}-v_0^2\Big)=0$$

(expanding the product gives back the three terms). Roots: $r=r_0$ and $r^*=v_0\sqrt{c/g}=v_0/\Omega_0$. If $v_0>r_0\Omega_0$ the particle climbs to $r^*>r_0$; if $v_0=r_0\Omega_0$ both coincide (circular orbit of (d)). The time between them is a quadrature: from the energy, $dt=\dfrac{q\,dr}{\sqrt{2E/m-H^2/r^2-gr^2/c}}$.

#### Step 3. The numerical case

$r_0=c/2$, $v_0=c\Omega_0$: $r^*=c\Omega_0/\Omega_0=c$. So $r$ oscillates between $c/2$ and $c$ ($z$ between $c/8$ and $c/2$). With $H^2=r_0^2v_0^2=c^3g/4$, $E/m=\tfrac58gc$. For $c=1$ m: $\Omega_0=v_0=3.132$ (rad/s and m/s), $\omega_r(r_0)=\tfrac{4}{\sqrt5}\Omega_0=5.603$ rad/s for the small oscillations of (e), which do not apply here because the amplitude is large.

At the turning points $\dot r=0$, so $q^2\ddot r=\dfrac{H^2}{r^3}-\dfrac{gr}{c}$:

- $r=c/2$: $\dfrac{H^2}{r^3}=\dfrac{c^3g/4}{c^3/8}=2g$, $\dfrac{gr}{c}=\dfrac g2$, $q^2=\dfrac54$: $\ddot r=\dfrac{3g/2}{5/4}=\dfrac65g$.
- $r=c$: $\dfrac{H^2}{r^3}=\dfrac g4$, $\dfrac{gr}{c}=g$, $q^2=2$: $\ddot r=-\dfrac{3g}{8}$.

Then $N=mq\Big(\dfrac{r\ddot r}{c}+g\Big)$: at $r=c/2$, $N=m\dfrac{\sqrt5}{2}\Big(\dfrac35g+g\Big)=\dfrac{4}{\sqrt5}mg\approx1.789\,mg$; at $r=c$, $N=m\sqrt2\Big(-\dfrac38g+g\Big)=\dfrac{5\sqrt2}{8}mg\approx0.884\,mg$.

#### Step 4. Contact along any motion

From Step 3 of (c), multiplied by $r$: $r\ddot r\,q^2=\dfrac{H^2}{r^2}-\dfrac{r^2\dot r^2}{c^2}-\dfrac{gr^2}{c}$. Adding $q^2\dot r^2$ to both sides and using $q^2-r^2/c^2=1$:

$$q^2\big(\dot r^2+r\ddot r\big)=\dot r^2+\frac{H^2}{r^2}-\frac{gr^2}{c}$$

From the energy of (c), $q^2\dot r^2=2E/m-H^2/r^2-gr^2/c$. Multiplying the previous line by $q^2$ and substituting $q^2\dot r^2$:

$$q^4\big(\dot r^2+r\ddot r\big)=\frac{2E}{m}-\frac{H^2}{r^2}-\frac{gr^2}{c}+q^2\frac{H^2}{r^2}-q^2\frac{gr^2}{c}=\frac{2E}{m}+\frac{H^2}{c^2}-\Big(2+\frac{r^2}{c^2}\Big)\frac{gr^2}{c}$$

because $(q^2-1)\dfrac{H^2}{r^2}=\dfrac{H^2}{c^2}$ and $(1+q^2)\dfrac{gr^2}{c}=\Big(2+\dfrac{r^2}{c^2}\Big)\dfrac{gr^2}{c}$. So

$$\dot r^2+r\ddot r=\frac{1}{q^4}\Big[\frac{2E}{m}+\frac{H^2}{c^2}-\Big(2+\frac{r^2}{c^2}\Big)\frac{gr^2}{c}\Big]$$

Substituting in $N=mq\big[(\dot r^2+r\ddot r)/c+g\big]=\dfrac{m}{cq^3}\big[q^4(\dot r^2+r\ddot r)+gc\,q^4\big]$ and using the identity

$$gc\,q^4-\Big(2+\frac{r^2}{c^2}\Big)\frac{gr^2}{c}=gc\Big(1+\frac{2r^2}{c^2}+\frac{r^4}{c^4}\Big)-\frac{2gr^2}{c}-\frac{gr^4}{c^3}=gc$$

we get $N=\dfrac{m}{cq^3}\Big(\dfrac{2E}{m}+\dfrac{H^2}{c^2}+gc\Big)$, and with $cq^3=(c^2+r^2)^{3/2}/c^2$:

$$N=\frac{m\,\big(2c^2E/m+H^2+gc^3\big)}{(c^2+r^2)^{3/2}}$$

With $V=mgz\ge0$ the energy is positive, so $N>0$ on **every** motion: the particle never leaves the inner face. In the numerical case $2c^2E/m+H^2+gc^3=\tfrac54gc^3+\tfrac14gc^3+gc^3=\tfrac52gc^3$, so $N=\dfrac{5mgc^3}{2(c^2+r^2)^{3/2}}$, decreasing from $1.789\,mg$ at $r=c/2$ to its minimum $0.884\,mg$ at $r=c$, in agreement with Step 3.

## Interpretation

- **Dimensional check:** $c$ is a length, so $g/c$ and $\omega_r^2=4gc/(c^2+r_0^2)$ are s$^{-2}$; $H=r^2\dot\varphi$ is m$^2$ s$^{-1}$, $H^2/r^3$ and $gr/c$ are m s$^{-2}$; in $N$, $(2c^2E/m+H^2+gc^3)$ is m$^4$ s$^{-2}$ and $(c^2+r^2)^{3/2}$ is m$^3$: $N$ is kg m s$^{-2}$.
- **Limits:** $c\to\infty$ (flat floor): $\Omega_0\to0$, no horizontal circle without a wall. $r_0\ll c$: the bowl acts as an isotropic linear spring, $\omega_r=2\Omega_0$ and the orbits are centred ellipses.
- **Common mistakes in the exam:** (1) claiming that the angular momentum about $O$ is conserved because "the reaction is normal": only the axial component is; (2) expecting the orbital rate to depend on $r_0$ (it does not on a paraboloid); (3) linearising without the factor $1+r_0^2/c^2$, which gives $\omega_r=2\Omega_0$ for every radius; (4) solving the quartic for the turning points instead of noticing that $r_0$ is a root; (5) not checking $N\ge0$ for a unilateral contact.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
