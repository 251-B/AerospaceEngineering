---
materia: Engineering Mechanics
tema: "Unit 4: Kepler's problem, vis-viva equation and impulsive manoeuvres"
bank_id: P07
title: "Insertion orbit and circularisation impulse: conic from the energy, apsides, apogee burn and time of flight"
category: midterm_problem
archetype: central-force
level: standard
unit: 4
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers; not an official exercise. Verified with scripts/mechanics/p07.py"
tags:
  - problem-bank
  - midterm-1
  - central-force
  - kepler-problem
  - vis-viva
  - orbital-manoeuvre
---

# Bank P07 — Insertion orbit and circularisation impulse

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §4.8.1 (central force motion), §8.3 and §8.4 (dynamics, conic orbits, Kepler's third law) and §8.5 (vis-viva equation). The time of flight of part (e) uses Kepler's equation, which is an **extension** beyond the Notes and is derived here. Every equation and number was checked with SymPy and with a numerical quadrature.

## Statement

A probe $P$ of mass $m$ moves in the gravitational field of a planet of centre $O$, radius $R$ and gravitational parameter $\mu$: the only force is $\mathbf F=-\dfrac{m\mu}{r^2}\mathbf e_r$, with $r=|\mathbf{OP}|$, $\mathbf e_r=\mathbf{OP}/r$; $O$ is fixed and the frame $S_0$ attached to it is inertial. At $t=0$ the probe is at the distance $r_0$ from $O$ and its velocity $\mathbf v_0$ has the magnitude

$$v_0=\sqrt{\mu/r_0}$$

(the local circular speed) and makes the **flight-path angle** $\gamma=30^\circ$ with the local horizontal, pointing away from the planet. Use polar coordinates $(r,\theta)$ in the orbital plane, with $\theta$ (the true anomaly) measured from the perigee $\Pi$ of the conic in the sense of the motion ($\Pi$ is a virtual point: with the data below it lies inside the planet, so the probe never reaches it; the trajectory arc starts at the surface $r=R$), the unit vectors $\mathbf e_r$, $\mathbf e_\theta$ and $h=r^2\dot\theta>0$. The local horizontal at $P$ is the direction of $\mathbf e_\theta$, so $\mathbf v_0=v_0(\sin\gamma\,\mathbf e_r+\cos\gamma\,\mathbf e_\theta)$.

![[attachments/EM-M1/p07-insertion-orbit.svg]]

When the probe reaches the apogee $A$, its engine fires a short **tangential** impulse $\Delta\mathbf v$ that puts it on the circular orbit of radius $r_a=|\mathbf{OA}|$.

## Setup

- Data: $\mu$, $r_0$, $v_0=\sqrt{\mu/r_0}$, $\gamma=30^\circ$. Numerical part (f): $\mu=4.0\times10^{14}$ m$^3$ s$^{-2}$, $r_0=1.0\times10^{7}$ m, $R=6.0\times10^{6}$ m.
- Hypotheses: point particle; planet's field spherically symmetric; no drag; the impulse is instantaneous (the position does not change during the burn) and the mass of propellant is irrelevant for the kinematics.
- Frames: $S_0=\{O;\mathbf i,\mathbf j,\mathbf k\}$ with $\mathbf i$ towards $\Pi$, $\mathbf j$ in the orbital plane and $\mathbf k$ along $\mathbf H_O$; polar basis $\mathbf e_r=\cos\theta\,\mathbf i+\sin\theta\,\mathbf j$, $\mathbf e_\theta=-\sin\theta\,\mathbf i+\cos\theta\,\mathbf j$. Change of basis:

$$\begin{pmatrix}\mathbf e_r\ \mathbf e_\theta\ \mathbf k\end{pmatrix}=[R]\begin{pmatrix}\mathbf i\ \mathbf j\ \mathbf k\end{pmatrix},\qquad [R]=\begin{pmatrix}\cos\theta&\sin\theta&0\ -\sin\theta&\cos\theta&0\ 0&0&1\end{pmatrix}$$

with $[R][R]^T=I$ (rows of length $\cos^2\theta+\sin^2\theta=1$, rows 1 and 2 orthogonal: $-\cos\theta\sin\theta+\sin\theta\cos\theta=0$) and $\det[R]=\cos^2\theta+\sin^2\theta=+1$, so $\mathbf e_r\times\mathbf e_\theta=\mathbf k$.
- Results from Notes §8.4 used: orbit $r=p/(1+e\cos\theta)$ with $p=h^2/\mu$ (Eq. 8.14), $p=a(1-e^2)$ (Eq. 8.16), $r_p=a(1-e)$, $r_a=a(1+e)$, period $\tau=2\pi\sqrt{a^3/\mu}$ (Eq. 8.18); vis-viva $v^2=\mu(2/r-1/a)$ (Notes §8.5).

## (a) Conserved quantities and type of conic [1.5 pts]

Explain why $h$ and the energy per unit mass $E/m$ are constant. Compute them from the initial conditions and decide the type of conic and its semi-major axis $a$.

### Hint

Only $\mathbf e_\theta$ components of $\mathbf v$ contribute to $h=|\mathbf r\times\mathbf v|$. The sign of $E$ classifies the conic.

### Checkpoint

- $h=r_0v_0\cos\gamma=\tfrac{\sqrt3}{2}\sqrt{\mu r_0}$, $\ h^2=\tfrac34\mu r_0$.
- $E/m=\tfrac12v_0^2-\mu/r_0=-\dfrac{\mu}{2r_0}<0$: ellipse, $a=-\dfrac{\mu}{2E/m}=r_0$.

### Solution

#### Step 1. Why they are conserved

$\mathbf F$ is central, so its torque about $O$ is $\mathbf r\times\mathbf F=\mathbf 0$ and $\mathbf H_O$ is constant (Notes §4.8); the motion is planar and $h=r^2\dot\theta$ is constant (Notes §4.8.1). $\mathbf F=-\nabla V$ with $V=-m\mu/r$, and it is the only force, so the mechanical energy $E=\tfrac12mv^2-m\mu/r$ is constant (Notes §4.5).

#### Step 2. Angular momentum

With $\mathbf r=r_0\,\mathbf e_r$ and $\mathbf v_0=v_0(\sin\gamma\,\mathbf e_r+\cos\gamma\,\mathbf e_\theta)$:

$$\mathbf r\times\mathbf v_0=r_0v_0\cos\gamma\,(\mathbf e_r\times\mathbf e_\theta)=r_0v_0\cos\gamma\,\mathbf k\ \Longrightarrow\ h=r_0\sqrt{\frac{\mu}{r_0}}\,\frac{\sqrt3}{2}=\frac{\sqrt3}{2}\sqrt{\mu r_0}$$

#### Step 3. Energy and conic

$$\frac Em=\frac12\,\frac{\mu}{r_0}-\frac{\mu}{r_0}=-\frac{\mu}{2r_0}<0$$

A negative energy means a bounded orbit: an **ellipse**. The vis-viva equation (Notes §8.5) gives $E/m=-\mu/(2a)$, so $a=r_0$. Note the trap: the probe has exactly the circular speed of its radius, yet the orbit is not a circle, because the velocity is not horizontal; the speed fixes $a$ only, the direction fixes the shape.

## (b) Shape of the orbit and apsides [2.0 pts]

Find the semi-latus rectum $p$, the eccentricity $e$ and the perigee and apogee radii $r_p$, $r_a$. Verify the apsides independently from the energy equation.

### Hint

$p=h^2/\mu$ and $p=a(1-e^2)$. At an apsis $\dot r=0$, so the energy equation is an equation for $r$ alone.

### Checkpoint

- $p=\tfrac34r_0$, $\ e=\sqrt{1-p/a}=\tfrac12$ (equivalently $e^2=1+2(E/m)h^2/\mu^2$).
- $r_p=a(1-e)=\tfrac12r_0$, $\ r_a=a(1+e)=\tfrac32r_0$.

### Solution

#### Step 1. Semi-latus rectum

$$p=\frac{h^2}{\mu}=\frac{\tfrac34\mu r_0}{\mu}=\frac34r_0$$

#### Step 2. Eccentricity

From $p=a(1-e^2)$ (Notes Eq. 8.16): $e^2=1-p/a=1-\tfrac34=\tfrac14$, so $e=\tfrac12$. Substituting $a=-\mu/(2E/m)$ and $p=h^2/\mu$ gives the general formula $e^2=1+2(E/m)h^2/\mu^2=1+2\big(-\tfrac{\mu}{2r_0}\big)\tfrac{3\mu r_0}{4\mu^2}=1-\tfrac34$, the same value.

#### Step 3. Apsides

$$r_p=a(1-e)=\frac{r_0}{2},\qquad r_a=a(1+e)=\frac{3r_0}{2}$$

and indeed $r_p+r_a=2a$.

#### Step 4. Independent check

With $v^2=\dot r^2+h^2/r^2$, the energy at an apsis ($\dot r=0$) reads $\dfrac{h^2}{2r^2}-\dfrac{\mu}{r}=\dfrac Em$. Multiplying by $2r^2/\mu$ with $h^2=\tfrac34\mu r_0$ and $E/m=-\mu/(2r_0)$:

$$\frac34r_0-2r=-\frac{r^2}{r_0}\ \Longrightarrow\ r^2-2r_0r+\frac34r_0^2=0\ \Longrightarrow\ r=r_0\pm\sqrt{r_0^2-\tfrac34r_0^2}=r_0\pm\frac{r_0}{2}$$

the same $r_p=r_0/2$ and $r_a=3r_0/2$.

## (c) Position on the orbit, apsidal speeds and period [1.5 pts]

Find the true anomaly $\theta_0$ of the initial point (justify the sign), the speeds $v_p$, $v_a$ at the apsides of the conic ($v_p$ is the speed the conic would have at its virtual perigee) and the period $\tau$ of the full ellipse.

### Hint

$r_0=p/(1+e\cos\theta_0)$ has two solutions; the radial velocity $\dot r=\dfrac{\mu}{h}e\sin\theta$ (differentiate the orbit equation) must be positive.

### Checkpoint

- $\cos\theta_0=-\tfrac12$ and $\dot r>0$, so $\theta_0=+120^\circ$ (outbound, between perigee and apogee).
- $v_p=h/r_p=\sqrt3\sqrt{\mu/r_0}$, $\ v_a=h/r_a=\sqrt{\mu/r_0}/\sqrt3$; $\ \tau=2\pi\sqrt{r_0^3/\mu}$.

### Solution

#### Step 1. True anomaly

$$r_0=\frac{p}{1+e\cos\theta_0}\ \Longrightarrow\ 1+\tfrac12\cos\theta_0=\frac{p}{r_0}=\frac34\ \Longrightarrow\ \cos\theta_0=-\frac12$$

so $\theta_0=\pm120^\circ$.

#### Step 2. Sign from the radial velocity

Differentiating $r=p\,(1+e\cos\theta)^{-1}$ with the chain rule and $\dot\theta=h/r^2$:

$$\dot r=\frac{p\,e\sin\theta\,\dot\theta}{(1+e\cos\theta)^2}=\frac{r^2}{p}\,e\sin\theta\,\frac{h}{r^2}=\frac{h}{p}e\sin\theta=\frac{\mu}{h}e\sin\theta$$

The velocity points away from the planet, $\dot r=v_0\sin\gamma>0$, so $\sin\theta_0>0$ and $\theta_0=+120^\circ$. Check: $\frac{\mu}{h}\,\frac12\,\frac{\sqrt3}2=\frac{\mu}{\sqrt3\sqrt{\mu r_0}}\frac{\sqrt3}{2}=\frac12\sqrt{\mu/r_0}=v_0\sin30^\circ$.

#### Step 3. Apsidal speeds

At the apsides the velocity is perpendicular to $\mathbf r$ ($\dot r=0$), so $v=h/r$:

$$v_p=\frac{h}{r_p}=\frac{\tfrac{\sqrt3}2\sqrt{\mu r_0}}{r_0/2}=\sqrt3\sqrt{\frac{\mu}{r_0}},\qquad v_a=\frac{h}{r_a}=\frac{\tfrac{\sqrt3}2\sqrt{\mu r_0}}{3r_0/2}=\frac{1}{\sqrt3}\sqrt{\frac{\mu}{r_0}}$$

Vis-viva check at the apogee: $\mu\big(\tfrac{2}{r_a}-\tfrac1a\big)=\tfrac{\mu}{r_0}\big(\tfrac43-1\big)=\tfrac{\mu}{3r_0}=v_a^2$.

#### Step 4. Period

Kepler's third law (Notes Eq. 8.18) with $a=r_0$: $\ \tau=2\pi\sqrt{a^3/\mu}=2\pi\sqrt{r_0^3/\mu}$.

## (d) Circularisation impulse at the apogee [2.0 pts]

Compute the impulse $\Delta\mathbf v$ (magnitude and direction) that makes the orbit circular at $r_a$, the change of energy per unit mass and the ratio of the new period to $\tau$. Why is the apogee the right place for a purely tangential burn?

### Hint

On the circle of radius $r_a$ the speed is $\sqrt{\mu/r_a}$ and the velocity is horizontal. At the apogee the velocity is already horizontal.

### Checkpoint

- $v_{circ}=\sqrt{\mu/r_a}=\sqrt{2/3}\,\sqrt{\mu/r_0}$; $\ \Delta v=v_{circ}-v_a=\dfrac{\sqrt2-1}{\sqrt3}\sqrt{\dfrac{\mu}{r_0}}\approx0.239\sqrt{\mu/r_0}$, along $+\mathbf e_\theta$ (prograde).
- $\Delta E/m=\tfrac12(v_{circ}^2-v_a^2)=\dfrac{\mu}{6r_0}>0$; $\ \tau_{circ}/\tau=(3/2)^{3/2}\approx1.837$.

### Solution

#### Step 1. Why the apogee

A circular orbit has $\dot r=0$ everywhere, so its velocity is perpendicular to $\mathbf r$. At the apogee $\dot r=0$ already: the velocity $v_a\,\mathbf e_\theta$ is horizontal and only its magnitude has to change. At any other point the burn would also have to cancel $\dot r$, so it could not be purely tangential.

#### Step 2. Impulse

The circular speed at $r_a$ follows from $\mu/r_a^2=v^2/r_a$ (or from vis-viva with $a=r_a$):

$$v_{circ}=\sqrt{\frac{\mu}{r_a}}=\sqrt{\frac{2\mu}{3r_0}},\qquad \Delta\mathbf v=(v_{circ}-v_a)\,\mathbf e_\theta=\Big(\sqrt{\tfrac23}-\tfrac{1}{\sqrt3}\Big)\sqrt{\frac{\mu}{r_0}}\,\mathbf e_\theta=\frac{\sqrt2-1}{\sqrt3}\sqrt{\frac{\mu}{r_0}}\,\mathbf e_\theta$$

positive: the engine pushes **forward**, in the direction of motion.

#### Step 3. Energy

The position does not change during the burn, so only the kinetic energy changes:

$$\frac{\Delta E}{m}=\frac12\big(v_{circ}^2-v_a^2\big)=\frac12\Big(\frac23-\frac13\Big)\frac{\mu}{r_0}=\frac{\mu}{6r_0}$$

Check with $E/m=-\mu/(2a)$: $-\dfrac{\mu}{2r_a}+\dfrac{\mu}{2a}=-\dfrac{\mu}{3r_0}+\dfrac{\mu}{2r_0}=\dfrac{\mu}{6r_0}$.

#### Step 4. New period

$\tau_{circ}=2\pi\sqrt{r_a^3/\mu}$, so $\tau_{circ}/\tau=(r_a/a)^{3/2}=(3/2)^{3/2}\approx1.837$.

## (e) Time of flight from $r_0$ to the apogee [1.5 pts]

Compute the time the probe needs to go from the initial point to the apogee. Show that it is **not** $\tau\cdot(60^\circ/360^\circ)$. (Extension: use the eccentric anomaly $\mathcal E$, defined by $r=a(1-e\cos\mathcal E)$.)

### Hint

Kepler's second law: equal areas in equal times, not equal angles. Derive $(1-e\cos\mathcal E)\,d\mathcal E=n\,dt$ with $n=\sqrt{\mu/a^3}$ and integrate with Barrow's rule.

### Checkpoint

- $\cos\mathcal E=\dfrac{e+\cos\theta}{1+e\cos\theta}$: $\ \mathcal E_0=90^\circ$ at $\theta_0=120^\circ$, $\ \mathcal E=180^\circ$ at the apogee.
- $t_{0\to A}=\dfrac{1}{n}\big[\mathcal E-e\sin\mathcal E\big]_{\pi/2}^{\pi}=\Big(\dfrac{\pi}{2}+\dfrac12\Big)\sqrt{\dfrac{r_0^3}{\mu}}\approx0.330\,\tau$, twice the naive $\tau/6\approx0.167\,\tau$.

### Solution

#### Step 1. Eccentric anomaly (extension)

Define $\mathcal E$ by $r=a(1-e\cos\mathcal E)$; it runs from $0$ at the perigee to $\pi$ at the apogee. Equating with $r=p/(1+e\cos\theta)$ and $p=a(1-e^2)$ and solving for $\cos\mathcal E$:

$$\cos\mathcal E=\frac1e\Big(1-\frac{1-e^2}{1+e\cos\theta}\Big)=\frac{e+\cos\theta}{1+e\cos\theta}$$

At $\theta_0=120^\circ$: $\cos\mathcal E_0=(\tfrac12-\tfrac12)/(1-\tfrac14)=0$, so $\mathcal E_0=\pi/2$ (outbound branch); check $r=a(1-0)=r_0$. At the apogee $\mathcal E=\pi$.

#### Step 2. Kepler's equation

The energy equation $\dot r^2+h^2/r^2=\mu(2/r-1/a)$ with $h^2=\mu a(1-e^2)$ gives

$$\dot r^2=\frac{\mu}{a\,r^2}\big[2ar-r^2-a^2(1-e^2)\big]$$

Substituting $r=a(1-e\cos\mathcal E)$: $2ar-r^2-a^2(1-e^2)=a^2\big[2-2e\cos\mathcal E-1+2e\cos\mathcal E-e^2\cos^2\mathcal E-1+e^2\big]=a^2e^2\sin^2\mathcal E$. Hence $\dot r=\pm\sqrt{\mu/a}\;a\,e\sin\mathcal E/r$. With $\mathcal E$ increasing along the motion, $\sin\mathcal E>0$ on the outbound branch ($0<\mathcal E<\pi$, $\dot r>0$) and $\sin\mathcal E<0$ on the inbound branch ($\pi<\mathcal E<2\pi$, $\dot r<0$), so the sign is $+$ on **both** branches: $\dot r=\sqrt{\mu/a}\;a\,e\sin\mathcal E/r$ for every $\mathcal E$. On the other hand, by the chain rule $\dot r=a\,e\sin\mathcal E\,\dot{\mathcal E}$, also valid on both branches. Equating (and, at the apses where $\sin\mathcal E=0$, by continuity):

$$\dot{\mathcal E}=\frac{\sqrt{\mu/a}}{r}=\frac{n}{1-e\cos\mathcal E}\quad\text{for every }\mathcal E\ \Longrightarrow\ (1-e\cos\mathcal E)\,d\mathcal E=n\,dt,\qquad n=\sqrt{\frac{\mu}{a^3}}$$

#### Step 3. Integration with Barrow's rule

The antiderivative of $1-e\cos\mathcal E$ is $\mathcal E-e\sin\mathcal E$, so

$$n\,t_{0\to A}=\big[\mathcal E-e\sin\mathcal E\big]_{\pi/2}^{\pi}=(\pi-0)-\Big(\frac{\pi}{2}-\frac12\Big)=\frac{\pi}{2}+\frac12$$

and with $1/n=\sqrt{r_0^3/\mu}$ (because $a=r_0$): $\ t_{0\to A}=\big(\tfrac{\pi}{2}+\tfrac12\big)\sqrt{r_0^3/\mu}\approx2.071\sqrt{r_0^3/\mu}$. As a fraction of the period, $(\pi/2+1/2)/(2\pi)\approx0.330$.

#### Step 4. The trap

The angle swept is $60^\circ$, one sixth of a turn, but the time is a third of the period: near the apogee the probe is slow ($\dot\theta=h/r^2$ is small), so equal angles do **not** take equal times. A direct numerical quadrature of $dt=r^2\,d\theta/h$ from $120^\circ$ to $180^\circ$ gives the same $\pi/2+1/2$.

## (f) Numerical values and a failed burn [1.5 pts]

With $\mu=4.0\times10^{14}$ m$^3$ s$^{-2}$, $r_0=1.0\times10^7$ m: compute $v_0$, $h$, $v_p$, $v_a$, $\tau$, $\Delta v$, $\Delta E/m$ and $t_{0\to A}$. If the engine had failed at the apogee, would the probe have survived, given the planet radius $R=6.0\times10^6$ m? If not, at which true anomaly and how long after the apogee would it hit the surface?

### Hint

Compare $r_p$ with $R$. The impact point solves $p/(1+e\cos\theta)=R$ on the inbound branch; use Kepler's equation again from $\mathcal E=\pi$.

### Checkpoint

- $v_0=6325$ m/s, $h=5.477\times10^{10}$ m$^2$/s, $v_p=1.095\times10^4$ m/s, $v_a=3651$ m/s, $\tau=9935$ s, $\Delta v=1512$ m/s, $\Delta E/m=6.67\times10^6$ J/kg, $t_{0\to A}=3274$ s (naive: 1656 s).
- $r_p=5.0\times10^6$ m $<R$: impact at $\theta=300^\circ$ ($\cos\theta=\tfrac12$, $\cos\mathcal E=\tfrac45$), $4424$ s after the apogee.

### Solution

#### Step 1. Numbers

$\sqrt{\mu/r_0}=\sqrt{4.0\times10^7}=6325$ m/s $=v_0$ and $\sqrt{r_0^3/\mu}=\sqrt{2.5\times10^6}=1581$ s. Then $h=\tfrac{\sqrt3}2r_0v_0=5.477\times10^{10}$ m$^2$/s, $v_p=\sqrt3\times6325=1.095\times10^4$ m/s, $v_a=6325/\sqrt3=3651$ m/s, $\tau=2\pi\times1581=9935$ s, $v_{circ}=5164$ m/s, $\Delta v=5164-3651=1512$ m/s, $\Delta E/m=\mu/(6r_0)=6.67\times10^6$ J/kg, $\tau_{circ}=1.825\times10^4$ s and $t_{0\to A}=2.071\times1581=3274$ s, against the naive $\tau/6=1656$ s.

#### Step 2. Failed burn

$r_p=r_0/2=5.0\times10^6$ m is smaller than $R=6.0\times10^6$ m: after the apogee the probe would descend into the planet. Impact: $7.5\times10^6/(1+\tfrac12\cos\theta)=6.0\times10^6\Rightarrow\cos\theta=\tfrac12$, and on the inbound branch ($\dot r<0$, $\sin\theta<0$) $\theta=300^\circ$. There $\cos\mathcal E=(\tfrac12+\tfrac12)/(1+\tfrac14)=\tfrac45$ with $\mathcal E$ in $(\pi,2\pi)$: $\mathcal E_i=2\pi-\arccos\tfrac45=5.640$ rad, $\sin\mathcal E_i=-\tfrac35$.

#### Step 3. Time to impact

$$n\,t_{A\to i}=\big[\mathcal E-e\sin\mathcal E\big]_{\pi}^{\mathcal E_i}=\Big(5.640+\frac12\cdot\frac35\Big)-\pi=2.798\ \Longrightarrow\ t_{A\to i}=2.798\times1581=4424\ \text{s}$$

The circularisation burn is therefore not optional: it also raises the perigee from $0.5\,r_0$ to $1.5\,r_0$.

## Interpretation

- **Dimensional check:** $h=r_0v_0$ in m$^2$/s; $h^2/\mu$ in m$^4$ s$^{-2}$/(m$^3$ s$^{-2}$) = m; $E/m$ and $\mu/r$ in m$^2$ s$^{-2}$ = J/kg; $\sqrt{a^3/\mu}$ in s; $\Delta v$ in m/s.
- **Limits:** $\gamma\to0$ with $v_0=\sqrt{\mu/r_0}$ gives $h^2=\mu r_0$, $e=0$: the probe is already on the circle of radius $r_0$. $\gamma\to90^\circ$ gives $h=0$: a radial (degenerate) orbit, straight up and back down. For any $\gamma$, $a=r_0$, so the period does not depend on $\gamma$.
- **Common mistakes in the exam:** (1) concluding that the orbit is circular because $v_0=\sqrt{\mu/r_0}$; (2) using $h=r_0v_0$ without $\cos\gamma$; (3) taking $\theta_0=-120^\circ$ (the inbound point) without checking the sign of $\dot r$; (4) computing $\Delta v$ as $v_{circ}(r_0)-v_0$ or applying it at $r_0$; (5) converting angles into times with $\tau\,\Delta\theta/2\pi$, which is wrong for any $e\ne0$.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
