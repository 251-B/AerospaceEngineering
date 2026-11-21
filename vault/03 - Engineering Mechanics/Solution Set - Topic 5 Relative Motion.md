---
title: "Solution Set - Topic 5: Relative Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (lecturer's order)"
language: "English"
tags:
  - solutions
  - topic-5
  - relative-motion
---

# Topic 5: Relative Motion - Full Analytical Solutions

Step-by-step solutions of the official relative-motion problems of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem follows the order of the course: reference frames, bases and coordinates; the change of basis $[{}_0R_1]$ and the position vector, deduced from drawings of each plane and each rotation; kinematics with the motion of the moving frame ($\mathbf{r}_0^A$, $\boldsymbol{\omega}_{10}$, $\boldsymbol{\alpha}_{10}$); forces and equations of motion; and the answers to every part with limiting cases and an SI dimensional check. Every chain rule, cross product and integral is written out. Statements: [[Problem Set - Topic 5 Relative Motion]]. Theory: [[Topic 5 - Relative Motion]]. Formulas: [[Formula Sheet - Topic 5 Relative Motion]].

---

## Problem 07: Skater Towed by a Vehicle on a Circumference (Rotating Frame)

### Reference Frames, Bases and Coordinates

A vehicle $A$ moves on the circumference of radius $a$ and centre $O$ with the constant angular velocity $\omega$, on a smooth horizontal plane; a skater $B$ of mass $m$ is joined to it by a massless rigid bar of length $a$. At the start the vehicle is at $(a, 0)$ and the skater at rest at $(2a, 0)$ (Problems.pdf, p. 8). The statement asks, in the rotating frame $Ox_1y_1$ that carries $OA$ on its first axis, for the relative acceleration, the centripetal and Coriolis terms, the reduction of the motion to quadratures, the tension of the bar and whether a string would go slack. The relative kinematics follows Notes.pdf, Sec. 3.1 and Sec. 3.2, and the dynamics in the non-inertial frame Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, the frame $Oxy$ of the statement, with $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$: $\mathbf i_0$ along $Ox$, $\mathbf j_0$ along $Oy$, $\mathbf k_0$ vertical, up (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $Ox_1y_1$: $\mathbf i_1$ along $OA$, $\mathbf k_1 = \mathbf k_0$, $\mathbf j_1$ the cross product of $\mathbf k_1$ and $\mathbf i_1$; it turns by the angle $\omega t$ about $\mathbf k_0$ |
| Origin of $S_1$ | the fixed point $O$ (the generic origin, called $A$ in Notes.pdf, Sec. 3.2, is here $O$; the letter $A$ stays for the vehicle, as in the statement) |
| Bar basis | $\mathcal B_2 = \{\mathbf u_{AB}, \mathbf u_\perp, \mathbf k_1\}$: $\mathbf u_{AB}$ from $A$ to $B$, $\mathbf u_\perp$ normal to the bar in the plane, in the sense of growing $\psi$ |
| Coordinate | $\psi$, the angle from $\mathbf i_1$ to the bar $AB$, measured at $A$, positive about $\mathbf k_1$ (counterclockwise seen from above) |
| Constraints | $B$ on the horizontal plane; distance $AB$ equal to $a$; in $S_1$ the vehicle is at rest at $(a, 0)$, so $B$ moves on a circle of radius $a$ about $A$, fixed in $S_1$ |
| Degrees of freedom | 3 minus 2: 1, the angle $\psi(t)$; the angle $\omega t$ of $S_1$ is prescribed |
| Data | $m$ [kg], $a$ [m], $\omega$ [rad s$^{-1}$], constant |
| Unknowns | $\psi(t)$, the bar force $T$ [N] (positive when the bar pulls $B$ towards $A$), the normal reaction of the plane $N$ [N] |
| Initial state | $\psi(0) = 0$ (skater at $(2a, 0)$); skater at rest in $S_0$ |
| Applied forces | weight $-mg\,\mathbf k_1$; the force of the bar, along the bar |
| Constraint force | normal reaction of the smooth plane, $N\,\mathbf k_1$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | the bar is massless and hinged at both ends, so the force it exerts on $B$ lies along the bar; the plane is smooth, so its reaction is vertical; $\omega$ constant; the skater is a point particle |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p07-attitude.svg]]

> [!derivation] Basis of the rotating frame: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up): a positive rotation about $\mathbf k_0$ is counterclockwise, the sense in which the vehicle turns. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf j_0$, opposite leg $\sin\omega t$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf i_1$)} \\
> \mathbf j_1 &= -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf j_1$: opposite leg on $-\mathbf i_0$)} \\
> \mathbf k_1 &= \mathbf k_0 \quad &\text{(axis of the rotation)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\omega t\cos\omega t - \left(-\sin\omega t\right)\sin\omega t\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\omega t\sin\omega t - \sin\omega t\cos\omega t = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$; $[\omega t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$
> **Meaning:** at the start ($t$ zero) the two frames coincide; afterwards $\mathbf i_1$ always points from $O$ to the vehicle.

![[attachments/EM-SOL/p07-bar-plane.svg]]

> [!derivation] Position vector of the skater in the rotating frame
> **Law:** position vector as a sum of segments; right triangle of the bar
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 3.16; Problems.pdf, p. 8
>
> In $S_1$ the vehicle is at rest on the axis $Ox_1$ at the distance $a$ from $O$. From $O$ to $B$ we pass through $A$, because the bar fixes the distance from $A$. Let $F$ be the foot of the perpendicular from $B$ to the line $Ox_1$: in the right triangle $AFB$ the hypotenuse is the bar, of length $a$; the leg adjacent to $\psi$ is $a\cos\psi$ along $\mathbf i_1$ and the leg opposite to $\psi$ is $a\sin\psi$ along $\mathbf j_1$. $\psi$ is measured from $\mathbf i_1$ counterclockwise, so it is already the standard polar angle about $A$ and needs no shift. For a negative $\psi$ (the case of the motion, part (c)) the opposite leg points along minus $\mathbf j_1$ and the same formula holds.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0 \quad &\text{(the origin of $S_1$ is the fixed point $O$)} \\
> \mathbf r_0^B &= \mathbf r_0^O + \mathbf r_1^B = \mathbf r_1^B \quad &\text{(Eq. 3.16)} \\
> \mathbf r_1^B &= \overrightarrow{OA} + \overrightarrow{AB} \quad &\text{(through the hinge $A$)} \\
> \overrightarrow{OA} &= a\,\mathbf i_1 \quad &\text{(vehicle at rest in $S_1$)} \\
> \overrightarrow{AB} &= a\cos\psi\,\mathbf i_1 + a\sin\psi\,\mathbf j_1 \quad &\text{(adjacent and opposite legs of $AFB$)} \\
> \mathbf r_1^B &= a\left(1 + \cos\psi\right)\mathbf i_1 + a\sin\psi\,\mathbf j_1 \quad &\text{(sum, grouped by unit vector)} \\
> x_1 &= a\left(1 + \cos\psi\right), \quad y_1 = a\sin\psi \quad &\text{(components in $\mathcal B_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^B = \mathbf r_1^B = a\left(1 + \cos\psi\right)\mathbf i_1 + a\sin\psi\,\mathbf j_1}$$
>
> **Units:** $[a] = [\mathrm{L}]$; $\psi$ dimensionless
> **Meaning:** $\psi$ zero gives the initial point at twice $a$ on $Ox_1$; $\psi$ equal to minus $\pi$ gives the point $O$ itself.

![[attachments/EM-SOL/p07-rotation-psi.svg]]

> [!derivation] Bar basis: rotation by psi about k1
> **Law:** elementary rotation about the third axis; change of basis matrix, its checks and its inverse
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20
>
> View from above along $\mathbf k_1$, out of the paper (⊙); $\mathbf i_1$ to the right and $\mathbf j_1$ up. $\mathbf u_{AB}$ is $\mathbf i_1$ turned by $\psi$: hypotenuse 1, adjacent leg $\cos\psi$ along $\mathbf i_1$, opposite leg $\sin\psi$ along $\mathbf j_1$. $\mathbf u_\perp$ is $\mathbf j_1$ turned by $\psi$: adjacent leg $\cos\psi$ along $\mathbf j_1$, opposite leg $\sin\psi$ along minus $\mathbf i_1$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf u_{AB} &= \frac{\overrightarrow{AB}}{a} = \cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1 \quad &\text{(right triangle of $\mathbf u_{AB}$)} \\
> \mathbf u_\perp &= -\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1 \quad &\text{(right triangle of $\mathbf u_\perp$: opposite leg on $-\mathbf i_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{11} &= \cos^2\psi + \sin^2\psi = 1, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{12} = \cos\psi\sin\psi - \sin\psi\cos\psi = 0 \quad &\text{(rows times rows)} \\
> \mathbf i_1 &= \cos\psi\,\mathbf u_{AB} - \sin\psi\,\mathbf u_\perp, \quad \mathbf j_1 = \sin\psi\,\mathbf u_{AB} + \cos\psi\,\mathbf u_\perp \quad &\text{(inverse: the rows of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad [{}_1R_2][{}_1R_2]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the bar force acts along $\mathbf u_{AB}$ only, so projecting on $\mathbf u_\perp$ will give an equation free of the unknown tension.

### Kinematics

> [!derivation] Motion of the rotating frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector fixed in a rotating basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9; [Lecture 5, Slide 16]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1 \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf k_0 = \mathbf k_1$ with the angle $\omega t$)} \\
> \boldsymbol\alpha_{10} &= \dot\omega\,\mathbf k_1 = \mathbf 0 \quad &\text{(Eq. 3.9; $\omega$ constant, $\mathbf k_1$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \boldsymbol\omega_{10}\times\mathbf i_1 = \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1 \quad &\text{(Eq. 3.3; $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> \left.\frac{d\mathbf j_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1 \quad &\text{(Eq. 3.4; $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \left.\frac{d\mathbf k_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf k_1 = \mathbf 0 \quad &\text{(Eq. 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) &= -\omega\sin\omega t\,\mathbf i_0 + \omega\cos\omega t\,\mathbf j_0 = \omega\,\mathbf j_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from $S_0$ the unit vectors of $S_1$ turn with the vehicle; seen from $S_1$ they are constant.

> [!derivation] Absolute velocity of the skater: relative and transport terms
> **Law:** time derivative in $S_0$ of the position vector written in the moving basis; product rule
> **Source:** Notes.pdf, Eq. 3.2; Notes.pdf, Eq. 3.6; Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.19; [Lecture 5, Slide 24]
>
> $$\begin{aligned}
> \mathbf v_0^B &= \left.\frac{d}{dt}\right|_0\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(definition; $\mathbf r_0^B = \mathbf r_1^B$)} \\
> &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + x_1\left.\frac{d\mathbf i_1}{dt}\right|_0 + y_1\left.\frac{d\mathbf j_1}{dt}\right|_0 \quad &\text{(product rule on each term)} \\
> &= \underbrace{\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1}_{\mathbf v_1^B} + \underbrace{\omega x_1\,\mathbf j_1 - \omega y_1\,\mathbf i_1}_{\boldsymbol\omega_{10}\times\mathbf r_1^B} \quad &\text{(derivatives of the unit vectors substituted)} \\
> \dot x_1 &= \frac{d}{dt}\left[a\left(1 + \cos\psi\right)\right] = -a\sin\psi\,\dot\psi \quad &\text{(chain rule: $\tfrac{d}{d\psi}\cos\psi = -\sin\psi$)} \\
> \dot y_1 &= \frac{d}{dt}\left(a\sin\psi\right) = a\cos\psi\,\dot\psi \quad &\text{(chain rule: $\tfrac{d}{d\psi}\sin\psi = \cos\psi$)} \\
> \mathbf v_1^B &= -a\dot\psi\sin\psi\,\mathbf i_1 + a\dot\psi\cos\psi\,\mathbf j_1 = a\dot\psi\,\mathbf u_\perp \quad &\text{(components; $\mathbf u_\perp$ of the bar basis)} \\
> \boldsymbol\omega_{10}\times\mathbf r_1^B &= -a\omega\sin\psi\,\mathbf i_1 + a\omega\left(1 + \cos\psi\right)\mathbf j_1 \quad &\text{($x_1$ and $y_1$ substituted)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^B = \mathbf v_1^B + \boldsymbol\omega_{10}\times\mathbf r_1^B = -a\left(\dot\psi + \omega\right)\sin\psi\,\mathbf i_1 + a\left[\left(\dot\psi + \omega\right)\cos\psi + \omega\right]\mathbf j_1}$$
>
> **Units:** $[a\dot\psi] = [a\omega] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the relative term comes from differentiating the components, the transport term from differentiating the turning unit vectors; it is the form of Eq. 3.20 with the origin at rest.

> [!derivation] Absolute acceleration of the skater: relative, Coriolis and centripetal terms
> **Law:** time derivative in $S_0$ of the two terms of the velocity; product rule and derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.24; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \left.\frac{d\mathbf v_1^B}{dt}\right|_0 &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 + \dot x_1\,\omega\,\mathbf j_1 - \dot y_1\,\omega\,\mathbf i_1 \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> &= \mathbf a_1^B + \boldsymbol\omega_{10}\times\mathbf v_1^B \quad &\text{(first pair: the relative acceleration; second pair: a rotation term)} \\
> \left.\frac{d}{dt}\right|_0\left(\omega\,\mathbf k_1\times\mathbf r_1^B\right) &= \dot\omega\,\mathbf k_1\times\mathbf r_1^B + \omega\left.\frac{d\mathbf k_1}{dt}\right|_0\times\mathbf r_1^B + \omega\,\mathbf k_1\times\left.\frac{d\mathbf r_1^B}{dt}\right|_0 \quad &\text{(product rule on the three factors)} \\
> &= \boldsymbol\omega_{10}\times\left(\mathbf v_1^B + \boldsymbol\omega_{10}\times\mathbf r_1^B\right) \quad &\text{($\dot\omega$ zero; $\mathbf k_1$ fixed; velocity box)} \\
> \mathbf a_0^B &= \mathbf a_1^B + \boldsymbol\omega_{10}\times\mathbf v_1^B + \boldsymbol\omega_{10}\times\mathbf v_1^B + \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B\right) \quad &\text{(sum of the two derivatives)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^B = \mathbf a_1^B + 2\,\boldsymbol\omega_{10}\times\mathbf v_1^B + \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B\right)}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** one Coriolis half comes from the turning of $\mathbf i_1$, $\mathbf j_1$ inside the relative velocity, the other from the change of the relative position inside the transport term; with the origin at rest and constant $\omega$ the origin and Euler terms of Eq. 3.27 are absent.

#### (a) Relative acceleration

> [!derivation] Relative acceleration of the skater
> **Law:** second time derivative in $S_1$, where $\mathbf i_1$ and $\mathbf j_1$ are constant; product rule and chain rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.24; Problems.pdf, p. 8
>
> $$\begin{aligned}
> \ddot x_1 &= \frac{d}{dt}\left(-a\dot\psi\sin\psi\right) = -a\ddot\psi\sin\psi - a\dot\psi^2\cos\psi \quad &\text{(product rule; chain rule on $\sin\psi$)} \\
> \ddot y_1 &= \frac{d}{dt}\left(a\dot\psi\cos\psi\right) = a\ddot\psi\cos\psi - a\dot\psi^2\sin\psi \quad &\text{(product rule; chain rule on $\cos\psi$)} \\
> \mathbf a_1^B &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 \quad &\text{(Eq. 3.24 with constant $\mathbf i_1$, $\mathbf j_1$ in $S_1$)} \\
> &= a\ddot\psi\left(-\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1\right) - a\dot\psi^2\left(\cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1\right) \quad &\text{(grouped by $\ddot\psi$ and $\dot\psi^2$)} \\
> &= a\ddot\psi\,\mathbf u_\perp - a\dot\psi^2\,\mathbf u_{AB} \quad &\text{(bar basis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_1^B = -a\left(\ddot\psi\sin\psi + \dot\psi^2\cos\psi\right)\mathbf i_1 + a\left(\ddot\psi\cos\psi - \dot\psi^2\sin\psi\right)\mathbf j_1 = a\ddot\psi\,\mathbf u_\perp - a\dot\psi^2\,\mathbf u_{AB}}$$
>
> **Units:** $[a\ddot\psi] = [a\dot\psi^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in $S_1$ the skater moves on a circle of radius $a$ about $A$: a tangential part along the normal of the bar and a centripetal part pointing from $B$ towards $A$.

#### (b) Centripetal and Coriolis terms

> [!derivation] Centripetal and Coriolis accelerations
> **Law:** vector products with the angular velocity of $S_1$, expanded term by term
> **Source:** Notes.pdf, Eq. 3.25; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10}\times\mathbf r_1^B &= \omega\,\mathbf k_1\times\left[a\left(1 + \cos\psi\right)\mathbf i_1 + a\sin\psi\,\mathbf j_1\right] = -a\omega\sin\psi\,\mathbf i_1 + a\omega\left(1 + \cos\psi\right)\mathbf j_1 \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B\right) &= \omega\,\mathbf k_1\times\left[-a\omega\sin\psi\,\mathbf i_1 + a\omega\left(1 + \cos\psi\right)\mathbf j_1\right] \quad &\text{(previous row)} \\
> &= -a\omega^2\sin\psi\,\mathbf j_1 - a\omega^2\left(1 + \cos\psi\right)\mathbf i_1 \quad &\text{(same products)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^B &= 2\omega\,\mathbf k_1\times\left(-a\dot\psi\sin\psi\,\mathbf i_1 + a\dot\psi\cos\psi\,\mathbf j_1\right) \quad &\text{(relative velocity of the velocity box)} \\
> &= -2a\omega\dot\psi\sin\psi\,\mathbf j_1 - 2a\omega\dot\psi\cos\psi\,\mathbf i_1 \quad &\text{(same products)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B\right) = -a\omega^2\left[\left(1 + \cos\psi\right)\mathbf i_1 + \sin\psi\,\mathbf j_1\right], \qquad 2\,\boldsymbol\omega_{10}\times\mathbf v_1^B = -2a\omega\dot\psi\left(\cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1\right) = -2a\omega\dot\psi\,\mathbf u_{AB}}$$
>
> **Units:** $[a\omega^2] = [a\omega\dot\psi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the centripetal term is $\omega^2$ times the position vector, reversed: it points from $B$ towards the axis through $O$, because the whole of $\mathbf r_1^B$ lies in the plane normal to $\boldsymbol\omega_{10}$. The Coriolis term lies along the bar.

### Forces and Equations of Motion

The free-body diagram of the skater in $S_1$ shows the weight and the normal reaction of the plane (both vertical), the bar force along the bar, and the two inertia forces that do not vanish: the centrifugal force, away from $O$, and the Coriolis force, along the bar. The inertia force of the origin and the Euler force vanish because $O$ is fixed and $\omega$ is constant.

![[attachments/EM-SOL/p07-fbd.svg]]

> [!derivation] Actual and inertia forces on the skater in the rotating frame
> **Law:** inertia forces of a non-inertial frame; force of a massless two-hinged bar along the bar
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> \mathbf F &= -T\,\mathbf u_{AB} - mg\,\mathbf k_1 + N\,\mathbf k_1 \quad &\text{(bar, weight, plane)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^B = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B\right) = ma\omega^2\left[\left(1 + \cos\psi\right)\mathbf i_1 + \sin\psi\,\mathbf j_1\right] \quad &\text{(centripetal term of part (b) times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^B = 2ma\omega\dot\psi\,\mathbf u_{AB} \quad &\text{(Coriolis term of part (b) times $-m$)} \\
> \mathbf F_C\cdot\mathbf u_{AB} &= ma\omega^2\left[\left(1 + \cos\psi\right)\cos\psi + \sin^2\psi\right] = ma\omega^2\left(1 + \cos\psi\right) \quad &\text{(components of $\mathbf u_{AB}$; $\cos^2\psi + \sin^2\psi = 1$)} \\
> \mathbf F_C\cdot\mathbf u_\perp &= ma\omega^2\left[-\left(1 + \cos\psi\right)\sin\psi + \sin\psi\cos\psi\right] = -ma\omega^2\sin\psi \quad &\text{(components of $\mathbf u_\perp$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_C = ma\omega^2\left(1 + \cos\psi\right)\mathbf u_{AB} - ma\omega^2\sin\psi\,\mathbf u_\perp, \qquad \mathbf F_{COR} = 2ma\omega\dot\psi\,\mathbf u_{AB}}$$
>
> **Units:** $[ma\omega^2] = [ma\omega\dot\psi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the centrifugal force pushes $B$ away from $O$; its part normal to the bar turns the bar back towards the axis $Ox_1$, like the weight of a pendulum hung from $A$.

> [!derivation] Newton's second law in the rotating frame, projected on the bar basis
> **Law:** Newton's second law in a non-inertial frame with the inertia forces
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 7.6; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> m\,\mathbf a_1^B &= \mathbf F + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63; $\mathbf F_A$ and $\mathbf F_E$ zero)} \\
> \mathbf u_\perp:\ ma\ddot\psi &= -ma\omega^2\sin\psi \quad &\text{(bar force and Coriolis force have no $\mathbf u_\perp$ part)} \\
> \mathbf u_{AB}:\ -ma\dot\psi^2 &= -T + ma\omega^2\left(1 + \cos\psi\right) + 2ma\omega\dot\psi \quad &\text{(all forces along the bar)} \\
> \mathbf k_1:\ 0 &= N - mg \quad &\text{(the skater stays on the plane)}
> \end{aligned}$$
>
> $$\boxed{\ddot\psi + \omega^2\sin\psi = 0, \qquad T = ma\left[\dot\psi^2 + 2\omega\dot\psi + \omega^2\left(1 + \cos\psi\right)\right], \qquad N = mg}$$
>
> **Units:** $[\ddot\psi] = [\omega^2] = [\mathrm{T^{-2}}]$; $[T] = [ma\dot\psi^2] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations for the three unknowns $\psi$, $T$ and $N$. In $S_1$ the skater swings like a pendulum of length $a$ hung from $A$, with the effective field $a\omega^2$ pointing along plus $\mathbf i_1$, away from $O$; $\psi$ zero is its stable bottom. The analogy is exact for the motion (the component along $\mathbf u_\perp$) but not for the tension: along the bar the centrifugal force is $ma\omega^2(1 + \cos\psi)$, not the $ma\omega^2\cos\psi$ of a uniform field, and the Coriolis force adds to it.

### Answers and Checks

#### (c) Reduction to quadratures

> [!derivation] First integral of the equation of motion
> **Law:** the equation of motion multiplied by twice the rate is an exact derivative (the hint of the statement); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Sec. 7.7; Problems.pdf, p. 8
>
> $$\begin{aligned}
> 2\dot\psi\ddot\psi + 2\omega^2\sin\psi\,\dot\psi &= 0 \quad &\text{(equation of motion times $2\dot\psi$)} \\
> \frac{d}{dt}\left(\dot\psi^2\right) &= 2\dot\psi\ddot\psi \quad &\text{(chain rule: $\tfrac{d}{d\dot\psi}\dot\psi^2 = 2\dot\psi$)} \\
> \frac{d}{dt}\left(-2\omega^2\cos\psi\right) &= 2\omega^2\sin\psi\,\dot\psi \quad &\text{(chain rule: $\tfrac{d}{d\psi}\cos\psi = -\sin\psi$)} \\
> \frac{d}{dt}\left(\dot\psi^2 - 2\omega^2\cos\psi\right) &= 0 \quad &\text{(the first row is this sum)} \\
> \left[\dot\psi^2 - 2\omega^2\cos\psi\right]_0^t &= 0 \quad &\text{(Barrow's rule between 0 and $t$)} \\
> \dot\psi^2 - \dot\psi^2(0) &= 2\omega^2\left(\cos\psi - \cos\psi(0)\right) = 2\omega^2\left(\cos\psi - 1\right) \quad &\text{($\psi(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi^2 = \dot\psi^2(0) + 2\omega^2\left(\cos\psi - 1\right)}$$
>
> **Units:** $[\dot\psi^2] = [\omega^2] = [\mathrm{T^{-2}}]$
> **Meaning:** the rate squared depends on the position only; the initial rate is still to be found from the condition that the skater starts at rest in $S_0$.

> [!derivation] Initial rate from the skater at rest in the inertial frame
> **Law:** absolute velocity of the velocity box evaluated at the initial instant
> **Source:** Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.26; Problems.pdf, p. 8
>
> $$\begin{aligned}
> \mathbf v_0^B &= -a\left(\dot\psi + \omega\right)\sin\psi\,\mathbf i_1 + a\left[\left(\dot\psi + \omega\right)\cos\psi + \omega\right]\mathbf j_1 \quad &\text{(velocity box)} \\
> \mathbf v_0^B(0) &= -a\left(\dot\psi(0) + \omega\right)\cdot 0\,\mathbf i_1 + a\left[\left(\dot\psi(0) + \omega\right)\cdot 1 + \omega\right]\mathbf j_1 \quad &\text{($\psi(0) = 0$: $\sin 0 = 0$, $\cos 0 = 1$)} \\
> &= a\left[\dot\psi(0) + 2\omega\right]\mathbf j_1 = \mathbf 0 \quad &\text{(skater at rest in $S_0$)} \\
> \dot\psi(0) &= -2\omega \quad &\text{(solved)} \\
> \dot\psi^2 &= 4\omega^2 + 2\omega^2\left(\cos\psi - 1\right) = 2\omega^2\left(1 + \cos\psi\right) \quad &\text{(first integral)} \\
> &= 4\omega^2\cos^2\frac{\psi}{2} \quad &\text{($1 + \cos\psi = 2\cos^2(\psi/2)$)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi(0) = -2\omega, \qquad \dot\psi^2 = 4\omega^2\cos^2\frac{\psi}{2}}$$
>
> **Units:** $[\dot\psi] = [\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from $S_1$, which turns counterclockwise, a skater at rest in $S_0$ moves clockwise: her relative velocity must cancel the transport velocity of the point at twice $a$ from the axis, of magnitude $2a\omega$.

> [!derivation] Sign of the rate and quadrature
> **Law:** continuity of the rate; separation of variables
> **Source:** Notes.pdf, Eq. 4.44; Notes.pdf, Sec. 7.7; Problems.pdf, p. 8
>
> The rate is a continuous function of time. Between minus $\pi$ and $\pi$ the factor $\cos(\psi/2)$ is positive, so the rate cannot vanish there and keeps the sign it has at the start, negative: $\psi$ decreases from 0 and stays between minus $\pi$ and 0.
>
> $$\begin{aligned}
> \dot\psi &= -2\omega\cos\frac{\psi}{2}, \quad -\pi \lt \psi \le 0 \quad &\text{(negative root, fixed by $\dot\psi(0) = -2\omega$)} \\
> \frac{d\psi}{2\cos(\psi/2)} &= -\omega\,dt \quad &\text{(variables separated)} \\
> \int_0^{\psi}\frac{d\psi'}{2\cos(\psi'/2)} &= -\int_0^t\omega\,dt' \quad &\text{(integrated from the initial state $\psi(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\int_0^{\psi}\frac{d\psi'}{2\cos(\psi'/2)} = -\int_0^t\omega\,dt', \qquad \dot\psi = -2\omega\cos\frac{\psi}{2} \ \ \left(-\pi \lt \psi \le 0\right)}$$
>
> **Units:** both integrals dimensionless; $[\omega\,dt] = [1]$
> **Meaning:** this is the form asked for in the statement; the next box evaluates it.

> [!derivation] Evaluation of the quadrature: the angle as a function of time
> **Law:** substitution, antiderivative of the secant, Barrow's rule; half-angle identities
> **Source:** Notes.pdf, Eq. 4.44; Problems.pdf, p. 8
>
> With the substitution $w = \psi'/2$ the differential is $d\psi' = 2\,dw$ and the limits 0 and $\psi$ become 0 and $\psi/2$. The antiderivative of $1/\cos w$ is $\ln|\sec w + \tan w|$; its derivative is $(\sec w\tan w + \sec^2 w)/(\sec w + \tan w) = \sec w$.
>
> $$\begin{aligned}
> \int_0^{\psi}\frac{d\psi'}{2\cos(\psi'/2)} &= \int_0^{\psi/2}\frac{2\,dw}{2\cos w} = \int_0^{\psi/2}\frac{dw}{\cos w} \quad &\text{(substitution $\psi' = 2w$)} \\
> &= \left[\ln\left|\sec w + \tan w\right|\right]_0^{\psi/2} = \ln\left(\sec\frac{\psi}{2} + \tan\frac{\psi}{2}\right) - \ln 1 \quad &\text{(Barrow's rule; the argument is positive for $|\psi/2| \lt \pi/2$)} \\
> -\int_0^t\omega\,dt' &= -\omega\left[t'\right]_0^t = -\omega t \quad &\text{(antiderivative $t'$; Barrow's rule)} \\
> \sec x + \tan x &= \frac{1 + \sin x}{\cos x} = \frac{\left(\cos\tfrac{x}{2} + \sin\tfrac{x}{2}\right)^2}{\cos^2\tfrac{x}{2} - \sin^2\tfrac{x}{2}} \quad &\text{(half-angle forms: $1 + \sin x = (\cos\tfrac{x}{2} + \sin\tfrac{x}{2})^2$, $\cos x = \cos^2\tfrac{x}{2} - \sin^2\tfrac{x}{2}$)} \\
> &= \frac{\left(\cos\tfrac{x}{2} + \sin\tfrac{x}{2}\right)^2}{\left(\cos\tfrac{x}{2} - \sin\tfrac{x}{2}\right)\left(\cos\tfrac{x}{2} + \sin\tfrac{x}{2}\right)} = \frac{\cos\tfrac{x}{2} + \sin\tfrac{x}{2}}{\cos\tfrac{x}{2} - \sin\tfrac{x}{2}} \quad &\text{(difference of squares; common factor cancelled)} \\
> &= \frac{1 + \tan\tfrac{x}{2}}{1 - \tan\tfrac{x}{2}} = \tan\left(\frac{\pi}{4} + \frac{x}{2}\right) \quad &\text{(numerator and denominator divided by $\cos\tfrac{x}{2}$; tangent of a sum with $\tan\tfrac{\pi}{4} = 1$)} \\
> \tan\left(\frac{\pi}{4} + \frac{\psi}{4}\right) &= e^{-\omega t} \quad &\text{(exponential of both sides, $x = \psi/2$)} \\
> \psi &= 4\arctan\left(e^{-\omega t}\right) - \pi \quad &\text{(solved; $\pi/4 + \psi/4$ lies between 0 and $\pi/4$)} \\
> \cos\frac{\psi}{2} &= \cos\left(2\arctan e^{-\omega t} - \frac{\pi}{2}\right) = \sin\left(2\arctan e^{-\omega t}\right) = \frac{2e^{-\omega t}}{1 + e^{-2\omega t}} = \frac{1}{\cosh\omega t} \quad &\text{($\sin 2\beta = 2\tan\beta/(1 + \tan^2\beta)$)}
> \end{aligned}$$
>
> $$\boxed{\psi(t) = 4\arctan\left(e^{-\omega t}\right) - \pi, \qquad \cos\frac{\psi}{2} = \frac{1}{\cosh\omega t}, \qquad \dot\psi = -\frac{2\omega}{\cosh\omega t}}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** $\psi$ starts at 0 and tends to minus $\pi$ as $t$ grows, without reaching it in a finite time: with a rigid bar the skater creeps towards the centre $O$. The rate written with the hyperbolic cosine has the value $-2\omega$ at the start, as the initial-rate box requires.

#### (d) Tension on the bar

> [!derivation] Tension as a function of the angle and of time
> **Law:** tangent equation of the bar basis with the first integral substituted
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 8
>
> Write $c$ for $\cos(\psi/2)$, positive during the motion.
>
> $$\begin{aligned}
> T &= ma\left[\dot\psi^2 + 2\omega\dot\psi + \omega^2\left(1 + \cos\psi\right)\right] \quad &\text{(equation along the bar)} \\
> \dot\psi^2 &= 4\omega^2c^2, \quad \dot\psi = -2\omega c, \quad 1 + \cos\psi = 2c^2 \quad &\text{(sign box and half-angle identity)} \\
> T &= ma\omega^2\left(4c^2 - 4c + 2c^2\right) = ma\omega^2\left(6c^2 - 4c\right) \quad &\text{(substituted and collected)} \\
> &= 2ma\omega^2\,c\left(3c - 2\right) \quad &\text{(common factor $2c$)} \\
> T(t) &= \frac{2ma\omega^2}{\cosh\omega t}\left(\frac{3}{\cosh\omega t} - 2\right) \quad &\text{($c = 1/\cosh\omega t$)}
> \end{aligned}$$
>
> $$\boxed{T = 2ma\omega^2\cos\frac{\psi}{2}\left(3\cos\frac{\psi}{2} - 2\right)}$$
>
> **Units:** $[ma\omega^2] = [\mathrm{M}][\mathrm{L}][\mathrm{T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$, a force
> **Meaning:** at the start ($c$ equal to 1) the bar pulls with $2ma\omega^2$; the pull decreases as the skater swings in and turns into a push later on.

#### (e) String instead of the bar

> [!derivation] Instant at which a string goes slack
> **Law:** a string can only pull: it stays taut while the tension of the bar solution is not negative
> **Source:** Notes.pdf, Sec. 6.4; Problems.pdf, p. 8
>
> While the string is taut it behaves as the bar, so the motion and the tension are those found above. $c$ is the reciprocal of $\cosh\omega t$, so it decreases monotonically from 1 towards 0; the factor $c$ stays positive and the factor $3c - 2$ changes sign once.
>
> $$\begin{aligned}
> T &= 0 \iff 3c - 2 = 0 \iff \cos\frac{\psi}{2} = \frac23 \quad &\text{(first zero of the tension)} \\
> \psi_\ell &= -2\arccos\frac23 = -1.6821\ \text{rad} = -96.38^\circ \quad &\text{(negative branch of the motion)} \\
> \cosh\omega t_\ell &= \frac32 \quad &\text{($c = 1/\cosh\omega t$)} \\
> e^{\omega t_\ell} &= \frac32 + \sqrt{\frac94 - 1} = \frac{3 + \sqrt5}{2} \quad &\text{(roots of $e^{2x} - 3e^x + 1 = 0$ are $(3\pm\sqrt5)/2$, both positive; $t_\ell \gt 0$ needs $e^{\omega t_\ell} \gt 1$, so the larger one; the other is the mirror time $-t_\ell$)} \\
> \omega t_\ell &= \ln\frac{3 + \sqrt5}{2} = 0.9624 \quad &\text{(logarithm)} \\
> \left|\mathbf r_1^B\right| &= a\sqrt{2\left(1 + \cos\psi_\ell\right)} = 2a\cos\frac{\psi_\ell}{2} = \frac43\,a \quad &\text{(distance from $O$ at that instant)}
> \end{aligned}$$
>
> $$\boxed{\text{the string goes slack at } \psi_\ell = -2\arccos\frac23 \simeq -96.38^\circ, \quad t_\ell = \frac{1}{\omega}\ln\frac{3 + \sqrt5}{2} \simeq \frac{0.9624}{\omega}}$$
>
> **Units:** $[t_\ell] = [\omega^{-1}] = [\mathrm{T}]$; angles dimensionless
> **Meaning:** yes, it goes slack, once, after the string has turned 96.38 degrees clockwise from $Ox_1$ (it lags behind the vehicle), when the skater is at four thirds of $a$ from the centre. From then on, until the string becomes taut again (not studied here), no force acts in the plane and the skater moves in a straight line in $S_0$.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Relative acceleration | $\mathbf a_1^B = -a\left(\ddot\psi\sin\psi + \dot\psi^2\cos\psi\right)\mathbf i_1 + a\left(\ddot\psi\cos\psi - \dot\psi^2\sin\psi\right)\mathbf j_1 = a\ddot\psi\,\mathbf u_\perp - a\dot\psi^2\,\mathbf u_{AB}$ |
| (b) Centripetal term | $\boldsymbol\omega_{10}\times(\boldsymbol\omega_{10}\times\mathbf r_1^B) = -a\omega^2\left[(1 + \cos\psi)\mathbf i_1 + \sin\psi\,\mathbf j_1\right]$ |
| (b) Coriolis term | $2\boldsymbol\omega_{10}\times\mathbf v_1^B = -2a\omega\dot\psi\left(\cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1\right)$ |
| (c) Equation of motion and quadrature | $\ddot\psi + \omega^2\sin\psi = 0$; $\dot\psi = -2\omega\cos(\psi/2)$ for $-\pi \lt \psi \le 0$; $\int_0^{\psi}d\psi'/(2\cos(\psi'/2)) = -\int_0^t\omega\,dt'$, giving $\psi = 4\arctan(e^{-\omega t}) - \pi$ |
| (d) Tension | $T = 2ma\omega^2\cos(\psi/2)\left(3\cos(\psi/2) - 2\right)$ |
| (e) String | goes slack at $\psi = -2\arccos(2/3) \simeq -96.38^\circ$, at $t = \ln\frac{3 + \sqrt5}{2}/\omega \simeq 0.9624/\omega$ |
| Normal reaction of the plane | $N = mg$ |

**Check against the official key:** Problems.pdf, p. 72 prints the Coriolis acceleration, the "centrifugal acceleration" (the term called centripetal here, as in Notes.pdf, Eq. 3.25), the first-order equation of motion with its range, the tension and the angle at which the string goes slack. The box below sets them side by side with the results above: every one coincides, so there is no discrepancy.

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison of the results with the key
> **Source:** Problems.pdf, p. 72; Notes.pdf, Eq. 3.25
>
> $$\begin{aligned}
> \text{key: } \mathbf a_{cor} &= -2a\omega\dot\psi\left(\cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1\right) \quad &\text{(same as $2\boldsymbol\omega_{10}\times\mathbf v_1^B$, part (b))} \\
> \text{key: } \mathbf a_{cf} &= -a\omega^2\left[\left(1 + \cos\psi\right)\mathbf i_1 + \sin\psi\,\mathbf j_1\right] \quad &\text{(same as the centripetal term, part (b))} \\
> \text{key: } \dot\psi &= -2\omega\cos\left(\psi/2\right), \ -\pi \lt \psi \le 0 \quad &\text{(same as the sign box, part (c))} \\
> \text{key: } T &= 2ma\omega^2\cos\frac{\psi}{2}\left(3\cos\frac{\psi}{2} - 2\right) \quad &\text{(same as part (d))} \\
> \text{key: } \psi &= -2\arccos\left(2/3\right) \quad &\text{(same as part (e))}
> \end{aligned}$$
>
> $$\boxed{\text{all five results of the key coincide with this solution}}$$
>
> **Units:** accelerations $[\mathrm{L\,T^{-2}}]$, rate $[\mathrm{T^{-1}}]$, tension $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the key calls centrifugal acceleration the term that Notes.pdf calls centripetal; it is the same vector, pointing towards the axis.

> [!derivation] Independent check: mechanical energy in the rotating frame
> **Law:** in $S_1$ the mechanical energy is conserved when every force that does work there has a potential
> **Source:** [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]; Notes.pdf, Eq. 4.31
>
> Two reasons make the energy in $S_1$ a constant. First, the forces that do work in $S_1$ have a potential: $\boldsymbol\omega_{10}$ is constant, so the centrifugal force derives from $-\tfrac12 m\omega^2 r_\perp^2$, where $r_\perp$ is the distance to the axis through $O$ (here the whole of $|\mathbf r_1^B|$), while the force of the origin and the Euler force vanish. Second, the other forces do no work in $S_1$: the bar force lies along $\mathbf u_{AB}$, normal to the relative velocity along $\mathbf u_\perp$; the Coriolis force is normal to the relative velocity; the weight and the normal reaction are vertical.
>
> $$\begin{aligned}
> r_\perp^2 &= a^2\left(1 + \cos\psi\right)^2 + a^2\sin^2\psi = 2a^2\left(1 + \cos\psi\right) \quad &\text{(components of $\mathbf r_1^B$; Pythagorean identity)} \\
> E_1^B &= \tfrac12 m\,\mathbf v_1^B\cdot\mathbf v_1^B - \tfrac12 m\omega^2 r_\perp^2 = \tfrac12 ma^2\dot\psi^2 - ma^2\omega^2\left(1 + \cos\psi\right) \quad &\text{(kinetic energy in $S_1$ plus the centrifugal potential)} \\
> E_1^B(0) &= \tfrac12 ma^2\left(4\omega^2\right) - ma^2\omega^2\cdot 2 = 0 \quad &\text{($\dot\psi(0) = -2\omega$, $\psi(0) = 0$)} \\
> \dot\psi^2 &= 2\omega^2\left(1 + \cos\psi\right) \quad &\text{(constant energy equal to zero)}
> \end{aligned}$$
>
> $$\boxed{E_1^B = \tfrac12 ma^2\dot\psi^2 - ma^2\omega^2\left(1 + \cos\psi\right) = 0 \ \Rightarrow\ \dot\psi^2 = 2\omega^2\left(1 + \cos\psi\right)}$$
>
> **Units:** $[ma^2\omega^2] = [\mathrm{M\,L^2\,T^{-2}}]$, an energy
> **Meaning:** the energy route, which never uses the equation of motion, gives the same first integral; the energy is exactly that of the separatrix of the effective pendulum, which is why the skater only creeps towards the top position at $\psi$ equal to minus $\pi$.

> [!derivation] Check at the initial instant, in the inertial frame
> **Law:** composition of accelerations at the start; Newton's second law in $S_0$ along $\mathbf i_1$
> **Source:** Notes.pdf, Eq. 3.27; Notes.pdf, Eq. 4.59
>
> $$\begin{aligned}
> \ddot\psi(0) &= -\omega^2\sin 0 = 0, \quad \dot\psi(0) = -2\omega \quad &\text{(equation of motion; initial rate)} \\
> \mathbf a_1^B(0) &= -a\left(4\omega^2\right)\mathbf i_1 = -4a\omega^2\,\mathbf i_1 \quad &\text{(part (a) with $\mathbf u_{AB}(0) = \mathbf i_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^B(0) &= -2a\omega\left(-2\omega\right)\mathbf i_1 = 4a\omega^2\,\mathbf i_1 \quad &\text{(part (b))} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^B(0)\right) &= -2a\omega^2\,\mathbf i_1 \quad &\text{(part (b) with $\psi = 0$)} \\
> \mathbf a_0^B(0) &= -4a\omega^2\,\mathbf i_1 + 4a\omega^2\,\mathbf i_1 - 2a\omega^2\,\mathbf i_1 = -2a\omega^2\,\mathbf i_1 \quad &\text{(sum)} \\
> -T(0)\,\mathbf i_1 &= m\,\mathbf a_0^B(0) \ \Rightarrow\ T(0) = 2ma\omega^2 \quad &\text{(Eq. 4.59 along $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{T(0) = 2ma\omega^2 = \left. 2ma\omega^2\,c\left(3c - 2\right)\right|_{c = 1}}$$
>
> **Units:** $[a\omega^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** at rest in $S_0$, the skater is set in motion by the bar alone, which pulls her towards the vehicle; the inertial frame gives the same tension as the rotating one.

> [!derivation] Limiting cases
> **Law:** the results evaluated at extreme values of the data and of time
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 8
>
> $$\begin{aligned}
> \omega \to 0:\quad \dot\psi &= -2\omega\cos\frac{\psi}{2} \to 0, \quad T \to 0 \quad &\text{(a vehicle at rest pulls nothing)} \\
> t \to \infty:\quad \psi &\to 4\arctan 0 - \pi = -\pi, \quad \mathbf r_1^B \to a\left(1 - 1\right)\mathbf i_1 = \mathbf 0 \quad &\text{(rigid bar: $B$ approaches $O$)} \\
> t \to \infty:\quad T &\to 2ma\omega^2\cdot 0\cdot\left(0 - 2\right) = 0 \quad &\text{(the bar unloads at the end)} \\
> t_\ell \lt t:\quad T &\lt 0 \quad &\text{(rigid bar in compression; $3c - 2 \lt 0$)}
> \end{aligned}$$
>
> $$\boxed{\omega \to 0:\ T \to 0; \qquad t \to \infty:\ \psi \to -\pi,\ B \to O,\ T \to 0^-}$$
>
> **Units:** $[T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** a rigid bar pushes the skater after the instant at which a string would go slack, and the push dies out as she approaches the centre.

---

## Problem 08: Kinematics, Two Trains on Tracks

### Reference Frames, Bases and Coordinates

Two trains $A$ and $B$ run on parallel tracks separated by the distance $a$, with absolute velocities $v_A$ and $v_B$; the statement asks for the velocity of each train relative to the other, first for the two straight tracks and then when train $B$ runs on a circular track of radius $R$ whose minimum distance to the straight track of $A$ is $a$ (Problems.pdf, p. 8). The problem is kinematic only: both motions are given. The observer of each train is read as a reference frame attached to it; on the circular track that frame turns with train $B$ (a reading: an observer on $B$ that only translates is also considered in the answers), and the velocity seen by a moving observer follows from the derivative of a vector in a moving frame, Notes.pdf, Sec. 3.1 and Sec. 3.2.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, the ground; $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k\}$: $\mathbf i_0$ along the track of $A$, $\mathbf j_0$ towards the track of $B$ in the plane of the tracks, $\mathbf k$ the cross product of $\mathbf i_0$ and $\mathbf j_0$, normal to that plane (Notes.pdf, Eq. 2.1) |
| Origin $O$ | the position of train $A$ at the initial instant |
| Frame of train $A$ | $S_A = \{A;\ \mathcal B_0\}$: origin on the train, axes parallel to the ground axes, since a train on a straight track does not turn |
| Frame of train $B$, case 1 | $S_B = \{B;\ \mathcal B_0\}$, for the same reason |
| Frame of train $B$, case 2 | $S_B = \{B;\ \mathcal B_B\}$, $\mathcal B_B = \{\mathbf i_B, \mathbf j_B, \mathbf k\}$: $\mathbf i_B$ along the track in the sense of motion, $\mathbf j_B$ from the train towards the centre $C$ of the track; it turns with the train |
| Notation | $\mathbf v_A^B$: velocity of train $B$ relative to $S_A$; $\mathbf v_B^A$: velocity of train $A$ relative to $S_B$ (subscript the frame, superscript the point, as in Notes.pdf, Eq. 3.19) |
| Coordinates | case 1: abscissas of the trains along $\mathbf i_0$; case 2: abscissa of $A$ and the angle $\theta_B$ of the segment from $C$ to $B$, measured at $C$ from the downward vertical (minus $\mathbf j_0$), positive about $\mathbf k$ |
| Degrees of freedom | 1 per train (each is constrained to its track), both prescribed: no unknown coordinate |
| Data | $a$ [m], $R$ [m], $v_A$, $v_B$ [m s$^{-1}$]; angular rate of train $B$ on the circle $\omega_B = v_B/R$ [rad s$^{-1}$] |
| Hypotheses | the tracks lie in one plane; the speeds are constant; $v_A$ and $v_B$ are signed components (positive along $\mathbf i_0$ where the trains are side by side; a train running the other way has a negative value); at the initial instant $A$ is at $O$ and $B$ at the point of its track closest to the track of $A$; the case 2 answers hold for this initial configuration: with $A$ starting at the abscissa $x_{A0}$ the observer on $B$ reads $[v_A - v_B(R + a)/R]\,\mathbf i_0 - (v_B/R)(x_{A0} + v_A t)\,\mathbf j_0$, and another initial angle of $B$ shifts every sine and cosine of $\theta_B$ |
| Unknowns | the relative velocities $\mathbf v_A^B$ and $\mathbf v_B^A$ in each case |

### Change of Basis and Position Vector

#### Case 1: parallel straight tracks

![[attachments/EM-SOL/p08-parallel.svg]]

> [!derivation] Positions of the trains on parallel tracks
> **Law:** position vectors of points moving with constant velocity along straight lines
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5; Problems.pdf, p. 8
>
> $x_{B0}$ is the abscissa of $B$ at the initial instant (any value; it does not enter the velocities).
>
> $$\begin{aligned}
> \mathbf r_0^A &= v_A t\,\mathbf i_0 \quad &\text{($A$ starts at $O$ and runs along $\mathbf i_0$)} \\
> \mathbf r_0^B &= \left(x_{B0} + v_B t\right)\mathbf i_0 + a\,\mathbf j_0 \quad &\text{(track of $B$ at the distance $a$)} \\
> \mathbf r_A^B &= \mathbf r_0^B - \mathbf r_0^A = \left(x_{B0} + \left(v_B - v_A\right)t\right)\mathbf i_0 + a\,\mathbf j_0 \quad &\text{(Eq. 3.16 with the origin $A$ of $S_A$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^A = v_A t\,\mathbf i_0, \qquad \mathbf r_0^B = \left(x_{B0} + v_B t\right)\mathbf i_0 + a\,\mathbf j_0, \qquad \mathbf r_A^B = \left(x_{B0} + \left(v_B - v_A\right)t\right)\mathbf i_0 + a\,\mathbf j_0}$$
>
> **Units:** $[v_A t] = [\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$; $[a] = [\mathrm{L}]$
> **Meaning:** seen from $A$, train $B$ stays at the distance $a$ across and slides along the tracks.

#### Case 2: train B on a circular track

![[attachments/EM-SOL/p08-tracks.svg]]

> [!derivation] Position of train B on the circular track
> **Law:** position vector as a sum of segments; right triangle at the centre of the track
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 3.16; Problems.pdf, p. 8
>
> The closest point of the circle to the straight track lies on the perpendicular from the centre $C$, so $C$ is at the height $R + a$ above $O$ (its lowest point is then at the height $a$). From $O$ to $B$ we pass through $C$, because the distance from $C$ is the one that stays constant. Let $F$ be the point of the vertical through $C$ at the height of $B$: in the right triangle $CFB$ the hypotenuse is $R$; the leg opposite to $\theta_B$ is $R\sin\theta_B$, horizontal, along $\mathbf i_0$; the leg adjacent to $\theta_B$ is $R\cos\theta_B$, vertical, pointing down, along minus $\mathbf j_0$. The angle $\theta_B$ is measured from the downward vertical, not from $\mathbf i_0$: the standard polar angle about $C$ is $\varphi = \theta_B - \pi/2$, and the last two rows show that the standard form gives the same vector.
>
> $$\begin{aligned}
> \theta_B &= \omega_B t = \frac{v_B}{R}\,t \quad &\text{(arc $R\theta_B$ travelled at the speed $v_B$, from the closest point)} \\
> \overrightarrow{OC} &= \left(R + a\right)\mathbf j_0 \quad &\text{(centre above the closest point)} \\
> \overrightarrow{CB} &= R\sin\theta_B\,\mathbf i_0 - R\cos\theta_B\,\mathbf j_0 \quad &\text{(opposite leg along $\mathbf i_0$; adjacent leg along $-\mathbf j_0$)} \\
> \mathbf r_0^B &= \overrightarrow{OC} + \overrightarrow{CB} = R\sin\theta_B\,\mathbf i_0 + \left(R + a - R\cos\theta_B\right)\mathbf j_0 \quad &\text{(sum)} \\
> \cos\left(\theta_B - \tfrac{\pi}{2}\right) &= \cos\theta_B\cos\tfrac{\pi}{2} + \sin\theta_B\sin\tfrac{\pi}{2} = \sin\theta_B \quad &\text{(cosine of a difference)} \\
> \sin\left(\theta_B - \tfrac{\pi}{2}\right) &= \sin\theta_B\cos\tfrac{\pi}{2} - \cos\theta_B\sin\tfrac{\pi}{2} = -\cos\theta_B \quad &\text{(sine of a difference: $R\cos\varphi\,\mathbf i_0 + R\sin\varphi\,\mathbf j_0$ is $\overrightarrow{CB}$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^A = v_A t\,\mathbf i_0, \qquad \mathbf r_0^B = R\sin\theta_B\,\mathbf i_0 + \left(R + a - R\cos\theta_B\right)\mathbf j_0, \qquad \theta_B = \frac{v_B t}{R}}$$
>
> **Units:** $[R] = [a] = [\mathrm{L}]$; $[v_B t/R] = [1]$
> **Meaning:** at the initial instant train $B$ is at the height $a$ just above train $A$; with a positive $v_B$ it moves counterclockwise, along plus $\mathbf i_0$ at that point, like $A$.

![[attachments/EM-SOL/p08-train-basis.svg]]

> [!derivation] Basis of train B: rotation by theta_B about k
> **Law:** unit tangent of the track; elementary rotation about the third axis and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.9
>
> View along $\mathbf k$, which points out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up). The tangent is the derivative of $\overrightarrow{CB}$ with respect to the angle, divided by its length $R$. $\mathbf i_B$ is then $\mathbf i_0$ turned by $\theta_B$: hypotenuse 1, adjacent leg $\cos\theta_B$ along $\mathbf i_0$, opposite leg $\sin\theta_B$ along $\mathbf j_0$. $\mathbf j_B$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\theta_B$ along $\mathbf j_0$, opposite leg $\sin\theta_B$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \frac{d\overrightarrow{CB}}{d\theta_B} &= R\cos\theta_B\,\mathbf i_0 + R\sin\theta_B\,\mathbf j_0 \quad &\text{($\tfrac{d}{d\theta}\sin\theta = \cos\theta$, $\tfrac{d}{d\theta}(-\cos\theta) = \sin\theta$)} \\
> \mathbf i_B &= \frac{1}{R}\,\frac{d\overrightarrow{CB}}{d\theta_B} = \cos\theta_B\,\mathbf i_0 + \sin\theta_B\,\mathbf j_0 \quad &\text{(length $R\sqrt{\cos^2\theta_B + \sin^2\theta_B} = R$)} \\
> \mathbf j_B &= \mathbf k\times\mathbf i_B = -\sin\theta_B\,\mathbf i_0 + \cos\theta_B\,\mathbf j_0 = -\frac{\overrightarrow{CB}}{R} \quad &\text{($\mathbf k\times\mathbf i_0 = \mathbf j_0$, $\mathbf k\times\mathbf j_0 = -\mathbf i_0$): it points to $C$} \\
> \det[{}_0R_B] &= 1\cdot\left(\cos^2\theta_B + \sin^2\theta_B\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_B][{}_0R_B]^T\right)_{11} &= \cos^2\theta_B + \sin^2\theta_B = 1, \quad \left([{}_0R_B][{}_0R_B]^T\right)_{12} = \cos\theta_B\sin\theta_B - \sin\theta_B\cos\theta_B = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_B] = \begin{pmatrix} \cos\theta_B & -\sin\theta_B & 0 \cr \sin\theta_B & \cos\theta_B & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_B] = 1, \quad [{}_0R_B][{}_0R_B]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the frame of train $B$ turns by the same angle $\theta_B$ as the radius $CB$: the train always points along the track and its second axis always points to the centre.

![[attachments/EM-SOL/p08-observer-b.svg]]

> [!derivation] Position of train A seen from train B
> **Law:** relative position vector and its components in the basis of the moving frame (projections)
> **Source:** Notes.pdf, Eq. 3.1; Notes.pdf, Eq. 3.16
>
> $$\begin{aligned}
> \mathbf r_B^A &= \mathbf r_0^A - \mathbf r_0^B = \left(v_A t - R\sin\theta_B\right)\mathbf i_0 + \left(R\cos\theta_B - R - a\right)\mathbf j_0 \quad &\text{(Eq. 3.16 with the origin $B$ of $S_B$)} \\
> x &= \mathbf r_B^A\cdot\mathbf i_B = \left(v_A t - R\sin\theta_B\right)\cos\theta_B + \left(R\cos\theta_B - R - a\right)\sin\theta_B \quad &\text{(components of $\mathbf i_B$)} \\
> &= v_A t\cos\theta_B - \left(R + a\right)\sin\theta_B \quad &\text{($R\sin\theta_B\cos\theta_B$ cancels)} \\
> y &= \mathbf r_B^A\cdot\mathbf j_B = -\left(v_A t - R\sin\theta_B\right)\sin\theta_B + \left(R\cos\theta_B - R - a\right)\cos\theta_B \quad &\text{(components of $\mathbf j_B$)} \\
> &= R - \left(R + a\right)\cos\theta_B - v_A t\sin\theta_B \quad &\text{($R\sin^2\theta_B + R\cos^2\theta_B = R$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_B^A = x\,\mathbf i_B + y\,\mathbf j_B, \qquad x = v_A t\cos\theta_B - \left(R + a\right)\sin\theta_B, \qquad y = R - \left(R + a\right)\cos\theta_B - v_A t\sin\theta_B}$$
>
> **Units:** $[x] = [y] = [\mathrm{L}]$
> **Meaning:** at the initial instant train $A$ is at the distance $a$ from $B$ along minus $\mathbf j_B$, on the side opposite to the centre $C$.

### Kinematics

#### Case 1

> [!derivation] Relative velocities on parallel tracks
> **Law:** derivative of the relative position in a frame that translates without turning
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.28; [Lecture 5, Slide 24]
>
> The frames $S_A$ and $S_B$ have the basis $\mathcal B_0$, whose unit vectors are constant: the derivative in either frame is the derivative of the components.
>
> $$\begin{aligned}
> \mathbf v_0^A &= \frac{d}{dt}\left(v_A t\right)\mathbf i_0 = v_A\,\mathbf i_0, \quad \mathbf v_0^B = \frac{d}{dt}\left(x_{B0} + v_B t\right)\mathbf i_0 = v_B\,\mathbf i_0 \quad &\text{(Eq. 2.3; constant speeds)} \\
> \mathbf v_A^B &= \left.\frac{d\mathbf r_A^B}{dt}\right|_A = \frac{d}{dt}\left(x_{B0} + \left(v_B - v_A\right)t\right)\mathbf i_0 = \left(v_B - v_A\right)\mathbf i_0 \quad &\text{(derivative of the components; $a$ constant)} \\
> \mathbf v_0^B &= \mathbf v_0^A + \mathbf v_A^B \quad &\text{(check: Eq. 3.28, no rotation term)} \\
> \mathbf v_B^A &= \left.\frac{d}{dt}\left(\mathbf r_0^A - \mathbf r_0^B\right)\right|_B = \left(v_A - v_B\right)\mathbf i_0 \quad &\text{(same reasoning with the roles exchanged)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_A^B = \left(v_B - v_A\right)\mathbf i_0, \qquad \mathbf v_B^A = \left(v_A - v_B\right)\mathbf i_0 = -\mathbf v_A^B}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** each observer sees the other train move along the tracks with the difference of the speeds; the separation $a$ does not enter, because it is a constant part of the relative position.

#### Case 2

> [!derivation] Absolute velocities and the angular velocity of train B
> **Law:** time derivatives in $S_0$; chain rule; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4
>
> $$\begin{aligned}
> \mathbf v_0^A &= v_A\,\mathbf i_0 \quad &\text{(as in case 1)} \\
> \mathbf v_0^B &= R\cos\theta_B\,\dot\theta_B\,\mathbf i_0 + R\sin\theta_B\,\dot\theta_B\,\mathbf j_0 \quad &\text{(chain rule; $R$ and $a$ constant)} \\
> &= v_B\cos\theta_B\,\mathbf i_0 + v_B\sin\theta_B\,\mathbf j_0 = v_B\,\mathbf i_B \quad &\text{($R\dot\theta_B = R\,\omega_B = v_B$)} \\
> \boldsymbol\omega_{B0} &= \dot\theta_B\,\mathbf k = \omega_B\,\mathbf k \quad &\text{($\mathcal B_B$ turns about the fixed $\mathbf k$ with the angle $\theta_B$)} \\
> \left.\frac{d\mathbf i_B}{dt}\right|_0 &= -\omega_B\sin\theta_B\,\mathbf i_0 + \omega_B\cos\theta_B\,\mathbf j_0 = \omega_B\,\mathbf j_B = \boldsymbol\omega_{B0}\times\mathbf i_B \quad &\text{(chain rule; Eq. 3.3)} \\
> \left.\frac{d\mathbf j_B}{dt}\right|_0 &= -\omega_B\cos\theta_B\,\mathbf i_0 - \omega_B\sin\theta_B\,\mathbf j_0 = -\omega_B\,\mathbf i_B = \boldsymbol\omega_{B0}\times\mathbf j_B \quad &\text{(chain rule; Eq. 3.4)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^A = v_A\,\mathbf i_0, \quad \mathbf v_0^B = v_B\,\mathbf i_B, \quad \boldsymbol\omega_{B0} = \frac{v_B}{R}\,\mathbf k, \quad \left.\frac{d\mathbf i_B}{dt}\right|_0 = \omega_B\,\mathbf j_B, \quad \left.\frac{d\mathbf j_B}{dt}\right|_0 = -\omega_B\,\mathbf i_B}$$
>
> **Units:** $[v_B] = [\mathrm{L\,T^{-1}}]$; $[\omega_B] = [\mathrm{T^{-1}}]$
> **Meaning:** train $B$ keeps its speed but turns its direction; its frame turns at the rate of the radius $CB$.

> [!derivation] Velocity of train B relative to train A
> **Law:** derivative of the relative position in the frame of $A$, which translates without turning
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.28
>
> $$\begin{aligned}
> \mathbf r_A^B &= \mathbf r_0^B - \mathbf r_0^A = \left(R\sin\theta_B - v_A t\right)\mathbf i_0 + \left(R + a - R\cos\theta_B\right)\mathbf j_0 \quad &\text{(Eq. 3.16)} \\
> \mathbf v_A^B &= \left.\frac{d\mathbf r_A^B}{dt}\right|_A = \left(R\cos\theta_B\,\omega_B - v_A\right)\mathbf i_0 + R\sin\theta_B\,\omega_B\,\mathbf j_0 \quad &\text{(constant $\mathcal B_0$; chain rule)} \\
> &= \left(v_B\cos\theta_B - v_A\right)\mathbf i_0 + v_B\sin\theta_B\,\mathbf j_0 \quad &\text{($R\,\omega_B = v_B$)} \\
> \left|\mathbf v_A^B\right|^2 &= v_B^2\cos^2\theta_B - 2v_Av_B\cos\theta_B + v_A^2 + v_B^2\sin^2\theta_B \quad &\text{(squares expanded)} \\
> &= v_A^2 + v_B^2 - 2v_Av_B\cos\theta_B \quad &\text{($\cos^2 + \sin^2 = 1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_A^B = \mathbf v_0^B - \mathbf v_0^A = \left(v_B\cos\frac{v_Bt}{R} - v_A\right)\mathbf i_0 + v_B\sin\frac{v_Bt}{R}\,\mathbf j_0, \qquad \left|\mathbf v_A^B\right| = \sqrt{v_A^2 + v_B^2 - 2v_Av_B\cos\frac{v_Bt}{R}}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$; inside the root $[\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the observer on $A$ does not turn, so he sees the plain difference of the two absolute velocities, which changes only because $B$ turns.

> [!derivation] Velocity of train A relative to train B, which turns
> **Law:** time derivative in $S_0$ of the position written in the turning basis of $S_B$; product rule
> **Source:** Notes.pdf, Eq. 3.2; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.20; [Lecture 5, Slide 24]
>
> The relative velocity is the derivative in $S_B$, in which $\mathbf i_B$ and $\mathbf j_B$ are constant: the derivative of the components $x$ and $y$.
>
> $$\begin{aligned}
> \mathbf r_0^A &= \mathbf r_0^B + x\,\mathbf i_B + y\,\mathbf j_B \quad &\text{(Eq. 3.16)} \\
> \mathbf v_0^A &= \mathbf v_0^B + \dot x\,\mathbf i_B + \dot y\,\mathbf j_B + x\left.\frac{d\mathbf i_B}{dt}\right|_0 + y\left.\frac{d\mathbf j_B}{dt}\right|_0 \quad &\text{(derivative in $S_0$; product rule)} \\
> &= \mathbf v_0^B + \underbrace{\dot x\,\mathbf i_B + \dot y\,\mathbf j_B}_{\mathbf v_B^A} + \underbrace{\omega_B\left(x\,\mathbf j_B - y\,\mathbf i_B\right)}_{\boldsymbol\omega_{B0}\times\mathbf r_B^A} \quad &\text{(derivatives of the unit vectors)} \\
> \dot x &= v_A\cos\theta_B - v_A t\,\omega_B\sin\theta_B - \left(R + a\right)\omega_B\cos\theta_B \quad &\text{(product rule; chain rule, $\dot\theta_B = \omega_B$)} \\
> \dot y &= \left(R + a\right)\omega_B\sin\theta_B - v_A\sin\theta_B - v_A t\,\omega_B\cos\theta_B \quad &\text{(product rule; chain rule)} \\
> \dot x\cos\theta_B - \dot y\sin\theta_B &= v_A\left(\cos^2\theta_B + \sin^2\theta_B\right) - \left(R + a\right)\omega_B\left(\cos^2\theta_B + \sin^2\theta_B\right) \quad &\text{($\mathbf i_0$ part of $\dot x\,\mathbf i_B + \dot y\,\mathbf j_B$; the $v_At\omega_B$ terms cancel)} \\
> \dot x\sin\theta_B + \dot y\cos\theta_B &= -v_A t\,\omega_B\left(\sin^2\theta_B + \cos^2\theta_B\right) \quad &\text{($\mathbf j_0$ part; the other terms cancel in pairs)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_B^A = \dot x\,\mathbf i_B + \dot y\,\mathbf j_B = \left[v_A - v_B\,\frac{R + a}{R}\right]\mathbf i_0 - \frac{v_Av_B t}{R}\,\mathbf j_0}$$
>
> **Units:** $[v_B(R + a)/R] = [v_Av_Bt/R] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the observer on $B$ turns with the train, so to the difference of the absolute velocities he adds minus the transport term: the ground itself seems to turn about him, and the component along minus $\mathbf j_0$ grows linearly with time, with the distance travelled by $A$.

> [!derivation] Check: composition of velocities for the observer on B
> **Law:** absolute velocity as the velocity of the origin plus the relative and transport terms
> **Source:** Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0}\times\mathbf r_B^A &= \omega_B\,\mathbf k\times\left[\left(v_A t - R\sin\theta_B\right)\mathbf i_0 + \left(R\cos\theta_B - R - a\right)\mathbf j_0\right] \quad &\text{(relative position in $\mathcal B_0$)} \\
> &= -\omega_B\left(R\cos\theta_B - R - a\right)\mathbf i_0 + \omega_B\left(v_A t - R\sin\theta_B\right)\mathbf j_0 \quad &\text{($\mathbf k\times\mathbf i_0 = \mathbf j_0$, $\mathbf k\times\mathbf j_0 = -\mathbf i_0$)} \\
> \mathbf i_0:\ v_B\cos\theta_B + v_A - \left(R + a\right)\omega_B - \omega_B\left(R\cos\theta_B - R - a\right) &= v_A + \left(v_B - \omega_B R\right)\cos\theta_B = v_A \quad &\text{(origin + relative + transport; $\omega_B R = v_B$)} \\
> \mathbf j_0:\ v_B\sin\theta_B - \omega_B v_A t + \omega_B\left(v_A t - R\sin\theta_B\right) &= \left(v_B - \omega_B R\right)\sin\theta_B = 0 \quad &\text{(same sum)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^B + \mathbf v_B^A + \boldsymbol\omega_{B0}\times\mathbf r_B^A = v_A\,\mathbf i_0 = \mathbf v_0^A}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the three terms rebuild the absolute velocity of train $A$, as Eq. 3.20 requires: the relative velocity of the previous box is consistent.

### Answers and Checks

#### Case 1: parallel tracks

> [!derivation] Answer for parallel tracks
> **Law:** relative velocity for observers that translate without turning
> **Source:** Notes.pdf, Eq. 3.28; Problems.pdf, p. 8
>
> $$\begin{aligned}
> \mathbf v_A^B &= \left(v_B - v_A\right)\mathbf i_0 \quad &\text{(train $B$ seen from $A$)} \\
> \mathbf v_B^A &= \left(v_A - v_B\right)\mathbf i_0 \quad &\text{(train $A$ seen from $B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_A^B = -\mathbf v_B^A = \left(v_B - v_A\right)\mathbf i_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** for trains running the same way the relative speed is the difference of the speeds; for opposite senses (a negative signed value) it is their sum.

#### Case 2: train B on a circular track

> [!derivation] Answer for the circular track
> **Law:** relative velocities of the kinematics boxes, with the rate of the angle written out
> **Source:** Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.28; Problems.pdf, p. 8
>
> $$\begin{aligned}
> \mathbf v_A^B &= \left(v_B\cos\frac{v_Bt}{R} - v_A\right)\mathbf i_0 + v_B\sin\frac{v_Bt}{R}\,\mathbf j_0 \quad &\text{(observer on $A$, not turning)} \\
> \mathbf v_B^A &= \left[v_A - v_B\,\frac{R + a}{R}\right]\mathbf i_0 - \frac{v_Av_Bt}{R}\,\mathbf j_0 \quad &\text{(observer on $B$, turning with the train)} \\
> \left|\mathbf v_B^A\right|^2 &= \left(v_A - v_B\,\frac{R + a}{R}\right)^2 + \left(\frac{v_Av_Bt}{R}\right)^2 \quad &\text{(sum of squares)} \\
> \mathbf v_{B'}^A &= \mathbf v_0^A - \mathbf v_0^B = -\mathbf v_A^B = \left(v_A - v_B\cos\theta_B\right)\mathbf i_0 - v_B\sin\theta_B\,\mathbf j_0 \quad &\text{(other reading: observer $S_{B'} = \{B;\ \mathcal B_0\}$ that only translates, Eq. 3.28)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_A^B = \left(v_B\cos\frac{v_Bt}{R} - v_A\right)\mathbf i_0 + v_B\sin\frac{v_Bt}{R}\,\mathbf j_0, \qquad \mathbf v_B^A = \left[v_A - v_B\,\frac{R + a}{R}\right]\mathbf i_0 - \frac{v_Av_Bt}{R}\,\mathbf j_0 \ne -\mathbf v_A^B}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** with the reading of an observer that turns with $B$, the two answers are no longer opposite: the observer on $B$ turns, and the transport term adds to his reading a part proportional to the distance of $A$ from him, which here grows with time. With the other reading, an observer on $B$ that does not turn, the answer is just minus the velocity of $B$ relative to $A$.

| Part of the statement | Answer |
| :--- | :--- |
| Case 1, velocity of $B$ relative to $A$ | $\mathbf v_A^B = (v_B - v_A)\,\mathbf i_0$ |
| Case 1, velocity of $A$ relative to $B$ | $\mathbf v_B^A = (v_A - v_B)\,\mathbf i_0$ |
| Case 2, velocity of $B$ relative to $A$ | $\mathbf v_A^B = (v_B\cos(v_Bt/R) - v_A)\,\mathbf i_0 + v_B\sin(v_Bt/R)\,\mathbf j_0$, modulus $\sqrt{v_A^2 + v_B^2 - 2v_Av_B\cos(v_Bt/R)}$ |
| Case 2, velocity of $A$ relative to $B$, observer not turning (other reading) | $\mathbf v_{B'}^A = -\mathbf v_A^B = (v_A - v_B\cos(v_Bt/R))\,\mathbf i_0 - v_B\sin(v_Bt/R)\,\mathbf j_0$ |
| Case 2, velocity of $A$ relative to $B$ (frame turning with $B$) | $\mathbf v_B^A = [v_A - v_B(R + a)/R]\,\mathbf i_0 - (v_Av_Bt/R)\,\mathbf j_0$; in the basis of the train, $\dot x\,\mathbf i_B + \dot y\,\mathbf j_B$ with $\dot x$ and $\dot y$ of the kinematics box |
| Intermediate results | $\omega_B = v_B/R$; $\mathbf r_B^A = x\,\mathbf i_B + y\,\mathbf j_B$ with $x = v_At\cos\theta_B - (R + a)\sin\theta_B$, $y = R - (R + a)\cos\theta_B - v_At\sin\theta_B$ |

**Check against the official key:** Problems.pdf, p. 72 lists item 8 with no answer, so there is no key to compare with. Independent checks: the composition box rebuilds the absolute velocity of train $A$ from the three terms of Notes.pdf, Eq. 3.20, and the limiting cases below give back case 1.

> [!derivation] Limiting cases
> **Law:** the case 2 results at the initial instant and for a straight track
> **Source:** Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.28
>
> $$\begin{aligned}
> t = 0:\quad \mathbf v_A^B &= \left(v_B - v_A\right)\mathbf i_0 \quad &\text{($\cos 0 = 1$, $\sin 0 = 0$: the velocities are parallel)} \\
> t = 0:\quad \mathbf v_B^A &= \left(v_A - v_B\right)\mathbf i_0 - \frac{a}{R}\,v_B\,\mathbf i_0 \quad &\text{(transport term of a point at the distance $a$ from $B$)} \\
> R \to \infty:\quad \mathbf v_A^B &\to \left(v_B - v_A\right)\mathbf i_0, \quad \mathbf v_B^A \to \left(v_A - v_B\right)\mathbf i_0 \quad &\text{($v_Bt/R \to 0$, $a/R \to 0$: case 1)} \\
> v_A = 0:\quad \left|\mathbf v_A^B\right| &= v_B \quad &\text{(a train at rest sees the speed of $B$)} \\
> v_A = v_B = v:\quad \left|\mathbf v_A^B\right| &= v\sqrt{2 - 2\cos\frac{vt}{R}} = 2v\left|\sin\frac{vt}{2R}\right| \quad &\text{($1 - \cos\beta = 2\sin^2(\beta/2)$)}
> \end{aligned}$$
>
> $$\boxed{t = 0 \text{ or } R \to \infty: \ \text{case 1 recovered, except the term } -\tfrac{a}{R}\,v_B\,\mathbf i_0 \text{ of the turning observer at } t = 0}$$
>
> **Units:** $[a\,v_B/R] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** even at the start, when the two trains run side by side and parallel, the turning observer on $B$ reads a different speed for $A$, by the fraction $a/R$ of $v_B$, because $A$ is at the distance $a$ from the axis about which he turns; the difference disappears for a straight track.

---

## Problem 09: Artificial Gravity in a Rotating Cylinder (2001: A Space Odyssey)

### Reference Frames, Bases and Coordinates

A cylindrical spaceship of radius $R$ spins with constant angular velocity $\omega$ about its axis, and the astronauts live on its inner surface, where the centrifugal force plays the part of gravity (Problems.pdf, p. 8). The statement asks for the spin rate that gives the artificial gravity $g$ (with $R$ of 10 m and $g$ of 9.81 m/s$^2$), for the artificial gravity felt by an astronaut running on the surface with the constant speed $u$ relative to the cylinder, and for the condition to feel none. What the astronaut feels is defined in the frame of the hull, so the solution works in that frame with the inertia forces of Notes.pdf, Sec. 4.9, after deriving the composition of motions of Notes.pdf, Sec. 3.2.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $O$ on the axis of the cylinder, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ with $\mathbf k_0$ along the axis (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$ fixed to the hull, $\mathcal B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$, $\mathbf k_1 = \mathbf k_0$; it coincides with $S_0$ at the initial instant and turns by $\omega t$ |
| Cylindrical basis (in $S_1$) | $\mathcal B_2 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k_1\}$ at the astronaut: $\mathbf e_r$ from the axis to the floor, $\mathbf e_\theta$ along the floor in the sense of rotation, $\mathbf k_1$ along the axis |
| Coordinates | $\varphi$, the azimuth of the astronaut in $S_1$, measured from $\mathbf i_1$ about $\mathbf k_1$; $z$, her position along the axis |
| Constraint | she stays on the floor: distance $R$ from the axis |
| Degrees of freedom | 3 minus 1: 2, $\varphi$ and $z$, both prescribed by her running |
| Running velocity | $u_\theta = R\dot\varphi$ (along $\mathbf e_\theta$, positive in the sense of rotation) and $u_z = \dot z$ (along the axis), constant; $\gamma$ is the angle between the running direction and $\mathbf e_\theta$, so that $u_\theta = u\cos\gamma$ and $u_z = u\sin\gamma$ |
| Data | $R$ [m] (10 m), $g$ [m s$^{-2}$] (9.81 m s$^{-2}$), $u$ [m s$^{-1}$], $m$ [kg] the mass of the astronaut |
| Unknowns | (a) $\omega$ [rad s$^{-1}$]; (b) and (c) the floor force $\mathbf N$ [N] and the artificial gravity it means |
| Applied forces | none other than the floor: no external gravity (deep space) |
| Constraint force | the total force of the floor on her feet, $\mathbf N$ (normal part and any friction) |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Artificial gravity | what she feels as weight is the force she must receive from the floor: $g_{art}$ is the magnitude of $\mathbf N$ per unit mass, felt in the direction opposite to $\mathbf N$ (the reading of a scale under her feet). Another reading, the sum of the inertia forces per unit mass, $\omega^2R + 2\omega u\cos\gamma$, would vanish at the circumferential running speed $-\omega R/2$; it is rejected because there the floor still pushes her with $m u_\theta^2/R$, so a scale would not read zero |
| Hypotheses | $\omega$ constant; $O$ fixed in an inertial frame; her height $h$ is negligible against $R$ (statement), so she is a point particle at the distance $R$ from the axis; the running is uniform (constant components) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p09-cross-section.svg]]

> [!derivation] Basis of the hull: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> Cross-section seen along the axis, $\mathbf k_0$ out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up); a positive $\omega$ turns the hull counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf j_0$, opposite leg $\sin\omega t$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\omega t + \sin^2\omega t\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\omega t\sin\omega t - \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the hull axes follow the hull; seen from them the floor is at rest.

> [!derivation] Cylindrical basis at the astronaut and her position vector
> **Law:** elementary rotation by the azimuth about the axis; position vector as a sum of segments
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.28; Notes.pdf, Eq. 3.16
>
> Same view along the axis (⊙). $\mathbf e_r$ is $\mathbf i_1$ turned by $\varphi$: hypotenuse 1, adjacent leg $\cos\varphi$ along $\mathbf i_1$, opposite leg $\sin\varphi$ along $\mathbf j_1$. $\mathbf e_\theta$ is $\mathbf j_1$ turned by $\varphi$: adjacent leg $\cos\varphi$ along $\mathbf j_1$, opposite leg $\sin\varphi$ along minus $\mathbf i_1$ (the minus sign, for the same reason). From $O$ we go along the axis to the cross-section of the astronaut and then out along the radius to the floor.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1, \quad \mathbf e_\theta = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1 \quad &\text{(right triangles of the shaded figure)} \\
> \det[{}_1R_2] &= \cos^2\varphi + \sin^2\varphi = 1, \quad \mathbf e_r\cdot\mathbf e_\theta = -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi = 0 \quad &\text{(checks of the rotation)} \\
> \mathbf r_0^O &= \mathbf 0 \quad &\text{(the origin of $S_1$ is the fixed point $O$)} \\
> \mathbf r_0^P &= \mathbf r_1^P = z\,\mathbf k_1 + R\,\mathbf e_r \quad &\text{(along the axis, then radially to the floor)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = \mathbf r_1^P = R\,\mathbf e_r + z\,\mathbf k_1, \qquad \mathbf e_r = \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1, \qquad \mathbf e_\theta = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1}$$
>
> **Units:** $[R] = [z] = [\mathrm{L}]$
> **Meaning:** the part of the position normal to the spin axis is $R\,\mathbf e_r$, the same for every cross-section: every point of the floor is at the distance $R$ from the axis.

![[attachments/EM-SOL/p09-running.svg]]

> [!derivation] Running direction on the floor
> **Law:** components of a vector from its right triangle in the plane tangent to the floor
> **Source:** Notes.pdf, Eq. 2.24; Problems.pdf, p. 8
>
> The tangent plane of the floor at the astronaut contains $\mathbf e_\theta$ (around the hull) and $\mathbf k_1$ (along it); the figure shows it from outside, with $\mathbf e_r$ out of the paper (⊙), since $\mathbf e_\theta\times\mathbf k_1 = \mathbf e_r$. The running velocity is the hypotenuse $u$ of a right triangle; its leg along $\mathbf e_\theta$ is adjacent to $\gamma$ and its leg along $\mathbf k_1$ is opposite.
>
> $$\begin{aligned}
> u_\theta &= R\dot\varphi = u\cos\gamma \quad &\text{(adjacent leg)} \\
> u_z &= \dot z = u\sin\gamma \quad &\text{(opposite leg)} \\
> u_\theta^2 + u_z^2 &= u^2\left(\cos^2\gamma + \sin^2\gamma\right) = u^2 \quad &\text{(Pythagorean identity: speed $u$)}
> \end{aligned}$$
>
> $$\boxed{u_\theta = u\cos\gamma, \qquad u_z = u\sin\gamma, \qquad \dot\varphi = \frac{u\cos\gamma}{R}}$$
>
> **Units:** $[u] = [\mathrm{L\,T^{-1}}]$; $[\dot\varphi] = [\mathrm{T^{-1}}]$
> **Meaning:** $\gamma$ zero is running around the hull in the sense of rotation, $\gamma$ equal to $\pi$ against it, and $\gamma$ equal to $\pi/2$ along the axis.

### Kinematics

> [!derivation] Derivatives of the unit vectors in each frame
> **Law:** derivative of a unit vector of a turning basis; chain rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0 \quad &\text{(simple rotation about the fixed $\mathbf k_0$; $\omega$ constant)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \left.\frac{d\mathbf e_r}{dt}\right|_1 &= -\sin\varphi\,\dot\varphi\,\mathbf i_1 + \cos\varphi\,\dot\varphi\,\mathbf j_1 = \dot\varphi\,\mathbf e_\theta \quad &\text{(in $S_1$, $\mathbf i_1$ and $\mathbf j_1$ are constant; chain rule)} \\
> \left.\frac{d\mathbf e_\theta}{dt}\right|_1 &= -\cos\varphi\,\dot\varphi\,\mathbf i_1 - \sin\varphi\,\dot\varphi\,\mathbf j_1 = -\dot\varphi\,\mathbf e_r \quad &\text{(chain rule)} \\
> \left.\frac{d\mathbf e_r}{dt}\right|_0 &= \dot\varphi\,\mathbf e_\theta + \cos\varphi\,\omega\,\mathbf j_1 - \sin\varphi\,\omega\,\mathbf i_1 = \left(\dot\varphi + \omega\right)\mathbf e_\theta \quad &\text{(in $S_0$: also the derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf e_\theta}{dt}\right|_0 &= -\dot\varphi\,\mathbf e_r - \sin\varphi\,\omega\,\mathbf j_1 - \cos\varphi\,\omega\,\mathbf i_1 = -\left(\dot\varphi + \omega\right)\mathbf e_r \quad &\text{(same)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf e_r}{dt}\right|_1 = \dot\varphi\,\mathbf e_\theta, \quad \left.\frac{d\mathbf e_r}{dt}\right|_0 = \left(\dot\varphi + \omega\right)\mathbf e_\theta, \quad \left.\frac{d\mathbf e_\theta}{dt}\right|_0 = -\left(\dot\varphi + \omega\right)\mathbf e_r}$$
>
> **Units:** $[\dot\varphi] = [\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from the hull the cylindrical basis turns with her running only; seen from inertial space it turns with her running plus the spin, which is the extra part $\boldsymbol\omega_{10}$ applied to each unit vector.

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$; product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24
>
> $$\begin{aligned}
> \mathbf v_1^P &= \left.\frac{d}{dt}\right|_1\left(R\,\mathbf e_r + z\,\mathbf k_1\right) = R\dot\varphi\,\mathbf e_\theta + \dot z\,\mathbf k_1 \quad &\text{(Eq. 3.19; $R$ constant, $\mathbf k_1$ fixed in $S_1$)} \\
> &= u_\theta\,\mathbf e_\theta + u_z\,\mathbf k_1 \quad &\text{(running velocity)} \\
> \mathbf a_1^P &= \dot u_\theta\,\mathbf e_\theta + u_\theta\left.\frac{d\mathbf e_\theta}{dt}\right|_1 + \dot u_z\,\mathbf k_1 \quad &\text{(Eq. 3.24; product rule)} \\
> &= -u_\theta\dot\varphi\,\mathbf e_r = -\frac{u_\theta^2}{R}\,\mathbf e_r \quad &\text{(constant components; $\dot\varphi = u_\theta/R$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = u_\theta\,\mathbf e_\theta + u_z\,\mathbf k_1, \qquad \mathbf a_1^P = -\frac{u_\theta^2}{R}\,\mathbf e_r}$$
>
> **Units:** $[u_\theta^2/R] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in the hull she runs on a helix of radius $R$ (a circle when she runs around, a straight line along the axis), and only the part around the hull bends her path.

> [!derivation] Absolute velocity and acceleration: relative, transport, Coriolis and centripetal terms
> **Law:** time derivatives in $S_0$ of the position written in the turning bases; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.25; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left.\frac{d}{dt}\right|_0\left(R\,\mathbf e_r + z\,\mathbf k_1\right) = R\left(\dot\varphi + \omega\right)\mathbf e_\theta + \dot z\,\mathbf k_1 \quad &\text{(derivatives in $S_0$ of the previous box)} \\
> &= \underbrace{u_\theta\,\mathbf e_\theta + u_z\,\mathbf k_1}_{\mathbf v_1^P} + \underbrace{\omega R\,\mathbf e_\theta}_{\boldsymbol\omega_{10}\times\mathbf r_1^P} \quad &\text{($\omega\,\mathbf k_1\times(R\,\mathbf e_r + z\,\mathbf k_1) = \omega R\,\mathbf e_\theta$)} \\
> \mathbf a_0^P &= R\ddot\varphi\,\mathbf e_\theta + R\left(\dot\varphi + \omega\right)\left.\frac{d\mathbf e_\theta}{dt}\right|_0 + \ddot z\,\mathbf k_1 \quad &\text{(product rule; $\dot\omega$ zero)} \\
> &= -R\left(\dot\varphi + \omega\right)^2\mathbf e_r \quad &\text{(uniform running: $\ddot\varphi$ and $\ddot z$ zero)} \\
> &= -R\dot\varphi^2\,\mathbf e_r - 2R\omega\dot\varphi\,\mathbf e_r - R\omega^2\,\mathbf e_r \quad &\text{(square expanded)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\omega\,\mathbf k_1\times\left(u_\theta\,\mathbf e_\theta + u_z\,\mathbf k_1\right) = -2\omega u_\theta\,\mathbf e_r \quad &\text{($\mathbf k_1\times\mathbf e_\theta = -\mathbf e_r$, $\mathbf k_1\times\mathbf k_1 = \mathbf 0$)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \omega\,\mathbf k_1\times\left(\omega R\,\mathbf e_\theta\right) = -\omega^2R\,\mathbf e_r \quad &\text{(same products)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \mathbf v_1^P + \omega R\,\mathbf e_\theta, \qquad \mathbf a_0^P = \underbrace{-\frac{u_\theta^2}{R}\,\mathbf e_r}_{\mathbf a_1^P}\ \underbrace{- 2\omega u_\theta\,\mathbf e_r}_{2\boldsymbol\omega_{10}\times\mathbf v_1^P}\ \underbrace{- \omega^2R\,\mathbf e_r}_{\boldsymbol\omega_{10}\times(\boldsymbol\omega_{10}\times\mathbf r_1^P)} = -\frac{\left(\omega R + u_\theta\right)^2}{R}\,\mathbf e_r}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$: $[u_\theta^2/R] = [\omega u_\theta] = [\omega^2R]$
> **Meaning:** the three terms of the expanded square are the relative, Coriolis and centripetal accelerations of Eq. 3.25 (the origin and Euler terms vanish); the axial running gives none of them.

### Forces and Equations of Motion

The free-body diagram of the astronaut in $S_1$ shows the floor force, the centrifugal force away from the axis and the Coriolis force, which is radial too. There is no weight in deep space; the inertia force of the origin and the Euler force vanish ($O$ fixed, $\omega$ constant).

![[attachments/EM-SOL/p09-forces.svg]]

> [!derivation] Inertia forces and the floor force
> **Law:** Newton's second law in a non-inertial frame with the inertia forces
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\omega^2R\,\mathbf e_r \quad &\text{(centripetal term times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\omega u_\theta\,\mathbf e_r \quad &\text{(Coriolis term times $-m$)} \\
> m\,\mathbf a_1^P &= \mathbf N + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63; the floor is the only actual force)} \\
> -m\frac{u_\theta^2}{R}\,\mathbf e_r &= \mathbf N + m\omega^2R\,\mathbf e_r + 2m\omega u_\theta\,\mathbf e_r \quad &\text{(substituted)} \\
> \mathbf N &= -m\left(\omega^2R + 2\omega u_\theta + \frac{u_\theta^2}{R}\right)\mathbf e_r = -\frac{m}{R}\left(\omega R + u_\theta\right)^2\mathbf e_r \quad &\text{(solved; perfect square)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = -\frac{m}{R}\left(\omega R + u_\theta\right)^2\mathbf e_r, \qquad N_\theta = N_z = 0}$$
>
> **Units:** $[m\,\omega^2R] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations give the three components of the floor force; it points to the axis and has no part along the floor, so uniform running needs no friction.

### Answers and Checks

#### (a) Spin rate for the artificial gravity g

> [!derivation] Astronaut at rest on the floor
> **Law:** static balance in $S_1$ between the floor force and the centrifugal force
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 30]; Problems.pdf, p. 8
>
> $$\begin{aligned}
> u_\theta &= u_z = 0 \ \Rightarrow\ \mathbf N = -m\omega^2R\,\mathbf e_r \quad &\text{(floor-force box at rest; no Coriolis force)} \\
> g_{art} &= \frac{|\mathbf N|}{m} = \omega^2R \quad &\text{(definition of the artificial gravity)} \\
> \omega^2R &= g \ \Rightarrow\ \omega = \sqrt{\frac{g}{R}} \quad &\text{(positive root)} \\
> \omega &= \sqrt{\frac{9.81}{10}}\ \mathrm{s^{-1}} = \sqrt{0.981}\ \mathrm{s^{-1}} = 0.9905\ \text{rad/s} \quad &\text{(data)} \\
> T_{rev} &= \frac{2\pi}{\omega} = 6.344\ \mathrm{s}, \quad \frac{60\,\omega}{2\pi} = 9.458\ \text{rpm}, \quad \omega R = 9.905\ \text{m/s} \quad &\text{(period, revolutions per minute, floor speed)}
> \end{aligned}$$
>
> $$\boxed{\omega = \sqrt{\frac{g}{R}} = 0.9905\ \text{rad/s} \quad (\text{one turn in } 6.34\ \mathrm{s})}$$
>
> **Units:** $[\sqrt{g/R}] = [\mathrm{L\,T^{-2}}\,\mathrm{L^{-1}}]^{1/2} = [\mathrm{T^{-1}}]$
> **Meaning:** the floor pushes her towards the axis with the force $m\omega^2R$, and she reads it as a weight pointing away from the axis, towards the floor; the floor itself moves at 9.90 m/s in inertial space.

#### (b) Artificial gravity while running

> [!derivation] Artificial gravity felt by the running astronaut
> **Law:** floor-force box with the relative velocity of the running
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 31]; Problems.pdf, p. 8
>
> $$\begin{aligned}
> g_{art} &= \frac{|\mathbf N|}{m} = \frac{\left(\omega R + u_\theta\right)^2}{R} \quad &\text{(floor-force box)} \\
> &= \omega^2R + 2\omega u_\theta + \frac{u_\theta^2}{R} = g + 2\omega u_\theta + \frac{u_\theta^2}{R} \quad &\text{(square expanded; $\omega^2R = g$ from part (a))} \\
> &= g\left(1 + \frac{u\cos\gamma}{\omega R}\right)^2 = g\left(1 + \frac{u\cos\gamma}{\sqrt{gR}}\right)^2 \quad &\text{($u_\theta = u\cos\gamma$; $\omega R = \sqrt{gR}$)} \\
> \gamma = 0:\quad g_{art} &= \frac{\left(\omega R + u\right)^2}{R} \gt g \quad &\text{(around the hull, with the rotation)} \\
> \gamma = \pi:\quad g_{art} &= \frac{\left(\omega R - u\right)^2}{R} \lt g \ \ (0 \lt u \lt 2\omega R) \quad &\text{(around the hull, against the rotation)} \\
> \gamma = \tfrac{\pi}{2}:\quad g_{art} &= g \quad &\text{(along the axis: relative velocity parallel to $\boldsymbol\omega_{10}$)}
> \end{aligned}$$
>
> $$\boxed{g_{art} = \frac{\left(\omega R + u\cos\gamma\right)^2}{R} = g + 2\omega u\cos\gamma + \frac{u^2\cos^2\gamma}{R}}$$
>
> **Units:** $[\omega u] = [u^2/R] = [g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** with the data of part (a), running at 2 m/s around the hull gives 14.17 m/s$^2$ (1.44 g) with the rotation and 6.25 m/s$^2$ (0.64 g) against it; at 5 m/s, 22.21 m/s$^2$ (2.26 g) and 2.41 m/s$^2$ (0.25 g).

#### (c) Condition for no artificial gravity

> [!derivation] Weightlessness while running
> **Law:** a perfect square vanishes only when its base vanishes
> **Source:** Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 4.63; Problems.pdf, p. 8
>
> $$\begin{aligned}
> g_{art} &= 0 \iff \omega R + u_\theta = 0 \iff u_\theta = -\omega R \quad &\text{(part (b))} \\
> u\cos\gamma &= -\omega R \ \Rightarrow\ \cos\gamma = -\frac{\omega R}{u}, \quad \text{possible only if } u \ge \omega R \quad &\text{(running direction; $|\cos\gamma| \le 1$)} \\
> \mathbf v_0^P &= \mathbf v_1^P + \omega R\,\mathbf e_\theta = \left(u_\theta + \omega R\right)\mathbf e_\theta + u_z\,\mathbf k_1 = u_z\,\mathbf k_1 \quad &\text{(absolute velocity box)} \\
> \mathbf a_0^P &= -\frac{\left(\omega R + u_\theta\right)^2}{R}\,\mathbf e_r = \mathbf 0 \quad &\text{(absolute acceleration box)}
> \end{aligned}$$
>
> $$\boxed{u_\theta = u\cos\gamma = -\omega R = -\sqrt{gR}\ \ (9.90\ \text{m/s}); \quad \text{running only around the hull: } u = \omega R \text{ against the rotation}}$$
>
> **Units:** $[\omega R] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** she must run against the rotation so fast that the part of her running around the hull cancels the speed of the floor; she is then at rest in inertial space (or drifts uniformly along the axis if she also runs along it), no force is needed and the floor slides under her feet. A speed below 9.90 m/s, a sprinter's speed, cannot achieve it.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Spin rate | $\omega = \sqrt{g/R} = 0.9905$ rad/s for $R = 10$ m and $g = 9.81$ m/s$^2$ (one turn in 6.34 s, 9.46 rpm) |
| (b) Artificial gravity while running | $g_{art} = (\omega R + u\cos\gamma)^2/R = g + 2\omega u\cos\gamma + u^2\cos^2\gamma/R$, felt away from the axis; the floor force is $\mathbf N = -m(\omega R + u_\theta)^2\,\mathbf e_r/R$ |
| (c) No artificial gravity | $u_\theta = -\omega R$: the part of the running velocity around the hull equal to the floor speed $\sqrt{gR}$ (9.90 m/s), against the rotation; any axial part is allowed; it needs $u \ge \omega R$ |
| Intermediate results | $\mathbf a_1^P = -u_\theta^2\,\mathbf e_r/R$; Coriolis acceleration $-2\omega u_\theta\,\mathbf e_r$; centripetal acceleration $-\omega^2R\,\mathbf e_r$; $\mathbf v_0^P = (\omega R + u_\theta)\,\mathbf e_\theta + u_z\,\mathbf k_1$ |

**Check against the official key:** Problems.pdf, p. 72 lists item 9 with no answer, so there is no key to compare with. Independent checks: the inertial reading below gives the same floor force without inertia forces, and the limiting cases close the results.

> [!derivation] Independent check in the inertial frame
> **Law:** Newton's second law in $S_0$ with the absolute acceleration
> **Source:** Notes.pdf, Eq. 4.59; Notes.pdf, Eq. 3.25
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left(\omega R + u_\theta\right)\mathbf e_\theta + u_z\,\mathbf k_1 \quad &\text{(absolute velocity box)} \\
> m\,\mathbf a_0^P &= \mathbf N \quad &\text{(Eq. 4.59: the floor is the only force)} \\
> \mathbf N &= -\frac{m\left(\omega R + u_\theta\right)^2}{R}\,\mathbf e_r \quad &\text{(absolute acceleration box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = -\frac{m}{R}\left(\omega R + u_\theta\right)^2\mathbf e_r \quad \text{(same as in } S_1\text{)}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** in inertial space she moves on a circle or helix of radius $R$ with the speed around the axis $\omega R + u_\theta$, so the floor must provide the centripetal force of that speed; the rotating observer splits the same force into the centrifugal, Coriolis and relative parts.

> [!derivation] Limiting cases
> **Law:** the artificial gravity of part (b) at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 8
>
> $$\begin{aligned}
> u \to 0:\quad g_{art} &\to \omega^2R = g \quad &\text{(part (a) recovered)} \\
> u \ll \omega R:\quad g_{art} &\simeq g\left(1 + \frac{2u\cos\gamma}{\sqrt{gR}}\right) \quad &\text{(first order in $u$: the Coriolis term alone)} \\
> R \to \infty,\ g \text{ fixed}:\quad \frac{2u}{\sqrt{gR}} &\to 0 \quad &\text{(relative Coriolis correction of a larger hull)} \\
> u = 2\ \text{m/s},\ R = 10\ \text{m}:\quad \frac{2u}{\sqrt{gR}} &= \frac{4}{9.905} = 0.404 \quad &\text{(first-order correction for the data)}
> \end{aligned}$$
>
> $$\boxed{g_{art} \to g \ \text{for} \ u \to 0; \qquad \text{first-order change } \pm 2\omega u \ \text{around the hull}}$$
>
> **Units:** $2u/\sqrt{gR}$ is dimensionless
> **Meaning:** a runner in a small hull feels a large change of weight (about 40 percent at 2 m/s in the hull of 10 m, to first order), which is why large habitats are more comfortable.

---

## Problem 20: Heavy Particle on a Rotating Circumference

### Reference Frames, Bases and Coordinates

A heavy particle moves along a smooth circumference of radius $R$ and centre $O$; one diameter is vertical and the circumference turns about it with the constant angular velocity $\omega$; $\theta$ is the angle between the particle and the lowest point (Problems.pdf, p. 10). The statement asks to discuss the conservation of the mechanical energy in the moving frame and compute its value, and for the reaction of the circumference normal to its plane as a function of $\theta$. The wire is fixed in the frame that turns with it, so the solution works in that frame, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ vertical, up, along the axis of rotation (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$ attached to the circumference: $\mathbf k_1 = \mathbf k_0$; $\mathbf i_1$ horizontal, in the plane of the circumference, on the side where $\theta$ is positive; $\mathbf j_1$ the cross product of $\mathbf k_1$ and $\mathbf i_1$, normal to the plane of the circumference; it turns by $\omega t$ about $\mathbf k_0$ |
| Wire basis | $\mathcal B_2 = \{\mathbf e_r, \mathbf e_\theta, -\mathbf j_1\}$: $\mathbf e_r$ from $O$ to the particle $P$, $\mathbf e_\theta$ tangent to the circumference in the sense of growing $\theta$ |
| Coordinate | $\theta$, the angle at $O$ from the downward vertical to $OP$, positive towards $\mathbf i_1$ |
| Constraints | $P$ on the circumference: distance $R$ from $O$ and plane of the circumference, both fixed in $S_1$; smooth and bilateral (a bead on the wire) |
| Degrees of freedom | 3 minus 2: 1, the angle $\theta(t)$ |
| Data | $m$ [kg], $R$ [m], $\omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$]; initial values $\theta_0$ [rad] and $\dot\theta_0$ [rad s$^{-1}$] (not given in the statement, kept as symbols) |
| Unknowns | $\theta(t)$; reaction $\mathbf N = N_r\,\mathbf e_r + N_b\,\mathbf j_1$ (normal subspace of a curve, Notes.pdf, Eq. 6.16): $N_r$ in the plane, $N_b$ normal to it |
| Applied force | weight $-mg\,\mathbf k_1$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial with $O$ fixed; uniform gravity; $\omega$ constant; smooth wire, so the reaction has no component along the tangent |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p20-top-view.svg]]

> [!derivation] Basis of the rotating circumference: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> Top view along $\mathbf k_0$, out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up); the circumference is seen edge-on, along $\mathbf i_1$, and turns counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf j_0$, opposite leg $\sin\omega t$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\omega t + \sin^2\omega t\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\omega t\sin\omega t - \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** $\mathbf j_1$ is horizontal and normal to the plane of the circumference: the direction of the reaction asked for in part (b).

![[attachments/EM-SOL/p20-wire-plane.svg]]

> [!derivation] Position vector and wire basis in the plane of the circumference
> **Law:** right triangle in the plane of the wire; relation with the standard polar angle; rotation in that plane and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 3.16; Problems.pdf, p. 10
>
> Plane of the circumference, fixed in $S_1$, drawn with $\mathbf i_1$ to the right and $\mathbf k_1$ up; then $\mathbf j_1$, the cross product of $\mathbf k_1$ (up) and $\mathbf i_1$ (right), points into the paper (⊗), and minus $\mathbf j_1$ out of it. Let $F$ be the point of the vertical diameter at the height of $P$: in the right triangle $OFP$ the hypotenuse is $R$; the leg opposite to $\theta$ is $R\sin\theta$, horizontal, along $\mathbf i_1$; the leg adjacent to $\theta$ is $R\cos\theta$, vertical, pointing down, along minus $\mathbf k_1$ (the minus sign: $\theta$ is measured from the downward vertical). The standard polar angle of this plane, measured from $\mathbf i_1$ towards $\mathbf k_1$, is $\theta - \pi/2$. The tangent is the derivative of $\mathbf e_r$ with respect to $\theta$.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^P = \mathbf r_1^P = \overrightarrow{OP} \quad &\text{(origin of $S_1$ at the fixed centre; Eq. 3.16)} \\
> \mathbf e_r &= \sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf k_1 \quad &\text{(legs of $OFP$ divided by $R$)} \\
> \cos\left(\theta - \tfrac{\pi}{2}\right) &= \sin\theta, \quad \sin\left(\theta - \tfrac{\pi}{2}\right) = -\cos\theta \quad &\text{(difference formulas: the standard form gives the same $\mathbf e_r$)} \\
> \mathbf e_\theta &= \frac{d\mathbf e_r}{d\theta} = \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf k_1 \quad &\text{($\tfrac{d}{d\theta}\sin\theta = \cos\theta$, $\tfrac{d}{d\theta}(-\cos\theta) = \sin\theta$; unit length)} \\
> \mathbf e_r\times\mathbf e_\theta &= \sin^2\theta\,\mathbf i_1\times\mathbf k_1 - \cos^2\theta\,\mathbf k_1\times\mathbf i_1 = -\mathbf j_1 \quad &\text{($\mathbf i_1\times\mathbf k_1 = -\mathbf j_1$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> \det[{}_1R_2] &= -(-1)\left(\sin^2\theta + \cos^2\theta\right) = 1 \quad &\text{(expansion along the second row, entry $-1$ in place (2,3))} \\
> \mathbf e_r\cdot\mathbf e_\theta &= \sin\theta\cos\theta - \cos\theta\sin\theta = 0 \quad &\text{(columns orthogonal: $[{}_1R_2][{}_1R_2]^T = I$)} \\
> \mathbf r_1^P &= R\,\mathbf e_r = R\sin\theta\,\mathbf i_1 - R\cos\theta\,\mathbf k_1 \quad &\text{(position vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = R\sin\theta\,\mathbf i_1 - R\cos\theta\,\mathbf k_1, \quad [{}_1R_2] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \cr 0 & 0 & -1 \cr -\cos\theta & \sin\theta & 0 \end{pmatrix}, \quad \det[{}_1R_2] = 1}$$
>
> **Units:** $[R] = [\mathrm{L}]$; direction cosines dimensionless
> **Meaning:** $\theta$ zero is the lowest point and $\theta$ equal to $\pi/2$ the end of the horizontal diameter; the distance of $P$ to the axis is the horizontal leg $R\sin\theta$.

### Kinematics

> [!derivation] Derivatives of the unit vectors
> **Law:** derivative of a unit vector of a turning basis; chain rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0 \quad &\text{(simple rotation about the fixed vertical; $\omega$ constant)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \left.\frac{d\mathbf e_r}{dt}\right|_1 &= \frac{d\mathbf e_r}{d\theta}\,\dot\theta = \dot\theta\,\mathbf e_\theta \quad &\text{(chain rule; $\mathbf i_1$, $\mathbf k_1$ constant in $S_1$)} \\
> \left.\frac{d\mathbf e_\theta}{dt}\right|_1 &= \left(-\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1\right)\dot\theta = -\dot\theta\,\mathbf e_r \quad &\text{(chain rule)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf e_r}{dt}\right|_1 = \dot\theta\,\mathbf e_\theta, \quad \left.\frac{d\mathbf e_\theta}{dt}\right|_1 = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** $[\omega] = [\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** in $S_1$ only the wire basis turns, with the particle; in $S_0$ the whole plane turns about the vertical as well.

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$; product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24
>
> $$\begin{aligned}
> \mathbf v_1^P &= \left.\frac{d}{dt}\right|_1\left(R\,\mathbf e_r\right) = R\dot\theta\,\mathbf e_\theta \quad &\text{($R$ constant)} \\
> \mathbf a_1^P &= R\ddot\theta\,\mathbf e_\theta + R\dot\theta\left.\frac{d\mathbf e_\theta}{dt}\right|_1 = R\ddot\theta\,\mathbf e_\theta - R\dot\theta^2\,\mathbf e_r \quad &\text{(product rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = R\dot\theta\,\mathbf e_\theta, \qquad \mathbf a_1^P = R\ddot\theta\,\mathbf e_\theta - R\dot\theta^2\,\mathbf e_r}$$
>
> **Units:** $[R\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[R\ddot\theta] = [R\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in $S_1$ the particle moves on a fixed circle: a tangential acceleration and a centripetal one towards $O$.

> [!derivation] Absolute velocity and acceleration: relative, transport, Coriolis and centripetal terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis $\mathcal B_1$; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left.\frac{d}{dt}\right|_0\left(R\sin\theta\,\mathbf i_1 - R\cos\theta\,\mathbf k_1\right) = R\dot\theta\cos\theta\,\mathbf i_1 + R\sin\theta\,\omega\,\mathbf j_1 + R\dot\theta\sin\theta\,\mathbf k_1 \quad &\text{(product rule; chain rule; derivatives of $\mathbf i_1$, $\mathbf k_1$)} \\
> &= \underbrace{R\dot\theta\,\mathbf e_\theta}_{\mathbf v_1^P} + \underbrace{\omega R\sin\theta\,\mathbf j_1}_{\boldsymbol\omega_{10}\times\mathbf r_1^P} \quad &\text{(grouped; $\omega\,\mathbf k_1\times\mathbf r_1^P = \omega R\sin\theta\,\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \frac{d}{dt}\left(R\dot\theta\cos\theta\right)\mathbf i_1 + \frac{d}{dt}\left(R\dot\theta\sin\theta\right)\mathbf k_1 + R\dot\theta\cos\theta\,\omega\,\mathbf j_1 = \mathbf a_1^P + \omega R\dot\theta\cos\theta\,\mathbf j_1 \quad &\text{(components in $S_1$ plus the turning of $\mathbf i_1$)} \\
> \left.\frac{d}{dt}\right|_0\left(\omega R\sin\theta\,\mathbf j_1\right) &= \omega R\dot\theta\cos\theta\,\mathbf j_1 - \omega^2R\sin\theta\,\mathbf i_1 \quad &\text{(chain rule; derivative of $\mathbf j_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\omega R\dot\theta\,\mathbf k_1\times\left(\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf k_1\right) = 2\omega R\dot\theta\cos\theta\,\mathbf j_1 \quad &\text{(the two $\mathbf j_1$ terms above)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \omega\,\mathbf k_1\times\left(\omega R\sin\theta\,\mathbf j_1\right) = -\omega^2R\sin\theta\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term above; $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = R\dot\theta\,\mathbf e_\theta + \omega R\sin\theta\,\mathbf j_1, \qquad \mathbf a_0^P = R\ddot\theta\,\mathbf e_\theta - R\dot\theta^2\,\mathbf e_r + 2\omega R\dot\theta\cos\theta\,\mathbf j_1 - \omega^2R\sin\theta\,\mathbf i_1}$$
>
> **Units:** every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the Coriolis acceleration is normal to the plane of the wire; it appears because the distance to the axis changes while the plane turns. The centripetal one points horizontally to the axis.

### Forces and Equations of Motion

The free-body diagram of the particle in $S_1$ shows the weight, the reaction (in the plane along $\mathbf e_r$, normal to the plane along $\mathbf j_1$), the centrifugal force, horizontal and away from the axis, and the Coriolis force, normal to the plane. The inertia force of the origin and the Euler force vanish ($O$ fixed, $\omega$ constant).

![[attachments/EM-SOL/p20-fbd.svg]]

> [!derivation] Newton's second law in the rotating frame, projected on the wire basis
> **Law:** Newton's second law in a non-inertial frame with the inertia forces; reaction of a smooth curve
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.16; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\omega^2R\sin\theta\,\mathbf i_1 \quad &\text{(centripetal term times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = -2m\omega R\dot\theta\cos\theta\,\mathbf j_1 \quad &\text{(Coriolis term times $-m$)} \\
> m\,\mathbf a_1^P &= -mg\,\mathbf k_1 + N_r\,\mathbf e_r + N_b\,\mathbf j_1 + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63; $\mathbf F_A$, $\mathbf F_E$ zero)} \\
> \mathbf k_1\cdot\mathbf e_\theta &= \sin\theta, \quad \mathbf i_1\cdot\mathbf e_\theta = \cos\theta, \quad \mathbf k_1\cdot\mathbf e_r = -\cos\theta, \quad \mathbf i_1\cdot\mathbf e_r = \sin\theta \quad &\text{(components of the wire basis)} \\
> \mathbf e_\theta:\ mR\ddot\theta &= -mg\sin\theta + m\omega^2R\sin\theta\cos\theta \quad &\text{(tangent: no reaction)} \\
> \mathbf e_r:\ -mR\dot\theta^2 &= mg\cos\theta + N_r + m\omega^2R\sin^2\theta \quad &\text{(in the plane, along the radius)} \\
> \mathbf j_1:\ 0 &= N_b - 2m\omega R\dot\theta\cos\theta \quad &\text{(normal to the plane: no relative motion there)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = -\frac{g}{R}\sin\theta + \omega^2\sin\theta\cos\theta, \qquad N_r = -mR\dot\theta^2 - mg\cos\theta - m\omega^2R\sin^2\theta, \qquad N_b = 2m\omega R\dot\theta\cos\theta}$$
>
> **Units:** $[g/R] = [\omega^2] = [\mathrm{T^{-2}}]$; $[m\omega R\dot\theta] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations for the three unknowns $\theta$, $N_r$ and $N_b$: the tangent equation is the equation of motion, the other two give the reaction afterwards. The normal reaction balances the Coriolis force alone.

### Answers and Checks

#### (a) Mechanical energy in the moving frame

> [!derivation] Which forces do work in the rotating frame, and their potentials
> **Law:** power of each force on the relative velocity; potential as minus the work along the wire, with Barrow's rule
> **Source:** [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]; Notes.pdf, Eq. 4.14; Notes.pdf, Sec. 6.4
>
> The energy in $S_1$ is conserved if every force that does work in $S_1$ has a potential. Two reasons hold here. First, the forces that do no work in $S_1$: the reaction, because the wire is smooth and at rest in $S_1$, so the reaction is normal to the relative velocity; the Coriolis force, always normal to the relative velocity; and the force of the origin and the Euler force, which vanish. Second, the forces that do work have potentials: the weight, and the centrifugal force because $\boldsymbol\omega_{10}$ is constant. Along the wire the displacement is $R\,\mathbf e_\theta\,d\theta'$.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= R\dot\theta\left(N_r\,\mathbf e_r + N_b\,\mathbf j_1\right)\cdot\mathbf e_\theta = 0, \quad \mathbf F_{COR}\cdot\mathbf v_1^P = -2m\omega R^2\dot\theta^2\cos\theta\,\mathbf j_1\cdot\mathbf e_\theta = 0 \quad &\text{(no power in $S_1$)} \\
> V_g(\theta) - V_g(0) &= -\int_0^{\theta}\left(-mg\,\mathbf k_1\right)\cdot\mathbf e_\theta\,R\,d\theta' = mgR\int_0^{\theta}\sin\theta'\,d\theta' \quad &\text{(Eq. 4.14; $\mathbf k_1\cdot\mathbf e_\theta = \sin\theta'$)} \\
> &= mgR\left[-\cos\theta'\right]_0^{\theta} = mgR\left(1 - \cos\theta\right) \quad &\text{(antiderivative $-\cos\theta'$; Barrow's rule)} \\
> V_C(\theta) - V_C(0) &= -\int_0^{\theta} m\omega^2R\sin\theta'\,\mathbf i_1\cdot\mathbf e_\theta\,R\,d\theta' = -m\omega^2R^2\int_0^{\theta}\sin\theta'\cos\theta'\,d\theta' \quad &\text{(Eq. 4.14; $\mathbf i_1\cdot\mathbf e_\theta = \cos\theta'$)} \\
> &= -m\omega^2R^2\left[\tfrac12\sin^2\theta'\right]_0^{\theta} = -\tfrac12 m\omega^2R^2\sin^2\theta \quad &\text{(antiderivative $\tfrac12\sin^2\theta'$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{V_g = -mgR\cos\theta \ \ \text{(zero at the height of $O$)}, \qquad V_C = -\tfrac12 m\omega^2R^2\sin^2\theta = -\tfrac12 m\omega^2 r_\perp^2}$$
>
> **Units:** $[mgR] = [m\omega^2R^2] = [\mathrm{M\,L^2\,T^{-2}}]$, energies
> **Meaning:** the centrifugal potential of the wire is the potential of Slide 30 with the distance to the axis $R\sin\theta$; it is lowest where the particle is farthest from the axis.

> [!derivation] Energy integral in the rotating frame
> **Law:** the tangent equation multiplied by the relative speed is an exact derivative (chain rule); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]
>
> $$\begin{aligned}
> mR^2\dot\theta\ddot\theta + mgR\sin\theta\,\dot\theta - m\omega^2R^2\sin\theta\cos\theta\,\dot\theta &= 0 \quad &\text{(tangent equation times $R\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12 mR^2\dot\theta^2\right) &= mR^2\dot\theta\ddot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(-mgR\cos\theta\right) &= mgR\sin\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(-\tfrac12 m\omega^2R^2\sin^2\theta\right) &= -m\omega^2R^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule on $\sin^2\theta$)} \\
> \left[\tfrac12 mR^2\dot\theta^2 - mgR\cos\theta - \tfrac12 m\omega^2R^2\sin^2\theta\right]_0^t &= 0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{E_1^P = \tfrac12 mR^2\dot\theta^2 - mgR\cos\theta - \tfrac12 m\omega^2R^2\sin^2\theta = \tfrac12 mR^2\dot\theta_0^2 - mgR\cos\theta_0 - \tfrac12 m\omega^2R^2\sin^2\theta_0}$$
>
> **Units:** each term $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy in $S_1$ (kinetic energy of the relative motion plus the potentials of the weight and of the centrifugal force) is conserved; its value is fixed by the initial angle and rate, which the statement leaves free.

> [!derivation] The energy in the inertial frame is not conserved
> **Law:** power of the reaction on the absolute velocity; kinetic energy in $S_0$
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_0^P &= \left(N_r\,\mathbf e_r + N_b\,\mathbf j_1\right)\cdot\left(R\dot\theta\,\mathbf e_\theta + \omega R\sin\theta\,\mathbf j_1\right) = N_b\,\omega R\sin\theta \quad &\text{(absolute velocity box)} \\
> &= 2m\omega^2R^2\dot\theta\sin\theta\cos\theta \quad &\text{($N_b$ of the equations of motion)} \\
> E_0^P &= \tfrac12 m\left(R^2\dot\theta^2 + \omega^2R^2\sin^2\theta\right) - mgR\cos\theta = E_1^P + m\omega^2R^2\sin^2\theta \quad &\text{(kinetic energy in $S_0$ plus the weight potential)} \\
> \frac{dE_0^P}{dt} &= 0 + 2m\omega^2R^2\sin\theta\cos\theta\,\dot\theta \quad &\text{($E_1^P$ constant; chain rule)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_0^P}{dt} = \mathbf N\cdot\mathbf v_0^P = N_b\,\omega R\sin\theta \ne 0}$$
>
> **Units:** $[N_b\,\omega R] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** in $S_0$ the wire moves and its reaction does work, so the energy there changes at the rate of that power (Eq. 4.11); in $S_1$ the wire is at rest and the energy is a constant.

#### (b) Reaction normal to the plane of the circumference

> [!derivation] Normal reaction as a function of theta
> **Law:** equation normal to the plane with the rate eliminated through the energy integral
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.19; [Lecture 5, Slide 29]
>
> $$\begin{aligned}
> N_b &= 2m\omega R\dot\theta\cos\theta \quad &\text{(equation along $\mathbf j_1$)} \\
> R^2\dot\theta^2 &= \frac{2E_1^P}{m} + 2gR\cos\theta + \omega^2R^2\sin^2\theta \quad &\text{(energy integral solved for the squared rate)} \\
> &= R^2\dot\theta_0^2 + 2gR\left(\cos\theta - \cos\theta_0\right) + \omega^2R^2\left(\sin^2\theta - \sin^2\theta_0\right) \quad &\text{(value of $E_1^P$)} \\
> R\dot\theta &= \pm\sqrt{R^2\dot\theta_0^2 + 2gR\left(\cos\theta - \cos\theta_0\right) + \omega^2R^2\left(\sin^2\theta - \sin^2\theta_0\right)} \quad &\text{(sign of $\dot\theta$)}
> \end{aligned}$$
>
> $$\boxed{N_b(\theta) = \pm\,2m\omega\cos\theta\sqrt{\frac{2E_1^P}{m} + 2gR\cos\theta + \omega^2R^2\sin^2\theta} \quad (\text{sign of } \dot\theta), \qquad \text{along } \mathbf j_1}$$
>
> **Units:** $[2E_1^P/m] = [gR] = [\omega^2R^2] = [\mathrm{L^2\,T^{-2}}]$, so $[N_b] = [\mathrm{M}][\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]$, a force
> **Meaning:** the normal reaction vanishes when the particle is at rest on the wire and when it crosses the horizontal diameter; it pushes the particle forwards, in the sense of the rotation, while the particle moves away from the axis, and backwards while it comes closer (the angular momentum box below shows why).

| Part of the statement | Answer |
| :--- | :--- |
| (a) Energy in the moving frame | conserved: the reaction and the Coriolis force do no work in $S_1$, the origin and Euler forces vanish, and the weight and the centrifugal force (constant $\omega$) have potentials; $E_1^P = \frac12 mR^2\dot\theta^2 - mgR\cos\theta - \frac12 m\omega^2R^2\sin^2\theta$, equal to its initial value $\frac12 mR^2\dot\theta_0^2 - mgR\cos\theta_0 - \frac12 m\omega^2R^2\sin^2\theta_0$ |
| (b) Reaction normal to the plane | $N_b = 2m\omega R\dot\theta\cos\theta = \pm 2m\omega\cos\theta\sqrt{2E_1^P/m + 2gR\cos\theta + \omega^2R^2\sin^2\theta}$ along $\mathbf j_1$ |
| Intermediate results | equation of motion $\ddot\theta = -(g/R)\sin\theta + \omega^2\sin\theta\cos\theta$; reaction in the plane $N_r = -mR\dot\theta^2 - mg\cos\theta - m\omega^2R\sin^2\theta$; energy in $S_0$ not conserved, its rate is $N_b\,\omega R\sin\theta$ |

**Check against the official key:** Problems.pdf, p. 72 lists item 20 with no answer, so there is no key to compare with. Independent checks: the normal reaction follows again from the angular momentum about the vertical axis in $S_0$ (box below), without inertia forces, and the limiting cases close the results.

> [!derivation] Independent check: angular momentum about the vertical axis
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.51; Notes.pdf, Eq. 4.53
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf k_1 &= m\left(\mathbf r_0^P\times\mathbf v_0^P\right)\cdot\mathbf k_1 = m\left(x_1v_{y1} - y_1v_{x1}\right) \quad &\text{(Eq. 4.48; $x_1$, $y_1$ the components on $\mathbf i_1$, $\mathbf j_1$)} \\
> &= m\left(R\sin\theta\cdot\omega R\sin\theta - 0\cdot R\dot\theta\cos\theta\right) = m\omega R^2\sin^2\theta \quad &\text{(absolute velocity box)} \\
> \mathbf M_O\cdot\mathbf k_1 &= \left(\mathbf r_0^P\times N_b\,\mathbf j_1\right)\cdot\mathbf k_1 = R\sin\theta\,N_b \quad &\text{(weight vertical and $N_r\,\mathbf e_r$ through $O$: no axial moment)} \\
> \frac{d}{dt}\left(m\omega R^2\sin^2\theta\right) &= 2m\omega R^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule; $\mathbf k_1$ fixed)} \\
> R\sin\theta\,N_b &= 2m\omega R^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(Eq. 4.53, axial component)}
> \end{aligned}$$
>
> $$\boxed{N_b = 2m\omega R\dot\theta\cos\theta \quad (\sin\theta \ne 0)}$$
>
> **Units:** $[H] = [\mathrm{M\,L^2\,T^{-1}}]$; $[R\,N_b] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** to keep turning at the rate $\omega$ while its distance to the axis changes, the particle needs an axial moment, and only the normal reaction can give it: the same result as the Coriolis balance in $S_1$.

> [!derivation] Limiting cases and relative equilibria
> **Law:** the results at extreme values of the data; rest in $S_1$ in the equation of motion
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \omega \to 0:\quad N_b &\to 0, \quad E_1^P \to \tfrac12 mR^2\dot\theta^2 - mgR\cos\theta \quad &\text{(simple pendulum of length $R$)} \\
> \dot\theta = 0,\ \ddot\theta = 0:\quad \sin\theta\left(\omega^2\cos\theta - \frac{g}{R}\right) &= 0 \quad &\text{(relative equilibria)} \\
> \theta_e &= 0, \quad \theta_e = \pi, \quad \cos\theta_e = \frac{g}{\omega^2R} \ \ (\omega^2R \gt g) \quad &\text{(the three families)} \\
> N_b(\theta_e) &= 0 \quad &\text{(no relative velocity)}
> \end{aligned}$$
>
> $$\boxed{\omega \to 0: \ N_b \to 0; \qquad \text{relative equilibria } \theta = 0,\ \pi \ \text{and}\ \cos\theta = g/(\omega^2R) \ \text{if}\ \omega^2R \gt g}$$
>
> **Units:** $[g/(\omega^2R)] = [1]$
> **Meaning:** without rotation the bead is a pendulum and the wire does not push sideways; a bead at rest on the turning wire needs no normal reaction either, and above the critical rate it can rest off the bottom (these equilibria are not asked for).

---

## Problem 21: Apparent Weight on a Spinning Planet

### Reference Frames, Bases and Coordinates

On a spinning spherical planet of radius $R$ and gravitational acceleration $g_p$, bodies weigh twice as much at the poles as at the equator; the statement asks for the duration of the day (Problems.pdf, p. 10). The weight of a body is what a scale on the ground reads, a quantity defined in the frame of the planet, where the body is at rest; the solution works in that frame, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $O$ at the centre of the planet, axes fixed with respect to the stars; $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ with $\mathbf k_0$ along the polar axis, towards the north pole (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$ fixed to the planet: $\mathbf k_1 = \mathbf k_0$; $\mathbf i_1$ in the equatorial plane and in the meridian plane of the body; $\mathbf j_1$ the cross product of $\mathbf k_1$ and $\mathbf i_1$ (towards the east); it turns by $\Omega t$ about $\mathbf k_0$ |
| Local basis at the body | $\mathcal B_2 = \{\mathbf e_r, \mathbf e_n, -\mathbf j_1\}$: $\mathbf e_r$ the local vertical, from $O$ to the body $P$; $\mathbf e_n$ horizontal, towards the north pole |
| Coordinate | $\lambda$, the latitude of $P$: the angle at $O$ from the equatorial plane to $OP$, positive towards the north |
| Degrees of freedom | none to find: the body is at rest on the ground, at a fixed latitude |
| Data | $R$ [m], $g_p$ [m s$^{-2}$], $m$ [kg] the mass of the body; the ratio 2 between the weights at a pole and at the equator |
| Unknowns | the spin rate $\Omega$ [rad s$^{-1}$] and the day $T_{day}$ [s]; on the way, the contact force $\mathbf N$ [N] |
| Applied force | the attraction of the planet, $-mg_p\,\mathbf e_r$ at the surface |
| Constraint force | the contact force of the ground (or of a scale) $\mathbf N$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Weight | the magnitude $W$ of the contact force on a body at rest on the ground, what a scale reads |
| Hypotheses | the frame of the centre is inertial; $\Omega$ constant; rigid spherical planet with a spherical mass distribution, so the attraction at the surface has the same magnitude $g_p$ everywhere and points to $O$; the ground can push but not pull; the day is the period of one rotation with respect to the stars (the statement gives no orbit, so a solar day is not computed) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p21-top-view.svg]]

> [!derivation] Basis of the planet: rotation by Omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above the north pole, along $\mathbf k_0$, out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up); a positive $\Omega$ turns the planet counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ along $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\Omega t$ along $\mathbf j_0$, opposite leg $\sin\Omega t$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\Omega t + \sin^2\Omega t\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\Omega t\sin\Omega t - \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \cr \sin\Omega t & \cos\Omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the planet axes come back to their initial position after the time in which $\Omega t$ grows by $2\pi$: that time is the day.

![[attachments/EM-SOL/p21-meridian.svg]]

> [!derivation] Position of the body in its meridian plane
> **Law:** right triangle in the meridian plane; part of the position normal to the spin axis
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 3.16; [Lecture 5, Slide 30]
>
> Meridian plane of the body, drawn with $\mathbf i_1$ to the right and $\mathbf k_1$ up; $\mathbf j_1$, the cross product of $\mathbf k_1$ (up) and $\mathbf i_1$ (right), points into the paper (⊗). Let $F$ be the foot of the perpendicular from $P$ to the equatorial line: in the right triangle $OFP$ the hypotenuse is $R$, the leg adjacent to $\lambda$ is $R\cos\lambda$ along $\mathbf i_1$ and the leg opposite to $\lambda$ is $R\sin\lambda$ along $\mathbf k_1$. $\lambda$ is measured from $\mathbf i_1$ towards $\mathbf k_1$, so it is already the standard polar angle of this plane.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^P = \mathbf r_1^P = \overrightarrow{OP} \quad &\text{(origin of $S_1$ at the centre; Eq. 3.16)} \\
> \mathbf r_1^P &= R\cos\lambda\,\mathbf i_1 + R\sin\lambda\,\mathbf k_1 = R\,\mathbf e_r \quad &\text{(legs of $OFP$)} \\
> \mathbf r_\parallel &= \left(\mathbf r_1^P\cdot\mathbf k_1\right)\mathbf k_1 = R\sin\lambda\,\mathbf k_1 \quad &\text{(part along the spin axis)} \\
> \mathbf r_\perp &= \mathbf r_1^P - \mathbf r_\parallel = R\cos\lambda\,\mathbf i_1 \quad &\text{(part normal to the spin axis, Slide 30)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = R\cos\lambda\,\mathbf i_1 + R\sin\lambda\,\mathbf k_1, \qquad \mathbf r_\perp = R\cos\lambda\,\mathbf i_1}$$
>
> **Units:** $[R] = [\mathrm{L}]$
> **Meaning:** at a pole the body is on the axis and its distance to it is zero; at the equator the distance is the whole radius.

![[attachments/EM-SOL/p21-local-basis.svg]]

> [!derivation] Local basis: rotation by the latitude in the meridian plane
> **Law:** elementary rotation in the meridian plane; change of basis matrix, its checks and its inverse
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19
>
> Same meridian view: $\mathbf j_1$ into the paper (⊗), so minus $\mathbf j_1$, the cross product of $\mathbf i_1$ and $\mathbf k_1$, points out of it (⊙), and positive angles about minus $\mathbf j_1$ are counterclockwise. $\mathbf e_r$ is $\mathbf i_1$ turned by $\lambda$: adjacent leg $\cos\lambda$ along $\mathbf i_1$, opposite leg $\sin\lambda$ along $\mathbf k_1$. $\mathbf e_n$ is $\mathbf k_1$ turned by $\lambda$: adjacent leg $\cos\lambda$ along $\mathbf k_1$, opposite leg $\sin\lambda$ along minus $\mathbf i_1$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\lambda\,\mathbf i_1 + \sin\lambda\,\mathbf k_1, \quad \mathbf e_n = -\sin\lambda\,\mathbf i_1 + \cos\lambda\,\mathbf k_1 \quad &\text{(the two right triangles)} \\
> \mathbf e_r\times\mathbf e_n &= \cos^2\lambda\,\mathbf i_1\times\mathbf k_1 - \sin^2\lambda\,\mathbf k_1\times\mathbf i_1 = -\mathbf j_1 \quad &\text{($\mathbf i_1\times\mathbf k_1 = -\mathbf j_1$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> \det[{}_1R_2] &= (-1)\cdot(-1)^{2+3}\left(\cos^2\lambda + \sin^2\lambda\right) = 1 \quad &\text{(expansion along the second row, entry $-1$ in place (2,3), cofactor sign $(-1)^5$)} \\
> \mathbf e_r\cdot\mathbf e_n &= -\cos\lambda\sin\lambda + \sin\lambda\cos\lambda = 0 \quad &\text{(checks: $[{}_1R_2][{}_1R_2]^T = I$)} \\
> \mathbf i_1 &= \cos\lambda\,\mathbf e_r - \sin\lambda\,\mathbf e_n \quad &\text{(inverse: first row of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \cos\lambda & -\sin\lambda & 0 \cr 0 & 0 & -1 \cr \sin\lambda & \cos\lambda & 0 \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad \mathbf i_1 = \cos\lambda\,\mathbf e_r - \sin\lambda\,\mathbf e_n}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the inverse relation splits the centrifugal force, along $\mathbf i_1$, into a part along the local vertical and a local horizontal part along minus $\mathbf e_n$, towards the equator (south in the northern hemisphere).

### Kinematics

> [!derivation] Composition of motions for a body at rest on the planet
> **Law:** derivatives of the unit vectors of a turning basis; time derivatives in $S_0$ of the position written in $\mathcal B_1$
> **Source:** Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.25; [Lecture 5, Slide 25]
>
> In $S_1$ the latitude and the radius are constant and $\mathbf i_1$, $\mathbf k_1$ are fixed, so the relative velocity and the relative acceleration vanish.
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0 \quad &\text{(simple rotation about the polar axis; $\Omega$ constant)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf k_1\times\mathbf i_1 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \mathbf v_1^P &= \mathbf 0, \quad \mathbf a_1^P = \mathbf 0 \quad &\text{(constant components in $S_1$)} \\
> \mathbf v_0^P &= \left.\frac{d}{dt}\right|_0\left(R\cos\lambda\,\mathbf i_1 + R\sin\lambda\,\mathbf k_1\right) = R\cos\lambda\,\Omega\,\mathbf j_1 = \boldsymbol\omega_{10}\times\mathbf r_1^P \quad &\text{(only the turning of $\mathbf i_1$: transport term)} \\
> \mathbf a_0^P &= \left.\frac{d}{dt}\right|_0\left(\Omega R\cos\lambda\,\mathbf j_1\right) = -\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(only the turning of $\mathbf j_1$)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf k_1\times\left(\Omega R\cos\lambda\,\mathbf j_1\right) = -\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(the same vector: centripetal term)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = \mathbf a_1^P = \mathbf 0, \qquad \mathbf v_0^P = \Omega R\cos\lambda\,\mathbf j_1, \qquad \mathbf a_0^P = \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = -\Omega^2\,\mathbf r_\perp}$$
>
> **Units:** $[\Omega R] = [\mathrm{L\,T^{-1}}]$; $[\Omega^2R] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** of the terms of Eq. 3.27 only the centripetal one survives: the body describes its parallel of latitude, of radius $R\cos\lambda$, once per day; with no relative velocity there is no Coriolis term.

### Forces and Equations of Motion

The free-body diagram of the body in $S_1$ shows the attraction of the planet towards $O$, the contact force of the ground and the centrifugal force, horizontal and away from the axis. The Coriolis force vanishes (the body is at rest in $S_1$), and so do the inertia force of the origin and the Euler force.

![[attachments/EM-SOL/p21-fbd.svg]]

> [!derivation] Static balance in the planet frame
> **Law:** Newton's second law in a non-inertial frame with the inertia forces, at relative rest
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(centripetal term times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = \mathbf 0, \quad \mathbf F_A = \mathbf F_E = \mathbf 0 \quad &\text{(rest in $S_1$; $O$ fixed; $\Omega$ constant)} \\
> m\,\mathbf a_1^P &= \mathbf 0 = -mg_p\,\mathbf e_r + \mathbf N + m\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(Eq. 4.63)} \\
> \mathbf N &= mg_p\,\mathbf e_r - m\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(solved)} \\
> &= m\left(g_p - \Omega^2R\cos^2\lambda\right)\mathbf e_r + m\Omega^2R\cos\lambda\sin\lambda\,\mathbf e_n \quad &\text{($\mathbf i_1 = \cos\lambda\,\mathbf e_r - \sin\lambda\,\mathbf e_n$)} \\
> W^2 &= \left|\mathbf N\right|^2 = m^2\left[\left(g_p - \Omega^2R\cos^2\lambda\right)^2 + \Omega^4R^2\cos^2\lambda\sin^2\lambda\right] \quad &\text{(components squared and added)} \\
> &= m^2\left[g_p^2 - \left(2g_p\Omega^2R - \Omega^4R^2\right)\cos^2\lambda\right] \quad &\text{($\cos^4\lambda + \cos^2\lambda\sin^2\lambda = \cos^2\lambda$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = m\left(g_p - \Omega^2R\cos^2\lambda\right)\mathbf e_r + m\Omega^2R\cos\lambda\sin\lambda\,\mathbf e_n, \qquad W = m\sqrt{g_p^2 - \left(2g_p\Omega^2R - \Omega^4R^2\right)\cos^2\lambda}}$$
>
> **Units:** $[g_p] = [\Omega^2R] = [\mathrm{L\,T^{-2}}]$, so $[W] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations give the three components of the contact force. Away from the poles and the equator it has a horizontal part towards the north (in the northern hemisphere), which a rigid spherical ground must supply by friction: the plumb line does not point to the centre.

### Answers and Checks

> [!derivation] Weights at a pole and at the equator
> **Law:** static balance of the previous box at the latitudes of a pole and of the equator; contact condition of a unilateral constraint
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 6.4; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \lambda = \tfrac{\pi}{2}:\quad \mathbf N_{pole} &= mg_p\,\mathbf k_1, \quad W_{pole} = mg_p \quad &\text{($\cos\lambda = 0$: on the axis, no centrifugal force)} \\
> \lambda = 0:\quad \mathbf N_{eq} &= m\left(g_p - \Omega^2R\right)\mathbf i_1 \quad &\text{($\mathbf e_r = \mathbf i_1$: centrifugal force radial and outward)} \\
> g_p - \Omega^2R &\ge 0 \ \Rightarrow\ W_{eq} = m\left(g_p - \Omega^2R\right) \quad &\text{(the ground pushes, it cannot pull)}
> \end{aligned}$$
>
> $$\boxed{W_{pole} = mg_p, \qquad W_{eq} = m\left(g_p - \Omega^2R\right) \ \ \left(\Omega^2R \le g_p\right)}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the spin does not change the weight at a pole and lightens it at the equator; a body could not stay on the equator of a planet spinning faster than the break-up rate.

> [!derivation] Spin rate and duration of the day
> **Law:** condition of the statement on the two weights; period of a uniform rotation
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 10
>
> $$\begin{aligned}
> W_{eq} &= m\left|g_p - \Omega^2R\right|, \quad W_{pole} = 2W_{eq} \ \Rightarrow\ mg_p = 2m\left|g_p - \Omega^2R\right| \quad &\text{(statement; magnitude of $\mathbf N_{eq}$)} \\
> g_p - \Omega^2R &= \pm\frac{g_p}{2} \ \Rightarrow\ \Omega^2R = \frac{g_p}{2} \ \ \text{or} \ \ \Omega^2R = \frac{3g_p}{2} \quad &\text{(two roots)} \\
> \Omega^2R = \frac{3g_p}{2}:\quad \mathbf N_{eq} &= m\left(g_p - \frac{3g_p}{2}\right)\mathbf i_1 = -\frac{mg_p}{2}\,\mathbf i_1 \quad &\text{(the ground would pull: rejected; it gives $T = 2\pi\sqrt{2R/(3g_p)} \simeq 5.130\sqrt{R/g_p}$)} \\
> \Omega^2R &= \frac{g_p}{2} \le g_p \ \Rightarrow\ \Omega = \sqrt{\frac{g_p}{2R}} \quad &\text{(kept: the contact condition holds; positive root)} \\
> \Omega\,T_{day} &= 2\pi \quad &\text{(one turn of $\mathcal B_1$, first box)} \\
> T_{day} &= \frac{2\pi}{\Omega} = 2\pi\sqrt{\frac{2R}{g_p}} = 2\sqrt2\,\pi\sqrt{\frac{R}{g_p}} \simeq 8.886\sqrt{\frac{R}{g_p}} \quad &\text{(substituted)}
> \end{aligned}$$
>
> $$\boxed{\Omega = \sqrt{\frac{g_p}{2R}}, \qquad T_{day} = 2\pi\sqrt{\frac{2R}{g_p}}}$$
>
> **Units:** $[\sqrt{R/g_p}] = [\mathrm{L}\,\mathrm{L^{-1}\,T^{2}}]^{1/2} = [\mathrm{T}]$
> **Meaning:** the centrifugal force at the equator cancels half of the attraction there. The second root would need the ground to pull the body.

| Part of the statement | Answer |
| :--- | :--- |
| Duration of the day | $T_{day} = 2\pi\sqrt{2R/g_p} \simeq 8.886\sqrt{R/g_p}$ (one rotation with respect to the stars) |
| Intermediate results | $\Omega = \sqrt{g_p/(2R)}$; $W_{pole} = mg_p$, $W_{eq} = m(g_p - \Omega^2R) = mg_p/2$; contact force $\mathbf N = m(g_p - \Omega^2R\cos^2\lambda)\,\mathbf e_r + m\Omega^2R\cos\lambda\sin\lambda\,\mathbf e_n$ |

**Check against the official key:** Problems.pdf, p. 72 lists item 21 with no answer, so there is no key to compare with. Independent checks: Newton's law in the inertial frame gives the same contact force (box below), and the limiting cases close the result.

> [!derivation] Independent check in the inertial frame
> **Law:** Newton's second law in $S_0$ with the absolute acceleration of the kinematics box
> **Source:** Notes.pdf, Eq. 4.59
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg_p\,\mathbf e_r + \mathbf N \quad &\text{(Eq. 4.59: attraction and contact are the only forces)} \\
> -m\Omega^2R\cos\lambda\,\mathbf i_1 &= -mg_p\,\mathbf e_r + \mathbf N \quad &\text{(kinematics box)} \\
> \mathbf N &= mg_p\,\mathbf e_r - m\Omega^2R\cos\lambda\,\mathbf i_1 \quad &\text{(solved)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = mg_p\,\mathbf e_r - m\Omega^2R\cos\lambda\,\mathbf i_1 \quad \text{(same as in } S_1\text{)}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** seen from the stars the body moves on its parallel of latitude and needs a centripetal force towards the axis; the attraction minus the contact force provides it.

> [!derivation] Limiting cases and the weight at any latitude
> **Law:** the weight formula of the balance box at extreme values and with the rate found
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \Omega \to 0:\quad W_{eq} &\to mg_p = W_{pole} \quad &\text{(no spin, no difference)} \\
> \Omega_b &= \sqrt{\frac{g_p}{R}}:\quad W_{eq} = 0 \quad &\text{(break-up rate: weightless equator)} \\
> \frac{\Omega}{\Omega_b} &= \sqrt{\frac{g_p/(2R)}{g_p/R}} = \frac{1}{\sqrt2} \simeq 0.707 \quad &\text{(the planet of the statement)} \\
> \Omega^2R = \frac{g_p}{2}:\quad W(\lambda) &= m\sqrt{g_p^2 - \left(g_p^2 - \tfrac14 g_p^2\right)\cos^2\lambda} = mg_p\sqrt{1 - \tfrac34\cos^2\lambda} \quad &\text{(balance box at a general latitude)} \\
> \lambda = \tfrac{\pi}{4}:\quad W &= mg_p\sqrt{1 - \tfrac38} = mg_p\sqrt{\tfrac58} \simeq 0.791\,mg_p \quad &\text{($\cos^2\tfrac{\pi}{4} = \tfrac12$)}
> \end{aligned}$$
>
> $$\boxed{W(\lambda) = mg_p\sqrt{1 - \tfrac34\cos^2\lambda}: \ \ mg_p/2 \ \text{at the equator}, \ \ mg_p \ \text{at the poles}}$$
>
> **Units:** $[mg_p] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the planet spins at 0.707 of its break-up rate; the weight grows monotonically from the equator to the poles (0.791 of the polar value at 45 degrees), so the ratio 2 of the statement is the largest ratio of weights between two places of the planet.

---

## Problem 22: Particle on a Curve

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides without friction on a plane curve of the shape given in the table, between the two crests at plus and minus $\pi a$; it starts at $O$ with the speed $v_0$ along the positive $x$ axis (Problems.pdf, p. 10). Parts (a) to (c) take the curve at rest; parts (d) to (g) let it turn about the vertical axis $OY$ with the constant rate $\Omega$. The fixed curve is solved in the inertial frame with the projections of Notes.pdf, Sec. 6.5; the turning curve in the frame attached to it, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Curve | $y = a\left(1 - \cos(x/a)\right)$ for $-\pi a \le x \le \pi a$, in a vertical plane; $a \gt 0$ |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$: $\mathbf i_0$ along $OX$ (horizontal), $\mathbf j_0$ along $OY$ (vertical, up; the $\mathbf j$ of the statement), $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$, horizontal (Notes.pdf, Eq. 2.1) |
| Moving frame (parts d to g) | $S_1 = \{O;\ \mathcal B_1\}$, the frame $OX_1Y_1Z_1$ attached to the curve: $\mathbf i_1$ along $OX_1$ in the plane of the curve, $\mathbf j_1 = \mathbf j_0$ the axis of rotation, $\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ normal to the plane of the curve; it coincides with $S_0$ at $t = 0$ and turns by the angle $\Omega t$ about $\mathbf j_0$ |
| Curve basis | $\{\mathbf e_t, \mathbf n, \mathbf k\}$ at $P$: unit tangent in the sense of growing abscissa, in-plane unit normal $\mathbf n$ (the tangent turned by $+90^\circ$ in the plane), and the normal to the plane ($\mathbf k_0$ for the fixed curve, $\mathbf k_1$ for the turning one) |
| Coordinates | $x$, abscissa of $P$ along $OX$ (fixed curve); $x_1$, abscissa of $P$ along $OX_1$ (turning curve) |
| Shorthand | $s = \sin(x_1/a)$, $c = \cos(x_1/a)$, $D = \sqrt{1 + s^2}$ (the same letters with $x$ for the fixed curve) |
| Constraints | $P$ in the plane of the curve and on the curve: two holonomic, smooth, bilateral constraints (rheonomic in $S_0$ when the curve turns, fixed in $S_1$) |
| Degrees of freedom | 3 minus 2: 1, the abscissa $x(t)$ or $x_1(t)$; the angle $\Omega t$ is prescribed |
| Data | $m$ [kg], $a$ [m], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$], $\Omega$ [rad s$^{-1}$] |
| Initial state | $x(0) = 0$ (or $x_1(0) = 0$), absolute velocity $v_0\,\mathbf i_0$ |
| Unknowns | the abscissa as a function of time; the reaction $\mathbf N = N_n\,\mathbf n + N_b\,\mathbf k$ (normal subspace of a curve, Notes.pdf, Eq. 6.16) |
| Applied force | weight $-mg\,\mathbf j_0$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial, uniform gravity, smooth curve (no tangential reaction), the rotation of the curve imposed from outside (whatever torque it needs is supplied) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p22-curve-plane.svg]]

> [!derivation] Position vector and slope triangle in the plane of the curve
> **Law:** position vector as the sum of its components; chain rule; right triangle of the arc element
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.19; Problems.pdf, p. 10
>
> The plane of the curve is drawn with the horizontal axis to the right and $\mathbf j_0$ up. For the fixed curve the horizontal axis is $OX$ with $\mathbf i_0$; for the turning curve the same drawing holds in $S_1$ with $OX_1$, $\mathbf i_1$ and $x_1$. The position of $P$ is the sum of its two dashed components: the abscissa along the horizontal axis and the height given by the equation of the curve. Moving a distance $dx_1$ along the axis, the height changes by $dy$; in the shaded right triangle the leg adjacent to the tangent angle $\alpha$ is $dx_1$, the opposite leg is $dy$ and the hypotenuse is the arc element $ds$ (Eq. 2.19).
>
> $$\begin{aligned}
> \mathbf r_1^P &= x_1\,\mathbf i_1 + a\left(1 - \cos\frac{x_1}{a}\right)\mathbf j_1 \quad &\text{(abscissa plus height on the curve)} \\
> \frac{d}{dx_1}\cos\frac{x_1}{a} &= -\sin\frac{x_1}{a}\cdot\frac{d}{dx_1}\left(\frac{x_1}{a}\right) = -\frac{1}{a}\sin\frac{x_1}{a} \quad &\text{(chain rule)} \\
> \frac{dy}{dx_1} &= a\cdot\frac{1}{a}\sin\frac{x_1}{a} = s \quad &\text{(derivative of the height; shorthand $s$)} \\
> ds^2 &= dx_1^2 + dy^2 = \left(1 + s^2\right)dx_1^2 \quad &\text{(Pythagoras in the slope triangle)} \\
> ds &= D\,dx_1, \quad \cos\alpha = \frac{dx_1}{ds} = \frac{1}{D}, \quad \sin\alpha = \frac{dy}{ds} = \frac{s}{D} \quad &\text{(adjacent and opposite legs over the hypotenuse)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = x_1\,\mathbf i_1 + a\left(1 - \cos\frac{x_1}{a}\right)\mathbf j_1, \qquad \frac{ds}{dx_1} = D = \sqrt{1 + \sin^2\frac{x_1}{a}}, \qquad \tan\alpha = \sin\frac{x_1}{a}}$$
>
> **Units:** $[x_1] = [a] = [\mathrm{L}]$; $x_1/a$ and the slope dimensionless
> **Meaning:** $x_1$ zero gives the initial point $O$; at the crests, plus and minus $\pi a$, the height is twice $a$. The fixed curve has the same expressions with $x$, $\mathbf i_0$ and $\mathbf j_0$.

> [!derivation] Tangent and normal of the curve: rotation by alpha in its plane
> **Law:** unit tangent along the hypotenuse of the slope triangle; elementary rotation about the normal to the plane and its checks
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20
>
> The plane is seen with $\mathbf i_1$ to the right and $\mathbf j_1$ up, so $\mathbf k_1$, their cross product, points out of the paper (⊙) and a positive rotation about it is counterclockwise. $\mathbf e_t$ is $\mathbf i_1$ turned by $\alpha$: hypotenuse 1, adjacent leg $\cos\alpha$ along $\mathbf i_1$, opposite leg $\sin\alpha$ along $\mathbf j_1$. $\mathbf n$ is $\mathbf j_1$ turned by the same angle: adjacent leg $\cos\alpha$ along $\mathbf j_1$, opposite leg $\sin\alpha$ along minus $\mathbf i_1$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_t &= \cos\alpha\,\mathbf i_1 + \sin\alpha\,\mathbf j_1 = \frac{\mathbf i_1 + s\,\mathbf j_1}{D} \quad &\text{(right triangle of $\mathbf e_t$; Eq. 2.9: $d\mathbf r/ds$)} \\
> \mathbf n &= -\sin\alpha\,\mathbf i_1 + \cos\alpha\,\mathbf j_1 = \frac{-s\,\mathbf i_1 + \mathbf j_1}{D} \quad &\text{(right triangle of $\mathbf n$: opposite leg on $-\mathbf i_1$)} \\
> \det[{}_1R_t] &= (+1)\cdot 1\cdot\left(\cos\alpha\cos\alpha - (-\sin\alpha)\sin\alpha\right) = \frac{1 + s^2}{D^2} = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \mathbf e_t\cdot\mathbf e_t &= \frac{1 + s^2}{D^2} = 1, \quad \mathbf e_t\cdot\mathbf n = \frac{-s + s}{D^2} = 0 \quad &\text{(columns orthonormal: $[{}_1R_t][{}_1R_t]^T = I$)} \\
> \mathbf j_1\cdot\mathbf e_t &= \frac{s}{D}, \quad \mathbf j_1\cdot\mathbf n = \frac{1}{D}, \quad \mathbf i_1\cdot\mathbf e_t = \frac{1}{D}, \quad \mathbf i_1\cdot\mathbf n = -\frac{s}{D} \quad &\text{(projections used below)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = \frac{\mathbf i_1 + s\,\mathbf j_1}{D}, \quad \mathbf n = \frac{-s\,\mathbf i_1 + \mathbf j_1}{D}, \quad [{}_1R_t] = \begin{pmatrix} 1/D & -s/D & 0 \cr s/D & 1/D & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_1R_t] = 1}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** the reaction of the smooth curve lies in the plane spanned by the normal $\mathbf n$ and the normal to the plane; projecting on the tangent removes it.

![[attachments/EM-SOL/p22-top-view.svg]]

> [!derivation] Basis of the turning curve: rotation by Omega t about j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf j_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf k_0$, the cross product of $\mathbf i_0$ and $\mathbf j_0$, points down the page (right-hand rule: fingers from $\mathbf i_0$, to the right, towards $\mathbf j_0$, towards the reader; the thumb goes down the page), so minus $\mathbf k_0$ points up the page. A positive $\Omega$ turns the curve counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ up the page, that is along minus $\mathbf k_0$ (the minus sign). $\mathbf k_1$ is $\mathbf k_0$ (down the page) turned by the same angle: its tip moves towards the right, adjacent leg $\cos\Omega t$ along $\mathbf k_0$, opposite leg $\sin\Omega t$ along plus $\mathbf i_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf i_1$: opposite leg on $-\mathbf k_0$)} \\
> \mathbf j_1 &= \mathbf j_0 \quad &\text{(axis of the rotation)} \\
> \mathbf k_1 &= \sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf k_1$)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \sin\Omega t\left(-\sin\Omega t\right)\right) = 1 \quad &\text{(expansion along the second row, cofactor sign $(-1)^{2+2}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows; row 2 is the unit row of $\mathbf j_0$)} \\
> \mathbf i_1\times\mathbf j_1 &= \cos\Omega t\,\mathbf i_0\times\mathbf j_0 - \sin\Omega t\,\mathbf k_0\times\mathbf j_0 = \cos\Omega t\,\mathbf k_0 + \sin\Omega t\,\mathbf i_0 = \mathbf k_1 \quad &\text{(right-handed; $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & 0 & \sin\Omega t \cr 0 & 1 & 0 \cr -\sin\Omega t & 0 & \cos\Omega t \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Omega t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$
> **Meaning:** it is the matrix of Eq. 1.19 with the angle $\Omega t$; at the start the two frames coincide.

### Kinematics

> [!derivation] Fixed curve: velocity and acceleration
> **Law:** time derivative of the position in $S_0$ with the constant basis $\mathcal B_0$; chain rule and product rule
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7; Notes.pdf, Eq. 2.16
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i_0 + a\left(1 - \cos\frac{x}{a}\right)\mathbf j_0 \quad &\text{(position box with $x$, $\mathbf i_0$, $\mathbf j_0$)} \\
> \frac{d}{dt}\left[a\left(1 - \cos\frac{x}{a}\right)\right] &= a\sin\frac{x}{a}\cdot\frac{\dot x}{a} = \sin\frac{x}{a}\,\dot x \quad &\text{(chain rule through $x(t)$)} \\
> \mathbf v_0^P &= \dot x\,\mathbf i_0 + \sin\frac{x}{a}\,\dot x\,\mathbf j_0 = D\,\dot x\,\mathbf e_t \quad &\text{(Eq. 2.6; $\mathbf e_t$ of the tangent box)} \\
> \frac{d}{dt}\left(\sin\frac{x}{a}\,\dot x\right) &= \frac{1}{a}\cos\frac{x}{a}\,\dot x\cdot\dot x + \sin\frac{x}{a}\,\ddot x \quad &\text{(product rule; chain rule on the sine)} \\
> \mathbf a_0^P &= \ddot x\,\mathbf i_0 + \left(s\,\ddot x + \frac{c}{a}\,\dot x^2\right)\mathbf j_0 \quad &\text{(Eq. 2.7)} \\
> \mathbf a_0^P\cdot\mathbf e_t &= \frac{\ddot x + s^2\ddot x + \frac{sc}{a}\dot x^2}{D} = \frac{\left(1 + s^2\right)\ddot x + \frac{sc}{a}\dot x^2}{D} \quad &\text{(projection on $\mathbf e_t$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i_0 + \sin\frac{x}{a}\,\dot x\,\mathbf j_0, \qquad \mathbf a_0^P\cdot\mathbf e_t = \frac{1}{D}\left[\left(1 + \sin^2\frac{x}{a}\right)\ddot x + \frac{1}{a}\sin\frac{x}{a}\cos\frac{x}{a}\,\dot x^2\right]}$$
>
> **Units:** $[\dot x] = [\mathrm{L\,T^{-1}}]$; $[\ddot x] = [\dot x^2/a] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the speed along the curve is the factor $D$ times the horizontal rate; it is larger than the horizontal rate wherever the curve is inclined.

> [!derivation] Motion of the turning frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9; [Lecture 5, Slide 16]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = \dot\Omega\,\mathbf j_1 = \mathbf 0 \quad &\text{(simple rotation about the fixed $\mathbf j_0 = \mathbf j_1$; $\Omega$ constant)} \\
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf v_0^O = \mathbf 0, \quad \mathbf a_0^O = \mathbf 0 \quad &\text{(origin of $S_1$ at the fixed point $O$)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf i_1 = -\Omega\,\mathbf k_1 \quad &\text{(Eq. 3.3; $\mathbf j_1\times\mathbf i_1 = -\mathbf k_1$)} \\
> \left.\frac{d\mathbf j_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf j_1 = \mathbf 0 \quad &\text{(Eq. 3.4)} \\
> \left.\frac{d\mathbf k_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf k_1 = \Omega\,\mathbf i_1 \quad &\text{(Eq. 3.5; $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$)} \\
> \frac{d}{dt}\left(\cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0\right) &= -\Omega\sin\Omega t\,\mathbf i_0 - \Omega\cos\Omega t\,\mathbf k_0 = -\Omega\,\mathbf k_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf i_1}$$
>
> **Units:** $[\Omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from above the plane of the curve turns counterclockwise; seen from $S_1$ its unit vectors are constant.

> [!derivation] Turning curve: relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$ and $\mathbf j_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24
>
> $$\begin{aligned}
> \mathbf v_1^P &= \left.\frac{d\mathbf r_1^P}{dt}\right|_1 = \dot x_1\,\mathbf i_1 + \sin\frac{x_1}{a}\,\dot x_1\,\mathbf j_1 \quad &\text{(chain rule on the height, as for the fixed curve)} \\
> \mathbf a_1^P &= \ddot x_1\,\mathbf i_1 + \left(s\,\ddot x_1 + \frac{c}{a}\,\dot x_1^2\right)\mathbf j_1 \quad &\text{(product rule on $\sin(x_1/a)\,\dot x_1$)} \\
> \mathbf a_1^P\cdot\mathbf e_t &= \frac{\left(1 + s^2\right)\ddot x_1 + \frac{sc}{a}\dot x_1^2}{D} \quad &\text{(projection on $\mathbf e_t$)} \\
> \mathbf a_1^P\cdot\mathbf n &= \frac{-s\,\ddot x_1 + s\,\ddot x_1 + \frac{c}{a}\dot x_1^2}{D} = \frac{c\,\dot x_1^2}{aD} \quad &\text{(projection on $\mathbf n$; the $\ddot x_1$ terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = \dot x_1\,\mathbf i_1 + \sin\frac{x_1}{a}\,\dot x_1\,\mathbf j_1, \qquad \mathbf a_1^P = \ddot x_1\,\mathbf i_1 + \left(\sin\frac{x_1}{a}\,\ddot x_1 + \frac{\dot x_1^2}{a}\cos\frac{x_1}{a}\right)\mathbf j_1}$$
>
> **Units:** $[\dot x_1] = [\mathrm{L\,T^{-1}}]$; $[\ddot x_1] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in $S_1$ the curve is at rest, so the relative motion has the kinematics of the fixed curve, with no component along $\mathbf k_1$.

> [!derivation] Absolute velocity and acceleration: transport, Coriolis and centripetal terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule and derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write $y_1$ for the height $a(1 - \cos(x_1/a))$, so that the position is $x_1\,\mathbf i_1 + y_1\,\mathbf j_1$.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + x_1\left.\frac{d\mathbf i_1}{dt}\right|_0 + y_1\left.\frac{d\mathbf j_1}{dt}\right|_0 \quad &\text{(product rule on each term)} \\
> &= \underbrace{\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1}_{\mathbf v_1^P}\ \underbrace{-\ \Omega x_1\,\mathbf k_1}_{\boldsymbol\omega_{10}\times\mathbf r_1^P} \quad &\text{(derivatives of the unit vectors; $\Omega\,\mathbf j_1\times(x_1\mathbf i_1 + y_1\mathbf j_1) = -\Omega x_1\,\mathbf k_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 + \dot x_1\left(-\Omega\,\mathbf k_1\right) = \mathbf a_1^P - \Omega\dot x_1\,\mathbf k_1 \quad &\text{(product rule; the turning of $\mathbf i_1$ inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left(-\Omega x_1\,\mathbf k_1\right) &= -\Omega\dot x_1\,\mathbf k_1 - \Omega x_1\,\Omega\,\mathbf i_1 \quad &\text{(product rule; $\Omega$ constant; derivative of $\mathbf k_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\Omega\,\mathbf j_1\times\left(\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1\right) = -2\Omega\dot x_1\,\mathbf k_1 \quad &\text{(the two $\mathbf k_1$ terms above)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf j_1\times\left(-\Omega x_1\,\mathbf k_1\right) = -\Omega^2x_1\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \mathbf v_1^P - \Omega x_1\,\mathbf k_1, \qquad \mathbf a_0^P = \mathbf a_1^P - 2\Omega\dot x_1\,\mathbf k_1 - \Omega^2x_1\,\mathbf i_1}$$
>
> **Units:** $[\Omega x_1] = [\mathrm{L\,T^{-1}}]$; $[\Omega\dot x_1] = [\Omega^2x_1] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** one half of the Coriolis term comes from the turning of $\mathbf i_1$ inside the relative velocity, the other from the change of the distance to the axis inside the transport velocity; the centripetal term points horizontally towards the axis. With $O$ fixed and $\Omega$ constant the origin and Euler terms of Eq. 3.27 are absent.

### Forces and Equations of Motion

The free-body diagram of $P$ in $S_1$ shows, in the plane of the curve, the weight, the in-plane reaction along $\mathbf n$ and the centrifugal force (horizontal, away from the axis); normal to the plane, the reaction along $\mathbf k_1$ and the Coriolis force. The inertia force of the origin and the Euler force vanish ($O$ fixed, $\Omega$ constant). For the fixed curve only the weight and the reaction act.

![[attachments/EM-SOL/p22-fbd.svg]]

> [!derivation] Fixed curve: equation of motion along the tangent
> **Law:** Newton's second law projected on the tangent of a smooth curve
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.16; Notes.pdf, Eq. 6.17
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf j_0 + N_n\,\mathbf n + N_b\,\mathbf k_0 \quad &\text{(Eq. 4.4; smooth reaction of Eq. 6.16)} \\
> m\,\mathbf a_0^P\cdot\mathbf e_t &= -mg\,\mathbf j_0\cdot\mathbf e_t = -\frac{mg\,s}{D} \quad &\text{($\mathbf n\cdot\mathbf e_t$ and $\mathbf k_0\cdot\mathbf e_t$ zero)} \\
> \frac{m}{D}\left[\left(1 + s^2\right)\ddot x + \frac{sc}{a}\dot x^2\right] &= -\frac{mg\,s}{D} \quad &\text{(projection of the kinematics box)} \\
> \left(1 + s^2\right)\ddot x + \frac{sc}{a}\dot x^2 + g\,s &= 0 \quad &\text{(multiplied by $D/m$; terms collected on one side)}
> \end{aligned}$$
>
> $$\boxed{\left(1 + \sin^2\frac{x}{a}\right)\ddot x + \frac{1}{a}\sin\frac{x}{a}\cos\frac{x}{a}\,\dot x^2 + g\sin\frac{x}{a} = 0}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** one equation for the one unknown function $x(t)$; the other two projections would give the reaction, which parts (a) to (c) do not ask for.

#### (d) Inertia forces in the moving frame

> [!derivation] Inertia forces on the particle in the turning frame
> **Law:** inertia forces of a non-inertial frame, each vector product expanded
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = -m\left(-\Omega^2x_1\,\mathbf i_1\right) = m\Omega^2x_1\,\mathbf i_1 \quad &\text{(centripetal term of the composition box times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = -m\left(-2\Omega\dot x_1\,\mathbf k_1\right) = 2m\Omega\dot x_1\,\mathbf k_1 \quad &\text{(Coriolis term of the composition box times $-m$)} \\
> \mathbf F_C\cdot\mathbf e_t &= \frac{m\Omega^2x_1}{D}, \quad \mathbf F_C\cdot\mathbf n = -\frac{m\Omega^2x_1 s}{D}, \quad \mathbf F_{COR}\cdot\mathbf e_t = \mathbf F_{COR}\cdot\mathbf n = 0 \quad &\text{(projections of the tangent box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_i = \mathbf F_C + \mathbf F_{COR} = m\Omega^2x_1\,\mathbf i_1 + 2m\Omega\dot x_1\,\mathbf k_1}$$
>
> **Units:** $[m\Omega^2x_1] = [m\Omega\dot x_1] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the centrifugal force is horizontal and points away from the axis on both sides (it changes sign with $x_1$); the Coriolis force is normal to the plane of the curve, along plus $\mathbf k_1$ while $P$ moves towards growing $x_1$.

> [!derivation] Newton's second law in the turning frame, projected on the curve basis
> **Law:** Newton's second law in a non-inertial frame with the inertia forces; reaction of a smooth curve
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.16; Notes.pdf, Eq. 6.19; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> m\,\mathbf a_1^P &= -mg\,\mathbf j_1 + N_n\,\mathbf n + N_b\,\mathbf k_1 + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63)} \\
> \mathbf e_t:\ \frac{m}{D}\left[\left(1 + s^2\right)\ddot x_1 + \frac{sc}{a}\dot x_1^2\right] &= -\frac{mg\,s}{D} + \frac{m\Omega^2x_1}{D} \quad &\text{(no reaction and no Coriolis force along the tangent)} \\
> \mathbf n:\ \frac{mc\,\dot x_1^2}{aD} &= -\frac{mg}{D} + N_n - \frac{m\Omega^2x_1 s}{D} \quad &\text{(in the plane, across the curve)} \\
> \mathbf k_1:\ 0 &= N_b + 2m\Omega\dot x_1 \quad &\text{(no relative motion normal to the plane)}
> \end{aligned}$$
>
> $$\boxed{\left(1 + s^2\right)\ddot x_1 + \frac{sc}{a}\dot x_1^2 + g\,s - \Omega^2x_1 = 0, \qquad N_n = \frac{m}{D}\left(g + \Omega^2x_1 s + \frac{c}{a}\dot x_1^2\right), \qquad N_b = -2m\Omega\dot x_1}$$
>
> **Units:** $[g] = [\Omega^2x_1] = [\dot x_1^2/a] = [\mathrm{L\,T^{-2}}]$; $[N_b] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations for the three unknowns $x_1$, $N_n$ and $N_b$. The reaction normal to the plane balances the Coriolis force alone.

### Answers and Checks

#### (a) Reduction to integrals, fixed curve

> [!derivation] Energy integral of the fixed curve
> **Law:** the equation of motion multiplied by the rate is an exact derivative (chain rule); Barrow's rule between 0 and $t$
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.31; Notes.pdf, Sec. 6.5
>
> $$\begin{aligned}
> m\left(1 + s^2\right)\dot x\ddot x + \frac{m}{a}sc\,\dot x^3 + mg\,s\,\dot x &= 0 \quad &\text{(equation of motion times $m\dot x$)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(1 + s^2\right)\dot x^2\right] &= m\left(1 + s^2\right)\dot x\ddot x + \tfrac12 m\cdot 2s\,\frac{c}{a}\dot x\cdot\dot x^2 \quad &\text{(product rule; chain rule: $\tfrac{d}{dt}s^2 = 2s\,\tfrac{c}{a}\,\dot x$)} \\
> \frac{d}{dt}\left[mga\left(1 - c\right)\right] &= mga\,\frac{s}{a}\,\dot x = mg\,s\,\dot x \quad &\text{(chain rule: $\tfrac{d}{dt}c = -\tfrac{s}{a}\,\dot x$)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(1 + s^2\right)\dot x^2 + mga\left(1 - c\right)\right] &= 0 \quad &\text{(the first row is this sum)} \\
> \left[\tfrac12 m\left(1 + s^2\right)\dot x^2 + mga\left(1 - c\right)\right]_0^t &= 0 \quad &\text{(Barrow's rule between 0 and $t$)} \\
> \tfrac12 m\left(1 + 0\right)v_0^2 + mga\left(1 - 1\right) &= \tfrac12 mv_0^2 \quad &\text{(value at $t = 0$: $x = 0$, $\dot x(0) = v_0$, from $\mathbf v_0^P(0) = \dot x(0)\,\mathbf i_0 = v_0\,\mathbf i_0$)} \\
> \left(1 + s^2\right)\dot x^2 &= v_0^2 - 2ga\left(1 - c\right) \quad &\text{(multiplied by $2/m$)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12 m\left(1 + \sin^2\frac{x}{a}\right)\dot x^2 + mga\left(1 - \cos\frac{x}{a}\right) = \tfrac12 mv_0^2}$$
>
> **Units:** $[mv_0^2] = [mga] = [\mathrm{M\,L^2\,T^{-2}}]$, energies
> **Meaning:** the kinetic energy plus the potential energy of the weight is constant: the smooth reaction is normal to the velocity of a particle on a fixed curve and does no work.

> [!derivation] Quadrature of the fixed curve
> **Law:** separation of variables; the sign of the rate fixed by the initial condition
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.44; Problems.pdf, p. 10
>
> The rate starts positive ($\dot x(0) = v_0$) and keeps its sign until it first vanishes, at a turning point where the right-hand side is zero.
>
> $$\begin{aligned}
> \dot x &= +\sqrt{\frac{v_0^2 - 2ga\left(1 - \cos\left(x/a\right)\right)}{1 + \sin^2\left(x/a\right)}} \quad &\text{(energy integral solved; positive root)} \\
> dt &= \sqrt{\frac{1 + \sin^2\left(x/a\right)}{v_0^2 - 2ga\left(1 - \cos\left(x/a\right)\right)}}\,dx \quad &\text{(variables separated)} \\
> \int_0^t dt' &= \left[t'\right]_0^t = t \quad &\text{(antiderivative $t'$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{t = \int_0^{x}\sqrt{\frac{1 + \sin^2(\xi/a)}{v_0^2 - 2ga\left(1 - \cos(\xi/a)\right)}}\;d\xi \quad \text{(until the first turning point; then the sign of the root changes)}}$$
>
> **Units:** the integrand is $[\mathrm{L\,T^{-1}}]^{-1}$, times $[d\xi] = [\mathrm{L}]$: a time
> **Meaning:** the motion is reduced to one integral; the region allowed to the particle is where the radicand is not negative.

#### (b) Extreme abscissas of the motion

> [!derivation] Turning points
> **Law:** the rate vanishes where the kinetic energy is zero; allowed region of the energy integral
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \left(1 + s^2\right)\dot x^2 &= ga - 2ga\left(1 - \cos\frac{x}{a}\right) = ga\left(2\cos\frac{x}{a} - 1\right) \quad &\text{(energy integral with $v_0^2 = ga$; terms collected)} \\
> \dot x^2 \ge 0 &\iff \cos\frac{x}{a} \ge \frac12 \iff -\frac{\pi}{3} \le \frac{x}{a} \le \frac{\pi}{3} \quad &\text{(the factor $1 + s^2$ is positive; $x/a$ between $-\pi$ and $\pi$)} \\
> \ddot x\left(\pm\frac{\pi a}{3}\right) &= -\frac{g\sin(\pm\pi/3)}{1 + \sin^2(\pi/3)} = \mp\frac{g\sqrt3/2}{7/4} = \mp\frac{2\sqrt3}{7}\,g \quad &\text{(equation of motion with $\dot x = 0$; $\sin^2(\pi/3) = 3/4$)}
> \end{aligned}$$
>
> $$\boxed{x_{\min} = -\frac{\pi a}{3}, \qquad x_{\max} = \frac{\pi a}{3}}$$
>
> **Units:** $[x] = [a] = [\mathrm{L}]$
> **Meaning:** at each end of the allowed interval the acceleration points back towards $O$, so the particle turns there: it oscillates between the two points at a height of half of $a$, symmetric about $O$, and never stays at an end.

#### (c) Minimum initial speed to reach the crest

> [!derivation] Speed needed to reach x equal to pi a
> **Law:** allowed region of the energy integral; behaviour of the quadrature near a maximum of the potential
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.44; Problems.pdf, p. 10
>
> To reach the crest the radicand must not be negative on the whole way from 0 to $\pi a$; it decreases with $x$ there, because $1 - \cos(x/a)$ grows, so the condition is its value at the crest. At the limiting speed write $u$ for the distance $\pi a - x$ still to go; the half-angle identity is $1 + \cos\beta = 2\cos^2(\beta/2)$.
>
> $$\begin{aligned}
> v_0^2 - 2ga\left(1 - \cos\pi\right) &= v_0^2 - 4ga \ge 0 \quad &\text{(radicand at $x = \pi a$; $\cos\pi = -1$)} \\
> v_0 &\ge 2\sqrt{ga} \quad &\text{(positive root, $v_0 \gt 0$)} \\
> v_0^2 - 2ga\left(1 - \cos\frac{x}{a}\right) &= 2ga\left(1 + \cos\frac{x}{a}\right) = 4ga\cos^2\frac{x}{2a} \quad &\text{(case $v_0^2 = 4ga$; half-angle identity)} \\
> \cos\frac{x}{2a} &= \cos\left(\frac{\pi}{2} - \frac{u}{2a}\right) = \sin\frac{u}{2a} \simeq \frac{u}{2a} \quad &\text{(difference formula; small $u$)} \\
> \sqrt{\frac{1 + \sin^2(x/a)}{4ga\cos^2(x/2a)}} &\simeq \sqrt{\frac{1}{4ga}}\cdot\frac{2a}{u} = \sqrt{\frac{a}{g}}\,\frac{1}{u} \quad &\text{(integrand of the quadrature near the crest; $\sin(x/a) \simeq 0$)} \\
> \int_{u}^{u_1}\sqrt{\frac{a}{g}}\,\frac{du'}{u'} &= \sqrt{\frac{a}{g}}\left[\ln u'\right]_{u}^{u_1} = \sqrt{\frac{a}{g}}\,\ln\frac{u_1}{u} \to \infty \ \ (u \to 0) \quad &\text{(time from a point at $u_1$ to a point at $u$: antiderivative $\ln u'$, Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{v_{0,\min} = 2\sqrt{ga}: \ \text{for } v_0 \gt 2\sqrt{ga} \text{ the crest is reached in a finite time; at } v_0 = 2\sqrt{ga} \text{ only as } t \to \infty}$$
>
> **Units:** $[\sqrt{ga}] = [\mathrm{L\,T^{-1}}]$; $[\sqrt{a/g}] = [\mathrm{T}]$
> **Meaning:** the initial kinetic energy must pay for the rise to the crest, twice $a$ above $O$. At exactly the limiting speed the force on the particle vanishes at the crest as well as its speed, and the time to get there diverges logarithmically: $2\sqrt{ga}$ is the lower bound of the speeds that reach it.

#### (e) Quadratures and reaction force, turning curve

> [!derivation] Initial relative velocity
> **Law:** composition of velocities at the initial instant
> **Source:** Notes.pdf, Eq. 3.20; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \mathbf v_0^P(0) &= \mathbf v_1^P(0) - \Omega x_1(0)\,\mathbf k_1 = \dot x_1(0)\,\mathbf i_1 + \sin 0\cdot\dot x_1(0)\,\mathbf j_1 - 0 \quad &\text{(velocity box; $x_1(0) = 0$)} \\
> &= \dot x_1(0)\,\mathbf i_0 \quad &\text{($\mathbf i_1 = \mathbf i_0$ at $t = 0$)} \\
> \dot x_1(0)\,\mathbf i_0 &= v_0\,\mathbf i_0 \quad &\text{(initial condition of the statement)}
> \end{aligned}$$
>
> $$\boxed{x_1(0) = 0, \qquad \dot x_1(0) = v_0}$$
>
> **Units:** $[v_0] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** at the axis the transport velocity is zero, so the relative and the absolute initial velocities coincide.

> [!derivation] Energy integral in the turning frame and quadrature
> **Law:** the tangent equation multiplied by the rate is an exact derivative (chain rule); Barrow's rule; separation of variables
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> m\left(1 + s^2\right)\dot x_1\ddot x_1 + \frac{m}{a}sc\,\dot x_1^3 + mg\,s\,\dot x_1 - m\Omega^2x_1\dot x_1 &= 0 \quad &\text{(tangent equation times $m\dot x_1$)} \\
> \frac{d}{dt}\left(-\tfrac12 m\Omega^2x_1^2\right) &= -m\Omega^2x_1\dot x_1 \quad &\text{(chain rule; $\Omega$ constant)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(1 + s^2\right)\dot x_1^2 + mga\left(1 - c\right) - \tfrac12 m\Omega^2x_1^2\right] &= 0 \quad &\text{(the first two terms as for the fixed curve)} \\
> \left[\tfrac12 m\left(1 + s^2\right)\dot x_1^2 + mga\left(1 - c\right) - \tfrac12 m\Omega^2x_1^2\right]_0^t &= 0 \quad &\text{(Barrow's rule between 0 and $t$)} \\
> \tfrac12 m\left(1 + s^2\right)\dot x_1^2 + mga\left(1 - c\right) - \tfrac12 m\Omega^2x_1^2 &= \tfrac12 mv_0^2 \quad &\text{(value at $t = 0$: $x_1 = 0$, $\dot x_1 = v_0$)} \\
> \dot x_1^2 &= \frac{v_0^2 - 2ga\left(1 - c\right) + \Omega^2x_1^2}{1 + s^2} \quad &\text{(multiplied by $2/m$, divided by $1 + s^2$)} \\
> dt &= \sqrt{\frac{1 + s^2}{v_0^2 - 2ga\left(1 - c\right) + \Omega^2x_1^2}}\,dx_1 \quad &\text{(positive root, $\dot x_1(0) = v_0 \gt 0$; variables separated)}
> \end{aligned}$$
>
> $$\boxed{t = \int_0^{x_1}\sqrt{\frac{1 + \sin^2(\xi/a)}{v_0^2 - 2ga\left(1 - \cos(\xi/a)\right) + \Omega^2\xi^2}}\;d\xi \quad \text{(until the first turning point)}}$$
>
> **Units:** $[\Omega^2\xi^2] = [v_0^2] = [ga] = [\mathrm{L^2\,T^{-2}}]$; the integral is a time
> **Meaning:** compared with the fixed curve the radicand gains the centrifugal term, which grows with the distance to the axis and helps the particle climb.

> [!derivation] Reaction force on the turning curve
> **Law:** normal equations of the turning frame with the squared rate eliminated through the energy integral
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.16; Notes.pdf, Eq. 6.19
>
> $$\begin{aligned}
> N_n &= \frac{m}{D}\left(g + \Omega^2x_1 s + \frac{c}{a}\dot x_1^2\right) \quad &\text{(equation along $\mathbf n$)} \\
> &= \frac{m}{D}\left[g + \Omega^2x_1 s + \frac{c\left(v_0^2 - 2ga(1 - c) + \Omega^2x_1^2\right)}{a\left(1 + s^2\right)}\right] \quad &\text{(squared rate of the energy integral)} \\
> N_b &= -2m\Omega\dot x_1 = \mp 2m\Omega\sqrt{\frac{v_0^2 - 2ga(1 - c) + \Omega^2x_1^2}{1 + s^2}} \quad &\text{(equation along $\mathbf k_1$; upper sign while $x_1$ grows)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = \frac{m}{D}\left[g + \Omega^2x_1\sin\frac{x_1}{a} + \frac{\dot x_1^2}{a}\cos\frac{x_1}{a}\right]\mathbf n - 2m\Omega\dot x_1\,\mathbf k_1, \quad \dot x_1^2 = \frac{v_0^2 - 2ga\left(1 - \cos\frac{x_1}{a}\right) + \Omega^2x_1^2}{1 + \sin^2\frac{x_1}{a}}}$$
>
> **Units:** $[mg] = [m\Omega^2x_1] = [m\dot x_1^2/a] = [m\Omega\dot x_1] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the in-plane part carries the weight, the centrifugal push across the curve and the centripetal need of the curved path; the part normal to the plane points along minus $\mathbf k_1$ while $x_1$ grows, against the Coriolis force.

#### (f) Equilibrium positions in the turning frame

> [!derivation] Transcendental equation of the relative equilibria
> **Law:** relative rest in the tangent equation; monotony of the function sine over its argument
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.63
>
> Write $u$ for $x_1/a$ and $\lambda$ for the dimensionless number $\Omega^2a/g$. On $0 \lt u \le \pi$ the function $\sin u/u$ decreases from 1 (its limit at 0) to 0; its derivative is $h(u)/u^2$ with $h(u) = u\cos u - \sin u$, and $h$ starts at 0 with the derivative $-u\sin u$, negative there.
>
> $$\begin{aligned}
> \dot x_1 = 0,\ \ddot x_1 = 0:\quad g\sin\frac{x_1}{a} - \Omega^2x_1 &= 0 \quad &\text{(tangent equation at relative rest)} \\
> \sin u &= \lambda u \quad &\text{(divided by $g$; $u$ and $\lambda$ substituted)} \\
> u = 0 &\ \text{always}; \quad \frac{\sin u}{u} = \lambda \ \text{for } u \ne 0 \quad &\text{(the two families)} \\
> \frac{d}{du}\left(\frac{\sin u}{u}\right) &= \frac{u\cos u - \sin u}{u^2}, \quad h(u) = h(0) + \int_0^u\left(-u'\sin u'\right)du' \lt 0 \quad &\text{(quotient rule; $h' = \cos u - u\sin u - \cos u$)}
> \end{aligned}$$
>
> $$\boxed{g\sin\frac{x_1}{a} = \Omega^2x_1: \ \ x_1 = 0 \text{ for every } \Omega; \ \text{a symmetric pair } \pm x_1^* \ \text{with } 0 \lt x_1^* \lt \pi a \text{ exactly when } \Omega^2a \lt g}$$
>
> **Units:** $[g] = [\Omega^2x_1] = [\mathrm{L\,T^{-2}}]$; $\lambda$ dimensionless
> **Meaning:** at an off-axis equilibrium the tangential pull of the weight towards the bottom balances the tangential push of the centrifugal force; with a fast spin no off-axis balance exists inside the range of the curve.

#### (g) Variable spin rate

> [!derivation] Energy in the turning frame when Omega depends on time
> **Law:** inertia forces with a variable angular velocity; power of each force on the relative velocity; product rule
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.62; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]
>
> With $\Omega(t)$ the Euler force appears. It is normal to the plane of the curve, so it does no work in $S_1$ and drops out of the tangent equation, which keeps its form with $\Omega(t)$; it only changes the reaction along $\mathbf k_1$. The centrifugal force, however, no longer derives from a potential that depends on the position only.
>
> $$\begin{aligned}
> \boldsymbol\alpha_{10} &= \dot\Omega\,\mathbf j_1, \quad \mathbf F_E = -m\dot\Omega\,\mathbf j_1\times\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) = m\dot\Omega x_1\,\mathbf k_1 \quad &\text{(Eq. 3.9 and Eq. 4.62; $\mathbf j_1\times\mathbf i_1 = -\mathbf k_1$)} \\
> \mathbf F_E\cdot\mathbf v_1^P &= m\dot\Omega x_1\,\mathbf k_1\cdot\left(\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1\right) = 0 \quad &\text{(normal to the plane)} \\
> \mathbf k_1:\ 0 &= N_b + 2m\Omega\dot x_1 + m\dot\Omega x_1 \quad &\text{(the reaction balances Coriolis and Euler forces)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(1 + s^2\right)\dot x_1^2 + mga\left(1 - c\right)\right] &= m\Omega^2x_1\dot x_1 \quad &\text{(tangent equation with $\Omega(t)$ times $m\dot x_1$)} \\
> \frac{d}{dt}\left(\tfrac12 m\Omega^2x_1^2\right) &= m\Omega\dot\Omega x_1^2 + m\Omega^2x_1\dot x_1 \quad &\text{(product rule; chain rule on both factors)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(1 + s^2\right)\dot x_1^2 + mga\left(1 - c\right) - \tfrac12 m\Omega^2x_1^2\right] &= -m\Omega\dot\Omega x_1^2 \quad &\text{(difference of the last two rows)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_1^P}{dt} = -m\Omega\dot\Omega x_1^2 \ne 0: \ \text{with } \Omega(t) \text{ the energy equation is no longer a first integral}}$$
>
> **Units:** $[m\Omega\dot\Omega x_1^2] = [\mathrm{M}][\mathrm{T^{-1}}][\mathrm{T^{-2}}][\mathrm{L^2}] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** no, it cannot be used in the same way: the balance of the last row still holds, but its right-hand side depends on the unknown position, so it does not reduce the problem to a quadrature. With constant $\Omega$ the right-hand side vanishes and part (e) is recovered.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Integrals, fixed curve | $\frac12 m(1 + \sin^2\frac{x}{a})\dot x^2 + mga(1 - \cos\frac{x}{a}) = \frac12 mv_0^2$; $t = \int_0^x\sqrt{(1 + \sin^2(\xi/a))/(v_0^2 - 2ga(1 - \cos(\xi/a)))}\,d\xi$ |
| (b) Extreme abscissas, $v_0 = \sqrt{ga}$ | $x_{\min} = -\pi a/3$, $x_{\max} = \pi a/3$ (oscillation between them) |
| (c) Minimum speed to reach $x = \pi a$ | $v_0 = 2\sqrt{ga}$ (lower bound: reached in a finite time for any larger speed, asymptotically at that speed) |
| (d) Moving frame and inertia force | $S_1$: $\mathbf i_1$ in the plane of the curve, $\mathbf j_1 = \mathbf j_0$ the axis, $\mathbf k_1$ normal to the plane; $\mathbf F_i = m\Omega^2x_1\,\mathbf i_1 + 2m\Omega\dot x_1\,\mathbf k_1$ |
| (e) Quadrature, turning curve | $t = \int_0^{x_1}\sqrt{(1 + \sin^2(\xi/a))/(v_0^2 - 2ga(1 - \cos(\xi/a)) + \Omega^2\xi^2)}\,d\xi$ |
| (e) Reaction | $\mathbf N = \frac{m}{D}\left(g + \Omega^2x_1\sin\frac{x_1}{a} + \frac{\dot x_1^2}{a}\cos\frac{x_1}{a}\right)\mathbf n - 2m\Omega\dot x_1\,\mathbf k_1$, with $\mathbf n = (-\sin\frac{x_1}{a}\,\mathbf i_1 + \mathbf j_1)/D$ and $\dot x_1^2$ from the energy integral |
| (f) Equilibria | $g\sin(x_1/a) = \Omega^2x_1$: $x_1 = 0$ always, and a pair $\pm x_1^*$ only if $\Omega^2a \lt g$ |
| (g) Variable $\Omega$ | no: $dE_1^P/dt = -m\Omega\dot\Omega x_1^2 \ne 0$; the Euler force $m\dot\Omega x_1\,\mathbf k_1$ does no work, but the centrifugal force has no time-independent potential |

**Check against the official key:** Problems.pdf, p. 73 lists item 22 with no answer, so there is no key to compare with. Independent checks: the reaction normal to the plane follows again from the angular momentum about the vertical axis in $S_0$ (box below), and the limiting cases close the results.

> [!derivation] Independent check: angular momentum about the vertical axis
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$ the position has the components $(x_1, y_1, 0)$ and the absolute velocity $(\dot x_1, \dot y_1, -\Omega x_1)$ (velocity box). The component along $\mathbf j_1$ of a vector product is the first component of the second factor times the third of the first, minus the third of the second times the first of the first.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf j_1 &= m\left(\mathbf r_0^P\times\mathbf v_0^P\right)\cdot\mathbf j_1 = m\left(0\cdot\dot x_1 - x_1\left(-\Omega x_1\right)\right) = m\Omega x_1^2 \quad &\text{(Eq. 4.48)} \\
> \mathbf M_O\cdot\mathbf j_1 &= \left(\mathbf r_0^P\times N_b\,\mathbf k_1\right)\cdot\mathbf j_1 = 0\cdot 0 - x_1N_b = -x_1N_b \quad &\text{(weight along $\mathbf j_1$ and $N_n\,\mathbf n$ in the plane: no axial moment)} \\
> \frac{d}{dt}\left(m\Omega x_1^2\right) &= 2m\Omega x_1\dot x_1 \quad &\text{(chain rule; $\mathbf j_1$ fixed)} \\
> -x_1N_b &= 2m\Omega x_1\dot x_1 \quad &\text{(Eq. 4.53, axial component)}
> \end{aligned}$$
>
> $$\boxed{N_b = -2m\Omega\dot x_1 \quad (x_1 \ne 0)}$$
>
> **Units:** $[H] = [\mathrm{M\,L^2\,T^{-1}}]$; $[x_1N_b] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** to keep turning at the rate $\Omega$ while its distance to the axis changes, the particle needs an axial moment that only the normal reaction can give: the same result as the Coriolis balance in $S_1$.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega \to 0:\quad t &\to \int_0^{x}\sqrt{\frac{1 + \sin^2(\xi/a)}{v_0^2 - 2ga\left(1 - \cos(\xi/a)\right)}}\,d\xi, \quad N_b \to 0 \quad &\text{(the quadrature of part (a))} \\
> \Omega \to 0:\quad g\sin\frac{x_1}{a} &= 0 \Rightarrow x_1 = 0 \ \text{inside the open range} \quad &\text{(only the bottom; the crests are ends of the curve)} \\
> |x_1| \ll a:\quad \left(1 + s^2\right)\ddot x_1 + \frac{sc}{a}\dot x_1^2 + g\,s - \Omega^2x_1 &\simeq \ddot x_1 + \left(\frac{g}{a} - \Omega^2\right)x_1 \quad &\text{(first order in $x_1$ and its rates; $s \simeq x_1/a$)}
> \end{aligned}$$
>
> $$\boxed{\Omega \to 0: \text{ part (a) recovered}; \qquad |x_1| \ll a: \ \ddot x_1 + \left(\frac{g}{a} - \Omega^2\right)x_1 = 0}$$
>
> **Units:** $[g/a] = [\Omega^2] = [\mathrm{T^{-2}}]$
> **Meaning:** near the bottom the particle oscillates when the spin rate is below the square root of g over a, and drifts away from the bottom when it is above, the same threshold at which the off-axis equilibria of part (f) disappear.

---

## Problem 25: Ijon Tichy's Space Walk

### Reference Frames, Bases and Coordinates

A spacecraft $S$ moves on a conic of semi-latus rectum $p$ and eccentricity $e$ about the body $F$, with the true anomaly $\nu(t)$ a known function of time; the astronaut $P$, of mass $m$, is tied to it by a massless cord of length $L$ that stays taut, and the frame $Sx_1y_1$ of the figure moves with the spacecraft (Problems.pdf, p. 13). The statement asks for the acceleration and the unit tangent of the spacecraft, the relative velocity and acceleration of the astronaut, the inertia forces in $Sx_1y_1$, and, with equal gravity on both bodies, the differential equation of the cord angle and the tension. The relative kinematics follows Notes.pdf, Sec. 3.2, the inertia forces Notes.pdf, Sec. 4.9, and the gravity of $F$ Notes.pdf, Eq. 8.1.

| Item | Definition |
| :--- | :--- |
| Orbit of $S$ | $r = p/(1 + e\cos\nu)$, with $r$ the distance $FS$ and $\nu(t)$ known; $1 + e\cos\nu \gt 0$ on the orbit, since $r$ and $p$ are positive |
| Fixed (inertial) frame | $S_0 = \{F;\ \mathcal B_0\}$, the frame $Fxy$: $\mathbf i_0$ along $Fx$, $\mathbf j_0$ along $Fy$, $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ normal to the orbital plane (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{S;\ \mathcal B_1\}$, the frame $Sx_1y_1$: $\mathbf i_1$ along $FS$, pointing away from $F$; $\mathbf k_1 = \mathbf k_0$; $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$, in the sense of growing $\nu$ (read from the figure: $Sy_1$ is $Sx_1$ turned by a quarter turn counterclockwise) |
| Cord basis | $\mathcal B_2 = \{\mathbf e_c, \mathbf e_\theta, \mathbf k_1\}$: $\mathbf e_c$ from $S$ to $P$, $\mathbf e_\theta$ normal to the cord in the plane, in the sense of growing $\theta$ |
| Coordinate | $\theta$, the angle from $Sx_1$ to the cord $SP$, positive counterclockwise (from $\mathbf i_1$ towards $\mathbf j_1$, read from the figure) |
| Constraints | $P$ in the orbital plane at the distance $L$ from $S$ (taut cord) |
| Degrees of freedom | 2 minus 1: 1, the angle $\theta(t)$; the motion of $S$ is prescribed |
| Data | $p$ [m], $e$ [1], $\nu(t)$ [rad], $L$ [m], $m$ [kg]; $\mu_F$ [m$^3$ s$^{-2}$], the gravitational parameter of $F$ (Notes.pdf, Eq. 8.1), needed for the gravity of parts (e) and (f) |
| Unknowns | $\theta(t)$ and the tension $T(t) \ge 0$ of the cord, which pulls $P$ towards $S$ |
| Applied forces | the cord, $-T\,\mathbf e_c$; the gravity of $F$ on the astronaut, $m\,\mathbf g_P$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; planar motion in the orbital plane; the astronaut does not perturb $S$; from part (e) on, $\mathbf g_P$ equal to the gravitational acceleration $\mathbf g_S$ at $S$ |
| Readings | $\dot\nu \gt 0$ (the spacecraft moves towards growing $\nu$; with $\dot\nu \lt 0$ the unit tangent of part (b) changes sign). The spacecraft is in free flight about $F$, as the conic orbit of Notes.pdf, Eq. 8.14 implies; parts (e) and (f) are given both in general and under this reading |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p25-orbit.svg]]

> [!derivation] Basis of the moving frame: rotation by nu about k0
> **Law:** right triangle of the radius $FS$; elementary rotation about the third axis and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 8.2; Problems.pdf, p. 13
>
> The orbital plane is seen from the side of $\mathbf k_0$, which points out of the paper (⊙) because it is the cross product of $\mathbf i_0$ (to the right) and $\mathbf j_0$ (up): a positive rotation about $\mathbf k_0$ is counterclockwise. $\nu$ is measured at $F$ from $Fx$ counterclockwise, so it is already the standard polar angle of $S$. In the shaded right triangle (right angle at the foot of the perpendicular from $S$ to $Fx$) the hypotenuse is $r$, the leg adjacent to $\nu$ is $r\cos\nu$ along $\mathbf i_0$ and the opposite leg is $r\sin\nu$ along $\mathbf j_0$. Dividing by $r$ gives $\mathbf i_1$. $\mathbf j_1$ is $\mathbf j_0$ turned by $\nu$: adjacent leg $\cos\nu$ along $\mathbf j_0$, opposite leg $\sin\nu$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf r_0^S &= \overrightarrow{FS} = r\cos\nu\,\mathbf i_0 + r\sin\nu\,\mathbf j_0 = r\,\mathbf i_1 \quad &\text{(legs of the triangle of $FS$)} \\
> \mathbf i_1 &= \cos\nu\,\mathbf i_0 + \sin\nu\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf i_1$)} \\
> \mathbf j_1 &= -\sin\nu\,\mathbf i_0 + \cos\nu\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf j_1$: opposite leg on $-\mathbf i_0$)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\nu\cos\nu - \left(-\sin\nu\right)\sin\nu\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\nu + \sin^2\nu = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\nu\sin\nu - \sin\nu\cos\nu = 0 \quad &\text{(rows times rows; row 3 is the unit row of $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^S = r\,\mathbf i_1, \quad r = \frac{p}{1 + e\cos\nu}, \quad [{}_0R_1] = \begin{pmatrix} \cos\nu & -\sin\nu & 0 \cr \sin\nu & \cos\nu & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1}$$
>
> **Units:** $[r] = [p] = [\mathrm{L}]$; $e$ and $\nu$ dimensionless
> **Meaning:** $\mathbf i_1$ and $\mathbf j_1$ are the radial and transverse directions of the orbit (Eq. 8.2); the frame turns with the radius $FS$.

![[attachments/EM-SOL/p25-cord.svg]]

> [!derivation] Cord basis and position of the astronaut: rotation by theta about k1
> **Law:** right triangle of the cord; elementary rotation about the third axis and its checks; position as a sum of segments
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 3.16; Problems.pdf, p. 13
>
> The frame $Sx_1y_1$ is drawn with $\mathbf i_1$ to the right, $\mathbf j_1$ up and $\mathbf k_1$ out of the paper (⊙); $F$ lies along minus $\mathbf i_1$. $\theta$ is measured from $\mathbf i_1$ counterclockwise, so it is the standard polar angle of $P$ about $S$. In the shaded right triangle the hypotenuse is the cord $L$, the leg adjacent to $\theta$ is $L\cos\theta$ along $\mathbf i_1$ and the opposite leg is $L\sin\theta$ along $\mathbf j_1$. $\mathbf e_\theta$ is $\mathbf j_1$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j_1$, opposite leg $\sin\theta$ along minus $\mathbf i_1$ (the minus sign, as before). To go from $F$ to $P$ we pass through $S$.
>
> $$\begin{aligned}
> \mathbf e_c &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \quad \mathbf e_\theta = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(the two right triangles)} \\
> \det[{}_1R_2] &= (+1)\cdot 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1, \quad \mathbf e_c\cdot\mathbf e_\theta = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0 \quad &\text{(third row; columns orthogonal)} \\
> \mathbf r_1^P &= \overrightarrow{SP} = L\,\mathbf e_c = L\cos\theta\,\mathbf i_1 + L\sin\theta\,\mathbf j_1 \quad &\text{(legs of the triangle of the cord)} \\
> \mathbf r_0^P &= \mathbf r_0^S + \mathbf r_1^P = r\,\mathbf i_1 + L\cos\theta\,\mathbf i_1 + L\sin\theta\,\mathbf j_1 \quad &\text{(Eq. 3.16)} \\
> \mathbf e_c &= \cos\theta\left(\cos\nu\,\mathbf i_0 + \sin\nu\,\mathbf j_0\right) + \sin\theta\left(-\sin\nu\,\mathbf i_0 + \cos\nu\,\mathbf j_0\right) \quad &\text{(columns of $[{}_0R_1]$ substituted)} \\
> &= \cos\left(\theta + \nu\right)\mathbf i_0 + \sin\left(\theta + \nu\right)\mathbf j_0 \quad &\text{(addition formulas of cosine and sine)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = L\,\mathbf e_c, \quad \mathbf r_0^P = r\,\mathbf i_1 + L\,\mathbf e_c, \quad [{}_1R_2] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \mathbf e_c = \cos(\theta + \nu)\,\mathbf i_0 + \sin(\theta + \nu)\,\mathbf j_0}$$
>
> **Units:** $[L] = [\mathrm{L}]$; angles dimensionless
> **Meaning:** the cord makes the angle $\theta + \nu$ with the inertial axis $Fx$ (product of the two rotations, Eq. 1.16); this angle is used in the independent check.

### Kinematics

> [!derivation] Motion of the moving frame and derivatives of its unit vectors
> **Law:** angular velocity and acceleration of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.9; [Lecture 5, Slide 16]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\nu\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \left.\frac{d}{dt}\left(\dot\nu\,\mathbf k_1\right)\right|_0 = \ddot\nu\,\mathbf k_1 \quad &\text{(rotation by $\nu(t)$ about the fixed $\mathbf k_0 = \mathbf k_1$; Eq. 3.9)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \dot\nu\,\mathbf k_1\times\mathbf i_1 = \dot\nu\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \dot\nu\,\mathbf k_1\times\mathbf j_1 = -\dot\nu\,\mathbf i_1 \quad &\text{(Eq. 3.3 and 3.4)} \\
> \frac{d}{dt}\left(\cos\nu\,\mathbf i_0 + \sin\nu\,\mathbf j_0\right) &= -\sin\nu\,\dot\nu\,\mathbf i_0 + \cos\nu\,\dot\nu\,\mathbf j_0 = \dot\nu\,\mathbf j_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \dot\nu\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \ddot\nu\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \dot\nu\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\dot\nu\,\mathbf i_1}$$
>
> **Units:** $[\dot\nu] = [\mathrm{T^{-1}}]$; $[\ddot\nu] = [\mathrm{T^{-2}}]$
> **Meaning:** the frame turns at the rate of the true anomaly, which on a non-circular orbit is not constant: the angular acceleration does not vanish in general.

#### (a) Acceleration of the spacecraft

> [!derivation] Velocity and acceleration of the spacecraft in the inertial frame
> **Law:** time derivative in $S_0$ of $r\,\mathbf i_1$; product rule and derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 8.3; Problems.pdf, p. 13
>
> $$\begin{aligned}
> \mathbf v_0^S &= \dot r\,\mathbf i_1 + r\left.\frac{d\mathbf i_1}{dt}\right|_0 = \dot r\,\mathbf i_1 + r\dot\nu\,\mathbf j_1 \quad &\text{(product rule; derivative of $\mathbf i_1$)} \\
> \mathbf a_0^S &= \ddot r\,\mathbf i_1 + \dot r\dot\nu\,\mathbf j_1 + \left(\dot r\dot\nu + r\ddot\nu\right)\mathbf j_1 + r\dot\nu\left(-\dot\nu\,\mathbf i_1\right) \quad &\text{(product rule on both terms; $\tfrac{d}{dt}(r\dot\nu) = \dot r\dot\nu + r\ddot\nu$)} \\
> &= \left(\ddot r - r\dot\nu^2\right)\mathbf i_1 + \left(2\dot r\dot\nu + r\ddot\nu\right)\mathbf j_1 \quad &\text{(grouped by unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^S = \left(\ddot r - r\dot\nu^2\right)\mathbf i_1 + \left(2\dot r\dot\nu + r\ddot\nu\right)\mathbf j_1}$$
>
> **Units:** $[\ddot r] = [r\dot\nu^2] = [\dot r\dot\nu] = [r\ddot\nu] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the radial part holds the centripetal term of the turning radius; the transverse part holds the change of the angular rate and the Coriolis-like term of a changing radius.

> [!derivation] Rates of the distance as functions of time
> **Law:** chain rule through $\nu(t)$; product rule
> **Source:** Notes.pdf, Eq. 8.14; Problems.pdf, p. 13
>
> Write $D$ for $1 + e\cos\nu$, so that $r$ is $p$ times $D^{-1}$.
>
> $$\begin{aligned}
> \dot D &= \frac{dD}{d\nu}\,\dot\nu = -e\sin\nu\,\dot\nu \quad &\text{(chain rule)} \\
> \dot r &= -p\,D^{-2}\,\dot D = \frac{pe\,\dot\nu\sin\nu}{D^2} \quad &\text{(chain rule on $D^{-1}$)} \\
> \frac{d}{dt}\left(pe\,\dot\nu\sin\nu\right) &= pe\left(\ddot\nu\sin\nu + \dot\nu^2\cos\nu\right) \quad &\text{(product rule; chain rule on the sine)} \\
> \frac{d}{dt}D^{-2} &= -2D^{-3}\dot D = 2e\,\dot\nu\sin\nu\,D^{-3} \quad &\text{(chain rule)} \\
> \ddot r &= \frac{pe\left(\ddot\nu\sin\nu + \dot\nu^2\cos\nu\right)}{D^2} + pe\,\dot\nu\sin\nu\cdot\frac{2e\,\dot\nu\sin\nu}{D^3} \quad &\text{(product rule on the two factors of $\dot r$)}
> \end{aligned}$$
>
> $$\boxed{\dot r = \frac{pe\,\dot\nu\sin\nu}{\left(1 + e\cos\nu\right)^2}, \qquad \ddot r = \frac{pe\left(\ddot\nu\sin\nu + \dot\nu^2\cos\nu\right)}{\left(1 + e\cos\nu\right)^2} + \frac{2pe^2\dot\nu^2\sin^2\nu}{\left(1 + e\cos\nu\right)^3}}$$
>
> **Units:** $[\dot r] = [p][\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$; $[\ddot r] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** with $\nu(t)$ known, $r$, its rates, $\dot\nu$ and $\ddot\nu$ are known functions of time, and so is the acceleration of part (a).

#### (b) Tangent vector of the orbit

> [!derivation] Unit tangent of the trajectory of the spacecraft
> **Law:** unit tangent as the velocity divided by the speed; right triangle of the velocity components
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.16; Problems.pdf, p. 13
>
> The two components of the velocity are the legs of a right triangle: $e\sin\nu$ along $\mathbf i_1$ and $1 + e\cos\nu$ along $\mathbf j_1$, after the common factor is taken out; the hypotenuse gives the speed.
>
> $$\begin{aligned}
> \dot r &= \frac{p}{D}\cdot\frac{e\,\dot\nu\sin\nu}{D} = r\dot\nu\,\frac{e\sin\nu}{D} \quad &\text{($p/D = r$)} \\
> \mathbf v_0^S &= \frac{r\dot\nu}{D}\left[e\sin\nu\,\mathbf i_1 + D\,\mathbf j_1\right] \quad &\text{(common factor)} \\
> e^2\sin^2\nu + \left(1 + e\cos\nu\right)^2 &= e^2\left(\sin^2\nu + \cos^2\nu\right) + 1 + 2e\cos\nu = 1 + 2e\cos\nu + e^2 \quad &\text{(Pythagoras for the bracket)} \\
> \mathbf e_t &= \frac{\mathbf v_0^S}{|\mathbf v_0^S|} = \frac{e\sin\nu\,\mathbf i_1 + \left(1 + e\cos\nu\right)\mathbf j_1}{\sqrt{1 + 2e\cos\nu + e^2}} \quad &\text{($r$, $D$ and $\dot\nu$ positive)} \\
> e\sin\nu\cos\nu - \left(1 + e\cos\nu\right)\sin\nu &= -\sin\nu, \quad e\sin^2\nu + \left(1 + e\cos\nu\right)\cos\nu = e + \cos\nu \quad &\text{(components on $\mathbf i_0$ and $\mathbf j_0$ with $[{}_0R_1]$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t(t) = \frac{e\sin\nu\,\mathbf i_1 + \left(1 + e\cos\nu\right)\mathbf j_1}{\sqrt{1 + 2e\cos\nu + e^2}} = \frac{-\sin\nu\,\mathbf i_0 + \left(e + \cos\nu\right)\mathbf j_0}{\sqrt{1 + 2e\cos\nu + e^2}}, \quad \nu = \nu(t)}$$
>
> **Units:** dimensionless
> **Meaning:** on a circular orbit (zero eccentricity) the tangent is the transverse direction $\mathbf j_1$; otherwise it leans outwards while the spacecraft goes from the periapsis to the apoapsis (the factor $e\sin\nu$ positive) and inwards on the way back.

#### (c) Relative velocity and acceleration of the astronaut

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$ and $\mathbf j_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 13
>
> $$\begin{aligned}
> \mathbf v_1^P &= \frac{d}{dt}\left(L\cos\theta\right)\mathbf i_1 + \frac{d}{dt}\left(L\sin\theta\right)\mathbf j_1 = -L\dot\theta\sin\theta\,\mathbf i_1 + L\dot\theta\cos\theta\,\mathbf j_1 \quad &\text{(chain rule; $L$ constant)} \\
> \mathbf a_1^P &= -L\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right)\mathbf i_1 + L\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf j_1 \quad &\text{(product rule on $\dot\theta\sin\theta$ and $\dot\theta\cos\theta$)} \\
> &= L\ddot\theta\left(-\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1\right) - L\dot\theta^2\left(\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1\right) \quad &\text{(grouped by $\ddot\theta$ and $\dot\theta^2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = L\dot\theta\,\mathbf e_\theta = L\dot\theta\left(-\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1\right), \qquad \mathbf a_1^P = L\ddot\theta\,\mathbf e_\theta - L\dot\theta^2\,\mathbf e_c}$$
>
> **Units:** $[L\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[L\ddot\theta] = [L\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in $S_1$ the astronaut moves on a circle of radius $L$ about the spacecraft: a tangential part and a centripetal part towards $S$.

> [!derivation] Absolute acceleration of the astronaut: the five terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule and derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write $x_1$ and $y_1$ for the components $L\cos\theta$ and $L\sin\theta$ of $\mathbf r_1^P$.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \mathbf v_0^S + \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + x_1\dot\nu\,\mathbf j_1 - y_1\dot\nu\,\mathbf i_1 = \mathbf v_0^S + \mathbf v_1^P + \boldsymbol\omega_{10}\times\mathbf r_1^P \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 + \dot x_1\dot\nu\,\mathbf j_1 - \dot y_1\dot\nu\,\mathbf i_1 = \mathbf a_1^P + \boldsymbol\omega_{10}\times\mathbf v_1^P \quad &\text{(product rule; turning of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d}{dt}\right|_0\left(\dot\nu\,\mathbf k_1\times\mathbf r_1^P\right) &= \ddot\nu\,\mathbf k_1\times\mathbf r_1^P + \dot\nu\,\mathbf k_1\times\left(\mathbf v_1^P + \boldsymbol\omega_{10}\times\mathbf r_1^P\right) \quad &\text{(product rule; $\mathbf k_1$ fixed; first row for $d\mathbf r_1^P/dt|_0$)} \\
> \mathbf a_0^P &= \mathbf a_0^S + \mathbf a_1^P + \boldsymbol\alpha_{10}\times\mathbf r_1^P + \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) + 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P \quad &\text{(sum of the derivatives)} \\
> \boldsymbol\alpha_{10}\times\mathbf r_1^P &= \ddot\nu\,\mathbf k_1\times L\,\mathbf e_c = L\ddot\nu\,\mathbf e_\theta \quad &\text{($\mathbf k_1\times\mathbf e_c = \mathbf e_\theta$)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \dot\nu\,\mathbf k_1\times L\dot\nu\,\mathbf e_\theta = -L\dot\nu^2\,\mathbf e_c \quad &\text{($\mathbf k_1\times\mathbf e_\theta = -\mathbf e_c$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\dot\nu\,\mathbf k_1\times L\dot\theta\,\mathbf e_\theta = -2L\dot\nu\dot\theta\,\mathbf e_c \quad &\text{(same product)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_0^S + L\left(\ddot\theta + \ddot\nu\right)\mathbf e_\theta - L\left(\dot\theta^2 + 2\dot\nu\dot\theta + \dot\nu^2\right)\mathbf e_c}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the four terms beyond the acceleration of the origin add up to the acceleration of circular motion at the absolute angular rate of the cord, the sum of the two rates.

### Forces and Equations of Motion

The free-body diagram of the astronaut in $S_1$ shows the pull of the cord towards $S$, the gravity of $F$, and the four inertia forces: the force of the origin (minus the mass times the acceleration of $S$), the Euler force across the cord, and the centrifugal and Coriolis forces along the cord.

![[attachments/EM-SOL/p25-fbd.svg]]

#### (d) Inertia forces in the moving frame

> [!derivation] The four inertia forces on the astronaut
> **Law:** inertia forces of a non-inertial frame, each vector product expanded
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; Problems.pdf, p. 13
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^S = -m\left(\ddot r - r\dot\nu^2\right)\mathbf i_1 - m\left(2\dot r\dot\nu + r\ddot\nu\right)\mathbf j_1 \quad &\text{(part (a))} \\
> \mathbf F_E &= -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = -mL\ddot\nu\,\mathbf e_\theta = mL\ddot\nu\left(\sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j_1\right) \quad &\text{(Euler term of the composition box times $-m$)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = mL\dot\nu^2\,\mathbf e_c \quad &\text{(centripetal term times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2mL\dot\nu\dot\theta\,\mathbf e_c \quad &\text{(Coriolis term times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_A = -m\,\mathbf a_0^S, \quad \mathbf F_E = mL\ddot\nu\left(\sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j_1\right), \quad \mathbf F_C = mL\dot\nu^2\,\mathbf e_c, \quad \mathbf F_{COR} = 2mL\dot\nu\dot\theta\,\mathbf e_c}$$
>
> **Units:** $[m\,a_0^S] = [mL\ddot\nu] = [mL\dot\nu^2] = [mL\dot\nu\dot\theta] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the centrifugal force pushes the astronaut away from $S$ along the cord, because the whole of $\mathbf r_1^P$ lies in the plane normal to the rotation; the Euler force is present because the true anomaly does not grow uniformly on a non-circular orbit.

> [!derivation] Newton's second law in the moving frame, projected on the cord basis
> **Law:** Newton's second law in a non-inertial frame with the inertia forces; gravity of $F$ equal at $P$ and at $S$ (hypothesis of parts (e) and (f))
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 8.1; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> m\,\mathbf a_1^P &= -T\,\mathbf e_c + m\,\mathbf g_S + \mathbf F_A + \mathbf F_E + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63 with $\mathbf g_P = \mathbf g_S$)} \\
> \mathbf g_S &= -\frac{\mu_F}{r^2}\,\mathbf i_1 \quad &\text{(Eq. 8.1 at $S$)} \\
> \mathbf i_1\cdot\mathbf e_c &= \cos\theta, \quad \mathbf j_1\cdot\mathbf e_c = \sin\theta, \quad \mathbf i_1\cdot\mathbf e_\theta = -\sin\theta, \quad \mathbf j_1\cdot\mathbf e_\theta = \cos\theta \quad &\text{(components of the cord basis)} \\
> \mathbf e_\theta:\ mL\ddot\theta &= \frac{m\mu_F}{r^2}\sin\theta + m\left(\ddot r - r\dot\nu^2\right)\sin\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\cos\theta - mL\ddot\nu \quad &\text{(across the cord: no tension)} \\
> \mathbf e_c:\ -mL\dot\theta^2 &= -T - \frac{m\mu_F}{r^2}\cos\theta - m\left(\ddot r - r\dot\nu^2\right)\cos\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\sin\theta + mL\dot\nu^2 + 2mL\dot\nu\dot\theta \quad &\text{(along the cord)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} mL\ddot\theta = m\left(\frac{\mu_F}{r^2} + \ddot r - r\dot\nu^2\right)\sin\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\cos\theta - mL\ddot\nu \cr T = mL\dot\theta^2 + mL\dot\nu^2 + 2mL\dot\theta\dot\nu - \frac{m\mu_F}{r^2}\cos\theta + m\left(r\dot\nu^2 - \ddot r\right)\cos\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\sin\theta \end{gathered}}$$
>
> **Units:** $[m\mu_F/r^2] = [\mathrm{M}][\mathrm{L^3\,T^{-2}}][\mathrm{L^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$, like every other term
> **Meaning:** two scalar equations for the two unknowns $\theta$ and $T$: the projection across the cord is free of the tension and gives the motion; the projection along the cord gives the tension afterwards.

### Answers and Checks

#### (e) Differential equation of the cord angle

> [!derivation] Equation of motion of theta, and its form for a spacecraft in free flight
> **Law:** projection across the cord; Newton's second law of the spacecraft under the gravity of $F$ alone (radial and transverse components)
> **Source:** Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.6; Notes.pdf, Eq. 4.63; Problems.pdf, p. 13
>
> A spacecraft in free flight about $F$ (the reading stated in the table) has the acceleration $\mathbf g_S$: its radial and transverse components are Eq. 8.5 and Eq. 8.6 with $\nu$ in place of the polar angle.
>
> $$\begin{aligned}
> \ddot\theta &= -\ddot\nu + \frac{1}{L}\left(\frac{\mu_F}{r^2} + \ddot r - r\dot\nu^2\right)\sin\theta - \frac{1}{L}\left(2\dot r\dot\nu + r\ddot\nu\right)\cos\theta \quad &\text{(projection across the cord, divided by $mL$)} \\
> \ddot r - r\dot\nu^2 &= -\frac{\mu_F}{r^2}, \quad 2\dot r\dot\nu + r\ddot\nu = 0 \quad &\text{(Eq. 8.5 and Eq. 8.6: free flight)} \\
> \ddot\theta &= -\ddot\nu + \frac{1}{L}\left(\frac{\mu_F}{r^2} - \frac{\mu_F}{r^2}\right)\sin\theta - 0 = -\ddot\nu \quad &\text{(substituted)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = -\ddot\nu + \frac{1}{L}\left(\frac{\mu_F}{r^2} + \ddot r - r\dot\nu^2\right)\sin\theta - \frac{1}{L}\left(2\dot r\dot\nu + r\ddot\nu\right)\cos\theta; \qquad \text{free flight: } \ddot\theta + \ddot\nu(t) = 0}$$
>
> **Units:** $[\ddot\theta] = [\ddot\nu] = [\mu_F/(Lr^2)] = [\mathrm{T^{-2}}]$
> **Meaning:** $r$, its rates and $\nu$ are known functions of time, so the general form is one second-order equation for $\theta(t)$ alone. In free flight the weight of the astronaut and the force of the origin cancel exactly, and only the Euler force drives the angle.

#### (f) Tension of the cord

> [!derivation] Tension as a function of time
> **Law:** projection along the cord; integral of the free-flight equation with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.6; Problems.pdf, p. 13
>
> $$\begin{aligned}
> T(t) &= mL\dot\theta^2 + mL\dot\nu^2 + 2mL\dot\theta\dot\nu - \frac{m\mu_F}{r^2}\cos\theta + m\left(r\dot\nu^2 - \ddot r\right)\cos\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\sin\theta \quad &\text{(projection along the cord, $\theta(t)$ known)} \\
> &= mL\left(\dot\theta^2 + 2\dot\theta\dot\nu + \dot\nu^2\right) - \frac{m\mu_F}{r^2}\cos\theta + \frac{m\mu_F}{r^2}\cos\theta - 0 \quad &\text{(free flight: $r\dot\nu^2 - \ddot r = \mu_F/r^2$, transverse part zero)} \\
> &= mL\left(\dot\theta + \dot\nu\right)^2 \quad &\text{(square of a sum)} \\
> \int_0^t\left(\ddot\theta + \ddot\nu\right)dt' &= \left[\dot\theta + \dot\nu\right]_0^t = \dot\theta + \dot\nu - \dot\theta(0) - \dot\nu(0) = 0 \quad &\text{(free-flight equation integrated; antiderivative $\dot\theta + \dot\nu$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{T(t) = mL\dot\theta^2 + mL\dot\nu^2 + 2mL\dot\theta\dot\nu - \frac{m\mu_F\cos\theta}{r^2} + m\left(r\dot\nu^2 - \ddot r\right)\cos\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\sin\theta; \quad \text{free flight: } T = mL\left(\dot\theta + \dot\nu\right)^2 = mL\left(\dot\theta(0) + \dot\nu(0)\right)^2}$$
>
> **Units:** $[mL\dot\theta^2] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** in free flight the cord only supplies the centripetal force of a circle of radius $L$ described at the absolute rate of the cord, which stays at its initial value: the tension is constant, and the hypothesis of a taut cord holds as long as that rate is not zero.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Acceleration of $S$ | $\mathbf a_0^S = (\ddot r - r\dot\nu^2)\,\mathbf i_1 + (2\dot r\dot\nu + r\ddot\nu)\,\mathbf j_1$, with $r = p/(1 + e\cos\nu)$, $\dot r = pe\dot\nu\sin\nu/(1 + e\cos\nu)^2$, $\ddot r = pe(\ddot\nu\sin\nu + \dot\nu^2\cos\nu)/(1 + e\cos\nu)^2 + 2pe^2\dot\nu^2\sin^2\nu/(1 + e\cos\nu)^3$ |
| (b) Unit tangent of $S$ | $\mathbf e_t = [e\sin\nu\,\mathbf i_1 + (1 + e\cos\nu)\,\mathbf j_1]/\sqrt{1 + 2e\cos\nu + e^2} = [-\sin\nu\,\mathbf i_0 + (e + \cos\nu)\,\mathbf j_0]/\sqrt{1 + 2e\cos\nu + e^2}$ for $\dot\nu \gt 0$; the opposite vector if $\dot\nu \lt 0$ |
| (c) Relative velocity and acceleration | $\mathbf v_1^P = L\dot\theta(-\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1)$; $\mathbf a_1^P = -L(\ddot\theta\sin\theta + \dot\theta^2\cos\theta)\,\mathbf i_1 + L(\ddot\theta\cos\theta - \dot\theta^2\sin\theta)\,\mathbf j_1$ |
| (d) Inertia forces | $\mathbf F_A = -m\,\mathbf a_0^S$; $\mathbf F_E = mL\ddot\nu(\sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j_1)$; $\mathbf F_C = mL\dot\nu^2(\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1)$; $\mathbf F_{COR} = 2mL\dot\nu\dot\theta(\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1)$ |
| (e) Equation for $\theta$ | general: $L\ddot\theta = -L\ddot\nu + (\mu_F/r^2 + \ddot r - r\dot\nu^2)\sin\theta - (2\dot r\dot\nu + r\ddot\nu)\cos\theta$; spacecraft in free flight (reading taken): $\ddot\theta + \ddot\nu = 0$ |
| (f) Tension | general: $T = mL\dot\theta^2 + mL\dot\nu^2 + 2mL\dot\theta\dot\nu - m\mu_F\cos\theta/r^2 + m(r\dot\nu^2 - \ddot r)\cos\theta - m(2\dot r\dot\nu + r\ddot\nu)\sin\theta$; free flight: $T = mL(\dot\theta + \dot\nu)^2$, constant |

**Check against the official key:** Problems.pdf, p. 73 and p. 74 print the acceleration of the spacecraft with its rates of the distance, the Euler force and the general tension; the box below sets them side by side with the results above. Every one coincides, so there is no discrepancy. The key does not print the differential equation of part (e), nor the unit tangent of part (b).

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison with the key; common denominator
> **Source:** Problems.pdf, p. 73; Problems.pdf, p. 74
>
> The key writes the second rate of the distance over the denominator $(1 + e\cos\nu)^4$; dividing its numerator and denominator by $(1 + e\cos\nu)^2$ and by $(1 + e\cos\nu)$ term by term gives the form of the rates box.
>
> $$\begin{aligned}
> \text{key: } \mathbf a_0^S &= \left(\ddot r - r\dot\nu^2\right)\mathbf i_1 + \left(2\dot r\dot\nu + r\ddot\nu\right)\mathbf j_1, \quad \dot r = \frac{pe\dot\nu\sin\nu}{(1 + e\cos\nu)^2} \quad &\text{(same as part (a))} \\
> \text{key: } \ddot r &= \frac{pe\left(\ddot\nu\sin\nu + \dot\nu^2\cos\nu\right)(1 + e\cos\nu)^2 + 2pe^2\dot\nu^2\sin^2\nu\,(1 + e\cos\nu)}{(1 + e\cos\nu)^4} \quad &\text{(as printed)} \\
> &= \frac{pe\left(\ddot\nu\sin\nu + \dot\nu^2\cos\nu\right)}{(1 + e\cos\nu)^2} + \frac{2pe^2\dot\nu^2\sin^2\nu}{(1 + e\cos\nu)^3} \quad &\text{(each term simplified: same as the rates box)} \\
> \text{key: } \mathbf F_{Eul} &= mL\ddot\nu\left(\sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j_1\right) \quad &\text{(same as part (d))} \\
> \text{key: } T &= mL\dot\theta^2 - \frac{\mu_F m\cos\theta}{r^2} + mL\dot\nu^2 + 2mL\dot\theta\dot\nu + m\left(r\dot\nu^2 - \ddot r\right)\cos\theta - m\left(2\dot r\dot\nu + r\ddot\nu\right)\sin\theta \quad &\text{(same as the general tension of part (f))}
> \end{aligned}$$
>
> $$\boxed{\text{the four results of the key coincide with this solution}}$$
>
> **Units:** accelerations $[\mathrm{L\,T^{-2}}]$; forces $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the key keeps the gravity of $F$ and the acceleration of $S$ as separate terms, which is the general form; it does not use the free-flight reduction.

> [!derivation] Independent check in a non-rotating frame
> **Law:** Newton's second law in $S_0$ for the astronaut and for the spacecraft in free flight; the cord at the absolute angle of the change-of-basis box
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 8.4; Notes.pdf, Eq. 3.29
>
> With $\mathbf e_c$ at the angle $\theta + \nu$ from $\mathbf i_0$, the vector $L\,\mathbf e_c$ is a circle of radius $L$ described with the angle $\theta + \nu$; its unit vectors turn with the rate of that angle, and the frame through $S$ with the axes of $S_0$ only translates.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -T\,\mathbf e_c + m\,\mathbf g_S, \quad m\,\mathbf a_0^S = m\,\mathbf g_S \quad &\text{(Eq. 4.4 for $P$ with $\mathbf g_P = \mathbf g_S$; Eq. 8.4 for $S$)} \\
> m\left(\mathbf a_0^P - \mathbf a_0^S\right) &= -T\,\mathbf e_c \quad &\text{(difference)} \\
> \frac{d^2}{dt^2}\left(L\,\mathbf e_c\right) &= L\left(\ddot\theta + \ddot\nu\right)\mathbf e_\theta - L\left(\dot\theta + \dot\nu\right)^2\mathbf e_c \quad &\text{(chain rule on $\cos(\theta + \nu)$, $\sin(\theta + \nu)$, twice; product rule)} \\
> \mathbf e_\theta:\ mL\left(\ddot\theta + \ddot\nu\right) &= 0, \quad \mathbf e_c:\ -mL\left(\dot\theta + \dot\nu\right)^2 = -T \quad &\text{(projections)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \ddot\nu = 0, \qquad T = mL\left(\dot\theta + \dot\nu\right)^2}$$
>
> **Units:** $[mL\dot\theta^2] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** without any inertia force, the inertial route gives the same equation and the same tension as the free-flight forms of parts (e) and (f).

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 8.7; Notes.pdf, Eq. 8.14
>
> $$\begin{aligned}
> e = 0:\quad r &= p, \quad \dot r = \ddot r = 0, \quad \mathbf e_t = \mathbf j_1 \quad &\text{(circular orbit)} \\
> e = 0,\ \text{free flight}:\quad 2\dot r\dot\nu + r\ddot\nu &= p\,\ddot\nu = 0 \Rightarrow \ddot\nu = 0, \quad \mathbf F_E = \mathbf 0 \quad &\text{(Eq. 8.6: uniform rotation)} \\
> \dot\theta(0) + \dot\nu(0) = 0:\quad T &= 0 \quad &\text{(the astronaut keeps its direction in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{e = 0: \ \mathbf F_E = \mathbf 0,\ \mathbf e_t = \mathbf j_1; \qquad \dot\theta(0) + \dot\nu(0) = 0: \ T = 0}$$
>
> **Units:** $[T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** on a circular orbit the frame turns uniformly and the Euler force vanishes; an astronaut that does not turn in inertial space leaves the cord without tension, and the taut-cord hypothesis of the statement then fails.

---

## Problem 26: Heavy Particle on a Rotating Half-Circumference (Moving-Frame Method)

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides without friction on a half-circumference wire of radius $a$ whose lowest point is $O$ and whose ends are at the height $a$, at plus and minus $a$ from the axis (figure of the statement); the wire turns about the vertical axis $OY$ with the constant rate $\Omega$, and the particle starts at $O$ with the speed $v_0$ along the positive $x$ axis (Problems.pdf, p. 14). The statement asks for the degrees of freedom, a moving frame with the inertia force, the weight in that frame, the equilibrium points, the quadrature and the reaction, and the use of the energy equation. The wire is at rest in the frame that turns with it, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$: $\mathbf i_0$ along $OX$, $\mathbf j_0$ along $OY$ (vertical, up; the $\mathbf j$ of the statement), $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $OX_1Y_1Z_1$ attached to the wire: $\mathbf i_1$ along $OX_1$ in the plane of the wire, $\mathbf j_1 = \mathbf j_0$ the axis of rotation, $\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ normal to the plane of the wire; it coincides with $S_0$ at $t = 0$ and turns by $\Omega t$ about $\mathbf j_0$ |
| Wire basis | $\mathcal B_2 = \{\mathbf e_t, \mathbf e_n, \mathbf k_1\}$: unit tangent in the sense of growing $\theta$, principal normal (from $P$ towards the centre $C$) and the normal to the plane |
| Coordinate | $\theta$, the angle at the centre $C$ (at the height $a$ above $O$) from the downward vertical $CO$ to $CP$, positive towards $+\mathbf i_1$; $-\pi/2 \le \theta \le \pi/2$ on the wire |
| Constraints | $P$ in the plane of the wire and at the distance $a$ from $C$: two holonomic, smooth, bilateral constraints, fixed in $S_1$ (rheonomic in $S_0$) |
| Data | $m$ [kg], $a$ [m], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$], $\Omega$ [rad s$^{-1}$] |
| Initial state | $\theta(0) = 0$ (the particle at $O$), absolute velocity $v_0\,\mathbf i_0$ |
| Unknowns | $\theta(t)$; the reaction $\mathbf N = N_n\,\mathbf e_n + N_b\,\mathbf k_1$ (normal subspace of a curve, Notes.pdf, Eq. 6.16) |
| Applied force | weight $-mg\,\mathbf j_0$ |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial, uniform gravity, smooth wire (no tangential reaction), the rotation of the wire imposed from outside |

#### (a) Degrees of freedom

> [!derivation] Number of degrees of freedom
> **Law:** coordinates of a free particle minus independent holonomic constraints
> **Source:** Notes.pdf, Sec. 2.7; Notes.pdf, Sec. 6.5; Problems.pdf, p. 14
>
> In $S_1$ the two constraints are the plane of the wire and the circle of centre $C$; written with the components $x_1$, $y_1$, $z_1$ of the position in $\mathcal B_1$ they are independent, because one fixes $z_1$ and the other involves $x_1$ and $y_1$ only.
>
> $$\begin{aligned}
> z_1 &= 0 \quad &\text{(plane of the wire)} \\
> x_1^2 + \left(y_1 - a\right)^2 - a^2 &= 0 \quad &\text{(circle of centre $C$ and radius $a$)} \\
> 3 - 2 &= 1 \quad &\text{(coordinates minus constraints)}
> \end{aligned}$$
>
> $$\boxed{\text{one degree of freedom, the angle } \theta(t)}$$
>
> **Units:** $[x_1^2] = [a^2] = [\mathrm{L^2}]$
> **Meaning:** the angle $\Omega t$ of the wire is prescribed, a known function of time, so it adds no degree of freedom.

### Change of Basis and Position Vector

![[attachments/EM-SOL/p26-top-view.svg]]

> [!derivation] Basis of the turning wire: rotation by Omega t about j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf j_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf k_0$, the cross product of $\mathbf i_0$ and $\mathbf j_0$, points down the page (right-hand rule: fingers from $\mathbf i_0$, to the right, towards $\mathbf j_0$, towards the reader; the thumb goes down the page), so minus $\mathbf k_0$ points up the page. A positive $\Omega$ turns the wire counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ up the page, that is along minus $\mathbf k_0$ (the minus sign). $\mathbf k_1$ is $\mathbf k_0$ (down the page) turned by the same angle: adjacent leg $\cos\Omega t$ along $\mathbf k_0$, opposite leg $\sin\Omega t$ along plus $\mathbf i_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf i_1$: opposite leg on $-\mathbf k_0$)} \\
> \mathbf j_1 &= \mathbf j_0, \quad \mathbf k_1 = \sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf k_0 \quad &\text{(axis of the rotation; right triangle of $\mathbf k_1$)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \sin\Omega t\left(-\sin\Omega t\right)\right) = 1 \quad &\text{(expansion along the second row, cofactor sign $(-1)^{2+2}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows; row 2 is the unit row of $\mathbf j_0$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & 0 & \sin\Omega t \cr 0 & 1 & 0 \cr -\sin\Omega t & 0 & \cos\Omega t \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Omega t] = [1]$
> **Meaning:** it is the matrix of Eq. 1.19 with the angle $\Omega t$; $\mathbf k_1$ stays horizontal and normal to the plane of the wire.

![[attachments/EM-SOL/p26-wire-plane.svg]]

> [!derivation] Position vector and wire basis in the plane of the wire
> **Law:** position as a sum of segments; right triangle of the radius $CP$; relation with the standard polar angle; rotation in the plane and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 3.16; Problems.pdf, p. 14
>
> The plane of the wire, fixed in $S_1$, is drawn with $\mathbf i_1$ to the right and $\mathbf j_1$ up, so $\mathbf k_1$ points out of the paper (⊙). From $O$ to $P$ we pass through the centre $C$, because the distance from $C$ is the one that stays constant. Let $F$ be the point of the axis at the height of $P$: in the shaded right triangle $CFP$ the hypotenuse is $a$, the leg opposite to $\theta$ is $FP$, of length $a\sin\theta$, along $\mathbf i_1$, and the leg adjacent to $\theta$ is $CF$, of length $a\cos\theta$, pointing down, along minus $\mathbf j_1$ (the minus sign: $\theta$ is measured from the downward vertical). The standard polar angle about $C$, measured from $\mathbf i_1$ counterclockwise, is $\theta - \pi/2$.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^P = \mathbf r_1^P = \overrightarrow{OC} + \overrightarrow{CP} \quad &\text{(origin of $S_1$ at the fixed $O$; Eq. 3.16)} \\
> \overrightarrow{OC} &= a\,\mathbf j_1, \quad \overrightarrow{CP} = a\sin\theta\,\mathbf i_1 - a\cos\theta\,\mathbf j_1 \quad &\text{(centre on the axis; legs of $CFP$)} \\
> \cos\left(\theta - \tfrac{\pi}{2}\right) &= \cos\theta\cos\tfrac{\pi}{2} + \sin\theta\sin\tfrac{\pi}{2} = \sin\theta, \quad \sin\left(\theta - \tfrac{\pi}{2}\right) = \sin\theta\cos\tfrac{\pi}{2} - \cos\theta\sin\tfrac{\pi}{2} = -\cos\theta \quad &\text{(difference formulas: the standard form gives the same $\overrightarrow{CP}$)} \\
> \mathbf r_1^P &= a\sin\theta\,\mathbf i_1 + a\left(1 - \cos\theta\right)\mathbf j_1 \quad &\text{(sum, grouped by unit vector)} \\
> \frac{d\mathbf r_1^P}{d\theta} &= a\cos\theta\,\mathbf i_1 + a\sin\theta\,\mathbf j_1, \quad \left|\frac{d\mathbf r_1^P}{d\theta}\right| = a \quad &\text{($\tfrac{d}{d\theta}\sin\theta = \cos\theta$, $\tfrac{d}{d\theta}(1 - \cos\theta) = \sin\theta$)} \\
> \mathbf e_t &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \quad \mathbf e_n = \frac{d\mathbf e_t}{d\theta} = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(Eq. 2.9; $\mathbf e_n$ is minus $\overrightarrow{CP}/a$: towards $C$)} \\
> \det[{}_1R_2] &= (+1)\cdot 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1, \quad \mathbf e_t\cdot\mathbf e_n = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0 \quad &\text{(third row; columns orthogonal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = a\sin\theta\,\mathbf i_1 + a\left(1 - \cos\theta\right)\mathbf j_1, \quad [{}_1R_2] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_1R_2] = 1}$$
>
> **Units:** $[a] = [\mathrm{L}]$; direction cosines dimensionless
> **Meaning:** $\theta$ zero is the lowest point $O$ and $\theta$ equal to $\pi/2$ the end of the wire at the height $a$; the distance of $P$ to the axis is the horizontal leg $a\sin\theta$.

### Kinematics

> [!derivation] Motion of the turning frame and derivatives of the unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis; chain rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9; [Lecture 5, Slide 16]
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = \dot\Omega\,\mathbf j_1 = \mathbf 0, \quad \mathbf a_0^O = \mathbf 0 \quad &\text{(simple rotation about the fixed vertical; $\Omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf i_1 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf j_1\times\mathbf k_1 = \Omega\,\mathbf i_1 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0\right) &= -\Omega\sin\Omega t\,\mathbf i_0 - \Omega\cos\Omega t\,\mathbf k_0 = -\Omega\,\mathbf k_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)} \\
> \left.\frac{d\mathbf e_t}{dt}\right|_1 &= \frac{d\mathbf e_t}{d\theta}\,\dot\theta = \dot\theta\,\mathbf e_n \quad &\text{(chain rule; $\mathbf i_1$, $\mathbf j_1$ constant in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf e_t}{dt}\right|_1 = \dot\theta\,\mathbf e_n}$$
>
> **Units:** $[\Omega] = [\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** in $S_1$ only the wire basis turns, with the particle; in $S_0$ the whole plane of the wire turns about the vertical as well.

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24
>
> $$\begin{aligned}
> \mathbf v_1^P &= a\cos\theta\,\dot\theta\,\mathbf i_1 + a\sin\theta\,\dot\theta\,\mathbf j_1 = a\dot\theta\,\mathbf e_t \quad &\text{(chain rule on the components)} \\
> \mathbf a_1^P &= a\ddot\theta\,\mathbf e_t + a\dot\theta\left.\frac{d\mathbf e_t}{dt}\right|_1 = a\ddot\theta\,\mathbf e_t + a\dot\theta^2\,\mathbf e_n \quad &\text{(product rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = a\dot\theta\,\mathbf e_t, \qquad \mathbf a_1^P = a\ddot\theta\,\mathbf e_t + a\dot\theta^2\,\mathbf e_n}$$
>
> **Units:** $[a\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[a\ddot\theta] = [a\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in $S_1$ the particle moves on a fixed circle: a tangential acceleration and a centripetal one towards $C$.

> [!derivation] Absolute velocity and acceleration: transport, Coriolis and centripetal terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left.\frac{d}{dt}\right|_0\left(a\sin\theta\,\mathbf i_1 + a(1 - \cos\theta)\,\mathbf j_1\right) = a\dot\theta\cos\theta\,\mathbf i_1 + a\dot\theta\sin\theta\,\mathbf j_1 + a\sin\theta\left(-\Omega\,\mathbf k_1\right) \quad &\text{(product rule; chain rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> &= \underbrace{a\dot\theta\,\mathbf e_t}_{\mathbf v_1^P} + \underbrace{\left(-\Omega a\sin\theta\,\mathbf k_1\right)}_{\boldsymbol\omega_{10}\times\mathbf r_1^P} \quad &\text{(grouped; $\Omega\,\mathbf j_1\times a\sin\theta\,\mathbf i_1 = -\Omega a\sin\theta\,\mathbf k_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \frac{d}{dt}\left(a\dot\theta\cos\theta\right)\mathbf i_1 + \frac{d}{dt}\left(a\dot\theta\sin\theta\right)\mathbf j_1 + a\dot\theta\cos\theta\left(-\Omega\,\mathbf k_1\right) = \mathbf a_1^P - \Omega a\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(components in $S_1$ plus the turning of $\mathbf i_1$)} \\
> \left.\frac{d}{dt}\right|_0\left(-\Omega a\sin\theta\,\mathbf k_1\right) &= -\Omega a\dot\theta\cos\theta\,\mathbf k_1 - \Omega^2a\sin\theta\,\mathbf i_1 \quad &\text{(chain rule; derivative of $\mathbf k_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\Omega a\dot\theta\,\mathbf j_1\times\left(\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1\right) = -2\Omega a\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(the two $\mathbf k_1$ terms above)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf j_1\times\left(-\Omega a\sin\theta\,\mathbf k_1\right) = -\Omega^2a\sin\theta\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term above; $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = a\dot\theta\,\mathbf e_t - \Omega a\sin\theta\,\mathbf k_1, \qquad \mathbf a_0^P = a\ddot\theta\,\mathbf e_t + a\dot\theta^2\,\mathbf e_n - 2\Omega a\dot\theta\cos\theta\,\mathbf k_1 - \Omega^2a\sin\theta\,\mathbf i_1}$$
>
> **Units:** every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the Coriolis acceleration is normal to the plane of the wire and appears because the distance to the axis changes while the plane turns; the centripetal one points horizontally to the axis.

### Forces and Equations of Motion

The free-body diagram of the particle in $S_1$ shows, in the plane of the wire, the weight, the reaction along $\mathbf e_n$ and the centrifugal force (horizontal, away from the axis); normal to the plane, the reaction along $\mathbf k_1$ and the Coriolis force. The inertia force of the origin and the Euler force vanish ($O$ fixed, $\Omega$ constant).

![[attachments/EM-SOL/p26-fbd.svg]]

#### (b) Inertia force in the moving frame

> [!derivation] Inertia forces on the particle in the turning frame
> **Law:** inertia forces of a non-inertial frame, each vector product expanded
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; Problems.pdf, p. 14
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\Omega^2a\sin\theta\,\mathbf i_1 \quad &\text{(centripetal term of the composition box times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\Omega a\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(Coriolis term times $-m$)} \\
> \mathbf i_1\cdot\mathbf e_t &= \cos\theta, \quad \mathbf i_1\cdot\mathbf e_n = -\sin\theta \quad &\text{(components of the wire basis)} \\
> \mathbf F_C &= m\Omega^2a\sin\theta\cos\theta\,\mathbf e_t - m\Omega^2a\sin^2\theta\,\mathbf e_n \quad &\text{(projected on the wire basis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_i = \mathbf F_C + \mathbf F_{COR} = m\Omega^2a\sin\theta\,\mathbf i_1 + 2m\Omega a\dot\theta\cos\theta\,\mathbf k_1}$$
>
> **Units:** $[m\Omega^2a] = [m\Omega a\dot\theta] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the centrifugal force is horizontal, away from the axis, and proportional to the distance $a\sin\theta$; the Coriolis force is normal to the plane of the wire, along plus $\mathbf k_1$ while $\theta$ grows (the factor $\cos\theta$ is positive on the whole wire).

#### (c) Weight in the moving frame

> [!derivation] Components of the weight
> **Law:** the axis of rotation is the vertical, so $\mathbf j_1$ is the vertical at every instant
> **Source:** Notes.pdf, Eq. 1.19; Problems.pdf, p. 14
>
> $$\begin{aligned}
> \mathbf W &= -mg\,\mathbf j_0 = -mg\,\mathbf j_1 \quad &\text{(second column of $[{}_0R_1]$: $\mathbf j_1 = \mathbf j_0$)} \\
> \mathbf W\cdot\mathbf e_t &= -mg\sin\theta, \quad \mathbf W\cdot\mathbf e_n = -mg\cos\theta, \quad \mathbf W\cdot\mathbf k_1 = 0 \quad &\text{($\mathbf j_1\cdot\mathbf e_t = \sin\theta$, $\mathbf j_1\cdot\mathbf e_n = \cos\theta$)}
> \end{aligned}$$
>
> $$\boxed{W_{X_1} = 0, \quad W_{Y_1} = -mg, \quad W_{Z_1} = 0}$$
>
> **Units:** $[mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the weight keeps the same components in the turning frame, because it lies along the axis of the rotation.

> [!derivation] Newton's second law in the turning frame, projected on the wire basis
> **Law:** Newton's second law in a non-inertial frame with the inertia forces; reaction of a smooth curve
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.16; Notes.pdf, Eq. 6.17; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> m\,\mathbf a_1^P &= \mathbf W + N_n\,\mathbf e_n + N_b\,\mathbf k_1 + \mathbf F_C + \mathbf F_{COR} \quad &\text{(Eq. 4.63)} \\
> \mathbf e_t:\ ma\ddot\theta &= -mg\sin\theta + m\Omega^2a\sin\theta\cos\theta \quad &\text{(tangent: no reaction, no Coriolis force)} \\
> \mathbf e_n:\ ma\dot\theta^2 &= -mg\cos\theta + N_n - m\Omega^2a\sin^2\theta \quad &\text{(in the plane, towards $C$)} \\
> \mathbf k_1:\ 0 &= N_b + 2m\Omega a\dot\theta\cos\theta \quad &\text{(normal to the plane: no relative motion there)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = \sin\theta\left(\Omega^2\cos\theta - \frac{g}{a}\right), \qquad N_n = ma\dot\theta^2 + mg\cos\theta + m\Omega^2a\sin^2\theta, \qquad N_b = -2m\Omega a\dot\theta\cos\theta}$$
>
> **Units:** $[g/a] = [\Omega^2] = [\mathrm{T^{-2}}]$; $[N_n] = [N_b] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations for the three unknowns $\theta$, $N_n$ and $N_b$: the tangent equation is the equation of motion, the other two give the reaction afterwards.

### Answers and Checks

#### (d) Equilibrium points

> [!derivation] Relative equilibria on the wire
> **Law:** relative rest in the tangent equation
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \dot\theta = 0,\ \ddot\theta = 0:\quad \sin\theta\left(\Omega^2\cos\theta - \frac{g}{a}\right) &= 0 \quad &\text{(tangent equation at rest)} \\
> \sin\theta = 0 &\Rightarrow \theta = 0 \quad &\text{(the only zero of the sine between $-\pi/2$ and $\pi/2$)} \\
> \cos\theta_e &= \frac{g}{a\Omega^2} \quad &\text{(second factor)} \\
> 0 \lt \frac{g}{a\Omega^2} \lt 1 &\iff \Omega^2 \gt \frac{g}{a} \quad &\text{(a solution with $0 \lt |\theta_e| \lt \pi/2$ exists)} \\
> \theta = \pm\frac{\pi}{2}:\quad \ddot\theta &= \pm 1\cdot\left(0 - \frac{g}{a}\right) \ne 0 \quad &\text{(the ends of the wire are not equilibria)}
> \end{aligned}$$
>
> $$\boxed{\theta = 0 \ \text{for every } \Omega; \qquad \theta = \pm\arccos\frac{g}{a\Omega^2} \ \text{only if } \Omega^2 \gt \frac{g}{a}}$$
>
> **Units:** $[g/(a\Omega^2)] = [1]$
> **Meaning:** yes, there are equilibria: the bottom always, and two symmetric points off the axis above the critical rate, where the tangential pull of the weight towards the bottom balances the tangential push of the centrifugal force.

#### (e) Quadrature and reaction force

> [!derivation] Initial relative rate
> **Law:** composition of velocities at the initial instant
> **Source:** Notes.pdf, Eq. 3.20; Problems.pdf, p. 14
>
> $$\begin{aligned}
> \mathbf v_0^P(0) &= a\dot\theta(0)\,\mathbf e_t(0) - \Omega a\sin 0\,\mathbf k_1 = a\dot\theta(0)\left(\cos 0\,\mathbf i_1 + \sin 0\,\mathbf j_1\right) \quad &\text{(velocity box; $\theta(0) = 0$)} \\
> &= a\dot\theta(0)\,\mathbf i_0 = v_0\,\mathbf i_0 \quad &\text{($\mathbf i_1 = \mathbf i_0$ at $t = 0$; initial condition)}
> \end{aligned}$$
>
> $$\boxed{\theta(0) = 0, \qquad \dot\theta(0) = \frac{v_0}{a}}$$
>
> **Units:** $[v_0/a] = [\mathrm{T^{-1}}]$
> **Meaning:** at $O$ the particle is on the axis, so the transport velocity is zero and the given velocity is the relative one.

> [!derivation] First integral and quadrature
> **Law:** the tangent equation multiplied by the rate is an exact derivative (chain rule); Barrow's rule; separation of variables
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.44; [Lecture 5, Slide 29]
>
> $$\begin{aligned}
> ma^2\dot\theta\ddot\theta + mga\sin\theta\,\dot\theta - m\Omega^2a^2\sin\theta\cos\theta\,\dot\theta &= 0 \quad &\text{(tangent equation times $ma\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12 ma^2\dot\theta^2\right) &= ma^2\dot\theta\ddot\theta, \quad \frac{d}{dt}\left(-mga\cos\theta\right) = mga\sin\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(-\tfrac12 m\Omega^2a^2\sin^2\theta\right) &= -m\Omega^2a^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule on $\sin^2\theta$)} \\
> \left[\tfrac12 ma^2\dot\theta^2 - mga\cos\theta - \tfrac12 m\Omega^2a^2\sin^2\theta\right]_0^t &= 0 \quad &\text{(the sum is constant; Barrow's rule)} \\
> \tfrac12 ma^2\dot\theta^2 - mga\cos\theta - \tfrac12 m\Omega^2a^2\sin^2\theta &= \tfrac12 mv_0^2 - mga \quad &\text{(value at $t = 0$: $\theta = 0$, $a\dot\theta = v_0$)} \\
> \dot\theta^2 &= \frac{v_0^2}{a^2} - \frac{2g}{a}\left(1 - \cos\theta\right) + \Omega^2\sin^2\theta \quad &\text{(multiplied by $2/(ma^2)$)} \\
> dt &= \frac{d\theta}{\sqrt{v_0^2/a^2 - (2g/a)(1 - \cos\theta) + \Omega^2\sin^2\theta}} \quad &\text{(positive root, $\dot\theta(0) \gt 0$; variables separated)}
> \end{aligned}$$
>
> $$\boxed{t = \int_0^{\theta}\frac{d\theta'}{\sqrt{\dfrac{v_0^2}{a^2} - \dfrac{2g}{a}\left(1 - \cos\theta'\right) + \Omega^2\sin^2\theta'}} \quad \text{(until the first turning point or the end of the wire)}}$$
>
> **Units:** every term of the radicand $[\mathrm{T^{-2}}]$; the integral is a time
> **Meaning:** the motion is reduced to one integral; the particle turns back where the radicand vanishes, or reaches the end of the wire if it stays positive up to $\theta$ equal to $\pi/2$.

> [!derivation] Reaction force as a function of the angle
> **Law:** normal equations of the turning frame with the squared rate eliminated through the first integral
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19
>
> $$\begin{aligned}
> N_n &= ma\dot\theta^2 + mg\cos\theta + m\Omega^2a\sin^2\theta \quad &\text{(equation along $\mathbf e_n$)} \\
> &= \frac{mv_0^2}{a} - 2mg\left(1 - \cos\theta\right) + m\Omega^2a\sin^2\theta + mg\cos\theta + m\Omega^2a\sin^2\theta \quad &\text{(squared rate of the first integral times $ma$)} \\
> &= \frac{mv_0^2}{a} + mg\left(3\cos\theta - 2\right) + 2m\Omega^2a\sin^2\theta \quad &\text{(terms collected)} \\
> N_b &= -2m\Omega a\dot\theta\cos\theta = \mp 2m\Omega a\cos\theta\sqrt{\frac{v_0^2}{a^2} - \frac{2g}{a}\left(1 - \cos\theta\right) + \Omega^2\sin^2\theta} \quad &\text{(equation along $\mathbf k_1$; upper sign while $\theta$ grows)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = \left[\frac{mv_0^2}{a} + mg\left(3\cos\theta - 2\right) + 2m\Omega^2a\sin^2\theta\right]\mathbf e_n - 2m\Omega a\dot\theta\cos\theta\,\mathbf k_1, \quad \mathbf e_n = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1}$$
>
> **Units:** $[mv_0^2/a] = [mg] = [m\Omega^2a] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the in-plane part carries the weight, the centrifugal push and the centripetal need of the circle; the part normal to the plane points along minus $\mathbf k_1$ while $\theta$ grows, against the Coriolis force.

#### (f) Energy equation

> [!derivation] Energy in the turning frame with constant and with variable Omega
> **Law:** power of each force on the relative velocity; potentials as minus the work along the wire, with Barrow's rule; product rule
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> With constant $\Omega$ the energy in $S_1$ is conserved for two reasons. First, the forces that do no work in $S_1$: the reaction, because the wire is smooth and at rest in $S_1$, so the reaction is normal to the relative velocity; the Coriolis force, always normal to the relative velocity; the force of the origin and the Euler force, which vanish. Second, the forces that do work have potentials that depend on the position only: the weight, and the centrifugal force because $\Omega$ is constant. Along the wire the displacement is $a\,\mathbf e_t\,d\theta'$. With $\Omega(t)$ the Euler force appears; it is normal to the plane, so it still does no work, but the centrifugal potential now depends on time.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= a\dot\theta\left(N_n\,\mathbf e_n + N_b\,\mathbf k_1\right)\cdot\mathbf e_t = 0, \quad \mathbf F_{COR}\cdot\mathbf v_1^P = 2m\Omega a^2\dot\theta^2\cos\theta\,\mathbf k_1\cdot\mathbf e_t = 0 \quad &\text{(no power in $S_1$)} \\
> V_C(\theta) - V_C(0) &= -\int_0^{\theta}m\Omega^2a\sin\theta'\,\mathbf i_1\cdot\mathbf e_t\,a\,d\theta' = -m\Omega^2a^2\left[\tfrac12\sin^2\theta'\right]_0^{\theta} = -\tfrac12 m\Omega^2a^2\sin^2\theta \quad &\text{(Eq. 4.14; antiderivative $\tfrac12\sin^2\theta'$; Barrow's rule)} \\
> V_g(\theta) - V_g(0) &= -\int_0^{\theta}\left(-mg\,\mathbf j_1\right)\cdot\mathbf e_t\,a\,d\theta' = mga\left[-\cos\theta'\right]_0^{\theta} = mga\left(1 - \cos\theta\right) \quad &\text{(Eq. 4.14; antiderivative $-\cos\theta'$; Barrow's rule)} \\
> E_1^P &= \tfrac12 ma^2\dot\theta^2 + mga\left(1 - \cos\theta\right) - \tfrac12 m\Omega^2a^2\sin^2\theta = \tfrac12 mv_0^2 \quad &\text{(constant $\Omega$: the first integral of part (e), with its initial value)} \\
> \mathbf F_E &= -m\dot\Omega\,\mathbf j_1\times\mathbf r_1^P = -m\dot\Omega a\sin\theta\,\mathbf j_1\times\mathbf i_1 = m\dot\Omega a\sin\theta\,\mathbf k_1, \quad \mathbf F_E\cdot\mathbf v_1^P = 0 \quad &\text{(variable $\Omega$: Eq. 4.62; normal to the plane)} \\
> \frac{dE_1^P}{dt} &= \dot\theta\left(ma^2\ddot\theta + mga\sin\theta - m\Omega^2a^2\sin\theta\cos\theta\right) - m\Omega\dot\Omega a^2\sin^2\theta = -m\Omega\dot\Omega a^2\sin^2\theta \quad &\text{(product and chain rules; the bracket is the tangent equation, zero)}
> \end{aligned}$$
>
> $$\boxed{\Omega \text{ constant: } E_1^P = \tfrac12 ma^2\dot\theta^2 + mga\left(1 - \cos\theta\right) - \tfrac12 m\Omega^2a^2\sin^2\theta = \tfrac12 mv_0^2; \qquad \Omega(t): \ \frac{dE_1^P}{dt} = -m\Omega\dot\Omega a^2\sin^2\theta \ne 0}$$
>
> **Units:** $[E_1^P] = [ma^2\dot\theta^2] = [\mathrm{M\,L^2\,T^{-2}}]$; $[m\Omega\dot\Omega a^2] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** yes with constant $\Omega$, in the turning frame: it is the first integral of part (e). No with $\Omega(t)$: the balance still holds but its right-hand side depends on the unknown position, so it is not a first integral.

> [!derivation] The energy in the inertial frame is not conserved
> **Law:** power of the reaction on the absolute velocity
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_0^P &= \left(N_n\,\mathbf e_n + N_b\,\mathbf k_1\right)\cdot\left(a\dot\theta\,\mathbf e_t - \Omega a\sin\theta\,\mathbf k_1\right) = -N_b\,\Omega a\sin\theta \quad &\text{(absolute velocity box)} \\
> &= 2m\Omega^2a^2\dot\theta\sin\theta\cos\theta \quad &\text{($N_b$ of the equations of motion)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_0^P}{dt} = \mathbf N\cdot\mathbf v_0^P = 2m\Omega^2a^2\dot\theta\sin\theta\cos\theta \ne 0}$$
>
> **Units:** $[m\Omega^2a^2\dot\theta] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** in $S_0$ the wire moves and its reaction does work, supplied by whatever keeps the rotation uniform; the energy equation can only be used in $S_1$.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | one, the angle $\theta$ (two holonomic constraints; $\Omega t$ prescribed) |
| (b) Moving frame and inertia force | $S_1$: $\mathbf i_1$ in the plane of the wire, $\mathbf j_1 = \mathbf j_0$ the axis, $\mathbf k_1$ normal to the plane; $\mathbf F_i = m\Omega^2a\sin\theta\,\mathbf i_1 + 2m\Omega a\dot\theta\cos\theta\,\mathbf k_1$ |
| (c) Weight | $\mathbf W = -mg\,\mathbf j_1$: components $(0, -mg, 0)$ in $\mathcal B_1$ |
| (d) Equilibria | $\theta = 0$ always; $\theta = \pm\arccos(g/(a\Omega^2))$ if $\Omega^2 \gt g/a$ |
| (e) Quadrature | $t = \int_0^{\theta}d\theta'/\sqrt{v_0^2/a^2 - (2g/a)(1 - \cos\theta') + \Omega^2\sin^2\theta'}$ |
| (e) Reaction | $\mathbf N = [mv_0^2/a + mg(3\cos\theta - 2) + 2m\Omega^2a\sin^2\theta]\,\mathbf e_n - 2m\Omega a\dot\theta\cos\theta\,\mathbf k_1$ |
| (f) Energy equation | yes in $S_1$ with constant $\Omega$: $\frac12 ma^2\dot\theta^2 + mga(1 - \cos\theta) - \frac12 m\Omega^2a^2\sin^2\theta = \frac12 mv_0^2$; no with $\Omega(t)$: $dE_1^P/dt = -m\Omega\dot\Omega a^2\sin^2\theta$ |

**Check against the official key:** Problems.pdf, p. 74 lists item 26 with no answer, so there is no key to compare with. Independent checks: the reaction normal to the plane follows again from the angular momentum about the vertical axis in $S_0$ (box below), and the limiting cases close the results.

> [!derivation] Independent check: angular momentum about the vertical axis
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$ the position has the components $(a\sin\theta, a(1 - \cos\theta), 0)$ and the absolute velocity $(a\dot\theta\cos\theta, a\dot\theta\sin\theta, -\Omega a\sin\theta)$. The component along $\mathbf j_1$ of a vector product is the third component of the first factor times the first of the second, minus the first of the first times the third of the second.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf j_1 &= m\left(0\cdot a\dot\theta\cos\theta - a\sin\theta\left(-\Omega a\sin\theta\right)\right) = m\Omega a^2\sin^2\theta \quad &\text{(Eq. 4.48)} \\
> \mathbf M_O\cdot\mathbf j_1 &= 0\cdot 0 - a\sin\theta\,N_b = -a\sin\theta\,N_b \quad &\text{(weight along $\mathbf j_1$, $N_n\,\mathbf e_n$ in the plane: no axial moment)} \\
> \frac{d}{dt}\left(m\Omega a^2\sin^2\theta\right) &= 2m\Omega a^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule; $\mathbf j_1$ fixed)} \\
> -a\sin\theta\,N_b &= 2m\Omega a^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(Eq. 4.53, axial component)}
> \end{aligned}$$
>
> $$\boxed{N_b = -2m\Omega a\dot\theta\cos\theta \quad (\sin\theta \ne 0)}$$
>
> **Units:** $[H] = [\mathrm{M\,L^2\,T^{-1}}]$; $[a\,N_b] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** to keep turning at the rate $\Omega$ while its distance to the axis changes, the particle needs an axial moment that only the normal reaction can give: the same result as the Coriolis balance in $S_1$.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega \to 0:\quad \ddot\theta &= -\frac{g}{a}\sin\theta, \quad N_b \to 0, \quad N_n \to \frac{mv_0^2}{a} + mg\left(3\cos\theta - 2\right) \quad &\text{(simple pendulum of length $a$, Eq. 4.38)} \\
> \Omega^2 \to \infty:\quad \cos\theta_e &= \frac{g}{a\Omega^2} \to 0, \quad \theta_e \to \pm\frac{\pi}{2} \quad &\text{(the off-axis equilibria move to the ends)} \\
> v_0 = 0:\quad \dot\theta^2 &= -\frac{2g}{a}\left(1 - \cos\theta\right) + \Omega^2\sin^2\theta \quad &\text{(zero at $\theta = 0$: the particle stays at the bottom)}
> \end{aligned}$$
>
> $$\boxed{\Omega \to 0: \text{ pendulum of length } a,\ N_b \to 0; \qquad \Omega \to \infty: \ \theta_e \to \pm\frac{\pi}{2}}$$
>
> **Units:** $[g/a] = [\mathrm{T^{-2}}]$
> **Meaning:** without rotation the wire is a pendulum and pushes nothing sideways; a very fast spin pushes the off-axis equilibria up to the ends of the wire.

---

## Problem 27: Bead on a Rotating Sine-Shaped Wire with a Spring

### Reference Frames, Bases and Coordinates

A heavy bead $P$ of mass $m$ slides without friction on a plane wire of sine shape; a vertical spring of stiffness $k$ joins it to a horizontal rail along which its upper end slides freely, and the whole setup turns about the vertical axis $Oy_1$ with the constant rate $\omega$ (Problems.pdf, p. 15). The statement asks for the relative velocity and acceleration, the three components of Newton's second law with the reaction and the equation of motion, the energy equation of the relative motion, the equilibria without rotation, and the motion without spring after a release at $x_1$ equal to $\pi$. The wire, rail and spring are at rest in the turning frame, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Wire and rail | wire $y_1 = \sin x_1$, rail $y_1 = 2$, both in the plane $Ox_1y_1$, fixed in $S_1$ |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf j_0$ vertical, up, along the axis of rotation, $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $Ox_1y_1z_1$ of the statement: $\mathbf i_1$ along $Ox_1$ in the plane of the wire, $\mathbf j_1 = \mathbf j_0$, $\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ normal to the plane; it coincides with $S_0$ at $t = 0$ and turns by $\omega t$ about $\mathbf j_0$ |
| Wire directions | $\mathbf t = \mathbf i_1 + \cos x_1\,\mathbf j_1$ (tangent, in the sense of growing $x_1$) and $\mathbf n = -\cos x_1\,\mathbf i_1 + \mathbf j_1$ (in-plane normal), both of length $\sqrt{1 + \cos^2 x_1}$ |
| Coordinate | $x_1$, the axial position of the bead |
| Constraints | $z_1 = 0$ and $y_1 = \sin x_1$: two holonomic, smooth, bilateral constraints, fixed in $S_1$ |
| Degrees of freedom | 3 minus 2: 1, the coordinate $x_1(t)$ |
| Data | $m$ [kg], $k$ [N m$^{-1}$], $g$ [m s$^{-2}$], $\omega$ [rad s$^{-1}$]; $\lambda = mg/k$ [m] (part (d)); $\beta = \omega^2/g$ [m$^{-1}$] (part (e)) |
| Unknowns | $x_1(t)$; the reaction $\mathbf N = N_x\,\mathbf i_1 + N_y\,\mathbf j_1 + N_z\,\mathbf k_1$ with $\mathbf N\cdot\mathbf t$ zero (smooth wire) |
| Applied forces | weight $-mg\,\mathbf j_1$; spring, vertical, towards the rail |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; smooth wire; massless spring with its upper end free on a smooth rail, so it stays vertical; $\omega$ constant |
| Readings | the wire equation is numerical, with $x_1$ and $y_1$ in metres (the rail at 2 m); the natural length of the spring is taken as zero, as the energy integral of the key implies (with a natural length $\ell_0$ every result below holds with 2 replaced by $2 - \ell_0$) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p27-top-view.svg]]

> [!derivation] Basis of the turning setup: rotation by omega t about j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf j_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf k_0$, the cross product of $\mathbf i_0$ and $\mathbf j_0$, points down the page (right-hand rule: fingers from $\mathbf i_0$, to the right, towards $\mathbf j_0$, towards the reader; the thumb goes down the page), so minus $\mathbf k_0$ points up the page. A positive $\omega$ turns the setup counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ up the page, along minus $\mathbf k_0$ (the minus sign). $\mathbf k_1$ is $\mathbf k_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf k_0$, opposite leg $\sin\omega t$ along plus $\mathbf i_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 - \sin\omega t\,\mathbf k_0, \quad \mathbf j_1 = \mathbf j_0, \quad \mathbf k_1 = \sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\omega t\cos\omega t - \sin\omega t\left(-\sin\omega t\right)\right) = 1 \quad &\text{(expansion along the second row, cofactor sign $(-1)^{2+2}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & 0 & \sin\omega t \cr 0 & 1 & 0 \cr -\sin\omega t & 0 & \cos\omega t \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** it is the matrix of Eq. 1.19 with the angle $\omega t$; the vertical keeps its direction, so the weight has the same components in both frames.

![[attachments/EM-SOL/p27-wire-plane.svg]]

> [!derivation] Position vector, spring length and wire directions
> **Law:** position as the sum of its components; chain rule; slope triangle; quarter turn in the plane
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.19; Notes.pdf, Eq. 3.16; Problems.pdf, p. 15
>
> The plane of the wire, fixed in $S_1$, is drawn with $\mathbf i_1$ to the right and $\mathbf j_1$ up, so $\mathbf k_1$ points out of the paper (⊙) and a quarter turn about it is counterclockwise. The bead is at the abscissa $x_1$ and at the height of the wire; the spring goes vertically from $P$ up to the rail. In the slope triangle the horizontal leg is $dx_1$ and the vertical leg $dy_1$; the hypotenuse lies along the wire, so the vector sum of the two legs divided by $dx_1$ is a tangent vector.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^P = \mathbf r_1^P = x_1\,\mathbf i_1 + \sin x_1\,\mathbf j_1 \quad &\text{(Eq. 3.16 with $O$ fixed; components of $P$)} \\
> \ell_s &= 2 - \sin x_1 \gt 0 \quad &\text{(spring length: difference of heights; $\sin x_1 \le 1$)} \\
> dy_1 &= \frac{d}{dx_1}\left(\sin x_1\right)dx_1 = \cos x_1\,dx_1 \quad &\text{(vertical leg of the slope triangle)} \\
> \mathbf t &= \frac{dx_1\,\mathbf i_1 + \cos x_1\,dx_1\,\mathbf j_1}{dx_1} = \mathbf i_1 + \cos x_1\,\mathbf j_1, \quad |\mathbf t|^2 = 1 + \cos^2 x_1 \quad &\text{(sum of the legs; Pythagoras)} \\
> \mathbf n &= \mathbf k_1\times\mathbf t = \mathbf k_1\times\mathbf i_1 + \cos x_1\,\mathbf k_1\times\mathbf j_1 = \mathbf j_1 - \cos x_1\,\mathbf i_1 \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \mathbf t\cdot\mathbf n &= -\cos x_1 + \cos x_1 = 0 \quad &\text{(orthogonal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = x_1\,\mathbf i_1 + \sin x_1\,\mathbf j_1, \quad \ell_s = 2 - \sin x_1, \quad \mathbf t = \mathbf i_1 + \cos x_1\,\mathbf j_1, \quad \mathbf n = -\cos x_1\,\mathbf i_1 + \mathbf j_1}$$
>
> **Units:** $[x_1] = [y_1] = [\ell_s] = [\mathrm{L}]$
> **Meaning:** the minus sign of $\mathbf n$: the tangent turned a quarter turn counterclockwise sends its horizontal part up and its vertical part to the left. The spring is never compressed below zero length, because the wire stays below the rail.

### Kinematics

> [!derivation] Motion of the turning frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf a_0^O = \mathbf 0 \quad &\text{(simple rotation about the fixed vertical; $\omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf j_1\times\mathbf i_1 = -\omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \omega\,\mathbf j_1\times\mathbf k_1 = \omega\,\mathbf i_1 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 - \sin\omega t\,\mathbf k_0\right) &= -\omega\sin\omega t\,\mathbf i_0 - \omega\cos\omega t\,\mathbf k_0 = -\omega\,\mathbf k_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = -\omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \omega\,\mathbf i_1}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from $S_1$ the three unit vectors are constant; seen from $S_0$ the horizontal ones turn with the setup.

#### (a) Relative velocity and acceleration

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 15
>
> $$\begin{aligned}
> \frac{d}{dt}\sin x_1 &= \cos x_1\,\dot x_1 \quad &\text{(chain rule)} \\
> \mathbf v_1^P &= \dot x_1\,\mathbf i_1 + \cos x_1\,\dot x_1\,\mathbf j_1 + 0\,\mathbf k_1 = \dot x_1\,\mathbf t \quad &\text{(components differentiated)} \\
> \frac{d}{dt}\left(\cos x_1\,\dot x_1\right) &= -\sin x_1\,\dot x_1\cdot\dot x_1 + \cos x_1\,\ddot x_1 \quad &\text{(product rule; chain rule on the cosine)} \\
> \mathbf a_1^P &= \ddot x_1\,\mathbf i_1 + \left(\cos x_1\,\ddot x_1 - \sin x_1\,\dot x_1^2\right)\mathbf j_1 + 0\,\mathbf k_1 \quad &\text{(components differentiated again)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = \left(\dot x_1,\ \cos x_1\,\dot x_1,\ 0\right), \qquad \mathbf a_1^P = \left(\ddot x_1,\ \cos x_1\,\ddot x_1 - \sin x_1\,\dot x_1^2,\ 0\right) \quad \text{in } \mathcal B_1}$$
>
> **Units:** $[\dot x_1] = [\mathrm{L\,T^{-1}}]$; $[\ddot x_1] = [\dot x_1^2] = [\mathrm{L\,T^{-2}}]$ (the arguments of sine and cosine in metres, numerically)
> **Meaning:** the relative velocity is tangent to the wire; the relative acceleration has no component normal to the plane of the wire.

> [!derivation] Absolute acceleration: transport, Coriolis and centripetal terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x_1\,\mathbf i_1 + \cos x_1\,\dot x_1\,\mathbf j_1 + x_1\left(-\omega\,\mathbf k_1\right) = \mathbf v_1^P - \omega x_1\,\mathbf k_1 \quad &\text{(product rule; derivative of $\mathbf i_1$; $\mathbf j_1$ constant)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \dot x_1\left(-\omega\,\mathbf k_1\right) \quad &\text{(product rule; the turning of $\mathbf i_1$ inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left(-\omega x_1\,\mathbf k_1\right) &= -\omega\dot x_1\,\mathbf k_1 - \omega x_1\,\omega\,\mathbf i_1 \quad &\text{(product rule; derivative of $\mathbf k_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\omega\,\mathbf j_1\times\left(\dot x_1\,\mathbf i_1 + \cos x_1\,\dot x_1\,\mathbf j_1\right) = -2\omega\dot x_1\,\mathbf k_1 \quad &\text{(the two $\mathbf k_1$ terms above)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \omega\,\mathbf j_1\times\left(-\omega x_1\,\mathbf k_1\right) = -\omega^2x_1\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - 2\omega\dot x_1\,\mathbf k_1 - \omega^2x_1\,\mathbf i_1}$$
>
> **Units:** $[\omega\dot x_1] = [\omega^2x_1] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the Coriolis term is normal to the plane of the wire and the centripetal term points horizontally to the axis; with $O$ fixed and $\omega$ constant there are no origin or Euler terms.

### Forces and Equations of Motion

The free-body diagram of the bead in $S_1$ shows, in the plane of the wire, the weight, the spring force (vertical, up to the rail), the in-plane reaction along $\mathbf n$ and the centrifugal force (horizontal, away from the axis); normal to the plane, the reaction along $\mathbf k_1$ and the Coriolis force.

![[attachments/EM-SOL/p27-fbd.svg]]

#### (b) Forces, Newton's second law, reaction and equation of motion

> [!derivation] Actual and inertia forces on the bead
> **Law:** linear spring along its length; smooth reaction normal to the tangent; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 5.1; Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.16; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> \mathbf W &= -mg\,\mathbf j_1 \quad &\text{(weight; $\mathbf j_1$ is the vertical)} \\
> \mathbf F_s &= k\,\ell_s\,\mathbf j_1 = k\left(2 - \sin x_1\right)\mathbf j_1 \quad &\text{(spring stretched by its whole length, pulling $P$ up to the rail)} \\
> \mathbf N\cdot\mathbf t &= N_x + N_y\cos x_1 = 0 \quad &\text{(smooth wire)} \\
> \mathbf F_A &= \mathbf 0, \quad \mathbf F_E = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\omega^2x_1\,\mathbf i_1, \quad \mathbf F_{COR} = -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\omega\dot x_1\,\mathbf k_1 \quad &\text{(composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf W = -mg\,\mathbf j_1, \quad \mathbf F_s = k\left(2 - \sin x_1\right)\mathbf j_1, \quad \mathbf N = N_x\,\mathbf i_1 + N_y\,\mathbf j_1 + N_z\,\mathbf k_1, \quad \mathbf F_C = m\omega^2x_1\,\mathbf i_1, \quad \mathbf F_{COR} = 2m\omega\dot x_1\,\mathbf k_1}$$
>
> **Units:** $[k\,\ell_s] = [mg] = [m\omega^2x_1] = [m\omega\dot x_1] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** four actual forces (weight, spring, two reaction components in the plane tied by the smooth condition, one normal to it) and two inertia forces.

> [!derivation] Three components of Newton's second law and their solution
> **Law:** Newton's second law in a non-inertial frame, projected on $\mathcal B_1$; elimination of the reaction
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.17; [Lecture 5, Slide 28]; Problems.pdf, p. 15
>
> $$\begin{aligned}
> \mathbf i_1:\ m\ddot x_1 &= N_x + m\omega^2x_1 \quad &\text{(horizontal, in the plane)} \\
> \mathbf j_1:\ m\left(\cos x_1\,\ddot x_1 - \sin x_1\,\dot x_1^2\right) &= N_y - mg + k\left(2 - \sin x_1\right) \quad &\text{(vertical)} \\
> \mathbf k_1:\ 0 &= N_z + 2m\omega\dot x_1 \quad &\text{(normal to the plane)} \\
> m\cos x_1\,\ddot x_1 &= -N_y\cos^2 x_1 + m\omega^2x_1\cos x_1 \quad &\text{($\mathbf i_1$ equation with $N_x = -N_y\cos x_1$, times $\cos x_1$)} \\
> -N_y\cos^2 x_1 + m\omega^2x_1\cos x_1 - m\sin x_1\,\dot x_1^2 &= N_y - mg + k\left(2 - \sin x_1\right) \quad &\text{(substituted in the $\mathbf j_1$ equation)} \\
> N_y\left(1 + \cos^2 x_1\right) &= m\left(\omega^2x_1\cos x_1 - \dot x_1^2\sin x_1\right) + mg - k\left(2 - \sin x_1\right) \quad &\text{(terms in $N_y$ collected)} \\
> m\left(1 + \cos^2 x_1\right)\ddot x_1 - m\sin x_1\cos x_1\,\dot x_1^2 &= m\omega^2x_1 - mg\cos x_1 + k\cos x_1\left(2 - \sin x_1\right) \quad &\text{($\mathbf i_1$ equation plus $\cos x_1$ times the $\mathbf j_1$ equation: the reaction cancels)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} N_y = \frac{m\left(\omega^2x_1\cos x_1 - \dot x_1^2\sin x_1\right) + mg - k\left(2 - \sin x_1\right)}{1 + \cos^2 x_1}, \quad N_x = -N_y\cos x_1, \quad N_z = -2m\omega\dot x_1 \cr m\left(1 + \cos^2 x_1\right)\ddot x_1 - m\sin x_1\cos x_1\,\dot x_1^2 = m\omega^2x_1 - mg\cos x_1 + k\cos x_1\left(2 - \sin x_1\right) \end{gathered}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three scalar equations plus the smooth condition for the four unknowns $x_1$, $N_x$, $N_y$, $N_z$. The in-plane reaction is $N_y$ times $\mathbf n$, normal to the wire; the reaction normal to the plane cancels the Coriolis force.

### Answers and Checks

#### (c) Energy of the relative motion

> [!derivation] Energy integral in the turning frame
> **Law:** power of each force on the relative velocity; potentials as minus the work along the wire, with Barrow's rule; chain rule
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Yes, it can be used, for two reasons. First, the forces that do no work in $S_1$: the reaction (smooth wire at rest in $S_1$, normal to the relative velocity), the Coriolis force (normal to the relative velocity), and the force of the origin and the Euler force, which vanish. Second, the forces that do work have potentials that depend on the position only: the weight, the spring (its upper end slides freely, so only its length matters) and the centrifugal force ($\omega$ constant). Along the wire the displacement is $\mathbf t\,dx'$.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= \dot x_1\left(N_x + N_y\cos x_1\right) = 0, \quad \mathbf F_{COR}\cdot\mathbf v_1^P = 2m\omega\dot x_1\,\mathbf k_1\cdot\dot x_1\,\mathbf t = 0 \quad &\text{(no power in $S_1$)} \\
> V_s - V_s(0) &= -\int_0^{x_1}k\left(2 - \sin x'\right)\cos x'\,dx' = \left[\tfrac12 k\left(2 - \sin x'\right)^2\right]_0^{x_1} \quad &\text{(Eq. 4.14 with $\mathbf j_1\cdot\mathbf t = \cos x'$; antiderivative by the chain rule; Barrow's rule)} \\
> V_g - V_g(0) &= -\int_0^{x_1}\left(-mg\cos x'\right)dx' = mg\left[\sin x'\right]_0^{x_1} = mg\sin x_1 \quad &\text{(Eq. 4.14; Barrow's rule)} \\
> V_C - V_C(0) &= -\int_0^{x_1}m\omega^2x'\,dx' = -\tfrac12 m\omega^2\left[x'^2\right]_0^{x_1} = -\tfrac12 m\omega^2x_1^2 \quad &\text{(Eq. 4.14 with $\mathbf i_1\cdot\mathbf t = 1$; Barrow's rule)} \\
> T_1^P &= \tfrac12 m\,\mathbf v_1^P\cdot\mathbf v_1^P = \tfrac12 m\dot x_1^2\left(1 + \cos^2 x_1\right) \quad &\text{(kinetic energy in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{E_1^P = \tfrac12 m\dot x_1^2\left(1 + \cos^2 x_1\right) + mg\sin x_1 + \tfrac12 k\left(2 - \sin x_1\right)^2 - \tfrac12 m\omega^2x_1^2 = \text{const}}$$
>
> **Units:** $[m\dot x_1^2] = [mg\,x_1] = [k\,\ell_s^2] = [m\omega^2x_1^2] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the constant is fixed by the initial position and rate. The centrifugal potential is lowest far from the axis: the rotation pushes the bead outwards.

> [!derivation] Relation of the energy equation with the equation of motion
> **Law:** time derivative of the energy along a motion; product rule and chain rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.29
>
> $$\begin{aligned}
> \frac{d}{dt}\left[\tfrac12 m\dot x_1^2\left(1 + \cos^2 x_1\right)\right] &= m\dot x_1\ddot x_1\left(1 + \cos^2 x_1\right) - m\dot x_1^3\sin x_1\cos x_1 \quad &\text{(product rule; $\tfrac{d}{dt}\cos^2 x_1 = -2\cos x_1\sin x_1\,\dot x_1$)} \\
> \frac{d}{dt}\left[mg\sin x_1 + \tfrac12 k\left(2 - \sin x_1\right)^2 - \tfrac12 m\omega^2x_1^2\right] &= \dot x_1\left[mg\cos x_1 - k\left(2 - \sin x_1\right)\cos x_1 - m\omega^2x_1\right] \quad &\text{(chain rule on each term)} \\
> \frac{dE_1^P}{dt} &= \dot x_1\left[m\left(1 + \cos^2 x_1\right)\ddot x_1 - m\sin x_1\cos x_1\,\dot x_1^2 - m\omega^2x_1 + mg\cos x_1 - k\cos x_1\left(2 - \sin x_1\right)\right] \quad &\text{(sum, factor $\dot x_1$)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_1^P}{dt} = \dot x_1\times\left(\text{equation of motion of part (b), all terms on the left}\right) = 0}$$
>
> **Units:** $[\dot x_1][\mathrm{M\,L\,T^{-2}}] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** the energy equation is a first integral of the equation of motion: it is that equation multiplied by the rate and integrated once, and differentiating it gives the equation of motion back wherever the rate is not zero.

#### (d) Equilibria without rotation

> [!derivation] Equilibrium positions for omega equal to zero
> **Law:** equilibria of a conservative system are the critical points of the potential energy
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6
>
> With $\omega$ zero the potential is the weight term plus the spring term, and the equation of motion has minus its derivative on the right-hand side.
>
> $$\begin{aligned}
> V(x_1) &= mg\sin x_1 + \tfrac12 k\left(2 - \sin x_1\right)^2 \quad &\text{(potential with $\omega = 0$)} \\
> V'(x_1) &= mg\cos x_1 - k\left(2 - \sin x_1\right)\cos x_1 = k\cos x_1\left(\lambda - 2 + \sin x_1\right) \quad &\text{(chain rule; $mg = k\lambda$)} \\
> \cos x_1 = 0 &\Rightarrow x_1 = \frac{\pi}{2},\ \frac{3\pi}{2} \quad &\text{(first factor, for every $\lambda$)} \\
> \sin x_1 = 2 - \lambda, \quad -1 \le 2 - \lambda \le 1 &\iff 1 \le \lambda \le 3 \quad &\text{(second factor, only where the sine reaches the value)} \\
> 1 \lt \lambda \lt 2:\quad x_1 &= \arcsin(2 - \lambda),\ \ \pi - \arcsin(2 - \lambda) \quad &\text{(two points on both sides of the crest)} \\
> \lambda = 2:\quad x_1 &= 0,\ \pi,\ 2\pi \quad &\text{($\sin x_1 = 0$)} \\
> 2 \lt \lambda \lt 3:\quad x_1 &= \pi + \arcsin(\lambda - 2),\ \ 2\pi - \arcsin(\lambda - 2) \quad &\text{(two points on both sides of the trough)}
> \end{aligned}$$
>
> $$\boxed{x_1 = \frac{\pi}{2} \text{ and } \frac{3\pi}{2} \text{ for every } \lambda; \qquad \sin x_1 = 2 - \lambda \text{ for } 1 \le \lambda \le 3 \ \ \left(\lambda = \frac{mg}{k}\right)}$$
>
> **Units:** $[\lambda] = [mg/k] = [\mathrm{L}]$, compared with the heights $2$ and $\sin x_1$ in metres
> **Meaning:** at the crest and at the trough the wire is horizontal, so the vertical forces need no balance along the wire; at the other points the weight and the spring force balance each other exactly, which needs a spring length equal to $\lambda$.

> [!derivation] Stability of the equilibria without rotation
> **Law:** an equilibrium is stable if and only if it is a minimum of the potential energy; second derivative, and Taylor expansion where it vanishes
> **Source:** Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> V''(x_1) &= -k\sin x_1\left(\lambda - 2 + \sin x_1\right) + k\cos^2 x_1 \quad &\text{(product rule on $V'$)} \\
> V''\left(\tfrac{\pi}{2}\right) &= -k\left(\lambda - 1\right) + 0 = k\left(1 - \lambda\right) \quad &\text{($\sin = 1$, $\cos = 0$)} \\
> V''\left(\tfrac{3\pi}{2}\right) &= k\left(\lambda - 3\right) \quad &\text{($\sin = -1$, $\cos = 0$)} \\
> \sin x_1 = 2 - \lambda:\quad V'' &= 0 + k\cos^2 x_1 \gt 0 \quad &\text{(bracket zero; $\cos x_1 \ne 0$ for $1 \lt \lambda \lt 3$)} \\
> \lambda = 1,\ u = x_1 - \tfrac{\pi}{2}:\quad V' &= k\left(-\sin u\right)\left(\cos u - 1\right) \simeq k\left(-u\right)\left(-\tfrac{u^2}{2}\right) = \tfrac12 ku^3 \quad &\text{($\cos x_1 = -\sin u$, $\sin x_1 = \cos u$; Taylor)} \\
> \lambda = 3,\ u = x_1 - \tfrac{3\pi}{2}:\quad V' &= k\sin u\left(1 - \cos u\right) \simeq k\,u\,\tfrac{u^2}{2} = \tfrac12 ku^3 \quad &\text{($\cos x_1 = \sin u$, $\sin x_1 = -\cos u$; Taylor)}
> \end{aligned}$$
>
> $$\boxed{\tfrac{\pi}{2}: \text{ stable for } \lambda \le 1,\ \text{unstable for } \lambda \gt 1; \quad \tfrac{3\pi}{2}: \text{ stable for } \lambda \ge 3,\ \text{unstable for } \lambda \lt 3; \quad \sin x_1 = 2 - \lambda: \text{ stable } (1 \lt \lambda \lt 3)}$$
>
> **Units:** $[V''] = [k] = [\mathrm{M\,T^{-2}}]$
> **Meaning:** a stiff spring (small $\lambda$) holds the bead on the crest; a heavy bead (large $\lambda$) sits in the trough; in between the bead rests on the flank where weight and spring balance. At the two limiting values the derivative grows like the cube of the distance, a minimum of fourth order: stable, with no linear restoring force.

#### (e) Motion without spring after a release at pi

> [!derivation] Dimensionless potential and allowed region
> **Law:** energy integral of part (c) with $k = 0$; the bead can only be where the potential does not exceed its initial value
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> V(x_1) &= mg\sin x_1 - \tfrac12 m\omega^2x_1^2 \quad &\text{(potential of part (c) with $k = 0$)} \\
> \tilde V(x_1) &= \frac{2V}{mg} = 2\sin x_1 - \beta x_1^2, \quad \tilde V(\pi) = -\beta\pi^2 \quad &\text{(scaled by $2/(mg)$; $\beta = \omega^2/g$)} \\
> \tfrac12 m\dot x_1^2\left(1 + \cos^2 x_1\right) &= V(\pi) - V(x_1) \quad &\text{(energy integral; released at rest at $\pi$)} \\
> \frac{\dot x_1^2}{g}\left(1 + \cos^2 x_1\right) &= \tilde V(\pi) - \tilde V(x_1) \quad &\text{(divided by $mg/2$)} \\
> \tilde V'(\pi) &= 2\cos\pi - 2\beta\pi = -2\left(1 + \beta\pi\right) \lt 0 \quad &\text{(the generalized force minus $V'$ is positive at the start)}
> \end{aligned}$$
>
> $$\boxed{\tilde V(x_1) = 2\sin x_1 - \beta x_1^2, \qquad \frac{\dot x_1^2}{g}\left(1 + \cos^2 x_1\right) = \tilde V(\pi) - \tilde V(x_1)}$$
>
> **Units:** $[\tilde V] = [\beta x_1^2] = [\mathrm{L}]$
> **Meaning:** the bead starts towards larger $x_1$, down the wire into the trough near three halves of $\pi$; it moves only where the scaled potential lies below its starting value.

![[attachments/EM-SOL/p27-potential.svg]]

> [!derivation] Small and large beta: oscillation or escape
> **Law:** comparison of the potential beyond the start with its starting value; sign of its derivative
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Sec. 4.6
>
> The scaled potential is a sine of amplitude 2 riding on the downward parabola of the centrifugal term: wells near the troughs, humps near the crests, and it tends to minus infinity far from the axis. The bead is trapped if some point beyond $\pi$ has a potential at least equal to the starting value; it escapes if the potential decreases all the way.
>
> $$\begin{aligned}
> \tilde V\left(\tfrac{5\pi}{2}\right) - \tilde V(\pi) &= 2 - \beta\frac{25\pi^2}{4} + \beta\pi^2 = 2 - \frac{21\pi^2}{4}\beta \quad &\text{($\sin(5\pi/2) = 1$)} \\
> \beta \lt \frac{8}{21\pi^2} = 0.0386\ \mathrm{m^{-1}} &\Rightarrow \tilde V\left(\tfrac{5\pi}{2}\right) \gt \tilde V(\pi) \quad &\text{(the hump near the next crest is higher than the start: a turning point before it)} \\
> \beta\pi \ge 1,\ x_1 \gt \pi:\quad \tilde V'(x_1) &= 2\left(\cos x_1 - \beta x_1\right) \lt 2\left(1 - \beta\pi\right) \le 0 \quad &\text{($\cos x_1 \le 1$, $\beta x_1 \gt \beta\pi$)} \\
> \beta = 0.02\ \mathrm{m^{-1}}:\quad \tilde V(\pi) &= -0.197\ \mathrm{m}, \quad \tilde V\left(\tfrac{3\pi}{2}\right) = -2.444\ \mathrm{m}, \quad \tilde V\left(\tfrac{5\pi}{2}\right) = 0.766\ \mathrm{m} \quad &\text{(example of a small value)} \\
> \beta = 0.1\ \mathrm{m^{-1}}:\quad \tilde V(\pi) &= -0.987\ \mathrm{m}, \quad \tilde V\left(\tfrac{3\pi}{2}\right) = -4.221\ \mathrm{m}, \quad \tilde V\left(\tfrac{5\pi}{2}\right) = -4.169\ \mathrm{m} \quad &\text{(example of a larger value)}
> \end{aligned}$$
>
> $$\boxed{\beta \text{ small: periodic oscillation between } \pi \text{ and a turning point beyond the trough}; \qquad \beta \text{ large: } x_1 \to \infty}$$
>
> **Units:** $[\beta] = [\mathrm{L^{-1}}]$; $[\tilde V] = [\mathrm{L}]$
> **Meaning:** slow rotation: gravity keeps the bead in the well of the trough, and it swings back to the release point, where it stops and starts again. Fast rotation: the centrifugal term lowers every hump below the start and throws the bead outwards along the wire. For the larger example the next hump, at 7.069 m, has the value $-3.582$ m, below the start: escape.

> [!derivation] System for the critical value of beta
> **Law:** the separating case has a maximum of the potential exactly at the starting level
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Sec. 4.6; Problems.pdf, p. 15
>
> At the critical value the bead creeps towards the top $x_c$ of the first hump beyond $\pi$, where the potential is stationary and equal to its starting value.
>
> $$\begin{aligned}
> \tilde V(x_c) &= 2\sin x_c - \beta_c x_c^2 = -\beta_c\pi^2 \quad &\text{(the top at the starting level)} \\
> \tilde V'(x_c) &= 2\cos x_c - 2\beta_c x_c = 0 \quad &\text{(stationary)} \\
> \tilde V''(x_c) &= -2\sin x_c - 2\beta_c \lt 0 \quad &\text{(a maximum; $x_c \gt \pi$)} \\
> x_c &= 7.5436\ \mathrm{m} = 2.4012\pi, \quad \beta_c = 0.040489\ \mathrm{m^{-1}}, \quad \tilde V''(x_c) = -1.985\ \mathrm{m^{-1}} \quad &\text{(numerical solution: Newton's method from the starting values 7.5 and 0.04)} \\
> \beta = 0.95\beta_c:\ \max\tilde V &= -0.284\ \mathrm{m} \gt \tilde V(\pi) = -0.380\ \mathrm{m}; \quad \beta = 1.05\beta_c:\ \max\tilde V = -0.515\ \mathrm{m} \lt \tilde V(\pi) = -0.420\ \mathrm{m} \quad &\text{(top of the hump against the start, on both sides)}
> \end{aligned}$$
>
> $$\boxed{\begin{cases} 2\sin x_c - \beta_c x_c^2 = -\beta_c\pi^2 \cr \cos x_c - \beta_c x_c = 0 \end{cases} \quad x_c \simeq 7.544\ \mathrm{m}, \ \ \beta_c \simeq 0.0405\ \mathrm{m^{-1}}: \ \ \beta \lt \beta_c \text{ oscillation}, \ \beta \gt \beta_c \text{ escape}}$$
>
> **Units:** $[\beta_c x_c^2] = [\mathrm{L}]$; $[\beta_c x_c] = [1]$
> **Meaning:** just below the critical value the hump still stands above the start and the bead turns back; just above it the hump is below the start and the bead passes over it.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Relative velocity and acceleration | $\mathbf v_1^P = (\dot x_1,\ \cos x_1\,\dot x_1,\ 0)$, $\mathbf a_1^P = (\ddot x_1,\ \cos x_1\,\ddot x_1 - \sin x_1\,\dot x_1^2,\ 0)$ in $\mathcal B_1$ |
| (b) Forces | weight $-mg\,\mathbf j_1$, spring $k(2 - \sin x_1)\,\mathbf j_1$, reaction $(N_x, N_y, N_z)$ with $N_x + N_y\cos x_1 = 0$, centrifugal $m\omega^2x_1\,\mathbf i_1$, Coriolis $2m\omega\dot x_1\,\mathbf k_1$ |
| (b) Newton, three components | $m\ddot x_1 = N_x + m\omega^2x_1$; $m(\cos x_1\,\ddot x_1 - \sin x_1\,\dot x_1^2) = N_y - mg + k(2 - \sin x_1)$; $0 = N_z + 2m\omega\dot x_1$ |
| (b) Reaction | $N_y = [m(\omega^2x_1\cos x_1 - \dot x_1^2\sin x_1) + mg - k(2 - \sin x_1)]/(1 + \cos^2 x_1)$, $N_x = -N_y\cos x_1$, $N_z = -2m\omega\dot x_1$ |
| (b) Equation of motion | $m(1 + \cos^2 x_1)\ddot x_1 - m\sin x_1\cos x_1\,\dot x_1^2 = m\omega^2x_1 - mg\cos x_1 + k\cos x_1(2 - \sin x_1)$ |
| (c) Energy | yes: $\frac12 m\dot x_1^2(1 + \cos^2 x_1) + mg\sin x_1 + \frac12 k(2 - \sin x_1)^2 - \frac12 m\omega^2x_1^2 = $ const; it is the first integral of the equation of motion (its time derivative is the rate times that equation) |
| (d) Equilibria, $\omega = 0$ | $\pi/2$ (stable for $\lambda \le 1$), $3\pi/2$ (stable for $\lambda \ge 3$), $\sin x_1 = 2 - \lambda$ for $1 \lt \lambda \lt 3$ (stable) |
| (e) Motion, $k = 0$ | $\tilde V = 2\sin x_1 - \beta x_1^2$; small $\beta$: oscillation; large $\beta$: escape to infinity; critical value from $2\sin x_c - \beta_c x_c^2 = -\beta_c\pi^2$, $\cos x_c = \beta_c x_c$ ($x_c \simeq 7.544$ m, $\beta_c \simeq 0.0405$ m$^{-1}$) |
| Reading of the spring | natural length zero; with a natural length $\ell_0$, replace 2 by $2 - \ell_0$ in the spring terms |

**Check against the official key:** Problems.pdf, p. 74 prints the energy integral, the reaction, the equilibria for zero rotation and the system for the critical value. The energy integral and the reaction coincide (box below). The equilibria coincide after a change of parameter: the key writes them with a parameter $\alpha$ that the statement does not define, and its statements match these results exactly when $\alpha$ is the reciprocal of $\lambda$ (box below). The system for the critical value coincides, but the key assigns the two behaviours the other way round: see the warning.

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison; expansion of the spring potential; change of parameter
> **Source:** Problems.pdf, p. 74
>
> $$\begin{aligned}
> \tfrac12 k\left(2 - \sin x_1\right)^2 &= 2k - 2k\sin x_1 + \tfrac12 k\sin^2 x_1 \quad &\text{(square expanded)} \\
> \text{key: } \tfrac12 m\dot x_1^2\left(1 + \cos^2 x_1\right) + \sin x_1\left(mg - 2k\right) + \tfrac12 k\sin^2 x_1 - \tfrac12 m\omega^2x_1^2 &= C \quad &\text{(part (c) with the constant $2k$ moved into $C$)} \\
> \text{key: } \mathbf N_1 &= \frac{m\left(\omega^2x_1\cos x_1 - \dot x_1^2\sin x_1\right) - k\left(2 - \sin x_1\right) + mg}{1 + \cos^2 x_1}\left(-\cos x_1\,\mathbf i_1 + \mathbf j_1\right), \quad \mathbf N_2 = -2m\omega\dot x_1\,\mathbf k_1 \quad &\text{(part (b); the key prints $\cos x$ for $\cos x_1$ in the direction)} \\
> \alpha &= \frac{1}{\lambda} = \frac{k}{mg} \quad &\text{(reading of the parameter of the key)} \\
> \alpha \gt 1 \iff \lambda \lt 1, \quad \alpha \lt \tfrac13 &\iff \lambda \gt 3, \quad 2 - \tfrac{1}{\alpha} = 2 - \lambda, \quad \tfrac13 \lt \alpha \lt 1 \iff 1 \lt \lambda \lt 3 \quad &\text{(the three statements of the key converted)} \\
> \text{key: } \alpha = 0 &\iff k = 0 \quad &\text{(the case of part (e), consistent with the same reading)}
> \end{aligned}$$
>
> $$\boxed{\text{energy integral, reaction and equilibria coincide, with } \alpha = k/(mg) = 1/\lambda}$$
>
> **Units:** $[\alpha] = [\mathrm{L^{-1}}]$
> **Meaning:** the key's stability statements are the ones of part (d) written with the reciprocal parameter; at the limiting values $\lambda$ equal to 1 and 3 this solution also finds stability (fourth-order minimum), which the key, with strict inequalities, leaves out.

> [!warning] Discrepancy with the official solution
> The key states "$\beta \gt \beta_c$, the bead oscillates; $\beta \lt \beta_c$, the bead moves towards infinity", with the same system of equations for $x_c$ and $\beta_c$. This solution obtains the opposite assignment: the bead oscillates for $\beta \lt \beta_c$ and escapes for $\beta \gt \beta_c$. Proof, from the boxes above: for any $\beta$ with $\beta\pi \ge 1$ the scaled potential decreases for every $x_1$ beyond $\pi$, so the bead escapes; for $\beta$ below $8/(21\pi^2)$ the potential at five halves of $\pi$ is above the start, so the bead turns back. At $0.95\beta_c$ the top of the hump is $-0.284$ m, above the start, $-0.380$ m; at $1.05\beta_c$ it is $-0.515$ m, below the start, $-0.420$ m. The centrifugal term is the only one that pushes the bead outwards, so a faster spin cannot be the one that keeps it.

> [!derivation] Independent check: angular momentum about the vertical axis
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$ the position has the components $(x_1, \sin x_1, 0)$ and the absolute velocity $(\dot x_1, \cos x_1\,\dot x_1, -\omega x_1)$. The component along $\mathbf j_1$ of a vector product is the third component of the first factor times the first of the second, minus the first of the first times the third of the second.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf j_1 &= m\left(0\cdot\dot x_1 - x_1\left(-\omega x_1\right)\right) = m\omega x_1^2 \quad &\text{(Eq. 4.48)} \\
> \mathbf M_O\cdot\mathbf j_1 &= 0\cdot N_x - x_1N_z = -x_1N_z \quad &\text{(weight and spring along $\mathbf j_1$; in-plane reaction in the plane: no axial moment)} \\
> 2m\omega x_1\dot x_1 &= -x_1N_z \quad &\text{(Eq. 4.53, axial component; chain rule)}
> \end{aligned}$$
>
> $$\boxed{N_z = -2m\omega\dot x_1 \quad (x_1 \ne 0)}$$
>
> **Units:** $[x_1N_z] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the reaction normal to the plane is the one that keeps the bead turning with the wire while its distance to the axis changes: the same value as the Coriolis balance of part (b).

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> \omega \to 0:\quad N_z &\to 0, \quad m\left(1 + \cos^2 x_1\right)\ddot x_1 - m\sin x_1\cos x_1\,\dot x_1^2 = -mg\cos x_1 + k\cos x_1\left(2 - \sin x_1\right) \quad &\text{(bead on a fixed wire)} \\
> k \to 0\ (\lambda \to \infty):\quad \lambda - 3 &\gt 0, \quad 1 - \lambda \lt 0 \quad &\text{(stability boxes: the trough stable, the crest unstable)} \\
> k \to \infty\ (\lambda \to 0):\quad 1 - \lambda &\gt 0, \quad \lambda - 3 \lt 0 \quad &\text{(the crest stable, the trough unstable)}
> \end{aligned}$$
>
> $$\boxed{\omega \to 0: \ N_z \to 0; \qquad k \to 0: \text{ trough stable}; \qquad k \to \infty: \text{ crest stable}}$$
>
> **Units:** $[\lambda] = [\mathrm{L}]$
> **Meaning:** without spring the bead rests in the trough like any heavy bead; with a very stiff spring it is held on the crest, nearest to the rail.

---

## Problem 28: Spherical Pendulum with a Vertically Oscillating Suspension Point

### Reference Frames, Bases and Coordinates

A particle $P$ of mass $m$ hangs from a massless cord of length $L$ fixed at the point $A$, which oscillates on the vertical axis of the fixed frame with the height $a\sin\omega t$; in the frame $Ax'y'z'$ the particle is located by the angles $\varphi$ and $\theta$ of the figure, and the statement gives the spherical unit vectors, their partial derivatives and the initial values of the angles and rates (Problems.pdf, p. 16). The statement asks to show the relative acceleration, to write the equations of motion with the tension, and to evaluate the relative acceleration and the tension at the start. The frame $Ax'y'z'$ translates without turning, so the composition of motions of Notes.pdf, Sec. 3.2 reduces to Eq. 3.28 and Eq. 3.29, and the only inertia force of Notes.pdf, Sec. 4.9 is the force of the origin.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, the frame $Oxyz$, $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$ of the statement, $\mathbf k$ vertical, up (Notes.pdf, Eq. 2.1) |
| Moving frame | $S_1 = \{A;\ \mathcal B_1\}$, the frame $Ax'y'z'$; its axes stay parallel to those of $Oxyz$ (figure of the statement), so $\mathcal B_1 = \mathcal B_0$ |
| Spherical basis | $\mathcal B_s = \{\mathbf e_r, \mathbf e_\varphi, \mathbf e_\theta\}$ of the statement, attached to $P$ |
| Coordinates | $\varphi$, the angle from the upward axis $Az'$ to the cord $AP$ (figure, and $\mathbf e_r\cdot\mathbf k = \cos\varphi$); $\theta$, the azimuth of the vertical plane of the cord, from $Ax'$, counterclockwise seen from above |
| Constraint | $P$ at the distance $L$ from $A$ (taut cord) |
| Degrees of freedom | 3 minus 1: 2, the angles $\varphi(t)$ and $\theta(t)$; the motion of $A$ is prescribed |
| Data | $m$ [kg], $L$ [m], $a$ [m], $\omega$ [rad s$^{-1}$] (the frequency of the oscillation of $A$, not a rotation of the frame), $g$ [m s$^{-2}$] |
| Initial state | $\theta_0 = 0$, $\varphi_0 = 30^\circ$, $\dot\theta_0 = \sqrt{2g/(\sqrt3 L)}$, $\dot\varphi_0 = 0$ (relative values) |
| Unknowns | $\varphi(t)$, $\theta(t)$ and the tension $T(t)$, positive when the cord pulls $P$ towards $A$ |
| Applied forces | weight $-mg\,\mathbf k$; cord $-T\,\mathbf e_r$ |
| Inertia force (in $S_1$) | of the origin only (Notes.pdf, Eq. 4.62 with zero angular velocity) |
| Hypotheses | $S_0$ inertial; uniform gravity; massless cord, taut as long as $T \ge 0$; no friction or drag |
| Reading | the statement as written ($\varphi$ from the upward vertical, $P$ above the horizontal plane of $A$ at the start). The other reading, $\varphi$ from the downward vertical (a conical pendulum hanging below $A$, for which the given $\dot\theta_0$ is the steady rate), is worked out in the Answers section and listed in the table |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p28-meridian.svg]]

> [!derivation] Translation of the moving frame
> **Law:** a frame whose axes stay parallel to the fixed ones: identity change of basis, zero angular velocity; position, velocity and acceleration of its origin
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 3.16; Notes.pdf, Eq. 3.28; Notes.pdf, Eq. 3.29; Problems.pdf, p. 16
>
> $$\begin{aligned}
> [{}_0R_1] &= I, \quad \det I = 1, \quad I\,I^T = I, \quad \boldsymbol\omega_{10} = \mathbf 0, \quad \boldsymbol\alpha_{10} = \mathbf 0 \quad &\text{($\mathcal B_1 = \mathcal B_0$)} \\
> \mathbf r_0^A &= \overrightarrow{OA} = a\sin\omega t\,\mathbf k \quad &\text{($A$ on the fixed vertical axis)} \\
> \mathbf v_0^A &= a\omega\cos\omega t\,\mathbf k \quad &\text{(chain rule: $\tfrac{d}{dt}\sin\omega t = \omega\cos\omega t$)} \\
> \mathbf a_0^A &= -a\omega^2\sin\omega t\,\mathbf k \quad &\text{(chain rule: $\tfrac{d}{dt}\cos\omega t = -\omega\sin\omega t$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = I, \quad \boldsymbol\omega_{10} = \mathbf 0, \quad \mathbf r_0^A = a\sin\omega t\,\mathbf k, \quad \mathbf a_0^A = -a\omega^2\sin\omega t\,\mathbf k}$$
>
> **Units:** $[a\omega^2] = [\mathrm{L\,T^{-2}}]$; $[\omega t] = [1]$
> **Meaning:** the frame of $A$ only translates up and down; at the start $A$ passes through $O$ with zero acceleration.

> [!derivation] Position of the particle: meridian triangle and azimuth
> **Law:** right triangle of the cord in its vertical plane; right triangle of the horizontal projection; relation with the standard polar angle; position as a sum of segments
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 3.16; Problems.pdf, p. 16
>
> First figure: the vertical plane through $Az'$ and the cord, with $\mathbf u$ its horizontal unit vector from the axis towards $P$. In the shaded right triangle the hypotenuse is the cord $L$; the angle $\varphi$ is at $A$, measured from the upward vertical, so the adjacent leg is vertical, $L\cos\varphi$ along $\mathbf k$, and the opposite leg is horizontal, $L\sin\varphi$ along $\mathbf u$. The standard polar angle of $P$ in that plane, measured from $\mathbf u$, is $\pi/2 - \varphi$. Second figure (below): the view from above, $\mathbf k$ out of the paper (⊙), $Ax'$ to the right and $Ay'$ up; the horizontal projection, of length $L\sin\varphi$, makes the azimuth $\theta$ with $Ax'$: adjacent leg along $\mathbf i$, opposite leg along $\mathbf j$.
>
> $$\begin{aligned}
> \overrightarrow{AP} &= L\sin\varphi\,\mathbf u + L\cos\varphi\,\mathbf k \quad &\text{(legs of the meridian triangle)} \\
> \cos\left(\tfrac{\pi}{2} - \varphi\right) &= \cos\tfrac{\pi}{2}\cos\varphi + \sin\tfrac{\pi}{2}\sin\varphi = \sin\varphi, \quad \sin\left(\tfrac{\pi}{2} - \varphi\right) = \sin\tfrac{\pi}{2}\cos\varphi - \cos\tfrac{\pi}{2}\sin\varphi = \cos\varphi \quad &\text{(difference formulas: the polar form gives the same legs)} \\
> \mathbf u &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(legs of the projection divided by $L\sin\varphi$)} \\
> \mathbf r_1^P &= L\left(\sin\varphi\cos\theta\,\mathbf i + \sin\varphi\sin\theta\,\mathbf j + \cos\varphi\,\mathbf k\right) = L\,\mathbf e_r \quad &\text{($\mathbf u$ substituted; the $\mathbf e_r$ of the statement)} \\
> \mathbf r_0^P &= \mathbf r_0^A + \mathbf r_1^P = a\sin\omega t\,\mathbf k + L\,\mathbf e_r \quad &\text{(Eq. 3.16)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = L\,\mathbf e_r = L\left(\sin\varphi\cos\theta\,\mathbf i + \sin\varphi\sin\theta\,\mathbf j + \cos\varphi\,\mathbf k\right), \qquad \mathbf r_0^P = a\sin\omega t\,\mathbf k + L\,\mathbf e_r}$$
>
> **Units:** $[L] = [a] = [\mathrm{L}]$; angles dimensionless
> **Meaning:** with $\varphi$ below a right angle the vertical component $\cos\varphi$ is positive: at the start, with $\varphi$ equal to 30 degrees, the particle is above the horizontal plane through $A$, as drawn in the figure of the statement.

![[attachments/EM-SOL/p28-azimuth.svg]]

> [!derivation] Spherical basis: rotation by theta about k, then by phi; matrix and partial derivatives
> **Law:** unit vectors as normalised partial derivatives of the position; change of basis matrix, its determinant by cofactors, orthonormality; partial derivatives of each component
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 2.32; Notes.pdf, Eq. 2.34; Problems.pdf, p. 16
>
> $\mathbf e_\varphi$ is the direction in which $P$ moves when $\varphi$ grows: in the meridian plane, perpendicular to the cord, pointing down and away from the axis (the minus sign of its $\mathbf k$ component: $\varphi$ is measured from the upward vertical, so a growing $\varphi$ lowers the particle). $\mathbf e_\theta$ is $\mathbf u$ turned by a quarter turn counterclockwise about $\mathbf k$ in the view from above (⊙): the horizontal part $\cos\theta\,\mathbf i$ turns into $\cos\theta\,\mathbf j$, and $\sin\theta\,\mathbf j$ turns into minus $\sin\theta\,\mathbf i$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf e_\varphi &= \frac{\partial\mathbf e_r}{\partial\varphi} = \cos\varphi\cos\theta\,\mathbf i + \cos\varphi\sin\theta\,\mathbf j - \sin\varphi\,\mathbf k \quad &\text{($\tfrac{\partial}{\partial\varphi}\sin\varphi = \cos\varphi$, $\tfrac{\partial}{\partial\varphi}\cos\varphi = -\sin\varphi$; length 1)} \\
> \frac{\partial\mathbf e_r}{\partial\theta} &= \sin\varphi\left(-\sin\theta\,\mathbf i + \cos\theta\,\mathbf j\right) = \sin\varphi\,\mathbf e_\theta \quad &\text{(length $\sin\varphi$; $\mathbf e_\theta$ its direction)} \\
> \det[{}_1R_s] &= \cos\varphi\cdot(+1)\left(\cos\varphi\cos^2\theta + \cos\varphi\sin^2\theta\right) + \left(-\sin\varphi\right)\cdot(-1)\left(\sin\varphi\cos^2\theta + \sin\varphi\sin^2\theta\right) + 0 = 1 \quad &\text{(expansion along the third row, cofactor signs $+$, $-$, $+$)} \\
> \mathbf e_r\cdot\mathbf e_\varphi &= \sin\varphi\cos\varphi\left(\cos^2\theta + \sin^2\theta\right) - \cos\varphi\sin\varphi = 0, \quad \mathbf e_r\cdot\mathbf e_\theta = \sin\varphi\left(-\cos\theta\sin\theta + \sin\theta\cos\theta\right) = 0 \quad &\text{(columns orthogonal; $\mathbf e_\varphi\cdot\mathbf e_\theta$ likewise)} \\
> \frac{\partial\mathbf e_\varphi}{\partial\varphi} &= -\sin\varphi\cos\theta\,\mathbf i - \sin\varphi\sin\theta\,\mathbf j - \cos\varphi\,\mathbf k = -\mathbf e_r, \quad \frac{\partial\mathbf e_\varphi}{\partial\theta} = \cos\varphi\,\mathbf e_\theta \quad &\text{(component by component)} \\
> \frac{\partial\mathbf e_\theta}{\partial\theta} &= -\cos\theta\,\mathbf i - \sin\theta\,\mathbf j = -\left(\sin\varphi\,\mathbf e_r + \cos\varphi\,\mathbf e_\varphi\right), \quad \frac{\partial\mathbf e_\theta}{\partial\varphi} = \mathbf 0 \quad &\text{($\sin\varphi\,\mathbf e_r + \cos\varphi\,\mathbf e_\varphi = \mathbf u$)} \\
> \mathbf k &= \cos\varphi\,\mathbf e_r - \sin\varphi\,\mathbf e_\varphi \quad &\text{(third row of the matrix: the vertical in the spherical basis)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_s] = \begin{pmatrix} \sin\varphi\cos\theta & \cos\varphi\cos\theta & -\sin\theta \cr \sin\varphi\sin\theta & \cos\varphi\sin\theta & \cos\theta \cr \cos\varphi & -\sin\varphi & 0 \end{pmatrix}, \quad \det[{}_1R_s] = 1, \quad \mathbf k = \cos\varphi\,\mathbf e_r - \sin\varphi\,\mathbf e_\varphi}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** these are the vectors and the six partial derivatives given in the statement; the last row writes the vertical along the cord and across it, the two legs of the meridian triangle.

### Kinematics

#### (a) Relative acceleration

> [!derivation] Relative velocity and relative acceleration in the translating frame
> **Law:** time derivatives in $S_1$; multivariable chain rule through $\varphi(t)$ and $\theta(t)$; product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Notes.pdf, Eq. 2.33; Problems.pdf, p. 16
>
> The vectors $\mathbf i$, $\mathbf j$, $\mathbf k$ are constant in $S_1$; each spherical vector depends on time through the two angles, so its rate is the partial derivative with respect to $\varphi$ times the rate of $\varphi$ plus the one with respect to $\theta$ times the rate of $\theta$.
>
> $$\begin{aligned}
> \dot{\mathbf e}_r &= \frac{\partial\mathbf e_r}{\partial\varphi}\dot\varphi + \frac{\partial\mathbf e_r}{\partial\theta}\dot\theta = \dot\varphi\,\mathbf e_\varphi + \dot\theta\sin\varphi\,\mathbf e_\theta \quad &\text{(chain rule)} \\
> \dot{\mathbf e}_\varphi &= -\dot\varphi\,\mathbf e_r + \dot\theta\cos\varphi\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = -\dot\theta\left(\sin\varphi\,\mathbf e_r + \cos\varphi\,\mathbf e_\varphi\right) \quad &\text{(chain rule)} \\
> \mathbf v_1^P &= L\,\dot{\mathbf e}_r = L\dot\varphi\,\mathbf e_\varphi + L\dot\theta\sin\varphi\,\mathbf e_\theta \quad &\text{($L$ constant)} \\
> \frac{d}{dt}\left(L\dot\varphi\,\mathbf e_\varphi\right) &= L\ddot\varphi\,\mathbf e_\varphi - L\dot\varphi^2\,\mathbf e_r + L\dot\varphi\dot\theta\cos\varphi\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \frac{d}{dt}\left(L\dot\theta\sin\varphi\,\mathbf e_\theta\right) &= L\ddot\theta\sin\varphi\,\mathbf e_\theta + L\dot\theta\cos\varphi\,\dot\varphi\,\mathbf e_\theta - L\dot\theta^2\sin\varphi\left(\sin\varphi\,\mathbf e_r + \cos\varphi\,\mathbf e_\varphi\right) \quad &\text{(product rule on three factors; $\tfrac{d}{dt}\sin\varphi = \cos\varphi\,\dot\varphi$)} \\
> \mathbf a_1^P &= -L\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right)\mathbf e_r + L\left(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi\right)\mathbf e_\varphi + L\left(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi\right)\mathbf e_\theta \quad &\text{(sum, collected by unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a'_P \equiv \mathbf a_1^P = -L\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right)\mathbf e_r + L\left(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi\right)\mathbf e_\varphi + L\left(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi\right)\mathbf e_\theta}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** this is the expression of the statement: along the cord the centripetal part of the motion on the sphere; across it, the angular accelerations with the centrifugal and the Coriolis-like terms of the spherical coordinates.

> [!derivation] Absolute acceleration in a translating frame
> **Law:** time derivative in $S_0$ of the position; the basis of $S_1$ is constant in $S_0$
> **Source:** Notes.pdf, Eq. 3.28; Notes.pdf, Eq. 3.29; Notes.pdf, Eq. 3.27
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(a\sin\omega t\,\mathbf k\right) + \frac{d}{dt}\left(L\,\mathbf e_r\right) = \mathbf v_0^A + \mathbf v_1^P \quad &\text{(the derivative of $L\,\mathbf e_r$ is the same in $S_0$ and $S_1$: $\mathcal B_1 = \mathcal B_0$)} \\
> \mathbf a_0^P &= \mathbf a_0^A + \mathbf a_1^P \quad &\text{(once more; Eq. 3.27 with zero $\boldsymbol\omega_{10}$ and $\boldsymbol\alpha_{10}$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = -a\omega^2\sin\omega t\,\mathbf k + \mathbf a_1^P}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** no Euler, centrifugal or Coriolis terms: the frame does not turn.

### Forces and Equations of Motion

The free-body diagram of $P$ in $S_1$ shows the pull of the cord towards $A$, the weight and the inertia force of the origin, both vertical. Weight and inertia force add up to an effective weight with a gravity that changes in time.

![[attachments/EM-SOL/p28-fbd.svg]]

> [!derivation] Forces in the translating frame and effective gravity
> **Law:** inertia force of the origin of a translating frame
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^A = ma\omega^2\sin\omega t\,\mathbf k, \quad \mathbf F_E = \mathbf F_C = \mathbf F_{COR} = \mathbf 0 \quad &\text{(Eq. 4.62 with zero $\boldsymbol\omega_{10}$)} \\
> -mg\,\mathbf k + ma\omega^2\sin\omega t\,\mathbf k &= -m\left(g - a\omega^2\sin\omega t\right)\mathbf k = -mg_e\,\mathbf k \quad &\text{(weight plus inertia force)} \\
> -mg_e\,\mathbf k &= -mg_e\cos\varphi\,\mathbf e_r + mg_e\sin\varphi\,\mathbf e_\varphi \quad &\text{($\mathbf k$ in the spherical basis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_A = ma\omega^2\sin\omega t\,\mathbf k, \qquad g_e(t) = g - a\omega^2\sin\omega t}$$
>
> **Units:** $[a\omega^2] = [g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** in the frame of $A$ the oscillation of the support only changes the strength of gravity: weaker while $A$ is above $O$, stronger while it is below, and reversed whenever the product $a\omega^2\sin\omega t$ exceeds $g$.

#### (b) Equations of motion and tension

> [!derivation] Newton's second law in the translating frame, projected on the spherical basis
> **Law:** Newton's second law in a non-inertial frame with the inertia force of the origin
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; Problems.pdf, p. 16
>
> $$\begin{aligned}
> m\,\mathbf a_1^P &= -T\,\mathbf e_r - mg\,\mathbf k + \mathbf F_A = -T\,\mathbf e_r - mg_e\,\mathbf k \quad &\text{(Eq. 4.63)} \\
> \mathbf e_r:\ -mL\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right) &= -T - mg_e\cos\varphi \quad &\text{(along the cord)} \\
> \mathbf e_\varphi:\ mL\left(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi\right) &= mg_e\sin\varphi \quad &\text{(in the meridian plane, across the cord)} \\
> \mathbf e_\theta:\ mL\left(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi\right) &= 0 \quad &\text{(horizontal, normal to the meridian plane)}
> \end{aligned}$$
>
> $$\boxed{\begin{cases} \ddot\varphi = \dot\theta^2\sin\varphi\cos\varphi + \dfrac{g - a\omega^2\sin\omega t}{L}\sin\varphi \cr \ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi = 0 \cr T = mL\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right) - m\left(g - a\omega^2\sin\omega t\right)\cos\varphi \end{cases}}$$
>
> **Units:** $[\dot\theta^2] = [g/L] = [\mathrm{T^{-2}}]$; $[mL\dot\theta^2] = [mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three equations for the three unknowns: the first two, with the initial values, give the two angles; the third then gives the tension.

> [!derivation] First integral of the azimuth equation
> **Law:** the azimuth equation times $\sin\varphi$ is an exact derivative (product rule); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\dot\theta\sin^2\varphi\right) &= \ddot\theta\sin^2\varphi + \dot\theta\cdot 2\sin\varphi\cos\varphi\,\dot\varphi \quad &\text{(product rule; chain rule on $\sin^2\varphi$)} \\
> &= \sin\varphi\left(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi\right) = 0 \quad &\text{(second equation of the system)} \\
> \left[\dot\theta\sin^2\varphi\right]_0^t &= 0 \Rightarrow \dot\theta\sin^2\varphi = \dot\theta_0\sin^2\varphi_0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{mL^2\dot\theta\sin^2\varphi = mL^2\dot\theta_0\sin^2\varphi_0}$$
>
> **Units:** $[mL^2\dot\theta] = [\mathrm{M\,L^2\,T^{-1}}]$, an angular momentum
> **Meaning:** it is the vertical component of the relative angular momentum about $A$: the tension passes through $A$ and the effective weight is vertical, so neither has a moment about the vertical through $A$.

### Answers and Checks

#### (c) Relative acceleration at the start

> [!derivation] Angular accelerations and relative acceleration at t equal to zero
> **Law:** the system of part (b) and the expression of part (a) evaluated at the initial instant
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 16
>
> $$\begin{aligned}
> g_e(0) &= g - a\omega^2\sin 0 = g, \quad \sin\varphi_0 = \tfrac12, \quad \cos\varphi_0 = \tfrac{\sqrt3}{2}, \quad \dot\theta_0^2 = \frac{2g}{\sqrt3 L} \quad &\text{(data)} \\
> \ddot\varphi_0 &= \frac{2g}{\sqrt3 L}\cdot\frac12\cdot\frac{\sqrt3}{2} + \frac{g}{L}\cdot\frac12 = \frac{g}{2L} + \frac{g}{2L} = \frac{g}{L} \quad &\text{(first equation)} \\
> \ddot\theta_0\cdot\tfrac12 &= -2\dot\theta_0\cdot 0\cdot\tfrac{\sqrt3}{2} = 0 \Rightarrow \ddot\theta_0 = 0 \quad &\text{(second equation; $\dot\varphi_0 = 0$)} \\
> \dot\theta_0^2\sin^2\varphi_0 &= \frac{2g}{\sqrt3 L}\cdot\frac14 = \frac{g}{2\sqrt3 L}, \quad \dot\theta_0^2\sin\varphi_0\cos\varphi_0 = \frac{2g}{\sqrt3 L}\cdot\frac{\sqrt3}{4} = \frac{g}{2L} \quad &\text{(products of the data)} \\
> \mathbf a_1^P(0) &= -\frac{g}{2\sqrt3}\,\mathbf e_r + L\left(\frac{g}{L} - \frac{g}{2L}\right)\mathbf e_\varphi + 0\,\mathbf e_\theta = -\frac{g}{2\sqrt3}\,\mathbf e_r + \frac{g}{2}\,\mathbf e_\varphi \quad &\text{(part (a))} \\
> \mathbf e_r(0) &= \tfrac12\,\mathbf i + \tfrac{\sqrt3}{2}\,\mathbf k, \quad \mathbf e_\varphi(0) = \tfrac{\sqrt3}{2}\,\mathbf i - \tfrac12\,\mathbf k \quad &\text{($\theta = 0$, $\varphi = 30^\circ$)} \\
> \mathbf a_1^P(0) &= \left(-\frac{g}{4\sqrt3} + \frac{\sqrt3 g}{4}\right)\mathbf i + \left(-\frac{g}{4} - \frac{g}{4}\right)\mathbf k = \frac{g}{2\sqrt3}\,\mathbf i - \frac{g}{2}\,\mathbf k \quad &\text{($\tfrac{\sqrt3}{4} - \tfrac{1}{4\sqrt3} = \tfrac{3 - 1}{4\sqrt3}$)} \\
> \left|\mathbf a_1^P(0)\right| &= g\sqrt{\frac{1}{12} + \frac14} = g\sqrt{\frac{4}{12}} = \frac{g}{\sqrt3} \quad &\text{(modulus)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_1^P(0) = -\frac{g}{2\sqrt3}\,\mathbf e_r + \frac{g}{2}\,\mathbf e_\varphi = \frac{g}{2\sqrt3}\,\mathbf i - \frac{g}{2}\,\mathbf k \quad \text{(taut-cord model)}}$$
>
> **Units:** $[g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** this is the value the equations of the taut cord give; part (d) shows that the cord cannot actually be taut at that instant, and the box after it gives the acceleration of the real, slack start.

#### (d) Tension at the start

> [!derivation] Tension at t equal to zero, and what a negative value means
> **Law:** projection along the cord; a cord can only pull; Newton's second law of the free particle in the translating frame
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 6.4; Problems.pdf, p. 16
>
> $$\begin{aligned}
> T(0) &= mL\left(0 + \frac{g}{2\sqrt3 L}\right) - mg\,\frac{\sqrt3}{2} \quad &\text{(third equation of the system with the data)} \\
> &= mg\left(\frac{1}{2\sqrt3} - \frac{3}{2\sqrt3}\right) = -\frac{mg}{\sqrt3} \quad &\text{($\tfrac{\sqrt3}{2} = \tfrac{3}{2\sqrt3}$)} \\
> m\,\mathbf a_1^P(0) &= -mg\,\mathbf k + ma\omega^2\sin 0\,\mathbf k = -mg\,\mathbf k \quad &\text{(cord slack: Eq. 4.63 without the cord)}
> \end{aligned}$$
>
> $$\boxed{T(0) = -\frac{mg}{\sqrt3} \lt 0: \ \text{the cord cannot hold; a slack start has } \mathbf a_1^P(0) = -g\,\mathbf k}$$
>
> **Units:** $[mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the given rate is too small to keep a particle above the plane of $A$ on a taut cord: the cord would have to push with the force $mg/\sqrt3$, which only a massless rigid rod could do. With a cord, the particle starts in free fall in the frame of $A$ and the taut-cord equations do not apply at the start.

> [!derivation] Other reading: the angle measured from the downward vertical
> **Law:** the same method with the polar axis pointing down
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 16
>
> If $\varphi$ is measured from the downward vertical (the particle below $A$, as in a hanging pendulum), the radial vector has the vertical component minus $\cos\varphi$, the derivative relations of the basis are the same, so the relative acceleration keeps the form of part (a), and the vertical in the new basis is minus $\cos\varphi$ times the radial vector plus $\sin\varphi$ times the new $\mathbf e_\varphi$.
>
> $$\begin{aligned}
> \mathbf e_r' &= \sin\varphi\cos\theta\,\mathbf i + \sin\varphi\sin\theta\,\mathbf j - \cos\varphi\,\mathbf k, \quad \mathbf e_\varphi' = \frac{\partial\mathbf e_r'}{\partial\varphi} = \cos\varphi\cos\theta\,\mathbf i + \cos\varphi\sin\theta\,\mathbf j + \sin\varphi\,\mathbf k \quad &\text{(polar axis along $-\mathbf k$)} \\
> \mathbf k &= -\cos\varphi\,\mathbf e_r' + \sin\varphi\,\mathbf e_\varphi' \quad &\text{(vertical components $-\cos\varphi$ and $\sin\varphi$)} \\
> \mathbf e_r':\ -mL\left(\dot\varphi^2 + \dot\theta^2\sin^2\varphi\right) &= -T + mg_e\cos\varphi, \quad \mathbf e_\varphi':\ mL\left(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi\right) = -mg_e\sin\varphi \quad &\text{(projections)} \\
> \ddot\varphi_0 &= \frac{g}{2L} - \frac{g}{2L} = 0, \quad T(0) = \frac{mg}{2\sqrt3} + \frac{\sqrt3 mg}{2} = \frac{2mg}{\sqrt3} \quad &\text{(data at $t = 0$)} \\
> \mathbf a_1^P(0) &= -\frac{g}{2\sqrt3}\,\mathbf e_r' - \frac{g}{2}\,\mathbf e_\varphi' = \left(-\frac{g}{4\sqrt3} - \frac{\sqrt3 g}{4}\right)\mathbf i + \left(\frac{g}{4} - \frac{g}{4}\right)\mathbf k = -\frac{g}{\sqrt3}\,\mathbf i \quad &\text{($\mathbf e_r'(0) = \tfrac12\mathbf i - \tfrac{\sqrt3}{2}\mathbf k$, $\mathbf e_\varphi'(0) = \tfrac{\sqrt3}{2}\mathbf i + \tfrac12\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\text{hanging reading: } \ddot\varphi_0 = 0, \quad \mathbf a_1^P(0) = -\frac{g}{\sqrt3}\,\mathbf i, \quad T(0) = \frac{2mg}{\sqrt3}}$$
>
> **Units:** $[g] = [\mathrm{L\,T^{-2}}]$; $[mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** in this reading the given rate is exactly the one of a steady conical pendulum at 30 degrees from the downward vertical: the angle has no acceleration at the start, the relative acceleration points horizontally to the axis, and the cord pulls with twice the weight divided by the square root of 3.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Relative acceleration | $\mathbf a'_P = -L(\dot\varphi^2 + \dot\theta^2\sin^2\varphi)\,\mathbf e_r + L(\ddot\varphi - \dot\theta^2\sin\varphi\cos\varphi)\,\mathbf e_\varphi + L(\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi)\,\mathbf e_\theta$, derived |
| (b) System of equations | $\ddot\varphi = \dot\theta^2\sin\varphi\cos\varphi + (g - a\omega^2\sin\omega t)\sin\varphi/L$; $\ddot\theta\sin\varphi + 2\dot\theta\dot\varphi\cos\varphi = 0$; $T = mL(\dot\varphi^2 + \dot\theta^2\sin^2\varphi) - m(g - a\omega^2\sin\omega t)\cos\varphi$ |
| (c) Relative acceleration at $t = 0$ | taut-cord model: $\mathbf a_1^P(0) = -\frac{g}{2\sqrt3}\,\mathbf e_r + \frac{g}{2}\,\mathbf e_\varphi = \frac{g}{2\sqrt3}\,\mathbf i - \frac{g}{2}\,\mathbf k$, modulus $g/\sqrt3$; actual cord (slack at the start): $-g\,\mathbf k$ |
| (d) Tension at $t = 0$ | $T(0) = -mg/\sqrt3$: impossible for a cord, which goes slack at the start (a rod would push with $mg/\sqrt3$) |
| Other reading ($\varphi$ from the downward vertical) | $\ddot\varphi_0 = 0$, $\mathbf a_1^P(0) = -\frac{g}{\sqrt3}\,\mathbf i$, $T(0) = 2mg/\sqrt3$ |

**Check against the official key:** Problems.pdf, p. 74 lists item 28 with no answer, so there is no key to compare with. Independent checks: the relative acceleration of part (a) is also the second derivative of the Cartesian components of $L\,\mathbf e_r$ (box below), and the limiting cases close the results.

> [!warning] Data inconsistency in the statement
> With $\varphi$ measured from the upward axis $Az'$ (figure and the given $\mathbf e_r$), the given initial azimuthal rate cannot keep the cord taut: the tension at the start is minus $mg/\sqrt3$ (part (d)). The given value is exactly the rate of a steady conical pendulum hanging below $A$ at 30 degrees, which suggests that the statement intends the hanging reading; that reading contradicts the figure and the given unit vectors, so the answers follow the statement as written and the hanging reading is given beside them.

> [!derivation] Independent check: Cartesian components of the relative acceleration at the start
> **Law:** second time derivative of each component of $L\,\mathbf e_r$; chain rule and product rule
> **Source:** Notes.pdf, Eq. 2.7; Problems.pdf, p. 16
>
> $$\begin{aligned}
> \frac{d^2}{dt^2}\left(L\sin\varphi\cos\theta\right) &= L\left(\ddot\varphi\cos\varphi - \dot\varphi^2\sin\varphi\right)\cos\theta - 2L\dot\varphi\dot\theta\cos\varphi\sin\theta - L\sin\varphi\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right) \quad &\text{(product rule; chain rule on each factor)} \\
> &= L\left(\frac{g}{L}\cdot\frac{\sqrt3}{2} - 0\right)\cdot 1 - 0 - L\cdot\frac12\left(0 + \frac{2g}{\sqrt3 L}\right) = \frac{\sqrt3 g}{2} - \frac{g}{\sqrt3} = \frac{g}{2\sqrt3} \quad &\text{(data at $t = 0$, $\ddot\varphi_0 = g/L$)} \\
> \frac{d^2}{dt^2}\left(L\cos\varphi\right) &= -L\left(\ddot\varphi\sin\varphi + \dot\varphi^2\cos\varphi\right) = -L\cdot\frac{g}{L}\cdot\frac12 = -\frac{g}{2} \quad &\text{(chain rule twice)} \\
> \frac{d^2}{dt^2}\left(L\sin\varphi\sin\theta\right) &= L\left(\ddot\varphi\cos\varphi - \dot\varphi^2\sin\varphi\right)\cdot 0 + 2L\dot\varphi\dot\theta\cos\varphi\cdot 1 + L\sin\varphi\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right) = 0 \quad &\text{($\sin 0 = 0$, $\dot\varphi_0 = 0$, $\ddot\theta_0 = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_1^P(0) = \frac{g}{2\sqrt3}\,\mathbf i + 0\,\mathbf j - \frac{g}{2}\,\mathbf k}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the Cartesian route, which never uses the spherical basis, gives the same vector as part (c).

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> a \to 0 \ \text{or}\ \omega \to 0:\quad g_e &\to g \quad &\text{(spherical pendulum with a fixed support)} \\
> \dot\theta \equiv 0:\quad \ddot\varphi &= \frac{g_e}{L}\sin\varphi \quad &\text{(planar pendulum written from the upward vertical: Eq. 4.38 with $\varphi = \pi - $ the hanging angle)} \\
> \varphi = \pi,\ \dot\varphi = \dot\theta = 0:\quad T &= -mg_e\cos\pi = mg_e \quad &\text{(particle hanging at rest below $A$)}
> \end{aligned}$$
>
> $$\boxed{a\omega^2 \to 0: \ g_e \to g; \qquad \text{hanging at rest: } T = m\left(g - a\omega^2\sin\omega t\right)}$$
>
> **Units:** $[mg_e] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** with a still support the problem is the ordinary spherical pendulum; a particle hanging at rest below the oscillating support feels the weight changed by the inertia force of the support, and the cord stays taut only while $g$ exceeds the product $a\omega^2\sin\omega t$.

---

## Problem 30: Particle on a Rotating Quarter Circumference with a Spring

### Reference Frames, Bases and Coordinates
* **System:** a particle $P$ of mass $m$ slides on a smooth quarter circumference of radius $R$ and centre $O$, drawn in the vertical plane $X_1Z_1$ of a frame that rotates with constant angular velocity $\omega\mathbf{k}_1$ about the vertical axis $x_1 = -R$, $y_1 = 0$. A spring of constant $K = \alpha m\omega^2$ joins $P$ to the point $B = (-2R, 0, 0)$ of the rotating frame. Gravity is neglected.
* **Why a rotating frame.** The wire and the spring anchor $B$ are fixed in $OX_1Y_1Z_1$, so the constraint is a fixed circle there and the position of $P$ is described by one angle. The price is the inertia force of Notes Eqs. 4.62–4.63, which is easy to compute because $\boldsymbol{\omega}_{10}$ is constant. In the inertial frame the wire itself moves, and the constraint would be harder to write.
* **Hypotheses:** <br>1. $OXYZ$ is inertial; the frame rotates uniformly, $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_1$ with $\omega$ constant. <br>2. The arc is smooth (no friction) and acts as a bilateral constraint (a bead on a wire): the reaction has no tangential component but its normal and binormal components can take either sign. <br>3. The spring is linear and, since no natural length is given, of **zero natural length**: $\mathbf{F}_K = -K\,\overrightarrow{BP}$. <br>4. Gravity is neglected, as the statement says.
* **Fixed (inertial) frame.** The only points that do not move are those of the rotation axis. We take $S_0 = \{Q; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, basis $\mathcal{B}_0$, with origin at the point $Q$ of the axis at the height of $O$ (the point $x_1 = -R$, $y_1 = z_1 = 0$, the upper end of the arc). It plays the role of the statement's $OXYZ$; moving the origin of an inertial frame to another fixed point does not change any velocity or acceleration. $\mathbf{k}_0 = \mathbf{k}$ is vertical.
* **Moving frame.** $S_1 = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, basis $\mathcal{B}_1$, is the statement's $OX_1Y_1Z_1$, attached to the arc, with $\mathbf{k}_1 = \mathbf{k}_0$. Its origin $O$ is at distance $R$ from the axis, so it moves on a horizontal circle. We choose $\mathbf{i}_1 = \mathbf{i}_0$ at $t = 0$.
* **Path (intrinsic) basis** $\{\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b\}$ at $P$: tangent in the direction of increasing $\phi$, principal normal towards the centre of curvature and binormal; it is deduced in the next section.
* **Degrees of freedom and coordinate:** on the arc, $P$ has one degree of freedom, the angle $\phi \in [0, \pi/2]$ between $\overline{OP}$ and the negative $z_1$ axis. After leaving the arc in part (f), $P$ is free: three degrees of freedom $(x_1, y_1, z_1)$.
* **Initial conditions:** $\phi(0) = 0$, $\mathbf{v}_1^P(0) = -\beta\omega R\,\mathbf{i}_1$.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $R$ | radius of the arc and distance from $O$ to the axis | m |
| $\omega$ | constant angular velocity of the frame | rad/s |
| $K = \alpha m\omega^2$ | spring constant | N/m = kg/s$^2$ |
| $\alpha$, $\beta$ | positive nondimensional parameters | 1 |
| $\phi$ | angle between $\overline{OP}$ and the $-z_1$ axis | rad |
| $N_n$, $N_b$ | components of the reaction of the arc | N |

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p30-top-view.svg]]

The rotation is about the vertical $\mathbf{k}_0$, so it is drawn looking down the axis, from $+z$, with the axis at $Q$. In that view $\mathbf{k}_0$ points out of the paper, towards the reader ($\odot$). Take $\mathbf{i}_0$ to the right. Then $\mathbf{j}_0 = \mathbf{k}_0\times\mathbf{i}_0$ (right-hand rule: thumb along $\mathbf{k}_0$, towards the reader, and the fingers turn $\mathbf{i}_0$ counter-clockwise by $90^\circ$) points up the page.

With $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_0$ and $\omega \gt 0$, the frame turns counter-clockwise in this view (thumb towards the reader). After a time $t$ it has turned the angle $\omega t$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the dashed right triangle. The leg adjacent to $\omega t$ lies along $\mathbf{i}_0$ and measures $\cos\omega t$; the leg opposite to $\omega t$ points up the page, along $+\mathbf{j}_0$, and measures $\sin\omega t$. Hence $\mathbf{i}_1 = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$, with no minus sign.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ (up the page) and turns the same angle counter-clockwise, so its tip moves to the left, towards $-\mathbf{i}_0$. Its leg along $\mathbf{j}_0$ (adjacent) is $\cos\omega t$ and its leg along $-\mathbf{i}_0$ (opposite) is $\sin\omega t$: $\mathbf{j}_1 = -\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0$. **The minus sign comes from the counter-clockwise turn carrying the upward axis to the left.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

The columns of $[{}_0R_1]$ are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix} $$

* **Checks.** Expanding along the third row, $\det[{}_0R_1] = 1\cdot\left(\cos\omega t\cos\omega t - (-\sin\omega t)\sin\omega t\right) = \cos^2\omega t + \sin^2\omega t = 1$. The columns have unit length ($\cos^2\omega t + \sin^2\omega t = 1$) and the first two are orthogonal ($-\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0$), so $[{}_0R_1][{}_0R_1]^T = I$.
* **Angular motion of $S_1$:** $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_1$ and, $\omega$ being constant, $\boldsymbol{\alpha}_{10} = \left.\dfrac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 = \mathbf{0}$.
* **Motion of the origin $O$.** $O$ lies on the line of $\mathbf{i}_1$ through $Q$, at distance $R$ from the axis (the figure shows its dashed circle), so $\mathbf{r}_0^O = \overrightarrow{QO} = R\,\mathbf{i}_1$. By the Coriolis theorem (Notes Eq. 3.8), since $R\,\mathbf{i}_1$ is constant in $S_1$:
$$ \mathbf{v}_0^O = \left.\frac{d(R\mathbf{i}_1)}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times R\,\mathbf{i}_1 = \mathbf{0} + \omega R\,(\mathbf{k}_1\times\mathbf{i}_1) = \omega R\,\mathbf{j}_1 $$
$$ \mathbf{a}_0^O = \left.\frac{d(\omega R\mathbf{j}_1)}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\omega R\,\mathbf{j}_1 = \omega^2 R\,(\mathbf{k}_1\times\mathbf{j}_1) = -\omega^2 R\,\mathbf{i}_1 $$
* **Direct check in $\mathcal{B}_0$.** $\mathbf{r}_0^O = R\cos\omega t\,\mathbf{i}_0 + R\sin\omega t\,\mathbf{j}_0$. By the chain rule, $\frac{d}{dt}\cos\omega t = -\omega\sin\omega t$ and $\frac{d}{dt}\sin\omega t = \omega\cos\omega t$, so $\mathbf{v}_0^O = \omega R\left(-\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0\right) = \omega R\,\mathbf{j}_1$ and, differentiating again, $\mathbf{a}_0^O = -\omega^2R\left(\cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0\right) = -\omega^2R\,\mathbf{i}_1$, the vectors drawn at $O$ in orange.

#### The position vector in the plane of the arc

![[attachments/EM-SOL/p30-arc-plane.svg]]

The plane $X_1Z_1$ is fixed in $S_1$; it is drawn with $\mathbf{i}_1$ to the right and $\mathbf{k}_1$ up. The direction out of the paper is then $\mathbf{i}_1\times\mathbf{k}_1 = -\mathbf{j}_1$, so $\mathbf{j}_1$ points **into** the paper ($\otimes$).

Let $F$ be the point of the $z_1$ axis at the height of $P$. In the shaded right triangle $OFP$ (right angle at $F$) the hypotenuse is $|OP| = R$ and the angle at $O$ is $\phi$:

* the leg adjacent to $\phi$ is $OF = R\cos\phi$, along the $z_1$ axis and pointing down: $\overrightarrow{OF} = -R\cos\phi\,\mathbf{k}_1$;
* the leg opposite to $\phi$ is $FP = R\sin\phi$, horizontal and pointing to the left, towards $B$: $\overrightarrow{FP} = -R\sin\phi\,\mathbf{i}_1$.

So $\mathbf{r}_1^P = \overrightarrow{OF} + \overrightarrow{FP}$:

$$ \mathbf{r}_1^P = -R\sin\phi\,\mathbf{i}_1 - R\cos\phi\,\mathbf{k}_1 $$

Checks: $\phi = 0$ gives $-R\,\mathbf{k}_1$, the lowest point of the arc on the $-z_1$ axis (the initial position); $\phi = \pi/2$ gives $-R\,\mathbf{i}_1$, the upper end of the arc, which lies on the rotation axis $x_1 = -R$. The horizontal distance from $P$ to the rotation axis is $x_1 - (-R) = R - R\sin\phi = R(1 - \sin\phi)$, the dimension drawn in the figure; it is the lever arm of the centrifugal force.

**Relation with the standard polar angle.** In the plane $X_1Z_1$ the usual polar angle $\vartheta$ about $O$ is measured from $\mathbf{i}_1$ towards $\mathbf{k}_1$, with $\mathbf{r}_1^P = R\left(\cos\vartheta\,\mathbf{i}_1 + \sin\vartheta\,\mathbf{k}_1\right)$. Comparing with the expression above requires $\cos\vartheta = -\sin\phi$ and $\sin\vartheta = -\cos\phi$, which holds for

$$ \vartheta = -\frac{\pi}{2} - \phi: \qquad \cos\left(\tfrac{\pi}{2} + \phi\right) = \cos\tfrac{\pi}{2}\cos\phi - \sin\tfrac{\pi}{2}\sin\phi = -\sin\phi, \qquad \sin\left(\tfrac{\pi}{2} + \phi\right) = \sin\tfrac{\pi}{2}\cos\phi + \cos\tfrac{\pi}{2}\sin\phi = \cos\phi $$

so $\cos\vartheta = \cos\left(\tfrac{\pi}{2} + \phi\right) = -\sin\phi$ (the cosine is even) and $\sin\vartheta = -\sin\left(\tfrac{\pi}{2} + \phi\right) = -\cos\phi$ (the sine is odd), with $\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$. Thus $\phi$ is measured from $-\mathbf{k}_1$ instead of $\mathbf{i}_1$, and it grows clockwise in the drawing (from the downward axis towards $B$), while $\vartheta$ grows counter-clockwise.

**Path basis.** On the arc we take the arc length $s = R\phi$ (increasing with $\phi$). The tangent is the derivative of the position with respect to $\phi$, divided by its length. With $\frac{d}{d\phi}(-R\sin\phi) = -R\cos\phi$ and $\frac{d}{d\phi}(-R\cos\phi) = R\sin\phi$:

$$ \frac{d\mathbf{r}_1^P}{d\phi} = -R\cos\phi\,\mathbf{i}_1 + R\sin\phi\,\mathbf{k}_1, \qquad \left|\frac{d\mathbf{r}_1^P}{d\phi}\right| = R\sqrt{\cos^2\phi + \sin^2\phi} = R \;\Rightarrow\; \mathbf{e}_t = -\cos\phi\,\mathbf{i}_1 + \sin\phi\,\mathbf{k}_1 $$

Differentiating $\mathbf{e}_t$ with respect to $\phi$ ($\frac{d}{d\phi}(-\cos\phi) = \sin\phi$, $\frac{d}{d\phi}\sin\phi = \cos\phi$) gives a vector of length $\sqrt{\sin^2\phi + \cos^2\phi} = 1$, the principal normal:

$$ \mathbf{e}_n = \frac{d\mathbf{e}_t}{d\phi} = \sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{k}_1 = -\frac{\mathbf{r}_1^P}{R} $$

so $\mathbf{e}_n$ points from $P$ to the centre of curvature $O$, along the hypotenuse of the triangle, as drawn. The binormal:

$$ \mathbf{e}_b = \mathbf{e}_t\times\mathbf{e}_n = \begin{vmatrix} \mathbf{i}_1 & \mathbf{j}_1 & \mathbf{k}_1 \\ -\cos\phi & 0 & \sin\phi \\ \sin\phi & 0 & \cos\phi \end{vmatrix} = (0 - 0)\,\mathbf{i}_1 - (-\cos^2\phi - \sin^2\phi)\,\mathbf{j}_1 + (0 - 0)\,\mathbf{k}_1 = \mathbf{j}_1 $$

the direction into the paper, normal to the plane of the arc. The matrix whose columns are $\mathbf{e}_t, \mathbf{e}_n, \mathbf{e}_b$ in $\mathcal{B}_1$ is

$$ [{}_1R_t] = \begin{pmatrix} -\cos\phi & \sin\phi & 0 \\ 0 & 0 & 1 \\ \sin\phi & \cos\phi & 0 \end{pmatrix}, \qquad \det[{}_1R_t] = -\cos\phi\,(0 - \cos\phi) - \sin\phi\,(0 - \sin\phi) = 1 $$

and its columns are unit and mutually orthogonal ($\mathbf{e}_t\cdot\mathbf{e}_n = -\cos\phi\sin\phi + \sin\phi\cos\phi = 0$), so $[{}_1R_t][{}_1R_t]^T = I$.

* **Useful projections** (read from the columns): $\mathbf{i}_1\cdot\mathbf{e}_t = -\cos\phi$, $\mathbf{i}_1\cdot\mathbf{e}_n = \sin\phi$, $\mathbf{k}_1\cdot\mathbf{e}_t = \sin\phi$, $\mathbf{k}_1\cdot\mathbf{e}_n = \cos\phi$, $\mathbf{j}_1 = \mathbf{e}_b$.

### Kinematics

##### (a) Relative velocity and acceleration in the path basis
* **Pedagogical Justification:** The relative velocity and acceleration are the first and second derivatives of $\mathbf{r}_1^P$ taken in $S_1$, where $\mathbf{i}_1, \mathbf{k}_1$ are constant. Only $\phi$ depends on time, so each derivative is a chain rule.

Differentiate $\mathbf{r}_1^P = -R\sin\phi\,\mathbf{i}_1 - R\cos\phi\,\mathbf{k}_1$ with $\dfrac{d}{dt}\sin\phi = \cos\phi\,\dot\phi$ and $\dfrac{d}{dt}\cos\phi = -\sin\phi\,\dot\phi$:

$$ \mathbf{v}_1^P = \left.\frac{d\mathbf{r}_1^P}{dt}\right|_1 = -R\cos\phi\,\dot\phi\,\mathbf{i}_1 + R\sin\phi\,\dot\phi\,\mathbf{k}_1 = R\dot\phi\left(-\cos\phi\,\mathbf{i}_1 + \sin\phi\,\mathbf{k}_1\right) = R\dot\phi\,\mathbf{e}_t $$

which is $\dot s\,\mathbf{e}_t$ with $s = R\phi$. For the acceleration use the product rule on $R\dot\phi\,\mathbf{e}_t$, and the chain rule on $\mathbf{e}_t(\phi(t))$:

$$ \left.\frac{d\mathbf{e}_t}{dt}\right|_1 = \frac{d\mathbf{e}_t}{d\phi}\,\dot\phi = \left(\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{k}_1\right)\dot\phi = \dot\phi\,\mathbf{e}_n $$
$$ \mathbf{a}_1^P = \left.\frac{d\mathbf{v}_1^P}{dt}\right|_1 = R\ddot\phi\,\mathbf{e}_t + R\dot\phi\left.\frac{d\mathbf{e}_t}{dt}\right|_1 = R\ddot\phi\,\mathbf{e}_t + R\dot\phi^2\,\mathbf{e}_n $$

The normal part is $\dot s^2/\rho$ with radius of curvature $\rho = R$, as expected for a circle. There is no binormal component.

### Forces and Equations of Motion

##### (b) Newton's second law in the path basis
* **Pedagogical Justification:** $S_1$ is not inertial, so we use Newton's law with inertia forces, $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ (Notes Eqs. 4.62–4.63, Slides 27–28). This keeps the simple relative acceleration of part (a) and puts the frame's motion into four forces.

**Actual forces.**

* Spring (zero natural length): $\overrightarrow{BP} = \mathbf{r}_1^P - \mathbf{r}_1^B = (-R\sin\phi + 2R)\,\mathbf{i}_1 - R\cos\phi\,\mathbf{k}_1 = (2R - R\sin\phi)\,\mathbf{i}_1 - R\cos\phi\,\mathbf{k}_1$, with $\mathbf{r}_1^B = -2R\,\mathbf{i}_1$, so
$$ \mathbf{F}_K = -\alpha m\omega^2 R\left[(2 - \sin\phi)\,\mathbf{i}_1 - \cos\phi\,\mathbf{k}_1\right] $$
* Reaction of the smooth arc: $\mathbf{N} = N_n\,\mathbf{e}_n + N_b\,\mathbf{e}_b$ (no $\mathbf{e}_t$ component, because the arc is smooth).

**Inertia forces** (Slide 28), with $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_1$, $\boldsymbol{\alpha}_{10} = \mathbf{0}$, $\mathbf{a}_0^O = -\omega^2R\,\mathbf{i}_1$:

* Force due to the acceleration of the origin: $\mathbf{F}_A = -m\mathbf{a}_0^O = m\omega^2R\,\mathbf{i}_1$.
* Euler force: $\mathbf{F}_E = -m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P = \mathbf{0}$.
* Centrifugal force. First $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = \omega\mathbf{k}_1\times(-R\sin\phi\,\mathbf{i}_1 - R\cos\phi\,\mathbf{k}_1) = -\omega R\sin\phi\,\mathbf{j}_1$ (using $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$); then $\boldsymbol{\omega}_{10}\times(-\omega R\sin\phi\,\mathbf{j}_1) = -\omega^2R\sin\phi\,(\mathbf{k}_1\times\mathbf{j}_1) = \omega^2R\sin\phi\,\mathbf{i}_1$ (using $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$), so $\mathbf{F}_C = -m\omega^2R\sin\phi\,\mathbf{i}_1$.
* Coriolis force: $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = \omega R\dot\phi\,\mathbf{k}_1\times(-\cos\phi\,\mathbf{i}_1 + \sin\phi\,\mathbf{k}_1) = -\omega R\dot\phi\cos\phi\,\mathbf{j}_1$, so $\mathbf{F}_{COR} = -2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = 2m\omega R\dot\phi\cos\phi\,\mathbf{j}_1$.

The first and third combine into the centrifugal force about the **true** rotation axis, whose distance to $P$ is $x_1 + R = R(1 - \sin\phi)$ (Slide 30, and the dimension of the figure of the arc):

$$ \mathbf{F}_A + \mathbf{F}_C = m\omega^2R\,(1 - \sin\phi)\,\mathbf{i}_1 $$

**Projections.** With the projections listed at the end of the change-of-basis section:

$$ \mathbf{F}_K\cdot\mathbf{e}_t = -\alpha m\omega^2R\left[(2 - \sin\phi)(-\cos\phi) + (-\cos\phi)(\sin\phi)\right] = -\alpha m\omega^2R\left[-2\cos\phi + \sin\phi\cos\phi - \sin\phi\cos\phi\right] = 2\alpha m\omega^2R\cos\phi $$
$$ \mathbf{F}_K\cdot\mathbf{e}_n = -\alpha m\omega^2R\left[(2 - \sin\phi)\sin\phi - \cos^2\phi\right] = -\alpha m\omega^2R\left[2\sin\phi - 1\right] = \alpha m\omega^2R\,(1 - 2\sin\phi) $$
$$ (\mathbf{F}_A + \mathbf{F}_C)\cdot\mathbf{e}_t = -m\omega^2R\,(1 - \sin\phi)\cos\phi, \qquad (\mathbf{F}_A + \mathbf{F}_C)\cdot\mathbf{e}_n = m\omega^2R\,(1 - \sin\phi)\sin\phi $$

(in the second line $\sin^2\phi + \cos^2\phi = 1$ was used), and $\mathbf{F}_K$, $\mathbf{F}_A + \mathbf{F}_C$ have no $\mathbf{e}_b = \mathbf{j}_1$ component, while $\mathbf{F}_{COR}$ lies entirely along $\mathbf{e}_b$.

##### (b, continued) Equation of motion and reaction

**The three components** of $m\mathbf{a}_1^P = \mathbf{F}_K + \mathbf{N} + \mathbf{F}_A + \mathbf{F}_E + \mathbf{F}_C + \mathbf{F}_{COR}$:

$$ \mathbf{e}_t:\quad mR\ddot\phi = 2\alpha m\omega^2R\cos\phi - m\omega^2R\,(1 - \sin\phi)\cos\phi $$
$$ \mathbf{e}_n:\quad mR\dot\phi^2 = N_n + \alpha m\omega^2R\,(1 - 2\sin\phi) + m\omega^2R\,(1 - \sin\phi)\sin\phi $$
$$ \mathbf{e}_b:\quad 0 = N_b + 2m\omega R\dot\phi\cos\phi $$

The tangential component contains no reaction and is the **equation of motion**; the other two give the **reaction**:

$$ \boxed{\ddot\phi = \omega^2\cos\phi\,\left(2\alpha - 1 + \sin\phi\right)} $$
$$ \boxed{N_n = mR\dot\phi^2 - \alpha m\omega^2R\,(1 - 2\sin\phi) - m\omega^2R\,\sin\phi\,(1 - \sin\phi), \qquad N_b = -2m\omega R\dot\phi\cos\phi} $$

The binormal reaction balances the Coriolis force: the arc has to push $P$ sideways to keep it in the rotating plane.

### Answers and Checks

##### (a) Relative velocity and acceleration
$$ \boxed{\mathbf{v}_1^P = R\dot\phi\,\mathbf{e}_t, \qquad \mathbf{a}_1^P = R\ddot\phi\,\mathbf{e}_t + R\dot\phi^2\,\mathbf{e}_n} $$

##### (b) Newton's second law in the path basis
The three components are the $\mathbf{e}_t$, $\mathbf{e}_n$ and $\mathbf{e}_b$ equations of the previous section: $\ddot\phi = \omega^2\cos\phi\,(2\alpha - 1 + \sin\phi)$, $N_n = mR\dot\phi^2 - \alpha m\omega^2R\,(1 - 2\sin\phi) - m\omega^2R\sin\phi\,(1 - \sin\phi)$ and $N_b = -2m\omega R\dot\phi\cos\phi$.

##### (c) Energy conservation in the relative frame
* **Pedagogical Justification:** In $S_1$ (Slide 29) the mechanical energy $E_1^P$ is conserved if every force that does work in $S_1$ has a potential. Here: $\mathbf{N}$ does no work in $S_1$ because the arc is fixed in $S_1$ and $\mathbf{N}\perp\mathbf{v}_1^P = R\dot\phi\,\mathbf{e}_t$; $\mathbf{F}_{COR}\perp\mathbf{v}_1^P$ never does work (Slide 31); $\mathbf{F}_E = \mathbf{0}$; the spring is conservative; and $\mathbf{F}_A + \mathbf{F}_C$ is the centrifugal force about an axis fixed in $S_1$ with constant $\omega$, which has the potential of Slide 30.

**Potentials.** Spring: $V_K = \tfrac12 K\,|\overrightarrow{BP}|^2$ with

$$ |\overrightarrow{BP}|^2 = R^2\left[(2 - \sin\phi)^2 + \cos^2\phi\right] = R^2\left[4 - 4\sin\phi + \sin^2\phi + \cos^2\phi\right] = R^2\,(5 - 4\sin\phi) $$

so $V_K = \tfrac12\alpha m\omega^2R^2\,(5 - 4\sin\phi)$. Centrifugal (Slide 30), with $r_\perp = x_1 + R = R(1 - \sin\phi)$:

$$ V_C = -\tfrac12 m\omega^2 r_\perp^2 = -\tfrac12 m\omega^2R^2\,(1 - \sin\phi)^2 $$

(Check: in Cartesian form $V_C = -\tfrac12 m\omega^2(x_1 + R)^2$ and $-\partial V_C/\partial x_1 = m\omega^2(x_1 + R)$, the $\mathbf{i}_1$ component of $\mathbf{F}_A + \mathbf{F}_C$.)

**Energy equation:**

$$ \boxed{E_1^P = \tfrac12 mR^2\dot\phi^2 + \tfrac12\alpha m\omega^2R^2\,(5 - 4\sin\phi) - \tfrac12 m\omega^2R^2\,(1 - \sin\phi)^2 = \text{const}} $$

**Initial value.** At $t = 0$, $\mathbf{e}_t(0) = -\mathbf{i}_1$, so $\mathbf{v}_1^P(0) = R\dot\phi(0)\,(-\mathbf{i}_1) = -\beta\omega R\,\mathbf{i}_1$ gives $\dot\phi(0) = \beta\omega$, and $E_1^P(0) = \tfrac12 m\omega^2R^2\,(\beta^2 + 5\alpha - 1)$. Equating and dividing by $\tfrac12 mR^2$:

$$ \dot\phi^2 = \omega^2\left[\beta^2 + 5\alpha - 1 - \alpha(5 - 4\sin\phi) + (1 - \sin\phi)^2\right] \implies \boxed{\dot\phi^2 = \omega^2\left[\beta^2 + (4\alpha - 2)\sin\phi + \sin^2\phi\right]} $$

**Equivalence.** Differentiate $E_1^P$ in time with the chain rule ($\tfrac{d}{dt}\sin\phi = \cos\phi\,\dot\phi$, $\tfrac{d}{dt}(1 - \sin\phi)^2 = 2(1 - \sin\phi)(-\cos\phi\,\dot\phi)$):

$$ \frac{dE_1^P}{dt} = mR^2\dot\phi\ddot\phi - 2\alpha m\omega^2R^2\cos\phi\,\dot\phi + m\omega^2R^2(1 - \sin\phi)\cos\phi\,\dot\phi = mR^2\dot\phi\left[\ddot\phi - 2\alpha\omega^2\cos\phi + \omega^2(1 - \sin\phi)\cos\phi\right] $$

The bracket is zero exactly when the $\mathbf{e}_t$ equation of part (b) holds. So the energy equation is **not new information**: it is the first integral of the tangential component (the $\mathbf{e}_t$ equation multiplied by $R\dot\phi$ and integrated once). The $\mathbf{e}_n$ and $\mathbf{e}_b$ components are independent of it and are needed to compute the reaction.

##### (d) Value of $\alpha$ for equilibrium at $\phi = \pi/6$
* **Pedagogical Justification:** Relative equilibrium in $S_1$ means $\dot\phi = 0$ and $\ddot\phi = 0$ for all time. The $\mathbf{e}_t$ equation then requires that the tangential force vanish.
$$ \ddot\phi = 0 \iff \cos\phi\,(2\alpha - 1 + \sin\phi) = 0 $$

The root $\cos\phi = 0$ ($\phi = \pi/2$, the particle on the axis) is an equilibrium for every $\alpha$. Any other equilibrium must satisfy $\sin\phi_e = 1 - 2\alpha$. For $\phi_e = \pi/6$, $\sin\phi_e = \tfrac12$:

$$ 2\alpha - 1 + \tfrac12 = 0 \implies \boxed{\alpha = \tfrac14} $$

At that equilibrium, from part (b) with $\dot\phi = 0$: $N_b = 0$ and $N_n = -\tfrac14 m\omega^2R\,(1 - 1) - m\omega^2R\cdot\tfrac12\cdot\tfrac12 = -\tfrac14 m\omega^2R$, i.e. the arc pulls $P$ away from $O$ with force $\tfrac14 m\omega^2R$.

##### (e) Types of motion for $\alpha = 1/4$, critical $\beta$ and reaction at $\phi = \pi/2$
* **Pedagogical Justification:** The energy integral of part (c) is a first-order equation $\dot\phi^2 = \omega^2[\beta^2 - W(\phi)]$; motion is possible only where $W(\phi) \le \beta^2$, so the shape of $W$ classifies the motions, as with a one-dimensional potential.

With $\alpha = \tfrac14$, $4\alpha - 2 = -1$:

$$ \dot\phi^2 = \omega^2\left[\beta^2 - W(\phi)\right], \qquad W(\phi) = \sin\phi\,(1 - \sin\phi) $$

On $[0, \pi/2]$: $W(0) = 0$, $W(\pi/2) = 0$, and $\dfrac{dW}{d\phi} = \cos\phi\,(1 - 2\sin\phi)$ vanishes inside the interval only at $\sin\phi = \tfrac12$, i.e. $\phi = \pi/6$, where $W$ has its maximum $W(\pi/6) = \tfrac12\cdot\tfrac12 = \tfrac14$. $W$ plays the role of a potential barrier, so the equilibrium $\phi = \pi/6$ is **unstable**. Three types of motion follow:

* **$\beta \gt \tfrac12$:** $\dot\phi^2 \ge \omega^2(\beta^2 - \tfrac14) \gt 0$ on the whole arc, so $\phi$ increases monotonically, crosses the barrier at $\pi/6$ and reaches $\phi = \pi/2$ with $\dot\phi^2 = \omega^2[\beta^2 - 0]$, i.e. $\dot\phi = \beta\omega$: the relative speed there equals the initial one, $\beta\omega R$. The particle then leaves the arc at its upper end (part f).
* **$\beta = \tfrac12$:** $\beta^2 - W = \tfrac14 - \sin\phi + \sin^2\phi = (\tfrac12 - \sin\phi)^2$, so $\dot\phi = \omega(\tfrac12 - \sin\phi)$. The particle approaches the unstable equilibrium $\phi = \pi/6$ asymptotically and never reaches it: near it, $\sin\phi \approx \tfrac12 + \tfrac{\sqrt3}{2}(\phi - \tfrac{\pi}{6})$ and $\dot\phi \approx -\tfrac{\sqrt3}{2}\omega\,(\phi - \tfrac{\pi}{6})$, an exponential approach with rate $\tfrac{\sqrt3}{2}\omega$.
* **$\beta \lt \tfrac12$:** $\dot\phi$ vanishes at the turning point $\phi^*$ with $W(\phi^*) = \beta^2$, i.e. $\sin^2\phi^* - \sin\phi^* + \beta^2 = 0$; the root reached first is
$$ \sin\phi^* = \frac{1 - \sqrt{1 - 4\beta^2}}{2} \lt \frac12 $$

There $\ddot\phi = \omega^2\cos\phi^*\,(\sin\phi^* - \tfrac12) \lt 0$, so the particle turns back, returns to $\phi = 0$ with $\dot\phi = -\beta\omega$ (relative velocity $+\beta\omega R\,\mathbf{i}_1$, same speed by energy conservation) and leaves the quarter circumference at its lower end.

**Critical value.** The particle reaches $\phi = \pi/2$ if and only if $\beta$ exceeds

$$ \boxed{\beta_c = \tfrac12} $$

**Reaction at $\phi = \pi/2$.** Here $\cos\phi = 0$, $\sin\phi = 1$, $\dot\phi = \beta\omega$, and $\mathbf{e}_n(\pi/2) = \mathbf{i}_1$. From part (b) with $\alpha = \tfrac14$:

$$ N_b = -2m\omega R\,\beta\omega\cdot 0 = 0, \qquad N_n = mR\beta^2\omega^2 - \tfrac14 m\omega^2R\,(1 - 2) - m\omega^2R\cdot 1\cdot 0 = m\omega^2R\left(\beta^2 + \tfrac14\right) $$
$$ \boxed{\mathbf{N}(\phi = \tfrac{\pi}{2}) = m\omega^2R\left(\beta^2 + \tfrac14\right)\mathbf{i}_1 \;\xrightarrow{\;\beta\to\beta_c\;}\; \tfrac12 m\omega^2R\,\mathbf{i}_1} $$

It points towards $O$: it supplies the centripetal force $mR\dot\phi^2$ and also balances the spring, which pulls $P$ towards $B$ with $\tfrac14 m\omega^2R$. The centrifugal and Coriolis forces vanish there because $P$ is on the axis and moves parallel to it.

##### (f) Maximum height after leaving the arc ($\beta \gt \beta_c$)
* **Pedagogical Justification:** Once free, $P$ has three degrees of freedom, and the horizontal motion is coupled through the Coriolis and centrifugal forces. But every inertia force of a frame rotating about the vertical is horizontal, so the vertical component of $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ involves only the spring and decouples.

**Initial state of the free motion** (time $\tau = 0$ at separation): $\phi = \pi/2$ gives $\mathbf{r}_1^P = -R\,\mathbf{i}_1$ (on the axis, $z_1 = 0$), and $\mathbf{v}_1^P = R\dot\phi\,\mathbf{e}_t(\pi/2) = \beta\omega R\,\mathbf{k}_1$ (vertical, upward).

**Vertical equation.** For a free position $\mathbf{r}_1^P = x_1\mathbf{i}_1 + y_1\mathbf{j}_1 + z_1\mathbf{k}_1$:

* $\mathbf{k}_1\cdot\mathbf{F}_K = -K\,\mathbf{k}_1\cdot\left[(x_1 + 2R)\mathbf{i}_1 + y_1\mathbf{j}_1 + z_1\mathbf{k}_1\right] = -\alpha m\omega^2 z_1$;
* $\mathbf{k}_1\cdot(\mathbf{F}_A + \mathbf{F}_C) = 0$, because $\mathbf{F}_A + \mathbf{F}_C = m\omega^2\left[(x_1 + R)\mathbf{i}_1 + y_1\mathbf{j}_1\right]$ is horizontal;
* $\mathbf{k}_1\cdot\mathbf{F}_{COR} = -2m\,\mathbf{k}_1\cdot(\omega\mathbf{k}_1\times\mathbf{v}_1^P) = 0$, because $\mathbf{k}_1\times\mathbf{v}_1^P\perp\mathbf{k}_1$.

Hence, with $\alpha = \tfrac14$,

$$ m\ddot z_1 = -\alpha m\omega^2 z_1 \implies \ddot z_1 + \frac{\omega^2}{4}z_1 = 0 $$

a harmonic oscillator of angular frequency $\omega/2$. Its general solution and derivative (chain rule $\tfrac{d}{d\tau}\sin\tfrac{\omega\tau}{2} = \tfrac{\omega}{2}\cos\tfrac{\omega\tau}{2}$) are

$$ z_1 = C_1\cos\frac{\omega\tau}{2} + C_2\sin\frac{\omega\tau}{2}, \qquad \dot z_1 = -\frac{\omega}{2}C_1\sin\frac{\omega\tau}{2} + \frac{\omega}{2}C_2\cos\frac{\omega\tau}{2} $$

Initial conditions: $z_1(0) = C_1 = 0$ and $\dot z_1(0) = \tfrac{\omega}{2}C_2 = \beta\omega R$, so $C_2 = 2\beta R$:

$$ z_1(\tau) = 2\beta R\,\sin\frac{\omega\tau}{2} \implies \boxed{z_{max} = 2\beta R}\quad\text{reached at } \tau = \pi/\omega $$

Since $\mathbf{k}_1 = \mathbf{k}$, this is also the height in the inertial frame, measured from the horizontal plane through $O$ and $B$. For a general $\alpha$ the same steps give $z_{max} = \beta R/\sqrt{\alpha}$. (Equivalently, the vertical motion conserves $\tfrac12 m\dot z_1^2 + \tfrac12 Kz_1^2$, and $\tfrac12 m(\beta\omega R)^2 = \tfrac12\cdot\tfrac14 m\omega^2 z_{max}^2$ gives the same result.) The result assumes that the free particle does not hit the wire again.

##### Checks
* **Competition of two forces.** Along the arc the spring pulls $P$ towards $B$ (towards larger $\phi$) with tangential force $2\alpha m\omega^2R\cos\phi$, while the centrifugal force about the axis pushes it away from the axis (towards smaller $\phi$) with $m\omega^2R(1 - \sin\phi)\cos\phi$. Both scale with $\omega^2$ because $K = \alpha m\omega^2$, so $\omega$ only sets the time scale $1/\omega$ and the dynamics depends on $\alpha$ and $\beta$ alone.
* **Limiting cases.** For $\alpha \gt \tfrac12$ the factor $2\alpha - 1 + \sin\phi$ is positive on the whole arc and there is no interior equilibrium. For $\beta \to \beta_c^+$ the time to cross the barrier grows without bound (logarithmically), consistent with the asymptotic motion at $\beta = \beta_c$. As $\phi\to\pi/2$, both the Coriolis force and $N_b$ vanish, as they must for motion parallel to $\boldsymbol{\omega}_{10}$.
* **Orthogonality:** $\mathbf{e}_t\cdot\mathbf{e}_n = 0$, $\mathbf{e}_t\times\mathbf{e}_n = \mathbf{j}_1$ and $\det[{}_1R_t] = \det[{}_0R_1] = 1$ (change-of-basis section).
* **Inertial check.** Computing $\mathbf{a}_0^P$ by differentiating $\mathbf{r}_0^P = \mathbf{r}_0^O + [{}_0R_1]\mathbf{r}_1^P$ twice gives exactly $\mathbf{a}_0^O + \mathbf{a}_1^P + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ (Notes Eq. 3.27), and $m\mathbf{a}_0^P = \mathbf{F}_K + \mathbf{N}$ holds with the reactions of part (b) (checked symbolically with sympy).
* **Dimensions.** $[R\sin\phi] = [R\cos\phi] = \text{m}$; $[K] = [\alpha m\omega^2] = \text{kg}\cdot\text{s}^{-2} = \text{N/m}$; $[\ddot\phi] = [\omega^2] = \text{s}^{-2}$; $[N_n] = [m\omega^2R] = \text{kg}\cdot\text{m}\cdot\text{s}^{-2} = \text{N}$; $[E_1^P] = [m\omega^2R^2] = \text{J}$; $[z_{max}] = [\beta R] = \text{m}$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 30 in its solution keys, so the results are verified by independent derivation (energy equivalence of part (c) and the symbolic inertial check above).

---

## Problem 33: Two Repelling Particles on a Rotating Parabola

### Reference Frames, Bases and Coordinates
* **System:** two particles $P_1$, $P_2$ of mass $m$ slide on a smooth parabolic wire $z = x^2/(2L)$ that spins about its vertical axis $Oz$ at constant $\omega$. They repel each other with $F_E = k/d^2$ along the line that joins them, and both are heavy.
* **Why the rotating frame $Oxyz$.** In $Oxyz$ the wire is fixed, so each particle is located by a single coordinate $x_i$ and its relative kinematics is that of a point on a fixed plane curve. The frame rotates uniformly about a fixed axis through $O$, so the inertia forces reduce to the centrifugal and Coriolis forces (Slide 28), and the centrifugal force has a potential (Slide 30).
* **Hypotheses:** <br>1. The frame $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, with $O$ the vertex of the parabola and $\mathbf{k}_0$ vertical upward, is inertial. <br>2. The wire is smooth and bilateral (each particle is a bead): its reaction on $P_i$ is perpendicular to the wire, with components in the plane of the wire and along $\mathbf{j}_1$. <br>3. $\omega$ is kept constant by the motor; the axis bearings exert no torque about $Oz$. <br>4. Electric repulsion is a central internal force: equal and opposite on the two particles, along $\overrightarrow{P_2P_1}$.
* **Fixed (inertial) frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, basis $\mathcal{B}_0$, origin at the vertex of the parabola, which lies on the axis and is fixed.
* **Moving frame:** $S_1 = Oxyz = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, basis $\mathcal{B}_1$, attached to the wire, with the wire in the plane $Oxz$ and $\mathbf{k}_1 = \mathbf{k}_0$ along the axis. The two frames share the origin $O$. We choose $\mathbf{i}_1 = \mathbf{i}_0$ at $t = 0$.
* **Local basis of the wire at $P_i$:** unit tangent $\mathbf{t}_i$, in-plane unit normal $\mathbf{n}_i$ and $-\mathbf{j}_1$; deduced in the next section.
* **Degrees of freedom:** two, the abscissas $x_1$ and $x_2$ in $Oxyz$ (each bead has 3 coordinates and 2 constraints: $y = 0$ and $z = x^2/(2L)$). In part (e) the symmetry constraint $x_2 = -x_1$ leaves one.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of each particle | kg |
| $L$ | parameter of the parabola $z = x^2/(2L)$ (the radius of curvature at the vertex) | m |
| $\omega$ | constant angular velocity of the wire | rad/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $k$ | electric repulsion constant, $F_E = k/d^2$ | N$\cdot$m$^2$ |
| $\gamma = g/(\omega^2L)$ | weight versus centrifugal force | 1 |
| $\kappa = k/(m\omega^2L^3)$ | repulsion versus centrifugal force | 1 |

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p33-top-view.svg]]

The rotation is about the vertical $\mathbf{k}_0$, so it is drawn looking down the axis, from $+z$. In that view $\mathbf{k}_0$ points out of the paper, towards the reader ($\odot$). Take $\mathbf{i}_0$ to the right; then $\mathbf{j}_0 = \mathbf{k}_0\times\mathbf{i}_0$ (right-hand rule: thumb along $\mathbf{k}_0$, towards the reader, fingers turning $\mathbf{i}_0$ counter-clockwise by $90^\circ$) points up the page. With $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_0$, $\omega \gt 0$, the wire turns counter-clockwise in this view, and after a time $t$ it has turned the angle $\omega t$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of a dashed right triangle: its leg adjacent to $\omega t$ lies along $\mathbf{i}_0$ and measures $\cos\omega t$; its opposite leg lies along $+\mathbf{j}_0$ and measures $\sin\omega t$. So $\mathbf{i}_1 = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ (up the page) and turns counter-clockwise, so its tip moves to the left: its leg along $\mathbf{j}_0$ (adjacent) is $\cos\omega t$ and its leg along $-\mathbf{i}_0$ (opposite) is $\sin\omega t$. So $\mathbf{j}_1 = -\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0$; **the minus sign comes from the counter-clockwise turn carrying the upward axis to the left.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

The plane of the wire contains $\mathbf{i}_1$ and $\mathbf{k}_1$, so in this view it is seen edge-on as the dotted line along $\mathbf{i}_1$; $P_1$ ($x_1 \lt 0$) and $P_2$ ($x_2 \gt 0$) lie on it, on either side of the axis. The columns of $[{}_0R_1]$ are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1\cdot\left(\cos\omega t\cos\omega t - (-\sin\omega t)\sin\omega t\right) = \cos^2\omega t + \sin^2\omega t = 1 $$

The columns have unit length ($\cos^2\omega t + \sin^2\omega t = 1$) and are mutually orthogonal (first and second: $-\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0$; the third is orthogonal to both because their third components are zero), so $[{}_0R_1][{}_0R_1]^T = I$.

* **Motion of $S_1$:** $\mathbf{r}_0^O = \mathbf{v}_0^O = \mathbf{a}_0^O = \mathbf{0}$; $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_1$; $\boldsymbol{\alpha}_{10} = \mathbf{0}$ because $\omega$ is constant. Poisson check with the chain rule: $\left.\frac{d\mathbf{i}_1}{dt}\right|_0 = -\omega\sin\omega t\,\mathbf{i}_0 + \omega\cos\omega t\,\mathbf{j}_0 = \omega\,\mathbf{j}_1$, and indeed $\omega\mathbf{k}_1\times\mathbf{i}_1 = \omega\,\mathbf{j}_1$.

#### The position vectors and the local basis of the wire

![[attachments/EM-SOL/p33-wire-plane.svg]]

The plane $Oxz$ is fixed in $S_1$; it is drawn with $\mathbf{i}_1$ to the right and $\mathbf{k}_1$ up. The direction out of the paper is $\mathbf{i}_1\times\mathbf{k}_1 = -\mathbf{j}_1$, so $\mathbf{j}_1$ points **into** the paper ($\otimes$).

**Position.** A bead at abscissa $x_i$ is reached from $O$ by moving $x_i$ along $\mathbf{i}_1$ and then the height of the wire at that abscissa, $z_i = x_i^2/(2L)$, along $\mathbf{k}_1$ (the two dashed components drawn for $P_2$):

$$ \mathbf{r}_1^{P_i} = x_i\,\mathbf{i}_1 + \frac{x_i^2}{2L}\,\mathbf{k}_1, \qquad i = 1, 2 $$

**Tangent.** A tangent vector is the derivative of the position with respect to the coordinate; with $\frac{d}{dx}\left(\frac{x^2}{2L}\right) = \frac{2x}{2L} = \frac{x}{L}$:

$$ \frac{d}{dx}\left(x\,\mathbf{i}_1 + \frac{x^2}{2L}\mathbf{k}_1\right) = \mathbf{i}_1 + \frac{x}{L}\,\mathbf{k}_1 $$

It is the hypotenuse of the shaded slope triangle at $P_2$: horizontal leg $1$, vertical leg $dz/dx = x_i/L$, hence length $s_i = \sqrt{1 + x_i^2/L^2}$ (Pythagoras). Dividing by $s_i$:

$$ \mathbf{t}_i = \frac{1}{s_i}\left(\mathbf{i}_1 + \frac{x_i}{L}\mathbf{k}_1\right), \qquad \mathbf{n}_i = \frac{1}{s_i}\left(-\frac{x_i}{L}\mathbf{i}_1 + \mathbf{k}_1\right) $$

$\mathbf{n}_i$ is $\mathbf{t}_i$ turned $90^\circ$ counter-clockwise in the drawing (the components $(a, b)$ become $(-b, a)$), which points towards the concave side of the parabola, upwards and towards the axis. They are orthogonal, $\mathbf{t}_i\cdot\mathbf{n}_i = \dfrac{1}{s_i^2}\left(-\dfrac{x_i}{L} + \dfrac{x_i}{L}\right) = 0$, both have length $\sqrt{1 + x_i^2/L^2}/s_i = 1$, and, using $\mathbf{i}_1\times\mathbf{k}_1 = -\mathbf{j}_1$ and $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$,

$$ \mathbf{t}_i\times\mathbf{n}_i = \frac{1}{s_i^2}\left[\mathbf{i}_1\times\mathbf{k}_1 - \frac{x_i^2}{L^2}\,\mathbf{k}_1\times\mathbf{i}_1\right] = \frac{1}{s_i^2}\left[-\mathbf{j}_1 - \frac{x_i^2}{L^2}\mathbf{j}_1\right] = -\mathbf{j}_1 $$

(the direction out of the paper), so $\{\mathbf{t}_i, \mathbf{n}_i, -\mathbf{j}_1\}$ is a right-handed orthonormal triad attached to the wire at $P_i$. The reaction of the smooth wire lies in the plane spanned by $\mathbf{n}_i$ and $\mathbf{j}_1$.

#### The chord between the beads

![[attachments/EM-SOL/p33-chord.svg]]

The repulsion acts along the chord $P_1P_2$. With $\Delta x = x_1 - x_2$, the shaded right triangle has the horizontal leg $|\Delta x|$, the vertical leg $\Delta z = z_1 - z_2 = \dfrac{x_1^2 - x_2^2}{2L} = \Delta x\,\dfrac{x_1 + x_2}{2L}$ (difference of squares) and the hypotenuse $d$. Hence

$$ \overrightarrow{P_2P_1} = \mathbf{r}_1^{P_1} - \mathbf{r}_1^{P_2} = \Delta x\left[\mathbf{i}_1 + \frac{x_1 + x_2}{2L}\mathbf{k}_1\right], \qquad d^2 = |\overrightarrow{P_2P_1}|^2 = \Delta x^2\left[1 + \frac{(x_1 + x_2)^2}{4L^2}\right] $$

so the slope of the chord is $(x_1 + x_2)/(2L)$, the mean of the slopes $x_i/L$ at its ends.

### Kinematics

##### (a) Relative position, velocity and acceleration
* **Pedagogical Justification:** Relative kinematics is computed in $S_1$, where $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ are constant, so only the scalar components are differentiated. Each $z_i = x_i^2/(2L)$ depends on time through $x_i(t)$, so the chain rule is needed.

Chain rule: $\dfrac{d}{dt}\left(\dfrac{x_i^2}{2L}\right) = \dfrac{2x_i}{2L}\,\dot x_i = \dfrac{x_i\dot x_i}{L}$. Hence

$$ \mathbf{v}_1^{P_i} = \dot x_i\,\mathbf{i}_1 + \frac{x_i\dot x_i}{L}\,\mathbf{k}_1 $$

Product rule on $x_i\dot x_i$: $\dfrac{d}{dt}(x_i\dot x_i) = \dot x_i\dot x_i + x_i\ddot x_i$. Hence

$$ \mathbf{a}_1^{P_i} = \ddot x_i\,\mathbf{i}_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\,\mathbf{k}_1 $$

Note $\mathbf{v}_1^{P_i} = s_i\dot x_i\,\mathbf{t}_i$, tangent to the wire, as it must be.

### Forces and Equations of Motion

##### (b) Newton's second law in $Oxyz$
* **Pedagogical Justification:** $Oxyz$ is not inertial; Newton's law holds there if the inertia forces are added, $m\mathbf{a}_1^{P_i} = \mathbf{F} + \mathbf{F}_i$ (Notes Eqs. 4.62–4.63). Projecting on the tangent $\mathbf{t}_i$ eliminates the unknown reaction and gives the equation of motion; the other two projections give the reaction.

**Actual forces on $P_i$:**

* Weight: $-mg\,\mathbf{k}_1$.
* Reaction of the smooth wire: $\mathbf{N}_i = N_{in}\,\mathbf{n}_i + N_{iy}\,\mathbf{j}_1$ (so $\mathbf{N}_i\cdot\mathbf{t}_i = 0$).
* Electric repulsion. With $\overrightarrow{P_2P_1}$ and $d$ of the chord triangle, the force on $P_1$ has magnitude $k/d^2$ and the direction of $\overrightarrow{P_2P_1}/d$, and the force on $P_2$ is opposite:
$$ \mathbf{F}_{E1} = \frac{k}{d^2}\,\frac{\overrightarrow{P_2P_1}}{d} = \frac{k}{d^3}\,\Delta x\left[\mathbf{i}_1 + \frac{x_1 + x_2}{2L}\mathbf{k}_1\right] = -\mathbf{F}_{E2} $$

**Inertia forces** ($\mathbf{a}_0^O = \mathbf{0}$, $\boldsymbol{\alpha}_{10} = \mathbf{0}$, so $\mathbf{F}_A = \mathbf{F}_E^{\text{Euler}} = \mathbf{0}$):

* Centrifugal: $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^{P_i} = \omega\mathbf{k}_1\times\left(x_i\mathbf{i}_1 + \tfrac{x_i^2}{2L}\mathbf{k}_1\right) = \omega x_i\,\mathbf{j}_1$, then $\boldsymbol{\omega}_{10}\times\omega x_i\mathbf{j}_1 = \omega^2x_i\,(\mathbf{k}_1\times\mathbf{j}_1) = -\omega^2x_i\,\mathbf{i}_1$, so $\mathbf{F}_{C,i} = m\omega^2x_i\,\mathbf{i}_1$ (outward from the axis, Slide 30).
* Coriolis: $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^{P_i} = \omega\mathbf{k}_1\times\left(\dot x_i\mathbf{i}_1 + \tfrac{x_i\dot x_i}{L}\mathbf{k}_1\right) = \omega\dot x_i\,\mathbf{j}_1$, so $\mathbf{F}_{COR,i} = -2m\omega\dot x_i\,\mathbf{j}_1$.

##### (b, continued) Newton's equations

**Newton's second law for each particle** (vector form):

$$ m\left[\ddot x_i\,\mathbf{i}_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\,\mathbf{k}_1\right] = -mg\,\mathbf{k}_1 + N_{in}\,\mathbf{n}_i + N_{iy}\,\mathbf{j}_1 + \mathbf{F}_{Ei} + m\omega^2x_i\,\mathbf{i}_1 - 2m\omega\dot x_i\,\mathbf{j}_1, \qquad i = 1, 2 $$

**Projection on $s_i\mathbf{t}_i = \mathbf{i}_1 + \dfrac{x_i}{L}\mathbf{k}_1$** (no reaction). Left side: $m\left[\ddot x_i + \dfrac{x_i}{L}\cdot\dfrac{\dot x_i^2 + x_i\ddot x_i}{L}\right] = m\left[\left(1 + \dfrac{x_i^2}{L^2}\right)\ddot x_i + \dfrac{x_i\dot x_i^2}{L^2}\right]$. Right side: weight $-mg\,x_i/L$; centrifugal $m\omega^2x_i$; Coriolis $0$; electric, for $P_1$,

$$ \mathbf{F}_{E1}\cdot\left(\mathbf{i}_1 + \frac{x_1}{L}\mathbf{k}_1\right) = \frac{k}{d^3}\,(x_1 - x_2)\left[1 + \frac{x_1(x_1 + x_2)}{2L^2}\right] $$

and for $P_2$ the same with the indices exchanged (because $\mathbf{F}_{E2} = -\mathbf{F}_{E1}$ and $-\Delta x = x_2 - x_1$). The **equations of motion** are

$$ \boxed{m\left[\left(1 + \frac{x_1^2}{L^2}\right)\ddot x_1 + \frac{x_1\dot x_1^2}{L^2}\right] = m\left(\omega^2 - \frac{g}{L}\right)x_1 + \frac{k}{d^3}\,(x_1 - x_2)\left[1 + \frac{x_1(x_1 + x_2)}{2L^2}\right]} $$
$$ \boxed{m\left[\left(1 + \frac{x_2^2}{L^2}\right)\ddot x_2 + \frac{x_2\dot x_2^2}{L^2}\right] = m\left(\omega^2 - \frac{g}{L}\right)x_2 + \frac{k}{d^3}\,(x_2 - x_1)\left[1 + \frac{x_2(x_1 + x_2)}{2L^2}\right]} $$

with $d^3 = |x_1 - x_2|^3\left[1 + \dfrac{(x_1 + x_2)^2}{4L^2}\right]^{3/2}$.

**Projection on $\mathbf{j}_1$:** $0 = N_{iy} - 2m\omega\dot x_i$, so $\boxed{N_{iy} = 2m\omega\dot x_i}$: the wire pushes each bead sideways to cancel the Coriolis force.

**Projection on $s_i\mathbf{n}_i = -\dfrac{x_i}{L}\mathbf{i}_1 + \mathbf{k}_1$.** Left side: $m\left[-\dfrac{x_i\ddot x_i}{L} + \dfrac{\dot x_i^2 + x_i\ddot x_i}{L}\right] = \dfrac{m\dot x_i^2}{L}$. Right side: $N_{in}s_i - mg - \dfrac{m\omega^2x_i^2}{L} + \mathbf{F}_{Ei}\cdot(s_i\mathbf{n}_i)$, where for $P_1$

$$ \mathbf{F}_{E1}\cdot\left(-\frac{x_1}{L}\mathbf{i}_1 + \mathbf{k}_1\right) = \frac{k\,\Delta x}{d^3}\left[-\frac{x_1}{L} + \frac{x_1 + x_2}{2L}\right] = \frac{k\,\Delta x}{d^3}\cdot\frac{x_2 - x_1}{2L} = -\frac{k\,\Delta x^2}{2Ld^3} $$

and the same value is found for $P_2$. Therefore

$$ \boxed{N_{in} = \frac{m}{s_i}\left[\frac{\dot x_i^2}{L} + g + \frac{\omega^2x_i^2}{L}\right] + \frac{k\,(x_1 - x_2)^2}{2L\,s_i\,d^3}}, \qquad s_i = \sqrt{1 + \frac{x_i^2}{L^2}} $$

### Answers and Checks

##### (a) Relative position, velocity and acceleration
$$ \mathbf{r}_1^{P_i} = x_i\,\mathbf{i}_1 + \frac{x_i^2}{2L}\,\mathbf{k}_1, \qquad \mathbf{v}_1^{P_i} = \dot x_i\,\mathbf{i}_1 + \frac{x_i\dot x_i}{L}\,\mathbf{k}_1, \qquad \mathbf{a}_1^{P_i} = \ddot x_i\,\mathbf{i}_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\,\mathbf{k}_1 \qquad (i = 1, 2) $$

##### (b) Newton's second law in $Oxyz$
The vector equation of each bead, with its tangential projections (the two boxed equations of motion), $N_{iy} = 2m\omega\dot x_i$ and the boxed $N_{in}$, all derived in the previous section.

##### (c) Motor torque that keeps $\omega$ constant
* **Pedagogical Justification:** The motor torque acts on the wire; the wire acts on the particles through the reactions $\mathbf{N}_i$, and the particles act back with $-\mathbf{N}_i$. The wire is a massless guide (if it had mass and were symmetric about $Oz$, rotating at constant $\omega$, its own angular momentum about $Oz$ would be constant; this remark goes beyond the particle units and does not change the result). Hence the moment about $Oz$ of all the actions on it must vanish.

**Balance of moments about $Oz$ on the wire:** $M + \sum_i \left[\mathbf{r}^{P_i}\times(-\mathbf{N}_i)\right]\cdot\mathbf{k}_1 = 0$. Expand the cross product with $\mathbf{r}^{P_i} = x_i\mathbf{i}_1 + z_i\mathbf{k}_1$ and $\mathbf{N}_i = N_{ix}\mathbf{i}_1 + N_{iy}\mathbf{j}_1 + N_{iz}\mathbf{k}_1$; its $\mathbf{k}_1$ component is $x_iN_{iy} - 0\cdot N_{ix} = x_iN_{iy}$. With $N_{iy} = 2m\omega\dot x_i$ from part (b):

$$ \boxed{M = x_1N_{1y} + x_2N_{2y} = 2m\omega\left(x_1\dot x_1 + x_2\dot x_2\right)} $$

**Check with the angular momentum of the particles in $S_0$.** By Notes Eq. 3.26, $\mathbf{v}_0^{P_i} = \mathbf{v}_1^{P_i} + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^{P_i} = \dot x_i\mathbf{i}_1 + \omega x_i\mathbf{j}_1 + \tfrac{x_i\dot x_i}{L}\mathbf{k}_1$, whose $\mathbf{k}_1$-moment about $O$ is $m\left[x_i(\omega x_i) - 0\cdot\dot x_i\right] = m\omega x_i^2$. So $H_{Oz} = m\omega(x_1^2 + x_2^2)$ and, by the product and chain rules, $\dot H_{Oz} = 2m\omega(x_1\dot x_1 + x_2\dot x_2)$. The weights are parallel to $Oz$ and the electric pair is central ($(\mathbf{r}^{P_1} - \mathbf{r}^{P_2})\times\mathbf{F}_{E1} = \mathbf{0}$), so only the reactions have a moment about $Oz$, and that moment equals $M$. Both routes agree with the official key (Problems.pdf, p. 75).

##### (d) Equilibrium configurations in $Oxyz$
* **Pedagogical Justification:** A relative equilibrium has $\dot x_i = \ddot x_i = 0$; then the two equations of motion become algebraic. Writing them with $u_i = x_i/L$ and dividing by $m\omega^2L$ shows that only $\gamma$ and $\kappa$ matter.

With $\dot x_i = \ddot x_i = 0$, $x_i = Lu_i$ and $d = LD$, $D = |u_1 - u_2|\sqrt{1 + (u_1 + u_2)^2/4}$, dividing by $m\omega^2L$:

$$ f_1 \equiv (1 - \gamma)\,u_1 + \frac{\kappa}{D^3}(u_1 - u_2)\left[1 + \frac{u_1(u_1 + u_2)}{2}\right] = 0, \qquad f_2 \equiv (1 - \gamma)\,u_2 + \frac{\kappa}{D^3}(u_2 - u_1)\left[1 + \frac{u_2(u_1 + u_2)}{2}\right] = 0 $$

**Sum.** With $S = u_1 + u_2$, the electric terms add to $\dfrac{\kappa}{D^3}(u_1 - u_2)\left[\dfrac{u_1S}{2} - \dfrac{u_2S}{2}\right] = \dfrac{\kappa\,(u_1 - u_2)^2S}{2D^3}$, so

$$ f_1 + f_2 = S\left[(1 - \gamma) + \frac{\kappa\,(u_1 - u_2)^2}{2D^3}\right] = 0 $$

Either $S = 0$ (symmetric configuration) or $\gamma - 1 = \dfrac{\kappa(u_1 - u_2)^2}{2D^3} \gt 0$.

**Case $\gamma \lt 1$.** If $S = 0$, $u_2 = -u_1$, $D = 2|u_1|$ and $f_1 = u_1\left[(1 - \gamma) + \dfrac{2\kappa}{8|u_1|^3}\right]$: both terms of the bracket are positive and $u_1 \neq 0$ (the particles cannot coincide), so $f_1 \neq 0$. If $S \neq 0$ the bracket of the sum is positive. **No equilibrium exists.** (Centrifugal force beats gravity everywhere and the repulsion only pushes the particles further out.)

**Case $\gamma = 1$.** Both alternatives require $\kappa = 0$. For $\kappa \gt 0$ there is no equilibrium; only without repulsion ($\kappa = 0$) is every configuration an equilibrium (gravity and centrifugal force balance along the wire at every point: $(\omega^2 - g/L)x_i = 0$).

**Case $\gamma \gt 1$, symmetric ($x_2 = -x_1$).** $f_1 = u_1\left[(1 - \gamma) + \dfrac{\kappa}{4|u_1|^3}\right] = 0$ gives $|u_1|^3 = \dfrac{\kappa}{4(\gamma - 1)}$:

$$ \boxed{x_1 = -x_2, \qquad x_1^2 = \left[\frac{\kappa L^3}{4(\gamma - 1)}\right]^{2/3}} $$

**Case $\gamma \gt 1$, asymmetric ($S \neq 0$).** Insert $\dfrac{\kappa}{D^3} = \dfrac{2(\gamma - 1)}{(u_1 - u_2)^2}$ from the sum into $f_1 = 0$ and divide by $(\gamma - 1)$:

$$ -u_1 + \frac{2}{u_1 - u_2}\left[1 + \frac{u_1(u_1 + u_2)}{2}\right] = 0 \implies u_1(u_1 - u_2) = 2 + u_1(u_1 + u_2) \implies \boxed{x_1x_2 = -L^2} $$

The particles are on opposite branches and the chord $P_1P_2$ passes through the focus $(0, L/2)$ of the parabola. Then $u_2 = -1/u_1$, $S = u_1 - 1/u_1$, $u_1 - u_2 = u_1 + 1/u_1$, and $1 + S^2/4 = (u_1 + 1/u_1)^2/4$, so $D^3 = |u_1 + 1/u_1|^6/8$ and the sum condition becomes

$$ \gamma - 1 = \frac{4\kappa}{(u_1 + 1/u_1)^4} \implies \left|u_1 + \frac{1}{u_1}\right| = \left(\frac{4\kappa}{\gamma - 1}\right)^{1/4} $$

Since $|u_1 + 1/u_1| \ge 2$, with equality only for $|u_1| = 1$ (which is the symmetric equilibrium), **asymmetric equilibria exist if and only if $\kappa \gt 4(\gamma - 1)$**, i.e. exactly when the symmetric equilibrium lies at $|x_1| \gt L$. They come in mirror pairs, $u_1 = \tfrac12\left[q \pm \sqrt{q^2 - 4}\right]$ with $q = (4\kappa/(\gamma - 1))^{1/4}$ and $u_2 = -1/u_1$ (plus the configurations with the labels exchanged). No equilibrium has both particles on the same branch.

##### (e) Symmetric motion with $\gamma = \kappa = 2$: turning points
* **Pedagogical Justification:** In $Oxyz$ the wire (and the symmetry constraint) is fixed, $\boldsymbol{\omega}_{10}$ is constant and the origin is fixed. The reactions and the Coriolis forces do no work in $S_1$ (Slide 31), and the weights, the electric pair and the centrifugal forces have potentials (Slides 29–30). The mechanical energy of the pair in $S_1$ is therefore conserved, and its turning points ($\dot x_1 = 0$) give the extreme values of $x_1$.

Put $x_1 = x \gt 0$, $x_2 = -x$ (the repulsion becomes infinite at $x = 0$, so $x_1$ stays positive). Then $d = 2x$ and, for each particle, $|\mathbf{v}_1^{P_i}|^2 = \dot x^2\left(1 + x^2/L^2\right)$.

* Kinetic energy: $T_1 = 2\cdot\tfrac12 m\dot x^2\left(1 + \dfrac{x^2}{L^2}\right) = m\dot x^2\left(1 + \dfrac{x^2}{L^2}\right)$.
* Gravity: $2\,mg\,\dfrac{x^2}{2L} = \dfrac{mgx^2}{L}$. Centrifugal: $2\left(-\tfrac12 m\omega^2x^2\right) = -m\omega^2x^2$. Electric: $\dfrac{k}{d} = \dfrac{k}{2x}$ (its gradient gives the repulsion $k/d^2$).
$$ E_1 = m\dot x^2\left(1 + \frac{x^2}{L^2}\right) + m\left(\frac{g}{L} - \omega^2\right)x^2 + \frac{k}{2x} = \text{const} $$

**Initial value.** $|\mathbf{v}_1^{P_1}(0)| = L\omega$ at $x = L$ gives $2\dot x(0)^2 = L^2\omega^2$, so $T_1(0) = mL^2\omega^2$ and $E_1 = mL^2\omega^2 + m(g/L - \omega^2)L^2 + k/(2L)$. Dividing by $m\omega^2L^2$, with $u = x/L$:

$$ \frac{E_1}{m\omega^2L^2} = \gamma + \frac{\kappa}{2} = 3 \qquad (\gamma = \kappa = 2) $$

**Turning points** ($\dot x = 0$): $(\gamma - 1)u^2 + \dfrac{\kappa}{2u} = \gamma + \dfrac{\kappa}{2}$, i.e. $u^2 + \dfrac1u = 3$. Multiply by $u \gt 0$:

$$ \boxed{\frac{x_1^3}{L^3} - 3\,\frac{x_1}{L} + 1 = 0} $$

**Roots.** With $u = 2\cos\theta$ and $4\cos^3\theta - 3\cos\theta = \cos3\theta$: $8\cos^3\theta - 6\cos\theta + 1 = 2\cos3\theta + 1 = 0$, so $\cos3\theta = -\tfrac12$ and $\theta = 2\pi/9,\ 4\pi/9,\ 8\pi/9$. The roots are $u = 2\cos(2\pi/9) = 1.532$, $2\cos(4\pi/9) = 0.347$ and $2\cos(8\pi/9) = -1.879$ (rejected, $x_1 \gt 0$). Since the starting point $u = 1$ lies between the two positive roots (there $u^2 + 1/u = 2 \lt 3$),

$$ x_{1,\min} = 2L\cos\frac{4\pi}{9} \approx 0.347\,L, \qquad x_{1,\max} = 2L\cos\frac{2\pi}{9} \approx 1.532\,L $$

and $x_1$ oscillates between them. The key also lists $x_1^3/L^3 - 3x_1/L - 1 = 0$ for $x_1 \lt 0$: that is the mirror image (a start on the negative branch) and does not apply to $x_1(0) = L \gt 0$.

##### Checks
* **Effective spring along the wire.** Gravity and the centrifugal force combine into $m(\omega^2 - g/L)x_i$ in the tangential equation: a restoring force if $\gamma \gt 1$ (gravity wins and pulls the beads to the vertex) and a repelling one if $\gamma \lt 1$. Equilibrium requires the repulsion to be balanced by this restoring force, hence the condition $\gamma \gt 1$.
* **Limits.** $\kappa \to 0$: the symmetric equilibrium collapses to $x_1 = x_2 = 0$ (no repulsion to separate the beads). $\gamma \to 1^+$: $x_1^2 \to \infty$, the restoring force vanishes and the beads are pushed to infinity. At the vertex, $x_i = 0$ gives $\mathbf{t}_i = \mathbf{i}_1$ and $\mathbf{n}_i = \mathbf{k}_1$, as the slope triangle degenerates to its horizontal leg.
* **Torque sign.** $M = \tfrac{d}{dt}\left[m\omega(x_1^2 + x_2^2)\right]$: when the beads move outward the moment of inertia of the system grows and the motor has to supply angular momentum ($M \gt 0$); when they move inward it must brake ($M \lt 0$).
* **Orthogonality:** $\mathbf{t}_i\cdot\mathbf{n}_i = 0$, $\mathbf{t}_i\times\mathbf{n}_i = -\mathbf{j}_1$ and $\det[{}_0R_1] = 1$ (change-of-basis section).
* **Inertial check.** Differentiating $[{}_0R_1]\mathbf{r}_1^{P_i}$ twice reproduces $\mathbf{a}_1^{P_i} + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^{P_i}) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^{P_i}$ (Notes Eq. 3.27), and $dE_1/dt = 0$ along the equations of motion of part (b) (both checked symbolically with sympy, together with the equilibria of part (d)).
* **Dimensions.** $[x_i^2/(2L)] = \text{m}$, $[x_i/L] = 1$; $[k/d^2] = \text{N}\cdot\text{m}^2/\text{m}^2 = \text{N}$; $[m\omega^2x] = \text{kg}\cdot\text{s}^{-2}\cdot\text{m} = \text{N}$; $[M] = [m\omega x\dot x] = \text{kg}\cdot\text{s}^{-1}\cdot\text{m}\cdot\text{m/s} = \text{N}\cdot\text{m}$; $[\gamma] = \dfrac{\text{m/s}^2}{\text{s}^{-2}\,\text{m}} = 1$; $[\kappa] = \dfrac{\text{N}\cdot\text{m}^2}{\text{kg}\cdot\text{s}^{-2}\cdot\text{m}^3} = 1$.
* **Check against the official key:** the key of `Problems.pdf` gives the motor torque $2m\omega\left(\dot x_1x_1 + \dot x_2x_2\right)$, the equilibrium cases ($\gamma \lt 1$: none; $\gamma = 1$: only for $\kappa = 0$; $\gamma \gt 1$: symmetric with $x_1 = -x_2$ and $x_1^2 = \left[\kappa L^3/\left(4(\gamma - 1)\right)\right]^{2/3}$, and asymmetric ones) and the turning-point equations $x_1^3/L^3 - 3x_1/L \pm 1 = 0$. They coincide with the results of (c), (d) and (e) (for $\gamma = \kappa = 2$ the turning-point condition $u^3 - 3u + 1 = 0$ is the positive-$x_1$ case).

---

## Problem 34: Particle on a Circular Wire in an Oscillating Vertical Plane

### Reference Frames, Bases and Coordinates
* **System:** a heavy bead $P$ (mass $m$) slides on a smooth circular wire of radius $R$ whose centre $C$ lies on the $Ox$ axis at distance $R$ from $O$ (the circle passes through $O$). The vertical plane $Oxy$ of the wire swings about the vertical axis $Oy$ with the prescribed angular velocity $\boldsymbol{\Omega}(t) = A\omega\sin(\omega t)\,\mathbf{j}$.
* **Why the frame $Oxyz$.** The wire is fixed in $Oxyz$, so $P$ is described by the single angle $\varphi$ and its relative kinematics is that of circular motion. Because $\Omega$ depends on time, the inertia forces now include the **Euler force** $-m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P$ (Slide 28), which has no potential (Slide 31), and the centrifugal potential depends explicitly on time; the energy discussion of part (c) depends on both facts.
* **Hypotheses:** <br>1. A frame $S_0$ with origin $O$ on the fixed vertical axis is inertial; $Oy$ is vertical upward and gravity is $-g\,\mathbf{j}$. <br>2. The wire is smooth and bilateral: the reaction is perpendicular to the tangent of the wire, with a radial component in the plane of the wire and a component along $\mathbf{k}_1$, normal to the plane. <br>3. The rotation of the plane is prescribed (imposed by an external drive whatever the motion of $P$).
* **Fixed (inertial) frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, basis $\mathcal{B}_0$, with $\mathbf{j}_0$ along the vertical rotation axis $Oy$.
* **Moving frame:** $S_1 = Oxyz = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, basis $\mathcal{B}_1$, attached to the plane of the wire ($\mathbf{i}_1$ along $Ox$, $\mathbf{j}_1$ along $Oy$ upward, $\mathbf{k}_1 = \mathbf{i}_1\times\mathbf{j}_1$ normal to the plane), with $\mathbf{j}_1 = \mathbf{j}_0$ (the rotation axis) and $S_1$ coinciding with $S_0$ at $t = 0$.
* **Polar basis of the wire** $\{\mathbf{e}_r, \mathbf{e}_\varphi, \mathbf{k}_1\}$ at $P$, attached to the centre $C$; deduced in the next section.
* **Degrees of freedom:** one, the angle $\varphi$ of $\overrightarrow{CP}$ measured from $Ox$ (3 coordinates minus 2 constraints: $z = 0$ and the circle of centre $C$).

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $R$ | radius of the wire ($OC = R$) | m |
| $A$ | amplitude parameter of $\Omega(t)$ | 1 (rad) |
| $\omega$ | frequency of the oscillation of the plane | rad/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\varphi$ | angle of $\overrightarrow{CP}$ from $Ox$ | rad |

### Change of Basis and Position Vector

#### Angle turned by the plane
With $\psi(t)$ the angle of rotation about $\mathbf{j}_0$, $\dot\psi = \Omega(t)$ and $\psi(0) = 0$. Integrating with the substitution $u = \omega\tau$, $du = \omega\,d\tau$ (so $A\omega\sin(\omega\tau)\,d\tau = A\sin u\,du$, and the limits $\tau = 0, t$ become $u = 0, \omega t$), and Barrow's rule:

$$ \psi(t) = \int_0^t A\omega\sin(\omega\tau)\,d\tau = A\int_0^{\omega t}\sin u\,du = A\left[-\cos u\right]_0^{\omega t} = A\left(-\cos\omega t + \cos 0\right) = A\left(1 - \cos\omega t\right) $$

Since $0 \le 1 - \cos\omega t \le 2$, the plane swings between $\psi = 0$ and $\psi = 2A$: it oscillates, it does not spin.

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p34-top-view.svg]]

The rotation is about $\mathbf{j}_0$, so it is drawn looking down the vertical axis, from $+y$. In that view $\mathbf{j}_0$ points out of the paper, towards the reader ($\odot$). Take $\mathbf{i}_0$ to the right. By the right-hand rule $\mathbf{k}_0 = \mathbf{i}_0\times\mathbf{j}_0$: the fingers go from $\mathbf{i}_0$ (right) to $\mathbf{j}_0$ (towards the reader) and the thumb points down the page. So $\mathbf{k}_0$ points down and $-\mathbf{k}_0$ up. A positive rotation $\psi$ about $\mathbf{j}_0$ (thumb towards the reader) is counter-clockwise in this view:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the dashed right triangle. Its leg adjacent to $\psi$ lies along $\mathbf{i}_0$ and measures $\cos\psi$; its leg opposite to $\psi$ points up the page, along $-\mathbf{k}_0$, and measures $\sin\psi$. So $\mathbf{i}_1 = \cos\psi\,\mathbf{i}_0 - \sin\psi\,\mathbf{k}_0$; **the minus sign comes from $\mathbf{k}_0$ pointing down the page in this view.**
* $\mathbf{k}_1$ starts on $\mathbf{k}_0$ (down the page) and turns $\psi$ counter-clockwise, so its tip moves towards $+\mathbf{i}_0$: its leg along $\mathbf{k}_0$ (adjacent) is $\cos\psi$ and its leg along $\mathbf{i}_0$ (opposite) is $+\sin\psi$. So $\mathbf{k}_1 = \sin\psi\,\mathbf{i}_0 + \cos\psi\,\mathbf{k}_0$.
* $\mathbf{j}_1 = \mathbf{j}_0$, the axis of the rotation.

This is the simple rotation of angle $\psi$ about $\mathbf{j}_0$ (Notes Eqs. 1.18–1.20); the columns of $[{}_0R_1]$ are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\psi & 0 & \sin\psi \\ 0 & 1 & 0 \\ -\sin\psi & 0 & \cos\psi \end{pmatrix}, \qquad \det[{}_0R_1] = \cos\psi\cdot\cos\psi - 0 + \sin\psi\cdot\sin\psi = 1 $$

(expansion along the first row: $\cos\psi\,(1\cdot\cos\psi - 0) - 0 + \sin\psi\,(0 - 1\cdot(-\sin\psi))$). The columns are unit vectors and pairwise orthogonal ($\cos\psi\sin\psi - \sin\psi\cos\psi = 0$), so $[{}_0R_1][{}_0R_1]^T = I$. Poisson check, with the chain rule $\frac{d}{dt}\cos\psi = -\sin\psi\,\dot\psi$ and $\frac{d}{dt}\sin\psi = \cos\psi\,\dot\psi$: $\left.\dfrac{d\mathbf{i}_1}{dt}\right|_0 = \dot\psi\left(-\sin\psi\,\mathbf{i}_0 - \cos\psi\,\mathbf{k}_0\right) = -\dot\psi\,\mathbf{k}_1$, and indeed $\Omega\,\mathbf{j}_1\times\mathbf{i}_1 = -\Omega\,\mathbf{k}_1$.

* **Motion of $S_1$:** origin fixed on the axis, $\mathbf{r}_0^O = \mathbf{v}_0^O = \mathbf{a}_0^O = \mathbf{0}$;
$$ \boldsymbol{\omega}_{10} = \Omega(t)\,\mathbf{j}_1 = A\omega\sin(\omega t)\,\mathbf{j}_1, \qquad \boldsymbol{\alpha}_{10} = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 = \dot\Omega\,\mathbf{j}_1 = A\omega^2\cos(\omega t)\,\mathbf{j}_1 $$

($\mathbf{j}_1 = \mathbf{j}_0$ is fixed, and the chain rule gives $\tfrac{d}{dt}\sin\omega t = \omega\cos\omega t$.)

#### The position vector in the plane of the wire

![[attachments/EM-SOL/p34-wire-plane.svg]]

The plane $Oxy$ is fixed in $S_1$ and is drawn with $\mathbf{i}_1$ to the right and $\mathbf{j}_1$ up, so $\mathbf{k}_1 = \mathbf{i}_1\times\mathbf{j}_1$ points out of the paper ($\odot$). To go from $O$ to $P$ we pass through the centre, because the distance from $C$ is the one that stays constant:

$$ \mathbf{r}_1^P = \overrightarrow{OC} + \overrightarrow{CP} $$

* $\overrightarrow{OC} = R\,\mathbf{i}_1$: the circle passes through $O$ and its centre lies on $Ox$ at distance $R$.
* $\overrightarrow{CP}$ has length $R$ and makes the angle $\varphi$ with $Ox$. Let $F$ be the foot of the perpendicular from $P$ to the $x$ axis. In the shaded right triangle $CFP$ (right angle at $F$) the hypotenuse is $|CP| = R$, the leg adjacent to $\varphi$ is $CF = R\cos\varphi$, along $\mathbf{i}_1$, and the leg opposite to $\varphi$ is $FP = R\sin\varphi$, along $\mathbf{j}_1$. So $\overrightarrow{CP} = R\cos\varphi\,\mathbf{i}_1 + R\sin\varphi\,\mathbf{j}_1$.

Adding the two vectors:

$$ \mathbf{r}_1^P = R\,(1 + \cos\varphi)\,\mathbf{i}_1 + R\sin\varphi\,\mathbf{j}_1 $$

Checks: $\varphi = \pi$ gives $\mathbf{r}_1^P = \mathbf{0}$ (the point $O$ of the wire); $\varphi = -\pi/2$ gives $R\,\mathbf{i}_1 - R\,\mathbf{j}_1$, the lowest point of the wire. The $\mathbf{i}_1$ component $x = R(1 + \cos\varphi)$ is the distance from $P$ to the rotation axis $Oy$ (the dimension at the bottom of the figure); it is the lever arm of the centrifugal and Euler forces.

**Polar angle.** Here $\varphi$ is measured at $C$ from the direction $+\mathbf{i}_1$, counter-clockwise towards $+\mathbf{j}_1$, so it is already the standard polar angle about $C$; no shift of origin of the angle is needed (unlike an angle measured from a vertical).

**Polar basis.** The radial unit vector is $\overrightarrow{CP}/R$, and the transverse one is its derivative with respect to $\varphi$ ($\frac{d}{d\varphi}\cos\varphi = -\sin\varphi$, $\frac{d}{d\varphi}\sin\varphi = \cos\varphi$):

$$ \mathbf{e}_r = \cos\varphi\,\mathbf{i}_1 + \sin\varphi\,\mathbf{j}_1, \qquad \mathbf{e}_\varphi = \frac{d\mathbf{e}_r}{d\varphi} = -\sin\varphi\,\mathbf{i}_1 + \cos\varphi\,\mathbf{j}_1, \qquad \frac{d\mathbf{e}_\varphi}{d\varphi} = -\cos\varphi\,\mathbf{i}_1 - \sin\varphi\,\mathbf{j}_1 = -\mathbf{e}_r $$

$\mathbf{e}_\varphi$ has length $\sqrt{\sin^2\varphi + \cos^2\varphi} = 1$ and is the tangent to the wire in the direction of increasing $\varphi$. With $\mathbf{i}_1\times\mathbf{j}_1 = \mathbf{k}_1$ and $\mathbf{j}_1\times\mathbf{i}_1 = -\mathbf{k}_1$, $\mathbf{e}_r\times\mathbf{e}_\varphi = \cos^2\varphi\,\mathbf{k}_1 - \sin^2\varphi\,(-\mathbf{k}_1) = (\cos^2\varphi + \sin^2\varphi)\,\mathbf{k}_1 = \mathbf{k}_1$. Its matrix in $\mathcal{B}_1$ (columns $\mathbf{e}_r, \mathbf{e}_\varphi, \mathbf{k}_1$) is a rotation by $\varphi$ about $\mathbf{k}_1$, with determinant $\cos^2\varphi + \sin^2\varphi = 1$. Useful projections: $\mathbf{i}_1\cdot\mathbf{e}_r = \cos\varphi$, $\mathbf{i}_1\cdot\mathbf{e}_\varphi = -\sin\varphi$, $\mathbf{j}_1\cdot\mathbf{e}_r = \sin\varphi$, $\mathbf{j}_1\cdot\mathbf{e}_\varphi = \cos\varphi$.

### Kinematics

##### (a) Relative position, velocity and acceleration
* **Pedagogical Justification:** Relative quantities are derivatives in $S_1$, where $\mathbf{i}_1, \mathbf{j}_1$ are constant; only $\varphi$ depends on time, so each component is differentiated with the chain rule.

With $\tfrac{d}{dt}\cos\varphi = -\sin\varphi\,\dot\varphi$ and $\tfrac{d}{dt}\sin\varphi = \cos\varphi\,\dot\varphi$ applied to $\mathbf{r}_1^P = R\,(1 + \cos\varphi)\,\mathbf{i}_1 + R\sin\varphi\,\mathbf{j}_1$:

$$ \mathbf{v}_1^P = -R\dot\varphi\sin\varphi\,\mathbf{i}_1 + R\dot\varphi\cos\varphi\,\mathbf{j}_1 = R\dot\varphi\,\mathbf{e}_\varphi $$

Product rule on each component, e.g. $\tfrac{d}{dt}\left(-R\dot\varphi\sin\varphi\right) = -R\ddot\varphi\sin\varphi - R\dot\varphi^2\cos\varphi$ and $\tfrac{d}{dt}\left(R\dot\varphi\cos\varphi\right) = R\ddot\varphi\cos\varphi - R\dot\varphi^2\sin\varphi$:

$$ \mathbf{a}_1^P = -R\left(\ddot\varphi\sin\varphi + \dot\varphi^2\cos\varphi\right)\mathbf{i}_1 + R\left(\ddot\varphi\cos\varphi - \dot\varphi^2\sin\varphi\right)\mathbf{j}_1 = R\ddot\varphi\,\mathbf{e}_\varphi - R\dot\varphi^2\,\mathbf{e}_r $$

### Forces and Equations of Motion

##### (b) Forces acting on $P$
* **Pedagogical Justification:** In the non-inertial frame $Oxyz$ we use $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ (Notes Eqs. 4.62–4.63). The actual forces are the weight and the reaction of the wire; the inertia forces follow from Slide 28 with $\mathbf{a}_0^O = \mathbf{0}$, $\boldsymbol{\omega}_{10} = \Omega\mathbf{j}_1$, $\boldsymbol{\alpha}_{10} = \dot\Omega\mathbf{j}_1$.

**Actual forces:**

* Weight: $\mathbf{W} = -mg\,\mathbf{j}_1$.
* Reaction of the smooth wire (no component along the tangent $\mathbf{e}_\varphi$): $\mathbf{N} = N_1\,\mathbf{e}_r + N_2\,\mathbf{k}_1 = N_1\cos\varphi\,\mathbf{i}_1 + N_1\sin\varphi\,\mathbf{j}_1 + N_2\,\mathbf{k}_1$.

**Inertia forces** (cross products with $\mathbf{j}_1\times\mathbf{i}_1 = -\mathbf{k}_1$, $\mathbf{j}_1\times\mathbf{j}_1 = \mathbf{0}$, $\mathbf{j}_1\times\mathbf{k}_1 = \mathbf{i}_1$):

* Origin: $\mathbf{F}_A = -m\mathbf{a}_0^O = \mathbf{0}$.
* Euler: $\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P = \dot\Omega\,\mathbf{j}_1\times\left[R(1 + \cos\varphi)\mathbf{i}_1 + R\sin\varphi\,\mathbf{j}_1\right] = -\dot\Omega R(1 + \cos\varphi)\,\mathbf{k}_1$, so
$$ \mathbf{F}_E = -m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P = mA\omega^2R\cos(\omega t)\,(1 + \cos\varphi)\,\mathbf{k}_1 $$
* Centrifugal: $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = -\Omega R(1 + \cos\varphi)\,\mathbf{k}_1$ and $\boldsymbol{\omega}_{10}\times\left(-\Omega R(1 + \cos\varphi)\mathbf{k}_1\right) = -\Omega^2R(1 + \cos\varphi)\,\mathbf{i}_1$, so (Slide 30, distance to the axis $x = R(1 + \cos\varphi)$)
$$ \mathbf{F}_C = m\Omega^2R\,(1 + \cos\varphi)\,\mathbf{i}_1 = mA^2\omega^2R\sin^2(\omega t)\,(1 + \cos\varphi)\,\mathbf{i}_1 $$
* Coriolis: $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = \Omega R\dot\varphi\,\mathbf{j}_1\times\left(-\sin\varphi\,\mathbf{i}_1 + \cos\varphi\,\mathbf{j}_1\right) = \Omega R\dot\varphi\sin\varphi\,\mathbf{k}_1$, so
$$ \mathbf{F}_{COR} = -2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = -2mA\omega R\dot\varphi\sin(\omega t)\sin\varphi\,\mathbf{k}_1 $$

##### (d) Equation of motion
* **Pedagogical Justification:** The tangential direction $\mathbf{e}_\varphi$ is the only one free of the unknown reaction ($\mathbf{N}\perp\mathbf{e}_\varphi$), and the Euler and Coriolis forces (along $\mathbf{k}_1$) also drop out.

Projections on $\mathbf{e}_\varphi = -\sin\varphi\,\mathbf{i}_1 + \cos\varphi\,\mathbf{j}_1$: $m\mathbf{a}_1^P\cdot\mathbf{e}_\varphi = mR\ddot\varphi$; $\mathbf{W}\cdot\mathbf{e}_\varphi = -mg\cos\varphi$; $\mathbf{F}_C\cdot\mathbf{e}_\varphi = -m\Omega^2R(1 + \cos\varphi)\sin\varphi$. Hence $mR\ddot\varphi = -mg\cos\varphi - m\Omega^2R(1 + \cos\varphi)\sin\varphi$, i.e.

$$ \boxed{\ddot\varphi + \frac{g}{R}\cos\varphi + A^2\omega^2\sin^2(\omega t)\,(1 + \cos\varphi)\sin\varphi = 0} $$

a nonlinear equation with a time-periodic coefficient (parametric forcing). It agrees with the official key.

##### (e) Reaction of the wire
* **Pedagogical Justification:** The remaining two components of $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$, along $\mathbf{e}_r$ and $\mathbf{k}_1$, each contain one reaction component.

**Along $\mathbf{e}_r$:** $m\mathbf{a}_1^P\cdot\mathbf{e}_r = -mR\dot\varphi^2$; $\mathbf{W}\cdot\mathbf{e}_r = -mg\sin\varphi$; $\mathbf{F}_C\cdot\mathbf{e}_r = m\Omega^2R(1 + \cos\varphi)\cos\varphi$. So $-mR\dot\varphi^2 = N_1 - mg\sin\varphi + m\Omega^2R(1 + \cos\varphi)\cos\varphi$:

$$ \boxed{N_1 = mg\sin\varphi - mA^2R\omega^2\,(1 + \cos\varphi)\sin^2(\omega t)\cos\varphi - mR\dot\varphi^2} $$

**Along $\mathbf{k}_1$:** $m\mathbf{a}_1^P\cdot\mathbf{k}_1 = 0 = N_2 + mA\omega^2R\cos(\omega t)(1 + \cos\varphi) - 2mA\omega R\dot\varphi\sin(\omega t)\sin\varphi$:

$$ \boxed{N_2 = 2mAR\omega\,\dot\varphi\sin\varphi\sin(\omega t) - mAR\omega^2\,(1 + \cos\varphi)\cos(\omega t)} $$

and $\mathbf{N} = N_1\cos\varphi\,\mathbf{i}_1 + N_1\sin\varphi\,\mathbf{j}_1 + N_2\,\mathbf{k}_1$. Both components agree with the official key. The normal component $N_2$ is what the wire must supply to drag $P$ along with the swinging plane (it balances the Euler and Coriolis forces).

### Answers and Checks

##### (a) Relative position, velocity and acceleration
$$ \mathbf{r}_1^P = R\,(1 + \cos\varphi)\,\mathbf{i}_1 + R\sin\varphi\,\mathbf{j}_1, \qquad \mathbf{v}_1^P = R\dot\varphi\,\mathbf{e}_\varphi, \qquad \mathbf{a}_1^P = R\ddot\varphi\,\mathbf{e}_\varphi - R\dot\varphi^2\,\mathbf{e}_r $$

##### (b) Forces acting on $P$
Weight $-mg\,\mathbf{j}_1$, reaction $N_1\,\mathbf{e}_r + N_2\,\mathbf{k}_1$, and the inertia forces $\mathbf{F}_A = \mathbf{0}$, $\mathbf{F}_E = mA\omega^2R\cos(\omega t)(1 + \cos\varphi)\,\mathbf{k}_1$, $\mathbf{F}_C = mA^2\omega^2R\sin^2(\omega t)(1 + \cos\varphi)\,\mathbf{i}_1$ and $\mathbf{F}_{COR} = -2mA\omega R\dot\varphi\sin(\omega t)\sin\varphi\,\mathbf{k}_1$.

##### (c) Is the mechanical energy conserved in $Oxy$?
* **Pedagogical Justification:** By Slide 29, $E_1^P$ is conserved only if every force that does work in $S_1$ derives from a potential that does not depend explicitly on time. Compute the power of each force in $S_1$.
* $\mathbf{N}\cdot\mathbf{v}_1^P = R\dot\varphi\,(N_1\mathbf{e}_r + N_2\mathbf{k}_1)\cdot\mathbf{e}_\varphi = 0$ (the wire is fixed in $S_1$).
* $\mathbf{F}_E$ and $\mathbf{F}_{COR}$ are along $\mathbf{k}_1$, normal to the plane in which $\mathbf{v}_1^P$ lies: they do no work. (In general the Euler force has no potential, Slide 31; here it happens to be powerless.)
* The weight has the potential $mgy = mgR\sin\varphi$.
* The centrifugal force has the potential $V_C = -\tfrac12 m\Omega(t)^2x^2$, but **it depends explicitly on time** because $\Omega$ does.

Define $E_1^P = \tfrac12 mR^2\dot\varphi^2 + mgR\sin\varphi - \tfrac12 m\Omega^2R^2(1 + \cos\varphi)^2$. Differentiating with the chain and product rules,

$$ \frac{dE_1^P}{dt} = mR^2\dot\varphi\ddot\varphi + mgR\cos\varphi\,\dot\varphi + m\Omega^2R^2(1 + \cos\varphi)\sin\varphi\,\dot\varphi - m\Omega\dot\Omega R^2(1 + \cos\varphi)^2 $$

The first three terms are $mR^2\dot\varphi$ times the equation of motion of part (d), so they cancel, leaving

$$ \frac{dE_1^P}{dt} = -m\Omega\dot\Omega\,R^2(1 + \cos\varphi)^2 = -mA^2\omega^3R^2\sin(\omega t)\cos(\omega t)\,(1 + \cos\varphi)^2 \neq 0 $$

**No**: the mechanical energy of $P$ in $Oxy$ is not conserved, because the centrifugal potential changes with time (the frame does not rotate at a constant rate). It would be conserved if $\Omega$ were constant. Nor is the energy conserved in $S_0$: there the wire moves and its reaction $N_2\mathbf{k}_1$ does work.

##### (d) Equation of motion
$$ \ddot\varphi + \frac{g}{R}\cos\varphi + A^2\omega^2\sin^2(\omega t)\,(1 + \cos\varphi)\sin\varphi = 0 $$

##### (e) Reaction of the wire
$\mathbf{N} = N_1\,\mathbf{e}_r + N_2\,\mathbf{k}_1$ with the boxed $N_1(\varphi, \dot\varphi, t)$ and $N_2(\varphi, \dot\varphi, t)$ of the previous section.

##### (f) Small oscillations about the lowest point
* **Pedagogical Justification:** For $\delta \ll 1$ the trigonometric functions are replaced by their first-order Taylor expansions; the condition $A^2 \ll g/(R\omega^2)$, i.e. $A^2\omega^2 \ll g/R$, lets us drop the parametric term $A^2\omega^2\sin^2(\omega t)\,\delta$ against $(g/R)\,\delta$. The result is a linear forced oscillator.

With $\varphi = \delta - \pi/2$, the subtraction formulas give $\cos\varphi = \cos\delta\cos\tfrac{\pi}{2} + \sin\delta\sin\tfrac{\pi}{2} = \sin\delta \approx \delta$ and $\sin\varphi = \sin\delta\cos\tfrac{\pi}{2} - \cos\delta\sin\tfrac{\pi}{2} = -\cos\delta \approx -1$; also $\ddot\varphi = \ddot\delta$. Substituting into the equation of part (d) and keeping first-order terms:

$$ \ddot\delta + \frac{g}{R}\,\delta - A^2\omega^2\sin^2(\omega t)\,(1 + \delta) = 0 $$

Dropping $A^2\omega^2\sin^2(\omega t)\,\delta$ (small compared with $(g/R)\,\delta$) and using $\sin^2(\omega t) = \tfrac12\left[1 - \cos(2\omega t)\right]$:

$$ \boxed{\ddot\delta + \frac{g}{R}\,\delta = \frac{A^2\omega^2}{2}\left[1 - \cos(2\omega t)\right]} $$

**Solution.** With $\omega_n = \sqrt{g/R}$, a particular solution is a constant plus a term at $2\omega$. The constant $\delta_0$ satisfies $\omega_n^2\delta_0 = A^2\omega^2/2$. For $\delta_p = C\cos(2\omega t)$, $\ddot\delta_p = -4\omega^2C\cos(2\omega t)$ and $(\omega_n^2 - 4\omega^2)\,C = -A^2\omega^2/2$. Hence

$$ \delta(t) = \frac{A^2R\omega^2}{2g} - \frac{A^2\omega^2}{2\left(\omega_n^2 - 4\omega^2\right)}\cos(2\omega t) + a\cos\omega_nt + b\sin\omega_nt $$

($a$, $b$ set by the initial conditions). The particle oscillates, with natural frequency $\omega_n = \sqrt{g/R}$, about

$$ \boxed{\delta_0 = \frac{A^2R\omega^2}{2g}} $$

which is small, consistent with $A^2 \ll g/(R\omega^2)$. It is positive: on average the bead is displaced slightly outward, away from the axis, by the mean centrifugal force.

**Breakdown.** The forced amplitude $|C| = \dfrac{A^2\omega^2}{2\left|\omega_n^2 - 4\omega^2\right|}$ grows without bound when $2\omega \to \omega_n$, i.e. for

$$ \boxed{\omega \approx \frac12\sqrt{\frac{g}{R}}} $$

At exact resonance the particular solution is $\delta_p = -\dfrac{A^2\omega^2}{4\omega_n}\,t\sin(\omega_nt)$ (check: $\ddot\delta_p + \omega_n^2\delta_p = -\tfrac{A^2\omega^2}{2}\cos\omega_nt$), whose amplitude grows linearly in time. The assumption $\delta \ll 1$ then fails, as stated in the key.

##### Checks
* **Role of each inertia force.** The centrifugal force (along $\mathbf{i}_1$, in the plane) is the only inertia force that enters the equation of motion. The Euler and Coriolis forces are normal to the plane: they do not change $\varphi$, but they load the wire through $N_2$.
* **Limits.** $A \to 0$: $\ddot\varphi + (g/R)\cos\varphi = 0$, the simple pendulum about $\varphi = -\pi/2$ in a fixed plane, and $N_2 = 0$. $\omega \to 0$ with $A$ fixed: $\Omega \to 0$ and the same pendulum is recovered.
* **Energy.** $dE_1^P/dt$ averages to zero over a period of the forcing ($\sin\omega t\cos\omega t$ has zero mean) but is not zero instant by instant; near resonance the drive pumps energy into the oscillation.
* **Orthogonality:** $\mathbf{e}_r\cdot\mathbf{e}_\varphi = -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi = 0$, $\mathbf{e}_r\times\mathbf{e}_\varphi = \mathbf{k}_1$ and $\det[{}_0R_1] = 1$ (change-of-basis section).
* **Inertial check.** Differentiating $[{}_0R_1]\mathbf{r}_1^P$ twice reproduces $\mathbf{a}_1^P + \boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ (Notes Eq. 3.27), and $m\mathbf{a}_0^P = \mathbf{W} + \mathbf{N}$ holds with the reaction of part (e) (checked symbolically with sympy).
* **Dimensions.** $[R(1 + \cos\varphi)] = [R\sin\varphi] = \text{m}$; $[\psi] = [A] = 1$; $[g/R] = [A^2\omega^2] = \text{s}^{-2}$ (same units as $\ddot\varphi$); $[mA^2R\omega^2] = [mR\dot\varphi^2] = [mg] = \text{N}$; $[mAR\omega\dot\varphi] = \text{kg}\cdot\text{m}\cdot\text{s}^{-2} = \text{N}$; $[A^2R\omega^2/g] = \dfrac{\text{m}\cdot\text{s}^{-2}}{\text{m}\cdot\text{s}^{-2}} = 1$, as an angle must be.
* **Check against the official key:** the key of `Problems.pdf` gives the equation of motion $\ddot\varphi + (g/R)\cos\varphi + A^2\omega^2(1 + \cos\varphi)\sin^2(\omega t)\sin\varphi = 0$, the reaction components $N_1$ and $N_2$ and the small-oscillation equation; all coincide with (d), (e) and (f) (no discrepancy).

---

## Problem 36: Pendulum String Dragged by a Rotating Bar

### Reference Frames, Bases and Coordinates
* **System:** a heavy particle $P$ (mass $m$) hangs from the fixed ceiling point $A$ by a string of length $L$. A bar turning at constant rate $\omega$ about the vertical axis through its centre $O$, in a horizontal plane a distance $h$ below the ceiling, hits the string at $t = 0$ and drags it. The string then runs $A \to C \to P$, bent over the bar at the contact point $C$.
* **Why the frame $S_1$ attached to the bar.** In $S_1$ the bar is the fixed axis $Ox_1$, so the contact point is simply $C = (\xi, 0, 0)$ and the string geometry is described by $\xi$, $\ell$, $\varphi$, $\theta$. The price is that $A$ moves in $S_1$ and that the centrifugal and Coriolis forces (Slides 27–28) have to be added. Since $\boldsymbol{\omega}_{10}$ is constant and $O$ is fixed, the Euler force and the force of the origin's acceleration vanish, and the centrifugal force has a potential (Slide 30).
* **Hypotheses:** <br>1. A frame $S_0$ with origin $O$ and vertical axis $\mathbf{k}_0$ (upward) is inertial; gravity is $-g\,\mathbf{k}_0$. <br>2. The string is massless and inextensible, and stays tense ($T \gt 0$) and in contact with the bar (the only stage of the motion studied, as the statement asks). <br>3. The bar is thin (a straight line) and long enough for $C$ to stay on it; the contact is frictionless. <br>4. The rotation of the bar is prescribed: $\omega$ is kept constant whatever the string does. <br>5. The bar reaches the string at $t = 0$ while $P$ is at rest below $A$, so $L \gt h$.
* **Fixed (inertial) frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, basis $\mathcal{B}_0$, with $\mathbf{k}_0$ vertical upward and $\mathbf{i}_0$ pointing horizontally from $O$ towards the vertical of $A$, so that $\mathbf{r}_0^A = R\,\mathbf{i}_0 + h\,\mathbf{k}_0$.
* **Moving frame:** $S_1 = \{O; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, basis $\mathcal{B}_1$, attached to the bar: $\mathbf{i}_1$ along the bar and $\mathbf{k}_1 = \mathbf{k}_0$. At $t = 0$ the bar is below $A$, so $S_1$ coincides with $S_0$ at that instant.
* **Sense of rotation.** In the left drawing of the statement ($t \lt 0$) the vertical projection of $A$ lies at positive $x_1$ and positive $y_1$, so the bar reaches it turning from $\mathbf{i}_1$ towards $\mathbf{j}_1$: $\boldsymbol{\omega}_{10} = +\omega\,\mathbf{k}_1$. (The same sign is implied by the Coriolis force of the official key.) The angle turned by the bar is $\omega t$.
* **String basis:** $\mathcal{B}_2 = \{\mathbf{e}_{CP}, \mathbf{e}_\theta, \mathbf{e}_\varphi\}$, with $\mathbf{e}_{CP}$ the unit vector from $C$ to $P$; it is deduced, with two drawings, in the next section.
* **Degrees of freedom:** $P$ moves in space with the single constraint "string tense", so it has **two** degrees of freedom. We take $\xi$ and $\theta$; $\ell$ and $\varphi$ are fixed by $\xi$ and $t$ through the constraints of part (c). The tension $T$ is the additional unknown.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $L$ | total length of the string | m |
| $h$ | height of the ceiling above the plane of the bar | m |
| $R$ | horizontal distance between $O$ and $A$ | m |
| $\omega$ | angular velocity of the bar (constant) | rad/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\xi$ | distance $OC$ along the bar | m |
| $\ell$ | length of the segment $CP$ | m |
| $\varphi$ | angle between $\overrightarrow{CP}$ and the bar ($\mathbf{i}_1$) | rad |
| $\theta$ | angle between the plane $Ox_1z_1$ and the plane bar–$P$ | rad |
| $T$ | tension of the string | N |

### Change of Basis and Position Vector

There are two rotations: the bar turns $\omega t$ about the vertical $\mathbf{k}_0$ ($\mathcal{B}_0 \to \mathcal{B}_1$), and the plane that contains the bar and $P$ is turned $\theta$ about the bar from the vertical plane $Ox_1z_1$, inside which the segment $CP$ makes the angle $\varphi$ with the bar ($\mathcal{B}_1 \to \mathcal{B}_2$). Each one is drawn looking along its own axis.

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p36-top-view.svg]]

The first rotation is about $\mathbf{k}_0$, so we look down the vertical from $+z_0$: $\mathbf{k}_0 = \mathbf{k}_1$ points out of the paper, towards the reader ($\odot$). Take $\mathbf{i}_0$ to the right, towards the point $A'$ of the plane of the bar directly below $A$. The direction of $\mathbf{j}_0$ follows from the right-hand rule, $\mathbf{j}_0 = \mathbf{k}_0\times\mathbf{i}_0$: the fingers go from $\mathbf{k}_0$ (towards the reader) to $\mathbf{i}_0$ (right) and the thumb points up the page. With $\boldsymbol{\omega}_{10} = \omega\,\mathbf{k}_0$ and $\omega \gt 0$, the bar turns counter-clockwise in this view (thumb along $\mathbf{k}_0$, towards the reader), and at time $t$ it has turned the angle $\omega t$ from $\mathbf{i}_0$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of a right triangle whose leg adjacent to $\omega t$ lies along $\mathbf{i}_0$ and measures $\cos\omega t$, and whose opposite leg points up the page, along $+\mathbf{j}_0$, and measures $\sin\omega t$. Hence $\mathbf{i}_1 = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ (up the page) and turns the same angle counter-clockwise, so its tip leans to the left, towards $-\mathbf{i}_0$. Its leg along $\mathbf{j}_0$ (adjacent) is $\cos\omega t$ and its leg along $-\mathbf{i}_0$ (opposite) is $\sin\omega t$: $\mathbf{j}_1 = -\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0$. **The minus sign comes from the counter-clockwise turn carrying the upward axis to the left, towards $-\mathbf{i}_0$.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

The columns of the change-of-basis matrix are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = \cos\omega t\cos\omega t - (-\sin\omega t)\sin\omega t = \cos^2\omega t + \sin^2\omega t = 1 $$

The product $[{}_0R_1][{}_0R_1]^T$ has diagonal entries $\cos^2\omega t + \sin^2\omega t = 1$ (first two rows) and $1$ (third row), and off-diagonal entries $\cos\omega t\sin\omega t - \sin\omega t\cos\omega t = 0$ (first row times second row) and $0$ (any row times the third), so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$:** $\mathbf{r}_0^O = \mathbf{v}_0^O = \mathbf{a}_0^O = \mathbf{0}$ (the centre of the bar is fixed), $\boldsymbol{\omega}_{10} = \omega\,\mathbf{k}_1$, $\boldsymbol{\alpha}_{10} = \mathbf{0}$ ($\omega$ constant and $\mathbf{k}_1 = \mathbf{k}_0$ fixed). Check with the chain rule: $\left.\frac{d\mathbf{i}_1}{dt}\right|_0 = -\omega\sin\omega t\,\mathbf{i}_0 + \omega\cos\omega t\,\mathbf{j}_0 = \omega\,\mathbf{j}_1$, and indeed $\boldsymbol{\omega}_{10}\times\mathbf{i}_1 = \omega\,\mathbf{k}_1\times\mathbf{i}_1 = \omega\,\mathbf{j}_1$.

![[attachments/EM-SOL/p36-anchor-top.svg]]

**Position of $A$ in $S_1$.** In the same view, $A'$ is at distance $R$ from $O$ along $\mathbf{i}_0$, that is, the angle $\omega t$ behind the bar (clockwise from $\mathbf{i}_1$). Drop the perpendicular from $A'$ to the line of the bar, with foot $F$. In the right triangle $OFA'$ (right angle at $F$) the hypotenuse is $OA' = R$, the leg adjacent to $\omega t$ is $OF = R\cos\omega t$, along $+\mathbf{i}_1$, and the opposite leg is $FA' = R\sin\omega t$, along $-\mathbf{j}_1$ because $A'$ lies on the clockwise side of the bar. $A$ is a height $h$ above $A'$, so

$$ \mathbf{r}_1^A = R\cos\omega t\,\mathbf{i}_1 - R\sin\omega t\,\mathbf{j}_1 + h\,\mathbf{k}_1 $$

The matrix gives the same result: the origins coincide, so $\mathbf{r}_1^A = [{}_0R_1]^T\mathbf{r}_0^A$,

$$ [{}_0R_1]^T\begin{pmatrix} R \\ 0 \\ h \end{pmatrix} = \begin{pmatrix} R\cos\omega t \\ -R\sin\omega t \\ h \end{pmatrix} $$

#### The plane bar–$P$ seen along the bar

![[attachments/EM-SOL/p36-bar-view.svg]]

The second rotation is about the bar, so we now look along $\mathbf{i}_1$, with $\mathbf{i}_1$ pointing out of the paper ($\odot$) and the bar reduced to the point $C$. Take $\mathbf{k}_1$ up. Then $\mathbf{j}_1 = \mathbf{k}_1\times\mathbf{i}_1$ points to the right: the fingers go from $\mathbf{k}_1$ (up) to $\mathbf{i}_1$ (towards the reader) and the thumb points right. The plane that contains the bar and $P$ contains the line of sight, so in this view it is a straight line through $C$. $\theta$ is its angle with the downward vertical $-\mathbf{k}_1$ (the trace of the plane $Ox_1z_1$), and $\theta \gt 0$ puts $P$ on the side $y_1 \lt 0$, the side of $A$ for $0 \lt \omega t \lt \pi$ (this is the sign convention of the official key); in the drawing that is the left.

Let $\mathbf{u}$ be the unit vector along that line, from $C$ towards the side of $P$ (an auxiliary vector, perpendicular to the bar). It is the hypotenuse (length 1) of the shaded right triangle: the leg adjacent to $\theta$ lies along $-\mathbf{k}_1$ and measures $\cos\theta$; the leg opposite to $\theta$ lies along $-\mathbf{j}_1$ and measures $\sin\theta$. Hence

$$ \mathbf{u} = -\sin\theta\,\mathbf{j}_1 - \cos\theta\,\mathbf{k}_1 $$

Both components are negative because, for $0 \lt \theta \lt \pi/2$, $\mathbf{u}$ points down and to the left. Differentiating with respect to $\theta$ ($\frac{d}{d\theta}(-\sin\theta) = -\cos\theta$, $\frac{d}{d\theta}(-\cos\theta) = \sin\theta$) gives a vector of length $\sqrt{\cos^2\theta + \sin^2\theta} = 1$, perpendicular to $\mathbf{u}$ in this view and pointing in the sense of increasing $\theta$:

$$ \mathbf{e}_\theta = \frac{d\mathbf{u}}{d\theta} = -\cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1 $$

**Relation with the standard azimuth.** The usual azimuth $\psi$ about the polar axis $\mathbf{i}_1$ is measured from $\mathbf{j}_1$ towards $\mathbf{k}_1$, with perpendicular unit vector $\cos\psi\,\mathbf{j}_1 + \sin\psi\,\mathbf{k}_1$. Matching $\mathbf{u} = -\sin\theta\,\mathbf{j}_1 - \cos\theta\,\mathbf{k}_1$ requires $\cos\psi = -\sin\theta$ and $\sin\psi = -\cos\theta$, which holds for $\psi = -\theta - \frac{\pi}{2}$:

$$ \cos\left(-\theta - \tfrac{\pi}{2}\right) = \cos\left(\theta + \tfrac{\pi}{2}\right) = \cos\theta\cos\tfrac{\pi}{2} - \sin\theta\sin\tfrac{\pi}{2} = -\sin\theta, \qquad \sin\left(-\theta - \tfrac{\pi}{2}\right) = -\left(\sin\theta\cos\tfrac{\pi}{2} + \cos\theta\sin\tfrac{\pi}{2}\right) = -\cos\theta $$

(with $\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$, and cosine even, sine odd). So $\theta$ is measured from the downward vertical instead of $\mathbf{j}_1$, and in the opposite sense; it is chosen so that $\theta = 0$ is the hanging position, in the plane $Ox_1z_1$.

#### The segment $CP$ inside the plane bar–$P$

![[attachments/EM-SOL/p36-string-plane.svg]]

This drawing is the true view of the plane that contains the bar ($\mathbf{i}_1$, to the right) and $\mathbf{u}$ (down the page). The segment $CP$ makes the angle $\varphi$ with the bar, with $\varphi \in (0, \pi)$. Let $E$ be the foot of the perpendicular from $P$ to the line of the bar. In the shaded right triangle $CEP$ (right angle at $E$) the hypotenuse is $CP = \ell$, the leg adjacent to $\varphi$ is $CE = \ell\cos\varphi$, along $\mathbf{i}_1$, and the opposite leg is $EP = \ell\sin\varphi$, along $\mathbf{u}$. Therefore $\overrightarrow{CP} = \ell\cos\varphi\,\mathbf{i}_1 + \ell\sin\varphi\,\mathbf{u}$, and dividing by $\ell$ and substituting $\mathbf{u}$:

$$ \mathbf{e}_{CP} = \cos\varphi\,\mathbf{i}_1 + \sin\varphi\,\mathbf{u} = \cos\varphi\,\mathbf{i}_1 - \sin\varphi\sin\theta\,\mathbf{j}_1 - \sin\varphi\cos\theta\,\mathbf{k}_1 $$

The other two unit vectors of $\mathcal{B}_2$ come from differentiating $\mathbf{e}_{CP}$ with respect to each angle. With respect to $\varphi$ ($\frac{\partial}{\partial\varphi}\cos\varphi = -\sin\varphi$, $\frac{\partial}{\partial\varphi}\sin\varphi = \cos\varphi$) we get the unit vector perpendicular to $CP$ in this plane, drawn at $P$:

$$ \mathbf{e}_\varphi = \frac{\partial\mathbf{e}_{CP}}{\partial\varphi} = -\sin\varphi\,\mathbf{i}_1 + \cos\varphi\,\mathbf{u} = -\sin\varphi\,\mathbf{i}_1 - \cos\varphi\sin\theta\,\mathbf{j}_1 - \cos\varphi\cos\theta\,\mathbf{k}_1 $$

With respect to $\theta$, only $\mathbf{u}$ depends on it, so $\frac{\partial\mathbf{e}_{CP}}{\partial\theta} = \sin\varphi\,\frac{d\mathbf{u}}{d\theta} = \sin\varphi\,\mathbf{e}_\theta$, which has length $\sin\varphi$:

$$ \mathbf{e}_\theta = \frac{1}{\sin\varphi}\frac{\partial\mathbf{e}_{CP}}{\partial\theta} = -\cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1 $$

The matrix with columns $\mathbf{e}_{CP}, \mathbf{e}_\theta, \mathbf{e}_\varphi$ in $\mathcal{B}_1$ is

$$ [{}_1R_2] = \begin{pmatrix} \cos\varphi & 0 & -\sin\varphi \\ -\sin\varphi\sin\theta & -\cos\theta & -\cos\varphi\sin\theta \\ -\sin\varphi\cos\theta & \sin\theta & -\cos\varphi\cos\theta \end{pmatrix} $$

Expanding along the first row: $\det[{}_1R_2] = \cos\varphi\left(\cos\varphi\cos^2\theta + \cos\varphi\sin^2\theta\right) - \sin\varphi\left(-\sin\varphi\sin^2\theta - \sin\varphi\cos^2\theta\right) = \cos^2\varphi + \sin^2\varphi = 1$. Each column has unit norm, and $\mathbf{e}_{CP}\cdot\mathbf{e}_\theta = \sin\varphi\sin\theta\cos\theta - \sin\varphi\cos\theta\sin\theta = 0$, $\mathbf{e}_{CP}\cdot\mathbf{e}_\varphi = -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi\left(\sin^2\theta + \cos^2\theta\right) = 0$, $\mathbf{e}_\theta\cdot\mathbf{e}_\varphi = \cos\theta\cos\varphi\sin\theta - \sin\theta\cos\varphi\cos\theta = 0$, so $[{}_1R_2][{}_1R_2]^T = I$ and $\mathbf{e}_{CP}\times\mathbf{e}_\theta = \mathbf{e}_\varphi$.

**Derivatives of $\mathcal{B}_2$ in $S_1$** (chain rule, $\tfrac{d}{dt}\mathbf{e}(\varphi(t), \theta(t)) = \tfrac{\partial\mathbf{e}}{\partial\varphi}\dot\varphi + \tfrac{\partial\mathbf{e}}{\partial\theta}\dot\theta$, with $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ constant in $S_1$). Using $\partial\mathbf{e}_\varphi/\partial\varphi = \cos\varphi\,(-\mathbf{i}_1) + \sin\varphi\sin\theta\,\mathbf{j}_1 + \sin\varphi\cos\theta\,\mathbf{k}_1 = -\mathbf{e}_{CP}$, $\partial\mathbf{e}_\varphi/\partial\theta = -\cos\varphi\cos\theta\,\mathbf{j}_1 + \cos\varphi\sin\theta\,\mathbf{k}_1 = \cos\varphi\,\mathbf{e}_\theta$ and $\partial\mathbf{e}_\theta/\partial\theta = \sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1 = -\left(\sin\varphi\,\mathbf{e}_{CP} + \cos\varphi\,\mathbf{e}_\varphi\right)$:

$$ \left.\frac{d\mathbf{e}_{CP}}{dt}\right|_1 = \dot\varphi\,\mathbf{e}_\varphi + \dot\theta\sin\varphi\,\mathbf{e}_\theta, \qquad \left.\frac{d\mathbf{e}_\varphi}{dt}\right|_1 = -\dot\varphi\,\mathbf{e}_{CP} + \dot\theta\cos\varphi\,\mathbf{e}_\theta, \qquad \left.\frac{d\mathbf{e}_\theta}{dt}\right|_1 = -\dot\theta\left(\sin\varphi\,\mathbf{e}_{CP} + \cos\varphi\,\mathbf{e}_\varphi\right) $$

**Position of $P$ in $S_1$.** To go from $O$ to $P$ we pass through the contact point, which is on the bar: $\overrightarrow{OP} = \overrightarrow{OC} + \overrightarrow{CP}$, with $\overrightarrow{OC} = \xi\,\mathbf{i}_1$ (the dimension $\xi$ of the drawing) and $\overrightarrow{CP} = \ell\,\mathbf{e}_{CP}$:

$$ \mathbf{r}_1^P = \xi\,\mathbf{i}_1 + \ell\,\mathbf{e}_{CP} = (\xi + \ell\cos\varphi)\,\mathbf{i}_1 - \ell\sin\varphi\sin\theta\,\mathbf{j}_1 - \ell\sin\varphi\cos\theta\,\mathbf{k}_1 $$

### Kinematics

##### (a) Position and velocity of $A$ in $S_1$
* **Pedagogical Justification:** $A$ is fixed in $S_0$; its coordinates in $S_1$ were obtained above from the top view and from $\mathbf{r}_1^A = [{}_0R_1]^T\mathbf{r}_0^A$; its relative velocity is the derivative of those coordinates in $S_1$.

$$ \boxed{\mathbf{r}_1^A = R\cos\omega t\,\mathbf{i}_1 - R\sin\omega t\,\mathbf{j}_1 + h\,\mathbf{k}_1} $$

With the chain rule $\tfrac{d}{dt}\cos\omega t = -\omega\sin\omega t$ and $\tfrac{d}{dt}\sin\omega t = \omega\cos\omega t$:

$$ \boxed{\mathbf{v}_1^A = \left.\frac{d\mathbf{r}_1^A}{dt}\right|_1 = -R\omega\sin\omega t\,\mathbf{i}_1 - R\omega\cos\omega t\,\mathbf{j}_1} $$

Check with the velocity composition (Notes Eq. 3.26): $\mathbf{0} = \mathbf{v}_0^A = \mathbf{v}_1^A + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^A$, and $\omega\mathbf{k}_1\times\mathbf{r}_1^A = R\omega\cos\omega t\,\mathbf{j}_1 + R\omega\sin\omega t\,\mathbf{i}_1 = -\mathbf{v}_1^A$. In $S_1$, $A$ describes a circle of radius $R$ at height $h$ with angular velocity $-\omega$.

##### (b) Position, velocity and acceleration of $P$ in $S_1$
* **Pedagogical Justification:** $\overrightarrow{OP} = \overrightarrow{OC} + \overrightarrow{CP}$ with $\overrightarrow{OC} = \xi\,\mathbf{i}_1$ along the bar and $\overrightarrow{CP} = \ell\,\mathbf{e}_{CP}$. Derivatives are taken in $S_1$ with the product rule and the basis derivatives of the change-of-basis section.

**Position** (built step by step in the previous section):

$$ \boxed{\mathbf{r}_1^P = \xi\,\mathbf{i}_1 + \ell\,\mathbf{e}_{CP} = (\xi + \ell\cos\varphi)\,\mathbf{i}_1 - \ell\sin\varphi\sin\theta\,\mathbf{j}_1 - \ell\sin\varphi\cos\theta\,\mathbf{k}_1} $$

**Velocity.** Product rule, $\tfrac{d}{dt}(\ell\,\mathbf{e}_{CP}) = \dot\ell\,\mathbf{e}_{CP} + \ell\left(\dot\varphi\,\mathbf{e}_\varphi + \dot\theta\sin\varphi\,\mathbf{e}_\theta\right)$:

$$ \boxed{\mathbf{v}_1^P = \dot\xi\,\mathbf{i}_1 + \dot\ell\,\mathbf{e}_{CP} + \ell\dot\varphi\,\mathbf{e}_\varphi + \ell\dot\theta\sin\varphi\,\mathbf{e}_\theta} $$

In $\mathcal{B}_1$ (differentiating each component; e.g. $\tfrac{d}{dt}(-\ell\sin\varphi\sin\theta) = -\dot\ell\sin\varphi\sin\theta - \ell\dot\varphi\cos\varphi\sin\theta - \ell\dot\theta\sin\varphi\cos\theta$):

$$ \mathbf{v}_1^P = \left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right)\mathbf{i}_1 - \left(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta\right)\mathbf{j}_1 - \left(\dot\ell\sin\varphi\cos\theta + \ell\dot\varphi\cos\varphi\cos\theta - \ell\dot\theta\sin\varphi\sin\theta\right)\mathbf{k}_1 $$

**Acceleration.** Differentiate term by term:

* $\tfrac{d}{dt}(\dot\xi\,\mathbf{i}_1) = \ddot\xi\,\mathbf{i}_1$;
* $\tfrac{d}{dt}(\dot\ell\,\mathbf{e}_{CP}) = \ddot\ell\,\mathbf{e}_{CP} + \dot\ell\dot\varphi\,\mathbf{e}_\varphi + \dot\ell\dot\theta\sin\varphi\,\mathbf{e}_\theta$;
* $\tfrac{d}{dt}(\ell\dot\varphi\,\mathbf{e}_\varphi) = (\dot\ell\dot\varphi + \ell\ddot\varphi)\,\mathbf{e}_\varphi + \ell\dot\varphi\left(-\dot\varphi\,\mathbf{e}_{CP} + \dot\theta\cos\varphi\,\mathbf{e}_\theta\right)$;
* $\tfrac{d}{dt}(\ell\dot\theta\sin\varphi\,\mathbf{e}_\theta) = \left(\dot\ell\dot\theta\sin\varphi + \ell\ddot\theta\sin\varphi + \ell\dot\theta\dot\varphi\cos\varphi\right)\mathbf{e}_\theta - \ell\dot\theta^2\sin\varphi\left(\sin\varphi\,\mathbf{e}_{CP} + \cos\varphi\,\mathbf{e}_\varphi\right)$.

Collecting along each unit vector:

$$ \boxed{\mathbf{a}_1^P = \ddot\xi\,\mathbf{i}_1 + \left(\ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi\right)\mathbf{e}_{CP} + \left(\ell\ddot\varphi + 2\dot\ell\dot\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi\right)\mathbf{e}_\varphi + \left(\ell\ddot\theta\sin\varphi + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi\right)\mathbf{e}_\theta} $$

with $\mathbf{e}_{CP}, \mathbf{e}_\varphi, \mathbf{e}_\theta$ given in $\mathcal{B}_1$ in the change-of-basis section. The bracketed terms are the spherical-coordinate acceleration of $P$ about the moving centre $C$, plus the acceleration $\ddot\xi\,\mathbf{i}_1$ of the centre along the bar. Time enters through $\xi$, $\ell$, $\varphi$, $\theta$ only; the explicit time dependence appears when $\ell$ and $\varphi$ are replaced by the constraints of part (c).

##### (c) $AC$, $\ell$ and $\varphi$ as functions of $\xi$ and $t$
* **Pedagogical Justification:** The string has constant length, which gives $\ell$. The angle $\varphi$ follows from the frictionless contact: the massless piece of string at $C$ must be in equilibrium under the two tensions and the bar's reaction, which has no component along the bar.

**Vector $\overrightarrow{AC}$:** with $\mathbf{r}_1^C = \xi\,\mathbf{i}_1$ and part (a),

$$ \boxed{\overrightarrow{AC} = \mathbf{r}_1^C - \mathbf{r}_1^A = (\xi - R\cos\omega t)\,\mathbf{i}_1 + R\sin\omega t\,\mathbf{j}_1 - h\,\mathbf{k}_1} $$
$$ AC^2 = (\xi - R\cos\omega t)^2 + R^2\sin^2\omega t + h^2 = \xi^2 - 2R\xi\cos\omega t + R^2\left(\cos^2\omega t + \sin^2\omega t\right) + h^2 \quad\Longrightarrow\quad \boxed{AC = \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}} $$

**Length $\ell$.** $AC + CP = L$:

$$ \boxed{\ell = L - \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}} $$

**Angle $\varphi$.** With no friction the tension is the same, $T$, on both sides of $C$. Equilibrium of the massless string element at $C$: $T\,\mathbf{e}_{CA} + T\,\mathbf{e}_{CP} + \mathbf{N}_b = \mathbf{0}$ with $\mathbf{N}_b\cdot\mathbf{i}_1 = 0$. Projecting on $\mathbf{i}_1$: $\mathbf{e}_{CP}\cdot\mathbf{i}_1 = -\mathbf{e}_{CA}\cdot\mathbf{i}_1$, where $\mathbf{e}_{CA} = -\overrightarrow{AC}/AC$. Hence

$$ \cos\varphi = \frac{\xi - R\cos\omega t}{AC} \quad\Longrightarrow\quad \boxed{\varphi = \arccos\frac{\xi - R\cos\omega t}{\sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}}}, \qquad \sin\varphi = \frac{\sqrt{R^2\sin^2\omega t + h^2}}{AC} $$

($\varphi \in (0, \pi)$, so $\sin\varphi \gt 0$). The two segments make equal angles with the bar, on opposite sides of the plane perpendicular to it. (Extension: this is also the condition for the path $A \to C \to P$ to be the shortest one for fixed $P$, $\tfrac{\partial}{\partial\xi}(AC + CP) = \cos\angle(\overrightarrow{AC}, \mathbf{i}_1) - \cos\varphi = 0$.)

**Compact notation for part (e).** Let $q = \xi - R\cos\omega t$, $\rho = \sqrt{R^2\sin^2\omega t + h^2}$ and $D = AC = \sqrt{q^2 + \rho^2}$. Then $q = D\cos\varphi$, $\rho = D\sin\varphi$: $(D, \varphi)$ are the polar coordinates of the point $(q, \rho)$, and $\ell = L - D$. Their derivatives:

* $\dot q = \dot\xi + R\omega\sin\omega t$ and $\ddot q = \ddot\xi + R\omega^2\cos\omega t$ (chain rule on $\cos\omega t$).
* From $\rho^2 = R^2\sin^2\omega t + h^2$: $2\rho\dot\rho = 2R^2\omega\sin\omega t\cos\omega t$, so $\dot\rho = \dfrac{R^2\omega\sin 2\omega t}{2\rho}$. Differentiating $\rho\dot\rho = \tfrac12 R^2\omega\sin 2\omega t$ (product rule): $\dot\rho^2 + \rho\ddot\rho = R^2\omega^2\cos 2\omega t$, so $\ddot\rho = \dfrac{R^2\omega^2\cos 2\omega t - \dot\rho^2}{\rho}$.
* Differentiating $q = D\cos\varphi$, $\rho = D\sin\varphi$: $\dot q = \dot D\cos\varphi - D\dot\varphi\sin\varphi$, $\dot\rho = \dot D\sin\varphi + D\dot\varphi\cos\varphi$. Solving this rotation-type system:
$$ \dot D = \dot q\cos\varphi + \dot\rho\sin\varphi, \qquad D\dot\varphi = \dot\rho\cos\varphi - \dot q\sin\varphi $$
* Differentiating once more, $\ddot q = (\ddot D - D\dot\varphi^2)\cos\varphi - (D\ddot\varphi + 2\dot D\dot\varphi)\sin\varphi$ and $\ddot\rho = (\ddot D - D\dot\varphi^2)\sin\varphi + (D\ddot\varphi + 2\dot D\dot\varphi)\cos\varphi$, so
$$ \ddot D - D\dot\varphi^2 = \ddot q\cos\varphi + \ddot\rho\sin\varphi, \qquad D\ddot\varphi + 2\dot D\dot\varphi = \ddot\rho\cos\varphi - \ddot q\sin\varphi $$
* Finally $\dot\ell = -\dot D$, $\ddot\ell = -\ddot D$. Since $\dot\rho\sin\varphi = \dfrac{R^2\omega\sin\omega t\cos\omega t}{\rho}\dfrac{\rho}{D}$ and $\cos\varphi = q/D$,
$$ \dot\ell = -(\dot\xi + R\omega\sin\omega t)\frac{\xi - R\cos\omega t}{D} - \frac{R^2\omega\sin\omega t\cos\omega t}{D} \quad\Longrightarrow\quad \boxed{\dot\ell + \dot\xi\cos\varphi = -\frac{R\omega\,\xi\sin\omega t}{D}} $$

### Forces and Equations of Motion

##### (d) Forces acting on $P$
* **Pedagogical Justification:** In the non-inertial frame $S_1$, $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ (Notes Eqs. 4.62–4.63). The actual forces on $P$ are only the weight and the pull of the string (the bar touches the string, not $P$). The inertia forces are those of Slide 28 with $\mathbf{a}_0^O = \mathbf{0}$, $\boldsymbol{\alpha}_{10} = \mathbf{0}$, $\boldsymbol{\omega}_{10} = \omega\mathbf{k}_1$.

**Actual forces:**

* Weight: $\mathbf{W} = -mg\,\mathbf{k}_1$.
* Tension, along the string towards $C$: $\mathbf{T} = -T\,\mathbf{e}_{CP} = -T\cos\varphi\,\mathbf{i}_1 + T\sin\varphi\sin\theta\,\mathbf{j}_1 + T\sin\varphi\cos\theta\,\mathbf{k}_1$, with $T \gt 0$.

**Inertia forces:** write $\mathbf{r}_1^P = x\,\mathbf{i}_1 + y\,\mathbf{j}_1 + z\,\mathbf{k}_1$ with $x = \xi + \ell\cos\varphi$, $y = -\ell\sin\varphi\sin\theta$, and $\mathbf{v}_1^P = v_x\mathbf{i}_1 + v_y\mathbf{j}_1 + v_z\mathbf{k}_1$ from part (b). With $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$:

* Origin and Euler: $\mathbf{F}_A = -m\mathbf{a}_0^O = \mathbf{0}$, $\mathbf{F}_E = -m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P = \mathbf{0}$.
* Centrifugal: $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = \omega\left(x\,\mathbf{j}_1 - y\,\mathbf{i}_1\right)$, $\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \omega^2\left(-x\,\mathbf{i}_1 - y\,\mathbf{j}_1\right)$, so (Slide 30, $\mathbf{r}_\perp = x\,\mathbf{i}_1 + y\,\mathbf{j}_1$)
$$ \boxed{\mathbf{F}_C = m\omega^2(\xi + \ell\cos\varphi)\,\mathbf{i}_1 - m\omega^2\ell\sin\varphi\sin\theta\,\mathbf{j}_1} $$
* Coriolis: $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = \omega\left(v_x\,\mathbf{j}_1 - v_y\,\mathbf{i}_1\right)$, so $\mathbf{F}_{COR} = -2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = 2m\omega v_y\,\mathbf{i}_1 - 2m\omega v_x\,\mathbf{j}_1$:
$$ \boxed{\mathbf{F}_{COR} = -2m\omega\left(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta\right)\mathbf{i}_1 - 2m\omega\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right)\mathbf{j}_1} $$

Both inertia forces agree with the official key.

##### (e) Equations of motion
* **Pedagogical Justification:** Project $m\mathbf{a}_1^P = \mathbf{W} + \mathbf{T} + \mathbf{F}_C + \mathbf{F}_{COR}$ on $\mathcal{B}_2$. The tension is along $\mathbf{e}_{CP}$, so the projections on $\mathbf{e}_\theta$ and $\mathbf{e}_\varphi$ are free of the unknown $T$: they are the two equations of motion for the two degrees of freedom $\xi$, $\theta$. The projection on $\mathbf{e}_{CP}$ then gives $T$.

**Projections of each term** (using $\mathbf{i}_1\cdot\mathbf{e}_{CP} = \cos\varphi$, $\mathbf{i}_1\cdot\mathbf{e}_\varphi = -\sin\varphi$, $\mathbf{i}_1\cdot\mathbf{e}_\theta = 0$, and the components of the change-of-basis section):

| Term | $\cdot\,\mathbf{e}_\theta$ | $\cdot\,\mathbf{e}_\varphi$ | $\cdot\,\mathbf{e}_{CP}$ |
|---|---|---|---|
| $\mathbf{a}_1^P$ (multiply by $m$) | $\ell\ddot\theta\sin\varphi + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi$ | $\ell\ddot\varphi + 2\dot\ell\dot\varphi - \ddot\xi\sin\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi$ | $\ddot\xi\cos\varphi + \ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi$ |
| $\mathbf{W}$ | $-mg\sin\theta$ | $mg\cos\varphi\cos\theta$ | $mg\sin\varphi\cos\theta$ |
| $\mathbf{T}$ | $0$ | $0$ | $-T$ |
| $\mathbf{F}_C$ | $m\omega^2\ell\sin\varphi\sin\theta\cos\theta$ | $-m\omega^2\sin\varphi\left(\xi + \ell\cos\varphi\cos^2\theta\right)$ | $m\omega^2\left[(\xi + \ell\cos\varphi)\cos\varphi + \ell\sin^2\varphi\sin^2\theta\right]$ |
| $\mathbf{F}_{COR}$ | $2m\omega\cos\theta\,v_x$ | $2m\omega\left[\sin\theta(\dot\ell + \dot\xi\cos\varphi) + \ell\dot\theta\sin^2\varphi\cos\theta\right]$ | $2m\omega\left[\sin\theta(\dot\xi\sin\varphi - \ell\dot\varphi) - \ell\dot\theta\sin\varphi\cos\varphi\cos\theta\right]$ |

Details of the less obvious entries:

* $\mathbf{F}_C\cdot\mathbf{e}_\varphi = m\omega^2\left[-x\sin\varphi - y\cos\varphi\sin\theta\right] = m\omega^2\left[-(\xi + \ell\cos\varphi)\sin\varphi + \ell\sin\varphi\cos\varphi\sin^2\theta\right] = -m\omega^2\sin\varphi\left[\xi + \ell\cos\varphi(1 - \sin^2\theta)\right]$.
* $\mathbf{F}_{COR}\cdot\mathbf{e}_\varphi = 2m\omega\left[-v_y\sin\varphi + v_x\cos\varphi\sin\theta\right]$, where $-v_y\sin\varphi = \dot\ell\sin^2\varphi\sin\theta + \ell\dot\varphi\sin\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin^2\varphi\cos\theta$ and $v_x\cos\varphi\sin\theta = \dot\xi\cos\varphi\sin\theta + \dot\ell\cos^2\varphi\sin\theta - \ell\dot\varphi\sin\varphi\cos\varphi\sin\theta$; the $\dot\varphi$ terms cancel and $\sin^2\varphi + \cos^2\varphi = 1$.
* $\mathbf{F}_{COR}\cdot\mathbf{e}_{CP} = 2m\omega\left[v_y\cos\varphi + v_x\sin\varphi\sin\theta\right]$: the $\dot\ell$ terms cancel and the $\dot\varphi$ terms add up to $-\ell\dot\varphi\sin\theta\left(\cos^2\varphi + \sin^2\varphi\right)$.
* $\mathbf{F}_{COR}\cdot\mathbf{e}_\theta = 2m\omega\left[-v_x\,(-\cos\theta)\right] = 2m\omega\cos\theta\,v_x$, with $v_x = \dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi$.

**Equation along $\mathbf{e}_\theta$** (divided by $m$):

$$ \boxed{\ell\sin\varphi\,\ddot\theta + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi = -g\sin\theta + \omega^2\ell\sin\varphi\sin\theta\cos\theta + 2\omega\cos\theta\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right)} $$

**Equation along $\mathbf{e}_\varphi$** (divided by $m$):

$$ \boxed{\ell\ddot\varphi + 2\dot\ell\dot\varphi - \ddot\xi\sin\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi = g\cos\varphi\cos\theta - \omega^2\sin\varphi\left(\xi + \ell\cos\varphi\cos^2\theta\right) + 2\omega\left[\sin\theta\left(\dot\ell + \dot\xi\cos\varphi\right) + \ell\dot\theta\sin^2\varphi\cos\theta\right]} $$

**Closing the system.** $\ell$, $\varphi$ and their derivatives are the functions of $(\xi, \dot\xi, \ddot\xi, t)$ of part (c). In particular $\ell\ddot\varphi = \tfrac{\ell}{D}\left(\ddot\rho\cos\varphi - \ddot q\sin\varphi - 2\dot D\dot\varphi\right)$ with $\ddot q = \ddot\xi + R\omega^2\cos\omega t$, and $2\dot\ell\dot\varphi = -2\dot D\dot\varphi$, so with $\ell + D = L$ the left-hand side of the $\mathbf{e}_\varphi$ equation becomes

$$ \ell\ddot\varphi + 2\dot\ell\dot\varphi - \ddot\xi\sin\varphi = -\frac{L}{D}\sin\varphi\,\ddot\xi + \frac{\ell}{D}\left(\ddot\rho\cos\varphi - R\omega^2\cos\omega t\sin\varphi\right) - \frac{2L}{D}\dot D\dot\varphi $$

The coefficient of $\ddot\xi$, $-(L/D)\sin\varphi$, is non-zero while the string is bent ($\sin\varphi \gt 0$), so the $\mathbf{e}_\varphi$ equation gives $\ddot\xi$ and the $\mathbf{e}_\theta$ equation gives $\ddot\theta$: **two second-order ODEs for $\xi(t)$ and $\theta(t)$**, non-autonomous through $\omega t$ (the motion of $A$ in $S_1$). In the $\mathbf{e}_\varphi$ equation the Coriolis term can also be written with $\dot\ell + \dot\xi\cos\varphi = -R\omega\xi\sin\omega t/D$.

**Tension** (projection on $\mathbf{e}_{CP}$, solved for $T$):

$$ \boxed{T = -m\left(\ddot\xi\cos\varphi + \ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi\right) + mg\sin\varphi\cos\theta + m\omega^2\left[(\xi + \ell\cos\varphi)\cos\varphi + \ell\sin^2\varphi\sin^2\theta\right] + 2m\omega\left[\sin\theta\left(\dot\xi\sin\varphi - \ell\dot\varphi\right) - \ell\dot\theta\sin\varphi\cos\varphi\cos\theta\right]} $$

The solution is valid while $T \gt 0$ (string tense).

### Answers and Checks

##### (a) Position and velocity of $A$
$\mathbf{r}_1^A = R\cos\omega t\,\mathbf{i}_1 - R\sin\omega t\,\mathbf{j}_1 + h\,\mathbf{k}_1$ and $\mathbf{v}_1^A = -R\omega\sin\omega t\,\mathbf{i}_1 - R\omega\cos\omega t\,\mathbf{j}_1$: in $S_1$, $A$ goes round a circle of radius $R$ at height $h$ with angular velocity $-\omega$.

##### (b) Position, velocity and acceleration of $P$
$\mathbf{r}_1^P = \xi\,\mathbf{i}_1 + \ell\,\mathbf{e}_{CP}$, $\mathbf{v}_1^P = \dot\xi\,\mathbf{i}_1 + \dot\ell\,\mathbf{e}_{CP} + \ell\dot\varphi\,\mathbf{e}_\varphi + \ell\dot\theta\sin\varphi\,\mathbf{e}_\theta$ and $\mathbf{a}_1^P$ as boxed in the kinematics section, with $\mathbf{e}_{CP}, \mathbf{e}_\varphi, \mathbf{e}_\theta$ given in $\mathcal{B}_1$.

##### (c) $AC$, $\ell$ and $\varphi$
$AC = \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}$, $\ell = L - AC$ and $\cos\varphi = (\xi - R\cos\omega t)/AC$.

##### (d) Forces
Weight $-mg\,\mathbf{k}_1$, tension $-T\,\mathbf{e}_{CP}$, and the centrifugal and Coriolis forces boxed above; the Euler force and the force of the origin's acceleration are zero.

##### (e) Equations of motion
The $\mathbf{e}_\theta$ and $\mathbf{e}_\varphi$ equations boxed above, closed with part (c), are two second-order ODEs for $\xi(t)$ and $\theta(t)$; the $\mathbf{e}_{CP}$ projection gives $T$.

##### (f) Initial conditions at $t = 0$
* **Pedagogical Justification:** At $t = 0^-$ the particle hangs at rest below $A$, and the string is straight and vertical. The bar touches it at the point of the string at the height of the bar. No impulsive force acts on $P$: the string is perpendicular to the bar, so displacing $C$ sideways does not change the path length to first order ($\dot D(0) = 0$ below). Position and velocity of $P$ are therefore continuous at $t = 0$.

**Positions.** At $t = 0$ the bar lies along $\mathbf{i}_0$, and the string meets it directly below $A$: $\xi(0) = R$. Then $q(0) = R - R = 0$, $\rho(0) = h$, $D(0) = h$, so

$$ \xi(0) = R, \qquad \ell(0) = L - h, \qquad \cos\varphi(0) = 0 \;\Rightarrow\; \varphi(0) = \frac{\pi}{2}, \qquad \theta(0) = 0 $$

($P$ is directly below the bar in the plane $Ox_1z_1$). Check: $\mathbf{r}_1^P(0) = R\,\mathbf{i}_1 - (L - h)\,\mathbf{k}_1$, i.e. $P$ at depth $L - h$ below the bar, $L$ below $A$.

**Velocities.** $\mathbf{v}_0^P(0) = \mathbf{0}$, and by Notes Eq. 3.26

$$ \mathbf{v}_1^P(0) = \mathbf{v}_0^P - \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = -\omega\,\mathbf{k}_1\times\left[R\,\mathbf{i}_1 - (L - h)\,\mathbf{k}_1\right] = -\omega R\,\mathbf{j}_1 $$

At $\varphi = \pi/2$, $\theta = 0$: $\mathbf{e}_{CP} = -\mathbf{k}_1$, $\mathbf{e}_\varphi = -\mathbf{i}_1$, $\mathbf{e}_\theta = -\mathbf{j}_1$, so the velocity of part (b) is $\mathbf{v}_1^P(0) = \left(\dot\xi - \ell\dot\varphi\right)\mathbf{i}_1 - \ell\dot\theta\,\mathbf{j}_1 - \dot\ell\,\mathbf{k}_1$. Matching components:

* $\mathbf{k}_1$: $\dot\ell(0) = 0$, consistent with the constraint: $\dot D(0) = \dot q\cos\tfrac{\pi}{2} + \dot\rho(0)\sin\tfrac{\pi}{2} = \dot\rho(0) = \dfrac{R^2\omega\sin 0}{2h} = 0$.
* $\mathbf{j}_1$: $(L - h)\,\dot\theta(0) = \omega R$, so $\dot\theta(0) = \dfrac{\omega R}{L - h}$.
* $\mathbf{i}_1$: $\dot\xi(0) = (L - h)\,\dot\varphi(0)$. From part (c), $D\dot\varphi = \dot\rho\cos\varphi - \dot q\sin\varphi$ gives $h\,\dot\varphi(0) = -\dot q(0) = -\left(\dot\xi(0) + R\omega\sin 0\right) = -\dot\xi(0)$. Substituting, $\dot\xi(0)\left(1 + \dfrac{L - h}{h}\right) = \dot\xi(0)\dfrac{L}{h} = 0$, so $\dot\xi(0) = 0$ and $\dot\varphi(0) = 0$.
$$ \boxed{\xi(0) = R, \quad \dot\xi(0) = 0, \quad \theta(0) = 0, \quad \dot\theta(0) = \frac{\omega R}{L - h}} \qquad \left(\ell(0) = L - h,\ \dot\ell(0) = 0,\ \varphi(0) = \frac{\pi}{2},\ \dot\varphi(0) = 0\right) $$

In $S_1$ the particle starts moving backwards ($-\mathbf{j}_1$) with the speed $\omega R$ of the point of the bar that hits the string: $P$ lags behind the bar, $\theta$ grows from zero.

##### (g) Is the mechanical energy conserved?
* **Pedagogical Justification:** By Slide 29, $E_1^P$ is conserved only if every force that does work in $S_1$ derives from a potential that does not depend explicitly on time. Here $\mathbf{W}$ and $\mathbf{F}_C$ have potentials ($mgz$ and $-\tfrac12 m\omega^2 r_\perp^2$, $\omega$ constant, Slide 30) and $\mathbf{F}_{COR}$ does no work (Slide 31). The question is the power of the tension, which is a constraint force of a constraint that moves.

**In $S_1$.** Define $E_1^P = \tfrac12 m\left|\mathbf{v}_1^P\right|^2 + mgz - \tfrac12 m\omega^2\left(x^2 + y^2\right)$. By the work–energy theorem in $S_1$, $\dfrac{dE_1^P}{dt} = \mathbf{T}\cdot\mathbf{v}_1^P = -T\,\mathbf{e}_{CP}\cdot\mathbf{v}_1^P$. From part (b), $\mathbf{e}_{CP}\cdot\mathbf{v}_1^P = \dot\xi\cos\varphi + \dot\ell$, and part (c) gives $\dot\ell + \dot\xi\cos\varphi = -R\omega\xi\sin\omega t/D$. Therefore

$$ \boxed{\frac{dE_1^P}{dt} = \frac{T\,R\,\omega\,\xi\sin\omega t}{\sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}}} $$

which is positive for $0 \lt \omega t \lt \pi$ (with $T \gt 0$, $\xi \gt 0$): **$E_1^P$ is not conserved.** The reason is that the end $A$ of the string moves in $S_1$ (part (a)): the constraint "string tense" depends explicitly on time in $S_1$, and the tension does work on $P$.

**In $S_0$.** $E_0^P = \tfrac12 m\left|\mathbf{v}_0^P\right|^2 + mgz$ changes at the rate $\mathbf{T}\cdot\mathbf{v}_0^P$ with $\mathbf{v}_0^P = \mathbf{v}_1^P + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P$ (Notes Eq. 3.26). The extra term is $-T\,\mathbf{e}_{CP}\cdot\omega\left(x\,\mathbf{j}_1 - y\,\mathbf{i}_1\right) = -T\omega\left(-x\sin\varphi\sin\theta - y\cos\varphi\right) = T\omega\sin\varphi\sin\theta\left(\xi + \ell\cos\varphi - \ell\cos\varphi\right) = T\omega\xi\sin\varphi\sin\theta$, so

$$ \frac{dE_0^P}{dt} = T\,\omega\,\xi\left(\frac{R\sin\omega t}{D} + \sin\varphi\sin\theta\right) \neq 0 $$

**No**: the mechanical energy of the particle is not conserved in either frame. The motor that keeps the bar at constant $\omega$ feeds energy into the particle through the string.

##### (h) Separation condition
* **Pedagogical Justification:** The string can only be pushed by the bar. The bar's force on the string, $\mathbf{N}_b = -T\left(\mathbf{e}_{CA} + \mathbf{e}_{CP}\right)$, vanishes when the string is straight; beyond that instant the bend would have to reverse, which a bar pushing from one side cannot impose. Separation is therefore the instant at which $A$, $C$ and $P$ become collinear: $\mathbf{e}_{CP} = -\mathbf{e}_{CA}$.

From part (c), $-\mathbf{e}_{CA} = \overrightarrow{AC}/D = \dfrac{1}{D}\left[(\xi - R\cos\omega t)\,\mathbf{i}_1 + R\sin\omega t\,\mathbf{j}_1 - h\,\mathbf{k}_1\right]$. The $\mathbf{i}_1$ components of $\mathbf{e}_{CP}$ and $-\mathbf{e}_{CA}$ are already equal (frictionless condition, $\cos\varphi = q/D$). Equating the other two, with $\sin\varphi = \rho/D$:

$$ -\frac{\rho}{D}\sin\theta = \frac{R\sin\omega t}{D}, \qquad -\frac{\rho}{D}\cos\theta = -\frac{h}{D} \quad\Longrightarrow\quad \sin\theta = -\frac{R\sin\omega t}{\rho}, \quad \cos\theta = \frac{h}{\rho} $$

Dividing the two relations ($\cos\theta = h/\rho \gt 0$):

$$ \boxed{\tan\theta = -\frac{R\sin\omega t}{h}} \qquad \text{i.e.}\quad \theta_{sep}(t) = -\arctan\left(\frac{R\sin\omega t}{h}\right) $$

The string leaves the bar at the first instant at which $\theta(t)$, obtained from the equations of part (e), reaches this value. For $0 \lt \omega t \lt \pi$ it is negative: $P$ must have swung forward, past the vertical plane of the bar, to the side opposite to $A$, so that the straight line from $A$ through $C$ passes through $P$.

##### Checks
* **Mechanism.** In $S_1$ the anchor $A$ circles backwards at radius $R$ and speed $\omega R$, while the string is held on the rotating bar. The string's end at $A$ and the bar together act as a moving constraint that pumps energy into the pendulum ($dE_1^P/dt \gt 0$ for $0 \lt \omega t \lt \pi$). The centrifugal force pushes $P$ outward along the bar ($+\mathbf{i}_1$); the Coriolis force deflects it sideways and couples $\xi$ and $\theta$.
* **Initial kick.** $\dot\theta(0) = \omega R/(L - h)$: in $S_1$ the particle starts swinging backwards about the contact point with the speed of the point of the bar that hits the string, a pendulum of length $L - h$.
* **Limits.** $R \to 0$: $A$ lies on the rotation axis and is fixed in $S_1$, the constraint becomes time-independent, and $dE_1^P/dt = TR\omega\xi\sin\omega t/D \to 0$: $E_1^P$ becomes a first integral (Slide 29). $\omega \to 0$: the inertia forces vanish and the bar would never reach the string; the problem reduces to a pendulum at rest. Separation: $h \to \infty$ gives $\theta_{sep} \to 0$; $\omega t = \pi$ (anchor on the opposite side of the bar) gives $\theta_{sep} = 0$. Basis: $\theta = 0$, $\varphi = \pi/2$ give $\mathbf{u} = -\mathbf{k}_1$ and $\mathbf{e}_{CP} = -\mathbf{k}_1$, the hanging string.
* **Inertial check.** Differentiating $[{}_0R_1]\mathbf{r}_1^P$ twice reproduces Notes Eq. 3.27; at random states, with $\ddot\xi$, $\ddot\theta$ taken from the two equations of part (e), $m\mathbf{a}_0^P - \mathbf{W}$ is parallel to $\mathbf{e}_{CP}$ (only the tension is left), and $dE_1^P/dt = -T\,\mathbf{e}_{CP}\cdot\mathbf{v}_1^P$; the constraint derivatives of part (c), the initial conditions and the separation condition were also checked symbolically with sympy.
* **Dimensions.** $[AC] = \sqrt{\text{m}^2} = \text{m}$; $[\omega^2\ell] = [\omega\dot\xi] = [g] = \text{m}\cdot\text{s}^{-2}$, the same as $[\ell\ddot\theta] = [\ddot\xi]$ in the equations of part (e); $[m\omega^2\xi] = [m\omega\dot\ell] = \text{kg}\cdot\text{m}\cdot\text{s}^{-2} = \text{N}$; $[\dot\theta(0)] = \dfrac{\text{s}^{-1}\cdot\text{m}}{\text{m}} = \text{s}^{-1}$; $\left[TR\omega\xi/D\right] = \dfrac{\text{N}\cdot\text{m}\cdot\text{s}^{-1}\cdot\text{m}}{\text{m}} = \text{W}$, a power; $[R\sin\omega t/h] = 1$, as $\tan\theta$ must be.
* **Check against the official key:** the centrifugal and Coriolis forces of part (d) coincide term by term with the official key (the key gives only these two forces).

---

## Problem 37: Particle on a Spinning Elliptic Cone

### Reference Frames, Bases and Coordinates
* **Physical system:** a heavy point particle $P$ of mass $m$ slides on the inner surface of an elliptic cone with vertex $O$ and vertical axis $Oz_1 \equiv Oz_0$. The cone spins about that axis with constant angular rate $\Omega$ relative to the inertial frame $S_0$.
* **Hypotheses:**
  1. $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ is inertial; gravity is $\mathbf{g} = -g\,\mathbf{k}_0$.
  2. The contact is smooth (no friction) and bilateral: the reaction of the cone is normal to its surface.
  3. $\Omega$ is constant and the vertex $O$ is fixed, so $O$ is a common origin of $S_0$ and $S_1$.
  4. The data $\mathbf{r}^P_{1,0} = 2\mathbf{j}_1 + \mathbf{k}_1$ and $\mathbf{v}^P_{1,0} = \mathbf{i}_1$ are read in SI units (m and m/s).
* **Why a moving frame:** in $S_0$ the surface of the cone moves, so the constraint depends explicitly on time. In the frame $S_1$ attached to the cone the surface is fixed and is described by the two parameters $(\zeta, \beta)$ of Eq. (5). The price is that $S_1$ is not inertial, so Newton's law in $S_1$ needs the inertia forces of Notes Eqs. 4.62–4.63 (Slides 27–28); they are known functions of the relative position and velocity.
* **Fixed (inertial) frame:** $S_0 = \{O; \mathcal{B}_0\}$, $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, with $\mathbf{k}_0$ vertical and upward.
* **Cone frame:** $S_1 = \{O; \mathcal{B}_1\}$, $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, attached to the cone, with $\mathbf{k}_1 = \mathbf{k}_0$ along its axis and $\mathbf{i}_1$, $\mathbf{j}_1$ along the two axes of its elliptic sections. It turns the angle $\Omega t$ about $\mathbf{k}_0$ (the figure of the statement measures $\Omega t$ from $x_0$ to $x_1$) and coincides with $S_0$ at $t = 0$.
* **Surface basis:** the two tangent vectors $\mathbf{e}_\zeta$, $\mathbf{e}_\beta$ of the cone at $P$ and its unit normal $\mathbf{n}$, deduced in the next section.
* **Coordinates:** $(\zeta, \beta)$, the parameters of Eq. (5): $\zeta$ is the height of $P$ above the vertex and $\beta$ the angular parameter of the elliptic section through $P$.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\Omega$ | constant spin rate of the cone | rad/s |
| $\zeta$ | height of $P$ above the vertex ($z_1 = \zeta$) | m |
| $\beta$ | angular parameter of the elliptic section | rad |
| $N$ | magnitude of the normal reaction | N |

##### (a) Degrees of freedom
* **Pedagogical Justification:** a free particle has 3 coordinates; each independent holonomic constraint removes one.

Eliminating the parameters of Eq. (5): $\cos\beta = x_1/\zeta$, $\sin\beta = y_1/(2\zeta)$ and $\zeta = z_1$, so $\cos^2\beta + \sin^2\beta = 1$ gives the single constraint equation of the surface, fixed in $S_1$:

$$ \frac{x_1^2}{z_1^2} + \frac{y_1^2}{4z_1^2} = 1 \iff x_1^2 + \frac{y_1^2}{4} - z_1^2 = 0 $$

Hence $\text{DOF} = 3 - 1 = 2$, and $(\zeta, \beta)$ are suitable generalized coordinates. Each horizontal section $z_1 = \zeta$ is an ellipse with semi-axes $\zeta$ (along $\mathbf{i}_1$) and $2\zeta$ (along $\mathbf{j}_1$).

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p37-top-view.svg]]

The cone spins about $\mathbf{k}_0$, so we look down the axis from $+z_0$: $\mathbf{k}_0 = \mathbf{k}_1$ points out of the paper, towards the reader ($\odot$). Take $\mathbf{i}_0$ to the right; then $\mathbf{j}_0 = \mathbf{k}_0\times\mathbf{i}_0$ points up the page (right-hand rule: fingers from $\mathbf{k}_0$, towards the reader, to $\mathbf{i}_0$, right; the thumb points up). With $\Omega \gt 0$ the cone turns counter-clockwise in this view (thumb along $\mathbf{k}_0$), and at time $t$ it has turned $\Omega t$ from $\mathbf{i}_0$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the shaded right triangle on the right: the leg adjacent to $\Omega t$ lies along $\mathbf{i}_0$ and measures $\cos\Omega t$; the opposite leg lies along $+\mathbf{j}_0$ and measures $\sin\Omega t$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ (up) and turns the same angle counter-clockwise, so its tip leans to the left, towards $-\mathbf{i}_0$: its leg along $\mathbf{j}_0$ (adjacent) is $\cos\Omega t$ and its leg along $-\mathbf{i}_0$ (opposite) is $\sin\Omega t$. **That is where the minus sign of $\mathbf{j}_1$ comes from.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

$$ \mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0, \qquad \mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0, \qquad \mathbf{k}_1 = \mathbf{k}_0 $$

The columns of the change-of-basis matrix are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \\ \sin\Omega t & \cos\Omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = \cos\Omega t\cos\Omega t - (-\sin\Omega t)\sin\Omega t = \cos^2\Omega t + \sin^2\Omega t = 1 $$

In the product $[{}_0R_1][{}_0R_1]^T$ the diagonal entries are $\cos^2\Omega t + \sin^2\Omega t = 1$ (first and second rows) and $1$ (third row), and the off-diagonal ones are $\cos\Omega t\sin\Omega t - \sin\Omega t\cos\Omega t = 0$ (first row times second) and $0$ (any row times the third), so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$:** the origin is fixed, $\mathbf{r}_0^O = \mathbf{v}_0^O = \mathbf{a}_0^O = \mathbf{0}$. For a simple rotation about the fixed vector $\mathbf{k}_0$ (Slide 16), $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{k}_1$. Check with the chain rule: $\left.\dfrac{d\mathbf{i}_1}{dt}\right|_0 = \dfrac{d\cos\Omega t}{d(\Omega t)}\,\Omega\,\mathbf{i}_0 + \dfrac{d\sin\Omega t}{d(\Omega t)}\,\Omega\,\mathbf{j}_0 = \Omega\left(-\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0\right) = \Omega\,\mathbf{j}_1 = \Omega\,\mathbf{k}_1\times\mathbf{i}_1$. Since $\Omega$ and $\mathbf{k}_1 = \mathbf{k}_0$ are constant, $\boldsymbol{\alpha}_{10} = \left.\dfrac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 = \mathbf{0}$.

#### The elliptic section through $P$

![[attachments/EM-SOL/p37-section.svg]]

$O$ is the origin of $S_1$, so $\mathbf{r}_1^P = \overrightarrow{OP}$ (Notes Eq. 3.16 with $\mathbf{r}_0^O = \mathbf{0}$). We build it in two steps: up the axis to the height of $P$, then across the horizontal section. The section $z_1 = \zeta$, seen from above, is the ellipse of semi-axes $\zeta$ along $\mathbf{i}_1$ and $2\zeta$ along $\mathbf{j}_1$.

**What $\beta$ is.** $\beta$ is not the polar angle of $P$. Draw the auxiliary circle of radius $\zeta$ (dashed) and the point $B$ of that circle at the polar angle $\beta$. In the shaded right triangle with vertex $O$ and hypotenuse $OB = \zeta$, the leg adjacent to $\beta$ lies along $\mathbf{i}_1$ and measures $\zeta\cos\beta$, and the opposite leg measures $\zeta\sin\beta$. The point of the ellipse has the same $x_1 = \zeta\cos\beta$ and twice the height, $y_1 = 2\zeta\sin\beta$: the ellipse is the circle stretched by a factor 2 along $\mathbf{j}_1$. So $\beta$ is the polar angle of $B$, not of $P$; the polar angle $\alpha$ of the horizontal projection of $P$ satisfies

$$ \tan\alpha = \frac{y_1}{x_1} = \frac{2\zeta\sin\beta}{\zeta\cos\beta} = 2\tan\beta $$

and $\alpha = \beta$ only at $\beta = 0, \pi/2, \pi, 3\pi/2$, on the axes of the ellipse. Adding the vertical part $\zeta\,\mathbf{k}_1$:

$$ \mathbf{r}_1^P = \zeta\cos\beta\,\mathbf{i}_1 + 2\zeta\sin\beta\,\mathbf{j}_1 + \zeta\,\mathbf{k}_1 $$

Check with the initial datum: $\zeta = 1$, $\beta = \pi/2$ give $2\mathbf{j}_1 + \mathbf{k}_1 = \mathbf{r}^P_{1,0}$.

**Tangent vectors and normal of the cone.** Two tangent vectors at $P$ are the partial derivatives of $\mathbf{r}_1^P$ with respect to each parameter (they are not unit vectors). With $\frac{\partial}{\partial\beta}\cos\beta = -\sin\beta$ and $\frac{\partial}{\partial\beta}\sin\beta = \cos\beta$:

$$ \mathbf{e}_\zeta \equiv \frac{\partial\mathbf{r}_1^P}{\partial\zeta} = \cos\beta\,\mathbf{i}_1 + 2\sin\beta\,\mathbf{j}_1 + \mathbf{k}_1, \qquad \frac{\partial\mathbf{r}_1^P}{\partial\beta} = \zeta\,\mathbf{e}_\beta, \quad \mathbf{e}_\beta \equiv -\sin\beta\,\mathbf{i}_1 + 2\cos\beta\,\mathbf{j}_1 $$

$\mathbf{e}_\zeta$ runs along the generator through $P$ (the straight line from the vertex) and $\mathbf{e}_\beta$ is tangent to the ellipse, drawn at $P$ in the figure. A normal vector is their cross product, expanded component by component:

$$ \mathbf{e}_\zeta\times\mathbf{e}_\beta = \begin{vmatrix} \mathbf{i}_1 & \mathbf{j}_1 & \mathbf{k}_1 \\ \cos\beta & 2\sin\beta & 1 \\ -\sin\beta & 2\cos\beta & 0 \end{vmatrix} = \left(0 - 2\cos\beta\right)\mathbf{i}_1 - \left(0 + \sin\beta\right)\mathbf{j}_1 + \left(2\cos^2\beta + 2\sin^2\beta\right)\mathbf{k}_1 = -2\cos\beta\,\mathbf{i}_1 - \sin\beta\,\mathbf{j}_1 + 2\,\mathbf{k}_1 $$

Its squared norm is $4\cos^2\beta + \sin^2\beta + 4 = 5 + 3\cos^2\beta$, so the unit normal (pointing into the cone, upward) is

$$ \mathbf{n} = \frac{-2\cos\beta\,\mathbf{i}_1 - \sin\beta\,\mathbf{j}_1 + 2\,\mathbf{k}_1}{\sqrt{5 + 3\cos^2\beta}} $$

(Check: the gradient of $x_1^2 + y_1^2/4 - z_1^2$ is $(2x_1, y_1/2, -2z_1) = \zeta(2\cos\beta, \sin\beta, -2)$, parallel to $\mathbf{n}$.)

#### The two principal vertical sections

![[attachments/EM-SOL/p37-sections.svg]]

In the vertical plane $x_1z_1$ ($\beta = 0$ or $\pi$) the generators are the lines $z_1 = |x_1|$: in the shaded right triangle the horizontal leg is $\zeta$ and the vertical leg is $\zeta$, so the hypotenuse is $\zeta\sqrt2$ and the generator makes $45^\circ$ with the horizontal. In the plane $y_1z_1$ ($\beta = \pm\pi/2$) the generators are $z_1 = |y_1|/2$: horizontal leg $2\zeta$, vertical leg $\zeta$, hypotenuse $\sqrt{4\zeta^2 + \zeta^2} = \zeta\sqrt5$. At $\beta = 0$, $\mathbf{e}_\zeta = \mathbf{i}_1 + \mathbf{k}_1$ and $\mathbf{n} = (-\mathbf{i}_1 + \mathbf{k}_1)/\sqrt2$; at $\beta = \pi/2$, $\mathbf{e}_\zeta = 2\mathbf{j}_1 + \mathbf{k}_1$ and $\mathbf{n} = (-\mathbf{j}_1 + 2\mathbf{k}_1)/\sqrt5$, perpendicular to the generator in each drawing. These sections are where the equilibria of part (f) lie.

### Kinematics

##### (b) Position, velocity and acceleration in $S_1$
* **Pedagogical Justification:** the relative derivatives $\left.\frac{d}{dt}\right|_1$ treat $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ as constants, so only the components of $\mathbf{r}_1^P$ are differentiated (product and chain rules).

$$ \mathbf{r}_1^P = \zeta\cos\beta\,\mathbf{i}_1 + 2\zeta\sin\beta\,\mathbf{j}_1 + \zeta\,\mathbf{k}_1 $$

Component by component, with $\frac{d}{dt}\cos\beta = \frac{d\cos\beta}{d\beta}\dot\beta = -\dot\beta\sin\beta$ and $\frac{d}{dt}\sin\beta = \dot\beta\cos\beta$:

$$ \frac{d}{dt}\left(\zeta\cos\beta\right) = \dot\zeta\cos\beta - \zeta\dot\beta\sin\beta, \qquad \frac{d}{dt}\left(2\zeta\sin\beta\right) = 2\dot\zeta\sin\beta + 2\zeta\dot\beta\cos\beta, \qquad \frac{d}{dt}\zeta = \dot\zeta $$
$$ \mathbf{v}_1^P = \left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\mathbf{i}_1 + 2\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\mathbf{j}_1 + \dot\zeta\,\mathbf{k}_1 $$

Equivalently $\mathbf{v}_1^P = \dot\zeta\,\mathbf{e}_\zeta + \zeta\dot\beta\,\mathbf{e}_\beta$: the velocity is tangent to the cone.

Differentiating again. For the $\mathbf{i}_1$ component, $\frac{d}{dt}(\dot\zeta\cos\beta) = \ddot\zeta\cos\beta - \dot\zeta\dot\beta\sin\beta$ and $\frac{d}{dt}(\zeta\dot\beta\sin\beta) = \dot\zeta\dot\beta\sin\beta + \zeta\ddot\beta\sin\beta + \zeta\dot\beta^2\cos\beta$; for the $\mathbf{j}_1$ component, $\frac{d}{dt}(\dot\zeta\sin\beta) = \ddot\zeta\sin\beta + \dot\zeta\dot\beta\cos\beta$ and $\frac{d}{dt}(\zeta\dot\beta\cos\beta) = \dot\zeta\dot\beta\cos\beta + \zeta\ddot\beta\cos\beta - \zeta\dot\beta^2\sin\beta$. Collecting terms:

$$ \mathbf{a}_1^P = \left[\left(\ddot\zeta - \zeta\dot\beta^2\right)\cos\beta - \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\sin\beta\right]\mathbf{i}_1 + 2\left[\left(\ddot\zeta - \zeta\dot\beta^2\right)\sin\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\cos\beta\right]\mathbf{j}_1 + \ddot\zeta\,\mathbf{k}_1 $$

The unit vectors $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ are defined in terms of $\mathcal{B}_0$ in the change-of-basis section. For later use we write $\mathbf{r}_1^P = x_1\mathbf{i}_1 + y_1\mathbf{j}_1 + z_1\mathbf{k}_1$ and $\mathbf{v}_1^P = \dot x_1\mathbf{i}_1 + \dot y_1\mathbf{j}_1 + \dot z_1\mathbf{k}_1$ with the components above.

### Forces and Equations of Motion

##### (c) Forces acting on $P$ as seen from $S_1$
* **Pedagogical Justification:** in the non-inertial frame $S_1$ Newton's law reads $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ (Notes Eq. 4.63), where $\mathbf{F}$ are the actual forces and $\mathbf{F}_i$ the inertia forces of Notes Eq. 4.62 (Slide 28).

**1. Weight:** $\mathbf{W} = -mg\,\mathbf{k}_0 = -mg\,\mathbf{k}_1$.

**2. Normal reaction.** The contact is smooth, so the reaction is along the unit normal of the change-of-basis section:

$$ \mathbf{N} = N\,\mathbf{n}, \qquad \mathbf{n} = \frac{-2\cos\beta\,\mathbf{i}_1 - \sin\beta\,\mathbf{j}_1 + 2\,\mathbf{k}_1}{\sqrt{5 + 3\cos^2\beta}} $$

with $N$ an unknown scalar.

**3. Inertia forces** (Notes Eq. 4.62). Since $\mathbf{a}_0^O = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$, the force due to the acceleration of the origin and the Euler force vanish: $\mathbf{F}_A = -m\mathbf{a}_0^O = \mathbf{0}$, $\mathbf{F}_E = -m\boldsymbol{\alpha}_{10}\times\mathbf{r}_1^P = \mathbf{0}$.

*Centrifugal force.* With $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$:

$$ \boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = \Omega\,\mathbf{k}_1\times\left(x_1\mathbf{i}_1 + y_1\mathbf{j}_1 + z_1\mathbf{k}_1\right) = \Omega\left(x_1\mathbf{j}_1 - y_1\mathbf{i}_1\right) $$
$$ \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \Omega\,\mathbf{k}_1\times\Omega\left(x_1\mathbf{j}_1 - y_1\mathbf{i}_1\right) = -\Omega^2\left(x_1\mathbf{i}_1 + y_1\mathbf{j}_1\right) $$
$$ \mathbf{F}_C = -m\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = m\Omega^2\left(x_1\mathbf{i}_1 + y_1\mathbf{j}_1\right) = m\Omega^2\zeta\left(\cos\beta\,\mathbf{i}_1 + 2\sin\beta\,\mathbf{j}_1\right) $$

which is $m\Omega^2\mathbf{r}_\perp$, radially outward from the axis (Slide 30).

*Coriolis force.*

$$ \mathbf{F}_{COR} = -2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = -2m\Omega\,\mathbf{k}_1\times\left(\dot x_1\mathbf{i}_1 + \dot y_1\mathbf{j}_1 + \dot z_1\mathbf{k}_1\right) = 2m\Omega\left(\dot y_1\,\mathbf{i}_1 - \dot x_1\,\mathbf{j}_1\right) $$
$$ \mathbf{F}_{COR} = 4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\mathbf{i}_1 - 2m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\mathbf{j}_1 $$

**Equation of motion in $S_1$** (Notes Eq. 4.63):

$$ m\mathbf{a}_1^P = -mg\,\mathbf{k}_1 + N\,\mathbf{n} + \mathbf{F}_C + \mathbf{F}_{COR} $$

##### (d) Two equations of motion free of the reaction
* **Pedagogical Justification:** the only unknown besides $\zeta$ and $\beta$ is $N$, and $\mathbf{N}$ is perpendicular to the surface. Projecting the vector equation on the two tangent vectors $\mathbf{e}_\zeta$ and $\mathbf{e}_\beta$ eliminates it: $(-2\cos\beta)\cos\beta + (-\sin\beta)(2\sin\beta) + 2 = 0$ and $(-2\cos\beta)(-\sin\beta) + (-\sin\beta)(2\cos\beta) = 0$.

**Projection on $\mathbf{e}_\zeta = (\cos\beta, 2\sin\beta, 1)$.** Left-hand side:

$$ \mathbf{a}_1^P\cdot\mathbf{e}_\zeta = \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(\cos^2\beta + 4\sin^2\beta\right) + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(-\sin\beta\cos\beta + 4\sin\beta\cos\beta\right) + \ddot\zeta $$
$$ = \ddot\zeta + \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(1 + 3\sin^2\beta\right) + 3\left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\sin\beta\cos\beta $$

Right-hand side, term by term: $-mg\,\mathbf{k}_1\cdot\mathbf{e}_\zeta = -mg$; $\mathbf{F}_C\cdot\mathbf{e}_\zeta = m\Omega^2\zeta\left(\cos^2\beta + 4\sin^2\beta\right) = m\Omega^2\zeta\left(1 + 3\sin^2\beta\right)$;

$$ \mathbf{F}_{COR}\cdot\mathbf{e}_\zeta = 4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\cos\beta - 4m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\sin\beta = 4m\Omega\zeta\dot\beta\left(\cos^2\beta + \sin^2\beta\right) = 4m\Omega\zeta\dot\beta $$

Dividing by $m$:

$$ \boxed{\ddot\zeta + \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(1 + 3\sin^2\beta\right) + 3\left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\cos\beta\sin\beta = -g + \Omega^2\zeta\left(1 + 3\sin^2\beta\right) + 4\Omega\zeta\dot\beta} $$

**Projection on $\mathbf{e}_\beta = (-\sin\beta, 2\cos\beta, 0)$.** Left-hand side:

$$ \mathbf{a}_1^P\cdot\mathbf{e}_\beta = \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(-\sin\beta\cos\beta + 4\sin\beta\cos\beta\right) + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(\sin^2\beta + 4\cos^2\beta\right) = 3\left(\ddot\zeta - \zeta\dot\beta^2\right)\sin\beta\cos\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(1 + 3\cos^2\beta\right) $$

Right-hand side: $-mg\,\mathbf{k}_1\cdot\mathbf{e}_\beta = 0$; $\mathbf{F}_C\cdot\mathbf{e}_\beta = m\Omega^2\zeta\left(-\cos\beta\sin\beta + 4\sin\beta\cos\beta\right) = 3m\Omega^2\zeta\sin\beta\cos\beta$;

$$ \mathbf{F}_{COR}\cdot\mathbf{e}_\beta = -4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\sin\beta - 4m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\cos\beta = -4m\Omega\dot\zeta $$

Dividing by $m$:

$$ \boxed{3\left(\ddot\zeta - \zeta\dot\beta^2\right)\cos\beta\sin\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(1 + 3\cos^2\beta\right) = 3\Omega^2\zeta\cos\beta\sin\beta - 4\Omega\dot\zeta} $$

These two equations contain only $\zeta$, $\beta$ and their derivatives. The initial conditions follow from the data: $\mathbf{r}^P_{1,0} = 2\mathbf{j}_1 + \mathbf{k}_1$ gives $\zeta_0 = 1$, $\zeta_0\cos\beta_0 = 0$ and $2\zeta_0\sin\beta_0 = 2$, so $\beta_0 = \pi/2$; $\mathbf{v}^P_{1,0} = \mathbf{i}_1$ gives $\dot\zeta_0 = 0$ ($\mathbf{k}_1$ component) and $\dot\zeta_0\cos\beta_0 - \zeta_0\dot\beta_0\sin\beta_0 = -\dot\beta_0 = 1$, so $\dot\beta_0 = -1$ rad/s; the $\mathbf{j}_1$ component $2(\dot\zeta_0\sin\beta_0 + \zeta_0\dot\beta_0\cos\beta_0) = 0$ is consistent (the initial velocity is tangent to the cone).

### Answers and Checks

##### (a) Degrees of freedom
$\text{DOF} = 2$, with generalized coordinates $(\zeta, \beta)$.

##### (b) Kinematics in $S_1$
$\mathbf{r}_1^P$, $\mathbf{v}_1^P$ and $\mathbf{a}_1^P$ as in the kinematics section, with $\mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0$, $\mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0$, $\mathbf{k}_1 = \mathbf{k}_0$.

##### (c) Forces
Weight $-mg\,\mathbf{k}_1$, normal reaction $N\,\mathbf{n}$, centrifugal force $m\Omega^2\zeta(\cos\beta\,\mathbf{i}_1 + 2\sin\beta\,\mathbf{j}_1)$ and Coriolis force $2m\Omega(\dot y_1\,\mathbf{i}_1 - \dot x_1\,\mathbf{j}_1)$; the Euler force and the force of the origin's acceleration are zero.

##### (d) Equations of motion
The two boxed equations of the previous section, with $\zeta_0 = 1$ m, $\beta_0 = \pi/2$, $\dot\zeta_0 = 0$, $\dot\beta_0 = -1$ rad/s.

##### (e) Conservation law: mechanical energy in $S_1$
* **Pedagogical Justification:** $E_1^P$ is conserved when every force that does work in $S_1$, inertia forces included, derives from a potential (Slide 29). Here: $\mathbf{N}\cdot\mathbf{v}_1^P = 0$ because the cone is fixed in $S_1$ and $\mathbf{v}_1^P$ is tangent to it; $\mathbf{F}_{COR}\cdot\mathbf{v}_1^P = 0$ always (Slide 31); $\mathbf{F}_A = \mathbf{F}_E = \mathbf{0}$; the weight is a constant force in $S_1$ ($\mathbf{k}_1 = \mathbf{k}_0$) with potential $mgz_1$; and, since $\boldsymbol{\omega}_{10}$ is constant, the centrifugal force has potential $-\tfrac12 m\Omega^2 r_\perp^2$ (Slide 30).

Kinetic energy in $S_1$, expanding the squares of the components of $\mathbf{v}_1^P$:

$$ \left|\mathbf{v}_1^P\right|^2 = \left(\dot\zeta^2\cos^2\beta - 2\zeta\dot\zeta\dot\beta\sin\beta\cos\beta + \zeta^2\dot\beta^2\sin^2\beta\right) + 4\left(\dot\zeta^2\sin^2\beta + 2\zeta\dot\zeta\dot\beta\sin\beta\cos\beta + \zeta^2\dot\beta^2\cos^2\beta\right) + \dot\zeta^2 $$
$$ T_1^P = \frac{m}{2}\left[\left(2 + 3\sin^2\beta\right)\dot\zeta^2 + \left(1 + 3\cos^2\beta\right)\zeta^2\dot\beta^2 + 6\zeta\dot\zeta\dot\beta\sin\beta\cos\beta\right] $$

Potential in $S_1$, with $z_1 = \zeta$ and $r_\perp^2 = x_1^2 + y_1^2 = \zeta^2\left(\cos^2\beta + 4\sin^2\beta\right) = \zeta^2\left(1 + 3\sin^2\beta\right)$:

$$ V_1 = mg\zeta - \frac12 m\Omega^2\zeta^2\left(1 + 3\sin^2\beta\right) $$

**Direct check that $E_1^P = T_1^P + V_1$ is constant.** Since $\mathbf{v}_1^P = \dot\zeta\,\mathbf{e}_\zeta + \zeta\dot\beta\,\mathbf{e}_\beta$ and $\dfrac{dV_1}{dt} = -\left(\mathbf{W} + \mathbf{F}_C\right)\cdot\mathbf{v}_1^P$ (chain rule on $V_1(\mathbf{r}_1^P(t))$):

$$ \frac{dE_1^P}{dt} = \left(m\mathbf{a}_1^P - \mathbf{W} - \mathbf{F}_C\right)\cdot\mathbf{v}_1^P = \dot\zeta\left(m\mathbf{a}_1^P - \mathbf{W} - \mathbf{F}_C\right)\cdot\mathbf{e}_\zeta + \zeta\dot\beta\left(m\mathbf{a}_1^P - \mathbf{W} - \mathbf{F}_C\right)\cdot\mathbf{e}_\beta $$

and by the two equations of part (d) the brackets equal $4m\Omega\zeta\dot\beta$ and $-4m\Omega\dot\zeta$, so

$$ \frac{dE_1^P}{dt} = \dot\zeta\left(4m\Omega\zeta\dot\beta\right) + \zeta\dot\beta\left(-4m\Omega\dot\zeta\right) = 0 $$

**Conservation law:**

$$ \boxed{\frac{m}{2}\left[\left(2 + 3\sin^2\beta\right)\dot\zeta^2 + \left(1 + 3\cos^2\beta\right)\zeta^2\dot\beta^2 + 6\zeta\dot\zeta\dot\beta\sin\beta\cos\beta\right] + mg\zeta - \frac{m}{2}\Omega^2\zeta^2\left(1 + 3\sin^2\beta\right) = E_1^P = m\left(\tfrac12 v_0^2 + g\zeta_0 - 2\Omega^2\zeta_0^2\right)} $$
with $v_0 = |\mathbf{v}^P_{1,0}| = 1$ m/s and $\zeta_0 = 1$ m, so numerically $E_1^P = m\left(\tfrac12 + g - 2\Omega^2\right)$ in SI units.

The constant comes from $t = 0$: $\zeta_0 = 1$ m, $\beta_0 = \pi/2$, $\dot\zeta_0 = 0$, $\dot\beta_0 = -1$ rad/s give $T_1^P(0) = \frac{m}{2}\left(1 + 0\right)(1)^2(-1)^2 = \frac{m}{2}$ (that is, $\tfrac12 m|\mathbf{v}^P_{1,0}|^2$ with $|\mathbf{v}^P_{1,0}| = 1$ m/s) and $V_1(0) = mg(1) - \frac12 m\Omega^2(1)^2(1 + 3) = m\left(g - 2\Omega^2\right)$, in joules when $m$, $g$ and $\Omega$ are in SI units.

The angular momentum about $Oz_0$ is **not** conserved: the moment of $\mathbf{N}$ about the axis is $\left(\mathbf{r}_1^P\times\mathbf{n}\right)\cdot\mathbf{k}_1\,N = \left(x_1n_y - y_1n_x\right)N = \dfrac{\zeta\left(-\cos\beta\sin\beta + 4\sin\beta\cos\beta\right)}{\sqrt{5 + 3\cos^2\beta}}N = \dfrac{3\zeta\sin\beta\cos\beta}{\sqrt{5 + 3\cos^2\beta}}N$, which does not vanish in general because the section is not circular.

##### (f) Equilibrium positions in $S_1$
* **Pedagogical Justification:** an equilibrium in $S_1$ is a solution with $\zeta$ and $\beta$ constant, so $\dot\zeta = \dot\beta = \ddot\zeta = \ddot\beta = 0$ in the two equations of part (d); the Coriolis terms vanish automatically.

The $\mathbf{e}_\beta$ equation reduces to $0 = 3\Omega^2\zeta\cos\beta\sin\beta = \tfrac32\Omega^2\zeta\sin 2\beta$. With $\zeta \gt 0$ and $\Omega \neq 0$, $\sin 2\beta = 0$:

$$ \beta \in \left\{0,\ \frac{\pi}{2},\ \pi,\ \frac{3\pi}{2}\right\} $$

The $\mathbf{e}_\zeta$ equation reduces to $0 = -g + \Omega^2\zeta\left(1 + 3\sin^2\beta\right)$, so

$$ \zeta_{eq} = \frac{g}{\Omega^2\left(1 + 3\sin^2\beta\right)} $$

| $\beta$ | $\zeta_{eq}$ | Position $\mathbf{r}_1^P$ |
|---|---|---|
| $0$ | $g/\Omega^2$ | $\dfrac{g}{\Omega^2}\left(\mathbf{i}_1 + \mathbf{k}_1\right)$ |
| $\pi$ | $g/\Omega^2$ | $\dfrac{g}{\Omega^2}\left(-\mathbf{i}_1 + \mathbf{k}_1\right)$ |
| $\pi/2$ | $g/(4\Omega^2)$ | $\dfrac{g}{2\Omega^2}\mathbf{j}_1 + \dfrac{g}{4\Omega^2}\mathbf{k}_1$ |
| $3\pi/2$ | $g/(4\Omega^2)$ | $-\dfrac{g}{2\Omega^2}\mathbf{j}_1 + \dfrac{g}{4\Omega^2}\mathbf{k}_1$ |

**Force-balance check at $\beta = 0$:** $\mathbf{n} = (-2, 0, 2)/\sqrt{8}$, so $\mathbf{0} = -mg\,\mathbf{k}_1 + m\Omega^2\zeta\,\mathbf{i}_1 + \dfrac{N}{\sqrt2}\left(-\mathbf{i}_1 + \mathbf{k}_1\right)$ gives $N = \sqrt2\,mg$ and $\Omega^2\zeta = g$. **At $\beta = \pi/2$:** $\mathbf{n} = (0, -1, 2)/\sqrt5$, so $\mathbf{0} = -mg\,\mathbf{k}_1 + 2m\Omega^2\zeta\,\mathbf{j}_1 + \dfrac{N}{\sqrt5}\left(-\mathbf{j}_1 + 2\mathbf{k}_1\right)$ gives $N = \tfrac{\sqrt5}{2}mg$ and $2\Omega^2\zeta = \tfrac{g}{2}$, i.e. $\zeta = g/(4\Omega^2)$. Both agree with the table.

*Extension (stability, not asked):* the Hessian of $V_1(\zeta, \beta)$ is $\operatorname{diag}\left(-m\Omega^2,\ -3mg^2/\Omega^2\right)$ at $\beta = 0, \pi$ and $\operatorname{diag}\left(-4m\Omega^2,\ 3mg^2/(16\Omega^2)\right)$ at $\beta = \pi/2, 3\pi/2$. $V_1$ has no minimum (along each generator it is a downward parabola in $\zeta$), so the energy criterion cannot certify the stability of any of these equilibria.

##### Checks
* **Meaning of the equilibria:** they lie on the four generators contained in the principal planes $x_1z_1$ and $y_1z_1$ of the cone (the sections drawn above). Only there does the normal $\mathbf{n}$ lie in the vertical plane through the axis, so that it can balance the weight and the (radial) centrifugal force without a tangential remainder. On the steeper generators ($\beta = 0, \pi$, slope $45^\circ$) the particle must be higher, $\zeta = g/\Omega^2$, than on the flatter ones ($\beta = \pm\pi/2$, $\zeta = g/(4\Omega^2)$).
* **Gyroscopic coupling:** the Coriolis terms $4\Omega\zeta\dot\beta$ and $-4\Omega\dot\zeta$ couple the two equations antisymmetrically, which is why they cancel in $dE_1^P/dt$ (Coriolis never does work).
* **Limit $\Omega \to 0$:** the centrifugal and Coriolis terms vanish, $E_1^P$ becomes the ordinary energy $\tfrac12 m v^2 + mgz$, and $\zeta_{eq} \to \infty$: a fixed, vertex-down smooth cone has no equilibrium position with $\zeta \gt 0$. Basis: $t = 0$ gives $[{}_0R_1] = I$, the two frames coincide as stated.
* **Orthogonality:** $\mathbf{n}\cdot\mathbf{e}_\zeta = \mathbf{n}\cdot\mathbf{e}_\beta = 0$ (computed in part (d)); $\mathbf{e}_\zeta$ and $\mathbf{e}_\beta$ are not orthogonal in general, $\mathbf{e}_\zeta\cdot\mathbf{e}_\beta = 3\sin\beta\cos\beta$, which is why the projections of part (d) mix the two accelerations.
* **Dimensions:** in the $\mathbf{e}_\zeta$ equation, $[\ddot\zeta] = [\zeta\dot\beta^2] = [\dot\zeta\dot\beta] = [\zeta\ddot\beta] = \text{m/s}^2$, $[g] = \text{m/s}^2$, $[\Omega^2\zeta] = \text{s}^{-2}\,\text{m}$, $[\Omega\zeta\dot\beta] = \text{s}^{-1}\,\text{m}\,\text{s}^{-1}$; the $\mathbf{e}_\beta$ equation has the same terms. $[E_1^P] = \text{kg}\,\text{m}^2/\text{s}^2 = \text{J}$; $[g/\Omega^2] = (\text{m/s}^2)/\text{s}^{-2} = \text{m}$.
* **Symbolic check (sympy):** $\mathbf{a}_0^P$ obtained by differentiating $[{}_0R_1]\,\mathbf{r}_1^P$ twice equals $\mathbf{a}_1^P + \boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P$ (Notes Eq. 3.27); both projections match the key; $dE_1^P/dt = 0$ along the equations of motion; the four equilibria satisfy both equations.
* **Check against the official key:** both equations of part (d) coincide with the official key (Problems.pdf, p. 75) term by term.

---

## Problem 40: Spring-Coupled Particles on a Vertical Axis and a Revolving Ring

### Reference Frames, Bases and Coordinates
* **Physical system:** two heavy particles of mass $m$. $P$ slides on the fixed vertical axis $Oz_0$; $Q$ slides on a horizontal ring of radius $R$ in the plane $z_0 = 0$ whose centre $D$, at distance $\ell$ from $O$, revolves about $Oz_0$ at constant rate $\Omega$. A spring of stiffness $k$ joins $P$ and $Q$.
* **Hypotheses:**
  1. $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ is inertial, $\mathbf{k}_0$ vertical upward, gravity $-g\,\mathbf{k}_0$.
  2. Both contacts are smooth and bilateral: the reactions have no component along the direction in which each particle can move.
  3. The spring is linear and massless, with zero natural length (no natural length is given), so the force it exerts on $P$ is $k\left(\mathbf{r}^Q - \mathbf{r}^P\right)$ and on $Q$ the opposite.
  4. The ring moves rigidly with $S_1$ (only its centre's motion is prescribed; it does not spin relative to $S_1$, which is irrelevant anyway for a smooth circular wire).
  5. $\phi$ is measured from $\mathbf{j}_1$ in the positive sense about $\mathbf{k}_1$ (from $\mathbf{j}_1$ towards $-\mathbf{i}_1$), as in the figure; this is also the convention of the official key, whose ring reaction contains the radial vector $-\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{j}_1$.
* **Why $S_1$:** in $S_1$ the ring is fixed (centre at $\ell\,\mathbf{j}_1$), so $Q$ moves on a fixed circle described by $\phi$ alone and $P$ stays on the axis. The inertia forces (Notes Eq. 4.62) are the price; for $P$, on the rotation axis, they vanish.
* **Fixed (inertial) frame:** $S_0 = \{O; \mathcal{B}_0\}$, $\mathcal{B}_0 = \{\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Moving frame:** $S_1 = \{O; \mathcal{B}_1\}$ with the same origin, $\mathbf{k}_1 = \mathbf{k}_0$ and $\mathbf{j}_1$ pointing from $O$ to $D$. $S_1$ is turned $\Omega t$ about $\mathbf{k}_0$ (the figure of the statement measures $\Omega t$ from $\mathbf{i}_0$ to $\mathbf{i}_1$), and we take $S_1 \equiv S_0$ at $t = 0$.
* **Ring basis:** $\{\mathbf{e}_r, \mathbf{e}_\phi, \mathbf{k}_1\}$ attached to $Q$: $\mathbf{e}_r$ from $D$ to $Q$, $\mathbf{e}_\phi$ tangent to the ring; deduced in the next section.
* **Coordinates:** $\zeta$, the height of $P$ on the axis, and $\phi$, the angle of $Q$ on the ring.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of each particle | kg |
| $k$ | spring stiffness | N/m |
| $R$ | radius of the ring | m |
| $\ell$ | distance $OD$ | m |
| $\Omega$ | constant angular rate of $D$ | rad/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\zeta$, $\phi$ | height of $P$, angle of $Q$ on the ring | m, rad |
| $N_1, \dots, N_4$ | reaction components | N |

##### (a) Degrees of freedom and the basis $\mathcal{B}_1$
* **Pedagogical Justification:** count coordinates minus independent constraints for each particle.

$P$ is free in space (3 coordinates) but constrained to the vertical axis ($x = y = 0$): 1 DOF, the height $\zeta$. $Q$ (3 coordinates) is constrained to the plane $z_1 = 0$ and to the circle $\left|\mathbf{r}^Q - \overrightarrow{OD}\right| = R$: 1 DOF, the angle $\phi$. The motion of $D$ is prescribed, so it adds no unknown. Hence

$$ \text{DOF} = 6 - 4 = 2, \qquad \text{generalized coordinates } (\zeta, \phi) $$

The vectors of $\mathcal{B}_1$ in terms of $\mathcal{B}_0$ are deduced in the next section.

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p40-top-view.svg]]

$S_1$ turns about the vertical, so we look down the axis from $+z_0$: $\mathbf{k}_0 = \mathbf{k}_1$ points out of the paper ($\odot$). With $\mathbf{i}_0$ to the right, $\mathbf{j}_0 = \mathbf{k}_0\times\mathbf{i}_0$ points up the page (right-hand rule: fingers from $\mathbf{k}_0$, towards the reader, to $\mathbf{i}_0$; thumb up). With $\Omega \gt 0$ the frame turns counter-clockwise in this view, and at time $t$ it has turned $\Omega t$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the right triangle whose leg adjacent to $\Omega t$ lies along $\mathbf{i}_0$ ($\cos\Omega t$) and whose opposite leg lies along $+\mathbf{j}_0$ ($\sin\Omega t$).
* $\mathbf{j}_1$, the direction of $D$, starts on $\mathbf{j}_0$ and turns the same angle counter-clockwise, so it leans to the left: adjacent leg $\cos\Omega t$ along $\mathbf{j}_0$, opposite leg $\sin\Omega t$ along $-\mathbf{i}_0$. **The minus sign of $\mathbf{j}_1$ is that leftward lean.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

$$ \mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0, \qquad \mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0, \qquad \mathbf{k}_1 = \mathbf{k}_0 $$
$$ [{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \\ \sin\Omega t & \cos\Omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = \cos\Omega t\cos\Omega t - (-\sin\Omega t)\sin\Omega t = \cos^2\Omega t + \sin^2\Omega t = 1 $$

**Orthogonality:** in $[{}_0R_1][{}_0R_1]^T$ each diagonal entry is a squared row norm, $\cos^2\Omega t + \sin^2\Omega t = 1$ (or $1$ for the third row), and the first two rows have dot product $\cos\Omega t\sin\Omega t - \sin\Omega t\cos\Omega t = 0$ (the third row is orthogonal to both), so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$:** $\mathbf{r}_0^O = \mathbf{v}_0^O = \mathbf{a}_0^O = \mathbf{0}$; simple rotation about $\mathbf{k}_0$ (Slide 16): $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{k}_1$, and $\boldsymbol{\alpha}_{10} = \mathbf{0}$ because $\Omega$ and $\mathbf{k}_0$ are constant. Check with the chain rule: $\left.\frac{d\mathbf{j}_1}{dt}\right|_0 = -\Omega\cos\Omega t\,\mathbf{i}_0 - \Omega\sin\Omega t\,\mathbf{j}_0 = -\Omega\,\mathbf{i}_1 = \Omega\,\mathbf{k}_1\times\mathbf{j}_1$.

#### The ring and the position of $Q$

![[attachments/EM-SOL/p40-ring.svg]]

The plane of the ring is fixed in $S_1$; we draw it from above ($\mathbf{k}_1$ out of the paper), with $\mathbf{i}_1$ to the right and $\mathbf{j}_1$ up, towards $D$. To go from $O$ to $Q$ we pass through the centre of the ring, because the distance from $D$ is the one that stays constant:

$$ \overrightarrow{OQ} = \overrightarrow{OD} + \overrightarrow{DQ}, \qquad \overrightarrow{OD} = \ell\,\mathbf{j}_1 $$

$\overrightarrow{DQ}$ has length $R$ and makes the angle $\phi$ with $\mathbf{j}_1$, measured counter-clockwise (towards $-\mathbf{i}_1$). Let $F$ be the point of the line $D + s\,\mathbf{j}_1$ level with $Q$. In the shaded right triangle $DFQ$ (right angle at $F$) the hypotenuse is $DQ = R$, the leg adjacent to $\phi$ is $DF = R\cos\phi$, along $+\mathbf{j}_1$, and the opposite leg is $FQ = R\sin\phi$, along $-\mathbf{i}_1$ because a counter-clockwise turn from $\mathbf{j}_1$ carries the point to the left. Hence the unit radial vector of the ring is

$$ \mathbf{e}_r = \frac{\overrightarrow{DQ}}{R} = -\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{j}_1, \qquad \mathbf{r}_1^Q = \ell\,\mathbf{j}_1 + R\,\mathbf{e}_r = -R\sin\phi\,\mathbf{i}_1 + \left(\ell + R\cos\phi\right)\mathbf{j}_1 $$

**Relation with the standard polar angle.** The usual polar angle $\psi$ about $D$ is measured from $\mathbf{i}_1$, with $\mathbf{e}_r = \cos\psi\,\mathbf{i}_1 + \sin\psi\,\mathbf{j}_1$. Matching requires $\cos\psi = -\sin\phi$ and $\sin\psi = \cos\phi$, which holds for $\psi = \phi + \frac{\pi}{2}$:

$$ \cos\left(\phi + \tfrac{\pi}{2}\right) = \cos\phi\cos\tfrac{\pi}{2} - \sin\phi\sin\tfrac{\pi}{2} = -\sin\phi, \qquad \sin\left(\phi + \tfrac{\pi}{2}\right) = \sin\phi\cos\tfrac{\pi}{2} + \cos\phi\sin\tfrac{\pi}{2} = \cos\phi $$

(with $\cos\frac{\pi}{2} = 0$, $\sin\frac{\pi}{2} = 1$). So $\phi$ is the polar angle measured from $\mathbf{j}_1$, the direction $O \to D$; $\phi = 0$ is the point of the ring farthest from the axis and $\phi = \pi$ the nearest.

**Ring basis.** Differentiating $\mathbf{e}_r$ with respect to $\phi$ ($\frac{d}{d\phi}(-\sin\phi) = -\cos\phi$, $\frac{d}{d\phi}\cos\phi = -\sin\phi$) gives a vector of length $\sqrt{\cos^2\phi + \sin^2\phi} = 1$ tangent to the ring, pointing in the sense of increasing $\phi$:

$$ \mathbf{e}_\phi = \frac{d\mathbf{e}_r}{d\phi} = -\cos\phi\,\mathbf{i}_1 - \sin\phi\,\mathbf{j}_1, \qquad \mathbf{k}_1 $$

Check: $\mathbf{e}_r\times\mathbf{e}_\phi = \left[(-\sin\phi)(-\sin\phi) - (\cos\phi)(-\cos\phi)\right]\mathbf{k}_1 = \mathbf{k}_1$, so $\{\mathbf{e}_r, \mathbf{e}_\phi, \mathbf{k}_1\}$ is right-handed and orthonormal ($\mathbf{e}_r\cdot\mathbf{e}_\phi = \sin\phi\cos\phi - \cos\phi\sin\phi = 0$). The inverse relations used below are $\mathbf{j}_1 = \cos\phi\,\mathbf{e}_r - \sin\phi\,\mathbf{e}_\phi$ and $\mathbf{i}_1 = -\sin\phi\,\mathbf{e}_r - \cos\phi\,\mathbf{e}_\phi$.

**Position of $P$.** $P$ is on the axis at height $\zeta$: $\mathbf{r}_1^P = \zeta\,\mathbf{k}_1$. The spring vector is then

$$ \mathbf{r}^Q - \mathbf{r}^P = \ell\,\mathbf{j}_1 + R\,\mathbf{e}_r - \zeta\,\mathbf{k}_1 = -R\sin\phi\,\mathbf{i}_1 + \left(\ell + R\cos\phi\right)\mathbf{j}_1 - \zeta\,\mathbf{k}_1 $$

### Kinematics

##### (b) Relative kinematics of $P$ and $Q$ in $S_1$
* **Pedagogical Justification:** $O$ is the origin of $S_1$, so $\mathbf{r}_1 = \overrightarrow{OP}$ or $\overrightarrow{OQ}$ (Notes Eq. 3.16). The vectors $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ are constant in $S_1$; $\mathbf{e}_r$ and $\mathbf{e}_\phi$ change only through $\phi(t)$, so the chain rule gives $\left.\dfrac{d\mathbf{e}_r}{dt}\right|_1 = \dfrac{d\mathbf{e}_r}{d\phi}\dot\phi = \dot\phi\,\mathbf{e}_\phi$ and $\left.\dfrac{d\mathbf{e}_\phi}{dt}\right|_1 = \dfrac{d\mathbf{e}_\phi}{d\phi}\dot\phi = \dot\phi\left(\sin\phi\,\mathbf{i}_1 - \cos\phi\,\mathbf{j}_1\right) = -\dot\phi\,\mathbf{e}_r$.

**Particle $P$:**

$$ \mathbf{r}_1^P = \zeta\,\mathbf{k}_1, \qquad \mathbf{v}_1^P = \dot\zeta\,\mathbf{k}_1, \qquad \mathbf{a}_1^P = \ddot\zeta\,\mathbf{k}_1 $$

**Particle $Q$:** with $\overrightarrow{OD} = \ell\,\mathbf{j}_1$ constant in $S_1$,

$$ \mathbf{r}_1^Q = \ell\,\mathbf{j}_1 + R\,\mathbf{e}_r = -R\sin\phi\,\mathbf{i}_1 + \left(\ell + R\cos\phi\right)\mathbf{j}_1 $$
$$ \mathbf{v}_1^Q = R\left.\frac{d\mathbf{e}_r}{dt}\right|_1 = R\dot\phi\,\mathbf{e}_\phi = -R\dot\phi\cos\phi\,\mathbf{i}_1 - R\dot\phi\sin\phi\,\mathbf{j}_1 $$

By the product rule, $\mathbf{a}_1^Q = R\ddot\phi\,\mathbf{e}_\phi + R\dot\phi\left.\dfrac{d\mathbf{e}_\phi}{dt}\right|_1$:

$$ \mathbf{a}_1^Q = R\ddot\phi\,\mathbf{e}_\phi - R\dot\phi^2\,\mathbf{e}_r $$

### Forces and Equations of Motion

##### (c) Forces on $P$ and $Q$ (actual and inertia forces in $S_1$)
* **Pedagogical Justification:** in $S_1$ we apply $m\mathbf{a}_1 = \mathbf{F} + \mathbf{F}_i$ (Notes Eq. 4.63) with $\mathbf{F}_i$ from Notes Eq. 4.62. Here $\mathbf{a}_0^O = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$, so only the centrifugal and Coriolis forces survive (Slide 28).

**Spring.** With the spring vector of the change-of-basis section, the spring force on $P$ is $\mathbf{F}_s^P = k\left(\mathbf{r}^Q - \mathbf{r}^P\right)$ and on $Q$ it is $\mathbf{F}_s^Q = -k\left(\mathbf{r}^Q - \mathbf{r}^P\right)$. In the ring basis, using $\mathbf{j}_1 = \cos\phi\,\mathbf{e}_r - \sin\phi\,\mathbf{e}_\phi$:

$$ \mathbf{F}_s^Q = -k\left(\ell\cos\phi + R\right)\mathbf{e}_r + k\ell\sin\phi\,\mathbf{e}_\phi + k\zeta\,\mathbf{k}_1 $$

**Forces on $P$:**

* Weight $-mg\,\mathbf{k}_1$.
* Reaction of the smooth axis, perpendicular to $\mathbf{k}_1$: $\mathbf{N}_P = N_1\,\mathbf{i}_1 + N_2\,\mathbf{j}_1$.
* Spring $\mathbf{F}_s^P = k\left[-R\sin\phi\,\mathbf{i}_1 + \left(\ell + R\cos\phi\right)\mathbf{j}_1 - \zeta\,\mathbf{k}_1\right]$.
* Inertia forces: $P$ is on the rotation axis. $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = \Omega\zeta\,\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$, so $\mathbf{F}_C^P = \mathbf{0}$; $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = \Omega\dot\zeta\,\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$, so $\mathbf{F}_{COR}^P = \mathbf{0}$.

**Forces on $Q$:**

* Weight $-mg\,\mathbf{k}_1$.
* Reaction of the smooth ring, perpendicular to the tangent $\mathbf{e}_\phi$: $\mathbf{N}_Q = N_3\,\mathbf{e}_r + N_4\,\mathbf{k}_1 = N_3\left(-\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{j}_1\right) + N_4\,\mathbf{k}_1$.
* Spring $\mathbf{F}_s^Q$ above.
* Centrifugal force. Since $\mathbf{r}_1^Q$ has no $\mathbf{k}_1$ component, $\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^Q\right) = -\Omega^2\mathbf{r}_1^Q$ (from $\mathbf{k}_1\times(\mathbf{k}_1\times\mathbf{i}_1) = -\mathbf{i}_1$ and $\mathbf{k}_1\times(\mathbf{k}_1\times\mathbf{j}_1) = -\mathbf{j}_1$), hence
$$ \mathbf{F}_C^Q = m\Omega^2\mathbf{r}_1^Q = m\Omega^2\left(\ell\,\mathbf{j}_1 + R\,\mathbf{e}_r\right) = m\Omega^2\left(\ell\cos\phi + R\right)\mathbf{e}_r - m\Omega^2\ell\sin\phi\,\mathbf{e}_\phi $$
* Coriolis force. From $\mathbf{e}_r\times\mathbf{e}_\phi = \mathbf{k}_1$ (cyclic: $\mathbf{e}_\phi\times\mathbf{k}_1 = \mathbf{e}_r$), $\mathbf{k}_1\times\mathbf{e}_\phi = -\mathbf{e}_r$:
$$ \mathbf{F}_{COR}^Q = -2m\Omega\,\mathbf{k}_1\times R\dot\phi\,\mathbf{e}_\phi = 2m\Omega R\dot\phi\,\mathbf{e}_r $$
* Euler force and force due to the origin's acceleration: zero for both particles.

##### (d) Scalar equations of motion in $S_1$
* **Pedagogical Justification:** project $m\mathbf{a}_1 = \mathbf{F} + \mathbf{F}_i$ for each particle on an orthonormal basis adapted to its constraint: $\{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ for $P$ and $\{\mathbf{e}_r, \mathbf{e}_\phi, \mathbf{k}_1\}$ for $Q$. This gives $3 + 3 = 6$ scalar equations for the 6 unknowns $\zeta, \phi, N_1, N_2, N_3, N_4$.

**Particle $P$** ($m\ddot\zeta\,\mathbf{k}_1 = -mg\,\mathbf{k}_1 + N_1\mathbf{i}_1 + N_2\mathbf{j}_1 + \mathbf{F}_s^P$):

$$ \mathbf{i}_1: \quad 0 = N_1 - kR\sin\phi $$
$$ \mathbf{j}_1: \quad 0 = N_2 + k\left(\ell + R\cos\phi\right) $$
$$ \mathbf{k}_1: \quad m\ddot\zeta = -mg - k\zeta $$

**Particle $Q$** ($m\left(R\ddot\phi\,\mathbf{e}_\phi - R\dot\phi^2\mathbf{e}_r\right) = -mg\,\mathbf{k}_1 + N_3\mathbf{e}_r + N_4\mathbf{k}_1 + \mathbf{F}_s^Q + \mathbf{F}_C^Q + \mathbf{F}_{COR}^Q$):

$$ \mathbf{e}_r: \quad -mR\dot\phi^2 = N_3 - k\left(\ell\cos\phi + R\right) + m\Omega^2\left(\ell\cos\phi + R\right) + 2m\Omega R\dot\phi $$
$$ \mathbf{e}_\phi: \quad mR\ddot\phi = k\ell\sin\phi - m\Omega^2\ell\sin\phi $$
$$ \mathbf{k}_1: \quad 0 = -mg + N_4 + k\zeta $$

### Answers and Checks

##### (a) Degrees of freedom and $\mathcal{B}_1$
$\text{DOF} = 2$, coordinates $(\zeta, \phi)$; $\mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0$, $\mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0$, $\mathbf{k}_1 = \mathbf{k}_0$.

##### (b) Kinematics in $S_1$
$\mathbf{r}_1^P = \zeta\,\mathbf{k}_1$, $\mathbf{v}_1^P = \dot\zeta\,\mathbf{k}_1$, $\mathbf{a}_1^P = \ddot\zeta\,\mathbf{k}_1$; $\mathbf{r}_1^Q = \ell\,\mathbf{j}_1 + R\,\mathbf{e}_r$, $\mathbf{v}_1^Q = R\dot\phi\,\mathbf{e}_\phi$, $\mathbf{a}_1^Q = R\ddot\phi\,\mathbf{e}_\phi - R\dot\phi^2\,\mathbf{e}_r$.

##### (c) Forces
As listed in the previous section: weights, reactions $\mathbf{N}_P = N_1\mathbf{i}_1 + N_2\mathbf{j}_1$ and $\mathbf{N}_Q = N_3\mathbf{e}_r + N_4\mathbf{k}_1$, spring forces $\pm k(\mathbf{r}^Q - \mathbf{r}^P)$, and on $Q$ only the centrifugal force $m\Omega^2\mathbf{r}_1^Q$ and the Coriolis force $2m\Omega R\dot\phi\,\mathbf{e}_r$.

##### (d) Scalar equations of motion
The six projections of the previous section.

##### (e) Two equations free of the reactions
* **Pedagogical Justification:** the reactions appear only in the projections perpendicular to the allowed motions; the projections along the allowed motions ($\mathbf{k}_1$ for $P$, $\mathbf{e}_\phi$ for $Q$) are free of them.

Dividing the $\mathbf{k}_1$ equation of $P$ and the $\mathbf{e}_\phi$ equation of $Q$ by $m$ and $mR$:

$$ \boxed{\ddot\zeta + \frac{k}{m}\zeta = -g, \qquad \ddot\phi = \frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)\sin\phi} $$

The other four equations then give the reactions once $\zeta(t)$, $\phi(t)$ are known: $N_1 = kR\sin\phi$, $N_2 = -k\left(\ell + R\cos\phi\right)$, $N_3 = -mR\dot\phi^2 + \left(k - m\Omega^2\right)\left(R + \ell\cos\phi\right) - 2m\Omega R\dot\phi$, $N_4 = mg - k\zeta$. In particular the ring reaction has the form $\mathbf{N}_Q = N_3\left(-\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{j}_1\right) + N_4\,\mathbf{k}_1$ of the official key.

The two equations are **decoupled**: the vertical spring component acts only on $P$'s coordinate, and the horizontal one only on $Q$'s, because the spring force is linear in $\mathbf{r}^Q - \mathbf{r}^P$ and $P$ moves along $\mathbf{k}_1$ while $Q$ moves in the plane $\perp\mathbf{k}_1$.

##### (f) A conservation law in $S_1$
* **Pedagogical Justification:** in $S_1$ the constraints (axis and ring) are fixed and smooth, so the reactions do no work; the Coriolis force on $Q$ is perpendicular to $\mathbf{v}_1^Q$ (Slide 31); the weight and spring are conservative; and with $\boldsymbol{\omega}_{10}$ constant the centrifugal force has potential $-\tfrac12 m\Omega^2 r_\perp^2$ (Slide 30). Hence the mechanical energy of the system in $S_1$ is conserved (Slide 29).

Potential energies in $S_1$: weight of $P$, $mg\zeta$ (weight of $Q$: $mg\cdot 0$); spring $\tfrac12 k\left|\mathbf{r}^Q - \mathbf{r}^P\right|^2$; centrifugal on $Q$, $-\tfrac12 m\Omega^2\left|\mathbf{r}_1^Q\right|^2$ (here $r_\perp^Q = |\mathbf{r}_1^Q|$). With

$$ \left|\mathbf{r}^Q - \mathbf{r}^P\right|^2 = R^2\sin^2\phi + \left(\ell + R\cos\phi\right)^2 + \zeta^2 = \ell^2 + R^2 + 2\ell R\cos\phi + \zeta^2, \qquad \left|\mathbf{r}_1^Q\right|^2 = \ell^2 + R^2 + 2\ell R\cos\phi $$

and dropping the constant $\tfrac12\left(k - m\Omega^2\right)\left(\ell^2 + R^2\right)$:

$$ \boxed{E_1 = \frac12 m\left(\dot\zeta^2 + R^2\dot\phi^2\right) + mg\zeta + \frac12 k\zeta^2 + \left(k - m\Omega^2\right)\ell R\cos\phi = \text{const}} $$

**Check with the equations of part (e)** (chain rule $\frac{d}{dt}\cos\phi = -\dot\phi\sin\phi$, $\frac{d}{dt}\zeta^2 = 2\zeta\dot\zeta$):

$$ \frac{dE_1}{dt} = m\dot\zeta\ddot\zeta + mR^2\dot\phi\ddot\phi + mg\dot\zeta + k\zeta\dot\zeta - \left(k - m\Omega^2\right)\ell R\dot\phi\sin\phi = m\dot\zeta\left(\ddot\zeta + g + \frac{k}{m}\zeta\right) + mR\dot\phi\left(R\ddot\phi - \left(\frac{k}{m} - \Omega^2\right)\ell\sin\phi\right) = 0 $$

Because the equations are decoupled, each bracket vanishes separately, so in fact two first integrals exist: $\tfrac12 m\dot\zeta^2 + mg\zeta + \tfrac12 k\zeta^2 = \text{const}$ and $\tfrac12 mR^2\dot\phi^2 + \left(k - m\Omega^2\right)\ell R\cos\phi = \text{const}$. The constants are fixed by initial conditions, which the statement does not give.

##### Checks
* **Particle $P$:** $\ddot\zeta + (k/m)\zeta = -g$ is a harmonic oscillator about $\zeta_{eq} = -mg/k$ with angular frequency $\sqrt{k/m}$, unaffected by the rotation (it lies on the axis, where centrifugal and Coriolis forces vanish).
* **Particle $Q$:** $\ddot\phi = \tfrac{\ell}{R}\left(\tfrac{k}{m} - \Omega^2\right)\sin\phi$ is a pendulum equation. The spring pulls $Q$ towards the axis (towards $\phi = \pi$, the point of the ring nearest $O$) and the centrifugal force pushes it outward (towards $\phi = 0$). If $\Omega^2 \lt k/m$ the stable position is $\phi = \pi$; if $\Omega^2 \gt k/m$ it is $\phi = 0$; at $\Omega^2 = k/m$ the two effects cancel exactly and $\dot\phi$ is constant. The Coriolis force only loads the ring radially ($N_3$).
* **Limits:** $\Omega \to 0$ gives a fixed ring and $\ddot\phi = \tfrac{k\ell}{mR}\sin\phi$; $\ell \to 0$ (ring centred on the axis) gives $\ddot\phi = 0$, uniform motion, since every point of the ring is then equidistant from the axis. Geometry: $\phi = 0$ gives $\mathbf{r}_1^Q = (\ell + R)\,\mathbf{j}_1$, the far point of the ring, and $\phi = \pi$ gives $(\ell - R)\,\mathbf{j}_1$.
* **Dimensions:** $[k/m] = \text{N}/(\text{m}\,\text{kg}) = \text{s}^{-2}$, so $[(k/m)\zeta] = \text{m/s}^2 = [g] = [\ddot\zeta]$; $[(\ell/R)(k/m - \Omega^2)] = \text{s}^{-2} = [\ddot\phi]$; $[N_3]$: $[mR\dot\phi^2] = [kR] = [m\Omega R\dot\phi] = \text{N}$; $[E_1] = \text{kg}\,\text{m}^2/\text{s}^2 = [k\zeta^2] = [k\ell R] = \text{J}$.
* **Symbolic check (sympy):** $\mathbf{a}_0$ of both particles obtained by differentiating $[{}_0R_1]\,\mathbf{r}_1$ twice matches Notes Eq. 3.27; the six scalar equations, the four reactions, and $dE_1/dt = 0$ along the motion are confirmed.
* **Check against the official key** (Problems.pdf, p. 76): "One of the forces acting on $Q$ is the reaction of the ring, $\mathbf{N}_Q = N_3(-\sin\phi\,\mathbf{i}_1 + \cos\phi\,\mathbf{j}_1) + N_4\,\mathbf{k}_1$", which matches part (c).

---

## Problem 41: Satellite Solar Panel (Composition of Rotations)

### Reference Frames, Bases and Coordinates
* **Physical system:** a satellite body spins about its $z$ axis at constant rate $\omega$; a solar panel turns about the body-fixed $x$ axis through the prescribed angle $\theta(t)$. Point $B$ is a corner of the panel.
* **Why relative motion.** The motion of $B$ is the superposition of two simple motions: in the body frame $S_1$, $B$ just describes a circle of radius $W$ about the $x$ axis; and $S_1$ itself just spins about $z$. Notes Eqs. 3.26–3.27 combine the two without writing the inertial position explicitly. A second route uses the panel frame $S_2$, in which $B$ is fixed, and the composition of angular velocities (Notes Eqs. 3.13–3.15).
* **Hypotheses:**
  1. The frame centred at $A$ with non-rotating axes is inertial, so the centre $A$ of the satellite is fixed: $\mathbf{v}_0^A = \mathbf{a}_0^A = \mathbf{0}$.
  2. Body and panel are rigid; $\omega$ is constant; $\theta(t)$ is an arbitrary (known) function.
  3. **Geometry (read from the figure):** $B$ is at distance $H$ from $A$ measured along $x$, and at distance $W$ from the $x$ axis; $\theta$ is measured about $+x$ from the body axis $y$, so for $\theta = 0$ the segment from the hinge axis to $B$ points along $+y$.
* **Inertial frame:** $S_0 = \{A; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, basis $\mathcal{B}_0$.
* **Body frame:** $S_1 = \{A; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$ (the axes $x$, $y$, $z$ of the figure), basis $\mathcal{B}_1$, turning with the satellite about $\mathbf{k}_0 = \mathbf{k}_1$. It coincides with $S_0$ at $t = 0$.
* **Panel frame:** $S_2 = \{C; \mathbf{i}_2, \mathbf{j}_2, \mathbf{k}_2\}$, basis $\mathcal{B}_2$, attached to the panel, where $C = A + H\,\mathbf{i}_1$ is the point of the hinge axis at the abscissa of $B$; $\mathbf{i}_2 = \mathbf{i}_1$ is the hinge axis and $\mathbf{j}_2$ points from $C$ to $B$.
* **Degrees of freedom:** none to determine; the motion is prescribed by $\omega t$ and $\theta(t)$ (kinematics only).

| Symbol | Meaning | SI unit |
|---|---|---|
| $H$ | axial distance from $A$ to $B$ (along $x$) | m |
| $W$ | distance from $B$ to the hinge axis $x$ | m |
| $\omega$ | constant spin rate of the satellite about $z$ | rad/s |
| $\theta(t)$ | panel angle about $x$ | rad |

### Change of Basis and Position Vector

#### First rotation: the body frame $S_1$ about $\mathbf{k}_0$

![[attachments/EM-SOL/p41-spin-view.svg]]

The spin is about $\mathbf{k}_0$, so we look down that axis, from $+z$: $\mathbf{k}_0 = \mathbf{k}_1$ points out of the paper ($\odot$). With $\mathbf{i}_0$ to the right, the right-hand rule fixes $\mathbf{j}_0$: $\mathbf{i}_0\times\mathbf{j}_0 = \mathbf{k}_0$ means that the fingers turning from $\mathbf{i}_0$ to $\mathbf{j}_0$ must curl counter-clockwise for the thumb to point at the reader, so $\mathbf{j}_0$ points up the page. A positive spin $\omega\,\mathbf{k}_0$ turns the body counter-clockwise in this view, and after a time $t$ the body axes have turned the angle $\omega t$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the shaded right triangle. The leg adjacent to $\omega t$ lies along $\mathbf{i}_0$ and measures $\cos\omega t$; the leg opposite to $\omega t$ lies along $+\mathbf{j}_0$ and measures $\sin\omega t$. So $\mathbf{i}_1 = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ (up) and turns the same angle counter-clockwise, which moves its tip to the left, to the side of $-\mathbf{i}_0$. Its leg along $\mathbf{j}_0$ (adjacent) is $\cos\omega t$ and its leg along $\mathbf{i}_0$ (opposite) is $\sin\omega t$ pointing to $-\mathbf{i}_0$: $\mathbf{j}_1 = -\sin\omega t\,\mathbf{i}_0 + \cos\omega t\,\mathbf{j}_0$. **The minus sign comes from the tip of $\mathbf{j}_1$ moving towards $-\mathbf{i}_0$.**
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

The columns of the matrix are the components of $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in $\mathcal{B}_0$:

$$ [{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1\cdot\left(\cos\omega t\cos\omega t - (-\sin\omega t)\sin\omega t\right) = \cos^2\omega t + \sin^2\omega t = 1 $$

(expansion along the third row). The columns have unit norm, $\cos^2\omega t + \sin^2\omega t = 1$, and the first two are orthogonal, $\cos\omega t\,(-\sin\omega t) + \sin\omega t\cos\omega t = 0$, so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$.** $\boldsymbol{\omega}_{10} = \omega\,\mathbf{k}_1$ and, $\omega$ and $\mathbf{k}_1 = \mathbf{k}_0$ being constant, $\boldsymbol{\alpha}_{10} = \mathbf{0}$. Check with Poisson's formula: by the chain rule, $\left.\frac{d\mathbf{i}_1}{dt}\right|_0 = -\omega\sin\omega t\,\mathbf{i}_0 + \omega\cos\omega t\,\mathbf{j}_0 = \omega\,\mathbf{j}_1$, and indeed $\boldsymbol{\omega}_{10}\times\mathbf{i}_1 = \omega\,\mathbf{k}_1\times\mathbf{i}_1 = \omega\,\mathbf{j}_1$.

#### Second rotation: the panel frame $S_2$ about the hinge $\mathbf{i}_1$

![[attachments/EM-SOL/p41-hinge-view.svg]]

The panel turns about the hinge axis $\mathbf{i}_1 = \mathbf{i}_2$, so we look along that axis with $\mathbf{i}_1$ out of the paper ($\odot$). With $\mathbf{j}_1$ to the right, $\mathbf{k}_1 = \mathbf{i}_1\times\mathbf{j}_1$: the fingers go from $\mathbf{i}_1$ (towards the reader) to $\mathbf{j}_1$ (right) and the thumb points up the page, so $\mathbf{k}_1$ points up. The angle $\theta$ is measured about $+\mathbf{i}_1$, which is counter-clockwise in this view, from $\mathbf{j}_1$:

* $\mathbf{j}_2$ has the leg $\cos\theta$ along $\mathbf{j}_1$ (adjacent) and the leg $\sin\theta$ along $+\mathbf{k}_1$ (opposite): $\mathbf{j}_2 = \cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1$.
* $\mathbf{k}_2$ starts on $\mathbf{k}_1$ and its tip moves to the side of $-\mathbf{j}_1$: $\mathbf{k}_2 = -\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1$.
* $\mathbf{i}_2 = \mathbf{i}_1$.

$$ [{}_1R_2] = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}, \qquad \det[{}_1R_2] = 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1, \qquad \boldsymbol{\omega}_{21} = \dot{\theta}\,\mathbf{i}_1 $$

The columns are orthonormal (norms $\cos^2\theta + \sin^2\theta = 1$, scalar product of the last two $-\cos\theta\sin\theta + \sin\theta\cos\theta = 0$), so $[{}_1R_2][{}_1R_2]^T = I$; hence $[{}_0R_2] = [{}_0R_1][{}_1R_2]$ is also a proper rotation, with $\det[{}_0R_2] = 1\cdot 1 = 1$ (Notes Eq. 1.16).

#### Position vector of $B$

To go from $A$ to $B$ we pass through the hinge point $C$, because the distance from the hinge axis is the one that stays constant:

$$ \mathbf{r}_1^B = \overrightarrow{AC} + \overrightarrow{CB} $$

* $\overrightarrow{AC} = H\,\mathbf{i}_1$: $C$ is on the hinge axis, at the abscissa $H$ of $B$.
* $\overrightarrow{CB} = W\,\mathbf{j}_2$ is fixed in $S_2$. In the shaded triangle of the hinge view the hypotenuse is $|CB| = W$, the leg adjacent to $\theta$ is $W\cos\theta$ along $\mathbf{j}_1$ and the leg opposite to $\theta$ is $W\sin\theta$ along $\mathbf{k}_1$; this is the second column of $[{}_1R_2]$ times $W$.

$$ \mathbf{r}_1^B = H\,\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1 $$

Checks: $\theta = 0$ gives $H\,\mathbf{i}_1 + W\,\mathbf{j}_1$ (panel along $+y$, as in the reading of the figure); $\theta = \pi/2$ gives $H\,\mathbf{i}_1 + W\,\mathbf{k}_1$ (panel turned up, along $+z$).

![[attachments/EM-SOL/p41-body-plane.svg]]

**Distance to the spin axis.** The spin is about $\mathbf{k}_1$, so the part of $\mathbf{r}_1^B$ that matters for the rotation is the one perpendicular to $\mathbf{k}_1$: dropping the component $W\sin\theta\,\mathbf{k}_1$ (the height of $B$ above the body plane), $\mathbf{r}_\perp = H\,\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1$, the vector from the axis to the projection $B'$ in the figure above. It reappears in the centripetal term.

### Kinematics

##### 1. Relative motion of $B$ in the body frame $S_1$
* **Pedagogical Justification:** the body frame rotates at constant rate with fixed origin, so Notes Eq. 3.27 keeps only three terms; the relative quantities are derivatives in $S_1$, where $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ are constant.

Only the components of $\mathbf{r}_1^B$ change. By the chain rule, $\frac{d}{dt}(W\cos\theta) = -W\sin\theta\,\dot{\theta}$ and $\frac{d}{dt}(W\sin\theta) = W\cos\theta\,\dot{\theta}$ ($H$ is constant):

$$ \mathbf{v}_1^B = \left.\frac{d\mathbf{r}_1^B}{dt}\right|_1 = -W\dot{\theta}\sin\theta\,\mathbf{j}_1 + W\dot{\theta}\cos\theta\,\mathbf{k}_1 $$

Differentiating again with the product rule, $\frac{d}{dt}(\dot{\theta}\sin\theta) = \ddot{\theta}\sin\theta + \dot{\theta}\,\dot{\theta}\cos\theta$ and $\frac{d}{dt}(\dot{\theta}\cos\theta) = \ddot{\theta}\cos\theta - \dot{\theta}\,\dot{\theta}\sin\theta$:

$$ \mathbf{a}_1^B = \left.\frac{d\mathbf{v}_1^B}{dt}\right|_1 = -W\left(\ddot{\theta}\sin\theta + \dot{\theta}^2\cos\theta\right)\mathbf{j}_1 + W\left(\ddot{\theta}\cos\theta - \dot{\theta}^2\sin\theta\right)\mathbf{k}_1 $$

(circular motion of radius $W$ about the $x$ axis: tangential part $W\ddot{\theta}\,\mathbf{k}_2$ and normal part $-W\dot{\theta}^2\,\mathbf{j}_2$).

##### 2. Absolute velocity of $B$
* **Pedagogical Justification:** Notes Eq. 3.26 (Slide 24), $\mathbf{v}_0^B = \mathbf{v}_0^A + \mathbf{v}_1^B + \boldsymbol{\omega}_{10}\times\mathbf{r}_1^B$, with $\mathbf{v}_0^A = \mathbf{0}$.

Cross products: $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$, $\mathbf{k}_1\times\mathbf{k}_1 = \mathbf{0}$:

$$ \boldsymbol{\omega}_{10}\times\mathbf{r}_1^B = \omega\mathbf{k}_1\times\left(H\,\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1\right) = H\omega\,\mathbf{j}_1 - W\omega\cos\theta\,\mathbf{i}_1 $$

(only $\mathbf{r}_\perp$ contributes). Adding $\mathbf{v}_1^B$ component by component:

$$ \boxed{\mathbf{v}_0^B = -W\omega\cos\theta\,\mathbf{i}_1 + \left(H\omega - W\dot{\theta}\sin\theta\right)\mathbf{j}_1 + W\dot{\theta}\cos\theta\,\mathbf{k}_1} $$

The components are given in the body basis $\mathcal{B}_1$; in $\mathcal{B}_0$ they follow from $\{\mathbf{v}_0^B\}_0 = [{}_0R_1]\{\mathbf{v}_0^B\}_1$.

##### 3. Absolute acceleration of $B$
* **Pedagogical Justification:** Notes Eq. 3.27 (Slide 25) with $\mathbf{a}_0^A = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$: $\mathbf{a}_0^B = \mathbf{a}_1^B + \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^B\right) + 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^B$.

**Centripetal term** (reusing $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^B$ from step 2):

$$ \boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^B\right) = \omega\mathbf{k}_1\times\left(-W\omega\cos\theta\,\mathbf{i}_1 + H\omega\,\mathbf{j}_1\right) = -W\omega^2\cos\theta\,\mathbf{j}_1 - H\omega^2\,\mathbf{i}_1 $$

i.e. $-\omega^2\mathbf{r}_\perp$ with $\mathbf{r}_\perp = H\,\mathbf{i}_1 + W\cos\theta\,\mathbf{j}_1$, the vector of the body-plane figure.

**Coriolis term:**

$$ 2\boldsymbol{\omega}_{10}\times\mathbf{v}_1^B = 2\omega\mathbf{k}_1\times\left(-W\dot{\theta}\sin\theta\,\mathbf{j}_1 + W\dot{\theta}\cos\theta\,\mathbf{k}_1\right) = -2W\omega\dot{\theta}\sin\theta\,(\mathbf{k}_1\times\mathbf{j}_1) = 2W\omega\dot{\theta}\sin\theta\,\mathbf{i}_1 $$

**Sum**, collecting the $\mathbf{i}_1$, $\mathbf{j}_1$ and $\mathbf{k}_1$ components of $\mathbf{a}_1^B$, the centripetal term and the Coriolis term:

$$ \boxed{\mathbf{a}_0^B = \left(2W\omega\dot{\theta}\sin\theta - H\omega^2\right)\mathbf{i}_1 - \left(W\ddot{\theta}\sin\theta + W\dot{\theta}^2\cos\theta + W\omega^2\cos\theta\right)\mathbf{j}_1 + \left(W\ddot{\theta}\cos\theta - W\dot{\theta}^2\sin\theta\right)\mathbf{k}_1} $$

##### 4. Second route: panel frame and composition of angular velocities
* **Pedagogical Justification:** $B$ is fixed in $S_2$, so $\mathbf{v}_2^B = \mathbf{a}_2^B = \mathbf{0}$ and Notes Eqs. 3.26–3.27 applied to $S_2$ (origin $C$) need only $\boldsymbol{\omega}_{20}$, $\boldsymbol{\alpha}_{20}$ and the motion of $C$. Angular velocities add (Notes Eqs. 3.13–3.15, Slide 19); angular accelerations do not simply add.
$$ \boldsymbol{\omega}_{20} = \boldsymbol{\omega}_{21} + \boldsymbol{\omega}_{10} = \dot{\theta}\,\mathbf{i}_1 + \omega\,\mathbf{k}_1 $$

Its derivative in $S_0$ by the Coriolis theorem (Notes Eq. 3.8), with $\left.\frac{d}{dt}\right|_1\left(\dot{\theta}\,\mathbf{i}_1 + \omega\,\mathbf{k}_1\right) = \ddot{\theta}\,\mathbf{i}_1$ ($\omega$ constant):

$$ \boldsymbol{\alpha}_{20} = \left.\frac{d\boldsymbol{\omega}_{20}}{dt}\right|_1 + \boldsymbol{\omega}_{10}\times\boldsymbol{\omega}_{20} = \ddot{\theta}\,\mathbf{i}_1 + \omega\mathbf{k}_1\times\dot{\theta}\,\mathbf{i}_1 = \ddot{\theta}\,\mathbf{i}_1 + \omega\dot{\theta}\,\mathbf{j}_1 $$

Motion of $C$ (fixed in $S_1$ at $H\mathbf{i}_1$): $\mathbf{v}_0^C = \omega\mathbf{k}_1\times H\mathbf{i}_1 = H\omega\,\mathbf{j}_1$, $\mathbf{a}_0^C = \omega\mathbf{k}_1\times H\omega\,\mathbf{j}_1 = -H\omega^2\,\mathbf{i}_1$. With $\mathbf{r}_2^B = \overrightarrow{CB} = W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1$:

$$ \boldsymbol{\omega}_{20}\times\mathbf{r}_2^B = \dot{\theta}W\cos\theta\,\mathbf{k}_1 - \dot{\theta}W\sin\theta\,\mathbf{j}_1 - \omega W\cos\theta\,\mathbf{i}_1 $$

so $\mathbf{v}_0^B = \mathbf{v}_0^C + \boldsymbol{\omega}_{20}\times\mathbf{r}_2^B$ reproduces the boxed velocity. For the acceleration, $\mathbf{a}_0^B = \mathbf{a}_0^C + \boldsymbol{\alpha}_{20}\times\mathbf{r}_2^B + \boldsymbol{\omega}_{20}\times(\boldsymbol{\omega}_{20}\times\mathbf{r}_2^B)$:

$$ \boldsymbol{\alpha}_{20}\times\mathbf{r}_2^B = \left(\ddot{\theta}\,\mathbf{i}_1 + \omega\dot{\theta}\,\mathbf{j}_1\right)\times\left(W\cos\theta\,\mathbf{j}_1 + W\sin\theta\,\mathbf{k}_1\right) = W\ddot{\theta}\cos\theta\,\mathbf{k}_1 - W\ddot{\theta}\sin\theta\,\mathbf{j}_1 + W\omega\dot{\theta}\sin\theta\,\mathbf{i}_1 $$
$$ \boldsymbol{\omega}_{20}\times\left(\boldsymbol{\omega}_{20}\times\mathbf{r}_2^B\right) = \left(\dot{\theta}\,\mathbf{i}_1 + \omega\,\mathbf{k}_1\right)\times\left(-\omega W\cos\theta\,\mathbf{i}_1 - \dot{\theta}W\sin\theta\,\mathbf{j}_1 + \dot{\theta}W\cos\theta\,\mathbf{k}_1\right) $$
$$ = -\dot{\theta}^2W\sin\theta\,\mathbf{k}_1 - \dot{\theta}^2W\cos\theta\,\mathbf{j}_1 - \omega^2W\cos\theta\,\mathbf{j}_1 + \omega\dot{\theta}W\sin\theta\,\mathbf{i}_1 $$

(using $\mathbf{i}_1\times\mathbf{j}_1 = \mathbf{k}_1$, $\mathbf{i}_1\times\mathbf{k}_1 = -\mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{i}_1 = \mathbf{j}_1$, $\mathbf{k}_1\times\mathbf{j}_1 = -\mathbf{i}_1$). Adding $\mathbf{a}_0^C = -H\omega^2\,\mathbf{i}_1$: the $\mathbf{i}_1$ component is $2W\omega\dot{\theta}\sin\theta - H\omega^2$, the $\mathbf{j}_1$ component $-W(\ddot{\theta}\sin\theta + \dot{\theta}^2\cos\theta + \omega^2\cos\theta)$, the $\mathbf{k}_1$ component $W(\ddot{\theta}\cos\theta - \dot{\theta}^2\sin\theta)$: the same boxed result. Note that the Coriolis term of route 1, $2W\omega\dot{\theta}\sin\theta\,\mathbf{i}_1$, appears in route 2 split in two equal halves, one from $\boldsymbol{\alpha}_{20}$ (the term $\omega\dot{\theta}\,\mathbf{j}_1$ that makes angular accelerations not add) and one from the double cross product.

### Answers and Checks

##### Absolute velocity and acceleration of $B$
Both routes give, in the body basis $\mathcal{B}_1$ (to be multiplied by $[{}_0R_1]$ for the components in $\mathcal{B}_0$):

$$ \mathbf{v}_0^B = -W\omega\cos\theta\,\mathbf{i}_1 + \left(H\omega - W\dot{\theta}\sin\theta\right)\mathbf{j}_1 + W\dot{\theta}\cos\theta\,\mathbf{k}_1 $$
$$ \mathbf{a}_0^B = \left(2W\omega\dot{\theta}\sin\theta - H\omega^2\right)\mathbf{i}_1 - \left(W\ddot{\theta}\sin\theta + W\dot{\theta}^2\cos\theta + W\omega^2\cos\theta\right)\mathbf{j}_1 + \left(W\ddot{\theta}\cos\theta - W\dot{\theta}^2\sin\theta\right)\mathbf{k}_1 $$

No forces or masses are given, so the problem has no dynamics to write.

##### Checks
* **Reading of the terms.** $-H\omega^2\mathbf{i}_1 - W\omega^2\cos\theta\,\mathbf{j}_1 = -\omega^2\mathbf{r}_\perp$ is the centripetal acceleration of the spin; the $W\ddot{\theta}$ and $W\dot{\theta}^2$ terms are the tangential and normal accelerations of the panel rotation; $2W\omega\dot{\theta}\sin\theta\,\mathbf{i}_1$ is the Coriolis coupling of the two rotations, present only when the panel moves ($\dot{\theta} \neq 0$) with a velocity component normal to the spin axis.
* **Limits:** $\dot{\theta} = 0$ (panel locked) gives the rigid-body motion $\mathbf{v}_0^B = \boldsymbol{\omega}_{10}\times\mathbf{r}_1^B$, $\mathbf{a}_0^B = -\omega^2\mathbf{r}_\perp$; $\omega = 0$ (no spin) leaves the circular motion of radius $W$ about the hinge.
* **Orthogonality:** $\mathbf{j}_2\cdot\mathbf{k}_2 = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0$ and $\mathbf{i}_1\cdot\mathbf{j}_1 = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0$.
* **Dimensions:** every velocity component is of the form $[W\omega] = [H\omega] = [W\dot{\theta}] = \text{m}\,\text{s}^{-1}$; every acceleration component $[W\omega\dot{\theta}] = [H\omega^2] = [W\ddot{\theta}] = [W\dot{\theta}^2] = \text{m}\,\text{s}^{-2}$.
* **Verification (sympy):** $[{}_0R_1]$, $[{}_1R_2]$, $[{}_0R_2]$ are proper rotations; the inertial first and second derivatives of $[{}_0R_1]\{\mathbf{r}_1^B\}$ equal the Notes Eq. 3.26 and 3.27 expressions; both routes give exactly the official key.
* **Check against the official key:** the key of `Problems.pdf` (p. 76) for Problem 41 (absolute velocity and acceleration of $B$) is reproduced exactly by both routes, as the sympy verification above records; no discrepancy.

---

## Problem 47: Two Repelling Particles on Concentric Wires in a Rotating Plane

### Reference Frames, Bases and Coordinates
* **Physical system:** two heavy particles of mass $m$; $P$ on a circular wire of radius $a$ and $Q$ on a concentric circular wire of radius $2a$, both centred at $O$ and lying in the plane $Ox_1y_1$. The plane spins about the vertical axis $Oy_1 \equiv Oy_0$ with constant rate $\Omega$. The particles repel each other with a force $k$ times their distance.
* **Hypotheses:**
  1. $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ is inertial; $\mathbf{j}_0$ is vertical upward and gravity is $-g\,\mathbf{j}_0$ (the figure draws $\mathbf{g}$ antiparallel to $y_1$).
  2. Smooth, bilateral wires: each reaction is perpendicular to the tangent of its wire.
  3. The repulsion acts along the line $PQ$: on $P$ it is $k\left(\mathbf{r}^P - \mathbf{r}^Q\right)$, on $Q$ it is $k\left(\mathbf{r}^Q - \mathbf{r}^P\right)$ (action and reaction).
  4. $\varphi$ and $\theta$ are measured from $Ox_1$ in the positive sense about $\mathbf{k}_1$, as in the figure. The sense of $\Omega$ only affects the sign of the Coriolis terms; we take $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{j}_0$ with $\Omega$ a signed constant.
* **Why $S_1$:** both wires are fixed in $S_1$, so each particle has a single angular coordinate there. The inertia forces (Notes Eq. 4.62) are the price, and with $\boldsymbol{\omega}_{10}$ constant and $O$ fixed only the centrifugal and Coriolis forces appear.
* **Frames:** $S_0 = \{O; \mathcal{B}_0\}$ (inertial) and $S_1 = \{O; \mathcal{B}_1\}$, $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, attached to the plane of the wires, with common origin; $\mathbf{j}_1 = \mathbf{j}_0$ is the axis of rotation and $S_1 \equiv S_0$ at $t = 0$.
* **Polar bases:** $\{\mathbf{e}_r^P, \mathbf{e}_\varphi, \mathbf{k}_1\}$ at $P$ and $\{\mathbf{e}_r^Q, \mathbf{e}_\theta, \mathbf{k}_1\}$ at $Q$, deduced in the next section.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of each particle | kg |
| $a$ | radius of the inner wire (outer: $2a$) | m |
| $k$ | repulsion constant | N/m |
| $\Omega$ | constant rotation rate of the plane | rad/s |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\varphi$, $\theta$ | angular positions of $P$ and $Q$ from $Ox_1$ | rad |
| $\alpha = ka/(mg)$, $\beta = a\Omega^2/g$ | dimensionless parameters | 1 |

##### (a) Configuration degrees of freedom
* **Pedagogical Justification:** each particle on a wire (a curve) loses 2 of its 3 coordinates.

$P$: 3 coordinates minus 2 constraints ($z_1 = 0$, $x_1^2 + y_1^2 = a^2$) = 1. $Q$: 3 minus 2 ($z_1 = 0$, $x_1^2 + y_1^2 = 4a^2$) = 1. The motion of the plane is prescribed. Hence

$$ \text{DOF} = 2, \qquad \text{coordinates } (\varphi, \theta) $$

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p47-top-view.svg]]

The plane turns about $\mathbf{j}_0$, so we look down that axis, from $+y_0$: $\mathbf{j}_0 = \mathbf{j}_1$ points out of the paper ($\odot$). With $\mathbf{i}_0$ to the right, the right-hand rule gives $\mathbf{k}_0 = \mathbf{i}_0\times\mathbf{j}_0$: the fingers turn from $\mathbf{i}_0$ (right) to $\mathbf{j}_0$ (towards the reader) and the thumb points down the page. So in this view $\mathbf{k}_0$ points down and $-\mathbf{k}_0$ up. For $\Omega \gt 0$ the plane turns counter-clockwise (thumb along $\mathbf{j}_0$, towards the reader), and after a time $t$ the axis $\mathbf{i}_1$ has turned $\Omega t$ from $\mathbf{i}_0$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the shaded right triangle: the leg adjacent to $\Omega t$ is $\cos\Omega t$ along $\mathbf{i}_0$; the leg opposite to $\Omega t$ is $\sin\Omega t$ and points up the page, the direction $-\mathbf{k}_0$. Hence $\mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 - \sin\Omega t\,\mathbf{k}_0$. **The minus sign comes from $\mathbf{k}_0$ pointing down the page in this view.**
* $\mathbf{k}_1$ starts on $\mathbf{k}_0$ (down) and turns $\Omega t$ counter-clockwise, which moves its tip towards $+\mathbf{i}_0$: leg $\cos\Omega t$ along $\mathbf{k}_0$ (adjacent) and $+\sin\Omega t$ along $\mathbf{i}_0$ (opposite).
* $\mathbf{j}_1 = \mathbf{j}_0$, the axis of the rotation.

$$ \mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 - \sin\Omega t\,\mathbf{k}_0, \qquad \mathbf{j}_1 = \mathbf{j}_0, \qquad \mathbf{k}_1 = \sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{k}_0 $$
$$ [{}_0R_1] = \begin{pmatrix} \cos\Omega t & 0 & \sin\Omega t \\ 0 & 1 & 0 \\ -\sin\Omega t & 0 & \cos\Omega t \end{pmatrix} $$

**Checks:** $\det[{}_0R_1] = \cos\Omega t\left(\cos\Omega t\right) + \sin\Omega t\left(\sin\Omega t\right) = 1$ (expansion along the second row). Rows: $\cos^2\Omega t + \sin^2\Omega t = 1$, $1$, $\sin^2\Omega t + \cos^2\Omega t = 1$; first and third rows: $-\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0$; so $[{}_0R_1][{}_0R_1]^T = I$. Also $\mathbf{i}_1\times\mathbf{j}_1 = \sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{k}_0 = \mathbf{k}_1$ (right-handed).

**Motion of $S_1$:** $\mathbf{a}_0^O = \mathbf{0}$; $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{j}_1$. Check with Poisson's formula: by the chain rule, $\left.\dfrac{d\mathbf{i}_1}{dt}\right|_0 = -\Omega\sin\Omega t\,\mathbf{i}_0 - \Omega\cos\Omega t\,\mathbf{k}_0 = -\Omega\,\mathbf{k}_1$, and $\Omega\,\mathbf{j}_1\times\mathbf{i}_1 = -\Omega\,\mathbf{k}_1$. Since $\Omega$ and $\mathbf{j}_0$ are constant, $\boldsymbol{\alpha}_{10} = \mathbf{0}$.

#### Position vectors in the plane of the wires

![[attachments/EM-SOL/p47-wire-plane.svg]]

The plane $Ox_1y_1$ is fixed in $S_1$; it is drawn with $\mathbf{i}_1$ to the right, $\mathbf{j}_1$ up (and $\mathbf{k}_1 = \mathbf{i}_1\times\mathbf{j}_1$ out of the paper), at the configuration of part (i).

* $P$ is on the circle of radius $a$ centred at $O$, at the angle $\varphi$ from $Ox_1$. In the shaded right triangle the hypotenuse is $|OP| = a$, the leg adjacent to $\varphi$ is $a\cos\varphi$ along $\mathbf{i}_1$ and the leg opposite to $\varphi$ is $a\sin\varphi$ along $\mathbf{j}_1$: $\mathbf{r}_1^P = a\cos\varphi\,\mathbf{i}_1 + a\sin\varphi\,\mathbf{j}_1$.
* $Q$ is on the circle of radius $2a$ at the angle $\theta$; the same triangle with hypotenuse $2a$ gives $\mathbf{r}_1^Q = 2a\cos\theta\,\mathbf{i}_1 + 2a\sin\theta\,\mathbf{j}_1$. For $\theta \lt 0$ (as drawn) the leg $2a\sin\theta$ is negative: $Q$ is below $Ox_1$.

These angles are the standard polar angles of the plane (measured from $\mathbf{i}_1$, counter-clockwise about $\mathbf{k}_1$), so no change of origin of the angle is needed.

**Polar bases.** The radial unit vector is the position divided by the radius, and the transverse one its derivative with respect to the angle ($\frac{d}{d\varphi}\cos\varphi = -\sin\varphi$, $\frac{d}{d\varphi}\sin\varphi = \cos\varphi$):

$$ \mathbf{e}_r^P = \cos\varphi\,\mathbf{i}_1 + \sin\varphi\,\mathbf{j}_1, \quad \mathbf{e}_\varphi = \frac{d\mathbf{e}_r^P}{d\varphi} = -\sin\varphi\,\mathbf{i}_1 + \cos\varphi\,\mathbf{j}_1; \qquad \mathbf{e}_r^Q = \cos\theta\,\mathbf{i}_1 + \sin\theta\,\mathbf{j}_1, \quad \mathbf{e}_\theta = \frac{d\mathbf{e}_r^Q}{d\theta} = -\sin\theta\,\mathbf{i}_1 + \cos\theta\,\mathbf{j}_1 $$

so $\mathbf{r}_1^P = a\,\mathbf{e}_r^P$ and $\mathbf{r}_1^Q = 2a\,\mathbf{e}_r^Q$. Each triad $\{\mathbf{e}_r, \mathbf{e}_\varphi\ \text{or}\ \mathbf{e}_\theta, \mathbf{k}_1\}$ is orthonormal and right-handed ($\mathbf{e}_r\times\mathbf{e}_\varphi = \cos^2\varphi\,(\mathbf{i}_1\times\mathbf{j}_1) - \sin^2\varphi\,(\mathbf{j}_1\times\mathbf{i}_1) = (\cos^2\varphi + \sin^2\varphi)\,\mathbf{k}_1 = \mathbf{k}_1$). Dot products used below, from the difference formulas $\cos\varphi\cos\theta + \sin\varphi\sin\theta = \cos(\varphi - \theta)$ and $-\sin\varphi\cos\theta + \cos\varphi\sin\theta = \sin(\theta - \varphi)$: $\mathbf{e}_r^Q\cdot\mathbf{e}_r^P = \cos(\varphi - \theta)$, $\mathbf{e}_r^Q\cdot\mathbf{e}_\varphi = \sin(\theta - \varphi)$, $\mathbf{e}_r^P\cdot\mathbf{e}_\theta = \sin(\varphi - \theta)$, $\mathbf{j}_1\cdot\mathbf{e}_\varphi = \cos\varphi$, $\mathbf{j}_1\cdot\mathbf{e}_r^P = \sin\varphi$, $\mathbf{i}_1\cdot\mathbf{e}_\varphi = -\sin\varphi$, $\mathbf{i}_1\cdot\mathbf{e}_r^P = \cos\varphi$ (and the same with $\theta$ for $Q$).

### Kinematics

##### (c) Relative accelerations
* **Pedagogical Justification:** $\mathbf{i}_1, \mathbf{j}_1$ are constant in $S_1$; by the chain rule $\left.\dfrac{d\mathbf{e}_r^P}{dt}\right|_1 = \dfrac{d\mathbf{e}_r^P}{d\varphi}\dot\varphi = \dot\varphi\,\mathbf{e}_\varphi$ and $\left.\dfrac{d\mathbf{e}_\varphi}{dt}\right|_1 = \dot\varphi\left(-\cos\varphi\,\mathbf{i}_1 - \sin\varphi\,\mathbf{j}_1\right) = -\dot\varphi\,\mathbf{e}_r^P$ (same for $\theta$).

Product rule on $a\dot\varphi\,\mathbf{e}_\varphi$: $\frac{d}{dt}(a\dot\varphi) = a\ddot\varphi$ times $\mathbf{e}_\varphi$, plus $a\dot\varphi$ times $\left.\frac{d\mathbf{e}_\varphi}{dt}\right|_1$:

$$ \mathbf{r}_1^P = a\,\mathbf{e}_r^P, \qquad \mathbf{v}_1^P = a\dot\varphi\,\mathbf{e}_\varphi, \qquad \mathbf{a}_1^P = a\ddot\varphi\,\mathbf{e}_\varphi + a\dot\varphi\left(-\dot\varphi\,\mathbf{e}_r^P\right) = a\ddot\varphi\,\mathbf{e}_\varphi - a\dot\varphi^2\,\mathbf{e}_r^P $$
$$ \mathbf{r}_1^Q = 2a\,\mathbf{e}_r^Q, \qquad \mathbf{v}_1^Q = 2a\dot\theta\,\mathbf{e}_\theta, \qquad \mathbf{a}_1^Q = 2a\ddot\theta\,\mathbf{e}_\theta - 2a\dot\theta^2\,\mathbf{e}_r^Q $$

### Forces and Equations of Motion

##### (b) Reaction forces
* **Pedagogical Justification:** a smooth wire cannot push along its tangent, so its reaction lies in the normal plane of the wire, which is spanned by two independent directions; there is one unknown per removed coordinate.

Two components per particle, four in total:

$$ \mathbf{N}^P = N_1\,\mathbf{e}_r^P + N_2\,\mathbf{k}_1, \qquad \mathbf{N}^Q = N_3\,\mathbf{e}_r^Q + N_4\,\mathbf{k}_1 $$

##### (d) Applied forces
* **Pedagogical Justification:** the applied (actual, non-reaction) forces are the weights and the mutual repulsion; their components in each particle's polar basis are what enters the equations.

Weights: $-mg\,\mathbf{j}_1$ on each particle; with $\mathbf{j}_1\cdot\mathbf{e}_r^P = \sin\varphi$ and $\mathbf{j}_1\cdot\mathbf{e}_\varphi = \cos\varphi$, this is $-mg\sin\varphi\,\mathbf{e}_r^P - mg\cos\varphi\,\mathbf{e}_\varphi$ on $P$ and $-mg\sin\theta\,\mathbf{e}_r^Q - mg\cos\theta\,\mathbf{e}_\theta$ on $Q$.

Repulsion, with $\mathbf{r}^P - \mathbf{r}^Q = a\,\mathbf{e}_r^P - 2a\,\mathbf{e}_r^Q = a\left(\cos\varphi - 2\cos\theta\right)\mathbf{i}_1 + a\left(\sin\varphi - 2\sin\theta\right)\mathbf{j}_1$ (the dashed segment $PQ$ of the figure):

$$ \mathbf{F}_k^P = k\left(\mathbf{r}^P - \mathbf{r}^Q\right) = ka\left[1 - 2\cos(\varphi - \theta)\right]\mathbf{e}_r^P + 2ka\sin(\varphi - \theta)\,\mathbf{e}_\varphi $$
$$ \mathbf{F}_k^Q = k\left(\mathbf{r}^Q - \mathbf{r}^P\right) = ka\left[2 - \cos(\varphi - \theta)\right]\mathbf{e}_r^Q - ka\sin(\varphi - \theta)\,\mathbf{e}_\theta $$

(For $P$: $\mathbf{e}_r^Q\cdot\mathbf{e}_r^P = \cos(\varphi - \theta)$ and $-2a\,\mathbf{e}_r^Q\cdot\mathbf{e}_\varphi = -2a\sin(\theta - \varphi) = 2a\sin(\varphi - \theta)$. For $Q$: $-a\,\mathbf{e}_r^P\cdot\mathbf{e}_\theta = -a\sin(\varphi - \theta)$.)

##### (e) Inertia forces in $S_1$
* **Pedagogical Justification:** Notes Eq. 4.62 with $\mathbf{a}_0^O = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$: only the centrifugal force $-m\boldsymbol{\omega}_{10}\times(\boldsymbol{\omega}_{10}\times\mathbf{r}_1)$ and the Coriolis force $-2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1$ remain (Slide 28).

Cross products with $\mathbf{j}_1\times\mathbf{i}_1 = -\mathbf{k}_1$, $\mathbf{j}_1\times\mathbf{j}_1 = \mathbf{0}$, $\mathbf{j}_1\times\mathbf{k}_1 = \mathbf{i}_1$. For $P$, $\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P = \Omega a\left(\cos\varphi\,\mathbf{j}_1\times\mathbf{i}_1 + \sin\varphi\,\mathbf{j}_1\times\mathbf{j}_1\right) = -\Omega a\cos\varphi\,\mathbf{k}_1$ and $\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = -\Omega^2 a\cos\varphi\,\mathbf{j}_1\times\mathbf{k}_1 = -\Omega^2 a\cos\varphi\,\mathbf{i}_1$. Hence (it is $m\Omega^2\mathbf{r}_\perp$, Slide 30, with $\mathbf{r}_\perp = a\cos\varphi\,\mathbf{i}_1$ the horizontal leg of the triangle), using $\mathbf{i}_1 = \cos\varphi\,\mathbf{e}_r^P - \sin\varphi\,\mathbf{e}_\varphi$:

$$ \mathbf{F}_C^P = m\Omega^2 a\cos\varphi\,\mathbf{i}_1 = m\Omega^2 a\cos\varphi\left(\cos\varphi\,\mathbf{e}_r^P - \sin\varphi\,\mathbf{e}_\varphi\right), \qquad \mathbf{F}_C^Q = 2m\Omega^2 a\cos\theta\left(\cos\theta\,\mathbf{e}_r^Q - \sin\theta\,\mathbf{e}_\theta\right) $$

For the Coriolis force, $\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P = \Omega a\dot\varphi\left(-\sin\varphi\,\mathbf{j}_1\times\mathbf{i}_1 + \cos\varphi\,\mathbf{j}_1\times\mathbf{j}_1\right) = \Omega a\dot\varphi\sin\varphi\,\mathbf{k}_1$, so

$$ \mathbf{F}_{COR}^P = -2m\Omega a\dot\varphi\sin\varphi\,\mathbf{k}_1, \qquad \mathbf{F}_{COR}^Q = -4m\Omega a\dot\theta\sin\theta\,\mathbf{k}_1 $$

The Coriolis forces are perpendicular to the plane of the wires: only the reactions $N_2$, $N_4$ can balance them.

##### (f) Equations of motion free of unknown reactions
* **Pedagogical Justification:** write $m\mathbf{a}_1 = \mathbf{F} + \mathbf{F}_i$ (Notes Eq. 4.63) for each particle and project on its tangent ($\mathbf{e}_\varphi$, $\mathbf{e}_\theta$), which is perpendicular to both reaction components and to the Coriolis force.

$P$, along $\mathbf{e}_\varphi$: $ma\ddot\varphi = -mg\cos\varphi + 2ka\sin(\varphi - \theta) - m\Omega^2 a\sin\varphi\cos\varphi$.

$Q$, along $\mathbf{e}_\theta$: $2ma\ddot\theta = -mg\cos\theta - ka\sin(\varphi - \theta) - 2m\Omega^2 a\sin\theta\cos\theta$.

Dividing by $ma$ and $2ma$:

$$ \boxed{\ddot\varphi = -\frac{g}{a}\cos\varphi + \frac{2k}{m}\sin(\varphi - \theta) - \Omega^2\sin\varphi\cos\varphi, \qquad \ddot\theta = -\frac{g}{2a}\cos\theta - \frac{k}{2m}\sin(\varphi - \theta) - \Omega^2\sin\theta\cos\theta} $$

**Remaining projections** (they contain the reactions). $P$, along $\mathbf{e}_r^P$: $-ma\dot\varphi^2 = N_1 - mg\sin\varphi + ka\left[1 - 2\cos(\varphi - \theta)\right] + m\Omega^2 a\cos^2\varphi$. Along $\mathbf{k}_1$: $0 = N_2 - 2m\Omega a\dot\varphi\sin\varphi$.

$Q$, along $\mathbf{e}_r^Q$: $-2ma\dot\theta^2 = N_3 - mg\sin\theta + ka\left[2 - \cos(\varphi - \theta)\right] + 2m\Omega^2 a\cos^2\theta$. Along $\mathbf{k}_1$: $0 = N_4 - 4m\Omega a\dot\theta\sin\theta$.

### Answers and Checks

##### (a) Degrees of freedom
Two, with coordinates $(\varphi, \theta)$.

##### (b) Reactions
Four independent components: $\mathbf{N}^P = N_1\,\mathbf{e}_r^P + N_2\,\mathbf{k}_1$, $\mathbf{N}^Q = N_3\,\mathbf{e}_r^Q + N_4\,\mathbf{k}_1$.

##### (c) Relative accelerations
$\mathbf{a}_1^P = a\ddot\varphi\,\mathbf{e}_\varphi - a\dot\varphi^2\,\mathbf{e}_r^P$, $\mathbf{a}_1^Q = 2a\ddot\theta\,\mathbf{e}_\theta - 2a\dot\theta^2\,\mathbf{e}_r^Q$.

##### (d) Applied forces
Weights $-mg\,\mathbf{j}_1$ on each particle; repulsions $\mathbf{F}_k^P$ and $\mathbf{F}_k^Q$ as above.

##### (e) Inertia forces
$\mathbf{F}_C^P = m\Omega^2 a\cos\varphi\,\mathbf{i}_1$, $\mathbf{F}_C^Q = 2m\Omega^2 a\cos\theta\,\mathbf{i}_1$, $\mathbf{F}_{COR}^P = -2m\Omega a\dot\varphi\sin\varphi\,\mathbf{k}_1$, $\mathbf{F}_{COR}^Q = -4m\Omega a\dot\theta\sin\theta\,\mathbf{k}_1$.

##### (f) Equations of motion
The two boxed equations above, free of the reactions.

##### (g) Reactions as functions of time
* **Pedagogical Justification:** the remaining projections ($\mathbf{e}_r$ and $\mathbf{k}_1$) contain one reaction each; with $\varphi(t)$, $\theta(t)$ known from (f), they give the reactions explicitly.

$$ \boxed{\begin{aligned} N_1(t) &= -ma\dot\varphi^2 + mg\sin\varphi - ka\left[1 - 2\cos(\varphi - \theta)\right] - m\Omega^2 a\cos^2\varphi, & N_2(t) &= 2m\Omega a\dot\varphi\sin\varphi \\ N_3(t) &= -2ma\dot\theta^2 + mg\sin\theta - ka\left[2 - \cos(\varphi - \theta)\right] - 2m\Omega^2 a\cos^2\theta, & N_4(t) &= 4m\Omega a\dot\theta\sin\theta \end{aligned}} $$

##### (h) Mechanical energy in $S_1$
* **Pedagogical Justification:** yes, it is conserved. In $S_1$ the wires are fixed and smooth, so $\mathbf{N}\cdot\mathbf{v}_1 = 0$; the Coriolis forces do no work (Slide 31); the Euler force and $-m\mathbf{a}_0^O$ vanish; the weights, the repulsion (a central force linear in the distance) and the centrifugal forces (constant $\boldsymbol{\omega}_{10}$, Slide 30) all derive from potentials.

Potentials in $S_1$: weights $mga\sin\varphi + 2mga\sin\theta$ (heights $y_1$); repulsion $-\tfrac12 k\left|\mathbf{r}^P - \mathbf{r}^Q\right|^2$ (minus sign: repulsive, so that $-\nabla_P$ gives $+k(\mathbf{r}^P - \mathbf{r}^Q)$), with

$$ \left|\mathbf{r}^P - \mathbf{r}^Q\right|^2 = a^2 + 4a^2 - 4a^2\,\mathbf{e}_r^P\cdot\mathbf{e}_r^Q = 5a^2 - 4a^2\cos(\varphi - \theta) $$

and centrifugal $-\tfrac12 m\Omega^2\left(r_\perp^P\right)^2 - \tfrac12 m\Omega^2\left(r_\perp^Q\right)^2$ with $r_\perp = |x_1|$ (distance to the axis $Oy_1$, since $z_1 = 0$): $-\tfrac12 m\Omega^2 a^2\cos^2\varphi - 2m\Omega^2 a^2\cos^2\theta$. Kinetic energy: $\tfrac12 m a^2\dot\varphi^2 + \tfrac12 m\,4a^2\dot\theta^2$. Dropping the constant $-\tfrac52 ka^2$:

$$ \boxed{E_1 = \frac12 ma^2\left(\dot\varphi^2 + 4\dot\theta^2\right) + mga\left(\sin\varphi + 2\sin\theta\right) + 2ka^2\cos(\varphi - \theta) - \frac12 m\Omega^2 a^2\left(\cos^2\varphi + 4\cos^2\theta\right) = \text{const}} $$

**Check.** By the chain rule ($\frac{d}{dt}\cos(\varphi - \theta) = -\sin(\varphi - \theta)(\dot\varphi - \dot\theta)$, $\frac{d}{dt}\cos^2\varphi = -2\cos\varphi\sin\varphi\,\dot\varphi$):

$$ \frac{dE_1}{dt} = \dot\varphi\left[ma^2\ddot\varphi + mga\cos\varphi - 2ka^2\sin(\varphi - \theta) + m\Omega^2a^2\sin\varphi\cos\varphi\right] + \dot\theta\left[4ma^2\ddot\theta + 2mga\cos\theta + 2ka^2\sin(\varphi - \theta) + 4m\Omega^2a^2\sin\theta\cos\theta\right] $$

and both brackets vanish by the two equations of (f) (multiplied by $ma^2$ and $4ma^2$), so $dE_1/dt = 0$.

##### (i) Parameters for the equilibrium $\varphi = 30^\circ$, $\theta = -60^\circ$
* **Pedagogical Justification:** a relative equilibrium has $\dot\varphi = \dot\theta = \ddot\varphi = \ddot\theta = 0$, so the right-hand sides of (f) must vanish. Dividing the first by $g/a$ and the second by $g/(2a)$ introduces $\alpha = ka/(mg)$ and $\beta = a\Omega^2/g$.
$$ 0 = -\cos\varphi + 2\alpha\sin(\varphi - \theta) - \beta\sin\varphi\cos\varphi, \qquad 0 = -\cos\theta - \alpha\sin(\varphi - \theta) - 2\beta\sin\theta\cos\theta $$

With $\varphi - \theta = 90^\circ$ ($\sin = 1$), $\cos 30^\circ = \tfrac{\sqrt3}{2}$, $\sin 30^\circ = \tfrac12$, $\cos(-60^\circ) = \tfrac12$, $\sin(-60^\circ) = -\tfrac{\sqrt3}{2}$:

$$ 0 = -\frac{\sqrt3}{2} + 2\alpha - \frac{\sqrt3}{4}\beta, \qquad 0 = -\frac12 - \alpha + \frac{\sqrt3}{2}\beta $$

From the second, $\alpha = \tfrac{\sqrt3}{2}\beta - \tfrac12$. Substituting in the first: $-\tfrac{\sqrt3}{2} + \sqrt3\beta - 1 - \tfrac{\sqrt3}{4}\beta = 0$, i.e. $\tfrac{3\sqrt3}{4}\beta = 1 + \tfrac{\sqrt3}{2} = \tfrac{2 + \sqrt3}{2}$, so

$$ \beta = \frac{2\left(2 + \sqrt3\right)}{3\sqrt3} = \frac{6 + 4\sqrt3}{9} \approx 1.4365, \qquad \alpha = \frac{\sqrt3}{2}\cdot\frac{6 + 4\sqrt3}{9} - \frac12 = \frac{12 + 6\sqrt3 - 9}{18} = \frac{1 + 2\sqrt3}{6} \approx 0.7440 $$
$$ \boxed{\alpha = \frac{ka}{mg} = \frac{1 + 2\sqrt3}{6} \approx 0.744, \qquad \beta = \frac{a\Omega^2}{g} = \frac{6 + 4\sqrt3}{9} \approx 1.4365} $$

Both values are positive, so the equilibrium is physically realisable.

##### Checks
* **Equilibrium:** at $\varphi - \theta = 90^\circ$ the radii $OP$ and $OQ$ are perpendicular (as in the wire-plane figure), so the tangential part of the repulsion is as large as it can be ($2ka$ on $P$, $ka$ on $Q$), and it balances the tangential components of the weight and of the centrifugal force. $P$ (at $30^\circ$ above $Ox_1$) is pushed up its wire by the repulsion from $Q$, while gravity and the centrifugal force pull it back; $Q$ (at $60^\circ$ below $Ox_1$) is pushed down by the repulsion and by gravity, and the centrifugal force (which pulls it towards $\theta = 0$, away from the axis) holds it.
* **Coriolis forces:** they are normal to the rotating plane and only load the wires ($N_2$, $N_4$); they never enter the equations of motion or the energy.
* **Limits:** $\Omega \to 0$ removes the centrifugal terms and $N_2 = N_4 = 0$; $k \to 0$ decouples the two particles into two independent rotating-ring pendulums, $\ddot\varphi = -\tfrac{g}{a}\cos\varphi - \Omega^2\sin\varphi\cos\varphi$.
* **Orthogonality:** $\mathbf{e}_r^P\cdot\mathbf{e}_\varphi = -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi = 0$, and the same for $Q$.
* **Dimensions:** $[g/a] = [k/m] = [\Omega^2] = \text{s}^{-2} = [\ddot\varphi]$; $[N_1]$: $[ma\dot\varphi^2] = [mg] = [ka] = [m\Omega^2a] = \text{N}$; $[N_2] = [m\Omega a\dot\varphi] = \text{N}$; $[E_1] = \text{kg}\,\text{m}^2/\text{s}^2 = [mga] = [ka^2] = \text{J}$; $\alpha = \text{N}\,\text{m}^{-1}\,\text{m}/\text{N}$ and $\beta = \text{m}\,\text{s}^{-2}/(\text{m}\,\text{s}^{-2})$ are dimensionless.
* **Symbolic check (sympy):** $\mathbf{a}_0$ of each particle obtained by differentiating $[{}_0R_1]\,\mathbf{r}_1$ twice equals the Notes Eq. 3.27 decomposition; the two equations of motion, the four reactions and $dE_1/dt = 0$ are confirmed, and solving the equilibrium conditions gives exactly the values above.
* **Check against the official key** (Problems.pdf, p. 76): $\alpha = 0.744$, $\beta = 1.4365$. Our exact values $\alpha = (1 + 2\sqrt3)/6 = 0.74402$ and $\beta = (6 + 4\sqrt3)/9 = 1.43647$ agree.

---

## Problem 49: Particle on a Rotating Sphere Attracted to a Point

### Reference Frames, Bases and Coordinates
* **Physical system:** a particle $P$ of mass $m$ slides on a smooth sphere of radius $a$ centred at $O$. A point $A$ of the equatorial plane, at distance $a$ from the surface (so $OA = 2a$), attracts $P$ with the force $k\,\overrightarrow{PA}$. Sphere and $A$ rotate rigidly about the vertical with angular velocity $\Omega\,\mathbf{k}_0$. No gravity.
* **Hypotheses:**
  1. $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ is inertial; $\Omega$ is constant.
  2. The sphere is smooth and the contact bilateral: the reaction is radial, $\mathbf{N} = N\,\mathbf{e}_r$ with $N$ of either sign.
  3. **Reading of the figure (angles):** $\phi$ is the angle at $O$ between $\overrightarrow{OA}$ (i.e. $\mathbf{i}_1$) and $\overrightarrow{OP}$; $\theta$ is the angle, measured about the axis $OA$, between the plane containing $\mathbf{i}_1$ and $\overrightarrow{OP}$ and the equatorial plane (the figure draws it at the point where $OA$ crosses the sphere, between the equator and the arc through $P$). So $\phi$ is a polar angle about the axis $OA$ and $\theta$ the corresponding azimuth, with $\theta = 0$ in the equatorial plane on the side of $\mathbf{j}_1$ and $\theta = \pi/2$ in the upper hemisphere.
* **Frames:** $S_0 = \{O; \mathcal{B}_0\}$ inertial; $S_1 = \{O; \mathcal{B}_1\}$, $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, rotating with the sphere, with $\mathbf{k}_1 = \mathbf{k}_0$ and $\mathbf{i}_1$ along $\overrightarrow{OA}$; the figure measures the angle $\Omega t$ from $\mathbf{i}_0$ to $\mathbf{i}_1$.
* **Spherical basis with polar axis $OA$:** $\{\mathbf{e}_r, \mathbf{e}_\phi, \mathbf{e}_\theta\}$ at $P$, deduced in the next section.
* **Constraints and degrees of freedom:** $P$ has 3 coordinates and one constraint, $|\overrightarrow{OP}| = a$ (holonomic, scleronomic in $S_1$, smooth): CDOF $= 3 - 1 = 2$, with the angles $(\phi, \theta)$; the unknown reaction is $N$ along $\mathbf{e}_r$.
* **Why $S_1$:** in $S_1$ both the sphere and the attracting point $A$ are fixed, so the attraction depends only on the position of $P$ and the problem has no explicit time dependence; the inertia forces (Notes Eq. 4.62) take that role. With polar axis $OA$, the distance $AP$ depends on $\phi$ only, which keeps the attraction simple.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $a$ | radius of the sphere ($OA = 2a$) | m |
| $k$ | attraction constant | N/m |
| $\Omega$ | angular rate of sphere and $A$ | rad/s |
| $\phi$, $\theta$ | polar angle from $OA$, azimuth about $OA$ | rad |
| $N$ | normal reaction | N |
| $\Lambda = m\Omega^2/k$ | ratio of centrifugal to attraction stiffness | 1 |

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p49-top-view.svg]]

The rotation is about $\mathbf{k}_0$, so we look down from $+z$: $\mathbf{k}_0 = \mathbf{k}_1$ points out of the paper ($\odot$). With $\mathbf{i}_0$ to the right, $\mathbf{i}_0\times\mathbf{j}_0 = \mathbf{k}_0$ requires the fingers to curl counter-clockwise from $\mathbf{i}_0$ to $\mathbf{j}_0$ for the thumb to point at the reader, so $\mathbf{j}_0$ points up the page. With $\Omega \gt 0$ the frame $S_1$ turns counter-clockwise, and after a time $t$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the shaded triangle: the leg adjacent to $\Omega t$ is $\cos\Omega t$ along $\mathbf{i}_0$ and the leg opposite to $\Omega t$ is $\sin\Omega t$ along $+\mathbf{j}_0$. So $\mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ and turns the same angle counter-clockwise, so its tip moves to the side of $-\mathbf{i}_0$: leg $\cos\Omega t$ along $\mathbf{j}_0$ and leg $\sin\Omega t$ towards $-\mathbf{i}_0$. **That is the origin of the minus sign** in $\mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0$.
* $\mathbf{k}_1 = \mathbf{k}_0$, the axis of the rotation.

$$ \mathbf{i}_1 = \cos\Omega t\,\mathbf{i}_0 + \sin\Omega t\,\mathbf{j}_0, \qquad \mathbf{j}_1 = -\sin\Omega t\,\mathbf{i}_0 + \cos\Omega t\,\mathbf{j}_0, \qquad \mathbf{k}_1 = \mathbf{k}_0 $$
$$ [{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \\ \sin\Omega t & \cos\Omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1\cdot\left(\cos\Omega t\cos\Omega t - (-\sin\Omega t)\sin\Omega t\right) = \cos^2\Omega t + \sin^2\Omega t = 1 $$

The rows are unit vectors and the first two are orthogonal ($\cos\Omega t\sin\Omega t - \sin\Omega t\cos\Omega t = 0$), so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$:** $\mathbf{a}_0^O = \mathbf{0}$, $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{k}_1$ (simple rotation, Slide 16), $\boldsymbol{\alpha}_{10} = \mathbf{0}$. Check: by the chain rule $\left.\frac{d\mathbf{i}_1}{dt}\right|_0 = -\Omega\sin\Omega t\,\mathbf{i}_0 + \Omega\cos\Omega t\,\mathbf{j}_0 = \Omega\,\mathbf{j}_1 = \Omega\,\mathbf{k}_1\times\mathbf{i}_1$. The attracting point is fixed in $S_1$: $\mathbf{r}_1^A = 2a\,\mathbf{i}_1$ (it lies on the dashed $\mathbf{i}_1$ axis of the figure).

#### The azimuth $\theta$: view along $OA$

![[attachments/EM-SOL/p49-axis-view.svg]]

$\theta$ turns about the axis $OA$, so we look along that axis with $\mathbf{i}_1$ out of the paper ($\odot$). With $\mathbf{j}_1$ to the right, $\mathbf{k}_1 = \mathbf{i}_1\times\mathbf{j}_1$ points up (fingers from $\mathbf{i}_1$, towards the reader, to $\mathbf{j}_1$, right; thumb up). The azimuth starts at $\mathbf{j}_1$ ($\theta = 0$, equatorial plane) and grows counter-clockwise towards $\mathbf{k}_1$ ($\theta = \pi/2$, upper hemisphere), as in the reading of the figure. The unit vector $\mathbf{u}$ of the plane $\mathbf{j}_1\mathbf{k}_1$ in the direction $\theta$ is the hypotenuse of the shaded triangle, with the leg $\cos\theta$ along $\mathbf{j}_1$ (adjacent) and $\sin\theta$ along $\mathbf{k}_1$ (opposite):

$$ \mathbf{u}(\theta) = \cos\theta\,\mathbf{j}_1 + \sin\theta\,\mathbf{k}_1, \qquad \mathbf{e}_\theta = \frac{d\mathbf{u}}{d\theta} = -\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1 $$

($\frac{d}{d\theta}\cos\theta = -\sin\theta$, $\frac{d}{d\theta}\sin\theta = \cos\theta$; $|\mathbf{e}_\theta| = 1$ and $\mathbf{u}\cdot\mathbf{e}_\theta = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0$). The minus sign in $\mathbf{e}_\theta$ appears because turning $\mathbf{u}$ a further $90^\circ$ counter-clockwise takes its tip to the side of $-\mathbf{j}_1$.

#### The polar angle $\phi$: the meridian plane of $P$

![[attachments/EM-SOL/p49-meridian.svg]]

$P$ lies in the plane that contains the axis $OA$ and the direction $\mathbf{u}$ (the meridian plane of $P$); it is drawn with $\mathbf{i}_1$ to the right and $\mathbf{u}$ up, so $\mathbf{i}_1\times\mathbf{u} = \cos\theta\,\mathbf{k}_1 - \sin\theta\,\mathbf{j}_1 = \mathbf{e}_\theta$ points out of the paper. In the shaded right triangle the hypotenuse is $|OP| = a$, the leg adjacent to $\phi$ is $a\cos\phi$ along $\mathbf{i}_1$ and the leg opposite to $\phi$ is $a\sin\phi$ along $\mathbf{u}$ (the distance $OP'$ of the axis view). Hence

$$ \mathbf{r}_1^P = \overrightarrow{OP} = a\cos\phi\,\mathbf{i}_1 + a\sin\phi\,\mathbf{u} = a\cos\phi\,\mathbf{i}_1 + a\sin\phi\cos\theta\,\mathbf{j}_1 + a\sin\phi\sin\theta\,\mathbf{k}_1 = a\,\mathbf{e}_r $$

**Relation with the standard spherical coordinates.** The usual spherical coordinates take the polar axis along $\mathbf{k}$ and the azimuth from $\mathbf{i}$ towards $\mathbf{j}$: $\mathbf{e}_r = \sin\phi\cos\theta\,\mathbf{i} + \sin\phi\sin\theta\,\mathbf{j} + \cos\phi\,\mathbf{k}$. Here the roles are permuted cyclically, $(\mathbf{i}, \mathbf{j}, \mathbf{k}) \to (\mathbf{j}_1, \mathbf{k}_1, \mathbf{i}_1)$, which keeps the triad right-handed ($\mathbf{j}_1\times\mathbf{k}_1 = \mathbf{i}_1$); substituting gives exactly the $\mathbf{e}_r$ above. The polar axis is $OA$ instead of the vertical because then $|AP|$ depends on $\phi$ only.

**Spherical basis by differentiation.** The radial vector is $\mathbf{e}_r = \cos\phi\,\mathbf{i}_1 + \sin\phi\,\mathbf{u}$. Its derivative with respect to $\phi$ ($\frac{d}{d\phi}\cos\phi = -\sin\phi$, $\frac{d}{d\phi}\sin\phi = \cos\phi$) already has unit length, $\sqrt{\sin^2\phi + \cos^2\phi} = 1$; with respect to $\theta$, $\frac{\partial\mathbf{e}_r}{\partial\theta} = \sin\phi\,\frac{d\mathbf{u}}{d\theta} = \sin\phi\,\mathbf{e}_\theta$, whose length is $\sin\phi$:

$$ \mathbf{e}_\phi = \frac{\partial\mathbf{e}_r}{\partial\phi} = -\sin\phi\,\mathbf{i}_1 + \cos\phi\cos\theta\,\mathbf{j}_1 + \cos\phi\sin\theta\,\mathbf{k}_1, \qquad \mathbf{e}_\theta = \frac{1}{\sin\phi}\frac{\partial\mathbf{e}_r}{\partial\theta} = -\sin\theta\,\mathbf{j}_1 + \cos\theta\,\mathbf{k}_1 $$

with $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ given above in terms of $\mathcal{B}_0$. The triad is orthonormal and right-handed: $\mathbf{e}_r\times\mathbf{e}_\phi = \left(\cos^2\phi + \sin^2\phi\right)\mathbf{i}_1\times\mathbf{u} = \cos\theta\,\mathbf{k}_1 - \sin\theta\,\mathbf{j}_1 = \mathbf{e}_\theta$, hence also $\mathbf{e}_\phi\times\mathbf{e}_\theta = \mathbf{e}_r$, $\mathbf{e}_\theta\times\mathbf{e}_r = \mathbf{e}_\phi$. Inverse relations used below (read from the meridian triangle): $\mathbf{u} = \sin\phi\,\mathbf{e}_r + \cos\phi\,\mathbf{e}_\phi$, so

$$ \mathbf{i}_1 = \cos\phi\,\mathbf{e}_r - \sin\phi\,\mathbf{e}_\phi, \qquad \mathbf{k}_1 = \sin\theta\,\mathbf{u} + \cos\theta\,\mathbf{e}_\theta = \sin\phi\sin\theta\,\mathbf{e}_r + \cos\phi\sin\theta\,\mathbf{e}_\phi + \cos\theta\,\mathbf{e}_\theta $$

(the second from the axis-view triangle, $\mathbf{k}_1 = \sin\theta\,\mathbf{u} + \cos\theta\,\mathbf{e}_\theta$).

### Kinematics

##### (a) Position, velocity and acceleration in $S_1$
* **Pedagogical Justification:** $\mathbf{r}_1^P = a\,\mathbf{e}_r$ (Notes Eq. 3.16 with the origin $O$ common to both frames). The relative derivative keeps $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ fixed, so the spherical vectors change only through $\phi(t)$ and $\theta(t)$ (chain rule).

Time derivatives of the basis in $S_1$:

$$ \left.\frac{d\mathbf{e}_r}{dt}\right|_1 = -\sin\phi\,\dot\phi\,\mathbf{i}_1 + \cos\phi\,\dot\phi\,\mathbf{u} + \sin\phi\,\frac{d\mathbf{u}}{d\theta}\dot\theta = \dot\phi\,\mathbf{e}_\phi + \sin\phi\,\dot\theta\,\mathbf{e}_\theta $$
$$ \left.\frac{d\mathbf{e}_\phi}{dt}\right|_1 = -\cos\phi\,\dot\phi\,\mathbf{i}_1 - \sin\phi\,\dot\phi\,\mathbf{u} + \cos\phi\,\dot\theta\,\mathbf{e}_\theta = -\dot\phi\,\mathbf{e}_r + \cos\phi\,\dot\theta\,\mathbf{e}_\theta $$
$$ \left.\frac{d\mathbf{e}_\theta}{dt}\right|_1 = \dot\theta\left(-\cos\theta\,\mathbf{j}_1 - \sin\theta\,\mathbf{k}_1\right) = -\dot\theta\,\mathbf{u} = -\sin\phi\,\dot\theta\,\mathbf{e}_r - \cos\phi\,\dot\theta\,\mathbf{e}_\phi $$

Position and velocity:

$$ \mathbf{r}_1^P = a\,\mathbf{e}_r, \qquad \mathbf{v}_1^P = a\left.\frac{d\mathbf{e}_r}{dt}\right|_1 = a\dot\phi\,\mathbf{e}_\phi + a\sin\phi\,\dot\theta\,\mathbf{e}_\theta $$

Acceleration, by the product rule on each term, $\frac{d}{dt}(a\dot\phi\,\mathbf{e}_\phi) = a\ddot\phi\,\mathbf{e}_\phi + a\dot\phi\left(-\dot\phi\,\mathbf{e}_r + \cos\phi\,\dot\theta\,\mathbf{e}_\theta\right)$ and $\frac{d}{dt}(a\sin\phi\,\dot\theta\,\mathbf{e}_\theta) = a\left(\cos\phi\,\dot\phi\dot\theta + \sin\phi\,\ddot\theta\right)\mathbf{e}_\theta + a\sin\phi\,\dot\theta\left(-\sin\phi\,\dot\theta\,\mathbf{e}_r - \cos\phi\,\dot\theta\,\mathbf{e}_\phi\right)$; collecting:

$$ \mathbf{a}_1^P = -a\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right)\mathbf{e}_r + a\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right)\mathbf{e}_\phi + a\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right)\mathbf{e}_\theta $$

### Forces and Equations of Motion

##### (b) Forces on the particle
* **Pedagogical Justification:** in $S_1$, $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$ (Notes Eq. 4.63). The actual forces are the attraction and the reaction; the inertia forces (Notes Eq. 4.62) reduce to the centrifugal and Coriolis forces because $\mathbf{a}_0^O = \mathbf{0}$ and $\boldsymbol{\alpha}_{10} = \mathbf{0}$.

**Attraction** (along the dashed segment $PA$ of the meridian figure): $\mathbf{F}_k = k\left(\mathbf{r}_1^A - \mathbf{r}_1^P\right) = k\left(2a\,\mathbf{i}_1 - a\,\mathbf{e}_r\right)$; with $\mathbf{i}_1 = \cos\phi\,\mathbf{e}_r - \sin\phi\,\mathbf{e}_\phi$,

$$ \mathbf{F}_k = ka\left(2\cos\phi - 1\right)\mathbf{e}_r - 2ka\sin\phi\,\mathbf{e}_\phi $$

**Reaction:** $\mathbf{N} = N\,\mathbf{e}_r$.

**Centrifugal force.** With the identity $\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = (\mathbf{a}\cdot\mathbf{c})\mathbf{b} - (\mathbf{a}\cdot\mathbf{b})\mathbf{c}$ (Slide 30): $\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) = \Omega^2 z_1\,\mathbf{k}_1 - \Omega^2\mathbf{r}_1^P$, where $z_1 = \mathbf{r}_1^P\cdot\mathbf{k}_1 = a\sin\phi\sin\theta$. Hence $\mathbf{F}_C = m\Omega^2\left(\mathbf{r}_1^P - z_1\mathbf{k}_1\right)$, and with $\mathbf{k}_1$ in the spherical basis:

$$ \mathbf{F}_C = m\Omega^2 a\left[\left(1 - \sin^2\phi\sin^2\theta\right)\mathbf{e}_r - \sin^2\theta\sin\phi\cos\phi\,\mathbf{e}_\phi - \sin\phi\sin\theta\cos\theta\,\mathbf{e}_\theta\right] $$

**Coriolis force.** Using $\mathbf{k}_1 = \sin\phi\sin\theta\,\mathbf{e}_r + \cos\phi\sin\theta\,\mathbf{e}_\phi + \cos\theta\,\mathbf{e}_\theta$ and the cyclic products of the right-handed triad:

$$ \mathbf{k}_1\times\mathbf{e}_\phi = \sin\phi\sin\theta\,\mathbf{e}_r\times\mathbf{e}_\phi + \cos\theta\,\mathbf{e}_\theta\times\mathbf{e}_\phi = \sin\phi\sin\theta\,\mathbf{e}_\theta - \cos\theta\,\mathbf{e}_r $$
$$ \mathbf{k}_1\times\mathbf{e}_\theta = \sin\phi\sin\theta\,\mathbf{e}_r\times\mathbf{e}_\theta + \cos\phi\sin\theta\,\mathbf{e}_\phi\times\mathbf{e}_\theta = -\sin\phi\sin\theta\,\mathbf{e}_\phi + \cos\phi\sin\theta\,\mathbf{e}_r $$
$$ \mathbf{F}_{COR} = -2m\Omega\,\mathbf{k}_1\times\left(a\dot\phi\,\mathbf{e}_\phi + a\sin\phi\,\dot\theta\,\mathbf{e}_\theta\right) = 2m\Omega a\left[\left(\cos\theta\,\dot\phi - \sin\theta\sin\phi\cos\phi\,\dot\theta\right)\mathbf{e}_r + \sin\theta\sin^2\phi\,\dot\theta\,\mathbf{e}_\phi - \sin\theta\sin\phi\,\dot\phi\,\mathbf{e}_\theta\right] $$

##### (b, continued) Vector equation and scalar equations

**Vector equation of motion in $S_1$:**

$$ m\mathbf{a}_1^P = k\left(\mathbf{r}_1^A - \mathbf{r}_1^P\right) + N\,\mathbf{e}_r - m\boldsymbol{\omega}_{10}\times\left(\boldsymbol{\omega}_{10}\times\mathbf{r}_1^P\right) - 2m\boldsymbol{\omega}_{10}\times\mathbf{v}_1^P $$

**Scalar equations free of $N$:** project on $\mathbf{e}_\phi$ and $\mathbf{e}_\theta$, which are perpendicular to $\mathbf{N}$:

$$ \boxed{ma\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right) = -2ka\sin\phi - m\Omega^2 a\sin^2\theta\sin\phi\cos\phi + 2m\Omega a\sin\theta\sin^2\phi\,\dot\theta} $$
$$ \boxed{ma\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right) = -m\Omega^2 a\sin\phi\sin\theta\cos\theta - 2m\Omega a\sin\theta\sin\phi\,\dot\phi} $$

**Projection on $\mathbf{e}_r$** (it contains $N$):

$$ -ma\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) = N + ka\left(2\cos\phi - 1\right) + m\Omega^2 a\left(1 - \sin^2\phi\sin^2\theta\right) + 2m\Omega a\left(\cos\theta\,\dot\phi - \sin\theta\sin\phi\cos\phi\,\dot\theta\right) $$

### Answers and Checks

##### (a) Position, velocity and acceleration
$\mathbf{r}_1^P = a\,\mathbf{e}_r$, $\mathbf{v}_1^P = a\dot\phi\,\mathbf{e}_\phi + a\sin\phi\,\dot\theta\,\mathbf{e}_\theta$, $\mathbf{a}_1^P = -a\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right)\mathbf{e}_r + a\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right)\mathbf{e}_\phi + a\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right)\mathbf{e}_\theta$, with the unit vectors defined above in terms of $\mathcal{B}_1$ and, through $[{}_0R_1]$, of $\mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0$.

##### (b) Equations of motion
The forces are $\mathbf{F}_k$, $\mathbf{N}$, $\mathbf{F}_C$ and $\mathbf{F}_{COR}$ above; the vector equation and the two boxed scalar equations for $\phi$ and $\theta$ are the answer.

##### (c) Conservation of mechanical energy in $S_1$
* **Pedagogical Justification:** yes, $E_1^P$ is conserved. The sphere is fixed in $S_1$ and smooth, so $\mathbf{N}\cdot\mathbf{v}_1^P = 0$ ($\mathbf{v}_1^P$ has no $\mathbf{e}_r$ component); $\mathbf{F}_{COR}\cdot\mathbf{v}_1^P = 0$ (Slide 31); the Euler force and $-m\mathbf{a}_0^O$ are zero; the attraction towards the point $A$, fixed in $S_1$, is conservative with $V_k = \tfrac12 k\left|\mathbf{r}_1^P - \mathbf{r}_1^A\right|^2$; and the centrifugal force has $V_C = -\tfrac12 m\Omega^2 r_\perp^2$ because $\boldsymbol{\omega}_{10}$ is constant (Slide 30).

Potentials on the sphere:

$$ \left|\mathbf{r}_1^P - \mathbf{r}_1^A\right|^2 = a^2 - 4a^2\,\mathbf{e}_r\cdot\mathbf{i}_1 + 4a^2 = 5a^2 - 4a^2\cos\phi \;\Rightarrow\; V_k = \frac52 ka^2 - 2ka^2\cos\phi $$
$$ r_\perp^2 = x_1^2 + y_1^2 = a^2 - z_1^2 = a^2 - a^2\sin^2\phi\sin^2\theta \;\Rightarrow\; V_C = -\frac12 m\Omega^2 a^2 + \frac12 m\Omega^2 a^2\sin^2\phi\sin^2\theta $$

Dropping the constants, with $T_1^P = \tfrac12 m\left|\mathbf{v}_1^P\right|^2 = \tfrac12 ma^2\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right)$:

$$ \boxed{E_1^P = \frac12 ma^2\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) - 2ka^2\cos\phi + \frac12 m\Omega^2 a^2\sin^2\phi\sin^2\theta = \text{const}} $$

**Check.** Differentiating with the chain and product rules ($\frac{d}{dt}\sin^2\phi = 2\sin\phi\cos\phi\,\dot\phi$, $\frac{d}{dt}\sin^2\theta = 2\sin\theta\cos\theta\,\dot\theta$) and grouping:

$$ \frac{dE_1^P}{dt} = a\dot\phi\left[ma\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right) + 2ka\sin\phi + m\Omega^2a\sin^2\theta\sin\phi\cos\phi\right] + a\sin\phi\,\dot\theta\left[ma\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right) + m\Omega^2a\sin\phi\sin\theta\cos\theta\right] $$

By the equations of (b) the brackets equal $2m\Omega a\sin\theta\sin^2\phi\,\dot\theta$ and $-2m\Omega a\sin\theta\sin\phi\,\dot\phi$, so

$$ \frac{dE_1^P}{dt} = 2m\Omega a^2\sin\theta\sin^2\phi\,\dot\phi\dot\theta - 2m\Omega a^2\sin\theta\sin^2\phi\,\dot\phi\dot\theta = 0 $$

which is exactly $\mathbf{F}_{COR}\cdot\mathbf{v}_1^P = 0$. The constant is fixed by initial conditions (not given).

##### (d) Equilibrium configurations
* **Pedagogical Justification:** a relative equilibrium has $\dot\phi = \dot\theta = \ddot\phi = \ddot\theta = 0$, so the right-hand sides of the equations of (b) must vanish (the Coriolis terms disappear). The points $\phi = 0, \pi$ are the poles of the coordinates ($\theta$ undefined there) and must be examined separately; the symbolic check confirms the list below with Cartesian coordinates and a Lagrange multiplier.

With $\Lambda = m\Omega^2/k$, the two conditions are

$$ \sin\phi\left(2k + m\Omega^2\sin^2\theta\cos\phi\right) = 0 \iff \sin\phi\left(2 + \Lambda\sin^2\theta\cos\phi\right) = 0, \qquad \sin\phi\sin\theta\cos\theta = 0 $$
* **$\sin\phi = 0$:** both are satisfied. **E1:** $\phi = 0$, $\mathbf{r}_1^P = a\,\mathbf{i}_1$, the point of the sphere nearest to $A$. **E2:** $\phi = \pi$, $\mathbf{r}_1^P = -a\,\mathbf{i}_1$, the point farthest from $A$. They exist for every $\Lambda$: at both, the attraction and the centrifugal force are radial (along $\pm\mathbf{i}_1$) and the reaction balances them.
* **$\sin\phi \neq 0$:** the second condition needs $\sin\theta = 0$ or $\cos\theta = 0$. If $\sin\theta = 0$, the first becomes $2 = 0$: impossible. If $\cos\theta = 0$ ($\theta = \pm\pi/2$, $\sin^2\theta = 1$), the first gives
$$ \cos\phi^* = -\frac{2k}{m\Omega^2} = -\frac{2}{\Lambda} $$

which has a solution with $\sin\phi^* \neq 0$ only if $\Lambda \gt 2$. **E3, E4** ($\theta = \pm\pi/2$):

$$ \mathbf{r}_1^P = -\frac{2a}{\Lambda}\,\mathbf{i}_1 \pm a\sqrt{1 - \frac{4}{\Lambda^2}}\,\mathbf{k}_1 $$

They lie in the meridian plane $\mathbf{i}_1\mathbf{k}_1$ that contains $A$, on the hemisphere opposite to $A$, symmetric above and below the equator.

**Discussion in terms of $m\Omega^2/k$:**

* $\Lambda = m\Omega^2/k \le 2$: only E1 and E2.
* $\Lambda \gt 2$: E1, E2, E3 and E4. As $\Lambda \to 2^+$, $\cos\phi^* \to -1$ and E3, E4 merge into E2 (a pitchfork bifurcation); as $\Lambda \to \infty$, $\cos\phi^* \to 0$ and they tend to the poles $\pm a\,\mathbf{k}_1$.

*Extension (stability, beyond what is asked).* Near E1, $V_1 \approx \text{const} + k\left(y_1^2 + z_1^2\right) + \tfrac12 m\Omega^2 z_1^2$, a strict minimum, so E1 is stable for every $\Lambda$ (energy argument). Near E2, $V_1 \approx \text{const} - k y_1^2 + \left(\tfrac12 m\Omega^2 - k\right)z_1^2$; along $\mathbf{j}_1$ the linearised motion is $m\ddot y_1 = 2ky_1$ (no Coriolis coupling there, because $\mathbf{k}_1\times\mathbf{v}_1^P$ is normal to the sphere at E2), so E2 is always unstable with growth rate $\sqrt{2k/m}$. E3 and E4 are maxima of $V_1$; the linearisation including the Coriolis terms (computed numerically for several values $\Lambda \gt 2$) has eigenvalues with positive real part, so they are unstable as well.

##### (e) Reaction of the sphere
* **Pedagogical Justification:** the projection of the vector equation on $\mathbf{e}_r$ (written at the end of the previous section) contains $N$ and only known functions once $\phi(t)$, $\theta(t)$ are known.
$$ \boxed{\mathbf{N} = -\left[ma\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) + ka\left(2\cos\phi - 1\right) + m\Omega^2 a\left(1 - \sin^2\phi\sin^2\theta\right) + 2m\Omega a\left(\cos\theta\,\dot\phi - \sin\theta\sin\phi\cos\phi\,\dot\theta\right)\right]\mathbf{e}_r} $$

with $\mathbf{e}_r = \cos\phi\,\mathbf{i}_1 + \sin\phi\cos\theta\,\mathbf{j}_1 + \sin\phi\sin\theta\,\mathbf{k}_1$ and $\mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1$ in terms of $\mathcal{B}_0$ from the change-of-basis section.

##### Checks
* **Competition of two effects:** the attraction pulls $P$ towards the point nearest $A$ (E1), and its tangential part has stiffness $\sim k$; the centrifugal force pushes $P$ away from the vertical axis with stiffness $\sim m\Omega^2$. The ratio $\Lambda = m\Omega^2/k$ decides whether, on the far side of the sphere, the centrifugal push towards the equator can be balanced by the attraction: only for $\Lambda \gt 2$ do the extra equilibria E3, E4 appear.
* **Reaction at E1:** with $\phi = 0$ and no motion, $N = -ka - m\Omega^2a$: the sphere pulls $P$ inwards, since both the attraction (towards $A$, outside the sphere) and the centrifugal force push $P$ outwards. The bilateral contact assumed among the hypotheses is needed for that.
* **Limit $\Omega \to 0$:** the inertia forces vanish, $\Lambda \to 0$, and only E1 (stable) and E2 (unstable) remain, as for a fixed sphere with a fixed attracting point.
* **Orthogonality:** $\mathbf{e}_r\cdot\mathbf{e}_\phi = -\cos\phi\sin\phi + \sin\phi\cos\phi(\cos^2\theta + \sin^2\theta) = 0$, $\mathbf{e}_r\cdot\mathbf{e}_\theta = \sin\phi(-\cos\theta\sin\theta + \sin\theta\cos\theta) = 0$, $\mathbf{e}_\phi\cdot\mathbf{e}_\theta = \cos\phi(-\cos\theta\sin\theta + \sin\theta\cos\theta) = 0$.
* **Dimensions:** in the $\mathbf{e}_\phi$ equation, $[ma\ddot\phi] = \text{kg}\,\text{m}\,\text{s}^{-2} = \text{N}$, $[ka] = \text{N}$, $[m\Omega^2a] = \text{N}$, $[m\Omega a\dot\theta] = \text{N}$; $[E_1^P] = [ka^2] = [m\Omega^2a^2] = \text{J}$; $\Lambda = \text{kg}\,\text{s}^{-2}/(\text{N}/\text{m})$ is dimensionless.
* **Symbolic check (sympy):** $\mathbf{a}_0^P$ from differentiating $[{}_0R_1]\,\mathbf{r}_1^P$ twice equals the Notes Eq. 3.27 decomposition; the force components, both equations of motion, the reaction and $dE_1^P/dt = 0$ are confirmed; the equilibria found with Cartesian coordinates and a Lagrange multiplier are exactly E1 to E4.
* **Check against the official key:** none for this problem (Problems.pdf, p. 76 lists no answer for 49), so the results rest on the independent checks above.

---

## Problem 51: Particle inside a Hollow Sphere in a Rotating Frame

### Reference Frames, Bases and Coordinates
* **Physical system:** a heavy particle $P$ (mass $m$) slides on the smooth inner surface of a sphere of radius $R$ and centre $C$, $\mathbf{r}_1^C = R(\mathbf{j}_1 + \mathbf{k}_1)$. The sphere is fixed in the frame $S_1 = \{A; \mathbf{i}_1, \mathbf{j}_1, \mathbf{k}_1\}$, which turns about its vertical axis $A\mathbf{k}_1$ with the known rate $\Omega(t)$. The sphere touches the rotation axis at the point $(0, 0, R)$ and the plane $z_1 = 0$ at $(0, R, 0)$.
* **Why $S_1$.** The constraint (the sphere) is fixed in $S_1$, so in $S_1$ the particle simply moves on a fixed sphere described by two angles; all the effect of the rotation is collected in the inertia forces (Notes Eqs. 4.62–4.63). In $S_0$ the sphere would be a moving constraint.
* **Hypotheses:**
  1. The point $A$ is fixed in an inertial frame $S_0$ (it lies on the rotation axis), so $\mathbf{v}_0^A = \mathbf{a}_0^A = \mathbf{0}$; $\mathbf{k}_1$ is the ascending vertical and gravity is $-g\,\mathbf{k}_1$ (figure).
  2. The surface is smooth: the reaction is normal to the sphere, along the radius $CP$. It is unilateral: the particle is inside, so the surface can only push it toward $C$.
  3. $\Omega(t)$ is a known function; $\dot{\Omega}(t)$ is then known too.
* **Frames.** $S_0 = \{A; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ inertial, with $\mathbf{k}_0 = \mathbf{k}_1$; $S_1$, basis $\mathcal{B}_1$, turns about $\mathbf{k}_1$ through the angle $\Psi(t)$, with $\dot{\Psi} = \Omega(t)$.
* **Coordinates (from the figure):** $\theta$ is the azimuth about the vertical through $C$, measured from the direction $\mathbf{i}_1$ toward $\mathbf{j}_1$; $\phi$ is the elevation of $CP$ above the horizontal plane through $C$. Ranges: $\theta \in (-\pi, \pi]$, $\phi \in [-\pi/2, \pi/2]$ (the poles $\phi = \pm\pi/2$ are coordinate singularities).
* **Spherical basis at $P$:** $\{\mathbf{u}_r, \mathbf{u}_\theta, \mathbf{u}_\phi\}$, deduced in the next section.
* **Degrees of freedom:** 3 coordinates minus 1 constraint $|CP| = R$: **2 DOF**, $(\theta, \phi)$. The reaction adds **1 unknown**, $N$.

| Symbol | Meaning | SI unit |
|---|---|---|
| $m$ | mass of $P$ | kg |
| $R$ | radius of the sphere | m |
| $g$ | gravitational acceleration | m/s$^2$ |
| $\Omega(t),\ \dot{\Omega}(t)$ | angular velocity and acceleration of $S_1$ about $\mathbf{k}_1$ | rad/s, rad/s$^2$ |
| $\theta,\ \phi$ | azimuth and elevation of $P$ seen from $C$ | rad |
| $N$ | magnitude of the reaction, $\mathbf{N} = -N\,\mathbf{u}_r$, $N \ge 0$ while in contact | N |

### Change of Basis and Position Vector

#### The basis $\mathcal{B}_1$ seen from above

![[attachments/EM-SOL/p51-top-view.svg]]

The rotation is about $\mathbf{k}_1 = \mathbf{k}_0$, so we look down from $+z$: $\mathbf{k}_0$ points out of the paper ($\odot$), $\mathbf{i}_0$ to the right and, since $\mathbf{i}_0\times\mathbf{j}_0 = \mathbf{k}_0$ needs a counter-clockwise turn from $\mathbf{i}_0$ to $\mathbf{j}_0$ for the thumb to point at the reader, $\mathbf{j}_0$ points up. A positive $\Omega$ turns $S_1$ counter-clockwise by $\Psi(t)$:

* $\mathbf{i}_1$ is the hypotenuse (length 1) of the shaded triangle: adjacent leg $\cos\Psi$ along $\mathbf{i}_0$, opposite leg $\sin\Psi$ along $+\mathbf{j}_0$.
* $\mathbf{j}_1$ starts on $\mathbf{j}_0$ and its tip moves to the side of $-\mathbf{i}_0$: leg $\cos\Psi$ along $\mathbf{j}_0$ and $\sin\Psi$ towards $-\mathbf{i}_0$, **hence the minus sign** in $\mathbf{j}_1 = -\sin\Psi\,\mathbf{i}_0 + \cos\Psi\,\mathbf{j}_0$.
* $\mathbf{k}_1 = \mathbf{k}_0$.

$$ [{}_0R_1] = \begin{pmatrix} \cos\Psi & -\sin\Psi & 0 \\ \sin\Psi & \cos\Psi & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0R_1] = 1\cdot\left(\cos\Psi\cos\Psi - (-\sin\Psi)\sin\Psi\right) = \cos^2\Psi + \sin^2\Psi = 1 $$

The columns have unit norm and the first two are orthogonal ($-\cos\Psi\sin\Psi + \sin\Psi\cos\Psi = 0$), so $[{}_0R_1][{}_0R_1]^T = I$.

**Motion of $S_1$:** $\boldsymbol{\omega}_{10} = \Omega\,\mathbf{k}_1$; since $\mathbf{k}_1$ is fixed in both frames, $\boldsymbol{\alpha}_{10} = \left.\frac{d\boldsymbol{\omega}_{10}}{dt}\right|_0 = \dot{\Omega}\,\mathbf{k}_1 + \Omega\,\boldsymbol{\omega}_{10}\times\mathbf{k}_1 = \dot{\Omega}\,\mathbf{k}_1$; $\mathbf{r}_0^A = \mathbf{v}_0^A = \mathbf{a}_0^A = \mathbf{0}$. Check: by the chain rule, $\left.\frac{d\mathbf{i}_1}{dt}\right|_0 = \dot\Psi\left(-\sin\Psi\,\mathbf{i}_0 + \cos\Psi\,\mathbf{j}_0\right) = \Omega\,\mathbf{j}_1 = \Omega\,\mathbf{k}_1\times\mathbf{i}_1$.

#### The azimuth $\theta$: horizontal plane through $C$

![[attachments/EM-SOL/p51-horizontal.svg]]

Seen from above ($\mathbf{k}_1$ out of the paper), with $\mathbf{i}_1$ to the right and $\mathbf{j}_1$ up, the centre $C$ is at distance $R$ from the rotation axis on the side of $+\mathbf{j}_1$ (its horizontal position is $R\,\mathbf{j}_1$). The azimuth $\theta$ is measured at $C$ from $\mathbf{i}_1$ towards $\mathbf{j}_1$, counter-clockwise in this view. The horizontal unit vector in that direction is the hypotenuse of the shaded triangle, with the leg $\cos\theta$ along $\mathbf{i}_1$ (adjacent) and $\sin\theta$ along $\mathbf{j}_1$ (opposite), and its derivative with respect to $\theta$ ($\frac{d}{d\theta}\cos\theta = -\sin\theta$, $\frac{d}{d\theta}\sin\theta = \cos\theta$) is the horizontal unit vector of increasing $\theta$:

$$ \mathbf{e}_h = \cos\theta\,\mathbf{i}_1 + \sin\theta\,\mathbf{j}_1, \qquad \mathbf{u}_\theta = \frac{d\mathbf{e}_h}{d\theta} = -\sin\theta\,\mathbf{i}_1 + \cos\theta\,\mathbf{j}_1 $$

(the minus sign: turning $\mathbf{e}_h$ a further $90^\circ$ counter-clockwise takes its tip to the side of $-\mathbf{i}_1$). Also $\mathbf{k}_1\times\mathbf{e}_h = \mathbf{u}_\theta$ and $\mathbf{k}_1\times\mathbf{u}_\theta = -\mathbf{e}_h$.

#### The elevation $\phi$: vertical plane through $C$ and $P$

![[attachments/EM-SOL/p51-vertical.svg]]

$P$ lies in the vertical plane through $C$ that contains $\mathbf{e}_h$; it is drawn with $\mathbf{e}_h$ to the right and $\mathbf{k}_1$ up, so $\mathbf{e}_h\times\mathbf{k}_1 = -\mathbf{u}_\theta$ points out of the paper and $\mathbf{u}_\theta$ points into it ($\otimes$). In the shaded right triangle the hypotenuse is $|CP| = R$, the leg adjacent to $\phi$ is $R\cos\phi$ along $\mathbf{e}_h$ (the distance $CP'$ of the horizontal view) and the leg opposite to $\phi$ is $R\sin\phi$ along $\mathbf{k}_1$. The unit vector from $C$ to $P$ and its derivative with respect to $\phi$ are

$$ \mathbf{u}_r = \cos\phi\,\mathbf{e}_h + \sin\phi\,\mathbf{k}_1 = \cos\phi\cos\theta\,\mathbf{i}_1 + \cos\phi\sin\theta\,\mathbf{j}_1 + \sin\phi\,\mathbf{k}_1 \quad (\text{from } C \text{ to } P) $$
$$ \mathbf{u}_\phi = \frac{\partial\mathbf{u}_r}{\partial\phi} = -\sin\phi\,\mathbf{e}_h + \cos\phi\,\mathbf{k}_1 = -\sin\phi\cos\theta\,\mathbf{i}_1 - \sin\phi\sin\theta\,\mathbf{j}_1 + \cos\phi\,\mathbf{k}_1 \quad (\text{increasing } \phi) $$

while $\frac{\partial\mathbf{u}_r}{\partial\theta} = \cos\phi\,\frac{d\mathbf{e}_h}{d\theta} = \cos\phi\,\mathbf{u}_\theta$, so $\mathbf{u}_\theta = \frac{1}{\cos\phi}\frac{\partial\mathbf{u}_r}{\partial\theta}$ (horizontal, increasing $\theta$).

**Relation with the standard spherical coordinates.** The usual polar angle $\vartheta$ is measured from the upward vertical $\mathbf{k}_1$ (colatitude), with $\mathbf{u}_r = \sin\vartheta\cos\theta\,\mathbf{i}_1 + \sin\vartheta\sin\theta\,\mathbf{j}_1 + \cos\vartheta\,\mathbf{k}_1$. The elevation is measured from the horizontal instead, so $\phi = \frac{\pi}{2} - \vartheta$, and

$$ \sin\vartheta = \sin\left(\tfrac{\pi}{2} - \phi\right) = \sin\tfrac{\pi}{2}\cos\phi - \cos\tfrac{\pi}{2}\sin\phi = \cos\phi, \qquad \cos\vartheta = \cos\left(\tfrac{\pi}{2} - \phi\right) = \cos\tfrac{\pi}{2}\cos\phi + \sin\tfrac{\pi}{2}\sin\phi = \sin\phi $$

which turns the standard $\mathbf{u}_r$ into ours. Because $\phi$ grows upwards while $\vartheta$ grows downwards, $\mathbf{u}_\phi = -\mathbf{u}_\vartheta$.

**Change-of-basis matrix** (columns: $\mathbf{u}_r, \mathbf{u}_\theta, \mathbf{u}_\phi$ in $\mathcal{B}_1$):

$$ [{}_1R_u] = \begin{pmatrix} \cos\phi\cos\theta & -\sin\theta & -\sin\phi\cos\theta \\ \cos\phi\sin\theta & \cos\theta & -\sin\phi\sin\theta \\ \sin\phi & 0 & \cos\phi \end{pmatrix} $$

**Checks:** each column has unit norm ($\cos^2\phi(\cos^2\theta + \sin^2\theta) + \sin^2\phi = 1$, etc.); $\mathbf{u}_r\cdot\mathbf{u}_\theta = -\cos\phi\cos\theta\sin\theta + \cos\phi\sin\theta\cos\theta = 0$, $\mathbf{u}_r\cdot\mathbf{u}_\phi = -\cos\phi\sin\phi + \sin\phi\cos\phi = 0$, $\mathbf{u}_\theta\cdot\mathbf{u}_\phi = \sin\phi\sin\theta\cos\theta - \sin\phi\sin\theta\cos\theta = 0$, so $[{}_1R_u]^T[{}_1R_u] = I$. The determinant is the triple product $\det[{}_1R_u] = \mathbf{u}_r\cdot(\mathbf{u}_\theta\times\mathbf{u}_\phi)$, and $\mathbf{u}_\theta\times\mathbf{u}_\phi = -\sin\phi\,(\mathbf{u}_\theta\times\mathbf{e}_h) + \cos\phi\,(\mathbf{u}_\theta\times\mathbf{k}_1) = \sin\phi\,\mathbf{k}_1 + \cos\phi\,\mathbf{e}_h = \mathbf{u}_r$ (using $\mathbf{u}_\theta\times\mathbf{e}_h = -\mathbf{k}_1$ and $\mathbf{u}_\theta\times\mathbf{k}_1 = \mathbf{e}_h$), hence $\det[{}_1R_u] = \mathbf{u}_r\cdot\mathbf{u}_r = 1$: the triad $\{\mathbf{u}_r, \mathbf{u}_\theta, \mathbf{u}_\phi\}$ is right-handed.

**Useful inverse relations** (read from the two triangles): $\mathbf{e}_h = \cos\phi\,\mathbf{u}_r - \sin\phi\,\mathbf{u}_\phi$, $\mathbf{k}_1 = \sin\phi\,\mathbf{u}_r + \cos\phi\,\mathbf{u}_\phi$, $\mathbf{i}_1 = \cos\theta\,\mathbf{e}_h - \sin\theta\,\mathbf{u}_\theta$, $\mathbf{j}_1 = \sin\theta\,\mathbf{e}_h + \cos\theta\,\mathbf{u}_\theta$; and $\mathbf{k}_1\times\mathbf{e}_h = \mathbf{u}_\theta$, $\mathbf{k}_1\times\mathbf{u}_\theta = -\mathbf{e}_h$, $\mathbf{k}_1\times\mathbf{u}_\phi = -\sin\phi\,\mathbf{u}_\theta$.

**Derivatives in $S_1$** (chain rule, $\theta$ and $\phi$ depend on $t$):

$$ \left.\frac{d\mathbf{u}_r}{dt}\right|_1 = \frac{\partial\mathbf{u}_r}{\partial\theta}\dot{\theta} + \frac{\partial\mathbf{u}_r}{\partial\phi}\dot{\phi} = \dot{\theta}\cos\phi\,\mathbf{u}_\theta + \dot{\phi}\,\mathbf{u}_\phi $$
$$ \left.\frac{d\mathbf{u}_\theta}{dt}\right|_1 = -\dot{\theta}\,\mathbf{e}_h = -\dot{\theta}\left(\cos\phi\,\mathbf{u}_r - \sin\phi\,\mathbf{u}_\phi\right), \qquad \left.\frac{d\mathbf{u}_\phi}{dt}\right|_1 = -\dot{\phi}\cos\phi\,\mathbf{e}_h - \sin\phi\,\dot{\theta}\,\mathbf{u}_\theta - \dot{\phi}\sin\phi\,\mathbf{k}_1 = -\dot{\phi}\,\mathbf{u}_r - \dot{\theta}\sin\phi\,\mathbf{u}_\theta $$

#### Position vector

To reach $P$ from $A$ we pass through the centre $C$, because the distance from $C$ is the one that stays constant:

$$ \mathbf{r}_1^P = \overrightarrow{AC} + \overrightarrow{CP} = R\left(\mathbf{j}_1 + \mathbf{k}_1\right) + R\,\mathbf{u}_r $$

In components of $\mathcal{B}_1$: $x_1 = R\cos\phi\cos\theta$, $y_1 = R(1 + \cos\phi\sin\theta)$, $z_1 = R(1 + \sin\phi)$.

### Kinematics

##### (a) Position, velocity and acceleration of $P$ relative to $S_1$
* **Pedagogical Justification:** relative quantities are derivatives in $S_1$; $\mathbf{r}_1^C$ is constant in $S_1$ and only $\mathbf{u}_r$ changes, through $\theta(t)$ and $\phi(t)$.
$$ \boxed{\mathbf{r}_1^P = \mathbf{r}_1^C + \overrightarrow{CP} = R\left(\mathbf{j}_1 + \mathbf{k}_1\right) + R\,\mathbf{u}_r} $$

$$ \boxed{\mathbf{v}_1^P = R\left.\frac{d\mathbf{u}_r}{dt}\right|_1 = R\dot{\theta}\cos\phi\,\mathbf{u}_\theta + R\dot{\phi}\,\mathbf{u}_\phi} $$

Differentiating again in $S_1$ (product rule, $\frac{d}{dt}(\dot{\theta}\cos\phi) = \ddot{\theta}\cos\phi - \dot{\theta}\dot{\phi}\sin\phi$, and the basis derivatives of the change-of-basis section):

$$ \mathbf{a}_1^P = R\left(\ddot{\theta}\cos\phi - \dot{\theta}\dot{\phi}\sin\phi\right)\mathbf{u}_\theta + R\dot{\theta}\cos\phi\left[-\dot{\theta}\left(\cos\phi\,\mathbf{u}_r - \sin\phi\,\mathbf{u}_\phi\right)\right] + R\ddot{\phi}\,\mathbf{u}_\phi + R\dot{\phi}\left(-\dot{\phi}\,\mathbf{u}_r - \dot{\theta}\sin\phi\,\mathbf{u}_\theta\right) $$

Collecting components:

$$ \boxed{\mathbf{a}_1^P = -R\left(\dot{\phi}^2 + \dot{\theta}^2\cos^2\phi\right)\mathbf{u}_r + R\left(\ddot{\theta}\cos\phi - 2\dot{\theta}\dot{\phi}\sin\phi\right)\mathbf{u}_\theta + R\left(\ddot{\phi} + \dot{\theta}^2\sin\phi\cos\phi\right)\mathbf{u}_\phi} $$

### Forces and Equations of Motion

##### (b) Forces on $P$ seen from $S_1$
* **Pedagogical Justification:** in $S_1$, Notes Eq. 4.63 reads $m\mathbf{a}_1^P = \mathbf{F} + \mathbf{F}_i$, where $\mathbf{F}_i$ (Notes Eq. 4.62) has four terms (Slide 28). We evaluate each with $\mathbf{a}_0^A = \mathbf{0}$, $\boldsymbol{\omega}_{10} = \Omega\mathbf{k}_1$, $\boldsymbol{\alpha}_{10} = \dot{\Omega}\mathbf{k}_1$, and project on the spherical basis.

**Actual forces.**

* Weight: $m\mathbf{g} = -mg\,\mathbf{k}_1 = -mg\sin\phi\,\mathbf{u}_r - mg\cos\phi\,\mathbf{u}_\phi$.
* Reaction (smooth, unilateral, toward $C$, as drawn in the vertical view): $\mathbf{N} = -N\,\mathbf{u}_r$, $N \ge 0$ while in contact.

**Fictitious forces.** Only the part of $\mathbf{r}_1^P$ normal to $\mathbf{k}_1$ enters the cross products with $\mathbf{k}_1$. That part is $\mathbf{r}_\perp = x_1\mathbf{i}_1 + y_1\mathbf{j}_1$; substituting $\mathbf{i}_1 = \cos\theta\,\mathbf{e}_h - \sin\theta\,\mathbf{u}_\theta$ and $\mathbf{j}_1 = \sin\theta\,\mathbf{e}_h + \cos\theta\,\mathbf{u}_\theta$:

$$ \mathbf{r}_\perp = R\left[\cos\phi\cos^2\theta + \sin\theta + \cos\phi\sin^2\theta\right]\mathbf{e}_h + R\left[-\cos\phi\cos\theta\sin\theta + \cos\theta + \cos\phi\sin\theta\cos\theta\right]\mathbf{u}_\theta = R\left(\cos\phi + \sin\theta\right)\mathbf{e}_h + R\cos\theta\,\mathbf{u}_\theta $$
* **Origin force:** $\mathbf{F}_A = -m\mathbf{a}_0^A = \mathbf{0}$.
* **Euler force** (Slide 31), with $\mathbf{k}_1\times\mathbf{e}_h = \mathbf{u}_\theta$, $\mathbf{k}_1\times\mathbf{u}_\theta = -\mathbf{e}_h$:
$$ \mathbf{F}_E = -m\dot{\Omega}\,\mathbf{k}_1\times\mathbf{r}_\perp = -m\dot{\Omega}R\left[\left(\cos\phi + \sin\theta\right)\mathbf{u}_\theta - \cos\theta\,\mathbf{e}_h\right] $$
$$ \mathbf{F}_E = m\dot{\Omega}R\left[\cos\theta\cos\phi\,\mathbf{u}_r - \left(\cos\phi + \sin\theta\right)\mathbf{u}_\theta - \cos\theta\sin\phi\,\mathbf{u}_\phi\right] $$
* **Centrifugal force** (Slide 30), $\mathbf{F}_C = m\Omega^2\mathbf{r}_\perp$:
$$ \mathbf{F}_C = m\Omega^2R\left[\left(\cos\phi + \sin\theta\right)\cos\phi\,\mathbf{u}_r + \cos\theta\,\mathbf{u}_\theta - \left(\cos\phi + \sin\theta\right)\sin\phi\,\mathbf{u}_\phi\right] $$
* **Coriolis force** (Slide 31): $\mathbf{k}_1\times\mathbf{v}_1^P = R\dot{\theta}\cos\phi\left(-\mathbf{e}_h\right) + R\dot{\phi}\left(-\sin\phi\,\mathbf{u}_\theta\right)$, so
$$ \mathbf{F}_{COR} = -2m\Omega\,\mathbf{k}_1\times\mathbf{v}_1^P = 2m\Omega R\left(\dot{\theta}\cos\phi\,\mathbf{e}_h + \dot{\phi}\sin\phi\,\mathbf{u}_\theta\right) = 2m\Omega R\left[\dot{\theta}\cos^2\phi\,\mathbf{u}_r + \dot{\phi}\sin\phi\,\mathbf{u}_\theta - \dot{\theta}\sin\phi\cos\phi\,\mathbf{u}_\phi\right] $$

As required, $\mathbf{F}_{COR}\cdot\mathbf{v}_1^P = 2m\Omega R^2\left(\dot{\phi}\sin\phi\,\dot{\theta}\cos\phi - \dot{\theta}\sin\phi\cos\phi\,\dot{\phi}\right) = 0$.

##### (c) Two differential equations for $\theta$ and $\phi$
* **Pedagogical Justification:** the reaction is along $\mathbf{u}_r$, so the projections of Notes Eq. 4.63 on $\mathbf{u}_\theta$ and $\mathbf{u}_\phi$ contain no unknown force.

**Projection on $\mathbf{u}_\theta$** (weight and reaction have no $\mathbf{u}_\theta$ component):

$$ mR\left(\ddot{\theta}\cos\phi - 2\dot{\theta}\dot{\phi}\sin\phi\right) = m\Omega^2R\cos\theta - m\dot{\Omega}R\left(\cos\phi + \sin\theta\right) + 2m\Omega R\dot{\phi}\sin\phi $$
$$ \boxed{\ddot{\theta}\cos\phi - 2\dot{\phi}\sin\phi\left(\dot{\theta} + \Omega\right) = \Omega^2\cos\theta - \dot{\Omega}\left(\cos\phi + \sin\theta\right)} $$

**Projection on $\mathbf{u}_\phi$:**

$$ mR\left(\ddot{\phi} + \dot{\theta}^2\sin\phi\cos\phi\right) = -mg\cos\phi - m\Omega^2R\left(\cos\phi + \sin\theta\right)\sin\phi - m\dot{\Omega}R\cos\theta\sin\phi - 2m\Omega R\dot{\theta}\sin\phi\cos\phi $$
$$ \boxed{\ddot{\phi} + \dot{\theta}\left(\dot{\theta} + 2\Omega\right)\sin\phi\cos\phi + \frac{g}{R}\cos\phi + \Omega^2\sin\phi\left(\cos\phi + \sin\theta\right) + \dot{\Omega}\cos\theta\sin\phi = 0} $$

These two coupled, non-linear ODEs with the known forcing $\Omega(t)$ determine $\theta(t)$, $\phi(t)$ from the initial conditions.

**Projection on $\mathbf{u}_r$** (it contains the only unknown force, $N$):

$$ -mR\left(\dot{\phi}^2 + \dot{\theta}^2\cos^2\phi\right) = -N - mg\sin\phi + m\Omega^2R\cos\phi\left(\cos\phi + \sin\theta\right) + m\dot{\Omega}R\cos\theta\cos\phi + 2m\Omega R\dot{\theta}\cos^2\phi $$

### Answers and Checks

##### (a) Kinematics
$\mathbf{r}_1^P$, $\mathbf{v}_1^P$ and $\mathbf{a}_1^P$ are the three boxed expressions of the kinematics section, with $\mathbf{u}_r, \mathbf{u}_\theta, \mathbf{u}_\phi$ defined in the change-of-basis section.

##### (b) Forces
Weight $-mg\,\mathbf{k}_1$, reaction $-N\,\mathbf{u}_r$, origin force $\mathbf{0}$, and the Euler, centrifugal and Coriolis forces written above.

##### (c) Equations of motion
The two boxed equations for $\theta$ and $\phi$.

##### (d) Reaction and separation condition
From the projection on $\mathbf{u}_r$:

$$ \boxed{N = mR\left(\dot{\phi}^2 + \dot{\theta}^2\cos^2\phi\right) - mg\sin\phi + m\Omega^2R\cos\phi\left(\cos\phi + \sin\theta\right) + m\dot{\Omega}R\cos\phi\cos\theta + 2m\Omega R\dot{\theta}\cos^2\phi} $$

Grouping $\dot{\theta}^2 + 2\Omega\dot{\theta} + \Omega^2 = (\dot{\theta} + \Omega)^2$ in the $\cos^2\phi$ terms gives the equivalent compact form

$$ N = mR\dot{\phi}^2 + mR\cos^2\phi\left(\dot{\theta} + \Omega\right)^2 + m\Omega^2R\cos\phi\sin\theta + m\dot{\Omega}R\cos\phi\cos\theta - mg\sin\phi $$

It depends only on $\theta, \dot{\theta}, \phi, \dot{\phi}$ and the known $m, R, g, \Omega(t), \dot{\Omega}(t)$. **Separation:** the surface can only push ($N \ge 0$). The particle leaves the surface at the first instant at which

$$ \boxed{N\left(\theta, \dot{\theta}, \phi, \dot{\phi}, t\right) = 0 \ \text{ and would become negative}} $$

i.e. the motion predicted by (c) is valid only while $N \ge 0$.

##### (e) Equilibrium configurations for $\Omega = \text{const}$
* **Pedagogical Justification:** equilibrium in $S_1$ means $\theta$, $\phi$ constant: $\dot{\theta} = \dot{\phi} = \ddot{\theta} = \ddot{\phi} = 0$, with $\dot{\Omega} = 0$. Then $\mathbf{F}_E = \mathbf{F}_{COR} = \mathbf{0}$ and the equations of (c) become algebraic. We take $\Omega \neq 0$ (the case $\Omega = 0$ is discussed at the end).

From the $\theta$ equation: $\Omega^2\cos\theta = 0 \Rightarrow \cos\theta = 0$, so $\theta = \pi/2$ or $\theta = -\pi/2$: $P$ must lie in the vertical plane $x_1 = 0$ that contains the rotation axis and $C$ (otherwise the centrifugal force has a component $m\Omega^2R\cos\theta$ along $\mathbf{u}_\theta$ that nothing balances).

From the $\phi$ equation, multiplied by $R$: $g\cos\phi + \Omega^2R\sin\phi(\cos\phi + \sin\theta) = 0$. The poles $\cos\phi = 0$ do not satisfy it ($\Omega^2R\sin\phi\sin\theta = \pm\Omega^2R \neq 0$), so we can divide by $g\cos\phi \gt 0$. With the dimensionless number $\lambda = \Omega^2R/g \gt 0$:

**Branch 1, $\theta = \pi/2$** (far side of the sphere from the axis, $y_1 = R(1 + \cos\phi) \ge R$):

$$ 1 + \lambda\,\frac{\sin\phi\left(\cos\phi + 1\right)}{\cos\phi} = 0 \quad\Longleftrightarrow\quad \boxed{\tan\phi_1 + \sin\phi_1 = -\frac{g}{\Omega^2R}} $$

The function $f(\phi) = \tan\phi + \sin\phi$ is strictly increasing on $(-\pi/2, \pi/2)$ ($f' = \sec^2\phi + \cos\phi \gt 0$), goes from $-\infty$ to $+\infty$ and vanishes at $0$; so there is **exactly one root, $\phi_1 \in (-\pi/2, 0)$**, below the horizontal plane of $C$.

**Branch 2, $\theta = -\pi/2$** (side of the sphere next to the axis, $y_1 = R(1 - \cos\phi)$):

$$ 1 + \lambda\,\frac{\sin\phi\left(\cos\phi - 1\right)}{\cos\phi} = 0 \quad\Longleftrightarrow\quad \boxed{\tan\phi_2 - \sin\phi_2 = \frac{g}{\Omega^2R}} $$

$h(\phi) = \tan\phi - \sin\phi$ has $h' = \sec^2\phi - \cos\phi \ge 0$ (zero only at $\phi = 0$), $h(0) = 0$ and $h \to +\infty$ as $\phi \to \pi/2$, so there is **exactly one root, $\phi_2 \in (0, \pi/2)$**, above the horizontal plane of $C$.

**Reaction at equilibrium.** With $\dot{\theta} = \dot{\phi} = \dot{\Omega} = 0$, (d) gives $N = m\Omega^2R\cos\phi(\cos\phi + \sin\theta) - mg\sin\phi$. The equilibrium relation $\Omega^2R(\cos\phi + \sin\theta) = -g\cos\phi/\sin\phi$ ($\sin\phi \neq 0$ at both roots) turns it into

$$ N = -\frac{mg\cos^2\phi}{\sin\phi} - mg\sin\phi = -\frac{mg\left(\cos^2\phi + \sin^2\phi\right)}{\sin\phi} \quad\Longrightarrow\quad \boxed{N = -\frac{mg}{\sin\phi}} $$

This is simply the vertical balance: the centrifugal force is horizontal, so the vertical component of $\mathbf{N} = -N\mathbf{u}_r$, which is $-N\sin\phi$ (the leg $\sin\phi$ of the vertical-view triangle), must cancel the weight.

**Discussion.**

* **Branch 1** ($\theta = \pi/2$, $\phi_1 \lt 0$): $N_1 = mg/|\sin\phi_1| \gt 0$. **This is the only physically possible equilibrium.** The particle sits in the lower half of the sphere, on the side away from the axis, where the inward normal $-\mathbf{u}_r$ points up and toward the axis, balancing the weight and the outward centrifugal force. As $\Omega$ grows, $\phi_1$ rises toward the equator of the sphere: for $\lambda \gg 1$, $\phi_1 \approx -g/(2\Omega^2R)$ and $N_1 \approx 2m\Omega^2R$ (the centrifugal force at distance $2R$ from the axis); for $\Omega \to 0$, $\phi_1 \to -\pi/2$ (bottom) and $N_1 \to mg$. Example ($R = 1$ m, $g = 9.81$ m/s$^2$): $\Omega = 3$ rad/s gives $\phi_1 = -30.3^\circ$ and $N_1 = 1.98\,mg$.
* **Branch 2** ($\theta = -\pi/2$, $\phi_2 \gt 0$): $N_2 = -mg/\sin\phi_2 \lt 0$. It solves the equations of (c), but the reaction would have to **pull** the particle away from $C$, which the inner surface cannot do: it is **not an admissible equilibrium** for the unilateral contact (it would be one for a particle held on both sides of the surface, or resting on the outside of the sphere). On that side the centrifugal force points toward the inside of the sphere, so it cannot help the surface to hold the particle up.
* **Stability of branch 1** (extension, using the energy in $S_1$). For constant $\Omega$, $A$ fixed and a smooth sphere fixed in $S_1$, the energy $E_1^P = T_1^P + V_1$ is conserved (Slides 29–31), with $V_1 = mgz_1 - \tfrac12 m\Omega^2(x_1^2 + y_1^2) = mgR(1 + \sin\phi) - \tfrac12 m\Omega^2R^2\left(1 + \cos^2\phi + 2\cos\phi\sin\theta\right)$. Its derivatives $\partial V_1/\partial\theta = -m\Omega^2R^2\cos\phi\cos\theta$ and $\partial V_1/\partial\phi = mgR\cos\phi + m\Omega^2R^2\sin\phi(\cos\phi + \sin\theta)$ reproduce the equilibrium equations. At branch 1, $\partial^2V_1/\partial\theta^2 = m\Omega^2R^2\cos\phi_1\sin\theta = m\Omega^2R^2\cos\phi_1 \gt 0$, $\partial^2V_1/\partial\theta\partial\phi = m\Omega^2R^2\sin\phi_1\cos\theta = 0$ and $\partial^2V_1/\partial\phi^2 = mgR\lambda\cos\phi_1\left(\sec^2\phi_1 + \cos\phi_1\right) \gt 0$: $V_1$ has a strict minimum, so the equilibrium is stable (the linearised equations give purely imaginary eigenvalues, see the verification).
* **Case $\Omega = 0$:** the $\theta$ equation is satisfied identically and the $\phi$ equation gives $\cos\phi = 0$: the bottom point $\phi = -\pi/2$ with $N = mg$ (the top point $\phi = \pi/2$ would need $N = -mg \lt 0$); $\theta$ is undefined there (pole of the coordinates).

##### Checks
* **Role of each inertia force.** The centrifugal force pushes $P$ away from the axis and is responsible for the tilt of the equilibrium; the Euler force (only while $\Omega$ changes) drags $P$ against the sense of the angular acceleration, along $-\mathbf{u}_\theta$-like directions; the Coriolis force couples the two angular motions (terms $2\Omega\dot{\phi}\sin\phi$ and $2\Omega\dot{\theta}\sin\phi\cos\phi$) and does no work.
* **Absolute reading of $N$.** In the compact form, $\dot{\theta} + \Omega$ is the absolute azimuthal rate of the particle about the vertical through $C$, so $mR\dot{\phi}^2 + mR\cos^2\phi(\dot{\theta} + \Omega)^2$ is the centripetal demand of the absolute motion on the sphere.
* **Limit $\Omega \to 0$:** the equations reduce to those of the spherical pendulum, $\ddot{\theta}\cos\phi - 2\dot{\theta}\dot{\phi}\sin\phi = 0$ and $\ddot{\phi} + \dot{\theta}^2\sin\phi\cos\phi + (g/R)\cos\phi = 0$, and $N = mR(\dot{\phi}^2 + \dot{\theta}^2\cos^2\phi) - mg\sin\phi$.
* **Dimensions:** in (c) every term is $\text{s}^{-2}$ ($[\ddot{\theta}] = [\Omega^2] = [\dot{\Omega}] = [\Omega\dot{\phi}] = [g/R] = \text{s}^{-2}$); in (d) every term is $\text{kg}\,\text{m}\,\text{s}^{-2} = \text{N}$; $\lambda = \Omega^2R/g$ is dimensionless.
* **Verification (sympy):** with a general $\Psi(t)$, $\dot{\Psi} = \Omega(t)$, the inertial double derivative of $[{}_0R_1]\{\mathbf{r}_1^P\}$ equals the Notes Eq. 3.27 decomposition; solving $m\mathbf{a}_0^P = -mg\mathbf{k}_1 - N\mathbf{u}_r$ in $S_0$ returns exactly the two equations of (c) and the $N$ of (d); for $\Omega = 1, 3, 10$ rad/s ($R = 1$ m) both branches satisfy the equations with $N = -mg/\sin\phi$, branch 1 has $N \gt 0$ and purely imaginary eigenvalues, branch 2 has $N \lt 0$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 51 in its solution keys, so the results are verified by independent derivation (the sympy check recorded above).

