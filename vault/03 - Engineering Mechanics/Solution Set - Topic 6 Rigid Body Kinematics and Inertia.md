---
title: "Solution Set - Topic 6: Rigid Body Kinematics and Inertia"
subject: "Mechanics Applied to Aerospace Engineering"
course: "251-14165 (UC3M)"
source: "sources/cuatrimestre-1/03-engineering-mechanics/problemas/Problems.pdf"
type: "Full Analytical Solutions (lecturer's order)"
language: "English"
tags:
  - solutions
  - topic-6
  - rigid-body-kinematics
---

# Topic 6: Rigid Body Kinematics and Inertia - Full Analytical Solutions

Step-by-step solutions of the official rigid body problems of groups A and B (section 2 of `Problems.pdf`). Every problem follows the order of the course for a rigid body: reference frames, bases and degrees of freedom; change of basis, position vectors and constraint kinematics; centre of mass and inertia tensor; linear momentum, angular momentum and kinetic energy; free-body diagram and equations of motion; answers and checks. Every calculation is inside a derivation box and starts from the definitions of [[Topic 6 - Kinematics of Rigid Bodies and Inertia Properties]]. Statements: [[Problem Set - Topic 6 Rigid Body Kinematics and Inertia]]. Official answers: [[Problem Set - Rigid Body Official Key]]. Subject index: [[Engineering Mechanics MOC]].

---

## Problem RB-34: Velocity field of a rigid body 1

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** one rigid body $b$ observed at a single instant from the fixed frame. The statement gives the positions and velocities of two body points and says that the body is in pure rotation at that instant.
* **Fixed frame:** $S_0$, with origin $O$ and right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$; the origin is at the body point $A$ at this instant, because the statement places $A$ at the origin.
* **Body frame:** no body basis is needed. The problem is a snapshot: every vector is written in the fixed basis and no time derivative is taken.
* **Degrees of freedom:** a free rigid body has six. Its instantaneous velocity field is fixed by six scalars: the three components of the velocity of one body point and the three components of the angular velocity (Notes.pdf, Sec. 9.1.3).
* **Units:** the statement gives pure numbers. They are read in SI units: positions in m, velocities in m/s, so the angular velocity comes out in rad/s.

| Datum | Value in the fixed basis | SI unit |
| :--- | :--- | :--- |
| Position of $A$ | $(0, 0, 0)$ | m |
| Position of $B$ | $(1, 0, 0)$ | m |
| Velocity of $A$ | $(1, 0, 2)$ | m/s |
| Velocity of $B$ | $(c, 1, 0)$, with $c$ unknown | m/s |
| Kind of motion | pure rotation: zero slip velocity | - |

* **Unknowns:** the number $c$, the three components of the angular velocity, and one point $I$ of the instantaneous axis of rotation.
* **Count of equations:** the velocity field between $A$ and $B$ gives three scalar equations. Their component along the segment $AB$ does not contain the angular velocity, so it fixes $c$; the other two fix the two components of the angular velocity perpendicular to $AB$. The pure rotation condition is the sixth piece of information and fixes the component along $AB$.

### Change of Basis, Position Vectors and Constraint Kinematics

No change of basis is needed, because all the data are given in the fixed basis. The relative position vector of the two body points and the difference of their velocities are built first, since the velocity field only contains those two vectors.

![[attachments/EM-SOL/rb34-velocity-field.svg]]

> [!derivation] Relative position and relative velocity of the two body points
> **Law:** subtraction of vectors component by component in the fixed basis
> **Source:** Problems.pdf, p. 64; Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf{AB} &= \mathbf r_0^B - \mathbf r_0^A \quad &\text{(vector from $A$ to $B$: head minus tail)} \\
> &= (1, 0, 0) - (0, 0, 0) \quad &\text{(data of the statement)} \\
> &= (1, 0, 0) \quad &\text{(component by component)} \\
> \mathbf v_0^B - \mathbf v_0^A &= (c, 1, 0) - (1, 0, 2) \quad &\text{(data of the statement)} \\
> &= (c - 1,\ 1,\ -2) \quad &\text{(component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf{AB} = \mathbf i, \qquad \mathbf v_0^B - \mathbf v_0^A = (c-1)\,\mathbf i + \mathbf j - 2\,\mathbf k}$$
>
> **Units:** $\mathbf{AB}$ in $[\mathrm L]$ (m); the velocity difference in $[\mathrm{L\,T^{-1}}]$ (m/s)
> **Meaning:** the segment $AB$ lies along the first axis and has unit length, so the vector products with it are short.

> [!derivation] The unknown c from the rigidity of the segment AB
> **Law:** velocity field of a rigid body projected on the segment that joins the two points (equal projections)
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.7; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> \mathbf v_0^B &= \mathbf v_0^A + \boldsymbol\omega_{b0}\times\mathbf{AB} \quad &\text{(velocity field from $A$ to $B$, Eq. 9.3)} \\
> (\mathbf v_0^B - \mathbf v_0^A)\cdot\mathbf{AB} &= (\boldsymbol\omega_{b0}\times\mathbf{AB})\cdot\mathbf{AB} \quad &\text{(move $\mathbf v_0^A$ to the left and dot-multiply by $\mathbf{AB}$)} \\
> (\boldsymbol\omega_{b0}\times\mathbf{AB})\cdot\mathbf{AB} &= 0 \quad &\text{(a vector product is perpendicular to both of its factors)} \\
> (c - 1)(1) + (1)(0) + (-2)(0) &= 0 \quad &\text{(scalar product with the components of the previous box)} \\
> c &= 1 \quad &\text{(solve for $c$)}
> \end{aligned}$$
>
> $$\boxed{c = 1, \qquad \mathbf v_0^B = \mathbf i + \mathbf j, \qquad \mathbf v_0^B - \mathbf v_0^A = \mathbf j - 2\,\mathbf k}$$
>
> **Units:** $c$ multiplies a unit vector in a velocity, so it is in $[\mathrm{L\,T^{-1}}]$ (m/s); the equation solved is in $[\mathrm{L^2\,T^{-1}}]$ in every term
> **Meaning:** the distance between two points of a rigid body cannot change, so both points have the same velocity component along the line that joins them. Here that component is the first one, and it is 1 m/s for $A$, hence also for $B$.

> [!derivation] Two components of the angular velocity from the velocity field
> **Law:** velocity field of a rigid body, with the vector product expanded by its determinant
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 1.31; [Lecture 7, Slide 6]
>
> Write the unknown angular velocity with components $\omega_x$, $\omega_y$, $\omega_z$ in the fixed basis.
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0}\times\mathbf{AB} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr 1 & 0 & 0 \end{vmatrix} \quad &\text{(determinant form of the vector product)} \\
> &= \mathbf i\,(\omega_y\cdot 0 - \omega_z\cdot 0) - \mathbf j\,(\omega_x\cdot 0 - \omega_z\cdot 1) + \mathbf k\,(\omega_x\cdot 0 - \omega_y\cdot 1) \quad &\text{(expand along the first row)} \\
> &= \omega_z\,\mathbf j - \omega_y\,\mathbf k \quad &\text{(carry out the products)} \\
> \mathbf j - 2\,\mathbf k &= \omega_z\,\mathbf j - \omega_y\,\mathbf k \quad &\text{(Eq. 9.3 with the velocity difference of the previous box)} \\
> \omega_z &= 1 \quad &\text{(equate the components along $\mathbf j$)} \\
> \omega_y &= 2 \quad &\text{(equate the components along $\mathbf k$ and change sign)}
> \end{aligned}$$
>
> $$\boxed{\omega_y = 2\ \mathrm{rad/s}, \qquad \omega_z = 1\ \mathrm{rad/s}, \qquad \omega_x \text{ not fixed by the pair } A, B}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}] = [\mathrm{T^{-1}}][\mathrm L]$, so each component is in $[\mathrm{T^{-1}}]$
> **Meaning:** a rotation about the line $AB$ itself moves neither $A$ nor $B$, so two velocities can never give the component of the angular velocity along the segment that joins them. A third condition is needed.

> [!derivation] Third component from the pure rotation condition
> **Law:** in a pure rotation the slip velocity is zero: the velocity of every body point is perpendicular to the angular velocity
> **Source:** Notes.pdf, Eq. 9.5; Notes.pdf, Eq. 9.11; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> v_{0\parallel} &= \mathbf v_0^A\cdot\mathbf e_\omega \quad &\text{(slip speed: component of any body velocity along the angular velocity, Eq. 9.5)} \\
> \mathbf v_0^A\cdot\boldsymbol\omega_{b0} &= 0 \quad &\text{(pure rotation: zero slip speed; multiply by the modulus of the angular velocity)} \\
> (1)(\omega_x) + (0)(2) + (2)(1) &= 0 \quad &\text{(scalar product with the data and the previous box)} \\
> \omega_x &= -2 \quad &\text{(solve for $\omega_x$)} \\
> \omega_{b0}^2 &= (-2)^2 + 2^2 + 1^2 \quad &\text{(square of the modulus: sum of the squared components)} \\
> &= 9 \quad &\text{(add)} \\
> \mathbf v_0^B\cdot\boldsymbol\omega_{b0} &= (1)(-2) + (1)(2) + (0)(1) \quad &\text{(check with the second point)} \\
> &= 0 \quad &\text{(the velocity of $B$ is also perpendicular to the angular velocity)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega_{b0} = -2\,\mathbf i + 2\,\mathbf j + \mathbf k\ \ \mathrm{rad/s}, \qquad \omega_{b0} = 3\ \mathrm{rad/s}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{T^{-1}}]$ in every term of the condition; the result is in $[\mathrm{T^{-1}}]$
> **Meaning:** the body turns at 3 rad/s about an axis parallel to this vector. The check with $B$ is not an extra condition: the component along the angular velocity is the same for all body points, so it vanishes for all of them once it vanishes for one.

> [!derivation] A point of the instantaneous axis of rotation
> **Law:** a point $I$ of the axis has zero velocity; $I$ is chosen as the foot of the perpendicular from $A$ to the axis
> **Source:** Notes.pdf, Eq. 9.8; Notes.pdf, Eq. 9.9; Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 1.37; [Lecture 7, Slide 9]
>
> $$\begin{aligned}
> \mathbf 0 &= \mathbf v_0^A + \boldsymbol\omega_{b0}\times\mathbf{AI} \quad &\text{(velocity field from $A$ to $I$, with zero velocity at $I$)} \\
> \mathbf 0 &= \boldsymbol\omega_{b0}\times\mathbf v_0^A + \boldsymbol\omega_{b0}\times(\boldsymbol\omega_{b0}\times\mathbf{AI}) \quad &\text{(cross-multiply on the left by the angular velocity)} \\
> \boldsymbol\omega_{b0}\times(\boldsymbol\omega_{b0}\times\mathbf{AI}) &= (\boldsymbol\omega_{b0}\cdot\mathbf{AI})\,\boldsymbol\omega_{b0} - \omega_{b0}^2\,\mathbf{AI} \quad &\text{(double vector product, Eq. 1.37)} \\
> \boldsymbol\omega_{b0}\cdot\mathbf{AI} &= 0 \quad &\text{(choice of $I$: the foot of the perpendicular from $A$)} \\
> \mathbf{AI} &= \frac{\boldsymbol\omega_{b0}\times\mathbf v_0^A}{\omega_{b0}^2} \quad &\text{(substitute the two previous lines and solve)} \\
> \boldsymbol\omega_{b0}\times\mathbf v_0^A &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr -2 & 2 & 1 \cr 1 & 0 & 2 \end{vmatrix} \quad &\text{(determinant form of the vector product)} \\
> &= \mathbf i\,(2\cdot 2 - 1\cdot 0) - \mathbf j\,((-2)\cdot 2 - 1\cdot 1) + \mathbf k\,((-2)\cdot 0 - 2\cdot 1) \quad &\text{(expand along the first row)} \\
> &= 4\,\mathbf i + 5\,\mathbf j - 2\,\mathbf k \quad &\text{(carry out the products)} \\
> \mathbf r_0^I &= \mathbf r_0^A + \mathbf{AI} \quad &\text{(position of $I$ from the origin; $A$ is at the origin)} \\
> &= \frac{1}{9}\,(4\,\mathbf i + 5\,\mathbf j - 2\,\mathbf k) \quad &\text{(divide by the squared modulus, 9)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^I = \frac{4}{9}\,\mathbf i + \frac{5}{9}\,\mathbf j - \frac{2}{9}\,\mathbf k\ \ \mathrm m, \qquad \text{axis: } \mathbf r = \mathbf r_0^I + \lambda\,(-2\,\mathbf i + 2\,\mathbf j + \mathbf k)}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** the body is turning, at this instant, about the line through $I$ parallel to the angular velocity. Any other point of that line (any value of the parameter $\lambda$, in s·m per rad so that the product is a length) is an equally valid answer; $I$ is the one closest to $A$, at a distance of $\sqrt{45}/9 \approx 0.745$ m.

### Center of Mass and Inertia Tensor

This section does not apply: the problem is purely kinematic, and neither the mass of the body nor its distribution enters the velocity field.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for, and none can be computed without the mass properties.

### Free-Body Diagram and Equations of Motion

This section does not apply: the statement gives the motion at one instant and asks for no force, so no equation of motion is written.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Unknown $c$ | $1$ (m/s) |
| Angular velocity of the body | $-2\,\mathbf i + 2\,\mathbf j + \mathbf k$ rad/s, modulus 3 rad/s |
| A point of the instantaneous axis of rotation | $\left(\tfrac49, \tfrac59, -\tfrac29\right)$ m; the axis is the line through it parallel to the angular velocity |

`Problems.pdf` prints no answer for this problem (see [[Problem Set - Rigid Body Official Key]]), so the result is checked by substitution and with limiting cases.

> [!derivation] Check: the point I has zero velocity
> **Law:** velocity field from $A$ to $I$ with the values found
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.8
>
> $$\begin{aligned}
> \boldsymbol\omega_{b0}\times\mathbf{AI} &= \frac19\begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr -2 & 2 & 1 \cr 4 & 5 & -2 \end{vmatrix} \quad &\text{(determinant form, with the common factor taken out)} \\
> &= \frac19\left[\mathbf i\,(2\cdot(-2) - 1\cdot 5) - \mathbf j\,((-2)(-2) - 1\cdot 4) + \mathbf k\,((-2)\cdot 5 - 2\cdot 4)\right] \quad &\text{(expand along the first row)} \\
> &= \frac19\,(-9\,\mathbf i + 0\,\mathbf j - 18\,\mathbf k) \quad &\text{(carry out the products)} \\
> &= -\mathbf i - 2\,\mathbf k \quad &\text{(divide by 9)} \\
> \mathbf v_0^I &= (\mathbf i + 2\,\mathbf k) + (-\mathbf i - 2\,\mathbf k) \quad &\text{(Eq. 9.3: velocity of $A$ plus the product above)} \\
> &= \mathbf 0 \quad &\text{(add component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^I = \mathbf 0}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the point found is at rest at this instant, as a point of the axis of a pure rotation must be.

**Limiting cases and consistency:**

* **Speeds against distances to the axis.** In a pure rotation the speed of a body point is the angular speed times its distance to the axis. For $A$ the speed is $\sqrt5 \approx 2.236$ m/s and the distance to the axis is $\sqrt{45}/9 \approx 0.745$ m; their ratio is 3 rad/s, the modulus found.
* **Without the pure rotation condition** the first component of the angular velocity would stay free, and the slip speed would be a function of it. The data of two points alone describe a one-parameter family of motions; the statement removes the freedom by saying that the rotation is pure.
* **If the velocity of $A$ were zero,** the foot formula gives a zero vector from $A$ to $I$: the axis would pass through $A$, as it must when $A$ itself is at rest.
* **Rigidity.** With the value of $c$ found, the two points have the same velocity component along the segment that joins them, so their distance stays equal to 1 m.

---

## Problem RB-35: Velocity field of a rigid body 2 (Spaceship)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** a spaceship observed at one instant. Three of its points are tracked: the centre of mass $G$, a point $A$ on the solar array and a point $C$ on the rear side.
* **Fixed frame:** $S_0$, with origin $O$ and right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$; at this instant $G$ is at the origin.
* **Body frame:** not needed. The problem is a snapshot written entirely in the fixed basis.
* **Degrees of freedom:** six for a free rigid body. The velocity field at one instant is fixed by the velocity of one point and the angular velocity, six scalars; the statement gives nine (three velocities), so three of them are redundant and must satisfy compatibility conditions.
* **Units:** the numbers of the statement are read in SI units, positions in m and velocities in m/s.

| Point | Position (m) | Velocity (m/s) |
| :--- | :--- | :--- |
| $G$ | $(0, 0, 0)$ | $(8, 4, 0)$ |
| $A$ | $(-2, 4, 0)$ | $(4, 2, 6)$ |
| $C$ | $(-8, 0, 2)$ | $(10, -6, 8)$ |

* **Plan:** part (a) has two levels. The equal-projection test on the three pairs of points is necessary; the data are compatible when, in addition, one single angular velocity reproduces both velocity differences. Part (b) uses that every body point shares the velocity component along the angular velocity, which is the smallest speed found in the body.

### Change of Basis, Position Vectors and Constraint Kinematics

No change of basis is needed. The relative positions and the velocity differences are built first.

![[attachments/EM-SOL/rb35-three-points.svg]]

> [!derivation] Relative positions and velocity differences
> **Law:** subtraction of vectors component by component in the fixed basis
> **Source:** Problems.pdf, p. 64; Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf{GA} &= (-2, 4, 0) - (0, 0, 0) = (-2, 4, 0) \quad &\text{(head minus tail)} \\
> \mathbf{GC} &= (-8, 0, 2) - (0, 0, 0) = (-8, 0, 2) \quad &\text{(head minus tail)} \\
> \mathbf{AC} &= (-8, 0, 2) - (-2, 4, 0) = (-6, -4, 2) \quad &\text{(head minus tail)} \\
> \mathbf v_0^A - \mathbf v_0^G &= (4, 2, 6) - (8, 4, 0) = (-4, -2, 6) \quad &\text{(component by component)} \\
> \mathbf v_0^C - \mathbf v_0^G &= (10, -6, 8) - (8, 4, 0) = (2, -10, 8) \quad &\text{(component by component)} \\
> \mathbf v_0^C - \mathbf v_0^A &= (10, -6, 8) - (4, 2, 6) = (6, -8, 2) \quad &\text{(component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf{GA} = (-2, 4, 0),\quad \mathbf{GC} = (-8, 0, 2),\quad \mathbf{AC} = (-6, -4, 2)\ \ \mathrm m}$$
>
> **Units:** positions in $[\mathrm L]$ (m), velocity differences in $[\mathrm{L\,T^{-1}}]$ (m/s)
> **Meaning:** the three points are not collinear (the second and third vectors are not multiples of the first), so their velocities are enough to fix the whole velocity field.

#### Part (a): compatibility with the rigid body constraint

> [!derivation] Necessary test: equal projections on the three segments
> **Law:** the distance between two points of a rigid body is constant, so their velocity difference is perpendicular to the segment that joins them
> **Source:** Notes.pdf, Eq. 9.7; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> (\mathbf v_0^A - \mathbf v_0^G)\cdot\mathbf{GA} &= (-4)(-2) + (-2)(4) + (6)(0) \quad &\text{(scalar product, pair $G$, $A$)} \\
> &= 8 - 8 + 0 = 0 \quad &\text{(add)} \\
> (\mathbf v_0^C - \mathbf v_0^G)\cdot\mathbf{GC} &= (2)(-8) + (-10)(0) + (8)(2) \quad &\text{(scalar product, pair $G$, $C$)} \\
> &= -16 + 0 + 16 = 0 \quad &\text{(add)} \\
> (\mathbf v_0^C - \mathbf v_0^A)\cdot\mathbf{AC} &= (6)(-6) + (-8)(-4) + (2)(2) \quad &\text{(scalar product, pair $A$, $C$)} \\
> &= -36 + 32 + 4 = 0 \quad &\text{(add)}
> \end{aligned}$$
>
> $$\boxed{(\mathbf v_0^A - \mathbf v_0^G)\cdot\mathbf{GA} = 0,\qquad (\mathbf v_0^C - \mathbf v_0^G)\cdot\mathbf{GC} = 0,\qquad (\mathbf v_0^C - \mathbf v_0^A)\cdot\mathbf{AC} = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm L] = [\mathrm{L^2\,T^{-1}}]$ in every product
> **Meaning:** none of the three distances is changing at this instant. The data pass the test.

> [!derivation] Angular velocity from the pair G, A
> **Law:** velocity field of a rigid body, with the vector product expanded by its determinant
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.12; Notes.pdf, Eq. 1.31
>
> $$\begin{aligned}
> \mathbf v_0^A - \mathbf v_0^G &= \boldsymbol\omega\times\mathbf{GA} \quad &\text{(velocity field from $G$ to $A$)} \\
> \boldsymbol\omega\times\mathbf{GA} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -2 & 4 & 0 \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\,(\omega_y\cdot 0 - \omega_z\cdot 4) - \mathbf j\,(\omega_x\cdot 0 - \omega_z\cdot(-2)) + \mathbf k\,(\omega_x\cdot 4 - \omega_y\cdot(-2)) \quad &\text{(expand along the first row)} \\
> &= -4\omega_z\,\mathbf i - 2\omega_z\,\mathbf j + (4\omega_x + 2\omega_y)\,\mathbf k \quad &\text{(carry out the products)} \\
> -4\omega_z &= -4 \quad &\text{(components along $\mathbf i$)} \\
> -2\omega_z &= -2 \quad &\text{(components along $\mathbf j$: the same condition, already satisfied)} \\
> 4\omega_x + 2\omega_y &= 6 \quad &\text{(components along $\mathbf k$)}
> \end{aligned}$$
>
> $$\boxed{\omega_z = 1,\qquad 4\omega_x + 2\omega_y = 6}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}] = [\mathrm{T^{-1}}][\mathrm L]$, components of the angular velocity in rad/s
> **Meaning:** one pair of points gives only two independent conditions, because a rotation about the line that joins them is invisible to both. The first two components agree with each other, which is the equal-projection test seen again.

> [!derivation] Angular velocity from the pair G, C and compatibility
> **Law:** velocity field of a rigid body; the same angular velocity must hold for every pair
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.13; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> \boldsymbol\omega\times\mathbf{GC} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -8 & 0 & 2 \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\,(\omega_y\cdot 2 - \omega_z\cdot 0) - \mathbf j\,(\omega_x\cdot 2 - \omega_z\cdot(-8)) + \mathbf k\,(\omega_x\cdot 0 - \omega_y\cdot(-8)) \quad &\text{(expand along the first row)} \\
> &= 2\omega_y\,\mathbf i - (2\omega_x + 8\omega_z)\,\mathbf j + 8\omega_y\,\mathbf k \quad &\text{(carry out the products)} \\
> 2\omega_y &= 2 \quad &\text{(components along $\mathbf i$ of the difference $(2, -10, 8)$)} \\
> 8\omega_y &= 8 \quad &\text{(components along $\mathbf k$: the same condition)} \\
> \omega_y &= 1 \quad &\text{(from either of the two)} \\
> -(2\omega_x + 8\cdot 1) &= -10 \quad &\text{(components along $\mathbf j$, with $\omega_z$ of the previous box)} \\
> \omega_x &= 1 \quad &\text{(solve)} \\
> 4(1) + 2(1) &= 6 \quad &\text{(the remaining condition of the pair $G$, $A$ is satisfied)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega = \mathbf i + \mathbf j + \mathbf k\ \ \mathrm{rad/s},\qquad \omega^2 = 3\ \mathrm{rad^2/s^2}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]/[\mathrm L] = [\mathrm{T^{-1}}]$
> **Meaning:** the six scalar equations of the two pairs have one common solution, so the nine measured components describe a rigid motion: the data are compatible.

#### Part (b): minimum speed

![[attachments/EM-SOL/rb35-parallel-perpendicular.svg]]

> [!derivation] The velocity component along the angular velocity is common to all points
> **Law:** velocity field dot-multiplied by the angular velocity; Pythagoras on the parallel and perpendicular parts
> **Source:** Notes.pdf, Eq. 9.5; Notes.pdf, Eq. 9.6; Notes.pdf, Eq. 9.11; [Lecture 7, Slide 9]
>
> For any body point $P$:
>
> $$\begin{aligned}
> \mathbf v_0^P &= \mathbf v_0^G + \boldsymbol\omega\times\mathbf{GP} \quad &\text{(velocity field from $G$ to $P$)} \\
> \mathbf v_0^P\cdot\boldsymbol\omega &= \mathbf v_0^G\cdot\boldsymbol\omega + (\boldsymbol\omega\times\mathbf{GP})\cdot\boldsymbol\omega \quad &\text{(dot-multiply by the angular velocity)} \\
> &= \mathbf v_0^G\cdot\boldsymbol\omega \quad &\text{(a vector product is perpendicular to its factors)} \\
> \lvert\mathbf v_0^P\rvert^2 &= v_{0\parallel}^2 + \lvert\mathbf v_{0\perp}^P\rvert^2 \quad &\text{(right triangle: the parallel and perpendicular parts are the legs, the velocity is the hypotenuse)} \\
> &\geq v_{0\parallel}^2 \quad &\text{(the squared perpendicular part cannot be negative)} \\
> v_{0\parallel} &= \frac{\mathbf v_0^G\cdot\boldsymbol\omega}{\omega} \quad &\text{(component along the unit vector of the angular velocity)} \\
> &= \frac{(8)(1) + (4)(1) + (0)(1)}{\sqrt3} \quad &\text{(data and the previous box)} \\
> &= \frac{12}{\sqrt3} = 4\sqrt3 \quad &\text{(multiply numerator and denominator by $\sqrt3$)}
> \end{aligned}$$
>
> $$\boxed{v_{\min} = v_{0\parallel} = 4\sqrt3\ \mathrm{m/s} \approx 6.93\ \mathrm{m/s},\qquad \mathbf v_{0\parallel} = 4\,\mathbf i + 4\,\mathbf j + 4\,\mathbf k\ \ \mathrm{m/s}}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm{T^{-1}}]/[\mathrm{T^{-1}}] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** no point of the spacecraft moves slower than about 6.93 m/s. The minimum is reached where the perpendicular part vanishes, that is, on the instantaneous axis of rotation and slip; the motion is a screw motion about that axis.

> [!derivation] Where the minimum is reached: a point of the instantaneous axis
> **Law:** foot of the perpendicular from $G$ to the axis
> **Source:** Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 9.11
>
> $$\begin{aligned}
> \mathbf{GI} &= \frac{\boldsymbol\omega\times\mathbf v_0^G}{\omega^2} \quad &\text{(Eq. 9.10, obtained by cross-multiplying the velocity field by the angular velocity)} \\
> \boldsymbol\omega\times\mathbf v_0^G &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 1 & 1 & 1 \cr 8 & 4 & 0 \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\,(1\cdot 0 - 1\cdot 4) - \mathbf j\,(1\cdot 0 - 1\cdot 8) + \mathbf k\,(1\cdot 4 - 1\cdot 8) \quad &\text{(expand along the first row)} \\
> &= -4\,\mathbf i + 8\,\mathbf j - 4\,\mathbf k \quad &\text{(carry out the products)} \\
> \mathbf{GI} &= \frac13\,(-4\,\mathbf i + 8\,\mathbf j - 4\,\mathbf k) \quad &\text{(divide by the squared modulus, 3)}
> \end{aligned}$$
>
> $$\boxed{\mathbf r_0^I = -\frac43\,\mathbf i + \frac83\,\mathbf j - \frac43\,\mathbf k\ \ \mathrm m,\qquad \text{axis: } \mathbf r = \mathbf r_0^I + \lambda\,(\mathbf i + \mathbf j + \mathbf k)}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** the points of this line (which may lie outside the hull) are the ones that move at the minimum speed, along the line itself.

### Center of Mass and Inertia Tensor

This section does not apply: the centre of mass enters only as a tracked point, and no mass property is needed for the velocity field.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for.

### Free-Body Diagram and Equations of Motion

This section does not apply: the problem is a kinematic snapshot with no forces.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| (a) Compatibility | Yes. The three pairs satisfy the equal-projection condition and one angular velocity, $(1, 1, 1)$ rad/s, reproduces both velocity differences |
| (b) Minimum speed | $4\sqrt3 \approx 6.93$ m/s, the slip speed, reached on the instantaneous axis through $\left(-\tfrac43, \tfrac83, -\tfrac43\right)$ m with direction $(1, 1, 1)$ |

`Problems.pdf` prints no answer for this problem, so the result is checked by substitution and with limiting cases.

> [!derivation] Check: velocity of the point I
> **Law:** velocity field from $G$ to $I$ with the values found
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.11
>
> $$\begin{aligned}
> \boldsymbol\omega\times\mathbf{GI} &= \frac13\begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr 1 & 1 & 1 \cr -4 & 8 & -4 \end{vmatrix} \quad &\text{(determinant form, common factor taken out)} \\
> &= \frac13\left[\mathbf i\,(1\cdot(-4) - 1\cdot 8) - \mathbf j\,(1\cdot(-4) - 1\cdot(-4)) + \mathbf k\,(1\cdot 8 - 1\cdot(-4))\right] \quad &\text{(expand along the first row)} \\
> &= \frac13\,(-12\,\mathbf i + 0\,\mathbf j + 12\,\mathbf k) = -4\,\mathbf i + 4\,\mathbf k \quad &\text{(carry out the products and divide)} \\
> \mathbf v_0^I &= (8\,\mathbf i + 4\,\mathbf j) + (-4\,\mathbf i + 4\,\mathbf k) \quad &\text{(velocity of $G$ plus the product above)} \\
> &= 4\,\mathbf i + 4\,\mathbf j + 4\,\mathbf k \quad &\text{(add component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^I = 4\,(\mathbf i + \mathbf j + \mathbf k)\ \ \mathrm{m/s} = \mathbf v_{0\parallel}}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** the velocity of $I$ is parallel to the angular velocity and has modulus $4\sqrt3$ m/s, the minimum found in part (b).

**Limiting cases and consistency:**

* **Comparison with the measured points.** The speeds of $G$, $A$ and $C$ are about 8.94, 7.48 and 14.14 m/s, all above the minimum of 6.93 m/s, as they must be.
* **Same slip speed from the other points.** The scalar products of the velocities of $A$ and $C$ with the angular velocity are 12 and 12 (4 + 2 + 6 and 10 − 6 + 8), equal to that of $G$.
* **If the scalar product of the velocity of $G$ with the angular velocity were zero,** the minimum speed would be zero: the motion would be a pure rotation and the points of the axis would be at rest.
* **If one measured component were changed** (for example the third component of the velocity of $C$), the two conditions that fix the second component of the angular velocity would disagree and no angular velocity would exist: the object would not be moving as a rigid body.

---

## Problem RB-01: Kinematics (3 points)

### Reference Frames, Bases and Degrees of Freedom

* **Physical system:** one rigid body observed at a single instant. The velocities of three of its points, each on one coordinate axis at the same distance $a$ from the origin, are known.
* **Fixed frame:** $S_0$ is the frame $Oxyz$ of the statement, with origin $O$ and right-handed basis $\{\mathbf i, \mathbf j, \mathbf k\}$.
* **Body frame:** not needed; every vector is written in the fixed basis at the given instant.
* **Degrees of freedom:** six for a free rigid body. The nine velocity components of the statement contain three redundant data, which must satisfy the rigidity conditions.

| Point | Position | Velocity | SI units |
| :--- | :--- | :--- | :--- |
| $A$ | $(a, 0, 0)$ | $v_0\,(0, 1, 0)$ | m, m/s |
| $B$ | $(0, a, 0)$ | $v_0\,(0, 1, 1)$ | m, m/s |
| $C$ | $(0, 0, a)$ | $v_0\,(1, 1, 1)$ | m, m/s |

* **Unknowns:** the angular velocity of the body, its slip velocity (if any), the instantaneous axis, and the minimum speed among all body points.

### Change of Basis, Position Vectors and Constraint Kinematics

No change of basis is needed. The figure shows the three points, their velocities and the triangle they form.

![[attachments/EM-SOL/rb01-three-points.svg]]

> [!derivation] Relative positions and velocity differences
> **Law:** subtraction of vectors component by component in the fixed basis
> **Source:** Problems.pdf, p. 37; Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf{AB} &= (0, a, 0) - (a, 0, 0) = (-a, a, 0) \quad &\text{(head minus tail)} \\
> \mathbf{AC} &= (0, 0, a) - (a, 0, 0) = (-a, 0, a) \quad &\text{(head minus tail)} \\
> \mathbf{BC} &= (0, 0, a) - (0, a, 0) = (0, -a, a) \quad &\text{(head minus tail)} \\
> \mathbf v_0^B - \mathbf v_0^A &= v_0\,(0, 1, 1) - v_0\,(0, 1, 0) = v_0\,(0, 0, 1) \quad &\text{(component by component)} \\
> \mathbf v_0^C - \mathbf v_0^A &= v_0\,(1, 1, 1) - v_0\,(0, 1, 0) = v_0\,(1, 0, 1) \quad &\text{(component by component)} \\
> \mathbf v_0^C - \mathbf v_0^B &= v_0\,(1, 1, 1) - v_0\,(0, 1, 1) = v_0\,(1, 0, 0) \quad &\text{(component by component)}
> \end{aligned}$$
>
> $$\boxed{\mathbf{AB} = a\,(-1, 1, 0),\qquad \mathbf{AC} = a\,(-1, 0, 1),\qquad \mathbf{BC} = a\,(0, -1, 1)}$$
>
> **Units:** positions in $[\mathrm L]$, velocity differences in $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the three points are the vertices of an equilateral triangle of side $a\sqrt2$; they are not collinear, so their velocities fix the field.

> [!derivation] Rigidity test on the three sides
> **Law:** equal projections of the velocities of two body points on the segment that joins them
> **Source:** Notes.pdf, Eq. 9.7; [Lecture 7, Slide 7]
>
> $$\begin{aligned}
> (\mathbf v_0^B - \mathbf v_0^A)\cdot\mathbf{AB} &= v_0 a\,[(0)(-1) + (0)(1) + (1)(0)] = 0 \quad &\text{(side $AB$)} \\
> (\mathbf v_0^C - \mathbf v_0^A)\cdot\mathbf{AC} &= v_0 a\,[(1)(-1) + (0)(0) + (1)(1)] = 0 \quad &\text{(side $AC$)} \\
> (\mathbf v_0^C - \mathbf v_0^B)\cdot\mathbf{BC} &= v_0 a\,[(1)(0) + (0)(-1) + (0)(1)] = 0 \quad &\text{(side $BC$)}
> \end{aligned}$$
>
> $$\boxed{(\mathbf v_0^B - \mathbf v_0^A)\cdot\mathbf{AB} = (\mathbf v_0^C - \mathbf v_0^A)\cdot\mathbf{AC} = (\mathbf v_0^C - \mathbf v_0^B)\cdot\mathbf{BC} = 0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}][\mathrm L] = [\mathrm{L^2\,T^{-1}}]$
> **Meaning:** the three sides of the triangle keep their length, so the data can belong to a rigid body.

> [!derivation] Angular velocity from the pairs A, B and A, C
> **Law:** velocity field of a rigid body, with the vector products expanded by their determinants
> **Source:** Notes.pdf, Eq. 9.3; Notes.pdf, Eq. 9.12; Notes.pdf, Eq. 9.13; Notes.pdf, Eq. 1.31
>
> $$\begin{aligned}
> \boldsymbol\omega\times\mathbf{AB} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -a & a & 0 \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\,(\omega_y\cdot 0 - \omega_z a) - \mathbf j\,(\omega_x\cdot 0 + \omega_z a) + \mathbf k\,(\omega_x a + \omega_y a) \quad &\text{(expand along the first row)} \\
> &= -a\omega_z\,\mathbf i - a\omega_z\,\mathbf j + a(\omega_x + \omega_y)\,\mathbf k \quad &\text{(carry out the products)} \\
> -a\omega_z &= 0,\quad a(\omega_x + \omega_y) = v_0 \quad &\text{(equate to $v_0\,\mathbf k$, the difference for the pair $A$, $B$)} \\
> \boldsymbol\omega\times\mathbf{AC} &= \begin{vmatrix} \mathbf i & \mathbf j & \mathbf k \cr \omega_x & \omega_y & \omega_z \cr -a & 0 & a \end{vmatrix} \quad &\text{(determinant form)} \\
> &= \mathbf i\,(\omega_y a - \omega_z\cdot 0) - \mathbf j\,(\omega_x a + \omega_z a) + \mathbf k\,(\omega_x\cdot 0 + \omega_y a) \quad &\text{(expand along the first row)} \\
> &= a\omega_y\,\mathbf i - a(\omega_x + \omega_z)\,\mathbf j + a\omega_y\,\mathbf k \quad &\text{(carry out the products)} \\
> a\omega_y &= v_0,\quad -a(\omega_x + \omega_z) = 0 \quad &\text{(equate to $v_0\,(\mathbf i + \mathbf k)$, the difference for the pair $A$, $C$)} \\
> \omega_z &= 0,\quad \omega_y = \frac{v_0}{a},\quad \omega_x = -\omega_z = 0 \quad &\text{(solve the four conditions)} \\
> a\left(0 + \frac{v_0}{a}\right) &= v_0 \quad &\text{(the remaining condition of the pair $A$, $B$ is satisfied)}
> \end{aligned}$$
>
> $$\boxed{\boldsymbol\omega = \frac{v_0}{a}\,\mathbf j}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]/[\mathrm L] = [\mathrm{T^{-1}}]$
> **Meaning:** the body turns about a direction parallel to the second axis, counterclockwise when seen from the positive end of that axis, at the rate $v_0/a$.

![[attachments/EM-SOL/rb01-view-along-omega.svg]]

> [!derivation] Slip velocity and minimum speed
> **Law:** the velocity component along the angular velocity is common to all body points and is the smallest speed in the body
> **Source:** Notes.pdf, Eq. 9.5; Notes.pdf, Eq. 9.6; Notes.pdf, Eq. 9.11; [Lecture 7, Slide 9]
>
> For any body point $P$:
>
> $$\begin{aligned}
> \mathbf e_\omega &= \frac{\boldsymbol\omega}{\omega} = \mathbf j \quad &\text{(unit vector of the angular velocity)} \\
> v_{0\parallel} &= \mathbf v_0^A\cdot\mathbf e_\omega = v_0\,[(0)(0) + (1)(1) + (0)(0)] = v_0 \quad &\text{(component of the velocity of $A$ along it)} \\
> \mathbf v_0^B\cdot\mathbf e_\omega &= v_0,\quad \mathbf v_0^C\cdot\mathbf e_\omega = v_0 \quad &\text{(second components of the data: the same value, as Eq. 9.5 requires)} \\
> \lvert\mathbf v_0^P\rvert^2 &= v_{0\parallel}^2 + \lvert\mathbf v_{0\perp}^P\rvert^2 \geq v_{0\parallel}^2 \quad &\text{(right triangle with the parallel and perpendicular parts as legs)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_{0\parallel} = v_0\,\mathbf j \neq \mathbf 0,\qquad v_{\min} = v_0}$$
>
> **Units:** $[\mathrm{L\,T^{-1}}]$
> **Meaning:** the body does have a slip velocity: it advances along the direction of its angular velocity while it turns, so the motion is a screw motion and there is an instantaneous axis of rotation and slip, not of pure rotation. No body point moves slower than $v_0$.

> [!derivation] Position of the instantaneous axis
> **Law:** foot of the perpendicular from $A$ to the axis, obtained by cross-multiplying the velocity field by the angular velocity
> **Source:** Notes.pdf, Eq. 9.9; Notes.pdf, Eq. 9.10; Notes.pdf, Eq. 9.11
>
> $$\begin{aligned}
> \mathbf{AI} &= \frac{\boldsymbol\omega\times\mathbf v_0^A}{\omega^2} \quad &\text{(Eq. 9.10)} \\
> \boldsymbol\omega\times\mathbf v_0^A &= \frac{v_0}{a}\,\mathbf j\times v_0\,\mathbf j \quad &\text{(values found and data)} \\
> &= \mathbf 0 \quad &\text{(the vector product of parallel vectors vanishes)} \\
> \mathbf{AI} &= \mathbf 0 \quad &\text{(so the foot $I$ is the point $A$ itself)}
> \end{aligned}$$
>
> $$\boxed{\text{axis: } \mathbf r = a\,\mathbf i + \lambda\,\mathbf j \quad (\text{the line through } A \text{ parallel to } \mathbf j)}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm{L\,T^{-1}}]/[\mathrm{T^{-2}}] = [\mathrm L]$
> **Meaning:** the velocity of $A$ is already parallel to the angular velocity, so $A$ has no perpendicular part and lies on the axis. The axis is the line through $A$ parallel to the second coordinate axis.

### Center of Mass and Inertia Tensor

This section does not apply: the problem is purely kinematic.

### Linear Momentum, Angular Momentum and Kinetic Energy

This section does not apply: no momentum or energy is asked for.

### Free-Body Diagram and Equations of Motion

This section does not apply: the statement gives the motion at one instant and no forces.

### Answers and Checks

| Asked | Answer |
| :--- | :--- |
| Instantaneous axis | The line through $A$ with the direction of $\mathbf j$ |
| Slip velocity | Yes: $v_0\,\mathbf j$, so the axis is one of rotation and slip (screw motion) |
| Angular velocity | $(v_0/a)\,\mathbf j$ |
| Minimum speed | $v_0$, reached at the points of the axis (for example $A$) |

**Check against the official key:** the key (Problems.pdf, p. 77) prints a minimum speed $v_0$, the angular velocity $(v_0/a)\,\mathbf j$ and the axis as the line with the direction of $\mathbf j$ that passes through $A$. The three coincide with the results above.

> [!derivation] Check: the field found returns the three given velocities
> **Law:** velocity field from $A$ with the angular velocity found
> **Source:** Notes.pdf, Eq. 9.3
>
> $$\begin{aligned}
> \mathbf v_0^B &= v_0\,\mathbf j + \frac{v_0}{a}\,\mathbf j\times(-a\,\mathbf i + a\,\mathbf j) \quad &\text{(field from $A$ to $B$)} \\
> &= v_0\,\mathbf j - v_0\,(\mathbf j\times\mathbf i) \quad &\text{(the product of $\mathbf j$ with itself is zero)} \\
> &= v_0\,\mathbf j + v_0\,\mathbf k \quad &\text{(right-handed basis: $\mathbf j\times\mathbf i$ is $-\mathbf k$)} \\
> \mathbf v_0^C &= v_0\,\mathbf j + \frac{v_0}{a}\,\mathbf j\times(-a\,\mathbf i + a\,\mathbf k) \quad &\text{(field from $A$ to $C$)} \\
> &= v_0\,\mathbf j + v_0\,\mathbf k + v_0\,\mathbf i \quad &\text{($\mathbf j\times\mathbf i$ is $-\mathbf k$ and $\mathbf j\times\mathbf k$ is $\mathbf i$)}
> \end{aligned}$$
>
> $$\boxed{\mathbf v_0^B = v_0\,(\mathbf j + \mathbf k),\qquad \mathbf v_0^C = v_0\,(\mathbf i + \mathbf j + \mathbf k)}$$
>
> **Units:** $[\mathrm{T^{-1}}][\mathrm L] = [\mathrm{L\,T^{-1}}]$
> **Meaning:** both are the velocities of the statement, so the angular velocity is the only one compatible with the data.

**Limiting cases and consistency:**

* **Speeds against distances to the axis.** $B$ and $C$ are at the distances $a$ and $a\sqrt2$ from the axis; their perpendicular speeds, $v_0$ and $v_0\sqrt2$, are the angular speed times those distances.
* **Without the common second component.** If the three given velocities had no component along $\mathbf j$, the differences between them, and therefore the angular velocity, would be the same, and the same axis would be one of pure rotation with $A$ at rest.
* **Dimensions.** The angular velocity is a speed divided by a length, in rad/s.
