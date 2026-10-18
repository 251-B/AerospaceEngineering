---
materia: Engineering Mechanics
tema: "Unit 5: rotating frame with angular acceleration, Euler force, motor torque and power"
bank_id: P04
title: "Radial tube on a turntable with increasing rate: Euler force, three regimes and the motor torque"
category: midterm_problem
archetype: relative-motion
level: standard
unit: 5
difficulty: 2
points: 10.0
time_minutes: 60
official: false
origen: "Problem written for the bank in the style of the Midterm 1 papers (MECHANICS_FIRSTPARTIAL_2015 to 2019); not an official exercise. Verified with scripts/mechanics/p04.py"
tags:
  - problem-bank
  - midterm-1
  - rotating-frame
  - inertia-forces
  - euler-force
  - angular-momentum
  - power
---

# Bank P04 — Radial tube on a turntable with increasing rate

> [!info] Practice item, not an official exercise
> Written for the bank in the style of the Midterm 1 papers. Method: Notes §1.5 (change of basis), §3.2 (velocity and acceleration in a moving frame), §4.9 (dynamics of relative motion), §4.8 (angular momentum and torque), §4.4 (power and work) and Chapter 5 (harmonic oscillator). Every number was checked with SymPy.

## Statement

A horizontal turntable turns about the fixed vertical axis $O\mathbf k$ of the inertial frame $S_0=\{O;\mathbf i_0,\mathbf j_0,\mathbf k\}$ ($\mathbf k$ vertical upward, gravity $-g\,\mathbf k$). A motor imposes the angle $\theta(t)$ between $\mathbf i_0$ and a radial line of the table, with

$$\dot\theta=\Omega(t)=\Omega_0+\beta t,\qquad\theta(0)=0$$

($\Omega_0>0$ and $\beta$ constants). A smooth, thin, straight tube is fixed on the table along a diameter of the table, from the rim at $x=-L$ through $O$ to the rim at $x=L$. A bead $P$ of mass $m$ moves inside the tube and is joined to $O$ by a spring of stiffness $k$ and **zero natural length**. The frame $S_1=\{O;\mathbf i_1,\mathbf j_1,\mathbf k\}$ turns with the table, $\mathbf i_1$ along the tube and $\mathbf j_1=\mathbf k\times\mathbf i_1$; $x$ is the signed coordinate of $P$ along $\mathbf i_1$ (so $x<0$ means on the other side of $O$). The table and the tube have moment of inertia $I_T$ about the axis.

![[attachments/EM-M1/p04-turntable-tube.svg]]

(The scalar $k$ is the stiffness; the bold $\mathbf k$ is the vertical unit vector.)

## Setup

- Data: $m$, $k$, $g$, $\Omega_0$, $\beta$, $I_T$, $L$.
- Numerical parts (e), (f): $m=0.2$ kg, $k=20$ N/m (so $\omega_n=\sqrt{k/m}=10$ rad/s), $\beta=0$, $x(0)=x_0=0.1$ m, $\dot x(0)=v_0=0$, $L=0.5$ m, $g=9.81$ m s$^{-2}$, and $\Omega_0=6$, $10$ or $12.5$ rad/s.
- Hypotheses: point particle, no friction in the tube, $S_0$ inertial, the motor delivers whatever torque is needed to keep $\Omega(t)$.

## (a) Degrees of freedom and frames [1.0 pts]

Count the degrees of freedom of $P$. Give $[{}_0R_1]$, $\boldsymbol\omega_{10}$ and $\boldsymbol\alpha_{10}$.

### Hint

The tube removes two of the three coordinates; the rotation is prescribed, not unknown.

### Checkpoint

- 1 degree of freedom, $x$; constraints $y_1=0$, $z_1=0$ (rheonomic in $S_0$).
- $[{}_0R_1]=\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}$, $\boldsymbol\omega_{10}=\Omega(t)\,\mathbf k$, $\boldsymbol\alpha_{10}=\beta\,\mathbf k$.

### Solution

#### Step 1. Count

In $S_1$ the tube is the line $y_1=0$, $z_1=0$: two holonomic constraints, so $3-2=1$ degree of freedom, $x$ (Notes §2.7). In $S_0$ the tube turns with the prescribed $\theta(t)$, so the constraints depend explicitly on time (rheonomic).

#### Step 2. Frames

$\mathbf i_1=\cos\theta\,\mathbf i_0+\sin\theta\,\mathbf j_0$, $\mathbf j_1=-\sin\theta\,\mathbf i_0+\cos\theta\,\mathbf j_0$: the columns of $[{}_0R_1]$ above, a simple rotation about $\mathbf k$ (Notes §1.5) with $\det=\cos^2\theta+\sin^2\theta=1$ and $RR^T=I$. Then $\boldsymbol\omega_{10}=\dot\theta\,\mathbf k=\Omega(t)\,\mathbf k$ and $\boldsymbol\alpha_{10}=\dot\Omega\,\mathbf k=\beta\,\mathbf k$.

## (b) Kinematics [1.5 pts]

Write the relative velocity and acceleration of $P$ and its absolute acceleration in $\mathcal B_1$, (i) with the Coriolis theorem and (ii) by differentiating $\mathbf r=x\,\mathbf i_1$ directly in $S_0$.

### Hint

$\dot{\mathbf i}_1=\Omega\,\mathbf j_1$, $\dot{\mathbf j}_1=-\Omega\,\mathbf i_1$ and $\dot\Omega=\beta$.

### Checkpoint

- $\mathbf v_{rel}=\dot x\,\mathbf i_1$, $\mathbf a_{rel}=\ddot x\,\mathbf i_1$.
- $\mathbf a=(\ddot x-\Omega^2x)\,\mathbf i_1+(2\Omega\dot x+\beta x)\,\mathbf j_1$.

### Solution

#### Step 1. Coriolis theorem

$O$ is fixed, so (Notes §3.2) $\mathbf a=\mathbf a_{rel}+\boldsymbol\alpha\times\mathbf r+\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)+2\boldsymbol\omega\times\mathbf v_{rel}$, with $\mathbf r=x\,\mathbf i_1$ and $\mathbf k\times\mathbf i_1=\mathbf j_1$, $\mathbf k\times\mathbf j_1=-\mathbf i_1$:

$$\boldsymbol\alpha\times\mathbf r=\beta x\,\mathbf j_1,\qquad\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)=\Omega\,\mathbf k\times\Omega x\,\mathbf j_1=-\Omega^2x\,\mathbf i_1,\qquad2\boldsymbol\omega\times\mathbf v_{rel}=2\Omega\dot x\,\mathbf j_1$$

$$\mathbf a=(\ddot x-\Omega^2x)\,\mathbf i_1+(2\Omega\dot x+\beta x)\,\mathbf j_1$$

#### Step 2. Direct differentiation

$\mathbf v=\dfrac{d}{dt}(x\,\mathbf i_1)=\dot x\,\mathbf i_1+x\Omega\,\mathbf j_1$ (product rule). Again, with $\dfrac{d}{dt}(x\Omega)=\dot x\Omega+x\dot\Omega=\dot x\Omega+x\beta$:

$$\mathbf a=\ddot x\,\mathbf i_1+\dot x\Omega\,\mathbf j_1+(\dot x\Omega+x\beta)\,\mathbf j_1+x\Omega(-\Omega\,\mathbf i_1)$$

which is the same result. The term $\beta x\,\mathbf j_1$ is the tangential acceleration of the point of the table under $P$.

## (c) Forces and inertia forces [1.5 pts]

Write all the forces on $P$ in $S_1$, including the three inertia forces.

### Hint

The smooth tube cannot push along $\mathbf i_1$. Inertia forces: $-m\boldsymbol\alpha\times\mathbf r$, $-m\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)$, $-2m\boldsymbol\omega\times\mathbf v_{rel}$.

### Checkpoint

- $\mathbf F_k=-kx\,\mathbf i_1$, $\mathbf W=-mg\,\mathbf k$, $\mathbf N=N_y\,\mathbf j_1+N_z\,\mathbf k$.
- $\mathbf F_{E}=-m\beta x\,\mathbf j_1$ (Euler), $\mathbf F_{cf}=m\Omega^2x\,\mathbf i_1$, $\mathbf F_{cor}=-2m\Omega\dot x\,\mathbf j_1$.

### Solution

#### Step 1. Applied forces and reaction

The spring has zero natural length, so its force is $-k\,\overrightarrow{OP}=-kx\,\mathbf i_1$. The weight is $-mg\,\mathbf k$. The tube is smooth: its reaction has no $\mathbf i_1$ component, $\mathbf N=N_y\,\mathbf j_1+N_z\,\mathbf k$.

#### Step 2. Inertia forces of $S_1$

From the terms of (b) multiplied by $-m$ (Notes §4.9):

$$\mathbf F_E=-m\beta x\,\mathbf j_1,\qquad\mathbf F_{cf}=m\Omega^2x\,\mathbf i_1,\qquad\mathbf F_{cor}=-2m\Omega\dot x\,\mathbf j_1$$

The Euler (azimuthal) force exists only because the rotation accelerates; it points against the sense of rotation for $\beta>0$.

## (d) Equation of motion and reactions [1.5 pts]

Obtain the equation of motion free of reactions, and $N_y$, $N_z$. Why does the equation contain $\Omega^2$ but not $\beta$?

### Hint

Project $m\mathbf a_{rel}=\sum\mathbf F$ on $\mathbf i_1$, $\mathbf j_1$, $\mathbf k$.

### Checkpoint

- $\ddot x+\Big(\dfrac km-\Omega(t)^2\Big)x=0$.
- $N_y=m(\beta x+2\Omega\dot x)$, $\ N_z=mg$.

### Solution

#### Step 1. Projections

$$\mathbf i_1:\ m\ddot x=-kx+m\Omega^2x\qquad\mathbf j_1:\ 0=N_y-m\beta x-2m\Omega\dot x\qquad\mathbf k:\ 0=N_z-mg$$

#### Step 2. Result

$$\ddot x+\Big(\frac km-\Omega(t)^2\Big)x=0,\qquad N_y=m(\beta x+2\Omega\dot x),\qquad N_z=mg$$

#### Step 3. Why no $\beta$

The Euler force $-m\beta x\,\mathbf j_1$ and the Coriolis force are perpendicular to the tube: the wall absorbs them and they appear only in $N_y$. The angular acceleration still acts on $x$, but only through the time-dependent coefficient $\Omega(t)^2=(\Omega_0+\beta t)^2$. (In $S_0$ the same equation is the $\mathbf i_1$ component of $m\mathbf a$ of (b).)

## (e) Constant rate: the three regimes [2.0 pts]

Take $\beta=0$. Solve the equation of motion with $x(0)=x_0$, $\dot x(0)=v_0$ for $\Omega_0^2<k/m$, $\Omega_0^2=k/m$ and $\Omega_0^2>k/m$, write the Jacobi integral, and evaluate each case for the data of the Setup ($\Omega_0=6$, $10$, $12.5$ rad/s).

### Hint

With constant coefficients, $\ddot x+(\omega_n^2-\Omega_0^2)x=0$ is harmonic, free or exponential depending on the sign of $\omega_n^2-\Omega_0^2$.

### Checkpoint

- $\Omega_0^2<\omega_n^2$: $x=x_0\cos\omega t+\dfrac{v_0}{\omega}\sin\omega t$, $\omega=\sqrt{\omega_n^2-\Omega_0^2}$.
- $\Omega_0^2=\omega_n^2$: $x=x_0+v_0t$ (every position is a neutral relative equilibrium).
- $\Omega_0^2>\omega_n^2$: $x=x_0\cosh\lambda t+\dfrac{v_0}{\lambda}\sinh\lambda t$, $\lambda=\sqrt{\Omega_0^2-\omega_n^2}$; it decays only if $v_0=-\lambda x_0$.
- Data: $\omega=8$ rad/s, $x=0.1\cos8t$ m, period $0.7854$ s; $x\equiv0.1$ m; $\lambda=7.5$ s$^{-1}$, $x=0.1\cosh7.5t$ m.

### Solution

#### Step 1. $\Omega_0^2<k/m$

$\ddot x+\omega^2x=0$ with $\omega^2=k/m-\Omega_0^2>0$ (Notes Ch. 5): $x=A\cos\omega t+B\sin\omega t$. $x(0)=A=x_0$; $\dot x=-A\omega\sin\omega t+B\omega\cos\omega t$ gives $\dot x(0)=B\omega=v_0$. Data, $\Omega_0=6$: $\omega=\sqrt{100-36}=8$ rad/s, $x=0.1\cos8t$ m, period $2\pi/8=0.7854$ s. The spring wins over the centrifugal force.

#### Step 2. $\Omega_0^2=k/m$ (the trap)

$\ddot x=0$: integrating twice with Barrow's rule, $\dot x=v_0$ and $x=x_0+v_0t$. With $v_0=0$ the bead stays where it is, wherever that is: the spring force $kx$ is exactly the centrifugal force $m\Omega_0^2x$ at every $x$. With $v_0\neq0$ the bead drifts at constant relative speed. It is neither an oscillation of zero frequency nor an exponential escape. Data, $\Omega_0=10$: $x\equiv0.1$ m.

#### Step 3. $\Omega_0^2>k/m$

$\ddot x-\lambda^2x=0$ with $\lambda^2=\Omega_0^2-k/m$: $x=A\cosh\lambda t+B\sinh\lambda t$, with $x(0)=A=x_0$ and $\dot x(0)=B\lambda=v_0$. Writing it as $\tfrac12(x_0+v_0/\lambda)e^{\lambda t}+\tfrac12(x_0-v_0/\lambda)e^{-\lambda t}$, the growing exponential disappears only for $v_0=-\lambda x_0$, when $x=x_0e^{-\lambda t}$. Data, $\Omega_0=12.5$: $\lambda=\sqrt{156.25-100}=7.5$ s$^{-1}$, $x=0.1\cosh7.5t$ m.

#### Step 4. Jacobi integral

Multiplying the equation by $\dot x$: $\dfrac{d}{dt}\Big[\tfrac12\dot x^2+\tfrac12\Big(\dfrac km-\Omega_0^2\Big)x^2\Big]=0$, so

$$\tfrac12\dot x^2+\tfrac12\Big(\frac km-\Omega_0^2\Big)x^2=\text{const}$$

the energy in $S_1$ with the spring and centrifugal potentials. $\mathbf N$, $\mathbf F_{cor}$ and $\mathbf F_E$ do no work in $S_1$ because they are orthogonal to $\mathbf v_{rel}$.

## (f) Reaching the end of the tube [1.0 pts]

For $\Omega_0=12.5$ rad/s, $\beta=0$ and the data of the Setup, find the time at which the bead reaches the rim ($x=L$), its relative speed then, and the reaction there.

### Hint

$\cosh\lambda t=L/x_0$; for the speed use the Jacobi integral or $\dot x=\lambda x_0\sinh\lambda t$ with $\sinh=\sqrt{\cosh^2-1}$.

### Checkpoint

- $t_L=\dfrac{\operatorname{arccosh}5}{7.5}=0.3057$ s; $\dot x=0.75\sqrt{24}=3.674$ m/s.
- $N_y=2m\Omega_0\dot x=18.37$ N, $N_z=mg=1.962$ N.

### Solution

#### Step 1. Time

$0.1\cosh7.5t_L=0.5\Rightarrow\cosh7.5t_L=5\Rightarrow t_L=\dfrac{\operatorname{arccosh}5}{7.5}=\dfrac{2.2924}{7.5}=0.3057$ s.

#### Step 2. Speed

$\dot x=x_0\lambda\sinh\lambda t$ with $\sinh\lambda t_L=\sqrt{25-1}=\sqrt{24}$: $\dot x=0.1\cdot7.5\cdot\sqrt{24}=3.674$ m/s. Check with the Jacobi integral: $\dot x^2=\lambda^2(L^2-x_0^2)=56.25\cdot0.24=13.5$ m$^2$ s$^{-2}$.

#### Step 3. Reaction

$N_y=m(0+2\Omega_0\dot x)=2\cdot0.2\cdot12.5\cdot3.674=18.37$ N, about nine times the weight $N_z=mg=1.962$ N.

## (g) Motor torque and power balance [1.5 pts]

With the angular-momentum theorem about the axis, find the torque $M$ the motor must deliver to keep $\Omega(t)$, and check it against $N_y$. Write the power balance of the bead in $S_0$. For the case of (f), give $M$ (beyond $I_T\beta$) and the power at $x=L$, and the work of the motor on the bead between $x_0$ and $L$.

### Hint

$H_z=\mathbf k\cdot(\mathbf r\times m\mathbf v)$ with $\mathbf v=\dot x\,\mathbf i_1+\Omega x\,\mathbf j_1$. The bead pushes the tube with $-\mathbf N$.

### Checkpoint

- $H_z=mx^2\Omega$, $\ \dfrac{dH_z}{dt}=m(2x\dot x\Omega+x^2\beta)=xN_y$; $\ M=I_T\beta+mx(\beta x+2\Omega\dot x)$.
- $\dfrac{d}{dt}(T+V)=\Omega\,xN_y=M_{bead}\,\Omega$ (the reaction works in $S_0$, not in $S_1$).
- Case (f): $xN_y=9.186$ N m, power $114.8$ W, work $=\Omega_0\Delta H_z=m\Omega_0^2(L^2-x_0^2)=7.5$ J $=\Delta(T+V)$.

### Solution

#### Step 1. Angular momentum of the bead about the axis

$\mathbf r\times m\mathbf v=x\,\mathbf i_1\times m(\dot x\,\mathbf i_1+\Omega x\,\mathbf j_1)=mx^2\Omega\,\mathbf k$, so $H_z=mx^2\Omega$. By the product rule:

$$\frac{dH_z}{dt}=m\big(2x\dot x\,\Omega+x^2\dot\Omega\big)=m\big(2x\dot x\,\Omega+x^2\beta\big)$$

#### Step 2. Torque on the bead

Moments about the axis (Notes §4.8): the spring force passes through $O$; $\mathbf r\times\mathbf W=x\,\mathbf i_1\times(-mg\,\mathbf k)=mgx\,\mathbf j_1$ and $\mathbf r\times N_z\mathbf k$ are horizontal; only $\mathbf r\times N_y\mathbf j_1=xN_y\,\mathbf k$ counts. Hence $\dfrac{dH_z}{dt}=xN_y$, and with $N_y$ of (d): $xN_y=mx(\beta x+2\Omega\dot x)$, the same expression as Step 1. The two routes agree.

#### Step 3. Motor torque

The table receives the motor torque $M$ and the moment $-xN_y$ of the bead's push on the tube: $I_T\beta=M-xN_y$, so

$$M=I_T\beta+mx\big(\beta x+2\Omega\dot x\big)$$

Even at constant rate ($\beta=0$) the motor must supply $2m\Omega x\dot x$ whenever the bead moves radially.

#### Step 4. Power balance in $S_0$

$T=\tfrac12m(\dot x^2+\Omega^2x^2)$, $V=\tfrac12kx^2$. Differentiating, $\dfrac{d}{dt}(T+V)=m\dot x\ddot x+m\Omega\beta x^2+m\Omega^2x\dot x+kx\dot x$, and with $m\ddot x=-kx+m\Omega^2x$ from (d): $\dfrac{d}{dt}(T+V)=2m\Omega^2x\dot x+m\Omega\beta x^2=\Omega\,xN_y$. This is the power of $N_y\mathbf j_1$ on the absolute velocity, $N_y\,\Omega x$ (Notes §4.4): in $S_0$ the reaction of the moving tube works; in $S_1$ it does not.

#### Step 5. Numbers at $x=L$ (case (f), $\beta=0$)

$xN_y=0.5\cdot18.37=9.186$ N m and the power is $\Omega_0xN_y=12.5\cdot9.186=114.8$ W. Since $\beta=0$, the work of the motor on the bead is $\displaystyle\int M\Omega_0\,dt=\Omega_0\int\frac{dH_z}{dt}dt=\Omega_0\,[H_z]_{0}^{t_L}=\Omega_0\big(H_z(t_L)-H_z(0)\big)=m\Omega_0^2(L^2-x_0^2)=0.2\cdot156.25\cdot0.24=7.5$ J. Check: $T$ goes from $0.15625$ to $\tfrac12\cdot0.2\,(13.5+39.0625)=5.25625$ J and $V$ from $0.1$ to $2.5$ J, so $\Delta(T+V)=5.1+2.4=7.5$ J.

## Interpretation

- **Dimensional check:** $k/m$ and $\Omega^2$ are s$^{-2}$; $N_y=m(\beta x+2\Omega\dot x)$ is kg (s$^{-2}$ m) = N; $H_z=mx^2\Omega$ is kg m$^2$ s$^{-1}$; $M$ is N m and $M\Omega$ is W.
- **Limits:** $k=0$ gives the classic bead on a rotating rod, $x=x_0\cosh\Omega_0t$; $\Omega_0=0$, $\beta=0$ gives the plain oscillator $\omega=\omega_n$. With $\beta>0$ the coefficient $k/m-\Omega(t)^2$ eventually becomes negative: a bead that oscillates at first is pushed outwards once $\Omega(t)>\omega_n$.
- **Common mistakes in the exam:** (1) forgetting the Euler force $-m\boldsymbol\alpha\times\mathbf r$ (it changes $N_y$ and the torque, not the equation of motion); (2) at $\Omega_0^2=k/m$ writing an exponential or a harmonic solution instead of $x=x_0+v_0t$; (3) claiming that the energy $T+V$ of the bead is conserved because the tube is smooth: in $S_0$ the tube moves and its reaction works; (4) computing the motor torque without the $I_T\beta$ term of the table, or with the wrong sign of the bead's push.

**Back to:** [[Problem Set - Engineering Mechanics Midterm 1 Problem Bank]]
