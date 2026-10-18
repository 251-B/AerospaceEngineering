---
materia: Engineering Mechanics
tema: "Units 2 and 5: forced damped oscillator in a translating frame"
bank_id: P08
title: "Seismic accelerometer on a vibrating base: inertia force, frequency response and the two operating regimes"
category: midterm_problem
archetype: oscillations
level: standard
unit: 2
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers; not an official exercise. Verified with scripts/mechanics/p08.py"
tags:
  - problem-bank
  - midterm-1
  - oscillations
  - forced-damped-oscillator
  - translating-frame
  - inertia-forces
---

# Bank P08 — Seismic accelerometer on a vibrating base

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §3.2 and §4.9 (relative motion, inertia forces), §5.2 (complex representation), §5.3 (damped oscillator) and §5.4 to §5.4.1 (periodic forcing and resonance). Every equation and number was checked with SymPy (Lagrange equations in the inertial frame as an independent route, an extension beyond the course notes).

## Statement

A vibration sensor is a rigid case whose floor is bolted to a structure that moves **vertically** with the prescribed law $z(t)=Z\cos\nu t$ ($Z>0$, $\nu>0$), where $z$ is the height of the case floor above a fixed datum, measured along the upward vertical axis $y$ of the inertial frame $S_0$. Inside the case, a proof mass $m$ (a particle that can only move along the vertical) is joined to the case floor by a linear spring of stiffness $k$ and natural length $L_0$ and by a linear viscous damper of constant $c$ (force $-c$ times the velocity of the mass relative to the case). Uniform gravity $-g\,\mathbf j$ acts.

![[attachments/EM-M1/p08-seismic-accelerometer.svg]]

Let $S_1$ be the frame attached to the case. The relative coordinate $x$ is the height of the mass in $S_1$ measured **from its static equilibrium level** (the level where it rests when $z\equiv0$), positive upwards. Write $\omega_0=\sqrt{k/m}$ and $\zeta=c/(2\sqrt{km})$ (the Notes' damping parameter is $\gamma=c/(2m)=\zeta\omega_0$), and assume $0<\zeta<1$.

## Setup

- Data: $m$, $k$, $c$, $L_0$, $g$, $Z$, $\nu$. Numerical part (f): $m=0.050$ kg, $k=500$ N/m, $c=2.0$ N s/m, $Z=2.0$ mm, $\nu=50$ rad/s, $g=9.81$ m/s$^2$.
- Hypotheses: point mass with vertical motion only (lateral guides are smooth), massless spring and damper, linear laws, $S_0$ inertial.
- Frames: $S_0=\{O;\mathbf i,\mathbf j\}$ fixed; $S_1$ attached to the case, a **translating** frame: $\boldsymbol\omega_{10}=\mathbf 0$, origin acceleration $\ddot z\,\mathbf j$.
- Notation: $x$ is the **vertical** relative coordinate of the mass (along $\mathbf j$), not a coordinate along the horizontal axis $\mathbf i$ of $S_0$.

## (a) Degrees of freedom, frames and kinematics [1.5 pts]

How many degrees of freedom does the mass have? Write the absolute position, velocity and acceleration of the mass in terms of $z$ and $x$, and identify the relative and the transport (dragging) acceleration.

### Hint

The case motion is given, not unknown. Call $\xi$ the height of the mass above the case floor; $\xi=\xi_e+x$.

### Checkpoint

- 1 degree of freedom, $x(t)$; $z(t)$ is prescribed (rheonomic constraint).
- $y_P=z+\xi_e+x$, $\ \mathbf a_P=(\ddot z+\ddot x)\,\mathbf j$; $\mathbf a_{rel}=\ddot x\,\mathbf j$, transport $\ddot z\,\mathbf j=-\nu^2Z\cos\nu t\,\mathbf j$, no Coriolis term.

### Solution

#### Step 1. Degrees of freedom

The mass can only move along the vertical: 1 coordinate. The case is not a body of the problem but a prescribed motion, so it adds no unknown; the constraint "the mass moves on the vertical line of the case" is rheonomic in $S_0$ and fixed in $S_1$. The coordinate is $x$.

#### Step 2. Absolute kinematics

Let $\xi$ be the height of the mass above the case floor, so the absolute height is $y_P=z+\xi$, and $\xi=\xi_e+x$ with $\xi_e$ constant (found in (b)). Differentiating twice ($\xi_e$ is constant):

$$y_P=z+\xi_e+x,\qquad \dot y_P=\dot z+\dot x,\qquad \ddot y_P=\ddot z+\ddot x$$

#### Step 3. Relative-motion reading

$S_1$ translates, so $\mathbf a_P=\mathbf a_{O_1}+\mathbf a_{rel}$ (Notes §3.2 with $\boldsymbol\omega=\mathbf 0$): transport acceleration $\ddot z\,\mathbf j$ with, by the chain rule on $\cos(\nu t)$, $\dot z=-\nu Z\sin\nu t$ and $\ddot z=-\nu^2Z\cos\nu t$; relative acceleration $\ddot x\,\mathbf j$; the Coriolis term $2\boldsymbol\omega\times\mathbf v_{rel}$ vanishes.

## (b) Forces in the case frame and static equilibrium [1.5 pts]

List the forces on the mass in $S_1$, including the inertia force, in terms of $\xi$ and $\dot\xi$. Find the static equilibrium height $\xi_e$ for $z\equiv0$ and the static deflection of the spring.

### Hint

Spring force on the mass: $-k(\xi-L_0)\,\mathbf j$ (it pushes up when compressed). The inertia force of a translating frame is $-m\,\mathbf a_{O_1}$.

### Checkpoint

- $\mathbf F_s=-k(\xi-L_0)\,\mathbf j$, $\ \mathbf F_d=-c\dot\xi\,\mathbf j$, $\ \mathbf W=-mg\,\mathbf j$, $\ \mathbf F_{in}=-m\ddot z\,\mathbf j=m\nu^2Z\cos\nu t\,\mathbf j$; lateral reaction $\mathbf N\perp\mathbf j$.
- $\xi_e=L_0-mg/k$; static deflection $\delta_{st}=mg/k$ (spring compressed).

### Solution

#### Step 1. Applied forces

- Spring: elongation $\xi-L_0$; the force on the mass is $\mathbf F_s=-k(\xi-L_0)\,\mathbf j$.
- Damper: opposes the velocity relative to the case, $\mathbf F_d=-c\dot\xi\,\mathbf j=-c\dot x\,\mathbf j$.
- Weight: $\mathbf W=-mg\,\mathbf j$.
- Guides: a smooth lateral reaction $\mathbf N$, horizontal; it has no vertical component and does no work.

#### Step 2. Inertia force

In the translating frame $S_1$ the relative-motion law is $m\mathbf a_{rel}=\sum\mathbf F-m\mathbf a_{O_1}$ (Notes §4.9), so

$$\mathbf F_{in}=-m\ddot z\,\mathbf j=m\nu^2Z\cos\nu t\,\mathbf j$$

When the case accelerates upwards ($\ddot z>0$) the mass feels pushed down, as in a lift.

#### Step 3. Static equilibrium

With $z\equiv0$ there is no inertia force and at rest $\dot\xi=0$:

$$-k(\xi_e-L_0)-mg=0\ \Longrightarrow\ \xi_e=L_0-\frac{mg}{k}$$

The spring is compressed by $\delta_{st}=mg/k$ and carries the weight.

## (c) Equation of motion [1.5 pts]

Project the relative-motion law on $\mathbf j$ and obtain the equation of motion for $x$. Explain why $g$ does not appear, and write the equation in the normalised form with $\omega_0$ and $\zeta$.

### Hint

Substitute $\xi=\xi_e+x$ and use the equilibrium condition of (b).

### Checkpoint

- $m\ddot x+c\dot x+kx=m\nu^2Z\cos\nu t$.
- $\ddot x+2\zeta\omega_0\dot x+\omega_0^2x=\nu^2Z\cos\nu t$; $g$ is cancelled by the static preload of the spring.

### Solution

#### Step 1. Projection

$$m\ddot\xi=-k(\xi-L_0)-c\dot\xi-mg-m\ddot z$$

#### Step 2. Change of variable

With $\xi=\xi_e+x$, $\dot\xi=\dot x$, $\ddot\xi=\ddot x$ and $-k(\xi_e+x-L_0)=-kx-k(\xi_e-L_0)=-kx+mg$ (from (b)):

$$m\ddot x=-kx+mg-c\dot x-mg-m\ddot z\ \Longrightarrow\ m\ddot x+c\dot x+kx=-m\ddot z=m\nu^2Z\cos\nu t$$

The weight is a constant force; measuring $x$ from the static equilibrium absorbs it into the spring preload, so it drops out of the dynamics. This is true only because the spring is linear: the same constant offset works at every $x$.

#### Step 3. Normal form

Dividing by $m$, with $k/m=\omega_0^2$ and $c/m=2\zeta\omega_0$:

$$\ddot x+2\zeta\omega_0\dot x+\omega_0^2x=\nu^2Z\cos\nu t$$

This is Notes Eq. 5.32 with the force amplitude $F_1=m\nu^2Z$: the base motion acts as a harmonic force whose amplitude grows with $\nu^2$. Extension (Lagrange equations are not in the course notes): cross-check by Lagrange in $S_0$: $T=\tfrac12m(\dot z+\dot\xi)^2$, $V=mg(z+\xi)+\tfrac12k(\xi-L_0)^2$ and the damper's generalised force $-c\dot\xi$ give the same equation.

## (d) Steady-state response [2.0 pts]

Using the complex representation, find the amplitude $X$ and the phase $\varphi$ of the steady-state solution $x_p=X\cos(\nu t+\varphi)$, and write $X/Z$ as a function of $r=\nu/\omega_0$ and $\zeta$. What is the complete solution?

### Hint

Solve $\ddot{\tilde x}+2\zeta\omega_0\dot{\tilde x}+\omega_0^2\tilde x=\nu^2Ze^{i\nu t}$ with $\tilde x=Ae^{i\nu t}$ and take $x=\mathrm{Re}\,\tilde x$.

### Checkpoint

- $A=\dfrac{\nu^2Z}{\omega_0^2-\nu^2+2i\zeta\omega_0\nu}$; $\ X=|A|=\dfrac{\nu^2Z}{\sqrt{(\omega_0^2-\nu^2)^2+4\zeta^2\omega_0^2\nu^2}}$.
- $\tan\varphi=-\dfrac{2\zeta\omega_0\nu}{\omega_0^2-\nu^2}$ with $-\pi<\varphi<0$; $\ \dfrac XZ=\dfrac{r^2}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}$.
- $x=X\cos(\nu t+\varphi)+a\,e^{-\zeta\omega_0t}\cos(\omega_0\sqrt{1-\zeta^2}\,t+\beta)$.

### Solution

#### Step 1. Complex equation

The real forcing is $\nu^2Z\cos\nu t=\mathrm{Re}\big(\nu^2Ze^{i\nu t}\big)$ (Notes §5.2 and §5.4). With $\tilde x=Ae^{i\nu t}$: $\dot{\tilde x}=i\nu\tilde x$, $\ddot{\tilde x}=-\nu^2\tilde x$ (chain rule on the exponential), and

$$\big(-\nu^2+2i\zeta\omega_0\nu+\omega_0^2\big)A=\nu^2Z\ \Longrightarrow\ A=\frac{\nu^2Z}{\omega_0^2-\nu^2+2i\zeta\omega_0\nu}$$

#### Step 2. Amplitude and phase

Writing $A=Xe^{i\varphi}$, $|A|$ is the modulus of the numerator over that of the denominator:

$$X=\frac{\nu^2Z}{\sqrt{(\omega_0^2-\nu^2)^2+4\zeta^2\omega_0^2\nu^2}},\qquad \varphi=-\arg\big(\omega_0^2-\nu^2+2i\zeta\omega_0\nu\big)$$

so $\tan\varphi=-2\zeta\omega_0\nu/(\omega_0^2-\nu^2)$; the imaginary part of the denominator is positive, hence $-\pi<\varphi<0$ (the mass lags behind the forcing, Notes Eq. 5.42). The real part is $x_p=X\cos(\nu t+\varphi)$.

#### Step 3. Dimensionless form

Dividing numerator and denominator by $\omega_0^2$ with $r=\nu/\omega_0$:

$$\frac XZ=\frac{r^2}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\qquad \tan\varphi=-\frac{2\zeta r}{1-r^2}$$

#### Step 4. Complete solution

Add the general solution of the homogeneous equation (Notes Eq. 5.26, underdamped): $x=X\cos(\nu t+\varphi)+a\,e^{-\zeta\omega_0t}\cos(\omega_0\sqrt{1-\zeta^2}\,t+\beta)$, with $a$, $\beta$ fixed by the initial conditions. The second term is the transient.

## (e) Operating regimes and the resonant peak [2.0 pts]

Discuss the limits $\nu\ll\omega_0$ and $\nu\gg\omega_0$: what does $x$ measure in each case? Then find the forcing frequency at which $X$ is maximum and the maximum value of $X/Z$. Is it at $\nu=\omega_0$, or at $\omega_0\sqrt{1-2\zeta^2}$ as in Notes §5.4.1?

### Hint

Maximise $f(s)=\dfrac{s^2}{(1-s)^2+4\zeta^2s}$ with $s=r^2$. The forcing amplitude here is $m\nu^2Z$, not a constant $F_1$.

### Checkpoint

- $\nu\ll\omega_0$: $x\approx\nu^2Z\cos\nu t/\omega_0^2=-\ddot z/\omega_0^2$ (accelerometer). $\nu\gg\omega_0$: $X\to Z$, $\varphi\to-\pi$, $x\approx-z$ (the mass stays still in $S_0$: vibrometer).
- Peak at $r^2=\dfrac{1}{1-2\zeta^2}$, i.e. $\nu_{peak}=\dfrac{\omega_0}{\sqrt{1-2\zeta^2}}>\omega_0$ (for $\zeta<1/\sqrt2$); $\ \Big(\dfrac XZ\Big)_{max}=\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$.

### Solution

#### Step 1. Low frequency: accelerometer

For $r\to0$ the denominator tends to 1 and $\varphi\to0$: $X\approx r^2Z=\nu^2Z/\omega_0^2$ and

$$x\approx\frac{\nu^2Z\cos\nu t}{\omega_0^2}=-\frac{\ddot z}{\omega_0^2}$$

The relative displacement is proportional to the **acceleration** of the base: the spring force $kx$ supplies the force $-m\ddot z$ the mass needs to follow the case.

#### Step 2. High frequency: vibrometer

For $r\to\infty$: $X/Z\to r^2/r^2=1$ and $\tan\varphi=2\zeta r/(r^2-1)\to0^+$ with $\varphi$ in the third quadrant, so $\varphi\to-\pi$, so $x\approx Z\cos(\nu t-\pi)=-z$. The absolute height $y_P=z+\xi_e+x\approx\xi_e$ is constant: the mass cannot follow the fast motion and stays still in $S_0$, so $x$ measures the **displacement** of the base.

#### Step 3. Maximum of the response

$(X/Z)^2=f(s)=s^2/D$ with $D=(1-s)^2+4\zeta^2s$ and $D'=-2(1-s)+4\zeta^2$. By the quotient rule, $f'(s)=0$ requires $2sD-s^2D'=0$, i.e. $2D=sD'$:

$$2(1-2s+s^2)+8\zeta^2s=-2s+2s^2+4\zeta^2s\ \Longrightarrow\ 2-2s+4\zeta^2s=0\ \Longrightarrow\ s=\frac{1}{1-2\zeta^2}$$

which is admissible ($s>0$) for $\zeta<1/\sqrt2$. Then $1-s=-2\zeta^2/(1-2\zeta^2)$ and

$$D=\frac{4\zeta^4+4\zeta^2(1-2\zeta^2)}{(1-2\zeta^2)^2}=\frac{4\zeta^2(1-\zeta^2)}{(1-2\zeta^2)^2},\qquad f=\frac{s^2}{D}=\frac{1}{4\zeta^2(1-\zeta^2)}$$

so $\nu_{peak}=\omega_0/\sqrt{1-2\zeta^2}$ and $(X/Z)_{max}=1/\big(2\zeta\sqrt{1-\zeta^2}\big)$.

#### Step 4. The trap

The Notes' resonant frequency $\sqrt{\omega_0^2-2\gamma^2}=\omega_0\sqrt{1-2\zeta^2}$ (Eq. 5.46) is for a force of **constant** amplitude $F_1$. Here the forcing $m\nu^2Z$ grows with $\nu^2$, which shifts the maximum of the relative amplitude **above** $\omega_0$. Neither $\nu=\omega_0$ (where $X/Z=1/(2\zeta)$) nor $\omega_0\sqrt{1-2\zeta^2}$ is the peak.

## (f) Numerical case [1.5 pts]

With the data of the Setup, compute $\omega_0$, $\zeta$, the static deflection, $X$, $\varphi$, the energy dissipated per cycle, the decay of the transient, and the error of an accelerometer that reads $\omega_0^2X$ as the base acceleration amplitude. Locate the resonant peak.

### Hint

Energy dissipated per cycle: $W=\oint c\dot x\,dx=\int_0^{2\pi/\nu}c\dot x^2\,dt$.

### Checkpoint

- $\omega_0=100$ rad/s, $\zeta=0.2$, $r=0.5$, $\delta_{st}=0.981$ mm.
- $X=0.644$ mm, $\varphi=-14.93^\circ$; $W=\pi c\nu X^2=1.30\times10^{-4}$ J per cycle.
- Transient $\propto e^{-20t}$ (relaxation time 0.05 s, below 1 % after 0.230 s), $\omega_d=97.98$ rad/s.
- $\omega_0^2X=6.44$ m/s$^2$ against $\nu^2Z=5.0$ m/s$^2$: $+28.8$ % error; peak at $\nu=104.3$ rad/s with $X=2.552\,Z=5.10$ mm.

### Solution

#### Step 1. Parameters

$\omega_0=\sqrt{500/0.050}=100$ rad/s, $\zeta=2.0/(2\sqrt{500\times0.050})=2.0/10=0.2$, $r=50/100=0.5$, $\delta_{st}=mg/k=0.050\times9.81/500=9.81\times10^{-4}$ m $=0.981$ mm.

#### Step 2. Amplitude and phase

$$\frac XZ=\frac{0.25}{\sqrt{0.75^2+0.2^2}}=\frac{0.25}{\sqrt{0.6025}}=0.3221\ \Longrightarrow\ X=0.644\ \text{mm},\qquad \varphi=-\arctan\frac{0.2}{0.75}=-14.93^\circ$$

#### Step 3. Energy per cycle

With $\dot x=-\nu X\sin(\nu t+\varphi)$ and $\int_0^{2\pi/\nu}\sin^2(\nu t+\varphi)\,dt=\pi/\nu$ (the antiderivative of $\sin^2u$ is $\tfrac u2-\tfrac{\sin2u}{4}$, evaluated between $u=\varphi$ and $u=\varphi+2\pi$):

$$W=c\nu^2X^2\frac{\pi}{\nu}=\pi c\nu X^2=\pi\times2.0\times50\times(6.442\times10^{-4})^2=1.30\times10^{-4}\ \text{J}$$

In steady state this equals the work done per cycle by the inertia force $m\nu^2Z\cos\nu t$ on the relative motion.

#### Step 4. Transient

The homogeneous part decays as $e^{-\zeta\omega_0t}=e^{-20t}$: relaxation time $1/(\zeta\omega_0)=0.05$ s, and $e^{-20t}=0.01$ at $t=\ln100/20=0.230$ s. It oscillates at $\omega_d=\omega_0\sqrt{1-\zeta^2}=97.98$ rad/s.

#### Step 5. Accelerometer error and peak

The true acceleration amplitude is $\nu^2Z=2500\times0.002=5.0$ m/s$^2$; the instrument reads $\omega_0^2X=10^4\times6.442\times10^{-4}=6.44$ m/s$^2$, i.e. $+28.8$ %: at $r=0.5$ with $\zeta=0.2$ the sensor is too close to resonance. The peak is at $\nu_{peak}=100/\sqrt{0.92}=104.3$ rad/s with $X/Z=1/(0.4\sqrt{0.96})=2.552$, $X=5.10$ mm.

## Interpretation

- **Dimensional check:** $\omega_0^2=k/m$ in (N/m)/kg = s$^{-2}$; $\zeta=c/(2\sqrt{km})$ in (N s/m)/(kg s$^{-1}$) = 1; $\nu^2Z$ in m s$^{-2}$, the same as $\omega_0^2x$; $W=\pi c\nu X^2$ in (N s/m)(s$^{-1}$)(m$^2$) = J.
- **Limits:** $\zeta\to0$ gives $X/Z=r^2/|1-r^2|$, infinite at $r=1$; $Z\to0$ leaves the free damped oscillator of Notes §5.3. With $\zeta\approx0.7$ the factor $1/\sqrt{(1-r^2)^2+(2\zeta r)^2}$ stays close to 1 over a wide band (at $r=0.5$ it is 0.975, a $-2.5$ % error), which is why real accelerometers are built with that damping.
- **Common mistakes in the exam:** (1) writing the inertia force as $+m\ddot z$, or forgetting it and writing the spring force with the absolute coordinate; (2) keeping $mg$ in the equation after measuring $x$ from the static equilibrium (or dropping it when $x$ is measured from the natural length); (3) taking the peak at $\nu=\omega_0$ or at $\omega_0\sqrt{1-2\zeta^2}$; (4) choosing $\varphi$ in the wrong quadrant with the arctangent above resonance.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
