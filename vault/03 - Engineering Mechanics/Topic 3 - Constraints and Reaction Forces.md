---
title: "Topic 3 - Constraints and Reaction Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-3
  - point-particle
  - constraints
  - degrees-of-freedom
  - tangent-and-normal-subspaces
  - reaction-forces
  - friction
  - newtonian-procedure
---

# Topic 3 - Constraints and Reaction Forces

> A particle that must stay on a surface or on a curve loses one or two of its three configuration degrees of freedom, and the constraint makes itself felt through an unknown reaction force $\mathbf N$ that lies in the normal subspace of the constraint: one unknown for a surface, two for a curve, so that Newton's three scalar equations always close the problem. Projected on the tangent directions, the second law gives equations of motion free of the reaction; projected on the normal directions, it gives the reaction afterwards. A smooth stationary constraint never does work, so it does not decide whether the mechanical energy is conserved, while a moving constraint can work and friction, bounded by the normal reaction and opposed to the relative velocity, dissipates energy while the particle slides. The same ideas, applied step by step, make up the Newtonian procedure for any problem of particles.

This note follows `Notes.pdf` Chapter 6 (Constraints and reaction forces, Eqs. 6.1 to 6.21: curves and surfaces, choosing coordinates, tangent and normal vectors, motion on a smooth surface, motion along a smooth curve, friction forces) and Chapter 7 (The Newtonian mechanics approach I, Eq. 7.1 and Sections 7.1 to 7.8: understanding the problem, selecting the coordinates, defining reference frames, kinematics of the particles, defining the forces, obtaining the equations of motion, integration and particular questions, final comments), with the deck of Lecture 3 (Constraints and reaction forces, Slides 1 to 24), in the order of the notes; the slides on two-particle constraints, on the classification of constraints and their examples (Slides 17 and 21 to 23) are placed where the notes discuss the same ideas. Neither chapter has figures of its own: the figures redraw the sketches of the slides or are drawn for this note, and the worked examples are those of the slides; where an example or a step is built for this note it is said so. Earlier results are cited, not re-derived: the change of basis (Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20), the dot product (Notes.pdf, Eq. 1.24), the cross product, which is perpendicular to both factors (Notes.pdf, Sec. 1.6.2), and its distributivity (Notes.pdf, Eq. 1.32), the derivative of a unit vector of a rotating basis (Notes.pdf, Eq. 1.62), the gradient (Notes.pdf, Eq. 1.74), the velocity and acceleration (Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4), the intrinsic basis (Notes.pdf, Eq. 2.13) and the velocity and acceleration written in it (Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.17), the cylindrical and spherical bases (Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.32), the Coriolis theorem and the composition of velocities (Notes.pdf, Eq. 3.8; Notes.pdf, Eq. 3.20), the second law (Notes.pdf, Eq. 4.4) and the theorem of kinetic energy and the conservation of mechanical energy (Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.31).
See also [[Concept - Classification of Constraints Holonomic Rheonomic and Unilateral]], [[Concept - Normal and Tangent Subspaces for Surfaces and Curves]], [[Concept - Constraint and Reaction Forces Dynamical Decoupling]], [[Concept - Coulomb Friction as Applied Force and Tangent Reaction]], [[Concept - Work and Power of Constraint Forces and Energy Preservation]] and [[Concept - Constraints on Multi-Particle Systems and Pulleys]].

| Symbol | Meaning |
| :--- | :--- |
| $S_0 : \{O;\mathcal B_0\}$, $\mathcal B_0 : \{\mathbf i,\mathbf j,\mathbf k\}$ | inertial reference frame and its basis (also written $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$); axes $Ox$, $Oy$, $Oz$ |
| $x, y, z$ | Cartesian coordinates of a point in $S_0$ |
| $P$, $m$ | the point particle and its mass |
| $P'$, $m'$ | a second particle and its mass ([Lecture 3, Slide 17] writes $Q$) |
| $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf a_0^P$ | position, velocity and acceleration of $P$ with respect to $S_0$ (Topic 1); $v_0^P$ is the speed |
| $n_{\mathrm{dof}}$, $n_c$ | number of configuration degrees of freedom and number of independent constraint equations |
| $f(x,y,z)$, $h(x,y,z)$ | functions whose zero sets are surfaces (Eqs. 6.5, 6.7; the notes and the slides write the second one $g$, a letter kept here for gravity) |
| $\alpha$; $\alpha$, $\beta$ | parameter of a curve in parametric form; the two parameters of a surface in parametric form (Eq. 6.1 writes the curve parameter $\lambda$, a letter kept here for the multiplier of the reaction) |
| $f_1, f_2, f_3$; $g_1, g_2, g_3$ | functions of the parametric forms of a curve and of a surface (Eqs. 6.1, 6.3) |
| $C : (C_x, C_y, C_z)$, $a$ | centre and radius of the circumference of Eqs. 6.2 and 6.8; $a$ is also the radius of the circle of [Lecture 3, Slide 15] and of the cylinder of [Lecture 3, Slide 20] |
| $R_s$ | radius of the sphere of Eqs. 6.4 and 6.6 and of [Lecture 3, Slide 6] (the notes write $R$, the slide $a$) |
| $a_e$, $b_e$ | semi-axes of the ellipse of [Lecture 3, Slides 6 and 11] (the slides write $a$, $b$) |
| $R$, $\theta$, $z$; $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ | cylindrical coordinates and their local basis (Notes.pdf, Sec. 2.6.2) |
| $r$, $\theta$, $\varphi$; $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf e_\varphi$ | spherical coordinates (radius, azimuth, latitude) and their local basis (Notes.pdf, Sec. 2.6.3) |
| $A$, $\ell$ | fixed point and length of the string or rod that holds $P$ (Sec. 6.2) |
| $\gamma$, $\ell_V$ | half-angle of the cone of Sec. 6.2 and distance of $P$ to its vertex (the notes write $\ell$ for that distance) |
| $s$; $\mathbf e_t$, $\mathbf e_n$, $\mathbf e_b$; $\rho$ | arc length, intrinsic basis and radius of curvature (Topic 1) |
| $V_N$, $V_T$ | normal and tangent vector subspaces of a constraint at a point ([Lecture 3, Slides 7 and 8]) |
| $\mathbf n$; $\mathbf n_f$, $\mathbf n_h$ | normal vector of a surface; the two normal vectors of a curve given as the intersection of the surfaces $f$ and $h$ (the slides write $\mathbf n_g$) |
| $\mathbf t$; $\mathbf t_\alpha$, $\mathbf t_\beta$; $\mathbf t_R$, $\mathbf t_\theta$ | tangent vector of a curve; the two tangent vectors of a surface given by $\alpha$ and $\beta$; those of the paraboloid parametrized by $R$ and $\theta$ |
| $\mathbf u_n$ | unit normal of a surface, Eq. 6.10 |
| $\mathcal B_P$ | local, in general non-orthonormal, basis at a point of a constraint ([Lecture 3, Slides 9 and 10]) |
| $\sigma$, $\Gamma$ | parameter of a curve $\Gamma$ drawn on a surface, used to prove that the gradient is normal to it |
| $\mathbf F$; $F_t$, $F_n$, $F_b$ | resultant applied force on $P$ and its intrinsic components (Eq. 6.15) |
| $\mathbf N$; $\lambda$; $\lambda_1$, $\lambda_2$ | normal reaction of a smooth constraint; its unknown multiplier for a surface (Eq. 6.11); its two multipliers for a curve (Eq. 6.13) |
| $N_1$, $N_2$; $N_n$, $N_b$ | unknown components of the reaction along $\mathbf n$ or $\mathbf n_f$, $\mathbf n_h$ ([Lecture 3, Slide 13]); its intrinsic components (Eq. 6.16) |
| $N_R$, $N_z$ | components of the reaction along $\mathbf e_R$ and $\mathbf k$ in the worked examples |
| $\dot W_0$, $\delta W_0$, $W_0$ | power of a force, its work in a time $dt$, and its work over an interval, as seen from $S_0$; $\dot W_0^{(P)}$, $\dot W_0^{(P')}$ the power of the string on $P$ and on $P'$ |
| $T_0$, $V_0$, $E_0$ | kinetic, potential and mechanical energy with respect to $S_0$ (Topic 2) |
| $\mathbf F_\mu$; $R_1$, $R_2$; $\mu$ | friction force (the notes write $\mathbf R$); its unknown components along the tangent vectors while $P$ sticks; friction coefficient |
| $\mathbf F_g$, $g$ | weight of a particle and the acceleration of gravity |
| $\mathbf F_\tau$, $F_\tau$ | force of a string on a particle and the tension (its magnitude; the slides write $T$, a letter kept here for kinetic energy) |
| $K$ | constant of the first integral of the particle on the vertical circle |
| $\zeta$, $c$, $\ell_0$ | depth of $P$ below the spool, the rate at which the string is collected and the initial length of string ([Lecture 3, Slide 22]; the slide writes $L$) |
| $L$, $\rho_a$, $S_w$, $C_L$ | lift of the airplane of [Lecture 3, Slide 23], air density, wing area and lift coefficient; the speed of the airplane is $v_0^P$ (the slide writes $\rho$, $S$ and $v$) |
| $\eta$, $\eta'$, $\ell_s$, $\ell_c$ | depths of $P$ and $P'$ below the pulleys, total length of the string and its constant length over the pulleys (Section 7) |
| $S_1$, $\mathcal B_1$; $\mathbf i_1, \mathbf j_1, \mathbf k_1$ | an auxiliary frame, its basis and the vectors of that basis: the frame in which a rough constraint is at rest (Section 8), the frame whose basis is the polar basis $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf k$ and turns with the radius of the vertical circle (Sections 6 and 9), and the first frame of Eq. 7.1 |
| $S_c$, $\mathcal B_c$; $[{}_0R_c]$ | the frame of the rough cylinder of Section 8 that turns about its axis with the meridian plane of $P$, its cylindrical basis $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$, and its change of basis matrix to $\mathcal B_0$ (a separate letter, because in Section 8 $S_1$ is the frame in which the cylinder is at rest) |
| $S_2$; $\mathbf i_2, \mathbf j_2, \mathbf k_2$ | the frame rotated an angle $\theta$ with respect to $S_1$ about $\mathbf k_1$, and its basis (Eq. 7.1) |
| $[{}_0R_1]$, $[{}_1R_2]$ | change of basis matrices from the basis of $S_1$ to $\mathcal B_0$ and from that of $S_2$ to that of $S_1$ |
| $\boldsymbol\omega_{10}$, $\boldsymbol\omega_{21}$, $\boldsymbol\alpha_{10}$ | angular velocity of $S_1$ with respect to $S_0$, of $S_2$ with respect to $S_1$, and angular acceleration of $S_1$ with respect to $S_0$ (Topic 5 notation, Notes.pdf, Ch. 3) |
| $\mathbf r_1^P$, $\mathbf v_1^P$, $\mathbf a_1^P$ | position, velocity and acceleration of $P$ relative to $S_1$; for a rough constraint $\mathbf v_1^P$ is the velocity relative to the constraint (the slides write $\mathbf v_*^P$) |
| $\mathbf v_0^O$, $\mathbf a_0^O$ | velocity and acceleration of the origin of $S_1$ with respect to $S_0$ (zero in Section 9) |
| $k$, $\mathbf F_S$ | stiffness of a spring of zero natural length and its force on $P$ (Sec. 7.5) |
| $\theta_*$ | turning angle of the particle on the vertical circle, a root of the boundary of the region of existence |
| $\psi$; $v$, $t'$, $y'$, $\varepsilon'$ | constant angle between the velocity and the horizontal on the rough cylinder; integration (dummy) variables |
| $\varepsilon$; $\varepsilon_1$, $t_1$; $q$ | small departure of $\theta$ from the highest point of the vertical circle (Section 9); its value at an instant $t_1$; root of the characteristic equation of the linearized motion |
| $\ell_1$, $\ell_2$, $H$ | distances of $P$ to two parallel planes and the height of the second plane (Sec. 7.2; the notes write $l_1$, $l_2$, $L$) |

## 1. Constraints and configuration degrees of freedom

In many situations the motion of a particle is not free but restricted, or constrained: a ground vehicle must stay on the surface of a spherical Earth, a bead must slide along a fixed wire of known shape ([Lecture 3, Slide 3]). The constraints of this chapter are integrable: each one establishes a mathematical relation between the coordinates of the problem. Whenever there is one or more of them, the number of degrees of freedom is reduced, so fewer independent parameters, or generalized coordinates, are needed to fix the position of the particle; at the same time unknown reaction forces appear, which make the motion fulfil the constraints (Notes.pdf, Ch. 6). The simple constraints on a single particle are stationary surfaces, two-dimensional objects, and stationary curves, one-dimensional objects: they can be written as equations among the coordinates, for example $x$, $y$, $z$, and they do not depend on time ([Lecture 3, Slide 3]).

![[attachments/EM-T/t3-constraints.svg]]

> [!derivation] Configuration degrees of freedom of a constrained particle
> **Law:** each independent constraint equation among the coordinates removes one independent coordinate
> **Source:** [Lecture 3, Slide 4]; Notes.pdf, Ch. 6; Notes.pdf, Sec. 2.7
>
> A free particle needs its three coordinates. A surface is one equation among them (Eq. 6.5); a curve, the intersection of two surfaces, is two equations (Eq. 6.7).
>
> $$\begin{aligned}
> n_{\mathrm{dof}} &= 3 - n_c \quad &\text{(three coordinates minus one per independent constraint equation)} \\
> n_{\mathrm{dof}}\big|_{\text{free}} &= 3 - 0 = 3 \quad &\text{(no constraint)} \\
> n_{\mathrm{dof}}\big|_{\text{surface}} &= 3 - 1 = 2 \quad &\text{(one equation, Eq. 6.5)} \\
> n_{\mathrm{dof}}\big|_{\text{curve}} &= 3 - 2 = 1 \quad &\text{(two equations, Eq. 6.7)}
> \end{aligned}$$
>
> $$\boxed{n_{\mathrm{dof}} = 3 \ \text{(free)},\qquad 2 \ \text{(on a surface)},\qquad 1 \ \text{(on a curve)}}$$
>
> **Units:** pure numbers
> **Meaning:** a particle confined to a surface, or free in a two-dimensional space, has two configuration degrees of freedom; on a curve, or free in a one-dimensional space, it has one ([Lecture 3, Slide 4]). The two equations of a curve must be independent: two coincident surfaces would describe a surface, not a curve.

There are basically two ways to deal with a simple constraint ([Lecture 3, Slide 4]):

| Way | What is done | Comment |
| :--- | :--- | :--- |
| ignore the constraint in the choice of coordinates | use a three-dimensional coordinate system, for example $x$, $y$, $z$, and add the constraint equations explicitly to the formulation | the differential equations of motion must be complemented with the algebraic constraint equations; the solution of this differential-algebraic system is generally complex, so the way is usually not advised (it is the formulation of Eqs. 6.11 and 6.13) |
| parametrize the constraint | pick as many generalized coordinates as configuration degrees of freedom, chosen so that every value of them lies on the constraint | the constraint equations are satisfied identically and need no further attention; this is the path taken in the course |

## 2. Curves and surfaces

Before the constrained motion is analysed, the different ways of describing curves and surfaces in three-dimensional space are reviewed (Notes.pdf, Sec. 6.1; [Lecture 3, Slide 5]).

| Object | Form | Equations | Source |
| :--- | :--- | :--- | :--- |
| curve | parametric: a vector function of one parameter $\alpha$, $\mathbf r = \mathbf r(\alpha)$ | $x = f_1(\alpha)$, $y = f_2(\alpha)$, $z = f_3(\alpha)$ | Eq. 6.1; [Lecture 3, Slide 5] |
| surface | parametric: a vector function of two independent parameters, $\mathbf r = \mathbf r(\alpha,\beta)$ | $x = g_1(\alpha,\beta)$, $y = g_2(\alpha,\beta)$, $z = g_3(\alpha,\beta)$ | Eq. 6.3; [Lecture 3, Slide 5] |
| surface | implicit: the two parameters eliminated from the three equations | $f(x,y,z) = 0$ | Eq. 6.5; [Lecture 3, Slide 5] |
| curve | implicit: the parameter eliminated, leaving two equations, the intersection of two surfaces | $f(x,y,z) = 0$, $h(x,y,z) = 0$ | Eq. 6.7; [Lecture 3, Slide 5] |

The parameter of a curve can be, for example, an arc length. If a parametric form of a simple constraint is available, it gives a natural choice of generalized coordinates for the motion of the particle: $\alpha$ for a curve, $\alpha$ and $\beta$ for a surface ([Lecture 3, Slide 5]). It is useful to be able to pass from the parametric form to the implicit form and back; the boxes below do it for the examples of the notes and of [Lecture 3, Slide 6].

![[attachments/EM-T/t3-curve-surface-forms.svg]]

> [!derivation] The circumference: from the parametric to the implicit form
> **Law:** elimination of the parameter with $\cos^2\theta + \sin^2\theta = 1$
> **Source:** Notes.pdf, Eq. 6.2; Notes.pdf, Eq. 6.8
>
> The circumference of radius $a$ lies on a horizontal plane, with centre at the point $C$; Eq. 6.2 parametrizes it with the angle $\theta$, measured at $C$ from the direction of $\mathbf i$: the projection of the radius on $\mathbf i$ is the leg adjacent to $\theta$, of length $a\cos\theta$, and its projection on $\mathbf j$ is the leg opposite to $\theta$, of length $a\sin\theta$, in the right triangle whose hypotenuse is the radius.
>
> $$\begin{aligned}
> x &= C_x + a\cos\theta,\quad y = C_y + a\sin\theta,\quad z = C_z \quad &\text{(Eq. 6.2)} \\
> x - C_x &= a\cos\theta,\quad y - C_y = a\sin\theta \quad &\text{(isolate the trigonometric terms)} \\
> (x - C_x)^2 + (y - C_y)^2 &= a^2\cos^2\theta + a^2\sin^2\theta \quad &\text{(square both equations and add them)} \\
> &= a^2 \quad &\text{($\cos^2\theta + \sin^2\theta = 1$)} \\
> z - C_z &= 0 \quad &\text{(third equation of Eq. 6.2)}
> \end{aligned}$$
>
> $$\boxed{(x - C_x)^2 + (y - C_y)^2 - a^2 = 0,\qquad z - C_z = 0}$$
>
> **Units:** $\mathrm{m^2}$ in the first equation, $\mathrm m$ in the second
> **Meaning:** the circumference is the intersection of a circular cylinder of axis parallel to $Oz$ through $C$ with the horizontal plane through $C$ (Eq. 6.8). The pair is not unique: the same circumference is also the intersection of that plane with the sphere of radius $a$ centred at $C$ (Notes.pdf, Sec. 6.1).

> [!warning] Discrepancy with Notes.pdf, Eq. 6.8: the radius
> Eq. 6.2 calls the radius of the circumference $a$, but Eq. 6.8, which is said to be the implicit form of the same circumference, prints $R^2$ in its place. The box above shows that the elimination of $\theta$ from Eq. 6.2 gives $a^2$: the two letters denote the same radius.

> [!derivation] The sphere of the notes: from the parametric to the implicit form
> **Law:** elimination of two parameters with $\cos^2 + \sin^2 = 1$, used twice
> **Source:** Notes.pdf, Eq. 6.4; Notes.pdf, Eq. 6.6
>
> In Eq. 6.4, $\alpha$ is the azimuth, measured in the plane $Oxy$ from $Ox$, and $\beta$ is the angle measured from the axis $Oz$ (a colatitude): the radius $R_s$ is the hypotenuse of a right triangle in the meridian plane whose leg along $Oz$ (adjacent to $\beta$) is $R_s\cos\beta$ and whose horizontal leg (opposite to $\beta$) is $R_s\sin\beta$; the horizontal leg is in turn the hypotenuse of a triangle in the plane $Oxy$ with legs $R_s\sin\beta\cos\alpha$ along $Ox$ (adjacent to $\alpha$) and $R_s\sin\beta\sin\alpha$ along $Oy$ (opposite to $\alpha$).
>
> $$\begin{aligned}
> x &= R_s\cos\alpha\sin\beta,\quad y = R_s\sin\alpha\sin\beta,\quad z = R_s\cos\beta \quad &\text{(Eq. 6.4)} \\
> x^2 + y^2 &= R_s^2\cos^2\alpha\sin^2\beta + R_s^2\sin^2\alpha\sin^2\beta \quad &\text{(square the first two and add)} \\
> &= R_s^2\sin^2\beta\left(\cos^2\alpha + \sin^2\alpha\right) \quad &\text{(common factor $R_s^2\sin^2\beta$)} \\
> &= R_s^2\sin^2\beta \quad &\text{($\cos^2\alpha + \sin^2\alpha = 1$: $\alpha$ is eliminated)} \\
> x^2 + y^2 + z^2 &= R_s^2\sin^2\beta + R_s^2\cos^2\beta \quad &\text{(add the square of the third)} \\
> &= R_s^2 \quad &\text{($\sin^2\beta + \cos^2\beta = 1$: $\beta$ is eliminated)}
> \end{aligned}$$
>
> $$\boxed{x^2 + y^2 + z^2 - R_s^2 = 0}$$
>
> **Units:** $\mathrm{m^2}$
> **Meaning:** Eq. 6.6, the sphere of radius $R_s$ centred at $O$ in implicit form: three parametric equations with two parameters give one implicit equation.

> [!derivation] The examples of Lecture 3: an ellipse and a sphere in implicit form
> **Law:** elimination of the parameters with $\cos^2 + \sin^2 = 1$
> **Source:** [Lecture 3, Slide 6]
>
> Ellipse of semi-axes $a_e$ along $Ox$ and $b_e$ along $Oy$, in the plane $Oxy$, parameter $\alpha$. Sphere of radius $R_s$ with the parameters $\alpha$ (azimuth) and $\varphi$ (latitude, measured from the plane $Oxy$; the slide writes $\beta$): the radius is the hypotenuse of a meridian triangle with horizontal leg $R_s\cos\varphi$, adjacent to $\varphi$, and vertical leg $R_s\sin\varphi$, opposite to it.
>
> $$\begin{aligned}
> x &= a_e\cos\alpha,\quad y = b_e\sin\alpha,\quad z = 0 \quad &\text{(ellipse, Slide 6)} \\
> \frac{x}{a_e} &= \cos\alpha,\quad \frac{y}{b_e} = \sin\alpha \quad &\text{(divide each equation by its semi-axis)} \\
> \frac{x^2}{a_e^2} + \frac{y^2}{b_e^2} &= \cos^2\alpha + \sin^2\alpha \quad &\text{(square both equations and add them)} \\
> &= 1 \quad &\text{($\alpha$ is eliminated)} \\
> x &= R_s\cos\alpha\cos\varphi,\quad y = R_s\sin\alpha\cos\varphi,\quad z = R_s\sin\varphi \quad &\text{(sphere, Slide 6)} \\
> x^2 + y^2 &= R_s^2\cos^2\alpha\cos^2\varphi + R_s^2\sin^2\alpha\cos^2\varphi \quad &\text{(square the first two and add)} \\
> &= R_s^2\cos^2\varphi\left(\cos^2\alpha + \sin^2\alpha\right) \quad &\text{(common factor $R_s^2\cos^2\varphi$)} \\
> &= R_s^2\cos^2\varphi \quad &\text{($\cos^2\alpha + \sin^2\alpha = 1$: $\alpha$ is eliminated)} \\
> x^2 + y^2 + z^2 &= R_s^2\cos^2\varphi + R_s^2\sin^2\varphi \quad &\text{(add the square of the third)} \\
> &= R_s^2 \quad &\text{($\varphi$ is eliminated)}
> \end{aligned}$$
>
> $$\boxed{\text{ellipse: } \frac{x^2}{a_e^2} + \frac{y^2}{b_e^2} - 1 = 0,\ \ z = 0;\qquad \text{sphere: } x^2 + y^2 + z^2 - R_s^2 = 0}$$
>
> **Units:** the equation of the ellipse is dimensionless, the plane equation in $\mathrm m$, the sphere in $\mathrm{m^2}$
> **Meaning:** the ellipse is the intersection of an elliptic cylinder of axis $Oz$ with the plane $Oxy$; the sphere of the slide is the sphere of Eq. 6.6 with the latitude in place of the colatitude: $\varphi$ and the $\beta$ of Eq. 6.4 add up to a right angle, since $\cos\beta$ and $\sin\varphi$ are both the vertical leg divided by the hypotenuse. Different parametrizations give the same implicit equation.

## 3. Choosing coordinates

The coordinates of a problem can be chosen freely, but an intelligent choice can facilitate the work enormously, and the constraints are the main aspect to consider when selecting them (Notes.pdf, Sec. 6.2). As many coordinates are needed as degrees of freedom; the only exception is a non-integrable constraint, which appears in the second part of the course (Notes.pdf, Sec. 6.2, which refers to its Sec. 13.2). In general the coordinates should reflect the geometry of the constraints as much as possible: the constraint is then easy to parametrize in terms of them, and the vector basis associated with the coordinates at each point is aligned with the tangent and normal subspaces of the constraint (Section 4). The notes give four orientative examples, worked out in the box below.

![[attachments/EM-T/t3-coordinate-choices.svg]]

> [!derivation] Coordinates adapted to four constraints
> **Law:** parametrization of the constraint by as many coordinates as degrees of freedom; spherical and cylindrical local bases; right triangles in the meridian plane
> **Source:** Notes.pdf, Sec. 6.2; Notes.pdf, Eq. 2.32; Notes.pdf, Eq. 2.36; Notes.pdf, Eq. 2.24
>
> (1) $P$ is attached to the fixed point $A$ by a string or rod of length $\ell$: it moves on the sphere of radius $\ell$ centred at $A$, and the spherical angles $\theta$ (azimuth) and $\varphi$ (latitude), measured at $A$ with axes parallel to those of $S_0$, are a good choice. (2) $P$ must remain on a cone of vertex $O$, axis $Oz$ and half-angle $\gamma$ (the geometry of the cone is chosen for this note): the azimuth $\theta$ and the distance $\ell_V$ to the vertex, or the height $z$ instead of $\ell_V$, are good choices; in the meridian plane through $P$ the generatrix $OP$ is the hypotenuse of a right triangle with the angle $\gamma$ at $O$, whose leg along $Oz$ (adjacent) is $\ell_V\cos\gamma$ and whose horizontal leg (opposite) is $\ell_V\sin\gamma$, so the cylindrical coordinates of $P$ are those legs. (3) $P$ moves along a wire of fixed shape: the arc length $s$, or one Cartesian coordinate that parametrizes the curve. (4) $P$ must remain on a surface given in parametric form: the two parameters $\alpha$ and $\beta$.
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OA} + \ell\,\mathbf e_r(\theta,\varphi) \quad &\text{(1: Eq. 2.36 from the centre $A$ with $r = \ell$ fixed)} \\
> \mathbf e_r &= \cos\varphi\cos\theta\,\mathbf i + \cos\varphi\sin\theta\,\mathbf j + \sin\varphi\,\mathbf k \quad &\text{(1: Eq. 2.32)} \\
> R &= \ell_V\sin\gamma,\quad z = \ell_V\cos\gamma \quad &\text{(2: legs of the meridian triangle)} \\
> \mathbf r_0^P &= \ell_V\sin\gamma\,\mathbf e_R(\theta) + \ell_V\cos\gamma\,\mathbf k \quad &\text{(2: Eq. 2.28 with these $R$ and $z$; $\mathbf e_R$ of Eq. 2.24)} \\
> x^2 + y^2 - z^2\tan^2\gamma &= R^2 - z^2\tan^2\gamma \quad &\text{(2: $x^2 + y^2 = R^2$, the squared distance to $Oz$)} \\
> &= \ell_V^2\sin^2\gamma - \ell_V^2\cos^2\gamma\,\tan^2\gamma \quad &\text{(2: substitute the legs $R$ and $z$)} \\
> &= \ell_V^2\sin^2\gamma - \ell_V^2\cos^2\gamma\,\frac{\sin^2\gamma}{\cos^2\gamma} \quad &\text{(2: $\tan\gamma = \sin\gamma/\cos\gamma$)} \\
> &= \ell_V^2\sin^2\gamma - \ell_V^2\sin^2\gamma \quad &\text{(2: simplify $\cos^2\gamma$)} \\
> &= 0 \quad &\text{(2: the two terms cancel: the implicit equation of the cone)} \\
> \mathbf r_0^P &= \mathbf r_0^P(s) \quad &\text{(3: the position along the wire)} \\
> \mathbf r_0^P &= \mathbf r(\alpha,\beta) \quad &\text{(4: Eq. 6.3)}
> \end{aligned}$$
>
> $$\boxed{(1)\ \theta,\varphi;\qquad (2)\ \theta,\ell_V\ \text{or}\ \theta, z;\qquad (3)\ s\ \text{or}\ x;\qquad (4)\ \alpha,\beta}$$
>
> **Units:** lengths in $\mathrm m$, angles in $\mathrm{rad}$
> **Meaning:** the motion on the sphere and on the cone has two degrees of freedom and the motion along the wire one: each position vector depends on exactly that number of coordinates, and every value of them lies on the constraint, which is then satisfied identically. With the angles of (1) the local spherical basis has $\mathbf e_r$ normal to the sphere and $\mathbf e_\theta$, $\mathbf e_\varphi$ tangent to it.

Once the coordinates have been selected, the procedures of kinematics express the position, velocity and acceleration of the particle as functions of them and of their time derivatives: this is the main output of kinematics and the information needed to solve the dynamics of the motion (Notes.pdf, Sec. 6.2).

## 4. Tangent and normal vectors

When working with curve or surface constraints, it is useful to have a local vector basis that separates the directions tangent and normal to the constraint (Notes.pdf, Sec. 6.3; [Lecture 3, Slides 7 and 8]). At each point of a smooth constraint two vector subspaces are defined: the tangent subspace $V_T$, the directions along which the particle can move while staying on the constraint, and the normal subspace $V_N$, the directions perpendicular to all of them. Their direct sum is the whole space and they share only the zero vector.

| Constraint | dimension of $V_T$ | dimension of $V_N$ | Source |
| :--- | :--- | :--- | :--- |
| surface (two-dimensional manifold) | 2: the tangent plane | 1: the normal line | Notes.pdf, Sec. 6.3; [Lecture 3, Slide 7] |
| curve (one-dimensional manifold) | 1: the tangent line | 2: the normal plane | Notes.pdf, Sec. 6.3; [Lecture 3, Slide 8] |
| both | $V_N \oplus V_T = \mathbb R^3$ | $V_N \cap V_T = \{\mathbf 0\}$ | [Lecture 3, Slides 7 and 8] |

### From the parametric form: tangent vectors first

When a constraint is given in parametric form, partial differentiation with respect to each parameter yields a basis of the tangent subspace; the vectors obtained are in general neither unit vectors nor orthogonal, and they are normalized or orthogonalized if required (Notes.pdf, Sec. 6.3). This is the approach of Chapter 2 for the tangent vector of a curve.

![[attachments/EM-T/t3-surface-normal.svg]]

> [!derivation] Tangent vectors of a parametric curve and of a parametric surface, and the normal of the surface
> **Law:** the tangent to a curve is the limit of the chord divided by the change of the parameter; a coordinate line of a surface is a curve on it; the cross product is perpendicular to both factors
> **Source:** Notes.pdf, Sec. 6.3; Notes.pdf, Eq. 2.9; Notes.pdf, Sec. 1.6.2; [Lecture 3, Slide 8]; [Lecture 3, Slide 9]
>
> The chord between the points of parameters $\alpha$ and $\alpha + \Delta\alpha$ of a curve lies, in the limit, along the curve; on a surface, the curve obtained by varying $\alpha$ with $\beta$ fixed lies on the surface, and so does the curve obtained by varying $\beta$ with $\alpha$ fixed.
>
> $$\begin{aligned}
> \mathbf t &= \lim_{\Delta\alpha \to 0}\frac{\mathbf r(\alpha + \Delta\alpha) - \mathbf r(\alpha)}{\Delta\alpha} \quad &\text{(curve: the limit of the chord over the parameter step)} \\
> &= \frac{dx}{d\alpha}\,\mathbf i + \frac{dy}{d\alpha}\,\mathbf j + \frac{dz}{d\alpha}\,\mathbf k \quad &\text{(component by component; $\mathbf i$, $\mathbf j$, $\mathbf k$ constant)} \\
> \left|\frac{d\mathbf r}{ds}\right| &= 1 \quad &\text{(if $\alpha$ is the arc length $s$, Eq. 2.9: $\mathbf t$ is then $\mathbf e_t$)} \\
> \mathbf t_\alpha &= \frac{\partial x}{\partial\alpha}\,\mathbf i + \frac{\partial y}{\partial\alpha}\,\mathbf j + \frac{\partial z}{\partial\alpha}\,\mathbf k \quad &\text{(surface: tangent of the line of varying $\alpha$, $\beta$ fixed)} \\
> \mathbf t_\beta &= \frac{\partial x}{\partial\beta}\,\mathbf i + \frac{\partial y}{\partial\beta}\,\mathbf j + \frac{\partial z}{\partial\beta}\,\mathbf k \quad &\text{(tangent of the line of varying $\beta$, $\alpha$ fixed)} \\
> \mathbf n &= \mathbf t_\alpha \times \mathbf t_\beta \quad &\text{(perpendicular to both tangent vectors, Sec. 1.6.2)}
> \end{aligned}$$
>
> $$\boxed{\mathbf t = \frac{d\mathbf r}{d\alpha},\qquad \mathbf t_\alpha = \frac{\partial\mathbf r}{\partial\alpha},\quad \mathbf t_\beta = \frac{\partial\mathbf r}{\partial\beta},\quad \mathbf n = \mathbf t_\alpha \times \mathbf t_\beta}$$
>
> **Units:** $\mathbf t$ has the units of length over the units of $\alpha$ (dimensionless when $\alpha$ is a length, $\mathrm{m/rad}$ when it is an angle); $\mathbf n$ the product of the units of $\mathbf t_\alpha$ and $\mathbf t_\beta$
> **Meaning:** $\mathbf t_\alpha$ and $\mathbf t_\beta$ span the tangent plane wherever they are independent; normalizing them gives two unit tangent vectors, which in general are not orthogonal, and normalizing $\mathbf n$ gives a unit normal (Notes.pdf, Sec. 6.3). Instead of differentiating, two independent vectors perpendicular to a known normal $\mathbf n$ may also be sought ([Lecture 3, Slide 9]). The local basis $\mathcal B_P$ made of $\mathbf t_\alpha$, $\mathbf t_\beta$ and $\mathbf n$ is in general neither unitary, nor orthogonal, nor right-handed ([Lecture 3, Slide 9]).

### From the implicit form: normal vectors first

When a constraint is given by implicit equations, it is easier to obtain first a basis of the normal subspace: each implicit equation represents a surface, and the gradient of its function is perpendicular to that surface (Notes.pdf, Sec. 6.3; [Lecture 3, Slide 7]).

> [!derivation] The gradient is normal to the surface
> **Law:** a curve drawn on the surface keeps the function equal to zero; chain rule for a function of three variables; definition of the gradient
> **Source:** Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 6.10; Notes.pdf, Eq. 1.74; [Lecture 3, Slide 7]
>
> Let $\Gamma$ be any curve drawn on the surface of Eq. 6.5, with parameter $\sigma$, so that $f$ is zero at every one of its points; its tangent vector is a vector of $V_T$, and by choosing $\Gamma$ through the point in every direction of the tangent plane, every vector of $V_T$ is reached.
>
> $$\begin{aligned}
> f\big(x(\sigma), y(\sigma), z(\sigma)\big) &= 0 \quad &\text{(for every $\sigma$: $\Gamma$ lies on the surface)} \\
> \frac{d}{d\sigma}f\big(x(\sigma), y(\sigma), z(\sigma)\big) &= \frac{\partial f}{\partial x}\frac{dx}{d\sigma} + \frac{\partial f}{\partial y}\frac{dy}{d\sigma} + \frac{\partial f}{\partial z}\frac{dz}{d\sigma} \quad &\text{(chain rule)} \\
> &= \left(\frac{\partial f}{\partial x}\,\mathbf i + \frac{\partial f}{\partial y}\,\mathbf j + \frac{\partial f}{\partial z}\,\mathbf k\right)\cdot\left(\frac{dx}{d\sigma}\,\mathbf i + \frac{dy}{d\sigma}\,\mathbf j + \frac{dz}{d\sigma}\,\mathbf k\right) \quad &\text{(the sum of products is a dot product in $\mathcal B_0$)} \\
> &= \nabla f\cdot\frac{d\mathbf r}{d\sigma} \quad &\text{(Eq. 6.9 for the first factor; tangent of $\Gamma$ for the second)} \\
> \nabla f\cdot\frac{d\mathbf r}{d\sigma} &= 0 \quad &\text{(derivative of the constant zero of the first row)} \\
> \lvert\nabla f\rvert &= \sqrt{\left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2 + \left(\frac{\partial f}{\partial z}\right)^2} \quad &\text{(magnitude in an orthonormal basis)} \\
> \mathbf u_n &= \frac{\nabla f}{\lvert\nabla f\rvert} \quad &\text{(normalize, Eq. 6.10, wherever the gradient is not zero)}
> \end{aligned}$$
>
> $$\boxed{\nabla f = \frac{\partial f}{\partial x}\,\mathbf i + \frac{\partial f}{\partial y}\,\mathbf j + \frac{\partial f}{\partial z}\,\mathbf k \ \in V_N,\qquad \mathbf u_n = \frac{\nabla f}{\lvert\nabla f\rvert}}$$
>
> **Units:** $\nabla f$ has the units of $f$ per metre; $\mathbf u_n$ is dimensionless
> **Meaning:** the gradient is perpendicular to every tangent direction, so it spans the one-dimensional normal subspace; it is in general not a unit vector. It points to the side on which $f$ grows: a step $d\mathbf r$ along $\nabla f$ changes $f$ by $\nabla f\cdot d\mathbf r$, a positive amount ([Lecture 3, Slide 7]). For a surface, two directions perpendicular to $\mathbf u_n$ complete a basis of space (Notes.pdf, Sec. 6.3).

![[attachments/EM-T/t3-curve-normals.svg]]

> [!derivation] A curve as the intersection of two surfaces: two normals and the tangent
> **Law:** a curve lying on two surfaces is tangent to both; the cross product is perpendicular to both factors; the tangent subspace of a curve has dimension one
> **Source:** Notes.pdf, Sec. 6.3; Notes.pdf, Eq. 6.7; Notes.pdf, Sec. 1.6.2; [Lecture 3, Slide 10]
>
> The curve of Eq. 6.7 lies on the surface of $f$ and on the surface of $h$, so its tangent $\mathbf t$ belongs to the tangent plane of each of them.
>
> $$\begin{aligned}
> \mathbf n_f &= \nabla f,\quad \mathbf n_h = \nabla h \quad &\text{(the gradient of each implicit equation, previous box)} \\
> \mathbf n_f\cdot\mathbf t &= 0,\quad \mathbf n_h\cdot\mathbf t = 0 \quad &\text{(previous box applied to each surface, with $\Gamma$ the curve itself)} \\
> \mathbf t &\parallel \mathbf n_f \times \mathbf n_h \quad &\text{(the cross product is perpendicular to both normals, Sec. 1.6.2, and $V_T$ is a line)}
> \end{aligned}$$
>
> $$\boxed{\mathbf n_f = \nabla f,\quad \mathbf n_h = \nabla h \ \in V_N,\qquad \mathbf t = \mathbf n_f \times \mathbf n_h \ \in V_T}$$
>
> **Units:** each normal has the units of its function per metre; $\mathbf t$ the product of both
> **Meaning:** the two gradients span the normal plane of the curve wherever they are independent, that is, where the two surfaces are not tangent to each other; they are in general neither unit vectors nor orthogonal (Notes.pdf, Sec. 6.3). The two normals may also be found as two independent vectors perpendicular to a known tangent $\mathbf t$, and the tangent may also be obtained by differentiating a parametric form ([Lecture 3, Slide 10]). The local basis $\mathcal B_P$ of $\mathbf t$, $\mathbf n_f$ and $\mathbf n_h$ is in general neither unitary, nor orthogonal, nor right-handed.

One can always operate on the parametric equations of a constraint to obtain an implicit representation, and vice versa; sometimes this offers a faster route to the vectors wanted (Notes.pdf, Sec. 6.3). The two examples of [Lecture 3, Slides 11 and 12] use both routes and check one against the other.

> [!example] Tangent and normal vectors of an ellipse ([Lecture 3, Slide 11])
> Find a tangent vector and two normal vectors for the ellipse of [Lecture 3, Slide 6], given in parametric form in the plane $Oxy$.
>
> | Data | Value |
> | :--- | :--- |
> | parametric form | $x = a_e\cos\alpha$, $y = b_e\sin\alpha$, $z = 0$ |
> | implicit form (Section 2) | $f = x^2/a_e^2 + y^2/b_e^2 - 1 = 0$, $h = z = 0$ |

![[attachments/EM-T/t3-ellipse-vectors.svg]]

> [!derivation] Tangent and normals of the ellipse
> **Law:** derivative of the parametric form; gradients of the implicit equations; dot and cross products in $\mathcal B_0$
> **Source:** [Lecture 3, Slide 11]; [Lecture 3, Slide 10]; Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 1.24; Notes.pdf, Eq. 1.32
>
> $$\begin{aligned}
> \mathbf t &= \frac{d}{d\alpha}\left(a_e\cos\alpha\right)\mathbf i + \frac{d}{d\alpha}\left(b_e\sin\alpha\right)\mathbf j + \frac{d}{d\alpha}(0)\,\mathbf k \quad &\text{(derivative of the parametric form)} \\
> &= -a_e\sin\alpha\,\mathbf i + b_e\cos\alpha\,\mathbf j \quad &\text{(derivatives of cosine and sine)} \\
> \mathbf n_f &= \frac{2x}{a_e^2}\,\mathbf i + \frac{2y}{b_e^2}\,\mathbf j + 0\,\mathbf k \quad &\text{(partial derivatives of $f$, Eq. 6.9)} \\
> &= \frac{2\cos\alpha}{a_e}\,\mathbf i + \frac{2\sin\alpha}{b_e}\,\mathbf j \quad &\text{(substitute the parametric form)} \\
> \mathbf n_h &= \mathbf k \quad &\text{(partial derivatives of $h = z$)} \\
> \mathbf t\cdot\mathbf n_f &= -a_e\sin\alpha\,\frac{2\cos\alpha}{a_e} + b_e\cos\alpha\,\frac{2\sin\alpha}{b_e} \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= -2\sin\alpha\cos\alpha + 2\sin\alpha\cos\alpha \quad &\text{(simplify the semi-axes)} \\
> &= 0 \quad &\text{(the two terms cancel)} \\
> \mathbf t\cdot\mathbf n_h &= 0 \quad &\text{($\mathbf t$ has no $\mathbf k$ component)} \\
> \mathbf n_f\times\mathbf n_h &= \frac{2\cos\alpha}{a_e}\,\mathbf i\times\mathbf k + \frac{2\sin\alpha}{b_e}\,\mathbf j\times\mathbf k \quad &\text{(distribute)} \\
> &= -\frac{2\cos\alpha}{a_e}\,\mathbf j + \frac{2\sin\alpha}{b_e}\,\mathbf i \quad &\text{($\mathbf i\times\mathbf k = -\mathbf j$, $\mathbf j\times\mathbf k = \mathbf i$)} \\
> &= -\frac{2}{a_e b_e}\left(-a_e\sin\alpha\,\mathbf i + b_e\cos\alpha\,\mathbf j\right) \quad &\text{(take out the factor $-2/(a_e b_e)$)} \\
> &= -\frac{2}{a_e b_e}\,\mathbf t \quad &\text{(the bracket is $\mathbf t$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf t = -a_e\sin\alpha\,\mathbf i + b_e\cos\alpha\,\mathbf j,\qquad \mathbf n_f = \frac{2\cos\alpha}{a_e}\,\mathbf i + \frac{2\sin\alpha}{b_e}\,\mathbf j,\qquad \mathbf n_h = \mathbf k}$$
>
> **Units:** $\mathbf t$ in $\mathrm{m/rad}$; $\mathbf n_f$ in $\mathrm{m^{-1}}$; $\mathbf n_h$ dimensionless
> **Meaning:** both routes agree: the tangent obtained by differentiation is perpendicular to the two gradients, and the cross product of the gradients is parallel to it (here with the opposite sense, which only depends on the order of the factors). $\mathbf n_f$ lies in the plane of the ellipse and points outwards, where $f$ grows; $\mathbf n_h$ is normal to that plane. For a circle, with equal semi-axes, $\mathbf n_f$ points along the radius and is perpendicular to $\mathbf t$, as expected.

> [!example] Tangent and normal vectors of a paraboloid ([Lecture 3, Slide 12])
> Find two tangent vectors and a normal vector for the surface given by the equation below, written as on the slide.
>
> | Data | Value |
> | :--- | :--- |
> | implicit form | $x^2 + y^2 = z$, with $z > 0$; $f = x^2 + y^2 - z = 0$ |
> | parametrization chosen here | cylindrical $R$, $\theta$: $x = R\cos\theta$, $y = R\sin\theta$, $z = R^2$, with $R > 0$ |

> [!warning] Units of the paraboloid of Lecture 3, Slide 12
> As printed, the equation adds squares of lengths and a length: it holds with every length measured in the same unit (for example $\mathrm m$), which amounts to a hidden coefficient of one unit of length multiplying $z$. The box below keeps the form of the slide; its unit line follows that reading.

![[attachments/EM-T/t3-paraboloid-vectors.svg]]

> [!derivation] Tangent and normal vectors of the paraboloid
> **Law:** gradient of the implicit form; partial derivatives of the parametric form; cross product in $\mathcal B_0$
> **Source:** [Lecture 3, Slide 12]; [Lecture 3, Slide 9]; Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 1.24; Notes.pdf, Eq. 1.32
>
> In the meridian plane of $P$, $R$ is the horizontal distance to $Oz$: the right triangle in the plane $Oxy$ with hypotenuse $R$ and angle $\theta$ at $O$ has the leg $R\cos\theta$ along $Ox$ (adjacent) and $R\sin\theta$ along $Oy$ (opposite), and the surface sets the height to $R^2$.
>
> $$\begin{aligned}
> \mathbf n &= \nabla f = 2x\,\mathbf i + 2y\,\mathbf j - \mathbf k \quad &\text{(partial derivatives of $x^2 + y^2 - z$)} \\
> \mathbf r(R,\theta) &= R\cos\theta\,\mathbf i + R\sin\theta\,\mathbf j + R^2\,\mathbf k \quad &\text{(parametric form; $z = x^2 + y^2 = R^2$)} \\
> \mathbf t_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j + 2R\,\mathbf k \quad &\text{(partial derivative with respect to $R$)} \\
> \mathbf t_\theta &= -R\sin\theta\,\mathbf i + R\cos\theta\,\mathbf j \quad &\text{(partial derivative with respect to $\theta$)} \\
> \mathbf t_R\cdot\mathbf n &= 2R\cos^2\theta + 2R\sin^2\theta - 2R \quad &\text{(dot product, with $x = R\cos\theta$, $y = R\sin\theta$)} \\
> &= 0 \quad &\text{($\cos^2\theta + \sin^2\theta = 1$)} \\
> \mathbf t_\theta\cdot\mathbf n &= -2R^2\sin\theta\cos\theta + 2R^2\sin\theta\cos\theta \quad &\text{(dot product, with $x = R\cos\theta$, $y = R\sin\theta$)} \\
> &= 0 \quad &\text{(the two terms cancel)} \\
> \mathbf t_R\times\mathbf t_\theta &= R\cos^2\theta\,\mathbf i\times\mathbf j - R\sin^2\theta\,\mathbf j\times\mathbf i - 2R^2\sin\theta\,\mathbf k\times\mathbf i + 2R^2\cos\theta\,\mathbf k\times\mathbf j \quad &\text{(distribute; the products $\mathbf i\times\mathbf i$ and $\mathbf j\times\mathbf j$ vanish)} \\
> &= R\cos^2\theta\,\mathbf k + R\sin^2\theta\,\mathbf k - 2R^2\sin\theta\,\mathbf j - 2R^2\cos\theta\,\mathbf i \quad &\text{($\mathbf j\times\mathbf i = -\mathbf k$, $\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= -2R^2\cos\theta\,\mathbf i - 2R^2\sin\theta\,\mathbf j + R\left(\cos^2\theta + \sin^2\theta\right)\mathbf k \quad &\text{(reorder; common factor $R$ in the $\mathbf k$ terms)} \\
> &= -2R^2\cos\theta\,\mathbf i - 2R^2\sin\theta\,\mathbf j + R\,\mathbf k \quad &\text{(Pythagoras)} \\
> &= -R\left(2R\cos\theta\,\mathbf i + 2R\sin\theta\,\mathbf j - \mathbf k\right) \quad &\text{(take out $-R$)} \\
> &= -R\left(2x\,\mathbf i + 2y\,\mathbf j - \mathbf k\right) \quad &\text{($R\cos\theta = x$, $R\sin\theta = y$)} \\
> &= -R\,\mathbf n \quad &\text{(the bracket is the gradient)} \\
> \mathbf t_R\cdot\mathbf t_\theta &= -R\sin\theta\cos\theta + R\sin\theta\cos\theta + 2R\cdot 0 \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= 0 \quad &\text{(the two terms cancel: the tangent vectors are orthogonal here)}
> \end{aligned}$$
>
> $$\boxed{\mathbf t_R = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j + 2R\,\mathbf k,\quad \mathbf t_\theta = -R\sin\theta\,\mathbf i + R\cos\theta\,\mathbf j,\qquad \mathbf n = 2x\,\mathbf i + 2y\,\mathbf j - \mathbf k}$$
>
> **Units:** under the reading of the warning above, $f$ is in $\mathrm{m^2}$ (the hidden coefficient of one length multiplies $z$), so $\mathbf n$ is in $\mathrm m$; $\mathbf t_R$ is dimensionless (a length per length, the $\mathbf k$ component being $2R$ divided by that unit length) and $\mathbf t_\theta$ is in $\mathrm{m/rad}$
> **Meaning:** the cross product of the two tangent vectors is parallel to the gradient, as it must be; here it points the other way, inwards and upwards, because $f$ grows outwards and downwards, away from the axis and towards negative $z$. $\mathbf t_R$ climbs along the meridian with slope $2R$ and $\mathbf t_\theta$ is horizontal, along the parallel; they happen to be orthogonal here (last two rows), but they are not unit vectors. At the vertex, excluded because $z$ must be positive, $\mathbf t_\theta$ would vanish and the parametrization would fail.

## 5. Motion of a particle on a smooth surface

Consider a particle $P$ constrained to move without friction on a given surface, the zero set of $f$ (Eq. 6.5), under an applied force $\mathbf F$ that may depend on the position, the velocity and time (Notes.pdf, Sec. 6.4). The particle can move freely on the surface, which has a tangent plane at each point, so the motion has two degrees of freedom; it cannot move in the direction perpendicular to the surface. The mechanism that compels it to stay on the surface is an additional unknown reaction force $\mathbf N$, acting in the normal direction, which is the reason for its usual name, normal force: its magnitude is as large as necessary to make the motion satisfy the constraint, and it is unknown a priori. Applied forces are known a priori; of a constraint force only the subspace is known, not its components ([Lecture 3, Slide 13]). That a smooth constraint pushes only along the normal is the model of a frictionless contact: it is the definition of smoothness, and Section 8 adds the tangential force of a rough constraint.

![[attachments/EM-T/t3-surface-reaction.svg]]

> [!derivation] The reaction of a smooth surface and the equations to solve
> **Law:** model of a smooth constraint (the reaction lies in the normal subspace); the gradient spans that subspace; Newton's second law; counting of equations and unknowns
> **Source:** Notes.pdf, Eq. 6.11; Notes.pdf, Sec. 6.4; Notes.pdf, Eq. 4.4; [Lecture 3, Slide 13]
>
> The normal subspace of a surface has dimension one and is spanned by $\nabla f$ (Section 4), so one scalar, unknown function of time is enough to describe the reaction: $\lambda$ in the notes, or the component $N_1$ along a chosen normal $\mathbf n$ on the slide.
>
> $$\begin{aligned}
> \mathbf N &\in V_N \quad &\text{(smooth constraint: no tangential component)} \\
> \mathbf N &= \lambda(t)\,\nabla f \quad &\text{($V_N$ is spanned by the gradient; Notes.pdf form)} \\
> \mathbf N &= N_1\,\mathbf n \quad &\text{(the same with any normal vector $\mathbf n$, Slide 13)} \\
> m\,\frac{d^2\mathbf r}{dt^2} &= \mathbf F(\mathbf r, \dot{\mathbf r}, t) + \lambda\,\nabla f \quad &\text{(second law with the reaction, Eq. 4.4)} \\
> f(x, y, z) &= 0 \quad &\text{(the constraint)} \\
> 3 + 1 &= 4 \ \text{equations},\quad x, y, z, \lambda \ \to\ 4 \ \text{unknowns} \quad &\text{(Cartesian formulation, Eq. 6.11)} \\
> 3 \ \text{equations},\quad 2 + 1 &= 3 \ \text{unknowns} \quad &\text{(two generalized coordinates that parametrize the surface and $N_1$, Slide 13)}
> \end{aligned}$$
>
> $$\boxed{m\,\frac{d^2\mathbf r}{dt^2} = \mathbf F + \lambda\,\nabla f,\qquad f(x,y,z) = 0}$$
>
> **Units:** $\mathrm N$ in the second law; $\lambda$ has the units of newtons divided by those of $\nabla f$
> **Meaning:** in either formulation the problem is closed. The constraint equation removes one degree of freedom: locally it can be solved for one coordinate in terms of the other two, for example the height as a function of $x$ and $y$ (Notes.pdf, Sec. 6.4); with coordinates that parametrize the surface it is satisfied identically and only the three components of the second law remain.

### Projection on the tangent and normal directions

The coordinates can be found first if an equal number of equations of motion free of the reaction can be isolated; the remaining equations then give the reaction ([Lecture 3, Slide 14]).

> [!derivation] Equations of motion free of the reaction, and the equation of the reaction
> **Law:** dot product of the second law with the tangent and normal vectors; the gradient is perpendicular to every tangent vector
> **Source:** [Lecture 3, Slide 14]; Notes.pdf, Sec. 7.6; Notes.pdf, Eq. 6.11
>
> $\mathbf t_\alpha$ and $\mathbf t_\beta$ are two independent tangent vectors of the surface at the position of $P$ (Section 4).
>
> $$\begin{aligned}
> m\,\mathbf a_0^P\cdot\mathbf t_\alpha &= \mathbf F\cdot\mathbf t_\alpha + \lambda\,\nabla f\cdot\mathbf t_\alpha \quad &\text{(dot-multiply the second law by $\mathbf t_\alpha$)} \\
> &= \mathbf F\cdot\mathbf t_\alpha \quad &\text{($\nabla f\cdot\mathbf t_\alpha = 0$, Section 4)} \\
> m\,\mathbf a_0^P\cdot\mathbf t_\beta &= \mathbf F\cdot\mathbf t_\beta \quad &\text{(the same with $\mathbf t_\beta$)} \\
> m\,\mathbf a_0^P\cdot\nabla f &= \mathbf F\cdot\nabla f + \lambda\,\nabla f\cdot\nabla f \quad &\text{(dot-multiply by the normal $\nabla f$)} \\
> \lambda &= \frac{\left(m\,\mathbf a_0^P - \mathbf F\right)\cdot\nabla f}{\lvert\nabla f\rvert^2} \quad &\text{(solve for $\lambda$; $\nabla f\cdot\nabla f = \lvert\nabla f\rvert^2$)}
> \end{aligned}$$
>
> $$\boxed{m\,\mathbf a_0^P\cdot\mathbf t_\alpha = \mathbf F\cdot\mathbf t_\alpha,\quad m\,\mathbf a_0^P\cdot\mathbf t_\beta = \mathbf F\cdot\mathbf t_\beta;\qquad \lambda = \frac{\left(m\,\mathbf a_0^P - \mathbf F\right)\cdot\nabla f}{\lvert\nabla f\rvert^2}}$$
>
> **Units:** $\mathrm N$ times the units of each tangent vector in the first two equations
> **Meaning:** the two tangent projections contain only the coordinates and their derivatives: they are the equations of motion, two for two degrees of freedom. Once they are solved, the normal projection gives the reaction. Equivalently, linear combinations of the projections on any three independent directions may be formed until the reaction disappears ([Lecture 3, Slide 14]).

### Work and power of the reaction

> [!derivation] The reaction of a smooth stationary surface does no work
> **Law:** work and power of a force; the reaction is along the gradient; total differential and chain rule; theorem of kinetic energy
> **Source:** Notes.pdf, Eq. 6.12; Notes.pdf, Sec. 6.4; Notes.pdf, Eq. 4.10; Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.31; [Lecture 3, Slide 16]
>
> $\mathbf F$ is the applied force; in the last rows it is assumed conservative, with potential energy $V_0$.
>
> $$\begin{aligned}
> \delta W_0 &= \mathbf N\cdot d\mathbf r \quad &\text{(work in a differential displacement)} \\
> &= \lambda\,\nabla f\cdot d\mathbf r \quad &\text{(the reaction, previous box)} \\
> &= \lambda\left(\frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz\right) \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= \lambda\,df \quad &\text{(total differential of $f$)} \\
> &= 0 \quad &\text{($P$ stays on the zero set of $f$: $df = 0$ along the motion)} \\
> \dot W_0 &= \mathbf N\cdot\mathbf v_0^P \quad &\text{(power, Eq. 4.10)} \\
> &= \lambda\left(\frac{\partial f}{\partial x}\,\dot x + \frac{\partial f}{\partial y}\,\dot y + \frac{\partial f}{\partial z}\,\dot z\right) \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= \lambda\,\frac{d}{dt}f\big(x(t), y(t), z(t)\big) \quad &\text{(chain rule)} \\
> &= 0 \quad &\text{($f$ is zero at every instant)} \\
> \frac{dT_0}{dt} &= \left(\mathbf F + \mathbf N\right)\cdot\mathbf v_0^P \quad &\text{(theorem of kinetic energy, Eq. 4.11)} \\
> &= \mathbf F\cdot\mathbf v_0^P \quad &\text{(the reaction has zero power)} \\
> &= -\nabla V_0\cdot\mathbf v_0^P \quad &\text{(conservative applied force, Eq. 4.20)} \\
> &= -\frac{dV_0}{dt} \quad &\text{(chain rule for $V_0$ along the motion)} \\
> \frac{d}{dt}\left(T_0 + V_0\right) &= 0 \quad &\text{(move the right side over)} \\
> \int_0^t \frac{d}{dt'}\left(T_0 + V_0\right)dt' &= 0 \quad &\text{(integrate the previous row from $0$ to $t$)} \\
> \Big[T_0 + V_0\Big]_0^t &= 0 \quad &\text{(antiderivative of a derivative)} \\
> \big(T_0 + V_0\big)(t) - \big(T_0 + V_0\big)(0) &= 0 \quad &\text{(Barrow's rule: upper limit minus lower limit)} \\
> T_0 + V_0 &= E_0 \quad &\text{($E_0$: the value of $T_0 + V_0$ at $t = 0$, a constant)}
> \end{aligned}$$
>
> $$\boxed{\delta W_0 = \lambda\,df = 0,\qquad \dot W_0 = \mathbf N\cdot\mathbf v_0^P = 0;\qquad \mathbf F = -\nabla V_0 \ \Rightarrow\ T_0 + V_0 = E_0 = \text{const}}$$
>
> **Units:** $\mathrm J$ for the work, $\mathrm W$ for the power
> **Meaning:** $\mathbf N$ does not derive from a potential, yet it never works on the particle: it is always perpendicular to the surface while the velocity is always tangent to it ([Lecture 3, Slide 16]). Its presence therefore does not decide whether the mechanical energy is conserved; that depends only on the applied forces (Notes.pdf, Sec. 6.4).

This conclusion holds only under the assumptions above (Notes.pdf, Sec. 6.4): if the surface changes with time, the velocity can have a component along $\nabla f$ and the reaction may work; if the surface is not smooth, friction dissipates energy while the particle moves against it (Section 8).

> [!derivation] A moving surface: the power of the reaction
> **Law:** the constraint depends explicitly on time; chain rule for a function of the position and of time; the reaction is still along the spatial gradient
> **Source:** Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]; Notes.pdf, Eq. 4.10
>
> The surface is now the zero set of $f(x, y, z, t)$, and $\nabla f$ collects only the derivatives with respect to $x$, $y$, $z$.
>
> $$\begin{aligned}
> f\big(x(t), y(t), z(t), t\big) &= 0 \quad &\text{(for every $t$: $P$ is on the moving surface)} \\
> \frac{\partial f}{\partial x}\,\dot x + \frac{\partial f}{\partial y}\,\dot y + \frac{\partial f}{\partial z}\,\dot z + \frac{\partial f}{\partial t} &= 0 \quad &\text{(chain rule, with the explicit dependence on $t$)} \\
> \nabla f\cdot\mathbf v_0^P &= -\frac{\partial f}{\partial t} \quad &\text{(the first three terms are a dot product)} \\
> \dot W_0 &= \lambda\,\nabla f\cdot\mathbf v_0^P \quad &\text{(power of the reaction)} \\
> &= -\lambda\,\frac{\partial f}{\partial t} \quad &\text{(previous row)}
> \end{aligned}$$
>
> $$\boxed{\dot W_0 = \mathbf N\cdot\mathbf v_0^P = -\lambda\,\frac{\partial f}{\partial t} \ \neq 0 \ \text{in general}}$$
>
> **Units:** $\mathrm W$; $\partial f/\partial t$ has the units of $f$ per second
> **Meaning:** the velocity of the particle is no longer tangent to the instantaneous surface, because the surface itself moves, and the reaction can feed energy into the particle or take it out. A time-dependent constraint adds $t$, or a related variable, as an extra coordinate of the problem ([Lecture 3, Slide 21]).

> [!example] A string collected into a spool ([Lecture 3, Slide 22])
> A heavy particle $P$ of mass $m$ is attached to a massless, inextensible string that is being collected into a spool of negligible radius located at $O$, at a rate $c$ (length per unit time). The particle can only move along the vertical axis. Initially the extended length of string is $\ell_0$. Discuss this constraint.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, origin at the spool $O$, $\mathbf k$ vertical upwards |
> | coordinate | $\zeta$, depth of $P$ below $O$, the length of string extended |
> | rate and initial length | $\dot\zeta = -c$, $\zeta(0) = \ell_0$ |
> | forces | weight $\mathbf F_g = -m g\,\mathbf k$; force of the string $\mathbf F_\tau = F_\tau\,\mathbf k$, with the tension $F_\tau$ unknown |

![[attachments/EM-T/t3-spool.svg]]

> [!derivation] The spool: a time-dependent constraint that works
> **Law:** integration of the prescribed rate with Barrow's rule; definition of velocity and acceleration; second law along $\mathbf k$; power of the string; power of a moving constraint (previous box)
> **Source:** [Lecture 3, Slide 22]; [Lecture 3, Slide 21]; Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.10
>
> $$\begin{aligned}
> \zeta(t) - \zeta(0) &= \int_0^t \dot\zeta\,dt' \quad &\text{(fundamental theorem of calculus)} \\
> &= \int_0^t (-c)\,dt' \quad &\text{(prescribed rate)} \\
> &= \left[-c\,t'\right]_0^t \quad &\text{(antiderivative of a constant)} \\
> &= -c\,t \quad &\text{(Barrow: $-c\,t - (-c\cdot 0)$)} \\
> \zeta(t) &= \ell_0 - c\,t \quad &\text{(initial length)} \\
> \mathbf r_0^P &= -\zeta\,\mathbf k \quad &\text{($P$ is a depth $\zeta$ below $O$ on the vertical axis)} \\
> \mathbf v_0^P &= -\dot\zeta\,\mathbf k \quad &\text{(derivative in $S_0$; $\mathbf k$ is constant)} \\
> &= c\,\mathbf k \quad &\text{($\dot\zeta = -c$)} \\
> \mathbf a_0^P &= \mathbf 0 \quad &\text{(derivative of a constant vector)} \\
> m\,\mathbf a_0^P &= -m g\,\mathbf k + F_\tau\,\mathbf k \quad &\text{(second law, Eq. 4.4)} \\
> F_\tau &= m g \quad &\text{($\mathbf a_0^P = \mathbf 0$; component along $\mathbf k$)} \\
> \dot W_0 &= F_\tau\,\mathbf k\cdot c\,\mathbf k \quad &\text{(power of the string, Eq. 4.10)} \\
> &= F_\tau\,c \quad &\text{($\mathbf k\cdot\mathbf k = 1$)} \\
> &= m g\,c \quad &\text{($F_\tau = m g$)} \\
> f(z, t) &= z + \ell_0 - c\,t \quad &\text{(the constraint as a moving surface: $z = -\zeta$)} \\
> \nabla f &= \mathbf k \quad &\text{(gradient of $f$)} \\
> \lambda &= F_\tau \quad &\text{(the string force is $F_\tau\,\mathbf k = \lambda\,\nabla f$)} \\
> \frac{\partial f}{\partial t} &= -c \quad &\text{(explicit time derivative of $f$)} \\
> -\lambda\,\frac{\partial f}{\partial t} &= F_\tau\,c \quad &\text{(power of a moving constraint, previous box: the same value)}
> \end{aligned}$$
>
> $$\boxed{\zeta = \ell_0 - c\,t,\qquad \mathbf v_0^P = c\,\mathbf k,\qquad F_\tau = m g,\qquad \dot W_0 = m g\,c \neq 0}$$
>
> **Units:** $\zeta$ in $\mathrm m$; $c$ in $\mathrm{m/s}$; $F_\tau$ in $\mathrm N$; $\dot W_0$ in $\mathrm{N\,m/s} = \mathrm W$
> **Meaning:** the motion is fully prescribed by the spool: no coordinate is left free, only time, and the string, a constraint force, raises the particle at constant speed and works on it at the rate $m g\,c$, which is exactly the rate at which the potential energy of the weight grows; the kinetic energy stays constant. A time-dependent constraint can thus work, as the general box predicts with the same value. The horizontal reactions that keep $P$ on the vertical axis are zero here, because no applied force has a horizontal component.

Surface constraints come in two types (Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21]), and the constraints of the course are also classified by whether they can be written with the coordinates only and by their dependence on time ([Lecture 3, Slide 21]):

| Classification | Type | Property | Source |
| :--- | :--- | :--- | :--- |
| dependence on velocities | integrable or holonomic | expressed in terms of the coordinates, for example $x$, $y$, $z$; it reduces the number of coordinates | [Lecture 3, Slide 21] |
| dependence on velocities | non-integrable or non-holonomic | its expression necessarily involves the derivatives of the coordinates and cannot be integrated; it cannot reduce the number of coordinates and its equation must be included in the formulation (second part of the course) | [Lecture 3, Slide 21]; Notes.pdf, Sec. 6.2 |
| time | stationary | does not depend explicitly on time | [Lecture 3, Slide 21] |
| time | time-dependent or rheonomic | may work on the particle; $t$, or a related variable, is an extra coordinate | [Lecture 3, Slide 21] |
| sides | bilateral (equation) | the particle cannot leave the surface on either side; the normal force may point to either side as required | Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21] |
| sides | unilateral (inequality) | the particle can leave the surface on one side; two problems must be solved, with the constraint in effect and without it, and the particle separates when the normal force becomes zero | Notes.pdf, Sec. 6.4; [Lecture 3, Slide 21] |

A simple constraint is an integrable, stationary, bilateral constraint ([Lecture 3, Slide 21]). An airplane rolling on the ground, at the moment it takes off, is the example of a unilateral constraint (Notes.pdf, Sec. 6.4): it can take off into the sky but may not dig into the ground ([Lecture 3, Slide 21]).

> [!example] Lift-off of an airplane ([Lecture 3, Slide 23])
> Consider an ideal airplane on the runway, in a stationary atmosphere. The airplane is heavy and has a mass $m$; it is modelled as a point particle. The lift force has the magnitude given below; there is no drag. At what speed does the airplane lift off the ground?
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, origin on the horizontal runway, $\mathbf i$ along the runway, $\mathbf k$ vertical upwards |
> | lift | $L = \rho_a (v_0^P)^2 S_w C_L/2$, $v_0^P$ the speed; vertical upwards, perpendicular to the runway and to the velocity (direction assumed here; the slide gives the magnitude) |
> | weight | $\mathbf F_g = -m g\,\mathbf k$ |
> | ground | unilateral constraint $z \geq 0$; normal reaction $\mathbf N = N\,\mathbf k$ with $N \geq 0$ (the ground can only push) |

![[attachments/EM-T/t3-airplane-fbd.svg]]

> [!derivation] Lift-off: the normal force of a unilateral constraint vanishes
> **Law:** second law projected on the vertical while the constraint is in effect; separation when the normal force becomes zero
> **Source:** [Lecture 3, Slide 23]; [Lecture 3, Slide 21]; Notes.pdf, Sec. 6.4; Notes.pdf, Eq. 4.4
>
> Whatever accelerates the airplane along the runway (the slide gives no such force; any horizontal force) has no vertical component and does not enter the vertical projection.
>
> $$\begin{aligned}
> z &= 0,\quad \ddot z = 0 \quad &\text{(on the runway: the constraint is in effect)} \\
> m\,\ddot z &= N + \tfrac12\rho_a (v_0^P)^2 S_w C_L - m g \quad &\text{(second law along $\mathbf k$, Eq. 4.4)} \\
> 0 &= N + \tfrac12\rho_a (v_0^P)^2 S_w C_L - m g \quad &\text{($\ddot z = 0$)} \\
> N &= m g - \tfrac12\rho_a (v_0^P)^2 S_w C_L \quad &\text{(solve for $N$)} \\
> N &= 0 \quad &\text{(separation: the ground no longer pushes)} \\
> \tfrac12\rho_a (v_0^P)^2 S_w C_L &= m g \quad &\text{(previous two rows)} \\
> v_0^P &= \sqrt{\frac{2 m g}{\rho_a S_w C_L}} \quad &\text{(solve for the speed; positive root)}
> \end{aligned}$$
>
> $$\boxed{N = m g - \tfrac12\rho_a (v_0^P)^2 S_w C_L \geq 0 \ \text{on the ground},\qquad v_{\mathrm{lift\text{-}off}} = \sqrt{\frac{2 m g}{\rho_a S_w C_L}}}$$
>
> **Units:** $\sqrt{\mathrm{kg\cdot m\,s^{-2}}/(\mathrm{kg\,m^{-3}}\cdot\mathrm{m^2})} = \sqrt{\mathrm{m^2\,s^{-2}}} = \mathrm{m/s}$
> **Meaning:** as the airplane speeds up, the lift takes over more and more of the weight and the normal force decreases; it reaches zero at the lift-off speed. Beyond that speed the formula would give a negative normal force, which the ground cannot exert: the constraint stops being in effect and the airplane is a free particle (the second problem of a unilateral constraint). A heavier airplane, or a smaller wing or lift coefficient, needs a higher lift-off speed.

## 6. Motion of a particle along a smooth curve

Consider now a particle $P$ constrained to move without friction along a curve given implicitly as the intersection of the zero sets of $f$ and $h$ (Eq. 6.7), under an applied force $\mathbf F$ that may depend on the position, the velocity and time (Notes.pdf, Sec. 6.5). The normal force that compels the particle to stay on the curve can now have two components, one along the normal vector of each surface that defines the curve; the analysis is otherwise very similar to that of a surface.

> [!derivation] The reaction of a smooth curve and the equations to solve
> **Law:** the reaction lies in the normal plane of the curve, spanned by the two gradients; Newton's second law; counting of equations and unknowns; power of the reaction
> **Source:** Notes.pdf, Eq. 6.13; Notes.pdf, Sec. 6.5; Notes.pdf, Eq. 4.4; [Lecture 3, Slide 13]
>
> $$\begin{aligned}
> \mathbf N &= \lambda_1(t)\,\nabla f + \lambda_2(t)\,\nabla h \quad &\text{($V_N$ is spanned by the two gradients, Section 4)} \\
> \mathbf N &= N_1\,\mathbf n_f + N_2\,\mathbf n_h \quad &\text{(the same with the normals of Slide 13)} \\
> m\,\frac{d^2\mathbf r}{dt^2} &= \mathbf F(\mathbf r, \dot{\mathbf r}, t) + \lambda_1\,\nabla f + \lambda_2\,\nabla h \quad &\text{(second law with the reaction, Eq. 4.4)} \\
> f(x, y, z) &= 0,\quad h(x, y, z) = 0 \quad &\text{(the two equations of the curve)} \\
> 3 + 2 &= 5 \ \text{equations},\quad x, y, z, \lambda_1, \lambda_2 \ \to\ 5 \ \text{unknowns} \quad &\text{(Cartesian formulation, Eq. 6.13)} \\
> 3 \ \text{equations},\quad 1 + 2 &= 3 \ \text{unknowns} \quad &\text{(one generalized coordinate along the curve and $N_1$, $N_2$, Slide 13)} \\
> \mathbf N\cdot\mathbf v_0^P &= \lambda_1\,\frac{df}{dt} + \lambda_2\,\frac{dh}{dt} \quad &\text{(power; chain rule for each function, as in Section 5)} \\
> &= 0 \quad &\text{(both functions stay zero on a stationary curve)}
> \end{aligned}$$
>
> $$\boxed{m\,\frac{d^2\mathbf r}{dt^2} = \mathbf F + \lambda_1\,\nabla f + \lambda_2\,\nabla h,\qquad f = 0,\quad h = 0;\qquad \mathbf N\cdot\mathbf v_0^P = 0}$$
>
> **Units:** $\mathrm N$ in the second law; $\mathrm W$ for the power
> **Meaning:** the problem is closed in both formulations. As for a surface, the normal reaction of a stationary, smooth curve does no work, and the discussion of the conservation of mechanical energy is the same (Notes.pdf, Sec. 6.5). The equation of motion is the projection on the tangent $\mathbf t$; the projections on $\mathbf n_f$ and $\mathbf n_h$ give the two reaction components ([Lecture 3, Slide 14]).

When studying the motion along curves it is sometimes useful to use path variables: the arc length $s$ along the curve and its intrinsic basis (Notes.pdf, Sec. 6.5).

![[attachments/EM-T/t3-curve-reaction.svg]]

> [!derivation] Newton's second law in path variables
> **Law:** intrinsic acceleration; the trajectory is the curve, so its intrinsic basis separates $V_T$ from $V_N$; projection of the second law on the intrinsic basis
> **Source:** Notes.pdf, Eq. 6.14; Notes.pdf, Eq. 6.15; Notes.pdf, Eq. 6.16; Notes.pdf, Eq. 6.17; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19; Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 2.13
>
> The particle moves along the curve, so the curve is its trajectory: $\mathbf e_t$ spans the tangent line $V_T$, and $\mathbf e_n$ and $\mathbf e_b$, perpendicular to $\mathbf e_t$ and to each other, span the normal plane $V_N$.
>
> $$\begin{aligned}
> \mathbf a_0^P &= \ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n \quad &\text{(intrinsic acceleration, Eq. 2.17; Eq. 6.14)} \\
> \mathbf F &= F_t\,\mathbf e_t + F_n\,\mathbf e_n + F_b\,\mathbf e_b \quad &\text{(applied force in the intrinsic basis, Eq. 6.15)} \\
> \mathbf N &= N_n\,\mathbf e_n + N_b\,\mathbf e_b \quad &\text{($\mathbf N \in V_N$: no $\mathbf e_t$ component, Eq. 6.16)} \\
> m\,\ddot s\,\mathbf e_t + m\,\frac{\dot s^2}{\rho}\,\mathbf e_n &= F_t\,\mathbf e_t + \left(F_n + N_n\right)\mathbf e_n + \left(F_b + N_b\right)\mathbf e_b \quad &\text{(second law, grouped by unit vector)} \\
> \mathbf e_t:\quad F_t &= m\,\ddot s \quad &\text{(dot-multiply by $\mathbf e_t$, Eq. 6.17)} \\
> \mathbf e_n:\quad F_n + N_n &= m\,\frac{\dot s^2}{\rho} \quad &\text{(dot-multiply by $\mathbf e_n$, Eq. 6.18)} \\
> \mathbf e_b:\quad F_b + N_b &= 0 \quad &\text{(dot-multiply by $\mathbf e_b$, Eq. 6.19)}
> \end{aligned}$$
>
> $$\boxed{F_t = m\,\ddot s,\qquad F_n + N_n = m\,\frac{\dot s^2}{\rho},\qquad F_b + N_b = 0}$$
>
> **Units:** $\mathrm N$ in every term ($\dot s^2/\rho$ in $\mathrm{m^2\,s^{-2}}/\mathrm m = \mathrm{m\,s^{-2}}$)
> **Meaning:** the tangential equation is the equation of motion, free of the reaction; the normal and binormal equations give the two reaction components afterwards. The normal reaction supplies, together with the normal applied force, the centripetal force that bends the path, and the binormal reaction cancels whatever applied force pushes the particle out of the osculating plane.

> [!example] A heavy particle on a vertical circle ([Lecture 3, Slide 15])
> A heavy particle $P$ is constrained to move along a vertical circle of radius $a$. Get the equation of motion for the angle $\theta$ first, and then the equation that yields the magnitude of the constraint force $\mathbf N$. (The wire is taken smooth and fixed: an assumption of this note, not written on the slide.)
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial, origin at the centre $O$ of the circle; $\mathbf i$ horizontal to the right, $\mathbf j$ vertical upwards, $\mathbf k$ out of the paper |
> | curve | $f = x^2 + y^2 - a^2 = 0$ (circular cylinder of axis $Oz$), $h = z = 0$ (vertical plane $Oxy$) |
> | coordinate | $\theta$, from $Ox$ to $OP$, counterclockwise; one degree of freedom |
> | gravity | $\mathbf g = -g\,\mathbf j$; weight $\mathbf F_g = -m g\,\mathbf j$ |

![[attachments/EM-T/t3-vertical-circle.svg]]

### Basis, change of basis and kinematics

![[attachments/EM-T/t3-vertical-circle-basis.svg]]

> [!derivation] Polar basis of the particle and its change of basis matrix
> **Law:** right triangles of the unit vectors; right-hand rule about $\mathbf k$; change of basis matrix with the local unit vectors as columns; determinant and orthogonality
> **Source:** Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; [Lecture 3, Slide 15]
>
> View along $\mathbf k$, which points out of the paper (⊙). $\mathbf e_R$ points from $O$ to $P$: in the right triangle with unit hypotenuse $\mathbf e_R$ and the angle $\theta$ at $O$ between $\mathbf i$ and $\mathbf e_R$, the leg along $\mathbf i$ is adjacent to $\theta$, $\cos\theta$, and the leg along $\mathbf j$ is opposite, $\sin\theta$. $\mathbf e_\theta$ is $\mathbf e_R$ turned a quarter turn counterclockwise, the sense in which $\theta$ grows by the right-hand rule about $\mathbf k$; the same angle $\theta$ lies between $\mathbf j$ and $\mathbf e_\theta$, so the leg along $\mathbf j$ is adjacent, $\cos\theta$, and the leg along $\mathbf i$ is opposite, $\sin\theta$, but it points towards $-\mathbf i$: for $\theta$ between $0$ and $\pi/2$, turning $\mathbf e_R$ counterclockwise past $\mathbf j$ takes $\mathbf e_\theta$ to the left of the vertical, which is the minus sign of its $\mathbf i$ component.
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(legs of the first triangle, Eq. 2.24)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(legs of the second triangle, Eq. 2.24)} \\
> [{}_0R_1] &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf k$ in $\mathcal B_0$, Eq. 1.13; a simple rotation about $\mathbf k$, Eq. 1.20)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta\cos\theta - (-\sin\theta)\sin\theta\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2\theta + \sin^2\theta \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos\theta\cos\theta + (-\sin\theta)(-\sin\theta) + 0\cdot 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta + (-\sin\theta)\cos\theta + 0\cdot 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_R = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j,\quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j;\qquad [{}_0R_1] = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix},\ \ \det = 1}$$
>
> **Units:** dimensionless
> **Meaning:** $\mathcal B_1$, made of $\mathbf e_R$, $\mathbf e_\theta$ and $\mathbf k$, is the basis of a frame $S_1$ that turns with the radius $OP$; the other entries of the product follow the same way ($(2,2)$ by Pythagoras, the third row and column trivially), so the basis is orthonormal, and the cross product of $\mathbf e_R$ and $\mathbf e_\theta$ is $\mathbf k$ (Topic 1), so it is right-handed. When $\theta$ is zero it coincides with $\mathcal B_0$.

> [!derivation] Time derivatives of the polar unit vectors
> **Law:** chain rule through $\theta(t)$; check with the angular velocity of $S_1$
> **Source:** Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.32
>
> The derivatives are taken in $S_0$, where $\mathbf i$, $\mathbf j$, $\mathbf k$ are constant.
>
> $$\begin{aligned}
> \frac{d\mathbf e_R}{dt} &= \frac{d\mathbf e_R}{d\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= \left(-\sin\theta\,\mathbf i + \cos\theta\,\mathbf j\right)\dot\theta \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(previous box)} \\
> \frac{d\mathbf e_\theta}{dt} &= \frac{d\mathbf e_\theta}{d\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= \left(-\cos\theta\,\mathbf i - \sin\theta\,\mathbf j\right)\dot\theta \quad &\text{(derivatives of $-\sin\theta$ and $\cos\theta$)} \\
> &= -\dot\theta\,\mathbf e_R \quad &\text{(previous box)} \\
> \dot\theta\,\mathbf k\times\mathbf e_R &= \dot\theta\cos\theta\,\mathbf k\times\mathbf i + \dot\theta\sin\theta\,\mathbf k\times\mathbf j \quad &\text{(distribute)} \\
> &= \dot\theta\cos\theta\,\mathbf j - \dot\theta\sin\theta\,\mathbf i \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(equal to the first result: Eq. 1.62 with $\boldsymbol\omega_{10} = \dot\theta\,\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_R}{dt} = \dot\theta\,\mathbf e_\theta,\qquad \frac{d\mathbf e_\theta}{dt} = -\dot\theta\,\mathbf e_R,\qquad \boldsymbol\omega_{10} = \dot\theta\,\mathbf k}$$
>
> **Units:** $\mathrm{rad/s}$ in every term
> **Meaning:** the basis turns with the radius about $\mathbf k$ at the rate of change of $\theta$; each unit vector changes in the direction perpendicular to itself.

> [!derivation] Position, velocity and acceleration of the particle
> **Law:** position along the radius; definition of velocity and acceleration; product rule; the radius is constant
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 1.64; [Lecture 3, Slide 15]
>
> $$\begin{aligned}
> \mathbf r_0^P &= a\,\mathbf e_R \quad &\text{($P$ is at distance $a$ from $O$ along the radius)} \\
> \mathbf v_0^P &= \dot a\,\mathbf e_R + a\,\frac{d\mathbf e_R}{dt} \quad &\text{(Eq. 2.3; product rule, Eq. 1.64)} \\
> &= a\,\frac{d\mathbf e_R}{dt} \quad &\text{(the wire is fixed: $\dot a = 0$)} \\
> &= a\dot\theta\,\mathbf e_\theta \quad &\text{(previous box)} \\
> \mathbf a_0^P &= a\ddot\theta\,\mathbf e_\theta + a\dot\theta\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(Eq. 2.4; product rule, $a$ constant)} \\
> &= a\ddot\theta\,\mathbf e_\theta - a\dot\theta^2\,\mathbf e_R \quad &\text{(previous box)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf e_R,\qquad \mathbf v_0^P = a\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_0^P = -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta}$$
>
> **Units:** $\mathrm m$; $\mathrm{m/s}$; $\mathrm{m/s^2}$ for both terms of the acceleration
> **Meaning:** the velocity is tangent to the circle, so it lies in $V_T$ as it must; the acceleration has a part towards the centre, which turns the velocity, and a tangential part, which changes the speed.

### Forces, equations of motion and reaction

![[attachments/EM-T/t3-vertical-circle-fbd.svg]]

> [!derivation] The forces in the polar basis
> **Law:** the gradients of the two surfaces span the normal plane of the circle; change of basis with the transpose of the matrix
> **Source:** Notes.pdf, Eq. 6.13; Notes.pdf, Eq. 6.9; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.14; [Lecture 3, Slide 13]
>
> $$\begin{aligned}
> \nabla f &= 2x\,\mathbf i + 2y\,\mathbf j \quad &\text{(partial derivatives of $x^2 + y^2 - a^2$)} \\
> &= 2a\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) \quad &\text{(on the circle: $x = a\cos\theta$, $y = a\sin\theta$)} \\
> &= 2a\,\mathbf e_R \quad &\text{(polar basis)} \\
> \nabla h &= \mathbf k \quad &\text{(partial derivatives of $z$)} \\
> \mathbf N &= 2a\lambda_1\,\mathbf e_R + \lambda_2\,\mathbf k \quad &\text{(Eq. 6.13)} \\
> &= N_R\,\mathbf e_R + N_z\,\mathbf k \quad &\text{(names of the two unknown components)} \\
> [\mathbf F_g]_1 &= [{}_0R_1]^T\,[\mathbf F_g]_0 \quad &\text{(inverse change of basis: the transpose, Eqs. 1.12 and 1.14)} \\
> &= \begin{pmatrix} \cos\theta\cdot 0 + \sin\theta\,(-m g) + 0\cdot 0 \cr -\sin\theta\cdot 0 + \cos\theta\,(-m g) + 0\cdot 0 \cr 0\cdot 0 + 0\cdot(-m g) + 1\cdot 0 \end{pmatrix} \quad &\text{(rows of the transpose times the column $(0, -mg, 0)$)} \\
> &= \begin{pmatrix} -m g\sin\theta \cr -m g\cos\theta \cr 0 \end{pmatrix} \quad &\text{(arithmetic)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_g = -m g\sin\theta\,\mathbf e_R - m g\cos\theta\,\mathbf e_\theta,\qquad \mathbf N = N_R\,\mathbf e_R + N_z\,\mathbf k}$$
>
> **Units:** $\mathrm N$
> **Meaning:** the weight has a radial component, minus the weight times the sine of $\theta$, which points inwards in the upper half of the circle, and a tangential component, minus the weight times the cosine of $\theta$, which pulls the particle towards the lowest point, where $\theta$ is minus a right angle. The reaction has no $\mathbf e_\theta$ component, because the wire is smooth.

> [!derivation] Equation of motion and reaction of the particle on the vertical circle
> **Law:** Newton's second law projected on $\mathbf e_\theta$ (tangent), $\mathbf e_R$ and $\mathbf k$ (normals); counting of equations and unknowns
> **Source:** [Lecture 3, Slide 15]; [Lecture 3, Slide 14]; Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 6.13
>
> $$\begin{aligned}
> m\left(-a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta\right) &= -m g\sin\theta\,\mathbf e_R - m g\cos\theta\,\mathbf e_\theta + N_R\,\mathbf e_R + N_z\,\mathbf k \quad &\text{(second law: acceleration and forces of the boxes above)} \\
> \mathbf e_\theta:\quad m a\ddot\theta &= -m g\cos\theta \quad &\text{(dot-multiply by the tangent: no reaction)} \\
> m a\ddot\theta + m g\cos\theta &= 0 \quad &\text{(move the right side over)} \\
> \ddot\theta + \frac{g}{a}\cos\theta &= 0 \quad &\text{(divide by $m a$)} \\
> \mathbf e_R:\quad -m a\dot\theta^2 &= -m g\sin\theta + N_R \quad &\text{(dot-multiply by $\mathbf e_R$)} \\
> N_R &= m g\sin\theta - m a\dot\theta^2 \quad &\text{(solve for $N_R$)} \\
> \mathbf k:\quad 0 &= N_z \quad &\text{(dot-multiply by $\mathbf k$)} \\
> 3 \ \text{equations},\quad \theta, N_R, N_z &\ \to\ 3 \ \text{unknowns} \quad &\text{(the problem is closed)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \frac{g}{a}\cos\theta = 0,\qquad N_R = m g\sin\theta - m a\dot\theta^2,\qquad N_z = 0}$$
>
> **Units:** $\mathrm{rad/s^2}$ in the equation of motion ($g/a$ in $\mathrm{s^{-2}}$); $\mathrm N$ in the reaction
> **Meaning:** the tangential projection is the equation of motion for $\theta$ alone, as asked first; the radial projection then gives the reaction, as asked second. At the lowest point, where $\theta$ is minus a right angle and the sine is minus one, $N_R$ is minus the weight minus the mass times $a$ times the square of the rate of $\theta$; since $\mathbf e_R$ points down there, the wire pushes the particle upwards with the weight plus the force needed to turn the velocity. The wire does not push out of the plane, since no applied force does.

> [!derivation] First integral and the reaction as a function of the position
> **Law:** multiplication by $\dot\theta$; chain rule; integration in time with Barrow's rule; conservation of mechanical energy (the reaction does no work)
> **Source:** [Lecture 3, Slide 15]; [Lecture 3, Slide 16]; Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.31; Notes.pdf, Sec. 6.5
>
> $$\begin{aligned}
> \dot\theta\,\ddot\theta + \frac{g}{a}\cos\theta\,\dot\theta &= 0 \quad &\text{(multiply the equation of motion by $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\,\dot\theta^2\right) &= \dot\theta\,\ddot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\frac{g}{a}\sin\theta\right) &= \frac{g}{a}\cos\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta\right) &= 0 \quad &\text{(the first row is the sum of the two derivatives)} \\
> \int_0^t \frac{d}{dt'}\left(\tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta\right)dt' &= 0 \quad &\text{(integrate the previous row from $0$ to $t$)} \\
> \left[\tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta\right]_0^t &= 0 \quad &\text{(antiderivative of a derivative)} \\
> \tfrac12\,\dot\theta(t)^2 + \frac{g}{a}\sin\theta(t) - \tfrac12\,\dot\theta(0)^2 - \frac{g}{a}\sin\theta(0) &= 0 \quad &\text{(Barrow's rule: $F(t) - F(0)$)} \\
> \tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta &= K \quad &\text{($K = \tfrac12\,\dot\theta(0)^2 + (g/a)\sin\theta(0)$, a constant)} \\
> T_0 &= \tfrac12\,m\,\mathbf v_0^P\cdot\mathbf v_0^P \quad &\text{(kinetic energy, Eq. 4.11)} \\
> &= \tfrac12\,m\,a^2\dot\theta^2 \quad &\text{($\mathbf v_0^P = a\dot\theta\,\mathbf e_\theta$, $\mathbf e_\theta\cdot\mathbf e_\theta = 1$)} \\
> V_0 &= -\int_{\mathbf 0}^{\mathbf r_0^P}\left(-m g\,\mathbf j\right)\cdot d\mathbf r \quad &\text{(potential energy of the weight, Eq. 4.14, reference point $O$)} \\
> &= m g\int_{\mathbf 0}^{\mathbf r_0^P}\mathbf j\cdot d\mathbf r \quad &\text{(take out the constant factor; the two minus signs cancel)} \\
> &= m g\int_0^y dy' \quad &\text{($\mathbf j\cdot d\mathbf r = dy'$, the vertical component of the step)} \\
> &= m g\Big[y'\Big]_0^y \quad &\text{(antiderivative of a constant)} \\
> &= m g\,y \quad &\text{(Barrow's rule: $y - 0$)} \\
> -\nabla V_0 &= -m g\,\mathbf j \quad &\text{(check with Eq. 4.20: the weight is recovered)} \\
> V_0 &= m g\,a\sin\theta \quad &\text{($y = a\sin\theta$ on the circle)} \\
> T_0 + V_0 &= \tfrac12\,m\,a^2\dot\theta^2 + m g\,a\sin\theta \quad &\text{(add the two energies)} \\
> &= m a^2\left(\tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta\right) \quad &\text{(factor $m a^2$)} \\
> &= m a^2 K \quad &\text{(the first integral)} \\
> a\dot\theta^2 &= 2aK - 2g\sin\theta \quad &\text{(first integral times $2a$)} \\
> N_R &= m g\sin\theta - m\left(2aK - 2g\sin\theta\right) \quad &\text{(substitute into the reaction of the previous box)} \\
> &= 3 m g\sin\theta - 2 m a K \quad &\text{(group the sine terms)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12\,\dot\theta^2 + \frac{g}{a}\sin\theta = K,\qquad E_0 = m a^2 K,\qquad N_R = 3 m g\sin\theta - 2 m a K}$$
>
> **Units:** $\mathrm{s^{-2}}$ in the first integral and in $K$; $\mathrm J$ for $E_0$; $\mathrm N$ for $N_R$ ($m a K$ in $\mathrm{kg\,m\,s^{-2}}$)
> **Meaning:** the first integral is the conservation of mechanical energy divided by $m a^2$: the reaction does no work and the weight is conservative (Section 5). With it the reaction is known at every position, without integrating the motion: it is most negative, the wire pushing hardest towards the centre, at the lowest point, and it changes sign where the sine equals $2aK/(3g)$. The constant $K$ is fixed by the initial position and velocity.

> [!derivation] The same equations from the path variables
> **Law:** arc length along the circle; intrinsic basis from the derivative of the tangent; Eqs. 6.17 to 6.19
> **Source:** Notes.pdf, Eq. 6.17; Notes.pdf, Eq. 6.18; Notes.pdf, Eq. 6.19; Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.11; Notes.pdf, Eq. 2.12; Notes.pdf, Eq. 2.13
>
> Here $s$ is a signed arc coordinate, measured from the point of $Ox$ and growing with $\theta$; its rate is negative when the particle moves clockwise. Notes.pdf, Eq. 2.16 (p. 30) writes the rate of $s$ for the speed instead, which is never negative; the rows below use the signed coordinate.
>
> $$\begin{aligned}
> s &= a\,\theta \quad &\text{(arc of a circle of radius $a$)} \\
> \dot s &= a\dot\theta \quad &\text{(time derivative; $a$ constant)} \\
> \ddot s &= a\ddot\theta \quad &\text{(time derivative again)} \\
> \mathbf e_t &= \mathbf e_\theta \quad &\text{($\mathbf v_0^P = \dot s\,\mathbf e_t$, Eq. 2.16, and $\mathbf v_0^P = a\dot\theta\,\mathbf e_\theta$)} \\
> \frac{d\mathbf e_t}{ds} &= \frac{d\mathbf e_\theta}{d\theta}\,\frac{d\theta}{ds} \quad &\text{(chain rule)} \\
> &= -\frac{1}{a}\,\mathbf e_R \quad &\text{($d\mathbf e_\theta/d\theta = -\mathbf e_R$, $d\theta/ds = 1/a$)} \\
> \rho &= a,\quad \mathbf e_n = -\mathbf e_R \quad &\text{(magnitude $1/\rho$, Eq. 2.12, and direction, Eq. 2.11, of the derivative)} \\
> \mathbf e_b &= \mathbf e_t\times\mathbf e_n \quad &\text{(right-handed intrinsic basis, Eq. 2.13)} \\
> &= -\mathbf e_\theta\times\mathbf e_R \quad &\text{(substitute $\mathbf e_t$ and $\mathbf e_n$)} \\
> &= \mathbf k \quad &\text{($\mathbf e_\theta\times\mathbf e_R = -\mathbf k$)} \\
> F_t &= \mathbf F_g\cdot\mathbf e_\theta \quad &\text{(tangential component of the weight)} \\
> &= -m g\cos\theta \quad &\text{(forces box)} \\
> m a\ddot\theta &= -m g\cos\theta \quad &\text{(Eq. 6.17: the equation of motion again)} \\
> F_n &= \mathbf F_g\cdot(-\mathbf e_R) \quad &\text{(normal component of the weight)} \\
> &= m g\sin\theta \quad &\text{(forces box)} \\
> N_n &= \mathbf N\cdot\mathbf e_n = -N_R \quad &\text{(normal component of the reaction: $\mathbf e_n = -\mathbf e_R$)} \\
> m a\dot\theta^2 &= m g\sin\theta - N_R \quad &\text{(Eq. 6.18 with $\dot s^2/\rho = a\dot\theta^2$: the $\mathbf e_R$ equation again)} \\
> 0 &= F_b + N_b \quad &\text{(Eq. 6.19)} \\
> &= N_z \quad &\text{($\mathbf F_g$ has no $\mathbf k$ component; $N_b = \mathbf N\cdot\mathbf k = N_z$)}
> \end{aligned}$$
>
> $$\boxed{\rho = a,\quad \mathbf e_t = \mathbf e_\theta,\quad \mathbf e_n = -\mathbf e_R,\quad \mathbf e_b = \mathbf k:\qquad \text{Eqs. 6.17 to 6.19 reproduce the three projections}}$$
>
> **Units:** $\mathrm N$ in each projection
> **Meaning:** the path variables give the same three scalar equations, because the polar basis of this problem is the intrinsic basis up to the sign of $\mathbf e_R$. With the signed coordinate $s$ the result holds for either sense of motion. With the convention of the notes, where the rate of the arc length is the speed, a clockwise motion has $\mathbf e_t$ along the motion, the opposite of $\mathbf e_\theta$, and $\mathbf e_b$ the opposite of $\mathbf k$, while $\mathbf e_n$, towards the centre of curvature, is the opposite of $\mathbf e_R$ either way; the three projections are then the same scalar equations.

## 7. Constraints affecting two or more particles

In systems of particles there can be constraints that restrict the combined motion of two or more particles, for example two particles connected by a massless, inextensible string passing over a set of pulleys ([Lecture 3, Slide 17]). The kinematics is treated as before: the positions of all particles are described with a minimal set of coordinates, so that the constraint equation is already dealt with. The constraint forces on the particles concerned are related: in the string example the tension has the same magnitude at both particles. The constraint force may work on each particle; but if the constraint does not depend explicitly on time, the total mechanical energy of the system is conserved: the work done on the particle at one end of the string is equal and opposite to the work done on the other, and the constraint only transfers mechanical energy between them ([Lecture 3, Slide 17]). The example below, built for this note on the configuration of the slide, shows each of these statements.

> [!example] Two particles hanging from a string over two pulleys (built for this note on [Lecture 3, Slide 17])
> Two heavy particles, $P$ of mass $m$ and $P'$ of mass $m'$, hang from the two ends of a massless, inextensible string of length $\ell_s$ that passes over two fixed pulleys at the same height, of negligible radius and mass and without friction, a distance $\ell_c$ apart. Each particle moves along the vertical line below its pulley (an assumption of the example). Find the equation of motion, the tension and the work of the string on each particle.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial, origin $O$ at the left pulley; $\mathbf i$ horizontal towards the right pulley, $\mathbf j$ vertical upwards |
> | coordinates | depths $\eta$ of $P$ below the left pulley and $\eta'$ of $P'$ below the right pulley |
> | string | $\eta + \ell_c + \eta' = \ell_s$ (inextensible) |
> | forces | weights $-m g\,\mathbf j$ and $-m' g\,\mathbf j$; force of the string $F_\tau\,\mathbf j$ on each particle, with the same tension $F_\tau$ |

![[attachments/EM-T/t3-two-particles.svg]]

> [!derivation] Kinematics of the two particles with one coordinate
> **Law:** constant length of the string; positions in $S_0$; time derivatives in $S_0$
> **Source:** [Lecture 3, Slide 17]; Notes.pdf, Sec. 2.7; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4
>
> $$\begin{aligned}
> \eta' &= \ell_s - \ell_c - \eta \quad &\text{(string constraint solved for $\eta'$)} \\
> \dot \eta' &= -\dot \eta \quad &\text{(time derivative; $\ell_s$ and $\ell_c$ constant)} \\
> \ddot \eta' &= -\ddot \eta \quad &\text{(time derivative again)} \\
> \mathbf r_0^P &= -\eta\,\mathbf j \quad &\text{($P$ is a depth $\eta$ below $O$)} \\
> \mathbf r_0^{P'} &= \ell_c\,\mathbf i - \eta'\,\mathbf j \quad &\text{($P'$ is a depth $\eta'$ below the right pulley)} \\
> \mathbf v_0^P &= -\dot \eta\,\mathbf j \quad &\text{(derivative in $S_0$; $\mathbf j$ constant)} \\
> \mathbf a_0^P &= -\ddot \eta\,\mathbf j \quad &\text{(derivative again)} \\
> \mathbf v_0^{P'} &= -\dot \eta'\,\mathbf j \quad &\text{(derivative in $S_0$; $\ell_c\,\mathbf i$ constant)} \\
> &= \dot \eta\,\mathbf j \quad &\text{($\dot \eta' = -\dot \eta$)} \\
> \mathbf a_0^{P'} &= -\ddot \eta'\,\mathbf j \quad &\text{(derivative again)} \\
> &= \ddot \eta\,\mathbf j \quad &\text{($\ddot \eta' = -\ddot \eta$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = -\dot \eta\,\mathbf j,\quad \mathbf a_0^P = -\ddot \eta\,\mathbf j;\qquad \mathbf v_0^{P'} = \dot \eta\,\mathbf j,\quad \mathbf a_0^{P'} = \ddot \eta\,\mathbf j}$$
>
> **Units:** $\mathrm{m/s}$ and $\mathrm{m/s^2}$
> **Meaning:** one coordinate, $\eta$, describes both particles: two particles on their vertical lines, with one constraint, have one degree of freedom, and when $P$ goes down $P'$ goes up at the same speed.

> [!derivation] Equations of motion and tension of the two particles
> **Law:** Newton's second law for each particle along $\mathbf j$; counting of equations and unknowns
> **Source:** [Lecture 3, Slide 17]; Notes.pdf, Eq. 4.4; Notes.pdf, Sec. 7.6
>
> $$\begin{aligned}
> m\left(-\ddot \eta\right) &= -m g + F_\tau \quad &\text{(second law for $P$, component along $\mathbf j$)} \\
> m'\,\ddot \eta &= -m' g + F_\tau \quad &\text{(second law for $P'$, component along $\mathbf j$)} \\
> 2 \ \text{equations},\quad \eta, F_\tau &\ \to\ 2 \ \text{unknowns} \quad &\text{($\eta'$ already eliminated by the constraint)} \\
> -\left(m + m'\right)\ddot \eta &= -m g + m' g \quad &\text{(subtract the second equation from the first: $F_\tau$ disappears)} \\
> \ddot \eta &= \frac{m - m'}{m + m'}\,g \quad &\text{(divide by $-(m + m')$)} \\
> F_\tau &= m g - m\,\ddot \eta \quad &\text{(first equation solved for $F_\tau$)} \\
> &= m g - m g\,\frac{m - m'}{m + m'} \quad &\text{(substitute $\ddot \eta$)} \\
> &= m g\,\frac{\left(m + m'\right) - \left(m - m'\right)}{m + m'} \quad &\text{(common denominator)} \\
> &= \frac{2 m m'}{m + m'}\,g \quad &\text{(simplify the numerator)} \\
> &= m g\,\frac{2 m'}{m + m'} \quad &\text{(the weight of $P$ times a factor below one when $m > m'$)} \\
> &= m' g\,\frac{2 m}{m + m'} \quad &\text{(the weight of $P'$ times a factor above one when $m > m'$)}
> \end{aligned}$$
>
> $$\boxed{\ddot \eta = \frac{m - m'}{m + m'}\,g,\qquad F_\tau = \frac{2 m m'}{m + m'}\,g}$$
>
> **Units:** $\mathrm{m/s^2}$ and $\mathrm N$
> **Meaning:** the heavier particle goes down with a constant acceleration smaller than $g$; with equal masses there is no acceleration and the tension is the weight of each. The tension lies between the two weights: when $m$ is the heavier mass it is the weight of $P$ reduced by a factor smaller than one, and also the weight of $P'$ increased by a factor larger than one (last two rows).

> [!derivation] Work of the string on each particle and the energy of the system
> **Law:** power of a force; sum of the powers on the system; theorem of kinetic energy for each particle; chain rule
> **Source:** [Lecture 3, Slide 17]; Notes.pdf, Eq. 4.10; Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.14
>
> $$\begin{aligned}
> \dot W_0^{(P)} &= F_\tau\,\mathbf j\cdot\left(-\dot \eta\,\mathbf j\right) \quad &\text{(power of the string on $P$, Eq. 4.10)} \\
> &= -F_\tau\,\dot \eta \quad &\text{($\mathbf j\cdot\mathbf j = 1$)} \\
> \dot W_0^{(P')} &= F_\tau\,\mathbf j\cdot\dot \eta\,\mathbf j \quad &\text{(power of the string on $P'$)} \\
> &= F_\tau\,\dot \eta \quad &\text{($\mathbf j\cdot\mathbf j = 1$)} \\
> \dot W_0^{(P)} + \dot W_0^{(P')} &= 0 \quad &\text{(the two powers cancel at every instant)} \\
> \frac{d}{dt}\left(\tfrac12\left(m + m'\right)\dot \eta^2\right) &= \left(m + m'\right)\dot \eta\,\ddot \eta \quad &\text{(chain rule; total kinetic energy, both speeds equal to $\lvert\dot \eta\rvert$)} \\
> &= \left(m - m'\right)g\,\dot \eta \quad &\text{(equation of motion of the previous box)} \\
> &= \frac{d}{dt}\Big(\left(m - m'\right)g\,\eta\Big) \quad &\text{(chain rule backwards)} \\
> \frac{d}{dt}\left(\tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta\right) &= 0 \quad &\text{(move the right side over)} \\
> \int_0^t \frac{d}{dt'}\left(\tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta\right)dt' &= 0 \quad &\text{(integrate the previous row from $0$ to $t$)} \\
> \Big[\tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta\Big]_0^t &= 0 \quad &\text{(antiderivative of a derivative)} \\
> \tfrac12\left(m + m'\right)\dot \eta(t)^2 - \left(m - m'\right)g\,\eta(t) - \tfrac12\left(m + m'\right)\dot \eta(0)^2 + \left(m - m'\right)g\,\eta(0) &= 0 \quad &\text{(Barrow's rule: $F(t) - F(0)$)} \\
> \tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta &= \tfrac12\left(m + m'\right)\dot \eta(0)^2 - \left(m - m'\right)g\,\eta(0) \quad &\text{(the value at $t = 0$, a constant)} \\
> V_0 &= -m g\,\eta - m' g\,\eta' \quad &\text{(potential energy $m g y$ of each weight, as in Section 6, with heights $-\eta$ and $-\eta'$ below the pulleys)} \\
> &= -m g\,\eta - m' g\left(\ell_s - \ell_c - \eta\right) \quad &\text{(string constraint for $\eta'$)} \\
> &= -\left(m - m'\right)g\,\eta - m' g\left(\ell_s - \ell_c\right) \quad &\text{(group the terms in $\eta$)} \\
> T_0 + V_0 &= \tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta - m' g\left(\ell_s - \ell_c\right) \quad &\text{(add the kinetic energy of both particles)}
> \end{aligned}$$
>
> $$\boxed{\dot W_0^{(P)} = -F_\tau\,\dot \eta = -\dot W_0^{(P')},\qquad \tfrac12\left(m + m'\right)\dot \eta^2 - \left(m - m'\right)g\,\eta = \text{const}}$$
>
> **Units:** $\mathrm W$ for the powers, $\mathrm J$ for the energy
> **Meaning:** the string works on each particle, negatively on the one that goes down and positively on the one that goes up, but the two works are equal and opposite: the string only transfers energy from one particle to the other. The conserved quantity is the total mechanical energy of the system up to the additive constant set by the length of the string (last rows): the potential energy of the two weights, measured from the pulleys, depends on $\eta$ alone once $\eta'$ is eliminated with the constraint.

## 8. Friction forces

When a surface or a curve is not smooth, a friction force $\mathbf F_\mu$ must be considered in addition to the normal reaction (Notes.pdf, Sec. 6.6; [Lecture 3, Slide 18]). There are several friction models of different complexity; the course uses the simplest one, the Coulomb model, with a single friction coefficient $\mu$ that depends on the surface and on the particle (a glass particle sliding over ice is not the same as a sand particle sliding over wood). More advanced models distinguish a static coefficient, for a particle at rest, from a dynamic one, for a particle in relative motion; the course makes no such distinction (Notes.pdf, Sec. 6.6, footnote 15). The constraint is assumed to be at rest in some reference frame $S_1$, and $\mathbf v_1^P$ is the velocity of the particle relative to the constraint, measured in $S_1$.

![[attachments/EM-T/t3-friction.svg]]

> [!info] Extension: the friction cone
> The figure also draws a cone about the normal, of half-angle $\arctan\mu$, inside which the total reaction must lie, on its edge while the particle slides. This cone is an **extension**: neither Notes.pdf nor the slides of Lecture 3 use it; it is only the Coulomb bound of Eq. 6.20 read as a set of admissible directions of the total reaction.

> [!derivation] The Coulomb model: the bound and the two regimes
> **Law:** magnitude bound of the friction force; friction lies in the tangent subspace; while sliding it opposes the relative velocity with the saturated magnitude; power relative to the constraint
> **Source:** Notes.pdf, Eq. 6.20; Notes.pdf, Eq. 6.21; Notes.pdf, Sec. 6.6; [Lecture 3, Slide 18]; Notes.pdf, Eq. 4.10
>
> Sticking: $\mathbf v_1^P$ is zero, the magnitude of the friction force is unknown, and so is its direction within the tangent subspace. Sliding: $\mathbf v_1^P$ is not zero, and the force is fully known once the normal reaction is.
>
> $$\begin{aligned}
> \lvert\mathbf F_\mu\rvert &\leq \mu\,\lvert\mathbf N\rvert \quad &\text{(Coulomb bound, Eq. 6.20)} \\
> \mathbf F_\mu &= R_1\,\mathbf t \quad &\text{(sticking on a curve: one new unknown)} \\
> \mathbf F_\mu &= R_1\,\mathbf t_\alpha + R_2\,\mathbf t_\beta \quad &\text{(sticking on a surface: two new unknowns)} \\
> \mathbf F_\mu\cdot\mathbf v_1^P &= 0 \quad &\text{(sticking: $\mathbf v_1^P = \mathbf 0$, no work relative to the constraint)} \\
> \mathbf F_\mu &= -\mu\,\lvert\mathbf N\rvert\,\frac{\mathbf v_1^P}{\lvert\mathbf v_1^P\rvert} \quad &\text{(sliding: saturated bound, antiparallel to $\mathbf v_1^P$, Eq. 6.21)} \\
> \mathbf F_\mu\cdot\mathbf v_1^P &= -\mu\,\lvert\mathbf N\rvert\,\frac{\mathbf v_1^P\cdot\mathbf v_1^P}{\lvert\mathbf v_1^P\rvert} \quad &\text{(power while sliding, relative to the constraint)} \\
> &= -\mu\,\lvert\mathbf N\rvert\,\lvert\mathbf v_1^P\rvert \quad &\text{($\mathbf v_1^P\cdot\mathbf v_1^P = \lvert\mathbf v_1^P\rvert^2$)} \\
> &\leq 0 \quad &\text{($\mu \geq 0$ and both magnitudes $\geq 0$; equal to zero when $\mu\lvert\mathbf N\rvert = 0$)}
> \end{aligned}$$
>
> $$\boxed{\lvert\mathbf F_\mu\rvert \leq \mu\lvert\mathbf N\rvert;\qquad \mathbf v_1^P = \mathbf 0:\ \mathbf F_\mu \in V_T \ \text{unknown};\qquad \mathbf v_1^P \neq \mathbf 0:\ \mathbf F_\mu = -\mu\lvert\mathbf N\rvert\,\frac{\mathbf v_1^P}{\lvert\mathbf v_1^P\rvert},\ \ \mathbf F_\mu\cdot\mathbf v_1^P = -\mu\lvert\mathbf N\rvert\,\lvert\mathbf v_1^P\rvert \leq 0\ \ (< 0 \ \text{only if}\ \mu\lvert\mathbf N\rvert > 0)}$$
>
> **Units:** $\mathrm N$ for the forces ($\mu$ is dimensionless); $\mathrm W$ for the power
> **Meaning:** while the particle sticks, friction is a constraint force, contained in the tangent subspace, with components unknown a priori, and it does no work because the particle does not move relative to the constraint. While the particle slides, friction is an applied force: it introduces no new unknown, points against the relative velocity and its power relative to the constraint is never positive: it is negative, dissipating energy, whenever the normal reaction is not zero, and zero at the instants when the normal reaction vanishes, as on the rough cylinder below for a particle with no turning rate (Notes.pdf, Sec. 6.6; [Lecture 3, Slide 18]).

Each regime is a different mechanics problem, with different equations, and in general it is not known a priori whether friction is large enough to keep the particle at rest or whether it starts to move; the particle may begin moving, stop, move again, and so on. Solving such a problem requires monitoring the bound and the relative velocity continuously and switching from one formulation to the other as necessary (Notes.pdf, Sec. 6.6; [Lecture 3, Slide 19]).

> [!derivation] Counting the unknowns and the conditions to switch
> **Law:** counting of equations and unknowns in each regime; the Coulomb bound must hold in the sticking regime; the relative velocity vanishes when sliding ends
> **Source:** [Lecture 3, Slide 19]; [Lecture 3, Slide 18]; [Lecture 3, Slide 13]; Notes.pdf, Sec. 6.6
>
> Three scalar equations of motion are available in every regime. While the particle sticks, its coordinates are fixed (their rates vanish), so the unknowns are the reaction components only.
>
> $$\begin{aligned}
> \text{surface, sticking:}\quad &N_1,\ R_1,\ R_2 \ \to\ 3 \ \text{unknowns} \quad &\text{(coordinates fixed by $\mathbf v_1^P = \mathbf 0$)} \\
> \text{surface, sliding:}\quad &\text{2 coordinates},\ N_1 \ \to\ 3 \ \text{unknowns} \quad &\text{($\mathbf F_\mu$ known through Eq. 6.21)} \\
> \text{curve, sticking:}\quad &N_1,\ N_2,\ R_1 \ \to\ 3 \ \text{unknowns} \quad &\text{(coordinate fixed)} \\
> \text{curve, sliding:}\quad &\text{1 coordinate},\ N_1,\ N_2 \ \to\ 3 \ \text{unknowns} \quad &\text{($\mathbf F_\mu$ known through Eq. 6.21)} \\
> \text{sticking holds while}\quad &\lvert\mathbf F_\mu\rvert \leq \mu\lvert\mathbf N\rvert \quad &\text{(the friction found from the sticking equations must obey Eq. 6.20)} \\
> \text{switch to sliding when}\quad &\lvert\mathbf F_\mu\rvert = \mu\lvert\mathbf N\rvert \quad &\text{(beyond it the sticking solution would break Eq. 6.20)} \\
> \text{switch to sticking when}\quad &\mathbf v_1^P = \mathbf 0 \quad &\text{(Eq. 6.21 needs a direction of relative motion)}
> \end{aligned}$$
>
> $$\boxed{\text{constraint-force case while } \lvert\mathbf F_\mu\rvert \leq \mu\lvert\mathbf N\rvert;\qquad \text{applied-force case from } \lvert\mathbf F_\mu\rvert = \mu\lvert\mathbf N\rvert \text{ until } \mathbf v_1^P = \mathbf 0}$$
>
> **Units:** pure numbers in the counting; $\mathrm N$ in the conditions
> **Meaning:** both regimes are closed problems. The sticking formulation yields the friction force needed to keep the particle at rest; if that force would have to exceed the bound, no sticking solution exists and the particle begins to move immediately; it then slides until its relative velocity vanishes, and the sticking formulation is tried again ([Lecture 3, Slide 19]). Other friction models exist but are not covered in the course.

> [!example] A particle on a rough circular cylinder ([Lecture 3, Slide 20])
> A particle $P$ of mass $m$ moves over the surface of a rough circular cylinder of radius $a$, with friction coefficient $\mu$. Write down the equations of motion in the applied-force case and in the constraint-force case. The slide gives no other force on the particle, and the box below follows it.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial, origin $O$ on the axis of the cylinder, $\mathbf k$ along the axis; the cylinder is at rest in $S_0$, so $S_1$ is $S_0$ and $\mathbf v_1^P$ is $\mathbf v_0^P$ |
> | surface | $f = x^2 + y^2 - a^2 = 0$ |
> | coordinates | cylindrical $\theta$ and $z$ (two degrees of freedom); $R = a$ fixed |
> | reaction | normal $N_R\,\mathbf e_R$ (the slide writes $N\,\mathbf e_R$); friction $\mathbf F_\mu$ |

![[attachments/EM-T/t3-rough-cylinder.svg]]

> [!derivation] Kinematics of the particle on the cylinder
> **Law:** cylindrical basis and its change of basis matrix; derivatives of the unit vectors (Section 6); product rule
> **Source:** [Lecture 3, Slide 20]; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 1.64
>
> $S_c$ is the frame with origin $O$ and basis $\mathcal B_c$ made of $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$, which turns about the axis with the meridian plane of $P$; it is not the frame $S_1$ of the friction law, which here is $S_0$. View along $\mathbf k$, out of the paper (⊙), on a cross-section of the cylinder: $\mathbf e_R$ and $\mathbf e_\theta$ follow from $\mathbf i$ and $\mathbf j$ by the rotation of angle $\theta$ about $\mathbf k$ with the same right triangles as in Section 6 (adjacent legs $\cos\theta$, opposite legs $\sin\theta$, and the minus sign of the $\mathbf i$ component of $\mathbf e_\theta$, which points to the left of $\mathbf j$ when $\theta$ is between $0$ and $\pi/2$), and $\mathbf e_z$ is $\mathbf k$.
>
> $$\begin{aligned}
> [{}_0R_c] &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ in $\mathcal B_0$, Eq. 1.13)} \\
> \det[{}_0R_c] &= 1\cdot\left(\cos\theta\cos\theta - (-\sin\theta)\sin\theta\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2\theta + \sin^2\theta \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_c][{}_0R_c]^T\right)_{22} &= \sin\theta\sin\theta + \cos\theta\cos\theta + 0\cdot 0 \quad &\text{(row 2 times row 2)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_c][{}_0R_c]^T\right)_{12} &= \cos\theta\sin\theta + (-\sin\theta)\cos\theta + 0\cdot 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)} \\
> \mathbf r_0^P &= a\,\mathbf e_R + z\,\mathbf k \quad &\text{(radius $a$ from the axis, height $z$)} \\
> \mathbf v_0^P &= a\,\frac{d\mathbf e_R}{dt} + \dot z\,\mathbf k \quad &\text{(derivative in $S_0$; $a$ and $\mathbf k$ constant)} \\
> &= a\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k \quad &\text{($d\mathbf e_R/dt = \dot\theta\,\mathbf e_\theta$, Section 6)} \\
> \mathbf a_0^P &= a\ddot\theta\,\mathbf e_\theta + a\dot\theta\,\frac{d\mathbf e_\theta}{dt} + \ddot z\,\mathbf k \quad &\text{(product rule)} \\
> &= -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta + \ddot z\,\mathbf k \quad &\text{($d\mathbf e_\theta/dt = -\dot\theta\,\mathbf e_R$)} \\
> \lvert\mathbf v_0^P\rvert &= \sqrt{a^2\dot\theta^2 + \dot z^2} \quad &\text{(orthonormal basis)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = a\,\mathbf e_R + z\,\mathbf k,\quad \mathbf v_0^P = a\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k,\quad \mathbf a_0^P = -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta + \ddot z\,\mathbf k}$$
>
> **Units:** $\mathrm m$, $\mathrm{m/s}$, $\mathrm{m/s^2}$
> **Meaning:** the expressions of [Lecture 3, Slide 20]. The velocity lies in the tangent plane of the cylinder, spanned by $\mathbf e_\theta$ and $\mathbf k$; the normal $\nabla f$ is $2a\,\mathbf e_R$ on the cylinder, so the normal reaction is along $\mathbf e_R$ and the friction force along $\mathbf e_\theta$ and $\mathbf k$.

> [!derivation] Equations of motion on the rough cylinder in both regimes
> **Law:** Newton's second law with the normal reaction and the friction force of each regime, projected on $\mathbf e_R$, $\mathbf e_\theta$ and $\mathbf k$
> **Source:** [Lecture 3, Slide 20]; [Lecture 3, Slide 19]; Notes.pdf, Eq. 6.21; Notes.pdf, Eq. 4.4
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= N_R\,\mathbf e_R - \mu\lvert N_R\rvert\,\frac{a\dot\theta\,\mathbf e_\theta + \dot z\,\mathbf k}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(applied-force case, $\mathbf v_0^P \neq \mathbf 0$: Eq. 6.21)} \\
> \mathbf e_R:\quad -m a\dot\theta^2 &= N_R \quad &\text{(radial projection)} \\
> \mathbf e_\theta:\quad m a\ddot\theta &= -\mu\lvert N_R\rvert\,\frac{a\dot\theta}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(tangential projection along the parallel)} \\
> \mathbf k:\quad m\ddot z &= -\mu\lvert N_R\rvert\,\frac{\dot z}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(projection along the axis)} \\
> m a\ddot\theta &= -\mu m a\dot\theta^2\,\frac{a\dot\theta}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(substitute $\lvert N_R\rvert = m a\dot\theta^2$ from the radial projection)} \\
> \ddot\theta &= -\frac{\mu a\dot\theta^3}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(divide by $m a$)} \\
> m\ddot z &= -\mu m a\dot\theta^2\,\frac{\dot z}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(substitute $\lvert N_R\rvert$)} \\
> \ddot z &= -\frac{\mu a\dot\theta^2\,\dot z}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(divide by $m$)} \\
> \mathbf 0 &= N_R\,\mathbf e_R + R_1\,\mathbf e_\theta + R_2\,\mathbf k \quad &\text{(constraint-force case: $\mathbf v_0^P = \mathbf 0$ held, so $\mathbf a_0^P = \mathbf 0$)} \\
> N_R &= 0,\quad R_1 = 0,\quad R_2 = 0 \quad &\text{(the three projections; no applied force)} \\
> \sqrt{R_1^2 + R_2^2} &\leq \mu\lvert N_R\rvert \quad &\text{(condition of the sticking case: $0 \leq 0$ holds)}
> \end{aligned}$$
>
> $$\boxed{\text{sliding: } N_R = -m a\dot\theta^2,\ \ \ddot\theta = -\frac{\mu a\dot\theta^3}{\sqrt{a^2\dot\theta^2 + \dot z^2}},\ \ \ddot z = -\frac{\mu a\dot\theta^2\dot z}{\sqrt{a^2\dot\theta^2 + \dot z^2}},\ \ \sqrt{a^2\dot\theta^2 + \dot z^2} > 0;\qquad \text{sticking: } \mathbf 0 = N_R\,\mathbf e_R + R_1\,\mathbf e_\theta + R_2\,\mathbf k,\ \ \sqrt{R_1^2 + R_2^2} \leq \mu\lvert N_R\rvert}$$
>
> **Units:** $\mathrm N$ in the projections; $\mathrm{rad/s^2}$ and $\mathrm{m/s^2}$ in the two equations of motion
> **Meaning:** in the sliding case the radial projection gives the reaction, and the two tangential projections, once the reaction is substituted, are the two equations of motion; in the sticking case the three unknowns are the reaction components. Without applied forces a particle at rest stays at rest with zero reactions, and the sticking condition is met with equality; with an applied force the same three equations would give the friction needed, to be compared with the bound.

> [!warning] Sign of the normal reaction on the cylinder of Lecture 3, Slide 20
> The radial projection of the box above gives a negative $N_R$ whenever the particle turns about the axis: the cylinder pushes the particle towards the axis. That is possible only if the particle slides on the inner face of the cylinder, or if the constraint is bilateral; on the outer face of a unilateral cylinder, with no other force, the particle would leave the surface. The slide writes the friction magnitude as $\mu N$, with $N$ the magnitude of the normal force ([Lecture 3, Slide 18]); with the signed component $N_R$ used here, that magnitude is $\mu\lvert N_R\rvert$, as in Eq. 6.21.

> [!derivation] First integrals of the sliding motion on the cylinder (built for this note)
> **Law:** chain rule for the speed; quotient rule; separation of variables and Barrow's rule
> **Source:** [Lecture 3, Slide 20]; Notes.pdf, Eq. 6.21; Notes.pdf, Eq. 6.17
>
> Let the particle start sliding with $\dot\theta(0) > 0$ (if it starts with $\dot\theta(0) = 0$ the normal reaction and the friction are zero and it slides along a generatrix at constant speed). $v_0^P$ is the speed of the previous box and $\psi$ the angle between the velocity and the horizontal direction $\mathbf e_\theta$, with $\tan\psi$ equal to $\dot z/(a\dot\theta)$.
>
> $$\begin{aligned}
> \frac{d v_0^P}{dt} &= \frac{a^2\dot\theta\,\ddot\theta + \dot z\,\ddot z}{\sqrt{a^2\dot\theta^2 + \dot z^2}} \quad &\text{(chain rule on the square root)} \\
> &= \frac{-\mu a\dot\theta^2\left(a^2\dot\theta^2 + \dot z^2\right)}{a^2\dot\theta^2 + \dot z^2} \quad &\text{(substitute $\ddot\theta$ and $\ddot z$; common factor)} \\
> &= -\mu a\dot\theta^2 \quad &\text{(simplify)} \\
> \frac{d}{dt}\left(\frac{\dot z}{a\dot\theta}\right) &= \frac{\ddot z\,\dot\theta - \dot z\,\ddot\theta}{a\dot\theta^2} \quad &\text{(quotient rule)} \\
> &= \frac{1}{a\dot\theta^2}\left(-\frac{\mu a\dot\theta^3\,\dot z}{v_0^P} + \frac{\mu a\dot\theta^3\,\dot z}{v_0^P}\right) \quad &\text{(substitute $\ddot z$ and $\ddot\theta$)} \\
> &= 0 \quad &\text{(the two terms cancel: $\psi$ is constant)} \\
> a\dot\theta &= v_0^P\cos\psi \quad &\text{(the horizontal component of the velocity)} \\
> \frac{d v_0^P}{dt} &= -\frac{\mu\cos^2\psi}{a}\left(v_0^P\right)^2 \quad &\text{(substitute $\dot\theta$ in the first result)} \\
> \int_{v_0^P(0)}^{v_0^P(t)}\frac{dv}{v^2} &= -\frac{\mu\cos^2\psi}{a}\int_0^t dt' \quad &\text{(separate variables and integrate)} \\
> \left[-\frac1v\right]_{v_0^P(0)}^{v_0^P(t)} &= -\frac{\mu\cos^2\psi}{a}\,t \quad &\text{(antiderivatives; Barrow on the right)} \\
> \frac{1}{v_0^P(0)} - \frac{1}{v_0^P(t)} &= -\frac{\mu\cos^2\psi}{a}\,t \quad &\text{(Barrow on the left)} \\
> v_0^P(t) &= \frac{v_0^P(0)}{1 + \mu\cos^2\psi\,v_0^P(0)\,t/a} \quad &\text{(solve for $v_0^P(t)$)}
> \end{aligned}$$
>
> $$\boxed{\frac{\dot z}{a\dot\theta} = \tan\psi = \text{const},\qquad \frac{d v_0^P}{dt} = -\mu a\dot\theta^2,\qquad v_0^P(t) = \frac{v_0^P(0)}{1 + \mu\cos^2\psi\,v_0^P(0)\,t/a}}$$
>
> **Units:** $\mathrm{m/s^2}$ for the rate of the speed ($a\dot\theta^2$ in $\mathrm{m\,s^{-2}}$); $\mu\,v_0^P\,t/a$ dimensionless
> **Meaning:** friction only slows the particle down without turning its velocity within the tangent plane, so the particle follows a helix of constant angle $\psi$; the rate of the speed is minus $\mu$ times the magnitude of the normal reaction divided by the mass, the tangential equation of Eq. 6.17 with the friction as the only tangential force. The speed decreases like the inverse of time: it never vanishes in finite time, since the denominator stays finite, so the particle never sticks on this frictional cylinder without applied forces. Here $v$ and $t'$ are integration variables.

## 9. The Newtonian mechanics approach

With vector bases, reference frames and coordinate systems, the rotation, projection and differentiation of vectors, the kinematics of a particle, relative motion, force and linear momentum with Newton's second law, constraints with their degrees of freedom and reaction forces, the moment of a force and the angular momentum, and the conservation of mechanical energy, all the basic tools to solve a problem of particle motion are available (Notes.pdf, Ch. 7). Chapter 7 of the notes proposes a systematic approach for problems with one or more particles: it may not be the fastest route in some cases, but the step-by-step process is recommended, especially for beginners. The angular momentum belongs to Topic 4 and the relative motion to Topic 5; this section uses only what it needs of them, cited.

| Step | What is done | Its output | Where this note does it |
| :--- | :--- | :--- | :--- |
| understanding the problem (Sec. 7.1) | translate the conditions of the statement into mathematical constraints; draw the system | the number of degrees of freedom | the data tables of the examples |
| selecting the coordinates (Sec. 7.2) | as many independent coordinates as degrees of freedom, adapted to the constraints | the generalized coordinates | Section 3 |
| defining reference frames (Sec. 7.3) | the inertial frame and auxiliary frames, each a simple rotation from the previous one; every basis expressed in known vectors | the change of basis relations | the polar bases of Sections 6 and 8 |
| kinematics (Sec. 7.4) | angular velocities, then position, velocity and acceleration of each particle in terms of the coordinates | the vectors of the second law | Sections 6, 7 and 8 |
| defining the forces (Sec. 7.5) | applied, reaction and, only in a non-inertial frame, inertia forces, each with its magnitude and direction | the forces in terms of the coordinates and new unknown parameters | Sections 5 to 8 |
| equations of motion (Sec. 7.6) | project the second law on well-chosen directions; add the constraint equations; check that equations and unknowns are equal in number | a closed set of equations | Sections 5 to 8 |
| integration and particular questions (Sec. 7.7) | uncouple, integrate or reduce to quadratures; discuss the regions of existence | the motion or the asked features of it | Sections 6 and 8 |

### Understanding the problem

The first and most important step is to understand what is looked for (Notes.pdf, Sec. 7.1). In the course the statement is given; in real life the problem first needs to be defined in a crystal-clear form and modelled so that it can be analysed. The statement usually contains conditions on the motion (the particle is attached to a string, it moves on a plane) that must be translated into mathematical conditions, and an essential question to answer is how many degrees of freedom the problem has. Drawing sketches, as many as needed and from as many angles as needed, helps to visualize the system: at least a drawing of the particle in a generic configuration, and auxiliary sketches of the simple rotations. The next step should not be started before every part of the task is understood and a general idea of the solution is in place.

| Example of this note | Conditions translated into constraints | Degrees of freedom |
| :--- | :--- | :--- |
| vertical circle, Section 6 | circle and its plane: two equations | $3 - 2 = 1$: $\theta$ |
| two particles and a string, Section 7 | two vertical lines (two equations each) and the string (one equation) | $6 - 5 = 1$: $\eta$ |
| rough cylinder, Section 8 | the cylinder: one equation | $3 - 1 = 2$: $\theta$, $z$ (none while the particle sticks) |
| spool, Section 5 | vertical axis (two equations) and the string collected at a given rate (one equation, depending on time) | $3 - 3 = 0$: only time |

### Selecting the coordinates

The number of coordinates should match the number of configuration degrees of freedom; the only exception is a non-integrable constraint, which requires an excess of coordinates and appears only in the second part of the course (Notes.pdf, Sec. 7.2). The choice is not unique, but a poor one can lead to expressions too difficult to handle: one looks at the constraints and considers distances, arc lengths and angles that express the velocity and acceleration simply, such as the Cartesian coordinates, the distance of a particle to a fixed plane or the polar angle of a moving line. The ability to choose well comes from practice. A common error is to select redundant, dependent parameters.

> [!derivation] Two dependent distances
> **Law:** the distances to two parallel planes are tied by the distance between the planes
> **Source:** Notes.pdf, Sec. 7.2
>
> $\ell_1$ is the distance of $P$ to the plane at height zero and $\ell_2$ its distance to the plane at height $H$ (the notes write $l_1$, $l_2$ and $L$), with $P$ between the two planes.
>
> $$\begin{aligned}
> \ell_1 &= z,\quad \ell_2 = H - z \quad &\text{(distances measured along $\mathbf k$)} \\
> \ell_2 &= H - \ell_1 \quad &\text{(eliminate $z$)} \\
> \dot\ell_2 &= -\dot\ell_1 \quad &\text{(time derivative; $H$ constant)}
> \end{aligned}$$
>
> $$\boxed{\ell_2 = H - \ell_1}$$
>
> **Units:** $\mathrm m$
> **Meaning:** the two distances carry the same information, so only one of them may be a coordinate. Introducing a redundant coordinate temporarily can help to pose a problem, but it must then be eliminated with the constraint equation (Notes.pdf, Sec. 7.2), as $\eta'$ was in Section 7.

### Defining reference frames

In Newtonian mechanics there is always a predefined inertial frame $S_0$ in which the answer must be expressed; if it is not given explicitly, the conditions for a frame to be inertial are implicit in the problem, and the frame must be defined (Notes.pdf, Sec. 7.3). The solution may become easier with auxiliary frames that decompose the motion into simple rotations and simple translations; each one must be clearly defined in writing, identified in the drawing and labelled. With each frame comes its vector basis, and other bases may be of interest too, such as the intrinsic basis or the basis of the coordinates. The second task of this step is to express every new basis in terms of known vectors in a generic position of the system, using the chosen coordinates; otherwise those vectors cannot be used in the solution.

![[attachments/EM-T/t3-simple-rotation.svg]]

> [!derivation] Basis of a frame rotated about a common axis
> **Law:** right triangles of the unit vectors in the plane of the rotation; right-hand rule about $\mathbf k_1$; the change of basis matrix and its transpose
> **Source:** Notes.pdf, Eq. 7.1; Notes.pdf, Sec. 7.3; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.20
>
> $S_2$ is rotated an angle $\theta$ with respect to $S_1$ about the $\mathbf k_1$ direction. View along $\mathbf k_1$, which points out of the paper (⊙): $\mathbf i_1$, $\mathbf j_1$ fixed in the view, $\mathbf i_2$, $\mathbf j_2$ turned counterclockwise by $\theta$, the sense of positive rotation about $\mathbf k_1$ by the right-hand rule. In the right triangle with unit hypotenuse $\mathbf i_2$ and the angle $\theta$ between $\mathbf i_1$ and $\mathbf i_2$, the leg along $\mathbf i_1$ is adjacent, $\cos\theta$, and the leg along $\mathbf j_1$ is opposite, $\sin\theta$. In the triangle with hypotenuse $\mathbf j_2$ and the same angle $\theta$ between $\mathbf j_1$ and $\mathbf j_2$, the leg along $\mathbf j_1$ is adjacent, $\cos\theta$, and the opposite leg, $\sin\theta$, points towards $-\mathbf i_1$, since turning $\mathbf j_1$ counterclockwise moves it to the left: this is the minus sign.
>
> $$\begin{aligned}
> \mathbf i_2 &= \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1 \quad &\text{(legs of the first triangle)} \\
> \mathbf j_2 &= -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1 \quad &\text{(legs of the second triangle)} \\
> \mathbf k_2 &= \mathbf k_1 \quad &\text{(the axis of the rotation does not move)} \\
> [{}_1R_2] &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: the vectors of $S_2$ in the basis of $S_1$, Eq. 1.13; Eq. 1.20)} \\
> \det[{}_1R_2] &= 1\cdot\left(\cos^2\theta + \sin^2\theta\right) \quad &\text{(expand along the third row)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{11} &= \cos^2\theta + \sin^2\theta + 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_1R_2][{}_1R_2]^T\right)_{21} &= \sin\theta\cos\theta + \cos\theta\,(-\sin\theta) + 0 \quad &\text{(row 2 times row 1)} \\
> &= 0 \quad &\text{(the two products cancel)} \\
> \mathbf i_1 &= \cos\theta\,\mathbf i_2 - \sin\theta\,\mathbf j_2 \quad &\text{(first row of the matrix, read through the transpose, Eq. 1.14)} \\
> \mathbf j_1 &= \sin\theta\,\mathbf i_2 + \cos\theta\,\mathbf j_2 \quad &\text{(second row)}
> \end{aligned}$$
>
> $$\boxed{\mathbf i_2 = \cos\theta\,\mathbf i_1 + \sin\theta\,\mathbf j_1,\qquad \mathbf j_2 = -\sin\theta\,\mathbf i_1 + \cos\theta\,\mathbf j_1,\qquad \mathbf k_2 = \mathbf k_1}$$
>
> **Units:** dimensionless
> **Meaning:** Eq. 7.1, or alternatively the vectors of $S_1$ written in terms of those of $S_2$; once either set is written, every vector of both bases can be used. When consecutive bases are a simple rotation apart, the familiar cosine and sine expressions result; rather than memorizing them, it is preferable to rebuild them each time from the drawing, to avoid misplacing a minus sign (Notes.pdf, Sec. 7.3). The polar bases of Sections 6 and 8 are this rotation with $S_1$ replaced by $S_0$.

### Kinematics of the particles

With the coordinates and the frames chosen, the next step obtains the position, velocity and acceleration vectors of each particle in a generic state, as functions of the chosen coordinates and their derivatives only, together with the angular velocity and angular acceleration of every frame with respect to the fixed one (Notes.pdf, Sec. 7.4). Absolute quantities are usually enough, but some problems ask for relative ones. The angular velocities come first: between frames a simple rotation apart, the relative angular velocity is the rate of the angle times the axis; the laws of composition give the absolute ones, and differentiation gives the angular accelerations.

> [!derivation] Angular velocities of a chain of simple rotations
> **Law:** angular velocity of a simple rotation; composition of angular velocities; angular acceleration by differentiation
> **Source:** Notes.pdf, Sec. 7.4; Notes.pdf, Eq. 3.14; Notes.pdf, Eq. 3.15; Notes.pdf, Eq. 3.9
>
> $$\begin{aligned}
> \boldsymbol\omega_{21} &= \dot\theta\,\mathbf k_1 \quad &\text{($S_2$ results from rotating $S_1$ by $\theta$ about the positive $\mathbf k_1$)} \\
> \boldsymbol\omega_{20} &= \boldsymbol\omega_{21} + \boldsymbol\omega_{10} \quad &\text{(composition, Eq. 3.14)} \\
> \boldsymbol\alpha_{20} &= \boldsymbol\alpha_{21} + \boldsymbol\omega_{10}\times\boldsymbol\omega_{21} + \boldsymbol\alpha_{10} \quad &\text{(composition, Eq. 3.15)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{21} = \dot\theta\,\mathbf k_1,\qquad \boldsymbol\omega_{20} = \dot\theta\,\mathbf k_1 + \boldsymbol\omega_{10}}$$
>
> **Units:** $\mathrm{rad/s}$ and $\mathrm{rad/s^2}$
> **Meaning:** each simple rotation contributes the rate of its angle along its axis, and the contributions add; the angular acceleration of the last frame needs the extra term, the cross product of $\boldsymbol\omega_{10}$ with $\boldsymbol\omega_{21}$, because the axis $\mathbf k_1$ is carried by $S_1$.

The position, velocity and acceleration can then be obtained in several equivalent ways (Notes.pdf, Sec. 7.4): (1) write the absolute position with vectors of different bases and differentiate in the fixed frame, using the Coriolis theorem for every unit vector that is not constant in it; (2) first transform the position to the basis of the fixed frame with relations like Eq. 7.1 and differentiate there, which needs no Coriolis theorem but may give longer intermediate expressions; (3) write the relative position with respect to a useful auxiliary frame, differentiate it in that frame to obtain the relative velocity and acceleration, and connect them with the absolute ones through the composition laws of Chapter 3. Any of the three must give the same result, and all begin with a position vector, which can be built as a sum of simpler vectors, such as $\overrightarrow{OA}$, $\overrightarrow{AB}$, $\overrightarrow{BC}$ and $\overrightarrow{CP}$. Way (1) was used for the particle on the vertical circle of Section 6; the box below checks ways (2) and (3) on the same particle.

> [!derivation] Three equivalent ways to the kinematics of the particle on the vertical circle
> **Law:** way (2): derivatives of the Cartesian components (chain and product rules); way (3): relative kinematics in the frame that turns with the radius and the composition of velocities and accelerations
> **Source:** Notes.pdf, Sec. 7.4; Notes.pdf, Eq. 3.20; Notes.pdf, Eq. 3.25; Notes.pdf, Eq. 1.32; [Lecture 3, Slide 15]
>
> $S_1$ has its origin at $O$ (fixed) and the basis $\mathbf i_1$, $\mathbf j_1$, $\mathbf k_1$ equal to the $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf k$ of Section 6, so $\boldsymbol\omega_{10}$ is $\dot\theta\,\mathbf k$ and $\boldsymbol\alpha_{10}$ is $\ddot\theta\,\mathbf k$ (the derivative of $\dot\theta\,\mathbf k$, with $\mathbf k$ fixed).
>
> $$\begin{aligned}
> \mathbf r_0^P &= a\cos\theta\,\mathbf i + a\sin\theta\,\mathbf j \quad &\text{(2: position in the basis of $S_0$, Section 6)} \\
> \mathbf v_0^P &= -a\dot\theta\sin\theta\,\mathbf i + a\dot\theta\cos\theta\,\mathbf j \quad &\text{(2: chain rule on each component; $\mathbf i$, $\mathbf j$ constant)} \\
> &= a\dot\theta\,\mathbf e_\theta \quad &\text{(2: the bracket is $\mathbf e_\theta$)} \\
> \mathbf a_0^P &= \left(-a\ddot\theta\sin\theta - a\dot\theta^2\cos\theta\right)\mathbf i + \left(a\ddot\theta\cos\theta - a\dot\theta^2\sin\theta\right)\mathbf j \quad &\text{(2: product and chain rules on each component)} \\
> &= a\ddot\theta\left(-\sin\theta\,\mathbf i + \cos\theta\,\mathbf j\right) - a\dot\theta^2\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) \quad &\text{(2: group by $\ddot\theta$ and $\dot\theta^2$)} \\
> &= a\ddot\theta\,\mathbf e_\theta - a\dot\theta^2\,\mathbf e_R \quad &\text{(2: the brackets are $\mathbf e_\theta$ and $\mathbf e_R$)} \\
> \mathbf r_1^P &= a\,\mathbf i_1,\quad \mathbf v_1^P = \mathbf 0,\quad \mathbf a_1^P = \mathbf 0 \quad &\text{(3: $P$ is fixed in $S_1$)} \\
> \mathbf v_0^P &= \mathbf v_0^O + \mathbf v_1^P + \boldsymbol\omega_{10}\times\mathbf r_1^P \quad &\text{(3: composition of velocities, Eq. 3.20)} \\
> &= \dot\theta\,\mathbf k_1\times a\,\mathbf i_1 \quad &\text{(3: $O$ fixed, $\mathbf v_1^P = \mathbf 0$)} \\
> &= a\dot\theta\,\mathbf j_1 \quad &\text{(3: $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$)} \\
> \mathbf a_0^P &= \mathbf a_0^O + \mathbf a_1^P + \boldsymbol\alpha_{10}\times\mathbf r_1^P + \boldsymbol\omega_{10}\times\left(\boldsymbol\omega_{10}\times\mathbf r_1^P\right) + 2\,\boldsymbol\omega_{10}\times\mathbf v_1^P \quad &\text{(3: composition of accelerations, Eq. 3.25)} \\
> &= \ddot\theta\,\mathbf k_1\times a\,\mathbf i_1 + \dot\theta\,\mathbf k_1\times\left(\dot\theta\,\mathbf k_1\times a\,\mathbf i_1\right) \quad &\text{(3: $O$ fixed; $\mathbf a_1^P$ and $\mathbf v_1^P$ zero)} \\
> &= a\ddot\theta\,\mathbf j_1 + \dot\theta\,\mathbf k_1\times a\dot\theta\,\mathbf j_1 \quad &\text{(3: $\mathbf k_1\times\mathbf i_1 = \mathbf j_1$, twice)} \\
> &= a\ddot\theta\,\mathbf j_1 - a\dot\theta^2\,\mathbf i_1 \quad &\text{(3: $\mathbf k_1\times\mathbf j_1 = -\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\text{ways (1), (2), (3)}:\quad \mathbf v_0^P = a\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_0^P = -a\dot\theta^2\,\mathbf e_R + a\ddot\theta\,\mathbf e_\theta}$$
>
> **Units:** $\mathrm{m/s}$ and $\mathrm{m/s^2}$
> **Meaning:** the three ways give the vectors of Section 6, as they must. In way (3) the centripetal part of the acceleration comes from the double cross product of $\boldsymbol\omega_{10}$ with the cross product of $\boldsymbol\omega_{10}$ and $\mathbf r_1^P$, and the tangential part from the cross product of $\boldsymbol\alpha_{10}$ with $\mathbf r_1^P$; there is no Coriolis term because $P$ does not move in $S_1$.

> [!warning] Relative to a frame is not the same as expressed in a basis
> A position, velocity or acceleration relative to some reference frame (who observes, and which derivative is taken) is a different concept from a vector expressed in the basis of some frame (which unit vectors are used to write its components): any of these vectors can be written in any basis (Notes.pdf, Sec. 7.4). In way (3) above, $\mathbf v_0^P$ is relative to $S_0$ but is written in the basis of $S_1$.

### Defining the forces of the problem

The next step identifies the magnitude and direction of every force on each particle and expresses it in a useful mathematical form (Notes.pdf, Sec. 7.5). The forces fall into three groups:

| Group | Examples | What is known | Source |
| :--- | :--- | :--- | :--- |
| applied forces | gravity on a heavy particle, drag, buoyancy, the force of a spring, any force exerted directly on the particle; friction while sliding | the magnitude, always a priori, although it may depend on the position, the velocity and time in a prescribed way | Notes.pdf, Sec. 7.5; [Lecture 3, Slide 18] |
| reaction (constraint) forces | the normal force of a surface, the two normal components of a curve, the friction force when its magnitude and direction are unknown, the tension of a cable | only the subspace: an extra unknown parameter is introduced for each component, as $\lambda$ in $\lambda\,\nabla f$ or $F_\tau$ in a tension along the cable | Notes.pdf, Sec. 7.5; [Lecture 3, Slide 13] |
| inertia forces | present if and only if the second law is written in a non-inertial frame (Topic 5) | they follow from the motion of that frame | Notes.pdf, Sec. 7.5 |

Including inertia forces when the second law is applied in an inertial frame is a common mistake of beginners (Notes.pdf, Sec. 7.5). Each force must be expressed with its magnitude and direction as a function of the chosen coordinates, their derivatives and perhaps time; the direction of a normal reaction follows from the gradient of the surface or surfaces of the constraint.

> [!derivation] The force of a spring of zero natural length
> **Law:** the spring pulls each end towards the other with a force proportional to its elongation; the elongation of a spring of zero natural length is its length
> **Source:** Notes.pdf, Sec. 7.5
>
> A spring of stiffness $k$ and zero length at rest connects $P$ with the origin $O$.
>
> $$\begin{aligned}
> \mathbf F_S &= -k\,\lvert\overrightarrow{OP}\rvert\,\frac{\overrightarrow{OP}}{\lvert\overrightarrow{OP}\rvert} \quad &\text{(magnitude $k$ times the elongation, directed from $P$ towards $O$)} \\
> &= -k\,\overrightarrow{OP} \quad &\text{(the lengths cancel)} \\
> &= -k\,\mathbf r_0^P \quad &\text{($O$ is the origin of $S_0$)} \\
> &= -k x\,\mathbf i - k y\,\mathbf j - k z\,\mathbf k \quad &\text{(Cartesian components of $\mathbf r_0^P$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_S = -k\,\mathbf r_0^P = -k x\,\mathbf i - k y\,\mathbf j - k z\,\mathbf k}$$
>
> **Units:** $\mathrm{N/m}$ times $\mathrm m$, $\mathrm N$
> **Meaning:** an applied force known in magnitude and direction at every position; as for the kinematics, the vector from one end of the spring to the other may be easier to build as a sum of partial vectors.

> [!warning] Typo in Notes.pdf, Sec. 7.5: the spring vector
> The notes write the force of the spring that connects $P$ with $O$ as minus $k$ times $\overrightarrow{OA}$, and in the same line as minus $k$ times $\mathbf r_0^P$; no point $A$ is defined there. The vector must be $\overrightarrow{OP}$, which is $\mathbf r_0^P$, as the box above shows.

### Obtaining the equations of motion

The unknowns of the problem are the chosen coordinates as functions of time and the additional parameters introduced for the reaction forces; an equal number of independent scalar equations is needed to close the problem (Notes.pdf, Sec. 7.6). Newton's second law is a vector equation that can be projected on any three independent directions, giving three independent scalar equations per particle. First the frame in which it is applied must be chosen: in an inertial frame no inertia forces appear. The accelerations and forces of the previous steps are then simply plugged in, the accelerations being those relative to the chosen frame. The directions of projection deserve thought: projecting on the tangent subspace of the constraints removes the normal reactions, and projecting on the normal directions gives equations for them. The constraint equations, if any, are added, and the sanity check follows: if equations and unknowns are not equal in number, something has been missed in this or in a previous step.

> [!derivation] Equations and unknowns in the examples of this note
> **Law:** three scalar equations per particle, plus one equation per constraint not built into the coordinates; unknowns: the coordinates and one parameter per reaction component
> **Source:** Notes.pdf, Sec. 7.6; [Lecture 3, Slide 13]; [Lecture 3, Slide 19]
>
> In every example the coordinates parametrize the constraints, so no constraint equation is added.
>
> $$\begin{aligned}
> \text{vertical circle:}\quad &3 \ \text{equations};\ \ \theta,\ N_R,\ N_z \ \to\ 3 \ \text{unknowns} \quad &\text{(Section 6)} \\
> \text{two particles:}\quad &3 + 3 = 6 \ \text{equations};\ \ \eta,\ F_\tau \ \text{and two horizontal reaction components per particle} \ \to\ 6 \ \text{unknowns} \quad &\text{(Section 7: the reactions of the vertical lines are zero, no applied force being horizontal)} \\
> \text{rough cylinder, sliding:}\quad &3 \ \text{equations};\ \ \theta,\ z,\ N_R \ \to\ 3 \ \text{unknowns} \quad &\text{(Section 8)} \\
> \text{rough cylinder, sticking:}\quad &3 \ \text{equations};\ \ N_R,\ R_1,\ R_2 \ \to\ 3 \ \text{unknowns} \quad &\text{(Section 8)} \\
> \text{spool:}\quad &3 \ \text{equations};\ \ F_\tau \ \text{and two horizontal reaction components} \ \to\ 3 \ \text{unknowns} \quad &\text{(Section 5: no coordinate left)}
> \end{aligned}$$
>
> $$\boxed{\text{number of independent scalar equations} = \text{number of coordinates} + \text{number of reaction parameters}}$$
>
> **Units:** pure numbers
> **Meaning:** every example is closed. For the two particles, two components of the second law of each particle are horizontal; they only fix the reactions that keep each particle on its vertical line, which is why Section 7 could work with the two vertical components alone.

Instead of the second law, or of some of its projections, the conservation of mechanical energy, when its conditions hold, and the angular momentum equation may be used (Notes.pdf, Sec. 7.6). They add no information, since they follow from the second law, but they are often a useful substitute: the first integral of Section 6 is the energy equation of that problem.

### Integration of the problem and particular questions

The last step integrates the problem: the equations obtained are a mix of differential and algebraic equations, and the differential ones are integrated to give the trajectory of each particle as a function of time and of the initial conditions, as for the harmonic oscillator (Notes.pdf, Sec. 7.7). Except in very particular problems a fully analytical integration is impossible and numerical integration is needed. Often some unknowns can be eliminated from a subset of the equations, which are then uncoupled from the rest and can be integrated separately, "divide et impera": the typical case is the normal reaction, absent from the tangential projections, so the motion is solved first and the reaction computed afterwards, as in Sections 6 and 8.

Sometimes only certain features of the motion are wanted, such as the regions of existence of the solution or the shape of the possible trajectories as a function of the initial conditions (Notes.pdf, Sec. 7.7). It may then be enough to work with the original equations, or to integrate them once instead of twice: reducing the problem to equations that contain only time, the unknowns and at most their first derivatives is called reducing it to quadratures, and the conservation of mechanical energy, when it applies, is already such a first integral. A common case is a relation between the square of the rate of one coordinate and that coordinate, depending on the initial conditions: since that square cannot be negative, the boundaries of the regions of existence are the roots of the relation with the rate set to zero, and they can be visualized by plotting an effective potential against the coordinate.

![[attachments/EM-T/t3-region-existence.svg]]

> [!derivation] Regions of existence of the particle on the vertical circle
> **Law:** the first integral is a relation between the square of the rate and the angle; a real motion needs a non-negative square; boundaries where the rate vanishes
> **Source:** Notes.pdf, Sec. 7.7; [Lecture 3, Slide 15]
>
> The first integral of Section 6, with $K$ fixed by the initial conditions; the effective potential is the term $(g/a)\sin\theta$, plotted against $\theta$ with the level $K$. In the separating case the angle is written near the highest point with a small departure $\varepsilon$, whose value at an instant $t_1$ is $\varepsilon_1$.
>
> $$\begin{aligned}
> \dot\theta^2 &= 2K - \frac{2g}{a}\sin\theta \quad &\text{(first integral of Section 6 solved for the square of the rate)} \\
> 2K - \frac{2g}{a}\sin\theta &\geq 0 \quad &\text{(the square of a real rate is not negative)} \\
> \frac{2g}{a}\sin\theta &\leq 2K \quad &\text{(move the sine term over)} \\
> \sin\theta &\leq \frac{a K}{g} \quad &\text{(divide by $2g/a$, which is positive)} \\
> \sin\theta_* &= \frac{a K}{g} \quad &\text{(boundaries: the rate is zero)} \\
> \frac{a K}{g} &\geq 1 \ \Rightarrow \ \text{every } \theta \text{ allowed} \quad &\text{(the sine never exceeds one)} \\
> -1 < \frac{a K}{g} &< 1 \ \Rightarrow \ \sin\theta \leq \frac{a K}{g} \quad &\text{(an arc around the lowest point, between two turning angles $\theta_*$)} \\
> \frac{a K}{g} &= -1 \ \Rightarrow \ \theta = -\frac{\pi}{2},\ \dot\theta = 0 \quad &\text{(only the lowest point: rest at the bottom)} \\
> \frac{a K}{g} &= 1:\quad \theta = \frac{\pi}{2} + \varepsilon \quad &\text{(the separating case, near the highest point)} \\
> \ddot\theta\big|_{\theta = \pi/2} &= -\frac{g}{a}\cos\frac{\pi}{2} \quad &\text{(equation of motion of Section 6 at the highest point)} \\
> &= 0 \quad &\text{($\cos(\pi/2) = 0$: the highest point is an equilibrium)} \\
> \ddot\theta &= \ddot\varepsilon \quad &\text{(second time derivative; $\pi/2$ is constant)} \\
> \cos\left(\frac{\pi}{2} + \varepsilon\right) &= \cos\frac{\pi}{2}\cos\varepsilon - \sin\frac{\pi}{2}\sin\varepsilon \quad &\text{(cosine of a sum)} \\
> &= -\sin\varepsilon \quad &\text{($\cos(\pi/2) = 0$, $\sin(\pi/2) = 1$)} \\
> &\approx -\varepsilon \quad &\text{(first order in $\varepsilon$)} \\
> \ddot\varepsilon - \frac{g}{a}\,\varepsilon &= 0 \quad &\text{(substitute in the equation of motion of Section 6: linearized)} \\
> \varepsilon &= e^{q t} \quad &\text{(trial solution of a linear equation with constant coefficients)} \\
> q^2 e^{q t} - \frac{g}{a}\,e^{q t} &= 0 \quad &\text{(substitute the trial solution)} \\
> q^2 - \frac{g}{a} &= 0 \quad &\text{(characteristic equation; $e^{q t} \neq 0$)} \\
> q &= \pm\sqrt{g/a} \quad &\text{(one root is positive: a small departure grows exponentially, unstable)} \\
> \dot\theta^2 &= \frac{2g}{a}\left(1 - \sin\theta\right) \quad &\text{(first row with $K = g/a$)} \\
> 1 - \sin\left(\frac{\pi}{2} + \varepsilon\right) &= 1 - \cos\varepsilon \quad &\text{(sine of a sum: $\sin(\pi/2 + \varepsilon) = \cos\varepsilon$)} \\
> &\approx \tfrac12\,\varepsilon^2 \quad &\text{(Taylor expansion of $\cos\varepsilon$ to second order)} \\
> \dot\varepsilon^2 &\approx \frac{g}{a}\,\varepsilon^2 \quad &\text{(substitute; $\dot\theta = \dot\varepsilon$)} \\
> \dot\varepsilon &= -\sqrt{g/a}\,\varepsilon \quad &\text{(approach: $\lvert\varepsilon\rvert$ decreases, from either side; the negative root $q$)} \\
> \int_{\varepsilon_1}^{\varepsilon}\frac{d\varepsilon'}{\varepsilon'} &= -\sqrt{g/a}\int_{t_1}^{t} dt' \quad &\text{(separate variables and integrate)} \\
> \Big[\ln\lvert\varepsilon'\rvert\Big]_{\varepsilon_1}^{\varepsilon} &= -\sqrt{g/a}\,\Big[t'\Big]_{t_1}^{t} \quad &\text{(antiderivatives; $\varepsilon$ keeps its sign)} \\
> \ln\lvert\varepsilon\rvert - \ln\lvert\varepsilon_1\rvert &= -\sqrt{g/a}\,\left(t - t_1\right) \quad &\text{(Barrow's rule on both sides)} \\
> t - t_1 &= \sqrt{a/g}\,\ln\frac{\lvert\varepsilon_1\rvert}{\lvert\varepsilon\rvert} \quad &\text{(solve for the time)} \\
> t - t_1 &\to \infty \ \text{as}\ \varepsilon \to 0 \quad &\text{(the logarithm diverges: the highest point is reached only in infinite time)}
> \end{aligned}$$
>
> $$\boxed{\dot\theta^2 = 2K - \frac{2g}{a}\sin\theta \geq 0:\quad aK/g > 1 \ \text{revolutions};\quad -1 < aK/g < 1 \ \text{oscillations between the two roots of } \sin\theta_* = aK/g;\quad aK/g = -1 \ \text{rest at the bottom};\quad aK/g = 1 \ \text{unstable equilibrium at } \theta = \pi/2 \ (q = \pm\sqrt{g/a}),\ \text{approached in infinite time}}$$
>
> **Units:** $\mathrm{s^{-2}}$ in the first row; $aK/g$ and $\varepsilon$ dimensionless (radians); $q$ in $\mathrm{s^{-1}}$ and $\sqrt{a/g}$ in $\mathrm s$, as $\sqrt{\mathrm m/(\mathrm{m\,s^{-2}})}$
> **Meaning:** with $aK/g$ above one the rate never vanishes and the particle goes round the circle for ever, fastest at the bottom; between minus one and one it swings about the lowest point between the two angles where the sine equals $aK/g$, where its rate vanishes and its tangential acceleration sends it back; values of $aK/g$ below minus one are impossible. The value one separates both classes: the particle then tends to the highest point with vanishing speed. That point is an equilibrium, and an unstable one, because the linearized equation has a positive root, so any small departure grows exponentially; and the particle never reaches it, because the time needed grows like the logarithm of the inverse of the remaining departure. No integration of the motion in time was needed for this discussion.

### Final comments

New knowledge and abilities build on previous ones, "standing on the shoulders of giants", and the course is difficult if the mathematical tools are not mastered (Notes.pdf, Sec. 7.8). The notes list the essential skills, to be reviewed until one is totally confident with them:

| Area | Skills | Source |
| :--- | :--- | :--- |
| linear algebra | vector operations and projections; expressing vectors in any basis and transforming between bases; projecting any vector in a three-dimensional orthogonal basis with the sine and cosine of the relevant angles | Notes.pdf, Sec. 7.8 |
| equations | manipulating and rearranging systems of equations; trigonometric and hyperbolic relations; complex exponentials | Notes.pdf, Sec. 7.8 |
| calculus | differentiating any expression; changes of variable and integration by parts for immediate integrals; linear ordinary differential equations with constant coefficients | Notes.pdf, Sec. 7.8 |
| curve sketching | plotting a function of one variable faithfully, with its maxima, minima, zeros, asymptotes and behaviour at infinity | Notes.pdf, Sec. 7.8 |

> [!key] Summary of Topic 3
> - Simple constraints are stationary surfaces and curves; each independent constraint equation removes one configuration degree of freedom: two remain on a surface, one on a curve. The course parametrizes the constraint with as many generalized coordinates as degrees of freedom, so the constraint equations hold identically (Sections 1 to 3).
> - A curve or a surface may be given in parametric or implicit form. The partial derivatives of the parametric form are tangent vectors; the gradient of each implicit equation is a normal vector; the cross product turns two tangents into a normal of a surface, or two normals into the tangent of a curve. These local bases are in general neither unitary nor orthogonal (Section 4).
> - A smooth constraint acts through a reaction in its normal subspace, with one unknown component for a surface and two for a curve, so Newton's three scalar equations always close the problem. Projecting the second law on the tangent directions gives the equations of motion free of the reaction; projecting on the normal directions gives the reaction afterwards; in path variables these are the tangential, normal and binormal equations (Sections 5 and 6).
> - The reaction of a smooth stationary constraint has zero power, so it does not decide whether the mechanical energy is conserved; a moving constraint can work, as the spool shows. A unilateral constraint stops acting when its normal force vanishes, as at the lift-off of an airplane (Section 5).
> - A constraint between particles, such as a string over pulleys, may work on each particle but, if it does not depend on time, only transfers energy between them (Section 7).
> - Coulomb friction is bounded by the friction coefficient times the normal reaction: while the particle sticks it is an unknown tangential reaction that does no work; while it slides it is an applied force opposed to the relative velocity, with the saturated magnitude, that dissipates energy. The problem switches between the two formulations when the bound is reached and when the relative velocity vanishes (Section 8).
> - The Newtonian procedure: understand the problem and count the degrees of freedom; select the coordinates; define the frames and express every basis; obtain the kinematics; define the applied, reaction and, in a non-inertial frame only, inertia forces; project the second law, add the constraints and check that equations and unknowns match; integrate, uncouple or reduce to quadratures and discuss the regions of existence (Section 9).
