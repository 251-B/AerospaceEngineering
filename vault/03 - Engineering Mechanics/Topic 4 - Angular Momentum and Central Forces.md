---
title: "Topic 4 - Angular Momentum and Central Forces"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-4
  - point-particle
  - angular-momentum
  - torque
  - central-forces
  - kepler-problem
  - conic-orbits
  - vis-viva
---

# Topic 4 - Angular Momentum and Central Forces

> The angular momentum of a particle about a point is the moment of its linear momentum, and its rate of change about a fixed point is the moment of the resultant force: a consequence of Newton's second law that adds no new information but often reveals the nature of the motion. When the force always points along the line to a fixed centre its moment about that centre vanishes, so the angular momentum is a constant vector, the motion is planar and the radius sweeps equal areas in equal times. For the inverse-square attraction of gravity the radial equation becomes, in the variable one over the distance, a harmonic oscillator in the polar angle: the orbits are conic sections with the attracting body at a focus, the square of the period of an ellipse is proportional to the cube of its semi-major axis, and the mechanical energy, fixed by the semi-major axis alone, gives the speed at every distance.

This note follows `Notes.pdf` Section 4.8 (Angular momentum and torque, Eqs. 4.48 to 4.55) with Section 4.8.1 (Central force motion, Eqs. 4.56 to 4.58 and the five properties listed after them), and Chapter 8 (Orbital mechanics: Kepler's problem, Eqs. 8.1 to 8.21: Kepler's laws, kinematics, dynamics, the proof of Kepler's laws and the vis-viva equation), with the deck of Lecture 4 (Angular momentum and torque, Slides 1 to 17), in the order of the notes; the slides on the torques of a pair of particles, on systems of particles, on the worked example and on the two-body reduction (Slides 3, 5, 6, 9 and 10) are placed where the notes discuss the same ideas. The effective potential of a central force, the radial band it allows and the discussion of whether a particle can reach the centre are extensions, built on the regions of existence of Notes.pdf, Sec. 7.7; they are marked as such. Earlier results are cited, not re-derived: the change of basis (Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.20), the dot product (Notes.pdf, Eq. 1.24), the cross product and its magnitude, the area of a parallelogram (Notes.pdf, Eq. 1.30), its anticommutativity (Notes.pdf, Eq. 1.31) and linearity (Notes.pdf, Eq. 1.32), the triple product (Notes.pdf, Eq. 1.33), the derivative of a unit vector of a rotating basis (Notes.pdf, Eq. 1.62), the rules of vector differentiation (Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.66; Notes.pdf, Eq. 1.67), the velocity and acceleration (Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4) and their Cartesian form (Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.7), the cylindrical basis and its derivatives (Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26), the linear momentum and the kinetic energy (Notes.pdf, Eq. 4.1; Notes.pdf, Eq. 4.2), Newton's laws (Notes.pdf, Sec. 4.2; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 4.4), the potential energy (Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.20), the allowed regions (Notes.pdf, Eq. 4.28) and the conservation of mechanical energy (Notes.pdf, Eq. 4.31).
See also [[Concept - Angular Momentum Vector and Torque of Forces]], [[Concept - Differential Equation of Angular Momentum with Moving Origins]], [[Concept - Conservation Laws and Planar Character of Central Force Fields]], [[Concept - Kepler Laws and Barycentric Two-Body Reduction]], [[Concept - Binet Equation and Conic Section Trajectories]], [[Concept - Vis-Viva Energy Integral and Orbital Velocities]] and [[Formula Sheet - Topic 4 Angular Momentum]].

| Symbol | Meaning |
| :--- | :--- |
| $S_0 : \{O;\mathcal B_0\}$, $\mathcal B_0 : \{\mathbf i,\mathbf j,\mathbf k\}$ | inertial reference frame, its origin and its basis; axes $Ox$, $Oy$, $Oz$ |
| $x, y, z$ | Cartesian coordinates of a point in $S_0$ (in Sections 7 and 8, Cartesian coordinates in the plane of the orbit about $C$) |
| $P$, $m$ | the point particle and its mass (the slides write $m_P$ or $m^P$; the example of [Lecture 4, Slide 6] calls the particle $M$) |
| $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf a_0^P$; $v$ | position, velocity and acceleration of $P$ with respect to $S_0$ (Topic 1); $v$ is the speed |
| $\mathbf p_0$ | linear momentum of $P$ in $S_0$ (Notes.pdf, Eq. 4.1); not to be confused with the semi-parameter $p$ |
| $A$, $B$ | arbitrary points used as poles (centres of moments); $\mathbf r_0^A$, $\mathbf v_0^A$, $\mathbf a_0^A$ the position, velocity and acceleration of $A$ in $S_0$ |
| $\mathbf r_A^P$ | position of $P$ relative to $A$, the vector $\overrightarrow{AP}$ (Eq. 4.48) |
| $S_A : \{A;\mathcal B_0\}$; $\mathbf v_A^P$, $\mathbf a_A^P$ | frame with origin $A$ and axes parallel to those of $S_0$ (non-rotating); velocity and acceleration of $P$ relative to it (Eq. 4.54) |
| $\mathbf H_{A,0}$; $\mathbf H_{A,A}$ | angular momentum of $P$ about $A$ as seen from $S_0$ (the slides write $\mathbf H_{A0}^P$); the same as seen from $S_A$ (Eq. 4.55) |
| $\mathbf F$; $\mathbf M_A$ | resultant force on $P$; its moment, or torque, about $A$ (Eq. 4.51) |
| $Q$, $m_Q$; $\mathbf F_P$, $\mathbf F_Q$ | a second particle and its mass; the force of $Q$ on $P$ and the force of $P$ on $Q$ ([Lecture 4, Slide 3]) |
| $P_n$, $m_n$, $\mathbf F_n$ | the particles of a system ($n$ from $1$ to $N$), their masses and the external forces on them; $\mathbf f_{nl}$ the internal force of $P_l$ on $P_n$ (Notes.pdf, Eq. 12.1 writes $\mathbf f^{P_n}_{P_l}$) |
| $\mathbf H_{A,0}^{\mathrm{sys}}$, $\mathbf M_A^{\mathrm{ext}}$ | total angular momentum of the system about $A$ and the total moment of the external forces about $A$ |
| $\mathbf u$ | a fixed unit vector of $S_0$ (a constant direction) |
| $\Omega$, $g$ | constant of the attraction of [Lecture 4, Slide 6], whose square is the force per unit mass and per unit distance (the slide writes $k$, a letter kept here for the unit vector $\mathbf k$); acceleration of gravity |
| $F$; $f$ | radial component of a central force (Eq. 4.56); the same per unit mass (Section 10) |
| $r$, $\theta$ | polar coordinates of $P$ in the plane of motion: distance to the centre of force and polar angle (Notes.pdf, Sec. 4.8.1 writes $R$, Chapter 8 writes $r$) |
| $\mathcal B_1 : \{\mathbf e_r,\mathbf e_\theta,\mathbf k\}$, $S_1$; $[{}_0R_1]$ | polar basis of $P$ (Eq. 8.2, with $\mathbf e_z$ equal to $\mathbf k$), the frame with origin at the centre that turns with the radius, and the change of basis matrix from $\mathcal B_1$ to $\mathcal B_0$ |
| $\boldsymbol\omega_{10}$ | angular velocity of $S_1$ with respect to $S_0$ |
| $h$, $\mathbf h$ | magnitude of the mass-specific angular momentum about the centre and the vector itself (Eq. 8.7) |
| $\mathcal A$, $\mathcal A_e$ | area swept by the radius of $P$ and area of an elliptic orbit (the notes write $A$ and $A_e$, the slides $A$) |
| $T_0$, $V_0$, $E_0$; $\xi$ | kinetic, potential and mechanical energy of $P$ in $S_0$ (Topic 2); mass-specific mechanical energy (Eq. 8.19) |
| $C$, $m_C$ | the attracting body of Kepler's problem and its mass (the Earth in the notes, which call it $O$; the Sun $S$ with mass $m^S$ in the slides) |
| $Z$; $S_Z$, $S_C$ | barycentre of $P$ and $C$ (the slides write $G$, a letter kept here for the constant of gravitation); frames with origin at $Z$ and at $C$ and axes parallel to those of $S_0$ ([Lecture 4, Slides 9 and 10] write $S_G$ and $S_S$) |
| $G$, $\mu$ | constant of universal gravitation; gravitational parameter (Eq. 8.1, [Lecture 4, Slide 10]) |
| $\mathbf r$, $r$ | position of $P$ relative to $C$, the vector $\overrightarrow{CP}$, and its magnitude ([Lecture 4, Slide 10]); in Chapter 8 the notes write $\mathbf r_0^P$ |
| $e$, $\psi$; $c_1$, $c_2$ | eccentricity and phase, the two constants of the orbit equation (Eq. 8.13); constants of the homogeneous solution of the orbit equation |
| $p$; $a$, $b$; $r_p$, $r_a$ | semi-parameter of the conic; semi-major and semi-minor axes; pericentre and apocentre distances (Eq. 8.15) |
| $\tau$ | period of an elliptic orbit (Eq. 8.18) |
| $v_c$, $v_e$, $v_p$, $v_a$ | circular velocity, escape velocity, speeds at the pericentre and at the apocentre (Eqs. 8.20 and 8.21, [Lecture 4, Slide 16]) |
| $v_{\mathrm{eff}}$; $r_c$, $\varepsilon$, $q$; $\kappa$ | mass-specific effective potential of a central force (extension); radius of a circular orbit, small departure from it and root of its characteristic equation; constant of the inverse-cube attraction of the counterexample (extension) |
| $K_1, \dots, K_6$; $\mathbf u_1$ | constants of the solutions of the example of [Lecture 4, Slide 6]; unit vector of the plane of its orbit |
| $\lambda$; $t'$, $r'$, $\theta'$, $\phi$ | root of a characteristic equation; integration (dummy) variables |

## 1. Angular momentum and torque

The fundamental quantity of the linear motion of a particle is its linear momentum; the fundamental quantity of its rotational motion about a point $A$ is the moment of that momentum about $A$, the angular momentum (Notes.pdf, Sec. 4.8; [Lecture 4, Slide 3]). It is defined about an arbitrary point, which may move, and as seen from a given reference frame: its value depends on both, on the point because the arm of the moment changes with it, and on the frame because the velocity does ([Lecture 4, Slide 3]). When needed, a superscript names the particle: the slides write $\mathbf H_{A0}^P$.

![[attachments/EM-T/t4-angular-momentum.svg]]

> [!derivation] Angular momentum of a particle about a point
> **Law:** definition of the angular momentum as the moment of the linear momentum; the cross product is perpendicular to both factors
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.1; Notes.pdf, Eq. 1.33; Notes.pdf, Sec. 1.6.2; [Lecture 4, Slide 3]
>
> $\mathbf r_A^P$ goes from $A$ to $P$, so it is the position of $P$ minus the position of $A$, both measured from $O$ (Notes.pdf Fig. 4.5).
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^P \quad &\text{(linear momentum, Eq. 4.1)} \\
> \mathbf r_A^P &= \mathbf r_0^P - \mathbf r_0^A \quad &\text{($\overrightarrow{OA} + \overrightarrow{AP} = \overrightarrow{OP}$)} \\
> \mathbf H_{A,0} &= \mathbf r_A^P\times\mathbf p_0 \quad &\text{(moment of $\mathbf p_0$ about $A$)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf v_0^P \quad &\text{(substitute the two rows above)} \\
> \mathbf r_A^P\cdot\mathbf H_{A,0} &= m\,\mathbf r_A^P\cdot\left(\mathbf r_A^P\times\mathbf v_0^P\right) \quad &\text{(dot-multiply by the arm)} \\
> &= m\,\mathbf v_0^P\cdot\left(\mathbf r_A^P\times\mathbf r_A^P\right) \quad &\text{(cyclic order of the triple product, Eq. 1.33)} \\
> &= 0 \quad &\text{($\mathbf r_A^P\times\mathbf r_A^P = \mathbf 0$, Sec. 1.6.2)} \\
> \mathbf v_0^P\cdot\mathbf H_{A,0} &= m\,\mathbf v_0^P\cdot\left(\mathbf r_A^P\times\mathbf v_0^P\right) \quad &\text{(dot-multiply by the velocity)} \\
> &= m\,\mathbf r_A^P\cdot\left(\mathbf v_0^P\times\mathbf v_0^P\right) \quad &\text{(cyclic order of the triple product, Eq. 1.33)} \\
> &= 0 \quad &\text{($\mathbf v_0^P\times\mathbf v_0^P = \mathbf 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = \mathbf r_A^P\times m\,\mathbf v_0^P = \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf v_0^P,\qquad \mathbf H_{A,0}\perp\mathbf r_A^P,\quad \mathbf H_{A,0}\perp\mathbf v_0^P}$$
>
> **Units:** $\mathrm m\cdot\mathrm{kg}\cdot\mathrm{m\,s^{-1}} = \mathrm{kg\,m^2\,s^{-1}}$, that is $[\mathrm{M\,L^2\,T^{-1}}]$
> **Meaning:** the angular momentum is perpendicular to the plane of the arm and the velocity, with the sense given by the right-hand rule from the arm to the velocity; it vanishes when $P$ moves along the line through $A$, since the cross product of parallel vectors is zero.

> [!derivation] How the angular momentum depends on the pole
> **Law:** definition of the angular momentum; addition of positions; linearity of the cross product
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 1.32; [Lecture 4, Slide 3]
>
> The slide states that the value depends on the point; the relation between two poles $A$ and $B$ is written out here for this note.
>
> $$\begin{aligned}
> \mathbf H_{B,0} &= \left(\mathbf r_0^P - \mathbf r_0^B\right)\times m\,\mathbf v_0^P \quad &\text{(Eq. 4.48 with the pole $B$)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A + \mathbf r_0^A - \mathbf r_0^B\right)\times m\,\mathbf v_0^P \quad &\text{(add and subtract $\mathbf r_0^A$)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf v_0^P + \left(\mathbf r_0^A - \mathbf r_0^B\right)\times m\,\mathbf v_0^P \quad &\text{(linearity, Eq. 1.32)} \\
> &= \mathbf H_{A,0} + \overrightarrow{BA}\times m\,\mathbf v_0^P \quad &\text{(Eq. 4.48 with the pole $A$; $\mathbf r_0^A - \mathbf r_0^B$ goes from $B$ to $A$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{B,0} = \mathbf H_{A,0} + \overrightarrow{BA}\times m\,\mathbf v_0^P}$$
>
> **Units:** $\mathrm{kg\,m^2\,s^{-1}}$ in every term
> **Meaning:** changing the pole adds the moment about $B$ of the momentum placed at $A$; the angular momentum is the same about every point of the line through $A$ parallel to the velocity, where the added cross product vanishes.

The torque, or moment of a force about a point, is defined in the same way with the force in place of the momentum ([Lecture 4, Slide 3]; Notes.pdf, Eq. 4.51). Like the angular momentum it is a vector, it depends on the point, and it is the moment of the force about that point.

> [!derivation] Torque of a force about a point
> **Law:** definition of the moment of a force; Newton's second law for the resultant force
> **Source:** Notes.pdf, Eq. 4.51; Notes.pdf, Eq. 4.4; [Lecture 4, Slide 3]
>
> $$\begin{aligned}
> \mathbf M_A &= \mathbf r_A^P\times\mathbf F \quad &\text{(moment of the resultant force about $A$)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A\right)\times\mathbf F \quad &\text{($\mathbf r_A^P = \mathbf r_0^P - \mathbf r_0^A$)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf a_0^P \quad &\text{(second law, $\mathbf F = m\,\mathbf a_0^P$, Eq. 4.4)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_A = \mathbf r_A^P\times\mathbf F = \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf a_0^P}$$
>
> **Units:** $\mathrm m\cdot\mathrm N = \mathrm{N\,m} = \mathrm{kg\,m^2\,s^{-2}}$, that is $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the torque is perpendicular to the arm and to the force; it vanishes when the line of action of the force passes through $A$. The same steps as in the previous box show that changing the pole from $A$ to $B$ adds the moment about $B$ of the force placed at $A$.

If a particle $Q$ causes a torque on $P$ about $A$, then $P$ causes the opposite torque on $Q$ about the same point ([Lecture 4, Slide 3]). The slide writes this equality without its condition: it requires the two forces of the pair to share the same line of action, the line $PQ$, which is how the notes state Newton's third law for internal forces much later in the course (Notes.pdf, Eq. 12.1; Notes.pdf, Eq. 12.2). The box uses that condition.

![[attachments/EM-T/t4-torque-pair.svg]]

> [!derivation] The torques of an action-reaction pair cancel
> **Law:** Newton's third law with collinear forces; linearity of the cross product; cross product of parallel vectors
> **Source:** [Lecture 4, Slide 3]; Notes.pdf, Sec. 4.2; Notes.pdf, Eq. 12.1; Notes.pdf, Eq. 12.2; Notes.pdf, Eq. 1.32; Notes.pdf, Sec. 1.6.2
>
> $\mathbf F_P$ lies along the line $PQ$, so it is parallel to $\overrightarrow{QP}$.
>
> $$\begin{aligned}
> \mathbf F_Q &= -\mathbf F_P \quad &\text{(third law, Sec. 4.2 and Eq. 12.1)} \\
> \overrightarrow{AP}\times\mathbf F_P + \overrightarrow{AQ}\times\mathbf F_Q &= \overrightarrow{AP}\times\mathbf F_P - \overrightarrow{AQ}\times\mathbf F_P \quad &\text{(substitute $\mathbf F_Q$)} \\
> &= \left(\overrightarrow{AP} - \overrightarrow{AQ}\right)\times\mathbf F_P \quad &\text{(linearity, Eq. 1.32)} \\
> &= \overrightarrow{QP}\times\mathbf F_P \quad &\text{($\overrightarrow{AQ} + \overrightarrow{QP} = \overrightarrow{AP}$)} \\
> &= \mathbf 0 \quad &\text{($\mathbf F_P$ parallel to $\overrightarrow{QP}$, Sec. 1.6.2)}
> \end{aligned}$$
>
> $$\boxed{\overrightarrow{AP}\times\mathbf F_P = -\overrightarrow{AQ}\times\mathbf F_Q = -\overrightarrow{AQ}\times\left(-\mathbf F_P\right)}$$
>
> **Units:** $\mathrm{N\,m}$
> **Meaning:** internal torques cancel in pairs, whatever the pole; that is why torques are classified into internal and external with respect to the system analysed ([Lecture 4, Slide 3]). Without the collinearity the sum would be the moment of a couple, the cross product of $\overrightarrow{QP}$ with $\mathbf F_P$, which is not zero in general.

## 2. The rate of change of the angular momentum

Just as Newton's second law gives the evolution of the linear momentum, a differential equation gives the evolution of the angular momentum (Notes.pdf, Sec. 4.8; [Lecture 4, Slide 4]). It is obtained by differentiating the definition in $S_0$.

> [!derivation] Rate of change of the angular momentum about any point
> **Law:** product rule of the cross product; definition of velocity; Newton's second law; cross product of a vector with itself
> **Source:** Notes.pdf, Eq. 4.49; Notes.pdf, Eq. 4.50; Notes.pdf, Eq. 4.51; Notes.pdf, Eq. 4.52; Notes.pdf, Eq. 1.67; Notes.pdf, Eq. 1.32; Notes.pdf, Eq. 2.3; [Lecture 4, Slide 4]
>
> The derivative is taken in $S_0$; the mass is constant.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \frac{d}{dt}\left[\left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf v_0^P\right] \quad &\text{(derivative of Eq. 4.48)} \\
> &= \frac{d}{dt}\left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf v_0^P + \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\frac{d\mathbf v_0^P}{dt} \quad &\text{(product rule, Eq. 1.67)} \\
> &= \left(\mathbf v_0^P - \mathbf v_0^A\right)\times m\,\mathbf v_0^P + \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf a_0^P \quad &\text{(definitions of velocity and acceleration, Eqs. 2.3 and 2.4: Eq. 4.49)} \\
> &= \mathbf v_0^P\times m\,\mathbf v_0^P - \mathbf v_0^A\times m\,\mathbf v_0^P + \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf a_0^P \quad &\text{(linearity, Eq. 1.32)} \\
> &= \left(\mathbf r_0^P - \mathbf r_0^A\right)\times m\,\mathbf a_0^P - \mathbf v_0^A\times m\,\mathbf v_0^P \quad &\text{($\mathbf v_0^P\times\mathbf v_0^P = \mathbf 0$: Eq. 4.50)} \\
> &= \mathbf M_A - \mathbf v_0^A\times m\,\mathbf v_0^P \quad &\text{(torque of the resultant force, Eq. 4.51)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 = \mathbf M_A - \mathbf v_0^A\times m\,\mathbf v_0^P}$$
>
> **Units:** $\mathrm{kg\,m^2\,s^{-2}}$, the units of a torque, in every term (the last one is $\mathrm{m\,s^{-1}}\cdot\mathrm{kg\,m\,s^{-1}}$)
> **Meaning:** Eq. 4.52: the angular momentum about a moving point changes because of the torque and because the pole moves; the extra term is the cross product of the velocity of the pole with the linear momentum.

> [!derivation] The angular momentum theorem about a fixed point
> **Law:** Eq. 4.52 with a pole at rest in $S_0$, or moving parallel to $P$; projection on a fixed direction
> **Source:** Notes.pdf, Eq. 4.53; Notes.pdf, Eq. 4.52; Notes.pdf, Eq. 1.66; Notes.pdf, Sec. 4.8; [Lecture 4, Slide 4]
>
> Let $\mathbf u$ be a unit vector fixed in $S_0$, so that its derivative in $S_0$ is zero.
>
> $$\begin{aligned}
> \mathbf v_0^A &= \mathbf 0 \ \ \text{or}\ \ \mathbf v_0^A\parallel\mathbf v_0^P \ \Rightarrow\ \mathbf v_0^A\times m\,\mathbf v_0^P = \mathbf 0 \quad &\text{(cross product of zero or of parallel vectors)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \mathbf M_A \quad &\text{(Eq. 4.52 without its last term: Eq. 4.53)} \\
> \frac{d}{dt}\left(\mathbf H_{A,0}\cdot\mathbf u\right) &= \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0\cdot\mathbf u + \mathbf H_{A,0}\cdot\frac{d\mathbf u}{dt} \quad &\text{(product rule of the dot product, Eq. 1.66)} \\
> &= \mathbf M_A\cdot\mathbf u + 0 \quad &\text{(Eq. 4.53; $\mathbf u$ is fixed in $S_0$)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 = \mathbf M_A\ \ (A\ \text{fixed in}\ S_0),\qquad \frac{d}{dt}\left(\mathbf H_{A,0}\cdot\mathbf u\right) = \mathbf M_A\cdot\mathbf u}$$
>
> **Units:** $\mathrm{N\,m}$ on both sides
> **Meaning:** the rate of change of the angular momentum about a fixed point equals the torque of the resultant force about it, the rotational analogue of Newton's second law. It is derived from the second law, so it adds no new information about the motion; it is often easier or more enlightening to use (Notes.pdf, Sec. 4.8; [Lecture 4, Slide 4]). Projected on the three vectors of any basis it gives three scalar equations; if the torque has no component along a fixed direction, the component of the angular momentum along that direction stays constant.

When the pole moves, it is sometimes useful to work in the auxiliary frame $S_A$, with origin at $A$ and its axes parallel to those of $S_0$, so that it does not rotate (Notes.pdf, Sec. 4.8; Notes.pdf Fig. 4.5).

> [!derivation] Angular momentum about a moving point in the parallel frame
> **Law:** composition of positions with a non-rotating frame; Eq. 4.52; definition of the relative angular momentum
> **Source:** Notes.pdf, Eq. 4.54; Notes.pdf, Eq. 4.55; Notes.pdf, Eq. 4.52; Notes.pdf, Eq. 1.32; Notes.pdf, Eq. 1.67
>
> $S_A$ uses the basis $\mathcal B_0$, which is fixed in both frames, so the time derivative of a vector written in $\mathcal B_0$ is the same in $S_0$ and in $S_A$: no rotation enters the transformation.
>
> $$\begin{aligned}
> \mathbf r_0^P &= \mathbf r_0^A + \mathbf r_A^P \quad &\text{(position of $P$ through the origin of $S_A$)} \\
> \mathbf v_0^P &= \mathbf v_0^A + \mathbf v_A^P \quad &\text{(time derivative; the same derivative in $S_0$ and $S_A$)} \\
> \mathbf a_0^P &= \mathbf a_0^A + \mathbf a_A^P \quad &\text{(time derivative again)} \\
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \mathbf r_A^P\times m\,\mathbf a_0^P - \mathbf v_0^A\times m\,\mathbf v_0^P \quad &\text{(Eq. 4.50 with $\mathbf r_A^P = \mathbf r_0^P - \mathbf r_0^A$)} \\
> &= \mathbf r_A^P\times m\left(\mathbf a_0^A + \mathbf a_A^P\right) - \mathbf v_0^A\times m\left(\mathbf v_0^A + \mathbf v_A^P\right) \quad &\text{(substitute the composed velocity and acceleration)} \\
> &= \mathbf r_A^P\times m\left(\mathbf a_0^A + \mathbf a_A^P\right) - \mathbf v_0^A\times m\,\mathbf v_A^P \quad &\text{(linearity; $\mathbf v_0^A\times\mathbf v_0^A = \mathbf 0$: Eq. 4.54)} \\
> \mathbf H_{A,A} &= \mathbf r_A^P\times m\,\mathbf v_A^P \quad &\text{(angular momentum about $A$ as seen from $S_A$)} \\
> \left.\frac{d\mathbf H_{A,A}}{dt}\right|_A &= \mathbf v_A^P\times m\,\mathbf v_A^P + \mathbf r_A^P\times m\,\mathbf a_A^P \quad &\text{(product rule in $S_A$, Eq. 1.67)} \\
> &= \mathbf r_A^P\times m\,\mathbf a_A^P \quad &\text{($\mathbf v_A^P\times\mathbf v_A^P = \mathbf 0$)} \\
> \mathbf M_A &= \mathbf r_A^P\times m\,\mathbf a_0^P \quad &\text{(Eq. 4.51)} \\
> &= \mathbf r_A^P\times m\,\mathbf a_A^P \quad &\text{(if $\mathbf a_0^A = \mathbf 0$: $\mathbf a_0^P = \mathbf a_A^P$)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 = \mathbf r_A^P\times m\left(\mathbf a_0^A + \mathbf a_A^P\right) - \mathbf v_0^A\times m\,\mathbf v_A^P;\qquad \mathbf a_0^A = \mathbf 0:\ \ \mathbf r_A^P\times m\,\mathbf a_A^P = \left.\frac{d\mathbf H_{A,A}}{dt}\right|_A = \mathbf M_A}$$
>
> **Units:** $\mathrm{N\,m}$ in every term
> **Meaning:** Eq. 4.55: if the pole moves with constant velocity, the torque about it equals the rate of change of the angular momentum relative to the parallel frame $S_A$, which is then inertial (Notes.pdf, Sec. 4.2). The quantities of this chapter, the linear momentum, the energies and the angular momentum, depend in general on the frame of the analysis, and a potential may exist in some frames and not in others (Notes.pdf, Sec. 4.8).

## 3. Conservation of the angular momentum

The angular momentum of a particle about a fixed point is conserved if the net torque about that point is zero ([Lecture 4, Slide 5]). Being a vector, its conservation amounts to three scalar conservation laws.

> [!derivation] Conservation of the angular momentum of a particle
> **Law:** the angular momentum theorem about a fixed point; integration in time with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.53; [Lecture 4, Slide 5]
>
> $A$ is fixed in $S_0$ and the torque about it is zero at every instant.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf H_{A,0}}{dt}\right|_0 &= \mathbf M_A \quad &\text{(Eq. 4.53)} \\
> &= \mathbf 0 \quad &\text{(zero torque at every instant)} \\
> \int_0^t \left.\frac{d\mathbf H_{A,0}}{dt'}\right|_0 dt' &= \int_0^t \mathbf 0\,dt' \quad &\text{(integrate from $0$ to $t$, component by component in $\mathcal B_0$)} \\
> \Big[\mathbf H_{A,0}\Big]_0^t &= \mathbf 0 \quad &\text{(antiderivative of a derivative; the integral of zero is zero)} \\
> \mathbf H_{A,0}(t) - \mathbf H_{A,0}(0) &= \mathbf 0 \quad &\text{(Barrow's rule: $F(t) - F(0)$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf M_A = \mathbf 0\ \Rightarrow\ \mathbf H_{A,0}(t) = \mathbf H_{A,0}(0) = \text{const}}$$
>
> **Units:** $\mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** the three components of the angular momentum in $\mathcal B_0$ are constants of the motion, fixed by the initial position and velocity. The torque must vanish about the same fixed point at every instant; if only one component of the torque vanishes, only the corresponding component of the angular momentum is conserved (Section 2).

The slide extends the statement to a system of analysis: the total angular momentum about a fixed point is constant if the net external torque about it is zero, and an isolated system satisfies this condition ([Lecture 4, Slide 5]). The box proves it for a system of particles, with internal forces that are equal, opposite and collinear (Notes.pdf, Eq. 12.1).

> [!derivation] Conservation of the total angular momentum of a system of particles
> **Law:** the angular momentum theorem for each particle; the internal torques cancel in pairs
> **Source:** [Lecture 4, Slide 5]; [Lecture 4, Slide 3]; Notes.pdf, Eq. 4.53; Notes.pdf, Eq. 12.1; Notes.pdf, Eq. 12.2
>
> Each particle $P_n$ feels the external force $\mathbf F_n$ and the internal forces of the other particles; $A$ is fixed in $S_0$.
>
> $$\begin{aligned}
> \mathbf H_{A,0}^{\mathrm{sys}} &= \sum_{n=1}^{N}\overrightarrow{AP_n}\times m_n\,\mathbf v_0^{P_n} \quad &\text{(sum of the angular momenta, Eq. 4.48 for each particle)} \\
> \left.\frac{d\mathbf H_{A,0}^{\mathrm{sys}}}{dt}\right|_0 &= \sum_{n=1}^{N}\overrightarrow{AP_n}\times\Big(\mathbf F_n + \sum_{l\neq n}\mathbf f_{nl}\Big) \quad &\text{(Eq. 4.53 for each particle, with its resultant force)} \\
> &= \sum_{n=1}^{N}\overrightarrow{AP_n}\times\mathbf F_n + \sum_{n=1}^{N}\sum_{l\neq n}\overrightarrow{AP_n}\times\mathbf f_{nl} \quad &\text{(linearity, Eq. 1.32)} \\
> \overrightarrow{AP_n}\times\mathbf f_{nl} + \overrightarrow{AP_l}\times\mathbf f_{ln} &= \mathbf 0 \quad &\text{(each pair, previous section; Eq. 12.2)} \\
> \left.\frac{d\mathbf H_{A,0}^{\mathrm{sys}}}{dt}\right|_0 &= \mathbf M_A^{\mathrm{ext}} \quad &\text{(the double sum is a sum of such pairs)} \\
> \mathbf M_A^{\mathrm{ext}} = \mathbf 0\ &\Rightarrow\ \mathbf H_{A,0}^{\mathrm{sys}} = \text{const} \quad &\text{(integrate as in the previous box)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf H_{A,0}^{\mathrm{sys}}}{dt}\right|_0 = \mathbf M_A^{\mathrm{ext}},\qquad \mathbf M_A^{\mathrm{ext}} = \mathbf 0\ \Rightarrow\ \mathbf H_{A,0}^{\mathrm{sys}} = \text{const}}$$
>
> **Units:** $\mathrm{N\,m}$; $\mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** only the external torques change the total angular momentum; an isolated system has no external forces, so its total angular momentum about any fixed point is constant ([Lecture 4, Slide 5]). The angular momentum of each particle may still change, the internal torques transferring it between them.

### Worked example: a particle attracted by a point and by gravity

> [!example] A heavy particle attracted to a point ([Lecture 4, Slide 6])
> A force attracts a heavy particle $P$ of mass $m$ to a point $O$; the attractive force is proportional to the mass of the particle and to the distance $OP$, with proportionality coefficient $\Omega^2$. The coordinate system $Oxyz$ has its origin at the centre of attraction $O$ and the axis $Oz$ vertical. Its initial position and velocity are given in the table. The slide gives the statement, a sketch with a point $A$ marked below $O$ on the vertical, and the three equations of motion; this note derives them, shows that the resultant force is central about $A$, so that the angular momentum about $A$ is conserved, and integrates the motion.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial, origin at $O$, $\mathbf k$ vertical upwards |
> | attraction | magnitude $m\,\Omega^2\,OP$, directed from $P$ to $O$; $\Omega$ in $\mathrm{s^{-1}}$ |
> | gravity | $\mathbf g = -g\,\mathbf k$ |
> | initial position | $x(0) = \sqrt3\,g/\Omega^2$, $y(0) = 0$, $z(0) = 0$ |
> | initial velocity | $\dot x(0) = 0$, $\dot y(0) = 2g/\Omega$, $\dot z(0) = 0$ |
> | degrees of freedom | three, the Cartesian coordinates $x$, $y$, $z$ (no constraint) |

![[attachments/EM-T/t4-attraction-example.svg]]

> [!derivation] Forces and equations of motion of the attracted particle
> **Law:** position, velocity and acceleration in the fixed Cartesian basis; Newton's second law projected on $\mathcal B_0$
> **Source:** [Lecture 4, Slide 6]; Notes.pdf, Eq. 2.5; Notes.pdf, Eq. 2.7; Notes.pdf, Eq. 4.4
>
> The attraction points from $P$ to $O$, opposite to $\mathbf r_0^P$, and its magnitude is $m\,\Omega^2$ times the distance, which is the magnitude of $\mathbf r_0^P$.
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(Eq. 2.5)} \\
> \mathbf a_0^P &= \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k \quad &\text{(Eq. 2.7: the basis of $S_0$ is fixed)} \\
> \mathbf F &= -m\,\Omega^2\,\mathbf r_0^P - m g\,\mathbf k \quad &\text{(attraction towards $O$ plus the weight)} \\
> &= -m\,\Omega^2 x\,\mathbf i - m\,\Omega^2 y\,\mathbf j - \left(m g + m\,\Omega^2 z\right)\mathbf k \quad &\text{(components in $\mathcal B_0$)} \\
> m\ddot x &= -m\,\Omega^2 x \quad &\text{(second law along $\mathbf i$, Eq. 4.4)} \\
> m\ddot y &= -m\,\Omega^2 y \quad &\text{(second law along $\mathbf j$)} \\
> m\ddot z &= -m g - m\,\Omega^2 z \quad &\text{(second law along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\ddot x = -\Omega^2 x,\qquad \ddot y = -\Omega^2 y,\qquad \ddot z = -g - \Omega^2 z}$$
>
> **Units:** $\mathrm{m\,s^{-2}}$ in every term ($\Omega^2$ in $\mathrm{s^{-2}}$ times a length)
> **Meaning:** the three equations of the slide; the mass cancels and the three coordinates are uncoupled. The weight only adds a constant to the vertical equation.

> [!derivation] The resultant force is central about the point A
> **Law:** the resultant force rewritten about the point where it vanishes; torque about that point; conservation of the angular momentum
> **Source:** [Lecture 4, Slide 6]; Notes.pdf, Eq. 4.51; Notes.pdf, Eq. 4.53; Notes.pdf, Sec. 1.6.2
>
> The point $A$ of the sketch lies on the vertical through $O$, below it; its position is found as the point where the resultant force would vanish.
>
> $$\begin{aligned}
> \mathbf F &= -m\,\Omega^2\left(\mathbf r_0^P + \frac{g}{\Omega^2}\,\mathbf k\right) \quad &\text{(factor $-m\,\Omega^2$ in the force of the previous box)} \\
> \mathbf r_0^A &= -\frac{g}{\Omega^2}\,\mathbf k \quad &\text{(definition of $A$: the bracket is $\mathbf r_0^P - \mathbf r_0^A$)} \\
> \mathbf F &= -m\,\Omega^2\,\mathbf r_A^P \quad &\text{($\mathbf r_A^P = \mathbf r_0^P - \mathbf r_0^A$)} \\
> \mathbf M_A &= \mathbf r_A^P\times\left(-m\,\Omega^2\,\mathbf r_A^P\right) \quad &\text{(torque about $A$, Eq. 4.51)} \\
> &= -m\,\Omega^2\,\mathbf r_A^P\times\mathbf r_A^P \quad &\text{(take out the scalar)} \\
> &= \mathbf 0 \quad &\text{(cross product of a vector with itself)} \\
> \mathbf H_{A,0} &= \text{const} \quad &\text{($A$ is fixed in $S_0$: Eq. 4.53 and Section 3)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^A = -\frac{g}{\Omega^2}\,\mathbf k,\qquad \mathbf F = -m\,\Omega^2\,\overrightarrow{AP},\qquad \mathbf M_A = \mathbf 0,\qquad \mathbf H_{A,0} = \text{const}}$$
>
> **Units:** $g/\Omega^2$ in $\mathrm{m\,s^{-2}}/\mathrm{s^{-2}} = \mathrm m$; $\mathbf F$ in $\mathrm N$
> **Meaning:** the attraction towards $O$ and the weight add up to a single attraction towards $A$, the equilibrium point, where the attraction balances the weight; it lies below $O$ at the depth $g$ divided by the square of $\Omega$. The motion is a central force motion about $A$, so the angular momentum about $A$ is conserved, while the angular momentum about $O$ is not, because the weight has a torque about $O$.

> [!derivation] The angular momentum about A and about O
> **Law:** definition of the angular momentum at the initial instant; torque of the weight about $O$; conservation of a component
> **Source:** Notes.pdf, Eq. 4.48; Notes.pdf, Eq. 4.51; Notes.pdf, Eq. 4.53; Notes.pdf, Eq. 1.32
>
> The products of the unit vectors follow the right-hand rule in $\mathcal B_0$: $\mathbf i\times\mathbf j$ is $\mathbf k$ and $\mathbf k\times\mathbf j$ is $-\mathbf i$.
>
> $$\begin{aligned}
> \mathbf r_A^P(0) &= \frac{\sqrt3\,g}{\Omega^2}\,\mathbf i + \frac{g}{\Omega^2}\,\mathbf k \quad &\text{($\mathbf r_0^P(0) - \mathbf r_0^A$)} \\
> \mathbf H_{A,0} &= \left(\frac{\sqrt3\,g}{\Omega^2}\,\mathbf i + \frac{g}{\Omega^2}\,\mathbf k\right)\times m\,\frac{2g}{\Omega}\,\mathbf j \quad &\text{(Eq. 4.48 at $t = 0$; conserved, previous box)} \\
> &= \frac{2\sqrt3\,m g^2}{\Omega^3}\,\mathbf i\times\mathbf j + \frac{2 m g^2}{\Omega^3}\,\mathbf k\times\mathbf j \quad &\text{(distribute, Eq. 1.32)} \\
> &= \frac{2\sqrt3\,m g^2}{\Omega^3}\,\mathbf k - \frac{2 m g^2}{\Omega^3}\,\mathbf i \quad &\text{($\mathbf i\times\mathbf j = \mathbf k$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \lvert\mathbf H_{A,0}\rvert &= \frac{2 m g^2}{\Omega^3}\sqrt{1 + 3} \quad &\text{(magnitude in an orthonormal basis)} \\
> &= \frac{4 m g^2}{\Omega^3} \quad &\text{(arithmetic)} \\
> \mathbf M_O &= \mathbf r_0^P\times\left(-m\,\Omega^2\,\mathbf r_0^P - m g\,\mathbf k\right) \quad &\text{(torque of the resultant force about $O$)} \\
> &= -m g\,\mathbf r_0^P\times\mathbf k \quad &\text{(the attraction has zero moment about $O$)} \\
> &= -m g\left(x\,\mathbf i\times\mathbf k + y\,\mathbf j\times\mathbf k\right) \quad &\text{(distribute; $\mathbf k\times\mathbf k = \mathbf 0$)} \\
> &= m g\,x\,\mathbf j - m g\,y\,\mathbf i \quad &\text{($\mathbf i\times\mathbf k = -\mathbf j$, $\mathbf j\times\mathbf k = \mathbf i$)} \\
> \frac{d}{dt}\left(\mathbf H_{O,0}\cdot\mathbf k\right) &= \mathbf M_O\cdot\mathbf k \quad &\text{(Section 2, with the fixed direction $\mathbf k$)} \\
> &= 0 \quad &\text{(the torque has no $\mathbf k$ component)} \\
> \mathbf H_{O,0}\cdot\mathbf k &= \frac{\sqrt3\,g}{\Omega^2}\cdot m\,\frac{2g}{\Omega} \quad &\text{(the $\mathbf k$ component of $\mathbf r_0^P(0)\times m\,\mathbf v_0^P(0)$)} \\
> &= \frac{2\sqrt3\,m g^2}{\Omega^3} \quad &\text{(arithmetic)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{A,0} = \frac{2 m g^2}{\Omega^3}\left(-\mathbf i + \sqrt3\,\mathbf k\right),\quad \lvert\mathbf H_{A,0}\rvert = \frac{4 m g^2}{\Omega^3};\qquad \mathbf H_{O,0}\cdot\mathbf k = \frac{2\sqrt3\,m g^2}{\Omega^3}\ \text{(conserved)}}$$
>
> **Units:** $\mathrm{kg}\,(\mathrm{m\,s^{-2}})^2\,\mathrm{s^3} = \mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** the three components of the angular momentum about $A$ are constants of the motion; about $O$ only the vertical component is, because the weight is vertical and its moment about $O$ is horizontal. Both vertical components are equal, as the change of pole of Section 1 predicts: $\overrightarrow{OA}$ is vertical, so its cross product with the momentum is horizontal.

> [!derivation] Integration of the motion and the trajectory
> **Law:** linear equations with constant coefficients (characteristic equation); initial conditions on the position and on the first derivative; geometry of the trajectory about the centre $A$
> **Source:** [Lecture 4, Slide 6]; Notes.pdf, Eq. 4.53; Notes.pdf, Sec. 4.8.1
>
> The vertical equation is written for the height above $A$, so that it has the same form as the other two. Each coordinate has its own pair of constants.
>
> $$\begin{aligned}
> \ddot x + \Omega^2 x &= 0 \quad &\text{(first equation of motion)} \\
> \lambda^2 + \Omega^2 &= 0 \quad &\text{(characteristic equation of the trial solution $e^{\lambda t}$)} \\
> \lambda &= \pm\,\mathrm i\,\Omega \quad &\text{(two imaginary roots)} \\
> x &= K_1\cos\Omega t + K_2\sin\Omega t \quad &\text{(real form of the general solution)} \\
> \dot x &= -K_1\Omega\sin\Omega t + K_2\Omega\cos\Omega t \quad &\text{(first derivative, chain rule)} \\
> K_1 &= \frac{\sqrt3\,g}{\Omega^2} \quad &\text{(initial position: $x(0) = K_1$)} \\
> K_2 &= 0 \quad &\text{(initial velocity: $\dot x(0) = K_2\Omega = 0$)} \\
> x &= \frac{\sqrt3\,g}{\Omega^2}\cos\Omega t \quad &\text{(substitute the constants)} \\
> y &= K_3\cos\Omega t + K_4\sin\Omega t \quad &\text{(same equation, same characteristic roots)} \\
> \dot y &= -K_3\Omega\sin\Omega t + K_4\Omega\cos\Omega t \quad &\text{(first derivative, chain rule)} \\
> K_3 &= 0 \quad &\text{(initial position: $y(0) = K_3$)} \\
> K_4 &= \frac{2g}{\Omega^2} \quad &\text{(initial velocity: $\dot y(0) = K_4\Omega = 2g/\Omega$)} \\
> y &= \frac{2g}{\Omega^2}\sin\Omega t \quad &\text{(substitute the constants)} \\
> \frac{d^2}{dt^2}\left(z + \frac{g}{\Omega^2}\right) + \Omega^2\left(z + \frac{g}{\Omega^2}\right) &= \ddot z + \Omega^2 z + g \quad &\text{(the added constant has zero derivatives)} \\
> &= 0 \quad &\text{(third equation of motion)} \\
> z + \frac{g}{\Omega^2} &= K_5\cos\Omega t + K_6\sin\Omega t \quad &\text{(same form in the height above $A$)} \\
> \dot z &= -K_5\Omega\sin\Omega t + K_6\Omega\cos\Omega t \quad &\text{(first derivative, chain rule)} \\
> K_5 &= \frac{g}{\Omega^2} \quad &\text{(initial position: $z(0) + g/\Omega^2 = K_5$ with $z(0) = 0$)} \\
> K_6 &= 0 \quad &\text{(initial velocity: $\dot z(0) = K_6\Omega = 0$)} \\
> z &= -\frac{g}{\Omega^2}\left(1 - \cos\Omega t\right) \quad &\text{(substitute the constants and solve for $z$)} \\
> \mathbf r_A^P &= x\,\mathbf i + y\,\mathbf j + \left(z + \frac{g}{\Omega^2}\right)\mathbf k \quad &\text{($\mathbf r_0^P - \mathbf r_0^A$)} \\
> &= \frac{g}{\Omega^2}\left[\cos\Omega t\left(\sqrt3\,\mathbf i + \mathbf k\right) + 2\sin\Omega t\,\mathbf j\right] \quad &\text{(substitute the three coordinates and group the cosines)} \\
> &= \frac{2g}{\Omega^2}\left[\cos\Omega t\,\mathbf u_1 + \sin\Omega t\,\mathbf j\right] \quad &\text{(take out $2$; $\mathbf u_1$ is $(\sqrt3\,\mathbf i + \mathbf k)/2$)} \\
> \mathbf u_1\cdot\mathbf u_1 &= \frac{3 + 1}{4} \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= 1 \quad &\text{(arithmetic: $\mathbf u_1$ is a unit vector)} \\
> \mathbf u_1\cdot\mathbf j &= 0 \quad &\text{($\mathbf u_1$ has no $\mathbf j$ component)} \\
> \lvert\mathbf r_A^P\rvert^2 &= \frac{4g^2}{\Omega^4}\left(\cos^2\Omega t + \sin^2\Omega t\right) \quad &\text{(dot product with $\mathbf u_1$ and $\mathbf j$ orthonormal)} \\
> &= \frac{4g^2}{\Omega^4} \quad &\text{(Pythagoras)} \\
> \mathbf v_0^P &= \frac{2g}{\Omega}\left[-\sin\Omega t\,\mathbf u_1 + \cos\Omega t\,\mathbf j\right] \quad &\text{(time derivative; $A$, $\mathbf u_1$ and $\mathbf j$ are fixed)} \\
> \lvert\mathbf v_0^P\rvert^2 &= \frac{4g^2}{\Omega^2}\left(\sin^2\Omega t + \cos^2\Omega t\right) \quad &\text{(same orthonormal pair)} \\
> &= \frac{4g^2}{\Omega^2} \quad &\text{(Pythagoras)} \\
> \mathbf r_A^P\cdot\mathbf v_0^P &= \frac{4g^3}{\Omega^4}\left(-\cos\Omega t\sin\Omega t + \sin\Omega t\cos\Omega t\right) \quad &\text{(dot product in the orthonormal pair)} \\
> &= 0 \quad &\text{(the velocity is perpendicular to the radius)} \\
> \left(-\mathbf i + \sqrt3\,\mathbf k\right)\cdot\left(\sqrt3\,\mathbf i + \mathbf k\right) &= -\sqrt3 + \sqrt3 \quad &\text{(dot product in $\mathcal B_0$)} \\
> &= 0 \quad &\text{($\mathbf u_1$, and $\mathbf j$, are perpendicular to $\mathbf H_{A,0}$)} \\
> m\,\lvert\mathbf r_A^P\rvert\,\lvert\mathbf v_0^P\rvert &= m\,\frac{2g}{\Omega^2}\,\frac{2g}{\Omega} \quad &\text{(magnitude of $\mathbf r_A^P\times m\,\mathbf v_0^P$ for perpendicular factors, Eq. 1.30)} \\
> &= \frac{4 m g^2}{\Omega^3} \quad &\text{(the magnitude of the previous box)}
> \end{aligned}$$
>
> $$\boxed{x = \frac{\sqrt3\,g}{\Omega^2}\cos\Omega t,\quad y = \frac{2g}{\Omega^2}\sin\Omega t,\quad z = -\frac{g}{\Omega^2}\left(1 - \cos\Omega t\right);\qquad \lvert\overrightarrow{AP}\rvert = \frac{2g}{\Omega^2},\quad v = \frac{2g}{\Omega}}$$
>
> **Units:** $g/\Omega^2$ in $\mathrm m$; $g/\Omega$ in $\mathrm{m\,s^{-1}}$; $\Omega t$ in $\mathrm{rad}$; $\mathbf H_{A,0}$ in $\mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** the particle moves with constant speed on a circle centred at $A$ with a radius twice that depth, turning at the rate $\Omega$, so that one turn takes two pi over $\Omega$. The circle lies in the plane through $A$ spanned by $\mathbf j$ and $\mathbf u_1$; $\mathbf u_1$ rises thirty degrees above the horizontal, since its right triangle has the adjacent leg, the square root of three, along $\mathbf i$, the opposite leg, one, along $\mathbf k$, and the hypotenuse two, so its sine is one half. That plane is perpendicular to the constant angular momentum about $A$, as Section 4 proves for every central force, and the magnitude of the angular momentum computed from the motion agrees with its initial value.

![[attachments/EM-T/t4-attraction-circle.svg]]

## 4. Central force motion

If the line of action of the resultant force on a particle always passes through a fixed point $O$, the force is called a central force (Notes.pdf, Sec. 4.8.1). The slides define a central force problem with respect to a reference frame $S_0$ the same way, with $O$ its origin ([Lecture 4, Slide 7]). Central force problems are an important class of classical mechanics: the orbital motion of the planets about the Sun and of satellites about the Earth under gravity is one, Kepler's problem or the two-body problem (Sections 5 to 9). Kepler first postulated its laws from observation; later they were derived from Newton's laws (Notes.pdf, Sec. 4.8.1).

![[attachments/EM-T/t4-central-force.svg]]

> [!derivation] A central force has zero torque about its centre
> **Law:** definition of a central force; torque about $O$; cross product of parallel vectors; conservation of the angular momentum about a fixed point
> **Source:** Notes.pdf, Eq. 4.56; Notes.pdf, Eq. 4.57; Notes.pdf, Eq. 4.58; Notes.pdf, Eq. 4.53; [Lecture 4, Slide 7]
>
> $O$ is the origin of $S_0$, fixed; $r$ is the magnitude of $\mathbf r_0^P$ and $\mathbf e_r$ the unit vector along it, defined wherever $P$ is not at $O$. $F$ is a scalar of either sign: negative for an attraction, positive for a repulsion.
>
> $$\begin{aligned}
> \mathbf e_r &= \frac{\mathbf r_0^P}{r} \quad &\text{(radial unit vector)} \\
> \mathbf F &= F\,\mathbf e_r \quad &\text{(the line of action passes through $O$: Eq. 4.56)} \\
> \mathbf M_O &= \mathbf r_0^P\times\mathbf F \quad &\text{(torque about $O$, Eq. 4.51 with $\mathbf r_0^O = \mathbf 0$)} \\
> &= r\,\mathbf e_r\times F\,\mathbf e_r \quad &\text{(substitute both vectors)} \\
> &= r F\,\mathbf e_r\times\mathbf e_r \quad &\text{(take out the scalars)} \\
> &= \mathbf 0 \quad &\text{(cross product of a vector with itself: Eq. 4.57)} \\
> \mathbf H_{O,0} &= \mathbf r_0^P\times m\,\mathbf v_0^P = \text{const} \quad &\text{($O$ fixed and zero torque, Section 3: Eq. 4.58)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = F\,\mathbf e_r\ \Rightarrow\ \mathbf M_O = \mathbf 0\ \Rightarrow\ \mathbf H_{O,0} = \mathbf r_0^P\times m\,\mathbf v_0^P = \text{const}}$$
>
> **Units:** $\mathrm N$; $\mathrm{N\,m}$; $\mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** the first property of central force motion: a vector constant of the motion, the angular momentum about the centre, which gives three scalar conservation laws (Notes.pdf, Sec. 4.8.1; [Lecture 4, Slide 7]). $F$ may depend on anything, the distance, the velocity or time: only its direction matters here.

> [!derivation] The motion is planar
> **Law:** the angular momentum is perpendicular to the position and to the velocity; a constant vector fixes a plane through $O$; the derivative of a unit vector is perpendicular to it
> **Source:** Notes.pdf, Sec. 4.8.1; Notes.pdf, Eq. 4.58; Notes.pdf, Eq. 1.33; Notes.pdf, Eq. 1.63; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.66; [Lecture 4, Slide 7]
>
> Section 1 proved that the angular momentum is perpendicular to the arm and to the velocity; here the arm is $\mathbf r_0^P$ and the vector is constant. The case of zero angular momentum is discussed in the second part of the box.
>
> $$\begin{aligned}
> \mathbf H_{O,0}\cdot\mathbf r_0^P &= 0 \quad &\text{(Section 1, with $A$ at $O$; for every $t$)} \\
> \mathbf H_{O,0}\cdot\mathbf v_0^P &= 0 \quad &\text{(Section 1; for every $t$)} \\
> \mathbf H_{O,0} &\neq \mathbf 0:\ \ \mathbf r_0^P(t)\ \text{lies in the plane through $O$ perpendicular to the constant}\ \mathbf H_{O,0} \quad &\text{(a fixed normal and a point $O$ fix one plane)} \\
> \mathbf r_0^P\times m\,\mathbf v_0^P &= r\,\mathbf e_r\times m\left(\dot r\,\mathbf e_r + r\,\frac{d\mathbf e_r}{dt}\right) \quad &\text{($\mathbf r_0^P = r\,\mathbf e_r$; product rule, Eq. 1.64, as in Eq. 1.63)} \\
> &= m r^2\,\mathbf e_r\times\frac{d\mathbf e_r}{dt} \quad &\text{(linearity; $\mathbf e_r\times\mathbf e_r = \mathbf 0$)} \\
> \mathbf e_r\cdot\frac{d\mathbf e_r}{dt} &= \frac12\,\frac{d}{dt}\left(\mathbf e_r\cdot\mathbf e_r\right) \quad &\text{(product rule of the dot product, Eq. 1.66)} \\
> &= 0 \quad &\text{($\mathbf e_r\cdot\mathbf e_r = 1$ is constant)} \\
> \mathbf H_{O,0} &= \mathbf 0,\ r \neq 0\ \Rightarrow\ \frac{d\mathbf e_r}{dt} = \mathbf 0 \quad &\text{($d\mathbf e_r/dt$ is perpendicular to $\mathbf e_r$, so its cross product with $\mathbf e_r$ vanishes only if it vanishes)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{O,0} \neq \mathbf 0:\ P\ \text{moves in the fixed plane through}\ O\ \text{perpendicular to}\ \mathbf H_{O,0};\qquad \mathbf H_{O,0} = \mathbf 0:\ \mathbf e_r = \text{const},\ P\ \text{moves on a fixed line through}\ O}$$
>
> **Units:** $\mathrm{kg\,m^3\,s^{-1}}$ in the first two rows (they are zero); $\mathrm{kg\,m^2\,s^{-1}}$ in the others
> **Meaning:** the second property of central force motion: the particle stays in the plane perpendicular to the angular momentum that passes through $O$, so the motion is planar (Notes.pdf, Sec. 4.8.1). With zero angular momentum the motion is still planar, and simpler: the direction of the radius never changes, and $P$ moves back and forth along a fixed line through the centre, the only way it can reach $O$ (Section 10).

Since the motion is planar, it is conveniently described in polar coordinates in the plane of motion; in some cases a rotating frame centred at $O$ that tracks the position of the particle is useful (Notes.pdf, Sec. 4.8.1; [Lecture 4, Slide 7]). From here on, $S_0$ is chosen with its plane $Oxy$ as the plane of motion and $\mathbf k$ along the angular momentum, as Chapter 8 does (Notes.pdf, Sec. 8.2); then the cylindrical coordinate $z$ is zero throughout, and the cylindrical radius, which the notes write $R$ in Sec. 4.8.1, coincides with the distance $r$ to the centre.

![[attachments/EM-T/t4-polar-basis.svg]]

> [!derivation] The polar basis and its change of basis matrix
> **Law:** right triangles of the unit vectors; right-hand rule about $\mathbf k$; change of basis matrix with the local unit vectors as columns; determinant and orthogonality
> **Source:** Notes.pdf, Eq. 8.2; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; [Lecture 4, Slide 12]
>
> View along $\mathbf k$, which points out of the paper (⊙). $\mathbf e_r$ points from $O$ to $P$: in the right triangle with unit hypotenuse $\mathbf e_r$ and the angle $\theta$ at $O$ between $\mathbf i$ and $\mathbf e_r$, the leg along $\mathbf i$ is adjacent to $\theta$, $\cos\theta$, and the leg along $\mathbf j$ is opposite, $\sin\theta$. $\mathbf e_\theta$ is $\mathbf e_r$ turned a quarter turn counterclockwise, the sense in which $\theta$ grows by the right-hand rule about $\mathbf k$ (thumb out of the paper, fingers counterclockwise); the same angle $\theta$ lies between $\mathbf j$ and $\mathbf e_\theta$, so the leg along $\mathbf j$ is adjacent, $\cos\theta$, and the leg along $\mathbf i$ is opposite, $\sin\theta$, but points towards $-\mathbf i$: for $\theta$ between $0$ and $\pi/2$, turning $\mathbf e_r$ counterclockwise past $\mathbf j$ takes $\mathbf e_\theta$ to the left of $\mathbf j$, which is the minus sign of its $\mathbf i$ component.
>
> $$\begin{aligned}
> \mathbf e_r &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(legs of the first triangle, Eq. 8.2)} \\
> \mathbf e_\theta &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(legs of the second triangle, Eq. 8.2)} \\
> [{}_0R_1] &= \begin{pmatrix} \cos\theta & -\sin\theta & 0 \cr \sin\theta & \cos\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf e_r$, $\mathbf e_\theta$, $\mathbf k$ in $\mathcal B_0$, Eq. 1.13; a simple rotation about $\mathbf k$, Eq. 1.20)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\theta\cos\theta - (-\sin\theta)\sin\theta\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2\theta + \sin^2\theta \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \cos\theta\cos\theta + (-\sin\theta)(-\sin\theta) + 0\cdot 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{12} &= \cos\theta\sin\theta + (-\sin\theta)\cos\theta + 0\cdot 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_r = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j,\quad \mathbf e_\theta = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j,\quad \mathbf e_z = \mathbf k;\qquad [{}_0R_1] = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix},\ \ \det = 1}$$
>
> **Units:** dimensionless
> **Meaning:** $\mathcal B_1$ is the basis of the frame $S_1$, with origin at $O$, that turns with the radius $OP$, the rotating frame that tracks the particle; the other entries of the product follow the same way ($(2,2)$ by Pythagoras, the third row and column trivially), so the basis is orthonormal, and it is right-handed, since its determinant is one. When $\theta$ is zero it coincides with $\mathcal B_0$.

> [!derivation] Position, velocity and acceleration in polar coordinates
> **Law:** chain rule through $\theta(t)$ for the unit vectors; definition of velocity and acceleration; product rule
> **Source:** Notes.pdf, Eq. 8.3; Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 1.62; [Lecture 4, Slide 12]
>
> The derivatives are taken in $S_0$, where $\mathbf i$, $\mathbf j$, $\mathbf k$ are constant.
>
> $$\begin{aligned}
> \frac{d\mathbf e_r}{dt} &= \frac{d\mathbf e_r}{d\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= \left(-\sin\theta\,\mathbf i + \cos\theta\,\mathbf j\right)\dot\theta \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(previous box; Eq. 2.25)} \\
> \frac{d\mathbf e_\theta}{dt} &= \frac{d\mathbf e_\theta}{d\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= \left(-\cos\theta\,\mathbf i - \sin\theta\,\mathbf j\right)\dot\theta \quad &\text{(derivatives of $-\sin\theta$ and $\cos\theta$)} \\
> &= -\dot\theta\,\mathbf e_r \quad &\text{(previous box; Eq. 2.26)} \\
> \mathbf r_0^P &= r\,\mathbf e_r \quad &\text{($P$ at distance $r$ from $O$ along $\mathbf e_r$)} \\
> \mathbf v_0^P &= \dot r\,\mathbf e_r + r\,\frac{d\mathbf e_r}{dt} \quad &\text{(Eq. 2.3; product rule, Eq. 1.64)} \\
> &= \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta \quad &\text{(derivative of $\mathbf e_r$)} \\
> \mathbf a_0^P &= \ddot r\,\mathbf e_r + \dot r\,\frac{d\mathbf e_r}{dt} + \frac{d}{dt}\left(r\dot\theta\right)\mathbf e_\theta + r\dot\theta\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(Eq. 2.4; product rule on both terms)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \left(\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta + r\dot\theta\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(derivative of $\mathbf e_r$; product rule for $r\dot\theta$)} \\
> &= \ddot r\,\mathbf e_r + \dot r\dot\theta\,\mathbf e_\theta + \left(\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta - r\dot\theta^2\,\mathbf e_r \quad &\text{(derivative of $\mathbf e_\theta$)} \\
> &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta \quad &\text{(group the components)} \\
> \dot\theta\,\mathbf k\times\mathbf e_r &= \dot\theta\cos\theta\,\mathbf k\times\mathbf i + \dot\theta\sin\theta\,\mathbf k\times\mathbf j \quad &\text{(check with Eq. 1.62: distribute)} \\
> &= \dot\theta\cos\theta\,\mathbf j - \dot\theta\sin\theta\,\mathbf i \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(the derivative of $\mathbf e_r$ again: $\boldsymbol\omega_{10} = \dot\theta\,\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = r\,\mathbf e_r,\qquad \mathbf v_0^P = \dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_0^P = \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta}$$
>
> **Units:** $\mathrm m$; $\mathrm{m\,s^{-1}}$ for both terms of the velocity; $\mathrm{m\,s^{-2}}$ for every term of the acceleration ($\dot r\dot\theta$ is $\mathrm{m\,s^{-1}}\cdot\mathrm{rad\,s^{-1}}$)
> **Meaning:** Eq. 8.3, with $z$ zero (Eqs. 2.28 to 2.30 with the cylindrical radius equal to $r$). The radial acceleration has the term towards the centre that turns the velocity; the transverse one has, besides the angular acceleration, the term twice the product of the two rates. The basis turns about $\mathbf k$ at the rate of change of $\theta$.

> [!derivation] Angular momentum in polar coordinates
> **Law:** definition of the angular momentum about $O$; cross products of the polar unit vectors; its conservation
> **Source:** Notes.pdf, Sec. 4.8.1; Notes.pdf, Eq. 4.58; Notes.pdf, Eq. 1.32; [Lecture 4, Slide 7]
>
> $\mathcal B_1$ is orthonormal and right-handed, so $\mathbf e_r\times\mathbf e_\theta$ is $\mathbf k$, like $\mathbf i\times\mathbf j$.
>
> $$\begin{aligned}
> \mathbf H_{O,0} &= r\,\mathbf e_r\times m\left(\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta\right) \quad &\text{(Eq. 4.58 with the previous box)} \\
> &= m r\dot r\,\mathbf e_r\times\mathbf e_r + m r^2\dot\theta\,\mathbf e_r\times\mathbf e_\theta \quad &\text{(distribute, Eq. 1.32)} \\
> &= m r^2\dot\theta\,\mathbf k \quad &\text{($\mathbf e_r\times\mathbf e_r = \mathbf 0$, $\mathbf e_r\times\mathbf e_\theta = \mathbf k$)} \\
> m r^2\dot\theta &= \text{const} \quad &\text{(Eq. 4.58: the vector is constant)} \\
> \dot\theta &= \frac{\text{const}}{m r^2} \quad &\text{(solve for the rate of $\theta$, with $r$ not zero)}
> \end{aligned}$$
>
> $$\boxed{\mathbf H_{O,0} = m r^2\dot\theta\,\mathbf k,\qquad m r^2\dot\theta = \text{const}}$$
>
> **Units:** $\mathrm{kg}\,\mathrm{m^2}\,\mathrm{rad\,s^{-1}} = \mathrm{kg\,m^2\,s^{-1}}$
> **Meaning:** the fourth property of central force motion: given the initial conditions, the angular rate grows as the particle approaches the centre and decreases as it moves away, in inverse proportion to the square of the distance ([Lecture 4, Slide 7]; Notes.pdf, Sec. 4.8.1). With a non-zero angular momentum the rate never vanishes, so the polar angle changes always in the same sense.

> [!warning] Source issue: Notes.pdf, Sec. 4.8.1, property 4
> The fourth property of Notes.pdf, Sec. 4.8.1 (printed p. 52) writes the angular momentum about $O$ as the square of $R$ times the rate of $\theta$, without the mass; the box above, and [Lecture 4, Slide 7], give the mass times that product, which is the magnitude of the vector. The conclusion of the property is not affected, since the mass is constant. Dividing by the mass gives the mass-specific angular momentum $h$ of Chapter 8 (Section 6).

## 5. Kepler's problem

The two-body problem concerns the motion of two point particles under their mutual gravitational attraction; it is a great model for many problems of orbital mechanics, such as a satellite around the Earth or the Earth around the Sun ([Lecture 4, Slide 8]). The notes illustrate the Newtonian approach of Chapter 7 with it (Notes.pdf, Ch. 8): a spacecraft $P$ of mass $m$ moves around the Earth $C$ of mass $m_C$, both modelled as point particles, and nothing else in the universe perturbs the motion. Kepler (1571 to 1630), who lived before Newton was born, described the motion of the planets from observations only and postulated three laws, with no explanation of why they hold (Notes.pdf, Sec. 8.1; [Lecture 4, Slide 8]); Sections 6 to 8 derive them from Newton's laws, with spacecraft in place of planet and Earth in place of Sun.

| Law | Statement | Proved in |
| :--- | :--- | :--- |
| first | the orbits of the planets are ellipses, with the Sun at one of the foci | Section 7 (Eq. 8.14) |
| second | the line joining a planet to the Sun sweeps out equal areas in equal intervals of time | Section 6 (Eq. 8.8) |
| third | the square of the period of a planet is proportional to the cube of the major axis of its elliptical orbit | Section 8 (Eq. 8.17) |

![[attachments/EM-T/t4-two-body.svg]]

> [!derivation] The two bodies and their barycentre
> **Law:** Newton's law of universal gravitation; Newton's second and third laws in an inertial frame; definition of the barycentre; integration in time with Barrow's rule
> **Source:** [Lecture 4, Slide 9]; Notes.pdf, Sec. 4.2; Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4
>
> $S_0$ is any inertial frame, with origin $O$; $\mathbf r_0^C$ and $\mathbf a_0^C$ are the position and acceleration of $C$ in it. The attraction of $C$ on $P$ has the magnitude of the law of gravitation and points from $P$ to $C$, opposite to $\mathbf r_0^P - \mathbf r_0^C$; the attraction of $P$ on $C$ is equal and opposite (third law).
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= -\frac{G m m_C}{\lvert\mathbf r_0^P - \mathbf r_0^C\rvert^2}\,\frac{\mathbf r_0^P - \mathbf r_0^C}{\lvert\mathbf r_0^P - \mathbf r_0^C\rvert} \quad &\text{(second law for $P$, Slide 9)} \\
> m_C\,\mathbf a_0^C &= +\frac{G m m_C}{\lvert\mathbf r_0^P - \mathbf r_0^C\rvert^2}\,\frac{\mathbf r_0^P - \mathbf r_0^C}{\lvert\mathbf r_0^P - \mathbf r_0^C\rvert} \quad &\text{(second law for $C$, Slide 9)} \\
> m\,\mathbf a_0^P + m_C\,\mathbf a_0^C &= \mathbf 0 \quad &\text{(add the two rows: the right sides cancel)} \\
> \mathbf r_0^Z &= \frac{m\,\mathbf r_0^P + m_C\,\mathbf r_0^C}{m + m_C} \quad &\text{(definition of the barycentre $Z$)} \\
> \left(m + m_C\right)\frac{d^2\mathbf r_0^Z}{dt^2} &= m\,\mathbf a_0^P + m_C\,\mathbf a_0^C \quad &\text{(differentiate twice; the masses are constant)} \\
> &= \mathbf 0 \quad &\text{(the sum above)} \\
> \frac{d\mathbf v_0^Z}{dt} &= \mathbf 0 \quad &\text{(divide by the total mass; $\mathbf v_0^Z$ is the derivative of $\mathbf r_0^Z$)} \\
> \int_0^t \frac{d\mathbf v_0^Z}{dt'}\,dt' &= \mathbf 0 \quad &\text{(integrate from $0$ to $t$)} \\
> \mathbf v_0^Z(t) - \mathbf v_0^Z(0) &= \mathbf 0 \quad &\text{(antiderivative of a derivative; Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^Z = \mathbf 0,\qquad \mathbf v_0^Z = \text{const}:\ S_Z\ \text{is inertial, and}\ \left.\frac{d}{dt}\right|_0 = \left.\frac{d}{dt}\right|_Z}$$
>
> **Units:** $\mathrm N$ in the first rows ($G$ in $\mathrm{N\,m^2\,kg^{-2}}$); $\mathrm{m\,s^{-1}}$ in the last
> **Meaning:** the barycentre is not accelerated, so the frame $S_Z$, with origin at $Z$ and axes parallel to those of $S_0$, moves with constant velocity and without rotation, and it is inertial too (Notes.pdf, Sec. 4.2; [Lecture 4, Slide 9]). Since the axes are parallel, a time derivative is the same in both frames.

> [!derivation] The relative motion of the particle about the attracting body
> **Law:** the two equations of motion divided by the masses and subtracted; definition of the gravitational parameter; position of the barycentre relative to $C$
> **Source:** [Lecture 4, Slide 10]; [Lecture 4, Slide 11]; Notes.pdf, Eq. 8.1; Notes.pdf, Ch. 8
>
> $\mathbf r$ goes from $C$ to $P$; its time derivatives are the same in $S_0$ and in $S_C$, the frame with origin at $C$ and parallel axes, because the axes do not rotate.
>
> $$\begin{aligned}
> \mathbf r &= \mathbf r_0^P - \mathbf r_0^C,\qquad r = \lvert\mathbf r\rvert \quad &\text{(relative position, Slide 10)} \\
> \mathbf a_0^P &= -\frac{G m_C}{r^2}\,\frac{\mathbf r}{r} \quad &\text{(first equation of the previous box divided by $m$)} \\
> \mathbf a_0^C &= +\frac{G m}{r^2}\,\frac{\mathbf r}{r} \quad &\text{(second equation divided by $m_C$)} \\
> \frac{d^2\mathbf r}{dt^2} &= \mathbf a_0^P - \mathbf a_0^C \quad &\text{(second derivative of the relative position)} \\
> &= -\frac{G\left(m_C + m\right)}{r^2}\,\frac{\mathbf r}{r} \quad &\text{(subtract; common factor)} \\
> \mu &= G\left(m_C + m\right) \quad &\text{(gravitational parameter, Slide 10)} \\
> \frac{d^2\mathbf r}{dt^2} &= -\frac{\mu}{r^3}\,\mathbf r \quad &\text{(final equation, Slide 11)} \\
> \mathbf r_0^Z - \mathbf r_0^C &= \frac{m\,\mathbf r_0^P + m_C\,\mathbf r_0^C - \left(m + m_C\right)\mathbf r_0^C}{m + m_C} \quad &\text{(definition of $Z$, common denominator)} \\
> &= \frac{m}{m + m_C}\,\mathbf r \quad &\text{(the $m_C$ terms cancel)} \\
> m \ll m_C:\ \ \mu &\simeq G m_C,\quad \overrightarrow{CZ} \simeq \mathbf 0 \quad &\text{(the ratio of the masses is negligible)} \\
> m\,\frac{d^2\mathbf r}{dt^2} &\simeq -\frac{\mu}{r^2}\,m\,\mathbf e_r \quad &\text{(the model of the notes, Eq. 8.1, with $\mathbf e_r$ along $\mathbf r$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d^2\mathbf r}{dt^2} = -\frac{\mu}{r^2}\,\mathbf e_r,\qquad \mu = G\left(m_C + m\right) \simeq G m_C}$$
>
> **Units:** $\mu$ in $\mathrm{N\,m^2\,kg^{-2}}\cdot\mathrm{kg} = \mathrm{m^3\,s^{-2}}$; both sides in $\mathrm{m\,s^{-2}}$
> **Meaning:** the relative motion obeys the equation of a particle attracted by a fixed centre at $C$ with the parameter $\mu$, with no approximation. The frame $S_C$ is not inertial, since $C$ is accelerated; but when the mass of $P$ is negligible against that of $C$, $\mu$ tends to the product of $G$ and $m_C$, the barycentre tends to $C$, and the non-inertial effects are negligible ([Lecture 4, Slide 10]). The notes start directly from that limit: they take an inertial frame with its origin at the barycentre, neglect the acceleration of the Earth, and write the force on $P$ as Eq. 8.1 (Notes.pdf, Ch. 8).

> [!warning] Two values of the gravitational parameter
> The notes define $\mu$ as $G$ times the mass of the attracting body (Eq. 8.1, p. 71) and place the origin at a body they take as fixed; [Lecture 4, Slide 10] defines it as $G$ times the sum of both masses, which makes the relative equation exact. Both agree when the mass of $P$ is negligible, which is the case of a spacecraft about the Earth; for the Earth about the Sun the relative difference is the ratio of the masses, about three millionths. This note uses the exact relative equation, and every result below holds with either value.

> [!derivation] Properties of Kepler's problem and the potential of gravity
> **Law:** the relative equation is a central force problem; definition of the potential energy with the reference at infinity; the gradient recovers the force; conservation of mechanical energy
> **Source:** [Lecture 4, Slide 11]; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.31; Notes.pdf, Sec. 8.5
>
> Per unit mass, the force of the final equation is minus $\mu$ over the square of $r$ along $\mathbf e_r$. A step $d\mathbf r'$ along the path has the radial component $dr'$, since $\mathbf e_r\cdot d\mathbf r'$ is the change of the distance. The gradient of the distance is computed in Cartesian components about $C$.
>
> $$\begin{aligned}
> m\,\frac{d^2\mathbf r}{dt^2} &= -\frac{m\mu}{r^2}\,\mathbf e_r \quad &\text{(a central force, Eq. 4.56 with $F$ equal to $-m\mu/r^2$: Section 4 applies)} \\
> \frac{V_0}{m} &= -\int_{\infty}^{r}\left(-\frac{\mu}{r'^2}\,\mathbf e_r\right)\cdot d\mathbf r' \quad &\text{(Eq. 4.14 divided by $m$, reference point at infinite distance)} \\
> &= \mu\int_{\infty}^{r}\frac{dr'}{r'^2} \quad &\text{(the two minus signs cancel; $\mathbf e_r\cdot d\mathbf r' = dr'$)} \\
> &= \mu\left[-\frac{1}{r'}\right]_{\infty}^{r} \quad &\text{(antiderivative of $r'^{-2}$)} \\
> &= \mu\left(-\frac{1}{r} + \lim_{r'\to\infty}\frac{1}{r'}\right) \quad &\text{(Barrow's rule with both limits)} \\
> &= -\frac{\mu}{r} \quad &\text{(the limit is zero)} \\
> \frac{\partial r}{\partial x} &= \frac{\partial}{\partial x}\sqrt{x^2 + y^2 + z^2} \quad &\text{($r$ in Cartesian components about $C$)} \\
> &= \frac{2x}{2\sqrt{x^2 + y^2 + z^2}} = \frac{x}{r} \quad &\text{(chain rule; likewise for $y$ and $z$)} \\
> \nabla r &= \frac{x\,\mathbf i + y\,\mathbf j + z\,\mathbf k}{r} \quad &\text{(gradient of the distance)} \\
> &= \mathbf e_r \quad &\text{(the position about $C$ over its magnitude)} \\
> -\nabla\frac{V_0}{m} &= -\frac{\mu}{r^2}\,\nabla r \quad &\text{(chain rule: derivative of $-\mu/r$ with respect to $r$)} \\
> &= -\frac{\mu}{r^2}\,\mathbf e_r \quad &\text{(the force per unit mass is recovered, Eq. 4.20)}
> \end{aligned}$$
>
> $$\boxed{\frac{d^2\mathbf r}{dt^2} = -\frac{\mu}{r^2}\,\mathbf e_r\ \ \text{(central, independent of}\ m\text{)},\qquad \frac{V_0}{m} = -\frac{\mu}{r}}$$
>
> **Units:** $\mathrm{m^3\,s^{-2}}/\mathrm m = \mathrm{m^2\,s^{-2}} = \mathrm{J\,kg^{-1}}$
> **Meaning:** Kepler's problem is a central force problem, so the angular momentum is conserved and the motion is planar, best described in polar coordinates in the plane of motion; the mass of $P$ does not appear, so its motion does not depend on it and mass-specific quantities are used (specific angular momentum, specific energy); and gravity has a potential, so the problem is conservative ([Lecture 4, Slide 11]). The potential is negative and tends to zero at infinite distance, where the reference is placed.

## 6. Kinematics, dynamics and Kepler's second law

The particle is not subject to any constraint, so it has three degrees of freedom; the only force passes through the centre, so the motion is planar (Section 4). The frame is chosen with its plane $xy$ as the plane of motion and with cylindrical coordinates about the attracting body, so that $z$ is zero throughout (Notes.pdf, Sec. 8.2). In the notes that frame is the inertial $S_0$ with its origin at the Earth; with the exact relative equation it is $S_C$, whose acceleration does not enter the relative equation. In both readings the position of $P$ is $\mathbf r$, and the polar basis, the change of basis matrix and the kinematics of Section 4 hold with the origin at $C$ (Eqs. 8.2 and 8.3; [Lecture 4, Slide 12]).

> [!derivation] Equations of motion of Kepler's problem
> **Law:** Newton's second law per unit mass with the acceleration in polar coordinates; projection on $\mathbf e_r$ and $\mathbf e_\theta$
> **Source:** Notes.pdf, Eq. 8.4; Notes.pdf, Eq. 8.5; Notes.pdf, Eq. 8.6; Notes.pdf, Eq. 8.3; [Lecture 4, Slide 12]
>
> $$\begin{aligned}
> \frac{d^2\mathbf r}{dt^2} &= \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta \quad &\text{(Section 4 with the origin at $C$: Eq. 8.3)} \\
> \left(\ddot r - r\dot\theta^2\right)\mathbf e_r + \left(2\dot r\dot\theta + r\ddot\theta\right)\mathbf e_\theta &= -\frac{\mu}{r^2}\,\mathbf e_r \quad &\text{(second law per unit mass, Eq. 8.4)} \\
> \mathbf e_r:\quad \ddot r - r\dot\theta^2 &= -\frac{\mu}{r^2} \quad &\text{(dot-multiply by $\mathbf e_r$: Eq. 8.5)} \\
> \mathbf e_\theta:\quad r\ddot\theta + 2\dot r\dot\theta &= 0 \quad &\text{(dot-multiply by $\mathbf e_\theta$: Eq. 8.6)} \\
> \mathbf k:\quad 0 &= 0 \quad &\text{(no component out of the plane)}
> \end{aligned}$$
>
> $$\boxed{\ddot r - r\dot\theta^2 = -\frac{\mu}{r^2},\qquad r\ddot\theta + 2\dot r\dot\theta = 0}$$
>
> **Units:** $\mathrm{m\,s^{-2}}$ in every term
> **Meaning:** two coupled non-linear equations for the two polar coordinates; the transverse one has no force, because gravity is radial, and it gives a first integral at once.

> [!derivation] The specific angular momentum is constant
> **Law:** multiplication by $r$; product and chain rules; integration in time with Barrow's rule
> **Source:** Notes.pdf, Eq. 8.7; Notes.pdf, Eq. 8.6; Notes.pdf, Eq. 1.32; [Lecture 4, Slide 12]
>
> $$\begin{aligned}
> r^2\ddot\theta + 2 r\dot r\dot\theta &= 0 \quad &\text{(multiply Eq. 8.6 by $r$)} \\
> \frac{d}{dt}\left(r^2\dot\theta\right) &= \frac{d}{dt}\left(r^2\right)\dot\theta + r^2\ddot\theta \quad &\text{(product rule)} \\
> &= 2 r\dot r\dot\theta + r^2\ddot\theta \quad &\text{(chain rule: derivative of $r^2$ is $2r\dot r$)} \\
> \frac{d}{dt}\left(r^2\dot\theta\right) &= 0 \quad &\text{(the first row is this derivative)} \\
> \int_0^t \frac{d}{dt'}\left(r^2\dot\theta\right)dt' &= 0 \quad &\text{(integrate from $0$ to $t$)} \\
> \Big[r^2\dot\theta\Big]_0^t &= 0 \quad &\text{(antiderivative of a derivative)} \\
> r(t)^2\dot\theta(t) - r(0)^2\dot\theta(0) &= 0 \quad &\text{(Barrow's rule: $F(t) - F(0)$)} \\
> r^2\dot\theta &= h \quad &\text{($h = r(0)^2\dot\theta(0)$, fixed by the initial conditions)} \\
> \mathbf h &= \mathbf r\times\frac{d\mathbf r}{dt} \quad &\text{(mass-specific angular momentum about $C$)} \\
> &= r\,\mathbf e_r\times\left(\dot r\,\mathbf e_r + r\dot\theta\,\mathbf e_\theta\right) \quad &\text{(polar position and velocity)} \\
> &= r^2\dot\theta\,\mathbf k \quad &\text{(distribute; $\mathbf e_r\times\mathbf e_r = \mathbf 0$, $\mathbf e_r\times\mathbf e_\theta = \mathbf k$)} \\
> &= h\,\mathbf k \quad &\text{(the first integral)}
> \end{aligned}$$
>
> $$\boxed{h = r^2\dot\theta = \text{const},\qquad \mathbf h = \mathbf r\times\frac{d\mathbf r}{dt} = h\,\mathbf k}$$
>
> **Units:** $\mathrm{m^2\,s^{-1}}$
> **Meaning:** Eq. 8.7: $h$ is the magnitude of the angular momentum per unit mass about the centre, constant as expected in a central force problem; the vector is perpendicular to the plane of motion, and $h$ must be determined from the initial conditions (Notes.pdf, Sec. 8.3). The transverse equation of motion and the conservation of the angular momentum of Section 4 give the same first integral.

![[attachments/EM-T/t4-areal-velocity.svg]]

> [!derivation] Areal velocity: Kepler's second law
> **Law:** area of the triangle swept in a short time as half the magnitude of a cross product; limit of the quotient; the specific angular momentum is constant
> **Source:** Notes.pdf, Eq. 8.8; Notes.pdf, Eq. 1.30; Notes.pdf, Eq. 1.69; [Lecture 4, Slide 12]
>
> In a time $\Delta t$ the radius turns from $\mathbf r(t)$ to $\mathbf r(t+\Delta t)$ through the angle $\Delta\theta$. To first order the swept region is the triangle with these two sides: its area is half that of the parallelogram they define, which is the magnitude of their cross product (Eq. 1.30), and equivalently half its base $r$ times its height, the side opposite to $\Delta\theta$ in the right triangle whose hypotenuse is the second radius.
>
> $$\begin{aligned}
> \Delta\mathcal A &= \tfrac12\,r(t)\,r(t+\Delta t)\,\lvert\sin\Delta\theta\rvert \quad &\text{(half the parallelogram, Eq. 1.30)} \\
> &= \tfrac12\,r(t)\,r(t+\Delta t)\,\lvert\Delta\theta\rvert + O\!\left(\Delta\theta^3\right) \quad &\text{(the sine of a small angle, Eq. 1.69)} \\
> \frac{d\mathcal A}{dt} &= \lim_{\Delta t\to 0}\frac{\Delta\mathcal A}{\Delta t} \quad &\text{(definition of the rate)} \\
> &= \tfrac12\,r^2\,\lvert\dot\theta\rvert \quad &\text{($r(t+\Delta t)$ tends to $r(t)$, $\Delta\theta/\Delta t$ to the rate of $\theta$)} \\
> &= \tfrac12\,r^2\dot\theta \quad &\text{(the polar angle grows: $\theta$ measured in the sense of the motion, $h$ positive)} \\
> &= \frac{h}{2} \quad &\text{(Eq. 8.7)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathcal A}{dt} = \frac12\,r^2\dot\theta = \frac{h}{2} = \text{const}}$$
>
> **Units:** $\mathrm{m^2\,s^{-1}}$
> **Meaning:** Eq. 8.8, Kepler's second law: the line joining the spacecraft to the Earth sweeps out equal areas in equal intervals of time. It holds for every central force, since it uses only the conservation of the angular momentum. Integrating over a time interval, the area swept is $h$ over two times the interval, the relation used for the period in Section 8.

## 7. The orbit equation and Kepler's first law

The radial equation of motion, Eq. 8.5, can also be integrated ([Lecture 4, Slide 13]). The trajectory is sought as the distance in terms of the polar angle, not of time: with the first integral of the angular momentum the time is eliminated, and the variable one over $r$ turns the equation into a linear one (Notes.pdf, Sec. 8.4). The notes do not name the resulting equation; it is commonly called Binet's equation. Since $h$ is not zero for an orbit that is not a radial line (Section 4), the rate of $\theta$ never vanishes and $\theta$ grows monotonically with time, so $r$ can be written as a function of $\theta$.

> [!derivation] The radial velocity and acceleration in terms of the polar angle
> **Law:** chain rule for the derivative of one over $r$; the first integral of the angular momentum; time derivatives through $\theta$
> **Source:** Notes.pdf, Eq. 8.9; Notes.pdf, Eq. 8.10; Notes.pdf, Eq. 8.11; Notes.pdf, Eq. 8.7; [Lecture 4, Slide 13]
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\frac1r\right) &= -\frac{1}{r^2}\,\dot r \quad &\text{(chain rule: derivative of $r^{-1}$ is $-r^{-2}$, times $\dot r$)} \\
> -r^2\,\frac{d}{dt}\left(\frac1r\right) &= \dot r \quad &\text{(multiply by $-r^2$: Eq. 8.9)} \\
> r^2 &= \frac{h}{\dot\theta} \quad &\text{(Eq. 8.7 solved for $r^2$; the rate of $\theta$ is not zero)} \\
> \dot r &= -\frac{h}{\dot\theta}\,\frac{d}{dt}\left(\frac1r\right) \quad &\text{(substitute $r^2$)} \\
> \frac{d}{dt}\left(\frac1r\right) &= \frac{d}{d\theta}\left(\frac1r\right)\dot\theta \quad &\text{(chain rule through $\theta(t)$)} \\
> \dot r &= -h\,\frac{d}{d\theta}\left(\frac1r\right) \quad &\text{(the rate of $\theta$ cancels: Eq. 8.10)} \\
> \ddot r &= -h\,\frac{d}{dt}\left[\frac{d}{d\theta}\left(\frac1r\right)\right] \quad &\text{(time derivative; $h$ is constant)} \\
> &= -h\,\frac{d^2}{d\theta^2}\left(\frac1r\right)\dot\theta \quad &\text{(chain rule through $\theta(t)$)} \\
> &= -\frac{h^2}{r^2}\,\frac{d^2}{d\theta^2}\left(\frac1r\right) \quad &\text{(Eq. 8.7: the rate of $\theta$ is $h/r^2$; Eq. 8.11)} \\
> r\dot\theta^2 &= r\,\frac{h^2}{r^4} \quad &\text{(the same substitution)} \\
> &= \frac{h^2}{r^3} \quad &\text{(simplify)}
> \end{aligned}$$
>
> $$\boxed{\dot r = -h\,\frac{d}{d\theta}\left(\frac1r\right),\qquad \ddot r = -\frac{h^2}{r^2}\,\frac{d^2}{d\theta^2}\left(\frac1r\right),\qquad r\dot\theta^2 = \frac{h^2}{r^3}}$$
>
> **Units:** $\mathrm{m\,s^{-1}}$ for the radial velocity ($h$ in $\mathrm{m^2\,s^{-1}}$ times $\mathrm{m^{-1}\,rad^{-1}}$); $\mathrm{m\,s^{-2}}$ for the other two
> **Meaning:** every time derivative of the radius is a derivative with respect to the angle, multiplied by powers of $h$ and $r$; the time no longer appears.

> [!derivation] The orbit equation
> **Law:** substitution into the radial equation of motion; division by a non-zero factor
> **Source:** Notes.pdf, Eq. 8.12; Notes.pdf, Eq. 8.5; [Lecture 4, Slide 13]
>
> $$\begin{aligned}
> \ddot r - r\dot\theta^2 &= -\frac{\mu}{r^2} \quad &\text{(Eq. 8.5)} \\
> -\frac{h^2}{r^2}\,\frac{d^2}{d\theta^2}\left(\frac1r\right) - \frac{h^2}{r^3} &= -\frac{\mu}{r^2} \quad &\text{(previous box)} \\
> \frac{d^2}{d\theta^2}\left(\frac1r\right) + \frac1r &= \frac{\mu}{h^2} \quad &\text{(multiply by $-r^2/h^2$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d^2}{d\theta^2}\left(\frac1r\right) + \frac1r = \frac{\mu}{h^2}}$$
>
> **Units:** $\mathrm{m^{-1}}$ in every term ($\mu/h^2$ in $\mathrm{m^3\,s^{-2}}/\mathrm{m^4\,s^{-2}}$)
> **Meaning:** Eq. 8.12: a linear second-order equation with constant coefficients in the variable one over $r$, the equation of a harmonic oscillator in the angle $\theta$ forced by a constant, analogous to a forced harmonic oscillator (Notes.pdf, Sec. 8.4; [Lecture 4, Slide 13]).

> [!derivation] General solution: the trajectory is a conic section
> **Law:** homogeneous solution from the characteristic equation plus a particular solution; amplitude and phase with the cosine of a sum; choice of the polar axis
> **Source:** Notes.pdf, Eq. 8.13; Notes.pdf, Eq. 8.14; Notes.pdf, Sec. 8.4; [Lecture 4, Slide 13]; [Lecture 4, Slide 14]
>
> The constants $c_1$ and $c_2$ are written as an amplitude, proportional to $e$, and a phase $\psi$; then the polar axis is turned about $\mathbf k$ so that $\theta$ is measured from the direction of the closest point.
>
> $$\begin{aligned}
> \lambda^2 + 1 &= 0 \quad &\text{(characteristic equation of the homogeneous equation, trial solution $e^{\lambda\theta}$)} \\
> \lambda &= \pm\,\mathrm i \quad &\text{(two imaginary roots)} \\
> \left(\frac1r\right)_{\mathrm{hom}} &= c_1\cos\theta + c_2\sin\theta \quad &\text{(real form of the homogeneous solution)} \\
> \left(\frac1r\right)_{\mathrm{part}} &= \frac{\mu}{h^2} \quad &\text{(a constant: its second derivative is zero, so it equals the right side)} \\
> \frac1r &= \frac{\mu}{h^2} + c_1\cos\theta + c_2\sin\theta \quad &\text{(general solution: the sum)} \\
> c_1 &= \frac{\mu}{h^2}\,e\cos\psi,\qquad c_2 = -\frac{\mu}{h^2}\,e\sin\psi \quad &\text{(new constants: $e \geq 0$ is $h^2/\mu$ times the square root of the sum of the squares of $c_1$, $c_2$)} \\
> c_1\cos\theta + c_2\sin\theta &= \frac{\mu}{h^2}\,e\left(\cos\psi\cos\theta - \sin\psi\sin\theta\right) \quad &\text{(substitute the new constants)} \\
> &= \frac{\mu}{h^2}\,e\cos\left(\theta + \psi\right) \quad &\text{(cosine of a sum)} \\
> \frac1r &= \frac{\mu}{h^2}\left(1 + e\cos\left(\theta + \psi\right)\right) \quad &\text{(Eq. 8.13)} \\
> \theta + \psi &= 0 \ \Rightarrow\ \frac1r\ \text{is largest, $r$ smallest} \quad &\text{(the cosine is largest there, for $e > 0$)} \\
> \frac1r &= \frac{\mu}{h^2}\left(1 + e\cos\theta\right) \quad &\text{(polar axis turned to that direction: $\psi$ becomes $0$)} \\
> r &= \frac{h^2/\mu}{1 + e\cos\theta} \quad &\text{(invert: Eq. 8.14)} \\
> p &= \frac{h^2}{\mu} \quad &\text{(semi-parameter)}
> \end{aligned}$$
>
> $$\boxed{r = \frac{p}{1 + e\cos\theta},\qquad p = \frac{h^2}{\mu},\qquad e \geq 0}$$
>
> **Units:** $p$ in $\mathrm{m^4\,s^{-2}}/\mathrm{m^3\,s^{-2}} = \mathrm m$; $e$ dimensionless
> **Meaning:** Eq. 8.14, the equation of a conic section in polar coordinates about one of its foci, with eccentricity $e$ and semi-parameter $p$ (Notes.pdf, Sec. 8.4); both are fixed by the initial conditions. With the polar axis pointing to the closest point the phase is zero and $e$ is positive, as the notes state; for a circle, with $e$ zero, every direction is equally close and no axis is preferred. The orbit equation gives the distance as a function of the angle, but not the angle as a function of time ([Lecture 4, Slide 14]).

The notes and the slides state that Eq. 8.14 is a conic with a focus at the centre and list its four types by the value of the eccentricity (Notes.pdf, Sec. 8.4; [Lecture 4, Slide 14]). The box below proves it by writing the equation in Cartesian coordinates of the plane of the orbit, with origin at $C$ and the axis $x$ towards the closest point.

![[attachments/EM-T/t4-conic-orbit.svg]]

> [!derivation] Cartesian form of the orbit and the four types of conic
> **Law:** Cartesian coordinates as the legs of the right triangle of the radius; squaring; completing the square; distance from the centre of the conic to a focus
> **Source:** Notes.pdf, Eq. 8.14; Notes.pdf, Sec. 8.4; Notes.pdf, Eq. 2.23; [Lecture 4, Slide 14]
>
> In the right triangle with hypotenuse $r$ and the angle $\theta$ at $C$, the leg along the axis $x$ is adjacent to $\theta$, $r\cos\theta$, and the leg along $y$ is opposite, $r\sin\theta$. Squaring keeps the points with $r$ positive, the orbit, and adds those of the other branch of a hyperbola, where the bracket in the fourth row is negative; that branch is not part of the orbit.
>
> $$\begin{aligned}
> x &= r\cos\theta,\qquad y = r\sin\theta \quad &\text{(legs of the triangle, Eq. 2.23)} \\
> x^2 + y^2 &= r^2 \quad &\text{(Pythagoras in the same triangle)} \\
> r + e\,r\cos\theta &= p \quad &\text{(Eq. 8.14 times its denominator)} \\
> r + e\,x &= p \quad &\text{(first row)} \\
> r &= p - e\,x \quad &\text{(solve for $r$; positive on the orbit)} \\
> x^2 + y^2 &= p^2 - 2 p e\,x + e^2 x^2 \quad &\text{(square; $r^2 = x^2 + y^2$)} \\
> \left(1 - e^2\right)x^2 + 2 p e\,x + y^2 &= p^2 \quad &\text{(group the terms in $x$)} \\
> e = 0:\quad x^2 + y^2 &= p^2 \quad &\text{(a circle of radius $p$ centred at $C$)} \\
> e = 1:\quad y^2 &= p^2 - 2 p\,x \quad &\text{(a parabola, open towards negative $x$)} \\
> a &= \frac{p}{1 - e^2} \quad &\text{(definition for $e \neq 1$; positive if $e < 1$, negative if $e > 1$)} \\
> \left(1 - e^2\right)\left(x^2 + 2 a e\,x\right) + y^2 &= p^2 \quad &\text{($2pe$ is $2ae(1 - e^2)$)} \\
> \left(1 - e^2\right)\left(x + a e\right)^2 - \left(1 - e^2\right)a^2 e^2 + y^2 &= p^2 \quad &\text{(complete the square)} \\
> \left(1 - e^2\right)\left(x + a e\right)^2 + y^2 &= a^2\left(1 - e^2\right)^2 + \left(1 - e^2\right)a^2 e^2 \quad &\text{(move the term over; $p = a(1 - e^2)$)} \\
> &= a^2\left(1 - e^2\right) \quad &\text{(common factor $a^2(1 - e^2)$; $1 - e^2 + e^2 = 1$)} \\
> \frac{\left(x + a e\right)^2}{a^2} + \frac{y^2}{a^2\left(1 - e^2\right)} &= 1 \quad &\text{(divide by $a^2(1 - e^2)$)} \\
> e < 1:\quad b^2 &= a^2\left(1 - e^2\right) > 0 \quad &\text{(an ellipse of semi-axes $a$, $b$, centred at $x = -ae$)} \\
> e > 1:\quad a^2\left(1 - e^2\right) &< 0 \quad &\text{(the second term is subtracted: a hyperbola)} \\
> a^2 - b^2 &= a^2 e^2 \quad &\text{(ellipse: distance from the centre to a focus, squared)}
> \end{aligned}$$
>
> $$\boxed{e = 0\ \text{circle};\quad 0 < e < 1\ \text{ellipse},\ \frac{(x + ae)^2}{a^2} + \frac{y^2}{b^2} = 1,\ b = a\sqrt{1 - e^2};\quad e = 1\ \text{parabola};\quad e > 1\ \text{hyperbola}}$$
>
> **Units:** $\mathrm{m^2}$ in the Cartesian equations; the normalized ones are dimensionless
> **Meaning:** the four types of Notes.pdf, Sec. 8.4 and [Lecture 4, Slide 14]. The centre of the ellipse is at the distance $ae$ from $C$ along the line of the closest point, which is exactly the distance from the centre to a focus (last row): $C$ is a focus. With $e$ below one the trajectory is an ellipse with the Earth at one focus, which proves Kepler's first law; the other conics are possible orbits too, used in interplanetary flight (Notes.pdf, Sec. 8.4), and comets follow parabolas and hyperbolas as well as ellipses ([Lecture 4, Slide 14]).

![[attachments/EM-T/t4-conic-classes.svg]]

> [!derivation] Pericentre, apocentre and the semi-major axis
> **Law:** the orbit equation at the closest and farthest points; definition of the semi-major axis
> **Source:** Notes.pdf, Eq. 8.14; Notes.pdf, Eq. 8.15; Notes.pdf, Sec. 8.4; [Lecture 4, Slide 14]
>
> $$\begin{aligned}
> r_p &= \frac{p}{1 + e\cos 0} \quad &\text{(Eq. 8.14 at $\theta = 0$, the largest denominator)} \\
> &= \frac{p}{1 + e} \quad &\text{($\cos 0 = 1$)} \\
> r_a &= \frac{p}{1 + e\cos\pi} \quad &\text{(Eq. 8.14 at $\theta = \pi$, the smallest denominator)} \\
> &= \frac{p}{1 - e} \quad &\text{($\cos\pi = -1$; positive only if $e < 1$)} \\
> 2a &= r_p + r_a \quad &\text{(definition of the semi-major axis, Eq. 8.15)} \\
> &= \frac{p\left(1 - e\right) + p\left(1 + e\right)}{\left(1 + e\right)\left(1 - e\right)} \quad &\text{(common denominator)} \\
> &= \frac{2p}{1 - e^2} \quad &\text{(simplify)} \\
> p &= a\left(1 - e^2\right) \quad &\text{(solve for $p$: the $a$ of the previous box)} \\
> r_p &= \frac{a\left(1 - e\right)\left(1 + e\right)}{1 + e} \quad &\text{(substitute $p$; factor $1 - e^2$)} \\
> &= a\left(1 - e\right) \quad &\text{(simplify)} \\
> r_a &= \frac{a\left(1 - e\right)\left(1 + e\right)}{1 - e} \quad &\text{(the same substitution, for the ellipse)} \\
> &= a\left(1 + e\right) \quad &\text{(simplify)} \\
> e \geq 1:\quad 1 + e\cos\theta &= 0\ \ \text{at}\ \ \cos\theta = -\frac1e \quad &\text{(the denominator vanishes: $r$ grows without bound, no apocentre)}
> \end{aligned}$$
>
> $$\boxed{r_p = \frac{p}{1 + e} = a\left(1 - e\right),\qquad r_a = \frac{p}{1 - e} = a\left(1 + e\right),\qquad p = a\left(1 - e^2\right),\qquad b = a\sqrt{1 - e^2}}$$
>
> **Units:** $\mathrm m$
> **Meaning:** the point of the trajectory closest to the focus is the periapsis or pericentre, at the polar angle zero; for an ellipse the farthest point is the apoapsis or apocentre, at the angle pi; about the Earth they are the perigee and apogee, about the Sun the perihelion and aphelion (Notes.pdf, Sec. 8.4; [Lecture 4, Slide 14]). Two parameters, $p$ and $e$, fix the geometry of a conic orbit, and it is common to use $a$ instead of $p$. The semi-major axis is positive for circles and ellipses, infinite for parabolas and negative for hyperbolas (the table of [Lecture 4, Slide 14]); the pericentre formula in terms of $a$ holds for the hyperbola too, the apocentre one only for the ellipse.

## 8. Kepler's third law

The area of the ellipse and the constant areal velocity give the period of the orbit (Notes.pdf, Sec. 8.4; [Lecture 4, Slide 15]). The area of an ellipse of semi-axes $a$ and $b$ is pi times their product; the box derives it as an integral.

![[attachments/EM-T/t4-ellipse-area.svg]]

> [!derivation] Area of an ellipse
> **Law:** area as the integral of the height of the curve; symmetry about both axes; substitution with its differential; Barrow's rule
> **Source:** [Lecture 4, Slide 15]; Notes.pdf, Sec. 8.4
>
> With the coordinate $X$ measured from the centre of the ellipse along the major axis, the upper half of the curve has the height $b$ times the square root of one minus the square of $X/a$. The ellipse is symmetric about both of its axes, so its area is four times the area of the quarter with $X$ and $y$ positive. The substitution uses the angle $\phi$, with $X$ equal to $a\sin\phi$.
>
> $$\begin{aligned}
> \mathcal A_e &= 4\int_0^{a} b\sqrt{1 - \frac{X^2}{a^2}}\;dX \quad &\text{(four quarters; height of the upper half)} \\
> X &= a\sin\phi,\qquad dX = a\cos\phi\,d\phi \quad &\text{(substitution and its differential)} \\
> X = 0 \to \phi = 0,\qquad X &= a \to \phi = \frac{\pi}{2} \quad &\text{(new limits)} \\
> \sqrt{1 - \sin^2\phi} &= \cos\phi \quad &\text{(Pythagoras; the cosine is not negative on the interval)} \\
> \mathcal A_e &= 4\int_0^{\pi/2} b\cos\phi\;a\cos\phi\,d\phi \quad &\text{(substitute)} \\
> &= 4ab\int_0^{\pi/2}\frac{1 + \cos 2\phi}{2}\,d\phi \quad &\text{($\cos^2\phi = (1 + \cos 2\phi)/2$)} \\
> &= 4ab\left[\frac{\phi}{2} + \frac{\sin 2\phi}{4}\right]_0^{\pi/2} \quad &\text{(antiderivative)} \\
> &= 4ab\left(\frac{\pi}{4} + \frac{\sin\pi}{4} - 0 - \frac{\sin 0}{4}\right) \quad &\text{(Barrow's rule with both limits)} \\
> &= \pi a b \quad &\text{($\sin\pi = \sin 0 = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathcal A_e = \pi a b}$$
>
> **Units:** $\mathrm m\cdot\mathrm m = \mathrm{m^2}$
> **Meaning:** for a circle, with equal semi-axes, it is the area pi times the square of the radius; the ellipse is the circle of radius $a$ shrunk by the factor $b/a$ along the minor axis, and so is its area.

> [!derivation] The period of an elliptic orbit: Kepler's third law
> **Law:** the constant areal velocity integrated over one period; the semi-parameter in terms of $h$ and of $a$; one operation per row
> **Source:** Notes.pdf, Eq. 8.16; Notes.pdf, Eq. 8.17; Notes.pdf, Eq. 8.18; Notes.pdf, Eq. 8.8; [Lecture 4, Slide 15]
>
> In one period $\tau$ the radius sweeps the whole ellipse once.
>
> $$\begin{aligned}
> \int_0^{\tau}\frac{h}{2}\,dt &= \int_0^{\mathcal A_e} d\mathcal A \quad &\text{(Eq. 8.8: $d\mathcal A$ is $h/2$ times $dt$; integrate over one turn)} \\
> \frac{h}{2}\Big[t\Big]_0^{\tau} &= \Big[\mathcal A\Big]_0^{\mathcal A_e} \quad &\text{(antiderivatives; $h$ constant)} \\
> \frac{h\,\tau}{2} &= \mathcal A_e \quad &\text{(Barrow's rule on both sides)} \\
> \frac{h\,\tau}{2} &= \pi a b \quad &\text{(area of the ellipse, previous box)} \\
> \tau &= \frac{2\pi a b}{h} \quad &\text{(solve for $\tau$)} \\
> h^2 &= \mu p \quad &\text{(definition of $p$, Eq. 8.14)} \\
> &= \mu a\left(1 - e^2\right) \quad &\text{(Eq. 8.16)} \\
> \tau &= \frac{2\pi a\cdot a\sqrt{1 - e^2}}{\sqrt{\mu a}\,\sqrt{1 - e^2}} \quad &\text{(substitute $b$ and $h$)} \\
> &= \frac{2\pi a^2}{\sqrt{\mu a}} \quad &\text{(the square roots of $1 - e^2$ cancel)} \\
> &= \frac{2\pi}{\sqrt\mu}\,a^{3/2} \quad &\text{($a^2/\sqrt a = a^{3/2}$: Eq. 8.18)} \\
> \tau^2 &= \frac{4\pi^2}{\mu}\,a^3 \quad &\text{(square both sides)} \\
> \mu &= \left(\frac{2\pi}{\tau}\right)^2 a^3 \quad &\text{(solve for $\mu$: Eq. 8.17)}
> \end{aligned}$$
>
> $$\boxed{\tau = 2\pi\sqrt{\frac{a^3}{\mu}},\qquad \tau^2 = \frac{4\pi^2}{\mu}\,a^3}$$
>
> **Units:** $\sqrt{\mathrm{m^3}/(\mathrm{m^3\,s^{-2}})} = \mathrm s$
> **Meaning:** Kepler's third law: the square of the period is proportional to the cube of the semi-major axis, with the same constant for every orbit about the same body; the period does not depend on the eccentricity. The relation gives the time of flight around a closed orbit (Notes.pdf, Sec. 8.4).

> [!warning] Source issue: Notes.pdf, Sec. 8.4, the statement of the third law
> After Eq. 8.17 (printed p. 73) the notes write that "the square of the spacecraft" is proportional to the cube of the major axis; the word "period" is missing, as the statement of Notes.pdf, Sec. 8.1 and [Lecture 4, Slide 8] confirm. Kepler's statement uses the major axis and Eq. 8.17 the semi-major axis $a$; since one is twice the other, the cubes are proportional and both statements hold.

## 9. The vis-viva equation and the characteristic velocities

The only force of the problem, gravity, is conservative, so the mechanical energy of the particle is conserved; its equation could replace one of the projections of Newton's second law (Notes.pdf, Sec. 8.5). Per unit mass it is the specific mechanical energy $\xi$; its constant value is found at the pericentre and the apocentre ([Lecture 4, Slide 16]).

> [!derivation] The specific mechanical energy and its value
> **Law:** conservation of mechanical energy per unit mass; the radial velocity vanishes at the pericentre; the angular momentum gives the speed there
> **Source:** Notes.pdf, Eq. 8.19; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.2; Notes.pdf, Eq. 8.7; Notes.pdf, Eq. 8.14; [Lecture 4, Slide 16]
>
> At the pericentre the derivative of the orbit equation with respect to the angle vanishes, so the radial velocity is zero and the speed is the transverse velocity alone.
>
> $$\begin{aligned}
> \xi &= \frac{T_0 + V_0}{m} \quad &\text{(mechanical energy per unit mass, constant: Eq. 4.31)} \\
> &= \frac{v^2}{2} - \frac{\mu}{r} \quad &\text{(Eq. 4.2 and the potential of Section 5)} \\
> v^2 &= \dot r^2 + r^2\dot\theta^2 \quad &\text{(square of the polar velocity, an orthonormal basis)} \\
> \frac{dr}{d\theta} &= \frac{p\,e\sin\theta}{\left(1 + e\cos\theta\right)^2} \quad &\text{(derivative of Eq. 8.14, chain rule)} \\
> \dot r\big|_{\theta = 0} &= \frac{dr}{d\theta}\Big|_{\theta = 0}\,\dot\theta = 0 \quad &\text{(chain rule; $\sin 0 = 0$)} \\
> v_p &= r_p\,\dot\theta\big|_{\theta = 0} \quad &\text{(only the transverse velocity remains)} \\
> &= \frac{h}{r_p} \quad &\text{(Eq. 8.7: the rate of $\theta$ is $h/r^2$)} \\
> &= \frac{\mu\left(1 + e\right)}{h} \quad &\text{($r_p = p/(1 + e)$ and $p = h^2/\mu$)} \\
> \xi &= \frac{\mu^2\left(1 + e\right)^2}{2h^2} - \frac{\mu^2\left(1 + e\right)}{h^2} \quad &\text{(the energy at the pericentre)} \\
> &= \frac{\mu^2\left(1 + e\right)}{2h^2}\left[\left(1 + e\right) - 2\right] \quad &\text{(common factor)} \\
> &= \frac{\mu^2\left(e^2 - 1\right)}{2h^2} \quad &\text{($(1 + e)(e - 1) = e^2 - 1$)} \\
> &= \frac{\mu^2\left(e^2 - 1\right)}{2\mu a\left(1 - e^2\right)} \quad &\text{(Eq. 8.16, for $e \neq 1$)} \\
> &= -\frac{\mu}{2a} \quad &\text{(simplify)} \\
> v_a &= \frac{h}{r_a} \quad &\text{(apocentre of an ellipse: $\sin\pi = 0$, so the radial velocity vanishes too)} \\
> &= \frac{\mu\left(1 - e\right)}{h} \quad &\text{($r_a = p/(1 - e)$ and $p = h^2/\mu$)} \\
> \frac{v_a^2}{2} - \frac{\mu}{r_a} &= \frac{\mu^2\left(1 - e\right)}{2h^2}\left[\left(1 - e\right) - 2\right] \quad &\text{(the energy there, common factor)} \\
> &= \frac{\mu^2\left(e^2 - 1\right)}{2h^2} \quad &\text{(the same value: a check)} \\
> v^2 &= \frac{2\mu}{r} - \frac{\mu}{a} \quad &\text{(Eq. 8.19 solved for $v^2$)}
> \end{aligned}$$
>
> $$\boxed{\xi = \frac{v^2}{2} - \frac{\mu}{r} = \frac{\mu^2\left(e^2 - 1\right)}{2h^2} = -\frac{\mu}{2a}}$$
>
> **Units:** $\mathrm{m^2\,s^{-2}} = \mathrm{J\,kg^{-1}}$ in every term
> **Meaning:** Eq. 8.19, the vis-viva equation: the speed at any distance follows from the distance and the semi-major axis alone. The energy is negative for ellipses and circles, zero for parabolas and positive for hyperbolas, since it has the sign of the square of $e$ minus one ([Lecture 4, Slide 16]); a bound orbit has negative energy, and the larger its semi-major axis, the closer to zero.

> [!derivation] Speeds at the pericentre and the apocentre
> **Law:** the speeds of the previous box with the angular momentum in terms of $a$
> **Source:** [Lecture 4, Slide 16]; Notes.pdf, Eq. 8.16
>
> $$\begin{aligned}
> v_p^2 &= \frac{\mu^2\left(1 + e\right)^2}{h^2} \quad &\text{(previous box, squared)} \\
> &= \frac{\mu^2\left(1 + e\right)^2}{\mu a\left(1 - e\right)\left(1 + e\right)} \quad &\text{(Eq. 8.16; $1 - e^2 = (1 - e)(1 + e)$)} \\
> &= \frac{\mu}{a}\,\frac{1 + e}{1 - e} \quad &\text{(simplify)} \\
> v_a^2 &= \frac{\mu^2\left(1 - e\right)^2}{\mu a\left(1 - e\right)\left(1 + e\right)} \quad &\text{(the same for the apocentre)} \\
> &= \frac{\mu}{a}\,\frac{1 - e}{1 + e} \quad &\text{(simplify)}
> \end{aligned}$$
>
> $$\boxed{v_p = \sqrt{\frac{\mu}{a}\,\frac{1 + e}{1 - e}},\qquad v_a = \sqrt{\frac{\mu}{a}\,\frac{1 - e}{1 + e}}}$$
>
> **Units:** $\sqrt{\mathrm{m^3\,s^{-2}}/\mathrm m} = \mathrm{m\,s^{-1}}$
> **Meaning:** the particle is fastest at the pericentre and slowest at the apocentre; the ratio of the two speeds is the inverse ratio of the distances, because the product of distance and speed is $h$ at both points, where the velocity is perpendicular to the radius.

> [!derivation] Circular velocity and escape velocity
> **Law:** the vis-viva equation for a circle; reaching infinite distance with a speed that is real
> **Source:** Notes.pdf, Eq. 8.20; Notes.pdf, Eq. 8.21; Notes.pdf, Eq. 8.19; [Lecture 4, Slide 16]
>
> On a circular orbit the distance is constant and equal to $a$. For the escape, the speed at the distance $r$ must make the energy large enough for the square of the speed to stay non-negative as the distance grows without bound; the smallest such speed gives zero energy.
>
> $$\begin{aligned}
> v_c^2 &= \frac{2\mu}{r} - \frac{\mu}{r} \quad &\text{(vis-viva with $a = r$)} \\
> &= \frac{\mu}{r} \quad &\text{(subtract: Eq. 8.20)} \\
> \frac{v^2}{2} &= \xi + \frac{\mu}{r} \quad &\text{(Eq. 8.19 solved for the kinetic energy per unit mass)} \\
> \lim_{r\to\infty}\frac{v^2}{2} &= \xi \quad &\text{(the potential term goes to zero)} \\
> \xi &\geq 0 \quad &\text{(a speed squared cannot be negative)} \\
> \frac{v_e^2}{2} - \frac{\mu}{r} &= 0 \quad &\text{(the minimum: zero energy)} \\
> v_e^2 &= \frac{2\mu}{r} \quad &\text{(solve: Eq. 8.21)} \\
> \frac{v_e}{v_c} &= \sqrt{\frac{2\mu/r}{\mu/r}} \quad &\text{(ratio at the same distance)} \\
> &= \sqrt2 \quad &\text{(simplify)}
> \end{aligned}$$
>
> $$\boxed{v_c = \sqrt{\frac{\mu}{r}},\qquad v_e = \sqrt{\frac{2\mu}{r}} = \sqrt2\,v_c}$$
>
> **Units:** $\mathrm{m\,s^{-1}}$
> **Meaning:** the circular velocity is the speed of a circular orbit of radius $r$; the escape velocity is the minimum speed that takes the spacecraft to infinite distance, on a parabola, and it is the square root of two times the circular velocity (Notes.pdf, Sec. 8.5). Both decrease with the distance to the attracting body ([Lecture 4, Slide 16]). The slide writes the circular velocity with $a$ and the notes with $r$: on a circle they are the same length.

## 10. Extension: effective potential, radial band and the centre

This section is an extension: neither Sec. 4.8.1 nor Chapter 8 of the notes write it, but it applies to central forces the regions of existence of Notes.pdf, Sec. 7.7 and the allowed regions of Notes.pdf, Eq. 4.28: a first integral that relates the square of the rate of one coordinate to that coordinate bounds the motion, and the boundaries are visualized with an effective potential. It recovers the orbit classes of Sections 7 and 9 without solving the orbit equation, and it settles the fifth property of Notes.pdf, Sec. 4.8.1, that the particle can never reach the centre unless the angular momentum is zero.

> [!derivation] Extension: the radial motion as a one-dimensional problem
> **Law:** conservation of mechanical energy for a conservative central force; the first integral of the angular momentum eliminates the angle; non-negative square of the radial rate
> **Source:** Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 8.7
>
> The central force derives from a potential energy $V_0$ that depends only on the distance; $f$ is its radial component per unit mass. The gradient of a function of $r$ is its derivative with respect to $r$ times the gradient of $r$, which is $\mathbf e_r$ (Section 5). The specific angular momentum $h$ is constant (Section 6, whose steps do not use the form of the force).
>
> $$\begin{aligned}
> f &= -\frac{d}{dr}\left(\frac{V_0}{m}\right) \quad &\text{(Eq. 4.20 divided by $m$, with the chain rule)} \\
> \xi &= \tfrac12\left(\dot r^2 + r^2\dot\theta^2\right) + \frac{V_0}{m} \quad &\text{(energy per unit mass, Eq. 4.31; polar velocity)} \\
> r^2\dot\theta^2 &= \frac{h^2}{r^2} \quad &\text{(Eq. 8.7: the rate of $\theta$ is $h/r^2$)} \\
> \xi &= \tfrac12\,\dot r^2 + \frac{h^2}{2r^2} + \frac{V_0}{m} \quad &\text{(substitute)} \\
> v_{\mathrm{eff}}(r) &= \frac{V_0}{m} + \frac{h^2}{2r^2} \quad &\text{(definition of the effective potential per unit mass)} \\
> \dot r^2 &= 2\left(\xi - v_{\mathrm{eff}}(r)\right) \quad &\text{(solve for the square of the radial rate)} \\
> v_{\mathrm{eff}}(r) &\leq \xi \quad &\text{(the square is not negative: Eq. 4.28, Sec. 7.7)} \\
> \ddot r &= r\dot\theta^2 + f \quad &\text{(radial equation of motion of Section 6, with the force per unit mass $f$)} \\
> &= \frac{h^2}{r^3} - \frac{d}{dr}\left(\frac{V_0}{m}\right) \quad &\text{(Eq. 8.7; first row)} \\
> \frac{d}{dr}\left(\frac{h^2}{2r^2}\right) &= -\frac{h^2}{r^3} \quad &\text{(derivative of $r^{-2}$)} \\
> \ddot r &= -\frac{dv_{\mathrm{eff}}}{dr} \quad &\text{(the two rows above)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12\,\dot r^2 + v_{\mathrm{eff}}(r) = \xi,\qquad v_{\mathrm{eff}} = \frac{V_0}{m} + \frac{h^2}{2r^2},\qquad v_{\mathrm{eff}}(r) \leq \xi,\qquad \ddot r = -\frac{dv_{\mathrm{eff}}}{dr}}$$
>
> **Units:** $\mathrm{m^2\,s^{-2}}$ in the energy terms; $\mathrm{m\,s^{-2}}$ in the radial equation
> **Meaning:** the distance moves like a particle on a line in the potential $v_{\mathrm{eff}}$: the angular momentum adds a repulsive term, the energy of the transverse motion, that grows without bound near the centre. The motion is confined to the distances where the effective potential does not exceed the energy, and its boundaries, where the radial rate vanishes, are the roots of the equation of the effective potential equal to the energy.

![[attachments/EM-T/t4-effective-potential.svg]]

> [!derivation] Extension: the effective potential of gravity and the radial band
> **Law:** the effective potential of the gravity potential; its minimum; the turning points as roots of a quadratic; the energy of Section 9
> **Source:** Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 8.19; Notes.pdf, Eq. 8.14
>
> The turning points are computed for an energy $\xi$ different from zero, and then for zero energy.
>
> $$\begin{aligned}
> v_{\mathrm{eff}} &= -\frac{\mu}{r} + \frac{h^2}{2r^2} \quad &\text{(previous box with the potential of Section 5)} \\
> \frac{dv_{\mathrm{eff}}}{dr} &= \frac{\mu}{r^2} - \frac{h^2}{r^3} \quad &\text{(derivative)} \\
> &= \frac{\mu r - h^2}{r^3} \quad &\text{(common denominator: negative below $h^2/\mu$, positive above)} \\
> &= 0 \ \Leftrightarrow\ r = \frac{h^2}{\mu} = p \quad &\text{(the numerator vanishes; definition of $p$)} \\
> v_{\mathrm{eff}}(p) &= -\frac{\mu^2}{h^2} + \frac{\mu^2}{2h^2} \quad &\text{(substitute $r = h^2/\mu$)} \\
> &= -\frac{\mu^2}{2h^2} \quad &\text{(the minimum: the derivative changes from negative to positive at $p$)} \\
> -\frac{\mu}{r} + \frac{h^2}{2r^2} &= \xi \quad &\text{(turning points: the radial rate vanishes)} \\
> \xi r^2 + \mu r - \frac{h^2}{2} &= 0 \quad &\text{(multiply by $r^2$; a quadratic in $r$)} \\
> r &= \frac{-\mu \pm \sqrt{\mu^2 + 2\xi h^2}}{2\xi} \quad &\text{(quadratic formula, $\xi \neq 0$)} \\
> \mu^2 + 2\xi h^2 &= \mu^2 + \mu^2\left(e^2 - 1\right) \quad &\text{(energy of Section 9)} \\
> &= \mu^2 e^2 \quad &\text{(simplify)} \\
> r &= \frac{\mu\left(-1 \pm e\right)h^2}{\mu^2\left(e^2 - 1\right)} \quad &\text{(square root $\mu e$; $1/(2\xi) = h^2/(\mu^2(e^2 - 1))$)} \\
> r_{+} &= \frac{(e - 1)\,p}{(e - 1)(e + 1)} = \frac{p}{1 + e} = r_p \quad &\text{(upper sign; $h^2/\mu = p$, $e^2 - 1 = (e - 1)(e + 1)$)} \\
> r_{-} &= \frac{-(1 + e)\,p}{(e - 1)(e + 1)} = \frac{p}{1 - e} = r_a \quad &\text{(lower sign, the same factorization)} \\
> \xi = 0:\quad \mu r - \frac{h^2}{2} &= 0 \ \Rightarrow\ r = \frac{p}{2} \quad &\text{(the quadratic becomes linear: the pericentre of the parabola)}
> \end{aligned}$$
>
> $$\boxed{v_{\mathrm{eff}} = -\frac{\mu}{r} + \frac{h^2}{2r^2},\quad \min v_{\mathrm{eff}} = -\frac{\mu^2}{2h^2}\ \text{at}\ r = p;\qquad \text{turning points}\ r_p = \frac{p}{1 + e},\ r_a = \frac{p}{1 - e}}$$
>
> **Units:** $\mathrm{m^2\,s^{-2}}$; distances in $\mathrm m$
> **Meaning:** at the minimum energy the only allowed distance is $p$, a circular orbit with zero eccentricity; for negative energies above the minimum the distance oscillates in the band between the pericentre and the apocentre, an ellipse; for zero or positive energy only the pericentre bounds the motion and the particle goes to infinite distance, a parabola or a hyperbola. The turning points are those of Section 7, found without solving the orbit equation; the apocentre root is negative, so not a distance, when $e$ exceeds one.

> [!derivation] Extension: a slightly disturbed circular orbit stays close to it
> **Law:** linearization of the radial equation about the minimum of the effective potential; characteristic equation
> **Source:** Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 8.7
>
> The orbit is written with the distance $r_c + \varepsilon$, with $r_c$ the radius of the circular orbit with the same $h$, which is $p$ (previous box), and $\varepsilon$ small.
>
> $$\begin{aligned}
> \ddot\varepsilon &= -\frac{dv_{\mathrm{eff}}}{dr}\Big|_{r_c + \varepsilon} \quad &\text{(radial equation; $r_c$ is constant)} \\
> &\approx -\frac{dv_{\mathrm{eff}}}{dr}\Big|_{r_c} - \frac{d^2 v_{\mathrm{eff}}}{dr^2}\Big|_{r_c}\varepsilon \quad &\text{(Taylor expansion to first order)} \\
> &= -\frac{d^2 v_{\mathrm{eff}}}{dr^2}\Big|_{r_c}\varepsilon \quad &\text{(the first derivative is zero at the minimum)} \\
> \frac{d^2 v_{\mathrm{eff}}}{dr^2} &= -\frac{2\mu}{r^3} + \frac{3h^2}{r^4} \quad &\text{(derivative of the first derivative of the previous box)} \\
> \frac{d^2 v_{\mathrm{eff}}}{dr^2}\Big|_{p} &= -\frac{2\mu}{p^3} + \frac{3\mu p}{p^4} \quad &\text{($h^2 = \mu p$)} \\
> &= \frac{\mu}{p^3} \quad &\text{(simplify: positive)} \\
> \ddot\varepsilon + \frac{\mu}{p^3}\,\varepsilon &= 0 \quad &\text{(linearized equation)} \\
> q^2 + \frac{\mu}{p^3} &= 0 \quad &\text{(characteristic equation, trial solution $e^{q t}$)} \\
> q &= \pm\,\mathrm i\sqrt{\mu/p^3} \quad &\text{(imaginary roots: a bounded oscillation)} \\
> \dot\theta\big|_{r = p} &= \frac{h}{p^2} \quad &\text{(rate of turn of the circular orbit, Eq. 8.7)} \\
> &= \frac{\sqrt{\mu p}}{p^2} \quad &\text{($h^2 = \mu p$)} \\
> &= \sqrt{\mu/p^3} \quad &\text{(simplify)}
> \end{aligned}$$
>
> $$\boxed{\ddot\varepsilon + \frac{\mu}{p^3}\,\varepsilon = 0:\quad \varepsilon\ \text{oscillates with the angular frequency}\ \sqrt{\mu/p^3},\ \text{equal to the rate of turn}}$$
>
> **Units:** $\mu/p^3$ in $\mathrm{m^3\,s^{-2}}/\mathrm{m^3} = \mathrm{s^{-2}}$
> **Meaning:** both roots are imaginary, so a small radial departure neither grows nor decays: it oscillates about the circular radius, and the circular orbit is stable. The radial oscillation has the frequency of the turn, so the distance returns to the same value after one revolution: the disturbed orbit closes, as the ellipse of small eccentricity of Section 7 does.

> [!derivation] Extension: can the particle reach the centre?
> **Law:** the allowed region of the effective potential near the centre; an inverse-cube attraction as a counterexample; integration of an inequality with Barrow's rule
> **Source:** Notes.pdf, Sec. 4.8.1; Notes.pdf, Sec. 7.7; Notes.pdf, Eq. 4.28
>
> First gravity, with $h$ not zero. Then the potential energy per unit mass minus $\kappa$ over the square of $r$, with $\kappa$ positive, an attraction that grows like the inverse cube of the distance, built for this note, with $\kappa$ larger than half the square of $h$, a particle moving inwards and an energy that is not negative.
>
> $$\begin{aligned}
> r^2\,v_{\mathrm{eff}} &= \frac{h^2}{2} - \mu r \quad &\text{(gravity: multiply $v_{\mathrm{eff}}$ by $r^2$)} \\
> \lim_{r\to 0} r^2\,v_{\mathrm{eff}} &= \frac{h^2}{2} > 0 \quad &\text{(so $v_{\mathrm{eff}}$ grows without bound as $r$ tends to $0$)} \\
> v_{\mathrm{eff}}(r) \leq \xi\ &\Rightarrow\ r \geq r_p > 0 \quad &\text{(previous boxes: the pericentre bounds the distance)} \\
> \frac{V_0}{m} &= -\frac{\kappa}{r^2} \quad &\text{(counterexample)} \\
> f &= -\frac{d}{dr}\left(-\frac{\kappa}{r^2}\right) = -\frac{2\kappa}{r^3} \quad &\text{(first extension box: $f$ negative, an attraction)} \\
> v_{\mathrm{eff}} &= \frac{h^2/2 - \kappa}{r^2} \quad &\text{(first extension box)} \\
> \left(r\dot r\right)^2 &= 2\xi r^2 + 2\kappa - h^2 \quad &\text{(energy: $\dot r^2 = 2(\xi - v_{\mathrm{eff}})$, times $r^2$)} \\
> &\geq 2\kappa - h^2 > 0 \quad &\text{($\xi$ not negative; $\kappa$ larger than half of $h^2$)} \\
> \frac{d}{dt}\left(r^2\right) = 2 r\dot r &\leq -2\sqrt{2\kappa - h^2} \quad &\text{(chain rule; $\dot r$ negative and never zero, so it stays negative)} \\
> \int_0^t\frac{d}{dt'}\left(r^2\right)dt' &\leq -2\sqrt{2\kappa - h^2}\int_0^t dt' \quad &\text{(integrate the inequality from $0$ to $t$)} \\
> r(t)^2 - r(0)^2 &\leq -2\sqrt{2\kappa - h^2}\;t \quad &\text{(antiderivatives and Barrow's rule on both sides)}
> \end{aligned}$$
>
> $$\boxed{\text{gravity},\ h \neq 0:\ r \geq r_p > 0;\qquad \frac{V_0}{m} = -\frac{\kappa}{r^2},\ \kappa > \frac{h^2}{2}:\ r = 0\ \text{is reached before}\ t = \frac{r(0)^2}{2\sqrt{2\kappa - h^2}}}$$
>
> **Units:** $\kappa$ in $\mathrm{m^4\,s^{-2}}$, like $h^2$; $r\dot r$ in $\mathrm{m^2\,s^{-1}}$; the time bound in $\mathrm{m^2}/(\mathrm{m^2\,s^{-1}}) = \mathrm s$
> **Meaning:** under gravity, a particle with angular momentum never comes closer to the centre than its pericentre; the repulsive term of the angular momentum dominates near the centre. But an attraction that grows near the centre at least as fast as the inverse cube of the distance can overcome it: in the counterexample the square of the distance decreases at least linearly in time, so it reaches zero in a finite time although the angular momentum is not zero.

> [!warning] Source issue: Notes.pdf, Sec. 4.8.1, property 5
> The fifth property of Notes.pdf, Sec. 4.8.1 (printed p. 52) states, for any central force, that the particle can never reach the centre unless its angular momentum about it is zero. The extension box above shows that it holds for gravity, but not for every central force: the inverse-cube attraction of the counterexample takes the particle to the centre in a finite time with a non-zero angular momentum. With zero angular momentum the particle moves on a line through the centre (Section 4), so it can reach it. [Lecture 4, Slide 7] does not list this property.

> [!key] Summary of Topic 4
> - The angular momentum of a particle about a point is the moment of its linear momentum about that point; it depends on the point and on the frame, and it is perpendicular to the arm and to the velocity. The torque of a force is its moment about the point; the torques of an action-reaction pair cancel when the two forces share their line of action (Section 1).
> - Differentiating the angular momentum gives its rate of change: the torque minus the cross product of the velocity of the pole with the linear momentum. About a fixed point it is the torque, a consequence of the second law that adds no new information; about a pole moving with constant velocity it holds with the angular momentum relative to the parallel frame (Section 2).
> - With zero torque about a fixed point the angular momentum is a constant vector, three scalar conservation laws; the total angular momentum of a system is constant when the external torque is zero. The heavy particle attracted to a point moves under a force central about the equilibrium point below it, on a circle with constant speed (Section 3).
> - A central force has zero torque about its centre, so the angular momentum about the centre is constant, the motion is planar, the angular rate grows as the distance decreases, and with zero angular momentum the motion is a straight line through the centre (Section 4).
> - Kepler's problem reduces exactly to the relative motion about the attracting body with the parameter $\mu$; it is central, conservative and independent of the mass of the particle (Section 5). The transverse equation gives the constant specific angular momentum $h$ and the constant areal velocity, Kepler's second law (Section 6).
> - In the variable one over the distance, the radial equation becomes a forced harmonic oscillator in the polar angle; its solution is a conic with a focus at the attracting body, of semi-parameter $p$ and eccentricity $e$: circle, ellipse, parabola or hyperbola, the ellipse proving Kepler's first law (Section 7).
> - The areal velocity integrated over one turn of the ellipse gives the period, whose square is proportional to the cube of the semi-major axis: Kepler's third law (Section 8).
> - The specific energy depends only on the semi-major axis (the vis-viva equation): negative for closed orbits, zero for the parabola, positive for the hyperbola; it gives the speeds at the pericentre and the apocentre, the circular velocity and the escape velocity, the square root of two times larger (Section 9).
> - Extension: the effective potential turns the radial motion into a one-dimensional problem; for gravity it recovers the orbit classes and the turning points, shows that the circular orbit is stable, and that a particle with angular momentum cannot reach the centre, which is not true for every central force (Section 10).
