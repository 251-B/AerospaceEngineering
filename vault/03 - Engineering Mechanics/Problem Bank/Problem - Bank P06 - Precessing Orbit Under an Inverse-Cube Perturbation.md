---
materia: Engineering Mechanics
tema: "Unit 4: central forces, Binet equation and apsidal precession"
bank_id: P06
title: "Precessing orbit under an attractive inverse-cube perturbation: Binet equation, circular orbits and apsidal advance"
category: midterm_problem
archetype: central-force
level: standard
unit: 4
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers; not an official exercise. Verified with scripts/mechanics/p06.py"
tags:
  - problem-bank
  - midterm-1
  - central-force
  - binet-equation
  - effective-potential
  - precession
---

# Bank P06 — Precessing orbit under an inverse-cube perturbation

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §4.8 (angular momentum and torque), §4.8.1 (central force motion), §4.5 (conservation of mechanical energy), §4.6 (equilibrium) and §8.3 to §8.4 (polar equations, Binet equation and conic orbits). Every equation and number was checked with SymPy and with a numerical integration of the orbit.

## Statement

A particle $P$ of mass $m$ moves about a fixed centre $O$ (inertial frame $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$) under the single force

$$\mathbf F=-\Big(\frac{m\mu}{r^2}+\frac{m\varepsilon}{r^3}\Big)\mathbf e_r$$

where $r=|\mathbf{OP}|$, $\mathbf e_r=\mathbf{OP}/r$, $\mu>0$ is the gravitational parameter of the centre and $\varepsilon>0$ (units m$^4$ s$^{-2}$) measures a small attractive perturbation (a model perturbation added to the Newtonian attraction). Once the motion is shown to be planar, use polar coordinates $(r,\theta)$ in the plane of the orbit, with $\theta$ measured counter-clockwise from a fixed reference line through $O$, the unit vectors $\mathbf e_r$, $\mathbf e_\theta$ ($\mathbf e_\theta$ points towards increasing $\theta$) and $h=r^2\dot\theta$.

![[attachments/EM-M1/p06-precessing-orbit.svg]]

A perigee is a point of minimum $r$ and an apogee a point of maximum $r$. In the numerical part the reference line $\theta=0$ passes through a perigee.

## Setup

- Data: $m$, $\mu$, $\varepsilon$ and the initial conditions. Numerical case (part (f)): $\mu=4.0\times10^{14}$ m$^3$ s$^{-2}$; at $t=0$ the particle is at the perigee $r_p=8.0\times10^{6}$ m with the speed $v_p=1.0\times10^{4}$ m/s perpendicular to $\mathbf{OP}$; $\varepsilon=0.19\,h^2$.
- Hypotheses: point particle, $O$ fixed and $S_0$ inertial, no other force.
- Frames: $S_0$ (inertial, Cartesian) and the polar basis $\{\mathbf e_r,\mathbf e_\theta,\mathbf k\}$ attached to $P$, with $\mathbf e_r=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j$ and $\mathbf e_\theta=-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j$ ($\mathbf i$, $\mathbf j$ in the plane of the orbit, $\mathbf k$ along $\mathbf H_O$, see (a)).
- Change of basis:

$$\begin{pmatrix}\mathbf e_r\ \mathbf e_\theta\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\theta&\sin\theta&0\ -\sin\theta&\cos\theta&0\ 0&0&1\end{pmatrix}$$

with rows of unit length ($\cos^2\theta+\sin^2\theta=1$) and mutually orthogonal ($-\cos\theta\sin\theta+\sin\theta\cos\theta=0$), so $[R][R]^T=I$, and $\det[R]=\cos^2\theta+\sin^2\theta=+1$: the polar basis is right-handed, $\mathbf e_r\times\mathbf e_\theta=\mathbf k$.

## (a) Planar motion and conservation of angular momentum [1.5 pts]

Show that the angular momentum $\mathbf H_O$ of $P$ about $O$ is constant, that the motion takes place in a fixed plane through $O$, and that $h=r^2\dot\theta$ is a constant of the motion. How many degrees of freedom remain?

### Hint

Compute the torque of $\mathbf F$ about $O$ and use the angular momentum theorem $\dot{\mathbf H}_O=\mathbf M_O$. The position vector is always orthogonal to a constant vector.

### Checkpoint

- $\mathbf M_O=\mathbf r\times\mathbf F=\mathbf 0$, so $\mathbf H_O=m\,\mathbf r\times\mathbf v$ is constant.
- $\mathbf r\cdot\mathbf H_O=0$: $P$ stays in the plane through $O$ orthogonal to $\mathbf H_O$; in it $\mathbf H_O=mr^2\dot\theta\,\mathbf k$, so $h=r^2\dot\theta=$ const.
- 2 degrees of freedom, $(r,\theta)$, with one first integral ($h$).

### Solution

#### Step 1. Torque of a central force

$\mathbf F$ is parallel to $\mathbf r=r\,\mathbf e_r$, so

$$\mathbf M_O=\mathbf r\times\mathbf F=-\Big(\frac{m\mu}{r^2}+\frac{m\varepsilon}{r^3}\Big)\,r\,(\mathbf e_r\times\mathbf e_r)=\mathbf 0$$

By the angular momentum theorem about a fixed point (Notes §4.8), $\dot{\mathbf H}_O=\mathbf M_O=\mathbf 0$, so $\mathbf H_O=m\,\mathbf r\times\mathbf v$ is a constant vector.

#### Step 2. Plane of the motion

For every $t$, $\mathbf r\cdot\mathbf H_O=m\,\mathbf r\cdot(\mathbf r\times\mathbf v)=0$ (a triple product with a repeated vector). The position is always orthogonal to the fixed vector $\mathbf H_O$: $P$ moves in the fixed plane through $O$ orthogonal to $\mathbf H_O$ (if $\mathbf H_O=\mathbf 0$ the motion is radial, along a fixed line). Choose $\mathbf k$ along $\mathbf H_O$ (Notes §4.8.1).

#### Step 3. The constant $h$

In the plane, $\mathbf r=r\,\mathbf e_r$ and, with $\dot{\mathbf e}_r=\dot\theta\,\mathbf e_\theta$ (chain rule on $\mathbf e_r(\theta(t))$),

$$\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta,\qquad \mathbf H_O=m\,r\,\mathbf e_r\times\big(\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta\big)=mr^2\dot\theta\,\mathbf k$$

So $h=|\mathbf H_O|/m=r^2\dot\theta$ is constant (twice the areal velocity). The particle has 3 degrees of freedom in space; the plane is fixed by the initial conditions, and in it 2 remain, $r$ and $\theta$, linked by the first integral $h$.

## (b) Equations of motion and energy [1.5 pts]

Write the equations of motion in polar components. Show that $\mathbf F$ is conservative, find its potential energy, and write the energy integral as a one-dimensional problem in $r$ with an effective potential $U_{eff}(r)$.

### Hint

Use $\mathbf a=(\ddot r-r\dot\theta^2)\,\mathbf e_r+\frac1r\frac{d}{dt}(r^2\dot\theta)\,\mathbf e_\theta$. A radial force $f(r)\,\mathbf e_r$ has the potential $V=-\int f\,dr$. Replace $\dot\theta$ by $h/r^2$.

### Checkpoint

- $\ddot r-r\dot\theta^2=-\dfrac{\mu}{r^2}-\dfrac{\varepsilon}{r^3}$ and $\dfrac{d}{dt}(r^2\dot\theta)=0$.
- $V=-\dfrac{m\mu}{r}-\dfrac{m\varepsilon}{2r^2}$.
- $\dfrac Em=\tfrac12\dot r^2+U_{eff}(r)$, $\ U_{eff}=\dfrac{h^2-\varepsilon}{2r^2}-\dfrac{\mu}{r}$.

### Solution

#### Step 1. Acceleration in polar components

Differentiating $\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta$ with the product rule and $\dot{\mathbf e}_r=\dot\theta\,\mathbf e_\theta$, $\dot{\mathbf e}_\theta=-\dot\theta\,\mathbf e_r$:

$$\mathbf a=\ddot r\,\mathbf e_r+\dot r\dot\theta\,\mathbf e_\theta+(\dot r\dot\theta+r\ddot\theta)\,\mathbf e_\theta-r\dot\theta^2\,\mathbf e_r=(\ddot r-r\dot\theta^2)\,\mathbf e_r+(2\dot r\dot\theta+r\ddot\theta)\,\mathbf e_\theta$$

and $2\dot r\dot\theta+r\ddot\theta=\frac1r\frac{d}{dt}(r^2\dot\theta)$ (product rule: $\frac{d}{dt}(r^2\dot\theta)=2r\dot r\dot\theta+r^2\ddot\theta$).

#### Step 2. Newton's second law

$m\mathbf a=\mathbf F$ projected on $\mathbf e_r$ and $\mathbf e_\theta$ (Notes §8.3):

$$\ddot r-r\dot\theta^2=-\frac{\mu}{r^2}-\frac{\varepsilon}{r^3},\qquad \frac1r\frac{d}{dt}(r^2\dot\theta)=0$$

The second equation is the conservation of $h$ of part (a).

#### Step 3. Potential energy

$\mathbf F=f(r)\,\mathbf e_r$ with $f(r)=-m\mu/r^2-m\varepsilon/r^3$ depends only on $r$, so $\mathbf F=-\nabla V$ with $V'(r)=-f(r)$ (Notes §4.4). Choosing $V\to0$ as $r\to\infty$, $V(r)=-\displaystyle\int_\infty^rf(r')\,dr'$. An antiderivative of $-f(r')=\dfrac{m\mu}{r'^2}+\dfrac{m\varepsilon}{r'^3}$ is $G(r')=-\dfrac{m\mu}{r'}-\dfrac{m\varepsilon}{2r'^2}$, and Barrow's rule with $G(r')\to0$ as $r'\to\infty$ gives

$$V(r)=\int_\infty^r\Big(\frac{m\mu}{r'^2}+\frac{m\varepsilon}{r'^3}\Big)dr'=\Big[-\frac{m\mu}{r'}-\frac{m\varepsilon}{2r'^2}\Big]_\infty^r=\Big(-\frac{m\mu}{r}-\frac{m\varepsilon}{2r^2}\Big)-0=-\frac{m\mu}{r}-\frac{m\varepsilon}{2r^2}$$
Check: $-V'(r)=-\frac{m\mu}{r^2}-\frac{m\varepsilon}{r^3}=f(r)$.

#### Step 4. Energy integral and effective potential

The only force is conservative, so $E=\tfrac12m|\mathbf v|^2+V$ is constant (Notes §4.5), with $|\mathbf v|^2=\dot r^2+r^2\dot\theta^2=\dot r^2+h^2/r^2$:

$$\frac Em=\tfrac12\dot r^2+\frac{h^2}{2r^2}-\frac{\mu}{r}-\frac{\varepsilon}{2r^2}=\tfrac12\dot r^2+U_{eff}(r),\qquad U_{eff}(r)=\frac{h^2-\varepsilon}{2r^2}-\frac{\mu}{r}$$

The perturbation enters exactly as a reduction of the centrifugal barrier, $h^2\to h^2-\varepsilon$.

## (c) Circular orbit and its stability [1.5 pts]

For a given $h$, find the radius $r_c$ and the speed of the circular orbit. Under what condition does it exist? Is it stable against small radial perturbations? Compare the frequency of the small radial oscillations with the angular rate on the circle.

### Hint

A circular orbit is an equilibrium of the radial problem: $U_{eff}'(r_c)=0$. Stability: sign of $U_{eff}''(r_c)$ (Notes §4.6).

### Checkpoint

- $r_c=\dfrac{h^2-\varepsilon}{\mu}$, it exists only if $h^2>\varepsilon$; $v_c^2=\dfrac{h^2}{r_c^2}=\dfrac{\mu}{r_c}+\dfrac{\varepsilon}{r_c^2}$.
- $U_{eff}''(r_c)=\mu/r_c^3>0$: stable. $\omega_r^2=\mu/r_c^3$, $\ \omega_r/\dot\theta_c=\sqrt{1-\varepsilon/h^2}<1$.

### Solution

#### Step 1. Equilibrium of the radial problem

$$U_{eff}'(r)=-\frac{h^2-\varepsilon}{r^3}+\frac{\mu}{r^2}=0\ \Longrightarrow\ r_c=\frac{h^2-\varepsilon}{\mu}$$

A positive radius requires $h^2>\varepsilon$. If $h^2\le\varepsilon$ the barrier term is non-positive, $U_{eff}$ decreases monotonically towards $r\to0$, and the particle with $\dot r<0$ falls into the centre: no circular orbit exists.

#### Step 2. Speed

On the circle $\dot r=0$, so $v_c=r_c\dot\theta=h/r_c$. Equivalently, the radial equation with $\ddot r=0$ gives $r_c\dot\theta^2=\mu/r_c^2+\varepsilon/r_c^3$, i.e. $v_c^2=\mu/r_c+\varepsilon/r_c^2$; with $h^2=\mu r_c+\varepsilon$ both forms agree.

#### Step 3. Stability

$$U_{eff}''(r)=\frac{3(h^2-\varepsilon)}{r^4}-\frac{2\mu}{r^3}\ \Longrightarrow\ U_{eff}''(r_c)=\frac{3\mu r_c}{r_c^4}-\frac{2\mu}{r_c^3}=\frac{\mu}{r_c^3}>0$$

$r_c$ is a minimum of $U_{eff}$: the circular orbit is stable. Linearising $\ddot r=-U_{eff}'(r)$ about $r_c$ with $\rho=r-r_c$ gives $\ddot\rho+U_{eff}''(r_c)\rho=0$, so the radial oscillations have $\omega_r^2=\mu/r_c^3$.

#### Step 4. Radial frequency versus angular rate

On the circle $\dot\theta_c=h/r_c^2$, so $\dot\theta_c^2=h^2/r_c^4$ and

$$\frac{\omega_r^2}{\dot\theta_c^2}=\frac{\mu r_c}{h^2}=\frac{h^2-\varepsilon}{h^2}=1-\frac{\varepsilon}{h^2}$$

For $\varepsilon=0$ (Kepler) the ratio is 1: $r$ returns to its minimum exactly once per turn and the slightly perturbed orbit closes (an ellipse). For $\varepsilon>0$ the radial oscillation is slower than the rotation, so the minimum of $r$ is reached **after** more than one turn: the perigee advances. Part (e) makes this exact for any amplitude.

## (d) Binet equation and the orbit [2.0 pts]

With $u=1/r$ and $\theta$ as the independent variable, derive the Binet equation of this force field, solve it with the perigee at $\theta=0$, and give the perigee and apogee radii.

### Hint

$\dot\theta=hu^2$ turns time derivatives into $\theta$ derivatives: $\dot r=-h\,u'$ and $\ddot r=-h^2u^2u''$ (primes are $d/d\theta$). Write $k^2=1-\varepsilon/h^2$ (notation: this scalar $k$ is a dimensionless frequency ratio, unrelated to the unit vector $\mathbf k$).

### Checkpoint

- $u''+\Big(1-\dfrac{\varepsilon}{h^2}\Big)u=\dfrac{\mu}{h^2}$.
- $u=\dfrac{\mu}{h^2k^2}\big(1+e\cos k\theta\big)$, i.e. $r=\dfrac{r_c}{1+e\cos k\theta}$ with $r_c=\dfrac{h^2-\varepsilon}{\mu}=\dfrac{h^2k^2}{\mu}$.
- $r_p=\dfrac{r_c}{1+e}$ at $\theta=0$; $r_a=\dfrac{r_c}{1-e}$ at $k\theta=\pi$ (bounded orbit if $0\le e<1$).

### Solution

#### Step 1. First derivative

$r=1/u$ with $u=u(\theta(t))$. Chain rule:

$$\dot r=\frac{d}{dt}\Big(\frac1u\Big)=-\frac{1}{u^2}\frac{du}{d\theta}\dot\theta=-\frac{1}{u^2}u'\,hu^2=-h\,u'$$

using $\dot\theta=h/r^2=hu^2$.

#### Step 2. Second derivative

$h$ is constant, so again by the chain rule

$$\ddot r=\frac{d}{dt}(-h\,u')=-h\frac{du'}{d\theta}\dot\theta=-h\,u''\,hu^2=-h^2u^2u''$$

#### Step 3. Radial equation in $u$

Substitute $\ddot r$, $r\dot\theta^2=\frac1u\,h^2u^4=h^2u^3$, $\mu/r^2=\mu u^2$ and $\varepsilon/r^3=\varepsilon u^3$ in the radial equation of (b):

$$-h^2u^2u''-h^2u^3=-\mu u^2-\varepsilon u^3$$

Dividing by $-h^2u^2$ (Notes §8.3, Eq. 8.12 with the extra term):

$$u''+\Big(1-\frac{\varepsilon}{h^2}\Big)u=\frac{\mu}{h^2}$$

#### Step 4. Solution

With the scalar $k^2=1-\varepsilon/h^2>0$ (not the unit vector $\mathbf k$; the condition $h^2>\varepsilon$ of (c)), this is a forced harmonic oscillator in $\theta$ with "frequency" $k$. A particular solution is the constant $u_0=\mu/(h^2k^2)$; the homogeneous solution is $C\cos(k\theta-\theta_0)$. Choosing $\theta=0$ at a perigee (maximum of $u$) gives $\theta_0=0$ and $C\ge0$; write $C=u_0e$:

$$u=\frac{\mu}{h^2k^2}\big(1+e\cos k\theta\big),\qquad r=\frac{r_c}{1+e\cos k\theta},\qquad r_c=\frac{h^2k^2}{\mu}=\frac{h^2-\varepsilon}{\mu}$$

Check: $u''=-k^2u_0e\cos k\theta$ and $u''+k^2u=k^2u_0=\mu/h^2$.

#### Step 5. Apsides

$r$ is minimum where $\cos k\theta=1$ ($\theta=0$) and maximum where $\cos k\theta=-1$ ($k\theta=\pi$):

$$r_p=\frac{r_c}{1+e},\qquad r_a=\frac{r_c}{1-e}\quad(0\le e<1)$$

The shape looks like a conic with semi-parameter $r_c$, but the angle that appears is $k\theta$, not $\theta$: the apogee is reached at $\theta=\pi/k>\pi$.

## (e) Apsidal precession [1.5 pts]

Find the angle swept between two consecutive perigees and the advance $\Delta\phi$ of the perigee per radial cycle; give its first-order form for $\varepsilon\ll h^2$. Is the orbit closed? Is the time between two perigees the time the particle needs to turn $360^\circ$?

### Hint

Consecutive perigees: $k\theta$ grows by $2\pi$. For the time, note that the radial equation with $h^2-\varepsilon$ in place of $h^2$ is exactly Kepler's radial equation.

### Checkpoint

- Angle between perigees $2\pi/k$; $\ \Delta\phi=2\pi\Big(\dfrac{1}{\sqrt{1-\varepsilon/h^2}}-1\Big)\approx\dfrac{\pi\varepsilon}{h^2}$.
- Closed only if $k$ is rational; for irrational $k$ the orbit fills the annulus $r_p\le r\le r_a$ (a rosette).
- Time between perigees: the radial period $T_r=2\pi\sqrt{a^3/\mu}$, $2a=r_p+r_a$; in that time $\theta$ advances $2\pi/k$, **not** $2\pi$.

### Solution

#### Step 1. Angle between perigees

Perigees are at $\cos k\theta=1$, i.e. $k\theta=0,2\pi,4\pi,\dots$ Two consecutive ones are separated by $\theta=2\pi/k$, and since $k<1$ this is more than one turn. The advance per radial cycle is

$$\Delta\phi=\frac{2\pi}{k}-2\pi=2\pi\Big(\frac{1}{\sqrt{1-\varepsilon/h^2}}-1\Big)$$

positive: the perigee advances in the sense of the motion.

#### Step 2. Small perturbation

With $x=\varepsilon/h^2\ll1$ and the binomial series $(1-x)^{-1/2}=1+\tfrac12x+O(x^2)$:

$$\Delta\phi=2\pi\Big(\tfrac12x+O(x^2)\Big)\approx\frac{\pi\varepsilon}{h^2}$$

#### Step 3. Closed or not

The orbit closes if after $q$ radial cycles the particle has made an integer number $p$ of turns: $q\,(2\pi/k)=2\pi p$, i.e. $k=q/p$ rational. Otherwise the perigee directions never repeat and the trajectory densely fills the annulus between $r_p$ and $r_a$.

#### Step 4. Time between perigees (the trap)

Substituting $\dot\theta=h/r^2$ in the radial equation of (b):

$$\ddot r=\frac{h^2}{r^3}-\frac{\mu}{r^2}-\frac{\varepsilon}{r^3}=\frac{\tilde h^2}{r^3}-\frac{\mu}{r^2},\qquad \tilde h^2=h^2-\varepsilon$$

This is the radial equation of a Kepler orbit with angular momentum $\tilde h$ and the same $r_p$, $r_a$, so $r(t)$ is periodic with the Kepler period of semi-major axis $a=(r_p+r_a)/2$ (Notes §8.4, Eq. 8.18):

$$T_r=2\pi\sqrt{\frac{a^3}{\mu}}$$

During $T_r$ the angle advances by $2\pi/k$, not $2\pi$: $\dot\theta=h/r^2=(h/\tilde h)\,(\tilde h/r^2)$ and $h/\tilde h=1/k$. The time to turn $360^\circ$ and the time between perigees are different quantities; equating them is the classic error. The energy also matches: at $r_p$, $\frac Em=U_{eff}(r_p)=-\frac{\mu}{2a}$.

## (f) Numerical case [2.0 pts]

With the data of the Setup ($\mu=4.0\times10^{14}$ m$^3$ s$^{-2}$, $r_p=8.0\times10^6$ m, $v_p=1.0\times10^4$ m/s perpendicular to $\mathbf{OP}$, $\varepsilon=0.19\,h^2$), compute $h$, $\varepsilon$, $k$, $r_c$, $e$, $r_a$, $E/m$, the apsidal advance (exact and first-order), and the time between two perigees. Comment on the value of $v_p$.

### Hint

$h=r_pv_p$ because the velocity is perpendicular to $\mathbf{OP}$ at the perigee. Then $e=r_c/r_p-1$.

### Checkpoint

- $h=8.0\times10^{10}$ m$^2$/s, $\varepsilon=1.216\times10^{21}$ m$^4$ s$^{-2}$, $k=0.9$.
- $r_c=1.296\times10^{7}$ m, $e=0.62$, $r_a=3.411\times10^{7}$ m, $a=2.105\times10^7$ m, $E/m=-9.50\times10^{6}$ J/kg.
- $\Delta\phi=40^\circ$ exactly ($2\pi/9$); first-order estimate $34.2^\circ$; apogee at $\theta=200^\circ$; $T_r=3.035\times10^4$ s.

### Solution

#### Step 1. Constants of the motion

$h=r_pv_p=8.0\times10^6\times1.0\times10^4=8.0\times10^{10}$ m$^2$/s, $h^2=6.4\times10^{21}$ m$^4$ s$^{-2}$, $\varepsilon=0.19\,h^2=1.216\times10^{21}$ m$^4$ s$^{-2}$ and $k=\sqrt{1-0.19}=\sqrt{0.81}=0.9$.

#### Step 2. Orbit

$$r_c=\frac{h^2-\varepsilon}{\mu}=\frac{0.81\times6.4\times10^{21}}{4.0\times10^{14}}=1.296\times10^{7}\ \text{m}$$

At $\theta=0$, $r=r_p$: $r_p=r_c/(1+e)\Rightarrow e=r_c/r_p-1=1.62-1=0.62$. Then $r_a=r_c/(1-e)=1.296\times10^7/0.38=3.411\times10^{7}$ m and $a=(r_p+r_a)/2=2.105\times10^{7}$ m.

#### Step 3. Energy

$$\frac Em=\frac{v_p^2}{2}-\frac{\mu}{r_p}-\frac{\varepsilon}{2r_p^2}=5.0\times10^{7}-5.0\times10^{7}-\frac{1.216\times10^{21}}{1.28\times10^{14}}=-9.50\times10^{6}\ \text{J/kg}$$

in agreement with $-\mu/(2a)=-4.0\times10^{14}/(4.211\times10^{7})=-9.50\times10^{6}$ J/kg. Note that $\tfrac12v_p^2=\mu/r_p$: $v_p$ is exactly the **escape speed** of the unperturbed problem. Without the perturbation the orbit would be a parabola; the extra attraction makes it bound.

#### Step 4. Precession and times

$$\Delta\phi=2\pi\Big(\frac{1}{0.9}-1\Big)=\frac{2\pi}{9}=40^\circ,\qquad \frac{\pi\varepsilon}{h^2}=0.19\,\pi=0.597\ \text{rad}=34.2^\circ$$

The first-order formula underestimates by 15 %: $\varepsilon/h^2=0.19$ is not small. The apogee is at $\theta=\pi/k=200^\circ$ and the next perigee at $\theta=400^\circ$. Since $k=9/10$, the orbit closes after 9 radial cycles and 10 turns.

$$T_r=2\pi\sqrt{\frac{(2.105\times10^{7})^3}{4.0\times10^{14}}}=3.035\times10^{4}\ \text{s}\approx8.43\ \text{h}$$

A numerical integration of the equations of (b) from the perigee confirms that $r$ is minimum again after $3.035\times10^4$ s with $\theta=400.0^\circ$.

## Interpretation

- **Dimensional check:** $\mu/r^2$ and $\varepsilon/r^3$ are accelerations (m$^3$ s$^{-2}$/m$^2$ and m$^4$ s$^{-2}$/m$^3$); $\varepsilon/h^2$ is dimensionless (m$^4$ s$^{-2}$ over m$^4$ s$^{-2}$), so $k$ and $\Delta\phi$ are pure numbers; $r_c=(h^2-\varepsilon)/\mu$ has m$^4$ s$^{-2}$/(m$^3$ s$^{-2}$) = m; $\sqrt{a^3/\mu}$ has s.
- **Limits:** $\varepsilon\to0$ gives $k=1$, $\Delta\phi=0$, the conic $r=(h^2/\mu)/(1+e\cos\theta)$ of Notes Eq. 8.14 and $T_r$ equal to the orbital period. $\varepsilon\to h^2$ gives $k\to0$: the barrier disappears, $\Delta\phi\to\infty$ and $r_c\to0$ (the particle spirals in).
- **Common mistakes in the exam:** (1) dropping the $\varepsilon u^3$ term when changing to $u$, or writing it on the wrong side, which changes the sign of the precession; (2) treating the orbit as a closed ellipse with $\theta$ in place of $k\theta$ (apogee at $180^\circ$); (3) taking the time between perigees as the time for one turn, or dividing $\Delta\phi$ by the period of a Kepler orbit with $h$ instead of $\tilde h$; (4) using the first-order $\pi\varepsilon/h^2$ when $\varepsilon/h^2$ is not small.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
