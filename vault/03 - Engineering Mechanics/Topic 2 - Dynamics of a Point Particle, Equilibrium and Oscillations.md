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

This note follows `Notes.pdf` Chapter 4, Sections 4.1 to 4.7 (Dynamics of the point particle, Eqs. 4.1 to 4.47: force, linear momentum and kinetic energy; Newton's laws; the equations of motion; power, work and potential energy; the conservation of mechanical energy; equilibrium; the simple pendulum) and Chapter 5 (The harmonic oscillator, Eqs. 5.1 to 5.47: undamped motion, the complex representation, the damped oscillator with small, large and critical damping, the oscillator under a periodic force and resonance), with the decks of Lecture 2 (Particle dynamics, Slides 1 to 23) and Lecture 6 (Oscillations and linearisation: the free and forced oscillator, resonance, beats, damping, the amplification factor and the phase lag, Taylor linearisation about an equilibrium and the bead on a rotating hoop), in the order of the notes. Sections 4.8 (angular momentum and central forces) and 4.9 (dynamics of relative motion) of the same chapter belong to Topics 4 and 5. Kinematic results of Topic 1 are cited, not re-derived: the velocity and acceleration (Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.4) and their Cartesian (Eqs. 2.5 to 2.7), intrinsic (Eqs. 2.16 to 2.18) and cylindrical (Eqs. 2.23 to 2.29) forms, the dot product (Eqs. 1.24 to 1.28), the rules of differentiation of vectors (Eqs. 1.64 to 1.67) and the gradient and curl (Eqs. 1.74, 1.76 and 1.77). See also [[Concept - Newton Laws and Equations of Motion]], [[Concept - Work Power and Kinetic Energy Theorem]], [[Concept - Conservative Forces and Potential Energy]], [[Concept - Conservation of Mechanical Energy and Energy Diagrams]], [[Concept - Equilibrium Configurations and Stability Criteria]] and [[Concept - The Simple Pendulum Nonlinear Dynamics and Linearization]].

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
