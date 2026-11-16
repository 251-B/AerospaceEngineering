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
> \frac{d}{dt}\left(C_1\cos\Omega t + C_2\sin\Omega t\right) &= -C_1\Omega\sin\Omega t + C_2\Omega\cos\Omega t \quad &\text{(chain rule: $d(\Omega t)/dt = \Omega$)} \\
> \frac{d^2}{dt^2}\left(C_1\cos\Omega t + C_2\sin\Omega t\right) &= -\Omega^2\left(C_1\cos\Omega t + C_2\sin\Omega t\right) \quad &\text{(chain rule again; it satisfies the equation)} \\
> C_1 &= x_0 - x_E \quad &\text{(the position at $t = 0$, where $\cos 0 = 1$ and $\sin 0 = 0$)} \\
> \dot x_0 &= C_2\,\Omega \;\Rightarrow\; C_2 = \frac{\dot x_0}{\Omega} \quad &\text{(the first derivative at $t = 0$, Eqs. 5.8 and 5.9)} \\
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
> **Meaning:** the vertical component of the spring vector is never negative: $A$ is never above the height $2a$ of $C$, so the vertical component of the spring force is never downward; it vanishes when $A$ is at the top. The contact velocity has no vertical component (no penetration); on a smooth plane its horizontal components are free.

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
> **Meaning:** the friction becomes two more unknowns, balanced by the two rolling conditions. It enters the two force equations and all three moment equations; in particular the spin about $GA$ is no longer conserved, because the friction has the moment $aF_2\sin\theta$ about $GA$ whenever that axis is tilted. The normal reaction keeps the same expression. The friction can be eliminated with the force equations, $F_x$ equal to $M$ times the second rate of $\xi$ plus the spring term, and three second-order moment equations remain, which together with the two first-order rolling relations give five equations for the five coordinates.

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
> \theta(t) &= C_1\cos\Omega t + C_2\sin\Omega t, \qquad C_1 = \theta_0, \quad C_2 = \frac{\dot\theta_0}{\Omega} = 0 \quad &\text{(Eqs. 5.7 to 5.9; released from rest, so $\dot\theta(0) = C_2\Omega = 0$)} \\
> \dot\theta &= -\Omega\,\theta_0\sin\Omega t \quad &\text{(chain rule: $d(\Omega t)/dt = \Omega$)} \\
> \ddot\theta &= -\Omega^2\,\theta_0\cos\Omega t \quad &\text{(chain rule again: the solution satisfies the equation)}
> \end{aligned}$$
>
> $$\boxed{\theta(t) = \theta_0\cos\Omega t, \qquad \Omega = \sqrt{\frac{5\,g\sin\gamma}{7\,d}} = \sqrt{\frac{5\,g\sin\gamma\tan\beta}{7\,R}}}$$
>
> **Units:** $\Omega$ in $\sqrt{[\mathrm{L\,T^{-2}}]/[\mathrm L]} = [\mathrm{T^{-1}}]$
> **Meaning:** the sphere swings about the line of maximum slope like a pendulum of length $d$ in the reduced gravity $g\sin\gamma$, slowed by the factor square root of five sevenths that rolling brings; a sphere farther from $O$ (larger $d$) gives slower oscillations.

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
* **Large distance $d$.** For $d$ much larger than $R$, $\beta$ tends to zero: in equilibrium the rod force vanishes, the friction tends to the downhill weight component, and the torque of the rod tends to $MgR\sin\gamma$, which balances the moment of that friction about $G$; the frequency tends to zero, as for a very long pendulum.
* **Sign check.** For small positive $\theta$ the second rate of $\theta$ is negative: the sphere returns towards the line of maximum slope below $O$, which is the stable side.
* **Dimensions.** The squared frequency is an acceleration over a length; every reaction is a multiple of $Mg$.

---

## Problem RB-23: Rectangle with a hole on knob

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous rectangular plate $b$ of mass $m$, sides $h$ (along its longitudinal symmetry axis) and $w$, with a circular hole of radius $a_2$ centred at the centre of the rectangle. The hole hangs on a fixed cylindrical knob of radius $a_1$ and centre $O$; the inner surface of the hole touches the knob at the single point $I$ and rolls on it without slipping. Gravity acts downwards. The motion is planar, in the plane of the figure.
* **Fixed frame:** $S_1\{O; \mathbf i_1, \mathbf j_1, \mathbf k_1\}$, the frame $Ox_1y_1z_1$ of the statement: $\mathbf i_1$ horizontal to the right, $\mathbf j_1$ vertical upwards and $\mathbf k_1$ out of the paper (⊙). The knob is at rest, so this frame is inertial.
* **Body frame:** $S_B\{G; \mathbf i_B, \mathbf j_B, \mathbf k_1\}$, with $\mathbf j_B$ along the longitudinal axis $y_B$ (the side $h$) and $\mathbf i_B$ along the short axis $x_B$ (the side $w$), turned by $\theta$ with respect to $S_1$. Read from the figure: $\mathbf j_B$ points up and to the left when $\theta$ is positive, so $\theta$ is counterclockwise about $\mathbf k_1$.
* **Contact basis:** $\mathcal B_c\{\mathbf u_1, \mathbf u_2, \mathbf k_1\}$, with $\mathbf u_2$ along $OI$, turned by $\phi$ with respect to $\mathcal B_1$. Read from the figure: $I$ lies up and to the left of $O$ when $\phi$ is positive, so $\phi$ is also counterclockwise about $\mathbf k_1$.
* **Degrees of freedom:** a plate moving in its plane has three coordinates (two for $G$ and the angle $\theta$). Contact with the knob (Notes.pdf, Eq. 13.1) fixes the distance from $O$ to $G$: two coordinates remain, $\phi$ and $\theta$. Rolling without slip adds one relation between their rates (part (c)), which can be integrated: the plate has **one degree of freedom**.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the plate (with the hole), homogeneous | $m$ | kg |
| Width along $x_B$ | $w$ | m |
| Length along $y_B$ | $h = 2w$ | m |
| Radius of the hole | $a_2 = w/\sqrt{2\pi}$ | m |
| Radius of the knob | $a_1 = a_2/3$ | m |
| Angle of the axis $y_B$ with the vertical | $\theta$, counterclockwise | rad |
| Angle of $OI$ with the vertical | $\phi$, counterclockwise | rad |
| Gravity | $g$, along $-\mathbf j_1$ | m/s$^2$ |
| Initial state, part (f) | $\theta_0 = 0$, $G$ below $O$, speed of $G$ equal to $2wA/3$ [sic], counterclockwise rotation | rad, m/s |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb23-rot-theta.svg]]

> [!derivation] Body basis: rotation by theta about k1
> **Law:** simple rotation about the third axis, positive by the right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View of the plane of the plate with $\mathbf k_1$ out of the paper (⊙), $\mathbf i_1$ to the right and $\mathbf j_1$ up; a positive $\theta$ turns counterclockwise. Triangle of $\mathbf i_B$: hypotenuse 1, adjacent leg along $\mathbf i_1$ (cosine of $\theta$), opposite leg along $\mathbf j_1$ (sine). Triangle of $\mathbf j_B$: hypotenuse 1, adjacent leg along $\mathbf j_1$ (cosine), opposite leg along minus $\mathbf i_1$ (sine), because the counterclockwise turn carries the tip of $\mathbf j_1$ to the left.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \qquad \mathbf j_B = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_B] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k_1$ in $\mathcal B_1$)} \\
> \det[{}_1R_B] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_1R_B][{}_1R_B]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{B0} &= \dot\theta\,\mathbf k_1, \qquad \boldsymbol\alpha_{B0} = \ddot\theta\,\mathbf k_1 \quad &\text{(rotation about the fixed axis $\mathbf k_1$; $\mathbf k_1$ constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_B = \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1, \qquad \mathbf j_B = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1, \qquad \boldsymbol\omega_{B0} = \dot\theta\,\mathbf k_1, \qquad \boldsymbol\alpha_{B0} = \ddot\theta\,\mathbf k_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the plate is a plane body, so its angular velocity is always normal to the plane; $\theta$ is the angle that the plate itself has turned.

![[attachments/EM-SOL/rb23-contact.svg]]

> [!derivation] Contact basis: rotation by phi about k1
> **Law:** simple rotation about the third axis; Poisson's formula for a basis turning at the rate of $\phi$
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2
>
> Same view, $\mathbf k_1$ out of the paper (⊙). The unit vector $\mathbf u_2$ is $\mathbf j_1$ turned counterclockwise by $\phi$: hypotenuse 1, adjacent leg along $\mathbf j_1$ (cosine of $\phi$), opposite leg along minus $\mathbf i_1$ (sine). The unit vector $\mathbf u_1$ is $\mathbf i_1$ turned by $\phi$: adjacent leg along $\mathbf i_1$ (cosine), opposite leg along $\mathbf j_1$ (sine). The basis is not attached to the plate: it follows the contact point.
>
> $$\begin{aligned}
> \mathbf u_1 &= \cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1, \qquad \mathbf u_2 = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_c] &= \begin{bmatrix} \cos\phi & -\sin\phi & 0 \cr \sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf u_1$, $\mathbf u_2$, $\mathbf k_1$ in $\mathcal B_1$)} \\
> \det[{}_1R_c] &= 1\cdot\left(\cos^2\phi + \sin^2\phi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_1R_c][{}_1R_c]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & \cos\phi\sin\phi - \sin\phi\cos\phi & 0 \cr \sin\phi\cos\phi - \cos\phi\sin\phi & \sin^2\phi + \cos^2\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_1 &= \sin\phi\,\mathbf u_1 + \cos\phi\,\mathbf u_2 \quad &\text{(second row: the inverse is the transpose)} \\
> \dot{\mathbf u}_1 &= \dot\phi\,\mathbf k_1\times\mathbf u_1 = \dot\phi\,\mathbf u_2, \qquad \dot{\mathbf u}_2 = \dot\phi\,\mathbf k_1\times\mathbf u_2 = -\dot\phi\,\mathbf u_1 \quad &\text{(Poisson; $\mathbf k_1\times\mathbf u_1 = \mathbf u_2$, $\mathbf k_1\times\mathbf u_2 = -\mathbf u_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf u_1 = \cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1, \qquad \mathbf u_2 = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1, \qquad \dot{\mathbf u}_1 = \dot\phi\,\mathbf u_2, \qquad \dot{\mathbf u}_2 = -\dot\phi\,\mathbf u_1}$$
>
> **Units:** dimensionless; the derivatives in $[\mathrm{T^{-1}}]$
> **Meaning:** $\mathbf u_2$ is the common normal of the knob and the hole at $I$; $\mathbf u_1$ is their common tangent.

> [!derivation] Part (b): position, velocity and acceleration of G
> **Law:** internal tangency of two circles (the centres and the contact point are aligned); derivative of a vector written in a moving basis; product rule
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> The knob touches the inside of the hole at $I$, so the centre $O$ of the knob, the centre $G$ of the hole and $I$ lie on the common normal $\mathbf u_2$; $I$ is at $a_1$ from $O$ and at $a_2$ from $G$, on the same side, so $G$ is at $a_2 - a_1$ from $O$ on the side opposite to $I$.
>
> $$\begin{aligned}
> \mathbf r_1^I &= a_1\,\mathbf u_2, \qquad \mathbf r_1^G = \mathbf r_1^I - a_2\,\mathbf u_2 = -\left(a_2 - a_1\right)\mathbf u_2 \quad &\text{(sum of segments along the common normal)} \\
> \mathbf v_1^G &= -\left(a_2 - a_1\right)\dot{\mathbf u}_2 = \left(a_2 - a_1\right)\dot\phi\,\mathbf u_1 \quad &\text{($a_2 - a_1$ constant; Poisson)} \\
> \mathbf a_1^G &= \left(a_2 - a_1\right)\left(\ddot\phi\,\mathbf u_1 + \dot\phi\,\dot{\mathbf u}_1\right) = \left(a_2 - a_1\right)\left(\ddot\phi\,\mathbf u_1 + \dot\phi^2\,\mathbf u_2\right) \quad &\text{(product rule; Poisson)} \\
> a_2 - a_1 &= a_2 - \frac{a_2}{3} = \frac23\,a_2 = \frac{2w}{3\sqrt{2\pi}} \quad &\text{(data)} \\
> \mathbf v_1^G &= \left(a_2 - a_1\right)\dot\phi\left(\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1\right) \quad &\text{($\mathbf u_1$ in $\mathcal B_1$)} \\
> \mathbf a_1^G &= \left(a_2 - a_1\right)\left[\left(\ddot\phi\cos\phi - \dot\phi^2\sin\phi\right)\mathbf i_1 + \left(\ddot\phi\sin\phi + \dot\phi^2\cos\phi\right)\mathbf j_1\right] \quad &\text{($\mathbf u_1$ and $\mathbf u_2$ in $\mathcal B_1$; collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_1^G = -\frac{2w}{3\sqrt{2\pi}}\,\mathbf u_2, \qquad \mathbf v_1^G = \frac{2w}{3\sqrt{2\pi}}\,\dot\phi\,\mathbf u_1, \qquad \mathbf a_1^G = \frac{2w}{3\sqrt{2\pi}}\left(\ddot\phi\,\mathbf u_1 + \dot\phi^2\,\mathbf u_2\right)}$$
>
> **Units:** $[\mathrm L]$, $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $G$ moves on a circle of radius $a_2 - a_1$ about $O$, about 0.266 times $w$; its position depends on $\phi$ only, because the hole is centred at $G$: the angle $\theta$ of the plate does not change where $G$ is. The term in the square of the rate of $\phi$ points along $\mathbf u_2$, from $G$ towards $O$: it is the centripetal acceleration.

> [!derivation] Part (c): rolling without slip at I
> **Law:** velocity field of the rigid body; rolling without slipping on a body at rest; integration with Barrow's rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 13.4; Notes.pdf, Sec. 13.2
>
> The body point of the plate at $I$ must have the velocity of the knob point at $I$, which is zero.
>
> $$\begin{aligned}
> \mathbf v_1^{I(B)} &= \mathbf v_1^G + \boldsymbol\omega_{B0}\times\overrightarrow{GI} = \left(a_2 - a_1\right)\dot\phi\,\mathbf u_1 + \dot\theta\,\mathbf k_1\times\left(a_2\,\mathbf u_2\right) \quad &\text{(velocity field from $G$, Eq. 9.3; $\overrightarrow{GI} = a_2\,\mathbf u_2$)} \\
> &= \left(a_2 - a_1\right)\dot\phi\,\mathbf u_1 - a_2\,\dot\theta\,\mathbf u_1 \quad &\text{($\mathbf k_1\times\mathbf u_2 = -\mathbf u_1$)} \\
> \left(a_2 - a_1\right)\dot\phi - a_2\,\dot\theta &= 0 \quad &\text{(no slip, Eq. 13.5; the normal component is already zero)} \\
> \dot\theta &= \frac{a_2 - a_1}{a_2}\,\dot\phi = \frac23\,\dot\phi \quad &\text{(divide by $a_2$; $a_1 = a_2/3$)} \\
> \int_{\theta_0}^{\theta} d\theta' &= \frac23\int_{\phi_0}^{\phi} d\phi' \quad &\text{(separate and integrate from the initial instant)} \\
> \left[\theta'\right]_{\theta_0}^{\theta} &= \frac23\left[\phi'\right]_{\phi_0}^{\phi} \;\Rightarrow\; \theta - \theta_0 = \frac23\left(\phi - \phi_0\right) \quad &\text{(antiderivative; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta = \frac23\,\dot\phi, \qquad \ddot\theta = \frac23\,\ddot\phi, \qquad \theta - \theta_0 = \frac23\left(\phi - \phi_0\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ on both sides; the integrated form in rad
> **Meaning:** the plate turns in the same sense as the contact point travels round the knob, but more slowly: while $I$ goes once round the knob ($\phi$ grows by $2\pi$) the plate turns by two thirds of a turn. The constraint is integrable (holonomic), as for the planar disk of Notes.pdf, Eq. 13.4.

### Center of Mass and Inertia Tensor

![[attachments/EM-SOL/rb23-composite.svg]]

> [!derivation] Part (a): mass distribution and centre of mass
> **Law:** homogeneous plate: mass proportional to area; additivity, the hole entering with negative mass; symmetry
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 17]
>
> Surface density $\sigma$. The full rectangle $Q$ and the hole $H$ have their centres at the same point, the centre of the rectangle, and both are symmetric about it.
>
> $$\begin{aligned}
> A_Q &= h\,w = 2w^2, \qquad A_H = \pi a_2^2 = \pi\,\frac{w^2}{2\pi} = \frac{w^2}{2} \quad &\text{(areas; data)} \\
> \sigma &= \frac{m}{A_Q - A_H} = \frac{m}{2w^2 - w^2/2} = \frac{2m}{3w^2} \quad &\text{(mass over net area)} \\
> m_Q &= \sigma\,A_Q = \frac{4m}{3}, \qquad m_H = \sigma\,A_H = \frac{m}{3} \quad &\text{(masses of the full rectangle and of the hole)} \\
> m\,\mathbf r^G &= m_Q\,\mathbf 0 - m_H\,\mathbf 0 = \mathbf 0 \quad &\text{(additivity, positions from the common centre)}
> \end{aligned}$$
>
> $$\boxed{\sigma = \frac{2m}{3w^2}, \qquad m_Q = \frac43\,m, \qquad m_H = \frac13\,m, \qquad G \text{ at the centre of the rectangle and of the hole}}$$
>
> **Units:** kg/m$^2$; kg
> **Meaning:** the data are chosen so that the hole takes exactly one quarter of the rectangle; the plate keeps its two axes of symmetry, so $G$ is the common centre.

> [!derivation] Part (a): moment of inertia about the axis through G normal to the plate
> **Law:** moment of inertia as an area integral, in Cartesian coordinates for the rectangle and in polar coordinates (jacobian $\rho$) for the hole; additivity
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.5; Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 16]
>
> Body coordinates $x$ along $\mathbf i_B$ from minus $w/2$ to $w/2$ and $y$ along $\mathbf j_B$ from minus $w$ to $w$ (half of $h$); the squared distance to the axis $\mathbf k_1$ through $G$ is the sum of their squares. For the hole, polar coordinates $(\rho, \chi)$ about $G$, area element $\rho\,d\rho\,d\chi$.
>
> $$\begin{aligned}
> I_{Q} &= \sigma\int_{-w}^{w}\int_{-w/2}^{w/2}\left(x^2 + y^2\right)dx\,dy = \sigma\int_{-w}^{w}\left[\frac{x^3}{3} + y^2 x\right]_{-w/2}^{w/2}dy \quad &\text{(Eq. 10.11; antiderivative in $x$)} \\
> &= \sigma\int_{-w}^{w}\left(\frac{w^3}{12} + w\,y^2\right)dy = \sigma\left[\frac{w^3}{12}\,y + \frac{w\,y^3}{3}\right]_{-w}^{w} \quad &\text{(Barrow's rule in $x$; antiderivative in $y$)} \\
> &= \sigma\left(\frac{w^4}{6} + \frac{2w^4}{3}\right) = \frac56\,\sigma\,w^4 \quad &\text{(Barrow's rule in $y$; common denominator)} \\
> I_{H} &= \sigma\int_0^{2\pi}\int_0^{a_2}\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^{a_2} = \sigma\cdot 2\pi\cdot\frac{a_2^4}{4} \quad &\text{(separable integral; antiderivatives; Barrow's rule)} \\
> &= \frac{\pi\sigma}{2}\cdot\frac{w^4}{4\pi^2} = \frac{\sigma\,w^4}{8\pi} \quad &\text{($a_2^4 = w^4/(4\pi^2)$)} \\
> I_z &= I_Q - I_H = \sigma\,w^4\left(\frac56 - \frac{1}{8\pi}\right) = \frac{2m}{3w^2}\,w^4\,\frac{20\pi - 3}{24\pi} \quad &\text{(additivity: the hole is subtracted; value of $\sigma$)} \\
> &= \frac{20\pi - 3}{36\pi}\,m\,w^2 \quad &\text{(simplify)}
> \end{aligned}$$
>
> $$\boxed{I_z = \frac{20\pi - 3}{36\pi}\,m\,w^2 \approx 0.529\,m\,w^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the full rectangle alone would give $\tfrac43 m$ times $(h^2 + w^2)/12$, that is $\tfrac59 mw^2 \approx 0.556\,mw^2$; the hole, near the axis, removes only $mw^2/(12\pi) \approx 0.027\,mw^2$. The plane motion needs only this component of the tensor; both symmetry axes make the products of inertia with $\mathbf k_1$ zero.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and energies
> **Law:** linear momentum from $G$; angular momentum of a plane body about $G$; Koenig's decomposition; potential of the weight
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf p_1 &= m\,\mathbf v_1^G = m\left(a_2 - a_1\right)\dot\phi\,\mathbf u_1 \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{G} &= I_z\,\dot\theta\,\mathbf k_1, \qquad \left.\frac{d\mathbf H_G}{dt}\right|_1 = I_z\,\ddot\theta\,\mathbf k_1 \quad &\text{(Eq. 11.12; products of inertia with $\mathbf k_1$ zero; $\mathbf k_1$ constant)} \\
> T_1 &= \frac12\,m\left(a_2 - a_1\right)^2\dot\phi^2 + \frac12\,I_z\,\dot\theta^2 \quad &\text{(Eq. 11.31)} \\
> V &= m\,g\,\mathbf r_1^G\cdot\mathbf j_1 = -m\,g\left(a_2 - a_1\right)\cos\phi \quad &\text{(Eq. 12.34; $\mathbf u_2\cdot\mathbf j_1 = \cos\phi$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = I_z\,\dot\theta\,\mathbf k_1, \qquad T_1 = \frac12\,m\left(a_2 - a_1\right)^2\dot\phi^2 + \frac12\,I_z\,\dot\theta^2, \qquad V = -mg\left(a_2 - a_1\right)\cos\phi}$$
>
> **Units:** kg m/s; kg m$^2$/s; J
> **Meaning:** the potential is lowest at $\phi$ equal to zero, with $G$ straight below $O$: the hanging position.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb23-fbd.svg]]

| Force on the plate | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf j_1 = -mg(\sin\phi\,\mathbf u_1 + \cos\phi\,\mathbf u_2)$ | applied |
| Normal reaction of the knob | $I$ | $N\,\mathbf u_2$, with $N \ge 0$ (the knob pushes the edge of the hole away from $O$) | constraint |
| Friction of the knob | $I$ | $F\,\mathbf u_1$ (unknown: rolling without slip) | constraint |

> [!derivation] Part (d): equations of motion
> **Law:** Newton's second law for the centre of mass; moment equation about $G$ with the vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.14; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is the centre of mass, so the moment equation has no term in the velocity of the pole. The weight acts at $G$ and has no moment about it; the contact force acts at $I$, with the arm $a_2\,\mathbf u_2$.
>
> $$\begin{aligned}
> m\left(a_2 - a_1\right)\left(\ddot\phi\,\mathbf u_1 + \dot\phi^2\,\mathbf u_2\right) &= N\,\mathbf u_2 + F\,\mathbf u_1 - mg\left(\sin\phi\,\mathbf u_1 + \cos\phi\,\mathbf u_2\right) \quad &\text{(Eq. 12.8 with the acceleration of part (b))} \\
> m\left(a_2 - a_1\right)\ddot\phi &= F - mg\sin\phi \quad &\text{(component along $\mathbf u_1$)} \\
> m\left(a_2 - a_1\right)\dot\phi^2 &= N - mg\cos\phi \quad &\text{(component along $\mathbf u_2$)} \\
> \mathbf M_G &= \begin{vmatrix} \mathbf u_1 & \mathbf u_2 & \mathbf k_1 \cr 0 & a_2 & 0 \cr F & N & 0 \end{vmatrix} = \mathbf k_1\left(0\cdot N - a_2\,F\right) = -a_2\,F\,\mathbf k_1 \quad &\text{(expand along the first row)} \\
> I_z\,\ddot\theta &= -a_2\,F \quad &\text{(Eq. 12.13 with the pole at $G$, component along $\mathbf k_1$)} \\
> a_2\,\dot\theta &= \left(a_2 - a_1\right)\dot\phi \quad &\text{(rolling, part (c))}
> \end{aligned}$$
>
> $$\boxed{m\left(a_2 - a_1\right)\ddot\phi = F - mg\sin\phi, \qquad m\left(a_2 - a_1\right)\dot\phi^2 = N - mg\cos\phi, \qquad I_z\,\ddot\theta = -a_2\,F, \qquad a_2\,\dot\theta = \left(a_2 - a_1\right)\dot\phi}$$
>
> **Units:** N for the force equations; N m for the moment equation; m/s for the rolling condition
> **Meaning:** four equations for the four unknowns $\phi$, $\theta$, $N$ and $F$, as functions of time. A positive $F$ (along $\mathbf u_1$) has a clockwise moment about $G$.

> [!derivation] Part (e): equation of motion for phi alone
> **Law:** elimination of the reactions between the equations of part (d)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.5
>
> $$\begin{aligned}
> F &= -\frac{I_z\,\ddot\theta}{a_2} = -\frac{I_z\left(a_2 - a_1\right)}{a_2^2}\,\ddot\phi \quad &\text{(moment equation; rolling differentiated once)} \\
> m\left(a_2 - a_1\right)\ddot\phi + \frac{I_z\left(a_2 - a_1\right)}{a_2^2}\,\ddot\phi + mg\sin\phi &= 0 \quad &\text{(substitute in the force along $\mathbf u_1$)} \\
> \frac{I_z}{m\,a_2^2} &= \frac{20\pi - 3}{36\pi}\,w^2\cdot\frac{2\pi}{w^2} = \frac{20\pi - 3}{18} \quad &\text{($a_2^2 = w^2/(2\pi)$)} \\
> 1 + \frac{I_z}{m\,a_2^2} &= \frac{18 + 20\pi - 3}{18} = \frac{5\left(4\pi + 3\right)}{18} \quad &\text{(common denominator)} \\
> \ddot\phi &= -\frac{g\sin\phi}{\left(a_2 - a_1\right)\left(1 + I_z/(m a_2^2)\right)} = -\frac{g\sin\phi\cdot 3\sqrt{2\pi}\cdot 18}{2w\cdot 5\left(4\pi + 3\right)} \quad &\text{(divide by $m(a_2 - a_1)$ times the bracket)} \\
> &= -\frac{27\sqrt{2\pi}}{5\left(4\pi + 3\right)}\,\frac gw\,\sin\phi \quad &\text{(simplify)} \\
> F &= mg\sin\phi + m\left(a_2 - a_1\right)\ddot\phi = mg\sin\phi\left(1 - \frac{18}{5(4\pi + 3)}\right) = \frac{20\pi - 3}{5\left(4\pi + 3\right)}\,mg\sin\phi \quad &\text{(force along $\mathbf u_1$)} \\
> N &= mg\cos\phi + m\left(a_2 - a_1\right)\dot\phi^2 = mg\cos\phi + \frac{2\,m\,w}{3\sqrt{2\pi}}\,\dot\phi^2 \quad &\text{(force along $\mathbf u_2$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\phi + \frac{27\sqrt{2\pi}}{5\left(4\pi + 3\right)}\,\frac gw\,\sin\phi = 0, \qquad \frac{27\sqrt{2\pi}}{5\left(4\pi + 3\right)} \approx 0.870}$$
>
> **Units:** the coefficient of the sine is $[\mathrm{L\,T^{-2}}]/[\mathrm L] = [\mathrm{T^{-2}}]$; $F$ and $N$ in N
> **Meaning:** the plate swings like a pendulum about the knob. Rolling adds the rotational inertia of the plate to the inertia of the translation of $G$ and slows the swing; the friction needed is about 0.769 times $mg\sin\phi$, and the normal reaction carries the radial part of the weight plus the centripetal force.

> [!derivation] Part (f): initial conditions
> **Law:** geometry of the initial position; speed of $G$ from part (b); rolling relation of part (c)
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 13.5; Problems.pdf, p. 53
>
> $G$ and $O$ on the same vertical: read from the figure, the plate hangs, with $G$ below $O$, so $\mathbf u_2$ is $\mathbf j_1$ and $I$ is at the top of the knob. A counterclockwise rotation of the plate is a positive rate of $\theta$, hence (part (c)) a positive rate of $\phi$. The constant $A$ of the statement is not defined elsewhere; it is kept as a datum with units of $[\mathrm{T^{-1}}]$, so that $2wA/3$ is a speed.
>
> $$\begin{aligned}
> \mathbf r_1^G(0) &= -\left(a_2 - a_1\right)\mathbf u_2(0) = -\left(a_2 - a_1\right)\mathbf j_1 \;\Rightarrow\; \phi_0 = 0 \quad &\text{($G$ straight below $O$)} \\
> \left|\mathbf v_1^G(0)\right| &= \left(a_2 - a_1\right)\left|\dot\phi_0\right| = \frac{2w}{3\sqrt{2\pi}}\left|\dot\phi_0\right| = \frac{2wA}{3} \quad &\text{(part (b))} \\
> \dot\phi_0 &= +\sqrt{2\pi}\,A \quad &\text{(solve; positive sign: counterclockwise rotation)} \\
> \theta - 0 &= \frac23\left(\phi - 0\right), \qquad \dot\theta_0 = \frac23\,\dot\phi_0 = \frac{2\sqrt{2\pi}}{3}\,A \quad &\text{(part (c) with $\theta_0 = 0$, $\phi_0 = 0$)}
> \end{aligned}$$
>
> $$\boxed{\phi(0) = 0, \qquad \dot\phi(0) = \sqrt{2\pi}\,A \approx 2.507\,A, \qquad \text{and along the motion } \theta = \frac23\,\phi}$$
>
> **Units:** rad; rad/s
> **Meaning:** the plate starts from the bottom of its swing with $G$ moving to the right (along $\mathbf u_1 = \mathbf i_1$) and the plate turning counterclockwise. If $G$ were placed above $O$ instead, the initial angle would be $\pi$, an unstable equilibrium of the equation of part (e).

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Moment of inertia | $I_z = \dfrac{20\pi - 3}{36\pi}\,mw^2 \approx 0.529\,mw^2$ |
| (b) Kinematics of $G$ | $\mathbf r^G = -(a_2 - a_1)\,\mathbf u_2$, $\mathbf v^G = (a_2 - a_1)\dot\phi\,(\cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1)$, $\mathbf a^G = (a_2 - a_1)[(\ddot\phi\cos\phi - \dot\phi^2\sin\phi)\,\mathbf i_1 + (\ddot\phi\sin\phi + \dot\phi^2\cos\phi)\,\mathbf j_1]$, with $a_2 - a_1 = 2w/(3\sqrt{2\pi})$; independent of $\theta$ |
| (c) Rolling | $a_2\dot\theta = (a_2 - a_1)\dot\phi$, so $\dot\theta = \tfrac23\dot\phi$ |
| (d) Equations | $m(a_2 - a_1)\ddot\phi = F - mg\sin\phi$; $m(a_2 - a_1)\dot\phi^2 = N - mg\cos\phi$; $I_z\ddot\theta = -a_2F$; plus rolling |
| (e) Equation for $\phi$ | $\ddot\phi + \dfrac{27\sqrt{2\pi}}{5(4\pi + 3)}\dfrac gw\sin\phi = 0$ |
| (f) Initial conditions | $\phi(0) = 0$, $\dot\phi(0) = \sqrt{2\pi}\,A$ (and $\theta = \tfrac23\phi$) |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: energy of the rolling plate
> **Law:** conservation of the mechanical energy (the contact force acts on a body point at rest); chain rule
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 11.31
>
> $$\begin{aligned}
> T_1 &= \frac12\left(a_2 - a_1\right)^2\dot\phi^2\left(m + \frac{I_z}{a_2^2}\right) \quad &\text{(rolling: $\dot\theta = (a_2 - a_1)\dot\phi/a_2$)} \\
> \frac{d}{dt}\left(T_1 + V\right) &= \left(a_2 - a_1\right)^2\left(m + \frac{I_z}{a_2^2}\right)\dot\phi\,\ddot\phi + mg\left(a_2 - a_1\right)\sin\phi\,\dot\phi \quad &\text{(chain rule on both terms)} \\
> &= \left(a_2 - a_1\right)\dot\phi\left[\left(a_2 - a_1\right)\left(m + \frac{I_z}{a_2^2}\right)\ddot\phi + mg\sin\phi\right] \quad &\text{(factor)}
> \end{aligned}$$
>
> $$\boxed{\frac{d}{dt}\left(T_1 + V\right) = 0 \iff \text{the equation of part (e)}}$$
>
> **Units:** W in every term
> **Meaning:** the bracket is the equation of part (e) multiplied by $m(a_2 - a_1)$ times the bracket of that box; the energy method, with no reaction in sight, gives the same equation of motion.

**Limiting cases and consistency:**

* **Pin instead of knob.** For a knob of vanishing radius ($a_1$ tending to zero) the rolling condition gives equal rates of $\theta$ and $\phi$: the plate turns rigidly about the fixed point $I$ of the rim of the hole, and the general coefficient of the sine, $g$ divided by $(a_2 - a_1)(1 + I_z/(ma_2^2))$, becomes $mg\,a_2/(I_z + m a_2^2)$: the compound pendulum with the pivot at the distance $a_2$ from $G$ (parallel axis theorem). This is the expected limit.
* **Small oscillations.** For small $\phi$ the sine is replaced by $\phi$ (Notes.pdf, Eq. 5.6) and the plate oscillates with the angular frequency $\sqrt{0.870\,g/w}$; for $w$ equal to 0.1 m this is about 9.2 rad/s.
* **Sign check.** For a small positive $\phi$ the second rate of $\phi$ is negative: $G$ swings back below $O$, the stable position.
* **Dimensions.** $I_z$ is a mass times a squared length; the friction is a pure number times $mg$; every term of the equation of part (e) is in $[\mathrm{T^{-2}}]$.

---

## Problem RB-28: Euler's disk

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous coin $b$ of mass $m$, radius $R$, centre $G$ and negligible thickness, always touching a fixed horizontal plane at the point $C$ of its rim. Gravity acts downwards.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, with the basis $\{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$, $O$ on the plane and $\mathbf k_0$ vertical upwards. The plane is at rest, so this frame is inertial.
* **Polar frame of the contact point:** $S_1\{C; \mathbf i_1, \mathbf j_1, \mathbf k_1\}$, with $\mathbf i_1$ along $OC$ (radial), $\mathbf j_1$ horizontal and normal to it, $\mathbf k_1$ equal to $\mathbf k_0$; $(r, \psi)$ are the polar coordinates of $C$.
* **Euler angles with respect to $S_1$:** $\beta$ turns $\mathcal B_1$ about the vertical into $\mathcal B_2$, the basis $\{\mathbf x_2, \mathbf y_2, \mathbf k_1\}$; $\mathbf y_2$ is the horizontal tangent to the rim at $C$. $\theta$ tilts the coin about the line $\mathbf y_2$ into $\mathcal B_3$, the basis $\{\mathbf x_3, \mathbf y_2, \mathbf z_3\}$, with $\mathbf z_3$ along $CG$ and $\mathbf x_3$ normal to the coin (the coin lies in the plane $C y_2 z_3$). $\delta$ turns the coin about its normal $\mathbf x_3$ into the body basis $\mathcal B_b$, that is $\{\mathbf x_3, \mathbf y_4, \mathbf z_4\}$.
* **Signs, read from the figure:** $\beta$ is positive about $\mathbf k_1$. $\theta$ is positive when $\mathbf z_3$ leans from the vertical towards minus $\mathbf x_2$ (towards the side of $O$ when $\beta$ is zero, as in part (f), where $G$ is above $O$); this is a positive rotation about minus $\mathbf y_2$. $\delta$ is taken positive about $\mathbf x_3$ (the figure shows its magnitude only; the other choice changes the sign of $\delta$ in every formula).
* **Part (a), degrees of freedom:** a free rigid body has six coordinates. Contact with the plane (Notes.pdf, Eq. 13.1) fixes the height of $G$ in terms of $\theta$: five coordinates remain, $r$, $\psi$, $\beta$, $\theta$, $\delta$. If the coin can slip, it has **five degrees of freedom**. Rolling without slip adds two scalar conditions between the rates (part (c)) that cannot be integrated: the coin keeps five coordinates but has **three degrees of freedom** (independent velocities).

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the coin, homogeneous, thin | $m$ | kg |
| Radius | $R$ | m |
| Moment of inertia about the symmetry axis (statement) | $mR^2/2$ | kg m$^2$ |
| Polar coordinates of $C$ | $r$, $\psi$ | m, rad |
| Euler angles with respect to $S_1$ | $\beta$, $\theta$, $\delta$ | rad |
| Friction coefficient from part (c) on | $\mu$ infinite (no slip) | - |
| Part (f) | $\beta = 0$, $\mathbf r_0^G = h\,\mathbf k_0$ with $h$ constant, smaller than $R$ | m |
| Gravity | $g$, along $-\mathbf k_0$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb28-rot-psi.svg]]

> [!derivation] Polar basis of the contact point: rotation by psi about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View of the plane from above with $\mathbf k_0$ out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up; a positive $\psi$ turns counterclockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\psi$), opposite leg along $\mathbf j_0$ (sine). Triangle of $\mathbf j_1$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine), because the counterclockwise turn carries the tip of $\mathbf j_0$ to the left.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k_0, \qquad \dot{\mathbf i}_1 = \dot\psi\,\mathbf k_0\times\mathbf i_1 = \dot\psi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\psi\,\mathbf k_0\times\mathbf j_1 = -\dot\psi\,\mathbf i_1 \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k_0, \qquad \mathbf r_0^C = r\,\mathbf i_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$; $[\mathrm L]$
> **Meaning:** the frame $S_1$ follows the contact point round $O$; $\beta$ is measured from its radial direction.

![[attachments/EM-SOL/rb28-rot-beta.svg]]

> [!derivation] Heading of the coin: rotation by beta about k1
> **Law:** simple rotation about the third axis; composition of angular velocities
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> Same view from above at $C$, $\mathbf k_1$ out of the paper (⊙). Triangle of $\mathbf x_2$: adjacent leg along $\mathbf i_1$ (cosine of $\beta$), opposite leg along $\mathbf j_1$ (sine). Triangle of $\mathbf y_2$: adjacent leg along $\mathbf j_1$ (cosine), opposite leg along minus $\mathbf i_1$ (sine).
>
> $$\begin{aligned}
> \mathbf x_2 &= \cos\beta\,\mathbf i_1 + \sin\beta\,\mathbf j_1, \qquad \mathbf y_2 = -\sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf j_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} \cos\beta & -\sin\beta & 0 \cr \sin\beta & \cos\beta & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_1R_2] = \cos^2\beta + \sin^2\beta = 1 \quad &\text{(columns in $\mathcal B_1$; expand along the third row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} \cos^2\beta + \sin^2\beta & \cos\beta\sin\beta - \sin\beta\cos\beta & 0 \cr \sin\beta\cos\beta - \cos\beta\sin\beta & \sin^2\beta + \cos^2\beta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_1 &= \cos\beta\,\mathbf x_2 - \sin\beta\,\mathbf y_2, \qquad \mathbf j_1 = \sin\beta\,\mathbf x_2 + \cos\beta\,\mathbf y_2 \quad &\text{(rows: the inverse is the transpose)} \\
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \left(\dot\psi + \dot\beta\right)\mathbf k_1 \equiv \Lambda\,\mathbf k_1 \quad &\text{(composition, Eq. 9.21; both about the vertical)} \\
> \dot{\mathbf x}_2 &= \Lambda\,\mathbf k_1\times\mathbf x_2 = \Lambda\,\mathbf y_2, \qquad \dot{\mathbf y}_2 = \Lambda\,\mathbf k_1\times\mathbf y_2 = -\Lambda\,\mathbf x_2 \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf x_2 = \cos\beta\,\mathbf i_1 + \sin\beta\,\mathbf j_1, \qquad \mathbf y_2 = -\sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf j_1, \qquad \boldsymbol\omega_{20} = \Lambda\,\mathbf k_1, \qquad \Lambda = \dot\psi + \dot\beta}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\psi$ plus $\beta$ is the heading of the coin measured from $\mathbf i_0$; only its rate $\Lambda$ enters the rotation of the coin.

![[attachments/EM-SOL/rb28-rot-theta.svg]]

> [!derivation] Tilt of the coin: rotation by theta about minus y2
> **Law:** simple rotation about the second axis; right-hand rule with the axis out of the paper; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; Notes.pdf, Sec. 15.1
>
> Vertical section through $C$ normal to the tangent $\mathbf y_2$, with $\mathbf x_2$ to the right and $\mathbf k_1$ up. The product of $\mathbf x_2$ and $\mathbf k_1$ is minus $\mathbf y_2$, so in this right-handed view $\mathbf y_2$ points into the paper (⊗) and minus $\mathbf y_2$ out of it (⊙). The coin appears edge-on as the segment $CG$ extended; it leans to the left by $\theta$, a counterclockwise turn, which is a positive rotation about minus $\mathbf y_2$. Triangle of $\mathbf z_3$: hypotenuse 1 along $CG$, adjacent leg along $\mathbf k_1$ (cosine of $\theta$), opposite leg along minus $\mathbf x_2$ (sine). Triangle of $\mathbf x_3$: adjacent leg along $\mathbf x_2$ (cosine), opposite leg along $\mathbf k_1$ (sine).
>
> $$\begin{aligned}
> \mathbf x_3 &= \cos\theta\,\mathbf x_2 + \sin\theta\,\mathbf k_1, \qquad \mathbf z_3 = -\sin\theta\,\mathbf x_2 + \cos\theta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> [{}_2R_3] &= \begin{bmatrix} \cos\theta & 0 & -\sin\theta \cr 0 & 1 & 0 \cr \sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf x_3$, $\mathbf y_2$, $\mathbf z_3$ in $\mathcal B_2$)} \\
> \det[{}_2R_3] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_2R_3][{}_2R_3]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 & \cos\theta\sin\theta - \sin\theta\cos\theta \cr 0 & 1 & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf x_3\times\mathbf y_2 &= \cos\theta\,\mathbf x_2\times\mathbf y_2 + \sin\theta\,\mathbf k_1\times\mathbf y_2 = \cos\theta\,\mathbf k_1 - \sin\theta\,\mathbf x_2 = \mathbf z_3 \quad &\text{(the triad is right-handed)} \\
> \mathbf x_2 &= \cos\theta\,\mathbf x_3 - \sin\theta\,\mathbf z_3, \qquad \mathbf k_1 = \sin\theta\,\mathbf x_3 + \cos\theta\,\mathbf z_3 \quad &\text{(rows: the inverse is the transpose)} \\
> \boldsymbol\omega_{30} &= \Lambda\,\mathbf k_1 - \dot\theta\,\mathbf y_2 = \Lambda\sin\theta\,\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3 \quad &\text{(composition, Eq. 9.21; rotation about minus $\mathbf y_2$)} \\
> \dot{\mathbf x}_3 &= \boldsymbol\omega_{30}\times\mathbf x_3 = \Lambda\cos\theta\,\mathbf y_2 + \dot\theta\,\mathbf z_3, \qquad \dot{\mathbf z}_3 = \boldsymbol\omega_{30}\times\mathbf z_3 = -\dot\theta\,\mathbf x_3 - \Lambda\sin\theta\,\mathbf y_2 \quad &\text{(Poisson; $\mathbf z_3\times\mathbf x_3 = \mathbf y_2$, $\mathbf y_2\times\mathbf z_3 = \mathbf x_3$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf x_3 = \cos\theta\,\mathbf x_2 + \sin\theta\,\mathbf k_1, \qquad \mathbf z_3 = -\sin\theta\,\mathbf x_2 + \cos\theta\,\mathbf k_1, \qquad \boldsymbol\omega_{30} = \Lambda\sin\theta\,\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\mathbf x_3$ is the normal of the coin, lifted by $\theta$ above the horizontal; $\theta$ zero is the upright coin.

![[attachments/EM-SOL/rb28-rot-delta.svg]]

> [!derivation] Spin of the coin: rotation by delta about x3
> **Law:** simple rotation about the first axis; invariance of the tensor of an axisymmetric body
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 10.41
>
> View of the face of the coin with its normal $\mathbf x_3$ out of the paper (⊙), $\mathbf y_2$ to the right and $\mathbf z_3$ up; this is right-handed because the product of $\mathbf y_2$ and $\mathbf z_3$ is $\mathbf x_3$. A positive $\delta$ turns counterclockwise. Triangle of $\mathbf y_4$: adjacent leg along $\mathbf y_2$ (cosine of $\delta$), opposite leg along $\mathbf z_3$ (sine). Triangle of $\mathbf z_4$: adjacent leg along $\mathbf z_3$ (cosine), opposite leg along minus $\mathbf y_2$ (sine).
>
> $$\begin{aligned}
> \mathbf y_4 &= \cos\delta\,\mathbf y_2 + \sin\delta\,\mathbf z_3, \qquad \mathbf z_4 = -\sin\delta\,\mathbf y_2 + \cos\delta\,\mathbf z_3 \quad &\text{(legs of the two triangles)} \\
> [{}_3R_b] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\delta & -\sin\delta \cr 0 & \sin\delta & \cos\delta \end{bmatrix}, \qquad \det[{}_3R_b] = \cos^2\delta + \sin^2\delta = 1 \quad &\text{(columns: $\mathbf x_3$, $\mathbf y_4$, $\mathbf z_4$ in $\mathcal B_3$; expand along the first row)} \\
> [{}_3R_b][{}_3R_b]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\delta + \sin^2\delta & \cos\delta\sin\delta - \sin\delta\cos\delta \cr 0 & \sin\delta\cos\delta - \cos\delta\sin\delta & \sin^2\delta + \cos^2\delta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b3} &= \dot\delta\,\mathbf x_3 \quad &\text{(rotation about the normal of the coin)}
> \end{aligned}$$
>
> $$\boxed{\mathbf y_4 = \cos\delta\,\mathbf y_2 + \sin\delta\,\mathbf z_3, \qquad \mathbf z_4 = -\sin\delta\,\mathbf y_2 + \cos\delta\,\mathbf z_3, \qquad \boldsymbol\omega_{b3} = \dot\delta\,\mathbf x_3}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the coin differs from $\mathcal B_3$ only by a turn about its own axis; the tensor of inertia will have the same matrix in both bases.

> [!derivation] Part (b): angular velocity and angular acceleration
> **Law:** composition of angular velocities; derivative of each term with Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 3.8; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= \boldsymbol\omega_{b3} + \boldsymbol\omega_{30} = \Lambda\,\mathbf k_1 - \dot\theta\,\mathbf y_2 + \dot\delta\,\mathbf x_3 \quad &\text{(composition, Eq. 9.21)} \\
> &= \left(\dot\delta + \Lambda\sin\theta\right)\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3 \quad &\text{($\mathbf k_1$ in $\mathcal B_3$)} \\
> \boldsymbol\alpha_{B0} &= \dot\Lambda\,\mathbf k_1 - \ddot\theta\,\mathbf y_2 - \dot\theta\,\dot{\mathbf y}_2 + \ddot\delta\,\mathbf x_3 + \dot\delta\,\dot{\mathbf x}_3 \quad &\text{(product rule on each term; $\mathbf k_1$ constant)} \\
> &= \dot\Lambda\,\mathbf k_1 - \ddot\theta\,\mathbf y_2 + \dot\theta\Lambda\,\mathbf x_2 + \ddot\delta\,\mathbf x_3 + \dot\delta\left(\Lambda\cos\theta\,\mathbf y_2 + \dot\theta\,\mathbf z_3\right) \quad &\text{(Poisson for $\mathbf y_2$ and $\mathbf x_3$)} \\
> \dot\Lambda\,\mathbf k_1 + \dot\theta\Lambda\,\mathbf x_2 &= \left(\dot\Lambda\sin\theta + \dot\theta\Lambda\cos\theta\right)\mathbf x_3 + \left(\dot\Lambda\cos\theta - \dot\theta\Lambda\sin\theta\right)\mathbf z_3 \quad &\text{($\mathbf k_1$ and $\mathbf x_2$ in $\mathcal B_3$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{B0} = \left(\dot\delta + \Lambda\sin\theta\right)\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3}$$
>
> $$\boxed{\boldsymbol\alpha_{B0} = \left(\ddot\delta + \dot\Lambda\sin\theta + \Lambda\dot\theta\cos\theta\right)\mathbf x_3 + \left(-\ddot\theta + \dot\delta\Lambda\cos\theta\right)\mathbf y_2 + \left(\dot\Lambda\cos\theta - \Lambda\dot\theta\sin\theta + \dot\delta\dot\theta\right)\mathbf z_3}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** $\Lambda$ is the rate of $\psi$ plus the rate of $\beta$, and its derivative is the sum of the second rates. The component along the normal $\mathbf x_3$ is the spin of the coin; the other two describe the turning and the tilting of its plane.

> [!derivation] Part (b): position, velocity and acceleration of G
> **Law:** sum of segments; derivative of a vector written in moving bases; Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> $G$ is at the distance $R$ from the rim point $C$ along the diameter $\mathbf z_3$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \overrightarrow{OC} + \overrightarrow{CG} = r\,\mathbf i_1 + R\,\mathbf z_3 \quad &\text{(sum of segments)} \\
> &= \left(r - R\sin\theta\cos\beta\right)\mathbf i_1 - R\sin\theta\sin\beta\,\mathbf j_1 + R\cos\theta\,\mathbf k_0 \quad &\text{($\mathbf z_3$ and $\mathbf x_2$ in $\mathcal B_1$)} \\
> \mathbf v_0^G &= \dot r\,\mathbf i_1 + r\,\dot\psi\,\mathbf j_1 + R\,\dot{\mathbf z}_3 = \dot r\,\mathbf i_1 + r\,\dot\psi\,\mathbf j_1 - R\,\dot\theta\,\mathbf x_3 - R\,\Lambda\sin\theta\,\mathbf y_2 \quad &\text{(product rule; Poisson)} \\
> \mathbf v_0^G &= \left(\dot r\cos\beta + r\dot\psi\sin\beta - R\dot\theta\cos\theta\right)\mathbf x_2 + \left(-\dot r\sin\beta + r\dot\psi\cos\beta - R\Lambda\sin\theta\right)\mathbf y_2 - R\dot\theta\sin\theta\,\mathbf k_1 \quad &\text{($\mathbf i_1$, $\mathbf j_1$, $\mathbf x_3$ in $\mathcal B_2$)} \\
> \mathbf a_0^G &= \ddot r\,\mathbf i_1 + \dot r\dot\psi\,\mathbf j_1 + \left(\dot r\dot\psi + r\ddot\psi\right)\mathbf j_1 - r\dot\psi^2\,\mathbf i_1 - R\left(\ddot\theta\,\mathbf x_3 + \dot\theta\,\dot{\mathbf x}_3\right) - R\left(\dot\Lambda\sin\theta + \Lambda\dot\theta\cos\theta\right)\mathbf y_2 - R\Lambda\sin\theta\,\dot{\mathbf y}_2 \quad &\text{(product rule on each term)} \\
> &= \left(\ddot r - r\dot\psi^2\right)\mathbf i_1 + \left(r\ddot\psi + 2\dot r\dot\psi\right)\mathbf j_1 - R\ddot\theta\,\mathbf x_3 - R\dot\theta^2\,\mathbf z_3 - R\left(\dot\Lambda\sin\theta + 2\Lambda\dot\theta\cos\theta\right)\mathbf y_2 + R\Lambda^2\sin\theta\,\mathbf x_2 \quad &\text{(Poisson for $\mathbf x_3$ and $\mathbf y_2$; collect)}
> \end{aligned}$$
>
> Writing $\mathbf i_1$, $\mathbf j_1$ with the rows of $[{}_1R_2]$ and $\mathbf x_3$, $\mathbf z_3$ with the columns of $[{}_2R_3]$, the components of the acceleration along $\mathbf x_2$, $\mathbf y_2$, $\mathbf k_1$ are
>
> $$\boxed{a_{x_2} = \left(\ddot r - r\dot\psi^2\right)\cos\beta + \left(r\ddot\psi + 2\dot r\dot\psi\right)\sin\beta + R\left(\Lambda^2\sin\theta + \dot\theta^2\sin\theta - \ddot\theta\cos\theta\right)}$$
>
> $$\boxed{a_{y_2} = -\left(\ddot r - r\dot\psi^2\right)\sin\beta + \left(r\ddot\psi + 2\dot r\dot\psi\right)\cos\beta - R\left(\dot\Lambda\sin\theta + 2\Lambda\dot\theta\cos\theta\right)}$$
>
> $$\boxed{a_{k_1} = -R\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in every bracket (a length times a squared rate)
> **Meaning:** the vertical component is the second derivative of the height of $G$, which is $R$ times the cosine of $\theta$; the first two terms of the horizontal components are the polar acceleration of the contact point, the others the motion of $G$ relative to $C$.

> [!derivation] Part (c): rolling without slip at C
> **Law:** velocity field of the rigid body; rolling without slipping on a plane at rest; vector product by its determinant
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> Write the components of the angular velocity in $\mathcal B_3$ as $\omega_x$, $\omega_y$, $\omega_z$ (part (b)). The body point at $C$ is at minus $R\,\mathbf z_3$ from $G$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0}\times\left(-R\,\mathbf z_3\right) &= \begin{vmatrix} \mathbf x_3 & \mathbf y_2 & \mathbf z_3 \cr \omega_x & \omega_y & \omega_z \cr 0 & 0 & -R \end{vmatrix} = -R\,\omega_y\,\mathbf x_3 + R\,\omega_x\,\mathbf y_2 \quad &\text{(expand along the first row)} \\
> &= R\,\dot\theta\,\mathbf x_3 + R\left(\dot\delta + \Lambda\sin\theta\right)\mathbf y_2 \quad &\text{(components of part (b))} \\
> \mathbf v_0^{C(B)} &= \mathbf v_0^G + \boldsymbol\omega_{B0}\times\left(-R\,\mathbf z_3\right) = \dot r\,\mathbf i_1 + r\dot\psi\,\mathbf j_1 + R\,\dot\delta\,\mathbf y_2 \quad &\text{(velocity field, Eq. 9.3; the terms in $\dot\theta$ and $\Lambda$ cancel)} \\
> &= \left(\dot r\cos\beta + r\dot\psi\sin\beta\right)\mathbf x_2 + \left(-\dot r\sin\beta + r\dot\psi\cos\beta + R\dot\delta\right)\mathbf y_2 \quad &\text{($\mathbf i_1$, $\mathbf j_1$ in $\mathcal B_2$)} \\
> \mathbf v_0^{C(B)} &= \mathbf 0 \quad &\text{(no slip on the plane at rest, Eq. 13.5)}
> \end{aligned}$$
>
> $$\boxed{\dot r\cos\beta + r\,\dot\psi\sin\beta = 0, \qquad -\dot r\sin\beta + r\,\dot\psi\cos\beta + R\,\dot\delta = 0 \quad\Longleftrightarrow\quad \dot r = R\,\dot\delta\sin\beta, \quad r\,\dot\psi = -R\,\dot\delta\cos\beta}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ in every term
> **Meaning:** the vertical component vanishes identically (contact is kept). The geometric contact point must travel along the tangent $\mathbf y_2$ of the coin, at the speed at which the rim unrolls, $R$ times the rate of $\delta$. Two conditions on the rates that cannot be integrated into relations among $r$, $\psi$, $\beta$, $\delta$: rolling with $\beta$ held at zero changes $\psi$ and $\delta$ at fixed $r$, rolling with $\beta$ held at a right angle changes $r$ and $\delta$ at fixed $\psi$, and turning $\beta$ costs nothing, so every combination of $r$, $\psi$ and $\delta$ can be reached and no finite relation among them exists (the formal proof that the form is not integrable is an extension). This is why the coin keeps five coordinates but only three degrees of freedom, as stated in part (a).

### Center of Mass and Inertia Tensor

> [!derivation] Inertia tensor of the thin coin about G
> **Law:** moments and products of inertia as area integrals in polar coordinates (jacobian $\rho$); symmetry of revolution
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; Notes.pdf, Eq. 10.5; [Lecture 8, Slide 16]
>
> Polar coordinates $(\rho, \chi)$ in the plane of the coin about $G$, with $\rho$ from 0 to $R$ and $\chi$ from 0 to $2\pi$ measured from $\mathbf y_2$; area element $\rho\,d\rho\,d\chi$; surface density $\sigma$. A point of the coin is at $\rho\cos\chi$ along $\mathbf y_2$ and $\rho\sin\chi$ along $\mathbf z_3$, and at zero distance along the normal (negligible thickness). The centre of mass is the centre $G$ (symmetry).
>
> $$\begin{aligned}
> m &= \sigma\int_0^{2\pi}\int_0^R \rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^2}{2}\right]_0^R = \sigma\pi R^2 \quad &\text{(antiderivatives; Barrow's rule)} \\
> I_1 &= \sigma\int_0^{2\pi}\int_0^R \rho^2\,\rho\,d\rho\,d\chi = \sigma\cdot 2\pi\left[\frac{\rho^4}{4}\right]_0^R = \frac{\sigma\pi R^4}{2} = \frac{mR^2}{2} \quad &\text{(axis $\mathbf x_3$: squared distance $\rho^2$; Barrow's rule)} \\
> \int_0^{2\pi}\sin^2\chi\,d\chi &= \left[\frac{\chi}{2} - \frac{\sin 2\chi}{4}\right]_0^{2\pi} = \pi - 0 = \pi \quad &\text{(antiderivative; Barrow's rule)} \\
> I_2 &= \sigma\int_0^{2\pi}\int_0^R \rho^2\sin^2\chi\,\rho\,d\rho\,d\chi = \sigma\,\pi\left[\frac{\rho^4}{4}\right]_0^R = \frac{mR^2}{4} \quad &\text{(axis $\mathbf y_2$: squared distance $(\rho\sin\chi)^2$)} \\
> \int_0^{2\pi}\cos^2\chi\,d\chi &= \left[\frac{\chi}{2} + \frac{\sin 2\chi}{4}\right]_0^{2\pi} = \pi \;\Rightarrow\; I_3 = \frac{mR^2}{4} \quad &\text{(axis $\mathbf z_3$: squared distance $(\rho\cos\chi)^2$)} \\
> \int_0^{2\pi}\sin\chi\cos\chi\,d\chi &= \left[\frac{\sin^2\chi}{2}\right]_0^{2\pi} = 0 \quad &\text{(product $y z$; the products with the normal coordinate vanish, Eq. 10.15)} \\
> [{}_3R_b]^T\,\mathrm{diag}\left(I_1, I_2, I_2\right)[{}_3R_b] &= \mathrm{diag}\left(I_1,\ I_2\cos^2\delta + I_2\sin^2\delta,\ I_2\sin^2\delta + I_2\cos^2\delta\right) \quad &\text{(change of basis; the off-diagonal terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \frac{mR^2}{4}\begin{bmatrix} 2 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in } \mathcal B_3 \text{ and in } \mathcal B_b}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the axial moment $I_1 = mR^2/2$ agrees with the datum of the statement. Every diameter is a principal axis with the moment $mR^2/4$, so $\mathcal B_3$, which does not spin with the coin, is a principal basis at all times.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and energies
> **Law:** linear momentum from $G$; angular momentum from the principal tensor; Koenig's decomposition; potential of the weight
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G \quad &\text{(Eq. 11.3, with the velocity of part (b))} \\
> \mathbf H_{G} &= \frac{mR^2}{2}\left(\dot\delta + \Lambda\sin\theta\right)\mathbf x_3 - \frac{mR^2}{4}\,\dot\theta\,\mathbf y_2 + \frac{mR^2}{4}\,\Lambda\cos\theta\,\mathbf z_3 \quad &\text{(Eq. 11.12 in the principal basis $\mathcal B_3$)} \\
> T_0 &= \frac12\,m\left|\mathbf v_0^G\right|^2 + \frac{mR^2}{4}\left(\dot\delta + \Lambda\sin\theta\right)^2 + \frac{mR^2}{8}\left(\dot\theta^2 + \Lambda^2\cos^2\theta\right) \quad &\text{(Eq. 11.31)} \\
> V &= m\,g\,\mathbf r_0^G\cdot\mathbf k_0 = m\,g\,R\cos\theta \quad &\text{(Eq. 12.34, zero level on the plane)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = \frac{mR^2}{4}\left[2\left(\dot\delta + \Lambda\sin\theta\right)\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3\right], \qquad V = mgR\cos\theta}$$
>
> **Units:** kg m/s; kg m$^2$/s; J
> **Meaning:** the angular momentum is not parallel to the angular velocity: the spin component is weighted twice as much as the other two.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb28-fbd.svg]]

| Force on the coin | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf k_1$ | applied |
| Normal reaction of the plane | $C$ | $N\,\mathbf k_1$, $N \ge 0$ (new unknown) | constraint |
| Friction of the plane | $C$ | $F_x\,\mathbf x_2 + F_y\,\mathbf y_2$ (two new unknowns; no slip) | constraint |

> [!derivation] Part (d): resultant force and moment about G
> **Law:** sum of forces; moment about $G$ by a determinant in $\mathcal B_3$
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \mathbf F &= F_x\,\mathbf x_2 + F_y\,\mathbf y_2 + \left(N - mg\right)\mathbf k_1 \quad &\text{(sum of the three forces)} \\
> \mathbf F_C &= \left(F_x\cos\theta + N\sin\theta\right)\mathbf x_3 + F_y\,\mathbf y_2 + \left(N\cos\theta - F_x\sin\theta\right)\mathbf z_3 \quad &\text{(contact force in $\mathcal B_3$: $\mathbf x_2$ and $\mathbf k_1$ by the rows of $[{}_2R_3]$)} \\
> \mathbf M_G &= \begin{vmatrix} \mathbf x_3 & \mathbf y_2 & \mathbf z_3 \cr 0 & 0 & -R \cr F_x\cos\theta + N\sin\theta & F_y & N\cos\theta - F_x\sin\theta \end{vmatrix} \quad &\text{(arm $\overrightarrow{GC} = -R\,\mathbf z_3$; the weight has no arm)} \\
> &= R\,F_y\,\mathbf x_3 - R\left(F_x\cos\theta + N\sin\theta\right)\mathbf y_2 \quad &\text{(expand along the first row)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = F_x\,\mathbf x_2 + F_y\,\mathbf y_2 + \left(N - mg\right)\mathbf k_1, \qquad \mathbf M_G = R\,F_y\,\mathbf x_3 - R\left(F_x\cos\theta + N\sin\theta\right)\mathbf y_2}$$
>
> **Units:** N; N m
> **Meaning:** the contact force acts on the diameter through $G$, so it has no moment along $\mathbf z_3$; the friction along the tangent spins the coin, and the normal reaction together with the radial friction tries to tip it about the tangent $\mathbf y_2$.

> [!derivation] Part (e): Newton's equations
> **Law:** Newton's second law for the centre of mass, projected in $\mathcal B_2$
> **Source:** Notes.pdf, Eq. 12.8; [Lecture 10, Slide 4]
>
> $$\begin{aligned}
> m\left[\left(\ddot r - r\dot\psi^2\right)\cos\beta + \left(r\ddot\psi + 2\dot r\dot\psi\right)\sin\beta + R\left(\left(\Lambda^2 + \dot\theta^2\right)\sin\theta - \ddot\theta\cos\theta\right)\right] &= F_x \quad &\text{(component along $\mathbf x_2$)} \\
> m\left[-\left(\ddot r - r\dot\psi^2\right)\sin\beta + \left(r\ddot\psi + 2\dot r\dot\psi\right)\cos\beta - R\left(\dot\Lambda\sin\theta + 2\Lambda\dot\theta\cos\theta\right)\right] &= F_y \quad &\text{(component along $\mathbf y_2$)} \\
> -m\,R\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right) &= N - mg \quad &\text{(component along $\mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{m\,a_{x_2} = F_x, \qquad m\,a_{y_2} = F_y, \qquad N = mg - mR\left(\ddot\theta\sin\theta + \dot\theta^2\cos\theta\right)}$$
>
> **Units:** N in every equation
> **Meaning:** the normal reaction differs from the weight only while the height of $G$ accelerates.

> [!derivation] Part (e): Euler's equations about G
> **Law:** moment equation about the centre of mass; derivative of the angular momentum in the rotating basis $\mathcal B_3$ (Coriolis theorem); vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.8; Notes.pdf, Sec. 15.1; [Lecture 10, Slide 5]
>
> Write $I_1$ for $mR^2/2$ and $I_2$ for $mR^2/4$. The basis $\mathcal B_3$ turns with the angular velocity $\boldsymbol\omega_{30}$ of the tilt box, whose components are $\omega_x$ minus the rate of $\delta$, $\omega_y$ and $\omega_z$. The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G}{dt}\right|_0 &= I_1\,\dot\omega_x\,\mathbf x_3 + I_2\,\dot\omega_y\,\mathbf y_2 + I_2\,\dot\omega_z\,\mathbf z_3 + \boldsymbol\omega_{30}\times\mathbf H_G \quad &\text{(Coriolis theorem with $\mathcal B_3$, Eq. 3.8)} \\
> \boldsymbol\omega_{30}\times\mathbf H_G &= \begin{vmatrix} \mathbf x_3 & \mathbf y_2 & \mathbf z_3 \cr \Lambda\sin\theta & \omega_y & \omega_z \cr I_1\omega_x & I_2\omega_y & I_2\omega_z \end{vmatrix} \quad &\text{(vector product)} \\
> &= \left(I_2\,\omega_y\omega_z - I_2\,\omega_z\omega_y\right)\mathbf x_3 + \omega_z\left(I_1\omega_x - I_2\Lambda\sin\theta\right)\mathbf y_2 + \omega_y\left(I_2\Lambda\sin\theta - I_1\omega_x\right)\mathbf z_3 \quad &\text{(expand along the first row)} \\
> I_1\,\frac{d}{dt}\left(\dot\delta + \Lambda\sin\theta\right) &= R\,F_y \quad &\text{(moment along $\mathbf x_3$)} \\
> -I_2\,\ddot\theta + \Lambda\cos\theta\left(I_1\left(\dot\delta + \Lambda\sin\theta\right) - I_2\Lambda\sin\theta\right) &= -R\left(F_x\cos\theta + N\sin\theta\right) \quad &\text{(moment along $\mathbf y_2$)} \\
> I_2\,\frac{d}{dt}\left(\Lambda\cos\theta\right) - \dot\theta\left(I_2\Lambda\sin\theta - I_1\left(\dot\delta + \Lambda\sin\theta\right)\right) &= 0 \quad &\text{(moment along $\mathbf z_3$)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12 mR^2\left(\ddot\delta + \dot\Lambda\sin\theta + \Lambda\dot\theta\cos\theta\right) = R\,F_y}$$
>
> $$\boxed{-\tfrac14 mR^2\,\ddot\theta + \tfrac14 mR^2\Lambda\cos\theta\left(2\dot\delta + \Lambda\sin\theta\right) = -R\left(F_x\cos\theta + N\sin\theta\right)}$$
>
> $$\boxed{\tfrac14 mR^2\left(\dot\Lambda\cos\theta - \Lambda\dot\theta\sin\theta\right) + \tfrac14 mR^2\,\dot\theta\left(2\dot\delta + \Lambda\sin\theta\right) = 0}$$
>
> **Units:** N m in every equation ($[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$)
> **Meaning:** in the boxed lines the bracket of $I_1$ times $\omega_x$ minus $I_2\Lambda\sin\theta$ is written as $\tfrac14 mR^2$ times twice the rate of $\delta$ plus $\Lambda\sin\theta$. With the three Newton equations and the two rolling conditions of part (c) these are eight scalar equations for the eight unknowns $r$, $\psi$, $\beta$, $\theta$, $\delta$, $N$, $F_x$, $F_y$.

> [!derivation] Part (e): conservation laws
> **Law:** power of a force on a body point; theorem of the mechanical energy; potential of the weight
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> The contact force acts on the body point $C(B)$, whose velocity is zero by the rolling condition; the weight derives from the potential of the momentum box.
>
> $$\begin{aligned}
> P_C &= \left(F_x\,\mathbf x_2 + F_y\,\mathbf y_2 + N\,\mathbf k_1\right)\cdot\mathbf v_0^{C(B)} = 0 \quad &\text{(rolling: zero velocity of the body point)} \\
> \frac{d}{dt}\left(T_0 + V\right) &= P_C = 0 \quad &\text{(Eq. 12.33: only non-potential forces change the energy)}
> \end{aligned}$$
>
> $$\boxed{T_0 + mgR\cos\theta = E_0 \ \text{(constant)}}$$
>
> **Units:** J
> **Meaning:** the mechanical energy is the only simple conserved quantity. The linear momentum is not conserved (the friction is in general nonzero); the angular momentum about $G$ is not (the contact force has a moment about $G$); and its component along the vertical through any fixed point is not either, because the horizontal friction has a moment about that vertical whenever the contact point is not on it. The spin $\omega_x$ is not constant: the first Euler equation shows that the tangential friction changes it. (The rolling disk has two further first integrals, found by Chaplygin and Appell, which are not simple: this remark is an **extension**.) The real Euler's disk does lose energy, through rolling resistance and the air, which is what the next part explains.

![[attachments/EM-SOL/rb28-steady.svg]]

> [!derivation] Part (f): steady motion with G at rest on the vertical through O
> **Law:** the position of part (b) with the data; rolling conditions; Newton and Euler equations with constant tilt
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.5
>
> With $\beta$ zero, $\mathbf x_2$ is $\mathbf i_1$ and $\mathbf y_2$ is $\mathbf j_1$; the rate of $\beta$ is zero, so $\Lambda$ is the rate of $\psi$. The right triangle $C$, $G$, foot of $G$ on the plane (which is $O$): hypotenuse $CG$ of length $R$, vertical leg $h$ (adjacent to $\theta$), horizontal leg $r$ (opposite to $\theta$).
>
> $$\begin{aligned}
> \left(r - R\sin\theta\right)\mathbf i_1 + R\cos\theta\,\mathbf k_0 &= h\,\mathbf k_0 \quad &\text{(position of part (b) with $\beta$ zero)} \\
> r &= R\sin\theta, \qquad h = R\cos\theta \quad &\text{(components; both constant, so $\theta$ and $r$ are constant)} \\
> \theta &= \arccos\frac hR, \qquad r = \sqrt{R^2 - h^2} \quad &\text{(invert; legs of the triangle)} \\
> \dot\delta &= -\frac{r\,\dot\psi}{R} = -\dot\psi\sin\theta \quad &\text{(second rolling condition; the first holds because $r$ is constant and $\beta$ is zero)} \\
> \omega_x &= \dot\delta + \dot\psi\sin\theta = 0, \qquad \omega_y = 0, \qquad \omega_z = \dot\psi\cos\theta \quad &\text{(part (b))} \\
> \mathbf a_0^G &= \mathbf 0 \;\Rightarrow\; F_x = F_y = 0, \quad N = mg \quad &\text{($G$ fixed; Newton's equations)} \\
> \tfrac14 mR^2\,\ddot\psi\cos\theta &= 0 \;\Rightarrow\; \dot\psi = \text{constant} \quad &\text{(moment along $\mathbf z_3$; $\theta$ constant)} \\
> \tfrac14 mR^2\,\dot\psi\cos\theta\left(-2\dot\psi\sin\theta + \dot\psi\sin\theta\right) &= -R\,mg\sin\theta \quad &\text{(moment along $\mathbf y_2$; the spin is minus the rate of $\psi$ times the sine)} \\
> \tfrac14 mR^2\,\dot\psi^2\cos\theta &= mgR \quad &\text{(divide by minus the sine of $\theta$, not zero since $h \lt R$)} \\
> h\,\dot\psi^2 &= 4g \quad &\text{(multiply by 4 over $mR$; $R\cos\theta = h$)}
> \end{aligned}$$
>
> $$\boxed{r = \sqrt{R^2 - h^2}, \qquad \theta = \arccos\frac hR, \qquad N = mg, \qquad F_x = F_y = 0, \qquad h\,\dot\psi^2 = 4g}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-2}}] = [\mathrm{L\,T^{-2}}]$, an acceleration on both sides
> **Meaning:** the angular velocity is along $CG$: the coin turns about the line joining the contact point and the fixed centre, so $G$ stays at rest and the contact point runs round $O$ on a circle of radius $r$ at the constant rate of $\psi$, while the angular velocity has no component along the normal of the coin (the spin of the coin about its own axis cancels against the part of the rate of $\psi$ along that axis), so the face of the coin turns about the vertical only at the small rate of $\psi$ times one minus the sine of $\theta$. No friction is needed: the weight and the normal reaction form a couple, of arm $r$, that turns the angular momentum about the vertical. The lower $G$, the faster the motion: the rate of $\psi$ grows as one over the square root of $h$ and has no bound as the coin lies down. The energy of this motion is $mgh$ plus one eighth of $mh^2$ times the squared rate of $\psi$, that is $\tfrac32 mgh$: a real coin that loses energy slowly passes through these states with decreasing $h$, so its contact point circles faster and faster, the rising whirr of Euler's disk, until it stops abruptly.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom | 5 with slip ($r$, $\psi$, $\beta$, $\theta$, $\delta$); 3 when rolling without slip (5 coordinates, 2 non-integrable conditions) |
| (b) Kinematics | $\boldsymbol\omega = (\dot\delta + \Lambda\sin\theta)\,\mathbf x_3 - \dot\theta\,\mathbf y_2 + \Lambda\cos\theta\,\mathbf z_3$, $\Lambda = \dot\psi + \dot\beta$; $\boldsymbol\alpha$, $\mathbf v^G$, $\mathbf a^G$ in the boxes of part (b); $\mathbf r^G = (r - R\sin\theta\cos\beta)\,\mathbf i_1 - R\sin\theta\sin\beta\,\mathbf j_1 + R\cos\theta\,\mathbf k_0$ |
| (c) Rolling | $\dot r\cos\beta + r\dot\psi\sin\beta = 0$, $-\dot r\sin\beta + r\dot\psi\cos\beta + R\dot\delta = 0$ |
| (d) Forces | weight $-mg\,\mathbf k_1$ at $G$; $N\,\mathbf k_1 + F_x\,\mathbf x_2 + F_y\,\mathbf y_2$ at $C$; $\mathbf M_G = RF_y\,\mathbf x_3 - R(F_x\cos\theta + N\sin\theta)\,\mathbf y_2$ |
| (e) Equations | three Newton equations, three Euler equations (boxes of part (e)) and two rolling conditions; only the mechanical energy $T_0 + mgR\cos\theta$ is conserved |
| (f) Steady motion | $r = \sqrt{R^2 - h^2}$, $\theta = \arccos(h/R)$, $N = mg$, no friction, $h\dot\psi^2 = 4g$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: the steady motion from the energy and the angular momentum
> **Law:** angular momentum of the steady motion; its rate of change as a vector turning about the vertical; moment of the weight and the normal reaction about $G$
> **Source:** Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 9.4
>
> In the steady motion $\mathbf H_G$ is $I_2$ times the rate of $\psi$ times the cosine of $\theta$ along $\mathbf z_3$, a vector of constant length turning about $\mathbf k_1$ at the rate of $\psi$.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G}{dt}\right|_0 &= \dot\psi\,\mathbf k_1\times\left(I_2\,\dot\psi\cos\theta\,\mathbf z_3\right) = I_2\,\dot\psi^2\cos\theta\left(\mathbf k_1\times\mathbf z_3\right) \quad &\text{(Poisson for a vector fixed in $\mathcal B_3$, which turns about $\mathbf k_1$ only)} \\
> \mathbf k_1\times\mathbf z_3 &= \left(\sin\theta\,\mathbf x_3 + \cos\theta\,\mathbf z_3\right)\times\mathbf z_3 = -\sin\theta\,\mathbf y_2 \quad &\text{($\mathbf x_3\times\mathbf z_3 = -\mathbf y_2$)} \\
> \mathbf M_G &= -R\,mg\sin\theta\,\mathbf y_2 \quad &\text{(part (d) with $N = mg$ and no friction)} \\
> -\tfrac14 mR^2\,\dot\psi^2\cos\theta\sin\theta &= -mgR\sin\theta \quad &\text{(equate the components along $\mathbf y_2$)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi^2 = \frac{4g}{R\cos\theta} = \frac{4g}{h}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the gyroscopic argument, with no Euler angle derivative to expand, gives the same relation as part (f).

**Limiting cases and consistency:**

* **Upright coin.** As $h$ tends to $R$, $\theta$ and $r$ tend to zero: the coin stands on its rim at $O$ and spins about its vertical diameter, with the rate of $\psi$ tending to $2\sqrt{g/R}$, the lowest rate allowed by the relation; for the upright coin itself the tipping moment vanishes and any rate is possible.
* **Flat coin.** As $h$ tends to zero the rate of $\psi$ grows without bound while the energy, three halves of $mgh$, tends to zero: in the ideal model the rate of $\psi$ grows without bound as the energy is drained (an **extension**: whether this happens in finite time depends on the dissipation law, which the course does not cover).
* **Numbers.** For $R$ equal to 0.04 m and $h$ equal to 0.01 m, the rate of $\psi$ is $\sqrt{4\cdot 9.81/0.01}$, about 62.6 rad/s (about 10 turns per second), with $\theta$ about 75.5 deg.
* **Dimensions.** Every Newton equation is in N, every Euler equation in N m; both rolling conditions are velocities.

---

## Problem RB-33: Axle with two wheels

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a rigid body $b$ made of two thin homogeneous wheels of surface density $\sigma$, of centres $C_1$ and $C_2$ and radii $a$ and $2a$, joined by a massless axle of length $\sqrt3\,a$ normal to both wheels. Both wheels touch the horizontal ground, at the body points $P$ and $Q$, and roll without slipping. Gravity acts downwards.
* **Fixed frame:** $S_0\{O; \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, with $\mathbf k_0$ vertical upwards and $O$ the point of the ground where the line of the axle meets it (figure). The ground is at rest, so this frame is inertial.
* **Rotating frame:** $S_1\{O; \mathbf i_1, \mathbf j_1, \mathbf k_1\}$, turned by $\psi$ about $\mathbf k_0$, with $\mathbf j_1$ along $OPQ$ on the ground and $\mathbf k_1$ equal to $\mathbf k_0$.
* **Frame of the axle:** $\mathcal B_2$, the basis $\{\mathbf i_2, \mathbf j_2, \mathbf k_2\}$ with $\mathbf i_2$ equal to $\mathbf i_1$ and $\mathbf j_2$ along the axle from $O$ through $C_1$ to $C_2$; it is fixed in $S_1$ (the inclination of the axle is constant, see below).
* **Body basis:** $\mathcal B_3$, the basis $\{\mathbf i_3, \mathbf j_3, \mathbf k_3\}$ with $\mathbf j_3$ equal to $\mathbf j_2$, turned by $\phi$ about the axle; at the initial instant $\mathbf i_3$ points along $C_2Q$. Read from the figure, which shows only the angle between $\mathbf i_3$ and the line $C_2Q$, not its sense: $\phi$ is taken positive about $\mathbf j_2$ (right-hand rule along the axle oriented from $C_1$ to $C_2$). With the opposite sense the rolling condition only changes its sign (the box of part (c) gives the result) and nothing else changes, because $\phi$ is eliminated before the dynamics.
* **Degrees of freedom:** a free body has six coordinates. Contact of both wheels with the ground gives two conditions (Notes.pdf, Eq. 13.1); they fix the height and the inclination of the axle. Of the four remaining coordinates, the two coordinates of $O$ on the ground stay constant in the motion, as the figure takes them (rolling at $P$ and $Q$ forbids any velocity of the apex of the cone that the wheels define); the angles $\psi$ and $\phi$ remain. Rolling adds one relation between them (part (c)): the body has **one degree of freedom**.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Surface density of the wheels | $\sigma$ | kg/m$^2$ |
| Radius of the small wheel (centre $C_1$) | $a$ | m |
| Radius of the large wheel (centre $C_2$) | $2a$ | m |
| Length of the axle, massless, normal to both wheels | $\sqrt3\,a$ | m |
| Angles | $\psi$ (about $\mathbf k_0$), $\phi$ (about the axle) | rad |
| Initial state | $\psi = 0$, $\phi = 0$, $\mathbf i_3$ along $C_2Q$ | rad |
| Gravity | $g$, along $-\mathbf k_0$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb33-rot-psi.svg]]

> [!derivation] Rotating basis: rotation by psi about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View from above with $\mathbf k_0$ out of the paper (⊙). In the figure $\mathbf j_0$ is turned into $\mathbf j_1$ (and $\mathbf i_0$ into $\mathbf i_1$) by a counterclockwise turn seen from above, a positive rotation about $\mathbf k_0$. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\psi$), opposite leg along $\mathbf j_0$ (sine). Triangle of $\mathbf j_1$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= \dot\psi\,\mathbf k_0, \qquad \dot{\mathbf i}_1 = \dot\psi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = -\dot\psi\,\mathbf i_1 \quad &\text{(Poisson: $\mathbf k_0\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_0\times\mathbf j_1 = -\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $S_1$ carries the vertical plane that contains the axle and the two contact points.

![[attachments/EM-SOL/rb33-cone.svg]]

> [!derivation] Geometry of the axle and rotation by 30 deg about i1
> **Law:** lowest point of a wheel normal to its axle; similar right triangles; simple rotation about the first axis
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2
>
> The lowest point of a wheel lies in the vertical plane through its axis, so $C_1$, $C_2$, $P$, $Q$ lie in the vertical plane of $\mathbf j_1$ and $\mathbf k_1$; $C_1P$ and $C_2Q$ are radii, normal to the axle in that plane, hence parallel. The axle line meets the ground at $O$ (hint: $O$, $C_1$, $C_2$ aligned). View of that plane with $\mathbf j_1$ to the right and $\mathbf k_1$ up; the product of $\mathbf j_1$ and $\mathbf k_1$ is $\mathbf i_1$, so $\mathbf i_1$ points out of the paper (⊙) and a positive rotation about it looks counterclockwise. Right triangle $OC_1P$: right angle at $C_1$, adjacent leg $OC_1$ along the axle, opposite leg $C_1P$ of length $a$, hypotenuse $OP$ on the ground; $\gamma$ is the angle at $O$. Right triangle $OC_2Q$: the same angle, opposite leg $2a$.
>
> $$\begin{aligned}
> \frac{a}{OC_1} &= \frac{2a}{OC_1 + \sqrt3\,a} \;\Rightarrow\; OC_1 = \sqrt3\,a, \qquad OC_2 = 2\sqrt3\,a \quad &\text{(similar triangles; $OC_2$ is $OC_1$ plus the axle)} \\
> \tan\gamma &= \frac{a}{\sqrt3\,a} = \frac{1}{\sqrt3} \;\Rightarrow\; \gamma = \frac\pi6, \qquad OP = \sqrt{3a^2 + a^2} = 2a, \qquad OQ = 4a \quad &\text{(opposite over adjacent; Pythagoras)} \\
> \mathbf j_2 &= \cos\gamma\,\mathbf j_1 + \sin\gamma\,\mathbf k_1 = \frac{\sqrt3}{2}\,\mathbf j_1 + \frac12\,\mathbf k_1 \quad &\text{(triangle of $\mathbf j_2$: adjacent leg along $\mathbf j_1$, opposite leg along $\mathbf k_1$)} \\
> \mathbf k_2 &= -\sin\gamma\,\mathbf j_1 + \cos\gamma\,\mathbf k_1 = -\frac12\,\mathbf j_1 + \frac{\sqrt3}{2}\,\mathbf k_1 \quad &\text{(counterclockwise turn: the tip of $\mathbf k_1$ moves to minus $\mathbf j_1$)} \\
> [{}_1R_2] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \tfrac{\sqrt3}{2} & -\tfrac12 \cr 0 & \tfrac12 & \tfrac{\sqrt3}{2} \end{bmatrix}, \qquad \det[{}_1R_2] = \frac34 + \frac14 = 1 \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$; expand along the first row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \tfrac34 + \tfrac14 & \tfrac{\sqrt3}{4} - \tfrac{\sqrt3}{4} \cr 0 & \tfrac{\sqrt3}{4} - \tfrac{\sqrt3}{4} & \tfrac14 + \tfrac34 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_1 &= \frac{\sqrt3}{2}\,\mathbf j_2 - \frac12\,\mathbf k_2, \qquad \mathbf k_1 = \frac12\,\mathbf j_2 + \frac{\sqrt3}{2}\,\mathbf k_2 \quad &\text{(rows: the inverse is the transpose)} \\
> \overrightarrow{C_1P} &= -a\,\mathbf k_2, \qquad \overrightarrow{C_2Q} = -2a\,\mathbf k_2 \quad &\text{(radii normal to the axle, pointing down in the plane)}
> \end{aligned}$$
>
> $$\boxed{OC_1 = \sqrt3\,a, \quad OC_2 = 2\sqrt3\,a, \quad OP = 2a, \quad OQ = 4a, \quad \gamma = \frac\pi6, \quad \mathbf j_2 = \frac{\sqrt3}{2}\,\mathbf j_1 + \frac12\,\mathbf k_1, \quad \mathbf k_2 = -\frac12\,\mathbf j_1 + \frac{\sqrt3}{2}\,\mathbf k_1}$$
>
> **Units:** lengths in $[\mathrm L]$; dimensionless basis
> **Meaning:** the wheels behave as two sections of a cone with its apex at $O$ and half-angle 30 deg; the axle stays 30 deg above the ground, so $\mathcal B_2$ is fixed in $S_1$. Check: $\sqrt3 a\,\mathbf j_2$ minus $a\,\mathbf k_2$ is $2a\,\mathbf j_1$, the point $P$ on the ground.

![[attachments/EM-SOL/rb33-rot-phi.svg]]

> [!derivation] Body basis: rotation by phi about the axle
> **Law:** simple rotation about the second axis; right-hand rule with the axis into the paper
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2
>
> View along the axle from $O$, with $\mathbf j_2$ pointing into the paper (⊗), $\mathbf i_2$ to the right and $\mathbf k_2$ up; this is right-handed because the product of $\mathbf i_2$ and $\mathbf k_2$ is minus $\mathbf j_2$, and a positive rotation about an axis pointing into the paper looks clockwise. At $\phi$ zero the body basis is $\{-\mathbf k_2, \mathbf j_2, \mathbf i_2\}$ ($\mathbf i_3$ along $C_2Q$; the product of $-\mathbf k_2$ and $\mathbf j_2$ is $\mathbf i_2$). The clockwise turn by $\phi$ carries the tip of $-\mathbf k_2$ towards $-\mathbf i_2$. Triangle of $\mathbf i_3$: hypotenuse 1, adjacent leg along minus $\mathbf k_2$ (cosine of $\phi$), opposite leg along minus $\mathbf i_2$ (sine). Triangle of $\mathbf k_3$: adjacent leg along $\mathbf i_2$ (cosine), opposite leg along minus $\mathbf k_2$ (sine).
>
> $$\begin{aligned}
> \mathbf i_3 &= -\sin\phi\,\mathbf i_2 - \cos\phi\,\mathbf k_2, \qquad \mathbf j_3 = \mathbf j_2, \qquad \mathbf k_3 = \cos\phi\,\mathbf i_2 - \sin\phi\,\mathbf k_2 \quad &\text{(legs of the two triangles)} \\
> [{}_2R_3] &= \begin{bmatrix} -\sin\phi & 0 & \cos\phi \cr 0 & 1 & 0 \cr -\cos\phi & 0 & -\sin\phi \end{bmatrix} \quad &\text{(columns: $\mathbf i_3$, $\mathbf j_3$, $\mathbf k_3$ in $\mathcal B_2$)} \\
> \det[{}_2R_3] &= 1\cdot\left(\left(-\sin\phi\right)\left(-\sin\phi\right) - \cos\phi\left(-\cos\phi\right)\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_2R_3][{}_2R_3]^T &= \begin{bmatrix} \sin^2\phi + \cos^2\phi & 0 & \sin\phi\cos\phi - \cos\phi\sin\phi \cr 0 & 1 & 0 \cr \cos\phi\sin\phi - \sin\phi\cos\phi & 0 & \cos^2\phi + \sin^2\phi \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{32} &= \dot\phi\,\mathbf j_2, \qquad \boldsymbol\omega_{21} = \mathbf 0 \quad &\text{(rotation about the axle; $\mathcal B_2$ fixed in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_3 = -\sin\phi\,\mathbf i_2 - \cos\phi\,\mathbf k_2, \qquad \mathbf k_3 = \cos\phi\,\mathbf i_2 - \sin\phi\,\mathbf k_2, \qquad \boldsymbol\omega_{32} = \dot\phi\,\mathbf j_2}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\phi$ only marks the turn of the wheels about the axle; the wheels are bodies of revolution about $\mathbf j_2$, so the inertia tensor will not depend on it.

> [!derivation] Part (b): angular velocity and angular acceleration
> **Law:** composition of angular velocities; derivative of a vector with components in the rotating basis $\mathcal B_1$ (Coriolis theorem)
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.8; Notes.pdf, Sec. 15.1
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{32} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\phi\,\mathbf j_2 + \dot\psi\,\mathbf k_1 \quad &\text{(composition, Eq. 9.21)} \\
> &= \frac{\sqrt3}{2}\,\dot\phi\,\mathbf j_1 + \left(\dot\psi + \frac12\,\dot\phi\right)\mathbf k_1 \quad &\text{($\mathbf j_2$ in $\mathcal B_1$)} \\
> \boldsymbol\alpha_{b0} &= \left.\frac{d\boldsymbol\omega_{b0}}{dt}\right|_1 + \dot\psi\,\mathbf k_1\times\boldsymbol\omega_{b0} = \frac{\sqrt3}{2}\,\ddot\phi\,\mathbf j_1 + \left(\ddot\psi + \frac12\,\ddot\phi\right)\mathbf k_1 + \dot\psi\,\frac{\sqrt3}{2}\,\dot\phi\,\mathbf k_1\times\mathbf j_1 \quad &\text{(Coriolis theorem with $S_1$, Eq. 3.8)} \\
> &= -\frac{\sqrt3}{2}\,\dot\psi\dot\phi\,\mathbf i_1 + \frac{\sqrt3}{2}\,\ddot\phi\,\mathbf j_1 + \left(\ddot\psi + \frac12\,\ddot\phi\right)\mathbf k_1 \quad &\text{($\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \frac{\sqrt3}{2}\,\dot\phi\,\mathbf j_1 + \left(\dot\psi + \frac{\dot\phi}{2}\right)\mathbf k_1, \qquad \boldsymbol\alpha_{b0} = -\frac{\sqrt3}{2}\,\dot\psi\dot\phi\,\mathbf i_1 + \frac{\sqrt3}{2}\,\ddot\phi\,\mathbf j_1 + \left(\ddot\psi + \frac{\ddot\phi}{2}\right)\mathbf k_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the term along $\mathbf i_1$ appears because the spin vector along the axle is carried round the vertical by the rate of $\psi$.

> [!derivation] Part (b): position, velocity and acceleration of G
> **Law:** position along the axle; derivative of a vector written in the rotating basis $\mathcal B_1$; Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> $G$ lies on the axle at $\tfrac45\sqrt3\,a$ from $C_1$ (centre of mass box below), so at $\sqrt3 a$ plus that distance from $O$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \left(\sqrt3\,a + \frac45\sqrt3\,a\right)\mathbf j_2 = \frac{9\sqrt3}{5}\,a\,\mathbf j_2 \quad &\text{(sum of segments along the axle)} \\
> &= \frac{9\sqrt3}{5}\,a\left(\frac{\sqrt3}{2}\,\mathbf j_1 + \frac12\,\mathbf k_1\right) = \frac{27}{10}\,a\,\mathbf j_1 + \frac{9\sqrt3}{10}\,a\,\mathbf k_1 \quad &\text{($\mathbf j_2$ in $\mathcal B_1$)} \\
> \mathbf v_0^G &= \frac{27}{10}\,a\,\dot{\mathbf j}_1 = -\frac{27}{10}\,a\,\dot\psi\,\mathbf i_1 \quad &\text{(constant components; Poisson)} \\
> \mathbf a_0^G &= -\frac{27}{10}\,a\left(\ddot\psi\,\mathbf i_1 + \dot\psi\,\dot{\mathbf i}_1\right) = -\frac{27}{10}\,a\left(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1\right) \quad &\text{(product rule; Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \frac{27}{10}\,a\,\mathbf j_1 + \frac{9\sqrt3}{10}\,a\,\mathbf k_1, \qquad \mathbf v_0^G = -\frac{27}{10}\,a\,\dot\psi\,\mathbf i_1, \qquad \mathbf a_0^G = -\frac{27}{10}\,a\left(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1\right)}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}]$
> **Meaning:** $G$ moves on a horizontal circle of radius $\tfrac{27}{10}a$ about the vertical through $O$, at the constant height $\tfrac{9\sqrt3}{10}a$ (about 1.56 times $a$); the term along minus $\mathbf j_1$ is the centripetal acceleration, towards the axis.

> [!derivation] Part (c): rolling without slip at P and Q
> **Law:** velocity field of the rigid body; rolling without slipping on the ground at rest; integration with Barrow's rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> The velocity of $C_1$ follows from its position $\sqrt3 a\,\mathbf j_2$, that is $\tfrac32 a\,\mathbf j_1$ plus $\tfrac{\sqrt3}{2}a\,\mathbf k_1$, exactly as for $G$. Products needed: $\mathbf j_1\times\mathbf k_2$ is $\tfrac{\sqrt3}{2}\mathbf i_1$ and $\mathbf k_1\times\mathbf k_2$ is $\tfrac12\mathbf i_1$ (from $\mathbf k_2$ in $\mathcal B_1$).
>
> $$\begin{aligned}
> \mathbf v_0^{C_1} &= -\frac32\,a\,\dot\psi\,\mathbf i_1 \quad &\text{(Poisson on $\mathbf j_1$)} \\
> \boldsymbol\omega_{b0}\times\overrightarrow{C_1P} &= -a\left[\frac{\sqrt3}{2}\,\dot\phi\,\mathbf j_1\times\mathbf k_2 + \left(\dot\psi + \frac{\dot\phi}{2}\right)\mathbf k_1\times\mathbf k_2\right] = -a\left(\frac34\,\dot\phi + \frac12\,\dot\psi + \frac14\,\dot\phi\right)\mathbf i_1 \quad &\text{($\overrightarrow{C_1P} = -a\,\mathbf k_2$; distribute)} \\
> \mathbf v_0^{P(b)} &= \mathbf v_0^{C_1} + \boldsymbol\omega_{b0}\times\overrightarrow{C_1P} = -a\left(2\,\dot\psi + \dot\phi\right)\mathbf i_1 \quad &\text{(velocity field, Eq. 9.3; collect)} \\
> \mathbf v_0^{Q(b)} &= -3a\,\dot\psi\,\mathbf i_1 - 2a\left(\dot\phi + \frac12\,\dot\psi\right)\mathbf i_1 = -2a\left(2\,\dot\psi + \dot\phi\right)\mathbf i_1 \quad &\text{(same steps from $C_2$, with $2\sqrt3 a\,\mathbf j_2$ and $-2a\,\mathbf k_2$)} \\
> 2\,\dot\psi + \dot\phi &= 0 \quad &\text{(no slip at $P$ and at $Q$, Eq. 13.5: the same condition)} \\
> \int_0^{\phi} d\phi' &= -2\int_0^{\psi} d\psi' \;\Rightarrow\; \left[\phi'\right]_0^{\phi} = -2\left[\psi'\right]_0^{\psi} \;\Rightarrow\; \phi = -2\,\psi \quad &\text{(separate; antiderivatives; Barrow's rule with both initial values zero)} \\
> \boldsymbol\omega_{b0} &= -\sqrt3\,\dot\psi\,\mathbf j_1, \qquad \boldsymbol\alpha_{b0} = \sqrt3\,\dot\psi^2\,\mathbf i_1 - \sqrt3\,\ddot\psi\,\mathbf j_1 \quad &\text{(part (b) with the rate of $\phi$ equal to minus twice the rate of $\psi$)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi = -2\,\dot\psi, \qquad \phi = -2\,\psi, \qquad \boldsymbol\omega_{b0} = -\sqrt3\,\dot\psi\,\mathbf j_1, \qquad \boldsymbol\alpha_{b0} = \sqrt3\left(\dot\psi^2\,\mathbf i_1 - \ddot\psi\,\mathbf j_1\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the two contact conditions coincide because both contact points lie on the generatrix $OPQ$ of the same cone: once the vertical component of the angular velocity cancels, the angular velocity lies along $OPQ$, the instantaneous axis, and every point of that line (also $O$) is at rest. The wheels turn twice as fast as the axle goes round, in the sense of minus $\mathbf j_2$ (with the opposite convention for $\phi$, the relation would read $\phi$ equal to $2\psi$).

### Center of Mass and Inertia Tensor

> [!derivation] Part (a): mass and centre of mass
> **Law:** homogeneous plates: mass equal to density times area; centre of mass of a system as the mass-weighted mean
> **Source:** Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.8; Notes.pdf, Eq. 13.11; [Lecture 8, Slide 17]
>
> Each wheel is symmetric about its centre; the axle is massless.
>
> $$\begin{aligned}
> m_1 &= \sigma\pi a^2, \qquad m_2 = \sigma\pi\left(2a\right)^2 = 4\sigma\pi a^2 \quad &\text{(areas of the wheels)} \\
> m &= m_1 + m_2 = 5\sigma\pi a^2, \qquad m_1 = \frac m5, \quad m_2 = \frac{4m}{5} \quad &\text{(sum)} \\
> m\,\overrightarrow{C_1G} &= m_1\,\mathbf 0 + m_2\,\sqrt3\,a\,\mathbf j_2 \quad &\text{(first moments about $C_1$, Eq. 13.11)} \\
> \overrightarrow{C_1G} &= \frac45\sqrt3\,a\,\mathbf j_2, \qquad \overrightarrow{GC_2} = \frac15\sqrt3\,a\,\mathbf j_2 \quad &\text{(divide by $m$; the rest of the axle)}
> \end{aligned}$$
>
> $$\boxed{m = 5\pi\sigma a^2, \qquad \left|C_1G\right| = \frac{4\sqrt3}{5}\,a \approx 1.386\,a}$$
>
> **Units:** kg; m
> **Meaning:** the large wheel has four times the mass of the small one, so $G$ is four fifths of the way from $C_1$ to $C_2$.

> [!derivation] Part (a): inertia tensor of one thin wheel about its centre
> **Law:** moments and products of inertia as area integrals in polar coordinates (jacobian $\rho$)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; Notes.pdf, Eq. 10.5; [Lecture 8, Slide 16]
>
> A wheel of mass $M$, radius $L$, centre $C$, in the plane of $\mathbf i_2$ and $\mathbf k_2$, normal $\mathbf j_2$. Polar coordinates $(\rho, \chi)$ with $\rho\cos\chi$ along $\mathbf i_2$ and $\rho\sin\chi$ along $\mathbf k_2$; area element $\rho\,d\rho\,d\chi$; $M$ is $\sigma\pi L^2$.
>
> $$\begin{aligned}
> I_{yy} &= \sigma\int_0^{2\pi}\int_0^{L}\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^{L} = \frac{\sigma\pi L^4}{2} = \frac{ML^2}{2} \quad &\text{(normal axis: squared distance $\rho^2$; Barrow's rule)} \\
> I_{xx} &= \sigma\int_0^{2\pi}\sin^2\chi\,d\chi\int_0^{L}\rho^3\,d\rho = \sigma\left[\frac\chi2 - \frac{\sin 2\chi}{4}\right]_0^{2\pi}\frac{L^4}{4} = \sigma\pi\,\frac{L^4}{4} = \frac{ML^2}{4} \quad &\text{(axis $\mathbf i_2$: squared distance $\rho^2\sin^2\chi$; Barrow's rule)} \\
> I_{zz} &= \sigma\left[\frac\chi2 + \frac{\sin 2\chi}{4}\right]_0^{2\pi}\frac{L^4}{4} = \frac{ML^2}{4} \quad &\text{(axis $\mathbf k_2$: squared distance $\rho^2\cos^2\chi$)} \\
> I_{xz} &= \sigma\int_0^{2\pi}\sin\chi\cos\chi\,d\chi\int_0^{L}\rho^3\,d\rho = \sigma\left[\frac{\sin^2\chi}{2}\right]_0^{2\pi}\frac{L^4}{4} = 0 \quad &\text{(product; the products with the normal coordinate are zero, Eq. 10.15)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_C = \frac{ML^2}{4}\begin{bmatrix} 1 & 0 & 0 \cr 0 & 2 & 0 \cr 0 & 0 & 1 \end{bmatrix} \ \text{in } \mathcal B_2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** this is the tensor of the hint of the statement, recovered from its integrals.

> [!derivation] Part (a): inertia tensor of the body about G
> **Law:** Steiner's theorem for each wheel; additivity
> **Source:** Notes.pdf, Eq. 10.48; Notes.pdf, Sec. 10.8.1; [Lecture 8, Slide 18]
>
> Each centre is displaced from $G$ along $\mathbf j_2$ only, by $d_1$ for $C_1$ and $d_2$ for $C_2$. Steiner's theorem adds to the central tensor of each wheel its mass times the square of the displacement on the diagonal terms of the two axes normal to the displacement ($\mathbf i_2$ and $\mathbf k_2$), nothing on the axis of the displacement, and no products (the displacement has one component only).
>
> $$\begin{aligned}
> d_1^2 &= \left(\frac{4\sqrt3}{5}\,a\right)^2 = \frac{48}{25}\,a^2, \qquad d_2^2 = \left(\frac{\sqrt3}{5}\,a\right)^2 = \frac{3}{25}\,a^2 \quad &\text{(distances from $G$)} \\
> A &= \frac{m_1 a^2}{4} + m_1 d_1^2 + \frac{m_2\left(2a\right)^2}{4} + m_2 d_2^2 \quad &\text{(Eq. 10.48 for the axes $\mathbf i_2$ and $\mathbf k_2$)} \\
> &= m a^2\left(\frac{1}{20} + \frac{48}{125} + \frac45 + \frac{12}{125}\right) = m a^2\,\frac{25 + 192 + 400 + 48}{500} = \frac{133}{100}\,m a^2 \quad &\text{(masses $m/5$ and $4m/5$; common denominator)} \\
> B &= \frac{m_1 a^2}{2} + \frac{m_2\left(2a\right)^2}{2} = m a^2\left(\frac{1}{10} + \frac85\right) = \frac{17}{10}\,m a^2 \quad &\text{(axis of the displacement: no Steiner term)} \\
> [{}_2R_3]^T\,\mathrm{diag}\left(A, B, A\right)[{}_2R_3] &= \mathrm{diag}\left(A\sin^2\phi + A\cos^2\phi,\ B,\ A\cos^2\phi + A\sin^2\phi\right) \quad &\text{(same matrix in $\mathcal B_3$: the off-diagonal terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_G = \begin{bmatrix} A & 0 & 0 \cr 0 & B & 0 \cr 0 & 0 & A \end{bmatrix} \text{ in } \mathcal B_2 \text{ and } \mathcal B_3, \qquad A = \frac{133}{100}\,ma^2, \qquad B = \frac{17}{10}\,ma^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the body is a body of revolution about the axle, so the tensor has the same matrix in the basis $\mathcal B_2$, which does not spin; $A$ is smaller than $B$ here, although the wheels sit apart along the axle.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and its derivative, kinetic energy
> **Law:** linear momentum from $G$; angular momentum from the tensor; derivative in the rotating basis $\mathcal B_2$ (Coriolis theorem); Koenig's decomposition
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 3.8; [Lecture 9, Slide 5]
>
> With rolling, the angular velocity is minus $\sqrt3$ times the rate of $\psi$ along $\mathbf j_1$, and $\mathbf j_1$ is $\tfrac{\sqrt3}{2}\mathbf j_2$ minus $\tfrac12\mathbf k_2$. The basis $\mathcal B_2$ turns at $\dot\psi\,\mathbf k_1$, with $\mathbf k_1$ equal to $\tfrac12\mathbf j_2$ plus $\tfrac{\sqrt3}{2}\mathbf k_2$.
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = -\frac{27}{10}\,m\,a\,\dot\psi\,\mathbf i_1 \quad &\text{(Eq. 11.3)} \\
> \boldsymbol\omega_{b0} &= -\frac32\,\dot\psi\,\mathbf j_2 + \frac{\sqrt3}{2}\,\dot\psi\,\mathbf k_2 \quad &\text{($\mathbf j_1$ in $\mathcal B_2$)} \\
> \mathbf H_G &= -\frac32\,B\,\dot\psi\,\mathbf j_2 + \frac{\sqrt3}{2}\,A\,\dot\psi\,\mathbf k_2 \quad &\text{(Eq. 11.12 with the diagonal tensor)} \\
> \dot\psi\,\mathbf k_1\times\mathbf H_G &= \dot\psi\begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr 0 & \tfrac12 & \tfrac{\sqrt3}{2} \cr 0 & -\tfrac32 B\dot\psi & \tfrac{\sqrt3}{2} A\dot\psi \end{vmatrix} = \dot\psi^2\left(\frac{\sqrt3}{4}\,A + \frac{3\sqrt3}{4}\,B\right)\mathbf i_2 \quad &\text{(expand along the first row)} \\
> \left.\frac{d\mathbf H_G}{dt}\right|_0 &= -\frac32\,B\,\ddot\psi\,\mathbf j_2 + \frac{\sqrt3}{2}\,A\,\ddot\psi\,\mathbf k_2 + \frac{\sqrt3}{4}\left(A + 3B\right)\dot\psi^2\,\mathbf i_2 \quad &\text{(Coriolis theorem with $\mathcal B_2$, Eq. 3.8)} \\
> -\frac32\,B\,\ddot\psi\,\mathbf j_2 + \frac{\sqrt3}{2}\,A\,\ddot\psi\,\mathbf k_2 &= -\frac{\sqrt3}{4}\left(A + 3B\right)\ddot\psi\,\mathbf j_1 + \frac34\left(A - B\right)\ddot\psi\,\mathbf k_1 \quad &\text{($\mathbf j_2$ and $\mathbf k_2$ in $\mathcal B_1$; collect)} \\
> T_0 &= \frac12\,m\left(\frac{27}{10}\,a\,\dot\psi\right)^2 + \frac12\left(\frac94\,B + \frac34\,A\right)\dot\psi^2 = \frac{969}{160}\,m\,a^2\,\dot\psi^2 \quad &\text{(Eq. 11.31; values of $A$ and $B$)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_G}{dt}\right|_0 = \frac{\sqrt3}{4}\left(A + 3B\right)\dot\psi^2\,\mathbf i_1 - \frac{\sqrt3}{4}\left(A + 3B\right)\ddot\psi\,\mathbf j_1 + \frac34\left(A - B\right)\ddot\psi\,\mathbf k_1, \qquad T_0 = \frac{969}{160}\,ma^2\dot\psi^2}$$
>
> **Units:** N m; J
> **Meaning:** even at a constant rate of $\psi$ the angular momentum changes: its horizontal part is carried round the vertical, which needs a moment along $\mathbf i_1$ (the gyroscopic term). With the numbers, $A + 3B$ is $\tfrac{643}{100}ma^2$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb33-fbd.svg]]

| Force on the body | Point of application | Expression in $\mathcal B_1$ | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf k_1$ | applied |
| Contact force of the ground on the small wheel | $P$ | $X_P\,\mathbf i_1 + Y_P\,\mathbf j_1 + N_P\,\mathbf k_1$, $N_P \ge 0$ | constraint |
| Contact force of the ground on the large wheel | $Q$ | $X_Q\,\mathbf i_1 + Y_Q\,\mathbf j_1 + N_Q\,\mathbf k_1$, $N_Q \ge 0$ | constraint |

> [!derivation] Part (d): resultant force and moment about G
> **Law:** sum of forces; moment about $G$ of each contact force by a determinant
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \overrightarrow{GP} &= 2a\,\mathbf j_1 - \frac{27}{10}\,a\,\mathbf j_1 - \frac{9\sqrt3}{10}\,a\,\mathbf k_1 = -\frac{7}{10}\,a\,\mathbf j_1 - \frac{9\sqrt3}{10}\,a\,\mathbf k_1, \qquad \overrightarrow{GQ} = \frac{13}{10}\,a\,\mathbf j_1 - \frac{9\sqrt3}{10}\,a\,\mathbf k_1 \quad &\text{(head minus tail)} \\
> \overrightarrow{GP}\times\mathbf F_P &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr 0 & -\tfrac{7}{10}a & -\tfrac{9\sqrt3}{10}a \cr X_P & Y_P & N_P \end{vmatrix} = \frac{a}{10}\left[\left(-7N_P + 9\sqrt3\,Y_P\right)\mathbf i_1 - 9\sqrt3\,X_P\,\mathbf j_1 + 7X_P\,\mathbf k_1\right] \quad &\text{(expand along the first row)} \\
> \overrightarrow{GQ}\times\mathbf F_Q &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr 0 & \tfrac{13}{10}a & -\tfrac{9\sqrt3}{10}a \cr X_Q & Y_Q & N_Q \end{vmatrix} = \frac{a}{10}\left[\left(13N_Q + 9\sqrt3\,Y_Q\right)\mathbf i_1 - 9\sqrt3\,X_Q\,\mathbf j_1 - 13X_Q\,\mathbf k_1\right] \quad &\text{(expand along the first row)} \\
> \mathbf F &= \left(X_P + X_Q\right)\mathbf i_1 + \left(Y_P + Y_Q\right)\mathbf j_1 + \left(N_P + N_Q - mg\right)\mathbf k_1 \quad &\text{(sum; the weight acts at $G$ and has no moment)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_G = \frac{a}{10}\left[\left(13N_Q - 7N_P + 9\sqrt3\left(Y_P + Y_Q\right)\right)\mathbf i_1 - 9\sqrt3\left(X_P + X_Q\right)\mathbf j_1 + \left(7X_P - 13X_Q\right)\mathbf k_1\right]}$$
>
> **Units:** N; N m
> **Meaning:** the radial friction forces $Y_P$ and $Y_Q$ act on the same line $OPQ$, so they enter the resultant and the moment only through their sum.

> [!derivation] Part (e): the six equations of motion
> **Law:** Newton's second law for the centre of mass; moment equation about $G$
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole.
>
> $$\begin{aligned}
> -\frac{27}{10}\,m\,a\,\ddot\psi &= X_P + X_Q \quad &\text{(force along $\mathbf i_1$)} \\
> -\frac{27}{10}\,m\,a\,\dot\psi^2 &= Y_P + Y_Q \quad &\text{(force along $\mathbf j_1$)} \\
> 0 &= N_P + N_Q - mg \quad &\text{(force along $\mathbf k_1$)} \\
> \frac{\sqrt3}{4}\left(A + 3B\right)\dot\psi^2 &= \frac{a}{10}\left(13N_Q - 7N_P + 9\sqrt3\left(Y_P + Y_Q\right)\right) \quad &\text{(moment along $\mathbf i_1$)} \\
> -\frac{\sqrt3}{4}\left(A + 3B\right)\ddot\psi &= -\frac{9\sqrt3}{10}\,a\left(X_P + X_Q\right) \quad &\text{(moment along $\mathbf j_1$)} \\
> \frac34\left(A - B\right)\ddot\psi &= \frac{a}{10}\left(7X_P - 13X_Q\right) \quad &\text{(moment along $\mathbf k_1$)}
> \end{aligned}$$
>
> $$\boxed{\text{the six scalar equations above, with } A = \frac{133}{100}\,ma^2, \ B = \frac{17}{10}\,ma^2 \text{ and } \phi = -2\psi}$$
>
> **Units:** N for the forces; N m for the moments
> **Meaning:** the only coordinate left is $\psi$; the other unknowns are the contact components.

> [!derivation] Reduction: uniform rotation and the contact forces
> **Law:** elimination between the six equations
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> -\frac{\sqrt3}{4}\left(A + 3B\right)\ddot\psi &= \frac{9\sqrt3}{10}\cdot\frac{27}{10}\,m\,a^2\,\ddot\psi \quad &\text{(moment along $\mathbf j_1$ with the force along $\mathbf i_1$)} \\
> \sqrt3\,\ddot\psi\left(\frac{A + 3B}{4} + \frac{243}{100}\,ma^2\right) &= 0 \;\Rightarrow\; \ddot\psi = 0 \quad &\text{(the bracket is positive)} \\
> X_P + X_Q &= 0, \qquad 7X_P - 13X_Q = 0 \;\Rightarrow\; X_P = X_Q = 0 \quad &\text{(force along $\mathbf i_1$; moment along $\mathbf k_1$)} \\
> 13\left(mg - N_P\right) - 7N_P &= \frac{10}{a}\left[\frac{\sqrt3}{4}\left(A + 3B\right)\dot\psi^2 + \frac{9\sqrt3}{10}\cdot\frac{27}{10}\,m\,a^2\dot\psi^2\right] \quad &\text{(moment along $\mathbf i_1$ with $N_Q = mg - N_P$ and the sum of $Y$)} \\
> 20\,N_P &= 13\,mg - \sqrt3\,a\,\dot\psi^2\,m\left(\frac{10}{4}\cdot\frac{643}{100} + \frac{243}{10}\right) = 13\,mg - \frac{323\sqrt3}{8}\,m\,a\,\dot\psi^2 \quad &\text{(value of $A + 3B$; $16.075 + 24.3 = 40.375$)} \\
> N_P &= \frac{m}{160}\left(104\,g - 323\sqrt3\,a\,\dot\psi^2\right), \qquad N_Q = \frac{m}{160}\left(56\,g + 323\sqrt3\,a\,\dot\psi^2\right) \quad &\text{(divide by 20; vertical force)}
> \end{aligned}$$
>
> $$\boxed{\ddot\psi = 0, \quad X_P = X_Q = 0, \quad Y_P + Y_Q = -\frac{27}{10}\,ma\dot\psi^2, \quad N_P = \frac{m}{160}\left(104g - 323\sqrt3\,a\dot\psi^2\right), \quad N_Q = mg - N_P}$$
>
> **Units:** N for every force ($m$ times $a$ times a squared rate is a force)
> **Meaning:** the body goes round at a constant rate fixed by the initial condition. At rest the ground carries thirteen twentieths of the weight on the small wheel, because $G$ is horizontally closer to $P$ (0.7 times $a$) than to $Q$ (1.3 times $a$). As the rate grows, the gyroscopic moment and the moment of the centripetal force about $G$ both transfer load to the outer, large wheel.

> [!derivation] Part (f): maximum rate with both wheels on the ground
> **Law:** unilateral contact: the normal reaction cannot be negative
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.1; Problems.pdf, p. 81
>
> $N_Q$ is always positive, so the small wheel is the one that can leave the ground.
>
> $$\begin{aligned}
> N_P &\ge 0 \iff 104\,g - 323\sqrt3\,a\,\dot\psi^2 \ge 0 \quad &\text{(reduction box)} \\
> \dot\psi^2 &\le \frac{104\,g}{323\sqrt3\,a} = \frac{104\sqrt3}{969}\,\frac ga \approx 0.1859\,\frac ga \quad &\text{(solve; rationalise)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi_{\max}^2 = \frac{104\,g}{323\sqrt3\,a}, \qquad \left|\dot\psi\right|_{\max} \approx 0.431\sqrt{\frac ga}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]/[\mathrm L] = [\mathrm{T^{-2}}]$
> **Meaning:** for $a$ equal to 0.1 m the limit is about 4.27 rad/s, about 0.68 turns of the axle round $O$ per second.

> [!derivation] Part (g): mechanical energy
> **Law:** power of the forces on the body; contact forces on body points at rest; weight acting at a point that moves horizontally
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.5
>
> $$\begin{aligned}
> P_P &= \mathbf F_P\cdot\mathbf v_0^{P(b)} = 0, \qquad P_Q = \mathbf F_Q\cdot\mathbf v_0^{Q(b)} = 0 \quad &\text{(rolling: zero velocity of the contact body points)} \\
> P_W &= -mg\,\mathbf k_1\cdot\mathbf v_0^G = -mg\,\mathbf k_1\cdot\left(-\frac{27}{10}\,a\,\dot\psi\,\mathbf i_1\right) = 0 \quad &\text{(the velocity of $G$ is horizontal)} \\
> \frac{dT_0}{dt} &= \frac{969}{80}\,ma^2\,\dot\psi\,\ddot\psi = P_P + P_Q + P_W = 0 \quad &\text{(theorem of the kinetic energy; chain rule)}
> \end{aligned}$$
>
> $$\boxed{T_0 + V = \frac{969}{160}\,ma^2\dot\psi^2 + \frac{9\sqrt3}{10}\,mga = \text{constant}}$$
>
> **Units:** J
> **Meaning:** the mechanical energy is conserved: the contact forces do no work because the body points where they act are at rest, and the weight does no work because $G$ stays at the same height. Its conservation is equivalent to the uniform rotation found in the reduction box.

> [!derivation] Part (h): closure of the system of equations
> **Law:** count of unknowns and independent equations
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> \text{unknowns} &: \ \psi,\ N_P,\ N_Q,\ X_P,\ X_Q,\ Y_P,\ Y_Q \quad &\text{(seven, with $\phi$ eliminated by rolling)} \\
> \text{equations} &: \ 6 \quad &\text{(three forces, three moments)} \\
> 7 - 6 &= 1 \quad &\text{(one unknown too many)}
> \end{aligned}$$
>
> $$\boxed{\text{not closed: } Y_P \text{ and } Y_Q \text{ appear only through their sum}}$$
>
> **Units:** dimensionless count
> **Meaning:** the two radial friction forces lie on the same line $OPQ$, so no equation of the rigid body can separate them: the motion, the normal reactions, the transverse frictions and the sum of the radial frictions are determined, but the split of that sum between the two wheels is statically indeterminate. It would need a model of the deformation of the wheels or of the contact.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Mass, $G$, tensor | $m = 5\pi\sigma a^2$; $\lvert C_1G\rvert = 4\sqrt3 a/5$; $\bar{\bar I}_G = \mathrm{diag}(A, B, A)$ in $\{\mathbf i_2, \mathbf j_2, \mathbf k_2\}$, $A = \tfrac{133}{100}ma^2$, $B = \tfrac{17}{10}ma^2$ |
| (b) Kinematics | $\mathbf r^G = \tfrac{27}{10}a\,\mathbf j_1 + \tfrac{9\sqrt3}{10}a\,\mathbf k_1$, $\mathbf v^G = -\tfrac{27}{10}a\dot\psi\,\mathbf i_1$, $\mathbf a^G = -\tfrac{27}{10}a(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1)$; $\boldsymbol\omega = \tfrac{\sqrt3}{2}\dot\phi\,\mathbf j_1 + (\dot\psi + \tfrac12\dot\phi)\,\mathbf k_1$, $\boldsymbol\alpha = -\tfrac{\sqrt3}{2}\dot\psi\dot\phi\,\mathbf i_1 + \tfrac{\sqrt3}{2}\ddot\phi\,\mathbf j_1 + (\ddot\psi + \tfrac12\ddot\phi)\,\mathbf k_1$ |
| (c) Rolling | $\dot\phi = -2\dot\psi$, $\phi = -2\psi$ ($\phi$ positive about $\mathbf j_2$) |
| (d) Forces | weight at $G$; $(X_P, Y_P, N_P)$ at $P$, $(X_Q, Y_Q, N_Q)$ at $Q$; $\mathbf F$ and $\mathbf M_G$ of the part (d) box |
| (e) Equations | six equations of the part (e) box; they give $\ddot\psi = 0$ |
| (f) Maximum rate | $\dot\psi^2_{\max} = 104g/(323\sqrt3\,a)$ |
| (g) Energy | conserved |
| (h) Closure | not closed: 7 unknowns, 6 equations; only $Y_P + Y_Q$ is determined |

**Check against the official key:** `Problems.pdf`, p. 81, sets $N_P$ to zero in the first rotational equation (the moment along $\mathbf i_1$), writes it with the gyroscopic term in $A + 3B$ and the term $9\sqrt3$ times $27/10$, and gives the maximum squared rate of $\psi$ as $104g$ divided by $323\sqrt3\,a$. The reduction box above, multiplied by ten over $ma^2$, is the same equation, and part (f) gives the same maximum: **match**.

> [!derivation] Check: the key's equation and its number
> **Law:** the moment along $\mathbf i_1$ with $N_P$ set to zero; arithmetic of $A + 3B$
> **Source:** Problems.pdf, p. 81; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> \frac{10}{ma^2}\cdot\frac{\sqrt3}{4}\left(A + 3B\right)\dot\psi^2 + 9\sqrt3\cdot\frac{27}{10}\,\dot\psi^2 &= \frac{10}{ma^2}\cdot\frac{a}{10}\cdot 13\,mg = 13\,\frac ga \quad &\text{(moment along $\mathbf i_1$ with $N_P = 0$, $N_Q = mg$, times $10/(ma^2)$)} \\
> \frac{10\left(A + 3B\right)}{4\,ma^2} &= \frac{10}{4}\left(\frac{133}{100} + \frac{51}{10}\right) = \frac{6430}{400} = 16.075 \quad &\text{(values of $A$ and $B$)} \\
> \sqrt3\,\dot\psi^2\left(16.075 + 24.3\right) &= \sqrt3\,\dot\psi^2\,\frac{323}{8} = 13\,\frac ga \;\Rightarrow\; \dot\psi^2 = \frac{104\,g}{323\sqrt3\,a} \quad &\text{(collect; $13\cdot 8 = 104$)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi_{\max}^2 = \frac{104\,g}{323\sqrt3\,a}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the key's equation is the moment equation of this solution; its numbers follow from the tensor of part (a).

**Limiting cases and consistency:**

* **Rest.** With the rate of $\psi$ zero, the normal reactions are thirteen twentieths and seven twentieths of $mg$: the static split of the weight between $P$ and $Q$ by the lever rule about the vertical through $G$.
* **No gyroscopic term.** Without the term in $A + 3B$ the limit would come from the centripetal force alone, with the squared rate equal to $13g/(24.3\sqrt3\,a)$, about $0.309\,g/a$: the gyroscopic term lowers the limiting squared rate by about 40 percent (the limiting rate by about 22 percent).
* **Sign of the rate.** Only the square of the rate of $\psi$ enters $N_P$: turning either way gives the same limit.
* **Dimensions.** $A$ and $B$ are a mass times a squared length; every term of the key's equation is in $[\mathrm{T^{-2}}]$.

---

## Problem RB-37: Disk rolling without slip over a bigger cylinder

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous disk $b$ of mass $m$, radius $R$ and centre $G$, in contact with a fixed cylinder of radius $3R$ and centre $O$ at the point $C$, rolling on it without slip. Read from the figure: $C$ lies between $O$ and $G$, so the disk rolls on the outside of the cylinder, below it, and $OG$ is $4R$. The body point $P$ (on the rim, at $R\,\mathbf i_b$ from $G$) is pushed away from the fixed point $A$ by a force of magnitude $k$ times the distance $AP$. Gravity acts downwards. The motion is planar.
* **Fixed frame:** $S_0\{O; \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, with $\mathbf i_0$ to the right, $\mathbf j_0$ up and $\mathbf k_0$ out of the paper (⊙). The cylinder is at rest, so this frame is inertial.
* **Rotating basis of the line of centres:** $\mathcal B_1$, the basis $\{\mathbf i_1, \mathbf j_1, \mathbf k_0\}$ turned by $\psi$ about $\mathbf k_0$, with $\mathbf j_1$ along $GC$ (from $G$ towards $O$) and $\mathbf i_1$ tangent to the cylinder at $C$. Read from the figure: $\psi$ is measured from the downward vertical to $OG$, counterclockwise.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k_0\}$. Read from the figure: $\phi$ is the angle from the direction $GC$ to $\mathbf j_b$, drawn clockwise (in the figure $\mathbf j_b$ lies on the clockwise side of $GC$); the body is therefore turned by $\psi$ minus $\phi$ from $S_0$.
* **Part (a), degrees of freedom:** a plane body has three coordinates. Contact with the cylinder (Notes.pdf, Eq. 13.1) fixes the distance $OG$ to $4R$: two coordinates remain, $\psi$ and $\phi$. Rolling without slip adds one relation between their rates, which can be integrated (part (c)): **one effective degree of freedom**, $\psi$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the disk, homogeneous | $m$ | kg |
| Radius of the disk | $R$ | m |
| Radius of the fixed cylinder | $3R$ | m |
| Moment of inertia about the normal axis through $G$ (statement) | $mR^2/2$ | kg m$^2$ |
| Fixed point of the repulsive force | $\mathbf r_0^A = -6R\,\mathbf j_0$ | m |
| Body point where it acts | $\mathbf r_b^P = R\,\mathbf i_b$ (from $G$) | m |
| Constant of the repulsive force | $k$ | N/m |
| Friction coefficient | $\mu$ infinite (no slip while in contact) | - |
| Initial state | $\psi_0 = \phi_0 = 0$, disk at rest | rad, rad/s |
| Gravity | $g$, along $-\mathbf j_0$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb37-rot-psi.svg]]

> [!derivation] Basis of the line of centres: rotation by psi about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View of the plane of the figure with $\mathbf k_0$ out of the paper (⊙); a positive $\psi$ turns counterclockwise. The unit vector from $O$ to $G$ is the downward vertical turned by $\psi$: its triangle has the hypotenuse 1 along $OG$, the adjacent leg along minus $\mathbf j_0$ (cosine of $\psi$) and the opposite leg along $\mathbf i_0$ (sine). $\mathbf j_1$ is minus this vector, and $\mathbf i_1$ is $\mathbf i_0$ turned by $\psi$: adjacent leg along $\mathbf i_0$ (cosine), opposite leg along $\mathbf j_0$ (sine).
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0 \quad &\text{(legs of the triangles; $\mathbf j_1$ points from $G$ towards $O$)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_0$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_0 &= \sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1 \quad &\text{(second row: the inverse is the transpose)} \\
> \dot{\mathbf i}_1 &= \dot\psi\,\mathbf k_0\times\mathbf i_1 = \dot\psi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\psi\,\mathbf k_0\times\mathbf j_1 = -\dot\psi\,\mathbf i_1 \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \boldsymbol\omega_{10} = \dot\psi\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** at $\psi$ zero, $G$ is straight below $O$ and $\mathcal B_1$ coincides with $\mathcal B_0$.

![[attachments/EM-SOL/rb37-rot-phi.svg]]

> [!derivation] Part (a): body basis, rotation by phi about minus k0
> **Law:** simple rotation about the third axis; right-hand rule; composition of angular velocities
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 9.2
>
> View at $G$ with $\mathbf k_0$ out of the paper (⊙), $\mathbf i_1$ to the right and $\mathbf j_1$ (towards $C$) up. The figure turns $\mathbf j_b$ clockwise from $GC$ by $\phi$: a positive rotation about minus $\mathbf k_0$ (⊗). Triangle of $\mathbf j_b$: hypotenuse 1, adjacent leg along $\mathbf j_1$ (cosine of $\phi$), opposite leg along $\mathbf i_1$ (sine), because the clockwise turn carries the tip of $\mathbf j_1$ to the right. Triangle of $\mathbf i_b$: adjacent leg along $\mathbf i_1$ (cosine), opposite leg along minus $\mathbf j_1$ (sine).
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\phi\,\mathbf i_1 - \sin\phi\,\mathbf j_1, \qquad \mathbf j_b = \sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_b] &= \begin{bmatrix} \cos\phi & \sin\phi & 0 \cr -\sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_0$ in $\mathcal B_1$)} \\
> \det[{}_1R_b] &= 1\cdot\left(\cos^2\phi + \sin^2\phi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_1R_b][{}_1R_b]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & -\cos\phi\sin\phi + \sin\phi\cos\phi & 0 \cr -\sin\phi\cos\phi + \cos\phi\sin\phi & \sin^2\phi + \cos^2\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_b &= \cos\left(\psi - \phi\right)\mathbf i_0 + \sin\left(\psi - \phi\right)\mathbf j_0, \qquad \mathbf j_b = -\sin\left(\psi - \phi\right)\mathbf i_0 + \cos\left(\psi - \phi\right)\mathbf j_0 \quad &\text{(product $[{}_0R_1][{}_1R_b]$; angle subtraction formulas)} \\
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b1} + \boldsymbol\omega_{10} = -\dot\phi\,\mathbf k_0 + \dot\psi\,\mathbf k_0 \quad &\text{(composition, Eq. 9.21)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos(\psi - \phi)\,\mathbf i_0 + \sin(\psi - \phi)\,\mathbf j_0, \qquad \mathbf j_b = -\sin(\psi - \phi)\,\mathbf i_0 + \cos(\psi - \phi)\,\mathbf j_0, \qquad \boldsymbol\omega_{b0} = \left(\dot\psi - \dot\phi\right)\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the angle $\psi$ minus $\phi$ is the angle that the disk has turned counterclockwise in $S_0$; with $\psi$ and $\phi$ zero, $\mathbf i_b$ is $\mathbf i_0$ and $P$ is level with $G$, on its right.

> [!derivation] Part (b): kinematics of G and of the disk
> **Law:** position along the line of centres; derivative of a vector written in a moving basis; Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf r_0^G &= \overrightarrow{OC} + \overrightarrow{CG} = -3R\,\mathbf j_1 - R\,\mathbf j_1 = -4R\,\mathbf j_1 = 4R\left(\sin\psi\,\mathbf i_0 - \cos\psi\,\mathbf j_0\right) \quad &\text{(sum of segments along the line of centres)} \\
> \mathbf v_0^G &= -4R\,\dot{\mathbf j}_1 = 4R\,\dot\psi\,\mathbf i_1 \quad &\text{(Poisson)} \\
> \mathbf a_0^G &= 4R\left(\ddot\psi\,\mathbf i_1 + \dot\psi\,\dot{\mathbf i}_1\right) = 4R\left(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1\right) \quad &\text{(product rule; Poisson)} \\
> \boldsymbol\alpha_{b0} &= \frac{d}{dt}\left[\left(\dot\psi - \dot\phi\right)\mathbf k_0\right] = \left(\ddot\psi - \ddot\phi\right)\mathbf k_0 \quad &\text{($\mathbf k_0$ constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = -4R\,\mathbf j_1, \quad \mathbf v_0^G = 4R\dot\psi\,\mathbf i_1, \quad \mathbf a_0^G = 4R\left(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1\right), \quad \boldsymbol\omega_{b0} = \left(\dot\psi - \dot\phi\right)\mathbf k_0, \quad \boldsymbol\alpha_{b0} = \left(\ddot\psi - \ddot\phi\right)\mathbf k_0}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}]$; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** $G$ moves on the circle of radius $4R$ about $O$; the term along $\mathbf j_1$ is the centripetal acceleration, towards $O$.

> [!derivation] Part (c): rolling without slip at C
> **Law:** velocity field of the rigid body; rolling without slipping on a body at rest; integration with Barrow's rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 13.4; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> \mathbf v_0^{C(b)} &= \mathbf v_0^G + \boldsymbol\omega_{b0}\times\overrightarrow{GC} = 4R\dot\psi\,\mathbf i_1 + \left(\dot\psi - \dot\phi\right)\mathbf k_0\times R\,\mathbf j_1 \quad &\text{(velocity field from $G$, Eq. 9.3; $\overrightarrow{GC} = R\,\mathbf j_1$)} \\
> &= 4R\dot\psi\,\mathbf i_1 - R\left(\dot\psi - \dot\phi\right)\mathbf i_1 = R\left(3\dot\psi + \dot\phi\right)\mathbf i_1 \quad &\text{($\mathbf k_0\times\mathbf j_1 = -\mathbf i_1$; collect)} \\
> 3\dot\psi + \dot\phi &= 0 \quad &\text{(no slip on the fixed cylinder, Eq. 13.5)} \\
> \int_0^{\phi}d\phi' &= -3\int_0^{\psi}d\psi' \;\Rightarrow\; \left[\phi'\right]_0^{\phi} = -3\left[\psi'\right]_0^{\psi} \;\Rightarrow\; \phi = -3\psi \quad &\text{(separate; antiderivatives; Barrow's rule with $\psi_0 = \phi_0 = 0$)} \\
> \psi - \phi &= 4\psi, \qquad \boldsymbol\omega_{b0} = 4\dot\psi\,\mathbf k_0, \qquad \boldsymbol\alpha_{b0} = 4\ddot\psi\,\mathbf k_0 \quad &\text{(substitute in part (b))} \\
> \mathbf i_b &= \cos 4\psi\,\mathbf i_0 + \sin 4\psi\,\mathbf j_0 = \cos 3\psi\,\mathbf i_1 + \sin 3\psi\,\mathbf j_1 \quad &\text{(angle $4\psi$ in $\mathcal B_0$; $\cos\phi = \cos 3\psi$, $-\sin\phi = \sin 3\psi$ in $\mathcal B_1$)}
> \end{aligned}$$
>
> $$\boxed{\phi = -3\psi, \qquad \boldsymbol\omega_{b0} = 4\dot\psi\,\mathbf k_0, \qquad \boldsymbol\alpha_{b0} = 4\ddot\psi\,\mathbf k_0, \qquad \mathbf v_0^G = 4R\dot\psi\,\mathbf i_1, \qquad \mathbf a_0^G = 4R\left(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the arcs rolled on the disk and on the cylinder are equal ($R$ times the magnitude of $\phi$ equals $3R$ times $\psi$), and the disk turns four times faster than the line of centres: going once round the cylinder, it makes four turns, not three, because its centre also goes round $O$. With the opposite (counterclockwise) reading of $\phi$ the relation would read $\phi$ equal to $3\psi$; nothing else changes.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and moment of inertia of the disk
> **Law:** symmetry of the homogeneous disk; moment of inertia as an area integral in polar coordinates (jacobian $\rho$)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.5; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 16]
>
> Polar coordinates $(\rho, \chi)$ about $G$, area element $\rho\,d\rho\,d\chi$, surface density $\sigma$ equal to $m$ over $\pi R^2$. $G$ is the centre of the disk by symmetry.
>
> $$\begin{aligned}
> I &= \sigma\int_0^{2\pi}\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R \quad &\text{(Eq. 10.11; separable integral; antiderivatives)} \\
> &= \sigma\cdot 2\pi\cdot\frac{R^4}{4} = \frac{m}{\pi R^2}\cdot\frac{\pi R^4}{2} = \frac{mR^2}{2} \quad &\text{(Barrow's rule; value of $\sigma$)}
> \end{aligned}$$
>
> $$\boxed{I = \frac{mR^2}{2}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the datum of the statement; the plane motion needs only this component, and the products of inertia with $\mathbf k_0$ vanish by the symmetry of the disk about its plane.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and energies
> **Law:** linear momentum from $G$; angular momentum of a plane body; Koenig's decomposition; potentials of the weight and of the linear repulsive force
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 5.2
>
> With rolling (part (c)). The repulsive force is $k$ times the vector $\overrightarrow{AP}$: it derives from minus one half of $k$ times the square of $AP$, because the gradient of that square with respect to the position of $P$ is twice $\overrightarrow{AP}$ (a spring of zero natural length with the sign reversed).
>
> $$\begin{aligned}
> \mathbf p_0 &= 4mR\dot\psi\,\mathbf i_1, \qquad \mathbf H_G = \frac{mR^2}{2}\cdot 4\dot\psi\,\mathbf k_0 = 2mR^2\dot\psi\,\mathbf k_0 \quad &\text{(Eq. 11.3; Eq. 11.12)} \\
> T_0 &= \frac12\,m\left(4R\dot\psi\right)^2 + \frac12\cdot\frac{mR^2}{2}\left(4\dot\psi\right)^2 = 8mR^2\dot\psi^2 + 4mR^2\dot\psi^2 = 12\,mR^2\dot\psi^2 \quad &\text{(Eq. 11.31)} \\
> V_g &= m\,g\,\mathbf r_0^G\cdot\mathbf j_0 = -4mgR\cos\psi, \qquad V_k = -\frac k2\left|\overrightarrow{AP}\right|^2 \quad &\text{(Eq. 12.34; potential of the repulsive force)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = 2mR^2\dot\psi\,\mathbf k_0, \qquad T_0 = 12\,mR^2\dot\psi^2, \qquad V = -4mgR\cos\psi - \frac k2\left|\overrightarrow{AP}\right|^2}$$
>
> **Units:** kg m$^2$/s; J
> **Meaning:** two thirds of the kinetic energy is in the motion of $G$ and one third in the rotation of the disk about $G$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb37-fbd.svg]]

| Force on the disk | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf j_0 = -mg(\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1)$ | applied |
| Repulsion from $A$ | $P$ | $\mathbf F_P = k\,\overrightarrow{AP}$ | applied |
| Normal reaction of the cylinder | $C$ | $-N\,\mathbf j_1$, with $N \ge 0$ (pushes the disk away from $O$) | constraint |
| Friction of the cylinder | $C$ | $T\,\mathbf i_1$ (unknown: no slip) | constraint |

> [!derivation] Part (d): the repulsive force at P
> **Law:** position of a body point from the body basis; head minus tail
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 2.6; Problems.pdf, p. 66
>
> $$\begin{aligned}
> \overrightarrow{AP} &= \mathbf r_0^G + R\,\mathbf i_b - \mathbf r_0^A = -4R\,\mathbf j_1 + R\,\mathbf i_b + 6R\,\mathbf j_0 \quad &\text{(head minus tail)} \\
> &= -4R\,\mathbf j_1 + R\left(\cos 3\psi\,\mathbf i_1 + \sin 3\psi\,\mathbf j_1\right) + 6R\left(\sin\psi\,\mathbf i_1 + \cos\psi\,\mathbf j_1\right) \quad &\text{($\mathbf i_b$ and $\mathbf j_0$ in $\mathcal B_1$)} \\
> \mathbf F_P &= k\,R\left(6\sin\psi + \cos 3\psi\right)\mathbf i_1 + k\,R\left(6\cos\psi - 4 + \sin 3\psi\right)\mathbf j_1 \quad &\text{(collect; times $k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_P = kR\left[\left(6\sin\psi + \cos 3\psi\right)\mathbf i_1 + \left(6\cos\psi - 4 + \sin 3\psi\right)\mathbf j_1\right]}$$
>
> **Units:** N/m times m, N
> **Meaning:** at the start, with $\psi$ zero, the force is $kR$ times $\mathbf i_1$ plus $2\,\mathbf j_1$: it pushes the disk up against the cylinder and to the right.

> [!derivation] Part (d): resultant force and moment about G
> **Law:** sum of forces; moments about $G$ by determinants
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> The weight acts at $G$; the arm of the contact force is $R\,\mathbf j_1$; the arm of the repulsion is $R\,\mathbf i_b$, and its moment is $R$ times $\mathbf i_b$ crossed with $\mathbf F_P$.
>
> $$\begin{aligned}
> \mathbf F &= \left(T - mg\sin\psi + kR\left(6\sin\psi + \cos 3\psi\right)\right)\mathbf i_1 + \left(-N - mg\cos\psi + kR\left(6\cos\psi - 4 + \sin 3\psi\right)\right)\mathbf j_1 \quad &\text{(sum by components)} \\
> R\,\mathbf j_1\times\left(T\,\mathbf i_1 - N\,\mathbf j_1\right) &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_0 \cr 0 & R & 0 \cr T & -N & 0 \end{vmatrix} = -R\,T\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> R\,\mathbf i_b\times\mathbf F_P &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_0 \cr R\cos 3\psi & R\sin 3\psi & 0 \cr kR\left(6\sin\psi + \cos 3\psi\right) & kR\left(6\cos\psi - 4 + \sin 3\psi\right) & 0 \end{vmatrix} \quad &\text{(arm in $\mathcal B_1$)} \\
> &= kR^2\left[\cos 3\psi\left(6\cos\psi - 4 + \sin 3\psi\right) - \sin 3\psi\left(6\sin\psi + \cos 3\psi\right)\right]\mathbf k_0 \quad &\text{(expand along the first row)} \\
> &= kR^2\left[6\left(\cos 3\psi\cos\psi - \sin 3\psi\sin\psi\right) - 4\cos 3\psi\right]\mathbf k_0 = kR^2\left(6\cos 4\psi - 4\cos 3\psi\right)\mathbf k_0 \quad &\text{(the products of $\sin 3\psi$ and $\cos 3\psi$ cancel; cosine of a sum)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_G = \left[-R\,T + kR^2\left(6\cos 4\psi - 4\cos 3\psi\right)\right]\mathbf k_0}$$
>
> **Units:** N; N m
> **Meaning:** the contact adds only two unknowns, $N$ and $T$, to the coordinate $\psi$; the repulsion and the weight are known functions of $\psi$.

> [!derivation] Equations of motion and the equation for psi
> **Law:** Newton's second law for the centre of mass; moment equation about $G$; elimination of the reactions
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole.
>
> $$\begin{aligned}
> 4mR\,\ddot\psi &= T - mg\sin\psi + kR\left(6\sin\psi + \cos 3\psi\right) \quad &\text{(force along $\mathbf i_1$)} \\
> 4mR\,\dot\psi^2 &= -N - mg\cos\psi + kR\left(6\cos\psi - 4 + \sin 3\psi\right) \quad &\text{(force along $\mathbf j_1$)} \\
> 2mR^2\,\ddot\psi &= -R\,T + kR^2\left(6\cos 4\psi - 4\cos 3\psi\right) \quad &\text{(moment along $\mathbf k_0$; $I$ times $4\ddot\psi$)} \\
> T &= -2mR\,\ddot\psi + kR\left(6\cos 4\psi - 4\cos 3\psi\right) \quad &\text{(moment equation divided by $R$)} \\
> 6mR\,\ddot\psi &= -mg\sin\psi + kR\left(6\sin\psi - 3\cos 3\psi + 6\cos 4\psi\right) \quad &\text{(substitute in the force along $\mathbf i_1$; collect)}
> \end{aligned}$$
>
> $$\boxed{\ddot\psi = -\frac{g}{6R}\sin\psi + \frac km\left(\sin\psi - \frac12\cos 3\psi + \cos 4\psi\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]/[\mathrm L]$ and $[\mathrm{M\,T^{-2}}]/[\mathrm M]$, both $[\mathrm{T^{-2}}]$
> **Meaning:** gravity pulls the disk back to the bottom ($\psi$ zero) and the repulsion pushes it; at the start the second rate of $\psi$ is $k/(2m)$, positive: the disk starts to roll counterclockwise round the cylinder, $G$ moving to the right.

> [!derivation] Part (e): first-order equation and initial conditions
> **Law:** first integral of the equation of motion: multiply by the rate of $\psi$ and integrate; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 2.6; Problems.pdf, p. 66
>
> The rate of $\psi$ times its second rate is the derivative of one half of its square (chain rule); integrate from the initial instant, where $\psi$ and its rate are zero.
>
> $$\begin{aligned}
> \int_0^{t}\ddot\psi\,\dot\psi\,dt' &= \left[\frac{\dot\psi^2}{2}\right]_0^{t} = \frac{\dot\psi^2}{2} - 0 \quad &\text{(antiderivative; Barrow's rule; initial rest)} \\
> \int_0^{t} f\left(\psi\right)\dot\psi\,dt' &= \int_0^{\psi} f\left(\psi'\right)d\psi' \quad &\text{(substitution $d\psi' = \dot\psi\,dt'$)} \\
> \int_0^{\psi}\sin\psi'\,d\psi' &= \left[-\cos\psi'\right]_0^{\psi} = 1 - \cos\psi \quad &\text{(antiderivative; Barrow's rule)} \\
> \int_0^{\psi}\cos 3\psi'\,d\psi' &= \left[\frac{\sin 3\psi'}{3}\right]_0^{\psi} = \frac{\sin 3\psi}{3}, \qquad \int_0^{\psi}\cos 4\psi'\,d\psi' = \left[\frac{\sin 4\psi'}{4}\right]_0^{\psi} = \frac{\sin 4\psi}{4} \quad &\text{(antiderivatives with $d(3\psi') = 3\,d\psi'$, $d(4\psi') = 4\,d\psi'$; Barrow's rule)} \\
> \frac{\dot\psi^2}{2} &= -\frac{g}{6R}\left(1 - \cos\psi\right) + \frac km\left(1 - \cos\psi - \frac{\sin 3\psi}{6} + \frac{\sin 4\psi}{4}\right) \quad &\text{(term by term)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi^2 = \frac km\left(2 - 2\cos\psi - \frac{\sin 3\psi}{3} + \frac{\sin 4\psi}{2}\right) - \frac{g}{3R}\left(1 - \cos\psi\right), \qquad \psi(0) = 0, \quad \dot\psi(0) = 0}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every term
> **Meaning:** this is the conservation of the mechanical energy (checked below). The first-order equation is the positive square root, since the motion starts towards positive $\psi$ (previous box). At $\psi$ zero the right-hand side vanishes, so the first-order equation alone also admits the solution at rest; the second-order equation, with its positive initial value $k/(2m)$, selects the motion. The motion is possible while the right-hand side stays positive and the disk stays in contact.

> [!derivation] Part (f): detachment from the cylinder
> **Law:** unilateral contact: the normal reaction must stay non-negative; elimination of the rate with the first integral
> **Source:** Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.1; Notes.pdf, Eq. 12.8
>
> $$\begin{aligned}
> N &= kR\left(6\cos\psi - 4 + \sin 3\psi\right) - mg\cos\psi - 4mR\,\dot\psi^2 \quad &\text{(force along $\mathbf j_1$)} \\
> 4mR\,\dot\psi^2 &= kR\left(8 - 8\cos\psi - \frac43\sin 3\psi + 2\sin 4\psi\right) - \frac43\,mg\left(1 - \cos\psi\right) \quad &\text{(part (e) times $4mR$)} \\
> N &= kR\left(14\cos\psi - 12 + \frac73\sin 3\psi - 2\sin 4\psi\right) + mg\left(\frac43 - \frac73\cos\psi\right) \quad &\text{(substitute; collect)} \\
> N(0) &= 2kR - mg \quad &\text{(initial value: contact at the start needs $2kR \ge mg$)}
> \end{aligned}$$
>
> $$\boxed{\text{detachment at the first } \psi \gt 0 \text{ with } \ kR\left(42\cos\psi - 36 + 7\sin 3\psi - 6\sin 4\psi\right) + mg\left(4 - 7\cos\psi\right) = 0}$$
>
> **Units:** N in each term (before the factor 3)
> **Meaning:** the boxed condition is three times the normal reaction set to zero; it contains $\psi$ only. Beyond it the expression would be negative, which the cylinder cannot provide: the disk leaves the cylinder there. If $2kR$ is smaller than $mg$ the disk is not even held against the cylinder at the start.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom; bases | one ($\psi$); $\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0$, $\mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0$; $\mathbf i_b = \cos(\psi - \phi)\,\mathbf i_0 + \sin(\psi - \phi)\,\mathbf j_0$, $\mathbf j_b = -\sin(\psi - \phi)\,\mathbf i_0 + \cos(\psi - \phi)\,\mathbf j_0$ |
| (b) Kinematics | $\mathbf r^G = 4R(\sin\psi\,\mathbf i_0 - \cos\psi\,\mathbf j_0)$, $\mathbf v^G = 4R\dot\psi\,\mathbf i_1$, $\mathbf a^G = 4R(\ddot\psi\,\mathbf i_1 + \dot\psi^2\,\mathbf j_1)$, $\boldsymbol\omega = (\dot\psi - \dot\phi)\,\mathbf k_0$, $\boldsymbol\alpha = (\ddot\psi - \ddot\phi)\,\mathbf k_0$ |
| (c) Rolling | $\phi = -3\psi$ ($\phi$ read clockwise); $\boldsymbol\omega = 4\dot\psi\,\mathbf k_0$, $\boldsymbol\alpha = 4\ddot\psi\,\mathbf k_0$ |
| (d) Forces | $-mg\,\mathbf j_0$ at $G$; $k\,\overrightarrow{AP}$ at $P$; $-N\,\mathbf j_1 + T\,\mathbf i_1$ at $C$; $\mathbf F$ and $\mathbf M_G = [-RT + kR^2(6\cos 4\psi - 4\cos 3\psi)]\,\mathbf k_0$ |
| (e) First-order equation | $\dot\psi^2 = \tfrac km(2 - 2\cos\psi - \tfrac13\sin 3\psi + \tfrac12\sin 4\psi) - \tfrac{g}{3R}(1 - \cos\psi)$, $\psi(0) = 0$ |
| (f) Detachment | $kR(42\cos\psi - 36 + 7\sin 3\psi - 6\sin 4\psi) + mg(4 - 7\cos\psi) = 0$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with an independent derivation and limiting cases.

> [!derivation] Check: the first integral from the mechanical energy
> **Law:** conservation of the mechanical energy (the contact force acts on a body point at rest; weight and repulsion are conservative)
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.5
>
> In $\mathcal B_0$, $P$ is at $R$ times $(4\sin\psi + \cos 4\psi)$ along $\mathbf i_0$ and $R$ times $(-4\cos\psi + \sin 4\psi)$ along $\mathbf j_0$ (part (c)).
>
> $$\begin{aligned}
> \frac{\left|\overrightarrow{AP}\right|^2}{R^2} &= \left(4\sin\psi + \cos 4\psi\right)^2 + \left(6 - 4\cos\psi + \sin 4\psi\right)^2 \quad &\text{(components of $\overrightarrow{AP}$ in $\mathcal B_0$)} \\
> &= 16 + 1 + 36 - 48\cos\psi + 12\sin 4\psi + 8\left(\sin\psi\cos 4\psi - \cos\psi\sin 4\psi\right) \quad &\text{(expand; $\sin^2 + \cos^2 = 1$ twice)} \\
> &= 53 - 48\cos\psi + 12\sin 4\psi - 8\sin 3\psi \quad &\text{(sine of a difference)} \\
> 12mR^2\dot\psi^2 - 4mgR\cos\psi - \frac{kR^2}{2}\left(53 - 48\cos\psi + 12\sin 4\psi - 8\sin 3\psi\right) &= -4mgR - \frac{5kR^2}{2} \quad &\text{(Eq. 12.33 from the initial rest at $\psi$ zero)} \\
> \dot\psi^2 &= \frac{g}{3R}\left(\cos\psi - 1\right) + \frac{k}{24m}\left(48 - 48\cos\psi + 12\sin 4\psi - 8\sin 3\psi\right) \quad &\text{(divide by $12mR^2$)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi^2 = \frac km\left(2 - 2\cos\psi - \frac{\sin 3\psi}{3} + \frac{\sin 4\psi}{2}\right) - \frac{g}{3R}\left(1 - \cos\psi\right)}$$
>
> **Units:** J before the division; $[\mathrm{T^{-2}}]$ after
> **Meaning:** the energy gives exactly the first integral of part (e), without any reaction: the friction does no work because the disk rolls, and the normal reaction acts on a point at rest.

**Limiting cases and consistency:**

* **No repulsion.** With $k$ zero the disk below the cylinder has nothing pressing it against the cylinder: the initial normal reaction would be minus $mg$, so contact is impossible, in agreement with the condition $2kR \ge mg$. Formally (with a guide keeping the contact), the equation of motion would reduce to the pendulum of the centre about $O$, with the factor $g/(6R)$: $4R$ for the radius of the circle of $G$ times three halves for the rotational inertia of the rolling disk.
* **Start.** At $\psi$ zero the repulsion is $kR$ along $\mathbf i_0$ plus $2kR$ along $\mathbf j_0$; its horizontal part and its moment about $G$, $2kR^2$, both start the rolling: the initial second rate of $\psi$, $k/(2m)$, follows from the equation of motion with $\psi$ zero.
* **Sign check.** The first integral grows like $k/m$ times $\psi$ for small positive $\psi$ (its slope at zero is $k/m$), so the square of the rate of $\psi$ is positive just after the start, as it must be.
* **Dimensions.** $k/m$ and $g/R$ are both squared rates; every force term is a multiple of $kR$ or $mg$.

---

## Problem RB-39: Yo-yo

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** the yo-yo $b$ (two homogeneous disks of radius $R$ joined by an inner cylinder of radius $a$), of mass $m$ and centre $C$, hangs from the fixed point $O$ of the ceiling by a thin, massless, inextensible string that is wound on the inner cylinder and stays taut. The string, the centre $C$ and gravity lie in one vertical plane (the mid-plane of the yo-yo), so the motion is planar.
* **Fixed frame:** $S_0\{O; \mathbf i_0, \mathbf j_0, \mathbf k_0\}$, with $\mathbf i_0$ horizontal to the right, $\mathbf j_0$ up and $\mathbf k_0$ out of the paper (⊙). The ceiling is at rest, so the frame is inertial. Gravity is $g$ along minus $\mathbf j_0$.
* **Basis of the string:** $\mathcal B_1$, the basis $\{\mathbf i_1, \mathbf j_1, \mathbf k_0\}$ turned by $\theta$ about $\mathbf k_0$; minus $\mathbf j_1$ points along the straight part of the string, from $O$ towards the yo-yo, and $\mathbf i_1$ is normal to the string. Read from the figure: $\theta$ is measured from the downward vertical to the string, counterclockwise (the string leans to the right of $O$). The opposite reading (clockwise) would replace $\theta$ by its opposite in every formula below; the method is the same.
* **Generalized coordinates:** $\xi$, the length of the straight part of the string, from $O$ to the point $T$ where it leaves the inner cylinder, and $\theta$. Read from the figure: the string leaves the inner cylinder on its right-hand side, so the radius $CT$ points along $\mathbf i_1$ and $C$ lies at the distance $a$ on the left of the string.
* **Body angle:** $\varphi$, the angle from $\mathbf i_0$ to a line fixed in the yo-yo, counterclockwise. It is not a free coordinate: the string unwinds without slipping on the inner cylinder, and that relation is integrated below.
* **Degrees of freedom:** a plane body has three coordinates ($\xi$, $\theta$, $\varphi$ describe them: the first two fix $C$, the third the orientation). The taut, inextensible string wound without slip gives one relation among their rates, which integrates into a relation among the coordinates themselves: **two degrees of freedom**, $\xi$ and $\theta$, as the statement says.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the yo-yo | $m$ | kg |
| Radius of the outer disks | $R$ | m |
| Radius of the inner cylinder (string) | $a$ | m |
| Moment of inertia about the spin axis (statement) | $mR^2/2$ | kg m$^2$ |
| Length of the straight part of the string | $\xi$ | m |
| Angle of the string from the downward vertical | $\theta$ | rad |
| Tension of the string (unknown) | $F \ge 0$ | N |
| Gravity | $g$, along $-\mathbf j_0$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb39-rot-theta.svg]]

> [!derivation] Basis of the string: rotation by theta about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View of the plane of the figure with $\mathbf k_0$ out of the paper (⊙): a positive $\theta$ turns counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\theta$: its triangle has the hypotenuse 1, the adjacent leg along $\mathbf i_0$ (cosine of $\theta$) and the opposite leg along $\mathbf j_0$ (sine). $\mathbf j_1$ is $\mathbf j_0$ turned by $\theta$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine): the counterclockwise turn carries the tip of $\mathbf j_0$ to the left, which is the minus sign. The unit vector along the string, minus $\mathbf j_1$, then has the components sine of $\theta$ to the right and cosine of $\theta$ downwards, as in the figure.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_0$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_0 &= \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(second row: the inverse is the transpose)} \\
> \dot{\mathbf i}_1 &= \dot\theta\,\mathbf k_0\times\mathbf i_1 = \dot\theta\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\theta\,\mathbf k_0\times\mathbf j_1 = -\dot\theta\,\mathbf i_1 \quad &\text{(Poisson, with $\boldsymbol\omega_{10} = \dot\theta\,\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0, \qquad \boldsymbol\omega_{10} = \dot\theta\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** with $\theta$ zero the string hangs vertically and $\mathcal B_1$ coincides with $\mathcal B_0$.

![[attachments/EM-SOL/rb39-position.svg]]

> [!derivation] Part (a): position, velocity and acceleration of C
> **Law:** position as a sum of segments; derivative of a vector written in a moving basis; Poisson's formula; product rule
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> The straight string runs from $O$ to $T$ along minus $\mathbf j_1$ with length $\xi$; the radius from $T$ to $C$ is normal to the string (the string is tangent to the inner cylinder at $T$) and points along minus $\mathbf i_1$. The triangle $OTC$ has its right angle at $T$, legs $\xi$ and $a$, and hypotenuse $OC$.
>
> $$\begin{aligned}
> \mathbf r_0^C &= \overrightarrow{OT} + \overrightarrow{TC} = -\xi\,\mathbf j_1 - a\,\mathbf i_1 \quad &\text{(sum of segments)} \\
> &= \left(\xi\sin\theta - a\cos\theta\right)\mathbf i_0 + \left(-\xi\cos\theta - a\sin\theta\right)\mathbf j_0 \quad &\text{(substitute $\mathbf i_1$, $\mathbf j_1$ from the previous box)} \\
> \mathbf v_0^C &= -\dot\xi\,\mathbf j_1 - \xi\,\dot{\mathbf j}_1 - a\,\dot{\mathbf i}_1 = -\dot\xi\,\mathbf j_1 + \xi\dot\theta\,\mathbf i_1 - a\dot\theta\,\mathbf j_1 \quad &\text{(product rule; Poisson; $a$ constant)} \\
> &= \xi\dot\theta\,\mathbf i_1 - \left(\dot\xi + a\dot\theta\right)\mathbf j_1 \quad &\text{(collect)} \\
> \mathbf a_0^C &= \left(\dot\xi\dot\theta + \xi\ddot\theta\right)\mathbf i_1 + \xi\dot\theta\,\dot{\mathbf i}_1 - \left(\ddot\xi + a\ddot\theta\right)\mathbf j_1 - \left(\dot\xi + a\dot\theta\right)\dot{\mathbf j}_1 \quad &\text{(product rule on each term)} \\
> &= \left(\dot\xi\dot\theta + \xi\ddot\theta\right)\mathbf i_1 + \xi\dot\theta^2\,\mathbf j_1 - \left(\ddot\xi + a\ddot\theta\right)\mathbf j_1 + \left(\dot\xi + a\dot\theta\right)\dot\theta\,\mathbf i_1 \quad &\text{(Poisson)} \\
> &= \left(\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2\right)\mathbf i_1 + \left(\xi\dot\theta^2 - \ddot\xi - a\ddot\theta\right)\mathbf j_1 \quad &\text{(collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^C = -a\,\mathbf i_1 - \xi\,\mathbf j_1, \quad \mathbf v_0^C = \xi\dot\theta\,\mathbf i_1 - \left(\dot\xi + a\dot\theta\right)\mathbf j_1, \quad \mathbf a_0^C = \left(\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2\right)\mathbf i_1 + \left(\xi\dot\theta^2 - \ddot\xi - a\ddot\theta\right)\mathbf j_1}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$ in every term
> **Meaning:** along the string ($\mathbf j_1$) the term in the square of the rate of $\theta$ is the centripetal part (towards $O$) and the second rate of $\xi$ the unwinding; normal to it, the term in twice the product of the rates is the Coriolis-type term of a length that changes while it turns.

> [!derivation] Part (a): string without slip on the inner cylinder; angular velocity and acceleration
> **Law:** velocity field of the rigid body; rolling without slip (equal velocities of the two points in contact); integration with Barrow's rule
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.2; Notes.pdf, Sec. 13.2
>
> The string point that touches the cylinder at $T$ is at the fixed arc length $\xi$ from $O$ along a straight string that turns about $O$ with $\boldsymbol\omega_{10}$; since the string is inextensible and fixed at $O$, that material point does not slide along the string, so its position is $\xi$ times minus $\mathbf j_1$ with $\xi$ frozen. The yo-yo point at $T$ is $C$ plus $a\,\mathbf i_1$. With no slip both velocities are equal. The angular velocity of $b$ is the rate of $\varphi$ times $\mathbf k_0$.
>
> $$\begin{aligned}
> \mathbf v_0^{T(\text{string})} &= -\xi\,\dot{\mathbf j}_1 = \xi\dot\theta\,\mathbf i_1 \quad &\text{(arc length of the material point frozen; Poisson)} \\
> \mathbf v_0^{T(b)} &= \mathbf v_0^C + \dot\varphi\,\mathbf k_0\times a\,\mathbf i_1 = \xi\dot\theta\,\mathbf i_1 - \left(\dot\xi + a\dot\theta\right)\mathbf j_1 + a\dot\varphi\,\mathbf j_1 \quad &\text{(velocity field from $C$, Eq. 9.3; $\mathbf k_0\times\mathbf i_1 = \mathbf j_1$)} \\
> \mathbf v_0^{T(b)} - \mathbf v_0^{T(\text{string})} &= \left(a\dot\varphi - \dot\xi - a\dot\theta\right)\mathbf j_1 = \mathbf 0 \quad &\text{(no slip, Eq. 13.2)} \\
> \dot\varphi &= \dot\theta + \frac{\dot\xi}{a} \quad &\text{(divide by $a$)} \\
> \int_{0}^{t}\dot\varphi\,dt' &= \int_0^t\dot\theta\,dt' + \frac1a\int_0^t\dot\xi\,dt' \;\Rightarrow\; \left[\varphi\right]_0^t = \left[\theta\right]_0^t + \frac1a\left[\xi\right]_0^t \quad &\text{(antiderivatives; Barrow's rule)} \\
> \varphi - \varphi_0 &= \theta - \theta_0 + \frac{\xi - \xi_0}{a} \quad &\text{(holonomic: a relation among coordinates)} \\
> \boldsymbol\alpha_{b0} &= \frac{d}{dt}\left[\left(\dot\theta + \frac{\dot\xi}{a}\right)\mathbf k_0\right] = \left(\ddot\theta + \frac{\ddot\xi}{a}\right)\mathbf k_0 \quad &\text{($\mathbf k_0$ constant)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \left(\dot\theta + \frac{\dot\xi}{a}\right)\mathbf k_0, \qquad \boldsymbol\alpha_{b0} = \left(\ddot\theta + \frac{\ddot\xi}{a}\right)\mathbf k_0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ and $[\mathrm L\,\mathrm T^{-1}]/[\mathrm L]$; $[\mathrm{T^{-2}}]$
> **Meaning:** with the string vertical and fixed ($\theta$ constant), a growing $\xi$ (the yo-yo falls) makes the rate of $\varphi$ positive: the yo-yo spins counterclockwise, as a reel unwinding a string held on its right-hand side does. The yo-yo point at $T$ is not at rest: it moves with the string, normal to it.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and moment of inertia about the spin axis
> **Law:** symmetry of a homogeneous body of revolution; moment of inertia as an area integral in polar coordinates (jacobian $\rho$)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.5; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 16]
>
> The two equal disks and the inner cylinder are coaxial and symmetric about the mid-plane, so $C$ is the centre of mass and $\mathbf k_0$ (the spin axis) is a principal axis: the products of inertia with $\mathbf k_0$ vanish. The statement gives the moment about the spin axis; the value is the one of the two disks alone (inner cylinder of negligible mass), each of mass one half of $m$ and surface density $\sigma$ equal to $m/(2\pi R^2)$, which the integral checks.
>
> $$\begin{aligned}
> I_{\text{one disk}} &= \sigma\int_0^{2\pi}\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R \quad &\text{(Eq. 10.11; separable integral; antiderivatives)} \\
> &= \sigma\cdot 2\pi\cdot\frac{R^4}{4} = \frac{m}{2\pi R^2}\cdot\frac{\pi R^4}{2} = \frac{mR^2}{4} \quad &\text{(Barrow's rule; value of $\sigma$)} \\
> I &= 2\,I_{\text{one disk}} = \frac{mR^2}{2} \quad &\text{(the two disks share the axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \mathbf r_0^C, \qquad I = \frac{mR^2}{2}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the datum of the statement; a massive inner cylinder would lower the value, since its mass sits closer to the axis.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about C and energies
> **Law:** linear momentum from the centre of mass; angular momentum about $G$ of a body turning about a principal axis; kinetic energy about $G$; potential of the weight
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^C = m\xi\dot\theta\,\mathbf i_1 - m\left(\dot\xi + a\dot\theta\right)\mathbf j_1 \quad &\text{(Eq. 11.3)} \\
> \mathbf H_C &= I\,\dot\varphi\,\mathbf k_0 = \frac{mR^2}{2}\left(\dot\theta + \frac{\dot\xi}{a}\right)\mathbf k_0 \quad &\text{(Eq. 11.12; principal axis $\mathbf k_0$)} \\
> T_0 &= \frac12\,m\left(v_0^C\right)^2 + \frac12\,I\dot\varphi^2 = \frac m2\left[\xi^2\dot\theta^2 + \left(\dot\xi + a\dot\theta\right)^2\right] + \frac{mR^2}{4}\left(\dot\theta + \frac{\dot\xi}{a}\right)^2 \quad &\text{(Eq. 11.31; $\mathbf i_1$ and $\mathbf j_1$ orthonormal)} \\
> V_0 &= m\,g\,\mathbf r_0^C\cdot\mathbf j_0 = -m\,g\left(\xi\cos\theta + a\sin\theta\right) \quad &\text{(Eq. 12.34; height of $C$ from the position box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_C = \frac{mR^2}{2}\left(\dot\theta + \frac{\dot\xi}{a}\right)\mathbf k_0, \qquad T_0 = \frac m2\left[\xi^2\dot\theta^2 + \left(\dot\xi + a\dot\theta\right)^2\right] + \frac{mR^2}{4}\left(\dot\theta + \frac{\dot\xi}{a}\right)^2, \qquad V_0 = -mg\left(\xi\cos\theta + a\sin\theta\right)}$$
>
> **Units:** kg m$^2$/s; J in every term of $T_0$ and $V_0$
> **Meaning:** the rotational part grows with the square of the ratio $R/a$: for a thin axle most of the energy of a falling yo-yo goes into its spin.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb39-fbd.svg]]

| Force on the yo-yo | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $C$ | $-mg\,\mathbf j_0 = -mg(\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1)$ | applied |
| Tension of the string | $T$ (at $a\,\mathbf i_1$ from $C$) | $F\,\mathbf j_1$, along the string towards $O$, with $F \ge 0$ (taut string) | constraint |

> [!derivation] Part (b): resultant force and resultant torque at C
> **Law:** sum of forces; moment of a force about $C$ by a determinant expanded along the first row
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> The weight acts at $C$ and has no moment about it. The arm of the tension is $a\,\mathbf i_1$.
>
> $$\begin{aligned}
> \mathbf F &= F\,\mathbf j_1 - mg\left(\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1\right) = -mg\sin\theta\,\mathbf i_1 + \left(F - mg\cos\theta\right)\mathbf j_1 \quad &\text{(sum by components; $\mathbf j_0$ in $\mathcal B_1$)} \\
> \mathbf M_C &= a\,\mathbf i_1\times F\,\mathbf j_1 = \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_0 \cr a & 0 & 0 \cr 0 & F & 0 \end{vmatrix} = a\,F\,\mathbf k_0 \quad &\text{(expand along the first row)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -mg\sin\theta\,\mathbf i_1 + \left(F - mg\cos\theta\right)\mathbf j_1 \ \text{ at } C, \qquad \mathbf M_C = aF\,\mathbf k_0}$$
>
> **Units:** N; m N
> **Meaning:** the tension pulls up on the right-hand side of the axle: its torque is counterclockwise, the sense in which the yo-yo spins while it falls.

> [!derivation] Part (c): equations of motion
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $C$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole; the derivative of the angular momentum is $I$ times the angular acceleration, because $\mathbf k_0$ is fixed.
>
> $$\begin{aligned}
> m\left(\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2\right) &= -mg\sin\theta \quad &\text{(force along $\mathbf i_1$)} \\
> m\left(\xi\dot\theta^2 - \ddot\xi - a\ddot\theta\right) &= F - mg\cos\theta \quad &\text{(force along $\mathbf j_1$)} \\
> \frac{mR^2}{2}\left(\ddot\theta + \frac{\ddot\xi}{a}\right) &= aF \quad &\text{(moment along $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2 + g\sin\theta = 0, \qquad m\left(\ddot\xi + a\ddot\theta - \xi\dot\theta^2\right) = mg\cos\theta - F, \qquad \frac{mR^2}{2a}\left(\ddot\theta + \frac{\ddot\xi}{a}\right) = F}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in the first line; N in the second and third
> **Meaning:** three equations for three unknown functions of time, $\xi$, $\theta$ and the tension $F$ (the rotation is already eliminated by the no-slip relation). Substituting the third into the second leaves two equations for the two coordinates; the motion is valid while $F$ stays non-negative.

> [!derivation] Part (d): first integral of the energy
> **Law:** power of the forces reduced at $C$; energy theorem; conservation of the mechanical energy
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34
>
> Justification: the tension acts on the yo-yo point $T$, whose velocity is $\xi$ times the rate of $\theta$ along $\mathbf i_1$ (previous box), normal to the tension: its power is zero, because the string is fixed at $O$ and does not slip. The weight is conservative. The power is computed below with the resultant at $C$ and the equations of part (c) are not needed for it, so the integral holds for any motion with taut string.
>
> $$\begin{aligned}
> \dot W_0 &= \mathbf F\cdot\mathbf v_0^C + \mathbf M_C\cdot\boldsymbol\omega_{b0} \quad &\text{(power reduced at $C$, Eq. 12.29)} \\
> &= \left(F\,\mathbf j_1 - mg\,\mathbf j_0\right)\cdot\mathbf v_0^C + aF\left(\dot\theta + \frac{\dot\xi}{a}\right) \quad &\text{(part (b); angular velocity)} \\
> &= -F\left(\dot\xi + a\dot\theta\right) - mg\,\mathbf j_0\cdot\mathbf v_0^C + aF\dot\theta + F\dot\xi \quad &\text{($\mathbf j_1\cdot\mathbf v_0^C$ from part (a))} \\
> &= -mg\,\frac{d}{dt}\left(\mathbf r_0^C\cdot\mathbf j_0\right) = -\frac{dV_0}{dt} \quad &\text{(the tension terms cancel; $\mathbf j_0$ constant)} \\
> \frac{dT_0}{dt} &= -\frac{dV_0}{dt} \;\Rightarrow\; \int_0^t\frac{d}{dt'}\left(T_0 + V_0\right)dt' = \left[T_0 + V_0\right]_0^t = 0 \quad &\text{(energy theorem, Eq. 12.30; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\frac m2\left[\xi^2\dot\theta^2 + \left(\dot\xi + a\dot\theta\right)^2\right] + \frac{mR^2}{4}\left(\dot\theta + \frac{\dot\xi}{a}\right)^2 - mg\left(\xi\cos\theta + a\sin\theta\right) = E_0}$$
>
> **Units:** J in every term
> **Meaning:** $E_0$ is fixed by the initial values of $\xi$, $\theta$ and their rates; the equation holds no second derivatives. The angular momentum about $O$ is not conserved: the tension passes through $O$, but the weight has a moment about it.

#### The yo-yo kept on the vertical (theta fixed at zero)

> [!derivation] Part (e): initial acceleration from rest
> **Law:** equations of part (c) with the extra constraint; reaction of the ideal guide
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.1
>
> The extra constraint (a guide that keeps the string vertical) adds a horizontal reaction $H\,\mathbf i_1$ at $C$; with $\theta$ and its rates zero, $\mathcal B_1$ is $\mathcal B_0$. Write $\rho$ for the ratio $R/a$.
>
> $$\begin{aligned}
> 0 &= -mg\cdot 0 + H \;\Rightarrow\; H = 0 \quad &\text{(force along $\mathbf i_1$ with $\theta$ zero: the guide does not act)} \\
> m\ddot\xi &= mg - F, \qquad F = \frac{mR^2}{2a^2}\,\ddot\xi \quad &\text{(the other two equations with $\theta$ zero)} \\
> m\ddot\xi\left(1 + \frac{R^2}{2a^2}\right) &= mg \quad &\text{(eliminate $F$)} \\
> \ddot\xi &= \frac{2a^2 g}{2a^2 + R^2} = \frac{2g}{2 + \rho^2} \quad &\text{(solve; divide numerator and denominator by $a^2$)} \\
> F &= \frac{mR^2}{2a^2}\cdot\frac{2a^2 g}{2a^2 + R^2} = \frac{mgR^2}{2a^2 + R^2} \quad &\text{(back into the moment equation)}
> \end{aligned}$$
>
> $$\boxed{\ddot\xi_0 = \frac{2g}{2 + (R/a)^2}, \qquad F = \frac{mg\,(R/a)^2}{2 + (R/a)^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$; N
> **Meaning:** the acceleration does not depend on the velocity, so it is the same at every instant, at rest or not. It is two thirds of $g$ (0.667 g) for $R$ equal to $a$, one third of $g$ for $R$ twice $a$, one ninth for four times $a$, and decays like twice $g$ over the square of $R/a$ for a large ratio (graph below). The tension stays between one third of $mg$ and $mg$: positive, so the string is indeed taut.

![[attachments/EM-SOL/rb39-graph-accel.svg]]

> [!derivation] Part (f): minimum initial spin to climb back to the origin
> **Law:** first integral of part (d) with $\theta$ zero; condition of a real rate at the target position
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.2
>
> With $\theta$ zero, the no-slip relation gives the rate of $\xi$ as $a$ times the rate of $\varphi$; $\xi$ can only decrease if the yo-yo spins clockwise (rate of $\varphi$ negative): it winds the string up. Initially $\xi$ is $2R$ and the spin has magnitude $\Omega_0$; at a later instant the spin has magnitude $\Omega$.
>
> $$\begin{aligned}
> T_0 &= \frac m2\,a^2\dot\varphi^2 + \frac{mR^2}{4}\,\dot\varphi^2 = \frac m4\left(2a^2 + R^2\right)\dot\varphi^2, \qquad V_0 = -mg\,\xi \quad &\text{(part (d) with $\theta$ zero; rate of $\xi$ equal to $a$ times the rate of $\varphi$)} \\
> \frac m4\left(2a^2 + R^2\right)\Omega^2 - mg\,\xi &= \frac m4\left(2a^2 + R^2\right)\Omega_0^2 - 2mgR \quad &\text{(energy at a later instant and at the start)} \\
> \Omega^2 &= \Omega_0^2 - \frac{4g\left(2R - \xi\right)}{2a^2 + R^2} \quad &\text{(solve for the square of the spin)} \\
> \Omega^2\big|_{\xi = 0} &= \Omega_0^2 - \frac{8gR}{2a^2 + R^2} \ge 0 \quad &\text{(the origin is reached only with a real rate there)} \\
> \Omega_{0,\min} &= \sqrt{\frac{8gR}{R^2 + 2a^2}} \;\approx\; \sqrt{\frac{8g}{R}} \quad &\text{(equality; for $a$ much smaller than $R$, drop $2a^2$ next to $R^2$)}
> \end{aligned}$$
>
> $$\boxed{\Omega_{0,\min} = \sqrt{\frac{8gR}{R^2 + 2a^2}} \approx 2\sqrt{\frac{2g}{R}} \quad (a \ll R), \ \text{clockwise}}$$
>
> **Units:** $\sqrt{[\mathrm{L\,T^{-2}}][\mathrm L]/[\mathrm L^2]} = [\mathrm{T^{-1}}]$
> **Meaning:** the weight takes away the same kinetic energy for every metre of climb, so the climb stops after a fixed height whatever the speed. The symbol $\Omega$ of the statement is read here as the initial spin $\Omega_0$, and the graph shows its minimum value against $R$. With $a$ much smaller than $R$, the minimum spin falls like one over the square root of $R$ (graph below): a large yo-yo stores more rotational energy per unit of spin. With the minimum value the yo-yo arrives at the origin with zero spin and then falls again.

![[attachments/EM-SOL/rb39-graph-omega.svg]]

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Kinematics | $\mathbf r^C = -a\,\mathbf i_1 - \xi\,\mathbf j_1$; $\mathbf v^C = \xi\dot\theta\,\mathbf i_1 - (\dot\xi + a\dot\theta)\,\mathbf j_1$; $\mathbf a^C = (\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2)\,\mathbf i_1 + (\xi\dot\theta^2 - \ddot\xi - a\ddot\theta)\,\mathbf j_1$; $\boldsymbol\omega = (\dot\theta + \dot\xi/a)\,\mathbf k_0$; $\boldsymbol\alpha = (\ddot\theta + \ddot\xi/a)\,\mathbf k_0$, with $\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$, $\mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$ |
| (b) Forces and reduction at $C$ | weight $-mg\,\mathbf j_0$ at $C$; tension $F\,\mathbf j_1$ at $T$; $\mathbf F = -mg\sin\theta\,\mathbf i_1 + (F - mg\cos\theta)\,\mathbf j_1$, $\mathbf M_C = aF\,\mathbf k_0$ |
| (c) Equations of motion | $\xi\ddot\theta + 2\dot\xi\dot\theta + a\dot\theta^2 + g\sin\theta = 0$; $m(\ddot\xi + a\ddot\theta - \xi\dot\theta^2) = mg\cos\theta - F$; $\tfrac{mR^2}{2a}(\ddot\theta + \ddot\xi/a) = F$ (unknowns $\xi$, $\theta$, $F$) |
| (d) First integral | $\tfrac m2[\xi^2\dot\theta^2 + (\dot\xi + a\dot\theta)^2] + \tfrac{mR^2}{4}(\dot\theta + \dot\xi/a)^2 - mg(\xi\cos\theta + a\sin\theta) = E_0$ (the tension does no work) |
| (e) Initial acceleration with $\theta = 0$ | $\ddot\xi_0 = 2g/(2 + (R/a)^2)$: $2g/3$ at $R/a = 1$, decreasing to zero like $2g\,a^2/R^2$ |
| (f) Minimum initial spin from $\xi_0 = 2R$ | $\Omega_{0,\min} = \sqrt{8gR/(R^2 + 2a^2)} \approx \sqrt{8g/R}$ for $a \ll R$, clockwise (winding up) |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with a second route and limiting cases.

> [!derivation] Check: part (f) from the constant acceleration of part (e)
> **Law:** integration of a constant acceleration (multiply by the rate and integrate); Barrow's rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 12.8
>
> With $\theta$ zero the second rate of $\xi$ is the constant $c$ of part (e), whatever the velocity. The product of the rate of $\xi$ and its second rate is the derivative of one half of its square (chain rule).
>
> $$\begin{aligned}
> \int_0^t\ddot\xi\,\dot\xi\,dt' &= \int_0^t c\,\dot\xi\,dt' \;\Rightarrow\; \left[\frac{\dot\xi^2}{2}\right]_0^t = c\left[\xi\right]_0^t \quad &\text{(antiderivatives; Barrow's rule)} \\
> \dot\xi^2 &= a^2\Omega_0^2 + 2c\left(\xi - 2R\right) \quad &\text{(initial rate of $\xi$ of magnitude $a\Omega_0$; initial $\xi$ equal to $2R$)} \\
> 0 &\le a^2\Omega_0^2 - 4cR = a^2\Omega_0^2 - \frac{8a^2gR}{2a^2 + R^2} \quad &\text{(at $\xi$ zero; value of $c$)}
> \end{aligned}$$
>
> $$\boxed{\Omega_0^2 \ge \frac{8gR}{R^2 + 2a^2}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the same bound as from the energy: the climbing yo-yo decelerates uniformly, at the rate $c$, and the bound says that it stops exactly at the origin.

**Limiting cases and consistency:**

* **Thin string on the rim.** With $a$ equal to $R$ the acceleration of part (e) is two thirds of $g$, the known value for a uniform disk unwinding from its rim; with $a$ tending to zero it tends to zero: all the work of the weight goes into the spin.
* **Pendulum limit.** With $\xi$ held constant (no unwinding) and $a$ tending to zero, the first equation of part (c) becomes the simple pendulum of length $\xi$, with $g$ times the sine of $\theta$.
* **Ceiling.** The model of the statement treats the ceiling as no obstacle. A real yo-yo touches the ceiling when $\xi$ reaches $R$ (top of the disks at $O$); the energy of part (f) shows that this needs only half of the energy, a squared initial spin of $4gR$ over the sum of the square of $R$ and twice the square of $a$.
* **Dimensions.** Every term of part (c) is an acceleration or a force; every term of the first integral is an energy.

---

## Problem RB-40: Disk on parabolic groove

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous disk $b$ of mass $m$, radius $R$ and centre $G$ rolls without slip inside a fixed cavity whose section is the parabola of the statement (vertex at $O$, depth $3R$, so its rims are at the abscissas plus and minus $2\sqrt3\,R$, where the parabola reaches the height $3R$). The disk stays in contact with the parabola at the point $P$, of abscissa $x_P$. A constant torque $Q\,\mathbf k_0$ acts on the disk through an axle at $G$. Gravity acts downwards. The motion is planar.
* **Fixed frame:** $S_0\{O; \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ at the vertex of the parabola, $\mathbf i_0$ horizontal to the right, $\mathbf j_0$ up, $\mathbf k_0$ out of the paper (⊙). The cavity is at rest, so the frame is inertial. Read from the figure: the arrow of $Q$, drawn above the disk and pointing to the left, turns counterclockwise, the sense of $\mathbf k_0$; a positive $Q$ is a counterclockwise torque.
* **Intrinsic basis of the parabola at P:** $\mathcal B_P\{\mathbf e_t, \mathbf e_n, \mathbf k_0\}$, with $\mathbf e_t$ tangent to the parabola in the sense of growing $x$ and $\mathbf e_n$ normal to it, towards the concave side (into the cavity, towards $G$). It is $\mathcal B_0$ turned by the slope angle $\beta$ of the tangent.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k_0\}$. Read from the figure: $\phi$ is measured at $G$ from the horizontal direction $\mathbf i_0$ to $\mathbf i_b$, counterclockwise.
* **Part (a), degrees of freedom:** a plane body has three coordinates. Contact with the parabola (Notes.pdf, Eq. 13.1) places $G$ at the distance $R$ from $P$ along the normal: the two coordinates $x_P$ and $\phi$ remain. Rolling without slip adds one relation between their rates, which integrates into $\phi$ as a function of $x_P$ (part (d)): **one degree of freedom**, $x_P$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the disk, homogeneous | $m$ | kg |
| Radius of the disk | $R$ | m |
| Moment of inertia about the normal axis through $G$ (statement) | $mR^2/2$ | kg m$^2$ |
| Parabola of the cavity | $y = x^2/(4R)$, depth $3R$, rims at $x = \pm 2\sqrt3\,R$ | m |
| Abscissa of the contact point | $x_P$ | m |
| Constant torque on the disk | $Q\,\mathbf k_0$ | N m |
| Friction coefficient | $\mu$ infinite (no slip) | - |
| Initial state | $x_P = 0$, $\phi = 0$, at rest | m, rad |
| Gravity | $g$, along $-\mathbf j_0$ | m/s$^2$ |
| Shorthand | $s = \sqrt{4R^2 + x_P^2}$ | m |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb40-tangent.svg]]

> [!derivation] Part (a): tangent and normal unit vectors at P
> **Law:** slope of a plane curve; simple rotation about the third axis; chain rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 3.8; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> The slope of the parabola at $P$ is the derivative of $y$ with respect to $x$ at $x_P$. A tangent step of $2R$ along $\mathbf i_0$ rises by $x_P$ along $\mathbf j_0$: the right triangle has the horizontal leg $2R$ (adjacent to $\beta$), the vertical leg $x_P$ (opposite) and the hypotenuse $s$. View with $\mathbf k_0$ out of the paper (⊙): $\mathbf e_n$ is $\mathbf e_t$ turned counterclockwise by a right angle, so its $\mathbf i_0$ component carries the minus sign (for $x_P$ positive the normal leans to the left, towards the axis of the cavity).
>
> $$\begin{aligned}
> \tan\beta &= \frac{d}{dx}\left(\frac{x^2}{4R}\right)\bigg|_{x_P} = \frac{x_P}{2R}, \qquad \cos\beta = \frac{2R}{s}, \qquad \sin\beta = \frac{x_P}{s} \quad &\text{(derivative; adjacent and opposite legs over the hypotenuse)} \\
> \mathbf e_t &= \frac{2R\,\mathbf i_0 + x_P\,\mathbf j_0}{s}, \qquad \mathbf e_n = \mathbf k_0\times\mathbf e_t = \frac{-x_P\,\mathbf i_0 + 2R\,\mathbf j_0}{s} \quad &\text{(legs of the triangle; $\mathbf k_0\times\mathbf i_0 = \mathbf j_0$, $\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> [{}_0R_P] &= \begin{bmatrix} \cos\beta & -\sin\beta & 0 \cr \sin\beta & \cos\beta & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_0R_P] = \cos^2\beta + \sin^2\beta = 1 \quad &\text{(columns $\mathbf e_t$, $\mathbf e_n$, $\mathbf k_0$; expand along the third row)} \\
> [{}_0R_P][{}_0R_P]^T &= \begin{bmatrix} \cos^2\beta + \sin^2\beta & \cos\beta\sin\beta - \sin\beta\cos\beta & 0 \cr \sin\beta\cos\beta - \cos\beta\sin\beta & \sin^2\beta + \cos^2\beta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_0 &= \sin\beta\,\mathbf e_t + \cos\beta\,\mathbf e_n \quad &\text{(second row: the inverse is the transpose)} \\
> \dot\beta &= \frac{d}{dt}\arctan\frac{x_P}{2R} = \frac{1}{1 + x_P^2/(4R^2)}\cdot\frac{\dot x_P}{2R} = \frac{2R\,\dot x_P}{s^2} \quad &\text{(chain rule)} \\
> \dot{\mathbf e}_t &= \dot\beta\,\mathbf k_0\times\mathbf e_t = \dot\beta\,\mathbf e_n, \qquad \dot{\mathbf e}_n = \dot\beta\,\mathbf k_0\times\mathbf e_n = -\dot\beta\,\mathbf e_t \quad &\text{(Poisson)} \\
> \rho_c &= \frac{\left|\dot{\mathbf r}_0^P\right|}{\left|\dot\beta\right|} = \frac{s/(2R)}{2R/s^2} = \frac{s^3}{4R^2} \ge \frac{(2R)^3}{4R^2} = 2R \quad &\text{(radius of curvature: arc rate over turning rate; speed of $P$ taken from the kinematics box below, which does not depend on this one; $s$ smallest at the vertex)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_t = \frac{2R\,\mathbf i_0 + x_P\,\mathbf j_0}{\sqrt{4R^2 + x_P^2}}, \qquad \mathbf e_n = \frac{-x_P\,\mathbf i_0 + 2R\,\mathbf j_0}{\sqrt{4R^2 + x_P^2}}, \qquad \dot\beta = \frac{2R\,\dot x_P}{4R^2 + x_P^2}}$$
>
> **Units:** dimensionless; $[\mathrm{L\,T^{-1}}]/[\mathrm{L^2}] = [\mathrm{T^{-1}}]$; $[\mathrm L]$
> **Meaning:** at the vertex the tangent is $\mathbf i_0$ and the normal $\mathbf j_0$. The parabola is curved most at its vertex, with a radius of curvature of $2R$, larger than the radius of the disk: the disk touches the cavity at one point only, as assumed.

![[attachments/EM-SOL/rb40-rot-phi.svg]]

> [!derivation] Body basis: rotation by phi about k0
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View at $G$ with $\mathbf k_0$ out of the paper (⊙). $\mathbf i_b$ is $\mathbf i_0$ turned counterclockwise by $\phi$: adjacent leg along $\mathbf i_0$ (cosine), opposite leg along $\mathbf j_0$ (sine). $\mathbf j_b$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine), the counterclockwise turn carrying the tip of $\mathbf j_0$ to the left.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0, \qquad \mathbf j_b = -\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_b] &= \begin{bmatrix} \cos\phi & -\sin\phi & 0 \cr \sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_0R_b] = \cos^2\phi + \sin^2\phi = 1 \quad &\text{(columns $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_0$; expand along the third row)} \\
> [{}_0R_b][{}_0R_b]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & \cos\phi\sin\phi - \sin\phi\cos\phi & 0 \cr \sin\phi\cos\phi - \cos\phi\sin\phi & \sin^2\phi + \cos^2\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{b0} &= \dot\phi\,\mathbf k_0, \qquad \boldsymbol\alpha_{b0} = \ddot\phi\,\mathbf k_0 \quad &\text{(simple rotation about the fixed $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\phi\,\mathbf i_0 + \sin\phi\,\mathbf j_0, \qquad \mathbf j_b = -\sin\phi\,\mathbf i_0 + \cos\phi\,\mathbf j_0, \qquad \boldsymbol\omega_{b0} = \dot\phi\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\phi$ is the absolute rotation of the disk; a positive rate of $\phi$ is a counterclockwise spin.

> [!derivation] Part (b): position and velocity of G
> **Law:** position as a sum of segments; chain rule; derivative of a unit vector of a turning basis (Poisson)
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 13.1; [Lecture 7, Slide 6]
>
> The centre of the disk lies on the normal at the contact point, at the distance $R$ on the concave side.
>
> $$\begin{aligned}
> \mathbf r_0^P &= x_P\,\mathbf i_0 + \frac{x_P^2}{4R}\,\mathbf j_0, \qquad \dot{\mathbf r}_0^P = \dot x_P\,\mathbf i_0 + \frac{x_P\dot x_P}{2R}\,\mathbf j_0 = \dot x_P\,\frac{s}{2R}\,\mathbf e_t \quad &\text{(chain rule; $2R\,\mathbf i_0 + x_P\,\mathbf j_0$ is $s\,\mathbf e_t$)} \\
> \mathbf r_0^G &= \mathbf r_0^P + R\,\mathbf e_n = \left(x_P - \frac{R\,x_P}{s}\right)\mathbf i_0 + \left(\frac{x_P^2}{4R} + \frac{2R^2}{s}\right)\mathbf j_0 \quad &\text{(sum of segments; $\mathbf e_n$ of the previous box)} \\
> \mathbf v_0^G &= \dot{\mathbf r}_0^P + R\,\dot{\mathbf e}_n = \dot x_P\,\frac{s}{2R}\,\mathbf e_t - R\,\dot\beta\,\mathbf e_t \quad &\text{(derivative of the sum; Poisson)} \\
> &= \dot x_P\left(\frac{s}{2R} - \frac{2R^2}{s^2}\right)\mathbf e_t \quad &\text{(rate of $\beta$ from the first box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \left(x_P - \frac{R\,x_P}{\sqrt{4R^2 + x_P^2}}\right)\mathbf i_0 + \left(\frac{x_P^2}{4R} + \frac{2R^2}{\sqrt{4R^2 + x_P^2}}\right)\mathbf j_0, \qquad \mathbf v_0^G = \dot x_P\left(\frac{s}{2R} - \frac{2R^2}{s^2}\right)\mathbf e_t, \qquad \boldsymbol\omega_{b0} = \dot\phi\,\mathbf k_0}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$ (the bracket is dimensionless)
> **Meaning:** $G$ moves parallel to the tangent at $P$. At the vertex the bracket is one half: $G$ is on a curve of radius of curvature $2R$ minus $R$, half that of the parabola, so it moves at half the speed of the contact point.

> [!derivation] Rolling without slip at P
> **Law:** velocity field of the rigid body; rolling without slipping on a body at rest
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> \mathbf v_0^{P(b)} &= \mathbf v_0^G + \dot\phi\,\mathbf k_0\times\left(-R\,\mathbf e_n\right) = \mathbf v_0^G + R\dot\phi\,\mathbf e_t \quad &\text{(velocity field from $G$, Eq. 9.3; $\mathbf k_0\times\mathbf e_n = -\mathbf e_t$)} \\
> &= \left[\dot x_P\left(\frac{s}{2R} - \frac{2R^2}{s^2}\right) + R\dot\phi\right]\mathbf e_t = \mathbf 0 \quad &\text{(no slip on the fixed cavity, Eq. 13.5)} \\
> \dot\phi &= -f(x_P)\,\dot x_P, \qquad f(x_P) = \frac{s}{2R^2} - \frac{2R}{s^2} \quad &\text{(solve for the rate of $\phi$)} \\
> \mathbf v_0^G &= -R\dot\phi\,\mathbf e_t \quad &\text{(the bracket of the previous box is $R$ times $f$)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi = -\left(\frac{\sqrt{4R^2 + x_P^2}}{2R^2} - \frac{2R}{4R^2 + x_P^2}\right)\dot x_P, \qquad \mathbf v_0^G = -R\dot\phi\,\mathbf e_t}$$
>
> **Units:** $[\mathrm{L^{-1}}][\mathrm{L\,T^{-1}}] = [\mathrm{T^{-1}}]$
> **Meaning:** $f$ is positive for every $x_P$ (its first term is at least $1/R$ and its second at most $1/(2R)$): moving to the right the disk turns clockwise, and moving to the left counterclockwise. The speed of $G$ is exactly $R$ times the spin.

> [!derivation] Part (d): phi as a function of x_P
> **Law:** integration of the rolling relation; antiderivatives (the hint, verified by differentiation, and the arctangent); Barrow's rule
> **Source:** Notes.pdf, Eq. 13.3; Notes.pdf, Eq. 13.5; Problems.pdf, p. 69
>
> Integrate from the initial state, $x_P$ and $\phi$ zero, with the substitution $u = x_P(t')$, $du = \dot x_P\,dt'$. Write $A(u)$ for the antiderivative of the hint with $a$ equal to $R$.
>
> $$\begin{aligned}
> \int_0^{\phi}d\phi' &= -\int_0^{x_P}\left(\frac{\sqrt{u^2 + 4R^2}}{2R^2} - \frac{2R}{u^2 + 4R^2}\right)du \quad &\text{(separate; substitution $du = \dot x_P\,dt'$)} \\
> A(u) &= \frac{u\sqrt{u^2 + 4R^2}}{4R^2} + \ln\left(\sqrt{u^2 + 4R^2} + u\right) \quad &\text{(hint with $a$ equal to $R$)} \\
> \frac{dA}{du} &= \frac{\sqrt{u^2 + 4R^2}}{4R^2} + \frac{u^2}{4R^2\sqrt{u^2 + 4R^2}} + \frac{1 + u/\sqrt{u^2 + 4R^2}}{\sqrt{u^2 + 4R^2} + u} \quad &\text{(product rule; chain rule)} \\
> &= \frac{2u^2 + 4R^2}{4R^2\sqrt{u^2 + 4R^2}} + \frac{1}{\sqrt{u^2 + 4R^2}} = \frac{u^2 + 4R^2}{2R^2\sqrt{u^2 + 4R^2}} = \frac{\sqrt{u^2 + 4R^2}}{2R^2} \quad &\text{(common denominators: the hint is right)} \\
> \int\frac{2R\,du}{u^2 + 4R^2} &= \int\frac{dv}{1 + v^2} = \arctan v = \arctan\frac{u}{2R} \quad &\text{(substitution $v = u/(2R)$, $du = 2R\,dv$)} \\
> \left[\phi'\right]_0^{\phi} &= -\left[A(u) - \arctan\frac{u}{2R}\right]_0^{x_P} = -\left[\frac{x_P\,s}{4R^2} + \ln\left(s + x_P\right) - \ln 2R - \arctan\frac{x_P}{2R}\right] \quad &\text{(Barrow's rule; $A(0) = \ln 2R$, $\arctan 0 = 0$)}
> \end{aligned}$$
>
> $$\boxed{\phi(x_P) = -\frac{x_P\sqrt{4R^2 + x_P^2}}{4R^2} - \ln\frac{x_P + \sqrt{4R^2 + x_P^2}}{2R} + \arctan\frac{x_P}{2R}}$$
>
> **Units:** dimensionless in every term (the logarithm has a dimensionless argument after Barrow's rule)
> **Meaning:** $R$ times the first two terms is the arc length of the parabola from $O$ to $P$, and the last term is the slope angle $\beta$: the disk turns clockwise by the arc rolled over $R$, and the turning of the tangent gives back $\beta$ (equal arcs, Eq. 13.3). The function is odd. At the left rim, with $x_P$ equal to minus $2\sqrt3\,R$, it is $2\sqrt3 + \ln(2 + \sqrt3) - \pi/3$, that is 3.734 rad.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass and moment of inertia of the disk
> **Law:** symmetry of the homogeneous disk; moment of inertia as an area integral in polar coordinates (jacobian $\rho$)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.5; Notes.pdf, Sec. 10.3; [Lecture 8, Slide 16]
>
> Polar coordinates $(\rho, \chi)$ about $G$, area element $\rho\,d\rho\,d\chi$, surface density $\sigma$ equal to $m$ over $\pi R^2$. $G$ is the centre of the disk by symmetry, and $\mathbf k_0$ is a principal axis (the disk is symmetric about its plane).
>
> $$\begin{aligned}
> I &= \sigma\int_0^{2\pi}\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R \quad &\text{(Eq. 10.11; separable integral; antiderivatives)} \\
> &= \sigma\cdot 2\pi\cdot\frac{R^4}{4} = \frac{m}{\pi R^2}\cdot\frac{\pi R^4}{2} = \frac{mR^2}{2} \quad &\text{(Barrow's rule; value of $\sigma$)}
> \end{aligned}$$
>
> $$\boxed{I = \frac{mR^2}{2}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the datum of the statement; the plane motion needs only this component.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and energies
> **Law:** linear momentum from $G$; angular momentum about $G$ about a principal axis; kinetic energy about $G$; potential of the weight
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 12.34
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = -mR\dot\phi\,\mathbf e_t, \qquad \mathbf H_G = \frac{mR^2}{2}\,\dot\phi\,\mathbf k_0 \quad &\text{(Eq. 11.3 with rolling; Eq. 11.12)} \\
> T_0 &= \frac12\,m\left(R\dot\phi\right)^2 + \frac12\cdot\frac{mR^2}{2}\,\dot\phi^2 = \frac{mR^2}{2}\dot\phi^2 + \frac{mR^2}{4}\dot\phi^2 = \frac34\,mR^2\dot\phi^2 \quad &\text{(Eq. 11.31; speed of $G$ equal to $R$ times the spin)} \\
> V_0 &= m\,g\,\mathbf r_0^G\cdot\mathbf j_0 = m\,g\left(\frac{x_P^2}{4R} + \frac{2R^2}{s}\right) \quad &\text{(Eq. 12.34; height of $G$ from part (b))}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = \frac{mR^2}{2}\dot\phi\,\mathbf k_0, \qquad T_0 = \frac34\,mR^2\dot\phi^2, \qquad V_0 = mg\left(\frac{x_P^2}{4R} + \frac{2R^2}{\sqrt{4R^2 + x_P^2}}\right)}$$
>
> **Units:** kg m$^2$/s; J
> **Meaning:** two thirds of the kinetic energy is in the motion of $G$ and one third in the spin. At the start $G$ is at the height $R$ above $O$; at a rim, at $3.5R$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb40-fbd.svg]]

| Force on the disk | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf j_0 = -mg(\sin\beta\,\mathbf e_t + \cos\beta\,\mathbf e_n)$ | applied |
| Torque of the axle | couple on the disk (axle through $G$) | $Q\,\mathbf k_0$ | applied |
| Normal reaction of the cavity | $P$ | $N\,\mathbf e_n$, with $N \ge 0$ (pushes the disk towards the concave side) | constraint |
| Friction of the cavity | $P$ | $T_f\,\mathbf e_t$ (unknown: no slip, $\mu$ infinite) | constraint |

> [!derivation] Part (c): resultant force and moment about G
> **Law:** sum of forces; moment of a force about $G$ by a determinant expanded along the first row; a couple has the same moment about every point
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> The arm of the contact force from $G$ is minus $R\,\mathbf e_n$; the weight acts at $G$.
>
> $$\begin{aligned}
> \mathbf F &= \left(T_f - mg\sin\beta\right)\mathbf e_t + \left(N - mg\cos\beta\right)\mathbf e_n \quad &\text{(sum by components; $\mathbf j_0$ in $\mathcal B_P$)} \\
> -R\,\mathbf e_n\times\left(T_f\,\mathbf e_t + N\,\mathbf e_n\right) &= \begin{vmatrix} \mathbf e_t & \mathbf e_n & \mathbf k_0 \cr 0 & -R & 0 \cr T_f & N & 0 \end{vmatrix} = R\,T_f\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \mathbf M_G &= Q\,\mathbf k_0 + R\,T_f\,\mathbf k_0 \quad &\text{(couple plus moment of the contact force)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = \left(T_f - mg\sin\beta\right)\mathbf e_t + \left(N - mg\cos\beta\right)\mathbf e_n, \qquad \mathbf M_G = \left(Q + R\,T_f\right)\mathbf k_0, \qquad \sin\beta = \frac{x_P}{s}, \ \cos\beta = \frac{2R}{s}}$$
>
> **Units:** N; N m
> **Meaning:** the contact adds two unknowns, $N$ and $T_f$, to the coordinate $x_P$.

> [!derivation] Equations of motion
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass; elimination of the friction
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole. The acceleration of $G$ is the derivative of minus $R$ times the rate of $\phi$ times $\mathbf e_t$ (product rule, Poisson for $\mathbf e_t$).
>
> $$\begin{aligned}
> \mathbf a_0^G &= -R\ddot\phi\,\mathbf e_t - R\dot\phi\,\dot{\mathbf e}_t = -R\ddot\phi\,\mathbf e_t - R\dot\phi\dot\beta\,\mathbf e_n \quad &\text{(product rule; Poisson)} \\
> -mR\ddot\phi &= T_f - mg\sin\beta \quad &\text{(force along $\mathbf e_t$)} \\
> -mR\dot\phi\dot\beta &= N - mg\cos\beta \quad &\text{(force along $\mathbf e_n$)} \\
> \frac{mR^2}{2}\,\ddot\phi &= Q + R\,T_f \quad &\text{(moment along $\mathbf k_0$)} \\
> \frac{mR^2}{2}\,\ddot\phi &= Q + mgR\sin\beta - mR^2\ddot\phi \quad &\text{(friction from the first force equation)}
> \end{aligned}$$
>
> $$\boxed{\frac32\,mR^2\ddot\phi = Q + mgR\,\frac{x_P}{\sqrt{4R^2 + x_P^2}}, \qquad T_f = mg\sin\beta - mR\ddot\phi, \qquad N = mg\cos\beta - mR\dot\phi\dot\beta}$$
>
> **Units:** N m in the first equation; N in the other two
> **Meaning:** three equations for the three unknowns $x_P$ (with $\phi$ tied to it by part (d)), $T_f$ and $N$. On the right-hand side of the cavity gravity gives a positive (counterclockwise) moment that rolls the disk back to the left; a positive torque does the same everywhere. In either direction of motion the rates of $\phi$ and $\beta$ have opposite signs, so $N$ exceeds the normal component of the weight.

> [!derivation] Part (e): first-order equation for x_P
> **Law:** energy theorem with the power of the torque; the contact force does no work (its body point is at rest); Barrow's rule
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 13.5
>
> The power of the contact force is its dot product with the velocity of the body point $P$, which is zero; the power of the torque is $Q$ times the rate of $\phi$ (statement); the weight derives from $V_0$. Integrate from the initial rest, where $\phi$ is zero and $V_0$ is $mgR$.
>
> $$\begin{aligned}
> \frac{dT_0}{dt} &= Q\dot\phi - \frac{dV_0}{dt} \quad &\text{(energy theorem, Eq. 12.30 per unit time; power Eq. 12.29)} \\
> \int_0^t\frac{d}{dt'}\left(T_0 + V_0 - Q\phi\right)dt' &= \left[T_0 + V_0 - Q\phi\right]_0^t = 0 \quad &\text{($Q$ constant; antiderivative; Barrow's rule)} \\
> \frac34\,mR^2\dot\phi^2 + mg\left(\frac{x_P^2}{4R} + \frac{2R^2}{s}\right) - Q\phi &= 0 + mgR - 0 \quad &\text{(values at the start)} \\
> \frac34\,mR^2 f(x_P)^2\,\dot x_P^2 &= Q\,\phi(x_P) - mg\left(\frac{x_P^2}{4R} + \frac{2R^2}{s} - R\right) \quad &\text{(rate of $\phi$ equal to minus $f$ times the rate of $x_P$)}
> \end{aligned}$$
>
> $$\boxed{\dot x_P^2 = \frac{4\left[Q\,\phi(x_P) - mg\left(\dfrac{x_P^2}{4R} + \dfrac{2R^2}{\sqrt{4R^2 + x_P^2}} - R\right)\right]}{3mR^2\left(\dfrac{\sqrt{4R^2 + x_P^2}}{2R^2} - \dfrac{2R}{4R^2 + x_P^2}\right)^2}, \qquad x_P(0) = 0}$$
>
> **Units:** numerator J; denominator kg ($f$ is an inverse length); quotient m$^2$/s$^2$
> **Meaning:** the only unknown is $x_P$, with $\phi(x_P)$ of part (d). Until the first turning point, the first-order equation is the square root with the sign opposite to $Q$ (if the torque is too small the disk stops and rolls back, and the sign changes): with $Q$ positive the second rate of $\phi$ starts at $2Q/(3mR^2)$, positive, so $\phi$ grows and $x_P$ decreases (the disk climbs the left-hand side). At $x_P$ zero the right-hand side vanishes; as in any start from rest, the second-order equation selects the motion.

> [!derivation] Part (f): condition to leave the cavity
> **Law:** the first-order equation of part (e) must keep a positive right-hand side all the way to the rim
> **Source:** Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Problems.pdf, p. 69
>
> Take $Q$ positive (a negative $Q$ is the mirror image, towards the right-hand rim). The disk moves left; write $z$ for minus $x_P$ over $R$, from 0 to $2\sqrt3$ at the left rim. Because $\phi$ is odd, $\phi(x_P)$ is $\Phi(z)$, the bracket of part (d) evaluated at $z$, which is positive. The disk gets out when the contact point reaches the rim with the right-hand side still positive at every intermediate point.
>
> $$\begin{aligned}
> \Phi(z) &= \frac{z\sqrt{4 + z^2}}{4} + \ln\frac{z + \sqrt{4 + z^2}}{2} - \arctan\frac z2, \qquad Y(z) = \frac{z^2}{4} + \frac{2}{\sqrt{4 + z^2}} - 1 \quad &\text{(part (d) and the height of $G$ over $R$, minus 1, in terms of $z$)} \\
> Q\,\Phi(z) - mgR\,Y(z) &\gt 0 \;\Leftrightarrow\; \frac{Q}{mgR} \gt \frac{Y(z)}{\Phi(z)} \quad \text{for every } z \in \left(0, 2\sqrt3\right] \quad &\text{(positive kinetic energy; $\Phi$ positive)} \\
> \Phi\left(2\sqrt3\right) &= \frac{2\sqrt3\cdot 4}{4} + \ln\frac{2\sqrt3 + 4}{2} - \arctan\sqrt3 = 2\sqrt3 + \ln\left(2 + \sqrt3\right) - \frac\pi3 \quad &\text{(at the rim, the square root is 4)} \\
> Y\left(2\sqrt3\right) &= 3 + \frac12 - 1 = \frac52 \quad &\text{(the rim: $G$ at $3.5R$)} \\
> Q_c &= \frac{5\,mgR}{2\left(2\sqrt3 + \ln\left(2 + \sqrt3\right) - \pi/3\right)} = \frac{2.5}{3.7339}\,mgR \approx 0.6695\,mgR \quad &\text{(the ratio $Y/\Phi$ grows with $z$, table below: its largest value is at the rim)}
> \end{aligned}$$
>
> $$\boxed{|Q| \gt Q_c = \frac{5\,mgR}{2\left(2\sqrt3 + \ln(2 + \sqrt3) - \pi/3\right)} \approx 0.670\,mgR}$$
>
> **Units:** N m on both sides
> **Meaning:** why the rim decides: the weight adds the rise $dY$ for a turn $d\Phi$ at the rate given by the sine of the angle of the groove, which increases with $z$ from zero, so $Y$ is convex in $\Phi$ with both starting at zero and the ratio $Y/\Phi$ increases up to the rim (the table shows it). The work of the torque over the rotation 3.734 rad must exceed the rise of $G$ from $R$ to $3.5R$. With $Q$ exactly $Q_c$ the disk would reach the rim at rest and roll back, because there the moment of the weight, $mgR$ times the sine of 60 degrees, about $0.866\,mgR$, exceeds $Q_c$.

| $z = -x_P/R$ | $\Phi(z)$ (rad) | $Y(z)$ | $Y/\Phi$ |
| :--- | :--- | :--- | :--- |
| 0.5 | 0.2602 | 0.0326 | 0.1255 |
| 1 | 0.5766 | 0.1444 | 0.2505 |
| 2 | 1.5102 | 0.7071 | 0.4682 |
| 3 | 2.9161 | 1.8047 | 0.6189 |
| $2\sqrt3 \approx 3.464$ (rim) | 3.7339 | 2.5000 | 0.6695 |

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom; tangent and normal | one ($x_P$); $\mathbf e_t = (2R\,\mathbf i_0 + x_P\,\mathbf j_0)/\sqrt{4R^2 + x_P^2}$, $\mathbf e_n = (-x_P\,\mathbf i_0 + 2R\,\mathbf j_0)/\sqrt{4R^2 + x_P^2}$ |
| (b) Kinematics | $\mathbf r^G = \mathbf r^P + R\,\mathbf e_n$ (components in part (b)); $\mathbf v^G = \dot x_P(s/(2R) - 2R^2/s^2)\,\mathbf e_t$; $\boldsymbol\omega = \dot\phi\,\mathbf k_0$; rolling: $\dot\phi = -(s/(2R^2) - 2R/s^2)\,\dot x_P$ |
| (c) Forces and reduction at $G$ | $-mg\,\mathbf j_0$ at $G$; $N\,\mathbf e_n + T_f\,\mathbf e_t$ at $P$; couple $Q\,\mathbf k_0$; $\mathbf F = (T_f - mg\sin\beta)\,\mathbf e_t + (N - mg\cos\beta)\,\mathbf e_n$, $\mathbf M_G = (Q + RT_f)\,\mathbf k_0$ |
| (d) $\phi(x_P)$ | $\phi = -\tfrac{x_P s}{4R^2} - \ln\tfrac{x_P + s}{2R} + \arctan\tfrac{x_P}{2R}$ |
| (e) First-order equation | $\tfrac34 mR^2 f(x_P)^2\,\dot x_P^2 = Q\,\phi(x_P) - mg(\tfrac{x_P^2}{4R} + \tfrac{2R^2}{s} - R)$, $f = s/(2R^2) - 2R/s^2$, $x_P(0) = 0$ |
| (f) Leaving the cavity | $\lvert Q\rvert > 5mgR/[2(2\sqrt3 + \ln(2 + \sqrt3) - \pi/3)] \approx 0.670\,mgR$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with a second route and limiting cases.

> [!derivation] Check: the energy equation from the Newton-Euler equations
> **Law:** the equation of motion multiplied by the rate of $\phi$; chain rule on the height of $G$
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.33
>
> $$\begin{aligned}
> \frac{d}{dx_P}\left(\frac{x_P^2}{4R} + \frac{2R^2}{s}\right) &= \frac{x_P}{2R} - \frac{2R^2 x_P}{s^3} = R\,\frac{x_P}{s}\left(\frac{s}{2R^2} - \frac{2R}{s^2}\right) = R\sin\beta\,f(x_P) \quad &\text{(chain rule on $s$; factor out $R\sin\beta$)} \\
> \frac{dV_0}{dt} &= mgR\sin\beta\,f\,\dot x_P = -mgR\sin\beta\,\dot\phi \quad &\text{(chain rule; rolling)} \\
> \frac{d}{dt}\left(\frac34\,mR^2\dot\phi^2\right) &= \frac32\,mR^2\dot\phi\ddot\phi = \left(Q + mgR\sin\beta\right)\dot\phi = Q\dot\phi - \frac{dV_0}{dt} \quad &\text{(chain rule; equation of motion times the rate of $\phi$)}
> \end{aligned}$$
>
> $$\boxed{\frac{dT_0}{dt} = Q\dot\phi - \frac{dV_0}{dt}}$$
>
> **Units:** W in every term
> **Meaning:** the Newton-Euler equation gives exactly the power balance used in part (e): the reactions do no work.

**Limiting cases and consistency:**

* **No torque.** With $Q$ zero the disk released at the vertex stays there: the equation of motion has zero right-hand side at $x_P$ zero, and the first-order equation gives no motion. Near the vertex the slope sine is about $x_P/(2R)$ and $\phi$ about minus $x_P/(2R)$, so the equation of motion becomes three halves of $R$ times the second rate of $\phi$ equal to minus $g$ times $\phi$: small oscillations with the squared angular frequency $2g/(3R)$, the value of a disk rolling in a circular track of radius $2R$ (centre path of radius $R$).
* **Insufficient torque.** The ratio of the table grows continuously from zero at the vertex to 0.6695 at the rim. For $Q$ between zero and $Q_c$ it therefore equals $Q/(mgR)$ at some point short of the rim, where the right-hand side of part (e) vanishes: the disk stops there and rolls back.
* **Edge of the cavity (extension).** The statement keeps the disk on the parabola; beyond the rim the disk would pivot about the corner, turning a further 60 degrees while $G$ rises from $3.5R$ to $4R$. If it kept rolling round the corner without losing contact, the energy condition along that pivot raises the threshold slightly, to about $0.678\,mgR$ (largest ratio of the potential rise to the rotation, reached with the line from the corner to $G$ at about 43 degrees from the vertical).
* **Dimensions.** Every term of the energy equation is an energy; $Q_c$ is a multiple of $mgR$.

---

## Problem RB-41: Sail sledge

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** the sledge $b$, a rigid body of mass $m$ with centre of mass $G$ at a negligible height above the ice and moment of inertia $I$ about the vertical axis through $G$, slides on a horizontal sheet of ice on three blades $A$, $B$ and $C$. Each blade slides freely along its own direction and cannot slip across it. The wind acts on the sail at the centre of pressure $P$, at the height $\ell$ above $G$.
* **Fixed frame:** $S_0\{O; \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ with $\mathbf i_0$ and $\mathbf j_0$ on the ice and $\mathbf k_0$ vertical, up, out of the paper in the top view of the figure (⊙); gravity points into the paper (⊗), along minus $\mathbf k_0$. The ice is at rest, so the frame is inertial. The wind blows along $\mathbf j_0$ with the ground speed $U_\infty$.
* **Body frame:** $S_b\{G; \mathbf i_b, \mathbf j_b, \mathbf k_0\}$, with $\mathbf i_b$ along the axis of the sledge, from the rear blade $C$ through $G$ towards the front. Read from the figure: $\psi$ is measured at $G$ from the direction of $\mathbf i_0$ to $\mathbf i_b$, counterclockwise in the top view.
* **Blades (read from the figure):** $C$ lies on the axis behind $G$, and $A$ (on the side of $\mathbf j_b$) and $B$ (on the side of minus $\mathbf j_b$) lie on a line normal to the axis, ahead of $G$. The blades at $A$ and $B$ are parallel to $\mathbf i_b$; the blade at $C$ is turned from $\mathbf i_b$ by $\theta$, counterclockwise in the top view. The opposite reading of $\theta$ (clockwise) would replace $\theta$ by its opposite in parts (b) and (c); parts (e) and (f) use $\theta$ zero and do not change. $\theta$ is a fixed setting of the blade.
* **Degrees of freedom:** while the three blades stay on the ice, the sledge moves in the plane of the ice: three coordinates $x$, $y$, $\psi$. Each blade gives one condition on the velocities; the conditions at $A$ and $B$ turn out to be the same (blade conditions, below), so there are two independent conditions and **one degree of freedom** remains. For a fixed $\theta$ other than zero the motion is a rotation about a point $I$ fixed on the ice (part (b)), so the two conditions fix $x$ and $y$ as functions of $\psi$: they are integrable for a fixed blade setting.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the sledge | $m$ | kg |
| Moment of inertia about the vertical axis through $G$ | $I$ | kg m$^2$ |
| Side of the triangle of blades | $\sqrt3\,\ell$ | m |
| Height of the centre of pressure above $G$ | $\ell$ | m |
| Angle of the blade at $C$ from $\mathbf i_b$ | $\theta$ (fixed) | rad |
| Aerodynamic constants | $b_L$, $b_D$ | kg/m |
| Ground speed of the wind | $U_\infty$, along $\mathbf j_0$ | m/s |
| Gravity | $g$, along $-\mathbf k_0$ | m/s$^2$ |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb41-rot-psi.svg]]

> [!derivation] Body basis: rotation by psi about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> Top view with $\mathbf k_0$ out of the paper (⊙): a positive $\psi$ turns counterclockwise. $\mathbf i_b$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\psi$), opposite leg along $\mathbf j_0$ (sine). $\mathbf j_b$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine): the counterclockwise turn carries the tip of $\mathbf j_0$ to the left, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_b = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_b] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_0R_b] = 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(columns $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_0$; expand along the third row)} \\
> [{}_0R_b][{}_0R_b]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_0 &= \cos\psi\,\mathbf i_b - \sin\psi\,\mathbf j_b, \qquad \mathbf j_0 = \sin\psi\,\mathbf i_b + \cos\psi\,\mathbf j_b \quad &\text{(rows: the inverse is the transpose)} \\
> \dot{\mathbf i}_b &= \dot\psi\,\mathbf k_0\times\mathbf i_b = \dot\psi\,\mathbf j_b, \qquad \dot{\mathbf j}_b = \dot\psi\,\mathbf k_0\times\mathbf j_b = -\dot\psi\,\mathbf i_b \quad &\text{(Poisson, with $\boldsymbol\omega_{b0} = \dot\psi\,\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_b = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \boldsymbol\omega_{b0} = \dot\psi\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** with $\psi$ zero the sledge points along $\mathbf i_0$, across the wind.

> [!derivation] Part (a): kinematics of G and of the sledge
> **Law:** position of the centre of mass in the fixed frame; time derivatives; simple rotation
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> $G$ stays at its (negligible) height on the ice; its position is given by the coordinates $x$ and $y$. The components of the velocity of $G$ in $\mathcal B_b$ are called $u$ (forward) and $w$ (sideways); they follow from the rows of the previous box.
>
> $$\begin{aligned}
> \mathbf r_0^G &= x\,\mathbf i_0 + y\,\mathbf j_0, \qquad \mathbf v_0^G = \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0, \qquad \mathbf a_0^G = \ddot x\,\mathbf i_0 + \ddot y\,\mathbf j_0 \quad &\text{($\mathbf i_0$, $\mathbf j_0$ constant)} \\
> \boldsymbol\omega_{b0} &= \dot\psi\,\mathbf k_0, \qquad \boldsymbol\alpha_{b0} = \ddot\psi\,\mathbf k_0 \quad &\text{(simple rotation; $\mathbf k_0$ constant)} \\
> u &= \mathbf v_0^G\cdot\mathbf i_b = \dot x\cos\psi + \dot y\sin\psi, \qquad w = \mathbf v_0^G\cdot\mathbf j_b = -\dot x\sin\psi + \dot y\cos\psi \quad &\text{(projections on the body basis)} \\
> \mathbf a_0^G &= \frac{d}{dt}\left(u\,\mathbf i_b + w\,\mathbf j_b\right) = \left(\dot u - w\dot\psi\right)\mathbf i_b + \left(\dot w + u\dot\psi\right)\mathbf j_b \quad &\text{(product rule; Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = x\,\mathbf i_0 + y\,\mathbf j_0, \quad \mathbf v_0^G = \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0, \quad \mathbf a_0^G = \ddot x\,\mathbf i_0 + \ddot y\,\mathbf j_0, \quad \boldsymbol\omega_{b0} = \dot\psi\,\mathbf k_0, \quad \boldsymbol\alpha_{b0} = \ddot\psi\,\mathbf k_0}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}]$; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the body-basis form of the acceleration will be used with the blade conditions, which are written in $\mathcal B_b$.

![[attachments/EM-SOL/rb41-blades.svg]]

> [!derivation] Position of the blades and their directions
> **Law:** geometry of the equilateral triangle (its centre divides each median in the ratio 2 to 1); simple rotation by theta
> **Source:** Notes.pdf, Eq. 9.16; Problems.pdf, p. 70
>
> The median of the triangle, from $C$ to the midpoint $M$ of $AB$, lies on the axis and has the length of the side times the sine of 60 degrees. $G$ is two thirds of the way from $C$ to $M$. In the right triangle $GMA$ the leg $GM$ is along $\mathbf i_b$, the leg $MA$ along $\mathbf j_b$ (half the side) and the hypotenuse is $GA$. The blade at $C$ is $\mathbf i_b$ turned counterclockwise by $\theta$ (adjacent leg along $\mathbf i_b$, cosine; opposite leg along $\mathbf j_b$, sine); its normal on the ice is $\mathbf k_0$ crossed with it.
>
> $$\begin{aligned}
> CM &= \sqrt3\,\ell\cdot\frac{\sqrt3}{2} = \frac{3\ell}{2}, \qquad GC = \frac23\cdot\frac{3\ell}{2} = \ell, \qquad GM = \frac13\cdot\frac{3\ell}{2} = \frac{\ell}{2}, \qquad MA = \frac{\sqrt3\,\ell}{2} \quad &\text{(median; ratio 2 to 1; half side)} \\
> GA &= \sqrt{\frac{\ell^2}{4} + \frac{3\ell^2}{4}} = \ell \quad &\text{(Pythagoras in $GMA$: the three blades are at $\ell$ from $G$)} \\
> \overrightarrow{GA} &= \frac{\ell}{2}\,\mathbf i_b + \frac{\sqrt3\,\ell}{2}\,\mathbf j_b, \qquad \overrightarrow{GB} = \frac{\ell}{2}\,\mathbf i_b - \frac{\sqrt3\,\ell}{2}\,\mathbf j_b, \qquad \overrightarrow{GC} = -\ell\,\mathbf i_b, \qquad \overrightarrow{GP} = \ell\,\mathbf k_0 \quad &\text{(legs; $C$ behind $G$; $P$ above $G$)} \\
> \mathbf e_C &= \cos\theta\,\mathbf i_b + \sin\theta\,\mathbf j_b, \qquad \mathbf n_C = \mathbf k_0\times\mathbf e_C = -\sin\theta\,\mathbf i_b + \cos\theta\,\mathbf j_b \quad &\text{(blade at $C$ and its normal on the ice)}
> \end{aligned}$$
>
> $$\boxed{\overrightarrow{GA} = \frac{\ell}{2}\,\mathbf i_b + \frac{\sqrt3\,\ell}{2}\,\mathbf j_b, \quad \overrightarrow{GB} = \frac{\ell}{2}\,\mathbf i_b - \frac{\sqrt3\,\ell}{2}\,\mathbf j_b, \quad \overrightarrow{GC} = -\ell\,\mathbf i_b, \quad \mathbf n_C = -\sin\theta\,\mathbf i_b + \cos\theta\,\mathbf j_b}$$
>
> **Units:** $[\mathrm L]$; dimensionless
> **Meaning:** the blades at $A$ and $B$ are $\sqrt3\,\ell$ apart, and they stand $\ell/2$ ahead of $G$; the rear blade is $\ell$ behind it.

> [!derivation] Blade conditions: velocities of the blade points
> **Law:** velocity field of the rigid body; a blade cannot slip across its own direction
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> $$\begin{aligned}
> \mathbf v_0^A &= u\,\mathbf i_b + w\,\mathbf j_b + \dot\psi\,\mathbf k_0\times\left(\frac{\ell}{2}\,\mathbf i_b + \frac{\sqrt3\,\ell}{2}\,\mathbf j_b\right) = \left(u - \frac{\sqrt3\,\ell}{2}\dot\psi\right)\mathbf i_b + \left(w + \frac{\ell}{2}\dot\psi\right)\mathbf j_b \quad &\text{(Eq. 9.3; $\mathbf k_0\times\mathbf i_b = \mathbf j_b$, $\mathbf k_0\times\mathbf j_b = -\mathbf i_b$)} \\
> \mathbf v_0^B &= \left(u + \frac{\sqrt3\,\ell}{2}\dot\psi\right)\mathbf i_b + \left(w + \frac{\ell}{2}\dot\psi\right)\mathbf j_b \quad &\text{(same with the opposite $\mathbf j_b$ component of the arm)} \\
> \mathbf v_0^C &= u\,\mathbf i_b + w\,\mathbf j_b + \dot\psi\,\mathbf k_0\times\left(-\ell\,\mathbf i_b\right) = u\,\mathbf i_b + \left(w - \ell\dot\psi\right)\mathbf j_b \quad &\text{(Eq. 9.3)} \\
> \mathbf v_0^A\cdot\mathbf j_b &= w + \frac{\ell}{2}\dot\psi = 0, \qquad \mathbf v_0^B\cdot\mathbf j_b = w + \frac{\ell}{2}\dot\psi = 0 \quad &\text{(no slip across $A$ and $B$: one and the same condition)} \\
> \mathbf v_0^C\cdot\mathbf n_C &= -u\sin\theta + \left(w - \ell\dot\psi\right)\cos\theta = 0 \quad &\text{(no slip across $C$)} \\
> w &= -\frac{\ell}{2}\dot\psi, \qquad u\sin\theta = -\frac{3\ell}{2}\dot\psi\cos\theta \quad &\text{(substitute $w$ in the condition at $C$)}
> \end{aligned}$$
>
> $$\boxed{w = -\frac{\ell}{2}\,\dot\psi, \qquad u = -\frac{3\ell}{2}\,\dot\psi\cot\theta \quad (\theta \neq 0); \qquad \theta = 0:\ \ \dot\psi = 0, \ w = 0, \ u \text{ free}}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$ in each term
> **Meaning:** with the rear blade turned counterclockwise ($\theta$ positive and less than a right angle), forward motion ($u$ positive) needs a negative rate of $\psi$: the sledge turns clockwise, like a vehicle steered by its rear wheel. With $\theta$ zero all blades are parallel: the sledge can only slide straight along $\mathbf i_b$.

> [!derivation] Part (b): instantaneous centre of rotation
> **Law:** instantaneous axis of rotation of a plane motion; velocity field of the rigid body
> **Source:** Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 9.3; [Lecture 7, Slide 9]
>
> The point $I$ of the plane of the ice with zero velocity is found from $G$ with Eq. 9.10 (the velocity of $G$ is normal to the rotation axis, so the axis meets the ice at $I$).
>
> $$\begin{aligned}
> \overrightarrow{GI} &= \frac{\boldsymbol\omega_{b0}\times\mathbf v_0^G}{\omega_{b0}^2} = \frac{\dot\psi\,\mathbf k_0\times\left(u\,\mathbf i_b + w\,\mathbf j_b\right)}{\dot\psi^2} = \frac{u\,\mathbf j_b - w\,\mathbf i_b}{\dot\psi} \quad &\text{(Eq. 9.10; cross products of the basis)} \\
> &= \frac{\ell}{2}\,\mathbf i_b - \frac{3\ell}{2}\cot\theta\,\mathbf j_b \quad &\text{(blade conditions)} \\
> \mathbf v_0^G + \dot\psi\,\mathbf k_0\times\overrightarrow{GI} &= u\,\mathbf i_b + w\,\mathbf j_b + \dot\psi\left(\frac{\ell}{2}\,\mathbf j_b + \frac{3\ell}{2}\cot\theta\,\mathbf i_b\right) = \mathbf 0 \quad &\text{(check with Eq. 9.3: both components cancel)} \\
> \frac{d}{dt}\left(\mathbf r_0^G + \overrightarrow{GI}\right) &= \mathbf v_0^G + \dot\psi\,\mathbf k_0\times\overrightarrow{GI} = \mathbf 0 \quad &\text{(the components of $\overrightarrow{GI}$ in $\mathcal B_b$ are constant for a fixed $\theta$; Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_b^I = \overrightarrow{GI} = \frac{\ell}{2}\,\mathbf i_b - \frac{3\ell}{2}\cot\theta\,\mathbf j_b}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** $I$ is where the normals to the blades meet: on the line of $A$ and $B$ (normal to their blades) and on the normal to the blade at $C$. For $\theta$ positive and less than a right angle it lies on the side of minus $\mathbf j_b$, the side towards which the sledge turns when it moves forward. With $\theta$ a right angle it is the midpoint of $AB$; as $\theta$ tends to zero it goes to infinity (pure translation). For a fixed $\theta$ the point $I$ is also fixed on the ice (last row), so $G$ moves on a circle about it.

> [!derivation] Part (c): rates of x and y
> **Law:** components of the velocity of $G$ in $\mathcal B_0$ from those in $\mathcal B_b$
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \mathbf v_0^G &= u\,\mathbf i_b + w\,\mathbf j_b = u\left(\cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0\right) + w\left(-\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0\right) \quad &\text{(body basis in $\mathcal B_0$)} \\
> \dot x &= u\cos\psi - w\sin\psi = -\frac{3\ell}{2}\dot\psi\cot\theta\cos\psi + \frac{\ell}{2}\dot\psi\sin\psi \quad &\text{(component along $\mathbf i_0$; blade conditions)} \\
> \dot y &= u\sin\psi + w\cos\psi = -\frac{3\ell}{2}\dot\psi\cot\theta\sin\psi - \frac{\ell}{2}\dot\psi\cos\psi \quad &\text{(component along $\mathbf j_0$)}
> \end{aligned}$$
>
> $$\boxed{\dot x = \frac{\ell\dot\psi}{2}\left(\sin\psi - 3\cot\theta\cos\psi\right), \qquad \dot y = -\frac{\ell\dot\psi}{2}\left(3\cot\theta\sin\psi + \cos\psi\right)}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$
> **Meaning:** both rates are proportional to the rate of $\psi$: one degree of freedom. The speed of $G$ is the rate of $\psi$ times the distance $GI$, the square root of one plus nine times the square of the cotangent of $\theta$, times $\ell/2$.

### Center of Mass and Inertia Tensor

The statement gives the centre of mass $G$ (at a negligible height above the ice) and the moment of inertia $I$ about the vertical axis through $G$ as data; the shape of the sledge is not given, so there is no integral to set up. For a turning sledge the model also takes $\mathbf k_0$ as a principal axis of inertia at $G$ (no products of inertia between the vertical and the horizontal axes), so the angular momentum about $G$ is vertical; in parts (e) and (f) the sledge does not turn at all and this assumption is not needed.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momentum, angular momentum about G and kinetic energy
> **Law:** linear momentum from $G$; angular momentum about $G$ for a rotation about a principal axis; kinetic energy about $G$
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^G = m\left(u\,\mathbf i_b + w\,\mathbf j_b\right), \qquad \mathbf H_G = I\,\dot\psi\,\mathbf k_0 \quad &\text{(Eq. 11.3; Eq. 11.12 with $\mathbf k_0$ principal)} \\
> T_0 &= \frac12\,m\left(u^2 + w^2\right) + \frac12\,I\dot\psi^2 = \frac12\left[m\,\frac{\ell^2}{4}\left(9\cot^2\theta + 1\right) + I\right]\dot\psi^2 \quad &\text{(Eq. 11.31; blade conditions for $\theta \neq 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = m\,\mathbf v_0^G, \qquad \mathbf H_G = I\dot\psi\,\mathbf k_0, \qquad T_0 = \frac12\left(I + m\,\left|GI\right|^2\right)\dot\psi^2, \quad \left|GI\right|^2 = \frac{\ell^2}{4}\left(1 + 9\cot^2\theta\right)}$$
>
> **Units:** kg m/s; kg m$^2$/s; J
> **Meaning:** for a fixed $\theta$ the sledge turns about the fixed point $I$, and its kinetic energy is that of a rotation about $I$ (Steiner's moment about $I$ times one half of the square of the rate of $\psi$).

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb41-fbd.svg]]

| Force on the sledge | Point of application | Expression | Kind |
| :--- | :--- | :--- | :--- |
| Weight | $G$ | $-mg\,\mathbf k_0$ | applied |
| Normal reactions of the ice | $A$, $B$, $C$ | $N_A\,\mathbf k_0$, $N_B\,\mathbf k_0$, $N_C\,\mathbf k_0$, each $\ge 0$ (the ice only pushes) | constraint |
| Side reactions of the blades at $A$ and $B$ | $A$, $B$ | $Y\,\mathbf j_b$ at each, equal in magnitude (statement); read here with the same sense at $A$ and $B$ | constraint |
| Side reaction of the blade at $C$ | $C$ | $Y_C\,\mathbf n_C = Y_C(-\sin\theta\,\mathbf i_b + \cos\theta\,\mathbf j_b)$ | constraint |
| Lift | $P$ | $\mathbf L = b_L\,u_b^w\,(\mathbf u_b^w\times\mathbf k_0)$, horizontal, normal to the relative wind | applied |
| Drag | $P$ | $\mathbf D = b_D\,u_b^w\,\mathbf u_b^w$, along the relative wind | applied |

No blade exerts a force along its own direction (no friction along the blades).

> [!derivation] Part (d): aerodynamic forces at P
> **Law:** relative velocity of the wind with respect to the sledge; velocity field of the rigid body; magnitudes of the statement
> **Source:** Notes.pdf, Eq. 9.3; Problems.pdf, p. 70
>
> The relative wind at the sail is the wind velocity minus the velocity of the body point $P$. The lift is normal to it in the horizontal plane; of the two normal directions, the one along the relative wind crossed with $\mathbf k_0$ is taken, which is the side for which the statement asks $\mathbf L\cdot\mathbf i_b \ge 0$ in part (e) (the other side is the sail set on the other tack).
>
> $$\begin{aligned}
> \mathbf v_0^P &= \mathbf v_0^G + \dot\psi\,\mathbf k_0\times\ell\,\mathbf k_0 = \mathbf v_0^G \quad &\text{(Eq. 9.3; $\mathbf k_0\times\mathbf k_0 = \mathbf 0$)} \\
> \mathbf u_b^w &= U_\infty\,\mathbf j_0 - \mathbf v_0^G = \left(U_\infty\sin\psi - u\right)\mathbf i_b + \left(U_\infty\cos\psi - w\right)\mathbf j_b \quad &\text{(relative velocity; $\mathbf j_0$ in $\mathcal B_b$)} \\
> \left|\mathbf u_b^w\times\mathbf k_0\right| &= u_b^w, \qquad \mathbf L = b_L\,u_b^w\left(\mathbf u_b^w\times\mathbf k_0\right), \qquad \mathbf D = b_D\,u_b^w\,\mathbf u_b^w \quad &\text{(normal to both; magnitudes $b_L (u_b^w)^2$ and $b_D (u_b^w)^2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf L + \mathbf D = u_b^w\left[b_L\left(\mathbf u_b^w\times\mathbf k_0\right) + b_D\,\mathbf u_b^w\right] \ \text{ at } P, \qquad \mathbf u_b^w = U_\infty\,\mathbf j_0 - \mathbf v_0^G}$$
>
> **Units:** kg/m times m$^2$/s$^2$: N
> **Meaning:** the forces depend on the motion of the sledge through the relative wind; at rest the relative wind is the wind itself.

> [!derivation] Part (d): resultant force and moment about G
> **Law:** sum of forces; moments about $G$ by determinants expanded along the first row
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 2.6
>
> Write $F_{a1}$ and $F_{a2}$ for the components of $\mathbf L + \mathbf D$ along $\mathbf i_b$ and $\mathbf j_b$. Arms from the blade box; the weight acts at $G$.
>
> $$\begin{aligned}
> \mathbf F &= \left(F_{a1} - Y_C\sin\theta\right)\mathbf i_b + \left(F_{a2} + 2Y + Y_C\cos\theta\right)\mathbf j_b + \left(N_A + N_B + N_C - mg\right)\mathbf k_0 \quad &\text{(sum by components)} \\
> \overrightarrow{GA}\times\left(Y\,\mathbf j_b + N_A\,\mathbf k_0\right) &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_0 \cr \ell/2 & \sqrt3\,\ell/2 & 0 \cr 0 & Y & N_A \end{vmatrix} = \frac{\sqrt3\,\ell}{2}N_A\,\mathbf i_b - \frac{\ell}{2}N_A\,\mathbf j_b + \frac{\ell}{2}Y\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \overrightarrow{GB}\times\left(Y\,\mathbf j_b + N_B\,\mathbf k_0\right) &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_0 \cr \ell/2 & -\sqrt3\,\ell/2 & 0 \cr 0 & Y & N_B \end{vmatrix} = -\frac{\sqrt3\,\ell}{2}N_B\,\mathbf i_b - \frac{\ell}{2}N_B\,\mathbf j_b + \frac{\ell}{2}Y\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \overrightarrow{GC}\times\left(Y_C\,\mathbf n_C + N_C\,\mathbf k_0\right) &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_0 \cr -\ell & 0 & 0 \cr -Y_C\sin\theta & Y_C\cos\theta & N_C \end{vmatrix} = \ell N_C\,\mathbf j_b - \ell Y_C\cos\theta\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \overrightarrow{GP}\times\left(\mathbf L + \mathbf D\right) &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_0 \cr 0 & 0 & \ell \cr F_{a1} & F_{a2} & 0 \end{vmatrix} = -\ell F_{a2}\,\mathbf i_b + \ell F_{a1}\,\mathbf j_b \quad &\text{(expand along the first row)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_G = \left[\frac{\sqrt3\,\ell}{2}\left(N_A - N_B\right) - \ell F_{a2}\right]\mathbf i_b + \left[\ell N_C + \ell F_{a1} - \frac{\ell}{2}\left(N_A + N_B\right)\right]\mathbf j_b + \ell\left(Y - Y_C\cos\theta\right)\mathbf k_0}$$
>
> **Units:** N; N m
> **Meaning:** the sail force, applied at the height $\ell$, tilts the sledge about horizontal axes; the blades answer with unequal normal reactions. The equal side reactions at $A$ and $B$ (statement) leave five reaction unknowns.

> [!derivation] Equations of motion
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 4]; [Lecture 10, Slide 5]
>
> The pole $G$ is the centre of mass, so Eq. 12.13 has no term in the velocity of the pole, even though $G$ accelerates. While the blades stay on the ice the sledge does not tilt, and with $\mathbf k_0$ principal the derivative of the angular momentum about $G$ is $I$ times the second rate of $\psi$ along $\mathbf k_0$.
>
> $$\begin{aligned}
> m\left(\dot u - w\dot\psi\right) &= F_{a1} - Y_C\sin\theta \quad &\text{(force along $\mathbf i_b$)} \\
> m\left(\dot w + u\dot\psi\right) &= F_{a2} + 2Y + Y_C\cos\theta \quad &\text{(force along $\mathbf j_b$)} \\
> 0 &= N_A + N_B + N_C - mg \quad &\text{(force along $\mathbf k_0$: no vertical motion)} \\
> 0 &= \frac{\sqrt3\,\ell}{2}\left(N_A - N_B\right) - \ell F_{a2} \quad &\text{(moment along $\mathbf i_b$: no roll)} \\
> 0 &= \ell N_C + \ell F_{a1} - \frac{\ell}{2}\left(N_A + N_B\right) \quad &\text{(moment along $\mathbf j_b$: no pitch)} \\
> I\ddot\psi &= \ell\left(Y - Y_C\cos\theta\right) \quad &\text{(moment along $\mathbf k_0$)}
> \end{aligned}$$
>
> $$\boxed{\text{six equations for } \psi(t),\ Y,\ Y_C,\ N_A,\ N_B,\ N_C, \quad \text{with } u, w \text{ from the blade conditions, for } \theta \neq 0}$$
>
> **Units:** N in the force equations; N m in the moment equations
> **Meaning:** six unknowns, the coordinate $\psi$ (which gives $u$ and $w$) and five reactions, for six equations. The motion is valid while the three normal reactions stay non-negative; when one reaches zero the sledge starts to tip.

#### Sledge at psi and theta zero

> [!derivation] Part (e): largest wind speed without tipping, from rest
> **Law:** equations of motion with $\psi$ and $\theta$ zero; unilateral contact (normal reactions non-negative)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.1
>
> With $\theta$ zero the blade conditions give a zero rate of $\psi$ and a zero $w$ (blade box), at every instant, so $\psi$ stays zero and $\mathcal B_b$ is $\mathcal B_0$. At rest the relative wind is the wind, $U_\infty\,\mathbf j_b$; with $b_D$ zero only the lift acts.
>
> $$\begin{aligned}
> \mathbf L &= b_L\,U_\infty\left(U_\infty\,\mathbf j_b\times\mathbf k_0\right) = b_L U_\infty^2\,\mathbf i_b, \qquad F_{a1} = L = b_L U_\infty^2, \quad F_{a2} = 0 \quad &\text{(part (d); $\mathbf j_b\times\mathbf k_0 = \mathbf i_b$: forward, as the statement asks)} \\
> m\dot u &= L, \qquad 0 = 2Y + Y_C, \qquad 0 = \ell\left(Y - Y_C\right) \;\Rightarrow\; Y = Y_C = 0 \quad &\text{(forces in the plane; moment along $\mathbf k_0$)} \\
> N_A &= N_B, \qquad \frac{\ell}{2}\left(N_A + N_B\right) = \ell N_C + \ell L \quad &\text{(moments along $\mathbf i_b$ and $\mathbf j_b$)} \\
> N_A + N_B &= 2N_C + 2L, \qquad 2N_C + 2L + N_C = mg \quad &\text{(multiply by $2/\ell$; vertical force)} \\
> N_C &= \frac{mg - 2L}{3}, \qquad N_A = N_B = \frac{mg + L}{3} \quad &\text{(solve)} \\
> N_C \ge 0 &\;\Leftrightarrow\; b_L U_\infty^2 \le \frac{mg}{2} \quad &\text{(the rear blade must stay on the ice)}
> \end{aligned}$$
>
> $$\boxed{U_{\infty,\max} = \sqrt{\frac{mg}{2\,b_L}}}$$
>
> **Units:** $\sqrt{\mathrm N/(\mathrm{kg/m})} = \sqrt{\mathrm{m^2/s^2}}$, m/s
> **Meaning:** the lift pushes the sledge forward, at the height $\ell$ of the sail, and nothing resists it along the blades: the sledge accelerates at $L/m$. Its moment about $G$ pitches the sledge forward, unloading the rear blade $C$ and loading $A$ and $B$; the sledge tips about the line $AB$ when the lift reaches half the weight.

![[attachments/EM-SOL/rb41-wind.svg]]

> [!derivation] Part (f): largest steady speed
> **Law:** force equation along $\mathbf i_b$ with the relative wind of a moving sledge; steady motion
> **Source:** Notes.pdf, Eq. 12.8; Problems.pdf, p. 70
>
> With $\psi$ and $\theta$ zero the sledge moves along $\mathbf i_0$ with the speed $v$ (zero $w$ and rate of $\psi$). The blades take every force along $\mathbf j_0$; only the forward component matters.
>
> $$\begin{aligned}
> \mathbf u_b^w &= U_\infty\,\mathbf j_0 - v\,\mathbf i_0, \qquad u_b^w = \sqrt{U_\infty^2 + v^2} \quad &\text{(relative wind; Pythagoras)} \\
> \mathbf u_b^w\times\mathbf k_0 &= U_\infty\left(\mathbf j_0\times\mathbf k_0\right) - v\left(\mathbf i_0\times\mathbf k_0\right) = U_\infty\,\mathbf i_0 + v\,\mathbf j_0 \quad &\text{($\mathbf j_0\times\mathbf k_0 = \mathbf i_0$, $\mathbf i_0\times\mathbf k_0 = -\mathbf j_0$)} \\
> F_{a1} &= \sqrt{U_\infty^2 + v^2}\left(b_L U_\infty - b_D v\right) \quad &\text{(component of $\mathbf L + \mathbf D$ along $\mathbf i_0$)} \\
> m\dot v &= \sqrt{U_\infty^2 + v^2}\left(b_L U_\infty - b_D v\right) \quad &\text{(force along $\mathbf i_b$; no blade force along it)} \\
> \dot v &= 0 \;\Leftrightarrow\; b_L U_\infty - b_D v = 0 \quad &\text{(steady motion; the square root is positive)}
> \end{aligned}$$
>
> $$\boxed{v_{\max} = \frac{b_L}{b_D}\,U_\infty}$$
>
> **Units:** dimensionless ratio times m/s
> **Meaning:** below this speed the forward force is positive and the sledge speeds up; above it, negative: it is the largest speed at which the sledge can travel steadily. It exceeds the wind speed when $b_L$ is larger than $b_D$, as with real ice yachts: the lift, normal to the relative wind, keeps a forward component however fast the sledge goes.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Kinematics | $\mathbf r^G = x\,\mathbf i_0 + y\,\mathbf j_0$, $\mathbf v^G = \dot x\,\mathbf i_0 + \dot y\,\mathbf j_0$, $\mathbf a^G = \ddot x\,\mathbf i_0 + \ddot y\,\mathbf j_0$, $\boldsymbol\omega = \dot\psi\,\mathbf k_0$, $\boldsymbol\alpha = \ddot\psi\,\mathbf k_0$ |
| (b) Instantaneous centre | $\mathbf r_b^I = \overrightarrow{GI} = \tfrac{\ell}{2}\,\mathbf i_b - \tfrac{3\ell}{2}\cot\theta\,\mathbf j_b$ |
| (c) Rates of $x$, $y$ | $\dot x = \tfrac{\ell\dot\psi}{2}(\sin\psi - 3\cot\theta\cos\psi)$, $\dot y = -\tfrac{\ell\dot\psi}{2}(3\cot\theta\sin\psi + \cos\psi)$ |
| (d) Forces | $-mg\,\mathbf k_0$ at $G$; $N_A\mathbf k_0 + Y\mathbf j_b$ at $A$; $N_B\mathbf k_0 + Y\mathbf j_b$ at $B$; $N_C\mathbf k_0 + Y_C\mathbf n_C$ at $C$; $\mathbf L = b_L u_b^w(\mathbf u_b^w\times\mathbf k_0)$ and $\mathbf D = b_D u_b^w\,\mathbf u_b^w$ at $P$, $\mathbf u_b^w = U_\infty\mathbf j_0 - \mathbf v_0^G$ |
| (e) No tipping from rest | $U_\infty \le \sqrt{mg/(2b_L)}$ (then $N_C = (mg - 2L)/3 \ge 0$) |
| (f) Largest steady speed | $v_{\max} = b_L U_\infty/b_D$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with a second route and limiting cases.

> [!derivation] Check: the tipping limit from moments about the line AB
> **Law:** moment equation about a point of the line $AB$ with the inertia term of an accelerating pole
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 2.6
>
> Take the pole at $M$, the midpoint of $AB$, at $\ell/2$ ahead of $G$; at the limit $N_C$ is zero. The sledge does not rotate, so the angular momentum about $M$ is $\overrightarrow{MG}$ crossed with the momentum, whose derivative is $\overrightarrow{MG}$ crossed with $m$ times the acceleration of $G$; $G$ is on the ice, so that acceleration, along $\mathbf i_b$, is parallel to $\overrightarrow{MG}$ and the product vanishes.
>
> $$\begin{aligned}
> \overrightarrow{MG}\times\left(-mg\,\mathbf k_0\right) &= -\frac{\ell}{2}\,\mathbf i_b\times\left(-mg\,\mathbf k_0\right) = -\frac{\ell}{2}\,mg\,\mathbf j_b \quad &\text{(weight at $G$; $\mathbf i_b\times\mathbf k_0 = -\mathbf j_b$)} \\
> \overrightarrow{MP}\times L\,\mathbf i_b &= \left(-\frac{\ell}{2}\,\mathbf i_b + \ell\,\mathbf k_0\right)\times L\,\mathbf i_b = \ell L\,\mathbf j_b \quad &\text{(lift at $P$; $\mathbf k_0\times\mathbf i_b = \mathbf j_b$)} \\
> \ell L - \frac{\ell}{2}\,mg &= 0 \;\Rightarrow\; L = \frac{mg}{2} \quad &\text{(the reactions at $A$ and $B$ have no moment about $\mathbf j_b$: their lines cut the line $AB$, and the moments about $\mathbf i_b$ cancel because $N_A = N_B$)}
> \end{aligned}$$
>
> $$\boxed{b_L U_{\infty,\max}^2 = \frac{mg}{2}}$$
>
> **Units:** N m before the division by $\ell$
> **Meaning:** the same limit as part (e): the lever arm of the lift about the tipping line is $\ell$, that of the weight $\ell/2$.

**Limiting cases and consistency:**

* **Blade at C across the axis.** With $\theta$ a right angle the cotangent vanishes: the forward speed is zero and $G$ moves sideways with the rate of $\psi$ times $\ell/2$, the sledge pivoting about the midpoint of $AB$, which is the centre of part (b).
* **Straight blades.** As $\theta$ tends to zero, $I$ recedes to infinity and the rate of $\psi$ needed for a given forward speed tends to zero: the straight sliding of parts (e) and (f).
* **No drag.** With $b_D$ zero the forward force of part (f) is positive at every speed: no finite steady speed exists, in agreement with the ratio of part (f).
* **No lift.** With $b_L$ zero the steady speed is zero: a sledge pushed only by drag cannot sail across the wind, since the drag then has no component along $\mathbf i_0$ at rest and opposes any motion along it.
* **Dimensions.** $b_L$ times a squared speed is a force; $mg$ over $b_L$ is a squared speed; $b_L/b_D$ is dimensionless.

---

## Problem RB-17: Constrained pizza cutter (Fork and disc)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** two rigid bodies. The fork $F$, of mass $M$ and centre of mass $G$, turns about the fixed horizontal axis $AB$ through $O_1$ (an ideal pin: the fork can only turn about $AB$). The disc $D$, homogeneous, of mass $m$, radius $R$, negligible thickness and centre $O$, turns about the axis $CD$ of the fork through $O$ (an ideal bearing). $CD$ is perpendicular to $AB$ and to the arm of the fork, at the distance $b$ from $AB$; $G$ lies on the arm at the distance $a$ from $AB$.
* **Labels of the statement.** The statement calls the fixed frame $S_1$ and the disc frame $S_0$; this solution keeps those labels, so here, unlike in `Notes.pdf`, the index 1 marks the inertial frame and the index 0 the disc.
* **Fixed frame:** $S_1\{O_1; \mathcal B_1\}$ with $\mathbf i_1$ horizontal (to the right in the figure), $\mathbf j_1$ along $AB$ towards $A$ and $\mathbf k_1$ vertical, pointing down: gravity is $g\,\mathbf k_1$. The basis is right-handed; in the view of the figure, with $\mathbf i_1$ to the right and $\mathbf k_1$ down, $\mathbf j_1$ points out of the paper (⊙), which is the perspective in which $A$ is drawn in front.
* **Fork frame:** $S_2\{O_1; \mathcal B_2\}$, attached to the fork: $\mathbf j_2$ along $AB$ (equal to $\mathbf j_1$), $\mathbf k_2$ along the arm from $O_1$ towards $O$, and $\mathbf i_2$ parallel to $CD$ (the axis $x_2 \equiv x_0$ of the figure).
* **Disc frame:** $S_0\{O; \mathcal B_0\}$, attached to the disc: $\mathbf i_0$ equal to $\mathbf i_2$ (along $CD$, normal to the disc) and $\mathbf j_0$, $\mathbf k_0$ in the plane of the disc.
* **Angles:** $\theta$, from $\mathbf k_1$ to $\mathbf k_2$ about $\mathbf j_1$ (read from the figure: the arm swings from the downward vertical towards $\mathbf i_1$); $\varphi$, from $\mathbf j_2$ to $\mathbf j_0$ about $\mathbf i_2$. The figure marks only the size of $\varphi$; its sense is read as positive about $\mathbf i_2$. The opposite reading would change the sign of the rate of $\varphi$ in every formula below (the axial angular momentum and the gyroscopic torques), not the method.
* **Degrees of freedom:** two free bodies have twelve; the pin $AB$ removes five (the three components of the velocity of $O_1$ and the two rotations normal to $AB$) and the bearing $CD$ removes five more (the three components of the relative velocity at $O$ and the two relative rotations normal to $CD$). **Two degrees of freedom**, $\theta$ and $\varphi$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the fork | $M$ | kg |
| Distance from $G$ to $AB$ (along the arm) | $a$ | m |
| Tensor of inertia of the fork at $O_1$, in $\mathcal B_2$ | $\mathrm{diag}(I_1, I_2, I_3)$ | kg m$^2$ |
| Mass of the disc | $m$ | kg |
| Distance from $AB$ to $CD$ (from $O_1$ to $O$) | $b$ | m |
| Radius of the disc | $R$ | m |
| Gravity | $g$, along $\mathbf k_1$ (down) | m/s$^2$ |
| Pin $AB$ on the fork, at $O_1$ | force $\mathbf R_{O_1}$, torque $\mathbf Q_{O_1}$ with no $\mathbf j_2$ component | N, N m |
| Bearing $CD$ on the disc, at $O$ | force $\mathbf R_O$, torque $\mathbf Q_O$ with no $\mathbf i_2$ component | N, N m |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb17-rot-theta.svg]]

> [!derivation] Fork basis: rotation by theta about j1
> **Law:** simple rotation about the second axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the vertical plane of the arm with $\mathbf j_1$ out of the paper (⊙), $\mathbf i_1$ to the right and $\mathbf k_1$ down: a positive $\theta$ turns counterclockwise, from the downward $\mathbf k_1$ towards $\mathbf i_1$. $\mathbf k_2$ is $\mathbf k_1$ turned by $\theta$: hypotenuse 1, adjacent leg along $\mathbf k_1$ (cosine of $\theta$), opposite leg along $\mathbf i_1$ (sine). $\mathbf i_2$ is $\mathbf i_1$ turned by $\theta$: adjacent leg along $\mathbf i_1$ (cosine); the counterclockwise turn carries the tip of $\mathbf i_1$ upwards, and up is minus $\mathbf k_1$, which is the minus sign of the opposite leg (sine).
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1, \qquad \mathbf j_2 = \mathbf j_1, \qquad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 & -\cos\theta\sin\theta + \sin\theta\cos\theta \cr 0 & 1 & 0 \cr -\sin\theta\cos\theta + \cos\theta\sin\theta & 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf k_1 &= -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2 \quad &\text{(third row: the inverse is the transpose)} \\
> \boldsymbol\omega_{21} &= \dot\theta\,\mathbf j_2 \quad &\text{(rate of the angle along its axis)} \\
> \dot{\mathbf i}_2 &= \dot\theta\,\mathbf j_2\times\mathbf i_2 = -\dot\theta\,\mathbf k_2, \qquad \dot{\mathbf j}_2 = \mathbf 0, \qquad \dot{\mathbf k}_2 = \dot\theta\,\mathbf j_2\times\mathbf k_2 = \dot\theta\,\mathbf i_2 \quad &\text{(Poisson in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_2 = \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1, \quad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1, \quad \mathbf k_1 = -\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2, \quad \boldsymbol\omega_{21} = \dot\theta\,\mathbf j_2}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** with $\theta$ zero the arm hangs vertically and $\mathcal B_2$ coincides with $\mathcal B_1$; the weight, along $\mathbf k_1$, has a component along minus $\mathbf i_2$ that pulls the arm back towards the vertical.

![[attachments/EM-SOL/rb17-rot-phi.svg]]

> [!derivation] Disc basis: rotation by phi about i2, and the angular velocity of the disc
> **Law:** simple rotation about the first axis; right-hand rule; additivity of angular velocities
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 3.14; [Lecture 7, Slide 12]
>
> View of the plane of the disc with $\mathbf i_2$ out of the paper (⊙), $\mathbf j_2$ to the right and $\mathbf k_2$ up (right-handed, since the cross product of $\mathbf j_2$ and $\mathbf k_2$ is $\mathbf i_2$): a positive $\varphi$ turns counterclockwise. $\mathbf j_0$: adjacent leg along $\mathbf j_2$ (cosine of $\varphi$), opposite leg along $\mathbf k_2$ (sine). $\mathbf k_0$: adjacent leg along $\mathbf k_2$ (cosine); the counterclockwise turn carries the tip of $\mathbf k_2$ to the left, towards minus $\mathbf j_2$, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf j_0 &= \cos\varphi\,\mathbf j_2 + \sin\varphi\,\mathbf k_2, \qquad \mathbf k_0 = -\sin\varphi\,\mathbf j_2 + \cos\varphi\,\mathbf k_2 \quad &\text{(legs of the two triangles)} \\
> [{}_2R_0] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\varphi & -\sin\varphi \cr 0 & \sin\varphi & \cos\varphi \end{bmatrix} \quad &\text{(columns: $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$ in $\mathcal B_2$)} \\
> \det[{}_2R_0] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_2R_0][{}_2R_0]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi \cr 0 & \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{02} &= \dot\varphi\,\mathbf i_2 \quad &\text{(rate of the angle along its axis)} \\
> \boldsymbol\omega_{01} &= \boldsymbol\omega_{02} + \boldsymbol\omega_{21} = \dot\varphi\,\mathbf i_2 + \dot\theta\,\mathbf j_2 \quad &\text{(Eq. 3.14 with the intermediate frame $S_2$)} \\
> \boldsymbol\alpha_{01} &= \ddot\varphi\,\mathbf i_2 + \dot\varphi\,\dot{\mathbf i}_2 + \ddot\theta\,\mathbf j_2 = \ddot\varphi\,\mathbf i_2 + \ddot\theta\,\mathbf j_2 - \dot\varphi\dot\theta\,\mathbf k_2 \quad &\text{(product rule; Poisson from the previous box)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{01} = \dot\varphi\,\mathbf i_2 + \dot\theta\,\mathbf j_2, \qquad \boldsymbol\alpha_{01} = \ddot\varphi\,\mathbf i_2 + \ddot\theta\,\mathbf j_2 - \dot\varphi\dot\theta\,\mathbf k_2}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the disc always contains the line $AB$ (its plane is spanned by $\mathbf j_2$ and $\mathbf k_2$); the term in the product of the two rates is the turning of the spin axis $\mathbf i_2$ as the fork swings.

> [!derivation] Positions, velocities and accelerations of G and O
> **Law:** position along the arm; derivative of a vector written in a moving basis; product rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 2.6; [Lecture 7, Slide 6]
>
> Both points lie on the arm, at the distances $a$ and $b$ from $O_1$ along $\mathbf k_2$; $O_1$ is fixed.
>
> $$\begin{aligned}
> \mathbf r_1^G &= a\,\mathbf k_2, \qquad \mathbf r_1^O = b\,\mathbf k_2 \quad &\text{(along the arm)} \\
> \mathbf v_1^O &= b\,\dot{\mathbf k}_2 = b\dot\theta\,\mathbf i_2 \quad &\text{($b$ constant; Poisson)} \\
> \mathbf a_1^O &= b\ddot\theta\,\mathbf i_2 + b\dot\theta\,\dot{\mathbf i}_2 = b\ddot\theta\,\mathbf i_2 - b\dot\theta^2\,\mathbf k_2 \quad &\text{(product rule; Poisson)} \\
> \mathbf v_1^G &= a\dot\theta\,\mathbf i_2, \qquad \mathbf a_1^G = a\ddot\theta\,\mathbf i_2 - a\dot\theta^2\,\mathbf k_2 \quad &\text{(same steps with $a$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_1^O = b\dot\theta\,\mathbf i_2, \quad \mathbf a_1^O = b\ddot\theta\,\mathbf i_2 - b\dot\theta^2\,\mathbf k_2, \quad \mathbf v_1^G = a\dot\theta\,\mathbf i_2, \quad \mathbf a_1^G = a\ddot\theta\,\mathbf i_2 - a\dot\theta^2\,\mathbf k_2}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$ in every term
> **Meaning:** both points describe circles about $AB$; the $\mathbf k_2$ term is the centripetal part, pointing from the point back to $O_1$, and the $\mathbf i_2$ term the tangential part.

### Center of Mass and Inertia Tensor

> [!derivation] Tensor of inertia of the disc at O
> **Law:** moments and products of inertia as area integrals in polar coordinates (jacobian $\rho$); symmetry of revolution
> **Source:** Notes.pdf, Eq. 10.9; Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.35; [Lecture 8, Slide 10]
>
> The disc is homogeneous and thin, of surface density $\sigma$ equal to $m/(\pi R^2)$, so its centre of mass is the centre $O$. A point of the disc is at $\rho\cos\chi\,\mathbf j_0 + \rho\sin\chi\,\mathbf k_0$ from $O$, with $\rho$ from 0 to $R$ and $\chi$ from 0 to $2\pi$; its coordinate along $\mathbf i_0$ is zero (negligible thickness). The element of mass is $\sigma\rho\,d\rho\,d\chi$.
>
> $$\begin{aligned}
> I_{xx} &= \sigma\int_0^{2\pi}\!\!\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R = \sigma\cdot 2\pi\cdot\frac{R^4}{4} = \frac{mR^2}{2} \quad &\text{(distance to the axis $\mathbf i_0$ is $\rho$; antiderivatives; Barrow's rule)} \\
> I_{yy} &= \sigma\int_0^{2\pi}\!\!\int_0^R\rho^2\sin^2\chi\,\rho\,d\rho\,d\chi = \sigma\left[\frac{\chi}{2} - \frac{\sin 2\chi}{4}\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R \quad &\text{(squared distance to the axis $\mathbf j_0$ is the square of $\rho\sin\chi$)} \\
> &= \sigma\left(\pi - 0\right)\frac{R^4}{4} = \frac{m}{\pi R^2}\cdot\frac{\pi R^4}{4} = \frac{mR^2}{4} \quad &\text{(Barrow's rule; value of $\sigma$)} \\
> I_{zz} &= \frac{mR^2}{4} \quad &\text{(same integral with the cosine: the two diameters are equivalent)} \\
> P_{yz} &= \sigma\int_0^{2\pi}\!\!\sin\chi\cos\chi\,d\chi\int_0^R\rho^3\,d\rho = \sigma\left[\frac{\sin^2\chi}{2}\right]_0^{2\pi}\frac{R^4}{4} = 0, \qquad P_{xy} = P_{xz} = 0 \quad &\text{(antiderivative and Barrow's rule; zero coordinate along $\mathbf i_0$)} \\
> [{}_2R_0]\,\mathrm{diag}\!\left(A, B, B\right)[{}_2R_0]^T &= \mathrm{diag}\!\left(A, B, B\right) \quad &\text{(the lower block is $B$ times $R R^T$, the identity: same components in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}{}^D_O = \begin{bmatrix} A & 0 & 0 \cr 0 & B & 0 \cr 0 & 0 & B \end{bmatrix}_{2}, \qquad A = \frac{mR^2}{2}, \quad B = \frac{mR^2}{4}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the disc is symmetric about its axis $CD$, so its tensor has the same constant components in the fork basis $\mathcal B_2$, although the disc turns relative to it: this is why $\mathcal B_2$ is the basis used for the disc below.

The fork tensor is a datum of the statement: diagonal in $\mathcal B_2$ at $O_1$, with $I_2$ the moment about $AB$; the centre of mass $G$ is on the arm at the distance $a$ from $O_1$. Both tensors have constant components in $\mathcal B_2$.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (a): kinetic energy of the fork and disc relative to S1
> **Law:** kinetic energy about a fixed body point (fork); Koenig's theorem about the centre of mass (disc)
> **Source:** Notes.pdf, Eq. 11.32; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 9]
>
> $O_1$ is a fixed point of the fork, so its kinetic energy is the rotational term about $O_1$ alone; the disc has no fixed point and is expanded about its centre of mass $O$.
>
> $$\begin{aligned}
> T^F &= \frac12\,\boldsymbol\omega_{21}\cdot\bar{\bar I}{}^F_{O_1}\cdot\boldsymbol\omega_{21} = \frac12\begin{bmatrix} 0 & \dot\theta & 0 \end{bmatrix}\begin{bmatrix} I_1 & 0 & 0 \cr 0 & I_2 & 0 \cr 0 & 0 & I_3 \end{bmatrix}\begin{bmatrix} 0 \cr \dot\theta \cr 0 \end{bmatrix} = \frac12\,I_2\dot\theta^2 \quad &\text{(Eq. 11.32; components in $\mathcal B_2$)} \\
> T^D &= \frac12\,m\left(v_1^O\right)^2 + \frac12\,\boldsymbol\omega_{01}\cdot\bar{\bar I}{}^D_O\cdot\boldsymbol\omega_{01} \quad &\text{(Eq. 11.31, Koenig)} \\
> &= \frac12\,m\,b^2\dot\theta^2 + \frac12\left(A\dot\varphi^2 + B\dot\theta^2\right) \quad &\text{(velocity of $O$; diagonal tensor in $\mathcal B_2$)} \\
> T_1 &= T^F + T^D = \frac12\,I_2\dot\theta^2 + \frac12\,m b^2\dot\theta^2 + \frac{mR^2}{8}\dot\theta^2 + \frac{mR^2}{4}\dot\varphi^2 \quad &\text{(sum; values of $A$ and $B$)}
> \end{aligned}$$
>
> $$\boxed{T_1 = \left(\frac{I_2}{2} + \frac{mR^2}{8} + \frac{mb^2}{2}\right)\dot\theta^2 + \frac{mR^2}{4}\,\dot\varphi^2}$$
>
> **Units:** $[\mathrm{M\,L^2}][\mathrm{T^{-2}}]$, J in every term
> **Meaning:** the swing about $AB$ carries the fork, the disc as a point mass at $O$ and the disc turning about its own diameter; the spin about $CD$ adds a separate term, with no cross term between the two rates because $\mathcal B_2$ is principal for the disc.

> [!derivation] Part (b): angular momentum of the disc about O relative to S1
> **Law:** angular momentum about the centre of mass
> **Source:** Notes.pdf, Eq. 11.12; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf H_O^D &= \bar{\bar I}{}^D_O\cdot\boldsymbol\omega_{01} \quad &\text{(Eq. 11.12; $O$ is the centre of mass of the disc)} \\
> &= \begin{bmatrix} A & 0 & 0 \cr 0 & B & 0 \cr 0 & 0 & B \end{bmatrix}\begin{bmatrix} \dot\varphi \cr \dot\theta \cr 0 \end{bmatrix} = A\dot\varphi\,\mathbf i_2 + B\dot\theta\,\mathbf j_2 \quad &\text{(matrix product in $\mathcal B_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_O^D = \frac{mR^2}{2}\,\dot\varphi\,\mathbf i_2 + \frac{mR^2}{4}\,\dot\theta\,\mathbf j_2}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-1}}]$, kg m$^2$/s
> **Meaning:** the spin about $CD$ is weighted by the axial moment, twice the diametral one that weights the swing; the angular momentum is not parallel to the angular velocity unless one of the two rates is zero.

> [!derivation] Part (c): angular momentum of the fork and disc about O1 relative to S1, and the linear momentum
> **Law:** angular momentum about a fixed body point (fork); change of pole from the centre of mass (disc); linear momentum
> **Source:** Notes.pdf, Eq. 11.13; Notes.pdf, Eq. 11.21; Notes.pdf, Eq. 11.3; [Lecture 9, Slide 7]
>
> $$\begin{aligned}
> \mathbf H_{O_1}^F &= \bar{\bar I}{}^F_{O_1}\cdot\boldsymbol\omega_{21} = I_2\dot\theta\,\mathbf j_2 \quad &\text{(Eq. 11.13; $O_1$ fixed body point of the fork)} \\
> \mathbf H_{O_1}^D &= \mathbf H_O^D + m\,\mathbf r_{O_1}^O\times\mathbf v_1^O \quad &\text{(Eq. 11.21, change of pole)} \\
> m\,\mathbf r_{O_1}^O\times\mathbf v_1^O &= m\begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr 0 & 0 & b \cr b\dot\theta & 0 & 0 \end{vmatrix} = m\,b^2\dot\theta\,\mathbf j_2 \quad &\text{(expand along the first row)} \\
> \mathbf H_{O_1} &= A\dot\varphi\,\mathbf i_2 + \left(I_2 + B + m b^2\right)\dot\theta\,\mathbf j_2 \quad &\text{(sum of the two bodies)} \\
> &= A\dot\varphi\left(\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1\right) + \left(I_2 + B + m b^2\right)\dot\theta\,\mathbf j_1 \quad &\text{($\mathbf i_2$ and $\mathbf j_2$ in $\mathcal B_1$, first box)} \\
> \mathbf p_1 &= M\,\mathbf v_1^G + m\,\mathbf v_1^O = \left(Ma + mb\right)\dot\theta\,\mathbf i_2 \quad &\text{(Eq. 11.3 for each body; velocity box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{O_1} = \frac{mR^2}{2}\dot\varphi\cos\theta\,\mathbf i_1 + \left(I_2 + \frac{mR^2}{4} + m b^2\right)\dot\theta\,\mathbf j_1 - \frac{mR^2}{2}\dot\varphi\sin\theta\,\mathbf k_1, \qquad \mathbf p_1 = \left(Ma + mb\right)\dot\theta\,\mathbf i_2}$$
>
> **Units:** kg m$^2$/s; kg m/s
> **Meaning:** the component along $AB$ is the moment of inertia of the whole swinging assembly about $AB$ times the swing rate; the spin part lies along $CD$, which turns in the vertical plane with the fork, so its components in $\mathcal B_1$ change with $\theta$.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb17-exploded.svg]]

The exploded view separates the two bodies at the bearing $CD$. The bearing acts on the disc with the force $\mathbf R_O$ and the torque $\mathbf Q_O$, both reduced at $O$, and on the fork with $-\mathbf R_O$ and $-\mathbf Q_O$ (third law of Newton). An ideal bearing does not oppose the spin about $CD$, so $\mathbf Q_O$ has no component along $\mathbf i_2$; an ideal pin does not oppose the swing about $AB$, so $\mathbf Q_{O_1}$ has no component along $\mathbf j_2$.

| Load | Body | Point | Expression in $\mathcal B_2$ | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the disc | $D$ | $O$ | $mg\,\mathbf k_1 = mg(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2)$ | applied |
| Bearing force | $D$ | $O$ | $\mathbf R_O = R_{O,x}\,\mathbf i_2 + R_{O,y}\,\mathbf j_2 + R_{O,z}\,\mathbf k_2$ | constraint |
| Bearing torque | $D$ | - | $\mathbf Q_O = Q_{O,y}\,\mathbf j_2 + Q_{O,z}\,\mathbf k_2$ | constraint |
| Weight of the fork | $F$ | $G$ | $Mg\,\mathbf k_1 = Mg(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2)$ | applied |
| Reaction of the disc | $F$ | $O$ | $-\mathbf R_O$ and $-\mathbf Q_O$ | constraint (pair) |
| Pin force | $F$ | $O_1$ | $\mathbf R_{O_1} = R_{1,x}\,\mathbf i_2 + R_{1,y}\,\mathbf j_2 + R_{1,z}\,\mathbf k_2$ | constraint |
| Pin torque | $F$ | - | $\mathbf Q_{O_1} = Q_{1,x}\,\mathbf i_2 + Q_{1,z}\,\mathbf k_2$ | constraint |

> [!derivation] Equations of the disc (force, and moment about its centre O)
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass; derivative in the rotating basis
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 13.9; [Lecture 10, Slide 5]
>
> The pole $O$ is the centre of mass of the disc, so the term in the velocity of the pole of Eq. 12.13 is the cross product of the velocity of $O$ with itself, zero. The weight and $\mathbf R_O$ act at $O$ and have no moment about it. The components of the angular momentum in $\mathcal B_2$ are differentiated and the turning of $\mathcal B_2$ is added (Eq. 3.8 with the angular velocity of the fork).
>
> $$\begin{aligned}
> m\left(b\ddot\theta\,\mathbf i_2 - b\dot\theta^2\,\mathbf k_2\right) &= mg\left(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2\right) + \mathbf R_O \quad &\text{(Eq. 12.8; acceleration of $O$)} \\
> \frac{d\mathbf H_O^D}{dt}\bigg|_1 &= \frac{d\mathbf H_O^D}{dt}\bigg|_2 + \boldsymbol\omega_{21}\times\mathbf H_O^D \quad &\text{(Eq. 3.8)} \\
> \frac{d\mathbf H_O^D}{dt}\bigg|_2 &= A\ddot\varphi\,\mathbf i_2 + B\ddot\theta\,\mathbf j_2 \quad &\text{(constant components of the tensor in $\mathcal B_2$)} \\
> \boldsymbol\omega_{21}\times\mathbf H_O^D &= \begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr 0 & \dot\theta & 0 \cr A\dot\varphi & B\dot\theta & 0 \end{vmatrix} = -A\dot\varphi\dot\theta\,\mathbf k_2 \quad &\text{(expand along the first row)} \\
> A\ddot\varphi\,\mathbf i_2 + B\ddot\theta\,\mathbf j_2 - A\dot\varphi\dot\theta\,\mathbf k_2 &= Q_{O,y}\,\mathbf j_2 + Q_{O,z}\,\mathbf k_2 \quad &\text{(Eq. 12.13 about $O$)}
> \end{aligned}$$
>
> $$\boxed{A\ddot\varphi = 0, \quad B\ddot\theta = Q_{O,y}, \quad -A\dot\varphi\dot\theta = Q_{O,z}; \qquad R_{O,x} = m\left(b\ddot\theta + g\sin\theta\right), \quad R_{O,y} = 0, \quad R_{O,z} = -m\left(b\dot\theta^2 + g\cos\theta\right)}$$
>
> **Units:** N m in the moment equations; N in the force components
> **Meaning:** six equations of the disc. The first one is the free spin about the frictionless bearing: the axial component of the angular momentum is conserved although $\mathbf i_2$ turns, for two reasons: the bearing applies no torque along $\mathbf i_2$, and the gyroscopic term is along $\mathbf k_2$, normal to $\mathbf i_2$, because the angular momentum has no $\mathbf k_2$ component.

> [!derivation] Equations of the fork (force, and moment about the fixed point O1)
> **Law:** Newton's second law for the centre of mass; moment equation about a fixed point; third law of Newton for the bearing pair
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.10; Notes.pdf, Sec. 13.1
>
> The pole $O_1$ is fixed, so its velocity is zero and the pole term of Eq. 12.13 vanishes. The angular momentum of the fork is along $\mathbf j_2$, the axis of $\boldsymbol\omega_{21}$, so its gyroscopic term vanishes too. The moment of the pair at $O$ about $O_1$ uses the arm $b\,\mathbf k_2$.
>
> $$\begin{aligned}
> M\left(a\ddot\theta\,\mathbf i_2 - a\dot\theta^2\,\mathbf k_2\right) &= Mg\left(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2\right) + \mathbf R_{O_1} - \mathbf R_O \quad &\text{(Eq. 12.8 for the fork)} \\
> \frac{d\mathbf H_{O_1}^F}{dt}\bigg|_1 &= I_2\ddot\theta\,\mathbf j_2 + \dot\theta\,\mathbf j_2\times I_2\dot\theta\,\mathbf j_2 = I_2\ddot\theta\,\mathbf j_2 \quad &\text{(Eq. 3.8; a vector times itself is zero)} \\
> a\,\mathbf k_2\times Mg\,\mathbf k_1 &= a\,\mathbf k_2\times Mg\left(-\sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf k_2\right) = -Mga\sin\theta\,\mathbf j_2 \quad &\text{(moment of the weight; $\mathbf k_2\times\mathbf i_2 = \mathbf j_2$)} \\
> b\,\mathbf k_2\times\left(-\mathbf R_O\right) &= -b\begin{vmatrix} \mathbf i_2 & \mathbf j_2 & \mathbf k_2 \cr 0 & 0 & 1 \cr R_{O,x} & R_{O,y} & R_{O,z} \end{vmatrix} = b R_{O,y}\,\mathbf i_2 - b R_{O,x}\,\mathbf j_2 \quad &\text{(expand along the first row)} \\
> I_2\ddot\theta\,\mathbf j_2 &= -Mga\sin\theta\,\mathbf j_2 + b R_{O,y}\,\mathbf i_2 - b R_{O,x}\,\mathbf j_2 + \mathbf Q_{O_1} - \mathbf Q_O \quad &\text{(Eq. 12.13 about $O_1$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf i_2:\ 0 = b R_{O,y} + Q_{1,x}, \qquad \mathbf j_2:\ I_2\ddot\theta = -Mga\sin\theta - b R_{O,x} - Q_{O,y}, \qquad \mathbf k_2:\ 0 = Q_{1,z} - Q_{O,z} \\ \mathbf R_{O_1} = \mathbf R_O + M\left(a\ddot\theta + g\sin\theta\right)\mathbf i_2 - M\left(a\dot\theta^2 + g\cos\theta\right)\mathbf k_2 \end{gathered}}$$
>
> **Units:** N m; N
> **Meaning:** six equations of the fork. With the six of the disc they make twelve equations for twelve unknowns: the two coordinates, the three components of $\mathbf R_O$, the two of $\mathbf Q_O$, the three of $\mathbf R_{O_1}$ and the two of $\mathbf Q_{O_1}$.

> [!derivation] Part (d): equations of motion of the system
> **Law:** elimination of the bearing reactions between the equations of the two bodies
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> I_2\ddot\theta &= -Mga\sin\theta - b\,m\left(b\ddot\theta + g\sin\theta\right) - B\ddot\theta \quad &\text{(fork along $\mathbf j_2$ with $R_{O,x}$ and $Q_{O,y}$ of the disc)} \\
> \left(I_2 + m b^2 + B\right)\ddot\theta &= -\left(Ma + mb\right)g\sin\theta \quad &\text{(collect the second rates; collect the weights)} \\
> \ddot\varphi &= 0 \quad &\text{(disc along $\mathbf i_2$, divided by $A$)}
> \end{aligned}$$
>
> $$\boxed{\left(I_2 + \frac{mR^2}{4} + m b^2\right)\ddot\theta + \left(Ma + mb\right)g\sin\theta = 0, \qquad \ddot\varphi = 0}$$
>
> **Units:** N m in the first equation; $[\mathrm{T^{-2}}]$ in the second
> **Meaning:** the swing is a compound pendulum whose moment of inertia about $AB$ includes the disc as a point mass at $O$ plus its diametral moment, and whose restoring moment is the total weight moment; the spin does not enter the swing, and the swing does not change the spin.

> [!derivation] Part (d): reduction to quadratures
> **Law:** integration of a zero second rate; first integral of the swing (multiply by the rate, chain rule); separation of variables; Barrow's rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 12.30
>
> Write $J$ for the sum of $I_2$, $B$ and the product of $m$ and the square of $b$, and $K$ for the sum of the products $Ma$ and $mb$. The initial values are $\theta_0$, $\varphi_0$ and the two initial rates.
>
> $$\begin{aligned}
> \int_0^t\ddot\varphi\,dt' &= 0 \;\Rightarrow\; \left[\dot\varphi\right]_0^t = 0 \;\Rightarrow\; \dot\varphi = \dot\varphi_0 \equiv C_1 \quad &\text{(antiderivative of the second rate; Barrow's rule)} \\
> \int_0^t\dot\varphi\,dt' &= \int_0^t C_1\,dt' \;\Rightarrow\; \left[\varphi\right]_0^t = C_1\left[t'\right]_0^t \;\Rightarrow\; \varphi = \varphi_0 + C_1 t \quad &\text{(antiderivatives; Barrow's rule)} \\
> J\ddot\theta\,\dot\theta &= -K g\sin\theta\,\dot\theta \quad &\text{(multiply the swing equation by the rate of $\theta$)} \\
> \frac{d}{dt}\left(\frac12 J\dot\theta^2\right) &= \frac{d}{dt}\left(K g\cos\theta\right) \quad &\text{(chain rule on both sides)} \\
> \left[\frac12 J\dot\theta^2 - K g\cos\theta\right]_0^t &= 0 \;\Rightarrow\; \frac12 J\dot\theta^2 - K g\cos\theta = \frac12 J\dot\theta_0^2 - K g\cos\theta_0 \equiv E_\theta \quad &\text{(integrate from 0 to $t$; Barrow's rule)} \\
> \frac{d\theta}{dt} &= \pm\sqrt{\frac{2\left(E_\theta + K g\cos\theta\right)}{J}} \quad &\text{(solve for the rate; sign of the initial rate)} \\
> t &= \pm\int_{\theta_0}^{\theta}\frac{d\theta'}{\sqrt{2\left(E_\theta + K g\cos\theta'\right)/J}} \quad &\text{(separate the variables and integrate)}
> \end{aligned}$$
>
> $$\boxed{\dot\varphi = C_1, \qquad \left(\frac{I_2}{2} + \frac{mR^2}{8} + \frac{mb^2}{2}\right)\dot\theta^2 + \frac{mR^2}{4}\dot\varphi^2 - \left(mb + Ma\right)g\cos\theta = C_2, \qquad t = \pm\int_{\theta_0}^{\theta}\frac{\sqrt J\,d\theta'}{\sqrt{2\left(E_\theta + Kg\cos\theta'\right)}}}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; J; s
> **Meaning:** the second boxed integral is the first integral of the swing plus the constant term of the spin, with the constant $C_2$ equal to the sum of $E_\theta$ and the spin term: it is the total mechanical energy, as checked with the power of the reactions in Answers and Checks. The last integral gives the time as a function of $\theta$; its inverse is the motion of the fork, and the spin rate stays constant while the spin angle grows linearly with time.

#### Reactions

> [!derivation] Part (f): force and torque of the axis CD on the disc at O
> **Law:** equations of the disc with the motion of part (d)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> $$\begin{aligned}
> \mathbf R_O &= m\left(b\ddot\theta + g\sin\theta\right)\mathbf i_2 - m\left(b\dot\theta^2 + g\cos\theta\right)\mathbf k_2 \quad &\text{(force components of the disc box)} \\
> \mathbf Q_O &= B\ddot\theta\,\mathbf j_2 - A\dot\varphi\dot\theta\,\mathbf k_2 \quad &\text{(moment components of the disc box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf R_O = \left(mb\ddot\theta + mg\sin\theta\right)\mathbf i_2 - \left(mb\dot\theta^2 + mg\cos\theta\right)\mathbf k_2, \qquad \mathbf Q_O = \frac{mR^2}{4}\ddot\theta\,\mathbf j_2 - \frac{mR^2}{2}\dot\varphi\dot\theta\,\mathbf k_2}$$
>
> **Units:** N; N m
> **Meaning:** the force supports the weight of the disc and supplies its tangential and centripetal accelerations; the torque has two parts: along $AB$ it gives the disc its angular acceleration about its diameter, and along $\mathbf k_2$ it turns the spin angular momentum, which lies along $\mathbf i_2$ and is carried round by the swing (when both rates are positive this torque points along minus $\mathbf k_2$).

> [!derivation] Part (e): force and torque of the axis AB on the fork and disc at O1
> **Law:** equations of the fork with the bearing pair of part (f)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.12
>
> $$\begin{aligned}
> \mathbf R_{O_1} &= \mathbf R_O + M\left(a\ddot\theta + g\sin\theta\right)\mathbf i_2 - M\left(a\dot\theta^2 + g\cos\theta\right)\mathbf k_2 \quad &\text{(force of the fork box)} \\
> &= \left[\left(Ma + mb\right)\ddot\theta + \left(M + m\right)g\sin\theta\right]\mathbf i_2 - \left[\left(Ma + mb\right)\dot\theta^2 + \left(M + m\right)g\cos\theta\right]\mathbf k_2 \quad &\text{($\mathbf R_O$ of part (f); collect)} \\
> Q_{1,x} &= -b R_{O,y} = 0, \qquad Q_{1,z} = Q_{O,z} = -A\dot\varphi\dot\theta \quad &\text{(moment of the fork along $\mathbf i_2$ and $\mathbf k_2$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf R_{O_1} = \left[\left(Ma + mb\right)\ddot\theta + \left(M + m\right)g\sin\theta\right]\mathbf i_2 - \left[\left(Ma + mb\right)\dot\theta^2 + \left(M + m\right)g\cos\theta\right]\mathbf k_2, \qquad \mathbf Q_{O_1} = -\frac{mR^2}{2}\dot\varphi\dot\theta\,\mathbf k_2}$$
>
> **Units:** N; N m
> **Meaning:** the force is the rate of the total linear momentum of the assembly minus the total weight (at rest it holds the weight up); the pin carries the gyroscopic torque of the spinning disc to the ground, and the fork transmits it unchanged because its own angular momentum lies along the pin. With the second rate of $\theta$ from part (d) the force depends only on $\theta$ and its rate.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Kinetic energy relative to $S_1$ | $T_1 = \left(\tfrac{I_2}{2} + \tfrac{mR^2}{8} + \tfrac{mb^2}{2}\right)\dot\theta^2 + \tfrac{mR^2}{4}\dot\varphi^2$ |
| (b) $\mathbf H_O$ of the disc, in $\mathcal B_2$ | $\tfrac{mR^2}{2}\dot\varphi\,\mathbf i_2 + \tfrac{mR^2}{4}\dot\theta\,\mathbf j_2$ |
| (c) $\mathbf H_{O_1}$ of fork and disc, in $\mathcal B_1$ | $\tfrac{mR^2}{2}\dot\varphi\cos\theta\,\mathbf i_1 + \left(I_2 + \tfrac{mR^2}{4} + mb^2\right)\dot\theta\,\mathbf j_1 - \tfrac{mR^2}{2}\dot\varphi\sin\theta\,\mathbf k_1$ |
| (d) Equations of motion and quadratures | $\left(I_2 + \tfrac{mR^2}{4} + mb^2\right)\ddot\theta + (Ma + mb)g\sin\theta = 0$, $\ddot\varphi = 0$; $\dot\varphi = C_1$; $\left(\tfrac{I_2}{2} + \tfrac{mR^2}{8} + \tfrac{mb^2}{2}\right)\dot\theta^2 + \tfrac{mR^2}{4}\dot\varphi^2 - (mb + Ma)g\cos\theta = C_2$; $t = \pm\int_{\theta_0}^{\theta}\sqrt J\,d\theta'/\sqrt{2(E_\theta + Kg\cos\theta')}$ |
| (e) Axis $AB$ on the system, at $O_1$ | $\mathbf R_{O_1} = [(Ma + mb)\ddot\theta + (M + m)g\sin\theta]\,\mathbf i_2 - [(Ma + mb)\dot\theta^2 + (M + m)g\cos\theta]\,\mathbf k_2$; $\mathbf Q_{O_1} = -\tfrac{mR^2}{2}\dot\varphi\dot\theta\,\mathbf k_2$ |
| (f) Axis $CD$ on the disc, at $O$ | $\mathbf R_O = (mb\ddot\theta + mg\sin\theta)\,\mathbf i_2 - (mb\dot\theta^2 + mg\cos\theta)\,\mathbf k_2$; $\mathbf Q_O = \tfrac{mR^2}{4}\ddot\theta\,\mathbf j_2 - \tfrac{mR^2}{2}\dot\varphi\dot\theta\,\mathbf k_2$ |

> [!derivation] Check: the energy integral from the power of the loads
> **Law:** power of a force and a torque reduced at a point; energy theorem; potential of the weight
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34
>
> Second route to the constant $C_2$ of part (d), without the equations of motion: the power of every reaction is shown to be zero and the weights are conservative. The pair at the bearing acts on both bodies at $O$.
>
> $$\begin{aligned}
> \dot W^{\text{pin}} &= \mathbf R_{O_1}\cdot\mathbf v_1^{O_1} + \mathbf Q_{O_1}\cdot\boldsymbol\omega_{21} = \mathbf R_{O_1}\cdot\mathbf 0 + \left(Q_{1,x}\,\mathbf i_2 + Q_{1,z}\,\mathbf k_2\right)\cdot\dot\theta\,\mathbf j_2 = 0 \quad &\text{(Eq. 12.29 on the fork; $O_1$ fixed)} \\
> \dot W^{\text{bearing}} &= \mathbf R_O\cdot\mathbf v_1^O + \mathbf Q_O\cdot\boldsymbol\omega_{01} - \mathbf R_O\cdot\mathbf v_1^O - \mathbf Q_O\cdot\boldsymbol\omega_{21} \quad &\text{(on the disc plus on the fork, both reduced at $O$)} \\
> &= \mathbf Q_O\cdot\left(\boldsymbol\omega_{01} - \boldsymbol\omega_{21}\right) = \left(Q_{O,y}\,\mathbf j_2 + Q_{O,z}\,\mathbf k_2\right)\cdot\dot\varphi\,\mathbf i_2 = 0 \quad &\text{(relative angular velocity along $CD$)} \\
> V_1 &= -Mg\,\mathbf k_1\cdot\mathbf r_1^G - mg\,\mathbf k_1\cdot\mathbf r_1^O = -\left(Ma + mb\right)g\cos\theta \quad &\text{(Eq. 12.34; $\mathbf k_1\cdot\mathbf k_2$ is the cosine of $\theta$)} \\
> \int_0^t\frac{d}{dt'}\left(T_1 + V_1\right)dt' &= \left[T_1 + V_1\right]_0^t = 0 \quad &\text{(energy theorem with conservative weights, Eq. 12.33; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\left(\frac{I_2}{2} + \frac{mR^2}{8} + \frac{mb^2}{2}\right)\dot\theta^2 + \frac{mR^2}{4}\dot\varphi^2 - \left(Ma + mb\right)g\cos\theta = C_2}$$
>
> **Units:** J in every term
> **Meaning:** the same integral as in part (d), obtained without the equations of motion: the pin and the bearing are workless, so $T_1$ of part (a) plus the potential of the two weights is constant.

**Check against the official key:** the key (Problems.pdf, p. 79) prints the quadratures, the spin rate equal to $C_1$ and the energy integral with the coefficients $I_2/2 + mR^2/8 + mb^2/2$, $mR^2/4$ and $mb + Ma$; the force and torque of $AB$ at $O_1$, with the components $(Ma + mb)$ times the second rate plus $(M + m)g$ times the sine of $\theta$ along $\mathbf i_2$, minus $(Ma + mb)$ times the squared rate plus $(M + m)g$ times the cosine along $\mathbf k_2$, and the torque $mR^2/2$ times the product of the rates along minus $\mathbf k_2$; and the force and torque of $CD$ on the disc at $O$ with the same form, $m$ in place of the totals, and the torque $mR^2/4$ times the second rate of $\theta$ along $\mathbf j_2$ minus the same gyroscopic term along $\mathbf k_2$. Every printed item coincides with the boxes of parts (d), (e) and (f), in the same basis $\mathcal B_2$ and with the same angles: **match**. The key calls the pin a collar; the force component along $AB$ comes out zero here, so a collar that could also slide along $AB$, started at rest along it, gives the same results. The key prints no expressions for parts (a) to (c); those of this solution are the terms of its energy integral.

**Limiting cases and consistency:**

* **No disc.** With $m$ zero the swing equation is the compound pendulum of the fork about $AB$, with moment $I_2$ and restoring moment $Mga$ times the sine of $\theta$; the bearing loads vanish.
* **Disc as a particle.** With $R$ tending to zero the disc enters only as a point mass at $O$: the moment about $AB$ becomes $I_2$ plus $m b^2$, and the gyroscopic torques vanish.
* **Equilibrium.** At rest with $\theta$ zero, $\mathbf k_2$ is $\mathbf k_1$ (down) and the pin force is $(M + m)g$ along minus $\mathbf k_1$: it holds the total weight up.
* **Small swings.** For small $\theta$ the swing is harmonic with the squared angular frequency $(Ma + mb)g$ over $J$; the spin does not change it.
* **Dimensions.** Every term of the swing equation is a moment (N m); every term of the energy integral is an energy; the reactions are forces and moments.

---

## Problem RB-20: Pioneer III spacecraft (Yo-yo de-spin)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** three bodies in free space. The probe, an axisymmetric rigid body of mass $m$, radius $R$ and moment of inertia $I$ about its axis of symmetry, with centre $G$; two yo-yo masses of $m/2$ each, modelled as particles $P$ and $P'$; two massless, inextensible cords, wound on the rim of the probe, attached to it at $H$ and $H'$. No external force acts (gravity negligible).
* **Plane of the motion:** the spin axis of the probe is normal to the plane of the figure and the masses move in that plane, so the motion is planar.
* **Inertial frame:** $S_0\{G; \mathcal B_0\}$, with $\mathbf i_0$, $\mathbf j_0$ in the plane of the figure and $\mathbf k_0$ out of the paper (⊙) along the spin axis. Its origin is the position of $G$, which is shown below to stay at rest.
* **Probe frame:** $S_1\{G; \mathcal B_1\}$, attached to the probe, with $\mathbf i_1$ along $GA$, the radius through the point $A$ of the rim where the mass sat before the release (the axes $x$, $y$ of the figure), and $\mathbf j_1$ normal to it. The angle $\theta$ goes from $\mathbf i_0$ to $\mathbf i_1$ about $\mathbf k_0$; the spin of the statement is the rate of $\theta$, with the initial value $\omega_0$.
* **Cord basis:** $\mathcal B_2\{\mathbf e_r, \mathbf e_t, \mathbf k_0\}$, with $\mathbf e_r$ along $GT$ (the radius to the point of tangency $T$) and $\mathbf e_t$ tangent to the rim at $T$, counterclockwise. The angle $\phi$ goes from $\mathbf i_1$ to $\mathbf e_r$ about $\mathbf k_0$, measured in the probe, as in the figure.
* **Senses, read from the figure (the velocity arrow drawn at $P$ in the statement is only schematic: the true velocity has a radial part from the winding):** the cord is wound counterclockwise from $A$ over the top towards $H$, the point $T$ moves counterclockwise from $A$ towards $H$, and the straight part of the cord leaves $T$ in the clockwise tangent direction, towards $P$ (the figure, with $T$ at about 70 degrees, puts $P$ at about 1.5 $R$ to the right and 0.5 $R$ up, which the position vector below reproduces). With this winding the cord pulls the rim clockwise, so it slows the probe only if the spin is counterclockwise: the spin is read as counterclockwise (rate of $\theta$ positive). The mirror reading (cord and spin both clockwise) changes the sign of every angle and leaves every magnitude unchanged.
* **Degrees of freedom:** the planar probe has three coordinates and each particle two (seven); each taut cord leaves its particle on the curve given by its angle of tangency, one condition per cord. **Five degrees of freedom**: the two coordinates of $G$, $\theta$ and the two angles of tangency. Both masses are released at the same instant from diametrically opposite points with equal cords, and the motion considered is the symmetric one, in which $P'$ is the image of $P$ by the half-turn about $G$ (it satisfies every equation below, written once for $P$); then the two angles of tangency are equal to $\phi$, $G$ stays at rest (shown in the next sections) and **two coordinates remain**, $\theta$ and $\phi$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the probe | $m$ | kg |
| Radius of the probe (rim on which the cords are wound) | $R$ | m |
| Moment of inertia of the probe about its axis | $I$ | kg m$^2$ |
| Mass of each yo-yo weight | $m/2$ | kg |
| Initial spin, desired final spin | $\omega_0$, $\omega_f$ | rad/s |
| Length of each cord (unknown of part (b)) | $L$ | m |
| Tension of each cord (unknown of part (c)) | $T_c \ge 0$ | N |
| Ratio used by the key | $K$, equal to $mR^2/(I + mR^2)$ | - |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb20-bases.svg]]

> [!derivation] Probe basis and cord basis: two rotations about k0
> **Law:** simple rotations about the third axis; right-hand rule; additivity of angular velocities; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the plane of the figure with $\mathbf k_0$ out of the paper (⊙): positive angles turn counterclockwise. $\mathbf i_1$ is $\mathbf i_0$ turned by $\theta$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine), opposite leg along $\mathbf j_0$ (sine). $\mathbf j_1$ is $\mathbf j_0$ turned by $\theta$: adjacent leg along $\mathbf j_0$ (cosine); the counterclockwise turn carries the tip of $\mathbf j_0$ to the left, towards minus $\mathbf i_0$, which is the minus sign. The cord basis is the probe basis turned by $\phi$ in the same way.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_0$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf e_r &= \cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1, \qquad \mathbf e_t = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1 \quad &\text{(same triangles with $\phi$; same matrix with $\phi$ in place of $\theta$)} \\
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k_0, \qquad \boldsymbol\omega_{21} = \dot\phi\,\mathbf k_0, \qquad \boldsymbol\omega_{20} = \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \left(\dot\theta + \dot\phi\right)\mathbf k_0 \quad &\text{(rates along the common axis; Eq. 3.14)} \\
> \dot{\mathbf e}_r &= \left(\dot\theta + \dot\phi\right)\mathbf k_0\times\mathbf e_r = \left(\dot\theta + \dot\phi\right)\mathbf e_t, \qquad \dot{\mathbf e}_t = \left(\dot\theta + \dot\phi\right)\mathbf k_0\times\mathbf e_t = -\left(\dot\theta + \dot\phi\right)\mathbf e_r \quad &\text{(Poisson in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_r = \cos\phi\,\mathbf i_1 + \sin\phi\,\mathbf j_1, \quad \mathbf e_t = -\sin\phi\,\mathbf i_1 + \cos\phi\,\mathbf j_1, \quad \dot{\mathbf e}_r = \left(\dot\theta + \dot\phi\right)\mathbf e_t, \quad \dot{\mathbf e}_t = -\left(\dot\theta + \dot\phi\right)\mathbf e_r}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** the absolute angle of the radius to the point of tangency is the sum of $\theta$ and $\phi$, so the cord basis turns with the sum of the two rates.

![[attachments/EM-SOL/rb20-involute.svg]]

> [!derivation] Position, velocity and acceleration of the yo-yo mass P
> **Law:** position as a sum of segments (taut, inextensible cord leaving the rim tangentially); product rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 9.4; Notes.pdf, Sec. 13.1
>
> The cord was wound on the rim from $A$; the free part, from $T$ to $P$, is straight and tangent to the rim at $T$, and its length is the unwound arc from $A$ to $T$, of length $R$ times $\phi$ (inextensible cord). The triangle $GTP$ has its right angle at $T$, the leg $R$ along $\mathbf e_r$, the leg of length $R\phi$ along minus $\mathbf e_t$, and the hypotenuse $GP$. The probe point at $T$ moves with the probe.
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{GT} + \overrightarrow{TP} = R\,\mathbf e_r - R\phi\,\mathbf e_t \quad &\text{(sum of segments; $G$ at rest at the origin)} \\
> \left|\mathbf r_0^P\right| &= R\sqrt{1 + \phi^2} \quad &\text{(Pythagoras in the triangle $GTP$)} \\
> \mathbf v_0^P &= R\,\dot{\mathbf e}_r - R\dot\phi\,\mathbf e_t - R\phi\,\dot{\mathbf e}_t \quad &\text{(product rule; $R$ constant)} \\
> &= R\left(\dot\theta + \dot\phi\right)\mathbf e_t - R\dot\phi\,\mathbf e_t + R\phi\left(\dot\theta + \dot\phi\right)\mathbf e_r = R\phi\left(\dot\theta + \dot\phi\right)\mathbf e_r + R\dot\theta\,\mathbf e_t \quad &\text{(Poisson; collect)} \\
> \mathbf a_0^P &= R\left[\dot\phi\left(\dot\theta + \dot\phi\right) + \phi\left(\ddot\theta + \ddot\phi\right)\right]\mathbf e_r + R\phi\left(\dot\theta + \dot\phi\right)\dot{\mathbf e}_r + R\ddot\theta\,\mathbf e_t + R\dot\theta\,\dot{\mathbf e}_t \quad &\text{(product rule on each term)} \\
> &= R\left[\left(\dot\phi - \dot\theta\right)\left(\dot\theta + \dot\phi\right) + \phi\left(\ddot\theta + \ddot\phi\right)\right]\mathbf e_r + R\left[\phi\left(\dot\theta + \dot\phi\right)^2 + \ddot\theta\right]\mathbf e_t \quad &\text{(Poisson; collect)} \\
> \mathbf v_0^{T(\text{probe})} &= \dot\theta\,\mathbf k_0\times R\,\mathbf e_r = R\dot\theta\,\mathbf e_t \quad &\text{(velocity field of the probe from $G$, Eq. 9.3)} \\
> \mathbf v_0^P - \mathbf v_0^{T(\text{probe})} &= R\phi\left(\dot\theta + \dot\phi\right)\mathbf e_r \quad &\text{(difference: normal to the cord)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = R\,\mathbf e_r - R\phi\,\mathbf e_t, \quad \mathbf v_0^P = R\phi\left(\dot\theta + \dot\phi\right)\mathbf e_r + R\dot\theta\,\mathbf e_t, \quad \mathbf a_0^P = R\left[\left(\dot\phi - \dot\theta\right)\left(\dot\theta + \dot\phi\right) + \phi\left(\ddot\theta + \ddot\phi\right)\right]\mathbf e_r + R\left[\phi\left(\dot\theta + \dot\phi\right)^2 + \ddot\theta\right]\mathbf e_t}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$ in every term
> **Meaning:** relative to the probe, $P$ moves on the involute of the rim. Along the cord ($\mathbf e_t$) the mass and the probe point at $T$ have the same velocity, as an inextensible cord requires; their relative velocity is normal to the cord. At the release the angle $\phi$ is zero and the velocity of $P$ is the rim velocity, whatever the rate of $\phi$.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass of the system and rotational inertia
> **Law:** definition of the centre of mass of a system; moment of inertia of particles; symmetry of the probe
> **Source:** Notes.pdf, Eq. 13.11; Notes.pdf, Eq. 10.9; Notes.pdf, Eq. 10.5
>
> The probe is axisymmetric: its centre of mass is $G$, on the axis $\mathbf k_0$, which is a principal axis with the moment $I$ (datum). In the symmetric motion the position of $P'$ from $G$ is minus that of $P$. The masses are particles: they have no inertia about their own centre.
>
> $$\begin{aligned}
> \left(m + \frac m2 + \frac m2\right)\mathbf r_0^{C} &= m\,\mathbf r_0^G + \frac m2\left(\mathbf r_0^G + \mathbf r_G^P\right) + \frac m2\left(\mathbf r_0^G - \mathbf r_G^P\right) \quad &\text{(Eq. 13.11 with the three parts)} \\
> \mathbf r_0^{C} &= \mathbf r_0^G \quad &\text{(the two terms in $\mathbf r_G^P$ cancel; divide by $2m$)} \\
> I_{\text{masses}}(t = 0) &= \frac m2 R^2 + \frac m2 R^2 = mR^2 \quad &\text{(Eq. 10.9 for two particles at the distance $R$ from the axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^{C} = \mathbf r_0^G, \qquad I_{\text{probe}} = I, \qquad I_{\text{masses}}(t = 0) = mR^2}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{M\,L^2}]$
> **Meaning:** the centre of mass of the whole system is the centre of the probe at every instant of the symmetric motion; before the release the system turns as one body with the moment $I$ plus $mR^2$, the sum that appears in the key.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momenta and kinetic energy of the system
> **Law:** linear momentum from the centre of mass; angular momentum of a body about its centre of mass and of a particle about a point; kinetic energy (Koenig) and kinetic energy of a particle
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 13.12
>
> The probe turns about its principal axis $\mathbf k_0$ with $\boldsymbol\omega_{10}$; each mass contributes the moment of its momentum about $G$, and $P'$ contributes the same as $P$ (both its position and its velocity are reversed).
>
> $$\begin{aligned}
> \mathbf p_0 &= 2m\,\mathbf v_0^{C} = 2m\,\mathbf v_0^G \quad &\text{(Eq. 11.3 for the system; previous box)} \\
> \mathbf r_0^P\times\mathbf v_0^P &= \begin{vmatrix} \mathbf e_r & \mathbf e_t & \mathbf k_0 \cr R & -R\phi & 0 \cr R\phi\left(\dot\theta + \dot\phi\right) & R\dot\theta & 0 \end{vmatrix} = \left[R^2\dot\theta + R^2\phi^2\left(\dot\theta + \dot\phi\right)\right]\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \mathbf H_G &= I\dot\theta\,\mathbf k_0 + 2\cdot\frac m2\,\mathbf r_0^P\times\mathbf v_0^P = \left[\left(I + mR^2\right)\dot\theta + mR^2\phi^2\left(\dot\theta + \dot\phi\right)\right]\mathbf k_0 \quad &\text{(Eq. 11.12 for the probe; two equal particle terms)} \\
> \left(v_0^P\right)^2 &= R^2\phi^2\left(\dot\theta + \dot\phi\right)^2 + R^2\dot\theta^2 \quad &\text{($\mathbf e_r$ and $\mathbf e_t$ orthonormal)} \\
> T_0 &= \frac12\,I\dot\theta^2 + 2\cdot\frac12\cdot\frac m2\left(v_0^P\right)^2 = \frac12\left(I + mR^2\right)\dot\theta^2 + \frac12\,mR^2\phi^2\left(\dot\theta + \dot\phi\right)^2 \quad &\text{(Eq. 11.31 with $G$ at rest; two particles)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = \left[\left(I + mR^2\right)\dot\theta + mR^2\phi^2\left(\dot\theta + \dot\phi\right)\right]\mathbf k_0, \qquad T_0 = \frac12\left(I + mR^2\right)\dot\theta^2 + \frac12\,mR^2\phi^2\left(\dot\theta + \dot\phi\right)^2}$$
>
> **Units:** kg m$^2$/s; J
> **Meaning:** as the cords unwind, the masses move out and their share of the angular momentum grows with the square of $\phi$; since the total does not change (next section), the probe's own share, and so its spin, must decrease.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb20-exploded.svg]]

The exploded view cuts each cord at the probe. A cord is massless and straight between $T$ and $P$, so it transmits the same tension $T_c$ along its own direction to both ends: on the mass it pulls towards $T$, along $\mathbf e_t$; on the probe it pulls at $T$ towards $P$, along minus $\mathbf e_t$. For the image cord, $T'$ is minus $R\,\mathbf e_r$ and the cord direction is reversed.

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Cord 1 on the probe | probe | $T$, at $R\,\mathbf e_r$ from $G$ | $-T_c\,\mathbf e_t$ | constraint (pair) |
| Cord 2 on the probe | probe | $T'$, at $-R\,\mathbf e_r$ from $G$ | $T_c\,\mathbf e_t$ | constraint (pair) |
| Cord 1 on the mass | $P$ | $P$ | $T_c\,\mathbf e_t$ | constraint (pair) |
| Cord 2 on the mass | $P'$ | $P'$ | $-T_c\,\mathbf e_t$ | constraint (pair) |
| Gravity | all | - | negligible (statement) | - |

> [!derivation] Equations of the probe (force, and moment about its centre G)
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass; moments by determinants expanded along the first row
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9
>
> The pole $G$ is the centre of mass of the probe, so the pole term of Eq. 12.13 vanishes. The probe turns about its fixed principal axis $\mathbf k_0$, so its angular momentum is $I$ times the rate of $\theta$ along $\mathbf k_0$ and its derivative is $I$ times the second rate.
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= -T_c\,\mathbf e_t + T_c\,\mathbf e_t = \mathbf 0 \quad &\text{(Eq. 12.8; the two cord forces cancel)} \\
> \mathbf M_G &= R\,\mathbf e_r\times\left(-T_c\,\mathbf e_t\right) + \left(-R\,\mathbf e_r\right)\times T_c\,\mathbf e_t = \begin{vmatrix} \mathbf e_r & \mathbf e_t & \mathbf k_0 \cr R & 0 & 0 \cr 0 & -T_c & 0 \end{vmatrix} + \begin{vmatrix} \mathbf e_r & \mathbf e_t & \mathbf k_0 \cr -R & 0 & 0 \cr 0 & T_c & 0 \end{vmatrix} = -2RT_c\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> I\ddot\theta\,\mathbf k_0 &= -2RT_c\,\mathbf k_0 \quad &\text{(Eq. 12.13 about $G$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^G = \mathbf 0, \qquad I\ddot\theta = -2RT_c}$$
>
> **Units:** N; N m
> **Meaning:** the centre of the probe does not accelerate, so with $G$ initially at rest it stays at rest, as assumed in the position vector. Each taut cord pulls the rim clockwise with the arm $R$: the spin decreases while the tension is positive.

> [!derivation] Equations of the yo-yo mass P
> **Law:** Newton's second law for a particle
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 13.10
>
> $$\begin{aligned}
> \frac m2\,\mathbf a_0^P &= T_c\,\mathbf e_t \quad &\text{(the cord is the only force)} \\
> \frac m2\,R\left[\left(\dot\phi - \dot\theta\right)\left(\dot\theta + \dot\phi\right) + \phi\left(\ddot\theta + \ddot\phi\right)\right] &= 0 \quad &\text{(component along $\mathbf e_r$; acceleration box)} \\
> \frac m2\,R\left[\phi\left(\dot\theta + \dot\phi\right)^2 + \ddot\theta\right] &= T_c \quad &\text{(component along $\mathbf e_t$)}
> \end{aligned}$$
>
> $$\boxed{\left(\dot\phi - \dot\theta\right)\left(\dot\theta + \dot\phi\right) + \phi\left(\ddot\theta + \ddot\phi\right) = 0, \qquad T_c = \frac{mR}{2}\left[\phi\left(\dot\theta + \dot\phi\right)^2 + \ddot\theta\right]}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in the first equation; N in the second
> **Meaning:** with the probe equation, three equations for three unknowns ($\theta$, $\phi$ and $T_c$); the equations of $P'$ are the same, by the symmetry.

> [!derivation] Combination: conservation of the angular momentum about G
> **Law:** elimination of the tension between the probe and the mass; product rule
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 13.12; Notes.pdf, Eq. 12.13
>
> Write $\Omega$ for the sum of the rates of $\theta$ and $\phi$ (the absolute rate of the cord basis). The radial equation of the mass, multiplied by $\phi$, gives the square of $\phi$ times the rate of $\Omega$.
>
> $$\begin{aligned}
> I\ddot\theta &= -2R\cdot\frac{mR}{2}\left(\phi\,\Omega^2 + \ddot\theta\right) \;\Rightarrow\; \left(I + mR^2\right)\ddot\theta + mR^2\phi\,\Omega^2 = 0 \quad &\text{(probe equation with the tangential equation of the mass)} \\
> \phi^2\dot\Omega &= -\phi\left(\dot\phi - \dot\theta\right)\Omega \quad &\text{(radial equation of the mass times $\phi$)} \\
> \frac{d}{dt}\left(\phi^2\Omega\right) &= 2\phi\dot\phi\,\Omega + \phi^2\dot\Omega = 2\phi\dot\phi\,\Omega - \phi\dot\phi\,\Omega + \phi\dot\theta\,\Omega = \phi\,\Omega^2 \quad &\text{(product rule; previous row; collect)} \\
> \frac{d}{dt}\left[\left(I + mR^2\right)\dot\theta + mR^2\phi^2\Omega\right] &= \left(I + mR^2\right)\ddot\theta + mR^2\phi\,\Omega^2 = 0 \quad &\text{(first row)} \\
> \left[H_G\right]_0^t &= 0 \;\Rightarrow\; H_G(t) = H_G(0) \quad &\text{(integrate from 0 to $t$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\left(I + mR^2\right)\dot\theta + mR^2\phi^2\left(\dot\theta + \dot\phi\right) = H_G(0)}$$
>
> **Units:** kg m$^2$/s
> **Meaning:** the bracket is the angular momentum of the previous section: the equations of the parts reproduce the conservation that Eq. 13.12 gives directly for the whole system, on which no external moment acts and whose centre of mass $G$ is at rest (no pole term).

> [!derivation] Combination: conservation of the kinetic energy
> **Law:** probe equation times the rate of $\theta$ plus the mass equations; product rule; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.30; Notes.pdf, Sec. 13.4
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\phi^2\Omega^2\right) &= 2\phi\dot\phi\,\Omega^2 + 2\phi^2\Omega\dot\Omega = 2\phi\dot\phi\,\Omega^2 - 2\phi\left(\dot\phi - \dot\theta\right)\Omega^2 = 2\phi\dot\theta\,\Omega^2 \quad &\text{(product rule; radial equation times $\phi$)} \\
> \frac{d}{dt}\left[\left(I + mR^2\right)\dot\theta^2 + mR^2\phi^2\Omega^2\right] &= 2\dot\theta\left[\left(I + mR^2\right)\ddot\theta + mR^2\phi\,\Omega^2\right] = 0 \quad &\text{(chain rule; first row of the previous box)} \\
> \left[T_0\right]_0^t &= 0 \;\Rightarrow\; T_0(t) = T_0(0) \quad &\text{(integrate; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\left(I + mR^2\right)\dot\theta^2 + mR^2\phi^2\left(\dot\theta + \dot\phi\right)^2 = 2\,T_0(0)}$$
>
> **Units:** J
> **Meaning:** the cords do no net work: they only transfer energy from the spin of the probe to the motion of the masses (checked with the power of the pairs in Answers and Checks).

> [!derivation] Part (a): initial values and the spin of the probe as a function of time
> **Law:** the two first integrals with the state at the release; solution of two algebraic equations; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 13.12; Notes.pdf, Eq. 2.6
>
> At the release ($t$ zero) the masses ride on the rim: $\phi$ is zero and the velocity of $P$, from the velocity box with $\phi$ zero, is $R$ times the initial spin along $\mathbf e_t$, whatever the rate of $\phi$. The integrals are evaluated with that velocity. Write $\omega$ for the rate of $\theta$ and $c$ for the ratio of $I + mR^2$ to $mR^2$ (the inverse of $K$).
>
> $$\begin{aligned}
> H_G(0) &= I\omega_0 + m\,R\cdot R\omega_0 = \left(I + mR^2\right)\omega_0, \qquad 2T_0(0) = I\omega_0^2 + m\left(R\omega_0\right)^2 = \left(I + mR^2\right)\omega_0^2 \quad &\text{(state at the release)} \\
> \phi^2\,\Omega &= c\left(\omega_0 - \omega\right), \qquad \phi^2\,\Omega^2 = c\left(\omega_0^2 - \omega^2\right) = c\left(\omega_0 - \omega\right)\left(\omega_0 + \omega\right) \quad &\text{(the two integrals divided by $mR^2$)} \\
> \Omega &= \omega_0 + \omega \;\Rightarrow\; \dot\phi = \Omega - \omega = \omega_0 \quad &\text{(divide the second by the first, allowed while the spin differs from $\omega_0$)} \\
> \int_0^t\dot\phi\,dt' &= \int_0^t\omega_0\,dt' \;\Rightarrow\; \left[\phi\right]_0^t = \omega_0\left[t'\right]_0^t \;\Rightarrow\; \phi = \omega_0 t \quad &\text{(antiderivatives; Barrow's rule; $\phi$ zero at the release)} \\
> \omega_0^2 t^2\left(\omega_0 + \omega\right) &= c\left(\omega_0 - \omega\right) \quad &\text{(first integral with $\phi$ and $\Omega$)} \\
> \omega\left(c + \omega_0^2 t^2\right) &= \omega_0\left(c - \omega_0^2 t^2\right) \;\Rightarrow\; \omega = \omega_0\,\frac{c - \omega_0^2 t^2}{c + \omega_0^2 t^2} = \omega_0\,\frac{1 - K\omega_0^2 t^2}{1 + K\omega_0^2 t^2} \quad &\text{(collect the spin; divide numerator and denominator by $c$)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi = \omega_0, \quad \phi = \omega_0 t, \qquad \omega(t) = \dot\theta = \omega_0\,\frac{1 - K\omega_0^2 t^2}{1 + K\omega_0^2 t^2}, \quad K = \frac{mR^2}{I + mR^2}}$$
>
> **Units:** $K\omega_0^2 t^2$ is $[\mathrm{T^{-2}}][\mathrm{T^2}]$, dimensionless; $\omega$ in $[\mathrm{T^{-1}}]$
> **Meaning:** the cords unwind at the constant relative rate $\omega_0$, from the first instant: the rate of $\phi$ is not continuous at the release, which is allowed because at $\phi$ zero the velocity of the mass does not depend on it. The other root of the division, a spin equal to $\omega_0$ for all time, needs the product of the square of $\phi$ and $\Omega$ to stay zero: either the masses stay on the rim, or the cords wind back with $\phi$ negative; neither is the released motion. The spin falls monotonically; it is zero when the product of $K$ and the square of the time and of $\omega_0$ equals one, and negative (reversed) afterwards.

> [!derivation] Part (a): attitude of the probe and motion of the masses
> **Law:** integration of the spin with Barrow's rule; derivative of the arctangent (chain rule)
> **Source:** Notes.pdf, Eq. 2.6
>
> The spin is rewritten as twice $\omega_0$ over the denominator, minus $\omega_0$. The derivative of the arctangent of $\sqrt K\,\omega_0 t$ is $\sqrt K\,\omega_0$ over the same denominator (chain rule).
>
> $$\begin{aligned}
> \omega &= \frac{2\omega_0}{1 + K\omega_0^2 t^2} - \omega_0 \quad &\text{(add and subtract one in the fraction)} \\
> \int_0^t\omega\,dt' &= \left[\frac{2}{\sqrt K}\arctan\left(\sqrt K\,\omega_0 t'\right) - \omega_0 t'\right]_0^t \quad &\text{(antiderivative)} \\
> \theta(t) - \theta(0) &= \frac{2}{\sqrt K}\arctan\left(\sqrt K\,\omega_0 t\right) - \omega_0 t \quad &\text{(Barrow's rule; the arctangent of zero is zero)} \\
> \theta + \phi &= \theta(0) + \frac{2}{\sqrt K}\arctan\left(\sqrt K\,\omega_0 t\right) \quad &\text{(absolute angle of the point of tangency, with $\phi$ from part (a))}
> \end{aligned}$$
>
> $$\boxed{\theta(t) = \theta(0) + \frac{2}{\sqrt K}\arctan\left(\sqrt K\,\omega_0 t\right) - \omega_0 t, \qquad \mathbf r_0^P = R\,\mathbf e_r - R\,\omega_0 t\,\mathbf e_t}$$
>
> **Units:** radians; m
> **Meaning:** the point of tangency turns in space at the rate $\Omega$, twice $\omega_0$ over the denominator: it starts at twice $\omega_0$ and decreases towards zero as time grows, so its absolute angle tends to the finite value $\pi$ over $\sqrt K$. When the cords are released, each mass leaves along a straight line with its velocity at that instant, and the probe keeps its final spin, since no torque acts on it any longer.

> [!derivation] Part (b): length of the cord for the final spin
> **Law:** part (a) at the instant of release of the cords
> **Source:** Notes.pdf, Eq. 13.12
>
> The cords leave the probe when $T$ reaches $H$: the whole cord, of length $L$, is then straight, so the unwound arc $R\phi$ equals $L$; at that instant the spin must be $\omega_f$.
>
> $$\begin{aligned}
> \phi_f &= \frac LR = \omega_0 t_f \quad &\text{(whole cord unwound; part (a))} \\
> \omega_f &= \omega_0\,\frac{1 - K\phi_f^2}{1 + K\phi_f^2} \;\Rightarrow\; \omega_f + K\phi_f^2\omega_f = \omega_0 - K\phi_f^2\omega_0 \quad &\text{(part (a) at $t_f$; multiply out)} \\
> K\phi_f^2 &= \frac{\omega_0 - \omega_f}{\omega_0 + \omega_f} \quad &\text{(collect)} \\
> L^2 &= R^2\phi_f^2 = \frac{R^2}{K}\cdot\frac{\omega_0 - \omega_f}{\omega_0 + \omega_f} = \frac{I + mR^2}{m}\cdot\frac{\omega_0 - \omega_f}{\omega_0 + \omega_f} \quad &\text{(value of $K$)}
> \end{aligned}$$
>
> $$\boxed{L^2 = \frac{\left(I + mR^2\right)\left(\omega_0 - \omega_f\right)}{m\left(\omega_0 + \omega_f\right)}, \qquad t_f = \frac{L}{R\,\omega_0}}$$
>
> **Units:** $[\mathrm{M\,L^2}]/[\mathrm M] = [\mathrm{L^2}]$; $[\mathrm L]/([\mathrm L][\mathrm{T^{-1}}]) = [\mathrm T]$
> **Meaning:** the length does not depend on $\omega_0$ itself, only on the ratio of the two spins. To stop the spin completely the cord must be the square root of the ratio of $I + mR^2$ to $m$; with $I$ equal to $mR^2$ this is $\sqrt 2$ times $R$, about 1.414 $R$. A longer cord reverses the spin.

> [!derivation] Part (c): tension of each cord as a function of time
> **Law:** probe equation; derivative of the spin of part (a) by the chain rule
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.8
>
> Write $u$ for the product of $K$, the square of $\omega_0$ and the square of $t$; its rate is twice the product of $K$, the square of $\omega_0$ and $t$.
>
> $$\begin{aligned}
> \frac{d\omega}{du} &= \omega_0\,\frac{-\left(1 + u\right) - \left(1 - u\right)}{\left(1 + u\right)^2} = -\frac{2\omega_0}{\left(1 + u\right)^2} \quad &\text{(quotient rule)} \\
> \ddot\theta &= \frac{d\omega}{du}\,\frac{du}{dt} = -\frac{2\omega_0}{\left(1 + u\right)^2}\cdot 2K\omega_0^2 t = -\frac{4K\omega_0^3 t}{\left(1 + K\omega_0^2 t^2\right)^2} \quad &\text{(chain rule)} \\
> T_c &= -\frac{I\ddot\theta}{2R} = \frac{2KI\omega_0^3 t}{R\left(1 + K\omega_0^2 t^2\right)^2} \quad &\text{(probe equation)} \\
> \frac{d}{dt}\left[\frac{t}{\left(1 + u\right)^2}\right] &= \frac{\left(1 + u\right) - 4u}{\left(1 + u\right)^3} = 0 \;\Rightarrow\; u = \frac13 \quad &\text{(quotient and chain rules; maximum)} \\
> T_{c,\max} &= \frac{2KI\omega_0^3}{R}\cdot\frac{1}{\omega_0\sqrt{3K}}\cdot\frac{9}{16} = \frac{3\sqrt3}{8}\,\sqrt K\,\frac{I\omega_0^2}{R} \quad &\text{(time of the maximum; value of the bracket at $u$ one third)}
> \end{aligned}$$
>
> $$\boxed{T_c(t) = \frac{2KI\omega_0^3\,t}{R\left(1 + K\omega_0^2 t^2\right)^2} \quad (0 \le t \le t_f), \qquad T_{c,\max} = \frac{3\sqrt3}{8}\sqrt K\,\frac{I\omega_0^2}{R} \ \text{ at } \ t = \frac{1}{\omega_0\sqrt{3K}}}$$
>
> **Units:** $[\mathrm{M\,L^2}][\mathrm{T^{-3}}][\mathrm T]/[\mathrm L] = [\mathrm{M\,L\,T^{-2}}]$, N
> **Meaning:** the tension starts at zero, is positive for every later time (the cords stay taut, as assumed), peaks and then decays; it vanishes after the release of the cords. With $K$ equal to one half the peak is about 0.459 times the ratio of $I$ times the square of $\omega_0$ to $R$, at $\omega_0 t$ about 0.816 (graph below).

![[attachments/EM-SOL/rb20-graph.svg]]

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Motion and spin of the probe | $G$ at rest; cords unwind at the constant rate $\dot\phi = \omega_0$, $\phi = \omega_0 t$; $\omega(t) = \omega_0(1 - K\omega_0^2t^2)/(1 + K\omega_0^2t^2)$ with $K = mR^2/(I + mR^2)$; $\theta = \theta_0 + (2/\sqrt K)\arctan(\sqrt K\omega_0 t) - \omega_0 t$; masses on the involute $\mathbf r^P = R\,\mathbf e_r - R\omega_0 t\,\mathbf e_t$ |
| (b) Cord length | $L^2 = (I + mR^2)(\omega_0 - \omega_f)/[m(\omega_0 + \omega_f)]$, released at $t_f = L/(R\omega_0)$ |
| (c) Tension of each cord | $T_c = 2KI\omega_0^3 t/[R(1 + K\omega_0^2t^2)^2]$ for $0 \le t \le t_f$; maximum $\tfrac{3\sqrt3}{8}\sqrt K\,I\omega_0^2/R$ at $t = 1/(\omega_0\sqrt{3K})$ |

> [!derivation] Check: power of the cord pairs and the tension from the mass equation
> **Law:** power of the forces of a pair on two bodies; tangential equation of the mass with the motion of part (a)
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.8
>
> First, the energy integral without the equations: the pair of cord 1 acts on $P$ and on the probe point at $T$. Second, the tension from the equation of the mass instead of the probe, with the rate of $\phi$ equal to $\omega_0$ and $\Omega$ equal to $\omega_0 + \omega$.
>
> $$\begin{aligned}
> \dot W^{\text{cord 1}} &= T_c\,\mathbf e_t\cdot\mathbf v_0^P - T_c\,\mathbf e_t\cdot\mathbf v_0^{T(\text{probe})} = T_c\,\mathbf e_t\cdot R\phi\,\Omega\,\mathbf e_r = 0 \quad &\text{(relative velocity normal to the cord, position box)} \\
> \omega_0 + \omega &= \frac{2\omega_0}{1 + u}, \qquad \phi\left(\omega_0 + \omega\right)^2 = \frac{4\omega_0^2\,\omega_0 t}{\left(1 + u\right)^2} \quad &\text{(part (a); $u$ of part (c))} \\
> \phi\,\Omega^2 + \ddot\theta &= \frac{4\omega_0^3 t - 4K\omega_0^3 t}{\left(1 + u\right)^2} = \frac{4\left(1 - K\right)\omega_0^3 t}{\left(1 + u\right)^2} \quad &\text{(second rate of $\theta$ from part (c))} \\
> 1 - K &= \frac{I}{I + mR^2} = \frac{KI}{mR^2} \quad &\text{(value of $K$)} \\
> \frac{mR}{2}\left(\phi\,\Omega^2 + \ddot\theta\right) &= \frac{mR}{2}\cdot\frac{4KI\omega_0^3 t}{mR^2\left(1 + u\right)^2} = \frac{2KI\omega_0^3 t}{R\left(1 + u\right)^2} \quad &\text{(tangential equation of the mass)}
> \end{aligned}$$
>
> $$\boxed{\dot W^{\text{cord}} = 0, \qquad T_c\big|_{\text{mass}} = T_c\big|_{\text{probe}} = \frac{2KI\omega_0^3 t}{R\left(1 + K\omega_0^2t^2\right)^2}}$$
>
> **Units:** W; N
> **Meaning:** the cords are workless, which confirms the energy integral; the tension computed from either end of the cord is the same, so the tangential equation of the mass is satisfied by the motion of part (a); the radial equation is satisfied too, because its two terms cancel for the same motion (centripetal term of the mass against the term of the winding rate).

**Check against the official key:** the key (Problems.pdf, p. 80) prints the required length, the square of $L$ equal to $(I + mR^2)(\omega_0 - \omega_f)$ over $m(\omega_0 + \omega_f)$, and the tension $2KI\omega_0^3 t$ over $R(1 + K\omega_0^2t^2)^2$, with $K$ equal to $mR^2/(I + mR^2)$. Both coincide with the boxes of parts (b) and (c); the key's tension is that of one cord (the probe equation holds twice that tension, one per cord): **match**. The key prints no expression for part (a); the spin of part (a) is the one consistent with both printed results.

**Limiting cases and consistency:**

* **Light weights.** With $m$ much smaller than the ratio of $I$ to the square of $R$, $K$ tends to zero: the spin hardly changes during any finite time and the length of part (b) grows without bound.
* **No de-spin requested.** With $\omega_f$ equal to $\omega_0$ the length of part (b) is zero: no cord, no change.
* **Complete stop.** With $\omega_f$ zero, the square of $\phi_f$ is the inverse of $K$; at that instant the angular momentum is carried by the masses alone, each at the distance $R\sqrt{1 + \phi_f^2}$ from $G$.
* **Tension at the start.** At the release the tension is zero, consistent with the masses riding on the rim at that instant.
* **Dimensions.** $K$ is a ratio of two moments of inertia; $K\omega_0^2t^2$ is dimensionless; $L^2$ is a moment of inertia over a mass; $T_c$ is a moment of inertia times an angular acceleration over a length.

---

## Problem RB-21: Reaction wheel spacecraft attitude control

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** three rigid bodies in deep space, with no external force or torque. The spacecraft $b$ is a homogeneous rod of mass $6M$, length $L$ and negligible diameter, with centre $G$. The reaction wheels $w_1$ and $w_2$ are thin homogeneous discs of radius $R$ and mass $M$ (the tensor of the statement is that of a thin disc), with centres $G_1$ and $G_2$ at the two ends of the rod and their axes along the rod; each turns relative to the rod about the rod axis, driven by its motor.
* **Inertial frame:** $S_0\{O; \mathcal B_0\}$, with $\mathcal B_0\{\mathbf i_0, \mathbf j_0, \mathbf k_0\}$ along the axes $x$, $y$, $z$ of the figure ($z$ up). The frame $S_G\{G; \mathcal B_0\}$ translates with $G$ without rotating.
* **Intermediate basis:** $\mathcal B'\{\mathbf i', \mathbf j', \mathbf k_0\}$, turned by $\theta$ about $\mathbf k_0$; $\mathbf i'$ is the horizontal projection of the rod direction (the dashed line of the figure).
* **Spacecraft frame:** $S_b\{G; \mathcal B_b\}$, with $\mathbf i_b$ along the rod from wheel 2 to wheel 1, $\mathbf j_b$ equal to $\mathbf j'$ (horizontal) and $\mathbf k_b$ completing the right-handed basis (the axes $x_B$, $y_B$, $z_B$ of the figure; the statement writes $\mathbf i_B$ for $\mathbf i_b$).
* **Angles, read from the figure:** $\theta$ is the azimuth, from $\mathbf i_0$ to the projection $\mathbf i'$, about $\mathbf k_0$; $\varphi$ is the elevation of the rod above the horizontal plane $Gxy$ (its arc runs from the dashed projection up to $x_B$), about minus $\mathbf j'$. If $\varphi$ were read as the polar angle from $\mathbf k_0$, sine and cosine of $\varphi$ would swap in every formula below and the sign of its rate would flip, since the polar angle grows when the elevation falls: the $\mathbf j_b$ component of the spacecraft angular velocity would be plus the rate of the polar angle, and its initial value would be plus $\Omega/\sqrt2$. At the initial instant both readings give the same direction, since $\varphi$ is $\pi/4$. The wheel angles $\phi_1$ and $\phi_2$ are measured relative to $\mathcal B_b$ about $\mathbf i_b$.
* **The degenerate rod.** A rod of negligible diameter has no moment of inertia about its own axis, so a spin of the rod about that axis carries no momentum and no energy: the frame $\mathcal B_b$ is fixed to the direction of the rod by $\theta$ and $\varphi$ alone, and the wheel rates are measured from it. The initial angular velocity of the statement is consistent with this (checked in the next section).
* **Coordinates:** the position of $G$ (three), $\theta$, $\varphi$, $\phi_1$ and $\phi_2$. The momentum of the system is conserved and initially zero, so $G$ stays at the origin (shown below) and four coordinates remain.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass and length of the spacecraft rod | $6M$, $L$ | kg, m |
| Mass and radius of each wheel | $M$, $R$ | kg, m |
| Position of the wheel centres | $G_1$ and $G_2$ at $\pm(L/2)\,\mathbf i_b$ from $G$ | m |
| Tensor of the rod at $G$, in $\mathcal B_b$ | $\tfrac{1}{12}(6M)L^2\,\mathrm{diag}(0, 1, 1)$ | kg m$^2$ |
| Tensor of each wheel at its centre, in $\mathcal B_b$ | $\tfrac14 MR^2\,\mathrm{diag}(2, 1, 1)$ | kg m$^2$ |
| Initial state | $\mathbf r_0^G = \mathbf 0$, $\mathbf v_0^G = \mathbf 0$, $\theta = 0$, $\varphi = \pi/4$, $\phi_1 = \phi_2 = 0$, $\dot\phi_1 = \dot\phi_2 = \Omega/2$, $\boldsymbol\omega_{b0} = \tfrac{\Omega}{\sqrt2}\left[\tfrac{1}{\sqrt2}\mathbf i_b + \mathbf j_b + \tfrac{1}{\sqrt2}\mathbf k_b\right]$ | m, m/s, rad, rad/s |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb21-rot-theta.svg]]

> [!derivation] Intermediate basis: rotation by theta about k0
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; [Lecture 7, Slide 12]
>
> View from above, $\mathbf k_0$ out of the paper (⊙): a positive $\theta$ turns counterclockwise. $\mathbf i'$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine), opposite leg along $\mathbf j_0$ (sine). $\mathbf j'$: adjacent leg along $\mathbf j_0$ (cosine); the counterclockwise turn carries the tip of $\mathbf j_0$ towards minus $\mathbf i_0$, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf i' &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j' = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_{'}] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i'$, $\mathbf j'$, $\mathbf k_0$ in $\mathcal B_0$)} \\
> \det[{}_0R_{'}] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_{'}][{}_0R_{'}]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{'0} &= \dot\theta\,\mathbf k_0 \quad &\text{(rate of the angle along its axis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i' = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j' = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0, \qquad \boldsymbol\omega_{'0} = \dot\theta\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $\mathbf i'$ is the horizontal direction under the rod; $\mathbf j'$ is horizontal and normal to the vertical plane of the rod.

![[attachments/EM-SOL/rb21-rot-phi.svg]]

> [!derivation] Spacecraft basis: rotation by phi (elevation) about minus j'
> **Law:** simple rotation about the second axis; right-hand rule; product of rotation matrices
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> View of the vertical plane of the rod with $\mathbf i'$ to the right and $\mathbf k_0$ up; then $\mathbf j'$ points into the paper (⊗), because the cross product of $\mathbf i'$ and $\mathbf k_0$ is minus $\mathbf j'$, out of the paper. Raising the rod by $\varphi$ is a counterclockwise turn as seen, that is a positive rotation about the axis out of the paper, minus $\mathbf j'$. $\mathbf i_b$: adjacent leg along $\mathbf i'$ (cosine of $\varphi$), opposite leg along $\mathbf k_0$ (sine). $\mathbf k_b$: adjacent leg along $\mathbf k_0$ (cosine); the counterclockwise turn carries the tip of $\mathbf k_0$ to the left, towards minus $\mathbf i'$, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\varphi\,\mathbf i' + \sin\varphi\,\mathbf k_0, \qquad \mathbf j_b = \mathbf j', \qquad \mathbf k_b = -\sin\varphi\,\mathbf i' + \cos\varphi\,\mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_{'}R_b] &= \begin{bmatrix} \cos\varphi & 0 & -\sin\varphi \cr 0 & 1 & 0 \cr \sin\varphi & 0 & \cos\varphi \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$ in $\mathcal B'$)} \\
> \det[{}_{'}R_b] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_{'}R_b][{}_{'}R_b]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & 0 & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi \cr 0 & 1 & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & 0 & \sin^2\varphi + \cos^2\varphi \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> [{}_0R_b] &= [{}_0R_{'}][{}_{'}R_b] = \begin{bmatrix} \cos\theta\cos\varphi & -\sin\theta & -\cos\theta\sin\varphi \cr \sin\theta\cos\varphi & \cos\theta & -\sin\theta\sin\varphi \cr \sin\varphi & 0 & \cos\varphi \end{bmatrix} \quad &\text{(row of the first times column of the second)} \\
> \mathbf k_0 &= \sin\varphi\,\mathbf i_b + \cos\varphi\,\mathbf k_b \quad &\text{(third row: the inverse is the transpose)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \cos\theta\cos\varphi\,\mathbf i_0 + \sin\theta\cos\varphi\,\mathbf j_0 + \sin\varphi\,\mathbf k_0, \quad \mathbf j_b = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0, \quad \mathbf k_b = -\cos\theta\sin\varphi\,\mathbf i_0 - \sin\theta\sin\varphi\,\mathbf j_0 + \cos\varphi\,\mathbf k_0}$$
>
> **Units:** dimensionless
> **Meaning:** the first column is the unit vector of spherical coordinates with azimuth $\theta$ and elevation $\varphi$; $\mathbf k_b$ leans away from the vertical, backwards from the rod, as $z_B$ in the figure.

> [!derivation] Part (a): angular velocities of the spacecraft and of the wheels
> **Law:** additivity of angular velocities; rate of each angle along its own axis
> **Source:** Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 9.21; [Lecture 7, Slide 12]
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b'} + \boldsymbol\omega_{'0} = -\dot\varphi\,\mathbf j_b + \dot\theta\,\mathbf k_0 \quad &\text{(Eq. 3.14; elevation about minus $\mathbf j'$)} \\
> &= \dot\theta\sin\varphi\,\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b \quad &\text{($\mathbf k_0$ in $\mathcal B_b$, previous box)} \\
> \boldsymbol\omega_{10} &= \boldsymbol\omega_{1b} + \boldsymbol\omega_{b0} = \left(\dot\theta\sin\varphi + \dot\phi_1\right)\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b \quad &\text{(Eq. 3.14; wheel 1 turns about $\mathbf i_b$ relative to $b$)} \\
> \boldsymbol\omega_{20} &= \left(\dot\theta\sin\varphi + \dot\phi_2\right)\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b \quad &\text{(same for wheel 2)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \dot\theta\sin\varphi\,\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b, \qquad \boldsymbol\omega_{i0} = \left(\dot\theta\sin\varphi + \dot\phi_i\right)\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b \quad (i = 1, 2)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every component
> **Meaning:** the wheels share the transverse components of the spacecraft and differ from it only along the rod, by their own rates.

> [!derivation] Initial angular velocity: values of the rates of theta and phi
> **Law:** comparison of components in $\mathcal B_b$
> **Source:** Notes.pdf, Eq. 3.14
>
> At the initial instant the elevation is $\pi/4$, so the sine and the cosine of $\varphi$ are both $1/\sqrt2$.
>
> $$\begin{aligned}
> \frac{\dot\theta(0)}{\sqrt2}\,\mathbf i_b - \dot\varphi(0)\,\mathbf j_b + \frac{\dot\theta(0)}{\sqrt2}\,\mathbf k_b &= \frac{\Omega}{2}\,\mathbf i_b + \frac{\Omega}{\sqrt2}\,\mathbf j_b + \frac{\Omega}{2}\,\mathbf k_b \quad &\text{(part (a) against the statement)} \\
> \dot\theta(0) &= \frac{\Omega}{\sqrt2}, \qquad \dot\varphi(0) = -\frac{\Omega}{\sqrt2} \quad &\text{(components along $\mathbf i_b$ or $\mathbf k_b$, and along $\mathbf j_b$)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta(0) = \frac{\Omega}{\sqrt2}, \qquad \dot\varphi(0) = -\frac{\Omega}{\sqrt2}}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** three components fix two rates, and the statement's components along $\mathbf i_b$ and $\mathbf k_b$ are equal, as part (a) requires at this elevation: the data are consistent with a frame that has no own spin about the rod (an own spin would change the $\mathbf i_b$ component only). Initially the azimuth grows and the elevation decreases: the rod turns counterclockwise seen from above while tilting down towards the horizontal plane.

> [!derivation] Part (b): positions and absolute velocities of G1 and G2
> **Law:** velocity field of the rigid body $b$ (the wheel centres are points of the rod); vector product by a determinant expanded along the first row
> **Source:** Notes.pdf, Eq. 9.3; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf r_0^{G_1} &= \mathbf r_0^G + \frac L2\,\mathbf i_b, \qquad \mathbf r_0^{G_2} = \mathbf r_0^G - \frac L2\,\mathbf i_b \quad &\text{(wheels at the ends of the rod)} \\
> \boldsymbol\omega_{b0}\times\frac L2\,\mathbf i_b &= \frac L2\begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta\sin\varphi & -\dot\varphi & \dot\theta\cos\varphi \cr 1 & 0 & 0 \end{vmatrix} = \frac L2\left(\dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b\right) \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{G_1} &= \mathbf v_0^G + \frac L2\left(\dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b\right), \qquad \mathbf v_0^{G_2} = \mathbf v_0^G - \frac L2\left(\dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b\right) \quad &\text{(Eq. 9.3 from $G$)} \\
> \frac{d\mathbf i_b}{dt} &= \left(-\dot\theta\sin\theta\cos\varphi - \dot\varphi\cos\theta\sin\varphi\right)\mathbf i_0 + \left(\dot\theta\cos\theta\cos\varphi - \dot\varphi\sin\theta\sin\varphi\right)\mathbf j_0 + \dot\varphi\cos\varphi\,\mathbf k_0 \quad &\text{(second route: chain and product rules on the components of $\mathbf i_b$)} \\
> &= \dot\theta\cos\varphi\left(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0\right) + \dot\varphi\left(-\cos\theta\sin\varphi\,\mathbf i_0 - \sin\theta\sin\varphi\,\mathbf j_0 + \cos\varphi\,\mathbf k_0\right) = \dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b \quad &\text{(group; $\mathbf j_b$ and $\mathbf k_b$ in $\mathcal B_0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^{G_{1,2}} = \mathbf v_0^G \pm \frac L2\left[\dot\theta\cos\varphi\left(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0\right) + \dot\varphi\left(-\cos\theta\sin\varphi\,\mathbf i_0 - \sin\theta\sin\varphi\,\mathbf j_0 + \cos\varphi\,\mathbf k_0\right)\right]}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$ in every term
> **Meaning:** relative to $G$ the wheel centres move on a sphere of radius $L/2$, along the azimuthal direction (rate of $\theta$, scaled by the cosine of the elevation: the radius of the parallel) and the meridian direction (rate of $\varphi$); the two velocities are opposite, so their mean is the velocity of $G$.

### Center of Mass and Inertia Tensor

> [!derivation] Centre of mass of the assembly
> **Law:** centre of mass of a system of bodies
> **Source:** Notes.pdf, Eq. 13.11
>
> $$\begin{aligned}
> 8M\,\mathbf r_0^{C} &= 6M\,\mathbf r_0^G + M\left(\mathbf r_0^G + \frac L2\,\mathbf i_b\right) + M\left(\mathbf r_0^G - \frac L2\,\mathbf i_b\right) \quad &\text{(Eq. 13.11 with the three bodies)} \\
> \mathbf r_0^{C} &= \mathbf r_0^G \quad &\text{(the terms in $\mathbf i_b$ cancel; divide by $8M$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^{C} = \mathbf r_0^G}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** as the statement says, $G$ is the centre of mass of the rod and of the whole assembly.

> [!derivation] Tensor of the rod at G
> **Law:** moments of inertia of a thin rod as a line integral; Barrow's rule
> **Source:** Notes.pdf, Eq. 10.9; Notes.pdf, Eq. 10.11; [Lecture 8, Slide 10]
>
> The rod lies on the axis $\mathbf i_b$, from minus $L/2$ to $L/2$, with linear density $\lambda$ equal to $6M/L$; a point at the abscissa $x$ is at the distance $x$ from the axes $\mathbf j_b$ and $\mathbf k_b$ and at zero distance from $\mathbf i_b$ (negligible diameter); the products of inertia contain a zero coordinate.
>
> $$\begin{aligned}
> I^b_{yy} &= \int_{-L/2}^{L/2}x^2\,\lambda\,dx = \lambda\left[\frac{x^3}{3}\right]_{-L/2}^{L/2} = \lambda\left(\frac{L^3}{24} + \frac{L^3}{24}\right) = \frac{\lambda L^3}{12} \quad &\text{(antiderivative; Barrow's rule)} \\
> &= \frac{6M}{L}\cdot\frac{L^3}{12} = \frac{6ML^2}{12} = \frac{ML^2}{2}, \qquad I^b_{zz} = I^b_{yy}, \qquad I^b_{xx} = 0 \quad &\text{(value of $\lambda$; same distance; zero distance)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}{}^b_G = \frac{ML^2}{2}\begin{bmatrix} 0 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}_b}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the datum of the statement, one twelfth of $6ML^2$; the rod resists turning about any transverse axis, not about its own axis.

> [!derivation] Tensor of each wheel at its centre, and of the two wheels at G
> **Law:** moments of inertia of a thin disc as area integrals (jacobian $\rho$); symmetry of revolution; Steiner's theorem
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.35; Notes.pdf, Eq. 10.48; [Lecture 8, Slide 15]
>
> Surface density $\sigma$ equal to $M/(\pi R^2)$; a point of the wheel is at $\rho\cos\chi\,\mathbf j + \rho\sin\chi\,\mathbf k$ from its centre, in the plane normal to $\mathbf i_b$.
>
> $$\begin{aligned}
> I^w_{xx} &= \sigma\int_0^{2\pi}\!\!\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R = \frac{M}{\pi R^2}\cdot\frac{2\pi R^4}{4} = \frac{MR^2}{2} \quad &\text{(antiderivatives; Barrow's rule)} \\
> I^w_{yy} &= \sigma\int_0^{2\pi}\!\!\sin^2\chi\,d\chi\int_0^R\rho^3\,d\rho = \sigma\left[\frac\chi2 - \frac{\sin2\chi}{4}\right]_0^{2\pi}\frac{R^4}{4} = \frac{M}{\pi R^2}\cdot\pi\cdot\frac{R^4}{4} = \frac{MR^2}{4} \quad &\text{(squared distance to the diameter $\mathbf j_b$; Barrow's rule)} \\
> I^w_{zz} &= \frac{MR^2}{4}, \qquad P_{yz} = \sigma\left[\frac{\sin^2\chi}{2}\right]_0^{2\pi}\frac{R^4}{4} = 0 \quad &\text{(cosine in place of the sine; antiderivative and Barrow's rule)} \\
> \bar{\bar I}{}^{w}_{G}\Big|_{\text{position}} &= M\left[\left(\frac L2\right)^2\mathcal U - \left(\frac L2\right)^2\mathbf i_b\otimes\mathbf i_b\right] = \frac{ML^2}{4}\,\mathrm{diag}\left(0, 1, 1\right) \quad &\text{(Steiner, Eq. 10.48, term of a mass $M$ at $\pm\frac L2\,\mathbf i_b$)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}{}^{w_i}_{G_i} = \frac{MR^2}{4}\begin{bmatrix} 2 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}_b, \qquad \bar{\bar I}{}^{w_1 + w_2}_G = \begin{bmatrix} MR^2 & 0 & 0 \cr 0 & \frac{MR^2}{2} + \frac{ML^2}{2} & 0 \cr 0 & 0 & \frac{MR^2}{2} + \frac{ML^2}{2} \end{bmatrix}_b}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the datum of the statement. The wheel is symmetric about $\mathbf i_b$, so its tensor keeps these components in $\mathcal B_b$ although it spins relative to the rod; this is why $\mathcal B_b$ is used for the wheels below. With the rod, the whole assembly has the moment $MR^2$ about the rod and $ML^2$ plus $MR^2/2$ about any transverse axis.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (c): angular momentum of each wheel about its centre
> **Law:** angular momentum about the centre of mass
> **Source:** Notes.pdf, Eq. 11.12; [Lecture 9, Slide 5]
>
> $$\begin{aligned}
> \mathbf H_{G_1}^{w_1} &= \bar{\bar I}{}^{w_1}_{G_1}\cdot\boldsymbol\omega_{10} = \frac{MR^2}{4}\begin{bmatrix} 2 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} \dot\theta\sin\varphi + \dot\phi_1 \cr -\dot\varphi \cr \dot\theta\cos\varphi \end{bmatrix} \quad &\text{(Eq. 11.12; components in $\mathcal B_b$)} \\
> &= \frac{MR^2}{4}\left[2\left(\dot\theta\sin\varphi + \dot\phi_1\right)\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right] \quad &\text{(matrix product)} \\
> \mathbf H_{G_2}^{w_2} &= \frac{MR^2}{4}\left[2\left(\dot\theta\sin\varphi + \dot\phi_2\right)\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right] \quad &\text{(same with $\boldsymbol\omega_{20}$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G_i}^{w_i} = \frac{MR^2}{2}\left(\dot\theta\sin\varphi + \dot\phi_i\right)\mathbf i_b - \frac{MR^2}{4}\dot\varphi\,\mathbf j_b + \frac{MR^2}{4}\dot\theta\cos\varphi\,\mathbf k_b \quad (i = 1, 2)}$$
>
> **Units:** $[\mathrm{M\,L^2}][\mathrm{T^{-1}}]$, kg m$^2$/s
> **Meaning:** the spin of each wheel relative to the rod enters only the axial component, with the axial moment; the transverse components are those of a disc turning with the spacecraft.

> [!derivation] Parts (d) and (e): linear momentum, total angular momentum about G and kinetic energy
> **Law:** linear momentum of a system; change of pole from the centre of each body (Eq. 11.21); Koenig's theorem for each body
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.21; Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 13.12
>
> Write $\mathbf u$ for the bracket of part (b), the velocity of $G_1$ relative to $G$ divided by $L/2$: its components in $\mathcal B_b$ are zero, the rate of $\theta$ times the cosine of $\varphi$, and the rate of $\varphi$.
>
> $$\begin{aligned}
> \mathbf p_0 &= 6M\,\mathbf v_0^G + M\,\mathbf v_0^{G_1} + M\,\mathbf v_0^{G_2} = 8M\,\mathbf v_0^G \quad &\text{(Eq. 11.3 per body; part (b): the relative terms cancel)} \\
> \mathbf H_G^{b} &= \bar{\bar I}{}^b_G\cdot\boldsymbol\omega_{b0} = \frac{ML^2}{2}\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right) \quad &\text{(Eq. 11.12 for the rod)} \\
> \sum_i M\,\mathbf r_G^{G_i}\times\mathbf v_0^{G_i} &= 2M\,\frac L2\,\mathbf i_b\times\frac L2\,\mathbf u + M\left(\frac L2\,\mathbf i_b - \frac L2\,\mathbf i_b\right)\times\mathbf v_0^G = \frac{ML^2}{2}\begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr 1 & 0 & 0 \cr 0 & \dot\theta\cos\varphi & \dot\varphi \end{vmatrix} \quad &\text{(Eq. 11.21; the terms in the velocity of $G$ cancel, the relative terms add)} \\
> &= \frac{ML^2}{2}\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right) \quad &\text{(expand along the first row)} \\
> \mathbf H_G &= \mathbf H_G^b + \sum_i\left(\mathbf H_{G_i}^{w_i} + M\,\mathbf r_G^{G_i}\times\mathbf v_0^{G_i}\right) \quad &\text{(sum over the three bodies)} \\
> &= \frac{MR^2}{2}\left(2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2\right)\mathbf i_b + \left(ML^2 + \frac{MR^2}{2}\right)\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right) \quad &\text{(part (c); collect)} \\
> T_0 &= \frac12\,8M\left(v_0^G\right)^2 + \left(\frac{ML^2}{2} + \frac{MR^2}{4}\right)\left(\dot\varphi^2 + \dot\theta^2\cos^2\varphi\right) + \frac{MR^2}{4}\sum_i\left(\dot\theta\sin\varphi + \dot\phi_i\right)^2 \quad &\text{(Eq. 11.31 per body; cross terms in the velocity of $G$ cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = 8M\,\mathbf v_0^G, \quad \mathbf H_G = \frac{MR^2}{2}\left(2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2\right)\mathbf i_b + \left(ML^2 + \frac{MR^2}{2}\right)\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right), \quad T_0 = 4M\left(v_0^G\right)^2 + \left(\frac{ML^2}{2} + \frac{MR^2}{4}\right)\left(\dot\varphi^2 + \dot\theta^2\cos^2\varphi\right) + \frac{MR^2}{4}\left[\left(\dot\theta\sin\varphi + \dot\phi_1\right)^2 + \left(\dot\theta\sin\varphi + \dot\phi_2\right)^2\right]}$$
>
> **Units:** kg m/s; kg m$^2$/s; J
> **Meaning:** the angular momentum along the rod is held only by the wheels; the transverse part is that of the whole assembly turning with the rod.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb21-exploded.svg]]

No external load acts. The exploded view cuts each wheel from the rod at its axle: the rod acts on wheel $i$ at $G_i$ with the force $\mathbf F_i$ and the torque $\mathbf Q_i$ (bearing reactions normal to the axle plus the motor torque along $\mathbf i_b$), and the wheel acts on the rod with $-\mathbf F_i$ and $-\mathbf Q_i$ (third law of Newton).

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Axle 1 | $w_1$ | $G_1$ | $\mathbf F_1$, $\mathbf Q_1$ (its $\mathbf i_b$ component is the motor torque) | internal (pair) |
| Axle 2 | $w_2$ | $G_2$ | $\mathbf F_2$, $\mathbf Q_2$ | internal (pair) |
| Wheels on the rod | $b$ | $G_1$, $G_2$ | $-\mathbf F_1$, $-\mathbf Q_1$; $-\mathbf F_2$, $-\mathbf Q_2$ | internal (pair) |
| Gravity and other external loads | all | - | negligible (deep space) | - |

> [!derivation] Equations of each body
> **Law:** Newton's second law for each centre of mass; moment equation about each centre of mass
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> Each moment equation is taken about the centre of mass of its own body, so the pole term of Eq. 12.13 is a velocity crossed with itself, zero. The axle force on a wheel acts at its centre and has no moment about it.
>
> $$\begin{aligned}
> M\,\mathbf a_0^{G_i} &= \mathbf F_i, \qquad \frac{d\mathbf H_{G_i}^{w_i}}{dt}\bigg|_0 = \mathbf Q_i \quad (i = 1, 2) \quad &\text{(wheel $i$)} \\
> 6M\,\mathbf a_0^{G} &= -\mathbf F_1 - \mathbf F_2 \quad &\text{(rod, force)} \\
> \frac{d\mathbf H_{G}^{b}}{dt}\bigg|_0 &= \frac L2\,\mathbf i_b\times\left(-\mathbf F_1\right) - \frac L2\,\mathbf i_b\times\left(-\mathbf F_2\right) - \mathbf Q_1 - \mathbf Q_2 \quad &\text{(rod, moment about $G$; arms of $G_1$ and $G_2$)}
> \end{aligned}$$
>
> $$\boxed{M\mathbf a_0^{G_i} = \mathbf F_i, \quad \dot{\mathbf H}_{G_i}^{w_i} = \mathbf Q_i, \quad 6M\mathbf a_0^G = -\mathbf F_1 - \mathbf F_2, \quad \dot{\mathbf H}_G^b = -\frac L2\,\mathbf i_b\times\left(\mathbf F_1 - \mathbf F_2\right) - \mathbf Q_1 - \mathbf Q_2}$$
>
> **Units:** N; N m
> **Meaning:** eighteen scalar equations of the three bodies; their combinations below contain no axle load, and the axle loads of part (g) follow from the equations of the wheels.

> [!derivation] Combination: the centre of mass stays at rest and the total angular momentum is constant
> **Law:** sum of the equations of the parts; derivative of the moment of momentum; Barrow's rule
> **Source:** Notes.pdf, Eq. 13.12; Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 15.6; Notes.pdf, Eq. 15.7
>
> From part (b), the mean of the velocities of $G_1$ and $G_2$ is the velocity of $G$, and so is the mean of their accelerations (time derivative).
>
> $$\begin{aligned}
> 6M\,\mathbf a_0^G + M\,\mathbf a_0^{G_1} + M\,\mathbf a_0^{G_2} &= \mathbf 0 \;\Rightarrow\; 8M\,\mathbf a_0^G = \mathbf 0 \quad &\text{(sum of the force equations; the pairs cancel)} \\
> \left[\mathbf v_0^G\right]_0^t &= \mathbf 0 \;\Rightarrow\; \mathbf v_0^G = \mathbf 0, \qquad \left[\mathbf r_0^G\right]_0^t = \mathbf 0 \;\Rightarrow\; \mathbf r_0^G = \mathbf 0 \quad &\text{(integrate twice; Barrow's rule; initial values zero)} \\
> \frac{d}{dt}\left(\mathbf r_G^{G_i}\times M\,\mathbf v_0^{G_i}\right) &= \mathbf v_0^{G_i}\times M\,\mathbf v_0^{G_i} + \mathbf r_G^{G_i}\times M\,\mathbf a_0^{G_i} = \mathbf r_G^{G_i}\times\mathbf F_i \quad &\text{(product rule; $G$ at rest, so the rate of the arm is the velocity of $G_i$)} \\
> \frac{d\mathbf H_G}{dt}\bigg|_0 &= \dot{\mathbf H}_G^b + \sum_i\left(\mathbf Q_i + \mathbf r_G^{G_i}\times\mathbf F_i\right) = -\frac L2\,\mathbf i_b\times\left(\mathbf F_1 - \mathbf F_2\right) - \mathbf Q_1 - \mathbf Q_2 + \mathbf Q_1 + \mathbf Q_2 + \frac L2\,\mathbf i_b\times\left(\mathbf F_1 - \mathbf F_2\right) = \mathbf 0 \quad &\text{(sum of the moment equations)} \\
> \left[\mathbf H_G\right]_0^t &= \mathbf 0 \;\Rightarrow\; \mathbf H_G(t) = \mathbf H_G(0) \quad &\text{(integrate; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G(t) = \mathbf 0, \qquad \mathbf v_0^G(t) = \mathbf 0, \qquad \mathbf H_G(t) = \mathbf H_G(0)}$$
>
> **Units:** m; m/s; kg m$^2$/s
> **Meaning:** the axle loads are internal, so the total angular momentum about the fixed centre of mass is a constant vector of $S_0$. What this allows the motors to do is worked out in part (f): with the wheels on the axis of a rod that has no axial inertia, they cannot change the direction of the rod.

> [!derivation] Initial values: the conserved angular momentum and the initial kinetic energy
> **Law:** the expressions of the previous section at the initial instant; change of basis
> **Source:** Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 13.12
>
> At the initial instant the sine and cosine of $\varphi$ are $1/\sqrt2$, $\theta$ is zero, the rates are those found above and each wheel rate is $\Omega/2$; the products of the rate of $\theta$ with the sine and with the cosine of $\varphi$ are both $\Omega/2$.
>
> $$\begin{aligned}
> \mathbf H_G(0) &= \frac{MR^2}{2}\left(\Omega + \Omega\right)\mathbf i_b + \left(ML^2 + \frac{MR^2}{2}\right)\left(\frac{\Omega}{\sqrt2}\,\mathbf j_b + \frac{\Omega}{2}\,\mathbf k_b\right) \quad &\text{(previous section at $t$ zero)} \\
> \mathbf i_b(0) &= \frac{\mathbf i_0 + \mathbf k_0}{\sqrt2}, \qquad \mathbf j_b(0) = \mathbf j_0, \qquad \mathbf k_b(0) = \frac{-\mathbf i_0 + \mathbf k_0}{\sqrt2} \quad &\text{(columns of $[{}_0R_b]$ at $\theta$ zero, $\varphi$ equal to $\pi/4$)} \\
> \mathbf H_G(0) &= \frac{M\Omega}{2\sqrt2}\left[\left(2R^2 - L^2 - \frac{R^2}{2}\right)\mathbf i_0 + \left(2L^2 + R^2\right)\mathbf j_0 + \left(2R^2 + L^2 + \frac{R^2}{2}\right)\mathbf k_0\right] \quad &\text{(substitute; collect)} \\
> T_0(0) &= \left(\frac{ML^2}{2} + \frac{MR^2}{4}\right)\left(\frac{\Omega^2}{2} + \frac{\Omega^2}{4}\right) + \frac{MR^2}{4}\left(\Omega^2 + \Omega^2\right) = \frac{3ML^2\Omega^2}{8} + \frac{11MR^2\Omega^2}{16} \quad &\text{(kinetic energy at $t$ zero; $G$ at rest)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G = \frac{\sqrt2\,M\Omega}{8}\left[\left(3R^2 - 2L^2\right)\mathbf i_0 + 2\left(2L^2 + R^2\right)\mathbf j_0 + \left(2L^2 + 5R^2\right)\mathbf k_0\right] \ \text{(constant)}, \qquad T_0(0) = \frac{M\Omega^2\left(6L^2 + 11R^2\right)}{16}}$$
>
> **Units:** $[\mathrm M][\mathrm{T^{-1}}][\mathrm{L^2}]$; $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the angular momentum keeps this value for all time (combination box); the kinetic energy is only its initial value, since the motors can do work (part (f)). The boxed form of the angular momentum takes a factor one half out of each bracket of the previous line, and its components are called $h_x$, $h_y$, $h_z$ below.

> [!derivation] Part (f): what the constant angular momentum imposes on the rod
> **Law:** conservation of the total angular momentum; derivative of a scalar product (product rule); scalar triple product with a repeated vector
> **Source:** Notes.pdf, Eq. 15.6; Notes.pdf, Eq. 15.7; Notes.pdf, Eq. 9.4
>
> Write $J$ for the transverse moment of the assembly, $ML^2$ plus $MR^2/2$, $\mathbf h$ for the constant value of $\mathbf H_G$ and $A$ for its component along the rod. The rate of $\mathbf i_b$ is the bracket of part (b).
>
> $$\begin{aligned}
> \mathbf h &= A\,\mathbf i_b + J\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right), \qquad A = \frac{MR^2}{2}\left(2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2\right) \quad &\text{(part (d))} \\
> \mathbf h\times\mathbf i_b &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr A & -J\dot\varphi & J\dot\theta\cos\varphi \cr 1 & 0 & 0 \end{vmatrix} = J\left(\dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b\right) = J\,\dot{\mathbf i}_b \quad &\text{(expand along the first row; part (b))} \\
> \dot{\mathbf i}_b &= \frac{\mathbf h}{J}\times\mathbf i_b \quad &\text{(divide by $J$)} \\
> \frac{d}{dt}\left(\mathbf h\cdot\mathbf i_b\right) &= \dot{\mathbf h}\cdot\mathbf i_b + \mathbf h\cdot\dot{\mathbf i}_b = 0 + \frac1J\,\mathbf h\cdot\left(\mathbf h\times\mathbf i_b\right) = 0 \quad &\text{(product rule; no external moment; triple product with $\mathbf h$ twice)} \\
> A(t) &= A(0) = \frac{MR^2}{2}\left(\Omega + \Omega\right) = MR^2\,\Omega \;\Rightarrow\; 2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2 = 2\Omega \quad &\text{(initial values; divide by $MR^2/2$)} \\
> \left|\mathbf h\right|^2 &= A^2 + J^2\left(\dot\varphi^2 + \dot\theta^2\cos^2\varphi\right) = M^2R^4\Omega^2 + \frac34\,J^2\Omega^2 = \frac{M^2\Omega^2\left(12L^4 + 12L^2R^2 + 19R^4\right)}{16} \quad &\text{(orthonormal components at $t$ zero; value of $J$)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i}_b = \frac{\mathbf H_G}{J}\times\mathbf i_b, \qquad 2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2 = 2\Omega, \qquad J = ML^2 + \frac{MR^2}{2}, \qquad \left|\mathbf H_G\right| = \frac{M\Omega}{4}\sqrt{12L^4 + 12L^2R^2 + 19R^4}}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{M\,L^2\,T^{-1}}]$
> **Meaning:** the component of the angular momentum along the moving rod is constant for two reasons: the angular momentum itself does not change (no external moment) and the rate of $\mathbf i_b$ is normal to it. The direction of the rod turns about the fixed direction of $\mathbf H_G$ at the constant rate $|\mathbf H_G|/J$, keeping a constant angle to it, and the wheel rates do not appear in that equation: a rod with no inertia about its own axis, carrying the wheels on that axis, cannot be steered by them. The motors only exchange axial spin between the two wheels; the sum in the boxed relation is fixed and only the difference of the wheel rates is free.

> [!derivation] Part (g): axle force on each wheel
> **Law:** Newton's second law for the centre of each wheel; second derivative of the unit vector of the rod (product rule, Poisson's formula)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 13.9
>
> With $G$ at rest, the acceleration of $G_1$ is $L/2$ times the second rate of $\mathbf i_b$, and that of $G_2$ is its opposite. The rates of $\mathbf j_b$ and $\mathbf k_b$ come from Poisson's formula with $\boldsymbol\omega_{b0}$ of part (a); $s$ and $c$ stand for the sine and cosine of $\varphi$.
>
> $$\begin{aligned}
> \dot{\mathbf j}_b &= \boldsymbol\omega_{b0}\times\mathbf j_b = \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta s & -\dot\varphi & \dot\theta c \cr 0 & 1 & 0 \end{vmatrix} = -\dot\theta c\,\mathbf i_b + \dot\theta s\,\mathbf k_b \quad &\text{(Poisson; expand along the first row)} \\
> \dot{\mathbf k}_b &= \boldsymbol\omega_{b0}\times\mathbf k_b = \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta s & -\dot\varphi & \dot\theta c \cr 0 & 0 & 1 \end{vmatrix} = -\dot\varphi\,\mathbf i_b - \dot\theta s\,\mathbf j_b \quad &\text{(Poisson; expand along the first row)} \\
> \ddot{\mathbf i}_b &= \frac{d}{dt}\left(\dot\theta c\,\mathbf j_b + \dot\varphi\,\mathbf k_b\right) = \left(\ddot\theta c - \dot\theta\dot\varphi s\right)\mathbf j_b + \dot\theta c\,\dot{\mathbf j}_b + \ddot\varphi\,\mathbf k_b + \dot\varphi\,\dot{\mathbf k}_b \quad &\text{(product rule; chain rule on the cosine)} \\
> &= -\left(\dot\varphi^2 + \dot\theta^2 c^2\right)\mathbf i_b + \left(\ddot\theta c - 2\dot\theta\dot\varphi s\right)\mathbf j_b + \left(\ddot\varphi + \dot\theta^2 s c\right)\mathbf k_b \quad &\text{(substitute the two rates; collect)} \\
> \mathbf F_1 &= M\,\mathbf a_0^{G_1} = M\,\frac L2\,\ddot{\mathbf i}_b, \qquad \mathbf F_2 = M\,\mathbf a_0^{G_2} = -M\,\frac L2\,\ddot{\mathbf i}_b \quad &\text{(Eq. 12.8 for each wheel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_1 = -\mathbf F_2 = \frac{ML}{2}\left[-\left(\dot\varphi^2 + \dot\theta^2\cos^2\varphi\right)\mathbf i_b + \left(\ddot\theta\cos\varphi - 2\dot\theta\dot\varphi\sin\varphi\right)\mathbf j_b + \left(\ddot\varphi + \dot\theta^2\sin\varphi\cos\varphi\right)\mathbf k_b\right]}$$
>
> **Units:** $[\mathrm M][\mathrm L][\mathrm{T^{-2}}]$, N
> **Meaning:** the $\mathbf i_b$ part is the centripetal force that keeps each wheel on the sphere of radius $L/2$ about $G$, pointing from the wheel towards $G$; the other two are the tangential parts. The rod receives minus these forces, which cancel each other, in agreement with $G$ at rest; the two forces form a couple on the rod.

> [!derivation] Part (g): axle torque on each wheel
> **Law:** moment equation about the centre of each wheel; derivative in the rotating basis of the rod
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 13.9
>
> The tensor of the wheel has constant components in $\mathcal B_b$ (symmetry about $\mathbf i_b$), so the components of part (c) are differentiated and the turning of $\mathcal B_b$ is added (Eq. 3.8 with $\boldsymbol\omega_{b0}$). Write $a_i$, $b$, $c_3$ for the components of $\mathbf H_{G_i}$ of part (c): $a_i$ is $MR^2/2$ times the axial rate of the wheel, $b$ is minus $MR^2/4$ times the rate of $\varphi$, and $c_3$ is $MR^2/4$ times the rate of $\theta$ times the cosine of $\varphi$.
>
> $$\begin{aligned}
> \mathbf Q_i &= \frac{d\mathbf H_{G_i}}{dt}\bigg|_b + \boldsymbol\omega_{b0}\times\mathbf H_{G_i} \quad &\text{(Eq. 12.13 about $G_i$; Eq. 3.8)} \\
> \frac{d\mathbf H_{G_i}}{dt}\bigg|_b &= \frac{MR^2}{2}\left(\ddot\theta s + \dot\theta\dot\varphi c + \ddot\phi_i\right)\mathbf i_b - \frac{MR^2}{4}\ddot\varphi\,\mathbf j_b + \frac{MR^2}{4}\left(\ddot\theta c - \dot\theta\dot\varphi s\right)\mathbf k_b \quad &\text{(product and chain rules on each component)} \\
> \boldsymbol\omega_{b0}\times\mathbf H_{G_i} &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta s & -\dot\varphi & \dot\theta c \cr a_i & b & c_3 \end{vmatrix} = \left(-\dot\varphi c_3 - \dot\theta c\,b\right)\mathbf i_b + \left(\dot\theta c\,a_i - \dot\theta s\,c_3\right)\mathbf j_b + \left(\dot\theta s\,b + \dot\varphi\,a_i\right)\mathbf k_b \quad &\text{(expand along the first row)} \\
> &= 0\,\mathbf i_b + \left[\frac{MR^2}{2}\dot\theta c\left(\dot\theta s + \dot\phi_i\right) - \frac{MR^2}{4}\dot\theta^2 s c\right]\mathbf j_b + \left[-\frac{MR^2}{4}\dot\theta\dot\varphi s + \frac{MR^2}{2}\dot\varphi\left(\dot\theta s + \dot\phi_i\right)\right]\mathbf k_b \quad &\text{(values of $a_i$, $b$, $c_3$)} \\
> \mathbf Q_i &= \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta s + \dot\phi_i\right)\mathbf i_b + \frac{MR^2}{4}\left(-\ddot\varphi + \dot\theta^2 s c + 2\dot\theta c\,\dot\phi_i\right)\mathbf j_b + \frac{MR^2}{4}\left(\ddot\theta c + 2\dot\varphi\,\dot\phi_i\right)\mathbf k_b \quad &\text{(sum; collect)}
> \end{aligned}$$
>
> $$\boxed{\mathbf Q_i = \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta\sin\varphi + \dot\phi_i\right)\mathbf i_b + \frac{MR^2}{4}\left(-\ddot\varphi + \dot\theta^2\sin\varphi\cos\varphi + 2\dot\theta\cos\varphi\,\dot\phi_i\right)\mathbf j_b + \frac{MR^2}{4}\left(\ddot\theta\cos\varphi + 2\dot\varphi\,\dot\phi_i\right)\mathbf k_b \quad (i = 1, 2)}$$
>
> **Units:** $[\mathrm{M\,L^2}][\mathrm{T^{-2}}]$, N m
> **Meaning:** the $\mathbf i_b$ component is the motor torque $\tau_i$; the two transverse components are the bearing torques, which turn the axis of the wheel with the rod and contain the gyroscopic terms in the product of the wheel rate and the rates of the rod. The rod receives minus these torques.

> [!derivation] Part (f): the set of ordinary differential equations and the count
> **Law:** force equation of the system; components of the precession equation; axial moment equations of the rod and of the wheels; power of the motor pair
> **Source:** Notes.pdf, Eq. 13.12; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.29; Notes.pdf, Sec. 13.4
>
> The rod has no angular momentum along $\mathbf i_b$, and the rates of $\mathbf j_b$ and $\mathbf k_b$ along $\mathbf i_b$ are minus the rate of $\theta$ times the cosine of $\varphi$ and minus the rate of $\varphi$ (previous boxes). The components of $\mathbf h$ in $\mathcal B_0$ are $h_x$, $h_y$, $h_z$ (initial-values box). The moments of the axle forces about $G$ have no $\mathbf i_b$ component, since their arms lie along $\mathbf i_b$.
>
> $$\begin{aligned}
> \ddot{\mathbf r}_0^G &= \mathbf 0, \quad \mathbf r_0^G(0) = \mathbf 0, \quad \dot{\mathbf r}_0^G(0) = \mathbf 0 \;\Rightarrow\; \mathbf r_0^G(t) = \mathbf 0 \quad &\text{(combination box)} \\
> \dot{\mathbf i}_b\cdot\mathbf j_b &= \dot\theta\cos\varphi = \frac1J\left(\mathbf h\times\mathbf i_b\right)\cdot\mathbf j_b = \frac1J\,\mathbf h\cdot\left(\mathbf i_b\times\mathbf j_b\right) = \frac{\mathbf h\cdot\mathbf k_b}{J} \quad &\text{(precession box; cyclic triple product)} \\
> \dot{\mathbf i}_b\cdot\mathbf k_b &= \dot\varphi = \frac1J\,\mathbf h\cdot\left(\mathbf i_b\times\mathbf k_b\right) = -\frac{\mathbf h\cdot\mathbf j_b}{J} \quad &\text{(same; the cross product of $\mathbf i_b$ and $\mathbf k_b$ is minus $\mathbf j_b$)} \\
> \dot\theta\cos\varphi &= \frac{-h_x\cos\theta\sin\varphi - h_y\sin\theta\sin\varphi + h_z\cos\varphi}{J}, \qquad \dot\varphi = \frac{h_x\sin\theta - h_y\cos\theta}{J} \quad &\text{($\mathbf j_b$, $\mathbf k_b$ in $\mathcal B_0$)} \\
> \frac{d\mathbf H^b_G}{dt}\cdot\mathbf i_b &= \frac{ML^2}{2}\left[-\dot\varphi\,\dot{\mathbf j}_b\cdot\mathbf i_b + \dot\theta\cos\varphi\,\dot{\mathbf k}_b\cdot\mathbf i_b\right] = \frac{ML^2}{2}\left(\dot\varphi\dot\theta\cos\varphi - \dot\theta\cos\varphi\,\dot\varphi\right) = 0 = -\tau_1 - \tau_2 \quad &\text{(rod, moment along $\mathbf i_b$)} \\
> \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta\sin\varphi + \dot\phi_1\right) &= \tau_1, \qquad \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta\sin\varphi + \dot\phi_2\right) = \tau_2 = -\tau_1 \quad &\text{(wheels along $\mathbf i_b$, torque box)} \\
> \dot W^{\text{motors}} &= \mathbf Q_1\cdot\left(\boldsymbol\omega_{10} - \boldsymbol\omega_{b0}\right) + \mathbf Q_2\cdot\left(\boldsymbol\omega_{20} - \boldsymbol\omega_{b0}\right) = \tau_1\dot\phi_1 + \tau_2\dot\phi_2 = \tau_1\left(\dot\phi_1 - \dot\phi_2\right) \quad &\text{(power of the axle pairs, Eq. 12.29; relative rates along $\mathbf i_b$)} \\
> \dot\theta(0)\cos\frac{\pi}{4} &= \frac{h_z - h_x}{\sqrt2\,J} = \frac{\sqrt2\,M\Omega\left(4L^2 + 2R^2\right)}{8\sqrt2\,J} = \frac{\Omega}{2}, \qquad \dot\varphi(0) = -\frac{h_y}{J} = -\frac{\sqrt2\,M\Omega\left(2L^2 + R^2\right)}{4J} = -\frac{\Omega}{\sqrt2} \quad &\text{(check at $t$ zero; $J$ equal to $M(2L^2 + R^2)/2$)} \\
> n_{\text{unknowns}} &= 3 + 4 + 3 + 3 + 3 + 3 = 19, \qquad n_{\text{eq}} = 6 + 6 + 6 = 18 \quad &\text{($\mathbf r_0^G$, four angles, $\mathbf F_1$, $\mathbf F_2$, $\mathbf Q_1$, $\mathbf Q_2$; three bodies)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \ddot{\mathbf r}_0^G = \mathbf 0 \ (\mathbf r_0^G = \mathbf 0), \qquad \dot\theta\cos\varphi = \frac{\mathbf H_G\cdot\mathbf k_b}{J}, \qquad \dot\varphi = -\frac{\mathbf H_G\cdot\mathbf j_b}{J}, \\ \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta\sin\varphi + \dot\phi_1\right) = \tau_1, \qquad \frac{MR^2}{2}\frac{d}{dt}\left(\dot\theta\sin\varphi + \dot\phi_2\right) = -\tau_1, \qquad \tau_1(t) \text{ free (motor law)} \end{gathered}}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in the attitude equations; N m in the wheel equations
> **Meaning:** nineteen unknowns and eighteen equations: the problem is underdetermined by one, the law of one motor, which must be given (for example the torque or the difference of the wheel rates). The attitude equations are first-order and closed in $\theta$ and $\varphi$; the wheel equations, given the motor law, fix the two wheel rates, whose sum with twice the axial rate of the rod stays equal to twice $\Omega$. At the initial instant the attitude equations return the rates found from the data (row before the count). The kinetic energy changes only through the motor power, the motor torque times the difference of the wheel rates.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Angular velocities, in $\mathcal B_b$ | $\boldsymbol\omega_{b0} = \dot\theta\sin\varphi\,\mathbf i_b - \dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b$; $\boldsymbol\omega_{10} = \boldsymbol\omega_{b0} + \dot\phi_1\,\mathbf i_b$; $\boldsymbol\omega_{20} = \boldsymbol\omega_{b0} + \dot\phi_2\,\mathbf i_b$ |
| (b) Velocities of $G_1$, $G_2$ | $\mathbf v^{G_{1,2}} = \mathbf v^G \pm \tfrac L2(\dot\theta\cos\varphi\,\mathbf j_b + \dot\varphi\,\mathbf k_b)$, with $\mathbf j_b = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$, $\mathbf k_b = -\cos\theta\sin\varphi\,\mathbf i_0 - \sin\theta\sin\varphi\,\mathbf j_0 + \cos\varphi\,\mathbf k_0$ (and $\mathbf v^G = \mathbf 0$ for the given data) |
| (c) Angular momentum of each wheel about its centre | $\mathbf H_{G_i} = \tfrac{MR^2}{2}(\dot\theta\sin\varphi + \dot\phi_i)\,\mathbf i_b - \tfrac{MR^2}{4}\dot\varphi\,\mathbf j_b + \tfrac{MR^2}{4}\dot\theta\cos\varphi\,\mathbf k_b$ |
| (d) Angular momentum of the system about $G$ | $\mathbf H_G = \tfrac{MR^2}{2}(2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2)\,\mathbf i_b + (ML^2 + \tfrac{MR^2}{2})(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b)$, constant |
| (e) Kinetic energy | $T = 4M(v^G)^2 + (\tfrac{ML^2}{2} + \tfrac{MR^2}{4})(\dot\varphi^2 + \dot\theta^2\cos^2\varphi) + \tfrac{MR^2}{4}[(\dot\theta\sin\varphi + \dot\phi_1)^2 + (\dot\theta\sin\varphi + \dot\phi_2)^2]$; $T(0) = M\Omega^2(6L^2 + 11R^2)/16$ |
| (f) Equations of motion | $\ddot{\mathbf r}^G = \mathbf 0$ ($\mathbf r^G = \mathbf 0$); $\dot\theta\cos\varphi = \mathbf H_G\cdot\mathbf k_b/J$, $\dot\varphi = -\mathbf H_G\cdot\mathbf j_b/J$ with $J = ML^2 + MR^2/2$ (the rod precesses about $\mathbf H_G$ at the rate $\lvert\mathbf H_G\rvert/J$); $\tfrac{MR^2}{2}\tfrac{d}{dt}(\dot\theta\sin\varphi + \dot\phi_{1,2}) = \pm\tau_1$; $2\dot\theta\sin\varphi + \dot\phi_1 + \dot\phi_2 = 2\Omega$; 19 unknowns, 18 equations: one motor law free |
| (g) Axle loads on the wheels | $\mathbf F_1 = -\mathbf F_2 = \tfrac{ML}{2}[-(\dot\varphi^2 + \dot\theta^2\cos^2\varphi)\,\mathbf i_b + (\ddot\theta\cos\varphi - 2\dot\theta\dot\varphi\sin\varphi)\,\mathbf j_b + (\ddot\varphi + \dot\theta^2\sin\varphi\cos\varphi)\,\mathbf k_b]$; $\mathbf Q_i = \tfrac{MR^2}{2}\tfrac{d}{dt}(\dot\theta\sin\varphi + \dot\phi_i)\,\mathbf i_b + \tfrac{MR^2}{4}(-\ddot\varphi + \dot\theta^2\sin\varphi\cos\varphi + 2\dot\theta\cos\varphi\,\dot\phi_i)\,\mathbf j_b + \tfrac{MR^2}{4}(\ddot\theta\cos\varphi + 2\dot\varphi\dot\phi_i)\,\mathbf k_b$; on the rod, the opposites |
| Initial rates (from the data) | $\dot\theta(0) = \Omega/\sqrt2$, $\dot\varphi(0) = -\Omega/\sqrt2$ |
| Value of the conserved angular momentum | $\mathbf H_G = \tfrac{\sqrt2 M\Omega}{8}[(3R^2 - 2L^2)\,\mathbf i_0 + 2(2L^2 + R^2)\,\mathbf j_0 + (2L^2 + 5R^2)\,\mathbf k_0]$ |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the results are checked with a second route and limiting cases.

> [!derivation] Check: total angular momentum with the wheels locked
> **Law:** angular momentum of one rigid body about its centre of mass, with the tensor of the assembly
> **Source:** Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 10.48
>
> With the wheel rates zero the assembly is one rigid body turning with the spacecraft; its tensor at $G$ is the rod tensor plus the two wheel tensors plus their Steiner terms (Center of Mass and Inertia Tensor).
>
> $$\begin{aligned}
> \bar{\bar I}{}^S_G &= \mathrm{diag}\left(MR^2,\ \frac{ML^2}{2} + \frac{ML^2}{2} + \frac{MR^2}{2},\ ML^2 + \frac{MR^2}{2}\right) \quad &\text{(sum of the boxed tensors)} \\
> \bar{\bar I}{}^S_G\cdot\boldsymbol\omega_{b0} &= MR^2\dot\theta\sin\varphi\,\mathbf i_b + \left(ML^2 + \frac{MR^2}{2}\right)\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right) \quad &\text{(matrix product)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G\big|_{\text{locked}} = MR^2\dot\theta\sin\varphi\,\mathbf i_b + \left(ML^2 + \frac{MR^2}{2}\right)\left(-\dot\varphi\,\mathbf j_b + \dot\theta\cos\varphi\,\mathbf k_b\right)}$$
>
> **Units:** kg m$^2$/s
> **Meaning:** the same as the total of the momentum section with the wheel rates set to zero: the change of pole and the Steiner route agree.

**Limiting cases and consistency:**

* **Rod at rest in attitude.** With the rates of $\theta$ and $\varphi$ zero, the wheel centres move with $G$ and each wheel's angular momentum is only its axial spin term, along the rod.
* **Point wheels.** With $R$ tending to zero the wheels hold no angular momentum about their centres and only their positions count: the transverse moment of the assembly tends to $ML^2$.
* **Horizontal rod.** With $\varphi$ zero the rod is horizontal, $\mathbf k_b$ is vertical and the azimuth rate appears only in the $\mathbf k_b$ component, as a rotation about the vertical should.
* **Orthonormality.** The matrix $[{}_0R_b]$ is the product of two rotations, each checked above, so its determinant is one and its transpose is its inverse.
* **Dimensions.** Every angular velocity component is a rate; every velocity term is a length times a rate; every angular momentum term is a mass times a squared length times a rate.

---

---

## Problem RB-26: Unbalanced planetary bearings

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** four rigid bodies moving in the vertical plane $Oxy$. The disk $D$, homogeneous, of radius $d$ and mass $2m$; the three bearings $A$, $B$, $C$, homogeneous cylinders of radius $d/4$ and mass $m$ each (each body is named after its centre). The cavity is a fixed circle of radius $3d/2$ (read from the figure: the gap between the disk and the cavity is one bearing diameter, so the cavity radius is the sum of $d$ and twice $d/4$). Every contact disk-bearing and bearing-cavity rolls without slipping.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$ attached to the cavity, $O$ its centre, $\mathbf i$ along $Ox$ (to the right), $\mathbf j$ along $Oy$ (up), $\mathbf k$ out of the paper (⊙). Gravity is $-g\,\mathbf j$.
* **Angles:** $\theta$, angle of $\overrightarrow{OA}$ measured from $Ox$, counterclockwise about $\mathbf k$ (read from the arc of the figure). The two $45^\circ$ arcs of the figure are read as: $\overrightarrow{OB}$ and $\overrightarrow{OC}$ lie $45^\circ$ on either side of the prolongation of $\overrightarrow{AO}$ beyond $O$, so the polar angles of $B$ and $C$ are $\theta + 3\pi/4$ and $\theta + 5\pi/4$. Exchanging the labels $B$ and $C$ would change nothing below, since only the sum of their unit vectors enters.
* **Auxiliary bases:** for each bearing, the polar basis $\{\mathbf e_r(\alpha), \mathbf e_\theta(\alpha), \mathbf k\}$ attached to its centre line, with $\alpha$ the polar angle of that bearing.
* **Spin angles:** $\varphi_D$ for the disk and $\varphi_A$, $\varphi_B$, $\varphi_C$ for the bearings, all measured counterclockwise about $\mathbf k$, with rates $\omega_D$, $\omega_A$, $\omega_B$, $\omega_C$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Radius of the disk | $d$ | m |
| Mass of the disk | $2m$ | kg |
| Radius of each bearing | $d/4$ | m |
| Mass of each bearing | $m$ | kg |
| Radius of the cavity (read from the figure) | $3d/2$ | m |
| Gravity | $-g\,\mathbf j$ | m/s$^2$ |
| Initial state | $\theta_0 = 0$, everything at rest | rad, - |

#### Part (a): degrees of freedom

> [!derivation] Part (a): count of the degrees of freedom
> **Law:** three coordinates per body in planar motion; no-penetration and no-slip conditions at each contact
> **Source:** Notes.pdf, Sec. 13.1; Notes.pdf, Eq. 13.1; Notes.pdf, Eq. 13.2; Notes.pdf, Sec. 13.4
>
> Position constraints first. The centre of a bearing touching the cavity lies at the distance from $O$ equal to the cavity radius minus the bearing radius; touching the disk, it lies at the distance from the disk centre $O'$ equal to the disk radius plus the bearing radius. The three centres are on a circle about $O$ and on a circle about $O'$ of the same radius; a circle through three points that do not lie on one line is unique, so $O'$ coincides with $O$ (the three bearings are not on one line: their polar angles differ by $3\pi/4$, $\pi/2$ and $3\pi/4$).
>
> $$\begin{aligned}
> |\overrightarrow{OA}| &= \frac{3d}{2} - \frac d4 = \frac{5d}{4}, \qquad |\overrightarrow{O'A}| = d + \frac d4 = \frac{5d}{4} \quad &\text{(contact of $A$ with the cavity and with the disk)} \\
> O' &\equiv O \quad &\text{(three such points fix the centre of the circle)} \\
> n_{\mathrm{planar}} &= 12 \quad &\text{(disk and three bearings, three planar coordinates each)} \\
> n_{\mathrm{no\text{-}penetration}} &= 6 - 1 = 5 \quad &\text{(six contact conditions, but the centre of the circle through three points needs only two equations for the two coordinates of $O'$, so one condition repeats the others)} \\
> n_q &= \underbrace{1}_{\varphi_D} + \underbrace{3}_{\theta_A, \theta_B, \theta_C} + \underbrace{3}_{\varphi_A, \varphi_B, \varphi_C} = 12 - 5 = 7 \quad &\text{(coordinates left after the position constraints)} \\
> n_{\mathrm{dof}} &= 7 - 3\cdot 2 = 1 \quad &\text{(two independent no-slip conditions per bearing, Eq. 13.2)}
> \end{aligned}$$
>
> $$\boxed{n_{\mathrm{dof}} = 1, \qquad \text{coordinate: } \theta}$$
>
> **Units:** dimensionless counts
> **Meaning:** the whole train moves as one mechanism: the next box shows that the four rates are fixed multiples of the rate of $\theta$, and that the three bearings keep their angular spacing, so $\theta$ alone gives the configuration.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb26-polar-basis.svg]]

> [!derivation] Polar basis of a bearing: rotation by alpha about k
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the plane $Oxy$ with $\mathbf k$ out of the paper (⊙): a positive $\alpha$ turns counterclockwise. $\mathbf e_r$ is $\mathbf i$ turned by $\alpha$: hypotenuse 1, adjacent leg along $\mathbf i$ (cosine of $\alpha$), opposite leg along $\mathbf j$ (sine). $\mathbf e_\theta$ is $\mathbf j$ turned by $\alpha$: adjacent leg along $\mathbf j$ (cosine); the counterclockwise turn carries the tip of $\mathbf j$ to the left, towards minus $\mathbf i$, which is the minus sign of the opposite leg (sine). For the bearing $A$ the angle is $\theta$; for $B$ and $C$ it is $\theta$ plus a constant, and its rate is the rate of $\theta$ as soon as the constant spacing of the bearings is shown in the box of part (b) below.
>
> $$\begin{aligned}
> \mathbf e_r(\alpha) &= \cos\alpha\,\mathbf i + \sin\alpha\,\mathbf j, \qquad \mathbf e_\theta(\alpha) = -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_\alpha] &= \begin{bmatrix} \cos\alpha & -\sin\alpha & 0 \cr \sin\alpha & \cos\alpha & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_\alpha] &= 1\cdot\left(\cos^2\alpha + \sin^2\alpha\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_\alpha][{}_0R_\alpha]^T &= \begin{bmatrix} \cos^2\alpha + \sin^2\alpha & \cos\alpha\sin\alpha - \sin\alpha\cos\alpha & 0 \cr \sin\alpha\cos\alpha - \cos\alpha\sin\alpha & \sin^2\alpha + \cos^2\alpha & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \dot{\mathbf e}_r &= \dot\theta\,\mathbf k\times\mathbf e_r = \dot\theta\,\mathbf e_\theta, \qquad \dot{\mathbf e}_\theta = \dot\theta\,\mathbf k\times\mathbf e_\theta = -\dot\theta\,\mathbf e_r \quad &\text{(Poisson; rate of $\alpha$ equal to the rate of $\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_r(\alpha) = \cos\alpha\,\mathbf i + \sin\alpha\,\mathbf j, \quad \mathbf e_\theta(\alpha) = -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf j, \quad \dot{\mathbf e}_r = \dot\theta\,\mathbf e_\theta, \quad \dot{\mathbf e}_\theta = -\dot\theta\,\mathbf e_r}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$ in the derivatives
> **Meaning:** $\mathbf e_r$ points from $O$ to the centre of the bearing and $\mathbf e_\theta$ along its direction of travel for a growing $\theta$.

![[attachments/EM-SOL/rb26-rolling.svg]]

> [!derivation] Part (b): rolling of a bearing on the cavity and on the disk
> **Law:** velocity field of a rigid body; rolling without slipping on a fixed body and between two moving bodies
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.2; Notes.pdf, Eq. 13.5; [Lecture 10, Slide 11]
>
> Take the bearing $A$, of polar angle $\theta$, centre at the distance $5d/4$ from $O$. Its contact $Q_A$ with the cavity is at the distance $3d/2$ from $O$ (outer side, a bearing radius further along $\mathbf e_r$), and its contact $P_A$ with the disk is at the distance $d$ (inner side, a bearing radius back along $\mathbf e_r$). The cavity is at rest; the disk turns about the fixed point $O$.
>
> $$\begin{aligned}
> \mathbf r_0^A &= \frac{5d}{4}\,\mathbf e_r \quad &\text{(position of the centre)} \\
> \mathbf v_0^A &= \frac{5d}{4}\,\dot{\mathbf e}_r = \frac{5d}{4}\,\dot\theta\,\mathbf e_\theta \quad &\text{(derivative; $d$ constant; Poisson)} \\
> \mathbf v_0^{Q_A(A)} &= \mathbf v_0^A + \omega_A\,\mathbf k\times\frac d4\,\mathbf e_r = \left(\frac{5d}{4}\dot\theta + \frac d4\,\omega_A\right)\mathbf e_\theta \quad &\text{(Eq. 9.3 from $A$ to $Q_A$; $\mathbf k\times\mathbf e_r = \mathbf e_\theta$)} \\
> \frac{5d}{4}\dot\theta + \frac d4\,\omega_A &= 0 \;\Rightarrow\; \omega_A = -5\dot\theta \quad &\text{(Eq. 13.5: no slip on the fixed cavity)} \\
> \mathbf v_0^{P_A(A)} &= \mathbf v_0^A + \omega_A\,\mathbf k\times\left(-\frac d4\,\mathbf e_r\right) = \left(\frac{5d}{4}\dot\theta + \frac{5d}{4}\dot\theta\right)\mathbf e_\theta = \frac{5d}{2}\,\dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 9.3 from $A$ to $P_A$; value of $\omega_A$)} \\
> \mathbf v_0^{P_A(D)} &= \omega_D\,\mathbf k\times d\,\mathbf e_r = d\,\omega_D\,\mathbf e_\theta \quad &\text{(Eq. 9.3 from the fixed point $O$ of the disk)} \\
> d\,\omega_D &= \frac{5d}{2}\,\dot\theta \;\Rightarrow\; \omega_D = \frac52\,\dot\theta \quad &\text{(Eq. 13.2: equal velocities at $P_A$)}
> \end{aligned}$$
>
> $$\boxed{\omega_A = -5\dot\theta, \qquad \omega_D = \frac52\,\dot\theta, \qquad \mathbf v_0^A = \frac{5d}{4}\,\dot\theta\,\mathbf e_\theta(\theta)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-1}}]$
> **Meaning:** for a growing $\theta$ the bearing spins clockwise (negative rate) five times faster than its centre goes round, and the disk turns counterclockwise two and a half times faster than the centre of the bearing.

> [!derivation] Part (b): the other two bearings keep their spacing
> **Law:** the same two no-slip conditions for $B$ and $C$; integration of equal rates; Barrow's rule
> **Source:** Notes.pdf, Eq. 13.2; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 9.3
>
> Repeat the previous box for $B$ with its own polar angle $\theta_B$ in place of $\theta$: the cavity contact gives a bearing rate equal to minus five times the rate of $\theta_B$, and the disk contact gives the disk rate equal to five halves of the rate of $\theta_B$. The disk is one body, so its rate is the same in both results.
>
> $$\begin{aligned}
> \omega_D &= \frac52\,\dot\theta_B = \frac52\,\dot\theta \;\Rightarrow\; \dot\theta_B = \dot\theta \quad &\text{(disk rate from the contact with $B$ and with $A$)} \\
> \int_0^t\left(\dot\theta_B - \dot\theta\right)dt' &= \left[\theta_B - \theta\right]_0^t = 0 \;\Rightarrow\; \theta_B - \theta = \theta_B(0) - \theta_0 = \frac{3\pi}{4} \quad &\text{(antiderivative; Barrow's rule; initial spacing)} \\
> \theta_C - \theta &= \frac{5\pi}{4}, \qquad \omega_B = \omega_C = -5\dot\theta \quad &\text{(same steps for $C$)} \\
> \mathbf v_0^B &= \frac{5d}{4}\,\dot\theta\,\mathbf e_\theta\!\left(\theta + \frac{3\pi}{4}\right), \qquad \mathbf v_0^C = \frac{5d}{4}\,\dot\theta\,\mathbf e_\theta\!\left(\theta + \frac{5\pi}{4}\right) \quad &\text{(previous box with the angles of $B$ and $C$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf v_0^A = \tfrac{5d}{4}\dot\theta\left(-\sin\theta\,\mathbf i + \cos\theta\,\mathbf j\right), \quad \mathbf v_0^B = \tfrac{5d}{4}\dot\theta\left[-\sin\!\left(\theta + \tfrac{3\pi}{4}\right)\mathbf i + \cos\!\left(\theta + \tfrac{3\pi}{4}\right)\mathbf j\right], \quad \mathbf v_0^C = \tfrac{5d}{4}\dot\theta\left[-\sin\!\left(\theta + \tfrac{5\pi}{4}\right)\mathbf i + \cos\!\left(\theta + \tfrac{5\pi}{4}\right)\mathbf j\right] \\ \boldsymbol\omega_{D0} = \tfrac52\,\dot\theta\,\mathbf k, \qquad \boldsymbol\omega_{A0} = \boldsymbol\omega_{B0} = \boldsymbol\omega_{C0} = -5\dot\theta\,\mathbf k \end{gathered}}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm{T^{-1}}]$
> **Meaning:** the three bearings travel round together like the planets of a planetary gear whose carrier would turn with the rate of $\theta$; the cavity is the fixed ring and the disk the sun. The spacing of the figure is kept for ever.

### Center of Mass and Inertia Tensor

> [!derivation] Moment of inertia of a homogeneous cylinder about its axis
> **Law:** moment of inertia as the integral of the squared distance to the axis, in polar coordinates (jacobian $\rho$); centre of mass of a symmetric body
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.6; [Lecture 8, Slide 10]
>
> A homogeneous cylinder (or disk) of mass $M$, radius $a$ and length $\ell$ has density $\rho_m$ equal to $M/(\pi a^2\ell)$. With polar coordinates $\rho$ from 0 to $a$ and $\chi$ from 0 to $2\pi$ in the cross section, and the axial coordinate $\zeta$ from 0 to $\ell$, the element of mass is $\rho_m\,\rho\,d\rho\,d\chi\,d\zeta$ and its distance to the axis is $\rho$.
>
> $$\begin{aligned}
> I_{zz} &= \rho_m\int_0^{\ell}\!\!\int_0^{2\pi}\!\!\int_0^{a}\rho^2\,\rho\,d\rho\,d\chi\,d\zeta = \rho_m\left[\zeta\right]_0^{\ell}\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^{a} \quad &\text{(separable integrand; antiderivatives)} \\
> &= \rho_m\,\ell\cdot 2\pi\cdot\left(\frac{a^4}{4} - 0\right) = \frac{M}{\pi a^2\ell}\cdot\frac{\pi a^4\ell}{2} = \frac{M a^2}{2} \quad &\text{(Barrow's rule; value of $\rho_m$)} \\
> \int\rho\cos\chi\,dm &= \rho_m\,\ell\left[\frac{\rho^3}{3}\right]_0^{a}\left[\sin\chi\right]_0^{2\pi} = 0 \quad &\text{(first moment along $\mathbf i$: centre of mass on the axis; same with the sine)} \\
> I_D &= \frac{2m\,d^2}{2} = m d^2, \qquad I_b = \frac{m}{2}\left(\frac d4\right)^2 = \frac{m d^2}{32} \quad &\text{(disk: $M$ is $2m$, $a$ is $d$; bearing: $M$ is $m$, $a$ is $d/4$)}
> \end{aligned}$$
>
> $$\boxed{I_D = m d^2 \ \text{(disk about } O\text{)}, \qquad I_b = \frac{m d^2}{32} \ \text{(each bearing about its centre)}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** only the moment about the axis $\mathbf k$ enters a planar motion; the centre of mass of each body is its geometric centre.

> [!derivation] Part (c): centre of mass of the system
> **Law:** centre of mass of a system of bodies
> **Source:** Notes.pdf, Eq. 13.11; Notes.pdf, Eq. 10.6
>
> The disk centre is $O$; the bearing centres are at the distance $5d/4$ along their own radial unit vectors. The two unit vectors of $B$ and $C$ make the angles $\pm\pi/4$ with the prolongation of $\overrightarrow{AO}$, that is with minus $\mathbf e_r(\theta)$; their components normal to it cancel and their components along it add (adjacent leg of each triangle: cosine of $\pi/4$).
>
> $$\begin{aligned}
> 5m\,\mathbf r_0^G &= 2m\,\mathbf 0 + m\,\frac{5d}{4}\left[\mathbf e_r(\theta) + \mathbf e_r\!\left(\theta + \frac{3\pi}{4}\right) + \mathbf e_r\!\left(\theta + \frac{5\pi}{4}\right)\right] \quad &\text{(Eq. 13.11; total mass $5m$)} \\
> \mathbf e_r\!\left(\theta + \frac{3\pi}{4}\right) + \mathbf e_r\!\left(\theta + \frac{5\pi}{4}\right) &= 2\cos\frac{\pi}{4}\left(-\mathbf e_r(\theta)\right) = -\sqrt2\,\mathbf e_r(\theta) \quad &\text{(sum of the two adjacent legs along minus $\mathbf e_r$)} \\
> \mathbf r_0^G &= \frac{d}{4}\left(1 - \sqrt2\right)\mathbf e_r(\theta) \quad &\text{(divide by $5m$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = -\frac{\left(\sqrt2 - 1\right)d}{4}\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right)}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** the system is unbalanced: $G$ is not at $O$ but on the line $AO$, beyond $O$ on the side opposite to $A$, at a distance of about 0.104 times $d$ (the product of 0.25 and 0.4142). This offset is what makes gravity drive the train.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (d): kinetic energy of each body
> **Law:** kinetic energy about a fixed body point (disk); Koenig's theorem about the centre of mass (bearings)
> **Source:** Notes.pdf, Eq. 11.32; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 9]
>
> $$\begin{aligned}
> T^D &= \frac12\,I_D\,\omega_D^2 = \frac12\,m d^2\left(\frac52\,\dot\theta\right)^2 = \frac{25}{8}\,m d^2\dot\theta^2 \quad &\text{(Eq. 11.32; $O$ is a fixed point of the disk)} \\
> T^A &= \frac12\,m\left(v_0^A\right)^2 + \frac12\,I_b\,\omega_A^2 = \frac12\,m\,\frac{25 d^2}{16}\dot\theta^2 + \frac12\,\frac{m d^2}{32}\,25\dot\theta^2 \quad &\text{(Eq. 11.31, Koenig)} \\
> &= \frac{50}{64}\,m d^2\dot\theta^2 + \frac{25}{64}\,m d^2\dot\theta^2 = \frac{75}{64}\,m d^2\dot\theta^2 \quad &\text{(common denominator)} \\
> T^B &= T^C = \frac{75}{64}\,m d^2\dot\theta^2 \quad &\text{(same speed of the centre and same spin rate)} \\
> T &= \frac{200}{64}\,m d^2\dot\theta^2 + 3\cdot\frac{75}{64}\,m d^2\dot\theta^2 = \frac{425}{64}\,m d^2\dot\theta^2 \quad &\text{(sum of the four bodies)}
> \end{aligned}$$
>
> $$\boxed{T^D = \frac{25}{8}\,m d^2\dot\theta^2, \qquad T^A = T^B = T^C = \frac{75}{64}\,m d^2\dot\theta^2, \qquad T = \frac{425}{64}\,m d^2\dot\theta^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, J in every term
> **Meaning:** the disk carries 200 of the 425 parts of the kinetic energy (47.1 %, the ratio 200/425), because it is the heaviest body and spins fastest; in each bearing two thirds of the energy is translation (50 of 75 parts) and one third spin.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb26-exploded.svg]]

The exploded view separates the disk from the three bearings and the bearings from the cavity. At the contact of bearing $i$ with the cavity (point $Q_i$) the cavity pushes the bearing with a normal force $N_i^c$ along minus $\mathbf e_r$ and a friction force $F_i^c$ along $\mathbf e_\theta$; at the contact with the disk (point $P_i$) the disk pushes the bearing with $N_i^d$ along $\mathbf e_r$ and $F_i^d$ along $\mathbf e_\theta$, and the bearing pushes the disk with the opposite pair (third law of Newton). The friction forces are unknowns (no slip: they are not given by Coulomb's law); the signs are those of the components, to be found.

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the disk | $D$ | $O$ | $-2mg\,\mathbf j$ | applied |
| Contact of bearing $i$ on the disk | $D$ | $P_i$ | $-N_i^d\,\mathbf e_r(\theta_i) - F_i^d\,\mathbf e_\theta(\theta_i)$ | constraint (pair) |
| Weight of bearing $i$ | $i$ | $i$ | $-mg\,\mathbf j$ | applied |
| Cavity on bearing $i$ | $i$ | $Q_i$ | $-N_i^c\,\mathbf e_r(\theta_i) + F_i^c\,\mathbf e_\theta(\theta_i)$ | constraint |
| Disk on bearing $i$ | $i$ | $P_i$ | $N_i^d\,\mathbf e_r(\theta_i) + F_i^d\,\mathbf e_\theta(\theta_i)$ | constraint (pair) |

Here $\theta_i$ is $\theta$, $\theta + 3\pi/4$ or $\theta + 5\pi/4$ for $A$, $B$, $C$.

> [!derivation] Equations of bearing i (force along e_theta, and moment about its centre)
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9; [Lecture 10, Slide 5]
>
> The pole of the moment equation is the centre of mass of the bearing, so the term in the velocity of the pole vanishes (the velocity of the centre crossed with the momentum, which is parallel to it). The normal forces and the weight pass through the centre. The second derivative of the velocity of the centre follows from the Poisson relations of the polar basis.
>
> $$\begin{aligned}
> \mathbf a_0^i &= \frac{5d}{4}\left(\ddot\theta\,\mathbf e_\theta + \dot\theta\,\dot{\mathbf e}_\theta\right) = \frac{5d}{4}\,\ddot\theta\,\mathbf e_\theta - \frac{5d}{4}\,\dot\theta^2\,\mathbf e_r \quad &\text{(product rule; Poisson)} \\
> -mg\,\mathbf j\cdot\mathbf e_\theta(\theta_i) &= -mg\cos\theta_i \quad &\text{(second component of $\mathbf e_\theta$)} \\
> m\,\frac{5d}{4}\,\ddot\theta &= F_i^c + F_i^d - mg\cos\theta_i \quad &\text{(Eq. 12.8 along $\mathbf e_\theta$)} \\
> -m\,\frac{5d}{4}\,\dot\theta^2 &= N_i^d - N_i^c - mg\sin\theta_i \quad &\text{(Eq. 12.8 along $\mathbf e_r$; $-mg\,\mathbf j\cdot\mathbf e_r$ is $-mg\sin\theta_i$)} \\
> \frac d4\,\mathbf e_r\times F_i^c\,\mathbf e_\theta + \left(-\frac d4\,\mathbf e_r\right)\times F_i^d\,\mathbf e_\theta &= \frac d4\left(F_i^c - F_i^d\right)\mathbf k \quad &\text{(moments about the centre; $\mathbf e_r\times\mathbf e_\theta = \mathbf k$)} \\
> I_b\,\dot\omega_i &= \frac{m d^2}{32}\left(-5\ddot\theta\right) = \frac d4\left(F_i^c - F_i^d\right) \quad &\text{(Eq. 12.13 along $\mathbf k$; derivative of the spin rate)}
> \end{aligned}$$
>
> $$\boxed{F_i^c + F_i^d = \frac54\,m d\,\ddot\theta + mg\cos\theta_i, \qquad F_i^c - F_i^d = -\frac58\,m d\,\ddot\theta, \qquad N_i^d - N_i^c = mg\sin\theta_i - \frac54\,m d\,\dot\theta^2}$$
>
> **Units:** N in every term
> **Meaning:** three equations per bearing; the third is the radial component of Eq. 12.8, with the weight component along $\mathbf e_r$ equal to minus $mg$ times the sine of the polar angle. The friction forces are fixed by the tangential and moment equations; the radial equation fixes only the difference of the two normal forces.

> [!derivation] Equations of the disk (moment about the fixed point O, and force)
> **Law:** moment equation about a fixed point; Newton's second law; third law of Newton for the contact pairs
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.10
>
> $O$ is a fixed point of the disk and its centre of mass, so the pole term vanishes and the acceleration of the centre of mass is zero. The disk receives minus the contact pair of each bearing at the point $P_i$, at the distance $d$ along $\mathbf e_r(\theta_i)$.
>
> $$\begin{aligned}
> \sum_i d\,\mathbf e_r\times\left(-N_i^d\,\mathbf e_r - F_i^d\,\mathbf e_\theta\right) &= -d\sum_i F_i^d\,\mathbf k \quad &\text{(moment of the three pairs about $O$)} \\
> I_D\,\dot\omega_D &= m d^2\,\frac52\,\ddot\theta = -d\sum_i F_i^d \quad &\text{(Eq. 12.13 along $\mathbf k$)} \\
> \mathbf 0 &= -2mg\,\mathbf j - \sum_i\left(N_i^d\,\mathbf e_r(\theta_i) + F_i^d\,\mathbf e_\theta(\theta_i)\right) \quad &\text{(Eq. 12.8; $O$ at rest)}
> \end{aligned}$$
>
> $$\boxed{\sum_i F_i^d = -\frac52\,m d\,\ddot\theta, \qquad \sum_i\left(N_i^d\,\mathbf e_r(\theta_i) + F_i^d\,\mathbf e_\theta(\theta_i)\right) = -2mg\,\mathbf j}$$
>
> **Units:** N in every term
> **Meaning:** three equations of the disk. With the nine of the bearings: twelve equations for thirteen unknowns (the second rate of $\theta$, six friction forces, six normal forces). One unknown stays free, as shown in the next box.

> [!derivation] Equation of motion of the system
> **Law:** elimination of the contact forces among the twelve equations
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 12.13
>
> Sum the boxed tangential equations of the three bearings and their moment equations; the sum of the cosines uses the same two adjacent legs as the centre of mass box.
>
> $$\begin{aligned}
> \sum_i\cos\theta_i &= \cos\theta + \cos\!\left(\theta + \frac{3\pi}{4}\right) + \cos\!\left(\theta + \frac{5\pi}{4}\right) = \left(1 - \sqrt2\right)\cos\theta \quad &\text{(first components of the three $\mathbf e_r$)} \\
> \sum_i F_i^c &= \sum_i F_i^d - \frac{15}{8}\,m d\,\ddot\theta \quad &\text{(sum of the three moment equations)} \\
> \sum_i\left(F_i^c + F_i^d\right) &= 2\sum_i F_i^d - \frac{15}{8}\,m d\,\ddot\theta = -5\,m d\,\ddot\theta - \frac{15}{8}\,m d\,\ddot\theta = -\frac{55}{8}\,m d\,\ddot\theta \quad &\text{(disk moment equation)} \\
> \frac{15}{4}\,m d\,\ddot\theta &= -\frac{55}{8}\,m d\,\ddot\theta + \left(\sqrt2 - 1\right)mg\cos\theta \quad &\text{(sum of the tangential equations)} \\
> \frac{85}{8}\,m d\,\ddot\theta &= \left(\sqrt2 - 1\right)mg\cos\theta \quad &\text{(collect: 30/8 plus 55/8)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = \frac{8\left(\sqrt2 - 1\right)}{85}\,\frac gd\,\cos\theta}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]/[\mathrm L] = [\mathrm{T^{-2}}]$
> **Meaning:** with the second rate known, the tangential and moment equations of each bearing give its two friction forces, and the disk moment equation is then satisfied. The normal forces enter only the three radial equations and the two force equations of the disk: five equations for six normal forces, so one of them (a preload with which the bearings are squeezed between disk and cavity, shared among the three bearings in the ratio root two to one to one) stays free. This matches the count of part (a), where one of the six no-penetration conditions repeated the others.

> [!derivation] Part (e): reduction to quadratures
> **Law:** first integral by multiplying by the rate (chain rule); separation of variables; Barrow's rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 12.30
>
> Write $\kappa$ for the positive constant $8(\sqrt2 - 1)/85$. The initial values are zero for $\theta$ and for its rate.
>
> $$\begin{aligned}
> \ddot\theta\,\dot\theta &= \kappa\,\frac gd\,\cos\theta\,\dot\theta \quad &\text{(multiply the equation of motion by the rate)} \\
> \frac{d}{dt}\left(\frac12\,\dot\theta^2\right) &= \frac{d}{dt}\left(\kappa\,\frac gd\,\sin\theta\right) \quad &\text{(equal rates of the two sides)} \\
> \dot\theta\,\ddot\theta &= \kappa\,\frac gd\cos\theta\,\dot\theta \quad &\text{(chain rule: $d(\dot\theta^2/2)/dt = \dot\theta\ddot\theta$ and $d(\sin\theta)/dt = \cos\theta\,\dot\theta$)} \\
> \left[\frac12\,\dot\theta^2 - \kappa\,\frac gd\,\sin\theta\right]_0^t &= 0 \;\Rightarrow\; \frac12\,\dot\theta^2 - \kappa\,\frac gd\,\sin\theta = \frac12\cdot 0^2 - \kappa\,\frac gd\,\sin 0 = 0 \quad &\text{(integrate from 0 to $t$; Barrow's rule; initial rest)} \\
> \frac{425}{64}\,m d^2\dot\theta^2 &= \frac{425}{64}\,m d^2\cdot 2\kappa\,\frac gd\,\sin\theta = \frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\,\sin\theta \quad &\text{(multiply by twice the coefficient of $T$; 425 times 16 over 64 times 85 is 5/4)} \\
> \frac{d\theta}{dt} &= \sqrt{2\kappa\,\frac gd\,\sin\theta} \quad &\text{(positive root: the initial second rate is positive)} \\
> t &= \int_0^{\theta}\frac{d\theta'}{\sqrt{2\kappa\,(g/d)\,\sin\theta'}} \quad &\text{(separate the variables and integrate)}
> \end{aligned}$$
>
> $$\boxed{\frac{425}{64}\,m d^2\dot\theta^2 - \frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\,\sin\theta = 0, \qquad t = \sqrt{\frac{85\,d}{16\left(\sqrt2 - 1\right)g}}\int_0^{\theta}\frac{d\theta'}{\sqrt{\sin\theta'}}}$$
>
> **Units:** J in the first equation; $\sqrt{[\mathrm L]/[\mathrm{L\,T^{-2}}]} = [\mathrm T]$ in the second
> **Meaning:** the first equation is the kinetic energy of part (d) equal to the drop of potential energy of $G$; at the start the rate is zero and the second rate is positive (cosine of zero is 1), so $\theta$ grows. The rate vanishes again where the sine vanishes, at $\theta$ equal to $\pi$: the train swings between 0 and $\pi$. The integrand behaves as the inverse square root of $\theta$ near 0, which is integrable, so the time to leave the start is finite.

#### Equilibrium and small oscillations

> [!derivation] Part (f): equilibrium positions and stability
> **Law:** equilibrium: zero second rate with zero rate; stability from the sign of the restoring term
> **Source:** Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 12.34
>
> At rest the equation of motion requires the right-hand side to vanish. Write a position near an equilibrium $\theta_e$ as $\theta_e$ plus a small $\delta$ and expand the cosine to first order.
>
> $$\begin{aligned}
> \cos\theta_e &= 0 \;\Rightarrow\; \theta_e = \frac{\pi}{2} \ \text{or} \ \theta_e = -\frac{\pi}{2} \quad &\text{(zero second rate at rest)} \\
> \cos\left(\theta_e + \delta\right) &= \cos\theta_e\cos\delta - \sin\theta_e\sin\delta \approx -\sin\theta_e\,\delta \quad &\text{(addition formula; first order in $\delta$)} \\
> \ddot\delta &= -\kappa\,\frac gd\,\sin\theta_e\,\delta \quad &\text{(linearized equation of motion)} \\
> V &= 5mg\,\mathbf j\cdot\mathbf r_0^G = -\frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\,\sin\theta \quad &\text{(Eq. 12.34 with the centre of mass of part (c))}
> \end{aligned}$$
>
> $$\boxed{\theta_e = \frac{\pi}{2}\ \text{(stable)}, \qquad \theta_e = -\frac{\pi}{2}\ \text{(unstable)}}$$
>
> **Units:** rad; $[\mathrm{T^{-2}}]$ in the linearized coefficient; J in $V$
> **Meaning:** at $\theta$ equal to $\pi/2$ the sine is 1 and the linearized equation is a harmonic oscillator (restoring term); at minus $\pi/2$ the sine is minus 1 and the deviation grows exponentially. Equivalently, $G$ (opposite to $A$) is at its lowest point when $A$ is at the top, where the potential has its minimum, and at its highest when $A$ is at the bottom.

> [!derivation] Part (g): angular frequency of the small oscillations
> **Law:** harmonic oscillator
> **Source:** Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 5.6
>
> $$\begin{aligned}
> \ddot\delta + \kappa\,\frac gd\,\delta &= 0 \quad &\text{(previous box with the sine of $\pi/2$ equal to 1)} \\
> \omega_0^2 &= \kappa\,\frac gd = \frac{8\left(\sqrt2 - 1\right)}{85}\,\frac gd \quad &\text{(coefficient of the harmonic oscillator)}
> \end{aligned}$$
>
> $$\boxed{\omega_0 = \sqrt{\frac{8\left(\sqrt2 - 1\right)g}{85\,d}} \approx 0.197\sqrt{\frac gd}}$$
>
> **Units:** $\sqrt{[\mathrm{L\,T^{-2}}]/[\mathrm L]} = [\mathrm{T^{-1}}]$, rad/s
> **Meaning:** the number is the square root of 8 times 0.41421 over 85 (0.038984), that is 0.1974. The train oscillates slowly because the restoring moment comes from a small offset of $G$ while the inertia is that of the whole train with its fast spins.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom | One; coordinate $\theta$ (the disk centre stays at $O$, and six rolling contacts tie the four rates to $\dot\theta$) |
| (b) Velocities and angular velocities | $\mathbf v_0^A = \tfrac{5d}{4}\dot\theta\,\mathbf e_\theta(\theta)$, $\mathbf v_0^B = \tfrac{5d}{4}\dot\theta\,\mathbf e_\theta(\theta + 3\pi/4)$, $\mathbf v_0^C = \tfrac{5d}{4}\dot\theta\,\mathbf e_\theta(\theta + 5\pi/4)$ with $\mathbf e_\theta(\alpha) = -\sin\alpha\,\mathbf i + \cos\alpha\,\mathbf j$; $\boldsymbol\omega_{D0} = \tfrac52\dot\theta\,\mathbf k$; $\boldsymbol\omega_{A0} = \boldsymbol\omega_{B0} = \boldsymbol\omega_{C0} = -5\dot\theta\,\mathbf k$ |
| (c) Centre of mass | $\mathbf r_0^G = -\tfrac{(\sqrt2 - 1)d}{4}(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j)$ |
| (d) Kinetic energies | $T^D = \tfrac{25}{8}md^2\dot\theta^2$; $T^A = T^B = T^C = \tfrac{75}{64}md^2\dot\theta^2$; total $\tfrac{425}{64}md^2\dot\theta^2$ |
| (e) Quadratures | $\tfrac{425}{64}md^2\dot\theta^2 - \tfrac{5(\sqrt2 - 1)}{4}mgd\sin\theta = 0$; $t = \sqrt{\tfrac{85d}{16(\sqrt2 - 1)g}}\int_0^\theta d\theta'/\sqrt{\sin\theta'}$ |
| (f) Equilibria | $\theta = \pi/2$ stable; $\theta = -\pi/2$ unstable |
| (g) Small oscillations about $\theta = \pi/2$ | $\omega_0 = \sqrt{8(\sqrt2 - 1)g/(85d)} \approx 0.197\sqrt{g/d}$ |

> [!derivation] Check: the energy integral from the power of the loads
> **Law:** power of the contact forces under rolling without slipping; energy theorem; potential of the weights
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34
>
> Second route to the first boxed equation of part (e), without the twelve equations. At a cavity contact the force acts on a bearing point of zero velocity; at a disk contact the pair acts on two body points with the same velocity, so the powers on the bearing and on the disk cancel.
>
> $$\begin{aligned}
> \dot W^{c}_i &= \left(-N_i^c\,\mathbf e_r + F_i^c\,\mathbf e_\theta\right)\cdot\mathbf v_0^{Q_i(i)} = \left(-N_i^c\,\mathbf e_r + F_i^c\,\mathbf e_\theta\right)\cdot\mathbf 0 = 0 \quad &\text{(no slip on the cavity)} \\
> \dot W^{d}_i &= \left(N_i^d\,\mathbf e_r + F_i^d\,\mathbf e_\theta\right)\cdot\left(\mathbf v_0^{P_i(i)} - \mathbf v_0^{P_i(D)}\right) = 0 \quad &\text{(pair on the bearing and on the disk; equal velocities)} \\
> V &= 2mg\,\mathbf j\cdot\mathbf 0 + mg\,\mathbf j\cdot\left(\mathbf r_0^A + \mathbf r_0^B + \mathbf r_0^C\right) = 5mg\,\mathbf j\cdot\mathbf r_0^G = -\frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\,\sin\theta \quad &\text{(Eq. 12.34; part (c))} \\
> \left[T + V\right]_0^t &= 0 \;\Rightarrow\; \frac{425}{64}\,m d^2\dot\theta^2 - \frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\,\sin\theta = 0 + 0 \quad &\text{(Eq. 12.33 integrated; Barrow's rule; initial rest at zero angle)}
> \end{aligned}$$
>
> $$\boxed{\frac{425}{64}\,m d^2\dot\theta^2 + \frac{5\left(\sqrt2 - 1\right)}{4}\,m g d\left(1 - \sin\theta\right) = \frac{5\left(\sqrt2 - 1\right)}{4}\,m g d}$$
>
> **Units:** J in every term
> **Meaning:** the same integral as part (e), written with the constant on the right as in the key; the rolling contacts do no work, so the energy of the train is the kinetic energy of part (d) plus the potential of its unbalanced centre of mass.

**Check against the official key:** the key (Problems.pdf, pp. 80-81) prints the energy equation with the coefficient 425/64 for the kinetic energy and the potential term five times $mg$ times the factor of the square root of 2 minus 1 over 4 times $d$ times one minus the sine of $\theta$, equal to the same constant; the two equilibria at plus and minus $\pi/2$, the first one stable; and the angular frequency equal to the square root of $8g/(85d)$ times the square root of 2 minus 1. The boxes of parts (d), (e), (f) and (g) and the check box give the same expressions: **match**. The key prints no expressions for parts (a) to (c).

**Limiting cases and consistency:**

* **Balanced train.** If the three bearings were at $120^\circ$ from each other the sum of their unit vectors would vanish, $G$ would sit at $O$ and every position would be an equilibrium; the coefficient of the square root of 2 minus 1 comes only from the spacing of the figure.
* **Carrier at rest.** If the bearing centres were held still (rate of $\theta$ zero), the two no-slip conditions of part (b) would give a zero spin of every bearing and a zero rate of the disk: with the ring fixed, a planetary train cannot turn its sun without moving its planets.
* **Equilibrium position.** At $\theta$ equal to $\pi/2$ the bearing $A$ is at the top and $B$, $C$ are symmetric below, at $45^\circ$ on either side of the downward vertical: the configuration is symmetric about $Oy$, as an equilibrium of a symmetric heavy system should be.
* **Dimensions.** Every term of the equation of motion is an angular acceleration, every term of the energy equation an energy and the frequency is in rad/s.

---

## Problem RB-27: Rectangle with weight, pulleys, and string

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a homogeneous rectangular block of mass $2m$, width $2L$ (along $x_B$) and height $L$ (along $y_B$), moving in the vertical plane $Oxy$; a point weight $P$ of mass $m$ that slides on the vertical through $C$ (read as a frictionless guide); a massless inextensible string of length $6L$ from $G$ over the pulleys $O$ and $C$ to $P$, always tense; a spring of stiffness $k$ and zero natural length from the midpoint $A$ of the right short edge to the fixed point $B$.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, $\mathbf i$ along $Ox$ (to the right, towards $B$), $\mathbf j$ along $Oy$ (up), $\mathbf k$ out of the paper (⊙, the axes of the pulleys). Gravity is $-g\,\mathbf j$. The fixed points are $B$ at $2L\,\mathbf i$ and $C$ at minus $2L\,\mathbf i$.
* **String frame:** $S_1\{O; \mathcal B_1\}$, with $\mathbf i_1$ along $\overrightarrow{OG}$, $\mathbf k_1$ equal to $\mathbf k$ and $\mathbf j_1$ completing the right-handed basis (the choice of the key).
* **Block frame:** $S_B\{G; \mathcal B_B\}$, $\mathbf i_B$ along $Gx_B$ (from $G$ towards $A$), $\mathbf j_B$ along $Gy_B$, $\mathbf k_B$ equal to $\mathbf k$.
* **Coordinates (read from the figure):** $\xi$, depth of $P$ below $C$; $\theta$, angle of $\overrightarrow{OG}$ from the downward vertical, positive when $G$ is to the right of the vertical through $O$ (counterclockwise about $\mathbf k$, from minus $\mathbf j$ towards $\mathbf i$); $\varphi$, angle of $\mathbf i_B$ from the horizontal $\mathbf i$, counterclockwise. The figure marks only the angles and their arcs; the opposite reading of the sense of $\theta$ would change the sign of every term odd in $\theta$ (the sines of $\theta$), not the method.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the block | $2m$ | kg |
| Width and height of the block | $2L$, $L$ | m |
| Mass of the weight $P$ | $m$ | kg |
| Length of the string | $6L$ | m |
| Distance between the pulleys $O$ and $C$ | $2L$ | m |
| Spring | stiffness $k$, natural length zero, from $A$ to $B$ | N/m |
| Position of $B$ and of $C$ | $2L\,\mathbf i$, $-2L\,\mathbf i$ | m |
| Gravity | $-g\,\mathbf j$ | m/s$^2$ |

#### Part (a): degrees of freedom

> [!derivation] Part (a): count of the degrees of freedom
> **Law:** three coordinates for a rigid body in planar motion, two for a particle in the plane; one equation per constraint
> **Source:** Notes.pdf, Sec. 13.1; Notes.pdf, Sec. 13.4
>
> $$\begin{aligned}
> n_q &= 3 + 2 = 5 \quad &\text{(block in the plane: $G$ and $\varphi$; particle $P$ in the plane)} \\
> n_c &= 1 + 1 = 2 \quad &\text{($P$ on the vertical through $C$; length of the tense string)} \\
> n_{\mathrm{dof}} &= 5 - 2 = 3 \quad &\text{(the two constraints are independent: one fixes the abscissa of $P$, the other the distance $OG$)}
> \end{aligned}$$
>
> $$\boxed{n_{\mathrm{dof}} = 3, \qquad \text{coordinates } \xi,\ \theta,\ \varphi}$$
>
> **Units:** dimensionless counts
> **Meaning:** the depth of the weight fixes how much string is left between $O$ and $G$, the angle of the string fixes the direction of $G$, and the block can still turn freely about $G$ because the string is tied at $G$ itself.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb27-string-basis.svg]]

> [!derivation] String basis: the angle measured from the downward vertical
> **Law:** simple rotation about the third axis; right-hand rule; relation of an angle from the vertical with the polar angle; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the plane $Oxy$ with $\mathbf k$ out of the paper (⊙). The polar angle of $\mathbf i_1$ measured from $\mathbf i$ counterclockwise is $\theta - \pi/2$, because $\theta$ is measured from minus $\mathbf j$, which is itself $\mathbf i$ turned by minus $\pi/2$. Right triangle of $\mathbf i_1$ (hypotenuse 1): the leg along the vertical is adjacent to $\theta$ (cosine) and points down, towards minus $\mathbf j$; the horizontal leg is opposite to $\theta$ (sine) and points along $\mathbf i$. $\mathbf j_1$ is $\mathbf i_1$ turned counterclockwise by $\pi/2$ (the cross product of $\mathbf k$ and $\mathbf i_1$).
>
> $$\begin{aligned}
> \cos\!\left(\theta - \frac{\pi}{2}\right) &= \cos\theta\cos\frac{\pi}{2} + \sin\theta\sin\frac{\pi}{2} = \sin\theta \quad &\text{(addition formula)} \\
> \sin\!\left(\theta - \frac{\pi}{2}\right) &= \sin\theta\cos\frac{\pi}{2} - \cos\theta\sin\frac{\pi}{2} = -\cos\theta \quad &\text{(addition formula)} \\
> \mathbf i_1 &= \sin\theta\,\mathbf i - \cos\theta\,\mathbf j \quad &\text{(polar components; legs of the triangle)} \\
> \mathbf j_1 &= \mathbf k\times\mathbf i_1 = \sin\theta\,\mathbf k\times\mathbf i - \cos\theta\,\mathbf k\times\mathbf j = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> [{}_0R_1] &= \begin{bmatrix} \sin\theta & \cos\theta & 0 \cr -\cos\theta & \sin\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\sin^2\theta + \cos^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \sin^2\theta + \cos^2\theta & -\sin\theta\cos\theta + \cos\theta\sin\theta & 0 \cr -\cos\theta\sin\theta + \sin\theta\cos\theta & \cos^2\theta + \sin^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k, \qquad \dot{\mathbf i}_1 = \dot\theta\,\mathbf k\times\mathbf i_1 = \dot\theta\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\theta\,\mathbf k\times\mathbf j_1 = -\dot\theta\,\mathbf i_1 \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j, \quad \mathbf j_1 = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j, \quad \dot{\mathbf i}_1 = \dot\theta\,\mathbf j_1, \quad \dot{\mathbf j}_1 = -\dot\theta\,\mathbf i_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$ in the derivatives
> **Meaning:** with $\theta$ zero the string hangs straight down from $O$ and $\mathbf j_1$ is horizontal, pointing towards $B$; the derivative of $\mathbf i_1$ is the direction in which $G$ swings for a growing $\theta$.

![[attachments/EM-SOL/rb27-block-basis.svg]]

> [!derivation] Block basis: rotation by phi about k
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; [Lecture 7, Slide 12]
>
> View of the plane $Oxy$ with $\mathbf k$ out of the paper (⊙): a positive $\varphi$ turns counterclockwise. $\mathbf i_B$: adjacent leg along $\mathbf i$ (cosine of $\varphi$), opposite leg along $\mathbf j$ (sine). $\mathbf j_B$: adjacent leg along $\mathbf j$ (cosine); the counterclockwise turn carries the tip of $\mathbf j$ to the left, towards minus $\mathbf i$, which is the minus sign.
>
> $$\begin{aligned}
> \mathbf i_B &= \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j, \qquad \mathbf j_B = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j \quad &\text{(legs of the two triangles)} \\
> [{}_0R_B] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_B$, $\mathbf j_B$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_B] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_B][{}_0R_B]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{B0} &= \dot\varphi\,\mathbf k \quad &\text{(rate of the angle along its axis)} \\
> \boldsymbol\alpha_{B0} &= \ddot\varphi\,\mathbf k + \dot\varphi\,\dot{\mathbf k} = \ddot\varphi\,\mathbf k \quad &\text{(product rule; $\mathbf k$ fixed)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_B = \cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j, \quad \mathbf j_B = -\sin\varphi\,\mathbf i + \cos\varphi\,\mathbf j, \quad \boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k, \quad \boldsymbol\alpha_{B0} = \ddot\varphi\,\mathbf k}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the block turns about the fixed direction $\mathbf k$ only, so its angular acceleration is the second rate of $\varphi$ along $\mathbf k$, with no term from a turning axis.

> [!derivation] Constraint of the string, and positions of G, P and A
> **Law:** inextensible string over frictionless pulleys of negligible radius; position vectors
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Sec. 6.6; Problems.pdf, p. 57
>
> The string runs straight from $G$ to $O$, from $O$ to $C$ along the axis $Ox$ and down from $C$ to $P$; the pulleys have negligible radius, so the three straight pieces add up to the whole length. $A$ is the midpoint of the short edge on the side of $\mathbf i_B$, at half the width from $G$.
>
> $$\begin{aligned}
> |\overrightarrow{OG}| + |\overrightarrow{OC}| + |\overrightarrow{CP}| &= |\overrightarrow{OG}| + 2L + \xi = 6L \;\Rightarrow\; |\overrightarrow{OG}| = 4L - \xi \quad &\text{(length of the string)} \\
> \mathbf r_0^G &= \left(4L - \xi\right)\mathbf i_1 \quad &\text{(along the string piece $OG$)} \\
> \mathbf r_0^P &= \overrightarrow{OC} + \overrightarrow{CP} = -2L\,\mathbf i - \xi\,\mathbf j \quad &\text{($P$ below $C$)} \\
> \mathbf r_0^A &= \mathbf r_0^G + L\,\mathbf i_B = \left(4L - \xi\right)\mathbf i_1 + L\,\mathbf i_B \quad &\text{(half of the width $2L$ along $\mathbf i_B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \left(4L - \xi\right)\left(\sin\theta\,\mathbf i - \cos\theta\,\mathbf j\right), \qquad \mathbf r_0^P = -2L\,\mathbf i - \xi\,\mathbf j, \qquad \mathbf r_0^A = \mathbf r_0^G + L\left(\cos\varphi\,\mathbf i + \sin\varphi\,\mathbf j\right)}$$
>
> **Units:** $[\mathrm L]$
> **Meaning:** when the weight goes down (growing $\xi$) the string piece $OG$ shortens by the same length and the block rises towards $O$.

> [!derivation] Part (b): velocity and acceleration of G and of P
> **Law:** derivative of a vector written in a moving basis; product rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> $$\begin{aligned}
> \mathbf v_0^G &= \frac{d}{dt}\left(4L - \xi\right)\mathbf i_1 + \left(4L - \xi\right)\dot{\mathbf i}_1 = -\dot\xi\,\mathbf i_1 + \left(4L - \xi\right)\dot\theta\,\mathbf j_1 \quad &\text{(product rule; Poisson)} \\
> \mathbf a_0^G &= -\ddot\xi\,\mathbf i_1 - \dot\xi\,\dot{\mathbf i}_1 - \dot\xi\dot\theta\,\mathbf j_1 + \left(4L - \xi\right)\ddot\theta\,\mathbf j_1 + \left(4L - \xi\right)\dot\theta\,\dot{\mathbf j}_1 \quad &\text{(product rule on both terms)} \\
> &= -\ddot\xi\,\mathbf i_1 - 2\dot\xi\dot\theta\,\mathbf j_1 + \left(4L - \xi\right)\ddot\theta\,\mathbf j_1 - \left(4L - \xi\right)\dot\theta^2\,\mathbf i_1 \quad &\text{(Poisson; collect the two equal terms)} \\
> \mathbf v_0^P &= -\dot\xi\,\mathbf j, \qquad \mathbf a_0^P = -\ddot\xi\,\mathbf j \quad &\text{(derivatives in the fixed basis)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_0^G = \left(4L - \xi\right)\mathbf i_1, \qquad \mathbf v_0^G = -\dot\xi\,\mathbf i_1 + \left(4L - \xi\right)\dot\theta\,\mathbf j_1 \\ \mathbf a_0^G = -\left[\ddot\xi + \left(4L - \xi\right)\dot\theta^2\right]\mathbf i_1 + \left[\left(4L - \xi\right)\ddot\theta - 2\dot\xi\dot\theta\right]\mathbf j_1, \qquad \mathbf a_0^P = -\ddot\xi\,\mathbf j \end{gathered}}$$
>
> **Units:** $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$ in every term
> **Meaning:** along the string the acceleration of $G$ has the reeling term and the centripetal term (towards $O$); across it, the angular acceleration term and the Coriolis-like term of the reeling and swinging motions together.

### Center of Mass and Inertia Tensor

> [!derivation] Tensor of inertia of the block at G
> **Law:** moments and products of inertia as volume integrals in Cartesian coordinates; symmetry of the rectangle
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.6; [Lecture 8, Slide 10]
>
> The block is homogeneous, of thickness $e$ along $\mathbf k$, so its density is $2m/(2L\cdot L\cdot e)$, written $\rho_m$. Body coordinates $x$ from minus $L$ to $L$ along $\mathbf i_B$, $y$ from minus $L/2$ to $L/2$ along $\mathbf j_B$, $z$ from minus $e/2$ to $e/2$; the element of mass is $\rho_m\,dx\,dy\,dz$. The centre of mass is the geometric centre $G$, because every first moment is the integral of an odd function over a symmetric interval.
>
> $$\begin{aligned}
> \int_{-L}^{L}x^2\,dx &= \left[\frac{x^3}{3}\right]_{-L}^{L} = \frac{L^3}{3} - \left(-\frac{L^3}{3}\right) = \frac{2L^3}{3} \quad &\text{(antiderivative; Barrow's rule)} \\
> \int_{-L/2}^{L/2}y^2\,dy &= \left[\frac{y^3}{3}\right]_{-L/2}^{L/2} = \frac{L^3}{24} - \left(-\frac{L^3}{24}\right) = \frac{L^3}{12} \quad &\text{(antiderivative; Barrow's rule)} \\
> I_{zz} &= \rho_m\int_{-e/2}^{e/2}\!\!dz\left(\int_{-L}^{L}x^2\,dx\cdot L + 2L\cdot\int_{-L/2}^{L/2}y^2\,dy\right) = \rho_m\,e\left(\frac{2L^4}{3} + \frac{L^4}{6}\right) \quad &\text{(squared distance to the axis $Gz_B$ is the sum of the squares of $x$ and $y$)} \\
> &= \frac{2m}{2L^2 e}\cdot e\cdot\frac{5L^4}{6} = \frac{5mL^2}{6} \quad &\text{(value of $\rho_m$)} \\
> P_{xz} &= \rho_m\int x\,dx\int dy\int z\,dz = 0, \qquad P_{yz} = 0 \quad &\text{(odd integrands over symmetric intervals)}
> \end{aligned}$$
>
> $$\boxed{I_{zz}^G = \frac{5mL^2}{6}, \qquad P_{xz} = P_{yz} = 0}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the axis $Gz_B$ is a principal axis, so the angular momentum of the planar motion is along $\mathbf k$; the thickness does not enter. The value is the one printed in the key.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momenta and kinetic energy of the block and the weight
> **Law:** linear momentum; angular momentum about the centre of mass; Koenig's theorem
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 9]
>
> $$\begin{aligned}
> \mathbf p_0 &= 2m\,\mathbf v_0^G + m\,\mathbf v_0^P = -2m\dot\xi\,\mathbf i_1 + 2m\left(4L - \xi\right)\dot\theta\,\mathbf j_1 - m\dot\xi\,\mathbf j \quad &\text{(Eq. 11.3 for each body)} \\
> \mathbf H_G^B &= \bar{\bar I}_G\cdot\boldsymbol\omega_{B0} = \frac{5mL^2}{6}\,\dot\varphi\,\mathbf k \quad &\text{(Eq. 11.12; principal axis $\mathbf k$)} \\
> T^B &= \frac12\,2m\left(v_0^G\right)^2 + \frac12\,I_{zz}^G\,\dot\varphi^2 = m\left[\dot\xi^2 + \left(4L - \xi\right)^2\dot\theta^2\right] + \frac{5mL^2}{12}\,\dot\varphi^2 \quad &\text{(Eq. 11.31; orthonormal $\mathbf i_1$, $\mathbf j_1$)} \\
> T^P &= \frac12\,m\dot\xi^2 \quad &\text{(particle)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G^B = \frac{5mL^2}{6}\,\dot\varphi\,\mathbf k, \qquad T = \frac32\,m\dot\xi^2 + m\left(4L - \xi\right)^2\dot\theta^2 + \frac{5mL^2}{12}\,\dot\varphi^2}$$
>
> **Units:** kg m$^2$/s; J in every term
> **Meaning:** the reeling rate enters the energy with the mass of the block and of the weight together (the factor 3/2 is the half of $3m$), since both move with the speed of the string.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb27-exploded.svg]]

The exploded view separates the block, the weight $P$, the string and the two pulleys. The string is massless and pulls each end along itself; the pulleys are massless and frictionless, so the tension $T$ is the same on both sides of each of them (box below). The guide on the vertical through $C$ is frictionless and pushes $P$ horizontally. The block moves in the plane $Oxy$ by hypothesis of the statement, and every load below lies in that plane.

> [!derivation] Tension along the string
> **Law:** equations of a massless pulley; moment about its fixed axle
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Sec. 13.4
>
> Take the pulley at $O$, of radius $r$ that later tends to zero, with tensions $T_1$ and $T_2$ on its two sides. The axle is frictionless (no torque about $\mathbf k$) and the pulley has no mass, so its angular momentum is zero.
>
> $$\begin{aligned}
> \mathbf 0 &= \frac{d\mathbf H_O^{\text{pulley}}}{dt} = \left(r\,T_1 - r\,T_2\right)\mathbf k \quad &\text{(Eq. 12.13 about the fixed axle; zero mass)} \\
> T_1 &= T_2 \quad &\text{(divide by $r$)}
> \end{aligned}$$
>
> $$\boxed{T_{GO} = T_{OC} = T_{CP} \equiv T}$$
>
> **Units:** N
> **Meaning:** one unknown tension for the whole string; the axle reactions act on the pulleys only and never on the block or on $P$.

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of $P$ | $P$ | $P$ | $-mg\,\mathbf j$ | applied |
| String on $P$ | $P$ | $P$ | $T\,\mathbf j$ (towards $C$) | constraint |
| Guide on $P$ | $P$ | $P$ | $N_P\,\mathbf i$ | constraint |
| Weight of the block | block | $G$ | $-2mg\,\mathbf j = 2mg\left(\cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf j_1\right)$ | applied |
| String on the block | block | $G$ | $-T\,\mathbf i_1$ (towards $O$) | constraint |
| Spring on the block | block | $A$ | $\mathbf F_s = -k\left(\mathbf r_0^A - \mathbf r_0^B\right)$ | applied |

> [!derivation] Part (c): spring force, its components in B1 and its moment about G
> **Law:** linear spring of zero natural length; vector product expanded along the first row
> **Source:** Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 12.13; [Lecture 10, Slide 11]
>
> Write $\mathbf d$ for the vector from $B$ to $A$. The weight in $\mathcal B_1$ uses the inverse of the string basis: minus $\mathbf j$ dotted with $\mathbf i_1$ is the cosine of $\theta$, dotted with $\mathbf j_1$ minus the sine.
>
> $$\begin{aligned}
> \mathbf d &= \mathbf r_0^A - 2L\,\mathbf i = \left[\left(4L - \xi\right)\sin\theta + L\cos\varphi - 2L\right]\mathbf i + \left[-\left(4L - \xi\right)\cos\theta + L\sin\varphi\right]\mathbf j \quad &\text{(positions of $A$ and $B$)} \\
> \mathbf d\cdot\mathbf i_1 &= \left(4L - \xi\right)\left(\sin^2\theta + \cos^2\theta\right) + L\left(\cos\varphi\sin\theta - \sin\varphi\cos\theta\right) - 2L\sin\theta \quad &\text{(dot product with $\sin\theta\,\mathbf i - \cos\theta\,\mathbf j$)} \\
> &= 4L - \xi - L\sin\left(\varphi - \theta\right) - 2L\sin\theta \quad &\text{(Pythagoras; sine of a difference)} \\
> \mathbf d\cdot\mathbf j_1 &= L\left(\cos\varphi\cos\theta + \sin\varphi\sin\theta\right) - 2L\cos\theta = L\cos\left(\varphi - \theta\right) - 2L\cos\theta \quad &\text{(dot product with $\cos\theta\,\mathbf i + \sin\theta\,\mathbf j$; the terms in $4L - \xi$ cancel)} \\
> \overrightarrow{GA}\times\mathbf F_s &= -k\,L\begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \cos\varphi & \sin\varphi & 0 \cr d_x & d_y & 0 \end{vmatrix} = -kL\left(d_y\cos\varphi - d_x\sin\varphi\right)\mathbf k \quad &\text{(expand along the first row)} \\
> d_y\cos\varphi - d_x\sin\varphi &= -\left(4L - \xi\right)\left(\cos\theta\cos\varphi + \sin\theta\sin\varphi\right) + 2L\sin\varphi = -\left(4L - \xi\right)\cos\left(\varphi - \theta\right) + 2L\sin\varphi \quad &\text{(the terms $L\sin\varphi\cos\varphi$ cancel)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf F_s = -k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right]\mathbf i_1 - k\left[L\cos(\varphi - \theta) - 2L\cos\theta\right]\mathbf j_1 \\ \mathbf M_G^s = kL\left[\left(4L - \xi\right)\cos(\varphi - \theta) - 2L\sin\varphi\right]\mathbf k \end{gathered}}$$
>
> **Units:** N; N m
> **Meaning:** the spring pulls $A$ straight towards $B$ with a force proportional to their distance. Its moment about $G$ is the only moment on the block: the weight and the string act at $G$ itself.

> [!derivation] Equations of the weight P and of the block
> **Law:** Newton's second law for a particle and for the centre of mass of the block; moment equation about the centre of mass
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> The pole of the moment equation is $G$, the centre of mass, so the term in the velocity of the pole vanishes (velocity of $G$ crossed with a momentum parallel to it); the basis direction $\mathbf k$ is fixed, so the angular momentum is differentiated component by component.
>
> $$\begin{aligned}
> m\left(-\ddot\xi\,\mathbf j\right) &= -mg\,\mathbf j + T\,\mathbf j + N_P\,\mathbf i \quad &\text{(Eq. 12.8 for $P$)} \\
> 2m\,\mathbf a_0^G\cdot\mathbf i_1 &= -2m\left[\ddot\xi + \left(4L - \xi\right)\dot\theta^2\right] = 2mg\cos\theta - k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right] - T \quad &\text{(Eq. 12.8 for the block along $\mathbf i_1$)} \\
> 2m\,\mathbf a_0^G\cdot\mathbf j_1 &= 2m\left[\left(4L - \xi\right)\ddot\theta - 2\dot\xi\dot\theta\right] = -2mg\sin\theta - k\left[L\cos(\varphi - \theta) - 2L\cos\theta\right] \quad &\text{(Eq. 12.8 for the block along $\mathbf j_1$)} \\
> \frac{d\mathbf H_G^B}{dt} &= \frac{5mL^2}{6}\,\ddot\varphi\,\mathbf k = \mathbf M_G^s \quad &\text{(Eq. 12.13 about $G$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} -m\ddot\xi = -mg + T, \qquad N_P = 0 \\ -2m\left[\ddot\xi + \left(4L - \xi\right)\dot\theta^2\right] = 2mg\cos\theta - k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right] - T \\ 2m\left[\left(4L - \xi\right)\ddot\theta - 2\dot\xi\dot\theta\right] = -2mg\sin\theta - kL\left[\cos(\varphi - \theta) - 2\cos\theta\right] \\ \frac{5mL^2}{6}\,\ddot\varphi = kL\left[\left(4L - \xi\right)\cos(\varphi - \theta) - 2L\sin\varphi\right] \end{gathered}}$$
>
> **Units:** N in the force equations; N m in the moment equation
> **Meaning:** five scalar equations for five unknowns: the three second rates, the tension and the guide force. The guide force vanishes because $P$ has no horizontal acceleration and no other horizontal load.

> [!derivation] Part (d): three second order equations for xi, theta and phi
> **Law:** elimination of the tension with the equation of $P$
> **Source:** Notes.pdf, Sec. 13.4; Notes.pdf, Eq. 12.8
>
> $$\begin{aligned}
> T &= m\left(g - \ddot\xi\right) \quad &\text{(equation of $P$)} \\
> -2m\ddot\xi - 2m\left(4L - \xi\right)\dot\theta^2 &= 2mg\cos\theta - k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right] - mg + m\ddot\xi \quad &\text{(tension in the equation along $\mathbf i_1$)} \\
> 3m\ddot\xi &= -2m\left(4L - \xi\right)\dot\theta^2 - mg\left(2\cos\theta - 1\right) + k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right] \quad &\text{(collect the second rates on the left)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} 3m\ddot\xi = -2m\left(4L - \xi\right)\dot\theta^2 - mg\left(2\cos\theta - 1\right) + k\left[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta\right] \\ 2m\left[\left(4L - \xi\right)\ddot\theta - 2\dot\xi\dot\theta\right] = -2mg\sin\theta - kL\left[\cos(\varphi - \theta) - 2\cos\theta\right] \\ \frac{5mL^2}{6}\,\ddot\varphi = kL\left[\left(4L - \xi\right)\cos(\varphi - \theta) - 2L\sin\varphi\right] \end{gathered}}$$
>
> **Units:** N in the first two equations; N m in the third
> **Meaning:** the three equations are coupled through the spring, which ties the rotation of the block to the swing and to the length of the string. The string stays tense, as assumed, while the tension, $m$ times the difference of $g$ and the second rate of $\xi$, is positive, that is while the weight falls with an acceleration smaller than $g$.

> [!derivation] Part (e): conservation of mechanical energy
> **Law:** power of the constraint forces; energy theorem; potential energy of the weights and of the spring
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; [Lecture 10, Slide 18]
>
> The tension acts on the block at $G$ and on $P$; the guide force is normal to the velocity of $P$; the pulley reactions act on fixed axles. The weights and the spring are conservative.
>
> $$\begin{aligned}
> \dot W^{T} &= -T\,\mathbf i_1\cdot\mathbf v_0^G + T\,\mathbf j\cdot\mathbf v_0^P = -T\left(-\dot\xi\right) + T\left(-\dot\xi\right) = 0 \quad &\text{(string on the block plus string on $P$; here $T$ is the tension, not the kinetic energy)} \\
> \dot W^{N} &= N_P\,\mathbf i\cdot\left(-\dot\xi\,\mathbf j\right) = 0 \quad &\text{(guide normal to the motion of $P$)} \\
> V &= 2mg\,\mathbf j\cdot\mathbf r_0^G + mg\,\mathbf j\cdot\mathbf r_0^P + \frac k2\,\mathbf d\cdot\mathbf d = -2mg\left(4L - \xi\right)\cos\theta - mg\,\xi + \frac k2\,|\mathbf d|^2 \quad &\text{(Eq. 12.34; spring of zero natural length)} \\
> |\mathbf d|^2 &= \left(4L - \xi\right)^2 + L^2 + 4L^2 + 2L\left(4L - \xi\right)\left(\sin\theta\cos\varphi - \cos\theta\sin\varphi\right) - 4L\left(4L - \xi\right)\sin\theta - 4L^2\cos\varphi \quad &\text{(square of the two components of $\mathbf d$)} \\
> &= \left(4L - \xi\right)^2 + 5L^2 - 2L\left(4L - \xi\right)\sin(\varphi - \theta) - 4L\left(4L - \xi\right)\sin\theta - 4L^2\cos\varphi \quad &\text{(sine of a difference)} \\
> \int_0^t\frac{d}{dt'}\left(T + V\right)dt' &= \left[T + V\right]_0^t = 0 \quad &\text{(Eq. 12.33 with workless constraints; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\frac32\,m\dot\xi^2 + m\left(4L - \xi\right)^2\dot\theta^2 + \frac{5mL^2}{12}\,\dot\varphi^2 - 2mg\left(4L - \xi\right)\cos\theta - mg\,\xi + \frac k2\left[\left(4L - \xi\right)^2 + 5L^2 - 2L\left(4L - \xi\right)\sin(\varphi - \theta) - 4L\left(4L - \xi\right)\sin\theta - 4L^2\cos\varphi\right] = E_0}$$
>
> **Units:** J in every term
> **Meaning:** yes, the mechanical energy is conserved: the tension does positive work on one end of the string and the same negative work on the other, the guide and the pulley axles do no work, and the remaining forces derive from a potential. The constant is the value of the left side at the initial instant.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom | Three: $\xi$, $\theta$, $\varphi$ |
| (b) Kinematics of $G$ and of the block | $\mathbf r_0^G = (4L - \xi)\,\mathbf i_1$; $\mathbf v_0^G = -\dot\xi\,\mathbf i_1 + (4L - \xi)\dot\theta\,\mathbf j_1$; $\mathbf a_0^G = -[\ddot\xi + (4L - \xi)\dot\theta^2]\,\mathbf i_1 + [(4L - \xi)\ddot\theta - 2\dot\xi\dot\theta]\,\mathbf j_1$, with $\mathbf i_1 = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j$, $\mathbf j_1 = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j$; $\boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k$, $\boldsymbol\alpha_{B0} = \ddot\varphi\,\mathbf k$ |
| (c) Forces | On $P$: $-mg\,\mathbf j$, $T\,\mathbf j$, $N_P\,\mathbf i$ (zero). On the block: $-2mg\,\mathbf j$ and $-T\,\mathbf i_1$ at $G$; $\mathbf F_s = -k[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta]\,\mathbf i_1 - k[L\cos(\varphi - \theta) - 2L\cos\theta]\,\mathbf j_1$ at $A$ |
| (d) Equations of motion | $3m\ddot\xi = -2m(4L - \xi)\dot\theta^2 - mg(2\cos\theta - 1) + k[4L - \xi - L\sin(\varphi - \theta) - 2L\sin\theta]$; $2m[(4L - \xi)\ddot\theta - 2\dot\xi\dot\theta] = -2mg\sin\theta - kL[\cos(\varphi - \theta) - 2\cos\theta]$; $\tfrac{5mL^2}{6}\ddot\varphi = kL[(4L - \xi)\cos(\varphi - \theta) - 2L\sin\varphi]$ |
| (e) Energy | Conserved: $\tfrac32 m\dot\xi^2 + m(4L - \xi)^2\dot\theta^2 + \tfrac{5mL^2}{12}\dot\varphi^2 - 2mg(4L - \xi)\cos\theta - mg\xi + \tfrac k2\lvert\overrightarrow{BA}\rvert^2 = E_0$ |

**Check against the official key:** the key (Problems.pdf, p. 81) uses the same basis ($\mathbf i_1$ along $OG$, $\mathbf j_1$ by the right-hand rule) and prints Newton's second law of the block along $\mathbf i_1$ with the tension, along $\mathbf j_1$, the equation of $P$ that gives the tension, and the moment equation about $G$ with the moment of inertia $5mL^2/6$. Each printed equation coincides term by term with the boxed equations of the block and of $P$ in the Free-Body Diagram section (the equation along $\mathbf i_1$ is printed before the tension is eliminated; part (d) eliminates it): **match**. The key prints no expression for the energy of part (e).

**Limiting cases and consistency:**

* **No spring.** With $k$ zero the third equation gives a constant spin of the block, and with the string vertical and at rest the first equation gives a second rate of $\xi$ of minus $g/3$: the weight rises and the block descends with the acceleration of an Atwood machine with masses $2m$ and $m$, the difference of the weights over the sum of the masses.
* **Tension in that case.** Then the tension is $m$ times the sum of $g$ and $g/3$, four thirds of $mg$: between the weight of $P$ and the weight of the block, as it must be for $P$ to accelerate upwards and the block downwards.
* **Spring force at the reference position.** With the string vertical, $\varphi$ zero and $\xi$ equal to $2L$, $A$ lies at $L\,\mathbf i - 2L\,\mathbf j$ and $B$ at $2L\,\mathbf i$; the bracket of the $\mathbf j_1$ component is $L$ minus $2L$, so the spring pulls $A$, and with it the block, towards plus $\mathbf j_1$, which is $\mathbf i$ at that instant: towards $B$, as expected from its position.
* **Dimensions.** $k$ times a length is a force like $mg$; $kL$ times a length is a moment like $mL^2$ times an angular acceleration; every term of the energy is in joules.

---

## Problem RB-29: Disk-bar train

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** two rigid bodies in the vertical plane of the wall. The disk $D$, homogeneous, of radius $R$ and mass $m$, turns about its centre $O$, fixed to the wall (an ideal pin). The bar $B$, homogeneous and slender, of length $L$ and mass $2m$, with centre of mass $G$ at its midpoint, is pinned to the rim of the disk at its end $C$ (ideal pin) and slides without friction, through its groove, over the knob $K$ fixed at the height $h$ above $O$. Its other end $A$ is pulled towards the axis $Oy_0$ by the force $\mathbf F_A$, horizontal and proportional to the distance of $A$ to that axis, with constant $k$.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, $\mathbf i_0$ along $Ox_0$ (to the right), $\mathbf j_0$ along $Oy_0$ (up), $\mathbf k_0$ out of the paper (⊙). Gravity is $-g\,\mathbf j_0$; the knob is at $h\,\mathbf j_0$.
* **Disk basis:** $\mathcal B_2\{\mathbf i_2, \mathbf j_2, \mathbf k_0\}$, attached to the disk, with $\mathbf i_2$ along $\overrightarrow{OC}$.
* **Bar frame:** $S_1\{C; \mathcal B_1\}$, attached to the bar, with $\mathbf j_1$ along the bar from $C$ towards $A$ (axis $y_1$ of the figure) and $\mathbf i_1$ normal to it (axis $x_1$).
* **Angles (read from the figure):** $\theta$, from $\mathbf i_0$ to $\overrightarrow{OC}$, counterclockwise about $\mathbf k_0$; $\varphi$, from $\mathbf i_0$ (the horizontal through $C$) to $\mathbf i_1$, counterclockwise. Both arcs of the figure are drawn counterclockwise; the opposite reading of either sense would change the sign of that angle in every formula, not the method.
* **Hypotheses:** the knob stays inside the groove, between $C$ and $A$ (its distance $s$ to $C$ is between 0 and $L$), and it is above the disk at every configuration used, with $h$ larger than $R$ (read from the figure), so that the height of $K$ above $C$ is positive.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Radius and mass of the disk | $R$, $m$ | m, kg |
| Length and mass of the bar | $L$, $2m$ | m, kg |
| Height of the knob above $O$ | $h$ | m |
| Constant of the force on $A$ | $k$ | N/m |
| Force on $A$ | $\mathbf F_A = -k\,x_0^A\,\mathbf i_0$ | N |
| Distance from $C$ to $K$ along the bar | $s$ | m |
| Gravity | $-g\,\mathbf j_0$ | m/s$^2$ |

#### Part (a): degrees of freedom

> [!derivation] Part (a): count of the degrees of freedom
> **Law:** three coordinates per rigid body in planar motion; two equations per planar pin; one per sliding contact
> **Source:** Notes.pdf, Sec. 13.1; Notes.pdf, Sec. 13.4
>
> $$\begin{aligned}
> n_q &= 3 + 3 = 6 \quad &\text{(disk and bar in the plane)} \\
> n_c &= 2 + 2 + 1 = 5 \quad &\text{(pin at $O$; pin at $C$; the line of the bar passes through $K$)} \\
> n_{\mathrm{dof}} &= 6 - 5 = 1 \quad &\text{(independent constraints)}
> \end{aligned}$$
>
> $$\boxed{n_{\mathrm{dof}} = 1, \qquad \text{coordinate } \theta;\ \varphi \text{ is a function of } \theta}$$
>
> **Units:** dimensionless counts
> **Meaning:** the angle of the disk fixes $C$, and the bar must then point from $C$ through $K$: its direction is fixed too. The bar can still slide along the groove only as far as $C$ moves, so nothing is left free.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb29-bases.svg]]

> [!derivation] Disk basis and bar basis: rotations by theta and phi about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View of the wall with $\mathbf k_0$ out of the paper (⊙): positive angles turn counterclockwise. For an angle $\alpha$ ($\theta$ for the disk, $\varphi$ for the bar) the first rotated vector has its adjacent leg along $\mathbf i_0$ (cosine) and its opposite leg along $\mathbf j_0$ (sine); the second one has its adjacent leg along $\mathbf j_0$ (cosine) and the counterclockwise turn carries the tip of $\mathbf j_0$ towards minus $\mathbf i_0$, which is the minus sign of the opposite leg (sine). For the bar, $\mathbf j_1$ is the direction from $C$ to $A$, up and to the left in the figure, which is that second vector.
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j_2 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0 \quad &\text{(legs, angle $\theta$)} \\
> \mathbf i_1 &= \cos\varphi\,\mathbf i_0 + \sin\varphi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0 \quad &\text{(legs, angle $\varphi$)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\varphi & -\sin\varphi & 0 \cr \sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_0$ in $\mathcal B_0$; same form for $[{}_0R_2]$ with $\theta$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & \cos\varphi\sin\varphi - \sin\varphi\cos\varphi & 0 \cr \sin\varphi\cos\varphi - \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products; same with $\theta$)} \\
> \boldsymbol\omega_{D0} &= \dot\theta\,\mathbf k_0, \qquad \boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k_0 \quad &\text{(rates of the angles along their axis)} \\
> \dot{\mathbf i}_1 &= \dot\varphi\,\mathbf k_0\times\mathbf i_1 = \dot\varphi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\varphi\,\mathbf k_0\times\mathbf j_1 = -\dot\varphi\,\mathbf i_1 \quad &\text{(Poisson; same for $\mathcal B_2$ with the rate of $\theta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_2 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \quad \mathbf i_1 = \cos\varphi\,\mathbf i_0 + \sin\varphi\,\mathbf j_0, \quad \mathbf j_1 = -\sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0, \quad \boldsymbol\omega_{D0} = \dot\theta\,\mathbf k_0, \quad \boldsymbol\omega_{B0} = \dot\varphi\,\mathbf k_0}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** both bodies turn about the fixed direction $\mathbf k_0$; the bar points along $\mathbf j_1$ and the knob pushes it along $\mathbf i_1$.

![[attachments/EM-SOL/rb29-knob-triangle.svg]]

> [!derivation] Part (b): geometric relation between theta and phi
> **Law:** the line of the bar passes through the knob; components of a vector in the bar basis
> **Source:** Notes.pdf, Sec. 13.1; Problems.pdf, p. 59
>
> The vector from $C$ to $K$ lies along the bar, so it has no component along $\mathbf i_1$, and its component along $\mathbf j_1$ is the distance $s$. Right triangle $C$-$K$ with the vertical through $K$: horizontal leg $R\cos\theta$ (from the axis $Oy_0$ to $C$), vertical leg $h - R\sin\theta$ (from the height of $C$ up to $K$), hypotenuse $s$. The bar makes the angle $\varphi$ with the vertical (since $\mathbf j_1$ is $\mathbf j_0$ turned by $\varphi$), so the horizontal leg is opposite to $\varphi$ (sine) and the vertical leg adjacent (cosine).
>
> $$\begin{aligned}
> \overrightarrow{CK} &= h\,\mathbf j_0 - R\,\mathbf i_2 = -R\cos\theta\,\mathbf i_0 + \left(h - R\sin\theta\right)\mathbf j_0 \quad &\text{(positions of $K$ and $C$)} \\
> \overrightarrow{CK}\cdot\mathbf i_1 &= -R\cos\theta\cos\varphi + \left(h - R\sin\theta\right)\sin\varphi = 0 \quad &\text{($K$ on the line of the bar)} \\
> s &= \overrightarrow{CK}\cdot\mathbf j_1 = R\cos\theta\sin\varphi + \left(h - R\sin\theta\right)\cos\varphi \quad &\text{(distance from $C$ to $K$)} \\
> s^2 &= R^2\cos^2\theta + \left(h - R\sin\theta\right)^2 = R^2 + h^2 - 2Rh\sin\theta \quad &\text{(Pythagoras in the triangle; $\cos^2 + \sin^2$)} \\
> \sin\varphi &= \frac{R\cos\theta}{s}, \qquad \cos\varphi = \frac{h - R\sin\theta}{s} \quad &\text{(opposite and adjacent legs over the hypotenuse)}
> \end{aligned}$$
>
> $$\boxed{\tan\varphi = \frac{R\cos\theta}{h - R\sin\theta}, \qquad s = \sqrt{R^2 + h^2 - 2Rh\sin\theta}}$$
>
> **Units:** dimensionless; $[\mathrm L]$
> **Meaning:** with $\theta$ zero ($C$ on the right of $O$) the tangent of $\varphi$ is the ratio of $R$ to $h$; with $\theta$ equal to $\pi/2$ ($C$ right below $K$) the bar is vertical and $\varphi$ is zero.

> [!derivation] Part (b): first and second rates of phi
> **Law:** implicit differentiation with the chain rule; quotient rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Sec. 13.1
>
> Write $f(\theta, \varphi)$ for the left side of the condition of the previous box with its sign changed, $R\cos\theta\cos\varphi - (h - R\sin\theta)\sin\varphi$, which is zero at every instant; its time derivative is zero too. Write $N$ for the difference $R - h\sin\theta$.
>
> $$\begin{aligned}
> \frac{df}{dt} &= \frac{\partial f}{\partial\theta}\,\dot\theta + \frac{\partial f}{\partial\varphi}\,\dot\varphi = 0 \quad &\text{(chain rule)} \\
> \frac{\partial f}{\partial\theta} &= -R\sin\theta\cos\varphi + R\cos\theta\sin\varphi = R\sin\left(\varphi - \theta\right) \quad &\text{(sine of a difference)} \\
> \frac{\partial f}{\partial\varphi} &= -R\cos\theta\sin\varphi - \left(h - R\sin\theta\right)\cos\varphi = -s \quad &\text{(previous box)} \\
> \dot\varphi &= \frac{R\sin\left(\varphi - \theta\right)}{s}\,\dot\theta \quad &\text{(solve for the rate)} \\
> \sin\left(\varphi - \theta\right) &= \sin\varphi\cos\theta - \cos\varphi\sin\theta = \frac{R\cos^2\theta - h\sin\theta + R\sin^2\theta}{s} = \frac{N}{s} \quad &\text{(sine and cosine of $\varphi$ from the previous box)} \\
> \dot\varphi &= \frac{R\,N}{s^2}\,\dot\theta \quad &\text{(substitute)} \\
> \dot N &= -h\cos\theta\,\dot\theta, \qquad \frac{d\left(s^2\right)}{dt} = -2Rh\cos\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\frac{N}{s^2}\right) &= \frac{\dot N s^2 - N\,d(s^2)/dt}{s^4} = \frac{h\cos\theta\,\dot\theta\left(2RN - s^2\right)}{s^4} = \frac{h\left(R^2 - h^2\right)\cos\theta\,\dot\theta}{s^4} \quad &\text{(quotient rule; $2RN - s^2$ equals $R^2 - h^2$)} \\
> \ddot\varphi &= \frac{R\,N}{s^2}\,\ddot\theta + R\,\dot\theta\,\frac{d}{dt}\left(\frac{N}{s^2}\right) \quad &\text{(product rule)}
> \end{aligned}$$
>
> $$\boxed{\dot\varphi = \frac{R\left(R - h\sin\theta\right)}{R^2 + h^2 - 2Rh\sin\theta}\,\dot\theta, \qquad \ddot\varphi = \frac{R\left(R - h\sin\theta\right)}{R^2 + h^2 - 2Rh\sin\theta}\,\ddot\theta + \frac{R h\left(R^2 - h^2\right)\cos\theta}{\left(R^2 + h^2 - 2Rh\sin\theta\right)^2}\,\dot\theta^2}$$
>
> **Units:** $[\mathrm L^2]/[\mathrm L^2]$ times $[\mathrm{T^{-1}}]$ and $[\mathrm{T^{-2}}]$; $[\mathrm L^4]/[\mathrm L^4]$ times $[\mathrm{T^{-2}}]$
> **Meaning:** the bar stops turning when the sine of $\theta$ is $R/h$: then the vector from $O$ to $C$ is normal to the bar (its dot product with the vector from $C$ to $K$ is $R$ times the difference of $h\sin\theta$ and $R$, zero), so the bar is tangent to the disk and $C$ moves along the bar itself.

> [!derivation] Part (c): positions, velocities and accelerations of A and G
> **Law:** velocity and acceleration fields of a rigid body (disk from $O$, bar from $C$); vector products expanded
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 6]
>
> $C$ belongs to both bodies; the disk gives its motion and the bar field carries it to $G$ (at half the length along $\mathbf j_1$) and to $A$ (at the full length). Write $\lambda$ for that distance, $L/2$ or $L$.
>
> $$\begin{aligned}
> \mathbf r_0^C &= R\,\mathbf i_2, \qquad \mathbf v_0^C = \dot\theta\,\mathbf k_0\times R\,\mathbf i_2 = R\dot\theta\,\mathbf j_2 \quad &\text{(Eq. 9.3 from the fixed point $O$)} \\
> \mathbf a_0^C &= \ddot\theta\,\mathbf k_0\times R\,\mathbf i_2 + \dot\theta\,\mathbf k_0\times\left(\dot\theta\,\mathbf k_0\times R\,\mathbf i_2\right) = R\ddot\theta\,\mathbf j_2 + \dot\theta\,\mathbf k_0\times R\dot\theta\,\mathbf j_2 = R\ddot\theta\,\mathbf j_2 - R\dot\theta^2\,\mathbf i_2 \quad &\text{(Eq. 9.4 from $O$; inner product first)} \\
> \mathbf r_0^P &= R\,\mathbf i_2 + \lambda\,\mathbf j_1 \quad &\text{($P$ is $G$ or $A$)} \\
> \mathbf v_0^P &= \mathbf v_0^C + \dot\varphi\,\mathbf k_0\times\lambda\,\mathbf j_1 = R\dot\theta\,\mathbf j_2 - \lambda\dot\varphi\,\mathbf i_1 \quad &\text{(Eq. 9.3 from $C$; $\mathbf k_0\times\mathbf j_1 = -\mathbf i_1$)} \\
> \mathbf a_0^P &= \mathbf a_0^C + \ddot\varphi\,\mathbf k_0\times\lambda\,\mathbf j_1 + \dot\varphi\,\mathbf k_0\times\left(-\lambda\dot\varphi\,\mathbf i_1\right) = \mathbf a_0^C - \lambda\ddot\varphi\,\mathbf i_1 - \lambda\dot\varphi^2\,\mathbf j_1 \quad &\text{(Eq. 9.4 from $C$; $\mathbf k_0\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_0^G = \left(R\cos\theta - \tfrac L2\sin\varphi\right)\mathbf i_0 + \left(R\sin\theta + \tfrac L2\cos\varphi\right)\mathbf j_0, \qquad \mathbf r_0^A = \left(R\cos\theta - L\sin\varphi\right)\mathbf i_0 + \left(R\sin\theta + L\cos\varphi\right)\mathbf j_0 \\ \mathbf v_0^G = R\dot\theta\,\mathbf j_2 - \tfrac L2\dot\varphi\,\mathbf i_1, \qquad \mathbf v_0^A = R\dot\theta\,\mathbf j_2 - L\dot\varphi\,\mathbf i_1 \\ \mathbf a_0^G = R\ddot\theta\,\mathbf j_2 - R\dot\theta^2\,\mathbf i_2 - \tfrac L2\ddot\varphi\,\mathbf i_1 - \tfrac L2\dot\varphi^2\,\mathbf j_1, \qquad \mathbf a_0^A = R\ddot\theta\,\mathbf j_2 - R\dot\theta^2\,\mathbf i_2 - L\ddot\varphi\,\mathbf i_1 - L\dot\varphi^2\,\mathbf j_1 \end{gathered}}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$ in every term
> **Meaning:** each point of the bar moves with $C$ on the circle of the rim plus a rotation about $C$; the bases $\mathcal B_2$ and $\mathcal B_1$ are those of the box of the rotations, and the rates of $\varphi$ are those of part (b).

### Center of Mass and Inertia Tensor

> [!derivation] Moments of inertia of the disk about O and of the bar about G
> **Law:** moment of inertia as the integral of the squared distance to the axis (polar coordinates with jacobian $\rho$ for the disk; a line integral for the slender bar)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.6; [Lecture 8, Slide 10]
>
> Disk: surface density $m/(\pi R^2)$, element $\sigma\rho\,d\rho\,d\chi$, distance $\rho$ to the axis through $O$ normal to the wall. Bar: linear density $2m/L$, coordinate $u$ from minus $L/2$ to $L/2$ measured from $G$ along the bar, distance $|u|$ to the axis through $G$ normal to the wall. Both centres of mass are the geometric centres, since the first moments are integrals of odd functions over symmetric ranges.
>
> $$\begin{aligned}
> I_O^D &= \frac{m}{\pi R^2}\int_0^{2\pi}\!\!\int_0^R\rho^2\,\rho\,d\rho\,d\chi = \frac{m}{\pi R^2}\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^R = \frac{m}{\pi R^2}\cdot 2\pi\cdot\frac{R^4}{4} = \frac{mR^2}{2} \quad &\text{(antiderivatives; Barrow's rule)} \\
> I_G^B &= \frac{2m}{L}\int_{-L/2}^{L/2}u^2\,du = \frac{2m}{L}\left[\frac{u^3}{3}\right]_{-L/2}^{L/2} = \frac{2m}{L}\left(\frac{L^3}{24} + \frac{L^3}{24}\right) = \frac{mL^2}{6} \quad &\text{(antiderivative; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{I_O^D = \frac{mR^2}{2}, \qquad I_G^B = \frac{mL^2}{6}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** only the moments about the normal to the wall enter the planar motion; both axes are principal by the symmetry of each body.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (e): kinetic energy of the disk and of the bar
> **Law:** kinetic energy about a fixed body point (disk); Koenig's theorem (bar)
> **Source:** Notes.pdf, Eq. 11.32; Notes.pdf, Eq. 11.31; [Lecture 9, Slide 9]
>
> The dot product of $\mathbf j_2$ and $\mathbf i_1$ is minus the sine of $\theta$ times the cosine of $\varphi$ plus the cosine of $\theta$ times the sine of $\varphi$, that is the sine of the difference of $\varphi$ and $\theta$.
>
> $$\begin{aligned}
> T^D &= \frac12\,I_O^D\,\dot\theta^2 = \frac{mR^2}{4}\,\dot\theta^2 \quad &\text{(Eq. 11.32; $O$ fixed)} \\
> \left(v_0^G\right)^2 &= R^2\dot\theta^2 + \frac{L^2}{4}\,\dot\varphi^2 - 2R\dot\theta\,\frac L2\,\dot\varphi\,\mathbf j_2\cdot\mathbf i_1 = R^2\dot\theta^2 + \frac{L^2}{4}\,\dot\varphi^2 - RL\,\dot\theta\dot\varphi\sin\left(\varphi - \theta\right) \quad &\text{(square of the velocity of part (c))} \\
> T^B &= \frac12\,2m\left(v_0^G\right)^2 + \frac12\,\frac{mL^2}{6}\,\dot\varphi^2 = mR^2\dot\theta^2 + \frac{mL^2}{4}\,\dot\varphi^2 - mRL\,\dot\theta\dot\varphi\sin\left(\varphi - \theta\right) + \frac{mL^2}{12}\,\dot\varphi^2 \quad &\text{(Eq. 11.31, Koenig)}
> \end{aligned}$$
>
> $$\boxed{T^D = \frac{mR^2}{4}\,\dot\theta^2, \qquad T^B = mR^2\dot\theta^2 + \frac{mL^2}{3}\,\dot\varphi^2 - mRL\,\dot\theta\dot\varphi\sin\left(\varphi - \theta\right)}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, J in every term
> **Meaning:** the cross term couples the two rotations. It vanishes when $\varphi$ equals $\theta$, that is when the bar is tangent to the disk at $C$: the velocity of $C$ is then along the bar and the rotation part of the velocity of $G$ normal to it.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb29-exploded.svg]]

The exploded view separates the disk and the bar at the pin $C$. The pin acts on the bar with the force $\mathbf R_C$, of components $X$ and $Y$ in $\mathcal B_0$, and on the disk with minus $\mathbf R_C$ (third law of Newton); being ideal, it transmits no torque. The pin $O$ acts on the disk with $\mathbf R_O$. The knob is frictionless: it can only push the bar normally to the groove, along $\mathbf i_1$, with the unknown $N_K$, and it acts at the bar point that coincides with $K$, at the distance $s$ from $C$. The problem is planar: the out-of-plane supports of the wall are not needed and every load below lies in the plane.

| Load | Body | Point | Expression in $\mathcal B_0$ | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the disk | $D$ | $O$ | $-mg\,\mathbf j_0$ | applied |
| Pin $O$ on the disk | $D$ | $O$ | $\mathbf R_O = R_{Ox}\,\mathbf i_0 + R_{Oy}\,\mathbf j_0$ | constraint |
| Bar on the disk | $D$ | $C$ | $-\mathbf R_C = -X\,\mathbf i_0 - Y\,\mathbf j_0$ | constraint (pair) |
| Disk on the bar | $B$ | $C$ | $\mathbf R_C = X\,\mathbf i_0 + Y\,\mathbf j_0$ | constraint (pair) |
| Weight of the bar | $B$ | $G$ | $-2mg\,\mathbf j_0$ | applied |
| Knob on the bar | $B$ | $K$ | $N_K\,\mathbf i_1 = N_K(\cos\varphi\,\mathbf i_0 + \sin\varphi\,\mathbf j_0)$ | constraint |
| Force on $A$ | $B$ | $A$ | $\mathbf F_A = -k\,x_0^A\,\mathbf i_0 = -k\left(R\cos\theta - L\sin\varphi\right)\mathbf i_0$ | applied |

> [!derivation] Part (d): moments of the loads on the bar about G and on the disk about O
> **Law:** moment of a force about a point; vector products expanded along the first row
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 1.37
>
> The arms from $G$ along the bar are minus $L/2$ to $C$, the difference of $s$ and $L/2$ to $K$, and $L/2$ to $A$, all along $\mathbf j_1$; the arm from $O$ to $C$ is $R\,\mathbf i_2$. The weights act at $G$ and at $O$ and have no moment about those points.
>
> $$\begin{aligned}
> -\frac L2\,\mathbf j_1\times\mathbf R_C &= \frac L2\begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr \sin\varphi & -\cos\varphi & 0 \cr X & Y & 0 \end{vmatrix} = \frac L2\left(X\cos\varphi + Y\sin\varphi\right)\mathbf k_0 \quad &\text{(minus $\mathbf j_1$ in $\mathcal B_0$; expand along the first row)} \\
> \left(s - \frac L2\right)\mathbf j_1\times N_K\,\mathbf i_1 &= -\left(s - \frac L2\right)N_K\,\mathbf k_0 \quad &\text{($\mathbf j_1\times\mathbf i_1 = -\mathbf k_0$)} \\
> \frac L2\,\mathbf j_1\times\left(-k\,x_0^A\,\mathbf i_0\right) &= \frac L2\begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr -\sin\varphi & \cos\varphi & 0 \cr -k\,x_0^A & 0 & 0 \end{vmatrix} = \frac{kL}{2}\,x_0^A\cos\varphi\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> R\,\mathbf i_2\times\left(-\mathbf R_C\right) &= -R\begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr \cos\theta & \sin\theta & 0 \cr X & Y & 0 \end{vmatrix} = R\left(X\sin\theta - Y\cos\theta\right)\mathbf k_0 \quad &\text{(expand along the first row)}
> \end{aligned}$$
>
> $$\boxed{M_G^B = \frac L2\left(X\cos\varphi + Y\sin\varphi\right) - \left(s - \frac L2\right)N_K + \frac{kL}{2}\left(R\cos\theta - L\sin\varphi\right)\cos\varphi, \qquad M_O^D = R\left(X\sin\theta - Y\cos\theta\right)}$$
>
> **Units:** N m in every term
> **Meaning:** the components along $\mathbf k_0$ of the moments that enter the two moment equations below. When $A$ is on the left of the axis (negative abscissa) and the cosine of $\varphi$ is positive, the moment of the pull on $A$ is negative, a clockwise turn: the force then points towards plus $\mathbf i_0$ and acts above $G$, so it tips the upper end of the bar back towards the axis.

> [!derivation] Part (d): equations of the bar and of the disk
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass (bar) and about a fixed point (disk)
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> For the bar the pole is its centre of mass $G$, so the term in the velocity of the pole vanishes; for the disk the pole $O$ is fixed and is also its centre of mass, so its acceleration and the pole term are zero. Both angular momenta lie along the fixed $\mathbf k_0$.
>
> $$\begin{aligned}
> 2m\,\mathbf a_0^G &= \mathbf R_C + N_K\,\mathbf i_1 - 2mg\,\mathbf j_0 - k\,x_0^A\,\mathbf i_0 \quad &\text{(Eq. 12.8 for the bar)} \\
> \frac{mL^2}{6}\,\ddot\varphi &= M_G^B \quad &\text{(Eq. 12.13 about $G$)} \\
> \frac{mR^2}{2}\,\ddot\theta &= M_O^D \quad &\text{(Eq. 12.13 about the fixed point $O$)} \\
> \mathbf 0 &= \mathbf R_O - \mathbf R_C - mg\,\mathbf j_0 \quad &\text{(Eq. 12.8 for the disk; $O$ at rest)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} 2m\,\mathbf a_0^G\cdot\mathbf i_0 = X + N_K\cos\varphi - k\left(R\cos\theta - L\sin\varphi\right), \qquad 2m\,\mathbf a_0^G\cdot\mathbf j_0 = Y + N_K\sin\varphi - 2mg \\ \frac{mL^2}{6}\,\ddot\varphi = \frac L2\left(X\cos\varphi + Y\sin\varphi\right) - \left(s - \frac L2\right)N_K + \frac{kL}{2}\left(R\cos\theta - L\sin\varphi\right)\cos\varphi \\ \frac{mR^2}{2}\,\ddot\theta = R\left(X\sin\theta - Y\cos\theta\right), \qquad \mathbf R_O = X\,\mathbf i_0 + \left(Y + mg\right)\mathbf j_0 \end{gathered}}$$
>
> **Units:** N in the force equations; N m in the moment equations
> **Meaning:** six scalar equations for six unknowns: the second rate of $\theta$ (those of $\varphi$ and the acceleration of $G$ follow from it by parts (b) and (c)), the two components of $\mathbf R_C$, the knob force and the two components of $\mathbf R_O$. Part (f) avoids solving them by an energy argument.

> [!derivation] Part (f): power of the reactions and of the force on A
> **Law:** power of a force on a body point; ideal pins; frictionless sliding contact; potential of a force proportional to a distance
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34; Notes.pdf, Eq. 9.3
>
> The bar point at $K$ (call it $K(B)$) is at the distance $s$ from $C$ along $\mathbf j_1$; its velocity follows from the bar field. The first derivative of the geometric relation (part (b)) is used in the last step.
>
> $$\begin{aligned}
> \dot W^{O} &= \mathbf R_O\cdot\mathbf v_0^O = \mathbf R_O\cdot\mathbf 0 = 0 \quad &\text{(pin at a fixed point)} \\
> \dot W^{C} &= \mathbf R_C\cdot\mathbf v_0^{C(B)} - \mathbf R_C\cdot\mathbf v_0^{C(D)} = \mathbf R_C\cdot\left(R\dot\theta\,\mathbf j_2 - R\dot\theta\,\mathbf j_2\right) = 0 \quad &\text{(pair at the pin; same velocity of $C$ on both bodies)} \\
> \mathbf v_0^{K(B)} &= \mathbf v_0^C + \dot\varphi\,\mathbf k_0\times s\,\mathbf j_1 = R\dot\theta\,\mathbf j_2 - s\dot\varphi\,\mathbf i_1 \quad &\text{(Eq. 9.3 from $C$)} \\
> \dot W^{K} &= N_K\,\mathbf i_1\cdot\mathbf v_0^{K(B)} = N_K\left(R\dot\theta\sin\left(\varphi - \theta\right) - s\dot\varphi\right) = N_K\left(s\dot\varphi - s\dot\varphi\right) = 0 \quad &\text{($\mathbf j_2\cdot\mathbf i_1$ from part (e); rate of $\varphi$ from part (b))} \\
> \dot W^{A} &= -k\,x_0^A\,\mathbf i_0\cdot\mathbf v_0^A = -k\,x_0^A\,\dot x_0^A = -\frac{d}{dt}\left(\frac k2\left(x_0^A\right)^2\right) \quad &\text{(first component of the velocity of $A$; chain rule)} \\
> \dot W^{g} &= -2mg\,\mathbf j_0\cdot\mathbf v_0^G - mg\,\mathbf j_0\cdot\mathbf 0 = -\frac{d}{dt}\left(2mg\,y_0^G\right) \quad &\text{(Eq. 12.34; disk weight at the fixed point $O$)}
> \end{aligned}$$
>
> $$\boxed{V = 2mg\left(R\sin\theta + \frac L2\cos\varphi\right) + \frac k2\left(R\cos\theta - L\sin\varphi\right)^2, \qquad \dot W^{O} = \dot W^{C} = \dot W^{K} = 0}$$
>
> **Units:** W in the powers; J in $V$
> **Meaning:** the knob does no work although the bar slides over it, because the bar point at $K$ moves along the groove and the knob force is normal to it; the rest of the reactions act at points with no relative motion.

> [!derivation] Part (f): equation of motion free of unknown reactions
> **Law:** energy theorem with workless constraints; initial conditions; Barrow's rule
> **Source:** Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.33
>
> Initial values: $\theta_0$ is zero and the rate of $\theta$ is zero. The first derivative of part (b) gives the initial rate of $\varphi$; the relation of part (b) with $\theta$ zero gives $\varphi_0$, with the hypotenuse $s_0$ equal to the square root of the sum of the squares of $R$ and $h$.
>
> $$\begin{aligned}
> \dot\varphi_0 &= \frac{R\left(R - h\sin 0\right)}{R^2 + h^2 - 2Rh\sin 0}\,\dot\theta_0 = \frac{R^2}{R^2 + h^2}\cdot 0 = 0 \quad &\text{(first rate of part (b) at the initial instant)} \\
> \sin\varphi_0 &= \frac{R}{\sqrt{R^2 + h^2}}, \qquad \cos\varphi_0 = \frac{h}{\sqrt{R^2 + h^2}} \quad &\text{(part (b) with $\theta$ zero)} \\
> \frac{d}{dt}\left(T^D + T^B + V\right) &= \dot W^{O} + \dot W^{C} + \dot W^{K} = 0 \quad &\text{(Eq. 12.29 summed over both bodies; previous box)} \\
> \left[T^D + T^B + V\right]_0^t &= 0 \;\Rightarrow\; T^D + T^B + V = \left(T^D + T^B + V\right)\big|_{t = 0} \quad &\text{(integrate from 0 to $t$; Barrow's rule)} \\
> \left(T^D + T^B + V\right)\big|_{t = 0} &= 0 + 2mg\,\frac L2\cdot\frac{h}{\sqrt{R^2 + h^2}} + \frac k2\left(R - \frac{LR}{\sqrt{R^2 + h^2}}\right)^2 \quad &\text{(zero rates; sine of 0 is 0, cosine of 0 is 1)}
> \end{aligned}$$
>
> $$\boxed{\frac54\,mR^2\dot\theta^2 + \frac{mL^2}{3}\,\dot\varphi^2 - mRL\,\dot\theta\dot\varphi\sin(\varphi - \theta) + 2mgR\sin\theta + mgL\cos\varphi + \frac k2\left(R\cos\theta - L\sin\varphi\right)^2 = \frac{mgLh}{\sqrt{R^2 + h^2}} + \frac{kR^2}{2}\left(1 - \frac{L}{\sqrt{R^2 + h^2}}\right)^2}$$
>
> **Units:** J in every term
> **Meaning:** one equation in $\theta$, $\varphi$ and their rates, with no reaction in it; with the relation of part (b) and its first derivative it becomes a first order equation in $\theta$ alone, which can be separated and integrated.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom | One ($\theta$): six planar coordinates minus two pins (two equations each) minus the knob (one) |
| (b) Relation and rates | $\tan\varphi = R\cos\theta/(h - R\sin\theta)$; $\dot\varphi = \dfrac{R(R - h\sin\theta)}{R^2 + h^2 - 2Rh\sin\theta}\dot\theta$; $\ddot\varphi = \dfrac{R(R - h\sin\theta)}{R^2 + h^2 - 2Rh\sin\theta}\ddot\theta + \dfrac{Rh(R^2 - h^2)\cos\theta}{(R^2 + h^2 - 2Rh\sin\theta)^2}\dot\theta^2$ |
| (c) Kinematics of $A$ and $G$ | $\mathbf r_0^A = (R\cos\theta - L\sin\varphi)\,\mathbf i_0 + (R\sin\theta + L\cos\varphi)\,\mathbf j_0$; $\mathbf v_0^A = R\dot\theta\,\mathbf j_2 - L\dot\varphi\,\mathbf i_1$; $\mathbf a_0^A = R\ddot\theta\,\mathbf j_2 - R\dot\theta^2\,\mathbf i_2 - L\ddot\varphi\,\mathbf i_1 - L\dot\varphi^2\,\mathbf j_1$; the same for $G$ with $L/2$ in place of $L$; $\mathbf i_2 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$, $\mathbf j_2 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$, $\mathbf i_1 = \cos\varphi\,\mathbf i_0 + \sin\varphi\,\mathbf j_0$, $\mathbf j_1 = -\sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0$ |
| (d) Forces | Disk: $-mg\,\mathbf j_0$ and $\mathbf R_O$ at $O$, $-\mathbf R_C$ at $C$. Bar: $\mathbf R_C$ at $C$, $-2mg\,\mathbf j_0$ at $G$, $N_K\,\mathbf i_1$ at $K$, $\mathbf F_A = -k(R\cos\theta - L\sin\varphi)\,\mathbf i_0$ at $A$; six equations of the bar and the disk in the boxes above |
| (e) Kinetic energies | $T^D = \tfrac{mR^2}{4}\dot\theta^2$; $T^B = mR^2\dot\theta^2 + \tfrac{mL^2}{3}\dot\varphi^2 - mRL\dot\theta\dot\varphi\sin(\varphi - \theta)$ |
| (f) Equation free of unknowns | $\tfrac54 mR^2\dot\theta^2 + \tfrac{mL^2}{3}\dot\varphi^2 - mRL\dot\theta\dot\varphi\sin(\varphi - \theta) + 2mgR\sin\theta + mgL\cos\varphi + \tfrac k2(R\cos\theta - L\sin\varphi)^2 = \tfrac{mgLh}{\sqrt{R^2 + h^2}} + \tfrac{kR^2}{2}\left(1 - \tfrac{L}{\sqrt{R^2 + h^2}}\right)^2$ |

**Limiting cases and consistency:** the key prints no answer for this problem (Problems.pdf, pp. 77 to 81 checked).

* **Bar tangent to the disk.** Where the sine of $\theta$ equals $R/h$, part (b) gives a zero rate of $\varphi$: the bar is then tangent to the disk at $C$ (shown in the Meaning line of part (b)), so $C$ moves along the line of the bar and the bar slides over the knob without turning. In the same configuration $\varphi$ equals $\theta$ and the cross term of part (e) vanishes, consistently.
* **Bar vertical.** With $\theta$ equal to $\pi/2$, $C$ is right below $K$ and part (b) gives $\varphi$ zero, with the distance $s$ equal to the difference of $h$ and $R$.
* **No pull on A.** With $k$ zero the spring terms disappear on both sides of part (f); the force on $A$ enters only through its potential, as the power box shows.
* **Dimensions.** Every term of the energy equation is an energy: $mR^2$ times a squared rate, $mgR$, and $k$ times a squared length.

---

## Problem RB-31: Ball bearing between cylinder and cone

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** three bodies. The ball $b$, homogeneous and solid, of mass $m$, radius $R$ and centre $A$; the cone $c$, homogeneous and solid, of mass $2m$, half-angle $\beta$, base radius $2R$ and centre of mass $G$ on its axis; the cylindrical frame $d$, of inner radius $3R$ with a flat bottom, at rest. The ball touches the bottom of the frame at $Q$, the wall of the frame at $P$ and the cone at $I$; the friction coefficient at the three contacts is $\mu$, and no contact transmits a torque (the ball pivots freely).
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, with $\mathbf k_0$ along the common axis of the cone and of the frame, upwards, and $O$ on that axis at the height of $A$ (read from the figure: the axis $Ox_1$ passes through $A$ and $P$). Gravity is $-g\,\mathbf k_0$. The frame $d$ is at rest, so $S_0$ is inertial.
* **Frame of the ball centre:** $S_1\{O; \mathcal B_1\}$, turned by $\theta$ about $\mathbf k_0$, with $\mathbf i_1$ towards $A$, $\mathbf j_1$ horizontal and normal to it, $\mathbf k_1$ equal to $\mathbf k_0$.
* **Cone frame:** $S_c\{O; \mathcal B_c\}$, attached to the cone, turned by $\phi$ about $\mathbf k_0$. Both angles are positive counterclockwise as seen from above, as the statement says.
* **Geometry, read from the figure:** $P$ lies on $Ox_1$ on the wall, so $A$ is at the distance $3R - R$, that is $2R$, from the axis; $Q$ lies right below $A$, so the bottom of the frame is at the depth $R$ below $O$; $I$ lies on a generatrix of the cone, in the meridian plane $Ox_1z_1$, above and to the left of $A$.
* **Support of the cone, read from the statement:** the only constraint written is that the axis of the cone coincides with $Oz_0$. It is taken as an ideal cylindrical joint: it lets the cone turn about $\mathbf k_0$ and slide along it, and it exerts a force normal to the axis and a moment normal to the axis, but no axial force and no axial moment. The height of the cone is then held by the ball. If the support also held the cone axially, it would add one unknown (the axial force) and the contact with the cone would become a redundant geometric condition; the counts below change as stated where they are made.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass and radius of the ball | $m$, $R$ | kg, m |
| Mass, half-angle and base radius of the cone | $2m$, $\beta$, $2R$ | kg, rad, m |
| Inner radius of the frame | $3R$ | m |
| Position of the ball centre | $\mathbf r_0^A = 2R\,\mathbf i_1$ | m |
| Height of the centre of mass of the cone above $O$ | $z_G$ (fixed by the geometry) | m |
| Moment of the ball about any diameter (statement; integral below) | $\tfrac25 mR^2$ | kg m$^2$ |
| Moment of the cone about its axis (statement; integral below) | $\tfrac{12}{5} mR^2$ | kg m$^2$ |
| Friction coefficient at $I$, $P$, $Q$ | $\mu$ | - |
| Gravity | $-g\,\mathbf k_0$ | m/s$^2$ |

![[attachments/EM-SOL/rb31-meridian.svg]]

> [!derivation] Contact points in the meridian plane
> **Law:** geometry of tangent contact: the contact point lies on the line of centres along the common normal; right triangle of the generatrix
> **Source:** Notes.pdf, Sec. 13.2; Problems.pdf, p. 61
>
> Meridian plane $Ox_1z_1$ seen with $\mathbf i_1$ to the right and $\mathbf k_1$ up; the product of $\mathbf k_1$ and $\mathbf i_1$ is $\mathbf j_1$, so $\mathbf j_1$ points into the paper (⊗). The generatrix through $I$ makes the angle $\beta$ with the axis. Triangle of its upward unit tangent $\mathbf e_t$: hypotenuse 1 along the generatrix, adjacent leg along $\mathbf k_1$ (cosine of $\beta$), opposite leg along $\mathbf i_1$ (sine). The unit normal $\mathbf n$ of the cone surface, pointing out of the cone towards the ball, is $\mathbf e_t$ turned by a right angle clockwise in this view: adjacent leg along $\mathbf i_1$ (cosine), opposite leg along minus $\mathbf k_1$ (sine), because the outward normal of a cone that opens upwards points away from the axis and down.
>
> $$\begin{aligned}
> \mathbf e_t &= \sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf k_1, \qquad \mathbf n = \cos\beta\,\mathbf i_1 - \sin\beta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> \mathbf n\cdot\mathbf e_t &= \cos\beta\sin\beta - \sin\beta\cos\beta = 0 \quad &\text{(the two are orthogonal)} \\
> \mathbf r_0^Q &= \mathbf r_0^A - R\,\mathbf k_1 = 2R\,\mathbf i_1 - R\,\mathbf k_1 \quad &\text{(common normal of the bottom: $\mathbf k_1$)} \\
> \mathbf r_0^P &= \mathbf r_0^A + R\,\mathbf i_1 = 3R\,\mathbf i_1 \quad &\text{(common normal of the wall: $\mathbf i_1$)} \\
> \mathbf r_0^I &= \mathbf r_0^A - R\,\mathbf n = R\left(2 - \cos\beta\right)\mathbf i_1 + R\sin\beta\,\mathbf k_1 \quad &\text{(common normal of the cone: $\mathbf n$)}
> \end{aligned}$$
>
> $$\boxed{\overrightarrow{AQ} = -R\,\mathbf k_1, \qquad \overrightarrow{AP} = R\,\mathbf i_1, \qquad \overrightarrow{AI} = -R\cos\beta\,\mathbf i_1 + R\sin\beta\,\mathbf k_1, \qquad \mathbf r_0^I = R\left(2 - \cos\beta\right)\mathbf i_1 + R\sin\beta\,\mathbf k_1}$$
>
> **Units:** $[\mathrm L]$; the unit vectors are dimensionless
> **Meaning:** $I$ is at the distance $R(2 - \cos\beta)$ from the axis, less than $2R$, and at the height $R\sin\beta$ above $A$, as drawn: up and to the left of the centre of the ball.

#### Part (a): degrees of freedom with no friction

The second limit (infinite friction) needs the kinematics of parts (c) and (d), so it is answered after them, in the box "Part (a), second limit".

> [!derivation] Part (a), first limit: degrees of freedom when the coefficient of friction is zero
> **Law:** six coordinates per free rigid body; one geometric equation per contact without friction (no penetration, Eq. 13.1)
> **Source:** Notes.pdf, Sec. 13.1; Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 14.1
>
> Without friction a contact only forbids penetration: one scalar equation among the coordinates per contact. The ball has the three coordinates of $A$ and three angles; the cone, held by the cylindrical joint, keeps the angle $\phi$ and its height along the axis.
>
> $$\begin{aligned}
> n_q &= 6 + 2 = 8 \quad &\text{(ball: position of $A$ and three angles; cone: $\phi$ and its height)} \\
> n_c &= 1 + 1 + 1 = 3 \quad &\text{($Q$: height of $A$; $P$: distance of $A$ to the axis; $I$: height of the cone)} \\
> n_{\mathrm{dof}} &= n_q - n_c = 8 - 3 = 5 \quad &\text{(the three equations are independent)}
> \end{aligned}$$
>
> $$\boxed{\mu \to 0:\quad n_{\mathrm{dof}} = 5,\qquad \text{coordinates } \theta,\ \text{three angles of the ball},\ \phi}$$
>
> **Units:** dimensionless counts
> **Meaning:** the centre of the ball can only run round the circle of radius $2R$ at the height of $O$; the ball can turn in any way about its centre, and the cone can turn on its own, because no friction couples the rotations. With the other reading of the support (cone held axially) the count is seven coordinates minus the two independent equations at $Q$ and $P$, the contact at $I$ being then a redundant consequence of the geometry: five as well.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb31-rot-theta.svg]]

> [!derivation] Frame of the ball centre and cone frame: rotations about k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View from above with $\mathbf k_0$ out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up: a positive angle turns counterclockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\theta$), opposite leg along $\mathbf j_0$ (sine). Triangle of $\mathbf j_1$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine), because the counterclockwise turn carries the tip of $\mathbf j_0$ to the left. The cone basis is built in the same way with $\phi$.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$; $[{}_0R_c]$ has the same form with $\phi$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta & 0 \cr \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products; the same with $\phi$)} \\
> \boldsymbol\omega_{10} &= \dot\theta\,\mathbf k_0, \qquad \boldsymbol\omega_{c0} = \dot\phi\,\mathbf k_0 \quad &\text{(rates of the angles along their axis)} \\
> \dot{\mathbf i}_1 &= \dot\theta\,\mathbf k_0\times\mathbf i_1 = \dot\theta\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = \dot\theta\,\mathbf k_0\times\mathbf j_1 = -\dot\theta\,\mathbf i_1, \qquad \dot{\mathbf k}_1 = \mathbf 0 \quad &\text{(Poisson, Eq. 9.4)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0, \quad \mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0, \quad \boldsymbol\omega_{10} = \dot\theta\,\mathbf k_0, \quad \boldsymbol\omega_{c0} = \dot\phi\,\mathbf k_0, \quad \dot{\mathbf i}_1 = \dot\theta\,\mathbf j_1, \quad \dot{\mathbf j}_1 = -\dot\theta\,\mathbf i_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** $S_1$ follows the centre of the ball round the axis; in it the points $A$, $P$, $Q$ and $I$ have fixed coordinates.

> [!derivation] Part (b): position, velocity and acceleration of A
> **Law:** position vector in a moving basis; derivative with Poisson's formula and the product rule; check by the components in the fixed basis and the chain rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 3.8
>
> $$\begin{aligned}
> \mathbf r_0^A &= 2R\,\mathbf i_1 = 2R\cos\theta\,\mathbf i_0 + 2R\sin\theta\,\mathbf j_0 \quad &\text{(distance $2R$ from the axis, at the height of $O$)} \\
> \mathbf v_0^A &= 2R\,\dot{\mathbf i}_1 = 2R\dot\theta\,\mathbf j_1 \quad &\text{($R$ constant; Poisson)} \\
> \frac{d}{dt}\left(2R\cos\theta\right) &= -2R\sin\theta\,\dot\theta, \qquad \frac{d}{dt}\left(2R\sin\theta\right) = 2R\cos\theta\,\dot\theta \quad &\text{(chain rule on the fixed components: the same vector)} \\
> \mathbf a_0^A &= 2R\ddot\theta\,\mathbf j_1 + 2R\dot\theta\,\dot{\mathbf j}_1 = 2R\ddot\theta\,\mathbf j_1 - 2R\dot\theta^2\,\mathbf i_1 \quad &\text{(product rule; Poisson)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_0^A = 2R\,\mathbf i_1 = 2R\left(\cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0\right), \qquad \mathbf v_0^A = 2R\dot\theta\,\mathbf j_1 = 2R\dot\theta\left(-\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0\right) \\ \mathbf a_0^A = -2R\dot\theta^2\,\mathbf i_1 + 2R\ddot\theta\,\mathbf j_1 = -2R\left(\dot\theta^2\cos\theta + \ddot\theta\sin\theta\right)\mathbf i_0 + 2R\left(\ddot\theta\cos\theta - \dot\theta^2\sin\theta\right)\mathbf j_0 \end{gathered}}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm L][\mathrm{T^{-1}}]$; $[\mathrm L][\mathrm{T^{-2}}]$
> **Meaning:** these hold with or without friction, since they only use the contacts at $Q$ and $P$: the centre runs on a horizontal circle of radius $2R$; the acceleration has a tangential part from the second rate of $\theta$ and a part towards the axis from the square of the first rate.

#### Parts (c) and (d): rolling without slip

> [!derivation] Part (c): no slip at Q and P
> **Law:** velocity field of the ball; rolling without slipping on a body at rest; vector products by determinants
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> Write the angular velocity of the ball in $\mathcal B_1$ with three unknown components. The frame is at rest, so the ball points at $Q$ and at $P$ have zero velocity (Eq. 13.5). The normal component of each condition (along $\mathbf k_1$ at $Q$, along $\mathbf i_1$ at $P$) holds already by part (b); the other two components of each are new.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \omega_1\,\mathbf i_1 + \omega_2\,\mathbf j_1 + \omega_3\,\mathbf k_1 \quad &\text{(unknown components)} \\
> \boldsymbol\omega_{b0}\times\overrightarrow{AQ} &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \omega_1 & \omega_2 & \omega_3 \cr 0 & 0 & -R \end{vmatrix} = -R\omega_2\,\mathbf i_1 + R\omega_1\,\mathbf j_1 \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{Q(b)} &= 2R\dot\theta\,\mathbf j_1 - R\omega_2\,\mathbf i_1 + R\omega_1\,\mathbf j_1 = \mathbf 0 \quad &\text{(Eq. 9.3 from $A$; no slip on the bottom)} \\
> \boldsymbol\omega_{b0}\times\overrightarrow{AP} &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \omega_1 & \omega_2 & \omega_3 \cr R & 0 & 0 \end{vmatrix} = R\omega_3\,\mathbf j_1 - R\omega_2\,\mathbf k_1 \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{P(b)} &= 2R\dot\theta\,\mathbf j_1 + R\omega_3\,\mathbf j_1 - R\omega_2\,\mathbf k_1 = \mathbf 0 \quad &\text{(Eq. 9.3 from $A$; no slip on the wall)} \\
> \omega_2 &= 0 \ \text{(twice)}, \qquad \omega_1 = -2\dot\theta, \qquad \omega_3 = -2\dot\theta \quad &\text{(the four scalar conditions; one repeats)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = -2\dot\theta\left(\mathbf i_1 + \mathbf k_1\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** four scalar conditions, only three independent: a turn of the ball about $\mathbf j_1$ would move both $Q$ and $P$ tangentially, and both conditions forbid it. With a positive rate of $\theta$ the ball rolls along the bottom towards plus $\mathbf j_1$, so it turns about minus $\mathbf i_1$, and along the wall, so it turns about minus $\mathbf k_1$, as the signs of the box show.

> [!derivation] Part (c): instantaneous axis of rotation and angular acceleration of the ball
> **Law:** points of zero velocity of a rigid body; derivative of a vector written in a moving basis (product rule, Poisson)
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.4
>
> $Q$ and $P$ have zero velocity, so every point $X$ of the line through them, with $\overrightarrow{QX}$ equal to $\lambda(\mathbf i_1 + \mathbf k_1)$, has the velocity below, zero because the angular velocity is parallel to the line.
>
> $$\begin{aligned}
> \mathbf v_0^{X} &= \mathbf v_0^{Q(b)} + \boldsymbol\omega_{b0}\times\lambda\left(\mathbf i_1 + \mathbf k_1\right) = \mathbf 0 - 2\dot\theta\lambda\left(\mathbf i_1 + \mathbf k_1\right)\times\left(\mathbf i_1 + \mathbf k_1\right) = \mathbf 0 \quad &\text{(Eq. 9.3 from $Q$; product of parallel vectors)} \\
> \mathbf r_0^{X} &= \left(2R + \lambda\right)\mathbf i_1 + \left(\lambda - R\right)\mathbf k_1 \quad &\text{(points of the axis)} \\
> \mathbf r_0^{X}\big|_{\lambda = -2R} &= -3R\,\mathbf k_1 \quad &\text{(the axis meets $Oz_0$)} \\
> \boldsymbol\alpha_{b0} &= \frac{d}{dt}\left(-2\dot\theta\right)\left(\mathbf i_1 + \mathbf k_1\right) - 2\dot\theta\left(\dot{\mathbf i}_1 + \dot{\mathbf k}_1\right) \quad &\text{(product rule)} \\
> &= -2\ddot\theta\left(\mathbf i_1 + \mathbf k_1\right) - 2\dot\theta\left(\dot\theta\,\mathbf j_1 + \mathbf 0\right) \quad &\text{(Poisson for $\mathbf i_1$; $\mathbf k_1$ fixed)}
> \end{aligned}$$
>
> $$\boxed{\text{IAR: line } PQ,\ \ \mathbf r_0^X = 2R\,\mathbf i_1 - R\,\mathbf k_1 + \lambda\left(\mathbf i_1 + \mathbf k_1\right); \qquad \boldsymbol\omega_{b0} = -2\dot\theta\left(\mathbf i_1 + \mathbf k_1\right), \qquad \boldsymbol\alpha_{b0} = -2\ddot\theta\left(\mathbf i_1 + \mathbf k_1\right) - 2\dot\theta^2\,\mathbf j_1}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{T^{-1}}]$; $[\mathrm{T^{-2}}]$
> **Meaning:** the instantaneous axis is the line of the two contacts with the frame, at 45 degrees in the meridian plane; it turns with $S_1$ and always passes through the axis point at the depth $3R$ below $O$. Points on it have zero velocity (no sliding along the axis either). Even at a constant rate of $\theta$ the angular acceleration is not zero: the direction of the angular velocity turns with the meridian plane.

> [!derivation] Part (d): no slip at I and the relation between the rates
> **Law:** velocity fields of the ball and of the cone; rolling without slipping between two moving bodies
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.2; Notes.pdf, Sec. 13.2
>
> The cone turns about the fixed axis, so its point at $I$ moves with the field from $O$. The tangent plane at $I$ is spanned by $\mathbf j_1$ and the generatrix $\mathbf e_t$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0}\times\overrightarrow{AI} &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr -2\dot\theta & 0 & -2\dot\theta \cr -R\cos\beta & 0 & R\sin\beta \end{vmatrix} = -\mathbf j_1\left(-2R\dot\theta\sin\beta - 2R\dot\theta\cos\beta\right) \quad &\text{(expand along the first row; the other two minors vanish)} \\
> \mathbf v_0^{I(b)} &= 2R\dot\theta\,\mathbf j_1 + 2R\dot\theta\left(\sin\beta + \cos\beta\right)\mathbf j_1 = 2R\dot\theta\left(1 + \sin\beta + \cos\beta\right)\mathbf j_1 \quad &\text{(Eq. 9.3 from $A$)} \\
> \mathbf v_0^{I(c)} &= \dot\phi\,\mathbf k_1\times\left(R\left(2 - \cos\beta\right)\mathbf i_1 + R\sin\beta\,\mathbf k_1\right) = R\left(2 - \cos\beta\right)\dot\phi\,\mathbf j_1 \quad &\text{(Eq. 9.3 from $O$; $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> \left(\mathbf v_0^{I(b)} - \mathbf v_0^{I(c)}\right)\cdot\mathbf e_t &= 0 - 0 = 0 \quad &\text{(both are along $\mathbf j_1$: identically satisfied)} \\
> \left(\mathbf v_0^{I(b)} - \mathbf v_0^{I(c)}\right)\cdot\mathbf j_1 &= 2R\dot\theta\left(1 + \sin\beta + \cos\beta\right) - R\left(2 - \cos\beta\right)\dot\phi = 0 \quad &\text{(no slip, Eq. 13.2)} \\
> \left[\phi\right]_{\phi_0}^{\phi} &= \kappa\left[\theta\right]_{\theta_0}^{\theta} \;\Rightarrow\; \phi - \phi_0 = \kappa\left(\theta - \theta_0\right) \quad &\text{(integrate the relation from $0$ to $t$ with constant $\kappa$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\dot\phi = \kappa\,\dot\theta, \qquad \kappa = \frac{2\left(1 + \sin\beta + \cos\beta\right)}{2 - \cos\beta}, \qquad \ddot\phi = \kappa\,\ddot\theta}$$
>
> **Units:** dimensionless ratio of two rates, $[\mathrm{T^{-1}}]$ on both sides
> **Meaning:** the cone turns in the same sense as the centre of the ball and faster: $\kappa$ is positive, and for $\beta$ equal to 30 degrees it is $2(1 + 0.5 + 0.866)/(2 - 0.866)$, about 4.17. The normal component of the condition is the contact itself, already imposed by the geometry.

> [!derivation] Part (a), second limit: degrees of freedom when the coefficient of friction is infinite
> **Law:** independent velocities minus independent no-slip conditions; integrability of the conditions; composition of angular velocities
> **Source:** Notes.pdf, Sec. 14.1; Notes.pdf, Sec. 13.2; Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.14
>
> With infinite friction nothing slips at $I$, $P$ or $Q$. The five velocities of the first limit are the rate of $\theta$, the three components of the angular velocity of the ball and the rate of $\phi$. The previous boxes give three independent conditions at $Q$ and $P$ and one at $I$. To see whether the conditions can be integrated, take the angular velocity of the ball relative to $S_1$, in which $A$ is fixed.
>
> $$\begin{aligned}
> n_{\mathrm{dof}} &= 5 - \left(3 + 1\right) = 1 \quad &\text{(independent velocities minus independent conditions)} \\
> \boldsymbol\omega_{b1} &= \boldsymbol\omega_{b0} - \boldsymbol\omega_{10} = -2\dot\theta\,\mathbf i_1 - 2\dot\theta\,\mathbf k_1 - \dot\theta\,\mathbf k_1 = -\dot\theta\left(2\,\mathbf i_1 + 3\,\mathbf k_1\right) \quad &\text{(composition, Eq. 9.21)} \\
> \int_0^t -\sqrt{13}\,\dot\theta\,dt' &= -\sqrt{13}\int_{\theta_0}^{\theta} d\theta' = -\sqrt{13}\left[\theta'\right]_{\theta_0}^{\theta} = -\sqrt{13}\left(\theta - \theta_0\right) \quad &\text{(substitution with $d\theta' = \dot\theta\,dt'$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\mu \to \infty:\quad n_{\mathrm{dof}} = 1,\ \text{coordinate } \theta}$$
>
> **Units:** dimensionless counts; $[\mathrm{T^{-1}}]$ for the angular velocity
> **Meaning:** relative to $S_1$ the ball turns about a line through the fixed point $A$ with the fixed direction of $2\,\mathbf i_1$ plus $3\,\mathbf k_1$ (norm the square root of 13), by the angle of the last row: its attitude, like $\phi$ by part (d), is a function of $\theta$. The conditions are integrable, so one coordinate is enough. With the other reading of the support the cone contact adds nothing, and the count is the same.

### Center of Mass and Inertia Tensor

> [!derivation] Inertia of the ball about its centre
> **Law:** moments and products of inertia as volume integrals in spherical coordinates (jacobian $r^2\sin\vartheta$); symmetry
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; [Lecture 8, Slide 16]
>
> Spherical coordinates about $A$: $r$ from 0 to $R$, polar angle $\vartheta$ from 0 to $\pi$ measured from an arbitrary diameter, azimuth $\chi$ from 0 to $2\pi$; density $\rho$; the squared distance to that diameter is $r^2\sin^2\vartheta$. The centre of mass is $A$ and the products of inertia vanish, because the integrands of the first moments and of the products are odd under the reflections that leave the ball invariant.
>
> $$\begin{aligned}
> m &= \rho\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^R r^2\sin\vartheta\,dr\,d\vartheta\,d\chi = \rho\left[\chi\right]_0^{2\pi}\left[-\cos\vartheta\right]_0^{\pi}\left[\frac{r^3}{3}\right]_0^R = \rho\cdot 2\pi\cdot 2\cdot\frac{R^3}{3} = \frac{4\pi\rho R^3}{3} \quad &\text{(antiderivatives; Barrow's rule)} \\
> \int_0^{\pi}\sin^3\vartheta\,d\vartheta &= \left[-\cos\vartheta + \frac{\cos^3\vartheta}{3}\right]_0^{\pi} = \left(1 - \frac13\right) - \left(-1 + \frac13\right) = \frac43 \quad &\text{(antiderivative; Barrow's rule)} \\
> I &= \rho\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^R r^2\sin^2\vartheta\,r^2\sin\vartheta\,dr\,d\vartheta\,d\chi = \rho\cdot 2\pi\cdot\frac43\cdot\left[\frac{r^5}{5}\right]_0^R = \frac{8\pi\rho R^5}{15} \quad &\text{(squared distance times the element)} \\
> \frac{I}{m} &= \frac{8\pi\rho R^5/15}{4\pi\rho R^3/3} = \frac{2R^2}{5} \quad &\text{(divide)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}_A^{\,b} = \frac25 mR^2\,[U] \ \text{in any basis}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the value of the statement. Every diameter is principal with the same moment, so the angular momentum of the ball about $A$ is parallel to its angular velocity.

> [!derivation] Inertia of the cone about its axis
> **Law:** moment of inertia as a volume integral in cylindrical coordinates (jacobian $\varrho$); symmetry of revolution
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.6; Notes.pdf, Eq. 10.41; [Lecture 8, Slide 16]
>
> Height of the cone $h_c$, apex at $\zeta$ equal to 0 and base at $h_c$; the section at the height $\zeta$ is a disc of radius $a(\zeta)$, equal to $2R\zeta/h_c$ (similar triangles with the base). Cylindrical coordinates $(\varrho, \chi, \zeta)$, element $\varrho\,d\varrho\,d\chi\,d\zeta$, density $\rho_c$. $G$ lies on the axis and the products of inertia with the axis vanish, by the symmetry of revolution.
>
> $$\begin{aligned}
> 2m &= \rho_c\int_0^{h_c}\!\!\int_0^{2\pi}\!\!\int_0^{a(\zeta)}\varrho\,d\varrho\,d\chi\,d\zeta = \rho_c\int_0^{h_c}\pi\,\frac{4R^2\zeta^2}{h_c^2}\,d\zeta = \rho_c\,\frac{4\pi R^2}{h_c^2}\left[\frac{\zeta^3}{3}\right]_0^{h_c} = \frac{4\pi\rho_c R^2 h_c}{3} \quad &\text{(inner integrals; antiderivative; Barrow's rule)} \\
> I_c &= \rho_c\int_0^{h_c}\!\!\int_0^{2\pi}\!\!\int_0^{a(\zeta)}\varrho^2\,\varrho\,d\varrho\,d\chi\,d\zeta = \rho_c\int_0^{h_c}2\pi\,\frac{16R^4\zeta^4}{4h_c^4}\,d\zeta = \rho_c\,\frac{8\pi R^4}{h_c^4}\left[\frac{\zeta^5}{5}\right]_0^{h_c} = \frac{8\pi\rho_c R^4 h_c}{5} \quad &\text{(squared distance $\varrho^2$; Barrow's rule)} \\
> \frac{I_c}{2m} &= \frac{8\pi\rho_c R^4 h_c/5}{4\pi\rho_c R^2 h_c/3} = \frac{6R^2}{5} \quad &\text{(divide)}
> \end{aligned}$$
>
> $$\boxed{I_c = \frac{12}{5}\,mR^2 \ \text{about } \mathbf k_0, \ \text{a principal axis of the cone}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the value of the statement, independent of the height of the cone. Only this moment enters the equations, because the cone only turns about its axis.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momenta and rates of the ball and of the cone
> **Law:** linear momentum; angular momentum about the centre of mass; derivative in $S_0$ of a vector known in a moving basis (gyroscopic term)
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 12.20; Notes.pdf, Eq. 12.21
>
> The centre of mass of the cone stays at rest: it is on the fixed axis and the ball holds its height. The cone turns about its symmetry axis, so its angular velocity has no transverse component and its angular momentum is along $\mathbf k_0$.
>
> $$\begin{aligned}
> \mathbf p_0^b &= m\,\mathbf v_0^A = 2mR\dot\theta\,\mathbf j_1, \qquad \mathbf p_0^c = 2m\,\mathbf v_0^G = \mathbf 0 \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{A,0}^b &= \bar{\bar I}_A^{\,b}\cdot\boldsymbol\omega_{b0} = \frac25 mR^2\left(-2\dot\theta\right)\left(\mathbf i_1 + \mathbf k_1\right) \quad &\text{(Eq. 11.12; isotropic tensor)} \\
> \left.\frac{d\mathbf H_{A,0}^b}{dt}\right|_0 &= \bar{\bar I}_A^{\,b}\cdot\boldsymbol\alpha_{b0} + \boldsymbol\omega_{b0}\times\left(\frac25 mR^2\,\boldsymbol\omega_{b0}\right) = \frac25 mR^2\,\boldsymbol\alpha_{b0} + \mathbf 0 \quad &\text{(Eq. 12.21; product of parallel vectors)} \\
> &= \frac25 mR^2\left(-2\ddot\theta\,\mathbf i_1 - 2\dot\theta^2\,\mathbf j_1 - 2\ddot\theta\,\mathbf k_1\right) \quad &\text{(part (c))} \\
> \mathbf H_{G,0}^c &= I_c\,\dot\phi\,\mathbf k_0 = \frac{12}{5} mR^2\kappa\,\dot\theta\,\mathbf k_0, \qquad \left.\frac{d\mathbf H_{G,0}^c}{dt}\right|_0 = \frac{12}{5} mR^2\kappa\,\ddot\theta\,\mathbf k_0 \quad &\text{(Eq. 11.12; $\mathbf k_0$ fixed; part (d))}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}^b}{dt}\right|_0 = -\frac45 mR^2\left(\ddot\theta\,\mathbf i_1 + \dot\theta^2\,\mathbf j_1 + \ddot\theta\,\mathbf k_1\right), \qquad \left.\frac{d\mathbf H_{G,0}^c}{dt}\right|_0 = \frac{12}{5} mR^2\kappa\,\ddot\theta\,\mathbf k_0}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, N m
> **Meaning:** the gyroscopic term of the ball vanishes because its tensor is isotropic, yet a moment along minus $\mathbf j_1$ is needed even at a constant rate of $\theta$, to turn the angular momentum of the ball with the meridian plane.

> [!derivation] Kinetic energy of the system
> **Law:** Koenig's theorem for the ball; rotation about a fixed axis for the cone
> **Source:** Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 11.32; [Lecture 9, Slide 9]
>
> $$\begin{aligned}
> T^b &= \frac12 m\left(2R\dot\theta\right)^2 + \frac12\cdot\frac25 mR^2\left(\left(-2\dot\theta\right)^2 + \left(-2\dot\theta\right)^2\right) = 2mR^2\dot\theta^2 + \frac85 mR^2\dot\theta^2 \quad &\text{(Eq. 11.31)} \\
> T^c &= \frac12\cdot\frac{12}{5} mR^2\dot\phi^2 = \frac65 mR^2\kappa^2\dot\theta^2 \quad &\text{(Eq. 11.32; part (d))}
> \end{aligned}$$
>
> $$\boxed{T = T^b + T^c = \frac{6}{5}\,mR^2\left(3 + \kappa^2\right)\dot\theta^2}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, J
> **Meaning:** the energy of the whole bearing is fixed by the rate of $\theta$ alone, as expected with one degree of freedom; it is used in part (f) as a check.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb31-exploded.svg]]

#### Part (e): forces on the ball

The exploded view separates the ball, the cone and the frame. Each contact force acts at the contact point, with the opposite force on the other body (third law of Newton); no contact torque acts, because the ball pivots freely. Without slip, each contact force has three unknown components: the normal one, which points into the ball, and two of friction in the tangent plane (Notes.pdf, Sec. 13.2). The cylindrical joint acts on the cone with a force normal to the axis and a moment normal to the axis, reduced at $G$.

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the ball | $b$ | $A$ | $-mg\,\mathbf k_1$ | applied |
| Bottom of the frame on the ball | $b$ | $Q$ | $\mathbf F_Q = F_{Qx}\,\mathbf i_1 + F_{Qy}\,\mathbf j_1 + N_Q\,\mathbf k_1$ | constraint: normal $N_Q$, friction $F_{Qx}$, $F_{Qy}$ |
| Wall of the frame on the ball | $b$ | $P$ | $\mathbf F_P = -N_P\,\mathbf i_1 + F_{Py}\,\mathbf j_1 + F_{Pz}\,\mathbf k_1$ | constraint: normal $N_P$, friction $F_{Py}$, $F_{Pz}$ |
| Cone on the ball | $b$ | $I$ | $\mathbf F_I = N_I\,\mathbf n + F_{Ij}\,\mathbf j_1 + F_{It}\,\mathbf e_t$ | constraint (pair): normal $N_I$, friction $F_{Ij}$, $F_{It}$ |
| Ball on the cone | $c$ | $I$ | $-\mathbf F_I$ | constraint (pair) |
| Weight of the cone | $c$ | $G$ | $-2mg\,\mathbf k_1$ | applied |
| Joint on the cone | $c$ | $G$ | $X\,\mathbf i_1 + Y\,\mathbf j_1$ and moment $M_x\,\mathbf i_1 + M_y\,\mathbf j_1$ | constraint |
| Ball on the frame | $d$ | $Q$, $P$ | $-\mathbf F_Q$, $-\mathbf F_P$ | constraint (pairs) |

> [!derivation] Part (e): resultant force and moment about A of the loads on the ball
> **Law:** sum of forces; moment of a force about a point; vector products by determinants
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 6.6
>
> In $\mathcal B_1$ the force at $I$ has the components $N_I\cos\beta + F_{It}\sin\beta$, $F_{Ij}$ and $-N_I\sin\beta + F_{It}\cos\beta$ (the triangles of $\mathbf n$ and $\mathbf e_t$). The normal forces act along the lines $QA$, $PA$ and $IA$, so their arms about $A$ are parallel to them and their moments vanish; the weight acts at $A$.
>
> $$\begin{aligned}
> \mathbf F^b &= \left(F_{Qx} - N_P + N_I\cos\beta + F_{It}\sin\beta\right)\mathbf i_1 + \left(F_{Qy} + F_{Py} + F_{Ij}\right)\mathbf j_1 + \left(N_Q - mg + F_{Pz} - N_I\sin\beta + F_{It}\cos\beta\right)\mathbf k_1 \quad &\text{(sum of the four forces)} \\
> \overrightarrow{AQ}\times\mathbf F_Q &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr 0 & 0 & -R \cr F_{Qx} & F_{Qy} & N_Q \end{vmatrix} = R F_{Qy}\,\mathbf i_1 - R F_{Qx}\,\mathbf j_1 \quad &\text{(expand along the first row)} \\
> \overrightarrow{AP}\times\mathbf F_P &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr R & 0 & 0 \cr -N_P & F_{Py} & F_{Pz} \end{vmatrix} = -R F_{Pz}\,\mathbf j_1 + R F_{Py}\,\mathbf k_1 \quad &\text{(expand along the first row)} \\
> \overrightarrow{AI}\times F_{Ij}\,\mathbf j_1 &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr -R\cos\beta & 0 & R\sin\beta \cr 0 & F_{Ij} & 0 \end{vmatrix} = -R\sin\beta\,F_{Ij}\,\mathbf i_1 - R\cos\beta\,F_{Ij}\,\mathbf k_1 \quad &\text{(expand along the first row)} \\
> \overrightarrow{AI}\times F_{It}\,\mathbf e_t &= R F_{It}\left(-\cos\beta\,\mathbf i_1 + \sin\beta\,\mathbf k_1\right)\times\left(\sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf k_1\right) = R F_{It}\left(\cos^2\beta + \sin^2\beta\right)\mathbf j_1 \quad &\text{($\mathbf i_1\times\mathbf k_1 = -\mathbf j_1$, $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_A^b = R\left(F_{Qy} - F_{Ij}\sin\beta\right)\mathbf i_1 + R\left(F_{It} - F_{Qx} - F_{Pz}\right)\mathbf j_1 + R\left(F_{Py} - F_{Ij}\cos\beta\right)\mathbf k_1}$$
>
> **Units:** N in the force; N m in the moment
> **Meaning:** nine unknown contact components act on the ball: three at $Q$ (bottom), three at $P$ (wall), three at $I$ (cone), each applied at its contact point; with the weight at $A$ they reduce to the resultant $\mathbf F^b$ and the moment $\mathbf M_A^b$ at the centre. Only the friction components turn the ball.

#### Part (f): equations of motion and their count

> [!derivation] Part (f): equations of the ball and of the cone
> **Law:** Newton's second law for the centre of mass; moment equation about the centre of mass (pole term zero); Newton's third law at $I$
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> Poles: $A$ for the ball and $G$ for the cone, the centres of mass, so the pole term of Eq. 12.13 is zero. Arm from $G$ to $I$: $\ell_1\,\mathbf i_1 + \ell_3\,\mathbf k_1$, with $\ell_1$ equal to $R(2 - \cos\beta)$ and $\ell_3$ equal to $R\sin\beta - z_G$. The force of the ball on the cone, $-\mathbf F_I$, has the components $-F_1$, $-F_{Ij}$, $-F_3$ in $\mathcal B_1$, with $F_1$ and $F_3$ the first and third components of the previous box.
>
> $$\begin{aligned}
> m\,\mathbf a_0^A &= \mathbf F^b, \qquad \left.\frac{d\mathbf H_{A,0}^b}{dt}\right|_0 = \mathbf M_A^b \quad &\text{(ball: Eq. 12.8 and Eq. 12.13 at $A$)} \\
> \overrightarrow{GI}\times\left(-\mathbf F_I\right) &= -\begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_1 \cr \ell_1 & 0 & \ell_3 \cr F_1 & F_{Ij} & F_3 \end{vmatrix} = \ell_3 F_{Ij}\,\mathbf i_1 + \left(\ell_1 F_3 - \ell_3 F_1\right)\mathbf j_1 - \ell_1 F_{Ij}\,\mathbf k_1 \quad &\text{(expand along the first row)} \\
> \mathbf 0 &= -\mathbf F_I - 2mg\,\mathbf k_1 + X\,\mathbf i_1 + Y\,\mathbf j_1 \quad &\text{(cone: Eq. 12.8 with $G$ at rest)} \\
> \frac{12}{5} mR^2\kappa\,\ddot\theta\,\mathbf k_1 &= \overrightarrow{GI}\times\left(-\mathbf F_I\right) + M_x\,\mathbf i_1 + M_y\,\mathbf j_1 \quad &\text{(cone: Eq. 12.13 at $G$)}
> \end{aligned}$$
>
> Out of the meridian plane (components along $\mathbf j_1$ of the forces, along $\mathbf i_1$ and $\mathbf k_1$ of the moments):
>
> $$\begin{aligned}
> 2mR\ddot\theta &= F_{Qy} + F_{Py} + F_{Ij} \quad &\text{(ball, $\mathbf j_1$; part (b))} \\
> -\frac45 mR^2\ddot\theta &= R\left(F_{Qy} - F_{Ij}\sin\beta\right) \quad &\text{(ball, moment along $\mathbf i_1$)} \\
> -\frac45 mR^2\ddot\theta &= R\left(F_{Py} - F_{Ij}\cos\beta\right) \quad &\text{(ball, moment along $\mathbf k_1$)} \\
> \frac{12}{5} mR^2\kappa\,\ddot\theta &= -R\left(2 - \cos\beta\right)F_{Ij} \quad &\text{(cone, moment along $\mathbf k_1$)} \\
> 0 &= Y - F_{Ij}, \qquad 0 = M_x + \ell_3 F_{Ij} \quad &\text{(cone, $\mathbf j_1$; cone, moment along $\mathbf i_1$)}
> \end{aligned}$$
>
> In the meridian plane (components along $\mathbf i_1$ and $\mathbf k_1$ of the forces, along $\mathbf j_1$ of the moments):
>
> $$\begin{aligned}
> -2mR\dot\theta^2 &= F_{Qx} - N_P + N_I\cos\beta + F_{It}\sin\beta \quad &\text{(ball, $\mathbf i_1$; part (b))} \\
> 0 &= N_Q - mg + F_{Pz} - N_I\sin\beta + F_{It}\cos\beta \quad &\text{(ball, $\mathbf k_1$)} \\
> -\frac45 mR^2\dot\theta^2 &= R\left(F_{It} - F_{Qx} - F_{Pz}\right) \quad &\text{(ball, moment along $\mathbf j_1$)} \\
> 0 &= X - N_I\cos\beta - F_{It}\sin\beta \quad &\text{(cone, $\mathbf i_1$)} \\
> 0 &= N_I\sin\beta - F_{It}\cos\beta - 2mg \quad &\text{(cone, $\mathbf k_1$)} \\
> 0 &= M_y + \ell_1 F_3 - \ell_3 F_1 \quad &\text{(cone, moment along $\mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\text{12 scalar equations (6 of the ball, 6 of the cone) in the second rate of } \theta \text{ and the 13 reactions } N_Q, F_{Qx}, F_{Qy}, N_P, F_{Py}, F_{Pz}, N_I, F_{Ij}, F_{It}, X, Y, M_x, M_y}$$
>
> **Units:** N in the force equations; N m in the moment equations
> **Meaning:** the second rate of $\phi$ is not a new unknown, part (d) gives it; the cone height is constant, so the acceleration of $G$ is zero. The equations split into two groups that do not share unknowns, solved in the next box.

> [!derivation] Part (f): solution of the out-of-plane group and the free unknowns of the meridian plane
> **Law:** elimination; rank of a linear system
> **Source:** Notes.pdf, Sec. 14.1; Notes.pdf, Eq. 13.9; Notes.pdf, Eq. 13.10
>
> Out-of-plane group: four equations (the first four) in the four unknowns $\ddot\theta$, $F_{Qy}$, $F_{Py}$, $F_{Ij}$; the last two give $Y$ and $M_x$. Meridian group: five equations (the first five) in the seven unknowns $N_Q$, $F_{Qx}$, $N_P$, $F_{Pz}$, $N_I$, $F_{It}$, $X$; the last gives $M_y$. Take $F_{It}$ and $F_{Pz}$ as the free unknowns.
>
> $$\begin{aligned}
> F_{Qy} &= F_{Ij}\sin\beta - \frac45 mR\ddot\theta, \qquad F_{Py} = F_{Ij}\cos\beta - \frac45 mR\ddot\theta \quad &\text{(the two moments of the ball)} \\
> 2mR\ddot\theta &= F_{Ij}\left(1 + \sin\beta + \cos\beta\right) - \frac85 mR\ddot\theta \;\Rightarrow\; F_{Ij} = \frac{18\,mR\ddot\theta}{5\left(1 + \sin\beta + \cos\beta\right)} \quad &\text{(substitute in the force along $\mathbf j_1$)} \\
> \ddot\theta\left(\frac{18}{5\left(1 + \sin\beta + \cos\beta\right)} + \frac{12\,\kappa}{5\left(2 - \cos\beta\right)}\right)mR^2 &= 0 \quad &\text{(substitute in the moment of the cone along $\mathbf k_1$)} \\
> \ddot\theta &= 0, \qquad F_{Qy} = F_{Py} = F_{Ij} = Y = M_x = 0 \quad &\text{(the bracket is positive for $0 \lt \beta \lt \pi/2$)} \\
> N_I &= \frac{2mg + F_{It}\cos\beta}{\sin\beta} \quad &\text{(cone, $\mathbf k_1$)} \\
> F_{Qx} &= F_{It} - F_{Pz} + \frac45 mR\dot\theta^2 \quad &\text{(ball, moment along $\mathbf j_1$)} \\
> N_Q &= mg + N_I\sin\beta - F_{It}\cos\beta - F_{Pz} = 3mg - F_{Pz} \quad &\text{(ball, $\mathbf k_1$)} \\
> N_P &= F_{Qx} + N_I\cos\beta + F_{It}\sin\beta + 2mR\dot\theta^2 = \frac{14}{5} mR\dot\theta^2 + 2mg\cot\beta + F_{It}\left(1 + \frac{1}{\sin\beta}\right) - F_{Pz} \quad &\text{(ball, $\mathbf i_1$; $\cos^2\beta + \sin^2\beta = 1$)} \\
> X &= N_I\cos\beta + F_{It}\sin\beta = 2mg\cot\beta + \frac{F_{It}}{\sin\beta} \quad &\text{(cone, $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = 0; \qquad 14 \text{ unknowns},\ 12 \text{ independent equations}: \ F_{It} \text{ and } F_{Pz} \text{ stay free (two-parameter family)}}$$
>
> **Units:** N for every reaction; $[\mathrm{T^{-2}}]$ for the second rate
> **Meaning:** the motion is determined (a constant rate of $\theta$, hence of $\phi$), the reactions are not. A value of $F_{Pz}$ adds at $P$ the force $F_{Pz}$ times the sum of $\mathbf i_1$ and $\mathbf k_1$ and at $Q$ the opposite force: a pair along the chord $PQ$ that squeezes or stretches the ball with no resultant and no moment. A value of $F_{It}$ adds at $I$ a horizontal push along $\mathbf i_1$ of size $F_{It}$ over the sine of $\beta$, taken by the wall at $P$ and the friction at $Q$ on the ball, and by the joint on the cone. Rigid bodies cannot tell these preloads apart: the problem is undetermined. Under the other reading of the support (cone held axially), the axial force adds a third free unknown.

> [!derivation] Part (f): check by the energy theorem
> **Law:** power of the forces on each body; equal velocities at a rolling contact; energy theorem
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 13.2; Notes.pdf, Eq. 13.5
>
> $$\begin{aligned}
> \dot W^{Q} + \dot W^{P} &= \mathbf F_Q\cdot\mathbf 0 + \mathbf F_P\cdot\mathbf 0 = 0 \quad &\text{(no slip on the frame at rest)} \\
> \dot W^{I} &= \mathbf F_I\cdot\mathbf v_0^{I(b)} - \mathbf F_I\cdot\mathbf v_0^{I(c)} = 0 \quad &\text{(the pair acts on points with equal velocities, part (d))} \\
> \dot W^{\mathrm{joint}} &= \left(X\,\mathbf i_1 + Y\,\mathbf j_1\right)\cdot\mathbf 0 + \left(M_x\,\mathbf i_1 + M_y\,\mathbf j_1\right)\cdot\dot\phi\,\mathbf k_1 = 0 \quad &\text{(Eq. 12.29 at $G$, at rest; moment normal to $\mathbf k_1$)} \\
> \dot W^{g} &= -mg\,\mathbf k_1\cdot\mathbf v_0^A - 2mg\,\mathbf k_1\cdot\mathbf 0 = -mg\,\mathbf k_1\cdot 2R\dot\theta\,\mathbf j_1 = 0 \quad &\text{(weights; $A$ moves horizontally)} \\
> \frac{dT}{dt} &= \frac65 mR^2\left(3 + \kappa^2\right)\cdot 2\dot\theta\ddot\theta = 0 \quad &\text{(Eq. 12.30: the total power is zero; chain rule)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta\,\ddot\theta = 0 \;\Rightarrow\; \ddot\theta = 0 \text{ while the bearing turns}}$$
>
> **Units:** W in the powers
> **Meaning:** no force does work, so the kinetic energy and with it the rate of $\theta$ are constant: the same result as the out-of-plane group, by a second route.

#### Part (g): maximum rate without slip

> [!derivation] Part (g): reactions at a constant rate and the limit of the friction at Q
> **Law:** the equations of part (f) with the two assumptions of the statement; Coulomb's law of friction without slip
> **Source:** Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 6.6; Notes.pdf, Eq. 12.13
>
> The cone turns at a constant rate, so by part (d) the second rate of $\theta$ is zero; a torque $\Gamma\,\mathbf k_0$ from whatever keeps that rate is added to the cone, and its axial equation reads zero equal to $\Gamma$ minus $R(2 - \cos\beta)F_{Ij}$. The statement sets to zero the components of the friction at $P$ and at $I$ in the plane $Ox_1z_1$, which are $F_{Pz}$ and $F_{It}$: exactly the two free unknowns of part (f).
>
> $$\begin{aligned}
> F_{Ij}\left(1 + \sin\beta + \cos\beta\right) &= \frac{18}{5} mR\cdot 0 = 0 \;\Rightarrow\; F_{Ij} = F_{Qy} = F_{Py} = 0, \quad \Gamma = 0 \quad &\text{(out-of-plane group of the ball, previous box)} \\
> N_I &= \frac{2mg}{\sin\beta}, \qquad X = 2mg\cot\beta \quad &\text{(cone, with $F_{It}$ zero)} \\
> F_{Qx} &= \frac45 mR\dot\theta^2, \qquad N_Q = 3mg \quad &\text{(ball, with $F_{It}$ and $F_{Pz}$ zero)} \\
> N_P &= \frac{14}{5} mR\dot\theta^2 + 2mg\cot\beta \quad &\text{(ball, $\mathbf i_1$)} \\
> \left|\mathbf F_Q^{\mathrm{fr}}\right| &= \sqrt{F_{Qx}^2 + F_{Qy}^2} = \frac45 mR\dot\theta^2 \le \mu N_Q = 3\mu mg \quad &\text{(Coulomb at $Q$)} \\
> \dot\theta^2 &\le \frac{15\,\mu g}{4R} \quad &\text{(divide by $4mR/5$)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta_{\max} = \sqrt{\frac{15\,\mu g}{4R}}}$$
>
> **Units:** $\sqrt{[\mathrm{L\,T^{-2}}]/[\mathrm L]} = [\mathrm{T^{-1}}]$
> **Meaning:** the friction at $P$ and at $I$ is zero, below any limit, and the three normal forces are positive for $0 \lt \beta \lt \pi/2$, so contact is kept and only $Q$ can slip. There the friction, along plus $\mathbf i_1$ (outwards), supplies the moment along minus $\mathbf j_1$ that turns the angular momentum of the ball with the meridian plane; it grows with the square of the rate of $\theta$, while the normal force at $Q$ stays at the weight of the ball plus that of the cone. No torque is needed to keep the cone turning.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Degrees of freedom | $\mu \to 0$: five ($\theta$, three angles of the ball, $\phi$). $\mu \to \infty$: one ($\theta$); the no-slip conditions are integrable |
| (b) Kinematics of $A$ | $\mathbf r_0^A = 2R\,\mathbf i_1$, $\mathbf v_0^A = 2R\dot\theta\,\mathbf j_1$, $\mathbf a_0^A = -2R\dot\theta^2\,\mathbf i_1 + 2R\ddot\theta\,\mathbf j_1$, with $\mathbf i_1 = \cos\theta\,\mathbf i_0 + \sin\theta\,\mathbf j_0$, $\mathbf j_1 = -\sin\theta\,\mathbf i_0 + \cos\theta\,\mathbf j_0$ |
| (c) IAR, angular velocity and acceleration | IAR: the line $PQ$, through $Q$ along $\mathbf i_1 + \mathbf k_1$; $\boldsymbol\omega_{b0} = -2\dot\theta(\mathbf i_1 + \mathbf k_1)$; $\boldsymbol\alpha_{b0} = -2\ddot\theta(\mathbf i_1 + \mathbf k_1) - 2\dot\theta^2\,\mathbf j_1$ |
| (d) Relation of the rates | $\dot\phi = \dfrac{2(1 + \sin\beta + \cos\beta)}{2 - \cos\beta}\,\dot\theta$ |
| (e) Forces on the ball | $-mg\,\mathbf k_1$ at $A$; $\mathbf F_Q = F_{Qx}\mathbf i_1 + F_{Qy}\mathbf j_1 + N_Q\mathbf k_1$ at $Q$; $\mathbf F_P = -N_P\mathbf i_1 + F_{Py}\mathbf j_1 + F_{Pz}\mathbf k_1$ at $P$; $\mathbf F_I = N_I(\cos\beta\,\mathbf i_1 - \sin\beta\,\mathbf k_1) + F_{Ij}\mathbf j_1 + F_{It}(\sin\beta\,\mathbf i_1 + \cos\beta\,\mathbf k_1)$ at $I$; no contact torques |
| (f) Equations and indeterminacy | 12 equations (ball and cone) for 14 unknowns; $\ddot\theta = 0$, $F_{Qy} = F_{Py} = F_{Ij} = 0$; $F_{It}$ and $F_{Pz}$ free, the rest as in the box of part (f) |
| (g) Maximum rate without slip | $\dot\theta_{\max} = \sqrt{15\mu g/(4R)}$, with $N_Q = 3mg$, $F_{Qx} = \tfrac45 mR\dot\theta^2$, $N_I = 2mg/\sin\beta$, $N_P = \tfrac{14}{5}mR\dot\theta^2 + 2mg\cot\beta$ |

**Limiting cases and consistency:** the key prints no answer for this problem (Problems.pdf, pp. 77 to 81 checked).

* **Cylindrical inner race.** With $\beta$ tending to zero the cone becomes a cylinder of radius $R$ touching the ball at the height of $A$; part (d) then gives a ratio of 4 between the rates, the classic ball bearing: the inner race point at $I$ moves at twice the speed of the centre of the ball, whose speed is $2R$ times the rate of $\theta$.
* **Ratio of the rates.** For $\beta$ equal to 30 degrees, $\kappa$ is about 4.17 (recomputed in part (d)); it is positive for every half-angle between 0 and a right angle, so the cone and the centre of the ball always turn in the same sense.
* **Free motion.** Both the out-of-plane group and the energy theorem give a constant rate of $\theta$ when no torque acts on the cone.
* **Vertical balance in part (g).** The bottom carries $3mg$, the weight of the ball and of the cone: the joint has no axial force, so the cone weighs on the ball and the ball on the bottom.
* **Dimensions.** Every force term is a mass times $R$ times a squared rate or a mass times $g$; every moment has one more length.

---

## Problem RB-36: Mars rolling rover

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** two bodies in the vertical plane of the figure. The cylinder $b$, of mass $M$, radius $R$, centre of mass at its centre $C$ and moment of inertia $I_z$ about the axis through $C$ normal to the plane, with a diametral slot of length $2\ell$; and the particle $P$, of mass $m$, which moves along the slot with the prescribed law $x_1^P(t)$, pushed by a motor of negligible mass mounted on the cylinder. The cylinder touches the slope at $A$, with friction coefficient $\mu$.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, with $\mathbf i_0$ along the slope, upwards, $\mathbf j_0$ normal to the slope, away from it, and $\mathbf k_0$ out of the paper (⊙), as in the figure. The slope is at rest, so $S_0$ is inertial. $O$ is drawn above the slope in the figure; it is placed here on the line of the slope, so that $C$ is at the height $R$ along $\mathbf j_0$ (another position of $O$ only adds a constant to that coordinate).
* **Cylinder frame:** $S_1\{C; \mathcal B_1\}$, attached to the cylinder, with $\mathbf i_1$ along the slot (towards the end where $P$ is drawn) and $\mathbf j_1$ normal to it.
* **Angle, read from the figure:** $\varphi$ is drawn from the dashed line through $C$ parallel to $\mathbf j_0$ to $\mathbf j_1$, clockwise in the view with $\mathbf k_0$ out of the paper; it is taken positive in that sense, a positive rotation about minus $\mathbf k_0$. The opposite reading would change the sign of $\varphi$, of its rates and of the rolling relation in every formula, not the method.
* **Coordinates and degrees of freedom:** the contact with the slope fixes the height of $C$ (Notes.pdf, Eq. 13.1), so the cylinder keeps $x_0^C$ and $\varphi$: two degrees of freedom while it may slip; $x_1^P$ is not a degree of freedom, its law is prescribed. With rolling without slip (from part (e) on) one degree of freedom remains, $\varphi$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass, radius and centre of the cylinder | $M$, $R$, $C$ | kg, m |
| Moment of inertia of the cylinder about the normal through $C$ | $I_z$ | kg m$^2$ |
| Half-length of the slot | $\ell$, with $\ell \lt R$ | m |
| Mass and position of the particle along the slot | $m$, $x_1^P(t)$ prescribed | kg, m |
| Slope angle; friction coefficient | $\gamma$; $\mu$ | rad; - |
| Coordinates of the cylinder | $x_0^C$, $\varphi$ | m, rad |
| Contact forces of the slope at $A$ | normal $N_A\,\mathbf j_0$, friction $f_A\,\mathbf i_0$ | N |
| From part (e) on | $\gamma = 0$, $x_1^P(t) = \ell\sin\Omega t$, $\ell = R/2$, no slip | rad, m |

![[attachments/EM-SOL/rb36-gravity.svg]]

> [!derivation] Gravity in the basis of the slope
> **Law:** components of a vector in a rotated basis; right triangle of the slope
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 12.34; Problems.pdf, p. 65
>
> View with $\mathbf k_0$ out of the paper (⊙). Write $\mathbf e_h$ for the horizontal unit vector to the right and $\mathbf e_v$ for the upward vertical. The slope rises to the right by $\gamma$, so $\mathbf i_0$ is $\mathbf e_h$ turned counterclockwise by $\gamma$: adjacent leg along $\mathbf e_h$ (cosine), opposite leg along $\mathbf e_v$ (sine); $\mathbf j_0$ has its adjacent leg along $\mathbf e_v$ (cosine) and its opposite leg along minus $\mathbf e_h$ (sine), because the counterclockwise turn carries the tip of $\mathbf e_v$ to the left. The inverse relation is the transpose.
>
> $$\begin{aligned}
> \mathbf i_0 &= \cos\gamma\,\mathbf e_h + \sin\gamma\,\mathbf e_v, \qquad \mathbf j_0 = -\sin\gamma\,\mathbf e_h + \cos\gamma\,\mathbf e_v \quad &\text{(legs of the two triangles)} \\
> \mathbf e_v &= \sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0, \qquad \mathbf e_h = \cos\gamma\,\mathbf i_0 - \sin\gamma\,\mathbf j_0 \quad &\text{(transpose of the rotation)} \\
> \mathbf g &= -g\,\mathbf e_v \quad &\text{(gravity points down)}
> \end{aligned}$$
>
> $$\boxed{\mathbf g = -g\left(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the component along the slope points down the slope, minus $\mathbf i_0$, with the sine of $\gamma$; the component normal to the slope presses the cylinder on it, with the cosine.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb36-rot-phi.svg]]

> [!derivation] Cylinder basis: rotation by phi about minus k0
> **Law:** simple rotation about the third axis; right-hand rule; Poisson's formula
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.4; [Lecture 7, Slide 12]
>
> View with $\mathbf k_0$ out of the paper (⊙); a positive $\varphi$ turns clockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\varphi$), opposite leg along minus $\mathbf j_0$ (sine), because the clockwise turn carries the tip of $\mathbf i_0$ downwards. Triangle of $\mathbf j_1$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along plus $\mathbf i_0$ (sine), because the clockwise turn carries the tip of $\mathbf j_0$ to the right, as $\mathbf j_1$ is drawn.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\varphi\,\mathbf i_0 - \sin\varphi\,\mathbf j_0, \qquad \mathbf j_1 = \sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\varphi & \sin\varphi & 0 \cr -\sin\varphi & \cos\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\varphi + \sin^2\varphi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\varphi + \sin^2\varphi & -\cos\varphi\sin\varphi + \sin\varphi\cos\varphi & 0 \cr -\sin\varphi\cos\varphi + \cos\varphi\sin\varphi & \sin^2\varphi + \cos^2\varphi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \boldsymbol\omega_{10} &= -\dot\varphi\,\mathbf k_0 \quad &\text{(rotation about minus $\mathbf k_0$)} \\
> \dot{\mathbf i}_1 &= -\dot\varphi\,\mathbf k_0\times\mathbf i_1 = -\dot\varphi\,\mathbf j_1, \qquad \dot{\mathbf j}_1 = -\dot\varphi\,\mathbf k_0\times\mathbf j_1 = \dot\varphi\,\mathbf i_1 \quad &\text{(Poisson; $\mathbf k_0\times\mathbf i_1 = \mathbf j_1$, $\mathbf k_0\times\mathbf j_1 = -\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\varphi\,\mathbf i_0 - \sin\varphi\,\mathbf j_0, \quad \mathbf j_1 = \sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0, \quad \boldsymbol\omega_{10} = -\dot\varphi\,\mathbf k_0, \quad \dot{\mathbf i}_1 = -\dot\varphi\,\mathbf j_1, \quad \dot{\mathbf j}_1 = \dot\varphi\,\mathbf i_1}$$
>
> **Units:** dimensionless; $[\mathrm{T^{-1}}]$
> **Meaning:** a positive rate of $\varphi$ turns the cylinder clockwise, the sense in which it rolls up the slope; $\mathbf i_1$ is the direction of the slot.

> [!derivation] Part (a): position, velocity and acceleration of P
> **Law:** sum of segments; derivative of a vector written in a moving basis (product rule, Poisson)
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 9.4; Notes.pdf, Eq. 3.8
>
> $C$ is at the height $R$ above the slope, so its position has the constant component $R$ along $\mathbf j_0$ and its velocity has none.
>
> $$\begin{aligned}
> \mathbf r_0^P &= \mathbf r_0^C + \overrightarrow{CP} = x_0^C\,\mathbf i_0 + R\,\mathbf j_0 + x_1^P\,\mathbf i_1 \quad &\text{(sum of segments)} \\
> \mathbf v_0^P &= \dot x_0^C\,\mathbf i_0 + \dot x_1^P\,\mathbf i_1 + x_1^P\,\dot{\mathbf i}_1 = \dot x_0^C\,\mathbf i_0 + \dot x_1^P\,\mathbf i_1 - x_1^P\dot\varphi\,\mathbf j_1 \quad &\text{(product rule; Poisson)} \\
> \mathbf a_0^P &= \ddot x_0^C\,\mathbf i_0 + \ddot x_1^P\,\mathbf i_1 + \dot x_1^P\,\dot{\mathbf i}_1 - \left(\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right)\mathbf j_1 - x_1^P\dot\varphi\,\dot{\mathbf j}_1 \quad &\text{(product rule on each term)} \\
> &= \ddot x_0^C\,\mathbf i_0 + \ddot x_1^P\,\mathbf i_1 - \dot x_1^P\dot\varphi\,\mathbf j_1 - \left(\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right)\mathbf j_1 - x_1^P\dot\varphi^2\,\mathbf i_1 \quad &\text{(Poisson)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_0^P = x_0^C\,\mathbf i_0 + R\,\mathbf j_0 + x_1^P\,\mathbf i_1, \qquad \mathbf v_0^P = \dot x_0^C\,\mathbf i_0 + \dot x_1^P\,\mathbf i_1 - x_1^P\dot\varphi\,\mathbf j_1 \\ \mathbf a_0^P = \ddot x_0^C\,\mathbf i_0 + \left(\ddot x_1^P - x_1^P\dot\varphi^2\right)\mathbf i_1 - \left(2\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right)\mathbf j_1 \end{gathered}}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{L\,T^{-1}}]$; $[\mathrm{L\,T^{-2}}]$ in every term
> **Meaning:** the acceleration of $P$ is that of $C$ plus the relative acceleration along the slot, the centripetal term towards $C$, and the Coriolis and angular acceleration terms normal to the slot; $\mathbf i_1$ and $\mathbf j_1$ are those of the previous box.

> [!derivation] Rolling without slip at A (used from part (e) on)
> **Law:** velocity field of the cylinder; rolling without slipping on a body at rest
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Eq. 13.4
>
> $$\begin{aligned}
> \mathbf v_0^{A(b)} &= \mathbf v_0^C + \boldsymbol\omega_{10}\times\overrightarrow{CA} = \dot x_0^C\,\mathbf i_0 - \dot\varphi\,\mathbf k_0\times\left(-R\,\mathbf j_0\right) \quad &\text{(Eq. 9.3 from $C$)} \\
> &= \dot x_0^C\,\mathbf i_0 + R\dot\varphi\,\mathbf k_0\times\mathbf j_0 = \left(\dot x_0^C - R\dot\varphi\right)\mathbf i_0 \quad &\text{($\mathbf k_0\times\mathbf j_0 = -\mathbf i_0$)} \\
> \mathbf v_0^{A(b)} &= \mathbf 0 \;\Rightarrow\; \dot x_0^C = R\dot\varphi \quad &\text{(no slip on the slope at rest, Eq. 13.5)} \\
> \left[x_0^C\right]_0^t &= R\left[\varphi\right]_0^t \;\Rightarrow\; x_0^C(t) - x_0^C(0) = R\left(\varphi(t) - \varphi(0)\right) \quad &\text{(integrate from 0 to $t$; Barrow's rule)} \\
> \ddot x_0^C &= R\ddot\varphi \quad &\text{(derivative of the first relation)}
> \end{aligned}$$
>
> $$\boxed{\dot x_0^C = R\dot\varphi, \qquad x_0^C = x_0^C(0) + R\left(\varphi - \varphi(0)\right), \qquad \ddot x_0^C = R\ddot\varphi}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$; $[\mathrm L]$; $[\mathrm{L\,T^{-2}}]$
> **Meaning:** a clockwise turn (positive rate of $\varphi$) rolls the cylinder up the slope; the constraint is integrable, so with no slip $\varphi$ alone fixes the configuration.

### Center of Mass and Inertia Tensor

> [!derivation] Inertia data and centre of mass of the system
> **Law:** centre of mass of a system of bodies; principal axis normal to a plane of symmetry
> **Source:** Notes.pdf, Eq. 13.11; Notes.pdf, Eq. 10.5; Notes.pdf, Eq. 10.15
>
> The statement gives the centre of mass $C$ of the slotted cylinder and its moment $I_z$ about the normal through $C$ (the slot is diametral and centred, so $C$ stays at the geometric centre; with the slot, $I_z$ is not that of a full cylinder, so it is kept as the datum). The mid-plane of the cylinder is a plane of symmetry, so the products of inertia with $\mathbf k_0$ vanish and $\mathbf k_0$ is a principal axis. The particle is a point mass.
>
> $$\begin{aligned}
> \left(M + m\right)\mathbf r_0^{G} &= M\,\mathbf r_0^C + m\,\mathbf r_0^P \quad &\text{(Eq. 13.11)} \\
> \left(M + m\right)\mathbf a_0^{G} &= M\,\mathbf a_0^C + m\,\mathbf a_0^P = M\ddot x_0^C\,\mathbf i_0 + m\,\mathbf a_0^P \quad &\text{(second derivative; $C$ at constant height)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{C,0}^b\cdot\mathbf k_0 = I_z\,\boldsymbol\omega_{10}\cdot\mathbf k_0, \qquad \left(M + m\right)\mathbf a_0^{G} = M\ddot x_0^C\,\mathbf i_0 + m\,\mathbf a_0^P}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$; $[\mathrm M][\mathrm{L\,T^{-2}}]$
> **Meaning:** $G$ is the centre of mass of cylinder and particle together; it moves with $P$ along the slot even when $C$ is at rest.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Momenta of the cylinder and of the particle
> **Law:** linear momentum; angular momentum of a rigid body about its centre of mass
> **Source:** Notes.pdf, Eq. 11.3; Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 12.20
>
> $$\begin{aligned}
> \mathbf p_0^b &= M\,\mathbf v_0^C = M\dot x_0^C\,\mathbf i_0, \qquad \mathbf p_0^P = m\,\mathbf v_0^P \quad &\text{(Eq. 11.3)} \\
> \mathbf H_{C,0}^b &= \bar{\bar I}_C\cdot\boldsymbol\omega_{10} = -I_z\dot\varphi\,\mathbf k_0 \quad &\text{(Eq. 11.12; $\mathbf k_0$ principal)} \\
> \left.\frac{d\mathbf H_{C,0}^b}{dt}\right|_0 &= -I_z\ddot\varphi\,\mathbf k_0 \quad &\text{($\mathbf k_0$ fixed)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0^b = M\dot x_0^C\,\mathbf i_0, \qquad \mathbf H_{C,0}^b = -I_z\dot\varphi\,\mathbf k_0, \qquad \left.\frac{d\mathbf H_{C,0}^b}{dt}\right|_0 = -I_z\ddot\varphi\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-1}}]$; $[\mathrm{M\,L^2\,T^{-1}}]$; N m
> **Meaning:** the angular momentum of the cylinder is along minus $\mathbf k_0$ when it turns clockwise. The kinetic energy is not used: the pair of forces between particle and cylinder acts at two points whose velocities differ by the rate of $x_1^P$ along $\mathbf i_1$, so its total power is minus $F_1$ times that rate, not zero while the motor moves $P$, and the energy of the system is not constant.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb36-exploded.svg]]

The exploded view separates the particle and the cylinder. On the particle act its weight and the force of the cylinder, $-\mathbf F$: the push of the motor along the slot and the push of the slot walls normal to it, both at $P$. On the cylinder act the opposite force $\mathbf F$ at its point $P$ (third law of Newton; the statement notes that the reaction of the motor acts on the line of action of the push, through $P$), its weight at $C$, and the contact force of the slope at $A$.

| Load | Body | Point | Expression in $\mathcal B_0$ or $\mathcal B_1$ | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the particle | $P$ | $P$ | $-mg(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0)$ | applied |
| Cylinder (slot and motor) on the particle | $P$ | $P$ | $-\mathbf F = -F_1\,\mathbf i_1 - F_2\,\mathbf j_1$ | internal (pair) |
| Particle on the cylinder | $b$ | $P$ | $\mathbf F = F_1\,\mathbf i_1 + F_2\,\mathbf j_1$ | internal (pair) |
| Weight of the cylinder | $b$ | $C$ | $-Mg(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0)$ | applied |
| Slope on the cylinder | $b$ | $A$ | $f_A\,\mathbf i_0 + N_A\,\mathbf j_0$ | constraint |

> [!derivation] Part (b): force of the particle on the cylinder
> **Law:** Newton's second law for the particle; Newton's third law
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 13.9; Problems.pdf, p. 65
>
> The components along the slot ($F_1$, the push of the motor) and normal to it ($F_2$, the slot walls) use the dot products of the bases: $\mathbf i_0\cdot\mathbf i_1$ is the cosine of $\varphi$, $\mathbf j_0\cdot\mathbf i_1$ minus its sine, $\mathbf i_0\cdot\mathbf j_1$ its sine and $\mathbf j_0\cdot\mathbf j_1$ its cosine.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -mg\left(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0\right) - \mathbf F \quad &\text{(Eq. 12.8 for $P$)} \\
> \mathbf F &= -mg\left(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0\right) - m\,\mathbf a_0^P \quad &\text{(solve for the force)} \\
> F_1 &= \mathbf F\cdot\mathbf i_1 = -mg\left(\sin\gamma\cos\varphi - \cos\gamma\sin\varphi\right) - m\left(\ddot x_0^C\cos\varphi + \ddot x_1^P - x_1^P\dot\varphi^2\right) \quad &\text{(project on $\mathbf i_1$; part (a))} \\
> F_2 &= \mathbf F\cdot\mathbf j_1 = -mg\left(\sin\gamma\sin\varphi + \cos\gamma\cos\varphi\right) - m\left(\ddot x_0^C\sin\varphi - 2\dot x_1^P\dot\varphi - x_1^P\ddot\varphi\right) \quad &\text{(project on $\mathbf j_1$; part (a))}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -mg\left(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0\right) - m\,\mathbf a_0^P, \quad F_1 = mg\sin\left(\varphi - \gamma\right) - m\left(\ddot x_0^C\cos\varphi + \ddot x_1^P - x_1^P\dot\varphi^2\right), \quad F_2 = -mg\cos\left(\varphi - \gamma\right) - m\left(\ddot x_0^C\sin\varphi - 2\dot x_1^P\dot\varphi - x_1^P\ddot\varphi\right)}$$
>
> **Units:** N in every term
> **Meaning:** at rest the particle loads the cylinder with its weight only; in motion the cylinder must also supply the force that accelerates the particle, and feels the opposite of it. The sine and cosine of the difference of $\varphi$ and $\gamma$ come from the subtraction and addition formulas.

> [!derivation] Part (c): resultant force and moment about C on the cylinder
> **Law:** sum of forces; moment of a force about a point; vector products by determinants
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 12.15
>
> Arms from $C$: to $A$, minus $R\,\mathbf j_0$; to $P$, $x_1^P\,\mathbf i_1$; the weight acts at $C$.
>
> $$\begin{aligned}
> \mathbf F^b &= -Mg\left(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0\right) + f_A\,\mathbf i_0 + N_A\,\mathbf j_0 + \mathbf F \quad &\text{(sum of the three loads)} \\
> \overrightarrow{CA}\times\left(f_A\,\mathbf i_0 + N_A\,\mathbf j_0\right) &= \begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr 0 & -R & 0 \cr f_A & N_A & 0 \end{vmatrix} = \mathbf k_0\left(0 + R f_A\right) = R f_A\,\mathbf k_0 \quad &\text{(expand along the first row)} \\
> \overrightarrow{CP}\times\mathbf F &= \begin{vmatrix} \mathbf i_1 & \mathbf j_1 & \mathbf k_0 \cr x_1^P & 0 & 0 \cr F_1 & F_2 & 0 \end{vmatrix} = x_1^P F_2\,\mathbf k_0 \quad &\text{(expand along the first row; the push $F_1$ along the slot has no arm)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^b = \left(f_A - Mg\sin\gamma\right)\mathbf i_0 + \left(N_A - Mg\cos\gamma\right)\mathbf j_0 + \mathbf F, \qquad \mathbf M_C^b = \left(R f_A + x_1^P F_2\right)\mathbf k_0}$$
>
> **Units:** N; N m
> **Meaning:** with $\mathbf F$ and $F_2$ of part (b). The friction at $A$ turns the cylinder counterclockwise about $C$ when it is positive (up the slope); the force of the particle turns it only through the part normal to the slot, since the reaction of the motor acts along the slot through $C$.

> [!derivation] Part (d): equilibrium on the slope and the largest slope angle
> **Law:** equilibrium of the cylinder (Eq. 12.24, Eq. 12.25); Coulomb's law of friction without slip
> **Source:** Notes.pdf, Eq. 12.24; Notes.pdf, Eq. 12.25; Notes.pdf, Sec. 6.6; Notes.pdf, Sec. 13.2
>
> At rest every rate is zero, the particle is held at a constant $x_1^P$ and $\varphi$ equals $\gamma$, so the acceleration of $P$ is zero and part (b) gives $F_2$ equal to minus $mg\cos 0$, that is minus $mg$, and $\mathbf F\cdot\mathbf i_0$ equal to minus $mg\sin\gamma$. The slot is then horizontal: $\mathbf i_1$ is $\cos\gamma\,\mathbf i_0 - \sin\gamma\,\mathbf j_0$, the vector $\mathbf e_h$ of the gravity box.
>
> $$\begin{aligned}
> 0 &= f_A - Mg\sin\gamma - mg\sin\gamma \;\Rightarrow\; f_A = \left(M + m\right)g\sin\gamma \quad &\text{(resultant along $\mathbf i_0$)} \\
> 0 &= N_A - Mg\cos\gamma - mg\cos\gamma \;\Rightarrow\; N_A = \left(M + m\right)g\cos\gamma \quad &\text{(resultant along $\mathbf j_0$)} \\
> 0 &= R f_A - x_1^P mg \;\Rightarrow\; x_1^P = \frac{\left(M + m\right)R\sin\gamma}{m} \quad &\text{(moment about $C$, part (c))} \\
> \left|x_1^P\right| \le \ell &\;\Rightarrow\; \sin\gamma \le \frac{m\,\ell}{\left(M + m\right)R} \quad &\text{(the particle must fit in the slot)} \\
> \left|f_A\right| \le \mu N_A &\;\Rightarrow\; \tan\gamma \le \mu \quad &\text{(no slip; divide by $(M + m)g\cos\gamma$)}
> \end{aligned}$$
>
> $$\boxed{\gamma_{\max} = \min\left\{\arcsin\frac{m\,\ell}{\left(M + m\right)R},\ \arctan\mu\right\}}$$
>
> **Units:** dimensionless ratios: $[\mathrm M][\mathrm L]/([\mathrm M][\mathrm L])$
> **Meaning:** a positive $x_1^P$ puts $P$ along plus $\mathbf e_h$, on the uphill side of $C$: its weight there balances the moment of the friction that holds the cylinder on the slope. The first bound is the geometric one (the particle cannot go beyond the end of the slot), the second the friction one; the argument of the arcsine is below 1 because $\ell$ is below $R$ and $m$ below $M + m$.

#### Part (e): closed system with rolling, horizontal ground and the prescribed law

> [!derivation] Part (e): equations of the cylinder and elimination of the friction
> **Law:** Newton's second law and moment equation about the centre of mass of the cylinder; rolling relation; part (b) for the force of the particle
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.10; Notes.pdf, Eq. 13.5
>
> With $\gamma$ zero, gravity is minus $g\,\mathbf j_0$ and the second rate of $x_0^C$ is $R$ times that of $\varphi$. The pole of the moment equation is $C$, the centre of mass of the cylinder, so the pole term vanishes. The projections of the acceleration of $P$ on $\mathbf i_0$ and $\mathbf j_0$ use the rows of $[{}_0R_1]$.
>
> $$\begin{aligned}
> \mathbf a_0^P\cdot\mathbf i_0 &= R\ddot\varphi + \left(\ddot x_1^P - x_1^P\dot\varphi^2\right)\cos\varphi - \left(2\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right)\sin\varphi \quad &\text{(part (a); rolling)} \\
> \mathbf a_0^P\cdot\mathbf j_0 &= -\left(\ddot x_1^P - x_1^P\dot\varphi^2\right)\sin\varphi - \left(2\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right)\cos\varphi \quad &\text{(part (a))} \\
> MR\ddot\varphi &= f_A + \mathbf F\cdot\mathbf i_0 = f_A - m\,\mathbf a_0^P\cdot\mathbf i_0 \quad &\text{(cylinder, $\mathbf i_0$; part (b) with $\gamma$ zero)} \\
> 0 &= N_A - Mg + \mathbf F\cdot\mathbf j_0 = N_A - Mg - mg - m\,\mathbf a_0^P\cdot\mathbf j_0 \quad &\text{(cylinder, $\mathbf j_0$; $C$ at constant height)} \\
> -I_z\ddot\varphi &= R f_A + x_1^P F_2 \quad &\text{(cylinder, moment about $C$; parts (c) and the momenta)} \\
> F_2 &= -mg\cos\varphi - mR\ddot\varphi\sin\varphi + m\left(2\dot x_1^P\dot\varphi + x_1^P\ddot\varphi\right) \quad &\text{(part (b) with $\gamma$ zero; rolling)} \\
> 0 &= \left(I_z + MR^2\right)\ddot\varphi + mR\,\mathbf a_0^P\cdot\mathbf i_0 + x_1^P F_2 \quad &\text{(friction of the first equation into the moment equation)}
> \end{aligned}$$
>
> Expanding the last row with the first and the sixth, and collecting the terms in the second rate of $\varphi$:
>
> $$\boxed{\begin{gathered} \left[I_z + MR^2 + m\left(R^2 - 2R\,x_1^P\sin\varphi + \left(x_1^P\right)^2\right)\right]\ddot\varphi + mR\left(\ddot x_1^P - x_1^P\dot\varphi^2\right)\cos\varphi - 2mR\,\dot x_1^P\dot\varphi\sin\varphi + 2m\,x_1^P\dot x_1^P\dot\varphi - mg\,x_1^P\cos\varphi = 0 \\ f_A = MR\ddot\varphi + m\,\mathbf a_0^P\cdot\mathbf i_0, \qquad N_A = \left(M + m\right)g + m\,\mathbf a_0^P\cdot\mathbf j_0, \qquad x_1^P = \frac R2\sin\Omega t \end{gathered}}$$
>
> **Units:** N m in every term of the first equation ($[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$); N in the others
> **Meaning:** the bracket is $I_z + MR^2$ plus $m$ times the squared distance from $A$ to $P$ (the vector from $A$ to $P$ is $R\,\mathbf j_0$ plus $x_1^P\,\mathbf i_1$, and the dot product of $\mathbf j_0$ and $\mathbf i_1$ is minus the sine of $\varphi$). Three equations for the three unknowns $\varphi(t)$, $f_A$, $N_A$; the law of $x_1^P$ is known, and part (b) then gives the push of the motor and the force of the slot walls.

> [!derivation] Part (e): initial conditions and order of solution
> **Law:** second-order differential equation; rolling relation integrated with Barrow's rule; Coulomb's law to check the hypotheses
> **Source:** Notes.pdf, Sec. 14.1; Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 6.6
>
> The law of $x_1^P$ fixes its value and its rates at every instant, by the chain rule: the first rate is $\ell\Omega\cos\Omega t$, the second minus $\ell\Omega^2\sin\Omega t$. The equation of the previous box is of second order in $\varphi$.
>
> $$\begin{aligned}
> \dot x_1^P &= \frac{d}{dt}\left(\ell\sin\Omega t\right) = \ell\Omega\cos\Omega t, \qquad \ddot x_1^P = \frac{d}{dt}\left(\ell\Omega\cos\Omega t\right) = -\ell\Omega^2\sin\Omega t \quad &\text{(chain rule)} \\
> \text{data} &: \varphi(0),\ \dot\varphi(0),\ x_0^C(0) \quad &\text{(two for the second order equation, one for the position along the ground)} \\
> \text{step 1} &: \varphi(t) \ \text{from the equation of motion (numerically)} \quad &\text{(only unknown of that equation)} \\
> \text{step 2} &: x_0^C(t) = x_0^C(0) + R\left(\varphi(t) - \varphi(0)\right) \quad &\text{(rolling relation)} \\
> \text{step 3} &: \mathbf a_0^P,\ F_1,\ F_2 \quad &\text{(parts (a) and (b))} \\
> \text{step 4} &: f_A,\ N_A \quad &\text{(the two force equations)} \\
> \text{step 5} &: N_A \ge 0,\ \left|f_A\right| \le \mu N_A \quad &\text{(the hypotheses: contact and no slip)}
> \end{aligned}$$
>
> $$\boxed{\text{initial conditions } \varphi(0),\ \dot\varphi(0) \text{ (and } x_0^C(0)\text{)}; \quad \varphi \to x_0^C \to \mathbf F \to f_A, N_A \to \text{checks}}$$
>
> **Units:** rad and rad/s for the initial data of $\varphi$; m for $x_0^C(0)$
> **Meaning:** the motion of $P$ needs no initial condition, it is imposed; the reactions are algebraic once $\varphi$ is known, and if a check fails (contact lost or slip) the hypotheses of part (e) stop holding from that instant on.

#### Part (f): no take-off

> [!derivation] Part (f): normal force when the cylinder is momentarily at rest
> **Law:** the equations of part (e) at an instant with zero rate and zero second rate of $\varphi$; unilateral contact
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 13.1; Notes.pdf, Sec. 13.2
>
> At that instant the equation of motion keeps only the terms without the rates of $\varphi$; with the law of $x_1^P$ it fixes which configurations are possible.
>
> $$\begin{aligned}
> 0 &= mR\,\ddot x_1^P\cos\varphi - mg\,x_1^P\cos\varphi = m\cos\varphi\left(-R\ell\Omega^2 - g\ell\right)\sin\Omega t \quad &\text{(equation of motion with both rates of $\varphi$ zero)} \\
> 0 &= -m\ell\left(R\Omega^2 + g\right)\cos\varphi\,\sin\Omega t \;\Rightarrow\; \cos\varphi = 0 \ \text{or}\ \sin\Omega t = 0 \quad &\text{(the bracket is positive)} \\
> \mathbf a_0^P\cdot\mathbf j_0 &= -\ddot x_1^P\sin\varphi = \ell\Omega^2\sin\Omega t\,\sin\varphi \quad &\text{(part (e) with both rates of $\varphi$ zero)} \\
> N_A &= \left(M + m\right)g + m\ell\Omega^2\sin\Omega t\,\sin\varphi \quad &\text{(force equation along $\mathbf j_0$)} \\
> f_A &= m\,\ddot x_1^P\cos\varphi = -m\ell\Omega^2\sin\Omega t\cos\varphi = 0 \quad &\text{(force equation along $\mathbf i_0$; either case above)} \\
> N_A\big|_{\min} &= \left(M + m\right)g - m\ell\Omega^2 \quad &\text{(case of the cosine zero: $\sin\varphi = \pm1$ and $\sin\Omega t = \mp1$)} \\
> \left(M + m\right)g - m\,\frac R2\,\Omega^2 &\ge 0 \;\Rightarrow\; \Omega^2 \le \frac{2\left(M + m\right)g}{mR} \quad &\text{(contact kept; $\ell$ equal to $R/2$)}
> \end{aligned}$$
>
> $$\boxed{\Omega_{\max} = \sqrt{\frac{2\left(M + m\right)g}{mR}}}$$
>
> **Units:** $\sqrt{[\mathrm M][\mathrm{L\,T^{-2}}]/([\mathrm M][\mathrm L])} = [\mathrm{T^{-1}}]$
> **Meaning:** read from the statement: the contact must hold at every instant of that kind, whatever the orientation and the point of the cycle compatible with the equation of motion. With the cosine of $\varphi$ zero the slot is vertical; the worst case is the particle at the upper end of its stroke, where its acceleration, of size $\ell$ times the square of $\Omega$, points down: the cylinder must pull it down and is itself pulled up. With the sine of $\Omega t$ zero, $P$ passes through $C$ with no acceleration and the normal force is the full weight. In both cases no friction is needed at that instant.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Kinematics of $P$ | $\mathbf r_0^P = x_0^C\mathbf i_0 + R\,\mathbf j_0 + x_1^P\mathbf i_1$; $\mathbf v_0^P = \dot x_0^C\mathbf i_0 + \dot x_1^P\mathbf i_1 - x_1^P\dot\varphi\,\mathbf j_1$; $\mathbf a_0^P = \ddot x_0^C\mathbf i_0 + (\ddot x_1^P - x_1^P\dot\varphi^2)\mathbf i_1 - (2\dot x_1^P\dot\varphi + x_1^P\ddot\varphi)\mathbf j_1$; $\mathbf i_1 = \cos\varphi\,\mathbf i_0 - \sin\varphi\,\mathbf j_0$, $\mathbf j_1 = \sin\varphi\,\mathbf i_0 + \cos\varphi\,\mathbf j_0$ |
| (b) Force of $P$ on the cylinder | $\mathbf F = -mg(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0) - m\,\mathbf a_0^P$, applied at $P$ |
| (c) Reduction at $C$ | $\mathbf F^b = (f_A - Mg\sin\gamma)\mathbf i_0 + (N_A - Mg\cos\gamma)\mathbf j_0 + \mathbf F$; $\mathbf M_C^b = (R f_A + x_1^P\,\mathbf F\cdot\mathbf j_1)\mathbf k_0$ |
| (d) Largest slope at rest | $\gamma_{\max} = \min\{\arcsin[m\ell/((M+m)R)],\ \arctan\mu\}$, with $x_1^P = (M+m)R\sin\gamma/m$ |
| (e) Closed system | $[I_z + MR^2 + m(R^2 - 2Rx_1^P\sin\varphi + (x_1^P)^2)]\ddot\varphi + mR(\ddot x_1^P - x_1^P\dot\varphi^2)\cos\varphi - 2mR\dot x_1^P\dot\varphi\sin\varphi + 2mx_1^P\dot x_1^P\dot\varphi - mgx_1^P\cos\varphi = 0$; $x_0^C = x_0^C(0) + R(\varphi - \varphi(0))$; $f_A = MR\ddot\varphi + m\,\mathbf a_0^P\cdot\mathbf i_0$; $N_A = (M+m)g + m\,\mathbf a_0^P\cdot\mathbf j_0$; initial data $\varphi(0)$, $\dot\varphi(0)$ (and $x_0^C(0)$); order $\varphi \to x_0^C \to \mathbf F \to f_A, N_A$ |
| (f) No take-off | $\Omega_{\max} = \sqrt{2(M+m)g/(mR)}$ |

**Check against the official key:** the key (Problems.pdf, p. 81) answers part (b) only, with the equation of motion of the particle written as $m\mathbf a_0^P$ equal to the weight minus $\mathbf F$, and $\mathbf F$ equal to minus $mg(\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf j_0)$ minus $m\mathbf a_0^P$: the same expression as part (b), in the same basis and with the same sign convention. The other parts have no printed answer.

* **No particle.** With $m$ zero the equation of part (e) reduces to $(I_z + MR^2)$ times the second rate of $\varphi$ equal to zero: a cylinder rolling at constant rate on horizontal ground, as it must with no horizontal force.
* **Particle held at the centre.** With $x_1^P$ always zero the bracket becomes $I_z + (M + m)R^2$ and the other terms vanish: the particle at $C$ only adds its mass to the rolling cylinder.
* **Equilibrium on flat ground.** With every rate zero and $x_1^P$ constant, the equation of part (e) leaves $mg\,x_1^P\cos\varphi$ equal to zero: $P$ at the centre or the slot vertical, which is part (d) with $\gamma$ zero (a zero friction and $x_1^P$ zero for a horizontal slot).
* **Part (d) for a small particle.** With $m$ much smaller than $M$ the largest angle tends to zero: a light particle cannot shift the centre of mass far enough to hold the cylinder on a slope.
* **Dimensions.** Every term of the equation of motion is a mass times a squared length times a squared rate, or a mass times $g$ times a length.

---

## Problem RB-42: Gyro on inclined plane

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** two rigid bodies. The sphere $s$, thin, hollow and homogeneous, of mass $m$, radius $R$ and centre $G$, with a massless axle $AB$ fixed to it along a diameter; and the disk $d$, homogeneous, of mass $2m$, centred at $G$ on the axle, free to spin about it (ideal bearing). The sphere rolls without slipping on a fixed plane inclined by $\gamma$ and never leaves it; $C$ is the contact point.
* **Fixed frame:** $S_0\{O; \mathcal B_0\}$, with $O$ on the plane, $\mathbf i_0$ and $\mathbf j_0$ in the plane and $\mathbf k_0$ normal to it, away from it. The plane is at rest, so $S_0$ is inertial.
* **Slope, read from the figure:** the arc of $\gamma$ is drawn between the horizontal ground line and the edge of the plane through $O$ along $\mathbf i_0$, which descends from $O$ to the ground. So $\mathbf i_0$ points down the line of greatest slope and $\mathbf j_0$ is horizontal. With the other reading ($\mathbf j_0$ along the slope) the gravity term below would move from $\xi$ to $\eta$, and nothing else would change.
* **Sphere frame:** $S_s\{G; \mathcal B_s\}$, attached to the sphere, with $\mathbf k_s$ along the axle from $A$ to $B$. Its attitude is given by the 3-1-3 Euler angles: $\psi$ about $\mathbf k_0$ gives $\mathcal B_1$, $\theta$ about $\mathbf i_1$ (the line of nodes) gives $\mathcal B_2$, $\phi$ about $\mathbf k_2$ (equal to $\mathbf k_s$) gives $\mathcal B_s$.
* **Disk frame:** $S_d\{G; \mathcal B_d\}$, attached to the disk, turned by $\beta$ about $\mathbf k_s$ (equal to $\mathbf k_d$) from $\mathcal B_s$.
* **Contact point:** $\mathbf r_0^C$ is $\xi\,\mathbf i_0$ plus $\eta\,\mathbf j_0$ (the dashed lines of the figure, parallel to $\mathbf i_0$ and $\mathbf j_0$).
* **Coordinates and degrees of freedom:** the two bodies have twelve coordinates; the disk shares the centre of the sphere and turns only about the axle (five equations), and contact with the plane fixes the height of $G$ (one equation, Notes.pdf, Eq. 13.1). Six coordinates remain: $\xi$, $\eta$, $\psi$, $\theta$, $\phi$, $\beta$. Rolling without slip adds two conditions on the rates that cannot be integrated (part (c)), so the system keeps six coordinates and has four degrees of freedom (independent velocities), as in Notes.pdf, Sec. 14.1.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass and radius of the sphere | $m$, $R$ | kg, m |
| Mass of the disk | $2m$ | kg |
| Tensor of the sphere at $G$, in $\mathcal B_s$ | $\tfrac23 mR^2\,\mathrm{diag}(1, 1, 1)$ | kg m$^2$ |
| Tensor of the disk at $G$, in $\mathcal B_s$ | $\tfrac16 mR^2\,\mathrm{diag}(1, 1, 2)$ | kg m$^2$ |
| Slope angle | $\gamma$ | rad |
| Coordinates | $\xi$, $\eta$ (m); $\psi$, $\theta$, $\phi$, $\beta$ (rad) | m, rad |
| Gravity | $g$, vertical, downwards | m/s$^2$ |

![[attachments/EM-SOL/rb42-gravity.svg]]

> [!derivation] Gravity in the basis of the plane
> **Law:** components of a vector in a rotated basis; right triangle of the slope
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 12.34; Problems.pdf, p. 71
>
> Vertical section through the line of greatest slope, with $\mathbf j_0$ horizontal. Write $\mathbf e_h$ for the horizontal unit vector along the horizontal projection of $\mathbf i_0$ (drawn to the right) and $\mathbf e_v$ for the upward vertical (drawn up); the product of $\mathbf k_0$ and $\mathbf i_0$ is $\mathbf j_0$, and with $\mathbf i_0$ to the right and $\mathbf k_0$ up it points into the paper (⊗). $\mathbf i_0$ descends by $\gamma$: adjacent leg along $\mathbf e_h$ (cosine), opposite leg along minus $\mathbf e_v$ (sine). $\mathbf k_0$, normal to the plane, leans by $\gamma$ towards the downhill side: adjacent leg along $\mathbf e_v$ (cosine), opposite leg along $\mathbf e_h$ (sine).
>
> $$\begin{aligned}
> \mathbf i_0 &= \cos\gamma\,\mathbf e_h - \sin\gamma\,\mathbf e_v, \qquad \mathbf k_0 = \sin\gamma\,\mathbf e_h + \cos\gamma\,\mathbf e_v \quad &\text{(legs of the two triangles)} \\
> \mathbf i_0\cdot\mathbf k_0 &= \cos\gamma\sin\gamma - \sin\gamma\cos\gamma = 0 \quad &\text{(orthogonal, as they must be)} \\
> \mathbf e_v &= -\sin\gamma\,\mathbf i_0 + \cos\gamma\,\mathbf k_0 \quad &\text{(transpose of the rotation)} \\
> \mathbf g &= -g\,\mathbf e_v \quad &\text{(gravity points down)}
> \end{aligned}$$
>
> $$\boxed{\mathbf g = g\sin\gamma\,\mathbf i_0 - g\cos\gamma\,\mathbf k_0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the component in the plane points down the slope, along plus $\mathbf i_0$, with the sine of $\gamma$; the horizontal $\mathbf j_0$ carries none; the normal component presses the sphere on the plane.

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb42-rot-psi.svg]]

> [!derivation] Part (a): precession, rotation by psi about k0
> **Law:** simple rotation about the third axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View from above the plane with $\mathbf k_0$ out of the paper (⊙), $\mathbf i_0$ to the right and $\mathbf j_0$ up: a positive $\psi$ turns counterclockwise. Triangle of $\mathbf i_1$: hypotenuse 1, adjacent leg along $\mathbf i_0$ (cosine of $\psi$), opposite leg along $\mathbf j_0$ (sine). Triangle of $\mathbf j_1$: adjacent leg along $\mathbf j_0$ (cosine), opposite leg along minus $\mathbf i_0$ (sine), because the counterclockwise turn carries the tip of $\mathbf j_0$ to the left.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} \cos\psi & -\sin\psi & 0 \cr \sin\psi & \cos\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the third row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi & 0 \cr \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0, \qquad \mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0, \qquad \mathbf k_1 = \mathbf k_0}$$
>
> **Units:** dimensionless
> **Meaning:** $\mathbf i_1$ is the line of nodes, the trace in the inclined plane (the intersection of the plane of $\mathbf i_0$, $\mathbf j_0$ with the plane normal to the axle) about which the axle is then tilted; only $\mathbf j_0$ is horizontal.

![[attachments/EM-SOL/rb42-rot-theta.svg]]

> [!derivation] Part (a): nutation, rotation by theta about i1
> **Law:** simple rotation about the first axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View along the line of nodes with $\mathbf i_1$ out of the paper (⊙), $\mathbf j_1$ to the right and $\mathbf k_1$ up; this is right-handed because the product of $\mathbf j_1$ and $\mathbf k_1$ is $\mathbf i_1$. A positive $\theta$ turns counterclockwise. Triangle of $\mathbf j_2$: adjacent leg along $\mathbf j_1$ (cosine of $\theta$), opposite leg along $\mathbf k_1$ (sine). Triangle of $\mathbf k_2$: adjacent leg along $\mathbf k_1$ (cosine), opposite leg along minus $\mathbf j_1$ (sine), because the counterclockwise turn carries the tip of $\mathbf k_1$ to the left.
>
> $$\begin{aligned}
> \mathbf i_2 &= \mathbf i_1, \qquad \mathbf j_2 = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1, \qquad \mathbf k_2 = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \cr 0 & \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf k_1 &= \sin\theta\,\mathbf j_2 + \cos\theta\,\mathbf k_2 \quad &\text{(third row: the inverse is the transpose)}
> \end{aligned}$$
>
> $$\boxed{\mathbf j_2 = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1, \qquad \mathbf k_2 = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1, \qquad \mathbf k_0 = \mathbf k_1 = \sin\theta\,\mathbf j_2 + \cos\theta\,\mathbf k_2}$$
>
> **Units:** dimensionless
> **Meaning:** $\theta$ is the angle between the axle $\mathbf k_2$ and the normal $\mathbf k_0$ of the plane.

![[attachments/EM-SOL/rb42-rot-phi.svg]]

> [!derivation] Part (a): spin of the sphere, rotation by phi about k2, and the full matrix
> **Law:** simple rotation about the third axis; product of rotation matrices
> **Source:** Notes.pdf, Eq. 9.18; Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> View with $\mathbf k_2$ out of the paper (⊙), $\mathbf i_2$ to the right and $\mathbf j_2$ up; a positive $\phi$ turns counterclockwise. Triangle of $\mathbf i_s$: adjacent leg along $\mathbf i_2$ (cosine of $\phi$), opposite leg along $\mathbf j_2$ (sine). Triangle of $\mathbf j_s$: adjacent leg along $\mathbf j_2$ (cosine), opposite leg along minus $\mathbf i_2$ (sine): the counterclockwise turn carries the tip of $\mathbf j_2$ to the left, towards minus $\mathbf i_2$.
>
> $$\begin{aligned}
> \mathbf i_s &= \cos\phi\,\mathbf i_2 + \sin\phi\,\mathbf j_2, \qquad \mathbf j_s = -\sin\phi\,\mathbf i_2 + \cos\phi\,\mathbf j_2, \qquad \mathbf k_s = \mathbf k_2 \quad &\text{(legs of the two triangles)} \\
> [{}_2R_s] &= \begin{bmatrix} \cos\phi & -\sin\phi & 0 \cr \sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_2R_s] = \cos^2\phi + \sin^2\phi = 1 \quad &\text{(columns in $\mathcal B_2$; expand along the third row)} \\
> [{}_2R_s][{}_2R_s]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & \cos\phi\sin\phi - \sin\phi\cos\phi & 0 \cr \sin\phi\cos\phi - \cos\phi\sin\phi & \sin^2\phi + \cos^2\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_2 &= \cos\phi\,\mathbf i_s - \sin\phi\,\mathbf j_s, \qquad \mathbf j_2 = \sin\phi\,\mathbf i_s + \cos\phi\,\mathbf j_s \quad &\text{(rows: the inverse is the transpose)} \\
> [{}_0R_1][{}_1R_2] &= \begin{bmatrix} \cos\psi & -\sin\psi\cos\theta & \sin\psi\sin\theta \cr \sin\psi & \cos\psi\cos\theta & -\cos\psi\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix} \quad &\text{(row of the first times column of the second)} \\
> [{}_0R_s] &= [{}_0R_1][{}_1R_2][{}_2R_s] = \begin{bmatrix} c_\psi c_\phi - s_\psi c_\theta s_\phi & -c_\psi s_\phi - s_\psi c_\theta c_\phi & s_\psi s_\theta \cr s_\psi c_\phi + c_\psi c_\theta s_\phi & -s_\psi s_\phi + c_\psi c_\theta c_\phi & -c_\psi s_\theta \cr s_\theta s_\phi & s_\theta c_\phi & c_\theta \end{bmatrix} \quad &\text{(Eq. 9.19; $c$ and $s$ for cosine and sine)} \\
> \det[{}_0R_s] &= 1\cdot 1\cdot 1 = 1, \qquad [{}_0R_s][{}_0R_s]^T = [U] \quad &\text{(product of the three checked factors)}
> \end{aligned}$$
>
> $$\boxed{\mathbf k_s = \sin\psi\sin\theta\,\mathbf i_0 - \cos\psi\sin\theta\,\mathbf j_0 + \cos\theta\,\mathbf k_0, \qquad \mathbf k_0 = \sin\theta\sin\phi\,\mathbf i_s + \sin\theta\cos\phi\,\mathbf j_s + \cos\theta\,\mathbf k_s}$$
>
> **Units:** dimensionless
> **Meaning:** the third column of $[{}_0R_s]$ is the axle in $\mathcal B_0$; its third row is the normal of the plane in $\mathcal B_s$, both used below.

![[attachments/EM-SOL/rb42-rot-beta.svg]]

> [!derivation] Part (a): disk basis, rotation by beta about ks
> **Law:** simple rotation about the third axis
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Sec. 9.2
>
> Same view as the spin, with $\mathbf k_s$ out of the paper (⊙), $\mathbf i_s$ to the right and $\mathbf j_s$ up; a positive $\beta$ turns counterclockwise, with the same triangles; as for $\phi$, the counterclockwise turn carries the tip of $\mathbf j_s$ to the left, which is the minus sign of the opposite leg of $\mathbf j_d$.
>
> $$\begin{aligned}
> \mathbf i_d &= \cos\beta\,\mathbf i_s + \sin\beta\,\mathbf j_s, \qquad \mathbf j_d = -\sin\beta\,\mathbf i_s + \cos\beta\,\mathbf j_s, \qquad \mathbf k_d = \mathbf k_s \quad &\text{(legs of the two triangles)} \\
> [{}_sR_d] &= \begin{bmatrix} \cos\beta & -\sin\beta & 0 \cr \sin\beta & \cos\beta & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_sR_d] = \cos^2\beta + \sin^2\beta = 1 \quad &\text{(columns in $\mathcal B_s$; expand along the third row)} \\
> [{}_sR_d][{}_sR_d]^T &= \begin{bmatrix} \cos^2\beta + \sin^2\beta & \cos\beta\sin\beta - \sin\beta\cos\beta & 0 \cr \sin\beta\cos\beta - \cos\beta\sin\beta & \sin^2\beta + \cos^2\beta & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_d = \cos\beta\,\mathbf i_s + \sin\beta\,\mathbf j_s, \qquad \mathbf j_d = -\sin\beta\,\mathbf i_s + \cos\beta\,\mathbf j_s, \qquad \mathbf k_d = \mathbf k_s}$$
>
> **Units:** dimensionless
> **Meaning:** the disk differs from the sphere frame only by its turn about the axle.

> [!derivation] Part (b): position of G and angular velocities
> **Law:** sum of segments; composition of angular velocities, each rate along its own axis
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 2.6
>
> The normal of the plane at $C$ is $\mathbf k_0$, so $G$ is at $R$ from $C$ along it. The rates of $\psi$, $\theta$ and $\phi$ act along $\mathbf k_0$, $\mathbf i_1$ and $\mathbf k_s$; $\mathbf i_1$ and $\mathbf k_0$ are written in $\mathcal B_s$ with the previous boxes, and $\mathbf i_1$ and $\mathbf k_s$ in $\mathcal B_0$.
>
> $$\begin{aligned}
> \mathbf r_0^G &= \mathbf r_0^C + \overrightarrow{CG} = \xi\,\mathbf i_0 + \eta\,\mathbf j_0 + R\,\mathbf k_0, \qquad \mathbf v_0^G = \dot\xi\,\mathbf i_0 + \dot\eta\,\mathbf j_0 \quad &\text{(sum of segments; $R$ and $\mathcal B_0$ constant)} \\
> \boldsymbol\omega_{s0} &= \boldsymbol\omega_{s2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\phi\,\mathbf k_s + \dot\theta\,\mathbf i_1 + \dot\psi\,\mathbf k_0 \quad &\text{(composition, Eq. 9.21)} \\
> &= \dot\phi\,\mathbf k_s + \dot\theta\left(\cos\phi\,\mathbf i_s - \sin\phi\,\mathbf j_s\right) + \dot\psi\left(\sin\theta\sin\phi\,\mathbf i_s + \sin\theta\cos\phi\,\mathbf j_s + \cos\theta\,\mathbf k_s\right) \quad &\text{($\mathbf i_1 = \mathbf i_2$ and $\mathbf k_0$ in $\mathcal B_s$)} \\
> &= \dot\phi\left(\sin\psi\sin\theta\,\mathbf i_0 - \cos\psi\sin\theta\,\mathbf j_0 + \cos\theta\,\mathbf k_0\right) + \dot\theta\left(\cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0\right) + \dot\psi\,\mathbf k_0 \quad &\text{($\mathbf k_s$ and $\mathbf i_1$ in $\mathcal B_0$)} \\
> \boldsymbol\omega_{ds} &= \dot\beta\,\mathbf k_s, \qquad \boldsymbol\omega_{d0} = \boldsymbol\omega_{ds} + \boldsymbol\omega_{s0} \quad &\text{(turn about the axle; Eq. 9.21)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf r_0^G = \xi\,\mathbf i_0 + \eta\,\mathbf j_0 + R\,\mathbf k_0, \qquad \boldsymbol\omega_{ds} = \dot\beta\,\mathbf k_s \\ \boldsymbol\omega_{s0} = p\,\mathbf i_s + q\,\mathbf j_s + r\,\mathbf k_s, \quad p = \dot\psi\sin\theta\sin\phi + \dot\theta\cos\phi, \quad q = \dot\psi\sin\theta\cos\phi - \dot\theta\sin\phi, \quad r = \dot\psi\cos\theta + \dot\phi \\ \boldsymbol\omega_{s0} = \left(\dot\theta\cos\psi + \dot\phi\sin\psi\sin\theta\right)\mathbf i_0 + \left(\dot\theta\sin\psi - \dot\phi\cos\psi\sin\theta\right)\mathbf j_0 + \left(\dot\psi + \dot\phi\cos\theta\right)\mathbf k_0 \end{gathered}}$$
>
> **Units:** $[\mathrm L]$; $[\mathrm{T^{-1}}]$ in every component
> **Meaning:** $p$, $q$, $r$ are the components of the angular velocity of the sphere in its own basis; $r$ is the spin about the axle. The components in $\mathcal B_0$ enter the rolling condition; the components in $\mathcal B_s$ enter the momenta, because the tensors are known in $\mathcal B_s$.

#### Part (c): rolling without slip

> [!derivation] Part (c): rolling condition at C
> **Law:** velocity field of the sphere; rolling without slipping on a plane at rest; vector product by its determinant
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 13.5; Notes.pdf, Sec. 13.2
>
> Write $\omega_1$, $\omega_2$, $\omega_3$ for the components of the angular velocity of the sphere in $\mathcal B_0$ (last line of part (b)). The sphere point at $C$ is at minus $R\,\mathbf k_0$ from $G$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{s0}\times\overrightarrow{GC} &= \begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr \omega_1 & \omega_2 & \omega_3 \cr 0 & 0 & -R \end{vmatrix} = -R\omega_2\,\mathbf i_0 + R\omega_1\,\mathbf j_0 \quad &\text{(expand along the first row)} \\
> \mathbf v_0^{C(s)} &= \mathbf v_0^G + \boldsymbol\omega_{s0}\times\overrightarrow{GC} = \left(\dot\xi - R\omega_2\right)\mathbf i_0 + \left(\dot\eta + R\omega_1\right)\mathbf j_0 \quad &\text{(Eq. 9.3; the component along $\mathbf k_0$ is zero: contact kept)} \\
> \mathbf v_0^{C(s)} &= \mathbf 0 \quad &\text{(no slip on the plane at rest, Eq. 13.5)}
> \end{aligned}$$
>
> $$\boxed{\dot\xi = R\left(\dot\theta\sin\psi - \dot\phi\cos\psi\sin\theta\right), \qquad \dot\eta = -R\left(\dot\theta\cos\psi + \dot\phi\sin\psi\sin\theta\right)}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ in every term
> **Meaning:** two scalar relations among the rates. The plane is at rest and the relations hold with no explicit time: the constraint is **stationary**. It is **non-integrable**, as shown in the next box.

> [!derivation] Part (c): why the rolling constraint is non-integrable
> **Law:** a constraint is integrable when it is the time derivative of relations among the coordinates; composition of finite rotations
> **Source:** Notes.pdf, Sec. 13.2; Notes.pdf, Sec. 14.1
>
> The formal test (the Frobenius condition, or the set of configurations reachable from one point) is an **extension**. A direct sign of non-integrability: roll the sphere round a square path of side $L$ with no turn about $\mathbf k_0$, and follow the material point that starts at the top, along $\mathbf k_0$ from $G$. Rolling by $L$ along plus $\mathbf i_0$ needs, by the box above, a rotation about plus $\mathbf j_0$ by $L/R$; along plus $\mathbf j_0$, about minus $\mathbf i_0$; then the opposite ones. Take $L$ equal to $\pi R/2$, so each turn is a right angle.
>
> $$\begin{aligned}
> \mathbf k_0 &\mapsto \mathbf i_0 \quad &\text{(quarter turn about $\mathbf j_0$; $\mathbf j_0\times\mathbf k_0 = \mathbf i_0$)} \\
> \mathbf i_0 &\mapsto \mathbf i_0 \quad &\text{(quarter turn about $-\mathbf i_0$: the point is on the axis)} \\
> \mathbf i_0 &\mapsto \mathbf k_0 \quad &\text{(quarter turn about $-\mathbf j_0$; $-\mathbf j_0\times\mathbf i_0 = \mathbf k_0$)} \\
> \mathbf k_0 &\mapsto -\mathbf j_0 \quad &\text{(quarter turn about $\mathbf i_0$; $\mathbf i_0\times\mathbf k_0 = -\mathbf j_0$)}
> \end{aligned}$$
>
> $$\boxed{\text{non-integrable: } C \text{ returns to its start, the top point ends along } -\mathbf j_0}$$
>
> **Units:** dimensionless (directions)
> **Meaning:** the attitude is not a function of $\xi$ and $\eta$ along the motion. That alone rules out three relations; to rule out two, pivot the sphere about the vertical $\mathbf k_0$ with the contact point at rest (this keeps the velocity of $C$ equal to zero) and note that the loop changes the vertical component of a material direction, which a pivot cannot. So the attitudes reachable with the contact point at a fixed place form a set of at least two dimensions, while two relations among $\xi$, $\eta$, $\psi$, $\theta$, $\phi$ would leave only one. That is why the six coordinates must be kept with four independent velocities.

### Center of Mass and Inertia Tensor

> [!derivation] Inertia tensors of the hollow sphere and of the disk
> **Law:** moments and products of inertia as surface integrals (sphere: jacobian $R^2\sin\vartheta$; disk: jacobian $\rho$); symmetry
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.13; Notes.pdf, Eq. 10.15; [Lecture 8, Slide 16]
>
> The statement gives both tensors; the integrals check them. Sphere: surface density $\sigma_s$, polar angle $\vartheta$ from $\mathbf k_s$, squared distance to the axle $R^2\sin^2\vartheta$. Disk: thin, of radius $a$ (not given), surface density $\sigma_d$, polar coordinates $(\rho, \chi)$ in its plane with $\chi$ from $\mathbf i_s$, squared distances $\rho^2$ to the axle and $\rho^2\sin^2\chi$ to the diameter along $\mathbf i_s$. Both centres of mass are at $G$ and the products of inertia vanish, by the symmetries of each body.
>
> $$\begin{aligned}
> m &= \sigma_s\int_0^{2\pi}\!\!\int_0^{\pi}R^2\sin\vartheta\,d\vartheta\,d\chi = \sigma_s R^2\left[\chi\right]_0^{2\pi}\left[-\cos\vartheta\right]_0^{\pi} = 4\pi\sigma_s R^2 \quad &\text{(antiderivatives; Barrow's rule)} \\
> I^s &= \sigma_s\int_0^{2\pi}\!\!\int_0^{\pi}R^2\sin^2\vartheta\,R^2\sin\vartheta\,d\vartheta\,d\chi = \sigma_s R^4\cdot 2\pi\left[-\cos\vartheta + \frac{\cos^3\vartheta}{3}\right]_0^{\pi} = \sigma_s R^4\cdot 2\pi\cdot\frac43 = \frac23 mR^2 \quad &\text{(Barrow's rule: $\tfrac23 + \tfrac23$)} \\
> 2m &= \sigma_d\int_0^{2\pi}\!\!\int_0^{a}\rho\,d\rho\,d\chi = \sigma_d\cdot 2\pi\left[\frac{\rho^2}{2}\right]_0^{a} = \pi\sigma_d a^2 \quad &\text{(Barrow's rule)} \\
> I_3^d &= \sigma_d\int_0^{2\pi}\!\!\int_0^{a}\rho^2\,\rho\,d\rho\,d\chi = \sigma_d\cdot 2\pi\left[\frac{\rho^4}{4}\right]_0^{a} = \frac{\pi\sigma_d a^4}{2} = m a^2 \quad &\text{(axle: squared distance $\rho^2$)} \\
> I_1^d &= \sigma_d\int_0^{2\pi}\sin^2\chi\,d\chi\int_0^{a}\rho^3\,d\rho = \sigma_d\left[\frac{\chi}{2} - \frac{\sin 2\chi}{4}\right]_0^{2\pi}\frac{a^4}{4} = \frac{\pi\sigma_d a^4}{4} = \frac{m a^2}{2} = I_2^d \quad &\text{(diameters; Barrow's rule)} \\
> m a^2 &= \frac{mR^2}{3} \;\Rightarrow\; a = \frac{R}{\sqrt3} \quad &\text{(compare with the statement)} \\
> [{}_sR_d]\,\mathrm{diag}\left(1, 1, 2\right)[{}_sR_d]^T &= \mathrm{diag}\left(\cos^2\beta + \sin^2\beta,\ \sin^2\beta + \cos^2\beta,\ 2\right) \quad &\text{(the off-diagonal terms cancel)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}{}^{\,s}_G = \frac23 mR^2\,[U], \qquad \bar{\bar I}{}^{\,d}_G = \frac{mR^2}{6}\begin{bmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 2 \end{bmatrix} \ \text{in } \mathcal B_s \text{ and in } \mathcal B_d}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the tensors of the statement, with the ratio 2 between the axial and the transverse moment of a thin disk; they imply a disk of radius $R$ over the square root of 3. Since the disk tensor is the same in $\mathcal B_s$ and in $\mathcal B_d$, it is constant in $\mathcal B_s$, which does not spin with the disk.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (f): total angular momentum about G
> **Law:** angular momentum of each body about its centre of mass; sum over the bodies
> **Source:** Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 13.12; [Lecture 9, Slide 5]
>
> Both centres of mass are at $G$, so each body contributes its tensor at $G$ times its angular velocity, and the sum is the angular momentum of the system about its centre of mass. The angular velocity of the disk has the components $p$, $q$ and $r$ plus the rate of $\beta$ in $\mathcal B_s$.
>
> $$\begin{aligned}
> \mathbf H_{G}^s &= \frac23 mR^2\left(p\,\mathbf i_s + q\,\mathbf j_s + r\,\mathbf k_s\right) \quad &\text{(Eq. 11.12)} \\
> \mathbf H_{G}^d &= \frac{mR^2}{6}\left(p\,\mathbf i_s + q\,\mathbf j_s + 2\left(r + \dot\beta\right)\mathbf k_s\right) \quad &\text{(Eq. 11.12; tensor in $\mathcal B_s$)} \\
> \mathbf H_{G} &= \mathbf H_{G}^s + \mathbf H_{G}^d = mR^2\left(\frac23 + \frac16\right)\left(p\,\mathbf i_s + q\,\mathbf j_s\right) + mR^2\left(\frac23 r + \frac13 r + \frac13\dot\beta\right)\mathbf k_s \quad &\text{(sum, component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G} = mR^2\left[\frac56\left(\dot\psi\sin\theta\sin\phi + \dot\theta\cos\phi\right)\mathbf i_s + \frac56\left(\dot\psi\sin\theta\cos\phi - \dot\theta\sin\phi\right)\mathbf j_s + \left(\dot\psi\cos\theta + \dot\phi + \frac13\dot\beta\right)\mathbf k_s\right]}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-1}}]$
> **Meaning:** the transverse part sees the sphere and the disk together (five sixths of $mR^2$); along the axle the disk adds its own spin. With the disk locked to the sphere the system would be a single body with axial moment $mR^2$.

> [!derivation] Part (f): total kinetic energy
> **Law:** Koenig's theorem for each body, both centred at $G$
> **Source:** Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 11.37; [Lecture 9, Slide 9]
>
> The translational part uses the velocity of $G$ of part (b), whose square is the sum of the squares of the rates of $\xi$ and $\eta$; with the rolling condition the cross terms cancel ($\cos^2\psi + \sin^2\psi = 1$).
>
> $$\begin{aligned}
> T &= \frac12\left(m + 2m\right)\left(\dot\xi^2 + \dot\eta^2\right) + \frac12\cdot\frac23 mR^2\left(p^2 + q^2 + r^2\right) + \frac12\cdot\frac{mR^2}{6}\left(p^2 + q^2 + 2\left(r + \dot\beta\right)^2\right) \quad &\text{(Eq. 11.31 for each body)} \\
> p^2 + q^2 &= \dot\psi^2\sin^2\theta\left(\sin^2\phi + \cos^2\phi\right) + \dot\theta^2\left(\cos^2\phi + \sin^2\phi\right) + 2\dot\psi\dot\theta\sin\theta\left(\sin\phi\cos\phi - \cos\phi\sin\phi\right) = \dot\psi^2\sin^2\theta + \dot\theta^2 \quad &\text{(squares of part (b))} \\
> \dot\xi^2 + \dot\eta^2 &= R^2\left(\dot\theta^2 + \dot\phi^2\sin^2\theta\right) \quad &\text{(squares of part (c); cross terms cancel)}
> \end{aligned}$$
>
> $$\boxed{T = \frac32 m\left(\dot\xi^2 + \dot\eta^2\right) + mR^2\left[\frac{5}{12}\left(\dot\psi^2\sin^2\theta + \dot\theta^2\right) + \frac13\left(\dot\psi\cos\theta + \dot\phi\right)^2 + \frac16\left(\dot\psi\cos\theta + \dot\phi + \dot\beta\right)^2\right], \qquad \dot\xi^2 + \dot\eta^2 = R^2\left(\dot\theta^2 + \dot\phi^2\sin^2\theta\right)}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, J in every term
> **Meaning:** five twelfths come from one third (sphere) plus one twelfth (disk) for the transverse rotation; the axial rotation of the sphere and the spin of the disk enter separately.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb42-exploded.svg]]

#### Part (d): exploded view and reactions

The exploded view separates the disk, the sphere with its axle, and the plane. The plane acts on the sphere at $C$ with a force of three unknown components (normal and friction; bilateral, since the sphere cannot leave the plane) and no torque (point contact). The axle acts on the disk through the ideal bearing at $G$: a force of three components (it keeps the centre of the disk at $G$) and a torque normal to the axle, with no component along $\mathbf k_s$ because the disk spins freely; the disk acts on the axle, and so on the sphere, with the opposite force and torque (third law of Newton). The plane is held by its supports, which are not needed.

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the sphere | $s$ | $G$ | $m\,\mathbf g = mg(\sin\gamma\,\mathbf i_0 - \cos\gamma\,\mathbf k_0)$ | applied |
| Plane on the sphere | $s$ | $C$ | $\mathbf R_C = F_1\,\mathbf i_0 + F_2\,\mathbf j_0 + N\,\mathbf k_0$ | constraint (pair) |
| Sphere on the plane | plane | $C$ | $-\mathbf R_C$ | constraint (pair) |
| Axle on the disk | $d$ | $G$ | $\mathbf R_d = X_d\,\mathbf i_s + Y_d\,\mathbf j_s + Z_d\,\mathbf k_s$ and torque $\mathbf M_d = M_1\,\mathbf i_s + M_2\,\mathbf j_s$ | constraint (pair) |
| Disk on the axle (sphere) | $s$ | $G$ | $-\mathbf R_d$ and torque $-\mathbf M_d$ | constraint (pair) |
| Weight of the disk | $d$ | $G$ | $2m\,\mathbf g$ | applied |

> [!derivation] Part (e): forces and torques on the sphere reduced at G
> **Law:** sum of forces; moment of a force about a point; vector product by its determinant
> **Source:** Notes.pdf, Eq. 12.4; Notes.pdf, Eq. 12.14; Notes.pdf, Eq. 13.9
>
> The weight and the bearing force $-\mathbf R_d$ act at $G$ and have no moment about it; the arm of the contact force is $\overrightarrow{GC}$, minus $R\,\mathbf k_0$; the bearing torque $-\mathbf M_d$ adds as it is.
>
> $$\begin{aligned}
> \mathbf F^s &= mg\left(\sin\gamma\,\mathbf i_0 - \cos\gamma\,\mathbf k_0\right) + F_1\,\mathbf i_0 + F_2\,\mathbf j_0 + N\,\mathbf k_0 - \mathbf R_d \quad &\text{(sum of the forces)} \\
> \overrightarrow{GC}\times\mathbf R_C &= \begin{vmatrix} \mathbf i_0 & \mathbf j_0 & \mathbf k_0 \cr 0 & 0 & -R \cr F_1 & F_2 & N \end{vmatrix} = \mathbf i_0\left(0 + R F_2\right) - \mathbf j_0\left(0 + R F_1\right) + \mathbf k_0\left(0 - 0\right) \quad &\text{(expand along the first row)} \\
> \mathbf M_G^s &= R F_2\,\mathbf i_0 - R F_1\,\mathbf j_0 - M_1\,\mathbf i_s - M_2\,\mathbf j_s \quad &\text{(Eq. 12.14 with the torque of the bearing)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F^s = \left(mg\sin\gamma + F_1\right)\mathbf i_0 + F_2\,\mathbf j_0 + \left(N - mg\cos\gamma\right)\mathbf k_0 - X_d\,\mathbf i_s - Y_d\,\mathbf j_s - Z_d\,\mathbf k_s, \qquad \mathbf M_G^s = R F_2\,\mathbf i_0 - R F_1\,\mathbf j_0 - M_1\,\mathbf i_s - M_2\,\mathbf j_s}$$
>
> **Units:** N; N m
> **Meaning:** eight unknowns ($F_1$, $F_2$, $N$, $X_d$, $Y_d$, $Z_d$, $M_1$, $M_2$) enter the equations of the sphere. Among the forces, only the friction at $C$ has a moment about $G$, and that moment has no component along $\mathbf k_0$ (the third entry of the determinant is zero); part (g) uses this.

#### Part (g): first integrals

> [!derivation] Part (g): moment equation of the disk and its spin integral
> **Law:** moment equation about the centre of mass; derivative in $S_0$ of a vector known in $\mathcal B_s$ (gyroscopic term)
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.20; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 13.10
>
> On the disk act its weight and $\mathbf R_d$, both at $G$, and the torque $\mathbf M_d$; the pole $G$ is its centre of mass, so the pole term vanishes. The components of $\mathbf H_G^d$ are taken in $\mathcal B_s$, where the tensor of the disk is constant, and the frame $S_s$ turns with $\boldsymbol\omega_{s0}$.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0 &= \left.\frac{d\mathbf H_G^d}{dt}\right|_s + \boldsymbol\omega_{s0}\times\mathbf H_G^d \quad &\text{(Eq. 3.8 with the frame $S_s$)} \\
> \left.\frac{d\mathbf H_G^d}{dt}\right|_s &= \frac{mR^2}{6}\left(\dot p\,\mathbf i_s + \dot q\,\mathbf j_s + 2\left(\dot r + \ddot\beta\right)\mathbf k_s\right) \quad &\text{(derivatives of the components)} \\
> \boldsymbol\omega_{s0}\times\mathbf H_G^d &= \frac{mR^2}{6}\begin{vmatrix} \mathbf i_s & \mathbf j_s & \mathbf k_s \cr p & q & r \cr p & q & 2\left(r + \dot\beta\right) \end{vmatrix} = \frac{mR^2}{6}\left[q\left(2r + 2\dot\beta - r\right)\mathbf i_s - p\left(2r + 2\dot\beta - r\right)\mathbf j_s + \left(pq - qp\right)\mathbf k_s\right] \quad &\text{(expand along the first row)} \\
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0 &= \mathbf M_d = M_1\,\mathbf i_s + M_2\,\mathbf j_s \quad &\text{(Eq. 12.13 for the disk at $G$)} \\
> \frac{mR^2}{3}\left(\dot r + \ddot\beta\right) + 0 &= 0 \quad &\text{(component along $\mathbf k_s$)} \\
> \left[r + \dot\beta\right]_0^t &= 0 \;\Rightarrow\; r + \dot\beta = \left(r + \dot\beta\right)\big|_{t = 0} \quad &\text{(integrate from 0 to $t$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\dot\psi\cos\theta + \dot\phi + \dot\beta = n_0 \ \ (\text{constant}), \qquad M_1 = \frac{mR^2}{6}\left(\dot p + q\left(r + 2\dot\beta\right)\right), \qquad M_2 = \frac{mR^2}{6}\left(\dot q - p\left(r + 2\dot\beta\right)\right)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ for the integral; N m for the torques
> **Meaning:** the spin of the disk about the axle, measured in $S_0$ (the dot product of its angular velocity with $\mathbf k_s$), keeps its initial value although the axle turns, for two reasons: the moment about the axle is zero (free bearing, forces through $G$) and the gyroscopic term has no component along the axle, because the two transverse moments of the disk are equal. The transverse components give the torque that the axle must apply to turn the spinning disk.

> [!derivation] Part (g): power of the forces and the energy integral
> **Law:** power of the forces on each body; equal velocities at a rolling contact and at the bearing; potential of the weight; energy theorem
> **Source:** Notes.pdf, Eq. 12.29; Notes.pdf, Eq. 12.30; Notes.pdf, Eq. 12.33; Notes.pdf, Eq. 12.34
>
> $$\begin{aligned}
> \dot W^{C} &= \mathbf R_C\cdot\mathbf v_0^{C(s)} = \mathbf R_C\cdot\mathbf 0 = 0 \quad &\text{(no slip on the plane at rest)} \\
> \dot W^{\mathrm{bearing}} &= \mathbf R_d\cdot\mathbf v_0^G + \mathbf M_d\cdot\boldsymbol\omega_{d0} - \mathbf R_d\cdot\mathbf v_0^G - \mathbf M_d\cdot\boldsymbol\omega_{s0} = \mathbf M_d\cdot\dot\beta\,\mathbf k_s = 0 \quad &\text{(Eq. 12.29 on both bodies at $G$; torque normal to $\mathbf k_s$)} \\
> \dot W^{g} &= 3m\,\mathbf g\cdot\mathbf v_0^G = 3mg\sin\gamma\,\dot\xi = -\frac{d}{dt}\left(-3mg\sin\gamma\,\xi\right) \quad &\text{(Eq. 12.34; both weights at $G$; chain rule)} \\
> \frac{d}{dt}\left(T + V\right) &= \dot W^{C} + \dot W^{\mathrm{bearing}} = 0, \qquad V = -3mg\sin\gamma\,\xi \quad &\text{(Eq. 12.30; constant term of $V$ dropped)} \\
> \left[T + V\right]_0^t &= 0 \;\Rightarrow\; T + V = \left(T + V\right)\big|_{t = 0} \equiv E \quad &\text{(integrate from 0 to $t$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\frac32 mR^2\left(\dot\theta^2 + \dot\phi^2\sin^2\theta\right) + mR^2\left[\frac{5}{12}\left(\dot\psi^2\sin^2\theta + \dot\theta^2\right) + \frac13\left(\dot\psi\cos\theta + \dot\phi\right)^2 + \frac16\left(\dot\psi\cos\theta + \dot\phi + \dot\beta\right)^2\right] - 3mg\sin\gamma\,\xi = E}$$
>
> **Units:** J in every term
> **Meaning:** no reaction does work: the contact point of the sphere is at rest, the bearing force acts on points with the same velocity, and the bearing torque is normal to the relative rotation. As $\xi$ grows (the sphere goes down the slope) the potential term falls and the kinetic energy grows.

> [!derivation] Part (g): a further first integral, the angular momentum about G along the normal of the plane
> **Law:** moment equation of the system about its centre of mass; internal pairs cancel; projection on a fixed direction
> **Source:** Notes.pdf, Eq. 13.12; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 11.12
>
> On the whole system the bearing force and torque are internal pairs and cancel; the weights act at $G$; only the contact force has a moment about $G$, given in part (e). The direction $\mathbf k_0$ is fixed in $S_0$, so no gyroscopic term appears when the equation is projected on it. The normal $\mathbf k_0$ in $\mathcal B_s$ is the third row of $[{}_0R_s]$.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G}{dt}\right|_0 &= \overrightarrow{GC}\times\mathbf R_C = R F_2\,\mathbf i_0 - R F_1\,\mathbf j_0 \quad &\text{(Eq. 13.12 at $G$)} \\
> \frac{d}{dt}\left(\mathbf H_G\cdot\mathbf k_0\right) &= \left.\frac{d\mathbf H_G}{dt}\right|_0\cdot\mathbf k_0 + \mathbf H_G\cdot\mathbf 0 = 0 \quad &\text{(product rule; $\mathbf k_0$ fixed)} \\
> \mathbf H_G\cdot\mathbf k_0 &= mR^2\left[\frac56\sin\theta\left(p\sin\phi + q\cos\phi\right) + \left(r + \frac13\dot\beta\right)\cos\theta\right] \quad &\text{(part (f) dotted with the third row)} \\
> p\sin\phi + q\cos\phi &= \dot\psi\sin\theta\left(\sin^2\phi + \cos^2\phi\right) + \dot\theta\left(\cos\phi\sin\phi - \sin\phi\cos\phi\right) = \dot\psi\sin\theta \quad &\text{(part (b))}
> \end{aligned}$$
>
> $$\boxed{mR^2\left[\frac56\,\dot\psi\sin^2\theta + \left(\dot\psi\cos\theta + \dot\phi + \frac13\dot\beta\right)\cos\theta\right] = H_0 \ \ (\text{constant})}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-1}}]$
> **Meaning:** the contact force passes at the distance $R$ below $G$ along the normal, so its moment about $G$ is always parallel to the plane and cannot change the normal component of the angular momentum. The statement asks for two first integrals; this third one holds too.

> [!derivation] Check: rolling straight down the slope with the axle horizontal
> **Law:** the two first integrals on a particular motion, compared with Newton's second law and the moment equation of the whole system
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.12
>
> Take $\psi$ zero and $\theta$ a right angle, both constant: the axle $\mathbf k_s$ is minus $\mathbf j_0$ (third column of $[{}_0R_s]$), horizontal; then $p$ and $q$ are zero and $r$ is the rate of $\phi$, part (c) gives the rate of $\xi$ equal to minus $R$ times the rate of $\phi$ and the rate of $\eta$ zero. The spin integral gives the second rate of $\beta$ equal to minus that of $\phi$. Write $\Phi$ for the rate of $\phi$.
>
> $$\begin{aligned}
> T + V &= \frac32 mR^2\Phi^2 + \frac13 mR^2\Phi^2 + \frac16 mR^2 n_0^2 - 3mg\sin\gamma\,\xi \quad &\text{(energy integral on this motion)} \\
> 0 &= \frac{11}{3} mR^2\Phi\dot\Phi + 3mg\sin\gamma\,R\,\Phi \;\Rightarrow\; \dot\Phi = -\frac{9\,g\sin\gamma}{11\,R} \quad &\text{(time derivative; chain rule, with the rate of $\xi$ equal to $-R\Phi$)} \\
> \mathbf H_G &= -mR^2\left(\Phi + \frac13\dot\beta\right)\mathbf j_0, \qquad \left.\frac{d\mathbf H_G}{dt}\right|_0 = -mR^2\left(\dot\Phi - \frac13\dot\Phi\right)\mathbf j_0 = -\frac23 mR^2\dot\Phi\,\mathbf j_0 \quad &\text{(part (f); $\mathbf j_0$ fixed; spin integral)} \\
> -\frac23 mR^2\dot\Phi\,\mathbf j_0 &= R F_2\,\mathbf i_0 - R F_1\,\mathbf j_0 \;\Rightarrow\; F_2 = 0,\ F_1 = \frac23 mR\dot\Phi \quad &\text{(system moment equation at $G$: the bearing pairs cancel)} \\
> 3m\ddot\xi &= 3mg\sin\gamma + F_1 \;\Rightarrow\; -3mR\dot\Phi = 3mg\sin\gamma + \frac23 mR\dot\Phi \;\Rightarrow\; \dot\Phi = -\frac{9\,g\sin\gamma}{11\,R} \quad &\text{(system force equation along $\mathbf i_0$)}
> \end{aligned}$$
>
> $$\boxed{\ddot\xi = -R\dot\Phi = \frac{9}{11}\,g\sin\gamma \ \text{by both routes}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the centre accelerates down the slope at nine elevenths of the sine of $\gamma$ times $g$: the mass $3m$ is pulled by $3mg\sin\gamma$, but only the sphere (moment two thirds of $mR^2$) has to be spun up, because the spin of the disk about the horizontal axle stays constant; 3 over 3 plus two thirds is nine elevenths. The friction $F_1$ is negative, up the slope, as it must be to spin the sphere forwards.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Changes of basis | $\mathbf i_1 = \cos\psi\,\mathbf i_0 + \sin\psi\,\mathbf j_0$, $\mathbf j_1 = -\sin\psi\,\mathbf i_0 + \cos\psi\,\mathbf j_0$, $\mathbf k_1 = \mathbf k_0$; $\mathbf i_2 = \mathbf i_1$, $\mathbf j_2 = \cos\theta\,\mathbf j_1 + \sin\theta\,\mathbf k_1$, $\mathbf k_2 = -\sin\theta\,\mathbf j_1 + \cos\theta\,\mathbf k_1$; $\mathbf i_s = \cos\phi\,\mathbf i_2 + \sin\phi\,\mathbf j_2$, $\mathbf j_s = -\sin\phi\,\mathbf i_2 + \cos\phi\,\mathbf j_2$, $\mathbf k_s = \mathbf k_2$; full matrix $[{}_0R_s]$ in the box of the spin |
| (b) Position and angular velocities | $\mathbf r_0^G = \xi\,\mathbf i_0 + \eta\,\mathbf j_0 + R\,\mathbf k_0$; $\boldsymbol\omega_{s0} = \dot\psi\,\mathbf k_0 + \dot\theta\,\mathbf i_1 + \dot\phi\,\mathbf k_s = (\dot\psi\sin\theta\sin\phi + \dot\theta\cos\phi)\mathbf i_s + (\dot\psi\sin\theta\cos\phi - \dot\theta\sin\phi)\mathbf j_s + (\dot\psi\cos\theta + \dot\phi)\mathbf k_s$; $\boldsymbol\omega_{ds} = \dot\beta\,\mathbf k_s$ |
| (c) Rolling constraint | $\dot\xi = R(\dot\theta\sin\psi - \dot\phi\cos\psi\sin\theta)$, $\dot\eta = -R(\dot\theta\cos\psi + \dot\phi\sin\psi\sin\theta)$; non-integrable, stationary |
| (d) Exploded view | Plane on sphere at $C$: $\mathbf R_C = F_1\mathbf i_0 + F_2\mathbf j_0 + N\mathbf k_0$ (no torque); axle on disk at $G$: $\mathbf R_d$ (three components) and $\mathbf M_d = M_1\mathbf i_s + M_2\mathbf j_s$ (none along the axle); opposite pairs on the sphere and on the plane; weights $m\mathbf g$ and $2m\mathbf g$ at $G$ |
| (e) Resultant on the sphere at $G$ | $\mathbf F^s = m\mathbf g + \mathbf R_C - \mathbf R_d$; $\mathbf M_G^s = RF_2\,\mathbf i_0 - RF_1\,\mathbf j_0 - M_1\mathbf i_s - M_2\mathbf j_s$; $\mathbf g = g\sin\gamma\,\mathbf i_0 - g\cos\gamma\,\mathbf k_0$ |
| (f) Angular momentum and kinetic energy | $\mathbf H_G = mR^2[\tfrac56 p\,\mathbf i_s + \tfrac56 q\,\mathbf j_s + (r + \tfrac13\dot\beta)\mathbf k_s]$; $T = \tfrac32 m(\dot\xi^2 + \dot\eta^2) + mR^2[\tfrac{5}{12}(\dot\psi^2\sin^2\theta + \dot\theta^2) + \tfrac13(\dot\psi\cos\theta + \dot\phi)^2 + \tfrac16(\dot\psi\cos\theta + \dot\phi + \dot\beta)^2]$ |
| (g) First integrals | Spin of the disk: $\dot\psi\cos\theta + \dot\phi + \dot\beta = n_0$; energy: $T - 3mg\sin\gamma\,\xi = E$; also $\mathbf H_G\cdot\mathbf k_0 = mR^2[\tfrac56\dot\psi\sin^2\theta + (\dot\psi\cos\theta + \dot\phi + \tfrac13\dot\beta)\cos\theta] = H_0$ |

**Limiting cases and consistency:** the key prints no answer for this problem (Problems.pdf, pp. 77 to 81 checked).

* **Straight descent.** The last box of the previous section finds the acceleration of the centre down the slope, nine elevenths of $g\sin\gamma$, both from the two first integrals and from Newton's law with the moment equation: the integrals agree with the equations of motion on that motion.
* **Horizontal plane.** With $\gamma$ zero the potential term vanishes and the kinetic energy itself is constant.
* **No disk.** With the mass and the tensor of the disk set to zero, part (f) leaves the hollow sphere alone (moment two thirds of $mR^2$, isotropic), the spin integral disappears with the disk, and the normal component of the angular momentum about $G$ becomes two thirds of $mR^2$ times the component of the angular velocity along $\mathbf k_0$, which the moment equation keeps constant as before.
* **Dimensions.** Every term of the energy integral is a mass times a squared length times a squared rate, or a weight times a length; the spin integral is a rate.

---

## Problem RB-30: Free spinning asteroid (Poinsot's construction)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** one rigid body, the asteroid $b$, of mass $m$ and centre of mass $G$, floating in space with no force and no torque acting on it.
* **Inertial frame:** $S_0\{G; \mathcal B_0\}$, with $\mathcal B_0$ made of $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$, given as inertial by the statement. With no force the centre of mass moves with constant velocity (first box of the equations of motion), so a frame with origin $G$ and fixed directions is inertial.
* **Body frame:** $S_b\{G; \mathcal B_b\}$, with $\mathcal B_b$ made of $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$ attached to the asteroid. The figure of the statement labels these vectors $\mathbf e_1$, $\mathbf e_2$, $\mathbf e_3$ (read from the figure: $\mathbf e_1$ is $\mathbf i_b$, $\mathbf e_2$ is $\mathbf j_b$, $\mathbf e_3$ is $\mathbf k_b$, and the label of $\mathbf e_3$ says it is also $\mathbf k_2$, the axis of the last rotation).
* **Euler angles 1-2-3:** $\psi$ about $\mathbf i_0$ gives $\mathcal B_1$; $\theta$ about $\mathbf j_1$ gives $\mathcal B_2$; $\phi$ about $\mathbf k_2$ gives $\mathcal B_b$.
* **Degrees of freedom:** the three coordinates of $G$ and the three Euler angles. The motion of $G$ is trivial (constant velocity) and $G$ is the origin of $S_0$, so only the three angles remain to be studied.
* **Point $P$:** the point with position vector from $G$ equal to $\tau\ell$ times the angular velocity, components $x_b$, $y_b$, $z_b$ in $\mathcal B_b$. It moves both in $S_b$ and in $S_0$; since both frames have their origin at $G$, its position vector is the same arrow in both.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Mass of the asteroid | $m$ | kg |
| Characteristic length and time | $\ell$, $\tau$ | m, s |
| Tensor of inertia at $G$, in $\mathcal B_b$ | $m\ell^2\,\mathrm{diag}(2, 4, 8)$, so $I_x = 2m\ell^2$, $I_y = 4m\ell^2$, $I_z = 8m\ell^2$ | kg m$^2$ |
| Initial angles | $(\psi_0, \theta_0, \phi_0) = (\pi/3, 0, \pi/2)$ | rad |
| Initial rates | $(\dot\psi_0, \dot\theta_0, \dot\phi_0) = (-2, 0, 1)/\tau$ | rad/s |
| Components of the angular velocity in $\mathcal B_b$ | $\omega_{xb}$, $\omega_{yb}$, $\omega_{zb}$ | rad/s |
| Coordinates of $P$ in $\mathcal B_b$ | $x_b = \tau\ell\,\omega_{xb}$, $y_b = \tau\ell\,\omega_{yb}$, $z_b = \tau\ell\,\omega_{zb}$ | m |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb30-rot-psi.svg]]

> [!derivation] Part (a): first rotation, psi about i0
> **Law:** simple rotation about the first axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View along $\mathbf i_0$ with $\mathbf i_0$ out of the paper (⊙), $\mathbf j_0$ to the right and $\mathbf k_0$ up; this is right-handed because the product of $\mathbf j_0$ and $\mathbf k_0$ is $\mathbf i_0$. A positive $\psi$ turns counterclockwise. Triangle of $\mathbf j_1$: hypotenuse 1, adjacent leg along $\mathbf j_0$ (cosine of $\psi$), opposite leg along $\mathbf k_0$ (sine). Triangle of $\mathbf k_1$: adjacent leg along $\mathbf k_0$ (cosine), opposite leg along minus $\mathbf j_0$ (sine), because the counterclockwise turn carries the tip of $\mathbf k_0$, which points up, to the left.
>
> $$\begin{aligned}
> \mathbf i_1 &= \mathbf i_0, \qquad \mathbf j_1 = \cos\psi\,\mathbf j_0 + \sin\psi\,\mathbf k_0, \qquad \mathbf k_1 = -\sin\psi\,\mathbf j_0 + \cos\psi\,\mathbf k_0 \quad &\text{(legs of the two triangles)} \\
> [{}_0R_1] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\psi & -\sin\psi \cr 0 & \sin\psi & \cos\psi \end{bmatrix} \quad &\text{(columns: $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ in $\mathcal B_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos^2\psi + \sin^2\psi\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_0R_1][{}_0R_1]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\psi + \sin^2\psi & \cos\psi\sin\psi - \sin\psi\cos\psi \cr 0 & \sin\psi\cos\psi - \cos\psi\sin\psi & \sin^2\psi + \cos^2\psi \end{bmatrix} = [U] \quad &\text{(row by row products)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_1 = \mathbf i_0, \qquad \mathbf j_1 = \cos\psi\,\mathbf j_0 + \sin\psi\,\mathbf k_0, \qquad \mathbf k_1 = -\sin\psi\,\mathbf j_0 + \cos\psi\,\mathbf k_0}$$
>
> **Units:** dimensionless
> **Meaning:** the first turn leaves $\mathbf i_0$ in place and tilts the other two axes in the plane normal to it.

![[attachments/EM-SOL/rb30-rot-theta.svg]]

> [!derivation] Part (a): second rotation, theta about j1
> **Law:** simple rotation about the second axis; right-hand rule
> **Source:** Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View along $\mathbf j_1$ with $\mathbf j_1$ out of the paper (⊙), $\mathbf k_1$ to the right and $\mathbf i_1$ up; this is right-handed because the product of $\mathbf k_1$ and $\mathbf i_1$ is $\mathbf j_1$. A positive $\theta$ turns counterclockwise. Triangle of $\mathbf k_2$: adjacent leg along $\mathbf k_1$ (cosine of $\theta$), opposite leg along $\mathbf i_1$ (sine), because the counterclockwise turn carries the tip of $\mathbf k_1$, which points right, upwards. Triangle of $\mathbf i_2$: adjacent leg along $\mathbf i_1$ (cosine), opposite leg along minus $\mathbf k_1$ (sine), because the same turn carries the tip of $\mathbf i_1$, which points up, to the left. This is why the minus sign of a rotation about the second axis sits under the diagonal (third row, first column), unlike the rotations about the first and third axes, where it sits above the diagonal.
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1, \qquad \mathbf j_2 = \mathbf j_1, \qquad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1 \quad &\text{(legs of the two triangles)} \\
> [{}_1R_2] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr 0 & 1 & 0 \cr -\sin\theta & 0 & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_2$, $\mathbf j_2$, $\mathbf k_2$ in $\mathcal B_1$)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the second row)} \\
> [{}_1R_2][{}_1R_2]^T &= \begin{bmatrix} \cos^2\theta + \sin^2\theta & 0 & -\cos\theta\sin\theta + \sin\theta\cos\theta \cr 0 & 1 & 0 \cr -\sin\theta\cos\theta + \cos\theta\sin\theta & 0 & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_1 &= \cos\theta\,\mathbf i_2 + \sin\theta\,\mathbf k_2 \quad &\text{(first row: the inverse is the transpose)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_2 = \cos\theta\,\mathbf i_1 - \sin\theta\,\mathbf k_1, \qquad \mathbf j_2 = \mathbf j_1, \qquad \mathbf k_2 = \sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf k_1, \qquad \mathbf i_0 = \mathbf i_1 = \cos\theta\,\mathbf i_2 + \sin\theta\,\mathbf k_2}$$
>
> **Units:** dimensionless
> **Meaning:** $\theta$ is the angle between $\mathbf k_2$ (the last axis, $\mathbf k_b$) and $\mathbf k_1$; the last relation is used for the angular velocity in part (b).

![[attachments/EM-SOL/rb30-rot-phi.svg]]

> [!derivation] Part (a): third rotation, phi about k2, and the full matrix
> **Law:** simple rotation about the third axis; product of rotation matrices
> **Source:** Notes.pdf, Eq. 9.16; Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> View along $\mathbf k_2$ with $\mathbf k_2$ out of the paper (⊙), $\mathbf i_2$ to the right and $\mathbf j_2$ up; a positive $\phi$ turns counterclockwise. Triangle of $\mathbf i_b$: adjacent leg along $\mathbf i_2$ (cosine of $\phi$), opposite leg along $\mathbf j_2$ (sine). Triangle of $\mathbf j_b$: adjacent leg along $\mathbf j_2$ (cosine), opposite leg along minus $\mathbf i_2$ (sine), because the counterclockwise turn carries the tip of $\mathbf j_2$, which points up, to the left.
>
> $$\begin{aligned}
> \mathbf i_b &= \cos\phi\,\mathbf i_2 + \sin\phi\,\mathbf j_2, \qquad \mathbf j_b = -\sin\phi\,\mathbf i_2 + \cos\phi\,\mathbf j_2, \qquad \mathbf k_b = \mathbf k_2 \quad &\text{(legs of the two triangles)} \\
> [{}_2R_b] &= \begin{bmatrix} \cos\phi & -\sin\phi & 0 \cr \sin\phi & \cos\phi & 0 \cr 0 & 0 & 1 \end{bmatrix}, \qquad \det[{}_2R_b] = 1\cdot\left(\cos^2\phi + \sin^2\phi\right) = 1 \quad &\text{(columns in $\mathcal B_2$; expand along the third row)} \\
> [{}_2R_b][{}_2R_b]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & \cos\phi\sin\phi - \sin\phi\cos\phi & 0 \cr \sin\phi\cos\phi - \cos\phi\sin\phi & \sin^2\phi + \cos^2\phi & 0 \cr 0 & 0 & 1 \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf i_2 &= \cos\phi\,\mathbf i_b - \sin\phi\,\mathbf j_b, \qquad \mathbf j_2 = \sin\phi\,\mathbf i_b + \cos\phi\,\mathbf j_b \quad &\text{(rows: the inverse is the transpose)} \\
> [{}_0R_1][{}_1R_2] &= \begin{bmatrix} \cos\theta & 0 & \sin\theta \cr \sin\psi\sin\theta & \cos\psi & -\sin\psi\cos\theta \cr -\cos\psi\sin\theta & \sin\psi & \cos\psi\cos\theta \end{bmatrix} \quad &\text{(row of the first times column of the second)} \\
> [{}_0R_b] &= [{}_0R_1][{}_1R_2][{}_2R_b] = \begin{bmatrix} c_\theta c_\phi & -c_\theta s_\phi & s_\theta \cr c_\psi s_\phi + s_\psi s_\theta c_\phi & c_\psi c_\phi - s_\psi s_\theta s_\phi & -s_\psi c_\theta \cr s_\psi s_\phi - c_\psi s_\theta c_\phi & s_\psi c_\phi + c_\psi s_\theta s_\phi & c_\psi c_\theta \end{bmatrix} \quad &\text{(Eq. 9.19 for this sequence; $c$ and $s$ for cosine and sine)} \\
> \det[{}_0R_b] &= 1\cdot 1\cdot 1 = 1, \qquad [{}_0R_b][{}_0R_b]^T = [{}_0R_1][{}_1R_2][{}_2R_b][{}_2R_b]^T[{}_1R_2]^T[{}_0R_1]^T = [U] \quad &\text{(product of the three checked factors)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf i_b = \cos\theta\cos\phi\,\mathbf i_0 + \left(\cos\psi\sin\phi + \sin\psi\sin\theta\cos\phi\right)\mathbf j_0 + \left(\sin\psi\sin\phi - \cos\psi\sin\theta\cos\phi\right)\mathbf k_0 \\ \mathbf j_b = -\cos\theta\sin\phi\,\mathbf i_0 + \left(\cos\psi\cos\phi - \sin\psi\sin\theta\sin\phi\right)\mathbf j_0 + \left(\sin\psi\cos\phi + \cos\psi\sin\theta\sin\phi\right)\mathbf k_0 \\ \mathbf k_b = \sin\theta\,\mathbf i_0 - \sin\psi\cos\theta\,\mathbf j_0 + \cos\psi\cos\theta\,\mathbf k_0 \end{gathered}}$$
>
> **Units:** dimensionless
> **Meaning:** the three columns of $[{}_0R_b]$ are the body vectors in $\mathcal B_0$. Each column has unit length; for the third, the sum of the squares is the square of the sine of $\theta$ plus the square of its cosine times the sum of the squares of the sine and cosine of $\psi$, which is 1.

> [!derivation] Initial attitude of the body basis
> **Law:** the matrix of the previous box evaluated at the initial angles
> **Source:** Notes.pdf, Eq. 9.19; Problems.pdf, p. 60
>
> At the initial instant the sine of $\theta$ is 0 and its cosine 1, the sine of $\phi$ is 1 and its cosine 0, the cosine of $\psi$ is one half and its sine is the square root of 3 over 2.
>
> $$\begin{aligned}
> [{}_0R_b]_{t = 0} &= \begin{bmatrix} 1\cdot 0 & -1\cdot 1 & 0 \cr \tfrac12\cdot 1 + \tfrac{\sqrt3}{2}\cdot 0\cdot 0 & \tfrac12\cdot 0 - \tfrac{\sqrt3}{2}\cdot 0\cdot 1 & -\tfrac{\sqrt3}{2}\cdot 1 \cr \tfrac{\sqrt3}{2}\cdot 1 - \tfrac12\cdot 0\cdot 0 & \tfrac{\sqrt3}{2}\cdot 0 + \tfrac12\cdot 0\cdot 1 & \tfrac12\cdot 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 0 \cr \tfrac12 & 0 & -\tfrac{\sqrt3}{2} \cr \tfrac{\sqrt3}{2} & 0 & \tfrac12 \end{bmatrix} \quad &\text{(substitution, entry by entry)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b(0) = \tfrac12\,\mathbf j_0 + \tfrac{\sqrt3}{2}\,\mathbf k_0, \qquad \mathbf j_b(0) = -\mathbf i_0, \qquad \mathbf k_b(0) = -\tfrac{\sqrt3}{2}\,\mathbf j_0 + \tfrac12\,\mathbf k_0}$$
>
> **Units:** dimensionless
> **Meaning:** at the start the intermediate axis $\mathbf j_b$ points along minus $\mathbf i_0$ and the other two lie in the plane of $\mathbf j_0$ and $\mathbf k_0$; the angular momentum in $\mathcal B_0$ in part (d) uses this matrix.

> [!derivation] Part (b): angular velocity of the asteroid in the body basis
> **Law:** composition of angular velocities, each rate along its own axis
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Sec. 15.1
>
> The rate of $\psi$ acts along $\mathbf i_0$, the rate of $\theta$ along $\mathbf j_1$ and the rate of $\phi$ along $\mathbf k_2$. Each of them is written in $\mathcal B_b$ with the boxes of part (a): $\mathbf k_2$ is $\mathbf k_b$; $\mathbf j_1$ is $\mathbf j_2$; $\mathbf i_0$ is $\mathbf i_1$, written in $\mathcal B_2$ and then in $\mathcal B_b$.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{b2} + \boldsymbol\omega_{21} + \boldsymbol\omega_{10} = \dot\phi\,\mathbf k_2 + \dot\theta\,\mathbf j_1 + \dot\psi\,\mathbf i_0 \quad &\text{(composition, Eq. 9.21)} \\
> \mathbf i_0 &= \cos\theta\left(\cos\phi\,\mathbf i_b - \sin\phi\,\mathbf j_b\right) + \sin\theta\,\mathbf k_b \quad &\text{(second box, then the rows of the third)} \\
> \mathbf j_1 &= \mathbf j_2 = \sin\phi\,\mathbf i_b + \cos\phi\,\mathbf j_b \quad &\text{(third box)} \\
> \boldsymbol\omega_{b0} &= \dot\phi\,\mathbf k_b + \dot\theta\left(\sin\phi\,\mathbf i_b + \cos\phi\,\mathbf j_b\right) + \dot\psi\left(\cos\theta\cos\phi\,\mathbf i_b - \cos\theta\sin\phi\,\mathbf j_b + \sin\theta\,\mathbf k_b\right) \quad &\text{(substitution)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \left(\dot\psi\cos\theta\cos\phi + \dot\theta\sin\phi\right)\mathbf i_b + \left(-\dot\psi\cos\theta\sin\phi + \dot\theta\cos\phi\right)\mathbf j_b + \left(\dot\psi\sin\theta + \dot\phi\right)\mathbf k_b}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every component
> **Meaning:** these are the components of the statement, in order the first, second and third components of the angular velocity in $\mathcal B_b$; they enter the momenta because the tensor is known in $\mathcal B_b$.

> [!derivation] Initial angular velocity and initial position of P
> **Law:** the expression of part (b) evaluated at the initial angles and rates; definition of $P$
> **Source:** Notes.pdf, Eq. 9.21; Problems.pdf, p. 60
>
> The rates are the first time derivatives of the angles; at the initial instant they are given, minus 2, 0 and 1 over $\tau$; the sines and cosines are those of the previous box.
>
> $$\begin{aligned}
> \omega_{xb}(0) &= \left(-\frac2\tau\right)\cdot 1\cdot 0 + 0\cdot 1 = 0 \quad &\text{(first component)} \\
> \omega_{yb}(0) &= -\left(-\frac2\tau\right)\cdot 1\cdot 1 + 0\cdot 0 = \frac2\tau \quad &\text{(second component)} \\
> \omega_{zb}(0) &= \left(-\frac2\tau\right)\cdot 0 + \frac1\tau = \frac1\tau \quad &\text{(third component)} \\
> \mathbf r_b^P(0) &= \tau\ell\left(0\,\mathbf i_b + \frac2\tau\,\mathbf j_b + \frac1\tau\,\mathbf k_b\right) = \ell\left(2\,\mathbf j_b + \mathbf k_b\right) \quad &\text{(definition of $P$)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0}(0) = \frac1\tau\left(0\,\mathbf i_b + 2\,\mathbf j_b + \mathbf k_b\right), \qquad (x_b, y_b, z_b)_{t = 0} = \ell\,(0, 2, 1)}$$
>
> **Units:** $[\mathrm{T^{-1}}]$; $[\mathrm{T}][\mathrm L][\mathrm{T^{-1}}] = [\mathrm L]$
> **Meaning:** the initial angular velocity lies in the plane of $\mathbf j_b$ and $\mathbf k_b$; the cosine of its angle with $\mathbf k_b$ is 1 over the square root of 5 (63.4 degrees) and with $\mathbf j_b$ it is 2 over the square root of 5 (26.6 degrees), so it is geometrically closer to the intermediate axis $\mathbf j_b$. Part (f) shows that it nevertheless circulates about $\mathbf k_b$.

### Center of Mass and Inertia Tensor

$G$ is the centre of mass by the statement, and the tensor at $G$ is given in $\mathcal B_b$ with no products of inertia, so $\mathcal B_b$ is a principal basis with $I_x$, $I_y$, $I_z$ equal to 2, 4 and 8 times $m\ell^2$ (minor, intermediate and major axes); the shape is irregular and not described, so there is no integral to set up. The tensor is constant in $\mathcal B_b$ because the basis is attached to the body.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Part (c): kinetic energy of the asteroid
> **Law:** Koenig's theorem; rotational energy about $G$ with the tensor in the principal basis
> **Source:** Notes.pdf, Eq. 11.31; Notes.pdf, Eq. 15.20
>
> $G$ is the origin of the inertial frame $S_0$ of the statement, so its velocity in $S_0$ is zero and only the rotational part remains.
>
> $$\begin{aligned}
> T_0^b &= \frac12 m\left|\mathbf v_0^G\right|^2 + \frac12\,\boldsymbol\omega_{b0}\cdot\bar{\bar I}_G\cdot\boldsymbol\omega_{b0} \quad &\text{(Koenig, Eq. 11.31)} \\
> \bar{\bar I}_G\cdot\boldsymbol\omega_{b0} &= m\ell^2\left(2\omega_{xb}\,\mathbf i_b + 4\omega_{yb}\,\mathbf j_b + 8\omega_{zb}\,\mathbf k_b\right) \quad &\text{(diagonal tensor times the components)} \\
> T_0^b &= 0 + \frac12 m\ell^2\left(2\omega_{xb}^2 + 4\omega_{yb}^2 + 8\omega_{zb}^2\right) \quad &\text{(dot product with the angular velocity)} \\
> T_0^b(0) &= \frac12 m\ell^2\left(2\cdot 0 + 4\cdot\frac{4}{\tau^2} + 8\cdot\frac{1}{\tau^2}\right) = \frac12 m\ell^2\cdot\frac{24}{\tau^2} \quad &\text{(initial components)}
> \end{aligned}$$
>
> $$\boxed{T_0^b = m\ell^2\left(\omega_{xb}^2 + 2\omega_{yb}^2 + 4\omega_{zb}^2\right), \qquad T_0^b(0) = 12\,\frac{m\ell^2}{\tau^2}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-2}}]$, J
> **Meaning:** the energy weighs each component with its principal moment; the initial value comes from the components along $\mathbf j_b$ (16 of the 24 units) and $\mathbf k_b$ (8 units).

> [!derivation] Part (d): angular momentum about G
> **Law:** angular momentum of a rigid body about its centre of mass; change of basis to $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 11.21; Notes.pdf, Eq. 15.9
>
> $$\begin{aligned}
> \mathbf H_{G0}^b &= \bar{\bar I}_G\cdot\boldsymbol\omega_{b0} = m\ell^2\left(2\omega_{xb}\,\mathbf i_b + 4\omega_{yb}\,\mathbf j_b + 8\omega_{zb}\,\mathbf k_b\right) \quad &\text{(Eq. 11.21 at $G$, Eq. 15.9)} \\
> \mathbf H_{G0}^b(0) &= m\ell^2\left(2\cdot 0\,\mathbf i_b + 4\cdot\frac2\tau\,\mathbf j_b + 8\cdot\frac1\tau\,\mathbf k_b\right) = \frac{m\ell^2}{\tau}\left(8\,\mathbf j_b + 8\,\mathbf k_b\right) \quad &\text{(initial components)} \\
> \left|\mathbf H_{G0}^b\right| &= \frac{m\ell^2}{\tau}\sqrt{0 + 64 + 64} = 8\sqrt2\,\frac{m\ell^2}{\tau} \quad &\text{(orthonormal basis)} \\
> \left[\mathbf H_{G0}^b(0)\right]_0 &= [{}_0R_b]_{t = 0}\begin{bmatrix} 0 \cr 8 \cr 8 \end{bmatrix}\frac{m\ell^2}{\tau} = \begin{bmatrix} 0 - 8 + 0 \cr 0 + 0 - 4\sqrt3 \cr 0 + 0 + 4 \end{bmatrix}\frac{m\ell^2}{\tau} \quad &\text{(initial matrix times the body components)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G0}^b = m\ell^2\left(2\omega_{xb}\,\mathbf i_b + 4\omega_{yb}\,\mathbf j_b + 8\omega_{zb}\,\mathbf k_b\right), \qquad \mathbf H_{G0}^b(0) = \frac{m\ell^2}{\tau}\left(-8\,\mathbf i_0 - 4\sqrt3\,\mathbf j_0 + 4\,\mathbf k_0\right), \qquad \left|\mathbf H_{G0}^b\right| = 8\sqrt2\,\frac{m\ell^2}{\tau}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-1}}]$
> **Meaning:** the angular momentum is not parallel to the angular velocity (the components 0, 8, 8 against 0, 2, 1); the check of the magnitude in $\mathcal B_0$ gives 64 plus 48 plus 16, which is 128, the square of 8 times the square root of 2.

### Free-Body Diagram and Equations of Motion

No force acts on the asteroid (it floats freely in space): the free-body diagram is the body alone, with no load, and the resultant and the moment about $G$ are zero.

> [!derivation] Conservation of momentum and angular momentum; Euler's equations
> **Law:** force equation; moment equation about the centre of mass; derivative of a vector known in the body basis
> **Source:** Notes.pdf, Eq. 15.6; Notes.pdf, Eq. 15.7; Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 15.11; Notes.pdf, Eq. 15.12; Notes.pdf, Eq. 15.13
>
> The pole of the moment equation is $G$, the centre of mass, so the pole term (the velocity of $G$ times the linear momentum, which is a vector times a multiple of itself) is zero. The angular velocity in the vector product is written with its components in $\mathcal B_b$.
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= \mathbf 0 \;\Rightarrow\; \mathbf v_0^G = \text{const} \quad &\text{(Eq. 15.6: no force)} \\
> \left.\frac{d\mathbf H_{G0}^b}{dt}\right|_0 &= \mathbf M_G - \mathbf v_0^G\times m\,\mathbf v_0^G = \mathbf 0 - \mathbf 0 \quad &\text{(Eq. 12.13 at $G$, Eq. 15.7)} \\
> \left.\frac{d\mathbf H_{G0}^b}{dt}\right|_0 &= \left.\frac{d\mathbf H_{G0}^b}{dt}\right|_b + \boldsymbol\omega_{b0}\times\mathbf H_{G0}^b \quad &\text{(Eq. 3.8 with the frame $S_b$)} \\
> \boldsymbol\omega_{b0}\times\mathbf H_{G0}^b &= m\ell^2\begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \omega_{xb} & \omega_{yb} & \omega_{zb} \cr 2\omega_{xb} & 4\omega_{yb} & 8\omega_{zb} \end{vmatrix} = m\ell^2\left[\left(8 - 4\right)\omega_{yb}\omega_{zb}\,\mathbf i_b - \left(8 - 2\right)\omega_{xb}\omega_{zb}\,\mathbf j_b + \left(4 - 2\right)\omega_{xb}\omega_{yb}\,\mathbf k_b\right] \quad &\text{(expand along the first row)} \\
> \mathbf 0 &= m\ell^2\left(2\dot\omega_{xb}\,\mathbf i_b + 4\dot\omega_{yb}\,\mathbf j_b + 8\dot\omega_{zb}\,\mathbf k_b\right) + \boldsymbol\omega_{b0}\times\mathbf H_{G0}^b \quad &\text{(derivatives of the components in $S_b$, constant tensor)} \\
> \dot\omega_{xb}(0) &= -2\cdot\frac2\tau\cdot\frac1\tau = -\frac{4}{\tau^2}, \qquad \dot\omega_{yb}(0) = \frac32\cdot\frac1\tau\cdot 0 = 0, \qquad \dot\omega_{zb}(0) = -\frac14\cdot 0\cdot\frac2\tau = 0 \quad &\text{(previous row, component by component, at the initial instant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{G0}^b = \text{const in } S_0, \qquad \dot\omega_{xb} = -2\,\omega_{yb}\omega_{zb}, \qquad \dot\omega_{yb} = \frac32\,\omega_{zb}\omega_{xb}, \qquad \dot\omega_{zb} = -\frac14\,\omega_{xb}\omega_{yb}}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$ for the force equation; $[\mathrm{T^{-2}}]$ in each of Euler's equations
> **Meaning:** these are Euler's equations with no torque for moments 2, 4 and 8 (each component equation divided by its moment). At the start only the first component changes, and it becomes negative: the tip of the angular velocity leaves the plane of $\mathbf j_b$ and $\mathbf k_b$ towards minus $\mathbf i_b$.

> [!derivation] Conservation of kinetic energy
> **Law:** time derivative of the rotational energy with a constant tensor in the body basis; Euler's equations
> **Source:** Notes.pdf, Eq. 15.20; Notes.pdf, Eq. 15.10
>
> $$\begin{aligned}
> \frac{dT_0^b}{dt} &= m\ell^2\left(2\omega_{xb}\dot\omega_{xb} + 4\omega_{yb}\dot\omega_{yb} + 8\omega_{zb}\dot\omega_{zb}\right) \quad &\text{(chain rule on each square of the part (c) box)} \\
> &= m\ell^2\left(-4\,\omega_{xb}\omega_{yb}\omega_{zb} + 6\,\omega_{xb}\omega_{yb}\omega_{zb} - 2\,\omega_{xb}\omega_{yb}\omega_{zb}\right) = 0 \quad &\text{(Euler's equations of the previous box)} \\
> \left[T_0^b\right]_0^t &= 0 \;\Rightarrow\; T_0^b(t) = T_0^b(0) \quad &\text{(integrate from 0 to $t$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{T_0^b = 12\,\frac{m\ell^2}{\tau^2}\ \text{at all times}}$$
>
> **Units:** J
> **Meaning:** with no force there is no power, and the energy keeps its initial value; the three terms cancel because 4 minus 8, 8 minus 2 and 2 minus 4 add up to zero.

> [!derivation] Part (c): the body-fixed ellipsoid of P
> **Law:** constant kinetic energy written with the coordinates of $P$
> **Source:** Notes.pdf, Eq. 15.29
>
> Each angular velocity component is the matching coordinate of $P$ divided by $\tau\ell$.
>
> $$\begin{aligned}
> T_0^b &= m\ell^2\,\frac{x_b^2 + 2y_b^2 + 4z_b^2}{\tau^2\ell^2} = \frac{m}{\tau^2}\left(x_b^2 + 2y_b^2 + 4z_b^2\right) \quad &\text{(substitution in the part (c) box)} \\
> x_b^2 + 2y_b^2 + 4z_b^2 &= \frac{\tau^2}{m}\,T_0^b = \frac{\tau^2}{m}\cdot 12\,\frac{m\ell^2}{\tau^2} = 12\,\ell^2 \quad &\text{(energy constant)} \\
> \frac{x_b^2}{12} + \frac{y_b^2}{6} + \frac{z_b^2}{3} &= \ell^2 \quad &\text{(division by 12: the form of the hint)} \\
> a_x &= \sqrt{12}\,\ell, \qquad a_y = \sqrt6\,\ell, \qquad a_z = \sqrt3\,\ell \quad &\text{(semi-axes: set two coordinates to zero)} \\
> \frac{0}{12} + \frac{4}{6} + \frac{1}{3} &= 1 \quad &\text{(check with the initial $P$, in units of $\ell$)}
> \end{aligned}$$
>
> $$\boxed{\frac{x_b^2}{12} + \frac{y_b^2}{6} + \frac{z_b^2}{3} = \ell^2, \qquad a_x = 2\sqrt3\,\ell \approx 3.464\,\ell,\quad a_y = \sqrt6\,\ell \approx 2.449\,\ell,\quad a_z = \sqrt3\,\ell \approx 1.732\,\ell}$$
>
> **Units:** $[\mathrm L^2]$ in every term; semi-axes $[\mathrm L]$
> **Meaning:** the coordinates are in $\mathcal B_b$ and the right-hand side is constant, so $P$ stays on an ellipsoid fixed to the asteroid (the inertia ellipsoid of the notes, scaled by $\tau\ell$). The largest moment, along $\mathbf k_b$, gives the shortest semi-axis; the ratios of the semi-axes are the square roots of 4, 2 and 1.

> [!derivation] Part (d): the component of the angular velocity along the angular momentum
> **Law:** kinetic energy as half the dot product of angular velocity and angular momentum; both constant
> **Source:** Notes.pdf, Eq. 15.30; Notes.pdf, Eq. 15.31
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0}\cdot\mathbf H_{G0}^b &= m\ell^2\left(2\omega_{xb}^2 + 4\omega_{yb}^2 + 8\omega_{zb}^2\right) = 2T_0^b \quad &\text{(components in $\mathcal B_b$; part (c) box)} \\
> \omega_H &\equiv \boldsymbol\omega_{b0}\cdot\frac{\mathbf H_{G0}^b}{\left|\mathbf H_{G0}^b\right|} = \frac{2T_0^b}{\left|\mathbf H_{G0}^b\right|} \quad &\text{(definition of the component)} \\
> \omega_H &= \frac{24\,m\ell^2/\tau^2}{8\sqrt2\,m\ell^2/\tau} = \frac{3}{\sqrt2\,\tau} \quad &\text{(constant values of both boxes)} \\
> \omega_H(0) &= \frac{\left(0, 2, 1\right)\cdot\left(0, 8, 8\right)}{8\sqrt2\,\tau} = \frac{24}{8\sqrt2\,\tau} \quad &\text{(check with the initial components)}
> \end{aligned}$$
>
> $$\boxed{\omega_H = \frac{3\sqrt2}{2\,\tau} \approx \frac{2.121}{\tau}\ \text{(constant)}}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]/[\mathrm{M\,L^2\,T^{-1}}] = [\mathrm{T^{-1}}]$
> **Meaning:** the angular velocity changes in direction and size, but its projection on the fixed direction of the angular momentum stays the same, because the energy and the magnitude of the angular momentum are both constant.

> [!derivation] Part (d): the invariant plane of P and its distance from G
> **Law:** projection of the position of $P$ on the fixed unit vector of the angular momentum
> **Source:** Notes.pdf, Eq. 15.31; Notes.pdf, Sec. 15.4
>
> Write $\mathbf u_H$ for the unit vector of the angular momentum. It is constant in $S_0$ (first box of this section), and $G$ is the origin of $S_0$.
>
> $$\begin{aligned}
> \mathbf u_H &= \frac{1}{8\sqrt2}\left(-8\,\mathbf i_0 - 4\sqrt3\,\mathbf j_0 + 4\,\mathbf k_0\right) = -\frac{1}{\sqrt2}\,\mathbf i_0 - \frac{\sqrt3}{2\sqrt2}\,\mathbf j_0 + \frac{1}{2\sqrt2}\,\mathbf k_0 \quad &\text{(part (d) box, divided by the magnitude)} \\
> \mathbf r_b^P\cdot\mathbf u_H &= \tau\ell\,\boldsymbol\omega_{b0}\cdot\mathbf u_H = \tau\ell\,\omega_H = \tau\ell\cdot\frac{3\sqrt2}{2\,\tau} \quad &\text{(definition of $P$; previous box)} \\
> \mathbf r_b^P(0)\cdot\mathbf u_H &= \ell\,\frac{\left(0, 2, 1\right)\cdot\left(0, 8, 8\right)}{8\sqrt2} = \frac{24}{8\sqrt2}\,\ell \quad &\text{(check with the initial $P$, components in $\mathcal B_b$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_b^P\cdot\mathbf u_H = \delta, \qquad \delta = \frac{3\sqrt2}{2}\,\ell \approx 2.121\,\ell, \qquad \mathbf u_H = -\frac{1}{\sqrt2}\,\mathbf i_0 - \frac{\sqrt6}{4}\,\mathbf j_0 + \frac{\sqrt2}{4}\,\mathbf k_0}$$
>
> **Units:** $[\mathrm T][\mathrm L][\mathrm{T^{-1}}] = [\mathrm L]$
> **Meaning:** the points whose projection on a fixed unit vector has a fixed value form a plane normal to that vector, fixed in $S_0$, at the distance $\delta$ from $G$: this is the invariant plane. The distance lies between the shortest and the intermediate semi-axes (1.732, 2.121 and 2.449 times $\ell$), which the plane needs in order to touch the ellipsoid (it only requires a value between the shortest and the longest); being below the intermediate semi-axis is what puts the polhode around the major axis, and part (f) uses this order.

![[attachments/EM-SOL/rb30-poinsot.svg]]

> [!derivation] Part (e): the ellipsoid and the plane are tangent at P
> **Law:** the gradient of an implicit surface is normal to it; a weighted Cauchy-Schwarz inequality
> **Source:** Notes.pdf, Eq. 15.32; Problems.pdf, p. 81
>
> Write the ellipsoid of part (c) as $F$ equal to $12\ell^2$, with $F$ the sum of the square of $x_b$, twice the square of $y_b$ and four times the square of $z_b$. Its normal at $P$ is the gradient of $F$ there; the plane of part (d) has the normal $\mathbf u_H$. $P$ lies on both surfaces (parts (c) and (d)). For the last rows, $Q$ is any point of the ellipsoid with coordinates $x$, $y$, $z$, and the inequality is the Cauchy-Schwarz inequality for the inner product with weights 1, 2 and 4.
>
> $$\begin{aligned}
> \nabla F\big|_P &= 2x_b\,\mathbf i_b + 4y_b\,\mathbf j_b + 8z_b\,\mathbf k_b = 2\tau\ell\left(\omega_{xb}\,\mathbf i_b + 2\omega_{yb}\,\mathbf j_b + 4\omega_{zb}\,\mathbf k_b\right) \quad &\text{(partial derivatives; definition of $P$)} \\
> &= 2\tau\ell\cdot\frac{\mathbf H_{G0}^b}{2m\ell^2} = \frac{\tau}{m\ell}\,\mathbf H_{G0}^b \quad &\text{(part (d) box: components 2, 4, 8 times $m\ell^2$)} \\
> \mathbf r^Q\cdot\mathbf H_{G0}^b &= \frac{2m\ell}{\tau}\left(x\,x_b + 2\,y\,y_b + 4\,z\,z_b\right) \quad &\text{(the components of the angular momentum in terms of $P$)} \\
> &\le \frac{2m\ell}{\tau}\sqrt{x^2 + 2y^2 + 4z^2}\,\sqrt{x_b^2 + 2y_b^2 + 4z_b^2} = \frac{2m\ell}{\tau}\cdot 12\ell^2 = \mathbf r_b^P\cdot\mathbf H_{G0}^b \quad &\text{(Cauchy-Schwarz; both points on the ellipsoid)}
> \end{aligned}$$
>
> $$\boxed{\nabla F\big|_P = \frac{\tau}{m\ell}\,\mathbf H_{G0}^b\ \parallel\ \mathbf u_H, \qquad \mathbf r^Q\cdot\mathbf u_H \le \delta \ \text{for every point } Q \text{ of the ellipsoid}}$$
>
> **Units:** $[\mathrm L]$ for the gradient, and $[\mathrm T][\mathrm{M\,L^2\,T^{-1}}]/([\mathrm M][\mathrm L]) = [\mathrm L]$ for its expression; $[\mathrm L][\mathrm{M\,L^2\,T^{-1}}]$ on both sides of the inequality
> **Meaning:** at $P$ the normal of the ellipsoid and the normal of the plane are the same direction, which is the statement of the key; the surfaces share the point and the tangent plane, so they are tangent there. The inequality adds that the whole ellipsoid stays on the side of the plane where $G$ is: the plane touches it at $P$ and never cuts it.

#### Part (f): motion of the ellipsoid on the plane

> [!derivation] Part (f): the ellipsoid rolls without slipping on the invariant plane
> **Law:** velocity field of a rigid body; the vector product of a vector with itself is zero
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Sec. 15.4
>
> The material point of the asteroid (or of its ellipsoid) that is at $P$ at a given instant has the velocity of the field of the body at that position; $G$ is at rest in $S_0$.
>
> $$\begin{aligned}
> \mathbf v_0^{P(b)} &= \mathbf v_0^G + \boldsymbol\omega_{b0}\times\mathbf r_b^P \quad &\text{(Eq. 9.3)} \\
> &= \mathbf 0 + \boldsymbol\omega_{b0}\times\tau\ell\,\boldsymbol\omega_{b0} = \tau\ell\left(\boldsymbol\omega_{b0}\times\boldsymbol\omega_{b0}\right) = \mathbf 0 \quad &\text{(definition of $P$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^{P(b)} = \mathbf 0: \ \text{the ellipsoid rolls without slipping on the fixed plane, with its centre } G \text{ fixed at the distance } \delta}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** $P$ lies on the instantaneous axis of rotation (the line through $G$ along the angular velocity), so the body point in contact is at rest at every instant. The contact point moves over the ellipsoid along a body-fixed curve (the polhode) and over the plane along a curve fixed in $S_0$ (the herpolhode).

![[attachments/EM-SOL/rb30-polhode.svg]]

> [!derivation] Part (f): the polhode of this motion
> **Law:** intersection of the energy ellipsoid with the ellipsoid of constant magnitude of the angular momentum
> **Source:** Notes.pdf, Eq. 15.29; Notes.pdf, Eq. 15.33; Notes.pdf, Sec. 15.4
>
> In units of the inverse of $\tau$, the energy gives the first row and the square of the magnitude of the angular momentum (divided by the square of $m\ell^2$) gives the second; the other rows combine them to remove one component at a time.
>
> $$\begin{aligned}
> 2\omega_{xb}^2 + 4\omega_{yb}^2 + 8\omega_{zb}^2 &= 24 \quad &\text{(twice the energy, divided by $m\ell^2$)} \\
> 4\omega_{xb}^2 + 16\omega_{yb}^2 + 64\omega_{zb}^2 &= 128 \quad &\text{(square of the magnitude, Eq. 15.33)} \\
> 3\omega_{xb}^2 + 4\omega_{yb}^2 &= 16 \quad &\text{(8 times the first row minus the second, divided by 4)} \\
> 8\omega_{zb}^2 - \omega_{xb}^2 &= 8 \quad &\text{(the second row minus 4 times the first, divided by 4)} \\
> \omega_{yb}^2 + 6\,\omega_{zb}^2 &= 10 \quad &\text{(the second row minus 2 times the first, divided by 8)} \\
> \omega_{zb}^2 &= 1 + \frac{\omega_{xb}^2}{8} \ge 1, \qquad \omega_{xb}^2 \le \frac{16}{3}, \qquad \omega_{yb}^2 \le 4 \quad &\text{(ranges: squares are non-negative)}
> \end{aligned}$$
>
> $$\boxed{\text{polhode: } 3\omega_{xb}^2 + 4\omega_{yb}^2 = \frac{16}{\tau^2}, \quad 1 \le \tau\omega_{zb} \le \sqrt{5/3} \approx 1.291, \quad \left|\tau\omega_{xb}\right| \le \frac{4}{\sqrt3} \approx 2.309, \quad \left|\tau\omega_{yb}\right| \le 2}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every row (the factors of $\tau$ restored)
> **Meaning:** the third component of the angular velocity never vanishes and keeps the sign it had at the start (positive), so the polhode is a closed curve around plus $\mathbf k_b$, the major axis of inertia (shortest semi-axis of the ellipsoid), whose projection on the plane of $\mathbf i_b$ and $\mathbf j_b$ is the ellipse of the boxed equation. The initial angular velocity sits on it at the end of the $\mathbf j_b$ semi-axis of that ellipse, where the third component takes its smallest value, 1 over $\tau$. The motion is not a rotation about the intermediate axis: the second row minus 4 times the first is 32, positive, which is the sign of a polhode about the major axis (zero would be the separatrix through the intermediate axis). The polhode does not pass through any principal axis, where the right-hand sides of Euler's equations would all vanish, so the tip of the angular velocity never stops on it and travels round it periodically, in the sense from plus $\mathbf j_b$ towards minus $\mathbf i_b$ found in Euler's equations at the start.

> [!derivation] Part (f): the herpolhode lies in an annulus of the plane
> **Law:** right triangle formed by $G$, the foot of the perpendicular from $G$ to the plane, and $P$
> **Source:** Notes.pdf, Sec. 15.4; Notes.pdf, Eq. 15.31
>
> Let $N$ be the foot of the perpendicular from $G$ to the invariant plane. In the right triangle $GNP$ the hypotenuse is the distance from $G$ to $P$, one leg is $\delta$ (along $\mathbf u_H$) and the other leg, $\rho$, lies in the plane. The magnitude of the angular velocity is written with the rows of the polhode box.
>
> $$\begin{aligned}
> \rho^2 &= \left|\mathbf r_b^P\right|^2 - \delta^2 = \tau^2\ell^2\left(\omega_{xb}^2 + \omega_{yb}^2 + \omega_{zb}^2\right) - \frac92\,\ell^2 \quad &\text{(Pythagoras in the triangle $GNP$)} \\
> \tau^2\left(\omega_{xb}^2 + \omega_{yb}^2 + \omega_{zb}^2\right) &= \left(8\tau^2\omega_{zb}^2 - 8\right) + \left(10 - 6\tau^2\omega_{zb}^2\right) + \tau^2\omega_{zb}^2 = 3\tau^2\omega_{zb}^2 + 2 \quad &\text{(polhode rows)} \\
> \rho^2 &= \left(3\tau^2\omega_{zb}^2 + 2 - \frac92\right)\ell^2, \qquad 1 \le \tau^2\omega_{zb}^2 \le \frac53 \quad &\text{(substitution; range of the polhode box)} \\
> \rho_{\min}^2 &= \left(3 + 2 - \frac92\right)\ell^2 = \frac12\,\ell^2, \qquad \rho_{\max}^2 = \left(5 + 2 - \frac92\right)\ell^2 = \frac52\,\ell^2 \quad &\text{(both ends of the range)}
> \end{aligned}$$
>
> $$\boxed{\frac{\ell}{\sqrt2} \approx 0.707\,\ell \le \rho \le \sqrt{\frac52}\,\ell \approx 1.581\,\ell, \qquad \rho(0) = \frac{\ell}{\sqrt2}}$$
>
> **Units:** $[\mathrm L^2]$ in every row of $\rho^2$
> **Meaning:** the contact point moves on the plane between two circles centred at $N$, of radii 0.707 and 1.581 times $\ell$. It starts on the inner circle (the third component of the angular velocity is then smallest) and touches the outer one when the second component vanishes. Whether the herpolhode closes depends on the ratio of the period of the polhode to the turn of the contact point about $N$; in general it does not (**extension**, not shown here).

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Body basis in $\mathcal B_0$ | $\mathbf i_b = c_\theta c_\phi\,\mathbf i_0 + (c_\psi s_\phi + s_\psi s_\theta c_\phi)\mathbf j_0 + (s_\psi s_\phi - c_\psi s_\theta c_\phi)\mathbf k_0$; $\mathbf j_b = -c_\theta s_\phi\,\mathbf i_0 + (c_\psi c_\phi - s_\psi s_\theta s_\phi)\mathbf j_0 + (s_\psi c_\phi + c_\psi s_\theta s_\phi)\mathbf k_0$; $\mathbf k_b = s_\theta\,\mathbf i_0 - s_\psi c_\theta\,\mathbf j_0 + c_\psi c_\theta\,\mathbf k_0$; initially $\mathbf i_b = \tfrac12\mathbf j_0 + \tfrac{\sqrt3}2\mathbf k_0$, $\mathbf j_b = -\mathbf i_0$, $\mathbf k_b = -\tfrac{\sqrt3}2\mathbf j_0 + \tfrac12\mathbf k_0$ |
| (b) Angular velocity in $\mathcal B_b$ | $\omega_{xb} = \dot\psi c_\theta c_\phi + \dot\theta s_\phi$, $\omega_{yb} = -\dot\psi c_\theta s_\phi + \dot\theta c_\phi$, $\omega_{zb} = \dot\psi s_\theta + \dot\phi$; initially $(0, 2, 1)/\tau$ |
| (c) Kinetic energy and ellipsoid | $T_0^b = m\ell^2(\omega_{xb}^2 + 2\omega_{yb}^2 + 4\omega_{zb}^2) = 12\,m\ell^2/\tau^2$ (constant); $x_b^2/12 + y_b^2/6 + z_b^2/3 = \ell^2$, semi-axes $2\sqrt3\,\ell$, $\sqrt6\,\ell$, $\sqrt3\,\ell$ along $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$ |
| (d) Angular momentum and invariant plane | $\mathbf H_{G0}^b = m\ell^2(2\omega_{xb}\mathbf i_b + 4\omega_{yb}\mathbf j_b + 8\omega_{zb}\mathbf k_b) = (m\ell^2/\tau)(-8\mathbf i_0 - 4\sqrt3\mathbf j_0 + 4\mathbf k_0)$, magnitude $8\sqrt2\,m\ell^2/\tau$; component of $\boldsymbol\omega_{b0}$ along it, twice the kinetic energy over the magnitude of the angular momentum, $3\sqrt2/(2\tau)$; plane normal to $\mathbf H_{G0}^b$ at the distance $\delta = 3\sqrt2\,\ell/2 \approx 2.121\,\ell$ from $G$ |
| (e) Tangency | $\nabla F$ at $P$ is $(\tau/m\ell)\,\mathbf H_{G0}^b$, the normal of the plane; the ellipsoid lies on the side of $G$ |
| (f) Motion | The ellipsoid rolls without slipping on the invariant plane with $G$ fixed; polhode $3\omega_{xb}^2 + 4\omega_{yb}^2 = 16/\tau^2$ around $+\mathbf k_b$ (major axis of inertia, not the intermediate one), with $\tau\omega_{zb}$ between 1 and 1.291; initial $\boldsymbol\omega_{b0}$ 26.6 degrees from $\mathbf j_b$, on the polhode, at its point on the $\mathbf j_b$ side; herpolhode between the circles of radii $0.707\,\ell$ and $1.581\,\ell$ about the foot $N$ of the perpendicular from $G$ |

**Check against the official key:** the key (Problems.pdf, p. 81) prints only, for part (e), that the ellipsoid and the plane are tangent if their normals at $P$ coincide. Part (e) shows exactly that: the gradient of the ellipsoid at $P$ is a positive multiple of the angular momentum, which is the normal of the invariant plane. Match. The key gives no numbers for the other parts.

* **Order of the distances.** The distance of the plane lies between the shortest and the intermediate semi-axes, so the contact point stays on the side of the shortest semi-axis: its direction keeps between about 61 and 63 degrees of $\mathbf k_b$ and encircles that axis, which agrees with the polhode about $\mathbf k_b$.
* **Separatrix.** If the square of the magnitude of the angular momentum equalled 4 times twice the energy (in the units of the polhode box, 96 instead of 128), the polhode would pass through the intermediate axis; this motion is away from that case by 32.
* **Dimensions.** The semi-axes and the distance of the plane are lengths; the component of the angular velocity along the angular momentum is a rate.

---

## Problem RB-32: Rate gyro on aircraft

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** three rigid bodies. The aircraft $a$, whose motion is prescribed; the gimbal $b$, of negligible mass and moments of inertia, turning about an axis fixed in the aircraft; the disk $d$, of centre of mass $G$, spinning about an axle fixed in the gimbal, with principal moments $2I$ about the axle and $I$ about any perpendicular axis through $G$. A torsional spring (constant $k$) and a torsional damper (constant $\lambda$) act between the aircraft and the gimbal about the gimbal axis.
* **Inertial frame:** $S_0$, arbitrary, not shown in the figure.
* **Aircraft frame:** $S_a\{G; \mathcal B_a\}$, with $\mathcal B_a$ made of $\mathbf i_a$, $\mathbf j_a$, $\mathbf k_a$ as in the figure ($\mathbf k_a$ is the yaw axis). Its angular velocity relative to $S_0$ is the known yaw rate $\Omega$ along $\mathbf k_a$. Its origin is placed at $G$, which lies on the gimbal axis and on the spin axle, so $G$ is a point fixed in the aircraft.
* **Gimbal frame:** $S_b\{G; \mathcal B_b\}$, simple rotation $\theta$ about the gimbal axis.
* **Disk frame:** $S_d\{G; \mathcal B_d\}$, simple rotation $\phi$ about the spin axle.
* **Reading of the figure (axes):** the gimbal axis is the horizontal bar that carries the spring and the damper, drawn parallel to $\mathbf i_a$, so the first rotation is about $\mathbf i_a$, which equals $\mathbf i_b$. The angle $\theta$ is drawn at the bearing between a dashed line parallel to $\mathbf j_a$ and $\mathbf j_b$. The middle bar of the gimbal frame, parallel to $\mathbf j_b$, passes through $G$ and is drawn dashed behind the disk: it is read as the spin axle, so the spin axis is $\mathbf j_b$, which equals $\mathbf j_d$, and $\phi$ is the angle drawn in the plane of the disk between the dashed gimbal axis through $G$ (along $\mathbf i_b$) and $\mathbf i_d$. With the other possible reading (disk lying in the plane of the gimbal frame, spin about $\mathbf k_b$) the gyroscopic term of the gimbal equation would carry the sine of $\theta$ instead of its cosine, so it would vanish at small $\theta$ and the device would not measure the yaw rate; the reading used here is the one that makes it a rate gyroscope.
* **Reading of the figure (senses):** $\mathbf j_b$ is drawn above the dashed line, towards $\mathbf k_a$, which is the positive sense of a rotation about $\mathbf i_a$ by the right-hand rule. The figure marks the angle $\phi$ but no sense of turning (its drawing suggests the opposite sense); it is taken positive by the right-hand rule about $\mathbf j_b$. The opposite sense would replace $\phi$ by minus $\phi$ in every formula below.
* **Coordinates and degrees of freedom:** the motion of the aircraft is known (yaw rate $\Omega$, and a translation that does not enter the moment equations about $G$). The gimbal turns only about its axis (one coordinate, $\theta$) and the disk only about its axle relative to the gimbal (one coordinate, $\phi$): two degrees of freedom, $\theta$ and $\phi$.

| Datum | Symbol | SI unit |
| :--- | :--- | :--- |
| Principal moments of the disk at $G$ | $2I$ about the spin axle, $I$ about perpendicular axes | kg m$^2$ |
| Mass and moments of the gimbal | negligible | |
| Spring constant (torque per angle) | $k$ | N m/rad |
| Damper constant (torque per angular rate) | $\lambda$ | N m s/rad |
| Yaw rate of the aircraft, known | $\Omega(t)$, along $\mathbf k_a$ | rad/s |
| Coordinates | $\theta$ (gimbal), $\phi$ (spin) | rad |

### Change of Basis, Position Vectors and Constraint Kinematics

![[attachments/EM-SOL/rb32-rot-theta.svg]]

> [!derivation] Part (a): gimbal basis, rotation by theta about ia
> **Law:** simple rotation about the first axis; right-hand rule
> **Source:** Notes.pdf, Eq. 9.17; Notes.pdf, Sec. 9.2; [Lecture 7, Slide 12]
>
> View along the gimbal axis with $\mathbf i_a$ out of the paper (⊙), $\mathbf j_a$ to the right and $\mathbf k_a$ up; this is right-handed because the product of $\mathbf j_a$ and $\mathbf k_a$ is $\mathbf i_a$. A positive $\theta$ turns counterclockwise. Triangle of $\mathbf j_b$: hypotenuse 1, adjacent leg along $\mathbf j_a$ (cosine of $\theta$), opposite leg along $\mathbf k_a$ (sine). Triangle of $\mathbf k_b$: adjacent leg along $\mathbf k_a$ (cosine), opposite leg along minus $\mathbf j_a$ (sine), because the counterclockwise turn carries the tip of $\mathbf k_a$, which points up, to the left.
>
> $$\begin{aligned}
> \mathbf i_b &= \mathbf i_a, \qquad \mathbf j_b = \cos\theta\,\mathbf j_a + \sin\theta\,\mathbf k_a, \qquad \mathbf k_b = -\sin\theta\,\mathbf j_a + \cos\theta\,\mathbf k_a \quad &\text{(legs of the two triangles)} \\
> [{}_aR_b] &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos\theta & -\sin\theta \cr 0 & \sin\theta & \cos\theta \end{bmatrix} \quad &\text{(columns: $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$ in $\mathcal B_a$)} \\
> \det[{}_aR_b] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) = 1 \quad &\text{(expand along the first row)} \\
> [{}_aR_b][{}_aR_b]^T &= \begin{bmatrix} 1 & 0 & 0 \cr 0 & \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \cr 0 & \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> \mathbf j_a &= \cos\theta\,\mathbf j_b - \sin\theta\,\mathbf k_b, \qquad \mathbf k_a = \sin\theta\,\mathbf j_b + \cos\theta\,\mathbf k_b \quad &\text{(rows: the inverse is the transpose)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_b = \mathbf i_a, \qquad \mathbf j_b = \cos\theta\,\mathbf j_a + \sin\theta\,\mathbf k_a, \qquad \mathbf k_b = -\sin\theta\,\mathbf j_a + \cos\theta\,\mathbf k_a, \qquad \mathbf k_a = \sin\theta\,\mathbf j_b + \cos\theta\,\mathbf k_b}$$
>
> **Units:** dimensionless
> **Meaning:** at zero $\theta$ the spin axle $\mathbf j_b$ is along $\mathbf j_a$, normal to the yaw axis; a positive $\theta$ lifts it towards $\mathbf k_a$. The last relation writes the yaw axis in the gimbal basis for part (b).

![[attachments/EM-SOL/rb32-rot-phi.svg]]

> [!derivation] Part (a): disk basis, rotation by phi about jb
> **Law:** simple rotation about the second axis; right-hand rule; product of rotation matrices
> **Source:** Notes.pdf, Sec. 9.2; Notes.pdf, Eq. 9.19; [Lecture 7, Slide 12]
>
> View along the spin axle with $\mathbf j_b$ out of the paper (⊙), $\mathbf k_b$ to the right and $\mathbf i_b$ up; this is right-handed because the product of $\mathbf k_b$ and $\mathbf i_b$ is $\mathbf j_b$. A positive $\phi$ turns counterclockwise. Triangle of $\mathbf k_d$: adjacent leg along $\mathbf k_b$ (cosine of $\phi$), opposite leg along $\mathbf i_b$ (sine), because the counterclockwise turn carries the tip of $\mathbf k_b$, which points right, upwards. Triangle of $\mathbf i_d$: adjacent leg along $\mathbf i_b$ (cosine), opposite leg along minus $\mathbf k_b$ (sine), because the same turn carries the tip of $\mathbf i_b$, which points up, to the left.
>
> $$\begin{aligned}
> \mathbf i_d &= \cos\phi\,\mathbf i_b - \sin\phi\,\mathbf k_b, \qquad \mathbf j_d = \mathbf j_b, \qquad \mathbf k_d = \sin\phi\,\mathbf i_b + \cos\phi\,\mathbf k_b \quad &\text{(legs of the two triangles)} \\
> [{}_bR_d] &= \begin{bmatrix} \cos\phi & 0 & \sin\phi \cr 0 & 1 & 0 \cr -\sin\phi & 0 & \cos\phi \end{bmatrix}, \qquad \det[{}_bR_d] = 1\cdot\left(\cos^2\phi + \sin^2\phi\right) = 1 \quad &\text{(columns in $\mathcal B_b$; expand along the second row)} \\
> [{}_bR_d][{}_bR_d]^T &= \begin{bmatrix} \cos^2\phi + \sin^2\phi & 0 & -\cos\phi\sin\phi + \sin\phi\cos\phi \cr 0 & 1 & 0 \cr -\sin\phi\cos\phi + \cos\phi\sin\phi & 0 & \sin^2\phi + \cos^2\phi \end{bmatrix} = [U] \quad &\text{(row by row products)} \\
> [{}_aR_d] &= [{}_aR_b][{}_bR_d] = \begin{bmatrix} \cos\phi & 0 & \sin\phi \cr \sin\theta\sin\phi & \cos\theta & -\sin\theta\cos\phi \cr -\cos\theta\sin\phi & \sin\theta & \cos\theta\cos\phi \end{bmatrix} \quad &\text{(row of the first times column of the second)} \\
> \det[{}_aR_d] &= 1\cdot 1 = 1, \qquad [{}_aR_d][{}_aR_d]^T = [{}_aR_b][{}_bR_d][{}_bR_d]^T[{}_aR_b]^T = [U] \quad &\text{(product of the two checked factors)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \mathbf i_d = \cos\phi\,\mathbf i_a + \sin\theta\sin\phi\,\mathbf j_a - \cos\theta\sin\phi\,\mathbf k_a, \qquad \mathbf j_d = \cos\theta\,\mathbf j_a + \sin\theta\,\mathbf k_a \\ \mathbf k_d = \sin\phi\,\mathbf i_a - \sin\theta\cos\phi\,\mathbf j_a + \cos\theta\cos\phi\,\mathbf k_a \end{gathered}}$$
>
> **Units:** dimensionless
> **Meaning:** the columns of $[{}_aR_d]$ are the disk vectors in $\mathcal B_a$; the second column is the axle, the same as $\mathbf j_b$, because the spin does not move it.

> [!derivation] Part (b): angular velocities of the gimbal and of the disk
> **Law:** composition of angular velocities, each rate along its own axis
> **Source:** Notes.pdf, Eq. 9.21; Notes.pdf, Eq. 3.14
>
> The aircraft turns about $\mathbf k_a$ at the rate $\Omega$, the gimbal turns relative to it about $\mathbf i_b$ at the rate of $\theta$, the disk relative to the gimbal about $\mathbf j_b$ at the rate of $\phi$. The yaw axis is written in $\mathcal B_b$ with the last relation of the first box.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0} &= \boldsymbol\omega_{ba} + \boldsymbol\omega_{a0} = \dot\theta\,\mathbf i_b + \Omega\,\mathbf k_a \quad &\text{(composition, Eq. 9.21)} \\
> &= \dot\theta\,\mathbf i_b + \Omega\left(\sin\theta\,\mathbf j_b + \cos\theta\,\mathbf k_b\right) \quad &\text{($\mathbf k_a$ in $\mathcal B_b$)} \\
> \boldsymbol\omega_{d0} &= \boldsymbol\omega_{db} + \boldsymbol\omega_{b0} = \dot\phi\,\mathbf j_b + \dot\theta\,\mathbf i_b + \Omega\sin\theta\,\mathbf j_b + \Omega\cos\theta\,\mathbf k_b \quad &\text{(composition, Eq. 9.21)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = \dot\theta\,\mathbf i_b + \Omega\sin\theta\,\mathbf j_b + \Omega\cos\theta\,\mathbf k_b, \qquad \boldsymbol\omega_{d0} = \dot\theta\,\mathbf i_b + \left(\Omega\sin\theta + \dot\phi\right)\mathbf j_b + \Omega\cos\theta\,\mathbf k_b}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ in every component
> **Meaning:** the gimbal and the disk differ only by the spin about the axle. The disk vectors are not used for the components: the disk is symmetric about its axle, so its tensor is constant in $\mathcal B_b$ (inertia section), and $\mathcal B_b$ is the convenient basis.

> [!derivation] Part (b): angular accelerations of the gimbal and of the disk
> **Law:** derivative in $S_0$ of a vector known in $\mathcal B_b$ (Coriolis theorem); product rule and chain rule; vector product by its determinant
> **Source:** Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.9; Notes.pdf, Eq. 9.21
>
> The frame $S_b$ turns with $\boldsymbol\omega_{b0}$. Each component of the previous box is differentiated with the product rule and the chain rule; for instance the derivative of $\Omega\sin\theta$ is the rate of $\Omega$ times the sine of $\theta$ plus $\Omega$ times the derivative of the sine, which is its cosine times the rate of $\theta$.
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\Omega\sin\theta\right) &= \dot\Omega\sin\theta + \Omega\,\frac{d\sin\theta}{d\theta}\,\frac{d\theta}{dt} = \dot\Omega\sin\theta + \Omega\dot\theta\cos\theta \quad &\text{(product rule; chain rule)} \\
> \frac{d}{dt}\left(\Omega\cos\theta\right) &= \dot\Omega\cos\theta + \Omega\,\frac{d\cos\theta}{d\theta}\,\frac{d\theta}{dt} = \dot\Omega\cos\theta - \Omega\dot\theta\sin\theta \quad &\text{(product rule; chain rule)} \\
> \boldsymbol\alpha_{b0} &= \left.\frac{d\boldsymbol\omega_{b0}}{dt}\right|_b + \boldsymbol\omega_{b0}\times\boldsymbol\omega_{b0} = \ddot\theta\,\mathbf i_b + \left(\dot\Omega\sin\theta + \Omega\dot\theta\cos\theta\right)\mathbf j_b + \left(\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta\right)\mathbf k_b \quad &\text{(Eq. 3.8; a vector times itself is zero)} \\
> \boldsymbol\omega_{b0}\times\dot\phi\,\mathbf j_b &= \dot\phi\begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta & \Omega\sin\theta & \Omega\cos\theta \cr 0 & 1 & 0 \end{vmatrix} = \dot\phi\left[\left(0 - \Omega\cos\theta\right)\mathbf i_b - \left(0 - 0\right)\mathbf j_b + \left(\dot\theta - 0\right)\mathbf k_b\right] \quad &\text{(expand along the first row)} \\
> \boldsymbol\alpha_{d0} &= \left.\frac{d\boldsymbol\omega_{d0}}{dt}\right|_b + \boldsymbol\omega_{b0}\times\boldsymbol\omega_{d0} = \boldsymbol\alpha_{b0} + \ddot\phi\,\mathbf j_b + \boldsymbol\omega_{b0}\times\dot\phi\,\mathbf j_b \quad &\text{(Eq. 3.8 with $S_b$; the disk vector is the gimbal one plus the spin)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} \boldsymbol\alpha_{b0} = \ddot\theta\,\mathbf i_b + \left(\dot\Omega\sin\theta + \Omega\dot\theta\cos\theta\right)\mathbf j_b + \left(\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta\right)\mathbf k_b \\ \boldsymbol\alpha_{d0} = \left(\ddot\theta - \Omega\dot\phi\cos\theta\right)\mathbf i_b + \left(\dot\Omega\sin\theta + \Omega\dot\theta\cos\theta + \ddot\phi\right)\mathbf j_b + \left(\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta + \dot\phi\dot\theta\right)\mathbf k_b \end{gathered}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ in every term
> **Meaning:** the gimbal acceleration is the derivative of its components alone, because $\mathcal B_b$ turns with the gimbal itself. The disk gains two transport terms from the spin: the axle is carried round by the gimbal, which turns the spin vector.

### Center of Mass and Inertia Tensor

> [!derivation] Inertia tensor of the disk in the gimbal basis
> **Law:** change of basis of a tensor; moments of a thin disk as surface integrals (jacobian $\rho$)
> **Source:** Notes.pdf, Eq. 10.11; Notes.pdf, Eq. 10.15; Notes.pdf, Eq. 10.35; [Lecture 8, Slide 16]
>
> The statement gives the principal moments at $G$ in $\mathcal B_d$: $2I$ along $\mathbf j_d$, $I$ along $\mathbf i_d$ and $\mathbf k_d$. The integrals of the last rows only check the ratio 2 for a thin homogeneous disk, of surface density $\sigma$ and radius $a$ (neither is given; both cancel in the ratio), with polar coordinates $(\rho, \chi)$ in its plane, $\chi$ measured from $\mathbf i_d$; the squared distance to the axle is the square of $\rho$, to the diameter along $\mathbf i_d$ the square of $\rho\sin\chi$.
>
> $$\begin{aligned}
> [{}_bR_d]\,\mathrm{diag}\left(I, 2I, I\right)[{}_bR_d]^T &= \begin{bmatrix} I\cos^2\phi + I\sin^2\phi & 0 & -I\cos\phi\sin\phi + I\sin\phi\cos\phi \cr 0 & 2I & 0 \cr -I\sin\phi\cos\phi + I\cos\phi\sin\phi & 0 & I\sin^2\phi + I\cos^2\phi \end{bmatrix} \quad &\text{(row by column products)} \\
> &= \mathrm{diag}\left(I, 2I, I\right) \quad &\text{(equal transverse moments)} \\
> I_{\mathrm{axle}} &= \sigma\int_0^{2\pi}\!\!\int_0^{a}\rho^2\,\rho\,d\rho\,d\chi = \sigma\left[\chi\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^{a} = \frac{\pi\sigma a^4}{2} \quad &\text{(antiderivatives; Barrow's rule)} \\
> I_{\mathrm{diam}} &= \sigma\int_0^{2\pi}\sin^2\chi\,d\chi\int_0^{a}\rho^3\,d\rho = \sigma\left[\frac{\chi}{2} - \frac{\sin 2\chi}{4}\right]_0^{2\pi}\left[\frac{\rho^4}{4}\right]_0^{a} = \sigma\,\pi\,\frac{a^4}{4} \quad &\text{(antiderivatives; Barrow's rule)} \\
> \frac{I_{\mathrm{axle}}}{I_{\mathrm{diam}}} &= \frac{\pi\sigma a^4/2}{\pi\sigma a^4/4} = 2 \quad &\text{(ratio)}
> \end{aligned}$$
>
> $$\boxed{\bar{\bar I}{}^{\,d}_G = \begin{bmatrix} I & 0 & 0 \cr 0 & 2I & 0 \cr 0 & 0 & I \end{bmatrix} \ \text{in } \mathcal B_b \text{ and in } \mathcal B_d}$$
>
> **Units:** $[\mathrm M][\mathrm L^2]$
> **Meaning:** the tensor does not depend on $\phi$, so it is constant in the gimbal basis, which does not spin with the disk; the ratio 2 of the statement is that of a thin disk. $G$ is the centre of mass of the disk and the gimbal carries no mass, so the moment equations below are written at $G$.

### Linear Momentum, Angular Momentum and Kinetic Energy

> [!derivation] Angular momentum of the disk and of the gimbal about G
> **Law:** angular momentum of a rigid body about its centre of mass; a body with negligible mass and inertia
> **Source:** Notes.pdf, Eq. 11.12; Notes.pdf, Eq. 11.21
>
> $$\begin{aligned}
> \mathbf H_G^d &= \bar{\bar I}{}^{\,d}_G\cdot\boldsymbol\omega_{d0} = I\dot\theta\,\mathbf i_b + 2I\left(\Omega\sin\theta + \dot\phi\right)\mathbf j_b + I\Omega\cos\theta\,\mathbf k_b \quad &\text{(Eq. 11.21; tensor in $\mathcal B_b$, part (b))} \\
> \mathbf H_G^b &= \mathbf 0, \qquad \mathbf p^b = \mathbf 0 \quad &\text{(negligible mass and moments of the gimbal)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_G^d = I\dot\theta\,\mathbf i_b + 2I\left(\Omega\sin\theta + \dot\phi\right)\mathbf j_b + I\Omega\cos\theta\,\mathbf k_b, \qquad \mathbf H_G^b = \mathbf 0}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-1}}]$
> **Meaning:** the axial part, twice $I$ times the spin measured in $S_0$, dominates when the disk spins fast; the transverse part comes from the nutation rate and from the yaw rate projected on $\mathbf k_b$. The kinetic energy is not needed: the problem is solved with the moment equations.

### Free-Body Diagram and Equations of Motion

![[attachments/EM-SOL/rb32-exploded.svg]]

#### Part (c): loads on each body

The exploded view separates the disk, the gimbal and the aircraft. The spin axle joins the disk to the gimbal along $\mathbf j_b$ through $G$; the gimbal bearings join the gimbal to the aircraft along $\mathbf i_b$ through $G$; the spring and the damper act between the aircraft and the gimbal about the same axis. Both bearings are ideal (no friction torque about their own axis) and there is no motor on the spin axle. Every reaction is reduced at $G$ to a force and a moment. Write $\mathbf F_{bd}$ and $\mathbf M_{bd}$ for the force and moment of the gimbal on the disk, $\mathbf F_{ab}$ and $\mathbf M_{ab}$ for those of the aircraft on the gimbal at its bearings, and $m_d$ for the mass of the disk (not given; it enters only the force equations).

| Load | Body | Point | Expression | Kind |
| :--- | :--- | :--- | :--- | :--- |
| Weight of the disk | $d$ | $G$ | $m_d\,\mathbf g$ | applied |
| Gimbal on the disk (spin axle) | $d$ | $G$ | $\mathbf F_{bd}$, three components; $\mathbf M_{bd} = M_1\,\mathbf i_b + M_3\,\mathbf k_b$, none along $\mathbf j_b$ | constraint (pair) |
| Disk on the gimbal (spin axle) | $b$ | $G$ | $-\mathbf F_{bd}$ and $-\mathbf M_{bd}$ | constraint (pair) |
| Aircraft on the gimbal (bearings) | $b$ | $G$ | $\mathbf F_{ab}$, three components; $\mathbf M_{ab} = N_2\,\mathbf j_b + N_3\,\mathbf k_b$, none along $\mathbf i_b$ | constraint (pair) |
| Spring on the gimbal | $b$ | axis | $-k\theta\,\mathbf i_b$ | applied (pair) |
| Damper on the gimbal | $b$ | axis | $-\lambda\dot\theta\,\mathbf i_b$ | applied (pair) |
| Gimbal on the aircraft | $a$ | $G$ and axis | $-\mathbf F_{ab}$, $-\mathbf M_{ab}$, $+k\theta\,\mathbf i_b$, $+\lambda\dot\theta\,\mathbf i_b$ | pairs |
| Loads that drive the aircraft | $a$ | | whatever produces the prescribed motion | not needed |

> [!derivation] Part (c): why each bearing moment has no component along its own axis
> **Law:** moment of a force about a point; vector product by its determinant; ideal bearing
> **Source:** Notes.pdf, Eq. 12.14; Notes.pdf, Sec. 13.2
>
> Take a bearing force $\mathbf F$ with components $F_1$, $F_2$, $F_3$ in $\mathcal B_b$, applied at a point of the spin axle at the distance $s$ from $G$, that is at $s\,\mathbf j_b$; an ideal bearing transmits only such forces (no friction torque about the axle).
>
> $$\begin{aligned}
> s\,\mathbf j_b\times\mathbf F &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr 0 & s & 0 \cr F_1 & F_2 & F_3 \end{vmatrix} = s F_3\,\mathbf i_b - \left(0 - 0\right)\mathbf j_b - s F_1\,\mathbf k_b \quad &\text{(expand along the first row)} \\
> \left(s\,\mathbf j_b\times\mathbf F\right)\cdot\mathbf j_b &= 0 \quad &\text{(second component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_{bd}\cdot\mathbf j_b = 0, \qquad \mathbf M_{ab}\cdot\mathbf i_b = 0 \ \ \text{(the same argument with the points on the gimbal axis, at } s\,\mathbf i_b\text{)}}$$
>
> **Units:** N m
> **Meaning:** summed over all the points of a bearing, the moment about $G$ of its forces is normal to the bearing axis. The only torques about the gimbal axis are the spring and the damper; about the spin axle there is none.

> [!derivation] Part (c): equations of the massless gimbal and the torque on the disk
> **Law:** force and moment equations of a body with zero momentum and zero angular momentum
> **Source:** Notes.pdf, Eq. 12.8; Notes.pdf, Eq. 12.13
>
> The gimbal has zero linear momentum and zero angular momentum about $G$ at every instant, so their derivatives vanish, and so does the pole term at $G$. The resultant moment about $G$ on the gimbal is the sum of the moments of the table, projected on $\mathcal B_b$.
>
> $$\begin{aligned}
> \mathbf 0 &= -\mathbf F_{bd} + \mathbf F_{ab} \quad &\text{(Eq. 12.8 with zero momentum)} \\
> \mathbf 0 &= -\left(M_1\,\mathbf i_b + M_3\,\mathbf k_b\right) + N_2\,\mathbf j_b + N_3\,\mathbf k_b - k\theta\,\mathbf i_b - \lambda\dot\theta\,\mathbf i_b \quad &\text{(Eq. 12.13 at $G$ with zero angular momentum)} \\
> 0 &= -M_1 - k\theta - \lambda\dot\theta, \qquad 0 = N_2, \qquad 0 = -M_3 + N_3 \quad &\text{(components along $\mathbf i_b$, $\mathbf j_b$, $\mathbf k_b$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_{bd} = -\left(k\theta + \lambda\dot\theta\right)\mathbf i_b + M_3\,\mathbf k_b, \qquad \mathbf M_{ab} = M_3\,\mathbf k_b, \qquad \mathbf F_{ab} = \mathbf F_{bd}}$$
>
> **Units:** N m; N
> **Meaning:** the massless gimbal passes the spring and damper torque straight to the disk; the moment along $\mathbf k_b$ is a bearing reaction $M_3$, found in part (d). The total torque about $G$ on the disk is $\mathbf M_{bd}$, since its weight acts at $G$.

#### Part (d): equations of motion

> [!derivation] Part (d): moment equation of the disk about G
> **Law:** moment equation about the centre of mass; derivative in $S_0$ of a vector known in $\mathcal B_b$ (gyroscopic term)
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 12.20; Notes.pdf, Eq. 3.8
>
> The pole is $G$, the centre of mass of the disk: the pole term, the velocity of $G$ times the momentum of the disk (its mass times the same velocity), is zero even though $G$ is carried by the aircraft. Write $n$ for the spin of the disk measured in $S_0$, the second component of its angular velocity, $\Omega\sin\theta$ plus the rate of $\phi$.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0 &= \left.\frac{d\mathbf H_G^d}{dt}\right|_b + \boldsymbol\omega_{b0}\times\mathbf H_G^d \quad &\text{(Eq. 3.8 with the frame $S_b$)} \\
> \left.\frac{d\mathbf H_G^d}{dt}\right|_b &= I\ddot\theta\,\mathbf i_b + 2I\dot n\,\mathbf j_b + I\left(\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta\right)\mathbf k_b \quad &\text{(derivatives of the components; chain rule of part (b))} \\
> \boldsymbol\omega_{b0}\times\mathbf H_G^d &= \begin{vmatrix} \mathbf i_b & \mathbf j_b & \mathbf k_b \cr \dot\theta & \Omega\sin\theta & \Omega\cos\theta \cr I\dot\theta & 2In & I\Omega\cos\theta \end{vmatrix} \quad &\text{(vector product by its determinant)} \\
> &= \left(I\Omega^2\sin\theta\cos\theta - 2In\Omega\cos\theta\right)\mathbf i_b - \left(I\dot\theta\Omega\cos\theta - I\dot\theta\Omega\cos\theta\right)\mathbf j_b + \left(2In\dot\theta - I\Omega\dot\theta\sin\theta\right)\mathbf k_b \quad &\text{(expand along the first row)} \\
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0 &= \mathbf M_{bd} = -\left(k\theta + \lambda\dot\theta\right)\mathbf i_b + M_3\,\mathbf k_b \quad &\text{(Eq. 12.13 at $G$; previous box)} \\
> I\ddot\theta + I\Omega^2\sin\theta\cos\theta - 2In\Omega\cos\theta &= -k\theta - \lambda\dot\theta \quad &\text{(component along $\mathbf i_b$)} \\
> 2I\dot n + 0 &= 0 \quad &\text{(component along $\mathbf j_b$)} \\
> I\dot\Omega\cos\theta - I\Omega\dot\theta\sin\theta + 2In\dot\theta - I\Omega\dot\theta\sin\theta &= M_3 \quad &\text{(component along $\mathbf k_b$)} \\
> \dot n &= \dot\Omega\sin\theta + \Omega\dot\theta\cos\theta + \ddot\phi \quad &\text{(chain rule of part (b))} \\
> -2I\Omega\cos\theta\left(\Omega\sin\theta + \dot\phi\right) + I\Omega^2\sin\theta\cos\theta &= -I\Omega^2\sin\theta\cos\theta - 2I\Omega\dot\phi\cos\theta \quad &\text{($n$ substituted in the first equation)}
> \end{aligned}$$
>
> $$\boxed{\begin{gathered} I\ddot\theta + \lambda\dot\theta + k\theta - I\Omega^2\sin\theta\cos\theta - 2I\Omega\dot\phi\cos\theta = 0 \\ \ddot\phi + \dot\Omega\sin\theta + \Omega\dot\theta\cos\theta = 0 \\ M_3 = I\dot\Omega\cos\theta + 2I\dot\phi\dot\theta \end{gathered}}$$
>
> **Units:** N m in the first and third equations; $[\mathrm{T^{-2}}]$ in the second
> **Meaning:** three scalar equations for $\theta$, $\phi$ and the bearing moment $M_3$: the first two are the equations of motion, with only $\theta$, $\phi$, the known $\Omega$ and the data $I$, $k$, $\lambda$; the third gives the reaction (the $\mathbf k_b$ equation simplifies because the two terms in the sine of $\theta$ cancel against part of the $n$ term). The term in the product of $\Omega$, the spin rate and the cosine of $\theta$ is the gyroscopic torque that the turning aircraft imposes on the spinning disk about the gimbal axis. The force equation of the disk gives the axle force, which needs the translation of the aircraft and is not asked.

> [!derivation] Part (e): the axial component of the angular momentum is constant
> **Law:** derivative of the projection on a moving unit vector (product rule); moment equation at $G$; derivative of a unit vector of $\mathcal B_b$
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.3; Notes.pdf, Eq. 13.10
>
> The axle $\mathbf j_b$ turns with the gimbal, so its derivative in $S_0$ is the angular velocity of the gimbal times $\mathbf j_b$ (vector product computed in part (b), divided by the rate of $\phi$).
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\mathbf H_G^d\cdot\mathbf j_b\right) &= \left.\frac{d\mathbf H_G^d}{dt}\right|_0\cdot\mathbf j_b + \mathbf H_G^d\cdot\left.\frac{d\mathbf j_b}{dt}\right|_0 \quad &\text{(product rule)} \\
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0\cdot\mathbf j_b &= \mathbf M_{bd}\cdot\mathbf j_b = 0 \quad &\text{(first reason: no moment along the axle)} \\
> \mathbf H_G^d\cdot\left(\boldsymbol\omega_{b0}\times\mathbf j_b\right) &= \left(I\dot\theta, 2In, I\Omega\cos\theta\right)\cdot\left(-\Omega\cos\theta, 0, \dot\theta\right) = -I\dot\theta\,\Omega\cos\theta + I\Omega\cos\theta\,\dot\theta = 0 \quad &\text{(second reason: the gyroscopic term vanishes)} \\
> \left[\mathbf H_G^d\cdot\mathbf j_b\right]_0^t &= 0 \;\Rightarrow\; 2I\left(\Omega\sin\theta + \dot\phi\right) = 2I\left(\Omega\sin\theta + \dot\phi\right)\big|_{t = 0} \quad &\text{(integrate from 0 to $t$; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{H_s \equiv \mathbf H_G^d\cdot\mathbf j_b = 2I\left(\Omega\sin\theta + \dot\phi\right) = 2I\,n_0 \ \ (\text{constant}), \qquad n_0 = \left(\Omega\sin\theta + \dot\phi\right)\big|_{t = 0}}$$
>
> **Units:** $[\mathrm M][\mathrm L^2][\mathrm{T^{-1}}]$
> **Meaning:** the spin angular momentum is a constant of motion although the axle turns, for two reasons: the moment about the axle is zero (ideal bearing, weight through $G$), and the gyroscopic part vanishes because the two transverse moments of the disk are equal, so the transverse angular momentum stays in the plane of the transverse angular velocity. This is the second equation of part (d) integrated once. With it the equation of $\theta$ can also be written with the constant $n_0$ in place of the rate of $\phi$: the rate of $\phi$ is $n_0$ minus $\Omega$ times the sine of $\theta$.

> [!derivation] Part (e): the equation of theta with the spin integral
> **Law:** elimination of the rate of $\phi$ with the first integral
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 13.10
>
> $$\begin{aligned}
> -I\Omega^2\sin\theta\cos\theta - 2I\Omega\cos\theta\left(n_0 - \Omega\sin\theta\right) &= I\Omega^2\sin\theta\cos\theta - 2In_0\Omega\cos\theta \quad &\text{(rate of $\phi$ replaced; terms collected)}
> \end{aligned}$$
>
> $$\boxed{I\ddot\theta + \lambda\dot\theta + k\theta + I\Omega^2\sin\theta\cos\theta = 2In_0\,\Omega\cos\theta}$$
>
> **Units:** N m in every term
> **Meaning:** one equation for $\theta$ alone, forced by the yaw rate through the constant spin angular momentum $2In_0$.

#### Parts (f) and (g): linearized equation, steady reading and critical damping

> [!derivation] Part (f): linearization for small theta and slow yaw
> **Law:** first-order Taylor expansion; comparison of the orders of the terms
> **Source:** Notes.pdf, Sec. 14.4; Notes.pdf, Eq. 13.10
>
> With $\theta$ small, the sine of $\theta$ is $\theta$ and its cosine is 1 to first order. With $\Omega$ small compared with the spin, $n_0$ and the rate of $\phi$ differ by $\Omega$ times the sine of $\theta$, a small fraction of either. The term in the square of $\Omega$ is compared with the forcing term.
>
> $$\begin{aligned}
> \sin\theta &= \theta + O(\theta^3), \qquad \cos\theta = 1 + O(\theta^2) \quad &\text{(Taylor series at zero)} \\
> \frac{I\Omega^2\sin\theta\cos\theta}{2In_0\Omega\cos\theta} &= \frac{\Omega\sin\theta}{2n_0} \approx \frac{\Omega\,\theta}{2\dot\phi} \ll 1 \quad &\text{(ratio of the two terms: product of two small numbers)} \\
> n_0 &= \dot\phi + \Omega\sin\theta \approx \dot\phi \quad &\text{(spin integral; the correction is of the order of $\Omega\theta$)} \\
> I\ddot\theta + \lambda\dot\theta + k\theta &= 2In_0\,\Omega(t) \quad &\text{(previous box, linearized)}
> \end{aligned}$$
>
> $$\boxed{I\ddot\theta + \lambda\dot\theta + k\theta = 2I\dot\phi\,\Omega(t), \qquad \dot\phi \approx n_0 \ \text{constant}}$$
>
> **Units:** N m in every term
> **Meaning:** a damped linear oscillator about the gimbal axis, forced by the yaw rate times the spin angular momentum. The dropped term is also small compared with the spring term when $\theta$ follows the forcing (next box: there the spring term equals the forcing, so the same ratio applies).

> [!derivation] Part (f): steady deflection for a constant yaw rate
> **Law:** constant particular solution of a linear equation; decay of the homogeneous solution
> **Source:** Notes.pdf, Sec. 14.4
>
> With $\Omega$ constant, try a constant $\theta_s$: its first and second derivatives are zero. The homogeneous equation has solutions with the exponential of $st$, with $s$ a root of the characteristic polynomial; with $I$, $k$, $\lambda$ positive both roots have a negative real part (their sum is minus $\lambda$ over $I$, their product $k$ over $I$), so the homogeneous part dies out and $\theta$ tends to $\theta_s$.
>
> $$\begin{aligned}
> I\cdot 0 + \lambda\cdot 0 + k\,\theta_s &= 2I\dot\phi\,\Omega \quad &\text{(constant trial solution)} \\
> \theta_s &= \frac{2I\dot\phi\,\Omega}{k} \quad &\text{(division by $k$)} \\
> I s^2 + \lambda s + k &= 0 \;\Rightarrow\; s_{1,2} = \frac{-\lambda \pm \sqrt{\lambda^2 - 4Ik}}{2I} \quad &\text{(characteristic polynomial)}
> \end{aligned}$$
>
> $$\boxed{\theta_s = \frac{2I\dot\phi}{k}\,\Omega \quad\Longleftrightarrow\quad \Omega = \frac{k}{2I\dot\phi}\,\theta_s}$$
>
> **Units:** $[\mathrm M\,\mathrm L^2][\mathrm{T^{-1}}][\mathrm{T^{-1}}]/[\mathrm{M\,L^2\,T^{-2}}] = 1$ (rad)
> **Meaning:** the steady gimbal angle is proportional to the yaw rate: reading $\theta$ measures $\Omega$, which is what a rate gyro does. The sensitivity grows with the spin angular momentum and falls with the stiffness. With positive $\Omega$ and positive spin, $\theta_s$ is positive: the axle tilts towards $\mathbf k_a$; the check below confirms this sign with the angular momentum.

> [!derivation] Part (g): critical damping
> **Law:** roots of the characteristic polynomial of the linearized equation; a double real root
> **Source:** Notes.pdf, Sec. 14.4
>
> The system is critically damped when the two roots of the previous box coincide, that is when the discriminant is zero; below that value of $\lambda$ the roots are complex (damped oscillation), above it they are real and distinct (overdamped).
>
> $$\begin{aligned}
> \lambda^2 - 4Ik &= 0 \quad &\text{(zero discriminant)} \\
> \lambda_c &= \sqrt{4Ik} = 2\sqrt{Ik} \quad &\text{(positive root, $\lambda$ positive)} \\
> s_{1} &= s_{2} = -\frac{\lambda_c}{2I} = -\sqrt{\frac{k}{I}} \quad &\text{(double root)}
> \end{aligned}$$
>
> $$\boxed{\lambda_c = 2\sqrt{kI}}$$
>
> **Units:** $\sqrt{[\mathrm{M\,L^2\,T^{-2}}][\mathrm{M\,L^2}]} = [\mathrm{M\,L^2\,T^{-1}}]$, the units of a torque per angular rate (N m s)
> **Meaning:** with this damping (the double root) the gimbal reaches the steady reading without overshoot and, by a standard result of the course on the damped oscillator, faster than with any other damping that avoids overshoot, with the time scale of the square root of $I$ over $k$; it does not depend on the spin or on the yaw rate, because in the linearized equation they appear only in the forcing.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Bases of $S_b$ and $S_d$ in $\mathcal B_a$ | $\mathbf i_b = \mathbf i_a$, $\mathbf j_b = \cos\theta\,\mathbf j_a + \sin\theta\,\mathbf k_a$, $\mathbf k_b = -\sin\theta\,\mathbf j_a + \cos\theta\,\mathbf k_a$; $\mathbf i_d = \cos\phi\,\mathbf i_a + \sin\theta\sin\phi\,\mathbf j_a - \cos\theta\sin\phi\,\mathbf k_a$, $\mathbf j_d = \mathbf j_b$, $\mathbf k_d = \sin\phi\,\mathbf i_a - \sin\theta\cos\phi\,\mathbf j_a + \cos\theta\cos\phi\,\mathbf k_a$ |
| (b) Angular velocities and accelerations | $\boldsymbol\omega_{b0} = \dot\theta\,\mathbf i_b + \Omega\sin\theta\,\mathbf j_b + \Omega\cos\theta\,\mathbf k_b$, $\boldsymbol\omega_{d0} = \boldsymbol\omega_{b0} + \dot\phi\,\mathbf j_b$; $\boldsymbol\alpha_{b0} = \ddot\theta\,\mathbf i_b + (\dot\Omega\sin\theta + \Omega\dot\theta\cos\theta)\mathbf j_b + (\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta)\mathbf k_b$, $\boldsymbol\alpha_{d0} = (\ddot\theta - \Omega\dot\phi\cos\theta)\mathbf i_b + (\dot\Omega\sin\theta + \Omega\dot\theta\cos\theta + \ddot\phi)\mathbf j_b + (\dot\Omega\cos\theta - \Omega\dot\theta\sin\theta + \dot\phi\dot\theta)\mathbf k_b$ |
| (c) Torques | On the gimbal: spring $-k\theta\,\mathbf i_b$, damper $-\lambda\dot\theta\,\mathbf i_b$, bearing moment of the aircraft $\mathbf M_{ab}$ normal to $\mathbf i_b$ (found $M_3\,\mathbf k_b$), spin-axle moment of the disk $-\mathbf M_{bd}$; on the disk: $\mathbf M_{bd} = -(k\theta + \lambda\dot\theta)\mathbf i_b + M_3\,\mathbf k_b$ (none along the axle), weight and axle force through $G$ (no moment); on the aircraft: the opposite pairs |
| (d) Equations of motion | $I\ddot\theta + \lambda\dot\theta + k\theta - I\Omega^2\sin\theta\cos\theta - 2I\Omega\dot\phi\cos\theta = 0$; $\ddot\phi + \dot\Omega\sin\theta + \Omega\dot\theta\cos\theta = 0$; reaction $M_3 = I\dot\Omega\cos\theta + 2I\dot\phi\dot\theta$ |
| (e) Constant of motion | $\mathbf H_G^d\cdot\mathbf j_b = 2I(\Omega\sin\theta + \dot\phi) = 2In_0$ |
| (f) Linearized equation and steady relation | $I\ddot\theta + \lambda\dot\theta + k\theta = 2I\dot\phi\,\Omega(t)$; for constant $\Omega$, $\theta \to \theta_s = 2I\dot\phi\,\Omega/k$, i.e. $\Omega = k\theta_s/(2I\dot\phi)$ |
| (g) Critical damping | $\lambda_c = 2\sqrt{kI}$ |

**Limiting cases and consistency:** the key prints no answer for this problem (Problems.pdf, pp. 77 to 81 checked).

> [!derivation] Check: sign of the steady deflection from the turning angular momentum
> **Law:** moment equation at $G$ in steady state; derivative of a vector carried by the aircraft
> **Source:** Notes.pdf, Eq. 12.13; Notes.pdf, Eq. 3.8
>
> In the steady state with small $\theta$ the angular momentum of the disk is, to leading order, $2I$ times the spin along $\mathbf j_b$, close to $\mathbf j_a$, a vector fixed in the aircraft; it is carried round by the yaw rate.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_G^d}{dt}\right|_0 &\approx \Omega\,\mathbf k_a\times 2I\dot\phi\,\mathbf j_a = 2I\dot\phi\,\Omega\left(\mathbf k_a\times\mathbf j_a\right) = -2I\dot\phi\,\Omega\,\mathbf i_a \quad &\text{(Eq. 3.8: the components are constant in $S_a$; $\mathbf k_a\times\mathbf j_a = -\mathbf i_a$)} \\
> -k\theta_s\,\mathbf i_b &= -2I\dot\phi\,\Omega\,\mathbf i_a \;\Rightarrow\; \theta_s = \frac{2I\dot\phi\,\Omega}{k} \quad &\text{(the only torque about $\mathbf i_b$ at rest is the spring)}
> \end{aligned}$$
>
> $$\boxed{\theta_s = \frac{2I\dot\phi\,\Omega}{k}\ \text{by both routes}}$$
>
> **Units:** rad
> **Meaning:** to turn the spin angular momentum with the aircraft, the disk needs a torque along minus $\mathbf i_a$; the spring gives it only when $\theta$ is positive (for positive spin and yaw rate), so the axle tilts towards $\mathbf k_a$, as found from the linearized equation.

* **No yaw rate.** With $\Omega$ zero the equation of $\theta$ is a free damped oscillator and $\theta$ returns to zero; the second equation leaves the rate of $\phi$ constant.
* **No spin.** With the spin integral $n_0$ zero, the forcing of the linearized equation vanishes: a disk that does not spin gives no reading, the instrument works through the gyroscopic term only.
* **Exact equation.** Before linearizing, the equation of $\theta$ also carries the term in the square of $\Omega$; by the ratio of part (f) it is smaller than the forcing by the product of $\theta$ and the ratio of $\Omega$ to the spin.
* **Dimensions.** Every term of the equation of $\theta$ is a torque (N m); the steady angle is dimensionless; the critical damping is a torque per angular rate.
