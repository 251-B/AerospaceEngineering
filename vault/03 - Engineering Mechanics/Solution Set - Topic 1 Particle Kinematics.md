---
title: "Solution Set - Topic 1: Fundamentals and Particle Kinematics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (lecturer's order, derivation boxes)"
language: "English"
tags:
  - solutions
  - particle-kinematics
---

# Topic 1: Fundamentals and Particle Kinematics - Complete Analytical Solutions

This document contains the step-by-step solutions of the 6 problems of Topic 1 (*Particle Kinematics*) of the official UC3M problem collection (`Problems.pdf`), stated in [[Problem Set - Topic 1 Particle Kinematics]]. Each solution follows the lecturer's order: reference frames, bases and coordinates; change of basis and position vector; kinematics; answers and checks. Every calculation lives in a derivation box (law, source, one operation per row with its reason, boxed result, units, meaning) and every result is derived from first principles. Theory: [[Topic 1 - Kinematics of a Point Particle]].

---

## Problem 01: Rocket Helical Trajectory

### Reference Frames, Bases and Coordinates

The rocket is modelled as a point particle $P$. Its three Cartesian coordinates are given as functions of time, so the motion is prescribed: the problem is purely kinematic and has no forces section.

| Item | Definition |
| :--- | :--- |
| Fixed frame | $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, origin at the launch point, $\mathbf k_0$ vertical, along the axis of the helix |
| Fixed basis | $B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ (Notes.pdf, Eq. 1.1) |
| Cylindrical basis | $B_C = \{\mathbf e_R, \mathbf e_\theta, \mathbf e_z\}$, obtained from $B_0$ by a rotation of angle $\theta$ about $\mathbf k_0$ |
| Intrinsic basis | $B_F = \{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ (tangent, principal normal, binormal; Notes.pdf, Eq. 2.13) |
| Cartesian coordinates | $x = a\cos(\omega t)$, $y = a\sin(\omega t)$, $z = v_z t$ (statement) |
| Cylindrical coordinates | $R = \sqrt{x^2+y^2}$, $\theta = \arctan(y/x)$, $z$ (Notes.pdf, Eq. 2.23) |
| Arc length | $s$, measured along the helix from the point reached at $t = 0$ |
| Data | $a$ [m] radius of the helix, $\omega$ [rad/s] angular frequency, $v_z$ [m/s] vertical speed, $t$ [s] time |
| Hypotheses | $a \gt 0$, $\omega \gt 0$, $v_z \gt 0$ constant; the law of the statement is taken to hold for $t \ge 0$ so that part (g), at $t = 0$, is the limit $t \to 0^+$ |
| Degrees of freedom | 3 Cartesian coordinates minus 2 relations of the helix ($x = a\cos(\omega z/v_z)$, $y = a\sin(\omega z/v_z)$) leave 1; it is fixed by the time law |

The position vector is first written in $B_0$, then in $B_C$; the intrinsic basis is built from the velocity in the kinematics section.

### Change of Basis and Position Vector

The view along $\mathbf k_0$ (out of the paper) shows the rotation that takes $B_0$ into $B_C$; the right triangle of $\mathbf e_R$ gives its components.

![[attachments/EM-SOL/p01-top-view.svg]]

> [!derivation] Cylindrical radius and azimuth of the helix
> **Law:** coordinate transformation of cylindrical coordinates
> **Source:** Notes.pdf, Eq. 2.23; [Lecture 1, Slide 17]
>
> $$\begin{aligned}
> R &= \sqrt{x^2 + y^2} \quad &\text{(definition of the cylindrical radius)} \\
> &= \sqrt{a^2\cos^2(\omega t) + a^2\sin^2(\omega t)} \quad &\text{(statement, Eqs. (1) and (2))} \\
> &= a\sqrt{\cos^2(\omega t) + \sin^2(\omega t)} \quad &\text{(common factor $a^2$, with $a \gt 0$)} \\
> &= a \quad &\text{(Pythagorean identity)} \\
> \tan\theta &= \frac{y}{x} = \frac{a\sin(\omega t)}{a\cos(\omega t)} = \tan(\omega t) \quad &\text{(definition of the azimuth)} \\
> \theta &= \omega t \quad &\text{($x$ and $\cos\theta$ have the same sign, so the branch is the one of $\omega t$)}
> \end{aligned}$$
>
> $$\boxed{R = a, \qquad \theta = \omega t, \qquad z = v_z t}$$
>
> **Units:** $[R] = [a] = [\mathrm{L}]$; $[\theta] = [\omega][t] = [\mathrm{T^{-1}}][\mathrm{T}] = 1$; $[z] = [\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** the rocket stays on a cylinder of radius $a$ about $\mathbf k_0$, turns about it at the constant rate $\omega$ and climbs at the constant rate $v_z$.

> [!derivation] Unit vectors of the cylindrical basis and the change of basis matrix
> **Law:** components of a unit vector with a known angle; simple rotation about the third axis
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24; [Lecture 1, Slide 7]
>
> In the view of the figure $\mathbf k_0$ points out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up. A positive $\theta$ turns $\mathbf i_0$ towards $\mathbf j_0$, counterclockwise, as the right-hand rule about $\mathbf k_0$ requires.
>
> - $\mathbf e_R$ is the hypotenuse (length 1) of the right triangle whose adjacent leg lies along $\mathbf i_0$ and whose opposite leg lies along $\mathbf j_0$; the angle at $O$ is $\theta$.
> - $\mathbf e_\theta$ is $\mathbf e_R$ turned a further right angle counterclockwise. Its triangle has the angle $\theta$ between $\mathbf e_\theta$ and $\mathbf j_0$: the adjacent leg lies along $\mathbf j_0$, the opposite leg along the negative $\mathbf i_0$ direction, which is the origin of the minus sign.
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(adjacent leg $\cos\theta$ on $\mathbf i_0$, opposite leg $\sin\theta$ on $\mathbf j_0$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(adjacent leg $\cos\theta$ on $\mathbf j_0$, opposite leg $\sin\theta$ pointing to $-\mathbf i_0$ for $0 \lt \theta \lt \pi$)} \\
> \mathbf e_z &= \mathbf k_0 \quad &\text{(the rotation axis is unchanged)} \\
> \det[{}_0R_C] &= 1\cdot(\cos\theta\cos\theta - (-\sin\theta)\sin\theta) \quad &\text{(expansion along the third row, whose only entry is 1 at $(3,3)$)} \\
> &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(Pythagorean identity)} \\
> ([{}_0R_C][{}_0R_C]^T)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> ([{}_0R_C][{}_0R_C]^T)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_C][{}_0R_C]^T)_{22} &= \sin^2\theta + \cos^2\theta = 1 \quad &\text{(row 2 times row 2)} \\
> ([{}_0R_C][{}_0R_C]^T)_{13} &= ([{}_0R_C][{}_0R_C]^T)_{23} = 0, \quad ([{}_0R_C][{}_0R_C]^T)_{33} = 1 \quad &\text{(third row is $(0, 0, 1)$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_C] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_C] = 1, \quad [{}_0R_C][{}_0R_C]^T = I}$$
>
> **Units:** every entry is a cosine or a sine, dimensionless: $[1]$
> **Meaning:** the columns are $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ written in $B_0$; the matrix is a proper rotation, so $B_C$ is orthonormal and right-handed at every instant.

The position vector is built in two steps: from $O$ to the foot $Q$ of $P$ on the plane of $\mathbf i_0$ and $\mathbf j_0$, then up from $Q$ to $P$.

![[attachments/EM-SOL/p01-helix-3d.svg]]

> [!derivation] Position vector in the fixed and in the cylindrical basis
> **Law:** position vector of a point in Cartesian and in cylindrical components
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.28; [Lecture 1, Slide 12]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OQ} + \overrightarrow{QP} \quad &\text{(vector sum through the foot $Q$ on the horizontal plane)} \\
> \overrightarrow{OQ} &= a\cos(\omega t)\,\mathbf i_0 + a\sin(\omega t)\,\mathbf j_0 \quad &\text{(triangle $OQ$: hypotenuse $a$, adjacent leg $a\cos\omega t$, opposite leg $a\sin\omega t$)} \\
> &= a\left(\cos(\omega t)\,\mathbf i_0 + \sin(\omega t)\,\mathbf j_0\right) = a\,\mathbf e_R \quad &\text{(first column of $[{}_0R_C]$)} \\
> \overrightarrow{QP} &= v_z t\,\mathbf k_0 = v_z t\,\mathbf e_z \quad &\text{(height $z$ of the statement)} \\
> \mathbf r_0^P &= a\cos(\omega t)\,\mathbf i_0 + a\sin(\omega t)\,\mathbf j_0 + v_z t\,\mathbf k_0 \quad &\text{(sum in $B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\cos(\omega t)\,\mathbf i_0 + a\sin(\omega t)\,\mathbf j_0 + v_z t\,\mathbf k_0 = a\,\mathbf e_R + v_z t\,\mathbf e_z}$$
>
> **Units:** $[a] = [\mathrm{L}]$ and $[v_z t] = [\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** in $B_C$ the position has no $\mathbf e_\theta$ component: the turning of the rocket is carried entirely by the direction of $\mathbf e_R$.

### Kinematics

#### (a) Velocity and acceleration in the fixed basis

> [!derivation] Velocity and acceleration in Cartesian components
> **Law:** definition of velocity and acceleration; the vectors of $B_0$ are constant in $S_0$
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7; [Lecture 1, Slide 13]
>
> $$\begin{aligned}
> \frac{d}{dt}\cos(\omega t) &= -\sin(\omega t)\,\frac{d(\omega t)}{dt} = -\omega\sin(\omega t) \quad &\text{(chain rule)} \\
> \frac{d}{dt}\sin(\omega t) &= \cos(\omega t)\,\frac{d(\omega t)}{dt} = \omega\cos(\omega t) \quad &\text{(chain rule)} \\
> \mathbf v_0^P &= \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0 + \dot z\,\mathbf k_0 \quad &\text{(Eq. 2.6: $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ constant in $S_0$)} \\
> &= -a\omega\sin(\omega t)\,\mathbf i_0 + a\omega\cos(\omega t)\,\mathbf j_0 + v_z\,\mathbf k_0 \quad &\text{(the two derivatives above; $\dot z$ is $v_z$)} \\
> \mathbf a_0^P &= \ddot x\,\mathbf i_0 + \ddot y\,\mathbf j_0 + \ddot z\,\mathbf k_0 \quad &\text{(Eq. 2.7)} \\
> &= -a\omega\cdot\omega\cos(\omega t)\,\mathbf i_0 + a\omega\cdot(-\omega\sin(\omega t))\,\mathbf j_0 + 0\,\mathbf k_0 \quad &\text{(chain rule again; $v_z$ constant)} \\
> &= -a\omega^2\left(\cos(\omega t)\,\mathbf i_0 + \sin(\omega t)\,\mathbf j_0\right) \quad &\text{(common factor)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\cos\omega t\,\mathbf i_0 + a\sin\omega t\,\mathbf j_0 + v_z t\,\mathbf k_0,\quad \mathbf v_0^P = -a\omega\sin\omega t\,\mathbf i_0 + a\omega\cos\omega t\,\mathbf j_0 + v_z\,\mathbf k_0,\quad \mathbf a_0^P = -a\omega^2\cos\omega t\,\mathbf i_0 - a\omega^2\sin\omega t\,\mathbf j_0}$$
>
> **Units:** $[a\omega] = [\mathrm{L\,T^{-1}}]$, $[v_z] = [\mathrm{L\,T^{-1}}]$; $[a\omega^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the acceleration is horizontal and points from $P$ to the axis of the helix; the vertical motion is uniform.

#### (b) Velocity and acceleration in the cylindrical basis

> [!derivation] Time derivatives of the cylindrical unit vectors
> **Law:** derivative of a vector of constant modulus that rotates with angular velocity $\boldsymbol\omega$ (Poisson)
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eqs. 2.25-2.27; [Lecture 1, Slide 10]
>
> $B_C$ turns about $\mathbf k_0$ at the rate of $\theta$, which is $\omega$, so its angular velocity is $\omega\,\mathbf k_0$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{C} &= \dot\theta\,\mathbf k_0 = \omega\,\mathbf k_0 \quad &\text{(rotation about $\mathbf k_0$, positive by the right-hand rule)} \\
> \dot{\mathbf e}_R &= \omega\,\mathbf k_0\times(\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0) \quad &\text{(Eq. 1.62)} \\
> &= \omega\cos\theta\,(\mathbf k_0\times\mathbf i_0) + \omega\sin\theta\,(\mathbf k_0\times\mathbf j_0) \quad &\text{(distributive property)} \\
> &= \omega\cos\theta\,\mathbf j_0 - \omega\sin\theta\,\mathbf i_0 \quad &\text{($\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> &= \omega\,\mathbf e_\theta \quad &\text{(second column of $[{}_0R_C]$)} \\
> \dot{\mathbf e}_\theta &= \omega\,\mathbf k_0\times(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0) \quad &\text{(Eq. 1.62)} \\
> &= \omega\left(-\sin\theta\,(\mathbf k_0\times\mathbf i_0) + \cos\theta\,(\mathbf k_0\times\mathbf j_0)\right) \quad &\text{(distribute $\mathbf k_0\times$ over the two terms)} \\
> &= \omega\left(-\sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf i_0\right) \quad &\text{($\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> &= -\omega\,\mathbf e_R \quad &\text{(first column of $[{}_0R_C]$)} \\
> \dot{\mathbf e}_z &= \omega\,\mathbf k_0\times\mathbf k_0 = \mathbf 0 \quad &\text{(parallel vectors)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_R = \omega\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\omega\,\mathbf e_R, \qquad \dot{\mathbf e}_z = \mathbf 0}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$, the rate of change of a dimensionless unit vector
> **Meaning:** each unit vector of the horizontal plane turns at the rate $\omega$, always perpendicular to itself.

> [!derivation] Velocity and acceleration in cylindrical components
> **Law:** definition of velocity and acceleration; product rule for a scalar times a vector
> **Source:** Notes.pdf, Eq. 1.64; Notes.pdf, Eqs. 2.28-2.30; [Lecture 1, Slide 19]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(a\,\mathbf e_R + v_z t\,\mathbf e_z\right) \quad &\text{(definition of velocity)} \\
> &= \dot a\,\mathbf e_R + a\,\dot{\mathbf e}_R + v_z\,\mathbf e_z + v_z t\,\dot{\mathbf e}_z \quad &\text{(product rule, Eq. 1.64)} \\
> &= 0 + a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z + \mathbf 0 \quad &\text{($a$ constant; derivatives of the unit vectors)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z\right) \quad &\text{(definition of acceleration)} \\
> &= a\omega\,\dot{\mathbf e}_\theta + v_z\,\dot{\mathbf e}_z \quad &\text{(product rule; $a\omega$ and $v_z$ constant)} \\
> &= a\omega(-\omega\,\mathbf e_R) + \mathbf 0 \quad &\text{(derivatives of the unit vectors)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf e_R + v_z t\,\mathbf e_z, \qquad \mathbf v_0^P = a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z, \qquad \mathbf a_0^P = -a\omega^2\,\mathbf e_R}$$
>
> **Units:** $[a\omega] = [v_z] = [\mathrm{L\,T^{-1}}]$; $[a\omega^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** projecting the Cartesian result of part (a) on $\mathbf e_R$ gives the same centripetal acceleration; the cylindrical form shows at once that it has no $\mathbf e_\theta$ or $\mathbf e_z$ part.

#### (d) Modulus of the velocity

The speed is computed before part (c) because the intrinsic basis needs it.

> [!derivation] Speed of the rocket
> **Law:** modulus of a vector in an orthonormal basis
> **Source:** Notes.pdf, Eq. 1.40; Notes.pdf, Eq. 2.16
>
> $$\begin{aligned}
> v &= \sqrt{\mathbf v_0^P\cdot\mathbf v_0^P} \quad &\text{(definition of the modulus)} \\
> &= \sqrt{(a\omega)^2 + v_z^2} \quad &\text{(components $0$, $a\omega$, $v_z$ in the orthonormal $B_C$)}
> \end{aligned}$$
>
> $$\boxed{v = \dot s = \sqrt{a^2\omega^2 + v_z^2} \equiv V \quad (\text{constant})}$$
>
> **Units:** $\sqrt{[\mathrm{L\,T^{-1}}]^2} = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the rocket travels its path at a constant speed, the hypotenuse of the horizontal speed $a\omega$ and the vertical speed $v_z$.

#### (c) Intrinsic basis and the velocity and acceleration with $s$ and $\rho$

The unit tangent lies on the plane tangent to the cylinder; the figure folds that plane down onto the paper, with $\mathbf e_\theta$ to the right and $\mathbf e_z$ up.

![[attachments/EM-SOL/p01-tangent-plane.svg]]

> [!derivation] Unit tangent vector
> **Law:** the unit tangent is the derivative of the position with respect to the arc length; chain rule
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.16; [Lecture 1, Slide 25]
>
> $$\begin{aligned}
> \mathbf e_t &= \frac{d\mathbf r_0^P}{ds} = \frac{d\mathbf r_0^P}{dt}\,\frac{dt}{ds} \quad &\text{(Eq. 2.9 and chain rule)} \\
> &= \frac{\mathbf v_0^P}{V} \quad &\text{($ds/dt$ is the speed $V$)} \\
> &= \frac{a\omega}{V}\,\mathbf e_\theta + \frac{v_z}{V}\,\mathbf e_z \quad &\text{(velocity of part (b))} \\
> \cos\gamma &= \frac{a\omega}{V}, \quad \sin\gamma = \frac{v_z}{V} \quad &\text{(triangle: hypotenuse $V$, adjacent leg $a\omega$ on $\mathbf e_\theta$, opposite leg $v_z$ on $\mathbf e_z$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = \frac{a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z}{\sqrt{a^2\omega^2 + v_z^2}} = \cos\gamma\,\mathbf e_\theta + \sin\gamma\,\mathbf e_z}$$
>
> **Units:** $[a\omega]/[V] = [v_z]/[V] = 1$, a unit vector
> **Meaning:** the tangent climbs at the constant helix angle $\gamma$ above the horizontal direction $\mathbf e_\theta$.

> [!derivation] Principal normal and radius of curvature
> **Law:** definition of the normal vector and of the curvature
> **Source:** Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; [Lecture 1, Slide 26]
>
> $$\begin{aligned}
> \frac{d\mathbf e_t}{dt} &= \frac{a\omega}{V}\,\dot{\mathbf e}_\theta + \frac{v_z}{V}\,\dot{\mathbf e}_z \quad &\text{(product rule; $a\omega/V$ and $v_z/V$ constant)} \\
> &= \frac{a\omega}{V}(-\omega\,\mathbf e_R) + \mathbf 0 = -\frac{a\omega^2}{V}\,\mathbf e_R \quad &\text{(derivatives of the unit vectors)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{d\mathbf e_t}{dt}\,\frac{dt}{ds} = -\frac{a\omega^2}{V^2}\,\mathbf e_R \quad &\text{(chain rule, $dt/ds$ is $1/V$)} \\
> \frac{1}{\rho} &= \left|\frac{d\mathbf e_t}{ds}\right| = \frac{a\omega^2}{V^2} \quad &\text{(Eq. 2.12)} \\
> \rho &= \frac{a^2\omega^2 + v_z^2}{a\omega^2} = a + \frac{v_z^2}{a\omega^2} \quad &\text{(inverse; $V^2$ written out)} \\
> \mathbf e_n &= \frac{d\mathbf e_t/ds}{|d\mathbf e_t/ds|} = -\mathbf e_R \quad &\text{(Eq. 2.11)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_n = -\mathbf e_R, \qquad \rho = a + \frac{v_z^2}{a\omega^2}}$$
>
> **Units:** $[v_z^2]/[a\omega^2] = [\mathrm{L^2T^{-2}}]/[\mathrm{L\,T^{-2}}] = [\mathrm{L}]$
> **Meaning:** the normal points horizontally to the axis of the helix; the osculating circle is larger than the cylinder because the climb straightens the path.

> [!derivation] Binormal vector
> **Law:** the binormal completes a right-handed basis; vector product in an orthonormal right-handed basis
> **Source:** Notes.pdf, Eq. 2.13; Notes.pdf, Eq. 1.42; [Lecture 1, Slide 27]
>
> $$\begin{aligned}
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n = \frac{1}{V}\left(a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z\right)\times(-\mathbf e_R) \quad &\text{(definition of $\mathbf e_b$)} \\
> &= \frac{1}{V}\left(-a\omega\,(\mathbf e_\theta\times\mathbf e_R) - v_z\,(\mathbf e_z\times\mathbf e_R)\right) \quad &\text{(distributive property)} \\
> &= \frac{1}{V}\left(-a\omega\,(-\mathbf e_z) - v_z\,\mathbf e_\theta\right) \quad &\text{($\mathbf e_\theta\times\mathbf e_R = -\mathbf e_z$, $\mathbf e_z\times\mathbf e_R = \mathbf e_\theta$, cyclic order $R, \theta, z$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_b = \frac{-v_z\,\mathbf e_\theta + a\omega\,\mathbf e_z}{\sqrt{a^2\omega^2 + v_z^2}} = -\sin\gamma\,\mathbf e_\theta + \cos\gamma\,\mathbf e_z}$$
>
> **Units:** dimensionless, a unit vector
> **Meaning:** the binormal leans back from the vertical by the helix angle; it is constant in $B_C$ but turns with $\mathbf e_\theta$ in $S_0$.

> [!derivation] Change of basis from the cylindrical to the intrinsic basis
> **Law:** change of basis matrix (columns are the new vectors in the old basis); orthonormality
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.16
>
> $$\begin{aligned}
> \det[{}_CR_F] &= -(-1)\left(\frac{a\omega}{V}\frac{a\omega}{V} - \left(-\frac{v_z}{V}\right)\frac{v_z}{V}\right) \quad &\text{(expansion along row 1: only entry $-1$ at $(1,2)$, cofactor sign $-1$)} \\
> &= \frac{a^2\omega^2 + v_z^2}{V^2} = 1 \quad &\text{(definition of $V$)} \\
> (RR^T)_{11} &= 0 + 1 + 0 = 1 \quad &\text{(row 1 times row 1)} \\
> (RR^T)_{22} &= \frac{a^2\omega^2}{V^2} + 0 + \frac{v_z^2}{V^2} = 1 \quad &\text{(row 2 times row 2)} \\
> (RR^T)_{33} &= \frac{v_z^2}{V^2} + 0 + \frac{a^2\omega^2}{V^2} = 1 \quad &\text{(row 3 times row 3)} \\
> (RR^T)_{12} &= (RR^T)_{13} = 0 \quad &\text{(row 1 has its only entry where rows 2 and 3 have zero)} \\
> (RR^T)_{23} &= \frac{a\omega\,v_z}{V^2} + 0 - \frac{v_z\,a\omega}{V^2} = 0 \quad &\text{(row 2 times row 3)} \\
> \det[{}_0R_F] &= \det[{}_0R_C]\,\det[{}_CR_F] = 1 \quad &\text{(composition, Eq. 1.16)}
> \end{aligned}$$
>
> $$\boxed{[{}_CR_F] = \begin{pmatrix} 0 & -1 & 0 \\ a\omega/V & 0 & -v_z/V \\ v_z/V & 0 & a\omega/V \end{pmatrix}, \quad \det[{}_CR_F] = 1, \quad [{}_CR_F][{}_CR_F]^T = I}$$
>
> **Units:** dimensionless entries
> **Meaning:** $B_F$ is a proper orthonormal basis; it is $B_C$ turned so that its first vector follows the climbing tangent.

> [!derivation] Velocity and acceleration with $s$ and $\rho$ in the intrinsic basis
> **Law:** intrinsic components of velocity and acceleration
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.18; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot s\,\mathbf e_t \quad &\text{(Eq. 2.16)} \\
> \mathbf a_0^P &= \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n \quad &\text{(Eq. 2.17)} \\
> \ddot s &= \frac{dV}{dt} = 0 \quad &\text{($V$ constant)} \\
> \frac{\dot s^2}{\rho} &= \frac{V^2\,a\omega^2}{V^2} = a\omega^2 \quad &\text{($\rho$ of the normal box)} \\
> \mathbf a_0^P &= a\omega^2\,\mathbf e_n = -a\omega^2\,\mathbf e_R \quad &\text{(agrees with part (b))}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot s\,\mathbf e_t = V\,\mathbf e_t, \qquad \mathbf a_0^P = \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n = \frac{V^2}{\rho}\,\mathbf e_n = a\omega^2\,\mathbf e_n}$$
>
> **Units:** $[V^2/\rho] = [\mathrm{L^2T^{-2}}]/[\mathrm{L}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** no tangential acceleration (uniform speed): all the acceleration turns the velocity, and it has no binormal component, as Eq. 2.17 requires.

#### (e) and (f) Arc length and trajectory in terms of $s$

> [!derivation] Arc length as a function of time
> **Law:** the arc length is the integral of the speed
> **Source:** Notes.pdf, Eq. 2.16; [Lecture 1, Slide 24]
>
> $$\begin{aligned}
> s(t) &= \int_0^t \dot s\,dt' = \int_0^t V\,dt' \quad &\text{(origin of $s$ at $t = 0$)} \\
> &= V\left[t'\right]_0^t \quad &\text{(antiderivative of a constant)} \\
> &= V(t - 0) \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{s(t) = \sqrt{a^2\omega^2 + v_z^2}\;t}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** the distance along the helix grows linearly in time.

> [!derivation] Trajectory parametrised by the arc length
> **Law:** inversion of the time law and substitution in the parametric equations
> **Source:** Notes.pdf, Sec. 2.3; [Lecture 1, Slide 24]
>
> $$\begin{aligned}
> t &= \frac{s}{V} \quad &\text{(inverse of $s(t)$, $V \gt 0$)} \\
> x(s) &= a\cos\left(\frac{\omega s}{V}\right) \quad &\text{(substitution in Eq. (1))} \\
> y(s) &= a\sin\left(\frac{\omega s}{V}\right) \quad &\text{(substitution in Eq. (2))} \\
> z(s) &= \frac{v_z s}{V} \quad &\text{(substitution in Eq. (3))}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P(s) = a\cos\frac{\omega s}{\sqrt{a^2\omega^2+v_z^2}}\,\mathbf i_0 + a\sin\frac{\omega s}{\sqrt{a^2\omega^2+v_z^2}}\,\mathbf j_0 + \frac{v_z s}{\sqrt{a^2\omega^2+v_z^2}}\,\mathbf k_0}$$
>
> **Units:** $[\omega s/V] = [\mathrm{T^{-1}}][\mathrm{L}]/[\mathrm{L\,T^{-1}}] = 1$; $[v_z s/V] = [\mathrm{L}]$
> **Meaning:** the geometric curve, independent of how fast it is travelled; its derivative with respect to $s$ has unit modulus, as Eq. 2.9 requires.

#### (g) Centre of curvature at the point $(a, 0, 0)$

The meridian plane of $\mathbf i_0$ and $\mathbf k_0$ at that instant shows $P$, the normal and the centre $C$.

![[attachments/EM-SOL/p01-curvature-center.svg]]

> [!derivation] Centre of the osculating circle at $(a, 0, 0)$
> **Law:** the centre of curvature lies on the principal normal at distance $\rho$
> **Source:** Notes.pdf, Sec. 2.4; Notes.pdf, Eq. 2.12
>
> $$\begin{aligned}
> v_z t &= 0 \;\Rightarrow\; t = 0 \quad &\text{(the height of $(a,0,0)$ is zero; $v_z \gt 0$)} \\
> \mathbf r_0^P(0) &= a\,\mathbf i_0, \quad \mathbf e_R(0) = \mathbf i_0 \quad &\text{($\theta$ is zero)} \\
> \mathbf r_0^C &= \mathbf r_0^P + \rho\,\mathbf e_n \quad &\text{(Sec. 2.4)} \\
> &= a\,\mathbf i_0 + \left(a + \frac{v_z^2}{a\omega^2}\right)(-\mathbf i_0) \quad &\text{($\mathbf e_n$ is $-\mathbf e_R$)} \\
> &= -\frac{v_z^2}{a\omega^2}\,\mathbf i_0 \quad &\text{(the terms in $a$ cancel)}
> \end{aligned}$$
>
> $$\boxed{C = \left(-\frac{v_z^2}{a\omega^2},\ 0,\ 0\right)}$$
>
> **Units:** $[\mathrm{L^2T^{-2}}]/[\mathrm{L\,T^{-2}}] = [\mathrm{L}]$
> **Meaning:** the centre lies beyond the axis of the helix, on the opposite side from $P$, because the radius of curvature exceeds $a$.

### Answers and Checks

> [!derivation] Answers (a) to (g)
> **Law:** collection of the boxed results above
> **Source:** Notes.pdf, Eqs. 2.5-2.7; Notes.pdf, Eqs. 2.16-2.18; Notes.pdf, Eq. 2.28
>
> $$\begin{aligned}
> \text{(a)}\quad \mathbf r_0^P &= a\cos\omega t\,\mathbf i_0 + a\sin\omega t\,\mathbf j_0 + v_z t\,\mathbf k_0 \quad &\text{(Cartesian position)} \\
> \mathbf v_0^P &= -a\omega\sin\omega t\,\mathbf i_0 + a\omega\cos\omega t\,\mathbf j_0 + v_z\,\mathbf k_0 \quad &\text{(Cartesian velocity)} \\
> \mathbf a_0^P &= -a\omega^2\cos\omega t\,\mathbf i_0 - a\omega^2\sin\omega t\,\mathbf j_0 \quad &\text{(Cartesian acceleration)} \\
> \text{(b)}\quad \mathbf r_0^P &= a\,\mathbf e_R + v_z t\,\mathbf e_z,\ \ \mathbf v_0^P = a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z,\ \ \mathbf a_0^P = -a\omega^2\,\mathbf e_R \quad &\text{(cylindrical)} \\
> \text{(c)}\quad \mathbf v_0^P &= \dot s\,\mathbf e_t,\ \ \mathbf a_0^P = \frac{\dot s^2}{\rho}\,\mathbf e_n,\ \ \rho = a + \frac{v_z^2}{a\omega^2} \quad &\text{(intrinsic, $\ddot s$ is zero)} \\
> \text{(d)}\quad v &= \sqrt{a^2\omega^2 + v_z^2} \quad &\text{(speed)} \\
> \text{(e)}\quad s &= \sqrt{a^2\omega^2 + v_z^2}\;t \quad &\text{(time law)} \\
> \text{(g)}\quad C &= \left(-v_z^2/(a\omega^2),\,0,\,0\right) \quad &\text{(centre of curvature)}
> \end{aligned}$$
>
> $$\boxed{V = \sqrt{a^2\omega^2+v_z^2},\quad \rho = a + \frac{v_z^2}{a\omega^2},\quad s = Vt,\quad \mathbf r_0^P(s) = a\cos\tfrac{\omega s}{V}\,\mathbf i_0 + a\sin\tfrac{\omega s}{V}\,\mathbf j_0 + \tfrac{v_z s}{V}\,\mathbf k_0,\quad C = \left(-\tfrac{v_z^2}{a\omega^2}, 0, 0\right)}$$
>
> **Units:** every term checked in its own box: speeds $[\mathrm{L\,T^{-1}}]$, accelerations $[\mathrm{L\,T^{-2}}]$, lengths $[\mathrm{L}]$
> **Meaning:** a uniform helical motion: constant speed, constant curvature, acceleration always horizontal and toward the axis.

> [!derivation] Limiting cases
> **Law:** the general result must reduce to the known particular motions
> **Source:** Notes.pdf, Sec. 2.4; Notes.pdf, Eq. 2.12
>
> $$\begin{aligned}
> v_z \to 0:\quad \rho &\to a + 0 = a, \quad C \to (0, 0, 0) \quad &\text{(the helix flattens into the circle of radius $a$ centred on the axis)} \\
> \omega \to 0:\quad \frac{1}{\rho} &= \frac{a\omega^2}{a^2\omega^2 + v_z^2} \to 0 \quad &\text{(vertical straight ascent: zero curvature)} \\
> \text{independent check:}\quad |\mathbf v_0^P\times\mathbf a_0^P| &= |(a\omega\,\mathbf e_\theta + v_z\,\mathbf e_z)\times(-a\omega^2\,\mathbf e_R)| \quad &\text{(vector product of the results of part (b))} \\
> &= |a^2\omega^3\,\mathbf e_z - a\omega^2 v_z\,\mathbf e_\theta| = a\omega^2 V \quad &\text{($\mathbf e_\theta\times\mathbf e_R = -\mathbf e_z$, $\mathbf e_z\times\mathbf e_R = \mathbf e_\theta$)} \\
> \mathbf v_0^P\times\mathbf a_0^P &= \dot s\,\mathbf e_t\times\left(\ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n\right) \quad &\text{(velocity $\dot s\,\mathbf e_t$ and intrinsic acceleration, Notes.pdf Eq. 2.17)} \\
> &= \frac{\dot s^3}{\rho}\,\mathbf e_b \quad &\text{($\mathbf e_t\times\mathbf e_t = \mathbf 0$ and $\mathbf e_t\times\mathbf e_n = \mathbf e_b$)} \\
> \rho &= \frac{V^3}{|\mathbf v_0^P\times\mathbf a_0^P|} \quad &\text{(modulus of the previous row, with $\dot s = V$)} \\
> &= \frac{V^3}{a\omega^2 V} = \frac{V^2}{a\omega^2} \quad &\text{(the modulus found above)}
> \end{aligned}$$
>
> $$\boxed{v_z \to 0:\ \rho \to a,\ C \to O; \qquad \omega \to 0:\ \rho \to \infty; \qquad \frac{V^3}{|\mathbf v_0^P\times\mathbf a_0^P|} = \rho}$$
>
> **Units:** $[\mathrm{L^3T^{-3}}]/([\mathrm{L\,T^{-1}}][\mathrm{L\,T^{-2}}]) = [\mathrm{L}]$
> **Meaning:** both limits are the expected circle and straight line, and a second route to the radius of curvature gives the same value.

Check against the official key: the solution keys of Problems.pdf, p. 72 list Problem 1 with no answer, so there is no official result to compare with. The results are supported by the limiting cases and by the second computation of the radius of curvature in the box above.

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Helical trajectory of the rocket (Problem 01)", "intro": "Sample values: a = 1 m, ω = 2 rad/s, v_z = 0.5 m/s. The slider is the angle θ = ωt of the cylindrical coordinates, so the time is θ/ω; the default θ = 0 is the point (a, 0, 0) of part (g), reached at t = 0. The left view shows the helix, the position vector r, the intrinsic basis e_t, e_n, e_b and the cylindrical basis e_ρ, e_θ at the foot of P; the right view is the rotation of angle θ about k0 that takes B0 to the cylindrical basis. The readouts are the results of parts (a) to (g); the speed and the radius of curvature of the archetype below them are the same numbers, computed from the curve.", "params": {"curve": "helix", "R": 1.0, "b": 0.25, "rate": 2.0, "accel": 0, "umin": 0, "umax": 720, "extent": 2.6, "a": 1.0, "omega": 2.0, "vz": 0.5}, "defaults": {"u": 0}, "readouts": [{"label": "Time t = θ/ω", "expr": "u/omega", "unit": "s", "digits": 4}, {"label": "(a) Height z = v_z t", "expr": "vz*u/omega", "unit": "m", "digits": 4}, {"label": "(d) Speed V = √(a²ω² + v_z²)", "expr": "sqrt(a^2*omega^2 + vz^2)", "unit": "m/s", "digits": 4}, {"label": "(e) Arc length s = V t", "expr": "sqrt(a^2*omega^2 + vz^2)*u/omega", "unit": "m", "digits": 4}, {"label": "Angle γ of e_t above the horizontal, tan γ = v_z/(aω)", "expr": "deg(atan(vz/(a*omega)))", "unit": "deg", "digits": 2}, {"label": "(c) Radius of curvature ρ = a + v_z²/(aω²)", "expr": "a + vz^2/(a*omega^2)", "unit": "m", "digits": 4}, {"label": "(c) Normal acceleration V²/ρ = aω² (ṡ constant: no tangential part)", "expr": "a*omega^2", "unit": "m/s²", "digits": 4}, {"label": "(g) Centre of curvature at (a, 0, 0): x_C = −v_z²/(aω²)", "expr": "-vz^2/(a*omega^2)", "unit": "m", "digits": 4}]}

## Problem 02: Kinematics, Spiral

### Reference Frames, Bases and Coordinates

The particle $P$ moves on a given planar curve with a given angular law, so the motion is prescribed and the problem is purely kinematic (no forces section).

| Item | Definition |
| :--- | :--- |
| Fixed frame | $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ the pole of the spiral, the motion in the plane of $\mathbf i_0$ and $\mathbf j_0$, $\mathbf k_0$ normal to it |
| Polar basis | $B_C = \{\mathbf e_r, \mathbf e_\theta, \mathbf k_0\}$, $B_0$ turned by $\theta$ about $\mathbf k_0$ (cylindrical basis with $z = 0$, Notes.pdf, Eq. 2.24) |
| Intrinsic basis | $B_F = \{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ (Notes.pdf, Eq. 2.13) |
| Coordinates | polar radius $r$ and polar angle $\theta$, measured from $\mathbf i_0$ counterclockwise about $\mathbf k_0$ |
| Trajectory | $r = \alpha e^{\beta\theta}$ (logarithmic spiral) |
| Time law | $\theta = \delta t^n$ |
| Data | $\alpha$ [m], $\beta$ [1], $\delta$ [rad s$^{-n}$], $n$ [1], $t$ [s] |
| Hypotheses | $\alpha \gt 0$, $\delta \gt 0$, $n \gt 0$, $t \gt 0$ (so the angular rate is positive); $\beta \gt 0$ (the spiral opens as the angle grows; for $\beta \lt 0$ the same formulas hold with $\psi = \operatorname{arccot}\beta$ in $(0, \pi)$); $z = 0$ throughout |
| Degrees of freedom | 2 plane coordinates minus 1 relation (the spiral) leave 1; it is fixed by the time law |
| Notation | $\dot\theta$, $\ddot\theta$, $\dot r$, $\ddot r$ time derivatives; $v$ speed; $\rho$ radius of curvature |

### Change of Basis and Position Vector

The view along $\mathbf k_0$ (out of the paper) shows the rotation by $\theta$ from $B_0$ to the polar basis.

![[attachments/EM-SOL/p02-polar-rotation.svg]]

> [!derivation] Polar unit vectors and the change of basis matrix
> **Law:** components of a unit vector with a known angle; simple rotation about the third axis
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24; [Lecture 1, Slide 17]
>
> In the view of the figure $\mathbf k_0$ points out of the paper (⊙), $\mathbf i_0$ to the right, $\mathbf j_0$ up; a positive $\theta$ is counterclockwise by the right-hand rule about $\mathbf k_0$.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(hypotenuse 1; adjacent leg $\cos\theta$ on $\mathbf i_0$, opposite leg $\sin\theta$ on $\mathbf j_0$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(angle $\theta$ from $\mathbf j_0$: adjacent leg $\cos\theta$ on $\mathbf j_0$, opposite leg $\sin\theta$ toward $-\mathbf i_0$)} \\
> \det[{}_0R_C] &= 1\cdot(\cos^2\theta + \sin^2\theta) = 1 \quad &\text{(expansion along the third row $(0, 0, 1)$)} \\
> ([{}_0R_C][{}_0R_C]^T)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> ([{}_0R_C][{}_0R_C]^T)_{22} &= \sin^2\theta + \cos^2\theta = 1 \quad &\text{(row 2 times row 2)} \\
> ([{}_0R_C][{}_0R_C]^T)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_C][{}_0R_C]^T)_{13} &= ([{}_0R_C][{}_0R_C]^T)_{23} = 0,\ \ ([{}_0R_C][{}_0R_C]^T)_{33} = 1 \quad &\text{(third row and column are $(0, 0, 1)$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_C] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_C] = 1, \quad [{}_0R_C][{}_0R_C]^T = I}$$
>
> **Units:** dimensionless entries
> **Meaning:** the minus sign of the first component of $\mathbf e_\theta$ appears because, for $0 \lt \theta \lt \pi$, the vector turned a right angle counterclockwise from $\mathbf e_r$ points into the half-plane of negative $x$.

> [!derivation] Position vector on the spiral
> **Law:** position vector in polar components
> **Source:** Notes.pdf, Eq. 2.23; Notes.pdf, Eq. 2.28; [Lecture 1, Slide 12]
>
> $$\begin{aligned}
> \mathbf r_0^P &= r\cos\theta\,\mathbf i_0 + r\sin\theta\,\mathbf j_0 \quad &\text{(triangle: hypotenuse $r$, adjacent leg $x$, opposite leg $y$, Eq. 2.23)} \\
> &= r\left(\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0\right) = r\,\mathbf e_r \quad &\text{(first column of $[{}_0R_C]$)} \\
> r(t) &= \alpha e^{\beta\theta(t)} = \alpha e^{\beta\delta t^n} \quad &\text{(spiral with the time law substituted)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = \alpha e^{\beta\delta t^n}\,\mathbf e_r, \qquad \mathbf e_r = \cos(\delta t^n)\,\mathbf i_0 + \sin(\delta t^n)\,\mathbf j_0}$$
>
> **Units:** $[\alpha] = [\mathrm{L}]$; the exponent $\beta\delta t^n$ is dimensionless, as an exponent must be
> **Meaning:** the radius grows (for positive $\beta$) by the same factor every time $\theta$ advances by the same angle.

### Kinematics

> [!derivation] Rates of the coordinates
> **Law:** power rule and chain rule
> **Source:** Notes.pdf, Eq. 1.63; [Lecture 1, Slide 19]
>
> $$\begin{aligned}
> \dot\theta &= \frac{d}{dt}\left(\delta t^n\right) = n\delta t^{n-1} \quad &\text{(power rule)} \\
> \ddot\theta &= \frac{d}{dt}\left(n\delta t^{n-1}\right) = n(n-1)\delta t^{n-2} \quad &\text{(power rule)} \\
> \frac{dr}{d\theta} &= \frac{d}{d\theta}\left(\alpha e^{\beta\theta}\right) = \alpha\beta e^{\beta\theta} = \beta r \quad &\text{(derivative of the exponential, chain rule in $\beta\theta$)} \\
> \dot r &= \frac{dr}{d\theta}\,\dot\theta = \beta r\dot\theta \quad &\text{(chain rule, $r$ depends on $t$ through $\theta$)} \\
> \ddot r &= \beta\left(\dot r\,\dot\theta + r\,\ddot\theta\right) \quad &\text{(product rule on $\beta r\dot\theta$)} \\
> &= \beta\left(\beta r\dot\theta\cdot\dot\theta + r\ddot\theta\right) = \beta^2 r\dot\theta^2 + \beta r\ddot\theta \quad &\text{($\dot r$ substituted)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = n\delta t^{n-1},\quad \ddot\theta = n(n-1)\delta t^{n-2},\quad \dot r = \beta r\dot\theta,\quad \ddot r = \beta^2 r\dot\theta^2 + \beta r\ddot\theta}$$
>
> **Units:** $[\dot\theta] = [\mathrm{T^{-n}}][\mathrm{T^{n-1}}] = [\mathrm{T^{-1}}]$; $[\dot r] = [\mathrm{L\,T^{-1}}]$; $[\ddot r] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** on this spiral the radial rate is always the fraction $\beta$ of the transverse rate, whatever the time law.

> [!derivation] Time derivatives of the polar unit vectors
> **Law:** derivative of a rotating vector of constant modulus (Poisson)
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eqs. 2.25-2.26; [Lecture 1, Slide 10]
>
> $$\begin{aligned}
> \boldsymbol\omega_C &= \dot\theta\,\mathbf k_0 \quad &\text{(the polar basis turns about $\mathbf k_0$ at the rate of $\theta$)} \\
> \dot{\mathbf e}_r &= \dot\theta\,\mathbf k_0\times\left(\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0\right) \quad &\text{(Eq. 1.62)} \\
> &= \dot\theta\cos\theta\,\mathbf j_0 - \dot\theta\sin\theta\,\mathbf i_0 = \dot\theta\,\mathbf e_\theta \quad &\text{($\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k_0\times\left(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0\right) \quad &\text{(Eq. 1.62)} \\
> &= -\dot\theta\sin\theta\,\mathbf j_0 - \dot\theta\cos\theta\,\mathbf i_0 = -\dot\theta\,\mathbf e_r \quad &\text{(same vector products)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** each polar unit vector turns with the radius, perpendicular to itself.

#### (a) Radial and transverse components of the velocity

> [!derivation] Velocity in the polar basis
> **Law:** definition of velocity; product rule
> **Source:** Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 2.29; [Lecture 1, Slide 13]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(r\,\mathbf e_r\right) \quad &\text{(definition of velocity)} \\
> &= \dot r\,\mathbf e_r + r\,\dot{\mathbf e}_r \quad &\text{(product rule)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{(derivative of $\mathbf e_r$)} \\
> &= \beta r\dot\theta\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{(rate $\dot r$ of the spiral)} \\
> &= n\delta t^{n-1}\,\alpha e^{\beta\delta t^n}\left(\beta\,\mathbf e_r + \mathbf e_\theta\right) \quad &\text{($r$ and $\dot\theta$ substituted)}
> \end{aligned}$$
>
> $$\boxed{v_r = \beta r\dot\theta = \alpha\beta n\delta\,t^{n-1}e^{\beta\delta t^n}, \qquad v_\theta = r\dot\theta = \alpha n\delta\,t^{n-1}e^{\beta\delta t^n}}$$
>
> **Units:** $[\mathrm{L}][\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$ for both
> **Meaning:** the ratio of radial to transverse velocity is the constant $\beta$: the velocity always makes the same angle with the radius.

#### (b) Radial and transverse components of the acceleration

> [!derivation] Acceleration in the polar basis
> **Law:** definition of acceleration; product rule
> **Source:** Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 2.30; [Lecture 1, Slide 19]
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta\right) \quad &\text{(definition of acceleration)} \\
> &= \ddot r\,\mathbf e_r + \dot r\,\dot{\mathbf e}_r + (\dot r\dot\theta + r\ddot\theta)\,\mathbf e_\theta + r\dot\theta\,\dot{\mathbf e}_\theta \quad &\text{(product rule on each term)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + (\dot r\dot\theta + r\ddot\theta)\,\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivatives of the unit vectors)} \\
> &= (\ddot r - r\dot\theta^2)\,\mathbf e_r + (r\ddot\theta + 2\dot r\dot\theta)\,\mathbf e_\theta \quad &\text{(grouping by unit vector)} \\
> a_r &= \beta^2 r\dot\theta^2 + \beta r\ddot\theta - r\dot\theta^2 = (\beta^2 - 1)r\dot\theta^2 + \beta r\ddot\theta \quad &\text{($\ddot r$ of the rates box)} \\
> a_\theta &= r\ddot\theta + 2\beta r\dot\theta\cdot\dot\theta = r\ddot\theta + 2\beta r\dot\theta^2 \quad &\text{($\dot r$ of the rates box)} \\
> a_r &= r\left[(\beta^2-1)n^2\delta^2t^{2n-2} + \beta n(n-1)\delta t^{n-2}\right] \quad &\text{($\dot\theta^2$ and $\ddot\theta$ substituted)} \\
> &= n\delta t^{n-2}\,r\left[(\beta^2-1)n\delta t^n + \beta(n-1)\right] \quad &\text{(common factor $n\delta t^{n-2}$, since $t^{2n-2} = t^{n-2}t^n$)} \\
> a_\theta &= n\delta t^{n-2}\,r\left[(n-1) + 2\beta n\delta t^n\right] \quad &\text{(same substitution and factor)}
> \end{aligned}$$
>
> $$\boxed{a_r = n\delta t^{n-2}\,\alpha e^{\beta\delta t^n}\left[(\beta^2-1)n\delta t^n + \beta(n-1)\right], \qquad a_\theta = n\delta t^{n-2}\,\alpha e^{\beta\delta t^n}\left[2\beta n\delta t^n + (n-1)\right]}$$
>
> **Units:** $[\delta t^{n-2}] = [\mathrm{T^{-2}}]$, $[\delta t^n] = 1$, so both are $[\mathrm{L\,T^{-2}}]$
> **Meaning:** for uniform rotation ($n$ equal to one) the bracket loses its constant term and the acceleration is set only by the square of the angular rate.

#### (c) Tangential and normal components of the velocity

The unit tangent makes a constant angle with $\mathbf e_r$; the fold-down triangle of the velocity gives its components.

![[attachments/EM-SOL/p02-tangent-triangle.svg]]

> [!derivation] Speed and unit tangent
> **Law:** the velocity is tangent to the path; unit tangent as the derivative with respect to the arc length
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.16; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> v &= \sqrt{v_r^2 + v_\theta^2} = \sqrt{\beta^2 r^2\dot\theta^2 + r^2\dot\theta^2} \quad &\text{(modulus in the orthonormal polar basis)} \\
> &= r\dot\theta\sqrt{1+\beta^2} \quad &\text{($r \gt 0$ and $\dot\theta \gt 0$ for $t \gt 0$)} \\
> \mathbf e_t &= \frac{\mathbf v_0^P}{\dot s} = \frac{r\dot\theta(\beta\,\mathbf e_r + \mathbf e_\theta)}{r\dot\theta\sqrt{1+\beta^2}} \quad &\text{(Eq. 2.16; $\dot s$ is $v$ because $s$ grows with $t$)} \\
> &= \cos\psi\,\mathbf e_r + \sin\psi\,\mathbf e_\theta \quad &\text{(triangle: hypotenuse $\sqrt{1+\beta^2}$, adjacent leg $\beta$ on $\mathbf e_r$, opposite leg 1 on $\mathbf e_\theta$)} \\
> \tan\psi &= \frac{1}{\beta} \quad &\text{(opposite over adjacent: constant angle $\psi$ between radius and tangent)}
> \end{aligned}$$
>
> $$\boxed{v_t = v = n\delta t^{n-1}\,\alpha e^{\beta\delta t^n}\sqrt{1+\beta^2}, \qquad v_n = 0, \qquad \mathbf e_t = \frac{\beta\,\mathbf e_r + \mathbf e_\theta}{\sqrt{1+\beta^2}}}$$
>
> **Units:** $[v] = [\mathrm{L\,T^{-1}}]$; $\mathbf e_t$ dimensionless
> **Meaning:** the velocity has no normal component, as for every motion (Eq. 2.16); the angle between the radius and the tangent never changes, which is why the curve is called equiangular.

> [!derivation] Principal normal, binormal and radius of curvature
> **Law:** definition of the normal vector and of the curvature; binormal completes the right-handed basis
> **Source:** Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; Notes.pdf, Eq. 2.13; [Lecture 1, Slide 26]
>
> $$\begin{aligned}
> \frac{d\mathbf e_t}{dt} &= \frac{\beta\,\dot{\mathbf e}_r + \dot{\mathbf e}_\theta}{\sqrt{1+\beta^2}} \quad &\text{(the coefficients are constant)} \\
> &= \frac{\beta\dot\theta\,\mathbf e_\theta - \dot\theta\,\mathbf e_r}{\sqrt{1+\beta^2}} = \dot\theta\,\frac{-\mathbf e_r + \beta\,\mathbf e_\theta}{\sqrt{1+\beta^2}} \quad &\text{(derivatives of the unit vectors)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{d\mathbf e_t}{dt}\,\frac{1}{\dot s} = \frac{\dot\theta}{r\dot\theta\sqrt{1+\beta^2}}\,\frac{-\mathbf e_r + \beta\,\mathbf e_\theta}{\sqrt{1+\beta^2}} \quad &\text{(chain rule)} \\
> \frac{1}{\rho} &= \left|\frac{d\mathbf e_t}{ds}\right| = \frac{1}{r\sqrt{1+\beta^2}} \quad &\text{(Eq. 2.12; the last fraction is a unit vector)} \\
> \mathbf e_n &= \frac{-\mathbf e_r + \beta\,\mathbf e_\theta}{\sqrt{1+\beta^2}} \quad &\text{(Eq. 2.11; $\dot\theta \gt 0$ keeps the sense)} \\
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n = \frac{(\beta\,\mathbf e_r + \mathbf e_\theta)\times(-\mathbf e_r + \beta\,\mathbf e_\theta)}{1+\beta^2} \quad &\text{(definition)} \\
> &= \frac{\beta^2\,\mathbf e_r\times\mathbf e_\theta - \mathbf e_\theta\times\mathbf e_r}{1+\beta^2} = \frac{(\beta^2 + 1)\,\mathbf k_0}{1+\beta^2} = \mathbf k_0 \quad &\text{($\mathbf e_r\times\mathbf e_\theta = \mathbf k_0$, parallel products vanish)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_n = \frac{-\mathbf e_r + \beta\,\mathbf e_\theta}{\sqrt{1+\beta^2}}, \qquad \mathbf e_b = \mathbf k_0, \qquad \rho = r\sqrt{1+\beta^2} = \alpha e^{\beta\delta t^n}\sqrt{1+\beta^2}}$$
>
> **Units:** $[\rho] = [\mathrm{L}]$
> **Meaning:** $\mathbf e_n$ is $\mathbf e_t$ turned a right angle counterclockwise: the particle turns to its left, about $\mathbf k_0$, as $\theta$ grows.

> [!derivation] Change of basis from the polar to the intrinsic basis
> **Law:** simple rotation about the third axis; orthonormality of a change of basis matrix
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.15
>
> Seen along $\mathbf k_0$ (⊙), $B_F$ is $B_C$ turned counterclockwise by the constant angle $\psi$; the minus sign of the first component of $\mathbf e_n$ comes from the same right-hand rule as the minus sign of $\mathbf e_\theta$.
>
> $$\begin{aligned}
> \cos\psi &= \frac{\beta}{\sqrt{1+\beta^2}}, \quad \sin\psi = \frac{1}{\sqrt{1+\beta^2}} \quad &\text{(triangle of the tangent: adjacent $\beta$, opposite 1, hypotenuse $\sqrt{1+\beta^2}$)} \\
> \det[{}_CR_F] &= 1\cdot\left(\frac{\beta\cdot\beta}{1+\beta^2} - \frac{(-1)\cdot 1}{1+\beta^2}\right) = \frac{\beta^2 + 1}{1+\beta^2} = 1 \quad &\text{(expansion along the third row)} \\
> (RR^T)_{11} &= \frac{\beta^2 + 1}{1+\beta^2} = 1, \quad (RR^T)_{22} = \frac{1 + \beta^2}{1+\beta^2} = 1 \quad &\text{(rows times themselves)} \\
> (RR^T)_{12} &= \frac{\beta\cdot 1 + (-1)\cdot\beta}{1+\beta^2} = 0 \quad &\text{(row 1 times row 2)}
> \end{aligned}$$
>
> $$\boxed{[{}_CR_F] = \frac{1}{\sqrt{1+\beta^2}}\begin{pmatrix} \beta & -1 & 0 \\ 1 & \beta & 0 \\ 0 & 0 & \sqrt{1+\beta^2} \end{pmatrix}, \quad \det[{}_CR_F] = 1, \quad [{}_CR_F][{}_CR_F]^T = I}$$
>
> **Units:** dimensionless entries
> **Meaning:** the intrinsic basis is rigidly attached to the polar basis at the fixed angle $\psi$: a property of the logarithmic spiral alone.

#### (d) Tangential and normal components of the acceleration

> [!derivation] Intrinsic components of the acceleration
> **Law:** tangential and normal acceleration
> **Source:** Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.18; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> a_t &= \ddot s = \frac{d}{dt}\left(\sqrt{1+\beta^2}\,r\dot\theta\right) \quad &\text{(Eq. 2.18)} \\
> &= \sqrt{1+\beta^2}\left(\dot r\dot\theta + r\ddot\theta\right) \quad &\text{(product rule)} \\
> &= \sqrt{1+\beta^2}\,r\left(\beta\dot\theta^2 + \ddot\theta\right) \quad &\text{($\dot r$ is $\beta r\dot\theta$)} \\
> &= \sqrt{1+\beta^2}\,n\delta t^{n-2}\,r\left[\beta n\delta t^n + (n-1)\right] \quad &\text{(rates substituted; factor $n\delta t^{n-2}$)} \\
> a_n &= \frac{\dot s^2}{\rho} = \frac{r^2\dot\theta^2(1+\beta^2)}{r\sqrt{1+\beta^2}} \quad &\text{(Eq. 2.18 with $\rho$ of part (c))} \\
> &= \sqrt{1+\beta^2}\,r\dot\theta^2 = \sqrt{1+\beta^2}\,n^2\delta^2t^{2n-2}\,r \quad &\text{(simplification)}
> \end{aligned}$$
>
> $$\boxed{a_t = \sqrt{1+\beta^2}\,n\delta t^{n-2}\,\alpha e^{\beta\delta t^n}\left[\beta n\delta t^n + n - 1\right], \qquad a_n = \sqrt{1+\beta^2}\,n^2\delta^2t^{2n-2}\,\alpha e^{\beta\delta t^n}}$$
>
> **Units:** $[\delta^2t^{2n-2}] = [\mathrm{T^{-2}}]$, so both are $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the normal acceleration is always positive (the path always bends to the same side); the tangential one changes the speed both because the radius grows and because the angular rate changes.

> [!derivation] Projection check of the intrinsic components
> **Law:** components of a vector by the dot product with the unit vectors
> **Source:** Notes.pdf, Eq. 1.28; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\mathbf e_t &= \frac{\beta a_r + a_\theta}{\sqrt{1+\beta^2}} \quad &\text{(components in the orthonormal polar basis)} \\
> &= \frac{\beta(\beta^2-1)r\dot\theta^2 + \beta^2 r\ddot\theta + 2\beta r\dot\theta^2 + r\ddot\theta}{\sqrt{1+\beta^2}} \quad &\text{($a_r$ and $a_\theta$ of part (b))} \\
> &= \frac{(1+\beta^2)\left(\beta r\dot\theta^2 + r\ddot\theta\right)}{\sqrt{1+\beta^2}} \quad &\text{(common factor $1+\beta^2$)} \\
> \mathbf a_0^P\cdot\mathbf e_n &= \frac{-a_r + \beta a_\theta}{\sqrt{1+\beta^2}} \quad &\text{(same rule)} \\
> &= \frac{-(\beta^2-1)r\dot\theta^2 - \beta r\ddot\theta + \beta r\ddot\theta + 2\beta^2 r\dot\theta^2}{\sqrt{1+\beta^2}} = \frac{(1+\beta^2)r\dot\theta^2}{\sqrt{1+\beta^2}} \quad &\text{(the $\ddot\theta$ terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P\cdot\mathbf e_t = \sqrt{1+\beta^2}\,r(\beta\dot\theta^2 + \ddot\theta) = a_t, \qquad \mathbf a_0^P\cdot\mathbf e_n = \sqrt{1+\beta^2}\,r\dot\theta^2 = a_n}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** projecting the polar acceleration of part (b) gives the same intrinsic components as Eq. 2.17: the two routes agree.

#### (e) Radius of curvature and centre of curvature

The main plane shows the spiral, the polar and intrinsic bases at $P$ and the centre of curvature $C$.

![[attachments/EM-SOL/p02-spiral-plane.svg]]

> [!derivation] Radius of curvature and its centre
> **Law:** definition of curvature; the centre of curvature lies on the normal at distance $\rho$
> **Source:** Notes.pdf, Eq. 2.12; Notes.pdf, Sec. 2.4
>
> $$\begin{aligned}
> \rho &= r\sqrt{1+\beta^2} \quad &\text{(normal box of part (c))} \\
> \mathbf r_0^C &= \mathbf r_0^P + \rho\,\mathbf e_n \quad &\text{(Sec. 2.4)} \\
> &= r\,\mathbf e_r + r\sqrt{1+\beta^2}\,\frac{-\mathbf e_r + \beta\,\mathbf e_\theta}{\sqrt{1+\beta^2}} \quad &\text{(substitution)} \\
> &= r\,\mathbf e_r - r\,\mathbf e_r + \beta r\,\mathbf e_\theta = \beta r\,\mathbf e_\theta \quad &\text{(the radial terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\rho = r\sqrt{1+\beta^2} = \alpha\sqrt{1+\beta^2}\,e^{\beta\delta t^n}, \qquad \mathbf r_0^C = \beta r\,\mathbf e_\theta}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the triangle $OPC$ has a right angle at $O$ (the segment $OC$ lies along $\mathbf e_\theta$, the segment $OP$ along $\mathbf e_r$): its legs are $r$ and the modulus of $\beta r$, and its hypotenuse $PC$ is $\rho$. The radius of curvature depends only on the shape, not on $\delta$ or $n$.

### Answers and Checks

> [!derivation] Answers (a) to (e)
> **Law:** collection of the boxed results, with $r = \alpha e^{\beta\delta t^n}$
> **Source:** Notes.pdf, Eqs. 2.29-2.30; Notes.pdf, Eqs. 2.16-2.18
>
> $$\begin{aligned}
> \text{(a)}\quad v_r &= \beta n\delta t^{n-1}\,r, \quad v_\theta = n\delta t^{n-1}\,r \quad &\text{(polar velocity)} \\
> \text{(b)}\quad a_r &= n\delta t^{n-2}\,r\left[(\beta^2-1)n\delta t^n + \beta(n-1)\right], \quad a_\theta = n\delta t^{n-2}\,r\left[2\beta n\delta t^n + n - 1\right] \quad &\text{(polar acceleration)} \\
> \text{(c)}\quad v_t &= \sqrt{1+\beta^2}\,n\delta t^{n-1}\,r, \quad v_n = 0 \quad &\text{(intrinsic velocity)} \\
> \text{(d)}\quad a_t &= \sqrt{1+\beta^2}\,n\delta t^{n-2}\,r\left[\beta n\delta t^n + n - 1\right], \quad a_n = \sqrt{1+\beta^2}\,n^2\delta^2 t^{2n-2}\,r \quad &\text{(intrinsic acceleration)} \\
> \text{(e)}\quad \rho &= r\sqrt{1+\beta^2} \quad &\text{(radius of curvature)}
> \end{aligned}$$
>
> $$\boxed{v_t = \sqrt{1+\beta^2}\,r\dot\theta,\quad v_n = 0,\quad a_t = \sqrt{1+\beta^2}\,r(\beta\dot\theta^2 + \ddot\theta),\quad a_n = \sqrt{1+\beta^2}\,r\dot\theta^2,\quad \rho = \alpha\sqrt{1+\beta^2}\,e^{\beta\delta t^n}}$$
>
> **Units:** velocities $[\mathrm{L\,T^{-1}}]$, accelerations $[\mathrm{L\,T^{-2}}]$, $\rho$ in $[\mathrm{L}]$
> **Meaning:** every component is proportional to the current radius: the spiral is self-similar.

> [!derivation] Limiting cases
> **Law:** the general result must reduce to the known particular motions
> **Source:** Notes.pdf, Eq. 2.30; Notes.pdf, Eq. 2.12
>
> $$\begin{aligned}
> \beta \to 0:\quad r &\to \alpha, \quad \rho \to \alpha, \quad v_r \to 0 \quad &\text{(the spiral becomes the circle of radius $\alpha$)} \\
> \beta \to 0:\quad a_r &\to -r\dot\theta^2, \quad a_\theta \to r\ddot\theta \quad &\text{(centripetal and angular acceleration of circular motion)} \\
> n = 1:\quad \ddot\theta &= 0, \quad a_t = \sqrt{1+\beta^2}\,\beta r\delta^2 \quad &\text{(uniform rotation: the speed still grows, with $r$)} \\
> \text{independent check:}\quad \frac{v^2}{a_n} &= \frac{(1+\beta^2)r^2\dot\theta^2}{\sqrt{1+\beta^2}\,r\dot\theta^2} = r\sqrt{1+\beta^2} \quad &\text{($\rho$ from Eq. 2.18 with $a_n$ from the projection box)}
> \end{aligned}$$
>
> $$\boxed{\beta \to 0:\ \rho \to \alpha,\ a_r \to -r\dot\theta^2; \qquad \frac{v^2}{\mathbf a_0^P\cdot\mathbf e_n} = r\sqrt{1+\beta^2} = \rho}$$
>
> **Units:** $[\mathrm{L}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the circle is recovered, and the radius of curvature found from the geometry (Eq. 2.12) matches the one found from the projected acceleration.

Check against the official key: the solution keys of Problems.pdf, p. 72 list Problem 2 with no answer, so there is no official result to compare with. The results are supported by the limiting cases and by the two independent routes to the intrinsic components (time derivative of the speed and projection of the polar acceleration).

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Particle on the logarithmic spiral (Problem 02)", "intro": "Sample values: α = 1 m, β = 0.15, δ = 1 rad/s and n = 1 (the archetype turns the radius at a constant angular rate, so the time law θ = δtⁿ is taken with n = 1; the readouts keep n as in the solution). The slider is the polar angle θ, and the time is t = (θ/δ)^(1/n); the default is the sample angle θ = 300°. The left view shows the spiral, r, the polar basis e_ρ, e_θ at P and the intrinsic basis e_t, e_n; the right view is the rotation of angle θ about k0 that takes B0 to the polar basis. The readouts are the components of parts (a) to (e).", "params": {"curve": "logspiral", "a": 1.0, "c": 0.15, "rate": 1.0, "accel": 0, "umin": 10, "umax": 540, "extent": 4.6, "delta": 1.0, "n": 1.0}, "defaults": {"u": 300}, "view": "top", "sliders": {"u": {"label": "Polar angle θ"}}, "readouts": [{"label": "Time t = (θ/δ)^(1/n)", "expr": "((u/delta)^(1/n))", "unit": "s", "digits": 4}, {"label": "r = α e^(βθ)", "expr": "a*exp(c*u)", "unit": "m", "digits": 4}, {"label": "(a) v_r = β n δ t^(n−1) r", "expr": "c*n*delta*((u/delta)^(1/n))^(n - 1)*a*exp(c*u)", "unit": "m/s", "digits": 4}, {"label": "(a) v_θ = n δ t^(n−1) r", "expr": "n*delta*((u/delta)^(1/n))^(n - 1)*a*exp(c*u)", "unit": "m/s", "digits": 4}, {"label": "(b) a_r = n δ t^(n−2) r [(β² − 1) n δ tⁿ + β(n − 1)]", "expr": "n*delta*((u/delta)^(1/n))^(n - 2)*a*exp(c*u)*((c^2 - 1)*n*delta*((u/delta)^(1/n))^n + c*(n - 1))", "unit": "m/s²", "digits": 4}, {"label": "(b) a_θ = n δ t^(n−2) r [2β n δ tⁿ + n − 1]", "expr": "n*delta*((u/delta)^(1/n))^(n - 2)*a*exp(c*u)*(2*c*n*delta*((u/delta)^(1/n))^n + n - 1)", "unit": "m/s²", "digits": 4}, {"label": "(c) v_t = √(1 + β²) n δ t^(n−1) r (v_n is zero)", "expr": "sqrt(1 + c^2)*n*delta*((u/delta)^(1/n))^(n - 1)*a*exp(c*u)", "unit": "m/s", "digits": 4}, {"label": "(d) a_t = √(1 + β²) n δ t^(n−2) r [β n δ tⁿ + n − 1]", "expr": "sqrt(1 + c^2)*n*delta*((u/delta)^(1/n))^(n - 2)*a*exp(c*u)*(c*n*delta*((u/delta)^(1/n))^n + n - 1)", "unit": "m/s²", "digits": 4}, {"label": "(d) a_n = √(1 + β²) n² δ² t^(2n−2) r", "expr": "sqrt(1 + c^2)*n^2*delta^2*((u/delta)^(1/n))^(2*n - 2)*a*exp(c*u)", "unit": "m/s²", "digits": 4}, {"label": "(e) Radius of curvature ρ = r √(1 + β²)", "expr": "a*exp(c*u)*sqrt(1 + c^2)", "unit": "m", "digits": 4}, {"label": "Angle ψ from e_r to e_t, cot ψ = β", "expr": "deg(atan(1/c))", "unit": "deg", "digits": 2}]}

## Problem 03: Kinematics, Astroid

### Reference Frames, Bases and Coordinates

The particle $P$ moves on a given planar curve with a given tangential acceleration. The only unknown is the time law along the curve, so the problem is kinematic (no forces section): the position follows from integrating the motion along the path.

| Item | Definition |
| :--- | :--- |
| Fixed frame | $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ the centre of the astroid, the curve in the plane of $\mathbf i_0$ and $\mathbf j_0$, $\mathbf k_0$ normal to it |
| Intrinsic basis | $B_F = \{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ (Notes.pdf, Eq. 2.13) |
| Trajectory | $x = a\cos^3\phi$, $y = a\sin^3\phi$ (statement); $\phi$ is a parameter of the curve, not the polar angle of $P$ |
| Polar angle of $P$ | $\vartheta$, measured from $\mathbf i_0$ counterclockwise, with $\tan\vartheta = y/x$ |
| Arc length | $s$, measured along the curve from the cusp $(a, 0)$ at $\phi = 0$ |
| Tangential acceleration | $a_t = \ddot s = k$, constant (statement) |
| Initial conditions | at $t = 0$: $\phi = 0$ (so $s = 0$) and rest (so $\dot s = 0$) |
| Data | $a$ [m], $k$ [m s$^{-2}$], $t$ [s] |
| Hypotheses | $a \gt 0$, $k \gt 0$; the particle leaves the cusp $(a, 0)$ along the first-quadrant arc, with $0 \le \phi \le \pi/2$ and $\phi$ growing (the smooth segment between the cusps $(a, 0)$ and $(0, a)$); $s$ grows with $\phi$ |
| Degrees of freedom | 2 plane coordinates minus 1 relation (the curve) leave 1, the arc length $s$; the time law $s(t)$ is the unknown |

### Change of Basis and Position Vector

The main plane shows the astroid, the smooth arc used, and the position vector of $P$ built from its two projections.

![[attachments/EM-SOL/p03-astroid-plane.svg]]

> [!derivation] Position vector on the astroid
> **Law:** position vector in Cartesian components
> **Source:** Notes.pdf, Eq. 2.5; [Lecture 1, Slide 16]
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i_0 + y\,\mathbf j_0 \quad &\text{(Eq. 2.5, plane motion: $z$ is zero)} \\
> &= a\cos^3\phi\,\mathbf i_0 + a\sin^3\phi\,\mathbf j_0 \quad &\text{(statement)} \\
> \phi = 0:\quad \mathbf r_0^P &= a\,\mathbf i_0 \quad &\text{($\cos 0$ is 1, $\sin 0$ is 0: start cusp)} \\
> \phi = \tfrac{\pi}{2}:\quad \mathbf r_0^P &= a\,\mathbf j_0 \quad &\text{(end cusp of the smooth arc)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P(\phi) = a\cos^3\phi\,\mathbf i_0 + a\sin^3\phi\,\mathbf j_0, \qquad 0 \le \phi \le \frac{\pi}{2}}$$
>
> **Units:** $[a] = [\mathrm{L}]$; powers of cosines and sines are dimensionless
> **Meaning:** the horizontal projection $a\cos^3\phi$ and the vertical projection $a\sin^3\phi$ are the legs of the right triangle whose hypotenuse is the segment $OP$.

The parameter is related to the polar angle through an auxiliary circle of radius $a$.

![[attachments/EM-SOL/p03-parameter-angle.svg]]

> [!derivation] Parameter of the curve and polar angle of the particle
> **Law:** polar angle of a point from its Cartesian coordinates
> **Source:** Notes.pdf, Eq. 2.23; Notes.pdf, Eq. 1.3
>
> $$\begin{aligned}
> \tan\vartheta &= \frac{y}{x} \quad &\text{(triangle $OP$: opposite leg $y$, adjacent leg $x$, Eq. 2.23)} \\
> &= \frac{a\sin^3\phi}{a\cos^3\phi} = \tan^3\phi \quad &\text{(statement)} \\
> \phi = 0,\ \tfrac{\pi}{4},\ \tfrac{\pi}{2}:\quad \tan^3\phi &= \tan\phi \quad &\text{($\tan\phi$ is 0, 1 or unbounded)}
> \end{aligned}$$
>
> $$\boxed{\tan\vartheta = \tan^3\phi, \qquad \vartheta = \phi \text{ only at } \phi = 0,\ \tfrac{\pi}{4},\ \tfrac{\pi}{2}}$$
>
> **Units:** dimensionless
> **Meaning:** $\phi$ is the angle of the point $(a\cos\phi, a\sin\phi)$ of the auxiliary circle, not the direction of $OP$; between the cusps $P$ is seen at a polar angle smaller than $\phi$ for $\phi \lt \pi/4$ and larger beyond.

### Kinematics

#### Arc element and arc length along the smooth arc

The fold-down of the arc element shows the right triangle of the hint: the legs are the changes of $x$ and $y$, the hypotenuse is the arc element.

![[attachments/EM-SOL/p03-arc-element.svg]]

> [!derivation] Derivatives of the coordinates with respect to the parameter
> **Law:** chain rule
> **Source:** Notes.pdf, Eq. 1.63; [Lecture 1, Slide 24]
>
> $$\begin{aligned}
> \frac{dx}{d\phi} &= 3a\cos^2\phi\,\frac{d(\cos\phi)}{d\phi} \quad &\text{(chain rule on the cube, $u$ is $\cos\phi$)} \\
> &= -3a\cos^2\phi\sin\phi \quad &\text{(derivative of the cosine)} \\
> \frac{dy}{d\phi} &= 3a\sin^2\phi\,\frac{d(\sin\phi)}{d\phi} \quad &\text{(chain rule on the cube, $u$ is $\sin\phi$)} \\
> &= 3a\sin^2\phi\cos\phi \quad &\text{(derivative of the sine)}
> \end{aligned}$$
>
> $$\boxed{dx = -3a\cos^2\phi\sin\phi\,d\phi, \qquad dy = 3a\sin^2\phi\cos\phi\,d\phi}$$
>
> **Units:** $[\mathrm{L}]$ per radian
> **Meaning:** on the arc, $x$ decreases and $y$ increases as $\phi$ grows: the particle moves up and to the left.

> [!derivation] Arc element
> **Law:** arc length of a plane curve (hint of the statement: Pythagoras on the infinitesimal triangle)
> **Source:** Notes.pdf, Eq. 2.19; Problems.pdf, p. 6
>
> $$\begin{aligned}
> ds^2 &= dx^2 + dy^2 \quad &\text{(hypotenuse $ds$, legs $dx$ and $dy$)} \\
> &= 9a^2\cos^4\phi\sin^2\phi\,d\phi^2 + 9a^2\sin^4\phi\cos^2\phi\,d\phi^2 \quad &\text{(squares of the differentials)} \\
> &= 9a^2\cos^2\phi\sin^2\phi\left(\cos^2\phi + \sin^2\phi\right)d\phi^2 \quad &\text{(common factor $9a^2\cos^2\phi\sin^2\phi$)} \\
> &= 9a^2\cos^2\phi\sin^2\phi\,d\phi^2 \quad &\text{(Pythagorean identity)} \\
> ds &= 3a\sin\phi\cos\phi\,d\phi \quad &\text{(positive root: $\sin\phi$, $\cos\phi \ge 0$ on the arc and $s$ grows with $\phi$)}
> \end{aligned}$$
>
> $$\boxed{\frac{ds}{d\phi} = 3a\sin\phi\cos\phi \ge 0, \qquad 0 \le \phi \le \frac{\pi}{2}}$$
>
> **Units:** $[\mathrm{L}]$ per radian
> **Meaning:** the rate of arc length per unit of parameter vanishes at both cusps, where the curve stops and turns back sharply.

> [!derivation] Arc length as a function of the parameter
> **Law:** integration of the arc element with a substitution and Barrow's rule
> **Source:** Notes.pdf, Sec. 2.3; [Lecture 1, Slide 24]
>
> $$\begin{aligned}
> s(\phi) &= \int_0^\phi 3a\sin u\cos u\,du \quad &\text{(origin of $s$ at the start cusp)} \\
> w &= \sin u, \quad dw = \cos u\,du \quad &\text{(substitution and its differential)} \\
> u = 0 \Rightarrow w = 0, \quad u &= \phi \Rightarrow w = \sin\phi \quad &\text{(new limits)} \\
> s(\phi) &= 3a\int_0^{\sin\phi} w\,dw = 3a\left[\frac{w^2}{2}\right]_0^{\sin\phi} \quad &\text{(antiderivative of $w$)} \\
> &= 3a\left(\frac{\sin^2\phi}{2} - 0\right) \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{s(\phi) = \frac{3a}{2}\sin^2\phi, \qquad s\!\left(\tfrac{\pi}{2}\right) = \frac{3a}{2}}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the smooth arc between two cusps has length one and a half times $a$; the whole astroid has four of them.

#### Intrinsic basis

The view along $\mathbf k_0$ (out of the paper) shows the intrinsic basis turned with respect to the fixed one.

![[attachments/EM-SOL/p03-intrinsic-rotation.svg]]

> [!derivation] Unit tangent, principal normal and radius of curvature
> **Law:** unit tangent and normal as derivatives with respect to the arc length; curvature
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; [Lecture 1, Slides 25-26]
>
> $$\begin{aligned}
> \mathbf e_t &= \frac{d\mathbf r_0^P}{ds} = \frac{d\mathbf r_0^P/d\phi}{ds/d\phi} \quad &\text{(Eq. 2.9 and chain rule, for $0 \lt \phi \lt \pi/2$)} \\
> &= \frac{-3a\cos^2\phi\sin\phi\,\mathbf i_0 + 3a\sin^2\phi\cos\phi\,\mathbf j_0}{3a\sin\phi\cos\phi} \quad &\text{(derivatives of the coordinates)} \\
> &= -\cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0 \quad &\text{(division by $3a\sin\phi\cos\phi$)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{d\mathbf e_t/d\phi}{ds/d\phi} = \frac{\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0}{3a\sin\phi\cos\phi} \quad &\text{(chain rule; derivatives of cosine and sine)} \\
> \frac{1}{\rho} &= \left|\frac{d\mathbf e_t}{ds}\right| = \frac{\sqrt{\sin^2\phi + \cos^2\phi}}{3a\sin\phi\cos\phi} = \frac{1}{3a\sin\phi\cos\phi} \quad &\text{(Eq. 2.12)} \\
> \mathbf e_n &= \rho\,\frac{d\mathbf e_t}{ds} = \sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0 \quad &\text{(Eq. 2.11)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = -\cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0, \qquad \mathbf e_n = \sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0, \qquad \rho = 3a\sin\phi\cos\phi}$$
>
> **Units:** $\mathbf e_t$, $\mathbf e_n$ dimensionless; $[\rho] = [\mathrm{L}]$
> **Meaning:** the normal points away from the centre $O$: the arc bulges toward $O$ and its centre of curvature lies outside. The radius of curvature vanishes at both cusps.

> [!derivation] Change of basis from the fixed to the intrinsic basis
> **Law:** change of basis matrix; binormal completes the right-handed basis; vector product in components
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.42; Notes.pdf, Eq. 2.13
>
> In the view of the figure $\mathbf k_0$ points out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up.
>
> - $\mathbf e_t$ makes the angle $\phi$ with $-\mathbf i_0$: the adjacent leg $\cos\phi$ lies along $-\mathbf i_0$, which gives the minus sign of its first component; the opposite leg $\sin\phi$ lies along $\mathbf j_0$.
> - $\mathbf e_n$ makes the angle $\phi$ with $\mathbf j_0$: the adjacent leg $\cos\phi$ lies along $\mathbf j_0$ and the opposite leg $\sin\phi$ along $\mathbf i_0$.
> - Turning from $\mathbf e_t$ to $\mathbf e_n$ is a clockwise right angle in this view, so by the right-hand rule $\mathbf e_b$ points into the paper (⊗).
>
> $$\begin{aligned}
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n = (-\cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0)\times(\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0) \quad &\text{(definition of the binormal)} \\
> &= -\cos^2\phi\,(\mathbf i_0\times\mathbf j_0) + \sin^2\phi\,(\mathbf j_0\times\mathbf i_0) \quad &\text{(distributive property; parallel products vanish)} \\
> &= -\cos^2\phi\,\mathbf k_0 - \sin^2\phi\,\mathbf k_0 = -\mathbf k_0 \quad &\text{($\mathbf j_0\times\mathbf i_0 = -\mathbf k_0$; Pythagorean identity)} \\
> \det[{}_0R_F] &= (-1)\left((-\cos\phi)\cos\phi - \sin\phi\sin\phi\right) \quad &\text{(expansion along the third row, entry $-1$ at $(3,3)$)} \\
> &= (-1)(-1) = 1 \quad &\text{(Pythagorean identity)} \\
> (RR^T)_{11} &= \cos^2\phi + \sin^2\phi = 1, \quad (RR^T)_{22} = \sin^2\phi + \cos^2\phi = 1 \quad &\text{(rows times themselves)} \\
> (RR^T)_{12} &= -\cos\phi\sin\phi + \sin\phi\cos\phi = 0 \quad &\text{(row 1 times row 2)} \\
> (RR^T)_{33} &= 1, \quad (RR^T)_{13} = (RR^T)_{23} = 0 \quad &\text{(third row $(0, 0, -1)$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_F] = \begin{pmatrix} -\cos\phi & \sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & -1 \end{pmatrix}, \quad \det[{}_0R_F] = 1, \quad [{}_0R_F][{}_0R_F]^T = I}$$
>
> **Units:** dimensionless entries
> **Meaning:** the intrinsic basis is proper and orthonormal; its binormal is the constant vector opposite to $\mathbf k_0$, as for every plane curve whose tangent turns clockwise.

#### Time law and position as a function of time

> [!derivation] Arc length as a function of time
> **Law:** the tangential acceleration is the second derivative of the arc length; two integrations with Barrow's rule
> **Source:** Notes.pdf, Eq. 2.18; Notes.pdf, Eq. 2.20; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \ddot s &= a_t = k \quad &\text{(Eq. 2.18 and statement)} \\
> \dot s(t) - \dot s(0) &= \int_0^t k\,dt' = \left[k t'\right]_0^t = kt - 0 \quad &\text{(antiderivative of a constant, Barrow's rule)} \\
> \dot s(t) &= kt \quad &\text{(starts from rest)} \\
> s(t) - s(0) &= \int_0^t k t'\,dt' = \left[\frac{k t'^2}{2}\right]_0^t = \frac{kt^2}{2} - 0 \quad &\text{(antiderivative of $kt'$, Barrow's rule)} \\
> s(t) &= \frac{kt^2}{2} \quad &\text{(starts at the origin of $s$)}
> \end{aligned}$$
>
> $$\boxed{\dot s = kt, \qquad s = \frac{kt^2}{2}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}][\mathrm{T}] = [\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}][\mathrm{T^2}] = [\mathrm{L}]$
> **Meaning:** along the curve the motion is uniformly accelerated, exactly as on a straight line.

> [!derivation] Parameter as a function of time
> **Law:** the arc length is one quantity: its geometric and its kinematic expressions are equal
> **Source:** Notes.pdf, Sec. 2.3; [Lecture 1, Slide 24]
>
> $$\begin{aligned}
> \frac{3a}{2}\sin^2\phi &= \frac{kt^2}{2} \quad &\text{(the two expressions of $s$)} \\
> \sin^2\phi &= \frac{kt^2}{3a} \quad &\text{(multiplication by $2/(3a)$)} \\
> \sin\phi &= \sqrt{\frac{k}{3a}}\;t \quad &\text{(positive root: $\sin\phi \ge 0$ on the arc, $t \ge 0$)} \\
> \phi &= \arcsin\left(\sqrt{\frac{k}{3a}}\;t\right) \quad &\text{(principal branch, $0 \le \phi \le \pi/2$)}
> \end{aligned}$$
>
> $$\boxed{\phi(t) = \arcsin\left(\sqrt{\frac{k}{3a}}\;t\right), \qquad 0 \le t \le \sqrt{\frac{3a}{k}}}$$
>
> **Units:** $\sqrt{[\mathrm{L\,T^{-2}}]/[\mathrm{L}]}\,[\mathrm{T}] = [\mathrm{T^{-1}}][\mathrm{T}] = 1$, a valid argument of the arcsine
> **Meaning:** the parameter grows from 0 to the right angle; the arc is left when the argument reaches 1.

> [!derivation] Position as a function of time
> **Law:** substitution of the time law in the parametric equations
> **Source:** Notes.pdf, Eq. 2.5; Problems.pdf, p. 6
>
> $$\begin{aligned}
> \cos\phi &= \sqrt{1 - \sin^2\phi} = \sqrt{1 - \frac{kt^2}{3a}} \quad &\text{(Pythagorean identity; $\cos\phi \ge 0$ on the arc)} \\
> x(t) &= a\cos^3\phi = a\left(1 - \frac{kt^2}{3a}\right)^{3/2} \quad &\text{(cube of the cosine)} \\
> y(t) &= a\sin^3\phi = a\left(\frac{k}{3a}\right)^{3/2}t^3 \quad &\text{(cube of the sine)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P(t) = a\left(1 - \frac{kt^2}{3a}\right)^{3/2}\mathbf i_0 + a\left(\frac{k}{3a}\right)^{3/2}t^3\,\mathbf j_0, \qquad 0 \le t \le \sqrt{\frac{3a}{k}}}$$
>
> **Units:** $kt^2/(3a)$ is dimensionless, so both components are $[\mathrm{L}]$
> **Meaning:** the particle leaves $(a, 0)$ moving along the negative $\mathbf i_0$ direction: $x$ falls as the square of time while $y$ grows only as its cube; it reaches the cusp $(0, a)$ at the end of the interval.

> [!derivation] Velocity and acceleration along the arc
> **Law:** intrinsic components of velocity and acceleration
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.17; [Lecture 1, Slide 28]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot s\,\mathbf e_t = kt\left(-\cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0\right) \quad &\text{(Eq. 2.16)} \\
> \mathbf a_0^P &= \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n \quad &\text{(Eq. 2.17)} \\
> \frac{\dot s^2}{\rho} &= \frac{k^2t^2}{3a\sin\phi\cos\phi} \quad &\text{(speed and radius of curvature)} \\
> &= \frac{k^2\cdot 3a\sin^2\phi/k}{3a\sin\phi\cos\phi} = k\,\frac{\sin\phi}{\cos\phi} = k\tan\phi \quad &\text{($t^2$ is $3a\sin^2\phi/k$ from the time law)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = kt\,\mathbf e_t, \qquad \mathbf a_0^P = k\,\mathbf e_t + k\tan\phi\,\mathbf e_n}$$
>
> **Units:** $[kt] = [\mathrm{L\,T^{-1}}]$; $[k\tan\phi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the normal acceleration grows without bound as the particle approaches the end cusp, where the curve turns with zero radius while the speed stays finite.

### Answers and Checks

> [!derivation] Answer: position as a function of time on the smooth arc
> **Law:** collection of the boxed results above
> **Source:** Notes.pdf, Eq. 2.18; Problems.pdf, p. 6
>
> $$\begin{aligned}
> s(t) &= \frac{kt^2}{2} \quad &\text{(time law)} \\
> \phi(t) &= \arcsin\left(\sqrt{\frac{k}{3a}}\;t\right) \quad &\text{(parameter)} \\
> x(t) &= a\left(1 - \frac{kt^2}{3a}\right)^{3/2}, \quad y(t) = a\left(\frac{k}{3a}\right)^{3/2}t^3 \quad &\text{(position)}
> \end{aligned}$$
>
> $$\boxed{\phi = \arcsin\left(\sqrt{\frac{k}{3a}}\,t\right),\quad s = \frac{kt^2}{2},\quad x = a\left(1 - \frac{kt^2}{3a}\right)^{3/2},\quad y = a\left(\frac{k}{3a}\right)^{3/2}t^3}$$
>
> **Units:** $[s] = [x] = [y] = [\mathrm{L}]$; the argument of the arcsine is dimensionless
> **Meaning:** valid from the start cusp until the particle reaches the next cusp.

> [!derivation] Limits of validity and limiting cases
> **Law:** consistency of the time law with the geometry of the arc
> **Source:** Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.12
>
> $$\begin{aligned}
> \sqrt{\frac{k}{3a}}\;t_c &= 1 \;\Rightarrow\; t_c = \sqrt{\frac{3a}{k}} \quad &\text{(end cusp: $\sin\phi$ reaches 1)} \\
> s(t_c) &= \frac{k}{2}\cdot\frac{3a}{k} = \frac{3a}{2} = s\!\left(\tfrac{\pi}{2}\right) \quad &\text{(time law and arc length agree at the cusp)} \\
> \dot s(t_c) &= k\sqrt{\frac{3a}{k}} = \sqrt{3ak} \neq 0 \quad &\text{(the particle arrives with finite speed)} \\
> \phi \to \tfrac{\pi}{2}:\quad k\tan\phi &\to \infty \quad &\text{(unbounded normal acceleration: the law cannot continue past the cusp)} \\
> t \to 0:\quad k\tan\phi &\approx k\phi \approx k\sqrt{\frac{k}{3a}}\;t \to 0 \quad &\text{(small angles: the start cusp is left smoothly)} \\
> t \to 0:\quad x &\approx a - \frac{kt^2}{2} \quad &\text{(binomial expansion: uniformly accelerated along $-\mathbf i_0$, the initial $\mathbf e_t$)}
> \end{aligned}$$
>
> $$\boxed{t_c = \sqrt{\frac{3a}{k}}, \qquad s(t_c) = \frac{3a}{2}, \qquad \dot s(t_c) = \sqrt{3ak}}$$
>
> **Units:** $[t_c] = \sqrt{[\mathrm{L}]/[\mathrm{L\,T^{-2}}]} = [\mathrm{T}]$; $[\sqrt{3ak}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the solution is the motion on one smooth segment, as the statement asks; at the start the particle moves like a body accelerated along the tangent of the cusp.

> [!derivation] Check against the official key
> **Law:** comparison with the solution key
> **Source:** Problems.pdf, p. 72
>
> $$\begin{aligned}
> \text{key:}\quad \phi &= \arcsin\sqrt{\frac{k}{3a}}\,t, \quad s = \frac{kt^2}{2} \quad &\text{(Problems.pdf, p. 72, item 3)} \\
> \text{computed:}\quad \phi &= \arcsin\left(\sqrt{\frac{k}{3a}}\;t\right), \quad s = \frac{kt^2}{2} \quad &\text{(boxes above)} \\
> s(\phi(t)) &= \frac{3a}{2}\cdot\frac{kt^2}{3a} = \frac{kt^2}{2} \quad &\text{(second route: geometric arc length at the computed parameter)}
> \end{aligned}$$
>
> $$\boxed{\text{computed result} = \text{official key}}$$
>
> **Units:** both sides in the same units, $[\mathrm{L}]$ for $s$ and dimensionless for $\phi$
> **Meaning:** full agreement; the key writes the square root over the fraction only, with $t$ outside it, which is the reading taken here.

Check against the official key: the result agrees with the key of Problems.pdf, p. 72, as the box above shows.

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Particle on the astroid (Problem 03)", "intro": "Sample values: a = 1 m and tangential acceleration k = 0.5 m/s². The slider is the parameter φ of the curve (not the polar angle of P), on the smooth arc from the cusp (a, 0) to the cusp (0, a); the default φ = 0 is the start of the statement, at rest at the cusp, where the velocity and its tangent arrow vanish. The readouts give the time at which the particle reaches the drawn φ and the time law of the solution. The speed and accelerations of the archetype below them assume a constant rate of φ, which is not the motion of this problem: use the readouts of the solution.", "params": {"curve": "astroid", "a": 1.0, "k": 0.5, "rate": 1, "accel": 0, "umin": 0, "umax": 90, "extent": 1.3}, "defaults": {"u": 0}, "view": "top", "sliders": {"u": {"label": "Parameter φ of the astroid"}}, "readouts": [{"label": "Time t = √(3a/k) sin φ, from φ = arcsin(√(k/3a) t)", "expr": "(sqrt(3*a/k)*sin(u))", "unit": "s", "digits": 4}, {"label": "Arc length s = k t²/2", "expr": "k*(sqrt(3*a/k)*sin(u))^2/2", "unit": "m", "digits": 4}, {"label": "Arc length s(φ) = (3a/2) sin²φ (geometric route)", "expr": "1.5*a*sin(u)^2", "unit": "m", "digits": 4}, {"label": "Speed ṡ = k t", "expr": "k*(sqrt(3*a/k)*sin(u))", "unit": "m/s", "digits": 4}, {"label": "x = a (1 − k t²/(3a))^(3/2)", "expr": "a*(1 - k*(sqrt(3*a/k)*sin(u))^2/(3*a))^1.5", "unit": "m", "digits": 4}, {"label": "y = a (k/(3a))^(3/2) t³", "expr": "a*(k/(3*a))^1.5*(sqrt(3*a/k)*sin(u))^3", "unit": "m", "digits": 4}, {"label": "Radius of curvature ρ = 3a sin φ cos φ", "expr": "3*a*sin(u)*cos(u)", "unit": "m", "digits": 4}, {"label": "Normal acceleration k tan φ", "expr": "k*tan(u)", "unit": "m/s²", "digits": 4}, {"label": "End of the smooth arc t_c = √(3a/k)", "expr": "sqrt(3*a/k)", "unit": "s", "digits": 4}, {"label": "Speed at the end cusp √(3ak)", "expr": "sqrt(3*a*k)", "unit": "m/s", "digits": 4}]}

## Problem 04: Plane at Constant Altitude

### Reference Frames, Bases and Coordinates

The aircraft is modelled as a point particle $P$ that moves in a vertical plane. The observer is a fixed point $O$ on the ground, directly below the position of the aircraft at the initial instant. The statement asks for the description of the motion in polar coordinates centred at $O$ and then in Cartesian coordinates.

| Symbol | Meaning | Units |
| :--- | :--- | :--- |
| $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ | fixed (inertial) frame of the observer; $\mathbf i_0$ horizontal, in the direction of flight; $\mathbf j_0$ vertical, upward; $\mathbf k_0 = \mathbf i_0 \times \mathbf j_0$ out of the paper (⊙) | - |
| $B_1 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k_0\}$ | polar basis at $P$: $\mathbf e_r$ along $\overrightarrow{OP}$, $\mathbf e_\theta$ in the sense of growing $\theta$ | - |
| $x(t)$, $y_0$ | Cartesian coordinates of $P$ in $S_0$; the altitude $y_0 \gt 0$ is constant | m |
| $r(t)$, $\theta(t)$ | polar coordinates of $P$: distance $OP$ and angle from $\mathbf i_0$ to $\overrightarrow{OP}$, counterclockwise seen with $\mathbf k_0$ ⊙ | m, rad |
| $v_0$ | speed of the aircraft at $t = 0$ | m/s |
| $a_x$ | constant acceleration along $\mathbf i_0$ for $t \ge 0$ | m/s$^2$ |
| $v(t) \equiv \dot x(t)$ | speed along $\mathbf i_0$ (notation of the statement) | m/s |
| Initial conditions | $x(0) = 0$, $\dot x(0) = v_0$ | m, m/s |

Hypotheses and degrees of freedom:

- The altitude is constant, so the motion is confined to the straight line at height $y_0$ in the plane of $\mathbf i_0$ and $\mathbf j_0$. This holonomic, time-independent constraint leaves one degree of freedom, the abscissa $x$, and its time law is fully prescribed by the statement (kinematics only, no forces are asked).
- The aircraft is above the observer, so the angle $\theta$ lies strictly between zero and $\pi$ for every instant; at the initial instant the aircraft is overhead and $\theta$ equals a right angle.
- The forces section is omitted: the problem has no dynamics.

![[attachments/EM-SOL/p04-main-plane.svg]]

### Change of Basis and Position Vector

The polar basis is the fixed basis turned by the angle $\theta$ about $\mathbf k_0$. The view along $\mathbf k_0$ (⊙) below shows both pairs of axes and the angle between them.

![[attachments/EM-SOL/p04-rotation-view.svg]]

> [!derivation] Polar unit vectors and the change of basis matrix
> **Law:** rotation of the basis about $\mathbf k_0$ by the angle $\theta$; definition of the change of basis matrix
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> In the view along $\mathbf k_0$ (⊙), $\mathbf e_r$ is a unit hypotenuse: its projection on $\mathbf i_0$ is the leg adjacent to $\theta$ and its projection on $\mathbf j_0$ is the opposite leg. The vector $\mathbf e_\theta$ is $\mathbf e_r$ turned a further right angle counterclockwise (right-hand rule about $\mathbf k_0$ ⊙); its leg adjacent to $\theta$ now lies along $\mathbf j_0$ and its opposite leg points toward $-\mathbf i_0$, which is the origin of the minus sign.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(hypotenuse 1; adjacent leg on $\mathbf i_0$, opposite leg on $\mathbf j_0$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(adjacent leg on $\mathbf j_0$; opposite leg on $-\mathbf i_0$, turning toward $-\mathbf i_0$ with $\mathbf k_0$ ⊙)} \\
> \mathbf k_0 &= \mathbf k_0 \quad &\text{(axis of the rotation, unchanged)} \\
> \det[{}_0R_1] &= 1\cdot(\cos\theta\cos\theta - (-\sin\theta)\sin\theta) \quad &\text{(expansion along the third row)} \\
> &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(Pythagorean identity)} \\
> ([{}_0R_1][{}_0R_1]^T)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> ([{}_0R_1][{}_0R_1]^T)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_1][{}_0R_1]^T)_{22} &= \sin^2\theta + \cos^2\theta = 1 \quad &\text{(row 2 times row 2; the third row and column are those of the identity)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},\qquad \det[{}_0R_1] = 1,\qquad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** every entry is a ratio of lengths, $[\mathrm{L}]/[\mathrm{L}] = [1]$
> **Meaning:** the columns of the matrix are the polar unit vectors written in the fixed basis; the matrix is a proper rotation, as Notes.pdf, Eq. 1.15 requires.

> [!derivation] Polar coordinates from the right triangle O H P
> **Law:** trigonometry of the right triangle with vertices $O$, the foot $H$ of the vertical through $P$, and $P$
> **Source:** Notes.pdf, Eq. 2.23; Problems.pdf, p. 7
>
> The triangle has its right angle at $H$; the hypotenuse is $OP$, the leg adjacent to $\theta$ is $OH$ (horizontal) and the opposite leg is $HP$ (vertical, of length equal to the altitude).
>
> $$\begin{aligned}
> r^2 &= x^2 + y_0^2 \quad &\text{(Pythagoras in triangle $OHP$)} \\
> r &= \sqrt{x^2 + y_0^2} \quad &\text{(positive root: $r$ is a distance)} \\
> \cos\theta &= \frac{x}{r} \quad &\text{(adjacent leg over hypotenuse)} \\
> \sin\theta &= \frac{y_0}{r} \quad &\text{(opposite leg over hypotenuse)} \\
> \cot\theta &= \frac{x}{y_0} \quad &\text{(quotient of the two lines above; valid also at zero $x$ since $y_0 \gt 0$)}
> \end{aligned}$$
>
> $$\boxed{r(t) = \sqrt{x(t)^2 + y_0^2},\qquad \cos\theta = \frac{x}{r},\qquad \sin\theta = \frac{y_0}{r},\qquad \theta = \operatorname{arccot}\frac{x}{y_0} \in (0, \pi)}$$
>
> **Units:** $[r] = [\mathrm{L}]$; $\cos\theta$ and $\sin\theta$ are $[\mathrm{L}]/[\mathrm{L}] = [1]$
> **Meaning:** when the aircraft is ahead of the observer the triangle has a positive horizontal leg and the angle is acute; behind the observer the horizontal leg is negative and the angle is obtuse; the branch of the arccotangent between zero and pi covers both.

> [!derivation] Change of basis matrix written with the Cartesian data, and the inverse relation
> **Law:** substitution of the triangle relations into the matrix; inverse of an orthogonal matrix equals its transpose
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.12
>
> $$\begin{aligned}
> [{}_0R_1]_{11} &= [{}_0R_1]_{22} = \frac{x}{r} \quad &\text{(substitution of $\cos\theta$)} \\
> [{}_0R_1]_{21} &= -[{}_0R_1]_{12} = \frac{y_0}{r} \quad &\text{(substitution of $\sin\theta$)} \\
> \det[{}_0R_1] &= \frac{x^2 + y_0^2}{r^2} = 1 \quad &\text{(Pythagoras of the previous box)} \\
> [{}_1R_0] &= [{}_0R_1]^T \quad &\text{(orthogonality)} \\
> \mathbf i_0 &= \cos\theta\,\mathbf e_r - \sin\theta\,\mathbf e_\theta \quad &\text{(first column of the transpose)} \\
> \mathbf j_0 &= \sin\theta\,\mathbf e_r + \cos\theta\,\mathbf e_\theta \quad &\text{(second column of the transpose)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_0 = \frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta,\qquad \mathbf j_0 = \frac{y_0}{r}\,\mathbf e_r + \frac{x}{r}\,\mathbf e_\theta}$$
>
> **Units:** $[\mathrm{L}]/[\mathrm{L}] = [1]$ for every coefficient
> **Meaning:** the direction of flight, seen from the polar basis of the observer, has a radial part that grows as the aircraft moves away and a negative azimuthal part that dominates when the aircraft is overhead.

> [!derivation] Position vector of the aircraft
> **Law:** definition of the position vector, written in both bases
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OH} + \overrightarrow{HP} \quad &\text{(path along the two legs of the triangle)} \\
> &= x\,\mathbf i_0 + y_0\,\mathbf j_0 \quad &\text{(horizontal leg plus vertical leg)} \\
> &= x\left(\frac{x}{r}\mathbf e_r - \frac{y_0}{r}\mathbf e_\theta\right) + y_0\left(\frac{y_0}{r}\mathbf e_r + \frac{x}{r}\mathbf e_\theta\right) \quad &\text{(inverse relations of the previous box)} \\
> &= \frac{x^2 + y_0^2}{r}\,\mathbf e_r + \frac{-x y_0 + y_0 x}{r}\,\mathbf e_\theta \quad &\text{(grouping by unit vector)} \\
> &= r\,\mathbf e_r \quad &\text{(Pythagoras; the azimuthal terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x(t)\,\mathbf i_0 + y_0\,\mathbf j_0 = r(t)\,\mathbf e_r}$$
>
> **Units:** $[\mathrm{L}]$ on both sides
> **Meaning:** in polar form the whole position is radial, which is the definition of the polar basis; all the information on the direction is carried by the unit vector.

### Kinematics

> [!derivation] Time law of the abscissa
> **Law:** definition of acceleration and velocity in $S_0$; integration with Barrow's rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7; Problems.pdf, p. 7
>
> $$\begin{aligned}
> \ddot x &= a_x \quad &\text{(statement: constant acceleration along $\mathbf i_0$)} \\
> v(t) - v(0) &= \int_0^t a_x\,dt' \quad &\text{(integration of $\dot v$ from 0 to $t$)} \\
> &= \left[a_x t'\right]_0^t = a_x t - a_x\cdot 0 \quad &\text{(antiderivative $a_x t'$; Barrow's rule)} \\
> v(t) &= v_0 + a_x t \quad &\text{(initial speed $v_0$)} \\
> x(t) - x(0) &= \int_0^t (v_0 + a_x t')\,dt' \quad &\text{(integration of $\dot x$ from 0 to $t$)} \\
> &= \left[v_0 t' + \tfrac{1}{2}a_x t'^2\right]_0^t = v_0 t + \tfrac{1}{2}a_x t^2 - 0 \quad &\text{(antiderivative; Barrow's rule)} \\
> x(t) &= v_0 t + \tfrac{1}{2}a_x t^2 \quad &\text{(initial abscissa zero)} \\
> v^2 - v_0^2 &= 2 a_x v_0 t + a_x^2 t^2 = 2a_x x \quad &\text{(squaring $v$ and comparing with $2a_x x$)}
> \end{aligned}$$
>
> $$\boxed{v(t) = v_0 + a_x t,\qquad x(t) = v_0 t + \tfrac{1}{2}a_x t^2,\qquad v^2 = v_0^2 + 2a_x x}$$
>
> **Units:** $[a_x t] = [\mathrm{L\,T^{-2}}][\mathrm{T}] = [\mathrm{L\,T^{-1}}]$; $[a_x t^2] = [\mathrm{L}]$
> **Meaning:** uniformly accelerated rectilinear motion; the last form gives the speed as a function of the position, used by the simulator below.

#### (a) Rate of change of the distance

> [!derivation] Radial rate
> **Law:** implicit differentiation of the Pythagorean relation with the chain rule
> **Source:** Notes.pdf, Eq. 2.23; Problems.pdf, p. 7
>
> $$\begin{aligned}
> r^2 &= x^2 + y_0^2 \quad &\text{(triangle $OHP$)} \\
> \frac{d}{dt}\left(r^2\right) &= 2r\,\dot r \quad &\text{(chain rule, $\tfrac{d}{dt}f(r) = f'(r)\,\dot r$)} \\
> \frac{d}{dt}\left(x^2 + y_0^2\right) &= 2x\,\dot x + 0 \quad &\text{(chain rule; $y_0$ is constant)} \\
> 2r\,\dot r &= 2x\,v \quad &\text{(equating both derivatives; $\dot x$ is $v$)} \\
> \dot r &= \frac{v\,x}{r} \quad &\text{(division by $2r \gt 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot r = \frac{v(t)\,x(t)}{r(t)}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{L}]/[\mathrm{L}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the distance does not change while the aircraft is overhead and tends to the flight speed far away, where the line of sight is aligned with the path.

#### (b) Angular rate of the line of sight

> [!derivation] Angular rate
> **Law:** differentiation of the horizontal leg of the triangle with the product and chain rules
> **Source:** Notes.pdf, Eq. 2.23; Problems.pdf, p. 7
>
> $$\begin{aligned}
> x &= r\cos\theta \quad &\text{(adjacent leg of triangle $OHP$)} \\
> \dot x &= \dot r\cos\theta + r\,\frac{d}{dt}\cos\theta \quad &\text{(product rule)} \\
> &= \dot r\cos\theta - r\sin\theta\,\dot\theta \quad &\text{(chain rule, $\tfrac{d}{dt}\cos\theta = -\sin\theta\,\dot\theta$)} \\
> v &= \frac{v x}{r}\,\frac{x}{r} - r\,\frac{y_0}{r}\,\dot\theta \quad &\text{(result (a), $\cos\theta$ and $\sin\theta$ of the triangle)} \\
> y_0\,\dot\theta &= v\,\frac{x^2}{r^2} - v = -v\,\frac{r^2 - x^2}{r^2} \quad &\text{(solving for the term in $\dot\theta$)} \\
> y_0\,\dot\theta &= -v\,\frac{y_0^2}{r^2} \quad &\text{(Pythagoras: $r^2 - x^2$ is $y_0^2$)} \\
> \dot\theta &= -\frac{v\,y_0}{r^2} \quad &\text{(division by $y_0 \gt 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = -\frac{v(t)\,y_0}{r(t)^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{L}]/[\mathrm{L^2}] = [\mathrm{T^{-1}}]$
> **Meaning:** for a forward speed the line of sight turns clockwise (negative sense about $\mathbf k_0$ ⊙); at constant speed the rate of turn is largest when the aircraft is overhead, where the distance is shortest; with a positive $a_x$ the rate is still increasing overhead, and its maximum lies beyond that point (part (d)).

#### (c) Second derivative of the distance

> [!derivation] Radial second derivative
> **Law:** quotient rule applied to result (a)
> **Source:** Problems.pdf, p. 7; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \ddot r &= \frac{d}{dt}\left(\frac{u}{w}\right),\ u = v x,\ w = r \quad &\text{(result (a) as a quotient)} \\
> \dot u &= \dot v\,x + v\,\dot x = a_x x + v^2 \quad &\text{(product rule; $\dot v$ is $a_x$, $\dot x$ is $v$)} \\
> \dot w &= \dot r = \frac{v x}{r} \quad &\text{(result (a))} \\
> \ddot r &= \frac{\dot u\,w - u\,\dot w}{w^2} \quad &\text{(quotient rule)} \\
> &= \frac{(a_x x + v^2)\,r - v x\,\dfrac{v x}{r}}{r^2} \quad &\text{(substitution)} \\
> &= \frac{(a_x x + v^2)\,r^2 - v^2 x^2}{r^3} \quad &\text{(multiplying numerator and denominator by $r$)} \\
> &= \frac{a_x x\,r^2 + v^2\,(r^2 - x^2)}{r^3} \quad &\text{(grouping the terms in $v^2$)} \\
> &= \frac{v^2 y_0^2 + a_x x\,r^2}{r^3} \quad &\text{(Pythagoras: $r^2 - x^2$ is $y_0^2$)}
> \end{aligned}$$
>
> $$\boxed{\ddot r = \frac{v^2(t)\,y_0^2 + a_x\,x(t)\,r^2(t)}{r^3(t)}}$$
>
> **Units:** $[\mathrm{L^2T^{-2}}][\mathrm{L^2}]/[\mathrm{L^3}] = [\mathrm{L\,T^{-2}}]$ and $[\mathrm{L\,T^{-2}}][\mathrm{L}][\mathrm{L^2}]/[\mathrm{L^3}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** even at constant speed the distance accelerates, because the radial rate changes as the line of sight turns.

#### (d) Second derivative of the angle

> [!derivation] Angular second derivative
> **Law:** quotient rule applied to result (b), with the chain rule for the square of the distance
> **Source:** Problems.pdf, p. 7; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\right) &= 2r\,\dot r = 2r\,\frac{v x}{r} = 2 v x \quad &\text{(chain rule and result (a))} \\
> \ddot\theta &= -y_0\,\frac{d}{dt}\left(\frac{v}{r^2}\right) \quad &\text{(result (b); $y_0$ is constant)} \\
> &= -y_0\,\frac{\dot v\,r^2 - v\,\tfrac{d}{dt}(r^2)}{r^4} \quad &\text{(quotient rule)} \\
> &= -y_0\,\frac{a_x r^2 - 2v^2 x}{r^4} \quad &\text{(substitution of $\dot v$ and of the first line)} \\
> &= y_0\,\frac{2v^2 x - a_x r^2}{r^4} \quad &\text{(sign taken into the numerator)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = y_0\,\frac{2v^2(t)\,x(t) - a_x\,r^2(t)}{r^4(t)}}$$
>
> **Units:** $[\mathrm{L}][\mathrm{L^2T^{-2}}][\mathrm{L}]/[\mathrm{L^4}] = [\mathrm{T^{-2}}]$
> **Meaning:** the angular acceleration changes sign during the flight: the acceleration along the path tends to make the line of sight turn faster, while the growing distance slows it down.

#### Position, velocity and acceleration in polar coordinates

> [!derivation] Derivatives of the polar unit vectors
> **Law:** derivative of a unit vector that rotates with angular velocity $\boldsymbol\omega$; the vector products written out
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> The basis $B_1$ turns about $\mathbf k_0$ with the rate of $\theta$, so its angular velocity seen from $S_0$ is the rate of $\theta$ times $\mathbf k_0$. The products of the fixed unit vectors are those of a right-handed basis: k0 cross i0 gives j0 and k0 cross j0 gives minus i0.
>
> $$\begin{aligned}
> \boldsymbol\omega_{1,0} &= \dot\theta\,\mathbf k_0 \quad &\text{(rotation about $\mathbf k_0$ by $\theta$)} \\
> \dot{\mathbf e}_r &= \dot\theta\,\mathbf k_0 \times (\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0) \quad &\text{(Notes Eq. 1.62)} \\
> &= \dot\theta\left(\cos\theta\,\mathbf j_0 - \sin\theta\,\mathbf i_0\right) = \dot\theta\,\mathbf e_\theta \quad &\text{(products of the fixed unit vectors; definition of $\mathbf e_\theta$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k_0 \times (-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0) \quad &\text{(Notes Eq. 1.62)} \\
> &= \dot\theta\left(-\sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf i_0\right) = -\dot\theta\,\mathbf e_r \quad &\text{(products of the fixed unit vectors; definition of $\mathbf e_r$)} \\
> \dot{\mathbf k}_0 &= \dot\theta\,\mathbf k_0 \times \mathbf k_0 = \mathbf 0 \quad &\text{(parallel vectors)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta,\qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ on both sides
> **Meaning:** the polar unit vectors change only in direction, at the angular rate of the line of sight.

> [!derivation] Velocity in the polar basis
> **Law:** time derivative of the position vector in $S_0$ with the product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.25
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(r\,\mathbf e_r\right) \quad &\text{(definition of velocity)} \\
> &= \dot r\,\mathbf e_r + r\,\dot{\mathbf e}_r \quad &\text{(product rule)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{(derivative of $\mathbf e_r$)} \\
> &= \frac{v x}{r}\,\mathbf e_r + r\left(-\frac{v y_0}{r^2}\right)\mathbf e_\theta \quad &\text{(results (a) and (b))} \\
> &= v\left(\frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta\right) \quad &\text{(common factor $v$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta = v(t)\left(\frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the bracket is the direction of flight written in the polar basis (inverse relations above), so the velocity is the speed along that direction, as it must be.

> [!derivation] Acceleration in the polar basis
> **Law:** time derivative of the velocity in $S_0$ with the product rule and the derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta\right) \quad &\text{(definition of acceleration)} \\
> &= \ddot r\,\mathbf e_r + \dot r\,\dot{\mathbf e}_r + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta + r\dot\theta\,\dot{\mathbf e}_\theta \quad &\text{(product rule on each term)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \dot r\dot\theta\,\mathbf e_\theta + r\ddot\theta\,\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivatives of $\mathbf e_r$ and $\mathbf e_\theta$)} \\
> &= (\ddot r - r\dot\theta^2)\,\mathbf e_r + (r\ddot\theta + 2\dot r\dot\theta)\,\mathbf e_\theta \quad &\text{(grouping by unit vector)}
> \end{aligned}$$
>
> $$\boxed{a_r = \ddot r - r\dot\theta^2,\qquad a_\theta = r\ddot\theta + 2\dot r\dot\theta}$$
>
> **Units:** each term is $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the radial component combines the change of the radial rate with the centripetal term; the azimuthal component combines the angular acceleration with the coupling of radial and angular rates.

> [!derivation] Radial component of the acceleration
> **Law:** substitution of results (b) and (c)
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> r\dot\theta^2 &= r\,\frac{v^2 y_0^2}{r^4} = \frac{v^2 y_0^2}{r^3} \quad &\text{(square of result (b))} \\
> a_r &= \frac{v^2 y_0^2 + a_x x r^2}{r^3} - \frac{v^2 y_0^2}{r^3} \quad &\text{(result (c) minus the line above)} \\
> &= \frac{a_x x r^2}{r^3} = a_x\,\frac{x}{r} \quad &\text{(the terms in $v^2$ cancel)}
> \end{aligned}$$
>
> $$\boxed{a_r = a_x\,\frac{x(t)}{r(t)}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}][\mathrm{L}]/[\mathrm{L}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** only the real acceleration of the aircraft survives; the speed terms, which are pure geometry of the line of sight, cancel.

> [!derivation] Azimuthal component of the acceleration
> **Law:** substitution of results (a), (b) and (d)
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> r\ddot\theta &= \frac{y_0\,(2v^2 x - a_x r^2)}{r^3} \quad &\text{(result (d) times $r$)} \\
> 2\dot r\dot\theta &= 2\,\frac{v x}{r}\left(-\frac{v y_0}{r^2}\right) = -\frac{2v^2 x y_0}{r^3} \quad &\text{(results (a) and (b))} \\
> a_\theta &= \frac{2v^2 x y_0 - a_x y_0 r^2 - 2v^2 x y_0}{r^3} \quad &\text{(sum over the common denominator)} \\
> &= -a_x\,\frac{y_0}{r} \quad &\text{(the terms in $v^2$ cancel)}
> \end{aligned}$$
>
> $$\boxed{a_\theta = -a_x\,\frac{y_0}{r(t)},\qquad \mathbf a_0^P = a_x\left(\frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the acceleration vector is the constant acceleration of flight seen in the turning polar basis.

![[attachments/EM-SOL/p04-acceleration-projection.svg]]

#### Repeating the problem in Cartesian coordinates

> [!derivation] Position, velocity and acceleration in the fixed basis
> **Law:** in $S_0$ the fixed unit vectors have zero derivative
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i_0 + y_0\,\mathbf j_0 \quad &\text{(position vector)} \\
> \mathbf v_0^P &= \dot x\,\mathbf i_0 + \dot y_0\,\mathbf j_0 = v\,\mathbf i_0 \quad &\text{(derivative; $y_0$ constant)} \\
> \mathbf a_0^P &= \dot v\,\mathbf i_0 = a_x\,\mathbf i_0 \quad &\text{(derivative of $v$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = \left(v_0 t + \tfrac{1}{2}a_x t^2\right)\mathbf i_0 + y_0\,\mathbf j_0,\qquad \mathbf v_0^P = (v_0 + a_x t)\,\mathbf i_0,\qquad \mathbf a_0^P = a_x\,\mathbf i_0}$$
>
> **Units:** $[\mathrm{L}]$, $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$
> **Meaning:** in Cartesian coordinates the description is immediate because the basis does not turn; all the work of the polar description comes from the rotation of its basis.

> [!derivation] Cartesian result carried to the polar basis
> **Law:** change of basis with the transpose matrix
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.12
>
> $$\begin{aligned}
> \mathbf v_0^P &= v\,\mathbf i_0 = v\left(\frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta\right) \quad &\text{(inverse relation for $\mathbf i_0$)} \\
> \mathbf a_0^P &= a_x\,\mathbf i_0 = a_x\left(\frac{x}{r}\,\mathbf e_r - \frac{y_0}{r}\,\mathbf e_\theta\right) \quad &\text{(same relation)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P\ \text{and}\ \mathbf a_0^P\ \text{agree term by term with the polar results}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** both descriptions give the same vectors, as they must: a vector does not depend on the basis used to write it.

### Answers and Checks

> [!derivation] Answers to (a) to (d) and the acceleration vector
> **Law:** collection of the results proved above
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> \dot r &= \frac{v x}{r},\quad \dot\theta = -\frac{v y_0}{r^2} \quad &\text{(parts (a) and (b))} \\
> \ddot r &= \frac{v^2 y_0^2 + a_x x r^2}{r^3},\quad \ddot\theta = y_0\,\frac{2v^2 x - a_x r^2}{r^4} \quad &\text{(parts (c) and (d))}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = a_r\,\mathbf e_r + a_\theta\,\mathbf e_\theta = a_x\,\frac{x}{r}\,\mathbf e_r - a_x\,\frac{y_0}{r}\,\mathbf e_\theta = a_x\,\mathbf i_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$, $[\mathrm{T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$, $[\mathrm{T^{-2}}]$
> **Meaning:** the four expressions of the statement are proved, and the polar and Cartesian descriptions coincide.

> [!derivation] Limiting case: aircraft overhead at the initial instant
> **Law:** evaluation of the results at zero time
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> x(0) &= 0,\quad r(0) = y_0,\quad \theta(0) = \tfrac{\pi}{2} \quad &\text{(initial data and triangle)} \\
> \dot r(0) &= 0,\quad \dot\theta(0) = -\frac{v_0}{y_0} \quad &\text{(parts (a) and (b))} \\
> a_r(0) &= 0,\quad a_\theta(0) = -a_x \quad &\text{(components of the acceleration)} \\
> \mathbf e_\theta(0) &= -\mathbf i_0 \quad &\text{(definition of $\mathbf e_\theta$ at a right angle)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P(0) = -a_x\,\mathbf e_\theta(0) = a_x\,\mathbf i_0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** overhead, the line of sight is vertical and the whole flight direction is azimuthal; the result is consistent with the Cartesian form.

> [!derivation] Limiting case: aircraft far away
> **Law:** asymptotic behaviour for large positive abscissa
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> \frac{x}{r} &= \frac{1}{\sqrt{1 + y_0^2/x^2}} \to 1 \quad &\text{(division by $x \gt 0$)} \\
> \dot r &\to v,\quad \dot\theta \to 0 \quad &\text{(parts (a) and (b))} \\
> a_r &\to a_x,\quad a_\theta \to 0 \quad &\text{(components of the acceleration)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P \to v\,\mathbf e_r,\qquad \mathbf a_0^P \to a_x\,\mathbf e_r}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** far away, the line of sight is aligned with the path and the motion seen by the observer is purely radial.

> [!derivation] Invariance of the magnitude of the acceleration
> **Law:** a proper rotation preserves the norm
> **Source:** Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> a_r^2 + a_\theta^2 &= a_x^2\,\frac{x^2}{r^2} + a_x^2\,\frac{y_0^2}{r^2} \quad &\text{(squares of the components)} \\
> &= a_x^2\,\frac{x^2 + y_0^2}{r^2} = a_x^2 \quad &\text{(Pythagoras)}
> \end{aligned}$$
>
> $$\boxed{\left|\mathbf a_0^P\right| = |a_x|}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the norm is the same in both bases, as the orthogonality of the change of basis matrix requires.

Check against the official key: the solution keys of Problems.pdf, p. 72 list item 4 with no answer. The statement itself gives the four target expressions (a) to (d), and each one is proved above step by step; the polar acceleration is confirmed independently by the Cartesian route and by the norm check. A numerical finite difference check of the four expressions at two instants (with arbitrary data) gives residuals below one part in ten million.

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Aircraft at constant altitude seen from the observer O (Problem 04)", "intro": "Sample values: y0 = 2 m, v0 = 1 m/s, a_x = 0.5 m/s². The vertical plane of the flight is the plane of the front view: i0 is the direction of flight and the altitude y0 of the statement is drawn along the vertical axis of the view. The slider is the abscissa x of the aircraft; the default x = 0 is the initial instant, with the aircraft overhead. The polar basis e_r, e_θ of the statement is drawn at P (blue), with the acceleration a_x i0 (orange); the archetype also draws its own horizontal cylindrical basis at the foot of P on the ground, which is not the polar basis of this problem. The readouts are parts (a) to (d) and the polar components of the acceleration; the speed of the archetype below them is the initial speed v0 only.", "params": {"curve": "line", "x0": 0, "y0": 0, "z0": 2.0, "vx": 1, "vy": 0, "vz": 0, "rate": 1.0, "accel": 0.5, "umin": 0, "umax": 3, "extent": 2.4, "v0": 1.0, "ax": 0.5}, "defaults": {"u": 0}, "view": "front", "sliders": {"u": {"label": "Abscissa x of the aircraft (m)"}}, "readouts": [{"label": "Speed v = √(v0² + 2 a_x x)", "expr": "sqrt(v0^2 + 2*ax*u)", "unit": "m/s", "digits": 4}, {"label": "Time t = (v − v0)/a_x", "expr": "(sqrt(v0^2 + 2*ax*u) - v0)/ax", "unit": "s", "digits": 4}, {"label": "r = √(x² + y0²)", "expr": "sqrt(u^2 + z0^2)", "unit": "m", "digits": 4}, {"label": "θ = arccot(x/y0)", "expr": "deg(atan2(z0, u))", "unit": "deg", "digits": 2}, {"label": "(a) ṙ = v x/r", "expr": "sqrt(v0^2 + 2*ax*u)*u/sqrt(u^2 + z0^2)", "unit": "m/s", "digits": 4}, {"label": "(b) θ̇ = −v y0/r²", "expr": "-sqrt(v0^2 + 2*ax*u)*z0/sqrt(u^2 + z0^2)^2", "unit": "rad/s", "digits": 4}, {"label": "(c) r̈ = (v² y0² + a_x x r²)/r³", "expr": "(sqrt(v0^2 + 2*ax*u)^2*z0^2 + ax*u*sqrt(u^2 + z0^2)^2)/sqrt(u^2 + z0^2)^3", "unit": "m/s²", "digits": 4}, {"label": "(d) θ̈ = y0 (2v² x − a_x r²)/r⁴", "expr": "z0*(2*sqrt(v0^2 + 2*ax*u)^2*u - ax*sqrt(u^2 + z0^2)^2)/sqrt(u^2 + z0^2)^4", "unit": "rad/s²", "digits": 4}, {"label": "a_r = a_x x/r", "expr": "ax*u/sqrt(u^2 + z0^2)", "unit": "m/s²", "digits": 4}, {"label": "a_θ = −a_x y0/r", "expr": "-ax*z0/sqrt(u^2 + z0^2)", "unit": "m/s²", "digits": 4}, {"label": "|a| = √(a_r² + a_θ²), equal to |a_x|", "expr": "sqrt((ax*u/sqrt(u^2 + z0^2))^2 + (ax*z0/sqrt(u^2 + z0^2))^2)", "unit": "m/s²", "digits": 4}], "vectors": [{"label": "e_r", "at": ["x", "y", "z"], "comp": ["u/sqrt(u^2 + z0^2)", "0", "z0/sqrt(u^2 + z0^2)"], "scale": 0.6, "cls": "m3-b1"}, {"label": "e_θ", "at": ["x", "y", "z"], "comp": ["-z0/sqrt(u^2 + z0^2)", "0", "u/sqrt(u^2 + z0^2)"], "scale": 0.6, "cls": "m3-b1"}, {"label": "a", "at": ["x", "y", "z"], "comp": ["ax", "0", "0"], "scale": 1, "cls": "m3-acc"}]}

## Problem 05: Plane and Glider

### Reference Frames, Bases and Coordinates

The airplane $A$ and the glider $B$ are modelled as point particles that move in one vertical plane. The answer is asked in the fixed (ground) frame, so the velocity and acceleration of $B$ are the derivatives of its position vector in $S_0$. Only the tools of chapters 1 and 2 of Notes.pdf are used: the position of $B$ is written as the position of $A$ plus the vector from $A$ to $B$, and that sum is differentiated; no theorem of relative motion is needed.

| Symbol | Meaning | Units |
| :--- | :--- | :--- |
| $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ | fixed frame; $O$ on the flight line of $A$ at the position of $A$ at the initial instant; $\mathbf i_0$ horizontal, in the direction of flight; $\mathbf j_0$ vertical, upward; $\mathbf k_0$ out of the paper (⊙) | - |
| $B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k_0\}$ | cable basis: $\mathbf i_1$ unit vector from $A$ to $B$ along the cable; $\mathbf j_1 = \mathbf k_0 \times \mathbf i_1$ | - |
| $v_A$ | constant speed of $A$ along $\mathbf i_0$ | m/s |
| $r$ | constant length of the taut cable | m |
| $\theta(t)$ | angle between the cable and the horizontal, measured from $-\mathbf i_0$ (behind $A$) up to the cable | rad |
| $\varphi(t)$ | standard polar angle of $\mathbf i_1$, measured counterclockwise from $\mathbf i_0$ with $\mathbf k_0$ ⊙ | rad |
| $\dot\theta$ | rate of the cable angle, constant and positive (statement) | rad/s |

Hypotheses and degrees of freedom:

- The airplane flies in a straight horizontal line at constant speed, so its motion is prescribed.
- The cable is taut and of fixed length, so $B$ stays on a circle of radius $r$ centred at $A$: a holonomic constraint that depends on time through the position of $A$. The glider keeps one degree of freedom, the angle $\theta$.
- Reading of the statement: the glider is towed, so it is behind $A$; it gains altitude while $\theta$ grows, so it is above the flight line of $A$ with $\theta$ between zero and a right angle. This is the only reading in which a growing angle raises the glider.
- The answer is kept for a general function $\theta(t)$, as the statement asks ("as a function of $\theta$ and its derivatives"), and then particularised to the constant rate.
- The forces section is omitted: the problem has no dynamics.

![[attachments/EM-SOL/p05-cable-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p05-rotation-view.svg]]

> [!derivation] Polar angle of the cable from the angle with the horizontal
> **Law:** relation between an angle measured from $-\mathbf i_0$ and the standard polar angle measured from $\mathbf i_0$
> **Source:** Notes.pdf, Eq. 2.23; Problems.pdf, p. 7
>
> The direction $-\mathbf i_0$ has polar angle $\pi$. The cable is reached from $-\mathbf i_0$ by turning $\theta$ clockwise (toward $+\mathbf j_0$ from the left side), that is, by turning $-\theta$ in the positive sense about $\mathbf k_0$ ⊙.
>
> $$\begin{aligned}
> \varphi &= \pi - \theta \quad &\text{(polar angle of $-\mathbf i_0$ minus the clockwise turn $\theta$)} \\
> \cos\varphi &= \cos\pi\cos\theta + \sin\pi\sin\theta = -\cos\theta \quad &\text{(cosine of a difference; $\cos\pi$ is $-1$, $\sin\pi$ is 0)} \\
> \sin\varphi &= \sin\pi\cos\theta - \cos\pi\sin\theta = \sin\theta \quad &\text{(sine of a difference)} \\
> \dot\varphi &= -\dot\theta \quad &\text{(chain rule; $\pi$ is constant)}
> \end{aligned}$$
>
> $$\boxed{\varphi = \pi - \theta,\qquad \cos\varphi = -\cos\theta,\qquad \sin\varphi = \sin\theta,\qquad \dot\varphi = -\dot\theta}$$
>
> **Units:** angles $[1]$ (rad); rates $[\mathrm{T^{-1}}]$
> **Meaning:** a growing angle with the horizontal is a clockwise turn of the cable, seen with $\mathbf k_0$ out of the paper.

> [!derivation] Cable basis and the change of basis matrix
> **Law:** rotation of the basis by the polar angle about $\mathbf k_0$; definition of the change of basis matrix
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.15
>
> In the plane of the motion, the unit vector $\mathbf i_1$ is the hypotenuse of a right triangle whose horizontal leg, adjacent to $\theta$, points toward $-\mathbf i_0$ (the glider is behind) and whose vertical leg, opposite to $\theta$, points toward $+\mathbf j_0$ (the glider is above). The vector $\mathbf j_1$ is $\mathbf i_1$ turned a right angle counterclockwise about $\mathbf k_0$ ⊙ (right-hand rule), so it points down and back: both of its components are negative.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\varphi\,\mathbf i_0 + \sin\varphi\,\mathbf j_0 = -\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(adjacent leg toward $-\mathbf i_0$, opposite leg toward $+\mathbf j_0$)} \\
> \mathbf j_1 &= \mathbf k_0 \times \mathbf i_1 = -\cos\theta\,(\mathbf k_0 \times \mathbf i_0) + \sin\theta\,(\mathbf k_0 \times \mathbf j_0) \quad &\text{(distributive property of the vector product)} \\
> &= -\cos\theta\,\mathbf j_0 - \sin\theta\,\mathbf i_0 \quad &\text{(right-handed products: k0 cross i0 is j0, k0 cross j0 is minus i0)} \\
> \det[{}_0R_1] &= 1\cdot\left((-\cos\theta)(-\cos\theta) - (-\sin\theta)(\sin\theta)\right) \quad &\text{(expansion along the third row)} \\
> &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(Pythagorean identity)} \\
> ([{}_0R_1][{}_0R_1]^T)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> ([{}_0R_1][{}_0R_1]^T)_{12} &= (-\cos\theta)(\sin\theta) + (-\sin\theta)(-\cos\theta) = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_1][{}_0R_1]^T)_{22} &= \sin^2\theta + \cos^2\theta = 1 \quad &\text{(row 2 times row 2; third row and column as the identity)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} -\cos\theta & -\sin\theta & 0 \\ \sin\theta & -\cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix},\qquad \det[{}_0R_1] = 1,\qquad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[1]$ for every entry
> **Meaning:** the columns are the cable unit vectors written in the fixed basis; the matrix is the rotation of Notes.pdf, Eq. 1.20 with the polar angle of the cable.

> [!derivation] Fixed unit vectors written in the cable basis
> **Law:** inverse change of basis equals the transpose
> **Source:** Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> [{}_1R_0] &= [{}_0R_1]^T \quad &\text{(orthogonality)} \\
> \mathbf i_0 &= -\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1 \quad &\text{(first row of $[{}_0R_1]$)} \\
> \mathbf j_0 &= \sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j_1 \quad &\text{(second row of $[{}_0R_1]$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_0 = -\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1}$$
>
> **Units:** $[1]$
> **Meaning:** the direction of flight seen from the cable basis; it is used for the second computation of the speed.

> [!derivation] Position vector of the glider
> **Law:** definition of the position vector as a sum of two segments
> **Source:** Notes.pdf, Eq. 2.2; Problems.pdf, p. 7
>
> $$\begin{aligned}
> \mathbf r_0^A &= v_A t\,\mathbf i_0 \quad &\text{(uniform motion of $A$ from $O$ along $\mathbf i_0$)} \\
> \overrightarrow{AB} &= r\,\mathbf i_1 \quad &\text{(cable of length $r$ along $\mathbf i_1$)} \\
> \mathbf r_0^B &= \overrightarrow{OA} + \overrightarrow{AB} = v_A t\,\mathbf i_0 + r\,\mathbf i_1 \quad &\text{(sum of segments)} \\
> &= (v_A t - r\cos\theta)\,\mathbf i_0 + r\sin\theta\,\mathbf j_0 \quad &\text{(components of $\mathbf i_1$; adjacent leg $r\cos\theta$, opposite leg $r\sin\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^B = v_A t\,\mathbf i_0 + r\,\mathbf i_1 = (v_A t - r\cos\theta)\,\mathbf i_0 + r\sin\theta\,\mathbf j_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$ and $[\mathrm{L}]$
> **Meaning:** the glider is at the position of the airplane moved back by the horizontal leg of the cable and up by its vertical leg; its height grows with the angle.

### Kinematics

> [!derivation] Derivatives of the cable unit vectors
> **Law:** derivative of a unit vector rotating with angular velocity $\boldsymbol\omega$; vector products written out
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.56
>
> $$\begin{aligned}
> \boldsymbol\omega_{1,0} &= \dot\varphi\,\mathbf k_0 = -\dot\theta\,\mathbf k_0 \quad &\text{(rotation about $\mathbf k_0$ by the polar angle; previous box)} \\
> \dot{\mathbf i}_1 &= -\dot\theta\,\mathbf k_0 \times \mathbf i_1 = -\dot\theta\,\mathbf j_1 \quad &\text{(Notes Eq. 1.62; definition of $\mathbf j_1$)} \\
> \mathbf k_0 \times \mathbf j_1 &= -\sin\theta\,(\mathbf k_0 \times \mathbf i_0) - \cos\theta\,(\mathbf k_0 \times \mathbf j_0) \quad &\text{(distributive property)} \\
> &= -\sin\theta\,\mathbf j_0 + \cos\theta\,\mathbf i_0 = -\mathbf i_1 \quad &\text{(right-handed products; components of $\mathbf i_1$)} \\
> \dot{\mathbf j}_1 &= -\dot\theta\,\mathbf k_0 \times \mathbf j_1 = \dot\theta\,\mathbf i_1 \quad &\text{(Notes Eq. 1.62 and the line above)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_1 = -\dot\theta\,\mathbf j_1,\qquad \dot{\mathbf j}_1 = \dot\theta\,\mathbf i_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the cable basis turns clockwise at the rate of the cable angle; the tip of the unit vector along the cable moves along minus j1, that is, up and forward.

> [!derivation] Velocity of the glider
> **Law:** time derivative of the position vector in $S_0$ with the product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 1.63
>
> $$\begin{aligned}
> \mathbf v_0^B &= \frac{d}{dt}\left(v_A t\,\mathbf i_0 + r\,\mathbf i_1\right) \quad &\text{(definition of velocity)} \\
> &= v_A\,\mathbf i_0 + \dot r\,\mathbf i_1 + r\,\dot{\mathbf i}_1 \quad &\text{(product rule; $\mathbf i_0$ is fixed in $S_0$)} \\
> &= v_A\,\mathbf i_0 - r\dot\theta\,\mathbf j_1 \quad &\text{($r$ constant; derivative of $\mathbf i_1$)} \\
> &= v_A\,\mathbf i_0 - r\dot\theta\left(-\sin\theta\,\mathbf i_0 - \cos\theta\,\mathbf j_0\right) \quad &\text{(components of $\mathbf j_1$)} \\
> &= \left(v_A + r\dot\theta\sin\theta\right)\mathbf i_0 + r\dot\theta\cos\theta\,\mathbf j_0 \quad &\text{(grouping by unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^B = \left(v_A + r\dot\theta\sin\theta\right)\mathbf i_0 + r\dot\theta\cos\theta\,\mathbf j_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L}][\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the glider moves with the airplane plus a velocity of magnitude $r$ times the angular rate, perpendicular to the cable, pointing forward and upward.

> [!derivation] Speed of the glider
> **Law:** magnitude of a vector from its orthonormal components
> **Source:** Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \left(v_0^B\right)^2 &= \left(v_A + r\dot\theta\sin\theta\right)^2 + \left(r\dot\theta\cos\theta\right)^2 \quad &\text{(sum of the squares of the components)} \\
> &= v_A^2 + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2\sin^2\theta + r^2\dot\theta^2\cos^2\theta \quad &\text{(expanding the squares)} \\
> &= v_A^2 + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2 \quad &\text{(Pythagorean identity)}
> \end{aligned}$$
>
> $$\boxed{v_0^B = \sqrt{\left(v_A + r\dot\theta\sin\theta\right)^2 + \left(r\dot\theta\cos\theta\right)^2} = \sqrt{v_A^2 + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the speed is largest when the cable is vertical, where the velocity of the glider relative to the airplane is horizontal and adds fully to the flight speed.

> [!derivation] Acceleration of the glider
> **Law:** time derivative of the velocity in $S_0$ with the product rule and the derivatives of the cable unit vectors
> **Source:** Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 1.63
>
> $$\begin{aligned}
> \mathbf a_0^B &= \frac{d}{dt}\left(v_A\,\mathbf i_0 - r\dot\theta\,\mathbf j_1\right) \quad &\text{(definition of acceleration)} \\
> &= \dot v_A\,\mathbf i_0 - r\ddot\theta\,\mathbf j_1 - r\dot\theta\,\dot{\mathbf j}_1 \quad &\text{(product rule; $r$ constant)} \\
> &= 0 - r\ddot\theta\,\mathbf j_1 - r\dot\theta\left(\dot\theta\,\mathbf i_1\right) \quad &\text{($v_A$ constant; derivative of $\mathbf j_1$)} \\
> &= -r\dot\theta^2\,\mathbf i_1 - r\ddot\theta\,\mathbf j_1 \quad &\text{(grouping by unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^B = -r\dot\theta^2\,\mathbf i_1 - r\ddot\theta\,\mathbf j_1}$$
>
> **Units:** $[\mathrm{L}][\mathrm{T^{-2}}] = [\mathrm{L\,T^{-2}}]$ for both terms
> **Meaning:** the airplane does not accelerate, so the glider accelerates only through its circular motion about the airplane: a centripetal part along the cable toward $A$ and a tangential part due to the angular acceleration.

> [!derivation] Magnitude of the acceleration
> **Law:** magnitude from orthonormal components
> **Source:** Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \left(a_0^B\right)^2 &= \left(-r\dot\theta^2\right)^2 + \left(-r\ddot\theta\right)^2 \quad &\text{($B_1$ is orthonormal)} \\
> &= r^2\dot\theta^4 + r^2\ddot\theta^2 \quad &\text{(squares)}
> \end{aligned}$$
>
> $$\boxed{a_0^B = \sqrt{r^2\ddot\theta^2 + r^2\dot\theta^4}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the magnitude does not depend on the flight speed or on the angle, only on the angular rate and acceleration of the cable.

![[attachments/EM-SOL/p05-velocity-acceleration.svg]]

### Answers and Checks

> [!derivation] Answer: magnitudes of the velocity and acceleration of the glider
> **Law:** results of the kinematics, for a general angle and for the constant rate of the statement
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> v_0^B &= \sqrt{\left(v_A + r\dot\theta\sin\theta\right)^2 + \left(r\dot\theta\cos\theta\right)^2} \quad &\text{(speed of the glider)} \\
> a_0^B &= \sqrt{r^2\ddot\theta^2 + r^2\dot\theta^4} \quad &\text{(general angle law)} \\
> \ddot\theta &= 0 \quad &\text{(constant rate of the statement)} \\
> a_0^B &= \sqrt{r^2\dot\theta^4} = r\dot\theta^2 \quad &\text{(positive root)}
> \end{aligned}$$
>
> $$\boxed{v_0^B = \sqrt{\left(v_A + r\dot\theta\sin\theta\right)^2 + \left(r\dot\theta\cos\theta\right)^2},\qquad a_0^B = \sqrt{r^2\ddot\theta^2 + r^2\dot\theta^4}\ \ \left(= r\dot\theta^2\ \text{at constant rate}\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** with the constant rate the acceleration is purely centripetal, directed along the cable toward the airplane.

> [!derivation] Second computation of the speed, in the cable basis
> **Law:** change of basis of the flight direction; norm in an orthonormal basis
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \mathbf v_0^B &= v_A\left(-\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1\right) - r\dot\theta\,\mathbf j_1 \quad &\text{($\mathbf i_0$ written in $B_1$)} \\
> &= -v_A\cos\theta\,\mathbf i_1 - \left(v_A\sin\theta + r\dot\theta\right)\mathbf j_1 \quad &\text{(grouping)} \\
> \left(v_0^B\right)^2 &= v_A^2\cos^2\theta + v_A^2\sin^2\theta + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2 \quad &\text{(squares of the components)} \\
> &= v_A^2 + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2 \quad &\text{(Pythagorean identity)}
> \end{aligned}$$
>
> $$\boxed{\left(v_0^B\right)^2 = v_A^2 + 2v_A r\dot\theta\sin\theta + r^2\dot\theta^2\ \text{in both bases}}$$
>
> **Units:** $[\mathrm{L^2T^{-2}}]$
> **Meaning:** the speed is independent of the basis, as the orthogonality of the change of basis matrix requires.

> [!derivation] Second computation of the acceleration, in the fixed basis
> **Law:** derivative of the Cartesian components with the product and chain rules
> **Source:** Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \frac{d}{dt}\left(v_A + r\dot\theta\sin\theta\right) &= r\ddot\theta\sin\theta + r\dot\theta^2\cos\theta \quad &\text{(product rule; chain rule on $\sin\theta$)} \\
> \frac{d}{dt}\left(r\dot\theta\cos\theta\right) &= r\ddot\theta\cos\theta - r\dot\theta^2\sin\theta \quad &\text{(product rule; chain rule on $\cos\theta$)} \\
> -r\dot\theta^2\,\mathbf i_1 - r\ddot\theta\,\mathbf j_1 &= -r\dot\theta^2\left(-\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0\right) - r\ddot\theta\left(-\sin\theta\,\mathbf i_0 - \cos\theta\,\mathbf j_0\right) \quad &\text{(cable basis written in the fixed basis, with $\mathbf i_1$ and $\mathbf j_1$ of the change of basis)} \\
> &= \left(r\dot\theta^2\cos\theta + r\ddot\theta\sin\theta\right)\mathbf i_0 + \left(r\ddot\theta\cos\theta - r\dot\theta^2\sin\theta\right)\mathbf j_0 \quad &\text{(collect the components of $\mathbf i_0$ and $\mathbf j_0$; equal to the boxed result)} \\
> \left(a_0^B\right)^2 &= r^2\ddot\theta^2(\sin^2\theta + \cos^2\theta) + r^2\dot\theta^4(\cos^2\theta + \sin^2\theta) \quad &\text{(sum of squares; the cross terms in $\sin\theta\cos\theta$ cancel)} \\
> &= r^2\ddot\theta^2 + r^2\dot\theta^4 \quad &\text{(Pythagorean identity)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^B = \left(r\ddot\theta\sin\theta + r\dot\theta^2\cos\theta\right)\mathbf i_0 + \left(r\ddot\theta\cos\theta - r\dot\theta^2\sin\theta\right)\mathbf j_0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the same magnitude as in the cable basis; the projection of the cable vectors onto the fixed basis, written in the row above, gives the same two components.

> [!derivation] Limiting cases
> **Law:** evaluation of the results in special configurations
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> \dot\theta \equiv 0 &\Rightarrow \mathbf v_0^B = v_A\,\mathbf i_0,\quad \mathbf a_0^B = \mathbf 0 \quad &\text{(the glider moves rigidly with the airplane)} \\
> \theta = 0 &\Rightarrow v_0^B = \sqrt{v_A^2 + r^2\dot\theta^2} \quad &\text{(cable horizontal: relative velocity vertical, perpendicular to the flight)} \\
> \theta = \tfrac{\pi}{2} &\Rightarrow v_0^B = v_A + r\dot\theta \quad &\text{(cable vertical: relative velocity horizontal, forward)}
> \end{aligned}$$
>
> $$\boxed{v_A \le v_0^B \le v_A + r\dot\theta\ \text{for}\ 0 \le \theta \le \tfrac{\pi}{2}\ \text{and positive rate}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the results reduce to the straight and the circular configurations when $\dot\theta$ or $\ddot\theta$ vanishes; the acceleration never depends on the flight speed because the airplane does not accelerate.

Check against the official key: Problems.pdf, p. 72, item 5, gives the speed of the glider as the square root of the sum of the squares of the two Cartesian components found above and the acceleration as the square root of the sum of the squared tangential and centripetal terms. Both coincide exactly with the boxed answers; they were also obtained by two independent routes (cable basis and fixed basis).

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Glider on its cable, seen in the vertical plane (Problem 05)", "intro": "Sample values: cable r = 1.5 m, v_A = 2 m/s, θ̇ = 0.5 rad/s constant (θ̈ zero). The top view is the vertical plane of the flight: i0 forward, j0 up, A at the origin. The circle is the path of B relative to A; the slider is the polar angle φ = π − θ of the cable, and the default θ = 30° is a sample angle (the statement gives none). The pink arrows are v_A at A and the absolute velocity v_B of the glider (scaled by 0.4); the speed of the archetype is the relative speed r θ̇ only. The right view is the rotation of angle φ about k0 that takes B0 to the cable basis.", "params": {"curve": "circle", "R": 1.5, "rate": -0.5, "accel": 0, "umin": 90, "umax": 180, "extent": 2.2, "vA": 2.0, "r": 1.5, "thetadot": 0.5, "thetaddot": 0.0}, "defaults": {"u": 150}, "view": "top", "sliders": {"u": {"label": "Polar angle φ = π − θ of the cable"}}, "readouts": [{"label": "Cable angle θ = π − φ", "expr": "deg(pi - u)", "unit": "deg", "digits": 2}, {"label": "v_B · i0 = v_A + r θ̇ sin θ", "expr": "vA + r*thetadot*sin(pi - u)", "unit": "m/s", "digits": 4}, {"label": "v_B · j0 = r θ̇ cos θ", "expr": "r*thetadot*cos(pi - u)", "unit": "m/s", "digits": 4}, {"label": "v_B = √((v_A + r θ̇ sin θ)² + (r θ̇ cos θ)²)", "expr": "sqrt((vA + r*thetadot*sin(pi - u))^2 + (r*thetadot*cos(pi - u))^2)", "unit": "m/s", "digits": 4}, {"label": "v_B from the cable basis, √(v_A² + 2 v_A r θ̇ sin θ + r² θ̇²)", "expr": "sqrt(vA^2 + 2*vA*r*thetadot*sin(pi - u) + r^2*thetadot^2)", "unit": "m/s", "digits": 4}, {"label": "a_B · i0 = r θ̈ sin θ + r θ̇² cos θ", "expr": "r*thetaddot*sin(pi - u) + r*thetadot^2*cos(pi - u)", "unit": "m/s²", "digits": 4}, {"label": "a_B · j0 = r θ̈ cos θ − r θ̇² sin θ", "expr": "r*thetaddot*cos(pi - u) - r*thetadot^2*sin(pi - u)", "unit": "m/s²", "digits": 4}, {"label": "a_B = √(r² θ̈² + r² θ̇⁴), r θ̇² at constant rate", "expr": "sqrt(r^2*thetaddot^2 + r^2*thetadot^4)", "unit": "m/s²", "digits": 4}], "vectors": [{"label": "v_A", "at": ["0", "0", "0"], "comp": ["vA", "0", "0"], "scale": 0.4, "cls": "m3-w"}, {"label": "v_B", "at": ["x", "y", "z"], "comp": ["vA + r*thetadot*sin(pi - u)", "r*thetadot*cos(pi - u)", "0"], "scale": 0.4, "cls": "m3-w"}]}

## Problem 06: Particle on Sinusoidal Curve

### Reference Frames, Bases and Coordinates

The particle $P$ moves on a fixed plane curve, the graph of the sine function, with a prescribed horizontal rate. The intrinsic (Frenet-Serret) basis of the trajectory is built from the definitions of Notes.pdf, Sec. 2.4, and the accelerations from the definitions of Sec. 2.5.

| Symbol | Meaning | Units |
| :--- | :--- | :--- |
| $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ | fixed frame; the curve lies in the plane of $\mathbf i_0$ (right) and $\mathbf j_0$ (up); $\mathbf k_0$ out of the paper (⊙) | - |
| $B_F = \{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ | intrinsic basis at $P$: tangent, principal normal (toward the centre of curvature), binormal $\mathbf e_t \times \mathbf e_n$ | - |
| $\mathbf e_\perp$ | auxiliary unit normal, $\mathbf k_0 \times \mathbf e_t$ (the tangent turned a right angle counterclockwise) | - |
| $x$, $y$ | Cartesian coordinates of $P$; the curve is $y = \sin x$ | m |
| $\gamma$ | angle from $\mathbf i_0$ to $\mathbf e_t$, counterclockwise with $\mathbf k_0$ ⊙ (the angle of Notes.pdf, Eq. 2.19) | rad |
| $s$ | arc length along the curve, measured from the origin $O$ | m |
| $L(x)$ | metric factor $\sqrt{1 + \cos^2 x}$, the arc length per unit of abscissa | - |
| $\dot x = 1$ | prescribed horizontal rate | m/s |
| $\sigma$ | sign that orients the normal toward the centre of curvature, $\sigma = -\operatorname{sgn}(\sin x)$ | - |

Hypotheses and degrees of freedom:

- The data are read in SI units: the sine curve carries a length scale $\ell$ of 1 m (height and abscissa in metres, the argument of the sine in units of $\ell$) and the horizontal rate is 1 m/s; with that length scale every formula below keeps its dimensions.
- The particle starts at the origin, so at the initial instant $x$ is zero and the arc length is measured from there.
- The curve is a holonomic, time-independent constraint in the plane: one degree of freedom, the abscissa $x$, whose time law is given. There is no dynamics, so the forces section is omitted.
- At the inflection points (zero $\sin x$) the curvature vanishes and the principal normal is not defined (Notes.pdf, footnote 12 of Sec. 2.4); the intrinsic basis is given for the other points.

![[attachments/EM-SOL/p06-curve-plane.svg]]

### Change of Basis and Position Vector

> [!derivation] Position vector and arc length element
> **Law:** definition of the position vector; length of the differential displacement along the curve
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.19
>
> The differential displacement along the curve is the hypotenuse of a right triangle whose horizontal leg is the increment of abscissa and whose vertical leg is the increment of height.
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i_0 + \sin x\,\mathbf j_0 \quad &\text{(Cartesian coordinates of a point of the curve)} \\
> \frac{d\mathbf r_0^P}{dx} &= \mathbf i_0 + \cos x\,\mathbf j_0 \quad &\text{(derivative with respect to $x$; $\tfrac{d}{dx}\sin x = \cos x$)} \\
> dy &= \cos x\,dx \quad &\text{(vertical leg of the differential triangle)} \\
> ds^2 &= dx^2 + dy^2 = (1 + \cos^2 x)\,dx^2 \quad &\text{(Pythagoras in the differential triangle)} \\
> ds &= \sqrt{1 + \cos^2 x}\,dx = L\,dx \quad &\text{(positive root: $s$ grows with $x$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i_0 + \sin x\,\mathbf j_0,\qquad ds = L(x)\,dx,\quad L(x) = \sqrt{1 + \cos^2 x}}$$
>
> **Units:** $[\mathrm{L}]$ for the position; $L$ is $[\mathrm{L}]/[\mathrm{L}] = [1]$
> **Meaning:** the metric factor lies between 1 (at the crests, where the curve is horizontal) and the square root of 2 (at the inflection points, where the slope is 1 in magnitude).

> [!derivation] Tangent unit vector and its angle
> **Law:** the tangent unit vector is the derivative of the position with respect to the arc length
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.19
>
> In the differential triangle the hypotenuse is the arc element, the leg adjacent to the angle of the tangent is the horizontal increment and the opposite leg is the vertical increment.
>
> $$\begin{aligned}
> \mathbf e_t &= \frac{d\mathbf r_0^P}{ds} = \frac{d\mathbf r_0^P}{dx}\,\frac{dx}{ds} \quad &\text{(chain rule)} \\
> &= \frac{\mathbf i_0 + \cos x\,\mathbf j_0}{L} \quad &\text{(derivative of the previous box; $dx/ds$ is $1/L$)} \\
> \cos\gamma &= \frac{dx}{ds} = \frac{1}{L} \quad &\text{(adjacent leg over hypotenuse)} \\
> \sin\gamma &= \frac{dy}{ds} = \frac{\cos x}{L} \quad &\text{(opposite leg over hypotenuse)} \\
> \tan\gamma &= \cos x \quad &\text{(quotient: the slope of the curve)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = \frac{\mathbf i_0 + \cos x\,\mathbf j_0}{\sqrt{1 + \cos^2 x}} = \cos\gamma\,\mathbf i_0 + \sin\gamma\,\mathbf j_0,\qquad \gamma = \arctan(\cos x)}$$
>
> **Units:** $[1]$
> **Meaning:** the tangent always points forward (positive horizontal component) and its angle swings between minus and plus 45 degrees, reached at the inflection points.

![[attachments/EM-SOL/p06-rotation-view.svg]]

> [!derivation] Auxiliary normal and the change of basis to the tangent basis
> **Law:** rotation of the basis by the angle of the tangent about $\mathbf k_0$; change of basis matrix
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15
>
> The auxiliary normal is the tangent turned a right angle counterclockwise about $\mathbf k_0$ ⊙ (right-hand rule). In the view along $\mathbf k_0$ its leg adjacent to the angle of the tangent lies along $\mathbf j_0$ and its opposite leg points toward $-\mathbf i_0$, which explains the minus sign.
>
> $$\begin{aligned}
> \mathbf e_\perp &= \mathbf k_0 \times \mathbf e_t = \cos\gamma\,(\mathbf k_0 \times \mathbf i_0) + \sin\gamma\,(\mathbf k_0 \times \mathbf j_0) \quad &\text{(distributive property)} \\
> &= \cos\gamma\,\mathbf j_0 - \sin\gamma\,\mathbf i_0 \quad &\text{(right-handed products: k0 cross i0 is j0, k0 cross j0 is minus i0)} \\
> &= \frac{-\cos x\,\mathbf i_0 + \mathbf j_0}{L} \quad &\text{(sine and cosine of the angle of the tangent)} \\
> \det[{}_0R_\gamma] &= 1\cdot(\cos^2\gamma + \sin^2\gamma) = 1 \quad &\text{(expansion along the third row)} \\
> ([{}_0R_\gamma][{}_0R_\gamma]^T)_{12} &= \cos\gamma\sin\gamma - \sin\gamma\cos\gamma = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_\gamma][{}_0R_\gamma]^T)_{11} &= ([{}_0R_\gamma][{}_0R_\gamma]^T)_{22} = \cos^2\gamma + \sin^2\gamma = 1 \quad &\text{(rows of unit length)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_\gamma] = \frac{1}{L}\begin{pmatrix} 1 & -\cos x & 0 \\ \cos x & 1 & 0 \\ 0 & 0 & L \end{pmatrix},\qquad \det = 1,\qquad RR^T = I}$$
>
> **Units:** $[1]$
> **Meaning:** the columns are the tangent, the auxiliary normal and the out-of-plane vector written in the fixed basis; the pair turns with the slope of the curve.

### Kinematics

> [!derivation] Time law, velocity and speed
> **Law:** definition of velocity in $S_0$; chain rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.16; Problems.pdf, p. 7
>
> $$\begin{aligned}
> x(t) &= x(0) + \int_0^t 1\,dt' = 0 + [t']_0^t = t \quad &\text{(prescribed rate; Barrow's rule)} \\
> \mathbf v_0^P &= \dot x\,\mathbf i_0 + \frac{d}{dt}(\sin x)\,\mathbf j_0 \quad &\text{(derivative of the position; fixed basis)} \\
> &= \dot x\,\mathbf i_0 + \cos x\,\dot x\,\mathbf j_0 \quad &\text{(chain rule)} \\
> &= \mathbf i_0 + \cos x\,\mathbf j_0 = L\,\mathbf e_t \quad &\text{(unit horizontal rate; tangent of the previous section)} \\
> \dot s &= \frac{ds}{dx}\,\dot x = L \quad &\text{(chain rule with the arc element)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \mathbf i_0 + \cos x\,\mathbf j_0 = \dot s\,\mathbf e_t,\qquad \dot s = v = \sqrt{1 + \cos^2 x}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the velocity is tangent to the curve, as Notes.pdf, Eq. 2.16 states; the speed is largest at the inflection points, where the curve is steepest.

> [!derivation] Rotation rate of the tangent and derivatives of the unit vectors
> **Law:** derivative of a unit vector rotating with angular velocity $\boldsymbol\omega$; vector products written out
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.56
>
> $$\begin{aligned}
> \dot\gamma &= \frac{d}{dt}\arctan(\cos x) = \frac{1}{1 + \cos^2 x}\,\frac{d}{dt}\cos x \quad &\text{(chain rule; derivative of the arctangent)} \\
> &= \frac{-\sin x\,\dot x}{1 + \cos^2 x} = -\frac{\sin x}{L^2} \quad &\text{(chain rule; unit horizontal rate)} \\
> \boldsymbol\omega_{\gamma,0} &= \dot\gamma\,\mathbf k_0 \quad &\text{(rotation about $\mathbf k_0$ by $\gamma$)} \\
> \dot{\mathbf e}_t &= \dot\gamma\,\mathbf k_0 \times (\cos\gamma\,\mathbf i_0 + \sin\gamma\,\mathbf j_0) \quad &\text{(Notes Eq. 1.62)} \\
> &= \dot\gamma\,(\cos\gamma\,\mathbf j_0 - \sin\gamma\,\mathbf i_0) = \dot\gamma\,\mathbf e_\perp \quad &\text{(right-handed products; definition of $\mathbf e_\perp$)} \\
> \dot{\mathbf e}_\perp &= \dot\gamma\,\mathbf k_0 \times (-\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0) \quad &\text{(Notes Eq. 1.62)} \\
> &= \dot\gamma\left(-\sin\gamma\,(\mathbf k_0\times\mathbf i_0) + \cos\gamma\,(\mathbf k_0\times\mathbf j_0)\right) \quad &\text{(distribute $\mathbf k_0\times$ over the two terms)} \\
> &= \dot\gamma\left(-\sin\gamma\,\mathbf j_0 - \cos\gamma\,\mathbf i_0\right) = -\dot\gamma\,\mathbf e_t \quad &\text{($\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$; definition of $\mathbf e_t$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_t = -\frac{\sin x}{L^2}\,\mathbf e_\perp,\qquad \dot{\mathbf e}_\perp = \frac{\sin x}{L^2}\,\mathbf e_t}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** on the arches above the axis the tangent turns clockwise, on the arches below it turns counterclockwise; it stops turning at the inflection points.

#### (a) Intrinsic unit basis

> [!derivation] Curvature and principal normal
> **Law:** derivative of the tangent with respect to the arc length; definition of the normal and of the curvature
> **Source:** Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; Notes.pdf, Eq. 2.15
>
> $$\begin{aligned}
> \frac{d\mathbf e_t}{ds} &= \frac{\dot{\mathbf e}_t}{\dot s} \quad &\text{(chain rule: derivative in time over the rate of $s$)} \\
> &= -\frac{\sin x}{L^3}\,\mathbf e_\perp \quad &\text{(previous two boxes)} \\
> \left|\frac{d\mathbf e_t}{ds}\right| &= \frac{|\sin x|}{L^3} = \kappa = \frac{1}{\rho} \quad &\text{(norm; $\mathbf e_\perp$ is a unit vector)} \\
> \mathbf e_n &= \frac{d\mathbf e_t/ds}{|d\mathbf e_t/ds|} = -\operatorname{sgn}(\sin x)\,\mathbf e_\perp = \sigma\,\mathbf e_\perp \quad &\text{(division by the norm, nonzero $\sin x$)} \\
> &= \sigma\,\frac{-\cos x\,\mathbf i_0 + \mathbf j_0}{L} \quad &\text{(components of $\mathbf e_\perp$)} \\
> \mathbf e_b &= \mathbf e_t \times \mathbf e_n = \sigma\,\mathbf e_t \times (\mathbf k_0 \times \mathbf e_t) \quad &\text{(definition of the binormal)} \\
> &= \sigma\left((\mathbf e_t\cdot\mathbf e_t)\,\mathbf k_0 - (\mathbf e_t\cdot\mathbf k_0)\,\mathbf e_t\right) = \sigma\,\mathbf k_0 \quad &\text{(double vector product, Notes Eq. 1.37; $\mathbf e_t$ lies in the plane)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = \frac{\mathbf i_0 + \cos x\,\mathbf j_0}{\sqrt{1 + \cos^2 x}},\quad \mathbf e_n = \operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf i_0 - \mathbf j_0}{\sqrt{1 + \cos^2 x}},\quad \mathbf e_b = -\operatorname{sgn}(\sin x)\,\mathbf k_0}$$
>
> **Units:** $[1]$ for the unit vectors; $\kappa$ is $[\mathrm{L^{-1}}]$
> **Meaning:** on the arches above the axis the curve is concave down and the normal points down, toward the centre of curvature below; on the arches below the axis it points up. The binormal is constant on each arch and flips at each inflection point.

> [!derivation] Change of basis matrix to the intrinsic basis
> **Law:** columns are the intrinsic unit vectors in the fixed basis; orthogonality and determinant checked
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 2.13
>
> $$\begin{aligned}
> \det[{}_0R_F] &= \sigma\cdot\left(\frac{1}{L}\cdot\frac{\sigma}{L} - \frac{-\sigma\cos x}{L}\cdot\frac{\cos x}{L}\right) \quad &\text{(expansion along the third row)} \\
> &= \sigma^2\,\frac{1 + \cos^2 x}{L^2} = 1 \quad &\text{($\sigma^2$ is 1; definition of $L$)} \\
> (RR^T)_{11} &= \frac{1 + \cos^2 x}{L^2} = 1,\quad (RR^T)_{22} = \frac{\cos^2 x + 1}{L^2} = 1 \quad &\text{(rows 1 and 2 of unit length)} \\
> (RR^T)_{12} &= \frac{\cos x - \sigma^2\cos x}{L^2} = 0,\quad (RR^T)_{33} = \sigma^2 = 1 \quad &\text{(rows 1 and 2 orthogonal; row 3 unit)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_F] = \frac{1}{L}\begin{pmatrix} 1 & -\sigma\cos x & 0 \\ \cos x & \sigma & 0 \\ 0 & 0 & \sigma L \end{pmatrix},\qquad \det[{}_0R_F] = 1,\qquad [{}_0R_F][{}_0R_F]^T = I}$$
>
> **Units:** $[1]$
> **Meaning:** the intrinsic basis is right-handed on every arch: when the normal flips, the binormal flips too, so the determinant stays 1.

#### (b) Abscissa as a function of the arc length

> [!derivation] Arc length as an integral and its inversion
> **Law:** integration of the arc element with Barrow's rule; inverse of a strictly increasing function
> **Source:** Notes.pdf, Sec. 2.3; Notes.pdf, Eq. 2.19
>
> $$\begin{aligned}
> s(x) &= \int_0^x \frac{ds}{du}\,du = \int_0^x \sqrt{1 + \cos^2 u}\,du \quad &\text{(arc element, origin of $s$ at the origin $O$)} \\
> \frac{ds}{dx} &= \sqrt{1 + \cos^2 x} \ge 1 \gt 0 \quad &\text{(derivative of the integral with respect to its upper limit)} \\
> x &\le s(x) \le \sqrt 2\,x \quad &\text{(bounds of the integrand, for positive $x$)} \\
> s(x + \pi) &= s(x) + s(\pi) \quad &\text{(the integrand has period $\pi$)} \\
> x &= s^{-1}(s) \quad &\text{(strictly increasing function: unique inverse)}
> \end{aligned}$$
>
> $$\boxed{s(x) = \int_0^x \sqrt{1 + \cos^2 u}\,du,\qquad x = s^{-1}(s),\qquad s(\pi) \approx 3.8202\ \mathrm{m}}$$
>
> **Units:** the integrand is $[1]$ and $du$ is $[\mathrm{L}]$, so $s$ is $[\mathrm{L}]$
> **Meaning:** the integral has no elementary antiderivative (extension: it is an incomplete elliptic integral of the second kind), so the statement allows leaving it as an integral; along one arch the particle travels 3.82 m while advancing 3.14 m.

#### (c) Tangential and normal acceleration

> [!derivation] Acceleration in the fixed basis
> **Law:** definition of acceleration; product and chain rules
> **Source:** Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i_0 + \cos x\,\dot x\,\mathbf j_0\right) \quad &\text{(definition of acceleration)} \\
> &= \ddot x\,\mathbf i_0 + \left(-\sin x\,\dot x^2 + \cos x\,\ddot x\right)\mathbf j_0 \quad &\text{(product rule; chain rule on $\cos x$)} \\
> &= -\sin x\,\mathbf j_0 \quad &\text{(unit rate, zero second derivative)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = -\sin x\,\mathbf j_0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the horizontal motion is uniform, so the only acceleration is vertical, the second derivative of the height.

> [!derivation] Intrinsic components of the acceleration
> **Law:** derivative of the velocity written in the intrinsic basis
> **Source:** Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.18
>
> $$\begin{aligned}
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot s\,\mathbf e_t\right) = \ddot s\,\mathbf e_t + \dot s\,\dot{\mathbf e}_t \quad &\text{(product rule)} \\
> \ddot s &= \frac{d}{dt}\sqrt{1 + \cos^2 x} = \frac{2\cos x\,(-\sin x)\,\dot x}{2\sqrt{1 + \cos^2 x}} = -\frac{\sin x\cos x}{L} \quad &\text{(chain rule twice)} \\
> \dot s\,\dot{\mathbf e}_t &= L\left(-\frac{\sin x}{L^2}\right)\mathbf e_\perp = -\frac{\sin x}{L}\,\sigma\,\mathbf e_n \quad &\text{(rotation of the tangent; $\mathbf e_\perp$ is $\sigma\,\mathbf e_n$)} \\
> -\sigma\sin x &= \operatorname{sgn}(\sin x)\sin x = |\sin x| \quad &\text{(definition of $\sigma$)} \\
> a_t &= -\frac{\sin x\cos x}{L},\quad a_n = \frac{|\sin x|}{L} \quad &\text{(components along $\mathbf e_t$ and $\mathbf e_n$)}
> \end{aligned}$$
>
> $$\boxed{a_t = -\frac{\sin x\cos x}{\sqrt{1 + \cos^2 x}},\qquad a_n = \frac{|\sin x|}{\sqrt{1 + \cos^2 x}}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the speed depends only on the slope, so it rises toward the inflection points and falls toward the crests and troughs, and the tangential acceleration is negative wherever $\sin x\cos x$ is positive; the normal acceleration is never negative, because the normal points to the centre of curvature.

#### (d) Radius of curvature

> [!derivation] Radius of curvature
> **Law:** normal acceleration equals the square of the speed over the radius of curvature
> **Source:** Notes.pdf, Eq. 2.18; Notes.pdf, Eq. 2.12
>
> $$\begin{aligned}
> \rho &= \frac{\dot s^2}{a_n} \quad &\text{(Notes Eq. 2.18 solved for $\rho$)} \\
> &= \frac{1 + \cos^2 x}{|\sin x|/\sqrt{1 + \cos^2 x}} \quad &\text{(speed and normal acceleration)} \\
> &= \frac{(1 + \cos^2 x)^{3/2}}{|\sin x|} \quad &\text{(product of the powers of $L$)} \\
> \frac{1}{\kappa} &= \frac{L^3}{|\sin x|} \quad &\text{(curvature of part (a), same result)}
> \end{aligned}$$
>
> $$\boxed{\rho(x) = \frac{\left(1 + \cos^2 x\right)^{3/2}}{|\sin x|}}$$
>
> **Units:** $[\mathrm{L^2T^{-2}}]/[\mathrm{L\,T^{-2}}] = [\mathrm{L}]$
> **Meaning:** the radius is smallest at the crests and troughs (1 m) and grows without bound at the inflection points, where the curve is locally straight.

![[attachments/EM-SOL/p06-osculating-circles.svg]]

### Answers and Checks

> [!derivation] Answers to (a) to (d)
> **Law:** collection of the results
> **Source:** Problems.pdf, p. 7
>
> $$\begin{aligned}
> \mathbf e_t &= \frac{\mathbf i_0 + \cos x\,\mathbf j_0}{L},\quad \mathbf e_n = \operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf i_0 - \mathbf j_0}{L},\quad \mathbf e_b = -\operatorname{sgn}(\sin x)\,\mathbf k_0 \quad &\text{(part (a))} \\
> s &= \int_0^x \sqrt{1 + \cos^2 u}\,du,\quad x = s^{-1}(s) \quad &\text{(part (b))} \\
> a_t &= -\frac{\sin x\cos x}{L},\quad a_n = \frac{|\sin x|}{L} \quad &\text{(part (c))}
> \end{aligned}$$
>
> $$\boxed{\rho = \frac{\left(1 + \cos^2 x\right)^{3/2}}{|\sin x|},\qquad L = \sqrt{1 + \cos^2 x}}$$
>
> **Units:** $[1]$, $[\mathrm{L}]$, $[\mathrm{L\,T^{-2}}]$, $[\mathrm{L}]$
> **Meaning:** the intrinsic description of the motion on the sine curve, valid away from the inflection points for the normal and binormal.

> [!derivation] Check: projections of the Cartesian acceleration
> **Law:** components of a vector on an orthonormal basis are dot products
> **Source:** Notes.pdf, Eq. 1.28; Notes.pdf, Eq. 1.40
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\mathbf e_t &= (-\sin x\,\mathbf j_0)\cdot\frac{\mathbf i_0 + \cos x\,\mathbf j_0}{L} = -\frac{\sin x\cos x}{L} \quad &\text{(only the $\mathbf j_0$ components multiply)} \\
> \mathbf a_0^P\cdot\mathbf e_n &= (-\sin x\,\mathbf j_0)\cdot\operatorname{sgn}(\sin x)\,\frac{\cos x\,\mathbf i_0 - \mathbf j_0}{L} = \frac{|\sin x|}{L} \quad &\text{(same; $\operatorname{sgn}(\sin x)\sin x$ is $|\sin x|$)} \\
> a_t^2 + a_n^2 &= \frac{\sin^2 x\,(\cos^2 x + 1)}{1 + \cos^2 x} = \sin^2 x \quad &\text{(sum of the squares)}
> \end{aligned}$$
>
> $$\boxed{a_t^2 + a_n^2 = \left|\mathbf a_0^P\right|^2 = \sin^2 x}$$
>
> **Units:** $[\mathrm{L^2T^{-4}}]$
> **Meaning:** the intrinsic route and the Cartesian route give the same acceleration.

> [!derivation] Limiting cases
> **Law:** evaluation at special points of the curve
> **Source:** Notes.pdf, Eq. 2.18
>
> $$\begin{aligned}
> x = \tfrac{\pi}{2} &: \ L = 1,\ \mathbf e_t = \mathbf i_0,\ \mathbf e_n = -\mathbf j_0,\ a_t = 0,\ a_n = 1,\ \rho = 1 \quad &\text{(crest: horizontal tangent, centre of curvature below)} \\
> x = \tfrac{\pi}{4} &: \ L^2 = \tfrac{3}{2},\ a_t = -\tfrac{1/2}{\sqrt{3/2}} \approx -0.408,\ \rho = \frac{(3/2)^{3/2}}{\sqrt 2/2} = \tfrac{3\sqrt 3}{2} \approx 2.598 \quad &\text{(climbing: the speed decreases)} \\
> x \to k\pi &: \ a_n \to 0,\ \rho \to \infty \quad &\text{(inflection points: locally straight)}
> \end{aligned}$$
>
> $$\boxed{\rho\!\left(\tfrac{\pi}{2}\right) = 1\ \mathrm{m},\qquad \rho\!\left(\tfrac{\pi}{4}\right) = \tfrac{3\sqrt 3}{2}\ \mathrm{m},\qquad \rho(k\pi) \to \infty}$$
>
> **Units:** $[\mathrm{L}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** at the crest the radius equals the inverse of the second derivative of the height, as for any graph at a horizontal tangent; at the inflection points the normal is not defined.

Check against the official key: the solution keys of Problems.pdf, p. 72 list item 6 with no answer, so the results are verified independently: the intrinsic acceleration agrees with the projections of the Cartesian acceleration, the radius of curvature agrees with the curvature of part (a), the limiting cases above hold, and a numerical quadrature (midpoint rule, 200000 intervals) gives the arc length of one arch, 3.8202 m.

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Particle on the curve y = sin x (Problem 06)", "intro": "Data of the statement: ẋ = 1 m/s, lengths in metres. The front view is the plane of the curve, with the y of the statement along the vertical axis of the view. The slider is the abscissa x; the default x = 0 is the start at the origin read in the solution, an inflection point, where the normal and the binormal are not defined and the radius of curvature is infinite (shown as a dash). Move x to see e_t, e_n and e_b; at the crest x = π/2 the readouts give ρ = 1 m. The archetype computes its speed and accelerations from the same curve and rate, so they agree with the readouts of the solution.", "params": {"curve": "sine", "a": 1, "k": 1, "rate": 1, "accel": 0, "umin": -3.1416, "umax": 3.1416, "extent": 3.4}, "defaults": {"u": 0}, "view": "front", "sliders": {"u": {"label": "Abscissa x (m)", "step": 0.0157}}, "readouts": [{"label": "Time t = x (ẋ = 1 m/s from the origin)", "expr": "u", "unit": "s", "digits": 4}, {"label": "Speed ṡ = L = √(1 + cos² x)", "expr": "sqrt(1 + cos(u)^2)", "unit": "m/s", "digits": 4}, {"label": "Angle γ of e_t, tan γ = cos x", "expr": "deg(atan(cos(u)))", "unit": "deg", "digits": 2}, {"label": "(c) a_t = −sin x cos x/L", "expr": "-sin(u)*cos(u)/sqrt(1 + cos(u)^2)", "unit": "m/s²", "digits": 4}, {"label": "(c) a_n = |sin x|/L", "expr": "abs(sin(u))/sqrt(1 + cos(u)^2)", "unit": "m/s²", "digits": 4}, {"label": "|a| = |sin x| (a = −sin x j0)", "expr": "abs(sin(u))", "unit": "m/s²", "digits": 4}, {"label": "(d) ρ = (1 + cos² x)^(3/2)/|sin x| (dash: infinite)", "expr": "(1 + cos(u)^2)^1.5/abs(sin(u))", "unit": "m", "digits": 4}]}








