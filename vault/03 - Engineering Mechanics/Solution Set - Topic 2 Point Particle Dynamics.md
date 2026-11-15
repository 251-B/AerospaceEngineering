---
title: "Solution Set - Topic 2: Point Particle Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (course order, Notes chapter 7)"
language: "English"
tags:
  - solutions
  - point-particle-dynamics
---

# Topic 2: Point Particle Dynamics - Full Analytical Solutions

Step-by-step analytical solutions for the 10 problems of Topic 2 (**Point Particle Dynamics**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every solution follows the systematic approach of `Notes.pdf`, chapter 7, inside four phases: constraints, degrees of freedom and coordinates (7.1, 7.2); reference frames (7.3); the derivation in the order kinematics (7.4), forces (7.5), equations of motion (7.6) and integration with the answers to the questions (7.7); and the interpretation and checks. Each formula is preceded by the reason for using it, with explicit derivatives (product and chain rules) and explicit integrals (primitive, substitution and Barrow's rule).

---

## Problem 10: Conservative Force and Potential I

### Reference Frames, Bases and Coordinates

The particle $P$ moves along a fixed straight line, the axis $Ox$ of an inertial frame. The force of the statement depends only on the abscissa, so the problem is one-dimensional and conservative: the answers follow from the potential energy and from the conservation of mechanical energy (Notes.pdf, Sec. 4.5).

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre of force $x = 0$ (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along the line of motion, $\mathbf j$ and $\mathbf k$ normal to it, right-handed |
| Moving frames | none: the only basis used is $\mathcal B_0$ |
| Coordinate | $x(t)$, abscissa of $P$ on $Ox$ |
| Applied force | $\mathbf F = -c\,x^3\,\mathbf i$ (statement) |
| Data | $m$ [kg] mass; $c \gt  0$ [kg m$^{-2}$ s$^{-2}$] force constant; $a \gt  0$ [m] release distance |
| Initial conditions | $x(0) = -a$, $\dot x(0) = 0$ (released from rest) |
| Hypotheses | the particle slides on a smooth straight guide along $Ox$ (or moves freely along it); every other force (the weight of a horizontal axis, the reaction of the guide) is normal to $\mathbf i$, with resultant $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$ |
| Constraints | $y = 0$, $z = 0$ (two holonomic, bilateral, smooth constraints) |
| Degrees of freedom | 3 Cartesian coordinates minus 2 constraints leave 1, the coordinate $x$ |

### Change of Basis and Position Vector

The view of the figure looks along $\mathbf k$, which points out of the paper (⊙): $\mathbf i$ to the right, $\mathbf j$ up. The particle is drawn at a point of negative abscissa, with the force that pulls it towards $O$.

![[attachments/EM-SOL/p10-axis-basis.svg]]

> [!derivation] The only basis and its change of basis matrix
> **Law:** change of basis matrix between two bases; orthonormality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> The problem needs one basis only, $\mathcal B_0$, attached to the inertial frame. The matrix that writes $\mathcal B_0$ in itself has as columns the components of $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_0$, so it is the identity; it is checked like any rotation matrix.
>
> $$\begin{aligned}
> \mathbf i &= 1\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k \quad &\text{(first column: components of $\mathbf i$ in $\mathcal B_0$)} \\
> \mathbf j &= 0\,\mathbf i + 1\,\mathbf j + 0\,\mathbf k \quad &\text{(second column)} \\
> \mathbf k &= 0\,\mathbf i + 0\,\mathbf j + 1\,\mathbf k \quad &\text{(third column)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_0] = 1, \quad [{}_0R_0][{}_0R_0]^T = I}$$
>
> **Units:** every entry is a direction cosine, dimensionless: $[1]$
> **Meaning:** no rotation is involved; $\mathcal B_0$ is orthonormal and right-handed, and every vector of the problem is written in it.

> [!derivation] Derivatives of the unit vectors of the fixed basis
> **Law:** derivative of a vector of constant modulus that rotates with angular velocity $\boldsymbol\omega$
> **Source:** Notes.pdf, Eq. 1.62
>
> The basis $\mathcal B_0$ is attached to $S_0$, so its angular velocity relative to $S_0$ is the zero vector.
>
> $$\begin{aligned}
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0} \times \mathbf i \quad &\text{(derivative of a unit vector)} \\
> &= \mathbf 0 \times \mathbf i \quad &\text{($\mathcal B_0$ does not rotate in $S_0$)} \\
> &= (0\cdot 0 - 0\cdot 0)\,\mathbf i + (0\cdot 1 - 0\cdot 0)\,\mathbf j + (0\cdot 0 - 0\cdot 1)\,\mathbf k = \mathbf 0 \quad &\text{(components of the vector product written out)} \\
> \frac{d\mathbf j}{dt} &= \mathbf 0 \times \mathbf j = \mathbf 0, \qquad \frac{d\mathbf k}{dt} = \mathbf 0 \times \mathbf k = \mathbf 0 \quad &\text{(same product with the other two vectors)}
> \end{aligned}$$
>
> $$\boxed{\frac{d\mathbf i}{dt} = \frac{d\mathbf j}{dt} = \frac{d\mathbf k}{dt} = \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$, every component zero
> **Meaning:** the unit vectors of $\mathcal B_0$ are constant, so only the coordinate $x$ changes in time.

> [!derivation] Position vector of the particle
> **Law:** position vector of a point in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(definition of the position vector)} \\
> &= x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(Cartesian components in $\mathcal B_0$)} \\
> &= x\,\mathbf i \quad &\text{(constraints $y = 0$, $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** $x$ is a signed distance: negative to the left of $O$, where the particle starts.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** velocity and acceleration as time derivatives of the position vector in $S_0$
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) \quad &\text{(definition of velocity)} \\
> &= \dot x\,\mathbf i + x\,\frac{d\mathbf i}{dt} \quad &\text{(product rule)} \\
> &= \dot x\,\mathbf i \quad &\text{($\mathbf i$ is constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) \quad &\text{(definition of acceleration)} \\
> &= \ddot x\,\mathbf i + \dot x\,\frac{d\mathbf i}{dt} = \ddot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ is constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i, \qquad \mathbf a_0^P = \ddot x\,\mathbf i}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** velocity and acceleration lie along the line of motion; the sign of the rate of $x$ tells the sense of motion.

### Forces and Equations of Motion

The free-body diagram shows the applied force along $\mathbf i$ and the resultant $\mathbf R_\perp$ of the forces normal to the axis. No inertia forces appear because $S_0$ is inertial.

![[attachments/EM-SOL/p10-fbd.svg]]

> [!derivation] Newton's second law projected on the fixed basis
> **Law:** Newton's second law in an inertial frame, projected on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F + \mathbf R_\perp \quad &\text{(sum of the forces on $P$)} \\
> m\,\ddot x\,\mathbf i &= -c\,x^3\,\mathbf i + R_y\,\mathbf j + R_z\,\mathbf k \quad &\text{(kinematics and forces in $\mathcal B_0$)} \\
> \mathbf i:\quad m\,\ddot x &= -c\,x^3 \quad &\text{(dot product with $\mathbf i$)} \\
> \mathbf j, \mathbf k:\quad 0 &= R_y, \qquad 0 = R_z \quad &\text{(dot products with $\mathbf j$ and $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{m\,\ddot x = -c\,x^3, \qquad \mathbf R_\perp = \mathbf 0}$$
>
> **Units:** $[\mathrm{M}][\mathrm{L\,T^{-2}}] = [\mathrm{M\,L^{-2}\,T^{-2}}][\mathrm{L^3}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the force always points towards $O$ (positive for negative $x$, negative for positive $x$) and grows with the cube of the distance; the forces normal to the axis balance each other (the guide carries the weight, if there is one).

> [!derivation] The force is conservative: potential energy function
> **Law:** in one dimension a force that depends only on position derives from a potential, defined by its work
> **Source:** Notes.pdf, Eq. 4.15; Notes.pdf, Eq. 4.16; [Lecture 2, Slide 14]
>
> The component $F_x(x)$ depends only on $x$, so the elementary work is an exact differential and the potential exists. The reference is taken at the origin.
>
> $$\begin{aligned}
> V_0(x) &= -\int_0^x F_x(x')\,dx' \quad &\text{(definition of the potential, reference $V_0(0) = 0$)} \\
> &= -\int_0^x \left(-c\,x'^3\right)dx' = c\int_0^x x'^3\,dx' \quad &\text{(component of the force of the statement)} \\
> &= c\left[\frac{x'^4}{4}\right]_0^x \quad &\text{(antiderivative of $x'^3$)} \\
> &= c\left(\frac{x^4}{4} - \frac{0^4}{4}\right) = \frac{1}{4}\,c\,x^4 \quad &\text{(Barrow's rule)} \\
> -\frac{dV_0}{dx} &= -\frac{1}{4}\,c\cdot 4x^3 = -c\,x^3 = F_x \quad &\text{(check: the inversion of the definition returns the force)}
> \end{aligned}$$
>
> $$\boxed{V_0(x) = \frac{1}{4}\,c\,x^4}$$
>
> **Units:** $[\mathrm{M\,L^{-2}\,T^{-2}}][\mathrm{L^4}] = [\mathrm{M\,L^2\,T^{-2}}]$, an energy
> **Meaning:** an even, convex well with its minimum at $O$, flatter than a parabola near the origin and steeper far from it.

The potential well and the energy level of the release are drawn below; the turning points are where the level meets the curve.

![[attachments/EM-SOL/p10-potential.svg]]

> [!derivation] First integral: conservation of mechanical energy
> **Law:** the equation of motion multiplied by the velocity is an exact time derivative
> **Source:** Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.26
>
> $$\begin{aligned}
> m\,\ddot x + c\,x^3 &= 0 \quad &\text{(equation of motion along $\mathbf i$)} \\
> \dot x\left(m\,\ddot x + c\,x^3\right) &= 0 \quad &\text{(multiplication by $\dot x$)} \\
> \frac{d}{dt}\left(\frac{1}{2}m\,\dot x^2\right) &= m\,\dot x\,\ddot x \quad &\text{(chain rule: derivative of $\tfrac12 m u^2$ with $u = \dot x$)} \\
> \frac{d}{dt}V_0(x(t)) &= \frac{dV_0}{dx}\,\frac{dx}{dt} = c\,x^3\,\dot x \quad &\text{(chain rule)} \\
> \frac{d}{dt}\left(\frac{1}{2}m\,\dot x^2 + \frac{1}{4}\,c\,x^4\right) &= 0 \quad &\text{(sum of the two derivatives above)}
> \end{aligned}$$
>
> $$\boxed{E_0 = \frac{1}{2}m\,\dot x^2 + \frac{1}{4}\,c\,x^4 = \text{const}}$$
>
> **Units:** $[\mathrm{M}][\mathrm{L^2\,T^{-2}}] = [\mathrm{M\,L^2\,T^{-2}}]$ for both terms
> **Meaning:** kinetic plus potential energy stays constant; the speed at each position follows from the position alone.

> [!derivation] Mechanical energy of the release
> **Law:** the constant of the energy integral is fixed by the initial conditions
> **Source:** Notes.pdf, Eq. 4.26; Problems.pdf, p. 9
>
> $$\begin{aligned}
> E_0 &= \frac{1}{2}m\,\dot x(0)^2 + \frac{1}{4}\,c\,x(0)^4 \quad &\text{(energy integral at $t = 0$)} \\
> &= \frac{1}{2}m\cdot 0^2 + \frac{1}{4}\,c\,(-a)^4 \quad &\text{(released from rest at $x = -a$)} \\
> &= \frac{1}{4}\,c\,a^4 \quad &\text{($(-a)^4 = a^4$, even power)}
> \end{aligned}$$
>
> $$\boxed{E_0 = \frac{1}{4}\,c\,a^4}$$
>
> **Units:** $[\mathrm{M\,L^{-2}\,T^{-2}}][\mathrm{L^4}] = [\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** all the energy is potential at the release; it turns into kinetic energy as the particle falls into the well.

### Answers and Checks

> [!derivation] Velocity on reaching the origin
> **Law:** conservation of mechanical energy between the release point and the origin
> **Source:** Notes.pdf, Eq. 4.27; [Lecture 2, Slide 20]
>
> $$\begin{aligned}
> \frac{1}{2}m\,\dot x^2 + \frac{1}{4}\,c\,x^4 &= \frac{1}{4}\,c\,a^4 \quad &\text{(energy integral with the energy of the release)} \\
> \frac{1}{2}m\,\dot x^2 + 0 &= \frac{1}{4}\,c\,a^4 \quad &\text{(at $x = 0$)} \\
> \dot x^2 &= \frac{c\,a^4}{2m} \quad &\text{(multiplication by $2/m$)} \\
> |\dot x| &= a^2\sqrt{\frac{c}{2m}} \quad &\text{(square root; $a^4 = (a^2)^2$ with $a^2 \gt  0$)} \\
> \dot x &\gt 0 \quad &\text{(sign: see the sentence below)}
> \end{aligned}$$
>
> Sign: at the release the velocity is zero and the force at $x = -a$ is $c\,a^3\,\mathbf i$, along $+\mathbf i$, so the particle starts moving towards positive $x$. The velocity can vanish again only where the kinetic energy vanishes, that is where the potential equals $E_0$, which happens only at $x = \pm a$; between $-a$ and $0$ it cannot change sign, so it is positive at the origin.
>
> $$\boxed{\mathbf v_0^P(x = 0) = a^2\sqrt{\frac{c}{2m}}\ \mathbf i}$$
>
> **Units:** $[\mathrm{L^2}]\left([\mathrm{M\,L^{-2}\,T^{-2}}]/[\mathrm{M}]\right)^{1/2} = [\mathrm{L^2}][\mathrm{L^{-1}\,T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the origin is the bottom of the well, so the speed there is the largest speed of the motion.

> [!derivation] Point where the particle stops again
> **Law:** turning points: the kinetic energy vanishes where the potential equals the mechanical energy
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> \frac{1}{4}\,c\,x_s^4 &= \frac{1}{4}\,c\,a^4 \quad &\text{(zero kinetic energy at the stop $x_s$)} \\
> x_s^4 - a^4 &= 0 \quad &\text{(division by $c/4 \gt  0$)} \\
> \left(x_s^2 - a^2\right)\left(x_s^2 + a^2\right) &= 0 \quad &\text{(difference of squares)} \\
> \left(x_s - a\right)\left(x_s + a\right)\left(x_s^2 + a^2\right) &= 0 \quad &\text{(difference of squares again)} \\
> x_s &= \pm a \quad &\text{($x_s^2 + a^2 \gt  0$ has no real root)} \\
> x_s &= +a \quad &\text{(the particle crossed $O$ moving towards positive $x$)}
> \end{aligned}$$
>
> $$\boxed{x_s = +a}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the motion is allowed only where the potential does not exceed $E_0$, the interval from $-a$ to $+a$; the particle stops at $+a$, is pushed back by the force $-c\,a^3\,\mathbf i$ and oscillates periodically between $-a$ and $+a$.

> [!derivation] Independent check: integration of the equation of motion in the variable x
> **Law:** chain rule on the acceleration, separation of variables and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.24
>
> $$\begin{aligned}
> \ddot x &= \frac{d\dot x}{dt} = \frac{d\dot x}{dx}\,\frac{dx}{dt} = v\,\frac{dv}{dx} \quad &\text{(chain rule, with $v = \dot x$ as a function of $x$)} \\
> m\,v\,dv &= -c\,x^3\,dx \quad &\text{(equation of motion times $dx$)} \\
> m\int_0^{v_1} v\,dv &= -c\int_{-a}^{0} x^3\,dx \quad &\text{(from the release, $v = 0$ at $x = -a$, to the origin, $v = v_1$)} \\
> m\left[\frac{v^2}{2}\right]_0^{v_1} &= -c\left[\frac{x^4}{4}\right]_{-a}^{0} \quad &\text{(antiderivatives)} \\
> \frac{1}{2}m\,v_1^2 &= -c\left(0 - \frac{a^4}{4}\right) = \frac{1}{4}\,c\,a^4 \quad &\text{(Barrow's rule)} \\
> v_1^2 &= \frac{c\,a^4}{2m} \quad &\text{(same value as with the energy integral)}
> \end{aligned}$$
>
> $$\boxed{v_1 = a^2\sqrt{\frac{c}{2m}}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the work of the force from $-a$ to $0$ is all converted into kinetic energy, which confirms the result without the potential.

> [!derivation] Limiting cases and symmetry
> **Law:** behaviour of the results for limiting data; parity of the potential
> **Source:** Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> a \to 0:\quad E_0 &= \frac{1}{4}\,c\,a^4 \to 0, \qquad v_1 = a^2\sqrt{\frac{c}{2m}} \to 0 \quad &\text{(released at the equilibrium, it stays at rest)} \\
> c \to 0:\quad v_1 &\to 0 \quad &\text{(no force, no motion from rest)} \\
> m \to \infty:\quad v_1 &\to 0 \quad &\text{(infinite inertia)} \\
> V_0(-x) &= \frac{1}{4}\,c\,(-x)^4 = V_0(x) \quad &\text{(even potential, so the stops are symmetric about $O$)}
> \end{aligned}$$
>
> $$\boxed{\text{the turning points are } \pm a \text{ and the speed at } O \text{ scales as } a^2}$$
>
> **Units:** each limit keeps the dimensions $[\mathrm{L\,T^{-1}}]$ of the speed
> **Meaning:** unlike a linear spring (speed proportional to $a$), the cubic force gives a speed at the origin proportional to $a^2$.

| Part of the statement | Answer |
| :--- | :--- |
| Potential energy function | $V_0(x) = \tfrac14 c\,x^4$ (plus an arbitrary constant; reference $V_0(0) = 0$) |
| Velocity on reaching $x = 0$ | $\mathbf v_0^P = a^2\sqrt{c/(2m)}\ \mathbf i$ |
| Where it stops again | at $x = +a$; afterwards it oscillates between $-a$ and $+a$ |

**Check against the official key:** the solution keys of the course (Problems.pdf, p. 72) print no answer for Problem 10: the entry is empty. The results above are checked independently by the integration in the variable $x$ (same speed at the origin), by the factorisation of the turning-point condition and by the limiting cases; a numerical integration of the equation of motion with unit data reproduces the speed 0.7071 m/s at the origin and the stop at plus 1 m.

---

## Problem 11: Conservative Force and Potential II

### Reference Frames, Bases and Coordinates

The particle moves along the axis $Ox$ of an inertial frame and its potential energy is given. The study follows the energy method of Notes.pdf, Sec. 4.5 and Sec. 4.6 and [Lecture 2, Slide 20]: the force and the equilibrium points come from the derivatives of the potential, the sketch from its extrema and limits, and the types of motion from the allowed regions where the potential does not exceed the mechanical energy.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre of symmetry of the potential (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along the line of motion, $\mathbf j$ and $\mathbf k$ normal to it, right-handed |
| Moving frames | none |
| Coordinate | $x(t)$, abscissa of the particle on $Ox$ |
| Potential energy | $V(x) = -\tfrac{c}{2}\left(x^2 - a^2\right)^2$ (statement; it is the $V_0$ of Notes.pdf) |
| Data | $m$ [kg]; $c \gt  0$ [kg m$^{-2}$ s$^{-2}$]; $a \gt  0$ [m]; $E$ [J], the mechanical energy (constant) |
| Auxiliary symbols | $s = \sqrt{2\lvert E\rvert/c}$ [m$^2$] for negative $E$; $x_{\text{in}} = \sqrt{a^2 - s}$, $x_{\text{out}} = \sqrt{a^2 + s}$ [m] |
| Hypotheses | smooth straight guide along $Ox$ (or free motion along it); every force other than the conservative one is normal to $\mathbf i$, with resultant $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$ |
| Constraints | $y = 0$, $z = 0$ (holonomic, bilateral, smooth) |
| Degrees of freedom | 3 minus 2 constraints leave 1, the coordinate $x$ |

### Change of Basis and Position Vector

Only the fixed basis is used. The figure looks along $\mathbf k$, out of the paper (⊙), with $\mathbf i$ to the right and $\mathbf j$ up.

![[attachments/EM-SOL/p11-axis-forces.svg]]

> [!derivation] The only basis, its matrix and the derivatives of its unit vectors
> **Law:** change of basis matrix (orthonormal, unit determinant); derivative of a unit vector, $\boldsymbol\omega$ cross the vector
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> [{}_0R_0] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ written in $\mathcal B_0$)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)} \\
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0} \times \mathbf i = \mathbf 0 \times \mathbf i = \mathbf 0 \quad &\text{($\mathcal B_0$ does not rotate in $S_0$; same for $\mathbf j$ and $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = I, \qquad \frac{d\mathbf i}{dt} = \frac{d\mathbf j}{dt} = \frac{d\mathbf k}{dt} = \mathbf 0}$$
>
> **Units:** dimensionless entries; $[\mathrm{T^{-1}}]$ for the derivatives, all zero
> **Meaning:** no rotation is involved; only the coordinate $x$ changes in time.

> [!derivation] Position vector of the particle
> **Law:** position vector in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(definition, components in $\mathcal B_0$)} \\
> &= x\,\mathbf i \quad &\text{(constraints $y = 0$, $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the abscissa is a signed distance from the centre of symmetry of the potential.

### Kinematics

> [!derivation] Velocity and acceleration
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) = \dot x\,\mathbf i + x\,\frac{d\mathbf i}{dt} = \dot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) = \ddot x\,\mathbf i + \dot x\,\frac{d\mathbf i}{dt} = \ddot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i, \qquad \mathbf a_0^P = \ddot x\,\mathbf i}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** both vectors lie on the axis; the sign of the velocity tells the sense of motion.

### Forces and Equations of Motion

The free-body diagram of the figure above shows the conservative force along $\mathbf i$ (its sign depends on the position) and the resultant of the normal forces. $S_0$ is inertial: no inertia forces.

> [!derivation] Force derived from the potential
> **Law:** in one dimension the force is minus the derivative of the potential; chain rule
> **Source:** Notes.pdf, Eq. 4.16; [Lecture 2, Slide 14]
>
> Write $u$ for the inner function $x^2 - a^2$, whose derivative is $2x$.
>
> $$\begin{aligned}
> V &= -\frac{c}{2}\,u^2, \qquad u = x^2 - a^2 \quad &\text{(composition of functions)} \\
> \frac{dV}{dx} &= \frac{dV}{du}\,\frac{du}{dx} = -\frac{c}{2}\cdot 2u\cdot 2x \quad &\text{(chain rule)} \\
> &= -2c\,x\left(x^2 - a^2\right) \quad &\text{(back to $x$)} \\
> F_x &= -\frac{dV}{dx} = 2c\,x\left(x^2 - a^2\right) \quad &\text{(force from the potential)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = 2c\,x\left(x^2 - a^2\right)\mathbf i}$$
>
> **Units:** $[\mathrm{M\,L^{-2}\,T^{-2}}][\mathrm{L}][\mathrm{L^2}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** for $0 \lt x \lt a$ the force is negative (towards the origin) and for $x \gt a$ it is positive (away from it): the origin attracts, the points beyond $\pm a$ repel.

> [!derivation] Equation of motion and energy integral
> **Law:** Newton's second law along $\mathbf i$; multiplication by the velocity and chain rule
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27
>
> $$\begin{aligned}
> m\,\ddot x\,\mathbf i &= F_x\,\mathbf i + R_y\,\mathbf j + R_z\,\mathbf k \quad &\text{(second law in $\mathcal B_0$)} \\
> m\,\ddot x &= -\frac{dV}{dx}, \qquad R_y = R_z = 0 \quad &\text{(components along $\mathbf i$, $\mathbf j$, $\mathbf k$)} \\
> \dot x\left(m\,\ddot x + \frac{dV}{dx}\right) &= \frac{d}{dt}\left(\frac12 m\dot x^2\right) + \frac{dV}{dx}\frac{dx}{dt} = 0 \quad &\text{(multiplication by $\dot x$; chain rule twice)} \\
> \frac{d}{dt}\left(\frac12 m\dot x^2 + V(x)\right) &= 0 \quad &\text{(the bracket is a first integral)} \\
> \frac12 m\dot x^2 &= E - V(x) \ge 0 \quad &\text{(kinetic energy is non-negative)}
> \end{aligned}$$
>
> $$\boxed{m\,\ddot x = 2c\,x\left(x^2 - a^2\right), \qquad \tfrac12 m\dot x^2 = E - V(x), \qquad V(x) \le E}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$ in the equation of motion; $[\mathrm{M\,L^2\,T^{-2}}]$ in the integral
> **Meaning:** the particle can only be where the potential does not exceed $E$; it stops (turning point) where the two are equal.

> [!derivation] Equilibrium points and their stability
> **Law:** equilibrium where the force vanishes; stable at a minimum of the potential, unstable at a maximum
> **Source:** Notes.pdf, Eq. 4.32; [Lecture 2, Slide 22]
>
> $$\begin{aligned}
> \frac{dV}{dx} &= -2c\,x\left(x - a\right)\left(x + a\right) = 0 \iff x = 0,\ a,\ -a \quad &\text{(difference of squares; product equal to zero)} \\
> \frac{d^2V}{dx^2} &= \frac{d}{dx}\left(-2c\,x^3 + 2c\,a^2x\right) = -6c\,x^2 + 2c\,a^2 \quad &\text{(derivative of a polynomial, term by term)} \\
> &= 2c\left(a^2 - 3x^2\right) \quad &\text{(common factor)} \\
> x = 0:\quad V &= -\frac{c}{2}\left(-a^2\right)^2 = -\frac{c\,a^4}{2}, \qquad \frac{d^2V}{dx^2} = 2c\,a^2 \gt 0 \quad &\text{(local minimum: stable)} \\
> x = \pm a:\quad V &= -\frac{c}{2}\cdot 0^2 = 0, \qquad \frac{d^2V}{dx^2} = 2c\left(a^2 - 3a^2\right) = -4c\,a^2 \lt 0 \quad &\text{(local maxima: unstable)}
> \end{aligned}$$
>
> $$\boxed{x = 0:\ \text{stable},\ V = -\tfrac12 c\,a^4; \qquad x = \pm a:\ \text{unstable},\ V = 0}$$
>
> **Units:** $[\mathrm{M\,L^{-2}\,T^{-2}}][\mathrm{L^4}] = [\mathrm{M\,L^2\,T^{-2}}]$ for the values of the potential
> **Meaning:** a well of depth $\tfrac12 c\,a^4$ at the origin between two barriers of zero height at $\pm a$.

> [!derivation] Shape of the potential: parity, inflections and limits
> **Law:** analysis of a function: symmetry, sign of the second derivative, behaviour at infinity
> **Source:** [Lecture 2, Slide 20]
>
> $$\begin{aligned}
> V(-x) &= -\frac{c}{2}\left((-x)^2 - a^2\right)^2 = V(x) \quad &\text{(even function: the sketch is symmetric about $x = 0$)} \\
> V(x) &\le 0 \ \text{for every}\ x \quad &\text{(minus a positive constant times a square)} \\
> \frac{d^2V}{dx^2} &= 0 \iff x = \pm\frac{a}{\sqrt 3} \quad &\text{(inflection points, between the minimum and the maxima)} \\
> V\!\left(\pm\frac{a}{\sqrt3}\right) &= -\frac{c}{2}\left(\frac{a^2}{3} - a^2\right)^2 = -\frac{2}{9}\,c\,a^4 \quad &\text{(height of the inflection points)} \\
> \lim_{x\to\pm\infty} V &= -\frac{c}{2}\lim_{x\to\pm\infty}\left(x^2 - a^2\right)^2 = -\infty \quad &\text{(the square grows without bound)}
> \end{aligned}$$
>
> $$\boxed{V:\ -\infty \nearrow 0\ (x = -a) \searrow -\tfrac12 c\,a^4\ (x = 0) \nearrow 0\ (x = a) \searrow -\infty}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the requested sketch: a W turned upside down, a central well bounded by two barrier tops at zero, falling without bound on both sides.

The sketch, with the three energy ranges of the statement drawn as horizontal levels, is the figure below.

![[attachments/EM-SOL/p11-potential.svg]]

> [!derivation] Turning points: roots of the condition that the potential equals the energy
> **Law:** the kinetic energy vanishes where the potential equals the mechanical energy; the allowed region is where it does not exceed it
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> For negative $E$ the number $s$ of the table is positive and its square is $-2E/c$.
>
> $$\begin{aligned}
> -\frac{c}{2}\left(x^2 - a^2\right)^2 &= E \quad &\text{(turning point)} \\
> \left(x^2 - a^2\right)^2 &= -\frac{2E}{c} \quad &\text{(multiplication by $-2/c$)} \\
> E \gt 0 &\Rightarrow \text{no real root} \quad &\text{(a square cannot be negative)} \\
> E \lt 0:\quad x^2 - a^2 &= \pm s \quad &\text{(square root of both sides)} \\
> x^2 &= a^2 + s \ \ \text{or}\ \ x^2 = a^2 - s \quad &\text{(two candidate values of $x^2$)} \\
> V(x) \le E &\iff \left(x^2 - a^2\right)^2 \ge s^2 \iff \lvert x^2 - a^2\rvert \ge s \quad &\text{(inequality multiplied by $-2/c$, which reverses it)}
> \end{aligned}$$
>
> $$\boxed{\text{allowed region: } x^2 \ge a^2 + s \ \text{ or } \ x^2 \le a^2 - s \qquad (E \lt 0)}$$
>
> **Units:** $[s] = \left([\mathrm{M\,L^2\,T^{-2}}]/[\mathrm{M\,L^{-2}\,T^{-2}}]\right)^{1/2} = [\mathrm{L^2}]$, like $a^2$
> **Meaning:** the outer branch exists for every negative energy; the inner branch needs $a^2 - s$ to be positive, i.e. an energy above the bottom of the well.

### Answers and Checks

> [!derivation] Case (a): energy above the barriers
> **Law:** allowed region and sign of the velocity from the energy integral
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> \frac12 m\dot x^2 &= E - V(x) = E + \frac{c}{2}\left(x^2 - a^2\right)^2 \quad &\text{(energy integral)} \\
> &\ge E \gt 0 \quad &\text{(the added square is non-negative)} \\
> \lvert\dot x\rvert &\ge \sqrt{2E/m} \gt 0 \quad &\text{(the velocity never vanishes, so it keeps its sign)}
> \end{aligned}$$
>
> $$\boxed{E \gt 0:\ \text{no turning point; the particle moves to } +\infty \text{ or to } -\infty \text{ according to the sign of its velocity}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for the bound on the speed
> **Meaning:** the whole axis is allowed; a particle launched towards the origin crosses the well and both barriers without stopping, and its speed grows without bound as it runs away because the potential falls to minus infinity.

> [!derivation] Case (b): energy below the bottom of the well
> **Law:** allowed regions; direction of the force at a turning point
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.16
>
> $$\begin{aligned}
> E \lt -\frac{c\,a^4}{2} &\Rightarrow s^2 = -\frac{2E}{c} \gt a^4 \Rightarrow s \gt a^2 \quad &\text{(the energy range of the statement)} \\
> a^2 - s &\lt 0 \quad &\text{(the inner branch has no real point)} \\
> x^2 &\ge a^2 + s \iff \lvert x\rvert \ge x_{\text{out}} \quad &\text{(only the outer regions are allowed)} \\
> F_x(x_{\text{out}}) &= 2c\,x_{\text{out}}\left(x_{\text{out}}^2 - a^2\right) = 2c\,x_{\text{out}}\,s \gt 0 \quad &\text{(force at the right turning point: outwards)}
> \end{aligned}$$
>
> $$\boxed{E \lt -\tfrac12 c\,a^4:\ \lvert x\rvert \ge x_{\text{out}} = \sqrt{a^2 + \sqrt{2\lvert E\rvert/c}};\ \text{goes to } \pm\infty \text{ directly, or after a reflection at } \pm x_{\text{out}}}$$
>
> **Units:** $[x_{\text{out}}] = ([\mathrm{L^2}] + [\mathrm{L^2}])^{1/2} = [\mathrm{L}]$
> **Meaning:** a particle in the right region moving outwards goes straight to $+\infty$; moving inwards it slows down, stops at $x_{\text{out}}$, is pushed outwards and then goes to $+\infty$ (and symmetrically on the left). It can never reach the well.

> [!derivation] Case (c): energy between the bottom of the well and the barrier tops
> **Law:** allowed regions; direction of the force at the turning points
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.16; [Lecture 2, Slide 20]
>
> $$\begin{aligned}
> -\frac{c\,a^4}{2} \lt E \lt 0 &\Rightarrow 0 \lt s^2 \lt a^4 \Rightarrow 0 \lt s \lt a^2 \quad &\text{(the energy range of the statement)} \\
> 0 \lt x_{\text{in}}^2 &= a^2 - s \lt a^2 \lt a^2 + s = x_{\text{out}}^2 \quad &\text{(four real turning points, ordered)} \\
> \lvert x\rvert &\le x_{\text{in}} \ \ \text{or}\ \ \lvert x\rvert \ge x_{\text{out}} \quad &\text{(allowed region of the previous box)} \\
> F_x(x_{\text{in}}) &= 2c\,x_{\text{in}}\left(x_{\text{in}}^2 - a^2\right) = -2c\,x_{\text{in}}\,s \lt 0 \quad &\text{(force at the inner right turning point: back towards the origin)}
> \end{aligned}$$
>
> $$\boxed{-\tfrac12 c\,a^4 \lt E \lt 0:\ \text{oscillation in } [-x_{\text{in}}, x_{\text{in}}],\ \text{or as in case (b) in } \lvert x\rvert \ge x_{\text{out}}}$$
>
> **Units:** $[\mathrm{L}]$ for both turning radii
> **Meaning:** which motion happens depends on where the particle starts: inside the well it oscillates for ever about the stable point $x = 0$ (the barriers are higher than its energy); outside it goes to infinity directly or after one reflection.

> [!derivation] Limiting energies and small oscillations
> **Law:** behaviour of the turning points at the ends of each range; linearisation about the stable equilibrium
> **Source:** [Lecture 6, Slide 15]; Notes.pdf, Eq. 5.6
>
> Write $\xi$ for a small displacement of the particle from the origin, so that its abscissa is $\xi$ itself.
>
> $$\begin{aligned}
> E \to -\frac{c\,a^4}{2}:\quad s &\to a^2,\quad x_{\text{in}} \to 0,\quad x_{\text{out}} \to \sqrt2\,a \quad &\text{(the well shrinks to the stable point)} \\
> E \to 0^-:\quad s &\to 0,\quad x_{\text{in}} \to a,\quad x_{\text{out}} \to a \quad &\text{(the turning points merge at the barrier tops)} \\
> m\,\ddot\xi &= F_x(0) + \left.\frac{dF_x}{dx}\right|_0\xi = 0 - \left.\frac{d^2V}{dx^2}\right|_0\xi = -2c\,a^2\,\xi \quad &\text{(first-order expansion of the force about $x = 0$)} \\
> \omega_0^2 &= \frac{2c\,a^2}{m} \quad &\text{(harmonic oscillator form)}
> \end{aligned}$$
>
> $$\boxed{\omega_0 = a\sqrt{2c/m}\ \text{for small oscillations about } x = 0}$$
>
> **Units:** $\left([\mathrm{L^2}][\mathrm{M\,L^{-2}\,T^{-2}}]/[\mathrm{M}]\right)^{1/2} = [\mathrm{T^{-1}}]$
> **Meaning:** at the bottom of the well the oscillation becomes harmonic; at the top ($E$ equal to zero) the turning points reach the unstable equilibria, the separatrix between cases (c) and (a).

| Energy range | Turning points | Allowed region | Possible motions |
| :--- | :--- | :--- | :--- |
| (a) $E \gt  0$ | none | the whole axis | towards $+\infty$ or $-\infty$, never stopping |
| (b) $E \lt  -\tfrac12 c a^4$ | $\pm x_{\text{out}}$ | $\lvert x\rvert \ge x_{\text{out}}$ | towards $\pm\infty$ directly, or reflected once at $\pm x_{\text{out}}$ and then to $\pm\infty$ |
| (c) $-\tfrac12 c a^4 \lt  E \lt  0$ | $\pm x_{\text{in}}$, $\pm x_{\text{out}}$ | $\lvert x\rvert \le x_{\text{in}}$ or $\lvert x\rvert \ge x_{\text{out}}$ | oscillation between $-x_{\text{in}}$ and $x_{\text{in}}$; or towards $\pm\infty$ directly or after one reflection |

with $x_{\text{in}}$ and $x_{\text{out}}$ defined in the table of the first section and computed in the turning-point box.

**Check against the official key:** Problems.pdf, p. 72, item 11, is qualitative: (a) the particle can move towards positive or negative infinity; (b) towards positive or negative infinity directly, or reflected towards positive or negative infinity; (c) the same, or oscillating back and forth. The three cases above agree with it. The derivatives of the potential were also checked by finite differences.

---

## Problem 12: Conservative Force and Potential III

### Reference Frames, Bases and Coordinates

The particle moves along the axis $Ox$ of an inertial frame under a conservative force, so its mechanical energy is constant and the velocity is a known function of the position. The time between two positions is then a quadrature: this is the method that Notes.pdf, Eq. 4.44 applies to the pendulum and [Lecture 6, Slide 7] to the harmonic oscillator. The second part applies the general formula to an anharmonic potential.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along the line of motion, right-handed |
| Moving frames | none |
| Coordinate | $x(t)$, abscissa on $Ox$ |
| Potential energy | $V(x)$, any smooth function (first part); $V(x) = \tfrac12 m\omega_0^2\left(x^2 - b\,x^4\right)$ (second part) |
| Turning points | $x_1 \lt  x_2$: the particle oscillates between them; $E = V(x_1) = V(x_2)$ |
| Data | $m$ [kg]; $\omega_0 \gt  0$ [s$^{-1}$]; $b$ [m$^{-2}$]; amplitude $a \gt  0$ [m] |
| Unknown | $\tau$ [s], the period of the oscillation |
| Hypotheses | smooth guide (or free motion) along $Ox$, other forces normal to $\mathbf i$ with resultant $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$; inside the interval the potential is below $E$; the turning points are simple, $V'(x_1) \lt  0 \lt  V'(x_2)$ |
| Constraints | $y = 0$, $z = 0$ (holonomic, bilateral, smooth) |
| Degrees of freedom | 1, the coordinate $x$ |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p12-axis-forces.svg]]

> [!derivation] The only basis, its matrix and the derivatives of its unit vectors
> **Law:** change of basis matrix (orthonormal, unit determinant); derivative of a unit vector, $\boldsymbol\omega$ cross the vector
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> [{}_0R_0] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ written in $\mathcal B_0$)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)} \\
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0} \times \mathbf i = \mathbf 0 \times \mathbf i = \mathbf 0 \quad &\text{($\mathcal B_0$ does not rotate in $S_0$; same for $\mathbf j$ and $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = I, \qquad \frac{d\mathbf i}{dt} = \frac{d\mathbf j}{dt} = \frac{d\mathbf k}{dt} = \mathbf 0}$$
>
> **Units:** dimensionless entries; $[\mathrm{T^{-1}}]$ for the derivatives, all zero
> **Meaning:** the figure looks along $\mathbf k$, out of the paper (⊙); no rotation is involved.

> [!derivation] Position vector of the particle
> **Law:** position vector in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(definition, components in $\mathcal B_0$)} \\
> &= x\,\mathbf i \quad &\text{(constraints $y = 0$, $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the particle sweeps the segment from $x_1$ to $x_2$ back and forth.

### Kinematics

> [!derivation] Velocity, acceleration and the differential of time
> **Law:** time derivatives of the position vector in $S_0$; product rule; differential of a monotonic function
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) = \dot x\,\mathbf i + x\,\frac{d\mathbf i}{dt} = \dot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) = \ddot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)} \\
> dx &= \dot x\,dt \iff dt = \frac{dx}{\dot x} \quad &\text{(differential of $x(t)$, valid while $\dot x \neq 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i, \qquad \mathbf a_0^P = \ddot x\,\mathbf i, \qquad dt = \frac{dx}{\dot x}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$ and $[\mathrm{L}]/[\mathrm{L\,T^{-1}}] = [\mathrm{T}]$
> **Meaning:** while the particle moves in one sense, $x$ can be used instead of $t$ as the variable of integration.

### Forces and Equations of Motion

The force along $\mathbf i$ is the conservative one; the normal forces balance (Notes.pdf, Eq. 4.5). $S_0$ is inertial: no inertia forces.

> [!derivation] Equation of motion and energy integral
> **Law:** Newton's second law along $\mathbf i$; multiplication by the velocity and chain rule
> **Source:** Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27
>
> $$\begin{aligned}
> m\,\ddot x &= -\frac{dV}{dx} \quad &\text{(second law along $\mathbf i$, force from the potential)} \\
> \frac{d}{dt}\left(\frac12 m\dot x^2 + V(x)\right) &= m\dot x\ddot x + \frac{dV}{dx}\dot x = \dot x\left(m\ddot x + \frac{dV}{dx}\right) = 0 \quad &\text{(chain rule on both terms)} \\
> \frac12 m\dot x^2 + V(x) &= E = V(x_2) \quad &\text{(constant; at the turning point $x_2$ the velocity is zero)} \\
> \dot x^2 &= \frac{2}{m}\left[V(x_2) - V(x)\right] \quad &\text{(solved for the square of the velocity)}
> \end{aligned}$$
>
> $$\boxed{\lvert\dot x\rvert = \sqrt{\frac{2\left[V(x_2) - V(x)\right]}{m}}}$$
>
> **Units:** $\left([\mathrm{M\,L^2\,T^{-2}}]/[\mathrm{M}]\right)^{1/2} = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the speed is a known function of the position; only its sign is not given by the energy.

> [!derivation] Sign of the velocity on each leg of the oscillation
> **Law:** continuity of the velocity; force at a turning point
> **Source:** Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.16
>
> Strictly between the turning points the potential is below $E$, so the speed is positive there and the velocity, being continuous, cannot change sign there.
>
> $$\begin{aligned}
> F_x(x_1) &= -V'(x_1) \gt 0 \quad &\text{(at the left turning point the force points to $+\mathbf i$)} \\
> x_1 \to x_2:\quad \dot x &= +\sqrt{2\left[V(x_2) - V(x)\right]/m} \quad &\text{(outward leg)} \\
> F_x(x_2) &= -V'(x_2) \lt 0 \quad &\text{(at the right turning point the force points to $-\mathbf i$)} \\
> x_2 \to x_1:\quad \dot x &= -\sqrt{2\left[V(x_2) - V(x)\right]/m} \quad &\text{(return leg)}
> \end{aligned}$$
>
> $$\boxed{\dot x \gt 0 \text{ from } x_1 \text{ to } x_2, \qquad \dot x \lt 0 \text{ from } x_2 \text{ back to } x_1}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** on each leg $x(t)$ is strictly monotonic, so the change of variable from $t$ to $x$ of the kinematics is valid on each leg separately.

### Answers and Checks

> [!derivation] Duration of the outward leg
> **Law:** change of the variable of integration from $t$ to $x$; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44; [Lecture 6, Slide 7]
>
> The particle leaves $x_1$ at the instant $t_A$ and reaches $x_2$ at $t_B$.
>
> $$\begin{aligned}
> t_B - t_A &= \int_{t_A}^{t_B} dt \quad &\text{(Barrow's rule: antiderivative $t$)} \\
> &= \int_{x_1}^{x_2}\frac{dx}{\dot x} \quad &\text{(change of variable, $x(t_A) = x_1$, $x(t_B) = x_2$)} \\
> &= \int_{x_1}^{x_2}\frac{dx}{\sqrt{2\left[V(x_2) - V(x)\right]/m}} \quad &\text{(positive root on this leg)} \\
> &= \int_{x_1}^{x_2}\sqrt{\frac{m}{2\left[V(x_2) - V(x)\right]}}\,dx \quad &\text{(the reciprocal of a square root is the square root of the reciprocal)}
> \end{aligned}$$
>
> $$\boxed{t_B - t_A = \int_{x_1}^{x_2}\sqrt{\frac{m}{2\left[V(x_2) - V(x)\right]}}\,dx}$$
>
> **Units:** $[\mathrm{M}/(\mathrm{M\,L^2\,T^{-2}})]^{1/2}[\mathrm{L}] = [\mathrm{L^{-1}\,T}][\mathrm{L}] = [\mathrm{T}]$
> **Meaning:** each element of length is crossed in the time length over speed; summing them gives the duration of the leg.

> [!derivation] Duration of the return leg
> **Law:** change of variable with the negative root; reversal of the limits of a definite integral
> **Source:** Notes.pdf, Eq. 4.44
>
> The particle leaves $x_2$ at $t_B$ and is back at $x_1$ at $t_C$.
>
> $$\begin{aligned}
> t_C - t_B &= \int_{x_2}^{x_1}\frac{dx}{\dot x} \quad &\text{(change of variable, $x(t_B) = x_2$, $x(t_C) = x_1$)} \\
> &= \int_{x_2}^{x_1}\frac{dx}{-\sqrt{2\left[V(x_2) - V(x)\right]/m}} \quad &\text{(negative root on this leg)} \\
> &= \int_{x_1}^{x_2}\frac{dx}{\sqrt{2\left[V(x_2) - V(x)\right]/m}} \quad &\text{(reversing the limits changes the sign)}
> \end{aligned}$$
>
> $$\boxed{t_C - t_B = t_B - t_A}$$
>
> **Units:** $[\mathrm{T}]$
> **Meaning:** the way back takes as long as the way out: at every point the speed is the same on both legs, only the sense is opposite.

> [!derivation] Period of the oscillation
> **Law:** periodicity of the motion; sum of the two legs
> **Source:** Notes.pdf, Eq. 4.44; [Lecture 6, Slide 7]
>
> At $t_C$ the particle is again at $x_1$ with zero velocity, the same state as at $t_A$; the equation of motion is of second order, so the same state is followed by the same motion and the time $t_C - t_A$ is the period.
>
> $$\begin{aligned}
> \tau &= t_C - t_A = \left(t_C - t_B\right) + \left(t_B - t_A\right) \quad &\text{(the period is the sum of the two legs)} \\
> &= 2\left(t_B - t_A\right) \quad &\text{(the two legs last the same)} \\
> &= 2\int_{x_1}^{x_2}\sqrt{\frac{m}{2\left[V(x_2) - V(x)\right]}}\,dx \quad &\text{(duration of the outward leg)}
> \end{aligned}$$
>
> $$\boxed{\tau = 2\int_{x_1}^{x_2}\sqrt{\frac{m}{2\left[V(x_2) - V(x)\right]}}\,dx}$$
>
> **Units:** $[\mathrm{T}]$
> **Meaning:** the first formula of the statement is proved; it holds for any potential with two simple turning points.

> [!derivation] The integral converges at the turning points
> **Law:** first-order expansion of the potential at a simple turning point; Barrow's rule for the improper integral
> **Source:** Notes.pdf, Eq. 4.27
>
> The integrand is unbounded at $x_2$, where the bracket vanishes. Write $\delta$ for a small positive length and $k_2$ for the positive slope $V'(x_2)$.
>
> $$\begin{aligned}
> V(x_2) - V(x) &\approx k_2\left(x_2 - x\right) \quad &\text{(first-order expansion about $x_2$)} \\
> \sqrt{\frac{m}{2\left[V(x_2) - V(x)\right]}} &\approx \sqrt{\frac{m}{2k_2}}\left(x_2 - x\right)^{-1/2} \quad &\text{(integrand near $x_2$)} \\
> \int_{x_2 - \delta}^{x_2}\left(x_2 - x\right)^{-1/2}dx &= \left[-2\left(x_2 - x\right)^{1/2}\right]_{x_2 - \delta}^{x_2} \quad &\text{(antiderivative; check: its derivative is the integrand)} \\
> &= -2\cdot 0 - \left(-2\sqrt\delta\right) = 2\sqrt\delta \quad &\text{(Barrow's rule)}
> \end{aligned}$$
>
> $$\boxed{\text{the period integral is finite at a simple turning point}}$$
>
> **Units:** $[\mathrm{L}]^{1/2}$ for the last integral, times $[\mathrm{M}/(\mathrm{M\,L\,T^{-2}})]^{1/2} = [\mathrm{L^{-1/2}\,T}]$ gives $[\mathrm{T}]$
> **Meaning:** although the particle stops at the turning points, it spends only a finite time near them; the same holds at $x_1$.

> [!derivation] Anharmonic potential: turning points of amplitude a
> **Law:** symmetry of the potential; turning points where the potential equals the energy
> **Source:** Notes.pdf, Eq. 4.28; Problems.pdf, p. 9
>
> $$\begin{aligned}
> V(-x) &= \frac12 m\omega_0^2\left((-x)^2 - b(-x)^4\right) = V(x) \quad &\text{(even potential)} \\
> x_2 &= a, \qquad x_1 = -a, \qquad V(x_1) = V(x_2) \quad &\text{(oscillation of amplitude $a$, symmetric about $O$)} \\
> V'(x) &= \frac12 m\omega_0^2\left(2x - 4b\,x^3\right) = m\omega_0^2\,x\left(1 - 2b\,x^2\right) \quad &\text{(derivative term by term)} \\
> V'(a) &= m\omega_0^2\,a\left(1 - 2b\,a^2\right) \gt 0 \iff b\,a^2 \lt \frac12 \quad &\text{(the turning point $a$ is simple when this holds)}
> \end{aligned}$$
>
> $$\boxed{x_1 = -a,\quad x_2 = a,\qquad 2b\,a^2 \lt 1}$$
>
> **Units:** $[b\,a^2] = [\mathrm{L^{-2}}][\mathrm{L^2}] = [1]$
> **Meaning:** for $b$ positive the potential has two maxima at $x^2$ equal to $1/(2b)$; only amplitudes below them give an oscillation. For $b$ zero or negative every amplitude does.

> [!derivation] Anharmonic potential: the period
> **Law:** the period formula of the first part; factorisation of a difference of fourth powers
> **Source:** Notes.pdf, Eq. 4.44; Problems.pdf, p. 9
>
> $$\begin{aligned}
> V(a) - V(x) &= \frac12 m\omega_0^2\left[\left(a^2 - x^2\right) - b\left(a^4 - x^4\right)\right] \quad &\text{(difference of the two values, grouped by powers)} \\
> a^4 - x^4 &= \left(a^2 - x^2\right)\left(a^2 + x^2\right) \quad &\text{(difference of squares)} \\
> V(a) - V(x) &= \frac12 m\omega_0^2\left(a^2 - x^2\right)\left[1 - b\left(a^2 + x^2\right)\right] \quad &\text{(common factor $a^2 - x^2$)} \\
> \frac{m}{2\left[V(a) - V(x)\right]} &= \frac{m}{m\omega_0^2\left(a^2 - x^2\right)\left[1 - b\left(a^2 + x^2\right)\right]} = \frac{1}{\omega_0^2\left(a^2 - x^2\right)\left[1 - b\left(a^2 + x^2\right)\right]} \quad &\text{(the mass cancels)} \\
> \sqrt{\frac{m}{2\left[V(a) - V(x)\right]}} &= \frac{1}{\omega_0\sqrt{a^2 - x^2}\,\sqrt{1 - b\left(a^2 + x^2\right)}} \quad &\text{(both brackets positive for $\lvert x\rvert \lt a$, since $b(a^2 + x^2) \lt 2b\,a^2 \lt 1$)} \\
> \tau &= 2\int_{-a}^{a}\frac{dx}{\omega_0\sqrt{a^2 - x^2}\,\sqrt{1 - b\left(a^2 + x^2\right)}} \quad &\text{(period formula with $x_1 = -a$, $x_2 = a$)}
> \end{aligned}$$
>
> $$\boxed{\tau = \frac{2}{\omega_0}\int_{-a}^{a}\frac{dx}{\sqrt{a^2 - x^2}\,\sqrt{1 - b\left(a^2 + x^2\right)}}}$$
>
> **Units:** $[\mathrm{T}]$: the integral is a length over a length, dimensionless, and $1/\omega_0$ is a time
> **Meaning:** the second formula of the statement is proved; the factor with $b$ measures how far the oscillation is from harmonic.

![[attachments/EM-SOL/p12-potential.svg]]

> [!derivation] Harmonic limit: the period does not depend on the amplitude
> **Law:** trigonometric substitution in a definite integral; Barrow's rule
> **Source:** [Lecture 6, Slide 7]; Notes.pdf, Eq. 5.13
>
> For $b$ equal to zero the potential is that of the harmonic oscillator with stiffness $m\omega_0^2$. Substitute $x = a\sin\varphi$: when $x$ runs from $-a$ to $a$, $\varphi$ runs from $-\pi/2$ to $\pi/2$, where $\cos\varphi$ is not negative.
>
> $$\begin{aligned}
> dx &= a\cos\varphi\,d\varphi \quad &\text{(differential of the substitution)} \\
> \sqrt{a^2 - x^2} &= \sqrt{a^2\left(1 - \sin^2\varphi\right)} = a\cos\varphi \quad &\text{(Pythagorean identity; $\cos\varphi \ge 0$ on the interval)} \\
> \int_{-a}^{a}\frac{dx}{\sqrt{a^2 - x^2}} &= \int_{-\pi/2}^{\pi/2}\frac{a\cos\varphi\,d\varphi}{a\cos\varphi} = \int_{-\pi/2}^{\pi/2}d\varphi \quad &\text{(substitution with the new limits)} \\
> &= \left[\varphi\right]_{-\pi/2}^{\pi/2} = \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) = \pi \quad &\text{(Barrow's rule)} \\
> \tau &= \frac{2}{\omega_0}\,\pi \quad &\text{(the second formula with $b$ equal to zero)}
> \end{aligned}$$
>
> $$\boxed{b = 0:\quad \tau = \frac{2\pi}{\omega_0}}$$
>
> **Units:** $[\mathrm{T}]$
> **Meaning:** the result of the course for the harmonic oscillator (isochronous: independent of $a$) is recovered.

> [!derivation] Effect of the amplitude: first-order correction
> **Law:** same substitution in the exact integral; first-order expansion of a power for small anharmonicity; Barrow's rule
> **Source:** Notes.pdf, Eq. 4.44; [Lecture 6, Slide 7]
>
> With the same substitution, $a^2 + x^2$ becomes $a^2(1 + \sin^2\varphi)$. Write $\epsilon$ for $b\,a^2(1 + \sin^2\varphi)$, small when $b\,a^2$ is small.
>
> $$\begin{aligned}
> \tau &= \frac{2}{\omega_0}\int_{-\pi/2}^{\pi/2}\frac{d\varphi}{\sqrt{1 - b\,a^2\left(1 + \sin^2\varphi\right)}} \quad &\text{(exact; the factor $a\cos\varphi$ cancels as before)} \\
> \left(1 - \epsilon\right)^{-1/2} &\approx 1 + \frac{\epsilon}{2} \quad &\text{(first-order expansion, derivative of the power at $\epsilon = 0$ equal to $1/2$)} \\
> \int_{-\pi/2}^{\pi/2}\sin^2\varphi\,d\varphi &= \left[\frac{\varphi}{2} - \frac{\sin 2\varphi}{4}\right]_{-\pi/2}^{\pi/2} = \left(\frac{\pi}{4} - 0\right) - \left(-\frac{\pi}{4} - 0\right) = \frac{\pi}{2} \quad &\text{(antiderivative from $\sin^2\varphi = (1 - \cos 2\varphi)/2$; Barrow's rule)} \\
> \tau &\approx \frac{2}{\omega_0}\left[\pi + \frac{b\,a^2}{2}\left(\pi + \frac{\pi}{2}\right)\right] \quad &\text{(term by term, with $\int d\varphi = \pi$)} \\
> &= \frac{2\pi}{\omega_0}\left(1 + \frac{3}{4}\,b\,a^2\right) \quad &\text{(common factor $\pi$)}
> \end{aligned}$$
>
> $$\boxed{\tau \approx \frac{2\pi}{\omega_0}\left(1 + \frac34\,b\,a^2\right)\quad (b\,a^2 \ll 1)}$$
>
> **Units:** $[b\,a^2] = [1]$, so $[\tau] = [\mathrm{T}]$
> **Meaning:** for $b$ positive (a softening force, weaker than the linear one far from $O$) the period grows with the amplitude and tends to infinity as $2b\,a^2$ tends to 1, where the turning points reach the maxima of the potential; for $b$ negative (hardening) it decreases.

| Part of the statement | Answer |
| :--- | :--- |
| Period for oscillation between $x_1$ and $x_2$ | $\tau = 2\int_{x_1}^{x_2}\sqrt{m/(2[V(x_2) - V(x)])}\,dx$, proved from the energy integral and the two legs |
| Period for $V = \tfrac12 m\omega_0^2(x^2 - b x^4)$, amplitude $a$ | $\tau = \dfrac{2}{\omega_0}\int_{-a}^{a}\dfrac{dx}{\sqrt{a^2 - x^2}\sqrt{1 - b(a^2 + x^2)}}$, valid for $2ba^2 \lt  1$ |
| Checks | $b = 0$ gives $2\pi/\omega_0$; small $ba^2$ gives $\tfrac{2\pi}{\omega_0}(1 + \tfrac34 ba^2)$ |

**Check against the official key:** Problems.pdf, p. 72, item 12, gives only the hint to separate variables (the two formulas to prove are in the statement), which is the method used above. Independent numerical check with unit values of $\omega_0$ (1 s$^{-1}$) and $b$ (1 m$^{-2}$): the period from the integral of the second formula (Simpson rule in the variable $\varphi$) and the period measured on a Runge-Kutta integration of the equation of motion agree to four decimals, and the first-order estimate is close only for small amplitudes.

| Amplitude $a$ [m] | Integral formula [s] | Integration of the equation of motion [s] | First-order estimate [s] |
| :--- | :--- | :--- | :--- |
| 0.1 | 6.3309 | 6.3309 | 6.3303 |
| 0.3 | 6.7592 | 6.7592 | 6.7073 |
| 0.5 | 8.0086 | 8.0086 | 7.4613 |
| 0.6 | 9.5549 | 9.5549 | 7.9796 |

---

## Problem 13: Conservative Force and Potential IV

### Reference Frames, Bases and Coordinates

A particle of mass $m$ moves along the axis $Ox$ of an inertial frame under a force that derives from the potential of the statement. The motion is one-dimensional, so the mechanical energy is a first integral and the time law follows from one quadrature, as in Notes.pdf, Sec. 4.5 (one-dimensional conservative motion). The integral given in the tip of the statement is used, and it is verified by differentiation before it is used.

| Symbol | Meaning | Units |
| :--- | :--- | :--- |
| $S_0 = \{O;\ \mathbf i, \mathbf j, \mathbf k\}$ | inertial frame; $O$ the origin of the potential; $\mathbf i$ along the axis $Ox$, positive in the sense of the initial velocity | - |
| $m$ | mass of the particle | kg |
| $g$ | positive constant with units of acceleration (it appears in the potential) | m/s$^2$ |
| $a$ | positive length of the potential | m |
| $V(x) = mgx\left[(x/a)^2 - 3\right]$ | potential energy of the statement | J |
| $x(t)$ | coordinate of the particle on $Ox$ (the only degree of freedom) | m |
| $y = x/a$ | dimensionless coordinate | - |
| $x_0 = a$, $\dot x(0) = v_0 = \sqrt{8ga}$ | initial conditions (statement), velocity along $+\mathbf i$ | m, m/s |
| $E$ | mechanical energy, kinetic plus potential | J |
| $\lambda = \sqrt{3g/(2a)}$ | rate that appears in the time law | 1/s |
| $\alpha = \operatorname{arctanh}(1/\sqrt 3)$ | constant offset of the time law | - |

Hypotheses and degrees of freedom:

- The particle is kept on the axis $Ox$ by a smooth guide (or moves on it freely). The only force with a component along $\mathbf i$ is the conservative force of the potential; any other force (the reaction of a smooth guide, a weight normal to the axis) is perpendicular to $\mathbf i$ and does no work.
- One degree of freedom, the coordinate $x$; the motion is described with the dimensionless coordinate $y$ to simplify the algebra.
- The statement asks for "the evolution of the particle as a function of time": the answer is the function $x(t)$ for every positive time, written in implicit form on each leg of the motion (as the key does) and inverted to one explicit formula.

![[attachments/EM-SOL/p13-axis-and-forces.svg]]

### Change of Basis and Position Vector

Only one basis is needed: $\mathcal B_0$ is fixed in the inertial frame. The boxes below state this as a (trivial) change of basis, give the position vector and the derivatives of the unit vectors from the angular velocity of the basis.

> [!derivation] Basis of the problem and its change of basis matrix
> **Law:** definition of the change of basis matrix; orthogonality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> The motion takes place on one fixed straight line, so the basis in which the position is written is the fixed basis itself: every column of the matrix is a fixed unit vector written in $\mathcal B_0$.
>
> $$\begin{aligned}
> \mathbf i &= 1\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k \quad &\text{(first column)} \\
> \mathbf j &= 0\,\mathbf i + 1\,\mathbf j + 0\,\mathbf k \quad &\text{(second column)} \\
> \mathbf k &= \mathbf i \times \mathbf j \quad &\text{(right-handed basis; $\mathbf k$ points out of the paper ⊙ in the figure)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(product of the identity with itself)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix},\qquad \det[{}_0R_0] = 1,\qquad [{}_0R_0][{}_0R_0]^T = I}$$
>
> **Units:** $[1]$ for every entry
> **Meaning:** no rotation is involved; every vector of the problem has one component, along $\mathbf i$.

> [!derivation] Position vector and dimensionless coordinate
> **Law:** definition of the position vector in the fixed basis
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(definition of the position vector)} \\
> &= x\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k \quad &\text{(the particle stays on the axis $Ox$)} \\
> &= a\,y\,\mathbf i \quad &\text{(dimensionless coordinate, $x$ is $a$ times $y$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i = a\,y\,\mathbf i,\qquad y(0) = 1}$$
>
> **Units:** $[\mathrm{L}]$; $y$ is dimensionless
> **Meaning:** the initial position is the point $x = a$, which turns out to be the bottom of the potential well.

> [!derivation] Derivatives of the unit vectors
> **Law:** derivative of a unit vector of constant magnitude, $\dot{\mathbf u} = \boldsymbol\omega \times \mathbf u$
> **Source:** Notes.pdf, Eq. 1.62
>
> The basis $\mathcal B_0$ does not rotate with respect to $S_0$, so its angular velocity is the zero vector.
>
> $$\begin{aligned}
> \boldsymbol\omega_{B0} &= 0\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k \quad &\text{(fixed basis)} \\
> \dot{\mathbf i} &= \boldsymbol\omega_{B0} \times \mathbf i = \mathbf 0 \times \mathbf i = \mathbf 0 \quad &\text{(every component of $\boldsymbol\omega$ is zero)} \\
> \dot{\mathbf j} &= \boldsymbol\omega_{B0} \times \mathbf j = \mathbf 0 \quad &\text{(same reason)} \\
> \dot{\mathbf k} &= \boldsymbol\omega_{B0} \times \mathbf k = \mathbf 0 \quad &\text{(same reason)}
> \end{aligned}$$
>
> $$\boxed{\dot{\mathbf i} = \dot{\mathbf j} = \dot{\mathbf k} = \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** only the coordinate changes in time; the unit vectors are constants.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** definitions of velocity and acceleration in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.3; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) \quad &\text{(definition of velocity)} \\
> &= \dot x\,\mathbf i + x\,\dot{\mathbf i} \quad &\text{(product rule)} \\
> &= \dot x\,\mathbf i \quad &\text{(the unit vector is constant)} \\
> &= a\,\dot y\,\mathbf i \quad &\text{(chain rule with $x$ equal to $a$ times $y$, $a$ constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) = \ddot x\,\mathbf i + \dot x\,\dot{\mathbf i} \quad &\text{(definition of acceleration; product rule)} \\
> &= \ddot x\,\mathbf i = a\,\ddot y\,\mathbf i \quad &\text{(constant unit vector)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i = a\,\dot y\,\mathbf i,\qquad \mathbf a_0^P = \ddot x\,\mathbf i = a\,\ddot y\,\mathbf i}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the velocity and the acceleration lie on the axis; their sign tells the sense of the motion and of the push.

### Forces and Equations of Motion

![[attachments/EM-SOL/p13-free-body.svg]]

> [!derivation] Conservative force from the potential
> **Law:** force of a one-dimensional potential, minus the derivative of the potential; chain rule
> **Source:** Notes.pdf, Eq. 4.16; Notes.pdf, Eq. 4.15
>
> $$\begin{aligned}
> V &= mgx\left(\frac{x^2}{a^2} - 3\right) = mg\left(\frac{x^3}{a^2} - 3x\right) \quad &\text{(potential of the statement, expanded)} \\
> \frac{dV}{dx} &= mg\left(\frac{3x^2}{a^2} - 3\right) \quad &\text{(derivative of a power, term by term)} \\
> F_x &= -\frac{dV}{dx} = -3mg\left(\frac{x^2}{a^2} - 1\right) \quad &\text{(force from the potential)} \\
> &= -3mg\left(y^2 - 1\right) \quad &\text{(dimensionless coordinate)} \\
> V &= mga\left(y^3 - 3y\right) \quad &\text{(the potential in terms of $y$: $x^3/a^2$ is $a\,y^3$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F = -3mg\left(y^2 - 1\right)\mathbf i,\qquad V = mga\left(y^3 - 3y\right)}$$
>
> **Units:** $[\mathrm{M}][\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$ for the force; $[\mathrm{M}][\mathrm{L\,T^{-2}}][\mathrm{L}] = [\mathrm{M\,L^2\,T^{-2}}]$ for the potential
> **Meaning:** between the points $x = -a$ and $x = a$ the force pushes toward $+\mathbf i$; outside that interval it pushes toward $-\mathbf i$.

> [!derivation] Equilibrium points and their stability
> **Law:** equilibrium where the force vanishes; stable at a minimum of the potential, unstable at a maximum
> **Source:** Notes.pdf, Eq. 4.32
>
> $$\begin{aligned}
> \frac{dV}{dy} &= mga\left(3y^2 - 3\right) = 3mga\left(y^2 - 1\right) \quad &\text{(derivative term by term)} \\
> 3mga\left(y^2 - 1\right) &= 0 \iff y = 1 \ \text{or}\ y = -1 \quad &\text{(difference of squares, $(y - 1)(y + 1)$)} \\
> \frac{d^2V}{dy^2} &= 6mga\,y \quad &\text{(second derivative)} \\
> V(1) &= mga(1 - 3) = -2mga,\quad \left.\frac{d^2V}{dy^2}\right|_{1} = 6mga \gt 0 \quad &\text{(local minimum: stable)} \\
> V(-1) &= mga(-1 + 3) = 2mga,\quad \left.\frac{d^2V}{dy^2}\right|_{-1} = -6mga \lt 0 \quad &\text{(local maximum: unstable)}
> \end{aligned}$$
>
> $$\boxed{x = a:\ \text{stable, } V = -2mga;\qquad x = -a:\ \text{unstable, } V = 2mga}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$ for every value of the potential
> **Meaning:** the particle starts at the bottom of a well whose left wall ends at the barrier top $x = -a$; to the right the potential grows without bound.

![[attachments/EM-SOL/p13-potential.svg]]

> [!derivation] Equation of motion
> **Law:** Newton's second law along $\mathbf i$ in the inertial frame
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.21
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F \quad &\text{(Newton's second law)} \\
> m\,a\,\ddot y &= -3mg\left(y^2 - 1\right) \quad &\text{(projection on $\mathbf i$, with the kinematics above)} \\
> \ddot y &= -\frac{3g}{a}\left(y^2 - 1\right) \quad &\text{(division by $m\,a$)}
> \end{aligned}$$
>
> $$\boxed{\ddot y + \frac{3g}{a}\left(y^2 - 1\right) = 0,\qquad y(0) = 1,\quad \dot y(0) = \sqrt{8g/a}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ on both sides
> **Meaning:** a non-linear equation of second order; it is integrated once with the energy, then by quadrature.

> [!derivation] Mechanical energy of the motion
> **Law:** conservation of mechanical energy of a particle under a conservative force
> **Source:** Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27
>
> $$\begin{aligned}
> E &= \tfrac{1}{2}m\dot x^2 + V(x) \quad &\text{(definition: kinetic plus potential energy)} \\
> &= \tfrac{1}{2}m(8ga) + mga\left(1^3 - 3\cdot 1\right) \quad &\text{(initial state, $y$ equal to 1)} \\
> &= 4mga - 2mga = 2mga \quad &\text{(arithmetic)} \\
> E - V(-a) &= 2mga - 2mga = 0 \quad &\text{(comparison with the barrier top)}
> \end{aligned}$$
>
> $$\boxed{E = 2mga = V(-a)}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** the energy equals exactly the height of the barrier: the motion is the separatrix, and the particle can reach the top of the barrier only in the limit of infinite time.

> [!derivation] First integral in factorised form
> **Law:** energy equation solved for the squared speed; factorisation of a cubic by one known root
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> \tfrac{1}{2}m a^2\dot y^2 &= E - V = 2mga - mga\left(y^3 - 3y\right) \quad &\text{(energy equation with $\dot x$ equal to $a\dot y$)} \\
> \dot y^2 &= \frac{2g}{a}\left(2 + 3y - y^3\right) \quad &\text{(multiplication by $2/(m a^2)$)} \\
> y^3 - 3y - 2\big|_{y = -1} &= -1 + 3 - 2 = 0 \quad &\text{(so $y + 1$ is a factor)} \\
> (y + 1)(y^2 - y - 2) &= y^3 - y^2 - 2y + y^2 - y - 2 = y^3 - 3y - 2 \quad &\text{(the quotient, checked by expansion)} \\
> y^2 - y - 2 &= (y + 1)(y - 2) \quad &\text{(roots $-1$ and $2$ of the quadratic)} \\
> 2 + 3y - y^3 &= -(y + 1)^2(y - 2) = (y + 1)^2(2 - y) \quad &\text{(change of sign of the cubic)}
> \end{aligned}$$
>
> $$\boxed{\dot y^2 = \frac{2g}{a}\,(y + 1)^2\,(2 - y)}$$
>
> **Units:** $[\mathrm{T^{-2}}]$ on both sides
> **Meaning:** the allowed region is the set of points with a non-negative right-hand side, every point with $y$ up to 2; the right end $x = 2a$ is a simple turning point and the left end $x = -a$ a double root (the barrier top).

> [!derivation] Verification of the integral of the tip
> **Law:** an antiderivative is checked by differentiating it; chain rule
> **Source:** Problems.pdf, p. 9
>
> Let $u$ be the square root of the quantity $(2 - y)/3$. For $y$ between $-1$ and $2$ it lies between 0 and 1, where the inverse hyperbolic tangent is defined.
>
> $$\begin{aligned}
> u^2 &= \frac{2 - y}{3} \quad &\text{(definition of $u$)} \\
> 2u\,du &= -\frac{dy}{3} \implies \frac{du}{dy} = -\frac{1}{6u} \quad &\text{(differential of both sides)} \\
> \frac{d}{dy}\left[-\frac{2}{\sqrt 3}\operatorname{arctanh}u\right] &= -\frac{2}{\sqrt 3}\,\frac{1}{1 - u^2}\,\frac{du}{dy} \quad &\text{(chain rule; the derivative of arctanh is $1/(1 - u^2)$)} \\
> &= \frac{2}{\sqrt 3}\,\frac{1}{1 - u^2}\,\frac{1}{6u} = \frac{1}{3\sqrt 3\,u\,(1 - u^2)} \quad &\text{(substitution of $du/dy$)} \\
> 1 - u^2 &= \frac{3 - 2 + y}{3} = \frac{y + 1}{3} \quad &\text{(definition of $u$)} \\
> 3\sqrt 3\,u\,(1 - u^2) &= 3\sqrt 3\,\frac{\sqrt{2 - y}}{\sqrt 3}\,\frac{y + 1}{3} = (y + 1)\sqrt{2 - y} \quad &\text{(product of the factors)}
> \end{aligned}$$
>
> $$\boxed{\int\frac{dy}{(y + 1)\sqrt{2 - y}} = -\frac{2}{\sqrt 3}\operatorname{arctanh}\sqrt{\frac{2 - y}{3}} + C}$$
>
> **Units:** dimensionless
> **Meaning:** the tip of the statement is correct on the whole allowed interval of $y$ between $-1$ and $2$.

> [!derivation] Outgoing leg: from the bottom of the well to the turning point
> **Law:** separation of variables and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.27; Problems.pdf, p. 9
>
> On this leg the velocity is positive (it starts positive and can change sign only where the right-hand side of the first integral vanishes), and the factor $y + 1$ is positive, so the positive square root is taken. $\lambda$ and $\alpha$ are defined in the table.
>
> $$\begin{aligned}
> \frac{dy}{dt} &= \sqrt{\frac{2g}{a}}\,(y + 1)\sqrt{2 - y} \quad &\text{(positive root of the first integral)} \\
> \int_1^{y}\frac{dy'}{(y' + 1)\sqrt{2 - y'}} &= \sqrt{\frac{2g}{a}}\int_0^{t}dt' \quad &\text{(separation of variables, from $y(0)$ equal to 1)} \\
> \left[-\frac{2}{\sqrt 3}\operatorname{arctanh}\sqrt{\frac{2 - y'}{3}}\right]_1^{y} &= \sqrt{\frac{2g}{a}}\,\bigl[t'\bigr]_0^{t} \quad &\text{(antiderivatives)} \\
> -\frac{2}{\sqrt 3}\operatorname{arctanh}\sqrt{\frac{2 - y}{3}} + \frac{2}{\sqrt 3}\operatorname{arctanh}\frac{1}{\sqrt 3} &= \sqrt{\frac{2g}{a}}\,(t - 0) \quad &\text{(Barrow's rule; at $y'$ equal to 1 the root is $1/\sqrt 3$)} \\
> \operatorname{arctanh}\sqrt{\frac{2 - y}{3}} &= -\frac{\sqrt 3}{2}\sqrt{\frac{2g}{a}}\,t + \operatorname{arctanh}\frac{1}{\sqrt 3} \quad &\text{(multiplication by $-\sqrt 3/2$)} \\
> \frac{\sqrt 3}{2}\sqrt{\frac{2g}{a}} &= \sqrt{\frac{3\cdot 2g}{4a}} = \sqrt{\frac{3g}{2a}} = \lambda \quad &\text{(simplification of the rate)}
> \end{aligned}$$
>
> $$\boxed{\operatorname{arctanh}\sqrt{\frac{2 - y}{3}} = -\sqrt{\frac{3g}{2a}}\,t + \operatorname{arctanh}\frac{1}{\sqrt 3},\qquad 0 \le t \le t_1}$$
>
> **Units:** $[\lambda\,t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$; both sides are dimensionless
> **Meaning:** as time grows the left side decreases from its initial value toward zero: the particle climbs the right wall of the well and slows down.

> [!derivation] Time to reach the turning point
> **Law:** the speed vanishes at the right end of the allowed region
> **Source:** Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> 2 - y(t_1) &= 0 \implies x(t_1) = 2a \quad &\text{(simple root of the first integral)} \\
> \operatorname{arctanh}0 &= 0 = -\lambda\,t_1 + \alpha \quad &\text{(outgoing leg at $t_1$)} \\
> t_1 &= \frac{\alpha}{\lambda} = \sqrt{\frac{2a}{3g}}\operatorname{arctanh}\frac{1}{\sqrt 3} \quad &\text{(solution for $t_1$)} \\
> \alpha &= \frac{1}{2}\ln\frac{1 + 1/\sqrt 3}{1 - 1/\sqrt 3} = \frac{1}{2}\ln\left(2 + \sqrt 3\right) \approx 0.6585 \quad &\text{(logarithmic form of arctanh; $(\sqrt3 + 1)^2/2$ is $2 + \sqrt 3$)} \\
> F_x(2a) &= -3mg\left(2^2 - 1\right) = -9mg \lt 0 \quad &\text{(force at the turning point)}
> \end{aligned}$$
>
> $$\boxed{x(t_1) = 2a,\qquad t_1 = \sqrt{\frac{2a}{3g}}\operatorname{arctanh}\frac{1}{\sqrt 3} \approx 0.5376\sqrt{a/g}}$$
>
> **Units:** $\sqrt{[\mathrm{L}]/[\mathrm{L\,T^{-2}}]} = [\mathrm{T}]$
> **Meaning:** the turning point is reached in finite time (simple root), and there the force points toward $-\mathbf i$, so the particle comes back.

> [!derivation] Return leg: toward the barrier top
> **Law:** separation of variables and Barrow's rule, restarted at the turning point
> **Source:** Notes.pdf, Eq. 4.27; Problems.pdf, p. 9
>
> After the turning point the velocity is negative, so the negative square root is taken; it cannot change sign again before the left end of the allowed region, which is the barrier top.
>
> $$\begin{aligned}
> \frac{dy}{dt} &= -\sqrt{\frac{2g}{a}}\,(y + 1)\sqrt{2 - y} \quad &\text{(negative root)} \\
> \int_2^{y}\frac{dy'}{(y' + 1)\sqrt{2 - y'}} &= -\sqrt{\frac{2g}{a}}\int_{t_1}^{t}dt' \quad &\text{(separation of variables, from $y(t_1)$ equal to 2)} \\
> -\frac{2}{\sqrt 3}\operatorname{arctanh}\sqrt{\frac{2 - y}{3}} + \frac{2}{\sqrt 3}\operatorname{arctanh}0 &= -\sqrt{\frac{2g}{a}}\,(t - t_1) \quad &\text{(Barrow's rule with the antiderivative of the tip)} \\
> \operatorname{arctanh}\sqrt{\frac{2 - y}{3}} &= \lambda\,(t - t_1) \quad &\text{(arctanh of 0 is 0; multiplication by $-\sqrt 3/2$)} \\
> &= \lambda\,t - \alpha \quad &\text{($\lambda\,t_1$ equals $\alpha$)}
> \end{aligned}$$
>
> $$\boxed{\operatorname{arctanh}\sqrt{\frac{2 - y}{3}} = \sqrt{\frac{3g}{2a}}\,t - \operatorname{arctanh}\frac{1}{\sqrt 3},\qquad t \ge t_1}$$
>
> **Units:** dimensionless on both sides
> **Meaning:** the left side grows without bound as time grows, which happens only as its argument tends to 1: the particle tends to the barrier top.

### Answers and Checks

> [!derivation] Answer: the position as a function of time
> **Law:** inversion of the two legs; parity of the squared hyperbolic tangent
> **Source:** Problems.pdf, p. 9
>
> $$\begin{aligned}
> \sqrt{\frac{2 - y}{3}} &= \tanh(\alpha - \lambda t) \ \text{on the first leg},\quad \tanh(\lambda t - \alpha) \ \text{on the second} \quad &\text{(tanh of both sides)} \\
> \frac{2 - y}{3} &= \tanh^2(\lambda t - \alpha) \quad &\text{(squaring; $\tanh^2$ is even, so both legs give the same expression)} \\
> y &= 2 - 3\tanh^2(\lambda t - \alpha) \quad &\text{(solution for $y$)} \\
> x &= a\,y \quad &\text{(back to the dimensional coordinate)}
> \end{aligned}$$
>
> $$\boxed{x(t) = a\left[2 - 3\tanh^2\left(\sqrt{\frac{3g}{2a}}\,t - \operatorname{arctanh}\frac{1}{\sqrt 3}\right)\right],\qquad t \ge 0}$$
>
> **Units:** $[\mathrm{L}]$; the argument of tanh is dimensionless
> **Meaning:** one smooth formula covers the whole motion: out from $x = a$ to $x = 2a$ and back, then toward $x = -a$.

> [!derivation] Check: initial conditions recovered
> **Law:** evaluation of the answer and of its time derivative at the initial instant; chain rule
> **Source:** Problems.pdf, p. 9
>
> $$\begin{aligned}
> \tanh(-\alpha) &= -\frac{1}{\sqrt 3},\quad \operatorname{sech}^2(-\alpha) = 1 - \frac{1}{3} = \frac{2}{3} \quad &\text{(tanh is odd; $\operatorname{sech}^2$ is $1 - \tanh^2$)} \\
> y(0) &= 2 - 3\cdot\frac{1}{3} = 1 \quad &\text{(answer at zero time)} \\
> \dot y &= -6\tanh(\lambda t - \alpha)\operatorname{sech}^2(\lambda t - \alpha)\,\lambda \quad &\text{(chain rule; the derivative of tanh is $\operatorname{sech}^2$)} \\
> \dot y(0) &= -6\left(-\frac{1}{\sqrt 3}\right)\frac{2}{3}\sqrt{\frac{3g}{2a}} = \frac{4}{\sqrt 3}\sqrt{\frac{3g}{2a}} = \sqrt{\frac{8g}{a}} \quad &\text{(evaluation at zero time)} \\
> \dot x(0) &= a\,\dot y(0) = \sqrt{8ga} \quad &\text{(back to the dimensional velocity)}
> \end{aligned}$$
>
> $$\boxed{x(0) = a,\qquad \dot x(0) = \sqrt{8ga}}$$
>
> **Units:** $[\mathrm{L}]$ and $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the formula satisfies the two initial conditions of the statement.

> [!derivation] Independent check: the answer satisfies the first integral
> **Law:** substitution of the answer into the energy equation
> **Source:** Notes.pdf, Eq. 4.27
>
> Write $\sigma$ for the argument of tanh, $\lambda t$ minus $\alpha$.
>
> $$\begin{aligned}
> \dot y^2 &= 36\,\lambda^2\tanh^2\sigma\,\operatorname{sech}^4\sigma = 54\,\frac{g}{a}\tanh^2\sigma\,\operatorname{sech}^4\sigma \quad &\text{(square of the derivative; $36\cdot 3/2$ is 54)} \\
> y + 1 &= 3 - 3\tanh^2\sigma = 3\operatorname{sech}^2\sigma \quad &\text{(identity $1 - \tanh^2$ equal to $\operatorname{sech}^2$)} \\
> 2 - y &= 3\tanh^2\sigma \quad &\text{(answer)} \\
> \frac{2g}{a}(y + 1)^2(2 - y) &= \frac{2g}{a}\,9\operatorname{sech}^4\sigma\,3\tanh^2\sigma = 54\,\frac{g}{a}\tanh^2\sigma\,\operatorname{sech}^4\sigma \quad &\text{(product of the factors)}
> \end{aligned}$$
>
> $$\boxed{\dot y^2 = \frac{2g}{a}(y + 1)^2(2 - y)\ \text{holds identically}}$$
>
> **Units:** $[\mathrm{T^{-2}}]$
> **Meaning:** the explicit answer has the energy of the motion at every instant; with the initial conditions it is the solution.

> [!derivation] Limiting case: long times and the barrier top
> **Law:** limit of the answer; speed from the energy equation
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.32
>
> $$\begin{aligned}
> \lim_{t\to\infty}\tanh^2(\lambda t - \alpha) &= 1 \quad &\text{(tanh tends to 1)} \\
> \lim_{t\to\infty}x &= a(2 - 3) = -a \quad &\text{(answer)} \\
> \lim_{t\to\infty}\dot y &= -6\cdot 1\cdot 0\cdot\lambda = 0 \quad &\text{($\operatorname{sech}^2$ tends to 0)} \\
> \dot x\big|_{x = a,\ \text{return}} &= -\sqrt{\frac{2}{m}\left[E - V(a)\right]} = -\sqrt{\frac{2}{m}\,4mga} = -\sqrt{8ga} \quad &\text{(energy at the bottom of the well on the way back)}
> \end{aligned}$$
>
> $$\boxed{x \to -a,\qquad \dot x \to 0\quad (t \to \infty);\qquad \max|\dot x| = \sqrt{8ga}\ \text{at}\ x = a}$$
>
> **Units:** $[\mathrm{L}]$ and $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the particle approaches the unstable equilibrium $x = -a$ asymptotically and never crosses it, as the separatrix energy demands; its largest speed is the initial one, reached again at the bottom of the well.

![[attachments/EM-SOL/p13-position-time.svg]]

| Part of the statement | Answer |
| :--- | :--- |
| Energy of the motion | $E = 2mga$, equal to the barrier top $V(-a)$ (separatrix) |
| Outward leg, $0 \le t \le t_1$ | $\operatorname{arctanh}\sqrt{(2 - y)/3} = -\sqrt{3g/(2a)}\,t + \operatorname{arctanh}(1/\sqrt3)$, with $y = x/a$ |
| Turning point | $x = 2a$ at $t_1 = \sqrt{2a/(3g)}\operatorname{arctanh}(1/\sqrt3) \approx 0.5376\sqrt{a/g}$ |
| Return leg, $t \ge t_1$ | $\operatorname{arctanh}\sqrt{(2 - y)/3} = \sqrt{3g/(2a)}\,t - \operatorname{arctanh}(1/\sqrt3)$ |
| Explicit law, all $t \ge 0$ | $x(t) = a\left[2 - 3\tanh^2\left(\sqrt{3g/(2a)}\,t - \operatorname{arctanh}(1/\sqrt3)\right)\right]$ |
| Long times | $x \to -a$ and $\dot x \to 0$: the particle approaches the unstable equilibrium without reaching it |

**Check against the official key:** Problems.pdf, p. 72, item 13, gives the two legs in exactly the implicit form of the boxes above, the first one for times up to the turning instant (written there as the square root of $2a/(3g)$ times the arctanh of one over root three, as here) and the second one after it: **match**. The key also states that "the terminal velocity is" the square root of $8ga$; the warning and the box below explain that this value is the initial and largest speed. A Runge-Kutta integration of the equation of motion with unit values of $g$ and $a$ reproduces the explicit law ($y$ equal to 1.759553 at $t$ equal to 0.3 s, the turning point at 0.537646 s, $y$ equal to -0.683994 at 2 s).

> [!warning] Discrepancy with the official solution
> The key calls the root of $8ga$ "the terminal velocity". In this motion the velocity tends to zero at long times (the particle approaches the barrier top, the unstable equilibrium at minus $a$), so there is no terminal velocity in the usual sense; the root of $8ga$ is the initial speed and the largest speed, reached at the bottom of the well, at the launch point. The position law of the key agrees with the computed one. The box below supports the reading.

> [!derivation] Speed as a function of position: largest value
> **Law:** energy equation; maximum of the kinetic energy at the minimum of the potential
> **Source:** Notes.pdf, Eq. 4.27
>
> $$\begin{aligned}
> \tfrac{1}{2}m\dot x^2 &= E - V(x) = 2mga - V(x) \quad &\text{(energy equation)} \\
> \min_{-a \le x \le 2a} V &= V(a) = -2mga \quad &\text{(stable equilibrium, the only minimum on the interval swept)} \\
> \max\dot x^2 &= \frac{2}{m}\,(2mga + 2mga) = 8ga \quad &\text{(largest kinetic energy)}
> \end{aligned}$$
>
> $$\boxed{\max|\dot x| = \sqrt{8ga},\qquad \lim_{t\to\infty}\dot x = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the value printed in the key is the peak speed of the motion; the terminal (long-time) speed is zero.

---

## Problem 14: Conservative Force and Potential V

### Reference Frames, Bases and Coordinates

The particle moves along the axis $Ox$ of an inertial frame under a force that depends only on its abscissa, so the force is conservative and the mechanical energy is constant. The types of motion follow from the shape of the potential and from the level of the energy fixed by the initial velocity (Notes.pdf, Sec. 4.5 and Sec. 4.6; [Lecture 2, Slide 20]).

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ along the line of motion, right-handed |
| Moving frames | none |
| Coordinate | $x(t)$, abscissa on $Ox$ |
| Applied force | $\mathbf F = m K x\,e^{x/a}\,\mathbf i$ (statement) |
| Data | $m$ [kg]; $K \gt  0$ [s$^{-2}$]; $a \gt  0$ [m]; $v_0 \gt  0$ [m/s] |
| Initial conditions | $x(0) = a$, $\dot x(0) = -v_0$ (towards the origin) |
| Auxiliary symbols | $V(x)$ potential energy (the $V_0$ of Notes.pdf), reference $V(a) = 0$; $E$ mechanical energy; $v_c = a\sqrt{2K}$ critical speed; $x^*$ turning point |
| Hypotheses | smooth guide (or free motion) along $Ox$; other forces normal to $\mathbf i$, with resultant $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$ |
| Constraints | $y = 0$, $z = 0$ (holonomic, bilateral, smooth) |
| Degrees of freedom | 1, the coordinate $x$ |

### Change of Basis and Position Vector

![[attachments/EM-SOL/p14-axis-forces.svg]]

> [!derivation] The only basis, its matrix and the derivatives of its unit vectors
> **Law:** change of basis matrix (orthonormal, unit determinant); derivative of a unit vector, $\boldsymbol\omega$ cross the vector
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> [{}_0R_0] &= \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix} \quad &\text{(columns: $\mathbf i$, $\mathbf j$, $\mathbf k$ written in $\mathcal B_0$)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)} \\
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0} \times \mathbf i = \mathbf 0 \times \mathbf i = \mathbf 0 \quad &\text{($\mathcal B_0$ does not rotate in $S_0$; same for $\mathbf j$ and $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = I, \qquad \frac{d\mathbf i}{dt} = \frac{d\mathbf j}{dt} = \frac{d\mathbf k}{dt} = \mathbf 0}$$
>
> **Units:** dimensionless entries; $[\mathrm{T^{-1}}]$ for the derivatives, all zero
> **Meaning:** the figure looks along $\mathbf k$, out of the paper (⊙); no rotation is involved.

> [!derivation] Position vector of the particle
> **Law:** position vector in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(definition, components in $\mathcal B_0$)} \\
> &= x\,\mathbf i \quad &\text{(constraints $y = 0$, $z = 0$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x\,\mathbf i, \qquad \mathbf r_0^P(0) = a\,\mathbf i}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the particle starts at a distance $a$ to the right of $O$.

### Kinematics

> [!derivation] Velocity and acceleration
> **Law:** time derivatives of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) = \dot x\,\mathbf i + x\,\frac{d\mathbf i}{dt} = \dot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) = \ddot x\,\mathbf i + \dot x\,\frac{d\mathbf i}{dt} = \ddot x\,\mathbf i \quad &\text{(product rule; $\mathbf i$ constant)} \\
> \mathbf v_0^P(0) &= -v_0\,\mathbf i \quad &\text{(initial velocity of the statement)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i, \qquad \mathbf a_0^P = \ddot x\,\mathbf i, \qquad \dot x(0) = -v_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the particle is launched towards the origin.

### Forces and Equations of Motion

The free-body diagram (figure above) shows the applied force along $\mathbf i$, positive for positive $x$ and negative for negative $x$, and the resultant of the normal forces. $S_0$ is inertial: no inertia forces.

> [!derivation] Equation of motion
> **Law:** Newton's second law in an inertial frame, projected on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5
>
> $$\begin{aligned}
> m\,\ddot x\,\mathbf i &= mK x\,e^{x/a}\,\mathbf i + R_y\,\mathbf j + R_z\,\mathbf k \quad &\text{(sum of the forces in $\mathcal B_0$)} \\
> \ddot x &= K x\,e^{x/a}, \qquad R_y = R_z = 0 \quad &\text{(components; division by $m$)}
> \end{aligned}$$
>
> $$\boxed{\ddot x = K\,x\,e^{x/a}}$$
>
> **Units:** $[\mathrm{T^{-2}}][\mathrm{L}] = [\mathrm{L\,T^{-2}}]$; the exponent is dimensionless
> **Meaning:** the force pushes the particle away from the origin on both sides: $O$ is an equilibrium point that repels.

> [!derivation] Potential energy by integration by parts
> **Law:** potential of a one-dimensional force, defined by its work; integration by parts and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.15; Notes.pdf, Eq. 4.16; [Lecture 2, Slide 14]
>
> The force depends only on $x$, so the potential exists. The reference is the initial point, $V(a) = 0$. In the integral take the factor $x'$ to differentiate and the exponential to integrate: the antiderivative of the exponential is $a\,e^{x'/a}$.
>
> $$\begin{aligned}
> V(x) &= -\int_a^x mK x'\,e^{x'/a}\,dx' \quad &\text{(definition of the potential, reference at $x' = a$)} \\
> \int_a^x x'\,e^{x'/a}\,dx' &= \left[a\,x'\,e^{x'/a}\right]_a^x - \int_a^x a\,e^{x'/a}\,dx' \quad &\text{(integration by parts)} \\
> &= \left(a\,x\,e^{x/a} - a^2 e\right) - \left[a^2 e^{x'/a}\right]_a^x \quad &\text{(Barrow's rule on the first term; antiderivative of the second)} \\
> &= a\,x\,e^{x/a} - a^2 e - a^2 e^{x/a} + a^2 e = a\left(x - a\right)e^{x/a} \quad &\text{(Barrow's rule; the constants cancel)} \\
> V(x) &= -mKa\left(x - a\right)e^{x/a} = mKa\left(a - x\right)e^{x/a} \quad &\text{(times $-mK$)} \\
> -\frac{dV}{dx} &= -mKa\left[-e^{x/a} + \left(a - x\right)\frac{1}{a}e^{x/a}\right] = mK x\,e^{x/a} \quad &\text{(check by the product and chain rules)}
> \end{aligned}$$
>
> $$\boxed{V(x) = mKa\left(a - x\right)e^{x/a}}$$
>
> **Units:** $[\mathrm{M}][\mathrm{T^{-2}}][\mathrm{L}][\mathrm{L}] = [\mathrm{M\,L^2\,T^{-2}}]$, an energy
> **Meaning:** the potential is positive to the left of $a$ and negative to its right; its derivative returns the force of the statement.

> [!derivation] Shape of the potential: the barrier at the origin
> **Law:** equilibrium where the force vanishes; stability from the second derivative; limits at infinity
> **Source:** Notes.pdf, Eq. 4.32; [Lecture 2, Slide 22]
>
> $$\begin{aligned}
> \frac{dV}{dx} &= -mK x\,e^{x/a} = 0 \iff x = 0 \quad &\text{(the exponential never vanishes)} \\
> \frac{dV}{dx} &\gt 0 \ \text{for}\ x \lt 0, \qquad \frac{dV}{dx} \lt 0 \ \text{for}\ x \gt 0 \quad &\text{(sign of minus $x$; increasing, then decreasing)} \\
> \frac{d^2V}{dx^2} &= -mK\left(e^{x/a} + x\,\frac{1}{a}e^{x/a}\right) = -mK\,e^{x/a}\left(1 + \frac{x}{a}\right) \quad &\text{(product rule; chain rule on the exponential)} \\
> V(0) &= mKa^2, \qquad \left.\frac{d^2V}{dx^2}\right|_0 = -mK \lt 0 \quad &\text{(a maximum: unstable equilibrium, the barrier)} \\
> \lim_{x\to-\infty}V &= \lim_{u\to+\infty} mKa^2\left(1 + u\right)e^{-u} = 0^+ \quad &\text{(with $u = -x/a$; the exponential decays faster than any polynomial grows)} \\
> \lim_{x\to+\infty}V &= -\infty \quad &\text{(the factor $a - x$ tends to $-\infty$ and the exponential to $+\infty$)}
> \end{aligned}$$
>
> $$\boxed{V:\ 0^+\ (x \to -\infty) \nearrow mKa^2\ (x = 0) \searrow 0\ (x = a) \searrow -\infty\ (x \to +\infty)}$$
>
> **Units:** $[\mathrm{M\,L^2\,T^{-2}}]$
> **Meaning:** a single barrier of height $mKa^2$ at the origin; to its left the potential stays positive and decays to zero, to its right it falls without bound.

![[attachments/EM-SOL/p14-potential.svg]]

> [!derivation] Mechanical energy and the critical initial speed
> **Law:** conservation of mechanical energy; comparison of the energy with the height of the barrier
> **Source:** Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> $$\begin{aligned}
> \frac{d}{dt}\left(\frac12 m\dot x^2 + V(x)\right) &= \dot x\left(m\ddot x + \frac{dV}{dx}\right) = 0 \quad &\text{(chain rule; equation of motion)} \\
> E &= \frac12 m\left(-v_0\right)^2 + V(a) = \frac12 m v_0^2 \quad &\text{(initial state; reference $V(a) = 0$)} \\
> \frac12 m\dot x^2 &= \frac12 m v_0^2 - V(x) \quad &\text{(energy integral at any position)} \\
> E = V(0) &\iff \frac12 m v_c^2 = mKa^2 \iff v_c = a\sqrt{2K} \quad &\text{(energy equal to the barrier top)}
> \end{aligned}$$
>
> $$\boxed{E = \tfrac12 m v_0^2, \qquad v_c = a\sqrt{2K}}$$
>
> **Units:** $[\mathrm{L}][\mathrm{T^{-2}}]^{1/2} = [\mathrm{L\,T^{-1}}]$ for the critical speed
> **Meaning:** the particle starts on the right slope, below the barrier top, moving towards it; whether it crosses depends only on the comparison of $v_0$ with $v_c$.

### Answers and Checks

> [!derivation] Case 1: initial speed below the critical one
> **Law:** turning point where the potential equals the energy; direction of the force there
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28; Notes.pdf, Eq. 4.16
>
> On the segment from $0$ to $a$ the potential is continuous and strictly decreasing, from $mKa^2$ down to $0$; the energy lies strictly between these two values, so the potential takes the value $E$ at exactly one point $x^*$ of the segment.
>
> $$\begin{aligned}
> 0 \lt v_0 \lt a\sqrt{2K} &\Rightarrow 0 \lt E \lt mKa^2 = V(0) \quad &\text{(energy below the barrier top)} \\
> mKa\left(a - x^*\right)e^{x^*/a} &= \frac12 m v_0^2 \iff \left(1 - \frac{x^*}{a}\right)e^{x^*/a} = \frac{v_0^2}{2Ka^2} \quad &\text{(turning point; division by $mKa^2$)} \\
> F_x(x^*) &= mK x^*\,e^{x^*/a} \gt 0 \quad &\text{(at the turning point the force points to $+\mathbf i$)} \\
> x \gt x^*:\quad \frac12 m\dot x^2 &= E - V(x) \gt E - V(x^*) = 0 \quad &\text{(the potential decreases to the right of $x^*$: no other stop)} \\
> x \ge a:\quad \dot x &\ge v_0 \quad &\text{(there the potential is not positive)}
> \end{aligned}$$
>
> $$\boxed{v_0 \lt a\sqrt{2K}:\ \text{stops at } x^* \in (0, a),\ \text{turns back and moves towards } +\infty}$$
>
> **Units:** both sides of the turning-point equation are dimensionless
> **Meaning:** the particle decelerates before reaching the origin, is reflected by the barrier and then runs away to the right faster and faster, since the potential falls without bound.

> [!derivation] Case 2: initial speed equal to the critical one
> **Law:** energy integral; Taylor expansion of the potential with remainder about the barrier top; separation of variables and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.27; [Lecture 6, Slide 15]
>
> Now the energy equals the barrier top. On the segment from $0$ to $a$ the potential is below $V(0)$ except at $0$, so the velocity stays negative and does not vanish before the origin. Expand the potential about $0$ with the remainder at an intermediate point $\xi$ between $0$ and $x$; since $\xi$ lies between $0$ and $a$, the factor $e^{\xi/a}(1 + \xi/a)$ is at most $2e$.
>
> $$\begin{aligned}
> V(0) - V(x) &= -V'(0)\,x - \frac12 V''(\xi)\,x^2 = \frac12 mK\,e^{\xi/a}\left(1 + \frac{\xi}{a}\right)x^2 \quad &\text{(Taylor with remainder; $V'(0) = 0$)} \\
> &\le e\,mK\,x^2 \quad &\text{(bound of the factor)} \\
> \dot x^2 &= \frac{2}{m}\left[V(0) - V(x)\right] \le 2eK\,x^2 \quad &\text{(energy integral with $E = V(0)$)} \\
> t(x) &= \int_x^a\frac{dx'}{\lvert\dot x\rvert} \ge \frac{1}{\sqrt{2eK}}\int_x^a\frac{dx'}{x'} \quad &\text{(time from $a$ to $x$; the speed is at most $\sqrt{2eK}\,x'$)} \\
> &= \frac{1}{\sqrt{2eK}}\left[\ln x'\right]_x^a = \frac{1}{\sqrt{2eK}}\ln\frac{a}{x} \quad &\text{(antiderivative; Barrow's rule)} \\
> \lim_{x\to 0^+}t(x) &= +\infty \quad &\text{(the logarithm grows without bound)}
> \end{aligned}$$
>
> $$\boxed{v_0 = a\sqrt{2K}:\ \text{the particle tends to } x = 0 \text{ but needs an infinite time to reach it}}$$
>
> **Units:** $[\mathrm{T^{-2}}]^{-1/2} = [\mathrm{T}]$ for the factor in front of the logarithm
> **Meaning:** the particle creeps up to the unstable equilibrium at the barrier top. The linearised equation there, $\ddot\xi$ equal to $K\xi$, gives the exponential approach $\xi$ proportional to $e^{-\sqrt K\,t}$ on the separatrix.

> [!derivation] Case 3: initial speed above the critical one
> **Law:** energy integral; lower bound of the speed
> **Source:** Notes.pdf, Eq. 4.27; Notes.pdf, Eq. 4.28
>
> For every $x$ up to $a$ the potential is at most its maximum $V(0)$.
>
> $$\begin{aligned}
> v_0 \gt a\sqrt{2K} &\Rightarrow E \gt V(0) \ge V(x)\ \text{for}\ x \le a \quad &\text{(energy above the barrier top)} \\
> \dot x^2 &= v_0^2 - \frac{2V(x)}{m} \ge v_0^2 - 2Ka^2 \gt 0 \quad &\text{(energy integral and the bound on the potential)} \\
> \dot x(x = 0) &= -\sqrt{v_0^2 - 2Ka^2} \quad &\text{(at the barrier top; negative sign kept from the start)} \\
> \lim_{x\to-\infty}\dot x^2 &= v_0^2 - 0 = v_0^2 \quad &\text{(the potential tends to zero on the left)}
> \end{aligned}$$
>
> $$\boxed{v_0 \gt a\sqrt{2K}:\ \text{crosses } x = 0 \text{ with speed } \sqrt{v_0^2 - 2Ka^2} \text{ and moves towards } -\infty,\ \lvert\dot x\rvert \to v_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the speed never falls below the value at the top, so the abscissa decreases at least linearly in time and the particle goes to minus infinity; far to the left the force vanishes and it recovers its launch speed.

> [!derivation] Limiting cases and a numerical example
> **Law:** behaviour of the results at the ends of the ranges; solution of the turning-point equation
> **Source:** Notes.pdf, Eq. 4.28; Problems.pdf, p. 9
>
> $$\begin{aligned}
> v_0 \to 0:\quad \left(1 - \frac{x^*}{a}\right)e^{x^*/a} &\to 0 \Rightarrow x^* \to a \quad &\text{(launched without speed it turns at once)} \\
> v_0 \to a\sqrt{2K}^{\,-}:\quad \left(1 - \frac{x^*}{a}\right)e^{x^*/a} &\to 1 \Rightarrow x^* \to 0 \quad &\text{(the turning point climbs to the barrier top)} \\
> K \to 0:\quad v_c &= a\sqrt{2K} \to 0 \quad &\text{(no barrier: every launch reaches minus infinity)} \\
> m = K = a = 1,\ v_0 = 1.2:\quad \left(1 - x^*\right)e^{x^*} &= 0.72 \Rightarrow x^* = 0.6080 \quad &\text{(bisection; case 1 because $1.2 \lt \sqrt2$)}
> \end{aligned}$$
>
> $$\boxed{x^* \to a \ (v_0 \to 0), \qquad x^* \to 0 \ (v_0 \to v_c), \qquad x^* = 0.6080\,\mathrm{m} \ \text{in the example}}$$
>
> **Units:** $[\mathrm{L}]$ for the turning point
> **Meaning:** the three regimes join continuously: the turning point moves from the launch point to the barrier top as the launch speed grows to its critical value.

| Initial speed | Type of motion |
| :--- | :--- |
| $v_0 \lt  a\sqrt{2K}$ | decelerates, stops at $x^* \in (0, a)$ with $(1 - x^*/a)e^{x^*/a} = v_0^2/(2Ka^2)$, is reflected and moves towards $+\infty$ |
| $v_0 = a\sqrt{2K}$ | approaches the unstable equilibrium $x = 0$ asymptotically: it needs an infinite time to reach it |
| $v_0 \gt  a\sqrt{2K}$ | crosses $x = 0$ with speed $\sqrt{v_0^2 - 2Ka^2}$ and moves towards $-\infty$, its speed tending to $v_0$ |

**Check against the official key:** Problems.pdf, p. 72, item 14 (with the constant written $k$): if the initial speed exceeds $a\sqrt{2k}$ the particle moves towards minus infinity; if it is smaller, the particle moves towards infinity after decelerating before arriving at $x$ equal to zero; if it is equal, it takes an infinite time to reach $x$ equal to zero. The three regimes above agree with it: **match**. The potential and its derivatives were also checked by finite differences, and the turning point of the example by bisection.

---

## 📌 Problem 15: Stokes Drag and Terminal Velocity

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a sphere of radius $r$ and density $\rho_s = 2\rho_0$ falls vertically from rest in a fluid at rest of density $\rho_0$ and dynamic viscosity $\mu$. The forces are the weight, the buoyancy and the Stokes drag $F_D = 6\pi\mu rv$ (as the statement says; unsteady and added-mass effects are not considered).
* **Constraints:** the motion is vertical (the sphere does not rotate or drift sideways); $\text{CDOF} = 1$, with the coordinate $x$ measured downward from the release point.
* **Initial conditions:** $x(0) = 0$, $\dot{x}(0) = 0$.
* **Relations:** volume $V = \tfrac{4}{3}\pi r^3$; mass $m = \rho_sV = \tfrac{8}{3}\pi\rho_0r^3$; kinematic viscosity $\nu = \mu/\rho_0$, so $\mu = \rho_0\nu$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0$ fixed to the fluid, with $Ox$ pointing downward along gravity ($\mathbf{i}$ downward); constant unit vectors.

### Phase 3: Derivation

#### 3.1 Kinematics
$$ \mathbf{r} = x\,\mathbf{i}, \qquad \mathbf{v} = \dot{x}\,\mathbf{i}, \qquad \mathbf{a} = \ddot{x}\,\mathbf{i} $$

#### 3.2 Forces
* **Pedagogical Justification:** three forces act along $Ox$ (positive downward). The drag opposes the motion, which is downward ($\dot{x} \gt 0$), so it points upward.
$$ W = mg = \tfrac{8}{3}\pi\rho_0r^3g \ (\downarrow), \qquad F_B = \rho_0Vg = \tfrac{4}{3}\pi\rho_0r^3g = \tfrac{1}{2}W \ (\uparrow), \qquad F_D = 6\pi\mu r\dot{x} = 6\pi\rho_0\nu r\dot{x} \ (\uparrow) $$
* **Net weight corrected by buoyancy:** $W - F_B = \tfrac{4}{3}\pi\rho_0r^3g = \tfrac{1}{2}mg$. **Inertia forces:** none.

#### 3.3 Equations of Motion
* **Newton's second law along $Ox$:** $m\ddot{x} = W - F_B - F_D$:
$$ \tfrac{8}{3}\pi\rho_0r^3\,\ddot{x} = \tfrac{4}{3}\pi\rho_0r^3g - 6\pi\rho_0\nu r\,\dot{x} $$
Dividing by $\tfrac{8}{3}\pi\rho_0r^3$: the first term gives $\dfrac{4/3}{8/3}g = \dfrac{g}{2}$ and the second $\dfrac{6\pi\rho_0\nu r}{(8/3)\pi\rho_0r^3} = 6\cdot\dfrac{3}{8}\cdot\dfrac{\nu}{r^2} = \dfrac{9\nu}{4r^2}$, so
$$ \ddot{x} + \frac{9\nu}{4r^2}\dot{x} = \frac{g}{2} \quad\Longleftrightarrow\quad \boxed{4r^2\ddot{x} + 9\nu\dot{x} = 2r^2g} $$
* One unknown, $x(t)$, and one linear equation with constant coefficients.

#### 3.4 Integration and Answers
##### (a) Terminal velocity
* **Pedagogical Justification:** the terminal velocity is reached when the acceleration vanishes ($\ddot{x} = 0$), i.e. when the drag balances the buoyancy-corrected weight:
$$ 9\nu v_t = 2r^2g \implies \boxed{v_t = \frac{2r^2g}{9\nu}} $$

##### (b) Position as a function of time
* **Velocity.** Let $\gamma = \dfrac{9\nu}{4r^2}$ ($[\gamma] = \text{s}^{-1}$). Then $\dot{v} + \gamma v = \dfrac{g}{2} = \gamma v_t$, i.e. $\dfrac{dv}{v - v_t} = -\gamma\,dt$. Integrating from $v(0) = 0$ with the substitution $w = v' - v_t$, $dw = dv'$, whose antiderivative is $\int dw/w = \ln|w|$ (Barrow):
$$ \int_0^v\frac{dv'}{v' - v_t} = -\gamma\int_0^tdt' \implies \left[\ln|v' - v_t|\right]_0^v = \ln|v - v_t| - \ln|0 - v_t| = \ln\frac{v_t - v}{v_t} = -\gamma t $$
(the absolute value is removed because $v \lt v_t$: the net force $m\gamma(v_t - v)$ is positive while $v \lt v_t$, so $v$ increases from $0$, and it cannot reach $v_t$ in finite time because $v \equiv v_t$ is itself a solution and the solutions of this linear equation are unique). Exponentiating, $1 - v/v_t = e^{-\gamma t}$:
$$ v(t) = v_t\left(1 - e^{-\gamma t}\right) \gt 0 \quad \text{for } t \gt 0 $$
so $\dot{x} \gt 0$ at all times and the drag indeed points upward, as assumed in 3.2.
* **Position.** Integrating the velocity with $x(0) = 0$:
With $u = -\gamma t'$, $du = -\gamma\,dt'$, the antiderivative is $\int e^{-\gamma t'}dt' = -\frac{1}{\gamma}\int e^u\,du = -\frac{1}{\gamma}e^{-\gamma t'}$, so
$$ x(t) = \int_0^tv_t\left(1 - e^{-\gamma t'}\right)dt' = v_t\left[t' + \frac{1}{\gamma}e^{-\gamma t'}\right]_0^t = v_t\left(t + \frac{1}{\gamma}e^{-\gamma t} - \frac{1}{\gamma}\right) = \frac{v_t}{\gamma}\left[\gamma t - 1 + e^{-\gamma t}\right] $$
* Substituting $\dfrac{v_t}{\gamma} = \dfrac{2r^2g}{9\nu}\cdot\dfrac{4r^2}{9\nu} = \dfrac{8r^4g}{81\nu^2}$ and $\gamma = \dfrac{9\nu}{4r^2}$, and writing $\dfrac{8r^4g}{81\nu^2} = \dfrac{2r^2g}{81\nu^2}\cdot 4r^2$ so that $4r^2$ multiplies the bracket (with $4r^2\cdot\gamma t = 4r^2\cdot\frac{9\nu}{4r^2}t = 9\nu t$):
$$ \boxed{x(t) = \frac{2r^2g}{81\nu^2}\left[-4r^2 + 4r^2\exp\left(-\frac{9\nu}{4r^2}t\right) + 9\nu t\right]} $$

### Phase 4: Interpretation & Checks
* **Short times ($t \ll \gamma^{-1}$):** with $e^{-\gamma t} \approx 1 - \gamma t + \tfrac{1}{2}\gamma^2t^2$, $x \approx \dfrac{v_t}{\gamma}\cdot\dfrac{1}{2}\gamma^2t^2 = \tfrac{1}{2}(\gamma v_t)t^2 = \tfrac{1}{4}gt^2$: free fall under the effective gravity $g\left(1 - \rho_0/\rho_s\right) = g/2$.
* **Long times ($t \gg \gamma^{-1}$):** $x \approx v_tt - v_t/\gamma$, uniform descent at $v_t$ with an offset $v_t/\gamma$.
* **Dimensional check:** $[v_t] = \dfrac{\text{m}^2\cdot\text{m s}^{-2}}{\text{m}^2\text{s}^{-1}} = \text{m/s}$ and $[\gamma] = \text{m}^2\text{s}^{-1}/\text{m}^2 = \text{s}^{-1}$.
* **Check against the official key:** the key of `Problems.pdf` gives the equation of motion $4r^2\ddot{x} + 9\nu\dot{x} = 2r^2g$ (with $x$ positive downward, initial conditions $x(0) = \dot{x}(0) = 0$) and $x = \frac{2r^2g}{81\nu^2}\left[-4r^2 + 4r^2\exp\left(-\frac{9\nu}{4r^2}t\right) + 9\nu t\right]$. Both are identical to the results above. Numerical integration (DOP853, $g = r = \nu = 1$) gives $x(2) = 0.3467762$, equal to the closed form.

---

## 📌 Problem 16: Drag on Falling Football

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a football of mass $m$, frontal area $S$ and drag coefficient $C_D$ falls vertically through air of density $\rho$. Only gravity and the quadratic drag $D = \tfrac{1}{2}\rho v^2SC_D$ act.
* **Constraints:** vertical motion; $\text{CDOF} = 1$, with the coordinate $s$ measured downward from the release point.
* **Initial conditions:** $s(0) = 0$, $v(0) = 0$. The statement gives $\displaystyle\int\frac{dx}{x_0^2 - x^2} = \frac{1}{x_0}\operatorname{atanh}\frac{x}{x_0}$ and $\int\tanh x\,dx = \ln\cosh x$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** fixed to the air, with $Os$ pointing vertically downward.

### Phase 3: Derivation

#### 3.1 Kinematics
$$ \mathbf{r} = s\,\mathbf{i}, \qquad \mathbf{v} = \dot{s}\,\mathbf{i} = v\,\mathbf{i}, \qquad \mathbf{a} = \dot{v}\,\mathbf{i} $$

#### 3.2 Forces
* **Weight:** $mg$ downward. **Drag:** $D = \tfrac{1}{2}\rho v^2SC_D$, upward because it opposes the downward velocity ($v \gt 0$). **Inertia forces:** none.

#### 3.3 Equations of Motion
* **Newton's second law:**
$$ m\frac{dv}{dt} = mg - \tfrac{1}{2}\rho SC_Dv^2 $$
One unknown, $v(t)$ (and then $s(t)$ by integration), and one first-order equation.

#### 3.4 Integration and Answers
##### Terminal velocity
* **Pedagogical Justification:** at the terminal velocity the net force vanishes: $mg = \tfrac{1}{2}\rho SC_Dv_t^2$:
$$ \boxed{v_t = \sqrt{\frac{2mg}{\rho SC_D}}} $$

##### Velocity as a function of time
* **Pedagogical Justification:** using $\tfrac{1}{2}\rho SC_D = mg/v_t^2$ writes the equation in terms of $v_t$ and allows the given integral:
$$ \frac{dv}{dt} = g\left(1 - \frac{v^2}{v_t^2}\right) = \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \implies \frac{dv}{v_t^2 - v^2} = \frac{g}{v_t^2}\,dt $$
* Integrating from $v = 0$ at $t = 0$ (Barrow, with $\operatorname{atanh}0 = 0$):
$$ \left[\frac{1}{v_t}\operatorname{atanh}\frac{v'}{v_t}\right]_0^v = \frac{g}{v_t^2}\int_0^tdt' \implies \operatorname{atanh}\frac{v}{v_t} = \frac{gt}{v_t} \implies \boxed{v(t) = v_t\tanh\left(\frac{gt}{v_t}\right)} $$
The speed increases from $0$ (the net force is positive while $v \lt v_t$) and cannot reach $v_t$ in finite time, because $v \equiv v_t$ is a solution (the terminal state) and solutions are unique; so $\left|v/v_t\right| \lt 1$ and $\operatorname{atanh}(v/v_t)$ is defined for all $t$; consistently, $\tanh \lt 1$.

##### Position as a function of time
* **Pedagogical Justification:** $s(t) = \int_0^tv\,dt'$. With the substitution $u = gt'/v_t$, $du = (g/v_t)\,dt'$, the limits are $u = 0$ at $t' = 0$ and $u = gt/v_t$ at $t' = t$:
$$ s(t) = v_t\cdot\frac{v_t}{g}\int_0^{gt/v_t}\tanh u\,du = \frac{v_t^2}{g}\Big[\ln\cosh u\Big]_0^{gt/v_t} = \frac{v_t^2}{g}\left[\ln\cosh\frac{gt}{v_t} - \ln\cosh 0\right] $$
$$ \boxed{s(t) = \frac{v_t^2}{g}\ln\left[\cosh\left(\frac{gt}{v_t}\right)\right]} \qquad (\ln\cosh 0 = \ln 1 = 0) $$

### Phase 4: Interpretation & Checks
* **Early times ($t \ll v_t/g$):** $\tanh u \approx u$ gives $v \approx gt$; and $\cosh u \approx 1 + u^2/2$, $\ln\cosh u \approx u^2/2$ give $s \approx \tfrac{1}{2}gt^2$: free fall, the drag is negligible.
* **Late times ($t \gg v_t/g$):** $\tanh u \to 1$, so $v \to v_t$; and $\cosh u \approx \tfrac{1}{2}e^u$ gives $\ln\cosh u \approx u - \ln 2$, so $s \approx v_tt - \dfrac{v_t^2}{g}\ln 2$: uniform descent with a constant delay.
* **Dimensional check:** $[v_t] = \sqrt{\dfrac{\text{kg m s}^{-2}}{\text{kg m}^{-3}\text{m}^2}} = \text{m/s}$; $gt/v_t$ is dimensionless; $[v_t^2/g] = \text{m}$.
* **Check against the official key:** the key of `Problems.pdf` gives the terminal velocity $v_t = \sqrt{2mg/(\rho SC_D)}$, $v(t) = v_t\tanh\left(\frac{g}{v_t}t\right)$ and $s(t) = \frac{v_t^2}{g}\ln\left[\cosh\left(\frac{g}{v_t}t\right)\right]$, identical to the results above. Numerical integration of $\dot{v} = 1 - v^2$, $\dot{s} = v$ (units $g = v_t = 1$) up to $t = 1$ gives $v = 0.761594 = \tanh 1$ and $s = 0.433781 = \ln\cosh 1$.

---

## 📌 Problem 17: Linear Central Force

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a heavy particle $M$ of mass $m$ is attracted to the fixed point $O$ by a force proportional to its mass and to the distance, with coefficient $k^2$: $\mathbf{F}_c = -mk^2\mathbf{r}$. The axis $Oz$ is vertical (upward) and gravity acts along $-Oz$.
* **Constraints:** none; the particle is free in space, so $\text{CDOF} = 3$, with the Cartesian coordinates $(x, y, z)$.
* **Initial state:** $(x_0, y_0, z_0) = \left(\sqrt{3}g/k^2,\ 0,\ 0\right)$ and $(\dot{x}_0, \dot{y}_0, \dot{z}_0) = \left(0,\ 2g/k,\ 0\right)$.
* **Parameters:** $m$ [kg], $g$ [m/s$^2$], $k$ [s$^{-1}$].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $\mathcal{F}_0 = \{O; \mathbf{i}, \mathbf{j}, \mathbf{k}\}$ with its origin at the centre of attraction and $\mathbf{k}$ vertical upward (constant unit vectors).

### Phase 3: Derivation

#### 3.1 Kinematics
$$ \mathbf{r} = x\,\mathbf{i} + y\,\mathbf{j} + z\,\mathbf{k}, \qquad \mathbf{v} = \dot{x}\,\mathbf{i} + \dot{y}\,\mathbf{j} + \dot{z}\,\mathbf{k}, \qquad \mathbf{a} = \ddot{x}\,\mathbf{i} + \ddot{y}\,\mathbf{j} + \ddot{z}\,\mathbf{k} $$

#### 3.2 Forces
* **Applied forces:** the linear central attraction $\mathbf{F}_c = -mk^2\mathbf{r}$ and the weight $\mathbf{F}_g = -mg\,\mathbf{k}$. **Constraint forces:** none. **Inertia forces:** none.

#### 3.3 Equations of Motion
* **Newton's second law in $S_0$:** $m\ddot{\mathbf{r}} = -mk^2\mathbf{r} - mg\,\mathbf{k}$.
* **Pedagogical Justification:** the system is linear and the basis is Cartesian and constant, so the vector equation decouples into three independent scalar equations with constant coefficients: three unknowns, three equations.
$$ \ddot{x} + k^2x = 0, \qquad \ddot{y} + k^2y = 0, \qquad \ddot{z} + k^2z = -g $$

#### 3.4 Integration and Answers
##### Integration of each component
* **$x$ and $y$ (homogeneous oscillators):** the equation $\ddot{x} + k^2x = 0$ is linear with constant coefficients and its characteristic equation $r^2 + k^2 = 0$ has the roots $\pm ik$ (the characteristic-equation method of Notes Eq. 5.20, Sec. 5.3), so the general solution is $A\cos kt + B\sin kt$ (Notes Sec. 5.1, Eq. 5.7). Its velocity follows from the chain rule, $\frac{d}{dt}\cos kt = -k\sin kt$ and $\frac{d}{dt}\sin kt = k\cos kt$: $\dot{x} = -kA\sin kt + kB\cos kt$. The initial conditions give
$$ x(0) = A_x = \frac{\sqrt{3}g}{k^2},\ \ \dot{x}(0) = kB_x = 0 \implies x(t) = \frac{\sqrt{3}g}{k^2}\cos kt $$
$$ y(0) = A_y = 0,\ \ \dot{y}(0) = kB_y = \frac{2g}{k} \implies B_y = \frac{2g}{k^2} \implies y(t) = \frac{2g}{k^2}\sin kt $$
* **$z$ (forced by gravity):** a particular solution of $\ddot{z} + k^2z = -g$ is the constant $z_p = -g/k^2$, so $z(t) = -\dfrac{g}{k^2} + A_z\cos kt + B_z\sin kt$. The initial conditions give $z(0) = -\dfrac{g}{k^2} + A_z = 0$, so $A_z = \dfrac{g}{k^2}$, and $\dot{z}(0) = kB_z = 0$:
$$ z(t) = \frac{g}{k^2}\left(\cos kt - 1\right) $$
* **Trajectory:** $\displaystyle\mathbf{r}(t) = \frac{\sqrt{3}g}{k^2}\cos kt\,\mathbf{i} + \frac{2g}{k^2}\sin kt\,\mathbf{j} + \frac{g}{k^2}\left(\cos kt - 1\right)\mathbf{k}$.

##### (a) Shape of the path
* **Pedagogical Justification:** a linear relation among the coordinates indicates a plane, and a constant distance to a point indicates a sphere; their intersection is a circle.
* **Plane.** From $x = \frac{\sqrt{3}g}{k^2}\cos kt$ we have $\cos kt = \frac{k^2}{\sqrt{3}g}x$, so $z = \frac{g}{k^2}\cos kt - \frac{g}{k^2} = \frac{x}{\sqrt{3}} - \frac{g}{k^2}$, i.e.
$$ x - \sqrt{3}\,z = \frac{\sqrt{3}g}{k^2} $$
* **Sphere.** The squared distance to the point $C = \left(0, 0, -g/k^2\right)$ is
$$ x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2 = \frac{3g^2}{k^4}\cos^2kt + \frac{4g^2}{k^4}\sin^2kt + \frac{g^2}{k^4}\cos^2kt = \frac{4g^2}{k^4}\left(\cos^2kt + \sin^2kt\right) = \frac{4g^2}{k^4} $$
a sphere of centre $C$ and radius $R = 2g/k^2$.
* **Circle.** The centre $C$ lies on the plane: $0 - \sqrt{3}\left(-g/k^2\right) = \sqrt{3}g/k^2$. The intersection of a sphere with a plane through its centre is a **great circle** of radius $R = 2g/k^2$.

##### (b) Velocity as a function of time
* Differentiating each component with the chain rule:
$$ \dot{x} = \frac{\sqrt{3}g}{k^2}\left(-k\sin kt\right), \qquad \dot{y} = \frac{2g}{k^2}\left(k\cos kt\right), \qquad \dot{z} = \frac{g}{k^2}\left(-k\sin kt\right) $$
$$ \mathbf{v}(t) = -\frac{\sqrt{3}g}{k}\sin kt\,\mathbf{i} + \frac{2g}{k}\cos kt\,\mathbf{j} - \frac{g}{k}\sin kt\,\mathbf{k} $$
* **Modulus:** $\|\mathbf{v}\|^2 = \dfrac{g^2}{k^2}\left[3\sin^2kt + 4\cos^2kt + \sin^2kt\right] = \dfrac{g^2}{k^2}\cdot 4\left(\sin^2kt + \cos^2kt\right) = \dfrac{4g^2}{k^2}$, so $\|\mathbf{v}\| = \dfrac{2g}{k}$: the speed is constant.

### Phase 4: Interpretation & Checks
* **Uniform circular motion:** the particle describes a great circle of radius $R = 2g/k^2$ at constant speed $v = 2g/k$, with angular frequency $\omega = v/R = k$.
* **Shifted centre:** the linear central force plus the uniform gravity is equivalent to a spring centred at the equilibrium point $C$ where $k^2z_{\text{eq}} = -g$, i.e. $z_{\text{eq}} = -g/k^2$.
* **Consistency:** the centripetal acceleration $v^2/R = (4g^2/k^2)/(2g/k^2) = 2g$ equals the effective spring acceleration $k^2R = 2g$.
* **Role of $k$:** the initial data are themselves multiples of $g/k^2$ ($x_0 = \sqrt{3}\,g/k^2$, $\dot{y}_0 = 2g/k$), so the solution is self-similar: $R$, $|z_{\text{eq}}|$ and $x_0$ all scale with $g/k^2$, the angular frequency is $k$, and the geometry (offset over radius $|z_{\text{eq}}|/R = 1/2$, tilt of the plane, ratio $1/2$ of gravity to central force on the orbit) does not depend on $k$. A larger $k$ only shrinks the same orbit; gravity never becomes negligible for these data.
* **Dimensional check:** $[g/k^2] = \dfrac{\text{m s}^{-2}}{\text{s}^{-2}} = \text{m}$, $[g/k] = \text{m/s}$, $[R] = \text{m}$ and $\omega = v/R = k$ in s$^{-1}$.
* **Check against the official key:** the key of `Problems.pdf` gives $\mathbf{r}_0^M = \frac{\sqrt{3}g}{k^2}\cos kt\,\mathbf{i} + \frac{2g}{k^2}\sin kt\,\mathbf{j} + \frac{g}{k^2}\left(\cos kt - 1\right)\mathbf{k}$, the circle as the intersection of the sphere $x^2 + y^2 + (z + g/k^2)^2 = 4g^2/k^4$ with the plane $x - \sqrt{3}z = \sqrt{3}g/k^2$, and the constant speed $2g/k$. All coincide with the results above. Sympy confirms $\ddot{\mathbf{r}} + k^2\mathbf{r} + g\mathbf{k} = \mathbf{0}$, the initial data, $\|\mathbf{v}\|^2 = 4g^2/k^2$, the plane and the sphere with zero residual.

---

## 📌 Problem 45: Vibrating Rotor (Unbalanced Turbojet)

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** a rigid disk of mass $m$ rotates at the constant angular velocity $\omega$. Its geometric centre $C$ is held near the design position $O$ by an elastic restoring force with constant $k$; its centre of mass $G$ is at the fixed distance $\ell$ from $C$ (unbalance).
* **Hypotheses:** planar motion in $Oxy$; the weight is negligible; the spring has zero natural length and acts at $C$, so its force is $-k\,\mathbf{r}_C$. As the statement asks, the dynamics is that of the centre of mass $G$, treated as a particle of mass $m$ under the resultant external force (the particle model of Topic 2). The drive that keeps $\omega$ constant applies a pure couple, with zero resultant force, so it does not enter the equation of $G$. The statement also assumes that the homogeneous solution of the equation of $G$ decays, which implies some damping that the model leaves out.
* **Constraints and degrees of freedom:** the disk rotates at the prescribed rate, so its orientation is $\omega t$ (a time-dependent, rheonomic constraint) and the segment $CG$ has the fixed length $\ell$ and the angle $\omega t$. The only free coordinates are the two coordinates of $C$ (or of $G$): $\text{CDOF} = 2$.
* **Unknowns:** $x_0^G(t)$, $y_0^G(t)$, $x_0^C(t)$, $y_0^C(t)$.
* **Parameters:** $m$ [kg], $k$ [N/m], $\ell$ [m], $\omega$ [rad/s]; natural frequency $\omega_0 = \sqrt{k/m}$.

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}_0, \mathbf{j}_0, \mathbf{k}_0\}$, with $\mathbf{r}_C = x_0^C\,\mathbf{i}_0 + y_0^C\,\mathbf{j}_0$ and $\mathbf{r}_G = x_0^G\,\mathbf{i}_0 + y_0^G\,\mathbf{j}_0$.
* **Disk-fixed basis.** It is the inertial basis rotated by $\omega t$ about $\mathbf{k}_0$:
$$ [{}_0 R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \\ \sin\omega t & \cos\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det[{}_0 R_1] = \cos^2\omega t + \sin^2\omega t = 1, \qquad [{}_0 R_1][{}_0 R_1]^T = \begin{pmatrix} \cos^2\omega t + \sin^2\omega t & 0 & 0 \\ 0 & \sin^2\omega t + \cos^2\omega t & 0 \\ 0 & 0 & 1 \end{pmatrix} = I $$
Multiplying out, $RR^T$ has diagonal entries $\cos^2 + \sin^2 = 1$ of the rotation angle (and $1$) and off-diagonal entries $\pm(\cos\sin - \sin\cos) = 0$, so it is the identity.
* **Unbalance vector.** The segment $CG$ is fixed in the disk, at the angle $\omega t$ from $\mathbf{i}_0$ (first column of the matrix):
$$ \mathbf{r}_G = \mathbf{r}_C + \ell\,\mathbf{e}(t), \qquad \mathbf{e}(t) = \cos\omega t\,\mathbf{i}_0 + \sin\omega t\,\mathbf{j}_0 $$

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the dynamics refers to $G$, but the force depends on $C$, so we express $\mathbf{r}_C$ with the geometry of the rotating segment. The acceleration of $G$ in $S_0$ is $\ddot{\mathbf{r}}_G = \ddot{x}_0^G\,\mathbf{i}_0 + \ddot{y}_0^G\,\mathbf{j}_0$, and
$$ \mathbf{r}_C = \mathbf{r}_G - \ell\,\mathbf{e}(t) $$

#### 3.2 Forces
* **Applied force:** the spring force $-k\,\mathbf{r}_C$, which depends on the position of $C$, not on that of $G$. **Constraint forces:** none that affect the centre of mass (the weight is neglected and the drive is a pure couple). **Inertia forces:** none, $S_0$ is inertial.

#### 3.3 Equations of Motion
* **Pedagogical Justification:** Newton's second law for $G$ with $\mathbf{r}_C = \mathbf{r}_G - \ell\,\mathbf{e}(t)$ gives a forced linear equation (Notes Sec. 5.4, oscillator under a periodic force):
$$ m\ddot{\mathbf{r}}_G = -k\,\mathbf{r}_C = -k\left[\mathbf{r}_G - \ell\,\mathbf{e}(t)\right] $$
* Dividing by $m$ with $\omega_0^2 = k/m$, and eliminating $\mathbf{r}_C$ through the geometric relation of 3.1 (so the unknowns reduce to the two coordinates of $G$), the two components decouple (two unknowns, two equations):
$$ \ddot{x}_0^G + \omega_0^2x_0^G = \omega_0^2\ell\cos\omega t, \qquad \ddot{y}_0^G + \omega_0^2y_0^G = \omega_0^2\ell\sin\omega t $$

#### 3.4 Integration and Answers
##### Particular solution for $G$
* **Pedagogical Justification:** the general solution is the homogeneous one, $A\cos\omega_0t + B\sin\omega_0t$, which the statement assumes damped out, plus a particular solution. Since the forcing is harmonic at $\omega$, we try the same harmonic with an unknown amplitude (undetermined coefficients): $x_0^G = a\cos\omega t$, so $\ddot{x}_0^G = -\omega^2a\cos\omega t$.
$$ -\omega^2a + \omega_0^2a = \omega_0^2\ell \implies a = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2} \qquad (\omega \ne \omega_0) $$
* The same steps with $y_0^G = b\sin\omega t$, $\ddot{y}_0^G = -\omega^2b\sin\omega t$, give $-\omega^2b + \omega_0^2b = \omega_0^2\ell$, so $b = a$:
$$ \boxed{x_0^G(t) = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\cos\omega t}, \qquad y_0^G(t) = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\sin\omega t $$

##### Position of the geometric centre
* From $\mathbf{r}_C = \mathbf{r}_G - \ell\,\mathbf{e}(t)$, component by component:
$$ \boxed{x_0^C(t) = \left[\frac{\omega_0^2}{\omega_0^2 - \omega^2} - 1\right]\ell\cos\omega t = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t}, \qquad y_0^C(t) = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\sin\omega t $$

##### Is $|OC| \gt |OG|$ for $\omega \gt \sqrt{k/m}$?
* Both points describe circles about $O$ at the rotation rate $\omega$, with radii
$$ |OG| = \frac{\omega_0^2\ell}{\left|\omega_0^2 - \omega^2\right|}, \qquad |OC| = \frac{\omega^2\ell}{\left|\omega_0^2 - \omega^2\right|}, \qquad \frac{|OC|}{|OG|} = \frac{\omega^2}{\omega_0^2} = \frac{m\omega^2}{k} $$
* **Yes.** The ratio exceeds $1$ exactly when $\omega \gt \omega_0 = \sqrt{k/m}$ (the case $\omega = \omega_0$ is excluded: the bounded harmonic particular solution $a\cos\omega t$ does not exist there, and the response grows linearly in time, $x_0^G = \tfrac{1}{2}\omega_0\ell\,t\sin\omega_0t$, which is the resonance: with $x_p = Dt\sin\omega_0t$, $\ddot{x}_p = 2D\omega_0\cos\omega_0t - D\omega_0^2t\sin\omega_0t$, so $\ddot{x}_p + \omega_0^2x_p = 2D\omega_0\cos\omega_0t = \omega_0^2\ell\cos\omega_0t$ and $D = \omega_0\ell/2$). For $\omega \lt \omega_0$ the opposite holds.

### Phase 4: Interpretation & Checks
* **Slow rotation ($\omega \to 0$):** $x_0^G \to \ell$ and $x_0^C \to 0$: $C$ sits at $O$ and $G$ at distance $\ell$, as for a static unbalanced disk.
* **Fast rotation ($\omega \gg \omega_0$):** $|OG| \to \ell\omega_0^2/\omega^2 \to 0$ and $|OC| \to \ell$: above the critical speed the disk self-centres and spins about its centre of mass, with $C$ circling $G$ at radius $\ell$ and in antiphase with the unbalance (the factor $\omega_0^2 - \omega^2$ is negative).
* **Resonance ($\omega = \omega_0$):** the amplitudes diverge in this undamped model.
* **Dimensional check:** $\left[\omega_0^2\ell/(\omega_0^2 - \omega^2)\right] = \text{m}$ and $[k/m] = \text{N m}^{-1}\text{kg}^{-1} = \text{s}^{-2} = [\omega^2]$.
* **Check against the official key:** the key of `Problems.pdf` gives, for $\omega \ne \omega_0$, $x_0^G(t) = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\cos\omega t$ and $x_0^C(t) = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t$, with $\omega_0 = \sqrt{k/m}$, identical to the results above. Sympy confirms that the particular solution satisfies the equations with zero residual.

---

## 📌 Problem 46: Bumpy Taxiway

### Phase 1: Constraints, Degrees of Freedom & Coordinates
* **System:** the airplane is modelled as a heavy particle $P$ of mass $m$ on a landing gear of stiffness $k$ and nominal (unloaded) length $L$ that rolls at the horizontal speed $c$ on the runway $y_1 = \sin x$. In part (c) a damper of constant $\lambda$ acts between the fuselage and the wheel.
* **Constraints:** the particle moves only vertically (the horizontal motion at speed $c$ is prescribed and does not enter the vertical dynamics), and the wheel stays on the ground: $y_b(t) = \sin(ct)$ with $x = ct$. This is a prescribed, time-dependent (rheonomic) base motion. The wheel contact is a unilateral constraint, assumed to remain active.
* **Degrees of freedom:** $\text{CDOF} = 1$, with the height $y$ of $P$.
* **Hypotheses:** the profile is written with unit wavenumber ($1\ \text{m}^{-1}$), so the excitation has angular frequency $\Omega = c$ (rad/s when $c$ is in m/s); gravity acts on $m$; the gear is linear.
* **Parameters:** $m$ [kg], $k$ [N/m], $L$ [m], $c$ [m/s], $g$ [m/s$^2$], $\omega_0 = \sqrt{k/m}$ [rad/s], $\lambda$ [N s/m].

### Phase 2: Reference Frames & Vector Bases
* **Inertial frame:** $S_0 = \{O; \mathbf{i}, \mathbf{j}\}$ with $Oy$ vertical upward (constant unit vectors).

### Phase 3: Derivation

#### 3.1 Kinematics
* **Pedagogical Justification:** the particle moves along the vertical, and the length of the spring is the distance between $P$ and the ground point under the wheel:
$$ \mathbf{r}_P = y\,\mathbf{j}, \qquad \mathbf{a}_P = \ddot{y}\,\mathbf{j}, \qquad y_b(t) = \sin(ct), \qquad \dot{y}_b = c\cos(ct), \qquad \ell_s = y - y_b $$

#### 3.2 Forces
* **Weight:** $-mg\,\mathbf{j}$. **Spring force:** $-k\left(\ell_s - L\right)\mathbf{j}$ (upward when compressed). **Damper (part c):** $-\lambda\left(\dot{y} - \dot{y}_b\right)\mathbf{j}$, proportional to the relative velocity between the fuselage and the wheel. **Inertia forces:** none.

#### 3.3 Equations of Motion
* **Newton's second law along $Oy$:**
$$ m\ddot{y} = -k\left[y - \sin(ct) - L\right] - mg $$
* The constant weight only shifts the equilibrium. With $y = z + L - mg/k$ (so $\ddot{y} = \ddot{z}$ and $-k(y - L) - mg = -kz$), $z$ measures the motion about the static equilibrium over flat ground:
$$ m\ddot{z} = -kz + k\sin(ct) \implies \ddot{z} + \omega_0^2z = \omega_0^2\sin(ct) $$

#### 3.4 Integration and Answers
##### (a) Resonance
* **Pedagogical Justification:** this is a harmonic oscillator forced at the angular frequency $\Omega = c$ by the base motion (Notes Sec. 5.4). Resonance occurs when the forcing frequency equals the natural frequency: the amplitude of the forced response, $A = \omega_0^2/(\omega_0^2 - c^2)$ derived in (b) below, diverges at $c = \omega_0$. There the trial $A\sin(ct)$ fails (it solves the homogeneous equation) and the particular solution is $z_p = -\tfrac{1}{2}\omega_0t\cos(\omega_0t)$ (check: $\ddot z_p + \omega_0^2z_p = \omega_0^2\sin(\omega_0t)$), which grows linearly in time, as in Problem 45.
$$ \boxed{c_{\text{res}} = \omega_0 = \sqrt{\frac{k}{m}}} $$
For a profile of general wavelength $\Lambda$ the resonant speed would be $c = \omega_0\Lambda/2\pi$ (here $\Lambda = 2\pi$).

##### (b) Amplitude at very high speed
* **Pedagogical Justification:** the motion is the free oscillation at $\omega_0$ plus the forced response; with negligible damping the free part does not decay and depends only on the initial conditions. The amplitude asked for is that of the forced part, the particular solution $z_p = A\sin(ct)$ for $c \ne \omega_0$ (in units of the bump height, $1$ m):
$$ \ddot{z}_p = -c^2A\sin ct \implies \left(\omega_0^2 - c^2\right)A = \omega_0^2 \implies A = \frac{\omega_0^2}{\omega_0^2 - c^2} $$
$$ \boxed{|A(c)| = \frac{\omega_0^2}{\left|\omega_0^2 - c^2\right|} \xrightarrow[c \gg \omega_0]{} \frac{\omega_0^2}{c^2} = \frac{k}{mc^2}} $$
For very high speed the amplitude decays as $1/c^2$: the mass cannot follow the fast bumps, and $z_p$ is in antiphase with the road ($A \lt 0$ for $c \gt \omega_0$).

##### (c) Landing gear with damping $\lambda$
* **Pedagogical Justification:** the damper adds $-\lambda\left(\dot{y} - \dot{y}_b\right)$. With $a = \lambda/m = 2\zeta\omega_0$ and the damping ratio $\zeta = \lambda/\left(2\sqrt{km}\right)$:
$$ \ddot{z} + a\dot{z} + \omega_0^2z = \omega_0^2\sin(ct) + ac\cos(ct) $$
* **Transient (homogeneous solution).** The characteristic equation $r^2 + ar + \omega_0^2 = 0$ has the roots $r = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$:
  - Underdamped, $\lambda \lt 2\sqrt{km}$ ($\zeta \lt 1$): $z_h = e^{-\zeta\omega_0t}\left(C_1\cos\omega_dt + C_2\sin\omega_dt\right)$ with $\omega_d = \omega_0\sqrt{1 - \zeta^2}$.
  - Critical, $\lambda = 2\sqrt{km}$ ($\zeta = 1$): $z_h = (C_1 + C_2t)e^{-\omega_0t}$, the fastest return without oscillation.
  - Overdamped, $\lambda \gt 2\sqrt{km}$ ($\zeta \gt 1$): $z_h = C_1e^{r_1t} + C_2e^{r_2t}$ with $r_{1,2} \lt 0$ real, a slower return (the three regimes of Notes Sec. 5.3).
* **Steady state.** The forcing is the imaginary part of $\left(\omega_0^2 + iac\right)e^{ict}$, so with $z_p = \operatorname{Im}\left[He^{ict}\right]$. Substituting $\tilde z = He^{ict}$, the chain rule gives $\dot{\tilde z} = ic\,\tilde z$ and $\ddot{\tilde z} = -c^2\tilde z$, so the equation becomes $\left(\omega_0^2 - c^2 + iac\right)H = \omega_0^2 + iac$ (Notes Sec. 5.2, complex representation):
$$ H = \frac{\omega_0^2 + iac}{\omega_0^2 - c^2 + iac}, \qquad |H|^2 = \frac{\omega_0^4 + a^2c^2}{\left(\omega_0^2 - c^2\right)^2 + a^2c^2} $$
The steady amplitude is $|H|$ and it is always finite. At resonance, $c = \omega_0$: $|H(\omega_0)| = \sqrt{1 + \dfrac{\omega_0^2}{a^2}} = \sqrt{1 + \dfrac{1}{4\zeta^2}}$. For $c \gg \max\left(a, \omega_0^2/a\right)$ (so that the damping term dominates both the numerator and the denominator), $|H| \approx ac/c^2 = a/c = \lambda/(mc)$: it decays only as $1/c$, slower than the undamped $1/c^2$ of part (b).
* **The steady state is the same in the three cases.** The formula $|H|$ does not depend on whether the gear is underdamped, critical or overdamped; only the transient $z_h$ differs, and it dies out in all three.
* **Effect on the results of (a) and (b).** With $r = c/\omega_0$ and $a = 2\zeta\omega_0$ (extension notation; the notes use $\gamma = \lambda/(2m)$, with $\zeta = \gamma/\omega_0$), $|H|^2 = \dfrac{1 + 4\zeta^2r^2}{\left(1 - r^2\right)^2 + 4\zeta^2r^2}$. The resonance is no longer infinite: the maximum of $|H|$ moves below $\omega_0$, to $r_p^2 = \dfrac{\sqrt{1 + 8\zeta^2} - 1}{4\zeta^2} \lt 1$ (with $u = r^2$, $N = 1 + 4\zeta^2u$ and $D = (1 - u)^2 + 4\zeta^2u$, the quotient rule gives $N'D - ND' = 4\zeta^2\left[(1 - u)^2 + 4\zeta^2u\right] - (1 + 4\zeta^2u)\left[-2(1 - u) + 4\zeta^2\right] = 2(1 - u - 2\zeta^2u^2)$, so $d|H|^2/du = 0$ means $2\zeta^2r^4 + r^2 - 1 = 0$), with $|H|_{\max} = 1.47$ for $\zeta = 0.5$ ($r_p = 0.856$) and $1.28$ for $\zeta = 0.7$ ($r_p = 0.788$). At $c = \omega_0$ the value is $|H(\omega_0)| = \sqrt{1 + 1/(4\zeta^2)}$, i.e. $1.41$ and $1.23$.
* **A fixed point of the curve.** At $c = \sqrt{2}\,\omega_0$ ($r^2 = 2$), $|H|^2 = \dfrac{1 + 8\zeta^2}{1 + 8\zeta^2} = 1$ for every $\zeta$: below this speed damping reduces the transmitted amplitude, above it damping increases it. The high-speed decay is only $1/c$.
* **Choice of $\lambda$.** Critical damping gives the fastest return of the transient without oscillation, but a larger $\lambda$ transmits more amplitude above $c = \sqrt{2}\,\omega_0$ and attenuates the bumps at high speed only as $1/c$. A compromise is $\zeta$ somewhat below $1$ (underdamped): it keeps the resonant peak moderate ($1.28$ to $1.47$ for $\zeta = 0.7$ to $0.5$) without overdamping.
* **Effect of the payload.** The mass changes $\omega_0 = \sqrt{k/m}$, so the resonant speed $c_{\text{res}} = \sqrt{k/m}$ is lower for a heavier aircraft, and $\zeta = \lambda/\left(2\sqrt{km}\right) \propto m^{-1/2}$, so a heavier aircraft is less damped. Since $\lambda$ is fixed hardware, it must be chosen so that $\zeta$ stays below $1$ for the lightest payload (to avoid overdamping) and is still large enough to limit the resonant peak for the heaviest one; the lightest payload then has a larger $\zeta$ and a higher resonant speed.

### Phase 4: Interpretation & Checks
* **Dimensional check:** the profile is $y_b = h\sin(\kappa ct)$ with $h = 1$ m and $\kappa = 1$ m$^{-1}$ (Hypotheses), so $\Omega = \kappa c$ is in s$^{-1}$, $[\omega_0^2] = [k/m] = \text{s}^{-2} = [\Omega^2]$, and the forcing $\omega_0^2h\sin(\Omega t)$ is in m/s$^2$; $[a] = [\lambda/m] = \text{N s m}^{-1}\text{kg}^{-1} = \text{s}^{-1}$, so $\zeta = a/(2\omega_0)$ is dimensionless.
* **Limits:** $c \to 0$ gives $|A| \to 1$ (the airplane follows the road quasi-statically); $\lambda \to 0$ in $|H|$ recovers $|A|$; for $\zeta \to \infty$ at fixed $c$, $|H| \to 1$ for every speed (the gear locks and the airplane follows the road); the $|H| \approx \lambda/(mc)$ regime needs $c \gg \max\left(\lambda/m,\ \omega_0^2m/\lambda\right)$ (otherwise the response still decays as $\omega_0^2/c^2$).
* **Check against the official key:** `Problems.pdf` has no entry for Problem 46 in its solution keys, so the results are verified by independent derivation. Sympy confirms that the undamped particular solution and the damped steady state satisfy their equations with zero residual; numerical integration of the damped equation ($\omega_0 = 1.7$, $a = 0.6$, $c = 2.3$, over $120$ s) gives a steady amplitude of $1.156806$, equal to $|H| = 1.156806$, and $|H(\omega_0)|^2 = 9.0278 = 1 + \omega_0^2/a^2$.
