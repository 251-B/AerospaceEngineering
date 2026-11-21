---
title: "Topic 2 - Dynamics of a Point Particle, Equilibrium and Oscillations"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/teoria/Notes.pdf"
type: "Theory"
language: "English"
tags:
  - theory
  - topic-2
  - point-particle
  - dynamics
  - newton-laws
  - work-energy
  - potential-energy
  - energy-conservation
  - equilibrium
  - stability
  - simple-pendulum
  - harmonic-oscillator
  - linearisation
---

# Topic 2 - Dynamics of a Point Particle, Equilibrium and Oscillations

> Dynamics asks what causes motion: in an inertial reference frame $S_0$ Newton's second law ties the rate of change of the linear momentum $\mathbf p_0$ of a particle to the resultant force $\mathbf F$ and gives the differential equations whose integration, with the initial position and velocity, yields the trajectory. Dotting that law with the velocity turns it into a statement about energy: the power of the forces changes the kinetic energy $T_0$, a force that derives from a potential energy $V_0$ can be absorbed into a mechanical energy $E_0$ that stays constant when no other force works, and the shape of $V_0$ alone shows the allowed regions, the equilibria (its critical points) and their stability (its minima). Near a stable equilibrium every such system behaves, to first order, as a harmonic oscillator, free or damped, driven or not, which is why the simple pendulum leads to the oscillator and to the linearisation of the equations of motion.

This note follows `Notes.pdf` Chapter 4, Sections 4.1 to 4.7 (Dynamics of the point particle, Eqs. 4.1 to 4.47: force, linear momentum and kinetic energy; Newton's laws; the equations of motion; power, work and potential energy; the conservation of mechanical energy; equilibrium; the simple pendulum) and Chapter 5 (The harmonic oscillator, Eqs. 5.1 to 5.47: undamped motion, the complex representation, the damped oscillator with small, large and critical damping, the oscillator under a periodic force and resonance), with the decks of Lecture 2 (Particle dynamics, Slides 1 to 23) and Lecture 6 (Oscillations, Slides 1 to 15: linear equations with constant coefficients, complex exponentials, the free oscillator without damping and with small, large and critical damping, the forced oscillator, resonance and the linearisation about an equilibrium), in the order of the notes. Two topics that neither the notes nor the slides treat are added as extensions, marked as such: the beats of the undamped forced oscillator and the bead on a rotating hoop with its bifurcation. Sections 4.8 (angular momentum and central forces) and 4.9 (dynamics of relative motion) of the same chapter belong to Topics 4 and 5. Kinematic results of Topic 1 are cited, not re-derived: the velocity and acceleration (Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4) and their Cartesian (Eqs. 2.5 to 2.7), intrinsic (Eqs. 2.16 to 2.18) and cylindrical (Eqs. 2.23 to 2.29) forms, the dot product (Eqs. 1.24 to 1.28), the rules of differentiation of vectors (Eqs. 1.64 to 1.67) and the gradient and curl (Eqs. 1.74, 1.76 and 1.77). See also [[Concept - Newton Laws and Equations of Motion]], [[Concept - Work Power and Kinetic Energy Theorem]], [[Concept - Conservative Forces and Potential Energy]], [[Concept - Conservation of Mechanical Energy and Energy Diagrams]], [[Concept - Equilibrium Configurations and Stability Criteria]] and [[Concept - The Simple Pendulum Nonlinear Dynamics and Linearization]].

| Symbol | Meaning |
| :--- | :--- |
| $S_0 : \{O;\mathcal B_0\}$, $\mathcal B_0 : \{\mathbf i,\mathbf j,\mathbf k\}$ | inertial reference frame and its basis (also written $\mathbf i_0$, $\mathbf j_0$, $\mathbf k_0$, as on the slides); axes $Ox$, $Oy$, $Oz$ |
| $S_1$, $O_1$, $\mathbf v_0^{O_1}$ | a second frame that does not rotate with respect to $S_0$, its origin, and the velocity of that origin with respect to $S_0$ |
| $P$, $m$ | the point particle and its mass (the slides write $m^{\mathrm P}$); $m$ is constant |
| $Q$, $m^{\mathrm Q}$ | a second particle (Slides 6, 8 and 16) and its mass |
| $\mathbf r_0^P$, $\mathbf v_0^P$, $\mathbf a_0^P$ | position, velocity and acceleration of $P$ with respect to $S_0$ (Topic 1) |
| $v_0^P$, $(v_0^P)^2$ | speed of $P$ and its square, $\mathbf v_0^P\cdot\mathbf v_0^P$ |
| $x, y, z$; $\dot x$, $\ddot x$ | Cartesian coordinates of $P$ in $S_0$ and their time derivatives |
| $\mathbf F$, $F_x$, $F_y$, $F_z$ | resultant of the forces on $P$ and its components in $\mathcal B_0$ |
| $\mathbf F_1, \mathbf F_2, \dots$ | individual forces acting on $P$ |
| $\mathbf F_C$, $\mathbf F_N$ | the conservative part and the non-conservative part of the resultant ([Lecture 2, Slide 19]) |
| $\mathbf p_0$ (also $\mathbf p_0^P$) | linear momentum of $P$ with respect to $S_0$ |
| $T_0$ (also $T_0^P$) | kinetic energy of $P$ with respect to $S_0$ |
| $\dot W_0$ | power of a force on $P$, as seen from $S_0$ |
| $W_0(t_1,t_2)$, $\delta W_0$ | work of a force between the instants $t_1$ and $t_2$, and work in a differential time interval $dt$ |
| $\Gamma$ | a path (curve) followed between two positions; $\oint_\Gamma$ when it is closed |
| $\Gamma_1$, $\Gamma_2$, $\Gamma'$ | two paths between the same two positions |
| $\alpha_F$ | angle between a force and the velocity |
| $\sigma$ | parameter along a path $\Gamma$, used to write a line integral as an ordinary integral |
| $\sigma_*$, $\sigma_P$ | values of $\sigma$ at the reference position and at the current position of $P$ |
| $x_1$, $x_2$, $x_{\mathrm{ref}}$ | positions on a line at $t_1$ and $t_2$, and the reference position of a one-dimensional potential |
| $x'$, $t'$, $R'$, $\eta$ | integration (dummy) variables |
| $\mathbf r_{0,1}^P$, $\mathbf r_{0,2}^P$; $\mathbf r_{0,*}^P$ | positions of $P$ at $t_1$ and $t_2$; reference position at which the potential energy is zero (the notes write $\mathbf r_{0,1}^P$ for it in Eq. 4.14) |
| $V_0$ | potential energy of a conservative force (a scalar field of the position) |
| $E_0$ (also $E_0^P$) | mechanical energy, kinetic plus potential |
| $T_{0,1}$, $V_{0,1}$, $T_{0,2}$, $V_{0,2}$ | values of $T_0$ and $V_0$ at $t_1$ and $t_2$ |
| $E_{0,1}$, $E_{0,2}$, $E_{0,3}$ | three levels of mechanical energy in the energy diagrams (Notes.pdf Fig. 4.2 and Fig. 4.4) |
| $g$, $\mathbf g$ | acceleration of gravity and its vector, pointing down |
| $k$ | stiffness of a linear spring of zero natural length ([Lecture 2, Slide 16]) |
| $k_0$, $q^{\mathrm P}$, $q^{\mathrm Q}$ | electrostatic constant and the charges of $P$ and $Q$ ([Lecture 2, Slide 16]) |
| $c_1$, $c_2$ | constants of the velocity of the example of [Lecture 2, Slide 12] (the slide writes $a$ and $b$) |
| $c_3$, $c_4$ | constants of the forces of [Lecture 2, Slides 17-18] (the slides write $a$ and $b$) |
| $R_*$, $R_0$ | radius at the reference position (Slide 17) and radius of the closed circular path (Slide 18) |
| $d$ | distance between the particles $P$ and $Q$ (Slide 16) |
| $w$ | inner argument of the second cosine of the example potential of Notes.pdf Fig. 4.1 |
| $C_1, \dots, C_6$ | integration constants of the equations of motion (Eqs. 4.7 to 4.9; Section 6) |
| $t_{\mathrm{apex}}$, $t_{\mathrm L}$ | instants of the apex and of the landing in the example of [Lecture 2, Slide 11] |
| $R$, $\theta$, $z$; $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf e_z$ | cylindrical coordinates and their local basis (Notes.pdf, Sec. 2.6.2); in Section 7 the pendulum angle $\theta$ is measured from the downward vertical |
| $\mathbf e_t$, $\mathbf e_n$; $s$; $\rho$ | tangent and normal unit vectors of the trajectory, the arc length and the radius of curvature (Topic 1) |
| $F_t$ | tension of the pendulum rod (magnitude), Section 7; not to be confused with the tangential component of a force, written $\mathbf F\cdot\mathbf e_t$ |
| $x^*$, $\mathbf r_0^*$, $\theta^*_{\mathrm{eq}}$ | an equilibrium position (in one dimension, in space, and of the pendulum) |
| $\xi$ | small displacement from an equilibrium position |
| $p$ | root of the characteristic equation of a linear differential equation |
| $\omega_0$, $p_1$ | angular frequency of the small oscillations about a minimum of the potential, and growth rate of the small departures from a maximum |
| $\xi_0$, $\dot\xi_0$ | initial displacement and velocity of a small motion about an equilibrium |
| $\varepsilon_r$, $\varepsilon_v$, $\delta_r$, $\delta_v$ | tolerances of the definition of stability ([Lecture 2, Slide 21]) |
| $\Delta V$ | depth of a potential well around a minimum, used in the stability argument of Section 6 |
| $\ell$ | length of the pendulum rod |
| $H$ | foot of the perpendicular from the bob to the vertical through $O$ |
| $\mathbf F_g$, $\mathbf F_t$ | weight of the bob and force of the rod on it |
| $C$ | constant of the first integral of the pendulum (Eq. 4.39) |
| $n$ | any integer, numbering the equilibria of the pendulum |
| $\theta_{\mathrm{pol}}$ | standard polar angle of the pendulum bob, measured from $Ox$ counterclockwise |
| $[{}_0R_{\mathrm{pol}}]$ | change of basis matrix from the polar basis of the pendulum to $\mathcal B_0$ |
| $\theta^*$, $\pm\theta^*$ | amplitude of a pendulum oscillation and its two turning points |
| $v_{0,0}^P$, $v_{0,1}^P$ | speed of the bob at its lowest point at the start, and at the upward vertical |
| $\tau$, $t^*$ | period of the oscillation, and the instant at which the bob reaches $\theta^*$ ($-\theta^*$ at $-t^*$) |
| $\tilde V_0$ | potential energy of the linearised pendulum |
| $u$ | substitution variable of the period integral |
| $x$, $\dot x$, $\ddot x$ (Sections 8 to 12) | displacement of the oscillator along $Ox$ from the position where the spring is relaxed, and its time derivatives; as in Chapter 5 of the notes, the indices $P$ and $0$ are dropped for the single particle in the single frame $S_0$ |
| $V$, $E$, $T$ (Sections 8 to 14) | potential, mechanical and kinetic energy with the indices dropped (the $V_0$, $E_0$, $T_0$ of Sections 4 to 7) |
| $\tilde f(t)$ | forcing term of the general equation of a harmonic oscillator (the notes and [Lecture 6, Slide 3] write $f(t)$; here $f$ is the frequency) |
| $\xi$, $b_2$, $b_1$, $b_0$ | generalised coordinate (the notes' name; near an equilibrium it is the small displacement defined above) and the constant coefficients of a linear second-order equation $b_2\ddot\xi + b_1\dot\xi + b_0\xi = \tilde f(t)$ ([Lecture 6, Slide 3] writes $a$, $b$, $c$ and $y$) |
| $\lambda$ | damping constant of the viscous damper, in $\mathrm{N\,s/m}$ |
| $F_x(t)$ | external force applied along $Ox$ ([Lecture 6, Slide 5]; the notes write $F(t)$) |
| $\mathbf F_k$, $\mathbf F_\lambda$, $\mathbf N_s$ | force of the spring, force of the damper, and the vertical reaction of the smooth support on the mass, Section 8 |
| $\omega_0$ (Sections 8 to 13) | natural angular frequency of the undamped oscillator, $\sqrt{k/m}$ (the $\omega_0$ of Section 6 with $k$ the second derivative of the potential) |
| $\gamma$ | damping coefficient $\lambda/(2m)$, in $\mathrm{s^{-1}}$ ([Lecture 6, Slide 5] also calls it damping ratio) |
| $\gamma/\omega_0$ | dimensionless damping ratio, the abscissa of [Lecture 6, Slide 10]: below one, equal to one and above one for small, critical and large damping |
| $\omega$ | angular frequency of the damped oscillator, $\sqrt{\omega_0^2 - \gamma^2}$ |
| $\gamma_+$, $\gamma_-$ | the two decay rates of the overdamped oscillator, $\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$ |
| $p_+$, $p_-$ | the two roots of a characteristic equation ([Lecture 6, Slides 3, 8 and 9] write $p_1$, $p_2$; here $p_1$ is the growth rate of Section 6) |
| $D_1$, $D_2$ | constants of a linear combination of two solutions (Notes.pdf, Eq. 5.5 writes $a_1$, $a_2$; [Lecture 6, Slides 3 and 6] write $A_1$, $A_2$) |
| $x_0$, $\dot x_0$ | initial displacement and initial velocity of the oscillator, at $t = 0$ |
| $a$, $\phi$ | amplitude and initial phase of a free oscillation ($\phi$ is the phase of Chapter 5, not an angle of a basis) |
| $f$ | frequency, the number of oscillations per unit time, in $\mathrm{Hz}$ |
| $i$, $z$, $z^*$ | imaginary unit (italic; the bold $\mathbf i$ is the unit vector), a complex solution (Sections 9 to 12; not the Cartesian coordinate $z$) and its complex conjugate |
| $A$, $A^*$ | complex amplitude of a free oscillation, $a\exp(i\phi)$, and its conjugate |
| $\Re$, $\Im$ | real part and imaginary part of a complex number |
| $\beta$ | real argument of Euler's relation (the notes write $\theta$, which is an angle of the particle in this note) |
| $t_r$ | relaxation time, the time in which the amplitude of the damped oscillator falls by the factor $1/e$ |
| $Q$ (Sections 10 to 12) | quality factor $\omega_0/(2\gamma)$; not the second particle $Q$ of Sections 1 to 4, which does not appear after Section 4 |
| $C_+$, $C_-$ | real constants of the overdamped solution ([Lecture 6, Slide 9]; the notes write $\tfrac12 A$ and $\tfrac12 B$) |
| $F_1$, $\omega_1$ | amplitude and angular frequency of the periodic applied force $F_1\cos(\omega_1 t)$ |
| $A_1$, $a_1$, $\phi_1$; $a_{1,\max}$ | complex amplitude, amplitude and phase of the forced (particular) response; $\phi_1$ is the phase lag behind the force; the amplitude at the resonant frequency |
| $z_h$, $z_p$; $x_h$, $x_p$ | homogeneous and particular solutions of the complex and of the real forced equations |
| $a_1 k/F_1$ | amplification factor: the forced amplitude divided by the static deflection $F_1/k$ |
| $\omega_1/\omega_0$ | frequency ratio, the abscissa of the amplification and phase curves |
| $B_1$ | coefficient of the particular solution of the undamped forced oscillator (beats, Section 11) |
| $F(x,\dot x)$ | force of a one-dimensional nonlinear system that may depend on the velocity (Section 13, [Lecture 6, Slide 15]) |
| $k$, $\lambda$ (Section 13) | equivalent stiffness and damping of a linearised system: minus the partial derivatives of $F$ with respect to $x$ and $\dot x$ at the equilibrium |
| $b$, $\Omega$, $\Omega_c$ | radius of the hoop, its constant rotation rate about the vertical, and the critical rate $\sqrt{g/b}$ (Section 14) |
| $\theta$ (Section 14) | angle of the bead from the downward vertical, measured in the plane of the hoop; $\theta^*_{\mathrm{eq}}$ is an equilibrium value of it |
| $S_h : \{O;\mathcal B_h\}$, $\mathcal B_h : \{\mathbf i_h, \mathbf j_h, \mathbf k\}$ | frame that turns with the hoop and its basis: $\mathbf i_h$ horizontal in the plane of the hoop, $\mathbf j_h$ normal to that plane |
| $[{}_0R_h]$ | change of basis matrix from $\mathcal B_h$ to $\mathcal B_0$ |
| $\mathbf u_r$, $\mathbf u_\theta$ | unit vectors in the plane of the hoop: from the centre to the bead, and tangent to the hoop in the sense of growing $\theta$ |
| $\mathbf N$, $N_r$, $N_h$ | reaction of the smooth hoop on the bead and its components along $\mathbf u_r$ and $\mathbf j_h$ |
| $V_{\mathrm{eff}}$ | effective potential of the bead on the rotating hoop |
| $\theta_e$ | angle of the off-axis equilibria of the bead, which exist above the critical rate |
| $\omega_{\mathrm{eq}}$ | angular frequency of the small oscillations of the bead about a stable equilibrium |

## 1. Force, linear momentum and kinetic energy

If kinematics relates positions, velocities and accelerations in the coordinates chosen to describe a problem, dynamics deals with the causes of motion and provides the differential equations that must be integrated to obtain the actual trajectory of the particle (Notes.pdf, Ch. 4). The basic equations of dynamics are the mathematical formulation of Newton's second law.

A force represents the action of one body on another, exerted by contact or at a distance, as gravitational, electric and magnetic forces are (Notes.pdf, Sec. 4.1). For particles and rigid bodies a force is described by its magnitude, its direction and its line of application: forces are sliding vectors. Their SI unit is the newton, $\mathrm N$, a kilogram metre per second squared; dimensionally $[\mathrm{M\,L\,T^{-2}}]$ ([Lecture 2, Slide 5]). Point particles have a physical property called mass, which in Newtonian mechanics is constant ([Lecture 2, Slide 3]).

![[attachments/EM-T/t2-momentum.svg]]

> [!derivation] Linear momentum of a point particle
> **Law:** definition of linear momentum
> **Source:** Notes.pdf, Eq. 4.1; [Lecture 2, Slide 3]
>
> $$\begin{aligned}
> \mathbf p_0 &= m\,\mathbf v_0^P \quad &\text{(definition, Eq. 4.1)} \\
> &= m\left.\frac{d\mathbf r_0^P}{dt}\right|_0 \quad &\text{(velocity in $S_0$, Eq. 2.3)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = m\,\mathbf v_0^P}$$
>
> **Units:** $[\mathrm M]\,[\mathrm{L\,T^{-1}}] = [\mathrm{M\,L\,T^{-1}}]$, $\mathrm{kg\,m/s}$
> **Meaning:** a vector with the direction and the sense of the velocity, because the mass is a positive scalar; it is tangent to the trajectory. Force and linear momentum are the basic quantities of the dynamics of point particles (Notes.pdf, Sec. 4.1).

> [!derivation] Kinetic energy of a point particle
> **Law:** definition of kinetic energy; square of the magnitude of a vector as its dot product with itself
> **Source:** Notes.pdf, Eq. 4.2; Notes.pdf, Eq. 1.24; Notes.pdf, Eq. 1.27; [Lecture 2, Slide 3]
>
> $$\begin{aligned}
> T_0 &= \tfrac12\,m\,(v_0^P)^2 \quad &\text{(definition, Eq. 4.2)} \\
> &= \tfrac12\,m\,\mathbf v_0^P\cdot\mathbf v_0^P \quad &\text{(Eq. 1.24 with the angle zero: $\mathbf A\cdot\mathbf A = A^2$)} \\
> &\geq 0 \quad &\text{($m > 0$ and $\mathbf v_0^P\cdot\mathbf v_0^P \geq 0$, Eq. 1.27)}
> \end{aligned}$$
>
> $$\boxed{T_0 = \tfrac12\,m\,\mathbf v_0^P\cdot\mathbf v_0^P \geq 0}$$
>
> **Units:** $[\mathrm M]\,[\mathrm{L\,T^{-1}}]^2 = [\mathrm{M\,L^2\,T^{-2}}]$, $\mathrm{kg\,m^2/s^2} = \mathrm J$
> **Meaning:** a scalar that is zero only when the particle is at rest in $S_0$. It depends on the speed only, not on the direction of motion.

Both $\mathbf p_0$ and $T_0$ are built from the velocity, so they depend on the reference frame in which they are computed, whereas the force does not; with several particles a superindex names the particle, as in $\mathbf p_0^P$ and $T_0^P$ (Notes.pdf, Sec. 4.1; [Lecture 2, Slide 3]). The next box makes the dependence explicit for a frame $S_1$ that translates with respect to $S_0$ at a constant velocity, using the composition of velocities quoted in the notes (Notes.pdf, p. 42, footnote 14; it is derived in Topic 5).

> [!derivation] Momentum and kinetic energy depend on the frame
> **Law:** composition of velocities for two frames without relative rotation; Eqs. 4.1 and 4.2 in each frame
> **Source:** Notes.pdf, Sec. 4.1; Notes.pdf, p. 42; Notes.pdf, Eq. 1.26; [Lecture 2, Slide 3]
>
> $$\begin{aligned}
> \mathbf v_0^P &= \mathbf v_1^P + \mathbf v_0^{O_1} \quad &\text{(composition of velocities for a non-rotating $S_1$, Notes p. 42)} \\
> \mathbf p_0 &= m\,\mathbf v_1^P + m\,\mathbf v_0^{O_1} \quad &\text{(multiply by $m$, Eq. 4.1)} \\
> &= \mathbf p_1 + m\,\mathbf v_0^{O_1} \quad &\text{(Eq. 4.1 written in $S_1$)} \\
> T_0 &= \tfrac12\,m\left(\mathbf v_1^P + \mathbf v_0^{O_1}\right)\cdot\left(\mathbf v_1^P + \mathbf v_0^{O_1}\right) \quad &\text{(Eq. 4.2)} \\
> &= \tfrac12\,m\left(\mathbf v_1^P\cdot\mathbf v_1^P + \mathbf v_1^P\cdot\mathbf v_0^{O_1} + \mathbf v_0^{O_1}\cdot\mathbf v_1^P + \mathbf v_0^{O_1}\cdot\mathbf v_0^{O_1}\right) \quad &\text{(distribute, Eq. 1.26)} \\
> &= \tfrac12\,m\,\mathbf v_1^P\cdot\mathbf v_1^P + m\,\mathbf v_1^P\cdot\mathbf v_0^{O_1} + \tfrac12\,m\,\mathbf v_0^{O_1}\cdot\mathbf v_0^{O_1} \quad &\text{(the two cross terms are equal by commutativity, Eq. 1.25: add them)} \\
> &= T_1 + m\,\mathbf v_1^P\cdot\mathbf v_0^{O_1} + \tfrac12\,m\,\mathbf v_0^{O_1}\cdot\mathbf v_0^{O_1} \quad &\text{(Eq. 4.2 written in $S_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = \mathbf p_1 + m\,\mathbf v_0^{O_1},\qquad T_0 = T_1 + m\,\mathbf v_1^P\cdot\mathbf v_0^{O_1} + \tfrac12\,m\,\mathbf v_0^{O_1}\cdot\mathbf v_0^{O_1}}$$
>
> **Units:** $\mathrm{kg\,m/s}$ in the first result; $\mathrm{kg\,(m/s)^2} = \mathrm J$ in every term of the second
> **Meaning:** both quantities change with the observer, by amounts that vanish only when $S_1$ is at rest with respect to $S_0$; a particle at rest in $S_1$ has zero momentum and kinetic energy there and not in $S_0$. A force, being an interaction between bodies, is the same for both observers.

## 2. Newton's laws

Newton's laws are the hallmark of classical mechanics: they are the axioms that condense the description of the dynamics of all particles and bodies (Notes.pdf, Sec. 4.2). They hold only in inertial reference frames, whose existence is accepted as an axiom; given one inertial frame, any other frame that moves at a constant velocity and does not rotate with respect to it is also inertial. Not all reference frames are inertial; in fact most are not ([Lecture 2, Slide 4]).

### First law

> [!key] Newton's first law (Notes.pdf, Sec. 4.2; [Lecture 2, Slide 4])
> "A body shall continue in a state of rest or of uniform motion in a straight line unless impressed upon by a force." An isolated body free of forces moves in a straight line at constant speed relative to an inertial frame. Turned around, the law defines the inertial frames: a reference frame is inertial if a particle free of forces stays at rest or in uniform rectilinear motion in it.

### Second law

> [!key] Newton's second law (Notes.pdf, Sec. 4.2; [Lecture 2, Slide 5])
> "The rate of change of momentum is proportional to the impressed force and takes place in the same direction as the force." The law defines the magnitude of a force through the rate of change of the linear momentum of the body on which it acts. It is only valid in an inertial reference frame.

> [!derivation] Second law for a particle of constant mass
> **Law:** Newton's second law; product rule for a scalar times a vector
> **Source:** Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 2.4; [Lecture 2, Slide 5]
>
> Here $\mathbf F$ is the resultant, the vector sum of all the forces acting on $P$, and $S_0$ is inertial.
>
> $$\begin{aligned}
> \mathbf F &= \left.\frac{d\mathbf p_0}{dt}\right|_0 \quad &\text{(second law, with the proportionality constant set to one by the choice of units)} \\
> &= \left.\frac{d}{dt}\left(m\,\mathbf v_0^P\right)\right|_0 \quad &\text{(Eq. 4.1)} \\
> &= \frac{dm}{dt}\,\mathbf v_0^P + m\left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(product rule, Eq. 1.64)} \\
> &= m\left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(the mass of a particle is constant in Newtonian mechanics)} \\
> &= m\,\mathbf a_0^P \quad &\text{(acceleration in $S_0$, Eq. 2.4)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = \left.\frac{d\mathbf p_0}{dt}\right|_0 = m\left.\frac{d\mathbf v_0^P}{dt}\right|_0 = m\,\mathbf a_0^P}$$
>
> **Units:** $[\mathrm M]\,[\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$, $\mathrm N = \mathrm{kg\,m/s^2}$ on both sides
> **Meaning:** the law fixes how the velocity changes in time and so embodies the equations of motion of the particle ([Lecture 2, Slide 5]): the acceleration is proportional to the vector sum of the forces, so a larger net force gives a larger acceleration, and inversely proportional to the mass (its inertia), so a more massive particle accelerates more slowly under the same force.

> [!derivation] The first law as a special case of the second
> **Law:** second law with zero resultant; integration in time with Barrow's rule
> **Source:** Notes.pdf, Sec. 4.2; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 2.3
>
> Let the resultant on $P$ be zero from the instant $t_1$ on; $t'$ is the integration variable.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf p_0}{dt'}\right|_0 &= \mathbf 0 \quad &\text{(Eq. 4.3 with zero resultant)} \\
> \int_{t_1}^{t}\left.\frac{d\mathbf p_0}{dt'}\right|_0 dt' &= \int_{t_1}^{t}\mathbf 0\,dt' \quad &\text{(integrate both sides from $t_1$ to $t$)} \\
> \mathbf p_0(t) - \mathbf p_0(t_1) &= \mathbf 0 \quad &\text{(Barrow: $\mathbf p_0$ is an antiderivative of its own derivative)} \\
> \mathbf v_0^P(t) &= \mathbf v_0^P(t_1) \quad &\text{(divide by the constant $m$, Eq. 4.1)} \\
> \int_{t_1}^{t}\left.\frac{d\mathbf r_0^P}{dt'}\right|_0 dt' &= \int_{t_1}^{t}\mathbf v_0^P(t_1)\,dt' \quad &\text{(Eq. 2.3, integrated from $t_1$ to $t$)} \\
> \mathbf r_0^P(t) - \mathbf r_0^P(t_1) &= \mathbf v_0^P(t_1)\,\big[t'\big]_{t_1}^{t} \quad &\text{(Barrow on the left; constant vector times the antiderivative $t'$ on the right)} \\
> &= \mathbf v_0^P(t_1)\,(t - t_1) \quad &\text{(Barrow: upper limit minus lower limit)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = \mathrm{const},\qquad \mathbf r_0^P(t) = \mathbf r_0^P(t_1) + \mathbf v_0^P(t_1)\,(t - t_1)}$$
>
> **Units:** $\mathrm{kg\,m/s}$ in the first result; $\mathrm m$ and $(\mathrm{m/s})\,\mathrm s$ in the second
> **Meaning:** with a null resultant the particle stays at rest (zero momentum) or moves along a straight line at constant velocity (constant momentum), which is the first law (Notes.pdf, Sec. 4.2).

The second law in the form of Eq. 4.3 complies with the principle of Galilean invariance, "the laws of motion are the same in all inertial reference frames", only because the mass is constant (Notes.pdf, p. 42, footnote 14). The next box shows why a varying mass breaks it.

> [!derivation] Galilean invariance requires a constant mass
> **Law:** composition of velocities between two inertial frames without relative rotation; product rule
> **Source:** Notes.pdf, p. 42; Notes.pdf, Eq. 1.64; Notes.pdf, Eq. 4.3
>
> Let $S_1$ be inertial and translate with the constant velocity $\mathbf v_0^{O_1}$ with respect to $S_0$, and suppose for the argument that the mass could change in time.
>
> $$\begin{aligned}
> \mathbf v_0^P &= \mathbf v_1^P + \mathbf v_0^{O_1} \quad &\text{(composition of velocities, Notes p. 42)} \\
> \left.\frac{d\mathbf v_0^P}{dt}\right|_0 &= \left.\frac{d\mathbf v_1^P}{dt}\right|_1 \quad &\text{($\mathbf v_0^{O_1}$ is constant and the frames do not rotate: equal accelerations, Notes p. 42)} \\
> \left.\frac{d\mathbf p_1}{dt}\right|_1 &= \frac{dm}{dt}\,\mathbf v_1^P + m\left.\frac{d\mathbf v_1^P}{dt}\right|_1 \quad &\text{(product rule in $S_1$, Eq. 1.64)} \\
> \left.\frac{d\mathbf p_0}{dt}\right|_0 &= \frac{dm}{dt}\,\mathbf v_0^P + m\left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(product rule in $S_0$)} \\
> \left.\frac{d\mathbf p_0}{dt}\right|_0 - \left.\frac{d\mathbf p_1}{dt}\right|_1 &= \frac{dm}{dt}\left(\mathbf v_0^P - \mathbf v_1^P\right) \quad &\text{(subtract; the acceleration terms cancel by the second row)} \\
> &= \frac{dm}{dt}\,\mathbf v_0^{O_1} \quad &\text{(first row)}
> \end{aligned}$$
>
> $$\boxed{\left.\frac{d\mathbf p_0}{dt}\right|_0 - \left.\frac{d\mathbf p_1}{dt}\right|_1 = \frac{dm}{dt}\,\mathbf v_0^{O_1} \neq \mathbf 0 \quad\text{if}\quad \frac{dm}{dt} \neq 0}$$
>
> **Units:** $(\mathrm{kg/s})\,(\mathrm{m/s}) = \mathrm{kg\,m/s^2} = \mathrm N$
> **Meaning:** with a varying mass the two inertial observers would assign different forces to the same interaction, which is the inconsistency of the footnote. Systems of varying mass, such as a rocket, are therefore studied by applying Newton's equation to a control volume whose total mass stays constant (Notes.pdf, p. 42).

### Third law

> [!key] Newton's third law (Notes.pdf, Sec. 4.2; [Lecture 2, Slide 6])
> "To every action (force) there is an equal and opposite reaction (force)." If a particle $Q$ exerts a force $\mathbf F$ on a particle $P$, then $P$ exerts the force $-\mathbf F$ on $Q$; the two forces, called action and reaction, share the same line of action. The law forbids unpaired forces in the universe, embodies the conservation of the total momentum of interacting bodies, and lies at the foundations of aerospace propulsion: a space vehicle must expel mass, and momentum with it, to accelerate and change its motion.

![[attachments/EM-T/t2-action-reaction.svg]]

### Internal and external forces and the conservation of linear momentum

Mechanics can consider the total linear momentum of a group of particles at once, the system of analysis; the rest of the universe is its environment ([Lecture 2, Slide 7]):

| Kind of force | Cause | Where its reaction acts |
| :--- | :--- | :--- |
| Internal | another particle of the system | on a particle of the system: action and reaction both lie within the system |
| External | something in the environment | somewhere else in the universe, on no particle of the system |

A system of analysis is isolated when no external force acts on its particles ([Lecture 2, Slide 7]).

![[attachments/EM-T/t2-momentum-conservation.svg]]

> [!derivation] Conservation of the total linear momentum of two particles
> **Law:** second law for each particle; third law; sum rule of differentiation; Barrow's rule
> **Source:** [Lecture 2, Slide 8]; Notes.pdf, Sec. 4.2; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 1.65
>
> The system of analysis is $\{P, Q\}$, isolated: the only forces are the force $\mathbf F$ of $Q$ on $P$ and, by the third law, $-\mathbf F$ of $P$ on $Q$.
>
> $$\begin{aligned}
> \left.\frac{d\mathbf p_0^P}{dt}\right|_0 &= \mathbf F \quad &\text{(second law for $P$, Eq. 4.3)} \\
> \left.\frac{d\mathbf p_0^Q}{dt}\right|_0 &= -\mathbf F \quad &\text{(second law for $Q$, with the third law)} \\
> \left.\frac{d}{dt}\left(\mathbf p_0^P + \mathbf p_0^Q\right)\right|_0 &= \left.\frac{d\mathbf p_0^P}{dt}\right|_0 + \left.\frac{d\mathbf p_0^Q}{dt}\right|_0 \quad &\text{(sum rule, Eq. 1.65)} \\
> &= \mathbf F - \mathbf F \quad &\text{(the two rows above)} \\
> &= \mathbf 0 \quad &\text{(action and reaction cancel)} \\
> \left(\mathbf p_0^P + \mathbf p_0^Q\right)(t) - \left(\mathbf p_0^P + \mathbf p_0^Q\right)(t_1) &= \mathbf 0 \quad &\text{(integrate from $t_1$ to $t$; Barrow)}
> \end{aligned}$$
>
> $$\boxed{\mathbf p_0 = \mathbf p_0^P + \mathbf p_0^Q = \mathrm{const}}$$
>
> **Units:** $\mathrm{kg\,m/s}$ in every term
> **Meaning:** the total linear momentum of an isolated system is constant ([Lecture 2, Slide 8]); the momenta of $P$ and $Q$ change, but every change of one is matched by an opposite change of the other.

## 3. Equations of motion

Consider a particle $P$ of mass $m$ moving freely in an inertial reference frame $S_0$ under a known resultant force $\mathbf F$ (Notes.pdf, Sec. 4.3). In general $\mathbf F$ may be a vector function of the position of the particle, of its velocity and of time. A particle moving freely in space has three degrees of freedom: three independent coordinates, such as the Cartesian $x$, $y$, $z$, are needed to fix its position. The first step of every problem is the free-body diagram of the particle: every force acting on it is drawn, and their vector sum is the resultant that enters the second law.

![[attachments/EM-T/t2-free-body.svg]]

> [!derivation] Vector equation of motion of a free particle
> **Law:** Newton's second law in the inertial frame $S_0$; resultant as the vector sum of the forces of the free-body diagram
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 2.4; [Lecture 2, Slide 9]
>
> $$\begin{aligned}
> \mathbf F &= \mathbf F_1 + \mathbf F_2 + \dots \quad &\text{(resultant of all the forces of the free-body diagram)} \\
> m\,\mathbf a_0^P &= \mathbf F\left(\mathbf r_0^P, \mathbf v_0^P, t\right) \quad &\text{(second law, Eq. 4.3; the force may depend on position, velocity and time)} \\
> m\left.\frac{d^2\mathbf r_0^P}{dt^2}\right|_0 &= \mathbf F \quad &\text{(acceleration as the second derivative of the position, Eq. 2.4)}
> \end{aligned}$$
>
> $$\boxed{m\left.\frac{d^2\mathbf r_0^P}{dt^2}\right|_0 = \mathbf F}$$
>
> **Units:** $\mathrm{kg\,m/s^2} = \mathrm N$ on both sides
> **Meaning:** a vector differential equation of second order for the position; it describes the evolution, or the dynamics, of the particle ([Lecture 2, Slide 9]).

> [!derivation] Scalar equations of motion in the basis of S0
> **Law:** projection of a vector equation on three linearly independent unit vectors (dot product); Cartesian acceleration
> **Source:** Notes.pdf, Eq. 4.5; Notes.pdf, Eq. 2.7; Notes.pdf, Eq. 1.28; [Lecture 2, Slide 9]
>
> $$\begin{aligned}
> \mathbf a_0^P &= \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k \quad &\text{(Cartesian acceleration, Eq. 2.7)} \\
> m\,\mathbf a_0^P\cdot\mathbf i &= \mathbf F\cdot\mathbf i \quad &\text{(dot-multiply Eq. 4.4 by $\mathbf i$)} \\
> m\,\ddot x &= F_x \quad &\text{(components as dot products with the basis, Eq. 1.28)} \\
> m\,\ddot y &= F_y \quad &\text{(the same with $\mathbf j$)} \\
> m\,\ddot z &= F_z \quad &\text{(the same with $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d^2x}{dt^2} = \frac{F_x}{m},\qquad \frac{d^2y}{dt^2} = \frac{F_y}{m},\qquad \frac{d^2z}{dt^2} = \frac{F_z}{m}}$$
>
> **Units:** $\mathrm{m/s^2}$ on both sides of each equation ($\mathrm N/\mathrm{kg}$ on the right)
> **Meaning:** three second-order ordinary differential equations for the three unknowns $x(t)$, $y(t)$ and $z(t)$. The basis of $S_0$ is the most obvious choice, not the only one: choosing the projection vectors wisely, or combining the scalar equations, can give simpler, more compact or more insightful expressions (Notes.pdf, Sec. 4.3; [Lecture 2, Slide 9]).

> [!derivation] The equations of motion as six first-order equations
> **Law:** the velocity components taken as additional unknowns; definition of the derivative
> **Source:** Notes.pdf, Eq. 4.6; Notes.pdf, Eq. 4.5; [Lecture 2, Slide 10]
>
> $$\begin{aligned}
> \frac{d\dot x}{dt} &= \ddot x \quad &\text{(the derivative of $\dot x$ is the second derivative of $x$)} \\
> &= \frac{F_x}{m} \quad &\text{(first of Eqs. 4.5)} \\
> \frac{dx}{dt} &= \dot x \quad &\text{(definition of $\dot x$, now an equation linking two unknowns)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\dot x}{dt} = \frac{F_x}{m};\quad \frac{d\dot y}{dt} = \frac{F_y}{m};\quad \frac{d\dot z}{dt} = \frac{F_z}{m};\qquad \frac{dx}{dt} = \dot x;\quad \frac{dy}{dt} = \dot y;\quad \frac{dz}{dt} = \dot z}$$
>
> **Units:** $\mathrm{m/s^2}$ in the first three equations, $\mathrm{m/s}$ in the last three
> **Meaning:** six first-order ordinary differential equations for the six unknowns $x$, $y$, $z$, $\dot x$, $\dot y$, $\dot z$; the rows for $y$ and $z$ are the same steps with the second and third of Eqs. 4.5.

Either form, once integrated, gives the position of the particle as a function of time and six arbitrary constants $C_1, \dots, C_6$, two for each second-order equation (Notes.pdf, Eqs. 4.7 to 4.9; [Lecture 2, Slide 10]):

| Coordinate | Solution |
| :--- | :--- |
| $x$ | $x = x(t; C_1, C_2, C_3, C_4, C_5, C_6)$ |
| $y$ | $y = y(t; C_1, C_2, C_3, C_4, C_5, C_6)$ |
| $z$ | $z = z(t; C_1, C_2, C_3, C_4, C_5, C_6)$ |

The six constants are fixed by the initial conditions, the initial position $\mathbf r_{0,0}^P$ and the initial velocity $\mathbf v_{0,0}^P$ of the particle; the kinematics of the problem turns them into the initial values of the coordinates and their derivatives, here the initial values $x_0$, $y_0$, $z_0$ of the three coordinates and the initial values of their three time derivatives (Notes.pdf, Sec. 4.3). Finding these functions is what is meant by "solving the dynamics of $P$" ([Lecture 2, Slide 10]). The equations of motion can also be read the other way round, to find the force that a particle needs to follow a given motion ([Lecture 2, Slide 12]); the two examples below do one of each.

> [!example] Motion under gravity ([Lecture 2, Slide 11])
> Integrate the motion of a point particle $P$ under the effect of its weight, which points along $-\mathbf j$. The motion takes place in the plane $Oxy$ of the slide.
>
> | Data | Value |
> | :--- | :--- |
> | mass | $m = 1\ \mathrm{kg}$ |
> | gravity | $g = 10\ \mathrm{m/s^2}$; weight $\mathbf F = -m\,g\,\mathbf j$ |
> | initial position | $x(0) = 0$, $y(0) = 0$ |
> | initial velocity | $\dot x(0) = 2\ \mathrm{m/s}$, $\dot y(0) = 5\ \mathrm{m/s}$ |

![[attachments/EM-T/t2-projectile.svg]]

> [!derivation] Motion under gravity: equations of motion
> **Law:** scalar equations of motion in the basis of $S_0$
> **Source:** [Lecture 2, Slide 11]; Notes.pdf, Eq. 4.5
>
> $$\begin{aligned}
> F_x &= -m\,g\,\mathbf j\cdot\mathbf i \quad &\text{(component of the weight along $\mathbf i$, Eq. 1.28)} \\
> &= 0 \quad &\text{($\mathbf j\cdot\mathbf i = 0$)} \\
> F_y &= -m\,g\,\mathbf j\cdot\mathbf j \quad &\text{(component along $\mathbf j$)} \\
> &= -m\,g \quad &\text{($\mathbf j\cdot\mathbf j = 1$)} \\
> \ddot x &= 0 \quad &\text{(first of Eqs. 4.5)} \\
> \ddot y &= -g \quad &\text{(second of Eqs. 4.5; the mass cancels)}
> \end{aligned}$$
>
> $$\boxed{\ddot x = 0,\qquad \ddot y = -g}$$
>
> **Units:** $\mathrm{m/s^2}$
> **Meaning:** the weight has no horizontal component, so the horizontal motion is free; the vertical acceleration is the same for every mass.

> [!derivation] Motion under gravity: horizontal coordinate
> **Law:** integration in time from $0$ to $t$ with Barrow's rule, twice
> **Source:** [Lecture 2, Slide 11]; Notes.pdf, Eq. 4.6
>
> $$\begin{aligned}
> \int_0^t \frac{d\dot x}{dt'}\,dt' &= \int_0^t 0\,dt' \quad &\text{(integrate the first-order form of $\ddot x = 0$, Eq. 4.6)} \\
> \dot x(t) - \dot x(0) &= 0 \quad &\text{(Barrow on the left; the integral of zero is zero)} \\
> \dot x(t) &= 2 \quad &\text{(initial condition $\dot x(0) = 2\ \mathrm{m/s}$)} \\
> \int_0^t \frac{dx}{dt'}\,dt' &= \int_0^t 2\,dt' \quad &\text{(integrate $dx/dt = \dot x$)} \\
> x(t) - x(0) &= \big[2t'\big]_0^t \quad &\text{(Barrow on the left; antiderivative $2t'$ on the right)} \\
> &= 2t - 0 \quad &\text{(Barrow: upper limit minus lower limit)} \\
> x(t) &= 2t \quad &\text{(initial condition $x(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot x(t) = 2,\qquad x(t) = 2t \quad (\mathrm{SI})}$$
>
> **Units:** $\dot x$ in $\mathrm{m/s}$; $x$ in $\mathrm m$, the factor $2$ in $\mathrm{m/s}$ times $t$ in $\mathrm s$
> **Meaning:** uniform horizontal motion at the initial horizontal velocity.

> [!derivation] Motion under gravity: vertical coordinate
> **Law:** integration in time from $0$ to $t$ with Barrow's rule, twice
> **Source:** [Lecture 2, Slide 11]; Notes.pdf, Eq. 4.6
>
> $$\begin{aligned}
> \int_0^t \frac{d\dot y}{dt'}\,dt' &= \int_0^t (-g)\,dt' \quad &\text{(integrate the first-order form of $\ddot y = -g$)} \\
> \dot y(t) - \dot y(0) &= \big[-g\,t'\big]_0^t \quad &\text{(Barrow on the left; antiderivative $-g\,t'$ on the right)} \\
> &= -g\,t \quad &\text{(Barrow: upper limit minus lower limit)} \\
> \dot y(t) &= 5 - 10\,t \quad &\text{(initial condition $\dot y(0) = 5\ \mathrm{m/s}$ and $g = 10\ \mathrm{m/s^2}$)} \\
> \int_0^t \frac{dy}{dt'}\,dt' &= \int_0^t \left(5 - 10\,t'\right)dt' \quad &\text{(integrate $dy/dt = \dot y$)} \\
> y(t) - y(0) &= \Big[5\,t' - 5\,t'^2\Big]_0^t \quad &\text{(Barrow on the left; antiderivative of each term on the right)} \\
> &= 5\,t - 5\,t^2 \quad &\text{(Barrow: the lower limit gives zero)} \\
> y(t) &= 5\,t - 5\,t^2 \quad &\text{(initial condition $y(0) = 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot y(t) = 5 - 10\,t,\qquad y(t) = 5\,t - 5\,t^2 \quad (\mathrm{SI})}$$
>
> **Units:** $\dot y$ in $\mathrm{m/s}$ ($5$ in $\mathrm{m/s}$, $10$ in $\mathrm{m/s^2}$ times $\mathrm s$); $y$ in $\mathrm m$ ($5$ in $\mathrm{m/s}$ times $\mathrm s$, $5$ in $\mathrm{m/s^2}$ times $\mathrm{s^2}$)
> **Meaning:** uniformly decelerated vertical motion; the four constants of this planar problem are the four initial values.

> [!derivation] Motion under gravity: trajectory, apex and landing
> **Law:** elimination of time between the two coordinates; vertical velocity zero at the apex
> **Source:** [Lecture 2, Slide 11]
>
> $$\begin{aligned}
> t &= \frac{x}{2} \quad &\text{(invert $x(t) = 2t$)} \\
> y &= 5\,\frac{x}{2} - 5\left(\frac{x}{2}\right)^2 \quad &\text{(substitute in $y(t)$)} \\
> &= \frac52\,x - \frac54\,x^2 \quad &\text{(expand the square)} \\
> 0 &= 5 - 10\,t_{\mathrm{apex}} \quad &\text{(apex: $\dot y = 0$)} \\
> t_{\mathrm{apex}} &= 0.5 \quad &\text{(solve for the time)} \\
> y(0.5) &= 5\cdot 0.5 - 5\cdot 0.25 \quad &\text{(substitute in $y(t)$)} \\
> &= 1.25 \quad &\text{(arithmetic)} \\
> 0 &= 5\,t_{\mathrm L} - 5\,t_{\mathrm L}^2 \quad &\text{(landing: back to $y = 0$)} \\
> t_{\mathrm L} &= 1 \quad &\text{(the root other than $t = 0$)} \\
> x(1) &= 2 \quad &\text{(substitute in $x(t)$)}
> \end{aligned}$$
>
> $$\boxed{y = \tfrac52\,x - \tfrac54\,x^2;\qquad t_{\mathrm{apex}} = 0.5\ \mathrm s,\ y_{\max} = 1.25\ \mathrm m;\qquad t_{\mathrm L} = 1\ \mathrm s,\ x(t_{\mathrm L}) = 2\ \mathrm m}$$
>
> **Units:** $\tfrac52$ is dimensionless and $\tfrac54$ is in $\mathrm{m^{-1}}$, so every term of the trajectory is in $\mathrm m$; times in $\mathrm s$, heights and distances in $\mathrm m$
> **Meaning:** the trajectory is a parabola with its vertex at the apex, reached at half the flight time because the vertical motion is symmetric about it.

> [!example] Force needed for a given motion ([Lecture 2, Slide 12])
> Find the force that a particle $P$ needs in order to have the velocity below with respect to $S_0$. The constants $c_1$ and $c_2$ are those the slide writes $a$ and $b$.
>
> | Data | Value |
> | :--- | :--- |
> | mass | $m = 2\ \mathrm{kg}$ |
> | velocity | $\mathbf v_0^P(t) = 2\,c_1 t^2\,\mathbf i_0 + \exp(c_2 t)\,\mathbf j_0$ |

> [!derivation] Force needed for a given motion
> **Law:** Newton's second law read as the force required by a known motion; chain rule for the exponential
> **Source:** [Lecture 2, Slide 12]; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 2.4
>
> $$\begin{aligned}
> \mathbf a_0^P &= \left.\frac{d\mathbf v_0^P}{dt}\right|_0 \quad &\text{(Eq. 2.4)} \\
> &= \frac{d}{dt}\left(2\,c_1 t^2\right)\mathbf i_0 + \frac{d}{dt}\left(\exp(c_2 t)\right)\mathbf j_0 \quad &\text{(the basis of $S_0$ is constant in $S_0$)} \\
> &= 4\,c_1 t\,\mathbf i_0 + \frac{d}{dt}\left(\exp(c_2 t)\right)\mathbf j_0 \quad &\text{(power rule: the derivative of $t^2$ is $2t$)} \\
> &= 4\,c_1 t\,\mathbf i_0 + \exp(c_2 t)\,\frac{d(c_2 t)}{dt}\,\mathbf j_0 \quad &\text{(chain rule: the exponential is its own derivative)} \\
> &= 4\,c_1 t\,\mathbf i_0 + c_2\exp(c_2 t)\,\mathbf j_0 \quad &\text{(the derivative of $c_2 t$ is $c_2$)} \\
> \mathbf F &= m\,\mathbf a_0^P \quad &\text{(Eq. 4.3)} \\
> &= 2\left(4\,c_1 t\,\mathbf i_0 + c_2\exp(c_2 t)\,\mathbf j_0\right) \quad &\text{($m = 2\ \mathrm{kg}$)} \\
> &= 8\,c_1 t\,\mathbf i_0 + 2\,c_2\exp(c_2 t)\,\mathbf j_0 \quad &\text{(distribute)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F(t) = 8\,c_1 t\,\mathbf i_0 + 2\,c_2\exp(c_2 t)\,\mathbf j_0 \quad (\mathrm N)}$$
>
> **Units:** $c_1$ in $\mathrm{m/s^3}$, so $2\,c_1 t^2$ is in $\mathrm{m/s}$ and $8\,c_1 t$ (with the $2\ \mathrm{kg}$) in $\mathrm{kg\,m/s^2}$; $c_2$ in $\mathrm{s^{-1}}$. The exponential is dimensionless, so the $\mathbf j_0$ component of the velocity carries an implied factor of $1\ \mathrm{m/s}$, and the second term of the force is then in $\mathrm{kg\,(m/s)\,s^{-1}} = \mathrm N$
> **Meaning:** the force is fixed at every instant by the prescribed motion; here its $\mathbf i_0$ component grows linearly in time and its $\mathbf j_0$ component grows (or decays, for a negative $c_2$) exponentially, like the velocity component it drives.

## 4. Power, work and potential energy

### Power and the rate of change of kinetic energy

> [!derivation] Power of a force and its tangential component
> **Law:** definition of power; dot product; velocity and acceleration in the intrinsic basis
> **Source:** Notes.pdf, Eq. 4.10; Notes.pdf, Eq. 1.24; Notes.pdf, Eq. 2.16; Notes.pdf, Eq. 2.17; [Lecture 2, Slide 13]
>
> $\alpha_F$ is the angle between the force and the velocity; $\mathbf e_t$ and $\mathbf e_n$ are the tangent and normal unit vectors of the trajectory and $s$ its arc length (Topic 1).
>
> $$\begin{aligned}
> \dot W_0 &= \mathbf F\cdot\mathbf v_0^P \quad &\text{(definition of power, Eq. 4.10)} \\
> &= \lVert\mathbf F\rVert\,v_0^P\cos\alpha_F \quad &\text{(dot product, Eq. 1.24)} \\
> \dot W_0 &= \mathbf F\cdot\left(\dot s\,\mathbf e_t\right) \quad &\text{(intrinsic velocity, Eq. 2.16)} \\
> &= \dot s\left(\mathbf F\cdot\mathbf e_t\right) \quad &\text{(the scalar $\dot s$ comes out of the dot product, Eq. 1.26)} \\
> \mathbf F\cdot\mathbf e_t &= m\,\mathbf a_0^P\cdot\mathbf e_t \quad &\text{(for the resultant: second law, Eq. 4.3)} \\
> &= m\left(\ddot s\,\mathbf e_t + \frac{\dot s^2}{\rho}\,\mathbf e_n\right)\cdot\mathbf e_t \quad &\text{(intrinsic acceleration, Eq. 2.17; $\rho$ is the radius of curvature)} \\
> &= m\,\ddot s \quad &\text{($\mathbf e_t\cdot\mathbf e_t = 1$, $\mathbf e_n\cdot\mathbf e_t = 0$)}
> \end{aligned}$$
>
> $$\boxed{\dot W_0 = \mathbf F\cdot\mathbf v_0^P = \dot s\,\left(\mathbf F\cdot\mathbf e_t\right);\qquad \text{resultant: } \mathbf F\cdot\mathbf e_t = m\,\ddot s}$$
>
> **Units:** $\mathrm N\cdot\mathrm{m/s} = \mathrm{kg\,m^2/s^3} = \mathrm W$
> **Meaning:** the power is positive when the angle between force and velocity is acute, negative when it is obtuse, and zero when they are perpendicular or one of them is zero (Notes.pdf, Sec. 4.4). Only the tangential component of a force works; for the resultant that component is $m$ times the tangential acceleration (last row), so on a moving particle a force exerts nonzero power if and only if it induces tangential acceleration ([Lecture 2, Slide 13]).

> [!warning] Typo in Notes.pdf, p. 43: units of power and work
> The notes print the SI units of power as "kg·m²/t³" and of work as "kg·m²/t²", with the letter of time in place of the second. The units are $\mathrm{kg\,m^2/s^3}$ (watt) and $\mathrm{kg\,m^2/s^2}$ (joule), as the dimensions $[\mathrm{M\,L^2\,T^{-3}}]$ and $[\mathrm{M\,L^2\,T^{-2}}]$ show. The typo changes no result.

> [!derivation] Rate of change of the kinetic energy
> **Law:** product rule for the dot product; commutativity of the dot product; Newton's second law
> **Source:** Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 1.66; Notes.pdf, Eq. 1.25; Notes.pdf, Eq. 4.3; [Lecture 2, Slide 13]
>
> $\mathbf F$ is now the resultant of all the forces on $P$.
>
> $$\begin{aligned}
> \frac{dT_0}{dt} &= \frac{d}{dt}\left(\tfrac12\,m\,\mathbf v_0^P\cdot\mathbf v_0^P\right) \quad &\text{(kinetic energy, Eq. 4.2)} \\
> &= \tfrac12\,m\left(\left.\frac{d\mathbf v_0^P}{dt}\right|_0\cdot\mathbf v_0^P + \mathbf v_0^P\cdot\left.\frac{d\mathbf v_0^P}{dt}\right|_0\right) \quad &\text{(product rule for the dot product, Eq. 1.66; $m$ is constant)} \\
> &= \tfrac12\,m\left(\mathbf a_0^P\cdot\mathbf v_0^P + \mathbf v_0^P\cdot\mathbf a_0^P\right) \quad &\text{(Eq. 2.4)} \\
> &= \tfrac12\,m\left(\mathbf a_0^P\cdot\mathbf v_0^P + \mathbf a_0^P\cdot\mathbf v_0^P\right) \quad &\text{(commutativity, Eq. 1.25)} \\
> &= m\,\mathbf a_0^P\cdot\mathbf v_0^P \quad &\text{(add the two equal terms)} \\
> &= \mathbf F\cdot\mathbf v_0^P \quad &\text{(second law, Eq. 4.3)} \\
> &= \dot W_0 \quad &\text{(Eq. 4.10)}
> \end{aligned}$$
>
> $$\boxed{\frac{dT_0}{dt} = m\,\mathbf a_0^P\cdot\mathbf v_0^P = \mathbf F\cdot\mathbf v_0^P = \dot W_0}$$
>
> **Units:** $\mathrm{kg\,m^2/s^3} = \mathrm W$ in every member: $\mathrm J/\mathrm s$ on the left, $\mathrm{kg}\,(\mathrm{m/s^2})(\mathrm{m/s})$ and $\mathrm N\,(\mathrm{m/s})$ on the right
> **Meaning:** the time derivative of the kinetic energy equals the power of the resultant force (Notes.pdf, Sec. 4.4): forces perpendicular to the velocity change the direction of motion but not the speed.

### Work along a path

![[attachments/EM-T/t2-work-path.svg]]

> [!derivation] Work of a force and the work-energy theorem
> **Law:** work as the time integral of the power; change of the integration variable from time to position; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.12; Notes.pdf, Eq. 4.13; Notes.pdf, Eq. 4.11; [Lecture 2, Slide 13]; [Lecture 2, Slide 14]
>
> Between $t_1$ and $t_2$ the particle goes from $\mathbf r_{0,1}^P$ to $\mathbf r_{0,2}^P$ along its trajectory $\Gamma$.
>
> $$\begin{aligned}
> W_0(t_1,t_2) &= \int_{t_1}^{t_2}\dot W_0\,dt \quad &\text{(definition of work, Eq. 4.12)} \\
> &= \int_{t_1}^{t_2}\mathbf F\cdot\mathbf v_0^P\,dt \quad &\text{(Eq. 4.10)} \\
> &= \int_{t_1}^{t_2}\mathbf F\cdot\left.\frac{d\mathbf r_0^P}{dt}\right|_0 dt \quad &\text{(Eq. 2.3)} \\
> &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(substitution: differential $d\mathbf r_0^P = \mathbf v_0^P\,dt$; limits $t_1 \to \mathbf r_{0,1}^P$, $t_2 \to \mathbf r_{0,2}^P$, along $\Gamma$)} \\
> \delta W_0 &= \mathbf F\cdot d\mathbf r_0^P \quad &\text{(integrand: the work done in a differential time interval, Eq. 4.13)} \\
> W_0(t_1,t_2) &= \int_{t_1}^{t_2}\frac{dT_0}{dt}\,dt \quad &\text{(for the resultant force, Eq. 4.11 in the first row)} \\
> &= T_0(t_2) - T_0(t_1) \quad &\text{(Barrow: $T_0$ is an antiderivative of its own derivative)}
> \end{aligned}$$
>
> $$\boxed{W_0(t_1,t_2) = \int_{t_1}^{t_2}\mathbf F\cdot\mathbf v_0^P\,dt = \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\mathbf F\cdot d\mathbf r_0^P;\qquad \text{resultant: } W_0(t_1,t_2) = T_{0,2} - T_{0,1}}$$
>
> **Units:** $\mathrm N\cdot\mathrm m = \mathrm{kg\,m^2/s^2} = \mathrm J$; $\mathrm W\cdot\mathrm s = \mathrm J$ in the time integral
> **Meaning:** the work is a line integral along the path followed. The symbol $\delta$ instead of $d$ says that $\delta W_0$ is in general not an exact differential: the integral depends on the whole path $\Gamma$ between the two end points, not only on them (Notes.pdf, Sec. 4.4; [Lecture 2, Slide 14]). The work of the resultant equals the change of kinetic energy.

### Potential energy

When $\delta W_0$ is an exact differential, the work integral does not depend on the path, only on its end points (Notes.pdf, Sec. 4.4; [Lecture 2, Slide 14]). Fixing the first end point at an arbitrary reference position $\mathbf r_{0,*}^P$ then defines a function of the second end point alone, and the force is called conservative.

> [!derivation] Potential energy of a conservative force
> **Law:** path independence of the work; additivity of the line integral over a path split at an intermediate point; reversal of the limits
> **Source:** Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.12; [Lecture 2, Slide 14]
>
> $$\begin{aligned}
> V_0(\mathbf r_0^P) &= -\int_{\mathbf r_{0,*}^P}^{\mathbf r_0^P}\mathbf F(\mathbf r_0^P)\cdot d\mathbf r_0^P \quad &\text{(definition, Eq. 4.14; the minus sign is customary)} \\
> W_0 &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(work between two positions, Eq. 4.12)} \\
> &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,*}^P}\mathbf F\cdot d\mathbf r_0^P + \int_{\mathbf r_{0,*}^P}^{\mathbf r_{0,2}^P}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(path independence: go through $\mathbf r_{0,*}^P$; split the integral)} \\
> &= -\int_{\mathbf r_{0,*}^P}^{\mathbf r_{0,1}^P}\mathbf F\cdot d\mathbf r_0^P + \int_{\mathbf r_{0,*}^P}^{\mathbf r_{0,2}^P}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(reversing the limits changes the sign)} \\
> &= V_0(\mathbf r_{0,1}^P) - V_0(\mathbf r_{0,2}^P) \quad &\text{(first row, at $\mathbf r_{0,1}^P$ and at $\mathbf r_{0,2}^P$)}
> \end{aligned}$$
>
> $$\boxed{V_0(\mathbf r_0^P) = -\int_{\mathbf r_{0,*}^P}^{\mathbf r_0^P}\mathbf F\cdot d\mathbf r_0^P,\qquad W_0(\mathbf r_{0,1}^P,\mathbf r_{0,2}^P) = V_0(\mathbf r_{0,1}^P) - V_0(\mathbf r_{0,2}^P)}$$
>
> **Units:** $\mathrm J$ in every term
> **Meaning:** the potential energy is a scalar field defined at every point of space ([Lecture 2, Slide 14]); the work of a conservative force is the decrease of its potential energy. Moving the reference position adds the same constant (the work between the old and the new reference) to every value of $V_0$, so the choice of $\mathbf r_{0,*}^P$ is irrelevant: it is the integration constant (Notes.pdf, Sec. 4.4). The notes write $\mathbf r_{0,1}^P$ for the reference position.

In one-dimensional problems without boundary conditions, a force that depends only on the position is necessary and sufficient for the potential energy to exist (Notes.pdf, Sec. 4.4).

> [!derivation] Potential energy in one dimension and the force from it
> **Law:** one-dimensional line integral; fundamental theorem of calculus (derivative of an integral with respect to its upper limit)
> **Source:** Notes.pdf, Eq. 4.15; Notes.pdf, Eq. 4.16; Notes.pdf, Eq. 4.14
>
> The particle moves along $Ox$ under a force along $\mathbf i$ that depends only on $x$; $x'$ is the integration variable and $x_1$ the reference position.
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i,\qquad \mathbf F = F_x(x)\,\mathbf i \quad &\text{(one-dimensional problem)} \\
> d\mathbf r_0^P &= dx\,\mathbf i \quad &\text{(differential of the position; $\mathbf i$ is constant)} \\
> \mathbf F\cdot d\mathbf r_0^P &= F_x(x)\,dx \quad &\text{($\mathbf i\cdot\mathbf i = 1$)} \\
> V_0(x) &= -\int_{x_1}^{x}F_x(x')\,dx' \quad &\text{(Eq. 4.14, Eq. 4.15)} \\
> \frac{dV_0}{dx} &= -F_x(x) \quad &\text{(fundamental theorem of calculus: the derivative with respect to the upper limit is the integrand there)}
> \end{aligned}$$
>
> $$\boxed{V_0(x) = -\int_{x_1}^{x}F_x(x')\,dx',\qquad F_x(x) = -\frac{dV_0}{dx}}$$
>
> **Units:** $\mathrm N\cdot\mathrm m = \mathrm J$ for $V_0$; $\mathrm J/\mathrm m = \mathrm N$ for the force
> **Meaning:** on a line the integral of a function of $x$ alone depends only on its limits, so any force of the position alone has a potential. Plotting $V_0(x)$ shows the problem as a terrain of hills and valleys: the force points downslope, with a magnitude proportional to the steepness (Notes.pdf, Sec. 4.4; [Lecture 2, Slide 15]).

![[attachments/EM-T/t2-potential-force.svg]]

> [!derivation] Force of the example potential of Fig. 4.1
> **Law:** force as minus the derivative of the potential; chain rule
> **Source:** Notes.pdf, Eq. 4.16; Notes.pdf Fig. 4.1; [Lecture 2, Slide 15]
>
> The potential of the example is the sum of $\cos x$ and $\cos(x/2 - \pi/4)$, written in dimensionless units; $w$ stands for the inner argument of the second cosine.
>
> $$\begin{aligned}
> V_0(x) &= \cos x + \cos w,\qquad w = \frac{x}{2} - \frac{\pi}{4} \quad &\text{(Fig. 4.1, Slide 15)} \\
> \frac{d}{dx}\cos x &= -\sin x \quad &\text{(derivative of the cosine)} \\
> \frac{dw}{dx} &= \frac12 \quad &\text{(derivative of the inner argument)} \\
> \frac{d}{dx}\cos w &= -\sin w\,\frac{dw}{dx} \quad &\text{(chain rule)} \\
> &= -\frac12\sin\left(\frac{x}{2} - \frac{\pi}{4}\right) \quad &\text{(substitute $dw/dx$ and $w$)} \\
> F_x &= -\frac{dV_0}{dx} \quad &\text{(Eq. 4.16)} \\
> &= \sin x + \frac12\sin\left(\frac{x}{2} - \frac{\pi}{4}\right) \quad &\text{(minus the sum of the two derivatives)}
> \end{aligned}$$
>
> $$\boxed{F_x = \sin x + \frac12\sin\left(\frac{x}{2} - \frac{\pi}{4}\right)}$$
>
> **Units:** dimensionless illustrative example (Fig. 4.1 plots it without units)
> **Meaning:** where the curve rises the derivative is positive and the force negative, so the force points down the slope towards the valleys, longer where the curve is steeper; at the peaks and troughs it vanishes ([Lecture 2, Slide 15]).

### Conservative forces in two and three dimensions

In two- and three-dimensional problems in simply connected domains without boundary conditions, a force that depends only on the position is necessary but not sufficient for a potential to exist: the work around every closed path must also vanish (Notes.pdf, Sec. 4.4; [Lecture 2, Slide 16]).

> [!derivation] Path independence and the closed-path condition
> **Law:** a closed path as one path followed by another reversed; additivity of the line integral; reversal of the limits
> **Source:** Notes.pdf, Eq. 4.17; [Lecture 2, Slide 14]; [Lecture 2, Slide 16]
>
> $\Gamma_1$ and $\Gamma_2$ are two paths from $\mathbf r_{0,1}^P$ to $\mathbf r_{0,2}^P$; $\Gamma$ is the closed path made of $\Gamma_1$ followed by $\Gamma_2$ run backwards.
>
> $$\begin{aligned}
> \oint_\Gamma\mathbf F\cdot d\mathbf r_0^P &= \int_{\Gamma_1}\mathbf F\cdot d\mathbf r_0^P + \int_{\Gamma_2\ \text{reversed}}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(split the closed path at its two end points)} \\
> &= \int_{\Gamma_1}\mathbf F\cdot d\mathbf r_0^P - \int_{\Gamma_2}\mathbf F\cdot d\mathbf r_0^P \quad &\text{(running a path backwards changes the sign of $d\mathbf r_0^P$)}
> \end{aligned}$$
>
> $$\boxed{\oint_\Gamma\mathbf F(\mathbf r_0^P)\cdot d\mathbf r_0^P = 0\ \ \forall\,\Gamma \quad\Longleftrightarrow\quad \int_{\Gamma_1}\mathbf F\cdot d\mathbf r_0^P = \int_{\Gamma_2}\mathbf F\cdot d\mathbf r_0^P\ \ \forall\,\Gamma_1, \Gamma_2}$$
>
> **Units:** $\mathrm J$
> **Meaning:** every closed path is a pair of paths between two of its points, and every pair of paths makes a closed path, so the work vanishes around every closed path exactly when it is independent of the path: this is the condition for the force to be conservative and for the potential energy to exist ([Lecture 2, Slide 16]).

> [!derivation] The force as minus the gradient of the potential
> **Law:** differential of the potential at the upper limit of its integral; total differential of a function of three variables; independence of the three differentials
> **Source:** Notes.pdf, Eq. 4.19; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 1.74; [Lecture 2, Slide 14]
>
> $$\begin{aligned}
> dV_0 &= -\mathbf F\cdot d\mathbf r_0^P \quad &\text{(moving the upper limit of Eq. 4.14 by $d\mathbf r_0^P$ adds the integrand times $d\mathbf r_0^P$)} \\
> &= -\left(F_x\,dx + F_y\,dy + F_z\,dz\right) \quad &\text{(dot product in components, with $d\mathbf r_0^P = dx\,\mathbf i + dy\,\mathbf j + dz\,\mathbf k$)} \\
> dV_0 &= \frac{\partial V_0}{\partial x}\,dx + \frac{\partial V_0}{\partial y}\,dy + \frac{\partial V_0}{\partial z}\,dz \quad &\text{(total differential of $V_0(x,y,z)$)} \\
> F_x &= -\frac{\partial V_0}{\partial x},\quad F_y = -\frac{\partial V_0}{\partial y},\quad F_z = -\frac{\partial V_0}{\partial z} \quad &\text{(the two rows hold for any $dx$, $dy$, $dz$: equate their coefficients)} \\
> \mathbf F &= -\frac{\partial V_0}{\partial x}\,\mathbf i - \frac{\partial V_0}{\partial y}\,\mathbf j - \frac{\partial V_0}{\partial z}\,\mathbf k \quad &\text{(assemble the vector)} \\
> &= -\nabla V_0 \quad &\text{(gradient, Eq. 1.74)}
> \end{aligned}$$
>
> $$\boxed{F_x = -\frac{\partial V_0}{\partial x};\quad F_y = -\frac{\partial V_0}{\partial y};\quad F_z = -\frac{\partial V_0}{\partial z};\qquad \mathbf F = -\nabla V_0}$$
>
> **Units:** $\mathrm J/\mathrm m = \mathrm N$ for each component
> **Meaning:** the conservative force points in the direction in which the potential energy decreases fastest, with a magnitude equal to that rate of decrease; this is the inversion of Eq. 4.15 in three dimensions (Notes.pdf, Sec. 4.4).

> [!derivation] A conservative force is irrotational
> **Law:** curl in components; equality of the mixed second partial derivatives of a smooth function
> **Source:** Notes.pdf, Eq. 4.18; Notes.pdf, Eq. 1.76; Notes.pdf, Eq. 1.77; Notes.pdf, Eq. 4.19
>
> $$\begin{aligned}
> \left(\nabla\times\mathbf F\right)\cdot\mathbf k &= \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \quad &\text{(third component of the curl, Eq. 1.76)} \\
> &= \frac{\partial}{\partial x}\left(-\frac{\partial V_0}{\partial y}\right) - \frac{\partial}{\partial y}\left(-\frac{\partial V_0}{\partial x}\right) \quad &\text{(Eq. 4.19)} \\
> &= -\frac{\partial^2 V_0}{\partial x\,\partial y} + \frac{\partial^2 V_0}{\partial y\,\partial x} \quad &\text{(take the signs out)} \\
> &= 0 \quad &\text{(the order of differentiation does not matter for a smooth $V_0$)}
> \end{aligned}$$
>
> $$\boxed{\nabla\times\mathbf F = \mathbf 0}$$
>
> **Units:** $\mathrm N/\mathrm m$ for each component of the curl
> **Meaning:** the first and second components vanish by the same steps with the pairs $(y,z)$ and $(z,x)$; this is Eq. 1.77, the curl of a gradient is zero. Conversely, the notes and the slide state that if the curl of a force that depends only on the position vanishes in a simply connected domain, the force is conservative and a potential energy exists in that domain (Notes.pdf, Sec. 4.4; [Lecture 2, Slide 16]).

### Examples of conservative and non-conservative forces

The potential energies of [Lecture 2, Slide 16] are derived below from their definition, as line integrals along an arbitrary path $\Gamma$ parametrised by $\sigma$, from $\sigma_*$ at the reference position to $\sigma_P$ at the current position of $P$.

> [!derivation] Potential energy of the weight
> **Law:** definition of the potential energy as a line integral; constant vector out of the integral; Barrow's rule
> **Source:** [Lecture 2, Slide 16]; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 4.20
>
> The weight $m\,\mathbf g$ is the same at every point. The path $\Gamma$ is $\mathbf r_0^P(\sigma)$ with $\sigma$ from $\sigma_*$ to $\sigma_P$; its differential is $d\mathbf r_0^P = (d\mathbf r_0^P/d\sigma)\,d\sigma$.
>
> $$\begin{aligned}
> V_0 &= -\int_{\sigma_*}^{\sigma_P} m\,\mathbf g\cdot\frac{d\mathbf r_0^P}{d\sigma}\,d\sigma \quad &\text{(Eq. 4.14 written with the parameter of the path)} \\
> &= -m\,\mathbf g\cdot\int_{\sigma_*}^{\sigma_P}\frac{d\mathbf r_0^P}{d\sigma}\,d\sigma \quad &\text{(the constant vector comes out of the integral)} \\
> &= -m\,\mathbf g\cdot\big[\mathbf r_0^P(\sigma)\big]_{\sigma_*}^{\sigma_P} \quad &\text{(antiderivative of $d\mathbf r_0^P/d\sigma$ is $\mathbf r_0^P$)} \\
> &= -m\,\mathbf g\cdot\left(\mathbf r_0^P - \mathbf r_{0,*}^P\right) \quad &\text{(Barrow: value at $\sigma_P$ minus value at $\sigma_*$)} \\
> &= -m\,\mathbf g\cdot\mathbf r_0^P \quad &\text{(reference position at the origin $O$)} \\
> &= -m\,(-g\,\mathbf j)\cdot\left(x\,\mathbf i + y\,\mathbf j + z\,\mathbf k\right) \quad &\text{(gravity along $-\mathbf j$, $Oy$ vertical and upwards; Eq. 2.5)} \\
> &= m\,g\,y \quad &\text{($\mathbf j\cdot\mathbf i = \mathbf j\cdot\mathbf k = 0$, $\mathbf j\cdot\mathbf j = 1$)} \\
> -\nabla V_0 &= -m\,g\,\mathbf j \quad &\text{(check with Eq. 4.20: only $\partial V_0/\partial y$ is nonzero)}
> \end{aligned}$$
>
> $$\boxed{V_0 = -m\,\mathbf g\cdot\mathbf r_0^P = m\,g\,y \quad (\mathbf g = -g\,\mathbf j)}$$
>
> **Units:** $\mathrm{kg}\,(\mathrm{m/s^2})\,\mathrm m = \mathrm J$
> **Meaning:** only the end points of $\Gamma$ appear in the result, so the weight is conservative; its potential energy grows linearly with the height, and the gradient check gives back the weight.

> [!derivation] Potential energy of a spring of zero natural length
> **Law:** definition of the potential energy as a line integral; product rule for the dot product; Barrow's rule
> **Source:** [Lecture 2, Slide 16]; Notes.pdf, Eq. 4.14; Notes.pdf, Eq. 1.66
>
> The spring joins $P$ to the origin and pulls with the force $-k\,\mathbf r_0^P$. The path is the same as in the box above.
>
> $$\begin{aligned}
> V_0 &= -\int_{\sigma_*}^{\sigma_P}\left(-k\,\mathbf r_0^P\right)\cdot\frac{d\mathbf r_0^P}{d\sigma}\,d\sigma \quad &\text{(Eq. 4.14 with the parameter of the path)} \\
> &= k\int_{\sigma_*}^{\sigma_P}\mathbf r_0^P\cdot\frac{d\mathbf r_0^P}{d\sigma}\,d\sigma \quad &\text{(the two minus signs cancel; $k$ is constant)} \\
> \frac{d}{d\sigma}\left(\mathbf r_0^P\cdot\mathbf r_0^P\right) &= \frac{d\mathbf r_0^P}{d\sigma}\cdot\mathbf r_0^P + \mathbf r_0^P\cdot\frac{d\mathbf r_0^P}{d\sigma} \quad &\text{(product rule for the dot product, Eq. 1.66)} \\
> &= \mathbf r_0^P\cdot\frac{d\mathbf r_0^P}{d\sigma} + \mathbf r_0^P\cdot\frac{d\mathbf r_0^P}{d\sigma} \quad &\text{(commutativity, Eq. 1.25)} \\
> &= 2\,\mathbf r_0^P\cdot\frac{d\mathbf r_0^P}{d\sigma} \quad &\text{(add the two equal terms)} \\
> V_0 &= \frac{k}{2}\int_{\sigma_*}^{\sigma_P}\frac{d}{d\sigma}\left(\mathbf r_0^P\cdot\mathbf r_0^P\right)d\sigma \quad &\text{(substitute the integrand)} \\
> &= \frac{k}{2}\Big[\mathbf r_0^P\cdot\mathbf r_0^P\Big]_{\sigma_*}^{\sigma_P} \quad &\text{(antiderivative of a derivative)} \\
> &= \frac{k}{2}\left((r_0^P)^2 - (r_{0,*}^P)^2\right) \quad &\text{(Barrow: value at $\sigma_P$ minus value at $\sigma_*$)} \\
> &= \frac{k}{2}\,(r_0^P)^2 \quad &\text{(reference position at the origin)}
> \end{aligned}$$
>
> $$\boxed{V_0 = \tfrac12\,k\,(r_0^P)^2}$$
>
> **Units:** $k$ in $\mathrm{N/m}$, so $(\mathrm{N/m})\,\mathrm{m^2} = \mathrm J$
> **Meaning:** the potential energy depends only on the distance to the origin, whatever the path, so the spring force is conservative; it is zero with the spring unstretched and grows with the square of the stretch.

A pair of internal forces between two particles $P$ and $Q$ may also be conservative; it then has a single potential energy, a function of both positions, and each force is minus the derivative of it with respect to the position of the particle it acts on ([Lecture 2, Slide 16]).

> [!derivation] Electrostatic pair: the forces from one potential
> **Law:** gradient with respect to the position of one particle; chain rule; Newton's third law as a check
> **Source:** [Lecture 2, Slide 16]; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 1.66
>
> $d$ is the distance between the particles; the derivative with respect to $\mathbf r_0^P$ is the gradient with respect to the coordinates of $P$, with $Q$ held fixed.
>
> $$\begin{aligned}
> V_0 &= \frac{k_0\,q^{\mathrm P}q^{\mathrm Q}}{d},\qquad d = \left\lVert\mathbf r_0^P - \mathbf r_0^Q\right\rVert \quad &\text{(potential of the pair, Slide 16)} \\
> d^2 &= \left(\mathbf r_0^P - \mathbf r_0^Q\right)\cdot\left(\mathbf r_0^P - \mathbf r_0^Q\right) \quad &\text{(square of a magnitude)} \\
> 2\,d\,\frac{\partial d}{\partial\mathbf r_0^P} &= 2\left(\mathbf r_0^P - \mathbf r_0^Q\right) \quad &\text{(differentiate both sides with respect to $\mathbf r_0^P$: chain rule on the left, Eq. 1.66 on the right)} \\
> \frac{\partial d}{\partial\mathbf r_0^P} &= \frac{\mathbf r_0^P - \mathbf r_0^Q}{d} \quad &\text{(divide by $2d$)} \\
> \frac{\partial V_0}{\partial\mathbf r_0^P} &= -\frac{k_0\,q^{\mathrm P}q^{\mathrm Q}}{d^2}\,\frac{\partial d}{\partial\mathbf r_0^P} \quad &\text{(chain rule: the derivative of $1/d$ is $-1/d^2$)} \\
> \mathbf F_{\mathrm P} &= -\frac{\partial V_0}{\partial\mathbf r_0^P} \quad &\text{(force on $P$, Slide 16)} \\
> &= \frac{k_0\,q^{\mathrm P}q^{\mathrm Q}}{d^3}\left(\mathbf r_0^P - \mathbf r_0^Q\right) \quad &\text{(substitute the two rows above)} \\
> \frac{\partial d}{\partial\mathbf r_0^Q} &= -\frac{\mathbf r_0^P - \mathbf r_0^Q}{d} \quad &\text{(the same steps with respect to $\mathbf r_0^Q$: the inner derivative is $-1$)} \\
> \mathbf F_{\mathrm Q} &= -\frac{\partial V_0}{\partial\mathbf r_0^Q} \quad &\text{(force on $Q$, Slide 16)} \\
> &= -\mathbf F_{\mathrm P} \quad &\text{(only the sign of the inner derivative changes)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_{\mathrm P} = \frac{k_0\,q^{\mathrm P}q^{\mathrm Q}}{\left\lVert\mathbf r_0^P - \mathbf r_0^Q\right\rVert^3}\left(\mathbf r_0^P - \mathbf r_0^Q\right) = -\mathbf F_{\mathrm Q}}$$
>
> **Units:** $k_0$ in $\mathrm{N\,m^2/C^2}$ and charges in $\mathrm C$: $V_0$ in $\mathrm{N\,m} = \mathrm J$, the forces in $(\mathrm{N\,m^2})\,\mathrm m/\mathrm{m^3} = \mathrm N$
> **Meaning:** the forces lie along the line joining the particles, are equal and opposite (the third law comes out of the single potential), have a magnitude inversely proportional to the square of the distance, and push the particles apart when the charges have the same sign.

> [!derivation] Example of Slide 17: a radial force proportional to R
> **Law:** line integral with the cylindrical differential of the position; substitution in the integral; Barrow's rule; gradient check
> **Source:** [Lecture 2, Slide 17]; Notes.pdf, Eq. 2.29; Notes.pdf, Eq. 2.23; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 4.20
>
> The force is $c_3 R\,\mathbf e_R$ (the slide writes $a$ for $c_3$), in cylindrical coordinates. The path runs from $\sigma_*$ to $\sigma_P$, where the radius goes from $R_*$ to $R$.
>
> $$\begin{aligned}
> d\mathbf r_0^P &= dR\,\mathbf e_R + R\,d\theta\,\mathbf e_\theta + dz\,\mathbf e_z \quad &\text{(Eq. 2.29 multiplied by $dt$)} \\
> \mathbf F\cdot d\mathbf r_0^P &= c_3 R\,dR \quad &\text{($\mathbf e_R\cdot\mathbf e_R = 1$, $\mathbf e_R\cdot\mathbf e_\theta = \mathbf e_R\cdot\mathbf e_z = 0$)} \\
> V_0 &= -\int_{\sigma_*}^{\sigma_P}c_3 R\,\frac{dR}{d\sigma}\,d\sigma \quad &\text{(Eq. 4.14 along the path)} \\
> &= -\int_{R_*}^{R}c_3 R'\,dR' \quad &\text{(substitution $R' = R(\sigma)$, differential $dR' = (dR/d\sigma)\,d\sigma$, limits $R_*$ and $R$)} \\
> &= -c_3\left[\frac{R'^2}{2}\right]_{R_*}^{R} \quad &\text{(antiderivative of $R'$)} \\
> &= -\frac{c_3}{2}\left(R^2 - R_*^2\right) \quad &\text{(Barrow)} \\
> &= -\frac{c_3}{2}\,R^2 \quad &\text{(reference on the axis, $R_* = 0$)} \\
> &= -\frac{c_3}{2}\left(x^2 + y^2\right) \quad &\text{(Eq. 2.23)} \\
> -\nabla V_0 &= c_3\left(x\,\mathbf i + y\,\mathbf j\right) \quad &\text{(Eq. 4.20: derivatives $-c_3 x$ and $-c_3 y$)} \\
> &= c_3 R\left(\cos\theta\,\mathbf i + \sin\theta\,\mathbf j\right) \quad &\text{(Eq. 2.23)} \\
> &= c_3 R\,\mathbf e_R \quad &\text{(Eq. 2.24: the gradient gives back the force)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = c_3 R\,\mathbf e_R \ \text{is conservative},\qquad V_0 = -\tfrac12\,c_3 R^2}$$
>
> **Units:** $c_3$ in $\mathrm{N/m}$; $V_0$ in $(\mathrm{N/m})\,\mathrm{m^2} = \mathrm J$
> **Meaning:** the work depends only on the initial and final distances to the axis, whatever the path, so the force has a potential. For a positive $c_3$ it pushes away from the axis and its potential energy decreases outwards; for a negative one it is a spring force towards the axis.

![[attachments/EM-T/t2-closed-circle.svg]]

> [!derivation] Example of Slide 18: an azimuthal force proportional to R squared
> **Law:** work around a closed path (Eq. 4.17); curl in components (Eq. 4.18)
> **Source:** [Lecture 2, Slide 18]; Notes.pdf, Eq. 4.17; Notes.pdf, Eq. 4.18; Notes.pdf, Eq. 1.76; Notes.pdf, Eq. 2.24; Notes.pdf, Eq. 2.29
>
> The force is $c_4 R^2\,\mathbf e_\theta$ (the slide writes $b$ for $c_4$). The closed path $\Gamma$ is the circle of radius $R_0$ about $Oz$ in a plane of constant $z$, run once counterclockwise with $\theta$ from $0$ to $2\pi$ as its parameter.
>
> $$\begin{aligned}
> d\mathbf r_0^P &= R_0\,d\theta\,\mathbf e_\theta \quad &\text{(Eq. 2.29 with $R = R_0$ and $z$ constant: $dR = dz = 0$)} \\
> \mathbf F\cdot d\mathbf r_0^P &= c_4 R_0^2\,R_0\,d\theta \quad &\text{($\mathbf e_\theta\cdot\mathbf e_\theta = 1$)} \\
> \oint_\Gamma\mathbf F\cdot d\mathbf r_0^P &= \int_0^{2\pi}c_4 R_0^3\,d\theta \quad &\text{(the integrand is constant along the circle)} \\
> &= c_4 R_0^3\,\big[\theta\big]_0^{2\pi} \quad &\text{(antiderivative of a constant)} \\
> &= 2\pi\,c_4 R_0^3 \quad &\text{(Barrow)} \\
> \mathbf F &= c_4 R^2\,\frac{-y\,\mathbf i + x\,\mathbf j}{R} \quad &\text{(Eq. 2.24 with $\cos\theta = x/R$, $\sin\theta = y/R$)} \\
> &= -c_4 y\sqrt{x^2+y^2}\,\mathbf i + c_4 x\sqrt{x^2+y^2}\,\mathbf j \quad &\text{(simplify, with $R$ written in Cartesian coordinates)} \\
> \frac{\partial}{\partial x}\sqrt{x^2+y^2} &= \frac{x}{\sqrt{x^2+y^2}} \quad &\text{(chain rule: derivative of the square root, one over twice the root, times $2x$)} \\
> \frac{\partial}{\partial y}\sqrt{x^2+y^2} &= \frac{y}{\sqrt{x^2+y^2}} \quad &\text{(the same with respect to $y$)} \\
> \frac{\partial F_y}{\partial x} &= c_4\sqrt{x^2+y^2} + c_4 x\,\frac{x}{\sqrt{x^2+y^2}} \quad &\text{(product rule on $c_4 x\sqrt{x^2+y^2}$)} \\
> \frac{\partial F_x}{\partial y} &= -c_4\sqrt{x^2+y^2} - c_4 y\,\frac{y}{\sqrt{x^2+y^2}} \quad &\text{(product rule on $-c_4 y\sqrt{x^2+y^2}$)} \\
> \left(\nabla\times\mathbf F\right)\cdot\mathbf k &= c_4\sqrt{x^2+y^2} + \frac{c_4 x^2}{\sqrt{x^2+y^2}} + c_4\sqrt{x^2+y^2} + \frac{c_4 y^2}{\sqrt{x^2+y^2}} \quad &\text{(Eq. 1.76: the first minus the second)} \\
> &= 2\,c_4\sqrt{x^2+y^2} + c_4\,\frac{x^2+y^2}{\sqrt{x^2+y^2}} \quad &\text{(group the like terms)} \\
> &= 2\,c_4 R + c_4 R \quad &\text{($\sqrt{x^2+y^2}$ is $R$, and so is the fraction)} \\
> &= 3\,c_4 R \quad &\text{(add)}
> \end{aligned}$$
>
> $$\boxed{\oint_\Gamma\mathbf F\cdot d\mathbf r_0^P = 2\pi\,c_4 R_0^3 \neq 0,\qquad \left(\nabla\times\mathbf F\right)\cdot\mathbf k = 3\,c_4 R \neq 0 \quad (c_4 \neq 0)}$$
>
> **Units:** $c_4$ in $\mathrm{N/m^2}$: the work in $(\mathrm{N/m^2})\,\mathrm{m^3} = \mathrm J$, the curl in $\mathrm{N/m}$
> **Meaning:** the work around a closed circle is not zero (it changes sign with the sense of travel), so Eq. 4.17 fails and the force is not conservative: no potential energy exists, even though the force depends only on the position. The curl, nonzero off the axis, says the same through Eq. 4.18.

## 5. Conservation of mechanical energy

The mechanical energy $E_0$ of a particle is the sum of its kinetic energy $T_0$ and its potential energy $V_0$ (Notes.pdf, Sec. 4.5).

> [!key] Principle of conservation of mechanical energy (Notes.pdf, Sec. 4.5)
> "If all the forces that exert non-zero work on a particle are conservative, then the mechanical energy of the particle is a conserved quantity of motion."

### One-dimensional motion

Consider first a particle moving along the axis $Ox$ of an inertial frame $S_0$ under a conservative force $F(x)\,\mathbf i$ (Notes.pdf, Sec. 4.5).

> [!derivation] Equation of motion of a particle on a line
> **Law:** Newton's second law projected on $\mathbf i$
> **Source:** Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 4.3; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= F(x)\,\mathbf i \quad &\text{(second law, Eq. 4.3)} \\
> \mathbf a_0^P &= \frac{d^2x}{dt^2}\,\mathbf i \quad &\text{(Eq. 2.7 with $y$ and $z$ constant)} \\
> m\,\ddot x &= F(x) \quad &\text{(dot-multiply by $\mathbf i$)}
> \end{aligned}$$
>
> $$\boxed{m\,\ddot x = F(x)}$$
>
> **Units:** $\mathrm N$ on both sides
> **Meaning:** an ordinary differential equation of second order: integrating it twice gives $x(t)$ with two arbitrary constants, fixed by the initial conditions $x_0$ and the initial velocity (Notes.pdf, Sec. 4.5).

> [!derivation] Conservation of mechanical energy in one dimension
> **Law:** multiplication of the equation of motion by the velocity; integration in time with a substitution in each term; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.23; Notes.pdf, Eq. 4.24; Notes.pdf, Eq. 4.25; Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.15
>
> Between the instants $t_1$ and $t_2$ the particle goes from $x_1$ to $x_2$ and its velocity from $\dot x_1$ to $\dot x_2$.
>
> $$\begin{aligned}
> \int_{t_1}^{t_2}m\,\dot x\,\frac{d\dot x}{dt}\,dt - \int_{t_1}^{t_2}F(x)\,\frac{dx}{dt}\,dt &= 0 \quad &\text{(multiply Eq. 4.21 by $\dot x$ and integrate, Eq. 4.22)} \\
> \int_{t_1}^{t_2}m\,\dot x\,\frac{d\dot x}{dt}\,dt &= \int_{\dot x_1}^{\dot x_2}m\,\eta\,d\eta \quad &\text{(substitution $\eta = \dot x$, differential $d\eta = (d\dot x/dt)\,dt$, limits $\dot x_1$ and $\dot x_2$)} \\
> &= \left[\tfrac12\,m\,\eta^2\right]_{\dot x_1}^{\dot x_2} \quad &\text{(antiderivative of $m\,\eta$)} \\
> &= \tfrac12\,m\,\dot x_2^2 - \tfrac12\,m\,\dot x_1^2 \quad &\text{(Barrow)} \\
> &= T_{0,2} - T_{0,1} \quad &\text{(Eq. 4.2 with $\mathbf v_0^P = \dot x\,\mathbf i$; Eq. 4.23)} \\
> -\int_{t_1}^{t_2}F(x)\,\frac{dx}{dt}\,dt &= -\int_{x_1}^{x_2}F(x)\,dx \quad &\text{(substitution $x = x(t)$, differential $dx = \dot x\,dt$, limits $x_1$ and $x_2$)} \\
> &= -\int_{x_1}^{x_{\mathrm{ref}}}F\,dx - \int_{x_{\mathrm{ref}}}^{x_2}F\,dx \quad &\text{(split the interval at the reference position $x_{\mathrm{ref}}$ of $V_0$)} \\
> &= \int_{x_{\mathrm{ref}}}^{x_1}F\,dx - \int_{x_{\mathrm{ref}}}^{x_2}F\,dx \quad &\text{(reverse the limits of the first integral)} \\
> &= V_{0,2} - V_{0,1} \quad &\text{(Eq. 4.15 at $x_2$ and at $x_1$; Eq. 4.24)} \\
> T_{0,2} - T_{0,1} + V_{0,2} - V_{0,1} &= 0 \quad &\text{(substitute both terms in the first row; Eq. 4.25)} \\
> T_{0,2} + V_{0,2} &= T_{0,1} + V_{0,1} \quad &\text{(rearrange)}
> \end{aligned}$$
>
> $$\boxed{T_0 + V_0 = E_0 = \mathrm{const}}$$
>
> **Units:** $\mathrm J$ in every term
> **Meaning:** the instant $t_2$ is arbitrary, so dropping its subindex gives Eq. 4.26 with the constant set by the initial state, $E_0$ equal to $T_{0,1}$ plus $V_{0,1}$: the mechanical energy is conserved. Whether it is conserved depends on the reference frame: in another frame non-conservative forces may work, and forces of inertia may appear (Notes.pdf, Sec. 4.5).

Energy conservation does not give the position as a function of time, but it says a great deal about the motion. With the initial position and velocity the constant $E_0$ is known, and the energy equation then gives the speed as a function of the position (Notes.pdf, Sec. 4.5; [Lecture 2, Slide 20]).

> [!derivation] Speed, allowed regions and turning points
> **Law:** conservation of mechanical energy; the kinetic energy is not negative
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.26; [Lecture 2, Slide 20]
>
> $$\begin{aligned}
> \tfrac12\,m\,\dot x^2 &= E_0 - V_0(x) \quad &\text{(Eq. 4.26 with the kinetic energy written out; Eq. 4.27)} \\
> \lvert\dot x\rvert &= \sqrt{\frac{2\left(E_0 - V_0(x)\right)}{m}} \quad &\text{(solve for the speed)} \\
> \tfrac12\,m\,\dot x^2 &\geq 0 \quad &\text{(square of a real number times a positive mass)} \\
> V_0(x) &\leq E_0 \quad &\text{(first row; Eq. 4.28)} \\
> \dot x &= 0 \ \text{ where } V_0(x) = E_0 \quad &\text{(first row at the boundary of the allowed region)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12\,m\,\dot x^2 = E_0 - V_0(x),\qquad V_0(x) \leq E_0}$$
>
> **Units:** $\mathrm J$ in the energy relations; $\sqrt{\mathrm J/\mathrm{kg}} = \mathrm{m/s}$ for the speed
> **Meaning:** the vertical gap between the line of height $E_0$ and the curve $V_0(x)$ is the kinetic energy, so it gives the speed at each position, but not the sense of motion. The particle is confined to the allowed regions where the curve lies below the line and cannot enter the forbidden regions where it lies above; at the points where they meet, the turning points, it stops for an instant and turns back ([Lecture 2, Slide 20]).

![[attachments/EM-T/t2-energy-diagram.svg]]

In the potential of Fig. 4.2, a particle with the energy $E_{0,1}$ is confined to the valley of the potential, or to one of the outer regions; with $E_{0,2}$ the valley connects with the region on the right and the particle may escape there; with $E_{0,3}$ it may access every region (Notes.pdf, Sec. 4.5). Raising the mechanical energy opens parts of space that were unavailable, but being allowed to reach a region does not mean that the particle will travel there: the actual trajectory still requires solving the equation of motion, Eq. 4.21. Sketching a given potential, with its maxima, minima and asymptotes found analytically, is an important skill for the student ([Lecture 2, Slide 20]).

> [!warning] Slip in [Lecture 2, Slide 20]: a missing mass
> The slide writes the kinetic energy as one half of the square of the speed, equal to the mechanical energy minus the potential energy, without the mass. The kinetic energy is half the mass times the square of the speed (Notes.pdf, Eq. 4.2 and Eq. 4.27), as in the box above; without $m$ the two sides would not even have the same units ($\mathrm{m^2/s^2}$ against $\mathrm J$).

### Two- and three-dimensional motion

The mechanical energy is also conserved in space when all the forces that work on the particle derive from a potential. The statement allows non-conservative forces to act, as long as they do no work, for instance when they are always perpendicular to the velocity (Notes.pdf, Sec. 4.5.1).

> [!derivation] Conservation of mechanical energy in space
> **Law:** second law dotted with the velocity and integrated in time; force as minus the gradient; total differential; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.30; Notes.pdf, Eq. 4.31; Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.20
>
> $$\begin{aligned}
> \int_{t_1}^{t_2}m\,\mathbf v_0^P\cdot\left.\frac{d\mathbf v_0^P}{dt}\right|_0 dt - \int_{t_1}^{t_2}\mathbf F\cdot\mathbf v_0^P\,dt &= 0 \quad &\text{(dot-multiply Eq. 4.3 by $\mathbf v_0^P$ and integrate, Eq. 4.29)} \\
> m\,\mathbf v_0^P\cdot\left.\frac{d\mathbf v_0^P}{dt}\right|_0 &= \frac{dT_0}{dt} \quad &\text{(the steps of the box on Eq. 4.11, read backwards)} \\
> \int_{t_1}^{t_2}\frac{dT_0}{dt}\,dt &= T_{0,2} - T_{0,1} \quad &\text{(Barrow)} \\
> -\int_{t_1}^{t_2}\mathbf F\cdot\mathbf v_0^P\,dt &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\nabla V_0\cdot d\mathbf r_0^P \quad &\text{($\mathbf F = -\nabla V_0$, Eq. 4.20; differential $d\mathbf r_0^P = \mathbf v_0^P\,dt$)} \\
> &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\left(\frac{\partial V_0}{\partial x}\,\mathbf i + \frac{\partial V_0}{\partial y}\,\mathbf j + \frac{\partial V_0}{\partial z}\,\mathbf k\right)\cdot\left(dx\,\mathbf i + dy\,\mathbf j + dz\,\mathbf k\right) \quad &\text{(gradient and differential in components)} \\
> &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}\left(\frac{\partial V_0}{\partial x}\,dx + \frac{\partial V_0}{\partial y}\,dy + \frac{\partial V_0}{\partial z}\,dz\right) \quad &\text{(dot product of orthonormal components)} \\
> &= \int_{\mathbf r_{0,1}^P}^{\mathbf r_{0,2}^P}dV_0 \quad &\text{(total differential of $V_0$)} \\
> &= V_{0,2} - V_{0,1} \quad &\text{(Barrow: $V_0$ is the antiderivative of $dV_0$)} \\
> T_{0,2} - T_{0,1} + V_{0,2} - V_{0,1} &= 0 \quad &\text{(substitute in the first row)}
> \end{aligned}$$
>
> $$\boxed{T_0 + V_0 = E_0}$$
>
> **Units:** $\mathrm J$ in every term
> **Meaning:** the same result as in one dimension, now for any conservative force in space (Notes.pdf, Sec. 4.5.1); the integral of the gradient along the path depends only on its end points.

### Conservative and non-conservative forces together

When a particle is subject to a conservative force $\mathbf F_C$ and a non-conservative force $\mathbf F_N$, the same steps give the rate at which its mechanical energy changes ([Lecture 2, Slide 19]).

> [!derivation] Rate of change of the mechanical energy
> **Law:** second law dotted with the velocity; chain rule for a scalar field along the motion
> **Source:** [Lecture 2, Slide 19]; Notes.pdf, Eq. 4.11; Notes.pdf, Eq. 4.20; Notes.pdf, Sec. 4.5.1
>
> $V_0$ is the potential energy of $\mathbf F_C$; it depends on time only through the position of $P$.
>
> $$\begin{aligned}
> m\left.\frac{d\mathbf v_0^P}{dt}\right|_0 &= \mathbf F_C + \mathbf F_N \quad &\text{(second law, Eq. 4.3)} \\
> m\left.\frac{d\mathbf v_0^P}{dt}\right|_0\cdot\mathbf v_0^P &= \mathbf F_C\cdot\mathbf v_0^P + \mathbf F_N\cdot\mathbf v_0^P \quad &\text{(dot-multiply by $\mathbf v_0^P$)} \\
> m\left.\frac{d\mathbf v_0^P}{dt}\right|_0\cdot\mathbf v_0^P &= \frac{dT_0}{dt} \quad &\text{(steps of the box on Eq. 4.11)} \\
> \mathbf F_C\cdot\mathbf v_0^P &= -\nabla V_0\cdot\left.\frac{d\mathbf r_0^P}{dt}\right|_0 \quad &\text{(Eq. 4.20 and Eq. 2.3)} \\
> &= -\left(\frac{\partial V_0}{\partial x}\,\dot x + \frac{\partial V_0}{\partial y}\,\dot y + \frac{\partial V_0}{\partial z}\,\dot z\right) \quad &\text{(dot product in components)} \\
> &= -\frac{dV_0}{dt} \quad &\text{(chain rule for $V_0(x(t), y(t), z(t))$)} \\
> \frac{dT_0}{dt} &= -\frac{dV_0}{dt} + \mathbf F_N\cdot\mathbf v_0^P \quad &\text{(substitute in the second row)} \\
> \frac{d}{dt}\left(T_0 + V_0\right) &= \mathbf F_N\cdot\mathbf v_0^P \quad &\text{(move the potential term to the left; sum rule)}
> \end{aligned}$$
>
> $$\boxed{\frac{dE_0}{dt} = \frac{dT_0}{dt} + \frac{dV_0}{dt} = \mathbf F_N\cdot\mathbf v_0^P,\qquad E_0 = T_0 + V_0}$$
>
> **Units:** $\mathrm W$ in every term
> **Meaning:** the mechanical energy changes at the rate of the power of the non-conservative forces. It is constant if and only if that power is zero at every instant: when no non-conservative force acts, or when the non-conservative forces are always perpendicular to the velocity and do no work ([Lecture 2, Slide 19]). The equation of conservation of energy is then a first integral of motion of the system ([Lecture 2, Slide 19]).

### Final comments

The conservation of energy was first derived from Newton's second law for a resultant force that depends only on the position, but its range of application is much wider: with other forms of energy (thermal, chemical, electromagnetic) it has been extended far beyond mechanics and is recognised as one of the most fundamental principles of physics (Notes.pdf, Sec. 4.5.2). Many forces that are non-conservative, or dissipative, in the macroscopic description of a problem are conservative on a microscopic scale. A body entering a retarding medium such as the atmosphere feels a velocity-dependent drag, non-conservative at the macroscopic scale; microscopically it undergoes a series of collisions with the molecules of the medium, each conserving energy, which pass part of its kinetic energy to the molecules and, through further collisions, spread it among them. The net result is the drag on the body and a rise of the average energy of the molecules, seen macroscopically as dissipated heat and a rise of the temperature of the medium.

## 6. Equilibrium

When a particle, or a system of particles, is and remains at rest, it is in an equilibrium point or configuration; the study of equilibrium is statics, a branch of mechanics (Notes.pdf, Sec. 4.6). A configuration is an equilibrium one if the particle, left in it with zero velocity, stays at rest indefinitely ([Lecture 2, Slide 21]).

> [!derivation] Equilibrium condition
> **Law:** definition of equilibrium; Newton's second law
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.4; [Lecture 2, Slide 21]
>
> Let the particle stay at the position $\mathbf r_0^*$ for all $t$.
>
> $$\begin{aligned}
> \mathbf r_0^P(t) &= \mathbf r_0^* \quad &\text{(at rest at $\mathbf r_0^*$ at every instant)} \\
> \mathbf v_0^P &= \left.\frac{d\mathbf r_0^*}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 2.3: the derivative of a constant vector)} \\
> \mathbf a_0^P &= \left.\frac{d\mathbf v_0^P}{dt}\right|_0 = \mathbf 0 \quad &\text{(Eq. 2.4)} \\
> \mathbf F\left(\mathbf r_0^*, \mathbf 0, t\right) &= m\,\mathbf a_0^P \quad &\text{(second law, Eq. 4.4, evaluated at rest at $\mathbf r_0^*$)} \\
> &= \mathbf 0 \quad &\text{(previous row)}
> \end{aligned}$$
>
> $$\boxed{\sum\mathbf F = \mathbf 0 \ \text{ at } \mathbf r_0^*}$$
>
> **Units:** $\mathrm N$
> **Meaning:** the equilibrium configurations are found by setting every velocity and acceleration to zero in the equations of motion, which is the same as requiring the sum of all the forces on each particle to vanish; the result is an algebraic system for the values of the coordinates in equilibrium (Notes.pdf, Sec. 4.6). Conversely, a particle left at rest where the resultant is zero has zero acceleration and stays there.

Equilibrium points are stable or unstable (Notes.pdf, Sec. 4.6). After a small perturbation, a system near a stable equilibrium oscillates about it, like a marble at the bottom of a bowl; if the oscillations are small enough the motion can always be linearised about the equilibrium and reduced to a harmonic oscillator, and if the system is dissipative the oscillations die out with time. Near an unstable equilibrium a small perturbation takes the system farther and farther away, like a ball on the peak of a mountain, which stays there indefinitely without perturbations but rolls down the slope after the smallest one. The precise definition of stability is the one of [Lecture 2, Slide 21]:

| The equilibrium position $\mathbf r_0^*$ is stable if and only if | for every pair of tolerances $\varepsilon_r, \varepsilon_v > 0$ there are $\delta_r, \delta_v > 0$ such that |
| :--- | :--- |
| the initial perturbation is small | $\lVert\mathbf r_0^P(0) - \mathbf r_0^*\rVert < \delta_r$ and $\lVert\mathbf v_0^P(0)\rVert < \delta_v$ |
| implies that the motion stays close for all $t > 0$ | $\lVert\mathbf r_0^P(t) - \mathbf r_0^*\rVert < \varepsilon_r$ and $\lVert\mathbf v_0^P(t)\rVert < \varepsilon_v$ |

Otherwise the equilibrium is unstable. To decide, one studies the forces in the neighbourhood of the equilibrium: if they tend to restore the system to the equilibrium configuration it is stable, if they push it further away it is unstable (Notes.pdf, Sec. 4.6).

![[attachments/EM-T/t2-stable-unstable.svg]]

> [!derivation] Equilibria of a conservative system are critical points of the potential
> **Law:** equilibrium condition with the force written as minus the gradient
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 4.32; Notes.pdf, Eq. 4.20; Notes.pdf, Eq. 4.16; [Lecture 2, Slide 22]
>
> $$\begin{aligned}
> \mathbf F(\mathbf r_0^*) &= \mathbf 0 \quad &\text{(Eq. 4.32)} \\
> -\nabla V_0(\mathbf r_0^*) &= \mathbf 0 \quad &\text{(conservative force, Eq. 4.20)} \\
> F(x^*) &= -\frac{dV_0}{dx}(x^*) = 0 \quad &\text{(one-dimensional problem, Eq. 4.16)}
> \end{aligned}$$
>
> $$\boxed{\nabla V_0(\mathbf r_0^*) = \mathbf 0;\qquad \text{in one dimension: } \frac{dV_0}{dx}(x^*) = 0}$$
>
> **Units:** $\mathrm J/\mathrm m = \mathrm N$
> **Meaning:** the equilibrium configurations are the critical points of the potential energy: in a plot of $V_0(x)$, the peaks, the valleys and any point with a horizontal tangent ([Lecture 2, Slide 22]).

> [!derivation] Restoring or repelling force near an equilibrium in one dimension
> **Law:** first-order Taylor expansion of the force about the equilibrium; force from the potential
> **Source:** [Lecture 2, Slide 22]; Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 4.16
>
> $\xi$ is a small displacement from the equilibrium position $x^*$ of a conservative one-dimensional problem.
>
> $$\begin{aligned}
> F(x^* + \xi) &= F(x^*) + \frac{dF}{dx}(x^*)\,\xi + O(\xi^2) \quad &\text{(Taylor expansion to first order)} \\
> &= \frac{dF}{dx}(x^*)\,\xi + O(\xi^2) \quad &\text{(equilibrium: $F(x^*) = 0$)} \\
> \frac{dF}{dx} &= -\frac{d^2V_0}{dx^2} \quad &\text{(differentiate Eq. 4.16)} \\
> F(x^* + \xi) &= -\frac{d^2V_0}{dx^2}(x^*)\,\xi + O(\xi^2) \quad &\text{(substitute)}
> \end{aligned}$$
>
> $$\boxed{\frac{dF}{dx}(x^*) = -\frac{d^2V_0}{dx^2}(x^*) < 0 \ \Longleftrightarrow\ \text{the force near } x^* \text{ has the sign of } -\xi \text{ (restoring): a minimum of } V_0}$$
>
> **Units:** $\mathrm N/\mathrm m$ for the derivative of the force and the second derivative of the potential
> **Meaning:** for a small enough displacement the first-order term dominates. With a positive second derivative of $V_0$ (a minimum, a valley) a displacement to the right ($\xi > 0$) meets a force to the left and a displacement to the left a force to the right: the force restores, the stability condition of [Lecture 2, Slide 22]. With a negative second derivative (a maximum, a peak) the force has the sign of $\xi$ and pushes the particle further away. The two boxes below turn these sign statements into the definition of stability.

> [!derivation] A strict minimum of the potential is a stable equilibrium
> **Law:** conservation of mechanical energy (Eq. 4.26) and the allowed region $V_0 \leq E_0$ (Eq. 4.28), applied to the definition of stability
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; [Lecture 2, Slide 21]
>
> Let $x^*$ be a strict local minimum of $V_0$ and let the tolerances $\varepsilon_r$, $\varepsilon_v$ be given, with $\varepsilon_r$ small enough that $V_0(x)$ is larger than $V_0(x^*)$ for every $x \neq x^*$ with $\lvert x - x^*\rvert \leq \varepsilon_r$. Define the depth of the well at that distance and a target margin:
>
> $$\begin{aligned}
> \Delta V &= \min\left\{V_0(x^* - \varepsilon_r),\ V_0(x^* + \varepsilon_r)\right\} - V_0(x^*) > 0 \quad &\text{(strict minimum)} \\
> E_0 - V_0(x^*) &= \tfrac12\,m\,\dot x(0)^2 + V_0\big(x(0)\big) - V_0(x^*) \quad &\text{(energy of the initial state, Eq. 4.26)} \\
> &< \tfrac12\,m\,\delta_v^2 + \left[V_0\big(x(0)\big) - V_0(x^*)\right] \quad &\text{(initial speed below $\delta_v$)} \\
> &< \min\left\{\Delta V,\ \tfrac12\,m\,\varepsilon_v^2\right\} \quad &\text{(choose $\delta_v$ and $\delta_r \leq \varepsilon_r$ small enough; $V_0$ is continuous at $x^*$)} \\
> V_0\big(x(t)\big) &\leq E_0 < V_0(x^*) + \Delta V \quad &\text{(allowed region, Eq. 4.28, at every $t > 0$; previous row)} \\
> \lvert x(t) - x^*\rvert &< \varepsilon_r \quad &\text{($x(t)$ is continuous, starts inside and cannot reach $x^* \pm \varepsilon_r$, where $V_0 \geq V_0(x^*) + \Delta V$)} \\
> \tfrac12\,m\,\dot x(t)^2 &= E_0 - V_0\big(x(t)\big) \quad &\text{(Eq. 4.27)} \\
> &\leq E_0 - V_0(x^*) \quad &\text{(inside the interval $V_0 \geq V_0(x^*)$)} \\
> &< \tfrac12\,m\,\varepsilon_v^2 \quad &\text{(choice of the initial perturbation)} \\
> \lvert\dot x(t)\rvert &< \varepsilon_v \quad &\text{(divide by $m/2$ and take the square root)}
> \end{aligned}$$
>
> $$\boxed{\lvert x(0) - x^*\rvert < \delta_r,\ \lvert\dot x(0)\rvert < \delta_v \ \Longrightarrow\ \lvert x(t) - x^*\rvert < \varepsilon_r,\ \lvert\dot x(t)\rvert < \varepsilon_v \ \ \forall\,t > 0}$$
>
> **Units:** energies in $\mathrm J$, distances in $\mathrm m$, speeds in $\mathrm{m/s}$; $\tfrac12\,m\,\varepsilon_v^2$ is in $\mathrm{kg\,(m/s)^2} = \mathrm J$
> **Meaning:** a particle started close to the bottom of a well with a small speed has too little energy to climb out of it, and its speed stays small because the gap between $E_0$ and the curve stays small: this is the definition of stability of [Lecture 2, Slide 21], and it shows the notes' criterion, stable at a minimum of the potential, from the energy alone (Notes.pdf, Sec. 4.6).

> [!derivation] Small motions about an equilibrium: oscillation or departure
> **Law:** equation of motion with the force expanded to first order; characteristic equation of a linear equation with constant coefficients
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 5.7; [Lecture 2, Slide 22]
>
> The stiffness at the equilibrium is the second derivative of the potential there; $C_1$, $C_2$ are integration constants and $\xi_0$, $\dot\xi_0$ the initial displacement and velocity.
>
> $$\begin{aligned}
> m\,\ddot\xi &= -\frac{d^2V_0}{dx^2}(x^*)\,\xi \quad &\text{(Eq. 4.21 with the first-order force of the box above; $\ddot x = \ddot\xi$ because $x^*$ is constant)} \\
> \xi &= \exp(p\,t) \quad &\text{(trial solution of a linear equation with constant coefficients)} \\
> m\,p^2\exp(p\,t) &= -\frac{d^2V_0}{dx^2}(x^*)\exp(p\,t) \quad &\text{(substitute: each time derivative brings a factor $p$)} \\
> m\,p^2 + \frac{d^2V_0}{dx^2}(x^*) &= 0 \quad &\text{(divide by the exponential, never zero: characteristic equation)} \\
> p &= \pm\,i\sqrt{\frac{d^2V_0/dx^2(x^*)}{m}} \quad &\text{(minimum: positive second derivative, two imaginary roots)} \\
> \xi &= C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t),\quad \omega_0 = \sqrt{\frac{d^2V_0/dx^2(x^*)}{m}} \quad &\text{(real form of the solution with imaginary roots, Eq. 5.7)} \\
> p &= \pm\,p_1,\quad p_1 = \sqrt{\frac{-d^2V_0/dx^2(x^*)}{m}} > 0 \quad &\text{(maximum: negative second derivative, two real roots)} \\
> \xi &= C_1\exp(p_1 t) + C_2\exp(-p_1 t) \quad &\text{(general solution with two real roots)} \\
> \dot\xi &= p_1 C_1\exp(p_1 t) - p_1 C_2\exp(-p_1 t) \quad &\text{(differentiate; chain rule on each exponential)} \\
> \xi_0 &= C_1 + C_2,\qquad \dot\xi_0 = p_1\left(C_1 - C_2\right) \quad &\text{(both rows at $t = 0$)} \\
> C_1 &= \tfrac12\left(\xi_0 + \frac{\dot\xi_0}{p_1}\right) \quad &\text{(add the first equation to the second divided by $p_1$, then halve)}
> \end{aligned}$$
>
> $$\boxed{\text{minimum: } \xi = C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t);\qquad \text{maximum: } \xi = C_1\exp(p_1 t) + C_2\exp(-p_1 t),\ \ C_1 = \tfrac12\left(\xi_0 + \dot\xi_0/p_1\right)}$$
>
> **Units:** $\omega_0$ and $p_1$ in $\sqrt{(\mathrm{N/m})/\mathrm{kg}} = \mathrm{s^{-1}}$, so their products with $t$ are dimensionless; $C_1$, $C_2$ in $\mathrm m$
> **Meaning:** at a minimum the linearised motion is a bounded oscillation about the equilibrium, a harmonic oscillator (Chapter 5). At a maximum every perturbation with $C_1 \neq 0$, which is every perturbation except those with the initial velocity exactly $-p_1\xi_0$, grows like $\exp(p_1 t)$ and carries the particle away, so the equilibrium is unstable; the linear model holds only while $\xi$ is small, which is enough to show the departure. A full treatment of linearisation about an equilibrium is given with the harmonic oscillator (Lecture 6).

> [!warning] When the second derivative is zero
> If the second derivative of $V_0$ vanishes at the equilibrium, the first-order force is zero and the boxes above decide nothing: the sign of the force near $x^*$, and with it the stability, is then set by the higher-order terms of the expansion of $V_0$. In two and three dimensions the equilibria are the points where the gradient of $V_0$ vanishes, and an equilibrium is stable if and only if it is a local minimum of the potential energy, which is checked with the second derivatives of $V_0$ (Notes.pdf, Sec. 4.6).

![[attachments/EM-T/t2-equilibria.svg]]

## 7. The simple pendulum

The simple pendulum illustrates the conservation of mechanical energy and the kind of analysis it allows (Notes.pdf, Sec. 4.7; [Lecture 2, Slide 23]): kinematics and dynamics of this simple system, the discussion of its energy, and the linearisation of its equation of motion.

> [!example] The simple pendulum (Notes.pdf, Sec. 4.7, Fig. 4.3; [Lecture 2, Slide 23])
> A bob of mass $m$ hangs from a fixed point $O$ of the inertial frame $S_0$ by a light rigid rod of length $\ell$ and negligible mass, and moves in the vertical plane $Oxy$ under gravity, with $Oy$ vertical and upwards. The problem is solved in polar coordinates $(R, \theta)$, with the angle $\theta$ measured from the downward vertical, the direction of $-Oy$, positive counterclockwise, and with the local basis $\{\mathbf e_R, \mathbf e_\theta\}$ of Notes.pdf, Sec. 2.6.2. Since the distance from $O$ is the constant $\ell$, the problem has a single degree of freedom, the coordinate $\theta$.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial; $\mathbf i$ horizontal to the right, $\mathbf j$ vertical upwards, $\mathbf k$ out of the paper |
> | bob | mass $m$, at distance $R = \ell$ from $O$ (constant) |
> | gravity | $\mathbf g = -g\,\mathbf j$ |
> | coordinate | $\theta$, from $-\mathbf j$ to the rod, counterclockwise |

![[attachments/EM-T/t2-pendulum.svg]]

### Position, basis and kinematics

> [!derivation] The angle from the vertical and the standard polar angle
> **Law:** right triangle of the rod with the vertical; cylindrical coordinates; angle subtraction formulas
> **Source:** Notes.pdf, Sec. 4.7; Notes.pdf Fig. 4.3; Notes.pdf, Eq. 2.23
>
> Main plane, $\mathbf k$ out of the paper (⊙): the bob $P$, the pivot $O$ and the foot $H$ of the perpendicular from $P$ to the vertical through $O$ form a right triangle, right-angled at $H$, with hypotenuse $OP$ of length $\ell$ and the angle $\theta$ at $O$, between the downward vertical $OH$ and the rod. $\theta_{\mathrm{pol}}$ is the standard polar angle of $P$, measured from $Ox$ counterclockwise, as in Eq. 2.23.
>
> $$\begin{aligned}
> x &= \ell\sin\theta \quad &\text{(leg $HP$, opposite to $\theta$, horizontal and to the right for $\theta > 0$)} \\
> y &= -\ell\cos\theta \quad &\text{(leg $OH$, adjacent to $\theta$, pointing along $-\mathbf j$)} \\
> x &= \ell\cos\theta_{\mathrm{pol}},\quad y = \ell\sin\theta_{\mathrm{pol}} \quad &\text{(standard polar coordinates of $P$, Eq. 2.23 with $R = \ell$)} \\
> \cos\left(\theta - \tfrac{\pi}{2}\right) &= \cos\theta\cos\tfrac{\pi}{2} + \sin\theta\sin\tfrac{\pi}{2} \quad &\text{(cosine of a difference)} \\
> &= \sin\theta \quad &\text{($\cos\tfrac{\pi}{2} = 0$, $\sin\tfrac{\pi}{2} = 1$)} \\
> \sin\left(\theta - \tfrac{\pi}{2}\right) &= \sin\theta\cos\tfrac{\pi}{2} - \cos\theta\sin\tfrac{\pi}{2} \quad &\text{(sine of a difference)} \\
> &= -\cos\theta \quad &\text{(the same values)} \\
> \theta_{\mathrm{pol}} &= \theta - \tfrac{\pi}{2} \quad &\text{(this angle gives the same $x$ and $y$ as the triangle, both rows)}
> \end{aligned}$$
>
> $$\boxed{x = \ell\sin\theta,\quad y = -\ell\cos\theta;\qquad \theta_{\mathrm{pol}} = \theta - \tfrac{\pi}{2}}$$
>
> **Units:** $x$, $y$, $\ell$ in $\mathrm m$; angles in $\mathrm{rad}$
> **Meaning:** measuring the angle from the downward vertical instead of from $Ox$ swaps the roles of sine and cosine and brings a minus sign into the vertical coordinate: the bob is below $O$ while $\lvert\theta\rvert < \pi/2$. The two angles grow together, so their rates are equal.

![[attachments/EM-T/t2-pendulum-basis.svg]]

> [!derivation] Polar basis of the pendulum and its change of basis matrix
> **Law:** cylindrical local basis at the polar angle; change of basis matrix with the local unit vectors as columns; determinant; orthogonality; right-handedness
> **Source:** Notes.pdf, Eq. 2.24; Notes.pdf, Sec. 2.6.2; Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.32
>
> View along $\mathbf k$, which points out of the paper (⊙): $\mathbf e_R$ points from $O$ along the rod to the bob; the angle $\theta$ lies between $-\mathbf j$ and $\mathbf e_R$, so in the right triangle of unit hypotenuse $\mathbf e_R$ its leg along $-\mathbf j$ (adjacent) is $\cos\theta$, which is the minus sign of the $\mathbf j$ component, and its leg along $\mathbf i$ (opposite) is $\sin\theta$. $\mathbf e_\theta$ is $\mathbf e_R$ turned a quarter turn counterclockwise, the sense in which $\theta$ grows by the right-hand rule about $\mathbf k$; the same angle $\theta$ lies between $\mathbf i$ and $\mathbf e_\theta$, so its leg along $\mathbf i$ (adjacent) is $\cos\theta$ and its leg along $\mathbf j$ (opposite) is $\sin\theta$, both positive for $\theta$ between $0$ and $\pi/2$.
>
> $$\begin{aligned}
> \mathbf e_R &= \cos\theta_{\mathrm{pol}}\,\mathbf i + \sin\theta_{\mathrm{pol}}\,\mathbf j \quad &\text{(Eq. 2.24 at the polar angle)} \\
> &= \sin\theta\,\mathbf i - \cos\theta\,\mathbf j \quad &\text{(box above: the cosine and the sine of $\theta - \pi/2$)} \\
> \mathbf e_\theta &= -\sin\theta_{\mathrm{pol}}\,\mathbf i + \cos\theta_{\mathrm{pol}}\,\mathbf j \quad &\text{(Eq. 2.24)} \\
> &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(the same substitution: $-\sin(\theta - \pi/2) = \cos\theta$)} \\
> [{}_0R_{\mathrm{pol}}] &= \begin{pmatrix} \sin\theta & \cos\theta & 0 \cr -\cos\theta & \sin\theta & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf e_R$, $\mathbf e_\theta$, $\mathbf k$ in $\mathcal B_0$, Eq. 1.13)} \\
> &= [{}_0R_1(z,\theta_{\mathrm{pol}})] \quad &\text{(Eq. 1.20: a simple rotation about $\mathbf k$ by $\theta - \pi/2$)} \\
> \det[{}_0R_{\mathrm{pol}}] &= 1\cdot\left(\sin\theta\sin\theta - \cos\theta\,(-\cos\theta)\right) \quad &\text{(expand along the third row)} \\
> &= \sin^2\theta + \cos^2\theta \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_{\mathrm{pol}}][{}_0R_{\mathrm{pol}}]^T\right)_{11} &= \sin\theta\sin\theta + \cos\theta\cos\theta + 0\cdot 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_{\mathrm{pol}}][{}_0R_{\mathrm{pol}}]^T\right)_{12} &= \sin\theta\,(-\cos\theta) + \cos\theta\sin\theta + 0\cdot 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)} \\
> \mathbf e_R\times\mathbf e_\theta &= \sin\theta\cos\theta\,\mathbf i\times\mathbf i + \sin^2\theta\,\mathbf i\times\mathbf j - \cos^2\theta\,\mathbf j\times\mathbf i - \cos\theta\sin\theta\,\mathbf j\times\mathbf j \quad &\text{(distribute, Eq. 1.32)} \\
> &= \sin^2\theta\,\mathbf i\times\mathbf j - \cos^2\theta\,\mathbf j\times\mathbf i \quad &\text{($\mathbf i\times\mathbf i = \mathbf j\times\mathbf j = \mathbf 0$)} \\
> &= \sin^2\theta\,\mathbf k + \cos^2\theta\,\mathbf k \quad &\text{($\mathbf i\times\mathbf j = \mathbf k$, $\mathbf j\times\mathbf i = -\mathbf k$)} \\
> &= \mathbf k \quad &\text{(Pythagoras)}
> \end{aligned}$$
>
> $$\boxed{\mathbf e_R = \sin\theta\,\mathbf i - \cos\theta\,\mathbf j,\qquad \mathbf e_\theta = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j;\qquad [{}_0R_{\mathrm{pol}}] = \begin{bmatrix} \sin\theta & \cos\theta & 0 \\ -\cos\theta & \sin\theta & 0 \\ 0 & 0 & 1 \end{bmatrix},\ \ \det = 1}$$
>
> **Units:** dimensionless
> **Meaning:** the remaining entries of $[{}_0R_{\mathrm{pol}}][{}_0R_{\mathrm{pol}}]^T$ follow the same way ($(2,2)$ by Pythagoras, $(1,3)$ and $(2,3)$ zero), so the polar basis is orthonormal, and with $\mathbf e_R\times\mathbf e_\theta$ equal to $\mathbf k$ it is right-handed. At $\theta = 0$ it reduces to $\mathbf e_R$ along $-\mathbf j$ and $\mathbf e_\theta$ along $\mathbf i$.

> [!derivation] Time derivatives of the polar unit vectors
> **Law:** partial derivatives with respect to $\theta$; chain rule through $\theta(t)$; check with an angular velocity about $\mathbf k$
> **Source:** Notes.pdf, Eq. 2.25; Notes.pdf, Eq. 2.26; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.32
>
> The derivatives are taken in $S_0$, where $\mathbf i$, $\mathbf j$, $\mathbf k$ are constant; the polar vectors depend on time only through $\theta(t)$.
>
> $$\begin{aligned}
> \frac{\partial\mathbf e_R}{\partial\theta} &= \cos\theta\,\mathbf i + \sin\theta\,\mathbf j \quad &\text{(derivatives of $\sin\theta$ and $-\cos\theta$)} \\
> &= \mathbf e_\theta \quad &\text{(box above)} \\
> \frac{\partial\mathbf e_\theta}{\partial\theta} &= -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j \quad &\text{(derivatives of $\cos\theta$ and $\sin\theta$)} \\
> &= -\mathbf e_R \quad &\text{(box above)} \\
> \frac{d\mathbf e_R}{dt} &= \frac{\partial\mathbf e_R}{\partial\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(first result)} \\
> \frac{d\mathbf e_\theta}{dt} &= \frac{\partial\mathbf e_\theta}{\partial\theta}\,\dot\theta \quad &\text{(chain rule)} \\
> &= -\dot\theta\,\mathbf e_R \quad &\text{(second result)} \\
> \dot\theta\,\mathbf k\times\mathbf e_R &= \dot\theta\left(\sin\theta\,\mathbf k\times\mathbf i - \cos\theta\,\mathbf k\times\mathbf j\right) \quad &\text{(distribute, Eq. 1.32)} \\
> &= \dot\theta\left(\sin\theta\,\mathbf j + \cos\theta\,\mathbf i\right) \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= \dot\theta\,\mathbf e_\theta \quad &\text{(the same as the derivative of $\mathbf e_R$: Eq. 1.62 with the angular velocity $\dot\theta\,\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf e_R}{dt} = \dot\theta\,\mathbf e_\theta,\qquad \frac{d\mathbf e_\theta}{dt} = -\dot\theta\,\mathbf e_R}$$
>
> **Units:** $\mathrm{rad/s}$ in every term
> **Meaning:** the basis turns with the rod about $\mathbf k$ at the rate $\dot\theta$, the rate of $\theta_{\mathrm{pol}}$ too, so these are Eqs. 2.25 and 2.26 unchanged by the shift of the origin of the angle.

> [!derivation] Position, velocity and acceleration of the bob
> **Law:** position along the rod; definition of velocity and acceleration; product rule; the rod length is constant
> **Source:** Notes.pdf, Eq. 4.33; Notes.pdf, Eq. 4.34; Notes.pdf, Eq. 4.35; Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 1.64
>
> $$\begin{aligned}
> \mathbf r_0^P &= \ell\,\mathbf e_R \quad &\text{(the bob is at distance $\ell$ from $O$ along the rod, Eq. 4.33)} \\
> \mathbf v_0^P &= \left.\frac{d}{dt}\left(\ell\,\mathbf e_R\right)\right|_0 \quad &\text{(Eq. 2.3)} \\
> &= \dot\ell\,\mathbf e_R + \ell\,\frac{d\mathbf e_R}{dt} \quad &\text{(product rule, Eq. 1.64)} \\
> &= \ell\,\frac{d\mathbf e_R}{dt} \quad &\text{(rigid rod: $\dot\ell = 0$)} \\
> &= \ell\dot\theta\,\mathbf e_\theta \quad &\text{(box above; Eq. 4.34)} \\
> \mathbf a_0^P &= \left.\frac{d}{dt}\left(\ell\dot\theta\,\mathbf e_\theta\right)\right|_0 \quad &\text{(Eq. 2.4)} \\
> &= \ell\ddot\theta\,\mathbf e_\theta + \ell\dot\theta\,\frac{d\mathbf e_\theta}{dt} \quad &\text{(product rule; $\ell$ constant)} \\
> &= \ell\ddot\theta\,\mathbf e_\theta - \ell\dot\theta^2\,\mathbf e_R \quad &\text{(box above)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = \ell\,\mathbf e_R,\qquad \mathbf v_0^P = \ell\dot\theta\,\mathbf e_\theta,\qquad \mathbf a_0^P = -\ell\dot\theta^2\,\mathbf e_R + \ell\ddot\theta\,\mathbf e_\theta}$$
>
> **Units:** $\mathrm m$; $\mathrm m\cdot\mathrm{rad/s} = \mathrm{m/s}$; $\mathrm m\cdot\mathrm{rad^2/s^2}$ and $\mathrm m\cdot\mathrm{rad/s^2}$, both $\mathrm{m/s^2}$
> **Meaning:** the velocity is perpendicular to the rod, tangent to the circle of radius $\ell$; the acceleration has a part along the rod pointing to $O$, which turns the velocity, and a part along $\mathbf e_\theta$, which changes the speed.

### Forces and equations of motion

The bob is subject to two forces (Notes.pdf, Sec. 4.7): the constant weight, pointing downwards, and the tension of the rod, a reaction force (Topic 3) whose magnitude $F_t$ is unknown until the problem is solved but whose direction is along the rod. The rod is light and rigid, so the force it exerts on the bob acts along $\mathbf e_R$; with $F_t$ positive it pulls the bob towards $O$.

![[attachments/EM-T/t2-pendulum-fbd.svg]]

> [!derivation] The forces in the polar basis
> **Law:** change of basis with the transpose of the rotation matrix; tension along the rod
> **Source:** Notes.pdf, Eq. 4.36; Notes.pdf, Sec. 4.7; Notes.pdf, Eq. 1.12; Notes.pdf, Eq. 1.14
>
> $$\begin{aligned}
> \mathbf F_g &= -m\,g\,\mathbf j \quad &\text{(weight, downwards)} \\
> [\mathbf F_g]_{\mathrm{pol}} &= [{}_0R_{\mathrm{pol}}]^T\,[\mathbf F_g]_0 \quad &\text{(inverse change of basis: the transpose, Eqs. 1.12 and 1.14)} \\
> &= \begin{pmatrix} \sin\theta\cdot 0 + (-\cos\theta)(-m g) + 0\cdot 0 \cr \cos\theta\cdot 0 + \sin\theta\,(-m g) + 0\cdot 0 \cr 0\cdot 0 + 0\cdot(-m g) + 1\cdot 0 \end{pmatrix} \quad &\text{(rows of the transpose, the columns of the matrix, times the column $(0, -mg, 0)$)} \\
> &= \begin{pmatrix} m g\cos\theta \cr -m g\sin\theta \cr 0 \end{pmatrix} \quad &\text{(arithmetic)} \\
> \mathbf F_t &= -F_t\,\mathbf e_R \quad &\text{(tension along the rod, towards $O$ for $F_t > 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_g = m g\cos\theta\,\mathbf e_R - m g\sin\theta\,\mathbf e_\theta,\qquad \mathbf F_t = -F_t\,\mathbf e_R}$$
>
> **Units:** $\mathrm N$
> **Meaning:** the component of the weight along the rod, $m g\cos\theta$, points away from $O$ while the bob is below the pivot; the component along $\mathbf e_\theta$, $-m g\sin\theta$, points back towards $\theta = 0$ whenever $\lvert\theta\rvert < \pi$: it is a restoring force that tries to bring the pendulum back to its equilibrium position (Notes.pdf, Sec. 4.7).

> [!derivation] Equations of motion of the pendulum
> **Law:** Newton's second law projected on $\mathbf e_R$ and $\mathbf e_\theta$
> **Source:** Notes.pdf, Eq. 4.37; Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.35; Notes.pdf, Eq. 4.36
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F_g + \mathbf F_t \quad &\text{(second law, Eq. 4.4)} \\
> m\left(-\ell\dot\theta^2\,\mathbf e_R + \ell\ddot\theta\,\mathbf e_\theta\right) &= \left(m g\cos\theta - F_t\right)\mathbf e_R - m g\sin\theta\,\mathbf e_\theta \quad &\text{(Eqs. 4.35 and 4.36; group by unit vector)} \\
> \mathbf e_R:\quad -m\ell\dot\theta^2 &= m g\cos\theta - F_t \quad &\text{(dot-multiply by $\mathbf e_R$)} \\
> \mathbf e_\theta:\quad m\ell\ddot\theta &= -m g\sin\theta \quad &\text{(dot-multiply by $\mathbf e_\theta$)} \\
> \ddot\theta + \frac{g}{\ell}\sin\theta &= 0 \quad &\text{(divide by $m\ell$ and move the right side over)} \\
> F_t &= m\ell\dot\theta^2 + m g\cos\theta \quad &\text{(solve the $\mathbf e_R$ equation for the tension)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \frac{g}{\ell}\sin\theta = 0,\qquad F_t = m\ell\dot\theta^2 + m g\cos\theta}$$
>
> **Units:** $\mathrm{rad/s^2}$ in the equation of motion ($g/\ell$ in $\mathrm{s^{-2}}$); $\mathrm N$ in the tension ($\mathrm{kg\cdot m\cdot s^{-2}}$ for both terms)
> **Meaning:** the $\mathbf e_\theta$ equation contains only the unknown $\theta$ and is the equation of motion; the mass drops out of it. The $\mathbf e_R$ equation then gives the tension: at the lowest point it is the weight plus the force $m\ell\dot\theta^2$ needed to turn the velocity.

> [!warning] Erratum to Notes.pdf, Eq. 4.37: sign of the tension
> Eq. 4.37 is printed with $+F_t$ on its right side, but the notes define the tension as $-F_t\,\mathbf e_R$, whose component along $\mathbf e_R$ is $-F_t$, so the projection on $\mathbf e_R$ is the one of the box above, with $-F_t$ on the right. Check: for the pendulum hanging at rest at its lowest point the printed equation would give a tension equal to $-mg$, a rod pushing the bob downwards, while the corrected one gives $mg$, the rod holding the weight. The error does not affect Eq. 4.38 or anything else in the section.

### Energy

> [!derivation] First integral of the equation of motion
> **Law:** multiplication by $\dot\theta$; chain rule; integration in time with Barrow's rule
> **Source:** Notes.pdf, Eq. 4.39; Notes.pdf, Eq. 4.38
>
> $$\begin{aligned}
> \dot\theta\,\ddot\theta + \frac{g}{\ell}\sin\theta\,\dot\theta &= 0 \quad &\text{(multiply Eq. 4.38 by $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\,\dot\theta^2\right) &= \dot\theta\,\ddot\theta \quad &\text{(chain rule: derivative of the square times the derivative of $\dot\theta$)} \\
> \frac{d}{dt}\left(\frac{g}{\ell}\left(1 - \cos\theta\right)\right) &= \frac{g}{\ell}\sin\theta\,\dot\theta \quad &\text{(chain rule: derivative of $-\cos\theta$ times $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\,\dot\theta^2 + \frac{g}{\ell}\left(1 - \cos\theta\right)\right) &= 0 \quad &\text{(the first row is the sum of the two derivatives)} \\
> \left[\tfrac12\,\dot\theta^2 + \frac{g}{\ell}\left(1 - \cos\theta\right)\right]_{0}^{t} &= 0 \quad &\text{(integrate from $0$ to $t$; Barrow)} \\
> \tfrac12\,\dot\theta^2 + \frac{g}{\ell}\left(1 - \cos\theta\right) &= C \quad &\text{($C$: the value of the bracket at $t = 0$)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12\,\dot\theta^2 + \frac{g}{\ell}\left(1 - \cos\theta\right) = C}$$
>
> **Units:** $\mathrm{rad^2/s^2}$, that is $\mathrm{s^{-2}}$, in every term and in $C$
> **Meaning:** a first integral: a combination of $\theta$ and $\dot\theta$ that stays constant during the motion. The mass does not appear in it (Notes.pdf, Sec. 4.7).

The same result follows directly from energy conservation (Notes.pdf, Sec. 4.7): the tension exerts no work on the bob, being always perpendicular to its velocity, and the weight is uniform and derives from a potential. From here on the indices $P$ and $0$ of the potential energy are dropped where no confusion arises, since there is one particle and one frame.

> [!derivation] Potential, kinetic and mechanical energy of the pendulum
> **Law:** potential energy of the weight (Section 4); zero power of a force perpendicular to the velocity; kinetic energy
> **Source:** Notes.pdf, Eq. 4.40; Notes.pdf, Eq. 4.41; Notes.pdf, Eq. 4.42; Notes.pdf, Eq. 4.10; [Lecture 2, Slide 16]; [Lecture 2, Slide 19]
>
> $$\begin{aligned}
> \mathbf F_t\cdot\mathbf v_0^P &= -F_t\,\mathbf e_R\cdot\ell\dot\theta\,\mathbf e_\theta \quad &\text{(tension and Eq. 4.34)} \\
> &= 0 \quad &\text{($\mathbf e_R\cdot\mathbf e_\theta = 0$: the tension does no work)} \\
> V_0 &= m g\,y + \mathrm{const} \quad &\text{(potential energy of the weight, Section 4, with any reference level)} \\
> &= m g\,(y + \ell) \quad &\text{(zero at the lowest point, $y = -\ell$)} \\
> &= m g\ell\left(1 - \cos\theta\right) \quad &\text{(previous box: $y = -\ell\cos\theta$; Eq. 4.40)} \\
> T_0 &= \tfrac12\,m\,\ell\dot\theta\,\mathbf e_\theta\cdot\ell\dot\theta\,\mathbf e_\theta \quad &\text{(Eq. 4.2 with Eq. 4.34)} \\
> &= \tfrac12\,m\left(\ell\dot\theta\right)^2 \quad &\text{($\mathbf e_\theta\cdot\mathbf e_\theta = 1$; Eq. 4.41)} \\
> E_0 &= \tfrac12\,m\left(\ell\dot\theta\right)^2 + m g\ell\left(1 - \cos\theta\right) \quad &\text{(the only working force is conservative: $E_0$ is constant, Eq. 4.42)} \\
> &= m\ell^2\left(\tfrac12\,\dot\theta^2 + \frac{g}{\ell}\left(1 - \cos\theta\right)\right) \quad &\text{(take out the factor $m\ell^2$)} \\
> &= m\ell^2\,C \quad &\text{(first integral, Eq. 4.39)}
> \end{aligned}$$
>
> $$\boxed{V_0(\theta) = m g\ell\left(1 - \cos\theta\right),\qquad T_0 = \tfrac12\,m\left(\ell\dot\theta\right)^2,\qquad T_0 + V_0 = E_0 = m\ell^2\,C}$$
>
> **Units:** $\mathrm J$; $\mathrm{kg\,m^2}$ times $C$ in $\mathrm{s^{-2}}$ is also $\mathrm J$
> **Meaning:** the conservation of energy is Eq. 4.39 multiplied by the constant factor $m\ell^2$ (Notes.pdf, Sec. 4.7). In general the energy equation, when available, can replace one of the scalar equations of motion, of which it is a combination; it is especially useful in problems with a single degree of freedom.

![[attachments/EM-T/t2-pendulum-potential.svg]]

> [!derivation] Equilibria of the pendulum and their stability
> **Law:** equation of motion written with the potential; critical points and second derivative of the potential (Section 6)
> **Source:** Notes.pdf, Sec. 4.6; Notes.pdf, Sec. 4.7; Notes.pdf, Eq. 4.40; Notes.pdf Fig. 4.4; [Lecture 2, Slide 22]
>
> $n$ is any integer.
>
> $$\begin{aligned}
> \frac{dV_0}{d\theta} &= m g\ell\sin\theta \quad &\text{(derivative of Eq. 4.40)} \\
> m\ell^2\,\ddot\theta &= -\frac{dV_0}{d\theta} \quad &\text{(Eq. 4.38 times $m\ell^2$: the form of Eq. 4.21 with $\theta$ for $x$ and $m\ell^2$ for $m$)} \\
> \sin\theta^*_{\mathrm{eq}} &= 0 \quad &\text{(equilibrium: critical point of $V_0$)} \\
> \theta^*_{\mathrm{eq}} &= n\pi \quad &\text{(zeros of the sine)} \\
> \frac{d^2V_0}{d\theta^2} &= m g\ell\cos\theta \quad &\text{(second derivative)} \\
> \frac{d^2V_0}{d\theta^2}(2n\pi) &= m g\ell > 0 \quad &\text{(hanging down: a minimum)} \\
> \frac{d^2V_0}{d\theta^2}(\pi + 2n\pi) &= -m g\ell < 0 \quad &\text{(upside down: a maximum)} \\
> m\ell^2 p^2 + m g\ell\cos\theta^*_{\mathrm{eq}} &= 0 \quad &\text{(characteristic equation of Section 6 with $m\ell^2$ for $m$)} \\
> p &= \pm\,i\sqrt{g/\ell} \quad &\text{(at $\theta^*_{\mathrm{eq}} = 2n\pi$: $\cos\theta^*_{\mathrm{eq}} = 1$, divide by $m\ell^2$)} \\
> p &= \pm\sqrt{g/\ell} \quad &\text{(at $\theta^*_{\mathrm{eq}} = \pi + 2n\pi$: $\cos\theta^*_{\mathrm{eq}} = -1$)} \\
> V_0(\pi + 2n\pi) &= m g\ell\left(1 - (-1)\right) \quad &\text{(Eq. 4.40 at the maxima)} \\
> &= 2\,m g\ell \quad &\text{(arithmetic)}
> \end{aligned}$$
>
> $$\boxed{\theta^*_{\mathrm{eq}} = 2n\pi \ \text{stable (minima, } V_0 = 0\text{)},\qquad \theta^*_{\mathrm{eq}} = \pi + 2n\pi \ \text{unstable (maxima, } V_0 = 2\,m g\ell\text{)}}$$
>
> **Units:** $\mathrm{J/rad}$ and $\mathrm{J/rad^2}$ for the derivatives of $V_0$; $p$ in $\mathrm{s^{-1}}$
> **Meaning:** the minima and maxima of Fig. 4.4 (Notes.pdf, Sec. 4.7): the hanging pendulum oscillates after a small push, and the inverted one falls away at an exponential rate. By the boxes of Section 6, every small perturbation of the inverted pendulum except a finely tuned one grows.

### Classes of motion

Let the bob start at its equilibrium position, the lowest point, with the speed $v_{0,0}^P$ towards the right, and ask which motions are possible for each value of that speed (Notes.pdf, Sec. 4.7). Since the potential is zero there, the mechanical energy is the initial kinetic energy.

> [!derivation] Oscillations: the turning points
> **Law:** conservation of mechanical energy; the kinetic energy vanishes at a turning point
> **Source:** Notes.pdf, Eq. 4.43; Notes.pdf, Eq. 4.42; Notes.pdf, Eq. 4.40
>
> $$\begin{aligned}
> E_0 &= \tfrac12\,m\left(v_{0,0}^P\right)^2 + V_0(0) \quad &\text{(initial state: speed $v_{0,0}^P$ at $\theta = 0$)} \\
> &= \tfrac12\,m\left(v_{0,0}^P\right)^2 \quad &\text{($V_0(0) = m g\ell(1 - 1) = 0$)} \\
> V_0(\theta^*) &= E_0 \quad &\text{(turning point: $T_0 = 0$, which needs $E_0 < 2\,m g\ell$)} \\
> m g\ell\left(1 - \cos\theta^*\right) &= \tfrac12\,m\left(v_{0,0}^P\right)^2 \quad &\text{(Eq. 4.40 and the second row)} \\
> 1 - \cos\theta^* &= \frac{\left(v_{0,0}^P\right)^2}{2 g\ell} \quad &\text{(divide by $m g\ell$)} \\
> \cos\theta^* &= 1 - \frac{\left(v_{0,0}^P\right)^2}{2 g\ell} \quad &\text{(rearrange)}
> \end{aligned}$$
>
> $$\boxed{\cos\theta^* = 1 - \frac{\left(v_{0,0}^P\right)^2}{2 g\ell}}$$
>
> **Units:** $(\mathrm{m/s})^2/(\mathrm{m/s^2}\cdot\mathrm m)$, dimensionless
> **Meaning:** if $E_0$ is below $2\,m g\ell$ (the level $E_{0,1}$ of Fig. 4.4) the motion is confined between the two angles $\pm\theta^*$, the turning points where the kinetic energy vanishes and the bob stops for an instant before turning back: an oscillation of amplitude $\theta^*$. The right side lies between $-1$ and $1$ exactly when the starting speed squared is below $4 g\ell$, which is the same condition, $E_0$ below $2\,m g\ell$.

> [!derivation] Period of the oscillations
> **Law:** energy equation solved for the rate; change of the integration variable from time to angle; symmetry of the two halves of the cycle
> **Source:** Notes.pdf, Eq. 4.44; Notes.pdf, Eq. 4.42
>
> In the half cycle from $-\theta^*$ to $\theta^*$, from the instant $-t^*$ to $t^*$, the rate $\dot\theta$ is positive; in the other half it is negative.
>
> $$\begin{aligned}
> \tfrac12\,m\ell^2\dot\theta^2 &= E_0 - V_0(\theta) \quad &\text{(Eq. 4.42 with $T_0 = \tfrac12\,m\ell^2\dot\theta^2$)} \\
> \left\lvert\frac{d\theta}{dt}\right\rvert &= \sqrt{\frac{2E_0 - 2V_0(\theta)}{m\ell^2}} \quad &\text{(solve for the magnitude of the rate)} \\
> \tau &= 2\int_{-t^*}^{t^*}dt \quad &\text{(the return half takes the same time: $\lvert\dot\theta\rvert$ depends only on $\theta$)} \\
> &= 2\int_{-\theta^*}^{\theta^*}\frac{d\theta}{d\theta/dt} \quad &\text{(change of variable $t \to \theta$: differential $d\theta = \dot\theta\,dt$, limits $-\theta^*$ and $\theta^*$)} \\
> &= 2\int_{-\theta^*}^{\theta^*}\sqrt{\frac{m\ell^2}{2E_0 - 2V_0(\theta)}}\,d\theta \quad &\text{(second row, with $\dot\theta > 0$ in this half)}
> \end{aligned}$$
>
> $$\boxed{\tau = 2\int_{-t^*}^{t^*}dt = 2\int_{-\theta^*}^{\theta^*}\sqrt{\frac{m\ell^2}{2E_0 - 2V_0(\theta)}}\,d\theta}$$
>
> **Units:** $\sqrt{\mathrm{kg\,m^2}/\mathrm J} = \mathrm s$ for the integrand per radian, so $\tau$ is in $\mathrm s$
> **Meaning:** the period depends on the amplitude through $E_0$. The integrand grows without bound at the turning points, where the bob stops, but the integral is finite (the box on small oscillations below evaluates it in that limit).

> [!derivation] Rotations: energy above the maxima
> **Law:** conservation of mechanical energy; the potential never exceeds its maximum
> **Source:** Notes.pdf, Eq. 4.45; Notes.pdf, Eq. 4.40; Notes.pdf, Eq. 4.42
>
> $$\begin{aligned}
> V_0(\theta) &\leq 2\,m g\ell \quad &\text{($1 - \cos\theta \leq 2$ for every $\theta$)} \\
> T_0 &= E_0 - V_0(\theta) \quad &\text{(Eq. 4.42)} \\
> &\geq E_0 - 2\,m g\ell > 0 \quad &\text{(first row, with $E_0 > 2\,m g\ell$)} \\
> T_{0,1} &= \tfrac12\,m\left(v_{0,1}^P\right)^2 \quad &\text{(at the upward vertical, $\theta = \pi$, where the speed is $v_{0,1}^P$)} \\
> &= E_0 - 2\,m g\ell \quad &\text{(Eq. 4.42 with $V_0(\pi) = 2\,m g\ell$; Eq. 4.45)}
> \end{aligned}$$
>
> $$\boxed{T_{0,1} = \tfrac12\,m\left(v_{0,1}^P\right)^2 = E_0 - 2\,m g\ell > 0}$$
>
> **Units:** $\mathrm J$
> **Meaning:** if the bob is pushed so hard that $E_0$ exceeds $2\,m g\ell$ (the level $E_{0,2}$ of Fig. 4.4) the kinetic energy never vanishes, the rate keeps its sign, and the bob passes the upward vertical with a nonzero speed: the motion is a continuous rotation rather than an oscillation (Notes.pdf, Sec. 4.7).

### Small oscillations

If the mechanical energy is small compared with $2\,m g\ell$, the oscillations are small and the angle stays much smaller than one radian; the equation of motion can then be linearised, giving an approximate but simpler model of the pendulum (Notes.pdf, Sec. 4.7).

> [!derivation] Linearised pendulum and its potential
> **Law:** Taylor expansions of the sine and the cosine about zero, kept to the lowest order
> **Source:** Notes.pdf, Eq. 4.46; Notes.pdf, Eq. 4.47; Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.40; Notes.pdf Fig. 4.4
>
> $$\begin{aligned}
> \sin\theta &= \theta - \frac{\theta^3}{6} + O(\theta^5) \quad &\text{(Taylor series of the sine)} \\
> \sin\theta &\approx \theta \quad &\text{(keep the first-order term, $\theta$ much smaller than one)} \\
> \ddot\theta + \frac{g}{\ell}\,\theta &= 0 \quad &\text{(substitute in Eq. 4.38; Eq. 4.46)} \\
> 1 - \cos\theta &= \frac{\theta^2}{2} - \frac{\theta^4}{24} + O(\theta^6) \quad &\text{(Taylor series of the cosine)} \\
> \tilde V_0(\theta) &= m g\ell\,\frac{\theta^2}{2} \quad &\text{(keep the lowest-order term in Eq. 4.40; Eq. 4.47)} \\
> -\frac{d\tilde V_0}{d\theta} &= -m g\ell\,\theta \quad &\text{(derivative of $\tilde V_0$)} \\
> &= m\ell^2\,\ddot\theta \quad &\text{(the linearised equation times $m\ell^2$: the same model)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta + \frac{g}{\ell}\,\theta = 0,\qquad \tilde V_0(\theta) = m g\ell\,\frac{\theta^2}{2}}$$
>
> **Units:** $\mathrm{s^{-2}}$ in the equation; $\mathrm J$ for the potential
> **Meaning:** the equation of a harmonic oscillator (Chapter 5); its potential is the parabola drawn dashed in Fig. 4.4, which matches the full potential near the bottom and departs from it as the amplitude grows. At an amplitude of $10^\circ$, about $0.1745\ \mathrm{rad}$, the sine is $0.1736$, so replacing it by the angle overestimates the restoring force by about $0.5\ \%$.

> [!derivation] Period of the small oscillations
> **Law:** period integral with the linearised potential; trigonometric substitution; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44; Notes.pdf, Eq. 4.47
>
> At the turning point the energy is all potential, so with the linearised potential the energy is $m g\ell$ times half the amplitude squared.
>
> $$\begin{aligned}
> E_0 &= m g\ell\,\frac{\theta^{*2}}{2} \quad &\text{(Eq. 4.47 at $\theta^*$, where $T_0 = 0$)} \\
> 2E_0 - 2\tilde V_0(\theta) &= m g\ell\left(\theta^{*2} - \theta^2\right) \quad &\text{(subtract twice Eq. 4.47)} \\
> \sqrt{\frac{m\ell^2}{2E_0 - 2\tilde V_0}} &= \sqrt{\frac{\ell}{g}}\,\frac{1}{\sqrt{\theta^{*2} - \theta^2}} \quad &\text{(cancel $m\ell$)} \\
> \tau &= 2\sqrt{\frac{\ell}{g}}\int_{-\theta^*}^{\theta^*}\frac{d\theta}{\sqrt{\theta^{*2} - \theta^2}} \quad &\text{(Eq. 4.44)} \\
> \theta &= \theta^*\sin u,\qquad d\theta = \theta^*\cos u\,du \quad &\text{(substitution and its differential)} \\
> \sqrt{\theta^{*2} - \theta^{*2}\sin^2 u} &= \theta^*\cos u \quad &\text{(Pythagoras; $\cos u \geq 0$ for $u$ between $-\pi/2$ and $\pi/2$)} \\
> \tau &= 2\sqrt{\frac{\ell}{g}}\int_{-\pi/2}^{\pi/2}\frac{\theta^*\cos u}{\theta^*\cos u}\,du \quad &\text{(limits: $\theta = -\theta^*$ gives $u = -\pi/2$, $\theta = \theta^*$ gives $u = \pi/2$)} \\
> &= 2\sqrt{\frac{\ell}{g}}\,\big[u\big]_{-\pi/2}^{\pi/2} \quad &\text{(the integrand is one; antiderivative $u$)} \\
> &= 2\sqrt{\frac{\ell}{g}}\left(\frac{\pi}{2} - \left(-\frac{\pi}{2}\right)\right) \quad &\text{(Barrow)} \\
> &= 2\pi\sqrt{\frac{\ell}{g}} \quad &\text{(arithmetic)}
> \end{aligned}$$
>
> $$\boxed{\tau = 2\pi\sqrt{\frac{\ell}{g}}}$$
>
> **Units:** $\sqrt{\mathrm m/(\mathrm{m/s^2})} = \mathrm s$
> **Meaning:** for small oscillations the period does not depend on the amplitude or on the mass; it is $2\pi$ over the imaginary part $\sqrt{g/\ell}$ of the characteristic roots found at $\theta = 0$, as the harmonic oscillator of Chapter 5 will confirm. For a rod of $1\ \mathrm m$ and $g = 9.81\ \mathrm{m/s^2}$ it is about $2.01\ \mathrm s$.

## 8. The harmonic oscillator: undamped motion

From the classical spring-mass-damper system to the linearised aeroelastic oscillations of an airfoil or the vibrations of an aircraft structure, many mechanical systems have an equation of motion that reduces to a linear second-order equation with constant coefficients in a generalised coordinate $\xi$, with two constants $\gamma$ and $\omega_0$ and a forcing term $\tilde f(t)$: this is the most general expression of the equation of a harmonic oscillator (Notes.pdf, Ch. 5), and any physical system governed by such an equation is termed a harmonic oscillator ([Lecture 6, Slide 5]). Since a single particle is studied in the single frame $S_0$, the indices $P$ and $0$ of the previous sections are dropped for many quantities: the displacement is $x$, the potential energy $V$, the mechanical energy $E$ (Notes.pdf, Ch. 5). The sections that follow take Chapter 5 of the notes in its order (Eqs. 5.1 to 5.47) with the slides of Lecture 6 at the places where they treat the same material, and close with the linearisation about an equilibrium of [Lecture 6, Slide 15] and an extended example.

> [!example] The spring-mass-damper system ([Lecture 6, Slide 5]; Notes.pdf, Sec. 5.1)
> A point particle $P$ of mass $m$ moves along the horizontal line $Ox$ of the inertial frame $S_0$, on a smooth support. It is attached to the wall at $O$ by a linear spring of stiffness $k$ and zero natural length and by a viscous damper of damping constant $\lambda$, and an external force $F_x(t)$ may be applied to it along $Ox$. Its weight and the reaction of the support are vertical. The undamped oscillator of this section is the case of no damper and no applied force; the damper is added in Section 10 and the applied force in Section 11.
>
> | Data | Value |
> | :--- | :--- |
> | frame | $S_0$, inertial; $\mathbf i$ along the line of motion, away from the wall; $\mathbf j$ vertical upwards |
> | particle | mass $m$, position $x$ along $Ox$ (the length of the spring) |
> | spring | stiffness $k > 0$, zero natural length |
> | damper | damping constant $\lambda \geq 0$ |
> | applied force | $F_x(t)$ along $\mathbf i$ |

![[attachments/EM-T/t2-spring-mass.svg]]

> [!derivation] Equation of motion of the spring-mass-damper
> **Law:** Newton's second law projected on the line of motion; linear spring and viscous damper
> **Source:** [Lecture 6, Slide 5]; Notes.pdf, Eq. 5.1; Notes.pdf, Eq. 5.19; Notes.pdf, Eq. 5.20; Notes.pdf, Eq. 5.32; Notes.pdf, Eq. 5.23; Notes.pdf, Eq. 4.4
>
> The spring has zero natural length, so its elongation is the displacement $x$ itself; the damper opposes the velocity. $\mathbf N_s$ is the reaction of the smooth support, vertical.
>
> $$\begin{aligned}
> \mathbf r_0^P &= x\,\mathbf i \quad &\text{(the particle moves on $Ox$)} \\
> \mathbf a_0^P &= \ddot x\,\mathbf i \quad &\text{(differentiate twice in $S_0$, where $\mathbf i$ is constant, Eq. 2.4)} \\
> \mathbf F_k &= -k\,x\,\mathbf i \quad &\text{(linear spring: proportional to the elongation, towards the wall; Eq. 5.1)} \\
> \mathbf F_\lambda &= -\lambda\,\dot x\,\mathbf i \quad &\text{(viscous damper: proportional and opposite to the velocity)} \\
> m\ddot x\,\mathbf i &= -k\,x\,\mathbf i - \lambda\dot x\,\mathbf i + F_x(t)\,\mathbf i + \left(\mathbf N_s - m g\,\mathbf j\right) \quad &\text{(second law, Eq. 4.4, with every force)} \\
> \mathbf N_s &= m g\,\mathbf j \quad &\text{(component along $\mathbf j$: the left side has none)} \\
> m\ddot x &= -k\,x - \lambda\dot x + F_x(t) \quad &\text{(component along $\mathbf i$)} \\
> m\ddot x + \lambda\dot x + k\,x &= F_x(t) \quad &\text{(move the spring and damper terms to the left; Eq. 5.32)} \\
> \ddot x + \frac{\lambda}{m}\,\dot x + \frac{k}{m}\,x &= \frac{F_x(t)}{m} \quad &\text{(divide by $m$)} \\
> \ddot x + 2\gamma\,\dot x + \omega_0^2\,x &= \frac{F_x(t)}{m} \quad &\text{(name the coefficients: $\gamma = \lambda/(2m)$, $\omega_0 = \sqrt{k/m}$, Eq. 5.23)} \\
> m\ddot x + k\,x &= 0 \quad &\text{(no damper and no applied force: $\lambda = 0$, $F_x = 0$; Eq. 5.4)}
> \end{aligned}$$
>
> $$\boxed{m\ddot x + \lambda\dot x + k\,x = F_x(t) \ \Longleftrightarrow\ \ddot x + 2\gamma\,\dot x + \omega_0^2\,x = \frac{F_x(t)}{m},\qquad \gamma = \frac{\lambda}{2m},\ \ \omega_0 = \sqrt{\frac{k}{m}}}$$
>
> **Units:** every term of the first form in $\mathrm N$ ($\mathrm{kg\,m/s^2}$, $\mathrm{(N\,s/m)(m/s)}$, $\mathrm{(N/m)\,m}$); $\gamma$ in $\mathrm{(N\,s/m)/kg} = \mathrm{s^{-1}}$; $\omega_0$ in $\sqrt{\mathrm{(N/m)/kg}} = \mathrm{s^{-1}}$; every term of the second form in $\mathrm{m/s^2}$
> **Meaning:** the spring and the damper give forces linear in $x$ and $\dot x$, so the equation of motion is linear with constant coefficients: it is the general equation of a harmonic oscillator with $x$ as the coordinate and $F_x/m$ as the forcing term ([Lecture 6, Slide 5]). The weight is carried by the support and does not enter the motion. The last row, Eq. 5.4, is the undamped free oscillator studied in this section.

> [!derivation] Potential energy of the spring and the turning points
> **Law:** potential energy of a one-dimensional force depending only on the position; conservation of mechanical energy; a turning point has zero velocity
> **Source:** Notes.pdf, Eq. 5.1; Notes.pdf, Eq. 5.2; Notes.pdf, Eq. 5.3; Notes.pdf, Eq. 4.15; Notes.pdf, Eq. 4.26; [Lecture 6, Slide 7]
>
> The reference position, where the potential is zero, is the relaxed spring, $x$ equal to zero; $x'$ is the integration variable.
>
> $$\begin{aligned}
> V(x) &= -\int_0^x F(x')\,dx' \quad &\text{(one-dimensional potential, Eq. 4.15)} \\
> &= -\int_0^x\left(-k\,x'\right)dx' \quad &\text{(spring force, Eq. 5.1)} \\
> &= k\int_0^x x'\,dx' \quad &\text{(take the constant $-k$ out of the integral)} \\
> &= k\left[\frac{x'^2}{2}\right]_0^x \quad &\text{(antiderivative of $x'$)} \\
> &= k\left(\frac{x^2}{2} - \frac{0^2}{2}\right) \quad &\text{(Barrow)} \\
> &= \tfrac12\,k\,x^2 \quad &\text{(Eq. 5.2)} \\
> &= \tfrac12\,m\,\omega_0^2\,x^2 \quad &\text{($k = m\omega_0^2$, Eq. 5.23)} \\
> \tfrac12\,m\,\dot x^2 + \tfrac12\,k\,x^2 &= E \quad &\text{(the only working force is conservative: $E$ is constant, Eq. 4.26)} \\
> \tfrac12\,k\,x^2 &= E \quad &\text{(at a turning point $\dot x = 0$)} \\
> x &= \pm\sqrt{2E/k} \quad &\text{(multiply by $2/k$ and take the square root; Eq. 5.3)}
> \end{aligned}$$
>
> $$\boxed{V(x) = \tfrac12\,k\,x^2 = \tfrac12\,m\,\omega_0^2\,x^2,\qquad x = \pm a = \pm\sqrt{2E/k}}$$
>
> **Units:** $\mathrm{(N/m)\,m^2} = \mathrm J$ for the potential; $\sqrt{\mathrm J/(\mathrm{N/m})} = \mathrm m$ for the turning points
> **Meaning:** the potential is a parabola (Notes.pdf Fig. 5.1). With $k$ positive, every energy $E$ above zero meets it at exactly two points, the turning points $\pm a$, where the particle stops and turns back: the motion is a harmonic oscillation between them (Notes.pdf, Sec. 5.1). The constant $a$ is identified with the amplitude in the box on the energy of the oscillation below.

![[attachments/EM-T/t2-oscillator-potential.svg]]

> [!derivation] Linear homogeneous equations: superposition and the characteristic equation
> **Law:** linearity of differentiation; trial exponential solution; independence of two solutions
> **Source:** Notes.pdf, Eq. 5.5; Notes.pdf, Sec. 5.1; [Lecture 6, Slide 3]
>
> The equation is the homogeneous one, $\tilde f$ equal to zero, with constant coefficients $b_2$ (nonzero), $b_1$, $b_0$. $\xi_1$ and $\xi_2$ are two of its solutions and $D_1$, $D_2$ any two constants.
>
> $$\begin{aligned}
> b_2\ddot\xi_1 + b_1\dot\xi_1 + b_0\xi_1 &= 0,\qquad b_2\ddot\xi_2 + b_1\dot\xi_2 + b_0\xi_2 = 0 \quad &\text{(both are solutions)} \\
> \xi &= D_1\xi_1 + D_2\xi_2 \quad &\text{(a linear combination, Eq. 5.5)} \\
> \dot\xi &= D_1\dot\xi_1 + D_2\dot\xi_2 \quad &\text{(derivative of a sum; the constants come out)} \\
> \ddot\xi &= D_1\ddot\xi_1 + D_2\ddot\xi_2 \quad &\text{(differentiate again)} \\
> b_2\ddot\xi + b_1\dot\xi + b_0\xi &= D_1\left(b_2\ddot\xi_1 + b_1\dot\xi_1 + b_0\xi_1\right) + D_2\left(b_2\ddot\xi_2 + b_1\dot\xi_2 + b_0\xi_2\right) \quad &\text{(substitute and group by constant)} \\
> &= 0 \quad &\text{(first row: both brackets vanish)} \\
> \xi &= \exp(p\,t) \quad &\text{(trial solution, $p$ a constant, possibly complex)} \\
> \dot\xi &= p\exp(p\,t) \quad &\text{(chain rule: the derivative of $p\,t$ is $p$)} \\
> \ddot\xi &= p^2\exp(p\,t) \quad &\text{(chain rule again)} \\
> \left(b_2\,p^2 + b_1\,p + b_0\right)\exp(p\,t) &= 0 \quad &\text{(substitute in the homogeneous equation and take out the exponential)} \\
> b_2\,p^2 + b_1\,p + b_0 &= 0 \quad &\text{(the exponential is never zero: characteristic equation)} \\
> \frac{\exp(p_+ t)}{\exp(p_- t)} &= \exp\big((p_+ - p_-)\,t\big) \quad &\text{(two roots $p_+$, $p_-$: the quotient of the two solutions)} \\
> \xi &= D_1\exp(p_+ t) + D_2\exp(p_- t) \quad &\text{(if $p_+ \neq p_-$ the quotient is not constant: two independent solutions, combined)}
> \end{aligned}$$
>
> $$\boxed{b_2\,p^2 + b_1\,p + b_0 = 0;\qquad p_+ \neq p_-:\ \ \xi = D_1\exp(p_+ t) + D_2\exp(p_- t)}$$
>
> **Units:** $p$ in $\mathrm{s^{-1}}$, so that $p\,t$ is dimensionless; $b_2\,p^2$, $b_1\,p$ and $b_0$ have the same units, those of the coefficient $b_0$
> **Meaning:** the solutions of the homogeneous equation satisfy the superposition principle and form a two-dimensional vector space of functions: the two exponentials are a basis of it and $D_1$, $D_2$ are the components of a solution in that basis ([Lecture 6, Slide 3]). A second-order equation has exactly two arbitrary constants, so this is the general solution (Notes.pdf, Sec. 5.1); adding the initial values of $\xi$ and of its derivative gives a Cauchy problem, whose unique solution is found by computing $D_1$ and $D_2$ from them ([Lecture 6, Slide 3]). The case of a double root is treated with critical damping, in Section 10.

> [!derivation] General solution of the undamped oscillator
> **Law:** characteristic equation; direct substitution of two real trial functions; superposition
> **Source:** Notes.pdf, Eq. 5.4; Notes.pdf, Eq. 5.6; Notes.pdf, Eq. 5.7; [Lecture 6, Slide 6]
>
> $$\begin{aligned}
> m\ddot x + k\,x &= 0 \quad &\text{(Eq. 5.4)} \\
> \ddot x + \omega_0^2\,x &= 0 \quad &\text{(divide by $m$, with $\omega_0 = \sqrt{k/m}$; Eq. 5.6)} \\
> p^2 + \omega_0^2 &= 0 \quad &\text{(characteristic equation: $b_2 = 1$, $b_1 = 0$, $b_0 = \omega_0^2$)} \\
> p &= \pm\,i\,\omega_0 \quad &\text{($p^2 = -\omega_0^2$ is negative: two imaginary roots)} \\
> x &= D_1\exp(i\omega_0 t) + D_2\exp(-i\omega_0 t) \quad &\text{(general solution with two distinct roots; [Lecture 6, Slide 6])} \\
> \frac{d}{dt}\cos(\omega_0 t) &= -\omega_0\sin(\omega_0 t) \quad &\text{(chain rule)} \\
> \frac{d^2}{dt^2}\cos(\omega_0 t) &= -\omega_0^2\cos(\omega_0 t) \quad &\text{(chain rule again)} \\
> \frac{d^2}{dt^2}\cos(\omega_0 t) + \omega_0^2\cos(\omega_0 t) &= 0 \quad &\text{(substitute in Eq. 5.6: the cosine is a solution)} \\
> \frac{d}{dt}\sin(\omega_0 t) &= \omega_0\cos(\omega_0 t) \quad &\text{(chain rule)} \\
> \frac{d^2}{dt^2}\sin(\omega_0 t) &= -\omega_0^2\sin(\omega_0 t) \quad &\text{(chain rule again)} \\
> \frac{d^2}{dt^2}\sin(\omega_0 t) + \omega_0^2\sin(\omega_0 t) &= 0 \quad &\text{(substitute: the sine is a solution)} \\
> \frac{\sin(\omega_0 t)}{\cos(\omega_0 t)} &= \tan(\omega_0 t) \quad &\text{(not constant: the two solutions are independent)} \\
> x &= C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t) \quad &\text{(superposition, Eq. 5.5; Eq. 5.7)}
> \end{aligned}$$
>
> $$\boxed{\ddot x + \omega_0^2\,x = 0:\qquad p = \pm\,i\,\omega_0,\qquad x = C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t)}$$
>
> **Units:** $\omega_0$ in $\mathrm{s^{-1}}$, so $\omega_0 t$ is in radians; $C_1$, $C_2$ in $\mathrm m$
> **Meaning:** the cosine and the sine of $\omega_0 t$ are two real, independent solutions, so their combination with two arbitrary constants is the general solution (Notes.pdf, Sec. 5.1). The complex form of the fifth row and this real form describe the same solutions; the passage from one to the other is Euler's relation, in Section 9.

> [!derivation] Constants from the initial conditions
> **Law:** evaluation of the solution and of its first derivative at the initial instant
> **Source:** Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.8; Notes.pdf, Eq. 5.9; [Lecture 6, Slide 6]
>
> At $t$ equal to zero the particle is at $x_0$ with velocity $\dot x_0$.
>
> $$\begin{aligned}
> x(0) &= C_1\cos 0 + C_2\sin 0 \quad &\text{(Eq. 5.7 at $t = 0$)} \\
> &= C_1 \quad &\text{($\cos 0 = 1$, $\sin 0 = 0$)} \\
> C_1 &= x_0 \quad &\text{(first initial condition; Eq. 5.8)} \\
> \dot x &= -C_1\,\omega_0\sin(\omega_0 t) + C_2\,\omega_0\cos(\omega_0 t) \quad &\text{(differentiate Eq. 5.7; chain rule on each term)} \\
> \dot x(0) &= C_2\,\omega_0 \quad &\text{(at $t = 0$)} \\
> C_2 &= \dot x_0/\omega_0 \quad &\text{(second initial condition, divided by $\omega_0$; Eq. 5.9)}
> \end{aligned}$$
>
> $$\boxed{C_1 = x_0,\qquad C_2 = \frac{\dot x_0}{\omega_0},\qquad x = x_0\cos(\omega_0 t) + \frac{\dot x_0}{\omega_0}\sin(\omega_0 t)}$$
>
> **Units:** $\mathrm m$ for $C_1$; $\mathrm{(m/s)/s^{-1}} = \mathrm m$ for $C_2$
> **Meaning:** the cosine carries the initial displacement and the sine the initial velocity; a particle released from rest ($\dot x_0$ zero) oscillates as a pure cosine, and a particle kicked from the rest position ($x_0$ zero) as a pure sine.

> [!derivation] Amplitude and initial phase
> **Law:** cosine of a sum; equal coefficients of independent functions; right triangle of the two constants
> **Source:** Notes.pdf, Eq. 5.10; Notes.pdf, Eq. 5.11; Notes.pdf, Eq. 5.12; [Lecture 6, Slide 6]
>
> The general solution is written as one cosine of amplitude $a$, not negative, and initial phase $\phi$. In the right triangle with hypotenuse $a$ and the angle $\phi$ at its vertex, the leg $C_1$ is adjacent to $\phi$ and the leg $-C_2$ is opposite to it.
>
> $$\begin{aligned}
> a\cos(\omega_0 t + \phi) &= a\cos\phi\cos(\omega_0 t) - a\sin\phi\sin(\omega_0 t) \quad &\text{(cosine of a sum)} \\
> C_1 &= a\cos\phi \quad &\text{(equal coefficients of $\cos(\omega_0 t)$ in Eq. 5.7 and Eq. 5.10; Eq. 5.11)} \\
> C_2 &= -a\sin\phi \quad &\text{(equal coefficients of $\sin(\omega_0 t)$; Eq. 5.12)} \\
> C_1^2 + C_2^2 &= a^2\cos^2\phi + a^2\sin^2\phi \quad &\text{(square both rows and add)} \\
> &= a^2 \quad &\text{(Pythagoras)} \\
> a &= \sqrt{C_1^2 + C_2^2} \quad &\text{(positive root)} \\
> &= \sqrt{x_0^2 + \left(\dot x_0/\omega_0\right)^2} \quad &\text{(Eqs. 5.8 and 5.9)} \\
> \tan\phi &= -\frac{C_2}{C_1} \quad &\text{(divide Eq. 5.12 by Eq. 5.11, sign changed)} \\
> &= -\frac{\dot x_0}{\omega_0\,x_0} \quad &\text{(Eqs. 5.8 and 5.9)}
> \end{aligned}$$
>
> $$\boxed{x = a\cos(\omega_0 t + \phi),\qquad C_1 = a\cos\phi,\ \ C_2 = -a\sin\phi,\qquad a = \sqrt{x_0^2 + \left(\dot x_0/\omega_0\right)^2},\ \ \tan\phi = -\frac{\dot x_0}{\omega_0\,x_0}}$$
>
> **Units:** $a$ in $\mathrm m$; $\phi$ in radians; the tangent is a quotient of two lengths, dimensionless
> **Meaning:** $a$ is the amplitude and $\phi$ the initial phase of the oscillator at $t$ equal to zero (Notes.pdf, Sec. 5.1); at that instant [Lecture 6, Slide 6] reads the same relations as $x_0$ equal to $a\cos\phi$ and $\dot x_0$ equal to $-a\,\omega_0\sin\phi$. The tangent alone leaves two possible angles; the right one is fixed by the signs of the legs: $\cos\phi$ has the sign of $x_0$ and $\sin\phi$ the sign of $-\dot x_0$.

> [!derivation] Energy of the oscillation and the amplitude
> **Law:** conservation of mechanical energy evaluated on the solution
> **Source:** [Lecture 6, Slide 7]; Notes.pdf, Eq. 5.3; Notes.pdf, Eq. 5.10
>
> $$\begin{aligned}
> E &= \tfrac12\,m\,\dot x^2 + \tfrac12\,k\,x^2 \quad &\text{(kinetic plus potential energy; [Lecture 6, Slide 7])} \\
> \dot x &= -a\,\omega_0\sin(\omega_0 t + \phi) \quad &\text{(differentiate Eq. 5.10; chain rule)} \\
> E &= \tfrac12\,m\,a^2\omega_0^2\sin^2(\omega_0 t + \phi) + \tfrac12\,k\,a^2\cos^2(\omega_0 t + \phi) \quad &\text{(substitute $x$ and $\dot x$)} \\
> &= \tfrac12\,k\,a^2\sin^2(\omega_0 t + \phi) + \tfrac12\,k\,a^2\cos^2(\omega_0 t + \phi) \quad &\text{($m\,\omega_0^2 = k$)} \\
> &= \tfrac12\,k\,a^2 \quad &\text{(Pythagoras)} \\
> a &= \sqrt{2E/k} \quad &\text{(solve for $a$; the turning point of Eq. 5.3)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12\,k\,a^2,\qquad a = \sqrt{2E/k}}$$
>
> **Units:** $\mathrm{(N/m)\,m^2} = \mathrm J$
> **Meaning:** the energy is constant and splits between kinetic and potential energy as the squares of a sine and a cosine; the amplitude of Eq. 5.10 is the same constant $a$ introduced in Eq. 5.3, and the particle oscillates between $x$ equal to $-a$ and $a$ (Notes.pdf, Sec. 5.1).

> [!derivation] Period and frequency
> **Law:** energy equation solved for the speed; change of the integration variable from time to position; trigonometric substitution; Barrow's rule
> **Source:** [Lecture 6, Slide 7]; Notes.pdf, Eq. 5.13; Notes.pdf, Eq. 5.3; Notes.pdf, Eq. 4.27
>
> In the half period in which the particle goes from $-a$ to $a$ its velocity is positive; the return takes the same time, because the speed depends only on $x$. $u$ is the substitution variable.
>
> $$\begin{aligned}
> \tfrac12\,m\,\dot x^2 &= E - \tfrac12\,k\,x^2 \quad &\text{(Eq. 4.27 with the potential of the spring)} \\
> \frac{dx}{dt} &= \sqrt{\frac{2E - k\,x^2}{m}} \quad &\text{(solve for the velocity, positive in this half)} \\
> \frac{\tau}{2} &= \int_{-a}^{a}\frac{dx}{\sqrt{\left(2E - k\,x^2\right)/m}} \quad &\text{(change of variable $t \to x$: $dx = \dot x\,dt$; [Lecture 6, Slide 7])} \\
> \sqrt{\frac{2E - k\,x^2}{m}} &= \sqrt{\frac{k}{m}}\sqrt{a^2 - x^2} \quad &\text{($2E = k\,a^2$; take out the factor $k/m$)} \\
> &= \omega_0\sqrt{a^2 - x^2} \quad &\text{(Eq. 5.23)} \\
> \frac{\tau}{2} &= \frac{1}{\omega_0}\int_{-a}^{a}\frac{dx}{\sqrt{a^2 - x^2}} \quad &\text{(substitute)} \\
> x &= a\sin u,\qquad dx = a\cos u\,du \quad &\text{(substitution and its differential)} \\
> \sqrt{a^2 - a^2\sin^2 u} &= a\cos u \quad &\text{(Pythagoras; $\cos u \geq 0$ for $u$ between $-\pi/2$ and $\pi/2$)} \\
> \frac{\tau}{2} &= \frac{1}{\omega_0}\int_{-\pi/2}^{\pi/2}\frac{a\cos u}{a\cos u}\,du \quad &\text{(limits: $x = -a$ gives $u = -\pi/2$, $x = a$ gives $u = \pi/2$)} \\
> &= \frac{1}{\omega_0}\big[u\big]_{-\pi/2}^{\pi/2} \quad &\text{(the integrand is one; antiderivative $u = \arcsin(x/a)$, as on the slide)} \\
> &= \frac{1}{\omega_0}\left(\frac{\pi}{2} - \left(-\frac{\pi}{2}\right)\right) \quad &\text{(Barrow)} \\
> &= \frac{\pi}{\omega_0} \quad &\text{(arithmetic)} \\
> \tau &= \frac{2\pi}{\omega_0} \quad &\text{(multiply by two)} \\
> f &= \frac{1}{\tau} \quad &\text{(oscillations per unit time)} \\
> &= \frac{\omega_0}{2\pi} \quad &\text{(Eq. 5.13)} \\
> \cos\big(\omega_0(t + \tau) + \phi\big) &= \cos(\omega_0 t + \phi + 2\pi) \quad &\text{(check on Eq. 5.10: $\omega_0\tau = 2\pi$)} \\
> &= \cos(\omega_0 t + \phi) \quad &\text{(the cosine has period $2\pi$)}
> \end{aligned}$$
>
> $$\boxed{\tau = \frac{2\pi}{\omega_0},\qquad f = \frac{1}{\tau} = \frac{\omega_0}{2\pi}}$$
>
> **Units:** $\tau$ in $\mathrm s$ ($\mathrm{rad}/\mathrm{s^{-1}}$); $f$ in $\mathrm{s^{-1}} = \mathrm{Hz}$
> **Meaning:** the motion is periodic, and its period does not depend on the amplitude $a$ (Notes.pdf, Sec. 5.1). The frequency $f$ counts oscillations per second and must not be confused with the angular frequency $\omega_0$, in radians per second. The linearised pendulum of Section 7 (Eq. 4.46) is an undamped harmonic oscillator with $\theta$ in place of $x$ and $g/\ell$ in place of the square of $\omega_0$, and the period of this box is then the one found there from its own integral.

![[attachments/EM-T/t2-free-oscillation.svg]]

## 9. Complex representation

It is often convenient to describe periodic phenomena with complex exponentials (Notes.pdf, Sec. 5.2; [Lecture 6, Slide 4]): a complex constant holds the two real constants of a solution, derivatives of exponentials are products, and the motion appears as the turning of an arrow in the complex plane. The imaginary unit is the italic $i$; the bold $\mathbf i$ remains the unit vector of $Ox$.

> [!derivation] Euler's relation
> **Law:** derivative of a product; derivative of a complex exponential; a function with zero derivative is constant
> **Source:** Notes.pdf, Eq. 5.16; [Lecture 6, Slide 4]
>
> $\beta$ is a real variable (the notes call it $\theta$). The auxiliary function is the product of $\exp(-i\beta)$ and $\cos\beta + i\sin\beta$; for any complex constant $c$ the derivative of $\exp(c\,\beta)$ with respect to $\beta$ is $c\exp(c\,\beta)$.
>
> $$\begin{aligned}
> \frac{d}{d\beta}\Big[\exp(-i\beta)\left(\cos\beta + i\sin\beta\right)\Big] &= -i\exp(-i\beta)\left(\cos\beta + i\sin\beta\right) + \exp(-i\beta)\left(-\sin\beta + i\cos\beta\right) \quad &\text{(product rule)} \\
> &= \exp(-i\beta)\left(-i\cos\beta + \sin\beta - \sin\beta + i\cos\beta\right) \quad &\text{(expand; $-i\cdot i = 1$)} \\
> &= 0 \quad &\text{(the four terms cancel in pairs)} \\
> \exp(-i\beta)\left(\cos\beta + i\sin\beta\right) &= \exp(0)\left(\cos 0 + i\sin 0\right) \quad &\text{(constant: equal to its value at $\beta = 0$)} \\
> &= 1 \quad &\text{(arithmetic)} \\
> \exp(i\beta) &= \cos\beta + i\sin\beta \quad &\text{(multiply by $\exp(i\beta)$; Eq. 5.16)} \\
> \exp(-i\beta) &= \cos\beta - i\sin\beta \quad &\text{(replace $\beta$ by $-\beta$: the cosine is even, the sine odd)} \\
> \cos\beta &= \frac{\exp(i\beta) + \exp(-i\beta)}{2} \quad &\text{(add the two rows and halve)} \\
> \sin\beta &= \frac{\exp(i\beta) - \exp(-i\beta)}{2i} \quad &\text{(subtract them and divide by $2i$)} \\
> \Re(z) &= \frac{z + z^*}{2},\qquad \Im(z) = \frac{z - z^*}{2i} \quad &\text{(the same steps for any complex $z$ and its conjugate)}
> \end{aligned}$$
>
> $$\boxed{\exp(i\beta) = \cos\beta + i\sin\beta,\qquad \cos\beta = \frac{\exp(i\beta) + \exp(-i\beta)}{2},\qquad \sin\beta = \frac{\exp(i\beta) - \exp(-i\beta)}{2i}}$$
>
> **Units:** $\beta$ in radians; every term is dimensionless
> **Meaning:** $\exp(i\beta)$ is the point of the unit circle at the angle $\beta$ from the real axis: its real part is the cosine and its imaginary part the sine. These are the useful relations of [Lecture 6, Slide 4].

> [!derivation] Complex form of the free oscillation
> **Law:** a real solution equals its own conjugate; Euler's relation; polar form of a complex number
> **Source:** Notes.pdf, Eq. 5.14; Notes.pdf, Eq. 5.15; Notes.pdf, Eq. 5.17; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.10; [Lecture 6, Slide 6]
>
> $$\begin{aligned}
> x &= D_1\exp(i\omega_0 t) + D_2\exp(-i\omega_0 t) \quad &\text{(general solution, Section 8)} \\
> x^* &= D_1^*\exp(-i\omega_0 t) + D_2^*\exp(i\omega_0 t) \quad &\text{(conjugate: the conjugate of $\exp(i\beta)$ is $\exp(-i\beta)$ for real $\beta$)} \\
> D_2 &= D_1^* \quad &\text{($x$ real means $x^* = x$ at every $t$: equal coefficients of $\exp(-i\omega_0 t)$)} \\
> x &= \tfrac12 A\exp(i\omega_0 t) + \tfrac12 A^*\exp(-i\omega_0 t) \quad &\text{(name $A$ twice $D_1$; Eq. 5.14)} \\
> &= \tfrac12\left(z + z^*\right),\qquad z = A\exp(i\omega_0 t) \quad &\text{(the second term is the conjugate of the first)} \\
> &= \Re(z) \quad &\text{(Euler box, last row)} \\
> A &= C_1 - i\,C_2 \quad &\text{(Eq. 5.15)} \\
> z &= \left(C_1 - i\,C_2\right)\left(\cos(\omega_0 t) + i\sin(\omega_0 t)\right) \quad &\text{(Euler's relation, Eq. 5.16)} \\
> &= C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t) + i\left(C_1\sin(\omega_0 t) - C_2\cos(\omega_0 t)\right) \quad &\text{(expand; $-i\cdot i = 1$; group real and imaginary terms)} \\
> \Re(z) &= C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t) \quad &\text{(real part: Eq. 5.7 is recovered)} \\
> A &= a\exp(i\phi) \quad &\text{(polar form, Eq. 5.17)} \\
> z &= a\exp\big(i(\omega_0 t + \phi)\big) \quad &\text{(product of exponentials: the exponents add)} \\
> \Re(z) &= a\cos(\omega_0 t + \phi) \quad &\text{(Euler's relation: Eq. 5.10 is recovered)} \\
> a\cos\phi + i\,a\sin\phi &= C_1 - i\,C_2 \quad &\text{(Euler on Eq. 5.17, equal to Eq. 5.15)} \\
> C_1 &= a\cos\phi,\qquad C_2 = -a\sin\phi \quad &\text{(equal real and imaginary parts: Eqs. 5.11 and 5.12)}
> \end{aligned}$$
>
> $$\boxed{x = \tfrac12 A\exp(i\omega_0 t) + \tfrac12 A^*\exp(-i\omega_0 t) = \Re\big(A\exp(i\omega_0 t)\big),\qquad A = C_1 - i\,C_2 = a\exp(i\phi)}$$
>
> **Units:** $A$, $z$, $C_1$, $C_2$ and $a$ in $\mathrm m$; exponents dimensionless
> **Meaning:** the complex amplitude $A$ contains in itself the two independent constants of the solution, its modulus the amplitude and its argument the initial phase (Notes.pdf, Sec. 5.2). For a real solution the two coefficients of the exponentials are conjugate, half of $a\exp(i\phi)$ and half of $a\exp(-i\phi)$, as written on [Lecture 6, Slide 6].

> [!derivation] Real and imaginary parts of a complex solution
> **Law:** linearity of the equation; the coefficients $m$ and $k$ are real
> **Source:** Notes.pdf, Eq. 5.18
>
> $$\begin{aligned}
> z &= \Re(z) + i\,\Im(z) \quad &\text{(any complex solution of Eq. 5.4)} \\
> m\ddot z + k\,z &= m\,\frac{d^2\Re(z)}{dt^2} + k\,\Re(z) + i\left(m\,\frac{d^2\Im(z)}{dt^2} + k\,\Im(z)\right) \quad &\text{(differentiate term by term; group; $m$, $k$ real)} \\
> 0 &= \left(m\,\frac{d^2\Re(z)}{dt^2} + k\,\Re(z)\right) + i\left(m\,\frac{d^2\Im(z)}{dt^2} + k\,\Im(z)\right) \quad &\text{($z$ is a solution; Eq. 5.18)} \\
> m\,\frac{d^2\Re(z)}{dt^2} + k\,\Re(z) &= 0,\qquad m\,\frac{d^2\Im(z)}{dt^2} + k\,\Im(z) = 0 \quad &\text{(a complex number is zero when both its parts are, and both brackets are real)}
> \end{aligned}$$
>
> $$\boxed{m\ddot z + k\,z = 0 \ \Longrightarrow\ \Re(z) \text{ and } \Im(z) \text{ each satisfy } m\ddot x + k\,x = 0}$$
>
> **Units:** $\mathrm N$ in every bracket
> **Meaning:** one may solve with complex exponentials, where every derivative is a multiplication, and take the real part at the end (Notes.pdf, Sec. 5.2). The argument works because the coefficients are real: it is also the reason why the forced oscillator of Section 11 can be solved with a complex force.

> [!derivation] The phasor in the complex plane
> **Law:** polar form of the complex amplitude and of the exponent; modulus and argument of a product of exponentials
> **Source:** Notes.pdf Fig. 5.2; Notes.pdf, Sec. 5.2; [Lecture 6, Slide 4]
>
> [Lecture 6, Slide 4] writes a general complex exponential with the complex amplitude $A$ and the eigenvalue $p$ split as $-\gamma + i\omega$: $\omega$ is the angular frequency and $\gamma$ the decay or damping rate. The free oscillation of this section is the case of $\gamma$ equal to zero and $\omega$ equal to $\omega_0$.
>
> $$\begin{aligned}
> z &= A\exp(p\,t) \quad &\text{([Lecture 6, Slide 4])} \\
> &= a\exp(i\phi)\exp\big((-\gamma + i\omega)\,t\big) \quad &\text{(polar form of $A$; $p = -\gamma + i\omega$)} \\
> &= a\exp(-\gamma t)\exp\big(i(\omega t + \phi)\big) \quad &\text{(the exponents add; real and imaginary exponents grouped)} \\
> \lvert z\rvert &= a\exp(-\gamma t) \quad &\text{($\lvert\exp(i\beta)\rvert = \sqrt{\cos^2\beta + \sin^2\beta} = 1$)} \\
> \arg z &= \omega t + \phi \quad &\text{(argument of $\exp(i\beta)$ is $\beta$)} \\
> \frac{d}{dt}\arg z &= \omega \quad &\text{(rate at which the arrow turns)} \\
> \Re(z) &= a\exp(-\gamma t)\cos(\omega t + \phi) \quad &\text{(Euler's relation: projection on the real axis)} \\
> \lvert z\rvert &= a,\qquad \Re(z) = a\cos(\omega_0 t + \phi) \quad &\text{(free undamped oscillator: $\gamma = 0$, $\omega = \omega_0$)}
> \end{aligned}$$
>
> $$\boxed{z = a\exp(-\gamma t)\exp\big(i(\omega t + \phi)\big):\quad \lvert z\rvert = a\exp(-\gamma t),\quad \arg z = \omega t + \phi;\qquad \text{undamped: a circle of radius } a \text{ at the rate } \omega_0}$$
>
> **Units:** $\lvert z\rvert$ in $\mathrm m$; $\omega$, $\gamma$ and the rate of the argument in $\mathrm{s^{-1}}$
> **Meaning:** the phasor, the arrow from $0$ to $z$, turns about the origin with angular velocity $\omega_0$ on a circle whose radius is the amplitude, starting at the initial phase; the solution is the projection of this circular motion on the real axis, which is why $\omega_0$ is called the angular frequency (Notes.pdf, Sec. 5.2). Exponentials with $\omega$ positive turn counterclockwise, and with $\gamma$ positive their modulus decays with time, so the arrow spirals in ([Lecture 6, Slide 4]): this is the damped oscillator of Section 10.

![[attachments/EM-T/t2-phasor.svg]]

## 10. The damped harmonic oscillator

A viscous damper added to the spring-mass system exerts a force proportional and opposite to the velocity, with the proportionality constant $\lambda$ (Notes.pdf, Sec. 5.3); with $k$ and $\lambda$ positive and no applied force, the equation of motion is the free damped equation of the first box of Section 8 ([Lecture 6, Slide 5]). The damper is a non-conservative force, so the mechanical energy is no longer constant.

> [!derivation] Energy dissipated by the damper
> **Law:** rate of change of the mechanical energy equals the power of the non-conservative forces (Section 5)
> **Source:** Notes.pdf, Eq. 5.19; Notes.pdf, Sec. 4.5.1; [Lecture 2, Slide 19]
>
> The spring force is conservative, with the potential of Section 8; the damper force is the non-conservative force.
>
> $$\begin{aligned}
> \frac{dE}{dt} &= \mathbf F_\lambda\cdot\mathbf v_0^P \quad &\text{(Section 5: $dE_0/dt = \mathbf F_N\cdot\mathbf v_0^P$)} \\
> &= \left(-\lambda\dot x\,\mathbf i\right)\cdot\left(\dot x\,\mathbf i\right) \quad &\text{(damper force, Eq. 5.19; velocity along $\mathbf i$)} \\
> &= -\lambda\,\dot x^2 \quad &\text{($\mathbf i\cdot\mathbf i = 1$)} \\
> E &= \tfrac12\,m\,\dot x^2 + \tfrac12\,k\,x^2 \quad &\text{(mechanical energy of the oscillator)}
> \end{aligned}$$
>
> $$\boxed{\frac{d}{dt}\left(\tfrac12\,m\,\dot x^2 + \tfrac12\,k\,x^2\right) = -\lambda\,\dot x^2 \leq 0}$$
>
> **Units:** $\mathrm{(N\,s/m)(m/s)^2} = \mathrm{N\,m/s} = \mathrm W$
> **Meaning:** the damper removes energy at every instant at which the particle moves, so the energy can only decrease, and it stays constant only at the instants of zero velocity. The oscillations must therefore die out, which the solutions below make precise.

> [!derivation] Characteristic equation of the damped oscillator
> **Law:** trial exponential solution; quadratic formula; sign of the discriminant
> **Source:** Notes.pdf, Eq. 5.20; Notes.pdf, Eq. 5.21; Notes.pdf, Eq. 5.22; Notes.pdf, Eq. 5.23; [Lecture 6, Slide 5]
>
> $$\begin{aligned}
> m\ddot x + \lambda\dot x + k\,x &= 0 \quad &\text{(Eq. 5.20: Section 8 with $F_x = 0$)} \\
> x &= \exp(p\,t),\qquad \dot x = p\exp(p\,t),\qquad \ddot x = p^2\exp(p\,t) \quad &\text{(trial solution and its derivatives, chain rule; Section 8)} \\
> \left(m\,p^2 + \lambda\,p + k\right)\exp(p\,t) &= 0 \quad &\text{(substitute)} \\
> m\,p^2 + \lambda\,p + k &= 0 \quad &\text{(the exponential is never zero; Eq. 5.21)} \\
> p^2 + 2\gamma\,p + \omega_0^2 &= 0 \quad &\text{(divide by $m$; Eq. 5.23; [Lecture 6, Slide 5])} \\
> p &= \frac{-2\gamma \pm \sqrt{4\gamma^2 - 4\omega_0^2}}{2} \quad &\text{(quadratic formula)} \\
> &= -\gamma \pm \sqrt{\gamma^2 - \omega_0^2} \quad &\text{(take the factor $4$ out of the root and divide by $2$; Eq. 5.22)} \\
> \sqrt{\gamma^2 - \omega_0^2} &< \gamma \quad &\text{(when $\gamma > \omega_0$: the radicand is smaller than $\gamma^2$)} \\
> -\gamma \pm \sqrt{\gamma^2 - \omega_0^2} &< 0 \quad &\text{(both real roots are then negative)}
> \end{aligned}$$
>
> $$\boxed{p = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}:\quad \frac{\gamma}{\omega_0} < 1 \text{ complex conjugate},\quad \frac{\gamma}{\omega_0} = 1 \text{ double, } -\gamma,\quad \frac{\gamma}{\omega_0} > 1 \text{ real, both negative}}$$
>
> **Units:** $p$, $\gamma$ and $\omega_0$ in $\mathrm{s^{-1}}$; every term of the characteristic equation in $\mathrm{s^{-2}}$
> **Meaning:** the roots are generally complex (Notes.pdf, Sec. 5.3), and the sign of the discriminant, that is, the damping ratio compared with one, separates three kinds of motion: small, critical and large damping. In every case their real part is negative, so every solution decays.

### Small damping

> [!derivation] Underdamped solution
> **Law:** complex conjugate roots; a real solution has conjugate coefficients; Euler's relation
> **Source:** Notes.pdf, Eq. 5.24; Notes.pdf, Eq. 5.25; Notes.pdf, Eq. 5.26; [Lecture 6, Slide 8]
>
> $$\begin{aligned}
> \sqrt{\gamma^2 - \omega_0^2} &= \sqrt{-\left(\omega_0^2 - \gamma^2\right)} \quad &\text{($\gamma < \omega_0$: the radicand is negative)} \\
> &= i\,\omega,\qquad \omega = \sqrt{\omega_0^2 - \gamma^2} \quad &\text{($\sqrt{-1} = i$; Eq. 5.24)} \\
> p_\pm &= -\gamma \pm i\,\omega \quad &\text{(the two roots; [Lecture 6, Slide 8])} \\
> x &= D_1\exp\big((-\gamma + i\omega)\,t\big) + D_2\exp\big((-\gamma - i\omega)\,t\big) \quad &\text{(two distinct roots, Section 8)} \\
> &= \tfrac12 A\exp(i\omega t - \gamma t) + \tfrac12 A^*\exp(-i\omega t - \gamma t) \quad &\text{($x$ real: $D_2 = D_1^*$, and $A$ is twice $D_1$, as in Section 9; Eq. 5.25)} \\
> &= \Re\big[A\exp(i\omega t - \gamma t)\big] \quad &\text{(the second term is the conjugate of the first; Eq. 5.26)} \\
> &= a\exp(-\gamma t)\,\Re\big[\exp(i\phi)\exp(i\omega t)\big] \quad &\text{($A = a\exp(i\phi)$; the real factor $a\exp(-\gamma t)$ comes out)} \\
> &= a\exp(-\gamma t)\cos(\omega t + \phi) \quad &\text{(exponents add; Euler's relation)} \\
> &= \exp(-\gamma t)\left[C_1\cos(\omega t) + C_2\sin(\omega t)\right] \quad &\text{(cosine of a sum, with $C_1 = a\cos\phi$, $C_2 = -a\sin\phi$)} \\
> \omega^2 &= \omega_0^2 - \gamma^2 < \omega_0^2 \quad &\text{($\gamma$ is positive)}
> \end{aligned}$$
>
> $$\boxed{x = a\exp(-\gamma t)\cos(\omega t + \phi) = \exp(-\gamma t)\left[C_1\cos(\omega t) + C_2\sin(\omega t)\right],\qquad \omega = \sqrt{\omega_0^2 - \gamma^2} < \omega_0}$$
>
> **Units:** $a$, $C_1$, $C_2$ in $\mathrm m$; $\gamma t$ and $\omega t$ dimensionless
> **Meaning:** the solution is an oscillation with the exponentially decreasing amplitude $a\exp(-\gamma t)$ and the angular frequency $\omega$ of the damped oscillator, always smaller than the frequency $\omega_0$ of the undamped one (Notes.pdf, Sec. 5.3.1; Notes.pdf Fig. 5.3): the oscillatory behaviour of the ideal case, with a slightly different frequency, damped with the decay rate $\gamma$ ([Lecture 6, Slide 8]).

> [!warning] Erratum to Notes.pdf, Eq. 5.26: position of a bracket
> The last form of Eq. 5.26 is printed with the real part closed before the factor $\exp(i\omega t)$, so that this factor multiplies a real number from outside the real part and the printed expression is complex, not a displacement. The real part must enclose both exponentials of unit modulus, as in the box above and on [Lecture 6, Slide 8], where the factor $a\exp(-\gamma t)$ is outside and $\exp(i\phi)\exp(i\omega t)$ inside. Check: with the printed bracket, for $\gamma$ equal to zero, $\phi$ equal to zero and $\omega t$ equal to $\pi/2$ the expression is $a$ times $i$, a purely imaginary number, while the corrected one gives $a\cos(\pi/2)$, zero.

> [!derivation] Constants of the underdamped solution from the initial conditions
> **Law:** evaluation of the solution and of its first derivative at the initial instant
> **Source:** Notes.pdf, Eq. 5.26; [Lecture 6, Slide 8]; [Lecture 6, Slide 3]
>
> $$\begin{aligned}
> x(0) &= \exp(0)\left[C_1\cos 0 + C_2\sin 0\right] \quad &\text{(last form of the box above at $t = 0$)} \\
> &= C_1 \quad &\text{(arithmetic)} \\
> C_1 &= x_0 \quad &\text{(first initial condition)} \\
> \dot x &= -\gamma\exp(-\gamma t)\left[C_1\cos(\omega t) + C_2\sin(\omega t)\right] + \exp(-\gamma t)\left[-C_1\,\omega\sin(\omega t) + C_2\,\omega\cos(\omega t)\right] \quad &\text{(product rule; chain rule on each factor)} \\
> \dot x(0) &= -\gamma\,C_1 + \omega\,C_2 \quad &\text{(at $t = 0$)} \\
> C_2 &= \frac{\dot x_0 + \gamma\,x_0}{\omega} \quad &\text{(second initial condition with $C_1 = x_0$; divide by $\omega$)}
> \end{aligned}$$
>
> $$\boxed{C_1 = x_0,\qquad C_2 = \frac{\dot x_0 + \gamma\,x_0}{\omega}}$$
>
> **Units:** $\mathrm m$ for both: $\mathrm{(m/s + s^{-1}\,m)/s^{-1}}$
> **Meaning:** without damping ($\gamma$ zero, $\omega$ equal to $\omega_0$) these are Eqs. 5.8 and 5.9. A particle released from rest still needs a small sine term, because the damper slows it from the start.

> [!derivation] Relaxation time and quality factor
> **Law:** decay of the amplitude $a\exp(-\gamma t)$; definitions of the notes; first-order expansion for small damping
> **Source:** Notes.pdf, Eq. 5.27; Notes.pdf, Eq. 5.28; Notes.pdf, Sec. 5.3.1; [Lecture 6, Slide 8]
>
> $$\begin{aligned}
> a\exp(-\gamma\,t_r) &= a\,e^{-1} \quad &\text{(the amplitude falls by the factor $1/e$ in the time $t_r$)} \\
> t_r &= \frac{1}{\gamma} \quad &\text{(equal exponents)} \\
> &= \frac{2m}{\lambda} \quad &\text{($\gamma = \lambda/(2m)$; Eq. 5.27)} \\
> Q &= \frac{\omega_0}{2\gamma} \quad &\text{(definition of the quality factor; Eq. 5.28; [Lecture 6, Slide 8])} \\
> &= \frac{m\,\omega_0}{\lambda} \quad &\text{(the same substitution; Eq. 5.28)} \\
> \frac{a\exp\big(-\gamma\,(t + 2\pi/\omega)\big)}{a\exp(-\gamma t)} &= \exp\left(-\frac{2\pi\gamma}{\omega}\right) \quad &\text{(amplitude after one period $2\pi/\omega$, over the amplitude before it)} \\
> \omega &= \omega_0\left(1 - \frac{\gamma^2}{\omega_0^2}\right)^{1/2} \quad &\text{(take $\omega_0^2$ out of the root)} \\
> &= \omega_0\left(1 - \frac{\gamma^2}{2\,\omega_0^2} + \dots\right) \quad &\text{(binomial expansion; the correction is of second order in $\gamma/\omega_0$)} \\
> \exp\left(-\frac{2\pi\gamma}{\omega}\right) &\simeq \exp\left(-\frac{2\pi\gamma}{\omega_0}\right) \quad &\text{(small damping: keep $\omega \simeq \omega_0$)} \\
> &= \exp\left(-\frac{\pi}{Q}\right) \quad &\text{($2\gamma/\omega_0 = 1/Q$)} \\
> \frac{t_r}{2\pi/\omega} &= \frac{\omega}{2\pi\gamma} \quad &\text{(number of periods in a relaxation time)} \\
> &\simeq \frac{\omega_0}{2\pi\gamma} \quad &\text{($\omega \simeq \omega_0$)} \\
> &= \frac{Q}{\pi} \quad &\text{(definition of $Q$)}
> \end{aligned}$$
>
> $$\boxed{t_r = \frac{1}{\gamma} = \frac{2m}{\lambda},\qquad Q = \frac{m\,\omega_0}{\lambda} = \frac{\omega_0}{2\gamma};\qquad \text{per period: } \exp\left(-\frac{2\pi\gamma}{\omega}\right) \simeq \exp\left(-\frac{\pi}{Q}\right),\quad \frac{t_r}{2\pi/\omega} \simeq \frac{Q}{\pi}}$$
>
> **Units:** $t_r$ in $\mathrm s$ ($1/\mathrm{s^{-1}}$ and $\mathrm{kg/(N\,s/m)} = \mathrm s$); $Q$ dimensionless ($\mathrm{kg\,s^{-1}/(N\,s/m)} = 1$)
> **Meaning:** small damping means a large quality factor (Notes.pdf, Sec. 5.3.1). For $Q$ equal to $10$ ($\gamma/\omega_0$ equal to $0.05$) one period multiplies the amplitude by $0.730$ (the approximation $\exp(-\pi/Q)$ gives $0.730$ as well), and a relaxation time holds about $3.2$ periods.

### Large damping

> [!derivation] Overdamped solution
> **Law:** two real negative roots; general solution with two exponentials; constants from the initial conditions
> **Source:** Notes.pdf, Eq. 5.29; Notes.pdf, Eq. 5.30; Notes.pdf, Sec. 5.3.2; [Lecture 6, Slide 9]
>
> The decay rates $\gamma_+$ and $\gamma_-$ are both positive, by the last row of the box on the characteristic equation.
>
> $$\begin{aligned}
> p &= -\gamma \pm \sqrt{\gamma^2 - \omega_0^2} \quad &\text{($\gamma > \omega_0$: real roots, Eq. 5.22)} \\
> p_- &= -\gamma_+,\qquad p_+ = -\gamma_-,\qquad \gamma_\pm = \gamma \pm \sqrt{\gamma^2 - \omega_0^2} \quad &\text{(Eq. 5.29; [Lecture 6, Slide 9])} \\
> x &= C_+\exp(-\gamma_+ t) + C_-\exp(-\gamma_- t) \quad &\text{(two distinct real roots; Eq. 5.30 with $C_+ = A/2$, $C_- = B/2$)} \\
> x_0 &= C_+ + C_- \quad &\text{(at $t = 0$)} \\
> \dot x &= -\gamma_+ C_+\exp(-\gamma_+ t) - \gamma_- C_-\exp(-\gamma_- t) \quad &\text{(differentiate; chain rule)} \\
> \dot x_0 &= -\gamma_+ C_+ - \gamma_- C_- \quad &\text{(at $t = 0$)} \\
> \gamma_+ x_0 + \dot x_0 &= \left(\gamma_+ - \gamma_-\right)C_- \quad &\text{(multiply the first condition by $\gamma_+$ and add the second)} \\
> C_- &= \frac{\dot x_0 + \gamma_+ x_0}{\gamma_+ - \gamma_-} \quad &\text{(divide; $\gamma_+ - \gamma_- = 2\sqrt{\gamma^2 - \omega_0^2} > 0$)} \\
> C_+ &= x_0 - C_- \quad &\text{(first condition)} \\
> &= -\frac{\dot x_0 + \gamma_- x_0}{\gamma_+ - \gamma_-} \quad &\text{(common denominator)} \\
> \frac{C_+\exp(-\gamma_+ t)}{C_-\exp(-\gamma_- t)} &= \frac{C_+}{C_-}\exp\big(-(\gamma_+ - \gamma_-)\,t\big) \quad &\text{(ratio of the fast term to the slow term, for $C_-$ nonzero)} \\
> &\to 0 \ \text{ as } t \to \infty \quad &\text{($\gamma_+ > \gamma_-$)}
> \end{aligned}$$
>
> $$\boxed{x = C_+\exp(-\gamma_+ t) + C_-\exp(-\gamma_- t),\quad \gamma_\pm = \gamma \pm \sqrt{\gamma^2 - \omega_0^2};\quad C_- = \frac{\dot x_0 + \gamma_+ x_0}{\gamma_+ - \gamma_-},\ \ C_+ = -\frac{\dot x_0 + \gamma_- x_0}{\gamma_+ - \gamma_-}}$$
>
> **Units:** $\gamma_\pm$ in $\mathrm{s^{-1}}$; $C_\pm$ in $\mathrm m$
> **Meaning:** the oscillatory behaviour has disappeared: the oscillator is dominated by the damping force, and the displacement is the sum of two real decaying exponentials, a fast one with $\gamma_+$ and a slow one with $\gamma_-$, which survives longer (Notes.pdf, Sec. 5.3.2; [Lecture 6, Slide 9]). For large times the slow term dominates, so the displacement falls by the factor $1/e$ in a time of order $1/\gamma_-$: the relaxation time is now about $1/\gamma_-$.

### Critical damping

> [!derivation] Critically damped solution
> **Law:** double root of the characteristic equation; second solution checked by direct substitution; constants from the initial conditions
> **Source:** Notes.pdf, Eq. 5.31; Notes.pdf, Sec. 5.3.3; [Lecture 6, Slide 10]; [Lecture 6, Slide 3]
>
> $$\begin{aligned}
> p &= -\gamma \quad &\text{($\gamma = \omega_0$: zero discriminant, one double root)} \\
> x &= t\exp(-\gamma t) \quad &\text{(candidate second solution)} \\
> \dot x &= \exp(-\gamma t) - \gamma\,t\exp(-\gamma t) \quad &\text{(product rule; chain rule on the exponential)} \\
> \ddot x &= -\gamma\exp(-\gamma t) - \gamma\exp(-\gamma t) + \gamma^2\,t\exp(-\gamma t) \quad &\text{(differentiate each term; product rule on the second)} \\
> &= \left(-2\gamma + \gamma^2\,t\right)\exp(-\gamma t) \quad &\text{(group)} \\
> \ddot x + 2\gamma\,\dot x + \omega_0^2\,x &= \left(-2\gamma + \gamma^2 t + 2\gamma - 2\gamma^2 t + \omega_0^2\,t\right)\exp(-\gamma t) \quad &\text{(substitute the three rows)} \\
> &= \left(\omega_0^2 - \gamma^2\right)t\exp(-\gamma t) \quad &\text{(the terms without $t$ cancel)} \\
> &= 0 \quad &\text{($\gamma = \omega_0$: the candidate is a solution)} \\
> \frac{t\exp(-\gamma t)}{\exp(-\gamma t)} &= t \quad &\text{(not constant: the two solutions are independent)} \\
> x &= \left(C_1 + C_2\,t\right)\exp(-\gamma t) \quad &\text{(general solution, Eq. 5.31, which writes $a$ and $b$ for $C_1$ and $C_2$)} \\
> x(0) &= C_1 \quad &\text{(at $t = 0$)} \\
> \dot x &= C_2\exp(-\gamma t) - \gamma\left(C_1 + C_2\,t\right)\exp(-\gamma t) \quad &\text{(product rule)} \\
> \dot x(0) &= C_2 - \gamma\,C_1 \quad &\text{(at $t = 0$)} \\
> C_1 &= x_0,\qquad C_2 = \dot x_0 + \gamma\,x_0 \quad &\text{(initial conditions)}
> \end{aligned}$$
>
> $$\boxed{\gamma = \omega_0:\qquad x = \left(C_1 + C_2\,t\right)\exp(-\gamma t),\qquad C_1 = x_0,\ \ C_2 = \dot x_0 + \gamma\,x_0}$$
>
> **Units:** $C_1$ in $\mathrm m$; $C_2$ in $\mathrm{m/s}$, so $C_2\,t$ is in $\mathrm m$
> **Meaning:** with a double root the single exponential holds only one arbitrary constant and cannot be the general solution; the second independent solution is $t\exp(-\gamma t)$, a new type of function (Notes.pdf, Sec. 5.3.3; [Lecture 6, Slide 10]), as [Lecture 6, Slide 3] states for any double root. The displacement decays without oscillating; with a large initial velocity towards the equilibrium it may cross zero once, where the bracket vanishes, as in the example of [Lecture 6, Slide 10].

![[attachments/EM-T/t2-damped-responses.svg]]

> [!derivation] Critical damping gives the fastest return to equilibrium
> **Law:** the slowest of the two decay rates sets the response time; derivative of the slow rate with respect to $\gamma$
> **Source:** Notes.pdf, Sec. 5.3.3; [Lecture 6, Slide 10]; Notes.pdf, Eq. 5.29
>
> The stiffness, hence $\omega_0$, is fixed and the damping is varied. The decay rate of each solution is minus the real part of its root.
>
> $$\begin{aligned}
> -\Re(p_\pm) &= \gamma \quad &\text{($\gamma < \omega_0$: both roots $-\gamma \pm i\omega$; grows with $\gamma$)} \\
> -p_+ &= \gamma_- = \gamma - \sqrt{\gamma^2 - \omega_0^2} \quad &\text{($\gamma > \omega_0$: the slower of the two rates)} \\
> \frac{d\gamma_-}{d\gamma} &= 1 - \frac{\gamma}{\sqrt{\gamma^2 - \omega_0^2}} \quad &\text{(derivative; chain rule on the root)} \\
> &< 0 \quad &\text{($\sqrt{\gamma^2 - \omega_0^2} < \gamma$: the fraction exceeds one)} \\
> \gamma_- &= \frac{\left(\gamma - \sqrt{\gamma^2 - \omega_0^2}\right)\left(\gamma + \sqrt{\gamma^2 - \omega_0^2}\right)}{\gamma + \sqrt{\gamma^2 - \omega_0^2}} \quad &\text{(multiply and divide by the conjugate)} \\
> &= \frac{\omega_0^2}{\gamma + \sqrt{\gamma^2 - \omega_0^2}} \quad &\text{(difference of squares: $\gamma^2 - (\gamma^2 - \omega_0^2)$)} \\
> &\simeq \frac{\omega_0^2}{2\gamma} \ \text{ for } \gamma \gg \omega_0 \quad &\text{(the root tends to $\gamma$)} \\
> \gamma_- &\to \omega_0 \ \text{ as } \gamma \to \omega_0 \quad &\text{(the root vanishes: both branches meet the value $\omega_0$ at critical damping)}
> \end{aligned}$$
>
> $$\boxed{\text{slowest decay rate} = \begin{cases} \gamma, & \gamma \leq \omega_0 \\ \gamma - \sqrt{\gamma^2 - \omega_0^2}, & \gamma \geq \omega_0 \end{cases} \quad\text{maximal, equal to } \omega_0, \text{ at } \gamma = \omega_0}$$
>
> **Units:** every rate in $\mathrm{s^{-1}}$; the derivative is dimensionless
> **Meaning:** below critical damping the response time is the relaxation time $1/\gamma$, which decreases as $\gamma$ grows; above it the response time $1/\gamma_-$ increases with $\gamma$, and for very strong damping the particle creeps back at the slow rate of about $\omega_0^2/(2\gamma)$. The shortest response time, $1/\omega_0$, is obtained with critical damping, which is the ideal for a measuring instrument whose pointer must settle at its correct position as quickly as possible (Notes.pdf, Sec. 5.3.3): the smaller decay rate of the two independent solutions is maximal in the critical case ([Lecture 6, Slide 10]).

![[attachments/EM-T/t2-decay-rates.svg]]

## 11. The damped oscillator under a periodic force

One is often interested in the response of an oscillatory system to an external force that is a function of time (Notes.pdf, Sec. 5.4): the equation of motion is then the complete equation of the first box of Section 8, with the applied force on the right side ([Lecture 6, Slide 11]). Here $x_p$ and $x_h$ denote a particular solution of the complete equation and a solution of the homogeneous one (the notes write $x_1$ and $x_0$; $x_0$ is the initial position in this note).

> [!derivation] General solution of the complete equation
> **Law:** linearity: the difference of two solutions of the complete equation solves the homogeneous one
> **Source:** Notes.pdf, Eq. 5.32; Notes.pdf, Eq. 5.20; Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3]
>
> $F(t)$ is the applied force and $x_p$ any one solution of the complete equation.
>
> $$\begin{aligned}
> m\ddot x_p + \lambda\dot x_p + k\,x_p &= F(t) \quad &\text{(a particular solution, Eq. 5.32)} \\
> m\ddot x_h + \lambda\dot x_h + k\,x_h &= 0 \quad &\text{(a homogeneous solution, Eq. 5.20)} \\
> m\left(\ddot x_p + \ddot x_h\right) + \lambda\left(\dot x_p + \dot x_h\right) + k\left(x_p + x_h\right) &= F(t) + 0 \quad &\text{(add the two rows; derivative of a sum)} \\
> m\left(\ddot x - \ddot x_p\right) + \lambda\left(\dot x - \dot x_p\right) + k\left(x - x_p\right) &= F(t) - F(t) = 0 \quad &\text{(any other solution $x$ of Eq. 5.32, minus the first row)}
> \end{aligned}$$
>
> $$\boxed{x = x_p + x_h,\qquad x_h = \text{general solution of } m\ddot x + \lambda\dot x + k\,x = 0}$$
>
> **Units:** $\mathrm N$ in every row
> **Meaning:** the sum of a particular solution and a homogeneous one is a solution, and every solution is of this form, because its difference from the particular one solves the homogeneous equation: one particular solution of the complete equation is enough, and the general solution follows by adding the general solution of Section 10, built from two independent solutions (Notes.pdf, Sec. 5.4). The solutions of the complete equation form a two-dimensional affine space ([Lecture 6, Slide 3]).

> [!derivation] The periodic force in complex form
> **Law:** Euler's relation; real coefficients keep the real part of a complex solution a solution
> **Source:** Notes.pdf, Eq. 5.33; Notes.pdf, Eq. 5.34; Notes.pdf, Eq. 5.35; [Lecture 6, Slide 11]
>
> $F_1$ and $\omega_1$ are real constants; $F_1$ is taken positive (a negative amplitude is a shift of the origin of time by half a period).
>
> $$\begin{aligned}
> F(t) &= F_1\cos(\omega_1 t) \quad &\text{(Eq. 5.33)} \\
> &= \Re\big[F_1\exp(i\omega_1 t)\big] \quad &\text{(Euler's relation, $F_1$ real; Eq. 5.34)} \\
> m\ddot z + \lambda\dot z + k\,z &= F_1\exp(i\omega_1 t) \quad &\text{(complex equation, Eq. 5.35)} \\
> m\,\frac{d^2\Re(z)}{dt^2} + \lambda\,\frac{d\Re(z)}{dt} + k\,\Re(z) &= \Re\big[F_1\exp(i\omega_1 t)\big] \quad &\text{(real part of both sides; $m$, $\lambda$, $k$ real, as in Section 9)} \\
> &= F_1\cos(\omega_1 t) \quad &\text{(second row)}
> \end{aligned}$$
>
> $$\boxed{m\ddot z + \lambda\dot z + k\,z = F_1\exp(i\omega_1 t) \ \Longrightarrow\ x = \Re(z) \text{ solves } m\ddot x + \lambda\dot x + k\,x = F_1\cos(\omega_1 t)}$$
>
> **Units:** $\mathrm N$ on both sides
> **Meaning:** the complex equation is solved first, where derivatives of $\exp(i\omega_1 t)$ are multiplications by $i\omega_1$, and its real part is the solution of the real problem (Notes.pdf, Sec. 5.4; [Lecture 6, Slide 11]).

> [!derivation] Particular solution: amplitude and phase of the forced oscillation
> **Law:** trial solution with the period of the force; equal real and imaginary parts; right triangle of the complex coefficient
> **Source:** Notes.pdf, Eq. 5.36; Notes.pdf, Eq. 5.37; Notes.pdf, Eq. 5.38; Notes.pdf, Eq. 5.39; Notes.pdf, Eq. 5.40; Notes.pdf, Eq. 5.41; Notes.pdf, Eq. 5.42; [Lecture 6, Slide 11]
>
> The coefficient of $a_1$ in Eq. 5.38 is a complex number: in the complex plane it is the hypotenuse of a right triangle whose horizontal leg is the real part $\omega_0^2 - \omega_1^2$ (adjacent to its argument) and whose vertical leg is the imaginary part $2\gamma\omega_1$ (opposite to its argument). By Eq. 5.38 its argument is $-\phi_1$.
>
> $$\begin{aligned}
> z_p &= A_1\exp(i\omega_1 t),\qquad A_1 = a_1\exp(i\phi_1) \quad &\text{(trial solution with the frequency of the force, Eq. 5.36)} \\
> \dot z_p &= i\omega_1 A_1\exp(i\omega_1 t) \quad &\text{(chain rule)} \\
> \ddot z_p &= -\omega_1^2 A_1\exp(i\omega_1 t) \quad &\text{(chain rule again; $i^2 = -1$)} \\
> \left(-m\,\omega_1^2 + i\lambda\omega_1 + k\right)A_1\exp(i\omega_1 t) &= F_1\exp(i\omega_1 t) \quad &\text{(substitute in Eq. 5.35)} \\
> \left(-m\,\omega_1^2 + i\lambda\omega_1 + k\right)A_1 &= F_1 \quad &\text{(divide by the exponential; Eq. 5.37)} \\
> \left(\omega_0^2 - \omega_1^2 + 2i\gamma\omega_1\right)A_1 &= \frac{F_1}{m} \quad &\text{(divide by $m$; $k/m = \omega_0^2$, $\lambda/m = 2\gamma$)} \\
> \left(\omega_0^2 - \omega_1^2 + 2i\gamma\omega_1\right)a_1 &= \frac{F_1}{m}\exp(-i\phi_1) \quad &\text{($A_1 = a_1\exp(i\phi_1)$; multiply by $\exp(-i\phi_1)$; Eq. 5.38)} \\
> &= \frac{F_1}{m}\left(\cos\phi_1 - i\sin\phi_1\right) \quad &\text{(Euler's relation)} \\
> \left(\omega_0^2 - \omega_1^2\right)a_1 &= \frac{F_1}{m}\cos\phi_1 \quad &\text{(real parts; Eq. 5.39)} \\
> 2\gamma\omega_1\,a_1 &= -\frac{F_1}{m}\sin\phi_1 \quad &\text{(imaginary parts; Eq. 5.40)} \\
> \left[\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2\right]a_1^2 &= \frac{F_1^2}{m^2}\left(\cos^2\phi_1 + \sin^2\phi_1\right) \quad &\text{(square the two rows and add)} \\
> &= \frac{F_1^2}{m^2} \quad &\text{(Pythagoras)} \\
> a_1 &= \frac{F_1/m}{\sqrt{\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2}} \quad &\text{(positive root: hypotenuse of the triangle; Eq. 5.41)} \\
> \tan\phi_1 &= -\frac{2\gamma\omega_1}{\omega_0^2 - \omega_1^2} \quad &\text{(divide Eq. 5.40 by Eq. 5.39: minus opposite over adjacent; Eq. 5.42)} \\
> \sin\phi_1 &= -\frac{2\gamma\omega_1\,a_1\,m}{F_1} < 0 \quad &\text{(Eq. 5.40 solved: $\gamma$, $\omega_1$, $a_1$, $F_1$ positive)} \\
> \cos\phi_1 &= \frac{\left(\omega_0^2 - \omega_1^2\right)a_1\,m}{F_1} \quad &\text{(Eq. 5.39 solved: the sign of $\omega_0^2 - \omega_1^2$)}
> \end{aligned}$$
>
> $$\boxed{a_1 = \frac{F_1/m}{\sqrt{\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2}},\qquad \tan\phi_1 = -\frac{2\gamma\omega_1}{\omega_0^2 - \omega_1^2},\qquad -\pi < \phi_1 < 0}$$
>
> **Units:** $a_1$ in $\mathrm{(N/kg)/s^{-2}} = \mathrm{(m/s^2)\,s^2} = \mathrm m$; the tangent is a quotient of two terms in $\mathrm{s^{-2}}$, dimensionless
> **Meaning:** of the two angles with this tangent, the meaningful one lies between $-\pi$ and $0$, because the sine of $\phi_1$ is negative (Notes.pdf, Sec. 5.4): below $\omega_0$ the cosine is positive and $\phi_1$ lies between $-\pi/2$ and $0$; above $\omega_0$ it lies between $-\pi$ and $-\pi/2$. A negative phase means that the oscillator lags behind the force: it moves after the force phasor in the complex circle ([Lecture 6, Slide 12]).

![[attachments/EM-T/t2-forced-triangle.svg]]

> [!derivation] General forced solution and the steady state
> **Law:** real part of the particular solution; superposition with the homogeneous solution; decay of the transient
> **Source:** Notes.pdf, Eq. 5.43; Notes.pdf, Eq. 5.44; Notes.pdf, Sec. 5.4; [Lecture 6, Slide 12]
>
> For damping less than critical the homogeneous solution is the underdamped one of Section 10.
>
> $$\begin{aligned}
> x_p &= \Re\Big(a_1\exp\big(i(\omega_1 t + \phi_1)\big)\Big) \quad &\text{(real part of Eq. 5.36)} \\
> &= a_1\cos(\omega_1 t + \phi_1) \quad &\text{(Euler's relation; Eq. 5.43)} \\
> x &= a_1\cos(\omega_1 t + \phi_1) + a\exp(-\gamma t)\cos(\omega t + \phi) \quad &\text{(add the homogeneous solution; Eq. 5.44; [Lecture 6, Slide 12])} \\
> x_h(0) &= x_0 - a_1\cos\phi_1 \quad &\text{(initial value of the homogeneous part: $x_0$ minus $x_p(0)$)} \\
> \dot x_p &= -a_1\,\omega_1\sin(\omega_1 t + \phi_1) \quad &\text{(differentiate $x_p$; chain rule)} \\
> \dot x_h(0) &= \dot x_0 + a_1\,\omega_1\sin\phi_1 \quad &\text{($\dot x_0$ minus $\dot x_p(0)$)} \\
> \lvert a\exp(-\gamma t)\cos(\omega t + \phi)\rvert &\leq a\exp(-\gamma t) \quad &\text{($\lvert\cos\rvert \leq 1$)} \\
> &\to 0 \ \text{ as } t \to \infty \quad &\text{($\gamma > 0$ when $\lambda \neq 0$)}
> \end{aligned}$$
>
> $$\boxed{x = a_1\cos(\omega_1 t + \phi_1) + a\exp(-\gamma t)\cos(\omega t + \phi) \ \longrightarrow\ a_1\cos(\omega_1 t + \phi_1) \ \text{ for large } t}$$
>
> **Units:** $\mathrm m$ in every term
> **Meaning:** $a_1$ and $\phi_1$ are fixed by the force (Eqs. 5.41 and 5.42), while $a$ and $\phi$ are fixed by the initial conditions: they are those of the underdamped box of Section 10 with the initial values of the homogeneous part found in the fourth and sixth rows. The second term is a free damped oscillation, the initial transient, and dies away exponentially; whatever the initial conditions, the motion is ultimately governed by the external force alone, at the angular frequency $\omega_1$ of the force and not at the natural frequency (Notes.pdf, Sec. 5.4). The particular solution is the solution at long times and is independent of the initial conditions ([Lecture 6, Slide 12]).

> [!info] Extension: beats
> Neither Notes.pdf nor the slides of Lecture 6 treat beats. They appear when an undamped oscillator, started at rest, is driven at a frequency close to its natural frequency: the free and the forced oscillations, of nearly equal frequencies, add up to a fast oscillation whose amplitude swells and fades slowly. The box below derives them with the tools of this section.

> [!derivation] Extension: beats of the undamped forced oscillator
> **Law:** particular solution by substitution; constants from the initial conditions; cosines of a sum and of a difference
> **Source:** Notes.pdf, Eq. 5.32; Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.41; [Lecture 6, Slide 11]
>
> No damper ($\lambda$ zero), the force of Eq. 5.33 with $\omega_1$ different from $\omega_0$, and the particle at rest at the relaxed position at $t$ equal to zero.
>
> $$\begin{aligned}
> \ddot x + \omega_0^2\,x &= \frac{F_1}{m}\cos(\omega_1 t) \quad &\text{(Eq. 5.32 with $\lambda = 0$, divided by $m$)} \\
> x_p &= B_1\cos(\omega_1 t) \quad &\text{(trial solution with the frequency of the force)} \\
> \ddot x_p &= -\omega_1^2 B_1\cos(\omega_1 t) \quad &\text{(chain rule twice)} \\
> \left(\omega_0^2 - \omega_1^2\right)B_1\cos(\omega_1 t) &= \frac{F_1}{m}\cos(\omega_1 t) \quad &\text{(substitute)} \\
> B_1 &= \frac{F_1/m}{\omega_0^2 - \omega_1^2} \quad &\text{(divide; $\omega_1 \neq \omega_0$; Eq. 5.41 with $\gamma = 0$, with a sign)} \\
> x &= C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t) + B_1\cos(\omega_1 t) \quad &\text{(add the homogeneous solution, Eq. 5.7)} \\
> \dot x &= -C_1\,\omega_0\sin(\omega_0 t) + C_2\,\omega_0\cos(\omega_0 t) - B_1\,\omega_1\sin(\omega_1 t) \quad &\text{(differentiate; chain rule)} \\
> C_1 + B_1 &= 0,\qquad C_2\,\omega_0 = 0 \quad &\text{($x(0) = 0$ and $\dot x(0) = 0$)} \\
> x &= B_1\left[\cos(\omega_1 t) - \cos(\omega_0 t)\right] \quad &\text{(substitute $C_1 = -B_1$, $C_2 = 0$)} \\
> \cos(\omega_1 t) &= \cos\tfrac{(\omega_0 + \omega_1)t}{2}\cos\tfrac{(\omega_0 - \omega_1)t}{2} + \sin\tfrac{(\omega_0 + \omega_1)t}{2}\sin\tfrac{(\omega_0 - \omega_1)t}{2} \quad &\text{($\omega_1 t$ is half the sum minus half the difference: cosine of a difference)} \\
> \cos(\omega_0 t) &= \cos\tfrac{(\omega_0 + \omega_1)t}{2}\cos\tfrac{(\omega_0 - \omega_1)t}{2} - \sin\tfrac{(\omega_0 + \omega_1)t}{2}\sin\tfrac{(\omega_0 - \omega_1)t}{2} \quad &\text{($\omega_0 t$ is half the sum plus half the difference: cosine of a sum)} \\
> \cos(\omega_1 t) - \cos(\omega_0 t) &= 2\sin\tfrac{(\omega_0 + \omega_1)t}{2}\sin\tfrac{(\omega_0 - \omega_1)t}{2} \quad &\text{(subtract: the products of cosines cancel)} \\
> x &= \left[2B_1\sin\tfrac{(\omega_0 - \omega_1)t}{2}\right]\sin\tfrac{(\omega_0 + \omega_1)t}{2} \quad &\text{(substitute)} \\
> \sin\tfrac{(\omega_0 - \omega_1)t}{2} &\simeq \tfrac{(\omega_0 - \omega_1)t}{2} \quad &\text{(as $\omega_1 \to \omega_0$, for fixed $t$: first-order Taylor term of the sine)} \\
> 2B_1\,\tfrac{(\omega_0 - \omega_1)t}{2} &= \frac{F_1\,t}{m\left(\omega_0 + \omega_1\right)} \quad &\text{($\omega_0^2 - \omega_1^2 = (\omega_0 - \omega_1)(\omega_0 + \omega_1)$; cancel)} \\
> x &\to \frac{F_1\,t}{2m\,\omega_0}\sin(\omega_0 t) \quad &\text{(limit $\omega_1 \to \omega_0$)}
> \end{aligned}$$
>
> $$\boxed{x = \left[\frac{2F_1/m}{\omega_0^2 - \omega_1^2}\sin\frac{(\omega_0 - \omega_1)t}{2}\right]\sin\frac{(\omega_0 + \omega_1)t}{2};\qquad \omega_1 \to \omega_0:\ \ x \to \frac{F_1\,t}{2m\,\omega_0}\sin(\omega_0 t)}$$
>
> **Units:** $B_1$ in $\mathrm{(m/s^2)/s^{-2}} = \mathrm m$; $\mathrm{N\,s/(kg\,s^{-1})} = \mathrm m$ for the limit
> **Meaning:** for close frequencies the second sine is a fast oscillation at the mean frequency, and the bracket is a slowly varying amplitude that vanishes each time half the frequency difference times $t$ is a multiple of $\pi$, that is, with the beat period $2\pi$ over the magnitude of the difference of the two frequencies: the oscillation swells and fades, and the closer the frequencies, the longer and larger the beats. At equal frequencies the amplitude grows linearly with time without bound: without damping, resonance has no steady state, which is why the damping, however small, sets the height of the peak in Section 12.

![[attachments/EM-T/t2-beats.svg]]

## 12. Resonance

The amplitude and the phase of the forced oscillation depend strongly on the angular frequency of the applied force (Notes.pdf, Sec. 5.4.1); they vary wildly with the difference of the squares of the two frequencies ([Lecture 6, Slide 13]). The amplitude of Eq. 5.41 is largest where the radicand of its denominator is smallest, so every maximum below is found as a minimum of that radicand.

> [!derivation] Oscillator tuned to the force
> **Law:** minimum of the radicand of Eq. 5.41 with respect to the natural frequency
> **Source:** Notes.pdf, Eq. 5.45; Notes.pdf, Eq. 5.41; Notes.pdf, Sec. 5.4.1
>
> $\gamma$ and the forcing frequency $\omega_1$ are fixed and the natural frequency $\omega_0$ of the oscillator is varied.
>
> $$\begin{aligned}
> \frac{d}{d\omega_0}\left[\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2\right] &= 2\left(\omega_0^2 - \omega_1^2\right)\cdot 2\omega_0 \quad &\text{(chain rule; the second term does not depend on $\omega_0$)} \\
> 4\omega_0\left(\omega_0^2 - \omega_1^2\right) &= 0 \quad &\text{(stationary point)} \\
> \omega_0 &= \omega_1 \quad &\text{($\omega_0$ and $\omega_1$ positive)} \\
> \left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2 &\geq 4\gamma^2\omega_1^2 \quad &\text{(a square is never negative: equality only at $\omega_0 = \omega_1$, a minimum)} \\
> a_1 &= \frac{F_1/m}{\sqrt{4\gamma^2\omega_1^2}} \quad &\text{(Eq. 5.41 at $\omega_0 = \omega_1$)} \\
> &= \frac{F_1}{2m\gamma\omega_1} \quad &\text{(root of the square)} \\
> &= \frac{F_1}{\lambda\,\omega_1} \quad &\text{($2m\gamma = \lambda$; Eq. 5.45)}
> \end{aligned}$$
>
> $$\boxed{\omega_0 = \omega_1:\qquad a_1 = \frac{F_1}{2m\gamma\omega_1} = \frac{F_1}{\lambda\,\omega_1}}$$
>
> **Units:** $\mathrm N/\mathrm{(kg\,s^{-1}\,s^{-1})} = \mathrm m$; $\mathrm N/\mathrm{(N\,s\,m^{-1}\,s^{-1})} = \mathrm m$
> **Meaning:** an oscillator whose natural frequency equals the forcing frequency responds with the largest amplitude, which can be very large if the damping constant is small (Notes.pdf, Sec. 5.4.1).

> [!derivation] Resonant frequency for a given oscillator
> **Law:** stationary point of the radicand of Eq. 5.41 with respect to the forcing frequency; sign of its derivative
> **Source:** Notes.pdf, Eq. 5.46; Notes.pdf, Eq. 5.41; Notes.pdf, Eq. 5.42; Notes.pdf, Sec. 5.4.1; [Lecture 6, Slide 14]
>
> Now $\omega_0$ and $\gamma$ are fixed and $\omega_1$, positive, is varied.
>
> $$\begin{aligned}
> \frac{d}{d\omega_1}\left[\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2\right] &= 2\left(\omega_0^2 - \omega_1^2\right)\left(-2\omega_1\right) + 8\gamma^2\omega_1 \quad &\text{(chain rule on the square; derivative of $\omega_1^2$)} \\
> &= 4\omega_1\left(\omega_1^2 - \omega_0^2 + 2\gamma^2\right) \quad &\text{(take out $4\omega_1$)} \\
> \omega_1^2 &= \omega_0^2 - 2\gamma^2 \quad &\text{(the bracket vanishes; $\omega_1 > 0$)} \\
> \omega_1 &= \sqrt{\omega_0^2 - 2\gamma^2} \quad &\text{(real only if $\gamma < \omega_0/\sqrt2$; Eq. 5.46)} \\
> \omega_1^2 - \omega_0^2 + 2\gamma^2 &\lessgtr 0 \ \text{ for } \omega_1 \lessgtr \sqrt{\omega_0^2 - 2\gamma^2} \quad &\text{(the derivative goes from negative to positive: a minimum of the radicand)} \\
> \left(2\gamma^2\right)^2 + 4\gamma^2\left(\omega_0^2 - 2\gamma^2\right) &= 4\gamma^2\left(\omega_0^2 - \gamma^2\right) \quad &\text{(radicand at the peak, where $\omega_0^2 - \omega_1^2 = 2\gamma^2$; expand and group)} \\
> a_{1,\max} &= \frac{F_1/m}{2\gamma\sqrt{\omega_0^2 - \gamma^2}} \quad &\text{(Eq. 5.41)} \\
> &= \frac{F_1}{2m\gamma\,\omega} \quad &\text{($\omega$ of the damped oscillator, Section 10)} \\
> \tan\phi_1 &= -\frac{2\gamma\sqrt{\omega_0^2 - 2\gamma^2}}{2\gamma^2} \quad &\text{(phase at the peak: Eq. 5.42 with $\omega_0^2 - \omega_1^2 = 2\gamma^2$)} \\
> &= -\frac{\sqrt{\omega_0^2 - 2\gamma^2}}{\gamma} \quad &\text{(cancel $2\gamma$)} \\
> \omega_1^2 - \omega_0^2 + 2\gamma^2 &> 0 \ \text{ for every } \omega_1 > 0 \quad &\text{(if $\gamma \geq \omega_0/\sqrt2$: no peak, the amplitude only decreases)} \\
> \omega_0^2 - 2\gamma^2 &< \omega_0^2 - \gamma^2 < \omega_0^2 \quad &\text{(ordering of the three squared frequencies)}
> \end{aligned}$$
>
> $$\boxed{\omega_1 = \sqrt{\omega_0^2 - 2\gamma^2}\ \ (\gamma < \omega_0/\sqrt2),\qquad a_{1,\max} = \frac{F_1}{2m\gamma\,\omega},\qquad \sqrt{\omega_0^2 - 2\gamma^2} < \omega < \omega_0}$$
>
> **Units:** every frequency in $\mathrm{s^{-1}}$; $a_{1,\max}$ in $\mathrm{N/(kg\,s^{-2})} = \mathrm m$
> **Meaning:** this is the resonant frequency, at which the system is at resonance: it is slightly lower than the natural frequency, and for small damping it hardly differs from it (Notes.pdf, Sec. 5.4.1; [Lecture 6, Slide 14]). The peak exists only while the damping coefficient is below $\omega_0/\sqrt2$; the frequency of the free damped oscillator lies between the resonant frequency and the undamped one. The peak height has the form of Eq. 5.45 with the damped frequency $\omega$ in place of the forcing frequency. Since the tangent of the phase at the peak is negative and finite, the phase there lies between $-\pi/2$ and $0$, not at $-\pi/2$ (see the warning below). Designers usually avoid systems that operate near their resonance frequency ([Lecture 6, Slide 14]).

> [!derivation] Half-width of the resonance and the quality factor
> **Law:** first-order approximation of the radicand near the natural frequency for small damping; ratio of two amplitudes of Eq. 5.41
> **Source:** Notes.pdf, Sec. 5.4.1; Notes.pdf, Eq. 5.41; Notes.pdf, Eq. 5.45; Notes.pdf, Eq. 5.47; Notes.pdf, Eq. 5.28; [Lecture 6, Slide 14]
>
> Small damping, and forcing frequencies close to $\omega_0$.
>
> $$\begin{aligned}
> \omega_0^2 - \omega_1^2 &= \left(\omega_0 - \omega_1\right)\left(\omega_0 + \omega_1\right) \quad &\text{(difference of squares)} \\
> &\simeq 2\omega_0\left(\omega_0 - \omega_1\right) \quad &\text{($\omega_1 \simeq \omega_0$ in the second factor)} \\
> \left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2 &\simeq 4\omega_0^2\left(\omega_0 - \omega_1\right)^2 + 4\gamma^2\omega_0^2 \quad &\text{(the same approximation in the second term)} \\
> a_1 &\simeq \frac{F_1/m}{2\omega_0\sqrt{\left(\omega_0 - \omega_1\right)^2 + \gamma^2}} \quad &\text{(Eq. 5.41; take out $4\omega_0^2$)} \\
> \frac{a_1}{a_1(\omega_0)} &\simeq \frac{\gamma}{\sqrt{\left(\omega_0 - \omega_1\right)^2 + \gamma^2}} \quad &\text{(divide by its value at $\omega_1 = \omega_0$)} \\
> &= \frac{1}{\sqrt2} \quad &\text{(when the two terms are equal: $(\omega_0 - \omega_1)^2 = \gamma^2$)} \\
> \omega_1 &\simeq \omega_0 \pm \gamma \quad &\text{(square root of both sides)} \\
> a_1(\omega_0) &= \frac{F_1/m}{2\gamma\omega_0} \quad &\text{(Eq. 5.41 at $\omega_1 = \omega_0$, exact)} \\
> a_1(0) &= \frac{F_1/m}{\omega_0^2} = \frac{F_1}{k} \quad &\text{(Eq. 5.41 at $\omega_1 = 0$: a constant force; Eq. 5.47)} \\
> \frac{a_1(\omega_0)}{a_1(0)} &= \frac{\omega_0}{2\gamma} \quad &\text{(divide)} \\
> &= Q \quad &\text{(Eq. 5.28)}
> \end{aligned}$$
>
> $$\boxed{\text{half-width} \simeq \gamma\ \ (a_1 \text{ down to } 1/\sqrt2 \text{ of its peak at } \omega_1 \simeq \omega_0 \pm \gamma),\qquad \frac{a_1(\omega_0)}{a_1(0)} = Q = \frac{\omega_0}{2\gamma}}$$
>
> **Units:** frequencies in $\mathrm{s^{-1}}$; the ratios are dimensionless
> **Meaning:** $\gamma$ is the approximate half-width of the resonance peak, and the narrower the resonance the higher its peak, since the height grows as $1/\gamma$ while the width shrinks as $\gamma$ (Notes.pdf, Sec. 5.4.1; [Lecture 6, Slide 14]). The quality factor measures the sharpness of the peak: it is exactly the ratio of the amplitude at $\omega_1$ equal to $\omega_0$ to the response to a constant force. For $\gamma/\omega_0$ equal to $0.05$ the amplitude stays above $1/\sqrt2$ of its peak between $0.946\,\omega_0$ and $1.046\,\omega_0$, a half-width of $0.05\,\omega_0$ as predicted.

> [!derivation] Amplification factor and phase lag against the frequency ratio
> **Law:** Eqs. 5.41 and 5.42 written with the dimensionless ratios; limits of small, equal and large forcing frequency
> **Source:** Notes.pdf, Eq. 5.41; Notes.pdf, Eq. 5.42; Notes.pdf, Eq. 5.47; Notes.pdf Fig. 5.4; [Lecture 6, Slide 13]; [Lecture 6, Slide 14]
>
> The amplification factor is the forced amplitude divided by the static deflection $F_1/k$; the damping enters only through the ratio $\gamma/\omega_0$ and the frequency only through $\omega_1/\omega_0$.
>
> $$\begin{aligned}
> \frac{a_1\,k}{F_1} &= \frac{m\,\omega_0^2\,a_1}{F_1} \quad &\text{($k = m\,\omega_0^2$)} \\
> &= \frac{\omega_0^2}{\sqrt{\left(\omega_0^2 - \omega_1^2\right)^2 + 4\gamma^2\omega_1^2}} \quad &\text{(Eq. 5.41)} \\
> &= \frac{1}{\sqrt{\left(1 - (\omega_1/\omega_0)^2\right)^2 + 4\left(\gamma/\omega_0\right)^2\left(\omega_1/\omega_0\right)^2}} \quad &\text{(divide numerator and denominator by $\omega_0^2$)} \\
> \tan\phi_1 &= -\frac{2\left(\gamma/\omega_0\right)\left(\omega_1/\omega_0\right)}{1 - (\omega_1/\omega_0)^2} \quad &\text{(Eq. 5.42, numerator and denominator divided by $\omega_0^2$)} \\
> \frac{a_1\,k}{F_1} &\to 1,\qquad \tan\phi_1 \to 0^-,\qquad \phi_1 \to 0 \quad &\text{($\omega_1 \ll \omega_0$: the ratio tends to zero; $\cos\phi_1 > 0$)} \\
> \frac{a_1\,k}{F_1} &= \frac{\omega_0}{2\gamma} = Q,\qquad \cos\phi_1 = 0,\qquad \phi_1 = -\frac{\pi}{2} \quad &\text{($\omega_1 = \omega_0$: Eq. 5.39 has a zero left side)} \\
> \frac{a_1\,k}{F_1} &\simeq \left(\frac{\omega_0}{\omega_1}\right)^2,\qquad \tan\phi_1 \to 0^+,\qquad \phi_1 \to -\pi \quad &\text{($\omega_1 \gg \omega_0$: the fourth power of the ratio dominates; $\cos\phi_1 < 0$)} \\
> a_1 &\simeq \frac{F_1}{k}\,\frac{\omega_0^2}{\omega_1^2} = \frac{F_1}{m\,\omega_1^2} \quad &\text{(multiply by $F_1/k$; $k = m\,\omega_0^2$)}
> \end{aligned}$$
>
> $$\boxed{\frac{a_1\,k}{F_1} = \frac{1}{\sqrt{\left(1 - (\omega_1/\omega_0)^2\right)^2 + 4\left(\gamma/\omega_0\right)^2\left(\omega_1/\omega_0\right)^2}},\qquad \tan\phi_1 = -\frac{2\left(\gamma/\omega_0\right)\left(\omega_1/\omega_0\right)}{1 - (\omega_1/\omega_0)^2}}$$
>
> **Units:** both sides dimensionless
> **Meaning:** one curve for each damping ratio, as in Notes.pdf Fig. 5.4 and [Lecture 6, Slides 13-14]: every amplitude curve starts at one, the static response; for small damping it rises to a sharp peak near the frequency ratio one and then falls as the inverse square of the ratio. For damping ratios $0.05$, $0.1$, $0.25$ and $0.5$ (quality factors $10$, $5$, $2$ and $1$) the peaks are $10.01$, $5.03$, $2.07$ and $1.15$, at the frequency ratios $0.997$, $0.990$, $0.935$ and $0.707$; from the ratio $1/\sqrt2$ on there is no peak. Every phase curve goes from $0$ to $-\pi$ through $-\pi/2$ at the ratio one, more abruptly the smaller the damping. The value of the damping constant matters for the forced amplitude only near resonance (Notes.pdf, Sec. 5.4.1).

![[attachments/EM-T/t2-amplification.svg]]

> [!derivation] Which force balances the applied force
> **Law:** sizes of the inertia, damping and spring terms on the steady response
> **Source:** [Lecture 6, Slide 13]; Notes.pdf, Eq. 5.43; Notes.pdf, Eq. 5.47; Notes.pdf, Sec. 5.4.1
>
> On the steady response each term of the equation of motion is a cosine of frequency $\omega_1$; their amplitudes are compared.
>
> $$\begin{aligned}
> x_p &= a_1\cos(\omega_1 t + \phi_1) \quad &\text{(Eq. 5.43)} \\
> \lvert m\ddot x_p\rvert_{\max} &= m\,\omega_1^2\,a_1 \quad &\text{(two derivatives, each a factor $\omega_1$)} \\
> \lvert\lambda\dot x_p\rvert_{\max} &= \lambda\,\omega_1\,a_1 = 2m\gamma\,\omega_1\,a_1 \quad &\text{(one derivative; $\lambda = 2m\gamma$)} \\
> \lvert k\,x_p\rvert_{\max} &= k\,a_1 = m\,\omega_0^2\,a_1 \quad &\text{(no derivative)} \\
> m\,\omega_1^2 : 2m\gamma\,\omega_1 : m\,\omega_0^2 &= \omega_1^2 : 2\gamma\,\omega_1 : \omega_0^2 \quad &\text{(ratios of the three amplitudes, $m\,a_1$ cancelled)} \\
> k\,x_p &\simeq F_1\cos(\omega_1 t) \quad &\text{($\omega_1 \ll \omega_0$, with $\gamma$ not larger than $\omega_0$: the spring term dominates)} \\
> m\ddot x_p &\simeq F_1\cos(\omega_1 t) \quad &\text{($\omega_1 \gg \omega_0$ and $\omega_1 \gg \gamma$: the inertia term dominates)} \\
> m\ddot x_p + k\,x_p &= -m\,\omega_1^2\,x_p + m\,\omega_0^2\,x_p \quad &\text{(two derivatives of the cosine give $-\omega_1^2$; $k = m\,\omega_0^2$)} \\
> &= 0 \quad &\text{($\omega_1 = \omega_0$: the inertia and spring terms cancel exactly)} \\
> \lambda\dot x_p &= F_1\cos(\omega_1 t) \quad &\text{(the equation of motion at $\omega_1 = \omega_0$ keeps only the damper)}
> \end{aligned}$$
>
> $$\boxed{\omega_1 \ll \omega_0:\ x \simeq \frac{F_1}{k}\cos(\omega_1 t);\qquad \omega_1 = \omega_0:\ \text{damper balances the force};\qquad \omega_1 \gg \omega_0:\ x \simeq \frac{F_1}{m\,\omega_1^2}\cos(\omega_1 t - \pi)}$$
>
> **Units:** each force amplitude in $\mathrm N$; the ratios of the fifth row in $\mathrm{s^{-2}}$ each
> **Meaning:** for a slowly varying force the position is approximately the instantaneous equilibrium position under the force minus the spring force, as if the force were constant, and the oscillation is in phase with it; for a very fast force the restoring and damping forces become irrelevant and the particle moves as a free particle under the applied force, completely out of phase with it (Notes.pdf, Sec. 5.4.1; [Lecture 6, Slide 13]). At $\omega_1$ equal to $\omega_0$ the response lags by a quarter period, so the velocity is in phase with the force and only the damper resists it, which is why the damping alone sets the height of the peak.

> [!warning] "At resonance" and the phase of a quarter period
> The notes state that at resonance the phase is $-\pi/2$ (Notes.pdf, Sec. 5.4.1). This holds exactly when the forcing frequency equals the natural frequency $\omega_0$, as [Lecture 6, Slide 14] states, and for every value of the damping. At the resonant frequency of Eq. 5.46, where the amplitude peaks, the phase is slightly smaller in magnitude (the box on the resonant frequency gives its tangent); the two frequencies, and the two statements, coincide only in the limit of small damping.

## 13. Linearisation about an equilibrium

Section 6 linearised a conservative force about an equilibrium. [Lecture 6, Slide 15] takes the general case: a one-dimensional system whose nonlinear equation of motion has a force depending on the position and on the velocity, with an equilibrium configuration $x^*$, where the force vanishes at rest. Near it, the motion is that of a harmonic oscillator, and the roots of its characteristic equation decide the stability.

> [!derivation] The linearised equation of motion
> **Law:** first-order Taylor expansion of the force in its two variables about the equilibrium at rest
> **Source:** [Lecture 6, Slide 15]; Notes.pdf, Sec. 4.6; Notes.pdf, Eq. 5.20; Notes.pdf, Eq. 5.22
>
> The equation of motion is $m$ times the acceleration equal to $F(x,\dot x)$, and the equilibrium condition is that $F$ vanishes at $x^*$ with zero velocity. $\xi$ is the departure from the equilibrium, as in Section 6.
>
> $$\begin{aligned}
> m\ddot x &= F(x, \dot x),\qquad F(x^*, 0) = 0 \quad &\text{(nonlinear equation and equilibrium; [Lecture 6, Slide 15])} \\
> \xi &= x - x^* \quad &\text{(departure from the equilibrium)} \\
> \dot x &= \dot\xi,\qquad \ddot x = \ddot\xi \quad &\text{(differentiate; $x^*$ is constant)} \\
> F(x^* + \xi, \dot\xi) &= F(x^*, 0) + \left.\frac{\partial F}{\partial x}\right|_{x^*,0}\xi + \left.\frac{\partial F}{\partial\dot x}\right|_{x^*,0}\dot\xi + \dots \quad &\text{(Taylor expansion about $(x^*, 0)$: zero-order term, then one first-order term per variable)} \\
> &= \left.\frac{\partial F}{\partial x}\right|_{x^*,0}\xi + \left.\frac{\partial F}{\partial\dot x}\right|_{x^*,0}\dot\xi + \dots \quad &\text{(the zero-order term vanishes: equilibrium)} \\
> k &= -\left.\frac{\partial F}{\partial x}\right|_{x^*,0},\qquad \lambda = -\left.\frac{\partial F}{\partial\dot x}\right|_{x^*,0} \quad &\text{(names of the two constant coefficients)} \\
> m\ddot\xi &= -k\,\xi - \lambda\,\dot\xi \quad &\text{(keep only the linear terms, for $\xi$ and $\dot\xi$ small enough)} \\
> m\ddot\xi + \lambda\dot\xi + k\,\xi &= 0 \quad &\text{(move the terms to the left)} \\
> m\,p^2 + \lambda\,p + k &= 0 \quad &\text{(characteristic equation, Section 10)} \\
> p_\pm &= -\frac{\lambda}{2m} \pm \sqrt{\frac{\lambda^2}{4m^2} - \frac{k}{m}} \quad &\text{(quadratic formula; [Lecture 6, Slide 15])} \\
> k &= \frac{d^2V}{dx^2}(x^*),\qquad \lambda = 0 \quad &\text{(conservative force, Eq. 4.16: the stiffness of Section 6)}
> \end{aligned}$$
>
> $$\boxed{m\ddot\xi + \lambda\dot\xi + k\,\xi = 0,\qquad k = -\left.\frac{\partial F}{\partial x}\right|_{x^*,0},\ \ \lambda = -\left.\frac{\partial F}{\partial\dot x}\right|_{x^*,0},\qquad p_\pm = -\frac{\lambda}{2m} \pm \sqrt{\frac{\lambda^2}{4m^2} - \frac{k}{m}}}$$
>
> **Units:** $k$ in $\mathrm{N/m}$, $\lambda$ in $\mathrm{N\,s/m}$, $p_\pm$ in $\mathrm{s^{-1}}$
> **Meaning:** near any equilibrium the motion obeys a second-order linear equation with constant coefficients, just like a harmonic oscillator: minus the slope of the force with respect to the position acts as a spring stiffness, and minus its slope with respect to the velocity as a damping constant ([Lecture 6, Slide 15]). For a conservative force there is no velocity dependence and the stiffness is the curvature of the potential, as in Section 6.

> [!derivation] Stability from the roots of the linearised equation
> **Law:** modulus of a complex exponential; ordering of the real parts of the roots; double root
> **Source:** [Lecture 6, Slide 15]; [Lecture 6, Slide 3]; [Lecture 6, Slide 4]
>
> The departure is a combination of $\exp(p_+ t)$ and $\exp(p_- t)$ (Section 8). The root $p_+$ carries the plus sign, so its real part is never smaller than that of $p_-$.
>
> $$\begin{aligned}
> \lvert\exp(p\,t)\rvert &= \exp\big(\Re(p)\,t\big)\,\lvert\exp\big(i\,\Im(p)\,t\big)\rvert \quad &\text{(split the exponent into its real and imaginary parts)} \\
> &= \exp\big(\Re(p)\,t\big) \quad &\text{(Euler: unit modulus)} \\
> \Re(p_+) &< 0:\ \ \lvert\xi\rvert \leq \left(\lvert D_1\rvert + \lvert D_2\rvert\right)\exp\big(\Re(p_+)\,t\big) \to 0 \quad &\text{(both terms decay: asymptotically stable)} \\
> \Re(p_+) &= 0,\ p_+ \neq p_-:\ \ \lvert\xi\rvert \leq \lvert D_1\rvert + \lvert D_2\rvert \quad &\text{(bounded, not decaying: marginally stable)} \\
> p_+ &= p_- = 0:\ \ \xi = D_1 + D_2\,t \quad &\text{($k = \lambda = 0$: double root, Section 10; grows unless $D_2 = 0$: unstable)} \\
> \Re(p_+) &> 0:\ \ \lvert D_1\exp(p_+ t)\rvert \to \infty \quad &\text{(grows unless $D_1 = 0$: unstable)} \\
> \Re(p_\pm) &= -\frac{\lambda}{2m} < 0 \ \text{ or } \ p_\pm = -\frac{\lambda}{2m} \pm \sqrt{\frac{\lambda^2}{4m^2} - \frac{k}{m}} < 0 \quad &\text{($k > 0$, $\lambda > 0$: complex roots, or real roots with the root smaller than $\lambda/(2m)$)} \\
> p_\pm &= \pm\,i\sqrt{k/m} \quad &\text{($k > 0$, $\lambda = 0$: marginal)} \\
> p_+ &= -\frac{\lambda}{2m} + \sqrt{\frac{\lambda^2}{4m^2} - \frac{k}{m}} > -\frac{\lambda}{2m} + \frac{\lvert\lambda\rvert}{2m} \geq 0 \quad &\text{($k < 0$: the radicand exceeds $\lambda^2/(4m^2)$; unstable for any $\lambda$)} \\
> \Re(p_+) &> 0 \quad &\text{($k > 0$, $\lambda < 0$: the real part $-\lambda/(2m)$, or the larger real root, is positive: unstable)}
> \end{aligned}$$
>
> $$\boxed{\Re(p_+) < 0:\ \text{asymptotically stable};\qquad \Re(p_+) = 0,\ p_+ \neq p_-:\ \text{marginally stable (check higher orders)};\qquad \text{otherwise unstable}}$$
>
> **Units:** $\Re(p)\,t$ dimensionless
> **Meaning:** if the real part of $p_+$ is negative, any perturbation from equilibrium dies away over time and the equilibrium is asymptotically stable; if it is zero with distinct roots, the perturbation survives but does not grow without bound and the equilibrium is marginally stable, although the higher-order terms must be checked to be sure; otherwise the perturbation grows and the equilibrium is unstable ([Lecture 6, Slide 15]). In terms of the coefficients: a positive stiffness with positive damping is asymptotically stable, a positive stiffness without damping is marginal, and a negative stiffness, or a negative damping, is unstable. The conservative equilibria of Section 6 have no damping, so a minimum of the potential is only marginal for the linear test; Section 6 proved its stability from the energy, which is the check of the higher-order terms that the slide asks for.

![[attachments/EM-T/t2-linearisation.svg]]

> [!example] Linearisation of the simple pendulum ([Lecture 6, Slide 15]; Section 7)
> The pendulum of Section 7 written in the form of the slide: the coordinate is the arc length of the bob from the lowest point, $\ell$ times $\theta$, and the force along the circle is the tangential component of the weight found in Section 7. Its equilibria are $\theta$ equal to $0$ and $\pi$.
>
> | Data | Value |
> | :--- | :--- |
> | coordinate | $x = \ell\theta$ (arc length) |
> | equation | $m\ddot x = F(x) = -m g\sin(x/\ell)$ (Eq. 4.38 times $m\ell$) |
> | equilibria | $x^* = 0$ and $x^* = \pi\ell$ |

> [!derivation] Stiffness of the pendulum at its two equilibria
> **Law:** linearised equation of [Lecture 6, Slide 15]; chain rule
> **Source:** [Lecture 6, Slide 15]; Notes.pdf, Eq. 4.38; Notes.pdf, Eq. 4.46
>
> $$\begin{aligned}
> \frac{\partial F}{\partial x} &= -m g\cos\left(\frac{x}{\ell}\right)\frac{1}{\ell} \quad &\text{(chain rule: derivative of the sine times that of $x/\ell$)} \\
> \frac{\partial F}{\partial\dot x} &= 0 \quad &\text{(no velocity dependence)} \\
> k &= \frac{m g}{\ell} \quad &\text{(at $x^* = 0$: $\cos 0 = 1$, sign changed)} \\
> p_\pm &= \pm\,i\sqrt{g/\ell} \quad &\text{(previous box with $\lambda = 0$: marginal; Eq. 4.46)} \\
> k &= -\frac{m g}{\ell} \quad &\text{(at $x^* = \pi\ell$: $\cos\pi = -1$)} \\
> p_\pm &= \pm\sqrt{g/\ell} \quad &\text{(one positive real root: unstable)}
> \end{aligned}$$
>
> $$\boxed{x^* = 0:\ k = \frac{m g}{\ell} > 0,\ p_\pm = \pm\,i\sqrt{g/\ell};\qquad x^* = \pi\ell:\ k = -\frac{m g}{\ell} < 0,\ p_\pm = \pm\sqrt{g/\ell}}$$
>
> **Units:** $k$ in $\mathrm{kg\,(m/s^2)/m} = \mathrm{N/m}$; $p$ in $\mathrm{s^{-1}}$
> **Meaning:** the inverted pendulum is unstable already for the linear test; the hanging pendulum is only marginally stable for it, and the energy argument of Sections 6 and 7 (a strict minimum of the potential) confirms its stability. The roots are those found in Section 7, as they must be.

## 14. Extension: the bead on a rotating hoop

> [!info] Extension: an example beyond Lecture 6
> Neither Notes.pdf, Chapter 5, nor the slides of Lecture 6 contain this example: the deck closes with the general linearisation of [Lecture 6, Slide 15]. It is added because it gathers every tool of this topic, an equation of motion from Newton's second law, a first integral with an effective potential, equilibria with their stability, small oscillations, and an equilibrium that changes its stability when a parameter crosses a critical value (a bifurcation). The problem is worked in the inertial frame $S_0$ with a basis that turns with the hoop, so no inertia force is needed; the same equation can be written in the frame of the hoop with the inertia forces of relative motion, which belong to Topic 5 (Notes.pdf, Ch. 3; Notes.pdf, Sec. 4.9). The reaction of a smooth wire is a constraint force, the subject of Topic 3 (Notes.pdf, Ch. 6); here only its direction is used.

> [!example] Bead on a hoop turning about its vertical diameter
> A small bead $P$ of mass $m$ slides without friction on a circular hoop of radius $b$ whose centre $O$ is fixed. The hoop is driven so that it turns about its vertical diameter at the constant rate $\Omega$. The position of the bead on the hoop is the angle $\theta$ from the downward vertical, measured in the plane of the hoop. Find the equation of motion, the equilibria and their stability as functions of $\Omega$, and the frequencies of the small oscillations.
>
> | Data | Value |
> | :--- | :--- |
> | inertial frame | $S_0 : \{O;\mathbf i,\mathbf j,\mathbf k\}$, $\mathbf k$ vertical upwards along the axis of rotation |
> | frame of the hoop | $S_h : \{O;\mathbf i_h,\mathbf j_h,\mathbf k\}$; $\mathbf i_h$ horizontal in the plane of the hoop, $\mathbf j_h$ normal to it; $\mathbf i_h$ along $\mathbf i$ at $t = 0$ |
> | rotation | angle $\Omega t$ from $\mathbf i$ to $\mathbf i_h$ about $\mathbf k$; $\Omega$ constant |
> | bead | mass $m$, at distance $b$ from $O$, angle $\theta$ from $-\mathbf k$ towards $\mathbf i_h$ |
> | forces | weight $-m g\,\mathbf k$; reaction $\mathbf N$ of the smooth hoop, normal to the hoop |

![[attachments/EM-T/t2-hoop.svg]]

> [!derivation] Extension: basis of the hoop and its change of basis matrix
> **Law:** simple rotation about the vertical axis; change of basis matrix with the rotated unit vectors as columns; determinant and orthogonality; derivatives of the rotating unit vectors
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.32
>
> View along $\mathbf k$, which points out of the paper (⊙), looking down on the hoop. The angle $\Omega t$ lies between $\mathbf i$ and $\mathbf i_h$, counterclockwise. In the right triangle of unit hypotenuse $\mathbf i_h$, the leg along $\mathbf i$ is adjacent to $\Omega t$ (cosine) and the leg along $\mathbf j$ is opposite (sine). $\mathbf j_h$ is $\mathbf i_h$ turned a quarter turn counterclockwise about $\mathbf k$; the same angle lies between $\mathbf j$ and $\mathbf j_h$, its leg along $\mathbf j$ is adjacent and its leg along $\mathbf i$ is opposite and points along $-\mathbf i$: by the right-hand rule a counterclockwise turn about $\mathbf k$ (⊙) carries $\mathbf j$ towards $-\mathbf i$, which is the minus sign of entry $(1,2)$.
>
> $$\begin{aligned}
> \mathbf i_h &= \cos(\Omega t)\,\mathbf i + \sin(\Omega t)\,\mathbf j \quad &\text{(adjacent and opposite legs)} \\
> \mathbf j_h &= -\sin(\Omega t)\,\mathbf i + \cos(\Omega t)\,\mathbf j \quad &\text{(opposite leg along $-\mathbf i$, adjacent leg along $\mathbf j$)} \\
> [{}_0R_h] &= \begin{pmatrix} \cos(\Omega t) & -\sin(\Omega t) & 0 \cr \sin(\Omega t) & \cos(\Omega t) & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf i_h$, $\mathbf j_h$, $\mathbf k$ in $\mathcal B_0$, Eq. 1.13; Eq. 1.20 with the angle $\Omega t$)} \\
> \det[{}_0R_h] &= 1\cdot\left(\cos^2(\Omega t) - \left(-\sin(\Omega t)\right)\sin(\Omega t)\right) \quad &\text{(expand along the third row)} \\
> &= \cos^2(\Omega t) + \sin^2(\Omega t) \quad &\text{(simplify the signs)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_h][{}_0R_h]^T\right)_{11} &= \cos^2(\Omega t) + \sin^2(\Omega t) + 0 \quad &\text{(row 1 times row 1)} \\
> &= 1 \quad &\text{(Pythagoras)} \\
> \left([{}_0R_h][{}_0R_h]^T\right)_{12} &= \cos(\Omega t)\sin(\Omega t) - \sin(\Omega t)\cos(\Omega t) + 0 \quad &\text{(row 1 times row 2)} \\
> &= 0 \quad &\text{(the two products cancel)} \\
> \frac{d\mathbf i_h}{dt} &= -\Omega\sin(\Omega t)\,\mathbf i + \Omega\cos(\Omega t)\,\mathbf j \quad &\text{(chain rule: the derivative of $\Omega t$ is $\Omega$; $\mathbf i$, $\mathbf j$ fixed)} \\
> &= \Omega\,\mathbf j_h \quad &\text{(second row)} \\
> \frac{d\mathbf j_h}{dt} &= -\Omega\cos(\Omega t)\,\mathbf i - \Omega\sin(\Omega t)\,\mathbf j \quad &\text{(chain rule)} \\
> &= -\Omega\,\mathbf i_h \quad &\text{(first row)} \\
> \Omega\,\mathbf k\times\mathbf i_h &= \Omega\cos(\Omega t)\,\mathbf k\times\mathbf i + \Omega\sin(\Omega t)\,\mathbf k\times\mathbf j \quad &\text{(distribute, Eq. 1.32)} \\
> &= \Omega\cos(\Omega t)\,\mathbf j - \Omega\sin(\Omega t)\,\mathbf i \quad &\text{($\mathbf k\times\mathbf i = \mathbf j$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> &= \Omega\,\mathbf j_h \quad &\text{(the same as the derivative of $\mathbf i_h$: Eq. 1.62 with the angular velocity $\Omega\,\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_h] = \begin{bmatrix} \cos\Omega t & -\sin\Omega t & 0 \\ \sin\Omega t & \cos\Omega t & 0 \\ 0 & 0 & 1 \end{bmatrix},\ \ \det = 1;\qquad \frac{d\mathbf i_h}{dt} = \Omega\,\mathbf j_h,\qquad \frac{d\mathbf j_h}{dt} = -\Omega\,\mathbf i_h}$$
>
> **Units:** the matrix is dimensionless; the derivatives of the unit vectors in $\mathrm{rad/s}$
> **Meaning:** the remaining entries of the product of the matrix with its transpose follow the same way ($(2,2)$ by Pythagoras, $(3,3)$ equal to one, $(1,3)$ and $(2,3)$ zero), so $\mathcal B_h$ is orthonormal, and with determinant one it is right-handed. The hoop basis turns about $\mathbf k$ at the rate $\Omega$, while $\mathbf k$ itself stays fixed.

![[attachments/EM-T/t2-hoop-top.svg]]

> [!derivation] Extension: position of the bead and the unit vectors in the plane of the hoop
> **Law:** right triangle of the radius with the vertical in the plane of the hoop; derivative with respect to the angle; orthonormality checks
> **Source:** Notes.pdf, Sec. 4.7; Notes.pdf, Eq. 1.24
>
> Plane of the hoop, $\mathbf j_h$ normal to it: $O$, the bead $P$ and the foot $H$ of the perpendicular from $P$ to the vertical diameter form a right triangle, right-angled at $H$, with hypotenuse $OP$ of length $b$ and the angle $\theta$ at $O$ between the downward vertical $OH$ and the radius. As for the pendulum of Section 7, the leg $OH$ is adjacent to $\theta$ and points along $-\mathbf k$, the leg $HP$ is opposite and points along $\mathbf i_h$.
>
> $$\begin{aligned}
> \mathbf r_0^P &= b\sin\theta\,\mathbf i_h - b\cos\theta\,\mathbf k \quad &\text{(opposite leg along $\mathbf i_h$; adjacent leg along $-\mathbf k$)} \\
> \mathbf u_r &= \sin\theta\,\mathbf i_h - \cos\theta\,\mathbf k \quad &\text{(unit vector from $O$ to $P$: divide by $b$)} \\
> \mathbf u_\theta &= \frac{\partial\mathbf u_r}{\partial\theta} \quad &\text{(tangent to the hoop, in the sense of growing $\theta$)} \\
> &= \cos\theta\,\mathbf i_h + \sin\theta\,\mathbf k \quad &\text{(derivatives of $\sin\theta$ and $-\cos\theta$)} \\
> \mathbf u_r\cdot\mathbf u_\theta &= \sin\theta\cos\theta - \cos\theta\sin\theta \quad &\text{(dot product in $\mathcal B_h$, Eq. 1.24)} \\
> &= 0 \quad &\text{(the products cancel)} \\
> \mathbf u_\theta\cdot\mathbf u_\theta &= \cos^2\theta + \sin^2\theta \quad &\text{(dot product)} \\
> &= 1 \quad &\text{(Pythagoras: unit length; the same for $\mathbf u_r$)} \\
> \sin\theta\,\mathbf u_r + \cos\theta\,\mathbf u_\theta &= \left(\sin^2\theta + \cos^2\theta\right)\mathbf i_h + \left(-\sin\theta\cos\theta + \cos\theta\sin\theta\right)\mathbf k \quad &\text{(combine the two rows)} \\
> &= \mathbf i_h \quad &\text{(Pythagoras; the $\mathbf k$ terms cancel)} \\
> -\cos\theta\,\mathbf u_r + \sin\theta\,\mathbf u_\theta &= \mathbf k \quad &\text{(the same steps)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = b\,\mathbf u_r,\qquad \mathbf u_r = \sin\theta\,\mathbf i_h - \cos\theta\,\mathbf k,\qquad \mathbf u_\theta = \cos\theta\,\mathbf i_h + \sin\theta\,\mathbf k;\qquad \mathbf i_h = \sin\theta\,\mathbf u_r + \cos\theta\,\mathbf u_\theta,\ \ \mathbf k = -\cos\theta\,\mathbf u_r + \sin\theta\,\mathbf u_\theta}$$
>
> **Units:** $\mathrm m$ for the position; the unit vectors are dimensionless
> **Meaning:** $\mathbf u_r$, $\mathbf u_\theta$ and $\mathbf j_h$ are three orthonormal vectors ($\mathbf j_h$ is normal to the plane that contains the other two); the last two rows invert the first ones and are used to project the acceleration and the weight. At $\theta$ equal to zero the bead is at the bottom of the hoop.

![[attachments/EM-T/t2-hoop-plane.svg]]

> [!derivation] Extension: velocity and acceleration of the bead
> **Law:** definition of velocity and acceleration in $S_0$; product rule; chain rule; derivatives of the hoop basis
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4; Notes.pdf, Eq. 1.64
>
> $$\begin{aligned}
> \mathbf v_0^P &= \left.\frac{d}{dt}\left(b\sin\theta\,\mathbf i_h - b\cos\theta\,\mathbf k\right)\right|_0 \quad &\text{(Eq. 2.3)} \\
> &= b\cos\theta\,\dot\theta\,\mathbf i_h + b\sin\theta\,\frac{d\mathbf i_h}{dt} + b\sin\theta\,\dot\theta\,\mathbf k \quad &\text{(product rule, Eq. 1.64; chain rule on the sine and the cosine; $\mathbf k$ fixed)} \\
> &= b\cos\theta\,\dot\theta\,\mathbf i_h + b\,\Omega\sin\theta\,\mathbf j_h + b\sin\theta\,\dot\theta\,\mathbf k \quad &\text{(derivative of $\mathbf i_h$)} \\
> &= b\dot\theta\,\mathbf u_\theta + b\,\Omega\sin\theta\,\mathbf j_h \quad &\text{(group the $\mathbf i_h$ and $\mathbf k$ terms into $\mathbf u_\theta$)} \\
> \frac{d\mathbf u_\theta}{dt} &= -\sin\theta\,\dot\theta\,\mathbf i_h + \cos\theta\,\frac{d\mathbf i_h}{dt} + \cos\theta\,\dot\theta\,\mathbf k \quad &\text{(product rule on $\mathbf u_\theta$; chain rule)} \\
> &= -\dot\theta\,\mathbf u_r + \Omega\cos\theta\,\mathbf j_h \quad &\text{(derivative of $\mathbf i_h$; group the rest into $-\mathbf u_r$)} \\
> \mathbf a_0^P &= b\ddot\theta\,\mathbf u_\theta + b\dot\theta\,\frac{d\mathbf u_\theta}{dt} + b\,\Omega\cos\theta\,\dot\theta\,\mathbf j_h + b\,\Omega\sin\theta\,\frac{d\mathbf j_h}{dt} \quad &\text{(Eq. 2.4: product rule on the two terms of the velocity; $\Omega$ constant)} \\
> &= b\ddot\theta\,\mathbf u_\theta - b\dot\theta^2\,\mathbf u_r + b\,\Omega\dot\theta\cos\theta\,\mathbf j_h + b\,\Omega\dot\theta\cos\theta\,\mathbf j_h - b\,\Omega^2\sin\theta\,\mathbf i_h \quad &\text{(substitute the two derivatives of unit vectors)} \\
> &= b\ddot\theta\,\mathbf u_\theta - b\dot\theta^2\,\mathbf u_r + 2b\,\Omega\dot\theta\cos\theta\,\mathbf j_h - b\,\Omega^2\sin\theta\left(\sin\theta\,\mathbf u_r + \cos\theta\,\mathbf u_\theta\right) \quad &\text{(add the $\mathbf j_h$ terms; $\mathbf i_h$ in terms of $\mathbf u_r$, $\mathbf u_\theta$)} \\
> &= -\left(b\dot\theta^2 + b\,\Omega^2\sin^2\theta\right)\mathbf u_r + \left(b\ddot\theta - b\,\Omega^2\sin\theta\cos\theta\right)\mathbf u_\theta + 2b\,\Omega\dot\theta\cos\theta\,\mathbf j_h \quad &\text{(group by unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = b\dot\theta\,\mathbf u_\theta + b\,\Omega\sin\theta\,\mathbf j_h,\qquad \mathbf a_0^P = -b\left(\dot\theta^2 + \Omega^2\sin^2\theta\right)\mathbf u_r + b\left(\ddot\theta - \Omega^2\sin\theta\cos\theta\right)\mathbf u_\theta + 2b\,\Omega\dot\theta\cos\theta\,\mathbf j_h}$$
>
> **Units:** $\mathrm{m/s}$ for every term of the velocity; $\mathrm{m/s^2}$ for every term of the acceleration ($\mathrm m\cdot\mathrm{s^{-2}}$)
> **Meaning:** the velocity has a part along the hoop, $b\dot\theta$, and a part normal to its plane, the speed $b\,\Omega\sin\theta$ of a point at the distance $b\sin\theta$ from the axis carried round by the hoop. With $\Omega$ equal to zero the velocity and acceleration are those of the pendulum of Section 7 with $b$ for $\ell$.

> [!derivation] Extension: equation of motion and the reaction of the hoop
> **Law:** Newton's second law projected on $\mathbf u_r$, $\mathbf u_\theta$ and $\mathbf j_h$; the reaction of a smooth hoop has no tangential component
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Ch. 6; Notes.pdf, Eq. 4.38
>
> The bead slides without friction, so the hoop can only push it perpendicularly to the wire: along $\mathbf u_r$ and along $\mathbf j_h$, never along $\mathbf u_\theta$.
>
> $$\begin{aligned}
> -m g\,\mathbf k &= m g\cos\theta\,\mathbf u_r - m g\sin\theta\,\mathbf u_\theta \quad &\text{(weight; $\mathbf k$ in terms of $\mathbf u_r$, $\mathbf u_\theta$)} \\
> \mathbf N &= N_r\,\mathbf u_r + N_h\,\mathbf j_h \quad &\text{(smooth hoop)} \\
> m\,\mathbf a_0^P &= -m g\,\mathbf k + \mathbf N \quad &\text{(second law, Eq. 4.4)} \\
> \mathbf u_\theta:\quad m b\left(\ddot\theta - \Omega^2\sin\theta\cos\theta\right) &= -m g\sin\theta \quad &\text{(dot-multiply by $\mathbf u_\theta$)} \\
> \ddot\theta &= -\frac{g}{b}\sin\theta + \Omega^2\sin\theta\cos\theta \quad &\text{(divide by $m b$; rearrange)} \\
> \mathbf u_r:\quad -m b\left(\dot\theta^2 + \Omega^2\sin^2\theta\right) &= m g\cos\theta + N_r \quad &\text{(dot-multiply by $\mathbf u_r$)} \\
> N_r &= -m b\dot\theta^2 - m b\,\Omega^2\sin^2\theta - m g\cos\theta \quad &\text{(solve)} \\
> \mathbf j_h:\quad N_h &= 2m b\,\Omega\dot\theta\cos\theta \quad &\text{(dot-multiply by $\mathbf j_h$: the weight has no component)}
> \end{aligned}$$
>
> $$\boxed{\ddot\theta = -\frac{g}{b}\sin\theta + \Omega^2\sin\theta\cos\theta,\qquad N_r = -m\left(b\dot\theta^2 + b\,\Omega^2\sin^2\theta + g\cos\theta\right),\qquad N_h = 2m b\,\Omega\dot\theta\cos\theta}$$
>
> **Units:** $\mathrm{s^{-2}}$ in the equation of motion; $\mathrm N$ for the reactions
> **Meaning:** the mass drops out of the equation of motion; with $\Omega$ equal to zero it is the pendulum equation, Eq. 4.38. The rotation adds a term that pushes the bead away from the axis. The reaction normal to the plane of the hoop is the push of the driven hoop that keeps the bead turning with it; it vanishes when the bead does not move along the hoop.

![[attachments/EM-T/t2-hoop-fbd.svg]]

> [!derivation] Extension: first integral and effective potential
> **Law:** multiplication by $\dot\theta$; chain rule; integration in time with Barrow's rule; power of the reaction of the hoop
> **Source:** Notes.pdf, Eq. 4.39; Notes.pdf, Sec. 4.5.1; Notes.pdf, Eq. 4.2
>
> $$\begin{aligned}
> \dot\theta\,\ddot\theta + \frac{g}{b}\sin\theta\,\dot\theta - \Omega^2\sin\theta\cos\theta\,\dot\theta &= 0 \quad &\text{(multiply the equation of motion by $\dot\theta$)} \\
> \frac{d}{dt}\left(\tfrac12\dot\theta^2\right) &= \dot\theta\,\ddot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(-\frac{g}{b}\cos\theta\right) &= \frac{g}{b}\sin\theta\,\dot\theta \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\tfrac12\Omega^2\sin^2\theta\right) &= \Omega^2\sin\theta\cos\theta\,\dot\theta \quad &\text{(chain rule twice: square, then sine)} \\
> \frac{d}{dt}\left(\tfrac12\dot\theta^2 - \frac{g}{b}\cos\theta - \tfrac12\Omega^2\sin^2\theta\right) &= 0 \quad &\text{(the first row is the sum of the three derivatives)} \\
> \left[\tfrac12\dot\theta^2 - \frac{g}{b}\cos\theta - \tfrac12\Omega^2\sin^2\theta\right]_0^t &= 0 \quad &\text{(integrate from $0$ to $t$; Barrow)} \\
> \tfrac12 m b^2\dot\theta^2 + m g b\left(1 - \cos\theta\right) - \tfrac12 m b^2\Omega^2\sin^2\theta &= \text{const} \quad &\text{(multiply by $m b^2$ and add the constant $m g b$)} \\
> V_{\mathrm{eff}}(\theta) &= m g b\left(1 - \cos\theta\right) - \tfrac12 m b^2\Omega^2\sin^2\theta \quad &\text{(name the terms that depend on $\theta$ only)} \\
> -\frac{dV_{\mathrm{eff}}}{d\theta} &= -m g b\sin\theta + m b^2\Omega^2\sin\theta\cos\theta \quad &\text{(derivative; chain rule)} \\
> &= m b^2\,\ddot\theta \quad &\text{(the equation of motion times $m b^2$)} \\
> T &= \tfrac12 m\,\mathbf v_0^P\cdot\mathbf v_0^P \quad &\text{(kinetic energy, Eq. 4.2)} \\
> &= \tfrac12 m b^2\dot\theta^2 + \tfrac12 m b^2\Omega^2\sin^2\theta \quad &\text{(velocity of the previous boxes; $\mathbf u_\theta\cdot\mathbf j_h = 0$)} \\
> E - m b^2\Omega^2\sin^2\theta &= \tfrac12 m b^2\dot\theta^2 + V_{\mathrm{eff}}(\theta) \quad &\text{($E$ is $T$ plus the potential $m g b(1 - \cos\theta)$ of the weight)} \\
> \mathbf N\cdot\mathbf v_0^P &= N_h\,b\,\Omega\sin\theta \quad &\text{(power of the reaction: only $\mathbf j_h$ survives)} \\
> &= 2m b^2\Omega^2\dot\theta\sin\theta\cos\theta \quad &\text{(previous box)} \\
> \frac{d}{dt}\left(m b^2\Omega^2\sin^2\theta\right) &= 2m b^2\Omega^2\dot\theta\sin\theta\cos\theta \quad &\text{(chain rule: the same as the power)}
> \end{aligned}$$
>
> $$\boxed{\tfrac12 m b^2\dot\theta^2 + V_{\mathrm{eff}}(\theta) = \text{const},\qquad V_{\mathrm{eff}}(\theta) = m g b\left(1 - \cos\theta\right) - \tfrac12 m b^2\Omega^2\sin^2\theta,\qquad m b^2\ddot\theta = -\frac{dV_{\mathrm{eff}}}{d\theta}}$$
>
> **Units:** $\mathrm J$ for every term ($\mathrm{kg\,m^2\,s^{-2}}$); $\mathrm W$ for the power
> **Meaning:** the motion along the hoop is that of a one-dimensional system with the coordinate $\theta$, the inertia $m b^2$ and the potential $V_{\mathrm{eff}}$: the gravity well of the pendulum minus a term that grows away from the axis. This constant is not the mechanical energy: the kinetic energy also contains the motion carried by the hoop, and the reaction normal to the hoop has a nonzero power, so the motor that keeps the rate constant feeds energy in and out (Notes.pdf, Sec. 4.5.1: the energy is conserved only when the non-conservative forces do no work). By Section 5 the mechanical energy changes at the rate of that power, and so does the subtracted term $m b^2\Omega^2\sin^2\theta$ (last row): their difference, the first integral, stays constant.

> [!derivation] Extension: equilibria of the bead and their stability
> **Law:** critical points of the effective potential; sign of its second derivative
> **Source:** Notes.pdf, Sec. 4.6; [Lecture 2, Slide 22]; [Lecture 6, Slide 15]
>
> $\Omega_c$ is the critical rate, the square root of $g/b$.
>
> $$\begin{aligned}
> \frac{dV_{\mathrm{eff}}}{d\theta} &= m g b\sin\theta - m b^2\Omega^2\sin\theta\cos\theta \quad &\text{(previous box)} \\
> &= m b^2\sin\theta\left(\Omega_c^2 - \Omega^2\cos\theta\right) \quad &\text{(take out $m b^2\sin\theta$; $g/b = \Omega_c^2$)} \\
> \sin\theta &= 0:\ \ \theta = 0,\ \ \theta = \pi \quad &\text{(first factor: bottom and top of the hoop, for every $\Omega$)} \\
> \cos\theta_e &= \frac{\Omega_c^2}{\Omega^2} \quad &\text{(second factor: $\pm\theta_e$, real only if $\Omega > \Omega_c$)} \\
> \frac{d^2V_{\mathrm{eff}}}{d\theta^2} &= m g b\cos\theta - m b^2\Omega^2\left(\cos^2\theta - \sin^2\theta\right) \quad &\text{(product rule on $\sin\theta\cos\theta$)} \\
> \frac{d^2V_{\mathrm{eff}}}{d\theta^2}(0) &= m b^2\left(\Omega_c^2 - \Omega^2\right) \quad &\text{($\cos 0 = 1$, $\sin 0 = 0$)} \\
> \frac{d^2V_{\mathrm{eff}}}{d\theta^2}(\pi) &= -m b^2\left(\Omega_c^2 + \Omega^2\right) < 0 \quad &\text{($\cos\pi = -1$: always a maximum)} \\
> \frac{d^2V_{\mathrm{eff}}}{d\theta^2}(\theta_e) &= m b^2\left(\Omega_c^2\cos\theta_e - 2\Omega^2\cos^2\theta_e + \Omega^2\right) \quad &\text{($\cos^2 - \sin^2 = 2\cos^2 - 1$)} \\
> &= m b^2\left(\Omega_c^2\cos\theta_e - 2\Omega_c^2\cos\theta_e + \Omega^2\right) \quad &\text{($\Omega^2\cos\theta_e = \Omega_c^2$)} \\
> &= m b^2\left(\Omega^2 - \Omega_c^2\cos\theta_e\right) \quad &\text{(group)} \\
> &= m b^2\,\Omega^2\left(1 - \cos^2\theta_e\right) \quad &\text{($\Omega_c^2 = \Omega^2\cos\theta_e$ again)} \\
> &= m b^2\,\Omega^2\sin^2\theta_e > 0 \quad &\text{(Pythagoras: a minimum whenever it exists)}
> \end{aligned}$$
>
> $$\boxed{\Omega < \Omega_c:\ \theta = 0 \text{ stable},\ \theta = \pi \text{ unstable};\qquad \Omega > \Omega_c:\ \theta = 0,\ \pi \text{ unstable},\ \pm\theta_e \text{ stable},\ \cos\theta_e = \frac{\Omega_c^2}{\Omega^2},\qquad \Omega_c = \sqrt{g/b}}$$
>
> **Units:** $\Omega$, $\Omega_c$ in $\mathrm{rad/s}$; the derivatives of $V_{\mathrm{eff}}$ in $\mathrm{J/rad}$ and $\mathrm{J/rad^2}$
> **Meaning:** below the critical rate the bead rests at the bottom as on a still hoop; above it the bottom becomes a maximum of the effective potential and the bead settles at one of two symmetric positions up the hoop, higher the faster the rotation, which approach the horizontal through $O$ as $\Omega$ grows without bound. For a hoop of radius $0.5\ \mathrm m$ the critical rate is $4.43\ \mathrm{rad/s}$, about $42$ revolutions per minute; at twice that rate the stable positions are at $75.5^\circ$ from the bottom.

![[attachments/EM-T/t2-hoop-potential.svg]]

> [!derivation] Extension: small oscillations of the bead
> **Law:** linearisation about an equilibrium (Section 13) with $\theta$ for $x$ and $m b^2$ for $m$
> **Source:** [Lecture 6, Slide 15]; Notes.pdf, Eq. 5.6
>
> The equation $m b^2\ddot\theta$ equal to minus the derivative of the effective potential has no velocity dependence, so the linearised equation has no damping and its stiffness is the second derivative of $V_{\mathrm{eff}}$ at the equilibrium.
>
> $$\begin{aligned}
> m b^2\,\ddot\xi + \frac{d^2V_{\mathrm{eff}}}{d\theta^2}(\theta^*_{\mathrm{eq}})\,\xi &= 0 \quad &\text{(Section 13: $\xi$ the departure from the equilibrium $\theta^*_{\mathrm{eq}}$)} \\
> \omega_{\mathrm{eq}}^2 &= \frac{1}{m b^2}\,\frac{d^2V_{\mathrm{eff}}}{d\theta^2}(\theta^*_{\mathrm{eq}}) \quad &\text{(Eq. 5.6: divide by $m b^2$, stable equilibria only)} \\
> \omega_{\mathrm{eq}} &= \sqrt{\Omega_c^2 - \Omega^2} \quad &\text{(at $\theta^*_{\mathrm{eq}} = 0$, for $\Omega < \Omega_c$)} \\
> \omega_{\mathrm{eq}} &= \Omega\sin\theta_e \quad &\text{(at $\pm\theta_e$, for $\Omega > \Omega_c$: previous box)} \\
> &= \sqrt{\Omega^2 - \Omega_c^4/\Omega^2} \quad &\text{($\sin^2\theta_e = 1 - \cos^2\theta_e = 1 - \Omega_c^4/\Omega^4$)}
> \end{aligned}$$
>
> $$\boxed{\theta = 0,\ \Omega < \Omega_c:\ \ \omega_{\mathrm{eq}} = \sqrt{\Omega_c^2 - \Omega^2};\qquad \pm\theta_e,\ \Omega > \Omega_c:\ \ \omega_{\mathrm{eq}} = \Omega\sin\theta_e = \sqrt{\Omega^2 - \Omega_c^4/\Omega^2}}$$
>
> **Units:** $\mathrm{rad/s}$
> **Meaning:** both frequencies fall to zero as the rate approaches the critical one from either side: the restoring stiffness vanishes there, and the linear test of Section 13 is marginal. At zero rate the first one is the pendulum frequency, the square root of $g/b$. For the hoop of radius $0.5\ \mathrm m$ at half the critical rate the bead oscillates about the bottom at $3.84\ \mathrm{rad/s}$, and at twice the critical rate about $\pm\theta_e$ at $8.58\ \mathrm{rad/s}$.

> [!derivation] Extension: the critical rate and the bifurcation
> **Law:** Taylor expansions to fourth order (higher-order terms when the second derivative vanishes); branch of equilibria near the critical rate
> **Source:** [Lecture 6, Slide 15]; Notes.pdf, Sec. 4.6
>
> $$\begin{aligned}
> 1 - \cos\theta &= \frac{\theta^2}{2} - \frac{\theta^4}{24} + O(\theta^6) \quad &\text{(Taylor series of the cosine)} \\
> \sin\theta &= \theta - \frac{\theta^3}{6} + O(\theta^5) \quad &\text{(Taylor series of the sine)} \\
> \sin^2\theta &= \theta^2 - 2\,\theta\,\frac{\theta^3}{6} + O(\theta^6) \quad &\text{(square: the cross term)} \\
> &= \theta^2 - \frac{\theta^4}{3} + O(\theta^6) \quad &\text{(arithmetic)} \\
> V_{\mathrm{eff}} &= m g b\left(1 - \cos\theta\right) - \tfrac12 m g b\sin^2\theta \quad &\text{(at $\Omega = \Omega_c$: $m b^2\Omega_c^2 = m g b$)} \\
> &= m g b\left(\frac{\theta^2}{2} - \frac{\theta^4}{24} - \frac{\theta^2}{2} + \frac{\theta^4}{6}\right) + O(\theta^6) \quad &\text{(substitute both series)} \\
> &= \frac{m g b}{8}\,\theta^4 + O(\theta^6) \quad &\text{(the squares cancel; $\tfrac16 - \tfrac1{24} = \tfrac18$)} \\
> \cos\theta_e &\simeq 1 - \frac{\theta_e^2}{2} \quad &\text{(near the critical rate $\theta_e$ is small)} \\
> \frac{\theta_e^2}{2} &\simeq 1 - \frac{\Omega_c^2}{\Omega^2} \quad &\text{(the previous row equals $\Omega_c^2/\Omega^2$: equilibrium condition)} \\
> &= \frac{\left(\Omega - \Omega_c\right)\left(\Omega + \Omega_c\right)}{\Omega^2} \quad &\text{(common denominator; difference of squares)} \\
> &\simeq \frac{2\left(\Omega - \Omega_c\right)}{\Omega_c} \quad &\text{($\Omega \simeq \Omega_c$ in the other factors)} \\
> \theta_e &\simeq \pm 2\sqrt{\frac{\Omega - \Omega_c}{\Omega_c}} \quad &\text{(square root)}
> \end{aligned}$$
>
> $$\boxed{\Omega = \Omega_c:\ V_{\mathrm{eff}} \simeq \frac{m g b}{8}\,\theta^4 \ \text{(a flat minimum, stable)};\qquad \Omega \gtrsim \Omega_c:\ \theta_e \simeq \pm 2\sqrt{\frac{\Omega - \Omega_c}{\Omega_c}}}$$
>
> **Units:** $\mathrm J$ for the potential; $\theta_e$ in radians (a quotient of rates)
> **Meaning:** at the critical rate the bottom of the hoop is still a strict minimum, now of fourth order, so the energy argument of Section 6 makes it stable although the linear test is marginal: this is the case where the higher-order terms must be checked ([Lecture 6, Slide 15]). As the rate crosses $\Omega_c$ the single stable equilibrium at the bottom loses its stability and two new stable equilibria branch off from it, growing like the square root of the excess rate: a pitchfork bifurcation, drawn in the bifurcation diagram below. For $\Omega$ equal to $1.1\,\Omega_c$ the estimate gives $0.63\ \mathrm{rad}$, against the exact $0.60\ \mathrm{rad}$ from the arccosine.

![[attachments/EM-T/t2-hoop-bifurcation.svg]]

> [!key] Summary of Topic 2
> - In an inertial frame the second law ties the rate of change of the linear momentum to the resultant force; projected on a basis it gives the equations of motion, whose integration with the initial position and velocity yields the trajectory (Sections 1 to 3).
> - Dotting the second law with the velocity gives the theorem of kinetic energy: the power of the forces changes the kinetic energy, and the work of a force is the time integral of its power (Section 4).
> - A force whose work does not depend on the path derives from a potential energy, the force is minus its gradient, and the curl test decides whether it exists; when every working force is conservative the mechanical energy is constant, and otherwise it changes at the rate of the power of the non-conservative forces (Sections 4 and 5).
> - In one dimension the energy diagram shows the allowed regions and the turning points; the equilibria are the critical points of the potential, the minima are stable and the maxima unstable (Section 6).
> - The simple pendulum gathers these tools: kinematics in a polar basis, the tension from the radial equation, a first integral, oscillations and rotations, and the linearised equation for small oscillations (Section 7).
> - The harmonic oscillator has a linear equation with constant coefficients, solved through its characteristic equation: an undamped oscillation of amplitude and phase set by the initial conditions, with a period independent of the amplitude; complex exponentials hold the two constants in one complex amplitude (Sections 8 and 9).
> - The damping ratio decides the free motion: below one a decaying oscillation at a frequency slightly lower than the natural one, with a relaxation time and a quality factor; above one two decaying exponentials; at one the fastest return to equilibrium (Section 10).
> - Under a periodic force the transient dies and the response follows the force at its own frequency, with an amplitude and a phase lag fixed by the frequency ratio and the damping ratio; the amplitude peaks at the resonant frequency, with a height set by the damping, and the phase lag passes a quarter period when the forcing frequency equals the natural one (Sections 11 and 12).
> - Near an equilibrium any one-dimensional system is linearised into a harmonic oscillator whose stiffness and damping are the slopes of the force; the real part of the larger root decides asymptotic stability, marginal stability or instability, and the marginal case needs the higher-order terms (Section 13).
> - Extensions: beats of a driven undamped oscillator, and the bead on a rotating hoop, whose bottom equilibrium loses its stability at the critical rate while two stable equilibria branch off (Sections 11 and 14).
