---
title: "Solution Set - Topic 8: Constraints, Rolling, Multibody and Torque-Free Motion"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (lecturer's order)"
language: "English"
tags:
  - solutions
  - topic-8
  - rolling-multibody
---

# Topic 8: Constraints, Rolling, Multibody and Torque-Free Motion - Full Analytical Solutions

Step-by-step solutions of the official rigid body problems of groups E, F and G (section 2 of `Problems.pdf`). Every problem follows the order of the course for a rigid body: reference frames, bases and degrees of freedom; change of basis, position vectors and constraint kinematics; centre of mass and inertia tensor; linear momentum, angular momentum and kinetic energy; free-body diagram and equations of motion; answers and checks. Every calculation is inside a derivation box and starts from the definitions of [[Topic 8 - Constraints, Rolling Motion, Multibody Systems and Torque-Free Motion]]. Statements: [[Problem Set - Topic 8 Constraints, Rolling, Multibody and Torque-Free Motion]]. Official answers: [[Problem Set - Rigid Body Official Key]]. Subject index: [[Engineering Mechanics MOC]].

---

## Problem RB-12: Box rolling on cylinder

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous box $b$ of mass $m$, width $b$ and height $h$, resting on the fixed semicylindrical surface of radius $R$ and rolling on it without slipping, in the vertical plane of the figure. Gravity acts downwards. The box is a prism; its depth $c$ normal to the paper is not given and cancels from every result.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$ with origin $O$ at the centre of the semicircular section (the foot of the radius $R$ in the figure), $\mathbf i$ horizontal to the right, $\mathbf j$ vertical upwards and $\mathbf k$ out of the paper (⊙). The cylinder is at rest, so $S_0$ is inertial.
* **Body frame:** $S_B\{G; \mathbf i_B, \mathbf j_B, \mathbf k\}$, with $\mathbf i_B$ parallel to the bottom face (along the width $b$, to the right in the initial position) and $\mathbf j_B$ normal to it, from the bottom face towards the top face.
* **Points:** $T$ is the top of the cylinder (the initial contact point), $M$ is the body point at the middle of the bottom face (the body point that touches $T$ at the start) and $C$ is the current contact point.
* **Coordinate:** the angle $\varphi$ from $\mathbf i$ to $\mathbf i_B$, positive counterclockwise about $\mathbf k$ by the right-hand rule. It is the angle by which the box has turned away from the horizontal.
* **Degrees of freedom:** a rigid body in plane motion has three coordinates (two for $G$ and one angle). Keeping contact with the cylinder (no penetration, Notes.pdf, Eq. 13.1) removes one; rolling without slipping removes another, and in a plane problem this constraint can be integrated into a relation among the coordinates (Notes.pdf, Eq. 13.4). One degree of freedom remains: $\varphi$.
* **Unknowns of the dynamics:** $\varphi(t)$ and the two components of the contact force at $C$, the normal reaction $N$ and the friction force $F$ (unknown, because the box does not slip). Three scalar equations are available: two components of the force equation and the component along $\mathbf k$ of the moment equation.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the box, homogeneous | $m$ | kg |
| Width and height of the box | $b$, $h$ | m |
| Radius of the fixed cylinder | $R$ | m |
| Gravity | $g$, along $-\mathbf j$ | m/s$^2$ |
| Initial position | bottom face horizontal, $M$ on $T$, $G$ above $O$ | - |
| Contact | rolling without slipping, one contact point | - |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb12-rotation.svg]]

> [!derivation] Body basis: rotation about k by the angle phi
> **Law:** simple rotation about the third axis, positive by the right-hand rule; Poisson's formula for the derivative of a unit vector
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the plane of motion with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up; a positive $\varphi$ turns counterclockwise. Right triangle of $\mathbf i_B$: hypotenuse the unit vector $\mathbf i_B$, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Right triangle of $\mathbf j_B$: hypotenuse $\mathbf j_B$, adjacent leg along $\mathbf j$ (cosine), opposite leg along $\mathbf i$ (sine); the tip of $\mathbf j$, turned counterclockwise about $\mathbf k$ pointing out of the paper, moves towards negative $\mathbf i$, hence the minus sign.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j \quad &\text{(legs of the triangle of $\mathbf i_B$)} \\
> \mathbf j_B &= -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j \quad &\text{(legs of the triangle of $\mathbf j_B$; tip carried towards minus $\mathbf i$)} \\
> [{}_0R_B] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_B] &= 1\cdot\left(\cos\varphi\cos\varphi - (-\sin\varphi)\sin\varphi\right) = \cos^2\varphi + \sin^2\varphi = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_B][{}_0R_B]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i &= \cos\varphi\,\mathbf i_B - \sin\varphi\,\mathbf j_B, \qquad \mathbf j = \sin\varphi\,\mathbf i_B + \cos\varphi\,\mathbf j_B \quad &\text{(rows of the matrix: the inverse is the transpose)} \\
> \boldsymbol\omega_{B0} &= \dot\varphi\,\mathbf k, \qquad \boldsymbol\alpha_{B0} = \ddot\varphi\,\mathbf k \quad &\text{(single rotation about the fixed axis $\mathbf k$; product rule with zero derivative of $\mathbf k$)} \\
> \dot{\mathbf i}_B &= \boldsymbol\omega_{B0}\times\mathbf i_B = \dot\varphi\,\mathbf k\times\mathbf i_B = \dot\varphi\,\mathbf j_B \quad &\text{(Poisson; $\mathbf k\times\mathbf i_B = \mathbf j_B$)} \\
> \dot{\mathbf j}_B &= \boldsymbol\omega_{B0}\times\mathbf j_B = \dot\varphi\,\mathbf k\times\mathbf j_B = -\dot\varphi\,\mathbf i_B \quad &\text{(Poisson; $\mathbf k\times\mathbf j_B = -\mathbf i_B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_B = \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j, \qquad \mathbf j_B = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j, \qquad \boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k}$$
>
> **Units:** the matrix is dimensionless; the angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** for a positive angle the box has turned counterclockwise: its left end has gone down and its right end up.

![[attachments/EM-SOL/rb12-geometry.svg]]

> [!derivation] Contact point on the cylinder (no penetration)
> **Law:** the bottom face is tangent to the cylinder at the contact point; the normal to a circle passes through its centre
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.2
>
> At the contact the two bodies share the normal. The normal to the flat bottom face is $\mathbf j_B$; the normal to the cylinder at $C$ is the unit vector along $OC$. So $OC$ is parallel to $\mathbf j_B$ and the radius $OC$ makes the angle $\varphi$ with the vertical. Right triangle with hypotenuse $OC$ of length $R$: the vertical leg is adjacent to the angle $\varphi$ at $O$, the horizontal leg is opposite to it and points to the left (towards negative $\mathbf i$) for a positive angle.
>
> $$\begin{aligned}
> \mathbf r_0^C &= R\,\mathbf j_B \quad &\text{(radius of length $R$ along the common normal)} \\
> &= R\left(-\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j\right) \quad &\text{($\mathbf j_B$ from the rotation box)} \\
> &= -R\sin\varphi\,\mathbf i + R\cos\varphi\,\mathbf j \quad &\text{(opposite leg to the left, adjacent leg upwards)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^C = R\,\mathbf j_B = -R\sin\varphi\,\mathbf i + R\cos\varphi\,\mathbf j}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** when the box tilts counterclockwise the contact point runs to the left along the cylinder, by the same angle as the box.

> [!derivation] Rolling without slipping: equal arcs
> **Law:** without slip the contact point sweeps equal arc lengths on both bodies
> **Source:** Notes.pdf, Eq. 13.3; Notes.pdf, Eq. 13.2
>
> On the cylinder the contact point has moved from $T$ to $C$ along an arc of radius $R$ and angle $\varphi$. On the box it has moved from $M$ along the straight bottom face. The tilt lowers the left half of the box onto the cylinder, so the contact moves towards the left end of the face, along minus $\mathbf i_B$ (the next box checks this sign with the velocity field).
>
> $$\begin{aligned}
> s_{\mathrm{cyl}}(t) - s_{\mathrm{cyl}}(0) &= R\,\varphi \quad &\text{(arc of a circle: radius times angle in radians)} \\
> s_{\mathrm{box}}(t) - s_{\mathrm{box}}(0) &= s_{\mathrm{cyl}}(t) - s_{\mathrm{cyl}}(0) \quad &\text{(Eq. 13.3)} \\
> \mathbf r_M^C &= -R\,\varphi\,\mathbf i_B \quad &\text{(distance $R\varphi$ along the face, towards its left end)} \\
> \mathbf r_0^M &= \mathbf r_0^C - \mathbf r_M^C \quad &\text{(sum of segments: $O$ to $C$, then $C$ back to $M$)} \\
> &= R\,\mathbf j_B + R\,\varphi\,\mathbf i_B \quad &\text{(previous box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^M = R\,\varphi\,\mathbf i_B + R\,\mathbf j_B}$$
>
> **Units:** $[\mathrm L] = [\mathrm L][1]$, the angle is dimensionless
> **Meaning:** the middle of the bottom face sits at the distance $R\varphi$ from the contact point, measured along the face; the contact stays on the face while that distance is smaller than $b/2$.

> [!derivation] Check: the contact body point has zero velocity
> **Law:** rolling without slip on a fixed body; velocity field of the rigid body
> **Source:** Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf v_0^M &= \frac{d}{dt}\left(R\,\varphi\,\mathbf i_B + R\,\mathbf j_B\right) = R\,\dot\varphi\,\mathbf i_B + R\,\varphi\,\dot{\mathbf i}_B + R\,\dot{\mathbf j}_B \quad &\text{(product rule; $R$ constant)} \\
> &= R\,\dot\varphi\,\mathbf i_B + R\,\varphi\,\dot\varphi\,\mathbf j_B - R\,\dot\varphi\,\mathbf i_B \quad &\text{(Poisson derivatives of the rotation box)} \\
> &= R\,\varphi\,\dot\varphi\,\mathbf j_B \quad &\text{(the terms along $\mathbf i_B$ cancel)} \\
> \mathbf v_0^{C(B)} &= \mathbf v_0^M + \boldsymbol\omega_{B0}\times\mathbf r_M^C \quad &\text{(velocity field from $M$ to the body point at $C$, Eq. 9.3)} \\
> \boldsymbol\omega_{B0}\times\mathbf r_M^C &= \dot\varphi\,\mathbf k\times\left(-R\,\varphi\,\mathbf i_B\right) = -R\,\varphi\,\dot\varphi\,\mathbf j_B \quad &\text{($\mathbf k\times\mathbf i_B = \mathbf j_B$)} \\
> \mathbf v_0^{C(B)} &= R\,\varphi\,\dot\varphi\,\mathbf j_B - R\,\varphi\,\dot\varphi\,\mathbf j_B = \mathbf 0 \quad &\text{(add)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^{C(B)} = \mathbf 0 = \mathbf v_0^{C(\mathrm{cyl})}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the body point of the box at the contact has the velocity of the fixed cylinder there, zero, which is Eq. 13.5. With the opposite sign of the segment from $M$ to $C$ the result would be $2R\varphi\dot\varphi\,\mathbf j_B$ plus a tangential term, a slipping contact; this confirms the choice of the previous box.

> [!derivation] Position, velocity and acceleration of G
> **Law:** position vector as a sum of segments; time derivatives with the product rule and Poisson's formula
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> The centre of mass is at the centre of the box (Center of Mass section), at the height $h/2$ above $M$ along $\mathbf j_B$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \mathbf r_0^M + \frac h2\,\mathbf j_B = R\,\varphi\,\mathbf i_B + \left(R + \frac h2\right)\mathbf j_B \quad &\text{(sum of segments)} \\
> x_G &= \mathbf r_0^G\cdot\mathbf i = R\,\varphi\cos\varphi - \left(R + \frac h2\right)\sin\varphi \quad &\text{(components of $\mathbf i_B$ and $\mathbf j_B$ along $\mathbf i$)} \\
> y_G &= \mathbf r_0^G\cdot\mathbf j = R\,\varphi\sin\varphi + \left(R + \frac h2\right)\cos\varphi \quad &\text{(components along $\mathbf j$)} \\
> \mathbf v_0^G &= R\,\dot\varphi\,\mathbf i_B + R\,\varphi\,\dot\varphi\,\mathbf j_B - \left(R + \frac h2\right)\dot\varphi\,\mathbf i_B \quad &\text{(product rule and Poisson derivatives)} \\
> &= -\frac h2\,\dot\varphi\,\mathbf i_B + R\,\varphi\,\dot\varphi\,\mathbf j_B \quad &\text{(collect along $\mathbf i_B$)} \\
> \mathbf a_0^G &= -\frac h2\,\ddot\varphi\,\mathbf i_B - \frac h2\,\dot\varphi\,\dot{\mathbf i}_B + R\left(\dot\varphi^2 + \varphi\,\ddot\varphi\right)\mathbf j_B + R\,\varphi\,\dot\varphi\,\dot{\mathbf j}_B \quad &\text{(product rule; derivative of $\varphi\dot\varphi$ by the product rule)} \\
> &= -\frac h2\,\ddot\varphi\,\mathbf i_B - \frac h2\,\dot\varphi^2\,\mathbf j_B + R\left(\dot\varphi^2 + \varphi\,\ddot\varphi\right)\mathbf j_B - R\,\varphi\,\dot\varphi^2\,\mathbf i_B \quad &\text{(Poisson derivatives)} \\
> &= \left(-\frac h2\,\ddot\varphi - R\,\varphi\,\dot\varphi^2\right)\mathbf i_B + \left(R\,\varphi\,\ddot\varphi + \left(R - \frac h2\right)\dot\varphi^2\right)\mathbf j_B \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = -\frac h2\,\dot\varphi\,\mathbf i_B + R\,\varphi\,\dot\varphi\,\mathbf j_B, \qquad \mathbf a_0^G = \left(-\frac h2\,\ddot\varphi - R\,\varphi\,\dot\varphi^2\right)\mathbf i_B + \left(R\,\varphi\,\ddot\varphi + \left(R - \frac h2\right)\dot\varphi^2\right)\mathbf j_B}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** the velocity of $G$ is the rotation about the contact point at rest: $\boldsymbol\omega_{B0}\times\mathbf r_C^G$ with $\mathbf r_C^G = R\varphi\,\mathbf i_B + \tfrac h2\,\mathbf j_B$ gives the same two components.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and moment of inertia about the axis through G normal to the plane
> **Law:** first symmetry theorem; definition of the moment of inertia as an integral over the volume
> **Source:** Notes.pdf, Sec. 10.3; Notes.pdf, Eq. 10.8; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; [Lecture 8, Slide 10]
>
> Coordinates $x_B, y_B, z_B$ along $\mathbf i_B, \mathbf j_B, \mathbf k$ from the centre of the box; the box occupies $|x_B| \le b/2$, $|y_B| \le h/2$, $|z_B| \le c/2$. Homogeneous: $dm = \rho\,dx_B\,dy_B\,dz_B$ with $\rho$ the density.
>
> $$\begin{aligned}
> \rho &= \frac{m}{b\,h\,c} \quad &\text{(mass over volume)} \\
> x_{BG} &= y_{BG} = z_{BG} = 0 \quad &\text{(the three coordinate planes are planes of symmetry: first symmetry theorem)} \\
> I_{z_B} &= \int(x_B^2 + y_B^2)\,dm = \rho\int_{-c/2}^{c/2}\int_{-h/2}^{h/2}\int_{-b/2}^{b/2}(x_B^2 + y_B^2)\,dx_B\,dy_B\,dz_B \quad &\text{(Eq. 10.11)} \\
> \int_{-b/2}^{b/2}x_B^2\,dx_B &= \left[\frac{x_B^3}{3}\right]_{-b/2}^{b/2} = \frac{b^3}{24} - \left(-\frac{b^3}{24}\right) = \frac{b^3}{12} \quad &\text{(antiderivative; Barrow with both limits)} \\
> \int_{-h/2}^{h/2}y_B^2\,dy_B &= \left[\frac{y_B^3}{3}\right]_{-h/2}^{h/2} = \frac{h^3}{12} \quad &\text{(same steps)} \\
> I_{z_B} &= \rho\,c\left(h\,\frac{b^3}{12} + b\,\frac{h^3}{12}\right) \quad &\text{(the other two integrals give the lengths $h$, $b$ and $c$)} \\
> &= \frac{m}{b\,h\,c}\cdot\frac{c\,b\,h\left(b^2 + h^2\right)}{12} = \frac{m\left(b^2 + h^2\right)}{12} \quad &\text{(value of $\rho$)} \\
> P_{x_Bz_B} &= \int x_B\,z_B\,dm = 0, \qquad P_{y_Bz_B} = \int y_B\,z_B\,dm = 0 \quad &\text{(odd integrand in $z_B$ over a symmetric interval)}
> \end{aligned}$$
>
> $$\boxed{G \text{ at the centre of the box}, \qquad I_G = I_{z_B} = \frac{m\left(b^2 + h^2\right)}{12}, \qquad P_{x_Bz_B} = P_{y_Bz_B} = 0}$$
>
> **Units:** $\rho$ in kg/m$^3$; the moment of inertia in $[\mathrm M][\mathrm L^2]$
> **Meaning:** the depth $c$ cancels, so the box behaves as a rectangular plate. The two other moments of the tensor depend on $c$ but are not needed: with zero products of inertia with $\mathbf k$ the angular momentum of a plane rotation about $\mathbf k$ only involves $I_G$.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum about $G$ from the inertia tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = m\,\dot\varphi\left(-\frac h2\,\mathbf i_B + R\,\varphi\,\mathbf j_B\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \bar{\bar I}_G\cdot\boldsymbol\omega_{B0} = I_G\,\dot\varphi\,\mathbf k \quad &\text{(Eq. 11.12; zero products with $\mathbf k$)} \\
> \left(v_0^G\right)^2 &= \dot\varphi^2\left(\frac{h^2}{4} + R^2\varphi^2\right) \quad &\text{(sum of the squared components in the orthonormal basis $\mathcal B_B$)} \\
> T_0 &= \frac12\,m\left(v_0^G\right)^2 + \frac12\,I_G\,\dot\varphi^2 \quad &\text{(Eq. 11.31)} \\
> &= \frac12\,m\,\dot\varphi^2\left(\frac{h^2}{4} + R^2\varphi^2 + \frac{b^2}{12} + \frac{h^2}{12}\right) \quad &\text{(substitute)} \\
> &= \frac12\,m\,\dot\varphi^2\left(\frac{b^2}{12} + \frac{h^2}{3} + R^2\varphi^2\right) \quad &\text{($\tfrac14 + \tfrac1{12} = \tfrac13$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = m\,\dot\varphi\left(-\frac h2\,\mathbf i_B + R\,\varphi\,\mathbf j_B\right), \qquad \mathbf H_{G,0} = \frac{m\left(b^2 + h^2\right)}{12}\,\dot\varphi\,\mathbf k, \qquad T_0 = \frac12\,m\left(\frac{b^2}{12} + \frac{h^2}{3} + R^2\varphi^2\right)\dot\varphi^2}$$
>
> **Units:** kg m/s, kg m$^2$/s and J
> **Meaning:** the bracket of the kinetic energy times $m$ is the moment of inertia about the contact point (Steiner from $G$ with the arm of length squared $h^2/4 + R^2\varphi^2$); it grows as the box rolls away from the top.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb12-fbd.svg]]

The forces on the box, in the inertial frame (no inertia forces):

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf j = -mg\left(\sin\varphi\,\mathbf i_B + \cos\varphi\,\mathbf j_B\right)$ | applied |
| Normal reaction | $C$ | $N\,\mathbf j_B$, $N$ unknown (unilateral: positive while in contact) | constraint |
| Friction | $C$ | $F\,\mathbf i_B$, $F$ unknown (no slip: static friction) | constraint |

> [!derivation] Force equation in the body basis
> **Law:** Newton's second law for the centre of mass of a rigid body
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Sec. 13.2; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= F\,\mathbf i_B + N\,\mathbf j_B - mg\left(\sin\varphi\,\mathbf i_B + \cos\varphi\,\mathbf j_B\right) \quad &\text{(Eq. 12.8 with the forces of the table)} \\
> m\left(-\frac h2\,\ddot\varphi - R\,\varphi\,\dot\varphi^2\right) &= F - mg\sin\varphi \quad &\text{($\mathbf i_B$ component)} \\
> m\left(R\,\varphi\,\ddot\varphi + \left(R - \frac h2\right)\dot\varphi^2\right) &= N - mg\cos\varphi \quad &\text{($\mathbf j_B$ component)}
> \end{aligned}$$
>
> $$\boxed{F = mg\sin\varphi - m\left(\frac h2\,\ddot\varphi + R\,\varphi\,\dot\varphi^2\right), \qquad N = mg\cos\varphi + m\left(R\,\varphi\,\ddot\varphi + \left(R - \frac h2\right)\dot\varphi^2\right)}$$
>
> **Units:** $[\mathrm M][\mathrm{L\,T^{-2}}]$, N, in every term
> **Meaning:** at rest in the initial position the contact force is the vertical reaction $N$ equal to the weight; once the box moves, friction is needed to keep the contact point at rest.

> [!derivation] Moment equation about G
> **Law:** moment equation about the centre of mass; vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; [Lecture 10, Slide 5]
>
> The pole is $G$: the extra term of Eq. 12.13 is the product of the velocity of $G$ with itself, zero, and the weight has no arm. The arm of the contact force goes from $G$ to $C$.
>
> $$\begin{aligned}
> \mathbf r_G^C &= \mathbf r_0^C - \mathbf r_0^G = R\,\mathbf j_B - R\,\varphi\,\mathbf i_B - \left(R + \frac h2\right)\mathbf j_B = -R\,\varphi\,\mathbf i_B - \frac h2\,\mathbf j_B \quad &\text{(head minus tail)} \\
> \mathbf M_G &= \mathbf r_G^C\times\left(F\,\mathbf i_B + N\,\mathbf j_B\right) = \begin{vmatrix} \mathbf i_B & \mathbf j_B & \mathbf k \cr -R\varphi & -h/2 & 0 \cr F & N & 0 \end{vmatrix} \quad &\text{(determinant in the basis $\mathcal B_B$)} \\
> &= \mathbf i_B\,(0) - \mathbf j_B\,(0) + \mathbf k\left(-R\,\varphi\,N - \left(-\frac h2\right)F\right) \quad &\text{(expand along the first row)} \\
> &= \left(\frac h2\,F - R\,\varphi\,N\right)\mathbf k \quad &\text{(simplify)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= I_G\,\ddot\varphi\,\mathbf k + I_G\,\dot\varphi\,\dot{\mathbf k} = I_G\,\ddot\varphi\,\mathbf k \quad &\text{(product rule; $\mathbf k$ is fixed)} \\
> I_G\,\ddot\varphi &= \frac h2\,F - R\,\varphi\,N \quad &\text{(equate the $\mathbf k$ components)}
> \end{aligned}$$
>
> $$\boxed{\frac{m\left(b^2 + h^2\right)}{12}\,\ddot\varphi = \frac h2\,F - R\,\varphi\,N}$$
>
> **Units:** $[\mathrm{M\,L^2}][\mathrm{T^{-2}}]$ on the left; $[\mathrm L][\mathrm{M\,L\,T^{-2}}]$ on the right, N m
> **Meaning:** the friction force, applied $h/2$ below $G$, and the normal reaction, applied $R\varphi$ to the side of $G$, are the only torques about the centre of mass.

> [!derivation] Equation of motion of the angle phi
> **Law:** elimination of the two contact unknowns between the three scalar equations
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 14.1
>
> $$\begin{aligned}
> \frac h2\,F &= \frac h2\,mg\sin\varphi - m\,\frac{h^2}{4}\,\ddot\varphi - m\,\frac h2\,R\,\varphi\,\dot\varphi^2 \quad &\text{(multiply the friction by $h/2$)} \\
> R\,\varphi\,N &= R\,\varphi\,mg\cos\varphi + m\,R^2\varphi^2\,\ddot\varphi + m\,R\,\varphi\left(R - \frac h2\right)\dot\varphi^2 \quad &\text{(multiply the normal reaction by $R\varphi$)} \\
> I_G\,\ddot\varphi &= \frac h2\,mg\sin\varphi - m\,\frac{h^2}{4}\,\ddot\varphi - m\,R^2\varphi^2\,\ddot\varphi - m\,R^2\varphi\,\dot\varphi^2 - mg\,R\,\varphi\cos\varphi \quad &\text{(subtract; the terms $\pm m\tfrac h2 R\varphi\dot\varphi^2$ cancel)} \\
> \left(\frac{b^2 + h^2}{12} + \frac{h^2}{4} + R^2\varphi^2\right)\ddot\varphi + R^2\varphi\,\dot\varphi^2 + g\left(R\,\varphi\cos\varphi - \frac h2\sin\varphi\right) &= 0 \quad &\text{(divide by $m$ and move every term to the left)} \\
> \frac{b^2 + h^2}{12} + \frac{h^2}{4} &= \frac{b^2}{12} + \frac{h^2}{3} \quad &\text{(add the fractions)}
> \end{aligned}$$
>
> $$\boxed{\left(\frac{b^2}{12} + \frac{h^2}{3} + R^2\varphi^2\right)\ddot\varphi + R^2\,\varphi\,\dot\varphi^2 + g\left(R\,\varphi\cos\varphi - \frac h2\sin\varphi\right) = 0}$$
>
> **Units:** $[\mathrm L^2][\mathrm{T^{-2}}]$ in every term (m$^2$/s$^2$)
> **Meaning:** a single second-order differential equation for the single degree of freedom. The gravity term contains the restoring part $gR\varphi\cos\varphi$, due to the shift of the contact point under $G$, and the overturning part $-g\tfrac h2\sin\varphi$, due to the height of $G$ above the face.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Differential equation of motion of $\varphi$ | $\left(\tfrac{b^2}{12} + \tfrac{h^2}{3} + R^2\varphi^2\right)\ddot\varphi + R^2\varphi\dot\varphi^2 + g\left(R\varphi\cos\varphi - \tfrac h2\sin\varphi\right) = 0$ |
| Contact forces (by-product) | $F = mg\sin\varphi - m\left(\tfrac h2\ddot\varphi + R\varphi\dot\varphi^2\right)$ along $\mathbf i_B$; $N = mg\cos\varphi + m\left(R\varphi\ddot\varphi + (R - \tfrac h2)\dot\varphi^2\right)$ along $\mathbf j_B$ |
| Validity | the contact stays on the bottom face while $R\lvert\varphi\rvert \lt b/2$; $N \gt 0$ and enough friction |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the equation is checked with the energy integral and with limiting cases.

> [!derivation] Check: conservation of the mechanical energy gives the same equation
> **Law:** the contact force acts at a body point at rest and does no work; the weight is conservative
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> \dot W_{C} &= \left(F\,\mathbf i_B + N\,\mathbf j_B\right)\cdot\mathbf v_0^{C(B)} = 0 \quad &\text{(power of the contact force; zero velocity of $C(B)$)} \\
> E &= T_0 + m\,g\,y_G = \frac12\,m\,J(\varphi)\,\dot\varphi^2 + m\,g\left(R\,\varphi\sin\varphi + \left(R + \frac h2\right)\cos\varphi\right) \quad &\text{(Eq. 12.34, with $J = \tfrac{b^2}{12} + \tfrac{h^2}{3} + R^2\varphi^2$)} \\
> \frac{dJ}{dt} &= \frac{dJ}{d\varphi}\,\dot\varphi = 2R^2\varphi\,\dot\varphi \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\varphi\sin\varphi\right) &= \left(\sin\varphi + \varphi\cos\varphi\right)\dot\varphi \quad &\text{(product and chain rules)} \\
> \frac{dE}{dt} &= m\,J\,\dot\varphi\,\ddot\varphi + m\,R^2\varphi\,\dot\varphi^3 + m\,g\,\dot\varphi\left(R\sin\varphi + R\,\varphi\cos\varphi - \left(R + \frac h2\right)\sin\varphi\right) \quad &\text{(derivative term by term)} \\
> &= m\,\dot\varphi\left[J\,\ddot\varphi + R^2\varphi\,\dot\varphi^2 + g\left(R\,\varphi\cos\varphi - \frac h2\sin\varphi\right)\right] \quad &\text{(the terms $\pm gR\sin\varphi$ cancel; factor out)} \\
> 0 &= m\,\dot\varphi\cdot 0 \quad &\text{(Eq. 12.33: $E$ constant; the bracket is the equation of motion)}
> \end{aligned}$$
>
> $$\boxed{\frac12\left(\frac{b^2}{12} + \frac{h^2}{3} + R^2\varphi^2\right)\dot\varphi^2 + g\left(R\,\varphi\sin\varphi + \left(R + \frac h2\right)\cos\varphi\right) = \text{const}}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]$ (J/kg) in every term
> **Meaning:** a first integral of the equation of motion, obtained without the contact forces; its time derivative reproduces the bracket of the Newtonian equation term by term.

> [!derivation] Small oscillations about the initial position
> **Law:** first-order Taylor expansion about the equilibrium; harmonic oscillator
> **Source:** Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 5.6
>
> $$\begin{aligned}
> \sin\varphi &\approx \varphi, \qquad \cos\varphi \approx 1 \quad &\text{(first order in $\varphi$)} \\
> R^2\varphi^2\,\ddot\varphi &\approx 0, \qquad R^2\varphi\,\dot\varphi^2 \approx 0 \quad &\text{(second and third order: dropped)} \\
> \left(\frac{b^2}{12} + \frac{h^2}{3}\right)\ddot\varphi + g\left(R - \frac h2\right)\varphi &= 0 \quad &\text{(linearized equation)}
> \end{aligned}$$
>
> $$\boxed{\ddot\varphi + \frac{g\left(R - h/2\right)}{b^2/12 + h^2/3}\,\varphi = 0, \qquad \text{stable if } R \gt \frac h2, \qquad \Omega = \sqrt{\frac{12\,g\left(R - h/2\right)}{b^2 + 4h^2}}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}][\mathrm L]/[\mathrm L^2] = [\mathrm{T^{-2}}]$, so the frequency is in rad/s
> **Meaning:** the height of $G$ has a minimum at the top position, so the box rocks back, when the height $h/2$ of $G$ above the contact is smaller than the radius $R$ of the cylinder; if $G$ is higher than that, its height has a maximum there and the box falls off.

**Limiting cases and consistency:**

* **Knife edge.** For a vanishing radius the equation becomes the one of an inverted pendulum pivoting about $M$: the coefficient of the angular acceleration is the moment of inertia about $M$ divided by the mass, and the only torque is the overturning one of the weight; the top position is then unstable, as expected.
* **Thin plank.** For a vanishing height the overturning term disappears and the box is stable on any cylinder: the contact point moves under the lowered side, which leaves $G$ on the raised side, so the weight always pulls it back.
* **Contact force at rest.** At the initial position with zero velocity the friction is zero and the normal reaction equals the weight.
* **Dimensions.** Every term of the equation of motion is in m$^2$/s$^2$; the frequency is in rad/s.

---

## Problem RB-13: Rolling disk with cavity

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous flat sheet $B$ of mass $m$: a disc of radius $R$ and centre $O$ with a circular hole of diameter $R$. Read from the figure: the hole is tangent to the rim from inside, so its centre $O_h$ is at the distance $R/2$ from $O$. The sheet moves in its own vertical plane on a horizontal rough line with friction coefficient $\mu$; the contact is unilateral. Gravity acts downwards.
* **Fixed frame:** $S_0\{Q; \mathcal B_0\}$, with origin $Q$ at the point of the line touched at the initial instant, $\mathbf i$ along the line to the right (the sense of the initial velocity of $O$), $\mathbf j$ vertical upwards and $\mathbf k$ out of the paper (⊙). It is inertial.
* **Body frame:** $S_B\{O; \mathbf i_B, \mathbf j_B, \mathbf k\}$, with $\mathbf i_B$ from $O$ towards the centre of the hole and $\mathbf j_B$ completing a right-handed basis in the plane.
* **Coordinates:** the abscissa $x$ and the height $y_O$ of $O$, and the angle $\theta$ from $\mathbf i$ to $\mathbf i_B$, positive counterclockwise about $\mathbf k$ (right-hand rule).
* **Initial conditions:** $\theta$ is zero (the hole to the right of $O$, as in the figure), $x$ is zero, $y_O$ is $R$, the velocity of $O$ is $\omega R$ along $\mathbf i$, and the sheet turns clockwise (read from the curved arrow of the figure). A clockwise rotation has its angular velocity into the paper (⊗), along minus $\mathbf k$, so the initial rate of $\theta$ is minus $\omega$.
* **Degrees of freedom:** a rigid body in plane motion has three coordinates. While the contact holds (normal reaction positive), no penetration fixes the height of $O$: two remain, $x$ and $\theta$ (case $\mu$ equal to zero, free slip). Rolling without slipping adds one more relation and leaves one, $\theta$ (case $\mu$ tending to infinity).
* **Unknowns of the dynamics:** the coordinates and the contact force: normal reaction $N$ and friction $F$ (zero for $\mu$ equal to zero, unknown for rolling without slip).

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the sheet (with the hole) | $m$ | kg |
| Radius of the disc | $R$ | m |
| Diameter of the hole; distance from $O$ to its centre | $R$; $R/2$ (read from the figure) | m |
| Friction coefficient | $\mu$ (cases 0 and infinite) | - |
| Initial velocity of $O$ | $\omega R\,\mathbf i$ | m/s |
| Initial angular velocity | $-\omega\,\mathbf k$ (clockwise) | rad/s |
| Gravity | $g$, along $-\mathbf j$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb13-rotation.svg]]

> [!derivation] Body basis: rotation about k by the angle theta
> **Law:** simple rotation about the third axis, positive by the right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right, $\mathbf j$ up; positive $\theta$ is counterclockwise. Triangle of $\mathbf i_B$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Triangle of $\mathbf j_B$: hypotenuse 1, adjacent leg along $\mathbf j$ (cosine), opposite leg along minus $\mathbf i$ (sine), because the tip of $\mathbf j$ turned counterclockwise about the outward $\mathbf k$ moves to the left.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(legs of the triangle of $\mathbf i_B$)} \\
> \mathbf j_B &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(legs of the triangle of $\mathbf j_B$; tip towards minus $\mathbf i$)} \\
> [{}_0R_B] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_B] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_B][{}_0R_B]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf k, \qquad \boldsymbol\alpha_{B0} = \ddot\theta\,\mathbf k \quad &\text{(single rotation about the fixed axis $\mathbf k$)} \\
> \dot{\mathbf i}_B &= \dot\theta\,\mathbf k\times\mathbf i_B = \dot\theta\,\mathbf j_B, \qquad \dot{\mathbf j}_B = \dot\theta\,\mathbf k\times\mathbf j_B = -\dot\theta\,\mathbf i_B \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_B = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \qquad \mathbf j_B = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j, \qquad \boldsymbol\omega_{B0} = \dot\theta\,\mathbf k}$$
>
> **Units:** the matrix is dimensionless; the angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** with the clockwise initial spin the angle starts to decrease: the hole first moves downwards.

![[attachments/EM-SOL/rb13-geometry.svg]]

> [!derivation] Velocity of the contact body point and the no-penetration constraint
> **Law:** velocity field of the rigid body; no penetration at a contact with a fixed line
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.2
>
> The rim is a circle of centre $O$ (the hole touches it at a single point), so the contact point $C$ is always straight below $O$, at the distance $R$.
>
> $$\begin{aligned}
> \mathbf r_0^O &= x\,\mathbf i + y_O\,\mathbf j, \qquad \mathbf r_O^C = -R\,\mathbf j \quad &\text{(coordinates of $O$; the radius to the contact is vertical)} \\
> \mathbf v_0^{C(B)} &= \mathbf v_0^O + \boldsymbol\omega_{B0}\times\mathbf r_O^C = \dot x\,\mathbf i + \dot y_O\,\mathbf j + \dot\theta\,\mathbf k\times\left(-R\,\mathbf j\right) \quad &\text{(velocity field from $O$, Eq. 9.3)} \\
> \dot\theta\,\mathbf k\times\left(-R\,\mathbf j\right) &= -R\,\dot\theta\left(\mathbf k\times\mathbf j\right) = R\,\dot\theta\,\mathbf i \quad &\text{($\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf v_0^{C(B)} &= \left(\dot x + R\,\dot\theta\right)\mathbf i + \dot y_O\,\mathbf j \quad &\text{(collect)} \\
> \mathbf v_0^{C(B)}\cdot\mathbf j &= \dot y_O = 0 \quad &\text{(Eq. 13.1: the line is at rest and the normal is $\mathbf j$)} \\
> y_O(t) - y_O(0) &= \int_0^t \dot y_O\,dt' = 0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{y_O = R \ \text{(while in contact)}, \qquad \mathbf v_0^{C(B)} = \left(\dot x + R\,\dot\theta\right)\mathbf i}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$; the height in $[\mathrm L]$
> **Meaning:** the bracket is the slip velocity of the sheet on the line; it is zero when the sheet rolls without slipping.

> [!derivation] Part (d): initial velocity of the contact point
> **Law:** previous box at the initial instant
> **Source:** Notes.pdf, Eq. 9.3; Problems.pdf, p. 45
>
> $$\begin{aligned}
> \dot x(0) &= \omega R, \qquad \dot\theta(0) = -\omega \quad &\text{(initial data: clockwise spin)} \\
> \mathbf v_0^{C(B)}(0) &= \left(\omega R + R\,(-\omega)\right)\mathbf i \quad &\text{(substitute)} \\
> &= \mathbf 0 \quad &\text{(the two terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^{C(B)}(0) = \mathbf 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the sheet is launched rolling without slip: the contact point is at rest at the initial instant, whatever the friction coefficient.

> [!derivation] Position, velocity and acceleration of G
> **Law:** position vector as a sum of segments; time derivatives with the chain rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> The centre of mass is on the line of $\mathbf i_B$, at the distance $R/6$ from $O$ on the side opposite to the hole (part (a), next section). Right triangle with hypotenuse $OG$ of length $R/6$ along minus $\mathbf i_B$: the horizontal leg $\tfrac R6\cos\theta$ (adjacent to $\theta$) points to the left and the vertical leg $\tfrac R6\sin\theta$ (opposite to $\theta$) points downwards.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \mathbf r_0^O + \mathbf r_O^G = x\,\mathbf i + R\,\mathbf j - \frac R6\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) \quad &\text{(sum of segments; contact kept)} \\
> x_G &= x - \frac R6\cos\theta, \qquad y_G = R - \frac R6\sin\theta \quad &\text{(components)} \\
> \frac{d}{dt}\cos\theta &= -\sin\theta\,\dot\theta, \qquad \frac{d}{dt}\sin\theta = \cos\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \dot x_G &= \dot x + \frac R6\sin\theta\,\dot\theta, \qquad \dot y_G = -\frac R6\cos\theta\,\dot\theta \quad &\text{(derivative of the components)} \\
> \ddot x_G &= \ddot x + \frac R6\left(\cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta\right) \quad &\text{(product rule on $\sin\theta\,\dot\theta$)} \\
> \ddot y_G &= -\frac R6\left(\cos\theta\,\ddot\theta - \sin\theta\,\dot\theta^2\right) \quad &\text{(product rule on $\cos\theta\,\dot\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \left(\dot x + \frac R6\sin\theta\,\dot\theta\right)\mathbf i - \frac R6\cos\theta\,\dot\theta\,\mathbf j, \qquad \ddot y_G = -\frac R6\left(\cos\theta\,\ddot\theta - \sin\theta\,\dot\theta^2\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the centre of mass circles around $O$ at the radius $R/6$ while $O$ translates; the same velocity follows from the velocity field, $\dot x\,\mathbf i + \dot\theta\,\mathbf k\times(-\tfrac R6\,\mathbf i_B)$.

### Center of Mass and Inertia Tensor

![[attachments/EM-SOL/rb13-composite.svg]]

> [!derivation] Part (a): centre of mass of the disc with a hole
> **Law:** additivity of the first moment over disjoint domains, the hole entering with negative mass; first symmetry theorem
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 17]
>
> Surface density $\sigma$ (homogeneous sheet). The full disc $D$ and the hole $H$ are each symmetric about their own centre, so each has its centre of mass at its centre.
>
> $$\begin{aligned}
> A &= \pi R^2 - \pi\left(\frac R2\right)^2 = \frac{3\pi R^2}{4} \quad &\text{(area of the sheet: disc minus hole)} \\
> \sigma &= \frac mA = \frac{4m}{3\pi R^2} \quad &\text{(mass over area)} \\
> m_D &= \sigma\,\pi R^2 = \frac{4m}{3}, \qquad m_H = \sigma\,\pi\left(\frac R2\right)^2 = \frac m3 \quad &\text{(masses of the full disc and of the hole)} \\
> m\,\mathbf r_O^G &= m_D\,\mathbf r_O^O - m_H\,\mathbf r_O^{O_h} \quad &\text{(additivity, the hole with negative mass)} \\
> &= \frac{4m}{3}\,\mathbf 0 - \frac m3\cdot\frac R2\,\mathbf i_B = -\frac{mR}{6}\,\mathbf i_B \quad &\text{(the centre of the hole is at $R/2$ along $\mathbf i_B$)} \\
> \mathbf r_O^G &= -\frac R6\,\mathbf i_B \quad &\text{(divide by $m$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_O^G = -\frac R6\,\mathbf i_B, \qquad \overline{OG} = \frac R6 \ \text{on the side opposite to the hole}}$$
>
> **Units:** $\sigma$ in kg/m$^2$; the distance in $[\mathrm L]$
> **Meaning:** removing material on one side moves the centre of mass to the other side; the line $OO_h$ is an axis of symmetry, so $G$ lies on it.

> [!derivation] Part (b): moment of inertia about the axis through O normal to the sheet
> **Law:** moment of inertia as an integral in polar coordinates (jacobian $r$); parallel axis theorem for the hole; additivity
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 16]; [Lecture 8, Slide 17]
>
> Polar coordinates $(r, \alpha)$ about the centre of each circle; area element $r\,dr\,d\alpha$, so $dm = \sigma\,r\,dr\,d\alpha$; the squared distance to the normal axis through the centre is $r^2$.
>
> $$\begin{aligned}
> I_{D,O} &= \int_0^{2\pi}\int_0^{R}\sigma\,r^2\,r\,dr\,d\alpha = 2\pi\sigma\left[\frac{r^4}{4}\right]_0^R = 2\pi\sigma\left(\frac{R^4}{4} - 0\right) \quad &\text{(Eq. 10.11; antiderivative; Barrow)} \\
> &= \frac{\pi\sigma R^4}{2} = \frac{4m}{3\pi R^2}\cdot\frac{\pi R^4}{2} = \frac23\,m R^2 \quad &\text{(value of $\sigma$)} \\
> I_{H,O_h} &= \int_0^{2\pi}\int_0^{R/2}\sigma\,r^3\,dr\,d\alpha = 2\pi\sigma\left[\frac{r^4}{4}\right]_0^{R/2} = 2\pi\sigma\,\frac{R^4}{64} \quad &\text{(same integral, radius $R/2$)} \\
> &= \frac{4m}{3\pi R^2}\cdot\frac{\pi R^4}{32} = \frac{m R^2}{24} \quad &\text{(value of $\sigma$)} \\
> I_{H,O} &= I_{H,O_h} + m_H\left(\frac R2\right)^2 = \frac{mR^2}{24} + \frac m3\cdot\frac{R^2}{4} \quad &\text{(parallel axis theorem from $O_h$ to $O$)} \\
> &= \frac{mR^2}{24} + \frac{2mR^2}{24} = \frac{mR^2}{8} \quad &\text{(common denominator)} \\
> I_O &= I_{D,O} - I_{H,O} = \frac23\,mR^2 - \frac18\,mR^2 = \frac{16 - 3}{24}\,mR^2 \quad &\text{(additivity: the hole is subtracted)}
> \end{aligned}$$
>
> $$\boxed{I_O = \frac{13}{24}\,m R^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** a full disc of mass $m$ would have $\tfrac12 mR^2$; the sheet has slightly more because the hole removes mass near the centre and the remaining mass is, on average, farther from $O$.

> [!derivation] Part (c): moment of inertia about the centre of mass
> **Law:** parallel axis theorem between $G$ and $O$; flat body
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8.1; Notes.pdf, Eq. 10.22; [Lecture 8, Slide 16]
>
> $$\begin{aligned}
> I_O &= I_G + m\,\overline{OG}^2 \quad &\text{(parallel axis theorem: the axis through $G$ is the one of least moment)} \\
> I_G &= \frac{13}{24}\,mR^2 - m\,\frac{R^2}{36} \quad &\text{(distance $R/6$)} \\
> &= \frac{39 - 2}{72}\,mR^2 = \frac{37}{72}\,mR^2 \quad &\text{(common denominator 72)} \\
> P_{xz} &= \int x\,z\,dm = 0, \qquad P_{yz} = \int y\,z\,dm = 0 \quad &\text{(flat body in the plane $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{I_G = \frac{37}{72}\,m R^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** with zero products of inertia with the normal axis, the angular momentum about $G$ of the plane rotation is $I_G\dot\theta\,\mathbf k$.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G, kinetic and potential energy
> **Law:** linear momentum from $G$; angular momentum about $G$; Koenig's decomposition; potential of the weight
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = m\left(\dot x + \frac R6\sin\theta\,\dot\theta\right)\mathbf i - m\,\frac R6\cos\theta\,\dot\theta\,\mathbf j \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= I_G\,\dot\theta\,\mathbf k = \frac{37}{72}\,mR^2\,\dot\theta\,\mathbf k \quad &\text{(Eq. 11.12; flat body)} \\
> \left(v_0^G\right)^2 &= \dot x^2 + \frac R3\sin\theta\,\dot x\,\dot\theta + \frac{R^2}{36}\left(\sin^2\theta + \cos^2\theta\right)\dot\theta^2 \quad &\text{(square of the binomial plus the second component)} \\
> T_0 &= \frac12\,m\left(v_0^G\right)^2 + \frac12\,I_G\,\dot\theta^2 \quad &\text{(Eq. 11.31)} \\
> &= \frac12\,m\left(\dot x^2 + \frac R3\sin\theta\,\dot x\,\dot\theta + \left(\frac{2}{72} + \frac{37}{72}\right)R^2\dot\theta^2\right) \quad &\text{($\sin^2 + \cos^2 = 1$; $\tfrac1{36} = \tfrac2{72}$)} \\
> &= \frac12\,m\left(\dot x^2 + \frac R3\sin\theta\,\dot x\,\dot\theta + \frac{13}{24}\,R^2\dot\theta^2\right) \quad &\text{($\tfrac{39}{72} = \tfrac{13}{24}$)} \\
> V_0 &= m\,g\,y_G = m\,g\,R\left(1 - \frac16\sin\theta\right) \quad &\text{(Eq. 12.34)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \frac m2\left(\dot x^2 + \frac R3\sin\theta\,\dot x\,\dot\theta + \frac{13}{24}R^2\dot\theta^2\right), \qquad V_0 = mgR\left(1 - \frac16\sin\theta\right)}$$
>
> **Units:** J in every term ($[\mathrm{M\,L^2\,T^{-2}}]$)
> **Meaning:** the coefficient $\tfrac{13}{24}$ is $I_O/(mR^2)$: written from $O$, the energy is the translation of $O$, the rotation about $O$ and the cross term due to the offset of $G$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb13-fbd.svg]]

The forces on the sheet while it touches the line, in the inertial frame:

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf j$ | applied |
| Normal reaction | $C$ | $N\,\mathbf j$, with $N \ge 0$ (unilateral) | constraint |
| Friction | $C$ | $F\,\mathbf i$: zero for $\mu$ equal to zero; unknown for rolling without slip | constraint |

> [!derivation] Force and moment equations
> **Law:** Newton's second law for the centre of mass; moment equation about $G$ with the vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The arm of the contact force from $G$: the contact point is $x\,\mathbf i$ (on the line, below $O$).
>
> $$\begin{aligned}
> m\,\ddot x_G &= F, \qquad m\,\ddot y_G = N - mg \quad &\text{(components of Eq. 12.8)} \\
> \mathbf r_G^C &= x\,\mathbf i - \left(x - \frac R6\cos\theta\right)\mathbf i - \left(R - \frac R6\sin\theta\right)\mathbf j = \frac R6\cos\theta\,\mathbf i - \left(R - \frac R6\sin\theta\right)\mathbf j \quad &\text{(head minus tail)} \\
> \mathbf M_G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \tfrac R6\cos\theta & -\left(R - \tfrac R6\sin\theta\right) & 0 \cr F & N & 0 \end{vmatrix} \quad &\text{(moment of the contact force; the weight has no arm)} \\
> &= \mathbf k\left(\frac R6\cos\theta\,N + \left(R - \frac R6\sin\theta\right)F\right) \quad &\text{(expand along the first row: only the $\mathbf k$ term survives)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= I_G\,\ddot\theta\,\mathbf k \quad &\text{(product rule; $\mathbf k$ fixed)} \\
> I_G\,\ddot\theta &= \frac R6\cos\theta\,N + \left(R - \frac R6\sin\theta\right)F \quad &\text{(Eq. 12.14 with the pole at $G$)}
> \end{aligned}$$
>
> $$\boxed{m\,\ddot x_G = F, \qquad N = m\left(g + \ddot y_G\right) = m\left(g - \frac R6\left(\cos\theta\,\ddot\theta - \sin\theta\,\dot\theta^2\right)\right), \qquad \frac{37}{72}\,mR^2\,\ddot\theta = \frac R6\cos\theta\,N + \left(R - \frac R6\sin\theta\right)F}$$
>
> **Units:** N for the force equations; N m for the moment equation
> **Meaning:** three equations for the two coordinates and the two contact forces, completed by the contact law: zero friction, or zero slip velocity.

> [!derivation] Power of the contact force
> **Law:** power of a force applied at a body point
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.33; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> \dot W_C &= \left(F\,\mathbf i + N\,\mathbf j\right)\cdot\mathbf v_0^{C(B)} \quad &\text{(power at the body point in contact)} \\
> &= \left(F\,\mathbf i + N\,\mathbf j\right)\cdot\left(\dot x + R\,\dot\theta\right)\mathbf i = F\left(\dot x + R\,\dot\theta\right) \quad &\text{(contact velocity of the kinematics section)}
> \end{aligned}$$
>
> $$\boxed{\dot W_C = F\left(\dot x + R\,\dot\theta\right)}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}][\mathrm{L\,T^{-1}}]$, W
> **Meaning:** the normal reaction never works; friction works only while the sheet slips. In both limiting cases of the statement the power is zero: with no friction the force is zero, with no slip the velocity is zero. The weight is conservative, so the mechanical energy is conserved in both cases (Eq. 12.33).

#### Part (e): quadratures for mu = 0

> [!derivation] First integral of the horizontal momentum
> **Law:** horizontal component of the force equation with no friction; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 11.3
>
> $$\begin{aligned}
> m\,\ddot x_G &= 0 \quad &\text{(no horizontal force)} \\
> \dot x_G(t) - \dot x_G(0) &= \int_0^t \ddot x_G\,dt' = 0 \quad &\text{(Barrow's rule)} \\
> \dot x_G(0) &= \omega R + \frac R6\sin 0\cdot(-\omega) = \omega R \quad &\text{(initial data)} \\
> \dot x + \frac R6\sin\theta\,\dot\theta &= \omega R \quad &\text{(velocity of $G$ of the kinematics section)} \\
> 6\,\dot x + R\,\dot\theta\sin\theta &= 6\,\omega R \quad &\text{(multiply by 6)} \\
> x(t) &= \omega R\,t - \frac R6\int_0^t\sin\theta\,\dot\theta\,dt' \quad &\text{(integrate from 0, with $x(0)$ zero)} \\
> \int_0^t\sin\theta\,\dot\theta\,dt' &= \int_0^{\theta}\sin u\,du = \left[-\cos u\right]_0^{\theta} = 1 - \cos\theta \quad &\text{(substitution $u = \theta(t')$, $du = \dot\theta\,dt'$; Barrow)}
> \end{aligned}$$
>
> $$\boxed{6\,\dot x + R\,\dot\theta\sin\theta = 6\,\omega R, \qquad x(t) = \omega R\,t - \frac R6\left(1 - \cos\theta(t)\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm L]$ in every term
> **Meaning:** with no friction the centre of mass keeps its initial horizontal velocity $\omega R$; $O$ oscillates about that uniform motion as $G$ turns around it.

> [!derivation] First integral of the energy
> **Law:** conservation of the mechanical energy (no work of the contact force)
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> T_0 + V_0 &= T_0(0) + V_0(0) \quad &\text{(Eq. 12.33)} \\
> \frac{48}{m}\left(T_0 + V_0\right) &= 24\,\dot x^2 + 8R\sin\theta\,\dot x\,\dot\theta + 13R^2\dot\theta^2 + 48gR - 8gR\sin\theta \quad &\text{(multiply the expressions of $T_0$ and $V_0$ by $48/m$)} \\
> \frac{48}{m}\left(T_0(0) + V_0(0)\right) &= 24\,\omega^2R^2 + 0 + 13R^2\omega^2 + 48gR - 0 \quad &\text{(initial data; $\sin 0 = 0$)} \\
> 24\,\dot x^2 + 13\,\dot\theta^2R^2 + 8\,\dot x\,\dot\theta R\sin\theta - 8gR\sin\theta &= 37\,\omega^2R^2 \quad &\text{(equate; $48gR$ cancels)}
> \end{aligned}$$
>
> $$\boxed{24\,\dot x^2 + 13\,\dot\theta^2R^2 + 8\,\dot x\,\dot\theta R\sin\theta - 8gR\sin\theta = 37\,\omega^2R^2}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]$ in every term
> **Meaning:** the second first integral. Two first integrals for two degrees of freedom reduce the motion to quadratures.

> [!derivation] Reduction to a quadrature in theta
> **Law:** elimination of the rate of $x$ between the two first integrals; separation of variables
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \dot x &= \omega R - \frac R6\sin\theta\,\dot\theta \quad &\text{(momentum integral)} \\
> 24\,\dot x^2 &= 24\,\omega^2R^2 - 8\,\omega R^2\sin\theta\,\dot\theta + \frac23\,R^2\sin^2\theta\,\dot\theta^2 \quad &\text{(square of the binomial times 24)} \\
> 8R\sin\theta\,\dot x\,\dot\theta &= 8\,\omega R^2\sin\theta\,\dot\theta - \frac43\,R^2\sin^2\theta\,\dot\theta^2 \quad &\text{(cross term)} \\
> R^2\dot\theta^2\left(13 - \frac23\sin^2\theta\right) - 8gR\sin\theta &= 13\,\omega^2R^2 \quad &\text{(substitute in the energy integral; the terms in $\omega\dot\theta$ cancel)} \\
> \dot\theta^2 &= \frac{39\,\omega^2R + 24\,g\sin\theta}{R\left(39 - 2\sin^2\theta\right)} \quad &\text{(multiply by 3 and divide)} \\
> \dot\theta &= -\sqrt{\frac{39\,\omega^2R + 24\,g\sin\theta}{R\left(39 - 2\sin^2\theta\right)}} \quad &\text{(negative root: initial rate $-\omega$)} \\
> t &= \int_{\theta}^{0}\sqrt{\frac{R\left(39 - 2\sin^2u\right)}{39\,\omega^2R + 24\,g\sin u}}\,du \quad &\text{(separate $dt = d\theta/\dot\theta$ and integrate from 0 to $\theta$)}
> \end{aligned}$$
>
> $$\boxed{t(\theta) = \int_{\theta}^{0}\sqrt{\frac{R\left(39 - 2\sin^2u\right)}{39\,\omega^2R + 24\,g\sin u}}\,du, \qquad x = \omega R\,t - \frac R6\left(1 - \cos\theta\right), \qquad y_O = R}$$
>
> **Units:** the integrand is $\sqrt{[\mathrm L]/[\mathrm{L\,T^{-2}}]} = [\mathrm T]$ per radian, so $t$ is in s
> **Meaning:** the quadrature gives $t(\theta)$, its inverse gives $\theta(t)$ and the momentum integral gives $x(t)$. It holds while the root stays real and the contact holds. If $39\omega^2R$ is smaller than $24g$ the rate vanishes where the sine of $\theta$ equals $-39\omega^2R/(24g)$ and the sheet rocks back (the integral is then continued with the other sign of the root).

#### Part (f): quadratures for mu tending to infinity

> [!derivation] Rolling without slip and its integrated form
> **Law:** zero velocity of the contact body point on a fixed line; Barrow's rule
> **Source:** Notes.pdf, Eq. 13.4; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> With an unbounded friction coefficient the friction force can always reach the value that keeps the contact point at rest, and part (d) shows that this point starts at rest. So the sheet rolls without slipping for as long as it touches the line.
>
> $$\begin{aligned}
> \mathbf v_0^{C(B)} &= \left(\dot x + R\,\dot\theta\right)\mathbf i = \mathbf 0 \quad &\text{(Eq. 13.5)} \\
> \dot x &= -R\,\dot\theta \quad &\text{(component along $\mathbf i$)} \\
> x(t) - x(0) &= -R\left(\theta(t) - \theta(0)\right) \quad &\text{(integrate from 0 to $t$, Barrow's rule)} \\
> x &= -R\,\theta \quad &\text{(both zero at the start)}
> \end{aligned}$$
>
> $$\boxed{x = -R\,\theta, \qquad \dot x = -R\,\dot\theta}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** a clockwise rotation (decreasing angle) makes $O$ advance to the right by the arc unrolled on the line.

> [!derivation] Energy integral and quadrature for rolling without slip
> **Law:** conservation of the mechanical energy (the contact force acts at a point at rest); separation of variables
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 13.5; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> 24\,\dot x^2 + 13\,\dot\theta^2R^2 + 8\,\dot x\,\dot\theta R\sin\theta - 8gR\sin\theta &= 37\,\omega^2R^2 \quad &\text{(energy integral of part (e), valid because the power is zero)} \\
> 24R^2\dot\theta^2 + 13R^2\dot\theta^2 - 8R^2\dot\theta^2\sin\theta - 8gR\sin\theta &= 37\,\omega^2R^2 \quad &\text{(substitute the rate of $x$)} \\
> \dot\theta^2R\left(37 - 8\sin\theta\right) - 8g\sin\theta &= 37\,\omega^2R \quad &\text{(collect and divide by $R$)} \\
> \dot\theta &= -\sqrt{\frac{37\,\omega^2R + 8\,g\sin\theta}{R\left(37 - 8\sin\theta\right)}} \quad &\text{(negative root: initial rate $-\omega$)} \\
> t &= \int_{\theta}^{0}\sqrt{\frac{R\left(37 - 8\sin u\right)}{37\,\omega^2R + 8\,g\sin u}}\,du \quad &\text{(separate and integrate from 0 to $\theta$)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta^2R\left(37 - 8\sin\theta\right) - 8g\sin\theta = 37\,\omega^2R, \qquad t(\theta) = \int_{\theta}^{0}\sqrt{\frac{R\left(37 - 8\sin u\right)}{37\,\omega^2R + 8\,g\sin u}}\,du, \qquad x = -R\,\theta}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in every term of the first integral; $t$ in s
> **Meaning:** one degree of freedom, one first integral, one quadrature. The coefficient $37 - 8\sin\theta$ is $24/(mR^2)$ times the moment of inertia about the contact point: $\tfrac{37}{72} mR^2$ plus $m$ times the squared distance from $G$ to $C$.

> [!derivation] Check: the moment equation gives the same motion
> **Law:** time derivative of the energy integral with the chain rule, compared with the moment equation with friction and normal reaction from the force equation
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> \frac{d}{dt}\left[\dot\theta^2R\left(37 - 8\sin\theta\right) - 8g\sin\theta\right] &= 2\dot\theta\ddot\theta R\left(37 - 8\sin\theta\right) - 8R\cos\theta\,\dot\theta^3 - 8g\cos\theta\,\dot\theta \quad &\text{(product and chain rules)} \\
> R\left(37 - 8\sin\theta\right)\ddot\theta - 4R\cos\theta\,\dot\theta^2 - 4g\cos\theta &= 0 \quad &\text{(set to zero and divide by $2\dot\theta$)} \\
> F &= m\,\ddot x_G = m\left(-R\,\ddot\theta + \frac R6\left(\cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta\right)\right) \quad &\text{(force equation with the rate of $x$ of rolling)} \\
> \frac{37}{72}mR^2\ddot\theta - \frac R6\cos\theta\,N - \left(R - \frac R6\sin\theta\right)F &= \frac{mR}{24}\left[R\left(37 - 8\sin\theta\right)\ddot\theta - 4R\cos\theta\,\dot\theta^2 - 4g\cos\theta\right] \quad &\text{(substitute $N$ and $F$ and expand)}
> \end{aligned}$$
>
> $$\boxed{R\left(37 - 8\sin\theta\right)\ddot\theta - 4R\cos\theta\,\dot\theta^2 - 4g\cos\theta = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** the moment equation about $G$ is the same equation of motion times $mR/24$, so the energy integral is exactly its first integral (the expansion was also checked symbolically).

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Centre of mass | on the line from the centre of the hole through $O$, at $R/6$ from $O$ on the side opposite to the hole: $\mathbf r_O^G = -\tfrac R6\,\mathbf i_B$ |
| (b) Moment of inertia about $O$ (normal axis) | $I_O = \tfrac{13}{24}mR^2$ |
| (c) Moment of inertia about $G$ (normal axis) | $I_G = \tfrac{37}{72}mR^2$ |
| (d) Initial velocity of the contact point | $\mathbf 0$: the sheet starts rolling without slip |
| (e) Quadratures, no friction | $6\dot x + R\dot\theta\sin\theta = 6\omega R$; $24\dot x^2 + 13\dot\theta^2R^2 + 8\dot x\dot\theta R\sin\theta - 8gR\sin\theta = 37\omega^2R^2$; hence $\dot\theta^2 R(39 - 2\sin^2\theta) = 39\omega^2R + 24g\sin\theta$, $t = \int_\theta^0\sqrt{R(39 - 2\sin^2u)/(39\omega^2R + 24g\sin u)}\,du$, $x = \omega Rt - \tfrac R6(1 - \cos\theta)$ |
| (f) Quadratures, infinite friction | $x = -R\theta$; $\dot\theta^2R(37 - 8\sin\theta) - 8g\sin\theta = 37\omega^2R$; $t = \int_\theta^0\sqrt{R(37 - 8\sin u)/(37\omega^2R + 8g\sin u)}\,du$ |
| Validity of both | contact while $N = m\left(g - \tfrac R6(\cos\theta\,\ddot\theta - \sin\theta\,\dot\theta^2)\right) \gt 0$ |

**Check against the official key:** the key (Problems.pdf, p. 79) prints, for the frictionless case, the momentum integral and the energy integral, and for the case of infinite friction the single energy integral of rolling without slip. The three expressions obtained in the boxes of parts (e) and (f) are identical term by term, with the same coordinates: $x$ the abscissa of $O$ and $\theta$ the counterclockwise angle of the line from $O$ to the centre of the hole, zero at the start. Match. The key prints no value for parts (a) to (d); the quadratures written here are the explicit next step of its first integrals.

> [!derivation] Check: lift-off with the hole straight below O
> **Law:** vertical force equation with the reduced first integrals; unilateral contact
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Sec. 13.2
>
> With the hole straight below $O$ the sine of $\theta$ is minus one and its cosine is zero, so the angular acceleration drops out of the normal reaction.
>
> $$\begin{aligned}
> N &= m\left(g - \frac R6\left(0\cdot\ddot\theta + \dot\theta^2\right)\right) = m\left(g - \frac{R\,\dot\theta^2}{6}\right) \quad &\text{(normal reaction of the force equation)} \\
> \dot\theta^2 &= \frac{39\,\omega^2R - 24\,g}{37\,R} \quad &\text{(frictionless integral with the sine equal to $-1$)} \\
> N \lt 0 &\iff 39\,\omega^2R - 24\,g \gt 222\,g \iff \omega^2 \gt \frac{82}{13}\,\frac gR \quad &\text{(substitute and solve)} \\
> \dot\theta^2 &= \frac{37\,\omega^2R - 8\,g}{45\,R} \quad &\text{(rolling integral with the sine equal to $-1$)} \\
> N \lt 0 &\iff 37\,\omega^2R - 8\,g \gt 270\,g \iff \omega^2 \gt \frac{278}{37}\,\frac gR \quad &\text{(substitute and solve)}
> \end{aligned}$$
>
> $$\boxed{\text{lift-off if } \omega^2 \gt \frac{82}{13}\frac gR \approx 6.31\,\frac gR \ (\mu = 0), \qquad \omega^2 \gt \frac{278}{37}\frac gR \approx 7.51\,\frac gR \ (\mu \to \infty)}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ on both sides of each inequality
> **Meaning:** when the heavy side passes over the top fast enough, the centripetal acceleration of $G$ exceeds gravity and the sheet jumps off the line; the unilateral contact must therefore be checked along the motion.

**Limiting cases and consistency:**

* **Initial instant.** At the start the sine of $\theta$ is zero and both reduced integrals give a squared rate equal to the square of $\omega$, the initial data.
* **No hole.** For a full disc the centre of mass is at $O$, the terms in the sine of $\theta$ disappear (they come from the offset of $G$) and the rolling disc keeps a constant angular velocity, as a homogeneous disc rolling on a horizontal line must.
* **Slow launch.** If the launch is slow (the numerator of the reduced integral can vanish), the rate of $\theta$ becomes zero before the heavy side reaches the top and the sheet rocks back: it cannot make a full turn.
* **Dimensions.** Every term of the first integrals is in m$^2$/s$^2$ or m/s$^2$ after division by $R$; the quadratures give seconds.

---

## Problem RB-14: Rocking semicircumference

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a thin homogeneous semicircular arc (a wire) of mass $M$, radius $R_0$ and centre $C$, standing on a horizontal plane with its convex side down, rolling on the plane without slipping, in its own vertical plane. Gravity acts downwards. It is turned by $\theta_0$, held at rest and released.
* **Fixed frame:** $S_0\{Q; \mathcal B_0\}$, with origin $Q$ at the point of the plane touched in the rest position (straight below $C$ when the diameter is horizontal), $\mathbf i$ horizontal to the right, $\mathbf j$ vertical upwards, $\mathbf k$ out of the paper (⊙). It is inertial.
* **Body frame:** $S_B\{C; \mathbf i_B, \mathbf j_B, \mathbf k\}$, with $\mathbf j_B$ along the axis of symmetry of the arc, from its middle point towards $C$, and $\mathbf i_B$ along the diameter that joins the two ends of the arc.
* **Coordinates:** the abscissa $x_C$ of the centre $C$ (its height is fixed by the contact) and the angle $\theta$ from $\mathbf i$ to $\mathbf i_B$, positive counterclockwise about $\mathbf k$. Read from the figure: the displaced arc has rolled to the left, which with this convention is a positive angle.
* **Points:** $G$ is the centre of mass, $G_0$ its position in the rest configuration, $P$ the contact point with the plane.
* **Degrees of freedom:** three coordinates in plane motion; no penetration fixes the height of $C$; rolling without slipping links $x_C$ and $\theta$. One degree of freedom remains: $\theta$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the arc, homogeneous | $M$ | kg |
| Radius | $R_0$ | m |
| Distance from $C$ to $G$ (given) | $R_G = 2R_0/\pi$ | m |
| Initial angle, released from rest | $\theta_0$ (with $\lvert\theta_0\rvert \lt \pi/2$) | rad |
| Gravity | $g$, along $-\mathbf j$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb14-rotation.svg]]

> [!derivation] Body basis: rotation about k by the angle theta
> **Law:** simple rotation about the third axis, positive by the right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right, $\mathbf j$ up. Triangle of $\mathbf i_B$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Triangle of $\mathbf j_B$: hypotenuse 1, adjacent leg along $\mathbf j$ (cosine), opposite leg along minus $\mathbf i$ (sine): turning counterclockwise about the outward $\mathbf k$ carries the tip of $\mathbf j$ to the left.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \qquad \mathbf j_B = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_B] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_B] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_B][{}_0R_B]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf k \quad &\text{(single rotation about the fixed axis $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_B = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \qquad \mathbf j_B = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j, \qquad \boldsymbol\omega_{B0} = \dot\theta\,\mathbf k}$$
>
> **Units:** the matrix is dimensionless; the angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** in the rest position the diameter is horizontal and the arc hangs below it; a positive angle tilts the arc counterclockwise.

![[attachments/EM-SOL/rb14-geometry.svg]]

> [!derivation] No penetration and rolling without slip: the contact point
> **Law:** the normal of a circle passes through its centre; zero velocity of the contact body point on a fixed plane; Barrow's rule
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 13.4; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 9.3
>
> The plane is tangent to the circle of the arc at $P$, so the radius $CP$ is vertical and $C$ stays at the height $R_0$ (this holds while $P$ belongs to the arc, that is while the tilt is below a right angle).
>
> $$\begin{aligned}
> \mathbf r_0^C &= x_C\,\mathbf i + R_0\,\mathbf j, \qquad \mathbf r_C^P = -R_0\,\mathbf j \quad &\text{(height fixed by no penetration; vertical radius to the contact)} \\
> \mathbf v_0^{P(B)} &= \dot x_C\,\mathbf i + \dot\theta\,\mathbf k\times\left(-R_0\,\mathbf j\right) \quad &\text{(velocity field from $C$, Eq. 9.3)} \\
> &= \dot x_C\,\mathbf i - R_0\,\dot\theta\left(\mathbf k\times\mathbf j\right) = \left(\dot x_C + R_0\,\dot\theta\right)\mathbf i \quad &\text{($\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \dot x_C + R_0\,\dot\theta &= 0 \quad &\text{(Eq. 13.5: rolling without slip on a plane at rest)} \\
> x_C(t) - x_C(0) &= -R_0\left(\theta(t) - \theta(0)\right) \quad &\text{(integrate from the rest position; Barrow's rule)} \\
> x_C &= -R_0\,\theta \quad &\text{(both zero in the rest position)}
> \end{aligned}$$
>
> $$\boxed{x_C = -R_0\,\theta, \qquad X_C = \lvert x_P(\theta_0) - x_P(0)\rvert = R_0\,\theta_0 \ \text{(to the left)}}$$
>
> **Units:** $[\mathrm L] = [\mathrm L][1]$
> **Meaning:** the contact point is always straight below $C$, so it moves with $C$; the distance it travels along the plane equals the arc of the semicircle unrolled on it, $R_0\theta_0$ (Eq. 13.3: equal arcs).

> [!derivation] Position and velocity of the centre of mass
> **Law:** position vector as a sum of segments; chain rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> $G$ is on the axis of symmetry at the distance $R_G$ below $C$ in the body (next section): along minus $\mathbf j_B$. Right triangle with hypotenuse $CG$ of length $R_G$, tilted by $\theta$ from the downward vertical: the vertical leg $R_G\cos\theta$ (adjacent) points down, the horizontal leg $R_G\sin\theta$ (opposite) points to the right.
>
> $$\begin{aligned}
> \mathbf r_C^G &= -R_G\,\mathbf j_B = R_G\sin\theta\,\mathbf i - R_G\cos\theta\,\mathbf j \quad &\text{($\mathbf j_B$ of the rotation box; legs of the triangle)} \\
> \mathbf r_0^G &= \mathbf r_0^C + \mathbf r_C^G = \left(-R_0\,\theta + R_G\sin\theta\right)\mathbf i + \left(R_0 - R_G\cos\theta\right)\mathbf j \quad &\text{(sum of segments)} \\
> \mathbf r_0^{G_0} &= \left(R_0 - R_G\right)\mathbf j \quad &\text{(value at zero angle)} \\
> \mathbf v_0^G &= \left(-R_0 + R_G\cos\theta\right)\dot\theta\,\mathbf i + R_G\sin\theta\,\dot\theta\,\mathbf j \quad &\text{(chain rule on each component)} \\
> \left(v_0^G\right)^2 &= \dot\theta^2\left(R_0^2 - 2R_0R_G\cos\theta + R_G^2\cos^2\theta + R_G^2\sin^2\theta\right) \quad &\text{(sum of the squared components)} \\
> &= \dot\theta^2\left(R_0^2 - 2R_0R_G\cos\theta + R_G^2\right) \quad &\text{($\cos^2 + \sin^2 = 1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G - \mathbf r_0^{G_0} = \left(R_G\sin\theta - R_0\,\theta\right)\mathbf i + R_G\left(1 - \cos\theta\right)\mathbf j, \qquad \left(v_0^G\right)^2 = \dot\theta^2\left(R_0^2 - 2R_0R_G\cos\theta + R_G^2\right)}$$
>
> **Units:** $[\mathrm L]$ and $[\mathrm{L^2\,T^{-2}}]$
> **Meaning:** the centre of mass rises by $R_G(1 - \cos\theta)$ and moves horizontally by the rolling $-R_0\theta$ of $C$ corrected by $R_G\sin\theta$ in the opposite sense; since $R_0\theta$ exceeds $R_G\sin\theta$, it moves in the sense of rolling.

### Center of Mass and Inertia Tensor

![[attachments/EM-SOL/rb14-arc-element.svg]]

> [!derivation] Centre of mass of the arc (check of the given value)
> **Law:** definition of the centre of mass with a linear density; first symmetry theorem
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 18]
>
> Body coordinates from $C$: a point of the arc is $R_0(\cos\alpha\,\mathbf i_B - \sin\alpha\,\mathbf j_B)$ with $\alpha$ from 0 to $\pi$ (the arc below the diameter). Arc element $ds = R_0\,d\alpha$, linear density $\lambda$.
>
> $$\begin{aligned}
> \lambda &= \frac{M}{\pi R_0}, \qquad dm = \lambda R_0\,d\alpha = \frac M\pi\,d\alpha \quad &\text{(mass over length of a half circle)} \\
> M\,x_{BG} &= \int_0^{\pi}R_0\cos\alpha\,\frac M\pi\,d\alpha = \frac{MR_0}{\pi}\left[\sin\alpha\right]_0^{\pi} = 0 \quad &\text{(antiderivative; Barrow; also by symmetry)} \\
> M\,y_{BG} &= \int_0^{\pi}\left(-R_0\sin\alpha\right)\frac M\pi\,d\alpha = -\frac{MR_0}{\pi}\left[-\cos\alpha\right]_0^{\pi} \quad &\text{(antiderivative)} \\
> &= -\frac{MR_0}{\pi}\left(1 - (-1)\right) = -\frac{2MR_0}{\pi} \quad &\text{(Barrow with both limits)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_C^G = -\frac{2R_0}{\pi}\,\mathbf j_B, \qquad R_G = \frac{2R_0}{\pi}}$$
>
> **Units:** $\lambda$ in kg/m; the distance in $[\mathrm L]$
> **Meaning:** the value given in the statement is confirmed: $G$ is on the axis of symmetry at about $0.637R_0$ from the centre, off the wire itself.

> [!derivation] Moment of inertia about C (normal axis)
> **Law:** definition of the moment of inertia as an integral over the arc
> **Source:** Notes.pdf, Eq. 10.11; [Lecture 8, Slide 10]; [Lecture 8, Slide 18]
>
> Every element of the arc is at the distance $R_0$ from the axis through $C$ normal to the plane.
>
> $$\begin{aligned}
> I_C &= \int r^2\,dm = \int_0^{\pi}R_0^2\,\frac M\pi\,d\alpha \quad &\text{(Eq. 10.11; squared distance $R_0^2$)} \\
> &= \frac{MR_0^2}{\pi}\left[\alpha\right]_0^{\pi} = \frac{MR_0^2}{\pi}\left(\pi - 0\right) \quad &\text{(antiderivative; Barrow)}
> \end{aligned}$$
>
> $$\boxed{I_C = M R_0^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** a thin arc of any angle has all its mass at the radius $R_0$, so its moment about the centre is the mass times the squared radius.

> [!derivation] Moment of inertia about the centre of mass
> **Law:** parallel axis theorem between $C$ and $G$; flat body
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8.1; Notes.pdf, Eq. 10.22; [Lecture 8, Slide 16]
>
> $$\begin{aligned}
> I_C &= I_G + M\,R_G^2 \quad &\text{(parallel axis theorem, axes normal to the plane)} \\
> I_G &= MR_0^2 - M\,\frac{4R_0^2}{\pi^2} \quad &\text{(value of $R_G$ squared)} \\
> &= MR_0^2\left(1 - \frac{4}{\pi^2}\right) \quad &\text{(factor out)} \\
> P_{xz} &= P_{yz} = 0 \quad &\text{(flat body in the plane $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{I_G = MR_0^2\left(1 - \frac{4}{\pi^2}\right) \approx 0.595\,MR_0^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** smaller than the moment about $C$, as it must be for the axis through the centre of mass.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Kinetic and potential energy as functions of theta
> **Law:** Koenig's decomposition; potential of the weight
> **Source:** Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 12.34; [Lecture 9, Slide 10]
>
> $$\begin{aligned}
> \mathbf p_0 &= M\,\mathbf v_0^G, \qquad \mathbf H_{G,0} = I_G\,\dot\theta\,\mathbf k \quad &\text{(Eqs. 11.3 and 11.12; flat body)} \\
> T_0 &= \frac12\,M\left(v_0^G\right)^2 + \frac12\,I_G\,\dot\theta^2 \quad &\text{(Eq. 11.31: translation of $G$ plus rotation about $G$)} \\
> &= \frac12\,M\dot\theta^2\left(R_0^2 - 2R_0R_G\cos\theta + R_G^2 + R_0^2 - R_G^2\right) \quad &\text{(previous boxes; $I_G = M(R_0^2 - R_G^2)$)} \\
> &= M R_0\,\dot\theta^2\left(R_0 - R_G\cos\theta\right) \quad &\text{(simplify)} \\
> V_0 &= M\,g\,y_G = M\,g\left(R_0 - R_G\cos\theta\right) \quad &\text{(Eq. 12.34, zero level on the plane)}
> \end{aligned}$$
>
> $$\boxed{T_0 = M R_0\left(R_0 - R_G\cos\theta\right)\dot\theta^2, \qquad V_0 = M g\left(R_0 - R_G\cos\theta\right)}$$
>
> **Units:** J in both
> **Meaning:** $2MR_0(R_0 - R_G\cos\theta)$ is the moment of inertia about the contact point $P$, the instantaneous centre of rotation, since the squared distance from $P$ to $G$ is $R_0^2 - 2R_0R_G\cos\theta + R_G^2$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb14-fbd.svg]]

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-Mg\,\mathbf j$ | applied, conservative |
| Normal reaction | $P$ | $N\,\mathbf j$ | constraint |
| Friction | $P$ | $F\,\mathbf i$, unknown (no slip) | constraint |

> [!derivation] Power of the contact force and conservation of energy
> **Law:** power of a force at a body point; work and energy theorem
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 13.5; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> \dot W_P &= \left(F\,\mathbf i + N\,\mathbf j\right)\cdot\mathbf v_0^{P(B)} = \left(F\,\mathbf i + N\,\mathbf j\right)\cdot\mathbf 0 = 0 \quad &\text{(the contact body point is at rest)} \\
> T_0 + V_0 &= T_0(0) + V_0(0) = 0 + M g\left(R_0 - R_G\cos\theta_0\right) \quad &\text{(Eq. 12.33; released from rest at $\theta_0$)} \\
> M R_0\left(R_0 - R_G\cos\theta\right)\dot\theta^2 &= M g R_G\left(\cos\theta - \cos\theta_0\right) \quad &\text{(subtract the potential at $\theta$)}
> \end{aligned}$$
>
> $$\boxed{R_0\left(R_0 - R_G\cos\theta\right)\dot\theta^2 = g R_G\left(\cos\theta - \cos\theta_0\right)}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]$ on both sides
> **Meaning:** a first integral: the arc oscillates between $-\theta_0$ and $\theta_0$, where the rate vanishes.

> [!derivation] Equation of motion
> **Law:** time derivative of the energy integral with the chain rule
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \frac{d}{dt}\left[R_0\left(R_0 - R_G\cos\theta\right)\dot\theta^2\right] &= R_0 R_G\sin\theta\,\dot\theta^3 + 2R_0\left(R_0 - R_G\cos\theta\right)\dot\theta\,\ddot\theta \quad &\text{(product and chain rules)} \\
> \frac{d}{dt}\left[g R_G\left(\cos\theta - \cos\theta_0\right)\right] &= -g R_G\sin\theta\,\dot\theta \quad &\text{(chain rule; $\theta_0$ is constant)} \\
> 2R_0\left(R_0 - R_G\cos\theta\right)\ddot\theta + R_0 R_G\sin\theta\,\dot\theta^2 + g R_G\sin\theta &= 0 \quad &\text{(equate and divide by the rate)}
> \end{aligned}$$
>
> $$\boxed{2R_0\left(R_0 - R_G\cos\theta\right)\ddot\theta + R_0 R_G\sin\theta\,\dot\theta^2 + g R_G\sin\theta = 0}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]$ in every term
> **Meaning:** the weight, applied at $G$ which is displaced sideways from the contact point, pulls the arc back towards the rest position.

#### Displacements and energies asked in the statement

> [!derivation] Displacements and potential energy at the released position
> **Law:** position of $G$ of the kinematics section at the angle $\theta_0$; potential of the weight
> **Source:** Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.4
>
> $$\begin{aligned}
> y_{CM} &= R_G\left(1 - \cos\theta_0\right) = \frac{2R_0}{\pi}\left(1 - \cos\theta_0\right) \quad &\text{(rise of $G$)} \\
> x_{CM} &= R_0\,\theta_0 - R_G\sin\theta_0 = R_0\,\theta_0 - \frac{2R_0}{\pi}\sin\theta_0 \quad &\text{(shift of $G$ in the sense of rolling, to the left)} \\
> \Delta V &= M g\,y_{CM} = \frac{2}{\pi}\,M g R_0\left(1 - \cos\theta_0\right) \quad &\text{(Eq. 12.34, zero at the rest position)}
> \end{aligned}$$
>
> $$\boxed{X_C = R_0\theta_0, \qquad y_{CM} = \frac{2R_0}{\pi}\left(1 - \cos\theta_0\right), \qquad x_{CM} = R_0\theta_0 - \frac{2R_0}{\pi}\sin\theta_0, \qquad \Delta V = \frac2\pi M g R_0\left(1 - \cos\theta_0\right)}$$
>
> **Units:** m and J
> **Meaning:** lifting $G$ stores potential energy; it is all returned as kinetic energy when the arc passes through the rest position.

> [!derivation] Kinetic energy at theta = 0, translation and rotation
> **Law:** energy integral at zero angle; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 11.31
>
> $$\begin{aligned}
> \dot\theta^2\big|_{0} &= \frac{g R_G\left(1 - \cos\theta_0\right)}{R_0\left(R_0 - R_G\right)} = \frac{2g\left(1 - \cos\theta_0\right)}{R_0\left(\pi - 2\right)} \quad &\text{(energy integral at zero angle; $R_G/(R_0 - R_G) = 2/(\pi - 2)$)} \\
> T_{\mathrm{tr}} &= \frac12\,M\left(R_0 - R_G\right)^2\dot\theta^2\big|_{0} = \frac12\,MR_0^2\,\frac{(\pi - 2)^2}{\pi^2}\cdot\frac{2g\left(1 - \cos\theta_0\right)}{R_0(\pi - 2)} \quad &\text{(speed of $G$ is $(R_0 - R_G)$ times the rate at zero angle)} \\
> &= \frac{\pi - 2}{\pi^2}\,M g R_0\left(1 - \cos\theta_0\right) \quad &\text{(simplify)} \\
> T_{\mathrm{rot}} &= \frac12\,I_G\,\dot\theta^2\big|_{0} = \frac12\,MR_0^2\,\frac{(\pi - 2)(\pi + 2)}{\pi^2}\cdot\frac{2g\left(1 - \cos\theta_0\right)}{R_0(\pi - 2)} \quad &\text{($1 - 4/\pi^2 = (\pi - 2)(\pi + 2)/\pi^2$)} \\
> &= \frac{\pi + 2}{\pi^2}\,M g R_0\left(1 - \cos\theta_0\right) \quad &\text{(simplify)} \\
> T_{\mathrm{tr}} + T_{\mathrm{rot}} &= \frac{2\pi}{\pi^2}\,M g R_0\left(1 - \cos\theta_0\right) = \frac2\pi\,M g R_0\left(1 - \cos\theta_0\right) \quad &\text{(add: equal to the potential energy released)}
> \end{aligned}$$
>
> $$\boxed{T_0\big|_{\theta = 0} = \frac2\pi M g R_0\left(1 - \cos\theta_0\right), \qquad T_{\mathrm{tr}} = \frac{\pi - 2}{\pi^2}M g R_0\left(1 - \cos\theta_0\right), \qquad T_{\mathrm{rot}} = \frac{\pi + 2}{\pi^2}M g R_0\left(1 - \cos\theta_0\right)}$$
>
> **Units:** J in every term
> **Meaning:** about 18 percent of the energy is translation of $G$ and 82 percent rotation about $G$ at the lowest position; at that instant $G$ moves horizontally, straight above the contact point.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| $I_C$ | $MR_0^2$ |
| $I_G$ | $MR_0^2(1 - 4/\pi^2) \approx 0.595\,MR_0^2$ |
| $X_C$ | $R_0\theta_0$, in the sense of rolling |
| $y_{CM}$ | $\tfrac{2R_0}{\pi}(1 - \cos\theta_0)$, upwards |
| $x_{CM}$ | $R_0\theta_0 - \tfrac{2R_0}{\pi}\sin\theta_0$, in the sense of rolling |
| Potential energy at $\theta_0$ (zero at the rest position) | $\tfrac2\pi MgR_0(1 - \cos\theta_0)$ |
| Kinetic energy at $\theta = 0$ | total $\tfrac2\pi MgR_0(1 - \cos\theta_0)$; translation $\tfrac{\pi - 2}{\pi^2}MgR_0(1 - \cos\theta_0)$; rotation about $G$ $\tfrac{\pi + 2}{\pi^2}MgR_0(1 - \cos\theta_0)$ |
| Equation of motion (by-product) | $2R_0(R_0 - R_G\cos\theta)\ddot\theta + R_0R_G\sin\theta\,\dot\theta^2 + gR_G\sin\theta = 0$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with limiting cases.

> [!derivation] Check: small oscillations
> **Law:** first-order expansion of the equation of motion about zero angle; harmonic oscillator
> **Source:** Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 5.6
>
> $$\begin{aligned}
> 2R_0\left(R_0 - R_G\right)\ddot\theta + g R_G\,\theta &= 0 \quad &\text{(cosine about 1, sine about the angle, the squared rate dropped)} \\
> \Omega^2 &= \frac{g R_G}{2R_0\left(R_0 - R_G\right)} = \frac{g\,(2/\pi)}{2R_0\left(1 - 2/\pi\right)} \quad &\text{(divide; value of $R_G$)} \\
> &= \frac{g}{R_0\left(\pi - 2\right)} \quad &\text{(multiply numerator and denominator by $\pi/2$)}
> \end{aligned}$$
>
> $$\boxed{\Omega = \sqrt{\frac{g}{(\pi - 2)\,R_0}}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]/[\mathrm L] = [\mathrm{T^{-2}}]$
> **Meaning:** the arc rocks like a pendulum of length $(\pi - 2)R_0 \approx 1.14R_0$; small amplitudes give the same period whatever $\theta_0$.

**Limiting cases and consistency:**

* **Energy balance.** The translational and rotational parts add up to the potential energy released, with no loss: the contact force does no work because its body point is at rest.
* **Zero amplitude.** For a vanishing $\theta_0$ every displacement and every energy vanishes; to first order the rise of $G$ is quadratic in the amplitude while the horizontal shift is linear, $(R_0 - R_G)\theta_0$, as for a body rolling about its lowest point.
* **Range.** The results hold while the contact point stays on the arc, that is for an amplitude below a right angle; at a right angle an end of the arc touches the plane.
* **Dimensions.** Lengths in m, energies in J, frequency in rad/s.

---

## Problem RB-15: Rocking hollow hemisphere

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a thin homogeneous hemispherical shell $b$ of mass $m$ and radius $a$, with centre $O$ (the centre of the sphere, in the plane of the rim), resting with its curved side on a smooth horizontal plane. Gravity acts downwards. The contact is a single point $P$ and, being smooth, transmits only a normal force.
* **Fixed frame:** $S_0\{O_1; \mathbf i_1, \mathbf j_1, \mathbf k_1\}$, the frame $O_1x_1y_1z_1$ of the statement: $O_1$ on the plane, $\mathbf k_1$ vertical upwards. It is inertial.
* **Intermediate frame:** $S_1\{G; \mathbf i, \mathbf j', \mathbf k_1\}$, obtained by turning $\mathcal B_0$ by $\psi$ about $\mathbf k_1$; $\mathbf i$ is the horizontal axis $Gx$ of the statement.
* **Auxiliary frame of the statement:** $Gxyz$, that is $S_2\{G; \mathbf i, \mathbf j, \mathbf k\}$, obtained by turning $S_1$ by $\theta$ about $\mathbf i$: $\mathbf k$ is the axis of revolution, oriented from the pole towards the rim, and $\mathbf i$ stays horizontal and normal to it (it is the line of nodes). This frame is not attached to the body: it does not follow the spin.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k\}$, obtained by turning $S_2$ by $\varphi$ about $\mathbf k$.
* **Coordinates:** the five parameters of the statement: $\xi$, $\eta$ (horizontal coordinates of $G$), $\psi$ (precession, from $\mathbf i_1$ to $\mathbf i$), $\theta$ (nutation, from $\mathbf k_1$ to $\mathbf k$) and $\varphi$ (spin about $\mathbf k$). They are the 3-1-3 Euler angles of the course.
* **Degrees of freedom:** a free rigid body has six coordinates; no penetration of the plane fixes the height of $G$ as a function of $\theta$, which leaves five. The plane is smooth, so there is no rolling condition and the five parameters are independent.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the shell, homogeneous, negligible thickness | $m$ | kg |
| Radius | $a$ | m |
| Moment of inertia of a full spherical shell (mass $M$, radius $R$) about a diameter, given | $2MR^2/3$ | kg m$^2$ |
| Plane | horizontal, smooth | - |
| Gravity | $g$, along $-\mathbf k_1$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb15-rot-psi.svg]]

> [!derivation] Precession: rotation by psi about k1
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View from above with $\mathbf k_1$ out of the paper (⊙), $\mathbf i_1$ to the right and $\mathbf j_1$ up; a positive $\psi$ turns counterclockwise. Triangle of $\mathbf i$: hypotenuse 1, adjacent leg along $\mathbf i_1$ (cosine), opposite leg along $\mathbf j_1$ (sine). Triangle of $\mathbf j'$: hypotenuse 1, adjacent leg along $\mathbf j_1$ (cosine), opposite leg along minus $\mathbf i_1$ (sine): the counterclockwise turn about the outward axis carries the tip of $\mathbf j_1$ to the left.
>
> $$\begin{aligned}
> \mathbf i &= \cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1, \qquad \mathbf j' = -\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j'$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k_1 \quad &\text{(rotation about the fixed axis $\mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i = \cos\psi\,\mathbf i_1 + \sin\psi\,\mathbf j_1, \qquad \mathbf j' = -\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k_1}$$
>
> **Units:** dimensionless matrix; angular velocity in $[\mathrm{T^{-1}}]$
> **Meaning:** $\psi$ is the angle between $Gx$ and $O_1x_1$, as the statement defines it; $\mathbf i$ is horizontal by construction.

![[attachments/EM-SOL/rb15-rot-theta.svg]]

> [!derivation] Nutation: rotation by theta about i
> **Law:** simple rotation about the first axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2
>
> View with $\mathbf i$ out of the paper (⊙), $\mathbf j'$ to the right and $\mathbf k_1$ up (right-handed, since the product of $\mathbf j'$ and $\mathbf k_1$ is $\mathbf i$). A positive $\theta$ turns counterclockwise. Triangle of $\mathbf j$: hypotenuse 1, adjacent leg along $\mathbf j'$ (cosine), opposite leg along $\mathbf k_1$ (sine). Triangle of $\mathbf k$: hypotenuse 1, adjacent leg along $\mathbf k_1$ (cosine), opposite leg along minus $\mathbf j'$ (sine): the tip of $\mathbf k_1$, turned counterclockwise about the outward $\mathbf i$, moves to the left.
>
> $$\begin{aligned}
> \mathbf j &= \cos\theta\,\mathbf j' + \sin\theta\,\mathbf k_1, \qquad \mathbf k = -\sin\theta\,\mathbf j' + \cos\theta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \cr 0 & \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf k_1 &= \sin\theta\,\mathbf j + \cos\theta\,\mathbf k, \qquad \mathbf j' = \cos\theta\,\mathbf j - \sin\theta\,\mathbf k \quad &\text{(rows of the matrix: the inverse is the transpose)} \\
> \boldsymbol\omega_{21} &= \dot\theta\,\mathbf i \quad &\text{(rotation about $\mathbf i$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k = -\sin\theta\,\mathbf j' + \cos\theta\,\mathbf k_1, \qquad \mathbf k_1 = \sin\theta\,\mathbf j + \cos\theta\,\mathbf k, \qquad \boldsymbol\omega_{21} = \dot\theta\,\mathbf i}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\theta$ is the angle between $Gz$ and $O_1z_1$; for zero nutation the axis of revolution is vertical, with the rim up.

![[attachments/EM-SOL/rb15-rot-phi.svg]]

> [!derivation] Spin: rotation by phi about k
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.18; Notes.pdf, Sec. 9.2
>
> View with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right, $\mathbf j$ up; the triangles are those of the precession with $\varphi$ in place of $\psi$.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j \quad &\text{(adjacent legs along $\mathbf i$ and $\mathbf j$; tip of $\mathbf j$ towards minus $\mathbf i$)} \\
> [{}_2R_b] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k$ in $\mathcal B_2$)} \\
> \det[{}_2R_b] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_2R_b][{}_2R_b]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b2} &= \dot\varphi\,\mathbf k \quad &\text{(rotation about $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j, \qquad \boldsymbol\omega_{b2} = \dot\varphi\,\mathbf k}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the spin turns the shell about its own axis of revolution; it changes neither $Gxyz$ nor the position of $G$.

> [!derivation] Part (d): angular velocity of the shell
> **Law:** composition of angular velocities of the three simple rotations
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\varphi\,\mathbf k + \dot\theta\,\mathbf i + \dot\psi\,\mathbf k_1 \quad &\text{(composition, Eq. 9.21)} \\
> &= \dot\theta\,\mathbf i + \dot\psi\left(\sin\theta\,\mathbf j + \cos\theta\,\mathbf k\right) + \dot\varphi\,\mathbf k \quad &\text{($\mathbf k_1$ in $Gxyz$, nutation box)} \\
> &= \dot\theta\,\mathbf i + \dot\psi\sin\theta\,\mathbf j + \left(\dot\psi\cos\theta + \dot\varphi\right)\mathbf k \quad &\text{(collect)} \\
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{b0} - \dot\varphi\,\mathbf k = \dot\theta\,\mathbf i + \dot\psi\sin\theta\,\mathbf j + \dot\psi\cos\theta\,\mathbf k \quad &\text{(angular velocity of $Gxyz$ itself)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \dot\theta\,\mathbf i + \dot\psi\sin\theta\,\mathbf j + \left(\dot\psi\cos\theta + \dot\varphi\right)\mathbf k, \qquad \boldsymbol\omega_{20} = \dot\theta\,\mathbf i + \dot\psi\sin\theta\,\mathbf j + \dot\psi\cos\theta\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** written in $Gxyz$, the components do not depend on the spin angle; the third component, the total spin about the axis of revolution, is called $n$ below.

![[attachments/EM-SOL/rb15-meridian.svg]]

> [!derivation] No penetration: height of G and position of the contact point
> **Law:** the plane is tangent to the sphere at the contact, and the normal of a sphere passes through its centre; position vector as a sum of segments
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.2; Notes.pdf, Eq. 9.3
>
> The lowest point of the sphere of centre $O$ is at the distance $a$ below $O$; it belongs to the shell (the curved side, from the pole to the rim) while the pole direction, minus $\mathbf k$, points downwards, that is while $\theta$ is below a right angle. In the vertical plane of $\mathbf j'$ and $\mathbf k_1$ (meridian section), the segment from $O$ to $G$ has length $a/2$ (part (b)) along minus $\mathbf k$; right triangle with that hypotenuse: the vertical leg $\tfrac a2\cos\theta$ (adjacent to $\theta$) points down and the horizontal leg $\tfrac a2\sin\theta$ (opposite) points along $\mathbf j'$.
>
> $$\begin{aligned}
> \mathbf r_O^P &= -a\,\mathbf k_1 \quad &\text{(contact straight below the centre, at distance $a$)} \\
> z_O &= a \quad &\text{(the contact point is on the plane $z_1 = 0$)} \\
> \mathbf r_O^G &= -\frac a2\,\mathbf k = \frac a2\sin\theta\,\mathbf j' - \frac a2\cos\theta\,\mathbf k_1 \quad &\text{(part (b); $\mathbf k$ of the nutation box)} \\
> z_G &= a - \frac a2\cos\theta \quad &\text{(vertical leg below $O$)} \\
> \mathbf r_0^G &= \xi\,\mathbf i_1 + \eta\,\mathbf j_1 + \left(a - \frac a2\cos\theta\right)\mathbf k_1 \quad &\text{(definition of $\xi$ and $\eta$)} \\
> \mathbf r_G^P &= \mathbf r_G^O + \mathbf r_O^P = \frac a2\,\mathbf k - a\,\mathbf k_1 \quad &\text{(sum of segments)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \xi\,\mathbf i_1 + \eta\,\mathbf j_1 + \left(a - \frac a2\cos\theta\right)\mathbf k_1, \qquad \mathbf r_G^P = \frac a2\,\mathbf k - a\,\mathbf k_1}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** the height of $G$ depends only on the nutation: it is lowest, $a/2$, with the axis vertical and rises as the shell tilts.

> [!derivation] Velocity of G and check of the no-penetration condition
> **Law:** chain rule; velocity field of the rigid body; scalar triple product
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \mathbf v_0^G &= \dot\xi\,\mathbf i_1 + \dot\eta\,\mathbf j_1 + \frac a2\sin\theta\,\dot\theta\,\mathbf k_1 \quad &\text{(derivative of the position; chain rule on the cosine)} \\
> \mathbf v_0^{P(b)}\cdot\mathbf k_1 &= \mathbf v_0^G\cdot\mathbf k_1 + \left(\boldsymbol\omega_{b0}\times\frac a2\,\mathbf k\right)\cdot\mathbf k_1 - a\left(\boldsymbol\omega_{b0}\times\mathbf k_1\right)\cdot\mathbf k_1 \quad &\text{(velocity field from $G$ to $P$, vertical component)} \\
> \left(\boldsymbol\omega_{b0}\times\mathbf k_1\right)\cdot\mathbf k_1 &= 0 \quad &\text{(a vector product is normal to its factors)} \\
> \left(\boldsymbol\omega_{b0}\times\mathbf k\right)\cdot\mathbf k_1 &= \boldsymbol\omega_{b0}\cdot\left(\mathbf k\times\mathbf k_1\right) = \boldsymbol\omega_{b0}\cdot\left(\sin\theta\,\mathbf k\times\mathbf j\right) = -\sin\theta\,\dot\theta \quad &\text{(cyclic triple product; $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \mathbf v_0^{P(b)}\cdot\mathbf k_1 &= \frac a2\sin\theta\,\dot\theta - \frac a2\sin\theta\,\dot\theta = 0 \quad &\text{(add)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \dot\xi\,\mathbf i_1 + \dot\eta\,\mathbf j_1 + \frac a2\sin\theta\,\dot\theta\,\mathbf k_1, \qquad \mathbf v_0^{P(b)}\cdot\mathbf k_1 = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the body point at the contact has no vertical velocity (Eq. 13.1); it may slide horizontally, since the plane is smooth.

### Center of Mass and Inertia Tensor

![[attachments/EM-SOL/rb15-shell-element.svg]]

> [!derivation] Part (a): inertia tensor about O
> **Law:** moments and products of inertia as integrals over the surface (jacobian $a^2\sin\beta$); relation between the moments about the axes and about the point
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Eq. 10.5; [Lecture 8, Slide 21]
>
> Spherical coordinates about $O$ in body axes: a point of the shell is $a(\sin\beta\cos\alpha\,\mathbf i_b + \sin\beta\sin\alpha\,\mathbf j_b - \cos\beta\,\mathbf k)$, with $\beta$ from 0 (the pole, at $-a\,\mathbf k$) to $\pi/2$ (the rim) and $\alpha$ from 0 to $2\pi$. Area element $a^2\sin\beta\,d\beta\,d\alpha$, surface density $\sigma$.
>
> $$\begin{aligned}
> A &= \int_0^{2\pi}\int_0^{\pi/2}a^2\sin\beta\,d\beta\,d\alpha = 2\pi a^2\left[-\cos\beta\right]_0^{\pi/2} = 2\pi a^2\left(0 + 1\right) \quad &\text{(area; Barrow)} \\
> \sigma &= \frac{m}{2\pi a^2}, \qquad dm = \sigma a^2\sin\beta\,d\beta\,d\alpha \quad &\text{(mass over area)} \\
> I_{Oz} &= \int\left(x^2 + y^2\right)dm = \sigma a^4\int_0^{2\pi}d\alpha\int_0^{\pi/2}\sin^3\beta\,d\beta \quad &\text{($x^2 + y^2 = a^2\sin^2\beta$)} \\
> \int_0^{\pi/2}\sin^3\beta\,d\beta &= \int_0^{\pi/2}\left(1 - \cos^2\beta\right)\sin\beta\,d\beta = \int_0^{1}\left(1 - u^2\right)du \quad &\text{($u = \cos\beta$, $du = -\sin\beta\,d\beta$, limits 1 to 0 reversed)} \\
> &= \left[u - \frac{u^3}{3}\right]_0^1 = \frac23 \quad &\text{(antiderivative; Barrow)} \\
> I_{Oz} &= \sigma a^4\cdot 2\pi\cdot\frac23 = \frac{m}{2\pi a^2}\cdot\frac{4\pi a^4}{3} = \frac23\,m a^2 \quad &\text{(value of $\sigma$)} \\
> I_{Ox} + I_{Oy} + I_{Oz} &= 2\int\left(x^2 + y^2 + z^2\right)dm = 2\int a^2\,dm = 2ma^2 \quad &\text{(Eq. 10.13; every point is at distance $a$ from $O$)} \\
> \int_0^{2\pi}\cos^2\alpha\,d\alpha &= \left[\frac\alpha2 + \frac{\sin2\alpha}{4}\right]_0^{2\pi} = \pi - 0 = \pi \quad &\text{(half-angle identity, antiderivative, Barrow's rule)} \\
> \int_0^{2\pi}\sin^2\alpha\,d\alpha &= \left[\frac\alpha2 - \frac{\sin2\alpha}{4}\right]_0^{2\pi} = \pi - 0 = \pi \quad &\text{(same steps, opposite sign of the second term)} \\
> \int x^2\,dm &= \sigma a^4\int_0^{\pi/2}\sin^3\beta\,d\beta\int_0^{2\pi}\cos^2\alpha\,d\alpha = \int y^2\,dm \quad &\text{(the two angular integrals are both $\pi$)} \\
> I_{Ox} &= I_{Oy} = \frac12\left(2ma^2 - \frac23\,ma^2\right) = \frac23\,ma^2 \quad &\text{(equal moments; subtract the axial one)} \\
> P_{xy},\ P_{xz},\ P_{yz} &\propto \int_0^{2\pi}\cos\alpha\sin\alpha\,d\alpha,\ \int_0^{2\pi}\cos\alpha\,d\alpha,\ \int_0^{2\pi}\sin\alpha\,d\alpha = 0,\ 0,\ 0 \quad &\text{(antiderivatives $\tfrac12\sin^2\alpha$, $\sin\alpha$, $-\cos\alpha$; Barrow over a full turn)} \\
> [R]\left(\tfrac23 ma^2[U]\right)[R]^T &= \tfrac23 ma^2\,[R][R]^T = \tfrac23 ma^2\,[U] \quad &\text{(change of basis by any rotation, Eq. 10.41)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_O = \frac23\,m a^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in axes parallel to } Gxyz \text{ (and in any other axes through } O\text{)}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the result agrees with the symmetry argument suggested by the statement: a full shell of mass $2m$ has $\tfrac23(2m)a^2$ about any diameter, and a reflection in the plane of the rim maps each half onto the other without changing the distance of any point to a diameter in that plane or to the axis, so each half carries half of it.

> [!derivation] Part (b): centre of mass
> **Law:** definition of the centre of mass; first symmetry theorem
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 21]
>
> $$\begin{aligned}
> x_G &= y_G = 0 \quad &\text{(the axis of revolution is an axis of symmetry)} \\
> m\,z_G &= \int z\,dm = \int_0^{2\pi}\int_0^{\pi/2}\left(-a\cos\beta\right)\sigma a^2\sin\beta\,d\beta\,d\alpha \quad &\text{(Eq. 10.8, $z$ from $O$ along $\mathbf k$)} \\
> \int_0^{\pi/2}\cos\beta\sin\beta\,d\beta &= \int_0^1 u\,du = \left[\frac{u^2}{2}\right]_0^1 = \frac12 \quad &\text{($u = \sin\beta$, $du = \cos\beta\,d\beta$; Barrow)} \\
> m\,z_G &= -\sigma a^3\cdot 2\pi\cdot\frac12 = -\frac{m}{2\pi a^2}\,\pi a^3 = -\frac{ma}{2} \quad &\text{(value of $\sigma$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_O^G = -\frac a2\,\mathbf k}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** $G$ lies on the axis of revolution, halfway between the centre $O$ and the pole; the axis $Gz$ therefore points from $G$ towards $O$ and the rim, as the statement says.

> [!derivation] Part (c): inertia tensor about G
> **Law:** parallel axis theorem component by component; invariance of an axisymmetric tensor under rotations about its axis
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Eq. 10.41; Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 15]
>
> The position of $G$ relative to $O$ is $(0, 0, -a/2)$ in axes parallel to $Gxyz$.
>
> $$\begin{aligned}
> I_{Gx} &= I_{Ox} - m\left(y_G^2 + z_G^2\right) = \frac23\,ma^2 - m\,\frac{a^2}{4} = \frac{5}{12}\,ma^2 \quad &\text{(Steiner; $\tfrac23 - \tfrac14 = \tfrac{8 - 3}{12}$)} \\
> I_{Gy} &= I_{Oy} - m\left(x_G^2 + z_G^2\right) = \frac{5}{12}\,ma^2 \quad &\text{(same distance)} \\
> I_{Gz} &= I_{Oz} - m\left(x_G^2 + y_G^2\right) = \frac23\,ma^2 \quad &\text{(the axis already passes through $G$)} \\
> P_{G,xz} &= P_{O,xz} - m\,x_G z_G = 0, \quad P_{G,yz} = P_{O,yz} - m\,y_G z_G = 0, \quad P_{G,xy} = P_{O,xy} - m\,x_G y_G = 0 \quad &\text{(Steiner for products; $x_G$, $y_G$ zero)} \\
> [{}_2R_b]\begin{bmatrix} A & 0 & 0 \cr 0 & A & 0 \cr 0 & 0 & C \end{bmatrix}[{}_2R_b]^T &= \begin{bmatrix} A(\cos^2\varphi + \sin^2\varphi) & 0 & 0 \cr 0 & A(\sin^2\varphi + \cos^2\varphi) & 0 \cr 0 & 0 & C \end{bmatrix} \quad &\text{(body axes to $Gxyz$, Eq. 10.41; the off-diagonal terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \begin{bmatrix} A & 0 & 0 \cr 0 & A & 0 \cr 0 & 0 & C \end{bmatrix}_{Gxyz}, \qquad A = \frac{5}{12}\,ma^2, \qquad C = \frac23\,ma^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the shell is axisymmetric, so the tensor has the same constant components in the body axes and in $Gxyz$, although $Gxyz$ does not spin with the body; this is what makes $Gxyz$ convenient.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (e): momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]; [Lecture 9, Slide 10]
>
> Write $n$ for the third component of the angular velocity, the rate of $\psi$ times the cosine of $\theta$ plus the rate of $\varphi$.
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = m\left(\dot\xi\,\mathbf i_1 + \dot\eta\,\mathbf j_1 + \frac a2\sin\theta\,\dot\theta\,\mathbf k_1\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \begin{bmatrix} A & 0 & 0 \cr 0 & A & 0 \cr 0 & 0 & C \end{bmatrix}\begin{bmatrix} \dot\theta \cr \dot\psi\sin\theta \cr n \end{bmatrix} = A\dot\theta\,\mathbf i + A\dot\psi\sin\theta\,\mathbf j + C\,n\,\mathbf k \quad &\text{(Eq. 11.12; row by column)} \\
> \left(v_0^G\right)^2 &= \dot\xi^2 + \dot\eta^2 + \frac{a^2}{4}\sin^2\theta\,\dot\theta^2 \quad &\text{(squared components)} \\
> T_0 &= \frac12\,m\left(v_0^G\right)^2 + \frac12\left(A\dot\theta^2 + A\dot\psi^2\sin^2\theta + C\,n^2\right) \quad &\text{(Eq. 11.31; diagonal tensor)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \frac m2\left(\dot\xi^2 + \dot\eta^2 + \frac{a^2}{4}\sin^2\theta\,\dot\theta^2\right) + \frac{5ma^2}{24}\left(\dot\theta^2 + \dot\psi^2\sin^2\theta\right) + \frac{ma^2}{3}\left(\dot\psi\cos\theta + \dot\varphi\right)^2}$$
>
> **Units:** J in every term
> **Meaning:** the energy depends on the angles only through $\theta$; neither $\psi$, nor $\varphi$, nor $\xi$, $\eta$ appear, which announces the first integrals below.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb15-fbd.svg]]

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf k_1$ | applied, conservative |
| Normal reaction | $P$ | $N\,\mathbf k_1$ (smooth plane: no tangential part) | constraint |

> [!derivation] Part (f): linear momentum equation and its integration
> **Law:** Newton's second law for the centre of mass; Barrow's rule twice
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 11.3; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= \left(N - mg\right)\mathbf k_1 \quad &\text{(Eq. 12.8; both forces are vertical)} \\
> m\,\ddot\xi &= 0, \qquad m\,\ddot\eta = 0 \quad &\text{(components along $\mathbf i_1$ and $\mathbf j_1$)} \\
> \dot\xi(t) - \dot\xi(0) &= \int_0^t\ddot\xi\,dt' = 0, \qquad \xi(t) - \xi(0) = \int_0^t\dot\xi(0)\,dt' = \dot\xi(0)\,t \quad &\text{(Barrow twice; same for $\eta$)} \\
> m\,\ddot z_G &= N - mg, \qquad \ddot z_G = \frac a2\left(\cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta\right) \quad &\text{(vertical component; product rule on $\tfrac a2\sin\theta\,\dot\theta$)}
> \end{aligned}$$
>
> $$\boxed{\xi = \xi_0 + \dot\xi_0\,t, \qquad \eta = \eta_0 + \dot\eta_0\,t, \qquad N = m\left(g + \frac a2\left(\cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta\right)\right)}$$
>
> **Units:** m; N
> **Meaning:** first integral (a): the projection of $G$ on the plane moves in a straight line at constant speed, because a smooth plane exerts no horizontal force.

> [!derivation] Part (g): angular momentum equation about G and the integral about Gz
> **Law:** moment equation about the centre of mass; Coriolis theorem between $S_0$ and $Gxyz$; vector products by determinants
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 12.23
>
> In $Gxyz$, the arm from $G$ to $P$ is $\tfrac a2\,\mathbf k - a(\sin\theta\,\mathbf j + \cos\theta\,\mathbf k)$ and the reaction is $N(\sin\theta\,\mathbf j + \cos\theta\,\mathbf k)$. The derivative of the angular momentum is taken in $Gxyz$, whose components of the tensor are constant, plus the angular velocity of that frame crossed with the angular momentum.
>
> $$\begin{aligned}
> \mathbf M_G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 0 & -a\sin\theta & a\left(\tfrac12 - \cos\theta\right) \cr 0 & N\sin\theta & N\cos\theta \end{vmatrix} \quad &\text{(moment of the reaction; the weight acts at $G$)} \\
> &= \mathbf i\left(-aN\sin\theta\cos\theta - a\left(\tfrac12 - \cos\theta\right)N\sin\theta\right) - \mathbf j\,(0 - 0) + \mathbf k\,(0 - 0) \quad &\text{(expand along the first row)} \\
> &= -\frac a2\,N\sin\theta\,\mathbf i \quad &\text{(the terms in $\sin\theta\cos\theta$ cancel)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= \left.\frac{d\mathbf H_{G,0}}{dt}\right|_2 + \boldsymbol\omega_{20}\times\mathbf H_{G,0} \quad &\text{(Coriolis theorem, Eq. 3.8)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_2 &= A\ddot\theta\,\mathbf i + A\left(\ddot\psi\sin\theta + \dot\psi\cos\theta\,\dot\theta\right)\mathbf j + C\,\dot n\,\mathbf k \quad &\text{(derivative of the components; product and chain rules)} \\
> \boldsymbol\omega_{20}\times\mathbf H_{G,0} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \dot\theta & \dot\psi\sin\theta & \dot\psi\cos\theta \cr A\dot\theta & A\dot\psi\sin\theta & C\,n \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\left(C\,n\,\dot\psi\sin\theta - A\dot\psi^2\sin\theta\cos\theta\right) - \mathbf j\left(C\,n\,\dot\theta - A\dot\psi\cos\theta\,\dot\theta\right) + \mathbf k\left(A\dot\theta\dot\psi\sin\theta - A\dot\psi\sin\theta\,\dot\theta\right) \quad &\text{(expand along the first row)} \\
> A\ddot\theta + C\,n\,\dot\psi\sin\theta - A\dot\psi^2\sin\theta\cos\theta &= -\frac a2\,N\sin\theta \quad &\text{(component along $\mathbf i$, Eq. 12.14)} \\
> A\left(\ddot\psi\sin\theta + 2\dot\psi\dot\theta\cos\theta\right) - C\,n\,\dot\theta &= 0 \quad &\text{(component along $\mathbf j$)} \\
> C\,\dot n &= 0 \quad &\text{(component along $\mathbf k$: the bracket is zero)} \\
> n(t) - n(0) &= \int_0^t\dot n\,dt' = 0 \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{n = \dot\psi\cos\theta + \dot\varphi = n_0 \ \text{(constant)}, \qquad \mathbf H_{G,0}\cdot\mathbf k = \frac23\,ma^2\,n_0}$$
>
> **Units:** N m for the moment equation; $[\mathrm{T^{-1}}]$ for $n$
> **Meaning:** first integral (b): the reaction is vertical through the contact point, so its line passes through the centre $O$, which lies on the axis of revolution; a force whose line meets an axis has no moment about it. Because the axis $Gz$ itself turns, that alone is not enough: the gyroscopic term along it also vanishes, since the two transverse moments of inertia are equal (axial symmetry), and so the total spin about that axis is conserved.

> [!derivation] Part (h): integral of the angular momentum about the vertical through G
> **Law:** moment equation about $G$ projected on a fixed direction
> **Source:** Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\mathbf H_{G,0}\cdot\mathbf k_1\right) &= \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0\cdot\mathbf k_1 + \mathbf H_{G,0}\cdot\left.\frac{d\mathbf k_1}{dt}\right|_0 \quad &\text{(product rule for the scalar product)} \\
> &= \mathbf M_G\cdot\mathbf k_1 + 0 = -\frac a2\,N\sin\theta\,\mathbf i\cdot\mathbf k_1 = 0 \quad &\text{($\mathbf k_1$ fixed; $\mathbf i$ is horizontal)} \\
> \mathbf H_{G,0}\cdot\mathbf k_1 &= \left(A\dot\theta\,\mathbf i + A\dot\psi\sin\theta\,\mathbf j + C\,n\,\mathbf k\right)\cdot\left(\sin\theta\,\mathbf j + \cos\theta\,\mathbf k\right) \quad &\text{($\mathbf k_1$ in $Gxyz$)} \\
> &= A\dot\psi\sin^2\theta + C\,n_0\cos\theta \quad &\text{(scalar product in an orthonormal basis)}
> \end{aligned}$$
>
> $$\boxed{\frac{5}{12}\,ma^2\,\dot\psi\sin^2\theta + \frac23\,ma^2\,n_0\cos\theta = K \ \text{(constant)}}$$
>
> **Units:** kg m$^2$/s
> **Meaning:** first integral (c): the reaction is vertical and the weight acts at $G$, so neither has a moment about the vertical through $G$. Multiplying the $\mathbf j$ equation of the previous box by $\sin\theta$ gives exactly the time derivative of this expression, a consistency check between the two boxes.

> [!derivation] Part (i): energy integral
> **Law:** power of the reaction at the contact body point; conservation of the mechanical energy
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; [Lecture 10, Slide 18]
>
> $$\begin{aligned}
> \dot W_P &= N\,\mathbf k_1\cdot\mathbf v_0^{P(b)} = 0 \quad &\text{(the contact body point has no vertical velocity: kinematics section)} \\
> T_0 + m\,g\,z_G &= E \quad &\text{(Eq. 12.33 with the potential of the weight, Eq. 12.34)} \\
> \frac m2\left(\dot\xi^2 + \dot\eta^2\right) &= \frac m2\left(\dot\xi_0^2 + \dot\eta_0^2\right), \qquad \frac{ma^2}{3}\,n^2 = \frac{ma^2}{3}\,n_0^2 \quad &\text{(constants by the integrals (a) and (b))} \\
> \frac m2\left(\frac{5a^2}{12} + \frac{a^2}{4}\sin^2\theta\right)\dot\theta^2 + \frac{5ma^2}{24}\,\dot\psi^2\sin^2\theta - \frac{mga}{2}\cos\theta &= E' \quad &\text{(subtract the constants and $mga$; $E'$ a new constant)} \\
> \dot\psi &= \frac{K - C\,n_0\cos\theta}{A\sin^2\theta} \quad &\text{(integral (c) solved for the precession rate)}
> \end{aligned}$$
>
> $$\boxed{\frac12\left(\frac{5}{12} + \frac14\sin^2\theta\right)a^2\dot\theta^2 + \frac{5a^2}{24}\,\dot\psi^2\sin^2\theta - \frac{ga}{2}\cos\theta = \frac{E'}{m}}$$
>
> **Units:** $[\mathrm{L^2\,T^{-2}}]$ in every term
> **Meaning:** first integral (d). With the precession rate replaced from integral (c), it is an equation in $\theta$ and its rate alone, so the nutation is reduced to a quadrature; $\psi$ then follows from (c), $\varphi$ from (b) and $\xi$, $\eta$ from (a).

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Inertia tensor about $O$, axes parallel to $Gxyz$ | $\tfrac23 ma^2\,[U]$ (isotropic) |
| (b) Centre of mass | on the axis, $\mathbf r_O^G = -\tfrac a2\,\mathbf k$ (halfway between $O$ and the pole); height $z_G = a - \tfrac a2\cos\theta$ |
| (c) Inertia tensor at $G$ | $\mathrm{diag}\left(\tfrac{5}{12}ma^2, \tfrac{5}{12}ma^2, \tfrac23 ma^2\right)$ in $Gxyz$ |
| (d) Angular velocity | $\dot\theta\,\mathbf i + \dot\psi\sin\theta\,\mathbf j + (\dot\psi\cos\theta + \dot\varphi)\,\mathbf k$ |
| (e) Kinetic energy | $\tfrac m2\left(\dot\xi^2 + \dot\eta^2 + \tfrac{a^2}{4}\sin^2\theta\,\dot\theta^2\right) + \tfrac{5ma^2}{24}\left(\dot\theta^2 + \dot\psi^2\sin^2\theta\right) + \tfrac{ma^2}{3}(\dot\psi\cos\theta + \dot\varphi)^2$ |
| (f) Linear momentum, integral (a) | $\ddot\xi = \ddot\eta = 0$: $\xi = \xi_0 + \dot\xi_0 t$, $\eta = \eta_0 + \dot\eta_0 t$; $N = m\left(g + \tfrac a2(\cos\theta\,\dot\theta^2 + \sin\theta\,\ddot\theta)\right)$ |
| (g) Integral (b), about $Gz$ | $\dot\psi\cos\theta + \dot\varphi = n_0$ |
| (h) Integral (c), about the vertical through $G$ | $5\dot\psi\sin^2\theta + 8n_0\cos\theta = 12K/(ma^2)$ |
| (i) Energy integral (d) | $\tfrac12\left(\tfrac{5}{12} + \tfrac14\sin^2\theta\right)a^2\dot\theta^2 + \tfrac{5a^2}{24}\dot\psi^2\sin^2\theta - \tfrac{ga}{2}\cos\theta = E'/m$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with limiting cases.

> [!derivation] Check: plane rocking and its small oscillations
> **Law:** the first integrals with no precession and no spin; derivative of the energy integral with the chain rule; first-order expansion
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 5.6
>
> With zero initial precession and spin rates, $n_0$ and $K$ are zero, so integral (c) keeps the precession rate at zero and the shell rocks in a fixed vertical plane.
>
> $$\begin{aligned}
> \frac12\left(\frac{5}{12} + \frac14\sin^2\theta\right)a^2\dot\theta^2 - \frac{ga}{2}\cos\theta &= \frac{E'}{m} \quad &\text{(energy integral with no precession)} \\
> \left(\frac{5}{12} + \frac14\sin^2\theta\right)a^2\dot\theta\ddot\theta + \frac14\sin\theta\cos\theta\,a^2\dot\theta^3 + \frac{ga}{2}\sin\theta\,\dot\theta &= 0 \quad &\text{(product and chain rules)} \\
> \frac{5}{12}\,a\,\ddot\theta + \frac g2\,\theta &= 0 \quad &\text{(divide by $a\dot\theta$; first order in $\theta$)} \\
> \Omega^2 &= \frac{g/2}{5a/12} = \frac{6g}{5a} \quad &\text{(coefficient of the harmonic oscillator)}
> \end{aligned}$$
>
> $$\boxed{\Omega = \sqrt{\frac{6g}{5a}}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]/[\mathrm L] = [\mathrm{T^{-2}}]$
> **Meaning:** on a smooth plane $G$ moves only vertically, and to first order not at all, so the shell rocks about the horizontal axis through $G$ with the moment of inertia $\tfrac{5}{12}ma^2$, restored by the weight with the arm $\tfrac a2\sin\theta$ that separates the contact point from the vertical through $G$.

**Limiting cases and consistency:**

* **Equilibrium.** The axis vertical with the rim up, at rest, is an equilibrium: the normal reaction equals the weight and passes through $G$ and $O$.
* **Spin only.** With the axis vertical and a pure spin, integral (b) keeps the spin constant and integral (c) reduces to the spin itself times $C$; the shell spins in place, as a top on its pole.
* **Full sphere check.** The tensor about $O$ is the one of a full shell with half the mass, as the symmetry argument of the statement predicts.
* **Independent derivation.** The three equations of the moment box and the vertical force equation were also compared symbolically with the equations obtained from the kinetic and potential energies of part (e) with the five parameters; they coincide.
* **Dimensions.** Every term of the energy integral is in m$^2$/s$^2$; the angular momentum integrals are in kg m$^2$/s.

---

## Problem RB-16: Sphere on inclined plane with central attraction

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous solid sphere $b$ of mass $m$, radius $R$ and centre $G$, rolling without slipping on a fixed plane inclined at the angle $\alpha$ to the horizontal. Two applied actions: gravity and an attraction towards the point $O$ of the plane, proportional to the mass and to the distance to $O$. The statement gives no figure; the frames below are chosen here.
* **Interpretation of the attraction:** it is read as a field that pulls every mass element towards $O$ with a force per unit mass equal to $-\kappa$ times its position vector from $O$, with $\kappa$ a positive constant in s$^{-2}$. Its resultant on the sphere is then proportional to $m$ and to the distance from $O$ to $G$, as the statement says, and it is computed in the force section.
* **Horizontal frame:** $S_h\{O; \mathbf I, \mathbf j, \mathbf K\}$, with $\mathbf K$ vertical upwards, $\mathbf j$ horizontal and lying in the inclined plane, and $\mathbf I$ horizontal, pointing towards the side where the plane goes down.
* **Fixed frame of the plane:** $S_0\{O; \mathbf i, \mathbf j, \mathbf k\}$, with $\mathbf i$ along the line of maximum slope pointing downhill, $\mathbf j$ the horizontal line of the plane and $\mathbf k$ the normal to the plane, pointing away from it on the side of the sphere. The plane is at rest, so $S_0$ is inertial.
* **Body frame:** any basis fixed to the sphere; it is never needed explicitly, because the inertia tensor of a sphere is the same in every basis (centre of mass section). The rotation of the sphere is described by the components of its angular velocity in $\mathcal B_0$.
* **Coordinates:** the coordinates $x$, $y$ of $G$ along $\mathbf i$ and $\mathbf j$ (its coordinate along $\mathbf k$ is fixed by the contact) and three angles for the orientation (for instance the Euler angles of the course).
* **Degrees of freedom:** a free rigid body has six coordinates. No penetration of the plane (Notes.pdf, Eq. 13.1) fixes the height of $G$ above the plane and leaves five. Rolling without slipping adds two relations among the velocities (Notes.pdf, Eq. 13.5) that cannot be integrated into relations among the coordinates: five coordinates are still needed to place the sphere, but only three velocities are independent.
* **Unknowns of the dynamics:** $x(t)$, $y(t)$, the three components of the angular velocity, the normal reaction $N$ and the two components of the friction force, $F_x$ and $F_y$. Equations: three force components, three moment components and the two rolling conditions.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the sphere, homogeneous | $m$ | kg |
| Radius | $R$ | m |
| Inclination of the plane | $\alpha$ | rad |
| Constant of the attraction (force per unit mass and unit distance) | $\kappa$ | s$^{-2}$ |
| Gravity | $g$, along $-\mathbf K$ | m/s$^2$ |
| Contact | rolling without slipping (friction as large as needed) | - |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb16-rot-alpha.svg]]

> [!derivation] Basis of the plane: rotation by alpha about j
> **Law:** simple rotation about the second axis, positive by the right-hand rule
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.16; [Lecture 7, Slide 12]
>
> View with $\mathbf j$ pointing into the paper (⊗), $\mathbf I$ to the right and $\mathbf K$ up; this view is right-handed because the product of $\mathbf K$ and $\mathbf I$ is $\mathbf j$. The plane is seen edge-on as a line going down to the right at the angle $\alpha$. Seen from the tip of $\mathbf j$ (from behind the paper), a positive rotation about $\mathbf j$ is counterclockwise; seen from the front, as drawn, it is clockwise, and it carries $\mathbf I$ downwards. Triangle of $\mathbf i$: hypotenuse 1 along the downhill line, adjacent leg along $\mathbf I$ (cosine of $\alpha$), opposite leg along minus $\mathbf K$ (sine of $\alpha$): the downhill direction drops. Triangle of $\mathbf k$: hypotenuse 1 along the normal, adjacent leg along $\mathbf K$ (cosine), opposite leg along $\mathbf I$ (sine): the normal leans towards the downhill side.
>
> $$\begin{aligned}
> \mathbf i &= \cos\alpha\,\mathbf I - \sin\alpha\,\mathbf K, \qquad \mathbf k = \sin\alpha\,\mathbf I + \cos\alpha\,\mathbf K \quad &\text{(legs of the two triangles)} \\
> [{}_hR_0] &= \begin{bmatrix} \cos\alpha & 0 & \sin\alpha \cr 0 & 1 & 0 \cr -\sin\alpha & 0 & \cos\alpha \end{bmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_h$)} \\
> \det[{}_hR_0] &= 1\cdot\left(\cos\alpha\cos\alpha - \sin\alpha\,(-\sin\alpha)\right) = \cos^2\alpha + \sin^2\alpha = 1 \quad &\text{(expand along the second row)} \\
> [{}_hR_0][{}_hR_0]^T &= \begin{bmatrix} \cos^2\alpha + \sin^2\alpha & 0 & -\cos\alpha\sin\alpha + \sin\alpha\cos\alpha \cr 0 & 1 & 0 \cr -\sin\alpha\cos\alpha + \cos\alpha\sin\alpha & 0 & \sin^2\alpha + \cos^2\alpha \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf K &= -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf k \quad &\text{(third row of the matrix: the inverse is the transpose)} \\
> m\,\mathbf g &= -mg\,\mathbf K = mg\sin\alpha\,\mathbf i - mg\cos\alpha\,\mathbf k \quad &\text{(weight in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf K = -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf k, \qquad m\,\mathbf g = mg\sin\alpha\,\mathbf i - mg\cos\alpha\,\mathbf k}$$
>
> **Units:** the matrix is dimensionless; the weight in N
> **Meaning:** the weight splits into a component along the plane, pointing downhill, and a component pressing the sphere against the plane; the basis is constant, so $S_0$ is a fixed frame.

![[attachments/EM-SOL/rb16-plane.svg]]

> [!derivation] Position and velocity of G and rolling without slipping
> **Law:** no penetration and no slip at the contact with a fixed plane; velocity field of the rigid body; vector products by determinants
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 9.3; Notes.pdf, Sec. 13.2
>
> The plane is tangent to the sphere at the contact point $P$, and the normal to a sphere passes through its centre, so $P$ is the foot of the perpendicular from $G$ to the plane, at the distance $R$. Write the angular velocity of the sphere as $\omega_x\,\mathbf i + \omega_y\,\mathbf j + \omega_z\,\mathbf k$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= x\,\mathbf i + y\,\mathbf j + R\,\mathbf k, \qquad \mathbf r_G^P = -R\,\mathbf k \quad &\text{(height $R$ above the plane: no penetration)} \\
> \mathbf v_0^G &= \dot x\,\mathbf i + \dot y\,\mathbf j \quad &\text{(derivative in the fixed basis; $R$ constant)} \\
> \boldsymbol\omega_{b0}\times\mathbf r_G^P &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr 0 & 0 & -R \end{vmatrix} = \mathbf i\left(-R\,\omega_y - 0\right) - \mathbf j\left(-R\,\omega_x - 0\right) + \mathbf k\,(0 - 0) \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{P(b)} &= \mathbf v_0^G + \boldsymbol\omega_{b0}\times\mathbf r_G^P = \left(\dot x - R\,\omega_y\right)\mathbf i + \left(\dot y + R\,\omega_x\right)\mathbf j \quad &\text{(velocity field from $G$, Eq. 9.3)} \\
> \mathbf v_0^{P(b)} &= \mathbf 0 \quad &\text{(rolling without slipping on a plane at rest, Eq. 13.5)} \\
> \omega_x &= -\frac{\dot y}{R}, \qquad \omega_y = \frac{\dot x}{R} \quad &\text{(components along $\mathbf j$ and $\mathbf i$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \dot x\,\mathbf i + \dot y\,\mathbf j, \qquad \boldsymbol\omega_{b0} = -\frac{\dot y}{R}\,\mathbf i + \frac{\dot x}{R}\,\mathbf j + \omega_z\,\mathbf k}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for the velocities; $[\mathrm{T^{-1}}]$ for the angular velocity
> **Meaning:** the two tangential components of the angular velocity are tied to the velocity of the centre; the spin about the normal, $\omega_z$, is left free by the contact. The relations involve rates only: they do not give the orientation as a function of $x$ and $y$.

### Center of Mass and Inertia Tensor

![[attachments/EM-SOL/rb16-sphere-element.svg]]

> [!derivation] Centre of mass and inertia tensor of the solid sphere
> **Law:** mass, centre of mass and moments of inertia as volume integrals in spherical coordinates (jacobian $r^2\sin\chi$); relation between the three axial moments and the polar integral
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 21]
>
> Spherical coordinates about $G$: distance $r$ from 0 to $R$, colatitude $\chi$ from 0 to $\pi$, longitude $\lambda$ from 0 to $2\pi$; a point is $r(\sin\chi\cos\lambda, \sin\chi\sin\lambda, \cos\chi)$ and the volume element is $r^2\sin\chi\,dr\,d\chi\,d\lambda$; the density is $\rho$.
>
> $$\begin{aligned}
> V &= \int_0^{2\pi}d\lambda\int_0^{\pi}\sin\chi\,d\chi\int_0^R r^2\,dr = 2\pi\left[-\cos\chi\right]_0^{\pi}\left[\frac{r^3}{3}\right]_0^R \quad &\text{(separable integral; antiderivatives)} \\
> &= 2\pi\left(-\cos\pi + \cos 0\right)\left(\frac{R^3}{3} - 0\right) = 2\pi\cdot 2\cdot\frac{R^3}{3} = \frac{4\pi R^3}{3} \quad &\text{(Barrow's rule)} \\
> \rho &= \frac{m}{V} = \frac{3m}{4\pi R^3} \quad &\text{(homogeneous sphere)} \\
> \mathbf r_G^G &= \mathbf 0 \quad &\text{(every plane through the centre is a plane of symmetry, Sec. 10.3)} \\
> I_x + I_y + I_z &= 2\int r^2\,dm = 2\rho\int_0^{2\pi}d\lambda\int_0^{\pi}\sin\chi\,d\chi\int_0^R r^4\,dr \quad &\text{(Eq. 10.13; squared distance to the centre)} \\
> &= 2\rho\cdot 2\pi\cdot 2\cdot\left[\frac{r^5}{5}\right]_0^R = \frac{8\pi\rho R^5}{5} \quad &\text{(antiderivative; Barrow's rule)} \\
> &= \frac{8\pi R^5}{5}\cdot\frac{3m}{4\pi R^3} = \frac65\,mR^2 \quad &\text{(value of $\rho$)} \\
> I_x &= I_y = I_z = \frac13\cdot\frac65\,mR^2 = \frac25\,mR^2 \quad &\text{(a rotation that exchanges the axes leaves the sphere unchanged)} \\
> \int_0^{2\pi}\cos\lambda\sin\lambda\,d\lambda &= \left[\frac{\sin^2\lambda}{2}\right]_0^{2\pi} = 0, \quad \int_0^{2\pi}\cos\lambda\,d\lambda = \left[\sin\lambda\right]_0^{2\pi} = 0, \quad \int_0^{2\pi}\sin\lambda\,d\lambda = \left[-\cos\lambda\right]_0^{2\pi} = 0 \quad &\text{(longitude factors of the products of inertia, Eq. 10.15)} \\
> [R]\left(\tfrac25 mR^2[U]\right)[R]^T &= \tfrac25 mR^2\,[R][R]^T = \tfrac25 mR^2\,[U] \quad &\text{(change of basis by any rotation, Eq. 10.41)}
> \end{aligned}$$
>
> $$\boxed{G \ \text{at the geometric centre}, \qquad \bar{\bar I}_G = \frac25\,mR^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in every basis}}$$
>
> **Units:** $\rho$ in kg/m$^3$; moments in $[\mathrm M][\mathrm L^2]$
> **Meaning:** the tensor is isotropic, so the angular momentum about $G$ is parallel to the angular velocity, whatever the orientation of the sphere.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]; [Lecture 9, Slide 10]
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = m\left(\dot x\,\mathbf i + \dot y\,\mathbf j\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \bar{\bar I}_G\cdot\boldsymbol\omega_{b0} = \frac25\,mR^2\left(\omega_x\,\mathbf i + \omega_y\,\mathbf j + \omega_z\,\mathbf k\right) \quad &\text{(Eq. 11.12; isotropic tensor)} \\
> &= \frac25\,mR\left(-\dot y\,\mathbf i + \dot x\,\mathbf j\right) + \frac25\,mR^2\,\omega_z\,\mathbf k \quad &\text{(rolling relations)} \\
> T_0 &= \frac12\,m\left(\dot x^2 + \dot y^2\right) + \frac12\cdot\frac25\,mR^2\left(\frac{\dot y^2}{R^2} + \frac{\dot x^2}{R^2} + \omega_z^2\right) \quad &\text{(Eq. 11.31)} \\
> &= \left(\frac12 + \frac15\right)m\left(\dot x^2 + \dot y^2\right) + \frac15\,mR^2\omega_z^2 \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} = \frac25\,mR^2\,\boldsymbol\omega_{b0}, \qquad T_0 = \frac{7}{10}\,m\left(\dot x^2 + \dot y^2\right) + \frac15\,mR^2\,\omega_z^2}$$
>
> **Units:** kg m/s; kg m$^2$/s; J
> **Meaning:** a rolling sphere carries, on top of the translational energy, two fifths of it as rotational energy about the tangential axes; the spin about the normal adds an independent term.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb16-fbd.svg]]

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $mg\sin\alpha\,\mathbf i - mg\cos\alpha\,\mathbf k$ | applied, conservative |
| Central attraction | $G$ (resultant, next box) | $-m\kappa\,\mathbf r_0^G$ | applied, conservative |
| Normal reaction | $P$ | $N\,\mathbf k$ | constraint |
| Friction | $P$ | $F_x\,\mathbf i + F_y\,\mathbf j$ (unknown: rolling without slip) | constraint |

> [!derivation] Resultant and moment of the central attraction
> **Law:** resultant and moment of a distributed force as integrals over the mass; definition of the centre of mass
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 10.6
>
> A mass element at $\mathbf r_0^G + \boldsymbol\rho$, with $\boldsymbol\rho$ measured from $G$, feels the force $-\kappa\left(\mathbf r_0^G + \boldsymbol\rho\right)dm$.
>
> $$\begin{aligned}
> \mathbf F_\kappa &= -\kappa\int\left(\mathbf r_0^G + \boldsymbol\rho\right)dm = -\kappa\,m\,\mathbf r_0^G - \kappa\int\boldsymbol\rho\,dm \quad &\text{(sum over the mass)} \\
> \int\boldsymbol\rho\,dm &= \mathbf 0 \quad &\text{(first moment about the centre of mass, Eq. 10.6)} \\
> \mathbf M_{G,\kappa} &= \int\boldsymbol\rho\times\left(-\kappa\left(\mathbf r_0^G + \boldsymbol\rho\right)\right)dm = -\kappa\left(\int\boldsymbol\rho\,dm\right)\times\mathbf r_0^G - \kappa\int\boldsymbol\rho\times\boldsymbol\rho\,dm \quad &\text{(distribute the product)} \\
> &= \mathbf 0 - \mathbf 0 \quad &\text{(first moment zero; a vector product of a vector with itself is zero)} \\
> \mathbf F_\kappa &= -m\kappa\left(x\,\mathbf i + y\,\mathbf j + R\,\mathbf k\right) \quad &\text{(position of $G$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_\kappa = -m\kappa\left(x\,\mathbf i + y\,\mathbf j + R\,\mathbf k\right) \ \text{acting at } G, \qquad \mathbf M_{G,\kappa} = \mathbf 0}$$
>
> **Units:** $[\mathrm M][\mathrm{T^{-2}}][\mathrm L]$, N
> **Meaning:** the attraction behaves as a single force applied at $G$, with magnitude proportional to the mass and to the distance from $O$ to $G$, as the statement describes it; it pulls $G$ towards $O$ and, through its normal component, presses the sphere against the plane.

> [!derivation] Force equation
> **Law:** Newton's second law for the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= m\,\mathbf g + \mathbf F_\kappa + N\,\mathbf k + F_x\,\mathbf i + F_y\,\mathbf j \quad &\text{(Eq. 12.8)} \\
> \mathbf a_0^G &= \ddot x\,\mathbf i + \ddot y\,\mathbf j \quad &\text{(derivative of the velocity of $G$ in the fixed basis)} \\
> m\,\ddot x &= mg\sin\alpha - m\kappa x + F_x \quad &\text{(component along $\mathbf i$)} \\
> m\,\ddot y &= -m\kappa y + F_y \quad &\text{(component along $\mathbf j$)} \\
> 0 &= -mg\cos\alpha - m\kappa R + N \quad &\text{(component along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{m\,\ddot x = mg\sin\alpha - m\kappa x + F_x, \qquad m\,\ddot y = -m\kappa y + F_y, \qquad N = m\left(g\cos\alpha + \kappa R\right)}$$
>
> **Units:** N in every term
> **Meaning:** the normal reaction is constant: the normal component of the weight plus the normal component of the attraction, which pulls $G$ towards the plane from the height $R$.

> [!derivation] Moment equation about G
> **Law:** moment equation about the centre of mass; vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; [Lecture 10, Slide 5]
>
> The weight and the attraction act at $G$ with no moment (previous box); only the contact force at $P$ has an arm. The pole $G$ is allowed because the term of Eq. 12.13 in the velocity of the pole vanishes when the pole is the centre of mass.
>
> $$\begin{aligned}
> \mathbf M_G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 0 & 0 & -R \cr F_x & F_y & N \end{vmatrix} = \mathbf i\left(0 + R\,F_y\right) - \mathbf j\left(0 + R\,F_x\right) + \mathbf k\,(0 - 0) \quad &\text{(arm $\mathbf r_G^P$; expand along the first row)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= \frac25\,mR^2\left(\dot\omega_x\,\mathbf i + \dot\omega_y\,\mathbf j + \dot\omega_z\,\mathbf k\right) \quad &\text{(constant tensor coefficient; $\mathcal B_0$ fixed)} \\
> \frac25\,mR^2\,\dot\omega_x &= R\,F_y, \qquad \frac25\,mR^2\,\dot\omega_y = -R\,F_x, \qquad \frac25\,mR^2\,\dot\omega_z = 0 \quad &\text{(components of Eq. 12.13 with the pole at $G$)}
> \end{aligned}$$
>
> $$\boxed{\frac25\,mR\,\dot\omega_x = F_y, \qquad \frac25\,mR\,\dot\omega_y = -F_x, \qquad \omega_z = \omega_{z0} \ \text{(constant)}}$$
>
> **Units:** N m in each moment component
> **Meaning:** friction is the only action that changes the rolling rates; the spin about the normal is conserved because no force has a moment about the normal through $G$ (the friction lies in the plane through $P$, whose line meets that normal), and the fixed axis $\mathbf k$ needs no gyroscopic term.

> [!derivation] Equations of motion of the centre
> **Law:** elimination of friction between the force and moment equations with the rolling relations; chain rule
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.5
>
> $$\begin{aligned}
> \dot\omega_y &= \frac{\ddot x}{R}, \qquad \dot\omega_x = -\frac{\ddot y}{R} \quad &\text{(time derivative of the rolling relations; $R$ constant)} \\
> F_x &= -\frac25\,mR\,\frac{\ddot x}{R} = -\frac25\,m\,\ddot x, \qquad F_y = \frac25\,mR\left(-\frac{\ddot y}{R}\right) = -\frac25\,m\,\ddot y \quad &\text{(moment equations)} \\
> m\,\ddot x + \frac25\,m\,\ddot x &= mg\sin\alpha - m\kappa x \quad &\text{(substitute $F_x$ in the force equation)} \\
> m\,\ddot y + \frac25\,m\,\ddot y &= -m\kappa y \quad &\text{(substitute $F_y$)} \\
> \ddot x + \frac57\,\kappa\,x &= \frac57\,g\sin\alpha, \qquad \ddot y + \frac57\,\kappa\,y = 0 \quad &\text{(divide by $\tfrac75 m$)}
> \end{aligned}$$
>
> $$\boxed{\ddot x + \Omega^2\left(x - x_E\right) = 0, \qquad \ddot y + \Omega^2\,y = 0, \qquad \Omega^2 = \frac{5\kappa}{7}, \qquad x_E = \frac{g\sin\alpha}{\kappa}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ for the squared frequency; $x_E$ in $[\mathrm{L\,T^{-2}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** both coordinates of $G$ perform harmonic oscillations with the same frequency about the point $E$ of the plane at the distance $x_E$ downhill from $O$, where the downhill pull of the weight balances the in-plane part of the attraction. The factor five sevenths comes from the rotational inertia: rolling makes the sphere respond as if its mass were seven fifths of $m$.

> [!derivation] Integration: trajectory of the centre
> **Law:** general solution of the harmonic oscillator, checked by substitution with the chain rule
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.8; Notes.pdf, Eq. 5.9
>
> Initial data: position $x_0$, $y_0$ and velocity components $\dot x_0$, $\dot y_0$.
>
> $$\begin{aligned}
> x - x_E &= C_1\cos\Omega t + C_2\sin\Omega t \quad &\text{(Eq. 5.7 for the variable $x - x_E$)} \\
> \frac{d^2}{dt^2}\left(C_1\cos\Omega t + C_2\sin\Omega t\right) &= -\Omega^2\left(C_1\cos\Omega t + C_2\sin\Omega t\right) \quad &\text{(chain rule twice; it satisfies the equation)} \\
> C_1 &= x_0 - x_E, \qquad C_2 = \frac{\dot x_0}{\Omega} \quad &\text{(Eqs. 5.8 and 5.9 at the initial instant)} \\
> y &= y_0\cos\Omega t + \frac{\dot y_0}{\Omega}\sin\Omega t \quad &\text{(same steps for $y$, centre 0)}
> \end{aligned}$$
>
> $$\boxed{x(t) = x_E + \left(x_0 - x_E\right)\cos\Omega t + \frac{\dot x_0}{\Omega}\sin\Omega t, \qquad y(t) = y_0\cos\Omega t + \frac{\dot y_0}{\Omega}\sin\Omega t, \qquad \Omega = \sqrt{\frac{5\kappa}{7}}}$$
>
> **Units:** $[\mathrm L]$ in every term; $\Omega t$ dimensionless
> **Meaning:** the two coordinates are combinations of the same cosine and sine, so the vector from $E$ to the projection of $G$ is a fixed linear combination of two constant vectors times the cosine and the sine: $G$ describes an ellipse centred above $E$, run through once per period $2\pi/\Omega$, whatever the inclination. The ellipse degenerates into a segment through $E$ when the initial position relative to $E$ and the initial velocity are parallel (for instance, release from rest), and into a circle for suitable launches.

> [!derivation] Angular velocity and reactions along the motion
> **Law:** rolling relations; friction from the moment equations; normal reaction from the force equation
> **Source:** Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 6.6
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= -\frac{\dot y}{R}\,\mathbf i + \frac{\dot x}{R}\,\mathbf j + \omega_{z0}\,\mathbf k \quad &\text{(kinematics section and conserved spin)} \\
> F_x &= -\frac25\,m\,\ddot x = -\frac25\,m\cdot\frac57\left(g\sin\alpha - \kappa x\right) = -\frac27\,m\left(g\sin\alpha - \kappa x\right) \quad &\text{(moment equation; equation of motion)} \\
> F_y &= -\frac25\,m\,\ddot y = -\frac25\,m\left(-\frac57\,\kappa y\right) = \frac27\,m\,\kappa\,y \quad &\text{(same for $y$)} \\
> \left|F_x\,\mathbf i + F_y\,\mathbf j\right| &\le \mu\,N \quad &\text{(Coulomb condition for rolling without slip, with $\mu$ the friction coefficient)}
> \end{aligned}$$
>
> $$\boxed{N = m\left(g\cos\alpha + \kappa R\right), \qquad F_x\,\mathbf i + F_y\,\mathbf j = -\frac27\left[m\left(g\sin\alpha - \kappa x\right)\mathbf i - m\kappa y\,\mathbf j\right]}$$
>
> **Units:** N
> **Meaning:** the friction force is always minus two sevenths of the in-plane resultant of the weight and the attraction (the bracket), so it vanishes when $G$ is above $E$ and is largest at the extremes of the ellipse farthest from $E$. The rolling assumption holds while the magnitude of the bracket times two sevenths stays below the friction coefficient times the constant normal reaction.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Coordinates and degrees of freedom | $x$, $y$ of $G$ plus three angles; no penetration leaves 5 coordinates, rolling leaves 3 independent velocities |
| Equations of motion | $\ddot x + \tfrac57\kappa\,(x - x_E) = 0$, $\ddot y + \tfrac57\kappa\,y = 0$, $\omega_z = \omega_{z0}$, with $x_E = g\sin\alpha/\kappa$ |
| Motion of $G$ | $x = x_E + (x_0 - x_E)\cos\Omega t + (\dot x_0/\Omega)\sin\Omega t$, $y = y_0\cos\Omega t + (\dot y_0/\Omega)\sin\Omega t$, $\Omega = \sqrt{5\kappa/7}$: an ellipse centred at $E$ (period $2\pi\sqrt{7/(5\kappa)}$) |
| Rotation | $\boldsymbol\omega_{b0} = -(\dot y/R)\,\mathbf i + (\dot x/R)\,\mathbf j + \omega_{z0}\,\mathbf k$ |
| Normal reaction | $N = m(g\cos\alpha + \kappa R)$, constant |
| Friction | $-\tfrac27\left[m(g\sin\alpha - \kappa x)\,\mathbf i - m\kappa y\,\mathbf j\right]$; rolling holds while its magnitude does not exceed $\mu N$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: conservation of the mechanical energy
> **Law:** zero power of the contact force at a body point at rest; potential of the weight and of a linear central force; chain rule
> **Source:** Notes.pdf, Eq. 12.31; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 5.2
>
> $$\begin{aligned}
> V_0 &= -mg\sin\alpha\,x + mg\cos\alpha\,R + \frac12\,m\kappa\left(x^2 + y^2 + R^2\right) \quad &\text{(height of $G$ along $\mathbf K$; potential of the attraction, Eq. 5.2 per unit mass)} \\
> \dot W_P &= \left(N\,\mathbf k + F_x\,\mathbf i + F_y\,\mathbf j\right)\cdot\mathbf v_0^{P(b)} = 0 \quad &\text{(the contact body point is at rest)} \\
> \frac{d}{dt}\left(T_0 + V_0\right) &= \frac75\,m\left(\dot x\ddot x + \dot y\ddot y\right) - mg\sin\alpha\,\dot x + m\kappa\left(x\dot x + y\dot y\right) \quad &\text{(chain rule; $\omega_z$ constant)} \\
> &= \frac75\,m\,\dot x\left(\ddot x + \frac57\,\kappa x - \frac57\,g\sin\alpha\right) + \frac75\,m\,\dot y\left(\ddot y + \frac57\,\kappa y\right) = 0 \quad &\text{(factor; the brackets are the equations of motion)}
> \end{aligned}$$
>
> $$\boxed{\frac{7}{10}\,m\left(\dot x^2 + \dot y^2\right) + \frac15\,mR^2\omega_{z0}^2 + V_0 = E_0 \ \text{(constant)}}$$
>
> **Units:** J in every term
> **Meaning:** the equations of motion obtained from the force and moment equations conserve the energy, as they must with no work of the contact force; the same equations were also confirmed symbolically by solving the six Newton-Euler equations together with the rolling relations.

**Limiting cases and consistency:**

* **No attraction.** With the constant of the attraction tending to zero, $x_E$ grows without bound and the equation for $x$ becomes a uniform acceleration of five sevenths of $g\sin\alpha$ down the slope: the classical sphere rolling down an incline.
* **Horizontal plane.** With zero inclination, $E$ coincides with $O$ and the friction balances two sevenths of the attraction alone; the sphere oscillates about $O$.
* **Equilibrium.** At rest with $G$ above $E$, the in-plane forces cancel, the friction is zero and the normal reaction is the normal part of the weight plus that of the attraction.
* **Smooth plane (comparison).** Without friction the factor seven fifths disappears and the frequency would be the square root of the attraction constant; rolling slows the oscillation by the factor square root of five sevenths.
* **Dimensions.** The squared frequency is in s$^{-2}$ like the constant of the attraction; every term of the energy is in J.

---

## Problem RB-18: Bowling ball (Jesús Quintana)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous solid sphere $b$ (the bowling ball, the holes being neglected in the mass distribution) of mass $M$, radius $a$ and centre $G$, moving on the horizontal lane, a plane strip of width $W$ and length $l$ with friction coefficient $\mu$. Gravity acts downwards. The contact with the lane is one point $P$.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, $\mathcal B_0\{\mathbf i, \mathbf j, \mathbf k\}$, the frame $Oxyz$ of the figure: $O$ at the foul line, on the axis of the lane; $\mathbf i$ along the lane towards the pins; $\mathbf k$ vertical upwards; $\mathbf j$ across the lane (to the left of a player looking at the pins, read from the top view of the figure), so that the basis is right-handed. It is inertial.
* **Intermediate frames:** $S_1\{G; \mathbf i_1, \mathbf j_1, \mathbf k\}$, obtained by turning $\mathcal B_0$ by $\psi$ about $\mathbf k$; $S_2\{G; \mathbf i_2, \mathbf j_1, \mathbf k_2\}$, obtained by turning $\mathcal B_1$ by $\theta$ about $\mathbf j_1$; $\mathbf k_2$ points from $G$ to the hole $A$, as the statement says.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k_2\}$, obtained by turning $\mathcal B_2$ by $\varphi$ about $\mathbf k_2$ (Euler angles in the order 3-2-3 of the statement).
* **Coordinates:** $x_G$, $y_G$ (projection of $G$ on the lane) and the three Euler angles $\psi$, $\theta$, $\varphi$. The rates of the coordinates of $G$ are written $\xi$ and $\eta$, as in the official key, and the angular velocity of the ball in $\mathcal B_0$ has components $\omega_x$, $\omega_y$, $\omega_z$.
* **Part (a), rolling with slip:** a free rigid body has six coordinates. No penetration of the lane (Notes.pdf, Eq. 13.1) is one holonomic constraint: the height of $G$ equals $a$. Five degrees of freedom remain, with the five coordinates above. Necessary variables: the five coordinates and the normal reaction $N$; the friction force is not an extra unknown, because with slip Coulomb's law gives it in terms of $N$ and of the slip velocity.
* **Part (b), rolling without slip:** the same holonomic constraint plus the two components of the no-slip condition (Notes.pdf, Eq. 13.5), which relate rates and cannot be integrated: three constraints in total. Three degrees of freedom remain (three independent velocities); the five coordinates are still needed to place the ball. Necessary variables: the five coordinates, $N$ and the two friction components $F_x$, $F_y$, which are now unknown reactions.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the ball, homogeneous sphere | $M$ | kg |
| Radius | $a$ | m |
| Width and length of the lane | $W$, $l$ | m |
| Friction coefficient | $\mu$ | - |
| Gravity | $g$, along $-\mathbf k$ | m/s$^2$ |
| Initial data, part (g) | $G$ above $O$; $\xi_0$ along $\mathbf i$; zero $\eta$; Euler angles zero; rate of $\theta$ equal to $\xi_0/(4a)$, other angle rates zero | m, m/s, rad/s |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb18-rot-psi.svg]]

> [!derivation] First rotation: psi about k
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View from above with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up; a positive $\psi$ turns counterclockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Triangle of $\mathbf j_1$: hypotenuse 1, adjacent leg along $\mathbf j$ (cosine), opposite leg along minus $\mathbf i$ (sine): the counterclockwise turn about the outward axis carries the tip of $\mathbf j$ to the left.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i + \sin\psi\,\mathbf j, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i + \cos\psi\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k \quad &\text{(rotation about the fixed axis $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i + \sin\psi\,\mathbf j, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i + \cos\psi\,\mathbf j, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k}$$
>
> **Units:** dimensionless matrix; $[\mathrm{T^{-1}}]$
> **Meaning:** $\mathbf j_1$ is horizontal; it is the axis of the second rotation.

![[attachments/EM-SOL/rb18-rot-theta.svg]]

> [!derivation] Second rotation: theta about j1
> **Law:** simple rotation about the second axis; right-hand rule
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.17
>
> View with $\mathbf j_1$ pointing into the paper (⊗), $\mathbf i_1$ to the right and $\mathbf k$ up; this view is right-handed because the product of $\mathbf k$ and $\mathbf i_1$ is $\mathbf j_1$. A positive rotation about an axis that points into the paper is clockwise as seen. Triangle of $\mathbf i_2$: hypotenuse 1, adjacent leg along $\mathbf i_1$ (cosine of $\theta$), opposite leg along minus $\mathbf k$ (sine): the tip of $\mathbf i_1$, turned clockwise, drops. Triangle of $\mathbf k_2$: hypotenuse 1, adjacent leg along $\mathbf k$ (cosine), opposite leg along $\mathbf i_1$ (sine): the tip of $\mathbf k$ moves to the right.
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k, \qquad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_1$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 & -\cos\theta\sin\theta + \sin\theta\cos\theta \cr 0 & 1 & 0 \cr -\sin\theta\cos\theta + \cos\theta\sin\theta & 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf k &= -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2 \quad &\text{(third row: the inverse is the transpose)} \\
> \mathbf k_2 &= \sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k \quad &\text{($\mathbf i_1$ of the first rotation)} \\
> \boldsymbol\omega_{21} &= \dot\theta\,\mathbf j_1 \quad &\text{(rotation about $\mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k_2 = \sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k, \qquad \mathbf k = -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2, \qquad \boldsymbol\omega_{21} = \dot\theta\,\mathbf j_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\theta$ is the angle between the vertical and the line $GA$; with $\theta$ zero the hole $A$ is at the top of the ball.

![[attachments/EM-SOL/rb18-rot-phi.svg]]

> [!derivation] Third rotation: phi about k2
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.18; Notes.pdf, Sec. 9.2
>
> View with $\mathbf k_2$ out of the paper (⊙), $\mathbf i_2$ to the right and $\mathbf j_1$ up; the triangles are those of the first rotation with $\varphi$ in place of $\psi$.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\varphi\,\mathbf i_2 + \sin\varphi\,\mathbf j_1, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i_2 + \cos\varphi\,\mathbf j_1 \quad &\text{(adjacent legs along $\mathbf i_2$ and $\mathbf j_1$; tip of $\mathbf j_1$ towards minus $\mathbf i_2$)} \\
> [{}_2R_b] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_2$ in $\mathcal B_2$)} \\
> \det[{}_2R_b] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_2R_b][{}_2R_b]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b2} &= \dot\varphi\,\mathbf k_2 \quad &\text{(rotation about $\mathbf k_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\varphi\,\mathbf i_2 + \sin\varphi\,\mathbf j_1, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i_2 + \cos\varphi\,\mathbf j_1, \qquad \boldsymbol\omega_{b2} = \dot\varphi\,\mathbf k_2}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the spin $\varphi$ turns the ball about the line $GA$; it moves the other holes but not $A$.

> [!derivation] Angular velocity of the ball
> **Law:** composition of the angular velocities of the three simple rotations
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\varphi\,\mathbf k_2 + \dot\theta\,\mathbf j_1 + \dot\psi\,\mathbf k \quad &\text{(composition, Eq. 9.21)} \\
> &= \dot\varphi\left(\sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k\right) + \dot\theta\left(-\sin\psi\,\mathbf i + \cos\psi\,\mathbf j\right) + \dot\psi\,\mathbf k \quad &\text{($\mathbf k_2$ and $\mathbf j_1$ in $\mathcal B_0$)} \\
> \omega_x &= -\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi \quad &\text{(collect along $\mathbf i$)} \\
> \omega_y &= \dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi \quad &\text{(collect along $\mathbf j$)} \\
> \omega_z &= \dot\psi + \dot\varphi\cos\theta \quad &\text{(collect along $\mathbf k$)} \\
> \boldsymbol\omega_{b0} &= -\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_1 + \left(\dot\psi\cos\theta + \dot\varphi\right)\mathbf k_2 \quad &\text{(same vector in $\mathcal B_2$, with $\mathbf k$ of the second rotation)}
> \end{aligned}$$
>
> $$\boxed{\omega_x = -\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi, \qquad \omega_y = \dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi, \qquad \omega_z = \dot\psi + \dot\varphi\cos\theta}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** these three relations are the kinematic equations that link the Euler angles to the angular velocity; the equations of motion below are simplest in the components of $\mathcal B_0$.

> [!derivation] Euler angle rates from the angular velocity
> **Law:** scalar products of the composition with unit vectors of the intermediate bases
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0}\cdot\mathbf j_1 &= \dot\theta \quad &\text{($\mathbf k_2$ and $\mathbf k$ are normal to $\mathbf j_1$)} \\
> \boldsymbol\omega_{b0}\cdot\mathbf j_1 &= -\omega_x\sin\psi + \omega_y\cos\psi \quad &\text{($\mathbf j_1$ in $\mathcal B_0$)} \\
> \boldsymbol\omega_{b0}\cdot\mathbf i_1 &= \dot\varphi\,\mathbf k_2\cdot\mathbf i_1 = \dot\varphi\sin\theta \quad &\text{($\mathbf j_1$ and $\mathbf k$ are normal to $\mathbf i_1$)} \\
> \boldsymbol\omega_{b0}\cdot\mathbf i_1 &= \omega_x\cos\psi + \omega_y\sin\psi \quad &\text{($\mathbf i_1$ in $\mathcal B_0$)} \\
> \dot\psi &= \omega_z - \dot\varphi\cos\theta \quad &\text{(third component of the previous box)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = -\omega_x\sin\psi + \omega_y\cos\psi, \qquad \dot\varphi = \frac{\omega_x\cos\psi + \omega_y\sin\psi}{\sin\theta}, \qquad \dot\psi = \omega_z - \dot\varphi\cos\theta}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** once the angular velocity is known in time, these three first-order equations give the Euler angles; they are singular when the sine of $\theta$ is zero (hole on the vertical through $G$), where $\psi$ and $\varphi$ turn about the same axis.

![[attachments/EM-SOL/rb18-slip.svg]]

> [!derivation] Position and velocity of G and slip velocity of the contact point
> **Law:** no penetration of the lane; velocity field of the rigid body; vector product by its determinant
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 9.3; Notes.pdf, Sec. 13.2
>
> The lane is tangent to the ball at $P$ and the normal of a sphere passes through its centre, so $P$ is straight below $G$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= x_G\,\mathbf i + y_G\,\mathbf j + a\,\mathbf k, \qquad \mathbf r_G^P = -a\,\mathbf k \quad &\text{(height $a$: no penetration)} \\
> \mathbf v_0^G &= \xi\,\mathbf i + \eta\,\mathbf j, \qquad \mathbf a_0^G = \dot\xi\,\mathbf i + \dot\eta\,\mathbf j \quad &\text{(derivatives in the fixed basis; $\xi$, $\eta$ the rates of $x_G$, $y_G$)} \\
> \boldsymbol\omega_{b0}\times\mathbf r_G^P &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr 0 & 0 & -a \end{vmatrix} = \mathbf i\left(-a\,\omega_y\right) - \mathbf j\left(-a\,\omega_x\right) + \mathbf k\,(0) \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{P(b)} &= \mathbf v_0^G + \boldsymbol\omega_{b0}\times\mathbf r_G^P \quad &\text{(velocity field, Eq. 9.3)} \\
> &= \left(\xi - a\,\omega_y\right)\mathbf i + \left(\eta + a\,\omega_x\right)\mathbf j \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_{\mathrm{slip}} = \mathbf v_0^{P(b)} = \left(\xi - a\,\omega_y\right)\mathbf i + \left(\eta + a\,\omega_x\right)\mathbf j, \qquad s = \sqrt{\left(\xi - a\,\omega_y\right)^2 + \left(\eta + a\,\omega_x\right)^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the slip velocity has no vertical component (no penetration holds). Rolling without slip makes both components zero: the two constraints of part (b).

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and inertia tensor of the ball
> **Law:** mass, centre of mass and moments of inertia as volume integrals in spherical coordinates (jacobian $r^2\sin\chi$); relation between the three axial moments and the polar integral
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 21]
>
> Spherical coordinates about $G$: distance $r$ from 0 to $a$, colatitude $\chi$ from 0 to $\pi$, longitude $\lambda$ from 0 to $2\pi$; volume element $r^2\sin\chi\,dr\,d\chi\,d\lambda$; density $\rho$.
>
> $$\begin{aligned}
> V &= \int_0^{2\pi}d\lambda\int_0^{\pi}\sin\chi\,d\chi\int_0^a r^2\,dr = 2\pi\left[-\cos\chi\right]_0^{\pi}\left[\frac{r^3}{3}\right]_0^a \quad &\text{(separable integral; antiderivatives)} \\
> &= 2\pi\left(-\cos\pi + \cos 0\right)\left(\frac{a^3}{3} - 0\right) = \frac{4\pi a^3}{3} \quad &\text{(Barrow's rule)} \\
> \rho &= \frac{3M}{4\pi a^3}, \qquad \mathbf r_G^G = \mathbf 0 \quad &\text{(homogeneous; every plane through the centre is a plane of symmetry)} \\
> I_x + I_y + I_z &= 2\int r^2\,dm = 2\rho\cdot 2\pi\cdot 2\cdot\left[\frac{r^5}{5}\right]_0^a = \frac{8\pi\rho a^5}{5} \quad &\text{(Eq. 10.13; same angular factors; Barrow's rule)} \\
> &= \frac{8\pi a^5}{5}\cdot\frac{3M}{4\pi a^3} = \frac65\,Ma^2 \quad &\text{(value of $\rho$)} \\
> I_x &= I_y = I_z = \frac25\,Ma^2 \quad &\text{(the three axes are equivalent for a sphere)} \\
> \left[\frac{\sin^2\lambda}{2}\right]_0^{2\pi} &= 0, \quad \left[\sin\lambda\right]_0^{2\pi} = 0, \quad \left[-\cos\lambda\right]_0^{2\pi} = 0 \quad &\text{(longitude integrals of $\cos\lambda\sin\lambda$, $\cos\lambda$, $\sin\lambda$: products of inertia zero, Eq. 10.15)} \\
> [R]\left(\tfrac25 Ma^2[U]\right)[R]^T &= \tfrac25 Ma^2\,[U] \quad &\text{(any change of basis, Eq. 10.41)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac25\,Ma^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in every basis}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the tensor is isotropic, so it is the same in $\mathcal B_0$, $\mathcal B_2$ and the body basis: the orientation of the holes does not enter the dynamics of the model.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (c): momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]; [Lecture 9, Slide 10]
>
> $$\begin{aligned}
> \mathbf p_0 &= M\,\mathbf v_0^G = M\left(\xi\,\mathbf i + \eta\,\mathbf j\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \bar{\bar I}_G\cdot\boldsymbol\omega_{b0} = \frac25\,Ma^2\left(\omega_x\,\mathbf i + \omega_y\,\mathbf j + \omega_z\,\mathbf k\right) \quad &\text{(Eq. 11.12; isotropic tensor)} \\
> &= \frac25\,Ma^2\left[\left(-\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi\right)\mathbf i + \left(\dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi\right)\mathbf j + \left(\dot\psi + \dot\varphi\cos\theta\right)\mathbf k\right] \quad &\text{(components of the angular velocity)} \\
> T_0 &= \frac12\,M\left(\xi^2 + \eta^2\right) + \frac15\,Ma^2\left(\dot\psi^2 + \dot\theta^2 + \dot\varphi^2 + 2\dot\psi\dot\varphi\cos\theta\right) \quad &\text{(Eq. 11.31; squared magnitude of the angular velocity in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} = \frac25\,Ma^2\left[\left(-\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi\right)\mathbf i + \left(\dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi\right)\mathbf j + \left(\dot\psi + \dot\varphi\cos\theta\right)\mathbf k\right]}$$
>
> **Units:** kg m$^2$/s; J
> **Meaning:** the angular momentum about $G$ is parallel to the angular velocity. The squared magnitude in $\mathcal B_2$ is the sum of the rate of $\psi$ squared times the sine of $\theta$ squared, the rate of $\theta$ squared and the third component squared; expanding the last square and using the identity of sine and cosine gives the bracket of the kinetic energy.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb18-fbd.svg]]

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-Mg\,\mathbf k$ | applied |
| Normal reaction | $P$ | $N\,\mathbf k$ | constraint |
| Friction, with slip | $P$ | $-\mu N$ times the unit vector of the slip velocity | constraint, known law |
| Friction, without slip | $P$ | $F_x\,\mathbf i + F_y\,\mathbf j$, unknown, with magnitude at most $\mu N$ | constraint |

> [!derivation] Part (d): resultant force and torque about G
> **Law:** resultant of the forces; moment about $G$ by a determinant; Coulomb's law of friction
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 6.6
>
> $$\begin{aligned}
> \mathbf F &= F_x\,\mathbf i + F_y\,\mathbf j + \left(N - Mg\right)\mathbf k \quad &\text{(sum of the three forces)} \\
> \mathbf M_G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 0 & 0 & -a \cr F_x & F_y & N \end{vmatrix} = \mathbf i\left(0 + a\,F_y\right) - \mathbf j\left(0 + a\,F_x\right) + \mathbf k\,(0 - 0) \quad &\text{(arm $\mathbf r_G^P$; the weight acts at $G$)} \\
> F_x\,\mathbf i + F_y\,\mathbf j &= -\mu N\,\frac{\mathbf v_{\mathrm{slip}}}{s} = -\frac{\mu N}{s}\left[\left(\xi - a\,\omega_y\right)\mathbf i + \left(\eta + a\,\omega_x\right)\mathbf j\right] \quad &\text{(with slip: maximum magnitude, opposite to the slip)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = F_x\,\mathbf i + F_y\,\mathbf j + \left(N - Mg\right)\mathbf k, \qquad \mathbf M_G = a\,F_y\,\mathbf i - a\,F_x\,\mathbf j}$$
>
> **Units:** N; N m
> **Meaning:** only the friction has a moment about $G$, and that moment is horizontal: nothing can change the spin about the vertical, $\omega_z$.

> [!derivation] Part (e): equations of motion with slip
> **Law:** Newton's second law for the centre of mass; moment equation about $G$ with the isotropic tensor
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is allowed in Eq. 12.13 because the term in the velocity of the pole vanishes for the centre of mass. The tensor coefficient is constant and $\mathcal B_0$ is fixed, so the derivative of the angular momentum is the tensor coefficient times the derivatives of the three components.
>
> $$\begin{aligned}
> 0 &= N - Mg \quad &\text{(vertical component of Eq. 12.8: $G$ stays at height $a$)} \\
> M\,\dot\xi &= -\frac{\mu Mg}{s}\left(\xi - a\,\omega_y\right), \qquad M\,\dot\eta = -\frac{\mu Mg}{s}\left(\eta + a\,\omega_x\right) \quad &\text{(horizontal components, with $N$ equal to $Mg$)} \\
> \frac25\,Ma^2\,\dot\omega_x &= a\,F_y = a\,M\,\dot\eta \quad &\text{(component along $\mathbf i$ of Eq. 12.13; $F_y$ from the force equation)} \\
> \frac25\,Ma^2\,\dot\omega_y &= -a\,F_x = -a\,M\,\dot\xi \quad &\text{(component along $\mathbf j$)} \\
> \frac25\,Ma^2\,\dot\omega_z &= 0 \quad &\text{(component along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\dot\xi = -\frac{\mu g\left(\xi - a\omega_y\right)}{s}, \quad \dot\eta = -\frac{\mu g\left(\eta + a\omega_x\right)}{s}, \quad 2a\,\dot\omega_x = 5\,\dot\eta, \quad 2a\,\dot\omega_y = -5\,\dot\xi, \quad \dot\omega_z = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in the force equations; $[\mathrm{L\,T^{-2}}]$ after multiplying the angular accelerations by $a$
> **Meaning:** five first-order equations for the five rates, completed by the algebraic relations for $N$ and $s$ and by five kinematic equations: the rates of $x_G$ and $y_G$ equal $\xi$ and $\eta$, and the Euler angle rates follow from the components of the angular velocity (kinematics section). Ten first-order equations in all, for the five degrees of freedom.

> [!derivation] Evolution of the slip velocity
> **Law:** time derivative of the slip velocity with the equations of motion; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.2
>
> Write the slip velocity as the components $u$ along $\mathbf i$ and $w$ along $\mathbf j$.
>
> $$\begin{aligned}
> \dot u &= \dot\xi - a\,\dot\omega_y = \dot\xi + \frac52\,\dot\xi = \frac72\,\dot\xi = -\frac72\,\mu g\,\frac us \quad &\text{(derivative of $\xi - a\omega_y$; previous box)} \\
> \dot w &= \dot\eta + a\,\dot\omega_x = \dot\eta + \frac52\,\dot\eta = \frac72\,\dot\eta = -\frac72\,\mu g\,\frac ws \quad &\text{(derivative of $\eta + a\omega_x$)} \\
> \frac{d}{dt}\left(\frac us\right) &= \frac{\dot u\,s - u\,\dot s}{s^2}, \qquad \dot s = \frac{u\dot u + w\dot w}{s} = -\frac72\,\mu g \quad &\text{(quotient rule; chain rule on the square root)} \\
> \frac{d}{dt}\left(\frac us\right) &= \frac{-\tfrac72\mu g\,u + \tfrac72\mu g\,u}{s^2} = 0 \quad &\text{(substitute)} \\
> s(t) - s(0) &= \int_0^t\dot s\,dt' = -\frac72\,\mu g\,t \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\frac{\mathbf v_{\mathrm{slip}}}{s} \ \text{constant}, \qquad s(t) = s_0 - \frac72\,\mu g\,t, \qquad t^{*} = \frac{2\,s_0}{7\,\mu g}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$; $t^{*}$ in $[\mathrm{L\,T^{-1}}]/[\mathrm{L\,T^{-2}}] = [\mathrm T]$
> **Meaning:** while the ball slips, the friction keeps a fixed direction and the slip speed falls linearly; at the time $t^{*}$ the slip vanishes and the motion continues as rolling without slip (part (f)). The centre of mass therefore has a constant acceleration of magnitude $\mu g$ during the slip: its path is a parabola, or a straight line when the initial velocity of $G$ is parallel to the slip.

> [!derivation] Part (f): rolling without slip reduced to quadratures
> **Law:** no-slip conditions; force and moment equations with unknown friction; Barrow's rule
> **Source:** Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> \xi &= a\,\omega_y, \qquad \eta = -a\,\omega_x \quad &\text{(slip velocity equal to zero, Eq. 13.5)} \\
> M\,\dot\xi &= F_x, \qquad \frac25\,Ma^2\,\dot\omega_y = -a\,F_x \quad &\text{(force along $\mathbf i$; moment along $\mathbf j$)} \\
> \frac25\,Ma^2\,\frac{\dot\xi}{a} &= -a\,M\,\dot\xi \quad &\text{(rate of $\omega_y$ equal to the rate of $\xi$ over $a$; eliminate $F_x$)} \\
> \frac75\,M\,\dot\xi &= 0, \qquad \frac75\,M\,\dot\eta = 0, \qquad \dot\omega_z = 0 \quad &\text{(divide by $a$ and collect; same steps for $\eta$ with the moment along $\mathbf i$)} \\
> F_x &= F_y = 0 \quad &\text{(force equations)} \\
> x_G(t) - x_G(t_1) &= \int_{t_1}^t\xi\,dt' = C_1\left(t - t_1\right), \qquad y_G(t) - y_G(t_1) = C_2\left(t - t_1\right) \quad &\text{(Barrow's rule, from the start $t_1$ of the rolling)}
> \end{aligned}$$
>
> $$\boxed{\xi = a\,\omega_y = C_1, \qquad \eta = -a\,\omega_x = C_2, \qquad \omega_z = C_3, \qquad x_G = x_{G1} + C_1\left(t - t_1\right), \qquad y_G = y_{G1} + C_2\left(t - t_1\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for $C_1$, $C_2$; $[\mathrm{T^{-1}}]$ for $C_3$
> **Meaning:** a sphere rolling without slip on a horizontal plane needs no friction: $G$ moves on a straight line at constant speed. The angular velocity is constant in $S_0$, so the ball turns uniformly about a fixed direction; the Euler angles follow by integrating the three rate equations of the kinematics section with these constant components, and $C_1$, $C_2$, $C_3$ are fixed by the state at the start of the rolling.

#### Part (g): the throw of Jesús Quintana

> [!derivation] Initial angular velocity and slip velocity
> **Law:** components of the angular velocity at the initial instant; slip velocity
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 9.3; Problems.pdf, p. 48
>
> $$\begin{aligned}
> \omega_x(0) &= -\frac{\xi_0}{4a}\sin 0 + 0 = 0 \quad &\text{(rates of $\psi$ and $\varphi$ zero; $\psi$ zero)} \\
> \omega_y(0) &= \frac{\xi_0}{4a}\cos 0 + 0 = \frac{\xi_0}{4a} \quad &\text{(rate of $\theta$ given)} \\
> \omega_z(0) &= 0 + 0 = 0 \quad &\text{(rates of $\psi$ and $\varphi$ zero)} \\
> u(0) &= \xi_0 - a\,\frac{\xi_0}{4a} = \frac34\,\xi_0, \qquad w(0) = 0 + 0 = 0 \quad &\text{(slip velocity components)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0}(0) = \frac{\xi_0}{4a}\,\mathbf j, \qquad \mathbf v_{\mathrm{slip}}(0) = \frac34\,\xi_0\,\mathbf i \ne \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the ball turns forwards only a quarter as fast as rolling would require, so it slides forwards from the very first instant, at the foul line: the friction points backwards, along minus $\mathbf i$.

![[attachments/EM-SOL/rb18-velocities.svg]]

> [!derivation] Motion during the slip
> **Law:** equations of motion with slip; Barrow's rule twice
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.2
>
> The slip is along plus $\mathbf i$ with zero component along $\mathbf j$, and its direction is constant (box on the slip velocity), so the ratio $u/s$ is 1 and $w/s$ is 0 until the slip ends.
>
> $$\begin{aligned}
> \dot\xi &= -\mu g, \qquad \dot\eta = 0, \qquad \dot\omega_x = 0, \qquad \dot\omega_y = \frac{5\mu g}{2a}, \qquad \dot\omega_z = 0 \quad &\text{(part (e) with $u/s$ equal to 1)} \\
> \xi(t) &= \xi_0 - \mu g\,t, \qquad x_G(t) = \int_0^t\left(\xi_0 - \mu g\,t'\right)dt' = \left[\xi_0 t' - \frac{\mu g\,t'^2}{2}\right]_0^t = \xi_0 t - \frac{\mu g\,t^2}{2} \quad &\text{(Barrow's rule twice)} \\
> \omega_y(t) &= \frac{\xi_0}{4a} + \frac{5\mu g}{2a}\,t, \qquad \eta = \omega_x = \omega_z = 0, \qquad y_G = 0 \quad &\text{(Barrow's rule; zero initial values)} \\
> \dot\theta &= \omega_y, \qquad \dot\psi = \dot\varphi = 0 \quad &\text{(Euler rates with $\psi$ and $\varphi$ zero; consistent with zero initial rates)} \\
> \theta(t) &= \int_0^t\left(\frac{\xi_0}{4a} + \frac{5\mu g}{2a}\,t'\right)dt' = \frac{\xi_0}{4a}\,t + \frac{5\mu g}{4a}\,t^2 \quad &\text{(antiderivative; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{x_G = \xi_0 t - \frac12\mu g t^2, \quad y_G = 0, \quad \xi = \xi_0 - \mu g t, \quad \omega_y = \frac{\xi_0}{4a} + \frac{5\mu g}{2a}\,t, \quad \psi = \varphi = 0, \quad \theta = \frac{\xi_0 t}{4a} + \frac{5\mu g\,t^2}{4a}}$$
>
> **Units:** m; m/s; rad/s; rad
> **Meaning:** the ball moves along the axis of the lane; friction slows the centre down and spins the ball up about the horizontal axis $\mathbf j$, so the hole $A$ turns forwards in the vertical plane of the lane.

> [!derivation] Part (g)1: end of the slip
> **Law:** zero slip velocity; previous box
> **Source:** Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> u(t) &= \frac34\,\xi_0 - \frac72\,\mu g\,t \quad &\text{(box on the slip velocity with $s_0$ equal to three quarters of $\xi_0$)} \\
> t^{*} &= \frac{3\xi_0/4}{7\mu g/2} = \frac{3\,\xi_0}{14\,\mu g} \quad &\text{(set $u$ to zero)} \\
> x^{*} &= \xi_0\,\frac{3\xi_0}{14\mu g} - \frac{\mu g}{2}\,\frac{9\xi_0^2}{196\,\mu^2g^2} = \frac{84\,\xi_0^2 - 9\,\xi_0^2}{392\,\mu g} = \frac{75\,\xi_0^2}{392\,\mu g} \quad &\text{(position of the previous box at $t^{*}$; common denominator 392)} \\
> \xi^{*} &= \xi_0 - \mu g\,\frac{3\xi_0}{14\mu g} = \frac{11}{14}\,\xi_0 \quad &\text{(velocity at $t^{*}$)}
> \end{aligned}$$
>
> $$\boxed{\text{slip from } t = 0 \text{ at } x_G = 0 \text{ until } t^{*} = \frac{3\xi_0}{14\mu g}, \ x^{*} = \frac{75\,\xi_0^2}{392\,\mu g}; \ \text{then rolling with } \xi = \frac{11}{14}\,\xi_0 = a\,\omega_y}$$
>
> **Units:** $t^{*}$ in s; $x^{*}$ in $[\mathrm{L^2\,T^{-2}}]/[\mathrm{L\,T^{-2}}] = [\mathrm L]$
> **Meaning:** read literally, the ball slips from the moment it is released, at the foul line. The transition the question is aiming at is the end of the slip: after the time $t^{*}$, about 0.214 times the ratio of the initial speed to the product of the friction coefficient and $g$, the ball would roll without slip at eleven fourteenths of its initial speed, if the lane were long enough.

> [!derivation] Part (g)2: arrival at the pins for the given length
> **Law:** position during the slip; roots of a quadratic equation
> **Source:** Notes.pdf, Eq. 12.8; Problems.pdf, p. 48
>
> $$\begin{aligned}
> l &= \frac{\xi_0^2}{10\,\mu g} \lt x^{*} = \frac{75\,\xi_0^2}{392\,\mu g} \quad &\text{(39.2 is smaller than 75 in units of $\xi_0^2/(392\mu g)$)} \\
> \xi_0 t_l - \frac{\mu g}{2}\,t_l^2 &= \frac{\xi_0^2}{10\,\mu g} \quad &\text{(the ball is still slipping at the pins)} \\
> \tau^2 - 2\tau + \frac15 &= 0, \qquad \tau = \frac{\mu g\,t_l}{\xi_0} \quad &\text{(multiply by $2\mu g/\xi_0^2$)} \\
> \tau &= 1 - \sqrt{1 - \frac15} = 1 - \frac{2}{\sqrt5} \quad &\text{(first arrival: smaller root)} \\
> \xi(t_l) &= \xi_0\left(1 - \tau\right) = \frac{2\,\xi_0}{\sqrt5} \quad &\text{(velocity during the slip)} \\
> \omega_y(t_l) &= \frac{\xi_0}{4a} + \frac{5}{2a}\,\xi_0\,\tau = \frac{\xi_0}{a}\left(\frac14 + \frac52 - \sqrt5\right) = \frac{\xi_0}{a}\left(\frac{11}{4} - \sqrt5\right) \quad &\text{(angular velocity during the slip; $\tfrac52\cdot\tfrac{2}{\sqrt5} = \sqrt5$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \frac{2\,\xi_0}{\sqrt5}\,\mathbf i, \qquad \boldsymbol\omega_{b0} = \frac{\xi_0}{a}\left(\frac{11}{4} - \sqrt5\right)\mathbf j, \qquad t_l = \left(1 - \frac{2}{\sqrt5}\right)\frac{\xi_0}{\mu g}}$$
>
> **Units:** m/s; rad/s; s
> **Meaning:** the ball reaches the pins at about 0.894 of its initial speed and is still slipping there: $a$ times its angular velocity is about 0.514 of the initial speed, below the speed of $G$, and the slip ($u$ about 0.380 of the initial speed) has not run out.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) With slip | 1 constraint (height of $G$); 5 degrees of freedom; variables $x_G$, $y_G$, $\psi$, $\theta$, $\varphi$ and $N$ |
| (b) Without slip | 3 constraints (height of $G$ and two non-integrable no-slip conditions); 3 degrees of freedom; variables $x_G$, $y_G$, $\psi$, $\theta$, $\varphi$, $N$, $F_x$, $F_y$ |
| (c) Angular momentum about $G$ | $\tfrac25 Ma^2\left[(-\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi)\,\mathbf i + (\dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi)\,\mathbf j + (\dot\psi + \dot\varphi\cos\theta)\,\mathbf k\right]$ |
| (d) Force and torque | $\mathbf F = F_x\mathbf i + F_y\mathbf j + (N - Mg)\mathbf k$, $\mathbf M_G = aF_y\,\mathbf i - aF_x\,\mathbf j$; with slip $F_x\mathbf i + F_y\mathbf j = -\mu N\,\mathbf v_{\mathrm{slip}}/s$ |
| (e) Equations with slip | $\dot\xi = -\mu g(\xi - a\omega_y)/s$, $\dot\eta = -\mu g(\eta + a\omega_x)/s$, $2a\dot\omega_x = 5\dot\eta$, $2a\dot\omega_y = -5\dot\xi$, $\dot\omega_z = 0$, $N = Mg$, plus the five kinematic equations |
| (f) Without slip | $\xi = a\omega_y = C_1$, $\eta = -a\omega_x = C_2$, $\omega_z = C_3$; $G$ moves on a straight line at constant speed |
| (g)1 | slip from the release, $t = 0$ at $x_G = 0$; the slip would end at $t^{*} = 3\xi_0/(14\mu g)$, $x^{*} = 75\xi_0^2/(392\mu g)$ |
| (g)2 | with $l = \xi_0^2/(10\mu g)$ the ball is still slipping: $\mathbf v_0^G = (2\xi_0/\sqrt5)\,\mathbf i$, $\boldsymbol\omega_{b0} = (\xi_0/a)(11/4 - \sqrt5)\,\mathbf j$ |

**Check against the official key:** the key (Problems.pdf, p. 79) prints 5 degrees of freedom with slip and 3 without, the equations of motion with slip in exactly the form of part (e), with the same symbols, the quadratures of part (f) and, at the pins, the velocity $2\xi_0/\sqrt5$ along $\mathbf i$ and the angular velocity $(\xi_0/a)(11/4 - \sqrt5)$ along $\mathbf j$. Match on every printed item. The key prints no time or position for question (g)1; the interpretation used here (slip from the release, end of the slip at $t^{*}$) is stated in its box.

**Limiting cases and consistency:**

* **Launch already rolling.** If the initial rate of $\theta$ were $\xi_0/a$, the slip velocity would start at zero and part (f) would apply from the start: constant velocity, no friction.
* **Energy.** During the slip the friction does the negative power $-\mu Mg\,s$, and the kinetic energy computed with the boxed solution decreases at exactly that rate; once the ball rolls, the energy is constant.
* **Independent derivation.** The time of the end of the slip and the state at the pins were recomputed symbolically from the boxed formulas; the quadratic root, the velocity and the angular velocity coincide with the values above.
* **Dimensions.** The time scale is the ratio of a speed to an acceleration; lengths are squared speeds over accelerations; the angular velocity is a speed over $a$.

---

## Problem RB-19: Sphere on the floor with spring

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous solid sphere $b$ of mass $M$, radius $a$ and centre $G$, resting on the horizontal plane $Oxy$ and touching it at one point $P$. A spring of constant $k$ and zero natural length joins the point $A$ of the surface of the sphere to the fixed point $C$ of the vertical axis, at the height $2a$ above $O$. Gravity acts downwards. The spring is massless, so it pulls on $A$ along the line from $A$ to $C$.
* **Fixed frame:** $S_0\{O; \mathbf i, \mathbf j, \mathbf k\}$, the frame $Oxyz$ of the figure, with $\mathbf k$ vertical upwards. It is inertial. The bold letter $\mathbf k$ is the unit vector; the plain $k$ is the spring constant.
* **Intermediate frames:** $S_1\{G; \mathbf i_1, \mathbf j_1, \mathbf k\}$, obtained by turning $\mathcal B_0$ by $\psi$ about $\mathbf k$; $S_2\{G; \mathbf i_2, \mathbf j_2, \mathbf k_2\}$, the frame $Gx_2y_2z_2$ of the statement, obtained by turning $\mathcal B_1$ by $\theta$ about $\mathbf j_1$. Then $\mathbf j_2$ equals $\mathbf j_1$: it is horizontal and normal to both $\mathbf k_2$ and $\mathbf k$, as the statement requires; $\psi$ is the angle from $Oy$ to $Gy_2$ and $\theta$ the angle from $Oz$ to $Gz_2$, which points from $G$ to $A$.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k_2\}$, obtained by turning $\mathcal B_2$ by $\varphi$ about $\mathbf k_2$; this is the rotation by which, in the statement, the frame $Gx_2y_2z_2$ differs from a body frame. The three angles are Euler angles in the order 3-2-3.
* **Coordinates:** $\xi$, $\eta$ (projection of $G$ on the plane), $\psi$, $\theta$, $\varphi$.
* **Degrees of freedom, smooth plane:** six coordinates of a free body minus the no-penetration constraint (Notes.pdf, Eq. 13.1), which fixes the height of $G$ at $a$: five, the five coordinates above. Unknowns: the five coordinates and the normal reaction $N$.
* **Degrees of freedom, rough plane with rolling without slip:** the two no-slip conditions (Notes.pdf, Eq. 13.5) relate rates and cannot be integrated, so the five coordinates are still needed but only three velocities are independent. Unknowns: the five coordinates, $N$ and the two friction components.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the sphere, homogeneous | $M$ | kg |
| Radius | $a$ | m |
| Spring constant, zero natural length | $k$ | N/m |
| Height of the anchor point $C$ on $Oz$ | $2a$ | m |
| Gravity | $g$, along $-\mathbf k$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb19-rot-psi.svg]]

> [!derivation] First rotation: psi about k
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View from above with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up; a positive $\psi$ turns counterclockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Triangle of $\mathbf j_1$: hypotenuse 1, adjacent leg along $\mathbf j$ (cosine), opposite leg along minus $\mathbf i$ (sine): the counterclockwise turn about the outward axis carries the tip of $\mathbf j$ to the left.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i + \sin\psi\,\mathbf j, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i + \cos\psi\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i &= \cos\psi\,\mathbf i_1 - \sin\psi\,\mathbf j_1, \qquad \mathbf j = \sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1 \quad &\text{(rows of the matrix: the inverse is the transpose)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k \quad &\text{(rotation about the fixed axis $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i + \sin\psi\,\mathbf j, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i + \cos\psi\,\mathbf j, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k}$$
>
> **Units:** dimensionless matrix; $[\mathrm{T^{-1}}]$
> **Meaning:** $\psi$ is the angle between $Oy$ and the horizontal axis $Gy_2$, as the statement defines it.

![[attachments/EM-SOL/rb19-rot-theta.svg]]

> [!derivation] Second rotation: theta about j1
> **Law:** simple rotation about the second axis; right-hand rule
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.17
>
> View with $\mathbf j_1$ pointing into the paper (⊗), $\mathbf i_1$ to the right and $\mathbf k$ up; this view is right-handed because the product of $\mathbf k$ and $\mathbf i_1$ is $\mathbf j_1$, and a positive rotation about an axis pointing into the paper looks clockwise. Triangle of $\mathbf i_2$: hypotenuse 1, adjacent leg along $\mathbf i_1$ (cosine of $\theta$), opposite leg along minus $\mathbf k$ (sine): the tip of $\mathbf i_1$ drops, as $Gx_2$ does in the figure. Triangle of $\mathbf k_2$: hypotenuse 1, adjacent leg along $\mathbf k$ (cosine), opposite leg along $\mathbf i_1$ (sine).
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k, \qquad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k, \qquad \mathbf j_2 = \mathbf j_1 \quad &\text{(legs of the two triangles; rotation axis unchanged)} \\
> [{}_1R_2] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 & -\cos\theta\sin\theta + \sin\theta\cos\theta \cr 0 & 1 & 0 \cr -\sin\theta\cos\theta + \cos\theta\sin\theta & 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_1 &= \cos\theta\,\mathbf i_2 + \sin\theta\,\mathbf k_2, \qquad \mathbf k = -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2 \quad &\text{(rows: the inverse is the transpose)} \\
> \mathbf k_2 &= \sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k \quad &\text{($\mathbf i_1$ of the first rotation)} \\
> \boldsymbol\omega_{21} &= \dot\theta\,\mathbf j_2 \quad &\text{(rotation about $\mathbf j_1$, equal to $\mathbf j_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\theta\,\mathbf i_2 + \sin\theta\,\mathbf k_2, \qquad \mathbf k = -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2, \qquad \mathbf k_2 = \sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\theta$ is the angle between $Oz$ and $GA$; with $\theta$ zero the point $A$ is at the top of the sphere, at the height of $C$.

![[attachments/EM-SOL/rb19-rot-phi.svg]]

> [!derivation] Third rotation: phi about k2
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.18; Notes.pdf, Sec. 9.2
>
> View with $\mathbf k_2$ out of the paper (⊙), $\mathbf i_2$ to the right and $\mathbf j_2$ up; the triangles are those of the first rotation with $\varphi$ in place of $\psi$.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\varphi\,\mathbf i_2 + \sin\varphi\,\mathbf j_2, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i_2 + \cos\varphi\,\mathbf j_2 \quad &\text{(adjacent legs along $\mathbf i_2$ and $\mathbf j_2$; tip of $\mathbf j_2$ towards minus $\mathbf i_2$)} \\
> [{}_2R_b] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_2$ in $\mathcal B_2$)} \\
> \det[{}_2R_b] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_2R_b][{}_2R_b]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b2} &= \dot\varphi\,\mathbf k_2 \quad &\text{(rotation about $\mathbf k_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\varphi\,\mathbf i_2 + \sin\varphi\,\mathbf j_2, \qquad \mathbf j_b = -\sin\varphi\,\mathbf i_2 + \cos\varphi\,\mathbf j_2, \qquad \boldsymbol\omega_{b2} = \dot\varphi\,\mathbf k_2}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the spin about $GA$ does not move $A$, so it does not change the spring force.

> [!derivation] Angular velocities of the sphere and of the frame Gx2y2z2
> **Law:** composition of the angular velocities of the simple rotations
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\theta\,\mathbf j_2 + \dot\psi\left(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2\right) \quad &\text{(composition; $\mathbf k$ in $\mathcal B_2$)} \\
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b2} + \boldsymbol\omega_{20} = -\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + \left(\dot\psi\cos\theta + \dot\varphi\right)\mathbf k_2 \quad &\text{(add the spin; Eq. 9.21)} \\
> \boldsymbol\omega_{b0} &= \dot\psi\,\mathbf k + \dot\theta\left(-\sin\psi\,\mathbf i + \cos\psi\,\mathbf j\right) + \dot\varphi\left(\sin\theta\cos\psi\,\mathbf i + \sin\theta\sin\psi\,\mathbf j + \cos\theta\,\mathbf k\right) \quad &\text{(same vector in $\mathcal B_0$)} \\
> \omega_x &= -\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi, \qquad \omega_y = \dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi \quad &\text{(horizontal components, used for rolling)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = -\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + n\,\mathbf k_2, \qquad n = \dot\psi\cos\theta + \dot\varphi, \qquad \boldsymbol\omega_{20} = -\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + \dot\psi\cos\theta\,\mathbf k_2}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every term
> **Meaning:** the sphere and the frame $Gx_2y_2z_2$ differ only by the spin along $\mathbf k_2$; $n$ is the total spin of the sphere about $GA$.

![[attachments/EM-SOL/rb19-spring.svg]]

> [!derivation] Positions of G, A and C, the spring vector and the contact point
> **Law:** position vectors as sums of segments; no penetration; velocity field of the rigid body
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.2
>
> The plane is tangent to the sphere at $P$ and the normal to a sphere passes through its centre, so $P$ is straight below $G$ and $G$ is at the height $a$. Write $\rho_1$ and $\rho_2$ for the components of the horizontal position of $G$ along $\mathbf i_1$ and $\mathbf j_1$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \xi\,\mathbf i + \eta\,\mathbf j + a\,\mathbf k, \qquad \mathbf r_G^A = a\,\mathbf k_2, \qquad \mathbf r_0^C = 2a\,\mathbf k, \qquad \mathbf r_G^P = -a\,\mathbf k \quad &\text{(definitions of the statement)} \\
> \overrightarrow{AC} &= \mathbf r_0^C - \mathbf r_0^G - \mathbf r_G^A = -\xi\,\mathbf i - \eta\,\mathbf j + a\,\mathbf k - a\,\mathbf k_2 \quad &\text{(head minus tail)} \\
> &= -\left(\xi + a\sin\theta\cos\psi\right)\mathbf i - \left(\eta + a\sin\theta\sin\psi\right)\mathbf j + a\left(1 - \cos\theta\right)\mathbf k \quad &\text{(in $\mathcal B_0$, with $\mathbf k_2$ of the second rotation)} \\
> -\xi\,\mathbf i - \eta\,\mathbf j &= -\rho_1\,\mathbf i_1 - \rho_2\,\mathbf j_1, \qquad \rho_1 = \xi\cos\psi + \eta\sin\psi, \quad \rho_2 = -\xi\sin\psi + \eta\cos\psi \quad &\text{($\mathbf i$ and $\mathbf j$ in $\mathcal B_1$)} \\
> \overrightarrow{AC} &= -\left(\rho_1\cos\theta + a\sin\theta\right)\mathbf i_2 - \rho_2\,\mathbf j_2 + \left(a\cos\theta - a - \rho_1\sin\theta\right)\mathbf k_2 \quad &\text{(in $\mathcal B_2$, with $\mathbf i_1$ and $\mathbf k$ of the second rotation)} \\
> \mathbf v_0^G &= \dot\xi\,\mathbf i + \dot\eta\,\mathbf j, \qquad \mathbf v_0^{P(b)} = \left(\dot\xi - a\,\omega_y\right)\mathbf i + \left(\dot\eta + a\,\omega_x\right)\mathbf j \quad &\text{(velocity field from $G$; the product of the angular velocity with $-a\,\mathbf k$ by its determinant)}
> \end{aligned}$$
>
> $$\boxed{\overrightarrow{AC} = -\left(\xi + a\sin\theta\cos\psi\right)\mathbf i - \left(\eta + a\sin\theta\sin\psi\right)\mathbf j + a\left(1 - \cos\theta\right)\mathbf k, \qquad \mathbf v_0^{P(b)} = \left(\dot\xi - a\,\omega_y\right)\mathbf i + \left(\dot\eta + a\,\omega_x\right)\mathbf j}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the vertical component of the spring vector is never negative: $A$ is never above the height $2a$ of $C$, so the spring always pulls the sphere upwards (or not at all, with $A$ at the top). The contact velocity has no vertical component (no penetration); on a smooth plane its horizontal components are free.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and inertia tensor of the sphere
> **Law:** mass, centre of mass and moments of inertia as volume integrals in spherical coordinates (jacobian $r^2\sin\chi$); relation between the three axial moments and the polar integral
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 21]
>
> Spherical coordinates about $G$: distance $r$ from 0 to $a$, colatitude $\chi$ from 0 to $\pi$, longitude $\lambda$ from 0 to $2\pi$; volume element $r^2\sin\chi\,dr\,d\chi\,d\lambda$; density $\rho$.
>
> $$\begin{aligned}
> V &= \int_0^{2\pi}d\lambda\int_0^{\pi}\sin\chi\,d\chi\int_0^a r^2\,dr = 2\pi\left[-\cos\chi\right]_0^{\pi}\left[\frac{r^3}{3}\right]_0^a \quad &\text{(separable integral; antiderivatives)} \\
> &= 2\pi\left(-\cos\pi + \cos 0\right)\left(\frac{a^3}{3} - 0\right) = \frac{4\pi a^3}{3} \quad &\text{(Barrow's rule)} \\
> \rho &= \frac{3M}{4\pi a^3}, \qquad \mathbf r_G^G = \mathbf 0 \quad &\text{(homogeneous; every plane through the centre is a plane of symmetry)} \\
> I_x + I_y + I_z &= 2\int r^2\,dm = 2\rho\cdot 2\pi\cdot 2\cdot\left[\frac{r^5}{5}\right]_0^a = \frac{8\pi\rho a^5}{5} \quad &\text{(Eq. 10.13; same angular factors; Barrow's rule)} \\
> &= \frac{8\pi a^5}{5}\cdot\frac{3M}{4\pi a^3} = \frac65\,Ma^2 \quad &\text{(value of $\rho$)} \\
> I_x &= I_y = I_z = \frac25\,Ma^2 \quad &\text{(the three axes are equivalent for a sphere)} \\
> \left[\frac{\sin^2\lambda}{2}\right]_0^{2\pi} &= 0, \quad \left[\sin\lambda\right]_0^{2\pi} = 0, \quad \left[-\cos\lambda\right]_0^{2\pi} = 0 \quad &\text{(longitude integrals of $\cos\lambda\sin\lambda$, $\cos\lambda$, $\sin\lambda$: products of inertia zero, Eq. 10.15)} \\
> [R]\left(\tfrac25 Ma^2[U]\right)[R]^T &= \tfrac25 Ma^2\,[U] \quad &\text{(any change of basis, Eq. 10.41)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac25\,Ma^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in every basis, in particular in } Gx_2y_2z_2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the frame $Gx_2y_2z_2$ is not attached to the sphere, but the tensor has the same constant components there, which is what makes that frame convenient.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (a)i: momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]; [Lecture 9, Slide 10]
>
> $$\begin{aligned}
> \mathbf p_0 &= M\left(\dot\xi\,\mathbf i + \dot\eta\,\mathbf j\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \frac25\,Ma^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} -\dot\psi\sin\theta \cr \dot\theta \cr n \end{bmatrix} \quad &\text{(Eq. 11.12 in $\mathcal B_2$)} \\
> &= \frac25\,Ma^2\left(-\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + n\,\mathbf k_2\right) \quad &\text{(row by column)} \\
> T_0 &= \frac12\,M\left(\dot\xi^2 + \dot\eta^2\right) + \frac15\,Ma^2\left(\dot\psi^2\sin^2\theta + \dot\theta^2 + n^2\right) \quad &\text{(Eq. 11.31)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} = \frac25\,Ma^2\left[-\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + \left(\dot\psi\cos\theta + \dot\varphi\right)\mathbf k_2\right]}$$
>
> **Units:** kg m$^2$/s; J
> **Meaning:** the angular momentum is parallel to the angular velocity; written in $Gx_2y_2z_2$ its components do not depend on $\varphi$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb19-fbd.svg]]

| Force | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-Mg\,\mathbf k$ | applied, conservative |
| Spring | $A$ | $k$ times the vector from $A$ to $C$ | applied, conservative |
| Normal reaction | $P$ | $N\,\mathbf k$ | constraint |
| Friction (part (b) only) | $P$ | $F_x\,\mathbf i + F_y\,\mathbf j$, unknown | constraint |

> [!derivation] Part (a)ii: force and torque of the spring
> **Law:** linear spring of zero natural length; moment about $G$ by a determinant in $\mathcal B_2$
> **Source:** Notes.pdf, Eq. 5.1; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> A spring of zero natural length pulls each end towards the other with a force equal to the constant times the full extension vector.
>
> $$\begin{aligned}
> \mathbf F_s &= k\,\overrightarrow{AC} = -k\left(\xi + a\sin\theta\cos\psi\right)\mathbf i - k\left(\eta + a\sin\theta\sin\psi\right)\mathbf j + ka\left(1 - \cos\theta\right)\mathbf k \quad &\text{(Eq. 5.1 in vector form)} \\
> \mathbf M_{G,s} &= \mathbf r_G^A\times\mathbf F_s = \begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr 0 & 0 & a \cr -k\left(\rho_1\cos\theta + a\sin\theta\right) & -k\rho_2 & k\left(a\cos\theta - a - \rho_1\sin\theta\right) \end{vmatrix} \quad &\text{(arm $a\,\mathbf k_2$; spring vector in $\mathcal B_2$)} \\
> &= \mathbf i_2\left(0 + ka\rho_2\right) - \mathbf j_2\left(0 + ka\left(\rho_1\cos\theta + a\sin\theta\right)\right) + \mathbf k_2\,(0 - 0) \quad &\text{(expand along the first row)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_{G,s} = ka\left(-\xi\sin\psi + \eta\cos\psi\right)\mathbf i_2 - ka\left(\left(\xi\cos\psi + \eta\sin\psi\right)\cos\theta + a\sin\theta\right)\mathbf j_2}$$
>
> **Units:** N; N m
> **Meaning:** the torque of the spring is normal to $GA$, so it never changes the spin about $GA$; the weight acts at $G$ and the normal reaction passes through $G$, so on the smooth plane the spring is the only source of moment.

> [!derivation] Part (a)iii and (a)iv: force equation and normal reaction
> **Law:** Newton's second law for the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> M\,\mathbf a_0^G &= \mathbf F_s - Mg\,\mathbf k + N\,\mathbf k \quad &\text{(Eq. 12.8, smooth plane)} \\
> \mathbf a_0^G &= \ddot\xi\,\mathbf i + \ddot\eta\,\mathbf j \quad &\text{(second derivative of the position; height constant)} \\
> M\,\ddot\xi &= -k\left(\xi + a\sin\theta\cos\psi\right) \quad &\text{(component along $\mathbf i$)} \\
> M\,\ddot\eta &= -k\left(\eta + a\sin\theta\sin\psi\right) \quad &\text{(component along $\mathbf j$)} \\
> 0 &= ka\left(1 - \cos\theta\right) - Mg + N \quad &\text{(component along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{M\,\ddot\xi = -k\left(\xi + a\sin\theta\cos\psi\right), \qquad M\,\ddot\eta = -k\left(\eta + a\sin\theta\sin\psi\right), \qquad N = Mg - ka\left(1 - \cos\theta\right)}$$
>
> **Units:** N in every term
> **Meaning:** the spring pulls $G$ towards the vertical through $C$, shifted by the horizontal offset of $A$ from $G$. The normal reaction depends only on $\theta$: it equals the weight with $A$ at the top and is smallest, $Mg - 2ka$, with $A$ at the bottom; the sphere stays on the plane while it is positive.

> [!derivation] Part (a)iii: moment equation about G
> **Law:** moment equation about the centre of mass; Coriolis theorem between $S_0$ and $Gx_2y_2z_2$; vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 12.20
>
> Write $I$ for the moment of inertia two fifths of $Ma^2$. The pole $G$ is allowed because the term in the velocity of the pole of Eq. 12.13 vanishes for the centre of mass.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= \left.\frac{d\mathbf H_{G,0}}{dt}\right|_2 + \boldsymbol\omega_{20}\times\mathbf H_{G,0} \quad &\text{(Coriolis theorem, Eq. 3.8)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_2 &= I\left(-\ddot\psi\sin\theta - \dot\psi\cos\theta\,\dot\theta\right)\mathbf i_2 + I\ddot\theta\,\mathbf j_2 + I\dot n\,\mathbf k_2 \quad &\text{(derivatives of the components; product and chain rules)} \\
> \boldsymbol\omega_{20}\times\mathbf H_{G,0} &= I\begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr -\dot\psi\sin\theta & \dot\theta & \dot\psi\cos\theta \cr -\dot\psi\sin\theta & \dot\theta & n \end{vmatrix} \quad &\text{(determinant form)} \\
> &= I\left[\mathbf i_2\,\dot\theta\left(n - \dot\psi\cos\theta\right) - \mathbf j_2\left(-\dot\psi\sin\theta\,n + \dot\psi^2\sin\theta\cos\theta\right) + \mathbf k_2\left(-\dot\psi\sin\theta\,\dot\theta + \dot\theta\dot\psi\sin\theta\right)\right] \quad &\text{(expand along the first row)} \\
> &= I\left(\dot\theta\dot\varphi\,\mathbf i_2 + \dot\psi\dot\varphi\sin\theta\,\mathbf j_2\right) \quad &\text{($n$ minus the rate of $\psi$ times the cosine is the rate of $\varphi$)} \\
> I\left(-\ddot\psi\sin\theta - \dot\psi\dot\theta\cos\theta + \dot\theta\dot\varphi\right) &= ka\,\rho_2 \quad &\text{(component along $\mathbf i_2$)} \\
> I\left(\ddot\theta + \dot\psi\dot\varphi\sin\theta\right) &= -ka\left(\rho_1\cos\theta + a\sin\theta\right) \quad &\text{(component along $\mathbf j_2$)} \\
> I\,\dot n &= 0 \quad &\text{(component along $\mathbf k_2$)}
> \end{aligned}$$
>
> $$\boxed{\tfrac25 Ma\left(-\ddot\psi\sin\theta - \dot\psi\dot\theta\cos\theta + \dot\theta\dot\varphi\right) = k\left(-\xi\sin\psi + \eta\cos\psi\right), \quad \tfrac25 Ma\left(\ddot\theta + \dot\psi\dot\varphi\sin\theta\right) = -k\left(\left(\xi\cos\psi + \eta\sin\psi\right)\cos\theta + a\sin\theta\right), \quad \dot\psi\cos\theta + \dot\varphi = n_0}$$
>
> **Units:** N in the first two equations (each side divided by $a$); $[\mathrm{T^{-1}}]$ for $n_0$
> **Meaning:** the spin about the moving axis $GA$ is conserved for two reasons together: no force has a moment along $GA$ (the spring acts on $GA$ itself and the other forces pass through $G$), and the gyroscopic term has no component along $GA$ because the tensor is isotropic. With the two force equations, these are the five ordinary differential equations for $\xi$, $\eta$, $\psi$, $\theta$, $\varphi$.

#### Part (b): rough plane, rolling without slip

> [!derivation] Changes to the equations and to the reactions
> **Law:** no-slip conditions; friction as an unknown reaction; moment of the friction about $G$ by a determinant
> **Source:** Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2; Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> Write the friction in $\mathcal B_1$ as $F_1\,\mathbf i_1 + F_2\,\mathbf j_1$, so that $F_1$ is the $\mathbf i$ component times the cosine of $\psi$ plus the $\mathbf j$ component times its sine, and $F_2$ minus the $\mathbf i$ component times the sine plus the $\mathbf j$ component times the cosine.
>
> $$\begin{aligned}
> \dot\xi &= a\left(\dot\theta\cos\psi + \dot\varphi\sin\theta\sin\psi\right), \qquad \dot\eta = -a\left(-\dot\theta\sin\psi + \dot\varphi\sin\theta\cos\psi\right) \quad &\text{(contact velocity zero, Eq. 13.5)} \\
> M\,\ddot\xi &= -k\left(\xi + a\sin\theta\cos\psi\right) + F_x, \qquad M\,\ddot\eta = -k\left(\eta + a\sin\theta\sin\psi\right) + F_y \quad &\text{(force equation with the friction)} \\
> \left(-a\,\mathbf k\right)\times\left(F_1\,\mathbf i_1 + F_2\,\mathbf j_1\right) &= -aF_1\,\mathbf j_1 + aF_2\,\mathbf i_1 \quad &\text{($\mathbf k\times\mathbf i_1 = \mathbf j_1$, $\mathbf k\times\mathbf j_1 = -\mathbf i_1$)} \\
> &= aF_2\cos\theta\,\mathbf i_2 - aF_1\,\mathbf j_2 + aF_2\sin\theta\,\mathbf k_2 \quad &\text{($\mathbf i_1$ of the second rotation)} \\
> I\left(-\ddot\psi\sin\theta - \dot\psi\dot\theta\cos\theta + \dot\theta\dot\varphi\right) &= ka\,\rho_2 + aF_2\cos\theta \quad &\text{(component along $\mathbf i_2$)} \\
> I\left(\ddot\theta + \dot\psi\dot\varphi\sin\theta\right) &= -ka\left(\rho_1\cos\theta + a\sin\theta\right) - aF_1 \quad &\text{(component along $\mathbf j_2$)} \\
> I\,\frac{d}{dt}\left(\dot\psi\cos\theta + \dot\varphi\right) &= aF_2\sin\theta \quad &\text{(component along $\mathbf k_2$)} \\
> N &= Mg - ka\left(1 - \cos\theta\right) \quad &\text{(vertical component unchanged: the friction is horizontal)}
> \end{aligned}$$
>
> $$\boxed{\text{7 equations (2 forces, 3 moments, 2 rolling conditions) for } \xi, \eta, \psi, \theta, \varphi, F_x, F_y; \qquad N = Mg - ka\left(1 - \cos\theta\right)}$$
>
> **Units:** N for the forces; N m for the moments; m/s for the rolling conditions
> **Meaning:** the friction becomes two more unknowns, balanced by the two rolling conditions. It enters the two force equations and all three moment equations; in particular the spin about $GA$ is no longer conserved, because the friction has the moment $aF_2\sin\theta$ about $GA$ whenever that axis is tilted. The normal reaction keeps the same expression. The friction can be eliminated with the force equations, $F_x$ equal to $M$ times the second rate of $\xi$ plus the spring term, and the problem becomes five second-order equations constrained by the two rolling relations.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a)i Angular momentum about $G$ | $\tfrac25 Ma^2\left[-\dot\psi\sin\theta\,\mathbf i_2 + \dot\theta\,\mathbf j_2 + (\dot\psi\cos\theta + \dot\varphi)\,\mathbf k_2\right]$ |
| (a)ii Spring force | $-k(\xi + a\sin\theta\cos\psi)\,\mathbf i - k(\eta + a\sin\theta\sin\psi)\,\mathbf j + ka(1 - \cos\theta)\,\mathbf k$ at $A$ |
| (a)ii Spring torque about $G$ | $ka(-\xi\sin\psi + \eta\cos\psi)\,\mathbf i_2 - ka\left((\xi\cos\psi + \eta\sin\psi)\cos\theta + a\sin\theta\right)\mathbf j_2$ |
| (a)iii Five equations | $M\ddot\xi = -k(\xi + a\sin\theta\cos\psi)$; $M\ddot\eta = -k(\eta + a\sin\theta\sin\psi)$; $\tfrac25 Ma(-\ddot\psi\sin\theta - \dot\psi\dot\theta\cos\theta + \dot\theta\dot\varphi) = k(-\xi\sin\psi + \eta\cos\psi)$; $\tfrac25 Ma(\ddot\theta + \dot\psi\dot\varphi\sin\theta) = -k((\xi\cos\psi + \eta\sin\psi)\cos\theta + a\sin\theta)$; $\dot\psi\cos\theta + \dot\varphi = n_0$ |
| (a)iv Reaction | $N\,\mathbf k$ with $N = Mg - ka(1 - \cos\theta)$ |
| (b) Rough plane | add $F_x\,\mathbf i + F_y\,\mathbf j$ at $P$ to the force equations and its moment $aF_2\cos\theta\,\mathbf i_2 - aF_1\,\mathbf j_2 + aF_2\sin\theta\,\mathbf k_2$ to the moment equations (the third one loses its first integral), plus the two rolling conditions; $N$ unchanged |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: energy integral on the smooth plane
> **Law:** conservation of the mechanical energy; potential of a spring of zero natural length and of the weight
> **Source:** Notes.pdf, Eq. 5.2; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34
>
> $$\begin{aligned}
> V_0 &= \frac12\,k\left|\overrightarrow{AC}\right|^2 + Mga \quad &\text{(Eq. 5.2 with the extension equal to the length; Eq. 12.34 with $G$ at height $a$)} \\
> \left|\overrightarrow{AC}\right|^2 &= \left(\xi + a\sin\theta\cos\psi\right)^2 + \left(\eta + a\sin\theta\sin\psi\right)^2 + a^2\left(1 - \cos\theta\right)^2 \quad &\text{(components in $\mathcal B_0$)} \\
> \dot W_P &= N\,\mathbf k\cdot\mathbf v_0^{P(b)} = 0 \quad &\text{(the contact velocity is horizontal)} \\
> T_0 + V_0 &= E_0 \quad &\text{(Eq. 12.33)}
> \end{aligned}$$
>
> $$\boxed{\frac12 M\left(\dot\xi^2 + \dot\eta^2\right) + \frac15 Ma^2\left(\dot\psi^2\sin^2\theta + \dot\theta^2 + n_0^2\right) + \frac12 k\left|\overrightarrow{AC}\right|^2 = E_0 - Mga}$$
>
> **Units:** J in every term
> **Meaning:** the five equations of part (a) were also obtained independently from these kinetic and potential energies with the five coordinates (Lagrange's equations, used only as a check); the two force equations and the equations for $\theta$ and $\varphi$ coincide term by term, and the equation for $\psi$ is the combination of the components along $\mathbf i_2$ and $\mathbf k_2$ that gives the moment about the vertical $\mathbf k$.

**Limiting cases and consistency:**

* **Equilibrium.** With $G$ above $O$ and $A$ at the top ($\xi$, $\eta$, $\theta$ zero), $A$ coincides with $C$, the spring is unstretched, every right-hand side vanishes and $N$ equals $Mg$: an equilibrium.
* **No spring.** With $k$ zero, $G$ moves uniformly on the plane and the three moment equations are those of a free sphere, whose angular velocity is constant.
* **Lift-off.** On the smooth plane the reaction can only vanish if the spring pulls hard enough: $N$ becomes zero for $ka(1 - \cos\theta)$ equal to $Mg$, possible only if $2ka$ exceeds $Mg$.
* **Dimensions.** $k$ times a length is a force; the equations with the factor two fifths of $Ma$ have N on both sides.

---

## Problem RB-22: Ball with bar on inclined plane

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous solid sphere $b$ of mass $M$, radius $R$ and centre $G$, always touching a fixed plane inclined at the angle $\gamma$; the contact point is $P$. A rigid massless rod, pinned at the point $O$ of the plane, passes through a small diametral hole of the sphere; the sphere slides along the rod and turns about it without friction. Gravity acts downwards.
* **Horizontal frame:** $S_h\{O; \mathbf I, \mathbf j, \mathbf K\}$, with $\mathbf K$ vertical upwards, $\mathbf j$ the horizontal line of the plane and $\mathbf I$ horizontal, towards the side where the plane goes down.
* **Fixed frame:** $S\{O; \mathbf i, \mathbf j, \mathbf k\}$, the frame $Oxyz$ of the statement: $\mathbf i$ down the line of maximum slope, $\mathbf k$ normal to the plane, upwards, and $\mathbf j$ completing a right-handed basis (horizontal). The plane is at rest, so this frame is inertial.
* **Auxiliary frame:** $S_2\{O; \mathbf i_2, \mathbf j_2, \mathbf k\}$, turned by $\theta$ about $\mathbf k$, with $\mathbf i_2$ along $OP$, as the statement defines it.
* **Frame of the rod:** $S_3\{O; \mathbf u, \mathbf j_2, \mathbf w\}$, with $\mathbf u$ along the rod from $O$ to $G$ (at the angle $\beta$ above the plane), $\mathbf j_2$ normal to the rod and parallel to the plane, and $\mathbf w$ normal to the rod in the vertical plane of $\mathbf i_2$ and $\mathbf k$. Read from the figure: $\varphi$ is drawn at $G$ from this normal line, so the rod is taken as carried by the two rotations $\theta$ (about $\mathbf k$) and $\beta$ (about $\mathbf j_2$), as by a universal joint at $O$; this is the reading of "free to turn in any direction but it does not rotate along its longitudinal axis". The angular velocity of this frame has an axial component equal to the rate of $\theta$ times the sine of $\beta$; with another convention for the rod, only the definition of $\varphi$ (and its rate in part (c)) changes, not the forces or the motion of $G$.
* **Body frame:** $S_b\{G; \mathbf u, \mathbf e_2, \mathbf e_3\}$, turned by $\varphi$ about the rod.
* **Part (a), coordinates:** a free body has six coordinates. Contact with the plane (no penetration, Notes.pdf, Eq. 13.1) fixes the height of $G$ at $R$: five remain, the two coordinates of $P$ in the plane and three angles. The rod is free to turn about $O$, so it imposes nothing on the position of $G$ (it simply points from $O$ to $G$), but the hole aligns a body diameter with the rod: two conditions on the orientation. Three coordinates remain: $\theta$ and $d$ (the polar coordinates of $P$ in the plane) and $\varphi$; $\beta$ is a function of $d$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the sphere, homogeneous | $M$ | kg |
| Radius | $R$ | m |
| Inclination of the plane | $\gamma$ | rad |
| Rod | massless, rigid, pinned at $O$; smooth along and about its axis | - |
| Angle of the rod with the plane | $\beta$, with tangent $R/d$ | rad |
| Gravity | $g$, along $-\mathbf K$ | m/s$^2$ |
| Initial state, part (j) | $\mathbf r_{G0} = 2R\,\mathbf i + 3R\,\mathbf j + R\,\mathbf k$, $\mathbf v_{G0} = -\sqrt{Rg}\,(\mathbf i + \mathbf j)$ | m, m/s |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb22-rot-gamma.svg]]

> [!derivation] Basis of the plane: rotation by gamma about j
> **Law:** simple rotation about the second axis, positive by the right-hand rule
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.16; [Lecture 7, Slide 12]
>
> View with $\mathbf j$ pointing into the paper (⊗), $\mathbf I$ to the right and $\mathbf K$ up; this view is right-handed because the product of $\mathbf K$ and $\mathbf I$ is $\mathbf j$, and a positive rotation about an axis pointing into the paper looks clockwise. Triangle of $\mathbf i$: hypotenuse 1 down the slope, adjacent leg along $\mathbf I$ (cosine of $\gamma$), opposite leg along minus $\mathbf K$ (sine). Triangle of $\mathbf k$: hypotenuse 1 along the normal, adjacent leg along $\mathbf K$ (cosine), opposite leg along $\mathbf I$ (sine).
>
> $$\begin{aligned}
> \mathbf i &= \cos\gamma\,\mathbf I - \sin\gamma\,\mathbf K, \qquad \mathbf k = \sin\gamma\,\mathbf I + \cos\gamma\,\mathbf K \quad &\text{(legs of the two triangles)} \\
> [{}_hR_0] &= \begin{bmatrix} \cos\gamma & 0 & \sin\gamma \cr 0 & 1 & 0 \cr -\sin\gamma & 0 & \cos\gamma \end{bmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_h$)} \\
> \det[{}_hR_0] &= 1\cdot\left(\cos^2\gamma + \sin^2\gamma\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_hR_0][{}_hR_0]^T &= \begin{bmatrix} \cos^2\gamma + \sin^2\gamma & 0 & -\cos\gamma\sin\gamma + \sin\gamma\cos\gamma \cr 0 & 1 & 0 \cr -\sin\gamma\cos\gamma + \cos\gamma\sin\gamma & 0 & \sin^2\gamma + \cos^2\gamma \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf K &= -\sin\gamma\,\mathbf i + \cos\gamma\,\mathbf k \quad &\text{(third row: the inverse is the transpose)} \\
> M\,\mathbf g &= -Mg\,\mathbf K = Mg\sin\gamma\,\mathbf i - Mg\cos\gamma\,\mathbf k \quad &\text{(weight in the basis of the plane)}
> \end{aligned}$$
>
> $$\boxed{M\,\mathbf g = Mg\sin\gamma\,\mathbf i - Mg\cos\gamma\,\mathbf k}$$
>
> **Units:** dimensionless matrix; N
> **Meaning:** the weight pulls the sphere down the slope, along $\mathbf i$, and presses it against the plane.

![[attachments/EM-SOL/rb22-rot-theta.svg]]

> [!derivation] Auxiliary basis: rotation by theta about k
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2
>
> View of the plane from above with $\mathbf k$ out of the paper (⊙), $\mathbf i$ to the right and $\mathbf j$ up; a positive $\theta$ turns counterclockwise. Triangle of $\mathbf i_2$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine), opposite leg along $\mathbf j$ (sine). Triangle of $\mathbf j_2$: adjacent leg along $\mathbf j$ (cosine), opposite leg along minus $\mathbf i$ (sine), because the counterclockwise turn carries the tip of $\mathbf j$ to the left.
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \qquad \mathbf j_2 = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_2] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_2][{}_0R_2]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i &= \cos\theta\,\mathbf i_2 - \sin\theta\,\mathbf j_2 \quad &\text{(first row: the inverse is the transpose)} \\
> \boldsymbol\omega_{20} &= \dot\theta\,\mathbf k, \qquad \dot{\mathbf i}_2 = \dot\theta\,\mathbf k\times\mathbf i_2 = \dot\theta\,\mathbf j_2, \qquad \dot{\mathbf j}_2 = \dot\theta\,\mathbf k\times\mathbf j_2 = -\dot\theta\,\mathbf i_2 \quad &\text{(Poisson)} \\
> M\,\mathbf g &= Mg\sin\gamma\cos\theta\,\mathbf i_2 - Mg\sin\gamma\sin\theta\,\mathbf j_2 - Mg\cos\gamma\,\mathbf k \quad &\text{(weight in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_2 = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \qquad \boldsymbol\omega_{20} = \dot\theta\,\mathbf k, \qquad M\,\mathbf g = Mg\sin\gamma\left(\cos\theta\,\mathbf i_2 - \sin\theta\,\mathbf j_2\right) - Mg\cos\gamma\,\mathbf k}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$; N
> **Meaning:** for positive $\theta$ the downhill pull has a component along minus $\mathbf j_2$, which turns $OP$ back towards the line of maximum slope.

![[attachments/EM-SOL/rb22-rod-section.svg]]

> [!derivation] Frame of the rod: rotation by beta about j2, and the rate of beta
> **Law:** simple rotation about the second axis; right triangle of the rod; chain rule
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.17; Notes.pdf, Eq. 2.6
>
> Vertical section through $O$, $P$ and $G$, with $\mathbf i_2$ to the right, $\mathbf k$ up and $\mathbf j_2$ pointing into the paper (⊗). Right triangle $OPG$: the leg $d$ along the plane from $O$ to $P$, the leg $R$ from $P$ to $G$ along the normal, and the hypotenuse $OG$ of length $L$, along the rod; $\beta$ is the angle at $O$. The rod turns counterclockwise as seen, which is a rotation about minus $\mathbf j_2$. Triangle of $\mathbf u$: adjacent leg along $\mathbf i_2$ (cosine), opposite leg along $\mathbf k$ (sine). Triangle of $\mathbf w$: adjacent leg along $\mathbf k$ (cosine), opposite leg along minus $\mathbf i_2$ (sine): the tip of $\mathbf k$ moves to the left.
>
> $$\begin{aligned}
> L &= \sqrt{d^2 + R^2}, \qquad \cos\beta = \frac dL, \qquad \sin\beta = \frac RL, \qquad \tan\beta = \frac Rd \quad &\text{(right triangle $OPG$)} \\
> \mathbf u &= \cos\beta\,\mathbf i_2 + \sin\beta\,\mathbf k, \qquad \mathbf w = -\sin\beta\,\mathbf i_2 + \cos\beta\,\mathbf k \quad &\text{(legs of the triangles of the unit vectors)} \\
> [{}_2R_3] &= \begin{bmatrix} \cos\beta & 0 & -\sin\beta \cr 0 & 1 & 0 \cr \sin\beta & 0 & \cos\beta \end{bmatrix} \quad &\text{(columns: $\mathbf u$, $\mathbf j_2$, $\mathbf w$ in $\mathcal B_2$)} \\
> \det[{}_2R_3] &= 1\cdot\left(\cos^2\beta + \sin^2\beta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_2R_3][{}_2R_3]^T &= \begin{bmatrix} \cos^2\beta + \sin^2\beta & 0 & \cos\beta\sin\beta - \sin\beta\cos\beta \cr 0 & 1 & 0 \cr \sin\beta\cos\beta - \cos\beta\sin\beta & 0 & \sin^2\beta + \cos^2\beta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf u\times\mathbf j_2 &= \cos\beta\,\mathbf i_2\times\mathbf j_2 + \sin\beta\,\mathbf k\times\mathbf j_2 = \cos\beta\,\mathbf k - \sin\beta\,\mathbf i_2 = \mathbf w \quad &\text{(the triad is right-handed)} \\
> \frac{d}{dt}\tan\beta &= \frac{\dot\beta}{\cos^2\beta} = -\frac{R\,\dot d}{d^2} \quad &\text{(chain rule on both sides of the tangent)} \\
> \dot\beta &= -\frac{R\,\dot d}{d^2}\cdot\frac{d^2}{d^2 + R^2} = -\frac{R\,\dot d}{d^2 + R^2} \quad &\text{(square of the cosine from the triangle)} \\
> \boldsymbol\omega_{32} &= -\dot\beta\,\mathbf j_2, \qquad \boldsymbol\omega_{30} = \dot\theta\,\mathbf k - \dot\beta\,\mathbf j_2 \quad &\text{(rotation about minus $\mathbf j_2$; composition, Eq. 9.21)}
> \end{aligned}$$
>
> $$\boxed{\mathbf u = \cos\beta\,\mathbf i_2 + \sin\beta\,\mathbf k, \qquad \mathbf w = -\sin\beta\,\mathbf i_2 + \cos\beta\,\mathbf k, \qquad \dot\beta = -\frac{R\,\dot d}{d^2 + R^2}, \qquad \boldsymbol\omega_{30} = \dot\theta\,\mathbf k - \dot\beta\,\mathbf j_2}$$
>
> **Units:** dimensionless; $\dot\beta$ in $[\mathrm L][\mathrm{L\,T^{-1}}]/[\mathrm{L^2}] = [\mathrm{T^{-1}}]$
> **Meaning:** when the sphere moves away from $O$ the rod flattens: $\beta$ decreases while $d$ grows.

![[attachments/EM-SOL/rb22-rot-phi.svg]]

> [!derivation] Body basis: rotation by phi about the rod
> **Law:** simple rotation about the first axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2
>
> View along the rod with $\mathbf u$ out of the paper (⊙), $\mathbf j_2$ to the right and $\mathbf w$ up; this is right-handed because the product of $\mathbf u$ and $\mathbf j_2$ is $\mathbf w$. A positive $\varphi$ turns counterclockwise. Triangle of $\mathbf e_2$: adjacent leg along $\mathbf j_2$ (cosine), opposite leg along $\mathbf w$ (sine). Triangle of $\mathbf e_3$: adjacent leg along $\mathbf w$ (cosine), opposite leg along minus $\mathbf j_2$ (sine).
>
> $$\begin{aligned}
> \mathbf e_2 &= \cos\varphi\,\mathbf j_2 + \sin\varphi\,\mathbf w, \qquad \mathbf e_3 = -\sin\varphi\,\mathbf j_2 + \cos\varphi\,\mathbf w \quad &\text{(legs of the two triangles)} \\
> [{}_3R_b] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\varphi & -\sin\varphi \cr 0 & \sin\varphi & \cos\varphi \end{bmatrix} \quad &\text{(columns: $\mathbf u$, $\mathbf e_2$, $\mathbf e_3$ in $\mathcal B_3$)} \\
> \det[{}_3R_b] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_3R_b][{}_3R_b]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi \cr 0 & \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b3} &= \dot\varphi\,\mathbf u \quad &\text{(rotation about the rod)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_2 = \cos\varphi\,\mathbf j_2 + \sin\varphi\,\mathbf w, \qquad \mathbf e_3 = -\sin\varphi\,\mathbf j_2 + \cos\varphi\,\mathbf w, \qquad \boldsymbol\omega_{b3} = \dot\varphi\,\mathbf u}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the sphere can only turn about the rod relative to the rod frame; that is the content of the two orientation constraints of part (a).

> [!derivation] Part (b): angular velocity and angular acceleration of the sphere
> **Law:** composition of angular velocities; Coriolis theorem between $S$ and $S_2$; product and chain rules
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.9; Notes.pdf, Sec. 15.1
>
> Write the angular velocity in $\mathcal B_2$ with the components $a_1$, $a_2$, $a_3$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b3} + \boldsymbol\omega_{30} = \dot\varphi\left(\cos\beta\,\mathbf i_2 + \sin\beta\,\mathbf k\right) + \dot\theta\,\mathbf k - \dot\beta\,\mathbf j_2 \quad &\text{(composition; $\mathbf u$ in $\mathcal B_2$)} \\
> a_1 &= \dot\varphi\cos\beta, \qquad a_2 = -\dot\beta, \qquad a_3 = \dot\theta + \dot\varphi\sin\beta \quad &\text{(collect)} \\
> \boldsymbol\alpha_{b0} &= \left.\frac{d\boldsymbol\omega_{b0}}{dt}\right|_2 + \dot\theta\,\mathbf k\times\left(a_1\,\mathbf i_2 + a_2\,\mathbf j_2 + a_3\,\mathbf k\right) \quad &\text{(Coriolis theorem with $S_2$, Eq. 3.8)} \\
> \dot\theta\,\mathbf k\times\left(a_1\,\mathbf i_2 + a_2\,\mathbf j_2\right) &= \dot\theta\,a_1\,\mathbf j_2 - \dot\theta\,a_2\,\mathbf i_2 \quad &\text{($\mathbf k\times\mathbf i_2 = \mathbf j_2$, $\mathbf k\times\mathbf j_2 = -\mathbf i_2$)} \\
> \dot a_1 &= \ddot\varphi\cos\beta - \dot\varphi\sin\beta\,\dot\beta, \qquad \dot a_3 = \ddot\theta + \ddot\varphi\sin\beta + \dot\varphi\cos\beta\,\dot\beta \quad &\text{(product and chain rules)} \\
> \ddot\beta &= -\frac{R\,\ddot d}{d^2 + R^2} + \frac{2Rd\,\dot d^2}{\left(d^2 + R^2\right)^2} \quad &\text{(quotient rule on the rate of $\beta$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \dot\varphi\cos\beta\,\mathbf i_2 - \dot\beta\,\mathbf j_2 + \left(\dot\theta + \dot\varphi\sin\beta\right)\mathbf k, \qquad \boldsymbol\alpha_{b0} = \left(\ddot\varphi\cos\beta - \dot\varphi\dot\beta\sin\beta + \dot\theta\dot\beta\right)\mathbf i_2 + \left(-\ddot\beta + \dot\theta\dot\varphi\cos\beta\right)\mathbf j_2 + \left(\ddot\theta + \ddot\varphi\sin\beta + \dot\varphi\dot\beta\cos\beta\right)\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ and $[\mathrm{T^{-2}}]$
> **Meaning:** with the cosine and sine of $\beta$ equal to $d/L$ and $R/L$ and the rate of $\beta$ from the previous box, both vectors are functions of $\theta$, $d$, $\varphi$ and their derivatives only.

> [!derivation] Part (b): velocity and acceleration of G
> **Law:** derivative of a position vector written in a moving basis; Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf r_0^G &= \overrightarrow{OP} + \overrightarrow{PG} = d\,\mathbf i_2 + R\,\mathbf k \quad &\text{(sum of segments; $G$ above $P$ at the height $R$)} \\
> \mathbf v_0^G &= \dot d\,\mathbf i_2 + d\,\dot{\mathbf i}_2 = \dot d\,\mathbf i_2 + d\,\dot\theta\,\mathbf j_2 \quad &\text{(product rule; Poisson)} \\
> \mathbf a_0^G &= \ddot d\,\mathbf i_2 + \dot d\,\dot\theta\,\mathbf j_2 + \left(\dot d\,\dot\theta + d\,\ddot\theta\right)\mathbf j_2 + d\,\dot\theta\left(-\dot\theta\,\mathbf i_2\right) \quad &\text{(product rule on each term; Poisson)} \\
> &= \left(\ddot d - d\,\dot\theta^2\right)\mathbf i_2 + \left(d\,\ddot\theta + 2\,\dot d\,\dot\theta\right)\mathbf j_2 \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \dot d\,\mathbf i_2 + d\,\dot\theta\,\mathbf j_2, \qquad \mathbf a_0^G = \left(\ddot d - d\,\dot\theta^2\right)\mathbf i_2 + \left(d\,\ddot\theta + 2\,\dot d\,\dot\theta\right)\mathbf j_2}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $G$ moves parallel to the plane like a point in polar coordinates $(d, \theta)$ at the constant height $R$.

> [!derivation] Part (c): velocity of P and rolling without slip
> **Law:** velocity field of the rigid body; rolling without slipping on a fixed plane; vector product by its determinant
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> \mathbf v_0^{P(b)} &= \mathbf v_0^G + \boldsymbol\omega_{b0}\times\left(-R\,\mathbf k\right) \quad &\text{(velocity field from $G$)} \\
> \boldsymbol\omega_{b0}\times\left(-R\,\mathbf k\right) &= \begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k \cr a_1 & a_2 & a_3 \cr 0 & 0 & -R \end{vmatrix} = -R\,a_2\,\mathbf i_2 + R\,a_1\,\mathbf j_2 \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{P(b)} &= \left(\dot d + R\,\dot\beta\right)\mathbf i_2 + \left(d\,\dot\theta + R\,\dot\varphi\cos\beta\right)\mathbf j_2 \quad &\text{(components $a_1$, $a_2$)} \\
> \dot d + R\,\dot\beta &= \dot d - \frac{R^2\,\dot d}{d^2 + R^2} = \frac{d^2}{d^2 + R^2}\,\dot d = \cos^2\beta\,\dot d = 0 \quad &\text{(component along $\mathbf i_2$ set to zero, Eq. 13.5)} \\
> d\,\dot\theta + R\,\dot\varphi\cos\beta &= 0 \quad &\text{(component along $\mathbf j_2$ set to zero)} \\
> \dot\varphi &= -\frac{d}{R\cos\beta}\,\dot\theta = -\frac{L\cos\beta}{L\sin\beta\cos\beta}\,\dot\theta \quad &\text{($d$ and $R$ from the triangle)}
> \end{aligned}$$
>
> $$\boxed{\dot d = 0, \qquad \dot\varphi = -\frac{\dot\theta}{\sin\beta}, \qquad \boldsymbol\omega_{b0} = -\frac{\dot\theta}{\tan\beta}\,\mathbf i_2 = -\frac dR\,\dot\theta\,\mathbf i_2, \qquad \boldsymbol\alpha_{b0} = -\frac dR\left(\ddot\theta\,\mathbf i_2 + \dot\theta^2\,\mathbf j_2\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** a rolling sphere cannot change its distance to $O$: moving radially would need a rotation about $\mathbf j_2$ larger than the one the rod allows, so $d$ and $\beta$ keep their initial values and $G$ moves on a circle of radius $d$. The third component of the angular velocity cancels and the angular velocity lies along $OP$: the instantaneous axis passes through $P$ and $O$, and the sphere rolls like a cone with its apex at $O$. The angular acceleration follows from part (b) with constant $\beta$.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and inertia tensor of the sphere
> **Law:** mass, centre of mass and moments of inertia as volume integrals in spherical coordinates (jacobian $r^2\sin\chi$); relation between the three axial moments and the polar integral
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 21]
>
> Spherical coordinates about $G$: distance $r$ from 0 to $R$, colatitude $\chi$ from 0 to $\pi$, longitude $\lambda$ from 0 to $2\pi$; volume element $r^2\sin\chi\,dr\,d\chi\,d\lambda$; density $\rho$. The small hole is neglected.
>
> $$\begin{aligned}
> V &= \int_0^{2\pi}d\lambda\int_0^{\pi}\sin\chi\,d\chi\int_0^R r^2\,dr = 2\pi\left[-\cos\chi\right]_0^{\pi}\left[\frac{r^3}{3}\right]_0^R \quad &\text{(separable integral; antiderivatives)} \\
> &= 2\pi\left(-\cos\pi + \cos 0\right)\left(\frac{R^3}{3} - 0\right) = \frac{4\pi R^3}{3} \quad &\text{(Barrow's rule)} \\
> \rho &= \frac{3M}{4\pi R^3}, \qquad \mathbf r_G^G = \mathbf 0 \quad &\text{(homogeneous; every plane through the centre is a plane of symmetry)} \\
> I_x + I_y + I_z &= 2\int r^2\,dm = 2\rho\cdot 2\pi\cdot 2\cdot\left[\frac{r^5}{5}\right]_0^R = \frac{8\pi\rho R^5}{5} \quad &\text{(Eq. 10.13; same angular factors; Barrow's rule)} \\
> &= \frac{8\pi R^5}{5}\cdot\frac{3M}{4\pi R^3} = \frac65\,MR^2 \quad &\text{(value of $\rho$)} \\
> I_x &= I_y = I_z = \frac25\,MR^2 \quad &\text{(the three axes are equivalent for a sphere)} \\
> \left[\frac{\sin^2\lambda}{2}\right]_0^{2\pi} &= 0, \quad \left[\sin\lambda\right]_0^{2\pi} = 0, \quad \left[-\cos\lambda\right]_0^{2\pi} = 0 \quad &\text{(longitude integrals of $\cos\lambda\sin\lambda$, $\cos\lambda$, $\sin\lambda$: products of inertia zero, Eq. 10.15)} \\
> [R]\left(\tfrac25 MR^2[U]\right)[R]^T &= \tfrac25 MR^2\,[U] \quad &\text{(any change of basis, Eq. 10.41)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac25\,MR^2\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in every basis}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the tensor is the same in $\mathcal B_2$, in the rod frame and in the body frame, so the angular momentum about $G$ is two fifths of $MR^2$ times the angular velocity.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf p_0 &= M\left(\dot d\,\mathbf i_2 + d\,\dot\theta\,\mathbf j_2\right) \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G,0} &= \frac25\,MR^2\left(\dot\varphi\cos\beta\,\mathbf i_2 - \dot\beta\,\mathbf j_2 + \left(\dot\theta + \dot\varphi\sin\beta\right)\mathbf k\right) \quad &\text{(Eq. 11.12; isotropic tensor)} \\
> \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 &= \frac25\,MR^2\,\boldsymbol\alpha_{b0} \quad &\text{(constant coefficient times the derivative of the angular velocity)} \\
> T_0 &= \frac12\,M\left(\dot d^2 + d^2\dot\theta^2\right) + \frac15\,MR^2\left(\dot\varphi^2\cos^2\beta + \dot\beta^2 + \left(\dot\theta + \dot\varphi\sin\beta\right)^2\right) \quad &\text{(Eq. 11.31)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G,0} = \frac25\,MR^2\,\boldsymbol\omega_{b0}, \qquad \left.\frac{d\mathbf H_{G,0}}{dt}\right|_0 = \frac25\,MR^2\,\boldsymbol\alpha_{b0}}$$
>
> **Units:** kg m$^2$/s; N m; J
> **Meaning:** with rolling (part (c)) the kinetic energy reduces to the seven fifths of $\tfrac12 M d^2$ times the squared rate of $\theta$, because the rotational part is two fifths of $MR^2$ times the square of $d/R$ times that rate, halved.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb22-exploded.svg]]

> [!derivation] Part (d): reactions on the rod
> **Law:** equilibrium of a massless body (force and moment equations with zero inertia); action and reaction between rod and sphere; ideal (frictionless) connections
> **Source:** Notes.pdf, Eq. 12.24; Notes.pdf, Eq. 12.25; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> The rod and the sphere act on each other at $G$ through a force $\mathbf F_r$ and a torque $\mathbf Q_r$ (on the sphere; minus these on the rod). The sphere slides along the rod and turns about it without friction, so neither has a component along $\mathbf u$. At $O$ the joint applies a force $\mathbf R_O$ (three components) and a torque that cannot act about the two axes of the joint, $\mathbf k$ and $\mathbf j_2$, so it is $Q_O\,\mathbf i_2$. Eight unknown components, six equations of equilibrium.
>
> $$\begin{aligned}
> \mathbf F_r &= F_j\,\mathbf j_2 + F_w\,\mathbf w, \qquad \mathbf Q_r = Q_j\,\mathbf j_2 + Q_w\,\mathbf w \quad &\text{(no components along the smooth rod)} \\
> \mathbf R_O - \mathbf F_r &= \mathbf 0 \quad &\text{(force equation of the massless rod, Eq. 12.24)} \\
> Q_O\,\mathbf i_2 + L\,\mathbf u\times\left(-\mathbf F_r\right) - \mathbf Q_r &= \mathbf 0 \quad &\text{(moments about $O$, Eq. 12.25; $G$ at $L\,\mathbf u$)} \\
> Q_O\,\mathbf i_2\cdot\mathbf u &= Q_O\cos\beta = 0 \quad &\text{(project on $\mathbf u$: the other two terms are normal to $\mathbf u$)} \\
> \mathbf u\times\mathbf F_r &= F_j\,\mathbf u\times\mathbf j_2 + F_w\,\mathbf u\times\mathbf w = F_j\,\mathbf w - F_w\,\mathbf j_2 \quad &\text{($\mathbf u\times\mathbf j_2 = \mathbf w$ and $\mathbf u\times\mathbf w = -\mathbf j_2$ in the right-handed rod triad)} \\
> \mathbf Q_r &= -L\left(F_j\,\mathbf w - F_w\,\mathbf j_2\right) = L\,F_w\,\mathbf j_2 - L\,F_j\,\mathbf w \quad &\text{(moment equation with $Q_O$ zero)}
> \end{aligned}$$
>
> $$\boxed{\mathbf R_O = \mathbf F_r = F_j\,\mathbf j_2 + F_w\,\mathbf w, \qquad Q_O = 0, \qquad \mathbf Q_r = L\,F_w\,\mathbf j_2 - L\,F_j\,\mathbf w, \qquad L = \sqrt{d^2 + R^2}}$$
>
> **Units:** N; N m ($L$ in m times a force)
> **Meaning:** all the reactions on the rod depend on the two force components $F_j$ and $F_w$. A massless rod is a two-force member only when it carries no torque; here it transmits the torque that the sphere needs, balanced by the moment of the force pair at $O$ and $G$. The joint torque is zero, so the result is the same if the joint at $O$ is read as a ball-and-socket joint.

| Force on the sphere | Point of application | Expression in $\mathcal B_2$ | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $Mg\sin\gamma(\cos\theta\,\mathbf i_2 - \sin\theta\,\mathbf j_2) - Mg\cos\gamma\,\mathbf k$ | applied |
| Rod force | $G$ | $F_j\,\mathbf j_2 + F_w(-\sin\beta\,\mathbf i_2 + \cos\beta\,\mathbf k)$ | constraint |
| Rod torque | - | $L F_w\,\mathbf j_2 - L F_j(-\sin\beta\,\mathbf i_2 + \cos\beta\,\mathbf k)$ | constraint |
| Normal reaction | $P$ | $N\,\mathbf k$ | constraint |
| Friction | $P$ | $T_1\,\mathbf i_2 + T_2\,\mathbf j_2$ (unknown with no slip; zero on a smooth plane) | constraint |

> [!derivation] Part (e): resultant force and moment about G on the sphere
> **Law:** sum of forces; moments about $G$ by a determinant; the torque of the rod added as a couple
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \mathbf F &= \left(Mg\sin\gamma\cos\theta - F_w\sin\beta + T_1\right)\mathbf i_2 + \left(-Mg\sin\gamma\sin\theta + F_j + T_2\right)\mathbf j_2 + \left(-Mg\cos\gamma + F_w\cos\beta + N\right)\mathbf k \quad &\text{(sum by components)} \\
> \left(-R\,\mathbf k\right)\times\left(T_1\,\mathbf i_2 + T_2\,\mathbf j_2 + N\,\mathbf k\right) &= \begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k \cr 0 & 0 & -R \cr T_1 & T_2 & N \end{vmatrix} = R\,T_2\,\mathbf i_2 - R\,T_1\,\mathbf j_2 \quad &\text{(moment of the contact force; expand along the first row)} \\
> \mathbf Q_r &= L F_j\sin\beta\,\mathbf i_2 + L F_w\,\mathbf j_2 - L F_j\cos\beta\,\mathbf k = R\,F_j\,\mathbf i_2 + L\,F_w\,\mathbf j_2 - d\,F_j\,\mathbf k \quad &\text{($\mathbf w$ in $\mathcal B_2$; $L\sin\beta = R$, $L\cos\beta = d$)} \\
> \mathbf M_G &= \mathbf Q_r + R\,T_2\,\mathbf i_2 - R\,T_1\,\mathbf j_2 \quad &\text{(weight and rod force act at $G$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_G = R\left(F_j + T_2\right)\mathbf i_2 + \left(L\,F_w - R\,T_1\right)\mathbf j_2 - d\,F_j\,\mathbf k}$$
>
> **Units:** N; N m
> **Meaning:** five unknown reaction components act on the sphere: $F_j$, $F_w$ (the rod), $N$, $T_1$, $T_2$ (the plane).

> [!derivation] Part (f): six equations for rolling without slip
> **Law:** Newton's second law for the centre of mass; moment equation about $G$
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> With rolling, $d$ and $\beta$ are constant (part (c)), so the acceleration of $G$ is minus $d$ times the squared rate of $\theta$ along $\mathbf i_2$ plus $d$ times its second rate along $\mathbf j_2$, and the angular acceleration is the one boxed in part (c). The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole.
>
> $$\begin{aligned}
> -M\,d\,\dot\theta^2 &= Mg\sin\gamma\cos\theta - F_w\sin\beta + T_1 \quad &\text{(force along $\mathbf i_2$)} \\
> M\,d\,\ddot\theta &= -Mg\sin\gamma\sin\theta + F_j + T_2 \quad &\text{(force along $\mathbf j_2$)} \\
> 0 &= -Mg\cos\gamma + F_w\cos\beta + N \quad &\text{(force along $\mathbf k$)} \\
> -\frac25\,MRd\,\ddot\theta &= R\left(F_j + T_2\right) \quad &\text{(moment along $\mathbf i_2$; $\tfrac25 MR^2$ times $-\tfrac dR\ddot\theta$)} \\
> -\frac25\,MRd\,\dot\theta^2 &= L\,F_w - R\,T_1 \quad &\text{(moment along $\mathbf j_2$)} \\
> 0 &= -d\,F_j \quad &\text{(moment along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\text{six equations for } \theta, F_j, F_w, N, T_1, T_2 \text{ (above)}, \qquad F_j = 0}$$
>
> **Units:** N for the forces; N m for the moments
> **Meaning:** the last equation already says that the rod pushes on the sphere only along $\mathbf w$, in the vertical plane of the rod.

> [!derivation] Reduction to one equation and the reactions along the motion
> **Law:** elimination of the reactions between the six equations
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> T_2 &= -\frac25\,M\,d\,\ddot\theta \quad &\text{(moment along $\mathbf i_2$ with $F_j$ zero, divided by $R$)} \\
> M\,d\,\ddot\theta + \frac25\,M\,d\,\ddot\theta &= -Mg\sin\gamma\sin\theta \quad &\text{(force along $\mathbf j_2$)} \\
> \ddot\theta + \frac{5\,g\sin\gamma}{7\,d}\,\sin\theta &= 0 \quad &\text{(divide by $\tfrac75 Md$)} \\
> T_1 &= F_w\sin\beta - Mg\sin\gamma\cos\theta - M\,d\,\dot\theta^2 \quad &\text{(force along $\mathbf i_2$)} \\
> L\,F_w - R\,F_w\sin\beta &= -R\left(Mg\sin\gamma\cos\theta + M\,d\,\dot\theta^2\right) - \frac25\,MRd\,\dot\theta^2 \quad &\text{(substitute in the moment along $\mathbf j_2$)} \\
> L - R\sin\beta &= L\left(1 - \sin^2\beta\right) = L\cos^2\beta = d\cos\beta \quad &\text{($R = L\sin\beta$; $d = L\cos\beta$)} \\
> F_w &= -\frac{R}{d\cos\beta}\,M\left(g\sin\gamma\cos\theta + \frac75\,d\,\dot\theta^2\right) = -\frac{M\tan\beta}{\cos\beta}\left(g\sin\gamma\cos\theta + \frac75\,d\,\dot\theta^2\right) \quad &\text{(divide; $R/d = \tan\beta$)} \\
> N &= Mg\cos\gamma - F_w\cos\beta = Mg\cos\gamma + M\tan\beta\left(g\sin\gamma\cos\theta + \frac75\,d\,\dot\theta^2\right) \quad &\text{(force along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \frac{5\,g\sin\gamma}{7\,d}\sin\theta = 0, \quad F_j = 0, \quad T_2 = \frac27\,Mg\sin\gamma\sin\theta, \quad F_w = -\frac{M\tan\beta}{\cos\beta}\left(g\sin\gamma\cos\theta + \frac75 d\dot\theta^2\right), \quad N = Mg\cos\gamma - F_w\cos\beta}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ for the coefficient of the sine ($[\mathrm{L\,T^{-2}}]/[\mathrm L]$); N for the reactions
> **Meaning:** the sphere is a pendulum about the line of maximum slope through $O$: the downhill pull, with the arm given by the sine of $\theta$, brings $OP$ back to $\theta$ zero, and the rolling adds two fifths to the inertia. $T_2$ follows from the first line with the second rate of $\theta$ from the third; $T_1$ is then the force along $\mathbf i_2$ with this $F_w$. Whenever the bracket is positive (near the equilibrium, for instance) $F_w$ is negative, along minus $\mathbf w$: the rod presses the sphere against the plane, which is why $N$ then exceeds the normal part of the weight.

> [!derivation] Part (g): reactions in the equilibrium at theta equal to zero
> **Law:** the previous box at rest with $\theta$ zero
> **Source:** Notes.pdf, Eq. 12.24; Notes.pdf, Eq. 12.25
>
> $$\begin{aligned}
> \ddot\theta &= -\frac{5\,g\sin\gamma}{7\,d}\sin 0 = 0 \quad &\text{(rest at $\theta$ zero is an equilibrium)} \\
> F_w &= -\frac{Mg\sin\gamma\tan\beta}{\cos\beta} = -\frac{Mg\sin\gamma\sin\beta}{\cos^2\beta}, \qquad F_j = 0 \quad &\text{(zero rate, cosine of $\theta$ equal to 1)} \\
> \mathbf F_r &= F_w\left(-\sin\beta\,\mathbf i_2 + \cos\beta\,\mathbf k\right) = Mg\sin\gamma\tan^2\beta\,\mathbf i_2 - Mg\sin\gamma\tan\beta\,\mathbf k \quad &\text{(rod force in $\mathcal B_2$)} \\
> \mathbf Q_r &= L\,F_w\,\mathbf j_2 = -\frac{MgR\sin\gamma}{\cos^2\beta}\,\mathbf j_2 \quad &\text{(part (d); $L\sin\beta = R$)} \\
> N &= Mg\cos\gamma + Mg\sin\gamma\tan\beta \quad &\text{(previous box)} \\
> T_1 &= F_w\sin\beta - Mg\sin\gamma = -Mg\sin\gamma\left(\tan^2\beta + 1\right) = -\frac{Mg\sin\gamma}{\cos^2\beta}, \qquad T_2 = 0 \quad &\text{(force along $\mathbf i_2$; $1 + \tan^2\beta = 1/\cos^2\beta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_r = Mg\sin\gamma\tan\beta\left(\tan\beta\,\mathbf i - \mathbf k\right), \quad \mathbf Q_r = -\frac{MgR\sin\gamma}{\cos^2\beta}\,\mathbf j, \quad N = Mg\left(\cos\gamma + \sin\gamma\tan\beta\right), \quad \mathbf T = -\frac{Mg\sin\gamma}{\cos^2\beta}\,\mathbf i}$$
>
> **Units:** N; N m
> **Meaning:** at $\theta$ zero the basis $\mathcal B_2$ coincides with $\mathcal B_0$. The sphere hangs below $O$ on the line of maximum slope: friction holds it up the slope with more than the downhill weight component, the rod pushes it down the slope and into the plane, and the torque of the rod balances the moment of the friction about $G$. Check of the moment along $\mathbf j_2$: $L F_w$ minus $R T_1$ is $MgR\sin\gamma$ over the square of the cosine of $\beta$ times minus one plus one, zero.

> [!derivation] Part (h): small oscillations about the equilibrium
> **Law:** first-order expansion of the sine; harmonic oscillator and its initial conditions
> **Source:** Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.8; Notes.pdf, Eq. 5.9
>
> $$\begin{aligned}
> \sin\theta &= \theta + O\left(\theta^3\right) \quad &\text{(Taylor expansion about zero)} \\
> \ddot\theta + \Omega^2\,\theta &= 0, \qquad \Omega^2 = \frac{5\,g\sin\gamma}{7\,d} = \frac{5\,g\sin\gamma\tan\beta}{7\,R} \quad &\text{(linearised equation, Eq. 5.6; $d = R/\tan\beta$)} \\
> \theta(t) &= C_1\cos\Omega t + C_2\sin\Omega t, \qquad C_1 = \theta_0, \quad C_2 = \frac{\dot\theta_0}{\Omega} = 0 \quad &\text{(Eqs. 5.7 to 5.9; released from rest)} \\
> \ddot\theta &= -\Omega^2\,\theta_0\cos\Omega t \quad &\text{(chain rule twice: the solution satisfies the equation)}
> \end{aligned}$$
>
> $$\boxed{\theta(t) = \theta_0\cos\Omega t, \qquad \Omega = \sqrt{\frac{5\,g\sin\gamma}{7\,d}} = \sqrt{\frac{5\,g\sin\gamma\tan\beta}{7\,R}}}$$
>
> **Units:** $\Omega$ in $\sqrt{[\mathrm{L\,T^{-2}}]/[\mathrm L]} = [\mathrm{T^{-1}}]$
> **Meaning:** the sphere swings about the line of maximum slope like a pendulum of length $d$ in the reduced gravity $g\sin\gamma$, slowed by the factor square root of five sevenths that rolling brings; a flatter plane or a longer rod gives slower oscillations.

#### Parts (i) and (j): frictionless inclined plane

> [!derivation] Part (i): equations on the smooth plane
> **Law:** the equations of part (f) with zero friction and without the rolling conditions; projection of the moment equation on the rod
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.2
>
> Without friction $T_1$ and $T_2$ vanish, the contact point may slide and $d$ and $\varphi$ are free again: three coordinates and three reaction components ($F_j$, $F_w$, $N$). Write $I$ for two fifths of $MR^2$, and the components of the angular acceleration as in part (b).
>
> $$\begin{aligned}
> M\left(\ddot d - d\,\dot\theta^2\right) &= Mg\sin\gamma\cos\theta - F_w\sin\beta \quad &\text{(force along $\mathbf i_2$)} \\
> M\left(d\,\ddot\theta + 2\,\dot d\,\dot\theta\right) &= -Mg\sin\gamma\sin\theta + F_j \quad &\text{(force along $\mathbf j_2$)} \\
> N &= Mg\cos\gamma - F_w\cos\beta \quad &\text{(force along $\mathbf k$; height of $G$ constant)} \\
> I\left(\ddot\varphi\cos\beta - \dot\varphi\dot\beta\sin\beta + \dot\theta\dot\beta\right) &= R\,F_j \quad &\text{(moment along $\mathbf i_2$)} \\
> I\left(-\ddot\beta + \dot\theta\dot\varphi\cos\beta\right) &= L\,F_w \quad &\text{(moment along $\mathbf j_2$)} \\
> I\left(\ddot\theta + \ddot\varphi\sin\beta + \dot\varphi\dot\beta\cos\beta\right) &= -d\,F_j \quad &\text{(moment along $\mathbf k$)} \\
> \mathbf M_G\cdot\mathbf u &= R\,F_j\cos\beta - d\,F_j\sin\beta = F_j L\left(\sin\beta\cos\beta - \cos\beta\sin\beta\right) = 0 \quad &\text{(moment about the rod)} \\
> \frac{d}{dt}\left(\boldsymbol\omega_{b0}\cdot\mathbf u\right) &= \boldsymbol\alpha_{b0}\cdot\mathbf u + \boldsymbol\omega_{b0}\cdot\left(\boldsymbol\omega_{30}\times\mathbf u\right) = \frac{\mathbf M_G\cdot\mathbf u}{I} + 0 \quad &\text{(product rule; Poisson for $\mathbf u$; $\boldsymbol\omega_{b0}$ minus $\boldsymbol\omega_{30}$ is parallel to $\mathbf u$)} \\
> \boldsymbol\omega_{b0}\cdot\mathbf u &= \dot\varphi\cos^2\beta + \left(\dot\theta + \dot\varphi\sin\beta\right)\sin\beta = \dot\varphi + \dot\theta\sin\beta \quad &\text{(components in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\text{the six equations above for } \theta, d, \varphi, F_j, F_w, N, \text{ with } \sin\beta = \frac{R}{L}, \ \cos\beta = \frac dL, \ \dot\beta = -\frac{R\dot d}{L^2}; \qquad \dot\varphi + \dot\theta\sin\beta = C}$$
>
> **Units:** N; N m; $[\mathrm{T^{-1}}]$ for the constant $C$
> **Meaning:** the spin of the sphere about the moving rod is conserved for two reasons together: the reactions have no moment about the rod (the rod exerts no torque along itself and the other forces act at $G$ or along the normal through $G$), and the gyroscopic term vanishes because the tensor is isotropic and the sphere differs from the rod frame only by a rotation about the rod. The force along $\mathbf j_2$ gives $F_j$, the moment along $\mathbf j_2$ gives $F_w$, and three second-order equations remain for $\theta$, $d$ and $\varphi$. The contact must be checked: $N$ must stay positive.

> [!derivation] Part (j): initial conditions
> **Law:** polar coordinates of the contact point; components of the velocity of $G$ in $\mathcal B_2$
> **Source:** Notes.pdf, Eq. 9.3; Problems.pdf, p. 52
>
> $$\begin{aligned}
> \overrightarrow{OP_0} &= 2R\,\mathbf i + 3R\,\mathbf j \quad &\text{(the contact is below $G$)} \\
> d_0 &= \sqrt{4R^2 + 9R^2} = \sqrt{13}\,R, \qquad \cos\theta_0 = \frac{2}{\sqrt{13}}, \quad \sin\theta_0 = \frac{3}{\sqrt{13}} \quad &\text{(right triangle with legs $2R$, $3R$)} \\
> \theta_0 &= \arctan\frac32, \qquad \tan\beta_0 = \frac{R}{d_0} = \frac{1}{\sqrt{13}}, \qquad \sin\beta_0 = \frac{1}{\sqrt{14}} \quad &\text{(hypotenuse $\sqrt{d_0^2 + R^2} = \sqrt{14}\,R$)} \\
> \dot d_0 &= \mathbf v_{G0}\cdot\mathbf i_2 = -\sqrt{Rg}\left(\cos\theta_0 + \sin\theta_0\right) = -\frac{5\sqrt{Rg}}{\sqrt{13}} \quad &\text{(component along $\mathbf i_2$)} \\
> d_0\,\dot\theta_0 &= \mathbf v_{G0}\cdot\mathbf j_2 = -\sqrt{Rg}\left(-\sin\theta_0 + \cos\theta_0\right) = \frac{\sqrt{Rg}}{\sqrt{13}} \quad &\text{(component along $\mathbf j_2$)} \\
> \dot\theta_0 &= \frac{\sqrt{Rg}}{\sqrt{13}\cdot\sqrt{13}\,R} = \frac{1}{13}\sqrt{\frac gR} \quad &\text{(divide by $d_0$)} \\
> \dot\varphi_0 &= C - \dot\theta_0\sin\beta_0 \quad &\text{(spin integral of part (i))}
> \end{aligned}$$
>
> $$\boxed{\theta_0 = \arctan\tfrac32, \quad d_0 = \sqrt{13}\,R, \quad \dot\theta_0 = \frac{1}{13}\sqrt{\frac gR}, \quad \dot d_0 = -5\sqrt{\frac{Rg}{13}}, \quad \varphi_0 = 0, \quad \dot\varphi_0 = C - \frac{1}{13\sqrt{14}}\sqrt{\frac gR}}$$
>
> **Units:** rad; m; rad/s; m/s
> **Meaning:** the sphere starts at about 56.3 deg from the line of maximum slope, with the rod at about 15.5 deg above the plane, moving towards $O$ (negative rate of $d$) while $OP$ turns slowly counterclockwise. The data fix the motion of $G$ but not the spin about the rod: $\varphi_0$ is zero by the choice of the reference, and the constant $C$ (the initial spin about the rod) is an extra datum; for a sphere launched with no angular velocity about the rod, $C$ is zero.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Coordinates | $\theta$, $d$, $\varphi$ (three); $\beta = \arctan(R/d)$ |
| (b) Kinematics | $\boldsymbol\omega = \dot\varphi\cos\beta\,\mathbf i_2 - \dot\beta\,\mathbf j_2 + (\dot\theta + \dot\varphi\sin\beta)\,\mathbf k$; $\boldsymbol\alpha = (\ddot\varphi\cos\beta - \dot\varphi\dot\beta\sin\beta + \dot\theta\dot\beta)\,\mathbf i_2 + (-\ddot\beta + \dot\theta\dot\varphi\cos\beta)\,\mathbf j_2 + (\ddot\theta + \ddot\varphi\sin\beta + \dot\varphi\dot\beta\cos\beta)\,\mathbf k$; $\mathbf v_G = \dot d\,\mathbf i_2 + d\dot\theta\,\mathbf j_2$; $\mathbf a_G = (\ddot d - d\dot\theta^2)\,\mathbf i_2 + (d\ddot\theta + 2\dot d\dot\theta)\,\mathbf j_2$; $\dot\beta = -R\dot d/(d^2 + R^2)$ |
| (c) Rolling | $\mathbf v_P = \mathbf v_G - R\,\boldsymbol\omega\times\mathbf k$; $\dot d = 0$, $\dot\varphi = -\dot\theta/\sin\beta$ |
| (d) Rod | $\mathbf R_O = \mathbf F_r = F_j\,\mathbf j_2 + F_w\,\mathbf w$, joint torque zero, $\mathbf Q_r = LF_w\,\mathbf j_2 - LF_j\,\mathbf w$ |
| (e) Sphere | force and moment of the part (e) box, with $F_j$, $F_w$, $N$, $T_1$, $T_2$ |
| (f) Six equations | box of part (f) |
| (g) Equilibrium | $\mathbf F_r = Mg\sin\gamma\tan\beta(\tan\beta\,\mathbf i - \mathbf k)$, $\mathbf Q_r = -MgR\sin\gamma\,\mathbf j/\cos^2\beta$; $N = Mg(\cos\gamma + \sin\gamma\tan\beta)$; friction $-Mg\sin\gamma\,\mathbf i/\cos^2\beta$ |
| (h) Small oscillations | $\theta = \theta_0\cos\Omega t$, $\Omega = \sqrt{5g\sin\gamma/(7d)} = \sqrt{5g\sin\gamma\tan\beta/(7R)}$ |
| (i) Smooth plane | $T_1 = T_2 = 0$; $d$ and $\varphi$ free; six equations of the part (i) box; $\dot\varphi + \dot\theta\sin\beta$ constant |
| (j) Initial conditions | $\theta_0 = \arctan(3/2)$, $d_0 = \sqrt{13}R$, $\dot\theta_0 = \sqrt{g/R}/13$, $\dot d_0 = -5\sqrt{Rg/13}$, $\varphi_0 = 0$; the spin about the rod is an extra datum |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: energy of the rolling sphere
> **Law:** conservation of the mechanical energy (contact point at rest, ideal smooth rod); potential of the weight; chain rule
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 12.31
>
> $$\begin{aligned}
> T_0 &= \frac12\,M\,d^2\dot\theta^2 + \frac12\cdot\frac25\,MR^2\,\frac{d^2}{R^2}\,\dot\theta^2 = \frac{7}{10}\,M\,d^2\dot\theta^2 \quad &\text{(Koenig with the angular velocity of part (c))} \\
> V_0 &= M g\,\mathbf r_0^G\cdot\mathbf K = Mg\left(-d\cos\theta\sin\gamma + R\cos\gamma\right) \quad &\text{($\mathbf K$ in $\mathcal B_0$; $\mathbf i_2\cdot\mathbf i$ is the cosine of $\theta$)} \\
> \frac{d}{dt}\left(T_0 + V_0\right) &= \frac75\,M\,d^2\dot\theta\ddot\theta + Mg\,d\sin\gamma\sin\theta\,\dot\theta = \frac75\,M\,d^2\dot\theta\left(\ddot\theta + \frac{5\,g\sin\gamma}{7\,d}\sin\theta\right) \quad &\text{(chain rule; $d$ constant)}
> \end{aligned}$$
>
> $$\boxed{\frac{7}{10}\,M\,d^2\dot\theta^2 - Mg\,d\sin\gamma\cos\theta = E_0 - MgR\cos\gamma}$$
>
> **Units:** J in every term
> **Meaning:** the derivative vanishes exactly by the equation of motion of the reduced box: the energy integral is its first integral. The frictionless equations of part (i) were also compared symbolically with the equations obtained from the kinetic energy of the momentum section and this potential with the three coordinates; after eliminating $F_j$ and $F_w$ they coincide.

**Limiting cases and consistency:**

* **Horizontal plane.** With zero inclination the coefficient of the sine vanishes: any $\theta$ is an equilibrium and the sphere rolls around $O$ at a constant rate. The centripetal force comes from the friction and the rod, and the rod presses the sphere against the plane, so the normal reaction exceeds the weight by a term proportional to the squared rate of $\theta$.
* **Very long rod.** For $d$ much larger than $R$, $\beta$ tends to zero: in equilibrium the rod force vanishes, the friction tends to the downhill weight component, and the torque of the rod tends to $MgR\sin\gamma$, which balances the moment of that friction about $G$; the frequency tends to zero, as for a very long pendulum.
* **Sign check.** For small positive $\theta$ the second rate of $\theta$ is negative: the sphere returns towards the line of maximum slope below $O$, which is the stable side.
* **Dimensions.** The squared frequency is an acceleration over a length; every reaction is a multiple of $Mg$.

---
