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

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "Circular orbit on the cone z = R (Problem 18)", "intro": "Data a = 1 m, g = 9.81 m/s². The wire of the archetype is the generator of the cone through P, rising at 45° from the vertex O, and it turns about the vertical k0 with the azimuth θ: the frame slider is θ and its rate is the √(g/a) of the solution. The slider q is the distance OP along the generator, so R and z both equal q/√2. The default, q = a√2 and θ = 0, is the initial point (a, 0, a), and the drag velocity arrow is the initial velocity √(ag) j. The solution proves that R stays equal to a, so turning the frame slider at the default q draws the whole motion, a horizontal circle at height a; the relative velocity and Coriolis arrows are absent because the radial rate is zero. Moving q shows other radii with the same areal constant: Φ(R) is negative there, so they are never reached.", "params": {"wire": "line", "beta": 45, "hgt": 0, "Omega": 3.132092, "qdot": 0, "qmin": 0.141421356, "qmax": 2.545584412, "extent": 1.4, "g": 9.81, "a": 1.0}, "defaults": {"psi": 0, "q": 1.414213562}, "sliders": {"psi": {"label": "Azimuth θ"}, "q": {"label": "Distance OP along the generator (m)", "min": 0.141421356, "max": 2.545584412, "step": 0.0141421356}}, "readouts": [{"label": "Distance to the axis R = q/√2", "expr": "rho", "unit": "m", "digits": 4}, {"label": "Height z = R (constraint of the cone)", "expr": "z", "unit": "m", "digits": 4}, {"label": "Areal constant h = R²θ̇ = a√(ag)", "expr": "a*sqrt(a*g)", "unit": "m²/s", "digits": 4}, {"label": "Rate of the circular orbit θ̇ = √(g/a)", "expr": "sqrt(g/a)", "unit": "rad/s", "digits": 4}, {"label": "Time t = θ/√(g/a) (θ = 0 at the start)", "expr": "psi/sqrt(g/a)", "unit": "s", "digits": 4}, {"label": "Ṙ² = Φ(R) = 3ga/2 − gR − a³g/(2R²) (negative: R not reached)", "expr": "1.5*g*a - g*rho - a^3*g/(2*rho^2)", "unit": "m²/s²", "digits": 4}, {"label": "Φ(R) factored, −g(2R + a)(R − a)²/(2R²)", "expr": "-g*(2*rho + a)*(rho - a)^2/(2*rho^2)", "unit": "m²/s²", "digits": 4}, {"label": "Reaction N/(mg) = (g + Rθ̇²)/(√2 g), θ̇ = h/R²", "expr": "(g + a^3*g/rho^3)/(sqrt(2)*g)", "unit": "", "digits": 4}, {"label": "Small radial oscillation ω_ρ = √(3g/(2a))", "expr": "sqrt(3*g/(2*a))", "unit": "rad/s", "digits": 4}]}

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

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "Particle released along the parallel r = a of the paraboloid a z = r² (Problem 19)", "intro": "The statement gives no numbers: sample values a = 1 m, g = 9.81 m/s² and v0 = 3 m/s, below the circular speed √(2ga), so the radius moves between r* and a. The wire of the archetype is the meridian parabola z = r²/a through P, turning about the vertical k0 with the azimuth θ (frame slider); its rate, 3 rad/s, is the initial rate v0/a. The slider q is the distance r to the axis; the default r = a, θ = 0 is the start, and the drag velocity arrow is the initial velocity v0 along the parallel. The readouts follow the first integrals: at any r they give the azimuthal rate and ṙ² of the motion that starts from the statement, and the reaction there. The frame rate is fixed by the archetype, so the arrows are exact only at the start.", "params": {"wire": "parabola", "k": 1.0, "Omega": 3.0, "qdot": 0, "qmin": 0.3, "qmax": 1.3, "extent": 1.4, "g": 9.81, "a": 1.0, "v0": 3.0}, "defaults": {"psi": 0, "q": 1}, "sliders": {"psi": {"label": "Azimuth θ"}, "q": {"label": "Distance to the axis r (m)", "min": 0.3, "max": 1.3, "step": 0.01}}, "readouts": [{"label": "Height z = r²/a", "expr": "q^2/a", "unit": "m", "digits": 4}, {"label": "Areal constant r²θ̇ = a v0", "expr": "a*v0", "unit": "m²/s", "digits": 4}, {"label": "Azimuthal rate θ̇ = a v0/r²", "expr": "a*v0/q^2", "unit": "rad/s", "digits": 4}, {"label": "Other turning radius r* = v0√(a/(2g))", "expr": "v0*sqrt(a/(2*g))", "unit": "m", "digits": 4}, {"label": "Circular speed √(2ga) (v0 below it: r between r* and a)", "expr": "sqrt(2*g*a)", "unit": "m/s", "digits": 4}, {"label": "ṙ² = 2ga(a² − r²)(r² − r*²)/(r²(a² + 4r²))", "expr": "2*g*a*(a^2 - q^2)*(q^2 - a*v0^2/(2*g))/(q^2*(a^2 + 4*q^2))", "unit": "m²/s²", "digits": 4}, {"label": "Reaction N/(mg) = (ga + 2ṙ² + 2r²θ̇²)/(g√(a² + 4r²))", "expr": "(g*a + 2*(2*g*a*(a^2 - q^2)*(q^2 - a*v0^2/(2*g))/(q^2*(a^2 + 4*q^2))) + 2*q^2*(a*v0/q^2)^2)/(g*sqrt(a^2 + 4*q^2))", "unit": "", "digits": 4}]}

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

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "Particle inside the circumference, fixed or turning about the vertical diameter (Problem 23)", "intro": "The statement gives no numbers: sample values L = 1 m, g = 9.81 m/s², push v0 = 6 m/s (between √(2gL) and √(5gL), so the particle leaves the circumference) and, for the second question, ω = 4 rad/s (above the critical rate √(g/L)). The vertical k0 of the view is the vertical j of the solution, and the hoop turns about it with the frame slider ψ = ωt; at ψ = 0 the plane of the circumference is the plane of the solution's figure. The slider θ is the angle from the lowest point; the default θ = 0 is the start of the statement, and the relative velocity arrow is the push v0. The readouts marked fixed belong to the circumference at rest (ignore the drag velocity and Coriolis arrows for them); those marked turning are the relative equilibria of the second question. Set θ near θ_d to see the reaction of the fixed case vanish, or near θ_e to see the relative acceleration vanish.", "params": {"wire": "hoop", "R": 1.0, "e": 0, "hgt": 0, "Omega": 4.0, "qdot": 6.0, "extent": 1.6, "g": 9.81, "L": 1.0, "v0": 6.0}, "defaults": {"psi": 0, "q": 0}, "sliders": {"psi": {"label": "Angle of the plane ωt"}, "q": {"label": "Angle θ from the lowest point"}}, "readouts": [{"label": "(fixed) v² = v0² − 2gL(1 − cos θ)", "expr": "v0^2 - 2*g*L*(1 - cos(q))", "unit": "m²/s²", "digits": 4}, {"label": "(fixed) Reaction N/m = v0²/L − g(2 − 3 cos θ)", "expr": "v0^2/L - g*(2 - 3*cos(q))", "unit": "m/s²", "digits": 4}, {"label": "(fixed) Separation angle θ_d = arccos((2gL − v0²)/(3gL))", "expr": "deg(acos((2*g*L - v0^2)/(3*g*L)))", "unit": "deg", "digits": 2}, {"label": "(fixed) Speed squared at θ_d, (v0² − 2gL)/3", "expr": "(v0^2 - 2*g*L)/3", "unit": "m²/s²", "digits": 4}, {"label": "Threshold √(2gL): oscillation below it", "expr": "sqrt(2*g*L)", "unit": "m/s", "digits": 4}, {"label": "Threshold √(5gL): complete loops above it", "expr": "sqrt(5*g*L)", "unit": "m/s", "digits": 4}, {"label": "(turning) θ̈ at relative rest, −(g/L − ω² cos θ) sin θ", "expr": "-(g/L - Omega^2*cos(q))*sin(q)", "unit": "rad/s²", "digits": 4}, {"label": "(turning) Reaction at relative rest N/m = Lω² sin²θ + g cos θ", "expr": "L*Omega^2*sin(q)^2 + g*cos(q)", "unit": "m/s²", "digits": 4}, {"label": "(turning) Off-axis equilibrium θ_e = arccos(g/(ω²L))", "expr": "deg(acos(g/(Omega^2*L)))", "unit": "deg", "digits": 2}, {"label": "(turning) Critical rate √(g/L)", "expr": "sqrt(g/L)", "unit": "rad/s", "digits": 4}]}

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

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Particle on the circumference pulled by the spring from A = (0, βa) (Problem 24)", "intro": "The statement gives no numbers: sample values m = 1 kg, a = 1 m, k = 20 N/m, β = 0.3, g = 9.81 m/s² and v0 = 2 m/s (kaβ is below mg, so the bottom is the stable equilibrium). The top view is the vertical plane of the figure: i0 to the right and j0 up, as in the statement, so the pink weight arrow points down the page; the other pink arrow is the spring force −k AP, both scaled by 0.04 m/N. The slider is the angle θ of the figure; the default θ = 0 is the start (a, 0), where e_t is the direction of the initial velocity v0 j. The readouts are the potential, the energy integral of part (c) and the radial reaction at the drawn θ; a negative θ̇² means that the angle is not reached. The speed and accelerations of the archetype below them assume a constant rate v0/a, which is the motion of part (d) only.", "params": {"curve": "circle", "R": 1.0, "rate": 2.0, "accel": 0, "umin": -180, "umax": 180, "extent": 1.1, "m": 1.0, "a": 1.0, "ks": 20.0, "beta": 0.3, "g": 9.81, "v0": 2.0}, "defaults": {"u": 0}, "view": "top", "sliders": {"u": {"label": "Angle θ from the axis Ox"}}, "readouts": [{"label": "(a) V − ½ka²(1 + β²) = (mg − kaβ) a sin θ", "expr": "(m*g - ks*a*beta)*a*sin(u)", "unit": "J", "digits": 4}, {"label": "(a) Potential V = ½ka²(1 + β²) + (mg − kaβ) a sin θ", "expr": "0.5*ks*a^2*(1 + beta^2) + (m*g - ks*a*beta)*a*sin(u)", "unit": "J", "digits": 4}, {"label": "Spring length |AP| = a√(1 + β² − 2β sin θ)", "expr": "a*sqrt(1 + beta^2 - 2*beta*sin(u))", "unit": "m", "digits": 4}, {"label": "(b) mg − kaβ (positive: the bottom θ = −90° is stable)", "expr": "m*g - ks*a*beta", "unit": "N", "digits": 4}, {"label": "(c) θ̇² = v0²/a² − 2(mg − kaβ) sin θ/(ma)", "expr": "(v0^2/a^2 - 2*(m*g - ks*a*beta)*sin(u)/(m*a))", "unit": "rad²/s²", "digits": 4}, {"label": "Radial reaction N_R = ka + (mg − kaβ) sin θ − maθ̇²", "expr": "ks*a + (m*g - ks*a*beta)*sin(u) - m*a*(v0^2/a^2 - 2*(m*g - ks*a*beta)*sin(u)/(m*a))", "unit": "N", "digits": 4}, {"label": "(d) Balanced spring β = mg/(ka)", "expr": "m*g/(ks*a)", "unit": "", "digits": 4}], "vectors": [{"label": "mg", "at": ["x", "y", "z"], "comp": ["0", "-m*g", "0"], "scale": 0.04, "cls": "m3-w"}, {"label": "−k AP", "at": ["x", "y", "z"], "comp": ["-ks*x", "-ks*(y - beta*a)", "0"], "scale": 0.04, "cls": "m3-w"}]}

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

> [!example] Interactive simulator
> sim: {"archetype": "curvilinear-3d", "title": "Cross-section of the tilted cylinder, case (e) (Problem 29)", "intro": "The statement gives no numbers: sample values R = 1 m, α = 30°, g = 9.81 m/s², v0 = 2 m/s and the rate of case (e), ω0² = 4g sin α/R. The top view is the cross-section of the cylinder seen along its axis Oz: i0 of the view is the axis Ox of the section, which points down the slope, as the pink arrow shows (the part g sin α of the weight per unit mass that lies in the section, scaled by 0.1). The slider is the angle θ of the statement, and θ = 0 is the lowest generator; the default θ = 90° is the start, and e_t is the direction of the initial rate ω0. The axial motion z(t) is not drawn: it is uncoupled, and its readouts are listed. The speed of the archetype assumes the constant rate ω0; the true rate is the θ̇ of the first readout.", "params": {"curve": "circle", "R": 1.0, "rate": 4.429447, "accel": 0, "umin": -180, "umax": 180, "extent": 1.1, "g": 9.81, "alph": 0.523598776, "w0": 4.429446918, "v0": 2.0}, "defaults": {"u": 90}, "view": "top", "sliders": {"u": {"label": "Angle θ of the section"}}, "readouts": [{"label": "(b) θ̇² = ω0² + 2g sin α cos θ/R", "expr": "w0^2 + 2*g*sin(alph)*cos(u)/R", "unit": "rad²/s²", "digits": 4}, {"label": "(c) Reaction per unit mass along e_R, N/m = −(Rω0² + 3g sin α cos θ)", "expr": "-(R*w0^2 + 3*g*sin(alph)*cos(u))", "unit": "m/s²", "digits": 4}, {"label": "(e) Least θ̇², 2g sin α/R (at θ = 180°)", "expr": "2*g*sin(alph)/R", "unit": "rad²/s²", "digits": 4}, {"label": "(e) Largest θ̇², 6g sin α/R (at θ = 0)", "expr": "6*g*sin(alph)/R", "unit": "rad²/s²", "digits": 4}, {"label": "(a) Axial deceleration g cos α in z(t) = v0 t − ½ g cos α t²", "expr": "g*cos(alph)", "unit": "m/s²", "digits": 4}, {"label": "(a) Time of the highest axial point v0/(g cos α)", "expr": "v0/(g*cos(alph))", "unit": "s", "digits": 4}, {"label": "(a) Highest axial coordinate v0²/(2g cos α)", "expr": "v0^2/(2*g*cos(alph))", "unit": "m", "digits": 4}, {"label": "(d) Turning angle of case (d), arccos(−1/2)", "expr": "deg(acos(-0.5))", "unit": "deg", "digits": 1}], "vectors": [{"label": "g sin α", "at": ["x", "y", "z"], "comp": ["g*sin(alph)", "0", "0"], "scale": 0.1, "cls": "m3-w"}]}

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

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "P1 on the cone, P2 hanging on the axis (Problem 31)", "intro": "The statement gives no numbers: sample values α = 30°, ℓ = 2.5 m, g = 9.81 m/s². The cone opens downwards from the vertex O; the wire of the archetype is the generator through P1, 60° below the horizontal, turning about the vertical k0 with the azimuth θ (frame slider). The slider q is the string length ξ from O to P1, and the blue arrow from O down the axis ends at P2, at the depth ℓ − ξ. The default ξ = 1 m is a sample circular parallel of part (e), and the frame rate, 2.293 rad/s, is the rate of that parallel, so the drag velocity arrow is the velocity of P1 on it. The readouts use that frame rate for θ̇: moving q away from 1 m shows the radial acceleration and the forces for the same θ̇.", "params": {"wire": "line", "beta": -60, "hgt": 0, "Omega": 2.29285, "qdot": 0, "qmin": 0.1, "qmax": 1.9, "extent": 2, "g": 9.81, "alph": 0.523598776, "ell": 2.5}, "defaults": {"psi": 0, "q": 1}, "sliders": {"psi": {"label": "Azimuth θ"}, "q": {"label": "String length ξ from O to P1 (m)", "min": 0.1, "max": 1.9, "step": 0.01}}, "readouts": [{"label": "Distance of P1 to the axis ξ sin α", "expr": "q*sin(alph)", "unit": "m", "digits": 4}, {"label": "(e) Rate of the circular parallel θ̇ = √(g/(ξ(1 + cos α)))", "expr": "sqrt(g/(q*(1 + cos(alph))))", "unit": "rad/s", "digits": 4}, {"label": "(c) ξ̈ = ½[ξθ̇² sin²α − g(1 − cos α)], θ̇ the frame rate", "expr": "0.5*(q*Omega^2*sin(alph)^2 - g*(1 - cos(alph)))", "unit": "m/s²", "digits": 4}, {"label": "(d) Tension T/(mg) = [g(1 + cos α) + ξθ̇² sin²α]/(2g)", "expr": "(g*(1 + cos(alph)) + q*Omega^2*sin(alph)^2)/(2*g)", "unit": "", "digits": 4}, {"label": "(c) Normal reaction N/(mg) = sin α (g − ξθ̇² cos α)/g", "expr": "sin(alph)*(g - q*Omega^2*cos(alph))/g", "unit": "", "digits": 4}, {"label": "(e) Its value on a parallel, (1 − cos α)/sin α", "expr": "(1 - cos(alph))/sin(alph)", "unit": "", "digits": 4}, {"label": "Depth of P2 below O, ℓ − ξ", "expr": "ell - q", "unit": "m", "digits": 4}, {"label": "(f) Areal constant C1 = ξ²θ̇", "expr": "q^2*Omega", "unit": "m²/s", "digits": 4}], "vectors": [{"label": "P2", "at": ["0", "0", "0"], "comp": ["0", "0", "-(ell - q)"], "scale": 1, "cls": "m3-b1"}]}

---

## Problem 32: Particle with String on Spool

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ hangs from a string of length $l$, equal to $4\pi a$, whose other end is fixed at the point $A$ of a spool of radius $a$ and centre $O$; the spool turns counterclockwise at the constant rate $\omega$, and the string leaves it at the tangency point $B$, at the angle $\phi$ from $Ox$ (Problems.pdf, p. 20). The statement asks for the degrees of freedom, the kinematics of $P$, its forces, whether its mechanical energy is conserved, a closed set of equations and, for a spool at rest, a first integral. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure, origin at the centre of the spool (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along $Ox$ (to the right), $\mathbf j$ along $Oy$ (vertical, **upward**), $\mathbf k$ out of the paper (right-handed) |
| Basis of the tangency point | $\mathcal B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k\}$, $\mathcal B_0$ turned by $\phi$ about $\mathbf k$: $\mathbf i_1$ along $OB$, $\mathbf j_1$ tangent to the spool at $B$ in the counterclockwise sense |
| Coordinate | $\phi$, the angle from $Ox$ to the radius $OB$, counterclockwise positive (statement) |
| Spool | turns about $\mathbf k$ at the constant rate $\omega \ge 0$; the attachment $A$ turns with it, from $\overrightarrow{OA} = -a\,\mathbf i$ at $t = 0$, so its polar angle is $\pi + \omega t$ |
| Hypotheses | $P$ moves in the plane $Oxy$ of the figure (the plane of the cross-section of the spool); the string is massless, inextensible, thin and always tense (statement); the wound part runs from $B$ counterclockwise to $A$ (figure), and $B$ never reaches $A$; $P$ never touches the spool |
| Constraints | plane of motion, $\mathbf r_0^P\cdot\mathbf k = 0$ (holonomic, stationary, bilateral); string: the straight segment $BP$ is tangent to the spool and its length is $l$ minus the wound arc $AB$ (holonomic, **rheonomic** when $\omega \ne 0$ because $A$ moves with time, **unilateral**: the string can only pull) ([Lecture 3, Slide 21]) |
| Degrees of freedom (a) | 3 coordinates of $P$ minus 2 constraint equations: one unknown function, $\phi(t)$. For $\omega \ne 0$ the string constraint contains $t$ explicitly (the lecture adds $t$ as an extra coordinate, [Lecture 3, Slide 21]), but $\omega t$ is prescribed, so $\phi$ is the only coordinate to solve for; for $\omega = 0$ the constraint is stationary and the problem has exactly one degree of freedom ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $a$ [m], $l = 4\pi a$ [m], $\omega$ [rad s$^{-1}$], $g$ [m s$^{-2}$] |
| Applied force | weight $-mg\,\mathbf j$ |
| Constraint force | tension of the string, $T \ge 0$ along $PB$, towards $B$ (Notes.pdf, Sec. 7.5) |

![[attachments/EM-SOL/p32-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p32-rotation-k.svg]]

> [!derivation] Basis of the tangency point: rotation about k
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20
>
> View along $\mathbf k$, which points out of the paper (⊙) because $\mathbf k$ is the cross product of $\mathbf i$ (to the right) and $\mathbf j$ (up): a positive rotation about $\mathbf k$ is counterclockwise, as $\phi$ in the figure. $\mathbf i_1$ is $\mathbf i$ turned by $\phi$: in its right triangle the hypotenuse is 1, the adjacent leg $\cos\phi$ lies along $\mathbf i$ and the opposite leg $\sin\phi$ along $\mathbf j$. $\mathbf j_1$ is $\mathbf j$ turned by $\phi$: the adjacent leg $\cos\phi$ lies along $\mathbf j$ and the opposite leg $\sin\phi$ along minus $\mathbf i$, because the upward vector turned counterclockwise leans to the left (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\phi\,\mathbf i + \sin\phi\,\mathbf j \quad &\text{(right triangle of $\mathbf i_1$: adjacent leg on $\mathbf i$, opposite leg on $\mathbf j$)} \\
> \mathbf j_1 &= -\sin\phi\,\mathbf i + \cos\phi\,\mathbf j \quad &\text{(right triangle of $\mathbf j_1$: opposite leg on $-\mathbf i$, adjacent leg on $\mathbf j$)} \\
> \mathbf i_1\times\mathbf j_1 &= \cos^2\phi\,\mathbf i\times\mathbf j - \sin^2\phi\,\mathbf j\times\mathbf i = \left(\cos^2\phi + \sin^2\phi\right)\mathbf k = \mathbf k \quad &\text{(right-handed: $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\phi\cdot\cos\phi - \left(-\sin\phi\right)\sin\phi\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\phi + \sin^2\phi = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\phi\sin\phi - \sin\phi\cos\phi = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)} \\
> \mathbf j &= \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1 \quad &\text{(second row of the matrix, Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\phi & -\sin\phi & 0 \cr \sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I, \quad \mathbf j = \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf i_1$ points from $O$ to the tangency point $B$ and $\mathbf j_1$ along the spool at $B$; the last relation projects the weight on $\mathcal B_1$.

> [!derivation] Free length of the string
> **Law:** inextensible string: total length equals wound arc plus straight segment
> **Source:** [Lecture 3, Slide 17]; [Lecture 3, Slide 21]; Problems.pdf, p. 20
>
> The wound part goes from $B$, at the polar angle $\phi$, counterclockwise to $A$, at the polar angle $\pi + \omega t$; an arc of a circle of radius $a$ is the radius times the angle it spans. The free length is $s = |BP|$.
>
> $$\begin{aligned}
> \text{arc } BA &= a\left(\pi + \omega t - \phi\right) \quad &\text{(radius times the angle spanned from $B$ to $A$)} \\
> s &= l - a\left(\pi + \omega t - \phi\right) \quad &\text{(constant total length $l$)} \\
> &= 4\pi a - \pi a - a\omega t + a\phi \quad &\text{($l = 4\pi a$; brackets removed)} \\
> &= a\left(3\pi - \omega t + \phi\right) \quad &\text{(common factor $a$)}
> \end{aligned}$$
>
> $$\boxed{s(t) = a\left(3\pi - \omega t + \phi\right), \qquad 0 \lt \pi + \omega t - \phi \ (\text{$B$ never reaches $A$})}$$
>
> **Units:** $[a] = [\mathrm{L}]$; $[\omega t] = [\phi] = [1]$, so $[s] = [\mathrm{L}]$
> **Meaning:** turning the spool counterclockwise winds the string ($s$ decreases with $t$), while a larger $\phi$ unwinds it; with $\omega = 0$ the free length depends only on $\phi$.

> [!derivation] Position vector of the particle
> **Law:** position vector as a sum of partial vectors; tangency of the free segment
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Sec. 7.4; Problems.pdf, p. 20
>
> $\overrightarrow{OB}$ has length $a$ along $\mathbf i_1$. The free segment is tangent to the spool at $B$ (right angle at $B$ in the figure), so it is along plus or minus $\mathbf j_1$; the wound part continues from $B$ in the sense of plus $\mathbf j_1$ (counterclockwise, towards $A$), so the free part leaves $B$ along minus $\mathbf j_1$, down and to the right in the figure. Because $BP$ is perpendicular to $OB$, which makes the angle $\phi$ with the horizontal, $BP$ makes the angle $\phi$ with the downward vertical: in the right triangle of $BP$ the hypotenuse is $s$, the vertical leg $s\cos\phi$ (adjacent to $\phi$, downwards) and the horizontal leg $s\sin\phi$ (opposite to $\phi$, to the right).
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OB} + \overrightarrow{BP} \quad &\text{(sum of partial vectors)} \\
> &= a\,\mathbf i_1 - s\,\mathbf j_1 \quad &\text{(radius along $\mathbf i_1$; free segment along $-\mathbf j_1$)} \\
> &= a\left(\cos\phi\,\mathbf i + \sin\phi\,\mathbf j\right) - s\left(-\sin\phi\,\mathbf i + \cos\phi\,\mathbf j\right) \quad &\text{($\mathcal B_1$ in $\mathcal B_0$)} \\
> &= \left(a\cos\phi + s\sin\phi\right)\mathbf i + \left(a\sin\phi - s\cos\phi\right)\mathbf j \quad &\text{(components grouped)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf i_1 - a\left(3\pi - \omega t + \phi\right)\mathbf j_1, \qquad y_P = a\sin\phi - a\left(3\pi - \omega t + \phi\right)\cos\phi}$$
>
> **Units:** $[\mathrm{L}]$ in every term
> **Meaning:** $P$ lies on the involute of the spool traced by the end of the string; the horizontal leg $s\sin\phi$ and the vertical leg $s\cos\phi$ of the free segment are the dashed projections of the figure.

### Kinematics

> [!derivation] Derivatives of the basis of the tangency point
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\phi\,\mathbf k \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf k$ with the angle $\phi$)} \\
> \mathbf k\times\mathbf i_1 &= \cos\phi\,\mathbf j - \sin\phi\,\mathbf i = \mathbf j_1 \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf k\times\mathbf j_1 &= -\sin\phi\,\mathbf j - \cos\phi\,\mathbf i = -\mathbf i_1 \quad &\text{(same products)} \\
> \dot{\mathbf i}_1 &= \boldsymbol\omega_{10}\times\mathbf i_1 = \dot\phi\,\mathbf j_1 \quad &\text{(Eq. 1.62)} \\
> \dot{\mathbf j}_1 &= \boldsymbol\omega_{10}\times\mathbf j_1 = -\dot\phi\,\mathbf i_1 \quad &\text{(Eq. 1.62)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_1 = \dot\phi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = -\dot\phi\,\mathbf i_1}$$
>
> **Units:** $[\dot\phi] = [\mathrm{T^{-1}}]$
> **Meaning:** the basis follows the tangency point $B$, not the spool: it turns with $\dot\phi$, whatever $\omega$ is.

> [!derivation] Rate of change of the free length
> **Law:** chain rule on the free length; the spool rate is constant
> **Source:** Notes.pdf, Eq. 2.3; Problems.pdf, p. 20
>
> $$\begin{aligned}
> \dot s &= \frac{d}{dt}\left[a\left(3\pi - \omega t + \phi\right)\right] = a\left(0 - \omega + \dot\phi\right) \quad &\text{($a$, $\pi$ and $\omega$ constant; chain rule on $\phi(t)$)} \\
> \ddot s &= a\left(\ddot\phi - 0\right) = a\ddot\phi \quad &\text{(derivative of $\dot s$; $\omega$ constant)}
> \end{aligned}$$
>
> $$\boxed{\dot s = a\left(\dot\phi - \omega\right), \qquad \ddot s = a\ddot\phi}$$
>
> **Units:** $[a\dot\phi] = [a\omega] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the free length grows when $B$ advances counterclockwise faster than the attachment $A$.

> [!derivation] (b) Velocity and acceleration of the particle
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \mathbf v_0^P &= a\,\dot{\mathbf i}_1 - \dot s\,\mathbf j_1 - s\,\dot{\mathbf j}_1 \quad &\text{(product rule on $s\,\mathbf j_1$; $a$ constant)} \\
> &= a\dot\phi\,\mathbf j_1 - a\left(\dot\phi - \omega\right)\mathbf j_1 + s\dot\phi\,\mathbf i_1 \quad &\text{(derivatives of $\mathbf i_1$, $\mathbf j_1$ and $s$)} \\
> &= s\dot\phi\,\mathbf i_1 + a\omega\,\mathbf j_1 \quad &\text{(the terms in $a\dot\phi\,\mathbf j_1$ cancel)} \\
> \mathbf a_0^P &= \dot s\dot\phi\,\mathbf i_1 + s\ddot\phi\,\mathbf i_1 + s\dot\phi\,\dot{\mathbf i}_1 + a\omega\,\dot{\mathbf j}_1 \quad &\text{(product rule; $a\omega$ constant)} \\
> &= a\left(\dot\phi - \omega\right)\dot\phi\,\mathbf i_1 + s\ddot\phi\,\mathbf i_1 + s\dot\phi^2\,\mathbf j_1 - a\omega\dot\phi\,\mathbf i_1 \quad &\text{(derivatives of $s$, $\mathbf i_1$, $\mathbf j_1$)} \\
> &= \left(s\ddot\phi + a\dot\phi^2 - 2a\omega\dot\phi\right)\mathbf i_1 + s\dot\phi^2\,\mathbf j_1 \quad &\text{(the two terms in $a\omega\dot\phi$ added)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^P = a\,\mathbf i_1 - a\left(3\pi - \omega t + \phi\right)\mathbf j_1 \cr \mathbf v_0^P = a\left(3\pi - \omega t + \phi\right)\dot\phi\,\mathbf i_1 + a\omega\,\mathbf j_1 \cr \mathbf a_0^P = a\left[\left(3\pi - \omega t + \phi\right)\ddot\phi + \dot\phi^2 - 2\omega\dot\phi\right]\mathbf i_1 + a\left(3\pi - \omega t + \phi\right)\dot\phi^2\,\mathbf j_1 \end{array}}$$
>
> **Units:** $[s\dot\phi] = [a\omega] = [\mathrm{L\,T^{-1}}]$; $[s\ddot\phi] = [a\dot\phi^2] = [a\omega\dot\phi] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $P$ turns about the instantaneous tangency point $B$ on a circle of radius $s$ (the term $s\dot\phi\,\mathbf i_1$, perpendicular to the string) while the spool reels the string in at the speed $a\omega$ along $\mathbf j_1$, from $P$ towards $B$.

### Forces and Equations of Motion

The free-body diagram of $P$ shows its weight and the tension of the string, directed from $P$ to $B$. $S_0$ is inertial, so no inertia force acts; $P$ does not touch the spool, which acts only on the string.

![[attachments/EM-SOL/p32-fbd.svg]]

> [!derivation] (c) Forces on the particle
> **Law:** weight; tension of a massless string along the string, pulling (constraint force of unknown magnitude)
> **Source:** Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \mathbf r_0^B - \mathbf r_0^P &= a\,\mathbf i_1 - \left(a\,\mathbf i_1 - s\,\mathbf j_1\right) = s\,\mathbf j_1 \quad &\text{(the string pulls $P$ towards $B$: unit vector $\mathbf j_1$)} \\
> \mathbf T &= T\,\mathbf j_1, \quad T \ge 0 \quad &\text{(tension, magnitude unknown; a string can only pull)} \\
> -mg\,\mathbf j &= -mg\sin\phi\,\mathbf i_1 - mg\cos\phi\,\mathbf j_1 \quad &\text{($\mathbf j$ in $\mathcal B_1$)} \\
> \mathbf F &= -mg\sin\phi\,\mathbf i_1 + \left(T - mg\cos\phi\right)\mathbf j_1 \quad &\text{(sum: weight plus tension)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -mg\,\mathbf j + T\,\mathbf j_1 = -mg\sin\phi\,\mathbf i_1 + \left(T - mg\cos\phi\right)\mathbf j_1, \qquad T \ge 0}$$
>
> **Units:** $[mg] = [T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the tension has no component along $\mathbf i_1$ (perpendicular to the string), so the projection on $\mathbf i_1$ will be free of the unknown $T$.

> [!derivation] (e) Newton's second law: a closed set of equations
> **Law:** Newton's second law in an inertial frame, projected on $\mathcal B_1$; the projection perpendicular to the string is free of the tension
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\,\mathbf j + T\,\mathbf j_1 \quad &\text{(all the forces; unknowns $\phi$ and $T$)} \\
> \mathbf i_1:\ m\left(s\ddot\phi + a\dot\phi^2 - 2a\omega\dot\phi\right) &= -mg\sin\phi \quad &\text{(dot product with $\mathbf i_1$; no tension)} \\
> \mathbf j_1:\ ms\dot\phi^2 &= -mg\cos\phi + T \quad &\text{(dot product with $\mathbf j_1$)} \\
> a\left[\left(3\pi - \omega t + \phi\right)\ddot\phi - 2\omega\dot\phi + \dot\phi^2\right] &= -g\sin\phi \quad &\text{(first projection divided by $m$; $s$ substituted)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} a\left[\left(3\pi - \omega t + \phi\right)\ddot\phi - 2\omega\dot\phi + \dot\phi^2\right] = -g\sin\phi \cr T = ma\left(3\pi - \omega t + \phi\right)\dot\phi^2 + mg\cos\phi \end{array}}$$
>
> **Units:** $[a\ddot\phi] = [a\omega\dot\phi] = [g] = [\mathrm{L\,T^{-2}}]$; $[T] = [ma\dot\phi^2] = [mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two scalar equations for the two unknowns $\phi(t)$ and $T(t)$ (the third projection, on $\mathbf k$, is identically zero for planar motion): the first contains only $\phi$ and gives the motion, with a coefficient that depends explicitly on $t$; the second gives the tension afterwards, which must stay positive for the string to be tense.

> [!derivation] (d) Power of the tension and the mechanical energy of P
> **Law:** theorem of kinetic energy (power of the forces); potential of the weight; power of a time-dependent constraint
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 16]; [Lecture 3, Slide 21]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P\right) &= m\,\mathbf a_0^P\cdot\mathbf v_0^P = \mathbf F\cdot\mathbf v_0^P \quad &\text{(product rule; Newton's second law)} \\
> -mg\,\mathbf j\cdot\mathbf v_0^P &= -mg\,\dot y_P = -\frac{d}{dt}\left(mg\,y_P\right) \quad &\text{(the weight derives from the potential $mg\,y_P$)} \\
> T\,\mathbf j_1\cdot\mathbf v_0^P &= T\,\mathbf j_1\cdot\left(s\dot\phi\,\mathbf i_1 + a\omega\,\mathbf j_1\right) = Ta\omega \quad &\text{(power of the tension; $\mathbf j_1\cdot\mathbf i_1 = 0$)} \\
> \frac{d}{dt}\left(\tfrac12 m\,|\mathbf v_0^P|^2 + mg\,y_P\right) &= Ta\omega \quad &\text{(the two powers moved to their sides)} \\
> |\mathbf v_0^P|^2 &= s^2\dot\phi^2 + a^2\omega^2 \quad &\text{(orthonormal $\mathcal B_1$)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12 m\left(s^2\dot\phi^2 + a^2\omega^2\right) + mg\left(a\sin\phi - s\cos\phi\right), \qquad \dot E = Ta\omega \gt 0 \ \text{for } \omega \gt 0: \ E \ \text{not conserved}}$$
>
> **Units:** $[E] = [\mathrm{M\,L^2\,T^{-2}}]$; $[Ta\omega] = [\mathrm{M\,L\,T^{-2}}][\mathrm{L}][\mathrm{T^{-1}}] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** the string constraint depends explicitly on time, so the velocity of $P$ is not orthogonal to the tension: the spool, driven at constant rate by its motor, reels $P$ in and works on it at the rate $Ta\omega$; since the string is tense, the mechanical energy of $P$ grows. It is conserved only for $\omega = 0$.

### Answers and Checks

#### (f) Spool at rest

With the spool at rest (zero $\omega$) the attachment $A$ stays at $-a\,\mathbf i$, the string constraint becomes stationary and the free length $a(3\pi + \phi)$ depends on $\phi$ alone. Part (a) becomes exactly one degree of freedom, the velocity of part (b) loses its term along $\mathbf j_1$, and the power of the tension of part (d) vanishes.

> [!derivation] First integral of the motion for a spool at rest
> **Law:** the equation of motion multiplied by a suitable factor is an exact derivative (product and chain rules); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 16]; Problems.pdf, p. 75
>
> $$\begin{aligned}
> a\left[\left(3\pi + \phi\right)\ddot\phi + \dot\phi^2\right] + g\sin\phi &= 0 \quad &\text{(equation of motion with $\omega = 0$)} \\
> a^2\left(3\pi + \phi\right)^2\dot\phi\ddot\phi + a^2\left(3\pi + \phi\right)\dot\phi^3 + ga\left(3\pi + \phi\right)\sin\phi\,\dot\phi &= 0 \quad &\text{(times $a\left(3\pi + \phi\right)\dot\phi$)} \\
> \frac{d}{dt}\left[\tfrac12 a^2\left(3\pi + \phi\right)^2\dot\phi^2\right] &= a^2\left(3\pi + \phi\right)\dot\phi\cdot\dot\phi^2 + a^2\left(3\pi + \phi\right)^2\dot\phi\ddot\phi \quad &\text{(product rule; chain rule on $\left(3\pi + \phi\right)^2$)} \\
> \frac{d}{dt}\left[a\sin\phi - a\left(3\pi + \phi\right)\cos\phi\right] &= a\cos\phi\,\dot\phi - a\dot\phi\cos\phi + a\left(3\pi + \phi\right)\sin\phi\,\dot\phi \quad &\text{(chain and product rules)} \\
> &= a\left(3\pi + \phi\right)\sin\phi\,\dot\phi \quad &\text{(the terms in $a\cos\phi\,\dot\phi$ cancel)} \\
> \frac{d}{dt}\left[\tfrac12 a^2\left(3\pi + \phi\right)^2\dot\phi^2 + g\left(a\sin\phi - a\left(3\pi + \phi\right)\cos\phi\right)\right] &= 0 \quad &\text{(the second line is this sum of derivatives)} \\
> \left[\tfrac12 a^2\left(3\pi + \phi\right)^2\dot\phi^2 + ga\left(\sin\phi - \left(3\pi + \phi\right)\cos\phi\right)\right]_0^t &= 0 \quad &\text{(Barrow's rule between $0$ and $t$)} \\
> \tfrac12 m a^2\left(3\pi + \phi\right)^2\dot\phi^2 + mga\left[\sin\phi - \left(3\pi + \phi\right)\cos\phi\right] &= E \quad &\text{(times $m$; Barrow's rule gives a constant)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12 m\left[a\left(3\pi + \phi\right)\right]^2\dot\phi^2 + mga\left[\sin\phi - \left(3\pi + \phi\right)\cos\phi\right] = E = \text{const}}$$
>
> **Units:** $[m a^2\dot\phi^2] = [mga] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the mechanical energy of part (d) with $\omega = 0$: kinetic energy of the circular motion about $B$ plus the potential of the weight, with the height $y_P$ of the position box. It contains $\phi$ and its rate only, and with the initial data it reduces the motion to a quadrature.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | $\omega = 0$: 1 degree of freedom ($\phi$). $\omega \ne 0$: one unknown coordinate $\phi(t)$, plus time as the extra coordinate of a rheonomic constraint (+1 CDOF, [Lecture 3, Slide 21]); $\omega t$ is prescribed |
| (b) Kinematics | $\mathbf r_0^P = a\,\mathbf i_1 - a(3\pi - \omega t + \phi)\,\mathbf j_1$; $\mathbf v_0^P = a(3\pi - \omega t + \phi)\dot\phi\,\mathbf i_1 + a\omega\,\mathbf j_1$; $\mathbf a_0^P = a[(3\pi - \omega t + \phi)\ddot\phi + \dot\phi^2 - 2\omega\dot\phi]\,\mathbf i_1 + a(3\pi - \omega t + \phi)\dot\phi^2\,\mathbf j_1$, with $\mathbf i_1 = \cos\phi\,\mathbf i + \sin\phi\,\mathbf j$, $\mathbf j_1 = -\sin\phi\,\mathbf i + \cos\phi\,\mathbf j$ |
| (c) Forces | weight $-mg\,\mathbf j = -mg(\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1)$; tension $T\,\mathbf j_1$ towards $B$, $T \ge 0$ |
| (d) Energy | not conserved for $\omega \ne 0$: $\dot E = Ta\omega$ (power of the tension of the moving spool) |
| (e) Closed set | $a[(3\pi - \omega t + \phi)\ddot\phi - 2\omega\dot\phi + \dot\phi^2] = -g\sin\phi$; $T = ma(3\pi - \omega t + \phi)\dot\phi^2 + mg\cos\phi$ |
| (f) Spool at rest | $\frac12 m[a(3\pi + \phi)]^2\dot\phi^2 + mga[\sin\phi - (3\pi + \phi)\cos\phi] = E$ |

**Check against the official key:** Problems.pdf, p. 75, item 32, prints the two projections of Newton's second law along $\mathbf i_1$ and $\mathbf j_1$ exactly as in the box of part (e) (the same equation for $\phi$ and the same equation for the tension $T$), states that the mechanical energy is conserved only for a spool at rest, and prints the same first integral as the box of part (f): **match**, term by term.

> [!derivation] Limiting case: tangency point held fixed
> **Law:** the velocity of the kinematics box with a constant angle
> **Source:** Notes.pdf, Eq. 2.3
>
> If $\phi$ stays constant, $B$ does not move and the spool simply reels the straight string in.
>
> $$\begin{aligned}
> \dot\phi &= 0 \quad &\text{(fixed tangency point)} \\
> \mathbf v_0^P &= 0\cdot\mathbf i_1 + a\omega\,\mathbf j_1 = a\omega\,\mathbf j_1 \quad &\text{(velocity of part (b))} \\
> \dot s &= a\left(0 - \omega\right) = -a\omega \quad &\text{(rate of the free length)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi = 0:\ \mathbf v_0^P = a\omega\,\mathbf j_1, \quad |\mathbf v_0^P| = -\dot s = a\omega}$$
>
> **Units:** $[a\omega] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** $P$ moves straight towards $B$ at the peripheral speed of the spool, exactly the rate at which the string shortens: the kinematics is consistent with the inextensible string.

> [!derivation] Limiting case: small oscillations of the spool at rest
> **Law:** equilibrium of the equation of motion and its linearisation about it
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 5.6; [Lecture 6, Slide 15]
>
> With $\omega = 0$, the state with constant zero $\phi$ satisfies the equation of motion (the sine vanishes): $B$ is at $(a, 0)$ and $P$ hangs vertically below it at the depth $3\pi a$. For a small $\phi$ the sine is replaced by its argument and the products of $\phi$ with its rate or acceleration, of second order, are dropped.
>
> $$\begin{aligned}
> a\left[\left(3\pi + 0\right)\cdot 0 + 0\right] + g\sin 0 &= 0 \quad &\text{(constant zero $\phi$ is an equilibrium)} \\
> T &= 0 + mg\cos 0 = mg \quad &\text{(tension at the equilibrium)} \\
> 3\pi a\,\ddot\phi + a\phi\ddot\phi + a\dot\phi^2 + g\sin\phi &= 0 \quad &\text{(equation of motion with $\omega = 0$, bracket expanded)} \\
> 3\pi a\,\ddot\phi + g\phi &= 0 \quad &\text{($\sin\phi \simeq \phi$; second-order terms dropped)} \\
> \ddot\phi + \frac{g}{3\pi a}\,\phi &= 0 \quad &\text{(divided by $3\pi a$: the form of Eq. 5.6)}
> \end{aligned}$$
>
> $$\boxed{\omega = 0,\ |\phi| \ll 1:\quad T = mg, \qquad \omega_n = \sqrt{\frac{g}{3\pi a}}}$$
>
> **Units:** $[g/(3\pi a)] = [\mathrm{L\,T^{-2}}]/[\mathrm{L}] = [\mathrm{T^{-2}}]$, so $[\omega_n] = [\mathrm{T^{-1}}]$
> **Meaning:** near the vertical the particle swings like a simple pendulum whose length is the free length $3\pi a$ of the string, hanging from the tangency point; the string carries exactly the weight at rest.

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "String unwinding from the spool, tangency point B at the angle φ (Problem 32)", "intro": "Sample values a = 0.3 m, g = 9.81 m/s², spool rate ω = 0.5 rad/s, drawn at the instant t = 0 with φ̇ = 0 (the statement gives no initial state). The top view is the plane of the figure, i0 to the right and j0 up. The frame slider is the angle φ of B (default 45°, as in the figure), and the blue basis i1, j1 is the basis B1 of the solution, i1 along OB. The wire of the archetype is the tangent to the spool at B, at the distance a from O, and the blue arrow B marks the tangency point; the spool itself is not drawn. The slider q is the coordinate of P along j1, minus the free length s: it must equal −s of the first readout (the default does), and then the dot P is the particle, at the end of the straight string. The relative velocity arrow is aω along j1, the spool reeling the string in at fixed φ; the pink arrow is the weight per unit mass, scaled by 0.1. A is at the angle π + ωt, so B must stay below 180°.", "params": {"wire": "chord", "d": 0.3, "Omega": 0, "qdot": 0.15, "qmin": -4, "qmax": 0, "extent": 3.3, "a": 0.3, "g": 9.81, "w": 0.5, "tt": 0, "phid": 0}, "defaults": {"psi": 45, "q": -3.063053}, "view": "top", "sliders": {"psi": {"label": "Angle φ of the tangency point B", "min": -90, "max": 179}, "q": {"label": "Coordinate of P along j1, minus s (m)", "min": -4, "max": 0, "step": 0.0001}}, "readouts": [{"label": "Free length s = a(3π − ωt + φ)", "expr": "(a*(3*pi - w*tt + psi))", "unit": "m", "digits": 4}, {"label": "Free length drawn, −q (equal to s for the string)", "expr": "-q", "unit": "m", "digits": 4}, {"label": "x_P = a cos φ + s sin φ", "expr": "a*cos(psi) + (a*(3*pi - w*tt + psi))*sin(psi)", "unit": "m", "digits": 4}, {"label": "x of the dot P, read from the drawing", "expr": "x", "unit": "m", "digits": 4}, {"label": "y_P = a sin φ − s cos φ", "expr": "a*sin(psi) - (a*(3*pi - w*tt + psi))*cos(psi)", "unit": "m", "digits": 4}, {"label": "y of the dot P, read from the drawing", "expr": "y", "unit": "m", "digits": 4}, {"label": "(b) Speed |v| = √(s²φ̇² + a²ω²)", "expr": "sqrt((a*(3*pi - w*tt + psi))^2*phid^2 + a^2*w^2)", "unit": "m/s", "digits": 4}, {"label": "(e) Tension per unit mass T/m = sφ̇² + g cos φ", "expr": "(a*(3*pi - w*tt + psi))*phid^2 + g*cos(psi)", "unit": "m/s²", "digits": 4}, {"label": "(e) φ̈ = (2ωφ̇ − φ̇² − (g/a) sin φ)/(3π − ωt + φ)", "expr": "(2*w*phid - phid^2 - (g/a)*sin(psi))/(3*pi - w*tt + psi)", "unit": "rad/s²", "digits": 4}, {"label": "(d) Power of the tension per unit mass, (T/m) a ω", "expr": "((a*(3*pi - w*tt + psi))*phid^2 + g*cos(psi))*a*w", "unit": "W/kg", "digits": 4}, {"label": "(f) ω = 0: E/m = ½[a(3π + φ)]²φ̇² + ga[sin φ − (3π + φ) cos φ]", "expr": "0.5*(a*(3*pi + psi))^2*phid^2 + g*a*(sin(psi) - (3*pi + psi)*cos(psi))", "unit": "J/kg", "digits": 4}, {"label": "Small oscillation of the spool at rest ω_n = √(g/(3πa))", "expr": "sqrt(g/(3*pi*a))", "unit": "rad/s", "digits": 4}], "vectors": [{"label": "B", "at": ["0", "0", "0"], "comp": ["a*cos(psi)", "a*sin(psi)", "0"], "scale": 1, "cls": "m3-b1"}, {"label": "g", "at": ["x", "y", "0"], "comp": ["0", "-g", "0"], "scale": 0.1, "cls": "m3-w"}]}

---

## Problem 35: String with Two Particles on a Cylinder

### Reference Frames, Bases and Coordinates

Two heavy particles $P$ and $Q$ of mass $m$ hang from the two ends of an inextensible massless string of length $L$ that lies over a smooth fixed cylinder of radius $R$ and centre $O$, touching it between the tangency points $A$ and $B$; a spring of zero natural length and stiffness $k$ joins $P$ and $Q$ (Problems.pdf, p. 23). The statement asks for the degrees of freedom and a set of coordinates, the kinematics, the forces, the mechanical energy of $P$, the symmetric configurations and, for them, the equilibrium and the frequency of small oscillations. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7, with the coordinates of the official key.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure, origin at the centre of the cylinder (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along $Ox$ (to the right), $\mathbf j$ along $Oy$ (vertical, **upward**), $\mathbf k$ along the axis of the cylinder, out of the paper |
| Basis at $A$ | $\mathcal B_1 = \{\mathbf e_A, \mathbf e_\theta, \mathbf k\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k$: $\mathbf e_A$ from $O$ to $A$, $\mathbf e_\theta$ tangent to the cylinder at $A$, counterclockwise |
| Basis at $B$ | $\mathcal B_2 = \{\mathbf e_B, \mathbf e_\psi, \mathbf k\}$, $\mathcal B_0$ turned by $\psi$ about $\mathbf k$: $\mathbf e_B$ from $O$ to $B$, $\mathbf e_\psi$ tangent at $B$, counterclockwise |
| Coordinates (a) | $\theta$, polar angle of $A$ from $Ox$; $\psi$, polar angle of $B$ from $Ox$ (with $\psi \gt \theta$); $\xi$, length of the straight segment $AP$. The length of $BQ$ is the auxiliary quantity $\zeta = L - \xi - R(\psi - \theta)$ |
| Hypotheses | motion in the plane $Oxy$ of the figure; the string is tense, touches the cylinder only along the arc from $A$ to $B$ over the top and slides on it without friction; the particles and the spring never touch the cylinder |
| Constraints | $P$ and $Q$ in the plane (2 equations, holonomic, stationary, bilateral); string: $\xi + R(\psi - \theta) + \zeta = L$, with each straight segment tangent to the cylinder (1 equation joining the two particles, holonomic, stationary, **unilateral**: the string can only pull) ([Lecture 3, Slide 17]; [Lecture 3, Slide 21]) |
| Degrees of freedom (a) | 6 coordinates of two particles minus 3 constraint equations: 3, namely $\theta(t)$, $\psi(t)$, $\xi(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $L$ [m], $R$ [m], $k$ [N m$^{-1}$], $g$ [m s$^{-2}$] |
| Applied forces | weights $-mg\,\mathbf j$ on each particle; spring of zero natural length, $k\overrightarrow{PQ}$ on $P$ and $-k\overrightarrow{PQ}$ on $Q$ (Notes.pdf, Sec. 7.5) |
| Constraint forces | tension $T \ge 0$ of the string, along $PA$ on $P$ and along $QB$ on $Q$; the same magnitude at both ends (massless string on a smooth cylinder, [Lecture 3, Slide 17]); the cylinder acts on the string only |

![[attachments/EM-SOL/p35-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p35-rotations-k.svg]]

> [!derivation] Bases at the tangency points: two rotations about k
> **Law:** elementary rotations about the third axis; change of basis matrices and their checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View along $\mathbf k$, out of the paper (⊙), since $\mathbf k$ is the cross product of $\mathbf i$ (to the right) and $\mathbf j$ (up): positive angles are counterclockwise, as $\theta$ and $\psi$ in the figure. $\mathbf e_A$ is $\mathbf i$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i$, opposite leg $\sin\theta$ along $\mathbf j$. $\mathbf e_\theta$ is $\mathbf j$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j$, opposite leg $\sin\theta$ along minus $\mathbf i$ (the upward vector turned counterclockwise leans to the left: the minus sign). The basis at $B$ is the same construction with the angle $\psi$.
>
> $$\begin{aligned}
> \mathbf e_A &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_A$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(right triangle of $\mathbf e_\theta$: opposite leg on $-\mathbf i$)} \\
> \mathbf e_B &= \cos\psi\,\mathbf i + \sin\psi\,\mathbf j \quad &\text{(same triangles with $\psi$)} \\
> \mathbf e_\psi &= -\sin\psi\,\mathbf i + \cos\psi\,\mathbf j \quad &\text{(same triangles with $\psi$)} \\
> \mathbf e_A\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed; $\mathbf i\times\mathbf j = \mathbf k$, $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta\cos\theta + \sin\theta\sin\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)} \\
> \mathbf j &= \sin\theta\,\mathbf e_A + \cos\theta\,\mathbf e_\theta \quad &\text{(second row of $[{}_0R_1]$, Eq. 1.14)} \\
> \mathbf j &= \sin\psi\,\mathbf e_B + \cos\psi\,\mathbf e_\psi \quad &\text{(second row of $[{}_0R_2]$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad [{}_0R_2] = \begin{pmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det = 1, \quad RR^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** each tangency point carries its own polar basis; the checks of $[{}_0R_2]$ are those of $[{}_0R_1]$ with $\psi$ in place of $\theta$.

> [!derivation] Length of the second straight segment
> **Law:** inextensible string: straight segments plus the wound arc equal the total length
> **Source:** [Lecture 3, Slide 17]; Problems.pdf, p. 23
>
> The string touches the cylinder from $A$, at the polar angle $\theta$, counterclockwise over the top to $B$, at $\psi$; the arc is the radius times the angle it spans.
>
> $$\begin{aligned}
> \text{arc } AB &= R\left(\psi - \theta\right) \quad &\text{(radius times the angle from $A$ to $B$)} \\
> \xi + R\left(\psi - \theta\right) + \zeta &= L \quad &\text{(constant length)} \\
> \zeta &= L - \xi - R\left(\psi - \theta\right) \quad &\text{(solved for the length of $BQ$)}
> \end{aligned}$$
>
> $$\boxed{\zeta = L - \xi - R\left(\psi - \theta\right)}$$
>
> **Units:** $[\mathrm{L}]$ in every term ($\theta$, $\psi$ in radians)
> **Meaning:** the length of $BQ$ is not a fourth coordinate: it follows from the three chosen ones.

> [!derivation] Position vectors of both particles
> **Law:** position vectors as sums of partial vectors; tangency of the straight segments
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Sec. 7.4; Problems.pdf, p. 23
>
> Each straight segment is tangent to the cylinder at its tangency point, so it is perpendicular to the radius there. At $A$ the wound part continues counterclockwise (along $\mathbf e_\theta$), so $AP$ leaves along minus $\mathbf e_\theta$, down and to the right. At $B$ the wound part continues clockwise (along minus $\mathbf e_\psi$), so $BQ$ leaves along $\mathbf e_\psi$, down and to the left. Since $AP$ is perpendicular to $OA$, which makes the angle $\theta$ with the horizontal, $AP$ makes the angle $\theta$ with the downward vertical: in its right triangle the hypotenuse is $\xi$, the vertical leg $\xi\cos\theta$ (adjacent, downwards) and the horizontal leg $\xi\sin\theta$ (opposite, to the right). In the same way $BQ$ makes the angle $\pi - \psi$ with the downward vertical: hypotenuse $\zeta$, horizontal leg $\zeta\sin(\pi - \psi)$ to the left and vertical leg $\zeta\cos(\pi - \psi)$ downwards.
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OA} + \overrightarrow{AP} = R\,\mathbf e_A - \xi\,\mathbf e_\theta \quad &\text{(radius to $A$; segment along $-\mathbf e_\theta$)} \\
> &= \left(R\cos\theta + \xi\sin\theta\right)\mathbf i + \left(R\sin\theta - \xi\cos\theta\right)\mathbf j \quad &\text{($\mathcal B_1$ in $\mathcal B_0$)} \\
> \mathbf r_0^Q &= \overrightarrow{OB} + \overrightarrow{BQ} = R\,\mathbf e_B + \zeta\,\mathbf e_\psi \quad &\text{(radius to $B$; segment along $\mathbf e_\psi$)} \\
> &= \left(R\cos\psi - \zeta\sin\psi\right)\mathbf i + \left(R\sin\psi + \zeta\cos\psi\right)\mathbf j \quad &\text{($\mathcal B_2$ in $\mathcal B_0$)} \\
> \sin\left(\pi - \psi\right) &= \sin\psi, \quad \cos\left(\pi - \psi\right) = -\cos\psi \quad &\text{(supplementary angles: legs $\zeta\sin\psi$ to the left, $-\zeta\cos\psi$ downwards)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_A - \xi\,\mathbf e_\theta, \qquad \mathbf r_0^Q = R\,\mathbf e_B + \left[L - \xi - R\left(\psi - \theta\right)\right]\mathbf e_\psi}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the position of each particle is the tangency point plus the hanging segment; in the figure $\psi$ lies between $\pi/2$ and $\pi$, so the cosine of $\psi$ is negative and the vertical leg of $BQ$ is positive downwards.

### Kinematics

> [!derivation] Derivatives of the two bases
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k, \quad \boldsymbol\omega_{20} = \dot\psi\,\mathbf k \quad &\text{(each basis turns about the fixed $\mathbf k$ with its own angle)} \\
> \dot{\mathbf e}_A &= \dot\theta\,\mathbf k\times\mathbf e_A = \dot\theta\,\mathbf e_\theta \quad &\text{($\mathbf k\times\mathbf e_A = \cos\theta\,\mathbf j - \sin\theta\,\mathbf i$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_A \quad &\text{($\mathbf k\times\mathbf e_\theta = -\sin\theta\,\mathbf j - \cos\theta\,\mathbf i$)} \\
> \dot{\mathbf e}_B &= \dot\psi\,\mathbf e_\psi, \quad \dot{\mathbf e}_\psi = -\dot\psi\,\mathbf e_B \quad &\text{(same products with $\psi$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf e}_A = \dot\theta\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_A, \quad \dot{\mathbf e}_B = \dot\psi\,\mathbf e_\psi, \quad \dot{\mathbf e}_\psi = -\dot\psi\,\mathbf e_B}$$
>
> **Units:** $[\dot\theta] = [\dot\psi] = [\mathrm{T^{-1}}]$
> **Meaning:** the bases follow the tangency points, which slide round the cylinder as the configuration changes.

> [!derivation] (b) Position, velocity and acceleration of P
> **Law:** time derivatives in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \mathbf v_0^P &= R\,\dot{\mathbf e}_A - \dot\xi\,\mathbf e_\theta - \xi\,\dot{\mathbf e}_\theta \quad &\text{(product rule; $R$ constant)} \\
> &= R\dot\theta\,\mathbf e_\theta - \dot\xi\,\mathbf e_\theta + \xi\dot\theta\,\mathbf e_A \quad &\text{(derivatives of the basis)} \\
> &= \xi\dot\theta\,\mathbf e_A + \left(R\dot\theta - \dot\xi\right)\mathbf e_\theta \quad &\text{(grouped)} \\
> \mathbf a_0^P &= \left(\dot\xi\dot\theta + \xi\ddot\theta\right)\mathbf e_A + \xi\dot\theta\,\dot{\mathbf e}_A + \left(R\ddot\theta - \ddot\xi\right)\mathbf e_\theta + \left(R\dot\theta - \dot\xi\right)\dot{\mathbf e}_\theta \quad &\text{(product rule on each term)} \\
> &= \left(\dot\xi\dot\theta + \xi\ddot\theta\right)\mathbf e_A + \xi\dot\theta^2\,\mathbf e_\theta + \left(R\ddot\theta - \ddot\xi\right)\mathbf e_\theta - \left(R\dot\theta - \dot\xi\right)\dot\theta\,\mathbf e_A \quad &\text{(derivatives of the basis)} \\
> &= \left(\xi\ddot\theta + 2\dot\xi\dot\theta - R\dot\theta^2\right)\mathbf e_A + \left(R\ddot\theta - \ddot\xi + \xi\dot\theta^2\right)\mathbf e_\theta \quad &\text{(grouped)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^P = R\,\mathbf e_A - \xi\,\mathbf e_\theta, \quad \mathbf v_0^P = \xi\dot\theta\,\mathbf e_A + \left(R\dot\theta - \dot\xi\right)\mathbf e_\theta \cr \mathbf a_0^P = \left(\xi\ddot\theta + 2\dot\xi\dot\theta - R\dot\theta^2\right)\mathbf e_A + \left(R\ddot\theta - \ddot\xi + \xi\dot\theta^2\right)\mathbf e_\theta \end{array}}$$
>
> **Units:** $[\xi\dot\theta] = [\dot\xi] = [\mathrm{L\,T^{-1}}]$; $[\xi\ddot\theta] = [\dot\xi\dot\theta] = [R\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the component along $\mathbf e_\theta$ (along the string, positive towards $A$) is the speed at which the string is pulled over $A$; the component along $\mathbf e_A$ is the swing of the segment.

> [!derivation] (b) Position, velocity and acceleration of Q
> **Law:** time derivatives in $S_0$; product rule; the length of $BQ$ differentiated with the chain rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \dot\zeta &= -\dot\xi - R\left(\dot\psi - \dot\theta\right) \quad &\text{(derivative of the length of $BQ$; $L$, $R$ constant)} \\
> R\dot\psi + \dot\zeta &= R\dot\theta - \dot\xi \quad &\text{(previous row with $R\dot\psi$ moved to the left: the rate along each segment is the same)} \\
> R\ddot\psi + \ddot\zeta &= R\ddot\theta - \ddot\xi \quad &\text{(time derivative of the previous row)} \\
> \mathbf v_0^Q &= R\,\dot{\mathbf e}_B + \dot\zeta\,\mathbf e_\psi + \zeta\,\dot{\mathbf e}_\psi \quad &\text{(product rule on $\zeta\,\mathbf e_\psi$; $R$ constant)} \\
> &= R\dot\psi\,\mathbf e_\psi + \dot\zeta\,\mathbf e_\psi - \zeta\dot\psi\,\mathbf e_B \quad &\text{(derivatives of $\mathbf e_B$ and $\mathbf e_\psi$)} \\
> &= -\zeta\dot\psi\,\mathbf e_B + \left(R\dot\theta - \dot\xi\right)\mathbf e_\psi \quad &\text{(grouped; $R\dot\psi + \dot\zeta = R\dot\theta - \dot\xi$)} \\
> \mathbf a_0^Q &= -\left(\dot\zeta\dot\psi + \zeta\ddot\psi\right)\mathbf e_B - \zeta\dot\psi\,\dot{\mathbf e}_B + \left(R\ddot\theta - \ddot\xi\right)\mathbf e_\psi + \left(R\dot\theta - \dot\xi\right)\dot{\mathbf e}_\psi \quad &\text{(product rule on each term)} \\
> &= -\left(\dot\zeta\dot\psi + \zeta\ddot\psi\right)\mathbf e_B - \zeta\dot\psi^2\,\mathbf e_\psi + \left(R\ddot\theta - \ddot\xi\right)\mathbf e_\psi - \left(R\dot\theta - \dot\xi\right)\dot\psi\,\mathbf e_B \quad &\text{(derivatives of $\mathbf e_B$ and $\mathbf e_\psi$)} \\
> &= -\left(\dot\zeta\dot\psi + \zeta\ddot\psi\right)\mathbf e_B - \zeta\dot\psi^2\,\mathbf e_\psi + \left(R\ddot\theta - \ddot\xi\right)\mathbf e_\psi - \left(R\dot\psi + \dot\zeta\right)\dot\psi\,\mathbf e_B \quad &\text{($R\dot\theta - \dot\xi = R\dot\psi + \dot\zeta$)} \\
> &= -\left(\zeta\ddot\psi + 2\dot\zeta\dot\psi + R\dot\psi^2\right)\mathbf e_B + \left(R\ddot\theta - \ddot\xi - \zeta\dot\psi^2\right)\mathbf e_\psi \quad &\text{(grouped)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^Q = R\,\mathbf e_B + \zeta\,\mathbf e_\psi, \quad \mathbf v_0^Q = -\zeta\dot\psi\,\mathbf e_B + \left(R\dot\theta - \dot\xi\right)\mathbf e_\psi \cr \mathbf a_0^Q = -\left(\zeta\ddot\psi + 2\dot\zeta\dot\psi + R\dot\psi^2\right)\mathbf e_B + \left(R\ddot\theta - \ddot\xi - \zeta\dot\psi^2\right)\mathbf e_\psi \cr \zeta = L - \xi - R\left(\psi - \theta\right), \quad \dot\zeta = R\dot\theta - R\dot\psi - \dot\xi \end{array}}$$
>
> **Units:** $[\zeta\dot\psi] = [R\dot\theta] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $Q$ moves along its segment ($\mathbf e_\psi$, away from $B$) at the same rate at which $P$ moves towards $A$: whatever the string gains on one side it loses on the other.

### Forces and Equations of Motion

The free-body diagrams show on each particle its weight, the tension towards its tangency point and the force of the spring towards the other particle. $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p35-fbd.svg]]

> [!derivation] (c) Forces on both particles
> **Law:** weight; spring of zero natural length; tension of a massless string, equal at both ends on a smooth support
> **Source:** Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]; Problems.pdf, p. 75
>
> $$\begin{aligned}
> \mathbf r_0^A - \mathbf r_0^P &= \xi\,\mathbf e_\theta, \quad \mathbf r_0^B - \mathbf r_0^Q = -\zeta\,\mathbf e_\psi \quad &\text{(directions from each particle to its tangency point)} \\
> \overrightarrow{PQ} &= \mathbf r_0^Q - \mathbf r_0^P = R\left(\mathbf e_B - \mathbf e_A\right) + \zeta\,\mathbf e_\psi + \xi\,\mathbf e_\theta \quad &\text{(difference of the position vectors)} \\
> \mathbf F_{S,P} &= k\overrightarrow{PQ} = kR\left(\mathbf e_B - \mathbf e_A\right) + k\left[L - \xi - R\left(\psi - \theta\right)\right]\mathbf e_\psi + k\xi\,\mathbf e_\theta \quad &\text{(zero natural length: the force is $k$ times the extension vector)} \\
> \mathbf F_{S,Q} &= -\mathbf F_{S,P} \quad &\text{(action and reaction of the massless spring)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf F^P = -mg\,\mathbf j + T\,\mathbf e_\theta + k\overrightarrow{PQ} \cr \mathbf F^Q = -mg\,\mathbf j - T\,\mathbf e_\psi - k\overrightarrow{PQ} \cr k\overrightarrow{PQ} = kR\left(\mathbf e_B - \mathbf e_A\right) + k\left[L - \xi - R\left(\psi - \theta\right)\right]\mathbf e_\psi + k\xi\,\mathbf e_\theta, \quad T \ge 0 \end{array}}$$
>
> **Units:** $[mg] = [T] = [kR] = [k\xi] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the tension is the only reaction on the particles, a single unknown $T(t)$ shared by both, since the smooth cylinder acts only on the string; the spring pair is equal and opposite.

> [!derivation] Newton's second law for both particles
> **Law:** Newton's second law in an inertial frame with all the forces, each particle projected on its own basis
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> The weight is projected with the rows of the matrices; the spring with the dot products of $\overrightarrow{PQ}$, written $\overrightarrow{PQ}\cdot\mathbf e_A$ and so on.
>
> $$\begin{aligned}
> P,\ \mathbf e_A:\ m\left(\xi\ddot\theta + 2\dot\xi\dot\theta - R\dot\theta^2\right) &= -mg\sin\theta + k\overrightarrow{PQ}\cdot\mathbf e_A \quad &\text{(no tension: $\mathbf e_\theta\cdot\mathbf e_A = 0$)} \\
> P,\ \mathbf e_\theta:\ m\left(R\ddot\theta - \ddot\xi + \xi\dot\theta^2\right) &= -mg\cos\theta + T + k\overrightarrow{PQ}\cdot\mathbf e_\theta \quad &\text{(along $PA$)} \\
> Q,\ \mathbf e_B:\ -m\left(\zeta\ddot\psi + 2\dot\zeta\dot\psi + R\dot\psi^2\right) &= -mg\sin\psi - k\overrightarrow{PQ}\cdot\mathbf e_B \quad &\text{(no tension: $\mathbf e_\psi\cdot\mathbf e_B = 0$)} \\
> Q,\ \mathbf e_\psi:\ m\left(R\ddot\theta - \ddot\xi - \zeta\dot\psi^2\right) &= -mg\cos\psi - T - k\overrightarrow{PQ}\cdot\mathbf e_\psi \quad &\text{(along $BQ$)} \\
> m\left(2R\ddot\theta - 2\ddot\xi + \xi\dot\theta^2 - \zeta\dot\psi^2\right) &= -mg\left(\cos\theta + \cos\psi\right) + k\overrightarrow{PQ}\cdot\left(\mathbf e_\theta - \mathbf e_\psi\right) \quad &\text{(sum of the two string projections: $T$ eliminated)}
> \end{aligned}$$
>
> $$\boxed{\text{3 equations free of } T \text{ (the } \mathbf e_A \text{, } \mathbf e_B \text{ projections and their string sum) for } \theta, \psi, \xi; \quad T \text{ from the } \mathbf e_\theta \text{ projection}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** four scalar equations for the four unknowns $\theta$, $\psi$, $\xi$ and $T$; the motion decouples from the tension, which is computed afterwards and must stay positive.

> [!derivation] (d) Work of the forces on P and the energy of the pair
> **Law:** power of a force; the tension transfers energy between the particles; potential of the weights and of the spring
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> T\,\mathbf e_\theta\cdot\mathbf v_0^P &= T\left(R\dot\theta - \dot\xi\right) \quad &\text{(power of the tension on $P$: not zero in general)} \\
> -T\,\mathbf e_\psi\cdot\mathbf v_0^Q &= -T\left(R\dot\theta - \dot\xi\right) \quad &\text{(power of the tension on $Q$)} \\
> k\overrightarrow{PQ}\cdot\mathbf v_0^P - k\overrightarrow{PQ}\cdot\mathbf v_0^Q &= -k\overrightarrow{PQ}\cdot\frac{d\overrightarrow{PQ}}{dt} = -\frac{d}{dt}\left(\tfrac12 k\left|\overrightarrow{PQ}\right|^2\right) \quad &\text{(power of the spring on both; chain rule)} \\
> -mg\,\mathbf j\cdot\left(\mathbf v_0^P + \mathbf v_0^Q\right) &= -\frac{d}{dt}\left[mg\left(y_P + y_Q\right)\right] \quad &\text{(power of the weights)} \\
> \frac{d}{dt}\left[\tfrac12 m\left(|\mathbf v_0^P|^2 + |\mathbf v_0^Q|^2\right)\right] &= -\frac{d}{dt}\left[mg\left(y_P + y_Q\right) + \tfrac12 k\left|\overrightarrow{PQ}\right|^2\right] \quad &\text{(sum of all powers; the two tension powers cancel)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} E_P \ \text{not conserved: } \dot E_P = T\left(R\dot\theta - \dot\xi\right) + \text{power of the spring, which depends on the motion of } Q \cr E = \tfrac12 m\left(|\mathbf v_0^P|^2 + |\mathbf v_0^Q|^2\right) + V = \text{const}, \quad V = mg\left(R\sin\theta - \xi\cos\theta + R\sin\psi + \zeta\cos\psi\right) + \tfrac12 k\left|\overrightarrow{PQ}\right|^2 \end{array}}$$
>
> **Units:** $[mgR] = [k\xi^2] = [\mathrm{M\,L^2\,T^{-2}}]$; powers $[\mathrm{M\,L^2\,T^{-3}}]$
> **Meaning:** the mechanical energy of $P$ alone is not conserved: the string works on $P$ whenever it slides over $A$, and the spring force on $P$ depends on where $Q$ is, so it has no potential of the position of $P$ alone. The pair is conservative: the string only transfers energy from one particle to the other and the spring is an internal conservative force, so the potential energy is the one in the box.

### Answers and Checks

#### (e) Symmetric configurations

> [!derivation] Coordinates of a configuration symmetric about Oy
> **Law:** mirror symmetry about the vertical axis; the length constraint
> **Source:** [Lecture 3, Slide 4]; Problems.pdf, p. 23
>
> The mirror in $Oy$ changes the sign of $x$ and keeps $y$; it sends the polar angle $\theta$ to $\pi - \theta$.
>
> $$\begin{aligned}
> \psi &= \pi - \theta \quad &\text{($B$ is the mirror image of $A$)} \\
> R\cos\psi - \zeta\sin\psi &= -R\cos\theta - \zeta\sin\theta \quad &\text{($x_Q$ with $\cos(\pi - \theta) = -\cos\theta$, $\sin(\pi - \theta) = \sin\theta$)} \\
> -R\cos\theta - \zeta\sin\theta &= -\left(R\cos\theta + \xi\sin\theta\right) \iff \zeta = \xi \quad &\text{(mirror condition $x_Q = -x_P$)} \\
> \xi &= L - \xi - R\left(\pi - \theta - \theta\right) \quad &\text{(length constraint with both relations)} \\
> \xi &= \frac{L - \pi R}{2} + R\theta \quad &\text{(solved for $\xi$)}
> \end{aligned}$$
>
> $$\boxed{\psi = \pi - \theta, \qquad \xi = \zeta = \ell_0 + R\theta, \qquad \ell_0 = \frac{L - \pi R}{2}; \qquad \text{1 degree of freedom, } \theta}$$
>
> **Units:** $[\ell_0] = [R\theta] = [\mathrm{L}]$
> **Meaning:** $\ell_0$ is the length of each hanging segment when $A$ and $B$ are at the ends of the horizontal diameter; the symmetric motion keeps one coordinate, and the vertical coordinates of $P$ and $Q$ are then equal.

#### (f) Equilibrium and small oscillations of the symmetric configuration

![[attachments/EM-SOL/p35-symmetric.svg]]

> [!derivation] Equation of motion of a symmetric motion
> **Law:** projection of Newton's second law perpendicular to the string (free of the tension), with the symmetric relations
> **Source:** Notes.pdf, Eq. 4.4; [Lecture 3, Slide 14]
>
> With the relations of part (e), the spring is horizontal: $\overrightarrow{PQ}$ is minus twice the abscissa of $P$ times $\mathbf i$, and its projection on $\mathbf e_A$ uses the first row of $[{}_0R_1]$.
>
> $$\begin{aligned}
> \overrightarrow{PQ} &= -2\left(R\cos\theta + \xi\sin\theta\right)\mathbf i \quad &\text{($x_Q = -x_P$, $y_Q = y_P$)} \\
> \overrightarrow{PQ}\cdot\mathbf e_A &= -2\left(R\cos\theta + \xi\sin\theta\right)\cos\theta \quad &\text{($\mathbf i\cdot\mathbf e_A = \cos\theta$)} \\
> \dot\xi &= R\dot\theta \quad &\text{(derivative of $\xi = \ell_0 + R\theta$)} \\
> 2\dot\xi\dot\theta - R\dot\theta^2 &= 2R\dot\theta^2 - R\dot\theta^2 = R\dot\theta^2 \quad &\text{(substitution in the acceleration along $\mathbf e_A$)} \\
> m\left(\xi\ddot\theta + R\dot\theta^2\right) &= -mg\sin\theta - 2k\cos\theta\left(R\cos\theta + \xi\sin\theta\right) \quad &\text{(projection of $P$ on $\mathbf e_A$)}
> \end{aligned}$$
>
> $$\boxed{m\left(\ell_0 + R\theta\right)\ddot\theta + mR\dot\theta^2 + mg\sin\theta + 2k\cos\theta\left[R\cos\theta + \left(\ell_0 + R\theta\right)\sin\theta\right] = 0}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the projection of $Q$ on $\mathbf e_B$ gives the same equation (mirror image of every term), so a symmetric start stays symmetric and no extra force is needed to keep it so.

> [!derivation] Linearisation for nearly vertical segments: equilibrium
> **Law:** small deviation of the segments from the vertical (the angle $\theta$, as shown in the position box): first-order expansion of the equation of motion; equilibrium with zero rate and acceleration
> **Source:** Notes.pdf, Eq. 4.32; [Lecture 6, Slide 15]
>
> Every term is expanded to first order in $\theta$ and its derivatives: products of two small quantities are dropped.
>
> $$\begin{aligned}
> m\left(\ell_0 + R\theta\right)\ddot\theta &\simeq m\ell_0\ddot\theta \quad &\text{($R\theta\ddot\theta$ is of second order)} \\
> mR\dot\theta^2 &\simeq 0 \quad &\text{(second order)} \\
> mg\sin\theta &\simeq mg\theta \quad &\text{($\sin\theta \simeq \theta$)} \\
> 2k\left[R\cos^2\theta + \left(\ell_0 + R\theta\right)\sin\theta\cos\theta\right] &\simeq 2k\left(R + \ell_0\theta\right) \quad &\text{($\cos^2\theta \simeq 1$; $\sin\theta\cos\theta \simeq \theta$; $R\theta^2$ dropped)} \\
> m\ell_0\ddot\theta + \left(mg + 2k\ell_0\right)\theta + 2kR &= 0 \quad &\text{(linearised equation)} \\
> \left(mg + 2k\ell_0\right)\theta_0 + 2kR &= 0 \quad &\text{(equilibrium: $\ddot\theta = 0$)}
> \end{aligned}$$
>
> $$\boxed{\theta_0 \simeq -\frac{2kR}{mg + 2k\ell_0}, \qquad \psi_0 = \pi - \theta_0 \simeq \pi + \frac{2kR}{mg + 2k\ell_0}, \qquad \xi_0 = \zeta_0 \simeq \ell_0 - \frac{2kR^2}{mg + 2k\ell_0}}$$
>
> **Units:** $[kR]/[mg] = [\mathrm{M\,T^{-2}}][\mathrm{L}]/[\mathrm{M\,L\,T^{-2}}] = [1]$ and $[k\ell_0] = [mg]$, so $\theta_0$ is dimensionless; $[kR^2/(mg)] = [\mathrm{L}]$
> **Meaning:** $\theta_0$ is negative: $A$ sits slightly below the horizontal diameter and the segments lean inwards, because the spring pulls the particles together and the horizontal part of the tension must balance it. The approximation holds when $2kR$ is small compared with the sum of $mg$ and $2k\ell_0$.

> [!derivation] Linearisation for nearly vertical segments: frequency
> **Law:** deviation from the equilibrium in the linearised equation; harmonic oscillator
> **Source:** Notes.pdf, Eq. 5.6; [Lecture 6, Slide 6]; [Lecture 6, Slide 15]
>
> $$\begin{aligned}
> \theta &= \theta_0 + \delta, \quad \ddot\theta = \ddot\delta \quad &\text{(deviation from the equilibrium; $\theta_0$ constant)} \\
> m\ell_0\ddot\delta + \left(mg + 2k\ell_0\right)\delta + \left[\left(mg + 2k\ell_0\right)\theta_0 + 2kR\right] &= 0 \quad &\text{(substitution in the linearised equation)} \\
> m\ell_0\ddot\delta + \left(mg + 2k\ell_0\right)\delta &= 0 \quad &\text{(the bracket is the equilibrium condition: zero)} \\
> \ddot\delta + \left(\frac{g}{\ell_0} + \frac{2k}{m}\right)\delta &= 0 \quad &\text{(divided by $m\ell_0$: the form of Eq. 5.6)}
> \end{aligned}$$
>
> $$\boxed{\omega_0 = \sqrt{\frac{g}{\ell_0} + \frac{2k}{m}}, \qquad \ell_0 = \frac{L - \pi R}{2}}$$
>
> **Units:** $[g/\ell_0] = [\mathrm{T^{-2}}]$; $[k/m] = [\mathrm{M\,T^{-2}}]/[\mathrm{M}] = [\mathrm{T^{-2}}]$; so $[\omega_0] = [\mathrm{T^{-1}}]$
> **Meaning:** two restoring effects add: gravity, as for a pendulum of length $\ell_0$, and the spring, which pulls both particles inwards when they swing apart. This is the frequency to leading order; the equilibrium shift $\theta_0$ corrects the frequency squared by a first-order factor that comes from the inertia of the segment at the shifted equilibrium (box "Correction of the frequency from the equilibrium shift" below), which is the 2.6 percent of the numerical check.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 3: $\theta$ (polar angle of $A$), $\psi$ (polar angle of $B$), $\xi$ (length of $AP$); $\zeta = L - \xi - R(\psi - \theta)$ |
| (b) Kinematics | $\mathbf r_0^P = R\,\mathbf e_A - \xi\,\mathbf e_\theta$, $\mathbf v_0^P = \xi\dot\theta\,\mathbf e_A + (R\dot\theta - \dot\xi)\,\mathbf e_\theta$, $\mathbf a_0^P = (\xi\ddot\theta + 2\dot\xi\dot\theta - R\dot\theta^2)\,\mathbf e_A + (R\ddot\theta - \ddot\xi + \xi\dot\theta^2)\,\mathbf e_\theta$; $\mathbf r_0^Q = R\,\mathbf e_B + \zeta\,\mathbf e_\psi$, $\mathbf v_0^Q = -\zeta\dot\psi\,\mathbf e_B + (R\dot\theta - \dot\xi)\,\mathbf e_\psi$, $\mathbf a_0^Q = -(\zeta\ddot\psi + 2\dot\zeta\dot\psi + R\dot\psi^2)\,\mathbf e_B + (R\ddot\theta - \ddot\xi - \zeta\dot\psi^2)\,\mathbf e_\psi$ |
| (c) Forces | $P$: $-mg\,\mathbf j$, $T\,\mathbf e_\theta$, $k\overrightarrow{PQ}$; $Q$: $-mg\,\mathbf j$, $-T\,\mathbf e_\psi$, $-k\overrightarrow{PQ}$; $k\overrightarrow{PQ} = kR(\mathbf e_B - \mathbf e_A) + k[L - \xi - R(\psi - \theta)]\,\mathbf e_\psi + k\xi\,\mathbf e_\theta$ |
| (d) Energy | of $P$ alone: not conserved (tension power $T(R\dot\theta - \dot\xi)$, spring force depends on $Q$); of the pair: conserved, $V = mg(y_P + y_Q) + \frac12 k|\overrightarrow{PQ}|^2$ |
| (e) Symmetric motion | 1 degree of freedom; $\psi = \pi - \theta$, $\xi = \zeta = \ell_0 + R\theta$, $\ell_0 = (L - \pi R)/2$ |
| (f) Equilibrium and frequency | $\theta_0 \simeq -2kR/(mg + 2k\ell_0)$, $\psi_0 = \pi - \theta_0$, $\xi_0 \simeq \ell_0 - 2kR^2/(mg + 2k\ell_0)$; $\omega_0 = \sqrt{g/\ell_0 + 2k/m}$ |

**Check against the official key:** Problems.pdf, p. 75, item 35, gives only the spring forces on $P$ and $Q$, written in the same coordinates $\theta$, $\psi$, $\xi$ and the same unit vectors: the key's vector is term by term the one of the box of part (c) (**match**). The other parts have no key; the box below checks the linearisation of part (f) against the exact nonlinear equation with sample data.

> [!derivation] Independent check of the linearisation with sample data
> **Law:** exact equilibrium of the nonlinear symmetric equation (root found by bisection) and its exact stiffness, compared with the first-order formulas
> **Source:** Notes.pdf, Eq. 4.32; [Lecture 6, Slide 15]
>
> Sample data: $R$ of 1 m, $\ell_0$ of 2 m, $m$ of 1 kg, $k$ of 0.3 N/m, $g$ of 9.81 m/s². The nonlinear equilibrium condition is $f(\theta)$ equal to zero, with $f$ the sum of the weight term and the spring term of the symmetric equation of motion.
>
> $$\begin{aligned}
> \theta_0^{\text{lin}} &= -\frac{2(0.3)(1)}{(1)(9.81) + 2(0.3)(2)} = -\frac{0.6}{11.01} = -0.05450\ \text{rad} \quad &\text{(formula of part (f))} \\
> f(\theta) &= mg\sin\theta + 2k\cos\theta\left[R\cos\theta + \left(\ell_0 + R\theta\right)\sin\theta\right] = 0 \ \Rightarrow\ \theta_0 = -0.05453\ \text{rad} \quad &\text{(exact root, bisection)} \\
> \omega_0^{2,\text{lin}} &= \frac{9.81}{2} + \frac{2(0.3)}{1} = 4.905 + 0.600 = 5.505\ \text{s}^{-2} \quad &\text{(formula of part (f))} \\
> \omega_0^2 &= \frac{f'(\theta_0)}{m\left(\ell_0 + R\theta_0\right)} = 5.648\ \text{s}^{-2} \quad &\text{(exact stiffness over the exact inertia at the root)}
> \end{aligned}$$
>
> $$\boxed{\theta_0:\ -0.05453 \ \text{(exact)}\ \text{vs}\ -0.05450 \ \text{(linear)}; \qquad \omega_0^2:\ 5.648 \ \text{vs}\ 5.505\ \text{s}^{-2}}$$
>
> **Units:** angles in rad; $[\omega_0^2] = [\mathrm{T^{-2}}]$
> **Meaning:** the equilibrium agrees to 0.06 percent and the frequency squared to 2.6 percent, a relative difference of the order of the small angle itself (5 percent), as a first-order approximation allows: the linearised results are confirmed.

> [!derivation] Correction of the frequency from the equilibrium shift
> **Law:** linearisation of the symmetric equation of motion about the exact equilibrium (first-order Taylor expansion); product rule
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 5.6; [Lecture 6, Slide 15]
>
> The symmetric equation of motion of part (f) is written with the function $f$ of the check box (weight term plus spring term), and the motion is taken about the exact equilibrium $\theta_0$, where $f$ vanishes.
>
> $$\begin{aligned}
> \theta &= \theta_0 + \delta, \quad \ddot\theta = \ddot\delta \quad &\text{(deviation from the equilibrium; $\theta_0$ constant)} \\
> f\left(\theta_0 + \delta\right) &\simeq f\left(\theta_0\right) + f'\left(\theta_0\right)\delta = f'\left(\theta_0\right)\delta \quad &\text{(first-order Taylor expansion; $f(\theta_0) = 0$ at the equilibrium)} \\
> m\left(\ell_0 + R\theta_0\right)\ddot\delta + f'\left(\theta_0\right)\delta &= 0 \quad &\text{(substitution in the equation of motion; $R\delta\ddot\delta$ and $mR\dot\delta^2$ of second order)} \\
> \frac{d}{d\theta}\left\{\cos\theta\left[R\cos\theta + \left(\ell_0 + R\theta\right)\sin\theta\right]\right\} &= -\sin\theta\left[R\cos\theta + \left(\ell_0 + R\theta\right)\sin\theta\right] + \cos\theta\left[-R\sin\theta + R\sin\theta + \left(\ell_0 + R\theta\right)\cos\theta\right] \quad &\text{(product rule; chain rule inside the bracket)} \\
> &= -R\sin\theta\cos\theta + \left(\ell_0 + R\theta\right)\left(\cos^2\theta - \sin^2\theta\right) \quad &\text{(brackets expanded; $-R\sin\theta + R\sin\theta$ cancels)} \\
> f'\left(\theta\right) &= mg\cos\theta + 2k\left[-R\sin\theta\cos\theta + \left(\ell_0 + R\theta\right)\left(\cos^2\theta - \sin^2\theta\right)\right] \quad &\text{(derivative of $f$ term by term)} \\
> f'\left(\theta_0\right) &\simeq mg + 2k\left(-R\theta_0 + \ell_0 + R\theta_0\right) = mg + 2k\ell_0 \quad &\text{($\cos\theta_0 \simeq 1$, $\sin\theta_0 \simeq \theta_0$; terms in $\theta_0^2$ dropped)} \\
> \omega_0^2 &= \frac{f'\left(\theta_0\right)}{m\left(\ell_0 + R\theta_0\right)} \simeq \frac{mg + 2k\ell_0}{m\left(\ell_0 + R\theta_0\right)} \quad &\text{(stiffness over inertia, form of Eq. 5.6)} \\
> &= \left(\frac{g}{\ell_0} + \frac{2k}{m}\right)\frac{1}{1 + R\theta_0/\ell_0} \quad &\text{(numerator and denominator divided by $m\ell_0$)} \\
> &\simeq \left(\frac{g}{\ell_0} + \frac{2k}{m}\right)\left(1 - \frac{R\theta_0}{\ell_0}\right) \quad &\text{($1/(1 + \varepsilon) \simeq 1 - \varepsilon$ for a small $\varepsilon$)} \\
> &= 5.505\left(1 + 0.5\cdot 0.05453\right) = 5.655\ \text{s}^{-2} \quad &\text{(sample data of the check box)}
> \end{aligned}$$
>
> $$\boxed{\omega_0^2 \simeq \left(\frac{g}{\ell_0} + \frac{2k}{m}\right)\left(1 - \frac{R\theta_0}{\ell_0}\right) + O\left(\theta_0^2\right); \qquad \text{sample data: } 5.655 \ \text{vs}\ 5.648\ \text{s}^{-2} \ \text{(exact)}}$$
>
> **Units:** $[R\theta_0/\ell_0] = [\mathrm{L}]/[\mathrm{L}] = [1]$, so the factor is dimensionless and $[\omega_0^2] = [\mathrm{T^{-2}}]$
> **Meaning:** the stiffness at the shifted equilibrium is unchanged to first order, but the inertia is that of the segment length $\ell_0 + R\theta_0$, shorter than $\ell_0$ because $\theta_0$ is negative, so the oscillation is slightly faster; this factor accounts for the 2.6 percent of the check box, and the remaining 0.1 percent is of second order.

> [!derivation] Limiting cases of the frequency
> **Law:** the equilibrium and frequency of part (f) at the ends of the range of the data
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Sec. 4.7
>
> $$\begin{aligned}
> k \to 0:\quad \theta_0 &\to 0, \quad \omega_0 \to \sqrt{\frac{g}{\ell_0}} \quad &\text{(no spring)} \\
> R \to 0:\quad \theta_0 &\to 0, \quad \ell_0 \to \frac{L}{2}, \quad \omega_0 \to \sqrt{\frac{2g}{L} + \frac{2k}{m}} \quad &\text{(cylinder shrunk to a point)}
> \end{aligned}$$
>
> $$\boxed{k \to 0:\ \omega_0 = \sqrt{g/\ell_0}\ \text{(simple pendulum)}; \qquad R \to 0:\ \omega_0 = \sqrt{2g/L + 2k/m}}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in both limits
> **Meaning:** without the spring each particle is a simple pendulum of length $\ell_0$ hanging vertically from its tangency point; with a vanishing cylinder the two particles hang from one point on segments of length $L/2$, and the spring adds its stiffness to the symmetric swing.

> [!example] Interactive simulator
> sim: {"archetype": "oscillator-phase", "title": "Symmetric swing of the two hanging segments, linearised (Problem 35)", "intro": "Sample data of the solution's own numerical check: R = 1 m, ℓ0 = 2 m (so the string length is L = 2ℓ0 + πR), m = 1 kg, k = 0.3 N/m, g = 9.81 m/s². The archetype draws no cylinder: the mass is the coordinate δ = θ − θ0 of the symmetric motion of part (f), in radians, the deviation of the polar angle of A from its equilibrium, which tilts both hanging segments together. The default is a sample release from rest at δ = 0.05 rad, at t = 0; the oscillation has the frequency ω0 of the linearised equation, and the damping ratio must stay at zero (the model has no damping). The readouts are the equilibrium and the frequency of part (f) and the first-order correction of the check box.", "params": {"mode": "free", "wn": 2.346274, "zeta": 0, "x0": 0.05, "v0": 0, "tmax": 10, "extent": 0.08, "R": 1.0, "l0": 2.0, "m": 1.0, "ks": 0.3, "g": 9.81}, "defaults": {"t": 0, "zeta": 0}, "readouts": [{"label": "String length L = 2ℓ0 + πR for this ℓ0", "expr": "2*l0 + pi*R", "unit": "m", "digits": 4}, {"label": "(f) Equilibrium θ0 = −2kR/(mg + 2kℓ0)", "expr": "(-2*ks*R/(m*g + 2*ks*l0))", "unit": "rad", "digits": 5}, {"label": "(f) ψ0 = π − θ0", "expr": "deg(pi - (-2*ks*R/(m*g + 2*ks*l0)))", "unit": "deg", "digits": 3}, {"label": "(f) Segment length ξ0 = ℓ0 − 2kR²/(mg + 2kℓ0)", "expr": "l0 - 2*ks*R^2/(m*g + 2*ks*l0)", "unit": "m", "digits": 5}, {"label": "(f) ω0 = √(g/ℓ0 + 2k/m)", "expr": "sqrt(g/l0 + 2*ks/m)", "unit": "rad/s", "digits": 4}, {"label": "(f) ω0² = g/ℓ0 + 2k/m", "expr": "g/l0 + 2*ks/m", "unit": "1/s²", "digits": 3}, {"label": "Corrected ω0² (g/ℓ0 + 2k/m)(1 − Rθ0/ℓ0)", "expr": "(g/l0 + 2*ks/m)*(1 - R*(-2*ks*R/(m*g + 2*ks*l0))/l0)", "unit": "1/s²", "digits": 3}, {"label": "Period 2π/ω0", "expr": "2*pi/sqrt(g/l0 + 2*ks/m)", "unit": "s", "digits": 3}, {"label": "Polar angle of A, θ = θ0 + δ", "expr": "(-2*ks*R/(m*g + 2*ks*l0)) + x", "unit": "rad", "digits": 4}]}

---

## Problem 38: Particle on Torus

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m_P$ moves without friction on a vertically standing torus and cannot leave it; a second particle $Q$ of mass $m_Q$ moves without friction on the horizontal plane $Ox_0y_0$; the two attract each other with a force proportional to their distance, of constant $k$ (Problems.pdf, p. 26). The statement asks for a minimal set of coordinates, the kinematics of both particles, two tangent vectors and a normal vector of the torus, the forces, the equations of motion free of reactions, a conservation law and whether $P$ can reach the top of the torus. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ vertical **upward**, $\mathbf i_0$ and $\mathbf j_0$ horizontal, right-handed |
| Torus | read from its parametric equations: the centre circle of the tube is $(2\sin\theta, 0, 4 + 2\cos\theta)$, of radius 2, in the vertical plane $Ox_0z_0$, centred at $C = (0, 0, 4)$; the tube has radius 1. The axis of symmetry of the torus is the horizontal line through $C$ parallel to $\mathbf j_0$ |
| Toroidal basis | $\mathcal B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k_1\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf j_0$ ($\mathbf j_1 = \mathbf j_0$): $\mathbf k_1$ from $C$ towards the centre of the tube section that holds $P$, $\mathbf i_1$ along increasing $\theta$ |
| Poloidal basis | $\mathcal B_2 = \{\mathbf i_2, \mathbf j_2, \mathbf k_2\}$, $\mathcal B_1$ turned by the angle $\phi$ about $-\mathbf i_1$ ($\mathbf i_2 = \mathbf i_1$): $\mathbf k_2$ the outward normal of the torus at $P$, $\mathbf j_2$ along increasing $\phi$ |
| Coordinates (a) | $\theta$: angle of the meridian half-plane of $P$ about the axis of the torus, from $\mathbf k_0$ towards $\mathbf i_0$; $\phi$: angle round the tube in that half-plane, from the outward direction $\mathbf k_1$ towards $\mathbf j_0$; $\xi$, $\eta$: Cartesian coordinates of $Q$ in the plane $Ox_0y_0$ (the letters of the official key) |
| Constraints | $P$ on the torus (1 equation, holonomic, stationary, smooth, bilateral: it cannot separate); $Q$ on the plane, $z_Q = 0$ (1 equation, holonomic, stationary, smooth, bilateral) ([Lecture 3, Slide 21]) |
| Degrees of freedom (a) | 6 coordinates of two particles minus 2 constraint equations: 4, namely $\theta$, $\phi$, $\xi$, $\eta$ ([Lecture 3, Slide 4]) |
| Data | $m_P = 1$, $m_Q = 2$, $k = 2$, lengths as in the equations of the torus; read as SI units (kg, N m$^{-1}$, m); $g$ [m s$^{-2}$] |
| Initial conditions | $\mathbf r_0^P = 2\mathbf i_0 + \mathbf j_0 + 4\mathbf k_0$, $\mathbf v_0^P = -\mathbf k_0$; $\mathbf r_0^Q = 3\mathbf i_0 + \mathbf j_0$, $\mathbf v_0^Q = -\mathbf i_0 + \mathbf j_0$ |
| Applied forces | weights $-m_Pg\,\mathbf k_0$ and $-m_Qg\,\mathbf k_0$; mutual attraction $k\overrightarrow{PQ}$ on $P$ and $-k\overrightarrow{PQ}$ on $Q$ (a zero-length spring, Notes.pdf, Sec. 7.5) |
| Constraint forces | normal reaction of the torus $N\,\mathbf k_2$ on $P$ (one unknown, Notes.pdf, Sec. 6.4); normal reaction of the plane $N_Q\,\mathbf k_0$ on $Q$ |

![[attachments/EM-SOL/p38-meridian.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p38-rotation-j.svg]]

> [!derivation] Toroidal basis: rotation about j0
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19
>
> View of the vertical plane $Ox_0z_0$ with $\mathbf i_0$ to the right and $\mathbf k_0$ up: $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points into the paper (⊗), so a positive rotation about $\mathbf j_0$ is clockwise as seen. The angle $\theta$ goes from $\mathbf k_0$ (up) towards $\mathbf i_0$ (right): clockwise, a positive rotation. $\mathbf k_1$ is $\mathbf k_0$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf k_0$, opposite leg $\sin\theta$ along $\mathbf i_0$. $\mathbf i_1$ is $\mathbf i_0$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf i_0$, opposite leg $\sin\theta$ along minus $\mathbf k_0$, because the vector to the right turned clockwise points downwards (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf i_1$: opposite leg on $-\mathbf k_0$)} \\
> \mathbf k_1 &= \sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf k_1$)} \\
> \mathbf i_1\times\mathbf j_0 &= \cos\theta\,\mathbf k_0 - \sin\theta\,\mathbf k_0\times\mathbf j_0 = \cos\theta\,\mathbf k_0 + \sin\theta\,\mathbf i_0 = \mathbf k_1 \quad &\text{(right-handed; $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> \det[{}_0R_1] &= \cos\theta\left(\cos\theta\right) - 0 + \sin\theta\left(0 + \sin\theta\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + 0 + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{13} &= -\cos\theta\sin\theta + \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 3; row 2 is the unit row of $\mathbf j_0$)} \\
> \mathbf i_0 &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf k_1, \quad \mathbf k_0 = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1 \quad &\text{(rows 1 and 3 of the matrix, Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf k_1$ points from the centre $C$ of the torus to the centre of the tube section through $P$; $\mathbf i_1$ is the direction in which $P$ moves when only $\theta$ changes.

> [!derivation] Poloidal basis: rotation in the meridian half-plane
> **Law:** elementary rotation about the first axis, with a negative angle; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.18
>
> View of the meridian half-plane with $\mathbf j_1$ to the right and $\mathbf k_1$ up: $\mathbf i_1$, the cross product of $\mathbf j_1$ and $\mathbf k_1$, points out of the paper (⊙), so positive angles about $\mathbf i_1$ are counterclockwise. The angle $\phi$ goes from $\mathbf k_1$ (up) towards $\mathbf j_1$ (right): clockwise, so the poloidal basis is Eq. 1.18 with the angle minus $\phi$. $\mathbf k_2$ is $\mathbf k_1$ turned clockwise by $\phi$: hypotenuse 1, adjacent leg $\cos\phi$ along $\mathbf k_1$, opposite leg $\sin\phi$ along $\mathbf j_1$. $\mathbf j_2$ is $\mathbf j_1$ turned clockwise by $\phi$: adjacent leg $\cos\phi$ along $\mathbf j_1$, opposite leg $\sin\phi$ along minus $\mathbf k_1$, since the vector to the right turned clockwise points downwards (the minus sign).
>
> $$\begin{aligned}
> \mathbf j_2 &= \cos\phi\,\mathbf j_1 - \sin\phi\,\mathbf k_1 \quad &\text{(right triangle of $\mathbf j_2$: opposite leg on $-\mathbf k_1$)} \\
> \mathbf k_2 &= \sin\phi\,\mathbf j_1 + \cos\phi\,\mathbf k_1 \quad &\text{(right triangle of $\mathbf k_2$)} \\
> \mathbf i_2\times\mathbf j_2 &= \cos\phi\,\mathbf i_1\times\mathbf j_1 - \sin\phi\,\mathbf i_1\times\mathbf k_1 = \cos\phi\,\mathbf k_1 + \sin\phi\,\mathbf j_1 = \mathbf k_2 \quad &\text{(right-handed; $\mathbf i_1\times\mathbf k_1 = -\mathbf j_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos\phi\cos\phi - \sin\phi\left(-\sin\phi\right)\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{22} &= 0 + \cos^2\phi + \sin^2\phi = 1 \quad &\text{(row 2 times row 2)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{23} &= -\cos\phi\sin\phi + \sin\phi\cos\phi = 0 \quad &\text{(row 2 times row 3; row 1 is the unit row of $\mathbf i_1$)} \\
> \mathbf j_1 &= \cos\phi\,\mathbf j_2 + \sin\phi\,\mathbf k_2, \quad \mathbf k_1 = -\sin\phi\,\mathbf j_2 + \cos\phi\,\mathbf k_2 \quad &\text{(rows 2 and 3 of the matrix)}
> \end{aligned}$$
>
> $$\boxed{[{}_1R_2] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & \cos\phi & \sin\phi \cr 0 & -\sin\phi & \cos\phi \end{pmatrix}, \quad \det[{}_1R_2] = 1, \quad [{}_1R_2][{}_1R_2]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf k_2$ is the outward normal of the tube at $P$ and $\mathbf j_2$ its tangent along the small circle of the section.

> [!derivation] Position vectors of both particles
> **Law:** position vector as a sum of partial vectors; constraints substituted
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Sec. 7.4; Problems.pdf, p. 26
>
> $\overrightarrow{OC}$ is $4\mathbf k_0$; the centre $D$ of the tube section of $P$ is at the distance 2 from $C$ along $\mathbf k_1$; $P$ is at the distance 1 from $D$ along $\mathbf k_2$. In the right triangle of $DP$ (meridian figure) the hypotenuse is 1, the leg along $\mathbf k_1$ is $\cos\phi$ (adjacent to $\phi$) and the leg along $\mathbf j_1$ is $\sin\phi$ (opposite).
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OC} + \overrightarrow{CD} + \overrightarrow{DP} = 4\,\mathbf k_0 + 2\,\mathbf k_1 + \mathbf k_2 \quad &\text{(sum of partial vectors)} \\
> &= 4\,\mathbf k_0 + \left(2 + \cos\phi\right)\mathbf k_1 + \sin\phi\,\mathbf j_1 \quad &\text{($\mathbf k_2$ in $\mathcal B_1$)} \\
> &= \left(2 + \cos\phi\right)\sin\theta\,\mathbf i_0 + \sin\phi\,\mathbf j_0 + \left[4 + \left(2 + \cos\phi\right)\cos\theta\right]\mathbf k_0 \quad &\text{($\mathbf k_1$ in $\mathcal B_0$; the equations of the statement)} \\
> \mathbf r_0^Q &= \xi\,\mathbf i_0 + \eta\,\mathbf j_0 \quad &\text{(on the plane $z_Q = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = 4\,\mathbf k_0 + \varrho\,\mathbf k_1 + \sin\phi\,\mathbf j_1, \quad \varrho = 2 + \cos\phi; \qquad \mathbf r_0^Q = \xi\,\mathbf i_0 + \eta\,\mathbf j_0}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** $\varrho$ is the distance from $P$ to the axis of the torus; the third line reproduces the parametric equations of the statement, which confirms the reading of $\theta$ and $\phi$.

> [!derivation] Coordinates at the initial instant
> **Law:** the initial position and velocity written with the coordinates
> **Source:** Problems.pdf, p. 26
>
> $$\begin{aligned}
> \sin\phi_0 &= 1 \Rightarrow \phi_0 = \tfrac{\pi}{2}, \quad \varrho_0 = 2 + 0 = 2 \quad &\text{($y_P = 1$)} \\
> 2\sin\theta_0 &= 2, \quad 4 + 2\cos\theta_0 = 4 \Rightarrow \theta_0 = \tfrac{\pi}{2} \quad &\text{($x_P = 2$, $z_P = 4$)} \\
> \mathbf i_1 &= -\mathbf k_0, \quad \mathbf j_2 = -\mathbf k_1 = -\mathbf i_0, \quad \mathbf k_2 = \mathbf j_0 \quad &\text{(bases at $\theta = \phi = \pi/2$)} \\
> \mathbf v_0^P &= \varrho\dot\theta\,\mathbf i_1 + \dot\phi\,\mathbf j_2 = -2\dot\theta\,\mathbf k_0 - \dot\phi\,\mathbf i_0 = -\mathbf k_0 \quad &\text{(velocity of the kinematics box below at $t_0$)} \\
> \xi_0 &= 3, \quad \eta_0 = 1, \quad \dot\xi_0 = -1, \quad \dot\eta_0 = 1 \quad &\text{(position and velocity of $Q$)}
> \end{aligned}$$
>
> $$\boxed{\theta_0 = \phi_0 = \tfrac{\pi}{2}, \quad \dot\theta_0 = \tfrac12, \quad \dot\phi_0 = 0; \qquad \xi_0 = 3, \quad \eta_0 = 1, \quad \dot\xi_0 = -1, \quad \dot\eta_0 = 1}$$
>
> **Units:** angles in rad, rates in $[\mathrm{T^{-1}}]$; $[\xi] = [\mathrm{L}]$
> **Meaning:** $P$ starts at the meridian angle $\theta = \pi/2$, where its tube section is the horizontal circle centred at $(2, 0, 4)$; the angle $\phi = \pi/2$ is the point of that circle farthest along $+\mathbf j_0$. The normal there is $\mathbf j_0$, perpendicular to the initial velocity $-\mathbf k_0$ (as it must be), and $P$ starts moving straight down along the toroidal direction $\mathbf i_1$, which is $-\mathbf k_0$ at that instant.

### Kinematics

> [!derivation] Derivatives of the toroidal basis
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf j_0 \quad &\text{($\mathcal B_1$ turns about the fixed $\mathbf j_0$ with $\theta$)} \\
> \dot{\mathbf k}_1 &= \dot\theta\,\mathbf j_1\times\mathbf k_1 = \dot\theta\,\mathbf i_1 \quad &\text{($\mathbf j_1\times\mathbf k_1 = \mathbf i_1$)} \\
> \dot{\mathbf i}_1 &= \dot\theta\,\mathbf j_1\times\mathbf i_1 = -\dot\theta\,\mathbf k_1 \quad &\text{($\mathbf j_1\times\mathbf i_1 = -\mathbf k_1$)} \\
> \dot{\mathbf j}_1 &= \mathbf 0 \quad &\text{($\mathbf j_1 = \mathbf j_0$ is fixed)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_1 = -\dot\theta\,\mathbf k_1, \qquad \dot{\mathbf j}_1 = \mathbf 0, \qquad \dot{\mathbf k}_1 = \dot\theta\,\mathbf i_1}$$
>
> **Units:** $[\dot\theta] = [\mathrm{T^{-1}}]$
> **Meaning:** the meridian half-plane of $P$ turns about the axis of the torus.

> [!derivation] (b) Position, velocity and acceleration of P
> **Law:** time derivatives in $S_0$; product and chain rules; projection on the poloidal basis
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \dot\varrho &= -\sin\phi\,\dot\phi \quad &\text{(chain rule on $2 + \cos\phi$)} \\
> \mathbf v_0^P &= \dot\varrho\,\mathbf k_1 + \varrho\,\dot{\mathbf k}_1 + \cos\phi\,\dot\phi\,\mathbf j_1 \quad &\text{(product rule; $4\,\mathbf k_0$ and $\mathbf j_1$ fixed)} \\
> &= \varrho\dot\theta\,\mathbf i_1 - \sin\phi\,\dot\phi\,\mathbf k_1 + \cos\phi\,\dot\phi\,\mathbf j_1 \quad &\text{(derivatives of $\varrho$ and $\mathbf k_1$ substituted)} \\
> &= \varrho\dot\theta\,\mathbf i_1 + \dot\phi\left(\cos\phi\,\mathbf j_1 - \sin\phi\,\mathbf k_1\right) \quad &\text{(common factor $\dot\phi$)} \\
> &= \varrho\dot\theta\,\mathbf i_2 + \dot\phi\,\mathbf j_2 \quad &\text{($\mathbf i_2 = \mathbf i_1$; the bracket is $\mathbf j_2$ of the poloidal basis)} \\
> \mathbf a_0^P &= \left(\dot\varrho\dot\theta + \varrho\ddot\theta\right)\mathbf i_1 + \varrho\dot\theta\,\dot{\mathbf i}_1 + \left(\cos\phi\,\ddot\phi - \sin\phi\,\dot\phi^2\right)\mathbf j_1 - \left(\sin\phi\,\ddot\phi + \cos\phi\,\dot\phi^2\right)\mathbf k_1 - \sin\phi\,\dot\phi\,\dot{\mathbf k}_1 \quad &\text{(product and chain rules on the velocity in $\mathcal B_1$)} \\
> &= \left(\varrho\ddot\theta - 2\sin\phi\,\dot\phi\dot\theta\right)\mathbf i_1 + \left(\cos\phi\,\ddot\phi - \sin\phi\,\dot\phi^2\right)\mathbf j_1 - \left(\varrho\dot\theta^2 + \sin\phi\,\ddot\phi + \cos\phi\,\dot\phi^2\right)\mathbf k_1 \quad &\text{(derivatives of $\mathbf i_1$, $\mathbf k_1$; grouped)} \\
> \mathbf a_0^P\cdot\mathbf j_2 &= \cos^2\phi\,\ddot\phi - \cos\phi\sin\phi\,\dot\phi^2 + \sin\phi\,\varrho\dot\theta^2 + \sin^2\phi\,\ddot\phi + \sin\phi\cos\phi\,\dot\phi^2 \quad &\text{(dot product with $\cos\phi\,\mathbf j_1 - \sin\phi\,\mathbf k_1$, expanded)} \\
> &= \left(\cos^2\phi + \sin^2\phi\right)\ddot\phi + \varrho\sin\phi\,\dot\theta^2 \quad &\text{(the terms in $\dot\phi^2$ cancel; terms in $\ddot\phi$ collected)} \\
> &= \ddot\phi + \varrho\sin\phi\,\dot\theta^2 \quad &\text{($\cos^2\phi + \sin^2\phi = 1$)} \\
> \mathbf a_0^P\cdot\mathbf k_2 &= \sin\phi\cos\phi\,\ddot\phi - \sin^2\phi\,\dot\phi^2 - \cos\phi\,\varrho\dot\theta^2 - \cos\phi\sin\phi\,\ddot\phi - \cos^2\phi\,\dot\phi^2 \quad &\text{(dot product with $\sin\phi\,\mathbf j_1 + \cos\phi\,\mathbf k_1$, expanded)} \\
> &= -\left(\sin^2\phi + \cos^2\phi\right)\dot\phi^2 - \varrho\cos\phi\,\dot\theta^2 \quad &\text{(the terms in $\ddot\phi$ cancel; terms in $\dot\phi^2$ collected)} \\
> &= -\dot\phi^2 - \varrho\cos\phi\,\dot\theta^2 \quad &\text{($\sin^2\phi + \cos^2\phi = 1$)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^P = 4\,\mathbf k_0 + \varrho\,\mathbf k_1 + \sin\phi\,\mathbf j_1, \quad \mathbf v_0^P = \varrho\dot\theta\,\mathbf i_2 + \dot\phi\,\mathbf j_2 \cr \mathbf a_0^P = \left(\varrho\ddot\theta - 2\sin\phi\,\dot\theta\dot\phi\right)\mathbf i_2 + \left(\ddot\phi + \varrho\sin\phi\,\dot\theta^2\right)\mathbf j_2 - \left(\dot\phi^2 + \varrho\cos\phi\,\dot\theta^2\right)\mathbf k_2, \quad \varrho = 2 + \cos\phi \end{array}}$$
>
> **Units:** lengths in m (the tube radius 1 m multiplies $\dot\phi$): $[\varrho\dot\theta] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity lies in the tangent plane of the torus (no $\mathbf k_2$ component) while the acceleration has a normal part, the centripetal acceleration of the two circular motions, which the reaction and the forces must supply.

> [!derivation] (b) Position, velocity and acceleration of Q
> **Law:** time derivatives in $S_0$ of Cartesian components
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4
>
> $$\begin{aligned}
> \mathbf v_0^Q &= \dot\xi\,\mathbf i_0 + \dot\eta\,\mathbf j_0 \quad &\text{(fixed unit vectors)} \\
> \mathbf a_0^Q &= \ddot\xi\,\mathbf i_0 + \ddot\eta\,\mathbf j_0 \quad &\text{(derivative of the velocity)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^Q = \xi\,\mathbf i_0 + \eta\,\mathbf j_0, \quad \mathbf v_0^Q = \dot\xi\,\mathbf i_0 + \dot\eta\,\mathbf j_0, \quad \mathbf a_0^Q = \ddot\xi\,\mathbf i_0 + \ddot\eta\,\mathbf j_0}$$
>
> **Units:** $[\mathrm{L}]$, $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $Q$ moves freely in the horizontal plane.

> [!derivation] (c) Tangent and normal vectors of the torus
> **Law:** tangent vectors as partial derivatives of the parametric form; normal as their cross product
> **Source:** [Lecture 3, Slide 9]; Notes.pdf, Sec. 6.3
>
> $$\begin{aligned}
> \mathbf t_\theta &= \frac{\partial\mathbf r_0^P}{\partial\theta} = \varrho\,\frac{\partial\mathbf k_1}{\partial\theta} = \varrho\,\mathbf i_1 \quad &\text{($\partial\mathbf k_1/\partial\theta = \cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf k_0 = \mathbf i_1$)} \\
> \mathbf t_\phi &= \frac{\partial\mathbf r_0^P}{\partial\phi} = -\sin\phi\,\mathbf k_1 + \cos\phi\,\mathbf j_1 = \mathbf j_2 \quad &\text{(derivative of $\varrho\,\mathbf k_1 + \sin\phi\,\mathbf j_1$)} \\
> \mathbf t_\theta\times\mathbf t_\phi &= \varrho\,\mathbf i_2\times\mathbf j_2 = \varrho\,\mathbf k_2 \quad &\text{(right-handed $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf t_\theta = \left(2 + \cos\phi\right)\mathbf i_1, \quad \mathbf t_\phi = \cos\phi\,\mathbf j_1 - \sin\phi\,\mathbf k_1, \quad \mathbf n = \mathbf k_2 = \sin\phi\,\mathbf j_1 + \cos\phi\,\mathbf k_1}$$
>
> **Units:** $[\mathbf t_\theta] = [\mathbf t_\phi] = [\mathrm{L}]$ per radian; $\mathbf n$ dimensionless
> **Meaning:** the two tangent vectors are orthogonal and $\varrho$ never vanishes (its minimum is 1), so the parametrisation is regular everywhere; in $\mathcal B_0$, $\mathbf i_1 = \cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf k_0$ and $\mathbf k_1 = \sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf k_0$.

### Forces and Equations of Motion

The free-body diagrams show on $P$ its weight, the attraction towards $Q$ and the normal reaction of the torus; on $Q$ its weight, the attraction towards $P$ and the normal reaction of the plane. $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p38-fbd.svg]]

> [!derivation] (d) Forces on both particles
> **Law:** weight; attraction proportional to the distance (zero-length spring); normal reactions of smooth surfaces
> **Source:** Notes.pdf, Sec. 6.4; Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]; Problems.pdf, p. 75
>
> $$\begin{aligned}
> \overrightarrow{PQ} &= \mathbf r_0^Q - \mathbf r_0^P = \left(\xi - \varrho\sin\theta\right)\mathbf i_0 + \left(\eta - \sin\phi\right)\mathbf j_0 - \left(4 + \varrho\cos\theta\right)\mathbf k_0 \quad &\text{(difference of the position vectors)} \\
> \mathbf F_P &= k\overrightarrow{PQ} = 2\left[\xi - \left(2 + \cos\phi\right)\sin\theta\right]\mathbf i_0 + 2\left(\eta - \sin\phi\right)\mathbf j_0 - 2\left[4 + \left(2 + \cos\phi\right)\cos\theta\right]\mathbf k_0 \quad &\text{(attraction on $P$, $k = 2$)} \\
> \mathbf F_Q &= -k\overrightarrow{PQ} \quad &\text{(action and reaction)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} P:\ -m_Pg\,\mathbf k_0, \quad \mathbf F_P = k\overrightarrow{PQ}, \quad N\,\mathbf k_2 \cr Q:\ -m_Qg\,\mathbf k_0, \quad -k\overrightarrow{PQ}, \quad N_Q\,\mathbf k_0 \end{array}}$$
>
> **Units:** $[k\,|\overrightarrow{PQ}|] = [\mathrm{M\,T^{-2}}][\mathrm{L}] = [mg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two unknown reactions, $N$ and $N_Q$, each along the single normal direction of its smooth surface.

> [!derivation] Projections of the forces on the tangent plane of the torus
> **Law:** dot products with the poloidal basis, using the rows of the change of basis matrices
> **Source:** Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.16
>
> From the two matrices: $\mathbf i_0$ has the components $\cos\theta$, $-\sin\theta\sin\phi$, $\sin\theta\cos\phi$ on $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$; $\mathbf j_0$ has $0$, $\cos\phi$, $\sin\phi$; $\mathbf k_0$ has $-\sin\theta$, $-\cos\theta\sin\phi$, $\cos\theta\cos\phi$; $\mathbf k_1$ has $0$, $-\sin\phi$, $\cos\phi$.
>
> $$\begin{aligned}
> \overrightarrow{PQ} &= \xi\,\mathbf i_0 + \eta\,\mathbf j_0 - 4\,\mathbf k_0 - \varrho\,\mathbf k_1 - \sin\phi\,\mathbf j_1 \quad &\text{(position vectors in mixed bases)} \\
> \overrightarrow{PQ}\cdot\mathbf i_2 &= \xi\cos\theta + 4\sin\theta \quad &\text{(components on $\mathbf i_2$; $\mathbf k_1$, $\mathbf j_1$ have none)} \\
> \overrightarrow{PQ}\cdot\mathbf j_2 &= -\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + \varrho\sin\phi - \sin\phi\cos\phi \quad &\text{(components on $\mathbf j_2$)} \\
> &= -\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + 2\sin\phi \quad &\text{($\varrho\sin\phi - \sin\phi\cos\phi = 2\sin\phi$)} \\
> -m_Pg\,\mathbf k_0\cdot\mathbf i_2 &= m_Pg\sin\theta, \quad -m_Pg\,\mathbf k_0\cdot\mathbf j_2 = m_Pg\cos\theta\sin\phi \quad &\text{(weight)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \left(\mathbf F_P - m_Pg\,\mathbf k_0\right)\cdot\mathbf i_2 = m_Pg\sin\theta + k\left(\xi\cos\theta + 4\sin\theta\right) \cr \left(\mathbf F_P - m_Pg\,\mathbf k_0\right)\cdot\mathbf j_2 = m_Pg\cos\theta\sin\phi + k\left(-\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + 2\sin\phi\right) \end{array}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the reaction $N\,\mathbf k_2$ has no component on $\mathbf i_2$ or $\mathbf j_2$, so these two projections carry the applied forces only.

> [!derivation] (e) Equations of motion free of reactions
> **Law:** Newton's second law in an inertial frame; projections on the tangent plane of the torus and on the plane of $Q$, free of the reactions
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> P,\ \mathbf i_2:\ m_P\left(\varrho\ddot\theta - 2\sin\phi\,\dot\theta\dot\phi\right) &= m_Pg\sin\theta + k\left(\xi\cos\theta + 4\sin\theta\right) \quad &\text{(toroidal direction)} \\
> P,\ \mathbf j_2:\ m_P\left(\ddot\phi + \varrho\sin\phi\,\dot\theta^2\right) &= m_Pg\cos\theta\sin\phi + k\left(-\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + 2\sin\phi\right) \quad &\text{(poloidal direction)} \\
> Q,\ \mathbf i_0:\ m_Q\ddot\xi &= -k\left(\xi - \varrho\sin\theta\right) \quad &\text{(horizontal: no reaction)} \\
> Q,\ \mathbf j_0:\ m_Q\ddot\eta &= -k\left(\eta - \sin\phi\right) \quad &\text{(horizontal: no reaction)} \\
> m_P = 1,\ m_Q = 2,\ k = 2 &\Rightarrow \text{the system below} \quad &\text{(data substituted)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \left(2 + \cos\phi\right)\ddot\theta = 2\sin\phi\,\dot\theta\dot\phi + g\sin\theta + 2\left(\xi\cos\theta + 4\sin\theta\right) \cr \ddot\phi = -\left(2 + \cos\phi\right)\sin\phi\,\dot\theta^2 + g\cos\theta\sin\phi + 2\left(-\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + 2\sin\phi\right) \cr \ddot\xi = -\xi + \left(2 + \cos\phi\right)\sin\theta, \qquad \ddot\eta = -\eta + \sin\phi \end{array}}$$
>
> **Units:** with the data in SI, $[\ddot\phi] = [\mathrm{T^{-2}}]$ and every term of its equation (divided by the tube radius 1 m) is $[\mathrm{T^{-2}}]$; $[\ddot\xi] = [\xi]\,[k/m_Q] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** four second-order equations for the four coordinates, free of $N$ and $N_Q$; the reactions follow afterwards from the projections on $\mathbf k_2$ (for $P$) and on $\mathbf k_0$ (for $Q$, which gives $N_Q = m_Qg - k\,z_P$).

### Answers and Checks

#### (f) A scalar conservation law

> [!derivation] Mechanical energy of the pair
> **Law:** theorem of kinetic energy for each particle; stationary smooth constraints do no work; internal conservative attraction
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 6.12; [Lecture 3, Slide 16]
>
> $$\begin{aligned}
> N\,\mathbf k_2\cdot\mathbf v_0^P &= N\,\mathbf k_2\cdot\left(\varrho\dot\theta\,\mathbf i_2 + \dot\phi\,\mathbf j_2\right) = 0, \quad N_Q\,\mathbf k_0\cdot\mathbf v_0^Q = 0 \quad &\text{(reactions normal to the velocities)} \\
> k\overrightarrow{PQ}\cdot\mathbf v_0^P - k\overrightarrow{PQ}\cdot\mathbf v_0^Q &= -k\overrightarrow{PQ}\cdot\frac{d\overrightarrow{PQ}}{dt} = -\frac{d}{dt}\left(\tfrac12 k\left|\overrightarrow{PQ}\right|^2\right) \quad &\text{(power of the attraction on both; chain rule)} \\
> -m_Pg\,\mathbf k_0\cdot\mathbf v_0^P - m_Qg\,\mathbf k_0\cdot\mathbf v_0^Q &= -\frac{d}{dt}\left(m_Pg\,z_P\right) \quad &\text{($z_Q = 0$ always)} \\
> \frac{d}{dt}\left[\tfrac12 m_P|\mathbf v_0^P|^2 + \tfrac12 m_Q|\mathbf v_0^Q|^2\right] &= -\frac{d}{dt}\left[m_Pg\,z_P + \tfrac12 k\left|\overrightarrow{PQ}\right|^2\right] \quad &\text{(sum of all powers)} \\
> |\mathbf v_0^P|^2 &= \varrho^2\dot\theta^2 + \dot\phi^2 \quad &\text{(orthonormal $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12\left[\left(2 + \cos\phi\right)^2\dot\theta^2 + \dot\phi^2\right] + \left(\dot\xi^2 + \dot\eta^2\right) + g\left[4 + \left(2 + \cos\phi\right)\cos\theta\right] + \left|\overrightarrow{PQ}\right|^2 = \text{const}}$$
>
> **Units:** every term $[\mathrm{M\,L^2\,T^{-2}}]$ with the masses and $k$ in SI ($\frac12 m_Q = 1$ kg, $\frac12 k = 1$ N m$^{-1}$)
> **Meaning:** the torus and the plane are fixed and smooth, so their reactions do no work; the weight of $Q$ does no work because $Q$ stays at zero height; the attraction is internal and conservative. The total mechanical energy is the scalar conservation law.

> [!derivation] Value of the energy at the initial instant
> **Law:** the conservation law evaluated with the initial conditions
> **Source:** Problems.pdf, p. 26
>
> $$\begin{aligned}
> \tfrac12 m_P|\mathbf v_0^P|^2 &= \tfrac12(1)(1)^2 = 0.5 \quad &\text{($\mathbf v_0^P = -\mathbf k_0$)} \\
> \tfrac12 m_Q|\mathbf v_0^Q|^2 &= \tfrac12(2)\left[(-1)^2 + 1^2\right] = 2 \quad &\text{($\mathbf v_0^Q = -\mathbf i_0 + \mathbf j_0$)} \\
> m_Pg\,z_P &= (1)\,g\,(4) = 4g \quad &\text{($z_P = 4$)} \\
> \left|\overrightarrow{PQ}\right|^2 &= (3 - 2)^2 + (1 - 1)^2 + (0 - 4)^2 = 17 \quad &\text{(initial positions)} \\
> \tfrac12 k\left|\overrightarrow{PQ}\right|^2 &= \tfrac12(2)(17) = 17 \quad &\text{(attraction potential)} \\
> E_0 &= 0.5 + 2 + 4g + 17 = 19.5 + 4g \quad &\text{(sum)}
> \end{aligned}$$
>
> $$\boxed{E_0 = 19.5 + 4g\ \text{J} = 58.74\ \text{J} \ (g = 9.81\ \text{m s}^{-2})}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$, joules
> **Meaning:** most of the initial energy is the potential of the attraction (17 J) and of the height of $P$ (39.24 J).

#### (g) Can P reach the highest point of the torus?

> [!derivation] Energy needed at the top of the torus
> **Law:** the kinetic energies are never negative, so at any reachable state the potential energy cannot exceed the constant energy
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.31
>
> The highest point of the torus is where $z_P$ is largest: $\cos\theta = 1$ and $\cos\phi = 1$, that is $\theta = \phi = 0$, with $z_P = 4 + 3 = 7$. There $P$ is 7 above the plane of $Q$, so the distance $|PQ|$ is at least 7.
>
> $$\begin{aligned}
> z_{P,\max} &= 4 + \left(2 + 1\right)\left(1\right) = 7 \quad &\text{($\theta = \phi = 0$)} \\
> \left|\overrightarrow{PQ}\right|^2 &= \left(\xi - 0\right)^2 + \left(\eta - 0\right)^2 + \left(0 - 7\right)^2 \ge 49 \quad &\text{(at the top; $\xi$, $\eta$ free)} \\
> E &\ge m_Pg\,(7) + \tfrac12 k\,(49) = 7g + 49 \quad &\text{(kinetic energies dropped)} \\
> E_0 - \left(7g + 49\right) &= 19.5 + 4g - 7g - 49 = -29.5 - 3g \lt 0 \quad &\text{(for every $g \ge 0$)}
> \end{aligned}$$
>
> $$\boxed{E_0 = 58.74\ \text{J} \lt 7g + 49 = 117.67\ \text{J}: \ P \ \text{can never reach the top of the torus}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$, joules
> **Meaning:** the energy falls short by 58.9 J; even without the attraction term (which only strengthens the conclusion) the gravity term alone would need $7g$ = 68.67 J against 58.74 J available. The answer does not depend on the value of $g$.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Coordinates | $\theta$ (meridian angle about the axis of the torus, the horizontal line through $(0, 0, 4)$ parallel to $\mathbf j_0$), $\phi$ (angle round the tube), $\xi$, $\eta$ (Cartesian coordinates of $Q$): 4 degrees of freedom |
| (b) Kinematics | $\mathbf r_0^P = 4\,\mathbf k_0 + \varrho\,\mathbf k_1 + \sin\phi\,\mathbf j_1$, $\mathbf v_0^P = \varrho\dot\theta\,\mathbf i_2 + \dot\phi\,\mathbf j_2$, $\mathbf a_0^P = (\varrho\ddot\theta - 2\sin\phi\,\dot\theta\dot\phi)\,\mathbf i_2 + (\ddot\phi + \varrho\sin\phi\,\dot\theta^2)\,\mathbf j_2 - (\dot\phi^2 + \varrho\cos\phi\,\dot\theta^2)\,\mathbf k_2$, $\varrho = 2 + \cos\phi$; $\mathbf r_0^Q = \xi\,\mathbf i_0 + \eta\,\mathbf j_0$, $\mathbf v_0^Q = \dot\xi\,\mathbf i_0 + \dot\eta\,\mathbf j_0$, $\mathbf a_0^Q = \ddot\xi\,\mathbf i_0 + \ddot\eta\,\mathbf j_0$ |
| (c) Tangent and normal | $\mathbf t_\theta = (2 + \cos\phi)\,\mathbf i_1$, $\mathbf t_\phi = \cos\phi\,\mathbf j_1 - \sin\phi\,\mathbf k_1$, $\mathbf n = \sin\phi\,\mathbf j_1 + \cos\phi\,\mathbf k_1$, with $\mathbf i_1 = \cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf k_0$, $\mathbf k_1 = \sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf k_0$ |
| (d) Forces | $P$: $-m_Pg\,\mathbf k_0$, $k\overrightarrow{PQ} = 2[\xi - (2 + \cos\phi)\sin\theta]\,\mathbf i_0 + 2(\eta - \sin\phi)\,\mathbf j_0 - 2[4 + (2 + \cos\phi)\cos\theta]\,\mathbf k_0$, $N\,\mathbf n$; $Q$: $-m_Qg\,\mathbf k_0$, $-k\overrightarrow{PQ}$, $N_Q\,\mathbf k_0$ |
| (e) Equations of motion | $(2 + \cos\phi)\ddot\theta = 2\sin\phi\,\dot\theta\dot\phi + g\sin\theta + 2(\xi\cos\theta + 4\sin\theta)$; $\ddot\phi = -(2 + \cos\phi)\sin\phi\,\dot\theta^2 + g\cos\theta\sin\phi + 2(-\xi\sin\theta\sin\phi + \eta\cos\phi + 4\cos\theta\sin\phi + 2\sin\phi)$; $\ddot\xi = -\xi + (2 + \cos\phi)\sin\theta$; $\ddot\eta = -\eta + \sin\phi$ |
| (f) Conservation law | $E = \frac12[(2 + \cos\phi)^2\dot\theta^2 + \dot\phi^2] + \dot\xi^2 + \dot\eta^2 + g\,z_P + |\overrightarrow{PQ}|^2$, $E_0 = 19.5 + 4g$ |
| (g) Top of the torus | no: it needs at least $7g + 49$, more than $E_0$ for any $g$ |

**Check against the official key:** Problems.pdf, p. 75, item 38, gives the force on $P$ due to $Q$ in the same coordinates (the key's letters $\xi$, $\eta$ for $Q$): identical, component by component, to the box of part (d) (**match**). The other parts have no key; the independent checks are the reproduction of the parametric equations of the statement by the position vector, the orthogonality of the initial velocity to the normal $\mathbf j_0$ in the box of the initial coordinates, and the limiting case below.

> [!derivation] Limiting case: P alone at the top of its tube section
> **Law:** the equations of motion with the attraction removed, at a point of symmetry
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.4
>
> Without the attraction ($k$ set to zero) $P$ is a heavy particle on a fixed smooth torus. The highest point, $\theta = \phi = 0$, must then be an equilibrium, since every tangent direction there is horizontal.
>
> $$\begin{aligned}
> \left(2 + 1\right)\ddot\theta &= 0 + g\sin 0 + 0 = 0 \quad &\text{(toroidal equation at rest, $k = 0$)} \\
> \ddot\phi &= 0 + g\cos 0\sin 0 + 0 = 0 \quad &\text{(poloidal equation at rest, $k = 0$)} \\
> m_P\,\mathbf a_0^P\cdot\mathbf k_2 &= 0 = -m_Pg\cos 0\cos 0 + N \quad &\text{(normal projection at rest: $\mathbf k_0\cdot\mathbf k_2 = \cos\theta\cos\phi$)}
> \end{aligned}$$
>
> $$\boxed{k = 0,\ \theta = \phi = 0,\ \text{at rest}:\ \ddot\theta = \ddot\phi = 0, \quad N = m_Pg}$$
>
> **Units:** $[N] = [m_Pg] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the equations recognise the top as an equilibrium where the torus carries the whole weight, as it must; this confirms the signs of the gravity terms ($g\sin\theta$ and $g\cos\theta\sin\phi$ push $P$ away from the top).

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "Particle P on the torus, attracted by Q on the plane (Problem 38)", "intro": "Data of the statement: m_P = 1 kg, m_Q = 2 kg, k = 2 N/m, g = 9.81 m/s². The view is turned so that its vertical axis k0 is the axis of the torus (the horizontal line through C = (0, 0, 4), parallel to the j0 of the statement) and its origin is C: the axis i0 of the view is the true upward vertical and j0 of the view is the i0 of the statement. The hoop is the section of the tube (radius 1 m, centre 2 m from the axis) in the meridian half-plane of P; the frame slider is θ and the hoop slider q is φ + 90°. The default θ = 90°, q = 180° is the initial point (2, 1, 4) of the statement, and the drag velocity arrow, with the frame rate 0.5 rad/s, is the initial velocity −k0, so it points down the true vertical. Q is not drawn: the readouts hold it at its initial point (3, 1, 0) of the plane z0 = 0.", "params": {"wire": "hoop", "R": 1, "e": 2, "hgt": 0, "Omega": 0.5, "qdot": 0, "extent": 4.5, "g": 9.81, "mP": 1.0, "katt": 2.0, "xi": 3.0, "eta": 1.0}, "defaults": {"psi": 90, "q": 180}, "sliders": {"psi": {"label": "Angle θ about the axis of the torus"}, "q": {"label": "Hoop angle q = φ + 90°"}}, "readouts": [{"label": "ϱ = 2 + cos φ (cos φ = sin q)", "expr": "2 + sin(q)", "unit": "m", "digits": 4}, {"label": "x_P = (2 + cos φ) sin θ", "expr": "(2 + sin(q))*sin(psi)", "unit": "m", "digits": 4}, {"label": "y_P = sin φ", "expr": "-cos(q)", "unit": "m", "digits": 4}, {"label": "z_P = 4 + (2 + cos φ) cos θ", "expr": "4 + (2 + sin(q))*cos(psi)", "unit": "m", "digits": 4}, {"label": "z_P read from the drawing, 4 + x of the view", "expr": "4 + x", "unit": "m", "digits": 4}, {"label": "|PQ|² with Q at its initial point (3, 1, 0)", "expr": "(xi - (2 + sin(q))*sin(psi))^2 + (eta + cos(q))^2 + (4 + (2 + sin(q))*cos(psi))^2", "unit": "m²", "digits": 4}, {"label": "Kinetic energy of P, ½ m_P ϱ²θ̇² (θ̇ = 0.5 rad/s, φ̇ = 0)", "expr": "0.5*mP*(2 + sin(q))^2*Omega^2", "unit": "J", "digits": 4}, {"label": "(f) Initial energy E0 = 19.5 + 4g", "expr": "19.5 + 4*g", "unit": "J", "digits": 2}, {"label": "(g) Least energy with P at the top, 7g + 49", "expr": "7*g + 49", "unit": "J", "digits": 2}]}

---

## Problem 39: Particle on a String with a Plate

### Reference Frames, Bases and Coordinates

A heavy particle $P$ of mass $m$ hangs from a massless inextensible string of length $\ell$ tied at the point $O$ of the upper surface of a thin horizontal plate; the string runs on the plate to the point $Q$ of its straight edge, at the distance $d$ from $O$, and hangs over that edge, sliding on it without friction (Problems.pdf, p. 27). The statement asks for the degrees of freedom, the unit vector from $Q$ to $P$, the kinematics of $Q$ and $P$, the forces on $P$, the equations of motion, the work of the tension and the mechanical energy. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ vertical **upward**, the plate in the plane $z_0 = 0$ |
| Edge of the plate | read from the figure: the straight line $x_0 = d$, $z_0 = 0$, parallel to $\mathbf j_0$ ($Ox_0$ is the perpendicular from $O$ to the edge); the plate occupies $x_0 \lt d$ |
| Basis of the hanging plane | $\mathcal B_1 = \{\mathbf i_1, \mathbf j_0, \mathbf k_1\}$, $\mathcal B_0$ turned by $\phi$ about $-\mathbf j_0$: minus $\mathbf k_1$ is the direction of the line from the edge to $P$ perpendicular to the edge |
| Coordinates | $\theta$: angle from $Ox_0$ to the segment $OQ$, in the plane of the plate; $\phi$: angle from the downward vertical to the line through $P$ perpendicular to the edge, positive away from the plate (towards $\mathbf i_0$), read from the figure |
| Hypotheses | the string is tense, lies straight on the plate from $O$ to $Q$ and straight in the air from $Q$ to $P$; the edge is smooth, so the tension has the same magnitude $T$ on both sides of $Q$ ([Lecture 3, Slide 17]); the hanging length stays positive, $\ell\cos\theta \gt d$ (at $t = 0$ this needs $\ell \gt 2d$) |
| Constraints | inextensible string: $|OQ| + |QP| = \ell$ with $Q$ on the edge (1 equation, holonomic, stationary, unilateral) ([Lecture 3, Slide 21]); the position of $Q$ on the edge is fixed by the balance of the string at the smooth edge (box of part (b)) |
| Degrees of freedom (a) | 3 coordinates of $P$ minus 1 constraint equation: 2, namely $\theta(t)$ and $\phi(t)$ ([Lecture 3, Slide 4]); $Q$ is a geometric point, not a particle, and adds no unknown |
| Data | $m$ [kg], $\ell$ [m], $d$ [m], $g$ [m s$^{-2}$]; at $t = 0$: $\theta = \phi = \pi/3$ and speed of $P$ equal to $\sqrt{\ell g}$ |
| Applied force | weight $-mg\,\mathbf k_0$ |
| Constraint force | tension $T \ge 0$ on $P$, from $P$ towards $Q$ (Notes.pdf, Sec. 7.5); the edge acts on the string only |

![[attachments/EM-SOL/p39-plate.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p39-rotation-j.svg]]

> [!derivation] Basis of the hanging plane: rotation about minus j0
> **Law:** elementary rotation about the second axis, with a negative angle; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19
>
> View of the vertical plane through $P$ perpendicular to the edge, with $\mathbf i_0$ to the right (away from the plate) and $\mathbf k_0$ up: $\mathbf j_0$, the cross product of $\mathbf k_0$ and $\mathbf i_0$, points into the paper (⊗), and a positive rotation about $\mathbf j_0$ is clockwise as seen. The angle $\phi$ goes from the downward vertical towards $\mathbf i_0$: counterclockwise, so the basis is Eq. 1.19 with the angle minus $\phi$ (a positive rotation about minus $\mathbf j_0$, which points out of the paper). $\mathbf i_1$ is $\mathbf i_0$ turned counterclockwise by $\phi$: hypotenuse 1, adjacent leg $\cos\phi$ along $\mathbf i_0$, opposite leg $\sin\phi$ along $\mathbf k_0$. $\mathbf k_1$ is $\mathbf k_0$ turned counterclockwise by $\phi$: adjacent leg $\cos\phi$ along $\mathbf k_0$, opposite leg $\sin\phi$ along minus $\mathbf i_0$, because the upward vector turned counterclockwise leans to the left (the minus sign).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf i_1$)} \\
> \mathbf k_1 &= -\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf k_0 \quad &\text{(right triangle of $\mathbf k_1$: opposite leg on $-\mathbf i_0$)} \\
> \mathbf i_1\times\mathbf j_0 &= \cos\phi\,\mathbf k_0 + \sin\phi\,\mathbf k_0\times\mathbf j_0 = \cos\phi\,\mathbf k_0 - \sin\phi\,\mathbf i_0 = \mathbf k_1 \quad &\text{(right-handed; $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> \det[{}_0R_1] &= \cos\phi\left(\cos\phi\right) - 0 + \left(-\sin\phi\right)\left(0 - \sin\phi\right) = 1 \quad &\text{(expansion along the first row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\phi + 0 + \sin^2\phi = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{13} &= \cos\phi\sin\phi - \sin\phi\cos\phi = 0 \quad &\text{(row 1 times row 3; row 2 is the unit row of $\mathbf j_0$)} \\
> \mathbf k_0 &= \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1 \quad &\text{(third row of the matrix, Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\phi & 0 & -\sin\phi \cr 0 & 1 & 0 \cr \sin\phi & 0 & \cos\phi \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** minus $\mathbf k_1$, equal to $\sin\phi\,\mathbf i_0 - \cos\phi\,\mathbf k_0$, points from the edge down to $P$ at the angle $\phi$ from the vertical; $\mathbf i_1$ is perpendicular to it in the same vertical plane.

> [!derivation] Position of Q and the two lengths of the string
> **Law:** right triangle in the plane of the plate; inextensible string
> **Source:** Notes.pdf, Eq. 2.2; [Lecture 3, Slide 17]; Problems.pdf, p. 27
>
> In the plane of the plate the triangle $O$, foot of the perpendicular on the edge, $Q$ is right-angled at the foot: the hypotenuse is $|OQ|$, the leg adjacent to $\theta$ is $d$ (along $\mathbf i_0$) and the opposite leg is $d\tan\theta$ (along the edge, $\mathbf j_0$).
>
> $$\begin{aligned}
> \mathbf r_0^Q &= d\,\mathbf i_0 + d\tan\theta\,\mathbf j_0 \quad &\text{(the two legs of the triangle)} \\
> |OQ| &= \frac{d}{\cos\theta} \quad &\text{(adjacent leg over the cosine)} \\
> \rho &= |QP| = \ell - \frac{d}{\cos\theta} \quad &\text{(constant total length)} \\
> \rho\cos\theta &= \ell\cos\theta - d \equiv u \quad &\text{(definition of $u$, used below)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^Q = d\,\mathbf i_0 + d\tan\theta\,\mathbf j_0, \qquad \rho = \ell - \frac{d}{\cos\theta}, \qquad u = \ell\cos\theta - d \gt 0}$$
>
> **Units:** $[d] = [\rho] = [u] = [\mathrm{L}]$
> **Meaning:** turning $OQ$ away from $Ox_0$ uses more string on the plate and shortens the hanging part.

> [!derivation] (b) Unit vector from Q to P
> **Law:** balance of the massless string at the smooth edge (no force along the edge); unit norm
> **Source:** Notes.pdf, Sec. 6.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]; Problems.pdf, p. 27
>
> The edge is a smooth straight curve, and the reaction of a smooth curve lies in its normal subspace (Notes.pdf, Sec. 6.5; [Lecture 3, Slide 13]), so the force of the edge on the string at $Q$ is perpendicular to the edge (to $\mathbf j_0$); the massless string at $Q$ is pulled by $T$ towards $O$ and by $T$ towards $P$. The balance along the edge gives the hint of the statement (equal angles of both segments with the edge). The rest of the unit vector lies in the vertical plane perpendicular to the edge, along minus $\mathbf k_1$.
>
> $$\begin{aligned}
> \mathbf e_{QO} &= -\cos\theta\,\mathbf i_0 - \sin\theta\,\mathbf j_0 \quad &\text{(from $Q$ back to $O$: minus the direction of $OQ$)} \\
> T\left(\mathbf e_{QO} + \mathbf e_{QP}\right)\cdot\mathbf j_0 &= 0 \quad &\text{(no force along the edge on the massless string at $Q$)} \\
> \mathbf e_{QP}\cdot\mathbf j_0 &= -\mathbf e_{QO}\cdot\mathbf j_0 = \sin\theta \quad &\text{(divided by $T \gt 0$; $\mathbf e_{QO}\cdot\mathbf j_0 = -\sin\theta$)} \\
> \mathbf e_{QP} &= \sin\theta\,\mathbf j_0 + c\left(-\mathbf k_1\right) \quad &\text{(the rest lies along the line from the edge to $P$)} \\
> c^2 + \sin^2\theta &= 1 \Rightarrow c = \cos\theta \quad &\text{(unit norm; $c \gt 0$ since $P$ hangs below the edge)} \\
> \mathbf e_{QP} &= \sin\theta\,\mathbf j_0 - \cos\theta\left(-\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf k_0\right) \quad &\text{($\mathbf k_1$ in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_{QP} = \cos\theta\sin\phi\,\mathbf i_0 + \sin\theta\,\mathbf j_0 - \cos\theta\cos\phi\,\mathbf k_0 = \sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf k_1}$$
>
> **Units:** dimensionless; $|\mathbf e_{QP}|^2 = \cos^2\theta\left(\sin^2\phi + \cos^2\phi\right) + \sin^2\theta = 1$
> **Meaning:** the hanging segment continues the direction of $OQ$ along the edge: its component along $\mathbf j_0$ equals that of $OQ$, as if the plate were unfolded about the edge.

> [!derivation] Position vector of P
> **Law:** position vector as a sum of partial vectors
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OQ} + \overrightarrow{QP} = d\,\mathbf i_0 + d\tan\theta\,\mathbf j_0 + \rho\left(\sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf k_1\right) \quad &\text{(sum of partial vectors)} \\
> d\tan\theta + \rho\sin\theta &= d\tan\theta + \ell\sin\theta - \frac{d\sin\theta}{\cos\theta} = \ell\sin\theta \quad &\text{(component along $\mathbf j_0$)} \\
> \rho\cos\theta &= u \quad &\text{(component along $-\mathbf k_1$)} \\
> \mathbf r_0^P &= d\,\mathbf i_0 + \ell\sin\theta\,\mathbf j_0 - u\,\mathbf k_1 \quad &\text{(both components substituted)} \\
> &= \left(d + u\sin\phi\right)\mathbf i_0 + \ell\sin\theta\,\mathbf j_0 - u\cos\phi\,\mathbf k_0 \quad &\text{($\mathbf k_1$ in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = d\,\mathbf i_0 + \ell\sin\theta\,\mathbf j_0 - \left(\ell\cos\theta - d\right)\mathbf k_1, \qquad z_P = -\left(\ell\cos\theta - d\right)\cos\phi}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** $P$ sits on the vertical plane perpendicular to the edge at the abscissa $\ell\sin\theta$ along the edge, at the distance $u$ from the edge, swung out by $\phi$; in the right triangle of that distance the vertical leg is $u\cos\phi$ (adjacent to $\phi$) and the horizontal leg $u\sin\phi$ (opposite).

### Kinematics

> [!derivation] Derivatives of the basis of the hanging plane
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= -\dot\phi\,\mathbf j_0 \quad &\text{(rotation by $\phi$ about $-\mathbf j_0$)} \\
> \dot{\mathbf i}_1 &= -\dot\phi\,\mathbf j_0\times\left(\cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf k_0\right) = -\dot\phi\left(-\cos\phi\,\mathbf k_0 + \sin\phi\,\mathbf i_0\right) = \dot\phi\,\mathbf k_1 \quad &\text{($\mathbf j_0\times\mathbf i_0 = -\mathbf k_0$, $\mathbf j_0\times\mathbf k_0 = \mathbf i_0$)} \\
> \dot{\mathbf k}_1 &= -\dot\phi\,\mathbf j_0\times\left(-\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf k_0\right) = -\dot\phi\left(\sin\phi\,\mathbf k_0 + \cos\phi\,\mathbf i_0\right) = -\dot\phi\,\mathbf i_1 \quad &\text{(same products)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_1 = \dot\phi\,\mathbf k_1, \qquad \dot{\mathbf k}_1 = -\dot\phi\,\mathbf i_1, \qquad \dot{\mathbf j}_0 = \mathbf 0}$$
>
> **Units:** $[\dot\phi] = [\mathrm{T^{-1}}]$
> **Meaning:** the hanging plane does not turn; only the direction of the swing inside it changes.

> [!derivation] (c) Velocity and acceleration of Q
> **Law:** time derivatives in $S_0$; chain and quotient rules
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4
>
> $$\begin{aligned}
> \frac{d}{dt}\tan\theta &= \frac{\dot\theta}{\cos^2\theta} \quad &\text{(chain rule; derivative of the tangent)} \\
> \mathbf v_0^Q &= \frac{d\dot\theta}{\cos^2\theta}\,\mathbf j_0 \quad &\text{($d\,\mathbf i_0$ is constant)} \\
> \frac{d}{dt}\left(\frac{\dot\theta}{\cos^2\theta}\right) &= \frac{\ddot\theta\cos^2\theta - \dot\theta\cdot 2\cos\theta\left(-\sin\theta\right)\dot\theta}{\cos^4\theta} = \frac{\ddot\theta\cos\theta + 2\dot\theta^2\sin\theta}{\cos^3\theta} \quad &\text{(quotient rule; chain rule on $\cos^2\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^Q = d\,\mathbf i_0 + d\tan\theta\,\mathbf j_0, \quad \mathbf v_0^Q = \frac{d\dot\theta}{\cos^2\theta}\,\mathbf j_0, \quad \mathbf a_0^Q = \frac{d\left(\ddot\theta\cos\theta + 2\dot\theta^2\sin\theta\right)}{\cos^3\theta}\,\mathbf j_0}$$
>
> **Units:** $[d\dot\theta] = [\mathrm{L\,T^{-1}}]$, $[d\ddot\theta] = [d\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the contact point slides along the edge only.

> [!derivation] (c) Velocity and acceleration of P
> **Law:** time derivatives in $S_0$; product and chain rules
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \dot u &= -\ell\sin\theta\,\dot\theta \quad &\text{(chain rule on $\ell\cos\theta - d$)} \\
> \mathbf v_0^P &= \ell\cos\theta\,\dot\theta\,\mathbf j_0 - \dot u\,\mathbf k_1 - u\,\dot{\mathbf k}_1 \quad &\text{(product rule; $d\,\mathbf i_0$ constant)} \\
> &= u\dot\phi\,\mathbf i_1 + \ell\dot\theta\cos\theta\,\mathbf j_0 + \ell\dot\theta\sin\theta\,\mathbf k_1 \quad &\text{($\dot u$ and the derivative of $\mathbf k_1$ substituted)} \\
> \frac{d}{dt}\left(u\dot\phi\,\mathbf i_1\right) &= \left(u\ddot\phi - \ell\sin\theta\,\dot\theta\dot\phi\right)\mathbf i_1 + u\dot\phi^2\,\mathbf k_1 \quad &\text{(product rule; derivative of $\mathbf i_1$)} \\
> \frac{d}{dt}\left(\ell\dot\theta\cos\theta\,\mathbf j_0\right) &= \ell\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf j_0 \quad &\text{(product and chain rules)} \\
> \frac{d}{dt}\left(\ell\dot\theta\sin\theta\,\mathbf k_1\right) &= \ell\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right)\mathbf k_1 - \ell\dot\theta\dot\phi\sin\theta\,\mathbf i_1 \quad &\text{(product rule; derivative of $\mathbf k_1$)} \\
> \mathbf a_0^P &= \left(u\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi\right)\mathbf i_1 + \ell\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf j_0 + \left[\ell\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right) + u\dot\phi^2\right]\mathbf k_1 \quad &\text{(sum of the three derivatives)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf v_0^P = \left(\ell\cos\theta - d\right)\dot\phi\,\mathbf i_1 + \ell\dot\theta\left(\cos\theta\,\mathbf j_0 + \sin\theta\,\mathbf k_1\right) \cr \mathbf a_0^P = \left[\left(\ell\cos\theta - d\right)\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi\right]\mathbf i_1 + \ell\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf j_0 + \left[\ell\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right) + \left(\ell\cos\theta - d\right)\dot\phi^2\right]\mathbf k_1 \end{array}}$$
>
> **Units:** $[u\dot\phi] = [\ell\dot\theta] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity has two orthogonal parts: the swing $u\dot\phi$ in the hanging plane and $\ell\dot\theta$ along $\cos\theta\,\mathbf j_0 + \sin\theta\,\mathbf k_1$, which is perpendicular to the string; so the speed squared is $\ell^2\dot\theta^2 + u^2\dot\phi^2$.

### Forces and Equations of Motion

The free-body diagram of $P$ shows its weight and the tension of the string, from $P$ towards $Q$. $S_0$ is inertial, so no inertia force acts; the plate and its edge act only on the string.

![[attachments/EM-SOL/p39-fbd.svg]]

> [!derivation] (d) Forces on P and a basis adapted to the string
> **Law:** weight; tension of a massless string along the string, pulling
> **Source:** Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]
>
> The unit vector $\mathbf e_\perp$, equal to $\cos\theta\,\mathbf j_0 + \sin\theta\,\mathbf k_1$, completes with $\mathbf i_1$ and $\mathbf e_{QP}$ an orthonormal triad: both $\mathbf i_1$ and $\mathbf e_\perp$ are perpendicular to the string.
>
> $$\begin{aligned}
> \mathbf T &= -T\,\mathbf e_{QP}, \quad T \ge 0 \quad &\text{(from $P$ towards $Q$; a string can only pull)} \\
> \mathbf e_\perp\cdot\mathbf e_{QP} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{($\mathbf e_\perp$ perpendicular to the string)} \\
> \mathbf i_1\cdot\mathbf e_{QP} &= \mathbf i_1\cdot\left(\sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf k_1\right) = 0 \quad &\text{($\mathbf i_1$ perpendicular to the string)} \\
> -mg\,\mathbf k_0\cdot\mathbf i_1 &= -mg\sin\phi \quad &\text{($\mathbf k_0 = \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf k_1$)} \\
> -mg\,\mathbf k_0\cdot\mathbf e_\perp &= -mg\cos\phi\,\mathbf k_1\cdot\left(\sin\theta\,\mathbf k_1\right) = -mg\cos\phi\sin\theta \quad &\text{(same expression of $\mathbf k_0$)} \\
> -mg\,\mathbf k_0\cdot\mathbf e_{QP} &= -mg\cos\phi\,\mathbf k_1\cdot\left(-\cos\theta\,\mathbf k_1\right) = mg\cos\phi\cos\theta \quad &\text{(same expression of $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -mg\,\mathbf k_0 - T\,\mathbf e_{QP} = -mg\sin\phi\,\mathbf i_1 - mg\sin\theta\cos\phi\,\mathbf e_\perp + \left(mg\cos\theta\cos\phi - T\right)\mathbf e_{QP}}$$
>
> **Units:** $[mg] = [T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the tension appears only along $\mathbf e_{QP}$; the projections on $\mathbf i_1$ and $\mathbf e_\perp$ are free of it.

> [!derivation] (e) Equations of motion for the two angles
> **Law:** Newton's second law in an inertial frame, projected on the two directions perpendicular to the string
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\mathbf i_1 &= u\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi \quad &\text{(component along $\mathbf i_1$)} \\
> \mathbf a_0^P\cdot\mathbf e_\perp &= \ell\cos^2\theta\,\ddot\theta - \ell\cos\theta\sin\theta\,\dot\theta^2 + \ell\sin^2\theta\,\ddot\theta + \ell\sin\theta\cos\theta\,\dot\theta^2 + u\sin\theta\,\dot\phi^2 \quad &\text{(components on $\mathbf j_0$, $\mathbf k_1$ times $\cos\theta$, $\sin\theta$)} \\
> &= \ell\ddot\theta + u\sin\theta\,\dot\phi^2 \quad &\text{($\cos^2\theta + \sin^2\theta = 1$; the $\dot\theta^2$ terms cancel)} \\
> \mathbf i_1:\ m\left(u\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi\right) &= -mg\sin\phi \quad &\text{(Newton, no tension)} \\
> \mathbf e_\perp:\ m\left(\ell\ddot\theta + u\sin\theta\,\dot\phi^2\right) &= -mg\sin\theta\cos\phi \quad &\text{(Newton, no tension)} \\
> \mathbf e_{QP}:\ -m\left(\ell\dot\theta^2 + u\cos\theta\,\dot\phi^2\right) &= mg\cos\theta\cos\phi - T \quad &\text{($\mathbf a_0^P\cdot\mathbf e_{QP}$ by the same products)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \ell\ddot\theta + \left(\ell\cos\theta - d\right)\sin\theta\,\dot\phi^2 + g\sin\theta\cos\phi = 0 \cr \left(\ell\cos\theta - d\right)\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi + g\sin\phi = 0 \cr T = m\left[\ell\dot\theta^2 + \left(\ell\cos\theta - d\right)\cos\theta\,\dot\phi^2\right] + mg\cos\theta\cos\phi \end{array}}$$
>
> **Units:** $[\ell\ddot\theta] = [u\dot\phi^2] = [g] = [\mathrm{L\,T^{-2}}]$; $[T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three equations for $\theta$, $\phi$ and $T$; the first two contain only the angles and give the motion, the third the tension, which must stay positive.

### Answers and Checks

#### (f) Work of the tension

> [!derivation] Power of the tension on P
> **Law:** power of a force, the dot product with the velocity
> **Source:** Notes.pdf, Eq. 4.11; [Lecture 3, Slide 16]; Problems.pdf, p. 76
>
> $$\begin{aligned}
> \mathbf e_{QP}\cdot\mathbf v_0^P &= \left(\sin\theta\,\mathbf j_0 - \cos\theta\,\mathbf k_1\right)\cdot\left(u\dot\phi\,\mathbf i_1 + \ell\dot\theta\cos\theta\,\mathbf j_0 + \ell\dot\theta\sin\theta\,\mathbf k_1\right) \quad &\text{(the two vectors in $\mathcal B_1$)} \\
> &= \ell\dot\theta\sin\theta\cos\theta - \ell\dot\theta\cos\theta\sin\theta = 0 \quad &\text{(orthonormal $\mathcal B_1$)} \\
> \dot W_T &= -T\,\mathbf e_{QP}\cdot\mathbf v_0^P = 0 \quad &\text{(power of the tension)}
> \end{aligned}$$
>
> $$\boxed{\mathbf T\cdot\mathbf v_0^P = 0 \ \text{for every motion: the tension does no work on } P}$$
>
> **Units:** power $[\mathrm{M\,L^2\,T^{-3}}]$, identically zero
> **Meaning:** $P$ never moves along the string: the plate is fixed and the string slides freely over the edge, so the constraint is stationary and its force is normal to every possible velocity.

#### (g) Mechanical energy

> [!derivation] Mechanical energy of P, its initial value and its conservation
> **Law:** theorem of kinetic energy; potential of the weight; zero power of the tension
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\tfrac12 m|\mathbf v_0^P|^2\right) &= -mg\,\mathbf k_0\cdot\mathbf v_0^P + 0 = -\frac{d}{dt}\left(mg\,z_P\right) \quad &\text{(power of the weight and of the tension)} \\
> |\mathbf v_0^P|^2 &= u^2\dot\phi^2 + \ell^2\dot\theta^2\left(\cos^2\theta + \sin^2\theta\right) = \ell^2\dot\theta^2 + u^2\dot\phi^2 \quad &\text{(orthonormal $\mathcal B_1$)} \\
> E &= \tfrac12 m\left(\ell^2\dot\theta^2 + u^2\dot\phi^2\right) - mg\,u\cos\phi \quad &\text{(kinetic plus potential energy; $z_P = -u\cos\phi$)} \\
> u(0) &= \ell\cos\tfrac{\pi}{3} - d = \tfrac{\ell}{2} - d \quad &\text{($\cos\frac{\pi}{3} = \frac12$)} \\
> z_P(0) &= -\left(\tfrac{\ell}{2} - d\right)\cos\tfrac{\pi}{3} = -\tfrac{\ell}{4} + \tfrac{d}{2} \quad &\text{(height of $P$ at $t = 0$)} \\
> E(0) &= \tfrac12 m\ell g - mg\left(\tfrac{\ell}{4} - \tfrac{d}{2}\right) = \frac{mg\ell}{4} + \frac{mgd}{2} \quad &\text{(speed squared $\ell g$ at $t = 0$)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12 m\left[\ell^2\dot\theta^2 + \left(\ell\cos\theta - d\right)^2\dot\phi^2\right] - mg\left(\ell\cos\theta - d\right)\cos\phi = \frac{mg\ell}{4} + \frac{mgd}{2} = \text{const}}$$
>
> **Units:** $[m\ell^2\dot\theta^2] = [mg\ell] = [mgd] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the energy is conserved: the weight is conservative and the only other force, the tension, does no work (part (f)), because the plate is at rest.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 2: $\theta$ and $\phi$ |
| (b) Unit vector $Q \to P$ | $\mathbf e_{QP} = \cos\theta\sin\phi\,\mathbf i_0 + \sin\theta\,\mathbf j_0 - \cos\theta\cos\phi\,\mathbf k_0$ |
| (c) Kinematics | $\mathbf r_0^Q = d\,\mathbf i_0 + d\tan\theta\,\mathbf j_0$, $\mathbf v_0^Q = d\dot\theta\cos^{-2}\theta\,\mathbf j_0$, $\mathbf a_0^Q = d(\ddot\theta\cos\theta + 2\dot\theta^2\sin\theta)\cos^{-3}\theta\,\mathbf j_0$; $\mathbf r_0^P = (d + u\sin\phi)\,\mathbf i_0 + \ell\sin\theta\,\mathbf j_0 - u\cos\phi\,\mathbf k_0$ with $u = \ell\cos\theta - d$; $\mathbf v_0^P = (\ell\cos\theta - d)\dot\phi\,\mathbf i_1 + \ell\dot\theta(\cos\theta\,\mathbf j_0 + \sin\theta\,\mathbf k_1)$, $\mathbf a_0^P = [(\ell\cos\theta - d)\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi]\,\mathbf i_1 + \ell(\ddot\theta\cos\theta - \dot\theta^2\sin\theta)\,\mathbf j_0 + [\ell(\ddot\theta\sin\theta + \dot\theta^2\cos\theta) + (\ell\cos\theta - d)\dot\phi^2]\,\mathbf k_1$, in the basis $\mathbf i_1 = \cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf k_0$, $\mathbf j_0$, $\mathbf k_1 = -\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf k_0$ |
| (d) Forces on $P$ | weight $-mg\,\mathbf k_0$; tension $-T\,\mathbf e_{QP}$, $T \ge 0$ |
| (e) Equations of motion | $\ell\ddot\theta + (\ell\cos\theta - d)\sin\theta\,\dot\phi^2 + g\sin\theta\cos\phi = 0$; $(\ell\cos\theta - d)\ddot\phi - 2\ell\sin\theta\,\dot\theta\dot\phi + g\sin\phi = 0$ |
| (f) Work of the tension | none: $\mathbf e_{QP}\cdot\mathbf v_0^P = 0$ identically |
| (g) Mechanical energy | $E = \frac12 m[\ell^2\dot\theta^2 + (\ell\cos\theta - d)^2\dot\phi^2] - mg(\ell\cos\theta - d)\cos\phi$; $E(0) = mg\ell/4 + mgd/2$; conserved |

**Check against the official key:** Problems.pdf, p. 76, item 39, answers only part (f): the tension does no work, which is proved with the dot product of the unit vector of the string and the velocity of $P$ vanishing; the box of part (f) is that proof (**match**). The other parts have no key; the limiting cases below are independent checks.

> [!derivation] Limiting case: motion in the vertical plane through Ox0
> **Law:** an invariant solution of the equations of motion
> **Source:** Notes.pdf, Sec. 4.7; Notes.pdf, Eq. 4.4
>
> With $\theta$ identically zero, $Q$ stays at the foot $(d, 0, 0)$ of the perpendicular and the string hangs from the edge in the plane $y_0 = 0$.
>
> $$\begin{aligned}
> \ell\cdot 0 + \left(\ell - d\right)\cdot 0\cdot\dot\phi^2 + g\cdot 0\cdot\cos\phi &= 0 \quad &\text{(first equation with $\theta \equiv 0$: satisfied for every $\phi(t)$)} \\
> \left(\ell - d\right)\ddot\phi - 0 + g\sin\phi &= 0 \quad &\text{(second equation with $\theta \equiv 0$)} \\
> T &= m\left(\ell - d\right)\dot\phi^2 + mg\cos\phi \quad &\text{(tension with $\theta \equiv 0$)}
> \end{aligned}$$
>
> $$\boxed{\theta \equiv 0:\quad \ddot\phi + \frac{g}{\ell - d}\sin\phi = 0, \qquad T = m\left(\ell - d\right)\dot\phi^2 + mg\cos\phi}$$
>
> **Units:** $[g/(\ell - d)] = [\mathrm{T^{-2}}]$; $[T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** a simple pendulum of length $\ell - d$ hanging from the edge, with its classical tension (Notes.pdf, Sec. 4.7): the general equations contain the expected special case.

> [!derivation] Limiting case: edge through the anchor point
> **Law:** the results with the distance d set to zero
> **Source:** Notes.pdf, Sec. 4.7
>
> $$\begin{aligned}
> d &\to 0:\quad \rho = \ell, \quad u = \ell\cos\theta \quad &\text{($Q$ coincides with $O$)} \\
> \mathbf r_0^P &= \ell\left(\cos\theta\sin\phi\,\mathbf i_0 + \sin\theta\,\mathbf j_0 - \cos\theta\cos\phi\,\mathbf k_0\right) = \ell\,\mathbf e_{QP} \quad &\text{(position box)} \\
> E(0) &= \frac{mg\ell}{4} + 0 = \tfrac12 m\ell g - mg\ell\cos\tfrac{\pi}{3}\cos\tfrac{\pi}{3} \quad &\text{(energy box)}
> \end{aligned}$$
>
> $$\boxed{d \to 0:\ |\mathbf r_0^P| = \ell, \quad E(0) = \frac{mg\ell}{4}}$$
>
> **Units:** $[\mathrm{L}]$; $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** $P$ stays on the sphere of radius $\ell$ centred at $O$: a spherical pendulum described by two angles, whose height is $-\ell\cos\theta\cos\phi$; the energy matches the general value with zero $d$.

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "String over the edge of the plate, φ held at π/3 (Problem 39)", "intro": "The statement gives no lengths: sample values ℓ = 2 m, d = 0.5 m, m = 1 kg, g = 9.81 m/s², with the angles of the start, θ = φ = π/3. The plate is the plane z0 = 0 on the side x0 below d. The wire of the archetype is the edge of the plate, the line x0 = d of that plane, and the dot the archetype labels P is the point Q where the string crosses the edge; its arrow r is the string OQ on the plate. The blue arrow QP is the hanging string, with the particle at its tip. The archetype has one moving coordinate: the slider q is the position of Q along the edge, d tan θ, so it sets θ (default π/3), and φ is held at its initial value π/3. Keep the frame slider at zero: the plate does not turn.", "params": {"wire": "chord", "d": 0.5, "Omega": 0, "qdot": 0, "qmin": -1.9, "qmax": 1.9, "extent": 1.8, "ell": 2.0, "m": 1.0, "g": 9.81, "phi0": 1.047197551}, "defaults": {"psi": 0, "q": 0.866025}, "sliders": {"psi": {"label": "Frame angle (keep at 0)"}, "q": {"label": "Position of Q on the edge, d tan θ (m)", "min": -1.9, "max": 1.9, "step": 0.001}}, "readouts": [{"label": "Angle θ = arctan(y_Q/d)", "expr": "deg(atan(q/d))", "unit": "deg", "digits": 2}, {"label": "|OQ| = d/cos θ", "expr": "d/cos(atan(q/d))", "unit": "m", "digits": 4}, {"label": "|OQ| read from the drawing", "expr": "sqrt(x^2 + y^2)", "unit": "m", "digits": 4}, {"label": "Hanging length ρ = ℓ − d/cos θ", "expr": "ell - d/cos(atan(q/d))", "unit": "m", "digits": 4}, {"label": "u = ℓ cos θ − d (distance of P from the edge)", "expr": "(ell*cos(atan(q/d)) - d)", "unit": "m", "digits": 4}, {"label": "x_P = d + u sin φ", "expr": "d + (ell*cos(atan(q/d)) - d)*sin(phi0)", "unit": "m", "digits": 4}, {"label": "y_P = ℓ sin θ", "expr": "ell*sin(atan(q/d))", "unit": "m", "digits": 4}, {"label": "z_P = −(ℓ cos θ − d) cos φ", "expr": "-(ell*cos(atan(q/d)) - d)*cos(phi0)", "unit": "m", "digits": 4}, {"label": "(b) e_QP · i0 = cos θ sin φ", "expr": "cos(atan(q/d))*sin(phi0)", "unit": "", "digits": 4}, {"label": "(g) Potential energy −mg u cos φ", "expr": "-m*g*(ell*cos(atan(q/d)) - d)*cos(phi0)", "unit": "J", "digits": 4}, {"label": "(g) Initial energy E(0) = mgℓ/4 + mgd/2", "expr": "m*g*ell/4 + m*g*d/2", "unit": "J", "digits": 4}, {"label": "Initial kinetic energy ½ m ℓ g (speed √(ℓg))", "expr": "0.5*m*ell*g", "unit": "J", "digits": 4}, {"label": "Pendulum frequency of the case θ = 0, √(g/(ℓ − d))", "expr": "sqrt(g/(ell - d))", "unit": "rad/s", "digits": 4}], "vectors": [{"label": "QP", "at": ["x", "y", "0"], "comp": ["(ell*cos(atan(q/d)) - d)*sin(phi0)", "ell*sin(atan(q/d)) - q", "-(ell*cos(atan(q/d)) - d)*cos(phi0)"], "scale": 1, "cls": "m3-b1 m3-mid"}]}

---

## Problem 48: Two Connected Particles, One on Paraboloid

### Reference Frames, Bases and Coordinates

Two heavy particles $P$ and $Q$ of mass $m$ are joined by an inextensible massless string of length $\ell$ that passes through a small hole at the vertex $O$ of a paraboloid; $P$ moves without friction on the paraboloid of height $cR^2$ at the radius $R$ and $Q$ hangs on the vertical axis below $O$ (Problems.pdf, p. 33). The statement asks for the degrees of freedom, the kinematics, a normal and two tangent vectors of the paraboloid, the forces, the condition for a tense string, the equations of motion for $R$ and $\theta$, two first integrals and the equation of the extreme radii. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the vertex of the paraboloid and the hole (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $\mathbf k_0$ vertical **upward**, along the axis of the paraboloid |
| Cylindrical basis | $\mathcal B_1 = \{\mathbf e_R, \mathbf e_\theta, \mathbf k_0\}$, $\mathcal B_0$ turned by $\theta$ about $\mathbf k_0$; $\mathbf e_R$ horizontal, towards the meridian plane of $P$ (Notes.pdf, Eq. 2.24) |
| Coordinates | $R$, distance from $P$ to the axis, and $\theta$, azimuth of $P$ from $\mathbf i_0$ (statement) |
| Hypotheses | $c \gt 0$ (the paraboloid opens upwards, figure); the string is straight from $O$ to $P$ (the bowl is convex, so the chord $OP$ does not touch the surface), always tense, and $Q$ never reaches $O$ (statement); no friction anywhere |
| Constraints | $P$ on the paraboloid, $z_P = cR^2$ (1 equation, holonomic, stationary, smooth, bilateral: $P$ is constrained to stay on it); $Q$ on the axis, $x_Q = y_Q = 0$ (2 equations, holonomic, stationary, smooth, bilateral); string, $|OP| + |OQ| = \ell$ (1 equation joining the particles, holonomic, stationary, **unilateral**) ([Lecture 3, Slide 17]; [Lecture 3, Slide 21]) |
| Degrees of freedom (a) | 6 coordinates of two particles minus 4 constraint equations: 2 effective degrees of freedom, $R(t)$ and $\theta(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $\ell$ [m], $c$ [m$^{-1}$], $g$ [m s$^{-2}$]; for part (h), $R(0) = 1/c$, $\theta(0) = 0$, $\dot R(0) = 0$, $\dot\theta(0) = d$ [s$^{-1}$], $d \ne 0$ |
| Applied forces | weights $-mg\,\mathbf k_0$ on each particle |
| Constraint forces | on $P$: tension towards $O$ and normal reaction of the paraboloid; on $Q$: tension along $\mathbf k_0$ and the reaction of the guide, normal to the axis; the same tension $T$ at both ends (massless string, small smooth hole, [Lecture 3, Slide 17]) |

![[attachments/EM-SOL/p48-meridian.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p48-rotation-k.svg]]

> [!derivation] Cylindrical basis: rotation about k0
> **Law:** elementary rotation about the third axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 2.24
>
> View from above along $\mathbf k_0$, which points out of the paper (⊙) with $\mathbf i_0$ to the right and $\mathbf j_0$ up; positive angles are counterclockwise. $\mathbf e_R$ is $\mathbf i_0$ turned by $\theta$: hypotenuse 1, adjacent leg $\cos\theta$ along $\mathbf i_0$, opposite leg $\sin\theta$ along $\mathbf j_0$. $\mathbf e_\theta$ is $\mathbf j_0$ turned by $\theta$: adjacent leg $\cos\theta$ along $\mathbf j_0$, opposite leg $\sin\theta$ along minus $\mathbf i_0$ (the upward vector turned counterclockwise leans to the left: the minus sign).
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf e_R$)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(right triangle of $\mathbf e_\theta$: opposite leg on $-\mathbf i_0$)} \\
> \mathbf e_R\times\mathbf e_\theta &= \left(\cos^2\theta + \sin^2\theta\right)\mathbf k_0 = \mathbf k_0 \quad &\text{(right-handed)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos^2\theta + \sin^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta - \sin\theta\cos\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** $\mathbf e_R$ and $\mathbf k_0$ span the meridian plane of $P$, where the string, the weight and the normal reaction all lie.

> [!derivation] Position vectors and the length of string on each side
> **Law:** position vectors with the constraints substituted; Pythagoras in the meridian triangle; inextensible string
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.28; [Lecture 3, Slide 17]
>
> In the meridian plane the segment $OP$ is the hypotenuse of the right triangle with the horizontal leg $R$ (along $\mathbf e_R$) and the vertical leg $cR^2$ (along $\mathbf k_0$).
>
> $$\begin{aligned}
> \mathbf r_0^P &= R\,\mathbf e_R + cR^2\,\mathbf k_0 \quad &\text{(cylindrical position with $z = cR^2$)} \\
> \rho &= |OP| = \sqrt{R^2 + c^2R^4} = R\sqrt{1 + c^2R^2} \quad &\text{(hypotenuse of the meridian triangle; $R \ge 0$)} \\
> |OQ| &= \ell - \rho \quad &\text{(inextensible string)} \\
> \mathbf r_0^Q &= -\left(\ell - \rho\right)\mathbf k_0 \quad &\text{(on the axis, below $O$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_R + cR^2\,\mathbf k_0, \qquad \mathbf r_0^Q = -\left(\ell - R\sqrt{1 + c^2R^2}\right)\mathbf k_0}$$
>
> **Units:** $[cR^2] = [\mathrm{L^{-1}}][\mathrm{L^2}] = [\mathrm{L}]$; $cR$ is dimensionless
> **Meaning:** when $P$ climbs the bowl (larger $R$), the string on its side lengthens and $Q$ rises by the same amount.

> [!derivation] Derivatives of the length of string on the side of P
> **Law:** chain rule; quotient rule
> **Source:** Notes.pdf, Eq. 2.3
>
> Write $w$ for the square root of $1 + c^2R^2$, so that $\rho = Rw$ and $\rho'$, $\rho''$ denote derivatives with respect to $R$.
>
> $$\begin{aligned}
> w' &= \frac{1}{2w}\cdot 2c^2R = \frac{c^2R}{w} \quad &\text{(chain rule on the square root)} \\
> \rho' &= w + Rw' = w + \frac{c^2R^2}{w} = \frac{1 + 2c^2R^2}{w} \quad &\text{(product rule; common denominator $w$)} \\
> \rho'' &= \frac{4c^2R\,w - \left(1 + 2c^2R^2\right)w'}{w^2} = \frac{4c^2R\,w^2 - \left(1 + 2c^2R^2\right)c^2R}{w^3} \quad &\text{(quotient rule; $w'$ substituted, times $w/w$)} \\
> &= \frac{c^2R\left[4 + 4c^2R^2 - 1 - 2c^2R^2\right]}{w^3} = \frac{c^2R\left(3 + 2c^2R^2\right)}{w^3} \quad &\text{($w^2 = 1 + c^2R^2$)} \\
> \dot\rho &= \rho'\dot R \quad &\text{(chain rule)} \\
> \ddot\rho &= \rho''\dot R\cdot\dot R + \rho'\ddot R \quad &\text{(product rule; chain rule on $\rho'(R)$)}
> \end{aligned}$$
>
> $$\boxed{\rho' = \frac{1 + 2c^2R^2}{\sqrt{1 + c^2R^2}}, \qquad \rho'' = \frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}}}$$
>
> **Units:** $\rho'$ dimensionless; $[\rho''] = [c^2R] = [\mathrm{L^{-1}}]$
> **Meaning:** $\rho'$ is at least 1: the string on the side of $P$ grows at least as fast as the radius.

### Kinematics

> [!derivation] (b) Position, velocity and acceleration of both particles
> **Law:** time derivatives in $S_0$; derivatives of the cylindrical unit vectors; product rule
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4
>
> $$\begin{aligned}
> \dot{\mathbf e}_R &= \dot\theta\,\mathbf k_0\times\mathbf e_R = \dot\theta\,\mathbf e_\theta \quad &\text{($\mathcal B_1$ turns about $\mathbf k_0$ with $\theta$; $\mathbf k_0\times\mathbf e_R = \mathbf e_\theta$)} \\
> \dot{\mathbf e}_\theta &= \dot\theta\,\mathbf k_0\times\mathbf e_\theta = -\dot\theta\,\mathbf e_R \quad &\text{($\mathbf k_0\times\mathbf e_\theta = -\mathbf e_R$)} \\
> \mathbf v_0^P &= \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + 2cR\dot R\,\mathbf k_0 \quad &\text{(product rule; chain rule on $cR^2$)} \\
> \mathbf a_0^P &= \ddot R\,\mathbf e_R + \dot R\dot\theta\,\mathbf e_\theta + \left(\dot R\dot\theta + R\ddot\theta\right)\mathbf e_\theta - R\dot\theta^2\,\mathbf e_R + 2c\left(\dot R^2 + R\ddot R\right)\mathbf k_0 \quad &\text{(product rule on each term)} \\
> &= \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(R\ddot\theta + 2\dot R\dot\theta\right)\mathbf e_\theta + 2c\left(\dot R^2 + R\ddot R\right)\mathbf k_0 \quad &\text{(grouped)} \\
> \mathbf v_0^Q &= \dot\rho\,\mathbf k_0 = \rho'\dot R\,\mathbf k_0 \quad &\text{($\ell$ constant; chain rule on $\rho$)} \\
> \mathbf a_0^Q &= \ddot\rho\,\mathbf k_0 = \left(\rho'\ddot R + \rho''\dot R^2\right)\mathbf k_0 \quad &\text{(product and chain rules)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^P = R\,\mathbf e_R + cR^2\,\mathbf k_0, \quad \mathbf v_0^P = \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + 2cR\dot R\,\mathbf k_0 \cr \mathbf a_0^P = \left(\ddot R - R\dot\theta^2\right)\mathbf e_R + \left(R\ddot\theta + 2\dot R\dot\theta\right)\mathbf e_\theta + 2c\left(\dot R^2 + R\ddot R\right)\mathbf k_0 \cr \mathbf r_0^Q = -\left(\ell - \rho\right)\mathbf k_0, \quad \mathbf v_0^Q = \rho'\dot R\,\mathbf k_0, \quad \mathbf a_0^Q = \left(\rho'\ddot R + \rho''\dot R^2\right)\mathbf k_0 \end{array}}$$
>
> **Units:** $[\dot R] = [R\dot\theta] = [cR\dot R] = [\mathrm{L\,T^{-1}}]$; every acceleration term $[\mathrm{L\,T^{-2}}]$, e.g. $[\rho''\dot R^2] = [\mathrm{L^{-1}}][\mathrm{L^2\,T^{-2}}]$
> **Meaning:** these are the derivatives of the cylindrical position with $z = cR^2$; $Q$ moves only along the axis, at the rate at which the string on the side of $P$ changes.

> [!derivation] (c) Tangent and normal vectors of the paraboloid
> **Law:** tangent vectors as partial derivatives of the parametric form; normal as their cross product
> **Source:** [Lecture 3, Slide 9]; Notes.pdf, Sec. 6.3
>
> $$\begin{aligned}
> \mathbf t_R &= \frac{\partial\mathbf r_0^P}{\partial R} = \mathbf e_R + 2cR\,\mathbf k_0 \quad &\text{(derivative at constant $\theta$)} \\
> \mathbf t_\theta &= \frac{\partial\mathbf r_0^P}{\partial\theta} = R\,\frac{\partial\mathbf e_R}{\partial\theta} = R\,\mathbf e_\theta \quad &\text{(derivative at constant $R$)} \\
> \mathbf t_R\times\mathbf t_\theta &= R\,\mathbf e_R\times\mathbf e_\theta + 2cR^2\,\mathbf k_0\times\mathbf e_\theta = R\,\mathbf k_0 - 2cR^2\,\mathbf e_R \quad &\text{($\mathbf k_0\times\mathbf e_\theta = -\mathbf e_R$)} \\
> \hat{\mathbf n} &= \frac{-2cR\,\mathbf e_R + \mathbf k_0}{\sqrt{1 + 4c^2R^2}} \quad &\text{(normalised; it points into the bowl)}
> \end{aligned}$$
>
> $$\boxed{\mathbf t_R = \mathbf e_R + 2cR\,\mathbf k_0, \qquad \mathbf t_\theta = R\,\mathbf e_\theta, \qquad \mathbf n = R\left(-2cR\,\mathbf e_R + \mathbf k_0\right)}$$
>
> **Units:** $\mathbf t_R$ dimensionless; $[\mathbf t_\theta] = [\mathbf n] = [\mathrm{L}]$
> **Meaning:** the meridian tangent rises with the slope $2cR$ (right triangle of legs 1 and $2cR$ in the meridian figure); the normal is perpendicular to both tangents, and only along it can the smooth paraboloid push.

### Forces and Equations of Motion

The free-body diagrams show on $P$ its weight, the tension towards the hole and the normal reaction; on $Q$ its weight, the tension upwards and the reaction of the guide. $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p48-fbd.svg]]

> [!derivation] (d) Forces on both particles
> **Law:** weight; tension of a massless string through a smooth hole; reactions in the normal subspaces
> **Source:** Notes.pdf, Sec. 6.4; Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]
>
> In the meridian triangle of $OP$ the cosine of the angle of the string with the horizontal is $R/\rho$ (adjacent leg over hypotenuse) and its sine is $cR^2/\rho$ (opposite leg over hypotenuse).
>
> $$\begin{aligned}
> -\frac{\mathbf r_0^P}{\rho} &= -\frac{R}{\rho}\,\mathbf e_R - \frac{cR^2}{\rho}\,\mathbf k_0 \quad &\text{(unit vector from $P$ towards $O$)} \\
> \mathbf F^P &= -mg\,\mathbf k_0 - \frac{T}{\rho}\left(R\,\mathbf e_R + cR^2\,\mathbf k_0\right) + N\,\hat{\mathbf n} \quad &\text{(weight, tension $T \ge 0$, normal reaction $N$)} \\
> \mathbf F^Q &= -mg\,\mathbf k_0 + T\,\mathbf k_0 + R_x\,\mathbf i_0 + R_y\,\mathbf j_0 \quad &\text{(weight, tension towards $O$, guide reaction normal to the axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^P = -mg\,\mathbf k_0 - \frac{T}{\sqrt{1 + c^2R^2}}\left(\mathbf e_R + cR\,\mathbf k_0\right) + N\,\frac{-2cR\,\mathbf e_R + \mathbf k_0}{\sqrt{1 + 4c^2R^2}}, \qquad \mathbf F^Q = \left(T - mg\right)\mathbf k_0 + R_x\,\mathbf i_0 + R_y\,\mathbf j_0}$$
>
> **Units:** every force $[\mathrm{M\,L\,T^{-2}}]$; the fractions are dimensionless
> **Meaning:** four new unknowns, $T$, $N$, $R_x$, $R_y$; none of the forces on $P$ has a component along $\mathbf e_\theta$.

> [!derivation] Newton's second law for each particle
> **Law:** Newton's second law in an inertial frame; projections on the tangent vectors (free of $N$) and on the axis
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\mathbf t_R &= \ddot R - R\dot\theta^2 + 4c^2R\left(\dot R^2 + R\ddot R\right) \quad &\text{(components on $\mathbf e_R$ and $\mathbf k_0$ times 1 and $2cR$)} \\
> -\frac{\mathbf r_0^P}{\rho}\cdot\mathbf t_R &= -\frac{R + 2c^2R^3}{R\sqrt{1 + c^2R^2}} = -\rho' \quad &\text{(tension direction on the meridian tangent)} \\
> P,\ \mathbf t_R:\ m\left[\left(1 + 4c^2R^2\right)\ddot R + 4c^2R\dot R^2 - R\dot\theta^2\right] &= -2mgcR - T\rho' \quad &\text{($-mg\,\mathbf k_0\cdot\mathbf t_R = -2mgcR$; $\hat{\mathbf n}\cdot\mathbf t_R = 0$)} \\
> P,\ \mathbf e_\theta:\ m\left(R\ddot\theta + 2\dot R\dot\theta\right) &= 0 \quad &\text{(no force along $\mathbf e_\theta$)} \\
> Q,\ \mathbf k_0:\ m\left(\rho'\ddot R + \rho''\dot R^2\right) &= T - mg \quad &\text{(along the axis)} \\
> Q,\ \mathbf i_0,\ \mathbf j_0:\ 0 &= R_x, \quad 0 = R_y \quad &\text{($\mathbf a_0^Q$ has no horizontal part)}
> \end{aligned}$$
>
> $$\boxed{T = m\left(g + \rho'\ddot R + \rho''\dot R^2\right), \qquad R_x = R_y = 0}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** five of the six scalar equations; the sixth, along $\hat{\mathbf n}$, gives $N$ afterwards. The equation of $Q$ gives the tension in terms of the motion of $R$.

> [!derivation] (f) Equations of motion for R and theta, free of other unknowns
> **Law:** elimination of the tension between the equations of P and Q
> **Source:** Notes.pdf, Sec. 7.6; Notes.pdf, Sec. 7.7
>
> $$\begin{aligned}
> m\left[\left(1 + 4c^2R^2\right)\ddot R + 4c^2R\dot R^2 - R\dot\theta^2\right] &= -2mgcR - m\rho'\left(g + \rho'\ddot R + \rho''\dot R^2\right) \quad &\text{(tension of $Q$ substituted)} \\
> \left(1 + 4c^2R^2 + \rho'^2\right)\ddot R + \left(4c^2R + \rho'\rho''\right)\dot R^2 - R\dot\theta^2 + 2gcR + g\rho' &= 0 \quad &\text{(divided by $m$; all terms on the left)} \\
> \rho'^2 &= \frac{\left(1 + 2c^2R^2\right)^2}{1 + c^2R^2} \quad &\text{(square of $\rho'$)} \\
> \rho'\rho'' &= \frac{1 + 2c^2R^2}{\left(1 + c^2R^2\right)^{1/2}}\cdot\frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}} = \frac{c^2R\left(1 + 2c^2R^2\right)\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^2} \quad &\text{(product of the two derivatives)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \left(1 + 4c^2R^2 + \rho'^2\right)\ddot R + \left(4c^2R + \rho'\rho''\right)\dot R^2 - R\dot\theta^2 + 2gcR + g\rho' = 0 \cr R\ddot\theta + 2\dot R\dot\theta = 0 \end{array}}$$
>
> **Units:** $[\ddot R] = [R\dot\theta^2] = [gcR] = [g\rho'] = [\mathrm{L\,T^{-2}}]$; $[c^2R\dot R^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** two second-order equations in $R$ and $\theta$ only; the coefficient of the radial acceleration is the effective inertia of the pair: $1 + 4c^2R^2$ from $P$ moving along the meridian and $\rho'^2$ from $Q$ moving along the axis.

> [!derivation] Normal reaction of the paraboloid
> **Law:** projection of Newton's second law for P on the unit normal
> **Source:** Notes.pdf, Eq. 4.4; [Lecture 3, Slide 14]
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\hat{\mathbf n} &= \frac{-2cR\left(\ddot R - R\dot\theta^2\right) + 2c\left(\dot R^2 + R\ddot R\right)}{\sqrt{1 + 4c^2R^2}} = \frac{2c\left(\dot R^2 + R^2\dot\theta^2\right)}{\sqrt{1 + 4c^2R^2}} \quad &\text{(the terms in $\ddot R$ cancel)} \\
> \mathbf F^P\cdot\hat{\mathbf n} &= \frac{-mg}{\sqrt{1 + 4c^2R^2}} - \frac{T}{\rho}\,\frac{-2cR^2 + cR^2}{\sqrt{1 + 4c^2R^2}} + N \quad &\text{(weight, tension, reaction)}
> \end{aligned}$$
>
> $$\boxed{N = \frac{2mc\left(\dot R^2 + R^2\dot\theta^2\right) + mg - \dfrac{TcR}{\sqrt{1 + c^2R^2}}}{\sqrt{1 + 4c^2R^2}}}$$
>
> **Units:** $[mc\dot R^2] = [\mathrm{M\,L^{-1}\,L^2\,T^{-2}}] = [mg] = [T] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the bowl carries the weight and supplies the normal part of the acceleration; the string, which pulls $P$ partly away from the surface, reduces the reaction.

### Answers and Checks

#### (e) Tense string

> [!derivation] Condition for the string to stay tense
> **Law:** a string can only pull: positive tension (unilateral constraint)
> **Source:** Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]
>
> $$\begin{aligned}
> T &= m\left(g + \rho'\ddot R + \rho''\dot R^2\right) \gt 0 \quad &\text{(equation of $Q$)} \\
> \ddot z_Q &= \frac{d^2\rho}{dt^2} = \rho'\ddot R + \rho''\dot R^2 \gt -g \quad &\text{(the bracket is the vertical acceleration of $Q$)}
> \end{aligned}$$
>
> $$\boxed{\frac{1 + 2c^2R^2}{\sqrt{1 + c^2R^2}}\,\ddot R + \frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}}\,\dot R^2 \gt -g \quad \text{for all } t}$$
>
> **Units:** every term $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the solution $R(t)$ must never make $Q$ accelerate downwards faster than free fall; if it did, the string would go slack and $Q$ would fall freely.

#### (g) Two first integrals

> [!derivation] Areal integral and energy integral derived from the equations of motion
> **Law:** exact derivatives (product and chain rules); Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(R^2\dot\theta\right) &= 2R\dot R\dot\theta + R^2\ddot\theta = R\left(R\ddot\theta + 2\dot R\dot\theta\right) = 0 \quad &\text{(product and chain rules; equation of $\theta$)} \\
> \left[R^2\dot\theta\right]_0^t &= 0 \Rightarrow R^2\dot\theta = h \quad &\text{(Barrow's rule; $h$ constant)} \\
> \frac{d}{dt}\left[\tfrac12\left(1 + 4c^2R^2 + \rho'^2\right)\dot R^2\right] &= \left(1 + 4c^2R^2 + \rho'^2\right)\dot R\ddot R + \left(4c^2R + \rho'\rho''\right)\dot R^3 \quad &\text{(product rule; chain rule on the coefficient)} \\
> -R\dot\theta^2\,\dot R &= -\frac{h^2}{R^3}\,\dot R = \frac{d}{dt}\left(\frac{h^2}{2R^2}\right) \quad &\text{($\dot\theta = h/R^2$; chain rule)} \\
> \left(2gcR + g\rho'\right)\dot R &= \frac{d}{dt}\left[g\left(cR^2 + \rho\right)\right] \quad &\text{(chain rule)} \\
> \left[\tfrac12\left(1 + 4c^2R^2 + \rho'^2\right)\dot R^2 + \frac{h^2}{2R^2} + g\left(cR^2 + \rho\right)\right]_0^t &= 0 \quad &\text{(equation of $R$ times $\dot R$: a sum of exact derivatives; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{R^2\dot\theta = h, \qquad E = \tfrac12 m\left[\left(1 + 4c^2R^2 + \rho'^2\right)\dot R^2 + R^2\dot\theta^2\right] + mg\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - mg\ell = \text{const}}$$
>
> **Units:** $[h] = [\mathrm{L^2\,T^{-1}}]$; every term of $E$ $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the first is the angular momentum of $P$ about the axis divided by $m$, constant because no force on $P$ has a moment about the axis; the second is the mechanical energy of the pair (kinetic energy of $P$ and $Q$ plus the potential $mg\,z_P + mg\,z_Q$, with $z_Q = \rho - \ell$): the smooth stationary constraints do no work and the string only transfers energy between the particles.

#### (h) Extreme values of R

> [!derivation] Equation of the turning radii
> **Law:** at an extreme of R its rate vanishes; the two first integrals with the initial data
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Problems.pdf, p. 33
>
> $$\begin{aligned}
> h &= R(0)^2\,\dot\theta(0) = \frac{d}{c^2} \quad &\text{($R(0) = 1/c$, $\dot\theta(0) = d$)} \\
> \rho(0) &= \frac{1}{c}\sqrt{1 + 1} = \frac{\sqrt2}{c} \quad &\text{(string on the side of $P$ at $t = 0$)} \\
> \frac{E}{m} + g\ell &= 0 + \frac{h^2c^2}{2} + g\left(\frac{1}{c} + \frac{\sqrt2}{c}\right) = \frac{d^2}{2c^2} + \frac{\left(1 + \sqrt2\right)g}{c} \quad &\text{($\dot R(0) = 0$; $R^2\dot\theta^2 = h^2/R^2$)} \\
> \frac{h^2}{2R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) &= \frac{d^2}{2c^2} + \frac{\left(1 + \sqrt2\right)g}{c} \quad &\text{(energy integral at a radius where $\dot R = 0$)}
> \end{aligned}$$
>
> $$\boxed{f(R) = \frac{d^2}{2c^4R^2} + g\left(cR^2 + R\sqrt{1 + c^2R^2}\right) - \frac{d^2}{2c^2} - \frac{\left(1 + \sqrt2\right)g}{c} = 0}$$
>
> **Units:** $[d^2/(c^4R^2)] = [\mathrm{T^{-2}}][\mathrm{L^4}][\mathrm{L^{-2}}] = [\mathrm{L^2\,T^{-2}}]$; $[gcR^2] = [g/c] = [\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the energy integral gives one half of the effective inertia times the square of the radial rate equal to minus $f(R)$, so the motion is confined to the radii where $f$ is negative or zero; $R = 1/c$ is always a root (the start), and the next box proves that there is at most one other root, which is then the other turning radius.

> [!derivation] At most two turning radii
> **Law:** a strictly convex function that tends to plus infinity at both ends of its interval has at most two roots
> **Source:** Notes.pdf, Eq. 4.28; Problems.pdf, p. 33
>
> The function $f$ of the previous box is differentiated twice with respect to $R$ on the interval of positive radii, with $\rho'$ and $\rho''$ from the box of the derivatives of the length of string; the initial azimuthal rate $d$ is taken as nonzero, as in the statement.
>
> $$\begin{aligned}
> f'(R) &= -\frac{d^2}{c^4R^3} + g\left(2cR + \rho'\right) \quad &\text{(derivative term by term; $\frac{d}{dR}R^{-2} = -2R^{-3}$; constants drop out)} \\
> f''(R) &= \frac{3d^2}{c^4R^4} + g\left(2c + \rho''\right) \quad &\text{(derivative again; $\frac{d}{dR}R^{-3} = -3R^{-4}$)} \\
> \rho'' &= \frac{c^2R\left(3 + 2c^2R^2\right)}{\left(1 + c^2R^2\right)^{3/2}} \gt 0 \quad &\text{(box of the derivatives, with $R \gt 0$ and $c \gt 0$)} \\
> f''(R) &\gt 0 \quad &\text{(each of the three terms is positive: $f$ is strictly convex)} \\
> \lim_{R\to 0^+} f(R) &= +\infty, \qquad \lim_{R\to\infty} f(R) = +\infty \quad &\text{(the terms $\frac{d^2}{2c^4R^2}$ and $gcR^2$ dominate)}
> \end{aligned}$$
>
> $$\boxed{f'' \gt 0 \ \text{on}\ R \gt 0 \ \text{and}\ f \to +\infty \ \text{at both ends:}\ f \ \text{has at most two roots; one is}\ R = 1/c, \ \text{the other (if}\ f'(1/c) \ne 0\text{) is the other turning radius}}$$
>
> **Units:** $[f''] = [3d^2/(c^4R^4)] = [\mathrm{T^{-2}}][\mathrm{L^4}][\mathrm{L^{-4}}] = [gc] = [\mathrm{T^{-2}}]$
> **Meaning:** a strictly convex function crosses zero at most twice; since $f$ is positive near the axis and far away, it is negative only between its two roots, the band of radii in which $P$ moves. If the derivative of $f$ vanished at the start the two roots would merge and $P$ would stay on its initial parallel (circular motion).

| Part of the statement | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 2 effective ($R$, $\theta$): 6 coordinates minus 4 constraint equations (paraboloid, axis of $Q$ twice, string) |
| (b) Kinematics | $\mathbf r_0^P = R\,\mathbf e_R + cR^2\,\mathbf k_0$, $\mathbf v_0^P = \dot R\,\mathbf e_R + R\dot\theta\,\mathbf e_\theta + 2cR\dot R\,\mathbf k_0$, $\mathbf a_0^P = (\ddot R - R\dot\theta^2)\,\mathbf e_R + (R\ddot\theta + 2\dot R\dot\theta)\,\mathbf e_\theta + 2c(\dot R^2 + R\ddot R)\,\mathbf k_0$; $\mathbf r_0^Q = -(\ell - \rho)\,\mathbf k_0$, $\mathbf v_0^Q = \rho'\dot R\,\mathbf k_0$, $\mathbf a_0^Q = (\rho'\ddot R + \rho''\dot R^2)\,\mathbf k_0$, with $\rho = R\sqrt{1 + c^2R^2}$, $\mathbf e_R = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$, $\mathbf e_\theta = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$ |
| (c) Tangent and normal | $\mathbf t_R = \mathbf e_R + 2cR\,\mathbf k_0$, $\mathbf t_\theta = R\,\mathbf e_\theta$, $\mathbf n = R(-2cR\,\mathbf e_R + \mathbf k_0)$ |
| (d) Forces | $P$: $-mg\,\mathbf k_0$, $-T\,\mathbf r_0^P/\rho$, $N\,\hat{\mathbf n}$; $Q$: $-mg\,\mathbf k_0$, $T\,\mathbf k_0$, $R_x\,\mathbf i_0 + R_y\,\mathbf j_0$ (zero) |
| (e) Tense string | $\rho'\ddot R + \rho''\dot R^2 \gt -g$ at all times |
| (f) Equations of motion | $(1 + 4c^2R^2 + \rho'^2)\ddot R + (4c^2R + \rho'\rho'')\dot R^2 - R\dot\theta^2 + 2gcR + g\rho' = 0$; $R\ddot\theta + 2\dot R\dot\theta = 0$ |
| (g) First integrals | $R^2\dot\theta = h$; $\frac12[(1 + 4c^2R^2 + \rho'^2)\dot R^2 + R^2\dot\theta^2] + g(cR^2 + \rho) = \text{const}$ |
| (h) Extreme radii | $f(R) = \frac{d^2}{2c^4R^2} + g(cR^2 + R\sqrt{1 + c^2R^2}) - \frac{d^2}{2c^2} - \frac{(1 + \sqrt2)g}{c} = 0$ |

**Check against the official key:** Problems.pdf, p. 76 lists item 48 with no answer, so there is no key to compare with. Independent checks: the energy integral was obtained from the equation of motion itself (box of part (g)), so the two are consistent by construction; the turning radii are checked numerically below, and the flat limit reproduces the classical problem of the table with a hole.

> [!derivation] Numerical check of the turning radii
> **Law:** roots of the equation of part (h) with unit data, located by the change of sign of f
> **Source:** Notes.pdf, Eq. 4.28
>
> Unit data: $c$ of 1 m$^{-1}$, $d$ of 1 s$^{-1}$, $g$ of 1 m s$^{-2}$ (so that every term is of order one).
>
> $$\begin{aligned}
> f(1) &= \tfrac12 + \left(1 + \sqrt2\right) - \tfrac12 - \left(1 + \sqrt2\right) = 0 \quad &\text{(the start is a root)} \\
> f(0.7) &= \frac{1}{0.98} + 0.49 + 0.7\sqrt{1.49} - 0.5 - 2.4142 = 1.0204 + 0.49 + 0.8545 - 2.9142 = -0.5493 \quad &\text{(negative: allowed radius)} \\
> f(0.4828) &\simeq 0 \quad &\text{(second root, by bisection of the change of sign)}
> \end{aligned}$$
>
> $$\boxed{c = d = g = 1:\quad 0.4828 \le R \le 1}$$
>
> **Units:** in these units $f$ is in m$^2$ s$^{-2}$
> **Meaning:** with these data the start $R = 1/c$ is the largest radius: the initial azimuthal speed is too small to hold $P$ on that parallel, so $P$ slides down the bowl to the radius 0.4828 and back, precessing round the axis.

> [!derivation] Limiting case: flat table with a hole
> **Law:** the equation of motion of R with the curvature c set to zero
> **Source:** Notes.pdf, Eq. 4.4
>
> $$\begin{aligned}
> c &\to 0:\quad \rho = R, \quad \rho' = 1, \quad \rho'' = 0 \quad &\text{(the bowl becomes the horizontal plane through $O$)} \\
> \left(1 + 0 + 1\right)\ddot R + 0 - R\dot\theta^2 + 0 + g &= 0 \quad &\text{(equation of $R$)} \\
> T &= m\left(g + \ddot R\right) \quad &\text{(tension)}
> \end{aligned}$$
>
> $$\boxed{c \to 0:\quad 2\ddot R - R\dot\theta^2 + g = 0, \qquad \text{circular motion when } R\dot\theta^2 = g}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the classical pair on a table with a hole: both particles move with the rate of $R$ (effective mass $2m$), and on a circle the weight of $Q$, carried by the string, is the centripetal force of $P$.

> [!example] Interactive simulator
> sim: {"archetype": "rotating-wire-groove", "title": "P on the paraboloid z = cR², Q hanging through the vertex (Problem 48)", "intro": "Unit data of the solution's numerical check: c = 1 1/m, d = 1 rad/s, g = 1 m/s², and a sample string length ℓ = 3 m. The wire of the archetype is the meridian parabola through P, turning about the vertical k0 with the azimuth θ (frame slider) at the initial rate d. The slider q is the radius R of P; the default R = 1/c, θ = 0 is the initial state of part (h), where the drag velocity arrow is the initial velocity. The blue arrow from O down the axis ends at Q. The readouts follow the two first integrals: f(R) of part (h) is negative where P can be, and zero at the turning radii (1/c and 0.4828 m with these data); the radial rate squared is −2f divided by the effective inertia.", "params": {"wire": "parabola", "k": 1.0, "Omega": 1.0, "qdot": 0, "qmin": 0.05, "qmax": 1.4, "extent": 1.4, "c": 1.0, "d": 1.0, "g": 1.0, "ell": 3.0}, "defaults": {"psi": 0, "q": 1}, "sliders": {"psi": {"label": "Azimuth θ"}, "q": {"label": "Radius R of P (m)", "min": 0.05, "max": 1.4, "step": 0.01}}, "readouts": [{"label": "Height of P, z = cR²", "expr": "c*q^2", "unit": "m", "digits": 4}, {"label": "String on the side of P, ρ = R√(1 + c²R²)", "expr": "q*sqrt(1 + c^2*q^2)", "unit": "m", "digits": 4}, {"label": "Depth of Q below O, ℓ − ρ", "expr": "ell - q*sqrt(1 + c^2*q^2)", "unit": "m", "digits": 4}, {"label": "(g) Areal constant h = R²θ̇ = d/c²", "expr": "d/c^2", "unit": "m²/s", "digits": 4}, {"label": "Azimuthal rate θ̇ = h/R²", "expr": "d/(c^2*q^2)", "unit": "rad/s", "digits": 4}, {"label": "(h) f(R) (P moves where f is negative or zero)", "expr": "(d^2/(2*c^4*q^2) + g*(c*q^2 + q*sqrt(1 + c^2*q^2)) - d^2/(2*c^2) - (1 + sqrt(2))*g/c)", "unit": "m²/s²", "digits": 4}, {"label": "Ṙ² = −2f(R)/(1 + 4c²R² + ρ'²), ρ' = (1 + 2c²R²)/√(1 + c²R²)", "expr": "-2*(d^2/(2*c^4*q^2) + g*(c*q^2 + q*sqrt(1 + c^2*q^2)) - d^2/(2*c^2) - (1 + sqrt(2))*g/c)/(1 + 4*c^2*q^2 + ((1 + 2*c^2*q^2)/sqrt(1 + c^2*q^2))^2)", "unit": "m²/s²", "digits": 4}], "vectors": [{"label": "Q", "at": ["0", "0", "0"], "comp": ["0", "0", "-(ell - q*sqrt(1 + c^2*q^2))"], "scale": 1, "cls": "m3-b1"}]}

---

## Problem 50: Double Pendulum

### Reference Frames, Bases and Coordinates

Two heavy particles $P$ and $Q$ of mass $m$ hang from the origin $O$ by two rigid massless bars of length $\ell$, $OP$ and $PQ$; the angles $\theta$ and $\phi$ of the bars with the downward vertical describe the configuration (Problems.pdf, p. 35). The statement asks for the kinematics, the forces, the equations of motion free of other unknowns, a conservation law, whether $Q$ can cross the axis $Ox$ for a given start and, with the extra constraint that $\phi$ is twice $\theta$, the natural frequency of small oscillations. The solution follows the Newtonian approach of Notes.pdf, Sec. 7.1 to Sec. 7.7.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ of the figure (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ horizontal to the right (axis $Ox$), $\mathbf j$ vertical **upward**, $\mathbf k$ out of the paper |
| Basis of the bar $OP$ | $\mathcal B_1 = \{\mathbf i_1, \mathbf j_1, \mathbf k\}$, $\mathcal B_0$ turned about $\mathbf k$ by the polar angle $\theta - \pi/2$: $\mathbf i_1$ from $O$ to $P$, $\mathbf j_1$ along increasing $\theta$ |
| Basis of the bar $PQ$ | $\mathcal B_2 = \{\mathbf i_2, \mathbf j_2, \mathbf k\}$, $\mathcal B_0$ turned about $\mathbf k$ by $\phi - \pi/2$: $\mathbf i_2$ from $P$ to $Q$, $\mathbf j_2$ along increasing $\phi$ |
| Coordinates | $\theta$, angle of $OP$ from the downward vertical; $\phi$, angle of $PQ$ from the downward vertical; both positive counterclockwise, towards $\mathbf i$ from below (figure) |
| Hypotheses | planar motion in the plane $Oxy$ of the figure; joints without friction; bars rigid and massless |
| Constraints | plane of motion for each particle (2 equations); bars, $|\overrightarrow{OP}| = \ell$ and $|\overrightarrow{PQ}| = \ell$ (2 equations, holonomic, stationary, bilateral: a bar can push and pull) ([Lecture 3, Slide 17]; [Lecture 3, Slide 21]) |
| Degrees of freedom | 6 coordinates minus 4 constraint equations: 2, namely $\theta(t)$ and $\phi(t)$ ([Lecture 3, Slide 4]) |
| Data | $m$ [kg], $\ell$ [m], $g$ [m s$^{-2}$]; part (e): $\theta = \phi = \pi/4$ at rest; part (f): extra constraint, $\phi$ equal to $2\theta$ |
| Applied forces | weights $-mg\,\mathbf j$ on each particle |
| Constraint forces | forces of the bars along the bars: $T_1$ in $OP$ and $T_2$ in $PQ$, positive when the bar pulls (tension), negative when it pushes (Notes.pdf, Sec. 6.4) |

![[attachments/EM-SOL/p50-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p50-rotations-k.svg]]

> [!derivation] Bases of the two bars: angles from the downward vertical
> **Law:** elementary rotation about the third axis, with the angle related to the usual polar angle; change of basis matrices and their checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.20; Notes.pdf, Sec. 4.7
>
> View along $\mathbf k$, out of the paper (⊙), since $\mathbf k$ is the cross product of $\mathbf i$ (to the right) and $\mathbf j$ (up): positive angles are counterclockwise. $\theta$ is measured from the downward vertical, minus $\mathbf j$, which is itself at the polar angle minus $\pi/2$ from $\mathbf i$; so the polar angle of $OP$ is $\theta - \pi/2$, and $\mathbf i_1$ is Notes.pdf, Eq. 1.20 with that angle. The right triangle of $OP$ has hypotenuse $\ell$, horizontal leg $\ell\sin\theta$ (opposite to $\theta$, along $\mathbf i$) and vertical leg $\ell\cos\theta$ (adjacent to $\theta$, along minus $\mathbf j$): this is the minus sign on $\mathbf j$. $\mathbf j_1$ is $\mathbf i_1$ turned a quarter turn counterclockwise. The bar $PQ$ is the same construction with $\phi$.
>
> $$\begin{aligned}
> \cos\left(\theta - \tfrac{\pi}{2}\right) &= \cos\theta\cos\tfrac{\pi}{2} + \sin\theta\sin\tfrac{\pi}{2} = \sin\theta \quad &\text{(cosine of a difference)} \\
> \sin\left(\theta - \tfrac{\pi}{2}\right) &= \sin\theta\cos\tfrac{\pi}{2} - \cos\theta\sin\tfrac{\pi}{2} = -\cos\theta \quad &\text{(sine of a difference)} \\
> \mathbf i_1 &= \sin\theta\,\mathbf i - \cos\theta\,\mathbf j \quad &\text{(opposite leg along $\mathbf i$, adjacent leg along $-\mathbf j$, over $\ell$)} \\
> \mathbf j_1 &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{($\mathbf i_1$ turned by $\pi/2$ counterclockwise)} \\
> \mathbf i_2 &= \sin\phi\,\mathbf i - \cos\phi\,\mathbf j \quad &\text{(same construction with $\phi$: triangle of $PQ$)} \\
> \mathbf j_2 &= \cos\phi\,\mathbf i + \sin\phi\,\mathbf j \quad &\text{($\mathbf i_2$ turned by $\pi/2$ counterclockwise)} \\
> \mathbf i_1\times\mathbf j_1 &= \sin^2\theta\,\mathbf i\times\mathbf j - \cos^2\theta\,\mathbf j\times\mathbf i = \left(\sin^2\theta + \cos^2\theta\right)\mathbf k = \mathbf k \quad &\text{(right-handed)} \\
> \det[{}_0R_1] &= 1\cdot\left(\sin\theta\sin\theta - \cos\theta\left(-\cos\theta\right)\right) = 1 \quad &\text{(expansion along the third row)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \sin^2\theta + \cos^2\theta = 1 \quad &\text{(row 1 times row 1)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= -\sin\theta\cos\theta + \cos\theta\sin\theta = 0 \quad &\text{(row 1 times row 2; row 3 is the unit row of $\mathbf k$)} \\
> \mathbf j &= -\cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1 = -\cos\phi\,\mathbf i_2 + \sin\phi\,\mathbf j_2 \quad &\text{(second rows of the matrices, Eq. 1.14)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \sin\theta & \cos\theta & 0 \cr -\cos\theta & \sin\theta & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad [{}_0R_2] = \begin{pmatrix} \sin\phi & \cos\phi & 0 \cr -\cos\phi & \sin\phi & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det = 1, \quad RR^T = I}$$
>
> **Units:** dimensionless direction cosines: $[1]$
> **Meaning:** at rest, hanging, $\mathbf i_1$ and $\mathbf i_2$ are minus $\mathbf j$; the checks of $[{}_0R_2]$ are those of $[{}_0R_1]$ with $\phi$.

> [!derivation] Dot products between the two bases
> **Law:** dot products of components in the orthonormal basis $\mathcal B_0$; angle-difference identities
> **Source:** Notes.pdf, Eq. 1.13
>
> $$\begin{aligned}
> \mathbf i_1\cdot\mathbf i_2 &= \sin\theta\sin\phi + \cos\theta\cos\phi = \cos\left(\theta - \phi\right) \quad &\text{(cosine of a difference)} \\
> \mathbf j_1\cdot\mathbf j_2 &= \cos\theta\cos\phi + \sin\theta\sin\phi = \cos\left(\theta - \phi\right) \quad &\text{(cosine of a difference)} \\
> \mathbf i_1\cdot\mathbf j_2 &= \sin\theta\cos\phi - \cos\theta\sin\phi = \sin\left(\theta - \phi\right) \quad &\text{(sine of a difference)} \\
> \mathbf j_1\cdot\mathbf i_2 &= \cos\theta\sin\phi - \sin\theta\cos\phi = -\sin\left(\theta - \phi\right) \quad &\text{(sine of a difference, with a minus sign)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1\cdot\mathbf i_2 = \mathbf j_1\cdot\mathbf j_2 = \cos\left(\theta - \phi\right), \qquad \mathbf i_1\cdot\mathbf j_2 = -\mathbf j_1\cdot\mathbf i_2 = \sin\left(\theta - \phi\right)}$$
>
> **Units:** dimensionless
> **Meaning:** only the angle between the two bars, $\theta - \phi$, enters the coupling of the two particles.

> [!derivation] Position vectors of both particles
> **Law:** position vectors as sums of partial vectors along the bars
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Sec. 7.4
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = \ell\,\mathbf i_1 = \ell\sin\theta\,\mathbf i - \ell\cos\theta\,\mathbf j \quad &\text{(legs of the triangle of $OP$)} \\
> \mathbf r_0^Q &= \overrightarrow{OP} + \overrightarrow{PQ} = \ell\,\mathbf i_1 + \ell\,\mathbf i_2 \quad &\text{(sum of partial vectors)} \\
> &= \ell\left(\sin\theta + \sin\phi\right)\mathbf i - \ell\left(\cos\theta + \cos\phi\right)\mathbf j \quad &\text{(legs of both triangles)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = \ell\,\mathbf i_1, \qquad \mathbf r_0^Q = \ell\,\mathbf i_1 + \ell\,\mathbf i_2, \qquad y_P = -\ell\cos\theta, \qquad y_Q = -\ell\left(\cos\theta + \cos\phi\right)}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** $Q$ is on the axis $Ox$ when its height $y_Q$ is zero, which is the question of part (e).

### Kinematics

> [!derivation] Derivatives of the bases of the bars
> **Law:** derivative of a unit vector turning about a fixed axis
> **Source:** Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k \quad &\text{(the polar angle $\theta - \pi/2$ changes at the rate $\dot\theta$)} \\
> \boldsymbol\omega_{20} &= \dot\phi\,\mathbf k \quad &\text{(the polar angle $\phi - \pi/2$ changes at the rate $\dot\phi$)} \\
> \dot{\mathbf i}_1 &= \dot\theta\,\mathbf k\times\mathbf i_1 = \dot\theta\left(\sin\theta\,\mathbf j + \cos\theta\,\mathbf i\right) = \dot\theta\,\mathbf j_1 \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \dot{\mathbf j}_1 &= \dot\theta\,\mathbf k\times\mathbf j_1 = \dot\theta\left(\cos\theta\,\mathbf j - \sin\theta\,\mathbf i\right) = -\dot\theta\,\mathbf i_1 \quad &\text{(same products)} \\
> \dot{\mathbf i}_2 &= \dot\phi\,\mathbf k\times\mathbf i_2 = \dot\phi\,\mathbf j_2 \quad &\text{(same products with $\phi$)} \\
> \dot{\mathbf j}_2 &= \dot\phi\,\mathbf k\times\mathbf j_2 = -\dot\phi\,\mathbf i_2 \quad &\text{(same products with $\phi$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_1 = \dot\theta\,\mathbf j_1, \quad \dot{\mathbf j}_1 = -\dot\theta\,\mathbf i_1, \quad \dot{\mathbf i}_2 = \dot\phi\,\mathbf j_2, \quad \dot{\mathbf j}_2 = -\dot\phi\,\mathbf i_2}$$
>
> **Units:** $[\dot\theta] = [\dot\phi] = [\mathrm{T^{-1}}]$
> **Meaning:** each bar turns about $\mathbf k$ with its own angular rate.

> [!derivation] (a) Position, velocity and acceleration of both particles
> **Law:** time derivatives in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 4.34; Notes.pdf, Eq. 4.35
>
> $$\begin{aligned}
> \mathbf v_0^P &= \ell\,\dot{\mathbf i}_1 = \ell\dot\theta\,\mathbf j_1 \quad &\text{($\ell$ constant)} \\
> \mathbf a_0^P &= \ell\ddot\theta\,\mathbf j_1 + \ell\dot\theta\,\dot{\mathbf j}_1 = \ell\ddot\theta\,\mathbf j_1 - \ell\dot\theta^2\,\mathbf i_1 \quad &\text{(product rule; derivative of $\mathbf j_1$)} \\
> \mathbf v_0^Q &= \ell\,\dot{\mathbf i}_1 + \ell\,\dot{\mathbf i}_2 = \ell\dot\theta\,\mathbf j_1 + \ell\dot\phi\,\mathbf j_2 \quad &\text{(sum of the two bar terms)} \\
> \mathbf a_0^Q &= \ell\ddot\theta\,\mathbf j_1 - \ell\dot\theta^2\,\mathbf i_1 + \ell\ddot\phi\,\mathbf j_2 - \ell\dot\phi^2\,\mathbf i_2 \quad &\text{(product rule on each term)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} \mathbf r_0^P = \ell\,\mathbf i_1, \quad \mathbf v_0^P = \ell\dot\theta\,\mathbf j_1, \quad \mathbf a_0^P = \ell\ddot\theta\,\mathbf j_1 - \ell\dot\theta^2\,\mathbf i_1 \cr \mathbf r_0^Q = \ell\left(\mathbf i_1 + \mathbf i_2\right), \quad \mathbf v_0^Q = \ell\dot\theta\,\mathbf j_1 + \ell\dot\phi\,\mathbf j_2, \quad \mathbf a_0^Q = \ell\left(\ddot\theta\,\mathbf j_1 - \dot\theta^2\,\mathbf i_1 + \ddot\phi\,\mathbf j_2 - \dot\phi^2\,\mathbf i_2\right) \end{array}}$$
>
> **Units:** $[\ell\dot\theta] = [\mathrm{L\,T^{-1}}]$; $[\ell\ddot\theta] = [\ell\dot\theta^2] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** $P$ moves on a circle about $O$ (the pendulum of Notes.pdf, Sec. 4.7); $Q$ adds to the motion of $P$ its own circular motion about $P$.

### Forces and Equations of Motion

The free-body diagrams show on each particle its weight and the forces of the bars attached to it; the bar $PQ$ acts on $P$ and on $Q$ with equal and opposite forces. $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p50-fbd.svg]]

> [!derivation] (b) Forces on both particles
> **Law:** weight; constraint forces in the normal subspaces of the bar constraints, along the gradients of their equations
> **Source:** Notes.pdf, Sec. 6.4; [Lecture 3, Slide 13]; [Lecture 3, Slide 17]
>
> The bar $OP$ is the constraint whose equation is the square of the length of $OP$ minus $\ell^2$; its gradient with respect to the position of $P$ is twice $\overrightarrow{OP}$, along $\mathbf i_1$. The bar $PQ$ is the constraint on the square of the length of $PQ$; its gradient is twice $\overrightarrow{PQ}$ (along $\mathbf i_2$) with respect to $Q$ and minus that with respect to $P$, so its forces on $Q$ and $P$ are equal and opposite.
>
> $$\begin{aligned}
> \mathbf N_{OP\to P} &= -T_1\,\mathbf i_1 \quad &\text{(along the bar; $T_1 \gt 0$ pulls $P$ towards $O$)} \\
> \mathbf N_{PQ\to Q} &= -T_2\,\mathbf i_2 \quad &\text{(along the bar; $T_2 \gt 0$ pulls $Q$ towards $P$)} \\
> \mathbf N_{PQ\to P} &= +T_2\,\mathbf i_2 \quad &\text{(equal and opposite: minus the gradient with respect to $Q$)} \\
> \mathbf F^P &= -mg\,\mathbf j - T_1\,\mathbf i_1 + T_2\,\mathbf i_2 \quad &\text{(all forces on $P$)} \\
> \mathbf F^Q &= -mg\,\mathbf j - T_2\,\mathbf i_2 \quad &\text{(all forces on $Q$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^P = -mg\,\mathbf j - T_1\,\mathbf i_1 + T_2\,\mathbf i_2, \qquad \mathbf F^Q = -mg\,\mathbf j - T_2\,\mathbf i_2}$$
>
> **Units:** $[mg] = [T_1] = [T_2] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** two new unknowns, $T_1$ and $T_2$; a bar, unlike a string, may also push, so they may take either sign.

> [!derivation] (c) Equations of motion free of the forces of the bars
> **Law:** Newton's second law in an inertial frame; projections chosen to eliminate $T_1$ and $T_2$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6; [Lecture 3, Slide 14]
>
> $\mathbf j_2$ is perpendicular to $\mathbf i_2$, so the equation of $Q$ along $\mathbf j_2$ is free of $T_2$. Adding the equations of $P$ and $Q$ cancels the pair $\pm T_2\,\mathbf i_2$, and $\mathbf j_1$ is perpendicular to $\mathbf i_1$, so the sum along $\mathbf j_1$ is free of $T_1$. The weight is projected with $\mathbf j\cdot\mathbf j_1 = \sin\theta$ and $\mathbf j\cdot\mathbf j_2 = \sin\phi$.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P + m\,\mathbf a_0^Q &= \mathbf F^P + \mathbf F^Q = -2mg\,\mathbf j - T_1\,\mathbf i_1 \quad &\text{(Newton for each particle, added: the pair $\pm T_2\,\mathbf i_2$ cancels)} \\
> \mathbf a_0^Q\cdot\mathbf j_2 &= \ell\ddot\theta\cos\left(\theta - \phi\right) - \ell\dot\theta^2\sin\left(\theta - \phi\right) + \ell\ddot\phi \quad &\text{(dot products of the previous box)} \\
> Q,\ \mathbf j_2:\ m\ell\left[\ddot\phi + \ddot\theta\cos\left(\theta - \phi\right) - \dot\theta^2\sin\left(\theta - \phi\right)\right] &= -mg\sin\phi \quad &\text{(no $T_2$)} \\
> \left(\mathbf a_0^P + \mathbf a_0^Q\right)\cdot\mathbf j_1 &= 2\ell\ddot\theta + \ell\ddot\phi\cos\left(\theta - \phi\right) + \ell\dot\phi^2\sin\left(\theta - \phi\right) \quad &\text{($\mathbf j_2\cdot\mathbf j_1 = \cos(\theta - \phi)$, $\mathbf i_2\cdot\mathbf j_1 = -\sin(\theta - \phi)$)} \\
> P + Q,\ \mathbf j_1:\ m\ell\left[2\ddot\theta + \ddot\phi\cos\left(\theta - \phi\right) + \dot\phi^2\sin\left(\theta - \phi\right)\right] &= -2mg\sin\theta \quad &\text{(no $T_1$, no $T_2$)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} 2\ddot\theta + \ddot\phi\cos\left(\theta - \phi\right) + \dot\phi^2\sin\left(\theta - \phi\right) + \dfrac{2g}{\ell}\sin\theta = 0 \cr \ddot\phi + \ddot\theta\cos\left(\theta - \phi\right) - \dot\theta^2\sin\left(\theta - \phi\right) + \dfrac{g}{\ell}\sin\phi = 0 \end{array}}$$
>
> **Units:** $[\ddot\theta] = [\dot\phi^2] = [g/\ell] = [\mathrm{T^{-2}}]$
> **Meaning:** two coupled second-order equations for the two angles; they contain no force of the bars.

> [!derivation] Forces of the bars, afterwards
> **Law:** Newton's second law projected along the bars
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.37
>
> $$\begin{aligned}
> Q,\ \mathbf i_2:\ m\ell\left[-\ddot\theta\sin\left(\theta - \phi\right) - \dot\theta^2\cos\left(\theta - \phi\right) - \dot\phi^2\right] &= mg\cos\phi - T_2 \quad &\text{($\mathbf j_1\cdot\mathbf i_2 = -\sin(\theta - \phi)$; $-\mathbf j\cdot\mathbf i_2 = \cos\phi$)} \\
> P,\ \mathbf i_1:\ -m\ell\dot\theta^2 &= mg\cos\theta - T_1 + T_2\cos\left(\theta - \phi\right) \quad &\text{($-\mathbf j\cdot\mathbf i_1 = \cos\theta$; $\mathbf i_2\cdot\mathbf i_1 = \cos(\theta - \phi)$)}
> \end{aligned}$$
>
> $$\boxed{\begin{array}{l} T_2 = mg\cos\phi + m\ell\left[\ddot\theta\sin\left(\theta - \phi\right) + \dot\theta^2\cos\left(\theta - \phi\right) + \dot\phi^2\right] \cr T_1 = mg\cos\theta + m\ell\dot\theta^2 + T_2\cos\left(\theta - \phi\right) \end{array}}$$
>
> **Units:** every term $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** hanging at rest ($\theta$, $\phi$ and their rates zero) the lower bar carries the weight of $Q$, $T_2 = mg$, and the upper bar both weights, $T_1 = 2mg$.

### Answers and Checks

#### (d) Conservation law

> [!derivation] Mechanical energy of the double pendulum
> **Law:** theorem of kinetic energy; the forces of the stationary bars do no total work; potential of the weights
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 16]; [Lecture 3, Slide 17]
>
> $$\begin{aligned}
> -T_1\,\mathbf i_1\cdot\mathbf v_0^P &= -T_1\,\mathbf i_1\cdot\ell\dot\theta\,\mathbf j_1 = 0 \quad &\text{(power of the bar $OP$)} \\
> T_2\,\mathbf i_2\cdot\mathbf v_0^P - T_2\,\mathbf i_2\cdot\mathbf v_0^Q &= -T_2\,\mathbf i_2\cdot\left(\mathbf v_0^Q - \mathbf v_0^P\right) = -T_2\,\mathbf i_2\cdot\ell\dot\phi\,\mathbf j_2 = 0 \quad &\text{(total power of the bar $PQ$)} \\
> -mg\,\mathbf j\cdot\left(\mathbf v_0^P + \mathbf v_0^Q\right) &= -\frac{d}{dt}\left[mg\left(y_P + y_Q\right)\right] \quad &\text{(power of the weights)} \\
> \frac{d}{dt}\left[\tfrac12 m|\mathbf v_0^P|^2 + \tfrac12 m|\mathbf v_0^Q|^2\right] &= -\frac{d}{dt}\left[mg\left(y_P + y_Q\right)\right] \quad &\text{(theorem of kinetic energy for each particle, added: sum of all powers; the bar powers are zero)} \\
> |\mathbf v_0^P|^2 &= \ell^2\dot\theta^2\,\mathbf j_1\cdot\mathbf j_1 = \ell^2\dot\theta^2 \quad &\text{(square of $\mathbf v_0^P$; $\mathbf j_1$ unit)} \\
> |\mathbf v_0^Q|^2 &= \ell^2\left[\dot\theta^2 + \dot\phi^2 + 2\dot\theta\dot\phi\cos\left(\theta - \phi\right)\right] \quad &\text{(square of $\mathbf v_0^Q$; $\mathbf j_1\cdot\mathbf j_2 = \cos(\theta - \phi)$)} \\
> E &= \tfrac12 m\ell^2\dot\theta^2 + \tfrac12 m|\mathbf v_0^Q|^2 - mg\ell\cos\theta - mg\ell\left(\cos\theta + \cos\phi\right) \quad &\text{(Barrow's rule: the bracket of kinetic plus potential energy is constant; $|\mathbf v_0^P|^2$, $y_P$, $y_Q$ substituted)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12 m\ell^2\left[2\dot\theta^2 + \dot\phi^2 + 2\dot\theta\dot\phi\cos\left(\theta - \phi\right)\right] - mg\ell\left(2\cos\theta + \cos\phi\right) = \text{const}}$$
>
> **Units:** $[m\ell^2\dot\theta^2] = [mg\ell] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the bars only transfer energy between the particles: the bar $OP$ is perpendicular to the velocity of $P$, and the bar $PQ$ is perpendicular to the velocity of $Q$ relative to $P$. Only the conservative weights work.

#### (e) Can Q cross the axis Ox?

> [!derivation] Energy needed to bring Q to the height of O
> **Law:** the kinetic energy is never negative, so the potential energy cannot exceed the constant energy
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> E_0 &= 0 - mg\ell\left(2\cos\tfrac{\pi}{4} + \cos\tfrac{\pi}{4}\right) = -\frac{3\sqrt2}{2}\,mg\ell = -2.121\,mg\ell \quad &\text{(at rest, $\theta = \phi = \pi/4$)} \\
> y_Q &= -\ell\left(\cos\theta + \cos\phi\right) = 0 \iff \cos\phi = -\cos\theta \quad &\text{($Q$ on the axis $Ox$)} \\
> V &= -mg\ell\left(2\cos\theta - \cos\theta\right) = -mg\ell\cos\theta \ge -mg\ell \quad &\text{(potential there; $\cos\theta \le 1$)} \\
> E_0 - V &\le -2.121\,mg\ell + mg\ell = -1.121\,mg\ell \lt 0 \quad &\text{(the kinetic energy would be negative)}
> \end{aligned}$$
>
> $$\boxed{E_0 = -\tfrac{3\sqrt2}{2}\,mg\ell \lt -mg\ell \le V\big|_{y_Q = 0}: \quad Q \ \text{never reaches, so never crosses, the axis } Ox}$$
>
> **Units:** $[mg\ell] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** whatever the configuration with $Q$ at the height of $O$, it needs at least the potential energy $-mg\ell$, more than the energy available; the motion stays below the axis.

#### (f) Small oscillations with the extra constraint

> [!derivation] Energy of the constrained system for small angles
> **Law:** the extra constraint is ideal and stationary (no work), so the energy of part (d) is still conserved; second-order expansion in the small angle; comparison with the energy of a harmonic oscillator
> **Source:** Notes.pdf, Eq. 5.6; [Lecture 6, Slide 7]; [Lecture 3, Slide 16]; Problems.pdf, p. 35
>
> With $\phi$ equal to $2\theta$ the system has one degree of freedom, $\theta$. The kinetic energy is already quadratic in the rate, so its coefficient is kept to zeroth order in $\theta$; the potential is expanded to second order with the Taylor series of the cosine.
>
> $$\begin{aligned}
> \dot\phi &= 2\dot\theta \quad &\text{(derivative of the extra constraint)} \\
> \cos\left(\theta - \phi\right) &= \cos\left(-\theta\right) = \cos\theta \quad &\text{(angle between the bars; cosine is even)} \\
> K &= \tfrac12 m\ell^2\left[2 + 4 + 4\cos\theta\right]\dot\theta^2 \simeq \tfrac12 m\ell^2\left(10\right)\dot\theta^2 = 5m\ell^2\dot\theta^2 \quad &\text{(kinetic energy of part (d); $\cos\theta \simeq 1$)} \\
> \cos\theta &\simeq 1 - \tfrac{\theta^2}{2} \quad &\text{(Taylor series to second order)} \\
> \cos 2\theta &\simeq 1 - \tfrac{\left(2\theta\right)^2}{2} = 1 - 2\theta^2 \quad &\text{(the same series with the argument $2\theta$)} \\
> V &= -mg\ell\left(2\cos\theta + \cos 2\theta\right) \simeq -mg\ell\left(2 - \theta^2 + 1 - 2\theta^2\right) = -3mg\ell + 3mg\ell\,\theta^2 \quad &\text{(potential of part (d))} \\
> E + 3mg\ell &\simeq 5m\ell^2\dot\theta^2 + 3mg\ell\,\theta^2 = \tfrac12\left(10m\ell^2\right)\left(\dot\theta^2 + \frac{3g}{5\ell}\,\theta^2\right) \quad &\text{(common factor $5m\ell^2$)} \\
> 10m\ell^2\dot\theta\ddot\theta + 6mg\ell\,\theta\dot\theta &= 0 \Rightarrow \ddot\theta + \frac{3g}{5\ell}\,\theta = 0 \quad &\text{(time derivative of the constant energy, chain rule; divided by $10m\ell^2\dot\theta$)}
> \end{aligned}$$
>
> $$\boxed{\omega_0 = \sqrt{\frac{3g}{5\ell}}}$$
>
> **Units:** $[g/\ell] = [\mathrm{T^{-2}}]$, so $[\omega_0] = [\mathrm{T^{-1}}]$
> **Meaning:** the energy has the form of the hint, with the mass replaced by $10m\ell^2$ and the coordinate by $\theta$; the linearised equation is the harmonic oscillator of Notes.pdf, Eq. 5.6. The frequency squared is 0.6 times that of a simple pendulum of length $\ell$: $Q$, which moves three times as far as $P$, adds more inertia than restoring weight.

| Part of the statement | Answer |
| :--- | :--- |
| (a) Kinematics | $\mathbf r_0^P = \ell\,\mathbf i_1$, $\mathbf v_0^P = \ell\dot\theta\,\mathbf j_1$, $\mathbf a_0^P = \ell(\ddot\theta\,\mathbf j_1 - \dot\theta^2\,\mathbf i_1)$; $\mathbf r_0^Q = \ell(\mathbf i_1 + \mathbf i_2)$, $\mathbf v_0^Q = \ell(\dot\theta\,\mathbf j_1 + \dot\phi\,\mathbf j_2)$, $\mathbf a_0^Q = \ell(\ddot\theta\,\mathbf j_1 - \dot\theta^2\,\mathbf i_1 + \ddot\phi\,\mathbf j_2 - \dot\phi^2\,\mathbf i_2)$, with $\mathbf i_1 = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j$, $\mathbf j_1 = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j$ and the same with $\phi$ |
| (b) Forces | $P$: $-mg\,\mathbf j$, $-T_1\,\mathbf i_1$, $T_2\,\mathbf i_2$; $Q$: $-mg\,\mathbf j$, $-T_2\,\mathbf i_2$ |
| (c) Equations of motion | $2\ddot\theta + \ddot\phi\cos(\theta - \phi) + \dot\phi^2\sin(\theta - \phi) + (2g/\ell)\sin\theta = 0$; $\ddot\phi + \ddot\theta\cos(\theta - \phi) - \dot\theta^2\sin(\theta - \phi) + (g/\ell)\sin\phi = 0$ |
| (d) Conservation law | $\frac12 m\ell^2[2\dot\theta^2 + \dot\phi^2 + 2\dot\theta\dot\phi\cos(\theta - \phi)] - mg\ell(2\cos\theta + \cos\phi) = E$ |
| (e) Crossing $Ox$ | never: $E_0 = -\frac{3\sqrt2}{2}mg\ell$ is below the least potential $-mg\ell$ with $Q$ on the axis |
| (f) Constrained small oscillations | $\omega_0 = \sqrt{3g/(5\ell)}$ |

**Check against the official key:** Problems.pdf, p. 76 lists item 50 with no answer, so there is no key to compare with. Independent checks: the energy of part (d) was obtained from the powers of the forces, and its time derivative vanishes along the equations of part (c) (box below); the static forces of the bars are the expected ones; and the frequency of part (f) belongs to a family of constraints whose limits are checked below.

> [!derivation] The energy is a first integral of the equations of motion
> **Law:** time derivative of the energy of part (d) (product and chain rules), compared with the equations of part (c) multiplied by the rates
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.4
>
> Write $\mathcal E_1$ and $\mathcal E_2$ for the left-hand sides of the first and second equations of the box of part (c); both vanish along every motion.
>
> $$\begin{aligned}
> \frac{d}{dt}\cos\left(\theta - \phi\right) &= -\sin\left(\theta - \phi\right)\left(\dot\theta - \dot\phi\right) \quad &\text{(chain rule)} \\
> \dot E &= m\ell^2\left[2\dot\theta\ddot\theta + \dot\phi\ddot\phi + \ddot\theta\dot\phi\cos\left(\theta - \phi\right) + \dot\theta\ddot\phi\cos\left(\theta - \phi\right) - \dot\theta\dot\phi\left(\dot\theta - \dot\phi\right)\sin\left(\theta - \phi\right)\right] + mg\ell\left(2\dot\theta\sin\theta + \dot\phi\sin\phi\right) \quad &\text{(product and chain rules on each term of $E$)} \\
> m\ell^2\dot\theta\,\mathcal E_1 &= m\ell^2\left[2\dot\theta\ddot\theta + \dot\theta\ddot\phi\cos\left(\theta - \phi\right) + \dot\theta\dot\phi^2\sin\left(\theta - \phi\right)\right] + 2mg\ell\,\dot\theta\sin\theta \quad &\text{(first equation of part (c) times $m\ell^2\dot\theta$)} \\
> m\ell^2\dot\phi\,\mathcal E_2 &= m\ell^2\left[\dot\phi\ddot\phi + \dot\phi\ddot\theta\cos\left(\theta - \phi\right) - \dot\theta^2\dot\phi\sin\left(\theta - \phi\right)\right] + mg\ell\,\dot\phi\sin\phi \quad &\text{(second equation of part (c) times $m\ell^2\dot\phi$)} \\
> \dot E &= m\ell^2\dot\theta\,\mathcal E_1 + m\ell^2\dot\phi\,\mathcal E_2 \quad &\text{(term by term, with $-\dot\theta\dot\phi\left(\dot\theta - \dot\phi\right) = \dot\theta\dot\phi^2 - \dot\theta^2\dot\phi$)} \\
> &= 0 \quad &\text{($\mathcal E_1 = \mathcal E_2 = 0$ along the motion)}
> \end{aligned}$$
>
> $$\boxed{\dot E = m\ell^2\left(\dot\theta\,\mathcal E_1 + \dot\phi\,\mathcal E_2\right) = 0}$$
>
> **Units:** $[m\ell^2\dot\theta\ddot\theta] = [mg\ell\dot\theta] = [\mathrm{M\,L^2\,T^{-3}}]$, a power
> **Meaning:** the energy of part (d), found from the powers of the forces, is also a first integral of the equations of part (c), found by projections: the two routes agree, which checks the signs and coefficients of both.

> [!derivation] Limiting cases: a family of imposed constraints
> **Law:** the energy method of part (f) with the constraint that $\phi$ equals $\lambda\theta$, for a constant $\lambda$
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Sec. 4.7
>
> $$\begin{aligned}
> K &\simeq \tfrac12 m\ell^2\left(2 + \lambda^2 + 2\lambda\right)\dot\theta^2 \quad &\text{(kinetic energy of part (d), $\dot\phi = \lambda\dot\theta$, $\cos(\theta - \phi) \simeq 1$)} \\
> V &\simeq -3mg\ell + \tfrac12 mg\ell\left(2 + \lambda^2\right)\theta^2 \quad &\text{(Taylor series of $\cos\theta$ and $\cos\lambda\theta$)} \\
> \omega_0^2 &= \frac{g}{\ell}\,\frac{2 + \lambda^2}{2 + 2\lambda + \lambda^2} \quad &\text{(ratio of the two coefficients)} \\
> \lambda = 0:\ \omega_0^2 &= \frac{g}{\ell}\,\frac{2}{2} = \frac{g}{\ell} \quad &\text{(lower bar held vertical)} \\
> \lambda = 2:\ \omega_0^2 &= \frac{g}{\ell}\,\frac{2 + 4}{2 + 4 + 4} = \frac{3g}{5\ell} \quad &\text{(the constraint of the statement)}
> \end{aligned}$$
>
> $$\boxed{\lambda = 0:\ \omega_0 = \sqrt{g/\ell}\ \text{(simple pendulum)}; \qquad \lambda = 2:\ \omega_0 = \sqrt{3g/(5\ell)}\ \text{(part (f))}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** with the lower bar kept vertical both particles move with $P$ and swing together as one simple pendulum of length $\ell$, the frequency of Notes.pdf, Sec. 4.7; the general formula reproduces the result of part (f) for the constraint of the statement.

> [!example] Interactive simulator
> sim: {"archetype": "oscillator-phase", "title": "Double pendulum with the constraint φ = 2θ: small oscillations (Problem 50)", "intro": "Sample values ℓ = 1 m, g = 9.81 m/s² (the statement gives none). The archetype draws no bars: the mass is the coordinate θ of part (f), in radians, and the lower bar follows with φ = 2θ. The default is a sample release from rest at θ = 0.1 rad, at t = 0; the oscillation has the frequency ω0 of the energy of the hint, and the damping ratio must stay at zero. The readouts give the frequency, its comparison with the simple pendulum through the family of constraints φ = λθ of the limiting cases, the height of Q at the drawn θ, and the energies of part (e).", "params": {"mode": "free", "wn": 2.426108, "zeta": 0, "x0": 0.1, "v0": 0, "tmax": 10, "extent": 0.15, "ell": 1.0, "g": 9.81}, "defaults": {"t": 0, "zeta": 0}, "readouts": [{"label": "(f) ω0 = √(3g/(5ℓ))", "expr": "sqrt(3*g/(5*ell))", "unit": "rad/s", "digits": 4}, {"label": "Simple pendulum √(g/ℓ), for comparison", "expr": "sqrt(g/ell)", "unit": "rad/s", "digits": 4}, {"label": "ω0²/(g/ℓ) = (2 + λ²)/(2 + 2λ + λ²), λ = 2", "expr": "(2 + 2^2)/(2 + 2*2 + 2^2)", "unit": "", "digits": 3}, {"label": "Period 2π/ω0", "expr": "2*pi/sqrt(3*g/(5*ell))", "unit": "s", "digits": 3}, {"label": "Angle θ of the upper bar (φ = 2θ)", "expr": "deg(x)", "unit": "deg", "digits": 3}, {"label": "Height of Q, y_Q = −ℓ(cos θ + cos 2θ)", "expr": "-ell*(cos(x) + cos(2*x))", "unit": "m", "digits": 5}, {"label": "(e) Initial energy E0/(mgℓ) = −3√2/2", "expr": "-3*sqrt(2)/2", "unit": "", "digits": 4}, {"label": "(e) Least potential with Q on Ox, over mgℓ", "expr": "-1", "unit": "", "digits": 1}]}
