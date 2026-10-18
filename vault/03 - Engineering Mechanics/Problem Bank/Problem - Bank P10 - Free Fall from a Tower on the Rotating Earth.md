---
materia: Engineering Mechanics
tema: "Unit 5: dynamics in a rotating frame (Coriolis force on the Earth)"
bank_id: P10
title: "Free fall from a tower on the rotating Earth: eastward deflection, the order of the north-south effect and an upward shot"
category: midterm_problem
archetype: relative-motion
level: standard
unit: 5
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2011 to 2019); not an official exercise. Verified with scripts/mechanics/p10.py"
tags:
  - problem-bank
  - midterm-1
  - rotating-frame
  - coriolis
  - perturbation
  - earth-rotation
---

# Bank P10 — Free fall from a tower on the rotating Earth

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §3.2 (velocity and acceleration in a moving frame), §4.9 (dynamics of relative motion) and §4.3 (equations of motion). Every equation and number was checked with SymPy and with a numerical integration of the exact equations.

## Statement

A particle $P$ of mass $m$ is released **from rest relative to the ground** from the top of a tower of height $h$ standing at the point $A$ of the Earth's surface at latitude $\lambda$ (northern hemisphere). The Earth rotates with constant angular velocity of modulus $\Omega$ about its polar axis, whose unit vector $\mathbf k_E$ points to the north pole; the centre of the Earth is taken as fixed in an inertial frame $S_0$.

The local frame $S_1=\{A;\mathbf i,\mathbf j,\mathbf k\}$ is attached to the ground at the foot $A$ of the tower and rotates with the Earth: $x$ points **east**, $y$ points **north**, $z$ points **up** along the plumb line. In $S_1$ the particle feels the effective gravity $-g\,\mathbf k$, which already contains the centrifugal force of the point $A$ (gravitation plus $-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r_{CA})$, $C$ the centre of the Earth). Air drag is neglected and $h$ is small compared with the radius of the Earth.

![[attachments/EM-M1/p10-earth-free-fall.svg]]

## Setup

- Data: $m$, $h$, $g$, $\Omega$, $\lambda$. Numerical part: $h=100$ m, $\lambda=40^\circ$, $g=9.81$ m s$^{-2}$, $\Omega=7.292\times10^{-5}$ rad s$^{-1}$ ($2\pi$ per sidereal day of $86\,164$ s).
- Hypotheses: point particle, uniform effective gravity along the height of the tower, $\Omega$ constant, $\Omega t\ll1$ during the fall (so a solution to first order in $\Omega$ is meaningful), no drag.
- $S_1$ is a **rotating** frame: $\boldsymbol\omega_{10}=\Omega\,\mathbf k_E$ with $\dot{\boldsymbol\omega}_{10}=\mathbf 0$.

## (a) Degrees of freedom, angular velocity of $S_1$ and inertia forces [1.5 pts]

How many degrees of freedom has $P$? Write $\boldsymbol\omega_{10}$ in the basis of $S_1$ and list the inertia forces that act on $P$ in $S_1$, saying which one is absorbed into $-g\,\mathbf k$ and which one is kept.

### Hint

The polar axis lies in the meridian plane of $A$ (the $yz$ plane) and makes the angle $\lambda$ with the local horizontal pointing north. Write the drag (transport) acceleration of $S_1$ at $P$ with $\mathbf r_{CP}=\mathbf r_{CA}+\mathbf r$.

### Checkpoint

- 3 degrees of freedom $(x,y,z)$, no constraint during the fall.
- $\boldsymbol\omega_{10}=\Omega\cos\lambda\,\mathbf j+\Omega\sin\lambda\,\mathbf k$, constant.
- Inertia forces: centrifugal $-m\boldsymbol\Omega\times\big(\boldsymbol\Omega\times(\mathbf r_{CA}+\mathbf r)\big)$ (the part with $\mathbf r_{CA}$ is in $g$; the part with $\mathbf r$ is $O(\Omega^2h)$ and is neglected) and Coriolis $-2m\boldsymbol\Omega\times\mathbf v_{rel}$ (kept). No Euler force.

### Solution

#### Step 1. Count

$P$ is a free particle in space: 3 degrees of freedom, the coordinates $(x,y,z)$ of $\mathbf r=\overrightarrow{AP}$ in $S_1$. Nothing constrains it between release and impact.

#### Step 2. The angular velocity in the local basis

The local vertical $\mathbf k$ is the plumb line at $A$ (statement), and the latitude $\lambda$ is measured from this plumb line: it is the angle between $\mathbf k$ and the equatorial plane. The angle between $\mathbf k$ and $\mathbf k_E$ is therefore $90^\circ-\lambda$, so $\mathbf k_E\cdot\mathbf k=\sin\lambda$ by definition of $\lambda$. The polar axis lies in the meridian plane through $A$, which contains $\mathbf j$ (north) and $\mathbf k$, so $\mathbf k_E\cdot\mathbf i=0$, and it leans towards the north: $\mathbf k_E\cdot\mathbf j=\cos\lambda$. Check: $\cos^2\lambda+\sin^2\lambda=1$. The ground turns with the Earth, so

$$\boldsymbol\omega_{10}=\Omega\,\mathbf k_E=\Omega\cos\lambda\,\mathbf j+\Omega\sin\lambda\,\mathbf k,\qquad \dot{\boldsymbol\omega}_{10}=\mathbf 0$$

#### Step 3. Change of basis

The polar axis is best described with the cylindrical basis of the Earth at $A$, $\{\mathbf e_\rho,\mathbf e_\varphi,\mathbf k_E\}$: $\mathbf e_\rho$ perpendicular to the polar axis and pointing away from it, in the meridian plane of $A$, $\mathbf e_\varphi=\mathbf i$ (east), $\mathbf k_E$ the polar axis. This basis turns about $\mathbf k_E$ with angular velocity $\Omega$ relative to $S_0$, like the local one. Projecting the local unit vectors ($\mathbf j\cdot\mathbf e_\rho=-\sin\lambda$, $\mathbf j\cdot\mathbf k_E=\cos\lambda$, $\mathbf k\cdot\mathbf e_\rho=\cos\lambda$, $\mathbf k\cdot\mathbf k_E=\sin\lambda$):

$$\begin{pmatrix}\mathbf i\\ \mathbf j\\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf e_\rho\\ \mathbf e_\varphi\\ \mathbf k_E\end{pmatrix},\qquad [R]=\begin{pmatrix}0&1&0\\ -\sin\lambda&0&\cos\lambda\\ \cos\lambda&0&\sin\lambda\end{pmatrix}$$

Checks: the rows have unit length ($1$, $\sin^2\lambda+\cos^2\lambda$, $\cos^2\lambda+\sin^2\lambda$) and are mutually orthogonal (row 1 with rows 2 and 3: $0$; rows 2 and 3: $-\sin\lambda\cos\lambda+\cos\lambda\sin\lambda=0$), so $[R][R]^T=I$; expanding along the first row, $\det[R]=-1\cdot\big((-\sin\lambda)\sin\lambda-\cos\lambda\cos\lambda\big)=+1$. The third column of $[R]$ gives back $\mathbf k_E=\cos\lambda\,\mathbf j+\sin\lambda\,\mathbf k$.

#### Step 4. Inertia forces (Notes §3.2 and §4.9)

The acceleration of $P$ in $S_0$ is $\mathbf a=\mathbf a_{rel}+\mathbf a_{drag}+2\boldsymbol\omega_{10}\times\mathbf v_{rel}$. The point of $S_1$ that coincides with $P$ moves on a circle about the polar axis (the centre $C$ is fixed and $\boldsymbol\omega_{10}$ constant), so $\mathbf a_{drag}=\boldsymbol\Omega\times\big(\boldsymbol\Omega\times\mathbf r_{CP}\big)$ with $\mathbf r_{CP}=\mathbf r_{CA}+\mathbf r$. In $S_1$, $m\mathbf a_{rel}=\mathbf F+\mathbf F_{cf}+\mathbf F_{cor}$ with

$$\mathbf F_{cf}=-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r_{CA})-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r),\qquad \mathbf F_{cor}=-2m\boldsymbol\Omega\times\mathbf v_{rel}$$

The first term is the same at every point of the tower: added to the gravitational attraction it gives the effective weight $-mg\,\mathbf k$ that a plumb line at $A$ measures (this is how $\mathbf k$ is defined). The second term has modulus at most $m\Omega^2h\approx5.3\times10^{-7}\,m$ m s$^{-2}$ for $h=100$ m: it is of order $\Omega^2$ and is dropped. The Coriolis force is of order $\Omega$ and is the one that matters.

## (b) Equations of motion in $S_1$ [2.0 pts]

Write the vector equation of motion of $P$ in $S_1$ and its three scalar components, with the initial conditions.

### Hint

Compute $\boldsymbol\Omega\times\mathbf v_{rel}$ with the determinant, $\mathbf v_{rel}=\dot x\,\mathbf i+\dot y\,\mathbf j+\dot z\,\mathbf k$.

### Checkpoint

- $\ddot x=-2\Omega\big(\dot z\cos\lambda-\dot y\sin\lambda\big)$, $\ \ddot y=-2\Omega\dot x\sin\lambda$, $\ \ddot z=-g+2\Omega\dot x\cos\lambda$.
- $x(0)=y(0)=0$, $z(0)=h$, $\dot x(0)=\dot y(0)=\dot z(0)=0$.

### Solution

#### Step 1. Vector equation

With the results of (a), the only forces in $S_1$ are the effective weight and the Coriolis force:

$$m\,\ddot{\mathbf r}=-mg\,\mathbf k-2m\,\boldsymbol\Omega\times\dot{\mathbf r}$$

#### Step 2. The cross product

$$\boldsymbol\Omega\times\dot{\mathbf r}=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\0&\Omega\cos\lambda&\Omega\sin\lambda\\\dot x&\dot y&\dot z\end{vmatrix}=\Omega\big(\dot z\cos\lambda-\dot y\sin\lambda\big)\mathbf i+\Omega\dot x\sin\lambda\,\mathbf j-\Omega\dot x\cos\lambda\,\mathbf k$$

#### Step 3. Components

Dividing by $m$ and projecting on $\mathbf i$, $\mathbf j$, $\mathbf k$:

$$\ddot x=-2\Omega\big(\dot z\cos\lambda-\dot y\sin\lambda\big),\qquad \ddot y=-2\Omega\dot x\sin\lambda,\qquad \ddot z=-g+2\Omega\dot x\cos\lambda$$

The particle starts at the top of the tower with zero velocity **relative to the ground** (in $S_0$ it moves east with the tower top): $\mathbf r(0)=h\,\mathbf k$, $\dot{\mathbf r}(0)=\mathbf 0$.

## (c) Solution to first order in $\Omega$ [2.0 pts]

Solve the equations to first order in $\Omega$ and show that the particle lands at $\Delta x=\dfrac{2\sqrt2}{3}\,\Omega\cos\lambda\sqrt{\dfrac{h^3}{g}}$ east of the foot of the tower. Does the time of fall change at this order?

### Hint

Write $\mathbf r=\mathbf r_0+\mathbf r_1+\dots$ with $\mathbf r_1=O(\Omega)$. In the Coriolis terms, which already carry a factor $\Omega$, insert the zeroth-order velocity.

### Checkpoint

- Order 0: $z_0=h-\tfrac12gt^2$, $\dot z_0=-gt$, $x_0=y_0=0$.
- Order 1: $\ddot x_1=2\Omega g t\cos\lambda$, $\ \dot x_1=\Omega gt^2\cos\lambda$, $\ x_1=\tfrac13\Omega gt^3\cos\lambda$; $y_1=z_1=0$.
- $t_f=\sqrt{2h/g}$ (unchanged at first order), $\Delta x=\tfrac{2\sqrt2}{3}\Omega\cos\lambda\sqrt{h^3/g}$, to the **east**.

### Solution

#### Step 1. Zeroth order

With $\Omega=0$: $\ddot x_0=\ddot y_0=0$ and $\ddot z_0=-g$, with $\dot{\mathbf r}_0(0)=\mathbf 0$ and $\mathbf r_0(0)=h\,\mathbf k$. Integrating twice with the limits $0$ and $t$ (antiderivative, then Barrow's rule $[F]_0^t=F(t)-F(0)$):

$$\dot z_0(t)=\dot z_0(0)+\int_0^t(-g)\,d\tau=0+\big[-g\tau\big]_0^t=-gt-(-g\cdot0)=-gt$$

$$z_0(t)=z_0(0)+\int_0^t(-g\tau)\,d\tau=h+\Big[-\tfrac12g\tau^2\Big]_0^t=h-\tfrac12gt^2$$

$$\dot x_0(t)=\dot x_0(0)+\int_0^t0\,d\tau=0,\qquad x_0(t)=x_0(0)+\int_0^t0\,d\tau=0$$

and in the same way $\dot y_0=0$, $y_0=0$.

#### Step 2. First order

Every Coriolis term carries a factor $\Omega$, so to first order the velocity inside it is the zeroth-order one, $\dot{\mathbf r}_0=-gt\,\mathbf k$:

$$\ddot x_1=-2\Omega\big(\dot z_0\cos\lambda-\dot y_0\sin\lambda\big)=2\Omega gt\cos\lambda,\qquad \ddot y_1=-2\Omega\dot x_0\sin\lambda=0,\qquad \ddot z_1=2\Omega\dot x_0\cos\lambda=0$$

with zero initial conditions, so $y_1=z_1=0$ and

$$\dot x_1=\int_0^t2\Omega g\cos\lambda\,\tau\,d\tau=\big[\Omega g\cos\lambda\,\tau^2\big]_0^t=\Omega gt^2\cos\lambda$$

$$x_1=\int_0^t\Omega g\cos\lambda\,\tau^2\,d\tau=\Big[\tfrac13\Omega g\cos\lambda\,\tau^3\Big]_0^t=\tfrac13\Omega gt^3\cos\lambda$$

#### Step 3. Landing point

Since $z_1=0$, the height is $h-\tfrac12gt^2$ up to $O(\Omega^2)$ and the particle reaches $z=0$ at $t_f=\sqrt{2h/g}$, as without rotation. Then $t_f^3=(2h/g)^{3/2}=2\sqrt2\,h^{3/2}/g^{3/2}$ and

$$\Delta x=x_1(t_f)=\tfrac13\Omega g\cos\lambda\cdot\frac{2\sqrt2\,h^{3/2}}{g^{3/2}}=\frac{2\sqrt2}{3}\,\Omega\cos\lambda\sqrt{\frac{h^3}{g}}>0$$

The particle lands **east** of the foot $A$.

#### Step 4. Physical reading in $S_0$

At release the top of the tower is a distance $h\cos\lambda$ farther from the polar axis than the foot, so in $S_0$ it moves east $\Omega h\cos\lambda$ faster **than the foot**. The particle keeps that eastward speed while it falls, which is why it ends up ahead of the foot. But this lead speed $\Omega h\cos\lambda$ is measured against the foot, not against the rotating ground under the particle: relative to the ground ($S_1$) the particle starts at rest, and its eastward speed $\dot x_1=\Omega gt^2\cos\lambda$ is zero at release and grows like $t^2$, as the particle descends to points of the ground that move more slowly. The crude estimate "lead speed $\Omega h\cos\lambda$ during the whole fall", $\Omega h\cos\lambda\,t_f$, assumes the full lead from the start and is therefore $3/2$ of the exact first-order value: with $h=\tfrac12gt_f^2$, $\Omega h\cos\lambda\,t_f=\tfrac12\Omega g\cos\lambda\,t_f^3$, against $\Delta x=\tfrac13\Omega g\cos\lambda\,t_f^3$.

## (d) Numbers [1.0 pts]

For $h=100$ m, $\lambda=40^\circ$: compute the time of fall and the eastward deflection. Where is the particle (east of the plumb line) at $t_f/2$?

### Hint

$x_1\propto t^3$.

### Checkpoint

- $t_f=\sqrt{200/9.81}=4.515$ s.
- $\Delta x=1.681$ cm east; $x_1(t_f/2)=\Delta x/8=0.210$ cm.

### Solution

#### Step 1. Time and deflection

$t_f=\sqrt{2\cdot100/9.81}=\sqrt{20.39}=4.515$ s. With $\cos40^\circ=0.7660$ and $\sqrt{h^3/g}=\sqrt{10^6/9.81}=319.3$ s:

$$\Delta x=\frac{2\sqrt2}{3}\,(7.292\times10^{-5})(0.7660)(319.3)\ \text{m}=1.681\times10^{-2}\ \text{m}=1.681\ \text{cm}$$

A numerical integration of the exact equations of (b) (no expansion) gives the same value to four significant figures.

#### Step 2. Half-way

$x_1\propto t^3$, so at $t_f/2$ the deflection is $(1/2)^3\Delta x=0.210$ cm: most of the deflection builds up in the second half of the fall.

## (e) Is there a north-south deflection? [1.5 pts]

A student integrates the $y$ equation once more and reports a southward deflection $y_2(t_f)=-\tfrac23\Omega^2h^2\sin\lambda\cos\lambda/g$. Check the formula, and say whether it is a consistent result of the model of the statement.

### Hint

Insert $\dot x_1$ in the $y$ equation. Then compare its order with the terms that were dropped in (a).

### Checkpoint

- $\ddot y_2=-2\Omega\dot x_1\sin\lambda=-2\Omega^2gt^2\sin\lambda\cos\lambda$, $\ y_2=-\tfrac16\Omega^2gt^4\sin\lambda\cos\lambda$; at $t_f$: $-\tfrac23\Omega^2h^2\sin\lambda\cos\lambda/g=-1.78\times10^{-6}$ m.
- The formula is right but **not consistent**: it is $O(\Omega^2)$, the same order as the residual centrifugal term $-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$ dropped in (a), whose own effect is $-\tfrac56\Omega^2h^2\sin\lambda\cos\lambda/g=-2.22\times10^{-6}$ m, and as the change of direction of gravitation along the fall. To first order in $\Omega$ there is no north-south deflection.

### Solution

#### Step 1. The second-order term

At second order the $y$ equation receives $\dot x_1$: $\ddot y_2=-2\Omega\dot x_1\sin\lambda=-2\Omega^2gt^2\sin\lambda\cos\lambda$. Integrating twice from rest:

$$\dot y_2(t)=\int_0^t\big(-2\Omega^2g\sin\lambda\cos\lambda\,\tau^2\big)\,d\tau=\Big[-\tfrac23\Omega^2g\sin\lambda\cos\lambda\,\tau^3\Big]_0^t=-\tfrac23\Omega^2gt^3\sin\lambda\cos\lambda$$

$$y_2(t)=\int_0^t\Big(-\tfrac23\Omega^2g\sin\lambda\cos\lambda\,\tau^3\Big)\,d\tau=\Big[-\tfrac16\Omega^2g\sin\lambda\cos\lambda\,\tau^4\Big]_0^t=-\tfrac16\Omega^2gt^4\sin\lambda\cos\lambda$$

(the lower limit contributes $0$ in both, since $\dot y_2(0)=y_2(0)=0$).

and with $t_f^4=4h^2/g^2$: $y_2(t_f)=-\tfrac23\Omega^2h^2\sin\lambda\cos\lambda/g$. With the data: $-1.78\times10^{-6}$ m, about $10^{-4}$ of $\Delta x$ (the ratio is $\tfrac12\Omega t_f\sin\lambda$).

#### Step 2. Why it is not a consistent answer

The equation of (b) is only exact to first order in $\Omega$: in (a) we dropped the residual centrifugal force $-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$, which is $O(\Omega^2)$. For $\mathbf r\approx z\,\mathbf k$ its $y$ component is $-m\Omega^2z\sin\lambda\cos\lambda$; with $z=z_0(t)$ it alone displaces the particle by

$$y_{cf}(t_f)=-\Omega^2\sin\lambda\cos\lambda\int_0^{t_f}\!\!\int_0^{\tau}z_0(s)\,ds\,d\tau=-\tfrac56\,\frac{\Omega^2h^2\sin\lambda\cos\lambda}{g}=-2.22\times10^{-6}\ \text{m}$$

which is larger than $y_2$. The direction of the gravitational attraction also changes along the vertical through $A$ by an amount of the same order. A second-order answer must collect all these terms; keeping only the Coriolis one is inconsistent. **To first order in $\Omega$, the only deflection is the eastward one**, and $y=O(\Omega^2)$ is at the micrometre level.

## (f) A projectile fired vertically upward [2.0 pts]

From $A$ a projectile is fired vertically upward (along $\mathbf k$) with speed $v_0$ relative to the ground. To first order in $\Omega$, where does it land? Compute it for $v_0=50$ m s$^{-1}$ at $\lambda=40^\circ$, and compare with the drop of (c) from the same maximum height.

### Hint

Same expansion, now with $\dot z_0=v_0-gt$. Look at the sign of $\dot x_1$ during the whole flight.

### Checkpoint

- $\ddot x_1=-2\Omega\cos\lambda\,(v_0-gt)$, $\ \dot x_1=-\Omega g\cos\lambda\,t\,(T-t)\le0$, $\ x_1=-\Omega\cos\lambda\big(v_0t^2-\tfrac13gt^3\big)$, with $T=2v_0/g$.
- $\Delta x=-\tfrac43\,\Omega\cos\lambda\,v_0^3/g^2$: it lands **west** of $A$; $-9.674$ cm for $v_0=50$ m s$^{-1}$ ($T=10.19$ s, apex $127.4$ m).
- With $v_0=\sqrt{2gh}$ the westward offset is $4$ times the eastward deflection of the drop from $h$.

### Solution

#### Step 1. Zeroth and first order

Order 0: $z_0=v_0t-\tfrac12gt^2$, $\dot z_0=v_0-gt$, back at $z=0$ at $T=2v_0/g$. Order 1, from the $x$ equation of (b) with $\dot y_0=0$:

$$\ddot x_1=-2\Omega\cos\lambda\,(v_0-gt)$$

$$\dot x_1=\int_0^t-2\Omega\cos\lambda\,(v_0-g\tau)\,d\tau=-2\Omega\cos\lambda\Big[v_0\tau-\tfrac12g\tau^2\Big]_0^t=-\Omega g\cos\lambda\;t\Big(\frac{2v_0}{g}-t\Big)$$

$$x_1=\int_0^t-2\Omega\cos\lambda\Big(v_0\tau-\tfrac12g\tau^2\Big)d\tau=-2\Omega\cos\lambda\Big[\tfrac12v_0\tau^2-\tfrac16g\tau^3\Big]_0^t=-\Omega\cos\lambda\Big(v_0t^2-\tfrac13gt^3\Big)$$

#### Step 2. Landing point

At $T=2v_0/g$: $v_0T^2=4v_0^3/g^2$ and $\tfrac13gT^3=\tfrac83v_0^3/g^2$, so

$$\Delta x=x_1(T)=-\Omega\cos\lambda\Big(4-\tfrac83\Big)\frac{v_0^3}{g^2}=-\frac43\,\Omega\cos\lambda\,\frac{v_0^3}{g^2}<0$$

The projectile lands **west** of the launch point. With $v_0=50$ m s$^{-1}$: $\Delta x=-\tfrac43(7.292\times10^{-5})(0.7660)(125\,000)/96.24$ m $=-9.674$ cm; the flight lasts $T=10.19$ s and the apex is at $v_0^2/2g=127.4$ m.

#### Step 3. Why it does not cancel

On the way up ($\dot z_0>0$) the Coriolis force pushes west; on the way down it pushes east. The symmetric-looking guess "the two halves cancel" confuses force with displacement: $\dot x_1=-\Omega g\cos\lambda\,t(T-t)$ is negative during the whole flight and only returns to zero at $t=T$. The westward velocity gained on the way up is removed on the way down, but the westward **displacement** accumulated meanwhile remains.

#### Step 4. Comparison with the drop

Setting $v_0=\sqrt{2gh}$ (apex at height $h$): $\Delta x_{up}=-\tfrac43\Omega\cos\lambda(2gh)^{3/2}/g^2=-4\cdot\tfrac{2\sqrt2}{3}\Omega\cos\lambda\sqrt{h^3/g}$, that is, $-4$ times the eastward deflection of (c): $-6.73$ cm for $h=100$ m. The descent of the projectile alone would push it $1.68$ cm east, but it starts the descent already moving west.

## Interpretation

- **Dimensional check:** $[\Omega gt^3]=\text{s}^{-1}\cdot\text{m s}^{-2}\cdot\text{s}^3=\text{m}$; $[\Omega\sqrt{h^3/g}]=\text{s}^{-1}\sqrt{\text{m}^3/(\text{m s}^{-2})}=\text{s}^{-1}\cdot\text{m s}=\text{m}$; $[\Omega v_0^3/g^2]=\text{s}^{-1}\,\text{m}^3\text{s}^{-3}/(\text{m}^2\text{s}^{-4})=\text{m}$.
- **Limits:** at the poles ($\lambda=90^\circ$) $\cos\lambda=0$: $\boldsymbol\Omega$ is vertical, parallel to the fall, and there is no deflection; it is largest at the equator. In the southern hemisphere ($\lambda<0$) $\cos\lambda>0$ still: the drop also lands **east**. The expansion requires $\Omega t_f\ll1$ (here $3.3\times10^{-4}$).
- **Common mistakes in the exam:** (1) writing $\boldsymbol\Omega=\Omega\,\mathbf k$ (the local vertical) instead of $\Omega(\cos\lambda\,\mathbf j+\sin\lambda\,\mathbf k)$; (2) a sign error in the Coriolis force (it is $-2m\boldsymbol\Omega\times\mathbf v_{rel}$) that sends the particle west; (3) keeping $O(\Omega^2)$ Coriolis terms while dropping the centrifugal term of the same order; (4) assuming that the up and down halves of a vertical shot cancel.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
