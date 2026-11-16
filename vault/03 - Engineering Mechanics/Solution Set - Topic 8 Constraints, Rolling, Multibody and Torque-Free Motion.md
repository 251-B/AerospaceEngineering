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
