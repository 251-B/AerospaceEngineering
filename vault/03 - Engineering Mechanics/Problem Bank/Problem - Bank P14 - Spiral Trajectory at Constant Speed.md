---
materia: Engineering Mechanics
tema: "Units 1 and 4: polar and intrinsic kinematics, angular momentum of a non-central force"
bank_id: P14
title: "A spiral trajectory flown at constant speed: polar and intrinsic kinematics, a non-central force and zero power"
category: midterm_problem
archetype: kinematics
level: standard
unit: 1
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p14.py"
tags:
  - problem-bank
  - midterm-1
  - polar-coordinates
  - intrinsic-frame
  - radius-of-curvature
  - angular-momentum
  - power
---

# Bank P14 — A spiral trajectory flown at constant speed

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §2.4 and §2.5 (intrinsic basis, tangential and normal acceleration), §2.6 (polar and cylindrical coordinates), §4.8 (angular momentum and torque) and §4.5 (work, power and kinetic energy). Every number was checked with SymPy.

## Statement

A drone $P$ of mass $m$ flies in a **horizontal** plane (its weight is balanced by the vertical lift, which is not studied). In this plane take the inertial frame $S_0=\{O;\mathbf i,\mathbf j\}$ and the polar coordinates $(r,\varphi)$ of $P$ about $O$, with $\varphi$ measured from $\mathbf i$ counter-clockwise and the polar basis $\mathbf e_r=\cos\varphi\,\mathbf i+\sin\varphi\,\mathbf j$, $\mathbf e_\varphi=-\sin\varphi\,\mathbf i+\cos\varphi\,\mathbf j$. The autopilot keeps $P$ on the logarithmic spiral

$$r=r_0\,e^{b\varphi}\qquad(r_0>0,\ b>0)$$

with a **constant speed** $|\mathbf v|=v_0$ and $\varphi$ increasing. At $t=0$ the drone is at $\varphi=0$, $r=r_0$. The resultant of the horizontal forces on the drone (thrust and drag) is called $\mathbf F$. Let $\mathbf e_t$, $\mathbf e_n$ be the unit tangent and the principal normal of the trajectory, $\rho$ its radius of curvature and $\alpha$ the angle between $\mathbf e_r$ and $\mathbf e_t$.

![[attachments/EM-M1/p14-log-spiral.svg]]

## Setup

- Data: $r_0$, $b$, $v_0$, $m$. In the numerical parts: $r_0=20$ m, $b=3/4$, $v_0=10$ m/s, $m=2$ kg, and the drone flies from $r_1=r_0=20$ m to $r_2=50$ m.
- Hypotheses: point particle, planar motion in the horizontal plane, $S_0$ inertial; the trajectory and the speed are imposed by the autopilot (the force $\mathbf F$ is whatever is needed to keep them).
- Useful constant: $k\equiv\sqrt{1+b^2}$; for $b=3/4$, $k=\sqrt{1+9/16}=5/4$.

## (a) Velocity in polar coordinates and the constant angle [2.0 pts]

How many parameters fix the position of $P$ on the trajectory? Write $\mathbf v$ in the polar basis and obtain $\dot r$ and $\dot\varphi$ as functions of $r$ from the two conditions of the statement. Show that the angle $\alpha$ between the velocity and the radius is constant. Give the numbers for the data of the Setup.

### Hint

Differentiate $r=r_0e^{b\varphi}$ with the chain rule and substitute in $|\mathbf v|^2=\dot r^2+r^2\dot\varphi^2=v_0^2$.

### Checkpoint

- One parameter ($\varphi$, or $r$, or $s$); with the speed imposed, the motion is fully determined.
- $\dot r=b\,r\dot\varphi$, $\ \dot\varphi=\dfrac{v_0}{r\sqrt{1+b^2}}$, $\ \dot r=\dfrac{b\,v_0}{\sqrt{1+b^2}}$ **constant**.
- $\tan\alpha=\dfrac{r\dot\varphi}{\dot r}=\dfrac1b$; numbers: $\dot r=6$ m/s, $r\dot\varphi=8$ m/s, $\alpha=\arctan(4/3)=53.13^\circ$.

### Solution

#### Step 1. Parameters

A free point of the plane has two coordinates $(r,\varphi)$. The trajectory $r=r_0e^{b\varphi}$ is one relation between them, so one parameter (for instance $\varphi$, or $r$, or the arc length $s$) fixes the position on the curve. The speed law $|\mathbf v|=v_0$ then fixes how that parameter changes with time: nothing is left free, which is why this is a pure kinematics problem and $\mathbf F$ is an output.

#### Step 2. Velocity in the polar basis

The polar basis turns with $\varphi$; its relation to the inertial basis is

$$\begin{pmatrix}\mathbf e_r\ \mathbf e_\varphi\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\varphi&\sin\varphi\ -\sin\varphi&\cos\varphi\end{pmatrix}$$

with $[R][R]^T=\begin{pmatrix}\cos^2\varphi+\sin^2\varphi&-\cos\varphi\sin\varphi+\sin\varphi\cos\varphi\ -\sin\varphi\cos\varphi+\cos\varphi\sin\varphi&\sin^2\varphi+\cos^2\varphi\end{pmatrix}=I$ and $\det[R]=\cos^2\varphi+\sin^2\varphi=+1$ (same orientation as $\{\mathbf i,\mathbf j\}$). Differentiating the rows with the chain rule gives $\dot{\mathbf e}_r=\dot\varphi\,\mathbf e_\varphi$ and $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_r$.

With $\dot{\mathbf e}_r=\dot\varphi\,\mathbf e_\varphi$ and $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_r$ (Notes §2.6), differentiating $\mathbf r=r\,\mathbf e_r$ with the product rule:

$$\mathbf v=\dot r\,\mathbf e_r+r\,\dot{\mathbf e}_r=\dot r\,\mathbf e_r+r\dot\varphi\,\mathbf e_\varphi$$

#### Step 3. The trajectory relates $\dot r$ and $\dot\varphi$

By the chain rule $\frac{d}{dt}r(\varphi(t))=\frac{dr}{d\varphi}\dot\varphi$, with $\frac{dr}{d\varphi}=b\,r_0e^{b\varphi}=b\,r$:

$$\dot r=b\,r\,\dot\varphi$$

#### Step 4. The speed fixes $\dot\varphi$

$$|\mathbf v|^2=\dot r^2+r^2\dot\varphi^2=b^2r^2\dot\varphi^2+r^2\dot\varphi^2=(1+b^2)\,r^2\dot\varphi^2=v_0^2$$

With $\dot\varphi>0$ (the statement):

$$\dot\varphi=\frac{v_0}{r\sqrt{1+b^2}},\qquad \dot r=b\,r\dot\varphi=\frac{b\,v_0}{\sqrt{1+b^2}}$$

The radial velocity is **constant** although $\dot\varphi$ is not: $\dot\varphi$ decreases as $1/r$.

#### Step 5. The angle with the radius

$\mathbf v=v_0\,\mathbf e_t$, so $\cos\alpha=\mathbf e_r\cdot\mathbf e_t=\dot r/v_0$ and $\sin\alpha=\mathbf e_\varphi\cdot\mathbf e_t=r\dot\varphi/v_0$:

$$\tan\alpha=\frac{r\dot\varphi}{\dot r}=\frac{r\dot\varphi}{b\,r\dot\varphi}=\frac1b$$

independent of the point: the logarithmic spiral cuts every radius at the same angle (it is the *equiangular* spiral).

#### Step 6. Numbers

$k=5/4$: $\dot r=\frac{(3/4)\cdot10}{5/4}=6$ m/s, $\ r\dot\varphi=\frac{v_0}{k}=8$ m/s (check: $6^2+8^2=10^2$), $\ \tan\alpha=4/3$, $\ \alpha=53.13^\circ$.

## (b) Time law: $r(t)$, $\varphi(t)$ and the flight time [1.5 pts]

Integrate the results of (a) to obtain $r(t)$ and $\varphi(t)$, and check that they lie on the spiral. Compute the time needed to go from $r_1=20$ m to $r_2=50$ m and the angle turned.

### Hint

$\dot r$ is constant. For $\varphi$, integrate $\dot\varphi=v_0/(k\,r(t))$ with the substitution $u=r_0+\dot r\,\tau$.

### Checkpoint

- $r(t)=r_0+\dfrac{b\,v_0}{\sqrt{1+b^2}}\,t$, $\ \varphi(t)=\dfrac1b\ln\dfrac{r(t)}{r_0}$.
- $t_{12}=\dfrac{(r_2-r_1)\sqrt{1+b^2}}{b\,v_0}=5$ s; $\ \Delta\varphi=\dfrac{\ln(5/2)}{3/4}=1.2217$ rad $=70.00^\circ$.

### Solution

#### Step 1. Radial law

$\dot r=c$ with $c=bv_0/k$ constant. Integrating from $0$ to $t$ with Barrow's rule, $r(t)-r(0)=\int_0^tc\,d\tau=c\,t$:

$$r(t)=r_0+\frac{b\,v_0}{\sqrt{1+b^2}}\,t$$

#### Step 2. Angular law (quadrature)

$$\varphi(t)=\varphi(0)+\int_0^t\frac{v_0}{k\,(r_0+c\tau)}\,d\tau$$

Substitution $u=r_0+c\tau$, $du=c\,d\tau$; the limits $\tau=0\mapsto u=r_0$ and $\tau=t\mapsto u=r(t)$:

$$\varphi(t)=\frac{v_0}{k\,c}\int_{r_0}^{r(t)}\frac{du}{u}=\frac{v_0}{k\,c}\Big[\ln u\Big]_{r_0}^{r(t)}=\frac{v_0}{k\,c}\big(\ln r(t)-\ln r_0\big)=\frac1b\ln\frac{r(t)}{r_0}$$

since $\frac{v_0}{kc}=\frac{v_0}{k}\cdot\frac{k}{bv_0}=\frac1b$. Inverting, $r(t)=r_0e^{b\varphi(t)}$: the time law lies on the spiral, as it must.

#### Step 3. Flight time and angle turned

$r_2-r_1=c\,t_{12}$:

$$t_{12}=\frac{(r_2-r_1)\sqrt{1+b^2}}{b\,v_0}=\frac{30\cdot(5/4)}{(3/4)\cdot10}=5\ \text{s}$$

$$\Delta\varphi=\frac1b\ln\frac{r_2}{r_1}=\frac43\ln2.5=1.2217\ \text{rad}=70.00^\circ$$

## (c) Arc length and the intrinsic basis [1.5 pts]

Obtain the arc length $s(r)$ measured from $r_0$, and check it against $v_0\,t_{12}$. Write $\mathbf e_t$ and the principal normal $\mathbf e_n$ in the polar basis.

### Hint

$ds^2=dr^2+r^2d\varphi^2$ and, on the spiral, $d\varphi=dr/(b\,r)$. For $\mathbf e_n$ differentiate $\mathbf e_t$: its polar components are constant.

### Checkpoint

- $s(r)=\dfrac{\sqrt{1+b^2}}{b}\,(r-r_0)$; from 20 m to 50 m: $s=50$ m $=v_0t_{12}$.
- $\mathbf e_t=\dfrac{b\,\mathbf e_r+\mathbf e_\varphi}{\sqrt{1+b^2}}$, $\ \mathbf e_n=\dfrac{-\mathbf e_r+b\,\mathbf e_\varphi}{\sqrt{1+b^2}}$ (towards the concave side, to the left of the motion).

### Solution

#### Step 1. Arc length

From $\varphi(r)=\frac1b\ln\frac r{r_0}$, $\frac{d\varphi}{dr}=\frac1{br}$, so $r\,d\varphi=\frac{dr}{b}$ and

$$ds=\sqrt{dr^2+r^2d\varphi^2}=\sqrt{1+\frac1{b^2}}\,dr=\frac{\sqrt{1+b^2}}{b}\,dr$$

Integrating from $r_0$ to $r$ (Barrow):

$$s(r)=\int_{r_0}^{r}\frac{k}{b}\,dr'=\frac kb\Big[r'\Big]_{r_0}^{r}=\frac{\sqrt{1+b^2}}{b}\,(r-r_0)$$

From 20 m to 50 m: $s=\frac{5/4}{3/4}\cdot30=50$ m, equal to $v_0t_{12}=10\cdot5=50$ m, as it must at constant speed.

#### Step 2. Unit tangent

$\mathbf e_t=\mathbf v/v_0$ with the components of (a):

$$\mathbf e_t=\frac{\dot r}{v_0}\,\mathbf e_r+\frac{r\dot\varphi}{v_0}\,\mathbf e_\varphi=\frac{b\,\mathbf e_r+\mathbf e_\varphi}{\sqrt{1+b^2}}=\cos\alpha\,\mathbf e_r+\sin\alpha\,\mathbf e_\varphi$$

#### Step 3. Principal normal

The components of $\mathbf e_t$ are constant, so only the basis vectors change. With the product rule and $\dot{\mathbf e}_r=\dot\varphi\,\mathbf e_\varphi$, $\dot{\mathbf e}_\varphi=-\dot\varphi\,\mathbf e_r$:

$$\dot{\mathbf e}_t=\frac{b\,\dot\varphi\,\mathbf e_\varphi-\dot\varphi\,\mathbf e_r}{k}=\dot\varphi\,\frac{-\mathbf e_r+b\,\mathbf e_\varphi}{k}$$

By the chain rule $\frac{d\mathbf e_t}{ds}=\frac{\dot{\mathbf e}_t}{\dot s}$ with $\dot s=v_0$, and the principal normal is the unit vector of $d\mathbf e_t/ds$ (Notes §2.4). The vector $(-\mathbf e_r+b\,\mathbf e_\varphi)/k$ has modulus $\sqrt{1+b^2}/k=1$, so

$$\mathbf e_n=\frac{-\mathbf e_r+b\,\mathbf e_\varphi}{\sqrt{1+b^2}},\qquad \Big|\frac{d\mathbf e_t}{ds}\Big|=\frac{\dot\varphi}{v_0}$$

Check: $\mathbf e_t\cdot\mathbf e_n=(-b+b)/k^2=0$, and $\mathbf e_n$ is $\mathbf e_t$ turned $+90^\circ$ (to the left of the motion, towards the concave side and partly towards $O$).

## (d) Acceleration, radius of curvature [2.0 pts]

Compute the acceleration in polar components. Obtain the radius of curvature $\rho$ and show that $\mathbf a=\dfrac{v_0^2}{\rho}\,\mathbf e_n$. Numbers at $r=20$ m and at $r=50$ m.

### Hint

$a_r=\ddot r-r\dot\varphi^2$, $a_\varphi=r\ddot\varphi+2\dot r\dot\varphi$. Do not set $a_r=0$ because $\dot r$ is constant. The curvature is $|d\mathbf e_t/ds|$ from (c).

### Checkpoint

- $a_r=-\dfrac{v_0^2}{r(1+b^2)}$, $\ a_\varphi=\dfrac{b\,v_0^2}{r(1+b^2)}$, $\ \rho=r\sqrt{1+b^2}$, $\ |\mathbf a|=\dfrac{v_0^2}{r\sqrt{1+b^2}}$.
- At $r=20$ m: $\rho=25$ m, $a_r=-3.2$ m/s$^2$, $a_\varphi=2.4$ m/s$^2$, $|\mathbf a|=4$ m/s$^2$; at $r=50$ m: $|\mathbf a|=1.6$ m/s$^2$.

### Solution

#### Step 1. Polar acceleration

Differentiating $\mathbf v=\dot r\,\mathbf e_r+r\dot\varphi\,\mathbf e_\varphi$ with the product rule (Notes §2.6):

$$\mathbf a=(\ddot r-r\dot\varphi^2)\,\mathbf e_r+(r\ddot\varphi+2\dot r\dot\varphi)\,\mathbf e_\varphi$$

#### Step 2. The derivatives needed

$\ddot r=0$ because $\dot r$ is constant. From $\dot\varphi=\frac{v_0}{k}\,r^{-1}$, with the chain rule $\frac{d}{dt}r^{-1}=-r^{-2}\dot r$:

$$\ddot\varphi=-\frac{v_0}{k}\,\frac{\dot r}{r^2}=-\frac{\dot r\,\dot\varphi}{r}$$

#### Step 3. Components

$$a_r=0-r\dot\varphi^2=-r\,\frac{v_0^2}{r^2k^2}=-\frac{v_0^2}{r(1+b^2)}$$

$$a_\varphi=r\Big(-\frac{\dot r\dot\varphi}{r}\Big)+2\dot r\dot\varphi=\dot r\dot\varphi=\frac{bv_0}{k}\cdot\frac{v_0}{rk}=\frac{b\,v_0^2}{r(1+b^2)}$$

#### Step 4. Intrinsic form and radius of curvature

The curvature is $1/\rho=|d\mathbf e_t/ds|=\dot\varphi/v_0=\frac1{rk}$ (part (c)), so $\rho=r\sqrt{1+b^2}$. In the intrinsic basis (Notes §2.5) $\mathbf a=\dot v\,\mathbf e_t+\frac{v^2}{\rho}\,\mathbf e_n$ with $\dot v=0$:

$$\mathbf a=\frac{v_0^2}{r\sqrt{1+b^2}}\,\mathbf e_n=\frac{v_0^2}{r\sqrt{1+b^2}}\cdot\frac{-\mathbf e_r+b\,\mathbf e_\varphi}{\sqrt{1+b^2}}=-\frac{v_0^2}{r(1+b^2)}\,\mathbf e_r+\frac{b\,v_0^2}{r(1+b^2)}\,\mathbf e_\varphi$$

which coincides with Step 3: the two routes agree. Check: $\sqrt{a_r^2+a_\varphi^2}=\frac{v_0^2\sqrt{1+b^2}}{r(1+b^2)}=\frac{v_0^2}{\rho}$.

#### Step 5. Numbers

At $r=20$ m: $\rho=20\cdot\frac54=25$ m, $|\mathbf a|=\frac{100}{25}=4$ m/s$^2$, $a_r=-\frac{100}{20\cdot25/16}=-3.2$ m/s$^2$, $a_\varphi=\frac34\cdot3.2=2.4$ m/s$^2$ (check: $3.2^2+2.4^2=16$). At $r=50$ m: $\rho=62.5$ m and $|\mathbf a|=1.6$ m/s$^2$: the spiral opens up and the turn becomes gentler.

## (e) Force, torque and angular momentum about $O$ [1.5 pts]

Find the horizontal force $\mathbf F$ needed at $r=20$ m. Is it a central force about $O$? Compute the torque $\mathbf M_O$ and the angular momentum $\mathbf H_O(t)$, and verify the angular momentum theorem between $r_1$ and $r_2$.

### Hint

$\mathbf F=m\mathbf a$. A force is central about $O$ only if it is parallel to $\mathbf e_r$. $\mathbf H_O=m\,\mathbf r\times\mathbf v=m\,r^2\dot\varphi\,\mathbf k$ with $\mathbf k=\mathbf i\times\mathbf j$.

### Checkpoint

- At $r=20$ m: $F_r=-6.4$ N, $F_\varphi=4.8$ N, $|\mathbf F|=8$ N; it makes $\arctan b=36.87^\circ$ with $-\mathbf e_r$: **not central**.
- $\mathbf M_O=m\,r\,a_\varphi\,\mathbf k=\dfrac{m\,b\,v_0^2}{1+b^2}\,\mathbf k=96$ N m (constant); $\ \mathbf H_O=\dfrac{m\,r(t)\,v_0}{\sqrt{1+b^2}}\,\mathbf k$: 320 kg m$^2$/s at 20 m, 800 kg m$^2$/s at 50 m; $\Delta H_O=96\cdot5=480$ kg m$^2$/s.

### Solution

#### Step 1. The force

Newton's second law in the inertial frame, $\mathbf F=m\mathbf a$, with $m=2$ kg and the numbers of (d):

$$\mathbf F=2\,(-3.2\,\mathbf e_r+2.4\,\mathbf e_\varphi)=-6.4\,\mathbf e_r+4.8\,\mathbf e_\varphi\ \text{N},\qquad|\mathbf F|=8\ \text{N}$$

In general $\mathbf F=\frac{mv_0^2}{\rho}\mathbf e_n$. Since $\mathbf e_n\cdot(-\mathbf e_r)=1/k$, the angle $\gamma$ between $\mathbf F$ and $-\mathbf e_r$ has $\cos\gamma=1/\sqrt{1+b^2}$, i.e. $\tan\gamma=b$: $\gamma=\arctan(3/4)=36.87^\circ$. The force is **not** central: $F_\varphi\ne0$ at every point.

#### Step 2. Torque

$\mathbf M_O=\mathbf r\times\mathbf F=r\,\mathbf e_r\times(F_r\mathbf e_r+F_\varphi\mathbf e_\varphi)=r\,F_\varphi\,\mathbf k$ (since $\mathbf e_r\times\mathbf e_\varphi=\mathbf k$):

$$\mathbf M_O=m\,r\,a_\varphi\,\mathbf k=m\,r\,\frac{b\,v_0^2}{r(1+b^2)}\,\mathbf k=\frac{m\,b\,v_0^2}{1+b^2}\,\mathbf k=\frac{2\cdot0.75\cdot100}{1.5625}\,\mathbf k=96\ \mathbf k\ \text{N m}$$

constant along the whole flight, although $\mathbf F$ changes.

#### Step 3. Angular momentum

$\mathbf r\times\mathbf v=r\,\mathbf e_r\times(\dot r\,\mathbf e_r+r\dot\varphi\,\mathbf e_\varphi)=r^2\dot\varphi\,\mathbf k$, so with $\dot\varphi$ of (a):

$$\mathbf H_O=m\,r^2\dot\varphi\,\mathbf k=\frac{m\,r(t)\,v_0}{\sqrt{1+b^2}}\,\mathbf k$$

At $r=20$ m: $H_O=\frac{2\cdot20\cdot10}{1.25}=320$ kg m$^2$/s; at $r=50$ m: $800$ kg m$^2$/s.

#### Step 4. Angular momentum theorem

About the fixed point $O$, $\dot{\mathbf H}_O=\mathbf M_O$ (Notes §4.8). By the chain rule $\frac{d}{dt}H_O=\frac{mv_0}{k}\dot r=\frac{mv_0}{k}\cdot\frac{bv_0}{k}=\frac{m\,b\,v_0^2}{1+b^2}=M_O$. Integrating from $0$ to $t_{12}$ (Barrow): $H_O(t_{12})-H_O(0)=\int_0^{t_{12}}M_O\,dt=96\cdot5=480$ kg m$^2$/s, and indeed $800-320=480$. The angular momentum is **not** conserved, and the areal velocity $\frac12r^2\dot\varphi$ grows: Kepler's second law does not hold for this force.

## (f) Power, kinetic energy and the trap [1.5 pts]

Compute the power of $\mathbf F$ and the work it does between $r_1$ and $r_2$, and check the result with the kinetic energy theorem. A student argues: "the speed is constant, so the drone is in equilibrium and the net force is zero; and since $\mathbf F$ does no work, it must be a central (or conservative) force". Discuss.

### Hint

$P=\mathbf F\cdot\mathbf v$ with $\mathbf F\parallel\mathbf e_n$ and $\mathbf v\parallel\mathbf e_t$.

### Checkpoint

- $P=\mathbf F\cdot\mathbf v=\frac{mv_0^2}{\rho}\,v_0\,(\mathbf e_n\cdot\mathbf e_t)=0$; $W_{12}=0$; $E_{kin}=\tfrac12mv_0^2=100$ J at every instant.
- Constant **speed** is not constant **velocity**: $|\mathbf F|=mv_0^2/\rho\neq0$. Zero power only says $\mathbf F\perp\mathbf v$; the force is neither zero nor central ($\mathbf M_O\ne\mathbf0$).

### Solution

#### Step 1. Power and work

The power of $\mathbf F$ is $P=\mathbf F\cdot\mathbf v$ (Notes §4.5). With $\mathbf F=\frac{mv_0^2}{\rho}\mathbf e_n$ and $\mathbf v=v_0\mathbf e_t$:

$$P=\frac{m\,v_0^3}{\rho}\,(\mathbf e_n\cdot\mathbf e_t)=0$$

In polar components the same result is $m(a_r\dot r+a_\varphi r\dot\varphi)=m\frac{v_0^2}{rk^2}\big(-\frac{bv_0}{k}+b\,\frac{v_0}{k}\big)=0$. The work between $r_1$ and $r_2$ is $W_{12}=\int_0^{t_{12}}P\,dt=0$.

#### Step 2. Kinetic energy theorem

$\frac{d}{dt}\big(\tfrac12m\,\mathbf v\cdot\mathbf v\big)=m\,\mathbf a\cdot\mathbf v=P=0$, consistent with $|\mathbf v|=v_0$: $E_{kin}=\tfrac12\cdot2\cdot10^2=100$ J at every instant.

#### Step 3. The trap

- "Constant speed means zero force" confuses the speed $|\mathbf v|$ with the velocity vector. The direction of $\mathbf v$ turns with angular rate $\dot\varphi$ (since $\alpha$ is constant, $\mathbf e_t$ turns exactly as $\mathbf e_r$), so $\mathbf a=\frac{v_0^2}{\rho}\mathbf e_n\neq\mathbf0$: at 20 m the autopilot must supply 8 N.
- "No work, so central" is false: zero power only means $\mathbf F\perp\mathbf v$ at each instant. Here $\mathbf F$ is perpendicular to $\mathbf v$ but makes $36.87^\circ$ with the radius, so it has a moment about $O$ and $\mathbf H_O$ grows by 480 kg m$^2$/s.
- A force perpendicular to the velocity is not conservative in general either: being workless along **this** path says nothing about the work along other paths. What matters for the energy budget is that it does no work along the actual motion.

## Interpretation

- **Dimensional check:** $\dot r=bv_0/k$ and $r\dot\varphi$ are m/s; $\rho=rk$ is m; $a=v_0^2/\rho$ is m$^2$s$^{-2}$/m = m s$^{-2}$; $M_O=mbv_0^2/k^2$ is kg m$^2$s$^{-2}$ = N m; $H_O=mrv_0/k$ is kg m$^2$/s; $t_{12}=(r_2-r_1)k/(bv_0)$ is s.
- **Limiting cases:** $b\to0$ gives $r=r_0$, $\dot r=0$, $\alpha=90^\circ$, $\rho=r_0$, $a_\varphi=0$: uniform circular motion with a central force $-mv_0^2/r_0\,\mathbf e_r$ and $\mathbf H_O$ constant. $b\to\infty$ gives $\alpha\to0$: an almost radial straight flight with $\rho\to\infty$ and $\mathbf a\to\mathbf0$.
- **Flying inwards:** with $\varphi$ decreasing, $r$ decreases linearly and reaches $O$ after the finite time $r_0k/(bv_0)=10/3$ s and the finite length $r_0k/b=100/3$ m, while $\varphi=\frac1b\ln(r/r_0)\to-\infty$: infinitely many turns in a finite time, with $\dot\varphi$ and $|\mathbf a|$ growing without bound. A real autopilot cannot follow the spiral to the end.
- **Common mistakes in the exam:** (1) setting $a_r=0$ because $\dot r$ is constant (the centripetal term $-r\dot\varphi^2$ remains); (2) taking $\dot\varphi$ constant and dropping $r\ddot\varphi$ in $a_\varphi$; (3) writing $\rho=r$ as for a circle; (4) concluding from $P=0$ that $\mathbf F=\mathbf0$ or that $\mathbf H_O$ is conserved.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
