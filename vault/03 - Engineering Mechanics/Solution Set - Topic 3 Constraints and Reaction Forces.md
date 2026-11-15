---
title: "Solution Set - Topic 3: Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions"
language: "English"
tags:
  - solutions
  - constraints
---

# 📚 Topic 3: Constraints and Reaction Forces - Full Analytical Solutions

Exhaustive, step-by-step analytical solutions for all 12 solvable problems from Topic 3 (**Constraints and Reaction Forces**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every problem follows the Engineering Mechanics order of the problem-solving standard (frames and coordinates, change of basis and position vector, kinematics, forces and equations of motion, answers and checks), with explicit justification prior to every equation, zero algebraic omissions, explicit derivative developments (product, quotient, and chain rules), explicit integral evaluations (substitutions, primitives, and Barrow's rule), rotation matrices $[{}_0 R_1]$, normal and tangent subspaces ($V_N, V_T$), and dimensional verifications.

---

## Problem 18: Heavy Particle on a Cone

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides without friction on the cone of the statement, whose vertex is the origin $O$ and whose axis is the ascending vertical $Oz$. The statement gives the initial position and velocity and asks for the reduction of the problem to integrals and for the extreme values of the height $z$ (Problems.pdf, p. 10). The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7: constraints and coordinates, frames, kinematics, forces, equations of motion, integration.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the vertex of the cone (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, $\mathbf k$ vertical **upward** (ascending $Oz$), right-handed |
| Cylindrical basis | $\mathcal B_1 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by the azimuth $\theta$ about $\mathbf k$ (Notes.pdf, Eq. 2.24) |
| Surface basis | $\mathcal B_2 = \{\mathbf e_g, \mathbf e_\theta, \mathbf n\}$: $\mathbf e_g$ along the generator through $P$ (upward), $\mathbf n$ normal to the cone towards its axis; $\mathcal B_1$ turned about $\mathbf e_\theta$ |
| Cylindrical coordinates | $R$ (distance to the axis), $\theta$ (azimuth from the plane $Oxz$), $z$ (height) (Notes.pdf, Eq. 2.23) |
| Constraint | $f(x, y, z) = x^2 + y^2 - z^2 = 0$ with $z \gt 0$ (upper nappe, the one that contains the initial point); in cylindrical coordinates $z = R$ |
| Classification | holonomic (an equation among the coordinates), stationary (no explicit time), smooth (ideal: the reaction is normal to the surface); the particle rides on the inner face of the cone, so the contact is unilateral and is checked by the sign of the reaction ([Lecture 3, Slide 21]) |
| Degrees of freedom | a free particle has 3; one surface constraint leaves 2: $R(t)$ and $\theta(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $g$ [m s$^{-2}$], $a$ [m] |
| Applied force | weight $-mg\,\mathbf k$ |
| Reaction | $\mathbf N = N\,\mathbf n$, one unknown component, since the normal subspace of a surface has dimension 1 (Notes.pdf, Sec. 6.3; Notes.pdf, Sec. 6.4) |
| Initial conditions | $\mathbf r_0^P(0) = a\,\mathbf i + a\,\mathbf k$, $\mathbf v_0^P(0) = \sqrt{ag}\,\mathbf j$: $R(0) = a$, $\theta(0) = 0$, $\dot R(0) = 0$, $\dot\theta(0) = \sqrt{g/a}$ (from $a\dot\theta(0) = \sqrt{ag}$, see the kinematics) |
| Hypotheses | no friction (statement); the reaction may only push the particle away from the surface towards the axis; the result shows that it always does |

![[attachments/EM-SOL/p18-meridian.svg]]

### Change of Basis and Position Vector

The cylindrical basis is seen from above, along $\mathbf k$: with $\mathbf i$ to the right and $\mathbf j$ up, $\mathbf k$, the cross product of $\mathbf i$ and $\mathbf j$, points out of the paper (⊙), and a positive rotation about $\mathbf k$ is counterclockwise.

![[attachments/EM-SOL/p18-rotation-k.svg]]

> [!derivation] Cylindrical basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View along $\mathbf k$ (⊙). The unit vector $\mathbf e_R$ is $\mathbf i$ turned counterclockwise by $\theta$: its right triangle has hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i$ and opposite leg $\sin\theta$ along $\mathbf j$. The unit vector $\mathbf e_\theta$ is $\mathbf j$ turned by the same angle: its adjacent leg $\cos\theta$ lies along $\mathbf j$ and its opposite leg $\sin\theta$ along minus $\mathbf i$, because turning the upward vector counterclockwise leans it to the left; that is the origin of the minus sign.
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(adjacent leg on $\mathbf i$, opposite leg on $\mathbf j$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(adjacent leg on $\mathbf j$, opposite leg on $-\mathbf i$)} \\
> \mathbf e_R\times\mathbf e_\theta &= \cos^2\theta\,\mathbf i\times\mathbf j - \sin^2\theta\,\mathbf j\times\mathbf i = \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed: $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= \cos\theta\left(\cos\theta\cdot 1 - 0\right) - \left(-\sin\theta\right)\left(\sin\theta\cdot 1 - 0\right) + 0 = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times rows 1 and 2; row 3 is the unit row of $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** every entry is a direction cosine, dimensionless: $[1]$; $\theta$ in radians, dimensionless
> **Meaning:** the columns are $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf k$ written in $\mathcal B_0$; $\mathbf e_R$ points horizontally away from the axis, towards the particle.

> [!derivation] Normal of the cone from the gradient
> **Law:** the gradient of the implicit equation is normal to the surface; unit normal by normalisation
> **Source:** Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 6.10; Notes.pdf, Eq. 2.23
>
> $$\begin{aligned}
> \nabla f &= 2x\,\mathbf i + 2y\,\mathbf j - 2z\,\mathbf k \quad &\text{(partial derivatives of $x^2 + y^2 - z^2$)} \\
> &= 2R\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) - 2z\,\mathbf k = 2R\,\mathbf e_R - 2z\,\mathbf k \quad &\text{($x = R\cos\theta$, $y = R\sin\theta$)} \\
> &= 2R\left(\mathbf e_R - \mathbf k\right) \quad &\text{(on the cone $z = R$)} \\
> |\nabla f| &= 2R\sqrt{1 + 1} = 2\sqrt2\,R \quad &\text{($\mathbf e_R \perp \mathbf k$, both unit)} \\
> \mathbf n &= -\frac{\nabla f}{|\nabla f|} = \frac{1}{\sqrt2}\left(-\mathbf e_R + \mathbf k\right) \quad &\text{(sign chosen towards the axis and upwards, the side of the particle)}
> \end{aligned}$$
>
> $$\boxed{\mathbf n = \frac{1}{\sqrt2}\left(-\mathbf e_R + \mathbf k\right), \qquad V_N = \mathrm{span}\{\mathbf n\}}$$
>
> **Units:** $[\nabla f] = [\mathrm{L}]$; $\mathbf n$ is dimensionless
> **Meaning:** the normal lies in the meridian plane of $P$ and makes 45 degrees with the vertical; the reaction of the smooth cone can only act along it.

> [!derivation] Surface basis: rotation about e_theta in the meridian plane
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.19
>
> View of the meridian plane of $P$ with $\mathbf e_R$ to the right and $\mathbf k$ up. Since $\mathbf e_\theta$ is the cross product of $\mathbf k$ and $\mathbf e_R$, it points into the paper (⊗) in this view, and a positive rotation about $\mathbf e_\theta$ (right-hand rule, thumb into the paper) is clockwise as seen. The generator $z = R$ rises at 45 degrees, so $\mathbf e_g$ is $\mathbf e_R$ turned counterclockwise by $\pi/4$: Notes.pdf, Eq. 1.19 with the negative angle $-\pi/4$. Its right triangle is the one of the generator itself: hypotenuse $R\sqrt2$ (the distance $OP$), adjacent leg $R$ (horizontal), opposite leg $z$, equal to $R$ (vertical); divided by the hypotenuse the legs give $\cos\frac{\pi}{4}$ and $\sin\frac{\pi}{4}$. The vector $\mathbf n$ is $\mathbf k$ turned by the same angle: adjacent leg along $\mathbf k$, opposite leg along minus $\mathbf e_R$ (turning the upward vector counterclockwise leans it to the left, towards the axis): that is the minus sign.
>
> $$\begin{aligned}
> \mathbf e_g &= \cos\tfrac{\pi}{4}\,\mathbf e_R + \sin\tfrac{\pi}{4}\,\mathbf k = \tfrac{1}{\sqrt2}\left(\mathbf e_R + \mathbf k\right) \quad &\text{(adjacent leg on $\mathbf e_R$, opposite leg on $\mathbf k$)} \\
> \mathbf n &= -\sin\tfrac{\pi}{4}\,\mathbf e_R + \cos\tfrac{\pi}{4}\,\mathbf k = \tfrac{1}{\sqrt2}\left(-\mathbf e_R + \mathbf k\right) \quad &\text{(same vector as from the gradient)} \\
> \mathbf e_g\times\mathbf e_\theta &= \tfrac{1}{\sqrt2}\left(\mathbf e_R\times\mathbf e_\theta + \mathbf k\times\mathbf e_\theta\right) = \tfrac{1}{\sqrt2}\left(\mathbf k - \mathbf e_R\right) = \mathbf n \quad &\text{($\mathbf e_R\times\mathbf e_\theta = \mathbf k$, $\mathbf k\times\mathbf e_\theta = -\mathbf e_R$: right-handed)} \\
> \det[{}_1R_2] &= \tfrac{1}{\sqrt2}\left(1\cdot\tfrac{1}{\sqrt2} - 0\right) - 0 + \left(-\tfrac{1}{\sqrt2}\right)\left(0 - 1\cdot\tfrac{1}{\sqrt2}\right) = \tfrac12 + \tfrac12 = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{11} &= \tfrac12 + \tfrac12 = 1, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{13} = \tfrac12 - \tfrac12 = 0 \quad &\text{(row 1 times rows 1 and 3; row 2 is the unit row of $\mathbf e_\theta$)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \tfrac{1}{\sqrt2} & 0 & -\tfrac{1}{\sqrt2} \cr 0 & 1 & 0 \cr \tfrac{1}{\sqrt2} & 0 & \tfrac{1}{\sqrt2} \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad [{}_1R_2][{}_1R_2]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf e_g$ and $\mathbf e_\theta$ span the tangent plane $V_T$ of the cone at $P$ and $\mathbf n$ spans the normal line $V_N$; the basis separates the directions where the particle may move from the one where the reaction acts.

> [!derivation] Position vector of the particle
> **Law:** position vector in cylindrical coordinates with the constraint substituted
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.28; [Lecture 3, Slide 4]
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = R\,\mathbf e_R + z\,\mathbf k \quad &\text{(horizontal leg plus vertical leg of the meridian triangle)} \\
> &= R\,\mathbf e_R + R\,\mathbf k \quad &\text{(constraint $z = R$ substituted: only $R$ and $\theta$ remain)} \\
> \mathbf r_0^P(0) &= a\,\mathbf i + a\,\mathbf k \quad &\text{($R(0) = a$, $\theta(0) = 0$ so $\mathbf e_R(0) = \mathbf i$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_R + R\,\mathbf k}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the two free coordinates parametrise the cone, so the constraint holds identically and never has to be imposed again.

### Kinematics

> [!derivation] Derivatives of the cylindrical unit vectors
> **Law:** derivative of a unit vector of a rotating basis, $\dot{\mathbf u} = \boldsymbol\omega\times\mathbf u$
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k \quad &\text{($\mathcal B_1$ turns about $\mathbf k$ at the rate of $\theta$)} \\
> \dot{\mathbf e}_R &= \dot\theta\,\mathbf k\times\mathbf e_R = \dot\theta\,\mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf e_R = \mathbf e_\theta$, right-handed $\mathcal B_1$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_R \quad &\text{($\mathbf k\times\mathbf e_\theta = -\mathbf e_R$)} \\
> \dot{\mathbf k} &= \mathbf 0 \quad &\text{($\mathbf k$ is the rotation axis and is fixed in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_R = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_R, \qquad \dot{\mathbf k} = \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the horizontal unit vectors turn with the meridian plane of the particle.

> [!derivation] Velocity and acceleration of the particle
> **Law:** velocity and acceleration as time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 2.29; Notes.pdf, Eq. 2.30
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(R\,\mathbf e_R + R\,\mathbf k\right) = \dot R\,\mathbf e_R + R\,\dot{\mathbf e}_R + \dot R\,\mathbf k \quad &\text{(product rule; $\mathbf k$ constant)} \\
> &= \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + \dot R\,\mathbf k \quad &\text{(derivative of $\mathbf e_R$)} \\
> \mathbf a_0^P &= \ddot R\,\mathbf e_R + \dot R\dot\theta\,\mathbf e_\theta + \left(\dot R\dot\theta + R\ddot\theta\right)\mathbf e_\theta + R\dot\theta\,\dot{\mathbf e}_\theta + \ddot R\,\mathbf k \quad &\text{(product rule on each term)} \\
> &= \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(2\dot R\dot\theta + R\ddot\theta\right)\mathbf e_\theta + \ddot R\,\mathbf k \quad &\text{(derivative of $\mathbf e_\theta$; terms grouped)} \\
> |\mathbf v_0^P|^2 &= \dot R^2 + R^2\dot\theta^2 + \dot R^2 = 2\dot R^2 + R^2\dot\theta^2 \quad &\text{(orthonormal components)} \\
> \mathbf v_0^P(0) &= a\,\dot\theta(0)\,\mathbf j = \sqrt{ag}\,\mathbf j \Rightarrow \dot\theta(0) = \sqrt{g/a}, \quad \dot R(0) = 0 \quad &\text{(at $t = 0$, $\mathbf e_\theta = \mathbf j$; comparison with the data)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + \dot R\,\mathbf k, \qquad \mathbf a_0^P = \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(2\dot R\dot\theta + R\ddot\theta\right)\mathbf e_\theta + \ddot R\,\mathbf k}$$
>
> **Units:** velocity $[\mathrm{L\,T^{-1}}]$: $[\dot R] = [R\dot\theta] = [\mathrm{L\,T^{-1}}]$; acceleration $[\mathrm{L\,T^{-2}}]$: $[\ddot R] = [R\dot\theta^2] = [\dot R\dot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity has no component along $\mathbf n$ (its $\mathbf e_R$ and $\mathbf k$ components are equal, so it lies in the tangent plane), as a stationary constraint requires; the initial velocity is horizontal, along the parallel.

### Forces and Equations of Motion

The free-body diagram, drawn in the meridian plane, shows the weight and the normal reaction. The frame $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p18-fbd.svg]]

> [!derivation] Newton's second law with the reaction, projected on the surface basis
> **Law:** Newton's second law in an inertial frame with the constraint force; projection on the tangent and normal directions
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.11; [Lecture 3, Slide 13]; [Lecture 3, Slide 14]
>
> The weight and the acceleration are written in $\mathcal B_2$ with the inverse relations of the surface basis, read from the rows of $[{}_1R_2]$.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf k + N\,\mathbf n \quad &\text{(weight plus normal reaction; 3 equations, unknowns $R$, $\theta$, $N$)} \\
> \mathbf e_R &= \tfrac{1}{\sqrt2}\left(\mathbf e_g - \mathbf n\right), \quad \mathbf k = \tfrac{1}{\sqrt2}\left(\mathbf e_g + \mathbf n\right) \quad &\text{(rows 1 and 3 of $[{}_1R_2]$)} \\
> \mathbf a_0^P\cdot\mathbf e_g &= \tfrac{1}{\sqrt2}\left(\ddot R - R\dot\theta^2 + \ddot R\right) = \tfrac{1}{\sqrt2}\left(2\ddot R - R\dot\theta^2\right) \quad &\text{(components on $\mathbf e_R$ and $\mathbf k$ projected)} \\
> \mathbf a_0^P\cdot\mathbf n &= \tfrac{1}{\sqrt2}\left(-\ddot R + R\dot\theta^2 + \ddot R\right) = \tfrac{1}{\sqrt2}\,R\dot\theta^2 \quad &\text{(same, on $\mathbf n$)} \\
> \mathbf e_g:\ \tfrac{m}{\sqrt2}\left(2\ddot R - R\dot\theta^2\right) &= -\tfrac{mg}{\sqrt2} \quad &\text{(tangent: $\mathbf n\cdot\mathbf e_g = 0$, the reaction drops out)} \\
> \mathbf e_\theta:\ m\left(2\dot R\dot\theta + R\ddot\theta\right) &= 0 \quad &\text{(tangent: neither the weight nor the reaction has an azimuthal part)} \\
> \mathbf n:\ \tfrac{m}{\sqrt2}\,R\dot\theta^2 &= -\tfrac{mg}{\sqrt2} + N \quad &\text{(normal: it holds the reaction)}
> \end{aligned}$$
>
> $$\boxed{2\ddot R - R\dot\theta^2 + g = 0, \qquad 2\dot R\dot\theta + R\ddot\theta = 0, \qquad N = \frac{m}{\sqrt2}\left(g + R\dot\theta^2\right)}$$
>
> **Units:** every term of the first two equations in $[\mathrm{L\,T^{-2}}]$; $[N] = [\mathrm{M}][\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the two tangent projections are the equations of motion of the two degrees of freedom, free of the reaction; the normal projection gives the reaction once the motion is known (dynamical decoupling). Since $N$ is a sum of positive terms, the cone always pushes the particle towards the axis: the unilateral contact never opens.

> [!derivation] First integral of the azimuthal equation
> **Law:** the azimuthal equation is an exact derivative; integration with Barrow's rule
> **Source:** Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 2.30
>
> $$\begin{aligned}
> \frac{d}{dt}\left(R^2\dot\theta\right) &= 2R\dot R\,\dot\theta + R^2\ddot\theta = R\left(2\dot R\dot\theta + R\ddot\theta\right) \quad &\text{(product rule; chain rule on $R^2$)} \\
> \frac{d}{dt}\left(R^2\dot\theta\right) &= 0 \quad &\text{(azimuthal equation times $R$)} \\
> \int_0^t \frac{d}{dt'}\left(R^2\dot\theta\right)dt' &= \left[R^2\dot\theta\right]_0^t = R^2\dot\theta - R(0)^2\dot\theta(0) = 0 \quad &\text{(Barrow's rule between $0$ and $t$)} \\
> R^2\dot\theta &= a^2\sqrt{g/a} = a\sqrt{ag} \equiv h \quad &\text{(initial data)}
> \end{aligned}$$
>
> $$\boxed{R^2\dot\theta = h = a\sqrt{ag}, \qquad \dot\theta = \frac{a\sqrt{ag}}{R^2}}$$
>
> **Units:** $[R^2\dot\theta] = [\mathrm{L^2\,T^{-1}}]$; $[a\sqrt{ag}] = [\mathrm{L}][\mathrm{L\,T^{-1}}] = [\mathrm{L^2\,T^{-1}}]$
> **Meaning:** no force has a moment about the vertical axis (the weight is vertical and the reaction lies in the meridian plane), so this areal quantity is constant: the particle turns faster when it is closer to the axis.

> [!derivation] Energy integral derived from the meridian equation
> **Law:** the equation of motion multiplied by the rate of the coordinate is an exact derivative (chain rule); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 6.12
>
> $$\begin{aligned}
> R\dot\theta^2 &= R\,\frac{h^2}{R^4} = \frac{h^2}{R^3} \quad &\text{(first integral substituted)} \\
> 2\dot R\ddot R - \frac{h^2}{R^3}\,\dot R + g\dot R &= 0 \quad &\text{(meridian equation times $\dot R$)} \\
> \frac{d}{dt}\left(\dot R^2\right) &= 2\dot R\ddot R, \quad \frac{d}{dt}\left(\frac{h^2}{2R^2}\right) = -\frac{h^2}{R^3}\,\dot R, \quad \frac{d}{dt}\left(gR\right) = g\dot R \quad &\text{(chain rule on each term)} \\
> \frac{d}{dt}\left(\dot R^2 + \frac{h^2}{2R^2} + gR\right) &= 0 \quad &\text{(sum of the three derivatives)} \\
> \left[\dot R^2 + \frac{h^2}{2R^2} + gR\right]_0^t &= 0 \quad &\text{(Barrow's rule between $0$ and $t$)} \\
> \dot R^2 + \frac{h^2}{2R^2} + gR &= 0 + \frac{a^3 g}{2a^2} + ga = \tfrac32\,ga \quad &\text{($\dot R(0) = 0$, $R(0) = a$, $h^2 = a^3 g$)} \\
> \tfrac12 m|\mathbf v_0^P|^2 + mgz &= m\left(\dot R^2 + \frac{R^2\dot\theta^2}{2} + gR\right) = \tfrac32\,mga \quad &\text{(the same constant times $m$: kinetic plus potential energy)}
> \end{aligned}$$
>
> $$\boxed{\dot R^2 = \tfrac32\,ga - gR - \frac{a^3 g}{2R^2}}$$
>
> **Units:** every term in $[\mathrm{L^2\,T^{-2}}]$: $[ga] = [gR] = [\mathrm{L\,T^{-2}}][\mathrm{L}]$; $[a^3 g/R^2] = [\mathrm{L^3}][\mathrm{L\,T^{-2}}]/[\mathrm{L^2}]$; energy $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy is conserved: the weight derives from a potential and the reaction of the stationary smooth cone does no work, since it is normal to the velocity.

### Answers and Checks

#### Reduction to integrals

> [!derivation] Quadratures of the motion
> **Law:** separation of variables in the energy integral; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44; Notes.pdf, Sec. 7.7
>
> For any data of the same kind (energy constant $E$ per unit mass written as $e$, areal constant $h$, start at $R_0$), the two first integrals give the motion by two quadratures.
>
> $$\begin{aligned}
> \frac{dR}{dt} &= \pm\sqrt{\Phi(R)}, \quad \Phi(R) = e - gR - \frac{h^2}{2R^2} \quad &\text{(energy integral solved for $\dot R$)} \\
> \frac{dR'}{\pm\sqrt{\Phi(R')}} &= dt' \quad &\text{(separation of variables)} \\
> \int_{R_0}^{R}\frac{dR'}{\pm\sqrt{\Phi(R')}} &= \int_0^t dt' = \left[t'\right]_0^t = t \quad &\text{(integration; Barrow's rule on the right)} \\
> \theta(t) - \theta(0) &= \int_0^t \dot\theta\,dt' = \int_0^t \frac{h}{R(t')^2}\,dt' \quad &\text{(areal integral, Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{t = \int_{R_0}^{R}\frac{dR'}{\pm\sqrt{e - gR' - h^2/(2R'^2)}}, \qquad \theta(t) = \theta(0) + \int_0^t\frac{h\,dt'}{R(t')^2}, \qquad z(t) = R(t)}$$
>
> **Units:** $[\Phi] = [\mathrm{L^2\,T^{-2}}]$, so $[dR/\sqrt\Phi] = [\mathrm{L}]/[\mathrm{L\,T^{-1}}] = [\mathrm{T}]$; $[h/R^2] = [\mathrm{T^{-1}}]$
> **Meaning:** the radius, and with it the height, oscillates between the zeros of $\Phi$; the azimuth follows from the radius.

#### Maximum and minimum of z

> [!derivation] Turning points of the radius for the data of the statement
> **Law:** the motion is possible only where the squared rate is not negative; factorisation of the cubic
> **Source:** Notes.pdf, Eq. 4.28; Problems.pdf, p. 10
>
> $$\begin{aligned}
> \Phi(R) &= \tfrac32\,ga - gR - \frac{a^3 g}{2R^2} = -\frac{g}{2R^2}\left(2R^3 - 3aR^2 + a^3\right) \quad &\text{(common denominator $2R^2$)} \\
> 2a^3 - 3a\cdot a^2 + a^3 &= 0 \quad &\text{($R = a$ is a root: the start)} \\
> \left(R - a\right)\left(2R^2 - aR - a^2\right) &= 2R^3 - aR^2 - a^2R - 2aR^2 + a^2R + a^3 = 2R^3 - 3aR^2 + a^3 \quad &\text{(division by $R - a$, checked by expansion)} \\
> 2R^2 - aR - a^2 &= \left(R - a\right)\left(2R + a\right) \quad &\text{(roots $a$ and $-a/2$ of the quadratic)} \\
> \Phi(R) &= -\frac{g\left(2R + a\right)}{2R^2}\left(R - a\right)^2 \quad &\text{(double root at $a$)} \\
> \Phi(R) &\le 0 \ \text{for } R \gt 0, \quad \Phi(R) = 0 \iff R = a \quad &\text{($2R + a \gt 0$, square not negative)} \\
> \dot R^2 = \Phi(R) \ge 0 &\Rightarrow R(t) \equiv a \Rightarrow \dot\theta = \frac{a\sqrt{ag}}{a^2} = \sqrt{g/a} \quad &\text{(only the double root is accessible)} \\
> \theta(t) &= \int_0^t\sqrt{g/a}\,dt' = \left[\sqrt{g/a}\,t'\right]_0^t = \sqrt{g/a}\,t \quad &\text{(Barrow's rule, $\theta(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{R(t) \equiv a, \quad z_{\max} = z_{\min} = a, \quad \theta(t) = \sqrt{g/a}\,t}$$
>
> **Units:** $[\Phi] = [\mathrm{L\,T^{-2}}][\mathrm{L^3}]/[\mathrm{L^2}] = [\mathrm{L^2\,T^{-2}}]$; $[\sqrt{g/a}] = [\mathrm{T^{-1}}]$
> **Meaning:** the data are exactly those of a steady circular orbit: the particle runs round the horizontal circle of radius $a$ at height $a$ with constant speed $\sqrt{ag}$; the height neither rises nor falls.

> [!derivation] Check of the circular motion and of the reaction
> **Law:** Newton's second law on the circular orbit; sign of the unilateral reaction
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> \mathbf a_0^P &= -a\,\frac{g}{a}\,\mathbf e_R = -g\,\mathbf e_R \quad &\text{($R = a$, $\dot R = \ddot R = 0$, $\ddot\theta = 0$, $\dot\theta^2 = g/a$)} \\
> N &= \frac{m}{\sqrt2}\left(g + a\,\frac{g}{a}\right) = \sqrt2\,mg \quad &\text{(reaction formula)} \\
> -mg\,\mathbf k + N\,\mathbf n &= -mg\,\mathbf k + \sqrt2\,mg\,\tfrac{1}{\sqrt2}\left(-\mathbf e_R + \mathbf k\right) = -mg\,\mathbf e_R \quad &\text{(sum of the forces)} \\
> m\,\mathbf a_0^P &= -mg\,\mathbf e_R \quad &\text{(equal: Newton's law holds)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N = mg\left(-\mathbf e_R + \mathbf k\right), \qquad |\mathbf N| = \sqrt2\,mg \gt 0}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the vertical part of the reaction carries the weight and its horizontal part, pointing to the axis, supplies the centripetal force $m v^2/a$ with $v^2 = ag$; the cone pushes, so the contact holds.

> [!derivation] Limiting case: a slightly perturbed start
> **Law:** linearisation of the meridian equation about the circular orbit
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 5.6
>
> If the start radius is moved to $a$ plus a small $\rho$ with the same areal constant $h$, the meridian equation is linearised in $\rho$.
>
> $$\begin{aligned}
> 2\ddot\rho &= \frac{h^2}{\left(a + \rho\right)^3} - g \quad &\text{(meridian equation with $R\dot\theta^2 = h^2/R^3$)} \\
> \frac{h^2}{\left(a + \rho\right)^3} &\approx \frac{h^2}{a^3}\left(1 - \frac{3\rho}{a}\right) = g - \frac{3g}{a}\,\rho \quad &\text{(first-order Taylor expansion; $h^2 = a^3 g$)} \\
> \ddot\rho + \frac{3g}{2a}\,\rho &= 0 \quad &\text{(the constant terms cancel; division by 2)}
> \end{aligned}$$
>
> $$\boxed{\omega_\rho = \sqrt{\frac{3g}{2a}}}$$
>
> **Units:** $[\omega_\rho] = [\mathrm{T^{-1}}]$
> **Meaning:** the orbit is stable: a small disturbance makes the height oscillate about $a$ instead of drifting away, so the extreme values of $z$ stay close to $a$.

| Part of the statement | Answer |
| :--- | :--- |
| Equations of motion | $2\ddot R - R\dot\theta^2 + g = 0$, $2\dot R\dot\theta + R\ddot\theta = 0$; reaction $N = \frac{m}{\sqrt2}(g + R\dot\theta^2)$ along $\mathbf n = (-\mathbf e_R + \mathbf k)/\sqrt2$ |
| Integral equations | $R^2\dot\theta = a\sqrt{ag}$; $\dot R^2 = \frac32 ga - gR - \frac{a^3 g}{2R^2}$; $t = \int_a^R dR'/\pm\sqrt{\Phi(R')}$, $\theta = \int_0^t h\,dt'/R^2$ |
| Maximum and minimum of $z$ | $\Phi(R) = -\frac{g(2R + a)}{2R^2}(R - a)^2 \le 0$, so $R \equiv a$: $z_{\max} = z_{\min} = a$ (uniform circular motion, $\dot\theta = \sqrt{g/a}$, reaction $\sqrt2\,mg$) |

**Check against the official key:** Problems.pdf, p. 73 lists item 18 with no answer, so there is no key to compare with. Independent check: the box of the circular motion substitutes the result back into Newton's law, and the linearised meridian equation shows the orbit is stable.

---

## Problem 19: Heavy Particle on a Paraboloid

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides without friction on the paraboloid of revolution of the statement, whose axis is the vertical $Oz$ and whose vertex is the origin. It starts on the parallel of radius $a$ with a velocity $v_0$ tangent to that parallel. The statement asks for the reduction to integrals of the form of an integral in $r$ equal to an integral in $t$, and for the extreme values of $r$ (Problems.pdf, p. 10). The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the vertex of the paraboloid (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, $\mathbf k$ vertical **upward** (the paraboloid opens upwards since $a \gt 0$), right-handed |
| Cylindrical basis | $\mathcal B_1 = \{\mathbf e_r, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by the azimuth $\theta$ about $\mathbf k$ (Notes.pdf, Eq. 2.24) |
| Surface basis | $\mathcal B_2 = \{\mathbf e_m, \mathbf e_\theta, \mathbf n\}$: $\mathbf e_m$ tangent to the meridian parabola (upward), $\mathbf n$ normal to the surface towards the axis; $\mathcal B_1$ turned about $\mathbf e_\theta$ by the slope angle $\varphi$ of the meridian |
| Cylindrical coordinates | $r$ (distance to the axis, the $r$ of the statement), $\theta$ (azimuth), $z$ (height) (Notes.pdf, Eq. 2.23) |
| Constraint | $f(x, y, z) = x^2 + y^2 - a z = 0$; in cylindrical coordinates $z = r^2/a$ |
| Classification | holonomic, stationary, smooth (ideal); the particle rides on the inner (upper) face, a unilateral contact checked by the sign of the reaction ([Lecture 3, Slide 21]) |
| Degrees of freedom | 3 minus 1 surface constraint: 2, namely $r(t)$ and $\theta(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $g$ [m s$^{-2}$], $a$ [m], $v_0$ [m s$^{-1}$] |
| Applied force | weight $-mg\,\mathbf k$ |
| Reaction | $\mathbf N = N\,\mathbf n$, one unknown component (Notes.pdf, Sec. 6.3; Notes.pdf, Sec. 6.4) |
| Initial conditions | $r(0) = a$, $\theta(0) = 0$ (azimuth origin chosen at the start), $\dot r(0) = 0$ and $a\,\dot\theta(0) = v_0$ (velocity tangent to the parallel), $z(0) = a$ |
| Hypotheses | no friction (statement); $v_0 \gt 0$ (sense of the azimuth chosen along the initial velocity) |

![[attachments/EM-SOL/p19-meridian.svg]]

### Change of Basis and Position Vector

Seen from above, along $\mathbf k$, with $\mathbf i$ to the right and $\mathbf j$ up, $\mathbf k$ (the cross product of $\mathbf i$ and $\mathbf j$) points out of the paper (⊙) and a positive rotation about $\mathbf k$ is counterclockwise.

![[attachments/EM-SOL/p19-rotation-k.svg]]

> [!derivation] Cylindrical basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View along $\mathbf k$ (⊙). $\mathbf e_r$ is $\mathbf i$ turned counterclockwise by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ on $\mathbf i$, opposite leg $\sin\theta$ on $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by the same angle: adjacent leg $\cos\theta$ on $\mathbf j$, opposite leg $\sin\theta$ on minus $\mathbf i$, since the upward vector turned counterclockwise leans to the left (the minus sign).
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(the two right triangles)} \\
> \mathbf e_r\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed)} \\
> \det[{}_0R_1] &= \cos\theta\cdot\cos\theta - \left(-\sin\theta\right)\sin\theta = 1 \quad &\text{(expansion along the third row, unit entry)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** the columns are $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf k$ in $\mathcal B_0$; $\mathbf e_r$ points from the axis to the particle.

> [!derivation] Normal and meridian tangent of the paraboloid
> **Law:** the gradient of the implicit equation is normal to the surface; the meridian tangent completes the right-handed triad
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 6.10; Notes.pdf, Sec. 6.3
>
> Meridian section through $P$ (view with $\mathbf e_r$ to the right and $\mathbf k$ up, $\mathbf e_\theta$ into the paper ⊗, since $\mathbf e_\theta$ is the cross product of $\mathbf k$ and $\mathbf e_r$). The slope of the meridian $z = r^2/a$ is $2r/a$; the slope triangle has horizontal leg $a$, vertical leg $2r$ and hypotenuse $D = \sqrt{a^2 + 4r^2}$, so the slope angle $\varphi$ has $\cos\varphi = a/D$ (adjacent over hypotenuse) and $\sin\varphi = 2r/D$ (opposite over hypotenuse). The tangent $\mathbf e_m$ is $\mathbf e_r$ turned counterclockwise by $\varphi$; with the axis $\mathbf e_\theta$ into the paper a positive rotation is clockwise, so this is Notes.pdf, Eq. 1.19 with the angle $-\varphi$. The normal $\mathbf n$ is $\mathbf k$ turned by the same angle and leans towards the axis, minus $\mathbf e_r$: the minus sign.
>
> $$\begin{aligned}
> \nabla f &= 2x\,\mathbf i + 2y\,\mathbf j - a\,\mathbf k = 2r\,\mathbf e_r - a\,\mathbf k \quad &\text{(partial derivatives; $x = r\cos\theta$, $y = r\sin\theta$)} \\
> |\nabla f| &= \sqrt{4r^2 + a^2} = D \quad &\text{(orthogonal components)} \\
> \mathbf n &= -\frac{\nabla f}{D} = -\frac{2r}{D}\,\mathbf e_r + \frac{a}{D}\,\mathbf k = -\sin\varphi\,\mathbf e_r + \cos\varphi\,\mathbf k \quad &\text{(sign chosen upwards, towards the axis)} \\
> \mathbf e_m &= \cos\varphi\,\mathbf e_r + \sin\varphi\,\mathbf k = \frac{a}{D}\,\mathbf e_r + \frac{2r}{D}\,\mathbf k \quad &\text{(slope triangle: adjacent leg on $\mathbf e_r$, opposite on $\mathbf k$)} \\
> \mathbf e_m\times\mathbf e_\theta &= \cos\varphi\,\mathbf k + \sin\varphi\left(-\mathbf e_r\right) = \mathbf n \quad &\text{($\mathbf e_r\times\mathbf e_\theta = \mathbf k$, $\mathbf k\times\mathbf e_\theta = -\mathbf e_r$: right-handed)} \\
> \det[{}_1R_2] &= \cos\varphi\cos\varphi - 0 + \left(-\sin\varphi\right)\left(-\sin\varphi\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{13} &= \cos\varphi\sin\varphi - \sin\varphi\cos\varphi = 0, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{11} = 1 \quad &\text{(rows 1 and 3; row 2 is the unit row of $\mathbf e_\theta$)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \tfrac{a}{D} & 0 & -\tfrac{2r}{D} \cr 0 & 1 & 0 \cr \tfrac{2r}{D} & 0 & \tfrac{a}{D} \end{pmatrix}, \quad D = \sqrt{a^2 + 4r^2}, \quad \det[{}_1R_2] = 1}$$
>
> **Units:** $[\nabla f] = [\mathrm{L}]$; $[D] = [\mathrm{L}]$; the entries are ratios of lengths, dimensionless
> **Meaning:** $\mathbf e_m$ and $\mathbf e_\theta$ span the tangent plane $V_T$ at $P$ and $\mathbf n$ the normal line $V_N$; the basis turns with the particle and tilts more as it climbs.

> [!derivation] Position vector of the particle
> **Law:** position vector in cylindrical coordinates with the constraint substituted
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.28
>
> $$\begin{aligned}
> \mathbf r_0^P &= r\,\mathbf e_r + z\,\mathbf k \quad &\text{(horizontal and vertical legs in the meridian plane)} \\
> &= r\,\mathbf e_r + \frac{r^2}{a}\,\mathbf k \quad &\text{(constraint substituted)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = r\,\mathbf e_r + \frac{r^2}{a}\,\mathbf k}$$
>
> **Units:** $[r^2/a] = [\mathrm{L^2}]/[\mathrm{L}] = [\mathrm{L}]$
> **Meaning:** the two coordinates $r$ and $\theta$ parametrise the paraboloid, so the constraint holds identically.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** time derivatives in $S_0$; derivatives of the unit vectors of a basis that turns about $\mathbf k$; chain and product rules
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.29; Notes.pdf, Eq. 2.30
>
> $$\begin{aligned}
> \dot{\mathbf e}_r &= \dot\theta\,\mathbf k\times\mathbf e_r = \dot\theta\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_r \quad &\text{($\boldsymbol\omega_{10} = \dot\theta\,\mathbf k$)} \\
> \dot z &= \frac{d}{dt}\left(\frac{r^2}{a}\right) = \frac{2r}{a}\,\dot r \quad &\text{(chain rule)} \\
> \ddot z &= \frac{2}{a}\left(\dot r\,\dot r + r\,\ddot r\right) = \frac{2}{a}\left(\dot r^2 + r\ddot r\right) \quad &\text{(product rule on $r\dot r$)} \\
> \mathbf v_0^P &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta + \frac{2r\dot r}{a}\,\mathbf k \quad &\text{(product rule on $r\,\mathbf e_r$; $\mathbf k$ constant)} \\
> \mathbf a_0^P &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \left(\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r + \ddot z\,\mathbf k \quad &\text{(product rule on each term)} \\
> &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta + \frac{2}{a}\left(\dot r^2 + r\ddot r\right)\mathbf k \quad &\text{(grouped)} \\
> |\mathbf v_0^P|^2 &= \dot r^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot\theta^2 \quad &\text{(orthonormal components)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta + \frac{2r\dot r}{a}\,\mathbf k, \qquad \mathbf a_0^P = \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta + \frac{2}{a}\left(\dot r^2 + r\ddot r\right)\mathbf k}$$
>
> **Units:** $[\dot r] = [r\dot\theta] = [r\dot r/a] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$, e.g. $[\dot r^2/a] = [\mathrm{L^2\,T^{-2}}]/[\mathrm{L}]$
> **Meaning:** the velocity is tangent to the surface: its $\mathbf e_r$ and $\mathbf k$ components are in the ratio $a$ to $2r$, the direction of $\mathbf e_m$.

### Forces and Equations of Motion

The free-body diagram in the meridian plane shows the weight and the normal reaction; $S_0$ is inertial, so there are no inertia forces.

![[attachments/EM-SOL/p19-fbd.svg]]

> [!derivation] Newton's second law with the reaction, projected on the surface basis
> **Law:** Newton's second law in an inertial frame with the constraint force; tangent projections free of the reaction, normal projection for the reaction
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.11; [Lecture 3, Slide 14]
>
> Write the acceleration components as $A_r$, $A_\theta$, $A_z$ (those of the kinematics box).
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf k + N\,\mathbf n \quad &\text{(all forces: weight and reaction)} \\
> \mathbf a_0^P\cdot\mathbf e_m &= \frac{a A_r + 2r A_z}{D}, \quad \mathbf a_0^P\cdot\mathbf n = \frac{-2r A_r + a A_z}{D} \quad &\text{(components of $\mathbf e_m$, $\mathbf n$ in $\mathcal B_1$)} \\
> \mathbf e_m:\ m\left[a\left(\ddot r - r\dot\theta^2\right) + \frac{4r}{a}\left(\dot r^2 + r\ddot r\right)\right] &= -2mgr \quad &\text{($-mg\,\mathbf k\cdot\mathbf e_m = -2mgr/D$; times $D$)} \\
> \mathbf e_\theta:\ m\left(2\dot r\dot\theta + r\ddot\theta\right) &= 0 \quad &\text{(no azimuthal force)} \\
> -2r\left(\ddot r - r\dot\theta^2\right) + 2\left(\dot r^2 + r\ddot r\right) &= 2r^2\dot\theta^2 + 2\dot r^2 \quad &\text{(the $r\ddot r$ terms cancel in $D\,\mathbf a_0^P\cdot\mathbf n$)} \\
> \mathbf n:\ \frac{m}{D}\left(2r^2\dot\theta^2 + 2\dot r^2\right) &= -\frac{mga}{D} + N \quad &\text{($-mg\,\mathbf k\cdot\mathbf n = -mga/D$)}
> \end{aligned}$$
>
> $$\boxed{\ddot r\left(1 + \frac{4r^2}{a^2}\right) + \frac{4r\dot r^2}{a^2} - r\dot\theta^2 + \frac{2g}{a}\,r = 0, \quad 2\dot r\dot\theta + r\ddot\theta = 0, \quad N = \frac{m\left(ga + 2\dot r^2 + 2r^2\dot\theta^2\right)}{\sqrt{a^2 + 4r^2}}}$$
>
> **Units:** first equation divided by $a$: every term $[\mathrm{L\,T^{-2}}]$; $[N] = [\mathrm{M}][\mathrm{L^2\,T^{-2}}]/[\mathrm{L}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two equations of motion free of the reaction for the two degrees of freedom, and the reaction afterwards; $N$ is always positive, so the surface always pushes and the particle never leaves it.

> [!derivation] Areal first integral
> **Law:** the azimuthal equation is an exact derivative; Barrow's rule
> **Source:** Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 2.30
>
> $$\begin{aligned}
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 2r\dot r\dot\theta + r^2\ddot\theta = r\left(2\dot r\dot\theta + r\ddot\theta\right) = 0 \quad &\text{(product and chain rules; azimuthal equation)} \\
> \left[r^2\dot\theta\right]_0^t &= r^2\dot\theta - a^2\,\frac{v_0}{a} = 0 \quad &\text{(Barrow's rule; $\dot\theta(0) = v_0/a$)}
> \end{aligned}$$
>
> $$\boxed{r^2\dot\theta = a v_0}$$
>
> **Units:** $[\mathrm{L^2\,T^{-1}}]$ on both sides
> **Meaning:** no force has a moment about the axis $Oz$, so the azimuthal rate grows as the particle approaches the axis.

> [!derivation] Energy integral derived from the meridian equation
> **Law:** the equation of motion multiplied by the rate of the coordinate is an exact derivative (chain rule); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 6.12
>
> $$\begin{aligned}
> \frac{d}{dt}\left[\dot r^2\left(1 + \frac{4r^2}{a^2}\right)\right] &= 2\dot r\ddot r\left(1 + \frac{4r^2}{a^2}\right) + \frac{8r\dot r^3}{a^2} \quad &\text{(product rule; chain rule on $r^2$)} \\
> \frac{d}{dt}\left(\frac{a^2 v_0^2}{r^2}\right) &= -\frac{2a^2v_0^2}{r^3}\,\dot r = -2r\dot\theta^2\,\dot r \quad &\text{(chain rule; $\dot\theta = a v_0/r^2$)} \\
> \frac{d}{dt}\left(\frac{2g}{a}\,r^2\right) &= \frac{4g}{a}\,r\dot r \quad &\text{(chain rule)} \\
> 2\dot r\times\left[\text{meridian equation}\right] &= \frac{d}{dt}\left[\dot r^2\left(1 + \frac{4r^2}{a^2}\right) + \frac{a^2v_0^2}{r^2} + \frac{2g}{a}\,r^2\right] = 0 \quad &\text{(sum of the three derivatives)} \\
> \left[\dot r^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot\theta^2 + \frac{2g}{a}\,r^2\right]_0^t &= 0 \quad &\text{(Barrow's rule; $a^2v_0^2/r^2 = r^2\dot\theta^2$)} \\
> \dot r^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\dot\theta^2 + \frac{2g}{a}\,r^2 &= 0 + v_0^2 + 2ga \quad &\text{(initial data)}
> \end{aligned}$$
>
> $$\boxed{\dot r^2\left(1 + \frac{4r^2}{a^2}\right) + r^2\left(\dot\theta^2 + \frac{2g}{a}\right) = v_0^2 + 2ga}$$
>
> **Units:** every term $[\mathrm{L^2\,T^{-2}}]$: $[g r^2/a] = [\mathrm{L\,T^{-2}}][\mathrm{L}]$
> **Meaning:** it is twice the mechanical energy per unit mass, $|\mathbf v_0^P|^2 + 2gz$: the reaction of the stationary smooth surface does no work and the weight derives from the potential $mgz$.

### Answers and Checks

#### Reduction to quadratures

> [!derivation] Integral in r equal to an integral in t
> **Law:** elimination of the azimuthal rate with the areal integral; factorisation; separation of variables and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44; Problems.pdf, p. 10
>
> Call $r_\ast$ the length with $r_\ast^2 = a v_0^2/(2g)$.
>
> $$\begin{aligned}
> \dot r^2\left(1 + \frac{4r^2}{a^2}\right) &= v_0^2 + 2ga - \frac{a^2v_0^2}{r^2} - \frac{2g}{a}\,r^2 \quad &\text{(areal integral substituted)} \\
> &= -\frac{2g}{a r^2}\left[r^4 - \left(a^2 + \frac{a v_0^2}{2g}\right)r^2 + \frac{a^3v_0^2}{2g}\right] \quad &\text{(common factor $-2g/(a r^2)$)} \\
> &= \frac{2g}{a r^2}\left(a^2 - r^2\right)\left(r^2 - r_\ast^2\right) \quad &\text{(quadratic in $r^2$: roots $a^2$ and $r_\ast^2$, sum and product checked)} \\
> \dot r^2 &= \frac{2ga\left(a^2 - r^2\right)\left(r^2 - r_\ast^2\right)}{r^2\left(a^2 + 4r^2\right)} \quad &\text{(division by $1 + 4r^2/a^2$)} \\
> \int_a^{r}\frac{r'\sqrt{a^2 + 4r'^2}}{\sqrt{2ga\left(a^2 - r'^2\right)\left(r'^2 - r_\ast^2\right)}}\,dr' &= \pm\int_0^t dt' = \pm t \quad &\text{(separation of variables; Barrow's rule from $r(0) = a$)} \\
> \theta(t) &= \int_0^t \frac{a v_0}{r(t')^2}\,dt' \quad &\text{(areal integral; Barrow's rule, $\theta(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\int_a^{r}\frac{r'\sqrt{a^2 + 4r'^2}\,dr'}{\sqrt{2ga\left(a^2 - r'^2\right)\left(r'^2 - r_\ast^2\right)}} = \pm t, \qquad \theta = \int_0^t\frac{a v_0\,dt'}{r^2}, \qquad r_\ast = v_0\sqrt{\frac{a}{2g}}}$$
>
> **Units:** $[r\sqrt{a^2 + 4r^2}\,dr] = [\mathrm{L^3}]$; $[\sqrt{ga\,\mathrm{L^4}}] = [\mathrm{L^3\,T^{-1}}]$; the ratio is $[\mathrm{T}]$; $[r_\ast] = [\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** the radicand is positive only between $a$ and $r_\ast$: the radius oscillates between these two values, which are the turning points.

#### Maximum and minimum of r

> [!derivation] Turning points in the three cases
> **Law:** the motion is confined where the squared rate is not negative
> **Source:** Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> \left(a^2 - r^2\right)\left(r^2 - r_\ast^2\right) &\ge 0 \iff \min(a, r_\ast) \le r \le \max(a, r_\ast) \quad &\text{(both factors must have the same sign)} \\
> r_\ast \lt a &\iff v_0^2 \lt 2ga \quad &\text{($r_\ast^2 = a v_0^2/(2g)$ compared with $a^2$)}
> \end{aligned}$$
>
> $$\boxed{v_0 \lt \sqrt{2ga}:\ r_{\max} = a,\ r_{\min} = v_0\sqrt{\tfrac{a}{2g}}; \quad v_0 = \sqrt{2ga}:\ r \equiv a; \quad v_0 \gt \sqrt{2ga}:\ r_{\min} = a,\ r_{\max} = v_0\sqrt{\tfrac{a}{2g}}}$$
>
> **Units:** $[\sqrt{ga}] = [\mathrm{L\,T^{-1}}]$, a speed, as $v_0$
> **Meaning:** slower than the circular speed the particle slides down from the start parallel and comes back; faster, it climbs; at exactly $\sqrt{2ga}$ it stays on the parallel of radius $a$.

> [!derivation] Check: the circular orbit and its reaction
> **Law:** Newton's second law on the parallel of radius a
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> -a\dot\theta^2 + \frac{2g}{a}\,a &= 0 \Rightarrow a^2\dot\theta^2 = 2ga \quad &\text{(meridian equation with $r = a$, $\dot r = \ddot r = 0$)} \\
> N &= \frac{m\left(ga + 0 + 2\cdot 2ga\right)}{\sqrt{a^2 + 4a^2}} = \frac{5mga}{\sqrt5\,a} = \sqrt5\,mg \quad &\text{(reaction formula with $a^2\dot\theta^2 = 2ga$)} \\
> N\,\mathbf n\cdot\mathbf k &= \sqrt5\,mg\,\frac{a}{\sqrt5\,a} = mg, \quad N\,\mathbf n\cdot\left(-\mathbf e_r\right) = \sqrt5\,mg\,\frac{2a}{\sqrt5\,a} = 2mg \quad &\text{(components of the reaction)}
> \end{aligned}$$
>
> $$\boxed{v_0^2 = 2ga, \qquad N = \sqrt5\,mg: \ \text{vertical part } mg,\ \text{inward part } 2mg = \frac{m v_0^2}{a}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the vertical part of the reaction carries the weight and its inward part is the centripetal force; this agrees with the double root of the quadrature.

> [!derivation] Limiting case: no initial velocity
> **Law:** behaviour of the turning points when the speed vanishes
> **Source:** Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> r_\ast &= v_0\sqrt{\frac{a}{2g}} \to 0 \quad &\text{($v_0 \to 0$)} \\
> r^2\dot\theta &= a v_0 \to 0 \quad &\text{(the areal constant vanishes)}
> \end{aligned}$$
>
> $$\boxed{v_0 = 0:\ \dot\theta \equiv 0,\ 0 \le r \le a,\ \text{oscillation through the vertex in a fixed meridian plane}}$$
>
> **Units:** lengths $[\mathrm{L}]$
> **Meaning:** without azimuthal speed nothing keeps the particle away from the axis, so it slides through the vertex in a vertical plane, like a bead on the meridian parabola; for small $v_0 \gt 0$ the rate at the inner turning radius, $a v_0/r_\ast^2 = 2g/v_0$, is large, so the particle swings round the axis by nearly $\pi$ each time it passes close to it.

| Part of the statement | Answer |
| :--- | :--- |
| Equations of motion | $\ddot r(1 + 4r^2/a^2) + 4r\dot r^2/a^2 - r\dot\theta^2 + 2gr/a = 0$; $2\dot r\dot\theta + r\ddot\theta = 0$; $N = m(ga + 2\dot r^2 + 2r^2\dot\theta^2)/\sqrt{a^2 + 4r^2}$ along $\mathbf n$ |
| First integrals | $r^2\dot\theta = a v_0$; $\dot r^2(1 + 4r^2/a^2) + r^2(\dot\theta^2 + 2g/a) = v_0^2 + 2ga$ |
| Quadrature | $\int_a^r \frac{r'\sqrt{a^2 + 4r'^2}\,dr'}{\sqrt{2ga(a^2 - r'^2)(r'^2 - r_\ast^2)}} = \pm t$, with $r_\ast = v_0\sqrt{a/(2g)}$; $\theta = \int_0^t a v_0\,dt'/r^2$ |
| Maximum and minimum of $r$ | $v_0 \lt \sqrt{2ga}$: $r_{\max} = a$, $r_{\min} = r_\ast$; $v_0 = \sqrt{2ga}$: $r \equiv a$; $v_0 \gt \sqrt{2ga}$: $r_{\min} = a$, $r_{\max} = r_\ast$ |

**Check against the official key:** Problems.pdf, p. 73, item 19, prints the energy quadrature and the areal integral of the boxes above, identical term by term, and the same three cases for the extreme radii: **match**. The key prints the second turning radius as $v_0\sqrt{a/2g}$, the same value.

---

## Problem 23: Simple Pendulum

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ moves on the inside of a smooth vertical circumference of radius $L$ and centre $O$, which is the simple pendulum with a string that can go slack. The statement asks, first with the circumference at rest, for the motion after a push $v_0$ at the lowest point, the point where the particle leaves the circumference and whether that point is reached; then, with the circumference turning about the vertical diameter at the constant rate $\omega$, for the equations of motion and the equilibrium positions (Problems.pdf, p. 11). The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7 and writes both parts at once: the fixed circumference is the case of zero $\omega$.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre of the circumference (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, $\mathbf j$ vertical **upward** (the axis of the turning diameter), $\mathbf i$ and $\mathbf k$ horizontal, right-handed; the plane $Oxy$ holds the circumference at $t = 0$, as in Notes.pdf, Fig. 4.3 |
| Basis of the plane of the circumference | $\mathcal B_1 = \{\mathbf i_1, \mathbf j, \mathbf k_1\}$, $\mathcal B_0$ turned by the angle $\omega t$ about $\mathbf j$; the circumference lies in the plane of $\mathbf i_1$ and $\mathbf j$ (for zero $\omega$, $\mathcal B_1$ is $\mathcal B_0$) |
| Polar basis | $\mathcal B_2 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k_1\}$: $\mathbf e_R$ from $O$ to $P$, $\mathbf e_\theta$ along increasing $\theta$, $\mathbf k_1$ normal to the plane |
| Coordinate | $\theta$, the angle of $OP$ from the downward vertical, positive towards $\mathbf i_1$ (the coordinate of Notes.pdf, Sec. 4.7) |
| Constraints | (1) plane of the circumference: $\mathbf r_0^P\cdot\mathbf k_1(t) = 0$, holonomic, bilateral, stationary for zero $\omega$ and rheonomic (time-dependent) when it turns; (2) circumference: $|\mathbf r_0^P| = L$ while in contact, holonomic, stationary, **unilateral** (the particle is inside and may move towards $O$, $|\mathbf r_0^P| \le L$) ([Lecture 3, Slide 21]) |
| Degrees of freedom | 3 minus 2 constraints: one unknown function, $\theta(t)$. The rheonomic plane makes time appear explicitly (the lecture counts $t$ as an extra coordinate, [Lecture 3, Slide 21]), but $\omega t$ is prescribed, so $\theta$ is the only coordinate to solve for |
| Data | $m$ [kg], $L$ [m], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$], $\omega$ [rad s$^{-1}$] |
| Applied force | weight $-mg\,\mathbf j$ |
| Reaction | normal subspace of a curve, dimension 2 (Notes.pdf, Eq. 6.16): $\mathbf N = -N\,\mathbf e_R + N_b\,\mathbf k_1$, with $N \ge 0$ (the circumference pushes towards $O$) and $N_b$ of either sign (the plane holds the particle on both sides) |
| Initial conditions (fixed circumference) | $\theta(0) = 0$ (lowest point), $L\dot\theta(0) = v_0 \gt 0$ |
| Hypotheses | smooth contact; the reaction of the inner face can only push towards the centre, so the particle leaves the circumference when $N$ reaches zero (Notes.pdf, Sec. 6.4) |

![[attachments/EM-SOL/p23-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p23-rotation-j.svg]]

> [!derivation] Plane of the circumference: rotation about the vertical j
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19
>
> View from above, along $\mathbf j$: since $\mathbf j$ is the cross product of $\mathbf k$ and $\mathbf i$, drawing $\mathbf k$ to the right and $\mathbf i$ up makes $\mathbf j$ point out of the paper (⊙), and a positive rotation about $\mathbf j$ is counterclockwise. The plane turns counterclockwise by $\omega t$. The vector $\mathbf i_1$ is $\mathbf i$ turned by $\omega t$: hypotenuse 1, adjacent leg $\cos\omega t$ along $\mathbf i$, opposite leg $\sin\omega t$ along minus $\mathbf k$, because the upward vector of the view turned counterclockwise leans to the left, towards minus $\mathbf k$ (the minus sign). The vector $\mathbf k_1$ is $\mathbf k$ turned by the same angle: adjacent leg $\cos\omega t$ along $\mathbf k$, opposite leg $\sin\omega t$ along $\mathbf i$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i - \sin\omega t\,\mathbf k, \quad \mathbf k_1 = \sin\omega t\,\mathbf i + \cos\omega t\,\mathbf k \quad &\text{(the two right triangles of the view)} \\
> \mathbf i_1\times\mathbf j &= \cos\omega t\,\mathbf k - \sin\omega t\,\mathbf k\times\mathbf j = \cos\omega t\,\mathbf k + \sin\omega t\,\mathbf i = \mathbf k_1 \quad &\text{(right-handed: $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \det[{}_0R_1] &= \cos\omega t\left(1\cdot\cos\omega t - 0\right) - 0 + \sin\omega t\left(0 - 1\cdot\left(-\sin\omega t\right)\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\omega t + \sin^2\omega t = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{13} = -\cos\omega t\sin\omega t + \sin\omega t\cos\omega t = 0 \quad &\text{(rows 1 and 3; row 2 is the unit row of $\mathbf j$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & 0 & \sin\omega t \cr 0 & 1 & 0 \cr -\sin\omega t & 0 & \cos\omega t \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines; $[\omega t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$
> **Meaning:** the columns are $\mathbf i_1$, $\mathbf j$, $\mathbf k_1$ written in $\mathcal B_0$; for zero $\omega$ the matrix is the identity and the circumference stays in the plane $Oxy$.

> [!derivation] Polar basis in the plane: angle from the downward vertical
> **Law:** elementary rotation about the third axis, with the angle related to the usual polar angle
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24; Notes.pdf, Sec. 4.7
>
> View along $\mathbf k_1$, with $\mathbf i_1$ to the right and $\mathbf j$ up: $\mathbf k_1$, the cross product of $\mathbf i_1$ and $\mathbf j$, points out of the paper (⊙), and positive angles are counterclockwise. The angle $\theta$ is measured from the downward vertical, minus $\mathbf j$, so the usual polar angle of $OP$, measured from $\mathbf i_1$, is $\theta - \pi/2$, and $\mathbf e_R$ is Notes.pdf, Eq. 1.20 with that angle. The right triangle of $OP$ has hypotenuse $L$, the horizontal leg $L\sin\theta$ (opposite to $\theta$, along $\mathbf i_1$) and the vertical leg $L\cos\theta$ (adjacent to $\theta$, along minus $\mathbf j$): this is why $\mathbf e_R$ has a minus sign on $\mathbf j$. The vector $\mathbf e_\theta$ is $\mathbf e_R$ turned by a quarter turn counterclockwise.
>
> $$\begin{aligned}
> \cos\left(\theta - \tfrac{\pi}{2}\right) &= \cos\theta\cos\tfrac{\pi}{2} + \sin\theta\sin\tfrac{\pi}{2} = \sin\theta \quad &\text{(cosine of a difference)} \\
> \sin\left(\theta - \tfrac{\pi}{2}\right) &= \sin\theta\cos\tfrac{\pi}{2} - \cos\theta\sin\tfrac{\pi}{2} = -\cos\theta \quad &\text{(sine of a difference)} \\
> \mathbf e_R &= \sin\theta\,\mathbf i_1 - \cos\theta\,\mathbf j \quad &\text{(opposite leg along $\mathbf i_1$, adjacent leg along $-\mathbf j$, over $L$)} \\
> \mathbf e_\theta &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j \quad &\text{($\mathbf e_R$ turned by $\pi/2$ counterclockwise)} \\
> \mathbf e_R\times\mathbf e_\theta &= \sin^2\theta\,\mathbf i_1\times\mathbf j - \cos^2\theta\,\mathbf j\times\mathbf i_1 = \left(\sin^2\theta + \cos^2\theta\right)\mathbf k_1 = \mathbf k_1 \quad &\text{(right-handed)} \\
> \det[{}_1R_2] &= 1\cdot\left(\sin\theta\cdot\sin\theta - \cos\theta\cdot\left(-\cos\theta\right)\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{12} &= -\sin\theta\cos\theta + \cos\theta\sin\theta = 0, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{11} = \sin^2\theta + \cos^2\theta = 1 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \cr -\cos\theta & \sin\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \mathbf i_1 = \sin\theta\,\mathbf e_R + \cos\theta\,\mathbf e_\theta, \quad \mathbf j = -\cos\theta\,\mathbf e_R + \sin\theta\,\mathbf e_\theta}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** at the lowest point $\mathbf e_R$ is minus $\mathbf j$ and $\mathbf e_\theta$ is $\mathbf i_1$; the inverse relations, read from the rows, are used to project the weight.

> [!derivation] Position vector of the particle
> **Law:** position vector of a point on a circumference of centre O
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 4.33
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = L\,\mathbf e_R \quad &\text{(both constraints substituted: radius $L$, in the plane)} \\
> &= L\sin\theta\,\mathbf i_1 - L\cos\theta\,\mathbf j \quad &\text{(legs of the right triangle)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = L\,\mathbf e_R = L\sin\theta\,\mathbf i_1 - L\cos\theta\,\mathbf j}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** one coordinate $\theta$ fixes the particle while it is in contact; the height of $P$ above $O$ is $-L\cos\theta$.

### Kinematics

> [!derivation] Derivatives of the unit vectors
> **Law:** derivative of a unit vector turning about a fixed axis; chain and product rules
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \dot{\mathbf i}_2 &= \omega\,\mathbf j\times\mathbf i_1 = -\omega\,\mathbf k_1, \quad \dot{\mathbf k}_2 = \omega\,\mathbf j\times\mathbf k_1 = \omega\,\mathbf i_1, \quad \dot{\mathbf j} = \mathbf 0 \quad &\text{($\mathcal B_1$ turns about $\mathbf j$ at the rate $\omega$; $\mathbf j\times\mathbf i_1 = -\mathbf k_1$, $\mathbf j\times\mathbf k_1 = \mathbf i_1$)} \\
> \dot{\mathbf e}_R &= \cos\theta\,\dot\theta\,\mathbf i_1 + \sin\theta\,\dot{\mathbf i}_2 + \sin\theta\,\dot\theta\,\mathbf j \quad &\text{(product rule; chain rule on $\sin\theta$, $-\cos\theta$)} \\
> &= \dot\theta\,\mathbf e_\theta - \omega\sin\theta\,\mathbf k_1 \quad &\text{(grouped with $\mathbf e_\theta$)} \\
> \dot{\mathbf e}_\theta &= -\sin\theta\,\dot\theta\,\mathbf i_1 + \cos\theta\,\dot{\mathbf i}_2 + \cos\theta\,\dot\theta\,\mathbf j = -\dot\theta\,\mathbf e_R - \omega\cos\theta\,\mathbf k_1 \quad &\text{(same rules)} \\
> \dot{\mathbf k}_2 &= \omega\left(\sin\theta\,\mathbf e_R + \cos\theta\,\mathbf e_\theta\right) \quad &\text{($\mathbf i_1$ written in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_R = \dot\theta\,\mathbf e_\theta - \omega\sin\theta\,\mathbf k_1, \quad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_R - \omega\cos\theta\,\mathbf k_1, \quad \dot{\mathbf k}_2 = \omega\left(\sin\theta\,\mathbf e_R + \cos\theta\,\mathbf e_\theta\right)}$$
>
> **Units:** $[\dot\theta] = [\omega] = [\mathrm{T^{-1}}]$
> **Meaning:** besides turning with $\theta$ inside the plane, the polar vectors are dragged out of the plane by the rotation of the circumference.

> [!derivation] Velocity and acceleration of the particle
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 4.34; Notes.pdf, Eq. 4.35
>
> $$\begin{aligned}
> \mathbf v_0^P &= L\,\dot{\mathbf e}_R = L\dot\theta\,\mathbf e_\theta - L\omega\sin\theta\,\mathbf k_1 \quad &\text{($L$ constant)} \\
> \mathbf a_0^P &= L\ddot\theta\,\mathbf e_\theta + L\dot\theta\,\dot{\mathbf e}_\theta - L\omega\cos\theta\,\dot\theta\,\mathbf k_1 - L\omega\sin\theta\,\dot{\mathbf k}_2 \quad &\text{(product rule; $\omega$ constant; chain rule on $\sin\theta$)} \\
> &= L\ddot\theta\,\mathbf e_\theta - L\dot\theta^2\,\mathbf e_R - 2L\omega\dot\theta\cos\theta\,\mathbf k_1 - L\omega^2\sin\theta\left(\sin\theta\,\mathbf e_R + \cos\theta\,\mathbf e_\theta\right) \quad &\text{(derivatives of the unit vectors)} \\
> &= -L\left(\dot\theta^2 + \omega^2\sin^2\theta\right)\mathbf e_R + L\left(\ddot\theta - \omega^2\sin\theta\cos\theta\right)\mathbf e_\theta - 2L\omega\dot\theta\cos\theta\,\mathbf k_1 \quad &\text{(grouped)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = L\dot\theta\,\mathbf e_\theta - L\omega\sin\theta\,\mathbf k_1, \quad \mathbf a_0^P = -L\left(\dot\theta^2 + \omega^2\sin^2\theta\right)\mathbf e_R + L\left(\ddot\theta - \omega^2\sin\theta\cos\theta\right)\mathbf e_\theta - 2L\omega\dot\theta\cos\theta\,\mathbf k_1}$$
>
> **Units:** $[L\dot\theta] = [L\omega] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** for zero $\omega$ these are Notes.pdf, Eq. 4.34 and Eq. 4.35; with rotation the particle is also carried round the vertical axis on a circle of radius $L\sin\theta$.

### Forces and Equations of Motion

The free-body diagram shows the weight, the reaction of the circumference towards $O$ and the reaction of the turning plane, normal to it. The frame $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p23-fbd.svg]]

> [!derivation] Newton's second law with all the reactions, projected on the polar basis
> **Law:** Newton's second law in an inertial frame with the constraint forces of a curve; tangent projection free of reactions
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.36; Notes.pdf, Eq. 6.13; Notes.pdf, Eq. 6.16
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf j - N\,\mathbf e_R + N_b\,\mathbf k_1 \quad &\text{(weight and the two reaction components; unknowns $\theta$, $N$, $N_b$)} \\
> -mg\,\mathbf j &= mg\cos\theta\,\mathbf e_R - mg\sin\theta\,\mathbf e_\theta \quad &\text{($\mathbf j$ in $\mathcal B_2$, second row of $[{}_1R_2]$)} \\
> \mathbf e_\theta:\ mL\left(\ddot\theta - \omega^2\sin\theta\cos\theta\right) &= -mg\sin\theta \quad &\text{(tangent: no reaction)} \\
> \mathbf e_R:\ -mL\left(\dot\theta^2 + \omega^2\sin^2\theta\right) &= mg\cos\theta - N \quad &\text{(normal in the plane)} \\
> \mathbf k_1:\ -2mL\omega\dot\theta\cos\theta &= N_b \quad &\text{(normal to the plane)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \left(\frac{g}{L} - \omega^2\cos\theta\right)\sin\theta = 0, \quad N = mL\left(\dot\theta^2 + \omega^2\sin^2\theta\right) + mg\cos\theta, \quad N_b = -2mL\omega\dot\theta\cos\theta}$$
>
> **Units:** $[g/L] = [\omega^2] = [\mathrm{T^{-2}}]$, as $[\ddot\theta]$; $[N] = [N_b] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** these are the new equations of motion asked for the turning circumference; for zero $\omega$ they reduce to the pendulum of Notes.pdf, Eq. 4.37 and Eq. 4.38 (with $N$ in the role of the tension) and the plane exerts no force (Eq. 4.37 is printed with $+F_t$; with the tension $-F_t\,\mathbf e_R$ of the notes the term is $-F_t$, as $-N$ here).

#### Fixed circumference

> [!derivation] Energy integral derived from the pendulum equation
> **Law:** the tangent equation multiplied by the angular rate is an exact derivative; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.39; Notes.pdf, Eq. 4.42; Notes.pdf, Eq. 6.12
>
> $$\begin{aligned}
> \dot\theta\ddot\theta + \frac{g}{L}\sin\theta\,\dot\theta &= 0 \quad &\text{(zero $\omega$; equation times $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\dot\theta^2\right) &= \dot\theta\ddot\theta, \quad \frac{d}{dt}\left(-\frac{g}{L}\cos\theta\right) = \frac{g}{L}\sin\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \left[\tfrac12\dot\theta^2 - \frac{g}{L}\cos\theta\right]_0^t &= 0 \quad &\text{(Barrow's rule between $0$ and $t$)} \\
> \tfrac12\dot\theta^2 - \frac{g}{L}\cos\theta &= \frac{v_0^2}{2L^2} - \frac{g}{L} \quad &\text{($\theta(0) = 0$, $\dot\theta(0) = v_0/L$)} \\
> L^2\dot\theta^2 &= v_0^2 - 2gL\left(1 - \cos\theta\right) \quad &\text{(times $2L^2$)}
> \end{aligned}$$
>
> $$\boxed{v^2(\theta) = L^2\dot\theta^2 = v_0^2 - 2gL\left(1 - \cos\theta\right)}$$
>
> **Units:** every term $[\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy is conserved: the reactions of the fixed smooth circumference are normal to the velocity and do no work; the speed falls as the particle rises.

> [!derivation] Motion reduced to a quadrature
> **Law:** separation of variables; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44
>
> $$\begin{aligned}
> \frac{d\theta}{dt} &= \frac{1}{L}\sqrt{v_0^2 - 2gL\left(1 - \cos\theta\right)} \quad &\text{(energy integral, $\dot\theta \gt 0$ after the push)} \\
> \int_0^{\theta}\frac{L\,d\theta'}{\sqrt{v_0^2 - 2gL\left(1 - \cos\theta'\right)}} &= \int_0^t dt' = \left[t'\right]_0^t = t \quad &\text{(separation of variables; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{t(\theta) = \int_0^{\theta}\frac{L\,d\theta'}{\sqrt{v_0^2 - 2gL\left(1 - \cos\theta'\right)}}}$$
>
> **Units:** $[L\,d\theta/v] = [\mathrm{L}]/[\mathrm{L\,T^{-1}}] = [\mathrm{T}]$
> **Meaning:** valid while the particle is in contact and moves forward; the denominator vanishes at a turning point and the reaction formula tells whether contact is lost first.

> [!derivation] Reaction of the circumference and the point where it vanishes
> **Law:** the normal projection with the energy integral; separation from a unilateral constraint when the reaction vanishes
> **Source:** Notes.pdf, Eq. 4.37; Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]
>
> $$\begin{aligned}
> N &= mL\dot\theta^2 + mg\cos\theta = \frac{m}{L}\left[v_0^2 - 2gL\left(1 - \cos\theta\right)\right] + mg\cos\theta \quad &\text{(zero $\omega$; energy integral)} \\
> &= \frac{m v_0^2}{L} - mg\left(2 - 3\cos\theta\right) \quad &\text{(terms in $mg$ collected)} \\
> \frac{dN}{d\theta} &= -3mg\sin\theta \lt 0 \ \text{for } 0 \lt \theta \lt \pi \quad &\text{(the reaction decreases as the particle rises)} \\
> N(\theta_d) &= 0 \iff \cos\theta_d = \frac{2gL - v_0^2}{3gL} \quad &\text{(separation condition)} \\
> v^2(\theta_d) &= v_0^2 - 2gL + 2gL\,\frac{2gL - v_0^2}{3gL} = \frac{v_0^2 - 2gL}{3} \quad &\text{(energy integral at $\theta_d$)}
> \end{aligned}$$
>
> $$\boxed{N(\theta) = \frac{m v_0^2}{L} - mg\left(2 - 3\cos\theta\right), \qquad \cos\theta_d = \frac{2gL - v_0^2}{3gL}}$$
>
> **Units:** $[m v_0^2/L] = [mg] = [\mathrm{M\,L\,T^{-2}}]$; $\cos\theta_d$ dimensionless: $[gL] = [v_0^2] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** contact is lost where the inward reaction would have to become a pull; it can only happen in the upper half, where the weight has an inward component (Eq. 4.37 is printed with $+F_t$; with the tension $-F_t\,\mathbf e_R$ of the notes the term is $-F_t$, as $-N$ here).

> [!derivation] Is the separation point reached? The three regimes
> **Law:** the particle reaches a point only if the speed squared stays positive up to it; sign of the reaction
> **Source:** Notes.pdf, Eq. 4.43; Notes.pdf, Sec. 6.4
>
> The speed vanishes at the angle with $\cos\theta_\ast = 1 - v_0^2/(2gL)$ (energy integral equal to zero).
>
> $$\begin{aligned}
> v_0^2 \le 2gL &\Rightarrow \cos\theta_\ast \ge 0, \quad N(\theta_\ast) = 0 + mg\cos\theta_\ast \ge 0 \quad &\text{(the particle stops in the lower half while still pressed)} \\
> 2gL \lt v_0^2 \lt 5gL &\Rightarrow -1 \lt \cos\theta_d \lt 0, \quad v^2(\theta_d) = \frac{v_0^2 - 2gL}{3} \gt 0 \quad &\text{(separation in the upper half, reached with speed)} \\
> v_0^2 \ge 5gL &\Rightarrow N(\pi) = \frac{m v_0^2}{L} - 5mg \ge 0, \quad N(\theta) \ge N(\pi) \quad &\text{(the reaction never vanishes: complete turns)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{ll} v_0 \le \sqrt{2gL}: & \text{oscillation in the lower half, } \theta_d \text{ never reached} \cr \sqrt{2gL} \lt v_0 \lt \sqrt{5gL}: & \text{the particle leaves at } \theta_d = \arccos\dfrac{2gL - v_0^2}{3gL} \in \left(\tfrac{\pi}{2}, \pi\right) \cr v_0 \ge \sqrt{5gL}: & \text{complete loops, never leaves} \end{array}}$$
>
> **Units:** $[\sqrt{gL}] = [\mathrm{L\,T^{-1}}]$, a speed
> **Meaning:** a small push gives the classical pendulum; a medium push lifts the particle above the horizontal diameter, where it falls off the circumference and continues as a projectile under gravity alone until it meets the circumference again; only a push of at least $\sqrt{5gL}$ keeps it in contact round the top.

#### Turning circumference

> [!derivation] First integral of the turning case and the work of the plane
> **Law:** the tangent equation multiplied by the angular rate (chain rule); power of a time-dependent constraint
> **Source:** Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]; Notes.pdf, Eq. 4.11
>
> $$\begin{aligned}
> \dot\theta\ddot\theta + \frac{g}{L}\sin\theta\,\dot\theta - \omega^2\sin\theta\cos\theta\,\dot\theta &= 0 \quad &\text{(equation of motion times $\dot\theta$)} \\
> \frac{d}{dt}\left(-\tfrac12\omega^2\sin^2\theta\right) &= -\omega^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \left[\tfrac12\dot\theta^2 - \frac{g}{L}\cos\theta - \tfrac12\omega^2\sin^2\theta\right]_0^t &= 0 \quad &\text{(sum of exact derivatives; Barrow's rule)} \\
> \mathbf N\cdot\mathbf v_0^P &= N_b\,\mathbf k_1\cdot\left(-L\omega\sin\theta\,\mathbf k_1\right) = 2mL^2\omega^2\dot\theta\sin\theta\cos\theta \quad &\text{(power of the reaction: only the plane works)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12\dot\theta^2 - \frac{g}{L}\cos\theta - \tfrac12\omega^2\sin^2\theta = \text{const}, \qquad \mathbf N\cdot\mathbf v_0^P = 2mL^2\omega^2\dot\theta\sin\theta\cos\theta \ne 0}$$
>
> **Units:** first integral $[\mathrm{T^{-2}}]$ in every term; power $[\mathrm{M\,L^2\,T^{-3}}]$
> **Meaning:** the turning plane is a rheonomic constraint and does work, so the mechanical energy in $S_0$ is not conserved; the conserved quantity above is a different one, read off the equation of motion.

> [!derivation] Equilibrium positions on the turning circumference
> **Law:** equilibrium: the coordinate stays constant, so its rate and acceleration vanish in the equation of motion; admissibility by the sign of the unilateral reaction
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> \left(\frac{g}{L} - \omega^2\cos\theta_e\right)\sin\theta_e &= 0 \quad &\text{(constant $\theta$: $\dot\theta = \ddot\theta = 0$)} \\
> \sin\theta_e = 0 &\Rightarrow \theta_e = 0 \ \text{or} \ \theta_e = \pi \quad &\text{(lowest and highest points)} \\
> \cos\theta_e = \frac{g}{\omega^2 L} &\Rightarrow \theta_e = \pm\arccos\frac{g}{\omega^2 L}, \ \text{only if } \omega^2 \gt \frac{g}{L} \quad &\text{(a cosine cannot exceed 1; at equality the two roots merge with $\theta_e = 0$)} \\
> N(0) &= mg \gt 0, \quad N(\pi) = -mg \lt 0 \quad &\text{(reaction at rest: $N = mL\omega^2\sin^2\theta_e + mg\cos\theta_e$)} \\
> N(\theta_e) &= mL\omega^2\sin^2\theta_e + \frac{mg^2}{\omega^2 L} \gt 0, \quad N_b = 0 \quad &\text{(off-axis positions, $\dot\theta = 0$)}
> \end{aligned}$$
>
> $$\boxed{\theta_e = 0 \ \text{always}; \quad \theta_e = \pm\arccos\frac{g}{\omega^2 L} \ \text{if } \omega^2 \gt \frac{g}{L}; \quad \theta_e = \pi \ \text{excluded (it needs a pull)}}$$
>
> **Units:** $[g/(\omega^2 L)] = [\mathrm{L\,T^{-2}}]/([\mathrm{T^{-2}}][\mathrm{L}]) = [1]$; $[N(\theta_e)] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** above the critical rate $\sqrt{g/L}$ the particle can ride at rest relative to the circumference on a horizontal circle of radius $L\sin\theta_e$, where the inward reaction and the weight give the centripetal force; the top would be an equilibrium only for a bead threaded on a wire, not for the inside of the circumference.

> [!derivation] Stability of the equilibria
> **Law:** linearisation of the equation of motion about an equilibrium
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 5.6
>
> Write the equation as the second derivative of $\theta$ equal to $F(\theta)$, with $F(\theta) = -(g/L - \omega^2\cos\theta)\sin\theta$. A small deviation $\delta$ obeys the second derivative of $\delta$ equal to $F'(\theta_e)\,\delta$: stable when $F'(\theta_e)$ is negative.
>
> $$\begin{aligned}
> F(\theta) &= -\frac{g}{L}\sin\theta + \frac{\omega^2}{2}\sin 2\theta \quad &\text{($\sin\theta\cos\theta = \tfrac12\sin 2\theta$)} \\
> F'(\theta) &= -\frac{g}{L}\cos\theta + \omega^2\cos 2\theta \quad &\text{(chain rule on $\sin 2\theta$)} \\
> F'(0) &= \omega^2 - \frac{g}{L} \quad &\text{(lowest point)} \\
> F'(\theta_e) &= -\omega^2\cos^2\theta_e + \omega^2\left(2\cos^2\theta_e - 1\right) = -\omega^2\sin^2\theta_e \quad &\text{($g/L = \omega^2\cos\theta_e$; $\cos 2\theta = 2\cos^2\theta - 1$)}
> \end{aligned}$$
>
> $$\boxed{\theta_e = 0 \ \text{stable if } \omega^2 \lt \frac{g}{L},\ \text{unstable if } \omega^2 \gt \frac{g}{L}; \qquad \theta_e = \pm\arccos\frac{g}{\omega^2L} \ \text{stable}}$$
>
> **Units:** $[F'] = [\mathrm{T^{-2}}]$
> **Meaning:** when the rate exceeds $\sqrt{g/L}$ the lowest point loses its stability and the particle settles on one of the two symmetric off-axis positions, which approach the horizontal diameter as the rate grows.

### Answers and Checks

| Part of the statement | Answer |
| :--- | :--- |
| Motion, fixed circumference | $\ddot\theta + (g/L)\sin\theta = 0$; $v^2 = v_0^2 - 2gL(1 - \cos\theta)$; $t = \int_0^\theta L\,d\theta'/\sqrt{v_0^2 - 2gL(1 - \cos\theta')}$; reaction $N = mv_0^2/L - mg(2 - 3\cos\theta)$ towards $O$ |
| Point where it leaves the circumference | $\cos\theta_d = (2gL - v_0^2)/(3gL)$, angle from the lowest point |
| Is it reached? | no if $v_0 \le \sqrt{2gL}$ (oscillation); yes if $\sqrt{2gL} \lt v_0 \lt \sqrt{5gL}$, with $\theta_d$ between $\pi/2$ and $\pi$ and speed $v^2 = (v_0^2 - 2gL)/3$ there; no if $v_0 \ge \sqrt{5gL}$ (complete loops) |
| Equations of motion, turning circumference | $\ddot\theta + (g/L - \omega^2\cos\theta)\sin\theta = 0$; $N = mL(\dot\theta^2 + \omega^2\sin^2\theta) + mg\cos\theta$; $N_b = -2mL\omega\dot\theta\cos\theta$ along $\mathbf k_1$ |
| Equilibrium positions | $\theta_e = 0$ (stable if $\omega^2 \lt g/L$); $\theta_e = \pm\arccos(g/(\omega^2 L))$ if $\omega^2 \gt g/L$ (stable); $\theta_e = \pi$ only for a bilateral constraint, excluded here |

**Check against the official key:** Problems.pdf, p. 73 lists item 23 with no answer, so there is no key to compare with. Independent checks: for zero $\omega$ the equations are those of Notes.pdf, Sec. 4.7; and the separation angle lies between the boundaries computed in the limiting cases below.

> [!derivation] Limiting cases of the separation point
> **Law:** the separation formula at the boundaries of its regime
> **Source:** Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> v_0^2 \to 2gL &\Rightarrow \cos\theta_d \to 0,\ \theta_d \to \tfrac{\pi}{2},\ v^2(\theta_d) \to 0 \quad &\text{(arrives at the horizontal diameter at rest, with zero reaction)} \\
> v_0^2 \to 5gL &\Rightarrow \cos\theta_d \to -1,\ \theta_d \to \pi,\ v^2(\theta_d) \to gL \quad &\text{(at the top the weight alone gives the centripetal acceleration $v^2/L = g$)}
> \end{aligned}$$
>
> $$\boxed{\theta_d \in \left(\tfrac{\pi}{2}, \pi\right) \ \text{moves continuously from the horizontal diameter to the top}}$$
>
> **Units:** $[v^2] = [gL] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the three regimes join continuously, and at the top the critical speed is the classical $\sqrt{gL}$ of a loop.

---

## Problem 24: Particle on a Circumference with a Spring

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ slides on a smooth circumference of radius $a$ and centre $O$ in a vertical plane, pulled by a linear spring of constant $k$ anchored at the point $A$ of the vertical axis at height $\beta a$ (Problems.pdf, p. 12). The statement asks for the potential, the equilibria, the quadratures, the motion in the special case of the spring constant matched to the weight, and then the motion and the reaction when an extra force along the velocity acts. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre of the circumference (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$ of the figure: $\mathbf i$ horizontal to the right, $\mathbf j$ vertical **upward**, $\mathbf k$ the cross product of $\mathbf i$ and $\mathbf j$, out of the paper (⊙) |
| Polar basis | $\mathcal B_1 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$ |
| Coordinate | $\theta$, angle of $OP$ from the axis $Ox$, counterclockwise (figure) |
| Points | $O$ centre; $A$ anchor at $(0, \beta a)$; $P$ particle |
| Constraints | circumference $x^2 + y^2 - a^2 = 0$ and plane $z = 0$: a curve given as the intersection of two surfaces (Notes.pdf, Eq. 6.8); holonomic, stationary, smooth, bilateral (the particle is threaded on the circumference) |
| Degrees of freedom | 3 minus 2: 1, the angle $\theta(t)$ |
| Data | $m$ [kg], $a$ [m], $k$ [N m$^{-1}$], $\beta$ [dimensionless], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$], $\mu$ [s$^{-1}$] |
| Applied forces | weight $-mg\,\mathbf j$; spring $-k\,\overrightarrow{AP}$; parts (e) and (f) also $\mathbf F_\mu = 2m\mu\,\mathbf v_0^P$ |
| Reaction | normal subspace of a curve, dimension 2 (Notes.pdf, Eq. 6.16): $\mathbf N = N_R\,\mathbf e_R + N_k\,\mathbf k$ |
| Initial conditions | $\theta(0) = 0$ (the point $(a, 0)$); $\mathbf v_0^P(0) = v_0\,\mathbf j$, hence $a\dot\theta(0) = v_0$ (see the kinematics) |
| Hypotheses | the spring has zero natural length (the statement gives only its constant; with this reading the force is $-k$ times the vector from $A$ to $P$ (it pulls $P$ towards $A$), the zero-length spring of Notes.pdf, Sec. 7.5); in parts (e) and (f) the spring and weight are those of part (d), $\beta = mg/(ka)$, since the statement continues from part (d), and only with this balance does part (e) have a closed-form position; the extra force is taken literally, along the velocity |

![[attachments/EM-SOL/p24-plane.svg]]

### Change of Basis and Position Vector

> [!derivation] Polar basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View of the figure, $\mathbf k$ out of the paper (⊙), so positive angles are counterclockwise. $\mathbf e_R$ is $\mathbf i$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i$, opposite leg $\sin\theta$ along $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j$, opposite leg $\sin\theta$ along minus $\mathbf i$, since the upward vector turned counterclockwise leans to the left (the minus sign).
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(the two right triangles)} \\
> \mathbf e_R\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta\cos\theta - \left(-\sin\theta\right)\sin\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{12} = \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(rows times rows)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \mathbf i = \cos\theta\,\mathbf e_R - \sin\theta\,\mathbf e_\theta, \quad \mathbf j = \sin\theta\,\mathbf e_R + \cos\theta\,\mathbf e_\theta}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf e_R$ is normal to the circumference and $\mathbf e_\theta$ tangent to it; the inverse relations (rows of the matrix) project the weight and the spring force.

> [!derivation] Position vector of P and the spring vector
> **Law:** position vectors; vector from the anchor to the particle; its modulus
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5; Problems.pdf, p. 12
>
> The right triangle of $OP$ has hypotenuse $a$, horizontal leg $a\cos\theta$ (adjacent to $\theta$) and vertical leg $a\sin\theta$ (opposite). The vector $\overrightarrow{AP}$ has the same horizontal leg and the vertical leg $a\sin\theta$ minus the height $\beta a$ of $A$.
>
> $$\begin{aligned}
> \mathbf r_0^P &= a\,\mathbf e_R = a\cos\theta\,\mathbf i + a\sin\theta\,\mathbf j \quad &\text{(constraints substituted: radius $a$, plane $z = 0$)} \\
> \overrightarrow{AP} &= \mathbf r_0^P - \beta a\,\mathbf j = a\cos\theta\,\mathbf i + a\left(\sin\theta - \beta\right)\mathbf j \quad &\text{($\overrightarrow{OA} = \beta a\,\mathbf j$)} \\
> |\overrightarrow{AP}|^2 &= a^2\cos^2\theta + a^2\left(\sin^2\theta - 2\beta\sin\theta + \beta^2\right) = a^2\left(1 + \beta^2 - 2\beta\sin\theta\right) \quad &\text{(sum of squares; Pythagorean identity)} \\
> \overrightarrow{AP}\cdot\mathbf e_R &= a\cos^2\theta + a\left(\sin\theta - \beta\right)\sin\theta = a\left(1 - \beta\sin\theta\right) \quad &\text{(components of $\mathbf e_R$)} \\
> \overrightarrow{AP}\cdot\mathbf e_\theta &= -a\cos\theta\sin\theta + a\left(\sin\theta - \beta\right)\cos\theta = -a\beta\cos\theta \quad &\text{(components of $\mathbf e_\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf e_R, \qquad \overrightarrow{AP} = a\left(1 - \beta\sin\theta\right)\mathbf e_R - a\beta\cos\theta\,\mathbf e_\theta, \qquad |\overrightarrow{AP}|^2 = a^2\left(1 + \beta^2 - 2\beta\sin\theta\right)}$$
>
> **Units:** $[\mathrm{L}]$ and $[\mathrm{L^2}]$; $\beta$ dimensionless
> **Meaning:** the spring is longest at the bottom and shortest at the top of the circumference.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** derivatives of the polar unit vectors; time derivatives in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 4.34; Notes.pdf, Eq. 4.35
>
> $$\begin{aligned}
> \dot{\mathbf e}_R &= \dot\theta\,\mathbf k\times\mathbf e_R = \dot\theta\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_R \quad &\text{($\boldsymbol\omega_{10} = \dot\theta\,\mathbf k$)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(a\,\mathbf e_R\right) = a\dot\theta\,\mathbf e_\theta \quad &\text{($a$ constant)} \\
> \mathbf a_0^P &= a\ddot\theta\,\mathbf e_\theta + a\dot\theta\,\dot{\mathbf e}_\theta = -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \mathbf v_0^P(0) &= a\dot\theta(0)\,\mathbf e_\theta(0) = a\dot\theta(0)\,\mathbf j = v_0\,\mathbf j \Rightarrow \dot\theta(0) = \frac{v_0}{a} \quad &\text{($\mathbf e_\theta(0) = \mathbf j$; data)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = a\dot\theta\,\mathbf e_\theta, \qquad \mathbf a_0^P = -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta, \qquad \dot\theta(0) = \frac{v_0}{a}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$; $[v_0/a] = [\mathrm{T^{-1}}]$
> **Meaning:** the velocity is tangent to the circumference; the acceleration has the centripetal part along minus $\mathbf e_R$ and the tangential part along $\mathbf e_\theta$.

### Forces and Equations of Motion

The free-body diagram shows the weight, the spring force towards $A$, the reaction (in the plane along $\mathbf e_R$; out of the plane along $\mathbf k$) and, in parts (e) and (f), the force along the velocity. The frame $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p24-fbd.svg]]

> [!derivation] Newton's second law with all the forces, projected on the polar basis
> **Law:** Newton's second law in an inertial frame with the constraint force of a curve; tangent projection free of the reaction
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.13; Notes.pdf, Eq. 6.16; [Lecture 3, Slide 14]
>
> The switch $\epsilon$ is 0 for parts (a) to (d) and 1 for parts (e) and (f).
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf j - k\,\overrightarrow{AP} + \epsilon\,2m\mu\,\mathbf v_0^P + N_R\,\mathbf e_R + N_k\,\mathbf k \quad &\text{(all forces)} \\
> -mg\,\mathbf j &= -mg\sin\theta\,\mathbf e_R - mg\cos\theta\,\mathbf e_\theta \quad &\text{($\mathbf j$ in $\mathcal B_1$)} \\
> -k\,\overrightarrow{AP} &= -ka\left(1 - \beta\sin\theta\right)\mathbf e_R + ka\beta\cos\theta\,\mathbf e_\theta \quad &\text{(spring vector in $\mathcal B_1$)} \\
> \mathbf e_\theta:\ ma\ddot\theta &= \left(ka\beta - mg\right)\cos\theta + \epsilon\,2m\mu a\dot\theta \quad &\text{(tangent: no reaction)} \\
> \mathbf e_R:\ -ma\dot\theta^2 &= -mg\sin\theta - ka\left(1 - \beta\sin\theta\right) + N_R \quad &\text{(normal in the plane)} \\
> \mathbf k:\ 0 &= N_k \quad &\text{(no motion and no applied force out of the plane)}
> \end{aligned}$$
>
> $$\boxed{ma\ddot\theta = \left(ka\beta - mg\right)\cos\theta + \epsilon\,2m\mu a\dot\theta, \qquad N_R = ka + \left(mg - ka\beta\right)\sin\theta - ma\dot\theta^2, \qquad N_k = 0}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$: $[ka] = [\mathrm{M\,T^{-2}}][\mathrm{L}]$, $[m\mu a\dot\theta] = [\mathrm{M}][\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]$
> **Meaning:** the tangent equation is the equation of motion of the single degree of freedom; the radial one gives the reaction afterwards. Weight and spring enter the tangent equation only through the combination $ka\beta - mg$.

### Answers and Checks

#### (a) Potential of the forces

> [!derivation] Potential of the weight and of the spring
> **Law:** a force is conservative when it is minus the gradient of a potential; potential as minus the work along the constraint, with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 6.12
>
> $$\begin{aligned}
> -\nabla\left(mgy\right) &= -mg\,\mathbf j, \quad -\nabla\left(\tfrac12 k\,|\mathbf r - \overrightarrow{OA}|^2\right) = -k\left(\mathbf r - \overrightarrow{OA}\right) = -k\,\overrightarrow{AP} \quad &\text{(gradients: both forces derive from a potential)} \\
> V &= mgy + \tfrac12 k\,|\overrightarrow{AP}|^2 = mga\sin\theta + \tfrac12 ka^2\left(1 + \beta^2 - 2\beta\sin\theta\right) \quad &\text{(on the circumference)} \\
> &= \tfrac12 ka^2\left(1 + \beta^2\right) + \left(mg - ka\beta\right)a\sin\theta \quad &\text{(terms in $\sin\theta$ collected)} \\
> V(\theta) - V(0) &= -\int_0^{\theta}\left(\mathbf F_g + \mathbf F_s\right)\cdot\mathbf e_\theta\,a\,d\theta' = -\int_0^{\theta}\left(ka\beta - mg\right)a\cos\theta'\,d\theta' \quad &\text{(work along $d\mathbf r = a\,\mathbf e_\theta\,d\theta'$)} \\
> &= -\left(ka\beta - mg\right)a\left[\sin\theta'\right]_0^{\theta} = \left(mg - ka\beta\right)a\sin\theta \quad &\text{(antiderivative $\sin\theta'$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{V(\theta) = \tfrac12 ka^2\left(1 + \beta^2\right) + \left(mg - ka\beta\right)a\sin\theta}$$
>
> **Units:** $[mga] = [ka^2] = [\mathrm{M\,L^2\,T^{-2}}]$, an energy
> **Meaning:** the direct sum and the work along the circumference agree; the reaction does no work, so it has no potential and does not enter.

#### (b) Equilibrium positions

> [!derivation] Equilibria and their stability
> **Law:** equilibria are the critical points of the potential; stable at a minimum
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> \frac{dV}{d\theta} &= \left(mg - ka\beta\right)a\cos\theta = 0 \quad &\text{(also the tangent equation at rest)} \\
> mg \ne ka\beta &\Rightarrow \cos\theta_e = 0 \Rightarrow \theta_e = \tfrac{\pi}{2} \ \text{or} \ \theta_e = -\tfrac{\pi}{2} \quad &\text{(top and bottom)} \\
> \frac{d^2V}{d\theta^2} &= -\left(mg - ka\beta\right)a\sin\theta \quad &\text{(second derivative)} \\
> \frac{d^2V}{d\theta^2}\Big|_{\pi/2} &= \left(ka\beta - mg\right)a, \quad \frac{d^2V}{d\theta^2}\Big|_{-\pi/2} = \left(mg - ka\beta\right)a \quad &\text{(the sign decides the stability)} \\
> mg = ka\beta &\Rightarrow \frac{dV}{d\theta} \equiv 0 \quad &\text{(constant potential)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{ll} ka\beta \gt mg: & \text{top } \theta_e = \tfrac{\pi}{2} \text{ stable, bottom unstable} \cr ka\beta \lt mg: & \text{bottom } \theta_e = -\tfrac{\pi}{2} \text{ stable, top unstable} \cr ka\beta = mg: & \text{every position is an equilibrium (neutral)} \end{array}}$$
>
> **Units:** $[ka\beta] = [mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the spring pulls the particle up with an effective vertical force $ka\beta$ that competes with the weight; when the two balance, nothing drives the particle along the circumference.

#### (c) Reduction to quadratures

> [!derivation] Energy integral and quadrature
> **Law:** the tangent equation multiplied by the angular rate is an exact derivative (chain rule); separation of variables; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.44
>
> $$\begin{aligned}
> ma^2\dot\theta\ddot\theta - \left(ka\beta - mg\right)a\cos\theta\,\dot\theta &= 0 \quad &\text{(zero $\epsilon$; tangent equation times $a\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12 ma^2\dot\theta^2\right) &= ma^2\dot\theta\ddot\theta, \quad \frac{d}{dt}V(\theta) = \frac{dV}{d\theta}\,\dot\theta = \left(mg - ka\beta\right)a\cos\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \left[\tfrac12 ma^2\dot\theta^2 + V(\theta)\right]_0^t &= 0 \quad &\text{(Barrow's rule)} \\
> \tfrac12 ma^2\dot\theta^2 + \left(mg - ka\beta\right)a\sin\theta &= \tfrac12 m v_0^2 \quad &\text{($\theta(0) = 0$, $a\dot\theta(0) = v_0$; constant part of $V$ cancels)} \\
> \dot\theta^2 &= \frac{v_0^2}{a^2} - \frac{2\left(mg - ka\beta\right)}{ma}\sin\theta \quad &\text{(solved for the squared rate)} \\
> \int_0^{\theta}\frac{d\theta'}{\sqrt{\dfrac{v_0^2}{a^2} - \dfrac{2\left(mg - ka\beta\right)}{ma}\sin\theta'}} &= \int_0^t dt' = t \quad &\text{(separation, $\dot\theta \gt 0$ at the start; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{t = \int_0^{\theta}\frac{d\theta'}{\sqrt{v_0^2/a^2 - 2\left(mg - ka\beta\right)\sin\theta'/(ma)}} \quad \text{(while $\dot\theta \gt 0$; the sign of the root changes at a turning point)}}$$
>
> **Units:** $[v_0^2/a^2] = [\mathrm{T^{-2}}]$; $[(mg - ka\beta)/(ma)] = [\mathrm{M\,L\,T^{-2}}]/[\mathrm{M\,L}] = [\mathrm{T^{-2}}]$; the integral is $[\mathrm{T}]$
> **Meaning:** the mechanical energy is conserved (smooth fixed constraint, conservative forces); the radicand decides whether the particle turns back or goes round the circumference.

#### (d) Motion when the spring balances the weight

> [!derivation] Uniform circular motion
> **Law:** the tangent equation with the balanced coefficient; two integrations with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> ka\beta - mg &= ka\,\frac{mg}{ka} - mg = 0 \quad &\text{($\beta = mg/(ka)$)} \\
> ma\ddot\theta &= 0 \Rightarrow \dot\theta(t) - \dot\theta(0) = \int_0^t 0\,dt' = 0 \Rightarrow \dot\theta = \frac{v_0}{a} \quad &\text{(Barrow's rule)} \\
> \theta(t) - \theta(0) &= \int_0^t \frac{v_0}{a}\,dt' = \left[\frac{v_0}{a}\,t'\right]_0^t = \frac{v_0}{a}\,t \quad &\text{(Barrow's rule, $\theta(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P(t) = a\cos\frac{v_0 t}{a}\,\mathbf i + a\sin\frac{v_0 t}{a}\,\mathbf j}$$
>
> **Units:** $[v_0 t/a] = [1]$; position $[\mathrm{L}]$
> **Meaning:** the spring cancels the tangential part of the weight everywhere, so the particle runs round the circumference with the constant speed $v_0$.

#### (e) Motion with the force along the velocity

> [!derivation] Exponentially growing angular rate
> **Law:** the tangent equation with the extra force; separation of variables; substitution and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 12
>
> Call $\Omega$ the angular rate, the time derivative of $\theta$.
>
> $$\begin{aligned}
> ma\dot\Omega &= 0 + 2m\mu a\,\Omega \Rightarrow \frac{d\Omega}{\Omega} = 2\mu\,dt \quad &\text{(unit $\epsilon$, balanced coefficient; separation)} \\
> \int_{v_0/a}^{\Omega}\frac{d\Omega'}{\Omega'} &= \left[\ln\Omega'\right]_{v_0/a}^{\Omega} = \ln\frac{a\Omega}{v_0} = \int_0^t 2\mu\,dt' = 2\mu t \quad &\text{(antiderivative $\ln$; Barrow's rule on both sides)} \\
> \Omega(t) &= \frac{v_0}{a}\,e^{2\mu t} \quad &\text{(exponential of both sides)} \\
> w &= 2\mu t', \quad dw = 2\mu\,dt', \quad t' = 0 \to w = 0, \quad t' = t \to w = 2\mu t \quad &\text{(substitution and its limits)} \\
> \theta(t) &= \int_0^t \frac{v_0}{a}\,e^{2\mu t'}\,dt' = \frac{v_0}{2\mu a}\int_0^{2\mu t} e^{w}\,dw = \frac{v_0}{2\mu a}\left[e^{w}\right]_0^{2\mu t} \quad &\text{(Barrow's rule, $\theta(0) = 0$)} \\
> &= \frac{v_0}{2\mu a}\left(e^{2\mu t} - 1\right) \quad &\text{(limits substituted)}
> \end{aligned}$$
>
> $$\boxed{\theta(t) = \frac{v_0}{2\mu a}\left(e^{2\mu t} - 1\right), \qquad \mathbf r_0^P(t) = a\cos\theta(t)\,\mathbf i + a\sin\theta(t)\,\mathbf j}$$
>
> **Units:** $[\mu t] = [1]$; $[v_0/(\mu a)] = [\mathrm{L\,T^{-1}}]/([\mathrm{T^{-1}}][\mathrm{L}]) = [1]$, radians
> **Meaning:** a force along the velocity feeds energy into the particle at the rate $2m\mu v^2$, so the angular rate grows exponentially.

#### (f) Reaction of the circumference

> [!derivation] Reaction with the force along the velocity
> **Law:** the normal projections of Newton's law with the motion of part (e)
> **Source:** Notes.pdf, Eq. 6.16; Notes.pdf, Sec. 6.5
>
> $$\begin{aligned}
> N_R &= ka + \left(mg - ka\beta\right)\sin\theta - ma\dot\theta^2 \quad &\text{(radial equation; the extra force is tangent)} \\
> &= ka - ma\,\frac{v_0^2}{a^2}\,e^{4\mu t} \quad &\text{(balanced coefficient; $\dot\theta = (v_0/a)\,e^{2\mu t}$)} \\
> N_k &= 0 \quad &\text{(out-of-plane equation)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N(t) = \left(ka - \frac{m v_0^2}{a}\,e^{4\mu t}\right)\mathbf e_R\big(\theta(t)\big)}$$
>
> **Units:** $[ka] = [m v_0^2/a] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the outward component starts at $ka - m v_0^2/a$ (the radial pull of the spring and weight against the centripetal need) and decreases without bound: the circumference must push the particle inwards harder and harder as it speeds up.

> [!note] Reading of the extra force
> The statement says that the extra force is proportional to the velocity and **in the same direction**, with constant $2m\mu$, and the solution follows it literally. If a viscous damping force opposite to the velocity was meant (the usual model of Notes.pdf, Eq. 5.19), the same steps with the sign of $\mu$ reversed give an angle that grows as $1 - e^{-2\mu t}$ towards the finite limit $v_0/(2\mu a)$, and a radial reaction that tends to $ka$ as the particle comes to rest.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Potential | $V(\theta) = \frac12 ka^2(1 + \beta^2) + (mg - ka\beta)\,a\sin\theta$ |
| (b) Equilibria | $\theta_e = \pm\pi/2$ if $ka\beta \ne mg$ (top stable if $ka\beta \gt mg$, bottom stable if $ka\beta \lt mg$); every $\theta$ if $ka\beta = mg$ |
| (c) Quadrature | $\dot\theta^2 = v_0^2/a^2 - 2(mg - ka\beta)\sin\theta/(ma)$; $t = \int_0^\theta d\theta'/\sqrt{v_0^2/a^2 - 2(mg - ka\beta)\sin\theta'/(ma)}$ |
| (d) Position for $\beta = mg/(ka)$ | $\theta = v_0 t/a$; $\mathbf r_0^P = a\cos(v_0t/a)\,\mathbf i + a\sin(v_0t/a)\,\mathbf j$ |
| (e) Position with the force $2m\mu\,\mathbf v$ | $\theta = \frac{v_0}{2\mu a}(e^{2\mu t} - 1)$; $\mathbf r_0^P = a\cos\theta\,\mathbf i + a\sin\theta\,\mathbf j$ |
| (f) Reaction | $\mathbf N = (ka - \frac{m v_0^2}{a}e^{4\mu t})\,\mathbf e_R$, no component out of the plane |

**Check against the official key:** Problems.pdf, p. 73 lists item 24 with no answer, so there is no key to compare with. Independent checks: the potential obtained as a direct sum and as minus the work along the circumference agree (box of part (a)); and the limiting cases below recover part (d).

> [!derivation] Limiting case: vanishing extra force
> **Law:** first-order expansion of the exponential
> **Source:** Notes.pdf, Eq. 4.4
>
> $$\begin{aligned}
> e^{2\mu t} - 1 &= 2\mu t + \tfrac12\left(2\mu t\right)^2 + \dots \quad &\text{(Taylor series of the exponential)} \\
> \theta(t) &= \frac{v_0}{2\mu a}\left(2\mu t + 2\mu^2 t^2 + \dots\right) \to \frac{v_0 t}{a} \quad &\text{($\mu \to 0$)} \\
> N_R &\to ka - \frac{m v_0^2}{a} \quad &\text{($e^{4\mu t} \to 1$)}
> \end{aligned}$$
>
> $$\boxed{\mu \to 0:\ \theta \to \frac{v_0 t}{a}, \quad N_R \to ka - \frac{m v_0^2}{a}}$$
>
> **Units:** $[\mathrm{rad}]$ and $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** without the extra force the uniform motion of part (d) is recovered, with a constant reaction.

---

## Problem 29: Heavy Particle on a Tilted Cylinder

### Reference Frames, Bases and Coordinates

A heavy particle of mass $m$ slides without friction on an infinitely long circular cylinder of radius $R$ whose axis $Oz$ is tilted by the angle $\alpha$ from the vertical $Oz_1$. Its position is given by the axial coordinate $z$ and the angle $\theta$ of the cross-section (Problems.pdf, p. 17). The statement asks for $z(t)$, the quadrature of $\theta(t)$, the reaction as a function of $\theta$, and a qualitative description for two initial angular rates. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_1\}$ with $\mathcal B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$ of the left panel: $\mathbf k_1$ vertical **upward**, $\mathbf i_1$ horizontal to the right, $\mathbf j_1$ horizontal, right-handed |
| Basis of the cylinder | $\mathcal B_2 = \{\mathbf i, \mathbf j, \mathbf k\}$ of the axes $x, y, z$ of the figure: $\mathbf k$ along the axis of the cylinder, $\mathbf j$ coincident with $\mathbf j_1$ ($y_1 \equiv y$), $\mathbf i$ completing the right-handed triad; fixed in $S_0$ |
| Cylindrical basis | $\mathcal B_3 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_2$ turned by $\theta$ about $\mathbf k$ (right panel) |
| Coordinates | $z$ along the axis and $\theta$ from the axis $Ox$ in the cross-section (statement) |
| Constraint | $f = x^2 + y^2 - R^2 = 0$ in the axes of the cylinder; holonomic, stationary, smooth; the particle is "constrained to move along the surface", read as bilateral (the sign of the reaction is discussed in part (c)) |
| Degrees of freedom | 3 minus 1: 2, namely $z(t)$ and $\theta(t)$ |
| Data | $m$ [kg], $R$ [m], $\alpha$ [rad], $g$ [m s$^{-2}$], $v_0$ [m s$^{-1}$], $\omega_0$ [rad s$^{-1}$] |
| Applied force | weight $-mg\,\mathbf k_1$ |
| Reaction | $\mathbf N = N\,\mathbf e_R$ (normal subspace of a surface, dimension 1; $N$ positive outwards) |
| Initial conditions | $z(0) = 0$, $\theta(0) = \pi/2$, $\dot z(0) = v_0$, $\dot\theta(0) = \omega_0$ (statement) |
| Hypotheses | $0 \lt \alpha \lt \pi/2$ as in the figure; $\omega_0 \gt 0$ in parts (d) and (e) |

![[attachments/EM-SOL/p29-rotation-j.svg]]

### Change of Basis and Position Vector

> [!derivation] Basis of the cylinder: rotation about j1
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19; Problems.pdf, p. 17
>
> View of the left panel, $\mathbf i_1$ to the right and $\mathbf k_1$ up. Since $\mathbf j_1$ is the cross product of $\mathbf k_1$ and $\mathbf i_1$, it points into the paper (⊗), and a positive rotation about $\mathbf j_1$ (thumb into the paper) is clockwise as seen. The axis $\mathbf k$ is $\mathbf k_1$ leaned clockwise towards $\mathbf i_1$ by $\alpha$: a positive rotation $\alpha$, Notes.pdf, Eq. 1.19 with the angle $\alpha$. The right triangle of $\mathbf k$ has hypotenuse 1, adjacent leg $\cos\alpha$ along $\mathbf k_1$ and opposite leg $\sin\alpha$ along $\mathbf i_1$. The axis $\mathbf i$ is $\mathbf i_1$ turned clockwise by the same angle: adjacent leg $\cos\alpha$ along $\mathbf i_1$, opposite leg $\sin\alpha$ along minus $\mathbf k_1$, because turning the right-pointing vector clockwise dips it below the horizontal (the minus sign; the figure draws $x$ pointing down to the right).
>
> $$\begin{aligned}
> \mathbf i &= \cos\alpha\,\mathbf i_1 - \sin\alpha\,\mathbf k_1, \quad \mathbf j = \mathbf j_1, \quad \mathbf k = \sin\alpha\,\mathbf i_1 + \cos\alpha\,\mathbf k_1 \quad &\text{(the two right triangles)} \\
> \mathbf i\times\mathbf j &= \cos\alpha\,\mathbf i_1\times\mathbf j_1 - \sin\alpha\,\mathbf k_1\times\mathbf j_1 = \cos\alpha\,\mathbf k_1 + \sin\alpha\,\mathbf i_1 = \mathbf k \quad &\text{(right-handed: $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)} \\
> \det[{}_1R_2] &= \cos\alpha\left(\cos\alpha - 0\right) - 0 + \sin\alpha\left(0 + \sin\alpha\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{11} &= \cos^2\alpha + \sin^2\alpha = 1, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{13} = -\cos\alpha\sin\alpha + \sin\alpha\cos\alpha = 0 \quad &\text{(rows 1 and 3; row 2 is the unit row of $\mathbf j$)} \\
> \mathbf k_1 &= -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf k \quad &\text{(third row of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \cos\alpha & 0 & \sin\alpha \cr 0 & 1 & 0 \cr -\sin\alpha & 0 & \cos\alpha \end{pmatrix}, \qquad \mathbf k_1 = -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf k}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** the axis $Ox$ of the cross-section points partly downwards, so gravity has a component along $\mathbf i$: the generator at $\theta$ equal to 0 is the lowest one.

![[attachments/EM-SOL/p29-cross-section.svg]]

> [!derivation] Cylindrical basis of the cross-section: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View of the right panel, along the axis: $\mathbf i$ to the right, $\mathbf j$ up, $\mathbf k$ out of the paper (⊙), as the figure marks; positive angles are counterclockwise. $\mathbf e_R$ is $\mathbf i$ turned by $\theta$ (adjacent leg $\cos\theta$ on $\mathbf i$, opposite leg $\sin\theta$ on $\mathbf j$); $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$ (adjacent leg $\cos\theta$ on $\mathbf j$, opposite leg $\sin\theta$ on minus $\mathbf i$: the upward vector leans to the left, the minus sign).
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(the two right triangles)} \\
> \mathbf e_R\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k, \quad \det[{}_2R_3] = \cos^2\theta + \sin^2\theta = 1 \quad &\text{(right-handed; expansion along the third row)} \\
> \left([{}_2R_3][{}_2R_3]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(rows 1 and 2; diagonal entries equal 1)} \\
> \mathbf i &= \cos\theta\,\mathbf e_R - \sin\theta\,\mathbf e_\theta \quad &\text{(first row of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_2R_3] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \qquad \mathbf i = \cos\theta\,\mathbf e_R - \sin\theta\,\mathbf e_\theta}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** $\mathbf e_R$ is the outward normal of the cylinder at the particle, $\mathbf e_\theta$ and $\mathbf k$ span its tangent plane.

> [!derivation] Position vector and the weight in the cylindrical basis
> **Law:** position vector in cylindrical coordinates; change of basis of the weight
> **Source:** Notes.pdf, Eq. 2.28; Notes.pdf, Eq. 1.16
>
> $$\begin{aligned}
> \mathbf r_0^P &= R\,\mathbf e_R + z\,\mathbf k \quad &\text{(constraint substituted: radius $R$)} \\
> -mg\,\mathbf k_1 &= mg\sin\alpha\,\mathbf i - mg\cos\alpha\,\mathbf k \quad &\text{($\mathbf k_1$ in $\mathcal B_2$)} \\
> &= mg\sin\alpha\cos\theta\,\mathbf e_R - mg\sin\alpha\sin\theta\,\mathbf e_\theta - mg\cos\alpha\,\mathbf k \quad &\text{($\mathbf i$ in $\mathcal B_3$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_R + z\,\mathbf k, \qquad -mg\,\mathbf k_1 = mg\sin\alpha\cos\theta\,\mathbf e_R - mg\sin\alpha\sin\theta\,\mathbf e_\theta - mg\cos\alpha\,\mathbf k}$$
>
> **Units:** $[\mathrm{L}]$; $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the weight splits into a part along the axis, $mg\cos\alpha$, and a part in the cross-section, $mg\sin\alpha$, that points along $\mathbf i$, towards the lowest generator.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** derivatives of the cylindrical unit vectors; time derivatives in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.29; Notes.pdf, Eq. 2.30
>
> $$\begin{aligned}
> \dot{\mathbf e}_R &= \dot\theta\,\mathbf k\times\mathbf e_R = \dot\theta\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_R, \quad \dot{\mathbf k} = \mathbf 0 \quad &\text{($\mathcal B_3$ turns about the fixed axis $\mathbf k$)} \\
> \mathbf v_0^P &= R\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k \quad &\text{(product rule; $R$ constant)} \\
> \mathbf a_0^P &= R\ddot\theta\,\mathbf e_\theta + R\dot\theta\,\dot{\mathbf e}_\theta + \ddot z\,\mathbf k = -R\dot\theta^2\,\mathbf e_R + R\ddot\theta\,\mathbf e_\theta + \ddot z\,\mathbf k \quad &\text{(product rule again)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = R\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k, \qquad \mathbf a_0^P = -R\dot\theta^2\,\mathbf e_R + R\ddot\theta\,\mathbf e_\theta + \ddot z\,\mathbf k}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity lies in the tangent plane of the cylinder; the centripetal part of the acceleration points to the axis.

### Forces and Equations of Motion

The free-body diagram, drawn in the cross-section, shows the in-plane part of the weight, the reaction along $\mathbf e_R$ and, as a ⊗ symbol, the axial part of the weight. The frame $S_0$ is inertial.

![[attachments/EM-SOL/p29-fbd.svg]]

> [!derivation] Newton's second law with the reaction, projected on the cylindrical basis
> **Law:** Newton's second law in an inertial frame with the constraint force; tangent projections free of the reaction
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.11; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf k_1 + N\,\mathbf e_R \quad &\text{(weight and reaction; unknowns $z$, $\theta$, $N$)} \\
> \mathbf k:\ m\ddot z &= -mg\cos\alpha \quad &\text{(tangent along the axis)} \\
> \mathbf e_\theta:\ mR\ddot\theta &= -mg\sin\alpha\sin\theta \quad &\text{(tangent along the cross-section)} \\
> \mathbf e_R:\ -mR\dot\theta^2 &= mg\sin\alpha\cos\theta + N \quad &\text{(normal)}
> \end{aligned}$$
>
> $$\boxed{\ddot z = -g\cos\alpha, \qquad \ddot\theta + \frac{g\sin\alpha}{R}\sin\theta = 0, \qquad N = -mR\dot\theta^2 - mg\sin\alpha\cos\theta}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$; $[g\sin\alpha/R] = [\mathrm{T^{-2}}]$; $[N] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the two degrees of freedom decouple: a uniformly decelerated motion along the axis and a pendulum of length $R$ in the reduced gravity $g\sin\alpha$ in the cross-section; the reaction follows afterwards.

### Answers and Checks

#### (a) Axial coordinate

> [!derivation] z as a function of time
> **Law:** two integrations of a constant acceleration with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5; Notes.pdf, Eq. 4.6
>
> $$\begin{aligned}
> \dot z(t) - \dot z(0) &= \int_0^t \left(-g\cos\alpha\right)dt' = \left[-g\cos\alpha\,t'\right]_0^t = -g\cos\alpha\,t \quad &\text{(Barrow's rule)} \\
> \dot z(t) &= v_0 - g\cos\alpha\,t \quad &\text{($\dot z(0) = v_0$)} \\
> z(t) - z(0) &= \int_0^t\left(v_0 - g\cos\alpha\,t'\right)dt' = \left[v_0 t' - \tfrac12 g\cos\alpha\,t'^2\right]_0^t \quad &\text{(antiderivative; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{z(t) = v_0 t - \tfrac12 g\cos\alpha\,t^2}$$
>
> **Units:** $[v_0 t] = [g t^2] = [\mathrm{L}]$
> **Meaning:** the particle climbs along the axis until the time $v_0/(g\cos\alpha)$ and then slides back down, whatever happens in the cross-section.

#### (b) Quadrature of the angle

> [!derivation] First integral of the angular equation and its quadrature
> **Law:** the angular equation multiplied by the angular rate is an exact derivative (chain rule); separation of variables; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.39; Notes.pdf, Eq. 4.44
>
> $$\begin{aligned}
> \dot\theta\ddot\theta + \frac{g\sin\alpha}{R}\sin\theta\,\dot\theta &= 0 \quad &\text{(equation times $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\dot\theta^2\right) &= \dot\theta\ddot\theta, \quad \frac{d}{dt}\left(-\frac{g\sin\alpha}{R}\cos\theta\right) = \frac{g\sin\alpha}{R}\sin\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \left[\tfrac12\dot\theta^2 - \frac{g\sin\alpha}{R}\cos\theta\right]_0^t &= 0 \quad &\text{(Barrow's rule)} \\
> \dot\theta^2 &= \omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta \quad &\text{($\theta(0) = \pi/2$, $\cos\tfrac{\pi}{2} = 0$, $\dot\theta(0) = \omega_0$)} \\
> \int_{\pi/2}^{\theta}\frac{d\theta'}{\sqrt{\omega_0^2 + \dfrac{2g\sin\alpha}{R}\cos\theta'}} &= \int_0^t dt' = t \quad &\text{(separation, $\dot\theta \gt 0$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\int_{\pi/2}^{\theta}\frac{d\theta'}{\sqrt{\omega_0^2 + 2g\sin\alpha\cos\theta'/R}} = t \quad \text{(while } \dot\theta \gt 0\text{; the sign changes at a turning point)}}$$
>
> **Units:** $[\omega_0^2] = [g/R] = [\mathrm{T^{-2}}]$; the integral is $[\mathrm{T}]$
> **Meaning:** the energy of the motion in the cross-section is conserved separately from the axial one, because the two equations are decoupled.

#### (c) Reaction of the cylinder

> [!derivation] Reaction as a function of the angle
> **Law:** normal projection with the first integral
> **Source:** Notes.pdf, Eq. 6.11; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> N &= -mR\left(\omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta\right) - mg\sin\alpha\cos\theta \quad &\text{(first integral substituted)} \\
> &= -m\left(R\omega_0^2 + 3g\sin\alpha\cos\theta\right) \quad &\text{(terms collected)}
> \end{aligned}$$
>
> $$\boxed{\mathbf N(\theta) = -m\left(R\omega_0^2 + 3g\sin\alpha\cos\theta\right)\mathbf e_R}$$
>
> **Units:** $[R\omega_0^2] = [g] = [\mathrm{L\,T^{-2}}]$; $[N] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** where the bracket is positive the cylinder pushes the particle towards the axis (as for a particle sliding on the inside); where it is negative it pulls it outwards, which a bilateral constraint can do and a one-sided contact cannot.

#### (d) Case of the smaller angular rate

> [!derivation] Oscillation about the lowest generator
> **Law:** turning points where the squared angular rate vanishes; reaction at those points
> **Source:** Notes.pdf, Eq. 4.43; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> \dot\theta^2 &= \frac{g\sin\alpha}{R}\left(1 + 2\cos\theta\right) \quad &\text{($\omega_0^2 = g\sin\alpha/R$)} \\
> \dot\theta^2 &= 0 \iff \cos\theta = -\tfrac12 \iff \theta = \pm\tfrac{2\pi}{3} \quad &\text{(turning points)} \\
> N &= -mg\sin\alpha\left(1 + 3\cos\theta\right) \quad &\text{(reaction of part (c))} \\
> N\left(\pm\tfrac{2\pi}{3}\right) &= -mg\sin\alpha\left(1 - \tfrac32\right) = \tfrac12\,mg\sin\alpha \gt 0 \quad &\text{(outward, opposite to its sign at the lowest generator)}
> \end{aligned}$$
>
> $$\boxed{-\tfrac{2\pi}{3} \le \theta \le \tfrac{2\pi}{3}: \ \text{periodic oscillation about } \theta = 0, \quad z(t) = v_0 t - \tfrac12 g\cos\alpha\,t^2}$$
>
> **Units:** $[g\sin\alpha/R] = [\mathrm{T^{-2}}]$; $[N] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the particle starts on the side of the cylinder moving up, rises to the angle $2\pi/3$, swings back through the lowest generator to minus $2\pi/3$ and repeats, while it climbs and then slides back along the axis: on the unrolled cylinder the path is a wave drawn along a parabola. Beyond the angle where the cosine is minus one third the reaction changes sign, so this motion needs the bilateral constraint.

#### (e) Case of the larger angular rate

> [!derivation] Complete turns round the axis
> **Law:** the squared angular rate never vanishes; reaction sign
> **Source:** Notes.pdf, Eq. 4.43; Notes.pdf, Sec. 6.4
>
> $$\begin{aligned}
> \dot\theta^2 &= \frac{2g\sin\alpha}{R}\left(2 + \cos\theta\right) \ge \frac{2g\sin\alpha}{R} \gt 0 \quad &\text{($\omega_0^2 = 4g\sin\alpha/R$; $\cos\theta \ge -1$)} \\
> \dot\theta_{\min}^2 &= \frac{2g\sin\alpha}{R} \ (\theta = \pi), \quad \dot\theta_{\max}^2 = \frac{6g\sin\alpha}{R} \ (\theta = 0) \quad &\text{(top and bottom generators)} \\
> N &= -mg\sin\alpha\left(4 + 3\cos\theta\right) \le -mg\sin\alpha \lt 0 \quad &\text{(always towards the axis)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta \ \text{never vanishes: complete, non-uniform turns, fastest at the lowest generator}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$; $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the particle winds round the cylinder on a helix-like path whose pitch follows the axial velocity, which falls to zero at the time $v_0/(g\cos\alpha)$ and then reverses; the cylinder always pushes it towards the axis, so a one-sided contact, with the particle on the inner face of the cylinder, would also hold.

| Part of the statement | Answer |
| :--- | :--- |
| (a) $z(t)$ | $z = v_0 t - \frac12 g\cos\alpha\,t^2$ |
| (b) Quadrature of $\theta$ | $\dot\theta^2 = \omega_0^2 + \frac{2g\sin\alpha}{R}\cos\theta$; $\int_{\pi/2}^{\theta} d\theta'/\sqrt{\omega_0^2 + 2g\sin\alpha\cos\theta'/R} = t$ |
| (c) Reaction | $\mathbf N = -m(R\omega_0^2 + 3g\sin\alpha\cos\theta)\,\mathbf e_R$ |
| (d) $\omega_0^2 = g\sin\alpha/R$ | oscillation between $\theta = \pm 2\pi/3$ about the lowest generator; the reaction changes sign (bilateral constraint needed) |
| (e) $\omega_0^2 = 4g\sin\alpha/R$ | complete non-uniform turns, $\dot\theta^2$ between $2g\sin\alpha/R$ and $6g\sin\alpha/R$; reaction always towards the axis |

**Check against the official key:** Problems.pdf, p. 74 lists item 29 with no answer, so there is no key to compare with. Independent checks: the limiting cases below.

> [!derivation] Limiting cases: vertical and horizontal axis
> **Law:** behaviour of the equations at the extreme tilts
> **Source:** Notes.pdf, Eq. 4.38
>
> $$\begin{aligned}
> \alpha \to 0:\ \ddot\theta &\to 0,\ \ddot z \to -g,\ N \to -mR\omega_0^2 \quad &\text{(vertical axis)} \\
> \alpha \to \tfrac{\pi}{2}:\ \ddot z &\to 0,\ \ddot\theta + \frac{g}{R}\sin\theta \to 0 \quad &\text{(horizontal axis)}
> \end{aligned}$$
>
> $$\boxed{\alpha \to 0:\ \text{uniform rotation and free fall along the axis}; \quad \alpha \to \tfrac{\pi}{2}:\ \text{simple pendulum of length } R \text{ and uniform axial motion}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$, $[\mathrm{L\,T^{-2}}]$, $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** with a vertical axis gravity has no part in the cross-section and the reaction is just the centripetal force; with a horizontal axis the cross-section is vertical and the problem is the simple pendulum of Notes.pdf, Sec. 4.7.

---

## Problem 31: Two Particles on Cone with String

### Reference Frames, Bases and Coordinates

Two heavy particles of mass $m$ are joined by an inextensible massless string of length $\ell$ that slides without friction through an aperture at the vertex $O$ of a cone of semi-angle $\alpha$. $P_1$ moves without friction on the cone and cannot leave it; $P_2$ hangs inside the cone along its axis and is guided along it (Problems.pdf, p. 19). The coordinates are the length $\xi$ of string between $O$ and $P_1$ and the azimuth $\theta$ of $P_1$. The statement asks for the kinematics, the forces, the equations, the condition for a tense string, the circular motion on a parallel and two first integrals. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure, origin at the vertex (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, $\mathbf k$ vertical **upward** (axis $OZ$); the cone opens downwards from $O$ |
| Cylindrical basis | $\mathcal B_1 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$; $\mathbf e_R$ horizontal, towards the meridian of $P_1$ |
| Cone basis | $\mathcal B_2 = \{\mathbf e_\xi, \mathbf e_\theta, \mathbf n\}$: $\mathbf e_\xi$ along the generator from $O$ to $P_1$, $\mathbf n$ the outward normal of the cone; $\mathcal B_1$ turned about $\mathbf e_\theta$ |
| Coordinates | $\xi$ (string length $OP_1$) and $\theta$ (azimuth of the projection of $\overrightarrow{OP_1}$ from $OX$) (statement) |
| Constraints | $P_1$ on the cone (1 equation, holonomic, stationary, smooth, bilateral: it cannot leave the surface); $P_2$ on the axis, $x_2 = y_2 = 0$ (2 equations, holonomic, stationary, smooth, bilateral); string, $\xi + |\overrightarrow{OP_2}| = \ell$ (1 equation joining the two particles, holonomic, stationary, unilateral: a string can only pull) ([Lecture 3, Slide 17]; [Lecture 3, Slide 21]) |
| Degrees of freedom | 6 coordinates of two particles minus 4 constraint equations: 2, namely $\xi(t)$ and $\theta(t)$ |
| Data | $m$ [kg] each, $\ell$ [m], $\alpha$ [rad] with $0 \lt \alpha \lt \pi/2$, $g$ [m s$^{-2}$] |
| Applied forces | weights $-mg\,\mathbf k$ on each particle |
| Constraint forces | on $P_1$: tension $-T\,\mathbf e_\xi$ (towards $O$) and normal reaction $N\,\mathbf n$; on $P_2$: tension $T\,\mathbf k$ and the guide reaction $\mathbf R_2$, normal to the axis (two unknown horizontal components); the same $T$ on both ends (massless string, smooth aperture) |
| Initial conditions | not given: generic $\xi(0)$, $\dot\xi(0)$, $\theta(0)$, $\dot\theta(0)$ |
| Hypotheses | string always tense and particles never at $O$ (statement); $0 \lt \xi \lt \ell$ |

![[attachments/EM-SOL/p31-meridian.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p31-rotation-k.svg]]

> [!derivation] Cylindrical basis: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View from above along $\mathbf k$ (⊙): $\mathbf i$ to the right, $\mathbf j$ up, counterclockwise positive. $\mathbf e_R$ is $\mathbf i$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ on $\mathbf i$, opposite leg $\sin\theta$ on $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: adjacent leg $\cos\theta$ on $\mathbf j$, opposite leg $\sin\theta$ on minus $\mathbf i$ (the upward vector leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(the two right triangles)} \\
> \mathbf e_R\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k, \quad \det[{}_0R_1] = \cos^2\theta + \sin^2\theta = 1 \quad &\text{(right-handed; expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(rows 1 and 2; diagonal entries equal 1)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** $\mathbf e_R$ points horizontally from the axis towards the meridian plane of $P_1$.

> [!derivation] Cone basis: rotation about e_theta in the meridian plane
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16; Notes.pdf, Eq. 1.19; Notes.pdf, Sec. 6.3
>
> View of the meridian plane of $P_1$ with $\mathbf e_R$ to the right and $\mathbf k$ up: $\mathbf e_\theta$, the cross product of $\mathbf k$ and $\mathbf e_R$, points into the paper (⊗), so a positive rotation about it is clockwise as seen. The generator $OP_1$ makes the semi-angle $\alpha$ with the downward axis, so $\mathbf e_\xi$ is $\mathbf e_R$ turned clockwise by $\pi/2 - \alpha$: a positive rotation of that angle. Its right triangle is the one of $OP_1$: hypotenuse $\xi$, vertical leg $\xi\cos\alpha$ along minus $\mathbf k$ (adjacent to $\alpha$) and horizontal leg $\xi\sin\alpha$ along $\mathbf e_R$ (opposite to $\alpha$); that is the minus sign on $\mathbf k$. The normal $\mathbf n$ is $\mathbf k$ turned by the same angle: it leans towards $\mathbf e_R$, outwards, with components $\cos\alpha$ on $\mathbf e_R$ and $\sin\alpha$ on $\mathbf k$.
>
> $$\begin{aligned}
> \cos\left(\tfrac{\pi}{2} - \alpha\right) &= \sin\alpha, \quad \sin\left(\tfrac{\pi}{2} - \alpha\right) = \cos\alpha \quad &\text{(complementary angles)} \\
> \mathbf e_\xi &= \sin\alpha\,\mathbf e_R - \cos\alpha\,\mathbf k, \quad \mathbf n = \cos\alpha\,\mathbf e_R + \sin\alpha\,\mathbf k \quad &\text{(columns of the rotation about the second axis, angle $\pi/2 - \alpha$)} \\
> \mathbf e_\xi\times\mathbf e_\theta &= \sin\alpha\,\mathbf k - \cos\alpha\left(\mathbf k\times\mathbf e_\theta\right) = \sin\alpha\,\mathbf k + \cos\alpha\,\mathbf e_R = \mathbf n \quad &\text{(right-handed; $\mathbf k\times\mathbf e_\theta = -\mathbf e_R$)} \\
> \det[{}_1R_2] &= \sin\alpha\cdot\sin\alpha - 0 + \cos\alpha\left(0 + \cos\alpha\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{13} &= -\sin\alpha\cos\alpha + \cos\alpha\sin\alpha = 0, \quad \left([{}_1R_2][{}_1R_2]^T\right)_{11} = 1 \quad &\text{(rows 1 and 3)} \\
> \mathbf e_R &= \sin\alpha\,\mathbf e_\xi + \cos\alpha\,\mathbf n, \quad \mathbf k = -\cos\alpha\,\mathbf e_\xi + \sin\alpha\,\mathbf n \quad &\text{(rows 1 and 3 of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} \sin\alpha & 0 & \cos\alpha \cr 0 & 1 & 0 \cr -\cos\alpha & 0 & \sin\alpha \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad [{}_1R_2][{}_1R_2]^T = I}$$
>
> **Units:** dimensionless: $[1]$
> **Meaning:** $\mathbf e_\xi$ and $\mathbf e_\theta$ span the tangent plane of the cone at $P_1$; $\mathbf n$, normal to the cone, is the only direction of its reaction.

> [!derivation] Position vectors of both particles
> **Law:** position vectors with the constraints substituted
> **Source:** Notes.pdf, Eq. 2.2; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \mathbf r_0^{P_1} &= \xi\,\mathbf e_\xi = \xi\sin\alpha\,\mathbf e_R - \xi\cos\alpha\,\mathbf k \quad &\text{(along the generator; legs of the meridian triangle)} \\
> |\overrightarrow{OP_2}| &= \ell - \xi \quad &\text{(inextensible string)} \\
> \mathbf r_0^{P_2} &= -\left(\ell - \xi\right)\mathbf k \quad &\text{(on the axis, below $O$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^{P_1} = \xi\,\mathbf e_\xi, \qquad \mathbf r_0^{P_2} = \left(\xi - \ell\right)\mathbf k}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** when $P_1$ moves away from $O$ along the generator, $P_2$ rises by the same length.

### Kinematics

> [!derivation] Derivatives of the cone basis
> **Law:** derivative of a unit vector of a basis turning about the fixed axis k
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{20} &= \dot\theta\,\mathbf k \quad &\text{($\alpha$ is constant: the cone basis turns only with $\theta$)} \\
> \dot{\mathbf e}_\xi &= \dot\theta\,\mathbf k\times\left(\sin\alpha\,\mathbf e_R - \cos\alpha\,\mathbf k\right) = \dot\theta\sin\alpha\,\mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf e_R = \mathbf e_\theta$, $\mathbf k\times\mathbf k = \mathbf 0$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_R = -\dot\theta\left(\sin\alpha\,\mathbf e_\xi + \cos\alpha\,\mathbf n\right) \quad &\text{($\mathbf e_R$ in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_\xi = \dot\theta\sin\alpha\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = -\dot\theta\sin\alpha\,\mathbf e_\xi - \dot\theta\cos\alpha\,\mathbf n}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the generator sweeps round the cone; the azimuthal vector turns inwards, partly along the generator and partly into the cone.

> [!derivation] (a) Position, velocity and acceleration of both particles
> **Law:** time derivatives in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Problems.pdf, p. 19
>
> $$\begin{aligned}
> \mathbf v_0^{P_1} &= \dot\xi\,\mathbf e_\xi + \xi\,\dot{\mathbf e}_\xi = \dot\xi\,\mathbf e_\xi + \xi\dot\theta\sin\alpha\,\mathbf e_\theta \quad &\text{(product rule)} \\
> \mathbf a_0^{P_1} &= \ddot\xi\,\mathbf e_\xi + \dot\xi\dot\theta\sin\alpha\,\mathbf e_\theta + \left(\dot\xi\dot\theta + \xi\ddot\theta\right)\sin\alpha\,\mathbf e_\theta + \xi\dot\theta\sin\alpha\,\dot{\mathbf e}_\theta \quad &\text{(product rule on each term)} \\
> &= \left(\ddot\xi - \xi\dot\theta^2\sin^2\alpha\right)\mathbf e_\xi + \left(2\dot\xi\dot\theta + \xi\ddot\theta\right)\sin\alpha\,\mathbf e_\theta - \xi\dot\theta^2\sin\alpha\cos\alpha\,\mathbf n \quad &\text{(derivative of $\mathbf e_\theta$; grouped)} \\
> \mathbf v_0^{P_2} &= \dot\xi\,\mathbf k, \quad \mathbf a_0^{P_2} = \ddot\xi\,\mathbf k \quad &\text{($\ell$ constant; $\mathbf k$ fixed)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^{P_1} = \xi\,\mathbf e_\xi, \quad \mathbf v_0^{P_1} = \dot\xi\,\mathbf e_\xi + \xi\dot\theta\sin\alpha\,\mathbf e_\theta \cr \mathbf a_0^{P_1} = \left(\ddot\xi - \xi\dot\theta^2\sin^2\alpha\right)\mathbf e_\xi + \left(2\dot\xi\dot\theta + \xi\ddot\theta\right)\sin\alpha\,\mathbf e_\theta - \xi\dot\theta^2\sin\alpha\cos\alpha\,\mathbf n \cr \mathbf r_0^{P_2} = \left(\xi - \ell\right)\mathbf k, \quad \mathbf v_0^{P_2} = \dot\xi\,\mathbf k, \quad \mathbf a_0^{P_2} = \ddot\xi\,\mathbf k \end{array}}$$
>
> **Units:** $[\mathrm{L}]$, $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$ in every term: e.g. $[\xi\dot\theta^2] = [\dot\xi\dot\theta] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $\xi\sin\alpha$ is the radius of the parallel of $P_1$; the velocity of $P_1$ has no normal component, as the cone requires, while its acceleration has one: the part of the centripetal acceleration that the normal reaction must supply.

### Forces and Equations of Motion

The free-body diagrams of the two particles show the weights, the tension pulling each one towards the aperture, the normal reaction of the cone on $P_1$ and the reaction of the guide on $P_2$. The frame $S_0$ is inertial.

![[attachments/EM-SOL/p31-fbd.svg]]

> [!derivation] (b) Forces on both particles
> **Law:** weight; tension of a massless string through a smooth aperture; reactions in the normal subspaces
> **Source:** Notes.pdf, Sec. 6.4; Notes.pdf, Sec. 6.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> -mg\,\mathbf k &= mg\cos\alpha\,\mathbf e_\xi - mg\sin\alpha\,\mathbf n \quad &\text{($\mathbf k$ in $\mathcal B_2$)} \\
> \mathbf F^{P_1} &= mg\cos\alpha\,\mathbf e_\xi - mg\sin\alpha\,\mathbf n - T\,\mathbf e_\xi + N\,\mathbf n \quad &\text{(weight, tension towards $O$, normal reaction)} \\
> \mathbf F^{P_2} &= -mg\,\mathbf k + T\,\mathbf k + R_{2x}\,\mathbf i + R_{2y}\,\mathbf j \quad &\text{(weight, tension towards $O$, guide reaction normal to the axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^{P_1} = \left(mg\cos\alpha - T\right)\mathbf e_\xi + \left(N - mg\sin\alpha\right)\mathbf n, \qquad \mathbf F^{P_2} = \left(T - mg\right)\mathbf k + R_{2x}\,\mathbf i + R_{2y}\,\mathbf j}$$
>
> **Units:** every force $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** no force on $P_1$ has an azimuthal component: gravity, the string and the normal all lie in the meridian plane.

> [!derivation] (c) Newton's second law for each particle and the decoupled equations
> **Law:** Newton's second law in an inertial frame with all the constraint forces; elimination of the tension
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.11; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> m\,\mathbf a_0^{P_1} &= \mathbf F^{P_1}, \quad m\,\mathbf a_0^{P_2} = \mathbf F^{P_2} \quad &\text{(all forces of box (b), reactions included)} \\
> P_1,\ \mathbf e_\xi:\ m\left(\ddot\xi - \xi\dot\theta^2\sin^2\alpha\right) &= mg\cos\alpha - T \quad &\text{(along the generator)} \\
> P_1,\ \mathbf e_\theta:\ m\left(2\dot\xi\dot\theta + \xi\ddot\theta\right)\sin\alpha &= 0 \quad &\text{(azimuthal)} \\
> P_1,\ \mathbf n:\ -m\xi\dot\theta^2\sin\alpha\cos\alpha &= N - mg\sin\alpha \quad &\text{(normal to the cone)} \\
> P_2,\ \mathbf k:\ m\ddot\xi &= T - mg \quad &\text{(along the axis)} \\
> P_2,\ \mathbf i,\ \mathbf j:\ 0 &= R_{2x}, \quad 0 = R_{2y} \quad &\text{(normal to the axis)} \\
> m\left(\ddot\xi - \xi\dot\theta^2\sin^2\alpha\right) &= mg\cos\alpha - m\left(\ddot\xi + g\right) \quad &\text{(tension from the equation of $P_2$ substituted)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} 2\ddot\xi - \xi\dot\theta^2\sin^2\alpha + g\left(1 - \cos\alpha\right) = 0, \qquad 2\dot\xi\dot\theta + \xi\ddot\theta = 0 \cr T = m\left(g + \ddot\xi\right), \qquad N = m\sin\alpha\left(g - \xi\dot\theta^2\cos\alpha\right), \qquad \mathbf R_2 = \mathbf 0 \end{array}}$$
>
> **Units:** $[\ddot\xi] = [\xi\dot\theta^2] = [g] = [\mathrm{L\,T^{-2}}]$; $[T] = [N] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** six scalar equations for the six unknowns $\xi$, $\theta$, $T$, $N$ and the two guide components; the first two contain no reaction and give the motion, the others give the tension and the reactions afterwards. The effective inertia of the string motion is $2m$, since both particles move with the rate of $\xi$.

### Answers and Checks

#### (d) Tense string

> [!derivation] Condition for the string to stay tense
> **Law:** a string can only pull: the tension must stay positive (unilateral constraint)
> **Source:** Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]
>
> $$\begin{aligned}
> T &= m\left(g + \ddot\xi\right) \gt 0 \iff \ddot\xi \gt -g \quad &\text{(equation of $P_2$)} \\
> \ddot\xi &= \tfrac12\left[\xi\dot\theta^2\sin^2\alpha - g\left(1 - \cos\alpha\right)\right] \quad &\text{(decoupled equation of $\xi$)} \\
> T &= m\left[g + \tfrac12\xi\dot\theta^2\sin^2\alpha - \tfrac12 g + \tfrac12 g\cos\alpha\right] = \tfrac{m}{2}\left[g\left(1 + \cos\alpha\right) + \xi\dot\theta^2\sin^2\alpha\right] \quad &\text{(substitution)}
> \end{aligned}$$
>
> $$\boxed{\ddot\xi(t) \gt -g \ \text{for all } t; \qquad T = \tfrac{m}{2}\left[g\left(1 + \cos\alpha\right) + \xi\dot\theta^2\sin^2\alpha\right] \gt 0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$; $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the hanging particle must never accelerate downwards faster than free fall; along any motion of these equations the tension is a sum of positive terms, so the condition holds automatically while both particles are away from $O$.

> [!warning] Discrepancy with the official solution
> The key (Problems.pdf, p. 74, item 31) states the condition as the second derivative of $\xi$ greater than $g$, with no minus sign. This solution keeps the second derivative greater than minus $g$: the equation of $P_2$ gives the tension as $m$ times the sum of $g$ and that second derivative, and the key's own circular motion of part (e), with the tension $mg$ and a constant $\xi$, would violate the condition as printed.

#### (e) Circular motion on a parallel

> [!derivation] Angular rate, tension and reaction on a parallel
> **Law:** constant generator length in the decoupled equations; the reactions follow
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 19
>
> $$\begin{aligned}
> -\xi\dot\theta^2\sin^2\alpha + g\left(1 - \cos\alpha\right) &= 0 \quad &\text{($\dot\xi = \ddot\xi = 0$; the azimuthal equation gives $\ddot\theta = 0$)} \\
> \dot\theta^2 &= \frac{g\left(1 - \cos\alpha\right)}{\xi\sin^2\alpha} = \frac{g}{\xi\left(1 + \cos\alpha\right)} \quad &\text{($\sin^2\alpha = (1 - \cos\alpha)(1 + \cos\alpha)$)} \\
> T &= m\left(g + 0\right) = mg \quad &\text{(equation of $P_2$)} \\
> N &= m\sin\alpha\left(g - \frac{g\cos\alpha}{1 + \cos\alpha}\right) = \frac{mg\sin\alpha}{1 + \cos\alpha} = \frac{mg\left(1 - \cos\alpha\right)}{\sin\alpha} \quad &\text{(reaction formula; same identity)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = \sqrt{\frac{g}{\xi\left(1 + \cos\alpha\right)}}, \quad -T\,\mathbf e_\xi = mg\left(-\sin\alpha\,\mathbf e_R + \cos\alpha\,\mathbf k\right), \quad N\,\mathbf n = \frac{mg\left(1 - \cos\alpha\right)}{\sin\alpha}\left(\cos\alpha\,\mathbf e_R + \sin\alpha\,\mathbf k\right), \quad \mathbf R_2 = \mathbf 0}$$
>
> **Units:** $[\sqrt{g/\xi}] = [\mathrm{T^{-1}}]$; forces $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** $P_2$ hangs at rest, so the string carries exactly its weight; on $P_1$ the horizontal parts of tension and reaction give the centripetal force and their vertical parts carry the weight. The reaction is positive: the cone pushes outwards on $P_1$.

#### (f) Two first integrals

> [!derivation] Areal integral and energy integral derived from the equations of motion
> **Law:** exact derivatives (product and chain rules); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\xi^2\dot\theta\right) &= 2\xi\dot\xi\dot\theta + \xi^2\ddot\theta = \xi\left(2\dot\xi\dot\theta + \xi\ddot\theta\right) = 0 \quad &\text{(product and chain rules; azimuthal equation)} \\
> \left[\xi^2\dot\theta\right]_0^t &= 0 \Rightarrow \xi^2\dot\theta = C_1 \quad &\text{(Barrow's rule)} \\
> 2\dot\xi\ddot\xi - \frac{C_1^2\sin^2\alpha}{\xi^3}\,\dot\xi + g\left(1 - \cos\alpha\right)\dot\xi &= 0 \quad &\text{(equation of $\xi$ times $\dot\xi$; $\xi\dot\theta^2 = C_1^2/\xi^3$)} \\
> \frac{d}{dt}\left(\dot\xi^2\right) &= 2\dot\xi\ddot\xi, \quad \frac{d}{dt}\left(\frac{C_1^2\sin^2\alpha}{2\xi^2}\right) = -\frac{C_1^2\sin^2\alpha}{\xi^3}\,\dot\xi \quad &\text{(chain rule)} \\
> \left[\dot\xi^2 + \frac{C_1^2\sin^2\alpha}{2\xi^2} + g\left(1 - \cos\alpha\right)\xi\right]_0^t &= 0 \quad &\text{(sum of exact derivatives; Barrow's rule)} \\
> 2\dot\xi^2 + \xi^2\dot\theta^2\sin^2\alpha + 2g\xi\left(1 - \cos\alpha\right) &= C_2 \quad &\text{(times 2; $C_1^2/\xi^2 = \xi^2\dot\theta^2$)} \\
> E &= m\dot\xi^2 + \tfrac12 m\xi^2\dot\theta^2\sin^2\alpha - mg\xi\cos\alpha - mg\left(\ell - \xi\right) = \tfrac{m}{2}\,C_2 - mg\ell \quad &\text{(kinetic plus potential energy of both particles)}
> \end{aligned}$$
>
> $$\boxed{\xi^2\dot\theta = C_1, \qquad 2\dot\xi^2 + \xi^2\dot\theta^2\sin^2\alpha + 2g\xi\left(1 - \cos\alpha\right) = C_2}$$
>
> **Units:** $[C_1] = [\mathrm{L^2\,T^{-1}}]$; every term of the second integral $[\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the first is the angular momentum of $P_1$ about the axis divided by $m\sin^2\alpha$, constant because no force has a moment about the axis; the second is the mechanical energy of the pair: the stationary smooth constraints do no work and the string only transfers energy from one particle to the other, its works on the two ends cancelling.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Kinematics | $\mathbf r_0^{P_1} = \xi\,\mathbf e_\xi$; $\mathbf v_0^{P_1} = \dot\xi\,\mathbf e_\xi + \xi\dot\theta\sin\alpha\,\mathbf e_\theta$; $\mathbf a_0^{P_1} = (\ddot\xi - \xi\dot\theta^2\sin^2\alpha)\,\mathbf e_\xi + (2\dot\xi\dot\theta + \xi\ddot\theta)\sin\alpha\,\mathbf e_\theta - \xi\dot\theta^2\sin\alpha\cos\alpha\,\mathbf n$; $\mathbf r_0^{P_2} = (\xi - \ell)\,\mathbf k$, $\mathbf v_0^{P_2} = \dot\xi\,\mathbf k$, $\mathbf a_0^{P_2} = \ddot\xi\,\mathbf k$ |
| (b) Forces | $P_1$: $-mg\,\mathbf k$, $-T\,\mathbf e_\xi$, $N\,\mathbf n$; $P_2$: $-mg\,\mathbf k$, $T\,\mathbf k$, $\mathbf R_2 \perp \mathbf k$ |
| (c) Equations | $2\ddot\xi - \xi\dot\theta^2\sin^2\alpha + g(1 - \cos\alpha) = 0$; $2\dot\xi\dot\theta + \xi\ddot\theta = 0$; $T = m(g + \ddot\xi)$; $N = m\sin\alpha(g - \xi\dot\theta^2\cos\alpha)$; $\mathbf R_2 = \mathbf 0$ |
| (d) Tense string | $\ddot\xi \gt -g$ (always satisfied: $T = \frac m2[g(1 + \cos\alpha) + \xi\dot\theta^2\sin^2\alpha]$) |
| (e) Circular parallel | $\xi\dot\theta^2\sin^2\alpha = g(1 - \cos\alpha)$; $T = mg$; $N = mg(1 - \cos\alpha)/\sin\alpha$ along $\mathbf n = \cos\alpha\,\mathbf e_R + \sin\alpha\,\mathbf k$; $\mathbf R_2 = \mathbf 0$ |
| (f) First integrals | $\xi^2\dot\theta = C_1$; $2\dot\xi^2 + \xi^2\dot\theta^2\sin^2\alpha + 2g\xi(1 - \cos\alpha) = C_2$ |

**Check against the official key:** Problems.pdf, p. 74, item 31, gives two degrees of freedom, the same two first integrals, the same condition for the circular parallel and the same tension and normal force (**match**), with two remarks. The key writes the direction of the normal force with $\mathbf e_\theta$ where this solution has $\mathbf k$: a combination of a horizontal radial and a horizontal azimuthal vector would not be normal to the cone, so the key's symbol is read as the vertical unit vector, and the magnitudes agree. The condition for a tense string differs by a sign (warning box of part (d)).

> [!derivation] Limiting case: a flat table with a hole
> **Law:** the equations with a right semi-angle
> **Source:** Notes.pdf, Eq. 4.4
>
> With a semi-angle of a right angle the cone becomes the horizontal plane through $O$ and $P_1$ moves on a table, with $P_2$ hanging through the hole.
>
> $$\begin{aligned}
> \cos\alpha &\to 0, \quad \sin\alpha \to 1 \quad &\text{($\alpha \to \pi/2$)} \\
> 2\ddot\xi - \xi\dot\theta^2 + g &= 0, \quad \dot\theta^2 \to \frac{g}{\xi}, \quad N \to mg \quad &\text{(equation of $\xi$, circular rate, reaction)}
> \end{aligned}$$
>
> $$\boxed{\alpha \to \tfrac{\pi}{2}:\ m\xi\dot\theta^2 = mg \ \text{on a circle}, \quad N = mg}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the classical table-with-a-hole problem: on a circle the centripetal force of $P_1$ is the weight of $P_2$ carried by the string, and the table carries the weight of $P_1$.

---

## 📌 Problem 32: Particle with String on Spool

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ of mass $m$ hangs from a string of length $l = 4\pi a$ that unwinds from a spool of radius $a$ and centre $O$, which rotates counterclockwise at the constant rate $\omega$. The string is massless, inextensible, thin and stays taut. One end is fixed to the spool at the point $A$ of its perimeter; $B$ is the point where the straight segment $BP$ leaves the spool, and $\phi$ is the angle between $Ox$ and $OB$. Initially $\overrightarrow{OA} = -a\,\mathbf{i}$ and $B$ never reaches $A$.
* **Constraints:** $P$ is a particle in the plane (2 coordinates). The string of fixed length that winds on the spool ties its position to the geometry: the free length $BP$ is $s = l - (\text{wrapped arc})$, and the attachment $A$ turns with the spool, so the constraint depends explicitly on time (rheonomic, holonomic) when $\omega \ne 0$. It is unilateral ($T \ge 0$, taut string).
* **Degrees of freedom (part a):** $\text{CDOF} = 2 - 1 = 1$, the angle $\phi$.
* **Parameters:** $m$, $a$, $l = 4\pi a$, $\omega$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$ with $\mathbf{j}$ vertical upward.
* **Basis at $B$:** $\mathbf{u}_r = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j}$ (radial) and $\mathbf{u}_t = -\sin\phi\,\mathbf{i} + \cos\phi\,\mathbf{j}$ (counterclockwise tangent), a rotation of $\{\mathbf{i}, \mathbf{j}\}$ by $\phi$ (matrix $\begin{pmatrix}\cos \phi & -\sin \phi & 0\\ \sin \phi & \cos \phi & 0\\ 0 & 0 & 1\end{pmatrix}$, $\det = \cos^2\phi + \sin^2\phi = 1$; $RR^T$ has diagonal entries $\cos^2\phi + \sin^2\phi = 1$ (and $1$) and off-diagonal entries $\cos \phi\sin \phi - \sin \phi\cos \phi = 0$, so $RR^T = I$), with $\dot{\mathbf{u}}_r = \dot{\phi}\,\mathbf{u}_t$ and $\dot{\mathbf{u}}_t = -\dot{\phi}\,\mathbf{u}_r$. The straight segment leaves $B$ clockwise, toward the lower right in the figure, i.e. along $-\mathbf{u}_t$.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Degrees of freedom
* The particle moves in the plane (2 coordinates) but the string constraint leaves exactly **one** degree of freedom, $\phi$.

##### (b) Position, velocity and acceleration of $P$
* **Pedagogical Justification:** the point $B$ is at $a\,\mathbf{u}_r$ and $P$ is at the distance $s$ from $B$ along $-\mathbf{u}_t$. The length $s$ is the total length minus the wrapped arc. The attachment $A$ is at the angle $\pi + \omega t$ (it turns with the spool), and the string is wound from $B$ (angle $\phi$) to $A$, so the wrapped arc is $a(\pi + \omega t - \phi)$:
$$ s(t) = l - a\left(\pi + \omega t - \phi\right) = a\left(3\pi - \omega t + \phi\right), \qquad \dot{s} = a\left(\dot{\phi} - \omega\right) $$
$$ \mathbf{r}_P = a\,\mathbf{u}_r - s\,\mathbf{u}_t $$
* **Velocity** (product rule and Poisson's formula):
$$ \mathbf{v}_P = a\dot{\phi}\,\mathbf{u}_t - \dot{s}\,\mathbf{u}_t - s\left(-\dot{\phi}\,\mathbf{u}_r\right) = a\dot{\phi}\,\mathbf{u}_t - a\left(\dot{\phi} - \omega\right)\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r = a\omega\,\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r $$
* **Acceleration:**
$$ \mathbf{a}_P = a\omega\left(-\dot{\phi}\,\mathbf{u}_r\right) + \dot{s}\dot{\phi}\,\mathbf{u}_r + s\ddot{\phi}\,\mathbf{u}_r + s\dot{\phi}\left(\dot{\phi}\,\mathbf{u}_t\right) = \left[s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}\right]\mathbf{u}_r + s\dot{\phi}^2\,\mathbf{u}_t $$
(using $\dot{s}\dot{\phi} = a\left(\dot{\phi} - \omega\right)\dot{\phi}$).

#### 3.2 Forces
##### (c) Forces on $P$
* **Weight:** $-mg\,\mathbf{j} = -mg\left(\sin\phi\,\mathbf{u}_r + \cos\phi\,\mathbf{u}_t\right)$.
* **Tension:** along the straight segment, toward $B$: $\mathbf{T} = +T\,\mathbf{u}_t$ with $T \gt 0$ (since $\mathbf{r}_B - \mathbf{r}_P = s\,\mathbf{u}_t$).
* **Inertia forces:** none. There is no other force: the string is the only constraint.

#### 3.3 Equations of Motion
##### (e) Closed set of equations
* **Pedagogical Justification:** Newton's second law in $S_0$ gives two scalar equations for the two unknowns $\phi(t)$ and $T(t)$. The radial projection contains no tension:
$$ \mathbf{u}_r: \; m\left[s\ddot{\phi} + a\dot{\phi}^2 - 2a\omega\dot{\phi}\right] = -mg\sin\phi, \qquad \mathbf{u}_t: \; ms\dot{\phi}^2 = T - mg\cos\phi $$
$$ \boxed{a\left[\left(3\pi - \omega t + \phi\right)\ddot{\phi} - 2\omega\dot{\phi} + \dot{\phi}^2\right] = -g\sin\phi}, \qquad \boxed{T = ma\left(3\pi - \omega t + \phi\right)\dot{\phi}^2 + mg\cos\phi} $$
The first is the equation of motion for $\phi(t)$; the tension follows from the second once $\phi(t)$ is known.

##### (d) Energy
* **Pedagogical Justification:** the power of the tension on $P$ is $\mathbf{T}\cdot\mathbf{v}_P = T\,\mathbf{u}_t\cdot\left(a\omega\,\mathbf{u}_t + s\dot{\phi}\,\mathbf{u}_r\right) = Ta\omega$. For $\omega \ne 0$ it is not zero (the contact point $B$ moves with the spool), so the tension does work on $P$ and the mechanical energy of $P$ is **not conserved**. For $\omega = 0$ the power is zero, the constraint is scleronomic and the energy is conserved.

#### 3.4 Integration and Answers
##### (f) Case $\omega = 0$
* **Pedagogical Justification:** with $\omega = 0$ the tension does no work and gravity is conservative, so the mechanical energy is a first integral that involves only $\phi$ and $\dot{\phi}$ (it contains no $\ddot{\phi}$). From $\mathbf{r}_P = a\,\mathbf{u}_r - s\,\mathbf{u}_t$ with $s = a(3\pi + \phi)$, the height is $y = a\sin\phi - a(3\pi + \phi)\cos\phi$, and $v^2 = s^2\dot{\phi}^2$ (from 3.1 with $\omega = 0$):
$$ \boxed{E = \tfrac{1}{2}m\left[a(3\pi + \phi)\right]^2\dot{\phi}^2 + mga\left[\sin\phi - (3\pi + \phi)\cos\phi\right] = \text{const}} $$

### Phase 4: Interpretation & Checks
* **Involute pendulum:** the system behaves like a pendulum whose effective length $s = a(3\pi - \omega t + \phi)$ changes as the string unwinds.
* **Dimensional check:** $[a\ddot{\phi}\,s/a] = \text{m s}^{-2}$, like $[g\sin\phi]$; $[T] = \left[ma\left(3\pi + \phi\right)\dot{\phi}^2\right] = \text{N}$.
* **Check against the official key:** the key of `Problems.pdf` gives the two equations $a\left[\left(3\pi - \omega t + \phi\right)\ddot{\phi} - 2\omega\dot{\phi} + \dot{\phi}^2\right] = -g\sin\phi$ and $ma\left(3\pi - \omega t + \phi\right)\dot{\phi}^2 = -mg\cos\phi + T$, the conservation of the mechanical energy for $\omega = 0$ and its quadrature $\tfrac{1}{2}m\left[a(3\pi + \phi)\right]^2\dot{\phi}^2 + mga\left[\sin\phi - (3\pi + \phi)\cos\phi\right] = E$. All coincide with the results above. Sympy reproduces $\mathbf{v}_P$ and $\mathbf{a}_P$ by differentiating $\mathbf{r}_P$, and numerical integration of the equation with $\omega = 0$ conserves the energy to $6\times 10^{-12}$ with $T \gt 0$.

---

## 📌 Problem 35: String with Two Particles on a Cylinder

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** two heavy particles $P$ and $Q$ of mass $m$ are joined by an inextensible massless string of length $L$ that rests on a fixed smooth cylinder of radius $R$ and centre $O$, and by a spring of zero natural length and stiffness $k$. The motion is planar, in $Oxy$ with $Oy$ upward. $A$ (right) and $B$ (left) are the tangency points of the string with the cylinder. The string stays taut and the spring does not touch the cylinder.
* **Constraints:** two free particles in the plane have $4$ coordinates. The inextensible string, taut and in contact with the cylinder, gives one holonomic constraint (unilateral: $T \ge 0$), so $\text{CDOF} = 4 - 1 = 3$. The smooth cylinder acts on the string, not on the particles.
* **Coordinates:** $A$ is at the polar angle $\alpha$ from $Ox$ and $B$ at the polar angle $\beta$. The straight segments $AP$ and $BQ$ have lengths $\xi_P$ and $\xi_Q$, and the string wraps the arc $AB$ of length $R(\beta - \alpha)$ on the cylinder:
$$ \xi_P + \xi_Q + R(\beta - \alpha) = L $$
The generalised coordinates are $(\alpha, \beta, \xi_P)$, with $\xi_Q = L - \xi_P - R(\beta - \alpha)$ (the four quantities $\alpha, \beta, \xi_P, \xi_Q$ are used below together with this one relation).
* **Parameters:** $m$ [kg], $L$ [m], $R$ [m], $k$ [N/m], $g$ [m/s$^2$]; $\ell_0 = (L - \pi R)/2$ [m] is defined in (e).

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ fixed to the cylinder.
* **Bases following the contact points:** $\mathbf{n}$ is the outward normal of the cylinder and $\mathbf{t}$ the unit vector along the straight string, from the tangency point to the particle (clockwise at $A$, counterclockwise at $B$):
$$ \mathbf{n}_A = \cos\alpha\,\mathbf{i} + \sin\alpha\,\mathbf{j}, \quad \mathbf{t}_A = \sin\alpha\,\mathbf{i} - \cos\alpha\,\mathbf{j}, \qquad \mathbf{n}_B = \cos\beta\,\mathbf{i} + \sin\beta\,\mathbf{j}, \quad \mathbf{t}_B = -\sin\beta\,\mathbf{i} + \cos\beta\,\mathbf{j} $$
* **Changes of basis** (columns are the components of $\mathbf{t}_A, \mathbf{n}_A, \mathbf{k}$ and of $\mathbf{n}_B, \mathbf{t}_B, \mathbf{k}$):
$$ [{}_0 R_A] = \begin{pmatrix} \sin\alpha & \cos\alpha & 0 \\ -\cos\alpha & \sin\alpha & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad [{}_0 R_B] = \begin{pmatrix} \cos\beta & -\sin\beta & 0 \\ \sin\beta & \cos\beta & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
$$ \det[{}_0 R_A] = \sin^2\alpha + \cos^2\alpha = 1, \quad \det[{}_0 R_B] = \cos^2\beta + \sin^2\beta = 1, \quad [{}_0 R_A][{}_0 R_A]^T = [{}_0 R_B][{}_0 R_B]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* **Time derivatives** (each basis turns about $\mathbf{k}$ at the rate of its angle):
$$ \dot{\mathbf{t}}_A = \dot{\alpha}\,\mathbf{n}_A, \quad \dot{\mathbf{n}}_A = -\dot{\alpha}\,\mathbf{t}_A, \qquad \dot{\mathbf{n}}_B = \dot{\beta}\,\mathbf{t}_B, \quad \dot{\mathbf{t}}_B = -\dot{\beta}\,\mathbf{n}_B $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** each particle is at the tangency point plus the straight segment, $\mathbf{r}_P = R\,\mathbf{n}_A + \xi_P\,\mathbf{t}_A$ and $\mathbf{r}_Q = R\,\mathbf{n}_B + \xi_Q\,\mathbf{t}_B$. The derivatives use the product rule and the formulas of Phase 2:
$$ \mathbf{v}_P = -R\dot{\alpha}\,\mathbf{t}_A + \dot{\xi}_P\,\mathbf{t}_A + \xi_P\dot{\alpha}\,\mathbf{n}_A = \left(\dot{\xi}_P - R\dot{\alpha}\right)\mathbf{t}_A + \xi_P\dot{\alpha}\,\mathbf{n}_A $$
$$ \mathbf{a}_P = \left(\ddot{\xi}_P - R\ddot{\alpha}\right)\mathbf{t}_A + \left(\dot{\xi}_P - R\dot{\alpha}\right)\dot{\alpha}\,\mathbf{n}_A + \left(\dot{\xi}_P\dot{\alpha} + \xi_P\ddot{\alpha}\right)\mathbf{n}_A - \xi_P\dot{\alpha}^2\,\mathbf{t}_A = \left(\ddot{\xi}_P - R\ddot{\alpha} - \xi_P\dot{\alpha}^2\right)\mathbf{t}_A + \left(\xi_P\ddot{\alpha} + 2\dot{\xi}_P\dot{\alpha} - R\dot{\alpha}^2\right)\mathbf{n}_A $$
$$ \mathbf{v}_Q = \left(\dot{\xi}_Q + R\dot{\beta}\right)\mathbf{t}_B - \xi_Q\dot{\beta}\,\mathbf{n}_B, \qquad \mathbf{a}_Q = \left(\ddot{\xi}_Q + R\ddot{\beta} - \xi_Q\dot{\beta}^2\right)\mathbf{t}_B - \left(\xi_Q\ddot{\beta} + 2\dot{\xi}_Q\dot{\beta} + R\dot{\beta}^2\right)\mathbf{n}_B $$
$\mathbf{a}_Q$ follows from $\mathbf{v}_Q$ exactly as $\mathbf{a}_P$ from $\mathbf{v}_P$, with $\dot{\mathbf{t}}_B$ and $\dot{\mathbf{n}}_B$ of Phase 2 and $\beta$ in place of $\alpha$. In terms of the chosen coordinates $(\alpha, \beta, \xi_P)$: $\xi_Q = L - \xi_P - R(\beta - \alpha)$, $\dot{\xi}_Q = -\dot{\xi}_P - R(\dot{\beta} - \dot{\alpha})$ (so $\dot{\xi}_Q + R\dot{\beta} = R\dot{\alpha} - \dot{\xi}_P$) and $\ddot{\xi}_Q + R\ddot{\beta} = R\ddot{\alpha} - \ddot{\xi}_P$.

#### 3.2 Forces
##### (c) Forces on $P$ and $Q$
* **Weights:** $-mg\,\mathbf{j}$ on each particle.
* **String tension** $T \ge 0$ (the same on both sides: the cylinder is smooth and the string massless): $-T\,\mathbf{t}_A$ on $P$ and $-T\,\mathbf{t}_B$ on $Q$, directed toward the tangency points.
* **Spring** (zero natural length): $\mathbf{F}_{s,P} = k\,\mathbf{d}$ and $\mathbf{F}_{s,Q} = -k\,\mathbf{d}$, with $\mathbf{d} = \mathbf{r}_Q - \mathbf{r}_P$.
* **Inertia forces:** none. The projections of the weight on the bases are $\mathbf{j}\cdot\mathbf{t}_A = -\cos\alpha$, $\mathbf{j}\cdot\mathbf{n}_A = \sin\alpha$, $\mathbf{j}\cdot\mathbf{t}_B = \cos\beta$, $\mathbf{j}\cdot\mathbf{n}_B = \sin\beta$.

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law for $P$ and $Q$, projected on the bases of the contact points, gives four scalar equations; together with the length constraint there are 5 equations for the 5 unknowns $\alpha, \beta, \xi_P, \xi_Q, T$:
$$ m\left(\ddot{\xi}_P - R\ddot{\alpha} - \xi_P\dot{\alpha}^2\right) = -T + mg\cos\alpha + k\,\mathbf{d}\cdot\mathbf{t}_A $$
$$ m\left(\xi_P\ddot{\alpha} + 2\dot{\xi}_P\dot{\alpha} - R\dot{\alpha}^2\right) = -mg\sin\alpha + k\,\mathbf{d}\cdot\mathbf{n}_A $$
$$ m\left(\ddot{\xi}_Q + R\ddot{\beta} - \xi_Q\dot{\beta}^2\right) = -T - mg\cos\beta - k\,\mathbf{d}\cdot\mathbf{t}_B $$
$$ -m\left(\xi_Q\ddot{\beta} + 2\dot{\xi}_Q\dot{\beta} + R\dot{\beta}^2\right) = -mg\sin\beta - k\,\mathbf{d}\cdot\mathbf{n}_B $$
* **Decoupling.** Subtracting the first and third equations removes the tension $T$; the remaining equations, with the length constraint, determine the three coordinates, and $T$ is computed afterwards.

#### 3.4 Integration and Answers
##### (a) Degrees of freedom
* $\text{CDOF} = 3$ (see Phase 1): for example $(\alpha, \beta, \xi_P)$.

##### (d) Mechanical energy
* **Pedagogical Justification:** the energy of $P$ alone is not conserved: the tension and the spring both do work on it, and that work is exchanged with $Q$. For the system $P + Q$, the only forces that could dissipate energy are the tensions, so their total power is computed first, with $\mathbf{t}_A\cdot\mathbf{v}_P = \dot{\xi}_P - R\dot{\alpha}$ and $\mathbf{t}_B\cdot\mathbf{v}_Q = \dot{\xi}_Q + R\dot{\beta}$:
$$ \dot{W}_T = -T\,\mathbf{t}_A\cdot\mathbf{v}_P - T\,\mathbf{t}_B\cdot\mathbf{v}_Q = -T\,\frac{d}{dt}\left[\xi_P + \xi_Q + R(\beta - \alpha)\right] = -T\dot{L} = 0 $$
* The tensions do zero net work. Gravity and the spring are conservative, so the total mechanical energy of the system is conserved, with the potential energy
$$ V = mg\left(y_P + y_Q\right) + \tfrac{1}{2}k\left|\mathbf{r}_Q - \mathbf{r}_P\right|^2, \qquad E = \tfrac{1}{2}m\left(v_P^2 + v_Q^2\right) + V = \text{const} $$

##### (e) Symmetric configurations about $Oy$
* **Pedagogical Justification:** if the motion keeps the mirror symmetry about $Oy$, then $\beta = \pi - \alpha$ and $\xi_P = \xi_Q = \xi$. The length constraint becomes $2\xi + R(\pi - 2\alpha) = L$, i.e.
$$ \xi(\alpha) = \ell_0 + R\alpha, \qquad \ell_0 = \frac{L - \pi R}{2} $$
* The system has $\text{CDOF} = 1$, the angle $\alpha$. The relations between the previous coordinates are $\beta = \pi - \alpha$, $\xi_P = \xi_Q = \ell_0 + R\alpha$ and $\dot{\xi} = R\dot{\alpha}$.

##### (f) Equilibrium and small oscillations
* **Pedagogical Justification:** with the symmetry, one coordinate $\alpha$ describes the system. The coordinates of $P$ are $x_P = R\cos\alpha + \xi\sin\alpha$ and $y_P = R\sin\alpha - \xi\cos\alpha$. Differentiating with respect to $\alpha$ (with $\xi' = R$):
$$ x_P' = -R\sin\alpha + R\sin\alpha + \xi\cos\alpha = \xi\cos\alpha, \qquad y_P' = R\cos\alpha - R\cos\alpha + \xi\sin\alpha = \xi\sin\alpha $$
so $v_P = \xi\dot{\alpha}$. By symmetry $x_Q = -x_P$, $y_Q = y_P$ and $|\mathbf{r}_Q - \mathbf{r}_P| = 2x_P$:
$$ K = 2\cdot\tfrac{1}{2}m\xi^2\dot{\alpha}^2 = m\xi^2\dot{\alpha}^2, \qquad V(\alpha) = 2mgy_P + \tfrac{1}{2}k(2x_P)^2 = 2mgy_P + 2kx_P^2 $$
$$ V'(\alpha) = 2mg\xi\sin\alpha + 4kx_P\xi\cos\alpha = 2\xi f(\alpha), \qquad f(\alpha) = mg\sin\alpha + 2k\cos\alpha\left(R\cos\alpha + \xi\sin\alpha\right) $$
* **Equilibrium.** $V'(\alpha_0) = 0$, i.e. $f(\alpha_0) = 0$ (since $\xi \gt 0$). Physically, the horizontal pull $2kx_P$ of the spring must be balanced by the horizontal component of the tension, which needs $\alpha_0 \lt 0$: the segments $AP$ and $BQ$ are slightly inclined inward. For a small deviation from the vertical, $|\alpha_0| \ll 1$, keep first-order terms ($\sin\alpha \approx \alpha$, $\cos\alpha \approx 1$, $\xi \approx \ell_0$):
$$ mg\alpha_0 + 2k\left(R + \ell_0\alpha_0\right) = 0 \implies \alpha_0 \approx -\frac{2kR}{mg + 2k\ell_0} $$
and the other coordinates at equilibrium follow from the symmetry relations: $\beta_0 = \pi - \alpha_0 \approx \pi + \dfrac{2kR}{mg + 2k\ell_0}$ and $\xi_0 = \ell_0 + R\alpha_0 \approx \ell_0 - \dfrac{2kR^2}{mg + 2k\ell_0}$.
* **Equation of motion.** From $\frac{d}{dt}(K + V) = 0$ with the chain rule and $\dot{\xi} = R\dot{\alpha}$:
$$ 2m\xi^2\dot{\alpha}\ddot{\alpha} + 2m\xi R\dot{\alpha}^3 + 2\xi f\dot{\alpha} = 0 \implies m\xi\ddot{\alpha} + mR\dot{\alpha}^2 + f(\alpha) = 0 $$
This is the $\mathbf{n}_A$ equation of 3.3 with $\dot{\xi}_P = R\dot{\alpha}$ and $\mathbf{d}\cdot\mathbf{n}_A = -2x_P\cos\alpha$.
* **Linearisation.** Put $\alpha = \alpha_0 + \delta$ with $\delta$ small: $\dot{\alpha}^2$ is second order and $f(\alpha) \approx f'(\alpha_0)\delta$, with $f'(\alpha) = mg\cos\alpha + 2k\left[\xi\cos^2\alpha - x_P\sin\alpha\right] \approx mg + 2k\ell_0$:
$$ \ddot{\delta} + \frac{mg + 2k\ell_0}{m\ell_0}\,\delta = 0 \implies \omega^2 = \frac{g}{\ell_0} + \frac{2k}{m}, \qquad \boxed{\omega = \sqrt{\frac{g}{\ell_0} + \frac{2k}{m}}} $$

### Phase 4: Interpretation & Checks
* **Limit $k \to 0$:** $\omega = \sqrt{g/\ell_0}$, the pendulum of length $\ell_0$ (the free length of each hanging segment).
* **Limit $g \to 0$:** $\omega = \sqrt{2k/m}$, the frequency of two particles of mass $m$ joined by a spring $k$ (reduced mass $m/2$ and stiffness $k$). In this limit $\alpha_0 \to -R/\ell_0$, which is small only if $R \ll \ell_0$; otherwise the limit lies outside the small-angle hypothesis.
* **Dimensional check:** $[g/\ell_0] = \text{s}^{-2}$, $[2k/m] = \text{N m}^{-1}\text{kg}^{-1} = \text{s}^{-2}$; $[\alpha_0] = [kR/(mg + 2k\ell_0)] = 1$.
* **Check against the official key:** `Problems.pdf` gives only the spring force, $\mathbf{F}_{S,P} = -\mathbf{F}_{S,Q} = k\overrightarrow{PQ} = k(\mathbf{r}_Q - \mathbf{r}_P)$ written in its own coordinates, which is the same vector as $k\,\mathbf{d}$ above. The remaining results are verified by independent derivation and numerically ($R = 1$ m, $\ell_0 = 2$ m, $m = 1$ kg, $k = 0.3$ N/m, $g = 9.81$ m/s$^2$): the exact root of $f(\alpha_0) = 0$ is $\alpha_0 = -0.054532$ rad against $-0.054496$ rad from the linear formula, and integrating $m\xi\ddot{\alpha} + mR\dot{\alpha}^2 + f = 0$ gives $\omega^2 = 5.6482$ s$^{-2}$, equal to $f'(\alpha_0)/(m\xi(\alpha_0))$; the difference with $g/\ell_0 + 2k/m = 5.505$ s$^{-2}$ is the first-order correction $\xi(\alpha_0) = \ell_0 + R\alpha_0$ in place of $\ell_0$.

---

## 📌 Problem 38: Particle on Torus

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ ($m_P = 1$) moves without friction on the vertical torus $x_0 = (2 + \cos\phi)\sin\theta$, $y_0 = \sin\phi$, $z_0 = 4 + (2 + \cos\phi)\cos\theta$, and cannot separate from its surface. A second particle $Q$ ($m_Q = 2$) is constrained to the plane $Ox_0y_0$ without friction. $P$ and $Q$ attract each other with a force proportional to their distance, with constant $k = 2$.
* **Initial state:** $\mathbf{r}_P(t_0) = 2\mathbf{i}_0 + \mathbf{j}_0 + 4\mathbf{k}_0$, $\mathbf{v}_P(t_0) = -\mathbf{k}_0$; $\mathbf{r}_Q(t_0) = 3\mathbf{i}_0 + \mathbf{j}_0$, $\mathbf{v}_Q(t_0) = -\mathbf{i}_0 + \mathbf{j}_0$.
* **Constraints and degrees of freedom (a):** two free particles have $6$ coordinates. $P$ is on the torus surface ($1$ constraint) and $Q$ is on the plane $z_0 = 0$ ($1$ constraint), so $\text{CDOF} = 6 - 2 = 4$. A minimal set: $(\theta, \phi)$ for $P$, where $\theta$ is the toroidal angle (rotation about $\mathbf{j}_0$ of the axis of the torus, which passes through $z_0 = 4$) and $\phi$ the poloidal angle (angle around the tube, whose centre circle has radius $2$ and the tube radius is $1$); and $(\xi, \eta)$ for $Q$, its Cartesian coordinates in the plane.
* **Initial values of the coordinates:** from $x_0 = 2$, $y_0 = 1$, $z_0 = 4$: $\sin\phi = 1$ and $(2 + \cos\phi)\sin\theta = 2$, so $\phi = \theta = \pi/2$. The initial velocity $-\mathbf{k}_0$ gives $\dot{\theta}(0) = 1/2$ and $\dot{\phi}(0) = 0$ (shown in 3.1), and $\xi = 3$, $\eta = 1$, $\dot{\xi} = -1$, $\dot{\eta} = 1$.
* **Parameters:** $m_P = 1$, $m_Q = 2$, $k = 2$, $g = 9.81$ m/s$^2$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{k}_0$ vertical upward.
* **Toroidal basis.** With $\theta$ (rotation about $\mathbf{j}_0$): $\mathcal{B}_1 = \{\mathbf{e}_\rho, \mathbf{e}_\theta, \mathbf{j}_0\}$ with $\mathbf{e}_\rho = \sin\theta\,\mathbf{i}_0 + \cos\theta\,\mathbf{k}_0$ and $\mathbf{e}_\theta = \cos\theta\,\mathbf{i}_0 - \sin\theta\,\mathbf{k}_0$ (so $\mathbf{e}_\rho\times\mathbf{e}_\theta = \mathbf{j}_0$):
$$ [{}_0 R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \\ \cos\theta & -\sin\theta & 0 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
with $\dot{\mathbf{e}}_\rho = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_\rho$.
* **Poloidal basis.** With $\phi$ (rotation about $\mathbf{e}_\theta$): $\mathcal{B}_2 = \{\mathbf{n}, \mathbf{e}_\theta, \mathbf{t}_\phi\}$ with $\mathbf{n} = \cos\phi\,\mathbf{e}_\rho + \sin\phi\,\mathbf{j}_0$ (outward normal) and $\mathbf{t}_\phi = -\sin\phi\,\mathbf{e}_\rho + \cos\phi\,\mathbf{j}_0$:
$$ [{}_1 R_2] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_1 R_2] = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** with $\varrho \equiv 2 + \cos\phi$, the position of $P$ is $\mathbf{r}_P = 4\mathbf{k}_0 + \varrho\,\mathbf{e}_\rho + \sin\phi\,\mathbf{j}_0$ and that of $Q$ is $\mathbf{r}_Q = \xi\,\mathbf{i}_0 + \eta\,\mathbf{j}_0$. With $\dot{\varrho} = -\sin\phi\,\dot{\phi}$ and Poisson's formula,
$$ \mathbf{v}_P = -\sin\phi\,\dot{\phi}\,\mathbf{e}_\rho + \varrho\dot{\theta}\,\mathbf{e}_\theta + \cos\phi\,\dot{\phi}\,\mathbf{j}_0, \qquad v_P^2 = \dot{\phi}^2 + \varrho^2\dot{\theta}^2 $$
$$ \mathbf{a}_P = \left(\ddot{\varrho} - \varrho\dot{\theta}^2\right)\mathbf{e}_\rho + \left(\varrho\ddot{\theta} + 2\dot{\varrho}\dot{\theta}\right)\mathbf{e}_\theta + \left(\cos\phi\,\ddot{\phi} - \sin\phi\,\dot{\phi}^2\right)\mathbf{j}_0, \qquad \ddot{\varrho} = -\cos\phi\,\dot{\phi}^2 - \sin\phi\,\ddot{\phi} $$
$$ \mathbf{v}_Q = \dot{\xi}\,\mathbf{i}_0 + \dot{\eta}\,\mathbf{j}_0, \qquad \mathbf{a}_Q = \ddot{\xi}\,\mathbf{i}_0 + \ddot{\eta}\,\mathbf{j}_0 $$
* **Initial rates.** At $\theta = \phi = \pi/2$: $\mathbf{e}_\theta = -\mathbf{k}_0$, $\varrho = 2$, so $\mathbf{v}_P = -\dot{\phi}\,\mathbf{e}_\rho - 2\dot{\theta}\,\mathbf{k}_0 = -\mathbf{k}_0$ gives $\dot{\theta}(0) = 1/2$ and $\dot{\phi}(0) = 0$.

##### (c) Two tangent vectors and one normal vector to the torus
* The two independent tangent vectors are the partial derivatives of $\mathbf{r}_P$, and the normal is their cross product:
$$ \frac{\partial\mathbf{r}_P}{\partial\theta} = \varrho\,\mathbf{e}_\theta, \qquad \frac{\partial\mathbf{r}_P}{\partial\phi} = \mathbf{t}_\phi, \qquad \frac{\partial\mathbf{r}_P}{\partial\theta}\times\frac{\partial\mathbf{r}_P}{\partial\phi} = \varrho\,\mathbf{n} $$

#### 3.2 Forces
##### (d) Forces on $P$ and $Q$
* **On $P$:** its weight $-m_Pg\,\mathbf{k}_0$; the attraction of $Q$, $\mathbf{F} = k\left(\mathbf{r}_Q - \mathbf{r}_P\right)$; and the reaction of the smooth torus $N\,\mathbf{n}$ (normal, with unknown magnitude; it does not enter the tangent projections). Explicitly,
$$ \mathbf{F} = 2\left[\xi - (2 + \cos\phi)\sin\theta\right]\mathbf{i}_0 + 2\left[\eta - \sin\phi\right]\mathbf{j}_0 - 2\left[4 + (2 + \cos\phi)\cos\theta\right]\mathbf{k}_0 $$
* **On $Q$:** the attraction $-\mathbf{F}$ and its weight $-m_Qg\,\mathbf{k}_0$, balanced by the vertical reaction of the smooth plane (so the motion of $Q$ is horizontal). **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (e) Second-order equations for the four coordinates
* **Pedagogical Justification:** the unknown reaction $N\,\mathbf{n}$ is orthogonal to the two tangent vectors, so projecting Newton's second law for $P$ on $\mathbf{e}_\theta$ and on $\mathbf{t}_\phi$ gives two equations free of $N$. With $\mathbf{k}_0 = \cos\theta\,\mathbf{e}_\rho - \sin\theta\,\mathbf{e}_\theta$, $\mathbf{i}_0 = \sin\theta\,\mathbf{e}_\rho + \cos\theta\,\mathbf{e}_\theta$, and the accelerations of 3.1:
$$ \mathbf{a}_P\cdot\mathbf{e}_\theta = \varrho\ddot{\theta} - 2\sin\phi\,\dot{\phi}\dot{\theta}, \qquad \mathbf{a}_P\cdot\mathbf{t}_\phi = \ddot{\phi} + \varrho\sin\phi\,\dot{\theta}^2 $$
$$ \left(\mathbf{F} - m_Pg\,\mathbf{k}_0\right)\cdot\mathbf{e}_\theta = m_Pg\sin\theta + k\left(\xi\cos\theta + 4\sin\theta\right) $$
$$ \left(\mathbf{F} - m_Pg\,\mathbf{k}_0\right)\cdot\mathbf{t}_\phi = m_Pg\sin\phi\cos\theta + k\left(-\xi\sin\phi\sin\theta + \eta\cos\phi + 4\sin\phi\cos\theta + 2\sin\phi\right) $$
* **Equations of motion** (with $m_P = 1$, $m_Q = 2$, $k = 2$; for $Q$, $m_Q\ddot{\xi} = -k(\xi - x_P)$ and $m_Q\ddot{\eta} = -k(\eta - y_P)$):
$$ (2 + \cos\phi)\,\ddot{\theta} = 2\sin\phi\,\dot{\phi}\dot{\theta} + g\sin\theta + 2\left(\xi\cos\theta + 4\sin\theta\right) $$
$$ \ddot{\phi} = -(2 + \cos\phi)\sin\phi\,\dot{\theta}^2 + g\sin\phi\cos\theta + 2\left(-\xi\sin\phi\sin\theta + \eta\cos\phi + 4\sin\phi\cos\theta + 2\sin\phi\right) $$
$$ \ddot{\xi} = -\left[\xi - (2 + \cos\phi)\sin\theta\right], \qquad \ddot{\eta} = -\left[\eta - \sin\phi\right] $$
* **Check of closure:** four unknown coordinates and four equations; the reaction of the torus follows afterwards from the $\mathbf{n}$ projection (the statement says that $P$ cannot separate from the surface, so the constraint is bilateral and $N$ may have either sign).

#### 3.4 Integration and Answers
##### (f) A scalar conservation law
* **Pedagogical Justification:** the reactions of the torus and of the plane are normal to the velocities of $P$ and $Q$ and do no work; gravity and the spring are conservative; there are no other forces. The total mechanical energy of the system is conserved:
$$ E = \tfrac{1}{2}m_Pv_P^2 + \tfrac{1}{2}m_Qv_Q^2 + m_Pgz_P + \tfrac{1}{2}k\left|\mathbf{r}_P - \mathbf{r}_Q\right|^2 = \text{const} $$
* **Initial value:**
$$ T_P = \tfrac{1}{2}(1)(1)^2 = \tfrac{1}{2}, \qquad T_Q = \tfrac{1}{2}(2)\left((-1)^2 + 1^2\right) = 2, \qquad V_g = m_Pgz_P(t_0) = 4g $$
$$ \left|\mathbf{r}_P - \mathbf{r}_Q\right|^2 = (2 - 3)^2 + (1 - 1)^2 + (4 - 0)^2 = 17 \implies V_{\text{spring}} = \tfrac{1}{2}(2)(17) = 17, \qquad E_0 = \tfrac{1}{2} + 2 + 4g + 17 = 19.5 + 4g $$

##### (g) Can $P$ reach the highest point of the torus?
* **Pedagogical Justification:** use the conservation law alone. The highest point of the torus is at $\phi = 0$, $\theta = 0$, with $z_{\max} = 4 + (2 + 1) = 7$. There the gravitational energy of $P$ is $7g$, and the other terms of $E$ (the kinetic energies and the spring energy) are non-negative, so reaching the summit requires $E_0 \ge 7g$:
$$ E_0 = 19.5 + 4g \ge 7g \iff 19.5 \ge 3g = 29.43 \quad\text{(false)} $$
* **Answer:** no. With $g = 9.81$ m/s$^2$, $E_0 = 58.74$ J and the summit needs at least $7g = 68.67$ J, a deficit of $9.93$ J.

### Phase 4: Interpretation & Checks
* **Robustness:** for a general stiffness $E_0 = 2.5 + 4g + 8.5k$. At the summit $z_P = 7$ and $z_Q = 0$, so $|\mathbf{r}_P - \mathbf{r}_Q| \ge 7$ and $V_{\text{spring}} \ge \tfrac12 k\cdot 49 = 24.5k$. Reaching it requires $2.5 + 4g + 8.5k \ge 7g + 24.5k$, i.e. $2.5 \ge 3g + 16k$, false for every $k \ge 0$: the conclusion does not depend on $k$. (With $k = 2$: $58.74$ J against at least $68.67 + 49 = 117.67$ J.)
* **Dimensional check:** $[k|\mathbf{r}_P - \mathbf{r}_Q|^2] = \text{N m}^{-1}\text{m}^2 = \text{J}$, $[mgz] = \text{J}$ and $[mv^2] = \text{J}$.
* **Check against the official key:** `Problems.pdf` gives the force on $P$ due to $Q$, $\mathbf{F}_P = 2\left[\xi - (2 + \cos\phi)\sin\theta\right]\mathbf{i}_0 + 2\left[\eta - \sin\phi\right]\mathbf{j}_0 - 2\left[4 + (2 + \cos\phi)\cos\theta\right]\mathbf{k}_0$ (the key writes the same vector with its own letters), identical to part (d). The rest is verified by independent derivation. Sympy confirms the two tangent vectors and the normal, the projections of $\mathbf{a}_P$ and of the forces used in (e), and numerical integration of the four equations (DOP853) conserves $E$ to $2\times 10^{-11}$ with $E_0 = 58.74$ and keeps $z_P \le 4$ over $6$ s (the summit $z = 7$ is not approached).

---

## 📌 Problem 39: Particle on a String with a Plate

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $P$ of mass $m$ hangs from a massless inextensible string of length $\ell$ anchored at the point $O$ of the upper surface of a thin horizontal plate. The string passes without friction over the straight edge of the plate, at perpendicular distance $d$ from $O$, at the contact point $Q$; it remains taut and in contact with the plate.
* **Geometry (read from the figure, `Problems.pdf` PDF page 27).** The edge is the straight line $x_0 = d$, parallel to $\mathbf{j}_0$ ($Ox_0$ is perpendicular to the edge); $\theta$ is the angle between $Ox_0$ and $OQ$, so $\mathbf{r}_Q = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0$; and $\phi$ is the angle between the vertical and the line through $P$ perpendicular to the edge, which lies in a plane normal to the edge. The statement text does not fix the direction of the edge, so this reading relies on the figure.
* **Constraints and degrees of freedom (a):** $P$ has $3$ coordinates. The string has constant length: $|OQ| + |QP| = \ell$ with $Q$ on the edge, and $Q$ slides on the edge (the position of $Q$ on the edge is not fixed). The frictionless sliding over the edge makes the two string segments meet the edge at equal angles (the hint of the statement). Counting: the $3$ coordinates of $P$ minus the single length constraint give $\text{CDOF} = 3 - 1 = 2$; $Q$ adds no unknown, because the equal-angle condition fixes it once $\theta$ is known. These conditions leave the two independent coordinates $\theta$ and $\phi$: $\text{CDOF} = 2$.
* **Initial state:** $\theta(0) = \phi(0) = \pi/3$ and $|\mathbf{v}_P(0)| = \sqrt{\ell g}$.
* **Parameters:** $m$, $\ell$, $d$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$ with $\mathbf{k}_0$ vertical upward; the plate in the plane $z_0 = 0$.
* **Lengths:** $|OQ| = d/\cos\theta$, so the hanging segment has length $\rho = \ell - \dfrac{d}{\cos\theta}$.
* **Swing basis.** The hanging segment $QP$ swings in the plane normal to the edge, i.e. about the direction $\mathbf{j}_0$. The basis $\mathcal{B}_1 = \{\mathbf{i}_1, \mathbf{j}_0, \mathbf{k}_1\}$ is the inertial basis rotated by $-\phi$ about $\mathbf{j}_0$ (by $\phi$ about $-\mathbf{j}_0$), with $\mathbf{i}_1 = \cos\phi\,\mathbf{i}_0 + \sin\phi\,\mathbf{k}_0$ and $\mathbf{k}_1 = -\sin\phi\,\mathbf{i}_0 + \cos\phi\,\mathbf{k}_0$ (columns in $\mathcal{B}_0$):
$$ [{}_0 R_1] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \\ 0 & 1 & 0 \\ \sin\phi & 0 & \cos\phi \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\phi + \sin^2\phi = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Unit vector from $Q$ to $P$
* **Pedagogical Justification:** the edge is frictionless, so the two string segments make equal angles with it (the hint). The unit vector from $Q$ to $O$ is $-\left(\cos\theta\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0\right)$, hence $\mathbf{e}_{QP}\cdot\mathbf{j}_0 = \sin\theta$. The remaining part of $\mathbf{e}_{QP}$ lies in the plane normal to the edge, along $\sin\phi\,\mathbf{i}_0 - \cos\phi\,\mathbf{k}_0 = -\mathbf{k}_1$, with magnitude $\sqrt{1 - \sin^2\theta} = \cos\theta$:
$$ \mathbf{e}_{QP} = \cos\theta\sin\phi\,\mathbf{i}_0 + \sin\theta\,\mathbf{j}_0 - \cos\theta\cos\phi\,\mathbf{k}_0 = \sin\theta\,\mathbf{j}_0 - \cos\theta\,\mathbf{k}_1, \qquad |\mathbf{e}_{QP}|^2 = \cos^2\theta\left(\sin^2\phi + \cos^2\phi\right) + \sin^2\theta = 1 $$

##### (c) Position, velocity and acceleration
* **Pedagogical Justification:** $Q$ is on the edge and $P$ hangs at the distance $\rho$ along $\mathbf{e}_{QP}$:
$$ \mathbf{r}_Q = d\,\mathbf{i}_0 + d\tan\theta\,\mathbf{j}_0, \qquad \mathbf{v}_Q = \frac{d\dot{\theta}}{\cos^2\theta}\,\mathbf{j}_0, \qquad \mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP} $$
$$ \mathbf{r}_P = \left[d + (\ell\cos\theta - d)\sin\phi\right]\mathbf{i}_0 + \left[d\tan\theta + \left(\ell - \frac{d}{\cos\theta}\right)\sin\theta\right]\mathbf{j}_0 - (\ell\cos\theta - d)\cos\phi\,\mathbf{k}_0 $$
(using $\rho\cos\theta = \ell\cos\theta - d$). Write $u \equiv \ell\cos\theta - d = \rho\cos\theta \ge 0$. The $\mathbf{j}_0$ component simplifies, $d\tan\theta + \ell\sin\theta - d\tan\theta = \ell\sin\theta$, so
$$ \mathbf{r}_P = \left(d + u\sin\phi\right)\mathbf{i}_0 + \ell\sin\theta\,\mathbf{j}_0 - u\cos\phi\,\mathbf{k}_0, \qquad z_P = -u\cos\phi, \qquad \frac{du}{d\theta} = -\ell\sin\theta $$
* **Velocity of $P$.** The chain rule gives $\mathbf{v}_P = \mathbf{t}_\theta\dot{\theta} + \mathbf{t}_\phi\dot{\phi}$ with the tangent vectors
$$ \mathbf{t}_\theta = \frac{\partial\mathbf{r}_P}{\partial\theta} = \ell\begin{pmatrix} -\sin\theta\sin\phi \\ \cos\theta \\ \sin\theta\cos\phi \end{pmatrix}, \qquad \mathbf{t}_\phi = \frac{\partial\mathbf{r}_P}{\partial\phi} = u\begin{pmatrix} \cos\phi \\ 0 \\ \sin\phi \end{pmatrix} $$
They are orthogonal ($\mathbf{t}_\theta\cdot\mathbf{t}_\phi = \ell u\sin\theta\sin\phi\cos\phi\,(-1 + 1) = 0$) with $|\mathbf{t}_\theta|^2 = \ell^2\left(\sin^2\theta + \cos^2\theta\right) = \ell^2$ and $|\mathbf{t}_\phi|^2 = u^2$, so
$$ v_P^2 = \ell^2\dot{\theta}^2 + u^2\dot{\phi}^2 $$
* **Acceleration of $P$.** Differentiating once more (product rule, with $\mathbf{t}_{\theta\theta} = \partial^2\mathbf{r}_P/\partial\theta^2$ and so on):
$$ \mathbf{a}_P = \mathbf{t}_\theta\ddot{\theta} + \mathbf{t}_\phi\ddot{\phi} + \mathbf{t}_{\theta\theta}\dot{\theta}^2 + 2\mathbf{t}_{\theta\phi}\dot{\theta}\dot{\phi} + \mathbf{t}_{\phi\phi}\dot{\phi}^2 $$
$$ \mathbf{t}_{\theta\theta} = \ell\begin{pmatrix} -\cos\theta\sin\phi \\ -\sin\theta \\ \cos\theta\cos\phi \end{pmatrix}, \quad \mathbf{t}_{\theta\phi} = -\ell\sin\theta\begin{pmatrix} \cos\phi \\ 0 \\ \sin\phi \end{pmatrix}, \quad \mathbf{t}_{\phi\phi} = u\begin{pmatrix} -\sin\phi \\ 0 \\ \cos\phi \end{pmatrix} $$
* **Velocity and acceleration of $Q$.** From $\mathbf{v}_Q = d\dot{\theta}\cos^{-2}\theta\,\mathbf{j}_0$ and $\frac{d}{dt}\cos^{-2}\theta = 2\sin\theta\cos^{-3}\theta\,\dot{\theta}$:
$$ \mathbf{a}_Q = \frac{d\left(\ddot{\theta}\cos\theta + 2\dot{\theta}^2\sin\theta\right)}{\cos^3\theta}\,\mathbf{j}_0 $$

#### 3.2 Forces
##### (d) Forces on $P$
* **Weight:** $-mg\,\mathbf{k}_0$. **String tension:** along the segment $QP$, toward $Q$: $\mathbf{T} = -T\,\mathbf{e}_{QP}$ with $T \ge 0$. The edge acts on the string, not on $P$. **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (f) Work of the tension (needed to eliminate $T$ from the equations)
* **Pedagogical Justification:** the tension acts along $-\mathbf{e}_{QP}$ on $P$, so its power is $-T\,\mathbf{e}_{QP}\cdot\mathbf{v}_P$. Differentiating $\mathbf{r}_P = \mathbf{r}_Q + \rho\,\mathbf{e}_{QP}$ (product rule) gives $\mathbf{v}_P = \mathbf{v}_Q + \dot{\rho}\,\mathbf{e}_{QP} + \rho\,\dot{\mathbf{e}}_{QP}$. Since $|\mathbf{e}_{QP}| = 1$, $\mathbf{e}_{QP}\cdot\dot{\mathbf{e}}_{QP} = \tfrac{1}{2}\frac{d}{dt}|\mathbf{e}_{QP}|^2 = 0$, so
$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \mathbf{e}_{QP}\cdot\mathbf{v}_Q + \dot{\rho} $$
* $\mathbf{v}_Q$ has only a $\mathbf{j}_0$ component, so $\mathbf{e}_{QP}\cdot\mathbf{v}_Q = \sin\theta\,\dfrac{d\dot{\theta}}{\cos^2\theta}$. With the chain rule $\frac{d}{dt}\left(\frac{1}{\cos\theta}\right) = \frac{\sin\theta}{\cos^2\theta}\dot{\theta}$, the hanging length changes at the rate $\dot{\rho} = -\dfrac{d\dot{\theta}\sin\theta}{\cos^2\theta}$. Therefore
$$ \mathbf{e}_{QP}\cdot\mathbf{v}_P = \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} - \frac{d\dot{\theta}\sin\theta}{\cos^2\theta} = 0 \implies \mathbf{T}\cdot\mathbf{v}_P = 0 $$
The tension does **no work** on $P$ ($W_T = 0$).
* **Consequence.** The identity holds for arbitrary $\dot{\theta}$ and $\dot{\phi}$, so $\mathbf{e}_{QP}$ is orthogonal to both tangent vectors $\partial\mathbf{r}_P/\partial\theta$ and $\partial\mathbf{r}_P/\partial\phi$. Projecting Newton's second law on these two vectors therefore removes the tension.

##### (e) Second-order equations for $\theta$ and $\phi$
* **Pedagogical Justification:** Newton's second law $m\mathbf{a}_P = -mg\,\mathbf{k}_0 + \mathbf{T}$ is projected on $\mathbf{t}_\theta$ and $\mathbf{t}_\phi$, which are orthogonal to $\mathbf{T}$ (part f), so the tension drops out: $m\,\mathbf{a}_P\cdot\mathbf{t}_q = -mg\,\mathbf{k}_0\cdot\mathbf{t}_q$ for $q = \theta, \phi$. The scalar products of the vectors of 3.1(c) are
$$ \mathbf{t}_{\theta\theta}\cdot\mathbf{t}_\theta = \ell^2\left(\cos\theta\sin\theta\sin^2\phi - \sin\theta\cos\theta + \sin\theta\cos\theta\cos^2\phi\right) = 0, \qquad \mathbf{t}_{\theta\phi}\cdot\mathbf{t}_\theta = \ell^2\sin^2\theta\left(\sin\phi\cos\phi - \sin\phi\cos\phi\right) = 0, \qquad \mathbf{t}_{\phi\phi}\cdot\mathbf{t}_\theta = \ell u\sin\theta $$
$$ \mathbf{t}_{\theta\theta}\cdot\mathbf{t}_\phi = 0, \qquad \mathbf{t}_{\theta\phi}\cdot\mathbf{t}_\phi = -\ell u\sin\theta, \qquad \mathbf{t}_{\phi\phi}\cdot\mathbf{t}_\phi = 0 $$
and the orthogonality of $\mathbf{t}_\theta$ and $\mathbf{t}_\phi$ gives
$$ \mathbf{a}_P\cdot\mathbf{t}_\theta = \ell^2\ddot{\theta} + \ell u\sin\theta\,\dot{\phi}^2, \qquad \mathbf{a}_P\cdot\mathbf{t}_\phi = u^2\ddot{\phi} - 2\ell u\sin\theta\,\dot{\theta}\dot{\phi} $$
while $-g\,\mathbf{k}_0\cdot\mathbf{t}_\theta = -g\ell\sin\theta\cos\phi$ and $-g\,\mathbf{k}_0\cdot\mathbf{t}_\phi = -gu\sin\phi$. Dividing the first projection by $\ell$ and the second by $u \gt 0$:
$$ \boxed{\ell\ddot{\theta} + \left(\ell\cos\theta - d\right)\sin\theta\,\dot{\phi}^2 + g\sin\theta\cos\phi = 0} $$
$$ \boxed{\left(\ell\cos\theta - d\right)\ddot{\phi} - 2\ell\sin\theta\,\dot{\theta}\dot{\phi} + g\sin\phi = 0} $$
* **Tension (afterwards).** Along $\mathbf{e}_{QP}$: $T = mg\cos\theta\cos\phi + m\,\mathbf{v}_P\cdot\dot{\mathbf{e}}_{QP}$, since $\mathbf{a}_P\cdot\mathbf{e}_{QP} = -\mathbf{v}_P\cdot\dot{\mathbf{e}}_{QP}$ (from $\mathbf{v}_P\cdot\mathbf{e}_{QP} = 0$).

#### 3.4 Integration and Answers
##### (g) Mechanical energy
* **Pedagogical Justification:** the plate is at rest (scleronomic constraint), the tension does no work (part f) and gravity is conservative, so the mechanical energy of $P$ is conserved:
$$ E = \tfrac{1}{2}mv_P^2 + mgz_P = \tfrac{1}{2}m\left[\ell^2\dot{\theta}^2 + \left(\ell\cos\theta - d\right)^2\dot{\phi}^2\right] - mg\left(\ell\cos\theta - d\right)\cos\phi = \text{const} $$
* **Initial value.** At $t = 0$, $|\mathbf{v}_P|^2 = \ell g$ and $\cos\theta = \cos\phi = \tfrac{1}{2}$, so $z_P(0) = -\left(\tfrac{\ell}{2} - d\right)\tfrac{1}{2}$:
$$ \boxed{E_0 = \tfrac{1}{2}m\ell g - mg\left(\frac{\ell}{2} - d\right)\frac{1}{2} = \frac{mg\ell}{4} + \frac{mgd}{2}} $$
It is a conserved quantity of the motion.

### Phase 4: Interpretation & Checks
* **Variable-length spherical pendulum:** the system acts as a spherical pendulum whose length changes as $Q$ slides along the edge.
* **Limit $d \to 0$:** the edge passes through $O$, so $Q = O$, $\rho = \ell$ and $\mathbf{e}_{QP}$ is the unit vector of a spherical pendulum of length $\ell$ with $\cos\gamma = \cos\theta\cos\phi$ the cosine of its angle with the downward vertical; the energy reduces to $E_0 = mg\ell/4$, equal to $\tfrac{1}{2}m\ell g - mg\ell\cos\theta\cos\phi$ at $\theta = \phi = \pi/3$.
* **Dimensional check:** $[\rho] = \text{m}$; $[mg\ell] = [mgd] = \text{J}$; $[u] = \text{m}$ and every term of the two equations of motion has units m/s$^2$.
* **Check against the official key:** the key of `Problems.pdf` answers (f): "No, the tension does not exert work; it is easy to prove it with $\mathbf{e}_r\cdot\mathbf{v}_P^0 = 0$", which is the result of 3.3. The rest is verified by independent derivation. Sympy confirms $\mathbf{e}_{QP}\cdot\mathbf{v}_P = 0$, $v_P^2 = \ell^2\dot{\theta}^2 + (\ell\cos\theta - d)^2\dot{\phi}^2$, $z_P = (d - \ell\cos\theta)\cos\phi$, the equivalence of the two projections with the equations above, and numerically $E_0 = mg\ell/4 + mgd/2 = 7.3575$ J for $m = 1$ kg, $\ell = 2$ m, $d = 0.5$ m, equal to $\tfrac{1}{2}m\ell g + mgz_P(0) = 9.81 - 2.4525$ J.

---

## 📌 Problem 48: Two Connected Particles, One on Paraboloid

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** two heavy particles $P$ and $Q$ of mass $m$ are joined by an inextensible massless cord of length $\ell$ that passes through a small hole at the origin $O$. $P$ moves without friction on the paraboloid $z = cR^2$ ($c \gt 0$, cylindrical coordinates $\{R, \theta, z\}$); $Q$ is restricted to hang along the vertical axis $Oz$. The frame $S_0$ is inertial, there is no friction, the cord is always taut and $Q$ never reaches $O$.
* **Constraints (a):** two free particles have $6$ coordinates, and there are $4$ independent constraints:
  - $P$ on the paraboloid: $z_P = cR^2$ (1; bilateral, since the statement says $P$ is constrained to stay on the paraboloid).
  - $Q$ on the axis: $x_Q = y_Q = 0$ (2).
  - Constant cord length: $|\overrightarrow{OP}| + |z_Q| = \ell$ (1; unilateral, $T \ge 0$).
* **Degrees of freedom:** $\text{CDOF} = 6 - 4 = 2$, with $(R, \theta)$.
* **Initial state (h):** $R(0) = 1/c$, $\theta(0) = 0$, $\dot{R}(0) = 0$, $\dot{\theta}(0) = d \ne 0$.
* **Parameters:** $m$, $c$ [m$^{-1}$], $\ell$, $g$, $d$ [s$^{-1}$].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$.
* **Cylindrical basis:** $\mathcal{B}_1 = \{\mathbf{e}_R, \mathbf{e}_\theta, \mathbf{k}\}$ with $\mathbf{k} = \mathbf{k}_0$, the inertial basis rotated by $\theta(t)$ about $\mathbf{k}$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
with $\dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta$ and $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R$.
* **Surface-adapted basis.** With $s = \sqrt{1 + 4c^2R^2}$, the unit meridian tangent is $\mathbf{e}_g = (\mathbf{e}_R + 2cR\,\mathbf{k})/s$, the unit normal pointing into the bowl is $\hat{\mathbf{n}} = (-2cR\,\mathbf{e}_R + \mathbf{k})/s$, and $\mathbf{e}_g\times\mathbf{e}_\theta = \hat{\mathbf{n}}$, so
$$ [{}_1 R_2] = \begin{pmatrix} 1/s & 0 & -2cR/s \\ 0 & 1 & 0 \\ 2cR/s & 0 & 1/s \end{pmatrix}, \qquad \det[{}_1 R_2] = \frac{1 + 4c^2R^2}{s^2} = 1, \qquad [{}_1 R_2][{}_1 R_2]^T = I $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (b) Position, velocity and acceleration
* **Pedagogical Justification:** the cord runs straight from $O$ to $P$, so the length of its part on the side of $P$ is $\rho(R) = |\mathbf{r}_P| = R\sqrt{1 + c^2R^2}$, and $Q$ hangs at the depth $\ell - \rho$:
$$ \mathbf{r}_P = R\,\mathbf{e}_R + cR^2\,\mathbf{k}, \qquad \mathbf{r}_Q = -\left(\ell - \rho(R)\right)\mathbf{k} $$
* **Derivatives of $\rho$** (chain rule, with $w = \sqrt{1 + c^2R^2}$): $\rho' = \dfrac{d\rho}{dR} = w + \dfrac{c^2R^2}{w} = \dfrac{1 + 2c^2R^2}{w}$ and, by the quotient rule with $w' = c^2R/w$, $\rho'' = \dfrac{4c^2R\,w - \left(1 + 2c^2R^2\right)c^2R/w}{w^2} = \dfrac{c^2R\left[4\left(1 + c^2R^2\right) - \left(1 + 2c^2R^2\right)\right]}{w^3} = \dfrac{c^2R\left(3 + 2c^2R^2\right)}{w^3}$.
* **Particle $P$** (product rule and Poisson):
$$ \mathbf{v}_P = \dot{R}\,\mathbf{e}_R + R\dot{\theta}\,\mathbf{e}_\theta + 2cR\dot{R}\,\mathbf{k}, \qquad v_P^2 = \dot{R}^2\left(1 + 4c^2R^2\right) + R^2\dot{\theta}^2 $$
$$ \mathbf{a}_P = \left(\ddot{R} - R\dot{\theta}^2\right)\mathbf{e}_R + \left(R\ddot{\theta} + 2\dot{R}\dot{\theta}\right)\mathbf{e}_\theta + 2c\left(\dot{R}^2 + R\ddot{R}\right)\mathbf{k} $$
(Notes Sec. 2.6.2: product rule on $\dot{R}\,\mathbf{e}_R$ and $R\dot{\theta}\,\mathbf{e}_\theta$ with $\dot{\mathbf{e}}_R = \dot{\theta}\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_R$, and $\frac{d}{dt}\left(2cR\dot{R}\right) = 2c\left(\dot{R}^2 + R\ddot{R}\right)$.)
* **Particle $Q$:** $\mathbf{v}_Q = \rho'\dot{R}\,\mathbf{k}$ and $\mathbf{a}_Q = \left(\rho'\ddot{R} + \rho''\dot{R}^2\right)\mathbf{k}$.

##### (c) Tangent and normal vectors to the paraboloid
$$ \mathbf{t}_R = \frac{\partial\mathbf{r}_P}{\partial R} = \mathbf{e}_R + 2cR\,\mathbf{k}, \qquad \mathbf{t}_\theta = \frac{\partial\mathbf{r}_P}{\partial\theta} = R\,\mathbf{e}_\theta, \qquad \mathbf{n} = \mathbf{t}_R\times\mathbf{t}_\theta = R\left(-2cR\,\mathbf{e}_R + \mathbf{k}\right) $$

#### 3.2 Forces
##### (d) Forces on $P$ and $Q$
* **On $P$:** its weight $-mg\,\mathbf{k}$; the reaction of the smooth paraboloid $\mathbf{N} = N\,\hat{\mathbf{n}}$ (unknown magnitude $N$, normal to the surface); and the tension of the cord, directed toward the hole, $\mathbf{T}_P = -T\,\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}$.
* **On $Q$:** its weight $-mg\,\mathbf{k}$, the tension $\mathbf{T}_Q = +T\,\mathbf{k}$ (same cord, smooth hole), and the horizontal reaction $\mathbf{R}_Q$ of the vertical guide.
* **Inertia forces:** none ($S_0$ is inertial).

#### 3.3 Equations of Motion
##### (f) Two second-order equations for $R$ and $\theta$
* **Pedagogical Justification:** the unknowns are $R$, $\theta$, $T$, $N$ and the two components of $\mathbf{R}_Q$, i.e. $6$ unknowns, and Newton's second law for $P$ and $Q$ gives $6$ scalar equations. Projecting the equation of $P$ on the tangent vectors removes the normal reaction $N$, and the equation of $Q$ gives $T$ and $\mathbf{R}_Q = \mathbf{0}$ (since $\mathbf{a}_Q \parallel \mathbf{k}$):
$$ Q,\ \mathbf{k}: \; m\left(\rho'\ddot{R} + \rho''\dot{R}^2\right) = T - mg \implies T = m\left(g + \rho'\ddot{R} + \rho''\dot{R}^2\right) $$
* **Equation for $\theta$.** Projecting on $\mathbf{e}_\theta$ (no component of the reaction, of gravity or of the tension, which lies in the meridian plane): $m\left(R\ddot{\theta} + 2\dot{R}\dot{\theta}\right) = 0$, i.e. $\dfrac{m}{R}\dfrac{d}{dt}\left(R^2\dot{\theta}\right) = 0$.
* **Equation for $R$.** Projecting on $\mathbf{t}_R$: the tension component is $-T\,\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}\cdot\mathbf{t}_R = -T\rho'$ (because $\dfrac{\mathbf{r}_P}{|\mathbf{r}_P|}\cdot\mathbf{t}_R = \dfrac{R + 2c^2R^3}{R w} = \rho'$) and the weight gives $-mg\,\mathbf{k}\cdot\mathbf{t}_R = -2cmgR$:
$$ m\left[\ddot{R} - R\dot{\theta}^2 + 2cR\cdot 2c\left(\dot{R}^2 + R\ddot{R}\right)\right] = -2cmgR - T\rho' $$
Substituting $T$ from the equation of $Q$:
$$ \boxed{\left(1 + 4c^2R^2 + \rho'^2\right)\ddot{R} + \left(4c^2R + \rho'\rho''\right)\dot{R}^2 - R\dot{\theta}^2 + 2cgR + g\rho' = 0}, \qquad \boxed{R\ddot{\theta} + 2\dot{R}\dot{\theta} = 0} $$
with $\rho'^2 = \dfrac{(1 + 2c^2R^2)^2}{1 + c^2R^2}$.

#### 3.4 Integration and Answers
##### (e) Condition for the cord to remain in tension
* **Pedagogical Justification:** the cord can only pull, so $T \gt 0$ at all times. From the equation of $Q$:
$$ T = m\left(g + \ddot{z}_Q\right) \gt 0 \iff \ddot{z}_Q = \rho'\ddot{R} + \rho''\dot{R}^2 \gt -g, \qquad \text{i.e.} \quad \frac{1 + 2c^2R^2}{\sqrt{1 + c^2R^2}}\ddot{R} + \frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}}\dot{R}^2 \gt -g $$

##### (g) Two scalar conservation laws (first integrals)
* **Azimuthal integral (first integral of the $\theta$ equation).** From the equation for $\theta$ and $a_\theta = \frac{1}{R}\frac{d}{dt}\left(R^2\dot{\theta}\right)$ (product rule: $\frac{1}{R}\left(2R\dot{R}\dot{\theta} + R^2\ddot{\theta}\right) = R\ddot{\theta} + 2\dot{R}\dot{\theta}$):
$$ \boxed{R^2\dot{\theta} = \text{const} = R(0)^2\,d = \frac{d}{c^2}} \implies \dot{\theta} = \frac{d}{c^2R^2} $$
* **Mechanical energy.** The reaction of the paraboloid does no work ($\mathbf{N}\cdot\mathbf{v}_P = 0$), the tension does the work $-T\rho'\dot{R}$ on $P$ and $+T\rho'\dot{R}$ on $Q$, which cancel (inextensible cord, smooth hole), the guide reaction is perpendicular to $\mathbf{v}_Q$, and gravity is conservative. With $V = mg\left(cR^2 + z_Q\right) = mg\left[cR^2 + \rho - \ell\right]$:
$$ E = \tfrac{1}{2}m\left[\left(1 + 4c^2R^2 + \rho'^2\right)\dot{R}^2 + R^2\dot{\theta}^2\right] + mg\left(cR^2 + \rho\right) - mg\ell = \text{const} $$

##### (h) Equation $f(R) = 0$ for the extreme values of $R$
* **Pedagogical Justification:** at the extremes $\dot{R} = 0$, so only $\tfrac{1}{2}mR^2\dot{\theta}^2$ remains of the kinetic energy, with $R^2\dot{\theta}^2 = d^2/(c^4R^2)$ from the azimuthal integral. The constant $-mg\ell$ cancels in $E - E_0$. At $R(0) = 1/c$: $\rho = \sqrt{2}/c$ and $R^2\dot{\theta}^2 = d^2/c^2$. Per unit mass:
$$ \boxed{f(R) = \frac{d^2}{2c^4R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - \frac{d^2}{2c^2} - \frac{(1 + \sqrt{2})\,g}{c} = 0} $$
* The allowed radii are those with $f(R) \le 0$ (so that $\dot{R}^2 \ge 0$), and $R = 1/c$ is a root.

### Phase 4: Interpretation & Checks
* **Limit $c \to 0$ (flat plane):** $\rho = R$, $\rho' = 1$, $\rho'' = 0$, and the equation for $R$ becomes $2\ddot{R} - R\dot{\theta}^2 + g = 0$, that of two equal particles joined through a hole in a horizontal plane.
* **Bounded precessing motion:** the particle moves between two parallel circles $R_{\min}$ and $R_{\max}$, with the azimuthal angle monotonic ($\dot{\theta} = d/(c^2R^2)$ has the sign of $d$).
* **Dimensional check:** $[c] = \text{m}^{-1}$, $[d] = \text{s}^{-1}$; $[cR^2] = [\rho] = \text{m}$ and $cR$ is dimensionless; every term of $f$ has units m$^2$/s$^2$.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 48 in its solution keys, so the results are verified by independent derivation. Sympy confirms $\rho'$, $\rho''$, the projections of $\mathbf{a}_P$ on $\mathbf{t}_R$ and $\mathbf{e}_\theta$, and numerical integration of the two equations of (f) ($c = d = g = 1$) conserves $E$ to $2\times 10^{-12}$, keeps $T/m \ge 0.303$ and bounds $R$ between $0.482807$ and $1$, the roots of $f$ ($f(0.482807) = 0$ and $f(1) = 0$; $f \lt 0$ between them).

---

## 📌 Problem 50: Double Pendulum

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a double pendulum of two heavy particles $P$ and $Q$ of mass $m$ joined to $O$ and to each other by two rigid massless bars of length $\ell$. The motion is planar (the figure and the angles $\theta$ and $\phi$ describe a plane). The angle $\theta$ is that of the bar $OP$ with the downward vertical and $\phi$ that of the bar $PQ$ with the downward vertical.
* **Constraints:** two particles in the plane have $4$ coordinates; the rigid bars give $|OP| = \ell$ and $|PQ| = \ell$ (holonomic, scleronomic, bilateral). $\text{CDOF} = 4 - 2 = 2$, with $(\theta, \phi)$.
* **Parameters:** $m$, $\ell$, $g$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$, with $\mathbf{i}$ horizontal to the right and $\mathbf{j}$ vertical upward (the horizontal axis is $Ox$).
* **Bar bases** (rotations about the axis perpendicular to the plane; check below):
$$ \mathbf{e}_P = \sin\theta\,\mathbf{i} - \cos\theta\,\mathbf{j}, \quad \mathbf{e}_\theta = \cos\theta\,\mathbf{i} + \sin\theta\,\mathbf{j}, \qquad \mathbf{e}_Q = \sin\phi\,\mathbf{i} - \cos\phi\,\mathbf{j}, \quad \mathbf{e}_\phi = \cos\phi\,\mathbf{i} + \sin\phi\,\mathbf{j} $$
In $\{\mathbf{i}, \mathbf{j}\}$ the matrix with columns $\mathbf{e}_P, \mathbf{e}_\theta$ is $\begin{pmatrix}\sin\theta & \cos\theta\\ -\cos\theta & \sin\theta\end{pmatrix}$, with $\det = \sin^2\theta + \cos^2\theta = 1$ and orthonormal columns ($\sin^2\theta + \cos^2\theta = 1$, $\sin\theta\cos\theta - \cos\theta\sin\theta = 0$), so $RR^T = I$; the same holds with $\phi$ for $\mathbf{e}_Q, \mathbf{e}_\phi$.
where $\mathbf{e}_P$ points from $O$ to $P$ and $\mathbf{e}_Q$ from $P$ to $Q$. Their derivatives are $\dot{\mathbf{e}}_P = \dot{\theta}\,\mathbf{e}_\theta$, $\dot{\mathbf{e}}_\theta = -\dot{\theta}\,\mathbf{e}_P$, and the same with $\phi$.
* **Scalar products needed:** $\mathbf{j}\cdot\mathbf{e}_P = -\cos\theta$, $\mathbf{j}\cdot\mathbf{e}_\theta = \sin\theta$, $\mathbf{j}\cdot\mathbf{e}_Q = -\cos\phi$, $\mathbf{j}\cdot\mathbf{e}_\phi = \sin\phi$, and
$$ \mathbf{e}_P\cdot\mathbf{e}_Q = \cos(\theta - \phi), \quad \mathbf{e}_\theta\cdot\mathbf{e}_Q = \sin(\phi - \theta), \quad \mathbf{e}_\theta\cdot\mathbf{e}_\phi = \cos(\theta - \phi), \quad \mathbf{e}_P\cdot\mathbf{e}_\phi = \sin(\theta - \phi) $$

### Phase 3: Derivation

#### 3.1 Kinematics
##### (a) Position, velocity and acceleration
* **Pedagogical Justification:** the positions are sums of the two bar vectors, $\mathbf{r}_P = \ell\,\mathbf{e}_P$ and $\mathbf{r}_Q = \ell\,\mathbf{e}_P + \ell\,\mathbf{e}_Q$; the derivatives use Poisson's formula:
$$ \mathbf{r}_P = \ell\sin\theta\,\mathbf{i} - \ell\cos\theta\,\mathbf{j}, \qquad \mathbf{r}_Q = \ell\left(\sin\theta + \sin\phi\right)\mathbf{i} - \ell\left(\cos\theta + \cos\phi\right)\mathbf{j} $$
$$ \mathbf{v}_P = \ell\dot{\theta}\,\mathbf{e}_\theta, \qquad \mathbf{v}_Q = \ell\dot{\theta}\,\mathbf{e}_\theta + \ell\dot{\phi}\,\mathbf{e}_\phi, \qquad v_P^2 = \ell^2\dot{\theta}^2, \quad v_Q^2 = \ell^2\left[\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi)\right] $$
$$ \mathbf{a}_P = \ell\left(\ddot{\theta}\,\mathbf{e}_\theta - \dot{\theta}^2\,\mathbf{e}_P\right), \qquad \mathbf{a}_Q = \mathbf{a}_P + \ell\left(\ddot{\phi}\,\mathbf{e}_\phi - \dot{\phi}^2\,\mathbf{e}_Q\right) $$

#### 3.2 Forces
##### (b) Forces on $P$ and $Q$
* The bars are massless and rigid, so each transmits a force along its axis: $T_1$ in $OP$ and $T_2$ in $PQ$ (negative values mean compression).
* **On $P$:** its weight $-mg\,\mathbf{j}$, the pull $-T_1\,\mathbf{e}_P$ of the bar $OP$ and the pull $+T_2\,\mathbf{e}_Q$ of the bar $PQ$. **On $Q$:** its weight $-mg\,\mathbf{j}$ and the pull $-T_2\,\mathbf{e}_Q$ of the bar $PQ$ (action and reaction). **Inertia forces:** none.

#### 3.3 Equations of Motion
##### (c) Equations of motion for $\theta$ and $\phi$
* **Pedagogical Justification:** Newton's second law, $m\mathbf{a}_P = -mg\,\mathbf{j} - T_1\mathbf{e}_P + T_2\mathbf{e}_Q$ and $m\mathbf{a}_Q = -mg\,\mathbf{j} - T_2\mathbf{e}_Q$, gives four scalar equations for the four unknowns $\theta, \phi, T_1, T_2$. The two tensions are removed by choosing the projection directions.
* **Equation for $\phi$.** Project the equation of $Q$ on $\mathbf{e}_\phi$, which is orthogonal to $\mathbf{e}_Q$ and removes $T_2$. With $\mathbf{a}_P\cdot\mathbf{e}_\phi = \ell\left[\ddot{\theta}\cos(\theta - \phi) - \dot{\theta}^2\sin(\theta - \phi)\right]$ and $\ell\left(\ddot{\phi}\,\mathbf{e}_\phi - \dot{\phi}^2\mathbf{e}_Q\right)\cdot\mathbf{e}_\phi = \ell\ddot{\phi}$:
$$ \boxed{\ddot{\phi} + \ddot{\theta}\cos(\theta - \phi) - \dot{\theta}^2\sin(\theta - \phi) + \frac{g}{\ell}\sin\phi = 0} $$
* **Equation for $\theta$.** Add the two equations of motion so that $T_2\,\mathbf{e}_Q$ cancels, and project on $\mathbf{e}_\theta$, which is orthogonal to $\mathbf{e}_P$ and removes $T_1$. The right-hand side is $-2mg\,\mathbf{j}\cdot\mathbf{e}_\theta = -2mg\sin\theta$, and the left-hand side is $m\left(\mathbf{a}_P + \mathbf{a}_Q\right)\cdot\mathbf{e}_\theta$ with $\mathbf{a}_P\cdot\mathbf{e}_\theta = \ell\ddot{\theta}$ and $\mathbf{a}_Q\cdot\mathbf{e}_\theta = \ell\ddot{\theta} + \ell\ddot{\phi}\cos(\theta - \phi) + \ell\dot{\phi}^2\sin(\theta - \phi)$:
$$ \boxed{2\ddot{\theta} + \ddot{\phi}\cos(\theta - \phi) + \dot{\phi}^2\sin(\theta - \phi) + \frac{2g}{\ell}\sin\theta = 0} $$
* **Tensions (afterwards).** Projecting on the bar directions,
$$ T_2 = mg\cos\phi - m\ell\left[\ddot{\theta}\sin(\phi - \theta) - \dot{\theta}^2\cos(\theta - \phi) - \dot{\phi}^2\right], \qquad T_1 = mg\cos\theta + m\ell\dot{\theta}^2 + T_2\cos(\theta - \phi) $$
At rest at $\theta = \phi = 0$: $T_2 = mg$ and $T_1 = 2mg$, the static tensions of the hanging chain.

#### 3.4 Integration and Answers
##### (d) Conservation law
* **Pedagogical Justification:** the bar forces do no net work. Bar $OP$ acts on $P$ with $-T_1\mathbf{e}_P$, whose power is $-T_1\mathbf{e}_P\cdot\ell\dot{\theta}\,\mathbf{e}_\theta = 0$. Bar $PQ$ acts with $+T_2\mathbf{e}_Q$ on $P$ and $-T_2\mathbf{e}_Q$ on $Q$, total power $-T_2\mathbf{e}_Q\cdot(\mathbf{v}_Q - \mathbf{v}_P) = -T_2\mathbf{e}_Q\cdot\ell\dot{\phi}\,\mathbf{e}_\phi = 0$. Gravity is conservative, so the mechanical energy is constant:
$$ E = \tfrac{1}{2}m\ell^2\left[2\dot{\theta}^2 + \dot{\phi}^2 + 2\dot{\theta}\dot{\phi}\cos(\theta - \phi)\right] - mg\ell\left(2\cos\theta + \cos\phi\right) = \text{const} $$

##### (e) Will $Q$ ever cross the $Ox$ axis?
* **Pedagogical Justification:** with $\theta(0) = \phi(0) = \pi/4$ and $\dot{\theta}(0) = \dot{\phi}(0) = 0$, the initial energy is purely potential:
$$ E_0 = -mg\ell\left(2\cos\frac{\pi}{4} + \cos\frac{\pi}{4}\right) = -\frac{3\sqrt{2}}{2}mg\ell \approx -2.121\,mg\ell $$
* $Q$ is on the axis when $y_Q = -\ell\left(\cos\theta + \cos\phi\right) = 0$, i.e. $\cos\phi = -\cos\theta$. There the potential energy is $V = -mg\ell\left(2\cos\theta + \cos\phi\right) = -mg\ell\cos\theta \ge -mg\ell$. Since the kinetic energy is non-negative, $E \ge V$ at any point of the motion, so reaching the axis would require $E_0 \ge -mg\ell$. But $E_0 = -2.121\,mg\ell \lt -mg\ell$.
* **Answer:** $Q$ can **never** cross the $Ox$ axis (it would need a negative kinetic energy).

##### (f) Additional constraint $\phi = 2\theta$: small-angle natural frequency
* **Pedagogical Justification:** with the constraint $\phi = 2\theta$ the system has one degree of freedom. The additional ideal constraint (scleronomic, no friction) does no work, so the energy is still conserved. For small angles, $\dot{\phi} = 2\dot{\theta}$, $\cos(\theta - \phi) = \cos\theta \approx 1$ and $\cos u \approx 1 - u^2/2$:
$$ K = \tfrac{1}{2}m\ell^2\left[2 + 4 + 4\right]\dot{\theta}^2 = 5m\ell^2\dot{\theta}^2, \qquad V = -mg\ell\left[2\left(1 - \tfrac{\theta^2}{2}\right) + \left(1 - 2\theta^2\right)\right] = -3mg\ell + 3mg\ell\theta^2 $$
$$ E = 5m\ell^2\dot{\theta}^2 + 3mg\ell\theta^2 + \text{const} \implies E' = 10m\ell^2\dot{\theta}\ddot{\theta} + 6mg\ell\theta\dot{\theta} = 0 \implies \ddot{\theta} + \frac{3g}{5\ell}\theta = 0 $$
* **Comparison with the hint.** The energy of an ideal oscillator is $\tfrac{1}{2}m_{\text{eq}}\left(\dot{x}^2 + \omega_0^2x^2\right)$; here $\tfrac{1}{2}(10m\ell^2)\left(\dot{\theta}^2 + \dfrac{3g}{5\ell}\theta^2\right)$, so
$$ \boxed{\omega_0 = \sqrt{\frac{3g}{5\ell}}} $$

### Phase 4: Interpretation & Checks
* **Dimensional check:** $[g/\ell] = \text{s}^{-2}$, so $[\omega_0] = \text{s}^{-1}$; $[T_1] = [T_2] = [mg] = \text{N}$.
* **Comparison (not a limit of this system):** for a single pendulum the frequency would be $\sqrt{g/\ell}$; the constrained double pendulum oscillates more slowly ($\omega_0^2 = 0.6\,g/\ell$) because the second mass adds inertia faster than restoring torque.
* **Check against the official key:** `Problems.pdf` has no entry for Problem 50 in its solution keys, so the results are verified by independent derivation. Sympy confirms that the Euler-Lagrange equations of $K - V$ are $m\ell^2$ times the two equations of (c), and gives $K \approx 5m\ell^2\dot{\theta}^2$ and $V''(0) = 6mg\ell$ for the constrained case.
