---
title: "Solution Set - Topic 2: Point Particle Dynamics"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full solutions with derivation boxes (lecturer's order)"
language: "English"
tags:
  - solutions
  - point-particle-dynamics
---

# Topic 2: Point Particle Dynamics - Full Analytical Solutions

Full step-by-step solutions, with derivation boxes, for the 10 problems of Topic 2 (**Point Particle Dynamics**) of *Mechanics Applied to Aerospace Engineering* (UC3M). Every solution follows the order of the lecturer: reference frames, bases and coordinates; change of basis and position vector; kinematics; forces and equations of motion; answers and checks. Each development sits in a derivation box with the law it uses, its source, explicit derivatives (product and chain rules) and explicit integrals (primitive, substitution and Barrow's rule), the SI check and the physical meaning.

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
> **Units:** $E_0$ in $[\mathrm{M\,L^2\,T^{-2}}]$, $v_1$ in $[\mathrm{L\,T^{-1}}]$; each limit keeps these dimensions
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

The particle moves along the axis $Ox$ of an inertial frame and its potential energy is given. The study follows the energy method of Notes.pdf, Sec. 4.5 and Notes.pdf, Sec. 4.6 and [Lecture 2, Slide 20]: the force and the equilibrium points come from the derivatives of the potential, the sketch from its extrema and limits, and the types of motion from the allowed regions where the potential does not exceed the mechanical energy.

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
> **Meaning:** for $0 \lt x \lt a$ the force is negative (towards the origin) and for $x \gt a$ it is positive (away from it): inside the barriers the force pulls towards $O$, outside them it pushes away from $O$ (symmetrically for negative $x$).

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
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; [Lecture 2, Slide 22]
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

The force along $\mathbf i$ is the conservative one; the normal forces balance (figure above; Notes.pdf, Eq. 4.5). $S_0$ is inertial: no inertia forces.

> [!derivation] Equation of motion and energy integral
> **Law:** Newton's second law in $\mathcal B_0$; multiplication by the velocity and chain rule
> **Source:** Notes.pdf, Eq. 4.21; Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.26; Notes.pdf, Eq. 4.27
>
> $$\begin{aligned}
> m\,\ddot x\,\mathbf i &= -\frac{dV}{dx}\,\mathbf i + R_y\,\mathbf j + R_z\,\mathbf k \quad &\text{(second law in $\mathcal B_0$, force from the potential)} \\
> m\,\ddot x &= -\frac{dV}{dx},\quad R_y = R_z = 0 \quad &\text{(components along $\mathbf i$, $\mathbf j$ and $\mathbf k$)} \\
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
> \sqrt{\frac{m}{2\left[V(a) - V(x)\right]}} &= \frac{1}{\omega_0\sqrt{a^2 - x^2}\,\sqrt{1 - b\left(a^2 + x^2\right)}} \quad &\text{(both brackets positive for $\lvert x\rvert \lt a$: for $b \gt 0$, $b(a^2+x^2) \lt 2ba^2 \lt 1$; for $b \le 0$ the bracket is at least 1)} \\
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
> \int\cos 2\varphi\,d\varphi &= \frac12\int\cos u\,du = \frac{\sin 2\varphi}{2} \quad &\text{(substitution $u = 2\varphi$, $du = 2\,d\varphi$)} \\
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
| $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$ | resultant of the forces normal to the axis (unknown) | N |
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
> &= a\,\dot y\,\mathbf i \quad &\text{($x = a\,y$ with $a$ constant: constant-factor rule)} \\
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
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; [Lecture 2, Slide 22]
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
> **Law:** Newton's second law in the inertial frame, projected on $\mathbf i$, $\mathbf j$ and $\mathbf k$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.21
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F + \mathbf R_\perp \quad &\text{(Newton's second law; $\mathbf R_\perp = R_y\,\mathbf j + R_z\,\mathbf k$)} \\
> 0 &= R_y, \qquad 0 = R_z \quad &\text{(dot products with $\mathbf j$ and $\mathbf k$)} \\
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
> \frac{d}{dt}\left(\tfrac12 m\dot x^2 + V(x)\right) &= \dot x\left(m\ddot x + \frac{dV}{dx}\right) = 0 \quad &\text{(chain rule on both terms; equation of motion)} \\
> E &= \tfrac{1}{2}m\dot x^2 + V(x) \quad &\text{(definition: kinetic plus potential energy, constant)} \\
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
> **Meaning:** the allowed region is every $y$ up to 2, past the barrier top too; $x = 2a$ is a simple root (a turning point reached in finite time), while $x = -a$ is a double root: the speed vanishes there, but a particle coming from the right reaches it only as $t \to \infty$, so it never goes beyond it.

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
> After the turning point the velocity is negative, so the negative square root is taken; it cannot change sign again before the next zero of the right-hand side, the double root $y = -1$ (the barrier top), which the boxes below show is approached only as $t \to \infty$.
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

**Check against the official key:** Problems.pdf, p. 72, item 13, gives the two legs in exactly the implicit form of the boxes above, the first one for times up to the turning instant (written there as the square root of $2a/(3g)$ times the arctanh of one over root three, as here) and the second one after it: **match** (the key does not define $y$; it is read as $x/a$, the only reading that makes its expressions dimensionless). The key also states that "the terminal velocity is" the square root of $8ga$; the warning and the box below explain that this value is the initial and largest speed. A Runge-Kutta integration of the equation of motion with unit values of $g$ and $a$ reproduces the explicit law ($y$ equal to 1.759553 at $t$ equal to 0.3 s, the turning point at 0.537646 s, $y$ equal to -0.683994 at 2 s).

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

The particle moves along the axis $Ox$ of an inertial frame under a force that depends only on its abscissa, so the force is conservative and the mechanical energy is constant. The types of motion follow from the shape of the potential and from the level of the energy fixed by the initial velocity (Notes.pdf, Sec. 4.5 and Notes.pdf, Sec. 4.6; [Lecture 2, Slide 20]).

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
> The force depends only on $x$, so the potential exists. The reference is the initial point, $V(a) = 0$. In the integral take the factor $x'$ to differentiate and the exponential to integrate: the exponential is integrated with the substitution of the next rows.
>
> $$\begin{aligned}
> V(x) &= -\int_a^x mK x'\,e^{x'/a}\,dx' \quad &\text{(definition of the potential, reference at $x' = a$)} \\
> \int_a^x a\,e^{x'/a}\,dx' &= a^2\int_1^{x/a} e^{u}\,du = a^2\left[e^u\right]_1^{x/a} \quad &\text{(substitution $u = x'/a$, $du = dx'/a$; limits $1$ and $x/a$)} \\
> \int_a^x x'\,e^{x'/a}\,dx' &= \left[a\,x'\,e^{x'/a}\right]_a^x - \int_a^x a\,e^{x'/a}\,dx' \quad &\text{(integration by parts; $a\,e^{x'/a}$ has derivative $e^{x'/a}$ by the chain rule)} \\
> &= \left(a\,x\,e^{x/a} - a^2 e\right) - a^2\left[e^u\right]_1^{x/a} \quad &\text{(Barrow's rule on the first term; the substitution above for the second)} \\
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
> **Source:** Notes.pdf, Eq. 4.32; Notes.pdf, Sec. 4.6; [Lecture 2, Slide 22]
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
> **Meaning:** the particle creeps up to the unstable equilibrium at the barrier top. The linearised equation there, $\ddot x$ equal to $K x$, gives the exponential approach $x$ proportional to $e^{-\sqrt K\,t}$ on the separatrix.

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
> **Units:** $[\mathrm{L}]$ for the turning point, $[\mathrm{L\,T^{-1}}]$ for $v_c$
> **Meaning:** the three regimes join continuously: the turning point moves from the launch point to the barrier top as the launch speed grows to its critical value.

| Initial speed | Type of motion |
| :--- | :--- |
| $v_0 \lt  a\sqrt{2K}$ | decelerates, stops at $x^* \in (0, a)$ with $(1 - x^*/a)e^{x^*/a} = v_0^2/(2Ka^2)$, is reflected and moves towards $+\infty$ |
| $v_0 = a\sqrt{2K}$ | approaches the unstable equilibrium $x = 0$ asymptotically: it needs an infinite time to reach it |
| $v_0 \gt  a\sqrt{2K}$ | crosses $x = 0$ with speed $\sqrt{v_0^2 - 2Ka^2}$ and moves towards $-\infty$, its speed tending to $v_0$ |

**Check against the official key:** Problems.pdf, p. 72, item 14 (with the constant written $k$): if the initial speed exceeds $a\sqrt{2k}$ the particle moves towards minus infinity; if it is smaller, the particle moves towards infinity after decelerating before arriving at $x$ equal to zero; if it is equal, it takes an infinite time to reach $x$ equal to zero. The three regimes above agree with it: **match**. The potential and its derivatives were also checked by finite differences, and the turning point of the example by bisection.

---

## Problem 15: Stokes Drag and Terminal Velocity

### Reference Frames, Bases and Coordinates

The sphere is modelled as a point particle $P$ of mass $m$ that falls along a vertical line through a fluid at rest in an inertial frame. Three forces act on it, as the statement imposes: its weight, the buoyancy of the fluid and the Stokes drag. The statement asks for the terminal velocity and for the position as a function of time when the sphere starts from rest (Problems.pdf, p. 9). The axis of the fall points downward, the convention of the official key, so that the velocity component stays positive.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ attached to the fluid at rest, origin $O$ at the release point (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ vertical **downward**, $\mathbf j$ and $\mathbf k$ horizontal, right-handed ($\mathbf i \times \mathbf j = \mathbf k$) |
| Moving frames | none: the only basis used is $\mathcal B_0$ |
| Coordinate | $x(t)$, distance fallen, measured along $\mathbf i$ from $O$; $v = \dot x$ its rate |
| Data | $r$ [m] radius; $\rho_0$ [kg m$^{-3}$] density of the fluid; $\rho_s = 2\rho_0$ density of the sphere; $\mu$ [kg m$^{-1}$ s$^{-1}$] dynamic viscosity; $\nu = \mu/\rho_0$ [m$^2$ s$^{-1}$] kinematic viscosity; $g$ [m s$^{-2}$] gravity |
| Derived data | volume $V = \tfrac43\pi r^3$; mass $m = \rho_s V = \tfrac83\pi\rho_0 r^3$ |
| Applied forces | weight $m g\,\mathbf i$; buoyancy, the weight of the displaced fluid, $-\rho_0 V g\,\mathbf i$; Stokes drag of magnitude $6\pi\mu r v$, opposite to the velocity (statement) |
| Initial conditions | $\mathbf r_0^P(0) = \mathbf 0$, $\mathbf v_0^P(0) = \mathbf 0$ (released from rest at $O$): $x$, $y$, $z$ and their rates are zero at $t = 0$ |
| Hypotheses | the fluid is unbounded and at rest, so the speed in the drag law is the speed of $P$ in $S_0$; the sphere does not rotate or drift sideways; the buoyancy is the hydrostatic one (Archimedes' principle, imposed by the statement, not derived in Notes.pdf); unsteady fluid forces (added mass, history force) are not considered, as the statement gives only the three forces |
| Constraints | none: the sphere is free; the horizontal coordinates stay zero because every force is vertical (proved in the box of Newton's law) |
| Degrees of freedom | 3 (free particle, no constraint); with these forces and the release from rest only $x$ varies, so the motion is rectilinear |

![[attachments/EM-SOL/p15-fall-axis.svg]]

### Change of Basis and Position Vector

The only basis is $\mathcal B_0$. In the view of the figure $\mathbf i$ points down the page and $\mathbf j$ to the right, so $\mathbf k$, the cross product of $\mathbf i$ and $\mathbf j$ (right-hand rule), points out of the paper (⊙).

> [!derivation] The only basis and its change of basis matrix
> **Law:** change of basis matrix between two bases; orthonormality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> The matrix that writes $\mathcal B_0$ in itself has as columns the components of $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_0$, so it is the identity; it is checked like any rotation matrix.
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
> **Meaning:** no rotation is involved; $\mathcal B_0$ is orthonormal and right-handed even though its first axis points down, and every vector of the problem is written in it.

> [!derivation] Position vector of the sphere
> **Law:** position vector of a point in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(definition of the position vector; $O$ is the release point)} \\
> &= x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(Cartesian components in $\mathcal B_0$)} \\
> &= x\,\mathbf i \quad &\text{(vertical fall: $y = z = 0$, see the box of Newton's law)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = x(t)\,\mathbf i, \qquad x(0) = 0}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** a single function of time, the distance fallen, describes the whole motion.

### Kinematics

> [!derivation] Velocity and acceleration of the sphere
> **Law:** velocity and acceleration as time derivatives of the position vector in $S_0$; derivative of a unit vector of a basis that does not rotate
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0}\times\mathbf i = \mathbf 0\times\mathbf i = \mathbf 0 \quad &\text{($\mathcal B_0$ is attached to $S_0$, its angular velocity is zero)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(x\,\mathbf i\right) = \dot x\,\mathbf i + x\,\frac{d\mathbf i}{dt} \quad &\text{(definition of velocity; product rule)} \\
> &= \dot x\,\mathbf i \quad &\text{($\mathbf i$ is constant)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(\dot x\,\mathbf i\right) = \ddot x\,\mathbf i + \dot x\,\frac{d\mathbf i}{dt} = \ddot x\,\mathbf i \quad &\text{(definition of acceleration; product rule; $\mathbf i$ constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = \dot x\,\mathbf i, \qquad \mathbf a_0^P = \ddot x\,\mathbf i}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ for the derivative of the unit vector (zero); $[\mathrm{L\,T^{-1}}]$ for the velocity; $[\mathrm{L\,T^{-2}}]$ for the acceleration
> **Meaning:** velocity and acceleration are vertical; a positive rate of the coordinate means the sphere moves down.

### Forces and Equations of Motion

The free-body diagram shows the weight, the buoyancy and the drag, drawn for a sphere that moves down. The sphere is free, so no reaction acts, and $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p15-fbd.svg]]

> [!derivation] Forces on the sphere
> **Law:** weight in a uniform gravity field; hydrostatic buoyancy; Stokes drag opposite to the velocity relative to the fluid
> **Source:** Problems.pdf, p. 9; Notes.pdf, Eq. 4.4
>
> The drag points along minus the unit vector of the velocity. The box of the sign of the velocity, below, proves that the velocity component is positive for every positive time, so that unit vector is $\mathbf i$.
>
> $$\begin{aligned}
> \mathbf F_g &= m\,g\,\mathbf i = \tfrac83\pi\rho_0 r^3 g\,\mathbf i \quad &\text{(weight; mass $\rho_s V$ with $\rho_s = 2\rho_0$)} \\
> \mathbf F_B &= -\rho_0 V g\,\mathbf i = -\tfrac43\pi\rho_0 r^3 g\,\mathbf i \quad &\text{(buoyancy: weight of the displaced fluid, upward)} \\
> \mathbf F_D &= -6\pi\mu r\,|\dot x|\,\frac{\dot x\,\mathbf i}{|\dot x|} = -6\pi\mu r\,\dot x\,\mathbf i \quad &\text{(magnitude of the statement times minus the unit vector of the velocity)} \\
> &= -6\pi\rho_0\nu r\,\dot x\,\mathbf i \quad &\text{(dynamic viscosity written as $\rho_0\nu$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_g = \tfrac83\pi\rho_0 r^3 g\,\mathbf i, \qquad \mathbf F_B = -\tfrac43\pi\rho_0 r^3 g\,\mathbf i, \qquad \mathbf F_D = -6\pi\rho_0\nu r\,\dot x\,\mathbf i}$$
>
> **Units:** $\mathbf F_g$ and $\mathbf F_B$: $[\mathrm{M\,L^{-3}}][\mathrm{L^3}][\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$; $\mathbf F_D$: $[\mathrm{M\,L^{-3}}][\mathrm{L^2\,T^{-1}}][\mathrm{L}][\mathrm{L\,T^{-1}}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the buoyancy cancels half of the weight, because the sphere is twice as dense as the fluid; the drag grows linearly with the speed and opposes the fall.

> [!derivation] Newton's second law projected on the fixed basis
> **Law:** Newton's second law in an inertial frame; projection on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5
>
> The sphere is free: the constraint reaction is the zero vector. The general position has horizontal components, which are carried here to show that they stay zero.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F_g + \mathbf F_B + \mathbf F_D + \mathbf R, \quad \mathbf R = \mathbf 0 \quad &\text{(second law in $S_0$; no constraint)} \\
> m\left(\ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k\right) &= \left(\tfrac83 - \tfrac43\right)\pi\rho_0 r^3 g\,\mathbf i - 6\pi\rho_0\nu r\left(\dot x\,\mathbf i + \dot y\,\mathbf j + \dot z\,\mathbf k\right) \quad &\text{(general motion; the drag is minus the velocity times $6\pi\mu r$)} \\
> \mathbf j, \mathbf k:\quad m\,\ddot y &= -6\pi\rho_0\nu r\,\dot y, \qquad m\,\ddot z = -6\pi\rho_0\nu r\,\dot z \quad &\text{(dot products with $\mathbf j$ and $\mathbf k$)} \\
> y(t) &= z(t) = 0 \quad &\text{(zero initial data solve these linear equations; uniqueness)} \\
> \mathbf i:\quad \tfrac83\pi\rho_0 r^3\,\ddot x &= \tfrac43\pi\rho_0 r^3 g - 6\pi\rho_0\nu r\,\dot x \quad &\text{(dot product with $\mathbf i$; mass written out)} \\
> \ddot x &= \frac{4/3}{8/3}\,g - \frac{6\pi\rho_0\nu r}{\tfrac83\pi\rho_0 r^3}\,\dot x \quad &\text{(division by the mass)} \\
> &= \frac{g}{2} - \frac{9\nu}{4r^2}\,\dot x \quad &\text{($\tfrac{4/3}{8/3} = \tfrac12$; $6\cdot\tfrac38 = \tfrac94$; $\rho_0$, $\pi$ and one $r$ cancel)} \\
> 4r^2\,\ddot x + 9\nu\,\dot x &= 2r^2 g \quad &\text{(multiplication by $4r^2$)}
> \end{aligned}$$
>
> $$\boxed{4r^2\,\ddot x + 9\nu\,\dot x = 2r^2 g, \qquad x(0) = 0, \quad \dot x(0) = 0}$$
>
> **Units:** $[\mathrm{L^2}][\mathrm{L\,T^{-2}}] = [\mathrm{L^2\,T^{-1}}][\mathrm{L\,T^{-1}}] = [\mathrm{L^2}][\mathrm{L\,T^{-2}}]$, all $[\mathrm{L^3\,T^{-2}}]$; the reaction $\mathbf R$ would be $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** one linear equation with constant coefficients for the one unknown; the mass and the fluid density have dropped out, only the radius, the kinematic viscosity and gravity remain, and the effective gravity is half of the real one.

> [!derivation] Rate constant and terminal velocity
> **Law:** the terminal state is the motion with zero acceleration, where the net force vanishes
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 9
>
> $$\begin{aligned}
> \gamma &\equiv \frac{9\nu}{4r^2} \quad &\text{(coefficient of the rate in the equation divided by $4r^2$)} \\
> 0 &= \frac{g}{2} - \gamma\,v_t \quad &\text{(zero acceleration at the constant speed $v_t$)} \\
> v_t &= \frac{g}{2\gamma} = \frac{g}{2}\cdot\frac{4r^2}{9\nu} = \frac{2r^2 g}{9\nu} \quad &\text{(solution for $v_t$; $\gamma$ substituted)} \\
> \ddot x &= \gamma\left(v_t - \dot x\right) \quad &\text{(equation of motion written with $\gamma$ and $v_t$, since $g/2 = \gamma v_t$)}
> \end{aligned}$$
>
> $$\boxed{\gamma = \frac{9\nu}{4r^2}, \qquad v_t = \frac{2r^2 g}{9\nu}, \qquad \frac{dv}{dt} = \gamma\left(v_t - v\right)}$$
>
> **Units:** $[\gamma] = [\mathrm{L^2\,T^{-1}}]/[\mathrm{L^2}] = [\mathrm{T^{-1}}]$; $[v_t] = [\mathrm{L^2}][\mathrm{L\,T^{-2}}]/[\mathrm{L^2\,T^{-1}}] = [\mathrm{L\,T^{-1}}]$; the rate equation $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** the terminal velocity grows with the square of the radius and falls with the viscosity; the rate constant is the inverse of the time scale on which the speed approaches it.

> [!derivation] Sign of the velocity during the fall
> **Law:** Newton's second law with the drag written for either sign of the velocity; uniqueness for a smooth right-hand side (extension, not in Notes.pdf)
> **Source:** Notes.pdf, Eq. 4.6; Problems.pdf, p. 9
>
> The drag of the statement is minus its magnitude times the unit vector of the velocity, so for a velocity $v\,\mathbf i$ of either sign it is minus the factor $\tfrac12\rho S C_D$ times $|v|$ times $v$ along $\mathbf i$. The law below uses no assumption on the sign of $v$.
>
> $$\begin{aligned}
> m\,\frac{dv}{dt} &= m g - \tfrac12\rho S C_D\,|v|\,v \quad &\text{($\mathbf i$ component of the second law; $\mathbf F_D = -\tfrac12\rho v^2 S C_D\,v\,\mathbf i/|v|$)} \\
> \frac{dv}{dt} &= g - \frac{\rho S C_D}{2m}\,|v|\,v \quad &\text{(division by $m$)} \\
> v \le 0 \ \Rightarrow\ \frac{dv}{dt} &= g + \frac{\rho S C_D}{2m}\,v^2 \ge g \gt 0 \quad &\text{($|v|\,v = -v^2$; the velocity cannot become or stay non-positive)} \\
> v(0) = 0,\ \ \frac{dv}{dt}\Big|_{t = 0} &= g \gt 0 \ \Rightarrow\ v(t) \gt 0 \ \text{for small}\ t \gt 0 \quad &\text{(initial condition; positive initial rate)} \\
> v(t_1) = 0,\ t_1 \gt 0 \ \Rightarrow\ \frac{dv}{dt}\Big|_{t_1} &\le 0 \quad &\text{(a first return to zero from positive values; contradicts the third line)} \\
> v(t) \gt 0 \ \Rightarrow\ |v|\,v &= v^2, \quad \frac{dv}{dt} = g - \frac{\rho S C_D}{2m}\,v^2 = \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \quad &\text{(only now the $v^2$ form; terminal speed box)} \\
> v(t) &\equiv v_t \ \text{solves this equation} \quad &\text{(zero right-hand side)} \\
> v(0) = 0 \lt v_t \ \Rightarrow\ v(t) &\lt v_t \ \text{for every}\ t \quad &\text{(two solutions of the same equation cannot cross: uniqueness, extension)} \\
> \frac{dv}{dt} &= \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \gt 0 \quad &\text{(positive right-hand side for $0 \lt v \lt v_t$: the speed grows)}
> \end{aligned}$$
>
> $$\boxed{0 \lt v(t) \lt v_t \quad \text{for every } t \gt 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for $v$ and $v_t$; $[\mathrm{L\,T^{-2}}]$ for $g$ and every rate $dv/dt$
> **Meaning:** the ball always falls, so the drag always points up as written in the box of the forces, and the ratio of $v$ to $v_t$ stays inside the interval where the inverse hyperbolic tangent is defined.

### Answers and Checks

#### (a) Terminal velocity

The terminal velocity is the boxed $v_t$ above: the asymptotic state in which drag balances the weight minus the buoyancy.

#### (b) Position as a function of time

> [!derivation] Integration of the velocity
> **Law:** separation of variables, change of variable and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.6; [Lecture 6, Slide 3]
>
> $$\begin{aligned}
> \frac{dv}{v_t - v} &= \gamma\,dt \quad &\text{(separation of variables; $v_t - v \gt 0$ by the sign box)} \\
> \int_0^{v}\frac{dv'}{v_t - v'} &= \gamma\int_0^{t}dt' \quad &\text{(from the release, $t' = 0$ and $v' = 0$, to the current state)} \\
> w &= v_t - v', \quad dw = -dv'; \quad v' = 0 \Rightarrow w = v_t, \quad v' = v \Rightarrow w = v_t - v \quad &\text{(change of variable, its differential and its limits)} \\
> -\int_{v_t}^{v_t - v}\frac{dw}{w} &= \gamma\Big[t'\Big]_0^{t} \quad &\text{(substitution)} \\
> -\Big[\ln w\Big]_{v_t}^{v_t - v} &= \gamma\left(t - 0\right) \quad &\text{(antiderivative $\ln w$, valid for $w \gt 0$; Barrow's rule on the right)} \\
> -\ln\left(v_t - v\right) + \ln v_t &= \gamma t \quad &\text{(Barrow's rule on the left: upper limit minus lower limit)} \\
> \ln\frac{v_t - v}{v_t} &= -\gamma t \quad &\text{(difference of logarithms; sign changed)} \\
> v &= v_t\left(1 - e^{-\gamma t}\right) \quad &\text{(exponential of both sides; solution for $v$)}
> \end{aligned}$$
>
> $$\boxed{v(t) = v_t\left(1 - e^{-\gamma t}\right)}$$
>
> **Units:** $[\gamma t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$; $[v] = [v_t] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the speed starts at zero and approaches the terminal velocity exponentially; after one time $1/\gamma$ it has reached about 63 % of it.

> [!derivation] Integration of the position
> **Law:** definition of velocity; change of variable and Barrow's rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 4.6
>
> $$\begin{aligned}
> x(t) - x(0) &= \int_0^t v_t\left(1 - e^{-\gamma t'}\right)dt' \quad &\text{(the velocity is the rate of the position)} \\
> &= v_t\Big[t'\Big]_0^t - v_t\int_0^t e^{-\gamma t'}\,dt' \quad &\text{(linearity of the integral)} \\
> u &= -\gamma t', \quad du = -\gamma\,dt'; \quad t' = 0 \Rightarrow u = 0, \quad t' = t \Rightarrow u = -\gamma t \quad &\text{(change of variable, its differential and its limits)} \\
> \int_0^t e^{-\gamma t'}\,dt' &= -\frac{1}{\gamma}\int_0^{-\gamma t}e^{u}\,du = -\frac{1}{\gamma}\Big[e^{u}\Big]_0^{-\gamma t} \quad &\text{(substitution; antiderivative $e^u$)} \\
> &= -\frac{1}{\gamma}\left(e^{-\gamma t} - 1\right) = \frac{1 - e^{-\gamma t}}{\gamma} \quad &\text{(Barrow's rule)} \\
> x(t) &= v_t\,t - \frac{v_t}{\gamma}\left(1 - e^{-\gamma t}\right) \quad &\text{($x(0) = 0$; both integrals substituted)} \\
> &= \frac{v_t}{\gamma}\left(\gamma t - 1 + e^{-\gamma t}\right) \quad &\text{(common factor $v_t/\gamma$)}
> \end{aligned}$$
>
> $$\boxed{x(t) = \frac{v_t}{\gamma}\left(\gamma t - 1 + e^{-\gamma t}\right), \qquad \gamma = \frac{9\nu}{4r^2}, \quad v_t = \frac{2r^2 g}{9\nu}}$$
>
> **Units:** $[v_t/\gamma] = [\mathrm{L\,T^{-1}}]/[\mathrm{T^{-1}}] = [\mathrm{L}]$; the bracket and $\gamma t$ are dimensionless; $[x] = [\mathrm{L}]$
> **Meaning:** the distance fallen grows first as in a free fall and then linearly at the terminal velocity, with a constant lag of $v_t/\gamma$.

> [!derivation] The position in the form of the official key
> **Law:** algebraic substitution of the rate constant and of the terminal velocity
> **Source:** Problems.pdf, p. 73
>
> $$\begin{aligned}
> \frac{v_t}{\gamma} &= \frac{2r^2 g}{9\nu}\cdot\frac{4r^2}{9\nu} = \frac{2r^2 g}{81\nu^2}\cdot 4r^2 \quad &\text{(product of the two data; $4r^2$ kept apart)} \\
> 4r^2\left(\gamma t - 1 + e^{-\gamma t}\right) &= 9\nu t - 4r^2 + 4r^2 e^{-\gamma t} \quad &\text{($4r^2\gamma = 9\nu$)} \\
> x(t) &= \frac{2r^2 g}{81\nu^2}\left[-4r^2 + 4r^2\exp\left(-\frac{9\nu}{4r^2}t\right) + 9\nu t\right] \quad &\text{(the two lines combined)}
> \end{aligned}$$
>
> $$\boxed{x(t) = \frac{2r^2 g}{81\nu^2}\left[-4r^2 + 4r^2\exp\left(-\frac{9\nu}{4r^2}\,t\right) + 9\nu t\right]}$$
>
> **Units:** $[\mathrm{L^2}][\mathrm{L\,T^{-2}}]/[\mathrm{L^4\,T^{-2}}] = [\mathrm{L^{-1}}]$ for the prefactor, $[\mathrm{L^2}]$ for each term of the bracket, $[\mathrm{L}]$ for $x$; the exponent is dimensionless
> **Meaning:** the same law as above, written term by term as the key prints it.

> [!derivation] Limiting cases: short and long times
> **Law:** Taylor expansion of the exponential; asymptotic behaviour for a large argument
> **Source:** Notes.pdf, Eq. 4.5
>
> $$\begin{aligned}
> e^{-\gamma t} &= 1 - \gamma t + \tfrac12\gamma^2 t^2 + O\!\left(\gamma^3 t^3\right) \quad &\text{(Taylor series for $\gamma t \ll 1$)} \\
> x &\approx \frac{v_t}{\gamma}\cdot\tfrac12\gamma^2 t^2 = \tfrac12\gamma v_t\,t^2 = \tfrac14 g\,t^2 \quad &\text{(the constant and linear terms cancel; $\gamma v_t = g/2$)} \\
> e^{-\gamma t} &\to 0 \quad &\text{($\gamma t \gg 1$)} \\
> x &\approx v_t\,t - \frac{v_t}{\gamma} \quad &\text{(uniform descent with a constant lag)}
> \end{aligned}$$
>
> $$\boxed{\gamma t \ll 1:\ x \approx \tfrac14 g t^2; \qquad \gamma t \gg 1:\ x \approx v_t t - \frac{v_t}{\gamma}}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}][\mathrm{T^2}] = [\mathrm{L}]$ and $[\mathrm{L\,T^{-1}}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** at first the drag is negligible and the sphere falls freely under the effective gravity $g/2$ (weight minus buoyancy, over the mass); at long times it falls at the terminal velocity.

| Part of the statement | Answer |
| :--- | :--- |
| Equation of motion ($x$ positive downward) | $4r^2\ddot x + 9\nu\dot x = 2r^2 g$ |
| (a) Terminal velocity | $v_t = \dfrac{2r^2 g}{9\nu}$, downward |
| (b) Velocity | $v(t) = v_t\left(1 - e^{-9\nu t/(4r^2)}\right)$ |
| (b) Position, from rest at $O$ | $x(t) = \dfrac{2r^2 g}{81\nu^2}\left[-4r^2 + 4r^2 e^{-9\nu t/(4r^2)} + 9\nu t\right]$ |

**Check against the official key:** Problems.pdf, p. 73, item 15, takes the axis positive downward and the release from rest at the origin, and prints the equation of motion and the trajectory written in the last two rows of the table, term by term: **match**. The terminal velocity, not printed in the key, is the slope of that trajectory at long times. A Runge-Kutta integration of the equation of motion with unit values of the radius, the kinematic viscosity and gravity gives a distance of 0.34678 m at the time 2 s, equal to the closed form.

---

## Problem 16: Drag on Falling Football

### Reference Frames, Bases and Coordinates

The football is modelled as a point particle $P$ of mass $m$ that falls along a vertical line through air at rest in an inertial frame. Only two forces act on it, as the statement imposes: its weight and the aerodynamic drag of quadratic law. The statement asks for the terminal speed and for the position as a function of time (Problems.pdf, p. 9). The axis of the fall points downward, the convention of the official key, so that the velocity component stays positive and the drag law needs no absolute value.

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ attached to the still air, origin $O$ at the release point (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ vertical **downward**, $\mathbf j$ and $\mathbf k$ horizontal, right-handed |
| Moving frames | none |
| Coordinate | $s(t)$, distance fallen along $\mathbf i$; $v = \dot s$ its rate |
| Data | $m$ [kg] mass; $S$ [m$^2$] frontal area; $C_D$ [-] drag coefficient; $\rho$ [kg m$^{-3}$] density of the air; $g$ [m s$^{-2}$] gravity |
| Applied forces | weight $m g\,\mathbf i$; drag of magnitude $D = \tfrac12\rho v^2 S C_D$ opposite to the velocity (statement) |
| Initial conditions | $\mathbf r_0^P(0) = \mathbf 0$, $\mathbf v_0^P(0) = \mathbf 0$, so $s(0) = 0$ and $v(0) = 0$ (reading of "falls": released from rest, the initial condition of the official key) |
| Given integrals | $\int dx/(x_0^2 - x^2) = \operatorname{atanh}(x/x_0)/x_0$ and $\int\tanh x\,dx = \ln\cosh x$ (statement; both checked below) |
| Hypotheses | the air is unbounded and at rest, so the speed in the drag law is the speed of $P$ in $S_0$; $\rho$, $S$ and $C_D$ are constant; no buoyancy and no lift (statement: only gravity and drag) |
| Constraints | none: the ball is free; the horizontal coordinates stay zero because both forces are vertical (box of Newton's law) |
| Degrees of freedom | 3 (free particle); only $s$ varies (rectilinear fall) |

![[attachments/EM-SOL/p16-fall-axis.svg]]

### Change of Basis and Position Vector

The only basis is $\mathcal B_0$. In the view of the figure $\mathbf i$ points down the page and $\mathbf j$ to the right, so $\mathbf k$, the cross product of $\mathbf i$ and $\mathbf j$ (right-hand rule), points out of the paper (⊙).

> [!derivation] The only basis and its change of basis matrix
> **Law:** change of basis matrix between two bases; orthonormality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> The matrix that writes $\mathcal B_0$ in itself has as columns the components of $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_0$, so it is the identity; it is checked like any rotation matrix.
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
> **Meaning:** no rotation is involved; $\mathcal B_0$ is orthonormal and right-handed, and the weight has a positive component along its first axis.

> [!derivation] Position vector of the ball
> **Law:** position vector of a point in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^P &= \overrightarrow{OP} \quad &\text{(definition; $O$ is the release point)} \\
> &= s\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(Cartesian components in $\mathcal B_0$)} \\
> &= s\,\mathbf i \quad &\text{(vertical fall: $y = z = 0$, see the box of Newton's law)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = s(t)\,\mathbf i, \qquad s(0) = 0}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** a single function of time, the distance fallen from the release point, describes the whole motion.

### Kinematics

> [!derivation] Velocity and acceleration of the ball
> **Law:** velocity and acceleration as time derivatives of the position vector in $S_0$; derivative of a unit vector of a basis that does not rotate
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \frac{d\mathbf i}{dt} &= \boldsymbol\omega_{B0}\times\mathbf i = \mathbf 0\times\mathbf i = \mathbf 0 \quad &\text{($\mathcal B_0$ is attached to $S_0$)} \\
> \mathbf v_0^P &= \frac{d}{dt}\left(s\,\mathbf i\right) = \dot s\,\mathbf i + s\,\frac{d\mathbf i}{dt} = \dot s\,\mathbf i = v\,\mathbf i \quad &\text{(definition of velocity; product rule; notation $v = \dot s$)} \\
> \mathbf a_0^P &= \frac{d}{dt}\left(v\,\mathbf i\right) = \dot v\,\mathbf i + v\,\frac{d\mathbf i}{dt} = \frac{dv}{dt}\,\mathbf i \quad &\text{(definition of acceleration; product rule; $\mathbf i$ constant)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = v\,\mathbf i, \qquad \mathbf a_0^P = \frac{dv}{dt}\,\mathbf i}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ for the derivative of the unit vector (zero); $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L\,T^{-2}}]$ for velocity and acceleration
> **Meaning:** velocity and acceleration are vertical; the speed of the ball is the absolute value of $v$, which equals $v$ while the ball falls.

### Forces and Equations of Motion

The free-body diagram shows the weight and the drag, drawn for a ball that moves down. The ball is free, so no reaction acts, and $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p16-fbd.svg]]

> [!derivation] Forces on the ball
> **Law:** weight in a uniform gravity field; quadratic drag opposite to the velocity relative to the air
> **Source:** Problems.pdf, p. 9; Notes.pdf, Eq. 4.4
>
> The drag points along minus the unit vector of the velocity. The sign box below proves that the velocity component is positive for every positive time, so that unit vector is $\mathbf i$.
>
> $$\begin{aligned}
> \mathbf F_g &= m\,g\,\mathbf i \quad &\text{(gravity points down, along $+\mathbf i$)} \\
> \mathbf F_D &= -D\,\frac{\mathbf v_0^P}{|\mathbf v_0^P|} = -\tfrac12\rho v^2 S C_D\,\frac{v\,\mathbf i}{|v|} \quad &\text{(drag opposite to the velocity; law of the statement)} \\
> &= -\tfrac12\rho S C_D\,v^2\,\mathbf i \quad &\text{($v \gt 0$ during the fall, so $v/|v| = 1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_g = m g\,\mathbf i, \qquad \mathbf F_D = -\tfrac12\rho S C_D\,v^2\,\mathbf i}$$
>
> **Units:** $\mathbf F_g$: $[\mathrm{M}][\mathrm{L\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$; $\mathbf F_D$: $[\mathrm{M\,L^{-3}}][\mathrm{L^2}][1][\mathrm{L^2\,T^{-2}}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** the weight is constant; the drag grows with the square of the speed and points up while the ball falls.

> [!derivation] Newton's second law projected on the fixed basis
> **Law:** Newton's second law in an inertial frame; projection on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5
>
> The ball is free: the constraint reaction is the zero vector. In a general motion the drag would be minus the factor $\tfrac12\rho S C_D$ times the speed times the velocity vector, so its horizontal components are proportional to the horizontal rates.
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F_g + \mathbf F_D + \mathbf R, \quad \mathbf R = \mathbf 0 \quad &\text{(second law in $S_0$; no constraint)} \\
> \mathbf j, \mathbf k:\quad m\,\ddot y &= -\tfrac12\rho S C_D\,|\mathbf v_0^P|\,\dot y, \qquad m\,\ddot z = -\tfrac12\rho S C_D\,|\mathbf v_0^P|\,\dot z \quad &\text{(dot products with $\mathbf j$ and $\mathbf k$)} \\
> y(t) &= z(t) = 0 \quad &\text{(zero initial data; the zero functions solve both equations; uniqueness)} \\
> \mathbf i:\quad m\,\frac{dv}{dt} &= m g - \tfrac12\rho S C_D\,v^2 \quad &\text{(dot product with $\mathbf i$)} \\
> \frac{dv}{dt} &= g - \frac{\rho S C_D}{2m}\,v^2 \quad &\text{(division by $m$)}
> \end{aligned}$$
>
> $$\boxed{\frac{dv}{dt} = g - \frac{\rho S C_D}{2m}\,v^2, \qquad v(0) = 0, \quad s(0) = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ on both sides: $\frac{[\mathrm{M\,L^{-3}}][\mathrm{L^2}]}{[\mathrm{M}]}[\mathrm{L^2\,T^{-2}}] = [\mathrm{L\,T^{-2}}]$; the reaction $\mathbf R$ would be $[\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** one first-order equation for the one unknown $v$; the position follows from a second integration.

> [!derivation] Terminal speed and the equation written with it
> **Law:** the terminal state is the motion with zero acceleration, where the net force vanishes
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 9
>
> $$\begin{aligned}
> 0 &= g - \frac{\rho S C_D}{2m}\,v_t^2 \quad &\text{(zero acceleration at the constant speed $v_t$)} \\
> v_t^2 &= \frac{2 m g}{\rho S C_D} \quad &\text{(solution for the square of the speed)} \\
> v_t &= +\sqrt{\frac{2 m g}{\rho S C_D}} \quad &\text{(positive root: downward velocity)} \\
> \frac{\rho S C_D}{2m} &= \frac{g}{v_t^2} \quad &\text{(first line rearranged: $\tfrac{\rho S C_D}{2m}\,v_t^2 = g$, divided by $v_t^2$)} \\
> \frac{dv}{dt} &= g - \frac{g}{v_t^2}\,v^2 = \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \quad &\text{(substitution in the equation of motion; common factor)}
> \end{aligned}$$
>
> $$\boxed{v_t = \sqrt{\frac{2 m g}{\rho S C_D}}, \qquad \frac{dv}{dt} = \frac{g}{v_t^2}\left(v_t^2 - v^2\right)}$$
>
> **Units:** $[v_t] = \left(\frac{[\mathrm{M}][\mathrm{L\,T^{-2}}]}{[\mathrm{M\,L^{-3}}][\mathrm{L^2}]}\right)^{1/2} = [\mathrm{L\,T^{-1}}]$; the rate equation $\frac{[\mathrm{L\,T^{-2}}]}{[\mathrm{L^2\,T^{-2}}]}[\mathrm{L^2\,T^{-2}}] = [\mathrm{L\,T^{-2}}]$
> **Meaning:** heavy, small and streamlined balls have a high terminal speed; the acceleration is downward while the speed is below it and vanishes at it.

> [!derivation] Sign of the velocity during the fall
> **Law:** uniqueness of the solution of a first-order differential equation with a smooth right-hand side
> **Source:** Notes.pdf, Eq. 4.6; [Lecture 6, Slide 3]
>
> The constant functions equal to $v_t$ and to minus $v_t$ solve the rate equation (they make the right-hand side vanish). Two different solutions cannot cross, so a solution that starts between them stays between them.
>
> $$\begin{aligned}
> \frac{dv}{dt}\Big|_{t = 0} &= \frac{g}{v_t^2}\left(v_t^2 - 0\right) = g \gt 0 \quad &\text{(initial condition $v(0) = 0$)} \\
> -v_t \lt v(t) &\lt v_t \quad &\text{(no crossing of the two constant solutions)} \\
> \frac{dv}{dt} &= \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \gt 0 \quad &\text{(positive right-hand side inside that interval)} \\
> 0 &\lt v(t) \lt v_t \quad \text{for } t \gt 0 \quad &\text{(the speed grows from zero)}
> \end{aligned}$$
>
> $$\boxed{0 \lt v(t) \lt v_t \quad \text{for every } t \gt 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for $v$ and $v_t$; $[\mathrm{L\,T^{-2}}]$ for the initial acceleration
> **Meaning:** the ball always falls, so the drag always points up as written, and the ratio of $v$ to $v_t$ stays inside the interval where the inverse hyperbolic tangent is defined.

### Answers and Checks

#### Terminal speed and velocity as a function of time

> [!derivation] Check of the first given antiderivative
> **Law:** derivative of the inverse hyperbolic tangent and chain rule
> **Source:** Problems.pdf, p. 9
>
> $$\begin{aligned}
> \frac{d}{dw}\operatorname{atanh}w &= \frac{1}{1 - w^2} \quad &\text{(derivative of the inverse of $\tanh$, for $|w| \lt 1$)} \\
> \frac{d}{dx}\left[\frac{1}{x_0}\operatorname{atanh}\frac{x}{x_0}\right] &= \frac{1}{x_0}\cdot\frac{1}{1 - x^2/x_0^2}\cdot\frac{1}{x_0} \quad &\text{(chain rule with $w = x/x_0$, $dw/dx = 1/x_0$)} \\
> &= \frac{1}{x_0^2 - x^2} \quad &\text{(numerator and denominator multiplied by $x_0^2$)}
> \end{aligned}$$
>
> $$\boxed{\int\frac{dx}{x_0^2 - x^2} = \frac{1}{x_0}\operatorname{atanh}\frac{x}{x_0} + C, \qquad |x| \lt x_0}$$
>
> **Units:** both sides have the dimension of the inverse of $x$; $x/x_0$ and $w$ are dimensionless
> **Meaning:** the antiderivative of the statement is correct on the interval where the velocity lives.

> [!derivation] Integration of the velocity
> **Law:** separation of variables and Barrow's rule
> **Source:** Problems.pdf, p. 9; Notes.pdf, Eq. 4.6
>
> $$\begin{aligned}
> \frac{dv}{v_t^2 - v^2} &= \frac{g}{v_t^2}\,dt \quad &\text{(separation of variables; $v_t^2 - v^2 \gt 0$ by the sign box)} \\
> \int_0^{v}\frac{dv'}{v_t^2 - v'^2} &= \frac{g}{v_t^2}\int_0^{t}dt' \quad &\text{(from $t' = 0$, $v' = 0$ to the current state)} \\
> \left[\frac{1}{v_t}\operatorname{atanh}\frac{v'}{v_t}\right]_0^{v} &= \frac{g}{v_t^2}\Big[t'\Big]_0^{t} \quad &\text{(antiderivatives: given integral with $x_0 = v_t$)} \\
> \frac{1}{v_t}\operatorname{atanh}\frac{v}{v_t} - \frac{1}{v_t}\operatorname{atanh}0 &= \frac{g}{v_t^2}\left(t - 0\right) \quad &\text{(Barrow's rule: upper limit minus lower limit)} \\
> \operatorname{atanh}\frac{v}{v_t} &= \frac{g\,t}{v_t} \quad &\text{($\operatorname{atanh}0 = 0$; multiplication by $v_t$)} \\
> v &= v_t\tanh\frac{g\,t}{v_t} \quad &\text{($\tanh$ applied to both sides)}
> \end{aligned}$$
>
> $$\boxed{v(t) = v_t\tanh\left(\frac{g}{v_t}\,t\right)}$$
>
> **Units:** $\left[\frac{g\,t}{v_t}\right] = \frac{[\mathrm{L\,T^{-2}}][\mathrm{T}]}{[\mathrm{L\,T^{-1}}]} = [1]$; $[v] = [v_t] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the velocity starts at zero and tends to the terminal speed without reaching it; the time scale of the approach is $v_t/g$.

> [!derivation] Check: the velocity law satisfies the equation of motion
> **Law:** time derivative with the chain rule
> **Source:** Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> u &= \frac{g\,t}{v_t}, \qquad \frac{du}{dt} = \frac{g}{v_t} \quad &\text{(argument and its rate)} \\
> \frac{dv}{dt} &= v_t\,\frac{1}{\cosh^2 u}\,\frac{du}{dt} = \frac{g}{\cosh^2 u} \quad &\text{(chain rule; the derivative of $\tanh$ is $1/\cosh^2$)} \\
> &= g\left(1 - \tanh^2 u\right) = \frac{g}{v_t^2}\left(v_t^2 - v^2\right) \quad &\text{(identity $1/\cosh^2 = 1 - \tanh^2$; $v = v_t\tanh u$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^P = \frac{g}{\cosh^2(g t/v_t)}\,\mathbf i = g\left(1 - \frac{v^2}{v_t^2}\right)\mathbf i}$$
>
> **Units:** $u$ dimensionless, its rate $[\mathrm{T^{-1}}]$; the acceleration $[\mathrm{L\,T^{-2}}]$
> **Meaning:** the second form is the equation of motion itself; the acceleration starts at $g$ and decays to zero.

#### Position as a function of time

> [!derivation] Check of the second given antiderivative
> **Law:** derivative of a logarithm and chain rule
> **Source:** Problems.pdf, p. 9
>
> $$\begin{aligned}
> \frac{d}{du}\ln\cosh u &= \frac{1}{\cosh u}\,\frac{d}{du}\cosh u \quad &\text{(chain rule; $\cosh u \gt 0$)} \\
> &= \frac{\sinh u}{\cosh u} = \tanh u \quad &\text{(the derivative of $\cosh$ is $\sinh$)}
> \end{aligned}$$
>
> $$\boxed{\int\tanh u\,du = \ln\cosh u + C}$$
>
> **Units:** $u$, $\tanh u$ and $\ln\cosh u$ are dimensionless
> **Meaning:** the antiderivative of the statement is correct for every real argument.

> [!derivation] Integration of the position
> **Law:** definition of velocity; change of variable and Barrow's rule
> **Source:** Problems.pdf, p. 9; Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> s(t) - s(0) &= \int_0^{t} v_t\tanh\frac{g\,t'}{v_t}\,dt' \quad &\text{(the velocity is the rate of the position)} \\
> u &= \frac{g\,t'}{v_t}, \quad du = \frac{g}{v_t}\,dt', \quad dt' = \frac{v_t}{g}\,du \quad &\text{(change of variable and its differential)} \\
> t' &= 0 \Rightarrow u = 0; \qquad t' = t \Rightarrow u = \frac{g\,t}{v_t} \quad &\text{(new limits)} \\
> s(t) &= v_t\,\frac{v_t}{g}\int_0^{g t/v_t}\tanh u\,du \quad &\text{($s(0) = 0$; substitution)} \\
> &= \frac{v_t^2}{g}\Big[\ln\cosh u\Big]_0^{g t/v_t} \quad &\text{(second given antiderivative)} \\
> &= \frac{v_t^2}{g}\left[\ln\cosh\frac{g\,t}{v_t} - \ln\cosh 0\right] \quad &\text{(Barrow's rule)} \\
> &= \frac{v_t^2}{g}\ln\cosh\frac{g\,t}{v_t} \quad &\text{($\cosh 0 = 1$, $\ln 1 = 0$)}
> \end{aligned}$$
>
> $$\boxed{s(t) = \frac{v_t^2}{g}\ln\left[\cosh\left(\frac{g}{v_t}\,t\right)\right], \qquad \mathbf r_0^P = s(t)\,\mathbf i}$$
>
> **Units:** $\left[\frac{v_t^2}{g}\right] = \frac{[\mathrm{L^2\,T^{-2}}]}{[\mathrm{L\,T^{-2}}]} = [\mathrm{L}]$, times a dimensionless logarithm; $u$ dimensionless
> **Meaning:** the distance fallen grows first as in free fall and then linearly at the terminal speed; the length scale is $v_t^2/g$.

![[attachments/EM-SOL/p16-time-laws.svg]]

> [!derivation] Limiting cases: early and late times
> **Law:** Taylor expansions about zero; asymptotic behaviour for a large argument
> **Source:** Notes.pdf, Eq. 4.5
>
> $$\begin{aligned}
> \tanh u &= u + O(u^3), \qquad v \approx v_t\,\frac{g t}{v_t} = g t \quad &\text{(first term of the series, $u \ll 1$)} \\
> \ln\cosh u &= \ln\left(1 + \tfrac{u^2}{2} + O(u^4)\right) = \tfrac{u^2}{2} + O(u^4), \qquad s \approx \frac{v_t^2}{g}\,\frac{g^2 t^2}{2 v_t^2} = \tfrac12 g t^2 \quad &\text{(series of $\cosh$, then $\ln(1 + \epsilon) \approx \epsilon$)} \\
> \tanh u &\to 1, \qquad v \to v_t \quad &\text{($u \to \infty$)} \\
> \cosh u &= \tfrac12\left(e^{u} + e^{-u}\right) \approx \tfrac12 e^{u}, \qquad \ln\cosh u \approx u - \ln 2 \quad &\text{($e^{-u}$ negligible; logarithm of a product)} \\
> s &\approx \frac{v_t^2}{g}\left(\frac{g t}{v_t} - \ln 2\right) = v_t\,t - \frac{v_t^2}{g}\ln 2 \quad &\text{(substitution)}
> \end{aligned}$$
>
> $$\boxed{t \ll \frac{v_t}{g}:\ v \approx g t,\ s \approx \tfrac12 g t^2; \qquad t \gg \frac{v_t}{g}:\ v \to v_t,\ s \approx v_t t - \frac{v_t^2}{g}\ln 2}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for the velocities, $[\mathrm{L}]$ for the distances; $u$ and $\ln 2$ dimensionless
> **Meaning:** at first the drag is negligible and the ball falls freely; at late times it falls uniformly at the terminal speed, a constant distance behind a ball that had fallen at that speed from the start.

> [!derivation] Independent check: speed as a function of the distance fallen
> **Law:** chain rule to change the independent variable from time to position; separation of variables and Barrow's rule
> **Source:** Notes.pdf, Eq. 4.22; Notes.pdf, Eq. 4.23
>
> $$\begin{aligned}
> \frac{dv}{dt} &= \frac{dv}{ds}\,\frac{ds}{dt} = v\,\frac{dv}{ds} = \frac12\,\frac{d(v^2)}{ds} \quad &\text{(chain rule twice)} \\
> \frac{d(v^2)}{ds} &= \frac{2g}{v_t^2}\left(v_t^2 - v^2\right) \quad &\text{(equation of motion with the terminal speed)} \\
> w &= v^2 \quad &\text{(definition of the new unknown)} \\
> \frac{dw}{v_t^2 - w} &= \frac{2g}{v_t^2}\,ds \quad &\text{(separation of variables; $v_t^2 - w \gt 0$ by the sign box)} \\
> \int_0^{v^2}\frac{dw}{v_t^2 - w} &= \frac{2g}{v_t^2}\int_0^{s}ds' \quad &\text{(integrals from $s' = 0$, $w = 0$ to the current state)} \\
> q &= v_t^2 - w, \ dq = -dw; \quad -\Big[\ln q\Big]_{v_t^2}^{v_t^2 - v^2} = \frac{2g\,s}{v_t^2} \quad &\text{(change of variable with its limits; Barrow's rule on the right)} \\
> \ln\frac{v_t^2}{v_t^2 - v^2} &= \frac{2g\,s}{v_t^2} \quad &\text{(Barrow's rule on the left)} \\
> v_t^2 - v^2 = v_t^2\,e^{-2 g s/v_t^2} \ \Rightarrow\ v^2 &= v_t^2\left(1 - e^{-2 g s/v_t^2}\right) \quad &\text{(exponential of both sides; solved for $v^2$)} \\
> \frac{v_t^2}{v_t^2 - v^2} &= \frac{1}{1 - \tanh^2 u} = \cosh^2 u \quad &\text{(time laws, $u = g t/v_t$)} \\
> \ln\cosh^2 u &= 2\ln\cosh u = \frac{2g}{v_t^2}\,s(t) \quad &\text{(the boxed position law: both sides agree)}
> \end{aligned}$$
>
> $$\boxed{v^2 = v_t^2\left(1 - e^{-2 g s/v_t^2}\right)\ \text{holds identically for the two time laws}}$$
>
> **Units:** $\left[\frac{g\,s}{v_t^2}\right] = \frac{[\mathrm{L\,T^{-2}}][\mathrm{L}]}{[\mathrm{L^2\,T^{-2}}]} = [1]$; $w$ and $q$ in $[\mathrm{L^2\,T^{-2}}]$
> **Meaning:** a route that never uses the time gives the same relation between speed and distance as the two time laws, so they are consistent; the work of the drag is what keeps the kinetic energy below the work of the weight.

| Part of the statement | Answer |
| :--- | :--- |
| Terminal speed | $v_t = \sqrt{2mg/(\rho S C_D)}$ |
| Velocity (downward) | $v(t) = v_t\tanh(g t/v_t)$ |
| Position (distance fallen from rest at $O$) | $s(t) = (v_t^2/g)\ln\cosh(g t/v_t)$ |

**Check against the official key:** Problems.pdf, p. 73, item 16, prints the same terminal velocity and, with the release from rest at the origin and the axis positive downward, the same velocity and position laws as the table above: **match**. A Runge-Kutta integration of the equation of motion with unit gravity and unit terminal speed gives, at the time 1 s, a speed of 0.761594 m/s and a distance of 0.433781 m, the values of the hyperbolic tangent and of the logarithm of the hyperbolic cosine of 1.

---

## Problem 17: Linear Central Force

### Reference Frames, Bases and Coordinates

The heavy particle $M$ moves freely in space under two forces: the attraction towards the fixed point $O$, proportional to its mass and to the distance with coefficient $k^2$, and its weight. The statement places the origin at the centre of attraction and the axis $Oz$ vertical, and asks for the shape of the path and for the velocity as a function of time (Problems.pdf, p. 9; parts on p. 10).

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$, origin at the centre of attraction (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$, $\mathbf k$ vertical **upward**, $\mathbf i$ and $\mathbf j$ horizontal, right-handed |
| Auxiliary basis (part a) | $\mathcal B_1 = \{\mathbf e_1, \mathbf j, \mathbf e_3\}$, the basis of the plane of the path, obtained from $\mathcal B_0$ by a rotation about $\mathbf j$ (defined in the next section) |
| Coordinates | $x(t)$, $y(t)$, $z(t)$, Cartesian coordinates of $M$ in $S_0$ |
| Data | $m$ [kg] mass; $k$ [s$^{-1}$] so that $k^2$ is in s$^{-2}$; $g$ [m s$^{-2}$] gravity |
| Applied forces | attraction $-m k^2\,\mathbf r_0^M$ (proportional to the mass and to the distance $OM$, towards $O$); weight $-m g\,\mathbf k$ |
| Initial conditions | position $(\sqrt3\,g/k^2,\ 0,\ 0)$; velocity $(0,\ 2g/k,\ 0)$ |
| Hypotheses | "vertically oriented" is read as $\mathbf k$ pointing up, so the weight is $-mg\,\mathbf k$ (the reading of the official key, whose orbit lies below $O$) |
| Constraints | none: the particle is free |
| Degrees of freedom | 3, the three Cartesian coordinates |

### Change of Basis and Position Vector

The basis $\mathcal B_0$ needs only the identity check. The auxiliary basis $\mathcal B_1$ is the one in which part (a) reads most simply: its first axis $\mathbf e_1$ lies in the vertical plane $Oxz$, raised by the angle of 30 degrees above $\mathbf i$, and its second axis is $\mathbf j$. The answer of part (a) shows that the path lies in the plane spanned by $\mathbf e_1$ and $\mathbf j$; the basis is built here so that every basis of the problem is defined before the kinematics.

![[attachments/EM-SOL/p17-rotation-j.svg]]

> [!derivation] The fixed basis and its change of basis matrix
> **Law:** change of basis matrix between two bases; orthonormality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> $$\begin{aligned}
> \mathbf i &= 1\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k, \quad \mathbf j = 0\,\mathbf i + 1\,\mathbf j + 0\,\mathbf k, \quad \mathbf k = 0\,\mathbf i + 0\,\mathbf j + 1\,\mathbf k \quad &\text{(columns: components of $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_0] = 1, \quad [{}_0R_0][{}_0R_0]^T = I}$$
>
> **Units:** every entry is a direction cosine: $[1]$
> **Meaning:** $\mathcal B_0$ is orthonormal and right-handed, and its unit vectors are constant in $S_0$.

> [!derivation] Basis of the plane of the path: rotation about j
> **Law:** elementary rotation about the second axis; change of basis matrix and its checks
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.15; Notes.pdf, Eq. 1.19
>
> View of the plane $Oxz$ with $\mathbf i$ to the right and $\mathbf k$ up. Since $\mathbf k\times\mathbf i = \mathbf j$, the axis $\mathbf j$ points into the paper (⊗) in this view, and a positive rotation about $\mathbf j$ (right-hand rule, thumb into the paper) is clockwise as seen. The vector $\mathbf e_1$ is $\mathbf i$ turned counterclockwise by 30 degrees, so it is the rotation of Notes.pdf, Eq. 1.19 with the negative angle $\theta_y = -\pi/6$. Its right triangle has hypotenuse 1, adjacent leg $\cos(\pi/6)$ along $\mathbf i$ and opposite leg $\sin(\pi/6)$ along $\mathbf k$. The vector $\mathbf e_3$ is $\mathbf k$ turned by the same angle: its adjacent leg $\cos(\pi/6)$ lies along $\mathbf k$ and its opposite leg $\sin(\pi/6)$ along minus $\mathbf i$, because turning counterclockwise from the upward vertical leans it to the left; that is the origin of the minus sign.
>
> $$\begin{aligned}
> \mathbf e_1 &= \cos\tfrac{\pi}{6}\,\mathbf i + \sin\tfrac{\pi}{6}\,\mathbf k = \tfrac{\sqrt3}{2}\,\mathbf i + \tfrac12\,\mathbf k \quad &\text{(adjacent leg on $\mathbf i$, opposite leg on $\mathbf k$)} \\
> \mathbf e_2 &= \mathbf j \quad &\text{(axis of the rotation, unchanged)} \\
> \mathbf e_3 &= -\sin\tfrac{\pi}{6}\,\mathbf i + \cos\tfrac{\pi}{6}\,\mathbf k = -\tfrac12\,\mathbf i + \tfrac{\sqrt3}{2}\,\mathbf k \quad &\text{(adjacent leg on $\mathbf k$, opposite leg on $-\mathbf i$)} \\
> \mathbf e_1\times\mathbf j &= \tfrac{\sqrt3}{2}\,\mathbf i\times\mathbf j + \tfrac12\,\mathbf k\times\mathbf j = \tfrac{\sqrt3}{2}\,\mathbf k - \tfrac12\,\mathbf i = \mathbf e_3 \quad &\text{(right-handed: $\mathbf i\times\mathbf j = \mathbf k$, $\mathbf k\times\mathbf j = -\mathbf i$)} \\
> \det[{}_0R_1] &= \tfrac{\sqrt3}{2}\left(1\cdot\tfrac{\sqrt3}{2} - 0\cdot 0\right) - 0 + \left(-\tfrac12\right)\left(0\cdot 0 - 1\cdot\tfrac12\right) \quad &\text{(expansion along the first row)} \\
> &= \tfrac34 + \tfrac14 = 1 \quad &\text{(sum of the two minors)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{11} &= \tfrac34 + 0 + \tfrac14 = 1, \quad \left([{}_0R_1][{}_0R_1]^T\right)_{33} = \tfrac14 + 0 + \tfrac34 = 1 \quad &\text{(rows 1 and 3 times themselves)} \\
> \left([{}_0R_1][{}_0R_1]^T\right)_{13} &= \tfrac{\sqrt3}{2}\cdot\tfrac12 + 0 - \tfrac12\cdot\tfrac{\sqrt3}{2} = 0 \quad &\text{(row 1 times row 3; row 2 is the unit row of $\mathbf j$)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \tfrac{\sqrt3}{2} & 0 & -\tfrac12 \cr 0 & 1 & 0 \cr \tfrac12 & 0 & \tfrac{\sqrt3}{2} \end{pmatrix}, \quad \det[{}_0R_1] = 1, \quad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** every entry is a direction cosine: $[1]$; the angle $\pi/6$ is in radians, dimensionless
> **Meaning:** the columns are $\mathbf e_1$, $\mathbf j$, $\mathbf e_3$ written in $\mathcal B_0$; $\mathcal B_1$ is a proper rotation of $\mathcal B_0$, and $\mathbf e_3$ will be the normal of the plane of the path.

> [!derivation] Position vector of the particle
> **Law:** position vector of a point in Cartesian components
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5
>
> $$\begin{aligned}
> \mathbf r_0^M &= \overrightarrow{OM} \quad &\text{(definition of the position vector)} \\
> &= x\,\mathbf i + y\,\mathbf j + z\,\mathbf k \quad &\text{(Cartesian components in $\mathcal B_0$)} \\
> \mathbf r_0^M(0) &= \frac{\sqrt3\,g}{k^2}\,\mathbf i \quad &\text{(initial position of the statement)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^M = x\,\mathbf i + y\,\mathbf j + z\,\mathbf k, \qquad \mathbf r_0^M(0) = \frac{\sqrt3\,g}{k^2}\,\mathbf i}$$
>
> **Units:** $[\mathrm{L}]$; $[g/k^2] = [\mathrm{L\,T^{-2}}]/[\mathrm{T^{-2}}] = [\mathrm{L}]$
> **Meaning:** the particle starts on the horizontal axis $Ox$, at the distance $\sqrt3\,g/k^2$ from the centre of attraction.

### Kinematics

> [!derivation] Velocity and acceleration of the particle
> **Law:** velocity and acceleration as time derivatives of the position vector in $S_0$
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \frac{d\mathbf i}{dt} &= \frac{d\mathbf j}{dt} = \frac{d\mathbf k}{dt} = \mathbf 0\times(\cdot) = \mathbf 0 \quad &\text{($\mathcal B_0$ does not rotate in $S_0$)} \\
> \mathbf v_0^M &= \frac{d}{dt}\left(x\,\mathbf i + y\,\mathbf j + z\,\mathbf k\right) = \dot x\,\mathbf i + \dot y\,\mathbf j + \dot z\,\mathbf k \quad &\text{(product rule on each term; constant unit vectors)} \\
> \mathbf a_0^M &= \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k \quad &\text{(the same rule once more)} \\
> \mathbf v_0^M(0) &= \frac{2g}{k}\,\mathbf j \quad &\text{(initial velocity of the statement)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^M = \dot x\,\mathbf i + \dot y\,\mathbf j + \dot z\,\mathbf k, \qquad \mathbf a_0^M = \ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k}$$
>
> **Units:** $[\mathrm{T^{-1}}]$ for the derivatives of the unit vectors (zero); $[\mathrm{L\,T^{-1}}]$, $[\mathrm{L\,T^{-2}}]$; $[g/k] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the initial velocity is horizontal and perpendicular to the initial position vector.

### Forces and Equations of Motion

The free-body diagram shows the attraction towards $O$ and the weight. The particle is free, so no reaction acts, and $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p17-fbd.svg]]

> [!derivation] Newton's second law projected on the fixed basis
> **Law:** Newton's second law in an inertial frame; projection on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5; Problems.pdf, p. 9
>
> $$\begin{aligned}
> m\,\mathbf a_0^M &= \mathbf F_c + \mathbf F_g + \mathbf R \quad &\text{(second law in $S_0$)} \\
> \mathbf F_c &= -m k^2\,\mathbf r_0^M, \quad \mathbf F_g = -m g\,\mathbf k, \quad \mathbf R = \mathbf 0 \quad &\text{(attraction towards $O$; weight; free particle)} \\
> m\left(\ddot x\,\mathbf i + \ddot y\,\mathbf j + \ddot z\,\mathbf k\right) &= -m k^2\left(x\,\mathbf i + y\,\mathbf j + z\,\mathbf k\right) - m g\,\mathbf k \quad &\text{(kinematics and forces in $\mathcal B_0$)} \\
> \mathbf i:\ \ddot x + k^2 x &= 0, \quad \mathbf j:\ \ddot y + k^2 y = 0, \quad \mathbf k:\ \ddot z + k^2 z = -g \quad &\text{(dot products with $\mathbf i$, $\mathbf j$, $\mathbf k$; division by $m$)}
> \end{aligned}$$
>
> $$\boxed{\ddot x + k^2 x = 0, \qquad \ddot y + k^2 y = 0, \qquad \ddot z + k^2 z = -g}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ in every term: $[k^2][\mathrm{L}] = [\mathrm{T^{-2}}][\mathrm{L}]$; the forces $[\mathrm{M}][\mathrm{T^{-2}}][\mathrm{L}] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** three uncoupled harmonic oscillators of angular frequency $k$ (Notes.pdf, Eq. 5.6 with $\omega_0$ equal to $k$); gravity only adds a constant force to the vertical one.

> [!derivation] Horizontal coordinates: free oscillators
> **Law:** characteristic equation of a linear equation with constant coefficients; general solution of the undamped oscillator and its constants
> **Source:** Notes.pdf, Eq. 5.7; Notes.pdf, Eq. 5.8; Notes.pdf, Eq. 5.9; [Lecture 6, Slide 6]
>
> $$\begin{aligned}
> p^2 + k^2 &= 0 \Rightarrow p = \pm \mathrm{i}\, k \quad &\text{(trial $e^{pt}$ in $\ddot x + k^2 x = 0$)} \\
> x &= C_1\cos kt + C_2\sin kt \quad &\text{(real form of the general solution)} \\
> \dot x &= -k C_1\sin kt + k C_2\cos kt \quad &\text{(chain rule: $\tfrac{d}{dt}\cos kt = -k\sin kt$, $\tfrac{d}{dt}\sin kt = k\cos kt$)} \\
> x(0) &= C_1 = \frac{\sqrt3\,g}{k^2}, \qquad \dot x(0) = k C_2 = 0 \quad &\text{(initial data of $x$)} \\
> y(0) &= C_1' = 0, \qquad \dot y(0) = k C_2' = \frac{2g}{k} \Rightarrow C_2' = \frac{2g}{k^2} \quad &\text{(the same solution for $y$, constants $C_1'$, $C_2'$)}
> \end{aligned}$$
>
> $$\boxed{x(t) = \frac{\sqrt3\,g}{k^2}\cos kt, \qquad y(t) = \frac{2g}{k^2}\sin kt}$$
>
> **Units:** $[\mathrm{L}]$; $[kt] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$; $p$ in $[\mathrm{T^{-1}}]$
> **Meaning:** seen from above, the particle describes an ellipse of semi-axes $\sqrt3\,g/k^2$ and $2g/k^2$ centred on the vertical through $O$.

> [!derivation] Vertical coordinate: oscillator under a constant force
> **Law:** general solution of the complete equation as homogeneous plus particular solution
> **Source:** Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3]
>
> $$\begin{aligned}
> z_p &= -\frac{g}{k^2} \quad &\text{(constant particular solution: $0 + k^2 z_p = -g$)} \\
> z &= -\frac{g}{k^2} + C_1''\cos kt + C_2''\sin kt \quad &\text{(particular plus homogeneous solution)} \\
> z(0) &= -\frac{g}{k^2} + C_1'' = 0 \Rightarrow C_1'' = \frac{g}{k^2} \quad &\text{(initial height)} \\
> \dot z(0) &= k C_2'' = 0 \Rightarrow C_2'' = 0 \quad &\text{(initial vertical rate, chain rule as above)}
> \end{aligned}$$
>
> $$\boxed{z(t) = \frac{g}{k^2}\left(\cos kt - 1\right)}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the weight shifts the centre of the vertical oscillation to the equilibrium height $-g/k^2$, where the attraction balances the weight; the particle oscillates between the height of $O$ and twice that depth.

### Answers and Checks

#### (a) Shape of the path

> [!derivation] The path is a great circle of a sphere
> **Law:** a linear relation among the coordinates is a plane; a constant distance to a point is a sphere; their intersection is a circle
> **Source:** Notes.pdf, Eq. 2.5; Problems.pdf, p. 73
>
> $$\begin{aligned}
> \cos kt &= \frac{k^2 x}{\sqrt3\,g} \quad &\text{(from the law of $x$)} \\
> z &= \frac{g}{k^2}\cdot\frac{k^2 x}{\sqrt3\,g} - \frac{g}{k^2} = \frac{x}{\sqrt3} - \frac{g}{k^2} \quad &\text{(substitution in the law of $z$)} \\
> x - \sqrt3\,z &= \frac{\sqrt3\,g}{k^2} \quad &\text{(multiplication by $\sqrt3$; the plane)} \\
> x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2 &= \frac{g^2}{k^4}\left(3\cos^2 kt + 4\sin^2 kt + \cos^2 kt\right) \quad &\text{(squares of the three laws, with $z + g/k^2 = (g/k^2)\cos kt$)} \\
> &= \frac{4g^2}{k^4}\left(\cos^2 kt + \sin^2 kt\right) = \frac{4g^2}{k^4} \quad &\text{(common factor 4; Pythagorean identity)} \\
> 0 - \sqrt3\left(-\frac{g}{k^2}\right) &= \frac{\sqrt3\,g}{k^2} \quad &\text{(the centre $C = (0, 0, -g/k^2)$ satisfies the plane)}
> \end{aligned}$$
>
> $$\boxed{\text{plane } x - \sqrt3\,z = \frac{\sqrt3\,g}{k^2}; \quad \text{sphere } x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2 = \frac{4g^2}{k^4}; \quad \text{path: circle of centre } C,\ R = \frac{2g}{k^2}}$$
>
> **Units:** every term of the plane in $[\mathrm{L}]$; every term of the sphere in $[\mathrm{L^2}]$; $[R] = [\mathrm{L}]$
> **Meaning:** the plane passes through the centre of the sphere, so the path is a great circle, of radius $2g/k^2$, centred at the equilibrium point $C$ below $O$.

![[attachments/EM-SOL/p17-path-plane.svg]]

> [!derivation] The motion written in the basis of the plane
> **Law:** change of basis of the position vector relative to the centre $C$
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 2.2
>
> $$\begin{aligned}
> \overrightarrow{CM} &= \mathbf r_0^M - \overrightarrow{OC} = x\,\mathbf i + y\,\mathbf j + \left(z + \frac{g}{k^2}\right)\mathbf k \quad &\text{($\overrightarrow{OC} = -(g/k^2)\,\mathbf k$)} \\
> &= \frac{g}{k^2}\left(\sqrt3\cos kt\,\mathbf i + \cos kt\,\mathbf k\right) + \frac{2g}{k^2}\sin kt\,\mathbf j \quad &\text{(the three laws)} \\
> &= \frac{2g}{k^2}\cos kt\left(\tfrac{\sqrt3}{2}\,\mathbf i + \tfrac12\,\mathbf k\right) + \frac{2g}{k^2}\sin kt\,\mathbf j \quad &\text{(factor 2 taken out of the first bracket)} \\
> &= \frac{2g}{k^2}\left(\cos kt\,\mathbf e_1 + \sin kt\,\mathbf j\right) \quad &\text{(first column of $[{}_0R_1]$)} \\
> \overrightarrow{CM}\cdot\mathbf e_3 &= \frac{2g}{k^2}\cos kt\left(-\tfrac{\sqrt3}{4} + \tfrac{\sqrt3}{4}\right) = 0 \quad &\text{(the path has no component along the normal $\mathbf e_3$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^M = -\frac{g}{k^2}\,\mathbf k + \frac{2g}{k^2}\left(\cos kt\,\mathbf e_1 + \sin kt\,\mathbf j\right)}$$
>
> **Units:** $[\mathrm{L}]$; the trigonometric arguments are dimensionless
> **Meaning:** the particle moves round the circle of centre $C$ and radius $2g/k^2$ in the plane spanned by $\mathbf e_1$ and $\mathbf j$, which is tilted by 30 degrees from the horizontal about $\mathbf j$; it starts at the end of $\mathbf e_1$ and sweeps the angle $kt$ uniformly, once every period $2\pi/k$.

#### (b) Velocity as a function of time

> [!derivation] Velocity and speed
> **Law:** time derivative of each coordinate with the chain rule; modulus from the components
> **Source:** Notes.pdf, Eq. 2.6
>
> $$\begin{aligned}
> \dot x &= \frac{\sqrt3\,g}{k^2}\left(-k\sin kt\right), \quad \dot y = \frac{2g}{k^2}\left(k\cos kt\right), \quad \dot z = \frac{g}{k^2}\left(-k\sin kt\right) \quad &\text{(chain rule on each law)} \\
> \mathbf v_0^M &= -\frac{\sqrt3\,g}{k}\sin kt\,\mathbf i + \frac{2g}{k}\cos kt\,\mathbf j - \frac{g}{k}\sin kt\,\mathbf k \quad &\text{(components assembled)} \\
> &= \frac{2g}{k}\left(-\sin kt\,\mathbf e_1 + \cos kt\,\mathbf j\right) \quad &\text{(first and third components grouped as $-\sin kt$ times $2\mathbf e_1$)} \\
> |\mathbf v_0^M|^2 &= \frac{g^2}{k^2}\left(3\sin^2 kt + 4\cos^2 kt + \sin^2 kt\right) = \frac{4g^2}{k^2} \quad &\text{(sum of squares; Pythagorean identity)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^M(t) = -\frac{\sqrt3\,g}{k}\sin kt\,\mathbf i + \frac{2g}{k}\cos kt\,\mathbf j - \frac{g}{k}\sin kt\,\mathbf k, \qquad |\mathbf v_0^M| = \frac{2g}{k}}$$
>
> **Units:** $[g/k] = [\mathrm{L\,T^{-2}}]/[\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the speed is constant: the motion is uniform circular motion; at the start the velocity equals the data $(2g/k)\,\mathbf j$.

> [!derivation] Consistency check: energy integral derived from the equation of motion
> **Law:** the equation of motion multiplied by the velocity is an exact time derivative
> **Source:** Notes.pdf, Eq. 4.29; Notes.pdf, Eq. 4.31
>
> $$\begin{aligned}
> \mathbf v_0^M\cdot\left(m\,\mathbf a_0^M + m k^2\,\mathbf r_0^M + m g\,\mathbf k\right) &= 0 \quad &\text{(equation of motion, dot product with the velocity)} \\
> m\,\mathbf v_0^M\cdot\mathbf a_0^M &= \frac{d}{dt}\left(\tfrac12 m\,\mathbf v_0^M\cdot\mathbf v_0^M\right) \quad &\text{(product rule on the dot product)} \\
> m k^2\,\mathbf r_0^M\cdot\mathbf v_0^M &= \frac{d}{dt}\left(\tfrac12 m k^2\,\mathbf r_0^M\cdot\mathbf r_0^M\right), \quad m g\,\mathbf k\cdot\mathbf v_0^M = \frac{d}{dt}\left(m g z\right) \quad &\text{(product rule; chain rule with $\dot z = \mathbf k\cdot\mathbf v_0^M$)} \\
> \tfrac12 m |\mathbf v_0^M|^2 + \tfrac12 m k^2\left(x^2 + y^2 + z^2\right) + m g z &= E_0 \quad &\text{(the sum of the three derivatives vanishes)} \\
> \tfrac12 m k^2\left[x^2 + y^2 + \left(z + \frac{g}{k^2}\right)^2\right] - \frac{m g^2}{2k^2} &= \tfrac12 m k^2\left(x^2 + y^2 + z^2\right) + m g z \quad &\text{(square completed in $z$)} \\
> \tfrac12 m |\mathbf v_0^M|^2 &= E_0 - \tfrac12 m k^2\,\frac{4g^2}{k^4} + \frac{m g^2}{2k^2} \quad &\text{(on the sphere of part (a))}
> \end{aligned}$$
>
> $$\boxed{|\mathbf v_0^M| = \text{const} = |\mathbf v_0^M(0)| = \frac{2g}{k}}$$
>
> **Units:** every energy term $[\mathrm{M\,L^2\,T^{-2}}]$; the speed $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the force is conservative; on a sphere centred at the equilibrium point the potential energy is constant, so the kinetic energy and the speed are constant, as found by differentiation.

> [!derivation] Consistency of the circular motion
> **Law:** acceleration of a uniform circular motion compared with the force per unit mass
> **Source:** Notes.pdf, Eq. 2.17; Notes.pdf, Eq. 4.4
>
> $$\begin{aligned}
> \mathbf a_0^M &= -k^2\,\mathbf r_0^M - g\,\mathbf k = -k^2\left(\mathbf r_0^M + \frac{g}{k^2}\,\mathbf k\right) = -k^2\,\overrightarrow{CM} \quad &\text{(equation of motion; $\overrightarrow{OC} = -(g/k^2)\,\mathbf k$)} \\
> |\mathbf a_0^M| &= k^2 R = k^2\,\frac{2g}{k^2} = 2g \quad &\text{(modulus on the circle)} \\
> \frac{|\mathbf v_0^M|^2}{R} &= \frac{4g^2/k^2}{2g/k^2} = 2g \quad &\text{(normal acceleration $\dot s^2/\rho$ of the intrinsic decomposition with $\rho = R$ and $\ddot s = 0$)}
> \end{aligned}$$
>
> $$\boxed{|\mathbf a_0^M| = \frac{|\mathbf v_0^M|^2}{R} = 2g, \qquad \text{angular rate } \frac{|\mathbf v_0^M|}{R} = k}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ for the accelerations; $[\mathrm{T^{-1}}]$ for the angular rate
> **Meaning:** the resultant of attraction and weight points from $M$ to the centre $C$ and has exactly the centripetal value of the circle; the particle turns at the angular rate $k$.

> [!derivation] Limiting case: no gravity
> **Law:** behaviour of the laws when the constant force vanishes
> **Source:** Notes.pdf, Eq. 5.7
>
> If gravity is switched off while the initial data keep the same numerical values $X_0$ and $V_0$ (initial distance and initial speed), the vertical oscillation disappears and the horizontal laws remain.
>
> $$\begin{aligned}
> z_p &= -\frac{g}{k^2} \to 0, \qquad z(t) \to 0 \quad &\text{(the vertical equation becomes homogeneous with zero data)} \\
> x &= X_0\cos kt, \qquad y = \frac{V_0}{k}\sin kt \quad &\text{(horizontal laws unchanged)}
> \end{aligned}$$
>
> $$\boxed{g \to 0:\ \text{a horizontal ellipse centred at } O \text{ with semi-axes } X_0 \text{ and } V_0/k}$$
>
> **Units:** $X_0$ and $V_0/k$ in $[\mathrm{L}]$
> **Meaning:** without weight the linear attraction alone gives the classical centred ellipse; the weight is what moves the centre to $C$ and tilts the plane of the path, which with the given data is a circle.

| Part of the statement | Answer |
| :--- | :--- |
| Motion | $\mathbf r_0^M = \frac{\sqrt3 g}{k^2}\cos kt\,\mathbf i + \frac{2g}{k^2}\sin kt\,\mathbf j + \frac{g}{k^2}(\cos kt - 1)\,\mathbf k$ |
| (a) Shape of the path | great circle of centre $C = (0, 0, -g/k^2)$ and radius $2g/k^2$: intersection of the sphere $x^2 + y^2 + (z + g/k^2)^2 = 4g^2/k^4$ with the plane $x - \sqrt3 z = \sqrt3 g/k^2$ (tilted 30 degrees about $\mathbf j$); uniform motion at the angular rate $k$ |
| (b) Velocity | $\mathbf v_0^M = -\frac{\sqrt3 g}{k}\sin kt\,\mathbf i + \frac{2g}{k}\cos kt\,\mathbf j - \frac{g}{k}\sin kt\,\mathbf k$, constant speed $2g/k$ |

**Check against the official key:** Problems.pdf, p. 73, item 17, prints the same position vector, the same sphere and plane (and notes that other pairs of surfaces describe the same curve) and the same constant speed: **match**. A Runge-Kutta integration of the three equations with unit values of gravity and of the constant, over one period, keeps the distance to the centre equal to 2 m and the speed equal to 2 m/s within the error of the method.

---

## Problem 45: Vibrating Rotor (Unbalanced Turbojet)

### Reference Frames, Bases and Coordinates

The rotor is a rigid disk that turns at the prescribed rate $\omega$ about an axis normal to the plane of the figure. Its geometric centre $C$ is pulled toward the design position $O$ by an elastic force, and its centre of mass $G$ is offset from $C$ by the fixed distance $\ell$. The statement asks for the dynamics of $G$, so $G$ is treated as a point particle of mass $m$ that carries the resultant of the external forces (the particle model of chapter 4 of Notes.pdf; the rotation of the disk is prescribed, so its own dynamics is not needed). The tools are those of chapters 1, 2, 4 and 5 of Notes.pdf and of Lecture 6.

| Symbol | Meaning | Units |
| :--- | :--- | :--- |
| $S_0 = \{O;\ \mathbf i_0, \mathbf j_0, \mathbf k_0\}$ | fixed (inertial) frame; $O$ the design position of $C$; $\mathbf i_0$ the $x$ axis of the figure (right), $\mathbf j_0$ the $y$ axis (up), $\mathbf k_0$ the rotation axis, out of the paper (⊙) | - |
| $S_1 = \{C;\ \mathbf i_1, \mathbf j_1, \mathbf k_0\}$ | frame attached to the disk; $\mathbf i_1$ the unit vector from $C$ to $G$; $\mathbf j_1 = \mathbf k_0 \times \mathbf i_1$ | - |
| $\omega t$ | angle from $\mathbf i_0$ to $\mathbf i_1$, counterclockwise seen with $\mathbf k_0$ ⊙ (figure of the statement) | rad |
| $m$ | mass of the disk | kg |
| $k$ | constant of the elastic restoring force acting on $C$ | N/m |
| $\ell$ | fixed distance from $C$ to $G$ (unbalance) | m |
| $\omega$ | constant angular velocity of the disk | rad/s |
| $\omega_0 = \sqrt{k/m}$ | natural angular frequency of the undamped oscillator (Notes.pdf, Eq. 5.6) | rad/s |
| $(x_0^C, y_0^C)$, $(x_0^G, y_0^G)$ | Cartesian coordinates of $C$ and $G$ in $S_0$ (unknowns) | m |

Hypotheses and degrees of freedom:

- The motion is planar, in the plane $Oxy$; the weight is negligible (statement).
- The elastic force has zero natural length and acts at $C$, directed toward $O$ and proportional to the distance $OC$: the restoring force of Notes.pdf, Eq. 5.1 in two dimensions.
- The motor that keeps the rate $\omega$ constant applies a pure couple; its resultant force is zero, so it does not enter the equation of $G$.
- The disk stays in the plane $Oxy$; whatever holds it there (bearings, guides) can only exert a reaction along $\mathbf k_0$, written as an unknown in Newton's law.
- The orientation of the disk is prescribed (a time-dependent constraint), so the segment $CG$ is known at every instant; the free coordinates are the two coordinates of $C$, or equivalently of $G$: two degrees of freedom.
- The statement assumes that the homogeneous solution dies out in time. This implies a small dissipation that the model does not write down; the answer is the particular (steady) solution.

![[attachments/EM-SOL/p45-disk-plane.svg]]

### Change of Basis and Position Vector

![[attachments/EM-SOL/p45-rotation-view.svg]]

> [!derivation] Disk basis and the change of basis matrix
> **Law:** rotation of a basis about $\mathbf k_0$; definition of the change of basis matrix and its orthogonality
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.20; Notes.pdf, Eq. 1.15; Problems.pdf, p. 31
>
> In the view along $\mathbf k_0$ (out of the paper, ⊙), the unit vector $\mathbf i_1$ is the hypotenuse (length 1) of a right triangle whose leg adjacent to the angle lies along $\mathbf i_0$ and whose opposite leg lies along $\mathbf j_0$. The vector $\mathbf j_1$ is $\mathbf i_1$ turned a right angle counterclockwise about $\mathbf k_0$ (right-hand rule, thumb out of the paper). Turning the triangle of $\mathbf i_1$ by that right angle sends its adjacent leg to the vertical and its opposite leg to the horizontal pointing toward minus $\mathbf i_0$: this is the origin of the minus sign.
>
> $$\begin{aligned}
> \mathbf i_1 &= \cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0 \quad &\text{(adjacent leg $\cos\omega t$ on $\mathbf i_0$, opposite leg $\sin\omega t$ on $\mathbf j_0$)} \\
> \mathbf j_1 &= \mathbf k_0 \times \mathbf i_1 = \cos\omega t\,(\mathbf k_0 \times \mathbf i_0) + \sin\omega t\,(\mathbf k_0 \times \mathbf j_0) \quad &\text{(distributive property of the vector product)} \\
> &= \cos\omega t\,\mathbf j_0 - \sin\omega t\,\mathbf i_0 \quad &\text{(right-handed products: $\mathbf k_0 \times \mathbf i_0 = \mathbf j_0$, $\mathbf k_0 \times \mathbf j_0 = -\mathbf i_0$)} \\
> \det[{}_0R_1] &= 1\cdot\left(\cos\omega t\cos\omega t - (-\sin\omega t)\sin\omega t\right) \quad &\text{(expansion along the third row)} \\
> &= \cos^2\omega t + \sin^2\omega t = 1 \quad &\text{(Pythagorean identity)} \\
> ([{}_0R_1][{}_0R_1]^T)_{11} &= \cos^2\omega t + \sin^2\omega t = 1 \quad &\text{(row 1 times row 1)} \\
> ([{}_0R_1][{}_0R_1]^T)_{12} &= \cos\omega t\sin\omega t - \sin\omega t\cos\omega t = 0 \quad &\text{(row 1 times row 2)} \\
> ([{}_0R_1][{}_0R_1]^T)_{22} &= \sin^2\omega t + \cos^2\omega t = 1 \quad &\text{(row 2 times row 2; third row and column as the identity)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_1] = \begin{pmatrix} \cos\omega t & -\sin\omega t & 0 \cr \sin\omega t & \cos\omega t & 0 \cr 0 & 0 & 1 \end{pmatrix},\qquad \det[{}_0R_1] = 1,\qquad [{}_0R_1][{}_0R_1]^T = I}$$
>
> **Units:** $[1]$ for every entry; $[\omega t] = [\mathrm{T^{-1}}][\mathrm{T}] = [1]$
> **Meaning:** the columns are the disk unit vectors written in the fixed basis; the matrix is the elementary rotation about the $z$ axis of Notes.pdf, Eq. 1.20 with the angle $\omega t$.

> [!derivation] Position vectors of the geometric centre and of the centre of mass
> **Law:** definition of the position vector as a sum of segments
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5; Problems.pdf, p. 31
>
> The segment from $C$ to $G$ is fixed in the disk, of length $\ell$ along $\mathbf i_1$. In the right triangle with hypotenuse $CG$, the leg adjacent to the angle is horizontal and the opposite leg vertical.
>
> $$\begin{aligned}
> \mathbf r_0^C &= \overrightarrow{OC} = x_0^C\,\mathbf i_0 + y_0^C\,\mathbf j_0 \quad &\text{(Cartesian coordinates of $C$)} \\
> \overrightarrow{CG} &= \ell\,\mathbf i_1 = \ell\cos\omega t\,\mathbf i_0 + \ell\sin\omega t\,\mathbf j_0 \quad &\text{(adjacent leg $\ell\cos\omega t$, opposite leg $\ell\sin\omega t$)} \\
> \mathbf r_0^G &= \overrightarrow{OC} + \overrightarrow{CG} \quad &\text{(sum of segments)} \\
> &= \left(x_0^C + \ell\cos\omega t\right)\mathbf i_0 + \left(y_0^C + \ell\sin\omega t\right)\mathbf j_0 \quad &\text{(components added)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^G = \mathbf r_0^C + \ell\,\mathbf i_1,\qquad x_0^G = x_0^C + \ell\cos\omega t,\qquad y_0^G = y_0^C + \ell\sin\omega t}$$
>
> **Units:** $[\mathrm{L}]$ in every term
> **Meaning:** the centre of mass sits at the geometric centre displaced by the unbalance, which turns with the disk.

### Kinematics

> [!derivation] Derivatives of the disk unit vectors
> **Law:** derivative of a unit vector of constant magnitude turning with angular velocity $\boldsymbol\omega$; vector products written out
> **Source:** Notes.pdf, Eq. 1.62; Notes.pdf, Eq. 1.56
>
> $$\begin{aligned}
> \boldsymbol\omega_{1,0} &= \omega\,\mathbf k_0 \quad &\text{(the disk turns about $\mathbf k_0$ at the rate of the angle $\omega t$)} \\
> \dot{\mathbf i}_1 &= \omega\,\mathbf k_0 \times \left(\cos\omega t\,\mathbf i_0 + \sin\omega t\,\mathbf j_0\right) \quad &\text{(derivative of a turning unit vector, $\boldsymbol\omega\times\mathbf u$)} \\
> &= \omega\cos\omega t\,\mathbf j_0 - \omega\sin\omega t\,\mathbf i_0 = \omega\,\mathbf j_1 \quad &\text{(right-handed products; components of $\mathbf j_1$)} \\
> \dot{\mathbf j}_1 &= \omega\,\mathbf k_0 \times \left(-\sin\omega t\,\mathbf i_0 + \cos\omega t\,\mathbf j_0\right) \quad &\text{(derivative of a turning unit vector, $\boldsymbol\omega\times\mathbf u$)} \\
> &= -\omega\sin\omega t\,\mathbf j_0 - \omega\cos\omega t\,\mathbf i_0 = -\omega\,\mathbf i_1 \quad &\text{(right-handed products; components of $\mathbf i_1$)}
> \end{aligned}$$
>
> As a check, the chain rule on the components gives the same result: the derivative of $\cos\omega t$ is $-\omega\sin\omega t$ and that of $\sin\omega t$ is $\omega\cos\omega t$.
>
> $$\boxed{\dot{\mathbf i}_1 = \omega\,\mathbf j_1,\qquad \dot{\mathbf j}_1 = -\omega\,\mathbf i_1}$$
>
> **Units:** $[\mathrm{T^{-1}}]$
> **Meaning:** the tip of each disk unit vector moves on the unit circle at the rate of the disk, a right angle ahead of the vector.

> [!derivation] Velocity of the centre of mass
> **Law:** definition of velocity as the time derivative of the position vector in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> \mathbf v_0^G &= \frac{d}{dt}\left(\mathbf r_0^C + \ell\,\mathbf i_1\right) \quad &\text{(definition of velocity)} \\
> &= \dot{\mathbf r}_0^C + \dot\ell\,\mathbf i_1 + \ell\,\dot{\mathbf i}_1 \quad &\text{(product rule)} \\
> &= \dot x_0^C\,\mathbf i_0 + \dot y_0^C\,\mathbf j_0 + \ell\omega\,\mathbf j_1 \quad &\text{($\ell$ constant; previous box; fixed unit vectors have zero derivative)} \\
> &= \left(\dot x_0^C - \ell\omega\sin\omega t\right)\mathbf i_0 + \left(\dot y_0^C + \ell\omega\cos\omega t\right)\mathbf j_0 \quad &\text{(components of $\mathbf j_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^G = \mathbf v_0^C + \ell\omega\,\mathbf j_1}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ and $[\mathrm{L}][\mathrm{T^{-1}}]$
> **Meaning:** the centre of mass moves with the geometric centre plus a velocity of magnitude the unbalance times the rate, perpendicular to the segment from $C$ to $G$.

> [!derivation] Acceleration of the centre of mass
> **Law:** definition of acceleration as the time derivative of the velocity in $S_0$; product rule
> **Source:** Notes.pdf, Eq. 2.7; Notes.pdf, Eq. 1.62
>
> $$\begin{aligned}
> \mathbf a_0^G &= \frac{d}{dt}\left(\mathbf v_0^C + \ell\omega\,\mathbf j_1\right) \quad &\text{(definition of acceleration)} \\
> &= \ddot{\mathbf r}_0^C + \ell\dot\omega\,\mathbf j_1 + \ell\omega\,\dot{\mathbf j}_1 \quad &\text{(product rule; $\ell$ constant)} \\
> &= \ddot{\mathbf r}_0^C - \ell\omega^2\,\mathbf i_1 \quad &\text{($\omega$ constant; derivative of $\mathbf j_1$)} \\
> &= \left(\ddot x_0^C - \ell\omega^2\cos\omega t\right)\mathbf i_0 + \left(\ddot y_0^C - \ell\omega^2\sin\omega t\right)\mathbf j_0 \quad &\text{(components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf a_0^G = \ddot x_0^G\,\mathbf i_0 + \ddot y_0^G\,\mathbf j_0 = \mathbf a_0^C - \ell\omega^2\,\mathbf i_1}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ and $[\mathrm{L}][\mathrm{T^{-2}}]$
> **Meaning:** the acceleration of $G$ is that of $C$ plus the centripetal acceleration of the turning unbalance, pointing from $G$ back toward $C$.

### Forces and Equations of Motion

![[attachments/EM-SOL/p45-free-body.svg]]

> [!derivation] Forces on the disk
> **Law:** inventory of the external forces; elastic restoring force proportional to the displacement of $C$
> **Source:** Notes.pdf, Eq. 5.1; [Lecture 6, Slide 5]; Problems.pdf, p. 31
>
> The frame $S_0$ is inertial, so no inertia force appears. The weight is neglected and the motor acts through a couple of zero resultant. The elastic force acts at $C$ and points from $C$ toward $O$; the reaction that keeps the disk in its plane is normal to it. The position of $C$ is then written with the position of $G$ (box of the position vectors), so that the unknowns are the coordinates of $G$ only.
>
> $$\begin{aligned}
> \mathbf F_k &= -k\,\mathbf r_0^C \quad &\text{(restoring force of zero natural length, acting at $C$)} \\
> \mathbf R &= R_z\,\mathbf k_0 \quad &\text{(reaction of the plane of motion, unknown)} \\
> \mathbf r_0^C &= \mathbf r_0^G - \ell\,\mathbf i_1 \quad &\text{(position vector of $G$ solved for $C$)} \\
> \mathbf F_k &= -k\,\mathbf r_0^G + k\ell\,\mathbf i_1 \quad &\text{(substitution)} \\
> &= \left(-k x_0^G + k\ell\cos\omega t\right)\mathbf i_0 + \left(-k y_0^G + k\ell\sin\omega t\right)\mathbf j_0 \quad &\text{(components of $\mathbf i_1$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_k = -k\,\mathbf r_0^G + k\ell\cos\omega t\,\mathbf i_0 + k\ell\sin\omega t\,\mathbf j_0, \qquad \mathbf R = R_z\,\mathbf k_0}$$
>
> **Units:** $[k][\mathrm{L}] = [\mathrm{M\,T^{-2}}][\mathrm{L}] = [\mathrm{M\,L\,T^{-2}}]$ for $\mathbf F_k$ and each of its terms; $[R_z] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** seen from $G$, the spring acts as a restoring force toward $O$ plus a force of constant magnitude $k\ell$ that turns with the unbalance: the excitation of the rotor.

> [!derivation] Equation of the dynamics of the centre of mass
> **Law:** Newton's second law for the particle $G$ in the inertial frame $S_0$, projected on $\mathcal B_0$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5; Notes.pdf, Eq. 5.32
>
> $$\begin{aligned}
> m\,\mathbf a_0^G &= \mathbf F_k + \mathbf R \quad &\text{(Newton's second law with every external force)} \\
> m\ddot x_0^G\,\mathbf i_0 + m\ddot y_0^G\,\mathbf j_0 &= \left(-k x_0^G + k\ell\cos\omega t\right)\mathbf i_0 + \left(-k y_0^G + k\ell\sin\omega t\right)\mathbf j_0 + R_z\,\mathbf k_0 \quad &\text{(acceleration and forces in $\mathcal B_0$)} \\
> \mathbf k_0:\quad 0 &= R_z \quad &\text{(dot product with $\mathbf k_0$: planar motion, weight neglected)} \\
> \mathbf i_0:\quad m\ddot x_0^G &= -k x_0^G + k\ell\cos\omega t \quad &\text{(dot product with $\mathbf i_0$)} \\
> \mathbf j_0:\quad m\ddot y_0^G &= -k y_0^G + k\ell\sin\omega t \quad &\text{(dot product with $\mathbf j_0$)} \\
> \ddot x_0^G + \omega_0^2 x_0^G &= \omega_0^2\ell\cos\omega t \quad &\text{(division by $m$; $\omega_0^2$ is $k/m$)} \\
> \ddot y_0^G + \omega_0^2 y_0^G &= \omega_0^2\ell\sin\omega t \quad &\text{(the same for the second component)}
> \end{aligned}$$
>
> $$\boxed{m\ddot{\mathbf r}_0^G + k\,\mathbf r_0^G = k\ell\,\mathbf i_1, \qquad \ddot x_0^G + \omega_0^2 x_0^G = \omega_0^2\ell\cos\omega t, \qquad \ddot y_0^G + \omega_0^2 y_0^G = \omega_0^2\ell\sin\omega t, \qquad R_z = 0}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$ for the vector equation and for $R_z$; $[\mathrm{L\,T^{-2}}]$ on both sides of the scalar equations; $[\omega_0^2] = [k/m] = [\mathrm{M\,T^{-2}}][\mathrm{M^{-1}}] = [\mathrm{T^{-2}}]$
> **Meaning:** each coordinate of $G$ is an undamped harmonic oscillator of natural frequency $\omega_0$ under a harmonic force at the rate of the disk (Notes.pdf, Eq. 5.32 with zero damping); the two equations are uncoupled, and the plane of motion carries no load.

### Answers and Checks

#### Particular solution for the centre of mass

> [!derivation] Steady motion of the centre of mass
> **Law:** general solution of a linear equation as homogeneous plus particular solution; method of undetermined coefficients for a harmonic forcing
> **Source:** Notes.pdf, Eq. 5.7; Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3]; [Lecture 6, Slide 11]
>
> The homogeneous solution is the free oscillation at $\omega_0$ (Notes.pdf, Eq. 5.7); the statement assumes it has died out. The forcing is harmonic at $\omega$, so the particular solution is sought as the same harmonic with an unknown amplitude, for $\omega \neq \omega_0$.
>
> $$\begin{aligned}
> x_0^G &= x_h + x_p,\quad x_h = C_1\cos\omega_0 t + C_2\sin\omega_0 t \to 0 \quad &\text{(general solution; homogeneous part damped out, hypothesis)} \\
> x_p &= a\cos\omega t \quad &\text{(trial function at the forcing frequency)} \\
> \dot x_p &= -a\omega\sin\omega t \quad &\text{(chain rule: derivative of $\cos u$ times the derivative of $u = \omega t$)} \\
> \ddot x_p &= -a\omega^2\cos\omega t \quad &\text{(chain rule again)} \\
> -a\omega^2\cos\omega t + \omega_0^2 a\cos\omega t &= \omega_0^2\ell\cos\omega t \quad &\text{(substitution in the equation of $x_0^G$)} \\
> a\left(\omega_0^2 - \omega^2\right) &= \omega_0^2\ell \quad &\text{(coefficients of $\cos\omega t$ equated)} \\
> a &= \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2} \quad &\text{(division, valid for $\omega \neq \omega_0$)} \\
> y_p &= b\sin\omega t,\quad \ddot y_p = -b\omega^2\sin\omega t \quad &\text{(same trial for the second component; chain rule twice)} \\
> b\left(\omega_0^2 - \omega^2\right) &= \omega_0^2\ell \Rightarrow b = a \quad &\text{(coefficients of $\sin\omega t$ equated)}
> \end{aligned}$$
>
> $$\boxed{x_0^G(t) = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\cos\omega t,\qquad y_0^G(t) = \frac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\sin\omega t,\qquad \omega_0 = \sqrt{k/m}}$$
>
> **Units:** $[a] = [b] = [\mathrm{T^{-2}}][\mathrm{L}]/[\mathrm{T^{-2}}] = [\mathrm{L}]$, so $x_0^G$, $y_0^G$, $x_h$, $x_p$ and $y_p$ are in $[\mathrm{L}]$; $[\omega_0] = ([\mathrm{M\,T^{-2}}]/[\mathrm{M}])^{1/2} = [\mathrm{T^{-1}}]$; $\omega t$ dimensionless
> **Meaning:** in steady state $G$ describes a circle about $O$ at the rate of the disk, and stays on the line through $O$ along the unbalance direction: the position vector of $G$ is the amplitude times $\mathbf i_1$.

#### Position of the geometric centre

> [!derivation] Steady motion of the geometric centre
> **Law:** position vector of $C$ from that of $G$ and the unbalance
> **Source:** Notes.pdf, Eq. 2.2; Problems.pdf, p. 31
>
> $$\begin{aligned}
> x_0^C &= x_0^G - \ell\cos\omega t \quad &\text{(box of the position vectors, first component)} \\
> &= \left(\frac{\omega_0^2}{\omega_0^2 - \omega^2} - 1\right)\ell\cos\omega t \quad &\text{(common factor $\ell\cos\omega t$)} \\
> &= \frac{\omega_0^2 - \omega_0^2 + \omega^2}{\omega_0^2 - \omega^2}\,\ell\cos\omega t \quad &\text{(common denominator)} \\
> &= \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t \quad &\text{(the squares of $\omega_0$ cancel)} \\
> y_0^C &= y_0^G - \ell\sin\omega t = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\sin\omega t \quad &\text{(same steps for the second component)}
> \end{aligned}$$
>
> $$\boxed{x_0^C(t) = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t,\qquad y_0^C(t) = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\sin\omega t}$$
>
> **Units:** $[\mathrm{T^{-2}}][\mathrm{L}]/[\mathrm{T^{-2}}] = [\mathrm{L}]$
> **Meaning:** the geometric centre also whirls in a circle about $O$ at the rate of the disk; $O$, $C$ and $G$ stay on one line, the line of $\mathbf i_1$.

#### Is the distance OC larger than OG above the natural frequency?

![[attachments/EM-SOL/p45-sub-super.svg]]

> [!derivation] Radii of the two circles and their ratio
> **Law:** magnitude of a position vector from its Cartesian components
> **Source:** Notes.pdf, Eq. 2.5; Problems.pdf, p. 31
>
> $$\begin{aligned}
> |OG| &= \sqrt{\left(x_0^G\right)^2 + \left(y_0^G\right)^2} = \frac{\omega_0^2\ell}{\left|\omega_0^2 - \omega^2\right|}\sqrt{\cos^2\omega t + \sin^2\omega t} \quad &\text{(common factor; square root of a square is the absolute value)} \\
> &= \frac{\omega_0^2\ell}{\left|\omega_0^2 - \omega^2\right|} \quad &\text{(Pythagorean identity)} \\
> |OC| &= \frac{\omega^2\ell}{\left|\omega_0^2 - \omega^2\right|} \quad &\text{(same steps with the components of $C$)} \\
> \frac{|OC|}{|OG|} &= \frac{\omega^2}{\omega_0^2} = \frac{m\omega^2}{k} \quad &\text{(quotient; the common factor cancels)} \\
> \omega \gt \omega_0 &\Leftrightarrow \frac{\omega^2}{\omega_0^2} \gt 1 \Leftrightarrow |OC| \gt |OG| \quad &\text{(both rates positive, squaring keeps the order)}
> \end{aligned}$$
>
> $$\boxed{\frac{|OC|}{|OG|} = \frac{m\omega^2}{k},\qquad \omega \gt \sqrt{k/m} \Rightarrow |OC| \gt |OG|\ \text{(yes)}}$$
>
> **Units:** $[\mathrm{M}][\mathrm{T^{-2}}]/[\mathrm{M\,T^{-2}}] = [1]$
> **Meaning:** above the natural frequency the amplitude of $G$ has the opposite sign to the unbalance, so $G$ lies between $O$ and $C$: the rotor turns about a point closer to its centre of mass than to its geometric centre. Below it, $C$ lies between $O$ and $G$ and the opposite inequality holds.

> [!derivation] The excluded case of resonance
> **Law:** particular solution when the forcing frequency equals the natural frequency (secular term)
> **Source:** Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3]
>
> At equal rates the trial function solves the homogeneous equation and gives no amplitude. A trial with a factor $t$ is used; the derivatives are written with the product rule and the chain rule.
>
> $$\begin{aligned}
> x_p &= D\,t\sin\omega_0 t \quad &\text{(trial function with a factor $t$)} \\
> \dot x_p &= D\sin\omega_0 t + D\omega_0 t\cos\omega_0 t \quad &\text{(product rule; chain rule on $\sin\omega_0 t$)} \\
> \ddot x_p &= 2D\omega_0\cos\omega_0 t - D\omega_0^2 t\sin\omega_0 t \quad &\text{(product rule on the second term; chain rule)} \\
> \ddot x_p + \omega_0^2 x_p &= 2D\omega_0\cos\omega_0 t \quad &\text{(the terms in $t\sin\omega_0 t$ cancel)} \\
> 2D\omega_0 &= \omega_0^2\ell \Rightarrow D = \frac{\omega_0\ell}{2} \quad &\text{(coefficients of $\cos\omega_0 t$ equated)}
> \end{aligned}$$
>
> $$\boxed{\omega = \omega_0:\quad x_p(t) = \frac{\omega_0\ell}{2}\,t\sin\omega_0 t\ \text{(particular solution; grows without bound; the free oscillation is added to it)}}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L}][\mathrm{T}] = [\mathrm{L}]$
> **Meaning:** at the critical speed the undamped whirl grows linearly in time; the ratio of radii of the previous box is not defined there, so the question concerns the speeds above it.

#### Limiting cases

> [!derivation] Slow and fast rotation
> **Law:** limits of the steady solution
> **Source:** Notes.pdf, Eq. 5.47; [Lecture 6, Slide 13]
>
> $$\begin{aligned}
> \omega \to 0 &: \quad x_0^G \to \ell\cos\omega t,\quad x_0^C \to 0 \quad &\text{($\omega^2$ negligible against $\omega_0^2$)} \\
> \omega \gg \omega_0 &: \quad x_0^G \to -\frac{\omega_0^2}{\omega^2}\,\ell\cos\omega t \to 0,\quad x_0^C \to -\ell\cos\omega t \quad &\text{($\omega_0^2$ negligible against $\omega^2$)}
> \end{aligned}$$
>
> $$\boxed{\omega \ll \omega_0:\ |OC| \to 0,\ |OG| \to \ell;\qquad \omega \gg \omega_0:\ |OG| \to 0,\ |OC| \to \ell}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** a slow rotor turns about its geometric centre, held at the design position; a fast rotor self-centres and turns about its centre of mass, the geometric centre then circling it at the distance of the unbalance. This is the out-of-phase regime of a fast forcing described in Notes.pdf, Eq. 5.47 and the text after it.

#### Independent check and answers

> [!derivation] Independent check through the equation of the geometric centre
> **Law:** Newton's second law written with the acceleration of $C$ as the unknown
> **Source:** Notes.pdf, Eq. 4.4; Problems.pdf, p. 76
>
> $$\begin{aligned}
> m\left(\ddot{\mathbf r}_0^C - \ell\omega^2\,\mathbf i_1\right) &= -k\,\mathbf r_0^C + R_z\,\mathbf k_0 \quad &\text{(acceleration of $G$ written with that of $C$; every external force)} \\
> \mathbf k_0:\quad R_z &= 0 \quad &\text{(dot product with $\mathbf k_0$, as before: planar motion)} \\
> \ddot x_0^C + \omega_0^2 x_0^C &= \omega^2\ell\cos\omega t \quad &\text{(projection on $\mathbf i_0$, division by $m$)} \\
> x_0^C &= c_1\cos\omega t,\quad \ddot x_0^C = -c_1\omega^2\cos\omega t \quad &\text{(trial function; chain rule twice)} \\
> c_1\left(\omega_0^2 - \omega^2\right) &= \omega^2\ell \quad &\text{(coefficients of $\cos\omega t$ equated)}
> \end{aligned}$$
>
> $$\boxed{x_0^C(t) = \frac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t\ \text{(the same as above, from the other unknown)}}$$
>
> **Units:** $[\mathrm{L}]$
> **Meaning:** the forcing on $C$ is the centrifugal effect of the unbalance, of amplitude proportional to the square of the rate; solving for $C$ first and then adding the unbalance gives back the result for $G$.

| Part of the statement | Answer |
| :--- | :--- |
| Equation of the dynamics of $G$ | $m\ddot{\mathbf r}_0^G + k\,\mathbf r_0^G = k\ell\,\mathbf i_1$, i.e. $\ddot x_0^G + \omega_0^2 x_0^G = \omega_0^2\ell\cos\omega t$ and $\ddot y_0^G + \omega_0^2 y_0^G = \omega_0^2\ell\sin\omega t$, with $\omega_0 = \sqrt{k/m}$ |
| Steady motion of $G$ ($\omega \ne \omega_0$) | $x_0^G(t) = \dfrac{\omega_0^2\ell}{\omega_0^2 - \omega^2}\cos\omega t$ (and $y_0^G$ with $\sin\omega t$) |
| Steady motion of $C$ | $x_0^C(t) = \dfrac{\omega^2\ell}{\omega_0^2 - \omega^2}\cos\omega t$ (and $y_0^C$ with $\sin\omega t$) |
| Is $\lvert OC\rvert \gt \lvert OG\rvert$ for $\omega \gt \sqrt{k/m}$? | Yes: $\lvert OC\rvert/\lvert OG\rvert = m\omega^2/k \gt 1$; for $\omega \lt \sqrt{k/m}$ the opposite holds, and at $\omega = \sqrt{k/m}$ the undamped response grows without bound |

**Check against the official key:** Problems.pdf, p. 76, item 45, gives, for a rate different from the natural frequency, the particular solutions of the coordinates of $G$ and $C$ along $\mathbf i_0$ with the same amplitudes as the table above: **match**. The second components, the ratio of the radii and the answer to the last question follow from them and are not printed in the key. A Runge-Kutta integration of the equation of $G$ with a small added damping (natural frequency 1 rad/s, rate 1.5 rad/s, unbalance 1 m) settles on a circle of radius 0.80 m for $G$ and 1.80 m for $C$, the values of the two formulas.

---

## Problem 46: Bumpy Taxiway

### Reference Frames, Bases and Coordinates

The airplane is modelled as a heavy particle $P$ of mass $m$ carried by a landing gear: a spring of stiffness $k$ and natural length $L$ (and, in part (c), a damper of constant $\lambda$) whose lower end rolls on the runway. The airplane advances at the constant horizontal speed $c$, so the lower end of the gear follows the profile of the runway and moves up and down in time: the vertical motion of $P$ is that of an oscillator excited through its base. The tools are those of chapters 4 and 5 of Notes.pdf and of Lecture 6 (Problems.pdf, p. 31).

| Item | Definition |
| :--- | :--- |
| Fixed (inertial) frame | $S_0 = \{O;\ \mathcal B_0\}$ attached to the runway, $O$ on the mean level of the profile, below the position of the wheel at $t = 0$ (Notes.pdf, Eq. 2.1) |
| Fixed basis | $\mathcal B_0 = \{\mathbf i, \mathbf j, \mathbf k\}$: $\mathbf i$ horizontal along the runway in the sense of taxiing, $\mathbf j$ vertical upward, $\mathbf k = \mathbf i\times\mathbf j$ out of the paper (⊙) in the figure |
| Moving frames | none |
| Points | $P$ the airplane; $B$ the lower end of the gear, in contact with the runway |
| Coordinates | $x_P = c\,t$ (prescribed horizontal motion); $y(t)$ height of $P$, the unknown; $y_b(t)$ height of $B$ |
| Profile | $y_1 = h\sin(\kappa x)$ with $h = 1$ m and $\kappa = 1$ rad/m: the statement writes $\sin x$ with lengths in metres, and the two symbols only keep the units visible |
| Data | $m$ [kg]; $k$ [N/m]; $L$ [m]; $c$ [m/s]; $\lambda$ [N s/m] (part c); $g$ [m s$^{-2}$] |
| Derived data | $\Omega = \kappa c$ [rad/s], angular frequency of the excitation; $\omega_0 = \sqrt{k/m}$ [rad/s]; $\gamma = \lambda/(2m)$ [s$^{-1}$] (Notes.pdf, Eq. 5.23) |
| Hypotheses | the wheel is a point that never leaves the runway (the unilateral contact is assumed active); the gear stays vertical, below $P$; the spring and the damper are linear; the gear (spring, damper and wheel) is massless, so the force it exerts on $P$ equals the contact force at $B$; the horizontal speed is constant: the net horizontal force $F_x\,\mathbf i$ (engine thrust, which acts on the airframe, minus the rolling resistance transmitted by the gear) vanishes; gravity acts on $P$ |
| Constraints | $x_P = c\,t$ (prescribed, rheonomic); $z_P = 0$; $B$ on the profile under $P$ |
| Degrees of freedom | 1, the height $y$ |

![[attachments/EM-SOL/p46-taxiway-plane.svg]]

### Change of Basis and Position Vector

> [!derivation] The only basis and its change of basis matrix
> **Law:** change of basis matrix between two bases; orthonormality and unit determinant
> **Source:** Notes.pdf, Eq. 1.13; Notes.pdf, Eq. 1.14; Notes.pdf, Eq. 1.15
>
> $$\begin{aligned}
> \mathbf i &= 1\,\mathbf i + 0\,\mathbf j + 0\,\mathbf k, \quad \mathbf j = 0\,\mathbf i + 1\,\mathbf j + 0\,\mathbf k, \quad \mathbf k = 0\,\mathbf i + 0\,\mathbf j + 1\,\mathbf k \quad &\text{(columns: components of $\mathbf i$, $\mathbf j$, $\mathbf k$ in $\mathcal B_0$)} \\
> \det[{}_0R_0] &= 1\cdot(1\cdot 1 - 0\cdot 0) - 0 + 0 = 1 \quad &\text{(expansion along the first row)} \\
> [{}_0R_0][{}_0R_0]^T &= I\,I = I \quad &\text{(the identity is symmetric and equal to its square)}
> \end{aligned}$$
>
> $$\boxed{[{}_0R_0] = \begin{pmatrix} 1 & 0 & 0 \cr 0 & 1 & 0 \cr 0 & 0 & 1 \end{pmatrix}, \quad \det[{}_0R_0] = 1, \quad [{}_0R_0][{}_0R_0]^T = I}$$
>
> **Units:** every entry is a direction cosine: $[1]$
> **Meaning:** no rotation is involved; the unit vectors of $\mathcal B_0$ are constant in $S_0$.

> [!derivation] Position vectors of the airplane and of the wheel; length of the gear
> **Law:** position vector in Cartesian components; composition of a function of the abscissa with the prescribed motion
> **Source:** Notes.pdf, Eq. 2.2; Notes.pdf, Eq. 2.5; Problems.pdf, p. 31
>
> $$\begin{aligned}
> \mathbf r_0^P &= x_P\,\mathbf i + y\,\mathbf j = c\,t\,\mathbf i + y\,\mathbf j \quad &\text{(prescribed abscissa, unknown height)} \\
> \mathbf r_0^B &= c\,t\,\mathbf i + y_b\,\mathbf j, \quad y_b(t) = h\sin\left(\kappa\,x_P(t)\right) = h\sin\left(\kappa c\,t\right) = h\sin\Omega t \quad &\text{($B$ on the profile, vertically below $P$)} \\
> \overrightarrow{BP} &= \mathbf r_0^P - \mathbf r_0^B = \left(y - y_b\right)\mathbf j \quad &\text{(difference of the two position vectors)} \\
> \ell_s &= \left|\overrightarrow{BP}\right| = y - y_b \quad &\text{($P$ above $B$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^P = c\,t\,\mathbf i + y\,\mathbf j, \qquad y_b = h\sin\Omega t, \qquad \ell_s = y - h\sin\Omega t}$$
>
> **Units:** $[\mathrm{L}]$ for the position vectors, $y$, $y_b$, $h$ and $\ell_s$; $[\kappa c\,t] = [\mathrm{L^{-1}}][\mathrm{L\,T^{-1}}][\mathrm{T}] = [1]$; $[\Omega] = [\mathrm{T^{-1}}]$
> **Meaning:** the wheel rises and falls with the bumps at the angular frequency $\Omega$, which grows with the taxiing speed; the gear is compressed when its length is below $L$.

### Kinematics

> [!derivation] Velocities and accelerations
> **Law:** velocity and acceleration as time derivatives in $S_0$; chain rule
> **Source:** Notes.pdf, Eq. 2.6; Notes.pdf, Eq. 2.7
>
> $$\begin{aligned}
> \mathbf v_0^P &= \frac{d}{dt}\left(c\,t\,\mathbf i + y\,\mathbf j\right) = c\,\mathbf i + \dot y\,\mathbf j \quad &\text{(constant $c$ and constant unit vectors)} \\
> \mathbf a_0^P &= \ddot y\,\mathbf j \quad &\text{(derivative once more)} \\
> \dot y_b &= h\cos\left(\Omega t\right)\frac{d}{dt}\left(\Omega t\right) = h\,\Omega\cos\Omega t \quad &\text{(chain rule)} \\
> \dot\ell_s &= \dot y - \dot y_b = \dot y - h\,\Omega\cos\Omega t \quad &\text{(rate of the length of the gear)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^P = c\,\mathbf i + \dot y\,\mathbf j, \qquad \mathbf a_0^P = \ddot y\,\mathbf j, \qquad \dot y_b = h\,\Omega\cos\Omega t}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$ for $\mathbf v_0^P$, $c$, $\dot y$, $\dot y_b$ and $\dot\ell_s$; $[\mathrm{L\,T^{-2}}]$ for $\mathbf a_0^P$
> **Meaning:** the horizontal motion is uniform, so all the acceleration is vertical; the wheel moves vertically faster when the airplane taxies faster.

### Forces and Equations of Motion

The free-body diagram of $P$ shows the weight, the force of the spring and the force of the damper (both along the gear), and the net horizontal force (engine thrust, acting on the airframe, minus the rolling resistance transmitted by the gear). $S_0$ is inertial, so no inertia force acts.

![[attachments/EM-SOL/p46-fbd.svg]]

> [!derivation] Forces on the airplane
> **Law:** linear spring and linear damper along the gear; weight
> **Source:** Notes.pdf, Eq. 5.19; [Lecture 6, Slide 5]
>
> The spring pushes $P$ up when it is compressed (length below $L$) and pulls it down when it is stretched; the damper opposes the rate of change of the length of the gear.
>
> $$\begin{aligned}
> \mathbf F_g &= -m g\,\mathbf j \quad &\text{(weight)} \\
> \mathbf F_k &= -k\left(\ell_s - L\right)\mathbf j = -k\left(y - y_b - L\right)\mathbf j \quad &\text{(spring: minus the stiffness times the elongation)} \\
> \mathbf F_\lambda &= -\lambda\,\dot\ell_s\,\mathbf j = -\lambda\left(\dot y - \dot y_b\right)\mathbf j \quad &\text{(damper: minus its constant times the rate of elongation)} \\
> \mathbf F_x &= F_x\,\mathbf i \quad &\text{(net horizontal force: engine thrust minus the rolling resistance transmitted by the gear, unknown)}
> \end{aligned}$$
>
> $$\boxed{\mathbf F_g = -m g\,\mathbf j, \quad \mathbf F_k = -k\left(y - y_b - L\right)\mathbf j, \quad \mathbf F_\lambda = -\lambda\left(\dot y - \dot y_b\right)\mathbf j, \quad \mathbf F_x = F_x\,\mathbf i}$$
>
> **Units:** $[\mathrm{M\,L\,T^{-2}}]$ for every force: $[k][\mathrm{L}] = [\mathrm{M\,T^{-2}}][\mathrm{L}]$, $[\lambda][\mathrm{L\,T^{-1}}] = [\mathrm{M\,T^{-1}}][\mathrm{L\,T^{-1}}]$
> **Meaning:** the road acts on the airplane only through the gear: through the spring by the position of the wheel and through the damper by its vertical speed.

> [!derivation] Newton's second law and the equation about the static equilibrium
> **Law:** Newton's second law in an inertial frame; projection on $\mathcal B_0$; change of variable to the static equilibrium
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 4.5; Notes.pdf, Eq. 5.32
>
> $$\begin{aligned}
> m\,\mathbf a_0^P &= \mathbf F_g + \mathbf F_k + \mathbf F_\lambda + \mathbf F_x \quad &\text{(second law with every force)} \\
> \mathbf i:\quad 0 &= F_x \quad &\text{(dot product with $\mathbf i$: no horizontal acceleration)} \\
> \mathbf j:\quad m\ddot y &= -m g - k\left(y - y_b - L\right) - \lambda\left(\dot y - \dot y_b\right) \quad &\text{(dot product with $\mathbf j$)} \\
> y_e &= L - \frac{m g}{k} \quad &\text{(static equilibrium on flat ground: $0 = -m g - k(y_e - L)$)} \\
> y &= y_e + z, \quad \dot y = \dot z, \quad \ddot y = \ddot z \quad &\text{(new unknown $z$; $y_e$ is constant)} \\
> m\ddot z + \lambda\dot z + k z &= k\,y_b + \lambda\,\dot y_b \quad &\text{(substitution: the weight and $k(y_e - L)$ cancel)} \\
> \ddot z + 2\gamma\dot z + \omega_0^2 z &= \omega_0^2 h\sin\Omega t + 2\gamma h\,\Omega\cos\Omega t \quad &\text{(division by $m$; $k/m = \omega_0^2$, $\lambda/m = 2\gamma$)}
> \end{aligned}$$
>
> $$\boxed{\ddot z + 2\gamma\dot z + \omega_0^2 z = \omega_0^2 h\sin\Omega t + 2\gamma h\,\Omega\cos\Omega t, \qquad y = L - \frac{m g}{k} + z, \qquad F_x = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-2}}]$ for every term of the scalar equation ($[\gamma] = [\Omega] = [\omega_0] = [\mathrm{T^{-1}}]$, $[h] = [\mathrm{L}]$); $[y_e] = [\mathrm{L}]$; $[F_x] = [\mathrm{M\,L\,T^{-2}}]$
> **Meaning:** about its static position the airplane is a damped harmonic oscillator forced at the frequency of the bumps; the weight only lowers the equilibrium by the static deflection $mg/k$.

### Answers and Checks

#### (a) Resonance without damping

> [!derivation] Forced response without damping
> **Law:** particular solution of the forced oscillator by undetermined coefficients
> **Source:** Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3]; [Lecture 6, Slide 11]
>
> With the damping negligible the equation is the undamped one, and the general solution is the free oscillation at $\omega_0$ plus a particular solution at the frequency of the forcing.
>
> $$\begin{aligned}
> \ddot z + \omega_0^2 z &= \omega_0^2 h\sin\Omega t \quad &\text{(equation with $\gamma = 0$)} \\
> z_p &= A\sin\Omega t, \quad \dot z_p = A\Omega\cos\Omega t, \quad \ddot z_p = -A\Omega^2\sin\Omega t \quad &\text{(trial function; chain rule twice)} \\
> \left(\omega_0^2 - \Omega^2\right)A\sin\Omega t &= \omega_0^2 h\sin\Omega t \quad &\text{(substitution)} \\
> A &= \frac{\omega_0^2 h}{\omega_0^2 - \Omega^2} \quad &\text{(coefficients equated, $\Omega \neq \omega_0$)} \\
> z &= C_1\cos\omega_0 t + C_2\sin\omega_0 t + A\sin\Omega t \quad &\text{(free plus forced oscillation)}
> \end{aligned}$$
>
> $$\boxed{z_p = \frac{\omega_0^2 h}{\omega_0^2 - \Omega^2}\sin\Omega t, \qquad \Omega = \kappa c}$$
>
> **Units:** $[A] = [\mathrm{T^{-2}}][\mathrm{L}]/[\mathrm{T^{-2}}] = [\mathrm{L}]$; $C_1$, $C_2$ and $z$ in $[\mathrm{L}]$
> **Meaning:** the forced amplitude grows without limit as the frequency of the bumps approaches the natural frequency of the airplane on its gear.

> [!derivation] Resonant taxiing speed
> **Law:** resonance: the forcing frequency equals the natural frequency; particular solution with a factor $t$
> **Source:** Notes.pdf, Sec. 5.4; [Lecture 6, Slide 3] (trial with a factor $t$, as for a double root; extension of the damped analysis of Sec. 5.4.1)
>
> At equal frequencies the trial of the previous box solves the homogeneous equation and fails; the trial with a factor $t$ is used, with the product rule and the chain rule.
>
> $$\begin{aligned}
> \Omega &= \omega_0 \Leftrightarrow \kappa c = \sqrt{k/m} \quad &\text{(denominator of the amplitude equal to zero)} \\
> z_p &= D\,t\cos\omega_0 t \quad &\text{(trial function with a factor $t$)} \\
> \dot z_p &= D\cos\omega_0 t - D\omega_0 t\sin\omega_0 t \quad &\text{(product rule; chain rule)} \\
> \ddot z_p &= -2D\omega_0\sin\omega_0 t - D\omega_0^2 t\cos\omega_0 t \quad &\text{(the same rules once more)} \\
> \ddot z_p + \omega_0^2 z_p &= -2D\omega_0\sin\omega_0 t = \omega_0^2 h\sin\omega_0 t \quad &\text{(the terms in $t\cos\omega_0 t$ cancel)} \\
> D &= -\frac{\omega_0 h}{2} \quad &\text{(coefficients of $\sin\omega_0 t$ equated)}
> \end{aligned}$$
>
> $$\boxed{c_{\text{res}} = \frac{1}{\kappa}\sqrt{\frac{k}{m}}\ \ (\text{numerically } \sqrt{k/m} \text{ in m/s}), \qquad z_p = -\frac{\omega_0 h}{2}\,t\cos\omega_0 t}$$
>
> **Units:** $[c_{\text{res}}] = [\mathrm{L}][\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$; $[D] = [\mathrm{T^{-1}}][\mathrm{L}]$, so $D\,t$ and $z_p$ are in $[\mathrm{L}]$
> **Meaning:** at this speed one bump arrives every natural period of the airplane on its gear, and without damping the oscillation grows linearly in time.

Contact requires the force of the gear on the airplane to stay compressive, that is, to push $P$ upward. Near the undamped resonance the amplitude grows until this condition fails, and from then on the hypothesis of permanent contact breaks down: the wheel would have to pull on the runway.

> [!derivation] Permanent contact of the wheel
> **Law:** unilateral contact: the runway can only push the wheel; the massless gear transmits the contact force to $P$
> **Source:** Notes.pdf, Eq. 4.4; Notes.pdf, Eq. 5.23; Problems.pdf, p. 31
>
> $$\begin{aligned}
> N &= k\left(L - \ell_s\right) + \lambda\left(\dot y_b - \dot y\right) \ge 0 \quad &\text{(upward component of $\mathbf F_k + \mathbf F_\lambda$: compressive gear)} \\
> \ell_s - L &= y_e + z - y_b - L = z - y_b - \frac{m g}{k} \quad &\text{(box of the position vectors; $y = y_e + z$ with $y_e = L - m g/k$)} \\
> N &= m g - k\left(z - y_b\right) - \lambda\left(\dot z - \dot y_b\right) \quad &\text{(substitution; $\dot y = \dot z$ because $y_e$ is constant)} \\
> \lambda = 0,\ \Omega = \omega_0:\quad N &= m g - k\left(z_h - \frac{\omega_0 h}{2}\,t\cos\omega_0 t - h\sin\omega_0 t\right) \quad &\text{(undamped resonance: $z = z_h + z_p$ of the previous box)} \\
> \frac{\omega_0 h}{2}\,t &\gt \frac{g}{\omega_0^2} + h + \max|z_h| \ \Rightarrow\ N \lt 0 \ \text{where}\ \cos\omega_0 t = -1 \quad &\text{(the secular term exceeds every bounded term; $k/m = \omega_0^2$)}
> \end{aligned}$$
>
> $$\boxed{N = m g - k\left(z - y_b\right) - \lambda\left(\dot z - \dot y_b\right) \ge 0 \ \text{required; it fails at undamped resonance once}\ t \gt \frac{2}{\omega_0 h}\left(\frac{g}{\omega_0^2} + h + \max|z_h|\right)}$$
>
> **Units:** $[N] = [m g] = [k][\mathrm{L}] = [\lambda][\mathrm{L\,T^{-1}}] = [\mathrm{M\,L\,T^{-2}}]$; $\left[\frac{g}{\omega_0^2}\right] = [\mathrm{L}]$; $\left[\frac{2}{\omega_0 h}\right][\mathrm{L}] = [\mathrm{T}]$
> **Meaning:** the static deflection $m g/k$ is the margin of the contact: while the dynamic compression stays below it the wheel keeps touching the runway; at undamped resonance the growing oscillation exhausts this margin in finite time, so the linear model of part (a) is valid only for the first cycles.

#### (b) Amplitude at very high taxiing speed

> [!derivation] Forced amplitude for a very high speed
> **Law:** limit of the forced amplitude when the forcing frequency is much larger than the natural one
> **Source:** Notes.pdf, Sec. 5.4.1; [Lecture 6, Slide 13]
>
> Without damping the free part keeps the amplitude fixed by the initial conditions and does not depend on the speed; the amplitude asked for is that of the forced part.
>
> $$\begin{aligned}
> |A| &= \frac{\omega_0^2 h}{\left|\omega_0^2 - \kappa^2 c^2\right|} \quad &\text{(previous box with $\Omega = \kappa c$)} \\
> &= \frac{\omega_0^2 h}{\kappa^2 c^2 - \omega_0^2} = \frac{\omega_0^2 h}{\kappa^2 c^2}\cdot\frac{1}{1 - \omega_0^2/(\kappa^2 c^2)} \quad &\text{($\kappa c \gt \omega_0$; factor $\kappa^2 c^2$ taken out)} \\
> &\approx \frac{\omega_0^2 h}{\kappa^2 c^2} = \frac{k\,h}{m\,\kappa^2 c^2} \quad &\text{($\omega_0^2/(\kappa^2 c^2) \ll 1$)}
> \end{aligned}$$
>
> $$\boxed{|A| \approx \frac{k\,h}{m\,\kappa^2 c^2}\ \ (\text{numerically } \frac{k}{m c^2} \text{ in metres}), \qquad A \lt 0}$$
>
> **Units:** $\frac{[\mathrm{M\,T^{-2}}][\mathrm{L}]}{[\mathrm{M}][\mathrm{L^{-2}}][\mathrm{L^2\,T^{-2}}]} = [\mathrm{L}]$
> **Meaning:** the airplane cannot follow fast bumps: its forced amplitude decays as the inverse square of the speed and moves in opposition to the road, as a free mass shaken through a soft spring.

#### (c) Landing gear with damping

> [!derivation] Transient: the three damping regimes
> **Law:** characteristic equation of the damped oscillator; underdamped, critical and overdamped solutions
> **Source:** Notes.pdf, Eq. 5.22; Notes.pdf, Eq. 5.23; Notes.pdf, Eq. 5.26; Notes.pdf, Eq. 5.30; Notes.pdf, Eq. 5.31; [Lecture 6, Slide 8]; [Lecture 6, Slide 9]; [Lecture 6, Slide 10]
>
> $$\begin{aligned}
> p^2 + 2\gamma p + \omega_0^2 &= 0 \Rightarrow p = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2} \quad &\text{(trial $e^{pt}$ in the homogeneous equation)} \\
> \gamma \lt \omega_0:\quad z_h &= a\,e^{-\gamma t}\cos\left(\omega t + \phi\right), \quad \omega = \sqrt{\omega_0^2 - \gamma^2} \quad &\text{(underdamped: complex roots)} \\
> \gamma = \omega_0:\quad z_h &= \left(a + b\,t\right)e^{-\gamma t} \quad &\text{(critical: double root)} \\
> \gamma \gt \omega_0:\quad z_h &= A_+ e^{-\gamma_+ t} + A_- e^{-\gamma_- t}, \quad \gamma_\pm = \gamma \pm \sqrt{\gamma^2 - \omega_0^2} \quad &\text{(overdamped: two negative real roots)} \\
> \gamma = \frac{\lambda}{2m} \lesseqgtr \omega_0 = \sqrt{\frac{k}{m}} \ &\Leftrightarrow\ \lambda \lesseqgtr 2\sqrt{k m} \quad &\text{(definitions of $\gamma$ and $\omega_0$; multiplication by $2m$)}
> \end{aligned}$$
>
> $$\boxed{\lambda \lt 2\sqrt{k m}:\ \text{underdamped}; \quad \lambda = 2\sqrt{k m}:\ \text{critical}; \quad \lambda \gt 2\sqrt{k m}:\ \text{overdamped}; \quad z_h \to 0 \text{ in the three cases}}$$
>
> **Units:** $[p] = [\gamma] = [\gamma_\pm] = [\omega] = [\mathrm{T^{-1}}]$; $a$, $A_\pm$, $z_h$ in $[\mathrm{L}]$, $b$ in $[\mathrm{L\,T^{-1}}]$; $[\lambda] = [\sqrt{k m}] = [\mathrm{M\,T^{-1}}]$
> **Meaning:** with any damping the free oscillation dies out: oscillating within the time $1/\gamma$ when underdamped, fastest without oscillation when critical, slowly (time $1/\gamma_-$) when overdamped; afterwards only the forced response remains.

> [!derivation] Steady response with damping
> **Law:** complex representation of the forced oscillator; the imaginary part of a complex solution is a solution
> **Source:** Notes.pdf, Eq. 5.18; Notes.pdf, Eq. 5.35; Notes.pdf, Eq. 5.37; [Lecture 6, Slide 11]
>
> The forcing is the imaginary part of $(\omega_0^2 + 2\mathrm{i}\gamma\Omega)\,h\,e^{\mathrm{i}\Omega t}$, because $\mathrm{Im}\,e^{\mathrm{i}\Omega t} = \sin\Omega t$ and $\mathrm{Im}\,(\mathrm{i}\,e^{\mathrm{i}\Omega t}) = \cos\Omega t$. The complex equation is solved and its imaginary part taken.
>
> $$\begin{aligned}
> \ddot{\tilde z} + 2\gamma\dot{\tilde z} + \omega_0^2\tilde z &= \left(\omega_0^2 + 2\mathrm{i}\gamma\Omega\right)h\,e^{\mathrm{i}\Omega t} \quad &\text{(complex equation)} \\
> \tilde z &= H\,h\,e^{\mathrm{i}\Omega t}, \quad \dot{\tilde z} = \mathrm{i}\Omega\,\tilde z, \quad \ddot{\tilde z} = -\Omega^2\tilde z \quad &\text{(trial at the forcing frequency; chain rule)} \\
> \left(\omega_0^2 - \Omega^2 + 2\mathrm{i}\gamma\Omega\right)H &= \omega_0^2 + 2\mathrm{i}\gamma\Omega \quad &\text{(substitution; division by $h\,e^{\mathrm{i}\Omega t}$)} \\
> |H|^2 &= \frac{\omega_0^4 + 4\gamma^2\Omega^2}{\left(\omega_0^2 - \Omega^2\right)^2 + 4\gamma^2\Omega^2} \quad &\text{(modulus of a quotient: quotient of the moduli)} \\
> z_p &= \mathrm{Im}\,\tilde z = |H|\,h\sin\left(\Omega t + \arg H\right) \quad &\text{(imaginary part; $H = |H|e^{\mathrm{i}\arg H}$)}
> \end{aligned}$$
>
> $$\boxed{z_p = |H|\,h\sin\left(\Omega t + \arg H\right), \qquad |H| = \sqrt{\frac{\omega_0^4 + 4\gamma^2\Omega^2}{\left(\omega_0^2 - \Omega^2\right)^2 + 4\gamma^2\Omega^2}}, \qquad \Omega = \kappa c}$$
>
> **Units:** $[\omega_0^4] = [\gamma^2\Omega^2] = [\mathrm{T^{-4}}]$, so $H$ is dimensionless and $z_p$, $\tilde z$ are in $[\mathrm{L}]$
> **Meaning:** the steady amplitude is the height of the bumps times the factor $|H|$, finite for every speed; it is the same formula in the three damping regimes, which differ only in the transient.

> [!derivation] How the results of (a) and (b) change
> **Law:** value of the amplitude factor at resonance, its maximum and its high-speed limit
> **Source:** Notes.pdf, Eq. 5.41; Notes.pdf, Eq. 5.46; [Lecture 6, Slide 14]
>
> With the ratios $r = \Omega/\omega_0$ and $\zeta = \gamma/\omega_0$ (notation of this solution; critical damping is $\zeta = 1$) and $u = r^2$, the amplitude factor is a function of $u$ whose derivative is taken with the quotient rule. Unlike the force-driven peak of Notes.pdf, Eq. 5.46, which disappears for $\gamma \ge \omega_0/\sqrt2$, the base-excitation factor $|H|$ keeps a maximum for every damping ($u_p \gt 0$); the analysis of $|H|$ is an extension built with the method of Notes.pdf, Sec. 5.4.
>
> $$\begin{aligned}
> |H|^2 &= \frac{1 + 4\zeta^2 u}{\left(1 - u\right)^2 + 4\zeta^2 u} \quad &\text{(numerator and denominator divided by $\omega_0^4$)} \\
> r = 1:\quad |H|^2 &= \frac{1 + 4\zeta^2}{4\zeta^2} = 1 + \frac{1}{4\zeta^2} \quad &\text{(finite at the former resonance)} \\
> \frac{d|H|^2}{du} &= \frac{4\zeta^2\left[(1 - u)^2 + 4\zeta^2 u\right] - \left(1 + 4\zeta^2 u\right)\left[-2(1 - u) + 4\zeta^2\right]}{\left[(1 - u)^2 + 4\zeta^2 u\right]^2} \quad &\text{(quotient rule; chain rule on $(1 - u)^2$)} \\
> &= \frac{2\left(1 - u - 2\zeta^2 u^2\right)}{\left[(1 - u)^2 + 4\zeta^2 u\right]^2} \quad &\text{(numerator expanded: the terms in $\zeta^2$, $\zeta^2 u$ and $\zeta^4 u$ cancel)} \\
> u_p &= \frac{\sqrt{1 + 8\zeta^2} - 1}{4\zeta^2} \gt 0 \quad &\text{(positive root of $2\zeta^2 u^2 + u - 1 = 0$: the derivative changes from positive to negative there, a maximum)} \\
> \left.\left(2\zeta^2 u^2 + u - 1\right)\right|_{u = 0} &= -1, \quad \left.\left(2\zeta^2 u^2 + u - 1\right)\right|_{u = 1} = 2\zeta^2 \gt 0 \ \Rightarrow\ u_p \lt 1 \quad &\text{(change of sign between $u = 0$ and $u = 1$, so its positive root lies below 1)} \\
> u = 2:\quad |H|^2 &= \frac{1 + 8\zeta^2}{1 + 8\zeta^2} = 1 \quad &\text{(the same value for every damping)} \\
> \Omega \gg \omega_0,\ \Omega \gg \frac{\omega_0^2}{2\gamma}:\quad |H| &\approx \frac{2\gamma\Omega}{\Omega^2} = \frac{2\gamma}{\Omega} = \frac{\lambda}{m\kappa c} \quad &\text{(the damping terms dominate the numerator, $\Omega^4$ the denominator)}
> \end{aligned}$$
>
> $$\boxed{|H(\omega_0)| = \sqrt{1 + \frac{\omega_0^2}{4\gamma^2}}, \qquad \Omega_p = \omega_0\sqrt{u_p} \lt \omega_0, \qquad |H(\sqrt2\,\omega_0)| = 1, \qquad |H| \approx \frac{\lambda}{m\kappa c}\ \text{at very high speed}}$$
>
> **Units:** $r$, $\zeta$, $u$, $u_p$ and $|H|$ dimensionless; $[\Omega_p] = [\mathrm{T^{-1}}]$; $\frac{[\mathrm{M\,T^{-1}}]}{[\mathrm{M}][\mathrm{L^{-1}}][\mathrm{L\,T^{-1}}]} = [1]$
> **Meaning:** damping removes the infinite resonance and moves the peak below the natural frequency; below $\sqrt2\,\omega_0$ it reduces the transmitted amplitude, above it increases it, and at very high speed the amplitude decays only as the inverse of the speed, through the force the damper transmits.

> [!derivation] Numerical values of the amplitude factor
> **Law:** evaluation of the formulas of the previous box
> **Source:** Notes.pdf, Eq. 5.41
>
> $$\begin{aligned}
> \zeta = 0.5:\quad u_p &= \sqrt3 - 1 = 0.732, \quad |H|_{\max}^2 = \frac{1.732}{0.8038} = 2.1547, \quad |H|_{\max} = 1.468, \quad |H(\omega_0)| = 1.414 \quad &\text{(underdamped)} \\
> \zeta = 1:\quad u_p &= \frac{3 - 1}{4} = 0.5, \quad |H|_{\max} = \sqrt{\frac{3}{2.25}} = 1.155, \quad |H(\omega_0)| = 1.118 \quad &\text{(critical)} \\
> \zeta = 2:\quad u_p &= \frac{\sqrt{33} - 1}{16} = 0.297, \quad |H|_{\max}^2 = \frac{5.7446}{5.2394} = 1.0964, \quad |H|_{\max} = 1.047, \quad |H(\omega_0)| = 1.031 \quad &\text{(overdamped)}
> \end{aligned}$$
>
> $$\boxed{|H|_{\max} = 1.468,\ 1.155,\ 1.047 \ \text{ for } \zeta = 0.5,\ 1,\ 2}$$
>
> **Units:** every quantity dimensionless
> **Meaning:** the more damping, the lower and flatter the peak; but every curve passes through $|H| = 1$ at $\Omega = \sqrt2\,\omega_0$ and decays more slowly beyond it when the damping is larger.

> [!derivation] Choice of the damping and effect of the payload
> **Law:** critical damping gives the shortest response time; dependence of the damping ratio on the mass
> **Source:** Notes.pdf, Sec. 5.3.3; Notes.pdf, Eq. 5.23
>
> The choice is a design judgement built on the results above: the critical value kills the transient fastest without oscillation (Notes.pdf, Sec. 5.3.3) and keeps the resonant peak low; more damping would lower the peak only slightly further while transmitting more of the fast bumps. The damper is fixed hardware, so its ratio to the critical value changes with the mass.
>
> $$\begin{aligned}
> \lambda_c &= 2 m\omega_0 = 2m\sqrt{\frac{k}{m}} = 2\sqrt{k m} \quad &\text{(critical: $\gamma = \omega_0$, with $\gamma = \lambda/(2m)$)} \\
> \zeta &= \frac{\gamma}{\omega_0} = \frac{\lambda}{2m}\sqrt{\frac{m}{k}} = \frac{\lambda}{2\sqrt{k m}} \propto m^{-1/2} \quad &\text{(damping ratio of a given damper)} \\
> c_{\text{res}} &= \frac{1}{\kappa}\sqrt{\frac{k}{m}} \propto m^{-1/2} \quad &\text{(resonant speed of part (a))} \\
> \lambda &= 2\sqrt{k\,m_{\max}} \Rightarrow \zeta = \sqrt{\frac{m_{\max}}{m}} \ge 1 \quad &\text{(damper critical at the largest mass)}
> \end{aligned}$$
>
> $$\boxed{\lambda = 2\sqrt{k\,m_{\max}}: \ \text{critical at full load, slightly overdamped for lighter loads}}$$
>
> **Units:** $[\lambda_c] = [\mathrm{M\,T^{-1}}]$; $\zeta$ dimensionless; $[c_{\text{res}}] = [\mathrm{L\,T^{-1}}]$; $m$ and $m_{\max}$ in $[\mathrm{M}]$
> **Meaning:** yes, the payload matters: a heavier airplane has a lower resonant speed and a smaller damping ratio. A damper sized at the critical value of the largest mass never lets the transient oscillate; a lighter airplane is then overdamped, with a slower return and somewhat more transmission at high speed, which is the price of never being underdamped.

| Part of the statement | Answer |
| :--- | :--- |
| Equation of motion (about the static equilibrium $y_e = L - mg/k$) | $\ddot z + 2\gamma\dot z + \omega_0^2 z = \omega_0^2 h\sin\Omega t + 2\gamma h\Omega\cos\Omega t$, with $\Omega = \kappa c$ |
| (a) Resonant taxiing speed | $c_{\text{res}} = \sqrt{k/m}/\kappa$, numerically $\sqrt{k/m}$ in m/s |
| (b) Amplitude at very high speed (undamped) | $\lvert A\rvert \approx k h/(m\kappa^2 c^2)$, numerically $k/(mc^2)$ in metres, in opposition to the road |
| (c) Transient | underdamped for $\lambda \lt 2\sqrt{km}$, critical for $\lambda = 2\sqrt{km}$, overdamped above; it dies out in the three cases |
| (c) Steady amplitude | $h\lvert H\rvert$, finite for every speed; at $c_{\text{res}}$ it is $h\sqrt{1 + \omega_0^2/(4\gamma^2)}$; peak below $c_{\text{res}}$; equal to $h$ at $\sqrt2\,c_{\text{res}}$; about $\lambda h/(m\kappa c)$ at very high speed |
| (c) Choice of $\lambda$ and payload | critical damping, $\lambda = 2\sqrt{k m_{\max}}$; the payload changes $\zeta$ and $c_{\text{res}}$ as $m^{-1/2}$, so the damper is sized for the heaviest airplane |

**Check against the official key:** the solution keys of the course (Problems.pdf, p. 76) print no answer for Problem 46: the entry is empty. The results above are checked independently: a Runge-Kutta integration of the damped equation (natural frequency 1.7 rad/s, damping rate 0.3 1/s, excitation 2.3 rad/s, bump height 1 m, 120 s) settles on the amplitude 1.1568 m given by the formula of the amplitude factor; the undamped integration at the resonant frequency grows linearly, as the secular solution predicts; and the maxima of the amplitude factor in the table of numerical values agree with a direct scan of the formula.
