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
> The plane of the curve is drawn with the horizontal axis to the right and $\mathbf j_0$ up. For the fixed curve the horizontal axis is $OX$ with $\mathbf i_0$; for the turning curve the same drawing holds in $S_1$ with $OX_1$, $\mathbf i_1$ and $x_1$. The position of $P$ is the sum of its two dashed components: the abscissa along the horizontal axis and the height given by the equation of the curve. Moving a distance $dx_1$ along the axis, the height changes by $dy$; in the shaded right triangle the leg adjacent to the tangent angle $\alpha$ is $dx_1$, the opposite leg is $dy$ and the hypotenuse is the arc element $d\ell$ (Eq. 2.19, where it is called $ds$; here $s$ is the sine of the shorthand).
>
> $$\begin{aligned}
> \mathbf r_1^P &= x_1\,\mathbf i_1 + a\left(1 - \cos\frac{x_1}{a}\right)\mathbf j_1 \quad &\text{(abscissa plus height on the curve)} \\
> \frac{d}{dx_1}\cos\frac{x_1}{a} &= -\sin\frac{x_1}{a}\cdot\frac{d}{dx_1}\left(\frac{x_1}{a}\right) = -\frac{1}{a}\sin\frac{x_1}{a} \quad &\text{(chain rule)} \\
> \frac{dy}{dx_1} &= a\cdot\frac{1}{a}\sin\frac{x_1}{a} = s \quad &\text{(derivative of the height; shorthand $s$)} \\
> d\ell^2 &= dx_1^2 + dy^2 = \left(1 + s^2\right)dx_1^2 \quad &\text{(Pythagoras in the slope triangle)} \\
> d\ell &= D\,dx_1, \quad \cos\alpha = \frac{dx_1}{d\ell} = \frac{1}{D}, \quad \sin\alpha = \frac{dy}{d\ell} = \frac{s}{D} \quad &\text{(adjacent and opposite legs over the hypotenuse)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = x_1\,\mathbf i_1 + a\left(1 - \cos\frac{x_1}{a}\right)\mathbf j_1, \qquad \frac{d\ell}{dx_1} = D = \sqrt{1 + \sin^2\frac{x_1}{a}}, \qquad \tan\alpha = \sin\frac{x_1}{a}}$$
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
> \mathbf e_t &= \cos\alpha\,\mathbf i_1 + \sin\alpha\,\mathbf j_1 = \frac{\mathbf i_1 + s\,\mathbf j_1}{D} \quad &\text{(right triangle of $\mathbf e_t$; Eq. 2.9: $d\mathbf r/d\ell$)} \\
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
> To reach the crest the radicand must not be negative on the whole way from 0 to $\pi a$; it decreases with $x$ there, because $1 - \cos(x/a)$ grows, so the condition is its value at the crest. At the limiting speed write $\delta$ for the distance $\pi a - x$ still to go; the half-angle identity is $1 + \cos\beta = 2\cos^2(\beta/2)$.
>
> $$\begin{aligned}
> v_0^2 - 2ga\left(1 - \cos\pi\right) &= v_0^2 - 4ga \ge 0 \quad &\text{(radicand at $x = \pi a$; $\cos\pi = -1$)} \\
> v_0 &\ge 2\sqrt{ga} \quad &\text{(positive root, $v_0 \gt 0$)} \\
> v_0^2 - 2ga\left(1 - \cos\frac{x}{a}\right) &= 2ga\left(1 + \cos\frac{x}{a}\right) = 4ga\cos^2\frac{x}{2a} \quad &\text{(case $v_0^2 = 4ga$; half-angle identity)} \\
> \cos\frac{x}{2a} &= \cos\left(\frac{\pi}{2} - \frac{\delta}{2a}\right) = \sin\frac{\delta}{2a} \simeq \frac{\delta}{2a} \quad &\text{(difference formula; small $\delta$)} \\
> \sqrt{\frac{1 + \sin^2(x/a)}{4ga\cos^2(x/2a)}} &\simeq \sqrt{\frac{1}{4ga}}\cdot\frac{2a}{\delta} = \sqrt{\frac{a}{g}}\,\frac{1}{\delta} \quad &\text{(integrand of the quadrature near the crest; $\sin(x/a) \simeq 0$)} \\
> \int_{\delta}^{\delta_1}\sqrt{\frac{a}{g}}\,\frac{d\delta'}{\delta'} &= \sqrt{\frac{a}{g}}\left[\ln \delta'\right]_{\delta}^{\delta_1} = \sqrt{\frac{a}{g}}\,\ln\frac{\delta_1}{\delta} \to \infty \ \ (\delta \to 0) \quad &\text{(time from a point at $\delta_1$ to a point at $\delta$: antiderivative $\ln \delta'$, Barrow's rule)}
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
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> The energy in $S_1$ is conserved for two reasons. First, the forces that do no work in $S_1$: the reaction, because the curve is smooth and at rest in $S_1$, so the reaction is normal to the relative velocity; the Coriolis force, always normal to the relative velocity; and the force of the origin and the Euler force, which vanish. Second, the forces that do work have potentials that depend on the position only: the weight, and the centrifugal force, whose potential is minus one half of $m\Omega^2x_1^2$ only because $\Omega$ is constant.
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
> $$\boxed{g\sin\frac{x_1}{a} = \Omega^2x_1: \ \ x_1 = 0 \text{ for every } \Omega; \ \text{a symmetric pair } \pm x_1^* \ \text{with } 0 \lt x_1^* \lt \pi a \text{ exactly when } 0 \lt \Omega^2a \lt g}$$
>
> **Units:** $[g] = [\Omega^2x_1] = [\mathrm{L\,T^{-2}}]$; $\lambda$ dimensionless
> **Meaning:** at an off-axis equilibrium the tangential pull of the weight towards the bottom balances the tangential push of the centrifugal force; with a fast spin no off-axis balance exists inside the range of the curve.

#### (g) Variable spin rate

> [!derivation] Energy in the turning frame when Omega depends on time
> **Law:** inertia forces with a variable angular velocity; power of each force on the relative velocity; product rule
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.62; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]
>
> With $\Omega(t)$ the Euler force appears. It is normal to the plane of the curve, so it does no work in $S_1$ and drops out of the tangent equation, which keeps its form with $\Omega(t)$; it only changes the reaction along $\mathbf k_1$. The centrifugal force, however, no longer derives from a potential that depends on the position only. Write $E_1^P$ for the energy of part (e) with $\Omega(t)$ in its centrifugal term: the bracket of the last row below, the relative kinetic energy plus the potential of the weight minus one half of $m\Omega^2x_1^2$.
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
| (d) Moving frame and inertia force | (answered in Forces and Equations of Motion, before (a)–(c)) $S_1$: $\mathbf i_1$ in the plane of the curve, $\mathbf j_1 = \mathbf j_0$ the axis, $\mathbf k_1$ normal to the plane; $\mathbf F_i = m\Omega^2x_1\,\mathbf i_1 + 2m\Omega\dot x_1\,\mathbf k_1$ |
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
| Readings | $\dot\nu \gt 0$ (the spacecraft moves towards growing $\nu$; with $\dot\nu \lt 0$ the unit tangent of part (b) changes sign). Hypothesis: the spacecraft is in free flight about $F$, which the conic orbit of Notes.pdf, Eq. 8.14 suggests but does not imply (the statement prescribes $\nu(t)$ and gives no force on $S$); parts (e) and (f) are given both in general and under this hypothesis |

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
> Write $E_0^P$ for the energy in $S_0$: the kinetic energy computed with the absolute velocity plus the potential of the weight. Of the forces in $S_0$ only the weight has a potential, so the rate of $E_0^P$ is the power of the reaction (Eq. 4.11).
>
> $$\begin{aligned}
> E_0^P &= \tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P + mga\left(1 - \cos\theta\right) = \tfrac12 m\left(a^2\dot\theta^2 + \Omega^2a^2\sin^2\theta\right) + mga\left(1 - \cos\theta\right) \quad &\text{(absolute velocity box: $\mathbf e_t$ and $\mathbf k_1$ orthogonal)} \\
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
| Readings | the wire equation is numerical, with $x_1$ and $y_1$ in metres (the rail at 2 m); the natural length of the spring is taken as zero, as the energy integral of the key implies (with a natural length $\ell_0$, replace 2 by $2 - \ell_0$ in the spring terms; the bounds on $\lambda$ in part (d) then shift by $\ell_0$) |

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

> [!derivation] Scaled potential and allowed region
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
> \tilde V''(x_c) &= -2\sin x_c - 2\beta_c \lt 0 \quad &\text{(a maximum: it needs $\sin x_c \gt 0$, so $x_c$ lies between $2\pi$ and $5\pi/2$, beyond the trough; a stationary point between $\pi$ and $2\pi$, where the sine is negative, is a minimum)} \\
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
> First figure: the vertical plane through $Az'$ and the cord, with $\mathbf u$ its horizontal unit vector from the axis towards $P$. In the shaded right triangle the hypotenuse is the cord $L$; the angle $\varphi$ is at $A$, measured from the upward vertical, so the adjacent leg is vertical, $L\cos\varphi$ along $\mathbf k$, and the opposite leg is horizontal, $L\sin\varphi$ along $\mathbf u$. The standard polar angle of $P$ in that plane, measured from $\mathbf u$, is $\pi/2 - \varphi$: the latitude, which is the angle called $\varphi$ in the spherical coordinates of Notes.pdf, Eq. 2.31, while the $\varphi$ of the statement is the colatitude, measured from the vertical. Second figure (below): the view from above, $\mathbf k$ out of the paper (⊙), $Ax'$ to the right and $Ay'$ up; the horizontal projection, of length $L\sin\varphi$, makes the azimuth $\theta$ with $Ax'$: adjacent leg along $\mathbf i$, opposite leg along $\mathbf j$.
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
> $\mathbf e_\varphi$ is the direction in which $P$ moves when $\varphi$ grows: in the meridian plane, perpendicular to the cord, pointing down and away from the axis (the minus sign of its $\mathbf k$ component: $\varphi$ is measured from the upward vertical, so a growing $\varphi$ lowers the particle). Because the Notes measure the latitude, the unit vector of their Eq. 2.32 to Eq. 2.34 for that angle is minus the $\mathbf e_\varphi$ of the statement; $\mathbf e_r$ and $\mathbf e_\theta$ are the same. $\mathbf e_\theta$ is $\mathbf u$ turned by a quarter turn counterclockwise about $\mathbf k$ in the view from above (⊙): the horizontal part $\cos\theta\,\mathbf i$ turns into $\cos\theta\,\mathbf j$, and $\sin\theta\,\mathbf j$ turns into minus $\sin\theta\,\mathbf i$ (the minus sign).
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
> Eq. 2.33 is written with the latitude of the Notes; with the colatitude of the statement its angle is replaced by $\pi/2 - \varphi$ and its polar unit vector by minus $\mathbf e_\varphi$, which is what the rows below do directly from the partial derivatives.
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
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 4.48
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
> **Meaning:** the quantity is the vertical component of the angular momentum about $A$ computed with the relative velocity (Eq. 4.48). Its conservation comes from the $\mathbf e_\theta$ equation of $S_1$, which contains no force: the tension lies along $\mathbf e_r$, and the weight plus the inertia force of the moving support form a vertical effective weight with no $\mathbf e_\theta$ component. It is not taken from the theorem of a fixed point, because $A$ accelerates.

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

A particle $P$ of mass $m$ slides on a smooth quarter circumference of radius $R$ and centre $O$, drawn in the plane $X_1Z_1$ of a frame that turns with the constant rate $\omega$ about the vertical axis through the point $(-R, 0, 0)$ of that frame; a spring of constant $K$ joins $P$ to the point $B$ of that frame, and gravity is neglected (Problems.pdf, p. 18). The statement asks for the relative velocity and acceleration in the path basis, the three components of Newton's second law, the energy equation of the relative motion, the value of $\alpha$ that gives an equilibrium at $\pi/6$, the types of motion with that value, and the maximum height after the particle leaves the arc. The arc and the point $B$ are at rest in the turning frame, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{Q;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, origin $Q$ on the rotation axis at the height of $O$, $\mathbf k_0$ vertical, up; it plays the role of the inertial frame $OXYZ$ of the statement (see Readings) |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $OX_1Y_1Z_1$ of the statement, attached to the arc: $\mathbf i_1$ horizontal, from the axis through $O$; $\mathbf k_1 = \mathbf k_0$; $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$; $\mathbf i_1 = \mathbf i_0$ at $t = 0$ |
| Points fixed in $S_1$ | $O$ (centre of the arc), at distance $R$ from the axis; $Q$, at $-R\,\mathbf i_1$ from $O$ (upper end of the arc); $B$, at $-2R\,\mathbf i_1$ from $O$ |
| Path basis | $\{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$ at $P$: tangent in the sense of growing $\phi$, principal normal towards the centre of curvature $O$, binormal (deduced below) |
| Coordinate | $\phi$, angle at $O$ between $\overline{OP}$ and the negative $z_1$ axis, $0 \le \phi \le \pi/2$ |
| Constraints | $y_1 = 0$ and $x_1^2 + z_1^2 = R^2$ (quarter with $x_1 \le 0$, $z_1 \le 0$): two holonomic, smooth, bilateral constraints, fixed in $S_1$ |
| Degrees of freedom | 3 minus 2: 1, the coordinate $\phi(t)$, while $P$ is on the arc; 3 after it leaves the arc (part (f)) |
| Data | $m$ [kg], $R$ [m], $\omega$ [rad s$^{-1}$], $K = \alpha m\omega^2$ [N m$^{-1}$]; $\alpha$, $\beta$ positive numbers [1] |
| Initial conditions | $\phi(0) = 0$; relative velocity $-\beta\omega R\,\mathbf i_1$ |
| Unknowns | $\phi(t)$; the reaction $\mathbf N = N_n\,\mathbf e_n + N_b\,\mathbf e_b$ (no tangential component: smooth arc) |
| Applied forces | spring only (no gravity) |
| Inertia forces (in $S_1$) | of the origin, Euler, centrifugal and Coriolis (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; $\omega$ constant; smooth arc acting as a bead on a wire; massless linear spring |
| Readings | (1) The origin $O$ of the statement's inertial frame cannot be the centre of the arc, which moves on a circle; the fixed origin is taken at $Q$, on the axis. Any fixed origin gives the same velocities and accelerations. (2) No natural length is given: the spring is taken with zero natural length, force $-K$ times the vector from $B$ to $P$. With a natural length $\ell_0$ the spring potential becomes $\frac12 K\left(R\sqrt{5 - 4\sin\phi} - \ell_0\right)^2$ and every spring term below changes. (3) The arc ends at $\phi = 0$ (on the $-z_1$ axis) and at $\phi = \pi/2$ (on the rotation axis), as drawn |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p30-top-view.svg]]

> [!derivation] Basis of the turning frame: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙), with the axis at $Q$. With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page (right-hand rule: thumb towards the reader, the fingers turn $\mathbf i_0$ counterclockwise by a quarter turn). A positive $\omega$ turns the frame counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ up the page, along plus $\mathbf j_0$ (no minus sign). $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf j_0$, and the counterclockwise turn carries its tip to the left, so the opposite leg $\sin\omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\omega t\cos\omega t - \left(-\sin\omega t\right)\sin\omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** it is the matrix of Eq. 1.20 with the angle $\omega t$; the vertical keeps its direction, so heights are the same in both frames.

![[attachments/EM-SOL/p30-arc-plane.svg]]

> [!derivation] Position vector of P in the plane of the arc
> **Law:** position as the sum of its legs; right triangle; relation with the standard polar angle
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 18
>
> The plane $X_1Z_1$, fixed in $S_1$, is drawn with $\mathbf i_1$ to the right and $\mathbf k_1$ up; the direction out of the paper is the cross product of $\mathbf i_1$ and $\mathbf k_1$, which is minus $\mathbf j_1$, so $\mathbf j_1$ points into the paper (⊗). Let $F$ be the point of the $z_1$ axis at the height of $P$. In the shaded right triangle $OFP$ (right angle at $F$) the hypotenuse is $OP$, of length $R$, and the angle at $O$ is $\phi$: the adjacent leg $OF$ has length $R\cos\phi$ and points down, the opposite leg $FP$ has length $R\sin\phi$ and points to the left, towards $B$. The standard polar angle $\vartheta$ of the plane, measured from $\mathbf i_1$ towards $\mathbf k_1$, is minus the sum of a quarter turn and $\phi$.
>
> $$\begin{aligned}
> \mathbf r_1^P &= \overrightarrow{OF} + \overrightarrow{FP} = -R\cos\phi\,\mathbf k_1 - R\sin\phi\,\mathbf i_1 \quad &\text{(the two legs, with their directions)} \\
> \cos\vartheta &= \cos\left(\tfrac{\pi}{2} + \phi\right) = \cos\tfrac{\pi}{2}\cos\phi - \sin\tfrac{\pi}{2}\sin\phi = -\sin\phi \quad &\text{($\vartheta = -\pi/2 - \phi$; cosine even; sum formula)} \\
> \sin\vartheta &= -\sin\left(\tfrac{\pi}{2} + \phi\right) = -\left(\sin\tfrac{\pi}{2}\cos\phi + \cos\tfrac{\pi}{2}\sin\phi\right) = -\cos\phi \quad &\text{(sine odd; sum formula)} \\
> R\cos\vartheta\,\mathbf i_1 + R\sin\vartheta\,\mathbf k_1 &= -R\sin\phi\,\mathbf i_1 - R\cos\phi\,\mathbf k_1 \quad &\text{(polar form gives the same vector)} \\
> \mathbf r_1^Q &= -R\,\mathbf i_1, \quad \rho = x_1^P - x_1^Q = -R\sin\phi + R = R\left(1 - \sin\phi\right) \quad &\text{(horizontal distance from $P$ to the rotation axis)} \\
> \mathbf r_0^O &= \overrightarrow{QO} = R\,\mathbf i_1, \quad \mathbf r_0^P = \mathbf r_0^O + \mathbf r_1^P = R\left(1 - \sin\phi\right)\mathbf i_1 - R\cos\phi\,\mathbf k_1 \quad &\text{(Eq. 3.16)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = -R\sin\phi\,\mathbf i_1 - R\cos\phi\,\mathbf k_1, \qquad \mathbf r_0^P = R\left(1 - \sin\phi\right)\mathbf i_1 - R\cos\phi\,\mathbf k_1, \qquad \rho = R\left(1 - \sin\phi\right)}$$
>
> **Units:** $[R\sin\phi] = [R\cos\phi] = [\rho] = [\mathrm{L}]$
> **Meaning:** at the start the particle is at the lowest point of the arc, a distance $R$ from the axis; at a quarter turn it is at the upper end, on the axis. The angle grows clockwise in the drawing, from the downward axis towards $B$.

> [!derivation] Path basis of the arc
> **Law:** unit tangent as the derivative of the position with respect to the arc length; principal normal; binormal as a vector product
> **Source:** Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.13; Notes.pdf, Eq. 2.15
>
> The arc length from the lowest point is $s$, equal to $R$ times $\phi$, so the derivative with respect to $s$ is the derivative with respect to $\phi$ divided by $R$ (chain rule). The binormal is the determinant expanded along its first row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \frac{d\mathbf r_1^P}{d\phi} &= -R\cos\phi\,\mathbf i_1 + R\sin\phi\,\mathbf k_1 \quad &\text{($\tfrac{d}{d\phi}\sin\phi = \cos\phi$, $\tfrac{d}{d\phi}\cos\phi = -\sin\phi$)} \\
> \mathbf e_t &= \frac{d\mathbf r_1^P}{ds} = \frac{1}{R}\frac{d\mathbf r_1^P}{d\phi} = -\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf k_1 \quad &\text{(Eq. 2.9; chain rule with $ds = R\,d\phi$)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{1}{R}\left(\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1\right), \quad \left|\frac{d\mathbf e_t}{ds}\right| = \frac{1}{R} \quad &\text{(curvature of the circle)} \\
> \mathbf e_n &= \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1 = -\frac{\mathbf r_1^P}{R} \quad &\text{(Eq. 2.11: towards $O$)} \\
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n = \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr -\cos\phi & 0 & \sin\phi \cr \sin\phi & 0 & \cos\phi \end{vmatrix} = (+1)(0 - 0)\,\mathbf i_1 + (-1)\left(-\cos^2\phi - \sin^2\phi\right)\mathbf j_1 + (+1)(0 - 0)\,\mathbf k_1 = \mathbf j_1 \quad &\text{(first row; cofactor signs)} \\
> \det[{}_1R_F] &= -\cos\phi\left(0\cdot 0 - 1\cdot\cos\phi\right) - \sin\phi\left(0\cdot 0 - 1\cdot\sin\phi\right) + 0 = \cos^2\phi + \sin^2\phi = 1 \quad &\text{(columns $\mathbf e_t, \mathbf e_n, \mathbf e_b$; first row; signs $+, -, +$)} \\
> \mathbf e_t\cdot\mathbf e_n &= -\cos\phi\sin\phi + \sin\phi\cos\phi = 0 \quad &\text{(orthogonal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = -\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf k_1, \quad \mathbf e_n = \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1, \quad \mathbf e_b = \mathbf j_1, \quad [{}_1R_F] = \begin{pmatrix} -\cos\phi & \sin\phi & 0 \cr 0 & 0 & 1 \cr \sin\phi & \cos\phi & 0 \end{pmatrix}}$$
>
> **Units:** the three vectors are dimensionless; $[d\mathbf e_t/ds] = [\mathrm{L^{-1}}]$
> **Meaning:** the tangent starts as minus $\mathbf i_1$ at the lowest point and ends as $\mathbf k_1$ at the upper end; the normal points along the radius to the centre; the binormal is the normal to the plane of the arc, into the paper.

### Kinematics

> [!derivation] Motion of the turning frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0 \quad &\text{(simple rotation about the fixed vertical; $\omega$ constant)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) &= -\omega\sin\omega t\,\mathbf i_0 + \omega\cos\omega t\,\mathbf j_0 = \omega\,\mathbf j_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from $S_1$ the three unit vectors are constant; seen from $S_0$ the horizontal ones turn with the frame.

#### (a) Relative velocity and acceleration in the path basis

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$ and $\mathbf k_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 18
>
> $$\begin{aligned}
> \frac{d}{dt}\sin\phi &= \cos\phi\,\dot\phi, \quad \frac{d}{dt}\cos\phi = -\sin\phi\,\dot\phi \quad &\text{(chain rule)} \\
> \mathbf v_1^P &= \left.\frac{d\mathbf r_1^P}{dt}\right|_1 = -R\cos\phi\,\dot\phi\,\mathbf i_1 + R\sin\phi\,\dot\phi\,\mathbf k_1 = R\dot\phi\,\mathbf e_t \quad &\text{(components differentiated; Eq. 3.19)} \\
> \left.\frac{d\mathbf e_t}{dt}\right|_1 &= \frac{d\mathbf e_t}{d\phi}\,\dot\phi = \left(\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1\right)\dot\phi = \dot\phi\,\mathbf e_n \quad &\text{(chain rule on $\mathbf e_t(\phi(t))$)} \\
> \mathbf a_1^P &= \left.\frac{d}{dt}\left(R\dot\phi\,\mathbf e_t\right)\right|_1 = R\ddot\phi\,\mathbf e_t + R\dot\phi\,\dot\phi\,\mathbf e_n \quad &\text{(product rule; Eq. 3.24)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^P = R\dot\phi\,\mathbf e_t, \qquad \mathbf a_1^P = R\ddot\phi\,\mathbf e_t + R\dot\phi^2\,\mathbf e_n}$$
>
> **Units:** $[R\dot\phi] = [\mathrm{L\,T^{-1}}]$; $[R\ddot\phi] = [R\dot\phi^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the relative velocity is tangent to the arc; the relative acceleration has the tangential part of the change of speed and the normal part towards the centre of the circle; nothing along the binormal.

> [!derivation] Absolute velocity and acceleration: origin, centripetal and Coriolis terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule; derivatives of the unit vectors
> **Source:** Notes.pdf, Eq. 3.16; Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> The absolute position is differentiated as it stands, term by term; the terms are named afterwards.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left[R\left(1 - \sin\phi\right)\right]\mathbf i_1 + R\left(1 - \sin\phi\right)\omega\,\mathbf j_1 + R\sin\phi\,\dot\phi\,\mathbf k_1 \quad &\text{(product rule; derivative of $\mathbf i_1$; $\mathbf k_1$ constant)} \\
> &= -R\cos\phi\,\dot\phi\,\mathbf i_1 + R\sin\phi\,\dot\phi\,\mathbf k_1 + \omega R\left(1 - \sin\phi\right)\mathbf j_1 = \mathbf v_1^P + \omega\rho\,\mathbf j_1 \quad &\text{(chain rule; relative velocity recognised)} \\
> \mathbf v_0^O + \boldsymbol\omega_{10}\times\mathbf r_1^P &= \omega R\,\mathbf j_1 + \omega\,\mathbf k_1\times\left(-R\sin\phi\,\mathbf i_1 - R\cos\phi\,\mathbf k_1\right) = \omega R\,\mathbf j_1 - \omega R\sin\phi\,\mathbf j_1 \quad &\text{(the transport part is Eq. 3.26)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \left(-R\cos\phi\,\dot\phi\right)\omega\,\mathbf j_1 \quad &\text{(product rule; the turning of $\mathbf i_1$ inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left[\omega R\left(1 - \sin\phi\right)\mathbf j_1\right] &= -\omega R\cos\phi\,\dot\phi\,\mathbf j_1 + \omega R\left(1 - \sin\phi\right)\left(-\omega\,\mathbf i_1\right) \quad &\text{(product rule; chain rule; derivative of $\mathbf j_1$)} \\
> \mathbf a_0^P &= \mathbf a_1^P - 2\omega R\cos\phi\,\dot\phi\,\mathbf j_1 - \omega^2R\left(1 - \sin\phi\right)\mathbf i_1 \quad &\text{(sum of the two lines above)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\omega R\dot\phi\,\mathbf k_1\times\left(-\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf k_1\right) = -2\omega R\cos\phi\,\dot\phi\,\mathbf j_1 \quad &\text{(the $\mathbf j_1$ term: Coriolis)} \\
> \mathbf a_0^O &= R\,\omega\left(-\omega\,\mathbf i_1\right) = -\omega^2R\,\mathbf i_1 \quad &\text{(second derivative of $R\,\mathbf i_1$: origin term)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \omega\,\mathbf k_1\times\left(-\omega R\sin\phi\,\mathbf j_1\right) = \omega^2R\sin\phi\,\mathbf i_1 \quad &\text{($\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$: centripetal term)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \underbrace{-\omega^2R\,\mathbf i_1}_{\mathbf a_0^O} + \mathbf a_1^P + \underbrace{\omega^2R\sin\phi\,\mathbf i_1}_{\boldsymbol\omega_{10}\times(\boldsymbol\omega_{10}\times\mathbf r_1^P)} + \underbrace{\left(-2\omega R\cos\phi\,\dot\phi\,\mathbf j_1\right)}_{2\boldsymbol\omega_{10}\times\mathbf v_1^P}}$$
>
> **Units:** $[\omega^2R] = [\omega R\dot\phi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the origin term and the centripetal term add up to minus the square of the rate times the distance to the true axis, along $\mathbf i_1$: the point is pulled towards the axis, not towards $O$. The Coriolis term is normal to the plane of the arc. There is no Euler term, the rate being constant.

### Forces and Equations of Motion

![[attachments/EM-SOL/p30-fbd.svg]]

#### (b) Newton's second law in the path basis

> [!derivation] Actual and inertia forces on the particle
> **Law:** linear spring of zero natural length; smooth reaction normal to the tangent; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 5.1; Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.16; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> \overrightarrow{BP} &= \mathbf r_1^P - \mathbf r_1^B = \left(-R\sin\phi + 2R\right)\mathbf i_1 - R\cos\phi\,\mathbf k_1 \quad &\text{($\mathbf r_1^B = -2R\,\mathbf i_1$)} \\
> \mathbf F_K &= -K\,\overrightarrow{BP} = -\alpha m\omega^2R\left[\left(2 - \sin\phi\right)\mathbf i_1 - \cos\phi\,\mathbf k_1\right] \quad &\text{(Eq. 5.1 in vector form; $K = \alpha m\omega^2$)} \\
> \mathbf N &= N_n\,\mathbf e_n + N_b\,\mathbf e_b \quad &\text{(smooth arc: no component along $\mathbf e_t$)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = m\omega^2R\,\mathbf i_1, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{(Eq. 4.62, first two terms)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = -m\omega^2R\sin\phi\,\mathbf i_1 \quad &\text{(centrifugal: composition box times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\omega R\cos\phi\,\dot\phi\,\mathbf j_1 \quad &\text{(Coriolis: composition box times $-m$)} \\
> \mathbf F_A + \mathbf F_C &= m\omega^2R\left(1 - \sin\phi\right)\mathbf i_1 = m\omega^2\rho\,\mathbf i_1 \quad &\text{(sum; Slide 30 about the true axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_K = -\alpha m\omega^2R\left[\left(2 - \sin\phi\right)\mathbf i_1 - \cos\phi\,\mathbf k_1\right], \quad \mathbf F_A + \mathbf F_C = m\omega^2R\left(1 - \sin\phi\right)\mathbf i_1, \quad \mathbf F_E = \mathbf 0, \quad \mathbf F_{COR} = 2m\omega R\cos\phi\,\dot\phi\,\mathbf j_1}$$
>
> **Units:** $[K\,R] = [\alpha m\omega^2R] = [m\omega R\dot\phi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** one actual applied force (the spring, towards $B$), the reaction with two unknown components, and the inertia forces: the origin and centrifugal terms together push the particle horizontally away from the true axis, and the Coriolis force is normal to the plane of the arc.

> [!derivation] Projections of the forces on the path basis
> **Law:** scalar products with the columns of $[{}_1R_F]$
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 2.13
>
> From the columns of $[{}_1R_F]$: the projections of $\mathbf i_1$ on $\mathbf e_t$ and $\mathbf e_n$ are minus the cosine and the sine; those of $\mathbf k_1$ are the sine and the cosine; $\mathbf j_1$ is $\mathbf e_b$.
>
> $$\begin{aligned}
> \mathbf F_K\cdot\mathbf e_t &= -\alpha m\omega^2R\left[\left(2 - \sin\phi\right)\left(-\cos\phi\right) - \cos\phi\sin\phi\right] = -\alpha m\omega^2R\left(-2\cos\phi\right) = 2\alpha m\omega^2R\cos\phi \quad &\text{(the two sine-cosine products cancel)} \\
> \mathbf F_K\cdot\mathbf e_n &= -\alpha m\omega^2R\left[\left(2 - \sin\phi\right)\sin\phi - \cos^2\phi\right] = -\alpha m\omega^2R\left(2\sin\phi - 1\right) \quad &\text{($\sin^2\phi + \cos^2\phi = 1$)} \\
> \left(\mathbf F_A + \mathbf F_C\right)\cdot\mathbf e_t &= -m\omega^2R\left(1 - \sin\phi\right)\cos\phi, \quad \left(\mathbf F_A + \mathbf F_C\right)\cdot\mathbf e_n = m\omega^2R\left(1 - \sin\phi\right)\sin\phi \quad &\text{(along $\mathbf i_1$)} \\
> \mathbf F_K\cdot\mathbf e_b &= 0, \quad \left(\mathbf F_A + \mathbf F_C\right)\cdot\mathbf e_b = 0, \quad \mathbf F_{COR}\cdot\mathbf e_b = 2m\omega R\cos\phi\,\dot\phi \quad &\text{(only the Coriolis force leaves the plane)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_K = 2\alpha m\omega^2R\cos\phi\,\mathbf e_t + \alpha m\omega^2R\left(1 - 2\sin\phi\right)\mathbf e_n, \quad \mathbf F_A + \mathbf F_C = m\omega^2R\left(1 - \sin\phi\right)\left(-\cos\phi\,\mathbf e_t + \sin\phi\,\mathbf e_n\right)}$$
>
> **Units:** every component $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** along the arc the spring always pulls towards larger angles, up towards $B$, and the inertia forces of the rotation pull towards smaller angles, away from the axis.

> [!derivation] Three components of Newton's second law in the path basis
> **Law:** Newton's second law in a non-inertial frame, projected on $\{\mathbf e_t, \mathbf e_n, \mathbf e_b\}$
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.17; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19; [Lecture 5, Slide 28]; Problems.pdf, p. 18
>
> Three scalar equations for three unknowns: the coordinate and the two components of the reaction.
>
> $$\begin{aligned}
> \mathbf e_t:\ mR\ddot\phi &= 2\alpha m\omega^2R\cos\phi - m\omega^2R\left(1 - \sin\phi\right)\cos\phi \quad &\text{(Eq. 6.17: no reaction along the tangent)} \\
> \mathbf e_n:\ mR\dot\phi^2 &= N_n + \alpha m\omega^2R\left(1 - 2\sin\phi\right) + m\omega^2R\left(1 - \sin\phi\right)\sin\phi \quad &\text{(Eq. 6.18, normal)} \\
> \mathbf e_b:\ 0 &= N_b + 2m\omega R\cos\phi\,\dot\phi \quad &\text{(Eq. 6.19, binormal)} \\
> \ddot\phi &= \omega^2\cos\phi\left(2\alpha - 1 + \sin\phi\right) \quad &\text{(tangential equation divided by $mR$; $\cos\phi$ factored)}
> \end{aligned}$$
>
> $$\boxed{\ddot\phi = \omega^2\cos\phi\left(2\alpha - 1 + \sin\phi\right), \quad N_n = mR\dot\phi^2 - \alpha m\omega^2R\left(1 - 2\sin\phi\right) - m\omega^2R\sin\phi\left(1 - \sin\phi\right), \quad N_b = -2m\omega R\cos\phi\,\dot\phi}$$
>
> **Units:** $[\ddot\phi] = [\omega^2] = [\mathrm{T^{-2}}]$; $[N_n] = [N_b] = [m\omega^2R] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the tangential component is the equation of motion; the normal and binormal components give the reaction once the motion is known. The binormal reaction balances the Coriolis force: the arc pushes the particle sideways so that it keeps turning with the plane while its distance to the axis changes.

### Answers and Checks

#### (c) Energy conservation in the relative frame

> [!derivation] Why the energy of the relative motion is conserved
> **Law:** power of each force on the relative velocity; potentials of the forces that work
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Two reasons. First, the forces that do no work in $S_1$: the reaction (the arc is at rest in $S_1$ and the reaction is normal to the tangent), the Coriolis force (normal to the relative velocity) and the Euler force (zero). Second, the forces that do work have potentials that depend on the position in $S_1$ only: the spring (its end $B$ is fixed in $S_1$), and the sum of the origin and centrifugal forces, a function of the position alone because the rate $\omega$ is constant and the acceleration of the origin is a constant vector of $S_1$. With a variable rate the centrifugal force would change in time at a fixed point and the Euler force would appear: no potential.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= \left(N_n\,\mathbf e_n + N_b\,\mathbf e_b\right)\cdot R\dot\phi\,\mathbf e_t = 0 \quad &\text{(reaction: no power in $S_1$)} \\
> \mathbf F_{COR}\cdot\mathbf v_1^P &= 2m\omega R\cos\phi\,\dot\phi\,\mathbf e_b\cdot R\dot\phi\,\mathbf e_t = 0 \quad &\text{(Coriolis: no power)} \\
> \mathbf F_E\cdot\mathbf v_1^P &= 0 \quad &\text{($\mathbf F_E = \mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\text{only } \mathbf F_K \text{ and } \mathbf F_A + \mathbf F_C \text{ work in } S_1, \text{ and both have potentials}}$$
>
> **Units:** $[\mathbf F\cdot\mathbf v_1^P] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** the conditions of Slide 29 are met, so the mechanical energy of the relative motion is a constant of the motion.

> [!derivation] Potentials along the arc and energy integral
> **Law:** potential as minus the work along the path, with Barrow's rule; change of variable in the integral
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.24; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]
>
> Along the arc the displacement is $\mathbf e_t$ times $R\,d\phi'$, so each potential is minus the integral of the tangential component times $R$. In the second integral the substitution $u$ equal to $\sin\phi'$ has the differential $\cos\phi'\,d\phi'$ and the limits 0 and $\sin\phi$. Potentials are taken zero at the lowest point.
>
> $$\begin{aligned}
> V_K(\phi) &= -\int_0^{\phi}2\alpha m\omega^2R\cos\phi'\,R\,d\phi' = -2\alpha m\omega^2R^2\left[\sin\phi'\right]_0^{\phi} = -2\alpha m\omega^2R^2\left(\sin\phi - 0\right) \quad &\text{(Eq. 4.14; antiderivative of the cosine; Barrow's rule)} \\
> V_{AC}(\phi) &= -\int_0^{\phi}\left(-m\omega^2R\left(1 - \sin\phi'\right)\cos\phi'\right)R\,d\phi' = m\omega^2R^2\int_0^{\sin\phi}\left(1 - u\right)du \quad &\text{(Eq. 4.14; $u = \sin\phi'$, $du = \cos\phi'\,d\phi'$)} \\
> &= m\omega^2R^2\left[u - \tfrac12 u^2\right]_0^{\sin\phi} = m\omega^2R^2\left(\sin\phi - \tfrac12\sin^2\phi\right) \quad &\text{(antiderivative; Barrow's rule)} \\
> T_1^P &= \tfrac12 m\,\mathbf v_1^P\cdot\mathbf v_1^P = \tfrac12 mR^2\dot\phi^2 \quad &\text{(kinetic energy in $S_1$)} \\
> E_1^P &= T_1^P + V_K + V_{AC} \quad &\text{(Eq. 4.31 in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{E_1^P = \tfrac12 mR^2\dot\phi^2 - 2\alpha m\omega^2R^2\sin\phi + m\omega^2R^2\left(\sin\phi - \tfrac12\sin^2\phi\right) = \text{const}}$$
>
> **Units:** $[mR^2\dot\phi^2] = [m\omega^2R^2] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the spring potential falls as the particle climbs towards $B$; the rotation potential rises as the particle approaches the axis. Up to additive constants they are one half of the spring constant times the squared length of the spring and minus one half of the mass times the squared rate times the squared distance to the axis (Slide 30).

> [!derivation] Constant of the motion and relation with the tangential equation
> **Law:** initial conditions; time derivative of the energy along the motion; chain rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.29; Problems.pdf, p. 18
>
> The initial relative velocity is the velocity of part (a) at the start, where the tangent is minus $\mathbf i_1$.
>
> $$\begin{aligned}
> \mathbf v_1^P(0) &= R\dot\phi(0)\,\mathbf e_t(0) = R\dot\phi(0)\left(-\cos 0\,\mathbf i_1 + \sin 0\,\mathbf k_1\right) = -R\dot\phi(0)\,\mathbf i_1 = -\beta\omega R\,\mathbf i_1 \quad &\text{(part (a) at $t = 0$; statement)} \\
> \dot\phi(0) &= \beta\omega, \quad E_1^P(0) = \tfrac12 mR^2\beta^2\omega^2 + 0 + 0 \quad &\text{(at $\phi = 0$ both potentials vanish)} \\
> \dot\phi^2 &= \beta^2\omega^2 + 4\alpha\omega^2\sin\phi - 2\omega^2\sin\phi + \omega^2\sin^2\phi \quad &\text{(energy equation divided by $\tfrac12 mR^2$)} \\
> \frac{dE_1^P}{dt} &= mR^2\dot\phi\ddot\phi - 2\alpha m\omega^2R^2\cos\phi\,\dot\phi + m\omega^2R^2\left(\cos\phi - \sin\phi\cos\phi\right)\dot\phi \quad &\text{(product rule; chain rule $\tfrac{d}{dt}\sin^2\phi = 2\sin\phi\cos\phi\,\dot\phi$)} \\
> &= mR^2\dot\phi\left[\ddot\phi - \omega^2\cos\phi\left(2\alpha - 1 + \sin\phi\right)\right] \quad &\text{(factor $mR^2\dot\phi$)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi^2 = \omega^2\left[\beta^2 + \left(4\alpha - 2\right)\sin\phi + \sin^2\phi\right], \qquad \frac{dE_1^P}{dt} = mR^2\dot\phi\times\left(\text{tangential equation of part (b)}\right)}$$
>
> **Units:** $[\dot\phi^2] = [\omega^2] = [\mathrm{T^{-2}}]$; $[dE_1^P/dt] = [\mathrm{M\,L^2\,T^{-3}}]$
> **Meaning:** the energy equation is not new information: it is the first integral of the tangential component (that equation times the relative speed, integrated once), and its derivative gives it back wherever the rate is not zero. The normal and binormal components are independent of it and give the reaction.

#### (d) Value of alpha for an equilibrium at pi/6

> [!derivation] Equilibrium positions and the value of alpha
> **Law:** relative equilibrium: rate and angular acceleration zero for all time, so the tangential force vanishes
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 18
>
> $$\begin{aligned}
> 0 &= \omega^2\cos\phi_e\left(2\alpha - 1 + \sin\phi_e\right) \quad &\text{(tangential equation with $\dot\phi = \ddot\phi = 0$)} \\
> \cos\phi_e = 0 &\Rightarrow \phi_e = \tfrac{\pi}{2} \quad &\text{(first factor: the upper end, on the axis, for every $\alpha$)} \\
> \sin\phi_e &= 1 - 2\alpha \quad &\text{(second factor: interior points, only for $0 \le 1 - 2\alpha \le 1$)} \\
> \sin\tfrac{\pi}{6} &= \tfrac12 = 1 - 2\alpha \;\Rightarrow\; 2\alpha = \tfrac12 \quad &\text{(the required position)} \\
> N_n &= 0 - \tfrac14 m\omega^2R\left(1 - 1\right) - m\omega^2R\cdot\tfrac12\left(1 - \tfrac12\right) = -\tfrac14 m\omega^2R, \quad N_b = 0 \quad &\text{(part (b) at rest at $\pi/6$ with $\alpha = 1/4$)}
> \end{aligned}$$
>
> $$\boxed{\alpha = \tfrac14 \qquad \left(\text{reaction at that equilibrium } \mathbf N = -\tfrac14 m\omega^2R\,\mathbf e_n\right)}$$
>
> **Units:** $[\alpha] = [1]$; $[N_n] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** a soft spring, a quarter of the reference stiffness, balances along the arc the outward pull of the rotation at thirty degrees. At rest there the reaction points away from $O$: the arc holds the particle against the net pull towards the centre.

#### (e) Types of motion for alpha equal to 1/4, critical beta and reaction at pi/2

> [!derivation] Barrier function and quadrature
> **Law:** energy integral of part (c); the motion is possible only where the kinetic energy is not negative
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Notes.pdf, Sec. 4.6
>
> With $\alpha$ equal to one quarter, the factor $4\alpha - 2$ is minus one. The function $U(\phi)$ below plays the role of a potential: the motion is allowed where $U$ does not exceed $\beta^2$.
>
> $$\begin{aligned}
> \dot\phi^2 &= \omega^2\left[\beta^2 - \sin\phi + \sin^2\phi\right] = \omega^2\left[\beta^2 - U(\phi)\right], \quad U(\phi) = \sin\phi\left(1 - \sin\phi\right) \quad &\text{(part (c) with $\alpha = 1/4$)} \\
> U(0) &= 0, \quad U\left(\tfrac{\pi}{2}\right) = 1\cdot 0 = 0 \quad &\text{(ends of the arc)} \\
> U'(\phi) &= \cos\phi\left(1 - \sin\phi\right) + \sin\phi\left(-\cos\phi\right) = \cos\phi\left(1 - 2\sin\phi\right) \quad &\text{(product rule; chain rule)} \\
> U'(\phi) = 0,\ 0 \lt \phi \lt \tfrac{\pi}{2} &\Rightarrow \sin\phi = \tfrac12,\ \phi = \tfrac{\pi}{6}, \quad U\left(\tfrac{\pi}{6}\right) = \tfrac12\cdot\tfrac12 = \tfrac14 \quad &\text{(single interior stationary point)} \\
> U''(\phi) &= -\sin\phi\left(1 - 2\sin\phi\right) - 2\cos^2\phi, \quad U''\left(\tfrac{\pi}{6}\right) = 0 - 2\cdot\tfrac34 = -\tfrac32 \lt 0 \quad &\text{(a maximum: a barrier)} \\
> t &= \int_0^{\phi}\frac{d\phi'}{\omega\sqrt{\beta^2 - U(\phi')}} \quad &\text{(quadrature while $\dot\phi \gt 0$; separation of variables)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi^2 = \omega^2\left[\beta^2 - U(\phi)\right], \qquad U(\phi) = \sin\phi\left(1 - \sin\phi\right), \qquad \max_{[0,\pi/2]}U = U\left(\tfrac{\pi}{6}\right) = \tfrac14}$$
>
> **Units:** $[U] = [\beta^2] = [1]$
> **Meaning:** the barrier has its top at the equilibrium of part (d), which is therefore unstable (a maximum of the potential); the particle crosses it only if the square of $\beta$ exceeds one quarter.

![[attachments/EM-SOL/p30-barrier.svg]]

> [!derivation] Three types of motion
> **Law:** turning points where the kinetic energy vanishes; sign of the tangential force there; linearisation about the unstable equilibrium by Taylor expansion
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Notes.pdf, Sec. 4.6
>
> For small $\beta$ the rate vanishes where $U$ reaches the square of $\beta$; the quadratic in the sine has two roots, and the particle, starting at the lowest point, meets the smaller one first. For $\beta$ equal to one half, write $\eta$ for the angle minus its equilibrium value.
>
> $$\begin{aligned}
> \sin^2\phi^* - \sin\phi^* + \beta^2 &= 0 \;\Rightarrow\; \sin\phi^* = \frac{1 \pm \sqrt{1 - 4\beta^2}}{2} \quad &\text{(turning points, $\beta \le 1/2$; both roots)} \\
> \sin\phi^*_- &= \frac{1 - \sqrt{1 - 4\beta^2}}{2} \le \tfrac12, \quad \sin\phi^*_+ = \frac{1 + \sqrt{1 - 4\beta^2}}{2} \ge \tfrac12 \quad &\text{(the root $+$ lies beyond the barrier: not reached from $\phi = 0$)} \\
> \ddot\phi\left(\phi^*_-\right) &= \omega^2\cos\phi^*_-\left(\sin\phi^*_- - \tfrac12\right) \lt 0 \quad &\text{(tangential equation, $\beta \lt 1/2$: it turns back)} \\
> \beta = \tfrac12:\quad \dot\phi^2 &= \omega^2\left(\tfrac14 - \sin\phi + \sin^2\phi\right) = \omega^2\left(\tfrac12 - \sin\phi\right)^2 \quad &\text{(perfect square)} \\
> \dot\phi &= \omega\left(\tfrac12 - \sin\phi\right) \quad &\text{(positive root: the rate starts at $\omega/2$)} \\
> \sin\left(\tfrac{\pi}{6} + \eta\right) &\simeq \tfrac12 + \tfrac{\sqrt3}{2}\eta \;\Rightarrow\; \dot\eta \simeq -\tfrac{\sqrt3}{2}\omega\,\eta \quad &\text{(Taylor expansion to first order; $\cos\tfrac{\pi}{6} = \tfrac{\sqrt3}{2}$)} \\
> \int_{\eta_1}^{\eta}\frac{d\eta'}{\eta'} &= \left[\ln\left|\eta'\right|\right]_{\eta_1}^{\eta} = \ln\frac{\eta}{\eta_1} = -\tfrac{\sqrt3}{2}\omega\left(t - t_1\right) \quad &\text{(separation of variables from a time $t_1$ near the top; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \beta \lt \tfrac12: \text{ turns back at } \sin\phi^* = \tfrac12\left(1 - \sqrt{1 - 4\beta^2}\right) \text{ and leaves the arc at its lower end}; \cr \beta = \tfrac12: \ \eta = \eta_1 e^{-\sqrt3\,\omega(t - t_1)/2} \text{ (creeps towards } \pi/6 \text{ without reaching it)}; \quad \beta \gt \tfrac12: \text{ reaches } \tfrac{\pi}{2} \end{gathered}}$$
>
> **Units:** $[\beta] = [1]$; $[\omega\,t] = [1]$; $[\eta] = [1]$
> **Meaning:** below the critical value the particle climbs part of the way, stops, comes back to the lowest point with its initial speed (energy conservation) and leaves the arc there, which ends at that point. At the critical value the distance to the top of the barrier decays exponentially and is never zero. Above it the rate never vanishes and the particle runs to the upper end.

> [!derivation] Critical beta and reaction at pi/2
> **Law:** energy integral at the end of the arc; normal and binormal components of part (b)
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 4.27; Problems.pdf, p. 18
>
> At the upper end the sine is 1 and the cosine 0, the normal is the column of $[{}_1R_F]$ with these values, and the rate follows from the energy integral.
>
> $$\begin{aligned}
> \dot\phi^2\left(\tfrac{\pi}{2}\right) &= \omega^2\left[\beta^2 - U\left(\tfrac{\pi}{2}\right)\right] = \beta^2\omega^2, \quad \dot\phi\left(\tfrac{\pi}{2}\right) = \beta\omega \quad &\text{(barrier crossed: the rate stayed positive)} \\
> \mathbf e_n\left(\tfrac{\pi}{2}\right) &= \sin\tfrac{\pi}{2}\,\mathbf i_1 + \cos\tfrac{\pi}{2}\,\mathbf k_1 = \mathbf i_1 \quad &\text{(towards $O$)} \\
> N_b &= -2m\omega R\cos\tfrac{\pi}{2}\,\beta\omega = 0 \quad &\text{(binormal component)} \\
> N_n &= mR\beta^2\omega^2 - \tfrac14 m\omega^2R\left(1 - 2\right) - m\omega^2R\cdot 1\cdot\left(1 - 1\right) = m\omega^2R\left(\beta^2 + \tfrac14\right) \quad &\text{(normal component, $\alpha = 1/4$)} \\
> \lim_{\beta\to 1/2^+}N_n &= m\omega^2R\left(\tfrac14 + \tfrac14\right) = \tfrac12 m\omega^2R \quad &\text{(at the critical value)}
> \end{aligned}$$
>
> $$\boxed{\beta_c = \tfrac12, \qquad \mathbf N\left(\tfrac{\pi}{2}\right) = m\omega^2R\left(\beta^2 + \tfrac14\right)\mathbf i_1 \ \xrightarrow{\ \beta\to\beta_c^+\ }\ \tfrac12 m\omega^2R\,\mathbf i_1}$$
>
> **Units:** $[m\omega^2R] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** at the upper end the particle is on the axis and moves along it, so the origin and centrifugal forces together, and the Coriolis force, vanish there; the reaction points to $O$ and supplies the centripetal force of the circular path plus the balance of the spring, which there pulls towards $B$ with a quarter of the mass times the squared rate times $R$.

#### (f) Maximum height after leaving the arc

> [!derivation] Vertical motion of the free particle
> **Law:** Newton's second law in $S_1$, vertical component; harmonic oscillator; initial conditions
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.8; Notes.pdf, Eq. 5.9
>
> Once free, the particle has three coordinates in $S_1$; time $\tau$ is counted from the separation. Every inertia force is normal to $\mathbf k_1$: the origin and centrifugal forces lie along the horizontal from the axis, and the Coriolis force is the cross product of $\mathbf k_1$ with a vector. Only the spring has a vertical component.
>
> $$\begin{aligned}
> \mathbf r_1^P(0) &= -R\,\mathbf i_1, \quad \mathbf v_1^P(0) = R\beta\omega\,\mathbf e_t\left(\tfrac{\pi}{2}\right) = \beta\omega R\,\mathbf k_1 \quad &\text{(state at the separation: on the axis, moving up)} \\
> \mathbf k_1\cdot\mathbf F_K &= -K\,\mathbf k_1\cdot\left[\left(x_1 + 2R\right)\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1\right] = -\alpha m\omega^2z_1 \quad &\text{(spring, free position)} \\
> \mathbf k_1\cdot\left(\mathbf F_A + \mathbf F_C + \mathbf F_{COR}\right) &= 0 \quad &\text{(all three normal to $\mathbf k_1$)} \\
> m\ddot z_1 &= -\alpha m\omega^2z_1 \;\Rightarrow\; \ddot z_1 + \omega_z^2z_1 = 0, \quad \omega_z = \sqrt{\alpha}\,\omega \quad &\text{(Eq. 4.63, vertical; Eq. 5.6)} \\
> z_1(\tau) &= C_1\cos\omega_z\tau + C_2\sin\omega_z\tau \quad &\text{(Eq. 5.7)} \\
> \dot z_1(\tau) &= -\omega_zC_1\sin\omega_z\tau + \omega_zC_2\cos\omega_z\tau \quad &\text{(chain rule)} \\
> z_1(0) &= C_1 = 0, \quad \dot z_1(0) = \omega_zC_2 = \beta\omega R \;\Rightarrow\; C_2 = \frac{\beta\omega R}{\sqrt{\alpha}\,\omega} = \frac{\beta R}{\sqrt{\alpha}} \quad &\text{(Eq. 5.8 and 5.9)} \\
> z_{max} &= C_2 = \frac{\beta R}{\sqrt{1/4}} = 2\beta R, \quad \omega_z\tau_{max} = \tfrac{\pi}{2} \Rightarrow \tau_{max} = \frac{\pi}{2\sqrt{\alpha}\,\omega} = \frac{\pi}{\omega} \quad &\text{(maximum of the sine; $\alpha = 1/4$)}
> \end{aligned}$$
>
> $$\boxed{z_{max} = \frac{\beta R}{\sqrt{\alpha}} = 2\beta R \quad \left(\alpha = \tfrac14,\ \beta \gt \tfrac12\right), \text{ reached a time } \pi/\omega \text{ after leaving the arc}}$$
>
> **Units:** $[\beta R] = [\mathrm{L}]$; $[\tau_{max}] = [\mathrm{T}]$
> **Meaning:** the vertical motion is a harmonic oscillation driven only by the vertical pull of the spring; the horizontal motion, coupled by the rotation, does not affect it. The height is measured from the horizontal plane through $O$ and $B$, the same in $S_0$ because the frames share the vertical. The result assumes the particle does not touch the arc again, which lies below that plane while the height stays positive.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Relative velocity and acceleration | $\mathbf v_1^P = R\dot\phi\,\mathbf e_t$, $\mathbf a_1^P = R\ddot\phi\,\mathbf e_t + R\dot\phi^2\,\mathbf e_n$, with $\mathbf e_t = -\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf k_1$, $\mathbf e_n = \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1$, $\mathbf e_b = \mathbf j_1$ |
| (b) Newton, $\mathbf e_t$ | $mR\ddot\phi = 2\alpha m\omega^2R\cos\phi - m\omega^2R(1 - \sin\phi)\cos\phi$, i.e. $\ddot\phi = \omega^2\cos\phi\,(2\alpha - 1 + \sin\phi)$ |
| (b) Newton, $\mathbf e_n$ | $mR\dot\phi^2 = N_n + \alpha m\omega^2R(1 - 2\sin\phi) + m\omega^2R(1 - \sin\phi)\sin\phi$ |
| (b) Newton, $\mathbf e_b$ | $0 = N_b + 2m\omega R\cos\phi\,\dot\phi$ |
| (c) Energy | $\frac12 mR^2\dot\phi^2 - 2\alpha m\omega^2R^2\sin\phi + m\omega^2R^2(\sin\phi - \frac12\sin^2\phi) = \frac12 m\beta^2\omega^2R^2$; equivalently $\dot\phi^2 = \omega^2[\beta^2 + (4\alpha - 2)\sin\phi + \sin^2\phi]$; it is the first integral of the $\mathbf e_t$ equation |
| (d) Equilibrium at $\pi/6$ | $\alpha = 1/4$ (and $\pi/2$ is an equilibrium for every $\alpha$); reaction there $-\frac14 m\omega^2R\,\mathbf e_n$ |
| (e) Types of motion | $\beta \lt 1/2$: turns back at $\sin\phi^* = \frac12(1 - \sqrt{1 - 4\beta^2})$, returns to $\phi = 0$ and leaves the arc; $\beta = 1/2$: approaches the unstable equilibrium $\pi/6$ asymptotically; $\beta \gt 1/2$: reaches $\pi/2$ with $\dot\phi = \beta\omega$ |
| (e) Critical value and reaction | $\beta_c = 1/2$; $\mathbf N(\pi/2) = m\omega^2R(\beta^2 + \frac14)\,\mathbf i_1$, tending to $\frac12 m\omega^2R\,\mathbf i_1$ as $\beta \to \beta_c$ |
| (f) Maximum height | $z_{max} = \beta R/\sqrt\alpha = 2\beta R$, at $\pi/\omega$ after leaving the arc |
| Reading of the spring | zero natural length; with a natural length $\ell_0$ the spring potential is $\frac12 K(R\sqrt{5 - 4\sin\phi} - \ell_0)^2$ and parts (b) to (f) change |
| Reading of the end of the arc | the arc ends at $\phi = 0$; if it continued below, the particle with $\beta \lt 1/2$ would keep moving to negative $\phi$ instead of leaving it there |

**Check against the official key:** Problems.pdf, p. 74 lists the number 30 with nothing after it: the key prints no answer. The results are checked independently below, with the axial angular momentum about the fixed rotation axis and with limiting cases.

> [!derivation] Independent check: angular momentum about the rotation axis
> **Law:** angular momentum about a fixed point of the axis and its rate, equal to the moment of the actual forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$, with $Q$ as the fixed point, the position has the components $(\rho, 0, -R\cos\phi)$ and the absolute velocity $(-R\cos\phi\,\dot\phi,\ \omega\rho,\ R\sin\phi\,\dot\phi)$. The component along $\mathbf k_1$ of a vector product is the first component of the first factor times the second of the second, minus the second of the first times the first of the second. The spring force and the normal reaction lie in the plane of the arc, which contains the axis: no axial moment.
>
> $$\begin{aligned}
> \mathbf H_{Q,0}\cdot\mathbf k_1 &= m\left(\rho\cdot\omega\rho - 0\right) = m\omega\rho^2 \quad &\text{(Eq. 4.48)} \\
> \mathbf M_Q\cdot\mathbf k_1 &= \rho\,N_b - 0 = \rho\,N_b \quad &\text{(only the binormal reaction, $N_b\,\mathbf j_1$, at the lever arm $\rho$)} \\
> \frac{d}{dt}\left(m\omega\rho^2\right) &= 2m\omega\rho\dot\rho, \quad \dot\rho = \frac{d}{dt}\left[R\left(1 - \sin\phi\right)\right] = -R\cos\phi\,\dot\phi \quad &\text{(chain rule)} \\
> 2m\omega\rho\left(-R\cos\phi\,\dot\phi\right) &= \rho\,N_b \quad &\text{(Eq. 4.53, axial component)}
> \end{aligned}$$
>
> $$\boxed{N_b = -2m\omega R\cos\phi\,\dot\phi \quad (\rho \ne 0)}$$
>
> **Units:** $[\rho N_b] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the same value as the binormal component of part (b), obtained without inertia forces: the sideways push of the arc is what changes the angular momentum about the axis as the particle moves towards it.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> \alpha \to 0:\quad \ddot\phi &= -\omega^2\cos\phi\left(1 - \sin\phi\right) \le 0 \quad &\text{(no spring: pushed to the lowest point, farthest from the axis)} \\
> \alpha \gt \tfrac12:\quad 2\alpha - 1 + \sin\phi &\gt 0 \text{ on } \left[0, \tfrac{\pi}{2}\right] \quad &\text{(no interior equilibrium: the spring wins everywhere)} \\
> \phi = \tfrac{\pi}{2}:\quad \mathbf F_A + \mathbf F_C &= \mathbf 0, \quad \mathbf F_{COR} = \mathbf 0 \quad &\text{(on the axis, moving along it)} \\
> \beta \to \tfrac12^+:\quad t\left(\tfrac{\pi}{2}\right) &\to \infty \quad &\text{(the quadrature diverges like the logarithm at the top of the barrier)}
> \end{aligned}$$
>
> $$\boxed{\alpha \to 0: \text{ particle driven to } \phi = 0; \quad \alpha \gt \tfrac12: \text{ no interior equilibrium}; \quad \beta \to \beta_c^+: \text{ infinite time to reach } \tfrac{\pi}{2}}$$
>
> **Units:** $[\alpha] = [\beta] = [1]$
> **Meaning:** both forces scale with the square of the rate, because the stiffness is a multiple of the mass times the squared rate; the rate only sets the time scale, and the type of motion depends on $\alpha$ and $\beta$ alone.

---

## Problem 33: Two Repelling Particles on a Rotating Parabola

### Reference Frames, Bases and Coordinates

Two heavy particles $P_1$ and $P_2$ of mass $m$ slide without friction on a parabolic wire in the vertical plane $Oxz$, which turns about its axis $Oz$ with the constant rate $\omega$; they repel each other with a force of magnitude $k$ over the square of their distance (Problems.pdf, p. 21). The statement asks for the relative position, velocity and acceleration of each particle, Newton's second law in the turning frame, the motor torque that keeps the rate constant, the equilibria in terms of $\gamma$ and $\kappa$, and the equation of the extreme values of $x_1$ in a symmetric motion. The wire is at rest in $Oxyz$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, origin at the vertex $O$ (on the axis, fixed), $\mathbf k_0$ vertical, up |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $Oxyz$ of the statement, attached to the wire: $\mathbf i_1$ along $Ox$ in the plane of the wire, $\mathbf k_1 = \mathbf k_0$ along the axis, $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$ normal to the plane; $\mathbf i_1 = \mathbf i_0$ at $t = 0$ |
| Wire | $z = x^2/(2L)$, $y = 0$, fixed in $S_1$ |
| Local basis of the wire at $P_i$ | unit tangent $\mathbf t_i$ (sense of growing $x$), in-plane unit normal $\mathbf n_i$ (towards the concave side), and $\mathbf j_1$ |
| Coordinates | $x_1$, $x_2$: abscissas of $P_1$ and $P_2$ along $Ox$ |
| Constraints | for each particle $y_i = 0$ and $z_i = x_i^2/(2L)$: four holonomic, smooth, bilateral constraints, fixed in $S_1$; in part (e) also $x_2 = -x_1$ |
| Degrees of freedom | 6 minus 4: 2, the coordinates $x_1(t)$, $x_2(t)$; 1 in part (e) |
| Data | $m$ [kg], $L$ [m], $\omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$], $k$ [N m$^2$]; $\gamma = g/(\omega^2L)$ and $\kappa = k/(m\omega^2L^3)$ [1] |
| Auxiliary symbols | $u_i = x_i/L$; $\sigma_i = \sqrt{1 + x_i^2/L^2}$ [1]; $\Delta x = x_1 - x_2$; $d$ distance between the particles; $D = d/L$ |
| Unknowns | $x_1(t)$, $x_2(t)$; reactions $\mathbf N_i = N_{in}\,\mathbf n_i + N_{iy}\,\mathbf j_1$ (no tangential component: smooth wire); in part (c) the motor torque $M_m$ |
| Applied forces | weights $-mg\,\mathbf k_1$; electric repulsion, equal and opposite, along the line $P_1P_2$ |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; smooth wire acting as a bead guide; $\omega$ constant (held by the motor); the wire is massless (see part (c)) |
| Readings | (1) In part (e) "$v_1(0) = L\omega$" is read as the speed of $P_1$ relative to $Oxyz$; the other reading, the rate of the abscissa equal to $L\omega$, is worked in the Answers table. (2) The initial abscissa of $P_2$ in part (e) is $-L$, by the symmetry stated |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p33-top-view.svg]]

> [!derivation] Basis of the wire frame: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙) at the vertex. With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page (thumb towards the reader, the fingers turn $\mathbf i_0$ counterclockwise by a quarter turn). A positive $\omega$ turns the wire counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf j_0$; the counterclockwise turn carries its tip to the left, so the opposite leg $\sin\omega t$ lies along minus $\mathbf i_0$ (the minus sign). The plane of the wire is seen edge-on along $\mathbf i_1$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\omega t\cos\omega t - \left(-\sin\omega t\right)\sin\omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** the matrix of Eq. 1.20 with the angle $\omega t$; heights and the weight have the same components in both frames.

![[attachments/EM-SOL/p33-wire-plane.svg]]

> [!derivation] Position vectors and local basis of the wire
> **Law:** position as the sum of its components; slope triangle; quarter turn in the plane; vector product
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.9; Notes.pdf, Eq. 3.16; Problems.pdf, p. 21
>
> The plane $Oxz$, fixed in $S_1$, is drawn with $\mathbf i_1$ to the right and $\mathbf k_1$ up; out of the paper is the cross product of $\mathbf i_1$ and $\mathbf k_1$, which is minus $\mathbf j_1$, so $\mathbf j_1$ points into the paper (⊗). A particle at the abscissa $x_i$ is reached from $O$ by $x_i$ along $\mathbf i_1$ and the height of the wire along $\mathbf k_1$. In the slope triangle the horizontal leg is $dx$ and the vertical leg $dz$; the hypotenuse lies along the wire, with length $\sigma_i\,dx$. The normal is the tangent turned a quarter turn counterclockwise in the drawing (components $(a, b)$ become $(-b, a)$), towards the concave side.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^{P_i} = \mathbf r_1^{P_i} = x_i\,\mathbf i_1 + \frac{x_i^2}{2L}\,\mathbf k_1 \quad &\text{(Eq. 3.16 with $O$ fixed and shared)} \\
> dz &= \frac{d}{dx}\left(\frac{x^2}{2L}\right)dx = \frac{2x}{2L}\,dx = \frac{x}{L}\,dx \quad &\text{(vertical leg of the slope triangle)} \\
> \mathbf t_i &= \frac{dx\,\mathbf i_1 + \frac{x_i}{L}dx\,\mathbf k_1}{\sigma_i\,dx} = \frac{1}{\sigma_i}\left(\mathbf i_1 + \frac{x_i}{L}\,\mathbf k_1\right), \quad \sigma_i^2 = 1 + \frac{x_i^2}{L^2} \quad &\text{(sum of the legs over the hypotenuse; Pythagoras)} \\
> \mathbf n_i &= \frac{1}{\sigma_i}\left(-\frac{x_i}{L}\,\mathbf i_1 + \mathbf k_1\right), \quad \mathbf t_i\cdot\mathbf n_i = \frac{1}{\sigma_i^2}\left(-\frac{x_i}{L} + \frac{x_i}{L}\right) = 0 \quad &\text{(quarter turn; orthogonal)} \\
> \mathbf t_i\times\mathbf n_i &= \frac{1}{\sigma_i^2}\left(\mathbf i_1\times\mathbf k_1 - \frac{x_i^2}{L^2}\,\mathbf k_1\times\mathbf i_1\right) = \frac{1}{\sigma_i^2}\left(-\mathbf j_1 - \frac{x_i^2}{L^2}\,\mathbf j_1\right) = -\mathbf j_1 \quad &\text{($\mathbf i_1\times\mathbf k_1 = -\mathbf j_1$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^{P_i} = x_i\,\mathbf i_1 + \frac{x_i^2}{2L}\,\mathbf k_1, \quad \mathbf t_i = \frac{\mathbf i_1 + (x_i/L)\,\mathbf k_1}{\sigma_i}, \quad \mathbf n_i = \frac{-(x_i/L)\,\mathbf i_1 + \mathbf k_1}{\sigma_i}, \quad \mathbf t_i\times\mathbf n_i = -\mathbf j_1}$$
>
> **Units:** $[x_i^2/L] = [\mathrm{L}]$; $[x_i/L] = [\sigma_i] = [1]$
> **Meaning:** $\{\mathbf t_i, \mathbf n_i, -\mathbf j_1\}$ is a right-handed orthonormal triad at each particle; the reaction of the smooth wire lies in the plane of $\mathbf n_i$ and $\mathbf j_1$.

![[attachments/EM-SOL/p33-chord.svg]]

> [!derivation] Chord between the particles
> **Law:** difference of position vectors; right triangle of the chord; difference of squares
> **Source:** Notes.pdf, Eq. 2.5; Problems.pdf, p. 21
>
> In the shaded right triangle of the chord the horizontal leg is $\Delta x$, the vertical leg is the difference of heights and the hypotenuse is the distance $d$.
>
> $$\begin{aligned}
> \overrightarrow{P_2P_1} &= \mathbf r_1^{P_1} - \mathbf r_1^{P_2} = \left(x_1 - x_2\right)\mathbf i_1 + \frac{x_1^2 - x_2^2}{2L}\,\mathbf k_1 \quad &\text{(difference of positions)} \\
> \frac{x_1^2 - x_2^2}{2L} &= \left(x_1 - x_2\right)\frac{x_1 + x_2}{2L} \quad &\text{(difference of squares)} \\
> d^2 &= \Delta x^2 + \Delta x^2\frac{\left(x_1 + x_2\right)^2}{4L^2} = \Delta x^2\left[1 + \frac{\left(x_1 + x_2\right)^2}{4L^2}\right] \quad &\text{(Pythagoras)}
> \end{aligned}$$
>
> $$\boxed{\overrightarrow{P_2P_1} = \Delta x\left[\mathbf i_1 + \frac{x_1 + x_2}{2L}\,\mathbf k_1\right], \qquad d = \left|\Delta x\right|\sqrt{1 + \frac{\left(x_1 + x_2\right)^2}{4L^2}}}$$
>
> **Units:** $[d] = [\Delta x] = [\mathrm{L}]$
> **Meaning:** the slope of the chord is the mean of the slopes of the wire at its two ends.

### Kinematics

> [!derivation] Motion of the wire frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed axis; $\omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) &= -\omega\sin\omega t\,\mathbf i_0 + \omega\cos\omega t\,\mathbf j_0 = \omega\,\mathbf j_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from $S_1$ the unit vectors are constant; seen from $S_0$ the horizontal ones turn with the wire.

#### (a) Relative position, velocity and acceleration

> [!derivation] Relative velocity and relative acceleration of each particle
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 21
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\frac{x_i^2}{2L}\right) &= \frac{2x_i}{2L}\,\dot x_i = \frac{x_i\dot x_i}{L} \quad &\text{(chain rule)} \\
> \mathbf v_1^{P_i} &= \dot x_i\,\mathbf i_1 + \frac{x_i\dot x_i}{L}\,\mathbf k_1 = \sigma_i\dot x_i\,\mathbf t_i \quad &\text{(components differentiated; Eq. 3.19)} \\
> \frac{d}{dt}\left(x_i\dot x_i\right) &= \dot x_i\dot x_i + x_i\ddot x_i \quad &\text{(product rule)} \\
> \mathbf a_1^{P_i} &= \ddot x_i\,\mathbf i_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\,\mathbf k_1 \quad &\text{(components differentiated again; Eq. 3.24)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^{P_i} = x_i\,\mathbf i_1 + \frac{x_i^2}{2L}\,\mathbf k_1, \quad \mathbf v_1^{P_i} = \dot x_i\,\mathbf i_1 + \frac{x_i\dot x_i}{L}\,\mathbf k_1, \quad \mathbf a_1^{P_i} = \ddot x_i\,\mathbf i_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\,\mathbf k_1 \quad (i = 1, 2)}$$
>
> **Units:** $[\dot x_i] = [\mathrm{L\,T^{-1}}]$; $[\ddot x_i] = [\dot x_i^2/L] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the relative velocity is tangent to the wire and the relative acceleration lies in the plane of the wire.

> [!derivation] Absolute acceleration: centripetal and Coriolis terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> $$\begin{aligned}
> \mathbf v_0^{P_i} &= \dot x_i\,\mathbf i_1 + x_i\,\omega\,\mathbf j_1 + \frac{x_i\dot x_i}{L}\,\mathbf k_1 = \mathbf v_1^{P_i} + \omega x_i\,\mathbf j_1 \quad &\text{(product rule; derivative of $\mathbf i_1$; $\mathbf k_1$ constant)} \\
> \left.\frac{d\mathbf v_1^{P_i}}{dt}\right|_0 &= \mathbf a_1^{P_i} + \dot x_i\,\omega\,\mathbf j_1 \quad &\text{(product rule; the turning of $\mathbf i_1$ inside $\mathbf v_1^{P_i}$)} \\
> \left.\frac{d}{dt}\right|_0\left(\omega x_i\,\mathbf j_1\right) &= \omega\dot x_i\,\mathbf j_1 + \omega x_i\left(-\omega\,\mathbf i_1\right) \quad &\text{(product rule; derivative of $\mathbf j_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^{P_i} &= 2\omega\,\mathbf k_1\times\left(\dot x_i\,\mathbf i_1 + \frac{x_i\dot x_i}{L}\,\mathbf k_1\right) = 2\omega\dot x_i\,\mathbf j_1 \quad &\text{(the two $\mathbf j_1$ terms above)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^{P_i}\right) &= \omega\,\mathbf k_1\times\left(\omega x_i\,\mathbf j_1\right) = -\omega^2x_i\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^{P_i} = \mathbf a_1^{P_i} - \omega^2x_i\,\mathbf i_1 + 2\omega\dot x_i\,\mathbf j_1}$$
>
> **Units:** $[\omega^2x_i] = [\omega\dot x_i] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the centripetal term points horizontally to the axis and the Coriolis term is normal to the plane of the wire; with $O$ fixed and the rate constant there are no origin or Euler terms.

### Forces and Equations of Motion

![[attachments/EM-SOL/p33-fbd.svg]]

#### (b) Newton's second law for each particle in Oxyz

> [!derivation] Actual and inertia forces on each particle
> **Law:** weight; repulsion along the line of the particles; smooth reaction; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.16; [Lecture 5, Slide 28]; Problems.pdf, p. 21
>
> The force on $P_1$ has the magnitude $k$ over the square of $d$ and the direction from $P_2$ to $P_1$ (repulsion); the force on $P_2$ is opposite.
>
> $$\begin{aligned}
> \mathbf W_i &= -mg\,\mathbf k_1, \quad \mathbf N_i = N_{in}\,\mathbf n_i + N_{iy}\,\mathbf j_1 \quad &\text{(weight; smooth wire)} \\
> \mathbf F_{E1} &= \frac{k}{d^2}\,\frac{\overrightarrow{P_2P_1}}{d} = \frac{k\,\Delta x}{d^3}\left[\mathbf i_1 + \frac{x_1 + x_2}{2L}\,\mathbf k_1\right], \quad \mathbf F_{E2} = -\mathbf F_{E1} \quad &\text{(chord box; action and reaction)} \\
> \mathbf F_{A,i} &= \mathbf 0, \quad \mathbf F_{E\!u,i} = \mathbf 0 \quad &\text{($O$ fixed; $\boldsymbol\alpha_{10}$ zero)} \\
> \mathbf F_{C,i} &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^{P_i}\right) = m\omega^2x_i\,\mathbf i_1 \quad &\text{(centrifugal: composition box times $-m$)} \\
> \mathbf F_{COR,i} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^{P_i} = -2m\omega\dot x_i\,\mathbf j_1 \quad &\text{(Coriolis: composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{m\,\mathbf a_1^{P_i} = -mg\,\mathbf k_1 + N_{in}\,\mathbf n_i + N_{iy}\,\mathbf j_1 + \mathbf F_{Ei} + m\omega^2x_i\,\mathbf i_1 - 2m\omega\dot x_i\,\mathbf j_1, \qquad i = 1, 2}$$
>
> **Units:** $[k/d^2] = [mg] = [m\omega^2x_i] = [m\omega\dot x_i] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** this is Newton's second law of each particle in $Oxyz$ (Eq. 4.63): six scalar equations for the six unknowns, two coordinates and four reaction components. The centrifugal force pushes each particle away from the axis.

> [!derivation] Projections: equations of motion and reactions
> **Law:** projection of Newton's second law on $\sigma_i\mathbf t_i$, $\mathbf j_1$ and $\sigma_i\mathbf n_i$
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.17; [Lecture 5, Slide 28]
>
> The projection on the tangent removes the reaction. The electric force on $P_2$ is the one on $P_1$ with the indices exchanged, because both the sign of $\Delta x$ and the direction of the force reverse.
>
> $$\begin{aligned}
> m\,\mathbf a_1^{P_1}\cdot\left(\mathbf i_1 + \tfrac{x_1}{L}\mathbf k_1\right) &= m\left[\ddot x_1 + \frac{x_1}{L}\cdot\frac{\dot x_1^2 + x_1\ddot x_1}{L}\right] = m\left[\left(1 + \frac{x_1^2}{L^2}\right)\ddot x_1 + \frac{x_1\dot x_1^2}{L^2}\right] \quad &\text{(left side, tangent)} \\
> \left(-mg\,\mathbf k_1 + m\omega^2x_1\,\mathbf i_1\right)\cdot\left(\mathbf i_1 + \tfrac{x_1}{L}\mathbf k_1\right) &= m\omega^2x_1 - mg\frac{x_1}{L} = m\left(\omega^2 - \frac{g}{L}\right)x_1 \quad &\text{(weight and centrifugal; Coriolis and reaction give 0)} \\
> \mathbf F_{E1}\cdot\left(\mathbf i_1 + \tfrac{x_1}{L}\mathbf k_1\right) &= \frac{k\,\Delta x}{d^3}\left[1 + \frac{x_1\left(x_1 + x_2\right)}{2L^2}\right] \quad &\text{(electric, tangent)} \\
> \mathbf j_1:\ 0 &= N_{iy} - 2m\omega\dot x_i \quad &\text{(binormal direction)} \\
> m\,\mathbf a_1^{P_i}\cdot\left(-\tfrac{x_i}{L}\mathbf i_1 + \mathbf k_1\right) &= m\left[-\frac{x_i\ddot x_i}{L} + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\right] = \frac{m\dot x_i^2}{L} \quad &\text{(left side, normal)} \\
> \mathbf F_{E1}\cdot\left(-\tfrac{x_1}{L}\mathbf i_1 + \mathbf k_1\right) &= \frac{k\,\Delta x}{d^3}\left[-\frac{x_1}{L} + \frac{x_1 + x_2}{2L}\right] = -\frac{k\,\Delta x^2}{2Ld^3} \quad &\text{(electric, normal; the same value for $P_2$)} \\
> \frac{m\dot x_i^2}{L} &= \sigma_iN_{in} - mg - \frac{m\omega^2x_i^2}{L} - \frac{k\,\Delta x^2}{2Ld^3} \quad &\text{(normal component: $\mathbf n_i\cdot\sigma_i\mathbf n_i = \sigma_i$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} m\left[\left(1 + \frac{x_1^2}{L^2}\right)\ddot x_1 + \frac{x_1\dot x_1^2}{L^2}\right] = m\left(\omega^2 - \frac{g}{L}\right)x_1 + \frac{k\left(x_1 - x_2\right)}{d^3}\left[1 + \frac{x_1\left(x_1 + x_2\right)}{2L^2}\right] \cr m\left[\left(1 + \frac{x_2^2}{L^2}\right)\ddot x_2 + \frac{x_2\dot x_2^2}{L^2}\right] = m\left(\omega^2 - \frac{g}{L}\right)x_2 + \frac{k\left(x_2 - x_1\right)}{d^3}\left[1 + \frac{x_2\left(x_1 + x_2\right)}{2L^2}\right] \cr N_{iy} = 2m\omega\dot x_i, \qquad N_{in} = \frac{m}{\sigma_i}\left[\frac{\dot x_i^2}{L} + g + \frac{\omega^2x_i^2}{L}\right] + \frac{k\left(x_1 - x_2\right)^2}{2L\sigma_id^3} \end{gathered}}$$
>
> **Units:** every term of the equations of motion $[\mathrm{M\,L\,T^{-2}}]$; $[k\,\Delta x^2/(L d^3)] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** weight and centrifugal force combine along the wire into one linear term in the abscissa: restoring towards the vertex if gravity wins ($\gamma$ above 1), repelling if the rotation wins. The reaction normal to the plane cancels the Coriolis force.

### Answers and Checks

#### (c) Motor torque that keeps omega constant

> [!derivation] Balance of moments on the wire about Oz
> **Law:** action and reaction between wire and particles; moment of a force about an axis; massless guide
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53; Problems.pdf, p. 21
>
> The particles push on the wire with minus the reactions. The wire is taken massless, so the moments about $Oz$ of all the actions on it add up to zero (a wire with mass, turning at a constant rate about its axis of symmetry, keeps its own angular momentum about the axis constant: rigid body result, **extension**; the torque is the same). The bearings act on the axis and have no moment about it. The component along $\mathbf k_1$ of the cross product of $x_i\,\mathbf i_1 + z_i\,\mathbf k_1$ with $N_{ix}\,\mathbf i_1 + N_{iy}\,\mathbf j_1 + N_{iz}\,\mathbf k_1$ is the first component of the first factor times the second of the second minus the second of the first times the first of the second.
>
> $$\begin{aligned}
> \left[\mathbf r_1^{P_i}\times\left(-\mathbf N_i\right)\right]\cdot\mathbf k_1 &= -\left(x_iN_{iy} - 0\cdot N_{ix}\right) = -x_iN_{iy} \quad &\text{(moment of the push of $P_i$)} \\
> M_m - x_1N_{1y} - x_2N_{2y} &= 0 \quad &\text{(massless wire)} \\
> M_m &= x_1\cdot 2m\omega\dot x_1 + x_2\cdot 2m\omega\dot x_2 \quad &\text{(part (b): $N_{iy} = 2m\omega\dot x_i$)}
> \end{aligned}$$
>
> $$\boxed{M_m = 2m\omega\left(x_1\dot x_1 + x_2\dot x_2\right)}$$
>
> **Units:** $[m\omega x\dot x] = [\mathrm{M\,L^2\,T^{-2}}]$, a torque
> **Meaning:** when the particles move away from the axis the motor must supply angular momentum (positive torque); when they move towards it, it must brake.

> [!derivation] Check: angular momentum of the particles about Oz
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the external forces on the particles
> **Source:** Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$ the position of $P_i$ has the components $(x_i, 0, z_i)$ and its absolute velocity $(\dot x_i, \omega x_i, \dot z_i)$ (composition box). The weights are parallel to the axis and the electric pair acts along the line of the particles, so its total moment is zero; only the reactions have an axial moment, the moment $M_m$ transmitted through the wire.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf k_1 &= \sum_i m\left(x_i\cdot\omega x_i - 0\cdot\dot x_i\right) = m\omega\left(x_1^2 + x_2^2\right) \quad &\text{(Eq. 4.48, axial component)} \\
> \frac{d}{dt}\left[m\omega\left(x_1^2 + x_2^2\right)\right] &= m\omega\left(2x_1\dot x_1 + 2x_2\dot x_2\right) \quad &\text{(chain rule; $\omega$ constant)} \\
> \sum_i\left(\mathbf r_1^{P_i}\times\mathbf N_i\right)\cdot\mathbf k_1 &= x_1N_{1y} + x_2N_{2y} \quad &\text{(Eq. 4.53)}
> \end{aligned}$$
>
> $$\boxed{x_1N_{1y} + x_2N_{2y} = 2m\omega\left(x_1\dot x_1 + x_2\dot x_2\right) = M_m}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the same torque by a second route, without inertia forces.

#### (d) Equilibrium configurations in Oxyz

> [!derivation] Equilibrium equations in nondimensional form and their sum
> **Law:** relative equilibrium: the rates and accelerations vanish; scaling by $m\omega^2L$
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 21
>
> With the rates and accelerations zero, the equations of motion become algebraic. Divide by $m\omega^2L$ and write $\Sigma$ for the sum of the $u_i$.
>
> $$\begin{aligned}
> f_1 &\equiv \left(1 - \gamma\right)u_1 + \frac{\kappa}{D^3}\left(u_1 - u_2\right)\left[1 + \frac{u_1\Sigma}{2}\right] = 0 \quad &\text{(equation of $P_1$)} \\
> f_2 &\equiv \left(1 - \gamma\right)u_2 + \frac{\kappa}{D^3}\left(u_2 - u_1\right)\left[1 + \frac{u_2\Sigma}{2}\right] = 0 \quad &\text{(equation of $P_2$)} \\
> D &= \left|u_1 - u_2\right|\sqrt{1 + \frac{\Sigma^2}{4}} \quad &\text{(chord box divided by $L$)} \\
> f_1 + f_2 &= \left(1 - \gamma\right)\Sigma + \frac{\kappa}{D^3}\left(u_1 - u_2\right)\frac{\left(u_1 - u_2\right)\Sigma}{2} = \Sigma\left[\left(1 - \gamma\right) + \frac{\kappa\left(u_1 - u_2\right)^2}{2D^3}\right] = 0 \quad &\text{(the constant 1 cancels in the brackets)}
> \end{aligned}$$
>
> $$\boxed{\Sigma = 0 \ \text{(symmetric)} \qquad \text{or} \qquad \gamma - 1 = \frac{\kappa\left(u_1 - u_2\right)^2}{2D^3} \ \text{(only if } \gamma \gt 1\text{)}}$$
>
> **Units:** $[\gamma] = [\kappa] = [u_i] = [1]$
> **Meaning:** only the two nondimensional numbers matter: weight against centrifugal force, and repulsion against centrifugal force.

> [!derivation] Cases gamma below 1 and gamma equal to 1
> **Law:** sign of the terms of the equilibrium equations
> **Source:** Notes.pdf, Eq. 4.32; Problems.pdf, p. 21
>
> Two particles cannot occupy the same point, so the difference of the $u_i$ is not zero and the symmetric case has the first abscissa not zero.
>
> $$\begin{aligned}
> \Sigma = 0:\quad u_2 &= -u_1, \quad D = 2\left|u_1\right|, \quad f_1 = u_1\left[\left(1 - \gamma\right) + \frac{2\kappa}{8\left|u_1\right|^3}\right] \quad &\text{(symmetric case)} \\
> \gamma \lt 1:\quad \left(1 - \gamma\right) + \frac{\kappa}{4\left|u_1\right|^3} &\gt 0 \ \text{ and } \ \left(1 - \gamma\right) + \frac{\kappa\left(u_1 - u_2\right)^2}{2D^3} \gt 0 \quad &\text{(neither alternative can vanish)} \\
> \gamma = 1:\quad \frac{\kappa}{4\left|u_1\right|^3} &= 0 \ \text{ and } \ \frac{\kappa\left(u_1 - u_2\right)^2}{2D^3} = 0 \iff \kappa = 0 \quad &\text{(both alternatives need $\kappa = 0$)} \\
> \gamma = 1,\ \kappa = 0:\quad f_1 &= 0\cdot u_1 + 0 = 0, \quad f_2 = 0 \quad &\text{(every configuration)}
> \end{aligned}$$
>
> $$\boxed{\gamma \lt 1: \text{ no equilibrium}; \qquad \gamma = 1: \text{ equilibrium only if } \kappa = 0, \text{ and then every position is one}}$$
>
> **Units:** dimensionless
> **Meaning:** when the rotation beats gravity everywhere along the wire, nothing holds the particles, and the repulsion only pushes them further out; when they balance exactly, any repulsion breaks the balance.

> [!derivation] Case gamma above 1: symmetric and asymmetric equilibria
> **Law:** solution of the algebraic equilibrium equations
> **Source:** Notes.pdf, Eq. 4.32; Problems.pdf, p. 21
>
> In the asymmetric case the second alternative of the sum gives $\kappa$ over the cube of $D$, which is substituted in the equation of $P_1$; then $c$ denotes the fourth root of $4\kappa$ over $\gamma - 1$.
>
> $$\begin{aligned}
> \Sigma = 0:\quad \left(1 - \gamma\right) + \frac{\kappa}{4\left|u_1\right|^3} &= 0 \;\Rightarrow\; \left|u_1\right|^3 = \frac{\kappa}{4\left(\gamma - 1\right)} \;\Rightarrow\; x_1^2 = \left[\frac{\kappa L^3}{4\left(\gamma - 1\right)}\right]^{2/3} \quad &\text{(symmetric; $x_1 = Lu_1$)} \\
> \Sigma \ne 0:\quad \frac{\kappa}{D^3} &= \frac{2\left(\gamma - 1\right)}{\left(u_1 - u_2\right)^2} \quad &\text{(second alternative)} \\
> \left(1 - \gamma\right)u_1 + \frac{2\left(\gamma - 1\right)}{u_1 - u_2}\left[1 + \frac{u_1\left(u_1 + u_2\right)}{2}\right] &= 0 \;\Rightarrow\; u_1\left(u_1 - u_2\right) = 2 + u_1\left(u_1 + u_2\right) \quad &\text{(in $f_1$; divided by $\gamma - 1$, times $u_1 - u_2$)} \\
> -u_1u_2 &= 2 + u_1u_2 \;\Rightarrow\; u_1u_2 = -1, \ \ x_1x_2 = -L^2 \quad &\text{(opposite branches)} \\
> u_1 - u_2 &= u_1 + \frac{1}{u_1}, \quad 1 + \frac{\Sigma^2}{4} = \frac{\left(u_1 + 1/u_1\right)^2}{4}, \quad D^3 = \frac{\left|u_1 + 1/u_1\right|^6}{8} \quad &\text{($u_2 = -1/u_1$; $\left(u_1 - 1/u_1\right)^2 + 4 = \left(u_1 + 1/u_1\right)^2$)} \\
> \gamma - 1 &= \frac{\kappa\left(u_1 + 1/u_1\right)^2\cdot 8}{2\left(u_1 + 1/u_1\right)^6} = \frac{4\kappa}{\left(u_1 + 1/u_1\right)^4} \;\Rightarrow\; \left|u_1 + \frac{1}{u_1}\right| = c \quad &\text{(back in the sum condition)} \\
> u_1^2 - c\,u_1 + 1 &= 0 \;\Rightarrow\; u_1 = \frac{c \pm \sqrt{c^2 - 4}}{2}, \quad u_2 = -\frac{1}{u_1} \quad &\text{($u_1 \gt 0$; both roots, real only if $c \ge 2$)} \\
> \gamma = 2,\ \kappa = 8:\quad c &= 32^{1/4} = 2.3784, \quad u_1 = 1.8328, \quad u_2 = -0.5456, \quad \Sigma = 1.2872, \quad D = 2\sqrt2, \quad \frac{\kappa}{D^3} = 0.35355 \quad &\text{(example)} \\
> f_1 &= -1.8328 + 0.35355\cdot 2.3784\cdot\left(1 + \tfrac12\cdot 1.8328\cdot 1.2872\right) = -1.8328 + 0.35355\cdot 2.3784\cdot 2.1796 = -1.8328 + 1.8328 \simeq 0 \quad &\text{(first equation)} \\
> f_2 &= 0.5456 + 0.35355\cdot\left(-2.3784\right)\cdot\left(1 - \tfrac12\cdot 0.5456\cdot 1.2872\right) = 0.5456 - 0.35355\cdot 2.3784\cdot 0.6488 = 0.5456 - 0.5456 \simeq 0 \quad &\text{(second equation)} \\
> \left|u_1\right|^3 &= \frac{8}{4\cdot 1} = 2 \;\Rightarrow\; u_1 = 1.2599, \quad f_1 = -1.2599 + \frac{8}{4\cdot 2}\cdot 1.2599 = 0 \quad &\text{(symmetric root, same example)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \text{symmetric: } x_1 = -x_2,\quad x_1^2 = \left[\frac{\kappa L^3}{4\left(\gamma - 1\right)}\right]^{2/3}; \cr \text{asymmetric: } x_1x_2 = -L^2,\quad \frac{x_1}{L} = \frac{c \pm \sqrt{c^2 - 4}}{2},\quad c = \left(\frac{4\kappa}{\gamma - 1}\right)^{1/4}, \ \text{ real and distinct only for } \kappa \gt 4\left(\gamma - 1\right) \end{gathered}}$$
>
> **Units:** $[x_1^2] = [L^2] = [\mathrm{L^2}]$
> **Meaning:** gravity, stronger than the rotation, acts along the wire as a spring towards the vertex that balances the repulsion. The two roots of the asymmetric case are a mirror pair (one root is the reciprocal of the other), with the chord through the point at height one half of $L$ on the axis; at the limiting value of $\kappa$ they merge into the symmetric equilibrium at the abscissa $L$. In the example of the last three rows ($\gamma$ equal to 2, $\kappa$ equal to 8) the asymmetric pair 1.833 and $-0.546$ and the symmetric value 1.260 satisfy the equilibrium equations to round-off. No equilibrium has both particles on the same branch, because both alternatives give abscissas of opposite sign.

#### (e) Symmetric motion with gamma and kappa equal to 2: extreme values of x1

> [!derivation] Why the energy of the pair in Oxyz is conserved, and its potentials
> **Law:** power of each force on the relative velocities; potentials as minus the work, with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.24; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> A symmetric start stays symmetric: the equations of part (b) are unchanged when the abscissas change sign and the labels are exchanged, so the symmetry needs no extra force. Two reasons for the conservation. First, the forces that do no work in $S_1$: the reactions (wire at rest in $S_1$, smooth), the Coriolis forces (normal to the relative velocities), and the origin and Euler forces, which vanish. Second, the forces that work have potentials of the positions in $S_1$ only: the weights, the repulsion (central pair, a function of the distance) and the centrifugal forces (rate constant, axis fixed). Along the wire the displacement is $\mathbf i_1$ plus $x/L$ times $\mathbf k_1$, times $dx$.
>
> $$\begin{aligned}
> V_g(x_i) &= -\int_0^{x_i}\left(-mg\,\mathbf k_1\right)\cdot\left(\mathbf i_1 + \frac{x'}{L}\mathbf k_1\right)dx' = \frac{mg}{L}\left[\frac{x'^2}{2}\right]_0^{x_i} = \frac{mgx_i^2}{2L} \quad &\text{(Eq. 4.14; Barrow's rule)} \\
> V_C(x_i) &= -\int_0^{x_i}m\omega^2x'\,dx' = -m\omega^2\left[\frac{x'^2}{2}\right]_0^{x_i} = -\tfrac12 m\omega^2x_i^2 \quad &\text{(Eq. 4.14; Barrow's rule)} \\
> V_E(d) &= -\int_{\infty}^{d}\frac{k}{d'^2}\,dd' = -\left[-\frac{k}{d'}\right]_{\infty}^{d} = \frac{k}{d} \quad &\text{(repulsion along growing $d$; zero at infinity; Barrow's rule)} \\
> T_1 &= \sum_i\tfrac12 m\,\mathbf v_1^{P_i}\cdot\mathbf v_1^{P_i} = \sum_i\tfrac12 m\dot x_i^2\left(1 + \frac{x_i^2}{L^2}\right) \quad &\text{(kinetic energy of the pair in $S_1$)} \\
> x_1 = x \gt 0,\ x_2 = -x:\quad d &= 2x, \quad T_1 = m\dot x^2\left(1 + \frac{x^2}{L^2}\right) \quad &\text{(symmetric motion)} \\
> E_1 &= m\dot x^2\left(1 + \frac{x^2}{L^2}\right) + \frac{mgx^2}{L} - m\omega^2x^2 + \frac{k}{2x} \quad &\text{(two weights, two centrifugal terms, one pair)}
> \end{aligned}$$
>
> $$\boxed{E_1 = m\dot x^2\left(1 + \frac{x^2}{L^2}\right) + m\left(\frac{g}{L} - \omega^2\right)x^2 + \frac{k}{2x} = \text{const}}$$
>
> **Units:** $[m\dot x^2] = [mgx^2/L] = [m\omega^2x^2] = [k/x] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the abscissa stays positive: the repulsion potential grows without bound as the particles approach the vertex together.

> [!derivation] Initial energy and the cubic of the turning points
> **Law:** initial conditions in the energy integral; turning points where the kinetic energy vanishes; all three roots of the cubic
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Problems.pdf, p. 21
>
> At the start the relative velocity of part (a) is evaluated at the abscissa $L$ and its length is set to $L\omega$ (Reading 1). Then everything is divided by $m\omega^2L^2$ with $u$ equal to $x/L$. The roots of the cubic follow from the triple-angle identity with $u$ written as twice a cosine.
>
> $$\begin{aligned}
> \left|\mathbf v_1^{P_1}(0)\right|^2 &= \dot x(0)^2\left(1 + \frac{L^2}{L^2}\right) = 2\dot x(0)^2 = L^2\omega^2 \;\Rightarrow\; \dot x(0) = \frac{L\omega}{\sqrt2} \quad &\text{(part (a) at $t = 0$; $\dot x(0) \gt 0$)} \\
> \frac{E_1}{m\omega^2L^2} &= \frac{\dot x^2}{\omega^2L^2}\left(1 + u^2\right) + \left(\gamma - 1\right)u^2 + \frac{\kappa}{2u} \quad &\text{(scaled energy; $k/(2x) = m\omega^2L^2\,\kappa/(2u)$)} \\
> \frac{E_1(0)}{m\omega^2L^2} &= \frac12\cdot 2 + \left(2 - 1\right)\cdot 1 + \frac{2}{2} = 3 \quad &\text{($u = 1$, $\gamma = \kappa = 2$)} \\
> u^2 + \frac{1}{u} &= 3 \;\Rightarrow\; u^3 - 3u + 1 = 0 \quad &\text{(rate zero; times $u \gt 0$)} \\
> u = 2\cos\theta:\quad 8\cos^3\theta - 6\cos\theta + 1 &= 2\left(4\cos^3\theta - 3\cos\theta\right) + 1 = 2\cos 3\theta + 1 = 0 \quad &\text{(triple-angle identity)} \\
> \cos 3\theta = -\tfrac12 &\Rightarrow\; \theta = \tfrac{2\pi}{9},\ \tfrac{4\pi}{9},\ \tfrac{8\pi}{9} \;\Rightarrow\; u = 1.532,\ 0.347,\ -1.879 \quad &\text{(the three roots)} \\
> 3 - u^2 - \frac1u \ge 0 &\iff u^3 - 3u + 1 \le 0 \ \ (u \gt 0); \quad 1 - 3 + 1 = -1 \le 0 \text{ at } u = 1 \quad &\text{(allowed region contains the start)}
> \end{aligned}$$
>
> $$\boxed{\frac{x_1^3}{L^3} - 3\frac{x_1}{L} + 1 = 0: \qquad x_{1,max} = 2L\cos\frac{2\pi}{9} \simeq 1.532\,L, \qquad x_{1,min} = 2L\cos\frac{4\pi}{9} \simeq 0.347\,L}$$
>
> **Units:** $[u] = [1]$; $[x_1] = [\mathrm{L}]$
> **Meaning:** the negative root, $-1.879$, is rejected: the abscissa of $P_1$ stays positive. The start lies between the two positive roots, so $P_1$ first moves out to 1.532 times $L$ and then oscillates between the two extreme values, with $P_2$ as its mirror image.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Position, velocity, acceleration | $\mathbf r_1^{P_i} = x_i\,\mathbf i_1 + \frac{x_i^2}{2L}\mathbf k_1$, $\mathbf v_1^{P_i} = \dot x_i\,\mathbf i_1 + \frac{x_i\dot x_i}{L}\mathbf k_1$, $\mathbf a_1^{P_i} = \ddot x_i\,\mathbf i_1 + \frac{\dot x_i^2 + x_i\ddot x_i}{L}\mathbf k_1$ ($i = 1, 2$) |
| (b) Newton's second law | $m\,\mathbf a_1^{P_i} = -mg\,\mathbf k_1 + N_{in}\mathbf n_i + N_{iy}\mathbf j_1 + \mathbf F_{Ei} + m\omega^2x_i\,\mathbf i_1 - 2m\omega\dot x_i\,\mathbf j_1$, $\mathbf F_{E1} = -\mathbf F_{E2} = \frac{k\Delta x}{d^3}[\mathbf i_1 + \frac{x_1 + x_2}{2L}\mathbf k_1]$; tangential projections give the two equations of motion, $N_{iy} = 2m\omega\dot x_i$ and $N_{in}$ (box of part (b)) |
| (c) Motor torque | $M_m = 2m\omega(x_1\dot x_1 + x_2\dot x_2)$ along $\mathbf k$ |
| (d) Equilibria | $\gamma \lt 1$: none; $\gamma = 1$: only if $\kappa = 0$ (then every position); $\gamma \gt 1$: symmetric $x_1 = -x_2$, $x_1^2 = [\kappa L^3/(4(\gamma - 1))]^{2/3}$; asymmetric $x_1x_2 = -L^2$ with $x_1/L = (c \pm \sqrt{c^2 - 4})/2$, $c = (4\kappa/(\gamma - 1))^{1/4}$, for $\kappa \gt 4(\gamma - 1)$ |
| (e) Extreme values of $x_1$ | $x_1^3/L^3 - 3x_1/L + 1 = 0$: $x_{1,min} = 2L\cos(4\pi/9) \simeq 0.347L$, $x_{1,max} = 2L\cos(2\pi/9) \simeq 1.532L$ |
| (e) Other reading of the initial velocity | if $\dot x_1(0) = L\omega$ instead of the speed: scaled energy 4, $x_1^3/L^3 - 4x_1/L + 1 = 0$, extreme values $0.254L$ and $1.861L$ |

**Check against the official key:** Problems.pdf, p. 75 prints the torque, the equilibria and the cubics of the extreme values for positive and negative $x_1$. The torque, the cases of $\gamma$ below and equal to 1, the symmetric equilibrium and the cubics coincide with parts (c), (d) and (e) (box below); the statement on the asymmetric equilibria differs (warning below). The cubic for negative $x_1$ is the mirror case of a start on the other branch, which does not apply to a start at $L$. The key's cubic confirms Reading 1 of the initial velocity (the speed); the other reading gives a different cubic.

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison
> **Source:** Problems.pdf, p. 75
>
> $$\begin{aligned}
> \text{key: } M &= 2m\omega\left(\dot x_1x_1 + \dot x_2x_2\right) = M_m \quad &\text{(part (c))} \\
> \text{key: } \gamma \lt 1 &: \text{none}; \quad \gamma = 1: \text{ only } \kappa = 0, \text{ all positions} \quad &\text{(part (d), first box of cases)} \\
> \text{key: } \gamma \gt 1 &: \ x_1 = -x_2,\ x_1^2 = \left[\frac{\kappa L^3}{4\left(\gamma - 1\right)}\right]^{2/3}, \text{ and "asymmetric ones also exist"} \quad &\text{(part (d); the key adds $x_1x_2 \lt 0$ for the symmetric one)} \\
> \text{key: } \frac{x_1^3}{L^3} - 3\frac{x_1}{L} &+ 1 = 0 \ (x_1 \gt 0), \quad \frac{x_1^3}{L^3} - 3\frac{x_1}{L} - 1 = 0 \ (x_1 \lt 0) \quad &\text{(part (e); the second is the first with $x_1 \to -x_1$)}
> \end{aligned}$$
>
> $$\boxed{\text{torque, symmetric equilibrium, cases } \gamma \le 1 \text{ and the cubic of the extreme values coincide with the key}}$$
>
> **Units:** $[M_m] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** every result printed by the key is recovered, except the statement on the asymmetric equilibria (warning below).

> [!warning] Discrepancy with the official solution
> The key says, for $\gamma$ above 1, that asymmetric equilibrium configurations also exist, with no condition. This solution finds that an asymmetric equilibrium must have $x_1x_2$ equal to $-L^2$ and $|x_1/L + L/x_1|$ equal to $c$, the fourth root of $4\kappa/(\gamma - 1)$; since $|u + 1/u|$ is never below 2, such configurations exist (distinct from the symmetric one) only for $\kappa$ above $4(\gamma - 1)$, the case in which the symmetric equilibrium lies beyond the abscissa $L$. For $\kappa$ at most $4(\gamma - 1)$ the only equilibrium is the symmetric one. Check: with $\gamma$ equal to 2 and $\kappa$ equal to 2, $c$ is the fourth root of 8, 1.68, below 2, so the quadratic for $u_1$ has no real root.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> \kappa \to 0:\quad x_1^2 &= \left[\frac{\kappa L^3}{4\left(\gamma - 1\right)}\right]^{2/3} \to 0 \quad &\text{(no repulsion: both particles at the vertex)} \\
> \gamma \to 1^+:\quad x_1^2 &\to \infty \quad &\text{(the restoring term vanishes: nothing balances the repulsion)} \\
> \omega \to 0:\quad N_{iy} &\to 0, \quad M_m \to 0 \quad &\text{(no Coriolis force and no torque without rotation)} \\
> x_i = 0:\quad \mathbf t_i &= \mathbf i_1, \quad \mathbf n_i = \mathbf k_1 \quad &\text{(at the vertex the wire is horizontal)}
> \end{aligned}$$
>
> $$\boxed{\kappa \to 0: \text{ equilibrium at the vertex}; \quad \gamma \to 1^+: \text{ equilibrium at infinity}; \quad \omega \to 0: \text{ no torque}}$$
>
> **Units:** dimensionless
> **Meaning:** each limit matches the physical picture: gravity pulls both particles to the vertex, the repulsion separates them and the rotation pushes them out.

---

## Problem 34: Particle on a Circular Wire in an Oscillating Vertical Plane

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides without friction on a circular wire of centre $C$ and radius $R$, in a vertical plane $Oxy$ that swings about the vertical axis $Oy$ with the prescribed angular velocity $A\omega\sin(\omega t)$ along $\mathbf j$ (Problems.pdf, p. 22). The statement asks for the relative position, velocity and acceleration, the forces, whether the mechanical energy seen from $Oxy$ is conserved, the equation of motion, the reaction, and the small oscillations about the lowest point. The wire is at rest in $Oxyz$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ on the rotation axis (fixed), $\mathbf j_0$ vertical, up, $\mathbf k_0 = \mathbf i_0\times\mathbf j_0$ |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, the frame $Oxyz$ of the statement, attached to the plane of the wire: $\mathbf i_1$ along $Ox$, $\mathbf j_1 = \mathbf j_0$ along the axis, $\mathbf k_1 = \mathbf i_1\times\mathbf j_1$ normal to the plane; it coincides with $S_0$ at $t = 0$ |
| Wire | circle of centre $C$ on $Ox$ at distance $R$ from $O$ and radius $R$: it passes through $O$ (read from the figure) |
| Polar basis at $P$ | $\{\mathbf e_r, \mathbf e_\varphi, \mathbf k_1\}$: $\mathbf e_r$ from $C$ to $P$, $\mathbf e_\varphi$ tangent in the sense of growing $\varphi$ |
| Coordinate | $\varphi$, angle at $C$ from $Ox$ to $\overrightarrow{CP}$, counterclockwise towards $\mathbf j_1$ |
| Angle of the plane | $\psi(t)$, rotation of $S_1$ about $\mathbf j_0$, with rate $\Omega(t) = A\omega\sin\omega t$ and $\psi(0) = 0$ |
| Constraints | $z_1 = 0$ and the circle: two holonomic, smooth, bilateral constraints, fixed in $S_1$ |
| Degrees of freedom | 3 minus 2: 1, the coordinate $\varphi(t)$ (the motion of the plane is prescribed) |
| Data | $m$ [kg], $R$ [m], $g$ [m s$^{-2}$], $A$ [1], $\omega$ [rad s$^{-1}$] |
| Unknowns | $\varphi(t)$; the reaction $\mathbf N = N_1\,\mathbf e_r + N_2\,\mathbf k_1$ (no tangential component: smooth wire) |
| Applied forces | weight $-mg\,\mathbf j_1$ |
| Inertia forces (in $S_1$) | Euler, centrifugal and Coriolis; no origin term ($O$ fixed) (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; smooth wire acting as a bead guide; the swing of the plane is imposed whatever the particle does |

### Change of Basis and Position Vector

> [!derivation] Angle turned by the plane
> **Law:** angle as the time integral of the angular rate; substitution in the integral; Barrow's rule
> **Source:** Notes.pdf, Eq. 1.62; Problems.pdf, p. 22
>
> The substitution $u$ equal to $\omega\tau$ has the differential $\omega\,d\tau$, and the limits 0 and $t$ become 0 and $\omega t$.
>
> $$\begin{aligned}
> \psi(t) &= \psi(0) + \int_0^t A\omega\sin\left(\omega\tau\right)d\tau = 0 + A\int_0^{\omega t}\sin u\,du \quad &\text{(rate integrated; $u = \omega\tau$, $du = \omega\,d\tau$)} \\
> &= A\left[-\cos u\right]_0^{\omega t} = A\left(-\cos\omega t + \cos 0\right) = A\left(1 - \cos\omega t\right) \quad &\text{(antiderivative; Barrow's rule)} \\
> \dot\psi &= A\omega\sin\omega t = \Omega(t) \quad &\text{(check: chain rule)}
> \end{aligned}$$
>
> $$\boxed{\psi(t) = A\left(1 - \cos\omega t\right), \qquad 0 \le \psi \le 2A}$$
>
> **Units:** $[A] = [\psi] = [1]$; $[A\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** the plane swings back and forth between the angles 0 and $2A$; it does not spin.

![[attachments/EM-SOL/p34-top-view.svg]]

> [!derivation] Basis of the swinging plane: rotation by psi about j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf j_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf k_0$, the cross product of $\mathbf i_0$ and $\mathbf j_0$, points down the page (fingers from $\mathbf i_0$, to the right, towards $\mathbf j_0$, towards the reader; the thumb goes down the page), so minus $\mathbf k_0$ points up the page. A positive $\psi$ is counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\psi$: hypotenuse 1, adjacent leg $\cos\psi$ along $\mathbf i_0$, opposite leg $\sin\psi$ up the page, along minus $\mathbf k_0$ (the minus sign). $\mathbf k_1$ is $\mathbf k_0$ turned by the same angle: adjacent leg $\cos\psi$ along $\mathbf k_0$, opposite leg $\sin\psi$ along plus $\mathbf i_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 - \sin\psi\,\mathbf k_0, \quad \mathbf j_1 = \mathbf j_0, \quad \mathbf k_1 = \sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\psi\cos\psi - \sin\psi\left(-\sin\psi\right)\right) = 1 \quad &\text{(expansion along the second row, cofactor sign $(-1)^{2+2}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\psi + \sin^2\psi = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\psi\sin\psi + \sin\psi\cos\psi = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\psi & 0 & \sin\psi \cr 0 & 1 & 0 \cr -\sin\psi & 0 & \cos\psi \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\psi] = [1]$
> **Meaning:** the matrix of Eq. 1.19 with the angle $\psi$; the vertical, and with it the weight, is the same in both frames.

![[attachments/EM-SOL/p34-wire-plane.svg]]

> [!derivation] Position vector and polar basis in the plane of the wire
> **Law:** position through the centre of the circle; right triangle; polar basis and its derivatives
> **Source:** Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 3.16; Problems.pdf, p. 22
>
> The plane $Oxy$, fixed in $S_1$, is drawn with $\mathbf i_1$ to the right and $\mathbf j_1$ up, so $\mathbf k_1$ points out of the paper (⊙). From $O$ to $P$ the path goes through $C$, because the distance from $C$ is the constant one. Let $F$ be the foot of the perpendicular from $P$ to the $x$ axis: in the shaded right triangle $CFP$ (right angle at $F$) the hypotenuse is $CP$, of length $R$, the leg adjacent to $\varphi$ is $CF$, of length $R\cos\varphi$, along $\mathbf i_1$, and the opposite leg $FP$, of length $R\sin\varphi$, is along $\mathbf j_1$. The angle is measured from $\mathbf i_1$ counterclockwise towards $\mathbf j_1$: it is already the standard polar angle about $C$.
>
> $$\begin{aligned}
> \mathbf r_1^P &= \overrightarrow{OC} + \overrightarrow{CP} = R\,\mathbf i_1 + R\cos\varphi\,\mathbf i_1 + R\sin\varphi\,\mathbf j_1 = R\left(1 + \cos\varphi\right)\mathbf i_1 + R\sin\varphi\,\mathbf j_1 \quad &\text{(the two legs)} \\
> \mathbf e_r &= \frac{\overrightarrow{CP}}{R} = \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1, \quad \mathbf e_\varphi = \frac{d\mathbf e_r}{d\varphi} = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1 \quad &\text{(Eq. 2.24)} \\
> \frac{d\mathbf e_\varphi}{d\varphi} &= -\cos\varphi\,\mathbf i_1 - \sin\varphi\,\mathbf j_1 = -\mathbf e_r \quad &\text{(derivative of each component)} \\
> \mathbf e_r\times\mathbf e_\varphi &= \cos^2\varphi\,\mathbf i_1\times\mathbf j_1 - \sin^2\varphi\,\mathbf j_1\times\mathbf i_1 = \left(\cos^2\varphi + \sin^2\varphi\right)\mathbf k_1 = \mathbf k_1 \quad &\text{($\mathbf i_1\times\mathbf j_1 = \mathbf k_1$, $\mathbf j_1\times\mathbf i_1 = -\mathbf k_1$)} \\
> x_1^P &= R\left(1 + \cos\varphi\right) \ge 0 \quad &\text{(distance from $P$ to the axis $Oy$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = R\left(1 + \cos\varphi\right)\mathbf i_1 + R\sin\varphi\,\mathbf j_1, \quad \mathbf e_r = \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1, \quad \mathbf e_\varphi = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1}$$
>
> **Units:** $[R(1 + \cos\varphi)] = [R\sin\varphi] = [\mathrm{L}]$
> **Meaning:** at an angle of $\pi$ the particle is at $O$, on the axis; at minus a quarter turn it is at the lowest point of the wire. The abscissa is the lever arm of the centrifugal and Euler forces.

### Kinematics

> [!derivation] Motion of the swinging frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; angular acceleration; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf j_1 = \Omega\,\mathbf j_1 = A\omega\sin\omega t\,\mathbf j_1, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(simple rotation about the fixed vertical; $O$ on the axis)} \\
> \boldsymbol\alpha_{10} &= \left.\frac{d\boldsymbol\omega_{10}}{dt}\right|_0 = \dot\Omega\,\mathbf j_1 = A\omega^2\cos\omega t\,\mathbf j_1 \quad &\text{(Eq. 3.9; $\mathbf j_1$ fixed; chain rule)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf i_1 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf j_1\times\mathbf k_1 = \Omega\,\mathbf i_1 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\psi\,\mathbf i_0 - \sin\psi\,\mathbf k_0\right) &= -\dot\psi\sin\psi\,\mathbf i_0 - \dot\psi\cos\psi\,\mathbf k_0 = -\Omega\,\mathbf k_1 \quad &\text{(check: chain rule on the components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = A\omega\sin\omega t\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = A\omega^2\cos\omega t\,\mathbf j_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf i_1}$$
>
> **Units:** $[A\omega] = [\mathrm{T^{-1}}]$; $[A\omega^2] = [\mathrm{T^{-2}}]$
> **Meaning:** the rate of the plane changes in time, so an Euler term appears; the angular acceleration is parallel to the angular velocity, both along the fixed axis.

#### (a) Relative position, velocity and acceleration

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$, $\mathbf j_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 22
>
> $$\begin{aligned}
> \frac{d}{dt}\cos\varphi &= -\sin\varphi\,\dot\varphi, \quad \frac{d}{dt}\sin\varphi = \cos\varphi\,\dot\varphi \quad &\text{(chain rule)} \\
> \mathbf v_1^P &= -R\sin\varphi\,\dot\varphi\,\mathbf i_1 + R\cos\varphi\,\dot\varphi\,\mathbf j_1 = R\dot\varphi\,\mathbf e_\varphi \quad &\text{(components differentiated; Eq. 3.19)} \\
> \left.\frac{d\mathbf e_\varphi}{dt}\right|_1 &= \frac{d\mathbf e_\varphi}{d\varphi}\,\dot\varphi = -\dot\varphi\,\mathbf e_r \quad &\text{(chain rule)} \\
> \mathbf a_1^P &= \left.\frac{d}{dt}\left(R\dot\varphi\,\mathbf e_\varphi\right)\right|_1 = R\ddot\varphi\,\mathbf e_\varphi + R\dot\varphi\left(-\dot\varphi\,\mathbf e_r\right) \quad &\text{(product rule; Eq. 3.24)} \\
> &= -R\left(\ddot\varphi\sin\varphi + \dot\varphi^2\cos\varphi\right)\mathbf i_1 + R\left(\ddot\varphi\cos\varphi - \dot\varphi^2\sin\varphi\right)\mathbf j_1 \quad &\text{(in $\mathcal B_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = R\left(1 + \cos\varphi\right)\mathbf i_1 + R\sin\varphi\,\mathbf j_1, \quad \mathbf v_1^P = R\dot\varphi\,\mathbf e_\varphi, \quad \mathbf a_1^P = R\ddot\varphi\,\mathbf e_\varphi - R\dot\varphi^2\,\mathbf e_r}$$
>
> **Units:** $[R\dot\varphi] = [\mathrm{L\,T^{-1}}]$; $[R\ddot\varphi] = [R\dot\varphi^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** circular motion about $C$ seen in the plane: tangential acceleration and centripetal acceleration towards $C$.

> [!derivation] Absolute acceleration: Euler, centripetal and Coriolis terms
> **Law:** time derivative in $S_0$ of the position written in the swinging basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position as $x\,\mathbf i_1 + y\,\mathbf j_1$, with $x$ and $y$ the two components of the boxed position; the time derivatives of $x$ and $y$ are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x\,\mathbf i_1 + \dot y\,\mathbf j_1 + x\left(-\Omega\,\mathbf k_1\right) = \mathbf v_1^P - \Omega x\,\mathbf k_1 \quad &\text{(product rule; derivative of $\mathbf i_1$; $\mathbf j_1$ constant)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \dot x\left(-\Omega\,\mathbf k_1\right) \quad &\text{(product rule; the turning of $\mathbf i_1$ inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left(-\Omega x\,\mathbf k_1\right) &= -\dot\Omega x\,\mathbf k_1 - \Omega\dot x\,\mathbf k_1 - \Omega x\,\Omega\,\mathbf i_1 \quad &\text{(product rule on three factors; derivative of $\mathbf k_1$)} \\
> \boldsymbol\alpha_{10}\times\mathbf r_1^P &= \dot\Omega\,\mathbf j_1\times\left(x\,\mathbf i_1 + y\,\mathbf j_1\right) = -\dot\Omega x\,\mathbf k_1 \quad &\text{(the $\dot\Omega$ term: Euler)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\Omega\,\mathbf j_1\times\left(\dot x\,\mathbf i_1 + \dot y\,\mathbf j_1\right) = -2\Omega\dot x\,\mathbf k_1 = 2\Omega R\sin\varphi\,\dot\varphi\,\mathbf k_1 \quad &\text{(the two $\Omega\dot x$ terms: Coriolis; $\dot x = -R\sin\varphi\,\dot\varphi$)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf j_1\times\left(-\Omega x\,\mathbf k_1\right) = -\Omega^2x\,\mathbf i_1 \quad &\text{(the $\mathbf i_1$ term: centripetal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - \dot\Omega R\left(1 + \cos\varphi\right)\mathbf k_1 - \Omega^2R\left(1 + \cos\varphi\right)\mathbf i_1 + 2\Omega R\sin\varphi\,\dot\varphi\,\mathbf k_1}$$
>
> **Units:** $[\dot\Omega R] = [\Omega^2R] = [\Omega R\dot\varphi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the Euler and Coriolis terms are normal to the plane of the wire; the centripetal term points horizontally to the axis.

### Forces and Equations of Motion

![[attachments/EM-SOL/p34-fbd.svg]]

#### (b) Forces acting on P

> [!derivation] Actual and inertia forces on the particle
> **Law:** weight; smooth reaction normal to the tangent; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.16; [Lecture 5, Slide 28]; Problems.pdf, p. 22
>
> $$\begin{aligned}
> \mathbf W &= -mg\,\mathbf j_1 \quad &\text{(weight; $\mathbf j_1$ is the vertical)} \\
> \mathbf N &= N_1\,\mathbf e_r + N_2\,\mathbf k_1 = N_1\cos\varphi\,\mathbf i_1 + N_1\sin\varphi\,\mathbf j_1 + N_2\,\mathbf k_1 \quad &\text{(smooth wire: no component along $\mathbf e_\varphi$)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0 \quad &\text{($O$ fixed)} \\
> \mathbf F_E &= -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = mA\omega^2R\cos\omega t\left(1 + \cos\varphi\right)\mathbf k_1 \quad &\text{(Euler: composition box times $-m$)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\mathbf i_1 \quad &\text{(centrifugal; $\Omega^2 = A^2\omega^2\sin^2\omega t$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = -2mA\omega R\sin\omega t\sin\varphi\,\dot\varphi\,\mathbf k_1 \quad &\text{(Coriolis: composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf W = -mg\,\mathbf j_1, \quad \mathbf N = N_1\,\mathbf e_r + N_2\,\mathbf k_1, \quad \mathbf F_C = mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\mathbf i_1, \cr \mathbf F_E = mA\omega^2R\cos\omega t\left(1 + \cos\varphi\right)\mathbf k_1, \quad \mathbf F_{COR} = -2mA\omega R\sin\omega t\sin\varphi\,\dot\varphi\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[mg] = [mA^2\omega^2R] = [mA\omega^2R] = [mA\omega R\dot\varphi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two actual forces (weight and reaction) and three inertia forces: the centrifugal force lies in the plane and pushes away from the axis; the Euler and Coriolis forces are normal to the plane.

> [!derivation] Projections of Newton's second law on the polar basis
> **Law:** Newton's second law in a non-inertial frame, projected on $\{\mathbf e_r, \mathbf e_\varphi, \mathbf k_1\}$
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.17; [Lecture 5, Slide 28]
>
> The projections of $\mathbf i_1$ on $\mathbf e_r$ and $\mathbf e_\varphi$ are the cosine and minus the sine; those of $\mathbf j_1$ are the sine and the cosine.
>
> $$\begin{aligned}
> \mathbf e_\varphi:\ mR\ddot\varphi &= -mg\cos\varphi - mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\sin\varphi \quad &\text{(weight and centrifugal; the reaction and the $\mathbf k_1$ forces drop out)} \\
> \mathbf e_r:\ -mR\dot\varphi^2 &= N_1 - mg\sin\varphi + mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\cos\varphi \quad &\text{(radial)} \\
> \mathbf k_1:\ 0 &= N_2 + mA\omega^2R\cos\omega t\left(1 + \cos\varphi\right) - 2mA\omega R\sin\omega t\sin\varphi\,\dot\varphi \quad &\text{(normal to the plane)}
> \end{aligned}$$
>
> $$\boxed{\text{three scalar equations for the three unknowns } \varphi,\ N_1,\ N_2}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** only the tangential equation is free of the reaction; it is the equation of motion of part (d). The other two give the reaction of part (e).

#### (d) Equation of motion

> [!derivation] Single second-order equation for phi
> **Law:** tangential component of Newton's second law in $S_1$
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 22
>
> $$\begin{aligned}
> mR\ddot\varphi + mg\cos\varphi + mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\sin\varphi &= 0 \quad &\text{(tangential equation, all terms on the left)} \\
> \ddot\varphi + \frac{g}{R}\cos\varphi + A^2\omega^2\sin^2\omega t\left(1 + \cos\varphi\right)\sin\varphi &= 0 \quad &\text{(divided by $mR$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\varphi + \frac{g}{R}\cos\varphi + A^2\omega^2\left(1 + \cos\varphi\right)\sin^2\left(\omega t\right)\sin\varphi = 0}$$
>
> **Units:** $[\ddot\varphi] = [g/R] = [A^2\omega^2] = [\mathrm{T^{-2}}]$
> **Meaning:** a nonlinear pendulum about the lowest point whose coefficient changes periodically in time: the swing of the plane enters only through the centrifugal force.

#### (e) Reaction of the wire

> [!derivation] Components of the reaction
> **Law:** radial and normal components of Newton's second law in $S_1$
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19; Problems.pdf, p. 22
>
> $$\begin{aligned}
> N_1 &= mg\sin\varphi - mA^2\omega^2R\sin^2\omega t\left(1 + \cos\varphi\right)\cos\varphi - mR\dot\varphi^2 \quad &\text{(radial equation solved for $N_1$; Eq. 6.18)} \\
> N_2 &= 2mA\omega R\sin\omega t\sin\varphi\,\dot\varphi - mA\omega^2R\cos\omega t\left(1 + \cos\varphi\right) \quad &\text{(normal equation solved for $N_2$; Eq. 6.19)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf N = N_1\cos\varphi\,\mathbf i_1 + N_1\sin\varphi\,\mathbf j_1 + N_2\,\mathbf k_1, \cr N_1 = mg\sin\varphi - mA^2R\omega^2\left(1 + \cos\varphi\right)\sin^2\left(\omega t\right)\cos\varphi - mR\dot\varphi^2, \cr N_2 = 2mAR\omega\,\dot\varphi\sin\varphi\sin\left(\omega t\right) - mAR\omega^2\left(1 + \cos\varphi\right)\cos\left(\omega t\right) \end{gathered}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the normal component is the push the wire must give to carry the particle with the swinging plane: it balances the Euler and Coriolis forces. It depends on time even at rest in the plane, through the Euler term.

### Answers and Checks

#### (c) Is the mechanical energy conserved in Oxy?

> [!derivation] Power of each force in the swinging frame
> **Law:** power of each force on the relative velocity; potential of the centrifugal force; time derivative of the energy along the motion
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> The reaction, the Euler force and the Coriolis force do no work in $S_1$ (the wire is at rest there; the last two are normal to the plane that holds the relative velocity). The weight has the potential $mgR\sin\varphi$. The centrifugal force has, at each instant, the potential minus one half of $m\Omega^2$ times the squared distance to the axis, but this potential depends explicitly on time because $\Omega$ does. Write $E_1^P$ for the kinetic energy in $S_1$ plus these two potentials.
>
> $$\begin{aligned}
> \left(\mathbf N + \mathbf F_E + \mathbf F_{COR}\right)\cdot\mathbf v_1^P &= \left(N_1\,\mathbf e_r + \left(N_2 + F_{E} + F_{COR}\right)\mathbf k_1\right)\cdot R\dot\varphi\,\mathbf e_\varphi = 0 \quad &\text{(no power)} \\
> E_1^P &= \tfrac12 mR^2\dot\varphi^2 + mgR\sin\varphi - \tfrac12 m\Omega^2R^2\left(1 + \cos\varphi\right)^2 \quad &\text{(kinetic plus the two potentials)} \\
> \frac{dE_1^P}{dt} &= mR^2\dot\varphi\ddot\varphi + mgR\cos\varphi\,\dot\varphi + m\Omega^2R^2\left(1 + \cos\varphi\right)\sin\varphi\,\dot\varphi - m\Omega\dot\Omega R^2\left(1 + \cos\varphi\right)^2 \quad &\text{(product rule; chain rule on each factor)} \\
> &= mR^2\dot\varphi\left[\ddot\varphi + \frac{g}{R}\cos\varphi + \Omega^2\left(1 + \cos\varphi\right)\sin\varphi\right] - m\Omega\dot\Omega R^2\left(1 + \cos\varphi\right)^2 \quad &\text{(first three terms grouped)} \\
> &= -m\Omega\dot\Omega R^2\left(1 + \cos\varphi\right)^2 = -mA^2\omega^3R^2\sin\omega t\cos\omega t\left(1 + \cos\varphi\right)^2 \quad &\text{(bracket zero by part (d); $\Omega\dot\Omega$ substituted)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_1^P}{dt} = -mA^2\omega^3R^2\sin\left(\omega t\right)\cos\left(\omega t\right)\left(1 + \cos\varphi\right)^2 \ne 0: \ \text{not conserved}}$$
>
> **Units:** $[mA^2\omega^3R^2] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** no. The rate of the plane is not constant, so the centrifugal force has no potential independent of time, and the energy changes at the rate of the explicit time derivative of that potential. With a constant rate the energy would be conserved: the Euler force would vanish and the Coriolis force does no work. The energy in $S_0$ is not conserved either: there the wire moves and its normal reaction works.

#### (f) Small oscillations about the lowest point

> [!derivation] Linearised equation about the lowest point
> **Law:** Taylor expansion to first order about the equilibrium; neglect of the small parametric term
> **Source:** Notes.pdf, Eq. 4.46; Notes.pdf, Eq. 5.32; Problems.pdf, p. 22
>
> With $\varphi$ equal to $\delta$ minus a quarter turn, the difference formulas give the cosine and the sine of $\varphi$; then the first-order Taylor expansions in $\delta$ are kept. The hypothesis on $A$ makes the product of $A^2\omega^2$ and $\delta$ small against $g/R$ times $\delta$.
>
> $$\begin{aligned}
> \cos\varphi &= \cos\delta\cos\tfrac{\pi}{2} + \sin\delta\sin\tfrac{\pi}{2} = \sin\delta \simeq \delta \quad &\text{(difference formula; Taylor)} \\
> \sin\varphi &= \sin\delta\cos\tfrac{\pi}{2} - \cos\delta\sin\tfrac{\pi}{2} = -\cos\delta \simeq -1 \quad &\text{(difference formula; Taylor, error of order $\delta^2$)} \\
> \ddot\varphi &= \ddot\delta \quad &\text{(the quarter turn is constant)} \\
> \ddot\delta + \frac{g}{R}\delta - A^2\omega^2\sin^2\omega t\left(1 + \delta\right) &= 0 \quad &\text{(part (d), first order in $\delta$)} \\
> A^2\omega^2\sin^2\omega t\,\delta &\ll \frac{g}{R}\delta \quad &\text{(hypothesis $A^2 \ll g/(R\omega^2)$: term dropped)} \\
> \sin^2\omega t &= \tfrac12\left(1 - \cos 2\omega t\right) \quad &\text{(double-angle identity)}
> \end{aligned}$$
>
> $$\boxed{\ddot\delta + \frac{g}{R}\delta = \frac{A^2\omega^2}{2}\left[1 - \cos\left(2\omega t\right)\right]}$$
>
> **Units:** $[g\delta/R] = [A^2\omega^2] = [\mathrm{T^{-2}}]$
> **Meaning:** a harmonic oscillator of natural frequency the square root of $g/R$, driven by a constant push and a push at twice the frequency of the swing; both come from the mean and the oscillating part of the centrifugal force.

> [!derivation] Solution: mean position and the frequency of breakdown
> **Law:** general solution of the forced undamped oscillator as homogeneous plus particular solution; resonance
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.32; Notes.pdf, Eq. 5.41; Notes.pdf, Sec. 5.4
>
> Write $\omega_n$ for the square root of $g/R$. A particular solution is a constant $\delta_0$ plus a term $D_1\cos 2\omega t$; the second derivative of that term is written before it is substituted.
>
> $$\begin{aligned}
> \omega_n^2\delta_0 &= \frac{A^2\omega^2}{2} \;\Rightarrow\; \delta_0 = \frac{A^2\omega^2}{2\omega_n^2} = \frac{A^2R\omega^2}{2g} \quad &\text{(constant part)} \\
> \frac{d}{dt}\left(D_1\cos 2\omega t\right) &= -2\omega D_1\sin 2\omega t, \quad \frac{d^2}{dt^2}\left(D_1\cos 2\omega t\right) = -4\omega^2D_1\cos 2\omega t \quad &\text{(chain rule, twice)} \\
> \left(\omega_n^2 - 4\omega^2\right)D_1 &= -\frac{A^2\omega^2}{2} \;\Rightarrow\; D_1 = -\frac{A^2\omega^2}{2\left(\omega_n^2 - 4\omega^2\right)} \quad &\text{(oscillating part, $2\omega \ne \omega_n$)} \\
> \delta(t) &= \delta_0 + D_1\cos 2\omega t + a\cos\omega_nt + b\sin\omega_nt \quad &\text{(Eq. 5.7 for the homogeneous part; $a$, $b$ from the initial conditions)} \\
> 2\omega = \omega_n:\quad \delta_p &= K\,t\sin\omega_nt, \quad \ddot\delta_p = 2K\omega_n\cos\omega_nt - K\omega_n^2t\sin\omega_nt \quad &\text{(trial at exact resonance; product rule)} \\
> \ddot\delta_p + \omega_n^2\delta_p &= 2K\omega_n\cos\omega_nt = -\frac{A^2\omega^2}{2}\cos\omega_nt \;\Rightarrow\; K = -\frac{A^2\omega^2}{4\omega_n} \quad &\text{(amplitude growing linearly in time)}
> \end{aligned}$$
>
> $$\boxed{\delta \text{ oscillates about } \delta_0 = \frac{A^2R\omega^2}{2g} \text{ with } \omega_n = \sqrt{\frac{g}{R}}; \qquad \delta \ll 1 \text{ fails near } 2\omega = \sqrt{\frac{g}{R}}}$$
>
> **Units:** $[\delta_0] = [A^2R\omega^2/g] = [1]$; $[\omega_n] = [\mathrm{T^{-1}}]$
> **Meaning:** the mean position is shifted outward, away from the axis, by the mean centrifugal force, and the shift is small precisely because of the hypothesis on $A$. When twice the swing frequency approaches the natural frequency the forced amplitude grows without bound (no damping), so the small-angle hypothesis breaks down.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Position, velocity, acceleration | $\mathbf r_1^P = R(1 + \cos\varphi)\,\mathbf i_1 + R\sin\varphi\,\mathbf j_1$, $\mathbf v_1^P = R\dot\varphi\,\mathbf e_\varphi$, $\mathbf a_1^P = R\ddot\varphi\,\mathbf e_\varphi - R\dot\varphi^2\,\mathbf e_r$, with $\mathbf e_r = \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1$, $\mathbf e_\varphi = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1$ |
| (b) Forces | weight $-mg\,\mathbf j_1$; reaction $N_1\mathbf e_r + N_2\mathbf k_1$; $\mathbf F_A = \mathbf 0$; Euler $mA\omega^2R\cos\omega t(1 + \cos\varphi)\,\mathbf k_1$; centrifugal $mA^2\omega^2R\sin^2\omega t(1 + \cos\varphi)\,\mathbf i_1$; Coriolis $-2mA\omega R\sin\omega t\sin\varphi\,\dot\varphi\,\mathbf k_1$ |
| (c) Energy in $Oxy$ | not conserved: the centrifugal potential depends explicitly on time; $dE_1^P/dt = -mA^2\omega^3R^2\sin\omega t\cos\omega t(1 + \cos\varphi)^2$ |
| (d) Equation of motion | $\ddot\varphi + (g/R)\cos\varphi + A^2\omega^2(1 + \cos\varphi)\sin^2(\omega t)\sin\varphi = 0$ |
| (e) Reaction | $\mathbf N = N_1\cos\varphi\,\mathbf i_1 + N_1\sin\varphi\,\mathbf j_1 + N_2\mathbf k_1$, $N_1 = mg\sin\varphi - mA^2R\omega^2(1 + \cos\varphi)\sin^2(\omega t)\cos\varphi - mR\dot\varphi^2$, $N_2 = 2mAR\omega\dot\varphi\sin\varphi\sin(\omega t) - mAR\omega^2(1 + \cos\varphi)\cos(\omega t)$ |
| (f) Oscillation | $\ddot\delta + (g/R)\delta = \frac{A^2\omega^2}{2}[1 - \cos 2\omega t]$; oscillation about $\delta_0 = A^2R\omega^2/(2g)$ with $\omega_n = \sqrt{g/R}$; the approximation fails near $\omega = \frac12\sqrt{g/R}$ (resonance) |

**Check against the official key:** Problems.pdf, p. 75 prints the equation of motion, the reaction with the components $N_1$ and $N_2$, the linearised equation, the centre of oscillation, the natural frequency and the resonance condition. All coincide with parts (d), (e) and (f), term by term (box below).

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison
> **Source:** Problems.pdf, p. 75
>
> $$\begin{aligned}
> \text{key: } \ddot\varphi + \frac{g\cos\varphi}{R} + A^2\omega^2\left(1 + \cos\varphi\right)\sin^2\left(\omega t\right)\sin\varphi &= 0 \quad &\text{(part (d))} \\
> \text{key: } \mathbf N = N_1\cos\varphi\,\mathbf i + N_1\sin\varphi\,\mathbf j + N_2\,\mathbf k&, \text{ with the same } N_1,\ N_2 \quad &\text{(part (e); the key's $\mathbf i, \mathbf j, \mathbf k$ are $\mathcal B_1$)} \\
> \text{key: } \ddot\delta + \frac{g}{R}\delta = \frac{A^2\omega^2}{2}\left[1 - \cos\left(2\omega t\right)\right]&, \quad \delta_0 = \frac{A^2R\omega^2}{2g}, \quad \omega_n = \sqrt{\frac{g}{R}}, \quad 2\omega \simeq \omega_n \quad &\text{(part (f))}
> \end{aligned}$$
>
> $$\boxed{\text{equation of motion, reaction and small oscillations coincide with the key}}$$
>
> **Units:** as in parts (d) to (f)
> **Meaning:** no discrepancy.

> [!derivation] Independent check: angular momentum about the vertical axis
> **Law:** angular momentum about the fixed point $O$ and its rate, equal to the moment of the actual forces
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> In $\mathcal B_1$ the position has the components $(x, y, 0)$ and the absolute velocity $(\dot x, \dot y, -\Omega x)$ (composition box). The component along $\mathbf j_1$ of a vector product is the third component of the first factor times the first of the second minus the first of the first times the third of the second. The weight and the in-plane reaction lie in the plane, which contains the axis: no axial moment.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf j_1 &= m\left(0\cdot\dot x - x\left(-\Omega x\right)\right) = m\Omega x^2 \quad &\text{(Eq. 4.48)} \\
> \mathbf M_O\cdot\mathbf j_1 &= 0\cdot N_x - x\,N_2 = -xN_2 \quad &\text{(only $N_2\,\mathbf k_1$ at the lever arm $x$)} \\
> m\dot\Omega x^2 + 2m\Omega x\dot x &= -xN_2 \quad &\text{(Eq. 4.53; product rule and chain rule)} \\
> N_2 &= -m\dot\Omega x - 2m\Omega\dot x = -mA\omega^2\cos\omega t\,R\left(1 + \cos\varphi\right) + 2mA\omega\sin\omega t\,R\sin\varphi\,\dot\varphi \quad &\text{(divided by $-x$; $\dot x = -R\sin\varphi\,\dot\varphi$)}
> \end{aligned}$$
>
> $$\boxed{N_2 = 2mAR\omega\,\dot\varphi\sin\varphi\sin\omega t - mAR\omega^2\left(1 + \cos\varphi\right)\cos\omega t \quad (x \ne 0)}$$
>
> **Units:** $[xN_2] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the same normal reaction as part (e), found without inertia forces.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> A \to 0:\quad \ddot\varphi + \frac{g}{R}\cos\varphi &= 0, \quad N_2 = 0 \quad &\text{(pendulum in a fixed plane, about the lowest point)} \\
> A \to 0:\quad \delta_0 &\to 0 \quad &\text{(no outward shift without swing)} \\
> \omega \to 0,\ A \text{ fixed}:\quad \Omega &\to 0, \quad \dot\Omega \to 0 \quad &\text{(the same pendulum)}
> \end{aligned}$$
>
> $$\boxed{A \to 0 \text{ or } \omega \to 0: \text{ simple pendulum in a fixed vertical plane, } N_2 \to 0}$$
>
> **Units:** dimensionless
> **Meaning:** without the swing of the plane the inertia forces vanish and the particle is a pendulum on a fixed circle.

---

## Problem 36: Pendulum String Dragged by a Rotating Bar

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ hangs at rest from the ceiling point $A$ by a string of length $L$. A bar turning at the constant rate $\omega$ about the vertical through its centre $O$, in a horizontal plane a distance $h$ below the ceiling, hits the string at the start and drags it; the string slides on the bar without friction, over the contact point $C$ (Problems.pdf, p. 24). The statement asks for the position and velocity of $A$ in the bar frame $S_1$, the position, velocity and acceleration of $P$ there, the length $AC$, $\ell$ and $\varphi$ in terms of $\xi$ and time, the forces on $P$, the equations of motion, their initial conditions, whether the energy is conserved, and the condition of separation. The bar is at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ the centre of the bar (fixed), $\mathbf k_0$ vertical, up, $\mathbf i_0$ horizontal from $O$ towards the point $A'$ of the plane of the bar directly below $A$ |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, attached to the bar: $\mathbf i_1$ along the bar, $\mathbf k_1 = \mathbf k_0$, $\mathbf j_1 = \mathbf k_1\times\mathbf i_1$; at $t = 0$ the bar lies along $\mathbf i_0$ (it hits the string at that instant), so $S_1$ coincides with $S_0$ then |
| Sense of rotation | read from the left drawing: before the impact $A'$ lies at positive $x_1$ and positive $y_1$, so the bar turns from $\mathbf i_1$ towards $\mathbf j_1$: angular velocity $+\omega\,\mathbf k_1$ (the Coriolis force of the key implies the same sign) |
| String basis | $\mathcal B_2 = \{\mathbf e_{CP}, \mathbf e_\theta, \mathbf e_\varphi\}$, with $\mathbf e_{CP}$ from $C$ to $P$ (deduced below) |
| Coordinates | $\xi$ (distance $OC$ along the bar), $\ell$ (length $CP$), $\theta$ (angle between the vertical plane $Ox_1z_1$ and the plane bar–$P$, from the downward vertical; positive towards negative $y_1$, the sign of the key), $\varphi$ (angle between $\overrightarrow{CP}$ and the bar, in $(0, \pi)$) |
| Constraints | constant string length, $AC + \ell = L$; frictionless contact (equal angles of the two segments with the bar, part (c)); string tense and in contact with the bar (the stage studied) |
| Degrees of freedom | the particle moves in space with one constraint (the string), so 3 minus 1: 2, taken as $\xi(t)$ and $\theta(t)$; $\ell$ and $\varphi$ are functions of $\xi$ and $t$ (part (c)) |
| Data | $m$ [kg], $L$ [m], $h$ [m], $R$ [m] (horizontal distance $OA$), $\omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$] |
| Auxiliary symbol | $D$, the length $AC$ [m] |
| Unknowns | $\xi(t)$, $\theta(t)$ and the tension $T(t) \gt 0$ |
| Applied forces | weight $-mg\,\mathbf k_1$; string pull $-T\,\mathbf e_{CP}$ (the bar touches the string, not $P$) |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms ($O$ fixed, $\omega$ constant) (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; massless inextensible string; thin bar, long enough for $C$ to stay on it; no friction at $C$; $\omega$ imposed whatever the string does; $L \gt h$ |
| Readings | (1) "Separates" (part (h)) is read as the string straightening, so that the bar no longer bends it; the other way to lose contact, $C$ sliding off the end of the bar, is the condition that $\xi$ reaches the half-length of the bar, not a relation between $\theta$ and time. (2) No impulse at the impact: the string is perpendicular to the bar there, so its path length changes only to second order (part (f)) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p36-top-view.svg]]

> [!derivation] Basis of the bar: rotation by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page (thumb towards the reader, the fingers turn $\mathbf i_0$ counterclockwise by a quarter turn). The bar turns counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\omega t\cos\omega t - \left(-\sin\omega t\right)\sin\omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** the matrix of Eq. 1.20 with the angle $\omega t$; the vertical is common to both frames.

![[attachments/EM-SOL/p36-anchor-top.svg]]

> [!derivation] Position of the anchor A in S1
> **Law:** right triangle in the plane of the bar; components through the transposed matrix
> **Source:** Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.14; Problems.pdf, p. 24
>
> In the same view, $A'$ is at the distance $R$ from $O$ along $\mathbf i_0$, that is, the angle $\omega t$ behind the bar (clockwise from $\mathbf i_1$). Let $F$ be the foot of the perpendicular from $A'$ to the line of the bar: in the right triangle $OFA'$ (right angle at $F$) the hypotenuse is $OA'$, of length $R$; the leg adjacent to $\omega t$, $OF$, has length $R\cos\omega t$ along plus $\mathbf i_1$; the opposite leg $FA'$ has length $R\sin\omega t$ along minus $\mathbf j_1$, because $A'$ lies on the clockwise side of the bar. $A$ is a height $h$ above $A'$.
>
> $$\begin{aligned}
> \mathbf r_1^A &= \overrightarrow{OF} + \overrightarrow{FA'} + \overrightarrow{A'A} = R\cos\omega t\,\mathbf i_1 - R\sin\omega t\,\mathbf j_1 + h\,\mathbf k_1 \quad &\text{(the legs, with their directions)} \\
> [{}_0R_1]^T\begin{pmatrix} R \cr 0 \cr h \end{pmatrix} &= \begin{pmatrix} \cos\omega t\cdot R + \sin\omega t\cdot 0 + 0\cdot h \cr -\sin\omega t\cdot R + \cos\omega t\cdot 0 + 0\cdot h \cr 0 + 0 + 1\cdot h \end{pmatrix} = \begin{pmatrix} R\cos\omega t \cr -R\sin\omega t \cr h \end{pmatrix} \quad &\text{(check: Eq. 1.14, rows of the transpose times $\mathbf r_0^A$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^A = R\cos\omega t\,\mathbf i_1 - R\sin\omega t\,\mathbf j_1 + h\,\mathbf k_1}$$
>
> **Units:** $[R\cos\omega t] = [h] = [\mathrm{L}]$
> **Meaning:** seen from the bar, the anchor turns backwards on a circle of radius $R$ at the height $h$.

![[attachments/EM-SOL/p36-bar-view.svg]]

> [!derivation] Plane bar–P: rotation by theta about the bar
> **Law:** right triangle in the view along the bar; derivative of a unit vector with respect to its angle; relation with the standard azimuth
> **Source:** Notes.pdf, Eq. 1.18; Notes.pdf, Eq. 2.24; Problems.pdf, p. 24
>
> View along the bar, with $\mathbf i_1$ out of the paper (⊙) at $C$ and $\mathbf k_1$ up; then $\mathbf j_1$, the cross product of $\mathbf k_1$ and $\mathbf i_1$, points to the right (fingers from $\mathbf k_1$, up, towards $\mathbf i_1$, towards the reader; the thumb points right). The plane bar–$P$ contains the line of sight, so it is seen as a line through $C$, at the angle $\theta$ from the downward vertical, towards the left (negative $y_1$) for positive $\theta$. Its unit vector $\mathbf u$, from $C$ towards the side of $P$, is the hypotenuse of the shaded right triangle: adjacent leg $\cos\theta$ along minus $\mathbf k_1$, opposite leg $\sin\theta$ along minus $\mathbf j_1$ (both minus signs: down and to the left). The standard azimuth $\chi$ about $\mathbf i_1$ is measured from $\mathbf j_1$ towards $\mathbf k_1$; $\theta$ is measured from minus $\mathbf k_1$ in the opposite sense, so $\chi$ is minus the sum of $\theta$ and a quarter turn.
>
> $$\begin{aligned}
> \mathbf u &= -\sin\theta\,\mathbf j_1 - \cos\theta\,\mathbf k_1 \quad &\text{(the two legs)} \\
> \mathbf e_\theta &= \frac{d\mathbf u}{d\theta} = -\cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1, \quad \mathbf u\cdot\mathbf e_\theta = \sin\theta\cos\theta - \cos\theta\sin\theta = 0 \quad &\text{(derivative of each component; orthogonal, unit)} \\
> \cos\chi &= \cos\left(\theta + \tfrac{\pi}{2}\right) = \cos\theta\cos\tfrac{\pi}{2} - \sin\theta\sin\tfrac{\pi}{2} = -\sin\theta \quad &\text{($\chi = -\theta - \pi/2$; cosine even)} \\
> \sin\chi &= -\sin\left(\theta + \tfrac{\pi}{2}\right) = -\left(\sin\theta\cos\tfrac{\pi}{2} + \cos\theta\sin\tfrac{\pi}{2}\right) = -\cos\theta \quad &\text{(sine odd)}
> \end{aligned}$$
>
> $$\boxed{\mathbf u = -\sin\theta\,\mathbf j_1 - \cos\theta\,\mathbf k_1 = \cos\chi\,\mathbf j_1 + \sin\chi\,\mathbf k_1, \qquad \mathbf e_\theta = -\cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1}$$
>
> **Units:** dimensionless
> **Meaning:** at zero $\theta$ the plane bar–$P$ is the vertical plane $Ox_1z_1$ and $\mathbf u$ points straight down: the hanging position.

![[attachments/EM-SOL/p36-string-plane.svg]]

> [!derivation] String basis and position of P
> **Law:** right triangle in the true view of the plane bar–$P$; partial derivatives of a unit vector; vector product; position through the contact point
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 3.16; Problems.pdf, p. 24
>
> True view of the plane bar–$P$: the bar to the right, $\mathbf u$ down the page. Let $E$ be the foot of the perpendicular from $P$ to the bar: in the shaded right triangle $CEP$ (right angle at $E$) the hypotenuse is $CP$, of length $\ell$, the leg adjacent to $\varphi$ is $CE$, of length $\ell\cos\varphi$, along $\mathbf i_1$, and the opposite leg $EP$, of length $\ell\sin\varphi$, is along $\mathbf u$. The determinant is expanded along its first row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf e_{CP} &= \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf u = \cos\varphi\,\mathbf i_1 - \sin\varphi\sin\theta\,\mathbf j_1 - \sin\varphi\cos\theta\,\mathbf k_1 \quad &\text{(the two legs over $\ell$)} \\
> \mathbf e_\varphi &= \frac{\partial\mathbf e_{CP}}{\partial\varphi} = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf u = -\sin\varphi\,\mathbf i_1 - \cos\varphi\sin\theta\,\mathbf j_1 - \cos\varphi\cos\theta\,\mathbf k_1 \quad &\text{(derivative in $\varphi$)} \\
> \frac{\partial\mathbf e_{CP}}{\partial\theta} &= \sin\varphi\,\frac{d\mathbf u}{d\theta} = \sin\varphi\,\mathbf e_\theta \quad &\text{(only $\mathbf u$ depends on $\theta$)} \\
> \det[{}_1R_2] &= (+1)\cos\varphi\left(\cos\varphi\cos^2\theta + \cos\varphi\sin^2\theta\right) - 0 + (+1)\left(-\sin\varphi\right)\left(-\sin\varphi\sin^2\theta - \sin\varphi\cos^2\theta\right) = 1 \quad &\text{(columns $\mathbf e_{CP}, \mathbf e_\theta, \mathbf e_\varphi$; first row)} \\
> \mathbf e_{CP}\cdot\mathbf e_\varphi &= -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi\left(\sin^2\theta + \cos^2\theta\right) = 0, \quad \mathbf e_{CP}\cdot\mathbf e_\theta = \sin\varphi\sin\theta\cos\theta - \sin\varphi\cos\theta\sin\theta = 0 \quad &\text{(orthogonal)} \\
> \mathbf r_1^P &= \overrightarrow{OC} + \overrightarrow{CP} = \xi\,\mathbf i_1 + \ell\,\mathbf e_{CP} \quad &\text{(through the contact point)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} [{}_1R_2] = \begin{pmatrix} \cos\varphi & 0 & -\sin\varphi \cr -\sin\varphi\sin\theta & -\cos\theta & -\cos\varphi\sin\theta \cr -\sin\varphi\cos\theta & \sin\theta & -\cos\varphi\cos\theta \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad \mathbf e_{CP}\times\mathbf e_\theta = \mathbf e_\varphi \cr \mathbf r_1^P = \left(\xi + \ell\cos\varphi\right)\mathbf i_1 - \ell\sin\varphi\sin\theta\,\mathbf j_1 - \ell\sin\varphi\cos\theta\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[\xi] = [\ell] = [\mathrm{L}]$; the unit vectors are dimensionless
> **Meaning:** $C$ plays the role of a moving centre of spherical coordinates: $\ell$ is the radius, $\varphi$ the angle from the bar and $\theta$ the azimuth about the bar.

> [!derivation] Derivatives of the string basis in S1
> **Law:** chain rule on unit vectors that depend on two angles; $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ constant in $S_1$
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.7
>
> $$\begin{aligned}
> \frac{\partial\mathbf e_\varphi}{\partial\varphi} &= -\cos\varphi\,\mathbf i_1 - \sin\varphi\,\mathbf u = -\mathbf e_{CP}, \quad \frac{\partial\mathbf e_\varphi}{\partial\theta} = \cos\varphi\,\mathbf e_\theta \quad &\text{(component by component)} \\
> \frac{d\mathbf e_\theta}{d\theta} &= \sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 = -\mathbf u = -\left(\sin\varphi\,\mathbf e_{CP} + \cos\varphi\,\mathbf e_\varphi\right) \quad &\text{($\sin\varphi\,\mathbf e_{CP} + \cos\varphi\,\mathbf e_\varphi = \mathbf u$)} \\
> \left.\frac{d\mathbf e_{CP}}{dt}\right|_1 &= \frac{\partial\mathbf e_{CP}}{\partial\varphi}\dot\varphi + \frac{\partial\mathbf e_{CP}}{\partial\theta}\dot\theta = \dot\varphi\,\mathbf e_\varphi + \dot\theta\sin\varphi\,\mathbf e_\theta \quad &\text{(chain rule)} \\
> \left.\frac{d\mathbf e_\varphi}{dt}\right|_1 &= -\dot\varphi\,\mathbf e_{CP} + \dot\theta\cos\varphi\,\mathbf e_\theta, \quad \left.\frac{d\mathbf e_\theta}{dt}\right|_1 = -\dot\theta\left(\sin\varphi\,\mathbf e_{CP} + \cos\varphi\,\mathbf e_\varphi\right) \quad &\text{(chain rule)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_{CP} = \dot\varphi\,\mathbf e_\varphi + \dot\theta\sin\varphi\,\mathbf e_\theta, \quad \dot{\mathbf e}_\varphi = -\dot\varphi\,\mathbf e_{CP} + \dot\theta\cos\varphi\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = -\dot\theta\left(\sin\varphi\,\mathbf e_{CP} + \cos\varphi\,\mathbf e_\varphi\right) \quad (\text{in } S_1)}$$
>
> **Units:** $[\dot\varphi] = [\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** the string basis turns with the rates of the two angles, as a spherical basis does.

### Kinematics

> [!derivation] Motion of the bar frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed vertical through $O$; $\omega$ constant)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) &= -\omega\sin\omega t\,\mathbf i_0 + \omega\cos\omega t\,\mathbf j_0 = \omega\,\mathbf j_1 \quad &\text{(check: chain rule)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** in $S_1$ the bar is a fixed line; in $S_0$ its basis turns at the constant rate.

#### (a) Position and velocity of A in S1

> [!derivation] Velocity of the anchor seen from the bar
> **Law:** time derivative in $S_1$; check with the composition of velocities for a point fixed in $S_0$
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.26; Problems.pdf, p. 24
>
> $$\begin{aligned}
> \mathbf v_1^A &= \left.\frac{d\mathbf r_1^A}{dt}\right|_1 = -R\omega\sin\omega t\,\mathbf i_1 - R\omega\cos\omega t\,\mathbf j_1 \quad &\text{(chain rule on $\cos\omega t$ and $\sin\omega t$; $h$ constant)} \\
> \boldsymbol\omega_{10}\times\mathbf r_1^A &= \omega\,\mathbf k_1\times\left(R\cos\omega t\,\mathbf i_1 - R\sin\omega t\,\mathbf j_1 + h\,\mathbf k_1\right) = R\omega\cos\omega t\,\mathbf j_1 + R\omega\sin\omega t\,\mathbf i_1 \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \mathbf v_0^A &= \mathbf v_0^O + \mathbf v_1^A + \boldsymbol\omega_{10}\times\mathbf r_1^A = \mathbf 0 \quad &\text{(Eq. 3.26: $A$ is fixed in $S_0$, as it must be)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^A = R\cos\omega t\,\mathbf i_1 - R\sin\omega t\,\mathbf j_1 + h\,\mathbf k_1, \qquad \mathbf v_1^A = -R\omega\sin\omega t\,\mathbf i_1 - R\omega\cos\omega t\,\mathbf j_1}$$
>
> **Units:** $[R\omega] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** in $S_1$ the anchor goes round its circle with the angular velocity minus $\omega$ about the vertical: the end of the string moves in the frame of the bar.

#### (b) Position, velocity and acceleration of P in S1

> [!derivation] Relative velocity and relative acceleration of P
> **Law:** time derivatives in $S_1$; product rule; derivatives of the string basis
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 24
>
> $$\begin{aligned}
> \mathbf v_1^P &= \dot\xi\,\mathbf i_1 + \dot\ell\,\mathbf e_{CP} + \ell\left(\dot\varphi\,\mathbf e_\varphi + \dot\theta\sin\varphi\,\mathbf e_\theta\right) \quad &\text{(product rule on $\ell\,\mathbf e_{CP}$)} \\
> \frac{d}{dt}\left(\dot\ell\,\mathbf e_{CP}\right) &= \ddot\ell\,\mathbf e_{CP} + \dot\ell\dot\varphi\,\mathbf e_\varphi + \dot\ell\dot\theta\sin\varphi\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \frac{d}{dt}\left(\ell\dot\varphi\,\mathbf e_\varphi\right) &= \left(\dot\ell\dot\varphi + \ell\ddot\varphi\right)\mathbf e_\varphi - \ell\dot\varphi^2\,\mathbf e_{CP} + \ell\dot\varphi\dot\theta\cos\varphi\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \frac{d}{dt}\left(\ell\dot\theta\sin\varphi\,\mathbf e_\theta\right) &= \left(\dot\ell\dot\theta\sin\varphi + \ell\ddot\theta\sin\varphi + \ell\dot\theta\dot\varphi\cos\varphi\right)\mathbf e_\theta - \ell\dot\theta^2\sin\varphi\left(\sin\varphi\,\mathbf e_{CP} + \cos\varphi\,\mathbf e_\varphi\right) \quad &\text{(product rule on three factors)} \\
> \mathbf a_1^P &= \ddot\xi\,\mathbf i_1 + \text{the three lines above, collected along } \mathbf e_{CP},\ \mathbf e_\varphi,\ \mathbf e_\theta \quad &\text{(sum)} \\
> v_x &= \dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi \quad &\text{(derivative of the first component of $\mathbf r_1^P$; product and chain rules)} \\
> v_y &= -\left(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta\right) \quad &\text{(second component)} \\
> v_z &= -\left(\dot\ell\sin\varphi\cos\theta + \ell\dot\varphi\cos\varphi\cos\theta - \ell\dot\theta\sin\varphi\sin\theta\right) \quad &\text{(third component)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = \xi\,\mathbf i_1 + \ell\,\mathbf e_{CP}, \qquad \mathbf v_1^P = \dot\xi\,\mathbf i_1 + \dot\ell\,\mathbf e_{CP} + \ell\dot\varphi\,\mathbf e_\varphi + \ell\dot\theta\sin\varphi\,\mathbf e_\theta, \cr \mathbf a_1^P = \ddot\xi\,\mathbf i_1 + \left(\ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi\right)\mathbf e_{CP} + \left(\ell\ddot\varphi + 2\dot\ell\dot\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi\right)\mathbf e_\varphi + \left(\ell\ddot\theta\sin\varphi + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi\right)\mathbf e_\theta \end{gathered}}$$
>
> **Units:** $[\dot\xi] = [\ell\dot\varphi] = [\mathrm{L\,T^{-1}}]$; $[\ddot\xi] = [\ell\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the acceleration along the bar of the moving centre $C$ plus the spherical acceleration about it; the components of the velocity in $\mathcal B_1$ are listed in the last three rows.

> [!derivation] Absolute acceleration of P: centripetal and Coriolis terms
> **Law:** time derivative in $S_0$ of a vector written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position in $\mathcal B_1$ as $x\,\mathbf i_1 + y\,\mathbf j_1 + z\,\mathbf k_1$, with the components of the boxed position; their time derivatives are $v_x$, $v_y$, $v_z$.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x\,\mathbf i_1 + \dot y\,\mathbf j_1 + \dot z\,\mathbf k_1 + x\,\omega\,\mathbf j_1 - y\,\omega\,\mathbf i_1 = \mathbf v_1^P + \omega\left(x\,\mathbf j_1 - y\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \omega\left(v_x\,\mathbf j_1 - v_y\,\mathbf i_1\right) \quad &\text{(product rule; the turning of $\mathbf i_1$, $\mathbf j_1$ inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left[\omega\left(x\,\mathbf j_1 - y\,\mathbf i_1\right)\right] &= \omega\left(v_x\,\mathbf j_1 - v_y\,\mathbf i_1\right) + \omega^2\left(-x\,\mathbf i_1 - y\,\mathbf j_1\right) \quad &\text{(product rule; derivatives of $\mathbf j_1$, $\mathbf i_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\omega\,\mathbf k_1\times\left(v_x\,\mathbf i_1 + v_y\,\mathbf j_1 + v_z\,\mathbf k_1\right) = 2\omega\left(v_x\,\mathbf j_1 - v_y\,\mathbf i_1\right) \quad &\text{(the two equal terms: Coriolis)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \omega\,\mathbf k_1\times\omega\left(x\,\mathbf j_1 - y\,\mathbf i_1\right) = -\omega^2\left(x\,\mathbf i_1 + y\,\mathbf j_1\right) \quad &\text{(the last term: centripetal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - \omega^2\left(x\,\mathbf i_1 + y\,\mathbf j_1\right) + 2\omega\left(v_x\,\mathbf j_1 - v_y\,\mathbf i_1\right)}$$
>
> **Units:** $[\omega^2x] = [\omega v_x] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the centripetal term points horizontally to the axis of the bar; the Coriolis term is horizontal and normal to the horizontal part of the relative velocity.

#### (c) AC, l and phi as functions of xi and time

> [!derivation] Length AC and length l
> **Law:** distance between two points; constant length of the string
> **Source:** Notes.pdf, Eq. 2.5; Problems.pdf, p. 24
>
> $$\begin{aligned}
> \overrightarrow{AC} &= \mathbf r_1^C - \mathbf r_1^A = \left(\xi - R\cos\omega t\right)\mathbf i_1 + R\sin\omega t\,\mathbf j_1 - h\,\mathbf k_1 \quad &\text{($\mathbf r_1^C = \xi\,\mathbf i_1$; part (a))} \\
> D^2 &= \left(\xi - R\cos\omega t\right)^2 + R^2\sin^2\omega t + h^2 = \xi^2 - 2R\xi\cos\omega t + R^2\left(\cos^2\omega t + \sin^2\omega t\right) + h^2 \quad &\text{(square expanded)} \\
> \ell &= L - D \quad &\text{(string of constant length)}
> \end{aligned}$$
>
> $$\boxed{AC = D = \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}, \qquad \ell = L - \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}}$$
>
> **Units:** $[D] = [\ell] = [\mathrm{L}]$
> **Meaning:** the cosine law in the triangle $OA'C$ plus the height: as the anchor falls behind the bar, $AC$ grows and the hanging part shortens.

![[attachments/EM-SOL/p36-contact.svg]]

> [!derivation] Angle phi from the frictionless contact
> **Law:** equilibrium of the massless piece of string at $C$; smooth contact: the bar pushes normal to itself
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 6.16; Problems.pdf, p. 24
>
> Without friction the tension is the same on both sides of $C$. The piece of string at $C$ is massless, so the two pulls and the push $\mathbf N_b$ of the bar add up to zero, and $\mathbf N_b$ has no component along the bar.
>
> $$\begin{aligned}
> T\,\mathbf e_{CA} + T\,\mathbf e_{CP} + \mathbf N_b &= \mathbf 0, \quad \mathbf N_b\cdot\mathbf i_1 = 0 \quad &\text{(equilibrium; smooth bar)} \\
> \mathbf e_{CP}\cdot\mathbf i_1 &= -\mathbf e_{CA}\cdot\mathbf i_1 = \frac{\overrightarrow{AC}\cdot\mathbf i_1}{D} \quad &\text{(projection on $\mathbf i_1$; $\mathbf e_{CA} = -\overrightarrow{AC}/D$)} \\
> \cos\varphi &= \frac{\xi - R\cos\omega t}{D}, \quad \sin\varphi = \sqrt{1 - \cos^2\varphi} = \frac{\sqrt{R^2\sin^2\omega t + h^2}}{D} \quad &\text{($\varphi$ in $(0, \pi)$: positive sine; $D^2$ of the box above)}
> \end{aligned}$$
>
> $$\boxed{\varphi = \arccos\frac{\xi - R\cos\omega t}{\sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}}}$$
>
> **Units:** $[\cos\varphi] = [\mathrm{L}]/[\mathrm{L}] = [1]$
> **Meaning:** the two segments make equal angles with the bar, on opposite sides of the plane normal to it: the string passes over the bar like a light ray reflected by a mirror. The bar pushes the string only across itself.

> [!derivation] Partial derivatives of l and phi with respect to xi and t
> **Law:** implicit differentiation of the two relations of part (c); chain rule
> **Source:** Problems.pdf, p. 24
>
> $$\begin{aligned}
> 2D\frac{\partial D}{\partial\xi} &= 2\xi - 2R\cos\omega t \;\Rightarrow\; \frac{\partial D}{\partial\xi} = \cos\varphi, \quad \frac{\partial\ell}{\partial\xi} = -\cos\varphi \quad &\text{(derivative of $D^2$)} \\
> 2D\frac{\partial D}{\partial t} &= 2R\xi\omega\sin\omega t \;\Rightarrow\; \frac{\partial\ell}{\partial t} = -\frac{R\omega\xi\sin\omega t}{D} \quad &\text{(chain rule on $\cos\omega t$)} \\
> \dot\ell &= \frac{\partial\ell}{\partial\xi}\dot\xi + \frac{\partial\ell}{\partial t} = -\dot\xi\cos\varphi - \frac{R\omega\xi\sin\omega t}{D} \quad &\text{(chain rule)} \\
> -\sin\varphi\,\frac{\partial\varphi}{\partial\xi} &= \frac{\partial}{\partial\xi}\left(\frac{\xi - R\cos\omega t}{D}\right) = \frac{D - \left(\xi - R\cos\omega t\right)\cos\varphi}{D^2} = \frac{1 - \cos^2\varphi}{D} \quad &\text{(quotient rule)} \\
> \frac{\partial\varphi}{\partial\xi} &= -\frac{\sin\varphi}{D}, \quad \ddot\varphi = \frac{\partial\varphi}{\partial\xi}\ddot\xi + \left(\text{terms in } \xi,\ \dot\xi,\ t\right) \quad &\text{(chain rule twice: $\ddot\xi$ appears only through the first factor)}
> \end{aligned}$$
>
> $$\boxed{\dot\ell + \dot\xi\cos\varphi = -\frac{R\omega\xi\sin\omega t}{D}, \qquad \frac{\partial\ell}{\partial\xi} = -\cos\varphi, \qquad \frac{\partial\varphi}{\partial\xi} = -\frac{\sin\varphi}{D}}$$
>
> **Units:** $[R\omega\xi/D] = [\mathrm{L\,T^{-1}}]$; $[\partial\varphi/\partial\xi] = [\mathrm{L^{-1}}]$
> **Meaning:** the string pays out along $CP$ (the left side is the rate of the projection of the relative velocity on $\mathbf e_{CP}$) only because the anchor moves; with the anchor fixed in $S_1$ the right side would vanish.

### Forces and Equations of Motion

![[attachments/EM-SOL/p36-fbd.svg]]

#### (d) Forces acting on P

> [!derivation] Actual and inertia forces on P
> **Law:** weight; string pull along the string; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]; Problems.pdf, p. 24
>
> $$\begin{aligned}
> \mathbf W &= -mg\,\mathbf k_1, \quad \mathbf T = -T\,\mathbf e_{CP} = -T\cos\varphi\,\mathbf i_1 + T\sin\varphi\sin\theta\,\mathbf j_1 + T\sin\varphi\cos\theta\,\mathbf k_1 \quad &\text{(weight; pull towards $C$, $T \gt 0$)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{($O$ fixed; $\omega$ constant)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\omega^2\left(x\,\mathbf i_1 + y\,\mathbf j_1\right) \quad &\text{(composition box times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\omega v_y\,\mathbf i_1 - 2m\omega v_x\,\mathbf j_1 \quad &\text{(composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf W = -mg\,\mathbf k_1, \quad \mathbf T = -T\,\mathbf e_{CP}, \quad \mathbf F_C = m\omega^2\left(\xi + \ell\cos\varphi\right)\mathbf i_1 - m\omega^2\ell\sin\varphi\sin\theta\,\mathbf j_1, \cr \mathbf F_{COR} = -2m\omega\left(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta\right)\mathbf i_1 - 2m\omega\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right)\mathbf j_1 \end{gathered}}$$
>
> **Units:** $[mg] = [m\omega^2\xi] = [m\omega\dot\xi] = [T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two actual forces (weight and string) and two inertia forces, both horizontal: the centrifugal force away from the axis, the Coriolis force normal to the horizontal relative velocity.

#### (e) Equations of motion

> [!derivation] Projections of each force on the string basis
> **Law:** scalar products with the columns of $[{}_1R_2]$
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 4.63
>
> From the columns of $[{}_1R_2]$: the projections of $\mathbf i_1$ on $\mathbf e_{CP}$, $\mathbf e_\varphi$, $\mathbf e_\theta$ are the cosine, minus the sine and 0; those of $\mathbf j_1$ are $-\sin\varphi\sin\theta$, $-\cos\varphi\sin\theta$ and $-\cos\theta$; those of $\mathbf k_1$ are $-\sin\varphi\cos\theta$, $-\cos\varphi\cos\theta$ and $\sin\theta$. In the Coriolis projections the terms in $\dot\varphi$ cancel along $\mathbf e_\varphi$ and the terms in $\dot\ell$ cancel along $\mathbf e_{CP}$.
>
> $$\begin{aligned}
> \mathbf W\cdot\mathbf e_\theta &= -mg\sin\theta, \quad \mathbf W\cdot\mathbf e_\varphi = mg\cos\varphi\cos\theta, \quad \mathbf W\cdot\mathbf e_{CP} = mg\sin\varphi\cos\theta \quad &\text{(third row of $[{}_1R_2]$ times $-mg$)} \\
> \mathbf F_C\cdot\mathbf e_\theta &= m\omega^2\left(-y\cos\theta\right) = m\omega^2\ell\sin\varphi\sin\theta\cos\theta \quad &\text{($\mathbf i_1\cdot\mathbf e_\theta = 0$)} \\
> \mathbf F_C\cdot\mathbf e_\varphi &= m\omega^2\left(-x\sin\varphi - y\cos\varphi\sin\theta\right) = -m\omega^2\sin\varphi\left(\xi + \ell\cos\varphi - \ell\cos\varphi\sin^2\theta\right) = -m\omega^2\sin\varphi\left(\xi + \ell\cos\varphi\cos^2\theta\right) \quad &\text{($1 - \sin^2\theta = \cos^2\theta$)} \\
> \mathbf F_C\cdot\mathbf e_{CP} &= m\omega^2\left(x\cos\varphi - y\sin\varphi\sin\theta\right) = m\omega^2\left[\left(\xi + \ell\cos\varphi\right)\cos\varphi + \ell\sin^2\varphi\sin^2\theta\right] \quad &\text{(first column)} \\
> \mathbf F_{COR}\cdot\mathbf e_\theta &= -2m\omega v_x\left(-\cos\theta\right) = 2m\omega\cos\theta\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right) \quad &\text{(second column)} \\
> \mathbf F_{COR}\cdot\mathbf e_\varphi &= 2m\omega\left(-v_y\sin\varphi + v_x\cos\varphi\sin\theta\right) = 2m\omega\left[\sin\theta\left(\dot\ell + \dot\xi\cos\varphi\right) + \ell\dot\theta\sin^2\varphi\cos\theta\right] \quad &\text{($\sin^2\varphi + \cos^2\varphi = 1$)} \\
> \mathbf F_{COR}\cdot\mathbf e_{CP} &= 2m\omega\left(v_y\cos\varphi + v_x\sin\varphi\sin\theta\right) = 2m\omega\left[\sin\theta\left(\dot\xi\sin\varphi - \ell\dot\varphi\right) - \ell\dot\theta\sin\varphi\cos\varphi\cos\theta\right] \quad &\text{(first column)} \\
> \mathbf T\cdot\mathbf e_\theta &= \mathbf T\cdot\mathbf e_\varphi = 0, \quad \mathbf T\cdot\mathbf e_{CP} = -T \quad &\text{(string along $\mathbf e_{CP}$)} \\
> m\,\mathbf a_1^P\cdot\mathbf e_\varphi &= m\left(\ell\ddot\varphi + 2\dot\ell\dot\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi - \ddot\xi\sin\varphi\right), \quad m\,\mathbf a_1^P\cdot\mathbf e_{CP} = m\left(\ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi + \ddot\xi\cos\varphi\right) \quad &\text{($\ddot\xi\,\mathbf i_1$ projected)}
> \end{aligned}$$
>
> $$\boxed{\text{every projection of } \mathbf W,\ \mathbf T,\ \mathbf F_C,\ \mathbf F_{COR} \text{ and } m\,\mathbf a_1^P \text{ on } \mathbf e_\theta,\ \mathbf e_\varphi,\ \mathbf e_{CP} \text{ as listed}}$$
>
> **Units:** every projection $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the tension appears only along $\mathbf e_{CP}$, so the two other projections are free of it.

> [!derivation] Two equations of motion and the tension
> **Law:** Newton's second law in a non-inertial frame projected on $\mathcal B_2$; elimination of $\ell$ and $\varphi$ through part (c)
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; Problems.pdf, p. 24
>
> Three scalar equations for the three unknowns $\xi$, $\theta$ and $T$. In the $\mathbf e_\varphi$ equation the second derivative of $\xi$ appears in $-\ddot\xi\sin\varphi$ and, through the chain rule of part (c), in $\ell\ddot\varphi$; their sum has a coefficient that does not vanish while the string is bent.
>
> $$\begin{aligned}
> \mathbf e_\theta:\ \ell\sin\varphi\,\ddot\theta + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi &= -g\sin\theta + \omega^2\ell\sin\varphi\sin\theta\cos\theta + 2\omega\cos\theta\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right) \quad &\text{(divided by $m$)} \\
> \mathbf e_\varphi:\ \ell\ddot\varphi + 2\dot\ell\dot\varphi - \ddot\xi\sin\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi &= g\cos\varphi\cos\theta - \omega^2\sin\varphi\left(\xi + \ell\cos\varphi\cos^2\theta\right) + 2\omega\left[\sin\theta\left(\dot\ell + \dot\xi\cos\varphi\right) + \ell\dot\theta\sin^2\varphi\cos\theta\right] \quad &\text{(divided by $m$)} \\
> \mathbf e_{CP}:\ m\left(\ddot\xi\cos\varphi + \ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi\right) &= -T + mg\sin\varphi\cos\theta + \mathbf F_C\cdot\mathbf e_{CP} + \mathbf F_{COR}\cdot\mathbf e_{CP} \quad &\text{(gives $T$)} \\
> \ell\,\frac{\partial\varphi}{\partial\xi}\ddot\xi - \sin\varphi\,\ddot\xi &= -\left(\frac{\ell}{D} + 1\right)\sin\varphi\,\ddot\xi = -\frac{L}{D}\sin\varphi\,\ddot\xi \quad &\text{(coefficient of $\ddot\xi$ in the $\mathbf e_\varphi$ equation; $\ell + D = L$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \ell\sin\varphi\,\ddot\theta + 2\dot\ell\dot\theta\sin\varphi + 2\ell\dot\theta\dot\varphi\cos\varphi = -g\sin\theta + \omega^2\ell\sin\varphi\sin\theta\cos\theta + 2\omega\cos\theta\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right) \cr \ell\ddot\varphi + 2\dot\ell\dot\varphi - \ddot\xi\sin\varphi - \ell\dot\theta^2\sin\varphi\cos\varphi = g\cos\varphi\cos\theta - \omega^2\sin\varphi\left(\xi + \ell\cos\varphi\cos^2\theta\right) + 2\omega\left[\sin\theta\left(\dot\ell + \dot\xi\cos\varphi\right) + \ell\dot\theta\sin^2\varphi\cos\theta\right] \cr T = -m\left(\ddot\xi\cos\varphi + \ddot\ell - \ell\dot\varphi^2 - \ell\dot\theta^2\sin^2\varphi\right) + mg\sin\varphi\cos\theta + m\omega^2\left[\left(\xi + \ell\cos\varphi\right)\cos\varphi + \ell\sin^2\varphi\sin^2\theta\right] + 2m\omega\left[\sin\theta\left(\dot\xi\sin\varphi - \ell\dot\varphi\right) - \ell\dot\theta\sin\varphi\cos\varphi\cos\theta\right] \end{gathered}}$$
>
> **Units:** every term of the first two lines $[\mathrm{L\,T^{-2}}]$; $[T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** with $\ell$, $\varphi$ and their derivatives replaced by the functions of $\xi$, its rate and time of part (c), the first two lines are two second-order equations for $\xi$ and $\theta$ (the coefficients of their second derivatives, $\ell\sin\varphi$ and minus $L$ over $D$ times the sine, are not zero while the string is bent), with time present explicitly through the motion of the anchor. The third gives the tension; the solution holds while it stays positive.

### Answers and Checks

#### (f) Initial conditions at t equal to zero

> [!derivation] Initial position
> **Law:** geometry at the instant of the impact
> **Source:** Problems.pdf, p. 24
>
> At the start the bar lies along $\mathbf i_0$ and meets the vertical string at $A'$, directly below $A$; the particle hangs in the vertical plane $Ox_1z_1$.
>
> $$\begin{aligned}
> \xi(0) &= R, \quad D(0) = \sqrt{R^2 - 2R^2 + R^2 + h^2} = h, \quad \ell(0) = L - h \quad &\text{(part (c) at $t = 0$)} \\
> \cos\varphi(0) &= \frac{R - R}{h} = 0 \;\Rightarrow\; \varphi(0) = \tfrac{\pi}{2}, \quad \theta(0) = 0 \quad &\text{(string normal to the bar, hanging)} \\
> \mathbf e_{CP}(0) &= -\mathbf k_1, \quad \mathbf e_\varphi(0) = -\mathbf i_1, \quad \mathbf e_\theta(0) = -\mathbf j_1, \quad \mathbf r_1^P(0) = R\,\mathbf i_1 - \left(L - h\right)\mathbf k_1 \quad &\text{(columns of $[{}_1R_2]$ at these angles)}
> \end{aligned}$$
>
> $$\boxed{\xi(0) = R, \quad \theta(0) = 0 \qquad \left(\ell(0) = L - h,\ \varphi(0) = \tfrac{\pi}{2}\right)}$$
>
> **Units:** $[\xi] = [\ell] = [\mathrm{L}]$
> **Meaning:** the particle is a depth $L - h$ below the bar, that is $L$ below the anchor.

> [!derivation] Initial rates
> **Law:** continuity of the absolute velocity (no impulse); composition of velocities; the velocity of part (b) at the start
> **Source:** Notes.pdf, Eq. 3.26; Problems.pdf, p. 24
>
> The particle is at rest in $S_0$ just before the impact. The string meets the bar at a right angle, so its path length grows only to second order in time ($\dot\ell(0)$ is zero below) and no impulsive tension acts: the absolute velocity stays zero. The velocity of part (b) is written at the start before the components are matched.
>
> $$\begin{aligned}
> \mathbf v_1^P(0) &= \mathbf v_0^P(0) - \boldsymbol\omega_{10}\times\mathbf r_1^P(0) = \mathbf 0 - \omega\,\mathbf k_1\times\left[R\,\mathbf i_1 - \left(L - h\right)\mathbf k_1\right] = -\omega R\,\mathbf j_1 \quad &\text{(Eq. 3.26 with $\mathbf v_0^O$ zero)} \\
> \mathbf v_1^P(0) &= \dot\xi\,\mathbf i_1 + \dot\ell\left(-\mathbf k_1\right) + \left(L - h\right)\dot\varphi\left(-\mathbf i_1\right) + \left(L - h\right)\dot\theta\left(-\mathbf j_1\right) \quad &\text{(part (b) at $\varphi = \pi/2$, $\theta = 0$)} \\
> \mathbf k_1:\ \dot\ell(0) &= 0, \quad \text{and part (c): } \dot\ell(0) = -\dot\xi(0)\cos\tfrac{\pi}{2} - \frac{R\omega R\sin 0}{h} = 0 \quad &\text{(consistent)} \\
> \mathbf j_1:\ \left(L - h\right)\dot\theta(0) &= \omega R \;\Rightarrow\; \dot\theta(0) = \frac{\omega R}{L - h} \quad &\text{(sideways component)} \\
> \dot\varphi(0) &= \frac{\partial\varphi}{\partial\xi}\dot\xi + \frac{\partial\varphi}{\partial t} = -\frac{\sin\tfrac{\pi}{2}}{h}\dot\xi(0) + 0 = -\frac{\dot\xi(0)}{h} \quad &\text{(chain rule; $\partial\varphi/\partial t$ is zero at $t = 0$, from $\cos\varphi\,D = \xi - R\cos\omega t$)} \\
> \mathbf i_1:\ \dot\xi(0) - \left(L - h\right)\dot\varphi(0) &= \dot\xi(0)\left(1 + \frac{L - h}{h}\right) = \frac{L}{h}\dot\xi(0) = 0 \;\Rightarrow\; \dot\xi(0) = 0,\ \dot\varphi(0) = 0 \quad &\text{(component along the bar)}
> \end{aligned}$$
>
> $$\boxed{\xi(0) = R, \quad \dot\xi(0) = 0, \quad \theta(0) = 0, \quad \dot\theta(0) = \frac{\omega R}{L - h} \qquad \left(\dot\ell(0) = 0,\ \dot\varphi(0) = 0\right)}$$
>
> **Units:** $[\dot\theta(0)] = [\omega R/(L - h)] = [\mathrm{T^{-1}}]$
> **Meaning:** seen from the bar, the particle starts moving backwards with the speed of the point of the bar that hits the string, swinging about $C$ as a pendulum of length $L - h$; $\theta$ grows from zero towards the side of the anchor. The time derivative of $\varphi$ at fixed $\xi$ vanishes at the start because the derivative of the cosine of $\omega t$ is zero there.

#### (g) Is the mechanical energy of the particle conserved?

> [!derivation] Rate of the energy in S0 and in S1
> **Law:** power of the forces on the absolute and on the relative velocity; potentials of the weight and of the centrifugal force
> **Source:** Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> In $S_0$ the weight has the potential $mgz$ and the only other force is the string pull. In $S_1$ the weight and the centrifugal force (constant rate, fixed axis) have potentials, the Coriolis force does no work, and again only the string pull is left. Let $E_0^P$ be one half of $m$ times the squared absolute speed plus $mgz$, and $E_1^P$ one half of $m$ times the squared relative speed plus $mgz$ minus one half of $m\omega^2(x^2 + y^2)$. The projection of the relative velocity on $\mathbf e_{CP}$ is $\dot\xi\cos\varphi + \dot\ell$.
>
> $$\begin{aligned}
> \frac{dE_1^P}{dt} &= \mathbf T\cdot\mathbf v_1^P = -T\left(\dot\xi\cos\varphi + \dot\ell\right) = \frac{TR\omega\xi\sin\omega t}{D} \quad &\text{(Eq. 4.29 in $S_1$; part (c))} \\
> \mathbf e_{CP}\cdot\omega\left(x\,\mathbf j_1 - y\,\mathbf i_1\right) &= \omega\left[-\left(\xi + \ell\cos\varphi\right)\sin\varphi\sin\theta + \ell\sin\varphi\sin\theta\cos\varphi\right] = -\omega\xi\sin\varphi\sin\theta \quad &\text{(the transport velocity of the composition box on $\mathbf e_{CP}$)} \\
> \frac{dE_0^P}{dt} &= \mathbf T\cdot\mathbf v_0^P = \mathbf T\cdot\mathbf v_1^P - T\,\mathbf e_{CP}\cdot\omega\left(x\,\mathbf j_1 - y\,\mathbf i_1\right) = T\omega\xi\left(\frac{R\sin\omega t}{D} + \sin\varphi\sin\theta\right) \quad &\text{(Eq. 4.29 in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_0^P}{dt} = T\omega\xi\left(\frac{R\sin\omega t}{D} + \sin\varphi\sin\theta\right) \ne 0, \qquad \frac{dE_1^P}{dt} = \frac{TR\omega\xi\sin\omega t}{D} \ne 0: \ \text{not conserved}}$$
>
> **Units:** $[T\omega\xi] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** no. The string is a moving constraint: in $S_0$ the bar drags the bend of the string, in $S_1$ the anchor moves, and in both frames the tension works on the particle. While the anchor is behind the bar (the sine of $\omega t$ positive) and the string is tense, the energy in $S_1$ grows. The energy comes from the motor that keeps the rate of the bar constant (check box below).

#### (h) Separation of the string from the bar

> [!derivation] Geometric condition of separation
> **Law:** the bar pushes the string only while the string is bent at $C$; straight string: $A$, $C$ and $P$ collinear
> **Source:** Notes.pdf, Eq. 4.32; Problems.pdf, p. 24
>
> The push of the bar is minus $T$ times the sum of $\mathbf e_{CA}$ and $\mathbf e_{CP}$ (contact box); it vanishes when the string is straight, and beyond that instant the bend would have to reverse, which a bar pushing from one side cannot impose. The components along $\mathbf i_1$ of $\mathbf e_{CP}$ and of minus $\mathbf e_{CA}$ are already equal (contact box); the other two components are equated, with the sine of $\varphi$ from part (c).
>
> $$\begin{aligned}
> \mathbf e_{CP} &= -\mathbf e_{CA} = \frac{\overrightarrow{AC}}{D} \quad &\text{(straight string)} \\
> \mathbf j_1:\ -\sin\varphi\sin\theta &= \frac{R\sin\omega t}{D} \;\Rightarrow\; \sin\theta = -\frac{R\sin\omega t}{\sqrt{R^2\sin^2\omega t + h^2}} \quad &\text{($\sin\varphi\,D = \sqrt{R^2\sin^2\omega t + h^2}$)} \\
> \mathbf k_1:\ -\sin\varphi\cos\theta &= -\frac{h}{D} \;\Rightarrow\; \cos\theta = \frac{h}{\sqrt{R^2\sin^2\omega t + h^2}} \gt 0 \quad &\text{(vertical component)} \\
> \tan\theta &= \frac{\sin\theta}{\cos\theta} = -\frac{R\sin\omega t}{h} \quad &\text{(quotient)}
> \end{aligned}$$
>
> $$\boxed{\tan\theta = -\frac{R\sin\omega t}{h}, \qquad \theta_{sep}(t) = -\arctan\frac{R\sin\omega t}{h}}$$
>
> **Units:** $[R\sin\omega t/h] = [1]$
> **Meaning:** the string leaves the bar at the first instant at which the angle obtained from the equations of part (e) reaches this value. For the sine of $\omega t$ positive the value is negative: the particle must have swung forward, past the vertical plane of the bar, to the side opposite to the anchor, so that the straight line from $A$ through $C$ reaches it.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Anchor in $S_1$ | $\mathbf r_1^A = R\cos\omega t\,\mathbf i_1 - R\sin\omega t\,\mathbf j_1 + h\,\mathbf k_1$, $\mathbf v_1^A = -R\omega\sin\omega t\,\mathbf i_1 - R\omega\cos\omega t\,\mathbf j_1$ |
| (b) $P$ in $S_1$ | $\mathbf r_1^P = \xi\,\mathbf i_1 + \ell\,\mathbf e_{CP}$; $\mathbf v_1^P = \dot\xi\,\mathbf i_1 + \dot\ell\,\mathbf e_{CP} + \ell\dot\varphi\,\mathbf e_\varphi + \ell\dot\theta\sin\varphi\,\mathbf e_\theta$; $\mathbf a_1^P$ as boxed in part (b), with $\mathbf e_{CP}, \mathbf e_\theta, \mathbf e_\varphi$ the columns of $[{}_1R_2]$ |
| (c) $AC$, $\ell$, $\varphi$ | $AC = \sqrt{\xi^2 - 2R\xi\cos\omega t + R^2 + h^2}$, $\ell = L - AC$, $\cos\varphi = (\xi - R\cos\omega t)/AC$ |
| (d) Forces | $\mathbf W = -mg\,\mathbf k_1$, $\mathbf T = -T\,\mathbf e_{CP}$, $\mathbf F_C = m\omega^2(\xi + \ell\cos\varphi)\,\mathbf i_1 - m\omega^2\ell\sin\varphi\sin\theta\,\mathbf j_1$, $\mathbf F_{COR} = -2m\omega(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta)\,\mathbf i_1 - 2m\omega(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi)\,\mathbf j_1$; origin and Euler forces zero |
| (e) Equations | the $\mathbf e_\theta$ and $\mathbf e_\varphi$ equations of part (e), closed with part (c): two second-order equations for $\xi(t)$, $\theta(t)$; the $\mathbf e_{CP}$ equation gives $T$ |
| (f) Initial conditions | $\xi(0) = R$, $\dot\xi(0) = 0$, $\theta(0) = 0$, $\dot\theta(0) = \omega R/(L - h)$ (and $\ell(0) = L - h$, $\varphi(0) = \pi/2$, $\dot\ell(0) = \dot\varphi(0) = 0$) |
| (g) Energy | not conserved in $S_0$ nor in $S_1$: $dE_0^P/dt = T\omega\xi(R\sin\omega t/AC + \sin\varphi\sin\theta)$, $dE_1^P/dt = TR\omega\xi\sin\omega t/AC$ |
| (h) Separation | $\tan\theta = -R\sin\omega t/h$ (string straight); the other way to lose contact, $C$ reaching the end of the bar, is $\xi$ equal to the half-length of the bar |

**Check against the official key:** Problems.pdf, p. 75 prints only the centrifugal and the Coriolis forces; both coincide term by term with part (d) (box below). The rest is checked independently with the power of the bar on the string and with limiting cases.

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison
> **Source:** Problems.pdf, p. 75
>
> $$\begin{aligned}
> \text{key: } \mathbf F_{cent} &= m\omega^2\left(\xi + \ell\cos\varphi\right)\mathbf i_1 - m\omega^2\ell\sin\varphi\sin\theta\,\mathbf j_1 = \mathbf F_C \quad &\text{(part (d))} \\
> \text{key: } \mathbf F_{Cori} &= -2m\omega\left(\dot\ell\sin\varphi\sin\theta + \ell\dot\varphi\cos\varphi\sin\theta + \ell\dot\theta\sin\varphi\cos\theta\right)\mathbf i_1 - 2m\omega\left(\dot\xi + \dot\ell\cos\varphi - \ell\dot\varphi\sin\varphi\right)\mathbf j_1 = \mathbf F_{COR} \quad &\text{(part (d))}
> \end{aligned}$$
>
> $$\boxed{\text{both inertia forces coincide with the key}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the agreement also confirms the reading of the sense of rotation and of the sign of $\theta$.

> [!derivation] Independent check: the energy comes from the bar
> **Law:** power of the push of the bar on the string at the moving contact point; the massless string transmits it to the particle
> **Source:** Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 4.29
>
> The contact point moves in $S_0$ with the velocity of part (b) for a point at $\xi$ on the bar, $\dot\xi\,\mathbf i_1 + \omega\xi\,\mathbf j_1$; the push of the bar has no component along $\mathbf i_1$. The anchor is fixed, so the string receives power only at $C$, and a massless string passes it on to the particle.
>
> $$\begin{aligned}
> \mathbf N_b &= -T\left(\mathbf e_{CA} + \mathbf e_{CP}\right), \quad \mathbf e_{CA}\cdot\mathbf j_1 = -\frac{R\sin\omega t}{D}, \quad \mathbf e_{CP}\cdot\mathbf j_1 = -\sin\varphi\sin\theta \quad &\text{(contact box; part (c))} \\
> \mathbf N_b\cdot\left(\dot\xi\,\mathbf i_1 + \omega\xi\,\mathbf j_1\right) &= 0 - T\omega\xi\left(-\frac{R\sin\omega t}{D} - \sin\varphi\sin\theta\right) = T\omega\xi\left(\frac{R\sin\omega t}{D} + \sin\varphi\sin\theta\right) \quad &\text{(power of the bar)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N_b\cdot\mathbf v_0^C = \frac{dE_0^P}{dt}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-3}}]$
> **Meaning:** the rate of the energy found in part (g) is exactly the power the bar puts into the string.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]
>
> $$\begin{aligned}
> R \to 0:\quad \frac{dE_1^P}{dt} &\to 0 \quad &\text{(anchor on the axis, fixed in $S_1$: the energy in $S_1$ becomes a first integral)} \\
> h \to \infty:\quad \theta_{sep} &\to 0 \quad &\text{(very high ceiling: the string separates near the vertical plane of the bar)} \\
> \omega t = \pi:\quad \theta_{sep} &= 0 \quad &\text{(anchor straight across the bar)} \\
> \theta = 0,\ \varphi = \tfrac{\pi}{2}:\quad \mathbf e_{CP} &= \mathbf u = -\mathbf k_1 \quad &\text{(the hanging string)}
> \end{aligned}$$
>
> $$\boxed{R \to 0: \ E_1^P \text{ conserved}; \qquad h \to \infty \text{ or } \omega t = \pi: \ \theta_{sep} = 0}$$
>
> **Units:** dimensionless
> **Meaning:** each limit matches the picture of an anchor that moves in the frame of the bar and feeds energy into the pendulum.

---

## Problem 37: Particle on a Spinning Elliptic Cone

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ moves without friction on a cone of elliptic cross-section, with vertex $O$ and vertical axis, described by the parameters $\zeta$ and $\beta$; the cone spins about its axis at the constant rate $\Omega$, and at the start the frames coincide, with the particle at $2\,\mathbf j_1 + \mathbf k_1$ and the velocity $\mathbf i_1$ (Problems.pdf, p. 25). The statement asks for the degrees of freedom, the position, velocity and acceleration in $S_1$, the forces seen from $S_1$, two equations of motion free of other unknowns, one conservation law with its constant, and the equilibria for positive $\zeta$. The cone is at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ the vertex (fixed), $\mathbf k_0$ vertical, up |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, attached to the cone: $\mathbf k_1 = \mathbf k_0$ along its axis, $\mathbf i_1$ and $\mathbf j_1$ along the axes of its elliptic sections; it turns by $\Omega t$ about $\mathbf k_0$, from $x_0$ towards $y_0$ (figure), and coincides with $S_0$ at $t = 0$ |
| Cone | $x_1 = \zeta\cos\beta$, $y_1 = 2\zeta\sin\beta$, $z_1 = \zeta$ (Eq. (5) of the statement), fixed in $S_1$ |
| Surface vectors at $P$ | $\mathbf e_\zeta$ and $\mathbf e_\beta$ (tangent, not unit; deduced below), unit normal $\mathbf n$ |
| Coordinates | $\zeta$ (height above the vertex), $\beta$ (angular parameter of the elliptic section, not the polar angle) |
| Data | $m$ [kg], $g$ [m s$^{-2}$], $\Omega$ [rad s$^{-1}$]; initial position $2\,\mathbf j_1 + \mathbf k_1$ and velocity $\mathbf i_1$ |
| Unknowns | $\zeta(t)$, $\beta(t)$ and the reaction $N\,\mathbf n$ |
| Applied forces | weight $-mg\,\mathbf k_1$ |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; smooth contact; $\Omega$ constant |
| Readings | (1) The initial data carry no units; they are read in SI units (metres and metres per second); with another unit of length the numbers of the constant of part (e) change accordingly. (2) The contact is taken as bilateral (the normal reaction may take either sign); the particle is on the inner surface of the cone, and the equilibria of part (f) need a positive reaction along the inward normal, which is checked there |

#### (a) Degrees of freedom

> [!derivation] Equation of the cone and number of degrees of freedom
> **Law:** elimination of the parameters; a holonomic constraint removes one coordinate
> **Source:** Notes.pdf, Eq. 6.3; Problems.pdf, p. 25
>
> $$\begin{aligned}
> \cos\beta &= \frac{x_1}{\zeta}, \quad \sin\beta = \frac{y_1}{2\zeta}, \quad \zeta = z_1 \quad &\text{(Eq. (5) solved for the parameters)} \\
> \cos^2\beta + \sin^2\beta &= \frac{x_1^2}{z_1^2} + \frac{y_1^2}{4z_1^2} = 1 \;\Rightarrow\; x_1^2 + \frac{y_1^2}{4} - z_1^2 = 0 \quad &\text{(Pythagorean identity)} \\
> \text{degrees of freedom} &= 3 - 1 = 2 \quad &\text{(one holonomic constraint, fixed in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{x_1^2 + \frac{y_1^2}{4} - z_1^2 = 0, \qquad \text{2 degrees of freedom: } \zeta,\ \beta}$$
>
> **Units:** $[x_1^2] = [y_1^2] = [z_1^2] = [\mathrm{L^2}]$
> **Meaning:** each horizontal section at the height $\zeta$ is an ellipse of semi-axes $\zeta$ along $\mathbf i_1$ and $2\zeta$ along $\mathbf j_1$.

### Change of Basis and Position Vector

![[attachments/EM-SOL/p37-top-view.svg]]

> [!derivation] Basis of the cone: rotation by Omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page. The figure measures $\Omega t$ from $x_0$ towards $y_0$, so the cone turns counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\Omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \left(-\sin\Omega t\right)\sin\Omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \cr \sin\Omega t & \cos\Omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Omega t] = [1]$
> **Meaning:** these are the unit vectors of $\mathcal B_1$ in terms of $\mathcal B_0$, as the statement asks; at the start the matrix is the identity and the frames coincide.

![[attachments/EM-SOL/p37-section.svg]]

> [!derivation] Position vector of P: the elliptic section through P
> **Law:** position up the axis and across the horizontal section; auxiliary circle; stretch of the ellipse
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 25
>
> The section at the height $\zeta$ is seen from above. Draw the auxiliary circle of radius $\zeta$ and its point $B$ at the polar angle $\beta$: in the shaded right triangle with hypotenuse $OB$, of length $\zeta$, the leg adjacent to $\beta$ is $\zeta\cos\beta$ along $\mathbf i_1$ and the opposite leg is $\zeta\sin\beta$ along $\mathbf j_1$. The point $P$ of the ellipse has the same abscissa and twice the ordinate: the ellipse is the circle stretched by 2 along $\mathbf j_1$. So $\beta$ is the polar angle of $B$, not of $P$; the polar angle $\alpha$ of the horizontal projection of $P$ is related to it below.
>
> $$\begin{aligned}
> \mathbf r_0^O &= \mathbf 0, \quad \mathbf r_0^P = \mathbf r_1^P = \zeta\,\mathbf k_1 + \zeta\cos\beta\,\mathbf i_1 + 2\zeta\sin\beta\,\mathbf j_1 \quad &\text{(up the axis, then across the section; Eq. 3.16)} \\
> \tan\alpha &= \frac{y_1}{x_1} = \frac{2\zeta\sin\beta}{\zeta\cos\beta} = 2\tan\beta \quad &\text{(polar angle of the projection)} \\
> \zeta_0 &= 1, \quad \zeta_0\cos\beta_0 = 0, \quad 2\zeta_0\sin\beta_0 = 2 \;\Rightarrow\; \beta_0 = \tfrac{\pi}{2} \quad &\text{(initial position $2\,\mathbf j_1 + \mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = \zeta\cos\beta\,\mathbf i_1 + 2\zeta\sin\beta\,\mathbf j_1 + \zeta\,\mathbf k_1, \qquad \zeta(0) = 1\ \mathrm{m}, \ \beta(0) = \tfrac{\pi}{2}}$$
>
> **Units:** $[\zeta] = [\mathrm{L}]$; $[\beta] = [1]$
> **Meaning:** the two angles coincide only on the axes of the ellipse; at the start the particle is at the end of the long axis of the section at height 1 m.

![[attachments/EM-SOL/p37-sections.svg]]

> [!derivation] Tangent vectors and unit normal of the cone
> **Law:** tangent vectors as partial derivatives of the position; normal as their vector product
> **Source:** Notes.pdf, Eq. 6.3; Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 6.10; Problems.pdf, p. 25
>
> The determinant is expanded along its first row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf e_\zeta &= \frac{\partial\mathbf r_1^P}{\partial\zeta} = \cos\beta\,\mathbf i_1 + 2\sin\beta\,\mathbf j_1 + \mathbf k_1 \quad &\text{(along the generator through $P$)} \\
> \frac{\partial\mathbf r_1^P}{\partial\beta} &= \zeta\,\mathbf e_\beta, \quad \mathbf e_\beta = -\sin\beta\,\mathbf i_1 + 2\cos\beta\,\mathbf j_1 \quad &\text{(tangent to the ellipse; $\tfrac{d}{d\beta}\cos\beta = -\sin\beta$)} \\
> \mathbf e_\zeta\times\mathbf e_\beta &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \cos\beta & 2\sin\beta & 1 \cr -\sin\beta & 2\cos\beta & 0 \end{vmatrix} = (+1)\left(0 - 2\cos\beta\right)\mathbf i_1 + (-1)\left(0 + \sin\beta\right)\mathbf j_1 + (+1)\left(2\cos^2\beta + 2\sin^2\beta\right)\mathbf k_1 \quad &\text{(first row; cofactor signs)} \\
> \left|\mathbf e_\zeta\times\mathbf e_\beta\right|^2 &= 4\cos^2\beta + \sin^2\beta + 4 = 5 + 3\cos^2\beta \quad &\text{(squared length)} \\
> \nabla\left(x_1^2 + \tfrac14 y_1^2 - z_1^2\right) &= \left(2x_1,\ \tfrac12 y_1,\ -2z_1\right) = -\zeta\left(-2\cos\beta,\ -\sin\beta,\ 2\right) \quad &\text{(check: parallel to the normal)} \\
> \mathbf e_\zeta\cdot\mathbf e_\beta &= -\sin\beta\cos\beta + 4\sin\beta\cos\beta = 3\sin\beta\cos\beta \quad &\text{(the tangent vectors are not orthogonal in general)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_\zeta = \cos\beta\,\mathbf i_1 + 2\sin\beta\,\mathbf j_1 + \mathbf k_1, \quad \mathbf e_\beta = -\sin\beta\,\mathbf i_1 + 2\cos\beta\,\mathbf j_1, \quad \mathbf n = \frac{-2\cos\beta\,\mathbf i_1 - \sin\beta\,\mathbf j_1 + 2\,\mathbf k_1}{\sqrt{5 + 3\cos^2\beta}}}$$
>
> **Units:** $[\mathbf e_\zeta] = [\mathbf e_\beta] = [\mathbf n] = [1]$
> **Meaning:** the normal points into the cone and upwards. In the vertical plane $x_1z_1$ the generators make 45 degrees with the horizontal (legs $\zeta$ and $\zeta$, hypotenuse $\zeta\sqrt2$); in the plane $y_1z_1$ they rise one for two across (legs $2\zeta$ and $\zeta$, hypotenuse $\zeta\sqrt5$), as drawn.

### Kinematics

> [!derivation] Motion of the cone frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed vertical; $\Omega$ constant; vertex fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf k_1\times\mathbf i_1 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \Omega\,\mathbf k_1\times\mathbf j_1 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0\right) &= -\Omega\sin\Omega t\,\mathbf i_0 + \Omega\cos\Omega t\,\mathbf j_0 = \Omega\,\mathbf j_1 \quad &\text{(check: chain rule)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\Omega] = [\mathrm{T^{-1}}]$
> **Meaning:** in $S_1$ the unit vectors are constant; in $S_0$ the horizontal ones turn with the cone.

#### (b) Position, velocity and acceleration in S1

> [!derivation] Relative velocity and relative acceleration
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.7; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 25
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\zeta\cos\beta\right) &= \dot\zeta\cos\beta - \zeta\sin\beta\,\dot\beta, \quad \frac{d}{dt}\left(2\zeta\sin\beta\right) = 2\dot\zeta\sin\beta + 2\zeta\cos\beta\,\dot\beta \quad &\text{(product rule; chain rule)} \\
> \mathbf v_1^P &= \left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\mathbf i_1 + 2\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\mathbf j_1 + \dot\zeta\,\mathbf k_1 = \dot\zeta\,\mathbf e_\zeta + \zeta\dot\beta\,\mathbf e_\beta \quad &\text{(Eq. 3.19; tangent to the cone)} \\
> \frac{d}{dt}\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right) &= \ddot\zeta\cos\beta - \dot\zeta\dot\beta\sin\beta - \dot\zeta\dot\beta\sin\beta - \zeta\ddot\beta\sin\beta - \zeta\dot\beta^2\cos\beta \quad &\text{(product rule on each term)} \\
> \frac{d}{dt}\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right) &= \ddot\zeta\sin\beta + \dot\zeta\dot\beta\cos\beta + \dot\zeta\dot\beta\cos\beta + \zeta\ddot\beta\cos\beta - \zeta\dot\beta^2\sin\beta \quad &\text{(product rule on each term)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf v_1^P = \left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\mathbf i_1 + 2\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\mathbf j_1 + \dot\zeta\,\mathbf k_1, \cr \mathbf a_1^P = \left[\left(\ddot\zeta - \zeta\dot\beta^2\right)\cos\beta - \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\sin\beta\right]\mathbf i_1 + 2\left[\left(\ddot\zeta - \zeta\dot\beta^2\right)\sin\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\cos\beta\right]\mathbf j_1 + \ddot\zeta\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[\dot\zeta] = [\zeta\dot\beta] = [\mathrm{L\,T^{-1}}]$; $[\ddot\zeta] = [\zeta\dot\beta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** with the unit vectors of $\mathcal B_1$ written in $\mathcal B_0$ in the rotation box, these are the vectors the statement asks for, as seen from $S_1$.

> [!derivation] Initial rates
> **Law:** the velocity of part (b) written at the start, matched with the datum
> **Source:** Problems.pdf, p. 25
>
> $$\begin{aligned}
> \mathbf v_1^P(0) &= \left(\dot\zeta_0\cdot 0 - 1\cdot\dot\beta_0\cdot 1\right)\mathbf i_1 + 2\left(\dot\zeta_0\cdot 1 + 1\cdot\dot\beta_0\cdot 0\right)\mathbf j_1 + \dot\zeta_0\,\mathbf k_1 = -\dot\beta_0\,\mathbf i_1 + 2\dot\zeta_0\,\mathbf j_1 + \dot\zeta_0\,\mathbf k_1 \quad &\text{($\zeta_0 = 1$, $\beta_0 = \pi/2$)} \\
> -\dot\beta_0\,\mathbf i_1 + 2\dot\zeta_0\,\mathbf j_1 + \dot\zeta_0\,\mathbf k_1 &= \mathbf i_1 \;\Rightarrow\; \dot\beta_0 = -1\ \mathrm{rad\,s^{-1}}, \quad \dot\zeta_0 = 0 \quad &\text{(three components; the second agrees with the third)}
> \end{aligned}$$
>
> $$\boxed{\dot\zeta(0) = 0, \qquad \dot\beta(0) = -1\ \mathrm{rad\,s^{-1}}}$$
>
> **Units:** $[\dot\beta] = [\mathrm{T^{-1}}]$
> **Meaning:** the initial velocity is horizontal and tangent to the section: the particle starts along the ellipse, towards decreasing $\beta$.

> [!derivation] Absolute acceleration: centripetal and Coriolis terms
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position as $x_1\,\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1$ with the components of part (b); their time derivatives are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1 + x_1\Omega\,\mathbf j_1 - y_1\Omega\,\mathbf i_1 = \mathbf v_1^P + \Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(product rule; the turning of the basis inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left[\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right)\right] &= \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(product rule; derivatives of $\mathbf j_1$, $\mathbf i_1$)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\Omega\,\mathbf k_1\times\left(\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1\right) = 2\Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(the two equal terms: Coriolis)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf k_1\times\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) = -\Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(the last term: centripetal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) + 2\Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right)}$$
>
> **Units:** $[\Omega^2x_1] = [\Omega\dot x_1] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** both rotation terms are horizontal; with the vertex fixed and the rate constant there are no origin or Euler terms.

### Forces and Equations of Motion

![[attachments/EM-SOL/p37-fbd.svg]]

#### (c) Forces acting on P as seen from S1

> [!derivation] Actual and inertia forces on the particle
> **Law:** weight; smooth reaction along the normal; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.11; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> \mathbf W &= -mg\,\mathbf k_1, \quad \mathbf N = N\,\mathbf n \quad &\text{(weight; smooth contact)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1^P = \mathbf 0 \quad &\text{(vertex fixed; $\Omega$ constant)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) = m\Omega^2\zeta\left(\cos\beta\,\mathbf i_1 + 2\sin\beta\,\mathbf j_1\right) \quad &\text{(composition box times $-m$)} \\
> \mathbf F_{COR} &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = 2m\Omega\left(\dot y_1\,\mathbf i_1 - \dot x_1\,\mathbf j_1\right) \quad &\text{(composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf W = -mg\,\mathbf k_1, \quad \mathbf N = N\,\frac{-2\cos\beta\,\mathbf i_1 - \sin\beta\,\mathbf j_1 + 2\,\mathbf k_1}{\sqrt{5 + 3\cos^2\beta}}, \quad \mathbf F_C = m\Omega^2\zeta\left(\cos\beta\,\mathbf i_1 + 2\sin\beta\,\mathbf j_1\right), \cr \mathbf F_{COR} = 4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\mathbf i_1 - 2m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\mathbf j_1 \end{gathered}}$$
>
> **Units:** $[mg] = [m\Omega^2\zeta] = [m\Omega\dot\zeta] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two actual forces and two inertia forces; the centrifugal force points horizontally away from the axis, the Coriolis force is horizontal and normal to the horizontal relative velocity. Newton's second law in $S_1$ is the sum of the four equal to the mass times the relative acceleration (Eq. 4.63).

#### (d) Two equations of motion free of the reaction

> [!derivation] Projections on the two tangent vectors
> **Law:** Newton's second law in a non-inertial frame projected on $\mathbf e_\zeta$ and $\mathbf e_\beta$, which are normal to the reaction
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.11; [Lecture 5, Slide 28]; Problems.pdf, p. 25
>
> Write $a$ for $\ddot\zeta - \zeta\dot\beta^2$ and $b$ for $2\dot\zeta\dot\beta + \zeta\ddot\beta$, the two brackets of the relative acceleration.
>
> $$\begin{aligned}
> \mathbf n\cdot\mathbf e_\zeta &\propto -2\cos^2\beta - 2\sin^2\beta + 2 = 0, \quad \mathbf n\cdot\mathbf e_\beta \propto 2\cos\beta\sin\beta - 2\sin\beta\cos\beta = 0 \quad &\text{(the reaction drops out)} \\
> \mathbf a_1^P\cdot\mathbf e_\zeta &= a\left(\cos^2\beta + 4\sin^2\beta\right) + b\left(-\sin\beta\cos\beta + 4\sin\beta\cos\beta\right) + \ddot\zeta = \ddot\zeta + a\left(1 + 3\sin^2\beta\right) + 3b\sin\beta\cos\beta \quad &\text{(components of part (b))} \\
> \mathbf W\cdot\mathbf e_\zeta &= -mg, \quad \mathbf F_C\cdot\mathbf e_\zeta = m\Omega^2\zeta\left(\cos^2\beta + 4\sin^2\beta\right) = m\Omega^2\zeta\left(1 + 3\sin^2\beta\right) \quad &\text{(weight; centrifugal)} \\
> \mathbf F_{COR}\cdot\mathbf e_\zeta &= 4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\cos\beta - 4m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\sin\beta = 4m\Omega\zeta\dot\beta \quad &\text{(the $\dot\zeta$ terms cancel)} \\
> \mathbf a_1^P\cdot\mathbf e_\beta &= a\left(-\sin\beta\cos\beta + 4\sin\beta\cos\beta\right) + b\left(\sin^2\beta + 4\cos^2\beta\right) = 3a\sin\beta\cos\beta + b\left(1 + 3\cos^2\beta\right) \quad &\text{(components of part (b))} \\
> \mathbf W\cdot\mathbf e_\beta &= 0, \quad \mathbf F_C\cdot\mathbf e_\beta = m\Omega^2\zeta\left(-\cos\beta\sin\beta + 4\sin\beta\cos\beta\right) = 3m\Omega^2\zeta\sin\beta\cos\beta \quad &\text{(weight; centrifugal)} \\
> \mathbf F_{COR}\cdot\mathbf e_\beta &= -4m\Omega\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)\sin\beta - 4m\Omega\left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)\cos\beta = -4m\Omega\dot\zeta \quad &\text{(the $\dot\beta$ terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \ddot\zeta + \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(1 + 3\sin^2\beta\right) + 3\left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\cos\beta\sin\beta = -g + \Omega^2\zeta\left(1 + 3\sin^2\beta\right) + 4\Omega\zeta\dot\beta \cr 3\left(\ddot\zeta - \zeta\dot\beta^2\right)\cos\beta\sin\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(1 + 3\cos^2\beta\right) = 3\Omega^2\zeta\cos\beta\sin\beta - 4\Omega\dot\zeta \end{gathered}}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** two second-order equations for $\zeta$ and $\beta$ alone, with the initial conditions $\zeta$ equal to 1 m, $\beta$ a quarter turn, zero rate of $\zeta$ and minus 1 rad/s for the rate of $\beta$. The Coriolis terms couple them antisymmetrically. The third projection, on $\mathbf n$, would give the reaction.

### Answers and Checks

#### (e) A conservation law: the energy of the relative motion

> [!derivation] Why the energy in S1 is conserved, and its value
> **Law:** power of each force on the relative velocity; potentials of the weight and of the centrifugal force; initial conditions
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Two reasons. First, the forces that do no work in $S_1$: the reaction (the cone is at rest in $S_1$ and the relative velocity is tangent to it), the Coriolis force (normal to the relative velocity), and the origin and Euler forces, which vanish. Second, the forces that work have potentials of the position in $S_1$: the weight, constant in $S_1$ because $\mathbf k_1$ is the fixed vertical, and the centrifugal force, because the rate is constant and the axis fixed. The squared distance to the axis is the sum of the squares of $x_1$ and $y_1$.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= N\,\mathbf n\cdot\left(\dot\zeta\,\mathbf e_\zeta + \zeta\dot\beta\,\mathbf e_\beta\right) = 0, \quad \mathbf F_{COR}\cdot\mathbf v_1^P = 2m\Omega\left(\dot y_1\dot x_1 - \dot x_1\dot y_1\right) = 0 \quad &\text{(no power)} \\
> V_1 &= mgz_1 - \tfrac12 m\Omega^2\left(x_1^2 + y_1^2\right) = mg\zeta - \tfrac12 m\Omega^2\zeta^2\left(\cos^2\beta + 4\sin^2\beta\right) = mg\zeta - \tfrac12 m\Omega^2\zeta^2\left(1 + 3\sin^2\beta\right) \quad &\text{(Eq. 4.14; Slide 30)} \\
> \left|\mathbf v_1^P\right|^2 &= \left(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta\right)^2 + 4\left(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta\right)^2 + \dot\zeta^2 \quad &\text{(components of part (b))} \\
> &= \left(2 + 3\sin^2\beta\right)\dot\zeta^2 + \left(1 + 3\cos^2\beta\right)\zeta^2\dot\beta^2 + 6\zeta\dot\zeta\dot\beta\sin\beta\cos\beta \quad &\text{(squares expanded; cross terms $-2 + 8 = 6$)} \\
> \frac{dE_1^P}{dt} &= \dot\zeta\left(m\,\mathbf a_1^P - \mathbf W - \mathbf F_C\right)\cdot\mathbf e_\zeta + \zeta\dot\beta\left(m\,\mathbf a_1^P - \mathbf W - \mathbf F_C\right)\cdot\mathbf e_\beta = \dot\zeta\left(4m\Omega\zeta\dot\beta\right) + \zeta\dot\beta\left(-4m\Omega\dot\zeta\right) = 0 \quad &\text{(check with the two equations of part (d))} \\
> E_1^P(0) &= \tfrac12 m\left|\mathbf i_1\right|^2 + mg\cdot 1 - \tfrac12 m\Omega^2\cdot 1^2\left(1 + 3\cdot 1\right) = m\left(\tfrac12 + g - 2\Omega^2\right) \quad &\text{(initial data, SI units)}
> \end{aligned}$$
>
> $$\boxed{\frac{m}{2}\left[\left(2 + 3\sin^2\beta\right)\dot\zeta^2 + \left(1 + 3\cos^2\beta\right)\zeta^2\dot\beta^2 + 6\zeta\dot\zeta\dot\beta\sin\beta\cos\beta\right] + mg\zeta - \frac{m}{2}\Omega^2\zeta^2\left(1 + 3\sin^2\beta\right) = m\left(\tfrac12 + g - 2\Omega^2\right)}$$
>
> **Units:** $[m\dot\zeta^2] = [mg\zeta] = [m\Omega^2\zeta^2] = [\mathrm{M\,L^2\,T^{-2}}]$; the constant is $m(\tfrac12\ \mathrm{m^2\,s^{-2}} + g\cdot 1\ \mathrm{m} - 2\Omega^2\cdot 1\ \mathrm{m^2})$
> **Meaning:** the energy of the motion relative to the cone is constant. The angular momentum about the axis is not: the section is not circular, so the normal reaction has a moment about the axis (next box).

> [!derivation] Why the angular momentum about the axis is not conserved
> **Law:** moment of the reaction about the vertical axis
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.53
>
> The weight is parallel to the axis; the reaction is the only force with an axial moment. Its component along $\mathbf k_1$ is the first component of the position times the second of the force minus the second times the first.
>
> $$\begin{aligned}
> \left(\mathbf r_1^P\times\mathbf N\right)\cdot\mathbf k_1 &= \frac{N}{\sqrt{5 + 3\cos^2\beta}}\left[\zeta\cos\beta\left(-\sin\beta\right) - 2\zeta\sin\beta\left(-2\cos\beta\right)\right] = \frac{3N\zeta\sin\beta\cos\beta}{\sqrt{5 + 3\cos^2\beta}} \quad &\text{(components of the position and of the normal)}
> \end{aligned}$$
>
> $$\boxed{M_{O} \cdot\mathbf k_1 = \frac{3N\zeta\sin\beta\cos\beta}{\sqrt{5 + 3\cos^2\beta}} \ne 0 \text{ in general}}$$
>
> **Units:** $[N\zeta] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** only on the principal planes of the cone, where the product of the sine and cosine vanishes, does the reaction pass through the axis; on a circular cone it always would.

#### (f) Equilibrium positions in S1 for positive zeta

> [!derivation] Equilibria and the reaction there
> **Law:** relative equilibrium: constant coordinates, so the rates and accelerations vanish in the two equations of part (d)
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 25
>
> $$\begin{aligned}
> \mathbf e_\beta:\ 0 &= 3\Omega^2\zeta\cos\beta\sin\beta = \tfrac32\Omega^2\zeta\sin 2\beta \;\Rightarrow\; \beta = 0,\ \tfrac{\pi}{2},\ \pi,\ \tfrac{3\pi}{2} \quad &\text{($\zeta \gt 0$, $\Omega \ne 0$)} \\
> \mathbf e_\zeta:\ 0 &= -g + \Omega^2\zeta\left(1 + 3\sin^2\beta\right) \;\Rightarrow\; \zeta_{eq} = \frac{g}{\Omega^2\left(1 + 3\sin^2\beta\right)} \quad &\text{(second equation)} \\
> \beta = 0, \pi:\quad \zeta_{eq} &= \frac{g}{\Omega^2}; \quad \beta = \tfrac{\pi}{2}, \tfrac{3\pi}{2}:\quad \zeta_{eq} = \frac{g}{4\Omega^2} \quad &\text{($\sin^2\beta$ equal to 0 or 1)} \\
> \beta = 0:\quad \mathbf 0 &= -mg\,\mathbf k_1 + m\Omega^2\zeta\,\mathbf i_1 + \frac{N}{\sqrt8}\left(-2\,\mathbf i_1 + 2\,\mathbf k_1\right) \;\Rightarrow\; N = \sqrt2\,mg \gt 0 \quad &\text{(check by the full balance, $\mathbf k_1$ component)} \\
> \beta = \tfrac{\pi}{2}:\quad \mathbf 0 &= -mg\,\mathbf k_1 + 2m\Omega^2\zeta\,\mathbf j_1 + \frac{N}{\sqrt5}\left(-\mathbf j_1 + 2\,\mathbf k_1\right) \;\Rightarrow\; N = \tfrac{\sqrt5}{2}mg \gt 0, \ \zeta = \frac{g}{4\Omega^2} \quad &\text{(check by the full balance)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = \frac{g}{\Omega^2}\left(\pm\mathbf i_1 + \mathbf k_1\right) \ \ (\beta = 0, \pi), \qquad \mathbf r_1^P = \pm\frac{g}{2\Omega^2}\,\mathbf j_1 + \frac{g}{4\Omega^2}\,\mathbf k_1 \ \ \left(\beta = \tfrac{\pi}{2}, \tfrac{3\pi}{2}\right) \end{gathered}}$$
>
> **Units:** $[g/\Omega^2] = [\mathrm{L}]$
> **Meaning:** the four equilibria lie on the generators of the two principal vertical planes, the only places where the normal lies in the vertical plane through the axis and can balance the weight and the horizontal centrifugal force with nothing left along the section. On the steeper generators (45 degrees) the particle sits four times higher than on the flatter ones. The reaction is positive along the inward normal at all four, so a particle on the inner surface stays in contact there.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 2 ($\zeta$, $\beta$); the cone is $x_1^2 + y_1^2/4 - z_1^2 = 0$ |
| (b) Kinematics in $S_1$ | $\mathbf r_1^P = \zeta\cos\beta\,\mathbf i_1 + 2\zeta\sin\beta\,\mathbf j_1 + \zeta\,\mathbf k_1$; $\mathbf v_1^P$, $\mathbf a_1^P$ as boxed in part (b); $\mathbf i_1 = \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0$, $\mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0$, $\mathbf k_1 = \mathbf k_0$ |
| (c) Forces | $-mg\,\mathbf k_1$; $N\,\mathbf n$, $\mathbf n = (-2\cos\beta, -\sin\beta, 2)/\sqrt{5 + 3\cos^2\beta}$; $\mathbf F_C = m\Omega^2\zeta(\cos\beta\,\mathbf i_1 + 2\sin\beta\,\mathbf j_1)$; $\mathbf F_{COR} = 4m\Omega(\dot\zeta\sin\beta + \zeta\dot\beta\cos\beta)\,\mathbf i_1 - 2m\Omega(\dot\zeta\cos\beta - \zeta\dot\beta\sin\beta)\,\mathbf j_1$; origin and Euler forces zero |
| (d) Equations of motion | the two boxed equations of part (d); initial conditions $\zeta(0) = 1$ m, $\beta(0) = \pi/2$, $\dot\zeta(0) = 0$, $\dot\beta(0) = -1$ rad/s |
| (e) Conservation law | energy in $S_1$: $\frac m2[(2 + 3\sin^2\beta)\dot\zeta^2 + (1 + 3\cos^2\beta)\zeta^2\dot\beta^2 + 6\zeta\dot\zeta\dot\beta\sin\beta\cos\beta] + mg\zeta - \frac12 m\Omega^2\zeta^2(1 + 3\sin^2\beta) = m(\frac12 + g - 2\Omega^2)$ (SI units); in general units, with $z_0$ one unit of length and $v_0$ one unit of velocity, the constant is $m(\frac12 v_0^2 + gz_0 - 2\Omega^2z_0^2)$ |
| (f) Equilibria | $\beta = 0, \pi$: $\zeta = g/\Omega^2$; $\beta = \pi/2, 3\pi/2$: $\zeta = g/(4\Omega^2)$ |

**Check against the official key:** Problems.pdf, p. 75 prints the two equations of part (d); they coincide term by term (box below). The key prints nothing for the other parts; the energy is checked against the two equations, and the equilibria by the full force balance in part (f).

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison
> **Source:** Problems.pdf, p. 75
>
> $$\begin{aligned}
> \text{key, } \mathbf e_\zeta:\ \ddot\zeta + \left(\ddot\zeta - \zeta\dot\beta^2\right)\left(1 + 3\sin^2\beta\right) + 3\left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\cos\beta\sin\beta &= -g + \Omega^2\zeta\left(1 + 3\sin^2\beta\right) + 4\Omega\zeta\dot\beta \quad &\text{(first equation of part (d))} \\
> \text{key, } \mathbf e_\beta:\ 3\left(\ddot\zeta - \zeta\dot\beta^2\right)\cos\beta\sin\beta + \left(2\dot\zeta\dot\beta + \zeta\ddot\beta\right)\left(1 + 3\cos^2\beta\right) &= 3\Omega^2\zeta\cos\beta\sin\beta - 4\Omega\dot\zeta \quad &\text{(second equation of part (d))}
> \end{aligned}$$
>
> $$\boxed{\text{both equations coincide with the key}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the signs of the Coriolis terms confirm the sense of rotation read from the figure.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega \to 0:\quad \zeta_{eq} &\to \infty \quad &\text{(a fixed smooth cone with its vertex down has no equilibrium above the vertex)} \\
> \Omega \to 0:\quad E_1^P &\to \tfrac12 m\left|\mathbf v_1^P\right|^2 + mg\zeta \quad &\text{(ordinary energy of a fixed cone)} \\
> \beta = \tfrac{\pi}{2}:\quad \mathbf e_\zeta &= 2\,\mathbf j_1 + \mathbf k_1, \quad \mathbf n = \frac{-\mathbf j_1 + 2\,\mathbf k_1}{\sqrt5}, \quad \mathbf e_\zeta\cdot\mathbf n = \frac{-2 + 2}{\sqrt5} = 0 \quad &\text{(generator of the plane $y_1z_1$)}
> \end{aligned}$$
>
> $$\boxed{\Omega \to 0: \ \text{no equilibrium for positive } \zeta, \text{ and the energy becomes the ordinary one}}$$
>
> **Units:** $[g/\Omega^2] = [\mathrm{L}]$
> **Meaning:** the rotation is what holds the particle up the wall of the cone.

---

## Problem 40: Spring-Coupled Particles on a Vertical Axis and a Revolving Ring

### Reference Frames, Bases and Coordinates

Two heavy particles $P$ and $Q$ of mass $m$ are joined by a spring of stiffness $k$. $P$ slides without friction on the vertical axis of $S_0$; $Q$ slides without friction on a horizontal ring of radius $R$, in the plane of $\mathbf i_0$ and $\mathbf j_0$, whose centre $D$ is at the distance $\ell$ from $O$ and revolves about the vertical at the constant rate $\Omega$ (Problems.pdf, p. 28). The statement asks for the degrees of freedom and the basis of $S_1$, the position, velocity and acceleration of both particles in $S_1$, the forces, the scalar equations of motion in $S_1$, two equations for $\zeta$ and $\phi$ alone, and one first integral. The ring is at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ vertical, up; gravity $-g\,\mathbf k_0$ |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, same origin, $\mathbf k_1 = \mathbf k_0$, $\mathbf j_1$ from $O$ towards $D$; it turns by $\Omega t$ about $\mathbf k_0$, from $\mathbf i_0$ towards $\mathbf j_0$ (figure), and coincides with $S_0$ at $t = 0$ |
| Ring basis at $Q$ | $\{\mathbf e_r, \mathbf e_\phi, \mathbf k_1\}$: $\mathbf e_r$ from $D$ towards $Q$, $\mathbf e_\phi$ tangent to the ring in the sense of growing $\phi$ (deduced below) |
| Coordinates | $\zeta$, height of $P$ on the axis; $\phi$, angle of $DQ$ measured from $\mathbf j_1$ about $\mathbf k_1$ |
| Data | $m$ [kg], $k$ [N m$^{-1}$], $R$ [m], $\ell$ [m], $\Omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$] |
| Unknowns | $\zeta(t)$, $\phi(t)$ and four reaction components $N_1, N_2$ (axis on $P$), $N_3, N_4$ (ring on $Q$) |
| Applied forces | weights $-mg\,\mathbf k_1$; spring between $P$ and $Q$ |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; massless linear spring; smooth bilateral contacts; $\Omega$ constant; the ring is rigidly attached to $S_1$ |
| Readings | (1) The statement gives no natural length; the spring is read as one of zero natural length, force on $P$ equal to $k\,\overrightarrow{PQ}$. With a natural length $L_0$ the factor $k$ becomes $k(1 - L_0/\lvert PQ\rvert)$ in every spring term and the two equations of part (e) couple (box at the end of part (e)). (2) $\phi$ is read from the figure as positive from $\mathbf j_1$ towards $-\mathbf i_1$ (counterclockwise seen from above); this is also the sense in the official ring reaction, which contains $-\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1$. With the opposite sense $\phi$ changes sign everywhere and the equations of part (e) keep their form |

#### (a) Degrees of freedom

> [!derivation] Coordinates minus independent constraints
> **Law:** each holonomic constraint removes one coordinate; the motion of $D$ is prescribed and adds none
> **Source:** Notes.pdf, Eq. 6.3; Problems.pdf, p. 28
>
> In $S_1$ write $(x_1^P, y_1^P, z_1^P)$ and $(x_1^Q, y_1^Q, z_1^Q)$ for the Cartesian coordinates of the two particles.
>
> $$\begin{aligned}
> P:&\quad x_1^P = 0, \quad y_1^P = 0 \quad &\text{(on the vertical axis: two constraints)} \\
> Q:&\quad z_1^Q = 0, \quad \left(x_1^Q\right)^2 + \left(y_1^Q - \ell\right)^2 - R^2 = 0 \quad &\text{(horizontal plane and ring: two constraints)} \\
> \text{degrees of freedom} &= 3 + 3 - 4 = 2 \quad &\text{(six coordinates, four constraints)}
> \end{aligned}$$
>
> $$\boxed{\text{2 degrees of freedom: } \zeta,\ \phi}$$
>
> **Units:** $[\zeta] = [\mathrm L]$, $[\phi] = [1]$
> **Meaning:** one coordinate per particle; the four constraints become the four reaction components.

### Change of Basis and Position Vector

![[attachments/EM-SOL/p40-top-view.svg]]

> [!derivation] Basis of S1: rotation by Omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page. The figure measures $\Omega t$ from $\mathbf i_0$ towards $\mathbf j_0$, so $S_1$ turns counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ along plus $\mathbf j_0$. $\mathbf j_1$, the direction of $D$, is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\Omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \left(-\sin\Omega t\right)\sin\Omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \cr \sin\Omega t & \cos\Omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Omega t] = [1]$
> **Meaning:** these are the vectors of $\mathcal B_1$ in terms of $\mathcal B_0$, as part (a) asks; the third row and column hold the fixed vertical.

![[attachments/EM-SOL/p40-ring.svg]]

> [!derivation] Position of Q: through the centre D of the ring
> **Law:** vector sum of positions; right triangle $DFQ$; standard polar angle
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 28
>
> The plane of the ring is seen from above ($\mathbf k_1$ out of the paper, ⊙), with $\mathbf i_1$ to the right and $\mathbf j_1$ up, towards $D$. The distance that stays constant is $DQ$, so the path goes from $O$ to $D$ and then to $Q$. Let $F$ be the foot of the perpendicular from $Q$ to the line through $D$ along $\mathbf j_1$. In the shaded right triangle $DFQ$ (right angle at $F$) the hypotenuse is $DQ$, of length $R$; the leg adjacent to $\phi$ is $DF$, of length $R\cos\phi$, along plus $\mathbf j_1$; the opposite leg is $FQ$, of length $R\sin\phi$, along minus $\mathbf i_1$, because a counterclockwise turn from $\mathbf j_1$ carries the point to the left.
>
> $$\begin{aligned}
> \overrightarrow{OD} &= \ell\,\mathbf j_1, \quad \overrightarrow{DQ} = \overrightarrow{DF} + \overrightarrow{FQ} = R\cos\phi\,\mathbf j_1 - R\sin\phi\,\mathbf i_1 \quad &\text{(triangle $DFQ$)} \\
> \mathbf e_r &= \frac{\overrightarrow{DQ}}{R} = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1 \quad &\text{(unit vector from $D$ to $Q$)} \\
> \mathbf r_1^Q &= \overrightarrow{OD} + \overrightarrow{DQ} = -R\sin\phi\,\mathbf i_1 + \left(\ell + R\cos\phi\right)\mathbf j_1 \quad &\text{(Eq. 3.16 with the common origin $O$)} \\
> \cos\left(\phi + \tfrac{\pi}{2}\right) &= \cos\phi\cdot 0 - \sin\phi\cdot 1 = -\sin\phi, \quad \sin\left(\phi + \tfrac{\pi}{2}\right) = \sin\phi\cdot 0 + \cos\phi\cdot 1 = \cos\phi \quad &\text{(sum formulas)} \\
> \mathbf e_r &= \cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1, \quad \psi = \phi + \tfrac{\pi}{2} \quad &\text{(standard polar angle about $D$, from $\mathbf i_1$)} \\
> \mathbf r_1^P &= \zeta\,\mathbf k_1 \quad &\text{($P$ on the axis at the height $\zeta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = \zeta\,\mathbf k_1, \qquad \mathbf r_1^Q = \ell\,\mathbf j_1 + R\,\mathbf e_r = -R\sin\phi\,\mathbf i_1 + \left(\ell + R\cos\phi\right)\mathbf j_1}$$
>
> **Units:** $[\ell] = [R] = [\zeta] = [\mathrm L]$
> **Meaning:** $\phi$ is the polar angle about $D$ counted from the direction $OD$; at zero $Q$ is the point of the ring farthest from the axis, at a half turn the nearest.

> [!derivation] Ring basis and its derivatives
> **Law:** tangent vector as the derivative of the radial unit vector; handedness by the vector product
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.5
>
> The determinant is expanded along its first row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf e_\phi &= \frac{d\mathbf e_r}{d\phi} = -\cos\phi\,\mathbf i_1 - \sin\phi\,\mathbf j_1 \quad &\text{($\tfrac{d}{d\phi}(-\sin\phi) = -\cos\phi$, $\tfrac{d}{d\phi}\cos\phi = -\sin\phi$)} \\
> \mathbf e_r\cdot\mathbf e_\phi &= \sin\phi\cos\phi - \cos\phi\sin\phi = 0, \quad \left|\mathbf e_\phi\right|^2 = \cos^2\phi + \sin^2\phi = 1 \quad &\text{(orthonormal)} \\
> \mathbf e_r\times\mathbf e_\phi &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr -\sin\phi & \cos\phi & 0 \cr -\cos\phi & -\sin\phi & 0 \end{vmatrix} = (+1)(0)\,\mathbf i_1 + (-1)(0)\,\mathbf j_1 + (+1)\left(\sin^2\phi + \cos^2\phi\right)\mathbf k_1 = \mathbf k_1 \quad &\text{(first row; cofactor signs)} \\
> \mathbf j_1 &= \left(\mathbf j_1\cdot\mathbf e_r\right)\mathbf e_r + \left(\mathbf j_1\cdot\mathbf e_\phi\right)\mathbf e_\phi = \cos\phi\,\mathbf e_r - \sin\phi\,\mathbf e_\phi \quad &\text{(projections)} \\
> \mathbf i_1 &= \left(\mathbf i_1\cdot\mathbf e_r\right)\mathbf e_r + \left(\mathbf i_1\cdot\mathbf e_\phi\right)\mathbf e_\phi = -\sin\phi\,\mathbf e_r - \cos\phi\,\mathbf e_\phi \quad &\text{(projections)} \\
> \left.\frac{d\mathbf e_r}{dt}\right|_1 &= \frac{d\mathbf e_r}{d\phi}\,\frac{d\phi}{dt} = \dot\phi\,\mathbf e_\phi, \quad \left.\frac{d\mathbf e_\phi}{dt}\right|_1 = \frac{d\mathbf e_\phi}{d\phi}\,\frac{d\phi}{dt} = \dot\phi\left(\sin\phi\,\mathbf i_1 - \cos\phi\,\mathbf j_1\right) = -\dot\phi\,\mathbf e_r \quad &\text{(chain rule; $\mathbf i_1$, $\mathbf j_1$ constant in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_\phi = -\cos\phi\,\mathbf i_1 - \sin\phi\,\mathbf j_1, \quad \mathbf e_r\times\mathbf e_\phi = \mathbf k_1, \quad \left.\frac{d\mathbf e_r}{dt}\right|_1 = \dot\phi\,\mathbf e_\phi, \quad \left.\frac{d\mathbf e_\phi}{dt}\right|_1 = -\dot\phi\,\mathbf e_r}$$
>
> **Units:** $[\mathbf e_r] = [\mathbf e_\phi] = [1]$; $[\dot\phi] = [\mathrm T^{-1}]$
> **Meaning:** $\{\mathbf e_r, \mathbf e_\phi, \mathbf k_1\}$ is a right-handed orthonormal basis attached to $Q$; $\mathbf e_\phi$ is the only direction in which the ring lets $Q$ move.

### Kinematics

> [!derivation] Motion of S1 and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed vertical; $\Omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf k_1\times\mathbf i_1 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \Omega\,\mathbf k_1\times\mathbf j_1 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(-\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0\right) &= -\Omega\cos\Omega t\,\mathbf i_0 - \Omega\sin\Omega t\,\mathbf j_0 = -\Omega\,\mathbf i_1 \quad &\text{(check: chain rule on $\mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\Omega] = [\mathrm T^{-1}]$
> **Meaning:** in $S_1$ the three unit vectors are constant; in $S_0$ the two horizontal ones turn with the ring.

#### (b) Position, velocity and acceleration of P and Q in S1

> [!derivation] Relative kinematics of both particles
> **Law:** time derivatives in $S_1$; product rule and the derivatives of the ring basis
> **Source:** Notes.pdf, Eq. 3.16; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 28
>
> $\overrightarrow{OD}$ is constant in $S_1$, so only $R\,\mathbf e_r$ changes for $Q$.
>
> $$\begin{aligned}
> \mathbf v_1^P &= \left.\frac{d}{dt}\left(\zeta\,\mathbf k_1\right)\right|_1 = \dot\zeta\,\mathbf k_1, \quad \mathbf a_1^P = \ddot\zeta\,\mathbf k_1 \quad &\text{($\mathbf k_1$ constant in $S_1$)} \\
> \mathbf v_1^Q &= \left.\frac{d}{dt}\left(\ell\,\mathbf j_1 + R\,\mathbf e_r\right)\right|_1 = R\dot\phi\,\mathbf e_\phi \quad &\text{(derivative of $\mathbf e_r$)} \\
> &= -R\dot\phi\cos\phi\,\mathbf i_1 - R\dot\phi\sin\phi\,\mathbf j_1 \quad &\text{($\mathbf e_\phi$ in $\mathcal B_1$)} \\
> \mathbf a_1^Q &= R\ddot\phi\,\mathbf e_\phi + R\dot\phi\left.\frac{d\mathbf e_\phi}{dt}\right|_1 = R\ddot\phi\,\mathbf e_\phi - R\dot\phi^2\,\mathbf e_r \quad &\text{(product rule; derivative of $\mathbf e_\phi$)} \\
> &= \left(-R\ddot\phi\cos\phi + R\dot\phi^2\sin\phi\right)\mathbf i_1 - \left(R\ddot\phi\sin\phi + R\dot\phi^2\cos\phi\right)\mathbf j_1 \quad &\text{($\mathbf e_r$, $\mathbf e_\phi$ in $\mathcal B_1$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = \zeta\,\mathbf k_1, \quad \mathbf v_1^P = \dot\zeta\,\mathbf k_1, \quad \mathbf a_1^P = \ddot\zeta\,\mathbf k_1, \cr \mathbf r_1^Q = \ell\,\mathbf j_1 + R\,\mathbf e_r, \quad \mathbf v_1^Q = R\dot\phi\,\mathbf e_\phi, \quad \mathbf a_1^Q = R\ddot\phi\,\mathbf e_\phi - R\dot\phi^2\,\mathbf e_r \end{gathered}}$$
>
> **Units:** $[\dot\zeta] = [R\dot\phi] = [\mathrm{L\,T^{-1}}]$; $[\ddot\zeta] = [R\ddot\phi] = [R\dot\phi^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $P$ moves on a straight line and $Q$ on a circle of radius $R$, with tangential and centripetal parts about $D$.

> [!derivation] Absolute acceleration: transport and Coriolis terms as they arise
> **Law:** time derivative in $S_0$ of a position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position of a point in the plane of the ring as $x_1\,\mathbf i_1 + y_1\,\mathbf j_1$ (for $Q$, the components of $\mathbf r_1^Q$); the time derivatives of the components are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0 &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + x_1\Omega\,\mathbf j_1 - y_1\Omega\,\mathbf i_1 = \mathbf v_1 + \Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1}{dt}\right|_0 &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) = \mathbf a_1 + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(product rule; the basis turns inside $\mathbf v_1$)} \\
> \left.\frac{d}{dt}\right|_0\left[\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right)\right] &= \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(product rule; $\Omega$ constant)} \\
> \mathbf a_0 &= \mathbf a_1 + 2\Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(the two equal terms add: Coriolis; the last: centripetal)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^Q &= 2\Omega\,\mathbf k_1\times R\dot\phi\,\mathbf e_\phi = 2\Omega R\dot\phi\left(-\cos\phi\,\mathbf j_1 + \sin\phi\,\mathbf i_1\right) = -2\Omega R\dot\phi\,\mathbf e_r \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> -\Omega^2\,\mathbf r_1^Q &= -\Omega^2\left(\ell\,\mathbf j_1 + R\,\mathbf e_r\right) = -\Omega^2\left(\ell\cos\phi + R\right)\mathbf e_r + \Omega^2\ell\sin\phi\,\mathbf e_\phi \quad &\text{($\mathbf j_1$ in the ring basis)} \\
> \mathbf a_0^P &= \left.\frac{d^2}{dt^2}\left(\zeta\,\mathbf k_1\right)\right|_0 = \ddot\zeta\,\mathbf k_1 \quad &\text{($\mathbf k_1$ does not turn)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^Q = \left(-R\dot\phi^2 - 2\Omega R\dot\phi - \Omega^2\left(\ell\cos\phi + R\right)\right)\mathbf e_r + \left(R\ddot\phi + \Omega^2\ell\sin\phi\right)\mathbf e_\phi, \qquad \mathbf a_0^P = \ddot\zeta\,\mathbf k_1}$$
>
> **Units:** $[\Omega R\dot\phi] = [\Omega^2\ell] = [R\dot\phi^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the Coriolis term collects two equal halves, one from the turning of the basis inside the relative velocity and one from the change of the transport velocity; $P$, on the axis, has neither a transport nor a Coriolis term.

### Forces and Equations of Motion

![[attachments/EM-SOL/p40-fbd.svg]]

#### (c) Forces acting on P and Q

> [!derivation] Actual and inertia forces on both particles
> **Law:** weight; smooth reactions normal to the allowed motion; linear spring; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.11; [Lecture 5, Slide 28]; Problems.pdf, p. 28
>
> The axis lets $P$ move only along $\mathbf k_1$, so its smooth reaction has no $\mathbf k_1$ component; the ring lets $Q$ move only along $\mathbf e_\phi$, so its reaction has no $\mathbf e_\phi$ component. The spring vector is $\overrightarrow{PQ}$, the difference of the two positions.
>
> $$\begin{aligned}
> \overrightarrow{PQ} &= \mathbf r_1^Q - \mathbf r_1^P = -R\sin\phi\,\mathbf i_1 + \left(\ell + R\cos\phi\right)\mathbf j_1 - \zeta\,\mathbf k_1 \quad &\text{(positions of part (b))} \\
> \mathbf F_s^P &= k\,\overrightarrow{PQ}, \quad \mathbf F_s^Q = -k\,\overrightarrow{PQ} = -k\left(\ell\cos\phi\,\mathbf e_r - \ell\sin\phi\,\mathbf e_\phi + R\,\mathbf e_r\right) + k\zeta\,\mathbf k_1 \quad &\text{(spring of zero natural length; $\mathbf j_1$ in the ring basis)} \\
> \mathbf N_P &= N_1\,\mathbf i_1 + N_2\,\mathbf j_1, \quad \mathbf N_Q = N_3\,\mathbf e_r + N_4\,\mathbf k_1 = N_3\left(-\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1\right) + N_4\,\mathbf k_1 \quad &\text{(smooth axis; smooth ring)} \\
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1 = \mathbf 0 \quad &\text{($O$ fixed; $\Omega$ constant)} \\
> \boldsymbol\omega_{10}\times\mathbf r_1^P &= \Omega\zeta\,\mathbf k_1\times\mathbf k_1 = \mathbf 0, \quad \boldsymbol\omega_{10}\times\mathbf v_1^P = \Omega\dot\zeta\,\mathbf k_1\times\mathbf k_1 = \mathbf 0 \quad &\text{($P$ on the axis: no centrifugal, no Coriolis force)} \\
> \mathbf F_C^Q &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^Q\right) = m\Omega^2\,\mathbf r_1^Q = m\Omega^2\left(\ell\cos\phi + R\right)\mathbf e_r - m\Omega^2\ell\sin\phi\,\mathbf e_\phi \quad &\text{(centripetal term of the composition box times $-m$)} \\
> \mathbf F_{COR}^Q &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^Q = 2m\Omega R\dot\phi\,\mathbf e_r \quad &\text{(Coriolis term of the composition box times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} P:\ -mg\,\mathbf k_1, \quad N_1\,\mathbf i_1 + N_2\,\mathbf j_1, \quad k\left[-R\sin\phi\,\mathbf i_1 + \left(\ell + R\cos\phi\right)\mathbf j_1 - \zeta\,\mathbf k_1\right], \quad \text{no inertia force} \cr Q:\ -mg\,\mathbf k_1, \quad N_3\,\mathbf e_r + N_4\,\mathbf k_1, \quad -k\left(\ell\cos\phi + R\right)\mathbf e_r + k\ell\sin\phi\,\mathbf e_\phi + k\zeta\,\mathbf k_1, \cr \mathbf F_C^Q = m\Omega^2\left(\ell\cos\phi + R\right)\mathbf e_r - m\Omega^2\ell\sin\phi\,\mathbf e_\phi, \quad \mathbf F_{COR}^Q = 2m\Omega R\dot\phi\,\mathbf e_r \end{gathered}}$$
>
> **Units:** $[mg] = [kR] = [m\Omega^2\ell] = [m\Omega R\dot\phi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the spring pulls $Q$ towards $P$; the centrifugal force pushes $Q$ away from the axis, horizontally; the Coriolis force on $Q$ is radial in the ring and only loads the ring.

#### (d) Scalar equations of motion in S1

> [!derivation] Newton's second law in S1 projected on the bases of the constraints
> **Law:** $m\,\mathbf a_1 = \mathbf F + \mathbf F_i$ for each particle, projected on $\mathcal B_1$ for $P$ and on the ring basis for $Q$
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; Problems.pdf, p. 28
>
> $$\begin{aligned}
> P,\ \mathbf i_1:&\quad 0 = N_1 - kR\sin\phi \quad &\text{($\mathbf a_1^P$ has no $\mathbf i_1$ part)} \\
> P,\ \mathbf j_1:&\quad 0 = N_2 + k\left(\ell + R\cos\phi\right) \quad &\text{($\mathbf a_1^P$ has no $\mathbf j_1$ part)} \\
> P,\ \mathbf k_1:&\quad m\ddot\zeta = -mg - k\zeta \quad &\text{(weight and spring)} \\
> Q,\ \mathbf e_r:&\quad -mR\dot\phi^2 = N_3 - k\left(\ell\cos\phi + R\right) + m\Omega^2\left(\ell\cos\phi + R\right) + 2m\Omega R\dot\phi \quad &\text{(reaction, spring, centrifugal, Coriolis)} \\
> Q,\ \mathbf e_\phi:&\quad mR\ddot\phi = k\ell\sin\phi - m\Omega^2\ell\sin\phi \quad &\text{(spring and centrifugal)} \\
> Q,\ \mathbf k_1:&\quad 0 = -mg + N_4 + k\zeta \quad &\text{(weight, reaction, spring)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} N_1 = kR\sin\phi, \quad N_2 = -k\left(\ell + R\cos\phi\right), \quad m\ddot\zeta = -mg - k\zeta, \cr -mR\dot\phi^2 = N_3 + \left(m\Omega^2 - k\right)\left(\ell\cos\phi + R\right) + 2m\Omega R\dot\phi, \quad mR\ddot\phi = \left(k - m\Omega^2\right)\ell\sin\phi, \quad N_4 = mg - k\zeta \end{gathered}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** six scalar equations for six unknowns, the two coordinates and the four reaction components.

#### (e) Two equations free of the other unknowns

> [!derivation] Projections along the allowed motions
> **Law:** the projections on $\mathbf k_1$ for $P$ and on $\mathbf e_\phi$ for $Q$ are normal to the reactions
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 28
>
> $$\begin{aligned}
> \ddot\zeta &= -g - \frac{k}{m}\,\zeta \quad &\text{($\mathbf k_1$ equation of $P$ divided by $m$)} \\
> \ddot\phi &= \frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)\sin\phi \quad &\text{($\mathbf e_\phi$ equation of $Q$ divided by $mR$)} \\
> N_3 &= -mR\dot\phi^2 + \left(k - m\Omega^2\right)\left(\ell\cos\phi + R\right) - 2m\Omega R\dot\phi \quad &\text{($\mathbf e_r$ equation of $Q$ solved for $N_3$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\zeta + \frac{k}{m}\,\zeta = -g, \qquad \ddot\phi = \frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)\sin\phi}$$
>
> **Units:** $[k/m] = [\Omega^2] = [\mathrm T^{-2}]$; $[(k/m)\zeta] = [g] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the two equations are decoupled: the spring force is linear in $\overrightarrow{PQ}$, its vertical part acts only on the motion of $P$ along the axis and its horizontal part only on the motion of $Q$ in the horizontal plane. Once $\zeta$ and $\phi$ are known, the other four equations of part (d) give the reactions.

> [!derivation] Reading with a natural length L0 (alternative)
> **Law:** spring force proportional to the stretch, along $\overrightarrow{PQ}$
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 28
>
> With a natural length $L_0$ the force on $P$ is $k\left(|PQ| - L_0\right)$ times the unit vector of $\overrightarrow{PQ}$, so every spring term above gains the factor $1 - L_0/|PQ|$, with the squared length written out below.
>
> $$\begin{aligned}
> |PQ|^2 &= R^2\sin^2\phi + \left(\ell + R\cos\phi\right)^2 + \zeta^2 = \ell^2 + R^2 + 2\ell R\cos\phi + \zeta^2 \quad &\text{(components of $\overrightarrow{PQ}$)} \\
> \ddot\zeta &= -g - \frac{k}{m}\left(1 - \frac{L_0}{|PQ|}\right)\zeta, \quad \ddot\phi = \frac{\ell}{R}\left[\frac{k}{m}\left(1 - \frac{L_0}{|PQ|}\right) - \Omega^2\right]\sin\phi \quad &\text{(same projections)}
> \end{aligned}$$
>
> $$\boxed{L_0 \ne 0: \ \text{the two equations couple through } |PQ| = \sqrt{\ell^2 + R^2 + 2\ell R\cos\phi + \zeta^2}}$$
>
> **Units:** $[L_0/|PQ|] = [1]$
> **Meaning:** only the zero natural length makes the problem separate; the forms of the reactions do not change.

### Answers and Checks

#### (f) A conservation law in S1

> [!derivation] Energy of the relative motion
> **Law:** power of each force on the relative velocity; potentials of the weight, the spring and the centrifugal force
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Two reasons. First, the forces that do no work in $S_1$: the reactions (the axis and the ring are at rest in $S_1$ and smooth, so each reaction is normal to the relative velocity of its particle), the Coriolis force on $Q$ (normal to its relative velocity; the one on $P$ is zero), and the origin and Euler forces, which vanish. Second, the forces that work have potentials of the positions in $S_1$: the weights, constant in $S_1$ because $\mathbf k_1$ is the fixed vertical; the spring, which depends only on $\overrightarrow{PQ}$; and the centrifugal force on $Q$, because the rate is constant and the axis fixed. $Q$ moves in the plane through $O$ normal to the axis, so its distance to the axis is the length of $\mathbf r_1^Q$.
>
> $$\begin{aligned}
> \mathbf N_P\cdot\mathbf v_1^P &= \left(N_1\,\mathbf i_1 + N_2\,\mathbf j_1\right)\cdot\dot\zeta\,\mathbf k_1 = 0, \quad \mathbf N_Q\cdot\mathbf v_1^Q = \left(N_3\,\mathbf e_r + N_4\,\mathbf k_1\right)\cdot R\dot\phi\,\mathbf e_\phi = 0, \quad \mathbf F_{COR}^Q\cdot\mathbf v_1^Q = 2m\Omega R^2\dot\phi^2\,\mathbf e_r\cdot\mathbf e_\phi = 0 \quad &\text{(no power)} \\
> V_1 &= mg\zeta + mg\cdot 0 + \tfrac12 k\,|PQ|^2 - \tfrac12 m\Omega^2\left|\mathbf r_1^Q\right|^2 \quad &\text{(Eq. 4.14; Slide 30)} \\
> \left|\mathbf r_1^Q\right|^2 &= R^2\sin^2\phi + \left(\ell + R\cos\phi\right)^2 = \ell^2 + R^2 + 2\ell R\cos\phi \quad &\text{(components of part (b))} \\
> V_1 &= mg\zeta + \tfrac12 k\zeta^2 + \left(k - m\Omega^2\right)\ell R\cos\phi + \tfrac12\left(k - m\Omega^2\right)\left(\ell^2 + R^2\right) \quad &\text{(with $|PQ|^2$ of the previous box, $L_0$ zero)} \\
> T_1 &= \tfrac12 m\left|\mathbf v_1^P\right|^2 + \tfrac12 m\left|\mathbf v_1^Q\right|^2 = \tfrac12 m\left(\dot\zeta^2 + R^2\dot\phi^2\right) \quad &\text{(velocities of part (b))} \\
> \frac{d}{dt}\left(T_1 + V_1\right) &= m\dot\zeta\ddot\zeta + mR^2\dot\phi\ddot\phi + mg\dot\zeta + k\zeta\dot\zeta - \left(k - m\Omega^2\right)\ell R\sin\phi\,\dot\phi \quad &\text{(chain rule: $\tfrac{d}{dt}\cos\phi = -\sin\phi\,\dot\phi$, $\tfrac{d}{dt}\zeta^2 = 2\zeta\dot\zeta$)} \\
> &= m\dot\zeta\left(\ddot\zeta + g + \frac{k}{m}\zeta\right) + mR\dot\phi\left(R\ddot\phi - \left(\frac{k}{m} - \Omega^2\right)\ell\sin\phi\right) = 0 \quad &\text{(check with the two equations of part (e))}
> \end{aligned}$$
>
> $$\boxed{E_1 = \frac12 m\left(\dot\zeta^2 + R^2\dot\phi^2\right) + mg\zeta + \frac12 k\zeta^2 + \left(k - m\Omega^2\right)\ell R\cos\phi = \text{const}}$$
>
> **Units:** $[m\dot\zeta^2] = [mg\zeta] = [k\zeta^2] = [k\ell R] = [m\Omega^2\ell R] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy in $S_1$ is a first integral; the constant term of the potential is dropped and the constant is fixed by initial conditions, which the statement does not give. Since each bracket of the check vanishes on its own, the two parts, the one in $\zeta$ and the one in $\phi$, are also conserved separately.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom; basis $\mathcal B_1$ | 2 ($\zeta$, $\phi$); $\mathbf i_1 = \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0$, $\mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0$, $\mathbf k_1 = \mathbf k_0$ |
| (b) Kinematics in $S_1$ | $\mathbf r_1^P = \zeta\,\mathbf k_1$, $\mathbf v_1^P = \dot\zeta\,\mathbf k_1$, $\mathbf a_1^P = \ddot\zeta\,\mathbf k_1$; $\mathbf r_1^Q = -R\sin\phi\,\mathbf i_1 + (\ell + R\cos\phi)\,\mathbf j_1$, $\mathbf v_1^Q = R\dot\phi\,\mathbf e_\phi$, $\mathbf a_1^Q = R\ddot\phi\,\mathbf e_\phi - R\dot\phi^2\,\mathbf e_r$, with $\mathbf e_r = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1$, $\mathbf e_\phi = -\cos\phi\,\mathbf i_1 - \sin\phi\,\mathbf j_1$ |
| (c) Forces | on $P$: $-mg\,\mathbf k_1$, $N_1\mathbf i_1 + N_2\mathbf j_1$, $k\,\overrightarrow{PQ}$, no inertia force; on $Q$: $-mg\,\mathbf k_1$, $N_3\,\mathbf e_r + N_4\,\mathbf k_1$, $-k\,\overrightarrow{PQ}$, $\mathbf F_C^Q = m\Omega^2\mathbf r_1^Q$, $\mathbf F_{COR}^Q = 2m\Omega R\dot\phi\,\mathbf e_r$; origin and Euler forces zero |
| (d) Scalar equations | $0 = N_1 - kR\sin\phi$; $0 = N_2 + k(\ell + R\cos\phi)$; $m\ddot\zeta = -mg - k\zeta$; $-mR\dot\phi^2 = N_3 + (m\Omega^2 - k)(\ell\cos\phi + R) + 2m\Omega R\dot\phi$; $mR\ddot\phi = (k - m\Omega^2)\ell\sin\phi$; $0 = N_4 - mg + k\zeta$ |
| (e) Two equations | $\ddot\zeta + (k/m)\zeta = -g$; $\ddot\phi = (\ell/R)(k/m - \Omega^2)\sin\phi$ (spring of zero natural length; with a natural length $L_0$ the factor $k$ becomes $k(1 - L_0/\lvert PQ\rvert)$ and they couple) |
| (f) First integral | $\frac12 m(\dot\zeta^2 + R^2\dot\phi^2) + mg\zeta + \frac12 k\zeta^2 + (k - m\Omega^2)\ell R\cos\phi = \text{const}$ (energy in $S_1$) |

**Check against the official key:** Problems.pdf, p. 76 prints only the reaction of the ring on $Q$, $N_3(-\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1) + N_4\,\mathbf k_1$; it coincides with the reaction of part (c), whose radial vector is the $\mathbf e_r$ of the position box. The other parts have no key; the energy is checked against the two equations in part (f), and the limiting cases follow.

> [!derivation] Limiting cases and equilibria
> **Law:** the equations of part (e) at extreme values of the data; Taylor expansion about an equilibrium and the harmonic oscillator
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \zeta_{eq} &= -\frac{mg}{k}, \quad \ddot\zeta + \frac{k}{m}\left(\zeta - \zeta_{eq}\right) = 0 \quad &\text{($P$: harmonic oscillator about $\zeta_{eq}$, frequency $\sqrt{k/m}$, Eq. 5.6)} \\
> \phi &= \pi + \varepsilon:\quad \sin\left(\pi + \varepsilon\right) = -\sin\varepsilon \approx -\varepsilon \;\Rightarrow\; \ddot\varepsilon + \frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)\varepsilon = 0 \quad &\text{(first-order Taylor expansion about the near point)} \\
> \phi &= \varepsilon:\quad \sin\varepsilon \approx \varepsilon \;\Rightarrow\; \ddot\varepsilon - \frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)\varepsilon = 0 \quad &\text{(first-order Taylor expansion about the far point)} \\
> \ell &\to 0:\quad \ddot\phi = 0 \quad &\text{(ring centred on the axis: every point at the same distance)} \\
> \Omega^2 &= \frac{k}{m}:\quad \ddot\phi = 0 \quad &\text{(spring and centrifugal forces cancel along the ring)}
> \end{aligned}$$
>
> $$\boxed{\Omega^2 \lt \frac{k}{m}: \ \phi = \pi \text{ oscillates with frequency } \sqrt{\frac{\ell}{R}\left(\frac{k}{m} - \Omega^2\right)}; \qquad \Omega^2 \gt \frac{k}{m}: \ \phi = 0 \text{ does}}$$
>
> **Units:** $[(\ell/R)(k/m - \Omega^2)] = [\mathrm T^{-2}]$; $[mg/k] = [\mathrm L]$
> **Meaning:** $P$ oscillates about the point below $O$ where the vertical pull of the spring balances its weight, unaffected by the rotation because it sits on the axis. For $Q$ the spring pulls towards the point of the ring nearest the axis and the centrifugal force pushes towards the farthest one: below the rate whose square is $k/m$ the near point is where small oscillations occur, above it the far one; the other point gives exponential departure.

---

## Problem 41: Satellite Solar Panel (Composition of Rotations)

### Reference Frames, Bases and Coordinates

A satellite spins about its $z$ axis at the constant rate $\omega$; its solar panel turns about the body-fixed $x$ axis through the angle $\theta$, an arbitrary function of time. The statement asks for the absolute velocity and acceleration of the corner $B$ of the panel with respect to an inertial frame centred at $A$ (Problems.pdf, p. 29). There are no forces: the problem is kinematics only, solved with the composition of motions of Notes.pdf, Sec. 3.2, and checked by a second route with the composition of angular velocities.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{A;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, centred at the satellite centre $A$, $\mathbf k_0$ along the spin axis |
| Body frame | $S_1 = \{A;\ \mathcal B_1\}$, the axes $x$, $y$, $z$ of the figure; $\mathbf k_1 = \mathbf k_0$; turns by $\omega t$ about $\mathbf k_0$, from $\mathbf i_0$ towards $\mathbf j_0$; coincides with $S_0$ at $t = 0$ |
| Panel frame | $S_2 = \{C;\ \mathcal B_2\}$, attached to the panel; $C$ is the point of the hinge axis at the abscissa of $B$; $\mathbf i_2 = \mathbf i_1$ (hinge), $\mathbf j_2$ from $C$ towards $B$ |
| Points | $A$ centre of the satellite; $C$ on the $x$ axis at the distance $H$ from $A$; $B$ the corner of the panel; $B'$ the projection of $B$ on the plane $xy$ |
| Data | $H$ [m] (distance from $A$ to $C$ along $x$), $W$ [m] (distance from $B$ to the hinge axis), $\omega$ [rad s$^{-1}$], $\theta(t)$ [rad] with its derivatives |
| Unknowns | $\mathbf v_0^B$, $\mathbf a_0^B$ |
| Hypotheses | $S_0$ inertial with $A$ fixed in it; rigid body and panel; $\omega$ constant; $\theta(t)$ known |
| Readings | (1) Read from the figure: $\theta$ is the angle of the panel about $+x$, measured from the body axis $y$, so for zero $\theta$ the segment $CB$ points along $+y$. If $\theta$ were measured from the body axis $z$ instead, the position of $B$ would be the one below with $\theta$ replaced by $\theta + \pi/2$, and so would every result. (2) $H$ is read as measured along $x$ from $A$ to the abscissa of $B$, and $W$ as the distance of $B$ from the $x$ axis |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p41-spin-view.svg]]

> [!derivation] First rotation: the body frame turns by omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from $+z$, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page; a positive spin turns the body counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i_0$, opposite leg $\sin\omega t$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\omega t\cos\omega t - \left(-\sin\omega t\right)\sin\omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\omega t] = [1]$
> **Meaning:** the body axes in terms of the inertial ones; they coincide at the start.

![[attachments/EM-SOL/p41-hinge-view.svg]]

> [!derivation] Second rotation: the panel turns by theta about the hinge i1
> **Law:** elementary rotation about the first axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.20
>
> View along the hinge, with $\mathbf i_1$ out of the paper (⊙). With $\mathbf j_1$ to the right, $\mathbf k_1$, the cross product of $\mathbf i_1$ and $\mathbf j_1$, points up the page. $\theta$ is measured about $+\mathbf i_1$, counterclockwise in this view, from $\mathbf j_1$. $\mathbf j_2$ is $\mathbf j_1$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf j_1$, opposite leg $\sin\theta$ along plus $\mathbf k_1$. $\mathbf k_2$ is $\mathbf k_1$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\theta$ lies along minus $\mathbf j_1$ (the minus sign). The determinant is expanded along the first row.
>
> $$\begin{aligned}
> \mathbf i_2 &= \mathbf i_1, \quad \mathbf j_2 = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1, \quad \mathbf k_2 = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \quad &\text{(axis; the two right triangles)} \\
> \det[{}_1R_2] &= (+1)\cdot 1\cdot\left(\cos\theta\cos\theta - \left(-\sin\theta\right)\sin\theta\right) = 1 \quad &\text{(expansion along the first row, cofactor sign $(-1)^{1+1}$)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{22} &= \cos^2\theta + \sin^2\theta = 1, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{23} = \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(rows times rows)} \\
> \det[{}_0R_2] &= \det[{}_0R_1]\,\det[{}_1R_2] = 1\cdot 1 = 1 \quad &\text{(product of the two rotations, Eq. 1.16)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad [{}_1R_2][{}_1R_2]^T = I}$$
>
> **Units:** $[\theta] = [1]$
> **Meaning:** the panel axes in terms of the body axes; for zero $\theta$ the panel lies in the plane $xy$ of the body.

![[attachments/EM-SOL/p41-body-plane.svg]]

> [!derivation] Position of B: through the hinge point C
> **Law:** vector sum of positions; the right triangle of the hinge view
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 29
>
> The distance that stays constant is the one from the hinge, so the path goes from $A$ along the hinge to $C$ and then across the panel to $B$. In the shaded triangle of the hinge view the hypotenuse is $CB$, of length $W$; the leg adjacent to $\theta$ is $W\cos\theta$ along $\mathbf j_1$ and the opposite leg is $W\sin\theta$ along $\mathbf k_1$. The body-plane figure shows the projection $B'$ of $B$ on the plane $xy$.
>
> $$\begin{aligned}
> \overrightarrow{AC} &= H\,\mathbf i_1, \quad \overrightarrow{CB} = W\,\mathbf j_2 = W\cos\theta\,\mathbf j_1 + W\sin\theta\,\mathbf k_1 \quad &\text{(hinge; second column of $[{}_1R_2]$ times $W$)} \\
> \mathbf r_1^B &= \overrightarrow{AC} + \overrightarrow{CB} = H\,\mathbf i_1 + W\cos\theta\,\mathbf j_1 + W\sin\theta\,\mathbf k_1 \quad &\text{(Eq. 3.16 with the common origin $A$)} \\
> \overrightarrow{AB'} &= H\,\mathbf i_1 + W\cos\theta\,\mathbf j_1 \quad &\text{(part normal to the spin axis: drop the $\mathbf k_1$ component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^B = \mathbf r_1^B = H\,\mathbf i_1 + W\cos\theta\,\mathbf j_1 + W\sin\theta\,\mathbf k_1}$$
>
> **Units:** $[H] = [W] = [\mathrm L]$
> **Meaning:** for zero $\theta$ the corner is at $H$ along $x$ and $W$ along $y$; a quarter turn lifts it to $W$ above the plane $xy$. The vector from the spin axis to $B$ is the one from $A$ to $B'$.

### Kinematics

> [!derivation] Motion of the body frame and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^A = \mathbf a_0^A = \mathbf 0 \quad &\text{(rotation about the fixed axis; $\omega$ constant; $A$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \omega\,\mathbf k_1\times\mathbf i_1 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \omega\,\mathbf k_1\times\mathbf j_1 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) &= -\omega\sin\omega t\,\mathbf i_0 + \omega\cos\omega t\,\mathbf j_0 = \omega\,\mathbf j_1 \quad &\text{(check: chain rule on $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\omega] = [\mathrm T^{-1}]$
> **Meaning:** the body axes $x$ and $y$ turn with the spin; the spin axis does not.

> [!derivation] Relative velocity and acceleration of B in the body frame
> **Law:** time derivatives in $S_1$, where $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ are constant; chain rule and product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24
>
> $$\begin{aligned}
> \frac{d}{dt}\left(W\cos\theta\right) &= -W\sin\theta\,\dot\theta, \quad \frac{d}{dt}\left(W\sin\theta\right) = W\cos\theta\,\dot\theta \quad &\text{(chain rule; $H$ and $W$ constant)} \\
> \mathbf v_1^B &= -W\dot\theta\sin\theta\,\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(Eq. 3.19)} \\
> \frac{d}{dt}\left(\dot\theta\sin\theta\right) &= \ddot\theta\sin\theta + \dot\theta^2\cos\theta, \quad \frac{d}{dt}\left(\dot\theta\cos\theta\right) = \ddot\theta\cos\theta - \dot\theta^2\sin\theta \quad &\text{(product rule, then chain rule)} \\
> \mathbf a_1^B &= -W\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right)\mathbf j_1 + W\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf k_1 \quad &\text{(Eq. 3.24)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^B = W\dot\theta\,\mathbf k_2, \qquad \mathbf a_1^B = W\ddot\theta\,\mathbf k_2 - W\dot\theta^2\,\mathbf j_2}$$
>
> **Units:** $[W\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[W\ddot\theta] = [W\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** seen from the body, $B$ describes a circle of radius $W$ about the hinge, with a tangential part along $\mathbf k_2$ and a centripetal part towards the hinge.

> [!derivation] Absolute velocity and acceleration: transport and Coriolis terms as they arise
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write $\mathbf r_1^B$ as $x_1\,\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1$ with $x_1$ equal to $H$, $y_1$ to $W\cos\theta$ and $z_1$ to $W\sin\theta$; the time derivatives of the components are the components of $\mathbf v_1^B$.
>
> $$\begin{aligned}
> \mathbf v_0^B &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1 + x_1\omega\,\mathbf j_1 - y_1\omega\,\mathbf i_1 = \mathbf v_1^B + \omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> &= -W\omega\cos\theta\,\mathbf i_1 + \left(H\omega - W\dot\theta\sin\theta\right)\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(components substituted)} \\
> \left.\frac{d\mathbf v_1^B}{dt}\right|_0 &= \mathbf a_1^B + \omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(product rule; the basis turns inside $\mathbf v_1^B$)} \\
> \left.\frac{d}{dt}\right|_0\left[\omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right)\right] &= \omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(product rule; $\omega$ constant)} \\
> \mathbf a_0^B &= \mathbf a_1^B + 2\omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(Coriolis: the two equal terms; centripetal: the last)} \\
> 2\omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) &= 2\omega\left(0\cdot\mathbf j_1 + W\dot\theta\sin\theta\,\mathbf i_1\right) = 2W\omega\dot\theta\sin\theta\,\mathbf i_1 \quad &\text{($\dot x_1$ zero, $\dot y_1 = -W\dot\theta\sin\theta$)} \\
> -\omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) &= -H\omega^2\,\mathbf i_1 - W\omega^2\cos\theta\,\mathbf j_1 \quad &\text{(minus $\omega^2$ times $\overrightarrow{AB'}$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf v_0^B = -W\omega\cos\theta\,\mathbf i_1 + \left(H\omega - W\dot\theta\sin\theta\right)\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \cr \mathbf a_0^B = \left(2W\omega\dot\theta\sin\theta - H\omega^2\right)\mathbf i_1 - \left(W\ddot\theta\sin\theta + W\dot\theta^2\cos\theta + W\omega^2\cos\theta\right)\mathbf j_1 + \left(W\ddot\theta\cos\theta - W\dot\theta^2\sin\theta\right)\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[W\omega] = [H\omega] = [W\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[W\omega\dot\theta] = [H\omega^2] = [W\ddot\theta] = [W\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity adds to the relative one the transport velocity of the body point that coincides with $B$; the acceleration adds the centripetal term towards the spin axis and the Coriolis term, the two equal halves coming from the turning basis inside the relative velocity and from the change of the transport velocity. The components are in $\mathcal B_1$; multiplying by $[{}_0R_1]$ gives them in $\mathcal B_0$.

> [!derivation] Second route: panel frame and composition of angular velocities
> **Law:** composition of angular velocities and accelerations; velocity and acceleration of a point fixed in a moving frame
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 3.15; Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 3.27
>
> $B$ is fixed in $S_2$, so its velocity and acceleration relative to $S_2$ vanish; $C$ is fixed in $S_1$ at $H\,\mathbf i_1$. Vector products use $\mathbf i_1\times\mathbf j_1 = \mathbf k_1$, $\mathbf j_1\times\mathbf k_1 = \mathbf i_1$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$ and the reversed products with a minus sign.
>
> $$\begin{aligned}
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\theta\,\mathbf i_1 + \omega\,\mathbf k_1 \quad &\text{(Eq. 3.14)} \\
> \boldsymbol\alpha_{20} &= \boldsymbol\alpha_{21} + \boldsymbol\omega_{10}\times\boldsymbol\omega_{21} + \boldsymbol\alpha_{10} = \ddot\theta\,\mathbf i_1 + \omega\dot\theta\,\mathbf k_1\times\mathbf i_1 + \mathbf 0 = \ddot\theta\,\mathbf i_1 + \omega\dot\theta\,\mathbf j_1 \quad &\text{(Eq. 3.15)} \\
> \mathbf v_0^C &= \omega\,\mathbf k_1\times H\,\mathbf i_1 = H\omega\,\mathbf j_1, \quad \mathbf a_0^C = \omega\,\mathbf k_1\times H\omega\,\mathbf j_1 = -H\omega^2\,\mathbf i_1 \quad &\text{($C$ fixed in $S_1$, Eq. 3.26 and 3.27)} \\
> \boldsymbol\omega_{20}\times\overrightarrow{CB} &= \left(\dot\theta\,\mathbf i_1 + \omega\,\mathbf k_1\right)\times\left(W\cos\theta\,\mathbf j_1 + W\sin\theta\,\mathbf k_1\right) = -W\omega\cos\theta\,\mathbf i_1 - W\dot\theta\sin\theta\,\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(term by term)} \\
> \mathbf v_0^B &= \mathbf v_0^C + \boldsymbol\omega_{20}\times\overrightarrow{CB} = -W\omega\cos\theta\,\mathbf i_1 + \left(H\omega - W\dot\theta\sin\theta\right)\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(Eq. 3.26 in $S_2$)} \\
> \boldsymbol\alpha_{20}\times\overrightarrow{CB} &= \left(\ddot\theta\,\mathbf i_1 + \omega\dot\theta\,\mathbf j_1\right)\times\left(W\cos\theta\,\mathbf j_1 + W\sin\theta\,\mathbf k_1\right) = W\omega\dot\theta\sin\theta\,\mathbf i_1 - W\ddot\theta\sin\theta\,\mathbf j_1 + W\ddot\theta\cos\theta\,\mathbf k_1 \quad &\text{(term by term)} \\
> \boldsymbol\omega_{20}\times\left(\boldsymbol\omega_{20}\times\overrightarrow{CB}\right) &= \left(\dot\theta\,\mathbf i_1 + \omega\,\mathbf k_1\right)\times\left(-W\omega\cos\theta\,\mathbf i_1 - W\dot\theta\sin\theta\,\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1\right) \quad &\text{(previous product)} \\
> &= W\omega\dot\theta\sin\theta\,\mathbf i_1 - \left(W\dot\theta^2\cos\theta + W\omega^2\cos\theta\right)\mathbf j_1 - W\dot\theta^2\sin\theta\,\mathbf k_1 \quad &\text{(term by term)} \\
> \mathbf a_0^B &= \mathbf a_0^C + \boldsymbol\alpha_{20}\times\overrightarrow{CB} + \boldsymbol\omega_{20}\times\left(\boldsymbol\omega_{20}\times\overrightarrow{CB}\right) \quad &\text{(Eq. 3.27 in $S_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^B = \left(2W\omega\dot\theta\sin\theta - H\omega^2\right)\mathbf i_1 - \left(W\ddot\theta\sin\theta + W\dot\theta^2\cos\theta + W\omega^2\cos\theta\right)\mathbf j_1 + \left(W\ddot\theta\cos\theta - W\dot\theta^2\sin\theta\right)\mathbf k_1}$$
>
> **Units:** $[\omega\dot\theta] = [\ddot\theta] = [\mathrm T^{-2}]$
> **Meaning:** both routes give the same velocity and acceleration. Here the Coriolis term of the first route appears split in two equal halves: one inside the angular acceleration of the panel, from the turning of the hinge axis, and one in the double vector product.

### Answers and Checks

| Part of the statement | Answer |
| :--- | :--- |
| Absolute velocity of $B$ | $\mathbf v_0^B = -W\omega\cos\theta\,\mathbf i_1 + (H\omega - W\dot\theta\sin\theta)\,\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1$, in the body basis, with $\mathbf i_1 = \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0$, $\mathbf j_1 = -\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0$, $\mathbf k_1 = \mathbf k_0$ (with $\theta$ measured from $z$ instead, replace $\theta$ by $\theta + \pi/2$) |
| Absolute acceleration of $B$ | $\mathbf a_0^B = (2W\omega\dot\theta\sin\theta - H\omega^2)\,\mathbf i_1 - (W\ddot\theta\sin\theta + W\dot\theta^2\cos\theta + W\omega^2\cos\theta)\,\mathbf j_1 + (W\ddot\theta\cos\theta - W\dot\theta^2\sin\theta)\,\mathbf k_1$ (same remark on the reading of $\theta$) |

**Check against the official key:** Problems.pdf, p. 76 prints both vectors in the body basis; they coincide term by term with the boxed results (box below). The two routes of the kinematics give the same result.

> [!derivation] Comparison with the official key
> **Law:** term-by-term comparison
> **Source:** Problems.pdf, p. 76
>
> $$\begin{aligned}
> \text{key: } \mathbf v_0^B &= -W\omega\cos\theta\,\mathbf i_1 + \left(H\omega - W\dot\theta\sin\theta\right)\mathbf j_1 + W\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(same three components)} \\
> \text{key: } \mathbf a_0^B &= \left(2W\omega\dot\theta\sin\theta - H\omega^2\right)\mathbf i_1 - \left(W\ddot\theta\sin\theta + W\dot\theta^2\cos\theta + W\omega^2\cos\theta\right)\mathbf j_1 + \left(W\ddot\theta\cos\theta - W\dot\theta^2\sin\theta\right)\mathbf k_1 \quad &\text{(same three components)}
> \end{aligned}$$
>
> $$\boxed{\text{velocity and acceleration coincide with the key}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the key uses the same reading of $\theta$ and the same body basis.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 3.26; Notes.pdf, Eq. 3.27
>
> $$\begin{aligned}
> \dot\theta = \ddot\theta = 0:\quad \mathbf v_0^B &= \omega\,\mathbf k_1\times\mathbf r_1^B, \quad \mathbf a_0^B = -\omega^2\left(H\,\mathbf i_1 + W\cos\theta\,\mathbf j_1\right) \quad &\text{(panel locked: rigid rotation about the spin axis)} \\
> \omega = 0:\quad \mathbf v_0^B &= W\dot\theta\,\mathbf k_2, \quad \mathbf a_0^B = W\ddot\theta\,\mathbf k_2 - W\dot\theta^2\,\mathbf j_2 \quad &\text{(no spin: circle of radius $W$ about the hinge)} \\
> \theta = 0:\quad 2W\omega\dot\theta\sin\theta &= 0 \quad &\text{(panel in the plane $xy$: its relative velocity is parallel to the spin axis)}
> \end{aligned}$$
>
> $$\boxed{\text{each limit reduces to a single simple rotation}}$$
>
> **Units:** $[\omega^2H] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the Coriolis term needs both rotations at once and a relative velocity with a part normal to the spin axis.

---

## Problem 47: Two Repelling Particles on Concentric Wires in a Rotating Plane

### Reference Frames, Bases and Coordinates

Two heavy particles of mass $m$ move without friction, $P$ on a circular wire of radius $a$ and $Q$ on a concentric circular wire of radius $2a$, both centred at $O$ in the plane $Ox_1y_1$. The plane turns at the constant rate $\Omega$ about the vertical axis $Oy_1$, which coincides with $Oy_0$; the particles repel each other with a force equal to $k$ times their distance (Problems.pdf, p. 32). The statement asks for the degrees of freedom, the reactions, the relative accelerations, the applied and the inertia forces, the equations of motion, the reactions as functions of time, the energy in $S_1$, and the values of two parameters that make one configuration an equilibrium. The wires are at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf j_0$ vertical, up; gravity $-g\,\mathbf j_0$ |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, attached to the plane of the wires; $\mathbf j_1 = \mathbf j_0$; it turns by $\Omega t$ about $\mathbf j_0$ and coincides with $S_0$ at $t = 0$ |
| Polar bases | at $P$: $\{\mathbf e_r^P, \mathbf e_\varphi, \mathbf k_1\}$; at $Q$: $\{\mathbf e_r^Q, \mathbf e_\theta, \mathbf k_1\}$ (deduced below) |
| Coordinates | $\varphi$ and $\theta$, angles of $OP$ and $OQ$ measured from $Ox_1$, positive from $\mathbf i_1$ towards $\mathbf j_1$ |
| Data | $m$ [kg], $a$ [m], $k$ [N m$^{-1}$], $\Omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$]; dimensionless $\alpha = ka/(mg)$, $\beta = a\Omega^2/g$ |
| Unknowns | $\varphi(t)$, $\theta(t)$ and the reaction components $N_1, N_2$ (on $P$), $N_3, N_4$ (on $Q$) |
| Applied forces | weights $-mg\,\mathbf j_1$; repulsion $k\,\overrightarrow{QP}$ on $P$ and $k\,\overrightarrow{PQ}$ on $Q$ |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; smooth bilateral wires; $\Omega$ constant |
| Readings | (1) The curved arrow of the figure is read as a turn in the positive sense about $+\mathbf j_0$ (counterclockwise seen from above), so the angular velocity is $\Omega\,\mathbf j_1$ with $\Omega$ positive. The opposite sense changes the sign of $\Omega$, which changes only the Coriolis forces and the reactions $N_2$, $N_4$ (they change sign); the equations of motion, the energy and part (i) contain only the square of $\Omega$ and do not change. (2) $\mathbf k_1$, the cross product of $\mathbf i_1$ and $\mathbf j_1$, points out of the paper in the figure |

#### (a) Configuration degrees of freedom

> [!derivation] Coordinates minus independent constraints
> **Law:** each holonomic constraint removes one coordinate; the motion of the plane is prescribed
> **Source:** Notes.pdf, Eq. 6.3; Problems.pdf, p. 32
>
> $$\begin{aligned}
> P:&\quad z_1^P = 0, \quad \left(x_1^P\right)^2 + \left(y_1^P\right)^2 - a^2 = 0 \quad &\text{(plane and circle of radius $a$)} \\
> Q:&\quad z_1^Q = 0, \quad \left(x_1^Q\right)^2 + \left(y_1^Q\right)^2 - 4a^2 = 0 \quad &\text{(plane and circle of radius $2a$)} \\
> \text{degrees of freedom} &= 3 + 3 - 4 = 2 \quad &\text{(six coordinates, four constraints)}
> \end{aligned}$$
>
> $$\boxed{\text{2 configuration degrees of freedom: } \varphi,\ \theta}$$
>
> **Units:** $[\varphi] = [\theta] = [1]$
> **Meaning:** one angle per particle; the four constraints become the four reaction components of part (b).

### Change of Basis and Position Vector

![[attachments/EM-SOL/p47-top-view.svg]]

> [!derivation] Basis of S1: rotation by Omega t about the vertical j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf j_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf k_0$, the cross product of $\mathbf i_0$ and $\mathbf j_0$, points down the page (fingers from $\mathbf i_0$ to the reader, thumb down). The plane turns counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ up the page, which is the direction of minus $\mathbf k_0$ (the minus sign). $\mathbf k_1$ is $\mathbf k_0$ turned by the same angle; the counterclockwise turn of a vector pointing down carries its tip to the right, so its opposite leg $\sin\Omega t$ lies along plus $\mathbf i_0$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0, \quad \mathbf j_1 = \mathbf j_0, \quad \mathbf k_1 = \sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \sin\Omega t\left(-\sin\Omega t\right)\right) = 1 \quad &\text{(expansion along the second row, cofactor sign $(-1)^{2+2}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows)} \\
> \mathbf i_1\times\mathbf j_1 &= \cos\Omega t\,\mathbf i_0\times\mathbf j_0 - \sin\Omega t\,\mathbf k_0\times\mathbf j_0 = \cos\Omega t\,\mathbf k_0 + \sin\Omega t\,\mathbf i_0 = \mathbf k_1 \quad &\text{(right-handed)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & 0 & \sin\Omega t \cr 0 & 1 & 0 \cr -\sin\Omega t & 0 & \cos\Omega t \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Omega t] = [1]$
> **Meaning:** the columns are the vectors of the plane frame in the fixed basis; the vertical is shared by both frames.

![[attachments/EM-SOL/p47-wire-plane.svg]]

> [!derivation] Positions and polar bases in the plane of the wires
> **Law:** right triangles of the radii; tangent vector as the derivative of the radial unit vector
> **Source:** Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 32
>
> The plane $Ox_1y_1$ is drawn with $\mathbf i_1$ to the right, $\mathbf j_1$ up and $\mathbf k_1$ out of the paper (⊙). For $P$ the shaded right triangle has the hypotenuse $OP$, of length $a$; the leg adjacent to $\varphi$ is $a\cos\varphi$ along $\mathbf i_1$ and the opposite leg $a\sin\varphi$ along $\mathbf j_1$. For $Q$ the same triangle has the hypotenuse $2a$; with $\theta$ negative, as drawn, its leg $2a\sin\theta$ is negative and $Q$ lies below $Ox_1$. Both angles are the standard polar angles of the plane, so no conversion is needed.
>
> $$\begin{aligned}
> \mathbf e_r^P &= \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1, \quad \mathbf e_\varphi = \frac{d\mathbf e_r^P}{d\varphi} = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1 \quad &\text{(triangle of $P$; $\tfrac{d}{d\varphi}\cos\varphi = -\sin\varphi$)} \\
> \mathbf e_r^Q &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \quad \mathbf e_\theta = \frac{d\mathbf e_r^Q}{d\theta} = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(triangle of $Q$)} \\
> \mathbf r_1^P &= a\,\mathbf e_r^P, \quad \mathbf r_1^Q = 2a\,\mathbf e_r^Q \quad &\text{(Eq. 3.16 with the common origin $O$)} \\
> \mathbf e_r^P\times\mathbf e_\varphi &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \cos\varphi & \sin\varphi & 0 \cr -\sin\varphi & \cos\varphi & 0 \end{vmatrix} = (+1)(0)\,\mathbf i_1 + (-1)(0)\,\mathbf j_1 + (+1)\left(\cos^2\varphi + \sin^2\varphi\right)\mathbf k_1 = \mathbf k_1 \quad &\text{(first row; cofactor signs plus, minus, plus)} \\
> \mathbf e_r^P\cdot\mathbf e_r^Q &= \cos\varphi\cos\theta + \sin\varphi\sin\theta = \cos\left(\varphi - \theta\right) \quad &\text{(difference formula)} \\
> \mathbf e_r^Q\cdot\mathbf e_\varphi &= -\sin\varphi\cos\theta + \cos\varphi\sin\theta = -\sin\left(\varphi - \theta\right), \quad \mathbf e_r^P\cdot\mathbf e_\theta = -\sin\theta\cos\varphi + \cos\theta\sin\varphi = \sin\left(\varphi - \theta\right) \quad &\text{(difference formula)} \\
> \mathbf i_1 &= \cos\varphi\,\mathbf e_r^P - \sin\varphi\,\mathbf e_\varphi, \quad \mathbf j_1 = \sin\varphi\,\mathbf e_r^P + \cos\varphi\,\mathbf e_\varphi \quad &\text{(projections; the same with $\theta$ at $Q$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^P = a\cos\varphi\,\mathbf i_1 + a\sin\varphi\,\mathbf j_1, \qquad \mathbf r_1^Q = 2a\cos\theta\,\mathbf i_1 + 2a\sin\theta\,\mathbf j_1}$$
>
> **Units:** $[a] = [\mathrm L]$
> **Meaning:** each polar triad is right-handed and orthonormal; the dot products between the two triads depend only on the difference of the angles.

### Kinematics

> [!derivation] Motion of S1 and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf j_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed vertical; $\Omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf j_1\times\mathbf i_1 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf j_1\times\mathbf k_1 = \Omega\,\mathbf i_1 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\Omega t\,\mathbf i_0 - \sin\Omega t\,\mathbf k_0\right) &= -\Omega\sin\Omega t\,\mathbf i_0 - \Omega\cos\Omega t\,\mathbf k_0 = -\Omega\,\mathbf k_1 \quad &\text{(check: chain rule on $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = -\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \mathbf 0, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \Omega\,\mathbf i_1}$$
>
> **Units:** $[\Omega] = [\mathrm T^{-1}]$
> **Meaning:** the horizontal axes of the plane frame turn; the vertical does not.

#### (c) Relative accelerations

> [!derivation] Relative velocity and acceleration of P and Q
> **Law:** time derivatives in $S_1$; chain rule on the polar vectors; product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 32
>
> $$\begin{aligned}
> \left.\frac{d\mathbf e_r^P}{dt}\right|_1 &= \frac{d\mathbf e_r^P}{d\varphi}\,\frac{d\varphi}{dt} = \dot\varphi\,\mathbf e_\varphi, \quad \left.\frac{d\mathbf e_\varphi}{dt}\right|_1 = \frac{d\mathbf e_\varphi}{d\varphi}\,\frac{d\varphi}{dt} = \dot\varphi\left(-\cos\varphi\,\mathbf i_1 - \sin\varphi\,\mathbf j_1\right) = -\dot\varphi\,\mathbf e_r^P \quad &\text{(chain rule; $\mathbf i_1$, $\mathbf j_1$ constant in $S_1$)} \\
> \mathbf v_1^P &= a\dot\varphi\,\mathbf e_\varphi, \quad \mathbf a_1^P = a\ddot\varphi\,\mathbf e_\varphi + a\dot\varphi\left(-\dot\varphi\,\mathbf e_r^P\right) = a\ddot\varphi\,\mathbf e_\varphi - a\dot\varphi^2\,\mathbf e_r^P \quad &\text{(product rule)} \\
> \mathbf v_1^Q &= 2a\dot\theta\,\mathbf e_\theta, \quad \mathbf a_1^Q = 2a\ddot\theta\,\mathbf e_\theta - 2a\dot\theta^2\,\mathbf e_r^Q \quad &\text{(the same with $2a$ and $\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_1^P = -a\dot\varphi^2\,\mathbf e_r^P + a\ddot\varphi\,\mathbf e_\varphi, \qquad \mathbf a_1^Q = -2a\dot\theta^2\,\mathbf e_r^Q + 2a\ddot\theta\,\mathbf e_\theta}$$
>
> **Units:** $[a\dot\varphi^2] = [a\ddot\varphi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** circular motions about $O$ in the plane: a centripetal part towards $O$ and a tangential part along each wire.

> [!derivation] Absolute acceleration: transport and Coriolis terms as they arise
> **Law:** time derivative in $S_0$ of a position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Both particles stay in the plane of the wires, so their positions are $x_1\,\mathbf i_1 + y_1\,\mathbf j_1$; the time derivatives of the components are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0 &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + x_1\left(-\Omega\,\mathbf k_1\right) = \mathbf v_1 - \Omega x_1\,\mathbf k_1 \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1}{dt}\right|_0 &= \ddot x_1\,\mathbf i_1 + \ddot y_1\,\mathbf j_1 + \dot x_1\left(-\Omega\,\mathbf k_1\right) = \mathbf a_1 - \Omega\dot x_1\,\mathbf k_1 \quad &\text{(product rule; the basis turns inside $\mathbf v_1$)} \\
> \left.\frac{d}{dt}\right|_0\left(-\Omega x_1\,\mathbf k_1\right) &= -\Omega\dot x_1\,\mathbf k_1 - \Omega x_1\,\Omega\,\mathbf i_1 \quad &\text{(product rule; derivative of $\mathbf k_1$)} \\
> \mathbf a_0 &= \mathbf a_1 - 2\Omega\dot x_1\,\mathbf k_1 - \Omega^2x_1\,\mathbf i_1 \quad &\text{(Coriolis: the two equal terms; centripetal: the last)} \\
> P:&\quad x_1 = a\cos\varphi, \ \dot x_1 = -a\dot\varphi\sin\varphi \;\Rightarrow\; -2\Omega\dot x_1\,\mathbf k_1 = 2\Omega a\dot\varphi\sin\varphi\,\mathbf k_1, \ -\Omega^2x_1\,\mathbf i_1 = -\Omega^2a\cos\varphi\,\mathbf i_1 \quad &\text{(chain rule)} \\
> Q:&\quad x_1 = 2a\cos\theta, \ \dot x_1 = -2a\dot\theta\sin\theta \;\Rightarrow\; -2\Omega\dot x_1\,\mathbf k_1 = 4\Omega a\dot\theta\sin\theta\,\mathbf k_1, \ -\Omega^2x_1\,\mathbf i_1 = -2\Omega^2a\cos\theta\,\mathbf i_1 \quad &\text{(chain rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - \Omega^2a\cos\varphi\,\mathbf i_1 + 2\Omega a\dot\varphi\sin\varphi\,\mathbf k_1, \qquad \mathbf a_0^Q = \mathbf a_1^Q - 2\Omega^2a\cos\theta\,\mathbf i_1 + 4\Omega a\dot\theta\sin\theta\,\mathbf k_1}$$
>
> **Units:** $[\Omega^2a] = [\Omega a\dot\varphi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the centripetal term points horizontally towards the axis, along minus $\mathbf i_1$ for a particle on the side of positive $x_1$; the Coriolis term is normal to the plane of the wires.

### Forces and Equations of Motion

![[attachments/EM-SOL/p47-fbd.svg]]

#### (b) Reaction forces

> [!derivation] Components of the reactions
> **Law:** a smooth wire exerts no force along its tangent; one reaction component per constraint
> **Source:** Notes.pdf, Eq. 6.11; [Lecture 3, Slide 14]; Problems.pdf, p. 32
>
> The tangent of the wire of $P$ is $\mathbf e_\varphi$ and that of $Q$ is $\mathbf e_\theta$; the plane normal to each tangent is spanned by the radial vector and $\mathbf k_1$.
>
> $$\begin{aligned}
> \mathbf N^P\cdot\mathbf e_\varphi &= 0 \;\Rightarrow\; \mathbf N^P = N_1\,\mathbf e_r^P + N_2\,\mathbf k_1 \quad &\text{(smooth wire of radius $a$)} \\
> \mathbf N^Q\cdot\mathbf e_\theta &= 0 \;\Rightarrow\; \mathbf N^Q = N_3\,\mathbf e_r^Q + N_4\,\mathbf k_1 \quad &\text{(smooth wire of radius $2a$)}
> \end{aligned}$$
>
> $$\boxed{4 \text{ independent components: } \mathbf N^P = N_1\,\mathbf e_r^P + N_2\,\mathbf k_1, \quad \mathbf N^Q = N_3\,\mathbf e_r^Q + N_4\,\mathbf k_1}$$
>
> **Units:** $[N_i] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** as many unknown components as constraints; each reaction lies in the plane normal to its wire.

#### (d) Applied forces

> [!derivation] Weights and mutual repulsion in the polar bases
> **Law:** uniform weight; repulsion along the line of the particles, proportional to the distance, action and reaction
> **Source:** Notes.pdf, Eq. 4.14; Problems.pdf, p. 32
>
> $$\begin{aligned}
> \mathbf W^P &= -mg\,\mathbf j_1 = -mg\sin\varphi\,\mathbf e_r^P - mg\cos\varphi\,\mathbf e_\varphi, \quad \mathbf W^Q = -mg\sin\theta\,\mathbf e_r^Q - mg\cos\theta\,\mathbf e_\theta \quad &\text{($\mathbf j_1$ in each polar basis)} \\
> \overrightarrow{QP} &= a\,\mathbf e_r^P - 2a\,\mathbf e_r^Q = a\left(\cos\varphi - 2\cos\theta\right)\mathbf i_1 + a\left(\sin\varphi - 2\sin\theta\right)\mathbf j_1 \quad &\text{(positions)} \\
> \mathbf F_k^P &= k\,\overrightarrow{QP} = ka\left[1 - 2\cos\left(\varphi - \theta\right)\right]\mathbf e_r^P + 2ka\sin\left(\varphi - \theta\right)\mathbf e_\varphi \quad &\text{(dot products with $\mathbf e_r^P$, $\mathbf e_\varphi$)} \\
> \mathbf F_k^Q &= k\,\overrightarrow{PQ} = ka\left[2 - \cos\left(\varphi - \theta\right)\right]\mathbf e_r^Q - ka\sin\left(\varphi - \theta\right)\mathbf e_\theta \quad &\text{(dot products with $\mathbf e_r^Q$, $\mathbf e_\theta$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf F^P = -mg\,\mathbf j_1 + k\left(\mathbf r_1^P - \mathbf r_1^Q\right) = \left[-mg\sin\varphi + ka\left(1 - 2\cos\left(\varphi - \theta\right)\right)\right]\mathbf e_r^P + \left[-mg\cos\varphi + 2ka\sin\left(\varphi - \theta\right)\right]\mathbf e_\varphi \cr \mathbf F^Q = -mg\,\mathbf j_1 + k\left(\mathbf r_1^Q - \mathbf r_1^P\right) = \left[-mg\sin\theta + ka\left(2 - \cos\left(\varphi - \theta\right)\right)\right]\mathbf e_r^Q + \left[-mg\cos\theta - ka\sin\left(\varphi - \theta\right)\right]\mathbf e_\theta \end{gathered}}$$
>
> **Units:** $[mg] = [ka] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the applied forces lie in the plane of the wires; the repulsion is tangent to the wire of $P$ with its largest value when the two radii are perpendicular.

#### (e) Inertia forces seen from S1

> [!derivation] Centrifugal and Coriolis forces
> **Law:** inertia forces of a non-inertial frame, the terms of the composition box times minus the mass
> **Source:** Notes.pdf, Eq. 4.62; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]
>
> $$\begin{aligned}
> \mathbf F_A &= -m\,\mathbf a_0^O = \mathbf 0, \quad \mathbf F_E = -m\,\boldsymbol\alpha_{10}\times\mathbf r_1 = \mathbf 0 \quad &\text{($O$ fixed; $\Omega$ constant)} \\
> \mathbf F_C^P &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\Omega^2a\cos\varphi\,\mathbf i_1 = m\Omega^2a\cos\varphi\left(\cos\varphi\,\mathbf e_r^P - \sin\varphi\,\mathbf e_\varphi\right) \quad &\text{(centripetal term times $-m$; $\mathbf i_1$ in the polar basis)} \\
> \mathbf F_C^Q &= 2m\Omega^2a\cos\theta\,\mathbf i_1 = 2m\Omega^2a\cos\theta\left(\cos\theta\,\mathbf e_r^Q - \sin\theta\,\mathbf e_\theta\right) \quad &\text{(the same for $Q$)} \\
> \mathbf F_{COR}^P &= -2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P = -2m\Omega a\dot\varphi\sin\varphi\,\mathbf k_1, \quad \mathbf F_{COR}^Q = -4m\Omega a\dot\theta\sin\theta\,\mathbf k_1 \quad &\text{(Coriolis term times $-m$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf F_C^P = m\Omega^2a\cos\varphi\,\mathbf i_1, \quad \mathbf F_C^Q = 2m\Omega^2a\cos\theta\,\mathbf i_1, \cr \mathbf F_{COR}^P = -2m\Omega a\dot\varphi\sin\varphi\,\mathbf k_1, \quad \mathbf F_{COR}^Q = -4m\Omega a\dot\theta\sin\theta\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[m\Omega^2a] = [m\Omega a\dot\varphi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the centrifugal force pushes each particle horizontally away from the vertical axis; the Coriolis force is normal to the plane of the wires, so only the reactions $N_2$ and $N_4$ can balance it.

#### (f) Equations of motion free of other unknowns

> [!derivation] Newton's second law in S1 projected on the polar bases
> **Law:** $m\,\mathbf a_1 = \mathbf F + \mathbf N + \mathbf F_i$ for each particle; the tangential projections are free of the reactions and of the Coriolis forces
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 5, Slide 28]; Problems.pdf, p. 32
>
> $$\begin{aligned}
> P,\ \mathbf e_\varphi:&\quad ma\ddot\varphi = -mg\cos\varphi + 2ka\sin\left(\varphi - \theta\right) - m\Omega^2a\sin\varphi\cos\varphi \quad &\text{(weight, repulsion, centrifugal)} \\
> Q,\ \mathbf e_\theta:&\quad 2ma\ddot\theta = -mg\cos\theta - ka\sin\left(\varphi - \theta\right) - 2m\Omega^2a\sin\theta\cos\theta \quad &\text{(weight, repulsion, centrifugal)} \\
> P,\ \mathbf e_r^P:&\quad -ma\dot\varphi^2 = N_1 - mg\sin\varphi + ka\left[1 - 2\cos\left(\varphi - \theta\right)\right] + m\Omega^2a\cos^2\varphi \quad &\text{(with the reaction $N_1$)} \\
> P,\ \mathbf k_1:&\quad 0 = N_2 - 2m\Omega a\dot\varphi\sin\varphi \quad &\text{(reaction and Coriolis)} \\
> Q,\ \mathbf e_r^Q:&\quad -2ma\dot\theta^2 = N_3 - mg\sin\theta + ka\left[2 - \cos\left(\varphi - \theta\right)\right] + 2m\Omega^2a\cos^2\theta \quad &\text{(with the reaction $N_3$)} \\
> Q,\ \mathbf k_1:&\quad 0 = N_4 - 4m\Omega a\dot\theta\sin\theta \quad &\text{(reaction and Coriolis)}
> \end{aligned}$$
>
> $$\boxed{\ddot\varphi = -\frac{g}{a}\cos\varphi + \frac{2k}{m}\sin\left(\varphi - \theta\right) - \Omega^2\sin\varphi\cos\varphi, \qquad \ddot\theta = -\frac{g}{2a}\cos\theta - \frac{k}{2m}\sin\left(\varphi - \theta\right) - \Omega^2\sin\theta\cos\theta}$$
>
> **Units:** $[g/a] = [k/m] = [\Omega^2] = [\ddot\varphi] = [\mathrm T^{-2}]$
> **Meaning:** six scalar equations for six unknowns; the two tangential ones are a closed system for the two angles, coupled through the repulsion.

#### (g) Reactions as functions of time

> [!derivation] The four remaining projections solved for the reactions
> **Law:** the radial and normal projections of part (f), with the angles known
> **Source:** Notes.pdf, Eq. 4.63; Problems.pdf, p. 32
>
> $$\begin{aligned}
> N_1 &= -ma\dot\varphi^2 + mg\sin\varphi - ka\left[1 - 2\cos\left(\varphi - \theta\right)\right] - m\Omega^2a\cos^2\varphi \quad &\text{($\mathbf e_r^P$ equation)} \\
> N_2 &= 2m\Omega a\dot\varphi\sin\varphi \quad &\text{($\mathbf k_1$ equation of $P$)} \\
> N_3 &= -2ma\dot\theta^2 + mg\sin\theta - ka\left[2 - \cos\left(\varphi - \theta\right)\right] - 2m\Omega^2a\cos^2\theta \quad &\text{($\mathbf e_r^Q$ equation)} \\
> N_4 &= 4m\Omega a\dot\theta\sin\theta \quad &\text{($\mathbf k_1$ equation of $Q$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf N^P(t) = \left\{-ma\dot\varphi^2 + mg\sin\varphi - ka\left[1 - 2\cos\left(\varphi - \theta\right)\right] - m\Omega^2a\cos^2\varphi\right\}\mathbf e_r^P + 2m\Omega a\dot\varphi\sin\varphi\,\mathbf k_1 \cr \mathbf N^Q(t) = \left\{-2ma\dot\theta^2 + mg\sin\theta - ka\left[2 - \cos\left(\varphi - \theta\right)\right] - 2m\Omega^2a\cos^2\theta\right\}\mathbf e_r^Q + 4m\Omega a\dot\theta\sin\theta\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** with the solution of part (f) substituted, each reaction is an explicit function of time; the components normal to the plane come only from the Coriolis forces.

### Answers and Checks

#### (h) Mechanical energy in S1

> [!derivation] Why the energy in S1 is conserved, and its expression
> **Law:** power of each force on the relative velocity; potentials of the weights, the repulsion and the centrifugal forces
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Two reasons. First, the forces that do no work in $S_1$: the reactions (the wires are at rest in $S_1$ and smooth, so each reaction is normal to the relative velocity), the Coriolis forces (normal to the relative velocities), and the origin and Euler forces, which vanish. Second, the forces that work have potentials of the positions in $S_1$: the weights, constant in $S_1$ because $\mathbf j_1$ is the fixed vertical; the repulsion, which depends only on $\overrightarrow{PQ}$ (its potential has a minus sign because the force pushes the particles apart); and the centrifugal forces, because the rate is constant and the axis fixed. A point of the plane is at the distance of its $x_1$ coordinate from the axis $Oy_1$.
>
> $$\begin{aligned}
> \mathbf N^P\cdot\mathbf v_1^P &= \left(N_1\,\mathbf e_r^P + N_2\,\mathbf k_1\right)\cdot a\dot\varphi\,\mathbf e_\varphi = 0, \quad \mathbf F_{COR}^P\cdot\mathbf v_1^P = -2m\Omega a^2\dot\varphi^2\sin\varphi\,\mathbf k_1\cdot\mathbf e_\varphi = 0 \quad &\text{(no power; the same for $Q$)} \\
> \left|\overrightarrow{PQ}\right|^2 &= a^2 + 4a^2 - 4a^2\,\mathbf e_r^P\cdot\mathbf e_r^Q = 5a^2 - 4a^2\cos\left(\varphi - \theta\right) \quad &\text{(square of the difference)} \\
> V_1 &= mga\sin\varphi + 2mga\sin\theta - \tfrac12 k\left|\overrightarrow{PQ}\right|^2 - \tfrac12 m\Omega^2a^2\cos^2\varphi - \tfrac12 m\Omega^2\left(2a\cos\theta\right)^2 \quad &\text{(Eq. 4.14; Slide 30)} \\
> &= mga\left(\sin\varphi + 2\sin\theta\right) + 2ka^2\cos\left(\varphi - \theta\right) - \tfrac12 m\Omega^2a^2\left(\cos^2\varphi + 4\cos^2\theta\right) - \tfrac52 ka^2 \quad &\text{(expanded)} \\
> T_1 &= \tfrac12 m\left(a\dot\varphi\right)^2 + \tfrac12 m\left(2a\dot\theta\right)^2 = \tfrac12 ma^2\left(\dot\varphi^2 + 4\dot\theta^2\right) \quad &\text{(relative velocities)} \\
> \frac{d}{dt}\left(T_1 + V_1\right) &= ma^2\dot\varphi\ddot\varphi + 4ma^2\dot\theta\ddot\theta + mga\left(\cos\varphi\,\dot\varphi + 2\cos\theta\,\dot\theta\right) - 2ka^2\sin\left(\varphi - \theta\right)\left(\dot\varphi - \dot\theta\right) + m\Omega^2a^2\left(\cos\varphi\sin\varphi\,\dot\varphi + 4\cos\theta\sin\theta\,\dot\theta\right) \quad &\text{(chain rule on each term)} \\
> &= a\dot\varphi\left[ma\ddot\varphi + mg\cos\varphi - 2ka\sin\left(\varphi - \theta\right) + m\Omega^2a\sin\varphi\cos\varphi\right] + 2a\dot\theta\left[2ma\ddot\theta + mg\cos\theta + ka\sin\left(\varphi - \theta\right) + 2m\Omega^2a\sin\theta\cos\theta\right] = 0 \quad &\text{(grouped; both brackets vanish by part (f))}
> \end{aligned}$$
>
> $$\boxed{\text{yes:}\quad \frac12 ma^2\left(\dot\varphi^2 + 4\dot\theta^2\right) + mga\left(\sin\varphi + 2\sin\theta\right) + 2ka^2\cos\left(\varphi - \theta\right) - \frac12 m\Omega^2a^2\left(\cos^2\varphi + 4\cos^2\theta\right) = E_1 = \text{const}}$$
>
> **Units:** $[ma^2\dot\varphi^2] = [mga] = [ka^2] = [m\Omega^2a^2] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the energy of the relative motion is a first integral; the constant term of the repulsion potential is dropped, and the constant is fixed by initial conditions, which the statement does not give.

#### (i) Parameters for the equilibrium at 30 and minus 60 degrees

> [!derivation] Relative equilibrium conditions
> **Law:** constant coordinates in $S_1$, so the rates and accelerations vanish in the two equations of part (f)
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 32
>
> The first equation of part (f) is multiplied by $a/g$ and the second by $2a/g$, which brings in the two parameters.
>
> $$\begin{aligned}
> 0 &= -\cos\varphi + 2\alpha\sin\left(\varphi - \theta\right) - \beta\sin\varphi\cos\varphi, \quad 0 = -\cos\theta - \alpha\sin\left(\varphi - \theta\right) - 2\beta\sin\theta\cos\theta \quad &\text{(rates zero; $\alpha = ka/(mg)$, $\beta = a\Omega^2/g$)} \\
> \varphi - \theta &= 30^\circ - \left(-60^\circ\right) = 90^\circ, \quad \sin 90^\circ = 1 \quad &\text{(the two radii are perpendicular)} \\
> 0 &= -\frac{\sqrt3}{2} + 2\alpha - \frac{\sqrt3}{4}\,\beta \quad &\text{($\cos 30^\circ = \tfrac{\sqrt3}{2}$, $\sin 30^\circ = \tfrac12$)} \\
> 0 &= -\frac12 - \alpha + \frac{\sqrt3}{2}\,\beta \quad &\text{($\cos(-60^\circ) = \tfrac12$, $\sin(-60^\circ) = -\tfrac{\sqrt3}{2}$, so $-2\beta\sin\theta\cos\theta = \tfrac{\sqrt3}{2}\beta$)} \\
> \alpha &= \frac{\sqrt3}{2}\,\beta - \frac12 \quad &\text{(second equation)} \\
> 0 &= -\frac{\sqrt3}{2} + \sqrt3\,\beta - 1 - \frac{\sqrt3}{4}\,\beta \;\Rightarrow\; \frac{3\sqrt3}{4}\,\beta = \frac{2 + \sqrt3}{2} \quad &\text{(substituted in the first)} \\
> \beta &= \frac{2\left(2 + \sqrt3\right)}{3\sqrt3} = \frac{6 + 4\sqrt3}{9} = 1.43647 \quad &\text{(rationalised: times $\sqrt3/\sqrt3$)} \\
> \alpha &= \frac{\sqrt3}{2}\cdot\frac{6 + 4\sqrt3}{9} - \frac12 = \frac{6\sqrt3 + 12 - 9}{18} = \frac{1 + 2\sqrt3}{6} = 0.74402 \quad &\text{(back-substituted)} \\
> -\frac{\sqrt3}{2} + 2\left(0.74402\right) - \frac{\sqrt3}{4}\left(1.43647\right) &= -0.86603 + 1.48804 - 0.62201 = 0.00000 \quad &\text{(numerical check of the first equation)}
> \end{aligned}$$
>
> $$\boxed{\alpha = \frac{ka}{mg} = \frac{1 + 2\sqrt3}{6} \approx 0.744, \qquad \beta = \frac{a\Omega^2}{g} = \frac{6 + 4\sqrt3}{9} \approx 1.4365}$$
>
> **Units:** $[ka/(mg)] = [a\Omega^2/g] = [1]$
> **Meaning:** both values are positive, so the configuration can be an equilibrium. Along the wire of $P$ the repulsion pushes it towards larger angles, while its weight and the centrifugal force (towards the horizontal, away from the axis) push it back; along the wire of $Q$ the weight and the repulsion push it towards more negative angles and the centrifugal force pulls it back towards the horizontal.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 2 ($\varphi$, $\theta$) |
| (b) Reactions | 4 independent components: $\mathbf N^P = N_1\,\mathbf e_r^P + N_2\,\mathbf k_1$, $\mathbf N^Q = N_3\,\mathbf e_r^Q + N_4\,\mathbf k_1$ |
| (c) Relative accelerations | $\mathbf a_1^P = a\ddot\varphi\,\mathbf e_\varphi - a\dot\varphi^2\,\mathbf e_r^P$, $\mathbf a_1^Q = 2a\ddot\theta\,\mathbf e_\theta - 2a\dot\theta^2\,\mathbf e_r^Q$, with $\mathbf e_r^P = \cos\varphi\,\mathbf i_1 + \sin\varphi\,\mathbf j_1$, $\mathbf e_\varphi = -\sin\varphi\,\mathbf i_1 + \cos\varphi\,\mathbf j_1$ (same with $\theta$) |
| (d) Applied forces | $-mg\,\mathbf j_1 + k(\mathbf r_1^P - \mathbf r_1^Q)$ on $P$ and $-mg\,\mathbf j_1 + k(\mathbf r_1^Q - \mathbf r_1^P)$ on $Q$, in polar components as boxed in part (d) |
| (e) Inertia forces | $\mathbf F_C^P = m\Omega^2a\cos\varphi\,\mathbf i_1$, $\mathbf F_C^Q = 2m\Omega^2a\cos\theta\,\mathbf i_1$, $\mathbf F_{COR}^P = -2m\Omega a\dot\varphi\sin\varphi\,\mathbf k_1$, $\mathbf F_{COR}^Q = -4m\Omega a\dot\theta\sin\theta\,\mathbf k_1$; origin and Euler forces zero (opposite sense of rotation: Coriolis forces change sign) |
| (f) Equations of motion | $\ddot\varphi = -(g/a)\cos\varphi + (2k/m)\sin(\varphi - \theta) - \Omega^2\sin\varphi\cos\varphi$; $\ddot\theta = -(g/2a)\cos\theta - (k/2m)\sin(\varphi - \theta) - \Omega^2\sin\theta\cos\theta$ |
| (g) Reactions | $N_1$, $N_3$ as boxed in part (g); $N_2 = 2m\Omega a\dot\varphi\sin\varphi$, $N_4 = 4m\Omega a\dot\theta\sin\theta$ (opposite sense of rotation: $N_2$, $N_4$ change sign) |
| (h) Energy in $S_1$ | conserved: $\frac12 ma^2(\dot\varphi^2 + 4\dot\theta^2) + mga(\sin\varphi + 2\sin\theta) + 2ka^2\cos(\varphi - \theta) - \frac12 m\Omega^2a^2(\cos^2\varphi + 4\cos^2\theta) = \text{const}$ |
| (i) Parameters | $\alpha = (1 + 2\sqrt3)/6 \approx 0.744$, $\beta = (6 + 4\sqrt3)/9 \approx 1.4365$ |

**Check against the official key:** Problems.pdf, p. 76 prints only the final quantities of part (i), 0.744 and 1.4365; the exact values of the box, 0.74402 and 1.43647, round to them. The other parts have no key; the energy is checked against the equations of motion in part (h), and the limiting cases follow.

> [!derivation] Limiting cases
> **Law:** the equations of part (f) and the reactions of part (g) at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega \to 0:\quad N_2 &= N_4 = 0, \quad \ddot\varphi = -\frac{g}{a}\cos\varphi + \frac{2k}{m}\sin\left(\varphi - \theta\right) \quad &\text{(fixed vertical wires)} \\
> k \to 0:\quad \ddot\varphi &= -\frac{g}{a}\cos\varphi - \Omega^2\sin\varphi\cos\varphi \quad &\text{(two independent beads on spinning circles)} \\
> k \to 0, \ \varphi = -\tfrac{\pi}{2}:\quad \ddot\varphi &= -\frac{g}{a}\cdot 0 - \Omega^2\left(-1\right)\cdot 0 = 0 \quad &\text{(the lowest point is an equilibrium)}
> \end{aligned}$$
>
> $$\boxed{\text{with no rotation the wires carry no load normal to the plane; with no repulsion the particles move independently}}$$
>
> **Units:** $[\mathrm T^{-2}]$
> **Meaning:** the Coriolis forces only load the wires; they never enter the equations of motion or the energy.

---

## Problem 49: Particle on a Rotating Sphere Attracted to a Point

### Reference Frames, Bases and Coordinates

A particle $P$ of mass $m$ slides without friction on a sphere of radius $a$ centred at the origin $O$ of the inertial frame $S_0$. A point $A$ of the equatorial plane, at the distance $a$ from the surface, attracts $P$ with a force equal to $k$ times their distance. The sphere and $A$ turn rigidly about the vertical with the angular velocity $\Omega\,\mathbf k_0$; there is no gravity (Problems.pdf, p. 34). The statement asks for the position, velocity and acceleration in $S_1$, the equation of motion and two scalar equations for the angles, the energy in $S_1$, the equilibria as functions of the ratio of $m\Omega^2$ to $k$, and the reaction. The sphere and $A$ are at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ along the axis of rotation |
| Moving frame | $S_1 = \{O;\ \mathcal B_1\}$, turning with the sphere and $A$: $\mathbf k_1 = \mathbf k_0$, $\mathbf i_1$ towards $A$; it turns by $\Omega t$ from $\mathbf i_0$ towards $\mathbf j_0$ (figure) and coincides with $S_0$ at $t = 0$ |
| Point $A$ | on the $\mathbf i_1$ axis, at the distance $a$ from the surface, so $OA$ is $2a$ |
| Spherical basis at $P$ | $\{\mathbf e_r, \mathbf e_\phi, \mathbf e_\theta\}$ with the polar axis along $OA$ (deduced below); auxiliary unit vector $\mathbf u$ of the plane of $\mathbf j_1$ and $\mathbf k_1$; $P'$ the projection of $P$ on that plane |
| Coordinates | $\phi$, angle at $O$ between $\overrightarrow{OA}$ and $\overrightarrow{OP}$; $\theta$, angle about the axis $OA$ from the equatorial plane (side of $\mathbf j_1$) towards $\mathbf k_1$ |
| Data | $m$ [kg], $a$ [m], $k$ [N m$^{-1}$], $\Omega$ [rad s$^{-1}$]; ratio $\Lambda = m\Omega^2/k$ [1] |
| Unknowns | $\phi(t)$, $\theta(t)$ and the reaction $N\,\mathbf e_r$ |
| Applied force | attraction $k\,\overrightarrow{PA}$; no gravity |
| Inertia forces (in $S_1$) | centrifugal and Coriolis; no origin or Euler terms (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; smooth sphere; $\Omega$ constant |
| Readings | (1) Read from the figure: $\phi$ is the angle $AOP$ and $\theta$ the angle, seen at the point where $OA$ crosses the sphere, between the equator and the great circle through that point and $P$; so $\phi$ is a polar angle about $OA$ and $\theta$ its azimuth. If instead $\phi$ were the azimuth in the equatorial plane from $\mathbf i_1$ and $\theta$ the latitude, the position would be $a(\cos\theta\cos\phi\,\mathbf i_1 + \cos\theta\sin\phi\,\mathbf j_1 + \sin\theta\,\mathbf k_1)$; the equilibria are the same points, with the coordinates given in the Answers table. (2) The contact is read as bilateral (the reaction may take either sign): one equilibrium needs the sphere to pull the particle in. With a one-sided contact on the outer face, the equilibria with a negative reaction are not admissible (Answers table) |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p49-top-view.svg]]

> [!derivation] Basis of S1: rotation by Omega t about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page. The figure measures $\Omega t$ from $\mathbf i_0$ towards $\mathbf j_0$, so $S_1$ turns counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Omega t$: hypotenuse 1, adjacent leg $\cos\Omega t$ along $\mathbf i_0$, opposite leg $\sin\Omega t$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\Omega t$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0, \quad \mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Omega t\cos\Omega t - \left(-\sin\Omega t\right)\sin\Omega t\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Omega t + \sin^2\Omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t = 0 \quad &\text{(rows times rows)} \\
> \mathbf r_1^A &= 2a\,\mathbf i_1 \quad &\text{($A$ at the distance $a$ outside the surface)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \cr \sin\Omega t & \cos\Omega t & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I, \quad \mathbf r_1^A = 2a\,\mathbf i_1}$$
>
> **Units:** $[\Omega t] = [1]$; $[a] = [\mathrm L]$
> **Meaning:** the vectors of $\mathcal B_1$ in terms of $\mathcal B_0$, which part (a) asks to define first; $A$ is at rest in $S_1$.

![[attachments/EM-SOL/p49-axis-view.svg]]

> [!derivation] The azimuth theta: view along OA
> **Law:** elementary rotation about $\mathbf i_1$; right triangle of the unit vector $\mathbf u$
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.5; Problems.pdf, p. 34
>
> View along $OA$, with $\mathbf i_1$ out of the paper (⊙). With $\mathbf j_1$ to the right, $\mathbf k_1$, the cross product of $\mathbf i_1$ and $\mathbf j_1$, points up the page. The azimuth starts at $\mathbf j_1$ (equatorial plane) and grows counterclockwise towards $\mathbf k_1$. The unit vector $\mathbf u$ of the plane of $\mathbf j_1$ and $\mathbf k_1$ in the direction $\theta$ is the hypotenuse of the shaded triangle: adjacent leg $\cos\theta$ along $\mathbf j_1$, opposite leg $\sin\theta$ along $\mathbf k_1$. $\mathbf e_\theta$ is $\mathbf u$ turned a further quarter turn counterclockwise; that carries its tip to the side of minus $\mathbf j_1$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf u &= \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1 \quad &\text{(shaded triangle)} \\
> \mathbf e_\theta &= \frac{d\mathbf u}{d\theta} = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \quad &\text{($\tfrac{d}{d\theta}\cos\theta = -\sin\theta$, $\tfrac{d}{d\theta}\sin\theta = \cos\theta$)} \\
> \mathbf u\cdot\mathbf e_\theta &= -\cos\theta\sin\theta + \sin\theta\cos\theta = 0, \quad \frac{d\mathbf e_\theta}{d\theta} = -\cos\theta\,\mathbf j_1 - \sin\theta\,\mathbf k_1 = -\mathbf u \quad &\text{(orthogonal; second derivative)}
> \end{aligned}$$
>
> $$\boxed{\mathbf u = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1, \qquad \mathbf e_\theta = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1}$$
>
> **Units:** $[\theta] = [1]$
> **Meaning:** $\mathbf u$ points from the axis $OA$ towards the projection $P'$ of the particle; $\mathbf e_\theta$ is the direction in which the particle moves when only $\theta$ grows.

![[attachments/EM-SOL/p49-meridian.svg]]

> [!derivation] The polar angle phi: meridian plane, position and spherical basis
> **Law:** right triangle of the radius; tangent vectors as derivatives of the radial unit vector; determinant by cofactors
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 34
>
> The meridian plane of $P$ contains the axis $OA$ and $\mathbf u$; it is drawn with $\mathbf i_1$ to the right and $\mathbf u$ up, so $\mathbf e_\theta$ points out of the paper. In the shaded right triangle the hypotenuse is $OP$, of length $a$; the leg adjacent to $\phi$ is $a\cos\phi$ along $\mathbf i_1$ and the opposite leg is $a\sin\phi$ along $\mathbf u$, the distance $OP'$ of the axis view. This is the usual spherical system with its polar axis along $OA$: the usual roles of $\mathbf k$, $\mathbf i$, $\mathbf j$ are taken by $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$, a cyclic permutation, which keeps the triad right-handed. The determinant of the matrix whose columns are $\mathbf e_r$, $\mathbf e_\phi$, $\mathbf e_\theta$ is expanded along its first row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf u = \cos\phi\,\mathbf i_1 + \sin\phi\cos\theta\,\mathbf j_1 + \sin\phi\sin\theta\,\mathbf k_1, \quad \mathbf r_1^P = a\,\mathbf e_r \quad &\text{(meridian triangle; Eq. 3.16)} \\
> \mathbf e_\phi &= \frac{\partial\mathbf e_r}{\partial\phi} = -\sin\phi\,\mathbf i_1 + \cos\phi\cos\theta\,\mathbf j_1 + \cos\phi\sin\theta\,\mathbf k_1 \quad &\text{(derivative in $\phi$; unit length)} \\
> \frac{\partial\mathbf e_r}{\partial\theta} &= \sin\phi\,\frac{d\mathbf u}{d\theta} = \sin\phi\,\mathbf e_\theta \quad &\text{(derivative in $\theta$; length $\sin\phi$)} \\
> \det\left[\mathbf e_r\ \mathbf e_\phi\ \mathbf e_\theta\right] &= (+1)\cos\phi\left(\cos\phi\cos^2\theta + \cos\phi\sin^2\theta\right) + (-1)\left(-\sin\phi\right)\left(\sin\phi\cos^2\theta + \sin\phi\sin^2\theta\right) + (+1)\cdot 0 = 1 \quad &\text{(first row; cofactor signs)} \\
> \mathbf e_r\cdot\mathbf e_\phi &= -\cos\phi\sin\phi + \sin\phi\cos\phi\left(\cos^2\theta + \sin^2\theta\right) = 0, \quad \mathbf e_r\cdot\mathbf e_\theta = \mathbf e_\phi\cdot\mathbf e_\theta = 0 \quad &\text{(orthogonality)} \\
> \mathbf i_1 &= \cos\phi\,\mathbf e_r - \sin\phi\,\mathbf e_\phi, \quad \mathbf k_1 = \sin\phi\sin\theta\,\mathbf e_r + \cos\phi\sin\theta\,\mathbf e_\phi + \cos\theta\,\mathbf e_\theta \quad &\text{(projections: third components of the three vectors)} \\
> \mathbf e_r &= \left(\cos\Omega t\cos\phi - \sin\Omega t\sin\phi\cos\theta\right)\mathbf i_0 + \left(\sin\Omega t\cos\phi + \cos\Omega t\sin\phi\cos\theta\right)\mathbf j_0 + \sin\phi\sin\theta\,\mathbf k_0 \quad &\text{($[{}_0R_1]$ times the components)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = a\,\mathbf e_r, \quad \mathbf e_r = \cos\phi\,\mathbf i_1 + \sin\phi\cos\theta\,\mathbf j_1 + \sin\phi\sin\theta\,\mathbf k_1, \cr \mathbf e_\phi = -\sin\phi\,\mathbf i_1 + \cos\phi\cos\theta\,\mathbf j_1 + \cos\phi\sin\theta\,\mathbf k_1, \quad \mathbf e_\theta = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[\mathbf e_r] = [\mathbf e_\phi] = [\mathbf e_\theta] = [1]$
> **Meaning:** a right-handed orthonormal basis at $P$, written in $\mathcal B_1$ and, through $[{}_0R_1]$, in $\mathcal B_0$; with the polar axis along $OA$ the distance to $A$ depends on $\phi$ only.

### Kinematics

> [!derivation] Motion of S1 and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \mathbf 0, \quad \mathbf v_0^O = \mathbf a_0^O = \mathbf 0 \quad &\text{(rotation about the fixed vertical; $\Omega$ constant; $O$ fixed)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf k_1\times\mathbf i_1 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \Omega\,\mathbf k_1\times\mathbf j_1 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0\right) &= -\Omega\sin\Omega t\,\mathbf i_0 + \Omega\cos\Omega t\,\mathbf j_0 = \Omega\,\mathbf j_1 \quad &\text{(check: chain rule on $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\Omega] = [\mathrm T^{-1}]$
> **Meaning:** in $S_1$ the three unit vectors are constant; in $S_0$ the two horizontal ones turn with the sphere.

#### (a) Position, velocity and acceleration of P in S1

> [!derivation] Derivatives of the spherical basis and relative kinematics
> **Law:** time derivatives in $S_1$; chain rule through $\phi(t)$ and $\theta(t)$; product rule
> **Source:** Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 34
>
> $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ are constant in $S_1$, so the spherical vectors change only through the two angles.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf e_r}{dt}\right|_1 &= \frac{\partial\mathbf e_r}{\partial\phi}\dot\phi + \frac{\partial\mathbf e_r}{\partial\theta}\dot\theta = \dot\phi\,\mathbf e_\phi + \sin\phi\,\dot\theta\,\mathbf e_\theta \quad &\text{(chain rule)} \\
> \left.\frac{d\mathbf e_\phi}{dt}\right|_1 &= \left(-\cos\phi\,\mathbf i_1 - \sin\phi\,\mathbf u\right)\dot\phi + \cos\phi\,\frac{d\mathbf u}{d\theta}\,\dot\theta = -\dot\phi\,\mathbf e_r + \cos\phi\,\dot\theta\,\mathbf e_\theta \quad &\text{(chain rule; $\mathbf e_\phi = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf u$)} \\
> \left.\frac{d\mathbf e_\theta}{dt}\right|_1 &= \frac{d\mathbf e_\theta}{d\theta}\,\dot\theta = -\dot\theta\,\mathbf u = -\sin\phi\,\dot\theta\,\mathbf e_r - \cos\phi\,\dot\theta\,\mathbf e_\phi \quad &\text{(chain rule; $\mathbf u = \sin\phi\,\mathbf e_r + \cos\phi\,\mathbf e_\phi$)} \\
> \mathbf v_1^P &= a\left.\frac{d\mathbf e_r}{dt}\right|_1 = a\dot\phi\,\mathbf e_\phi + a\sin\phi\,\dot\theta\,\mathbf e_\theta \quad &\text{($a$ constant)} \\
> \frac{d}{dt}\left(a\dot\phi\,\mathbf e_\phi\right) &= a\ddot\phi\,\mathbf e_\phi - a\dot\phi^2\,\mathbf e_r + a\cos\phi\,\dot\phi\dot\theta\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \frac{d}{dt}\left(a\sin\phi\,\dot\theta\,\mathbf e_\theta\right) &= a\left(\cos\phi\,\dot\phi\dot\theta + \sin\phi\,\ddot\theta\right)\mathbf e_\theta - a\sin^2\phi\,\dot\theta^2\,\mathbf e_r - a\sin\phi\cos\phi\,\dot\theta^2\,\mathbf e_\phi \quad &\text{(product rule, chain rule on $\sin\phi$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = a\,\mathbf e_r, \qquad \mathbf v_1^P = a\dot\phi\,\mathbf e_\phi + a\sin\phi\,\dot\theta\,\mathbf e_\theta, \cr \mathbf a_1^P = -a\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right)\mathbf e_r + a\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right)\mathbf e_\phi + a\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right)\mathbf e_\theta \end{gathered}}$$
>
> **Units:** $[a\dot\phi] = [\mathrm{L\,T^{-1}}]$; $[a\dot\phi^2] = [a\ddot\phi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the relative velocity is tangent to the sphere; the radial part of the relative acceleration is the centripetal one of the motion on the sphere.

> [!derivation] Absolute acceleration: transport and Coriolis terms as they arise
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position as $x_1\,\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1$, the components of $a\,\mathbf e_r$; their time derivatives are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1 + x_1\Omega\,\mathbf j_1 - y_1\Omega\,\mathbf i_1 = \mathbf v_1^P + \Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(product rule; the basis turns inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left[\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right)\right] &= \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(product rule; $\Omega$ constant)} \\
> 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P &= 2\Omega\,\mathbf k_1\times\left(\dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1\right) = 2\Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(the two equal terms: Coriolis)} \\
> \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) &= \Omega\,\mathbf k_1\times\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) = -\Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) = -\Omega^2\left(\mathbf r_1^P - z_1\,\mathbf k_1\right) \quad &\text{(the last term: centripetal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P - \Omega^2\left(\mathbf r_1^P - z_1\,\mathbf k_1\right) + 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P, \qquad z_1 = a\sin\phi\sin\theta}$$
>
> **Units:** $[\Omega^2 a] = [\Omega a\dot\phi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the centripetal term points horizontally to the vertical axis; with $O$ fixed and the rate constant there are no origin or Euler terms.

### Forces and Equations of Motion

![[attachments/EM-SOL/p49-fbd.svg]]

#### (b) Forces, vector equation and two scalar equations

> [!derivation] Actual and inertia forces in the spherical basis
> **Law:** linear attraction towards $A$; smooth reaction along the normal; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.11; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]; Problems.pdf, p. 34
>
> The vector products with $\mathbf k_1$ are determinants in the right-handed basis $\{\mathbf e_r, \mathbf e_\phi, \mathbf e_\theta\}$, with the components of $\mathbf k_1$ in the second row, expanded along the first row with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf F_k &= k\left(\mathbf r_1^A - \mathbf r_1^P\right) = k\left(2a\,\mathbf i_1 - a\,\mathbf e_r\right) = ka\left(2\cos\phi - 1\right)\mathbf e_r - 2ka\sin\phi\,\mathbf e_\phi \quad &\text{($\mathbf i_1$ in the spherical basis)} \\
> \mathbf N &= N\,\mathbf e_r, \quad \mathbf F_A = \mathbf 0, \quad \mathbf F_E = \mathbf 0 \quad &\text{(smooth sphere; $O$ fixed; $\Omega$ constant)} \\
> \mathbf F_C &= -m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = m\Omega^2\left(a\,\mathbf e_r - a\sin\phi\sin\theta\,\mathbf k_1\right) \quad &\text{(centripetal term times $-m$)} \\
> &= m\Omega^2a\left[\left(1 - \sin^2\phi\sin^2\theta\right)\mathbf e_r - \sin\phi\cos\phi\sin^2\theta\,\mathbf e_\phi - \sin\phi\sin\theta\cos\theta\,\mathbf e_\theta\right] \quad &\text{($\mathbf k_1$ in the spherical basis)} \\
> \mathbf k_1\times\mathbf e_\phi &= \begin{vmatrix} \mathbf e_r & \mathbf e_\phi & \mathbf e_\theta \cr \sin\phi\sin\theta & \cos\phi\sin\theta & \cos\theta \cr 0 & 1 & 0 \end{vmatrix} = (+1)\left(-\cos\theta\right)\mathbf e_r + (-1)(0)\,\mathbf e_\phi + (+1)\sin\phi\sin\theta\,\mathbf e_\theta \quad &\text{(first row; cofactor signs)} \\
> \mathbf k_1\times\mathbf e_\theta &= \begin{vmatrix} \mathbf e_r & \mathbf e_\phi & \mathbf e_\theta \cr \sin\phi\sin\theta & \cos\phi\sin\theta & \cos\theta \cr 0 & 0 & 1 \end{vmatrix} = (+1)\cos\phi\sin\theta\,\mathbf e_r + (-1)\sin\phi\sin\theta\,\mathbf e_\phi + (+1)(0)\,\mathbf e_\theta \quad &\text{(first row; cofactor signs)} \\
> \mathbf F_{COR} &= -2m\Omega\,\mathbf k_1\times\left(a\dot\phi\,\mathbf e_\phi + a\sin\phi\,\dot\theta\,\mathbf e_\theta\right) \quad &\text{(Coriolis term times $-m$)} \\
> &= 2m\Omega a\left[\left(\cos\theta\,\dot\phi - \sin\phi\cos\phi\sin\theta\,\dot\theta\right)\mathbf e_r + \sin^2\phi\sin\theta\,\dot\theta\,\mathbf e_\phi - \sin\phi\sin\theta\,\dot\phi\,\mathbf e_\theta\right] \quad &\text{(the two products above)}
> \end{aligned}$$
>
> $$\boxed{m\,\mathbf a_1^P = k\left(2a\,\mathbf i_1 - a\,\mathbf e_r\right) + N\,\mathbf e_r - m\,\boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) - 2m\,\boldsymbol\omega_{10}\times\mathbf v_1^P}$$
>
> **Units:** $[ka] = [m\Omega^2a] = [m\Omega a\dot\phi] = [N] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** one actual applied force, the reaction and two inertia forces; the attraction lies in the meridian plane, the centrifugal force is horizontal and away from the axis, the Coriolis force is normal to the relative velocity.

> [!derivation] Projections on the two tangent vectors
> **Law:** Newton's second law in a non-inertial frame projected on $\mathbf e_\phi$ and $\mathbf e_\theta$, which are normal to the reaction
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 3, Slide 14]; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> \mathbf e_\phi:\quad ma\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right) &= -2ka\sin\phi - m\Omega^2a\sin\phi\cos\phi\sin^2\theta + 2m\Omega a\sin^2\phi\sin\theta\,\dot\theta \quad &\text{(attraction, centrifugal, Coriolis)} \\
> \mathbf e_\theta:\quad ma\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right) &= -m\Omega^2a\sin\phi\sin\theta\cos\theta - 2m\Omega a\sin\phi\sin\theta\,\dot\phi \quad &\text{(centrifugal, Coriolis)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \ddot\phi - \sin\phi\cos\phi\,\dot\theta^2 = -\frac{2k}{m}\sin\phi - \Omega^2\sin\phi\cos\phi\sin^2\theta + 2\Omega\sin^2\phi\sin\theta\,\dot\theta \cr \sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta = -\Omega^2\sin\phi\sin\theta\cos\theta - 2\Omega\sin\phi\sin\theta\,\dot\phi \end{gathered}}$$
>
> **Units:** $[k/m] = [\Omega^2] = [\Omega\dot\theta] = [\ddot\phi] = [\mathrm T^{-2}]$
> **Meaning:** two second-order equations for the two angles, free of the reaction; the projection on $\mathbf e_r$ gives the reaction in part (e). Away from the poles of the coordinates, where the sine of $\phi$ vanishes, the second equation may be divided by that sine.

### Answers and Checks

#### (c) Mechanical energy in S1

> [!derivation] Why the energy in S1 is conserved, and its expression
> **Law:** power of each force on the relative velocity; potentials of the attraction and of the centrifugal force
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.31; [Lecture 5, Slide 29]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Yes, for two reasons. First, the forces that do no work in $S_1$: the reaction (the sphere is at rest in $S_1$ and smooth, so the reaction is normal to the relative velocity), the Coriolis force (normal to the relative velocity), and the origin and Euler forces, which vanish. Second, the forces that work have potentials of the position in $S_1$: the attraction, because $A$ is at rest in $S_1$, and the centrifugal force, because the rate is constant and the axis fixed. The squared distance to the vertical axis is the squared radius minus the square of $z_1$.
>
> $$\begin{aligned}
> \mathbf N\cdot\mathbf v_1^P &= N\,\mathbf e_r\cdot\left(a\dot\phi\,\mathbf e_\phi + a\sin\phi\,\dot\theta\,\mathbf e_\theta\right) = 0 \quad &\text{(no power)} \\
> \mathbf F_{COR}\cdot\mathbf v_1^P &= 2m\Omega a^2\left(\sin^2\phi\sin\theta\,\dot\theta\,\dot\phi - \sin\phi\sin\theta\,\dot\phi\,\sin\phi\,\dot\theta\right) = 0 \quad &\text{(components of the two boxes)} \\
> \left|\mathbf r_1^P - \mathbf r_1^A\right|^2 &= a^2 - 4a^2\,\mathbf e_r\cdot\mathbf i_1 + 4a^2 = 5a^2 - 4a^2\cos\phi \quad &\text{(square of the difference)} \\
> V_1 &= \tfrac12 k\left(5a^2 - 4a^2\cos\phi\right) - \tfrac12 m\Omega^2\left(a^2 - a^2\sin^2\phi\sin^2\theta\right) \quad &\text{(Eq. 4.14; Slide 30)} \\
> T_1 &= \tfrac12 m\left|\mathbf v_1^P\right|^2 = \tfrac12 ma^2\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) \quad &\text{(orthonormal components)} \\
> \frac{d}{dt}\left(T_1 + V_1\right) &= ma^2\dot\phi\left(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2\right) + ma^2\sin\phi\,\dot\theta\left(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta\right) + 2ka^2\sin\phi\,\dot\phi + m\Omega^2a^2\left(\sin\phi\cos\phi\sin^2\theta\,\dot\phi + \sin^2\phi\sin\theta\cos\theta\,\dot\theta\right) \quad &\text{(chain rule; terms regrouped)} \\
> &= a\dot\phi\left(2m\Omega a\sin^2\phi\sin\theta\,\dot\theta\right) + a\sin\phi\,\dot\theta\left(-2m\Omega a\sin\phi\sin\theta\,\dot\phi\right) = 0 \quad &\text{(the two equations of part (b))}
> \end{aligned}$$
>
> $$\boxed{\mathcal E_1 = \frac12 ma^2\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) - 2ka^2\cos\phi + \frac12 m\Omega^2a^2\sin^2\phi\sin^2\theta = \text{const}}$$
>
> **Units:** $[ma^2\dot\phi^2] = [ka^2] = [m\Omega^2a^2] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the constant terms of the potential are dropped; the constant is fixed by initial conditions, which the statement does not give. What is left of the check is exactly the power of the Coriolis force, which vanishes.

#### (d) Equilibrium configurations

> [!derivation] Relative equilibria away from the poles of the coordinates
> **Law:** constant coordinates, so the rates and accelerations vanish in the two equations of part (b)
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 34
>
> With $\Lambda$ the ratio of $m\Omega^2$ to $k$, and the sine of $\phi$ not zero:
>
> $$\begin{aligned}
> \mathbf e_\theta:\quad 0 &= -\Omega^2\sin\phi\sin\theta\cos\theta \;\Rightarrow\; \sin\theta = 0 \ \text{ or } \ \cos\theta = 0 \quad &\text{($\Omega \ne 0$, $\sin\phi \ne 0$)} \\
> \mathbf e_\phi:\quad 0 &= -\sin\phi\left(2k + m\Omega^2\cos\phi\sin^2\theta\right) \;\Rightarrow\; 2 + \Lambda\cos\phi\sin^2\theta = 0 \quad &\text{(divided by $-k\sin\phi$)} \\
> \sin\theta = 0:\quad 2 &= 0 \quad &\text{(impossible: no equilibrium off the axis in the equatorial plane)} \\
> \cos\theta = 0,\ \sin^2\theta = 1:\quad \cos\phi^* &= -\frac{2}{\Lambda} = -\frac{2k}{m\Omega^2} \quad &\text{(needs $\Lambda \gt 2$ for $\sin\phi^* \ne 0$)} \\
> \mathbf r_1^P &= a\cos\phi^*\,\mathbf i_1 \pm a\sin\phi^*\,\mathbf k_1 = -\frac{2a}{\Lambda}\,\mathbf i_1 \pm a\sqrt{1 - \frac{4}{\Lambda^2}}\,\mathbf k_1 \quad &\text{($\theta = \pm\tfrac{\pi}{2}$, $\sin\phi^* \gt 0$)}
> \end{aligned}$$
>
> $$\boxed{E_3, E_4:\ \theta = \pm\frac{\pi}{2}, \ \cos\phi^* = -\frac{2k}{m\Omega^2}, \ \text{only for } \frac{m\Omega^2}{k} \gt 2}$$
>
> **Units:** $[2k/(m\Omega^2)] = [1]$
> **Meaning:** these two equilibria lie in the meridian plane through $A$ and the axis, on the half of the sphere away from $A$, one above and one below the equator.

> [!derivation] The poles of the coordinates and the reaction at each equilibrium
> **Law:** full vector balance of the forces at rest (the angle $\theta$ is undefined at the poles of the coordinates)
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Sec. 4.6
>
> At rest the Coriolis force vanishes; the applied force and the centrifugal force must be balanced by the radial reaction alone. At the equilibria of the previous box the centrifugal force is the product of $m\Omega^2$, which is $\Lambda k$, and the horizontal part $x_1\,\mathbf i_1$ of the position, with $x_1$ equal to $-2a/\Lambda$.
>
> $$\begin{aligned}
> E_1,\ \mathbf r_1^P = a\,\mathbf i_1:\quad \mathbf F_k + \mathbf F_C &= k\left(2a - a\right)\mathbf i_1 + m\Omega^2a\,\mathbf i_1 = \left(k + m\Omega^2\right)a\,\mathbf e_r \;\Rightarrow\; N = -\left(k + m\Omega^2\right)a \quad &\text{(both forces radial, along $\mathbf e_r = \mathbf i_1$)} \\
> E_2,\ \mathbf r_1^P = -a\,\mathbf i_1:\quad \mathbf F_k + \mathbf F_C &= k\left(2a + a\right)\mathbf i_1 - m\Omega^2a\,\mathbf i_1 = -\left(3k - m\Omega^2\right)a\,\mathbf e_r \;\Rightarrow\; N = \left(3k - m\Omega^2\right)a \quad &\text{(radial, along $\mathbf e_r = -\mathbf i_1$)} \\
> E_3, E_4:\quad \mathbf F_k + \mathbf F_C &= k\left(2a\,\mathbf i_1 - \mathbf r_1^P\right) + \Lambda k\left(-\frac{2a}{\Lambda}\right)\mathbf i_1 = -k\,\mathbf r_1^P = -ka\,\mathbf e_r \;\Rightarrow\; N = ka \quad &\text{(the horizontal pulls cancel)}
> \end{aligned}$$
>
> $$\boxed{E_1:\ N = -\left(k + m\Omega^2\right)a, \qquad E_2:\ N = \left(3k - m\Omega^2\right)a, \qquad E_3, E_4:\ N = ka}$$
>
> **Units:** $[ka] = [m\Omega^2a] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** $E_1$ (the point nearest $A$) and $E_2$ (the farthest) exist for every rate, because there both forces are radial. At $E_1$ the reaction points inwards: the sphere must pull the particle in, which needs the bilateral contact of the readings. At $E_3$ and $E_4$ the reaction points outwards.

#### (e) Reaction of the sphere

> [!derivation] Projection on the normal
> **Law:** Newton's second law in $S_1$ projected on $\mathbf e_r$, the only projection that contains $N$
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> \mathbf e_r:\quad -ma\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) &= N + ka\left(2\cos\phi - 1\right) + m\Omega^2a\left(1 - \sin^2\phi\sin^2\theta\right) + 2m\Omega a\left(\cos\theta\,\dot\phi - \sin\phi\cos\phi\sin\theta\,\dot\theta\right) \quad &\text{(radial components of part (b))} \\
> \phi = 0, \ \dot\phi = \dot\theta = 0:\quad N &= -ka - m\Omega^2a \quad &\text{(check: equals the value at $E_1$)} \\
> \phi = \pi, \ \dot\phi = \dot\theta = 0:\quad N &= -\left[ka\left(-2 - 1\right) + m\Omega^2a\right] = \left(3k - m\Omega^2\right)a \quad &\text{(check: equals the value at $E_2$)} \\
> E_3, E_4:\quad N &= -\left[ka\left(-\frac{4}{\Lambda} - 1\right) + m\Omega^2a\,\frac{4}{\Lambda^2}\right] = ka + \frac{4ka}{\Lambda} - \frac{4ka}{\Lambda} = ka \quad &\text{(check: $\sin^2\theta = 1$, $1 - \sin^2\phi^* = \cos^2\phi^*$, $m\Omega^2 = \Lambda k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = -\left[ma\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) + ka\left(2\cos\phi - 1\right) + m\Omega^2a\left(1 - \sin^2\phi\sin^2\theta\right) + 2m\Omega a\left(\cos\theta\,\dot\phi - \sin\phi\cos\phi\sin\theta\,\dot\theta\right)\right]\mathbf e_r}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** once the two angles are known as functions of time, the reaction follows; $\mathbf e_r$ in terms of $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ is in the meridian box.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Kinematics in $S_1$ | $\mathbf r_1^P = a\,\mathbf e_r$, $\mathbf v_1^P = a\dot\phi\,\mathbf e_\phi + a\sin\phi\,\dot\theta\,\mathbf e_\theta$, $\mathbf a_1^P = -a(\dot\phi^2 + \sin^2\phi\,\dot\theta^2)\,\mathbf e_r + a(\ddot\phi - \sin\phi\cos\phi\,\dot\theta^2)\,\mathbf e_\phi + a(\sin\phi\,\ddot\theta + 2\cos\phi\,\dot\phi\dot\theta)\,\mathbf e_\theta$; $\mathbf i_1 = \cos\Omega t\,\mathbf i_0 + \sin\Omega t\,\mathbf j_0$, $\mathbf j_1 = -\sin\Omega t\,\mathbf i_0 + \cos\Omega t\,\mathbf j_0$, $\mathbf k_1 = \mathbf k_0$, spherical vectors as boxed |
| (b) Forces and equations | $\mathbf F_k = k(2a\,\mathbf i_1 - a\,\mathbf e_r)$, $\mathbf N = N\,\mathbf e_r$, $\mathbf F_C = m\Omega^2(\mathbf r_1^P - z_1\mathbf k_1)$, $\mathbf F_{COR} = -2m\Omega\,\mathbf k_1\times\mathbf v_1^P$; the two boxed scalar equations of part (b) |
| (c) Energy in $S_1$ | conserved: $\frac12 ma^2(\dot\phi^2 + \sin^2\phi\,\dot\theta^2) - 2ka^2\cos\phi + \frac12 m\Omega^2a^2\sin^2\phi\sin^2\theta = \text{const}$ |
| (d) Equilibria | $E_1$: $\phi = 0$ (point nearest $A$), $E_2$: $\phi = \pi$ (farthest point), for every $m\Omega^2/k$; $E_3$, $E_4$: $\theta = \pm\pi/2$, $\cos\phi = -2k/(m\Omega^2)$, only when $m\Omega^2/k \gt 2$; they branch off $E_2$ at the value 2 and tend to the top and bottom of the sphere as the ratio grows. In the other reading of the angles (azimuth $\phi$ in the equator, latitude $\theta$): $E_1$ at $(0, 0)$, $E_2$ at $(\pi, 0)$, $E_3$, $E_4$ at $\phi = \pi$, $\theta = \pm\arccos(2k/(m\Omega^2))$. With a one-sided contact on the outer face (reaction outwards only), $E_1$ is not admissible, and $E_2$ only when $m\Omega^2 \le 3k$ |
| (e) Reaction | $\mathbf N = -[ma(\dot\phi^2 + \sin^2\phi\,\dot\theta^2) + ka(2\cos\phi - 1) + m\Omega^2a(1 - \sin^2\phi\sin^2\theta) + 2m\Omega a(\cos\theta\,\dot\phi - \sin\phi\cos\phi\sin\theta\,\dot\theta)]\,\mathbf e_r$ |

**Check against the official key:** Problems.pdf, p. 76 prints no answer for problem 49. Independent checks: the energy of part (c) is constant along the equations of part (b), the reaction of part (e) gives at rest the values of the vector balance at the equilibria, and the limiting cases follow.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data
> **Source:** Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega \to 0:\quad \mathcal E_1 &= \tfrac12 ma^2\left(\dot\phi^2 + \sin^2\phi\,\dot\theta^2\right) - 2ka^2\cos\phi \quad &\text{(fixed sphere: only the attraction works)} \\
> \Lambda \to 2^+:\quad \cos\phi^* &= -\frac{2}{\Lambda} \to -1 \quad &\text{($E_3$ and $E_4$ merge with $E_2$)} \\
> \Lambda \to \infty:\quad \cos\phi^* &\to 0, \quad \mathbf r_1^P \to \pm a\,\mathbf k_1 \quad &\text{($E_3$, $E_4$ tend to the top and bottom of the sphere)} \\
> E_3:\quad \left|\mathbf r_1^P\right|^2 &= \frac{4a^2}{\Lambda^2} + a^2\left(1 - \frac{4}{\Lambda^2}\right) = a^2 \quad &\text{(check: on the sphere)}
> \end{aligned}$$
>
> $$\boxed{\frac{m\Omega^2}{k} \le 2: \ E_1, E_2 \text{ only}; \qquad \frac{m\Omega^2}{k} \gt 2: \ E_1, E_2, E_3, E_4}$$
>
> **Units:** $[\Lambda] = [1]$
> **Meaning:** the rotation must be fast enough, compared with the stiffness of the attraction, for the centrifugal push away from the axis to balance the attraction off the line $OA$. The statement does not ask for stability, which is not discussed here.

---

## Problem 51: Particle inside a Hollow Sphere in a Rotating Frame

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ moves on the smooth inner surface of a hollow sphere of radius $R$ whose centre $C$ is at $R(\mathbf j_1 + \mathbf k_1)$ in the frame $S_1$. $S_1$ is not inertial: it turns with the known angular velocity $\Omega(t)\,\mathbf k_1$ (Problems.pdf, p. 36). The statement asks for the position, velocity and acceleration in $S_1$, all the forces seen from $S_1$, two equations for $\theta$ and $\phi$, the reaction and the condition for the particle to leave the surface, and the equilibria when the rate is constant. The sphere is at rest in $S_1$, so the solution works there, with the composition of motions of Notes.pdf, Sec. 3.2 and the inertia forces of Notes.pdf, Sec. 4.9; since the rate may change, the Euler force appears.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{A;\ \mathcal B_0\}$, $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, with $A$ the origin of $S_1$ (on the axis of rotation) and $\mathbf k_0 = \mathbf k_1$ |
| Moving frame | $S_1 = \{A;\ \mathcal B_1\}$ of the figure, $\mathbf k_1$ vertical, up; it has turned the angle $\Psi(t)$ about $\mathbf k_0$, from $\mathbf i_0$ towards $\mathbf j_0$, whose rate of change is $\Omega$; $S_1$ and $S_0$ coincide when $\Psi$ is zero |
| Sphere | centre $C$, $\mathbf r_1^C = R(\mathbf j_1 + \mathbf k_1)$, radius $R$, fixed in $S_1$; it touches the axis of rotation at $R\,\mathbf k_1$ and the plane $z_1 = 0$ at $R\,\mathbf j_1$ |
| Bases at $P$ | horizontal unit vector $\mathbf e_h$ from $C$ towards the projection $P'$ of $P$ on the horizontal plane through $C$; spherical basis $\{\mathbf u_r, \mathbf u_\theta, \mathbf u_\phi\}$ (deduced below) |
| Coordinates | $\theta$, azimuth of $CP'$ measured at $C$ from the direction of $\mathbf i_1$ towards $\mathbf j_1$; $\phi$, elevation of $CP$ above the horizontal plane through $C$ |
| Data | $m$ [kg], $R$ [m], $g$ [m s$^{-2}$], $\Omega(t)$ [rad s$^{-1}$] and its derivative $\dot\Omega(t)$ [rad s$^{-2}$] |
| Unknowns | $\theta(t)$, $\phi(t)$ and the reaction $-N\,\mathbf u_r$ |
| Applied force | weight $-mg\,\mathbf k_1$ |
| Inertia forces (in $S_1$) | Euler, centrifugal and Coriolis; no origin term (Notes.pdf, Eq. 4.62) |
| Hypotheses | $S_0$ inertial; uniform gravity; $A$ fixed; smooth surface; $\Omega(t)$ known |
| Readings | (1) Read from the figure: $\theta$ is drawn in the horizontal plane through $C$ from the direction of $\mathbf i_1$ towards the side of $\mathbf j_1$, and $\phi$ from that plane upwards. If $\phi$ were the colatitude (measured from $\mathbf k_1$ downwards), $\cos\phi$ and $\sin\phi$ would swap in every result. (2) The particle is inside the sphere and the statement asks when it separates, so the contact is read as one-sided: the reaction points towards $C$, written $-N\,\mathbf u_r$ with $N$ non-negative while in contact. For a contact that holds on both sides, every solution of part (e) would be admissible |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p51-top-view.svg]]

> [!derivation] Basis of S1: rotation by Psi about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; [Lecture 5, Slide 16]
>
> View from above, along $\mathbf k_0$, which points out of the paper (⊙). With $\mathbf i_0$ to the right, $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points up the page; a positive rate turns $S_1$ counterclockwise in this view. $\mathbf i_1$ is $\mathbf i_0$ turned by $\Psi$: hypotenuse 1, adjacent leg $\cos\Psi$ along $\mathbf i_0$, opposite leg $\sin\Psi$ along plus $\mathbf j_0$. $\mathbf j_1$ is $\mathbf j_0$ turned by the same angle; the counterclockwise turn carries its tip to the left, so its opposite leg $\sin\Psi$ lies along minus $\mathbf i_0$ (the minus sign).
>
> $$\begin{aligned}
> \dot\Psi &= \Omega(t) \quad &\text{(definition of the angle turned: $\Psi$ is an antiderivative of the known rate)} \\
> \mathbf i_1 &= \cos\Psi\,\mathbf i_0 + \sin\Psi\,\mathbf j_0, \quad \mathbf j_1 = -\sin\Psi\,\mathbf i_0 + \cos\Psi\,\mathbf j_0, \quad \mathbf k_1 = \mathbf k_0 \quad &\text{(the two right triangles; axis)} \\
> \det[{}_0R_1] &= (+1)\cdot 1\cdot\left(\cos\Psi\cos\Psi - \left(-\sin\Psi\right)\sin\Psi\right) = 1 \quad &\text{(expansion along the third row, cofactor sign $(-1)^{3+3}$)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\Psi + \sin^2\Psi = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = -\cos\Psi\sin\Psi + \sin\Psi\cos\Psi = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\Psi & -\sin\Psi & 0 \cr \sin\Psi & \cos\Psi & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[\Psi] = [1]$; $[\Omega\,t] = [1]$
> **Meaning:** the orientation of $S_1$ is known at every instant because the rate is known; the rate of change of the angle is the given rate.

![[attachments/EM-SOL/p51-horizontal.svg]]

> [!derivation] The azimuth theta: horizontal plane through C
> **Law:** right triangle of the horizontal unit vector; tangent vector as its derivative
> **Source:** Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.5; Problems.pdf, p. 36
>
> Seen from above ($\mathbf k_1$ out of the paper, ⊙), with $\mathbf i_1$ to the right and $\mathbf j_1$ up, the centre $C$ is at the distance $R$ from the axis of rotation, on the side of $\mathbf j_1$. The horizontal unit vector $\mathbf e_h$ at the azimuth $\theta$ is the hypotenuse of the shaded triangle: adjacent leg $\cos\theta$ along $\mathbf i_1$, opposite leg $\sin\theta$ along $\mathbf j_1$. $\mathbf u_\theta$ is $\mathbf e_h$ turned a further quarter turn counterclockwise, which carries its tip to the side of minus $\mathbf i_1$ (the minus sign).
>
> $$\begin{aligned}
> \mathbf e_h &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1 \quad &\text{(shaded triangle)} \\
> \mathbf u_\theta &= \frac{d\mathbf e_h}{d\theta} = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{($\tfrac{d}{d\theta}\cos\theta = -\sin\theta$, $\tfrac{d}{d\theta}\sin\theta = \cos\theta$)} \\
> \mathbf k_1\times\mathbf e_h &= \cos\theta\,\mathbf j_1 - \sin\theta\,\mathbf i_1 = \mathbf u_\theta, \quad \mathbf k_1\times\mathbf u_\theta = -\sin\theta\,\mathbf j_1 - \cos\theta\,\mathbf i_1 = -\mathbf e_h \quad &\text{($\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \mathbf i_1 &= \cos\theta\,\mathbf e_h - \sin\theta\,\mathbf u_\theta, \quad \mathbf j_1 = \sin\theta\,\mathbf e_h + \cos\theta\,\mathbf u_\theta \quad &\text{(projections)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_h = \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \qquad \mathbf u_\theta = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1}$$
>
> **Units:** $[\theta] = [1]$
> **Meaning:** $\mathbf e_h$ points from $C$ towards the projection $P'$; $\mathbf u_\theta$ is the horizontal direction in which $P$ moves when only $\theta$ grows.

![[attachments/EM-SOL/p51-vertical.svg]]

> [!derivation] The elevation phi: vertical plane through C and P, position and spherical basis
> **Law:** right triangle of the radius $CP$; vector sum of positions; determinant by cofactors
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 3.16; Problems.pdf, p. 36
>
> The vertical plane through $C$ that contains $\mathbf e_h$ is drawn with $\mathbf e_h$ to the right and $\mathbf k_1$ up; the cross product of $\mathbf e_h$ and $\mathbf k_1$ is minus $\mathbf u_\theta$, so $\mathbf u_\theta$ points into the paper (⊗). In the shaded right triangle the hypotenuse is $CP$, of length $R$; the leg adjacent to $\phi$ is $R\cos\phi$ along $\mathbf e_h$ (the distance $CP'$ of the horizontal view) and the opposite leg is $R\sin\phi$ along $\mathbf k_1$. $\mathbf u_\phi$ is $\mathbf u_r$ turned a quarter turn counterclockwise in this view, which carries its tip to the side of minus $\mathbf e_h$ (the minus sign). The usual spherical polar angle is measured from $\mathbf k_1$ downwards and equals a quarter turn minus $\phi$, so its sine is $\cos\phi$ and its cosine $\sin\phi$ (difference formulas). The distance that stays constant is $CP$, so the path goes from $A$ to $C$ and then to $P$. The determinant of the matrix whose columns are $\mathbf u_r$, $\mathbf u_\theta$, $\mathbf u_\phi$ is expanded along the third row, with the cofactor signs plus, minus, plus.
>
> $$\begin{aligned}
> \mathbf u_r &= \cos\phi\,\mathbf e_h + \sin\phi\,\mathbf k_1 = \cos\phi\cos\theta\,\mathbf i_1 + \cos\phi\sin\theta\,\mathbf j_1 + \sin\phi\,\mathbf k_1 \quad &\text{(shaded triangle; $\mathbf e_h$ in $\mathcal B_1$)} \\
> \mathbf u_\phi &= \frac{\partial\mathbf u_r}{\partial\phi} = -\sin\phi\,\mathbf e_h + \cos\phi\,\mathbf k_1 = -\sin\phi\cos\theta\,\mathbf i_1 - \sin\phi\sin\theta\,\mathbf j_1 + \cos\phi\,\mathbf k_1 \quad &\text{(derivative in $\phi$)} \\
> \frac{\partial\mathbf u_r}{\partial\theta} &= \cos\phi\,\frac{d\mathbf e_h}{d\theta} = \cos\phi\,\mathbf u_\theta \quad &\text{(derivative in $\theta$; length $\cos\phi$)} \\
> \det\left[\mathbf u_r\ \mathbf u_\theta\ \mathbf u_\phi\right] &= (+1)\sin\phi\left(\sin\phi\sin^2\theta + \sin\phi\cos^2\theta\right) + (-1)\cdot 0 + (+1)\cos\phi\left(\cos\phi\cos^2\theta + \cos\phi\sin^2\theta\right) = 1 \quad &\text{(third row; cofactor signs)} \\
> \mathbf u_r\cdot\mathbf u_\phi &= -\cos\phi\sin\phi + \sin\phi\cos\phi = 0, \quad \mathbf u_r\cdot\mathbf u_\theta = \mathbf u_\phi\cdot\mathbf u_\theta = 0 \quad &\text{(orthogonality)} \\
> \mathbf e_h &= \cos\phi\,\mathbf u_r - \sin\phi\,\mathbf u_\phi, \quad \mathbf k_1 = \sin\phi\,\mathbf u_r + \cos\phi\,\mathbf u_\phi \quad &\text{(projections)} \\
> \mathbf r_1^P &= \overrightarrow{AC} + \overrightarrow{CP} = R\left(\mathbf j_1 + \mathbf k_1\right) + R\,\mathbf u_r \quad &\text{(Eq. 3.16 with the origin $A$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = R\cos\phi\cos\theta\,\mathbf i_1 + R\left(1 + \cos\phi\sin\theta\right)\mathbf j_1 + R\left(1 + \sin\phi\right)\mathbf k_1, \cr \mathbf u_r = \cos\phi\cos\theta\,\mathbf i_1 + \cos\phi\sin\theta\,\mathbf j_1 + \sin\phi\,\mathbf k_1, \quad \mathbf u_\theta = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1, \quad \mathbf u_\phi = -\sin\phi\cos\theta\,\mathbf i_1 - \sin\phi\sin\theta\,\mathbf j_1 + \cos\phi\,\mathbf k_1 \end{gathered}}$$
>
> **Units:** $[R] = [\mathrm L]$; the unit vectors $[1]$
> **Meaning:** a right-handed orthonormal basis at $P$; $\mathbf u_r$ points from $C$ to $P$, the outward normal of the sphere. The poles of the coordinates, where the cosine of $\phi$ vanishes, are the top and bottom points of the sphere.

### Kinematics

> [!derivation] Motion of S1 and derivatives of its unit vectors
> **Law:** angular velocity of a simple rotation; angular acceleration; derivative of a unit vector of a turning basis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 3.4; Notes.pdf, Eq. 3.5; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \Omega(t)\,\mathbf k_1, \quad \mathbf v_0^A = \mathbf a_0^A = \mathbf 0 \quad &\text{(rotation about the fixed vertical; $A$ fixed)} \\
> \boldsymbol\alpha_{10} &= \left.\frac{d\boldsymbol\omega_{10}}{dt}\right|_0 = \dot\Omega\,\mathbf k_1 + \Omega\left.\frac{d\mathbf k_1}{dt}\right|_0 = \dot\Omega\,\mathbf k_1 \quad &\text{(product rule; $\mathbf k_1$ does not turn)} \\
> \left.\frac{d\mathbf i_1}{dt}\right|_0 &= \Omega\,\mathbf k_1\times\mathbf i_1 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = \Omega\,\mathbf k_1\times\mathbf j_1 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 3.3 to 3.5)} \\
> \frac{d}{dt}\left(\cos\Psi\,\mathbf i_0 + \sin\Psi\,\mathbf j_0\right) &= \frac{d\Psi}{dt}\left(-\sin\Psi\,\mathbf i_0 + \cos\Psi\,\mathbf j_0\right) = \Omega\,\mathbf j_1 \quad &\text{(check: chain rule on $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{10} = \Omega\,\mathbf k_1, \quad \boldsymbol\alpha_{10} = \dot\Omega\,\mathbf k_1, \quad \left.\frac{d\mathbf i_1}{dt}\right|_0 = \Omega\,\mathbf j_1, \quad \left.\frac{d\mathbf j_1}{dt}\right|_0 = -\Omega\,\mathbf i_1, \quad \left.\frac{d\mathbf k_1}{dt}\right|_0 = \mathbf 0}$$
>
> **Units:** $[\Omega] = [\mathrm T^{-1}]$; $[\dot\Omega] = [\mathrm T^{-2}]$
> **Meaning:** the angular acceleration is along the fixed axis and vanishes only when the rate is constant.

#### (a) Position, velocity and acceleration of P in S1

> [!derivation] Derivatives of the spherical basis and relative kinematics
> **Law:** time derivatives in $S_1$; chain rule through $\theta(t)$ and $\phi(t)$; product rule
> **Source:** Notes.pdf, Eq. 3.16; Notes.pdf, Eq. 3.19; Notes.pdf, Eq. 3.24; Problems.pdf, p. 36
>
> $\mathbf r_1^C$ and $\mathbf k_1$ are constant in $S_1$; $\mathbf e_h$ and the spherical vectors change only through the two angles.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf u_r}{dt}\right|_1 &= \frac{\partial\mathbf u_r}{\partial\theta}\dot\theta + \frac{\partial\mathbf u_r}{\partial\phi}\dot\phi = \dot\theta\cos\phi\,\mathbf u_\theta + \dot\phi\,\mathbf u_\phi \quad &\text{(chain rule)} \\
> \left.\frac{d\mathbf u_\theta}{dt}\right|_1 &= \frac{d\mathbf u_\theta}{d\theta}\dot\theta = -\dot\theta\,\mathbf e_h = -\dot\theta\cos\phi\,\mathbf u_r + \dot\theta\sin\phi\,\mathbf u_\phi \quad &\text{(chain rule; $\mathbf e_h$ in the spherical basis)} \\
> \left.\frac{d\mathbf u_\phi}{dt}\right|_1 &= -\dot\phi\cos\phi\,\mathbf e_h - \sin\phi\,\dot\theta\,\mathbf u_\theta - \dot\phi\sin\phi\,\mathbf k_1 = -\dot\phi\,\mathbf u_r - \dot\theta\sin\phi\,\mathbf u_\theta \quad &\text{(product and chain rules on $-\sin\phi\,\mathbf e_h + \cos\phi\,\mathbf k_1$)} \\
> \mathbf v_1^P &= R\left.\frac{d\mathbf u_r}{dt}\right|_1 = R\dot\theta\cos\phi\,\mathbf u_\theta + R\dot\phi\,\mathbf u_\phi \quad &\text{($\mathbf r_1^C$ constant)} \\
> \frac{d}{dt}\left(R\dot\theta\cos\phi\,\mathbf u_\theta\right) &= R\left(\ddot\theta\cos\phi - \dot\theta\dot\phi\sin\phi\right)\mathbf u_\theta - R\dot\theta^2\cos^2\phi\,\mathbf u_r + R\dot\theta^2\sin\phi\cos\phi\,\mathbf u_\phi \quad &\text{(product rule; chain rule on $\cos\phi$)} \\
> \frac{d}{dt}\left(R\dot\phi\,\mathbf u_\phi\right) &= R\ddot\phi\,\mathbf u_\phi - R\dot\phi^2\,\mathbf u_r - R\dot\phi\dot\theta\sin\phi\,\mathbf u_\theta \quad &\text{(product rule)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_1^P = R\left(\mathbf j_1 + \mathbf k_1\right) + R\,\mathbf u_r, \qquad \mathbf v_1^P = R\dot\theta\cos\phi\,\mathbf u_\theta + R\dot\phi\,\mathbf u_\phi, \cr \mathbf a_1^P = -R\left(\dot\phi^2 + \dot\theta^2\cos^2\phi\right)\mathbf u_r + R\left(\ddot\theta\cos\phi - 2\dot\theta\dot\phi\sin\phi\right)\mathbf u_\theta + R\left(\ddot\phi + \dot\theta^2\sin\phi\cos\phi\right)\mathbf u_\phi \end{gathered}}$$
>
> **Units:** $[R\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[R\dot\phi^2] = [R\ddot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the relative velocity is tangent to the sphere; the radial part of the relative acceleration points to the centre $C$.

> [!derivation] Absolute acceleration: Euler, transport and Coriolis terms as they arise
> **Law:** time derivative in $S_0$ of the position written in the turning basis; product rule with a variable rate
> **Source:** Notes.pdf, Eq. 3.17; Notes.pdf, Eq. 3.21; Notes.pdf, Eq. 3.22; Notes.pdf, Eq. 3.23; Notes.pdf, Eq. 3.27; [Lecture 5, Slide 24]; [Lecture 5, Slide 25]
>
> Write the position as $x_1\,\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1$, with the components of the position box; their time derivatives are the components of the relative velocity.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \dot x_1\,\mathbf i_1 + \dot y_1\,\mathbf j_1 + \dot z_1\,\mathbf k_1 + x_1\Omega\,\mathbf j_1 - y_1\Omega\,\mathbf i_1 = \mathbf v_1^P + \Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(product rule; derivatives of $\mathbf i_1$, $\mathbf j_1$)} \\
> \left.\frac{d\mathbf v_1^P}{dt}\right|_0 &= \mathbf a_1^P + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(product rule; the basis turns inside $\mathbf v_1^P$)} \\
> \left.\frac{d}{dt}\right|_0\left[\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right)\right] &= \dot\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) + \Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) \quad &\text{(product rule; the rate changes)} \\
> \boldsymbol\alpha_{10}\times\mathbf r_1^P &= \dot\Omega\,\mathbf k_1\times\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1 + z_1\,\mathbf k_1\right) = \dot\Omega\left(x_1\,\mathbf j_1 - y_1\,\mathbf i_1\right) \quad &\text{(the new term: Euler)} \\
> \mathbf a_0^P &= \mathbf a_1^P + \dot\Omega\,\mathbf k_1\times\mathbf r_1^P - \Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right) + 2\Omega\left(\dot x_1\,\mathbf j_1 - \dot y_1\,\mathbf i_1\right) \quad &\text{(Euler; centripetal; Coriolis, the two equal terms)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \mathbf a_1^P + \boldsymbol\alpha_{10}\times\mathbf r_1^P + \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) + 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P, \qquad \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) = -\Omega^2\left(x_1\,\mathbf i_1 + y_1\,\mathbf j_1\right)}$$
>
> **Units:** $[\dot\Omega R] = [\Omega^2R] = [\Omega R\dot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** a changing rate adds the Euler term, horizontal and normal to the horizontal part of the position; the origin $A$ is fixed, so there is no origin term.

### Forces and Equations of Motion

![[attachments/EM-SOL/p51-fbd.svg]]

#### (b) Forces on P seen from S1

> [!derivation] Actual and inertia forces in the spherical basis
> **Law:** weight; one-sided smooth reaction towards the centre; inertia forces of a non-inertial frame
> **Source:** Notes.pdf, Eq. 4.62; Notes.pdf, Eq. 6.11; [Lecture 5, Slide 28]; [Lecture 5, Slide 30]; [Lecture 5, Slide 31]
>
> Only the horizontal part of the position, $x_1\,\mathbf i_1 + y_1\,\mathbf j_1$, enters the products with $\mathbf k_1$; call it $\mathbf r_\perp$. It is written in $\{\mathbf e_h, \mathbf u_\theta\}$ with the projections of the azimuth box, and then $\mathbf e_h$ in the spherical basis.
>
> $$\begin{aligned}
> \mathbf r_\perp &= R\cos\phi\cos\theta\left(\cos\theta\,\mathbf e_h - \sin\theta\,\mathbf u_\theta\right) + R\left(1 + \cos\phi\sin\theta\right)\left(\sin\theta\,\mathbf e_h + \cos\theta\,\mathbf u_\theta\right) = R\left(\cos\phi + \sin\theta\right)\mathbf e_h + R\cos\theta\,\mathbf u_\theta \quad &\text{(components collected)} \\
> \mathbf W &= -mg\,\mathbf k_1 = -mg\sin\phi\,\mathbf u_r - mg\cos\phi\,\mathbf u_\phi, \quad \mathbf N = -N\,\mathbf u_r \quad &\text{(weight; reaction towards $C$)} \\
> \mathbf F_A &= -m\,\mathbf a_0^A = \mathbf 0 \quad &\text{($A$ fixed)} \\
> \mathbf F_E &= -m\dot\Omega\,\mathbf k_1\times\mathbf r_\perp = -m\dot\Omega R\left[\left(\cos\phi + \sin\theta\right)\mathbf u_\theta - \cos\theta\,\mathbf e_h\right] \quad &\text{($\mathbf k_1\times\mathbf e_h = \mathbf u_\theta$, $\mathbf k_1\times\mathbf u_\theta = -\mathbf e_h$)} \\
> &= m\dot\Omega R\left[\cos\theta\cos\phi\,\mathbf u_r - \left(\cos\phi + \sin\theta\right)\mathbf u_\theta - \cos\theta\sin\phi\,\mathbf u_\phi\right] \quad &\text{($\mathbf e_h$ in the spherical basis)} \\
> \mathbf F_C &= m\Omega^2\,\mathbf r_\perp = m\Omega^2R\left[\left(\cos\phi + \sin\theta\right)\cos\phi\,\mathbf u_r + \cos\theta\,\mathbf u_\theta - \left(\cos\phi + \sin\theta\right)\sin\phi\,\mathbf u_\phi\right] \quad &\text{(centripetal term times $-m$)} \\
> \mathbf k_1\times\mathbf u_\phi &= -\sin\phi\,\mathbf k_1\times\mathbf e_h + \cos\phi\,\mathbf k_1\times\mathbf k_1 = -\sin\phi\,\mathbf u_\theta \quad &\text{($\mathbf u_\phi$ through $\mathbf e_h$ and $\mathbf k_1$)} \\
> \mathbf F_{COR} &= -2m\Omega\,\mathbf k_1\times\left(R\dot\theta\cos\phi\,\mathbf u_\theta + R\dot\phi\,\mathbf u_\phi\right) = 2m\Omega R\left(\dot\theta\cos\phi\,\mathbf e_h + \dot\phi\sin\phi\,\mathbf u_\theta\right) \quad &\text{(Coriolis term times $-m$)} \\
> &= 2m\Omega R\left[\dot\theta\cos^2\phi\,\mathbf u_r + \dot\phi\sin\phi\,\mathbf u_\theta - \dot\theta\sin\phi\cos\phi\,\mathbf u_\phi\right] \quad &\text{($\mathbf e_h$ in the spherical basis)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf W = -mg\,\mathbf k_1, \quad \mathbf N = -N\,\mathbf u_r, \quad \mathbf F_A = \mathbf 0, \quad \mathbf F_E = -m\dot\Omega\,\mathbf k_1\times\mathbf r_1^P, \quad \mathbf F_C = m\Omega^2\,\mathbf r_\perp, \quad \mathbf F_{COR} = -2m\Omega\,\mathbf k_1\times\mathbf v_1^P \cr \text{with the spherical components written above} \end{gathered}}$$
>
> **Units:** $[mg] = [m\dot\Omega R] = [m\Omega^2R] = [m\Omega R\dot\theta] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two actual forces and three inertia forces. The centrifugal force pushes $P$ horizontally away from the axis; the Euler force acts only while the rate changes, horizontally and against the sense of the angular acceleration; the Coriolis force is normal to the relative velocity.

#### (c) Two differential equations for theta and phi

> [!derivation] Projections on the two tangent vectors
> **Law:** Newton's second law in a non-inertial frame projected on $\mathbf u_\theta$ and $\mathbf u_\phi$, which are normal to the reaction
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 3, Slide 14]; [Lecture 5, Slide 28]
>
> $$\begin{aligned}
> \mathbf u_\theta:\quad mR\left(\ddot\theta\cos\phi - 2\dot\theta\dot\phi\sin\phi\right) &= m\Omega^2R\cos\theta - m\dot\Omega R\left(\cos\phi + \sin\theta\right) + 2m\Omega R\dot\phi\sin\phi \quad &\text{(centrifugal, Euler, Coriolis; no weight, no reaction)} \\
> \mathbf u_\phi:\quad mR\left(\ddot\phi + \dot\theta^2\sin\phi\cos\phi\right) &= -mg\cos\phi - m\Omega^2R\left(\cos\phi + \sin\theta\right)\sin\phi - m\dot\Omega R\cos\theta\sin\phi - 2m\Omega R\dot\theta\sin\phi\cos\phi \quad &\text{(weight, centrifugal, Euler, Coriolis)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \ddot\theta\cos\phi - 2\dot\phi\sin\phi\left(\dot\theta + \Omega\right) = \Omega^2\cos\theta - \dot\Omega\left(\cos\phi + \sin\theta\right) \cr \ddot\phi + \dot\theta\left(\dot\theta + 2\Omega\right)\sin\phi\cos\phi + \frac{g}{R}\cos\phi + \Omega^2\sin\phi\left(\cos\phi + \sin\theta\right) + \dot\Omega\cos\theta\sin\phi = 0 \end{gathered}}$$
>
> **Units:** $[\ddot\theta] = [\Omega^2] = [\dot\Omega] = [\Omega\dot\phi] = [g/R] = [\mathrm T^{-2}]$
> **Meaning:** two coupled non-linear equations, forced through the known functions $\Omega(t)$ and its derivative; with initial conditions they give the two angles. Each was divided by $mR$, and the Coriolis terms were grouped with the relative ones.

#### (d) Reaction and separation condition

> [!derivation] Projection on the normal
> **Law:** Newton's second law in $S_1$ projected on $\mathbf u_r$, the only projection that contains $N$; one-sided contact
> **Source:** Notes.pdf, Eq. 4.63; Notes.pdf, Eq. 6.11; [Lecture 3, Slide 14]; [Lecture 3, Slide 21]
>
> $$\begin{aligned}
> \mathbf u_r:\quad -mR\left(\dot\phi^2 + \dot\theta^2\cos^2\phi\right) &= -N - mg\sin\phi + m\Omega^2R\cos\phi\left(\cos\phi + \sin\theta\right) + m\dot\Omega R\cos\theta\cos\phi + 2m\Omega R\dot\theta\cos^2\phi \quad &\text{(radial components of part (b))} \\
> N &= mR\dot\phi^2 + mR\cos^2\phi\left(\dot\theta^2 + 2\Omega\dot\theta + \Omega^2\right) + m\Omega^2R\cos\phi\sin\theta + m\dot\Omega R\cos\phi\cos\theta - mg\sin\phi \quad &\text{(solved for $N$; the $\cos^2\phi$ terms grouped)} \\
> \dot\theta^2 + 2\Omega\dot\theta + \Omega^2 &= \left(\dot\theta + \Omega\right)^2 \quad &\text{(perfect square)}
> \end{aligned}$$
>
> $$\boxed{N = mR\dot\phi^2 + mR\cos^2\phi\left(\dot\theta + \Omega\right)^2 + m\Omega^2R\cos\phi\sin\theta + m\dot\Omega R\cos\phi\cos\theta - mg\sin\phi; \qquad \text{separation when } N = 0 \text{ and it would become negative}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the reaction depends only on the two angles, their rates and the known data. The inner surface can only push towards $C$, so the solution of part (c) holds while $N$ stays non-negative; the particle leaves the surface at the first instant at which $N$ reaches zero with a negative rate of change.

### Answers and Checks

#### (e) Equilibria for a constant rate

> [!derivation] Relative equilibria: theta first
> **Law:** constant coordinates and constant rate, so the rates, accelerations, Euler and Coriolis terms vanish in the equations of part (c)
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Problems.pdf, p. 36
>
> Take a non-zero rate (the case of zero rate is in the limiting cases) and write $\lambda$ for the ratio of $\Omega^2R$ to $g$. At the poles of the coordinates (top and bottom of the sphere) the tangent plane is horizontal and the centrifugal force there, $m\Omega^2R\,\mathbf j_1$, is horizontal and not zero, so no pole is an equilibrium; away from the poles the cosine of $\phi$ is positive.
>
> $$\begin{aligned}
> \mathbf u_\theta:\quad 0 &= \Omega^2\cos\theta \;\Rightarrow\; \theta = \frac{\pi}{2} \ \text{ or } \ \theta = -\frac{\pi}{2} \quad &\text{($\Omega \ne 0$)} \\
> \mathbf u_\phi:\quad 0 &= \frac{g}{R}\cos\phi + \Omega^2\sin\phi\left(\cos\phi + \sin\theta\right) \quad &\text{(rates and $\dot\Omega$ zero)} \\
> \theta = \frac{\pi}{2}:\quad 0 &= 1 + \lambda\,\frac{\sin\phi\left(\cos\phi + 1\right)}{\cos\phi} = 1 + \lambda\left(\tan\phi + \sin\phi\right) \quad &\text{(divided by $g\cos\phi/R$)} \\
> \theta = -\frac{\pi}{2}:\quad 0 &= 1 + \lambda\,\frac{\sin\phi\left(\cos\phi - 1\right)}{\cos\phi} = 1 - \lambda\left(\tan\phi - \sin\phi\right) \quad &\text{(divided by $g\cos\phi/R$)} \\
> f(\phi) &= \tan\phi + \sin\phi, \quad f'(\phi) = \frac{1}{\cos^2\phi} + \cos\phi \gt 0 \quad &\text{(on $(-\tfrac{\pi}{2}, \tfrac{\pi}{2})$: increasing, from $-\infty$ to $+\infty$, zero at $0$)} \\
> h(\phi) &= \tan\phi - \sin\phi, \quad h'(\phi) = \frac{1}{\cos^2\phi} - \cos\phi \ge 0 \quad &\text{(zero only at $\phi = 0$; $h(0) = 0$, $h \to +\infty$ at the top)}
> \end{aligned}$$
>
> $$\boxed{\theta_1 = \frac{\pi}{2}: \ \tan\phi_1 + \sin\phi_1 = -\frac{g}{\Omega^2R}, \ \phi_1 \in \left(-\tfrac{\pi}{2}, 0\right); \qquad \theta_2 = -\frac{\pi}{2}: \ \tan\phi_2 - \sin\phi_2 = \frac{g}{\Omega^2R}, \ \phi_2 \in \left(0, \tfrac{\pi}{2}\right)}$$
>
> **Units:** $[g/(\Omega^2R)] = [1]$
> **Meaning:** exactly one root on each branch, both in the vertical plane through the axis and $C$; the first lies below the horizontal plane of $C$ on the side away from the axis, the second above it on the side of the axis.

> [!derivation] Reaction at the equilibria and admissibility
> **Law:** the reaction of part (d) at rest, with the equilibrium relation substituted; vertical balance
> **Source:** Notes.pdf, Eq. 4.63; [Lecture 3, Slide 21]
>
> At both roots the sine of $\phi$ is not zero, so the $\mathbf u_\phi$ condition gives the product of $\Omega^2R$ and the sum of $\cos\phi$ and $\sin\theta$ as minus $g\cos\phi/\sin\phi$.
>
> $$\begin{aligned}
> N &= m\Omega^2R\cos\phi\left(\cos\phi + \sin\theta\right) - mg\sin\phi \quad &\text{(part (d) at rest, $\dot\Omega$ zero)} \\
> &= -\frac{mg\cos^2\phi}{\sin\phi} - mg\sin\phi = -\frac{mg\left(\cos^2\phi + \sin^2\phi\right)}{\sin\phi} = -\frac{mg}{\sin\phi} \quad &\text{(equilibrium relation substituted)} \\
> \mathbf k_1\cdot\left(\mathbf W - N\,\mathbf u_r\right) &= -mg - N\sin\phi = 0 \quad &\text{(check: the centrifugal force is horizontal, so the vertical balance gives the same)} \\
> \Omega = 3\ \mathrm{rad\,s^{-1}},\ R = 1\ \mathrm m:\quad \tan\phi_1 + \sin\phi_1 &= -0.5850 - 0.5050 = -1.0900 = -\frac{9.81}{9}, \quad \phi_1 = -30.33^\circ, \quad N_1 = \frac{mg}{0.5050} = 1.98\,mg \quad &\text{(numerical example)} \\
> \tan\phi_2 - \sin\phi_2 &= 1.9829 - 0.8929 = 1.0900, \quad \phi_2 = 63.24^\circ, \quad N_2 = -\frac{mg}{0.8929} = -1.12\,mg \quad &\text{(numerical example)}
> \end{aligned}$$
>
> $$\boxed{N = -\frac{mg}{\sin\phi}: \quad \text{branch 1 } (\phi_1 \lt 0): \ N_1 \gt 0, \ \text{admissible}; \qquad \text{branch 2 } (\phi_2 \gt 0): \ N_2 \lt 0, \ \text{not admissible}}$$
>
> **Units:** $[mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** on branch 1 the particle sits in the lower half, on the side away from the axis, where the inward normal points up and towards the axis and balances the weight and the centrifugal force. On branch 2 the surface would have to pull the particle away from $C$, which the inner face cannot do; it would be an equilibrium only for a contact that holds on both sides.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Kinematics in $S_1$ | $\mathbf r_1^P = R(\mathbf j_1 + \mathbf k_1) + R\,\mathbf u_r$, $\mathbf v_1^P = R\dot\theta\cos\phi\,\mathbf u_\theta + R\dot\phi\,\mathbf u_\phi$, $\mathbf a_1^P = -R(\dot\phi^2 + \dot\theta^2\cos^2\phi)\,\mathbf u_r + R(\ddot\theta\cos\phi - 2\dot\theta\dot\phi\sin\phi)\,\mathbf u_\theta + R(\ddot\phi + \dot\theta^2\sin\phi\cos\phi)\,\mathbf u_\phi$; unit vectors as boxed |
| (b) Forces in $S_1$ | $-mg\,\mathbf k_1$; $-N\,\mathbf u_r$; origin force zero; Euler $-m\dot\Omega\,\mathbf k_1\times\mathbf r_1^P$; centrifugal $m\Omega^2\mathbf r_\perp$ with $\mathbf r_\perp = R(\cos\phi + \sin\theta)\,\mathbf e_h + R\cos\theta\,\mathbf u_\theta$; Coriolis $2m\Omega R(\dot\theta\cos\phi\,\mathbf e_h + \dot\phi\sin\phi\,\mathbf u_\theta)$ |
| (c) Equations | $\ddot\theta\cos\phi - 2\dot\phi\sin\phi(\dot\theta + \Omega) = \Omega^2\cos\theta - \dot\Omega(\cos\phi + \sin\theta)$; $\ddot\phi + \dot\theta(\dot\theta + 2\Omega)\sin\phi\cos\phi + (g/R)\cos\phi + \Omega^2\sin\phi(\cos\phi + \sin\theta) + \dot\Omega\cos\theta\sin\phi = 0$ |
| (d) Reaction and separation | $N = mR\dot\phi^2 + mR\cos^2\phi(\dot\theta + \Omega)^2 + m\Omega^2R\cos\phi\sin\theta + m\dot\Omega R\cos\phi\cos\theta - mg\sin\phi$; separation when $N$ reaches zero and would become negative |
| (e) Equilibria, constant $\Omega$ | $\theta = \pi/2$ with $\tan\phi_1 + \sin\phi_1 = -g/(\Omega^2R)$, $\phi_1 \in (-\pi/2, 0)$, $N = mg/\lvert\sin\phi_1\rvert \gt 0$: the only admissible equilibrium; $\theta = -\pi/2$ with $\tan\phi_2 - \sin\phi_2 = g/(\Omega^2R)$, $\phi_2 \in (0, \pi/2)$, $N = -mg/\sin\phi_2 \lt 0$: not admissible for the one-sided contact (admissible for a two-sided one); with zero rate: the bottom point, $N = mg$ |

**Check against the official key:** Problems.pdf, p. 76 prints no answer for problem 51. Independent checks: the reaction at the equilibria agrees with the vertical balance (box above), and the limiting cases follow.

> [!derivation] Limiting cases
> **Law:** the results at extreme values of the data; first-order Taylor expansion
> **Source:** Notes.pdf, Eq. 4.63
>
> $$\begin{aligned}
> \Omega = 0:\quad \ddot\theta\cos\phi - 2\dot\theta\dot\phi\sin\phi &= 0, \quad \ddot\phi + \dot\theta^2\sin\phi\cos\phi + \frac{g}{R}\cos\phi = 0 \quad &\text{(spherical pendulum in a fixed sphere)} \\
> \Omega = 0,\ \text{rest}:\quad \cos\phi &= 0, \quad \phi = -\frac{\pi}{2}: \ N = -mg\sin\left(-\tfrac{\pi}{2}\right) = mg \quad &\text{(bottom point; the top would need $N = -mg$)} \\
> \lambda \gg 1:\quad \tan\phi + \sin\phi &\approx \phi + \phi = 2\phi \;\Rightarrow\; \phi_1 \approx -\frac{g}{2\Omega^2R}, \quad N_1 \approx \frac{mg}{\left|\phi_1\right|} = 2m\Omega^2R \quad &\text{(first-order Taylor expansion about zero)} \\
> \lambda \to 0:\quad \tan\phi_1 + \sin\phi_1 &\to -\infty \;\Rightarrow\; \phi_1 \to -\frac{\pi}{2}, \quad N_1 \to mg \quad &\text{(slow rotation: back to the bottom)}
> \end{aligned}$$
>
> $$\boxed{\Omega \to 0: \ \phi_1 \to -\tfrac{\pi}{2}, \ N_1 \to mg; \qquad \Omega \to \infty: \ \phi_1 \to 0^-, \ N_1 \approx 2m\Omega^2R}$$
>
> **Units:** $[m\Omega^2R] = [mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** as the rate grows the particle climbs towards the horizontal plane of $C$, at the distance $2R$ from the axis, and the reaction becomes the centripetal force of a circle of radius $2R$. The statement does not ask for stability, which is not discussed here.
