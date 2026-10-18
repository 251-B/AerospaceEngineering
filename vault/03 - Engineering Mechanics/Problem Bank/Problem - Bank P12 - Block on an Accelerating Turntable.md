---
materia: Engineering Mechanics
tema: "Unit 3: Coulomb friction; units 1 and 5: polar kinematics and inertia forces in a rotating frame"
bank_id: P12
title: "Block on an accelerating turntable: the friction cone, the instant of slip and the direction in which the block starts to slide"
category: midterm_problem
archetype: constraints
level: standard
unit: 3
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2011 to 2019); not an official exercise. Verified with scripts/mechanics/p12.py"
tags:
  - problem-bank
  - midterm-1
  - coulomb-friction
  - polar-coordinates
  - rotating-frame
  - euler-force
---

# Bank P12 — Block on an accelerating turntable

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §2.6.2 (polar coordinates), §2.7 (degrees of freedom and constraints), §6.6 (friction forces), §3.2 and §4.9 (relative motion). Every equation and number was checked with SymPy.

## Statement

A horizontal turntable rotates about the fixed vertical axis through its centre $O$. It starts from rest at $t=0$ with constant angular acceleration $\beta>0$, so its angular rate is $\Omega(t)=\beta t$ (counter-clockwise seen from above). A small block $P$ of mass $m$ rests on the table at the distance $r_0$ from the axis; at $t=0$ it lies on the fixed $x$ axis. The contact is rough, with static Coulomb coefficient $\mu$ and kinetic coefficient $\mu_k\le\mu$; gravity is $-g\,\mathbf k$.

Use the inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ ($\mathbf k$ vertical, upward), the turntable frame $S_1$ (rotating with the table), the angle $\varphi$ of $\overrightarrow{OP}$ from the $x$ axis and the unit vectors $\mathbf e_r=\cos\varphi\,\mathbf i+\sin\varphi\,\mathbf j$, $\mathbf e_\varphi=\cos\varphi\,\mathbf j-\sin\varphi\,\mathbf i$.

![[attachments/EM-M1/p12-turntable-block.svg]]

## Setup

- Data: $m$, $g$, $\mu$, $\mu_k$, $r_0$, $\beta$. Numbers: $\mu=0.4$, $\mu_k=0.3$, $r_0=0.5$ m, $\beta=0.2$ rad s$^{-2}$, $g=9.81$ m s$^{-2}$.
- Hypotheses: point particle (the block does not tip), rigid horizontal table, Coulomb friction, no air drag.
- In (e) and (f) the friction force on $P$ is written $\mathbf F=F_r\,\mathbf e_r+F_\varphi\,\mathbf e_\varphi$ and $\psi$ is its angle from the inward radius $-\mathbf e_r$, positive towards $+\mathbf e_\varphi$ (figure).

## (a) Degrees of freedom and frames [1.0 pts]

How many degrees of freedom has $P$ while it sticks to the table, and while it slides on it? Give the angular velocity and the angular acceleration of $S_1$ relative to $S_0$.

### Hint

Contact with the table fixes $z$. Sticking is an extra (temporary) constraint.

### Checkpoint

- Sliding: 2 degrees of freedom $(r,\varphi)$ on the plane $z=0$. Sticking: 0 degrees of freedom, $r=r_0$, $\varphi=\tfrac12\beta t^2$ prescribed.
- $\boldsymbol\omega_{10}=\beta t\,\mathbf k$, $\dot{\boldsymbol\omega}_{10}=\beta\,\mathbf k$.

### Solution

#### Step 1. Count

A free particle has 3 degrees of freedom. While it touches the table, $z=0$ (bilateral as long as $N\ge0$): 2 remain, the polar coordinates $(r,\varphi)$. While it does not slip, it moves with the table: $r=r_0$ and $\varphi$ is the angle turned by the table, $\varphi=\int_0^t\beta\tau\,d\tau=\big[\tfrac12\beta\tau^2\big]_0^t=\tfrac12\beta t^2$. Nothing is left free: 0 degrees of freedom, and the friction force is an **unknown reaction** that adjusts to keep the block in place, as long as it can (Notes §6.6).

#### Step 2. Frames

$S_1$ turns about $\mathbf k$ with $\boldsymbol\omega_{10}=\Omega\,\mathbf k=\beta t\,\mathbf k$; its angular acceleration $\dot{\boldsymbol\omega}_{10}=\beta\,\mathbf k$ is not zero, so in $S_1$ the block feels an Euler force as well as the centrifugal and Coriolis forces.

## (b) Kinematics while the block sticks [1.5 pts]

Compute the velocity and acceleration of $P$ in $S_0$ in the basis $\{\mathbf e_r,\mathbf e_\varphi\}$.

### Hint

Polar formulas with $\dot r=\ddot r=0$, $\dot\varphi=\Omega$, $\ddot\varphi=\beta$.

### Checkpoint

- $\mathbf v=r_0\Omega\,\mathbf e_\varphi$.
- $\mathbf a=-r_0\Omega^2\,\mathbf e_r+r_0\beta\,\mathbf e_\varphi$: centripetal **and** tangential parts.

### Solution

#### Step 1. Change of basis and unit vectors

The polar basis $\{\mathbf e_r,\mathbf e_\varphi,\mathbf k\}$ turns with the table; its relation to the inertial basis is

$$\begin{pmatrix}\mathbf e_r\\ \mathbf e_\varphi\\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\\ \mathbf j\\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\varphi&\sin\varphi&0\\ -\sin\varphi&\cos\varphi&0\\ 0&0&1\end{pmatrix}$$

Checks: rows 1 and 2 have length $\cos^2\varphi+\sin^2\varphi=1$ and $-\cos\varphi\sin\varphi+\sin\varphi\cos\varphi=0$, row 3 is $\mathbf k$, so $[R][R]^T=I$; $\det[R]=\cos^2\varphi+\sin^2\varphi=+1$ (right-handed, $\mathbf e_r\times\mathbf e_\varphi=\mathbf k$). Then $\dot{\mathbf e}_r=\dot\varphi\,(-\sin\varphi\,\mathbf i+\cos\varphi\,\mathbf j)=\dot\varphi\,\mathbf e_\varphi$ and $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_r$ (chain rule through $\varphi(t)$).

#### Step 2. Velocity and acceleration

$\mathbf r=r_0\,\mathbf e_r$ with $r_0$ constant:

$$\mathbf v=r_0\dot\varphi\,\mathbf e_\varphi=r_0\Omega\,\mathbf e_\varphi$$

$$\mathbf a=r_0\ddot\varphi\,\mathbf e_\varphi+r_0\dot\varphi\,\dot{\mathbf e}_\varphi=r_0\beta\,\mathbf e_\varphi-r_0\Omega^2\,\mathbf e_r$$

The general polar formula $\mathbf a=(\ddot r-r\dot\varphi^2)\mathbf e_r+(r\ddot\varphi+2\dot r\dot\varphi)\mathbf e_\varphi$ gives the same with $\dot r=\ddot r=0$.

## (c) Forces and the friction needed to stick [2.0 pts]

List the forces on $P$ and find the normal reaction and the friction force needed for the block to move with the table. Check the result in $S_1$.

### Hint

Newton in $S_0$, projected on $\mathbf k$, $\mathbf e_r$, $\mathbf e_\varphi$. In $S_1$ the block is at rest: the forces including the inertia forces add up to zero.

### Checkpoint

- $N=mg$; $\ F_r=-mr_0\Omega^2=-mr_0\beta^2t^2$; $\ F_\varphi=mr_0\beta$.
- $|\mathbf F|=mr_0\sqrt{\Omega^4+\beta^2}$, increasing in time.
- In $S_1$: $\mathbf F+mr_0\Omega^2\,\mathbf e_r-mr_0\beta\,\mathbf e_\varphi=\mathbf 0$ (centrifugal and Euler forces, no Coriolis).

### Solution

#### Step 1. Forces

Weight $-mg\,\mathbf k$; normal reaction $N\,\mathbf k$ ($N\ge0$); friction $\mathbf F=F_r\,\mathbf e_r+F_\varphi\,\mathbf e_\varphi$ in the plane of contact, unknown while the block sticks.

#### Step 2. Newton in $S_0$

$m\mathbf a=-mg\,\mathbf k+N\,\mathbf k+\mathbf F$. Projecting:

$$\mathbf k:\ 0=N-mg\Rightarrow N=mg;\qquad \mathbf e_r:\ -mr_0\Omega^2=F_r;\qquad \mathbf e_\varphi:\ mr_0\beta=F_\varphi$$

Friction must pull **inward** (to bend the path) and **forward** (to speed the block up along with the table).

#### Step 3. Check in $S_1$ (Notes §4.9)

In $S_1$ the block is at rest, $\mathbf v_{rel}=\mathbf 0$, so the Coriolis force vanishes. Centrifugal: $-m\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)=-m\Omega^2\,\mathbf k\times(\mathbf k\times r_0\mathbf e_r)=-m\Omega^2\,\mathbf k\times r_0\mathbf e_\varphi=mr_0\Omega^2\,\mathbf e_r$. Euler: $-m\dot{\boldsymbol\omega}\times\mathbf r=-m\beta\,\mathbf k\times r_0\mathbf e_r=-mr_0\beta\,\mathbf e_\varphi$. Balance in the plane: $\mathbf F+mr_0\Omega^2\mathbf e_r-mr_0\beta\,\mathbf e_\varphi=\mathbf 0$, the same $F_r$ and $F_\varphi$.

## (d) When does the block slip? [2.0 pts]

Using the Coulomb condition, find the instant $t^*$ at which the block starts to slide. What condition must $\beta$ satisfy for the block to stick at all?

### Hint

The friction force must lie inside the friction cone: $|\mathbf F|\le\mu N$. Use the **modulus** of $\mathbf F$, both components.

### Checkpoint

- $r_0^2\big(\Omega^4+\beta^2\big)\le\mu^2g^2$; slip when $\Omega^{*4}=\Big(\dfrac{\mu g}{r_0}\Big)^2-\beta^2$.
- $t^*=\dfrac{\Omega^*}{\beta}=\dfrac1\beta\Big[\Big(\dfrac{\mu g}{r_0}\Big)^2-\beta^2\Big]^{1/4}$; requires $\beta<\mu g/r_0$ (at $\beta=\mu g/r_0$, $t^*=0$), otherwise it slips at $t=0$.

### Solution

#### Step 1. The friction cone

Static friction holds while $|\mathbf F|\le\mu N$ (Notes §6.6). With (c):

$$m^2r_0^2\big(\Omega^4+\beta^2\big)\le\mu^2m^2g^2\ \Longleftrightarrow\ \Omega^4\le\Big(\frac{\mu g}{r_0}\Big)^2-\beta^2$$

#### Step 2. Slip instant

The left side grows with $t$ ($\Omega=\beta t$), so the inequality fails for the first time when it becomes an equality:

$$\Omega^*=\Big[\Big(\frac{\mu g}{r_0}\Big)^2-\beta^2\Big]^{1/4},\qquad t^*=\frac{\Omega^*}{\beta}$$

#### Step 3. Existence

A real $\Omega^*\ge0$ needs $\beta\le\mu g/r_0$. In the equality case $\beta=\mu g/r_0$ the formula gives $\Omega^*=0$, $t^*=0$: the friction is already at the limit of the cone at $t=0$ and the block slides as soon as $\Omega>0$, so it never sticks for a finite time. Sticking therefore requires the strict condition $\beta<\mu g/r_0$. If $\beta>\mu g/r_0$, already at $t=0$ (where $\Omega=0$) the tangential friction $mr_0\beta$ needed exceeds $\mu mg$: the table slides under the block from the start. Dropping $\beta^2$ in the cone (the usual shortcut $r_0\Omega^2=\mu g$) hides exactly this case.

## (e) Numbers and the direction of the friction at the slip instant [1.5 pts]

For the data of the Setup compute $\Omega^*$, $t^*$, the number of turns before slip and the speed of the block, and the angle $\psi$ of the friction force at $t^*$.

### Hint

$\tan\psi=F_\varphi/|F_r|$.

### Checkpoint

- $\mu g/r_0=7.848$ s$^{-2}$, $\Omega^{*4}=61.551$ s$^{-4}$, $\Omega^*=2.801$ rad s$^{-1}$, $t^*=14.00$ s.
- $\varphi^*=\Omega^{*2}/2\beta=19.61$ rad $=3.12$ turns; $\ |\mathbf v|=r_0\Omega^*=1.400$ m s$^{-1}$.
- $\tan\psi=\beta/\Omega^{*2}=0.0255$, $\psi=1.460^\circ$, inward and slightly forward.

### Solution

#### Step 1. Instant of slip

$\mu g/r_0=0.4\cdot9.81/0.5=7.848$ s$^{-2}$, so $(\mu g/r_0)^2=61.591$ s$^{-4}$ and $\Omega^{*4}=61.591-0.04=61.551$ s$^{-4}$. Then $\Omega^{*2}=7.8454$ s$^{-2}$, $\Omega^*=2.801$ rad s$^{-1}$ and $t^*=2.801/0.2=14.00$ s. Here $\beta^2/(\mu g/r_0)^2=6.5\times10^{-4}$: the tangential part barely changes $t^*$.

#### Step 2. Turns and speed

$\varphi^*=\tfrac12\beta t^{*2}=\Omega^{*2}/(2\beta)=7.8454/0.4=19.61$ rad, i.e. $19.61/2\pi=3.12$ turns. The speed is $r_0\Omega^*=1.400$ m s$^{-1}$, along $\mathbf e_\varphi$.

#### Step 3. Direction of the friction

At $t^*$: $|F_r|=mr_0\Omega^{*2}=3.923\,m$ N and $F_\varphi=mr_0\beta=0.1\,m$ N, so $\tan\psi=\beta/\Omega^{*2}=0.2/7.8454=0.0255$ and $\psi=1.460^\circ$. Check: $\cos\psi=r_0\Omega^{*2}/(\mu g)$, and $|\mathbf F|=\mu mg=3.924\,m$ N. The friction points to the axis, tilted $1.46^\circ$ **forward**.

## (f) How does the block start to slide? [2.0 pts]

Just after $t^*$ the friction is kinetic, of modulus $\mu_kmg$. Find the initial acceleration of $P$ relative to the table, its modulus and its direction. Does the block leave along the radius? Describe its motion in $S_0$ at that instant.

### Hint

At $t^{*+}$ the relative velocity is still zero: no Coriolis force. Kinetic friction opposes the relative sliding that is about to start, so it is aligned with the inertia forces.

### Checkpoint

- In $S_1$: centrifugal $+$ Euler $=-\mathbf F_{needed}$, of modulus $\mu mg$, pointing **outward and backward** (at $\psi$ behind the outward radius).
- $\mathbf a_{rel}(t^{*+})=(\mu-\mu_k)\,g$ in that direction: $0.981$ m s$^{-2}$, components $0.9807$ m s$^{-2}$ along $\mathbf e_r$ and $-0.0250$ m s$^{-2}$ along $\mathbf e_\varphi$.
- In $S_0$ the velocity is tangential ($1.400$ m s$^{-1}$, no radial launch) and the acceleration $\mu_kg=2.943$ m s$^{-2}$ is smaller than the $\mu g=3.924$ m s$^{-2}$ needed to follow the table.

### Solution

#### Step 1. Inertia forces at $t^*$

In $S_1$, with $\mathbf v_{rel}=\mathbf 0$, the inertia forces are those of (c): $\mathbf F_{in}=mr_0\Omega^{*2}\,\mathbf e_r-mr_0\beta\,\mathbf e_\varphi$. By (c) and (d), $\mathbf F_{in}=-\mathbf F_{needed}$ and $|\mathbf F_{in}|=\mu mg$. It points outward and **backward** (against the rotation), at the angle $\psi$ from $+\mathbf e_r$.

#### Step 2. Direction of sliding

Once static friction fails, the block starts to move relative to the table along the unit vector $\hat{\mathbf u}$ of its relative acceleration, and kinetic friction opposes that motion: $\mathbf F_k=-\mu_kmg\,\hat{\mathbf u}$. In $S_1$, $m\mathbf a_{rel}=\mathbf F_{in}-\mu_kmg\,\hat{\mathbf u}$ must be parallel to $\hat{\mathbf u}$, which is possible only if $\hat{\mathbf u}$ is along $\mathbf F_{in}$:

$$\mathbf a_{rel}(t^{*+})=(\mu-\mu_k)\,g\;\frac{\mathbf F_{in}}{|\mathbf F_{in}|},\qquad |\mathbf a_{rel}|=(0.4-0.3)\cdot9.81=0.981\ \text{m s}^{-2}$$

Components: $0.981\cos\psi=0.9807$ m s$^{-2}$ outward and $-0.981\sin\psi=-0.0250$ m s$^{-2}$ along $\mathbf e_\varphi$: the block **lags behind** the table as it drifts out. It does not start along the radius.

#### Step 3. Cross-check in $S_0$

In $S_0$, $\mathbf a=\mathbf F_k/m=\mu_kg\,\hat{\mathbf F}_{needed}$ (inward and forward, $2.943$ m s$^{-2}$), while the point of the table under the block has $\mathbf a_{drag}=\mu g\,\hat{\mathbf F}_{needed}$ ($3.924$ m s$^{-2}$, part (c)). With $\mathbf v_{rel}=\mathbf 0$ the Coriolis term vanishes and $\mathbf a_{rel}=\mathbf a-\mathbf a_{drag}=(\mu_k-\mu)g\,\hat{\mathbf F}_{needed}$: the same result. In $S_0$ the block moves at $1.400$ m s$^{-1}$ **tangentially**; it is not "flung out along the radius". It simply cannot be pulled inward hard enough to stay on its circle, so its path opens out.

#### Step 4. Equal coefficients

If $\mu_k=\mu$, $\mathbf a_{rel}(t^{*+})=\mathbf 0$: the sliding starts smoothly, driven by the growth of $\Omega$ after $t^*$, but in the same direction.

## Interpretation

- **Dimensional check:** $\mu g/r_0$ and $\beta$ are s$^{-2}$, so $\Omega^{*4}=(\mu g/r_0)^2-\beta^2$ is s$^{-4}$ and $t^*=\Omega^*/\beta$ is s; $r_0\Omega^2$, $r_0\beta$, $\mu g$ are m s$^{-2}$.
- **Limits:** $\beta\to0$ (very slow spin-up) gives $r_0\Omega^{*2}=\mu g$, the classic result for uniform rotation, with $\psi\to0$ and sliding along the outward radius in $S_1$; $\beta\to\mu g/r_0$ gives $t^*\to0$ and $\psi\to90^\circ$: the block slides straight backward.
- **Common mistakes in the exam:** (1) writing $r_0\Omega^2\le\mu g$ and forgetting the tangential friction $mr_0\beta$; (2) forgetting the Euler force $-m\dot{\boldsymbol\omega}\times\mathbf r$ in $S_1$; (3) putting $|\mathbf F|=\mu N$ before slip (static friction is only bounded by $\mu N$); (4) claiming the block flies off radially in $S_0$.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
