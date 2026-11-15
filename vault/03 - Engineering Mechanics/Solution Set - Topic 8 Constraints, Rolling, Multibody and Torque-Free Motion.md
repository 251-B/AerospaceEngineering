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
